#!/usr/bin/env python3
"""
Detector 2.0 mechanical pattern lint + parallel-structure / denial-gap detectors.

Scope (deliberately narrow): only implements checks that are decidable from
surface form (word lists, regex, line-diff) without semantic judgment. Flags
that require judging "does this vague phrase have a concrete event-trace
nearby" (vague_deixis, truncation white-list) or "is this cliche used
ironically" (banal_rhyme framing) or "does the closure read as earned"
(school_arc) are NOT implemented here -- they need a human/model read of
context, not a lint rule. See README section at bottom for the exact list.

Usage:
  python3 scripts/lint_patterns.py [files...]      # lint given files
  python3 scripts/lint_patterns.py --self-test      # run golden-corpus regression

Exit code: 0 if no hard-fail flags found (or self-test passes), 1 otherwise.
All non-hard-fail flags are printed as warnings and do not affect exit code,
matching validate.py's existing pattern of hard structural gates only.
"""
import re
import sys
import os
import difflib

KB_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# §25 mechanical patterns (weight, from songwriting/ru/detector-2.0.md)
# ---------------------------------------------------------------------------

KANTSELYARIT_RE = re.compile(
    r"\b(явля(ется|ются|лся)|данн(ый|ая|ое|ые)|осуществля\w*|в рамках|стоит отметить)\b",
    re.IGNORECASE,
)

# Curated closed list from G-04/G-09 examples. Genitive-metaphor and
# genre-autopilot are open-ended in principle, but the KB only cites closed
# examples, so we lint against the cited set and let the issue tracker grow
# it deliberately (same pattern as the denial-verb list below) rather than
# guessing a fuzzy semantic rule that would drift from the canon docs.
GENITIVE_METAPHOR_RE = re.compile(
    r"\b(осколки?|тени|нити|эхо|отблески?|искры)\s+(памяти|прошлого|судьбы|души|мечты)\b",
    re.IGNORECASE,
)

GENRE_AUTOPILOT_PHRASES = [
    r"неон\w*", r"город\s+спит", r"по\s+венам\s+ток", r"туман\w*\s+над\s+рекой",
    r"ворон\w*\s+круж\w*", r"древн\w*\s+лес\w*\s+хран\w*", r"кровь\s+предков",
]
GENRE_AUTOPILOT_RE = re.compile("|".join(GENRE_AUTOPILOT_PHRASES), re.IGNORECASE)

# Abstract-noun triad: three comma/и-joined nouns from a curated abstract set.
ABSTRACT_NOUNS = [
    "боль", "страх", "пустота", "тоска", "печаль", "тьма", "холод", "мрак",
    "надежда", "вера", "судьба", "память", "потеря", "любовь",
]
_noun_alt = "|".join(ABSTRACT_NOUNS)
TRIPLE_RHETORIC_RE = re.compile(
    rf"\b({_noun_alt}),\s+({_noun_alt})\s+и\s+({_noun_alt})\b", re.IGNORECASE
)

# chorus_checklist: "мы будем X, мы будем Y(, мы будем Z...)" with >=3
# interchangeable-verb repeats of the same frame in a tight span (weight 2.0,
# hard-fail per detector-2.0.md).
CHORUS_CHECKLIST_RE = re.compile(
    r"(мы\s+будем\s+\w+[,.]?\s*){3,}", re.IGNORECASE
)

# ---------------------------------------------------------------------------
# Denial-gap (issue #5): extended verb list. anti-patterns.md rule: a denial
# construction ("я не X") is legal at most ONCE per text; a second occurrence
# is a flag. Original list missed "звал" (caught manually in PRE-008 REPAIR).
# ---------------------------------------------------------------------------
DENIAL_VERBS = [
    "боюсь", "сдаюсь", "плачу", "жалею", "жду", "ждал", "ждала",
    "верю", "верил", "верила", "надеюсь", "надеялся", "надеялась",
    "молю", "молился", "молилась", "прошу", "просил", "просила",
    "звал", "звала", "зову", "помню", "помнил", "помнила",
    "забуду", "забыл", "забыла", "сплю", "спал", "спала",
]
DENIAL_RE = re.compile(
    r"\bя\s+не\s+(" + "|".join(DENIAL_VERBS) + r")\b", re.IGNORECASE
)


def check_denial_gap(text):
    """anti-patterns.md §B: denial construction legal <= 1 time per text."""
    matches = DENIAL_RE.findall(text)
    if len(matches) > 1:
        return [("denial_gap", 1.0, f"{len(matches)} denial constructions (max 1): {matches}")]
    return []


def check_em_dash_cascade(text):
    """Flag >=2 dash-insertions within a single sentence/clause, not merely a
    single physical line. A line holding two independent short sentences
    that each use one dash (parcelling / цветаевский режим, see G-14 and
    the CW-001 canon text «раз — и тьма. раз — и тьма.») is NOT a cascade --
    splitting on sentence-ending punctuation first avoids that false positive
    while still catching a real cascade like «это — не тишина, а — ожидание —
    и страх».
    """
    flags = []
    for i, line in enumerate(text.splitlines(), 1):
        for clause in re.split(r"(?<=[.!?])\s+", line.strip()):
            if clause.count("—") >= 2:
                flags.append(("em_dash_cascade", 0.5, f"line {i}: {clause!r}"))
                break
    return flags


def check_kantselyarit(text):
    hits = KANTSELYARIT_RE.findall(text)
    return [("kantselyarit", 1.5, f"{len(hits)} hits")] if hits else []


def check_genitive_metaphor(text):
    hits = GENITIVE_METAPHOR_RE.findall(text)
    return [("genitive_metaphor", 1.5, f"{len(hits)}x") for _ in [0]] if hits else []


def check_triple_rhetoric(text):
    hits = TRIPLE_RHETORIC_RE.findall(text)
    return [("triple_rhetoric", 0.5, str(h)) for h in hits]


def check_genre_autopilot(text):
    hits = GENRE_AUTOPILOT_RE.findall(text)
    return [("genre_autopilot", 1.0, f"{len(hits)}x")] if hits else []


def check_chorus_checklist(text):
    hits = CHORUS_CHECKLIST_RE.findall(text)
    return [("chorus_checklist", 2.0, "repeated мы будем X frame >=3x")] if hits else []


# ---------------------------------------------------------------------------
# parallel_shift_candidate (issue #3): mechanical *detector*, not a verdict.
# Finds pairs of repeated multi-line blocks (e.g. two pre-chorus instances)
# that are near-identical, and surfaces them for the 25.27 white-list review
# (is the differing word semantically accumulating -- G-11 -- or is the whole
# frame just interchangeable filler -- G-06/chorus_checklist). We do NOT
# auto-verdict this because that distinction is semantic; we only guarantee
# the bug class (PRE-003/004 pre-chorus repeat) can no longer pass silently.
# ---------------------------------------------------------------------------
def check_parallel_shift_candidate(text, block_lines=2, min_len=8):
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    flags = []
    seen_spans = set()
    for i in range(len(lines) - block_lines + 1):
        block_a = lines[i : i + block_lines]
        if any(len(l) < min_len for l in block_a):
            continue
        for j in range(i + block_lines, len(lines) - block_lines + 1):
            if (i, j) in seen_spans:
                continue
            block_b = lines[j : j + block_lines]
            ratio = difflib.SequenceMatcher(
                None, "\n".join(block_a), "\n".join(block_b)
            ).ratio()
            # near-identical (>=0.85) but not byte-identical duplicate lines
            # (verbatim repeat choruses are intentional, not a shift bug) --
            # only flag when there IS a difference (ratio < 1.0) that's small.
            if 0.85 <= ratio < 1.0:
                seen_spans.add((i, j))
                flags.append((
                    "parallel_shift_candidate",
                    0.0,  # advisory only, not scored -- needs human 25.27 check
                    f"lines {i+1}-{i+block_lines} vs {j+1}-{j+block_lines} "
                    f"(similarity {ratio:.2f}): review against 25.27 white-list "
                    f"(does the differing word accumulate meaning, or is it filler?)",
                ))
    return flags


MECHANICAL_CHECKS = [
    check_denial_gap,
    check_em_dash_cascade,
    check_kantselyarit,
    check_genitive_metaphor,
    check_triple_rhetoric,
    check_genre_autopilot,
    check_chorus_checklist,
]

ADVISORY_CHECKS = [check_parallel_shift_candidate]

HARD_FAIL_WEIGHT = 2.0


def lint_text(text):
    flags = []
    for check in MECHANICAL_CHECKS:
        flags.extend(check(text))
    advisories = []
    for check in ADVISORY_CHECKS:
        advisories.extend(check(text))
    return flags, advisories


def lint_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return lint_text(text)


def _extract_golden_corpus_cases(md_text):
    """Parse references/golden_corpus.md: returns {case_id: (code_block_text, expected_flag_names)}."""
    cases = {}
    case_blocks = re.split(r"### (G-\d+)", md_text)
    # case_blocks: [preamble, 'G-01', body1, 'G-02', body2, ...]
    for k in range(1, len(case_blocks), 2):
        case_id = case_blocks[k]
        body = case_blocks[k + 1]
        code_match = re.search(r"```\n(.*?)\n```", body, re.DOTALL)
        code = code_match.group(1) if code_match else ""
        cases[case_id] = code

    # Parse the summary table at the bottom for expected flag names.
    expected = {}
    table_match = re.search(
        r"## Сводная таблица ожиданий\n\n(.*?)\n\n-", md_text, re.DOTALL
    )
    table = table_match.group(1) if table_match else ""
    for line in table.splitlines():
        m = re.match(r"\|\s*(G-\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|", line)
        if m:
            case_id, flags_cell, _verdict = m.groups()
            names = re.findall(r"[a-z_]+(?=\s*(?:×\d+)?)", flags_cell)
            expected[case_id] = set(n for n in names if n not in ("×",))
    return cases, expected


IMPLEMENTED_FLAG_NAMES = {
    "kantselyarit", "genitive_metaphor", "em_dash_cascade", "triple_rhetoric",
    "genre_autopilot", "chorus_checklist",
}


def self_test():
    corpus_path = os.path.join(KB_DIR, "references", "golden_corpus.md")
    with open(corpus_path, encoding="utf-8") as f:
        md_text = f.read()
    cases, expected = _extract_golden_corpus_cases(md_text)

    failures = []
    for case_id, code in sorted(cases.items()):
        flags, _advisories = lint_text(code)
        got_names = {name for name, _w, _detail in flags}
        want_names = expected.get(case_id, set()) & IMPLEMENTED_FLAG_NAMES
        # Only compare on the subset of flags we actually implement --
        # unimplemented flags (banal_rhyme, vague_deixis, school_arc,
        # sentiment_flatline, tech_metaphor, truncation, perfect_grammar,
        # parallel_no_shift verdict) are explicitly out of scope, see module
        # docstring. We still check we don't fire flags we DO implement when
        # they're not expected (false positive), and that we DO fire flags
        # that ARE expected and implemented (false negative).
        implemented_got = got_names & IMPLEMENTED_FLAG_NAMES
        if implemented_got != want_names:
            failures.append(
                f"{case_id}: expected {sorted(want_names)}, got {sorted(implemented_got)}"
            )

    if failures:
        print(f"SELF-TEST FAIL: {len(failures)}/{len(cases)} cases mismatched")
        for f in failures:
            print(f"  ✗ {f}")
        return 1
    print(f"SELF-TEST OK: {len(cases)} golden-corpus cases match on implemented flags "
          f"({', '.join(sorted(IMPLEMENTED_FLAG_NAMES))})")
    return 0


def main():
    args = sys.argv[1:]
    if not args or args == ["--self-test"]:
        sys.exit(self_test())

    exit_code = 0
    for path in args:
        flags, advisories = lint_file(path)
        hard_fail = [f for f in flags if f[1] >= HARD_FAIL_WEIGHT]
        if flags or advisories:
            print(f"{path}:")
            for name, weight, detail in flags:
                marker = "HARD-FAIL" if weight >= HARD_FAIL_WEIGHT else "warn"
                print(f"  [{marker}] {name} (w={weight}): {detail}")
            for name, _weight, detail in advisories:
                print(f"  [advisory] {name}: {detail}")
        if hard_fail:
            exit_code = 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------
# Out of scope (needs semantic/contextual judgment, not a lint rule):
#   - vague_deixis: requires checking neighbouring 1-2 lines for a concrete,
#     "photographable" event trace (§25.27 умолчания criterion).
#   - truncation white-list: same event-trace judgment, formulaic-section-only.
#   - banal_rhyme conscious-framing: requires judging authorial irony.
#   - school_arc: requires judging whether the closing line is an earned
#     action/image vs a stated moral.
#   - sentiment_flatline: requires judging overall tonal register, not
#     matchable by a fixed word list without heavy false positives.
#   - tech_metaphor dual-read: requires judging whether a second, literal
#     reading exists for the metaphor.
#   - parallel_no_shift final verdict: this script only *detects candidates*
#     (see check_parallel_shift_candidate); the shift-vs-filler call in
#     §25.27 stays a human/model REPAIR-review step.
# ---------------------------------------------------------------------------

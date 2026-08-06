#!/usr/bin/env python3
"""
Detector 2.0 mechanical pattern lint + parallel-structure / denial-gap detectors.

Scope (deliberately narrow): only implements checks that are decidable from
surface form (word lists, regex, line-diff) without semantic judgment. Flags
that require judging "does this vague phrase have a concrete event-trace
nearby" (vague_deixis, and the omission side of truncation) or "is this cliche used
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

# ---------------------------------------------------------------------------
# marker_word / organ_cliche (issue #4): sourced verbatim from the canonical
# machine-readable detector block, songwriting/encyclopedia.md §30.2
# (`detector.marker_words`, `detector.organ_cliches_regex`), weights from
# `detector.weights.marker_word` (1.0) and `.organ_cliche` (1.5). Both are
# closed word/regex lists with no "is it earning its place" judgment call,
# unlike vague_deixis/school_arc/etc., so they are safe as mechanical checks.
# "прекрасный" and "глубокий" are deliberately excluded from the closed list:
# §30.2/§16.1 marks them as filler-ONLY markers whose flag-worthiness depends
# on sentence role (descriptive work vs. padding) -- exactly the semantic
# judgment this module's docstring says is out of scope. The remaining
# words/phrases below are flagged unconditionally with no such caveat.
# ---------------------------------------------------------------------------
MARKER_WORDS = [
    "вечность", "бесконечность", "симфония", "гармония", "мелодия души",
    "навсегда", "навечно", "бесконечный путь", "вечный",
    "непостижимый", "загадочный", "волшебный", "магический",
    "чудесный", "дивный", "неземной", "космический",
    "как никогда ранее", "ничто не могло подготовить",
]
MARKER_WORD_RE = re.compile(
    r"\b(" + "|".join(re.escape(w) for w in MARKER_WORDS) + r")\b", re.IGNORECASE
)

ORGAN_CLICHE_RE = re.compile(
    r"\bсердце\s+(бьётся|колотится|рвётся|кричит|плачет)\b"
    r"|\bдуша\s+(рвётся|кричит|плачет|горит|болит)\b",
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# not_x_but_y (issue #4, follow-up pass): §30.2 detector.constructions.not_x_but_y
# gives three regex alternatives. We implement ONLY the first, most specific
# one -- "не просто X — это был(о/а) Y" (the literal formula named in
# §16.3: «Формула «Это было не просто X — это было Y»: AI-слоуп чистой
# воды»). The other two spec alternatives are deliberately NOT implemented:
#   - "это не X — это Y" (generic redefinition) is a common REAL poetic
#     device (rhetorical restatement), not just AI-slop -- flagging it
#     unconditionally would false-positive on legitimate craft.
#   - "не X а Y" (bare) matches ordinary Russian grammar constantly (e.g.
#     "не сплю, а работаю") and is far too broad to be a mechanical rule.
# The implemented pattern requires the specific redundant-copula echo
# ("это был/это было/это была" restating "это было" from the setup) which
# is the actual tell of the AI formula, not just any "не X, а Y" contrast.
# ---------------------------------------------------------------------------
NOT_X_BUT_Y_RE = re.compile(
    r"не\s+просто\s+[^.!?—\n]{1,80}—\s*это\s+бы(?:ло|л|ла)\b",
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# position_explanation (issue #4, 4th pass): §30.2
# detector.constructions.position_explanation, weight 1.5. Closed list of
# literal phrases where the narrator stops the song to explain their moral
# standing instead of showing it through action. Safe as a mechanical check
# for the same reason organ_cliche is: it fires on an exact canonical
# phrase, not on a semantic category, so there is no "is it earned here"
# judgment call hidden in the rule.
# Both ё and е spellings of "я помню всё" are accepted: dropping ё is
# routine in Russian typing, so the е-form is the same phrase rather than a
# broadening of the closed list. Nothing else is added to the spec list --
# a bare "я помню" or "судить" elsewhere in a line must NOT fire (see G-22).
# ---------------------------------------------------------------------------
POSITION_EXPLANATION_PHRASES = [
    "я не сужу", "не мне судить", "я помню всё", "я помню все",
    "я не берусь объяснить", "не мне решать",
]
POSITION_EXPLANATION_RE = re.compile(
    r"\b(?:"
    + "|".join(
        r"\s+".join(re.escape(word) for word in phrase.split())
        for phrase in POSITION_EXPLANATION_PHRASES
    )
    + r")\b",
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# truncation (issue #4, 5th pass): §25.13 / §30.2 detector, weight 2.0, i.e.
# hard-fail tier. Closed list of the four canonical "I am not going to finish
# this scene" markers.
# This closed-list form is the ONLY safe way to mechanize truncation. The
# semantic version of the rule ("the text stops before the event happens")
# collides head-on with the 25.27 white-list, where an omission that leaves a
# trace in the text is a legal device -- see G-01 (лёд так и не встал) and
# G-10 (никто не звал). A semantic truncation rule would hard-fail both of
# them, so we do not judge omission at all: we only catch the narrator's
# explicit cop-out formulas.
# Dash tokens accept —, – and - because the same marker gets typed with any
# of them, and the leading ellipsis of "…дальше — позже" is optional for the
# same reason ("...", "…" or nothing at all).
# ---------------------------------------------------------------------------
TRUNCATION_PHRASES = [
    "[Продолжение следует",
    "Потом было",
    "…дальше — позже",
    "но это уже другая история",
]
_DASH_TOKENS = ("—", "–", "-")
_DASH_CLASS = r"[—–-]"
_OPTIONAL_ELLIPSIS = r"(?:…|\.\.\.)?\s*"


def _truncation_pattern(phrase):
    body = phrase
    prefix = ""
    if body.startswith("…"):
        body = body[1:]
        prefix = _OPTIONAL_ELLIPSIS
    tokens = [
        _DASH_CLASS if word in _DASH_TOKENS else re.escape(word)
        for word in body.split()
    ]
    return prefix + r"\s+".join(tokens)


TRUNCATION_RE = re.compile(
    r"(?<![А-Яа-яЁё])(?:"
    + "|".join(_truncation_pattern(phrase) for phrase in TRUNCATION_PHRASES)
    + r")(?![А-Яа-яЁё])",
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# tech_metaphor (issue #4, 6th pass): §25.2 / §30.2
# detector.tech_metaphors_regex, weight 2.0 -- hard-fail tier. This closes the
# last remaining false negative in the golden corpus: G-05 has expected this
# flag since the corpus was written.
# The spec writes each alternative as "<emotion noun>.*<tech token>". Taken
# literally that is unusable here and had to be narrowed in two ways, both
# because we lint whole texts rather than single lines:
#   1. The gap is bounded to the SAME line and to at most TECH_METAPHOR_GAP
#      characters. An unbounded ".*" would join an emotion noun in one clause
#      with an unrelated tech word far to the right -- e.g. G-05's "сердце"
#      and the "код" two lines below it are not one metaphor.
#   2. Tech tokens must start a word: the bare substring "лог" also lives
#      inside "диалог"/"монолог", which have nothing to do with logs, and at
#      weight 2.0 that false positive would cap a live text at SUSPECT.
# "слёзы" is accepted with ё and with е, and "перезагрузка чувств" is matched
# through its inflections ("перезагружаю чувства"), for the same reason the
# е-spelling is accepted in position_explanation: it is the same phrase, not a
# broadening of the closed list. Without this the canonical corpus example of
# the flag (G-05) would not fire at all.
# The spec's EXCEPTION ("tech lexicon as the hero's ground, not an emotion
# metaphor") is not decidable mechanically, but it is largely moot here: every
# alternative already requires an emotion noun next to the tech word, so a
# purely technical setting does not match -- see G-16 and G-26.
# ---------------------------------------------------------------------------
TECH_METAPHOR_TARGETS = [
    (r"сл[её]зы", ("формат", "WAV", "mp3", "файл")),
    (r"сердце", ("архив", "кэш", "лог", "облак", "код")),
    (r"душа", ("облак", "кэш", "сервер", "баз")),
    (r"любовь", ("кэш", "перезагруз", "файл")),
    (r"память", ("лог", "индекс", "баз")),
]
TECH_METAPHOR_LITERALS = [
    r"код\s+души",
    r"перезагру\w+\s+чувств\w*",
    r"файл\s+одиночества",
]
_CYRILLIC = r"[А-Яа-яЁё]"
TECH_METAPHOR_GAP = 40


def _tech_metaphor_patterns():
    patterns = []
    for noun, tech_tokens in TECH_METAPHOR_TARGETS:
        patterns.append(
            r"(?<!" + _CYRILLIC + r")" + noun
            + r"[^\n]{0," + str(TECH_METAPHOR_GAP) + r"}?"
            + r"(?<!" + _CYRILLIC + r")(?:" + "|".join(tech_tokens) + r")"
        )
    patterns.extend(TECH_METAPHOR_LITERALS)
    return patterns


TECH_METAPHOR_RE = re.compile("|".join(_tech_metaphor_patterns()), re.IGNORECASE)

# ---------------------------------------------------------------------------
# hypophora (issue #4, 7th pass): §30.2 detector.constructions pattern
# "line_ends_with_? AND next_line_answers", weight 1.5. The spec's own
# definition of "next_line_answers" is semantic (does the following line
# function as a reply to the question), which is exactly the kind of
# judgment call this module avoids -- see the docstring and the pre-existing
# backlog comment at the bottom of this file, which had hypophora on the
# deferred list for that reason.
# This pass narrows "answers" mechanically to the closed set of Russian
# causal-answer connectives that can ONLY function as an answer opener --
# "потому что", "оттого что", "затем что" -- there is no other syntactic
# role these three phrases play at the start of a line. The match is
# restricted to the immediate next physical line (no blank line in
# between), so a question at the end of one stanza followed by an unrelated
# new stanza does not fire.
# "просто" was deliberately excluded even though it is the most common
# informal AI-slop answer opener ("Почему? Просто устал.") because it is
# also an ordinary sentence adverb with no answer-marking role at all
# ("просто иду домой" as a fresh scene beat, not a reply) -- including it
# would need the same semantic judgment this rule exists to avoid.
# ---------------------------------------------------------------------------
HYPOPHORA_ANSWER_RE = re.compile(
    r"^\s*(?:потому\s+что|оттого\s+что|затем\s+что)\b", re.IGNORECASE
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


def check_marker_word(text):
    """§30.2 detector.marker_words, weight 1.0. Closed list, no filler-role
    judgment call (see module-level comment above the word list)."""
    hits = MARKER_WORD_RE.findall(text)
    return [("marker_word", 1.0, f"{len(hits)}x: {hits}")] if hits else []


def check_organ_cliche(text):
    """§30.2 detector.organ_cliches_regex, weight 1.5."""
    hits = ORGAN_CLICHE_RE.findall(text)
    return [("organ_cliche", 1.5, f"{len(hits)}x")] if hits else []


def check_not_x_but_y(text):
    """§30.2 detector.constructions.not_x_but_y, weight 1.5. Narrowed to the
    literal redundant-copula formula only -- see comment above NOT_X_BUT_Y_RE
    for why the other two spec regex alternatives are excluded."""
    hits = NOT_X_BUT_Y_RE.findall(text)
    return [("not_x_but_y", 1.5, f"{len(hits)}x")] if hits else []


def check_position_explanation(text):
    """§30.2 detector.constructions.position_explanation, weight 1.5. Closed
    literal phrase list (see comment above POSITION_EXPLANATION_PHRASES)."""
    hits = POSITION_EXPLANATION_RE.findall(text)
    return [("position_explanation", 1.5, f"{len(hits)}x")] if hits else []


def check_truncation(text):
    """§25.13 / §30.2 detector truncation, weight 2.0 (hard-fail tier). Closed
    literal marker list only -- see the comment above TRUNCATION_PHRASES for
    why the semantic reading of this rule is deliberately NOT implemented (it
    would hard-fail the 25.27 white-list cases G-01 and G-10)."""
    hits = TRUNCATION_RE.findall(text)
    return [("truncation", 2.0, f"{len(hits)}x")] if hits else []


def check_tech_metaphor(text):
    """§25.2 / §30.2 detector.tech_metaphors_regex, weight 2.0 (hard-fail
    tier). Closed regex list with a bounded same-line gap -- see the comment
    above TECH_METAPHOR_TARGETS for both narrowings and why each is
    required."""
    hits = TECH_METAPHOR_RE.findall(text)
    return [("tech_metaphor", 2.0, f"{len(hits)}x")] if hits else []


def check_hypophora(text):
    """§30.2 detector construction hypophora, weight 1.5. Mechanical
    narrowing of "next_line_answers" to a closed causal-connective set --
    see the comment above HYPOPHORA_ANSWER_RE for why "просто" is excluded
    and why the match requires the immediately adjacent physical line."""
    lines = text.splitlines()
    flags = []
    for i in range(1, len(lines)):
        prev_line = lines[i - 1].strip()
        curr_line = lines[i].strip()
        if prev_line.endswith("?") and HYPOPHORA_ANSWER_RE.match(curr_line):
            flags.append(
                ("hypophora", 1.5, f"line {i+1} answers question on line {i}: {curr_line!r}")
            )
    return flags


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
    check_marker_word,
    check_organ_cliche,
    check_not_x_but_y,
    check_position_explanation,
    check_truncation,
    check_tech_metaphor,
    check_hypophora,
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
    "genre_autopilot", "chorus_checklist", "marker_word", "organ_cliche",
    "not_x_but_y", "position_explanation", "truncation", "tech_metaphor",
    "hypophora",
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
        # sentiment_flatline, perfect_grammar,
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
#   - truncation as *omission*: the "text stops before the event" reading is
#     the same event-trace judgment as vague_deixis and stays out of scope --
#     it would hard-fail the 25.27 white-list cases G-01 and G-10. Only the
#     four literal cop-out markers of §25.13 are linted (check_truncation).
#   - banal_rhyme conscious-framing: requires judging authorial irony.
#   - school_arc: requires judging whether the closing line is an earned
#     action/image vs a stated moral.
#   - sentiment_flatline: requires judging overall tonal register, not
#     matchable by a fixed word list without heavy false positives.
#   - tech_metaphor's spec EXCEPTION (tech lexicon as the hero's ground
#     rather than an emotion metaphor): the closed regex list itself IS
#     linted (see check_tech_metaphor); only this semantic carve-out is not,
#     and it is largely moot because every alternative already requires an
#     emotion noun next to the tech word.
#   - hypophora's spec EXCEPTION (any line after a question that reads as an
#     answer): the closed causal-connective subset IS linted (see
#     check_hypophora); a broader semantic "does this line answer the
#     question" judgment is not, matching the same narrowing pattern as
#     tech_metaphor above.
#   - binary_light_dark / noun_stack / adj_pile / verb_rhyme /
#     uniform_line_length: §30.2 gives closed lists or regexes for these
#     too, but each carries a real false-positive risk on live text without
#     more corpus evidence or tooling we don't have (e.g. binary_light_dark's
#     own spec flags `frame_check: true`, meaning it needs to distinguish a
#     philosophical light/dark frame from a literal detail like a hallway
#     lamp -- not decidable from the regex alone; noun_stack/adj_pile need
#     POS tagging). Left for a follow-up pass, one flag at a time, each with
#     its own golden-corpus TP/FP pair per §0 protocol.
#     Promoted out of this list so far: not_x_but_y (narrowed to the literal
#     redundant-copula formula), position_explanation (closed phrase list),
#     truncation (closed marker list only, omission judgment excluded),
#     tech_metaphor (closed regex list with a bounded same-line gap) and
#     hypophora (closed causal-connective set, matched only on the
#     immediately adjacent physical line); each keeps the spec's flag name
#     but documents its narrowing next to the pattern definition.
# ---------------------------------------------------------------------------

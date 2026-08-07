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

Lyrics files (lyrics/<ID>.md, issue #14): if a file carries a "## Текст"
heading followed by a fenced block, ONLY that block is linted (card prose,
front-matter and notes are not lyrics and must not be swept). Front-matter
may declare `lint_exempt: [flag_name, ...]` together with a mandatory
`lint_exempt_note: <reason>`; an exemption without a note is itself a
hard-fail (lint_exempt_without_note). This is the legal exemption mechanism
for conscious devices (e.g. G-13's осознанная банальная рифма).

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

# ---------------------------------------------------------------------------
# banal_rhyme / verb_rhyme (issue #4, 8th pass): §25.10 / §16.4 / §30.2
# detector.banal_rhymes and detector.verb_rhymes, weights 1.0 each. Closed
# pair lists taken verbatim from §30.2.
# A pair counts only when BOTH words stand in rhyme position -- the final
# token of a line. The same words in the middle of a line are just
# vocabulary ("ночь стоит за окном ... я иду прочь" is not a rhyme, see
# G-30), and a naive whole-text word search would false-positive on living
# texts constantly. The final token is split on a hyphen because a
# line-ending compound like "любовь-морковь" (G-13) still puts its first
# part in rhyme position. ё/е are normalised ("слёзы" is typed both ways),
# same rationale as the е-spelling acceptance in position_explanation.
# banal_rhyme's own corpus TP is the pre-existing G-13 (осознанная пара
# «любовь/кровь» в поппанк-рамке): the flag fires there, and the
# «осознанно» discount (score weight P3 = 0.3) stays a scoring-layer
# concern, not a lint concern -- same separation as the
# parallel_shift_candidate advisory.
# ---------------------------------------------------------------------------
BANAL_RHYME_PAIRS = [
    ("любовь", "кровь"), ("любовь", "вновь"), ("кровь", "вновь"),
    ("ночь", "дочь"), ("ночь", "прочь"), ("дочь", "прочь"),
    ("пора", "гора"), ("слёзы", "грёзы"), ("беда", "звезда"),
    ("туман", "обман"), ("пожар", "пожал"),
]
VERB_RHYME_PAIRS = [
    ("любить", "забыть"), ("идти", "найти"), ("летать", "мечтать"),
    ("кричать", "молчать"), ("гореть", "тереть"), ("ждать", "бежать"),
]
_LINE_END_STRIP = ",.!?…:;—–-()[]«»\"'"


def _norm_token(token):
    return token.lower().replace("ё", "е")


def _line_end_tokens(text):
    """Collect the normalised rhyme-position token(s) of each line: the final
    whitespace token, stripped of surrounding punctuation, split on hyphen
    (a line-final compound still rhymes on its parts -- see G-13)."""
    tokens = []
    for line in text.splitlines():
        words = line.split()
        if not words:
            continue
        last = words[-1].strip(_LINE_END_STRIP)
        if not last:
            continue
        for part in last.split("-"):
            part = part.strip(_LINE_END_STRIP)
            if part:
                tokens.append(_norm_token(part))
    return tokens


def _rhyme_pair_hits(text, pairs):
    end_tokens = set(_line_end_tokens(text))
    return [(a, b) for a, b in pairs
            if _norm_token(a) in end_tokens and _norm_token(b) in end_tokens]


# ---------------------------------------------------------------------------
# uniform_line_length (issue #4, 9th pass): §25.14 / §30.2, weight 1.0.
# Parked in the 8th pass, calibrated here against the living texts in
# lyrics/. Syllables are approximated by vowel count (a Russian syllable
# carries one vowel).
# Two narrowings vs the spec's bare "variance < 1.5", both measured, not
# guessed:
#   1. Fragment exemption (UNIFORM_MIN_LINES = 12): §25.14 was written for
#      whole songs; the living corpus эталоны G-01, G-02, G-11 are 4-line
#      fragments with even lines -- that is craft, not a tell (§2.3: разная
#      длина строк is about long texts). Below 12 non-empty lines the check
#      stays silent.
#   2. Threshold tightened 1.5 -> 0.75: the living 16-line CW-002 in lyrics/
#      measures ~1.3 vowel-count variance, so the spec's 1.5 would
#      false-positive on living long-form texts. Below 0.75 only
#      robot-uniform texts sit (G-31: variance 0). The 0.75-1.5 zone stays
#      deliberately uncalibrated.
# The spec's genre exemptions (genre != поппанк AND genre != mantra_refrain)
# are not decidable from text alone; a conscious long mantra/refrain text
# uses lint_exempt + lint_exempt_note (issue #14 mechanism) -- that is what
# the mechanism is for.
# ---------------------------------------------------------------------------
_VOWELS = frozenset("аеёиоуыэюя")
UNIFORM_MIN_LINES = 12
UNIFORM_VARIANCE_THRESHOLD = 0.75


# ---------------------------------------------------------------------------
# Lyrics-file extraction + legal exemptions (issue #14): the blocking CI
# sweep over lyrics/ lints ONLY the fenced block under a "## Текст" heading
# -- card prose, front-matter and notes are not lyrics and must not be
# swept (a whole-file sweep of docs produced spurious chorus_checklist
# hard-fails in early CI wiring). A file may declare
# `lint_exempt: [flag_name, ...]` in front-matter for a conscious device
# (the G-13 case), but only together with a non-empty `lint_exempt_note:`
# giving the reason; an exemption without a note is itself a hard-fail
# (lint_exempt_without_note), so the exemption mechanism cannot silently
# mute the detector.
# ---------------------------------------------------------------------------
LYRICS_TEXT_RE = re.compile(r"## Текст\s*\n\s*```[^\n]*\n(.*?)\n```", re.DOTALL)
_FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---", re.DOTALL)
_LINT_EXEMPT_RE = re.compile(r"lint_exempt:\s*\[([^\]]*)\]")
_LINT_EXEMPT_NOTE_RE = re.compile(r"lint_exempt_note:\s*(\S.*)")


def extract_lint_text(text):
    """Return the lyric text to lint: the fenced block under '## Текст' when
    present (lyrics/<ID>.md format), otherwise the whole file as before."""
    m = LYRICS_TEXT_RE.search(text)
    return m.group(1) if m else text


def extract_lint_exemptions(text):
    """Parse front-matter `lint_exempt` / `lint_exempt_note`.
    Returns (exempt_flag_names, has_note)."""
    m = _FRONT_MATTER_RE.match(text)
    if not m:
        return set(), False
    fm = m.group(1)
    exempt = set()
    em = _LINT_EXEMPT_RE.search(fm)
    if em:
        exempt = {n.strip().strip("\"'") for n in em.group(1).split(",") if n.strip()}
    has_note = bool(_LINT_EXEMPT_NOTE_RE.search(fm))
    return exempt, has_note


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


def check_banal_rhyme(text):
    """§30.2 detector.banal_rhymes, weight 1.0. Both pair members must stand
    in rhyme position (line end) -- see the comment above BANAL_RHYME_PAIRS
    for the position requirement, the hyphen-split and ё/е normalisation."""
    hits = _rhyme_pair_hits(text, BANAL_RHYME_PAIRS)
    return [("banal_rhyme", 1.0, f"pair {a}/{b} at line ends") for a, b in hits]


def check_verb_rhyme(text):
    """§30.2 detector.verb_rhymes, weight 1.0. Both pair members must stand
    in rhyme position (line end) -- see the comment above BANAL_RHYME_PAIRS
    for the position requirement, the hyphen-split and ё/е normalisation."""
    hits = _rhyme_pair_hits(text, VERB_RHYME_PAIRS)
    return [("verb_rhyme", 1.0, f"pair {a}/{b} at line ends") for a, b in hits]


def check_uniform_line_length(text):
    """§25.14 / §30.2 uniform_line_length, weight 1.0. Calibrated narrowings
    (fragment exemption + tightened threshold) -- see the comment above
    UNIFORM_MIN_LINES for the measurements behind both."""
    counts = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            counts.append(sum(1 for ch in stripped.lower() if ch in _VOWELS))
    if len(counts) < UNIFORM_MIN_LINES:
        return []
    mean = sum(counts) / len(counts)
    if mean == 0:
        return []
    variance = sum((c - mean) ** 2 for c in counts) / len(counts)
    if variance < UNIFORM_VARIANCE_THRESHOLD:
        return [(
            "uniform_line_length", 1.0,
            f"{len(counts)} lines, syllable-count variance {variance:.2f} "
            f"< {UNIFORM_VARIANCE_THRESHOLD}",
        )]
    return []


# ---------------------------------------------------------------------------
# simile_chain (issue #23, 10th pass): §25.20 / §30.2, weight 1.0. Closed
# token set verbatim from the spec's own definition («словно/будто/как
# будто»), >= 2 in one stanza (blank-line-separated block).
# Bare «как» is deliberately NOT a token: it is the ordinary Russian
# comparative and appears constantly in living texts (lyrics/ uses it
# freely -- «ржавая, как гвоздь»), while the spec's chain markers are the
# *marked* similes. The spec's "штамп vs осознанная градация" judgment
# stays out of scope; a conscious long chain uses lint_exempt +
# lint_exempt_note (issue #14 mechanism).
# ---------------------------------------------------------------------------
SIMILE_MARKERS_RE = re.compile(
    r"\b(?:словно|будто|как\s+будто)\b", re.IGNORECASE
)


def check_simile_chain(text):
    """§25.20 / §30.2 simile_chain, weight 1.0. Closed token set verbatim from
    the spec's own definition («словно/будто/как будто»), >= 2 in one stanza
    (blank-line-separated block) -- see the comment above SIMILE_MARKERS_RE
    for why bare «как» is excluded and what stays out of scope."""
    flags = []
    stanzas = re.split(r"\n\s*\n", text)
    for idx, stanza in enumerate(stanzas, 1):
        hits = SIMILE_MARKERS_RE.findall(stanza)
        if len(hits) >= 2:
            flags.append((
                "simile_chain", 1.0,
                f"stanza {idx}: {len(hits)} marked similes (словно/будто/как будто)",
            ))
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


# ---------------------------------------------------------------------------
# Optional POS layer (issue #31): pymorphy3-based advisory checks for the two
# parked §30.2 flags noun_stack (3+ consecutive nouns in a line) and adj_pile
# (3+ consecutive adjectives in a line). Ending-based heuristics were evaluated
# and rejected (FP storm: «животное», «столовая» -- see #23), so the layer sits
# on a real morphological analyser.
# Strictly advisory: both checks report on the advisory channel with weight 0.0
# and never affect the exit code. Strictly optional: without pymorphy3 they
# silently no-op, so self-test and the blocking sweep are byte-identical to the
# pre-POS behaviour. Narrowing vs the spec's "без глагола": ANY non-noun token
# breaks the noun run (conservative -- fewer FPs). Tokens are Cyrillic words;
# POS is pymorphy3's first parse.
# ---------------------------------------------------------------------------
try:
    import pymorphy3
    _MORPH = pymorphy3.MorphAnalyzer()
except ImportError:
    _MORPH = None

_POS_WORD_RE = re.compile(r"[А-Яа-яЁё]+")

# --pos-trace (CLI): append the pymorphy3 token:POS sequence of each hit line
# to the advisory detail -- for FP analysis without local access to the
# analyser (see issue #31 and the PR #37/#38 measurement comments).
_POS_TRACE = False


def _pos_trace_detail(line):
    return " ".join(
        f"{word}:{_MORPH.parse(word)[0].tag.POS}" for word in _POS_WORD_RE.findall(line)
    )


def _pos_max_run(line, pos_names):
    """Longest run of consecutive tokens whose pymorphy3 POS is in pos_names."""
    if _MORPH is None:
        return 0
    best = run = 0
    for word in _POS_WORD_RE.findall(line):
        tag = _MORPH.parse(word)[0].tag.POS
        if tag in pos_names:
            run += 1
            if run > best:
                best = run
        else:
            run = 0
    return best


def check_noun_stack(text):
    """§30.2 noun_stack, advisory only (weight 0.0): 3+ consecutive nouns in a
    line. No-op without pymorphy3 -- see the comment above _MORPH."""
    if _MORPH is None:
        return []
    return [
        ("noun_stack", 0.0, f"line {i}: 3+ consecutive nouns" + (f" [{_pos_trace_detail(line)}]" if _POS_TRACE else ""))
        for i, line in enumerate(text.splitlines(), 1)
        if _pos_max_run(line, {"NOUN"}) >= 3
    ]


def check_adj_pile(text):
    """§30.2 adj_pile, advisory only (weight 0.0): 3+ consecutive adjectives in
    a line. No-op without pymorphy3 -- see the comment above _MORPH."""
    if _MORPH is None:
        return []
    return [
        ("adj_pile", 0.0, f"line {i}: 3+ consecutive adjectives" + (f" [{_pos_trace_detail(line)}]" if _POS_TRACE else ""))
        for i, line in enumerate(text.splitlines(), 1)
        if _pos_max_run(line, {"ADJF"}) >= 3
    ]


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
    check_banal_rhyme,
    check_verb_rhyme,
    check_uniform_line_length,
    check_simile_chain,
]

ADVISORY_CHECKS = [
    check_parallel_shift_candidate,
    check_noun_stack,
    check_adj_pile,
    check_school_arc,\n]

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
    """Lint one file. Returns (flags, advisories, exempted_flags).
    Applies lyric-block extraction and front-matter exemptions -- see the
    comment above LYRICS_TEXT_RE (issue #14)."""
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    exempt, has_note = extract_lint_exemptions(raw)
    flags, advisories = lint_text(extract_lint_text(raw))
    if exempt and not has_note:
        flags = flags + [(
            "lint_exempt_without_note", 2.0,
            "lint_exempt in front-matter requires a non-empty lint_exempt_note",
        )]
        return flags, advisories, []
    kept = [f for f in flags if f[0] not in exempt]
    exempted = [f for f in flags if f[0] in exempt]
    return kept, advisories, exempted


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
    "hypophora", "banal_rhyme", "verb_rhyme", "uniform_line_length",
    "simile_chain",
    "school_arc",\n}


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
        # unimplemented flags (vague_deixis, school_arc,
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



# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Out of scope (needs semantic/contextual judgment, not a lint rule):
#   - vague_deixis: requires checking neighbouring 1-2 lines for a concrete,
#     "photographable" event trace (§25.27 умолчания criterion).
#   - truncation as *omission*: the "text stops before the event" reading is
#     the same event-trace judgment as vague_deixis and stays out of scope --
#     it would hard-fail the 25.27 white-list cases G-01 and G-10. Only the
#     four literal cop-out markers of §25.13 are linted (check_truncation).
#   - banal_rhyme conscious-framing: the closed pair list itself IS linted
#     (check_banal_rhyme); only the authorial-irony discount (G-13
#     «осознанно», score weight P3 = 0.3) stays a scoring-layer concern and
#     is deliberately not part of the lint flag.
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
#   - uniform_line_length's spec genre exemptions (поппанк, mantra_refrain):
#     the calibrated core IS linted (check_uniform_line_length: min_lines 12
#     + vowel-variance threshold 0.75, both measured against the living
#     texts in lyrics/); genre stays undecidable from text alone -- a
#     conscious long mantra/refrain text uses lint_exempt + lint_exempt_note
#     (the issue #14 mechanism), which is what the mechanism is for.
#   - simile_chain's "штамп vs осознанная градация" judgment: the closed
#     marked-simile count itself IS linted (check_simile_chain); whether a
#     chain is deliberate build-up stays a scoring-layer concern (the
#     lint_exempt mechanism covers a conscious long chain).
#   - binary_light_dark / noun_stack / adj_pile:
#     §30.2 gives closed lists or regexes for these too, but each carries a
#     real false-positive risk on live text without more corpus evidence or
#     tooling we don't have (e.g. binary_light_dark's own spec flags
#     `frame_check: true`, meaning it needs to distinguish a philosophical
#     light/dark frame from a literal detail like a hallway lamp -- not
#     decidable from the regex alone; noun_stack/adj_pile need POS tagging).
#     Left for a follow-up pass, one flag at a time, each with its own
#     golden-corpus TP/FP pair per §0 protocol.
#     Promoted out of this list so far: not_x_but_y (narrowed to the literal
#     redundant-copula formula), position_explanation (closed phrase list),
#     truncation (closed marker list only, omission judgment excluded),
#     tech_metaphor (closed regex list with a bounded same-line gap),
#     hypophora (closed causal-connective set, matched only on the
#     immediately adjacent physical line), banal_rhyme and verb_rhyme
#     (closed pair lists, both members required in line-final rhyme
#     position), uniform_line_length (fragment exemption + threshold
#     tightened 1.5 -> 0.75, calibrated on the living long-form CW-002),
#     simile_chain (closed marked-simile token set «словно/будто/как будто»
#     verbatim from §25.20, >= 2 per stanza, bare «как» excluded per the
#     spec's own list); each keeps the spec's flag name but documents its
#     narrowing next to the pattern definition.
# ---------------------------------------------------------------------------

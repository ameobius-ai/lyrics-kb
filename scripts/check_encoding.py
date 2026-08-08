#!/usr/bin/env python3
"""Fail the build on mojibake (U+FFFD) or stray control chars in tracked text.

Why this exists
---------------
This KB is Russian-language, so effectively every source file is full of
multi-byte characters. A single mangled character is invisible in review and
can silently disable a rule. Real incidents:

1. scripts/lint_patterns.py shipped with one entry of MARKER_WORDS holding
   two U+FFFD bytes in the middle of the word. Python accepted it as a
   perfectly valid string literal, so the marker just never matched anything
   again -- a silent false-negative that no unit test and no golden-corpus
   case could catch, because the corpus does not contain that word either.
2. Raw-string regex patterns shipped with U+0008 (BACKSPACE) where "\\b"
   (word boundary) belonged (10 spots in SHARP_WORDS_PATTERNS /
   CONCRETE_INDICATORS). Python accepted the backspace as a literal pattern
   character, so the concrete-detail gate of check_sentiment_flatline
   silently matched nothing (found and fixed in the issue #72 pass).

The damage class is mechanical, so the guard is mechanical: any U+FFFD or
C0 control character (other than \\n, \\t, \\r) in a tracked text file is a red
build, not a latent bug. The same scan also rejects files that are not
decodable as UTF-8 at all.

Usage
-----
    python3 scripts/check_encoding.py [root]

Exits 1 and prints file:line for every damaged line. Exits 0 otherwise.
"""

import os
import sys

REPLACEMENT = "\ufffd"

# C0 control characters that are legitimate in text files. Everything else
# below U+0020 (U+0000-U+001F) is flagged: \\b/\\f/\\v/\\0 etc. have no business
# in Markdown, JSON, YAML or Python sources and are invisible in diffs.
ALLOWED_CONTROL = {"\n", "\t", "\r"}

TEXT_SUFFIXES = (
    ".md",
    ".py",
    ".json",
    ".yml",
    ".yaml",
    ".txt",
    ".csv",
    ".cfg",
    ".toml",
)

SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
}


def iter_text_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for name in sorted(filenames):
            if name.endswith(TEXT_SUFFIXES):
                yield os.path.join(dirpath, name)


def scan(root):
    """Return (scanned_count, problems) where problems is a list of tuples
    (path, lineno_or_zero, detail)."""
    problems = []
    scanned = 0
    for path in iter_text_files(root):
        try:
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
        except UnicodeDecodeError as exc:
            problems.append((path, 0, "not valid UTF-8: %s" % exc))
            continue
        scanned += 1
        for lineno, line in enumerate(text.splitlines(), 1):
            if REPLACEMENT in line:
                count = line.count(REPLACEMENT)
                problems.append((
                    path,
                    lineno,
                    "%d replacement char(s): %s" % (count, line.strip()),
                ))
            bad = [c for c in line if ord(c) < 32 and c not in ALLOWED_CONTROL]
            if bad:
                problems.append((
                    path,
                    lineno,
                    "%d control char(s), first U+%04X: %s" % (
                        len(bad),
                        ord(bad[0]),
                        line.strip()[:80],
                    ),
                ))
    return scanned, problems


def main(argv):
    root = argv[1] if len(argv) > 1 else "."
    scanned, problems = scan(root)
    if problems:
        print(
            "ENCODING CHECK FAILED: damaged text "
            "(U+FFFD replacement chars, stray control chars and/or non-UTF-8 bytes)"
        )
        for path, lineno, detail in problems:
            location = path if lineno == 0 else "%s:%d" % (path, lineno)
            print("  %s: %s" % (location, detail))
        print(
            "\n%d problem(s) found; %d text file(s) decoded cleanly. Re-write "
            "the affected characters from a clean source; do not hand-patch "
            "bytes." % (len(problems), scanned)
        )
        return 1
    print("ENCODING CHECK OK: %d text files scanned, no U+FFFD or stray control chars" % scanned)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

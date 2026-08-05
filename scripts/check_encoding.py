#!/usr/bin/env python3
"""Fail the build on mojibake (U+FFFD REPLACEMENT CHARACTER) in tracked text.

Why this exists
---------------
This KB is Russian-language, so effectively every source file is full of
multi-byte characters. A single mangled character is invisible in review and
can silently disable a rule. Real incident: scripts/lint_patterns.py shipped
with one entry of MARKER_WORDS holding two U+FFFD bytes in the middle of the
word. Python accepted it as a perfectly valid string literal, so the marker
just never matched anything again -- a silent false-negative that no unit test
and no golden-corpus case could catch, because the corpus does not contain
that word either.

The damage class is mechanical, so the guard is mechanical: any U+FFFD in a
tracked text file is a red build, not a latent bug. The same scan also
rejects files that are not decodable as UTF-8 at all.

Usage
-----
    python3 scripts/check_encoding.py [root]

Exits 1 and prints file:line for every damaged line. Exits 0 otherwise.
"""

import os
import sys

REPLACEMENT = "\ufffd"

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
        if REPLACEMENT not in text:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            if REPLACEMENT in line:
                count = line.count(REPLACEMENT)
                problems.append((
                    path,
                    lineno,
                    "%d replacement char(s): %s" % (count, line.strip()),
                ))
    return scanned, problems


def main(argv):
    root = argv[1] if len(argv) > 1 else "."
    scanned, problems = scan(root)
    if problems:
        print(
            "ENCODING CHECK FAILED: damaged text "
            "(U+FFFD replacement chars and/or non-UTF-8 bytes)"
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
    print("ENCODING CHECK OK: %d text files scanned, no U+FFFD" % scanned)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

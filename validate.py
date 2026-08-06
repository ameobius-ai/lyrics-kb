#!/usr/bin/env python3
"""Validate index.json integrity + structural checks for pipeline/packages/cases/lyrics."""
import json, sys, os, re

KB_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(KB_DIR, "index.json")

# Required structural files (not in index.json but must exist)
REQUIRED_PATHS = [
    "pipeline/release_v1.md",
    "suno/packages/darksynth_coldwave.md",
    "suno/packages/folk_horror.md",
    "suno/packages/cloud_bedroom.md",
    "cases/CW-001-poslednee-okno.md",
]

# Required headings in each package file
REQUIRED_PACKAGE_HEADINGS = ["## Style", "## Negatives"]

# Required fields in each case file
REQUIRED_CASE_FIELDS = ["id:", "status:"]

# Required front-matter fields in each lyrics file (see lyrics/README.md)
REQUIRED_LYRICS_FIELDS = ["id:", "title:", "case:"]

def main():
    errors = []

    # 1. index.json exists and is valid JSON
    if not os.path.exists(INDEX):
        print("FAIL: index.json not found")
        sys.exit(1)

    with open(INDEX) as f:
        idx = json.load(f)

    entries = idx.get("entries", [])
    declared = idx.get("count", 0)

    if len(entries) != declared:
        errors.append(f"count mismatch: declared={declared}, actual={len(entries)}")

    # 2. Check every entry has a file that exists
    seen_ids = set()
    for i, e in enumerate(entries):
        eid = e.get("id") or e.get("file") or f"entry-{i}"

        if eid in seen_ids:
            errors.append(f"[{eid}] duplicate id")
        seen_ids.add(eid)

        fp = e.get("file") or e.get("path")
        if not fp:
            errors.append(f"[{eid}] no file/path field")
            continue

        full = os.path.join(KB_DIR, fp)
        if not os.path.exists(full):
            errors.append(f"[{eid}] missing file: {fp}")

        if not e.get("title"):
            errors.append(f"[{eid}] missing title")
        if not e.get("category"):
            errors.append(f"[{eid}] missing category")

    # 3. Required structural paths exist
    for rp in REQUIRED_PATHS:
        full = os.path.join(KB_DIR, rp)
        if not os.path.exists(full):
            errors.append(f"structural: missing required path {rp}")

    # 4. Package files have required headings
    pkg_dir = os.path.join(KB_DIR, "suno", "packages")
    if os.path.isdir(pkg_dir):
        for fname in os.listdir(pkg_dir):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(pkg_dir, fname)
            with open(fpath) as f:
                content = f.read()
            for heading in REQUIRED_PACKAGE_HEADINGS:
                if heading not in content:
                    errors.append(f"package {fname}: missing heading '{heading}'")

    # 5. Case files have required YAML fields
    cases_dir = os.path.join(KB_DIR, "cases")
    if os.path.isdir(cases_dir):
        for fname in os.listdir(cases_dir):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(cases_dir, fname)
            with open(fpath) as f:
                content = f.read()
            for field in REQUIRED_CASE_FIELDS:
                if field not in content:
                    errors.append(f"case {fname}: missing field '{field}'")

    # 6. Lyrics files: front-matter fields + '## Текст' fenced block + case
    #    link target exists (the blocking lint sweep lints ONLY that block,
    #    so a missing block would silently degrade the sweep -- issue #14).
    lyrics_dir = os.path.join(KB_DIR, "lyrics")
    if os.path.isdir(lyrics_dir):
        for fname in sorted(os.listdir(lyrics_dir)):
            if not fname.endswith(".md") or fname == "README.md":
                continue
            fpath = os.path.join(lyrics_dir, fname)
            with open(fpath) as f:
                content = f.read()
            for field in REQUIRED_LYRICS_FIELDS:
                if field not in content:
                    errors.append(f"lyrics {fname}: missing field '{field}'")
            if "## Текст" not in content or "```" not in content:
                errors.append(
                    f"lyrics {fname}: missing '## Текст' fenced block "
                    "(blocking lint sweep lints only that block)"
                )
            m = re.search(r"^case:\s*(\S+)", content, re.MULTILINE)
            if m:
                case_target = os.path.join(KB_DIR, m.group(1))
                if not os.path.exists(case_target):
                    errors.append(f"lyrics {fname}: case link target missing: {m.group(1)}")

    # Report
    if errors:
        print(f"FAIL: {len(errors)} errors")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        print(f"OK: {len(entries)} entries, {declared} declared, all files present")
        cats = {}
        for e in entries:
            c = e.get("category", "?")
            cats[c] = cats.get(c, 0) + 1
        for c, n in sorted(cats.items()):
            print(f"  {c}: {n}")
        # structural checks
        print(f"  pipeline: {sum(1 for p in REQUIRED_PATHS if os.path.exists(os.path.join(KB_DIR, p)))}/{len(REQUIRED_PATHS)} required paths")
        pkg_count = len([f for f in os.listdir(os.path.join(KB_DIR, "suno", "packages")) if f.endswith(".md")]) if os.path.isdir(os.path.join(KB_DIR, "suno", "packages")) else 0
        case_count = len([f for f in os.listdir(cases_dir) if f.endswith(".md")]) if os.path.isdir(cases_dir) else 0
        lyrics_count = len([f for f in os.listdir(lyrics_dir) if f.endswith(".md") and f != "README.md"]) if os.path.isdir(lyrics_dir) else 0
        print(f"  packages: {pkg_count}")
        print(f"  cases: {case_count}")
        print(f"  lyrics: {lyrics_count}")
        sys.exit(0)

if __name__ == "__main__":
    main()

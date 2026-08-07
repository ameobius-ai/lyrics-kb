#!/usr/bin/env python3
"""
Automatic index.json synchronization tool.

Scans cases/ directory for .md files not registered in index.json,
parses their front-matter, and adds them to the index.

Usage:
    python3 scripts/auto_index.py              # Dry run (show what would be added)
    python3 scripts/auto_index.py --apply      # Apply changes to index.json
    python3 scripts/auto_index.py --commit     # Apply and commit changes

Exit codes:
    0 - No changes needed or changes applied successfully
    1 - Error occurred
"""

import json
import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path

KB_DIR = Path(__file__).parent.parent
INDEX_FILE = KB_DIR / "index.json"
CASES_DIR = KB_DIR / "cases"


def parse_case_frontmatter(filepath):
    """Parse front-matter from a case .md file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract front-matter (between --- markers)
    if not content.startswith("---"):
        return None
    
    end_idx = content.find("\n---", 3)
    if end_idx == -1:
        return None
    
    fm_text = content[3:end_idx].strip()
    
    # Parse key-value pairs
    data = {}
    for line in fm_text.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            data[key] = value
    
    # Extract title from H1 header
    title = None
    for line in content.split("\n"):
        if line.startswith("# "):
            title = line[2:].strip()
            break
    
    return {
        "id": data.get("id", filepath.stem),
        "title": title or data.get("title", "Untitled"),
        "status": data.get("status", "active"),
        "lane": data.get("lane", "unknown"),
        "bpm": data.get("bpm", ""),
        "form": data.get("form", ""),
        "lesson": data.get("lesson", "")
    }


def find_orphaned_cases(indexed_files):
    """Find case files not in index.json."""
    orphans = []
    
    if not CASES_DIR.exists():
        return orphans
    
    for case_file in sorted(CASES_DIR.glob("*.md")):
        rel_path = f"cases/{case_file.name}"
        if rel_path not in indexed_files:
            orphans.append(case_file)
    
    return orphans


def generate_index_entry(case_file):
    """Generate index.json entry from case file."""
    data = parse_case_frontmatter(case_file)
    if not data:
        return None
    
    # Map lane to category/subcategory
    lane = data["lane"]
    subcategory = lane if lane != "unknown" else "uncategorized"
    
    return {
        "id": data["id"],
        "title": data["title"],
        "category": "cases",
        "subcategory": subcategory,
        "file": f"cases/{case_file.name}",
        "status": data["status"],
        "tags": [lane, "case"],
        "added": datetime.now().strftime("%Y-%m-%d")
    }


def main():
    apply = "--apply" in sys.argv
    commit = "--commit" in sys.argv
    
    # Load current index
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        index = json.load(f)
    
    indexed_files = {e.get("file") for e in index.get("entries", [])}
    orphans = find_orphaned_cases(indexed_files)
    
    if not orphans:
        print("✓ No orphaned case files found. Index is synchronized.")
        return 0
    
    print(f"Found {len(orphans)} orphaned case file(s):")
    for orphan in orphans:
        print(f"  - {orphan.name}")
    
    if not apply and not commit:
        print("\nDry run mode. Use --apply to add these to index.json")
        return 0
    
    # Generate entries
    new_entries = []
    for orphan in orphans:
        entry = generate_index_entry(orphan)
        if entry:
            new_entries.append(entry)
            print(f"  ✓ Generated entry for {entry['id']}: {entry['title']}")
        else:
            print(f"  ✗ WARNING: Could not parse {orphan.name}")
    
    # Add to index
    index["entries"].extend(new_entries)
    index["count"] = len(index["entries"])
    
    # Write back
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Added {len(new_entries)} entries to index.json (count: {index['count']})")
    
    if commit:
        print("\nCommitting changes...")
        subprocess.run(["git", "config", "user.name", "Qwen3.8 AI Agent"], check=True, capture_output=True)
        subprocess.run(["git", "config", "user.email", "agent@qwen.ai"], check=True, capture_output=True)
        subprocess.run(["git", "add", "index.json"], check=True, capture_output=True)
        
        commit_msg = f"chore: auto-index {len(new_entries)} orphaned case files"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True, capture_output=True)
        print("✓ Committed successfully")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

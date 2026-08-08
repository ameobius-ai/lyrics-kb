#!/usr/bin/env python3
"""Validate the exact GigaChat HTTP manifest and installed runtime."""

from __future__ import annotations

import argparse
import re
import sys
from importlib.metadata import PackageNotFoundError, version as distribution_version
from pathlib import Path

LOCK_PATH = Path(__file__).with_name("requirements.txt")
EXPECTED_DISTRIBUTIONS = frozenset(
    {
        "certifi",
        "charset-normalizer",
        "idna",
        "requests",
        "urllib3",
    }
)
EXACT_PIN = re.compile(
    r"(?P<name>[A-Za-z0-9][A-Za-z0-9._-]*)=="
    r"(?P<version>[A-Za-z0-9][A-Za-z0-9.!+_-]*)"
)


def canonicalize_name(name: str) -> str:
    """Apply Python distribution-name normalization without extra packages."""

    return re.sub(r"[-_.]+", "-", name).lower()


def load_lock(path: Path = LOCK_PATH) -> dict[str, str]:
    """Load an exact five-package lock or raise a descriptive ValueError."""

    entries: dict[str, str] = {}
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw_line.partition("#")[0].strip()
        if not line:
            continue
        match = EXACT_PIN.fullmatch(line)
        if match is None:
            raise ValueError(
                f"{path}:{line_number}: expected one exact 'name==version' pin"
            )
        name = canonicalize_name(match.group("name"))
        if name in entries:
            raise ValueError(f"{path}:{line_number}: duplicate distribution {name!r}")
        entries[name] = match.group("version")

    actual_names = frozenset(entries)
    missing = sorted(EXPECTED_DISTRIBUTIONS - actual_names)
    extra = sorted(actual_names - EXPECTED_DISTRIBUTIONS)
    if missing or extra:
        raise ValueError(f"{path}: package set mismatch; missing={missing}, extra={extra}")

    return dict(sorted(entries.items()))


def validate_installed(expected: dict[str, str]) -> dict[str, str]:
    """Return installed versions when they match the manifest exactly."""

    actual: dict[str, str] = {}
    problems: list[str] = []
    for name, expected_version in expected.items():
        try:
            actual_version = distribution_version(name)
        except PackageNotFoundError:
            problems.append(f"{name}: not installed (expected {expected_version})")
            continue
        actual[name] = actual_version
        if actual_version != expected_version:
            problems.append(
                f"{name}: installed {actual_version}, expected {expected_version}"
            )

    if problems:
        raise RuntimeError("; ".join(problems))
    return actual


def format_fingerprint(versions: dict[str, str]) -> str:
    """Render a stable one-line dependency fingerprint."""

    return "; ".join(f"{name} {value}" for name, value in sorted(versions.items()))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest-only",
        action="store_true",
        help="validate exact pins without inspecting the active environment",
    )
    args = parser.parse_args()

    try:
        expected = load_lock()
        print(f"GigaChat HTTP lock manifest: {format_fingerprint(expected)}")
        if args.manifest_only:
            return 0

        actual = validate_installed(expected)
        __import__("requests")
        print(f"GigaChat HTTP runtime: {format_fingerprint(actual)}")
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

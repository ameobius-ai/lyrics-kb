#!/usr/bin/env python3
"""Tests for the exact GigaChat HTTP dependency manifest."""

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from integrations.gigachat.check_dependency_lock import (
    EXPECTED_DISTRIBUTIONS,
    LOCK_PATH,
    format_fingerprint,
    load_lock,
    validate_installed,
)

EXPECTED_VERSIONS = {
    "certifi": "2026.7.22",
    "charset-normalizer": "3.4.9",
    "idna": "3.18",
    "requests": "2.34.2",
    "urllib3": "2.7.0",
}


class DependencyLockTests(unittest.TestCase):
    def write_lock(self, content: str) -> Path:
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        path = Path(temp_dir.name) / "requirements.txt"
        path.write_text(content, encoding="utf-8")
        return path

    def valid_text(self) -> str:
        return "\n".join(
            ["# exact graph"]
            + [f"{name}=={version}" for name, version in EXPECTED_VERSIONS.items()]
        )

    def test_repository_manifest_matches_reviewed_baseline(self) -> None:
        self.assertEqual(load_lock(LOCK_PATH), EXPECTED_VERSIONS)
        self.assertEqual(frozenset(EXPECTED_VERSIONS), EXPECTED_DISTRIBUTIONS)

    def test_accepts_comments_and_normalizes_distribution_names(self) -> None:
        text = self.valid_text().replace(
            "charset-normalizer==3.4.9", "charset_normalizer==3.4.9  # normalized"
        )

        self.assertEqual(load_lock(self.write_lock(text)), EXPECTED_VERSIONS)

    def test_rejects_non_exact_or_wrong_package_sets(self) -> None:
        valid = self.valid_text()
        cases = {
            "range": valid.replace("requests==2.34.2", "requests>=2.31"),
            "spaces around operator": valid.replace(
                "requests==2.34.2", "requests == 2.34.2"
            ),
            "missing": valid.replace("urllib3==2.7.0", ""),
            "extra": f"{valid}\nsix==1.17.0",
            "duplicate normalized name": (
                f"{valid}\ncharset_normalizer==3.4.9"
            ),
        }
        for label, content in cases.items():
            with self.subTest(label=label):
                with self.assertRaises(ValueError):
                    load_lock(self.write_lock(content))

    @mock.patch(
        "integrations.gigachat.check_dependency_lock.distribution_version",
        side_effect=lambda name: EXPECTED_VERSIONS[name],
    )
    def test_installed_fingerprint_is_stable(self, _version: mock.Mock) -> None:
        actual = validate_installed(EXPECTED_VERSIONS)

        self.assertEqual(actual, EXPECTED_VERSIONS)
        self.assertEqual(
            format_fingerprint(actual),
            "certifi 2026.7.22; charset-normalizer 3.4.9; idna 3.18; "
            "requests 2.34.2; urllib3 2.7.0",
        )

    @mock.patch(
        "integrations.gigachat.check_dependency_lock.distribution_version",
        side_effect=lambda name: "0" if name == "requests" else EXPECTED_VERSIONS[name],
    )
    def test_rejects_installed_version_drift(self, _version: mock.Mock) -> None:
        with self.assertRaises(RuntimeError):
            validate_installed(EXPECTED_VERSIONS)


if __name__ == "__main__":
    unittest.main()

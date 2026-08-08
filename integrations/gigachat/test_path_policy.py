#!/usr/bin/env python3
"""Tests for the repository boundary used by the GigaChat workflow."""

import tempfile
import unittest
from pathlib import Path

from integrations.gigachat.path_policy import (
    GENERATED_SUFFIX,
    MAX_INPUT_BYTES,
    InputPathError,
    resolve_lyrics_path,
)


class ResolveLyricsPathTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base = Path(self.temp_dir.name)
        self.root = self.base / "repo"
        self.lyrics = self.root / "lyrics"
        self.lyrics.mkdir(parents=True)
        self.source = self.lyrics / "song.md"
        self.source.write_text("строка\n", encoding="utf-8")
        self.outside = self.base / "outside.md"
        self.outside.write_text("outside\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def resolve(self, raw_path: str) -> tuple[Path, Path]:
        return resolve_lyrics_path(raw_path, repo_root=self.root)

    def test_accepts_and_normalizes_repo_markdown(self) -> None:
        source, output = self.resolve("lyrics/../lyrics/song.md")

        self.assertEqual(source, self.source.resolve())
        self.assertEqual(output, self.lyrics / f"song{GENERATED_SUFFIX}")

    def test_rejects_untrusted_path_shapes(self) -> None:
        (self.root / ".git").mkdir()
        (self.root / ".git" / "config.md").write_text("secret\n", encoding="utf-8")
        (self.lyrics / "song.txt").write_text("text\n", encoding="utf-8")
        (self.lyrics / "folder.md").mkdir()
        (self.lyrics / f"report{GENERATED_SUFFIX}").write_text(
            "generated\n", encoding="utf-8"
        )
        (self.lyrics / "escape.md").symlink_to(self.outside)

        cases = {
            str(self.outside): "absolute path",
            "../outside.md": "parent traversal",
            ".git/config.md": "git metadata",
            "lyrics/song.txt": "non-Markdown",
            "lyrics/folder.md": "directory",
            f"lyrics/report{GENERATED_SUFFIX}": "generated report",
            "lyrics/escape.md": "symlink escape",
            "lyrics/missing.md": "missing file",
            "lyrics/song.md\nprintf INJECTED": "control character",
        }
        for raw_path, label in cases.items():
            with self.subTest(label=label):
                with self.assertRaises(InputPathError):
                    self.resolve(raw_path)

    def test_rejects_oversized_input(self) -> None:
        large = self.lyrics / "large.md"
        large.write_bytes(b"x" * (MAX_INPUT_BYTES + 1))

        with self.assertRaises(InputPathError):
            self.resolve("lyrics/large.md")

    def test_rejects_preexisting_output_symlink(self) -> None:
        output = self.lyrics / f"song{GENERATED_SUFFIX}"
        output.symlink_to(self.outside)

        with self.assertRaises(InputPathError):
            self.resolve("lyrics/song.md")


if __name__ == "__main__":
    unittest.main()

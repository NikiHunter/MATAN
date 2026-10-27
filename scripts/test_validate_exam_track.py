#!/usr/bin/env python3
"""Regression tests for the source-safe exam-track validation mode."""

from __future__ import annotations

import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_exam_track as exam


class SourceSafeExamTrackTests(unittest.TestCase):
    def setUp(self) -> None:
        exam.errors.clear()

    def test_source_safe_cli_runs_all_curated_checks_without_archive_access(self) -> None:
        class ForbiddenArchive:
            def glob(self, *_args, **_kwargs):
                raise AssertionError("source-safe validation must not list source lectures")

        with patch.object(exam, "SOURCE_LECTURES", ForbiddenArchive()), patch("sys.stdout", io.StringIO()):
            self.assertEqual(exam.main(["--source-safe"]), 0)
        self.assertEqual(exam.errors, [])

    def test_source_safe_link_check_does_not_stat_source_targets(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source_target = root / "source" / "restricted.pdf"
            markdown = root / "MathInMind" / "ru" / "lectures" / "notes.md"
            real_exists = Path.exists

            def guarded_exists(path: Path) -> bool:
                if path == source_target:
                    raise AssertionError("source-safe validation must not stat source targets")
                return real_exists(path)

            with patch.object(exam, "ROOT", root):
                with patch.object(exam, "SOURCE_ROOT", root / "source"):
                    with patch.object(Path, "exists", guarded_exists):
                        exam.check_links(markdown, "[restricted source](../../../source/restricted.pdf)", source_safe=True)

        self.assertEqual(exam.errors, [])


if __name__ == "__main__":
    unittest.main()

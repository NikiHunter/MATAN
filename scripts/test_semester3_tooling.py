#!/usr/bin/env python3
"""Tests for the semester-3 tooling: course layout, issue tables, notebook batches and markers.

The fixtures are small synthetic vaults in temporary directories, so these
tests do not depend on the lecture content.
"""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_views  # noqa: E402
import course_layout  # noqa: E402
import mdtext  # noqa: E402
import ocr_issues  # noqa: E402
import validate_course as course  # noqa: E402

JPEG = b"\xff\xd8\xff\xe0" + b"0" * 32 + b"\xff\xd9"


class LayoutTests(unittest.TestCase):
    def test_semester_tiers(self) -> None:
        self.assertEqual(course_layout.semester_of(0), 1)
        self.assertEqual(course_layout.semester_of(32), 1)
        self.assertEqual(course_layout.semester_of(33), 2)
        self.assertEqual(course_layout.semester_of(course_layout.LAST_LECTURE), course_layout.SEMESTERS[-1][0])
        with self.assertRaises(ValueError):
            course_layout.semester_of(course_layout.LAST_LECTURE + 1)

    def test_lecture_chapters_are_consistent(self) -> None:
        numbers = [c.number for c in course_layout.LECTURE_CHAPTERS]
        self.assertEqual(numbers, list(range(22, 22 + len(numbers))))
        for chapter in course_layout.LECTURE_CHAPTERS:
            self.assertTrue(chapter.filename.startswith(f"{chapter.number}-"))
            self.assertLessEqual(chapter.profile, 21)
            first, last = chapter.sections
            self.assertEqual(course_layout.chapter_for_section(chapter.lecturer_chapter, first), chapter.number)
            self.assertEqual(course_layout.chapter_for_section(chapter.lecturer_chapter, last), chapter.number)


class IssueTableTests(unittest.TestCase):
    def test_escaped_pipes_stay_inside_cells(self) -> None:
        row = r"| U001 | p001 | $\\|x\\|$ and $\|t\|$ | U |"
        self.assertEqual(ocr_issues.split_row(row), ["U001", "p001", r"$\\|x\\|$ and $\|t\|$", "U"])

    def test_legacy_rows_split_outside_math_and_code(self) -> None:
        row = r"| T010 | p002 | $o(|t|^s)$ | `a|b` | T |"
        self.assertEqual(ocr_issues.split_legacy_row(row), ["T010", "p002", "$o(|t|^s)$", "`a|b`", "T"])

    def test_escaping_round_trip(self) -> None:
        cells = ["M008", "$|x|$", r"$\\|y\\|$"]
        escaped = [ocr_issues.escape_cell(c) for c in cells]
        self.assertEqual(escaped[1], r"$\|x\|$")
        self.assertEqual(escaped[2], r"$\\|y\\|$")
        self.assertEqual(ocr_issues.split_row(ocr_issues.format_row(escaped)), escaped)


class StatementLabelTests(unittest.TestCase):
    def test_continuous_statements_are_statements(self) -> None:
        sites = lambda line, lang: list(build_views.statement_sites(line, lang))
        self.assertEqual(sites("**Theorem 6.3.1 (continuously differentiable maps).** Let", "en"),
                         [("theorem", "6.3.1")])
        self.assertEqual(sites("**Teorema 9.1.1 (continuidad).** Sea", "es"), [("theorem", "9.1.1")])
        self.assertEqual(sites("**Теорема 6.7.1 (окончание).**", "ru"), [])
        self.assertEqual(sites("**Theorem 2.2.2 (continued).**", "en"), [])

    def test_propositions_and_remarks_are_counted(self) -> None:
        text = "**Утверждение 10.3.1.** x\n**Замечание 8.4.1.** y\n> **Теорема 7.3.2 (признак Даламбера).** z"
        self.assertEqual(course.numbered_statements(text),
                         [("proposition", "10.3.1"), ("remark", "8.4.1"), ("theorem", "7.3.2")])

    def test_nolink_spans_are_protected(self) -> None:
        line = 'see <span class="nolink">теорема 9.2.1</span> and теорема 8.4.1'
        mask = mdtext.protected_mask(line)
        start = line.index("теорема 9.2.1")
        self.assertTrue(all(mask[start:start + 5]))
        self.assertFalse(mask[line.index("теорема 8.4.1")])


class ClassificationTests(unittest.TestCase):
    def test_exam_tracks_and_later_chapters(self) -> None:
        self.assertEqual(build_views.classify("ru/exam-sem3/tickets/100.md"), "ticket")
        self.assertEqual(build_views.classify("ru/exam-sem3/EXAM_SEM3.md"), "exam")
        self.assertEqual(build_views.classify("ru/exam/REEXAM_SEM2.md"), "exam")
        self.assertEqual(build_views.classify("ru/exam/index.md"), "index")
        self.assertEqual(build_views.classify("en/26-some-chapter.md"), "chapter")
        self.assertEqual(build_views.ticket_number("ru/exam-sem3/tickets/100.md"), 100)


class NotebookVault:
    """A three-language vault with one notebook lecture of two pages (one duplicate)."""

    def setUp(self) -> None:
        course.errors.clear()
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.vault = self.root / "MathInMind"
        self.assets = self.vault / "assets" / course.LECTURE_DIRECTORY
        self.assets.mkdir(parents=True)
        raw = self.root / "ocr" / "raw"
        raw.mkdir(parents=True)
        (raw / "p001.md").write_text("---\npage: p001\noriginal: a.jpg\n---\nТекст ⟦U001⟧\n", encoding="utf-8")
        (raw / "p002.md").write_text("---\npage: p002\noriginal: b.jpg\n---\nТекст\n", encoding="utf-8")
        (raw / "p003.md").write_text("---\npage: p003\noriginal: c.jpg\nduplicate_of: p002\n---\n", encoding="utf-8")
        (self.root / "ocr" / "ISSUES.md").write_text(
            "\n".join(ocr_issues.header_lines(ocr_issues.ISSUES_HEADER)
                      + ["| U001 | p001 | x | U | Текст ⟦U001⟧ | — | — | medium | open |  |  |"]) + "\n",
            encoding="utf-8")
        (self.assets / "lec65-66-p002-figure.jpg").write_bytes(JPEG)
        self.manifest = {
            "sources": {"notes": {"kind": "notebook", "sha256": None}},
            "pages": {"p001": {"source": "notes", "original": "a.jpg", "sha256_prefix": "0123456789ab"},
                      "p002": {"source": "notes", "original": "b.jpg", "sha256_prefix": "0123456789ab"},
                      "p003": {"source": "notes", "original": "c.jpg", "sha256_prefix": "0123456789ab",
                               "duplicate_of": "p002"}},
            "lectures": {"lecture-65-66.md": {"lecture": "65-66", "pages": ["p001", "p002"], "course_chapter": 22}},
            "figures": [{"file": "lec65-66-p002-figure.jpg", "page": "p002", "lecture_file": "lecture-65-66.md",
                         "origin": "MathInMind/assets/lectures-2025-26/lec65-66-p002-figure.jpg", "crop_box": None,
                         "width": 10, "height": 10, "sha256": hashlib.sha256(JPEG).hexdigest(),
                         "reviewed_individually": True}],
        }
        self.write_manifest()
        body = ('---\ntitle: "L"\nlang: {lang}\nlecture: 65-66\nsemester: {semester}\n'
                'source_pages: "p001, p002"\ncourse_chapter: 22\n---\n# L\n\n<a id="p001"></a>\n\n'
                "**Теорема 6.5.1.** $x$ ⟦U001⟧\n\n$$\ny=1\n$$\n\n<a id=\"p002\"></a>\n\n"
                "![f](../../assets/lectures-2025-26/lec65-66-p002-figure.jpg)\n")
        for lang in course.LANGUAGES:
            folder = self.vault / lang / course.LECTURE_DIRECTORY
            folder.mkdir(parents=True)
            text = body.format(lang=lang, semester=course_layout.semester_of(66) if
                               course_layout.LAST_LECTURE >= 66 else 3)
            (folder / "lecture-65-66.md").write_text(text, encoding="utf-8")

    def write_manifest(self) -> None:
        (self.assets / "figures-65-84.json").write_text(json.dumps(self.manifest), encoding="utf-8")

    def lecture(self, lang: str) -> Path:
        return self.vault / lang / course.LECTURE_DIRECTORY / "lecture-65-66.md"

    def run_batch(self) -> list[str]:
        with patch.multiple(course, ROOT=self.root, VAULT=self.vault, TRANSLATED_UP_TO=100), \
                patch.object(course, "semester_of", lambda n: 3 if n >= 65 else course_layout.semester_of(n)):
            course.check_notebook_batch("65-84")
        return list(course.errors)

    def run_markers(self) -> list[str]:
        with patch.multiple(course, ROOT=self.root, VAULT=self.vault):
            course.check_ocr_markers()
        return list(course.errors)


class NotebookBatchTests(NotebookVault, unittest.TestCase):
    def test_complete_batch_passes(self) -> None:
        self.assertEqual(self.run_batch(), [])

    def test_untranslated_lectures_need_only_russian(self) -> None:
        for lang in ("en", "es"):
            self.lecture(lang).unlink()
        with patch.multiple(course, ROOT=self.root, VAULT=self.vault, TRANSLATED_UP_TO=64):
            course.check_notebook_batch("65-84")
        self.assertEqual(course.errors, [])

    def test_duplicate_page_must_not_be_cited(self) -> None:
        self.manifest["lectures"]["lecture-65-66.md"]["pages"].append("p003")
        self.write_manifest()
        self.assertTrue(any("exactly one lecture" in e for e in self.run_batch()))

    def test_page_anchor_inside_a_paragraph_is_rejected(self) -> None:
        path = self.lecture("es")
        path.write_text(path.read_text(encoding="utf-8").replace('\n\n<a id="p002"></a>\n\n', ' <a id="p002"></a>\n\n'),
                        encoding="utf-8")
        self.assertTrue(any("own line" in e for e in self.run_batch()))

    def test_translation_parity(self) -> None:
        path = self.lecture("en")
        path.write_text(path.read_text(encoding="utf-8").replace("y=1", "y=2").replace(" ⟦U001⟧", ""),
                        encoding="utf-8")
        errors = self.run_batch()
        self.assertTrue(any("display formulas" in e for e in errors))
        self.assertTrue(any("open-issue markers" in e for e in errors))

    def test_figure_checksum(self) -> None:
        (self.assets / "lec65-66-p002-figure.jpg").write_bytes(JPEG.replace(b"0", b"1"))
        self.assertTrue(any("checksum" in e for e in self.run_batch()))

    def test_raw_pages_must_match(self) -> None:
        self.manifest["pages"]["p002"]["original"] = "other.jpg"
        self.write_manifest()
        self.assertTrue(any("original name differs" in e for e in self.run_batch()))


class MarkerRuleTests(NotebookVault, unittest.TestCase):
    def test_open_marker_in_lecture_is_allowed(self) -> None:
        self.assertEqual(self.run_markers(), [])

    def test_unknown_or_resolved_marker_is_rejected(self) -> None:
        path = self.lecture("ru")
        path.write_text(path.read_text(encoding="utf-8") + "\nещё ⟦T999⟧\n", encoding="utf-8")
        self.assertTrue(any("not an open row" in e for e in self.run_markers()))

    def test_marker_outside_lectures_is_rejected(self) -> None:
        (self.vault / "ru" / "23-chapter.md").write_text("Текст ⟦U001⟧\n", encoding="utf-8")
        self.assertTrue(any("outside the lecture notes" in e for e in self.run_markers()))

    def test_marker_inside_math_is_rejected(self) -> None:
        path = self.lecture("ru")
        path.write_text(path.read_text(encoding="utf-8") + "\n$a ⟦U001⟧ b$\n", encoding="utf-8")
        self.assertTrue(any("inside a formula" in e for e in self.run_markers()))


class FragmentTests(unittest.TestCase):
    def setUp(self) -> None:
        course.errors.clear()

    def test_links_to_generated_anchors_must_resolve(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "a.md").write_text('<a id="thm-8-4-1"></a>**Теорема 8.4.1.**\n', encoding="utf-8")
            with patch.object(course, "ROOT", root):
                course.check_links(root / "b.md", "[ok](a.md#thm-8-4-1) [bad](a.md#thm-8-4-2) [free](a.md#intro)")
        self.assertEqual(len(course.errors), 1)
        self.assertIn("thm-8-4-2", course.errors[0])


if __name__ == "__main__":
    unittest.main()

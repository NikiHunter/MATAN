#!/usr/bin/env python3
"""Dependency-free regression tests for the nested lecture validation.

Run from the repository root: python3 -m unittest discover -s scripts -p 'test_*.py'
Batch mutation tests work only on small temporary copies, never on the vault.
"""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_course as course


class HelperTests(unittest.TestCase):
    def setUp(self) -> None:
        course.errors.clear()

    def test_scalar_metadata(self) -> None:
        text = '---\ntitle: "A: title"\nlang: es\nlecture: 31-32\n---\n# Body'
        self.assertEqual(course.metadata(text), {"title": "A: title", "lang": "es", "lecture": "31-32"})
        self.assertEqual(course.metadata("# No header"), {})

    def test_number_ranges(self) -> None:
        for text, expected in (("00", [0]), ("01-02", [1, 2]), ("31–32", [31, 32]),
                               ("24-25-26", [24, 25, 26])):
            with self.subTest(text=text):
                self.assertEqual(course.number_range(text), expected)
        for text in ("", "3-1", "1-1", "1-3-4", "abc"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                course.number_range(text)

    def test_nested_alt_text_and_encoded_paths(self) -> None:
        text = ('![Intervals [a,b] and [c,d]](fig.jpg) '
                '[Archive](../../../source/Лекция%2036.md) '
                '[Web](https://example.com) [Here](#heading)')
        self.assertEqual(course.local_links(text), [
            (True, "fig.jpg"), (False, "../../../source/Лекция 36.md")])

    def test_valid_alt_text_is_not_a_wikilink(self) -> None:
        path = course.VAULT / "en/index.md"
        course.check_fences_and_math(path, "![Interval [a,b]](fig.jpg)")
        self.assertEqual(course.errors, [])
        course.check_fences_and_math(path, "[[not-portable]]")
        self.assertTrue(any("wiki-style" in e for e in course.errors))

    def test_nested_alt_text_does_not_hide_a_broken_image(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(course, "ROOT", root):
                course.check_links(root / "book.md", "![Intervals [a,b]](missing.jpg)")
        self.assertTrue(any("broken local link: missing.jpg" in e for e in course.errors))

    def test_headings_in_all_languages(self) -> None:
        headings = (
            "## Печатные слайды 1–3 (стр. PDF 1–3). Введение",
            "## Typed slides 1–3 (PDF pp. 1–3). Introduction",
            "## Diapositivas impresas 1–3 (pp. PDF 1–3). Introducción",
        )
        for text in headings:
            with self.subTest(text=text):
                for kind in ("pdf", "slides"):
                    self.assertEqual(course.heading_coverage(text, kind), Counter([1, 2, 3]))

    def test_math_parity_ignores_only_text_labels_and_inline_order(self) -> None:
        ru = r"$a$ затем $b$; $$ f(x)=x^2\text{ для всех }x $$"
        es = r"$b$ antes de $a$; $$f(x) = x^2\text{ para todo }x$$"
        self.assertEqual(course.math_tokens(ru), course.math_tokens(es))
        self.assertNotEqual(course.math_tokens(ru), course.math_tokens(es.replace("x^2", "x^3")))
        self.assertNotEqual(course.math_tokens("$$a$$ $$b$$"), course.math_tokens("$$b$$ $$a$$"))

    def test_numbered_statement_types_and_case(self) -> None:
        self.assertEqual(course.numbered_statements("**definición 3.8.1**; **Teorema 3.8.1.**"),
                         [("definition", "3.8.1"), ("theorem", "3.8.1")])

    def test_unbalanced_math_and_mermaid_are_detected(self) -> None:
        path = course.VAULT / "en/index.md"
        course.check_fences_and_math(path, "$$x\n```mermaid\nflowchart TD\nA --> B")
        self.assertTrue(any("display-math" in e for e in course.errors))
        self.assertTrue(any("unterminated Mermaid" in e for e in course.errors))


class ChronologyRegressionTests(unittest.TestCase):
    def setUp(self) -> None:
        course.errors.clear()
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.vault = self.root / "MathInMind"
        for lang in course.LANGUAGES:
            source = course.VAULT / lang / course.LECTURE_DIRECTORY
            target = self.vault / lang / course.LECTURE_DIRECTORY
            target.mkdir(parents=True)
            for path in source.glob("*.md"):
                shutil.copyfile(path, target / path.name)

    def run_tree(self) -> list[str]:
        # Links are tested separately; this fixture copies only lecture text.
        with patch.multiple(course, ROOT=self.root, VAULT=self.vault), patch.object(course, "check_links"):
            course.check_lecture_tree()
        return list(course.errors)

    def test_complete_chronology_passes(self) -> None:
        self.assertEqual(self.run_tree(), [])

    def test_missing_lecture_range_is_detected(self) -> None:
        (self.vault / "en" / course.LECTURE_DIRECTORY / "lecture-31-32.md").unlink()
        errors = self.run_tree()
        self.assertTrue(any("missing=[31, 32]" in e for e in errors))
        self.assertTrue(any("filenames differ" in e for e in errors))

    def test_stale_index_is_detected(self) -> None:
        index = self.vault / "en" / course.LECTURE_DIRECTORY / "index.md"
        text = index.read_text(encoding="utf-8")
        index.write_text("\n".join(line for line in text.splitlines()
                                   if "](lecture-29-30.md)" not in line), encoding="utf-8")
        self.assertTrue(any("must link to lecture-29-30.md exactly once" in e for e in self.run_tree()))

    def test_duplicated_lecture_number_is_detected(self) -> None:
        directory = self.vault / "en" / course.LECTURE_DIRECTORY
        text = (directory / "lecture-31-32.md").read_text(encoding="utf-8")
        (directory / "lecture-32.md").write_text(
            text.replace("lecture: 31-32", "lecture: 32", 1), encoding="utf-8")
        self.assertTrue(any("duplicate/extra=[32]" in e for e in self.run_tree()))


class BatchRegressionTests(unittest.TestCase):
    def setUp(self) -> None:
        course.errors.clear()
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.vault = self.root / "MathInMind"
        self.assets = self.vault / "assets" / course.LECTURE_DIRECTORY
        manifest = course.VAULT / "assets" / course.LECTURE_DIRECTORY / "figures-31-38.json"
        data = json.loads(manifest.read_text(encoding="utf-8"))
        paths = [manifest] + [manifest.parent / f["file"] for f in data["figures"]]
        paths += [course.VAULT / lang / course.LECTURE_DIRECTORY / name
                  for lang in course.LANGUAGES for name in course.NEW_LECTURES]
        for source in paths:
            target = self.root / source.relative_to(course.ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)

    def lecture(self, lang: str, number: str) -> Path:
        return self.vault / lang / course.LECTURE_DIRECTORY / f"lecture-{number}.md"

    def mutate(self, path: Path, old: str, new: str) -> None:
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def run_batch(self) -> tuple[int, list[str]]:
        with patch.multiple(course, ROOT=self.root, VAULT=self.vault):
            count = course.check_new_lecture_batch()
        return count, list(course.errors)

    def test_complete_batch_passes(self) -> None:
        self.assertEqual(self.run_batch(), (17, []))

    def test_changed_jpeg_is_detected(self) -> None:
        image = self.assets / "lec35-p06-vertical-inflection.jpg"
        image.write_bytes(image.read_bytes() + b"changed")
        _, errors = self.run_batch()
        self.assertTrue(any("JPEG checksum" in e for e in errors))

    def test_wrong_semester_is_detected(self) -> None:
        self.mutate(self.lecture("en", "35"), "semester: 2", "semester: 1")
        _, errors = self.run_batch()
        self.assertTrue(any("metadata semester" in e for e in errors))

    def test_skipped_pdf_page_is_detected(self) -> None:
        self.mutate(self.lecture("en", "36"), "(PDF p. 4)", "(PDF p. 5)")
        _, errors = self.run_batch()
        self.assertTrue(any("PDF-page headings" in e for e in errors))

    def test_changed_formula_is_detected(self) -> None:
        self.mutate(self.lecture("es", "37-38"), "2nq I_{n+1}", "3nq I_{n+1}")
        _, errors = self.run_batch()
        self.assertTrue(any("translated display formulas" in e for e in errors))

    def test_changed_numbering_is_detected(self) -> None:
        self.mutate(self.lecture("es", "37-38"), "**Teorema 4.1.4.**", "**Teorema 4.1.9.**")
        _, errors = self.run_batch()
        self.assertTrue(any("numbered statement" in e for e in errors))

    def test_missing_duplicate_cross_reference_is_detected(self) -> None:
        self.mutate(self.lecture("es", "36"), "../../ru/lectures/index.md", "#removed")
        _, errors = self.run_batch()
        self.assertTrue(any("missing duplicate-material cross-reference" in e for e in errors))

    def test_misattributed_figure_is_detected(self) -> None:
        self.mutate(self.lecture("en", "35"), "lec35-p06-vertical-inflection.jpg",
                    "lec36-p19-jump-no-antiderivative.jpg")
        _, errors = self.run_batch()
        self.assertTrue(any("misattributed figure" in e for e in errors))

    def test_malformed_manifest_fails_cleanly(self) -> None:
        (self.assets / "figures-31-38.json").write_text(
            '{"sources": {"bad": null}, "figures": []}', encoding="utf-8")
        count, errors = self.run_batch()
        self.assertEqual(count, 0)
        self.assertTrue(any("invalid/missing provenance manifest" in e for e in errors))


if __name__ == "__main__":
    unittest.main()

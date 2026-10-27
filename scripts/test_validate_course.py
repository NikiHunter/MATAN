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
from unittest.mock import call, patch

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


class BatchFixture:
    batch = "31-38"

    def setUp(self) -> None:
        course.errors.clear()
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.vault = self.root / "MathInMind"
        self.assets = self.vault / "assets" / course.LECTURE_DIRECTORY
        manifest = course.VAULT / "assets" / course.LECTURE_DIRECTORY / f"figures-{self.batch}.json"
        data = json.loads(manifest.read_text(encoding="utf-8"))
        paths = [manifest] + [manifest.parent / f["file"] for f in data["figures"]]
        paths += [course.VAULT / lang / course.LECTURE_DIRECTORY / name
                  for lang in course.LANGUAGES for name in course.LECTURE_BATCHES[self.batch]]
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
            count = course.check_new_lecture_batch(self.batch)
        return count, list(course.errors)


class BatchRegressionTests(BatchFixture, unittest.TestCase):
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


class ExtendedHelperTests(unittest.TestCase):
    def test_printed_and_typed_slide_aliases(self) -> None:
        for name in ("Typed", "Printed"):
            for plural, span, pdf in (("", "4", "p. 4"), ("s", "1–3", "pp. 1–3")):
                with self.subTest(name=name, span=span):
                    heading = f"### {name} slide{plural} {span} (PDF {pdf}). Topic"
                    expected = Counter(course.number_range(span))
                    self.assertEqual(course.heading_coverage(heading, "slides"), expected)
                    self.assertEqual(course.heading_coverage(heading, "pdf"), expected)

    def test_combined_printed_and_handwritten_headings(self) -> None:
        for heading in (
            "### Printed slide 5 and handwritten page (PDF pp. 6–7). Integral",
            "### Печатный слайд 5 и рукописная страница (стр. PDF 6–7). Интеграл",
            "### Diapositiva impresa 5 y página manuscrita (pp. PDF 6–7). Integral",
        ):
            with self.subTest(heading=heading):
                self.assertEqual(course.heading_coverage(heading, "slides"), Counter([5]))
                self.assertEqual(course.heading_coverage(heading, "pdf"), Counter([6, 7]))


class NewBatchRegressionTests(BatchFixture, unittest.TestCase):
    batch = "39-44"

    @property
    def manifest(self) -> Path:
        return self.assets / f"figures-{self.batch}.json"

    def edit_manifest(self, edit) -> None:
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        edit(data)
        self.manifest.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    def test_complete_new_batch_passes(self) -> None:
        self.assertEqual(self.run_batch(), (17, []))

    def test_new_jpeg_checksum_is_checked(self) -> None:
        image = self.assets / "lec43-44-p24-mean-value-rectangle.jpg"
        image.write_bytes(image.read_bytes() + b"changed")
        _, errors = self.run_batch()
        self.assertTrue(any("JPEG checksum" in error for error in errors))

    def test_missing_final_translation_is_detected(self) -> None:
        self.lecture("es", "43-44").unlink()
        _, errors = self.run_batch()
        self.assertTrue(any("missing new lecture translation" in error for error in errors))

    def test_new_pdf_page_gap_is_detected(self) -> None:
        self.mutate(self.lecture("en", "41-42"), "(PDF p. 7)", "(PDF p. 8)")
        _, errors = self.run_batch()
        self.assertTrue(any("PDF-page headings" in error for error in errors))

    def test_new_slide_number_gap_is_detected(self) -> None:
        self.mutate(self.lecture("en", "39-40"), "Printed slide 13", "Printed slide 14")
        _, errors = self.run_batch()
        self.assertTrue(any("typed-slide headings" in error for error in errors))

    def test_swapped_page_types_are_detected_despite_complete_page_coverage(self) -> None:
        path = self.lecture("en", "41-42")
        text = path.read_text(encoding="utf-8")
        self.assertIn("(PDF p. 7)", text)
        self.assertIn("(PDF pp. 8–9)", text)
        # Exchange the single printed page with the following handwritten pair.
        text = text.replace("(PDF p. 7)", "(PDF SWAP)", 1)
        text = text.replace("(PDF pp. 8–9)", "(PDF pp. 7–8)", 1)
        text = text.replace("(PDF SWAP)", "(PDF p. 9)", 1)
        path.write_text(text, encoding="utf-8")
        self.assertEqual(course.heading_coverage(text, "pdf"), Counter(range(1, 26)))
        _, errors = self.run_batch()
        self.assertTrue(any("printed-slide PDF-page attributions" in error for error in errors))

    def test_changed_continuity_hypothesis_is_detected(self) -> None:
        self.mutate(self.lecture("es", "43-44"), r"f\in C[a,b]", r"f\in\mathcal R[a,b]")
        _, errors = self.run_batch()
        self.assertTrue(any("translated display formulas" in error for error in errors))

    def test_new_theorem_number_is_checked(self) -> None:
        self.mutate(self.lecture("en", "43-44"), "**Theorem 4.3.3.**", "**Theorem 4.3.4.**")
        _, errors = self.run_batch()
        self.assertTrue(any("numbered statement" in error for error in errors))

    def test_exact_archive_suffix_is_required(self) -> None:
        self.mutate(self.lecture("en", "43-44"), "Лекция%2043-44%201.md", "Лекция%2043-44.md")
        _, errors = self.run_batch()
        self.assertTrue(any("missing duplicate-material cross-reference" in error and
                            "Лекция 43-44 1.md" in error for error in errors))

    def test_archive_override_cannot_be_silently_dropped(self) -> None:
        self.edit_manifest(lambda data: data["sources"]["ma25_26-lectures_39-40_notes.pdf"].pop("archive_file"))
        _, errors = self.run_batch()
        self.assertTrue(any("missing duplicate-material cross-reference" in error and
                            "Лекция 39-40.md" in error for error in errors))

    def test_invalid_archive_path_fails_cleanly(self) -> None:
        self.edit_manifest(lambda data: data["sources"]["ma25_26-lectures_43-44_notes.pdf"].update(
            archive_file="../outside.md"))
        _, errors = self.run_batch()
        self.assertTrue(any("invalid archive filename" in error for error in errors))

    def test_new_curated_section_link_is_required(self) -> None:
        self.mutate(self.lecture("es", "43-44"), "../../ru/lectures/04-riemann-properties-4-3.md", "#removed")
        _, errors = self.run_batch()
        self.assertTrue(any("missing duplicate-material cross-reference" in error and
                            "04-riemann-properties-4-3.md" in error for error in errors))

    def test_same_source_figure_order_is_checked(self) -> None:
        path = self.lecture("en", "41-42")
        text = path.read_text(encoding="utf-8")
        first, second = "lec41-42-p12-restriction.jpg", "lec41-42-p12-gluing.jpg"
        self.assertIn(first, text)
        self.assertIn(second, text)
        text = text.replace(first, "SWAP.jpg").replace(second, first).replace("SWAP.jpg", second)
        path.write_text(text, encoding="utf-8")
        _, errors = self.run_batch()
        self.assertTrue(any("figure references/order" in error for error in errors))

    def test_individual_review_flag_is_required(self) -> None:
        self.edit_manifest(lambda data: data["figures"][0].update(reviewed_individually=False))
        _, errors = self.run_batch()
        self.assertTrue(any("individual visual review" in error for error in errors))

    def test_incomplete_source_inventory_is_detected(self) -> None:
        self.edit_manifest(lambda data: data["sources"]["ma25_26-lectures_39-40_notes.pdf"]["handwritten_pdf_pages"].pop())
        _, errors = self.run_batch()
        self.assertTrue(any("page inventory is incomplete" in error for error in errors))

    def test_duplicate_source_record_is_detected(self) -> None:
        def duplicate(data):
            data["sources"]["duplicate.pdf"] = data["sources"]["ma25_26-lectures_43-44_notes.pdf"].copy()
        self.edit_manifest(duplicate)
        _, errors = self.run_batch()
        self.assertTrue(any("each lecture file" in error and "exactly once" in error for error in errors))

    def test_invalid_figure_filename_type_fails_cleanly(self) -> None:
        self.edit_manifest(lambda data: data["figures"][0].update(file=["bad.jpg"]))
        _, errors = self.run_batch()
        self.assertTrue(any("invalid JPEG filename" in error for error in errors))

    def test_missing_second_manifest_fails_cleanly(self) -> None:
        self.manifest.unlink()
        count, errors = self.run_batch()
        self.assertEqual(count, 0)
        self.assertTrue(any("invalid/missing provenance manifest" in error for error in errors))


class LatestBatchRegressionTests(BatchFixture, unittest.TestCase):
    batch = "45-50"

    @property
    def manifest(self) -> Path:
        return self.assets / f"figures-{self.batch}.json"

    def edit_manifest(self, edit) -> None:
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        edit(data)
        self.manifest.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    def test_complete_45_50_batch_passes(self) -> None:
        self.assertEqual(self.run_batch(), (4, []))

    def test_archive_suffix_override_is_required(self) -> None:
        self.mutate(self.lecture("en", "47-48"), "Лекция%2047-48%201.md", "Лекция%2047-48.md")
        _, errors = self.run_batch()
        self.assertTrue(any("missing duplicate-material cross-reference" in error and
                            "Лекция 47-48 1.md" in error for error in errors))

    def test_archive_filename_is_checked_in_frontmatter(self) -> None:
        self.mutate(self.lecture("es", "47-48"), 'archive_file: "Лекция 47-48 1.md"',
                    'archive_file: "Лекция 47-48.md"')
        _, errors = self.run_batch()
        self.assertTrue(any("metadata archive_file" in error for error in errors))

    def test_handwritten_page_inventory_is_complete(self) -> None:
        self.edit_manifest(lambda data: data["sources"]["ma25_26-lectures_47-48_notes.pdf"][
            "handwritten_pdf_pages"].remove(41))
        _, errors = self.run_batch()
        self.assertTrue(any("typed/handwritten page inventory is incomplete" in error for error in errors))

    def test_mixed_slide_annotation_does_not_duplicate_pdf_page(self) -> None:
        for lang in course.LANGUAGES:
            text = self.lecture(lang, "47-48").read_text(encoding="utf-8")
            self.assertEqual(course.heading_coverage(text, "pdf"), Counter(range(1, 42)))
            self.assertEqual(course.heading_coverage(text, "slides"), Counter(range(1, 26)))

    def test_new_figure_order_is_checked(self) -> None:
        path = self.lecture("es", "47-48")
        text = path.read_text(encoding="utf-8")
        first, second = "lec47-48-p20-improper-tail.jpg", "lec47-48-p40-spike-graph.jpg"
        self.assertIn(first, text)
        self.assertIn(second, text)
        text = text.replace(first, "SWAP.jpg").replace(second, first).replace("SWAP.jpg", second)
        path.write_text(text, encoding="utf-8")
        _, errors = self.run_batch()
        self.assertTrue(any("figure references/order" in error for error in errors))

    def test_theorem_sign_change_is_detected_across_languages(self) -> None:
        self.mutate(self.lecture("es", "49-50"), "g(x)\\to0", "g(x)\\to1")
        _, errors = self.run_batch()
        self.assertTrue(any("translated display formulas or inline-math inventory differ" in error
                            for error in errors))

    def test_individual_review_flag_is_required_for_new_crop(self) -> None:
        self.edit_manifest(lambda data: data["figures"][0].update(reviewed_individually=False))
        _, errors = self.run_batch()
        self.assertTrue(any("individual visual review" in error for error in errors))


class NewestBatchRegressionTests(BatchFixture, unittest.TestCase):
    batch = "51-54"

    @property
    def manifest(self) -> Path:
        return self.assets / f"figures-{self.batch}.json"

    def edit_manifest(self, edit) -> None:
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        edit(data)
        self.manifest.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    def test_complete_51_54_batch_passes_without_archive_material(self) -> None:
        self.assertEqual(self.run_batch(), (8, []))
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        self.assertTrue(all("archive_file" not in source for source in data["sources"].values()))
        for lang in course.LANGUAGES:
            for filename in course.LECTURE_BATCHES[self.batch]:
                text = self.lecture(lang, filename.removeprefix("lecture-").removesuffix(".md")).read_text()
                self.assertNotIn("../../../source/MathInMind/МАТАН_Л", text)

    def test_lost_handwritten_page_is_detected(self) -> None:
        self.edit_manifest(lambda data: data["sources"]["ma25_26-lectures_51-52_notes.pdf.txt"][
            "handwritten_pdf_pages"].remove(9))
        _, errors = self.run_batch()
        self.assertTrue(any("page inventory is incomplete" in error for error in errors))

    def test_printed_slide_pdf_attribution_is_checked(self) -> None:
        self.mutate(self.lecture("en", "51-52"), "(PDF p. 10)", "(PDF p. 9)")
        _, errors = self.run_batch()
        self.assertTrue(any("PDF-page headings" in error or
                            "printed-slide PDF-page attributions" in error for error in errors))

    def test_new_source_image_checksum_is_checked(self) -> None:
        image = self.assets / "lec54-p21-coordinate-limit-proof.jpg"
        image.write_bytes(image.read_bytes() + b"changed")
        _, errors = self.run_batch()
        self.assertTrue(any("JPEG checksum" in error for error in errors))

    def test_missing_thematic_cross_reference_is_detected(self) -> None:
        self.mutate(self.lecture("es", "54"), "../../ru/lectures/09-rn-foundations-5-1.md", "#removed")
        _, errors = self.run_batch()
        self.assertTrue(any("missing duplicate-material cross-reference" in error and
                            "09-rn-foundations-5-1.md" in error for error in errors))

    def test_changed_vector_formula_is_detected(self) -> None:
        self.mutate(self.lecture("es", "54"), r"\|x\|=\sqrt{\sum_{k=1}^{n}x_k^2}",
                    r"\|x\|=\sqrt{\sum_{k=1}^{n}x_k^3}")
        _, errors = self.run_batch()
        self.assertTrue(any("translated display formulas" in error for error in errors))


class LatestNewestBatchRegressionTests(BatchFixture, unittest.TestCase):
    batch = "55-60"

    @property
    def manifest(self) -> Path:
        return self.assets / f"figures-{self.batch}.json"

    def edit_manifest(self, edit) -> None:
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        edit(data)
        self.manifest.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    def test_complete_55_60_batch_passes_without_archive_material(self) -> None:
        self.assertEqual(self.run_batch(), (20, []))
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        self.assertTrue(all("archive_file" not in source for source in data["sources"].values()))
        for lang in course.LANGUAGES:
            for filename in course.LECTURE_BATCHES[self.batch]:
                text = self.lecture(lang, filename.removeprefix("lecture-").removesuffix(".md")).read_text()
                self.assertNotIn("../../../source/MathInMind/МАТАН_Л", text)

    def test_page_and_slide_totals_cover_the_three_uploads(self) -> None:
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        self.assertEqual(sum(source["pages"] for source in data["sources"].values()), 96)
        self.assertEqual(sum(source["typed_slides"] for source in data["sources"].values()), 53)
        self.assertEqual(len(data["figures"]), 20)

    def test_lost_handwritten_page_is_detected(self) -> None:
        self.edit_manifest(lambda data: data["sources"]["ma25_26-lectures_59-60_notes.pdf.txt"][
            "handwritten_pdf_pages"].remove(25))
        _, errors = self.run_batch()
        self.assertTrue(any("page inventory is incomplete" in error for error in errors))

    def test_printed_slide_pdf_attribution_is_checked(self) -> None:
        self.mutate(self.lecture("en", "59-60"), "(PDF p. 22)", "(PDF p. 21)")
        _, errors = self.run_batch()
        self.assertTrue(any("PDF-page headings" in error or
                            "printed-slide PDF-page attributions" in error for error in errors))

    def test_new_source_image_checksum_is_checked(self) -> None:
        image = self.assets / "lec59-60-p19-cantor-uniform-continuity.jpg"
        image.write_bytes(image.read_bytes() + b"changed")
        _, errors = self.run_batch()
        self.assertTrue(any("JPEG checksum" in error for error in errors))

    def test_missing_thematic_cross_reference_is_detected(self) -> None:
        self.mutate(self.lecture("ru", "59-60"), "../../ru/lectures/13-continuity-rn-5-5.md", "#removed")
        _, errors = self.run_batch()
        self.assertTrue(any("missing duplicate-material cross-reference" in error and
                            "13-continuity-rn-5-5.md" in error for error in errors))

    def test_changed_differential_formula_is_detected(self) -> None:
        self.mutate(self.lecture("es", "59-60"),
                    r"f(x)=f(a)+T(x-a)+o(x-a)", r"f(x)=f(a)+T(x-a)+O(x-a)")
        _, errors = self.run_batch()
        self.assertTrue(any("translated display formulas" in error for error in errors))

    def test_individual_review_flag_is_required_for_new_crop(self) -> None:
        self.edit_manifest(lambda data: data["figures"][-1].update(reviewed_individually=False))
        _, errors = self.run_batch()
        self.assertTrue(any("individual visual review not recorded" in error for error in errors))

    def test_stray_page_key_is_not_attributed_to_a_slide(self) -> None:
        self.edit_manifest(lambda data: data["sources"]["MA25-26_ktrwbb_55-56_notes.pdf.txt"][
            "typed_pdf_pages"].append(31))
        _, errors = self.run_batch()
        self.assertTrue(any("page inventory is incomplete" in error for error in errors))


class Lectures61To64RegressionTests(BatchFixture, unittest.TestCase):
    batch = "61-64"

    @property
    def manifest(self) -> Path:
        return self.assets / f"figures-{self.batch}.json"

    def edit_manifest(self, edit) -> None:
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        edit(data)
        self.manifest.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    def test_complete_batch_uses_only_attached_pdfs(self) -> None:
        self.assertEqual(self.run_batch(), (26, []))
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        self.assertEqual(set(data["sources"]), {
            "ma25_26-lectures_61-62_notes.pdf.txt",
            "ma25_26-lectures_63-64_notes.pdf.txt",
        })
        self.assertTrue(all("archive_file" not in source for source in data["sources"].values()))
        for lang in course.LANGUAGES:
            for filename in course.LECTURE_BATCHES[self.batch]:
                text = self.lecture(lang, filename.removeprefix("lecture-").removesuffix(".md")).read_text()
                self.assertNotIn("../../../source/MathInMind/МАТАН_Л", text)

    def test_page_slide_and_handwriting_totals(self) -> None:
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        self.assertEqual(sum(source["pages"] for source in data["sources"].values()), 82)
        self.assertEqual(sum(source["typed_slides"] for source in data["sources"].values()), 46)
        self.assertEqual(sum(len(source["handwritten_pdf_pages"]) for source in data["sources"].values()), 36)
        self.assertEqual(len(data["figures"]), 26)

    def test_lost_handwritten_page_is_detected(self) -> None:
        self.edit_manifest(lambda data: data["sources"]["ma25_26-lectures_63-64_notes.pdf.txt"][
            "handwritten_pdf_pages"].remove(42))
        _, errors = self.run_batch()
        self.assertTrue(any("page inventory is incomplete" in error for error in errors))

    def test_typed_page_attribution_is_checked_even_with_full_coverage(self) -> None:
        path = self.lecture("en", "61-62")
        text = path.read_text(encoding="utf-8")
        self.assertIn("Printed slide 7 (PDF p. 8)", text)
        self.assertIn("Handwritten page (PDF p. 7)", text)
        text = text.replace("Printed slide 7 (PDF p. 8)", "Printed slide 7 (PDF p. 7)", 1)
        text = text.replace("Handwritten page (PDF p. 7)", "Handwritten page (PDF p. 8)", 1)
        path.write_text(text, encoding="utf-8")
        self.assertEqual(course.heading_coverage(text, "pdf"), Counter(range(1, 41)))
        _, errors = self.run_batch()
        self.assertTrue(any("printed-slide PDF-page attributions" in error for error in errors))

    def test_archive_filename_claim_is_rejected(self) -> None:
        self.edit_manifest(lambda data: data["sources"]["ma25_26-lectures_61-62_notes.pdf.txt"].update(
            archive_file="Лекция 61-62.md"))
        _, errors = self.run_batch()
        self.assertTrue(any("source-only batch must not claim an archive filename" in error for error in errors))

    def test_changed_formula_is_detected(self) -> None:
        self.mutate(self.lecture("es", "63-64"), r"\beta(u,v)u=o(u^2+v^2)",
                    r"\beta(u,v)u=O(u^2+v^2)")
        _, errors = self.run_batch()
        self.assertTrue(any("translated display formulas" in error for error in errors))

    def test_new_image_checksum_is_checked(self) -> None:
        image = self.assets / "lec63-64-p42-multi-index-differential.jpg"
        image.write_bytes(image.read_bytes() + b"changed")
        _, errors = self.run_batch()
        self.assertTrue(any("JPEG checksum" in error for error in errors))

    def test_individual_review_flag_is_required(self) -> None:
        self.edit_manifest(lambda data: data["figures"][-1].update(reviewed_individually=False))
        _, errors = self.run_batch()
        self.assertTrue(any("individual visual review not recorded" in error for error in errors))

    def test_missing_final_translation_is_detected(self) -> None:
        self.lecture("es", "63-64").unlink()
        _, errors = self.run_batch()
        self.assertTrue(any("missing new lecture translation" in error for error in errors))

    def test_missing_thematic_cross_reference_is_detected(self) -> None:
        path = self.lecture("ru", "63-64")
        link = "../../ru/lectures/16-continuous-differentiability-6-3.md"
        text = path.read_text(encoding="utf-8")
        self.assertGreaterEqual(text.count(link), 1)
        path.write_text(text.replace(link, "#removed"), encoding="utf-8")
        _, errors = self.run_batch()
        self.assertTrue(any("missing duplicate-material cross-reference" in error and
                            "16-continuous-differentiability-6-3.md" in error for error in errors))


class BatchOrchestrationTests(unittest.TestCase):
    def test_main_checks_all_manifests(self) -> None:
        with patch.object(course, "check_new_lecture_batch", return_value=0) as check, patch("builtins.print"):
            self.assertEqual(course.main(), 0)
        self.assertEqual(check.call_args_list, [call("31-38"), call("39-44"), call("45-50"),
                                                 call("51-54"), call("55-60"), call("61-64")])


if __name__ == "__main__":
    unittest.main()

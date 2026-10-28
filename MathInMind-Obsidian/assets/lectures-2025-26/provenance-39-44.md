# Figure provenance — lectures 39–44 (2025/26)

These 17 JPEGs are crops of the three supplied lecture PDFs by **D. E. Apushkinskaya (RUDN University)**, not generated or redrawn illustrations. RU, EN and ES reference the same files in the same order. The source PDFs, full-page renders, contact sheets and development dependencies are not committed to Git. The earlier [[assets/lectures-2025-26/provenance-31-38|31–38 provenance]] and [manifest](figures-31-38.json) are preserved separately.

The machine-readable [39–44 manifest](figures-39-44.json) records the original PDF SHA-256 hashes, dates, semesters, complete typed/handwritten page inventories, exact archive filenames, overlapping semester-2 sections, crop boxes, source page sizes, final JPEG dimensions and hashes. Coordinates are **PDF points with a top-left origin**, rounded to 0.001 point; page numbers are **1-based PDF pages**, not printed-slide numbers.

## Review and extraction

1. Read all three text layers and visually review **all 94 PDF pages**, including handwriting and annotations on printed slides.
2. Attribute pages using contact sheets with the **source filename and page number burned into every tile**. Batches of unlabelled image results must not be used to infer page order.
3. Classify pages visually, not by the mere presence of text: handwritten p. 21 of lectures 39–40 and pp. 15, 16 and 36 of lectures 43–44 contain misleading OCR.
4. Render crops directly from the identified pages. No source annotations are recoloured or redrawn. JPEG quality is 86; nominal width is at most 1500 px (raster rounding may add one pixel), scale at most 3.2×, or 6× for the small mean-value rectangle.
5. **Open every final crop individually** to inspect its attribution, legibility and boundaries. Reopen corrected crops after changing their bounds. The final images include complete endpoint labels and diagrams, without clipped adjoining text. The unboundedness figure includes its complete preceding explanation to avoid cutting the upward curves. The Christmas-tree image retains its `@MathMatize` credit.
6. Keep source slips visible in the original images and explain the repairs in all three lecture versions. Distinguish editorial clarifications from statements or proofs actually supplied by the PDF.

The 17 new JPEGs occupy about **1 MB**; compressed working page renders stay outside Git. No large dataset, original upload or dependency directory is added to the repository.

## Source inventory

| Lectures | Date on slides | PDF pages | Typed slides | Handwritten PDF pages | Crops |
|---|---|---:|---:|---|---:|
| 39–40 | 5 Mar 2026 | 31 | 13 | 5, 7, 10–11, 13–21, 25–27, 29, 31 | 5 |
| 41–42 | 12 Mar 2026 | 25 | 11 | 5–6, 8–9, 11, 13–15, 17–18, 22–25 | 7 |
| 43–44 | 19 Mar 2026 | 38 | 16 | 4–8, 11–13, 15–16, 18–19, 21, 26–27, 29, 31–32, 34–36, 38 | 5 |
| **Total** | | **94** | **40** | **54 handwritten pages** | **17** |

Together with the previous batch: **217 pages from eight PDFs and 34 shared crops** for lectures 31–44. Semester 1 ends with lecture 32; lectures 33–64 belong to semester 2.

## Coverage and source-specific cautions

| Source | PDF pages | Content covered in the full lecture files |
|---|---|---|
| 39–40 | 1–8 | Introduction, common limit of all tagged sums, Riemann integral and terminology |
| 39–40 | 9–21 | Darboux sums, attainment warning, all four properties and handwritten proofs |
| 39–40 | 22–27 | Boundedness lemma, Darboux integrals, mesh-gap criterion and proof |
| 39–40 | 28–31 | Oscillations, proof of the sum-limit corollary, Darboux and Riemann criteria |
| 41–42 | 1–9 | Introduction; continuous and monotone integrability, with proofs |
| 41–42 | 10–15 | Finite modifications; restriction and gluing of integrability, with proofs |
| 41–42 | 16–20 | Piecewise continuity, proof, null sets and the unproved Lebesgue criterion |
| 41–42 | 21–25 | Arithmetic closure and all five oscillation arguments |
| 43–44 | 1–8 | Introduction; Dirichlet, Thomae/Riemann and the composition counterexample |
| 43–44 | 9–16 | Orientation, ten integral properties and proofs of properties 1–9 |
| 43–44 | 17–24 | Weighted mean-value theorem, three corollaries, proofs and geometry |
| 43–44 | 25–36 | Newton–Leibniz, proof, counterexamples, finite exceptions and postponed Barrow proof |
| 43–44 | 37–38 | Integration by parts and its complete product-rule proof |

Important transcription decisions:

- **39–40, p. 10:** height labels in the drawing start at 1; formal subinterval indices start at 0. The distinction is explained, not silently edited in the image.
- **39–40, pp. 19–21:** the subtraction in the refinement proof is used only for finite sums; the unbounded case is handled by extended-real comparison, not an undefined difference of infinities.
- **39–40, p. 26:** unpack the initial finiteness/boundedness step and correct the stray arrow toward infinite mesh to mesh tending to zero.
- **41–42, p. 11:** the handwritten bound already contains absolute values of the changed values. Do not invent a missing-absolute-value correction. Correct the final arrow’s direction and express the conclusion as convergence to one fixed integral, not to a changing sum.
- **41–42, p. 12:** Theorem 4.2.4 asserts restriction/gluing of **integrability**; it does not yet state additivity of integral values. Additivity is in lectures 43–44.
- **41–42, p. 24:** repair the final product estimate’s `f+g` to `fg`, explicitly.
- **43–44, pp. 5 and 7:** enlarged inspection confirms that the denominator cutoff already includes equality and the outer function already includes its right endpoint. These are preserved, not falsely labelled as source errors.
- **43–44, p. 9:** reverse the interval in the reversed-endpoint integrability hypothesis.
- **43–44, p. 14:** retain the handwritten continuity assumption for property 9; explicitly restore continuity for the standard Barrow statement and explain the antiderivative hypothesis used by the p. 36 proof. Endpoint positivity uses a one-sided subinterval when necessary.
- **43–44, pp. 29–32:** the negative result for the singular positive integrand is an **invalid application** of Newton–Leibniz, not a valid integral evaluation; the unbounded-derivative and sign-function examples establish independence of the hypotheses. Repair the printed extra `F` on p. 30.
- **43–44, pp. 34–35:** the exceptional-point indices in the original are already consistent. The limiting step uses boundedness of the integrand and continuity of the candidate antiderivative, not continuity of the integrand.
- **43–44, pp. 3 and 38:** substitution and Taylor’s integral remainder occur only in the goals. This PDF actually ends at Theorem 4.3.3, integration by parts; no missing development is invented.

## Figures

| File | PDF page | Content |
|---|---:|---|
| [lec39-40-p02-riemann-lebesgue-trees.jpg](lec39-40-p02-riemann-lebesgue-trees.jpg) | 2 | Original Riemann/Lebesgue Christmas-tree illustration and credit |
| [lec39-40-p10-darboux-sums.jpg](lec39-40-p10-darboux-sums.jpg) | 10 | Upper and lower Darboux rectangles |
| [lec39-40-p17-unbounded-function.jpg](lec39-40-p17-unbounded-function.jpg) | 17 | Unboundedness on at least one subinterval |
| [lec39-40-p20-one-point-refinement.jpg](lec39-40-p20-one-point-refinement.jpg) | 20 | Inserting a single partition point |
| [lec39-40-p21-common-refinement.jpg](lec39-40-p21-common-refinement.jpg) | 21 | Two partitions and their common refinement |
| [lec41-42-p10-finite-changes.jpg](lec41-42-p10-finite-changes.jpg) | 10 | Modifying finitely many function values |
| [lec41-42-p12-restriction.jpg](lec41-42-p12-restriction.jpg) | 12 | Restricting to a subinterval |
| [lec41-42-p12-gluing.jpg](lec41-42-p12-gluing.jpg) | 12 | Gluing at a common endpoint |
| [lec41-42-p13-extended-partition.jpg](lec41-42-p13-extended-partition.jpg) | 13 | Extending a subinterval partition |
| [lec41-42-p15-crossing-interval.jpg](lec41-42-p15-crossing-interval.jpg) | 15 | The interval crossing a gluing point |
| [lec41-42-p17-piecewise-partition.jpg](lec41-42-p17-piecewise-partition.jpg) | 17 | Pieces between discontinuities |
| [lec41-42-p18-continuous-integrable-classes.jpg](lec41-42-p18-continuous-integrable-classes.jpg) | 18 | Continuous functions inside the Riemann-integrable class |
| [lec43-44-p06-bounded-denominators.jpg](lec43-44-p06-bounded-denominators.jpg) | 6 | The finite small-denominator set in the Thomae proof |
| [lec43-44-p11-additivity-partition.jpg](lec43-44-p11-additivity-partition.jpg) | 11 | Concatenating partitions for additivity |
| [lec43-44-p24-mean-value-rectangle.jpg](lec43-44-p24-mean-value-rectangle.jpg) | 24 | Equal-area rectangle for the integral mean value |
| [lec43-44-p26-newton-leibniz-partition.jpg](lec43-44-p26-newton-leibniz-partition.jpg) | 26 | Uniform partition in the Newton–Leibniz proof |
| [lec43-44-p34-finite-exceptional-points.jpg](lec43-44-p34-finite-exceptional-points.jpg) | 34 | Trimming between exceptional points |

## Preserved duplicates

These full new lecture files explicitly link to the [[ru/lectures/index|existing Russian semester-2 register]], [[ru/lectures/03-riemann-integral-4-2|§4.2]], [[ru/lectures/04-riemann-properties-4-3|§4.3]] where relevant, and the unchanged archive originals:

- [Лекция 39-40 1.md](https://github.com/NikiHunter/matan/blob/main/source/MathInMind/%D0%9C%D0%90%D0%A2%D0%90%D0%9D_%D0%9B/%D0%9B%D0%B5%D0%BA%D1%86%D0%B8%D1%8F%2039-40%201.md);
- [Лекция 41-42.md](https://github.com/NikiHunter/matan/blob/main/source/MathInMind/%D0%9C%D0%90%D0%A2%D0%90%D0%9D_%D0%9B/%D0%9B%D0%B5%D0%BA%D1%86%D0%B8%D1%8F%2041-42.md);
- [Лекция 43-44 1.md](https://github.com/NikiHunter/matan/blob/main/source/MathInMind/%D0%9C%D0%90%D0%A2%D0%90%D0%9D_%D0%9B/%D0%9B%D0%B5%D0%BA%D1%86%D0%B8%D1%8F%2043-44%201.md).

The suffix ` 1` is part of the supplied archive filenames; it is recorded in `archive_file`, not removed by renaming the originals.

The `reviewed_individually` flags document actual visual review; a script cannot infer semantic correctness from a flag. `scripts/validate_course.py` checks **both** illustrated batches independently: complete chronology, page/slide coverage, metadata, duplicate links, matching figure hashes, image attribution/order and translation parity. It does not claim to prove the mathematics or inspect source PDFs that are intentionally absent from Git.

## Validation snapshot — 25 October 2026

- `python3 scripts/validate_course.py`: passed for lectures **0–44** in all three languages, both manifests, **167 Markdown files**, **89 Mermaid blocks** and **34 shared JPEGs**.
- `python3 scripts/validate_exam_track.py`: passed; the existing 148 source items, 72 exam tickets and Purgatory material remain intact.
- `python3 -m unittest discover -s scripts -p 'test_*.py'`: **43 tests passed**, retaining all 22 previous regressions and adding coverage for the second batch, both English slide labels, mixed headings, archive suffixes and damaged/missing provenance.
- One-off **MathJax 3.2.2** checks converted **3612** inline/display formulas from the 24 illustrated RU/EN/ES files for lectures 31–44 to SVG, with no errors. **Mermaid 11** parsed all **89** checked diagrams with no errors; this is a syntax check, not a claim of pixel-identical browser layout.
- Independent PyMuPDF/Pillow checks matched the three original PDF hashes and all 17 final JPEG hashes, actual pixel dimensions and crop bounds on the attributed pages. Rounded page dimensions were compared with a 0.001-point tolerance.

The one-off rendering dependencies and reports live outside the repository; the committed Python validators and tests remain dependency-free. These checks supplement, rather than replace, the individual page and crop reviews described above.

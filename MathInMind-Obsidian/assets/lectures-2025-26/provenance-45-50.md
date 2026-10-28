# Figure and source provenance — lectures 45–50 (2025/26)

This batch continues the existing trilingual lecture transcription through lecture 50. The three source PDFs are by **D. E. Apushkinskaya (RUDN University)** and were supplied as binary PDFs with `.pdf.txt` upload suffixes. Those uploads are not committed. The [machine-readable manifest](figures-45-50.json) records the exact source-byte SHA-256 hashes, source page counts and slide counts, printed/handwritten page inventories, dates, exact archive filenames, duplicate thematic sections, crop boxes, source page dimensions, JPEG dimensions and checksums, and the actual individual-review flags.

## Page review and attribution

All **84 PDF pages** were reviewed in source order: 29 pages for lectures 45–46, 41 pages for 47–48, and 14 pages for 49–50. Contact sheets were rendered with both the source filename and the 1-based PDF page number burned into every tile. Page attribution was checked against those labels rather than inferred from the order of returned image batches. The complete text layer was cross-checked against the printed slides; handwriting and annotations were read from the rendered page images.

| Lecture PDF | Date printed | PDF pages | Printed slides | Printed PDF pages | Handwritten PDF pages |
|---|---|---:|---:|---|---|
| `ma25_26-lectures_45-46_notes.pdf` | 26 Mar 2026 | 29 | 14 | 1–7, 10–12, 18, 22, 26, 29 | 8–9, 13–17, 19–21, 23–25, 27–28 |
| `ma25_26-lectures_47-48_notes.pdf` | 2 Apr 2026 | 41 | 25 | 1–4, 7–13, 15, 17–18, 20–23, 25–26, 29, 31–32, 34, 36 | 5–6, 14, 16, 19, 24, 27–28, 30, 33, 35, 37–41 |
| `ma25_26-lectures_49-50_notes.pdf` | 9 Apr 2026 | 14 | 10 | 1–7, 9, 12, 14 | 8, 10–11, 13 |
| **Total** | | **84** | **49** | | **35 handwritten pages** |

Printed-slide and PDF-page numbering are explicitly distinguished in all three languages. Each source page appears exactly once in its page-attribution headings. Mixed handwriting on printed pages (including slides 47–48 p. 4 and 49–50 pp. 6–7) is described as an annotation on that same page, not counted as an additional page.

## Original PDF illustrations

Four compressed JPEGs are crops of the supplied PDFs, not generated or redrawn assets. They are referenced in the same order in Russian, English and Spanish.

| JPEG | Source PDF page | Content | Crop review |
|---|---:|---|---|
| `lec45-46-p21-bonnet-interval.jpg` | 45–46, p. 21 | Handwritten interval decomposition for Bonnet's theorem | Opened individually; full labels and both colored arcs visible |
| `lec47-48-p20-improper-tail.jpg` | 47–48, p. 20 | Original slide illustrating the tail/remainder interval | Opened individually after the final full-slide bounds were selected; all labels and slide context retained |
| `lec47-48-p40-spike-graph.jpg` | 47–48, p. 40 | Hand-drawn narrow triangular peaks in the nonnegative-integral example | Opened individually; axes, integer labels and complete peaks visible |
| `lec49-50-p02-improper-integral-cartoon.jpg` | 49–50, p. 2 | Original cartoon and its printed caption about “orphan” integrals | Opened individually; caption, infinity sign, speech bubbles and full cartoon visible |

The coordinates use PDF points with the top-left origin. Page numbers are 1-based PDF pages, not slide numbers. The large handwritten images were downsampled and saved as JPEG; no complete page renders, contact sheets, source files or dependencies are in Git. The final crop of page 20 in the 47–48 PDF deliberately retains the full source slide because tighter trial bounds clipped the heading or endpoint annotations; the final bounds were reopened and reviewed.

## Source-specific transcription and mathematical review

- **45–46, pp. 4–5:** theorem 4.3.5 and both substitution remarks are included. In particular, the image's range need only lie in the stated domain `[A,B]`; it need not lie between its endpoint values. Reversed image endpoints retain their orientation.
- **45–46, pp. 8–9:** the induction proof of theorem 4.4.1 is continued across both handwritten pages, including the boundary term and the sign from integration by parts.
- **45–46, pp. 13–17:** the base values, recurrence and squeeze proof of Wallis are transcribed. The equivalent squeeze is written as `π < x_n < (2n+1)π/(2n)`.
- **45–46, pp. 19–21:** Bonnet's proof and interval diagram are included. The worked integral is the ordinary signed integral of `sin(x)/x` on `[100π,200π]`; estimates of the absolute-value integral are not described as a proof of absolute convergence.
- **45–46, pp. 27–28:** Jensen's proof uses a supporting line at the weighted mean and integrates it against the nonnegative weight. The hypotheses and normalization `∫λ=1` are retained.
- **47–48, pp. 5–6:** handwritten Hölder proof via finite sums and Riemann-sum limits is included; the Cauchy–Bunyakovsky corollary and Minkowski statement keep their source numbering.
- **47–48, pp. 13–14:** the logarithmic endpoint `p=1` is explicitly distinguished from the strict power cases; the integral diverges logarithmically there.
- **47–48, pp. 21–22:** the printed broad claim that the three linear-combination integrals “converge or diverge simultaneously” is not mathematically valid for arbitrary coefficients or cancellation. It is identified as a source error; the finite-cutoff proof and the valid convergence-qualified linearity statement are separated from it.
- **47–48, pp. 24, 27–28, 30, 33, 35:** the proofs of substitution, improper integration by parts, the right-endpoint substitution, the nonnegative-integrand criterion, comparison and limit comparison retain the limits and hypotheses. No principal value is substituted for ordinary convergence.
- **47–48, pp. 37–41:** the power-logarithm example is included. The triangular-spike construction has peaks of height `k` and half-width `1/(k²(k+1))`; each area is `1/(k(k+1))`, so the areas telescope to 1 although `f(k)=k` does not tend to zero. This resolves the handwritten red note and does not conflict with the printed remark, which assumes continuity.
- **49–50, pp. 8, 10–11, 13:** the Cauchy-criterion proof of absolute convergence, the integration-by-parts proof of Dirichlet's test and the reduction of Abel's test to Dirichlet are all represented. Monotonicity and the finite-limit condition on the endpoint product are stated where needed.

## Duplicated material and archive preservation

The complete new lecture transcriptions remain alongside the existing thematic notes:

- lectures 45–46 cross-reference [[ru/lectures/04-riemann-properties-4-3|§4.3]] and [[ru/lectures/05-taylor-wallis-inequalities-4-4|§4.4]];
- lectures 47–48 cross-reference [[ru/lectures/05-taylor-wallis-inequalities-4-4|§4.4]] and [[ru/lectures/06-improper-integrals-4-5|§4.5]];
- lectures 49–50 cross-reference [[ru/lectures/06-improper-integrals-4-5|§4.5]].

The exact source archive names, including the suffix on lectures 47–48, are preserved: [Лекция 45-46.md](https://github.com/NikiHunter/matan/blob/main/source/MathInMind/%D0%9C%D0%90%D0%A2%D0%90%D0%9D_%D0%9B/%D0%9B%D0%B5%D0%BA%D1%86%D0%B8%D1%8F%2045-46.md), [Лекция 47-48 1.md](https://github.com/NikiHunter/matan/blob/main/source/MathInMind/%D0%9C%D0%90%D0%A2%D0%90%D0%9D_%D0%9B/%D0%9B%D0%B5%D0%BA%D1%86%D0%B8%D1%8F%2047-48%201.md), [Лекция 49-50.md](https://github.com/NikiHunter/matan/blob/main/source/MathInMind/%D0%9C%D0%90%D0%A2%D0%90%D0%9D_%D0%9B/%D0%9B%D0%B5%D0%BA%D1%86%D0%B8%D1%8F%2049-50.md). The source PDFs and archive files are not renamed or replaced.

The validator checks the three language files, page/slide coverage, exact archive links, theorem/definition numbering, source and figure hashes, crop metadata, translation formula parity, figure attribution and figure order. A review flag records that the crop was actually viewed; it is not presented as an automated proof of semantic correctness.

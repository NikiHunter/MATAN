# Figure and source provenance — lectures 51–54 (2025/26)

This batch transcribes the three PDF uploads supplied in chat, with upload suffixes `.pdf.txt`. **Only those PDFs were consulted; the source folder was not opened.** Accordingly, this manifest contains no archive filenames, archive hashes, or archive links. Source SHA-256 hashes identify the exact attached PDF bytes; the source PDFs and review renders remain outside Git. The [machine-readable manifest](figures-51-54.json) records page inventories, dates, slide counts, duplicate thematic sections, full-page illustration bounds, image dimensions and hashes, and individual-review flags.

## Page review and attribution

All **85 PDF pages** were reviewed in source order. Contact-sheet tiles displayed the complete source filename and the 1-based PDF page number; text-layer extraction was checked alongside the page images. Handwriting-only pages and additional annotated pages were rendered separately and visually inspected. The trilingual lecture files distinguish printed slide numbers from PDF page numbers, and account for each source PDF page exactly once.

| Attached PDF upload | Lecture | Date printed | PDF pages | Printed slides | Handwritten-only PDF pages |
|---|---:|---|---:|---:|---|
| `ma25_26-lectures_51-52_notes.pdf.txt` | 51–52 | 16 Apr 2026 | 40 | 37 | 9, 17, 27 |
| `ма25_26_лекция_53_notes.pdf.txt` | 53 | 23 Apr 2026 | 20 | 11 | 6–12, 15–16 |
| `ма25_26_лекция_54_notes.pdf.txt` | 54 | 23 Apr 2026 | 25 | 21 | 8, 19, 21, 24 |
| **Total** | **51–54** | | **85** | **69** | **16** |

The printed-slide to PDF-page map is explicit in the page headings. In lecture 51–52, handwritten-only pages 9, 17 and 27 interrupt the printed sequence. In lecture 53, printed slides 1–5 are PDF pages 1–5, slides 6–7 are pages 13–14, and slides 8–11 are pages 17–20. In lecture 54, slide 18 is page 20; handwritten page 21 follows it, then slides 19–20 are pages 22–23, handwritten page 24, and slide 21 is page 25.

## Original-page illustration crops

Eight JPEGs were extracted from the supplied PDF pages and opened individually after the final image files were written. The illustration records use the full bounds of the relevant source page so formulas, captions, handwritten notes, and figure labels remain intact. They are genuine source-page images, not redrawn or generated. Each image is referenced in the same order in all three translations.

| JPEG | Source PDF / page | Content reviewed in final image |
|---|---|---|
| `lec51-52-p17-path-example.jpg` | 51–52, p. 17 | Four parametrizations of the upper semicircle; full handwritten board and labels |
| `lec51-52-p28-polar-sector.jpg` | 51–52, p. 28 | Polar-coordinate formulas and shaded curvilinear sector, including annotations |
| `lec51-52-p32-volume-slice.jpg` | 51–52, p. 32 | Cross-sections and nested slice illustration on the printed volume slide |
| `lec53-p11-length-estimate.jpg` | 53, p. 11 | Handwritten length-theorem estimate and completion step |
| `lec53-p15-polar-path.jpg` | 53, p. 15 | Polar parametrization and handwritten derivative expansion |
| `lec53-p16-polar-path.jpg` | 53, p. 16 | Simplification to the polar speed formula |
| `lec54-p10-neighborhoods-infinity.jpg` | 54, p. 10 | Neighborhood slide and handwritten one-point infinity notation |
| `lec54-p21-coordinate-limit-proof.jpg` | 54, p. 21 | Full handwritten proof of coordinatewise convergence |

Crop coordinates are PDF points from the top-left origin; page numbers are 1-based PDF pages. Complete source PDFs, renders, contact sheets, temporary reports and dependencies are not in Git.

## Source-specific mathematical and transcription notes

- **51–52, pp. 9, 17, 27:** the handwritten pages add sketches for area monotonicity, arbitrarily small enclosing rectangles and additivity when intersections have zero area; four different paths with the same upper-semicircle trace; and the graph-area formula, proved by shifting both integrable functions by `c = inf f`.
- **51–52, annotated slides:** handwritten additions clarify coordinate-vector and Euclidean-distance notation (p. 5), path maps and examples (pp. 14–16), the shaded subgraph (p. 21), area monotonicity (p. 24), polar coordinates (p. 28), volume cross-sections (p. 32), and `S(x)=πf²(x)` for solids of revolution (p. 39). The transcription preserves these as annotations on their printed pages, not as extra PDF pages.
- **53, pp. 6–12:** the handwritten proof of the smooth-path length theorem uses coordinatewise derivative extrema and uniform continuity. A red note on p. 9 correctly warns that the intermediate extrema-based sums are not automatically Darboux sums for `‖γ′‖`; the transcription records the necessary control of their difference.
- **53, p. 14:** the printed polar-length formula uses bounds `a,b` although the path is defined on `[α,β]`. The formula is editorially written with bounds `α,β`, consistent with the parametrization and handwritten derivation on pp. 15–16; the source mismatch is stated in all three lecture files.
- **53, p. 19:** the printed extrema sums use lowercase `f` where the force is otherwise denoted `F`. The transcription uses `F` and flags the source mismatch.
- **53, pp. 17–20:** the work convention keeps the sign of the force relative to the axis, proves the work bounds from additivity, and obtains work as the integral of the continuous force. A handwritten note on p. 18 records the constant-force case.
- **54, p. 8:** handwritten norm estimates include Cauchy–Schwarz and coordinate bounds. The printed maximum appears to end at `m` although the ambient vector is in `ℝⁿ`; the transcription flags and editorially reads the dimension as `n`.
- **54, pp. 10–13:** annotations explain why the one-point infinity notation is used in `ℝⁿ`, add vector-coordinate notation, and illustrate disjoint neighborhoods of distinct points.
- **54, pp. 19, 21, 24:** handwritten arguments prove uniqueness of vector limits, equivalence with coordinatewise convergence, and the sum-limit law. These pages are included as handwritten sections; the last one is not silently attributed to a printed slide.

## Thematic overlap and validation

The 51–52 transcription cross-references [[ru/lectures/07-measure-paths-4-6|§4.6]] and [[ru/lectures/08-integral-applications-4-7|§4.7]]; lecture 53 cross-references [[ru/lectures/08-integral-applications-4-7|§4.7]]; lecture 54 cross-references [[ru/lectures/09-rn-foundations-5-1|§5.1]] and [[ru/lectures/10-vector-sequences-5-2|§5.2]]. The relevant existing sections are maintained as a separate thematic register.

The validator checks the three language files, exact PDF-page and printed-slide coverage, source page inventories and hashes, definition/theorem numbering parity, formula and image-order parity, cross-references, figure attribution, crop bounds and JPEG hashes. Individual-review flags record actual visual inspection; they are not presented as automated proof of semantic correctness.

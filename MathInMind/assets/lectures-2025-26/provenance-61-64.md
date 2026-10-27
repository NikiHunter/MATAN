# Figure and source provenance — lectures 61–64 (2025/26)

This batch transcribes **only the two PDF uploads supplied in chat**. The repository source archive was not consulted, and no archive filenames or source-archive links are claimed. The manifest [`figures-61-64.json`](figures-61-64.json) records the exact source SHA-256 values, page and printed-slide inventories, thematic cross-references, crop bounds, image dimensions and hashes, and individual-review flags. Source PDFs, renders, contact sheets, scratch reports and dependencies remain outside Git.

## Page review and attribution

All **82 PDF pages** were reviewed in source order; the typed PDF text layers were checked alongside page images, and handwritten-only pages and handwritten annotations on printed slides were read from rendered images. The six lecture files cover every page once, distinguish 46 printed-slide numbers from PDF-page numbers, and preserve handwritten pages without assigning them slide numbers. Contact-sheet tiles show the complete uploaded filename and the 1-based PDF page number.

| Attached PDF upload | Lecture | Date printed | PDF pages | Printed slides | Typed PDF pages | Handwritten-only PDF pages |
|---|---:|---|---:|---:|---|---|
| `ma25_26-lectures_61-62_notes.pdf.txt` | 61–62 | 21 May 2026 | 40 | 25 | 1–6, 8–10, 12, 14, 16–17, 19, 21–22, 31–37, 39–40 | 7, 11, 13, 15, 18, 20, 23–30, 38 |
| `ma25_26-lectures_63-64_notes.pdf.txt` | 63–64 | 28 May 2026 | 42 | 21 | 1–4, 7, 11–12, 14, 16, 18, 21, 24–25, 27–28, 30, 34–35, 39–41 | 5–6, 8–10, 13, 15, 17, 19–20, 22–23, 26, 29, 31–33, 36–38, 42 |
| **Total** | **61–64** | | **82** | **46** | | **36** |

The printed-slide → PDF-page maps are explicit in the headings:

- **61–62:** 1→1, 2→2, 3→3, 4→4, 5→5, 6→6, 7→8, 8→9, 9→10, 10→12, 11→14, 12→16, 13→17, 14→19, 15→21, 16→22, 17→31, 18→32, 19→33, 20→34, 21→35, 22→36, 23→37, 24→39, 25→40.
- **63–64:** 1→1, 2→2, 3→3, 4→4, 5→7, 6→11, 7→12, 8→14, 9→16, 10→18, 11→21, 12→24, 13→25, 14→27, 15→28, 16→30, 17→34, 18→35, 19→39, 20→40, 21→41.

## Source hashes

| Attached PDF upload | Bytes | SHA-256 |
|---|---:|---|
| `ma25_26-lectures_61-62_notes.pdf.txt` | 16,512,885 | `1134c8b1da1cc0bb640db362255d50daca144917d512badcaf660f797ec586a5` |
| `ma25_26-lectures_63-64_notes.pdf.txt` | 23,386,821 | `91843b3c5f22ad5bc8c59b282a8b458cc38d868f5799d9269a4646fa8fdc99fa` |

## Individually reviewed source-page illustrations

All **26 final JPEGs** are cropped illustrations from selected PDF pages; none is a full-page render. Every final crop was opened and inspected individually. The manifest records each crop’s PDF-point bounds, pixel dimensions, SHA-256, and individual-review status. The same source image and ordering are used in all three translations.

| JPEG | Source PDF / page | Content inspected in the final image |
|---|---|---|
| `lec61-62-p07-vector-derivative-proof.jpg` | 61–62, p. 7 | Handwritten substitution $h=te$ into the differentiability expansion and the identification $T=d_af$ |
| `lec61-62-p08-differential-uniqueness.jpg` | 61–62, p. 8 | Corollary and handwritten uniqueness argument, including the value at the zero vector |
| `lec61-62-p11-partial-derivative-example.jpg` | 61–62, p. 11 | Function in three variables and its three partial-derivative calculations |
| `lec61-62-p13-differential-formula-proof.jpg` | 61–62, p. 13 | Linearity and basis-vector proof of the differential formula |
| `lec61-62-p15-jacobian-gradient.jpg` | 61–62, p. 15 | Jacobian matrix and coordinate notation for the gradient |
| `lec61-62-p18-coordinate-functions-lemma.jpg` | 61–62, p. 18 | Handwritten proof relating differentiability of a map to its coordinate functions |
| `lec61-62-p20-jacobian-matrix-proof.jpg` | 61–62, p. 20 | Columns $T(e^j)=\partial f/\partial x_j(a)$ and entries $\partial f_i/\partial x_j(a)$ of the Jacobian |
| `lec61-62-p23-gradient-extremal-proof.jpg` | 61–62, p. 23 | Gradient’s extremal property and the handwritten equality case |
| `lec61-62-p24-differentiable-partials-example.jpg` | 61–62, p. 24 | Differentiability and partial-derivative example |
| `lec61-62-p26-directional-derivative-counterexample.jpg` | 61–62, p. 26 | Sequence approaching the origin along the $x$-axis, its graph, and the note on discontinuity of $\partial f/\partial x$ |
| `lec61-62-p29-zero-directional-derivatives-example.jpg` | 61–62, p. 29 | Directional-derivative limit formula along a fixed direction, with value zero |
| `lec61-62-p30-directional-derivative-conclusions.jpg` | 61–62, p. 30 | Conclusions separating partial derivatives, directional derivatives and differentiability |
| `lec61-62-p32-chain-rule-diagram.jpg` | 61–62, p. 32 | Composition diagram for the chain rule |
| `lec61-62-p38-linearity-proof.jpg` | 61–62, p. 38 | Handwritten proof that the differential is linear in the function |
| `lec63-64-p05-coordinate-increment-proof.jpg` | 63–64, p. 5 | Opening setup of the telescoping coordinate path, showing the first three increment points |
| `lec63-64-p08-local-continuity-proof.jpg` | 63–64, p. 8 | Local-continuity estimate and neighborhood sketch |
| `lec63-64-p10-differentiability-remainder.jpg` | 63–64, p. 10 | Cauchy–Schwarz estimate for the differentiability remainder |
| `lec63-64-p11-pure-mixed-annotation.jpg` | 63–64, p. 11 | Printed higher-partial definition with handwritten pure/mixed examples |
| `lec63-64-p15-order-derivative-lemma.jpg` | 63–64, p. 15 | Lemma statement and opening of the downward-induction proof for lower-order derivatives |
| `lec63-64-p22-mixed-partials-counterexample.jpg` | 63–64, p. 22 | Counterexample where mixed partial derivatives need not agree |
| `lec63-64-p26-double-increment-mean-value.jpg` | 63–64, p. 26 | Mean-value proof of the double-increment formula |
| `lec63-64-p29-double-increment-criterion.jpg` | 63–64, p. 29 | Double-increment criterion and its proof |
| `lec63-64-p31-mixed-partial-symmetry-proof.jpg` | 63–64, p. 31 | Continuous-mixed-partials proof of symmetry |
| `lec63-64-p33-differentiability-remainder-proof.jpg` | 63–64, p. 33 | Estimate proving $\beta(u,v)u=o(u^2+v^2)$ |
| `lec63-64-p38-mixed-partial-independence-examples.jpg` | 63–64, p. 38 | Contrasting examples showing neither stated condition is necessary |
| `lec63-64-p42-multi-index-differential.jpg` | 63–64, p. 42 | Second differential as the quadratic form in the Hessian entries |

Crop coordinates are PDF points from the top-left origin; source and image pages are 1-based. Geometry and checksums for every crop are recorded in the manifest.

## Source-specific mathematical and transcription notes

- **61–62, p. 7:** the handwritten note identifies $T=d_af$; setting $h=te$ in the differentiability expansion gives the directional derivative $T(e)$.
- **61–62, pp. 26 and 29:** p. 26 is the coordinate-axes-only example. The separate p. 29 example is discontinuous at the origin although every nonzero directional derivative exists and equals zero; the crop name reflects p. 29’s content.
- **63–64, p. 12:** Definition 6.4.2 prints $f:E\to\mathbb R^n$, whereas surrounding general statements use $\mathbb R^m$; the printed codomain is retained and the inconsistency flagged.
- **63–64, pp. 22–23 and 26–33:** the mixed-partial counterexample and double-increment arguments are transcribed across their handwritten pages. The p. 33 estimate gives $\beta(u,v)u=o(u^2+v^2)$ and yields the equality of mixed partials under the theorem’s second condition.
- **63–64, pp. 36–38:** the examples use $\phi(t)=t^2\sin(1/t^2)$ for $t\ne0$ and $\phi(0)=0$; the product example has unbounded mixed partials. The comparison on p. 38 is retained.
- **63–64, p. 41:** the printed multinomial formula omits $h^\alpha$; the transcription restores the factor and flags the printed omission.
- **63–64, p. 42:** the handwritten formula is $d_a^2f(h)=\sum_{i=1}^{n}\sum_{j=1}^{n}(\partial^2 f/\partial x_i\partial x_j)(a)h_i h_j$.

## Thematic overlap with the semester-2 register

| Lecture | Duplicated semester-2 sections |
|---|---|
| 61–62 | [§6.1](../../ru/lectures/14-differentiability-6-1.md), [§6.2](../../ru/lectures/15-differentiation-rules-6-2.md), [§6.3](../../ru/lectures/16-continuous-differentiability-6-3.md) |
| 63–64 | [§6.3](../../ru/lectures/16-continuous-differentiability-6-3.md), [§6.4](../../ru/lectures/17-higher-derivatives-6-4.md) |

All translated lecture files link to the register index and their matching thematic sections. The ordered PDF transcriptions remain separate from, and complementary to, the thematic register.

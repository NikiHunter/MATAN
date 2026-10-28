# Figure provenance — lectures 31–38 (2025/26)

These 17 JPEGs are crops of the supplied lecture PDFs, **not generated or redrawn illustrations**. All three languages reference the same files. The source PDFs, full-page working renders and contact sheets are not committed to Git; their SHA-256 hashes identify the exact supplied files.

The machine-readable [manifest](figures-31-38.json) records source hashes, lecture/date/semester metadata, all typed and handwritten PDF-page numbers, figure hashes, source page sizes, crop boxes in PDF points (top-left origin), and final image dimensions. Pages are **1-based PDF pages**, not printed-slide numbers.

## Review and extraction

1. Read the text layer and visually review every PDF page, including the handwritten additions.
2. Check page attribution using contact sheets with the **source filename burned into every tile**. Do not infer page order from batches of separately returned images.
3. Do not classify handwriting solely by an empty text layer: several handwritten pages of lectures 33–34 contain meaningless OCR. Their handwritten-page list was corrected by visual inspection.
4. Render each crop directly from the identified PDF page, without recolouring or removing source annotations. JPEG quality: 86. Maximum nominal width: 1500 px (raster rounding may add one pixel); nominal scale at most 3.2×, or 6× for the small lecture-35 sketch.
5. **Open every final crop individually** to check page attribution, legibility and bounds. Crop adjustments were rechecked individually. The lecture-37–38 p. 5 crop includes the entire preceding printed paragraph, avoiding clipped fragments.
6. Transcribe source slips with an explicit correction in the lecture text, rather than silently changing the source image. In particular, see the subinterval-index slips on pp. 36–37 of lectures 37–38.

## Source inventory

| Lectures | Date on slides | PDF pages | Typed slides | Handwritten PDF pages | Crops |
|---|---|---:|---:|---|---:|
| 31–32 | 18 Dec 2025 | 29 | 20 | 6, 10, 12, 15, 17–19, 27–28 | 5 |
| 33–34 | 12 Feb 2026 | 28 | 16 | 6–7, 9–10, 12, 17–18, 22, 24–25, 27–28 | 3 |
| 35 | 19 Feb 2026 | 8 | 7 | 5 | 1 |
| 36 | 19 Feb 2026 | 20 | 14 | 8, 10–12, 18–19 | 2 |
| 37–38 | 26 Feb 2026 | 38 | 21 | 6, 8, 10, 12–13, 15–16, 19–21, 26–27, 29–32, 35 | 6 |
| **Total** | | **123** | **78** | **45 handwritten pages** | **17** |

Semester 1 ends with lecture 32; lectures 33–64 belong to semester 2. The full illustrated 33–38 files explicitly cross-link their duplicates in the [[ru/lectures/index|existing Russian semester-2 folder]] and [source archive](https://github.com/NikiHunter/matan/tree/main/source/MathInMind/%D0%9C%D0%90%D0%A2%D0%90%D0%9D_%D0%9B).

## Figures

| File | PDF page | Content |
|---|---:|---|
| [lec31-32-p08-first-derivative-test.jpg](lec31-32-p08-first-derivative-test.jpg) | 8 | First-derivative sign test |
| [lec31-32-p09-cubic-no-extremum.jpg](lec31-32-p09-cubic-no-extremum.jpg) | 9 | A zero derivative need not give an extremum |
| [lec31-32-p11-second-derivative-test.jpg](lec31-32-p11-second-derivative-test.jpg) | 11 | Second-derivative test |
| [lec31-32-p23-convex-concave-chords.jpg](lec31-32-p23-convex-concave-chords.jpg) | 23 | Convex and concave graphs and chords |
| [lec31-32-p25-three-chords.jpg](lec31-32-p25-three-chords.jpg) | 25 | Three-chords geometry |
| [lec33-34-p15-supporting-lines.jpg](lec33-34-p15-supporting-lines.jpg) | 15 | Supporting lines and one-sided slopes |
| [lec33-34-p21-tangent-envelopes.jpg](lec33-34-p21-tangent-envelopes.jpg) | 21 | Tangent-line characterization of convexity |
| [lec33-34-p22-asymptote-sketches.jpg](lec33-34-p22-asymptote-sketches.jpg) | 22 | Convex and concave branches relative to an asymptote |
| [lec35-p06-vertical-inflection.jpg](lec35-p06-vertical-inflection.jpg) | 6 | Inflection with a vertical tangent |
| [lec36-p04-differentiation-integration.jpg](lec36-p04-differentiation-integration.jpg) | 4 | Differentiation and its inverse problem |
| [lec36-p19-jump-no-antiderivative.jpg](lec36-p19-jump-no-antiderivative.jpg) | 19 | A jump excludes an antiderivative |
| [lec37-38-p05-elementary-operations.jpg](lec37-38-p05-elementary-operations.jpg) | 5 | Elementary functions: differentiation versus integration |
| [lec37-38-p16-smoothness-classes.jpg](lec37-38-p16-smoothness-classes.jpg) | 16 | Nested smoothness classes |
| [lec37-38-p35-integral-approaches.jpg](lec37-38-p35-integral-approaches.jpg) | 35 | Four approaches to the definite integral |
| [lec37-38-p36-partition.jpg](lec37-38-p36-partition.jpg) | 36 | A partition and a subinterval length |
| [lec37-38-p37-tagged-partition.jpg](lec37-38-p37-tagged-partition.jpg) | 37 | Tags chosen in subintervals |
| [lec37-38-p38-riemann-sum.jpg](lec37-38-p38-riemann-sum.jpg) | 38 | Rectangles corresponding to a Riemann sum |

The `reviewed_individually` fields document the visual review; a script cannot infer semantic correctness from that flag. `scripts/validate_course.py` independently checks paths, hashes, page coverage, crop metadata, figure references and translation parity. It does not claim to prove the mathematics or verify the contents of an unavailable source PDF.

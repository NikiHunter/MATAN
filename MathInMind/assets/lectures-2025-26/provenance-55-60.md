# Figure and source provenance — lectures 55–60 (2025/26)

This batch transcribes the three PDF uploads supplied in chat, with upload suffixes `.pdf.txt`. **Only those PDFs were consulted; the source folder was not opened.** Accordingly, this manifest contains no archive filenames, archive hashes, or archive links. Source SHA-256 hashes identify the exact attached PDF bytes; the source PDFs and review renders remain outside Git. The [machine-readable manifest](figures-55-60.json) records page inventories, dates, slide counts, duplicate thematic sections, full-page illustration bounds, image dimensions and hashes, and individual-review flags.

## Page review and attribution

All **96 PDF pages** were reviewed in source order. Contact-sheet tiles displayed the complete source filename and the 1-based PDF page number; text-layer extraction was checked alongside the page images. Handwriting-only pages and annotated printed pages were rendered separately and visually inspected. The trilingual lecture files distinguish printed slide numbers from PDF page numbers, and account for each source PDF page exactly once.

| Attached PDF upload | Lecture | Date printed | PDF pages | Printed slides | Handwritten-only PDF pages |
|---|---:|---|---:|---:|---|
| `MA25-26_ktrwbb_55-56_notes.pdf.txt` | 55–56 | 30 Apr 2026 | 31 | 18 | 10–12, 14–15, 18, 21, 23–25, 27–28, 31 |
| `ma25_26-lectures_57-58_notes.pdf.txt` | 57–58 | 7 May 2026 | 37 | 18 | 5–6, 8–9, 11–12, 16, 18–21, 26–28, 30–31, 34, 36–37 |
| `ma25_26-lectures_59-60_notes.pdf.txt` | 59–60 | 14 May 2026 | 28 | 17 | 7, 9, 11–13, 15, 17, 19–20, 25, 28 |
| **Total** | **55–60** | | **96** | **53** | **43** |

The printed-slide to PDF-page map is explicit in the page headings. In lecture 55–56, printed slides 1–9 are PDF pages 1–9, and the remaining slides are interleaved with handwritten proofs: slide 10 is page 13, slide 11 page 16, slide 12 page 17, slide 13 page 19, slide 14 page 20, slide 15 page 22, slide 16 page 26, slide 17 page 29 and slide 18 page 30. In lecture 57–58, slides 1–4 are pages 1–4 and then slide 5 is page 7, slide 6 page 10, slide 7 page 13, slide 8 page 14, slide 9 page 15, slide 10 page 17, slide 11 page 22, slide 12 page 23, slide 13 page 24, slide 14 page 25, slide 15 page 29, slide 16 page 32, slide 17 page 33 and slide 18 page 35. In lecture 59–60, slides 1–6 are pages 1–6 and then slide 7 is page 8, slide 8 page 10, slide 9 page 14, slide 10 page 16, slide 11 page 18, slide 12 page 21, slide 13 page 22, slide 14 page 23, slide 15 page 24, slide 16 page 26 and slide 17 page 27.

Every page of the three uploads carries a running footer that counts only printed slides ("k / 18", "k / 17"), while the PDF itself has more pages. The footer counter is therefore a slide counter, not a PDF page counter, and the lecture files never use it as a page number.

## Original-page illustration crops

Twenty JPEGs were extracted from the supplied PDF pages and opened individually after the final image files were written. The illustration records use the full bounds of the relevant source page so formulas, captions, handwritten notes, and figure labels remain intact. They are genuine source-page images, not redrawn or generated. Each image is referenced in the same order in all three translations.

| JPEG | Source PDF / page | Content reviewed in final image |
|---|---|---|
| `lec55-56-p04-subsequence-limit-proof.jpg` | 55–56, p. 4 | Theorem 5.2.3 on the printed slide plus the handwritten proof and both limits |
| `lec55-56-p10-bolzano-weierstrass-proof.jpg` | 55–56, p. 10 | Full handwritten diagonal-selection proof of the bounded case |
| `lec55-56-p11-diagonal-subsequence-diagram.jpg` | 55–56, p. 11 | Colour-coded scheme of successive coordinate thinning, with all index rows |
| `lec55-56-p14-cauchy-criterion-proof.jpg` | 55–56, p. 14 | Handwritten proof of the Cauchy criterion, including inequality (5.2.1) |
| `lec55-56-p19-open-set-interior.jpg` | 55–56, p. 19 | §3 heading, Definition 5.3.1 and the sketch with an interior and a non-interior point |
| `lec55-56-p26-ball-sphere-examples.jpg` | 55–56, p. 26 | Four examples with the handwritten "ball"/"sphere" and open-and-closed annotations |
| `lec55-56-p31-closure-criterion-proof.jpg` | 55–56, p. 31 | Handwritten cycle 1) ⇒ 2) ⇒ 3) ⇒ 1) for the closure criterion |
| `lec57-58-p04-interior-remarks.jpg` | 57–58, p. 4 | Definition 5.3.3, all five remarks and the marginal note on open sets |
| `lec57-58-p05-interior-open-proof.jpg` | 57–58, p. 5 | Handwritten proof that the interior is open |
| `lec57-58-p09-sphere-not-interior.jpg` | 57–58, p. 9 | Handwritten sequence leaving the closed ball, proving sphere points are not interior |
| `lec57-58-p14-compact-cover.jpg` | 57–58, p. 14 | Definitions of a cover, a subcover and a compact set, with the covering figure |
| `lec57-58-p16-closed-subset-compact.jpg` | 57–58, p. 16 | Handwritten compactness proof for a closed subset, including the deleted complement |
| `lec57-58-p26-cauchy-heine-proof.jpg` | 57–58, p. 26 | Boxed Cauchy condition ❋ and the handwritten 1) ⇒ 2) argument |
| `lec57-58-p31-limit-counterexample.jpg` | 57–58, p. 31 | Coordinatewise-limit corollary, the `xy/(x²+y²)` counterexample and its two paths |
| `lec59-60-p07-composition-proof.jpg` | 59–60, p. 7 | Handwritten proof that a composition of continuous maps is continuous |
| `lec59-60-p11-preimage-open-diagram.jpg` | 59–60, p. 11 | The `f⁻¹(G)` diagram, both axes and the printed/sketched labels |
| `lec59-60-p12-preimage-inclusion.jpg` | 59–60, p. 12 | Handwritten inclusion `V_δ(a) ∩ E ⊂ f⁻¹(V_ε(f(a))) ⊂ f⁻¹(G) = F` with the colour-coded sketch |
| `lec59-60-p15-compact-image-proof.jpg` | 59–60, p. 15 | Handwritten proof that the continuous image of a compact set is compact |
| `lec59-60-p19-cantor-uniform-continuity.jpg` | 59–60, p. 19 | Boxed ✳ estimate and the finite subcover construction in Cantor's theorem |
| `lec59-60-p28-differentiability-examples.jpg` | 59–60, p. 28 | Handwritten Examples 1 and 2 with the zero operator and the linearity step |

Crop coordinates are PDF points from the top-left origin; page numbers are 1-based PDF pages. Complete source PDFs, renders, contact sheets, temporary reports and dependencies are not in Git.

## Source-specific mathematical and transcription notes

- **55–56, pp. 10–12:** the handwritten proof of the Bolzano–Weierstrass selection principle is spread over three pages; the middle page carries only a diagram of the successive thinning of coordinate sequences, and it is transcribed as a diagram, not as a printed slide.
- **55–56, p. 26:** the text layer loses the bars in the ball examples, printing one and the same `B_δ(a)` as both open and closed. The page image shows the open ball and the closed ball; the transcription uses that reading and states the discrepancy.
- **55–56, p. 28:** the printed set-builder formula for the closure contains a stray comma where the word "замкнуто" belongs, i.e. `Ē = ⋂{F ⊂ Rⁿ : F , F ⊃ E}`. The mathematics is transcribed as the intended intersection over closed supersets, and the typo is flagged rather than silently repaired.
- **55–56, annotated slides:** handwritten additions record "not an interior point" and `V(a) ⊂ E` on p. 19, "ball"/"sphere" and the open-and-closed remark on p. 26, and the lower-bound step `‖x−a‖ = lim‖xᵏ−a‖ ≤ δ` on p. 28.
- **57–58, p. 16:** the handwritten compactness argument first writes the added open set as `Rⁿ \ F` and then as `Rⁿ \ E`; only the first is correct for covering `E`, and the transcription keeps the first and flags the second.
- **57–58, p. 21:** the handwritten line writes `E = [−c, c]ⁿ` where an inclusion `E ⊂ [−c, c]ⁿ` is meant; the flagged reading is used in the formulas.
- **57–58, p. 23:** the printed Definition 5.4.1 contains `f(x) ∈ B_ε(a)`, although the image is the point `A`; the transcription uses `B_ε(A)` and records the typo.
- **57–58, annotated slides:** p. 4 carries the marginal remark "if `E` is open then `Int E = E`", and p. 11 carries the rewritten arrow maps `f: E ⊂ Rⁿ → R` and `f: E ⊂ Rⁿ → Rᵐ`.
- **59–60, p. 21:** the running head of chapter 6 reads "Дифференциальное исчисление-2" while the slide itself is headed "Дифференциальное исчисление отображений нескольких переменных"; the mismatch is recorded in the lecture file.
- **59–60, p. 27:** the slide justifies the continuity of `d_a f` by "теорема 6.4.2", which has not been stated at this point of the course; the reference is kept as printed and marked as unverified in the lectures.
- **59–60, annotated slides:** p. 24 carries the handwritten "Обозначение `T ∈ L(Rⁿ, Rᵐ)`" pointing at Definition 6.1.2, and p. 26 carries `h = x − a` next to formula (6.1.2).

## Thematic overlap with the semester-2 register

| Lecture | Duplicated semester-2 sections |
|---|---|
| 55–56 | [§5.2](../../ru/lectures/10-vector-sequences-5-2.md), [§5.3](../../ru/lectures/11-topology-rn-5-3.md) |
| 57–58 | [§5.3](../../ru/lectures/11-topology-rn-5-3.md), [§5.4](../../ru/lectures/12-mapping-limits-5-4.md) |
| 59–60 | [§5.5](../../ru/lectures/13-continuity-rn-5-5.md), [§6.1](../../ru/lectures/14-differentiability-6-1.md) |

The register is linked from every translated lecture file of this batch, together with the semester-2 duplication notice covering lectures 33–64.

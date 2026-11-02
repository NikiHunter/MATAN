# Source provenance — lectures 65–84 (2025/26, semester 3)

Lectures 65–82 were cleaned from a student's handwritten notebook (82 photographed pages `p001`–`p082`);
lectures 83–84 from 42 Zoom video frames (`p083`–`p124`: typed PDF slides «k / 10» and the lecturer's
board «k of 11»). Unlike lectures 31–64 there are no lecture PDFs. The manifest
[`figures-65-84.json`](figures-65-84.json) records, for every page, the source archive, the original file
name, the first 12 hex digits of the original image's SHA-256 and technical duplicates (`p032`, `p033`,
`p043`); for every lecture its pages; for every figure its origin and checksum.

## Layers

| Layer | Where | What it is |
|---|---|---|
| Verbatim transcription | [`ocr/raw/pNNN.md`](https://github.com/NikiHunter/matan/blob/main/ocr/raw/p001.md) | page by page, as written, with `⟦ID⟧` markers at disputed places |
| Page inventory | [`ocr/MANIFEST.md`](https://github.com/NikiHunter/matan/blob/main/ocr/MANIFEST.md) | archives, original names, hashes, orientation, quality notes |
| Decided issues | [`ocr/RESOLVED.md`](https://github.com/NikiHunter/matan/blob/main/ocr/RESOLVED.md) | decision and its basis for every resolved marker |
| Open issues | [`ocr/ISSUES.md`](https://github.com/NikiHunter/matan/blob/main/ocr/ISSUES.md) | places to check against the notebook, with the lecture lines that show them |
| Cleaned lectures | `MathInMind/ru/lectures-2025-26/lecture-65-66.md … lecture-83-84.md` | study notes in the lecturer's numbering |

Every page appears in exactly one cleaned lecture, where its start is marked by the anchor `#pNNN`.
Corrections of slips in the notes are marked «Поправка к источнику» with the issue ID; text restored from
page gaps, missing slides or blank «// допис.» items is marked «Восстановлено» with its source: the
2024/25 slides of the same lecturer (identical numbering), the 2022 conspectus of the same course, or a
standard textbook proof. Scans of `p001`–`p021` are kept in [`raw/scans/`](https://github.com/NikiHunter/matan/blob/main/raw/scans/p001.jpg);
`p022`–`p124` are not stored in Git (see `.gitignore`).

## Figures

| File | Page | Origin |
|---|---|---|
| `lec65-66-p009-implicit-map-graph.jpg` | p009 | crop of `raw/scans/p009.jpg`, box (60, 2640, 2000, 3440), scaled to 1200 px |
| `lec79-80-p070-gamma-graph.jpg` | p070 | copy of `ocr/crops/p070_fig1.jpg` |
| `lec79-80-p072-measure-properties.jpg` | p072 | copy of `ocr/crops/p072_fig1.jpg` |
| `lec81-82-p079-darboux-column.jpg` | p079 | copy of `ocr/crops/p079_fig1.jpg` |
| `lec83-84-p097-two-partitions.jpg` | p097 | copy of `ocr/crops/p097_fig1.jpg` |
| `lec83-84-p102-multidim-remark.jpg` | p102 | copy of `ocr/crops/p102_fig1.jpg` |
| `lec83-84-p117-rectangle-sections.jpg` | p117 | copy of `ocr/crops/p117_fig1.jpg` |

# MathInMind

A trilingual course in mathematical analysis. Pick a language and a starting point:

| | English | Русский | Español |
|---|---|---|---|
| Course, 21 chapters | [Course index](en/index.md) | [Оглавление](ru/index.md) | [Índice del curso](es/index.md) |
| Lectures 2025/26, 0–64 | [Lecture index](en/lectures-2025-26/index.md) | [Указатель лекций](ru/lectures-2025-26/index.md) | [Índice de lecciones](es/lectures-2025-26/index.md) |
| Every term and theorem | [Terms & theorems](en/term-index.md) | [Термины и теоремы](ru/term-index.md) | [Términos y teoremas](es/term-index.md) |
| Glossary | [Glossary](en/glossary.md) | [Глоссарий](ru/glossary.md) | [Glosario](es/glossary.md) |

The language folders use identical chapter numbers and filenames, so the same note can be compared across languages.

## How the notes are connected

- **Terms.** The first mention of a term in each note links to the place where it is defined.
- **Statements.** References such as "Theorem 2.3.5", "по теореме 2.3.5" or "teorema 2.3.5" link to the statement in the 2025/26 lectures; proofs link back to what they prove.
- **Navigation.** Every chapter, lecture and exam ticket has *previous* and *next* links at the top.
- **Indexes.** Each language has an index of terms, named theorems and all numbered lecture statements.

## Lectures 2025/26

Full illustrated transcriptions of **lectures 0–64** in Russian, English and Spanish, including handwritten proofs and examples. **Semester 1:** lectures 0–32. **Semester 2:** lectures 33–64; these overlap the Russian [semester-2 register](ru/lectures/index.md), and each file says which register section it duplicates.

Lectures 51–64 were prepared only from the PDFs supplied with the request; the source archive was not consulted for them and no archive filenames are claimed. Figure provenance for each batch:

| Lectures | PDF pages | Reviewed images | Manifest | Review log |
|---|---|---|---|---|
| 51–54 | 85 | 8 | [figures-51-54.json](assets/lectures-2025-26/figures-51-54.json) | [provenance-51-54.md](assets/lectures-2025-26/provenance-51-54.md) |
| 55–60 | 96 | 20 | [figures-55-60.json](assets/lectures-2025-26/figures-55-60.json) | [provenance-55-60.md](assets/lectures-2025-26/provenance-55-60.md) |
| 61–64 | 82 (46 printed slides) | 26 | [figures-61-64.json](assets/lectures-2025-26/figures-61-64.json) | [provenance-61-64.md](assets/lectures-2025-26/provenance-61-64.md) |

## Exam track (Russian)

- [Lecture register with the original numbering](ru/lectures/index.md)
- [All 72 exam tickets](ru/exam/index.md)
- [54 Purgatory definitions with scans](ru/purgatory/definitions.md)
- [300 possible Purgatory questions](ru/purgatory/questions.md)

## Two views of the same notes

`MathInMind/` is the **GitHub view**: formulas are written `` $`...`$ `` and in ```` ```math ```` blocks so that GitHub renders them intact, and links are ordinary relative links. `MathInMind-Obsidian/` is the **Obsidian view**: choose **Open folder as vault** and select that folder to get `$...$` MathJax, `[[wikilinks]]` with hover previews, backlinks, the graph view, and coloured callouts for definitions and theorems. No community plugins are required.

Both views are generated from `MathInMind/` by `python3 scripts/build_views.py`. Edit the notes there (plain `$...$` is fine; it is converted on the next build) and never edit the Obsidian view by hand.

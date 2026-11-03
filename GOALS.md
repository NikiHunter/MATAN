# Goals — what is left to do

State on 3 November 2026. Lectures 65–84 (semester 3) are cleaned and integrated in Russian; the tooling
for semester 3 is in place. The goals below are ordered by priority. Each one ends with the check that
proves it is done. Course content is written in Russian; keep the lecturer's numbering and terminology
(§6.5…§10.4, «Теорема 8.4.1», «допустимое множество», …).

The file-by-file plan and the prompt to write each file are in [`WRITING_GUIDE.md`](WRITING_GUIDE.md).

## G1. Semester-3 exam: finish `MathInMind/ru/exam-sem3/EXAM_SEM3.md`

- Write tickets 06–95 in `MathInMind/ru/exam-sem3/tickets/NN.md` in the format of tickets 01–05:
  frontmatter `ticket`, `lecture`, `lecture_section` (forecast tickets 71–95: `forecast: true`,
  `reference_numbering: "2024"` and a visible `> **Прогноз.**` line, no links to `#thm-…` anchors);
  headings «Вопрос», «Эталонный ответ», «Доказательство», «Разобранный пример», «Если снять условие»,
  «Проверка готовности». Titles and sources are in the ticket table of `EXAM_SEM3.md`.
  - Read tickets (06–70): proofs are in the cleaned lectures `MathInMind/ru/lectures-2025-26/lecture-65-66.md … 83-84.md`.
  - Forecast tickets (71–95, гл. 11–13): from the 2024/25 slides of the same lecturer
    (`sem3_material/Матан-3 Финал Сериала.pdf`, pages 103–139: line and surface integrals, Green,
    Gauss–Ostrogradsky, Stokes, Fourier series and integral, field theory) and standard proofs.
- Add to the master the sections `## Сквозные вопросы` (~60 cumulative questions over semesters 1–3 with
  short answers), `## Чистилище` (~120 follow-ups with short answers), `## Задачи` (~30 typical and hard
  problems with solutions — say that no past papers exist and they are modelled on lecture examples and
  Демидович), `## Шпаргалка` (formula sheet), `## Пробные экзамены` (4 variants with full solutions).
- Link each finished ticket in the table; then extend `SEM3_MASTER_HEADINGS` in
  `scripts/validate_exam_track.py` back to all seven headings.
- Done when `python3 scripts/validate_exam_track.py --source-safe` reports 95 tickets.

## G2. Semester-2 reexam: `MathInMind/ru/exam/REEXAM_SEM2.md`

- Sections: «Как устроена пересдача»; «Билеты и где их доказательства» (all 72 tickets, each linked as
  `tickets/NN.md`, with the lecture or register anchor of the full proof); «Ключевые определения для
  допуска»; «Чистилище: семестр 1» (~100 follow-ups on lectures 0–32 with short answers); «Контрпримеры
  и что если убрать условие» (~40); «Пробные пересдачи» (3 variants with full solutions).
- Optional: add «Доказательство», «Задачи», «Если снять условие» to the 72 ticket files.
- Link it from `MathInMind/ru/exam/index.md`. Done when the exam validator prints «Reexam master: 72 tickets linked».

## G3. Chapters 22–26 in the lecturer's numbering (RU, EN, ES)

| Chapter | Lecturer's chapter | Lectures |
|---|---|---|
| 22 | гл. 6, §6.5–§6.7: Taylor in ℝⁿ, implicit maps, extrema | 65–68 |
| 23 | гл. 7, §7.1–§7.5: numerical series | 67–72 |
| 24 | гл. 8, §8.1–§8.4: functional and power series | 71–76 |
| 25 | гл. 9, §9.1–§9.3: parameter integrals, Γ and B | 75–80 |
| 26 | гл. 10, §10.1–§10.4: Riemann multiple integral, Fubini | 79–84 |

- Course style (goal, sections, labelled statements as blockquotes, worked example, typical mistakes,
  exercises with one `<details>` answer block), but headings `## §K.s. …` and every numbered
  definition/theorem/lemma/corollary of those lectures under its own number. Frontmatter:
  `chapter`, `part: "Семестр 3: главы лектора"`, `numbering: lecture`, `lecturer_chapter: K`.
- Register them in `scripts/course_layout.py` (`LECTURE_CHAPTERS`, with linking profiles 22→16, 23→4,
  24→10, 25→10, 26→17), list them in `{ru,en,es}/index.md`, add cross-links from chapters 04, 08, 10, 11,
  16 and 17. `validate_course.py` then checks headings, completeness and parity.
- Add semester-3 terms to `scripts/term_registry.py` (+ `_LABELS`, glossary): многочлен Тейлора в ℝⁿ
  (Опр 6.5.1), неявное отображение (Th 6.6.1), лемма Коши о сгущении, преобразование Абеля, интеграл,
  зависящий от параметра (Опр 9.1.1), равномерная сходимость несобственного интеграла (Опр 9.2.1),
  гамма- и бета-функции (Опр 9.3.1), брус и разбиение (Опр 10.1.1…), допустимое множество и мера Жордана
  (Опр 10.2.x; move «мера Жордана» off `lebesgue-measure`), интеграл по множеству, принцип Кавальери.

## G4. English and Spanish translations of lectures 65–84

- Translate `MathInMind/ru/lectures-2025-26/lecture-65-66.md … lecture-83-84.md` with formulas, page
  anchors, labels and figures unchanged.
- Then set `TRANSLATED_UP_TO = LAST_LECTURE` in `scripts/course_layout.py`.
- Add the language links back to the Russian nav lines; replace the «Russian only» notes in the EN/ES
  lecture indexes by full tables.
- The notebook-batch check then enforces RU/EN/ES parity.

## G5. Audit of chapters 01–21

Fix the open defects listed in [`ISSUES.md`](ISSUES.md) («Open») in all three languages, then do a full
mathematical read of every chapter (worked examples and exercise answers recomputed).

## G6. Lectures 85–98 (when the material arrives)

- Transcribe the new pages and frames as `ocr/raw/p125…`, with markers and rows in `ocr/ISSUES.md`.
- Clean them as lectures `lecture-85-86.md …`.
- Extend `SEMESTERS[-1]`, `figures-65-84.json` (or a new notebook batch) and the lecture indexes.
- Then write chapters 27–29 (гл. 11–13) and turn forecast tickets 71–95 into read tickets.

## How to check everything

```bash
python3 scripts/build_views.py && python3 scripts/build_views.py --check
python3 scripts/validate_course.py
python3 scripts/validate_exam_track.py --source-safe
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 ocr/check_issues.py && python3 ocr/check_formulas.py
```

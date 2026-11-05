# Writing guide — file-by-file plan for the goals in `GOALS.md`

State on 3 November 2026. This file holds the plan and the prompts; the files themselves come later,
one per session (or one per prompt). Each section below names the file, what goes into it, where its
sources are, and the check that proves it is done. All course content is in **Russian** (EN/ES only where
the goal says so). Keep the lecturer's numbering and terminology everywhere.

## How to use this guide

1. Pick the next unchecked item in the order of «Order of work» below.
2. Paste the **master prompt** (below) into a new Claude Code session in `/opt/matan/matan`, filling in
   `<FILE>` and `<SPEC>` (copy the item's bullet block from this guide).
3. After the file is written, run the item's check, tick the box here, commit and push (see «Git»).
4. Write at most ~5 tickets or one chapter per session; do not start subagents (they hit the rate limit
   and lose work — see session d43ac887).

## Master prompt (copy, fill in, paste)

```text
Work in /opt/matan/matan. Read GOALS.md and WRITING_GUIDE.md (only the item for <FILE>), then write
<FILE> exactly to this spec:

<SPEC>

Rules:
- Russian, lecturer's numbering and terms; formulas as $`…`$ / ```math blocks, like existing files.
- Read only the sources the spec names (the relevant lecture pages / pdf pages), not whole folders.
- Copy the format from the named model file (frontmatter, nav line, headings, link style).
- Link definitions/theorems to existing anchors (#def-…, #thm-…, #p0NN); never invent anchors —
  grep for them first. Forecast tickets: no #thm-… links to semester-3 lectures.
- Do not use subagents. Do not touch other files except the ones the spec lists.
- When done: run the check from the spec, fix what it reports, tick the item in WRITING_GUIDE.md,
  commit as NikiHunter (local config) and push to main via git@github-matan:NikiHunter/MATAN.git.
```

## Order of work

1. G1 tickets 06–70 (read tickets) — 65 files, ~5 per session.
2. G1 tickets 71–95 (forecast) — 25 files.
3. G1 master sections in `EXAM_SEM3.md` (5 sections, one per session) + validator update.
4. G2 `REEXAM_SEM2.md`.
5. G3 chapters 22–26 (RU first, then EN, ES) + registry/terms.
6. G4 translations of lectures 65–84 (10 files × 2 languages).
7. G5 audit (by `ISSUES.md` rows).
8. G6 only when the new material arrives.

---

## G1. Semester-3 exam

### G1.a Tickets `MathInMind/ru/exam-sem3/tickets/NN.md`, NN = 06…95

**Model file:** `MathInMind/ru/exam-sem3/tickets/01.md` (70 lines; copy its structure exactly).

**Per file:**

- Frontmatter: `title: "Билет N. <Тема>"`, `lang: ru`, `ticket: N`, `lecture: "AA-BB"`,
  `lecture_section: "K.s"`. Forecast tickets (71–95) add `forecast: true`, `reference_numbering: "2024"`.
- Nav line (as in tickets 02–10): `[← Билет N-1](…) · [Все билеты](../EXAM_SEM3.md) · [Лекции AA–BB](../../lectures-2025-26/lecture-AA-BB.md) · [Билет N+1 →](…)`;
  the last written ticket has no `[Билет N+1 →]` until the next one exists (the validator rejects broken links).
- `> **Лекционная опора:** …` with links to the exact `#def-K-s-i` / `#thm-K-s-i` / `#p0NN` anchors.
  Forecast: instead `> **Прогноз.** Билет по гл. 11–13; лекций 2025/26 ещё нет, нумерация по слайдам 2024/25 (стр. NNN).`
- Headings, in this order: `## Вопрос`, `## Эталонный ответ`, `## Доказательство`,
  `## Разобранный пример`, `## Если снять условие`, `## Проверка готовности`.
- «Эталонный ответ» = what to say in 2–3 minutes (notation, statement, idea). «Доказательство» = full proof
  as in the lecture. «Если снять условие» = 1–3 counterexamples. «Проверка готовности» = 3–5 self-check
  questions with `<details>` answers
  (numbered questions, then one `<details>` / `<summary>Ответы</summary>` block with numbered answers, as in tickets 06–10).

**Sources by block** (titles, lectures and § are in the ticket table of `EXAM_SEM3.md`):

| Tickets | Lectures file | Lecturer § |
|---|---|---|
| 06–11 | `lecture-65-66.md`, `lecture-67-68.md` | §6.6–§6.7 implicit maps, extrema, conditional extrema |
| 12–~30 | `lecture-67-68.md` … `lecture-71-72.md` | §7.1–§7.5 numerical series |
| ~31–~50 | `lecture-71-72.md` … `lecture-75-76.md` | §8.1–§8.4 functional and power series |
| ~51–~62 | `lecture-75-76.md` … `lecture-79-80.md` | §9.1–§9.3 parameter integrals, Γ, B |
| ~63–70 | `lecture-79-80.md` … `lecture-83-84.md` | §10.1–§10.4 multiple Riemann integral, Fubini |
| 71–95 | `sem3_material/Матан-3 Финал Сериала.pdf` pp. 103–139 | гл. 11–13 (forecast) |

(Exact ranges: take each row's «Лекции» and «§» column from `EXAM_SEM3.md`.)

**Also edit per ticket:** in `EXAM_SEM3.md` turn the number cell `| NN |` into `| [NN](tickets/NN.md) |`
and the status `прочитано · билет не написан` into `прочитано` (forecast: `прогноз`). Fix the
`[Билет N+1 →]` link of the previous ticket. Update «Готовы билеты 01–NN» in the «Состояние» note of
`EXAM_SEM3.md` and «tickets 01–NN written» in `README.md`.

**Check:** `python3 scripts/build_views.py` first — it links the first mention of each registered term in the new
tickets and writes their Obsidian copies (review the added links; pre-link a phrase yourself if the automatic link
splits it) — then `python3 scripts/validate_exam_track.py --source-safe` (ticket count grows; no broken anchors).

- [x] 06–10 · [x] 11–15 · [x] 16–20 · [x] 21–25 · [x] 26–30 · [x] 31–35 · [x] 36–40 · [x] 41–45
- [x] 46–50 · [x] 51–55 · [x] 56–60 · [x] 61–65 · [x] 66–70 · [x] 71–75 · [x] 76–80 · [x] 81–85
- [x] 86–90 · [ ] 91–95

### G1.b Master sections in `MathInMind/ru/exam-sem3/EXAM_SEM3.md`

Append after the ticket table, one section per session:

- [ ] `## Сквозные вопросы` — ~60 cumulative questions over semesters 1–3 (limits, continuity, Taylor,
  Riemann integral, series, ℝⁿ differentiability, implicit maps); each: question + 1–3-line answer + link
  to the lecture anchor. Sources: `MathInMind/ru/lectures-2025-26/`, `MathInMind/ru/exam/tickets/`.
- [ ] `## Чистилище` — ~120 short follow-ups («а если…», «почему нельзя…») grouped by § 6.5…10.4 and
  гл. 11–13; answer in `<details>`. Model: `MathInMind/ru/purgatory/`.
- [ ] `## Задачи` — ~30 typical and hard problems with full solutions; state explicitly that no past
  papers exist and the problems are modelled on lecture examples and Демидович. Mix: series tests,
  uniform convergence, power-series radius, parameter integrals/Γ/B, extrema with constraints, double
  integrals with change of order.
- [ ] `## Шпаргалка` — formula sheet: Taylor in ℝⁿ, extremum criteria, series tests table, Weierstrass /
  Abel / Dirichlet, power-series formulas, Γ/B identities, Fubini, change of variables, Green / Gauss /
  Stokes (forecast). Model: `MathInMind/ru/formula-sheet.md`.
- [ ] `## Пробные экзамены` — 4 variants, each 2 tickets + 1 problem + 3 follow-ups, full solutions in
  `<details>`.
- [ ] Then set `SEM3_MASTER_HEADINGS` in `scripts/validate_exam_track.py` (line 32) to all seven headings:
  `Формат экзамена, Билеты, Сквозные вопросы, Чистилище, Задачи, Шпаргалка, Пробные экзамены`.

**Check:** validator reports 95 tickets and no missing sections.

---

## G2. Semester-2 reexam: `MathInMind/ru/exam/REEXAM_SEM2.md`

**Model:** `MathInMind/ru/exam-sem3/EXAM_SEM3.md` (structure), tickets in `MathInMind/ru/exam/tickets/` (72 files).

- [ ] Frontmatter `title`, `lang: ru`; sections in this order:
  «Как устроена пересдача»; «Билеты и где их доказательства» (table of all 72, link `tickets/NN.md` +
  anchor of the full proof in lectures 33–64 or the register `MathInMind/ru/lectures/`);
  «Ключевые определения для допуска»; «Чистилище: семестр 1» (~100 follow-ups on lectures 0–32);
  «Контрпримеры и что если убрать условие» (~40); «Пробные пересдачи» (3 variants, full solutions).
- [ ] Link it from `MathInMind/ru/exam/index.md`.
- [ ] Optional: add «Доказательство», «Задачи», «Если снять условие» to the 72 ticket files.

**Check:** exam validator prints «Reexam master: 72 tickets linked».

---

## G3. Chapters 22–26 (lecturer's numbering), RU → EN → ES

**Model:** any `MathInMind/ru/NN-*.md` chapter (e.g. `16-implicit-functions-extrema.md`) for course style;
`MathInMind/ru/lectures/17-higher-derivatives-6-4.md` for §-numbered headings.

| File (ru/en/es) | Frontmatter `lecturer_chapter` | Lectures | Profile |
|---|---|---|---|
| `22-taylor-implicit-extrema.md` | 6 (§6.5–§6.7) | 65–68 | 16 |
| `23-numerical-series.md` | 7 (§7.1–§7.5) | 67–72 | 4 |
| `24-functional-power-series.md` | 8 (§8.1–§8.4) | 71–76 | 10 |
| `25-parameter-integrals.md` | 9 (§9.1–§9.3) | 75–80 | 10 |
| `26-multiple-riemann-integral.md` | 10 (§10.1–§10.4) | 79–84 | 17 |

**Per file:** frontmatter `chapter`, `part: "Семестр 3: главы лектора"`, `numbering: lecture`,
`lecturer_chapter: K`; goal; `## §K.s. …` headings; every numbered definition/theorem/lemma/corollary of
those lectures as a labelled blockquote under its own number; worked example; typical mistakes; exercises
with one `<details>` answer block.

**After the RU files:**
- [ ] Register in `scripts/course_layout.py` → `LECTURE_CHAPTERS` (line 68) with the profiles above.
- [ ] List in `MathInMind/{ru,en,es}/index.md`; cross-links from chapters 04, 08, 10, 11, 16, 17.
- [ ] Terms in `scripts/term_registry.py` (+ `_LABELS`, glossary) — the list is in `GOALS.md` G3;
  move «мера Жордана» off `lebesgue-measure`.
- [ ] EN and ES versions (same structure, translated).

**Check:** `python3 scripts/validate_course.py` (headings, completeness, RU/EN/ES parity).

- [ ] 22 ru · [ ] 23 ru · [ ] 24 ru · [ ] 25 ru · [ ] 26 ru · [ ] registry · [ ] terms
- [ ] 22–26 en · [ ] 22–26 es

---

## G4. EN/ES translations of lectures 65–84

**Files:** `MathInMind/{en,es}/lectures-2025-26/lecture-65-66.md … lecture-83-84.md` (10 per language).
**Model:** the existing EN/ES translation of `lecture-63-64.md`.

- Translate prose only; formulas, `#p0NN` page anchors, `#def/#thm` labels and figures stay byte-identical.
- [ ] After all 20 files: `TRANSLATED_UP_TO = LAST_LECTURE` in `scripts/course_layout.py` (line 24);
  restore language links in the RU nav lines; replace «Russian only» notes in EN/ES lecture indexes by
  full tables.

**Check:** `python3 scripts/build_views.py && python3 scripts/build_views.py --check` and the
notebook-batch check (RU/EN/ES parity).

- en: [ ] 65-66 · [ ] 67-68 · [ ] 69-70 · [ ] 71-72 · [ ] 73-74 · [ ] 75-76 · [ ] 77-78 · [ ] 79-80 · [ ] 81-82 · [ ] 83-84
- es: [ ] 65-66 · [ ] 67-68 · [ ] 69-70 · [ ] 71-72 · [ ] 73-74 · [ ] 75-76 · [ ] 77-78 · [ ] 79-80 · [ ] 81-82 · [ ] 83-84

---

## G5. Audit of chapters 01–21

One `ISSUES.md` «Open» row per session: fix in ru/en/es, move the row to «Closed». Then one chapter per
session: recompute worked examples and exercise answers.

## G6. Lectures 85–98

Blocked until the material arrives. Steps are in `GOALS.md` G6.

---

## Git (this project only)

```bash
git log --format='%an %ae %cn %ce' -3        # must show NikiHunter only, never Natan7217
git push git@github-matan:NikiHunter/MATAN.git main
```

Commit message ends with
`Co-Authored-By: NikiHunter <224284622+NikiHunter@users.noreply.github.com>` and Claude's trailer.

## Full check

```bash
python3 scripts/build_views.py && python3 scripts/build_views.py --check
python3 scripts/validate_course.py
python3 scripts/validate_exam_track.py --source-safe
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 ocr/check_issues.py && python3 ocr/check_formulas.py
```

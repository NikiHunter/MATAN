# Obsidian-vault: конспект по математическому анализу (семестр 3)

Трёхъязычное хранилище Obsidian: одно и то же содержание на русском (`ru/`),
английском (`en/`) и испанском (`es/`). Источник — рукописный конспект,
расшифрованный в `../ocr/raw/`; лекции для чтения без Obsidian — в `../lectures/`.

## Как открыть

1. Obsidian → «Open folder as vault» → выбрать каталог `obsidian/`.
2. Точка входа — `ru/00 Карта (MOC).md` (или `en/00 Map (MOC).md`, `es/00 Mapa (MOC).md`).
3. Граф: `Ctrl/Cmd + G`. Цвета узлов заданы в `.obsidian/graph.json` по типу заметки.

## Структура

```
obsidian/
├── .obsidian/graph.json     цвета групп в графе
├── .obsidian/app.json       настройки: вложения в assets/, wikilinks, frontmatter
├── assets/p009_fig1.jpg     вырезка рисунка со страницы p009
├── ru/  Понятия/ Лекции/ Глоссарий.md  00 Карта (MOC).md
├── en/  Concepts/ Lectures/ Glossary.md  00 Map (MOC).md
└── es/  Conceptos/ Clases/ Glosario.md  00 Mapa (MOC).md
```

Имена папок и файлов локализованы, `id` во frontmatter — всегда ASCII и одинаков
во всех трёх языках, поэтому заметки сопоставимы между ветками.

## Соглашения

- Одна заметка — одно утверждение: определение, теорема, лемма, свойство, пример
  или метод. `type` во frontmatter принимает одно из этих значений; служебные
  заметки (карта, глоссарий) имеют `type: note` и `type: lecture` соответственно.
- Frontmatter: `id`, `type`, `semester`, `lang`, `aliases`, `tags`,
  `source_pages`, `translations`, `status`.
- Теги: `analysis/taylor`, `analysis/implicit`, `analysis/extrema`,
  `analysis/series`, плюс `sem3` и тип заметки. По тегам работает раскраска графа.
- Callouts: `[!definition]`, `[!theorem]`, `[!proof]-` (свёрнутый),
  `[!warning]`, `[!todo]`, `[!editor]`.
- Лекции (`Лекции/`, `Lectures/`, `Clases/`) — скелеты: программа, встроенные
  через `![[...]]` заметки понятий, список открытых пометок и ссылка на полный
  текст лекции в `../lectures/sem3/`.
- Формулы записаны в plain MathJax (`$...$`, `$$...$$`), как в `../lectures/`;
  в трёх языках они совпадают посимвольно.

## Пометки неопределённости

Каждая спорная места помечена `⟦ID⟧` (тип + номер), полное описание — в
`../ocr/ISSUES.md`. В заметках понятий пометки собраны в callout
`> [!warning]`; ни одна пометка не потеряна и не переименована.
Пока решения по `ISSUES.md` не приняты, все заметки имеют `status: draft`.

Ссылки внутри тела заметки ведут только в свою языковую ветку; переход на другой
язык — через поле `translations` и раздел «Другие языки» в конце заметки.

## Проверки

```bash
python3 obsidian/check_links.py        # wikilinks, сироты, дубликаты, YAML-frontmatter
python3 ocr/check_formulas.py obsidian # парность знаков формул, begin/end
python3 ocr/check_issues.py            # ⟦ID⟧ в ocr/raw ↔ ocr/ISSUES.md
```

Сам этот README — служебный файл, а не заметка: оба чекера его пропускают
(он не имеет frontmatter). `check_links.py` не требует зависимостей; если установлен PyYAML, дополнительно
разбирает frontmatter и проверяет обязательные поля.

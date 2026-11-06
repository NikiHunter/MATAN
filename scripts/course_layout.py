"""Course structure shared by the build and the validators.

Two kinds of chapters live side by side in ``MathInMind/{lang}/``:

* the 21 *classic* chapters (``01``–``21``) with their own section numbers
  ``N.M`` and named statements (see ``term_registry.CHAPTER_STATEMENTS``);
* *lecture-numbered* chapters (``22`` onwards) that follow the lecturer's
  chapters and paragraphs: headings ``## §K.s`` and statements such as
  «Теорема 7.3.2» keep the numbers of the 2025/26 lectures.

To add lectures 85–98, extend the last ``SEMESTERS`` row; to add the chapters
for the lecturer's chapters 11–13, append ``LectureChapter`` rows.
"""

from __future__ import annotations

from dataclasses import dataclass

# (semester, first lecture, last lecture) of the 2025/26 notes.
SEMESTERS = ((1, 0, 32), (2, 33, 64), (3, 65, 84))
LAST_LECTURE = SEMESTERS[-1][2]
# Lectures after this number exist in Russian only until their English and
# Spanish translations are added; then raise it to LAST_LECTURE.
TRANSLATED_UP_TO = 72


def semester_of(lecture: int) -> int:
    for semester, first, last in SEMESTERS:
        if first <= lecture <= last:
            return semester
    raise ValueError(f"lecture {lecture} is outside 0–{LAST_LECTURE}")


CLASSIC_CHAPTERS = (
    "01-logic-sets-functions.md",
    "02-real-numbers.md",
    "03-sequences.md",
    "04-numeric-series.md",
    "05-limits-continuity.md",
    "06-derivatives.md",
    "07-taylor-convexity.md",
    "08-riemann-integration.md",
    "09-improper-integrals-applications.md",
    "10-function-sequences-series.md",
    "11-power-series.md",
    "12-fourier-series.md",
    "13-metric-spaces.md",
    "14-several-variables.md",
    "15-multivariable-differentiation.md",
    "16-implicit-functions-extrema.md",
    "17-multiple-integrals.md",
    "18-vector-calculus.md",
    "19-measure-theory.md",
    "20-lebesgue-integration.md",
    "21-lp-spaces.md",
)


@dataclass(frozen=True)
class LectureChapter:
    number: int  # course chapter, the filename prefix
    filename: str
    lecturer_chapter: int  # K in «§K.s» and «Теорема K.s.i»
    sections: tuple[int, int]  # first and last paragraph s of chapter K covered here
    profile: int  # classic chapter whose term filter (term.chapters) this chapter borrows


LECTURE_CHAPTERS: tuple[LectureChapter, ...] = ()

CHAPTERS = CLASSIC_CHAPTERS + tuple(c.filename for c in LECTURE_CHAPTERS)
LINKING_PROFILE = {c.number: c.profile for c in LECTURE_CHAPTERS}


def lecture_chapter(number: int) -> LectureChapter | None:
    return next((c for c in LECTURE_CHAPTERS if c.number == number), None)


def chapter_for_section(lecturer_chapter: int, section: int) -> int | None:
    """Course chapter that contains the lecturer's paragraph §K.s, if any."""
    for c in LECTURE_CHAPTERS:
        if c.lecturer_chapter == lecturer_chapter and c.sections[0] <= section <= c.sections[1]:
            return c.number
    return None

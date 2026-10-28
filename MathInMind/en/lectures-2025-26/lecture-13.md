---
title: "Lecture 13 — Upper and lower limits, fundamental sequences, the Cauchy criterion"
lang: en
course: "Mathematical Analysis, 2025/26"
lecture: 13
date: 2025-10-16
source: "ma25_26_лекция_13_notes.pdf"
---
# Lecture 13 — Upper and lower limits, the Bolzano–Cauchy criterion

[← Lectures 11–12](lecture-11-12.md) · [Lecture index](index.md) · [Lecture 14 →](lecture-14.md) · [Terms & theorems](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-13.md) · [Español](../../es/lectures-2025-26/lecture-13.md)

> **Source:** `ma25_26_лекция_13_notes.pdf` — 18 pages: typed slides with a text layer (pages 1–4, 7, 13–14, 16) and handwritten pages without a usable text layer (pages 5, 6, 8–12, 15, 17, 18). Handwritten pages were transcribed from their images. PDF page numbers are given in the headings.
>
> **Editor's note.** The lecture date is taken from the footer of the slides ("16 October 2025").

## Typed slides 1–4. Introduction and definition of upper and lower limits

**Quote of the day:** "I'm a wicked witch . . . I got up on the wrong foot . . . I flew off on the wrong broom . . . And I flew in the wrong direction . . . "

**Aim of the lecture.** Introduce the notions of [upper and lower limits](#def-2-3-9) of a sequence. Prove a theorem on the properties of upper and lower limits. Define a [fundamental sequence](#def-2-3-10) (a Cauchy sequence). Prove the [Bolzano–Cauchy criterion](#thm-2-3-7) for the convergence of a sequence.

<a id="def-2-3-9"></a>
### Definition 2.3.9 (upper and lower limits)

Let a real sequence $`\{x_n\}`$ be [bounded above](lecture-05-06.md#def-1-3-7). The quantity

```math
\varlimsup_{n\to\infty} x_n = \lim_{n\to\infty} \sup_{k\ge n} x_k
```

is called the **upper limit** of the sequence $`\{x_n\}`$.

Let a real sequence $`\{x_n\}`$ be bounded below. The quantity

```math
\varliminf_{n\to\infty} x_n = \lim_{n\to\infty} \inf_{k\ge n} x_k
```

is called the **lower limit** of the sequence $`\{x_n\}`$.

## Handwritten page 5 (PDF p. 5). Remarks on upper and lower limits

Let $`z_n = \sup_{k \ge n} x_k`$. Then $`\varlimsup x_n = \lim z_n`$.

- If $`\{x_n\}`$ is not bounded above, then $`\varlimsup_{n\to\infty} x_n = +\infty`$.
- If $`\{x_n\}`$ is not bounded below, then $`\varliminf_{n\to\infty} x_n = -\infty`$.

**Remark.** $`\varlimsup x_n`$ and $`\varliminf x_n`$ exist in $`\overline{\mathbb{R}}`$, and $`\varliminf x_n \le \varlimsup x_n`$.

Below in the handwriting: $`x_1, x_2, x_3, x_4, \dots`$; $`z_1 = \sup_{k \ge 1} x_k = \sup x_n`$, $`z_2 = \sup_{k \ge 2} x_k`$, $`z_3 = \sup_{k \ge 3} x_k`$, whence $`z_1 \ge z_2 \ge z_3 \ge \dots`$

## Handwritten page 6 (PDF p. 6). Boundedness and partial limits

If $`\{x_n\}`$ is bounded, then $`\exists a, b \in \mathbb{R}`$ with $`a \le b`$ and $`\forall n \in \mathbb{N}`$: $`a \le x_n \le b`$, whence $`a \le \dots \le z_2 \le z_1 \le b`$.

Recall that a point $`a`$ is called a **partial limit** of the sequence $`\{x_n\}`$ if there is a [subsequence](lecture-11-12.md#def-2-3-7) $`\{x_{n_k}\}`$ with $`x_{n_k} \to a`$.

## Typed slide 7. Theorem on upper and lower limits

<a id="thm-2-3-5"></a>**Theorem 2.3.5.** Let $`\{x_n\}`$ be a real sequence. Then the following statements hold.

1. The upper limit is the greatest, and the lower limit is the least, of the [partial limits](lecture-11-12.md#def-2-3-8) of $`\{x_n\}`$.
2. The limit of $`\{x_n\}`$ in $`\mathbb{R}`$ exists if and only if $`\varliminf x_n = \varlimsup x_n`$. In that case $`\lim x_n`$ equals their common value.

## Handwritten page 8 (PDF p. 8). Proof of Theorem 2.3.5, part A

**Proof ([Theorem 2.3.5](#thm-2-3-5)).**

**A)** Let $`\{x_n\}`$ be bounded. Denote $`b := \varlimsup x_n`$. We prove that $`b`$ is a partial limit.

$`b = \varlimsup x_n = \lim_{n\to\infty} z_n`$, $`z_n = \sup_{k\ge n} x_k`$; $`z_1 \ge z_2 \ge z_3 \ge \dots`$ $`\Rightarrow`$ $`\forall n`$: $`z_n \ge b`$.

$`\forall \varepsilon > 0`$ $`\forall N`$: $`z_{N+1} = \sup\{x_{N+1}, x_{N+2}, \dots\} > b - \varepsilon`$ $`\Rightarrow`$ $`\exists n > N`$: $`x_n > b - \varepsilon`$.

Then we find:
- $`n_1`$: $`x_{n_1} > b - 1`$;
- $`n_2`$: $`n_2 > n_1`$ and $`x_{n_2} > b - \frac{1}{2}`$;
- …
- $`n_k`$: $`n_k > n_{k-1}`$ and $`x_{n_k} > b - \frac{1}{k}`$.

## Handwritten page 9 (PDF p. 9). Continuation of the proof of Theorem 2.3.5

Altogether we have constructed a subsequence $`\{x_{n_k}\}`$ with $`b - \frac{1}{k} < x_{n_k} \le z_{n_k}`$.

$`\{z_{n_k}\}`$ is a subsequence of $`\{z_n\}`$, and $`z_n \to b`$, so $`z_{n_k} \to b`$. By the [squeeze theorem](lecture-08.md#thm-2-1-4) $`x_{n_k} \to b`$, i.e. $`b`$ is a partial limit.

If $`\{x_{m_\ell}\}`$ is a subsequence of $`\{x_n\}`$ and $`x_{m_\ell} \to \beta`$, then $`x_{m_\ell} \le z_{m_\ell} \to b`$, whence $`\beta \le b`$. That is, $`b`$ is the **greatest** partial limit of $`\{x_n\}`$.

## Handwritten page 10 (PDF p. 10). The lower limit is the least partial limit

Similarly one proves that $`\varliminf x_n`$ is the least partial limit.

Let $`a = \varliminf x_n = \lim_{n\to\infty} y_n`$, where $`y_n = \inf_{k\ge n} x_k`$ (circled in the handwriting). Then $`z_n = \sup_{k\ge n} x_k`$ and $`y_n \le x_n \le z_n`$ for all $`n`$.

If $`\varliminf x_n = \varlimsup x_n`$, then by the squeeze theorem $`x_n \to \varliminf x_n = \varlimsup x_n`$, i.e. $`\lim x_n = \varliminf x_n = \varlimsup x_n`$ exists.

> **Editor's note.** In the line at the top of the page defining $`z_n`$ and $`y_n`$, the handwriting uses $`x_{n_k}`$; in the circled formula and in the subsequent computations it is $`x_k`$. The version with $`x_k`$ is used here.

## Handwritten page 11 (PDF p. 11). Completion of Theorem 2.3.5

If $`\lim x_n`$ exists, then all partial limits, in particular $`\varliminf x_n`$ and $`\varlimsup x_n`$, coincide with it.

**B)** Let $`\{x_n\}`$ be bounded above but not below. Then $`\varliminf x_n = -\infty`$, so one can choose a subsequence tending to $`-\infty`$, and $`-\infty`$ is a partial limit. Of course, $`-\infty`$ is less than any partial limit (if there are any).

That $`\varlimsup x_n`$ is the greatest partial limit of $`\{x_n\}`$ is proved exactly as in part A.

If $`\varliminf x_n = \varlimsup x_n`$, then $`z_n = \sup_{k\ge n} x_k \to -\infty`$, so $`x_n \to -\infty`$, since $`x_n \le z_n`$.

## Handwritten page 12 (PDF p. 12). The converse and case C

Conversely, if $`\lim x_n = -\infty`$, then $`\varlimsup x_n = -\infty`$ as a partial limit.

The case in which $`\{x_n\}`$ is bounded below but not above is analogous.

**C)** If $`\{x_n\}`$ is bounded neither above nor below, then:

- **Statement 1** of the theorem is obvious: $`-\infty = \varliminf x_n < \varlimsup x_n = +\infty`$;
- **Statement 2** of the theorem is not realized (written briefly in the handwriting).

## Typed slide 13. Fundamental sequence

<a id="def-2-3-10"></a>**Definition 2.3.10.** A sequence $`\{x_n\}`$ is said to *converge in itself* if

```math
\forall \varepsilon > 0\ \exists N\ \forall n, l > N:\ |x_n - x_l| < \varepsilon.
```

A sequence that converges in itself is also called a **fundamental sequence** or a **Cauchy sequence**.

## Typed slide 14. Boundedness of a fundamental sequence

<a id="thm-2-3-6"></a>**Theorem 2.3.6.**

1. A fundamental sequence is bounded.
2. If a fundamental sequence has a convergent subsequence, then the sequence itself converges.

## Handwritten page 15 (PDF p. 15). Proof of Theorem 2.3.6, item ①

**Proof ([Theorem 2.3.6](#thm-2-3-6)).**

**①** $`\{x_n\}`$ converges in itself. Take $`\varepsilon = 1`$. $`\exists N`$: $`\forall n, l > N`$: $`|x_n - x_l| < 1`$.

In particular, $`|x_n - x_{N+1}| < 1`$ for all $`n > N`$. Then for $`n > N`$:

```math
|x_n| = |x_n - x_{N+1} + x_{N+1}| \le |x_n - x_{N+1}| + |x_{N+1}| < 1 + |x_{N+1}|.
```

Put $`R = \max\{|x_1|, |x_2|, \dots, |x_N|,\ 1 + |x_{N+1}|\}`$. Then $`|x_n| \le R`$ for all $`n \in \mathbb{N}`$.

**②** To be proved as an exercise.

## Typed slide 16. Bolzano–Cauchy criterion

<a id="thm-2-3-7"></a>**Theorem 2.3.7.** A real sequence converges if and only if it converges in itself.

## Handwritten pages 17–18 (PDF p. 17–18). Proof of Theorem 2.3.7

**Proof ([Theorem 2.3.7](#thm-2-3-7)).**

**(⇒)** Let $`\lim x_n = a`$. We show that $`\{x_n\}`$ converges in itself.

$`\forall \varepsilon > 0\ \exists N`$: $`\forall n > N`$: $`|x_n - a| < \frac{\varepsilon}{2}`$.

$`\forall n, m > N`$: $`|x_n - x_m| = |x_n - a + a - x_m| \le |x_n - a| + |x_m - a| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon`$. Hence $`\{x_n\}`$ converges in itself.

**(⇐)** Let $`\{x_n\}`$ converge in itself. Then:

1. by item ① of [Theorem 2.3.6](#thm-2-3-6), $`\{x_n\}`$ is bounded;
2. by the [Bolzano–Weierstrass selection principle](lecture-11-12.md#thm-2-3-4), one can choose a convergent subsequence $`\{x_{n_k}\}`$ from $`\{x_n\}`$;
3. by item ② of [Theorem 2.3.6](#thm-2-3-6), since $`\{x_{n_k}\}`$ converges, $`\{x_n\}`$ also converges.

> **Editor's note.** In step 3 the handwriting refers to "item ②"; by meaning this is item ② of [Theorem 2.3.6](#thm-2-3-6) (on a convergent subsequence of a fundamental sequence).

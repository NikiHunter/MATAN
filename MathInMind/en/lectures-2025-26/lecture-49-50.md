---
title: "Lectures 49–50 — Absolute convergence, Dirichlet's and Abel's tests"
lang: en
course: "Mathematical Analysis, 2025/26"
lecture: 49-50
semester: 2
date: 2026-04-09
source: "ma25_26-lectures_49-50_notes.pdf"
pdf_pages: 14
typed_slides: 10
archive_file: "Лекция 49-50.md"
---
# Lectures 49–50 — Absolute convergence, Dirichlet's and Abel's tests

[Lecture index](index.md) · [Русский](../../ru/lectures-2025-26/lecture-49-50.md) · [Español](../../es/lectures-2025-26/lecture-49-50.md) · [Previous: 47–48](lecture-47-48.md) · [Continuation: lectures 51–52](../../../source/MathInMind/МАТАН_Л/Лекция%2051-52.md)

> **Source:** `ma25_26-lectures_49-50_notes.pdf` — 14 PDF pages, 10 printed slides; the printed date is 9 April 2026. Printed pages: 1–7, 9, 12, 14. Handwritten pages: 8, 10–11, 13. Every page is listed exactly once. Handwritten additions on printed slides 6 and 7 are identified separately.
>
> **Semester-2 duplication.** Semester 1 ends with lecture 32; semester 2 spans lectures 33–64. The material fully overlaps [§4.5, “Improper integrals”](../../ru/lectures/06-improper-integrals-4-5.md) and is also part of the [semester-2 register](../../ru/lectures/index.md). The archived original is preserved without renaming: [“Лекция 49-50.md”](../../../source/MathInMind/МАТАН_Л/Лекция%2049-50.md). This link does not replace the independent full transcription.
>
> **Limits and qualifications.** Convergence of an improper integral means an ordinary finite one-sided limit. No Cauchy principal value is implied. At an interior or two-sided singularity, each one-sided part must be checked separately; Newton–Leibniz is not applied across a singularity without proof.

## Printed slide 1 (PDF p. 1). Title

“Mathematical Analysis,” lectures 49–50, 9 April 2026; D. E. Apushkinskaya, RUDN University.

## Printed slide 2 (PDF p. 2). Quote and illustration

“An integral in which infinity occurs is called an improper integral. This is not a very good name, since all the other integrals do not belong to anyone either.”

In the original cartoon, a large integral sign holds the infinity symbol and says, “Poor orphans!”; the smaller integral signs cry, “Ow!” The illustration is taken from the PDF and has not been redrawn.

![Original cartoon about improper integrals, printed slide 2 (PDF p. 2)](../../assets/lectures-2025-26/lec49-50-p02-improper-integral-cartoon.jpg)

## Printed slide 3 (PDF p. 3). Lecture goals

Improper integrals; substitution and integration by parts for improper integrals; convergence tests; absolute convergence; Dirichlet's and Abel's tests.

## Chapter 4, §5. Improper integrals

### Printed slide 4 (PDF p. 4). Remarks on convergence

1. Integrals of nonnegative functions equivalent near a singular point converge or diverge together.
2. Convergence of $\int_a^{+\infty}f$ does not imply $f(x)\to0$ as $x\to+\infty$, even if $f\ge0$ and is continuous.
3. Bounded partial integrals are necessary but not sufficient for convergence. For example, $\int_0^{+\infty}\cos x\,dx$ diverges because $\int_0^A\cos x\,dx=\sin A$ has no limit as $A\to+\infty$.

### Printed slide 5 (PDF p. 5). Absolute convergence: definition

**Definition 4.5.4.** Let $-\infty<a<b\le+\infty$, $f\in\mathcal R_{loc}[a,b)$. The integral $\int_a^b f$ is absolutely convergent if $\int_a^b|f|$ converges.

### Printed slide 6 (PDF p. 6). Properties of absolute convergence

1. If $\int_a^b f$ and $\int_a^b g$ converge absolutely and $\alpha,\beta\in\mathbb R$, then $\int_a^b(\alpha f+\beta g)$ converges absolutely. A handwritten note on the slide gives

$$
|\alpha f+\beta g|\le|\alpha|\,|f|+|\beta|\,|g|,
$$

followed by the comparison test.

2. If $\int_a^b f$ exists in the extended real line, then

$$
\left|\int_a^b f\right|\le\int_a^b|f|.
$$

### Printed slide 7 (PDF p. 7). Ordinary and absolute convergence

**Lemma 4.5.6.** Absolute convergence implies convergence.

1. The converse is false: an integral may converge without converging absolutely.
2. If an integral converges but not absolutely, it is called conditionally (or non-absolutely) convergent.
3. If $\int_a^b f$ converges conditionally while $\int_a^b g$ converges absolutely, then $\int_a^b(f+g)$ converges conditionally. The slide notes the identity $f=(f+g)-g$.

### Handwritten page (PDF p. 8). Proof of Lemma 4.5.6

Let $\varepsilon>0$. By the Cauchy criterion for absolute convergence, choose $\Delta\in(a,b)$ such that for all $A,B\in(\Delta,b)$ with $A<B$,

$$
\int_A^B|f|<\varepsilon.
$$

Then

$$
\left|\int_A^Bf\right|\le\int_A^B|f|<\varepsilon,
$$

so the Cauchy criterion holds for $\int_a^b f$ and the original integral converges.

### Printed slide 8 (PDF p. 9). Dirichlet's test

**Theorem 4.5.4.** Let $f\in C([a,b))$, $g\in C^1([a,b))$, and let $g$ be monotone. Suppose

1. $g(x)\to0$ as $x\to b-$;
2. there is an $M>0$ such that

$$
\left|\int_a^Bf(x)\,dx\right|\le M\qquad\text{for all }B<b,
$$

Then the improper integral $\int_a^{\to b}f(x)g(x)\,dx$ converges.

### Handwritten pages (PDF pp. 10–11). Proof of Dirichlet's test

Set $F(x)=\int_a^x f$, so $F(a)=0$ and $|F(x)|\le M$. For finite $B<b$, integration by parts gives

$$
\int_a^Bfg=F(B)g(B)-\int_a^BFg'.
$$

The first term tends to zero because $F$ is bounded and $g(B)\to0$. Since the differentiable monotone function $g$ has derivative $g' $ of constant sign,

$$
\int_a^{\to b}|Fg'|
\le M\int_a^{\to b}|g'|
=M\left|g(b-)-g(a)\right|<+\infty.
$$

Thus $\int Fg'$ converges absolutely, and integration by parts proves convergence of $\int fg$. The handwritten pages explicitly justify the endpoint term and the absolute convergence of the integral containing $Fg'$.

### Printed slide 9 (PDF p. 12). Abel's test

**Theorem 4.5.5.** Let $f\in C([a,b))$, $g\in C^1([a,b))$, and let $g$ be monotone. If $g$ is bounded and $\int_a^{\to b}f(x)\,dx$ converges, then $\int_a^{\to b}f(x)g(x)\,dx$ converges.

### Handwritten page (PDF p. 13). Proof of Abel's test

A bounded monotone function has a finite limit $\alpha=\lim_{x\to b-}g(x)$. The function $g-\alpha$ is monotone and tends to zero, while the partial integrals $F(B)=\int_a^Bf$ are bounded because the integral of $f$ converges. Dirichlet's test gives convergence of $\int_a^{\to b}f(g-\alpha)$. By hypothesis, $\alpha\int_a^{\to b}f$ also converges. Adding,

$$
\int_a^{\to b}fg
=\int_a^{\to b}f(g-\alpha)+\alpha\int_a^{\to b}f
$$

converges.

### Printed slide 10 (PDF p. 14). Weaker assumptions

Theorems 4.5.4 and 4.5.5 remain valid under weaker assumptions: $f\in\mathcal R_{loc}([a,b))$ and $g$ is monotone on $[a,b)$.

---

**Navigation:** [Lectures 47–48](lecture-47-48.md) · [Index](index.md) · [Archived lectures 51–52](../../../source/MathInMind/МАТАН_Л/Лекция%2051-52.md) · [Source and illustrations](../../assets/lectures-2025-26/provenance-45-50.md).

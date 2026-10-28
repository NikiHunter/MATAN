---
title: "Lecture 7 — Maximum and minimum of a finite set, consequences in ℤ and ℕ, density of ℚ in ℝ"
lang: en
course: "Mathematical Analysis, 2025/26"
lecture: 7
source: "ma25_26_лекция_7_notes.pdf"
aliases: ["Lecture 7 (en)"]
tags: [mathinmind/en, mathinmind/lecture]
---
# Lecture 7 — Maximum and minimum, integer part, density of $\mathbb{Q}$ in $\mathbb{R}$

[[en/lectures-2025-26/lecture-05-06|← Lectures 5–6]] · [[en/lectures-2025-26/index|Lecture index]] · [[en/lectures-2025-26/lecture-08|Lecture 8 →]] · [[en/term-index|Terms & theorems]] · [[ru/lectures-2025-26/lecture-07|Русский]] · [[es/lectures-2025-26/lecture-07|Español]]

> [!info] Source
> `ma25_26_лекция_7_notes.pdf` — 13 pages: typed slides with a text layer (pages 1–4, 9) and handwritten pages whose text layer is garbled (pages 5–8, 10–13). Handwritten pages were transcribed from their images. The figures from pages 6, 11 and 12 are embedded as illustrations.
>
> **Editor's note on numbering.** On slide 4 the theorem on the maximum and minimum of a finite set is numbered 1.3.2; in the handwritten proof of [[#^cor-1-3-1|Corollary 1.3.1]] (page 7) the text refers to "Theorem 1.4.2" — this is kept as written in the handwriting. The numbers of definitions and theorems have not been changed.

## Slide 2. Quote of the day

> Everything that happens happens for the best. It just isn't always for yours.

## Slide 3. Aim of the lecture

- Prove consequences of the statements about the maximum and minimum of a finite set.
- Talk about the density of the set of rational numbers.

## §3. Real numbers

### Slide 4. Existence of maximum and minimum of a finite set

> [!theorem] Theorem 1.3.2
> Every finite subset of $\mathbb{R}$ has a largest and a smallest element.

^thm-1-3-2

> [!corollary] Corollary 1.3.1
> Every non-empty subset of $\mathbb{Z}$ that is bounded above (below) has a largest (smallest) element.

^cor-1-3-1

> [!corollary] Corollary 1.3.2
> Every non-empty subset of $\mathbb{N}$ has a smallest element.

^cor-1-3-2

### Handwritten page 5 (PDF p. 5). Proof of Theorem 1.3.2

**Proof ([[#^thm-1-3-2|Theorem 1.3.2]]).** We use [[en/01-logic-sets-functions#^example-induction|induction]] on the number $n$ of elements of the set.

**Base of induction** $n = 1$: $A = \{a_1\}$ ⇒ $a_1$ is both the largest and the smallest element ✓.

For definiteness we continue the argument for the maximum.

**Induction hypothesis.** Let the set $A = \{x_1, x_2, \dots, x_n\}$ have a maximum.

Denote $c = \max\{x_1, x_2, \dots, x_n\}$.

**Induction step**: $n \mapsto n+1$, $A = \{x_1, x_2, \dots, x_n, x_{n+1}\}$.

- If $c \le x_{n+1}$, then $x_{n+1} = \max A$;
- if $c > x_{n+1}$, then $c = \max A$.

### Handwritten pages 6–7 (PDF pp. 6–7). Corollary 1.3.1 (integers)

**Proof ([[#^cor-1-3-1|Corollary 1.3.1]]).** Let $A \subset \mathbb{Z}$, $A \ne \varnothing$, with $A$ [[en/lectures-2025-26/lecture-05-06#^def-1-3-7|bounded above]].

Take an arbitrary element $n_0 \in A$ and consider

$$
A_1 = \{ n \in A : n \ge n_0 \}.
$$

Since $A$ is bounded above, $A_1$ is a **finite** set.

![Handwritten page 6: ℤ, n₀, the bound M and the set A₁](../../assets/lectures-2025-26/lec07-p06-integers-bounded-sets.jpg)

Let $M$ be an integer serving as an [[en/02-real-numbers#2.2 Supremum and infimum|upper bound]] of $A$ ⇒ then $A_1$ contains at most [the sentence is cut off at the edge of page 6; its continuation cannot be recovered from the scan].

Then (page 7): $A_1 \subset A \subset \mathbb{Z} \subset \mathbb{R}$; $A_1$ has finitely many elements ⇒ by Theorem 1.4.2, $A_1$ has a largest element. This largest element of $A_1$ is the largest element of $A$.

The case of a set bounded below is treated analogously.

### Handwritten page 7 (PDF p. 7). Corollary 1.3.2 (natural numbers)

**Proof ([[#^cor-1-3-2|Corollary 1.3.2]]).** $A \subset \mathbb{N} \subset \mathbb{Z}$, $A \ne \varnothing$; $\mathbb{N}$ is bounded below by $0$ (as written on the page — the course convention for $\mathbb{N}$ should be checked). ⇒ The result follows from [[#^cor-1-3-1|Corollary 1.3.1]].

### Handwritten page 8 (PDF p. 8). Definition of the integer part

**Definition.** Let $x \in \mathbb{R}$. The largest integer not exceeding $x$ is called the **integer part** of $x$ and is denoted $[x]$.

**Remark.** The existence of the integer part follows from Corollary 1.4.1 ⇒ the definition of the integer part is correct.

**Remark.**

$$
[x] \le x < [x] + 1, \qquad x - 1 < [x] \le x.
$$

Conversely, if $y \in \mathbb{Z}$ and $x - 1 < y \le x$, then $y = [x]$.

In the margin (in green): $x - [x] = \{x\}$ — the **fractional part** of $x$, $0 \le \{x\} < 1$.

### Slide 9. Density of the rational numbers (typed slide with handwritten annotation)

> [!theorem] Theorem 1.3.3
> Every interval contains a rational number.

^thm-1-3-3

> [!corollary] Corollary 1.3.3
> Every interval contains infinitely many rational numbers.

^cor-1-3-3

**Handwritten annotation** (arrow pointing at [[#^thm-1-3-3|Theorem 1.3.3]]): "The property described in [[#^thm-1-3-3|Theorem 1.3.3]] is called the **density** of the set $\mathbb{Q}$ in the set $\mathbb{R}$."

### Handwritten page 10 (PDF p. 10). Proof of Theorem 1.3.3

**Proof ([[#^thm-1-3-3|Theorem 1.3.3]]).** Let $a, b \in \mathbb{R}$, $a < b$ ⇒ $\dfrac{1}{b-a} > 0$.

In the [[en/lectures-2025-26/lecture-05-06#^def-1-3-5|Archimedean axiom]] put $x = 1$, $y = \dfrac{1}{b-a}$ ⇒ by the Archimedean axiom there exists $n \in \mathbb{N}$ with $n > \dfrac{1}{b-a}$ ⇒

$$
\frac{1}{n} < b - a.
$$

Put

$$
c = \frac{[na] + 1}{n} \in \mathbb{Q}.
$$

Then

$$
c = \frac{[na] + 1}{n} \le \frac{na + 1}{n} = a + \frac{1}{n} < a + b - a = b,
$$

$$
c = \frac{[na] + 1}{n} > \frac{na - 1 + 1}{n} = a.
$$

Hence $c \in (a, b)$. ∎

### Handwritten page 11 (PDF p. 11). Corollary 1.3.3: two approaches

**Proof ([[#^cor-1-3-3|Corollary 1.3.3]]).**

**Approach ① — recursion.** Take an interval $(a, b)$. By [[#^thm-1-3-3|Theorem 1.3.3]] there is $c_1 \in \mathbb{Q}$ in the interval $(a, c)$ [green on the page]; by [[#^thm-1-3-3|Theorem 1.3.3]] there is $c_2 \in \mathbb{Q}$ in the interval $(c, b)$ [red]; [[#^thm-1-3-3|Theorem 1.3.3]] is applied again to the point $c$ (marked on the figure); "etc." — the construction continues recursively, as the page indicates.

![Handwritten page 11: recursive construction of rational numbers inside (a, b)](../../assets/lectures-2025-26/lec07-p11-density-corollary.jpg)

**Approach ② — by contradiction.** Suppose some interval $(a, b)$ contains only finitely many rational numbers. Denote by $x_1$ the smallest of them. Then $(a, x_1)$ contains no rational numbers ⇒ a contradiction with [[#^thm-1-3-3|Theorem 1.3.3]].

### Handwritten page 12 (PDF p. 12). "Settling debts": $[0,1]$ is uncountable

**We prove that $[0,1]$ is uncountable.**

**Proof.** Suppose the contrary: let $[0,1]$ be [[en/lectures-2025-26/lecture-01-02#^def-1-2-5|countable]] ⇒ all elements of $[0,1]$ can be listed as

$$
[0,1] = \{ x_1, x_2, \dots, x_{100}, \dots \}.
$$

![Handwritten page 12: the segments [0, 1/3], [1/3, 2/3], [2/3, 1] and the selection of [a₁, b₁]](../../assets/lectures-2025-26/lec07-p12-uncountable-interval.jpg)

Divide $[0,1]$ into three parts: $[0, \tfrac13]$, $[\tfrac13, \tfrac23]$, $[\tfrac23, 1]$. Denote by $[a_1, b_1]$ the one that does not contain $x_1$.

### Handwritten page 13 (PDF p. 13). Continuation

Divide $[a_1, b_1]$ into 3 equal parts and denote by $[a_2, b_2]$ the one that does not contain $x_2$, and so on.

We obtain a sequence of nested segments $\{[a_n, b_n]\}_{n=1}^{\infty}$ such that $x_n \notin [a_n, b_n]$ for all $n$.

By **Cantor's axiom of nested segments** there exists $x^* \in [0,1]$ belonging to all $[a_n, b_n]$. Then $x^* = x_m$ for some $m \in \mathbb{N}$. But by construction $x_m \notin [a_m, b_m]$ — a contradiction. ∎

> [!remark] Editor's note
> The handwritten heading "Отдача долгов" at the top of page 12 is kept as written (literally "Repayment of debts"); the meaning of this annotation is not clear from the scan. The example itself concerns the uncountability of $[0,1]$.

## Non-content pages

- Page 1 is the title page; page 2 is the quote of the day (translated above).
- Pages 5–8 and 10–13 are handwritten and transcribed above; page 9 is a typed slide with a handwritten annotation.

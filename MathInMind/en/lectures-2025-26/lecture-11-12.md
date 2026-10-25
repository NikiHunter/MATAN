---
title: "Lectures 11–12 — Exact bounds, monotone sequences, the number e, subsequences, the Bolzano–Weierstrass theorem"
lang: en
course: "Mathematical Analysis, 2025/26"
lecture: "11–12"
date: 2025-10-09
source: "ma25_26-lectures_11-12_notes.pdf"
---
# Lectures 11–12 — Exact bounds, monotone sequences, subsequences

[Lecture index](index.md) · [Русский](../../ru/lectures-2025-26/lecture-11-12.md) · [Español](../../es/lectures-2025-26/lecture-11-12.md)

> **Source:** `ma25_26-lectures_11-12_notes.pdf` — 37 pages: typed slides with a text layer (pages 1–5, 8–10, 16, 18–20, 23, 26–28, 31, 34–35) and handwritten pages without a usable text layer (pages 6–7, 11–15, 21–22, 24–25, 29–30, 32–33, 36–37). Handwritten pages were transcribed from their images. Typed pages 27 and 34 carry handwritten annotations and are given below with those annotations. PDF page numbers are given in the headings.
>
> **Editor's note.** Numbers of definitions, theorems and lemmas are kept as in the source. The lecture date is taken from the footer of the slides ("9 October 2025").

## Typed slides 1–5. Introduction and nested intervals

**Quote of the day:** "If you have free time, it means you have forgotten to do something!"

**Aim of the lecture.** Investigate the existence of upper and lower bounds. Prove the theorem on nested intervals. Discuss sup and inf, max and min. Prove the theorem on the limit of a monotone sequence. Define the number $e$. Introduce subsequences, limits of subsequences and partial limits of a sequence. Prove lemmas on the properties of limits of subsequences. Justify the Bolzano–Weierstrass selection principle.

### §3. Exact bounds of numerical sets and monotone sequences

**Definition (nested intervals).** A sequence $\{[a_n, b_n]\}_{n=1}^{\infty}$ is called a **sequence of nested intervals** if

$$
a_n \le a_{n+1} \le b_{n+1} \le b_n \quad \text{for all } n \quad \text{and} \quad b_n - a_n \to 0.
$$

**Theorem 2.3.1 (nested intervals).** Let $\{[a_n, b_n]\}_{n=1}^{\infty}$ be a sequence of nested intervals. Then

$$
\exists c \in \mathbb{R}: \quad \bigcap_{n=1}^{\infty} [a_n, b_n] = \{c\},
$$

and moreover $a_n \to c$ and $b_n \to c$.

### Handwritten page 6 (PDF p. 6). Proof of Theorem 2.3.1

**Proof (Theorem 2.3.1).**

**①** That $\bigcap_{n=1}^{\infty}[a_n, b_n] \ne \varnothing$ follows from the axiom of nested intervals.

**②** Let $c, d \in \bigcap_{n=1}^{\infty}[a_n, b_n]$. We prove $c = d$.

$$
a_n \le c \le b_n,\quad a_n \le d \le b_n,\quad \forall n \in \mathbb{N} \ \Rightarrow\ a_n - b_n \le c - d \le b_n - a_n.
$$

As $n \to \infty$, both outer quantities tend to $0$ (arrows in the handwriting). By the theorem on passage to the limit in an inequality, $0 \le c - d \le 0$, i.e. $c = d$.

### Handwritten page 7 (PDF p. 7). Continuation: $a_n \to c$, $b_n \to c$

**③** It remains to show that $a_n \to c$ and $b_n \to c$.

From $a_n \le c \le b_n$ it follows that $0 \le c - a_n \le b_n - a_n \to 0$, so $c - a_n \to 0$, i.e. $a_n \to c$.

Similarly for $b_n$: the handwriting reads "$b_n - b_n \le b_n - c \le b_n - a_n$" (with "$= 0$" underlined); by meaning, $0 \le b_n - c \le b_n - a_n \to 0$, whence $b_n \to c$.

> **Editor's note.** On the left side of the inequality for $b_n$ the handwriting says "$b_n - b_n$"; by meaning this is $0$ (underlined as "$=0$"). Corrected in this note only; the handwritten text is otherwise unchanged.

Recall: $E \subset \mathbb{R}$ is called **bounded above** if $\exists M \in \mathbb{R}: x \le M\ \forall x \in E$; the number $M$ is called an upper bound of $E$.

### Typed slides 8–9. Exact bounds

**Definition 2.3.1.** Let $E \subset \mathbb{R}$, $E \ne \varnothing$, and let $E$ be bounded above. The least of the upper bounds of $E$ is called the **least upper bound** (supremum) of $E$ and is denoted $\sup E$.

**Definition 2.3.2.** Let $E \subset \mathbb{R}$, $E \ne \varnothing$, and let $E$ be bounded below. The greatest of the lower bounds of $E$ is called the **greatest lower bound** (infimum) of $E$ and is denoted $\inf E$.

**Definition of sup and inf by inequalities.**

$$
b = \sup E \iff \begin{cases} \forall x \in E: x \le b, \\ \forall \varepsilon > 0\ \exists x \in E: x > b - \varepsilon; \end{cases}
\qquad
a = \inf E \iff \begin{cases} \forall x \in E: x \ge a, \\ \forall \varepsilon > 0\ \exists x \in E: x < a + \varepsilon. \end{cases}
$$

### Typed slide 10. Existence of exact bounds

**Theorem 2.3.2.** Every nonempty subset of $\mathbb{R}$ that is bounded above (below) has an upper (lower) bound.

**Remark.** If a set is not bounded above (below), one sets $\sup E = +\infty$ ($\inf E = -\infty$). With this convention, the supremum and infimum exist in $\mathbb{R}$ for every nonempty set. Boundedness above (below) is equivalent to the inequality $\sup E < +\infty$ ($\inf E > -\infty$).

### Handwritten page 11 (PDF p. 11). Proof of Theorem 2.3.2

**Proof (Theorem 2.3.2).** To be definite, we prove the theorem for a set bounded above. The second statement (a set bounded below) is proved similarly.

Let $E \subset \mathbb{R}$, $E \ne \varnothing$, be bounded above: $\exists M \in \mathbb{R}: x \le M\ \forall x \in E$. Take $x_0 \in E$; then $x_0 \le M$. Denote $[a_1, b_1] := [x_0, M]$. The interval $[a_1, b_1]$ satisfies two conditions:

① $[a_1, b_1] \cap E \ne \varnothing$; ② $(b_1, +\infty) \cap E = \varnothing$.

### Handwritten page 12 (PDF p. 12). Continuation: bisection

Consider the midpoint of $[a_1, b_1]$: $\dfrac{a_1 + b_1}{2} = \dfrac{x_0 + M}{2}$. Two cases are possible:

- **①** If $\left(\dfrac{a_1 + b_1}{2}, b_1\right] \cap E = \varnothing$, put $[a_2, b_2] = \left[a_1, \dfrac{a_1 + b_1}{2}\right]$.
- **②** If $\left(\dfrac{a_1 + b_1}{2}, b_1\right] \cap E \ne \varnothing$, put $[a_2, b_2] = \left[\dfrac{a_1 + b_1}{2}, b_2\right]$.

In either case ① or ② we have $[a_2, b_2] \cap E \ne \varnothing$ and $(b_2, +\infty) \cap E = \varnothing$.

![Handwritten page 12: the interval [x₀, M], its midpoint and the two choices of half](../../assets/lectures-2025-26/lec11-12-p12-bisection-sup.jpg)

> **Editor's note.** In case ② the handwriting has $[a_2, b_2] = [\ldots, b_2]$; by meaning the right endpoint coincides with $b_1$ (i.e. $b_2 = b_1$). The handwritten text is kept unchanged.

### Handwritten page 13 (PDF p. 13). Continuation of the construction

Then take the midpoint of $[a_2, b_2]$ and continue the process…

As a result we have constructed a sequence of nested intervals with the properties

$$
\text{<1>}\ \ [a_n, b_n] \cap E \ne \varnothing, \qquad \text{<2>}\ \ (b_n, +\infty) \cap E = \varnothing.
$$

Moreover $b_n - a_n = \dfrac{b_{n-1} - a_{n-1}}{2} = \dots = \dfrac{b_1 - a_1}{2^{n-1}} \to 0$ as $n \to \infty$.

Then by the theorem on nested intervals (Theorem 2.3.1) there is a unique point $c \in \bigcap_{n=1}^{\infty}[a_n, b_n]$, and $a_n \to c$, $b_n \to c$.

We now check that $c = \sup E$.

### Handwritten page 14 (PDF p. 14). The upper bound

Take $x \in E$. By property <2>, $x \le b_n$ for all $n \in \mathbb{N}$. Passing to the limit as $n \to \infty$ ($b_n \to c$), by the theorem on passage to the limit in an inequality we get $x \le c$, i.e. $c$ is an upper bound of $E$.

Take $\varepsilon > 0$ and show that $c - \varepsilon$ is not an upper bound of $E$. Since $a_n \to c$, there is $N$ such that $\forall n > N$: $|a_n - c| < \varepsilon$, i.e. $c - \varepsilon < a_n < c + \varepsilon$; in particular $c - \varepsilon < a_{[N]+1}$. Then by property <1>: $[a_{[N]+1}, b_{[N]+1}] \cap E \ne \varnothing$.

### Handwritten page 15 (PDF p. 15). Conclusion

That is, there exists $\tilde{x} \in [a_{[N]+1}, b_{[N]+1}] \cap E$, and then $\tilde{x} \ge a_{[N]+1} > c - \varepsilon$. Hence $c$ is the least upper bound, i.e. $c = \sup E$.

**Remark (handwritten).** For $\varnothing$ every number is an upper bound, so the set of upper bounds of $\varnothing$ is not bounded below. It is therefore natural to set $\sup \varnothing = -\infty$; similarly $\inf \varnothing = +\infty$. These conventions give $\sup \varnothing < \inf \varnothing$ (marked in red). For this reason the bounds of $\varnothing$ are not defined.

### Typed slides 16–17. Properties of sup and inf; functions

**Lemma 2.3.1.**

1. If $D \subset E \subset \mathbb{R}$, $D \ne \varnothing$, then $\sup D \le \sup E$ and $\inf D \ge \inf E$.
2. If $E, F \subset \mathbb{R}$, $E, F \ne \varnothing$, $t > 0$, then
$$
\sup(E + F) = \sup E + \sup F,\quad \inf(E+F) = \inf E + \inf F,\quad \sup(tE) = t\sup E,\quad \inf(tE) = t\inf E,
$$
$$
\sup(-E) = -\inf E,\quad \inf(-E) = -\sup E.
$$

**Maximum and minimum of a function on a set.** The maximum and minimum (greatest and least values) of a function on a set are defined analogously.

**Definition 2.3.3.** A function $f$ is called bounded (above, below) on a set $D$ if the set $f(D)$ is bounded (above, below).

### Typed slide 18. Monotone functions

**Definition 2.3.4.** Let $D \subset X \subset \mathbb{R}$. A function $f : X \to \mathbb{R}$ is called

- **increasing** on $D$ if for all $x_1 < x_2$ in $D$ we have $f(x_1) \le f(x_2)$;
- **strictly increasing** on $D$ if for all $x_1 < x_2$ in $D$ we have $f(x_1) < f(x_2)$;
- **decreasing** on $D$ if for all $x_1 < x_2$ in $D$ we have $f(x_1) \ge f(x_2)$;
- **strictly decreasing** on $D$ if for all $x_1 < x_2$ in $D$ we have $f(x_1) > f(x_2)$.

> **Editor's note.** On the slide the definitions of "decreasing" and "strictly decreasing" are written with "$>$"; in the definition of a decreasing function the intended sign is $\ge$ (as for increasing, where it is $\le$). This is recorded as a typographical point; the meaning of the definition is unchanged.

### Typed slide 19. Monotone sequences

**Definition 2.3.5.** A real sequence $\{x_n\}_{n=1}^{\infty}$ is called

- increasing, if $x_n \le x_{n+1}$ for all $n \in \mathbb{N}$;
- strictly increasing, if $x_n < x_{n+1}$ for all $n$;
- decreasing, if $x_n \ge x_{n+1}$ for all $n$;
- strictly decreasing, if $x_n > x_{n+1}$ for all $n$.

> **Editor's note.** The slide writes "$x_n > x_{n+1}$" for "decreasing"; by meaning, for the non-strict case it should be $\ge$, as for increasing.

### Typed slide 20. Limit of a monotone sequence

**Theorem 2.3.3.**

1. Every increasing sequence bounded above converges.
2. Every decreasing sequence bounded below converges.
3. Every monotone bounded sequence converges.

### Handwritten pages 21–22 (PDF p. 21–22). Proof of Theorem 2.3.3

**Proof (Theorem 2.3.3).**

**①** Let $\{x_n\}$ be increasing and bounded above. We must show that $\{x_n\}$ converges. By Theorem 2.3.2, $\exists \sup_{n} x_n = c \in \mathbb{R}$. We prove $\lim x_n = c$.

Take $\varepsilon > 0$. Since $\sup x_n = c$, by the definition of sup there is $N$ with $x_N > c - \varepsilon$. Since $\{x_n\}$ is increasing, $\forall n > N$: $x_n \ge x_N$. By the definition of sup, $\forall n$: $x_n \le c$. Thus $\forall n > N$: $c - \varepsilon < x_N \le x_n \le c < c + \varepsilon$, i.e. $\lim x_n = c$.

**②** Proved similarly (take inf instead of sup).

**③** Follows from ① and ②.

### Typed slide 23. Remarks on Theorem 2.3.3

1. If a sequence is increasing and not bounded above, it tends to $+\infty$.
2. If a sequence is decreasing and not bounded below, it tends to $-\infty$.
3. Every monotone sequence has a limit in $\overline{\mathbb{R}}$, finite or infinite. For every increasing sequence $\lim x_n = \sup x_n$, and for every decreasing sequence $\lim x_n = \inf x_n$.

### Handwritten pages 24–25. The number $e$

**Example (the number $e$).** Let $x_n = \left(1 + \dfrac{1}{n}\right)^n$. We show that $\{x_n\}$ converges.

Put $y_n = \left(1 + \dfrac{1}{n}\right)^{n+1}$. For all $n$: $y_n \ge 1$ (as written in the handwriting; here $1 + \frac1n > 1$). Next

$$
\frac{y_{n-1}}{y_n} = \frac{\left(1 + \frac{1}{n-1}\right)^n}{\left(1 + \frac{1}{n}\right)^{n+1}} = \frac{\left(\frac{n}{n-1}\right)^n}{\left(\frac{n+1}{n}\right)^{n+1}} = \left(\frac{n^2}{n^2-1}\right)^{n+1} \cdot \frac{n-1}{n} = \left(1 + \frac{1}{n^2-1}\right)^{n+1} \cdot \frac{n-1}{n}.
$$

By Bernoulli's inequality (proved earlier: if $n \in \mathbb{Z}_+$ and $x > -1$, then $(1+x)^n \ge 1 + nx$):

$$
\left(1 + \frac{1}{n^2-1}\right)^{n+1} \cdot \frac{n-1}{n} \ge \left(1 + \frac{n+1}{n^2-1}\right) \cdot \frac{n-1}{n} = \left(1 + \frac{1}{n-1}\right)\cdot\frac{n-1}{n} = 1.
$$

Hence $y_{n-1} \ge y_n$, i.e. $\{y_n\}$ is decreasing.

Handwritten page 25 (PDF p. 25): since $\{y_n\}$ is decreasing and $y_n \ge 1$, the sequence $\{y_n\}$ converges (Theorem 2.3.3). Further, $x_n = \dfrac{y_n}{1 + \frac{1}{n}}$, and by the theorem on the limit of a quotient, $\{x_n\}$ converges to the same limit as $\{y_n\}$.

### Typed slide 26. Definition of the number $e$

**Definition 2.3.6.** The limit of the sequence

$$
\left(1 + \frac{1}{n}\right)^n
$$

is called the Napier number, or the base of the natural logarithms, and is denoted by the letter $e$:

$$
e = \lim_{n\to\infty}\left(1 + \frac{1}{n}\right)^n.
$$

### Typed slide 27 with the handwritten note "(exercises)"

In red, "(exercises)" has been added. Remarks-exercises:

1. Let $x_n > 0$ for all $n$ and $\lim \dfrac{x_{n+1}}{x_n} < 1$. Then $x_n \to 0$.
2. $\lim\limits_{n\to\infty} \dfrac{n^k}{a^n} = 0$, $a > 1$, $k \in \mathbb{N}$.
3. $\lim\limits_{n\to\infty} \dfrac{a^n}{n!}$, $a \in \mathbb{R}$.
4. $\lim\limits_{n\to\infty} \dfrac{n!}{n^n} = 0$.

### Typed slide 28. Subsequences

**Definition 2.3.7.** Let $\{x_n\}_{n=1}^{\infty}$ be a sequence in a set $X$ and $\{n_k\}_{k=1}^{\infty}$ a strictly increasing sequence of natural numbers ($n_k < n_{k+1}$ for all $k$). The composition ($\{x_n\}$ is the outer map, $\{n_k\}$ is the inner map) is called a **subsequence** of $\{x_n\}$ and is denoted $\{x_{n_k}\}$.

**Remark.** For a strictly increasing sequence $\{n_k\}$ we have $n_k \ge k$ for all $k$. Indeed, $n_1 \ge 1$ (base of induction), and $n_k \ge k$ implies $n_{k+1} \ge n_k + 1 \ge k + 1$ (induction step).

### Handwritten page 29 (PDF p. 29). Examples of subsequences

Consider the sequence $1, 2, 3, 4, 5, \dots = \{x_1, x_2, x_3, \dots\}$. Subsequences:

- $n_k = 2k$: $2, 4, 6, 8, 10, \dots$
- $n_k = 2k - 1$: $1, 3, 5, 7, 9, \dots$
- $n_k = k^2$: $1, 4, 9, 16, 25, \dots$

### Handwritten page 30 (PDF p. 30). Maps

Let $f: \mathbb{N} \to \mathbb{R}$, $f(n) = x_n$, and $\varphi: \mathbb{N} \to \mathbb{N}$, $\varphi(k) = n_k$. Then $f(\varphi(k)) = f(n_k) = x_{n_k}$.

Diagram: $\mathbb{N}$ (index $k$) $\xrightarrow{\varphi}$ $\mathbb{N}$ (index $n_k$) $\xrightarrow{f}$ $\mathbb{R}$ (value $x_{n_k}$).

**But!** The sequence $\{2, 1, 3, 5, 4, \dots\}$ is **not** a subsequence of $\{x_n\} = \{1, 2, 3, 4, 5, \dots\}$, because the order is violated ($n_k$ must be strictly increasing).

### Typed slide 31. Limits of subsequences

**Lemma 2.3.2.** Every subsequence of a sequence that has a limit tends to the same limit: if $\{x_n\}$ is a real sequence, $\{x_{n_k}\}$ is its subsequence, $a \in \mathbb{R} \cup \{\infty\}$, and $x_n \to a$, then $x_{n_k} \to a$.

**Lemma 2.3.3.** Let $\{x_n\}$ be a real sequence, and let $\{x_{n_k}\}$ and $\{x_{m_l}\}$ be its subsequences whose index sets together make up $\mathbb{N}$; let $a \in \mathbb{R} \cup \{\infty\}$. Then, if $x_{n_k} \to a$ and $x_{m_l} \to a$, also $x_n \to a$.

### Handwritten page 32 (PDF p. 32). Proof of Lemma 2.3.2

**Proof (Lemma 2.3.2).** Let $a \in \mathbb{R}$. Take $\varepsilon > 0$. $x_n \to a \Rightarrow \exists N: \forall n > N$: $|x_n - a| < \varepsilon$. Then if $k > N$, we have $n_k \ge k > N$ (by the remark) $\Rightarrow$ $|x_{n_k} - a| < \varepsilon$.

If $a = \pm\infty$ or $a = \infty$, replace the inequality $|x_n - a| < \varepsilon$ in the argument above by $|x_n| > E$.

### Handwritten page 33 (PDF p. 33). Proof of Lemma 2.3.3

**Proof (Lemma 2.3.3).** To be definite, consider the case $a \in \mathbb{R}$. Take $\varepsilon > 0$.

$x_{n_k} \to a \Rightarrow \exists K: \forall k > K$: $|x_{n_k} - a| < \varepsilon$.
$x_{m_l} \to a \Rightarrow \exists L: \forall l > L$: $|x_{m_l} - a| < \varepsilon$.

Put $N = \max\{K, L\}$. If $n > N$, then:
① either $n = n_k$, and then $k > K$ and $|x_n - a| < \varepsilon$;
② or $n = m_l$, and then $l > L$ and $|x_n - a| < \varepsilon$.

In either case $|x_n - a| < \varepsilon$, i.e. $x_n \to a$.

### Handwritten page 36 (PDF p. 36). Example of a divergent sequence

**Example.** $x_n = (-1)^n$ diverges.

$x_{2k} = (-1)^{2k} = 1 \to 1$; $x_{2k+1} = (-1)^{2k+1} = -1 \to -1$.

> **Editor's note.** The handwriting does not state the conclusion of divergence; it follows from the fact that the sequence has two subsequences with different limits (Lemma 2.3.3).

### Typed slide 34 with a handwritten example: partial limit

**Definition 2.3.8.** A point $a$ is called a **partial limit** of a sequence $\{x_n\}$ if there exists a subsequence $\{x_{n_k}\}$ tending to $a$.

Handwritten, for $x_n = (-1)^n$:

$x_{2k} = (-1)^{2k}$ $\Rightarrow$ $\{x_{2k}\} = \{1, 1, 1, \dots\} \to 1$ (circled).
$x_{2k-1} = (-1)^{2k-1}$ $\Rightarrow$ $\{x_{2k-1}\} = \{-1, -1, -1, \dots\} \to -1$ (circled).

A red note "partial limits" with arrows points to the values $1$ and $-1$.

### Typed slide 35. The Bolzano–Weierstrass theorem

**Theorem 2.3.4 (Bolzano–Weierstrass selection principle).** From every bounded sequence one can extract a convergent subsequence.

**Remark.** If a real sequence is not bounded above (below), one can extract from it a subsequence tending to $+\infty$ ($-\infty$).

### Handwritten pages 36–37 (PDF p. 36–37). Proof of Theorem 2.3.4

**Proof (Theorem 2.3.4).** $\{x_n\}$ is bounded $\iff \forall n \in \mathbb{N}\ \exists a, b \in \mathbb{R},\ a < b$: $a \le x_n \le b$ $\iff$ $\forall n \in \mathbb{N}$: $x_n \in [a, b]$.

Consider the midpoint of $[a, b]$. Denote by $[a_1, b_1]$ the half of $[a, b]$ that contains infinitely many terms of $\{x_n\}$ (i.e. $x_n \in [a_1, b_1]$ for infinitely many indices $n$).

**Remark (handwritten, in red).** If both halves contain infinitely many terms, take either half.

Choose an index $n_1$ with $x_{n_1} \in [a_1, b_1]$. Choose $n_2$ with $n_2 > n_1$ and $x_{n_2} \in [a_2, b_2]$. At step $k$ choose $n_k$ with $n_k > n_{k-1}$ and $x_{n_k} \in [a_k, b_k]$.

We have constructed a sequence of nested intervals $\{[a_k, b_k]\}$ and a subsequence $\{x_{n_k}\}$ of the original sequence. By the theorem on nested intervals, $\exists c \in \mathbb{R}$ with $a_k \to c$, $b_k \to c$. Moreover $a_k \le x_{n_k} \le b_k$, hence $x_{n_k} \to c$.

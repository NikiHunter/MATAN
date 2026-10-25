---
title: "Lecture 15 — Stabilization of sign, arithmetic of limits of functions, composition, one-sided limits, monotone functions, the Cauchy criterion for functions"
lang: en
course: "Mathematical Analysis, 2025/26"
lecture: 15
date: 2025-10-23
source: "ма25_26_лекция_15_notes_pdf.pdf"
---
# Lecture 15 — Properties of limits of functions, one-sided limits, the Cauchy criterion

[Lecture index](index.md) · [Русский](../../ru/lectures-2025-26/lecture-15.md) · [Español](../../es/lectures-2025-26/lecture-15.md)

> **Source:** `ма25_26_лекция_15_notes_pdf.pdf` — 24 pages: typed slides with a text layer (pages 1–4, 6, 9–10, 12–13, 15–16, 18–19, 22), handwritten pages without a usable text layer (pages 5, 7–8, 11, 14, 17, 20, 21, 23–24). Pages 12 and 18 are typed slides with blue handwritten annotations. Handwritten pages were transcribed from their images. PDF page numbers are given in the headings.
>
> **Editor's note.** The lecture date is taken from the footer of the slides ("23 October 2025"). The "quote of the day" on page 2 is a joke; its formulas are given as they appear in the image.

## Typed slides 1–3. Introduction

**Quote of the day (slide 2).** "TYPICAL METHODS OF PROOF":

- *Proof by intimidation:* "As is easily seen, $\left|\bigoplus_{\kappa\in S}(\Re^{F^\alpha(i)})_{i\in U_\kappa}\right| \preceq \aleph_1$ whenever $[\mathfrak{H}]_W \cap F^\alpha(\mathbb{N}) \ne \varnothing$."
- *Proof by obfuscation:* "This statement is a reformulation of Proposition 5.3.18, which follows from Theorem 7.1.24, based on Lemma 2.4.14, which is a consequence of Theorem 7.1.24 and Proposition 5.3.18."
- *Proof by authority:* "Obvious."

**Aim of the lecture.** Prove the theorem on the stabilization of sign. Consider arithmetic operations on functions that have limits. Prove results on the limit of a composition, on passage to the limit in an inequality for functions, and on the squeeze theorem for functions. Define left-hand and right-hand limits. Prove theorems on the limit of a monotone function and discuss the Bolzano–Cauchy criterion for functions.

## §4. The limit of a function (continued)

### Typed slide 4. Stabilization of sign

**Theorem 2.4.4.** Let $g : D \subset \mathbb{R} \to \mathbb{R}$, let $a$ be a limit point of $D$, and let $\lim\limits_{x\to a} g(x) = B \in \mathbb{R} \setminus \{0\}$. Then there exists a neighbourhood $V(a)$ such that $g(x)$ and $B$ have the same sign on $\dot V(a) \cap D$; in particular, $g(x) \ne 0$ for all $x \in \dot V(a) \cap D$.

The last statement also holds in the case $\lim\limits_{x\to a} g(x) = \infty$ (the slide shows this case with the symbol "1" in the text layer, which stands for $\infty$).

### Handwritten page 5 (PDF p. 5). Proof of Theorem 2.4.4

**Proof (Theorem 2.4.4).** Consider, to be definite, $B > 0$ (circled in red).

Suppose the statement of Theorem 2.4.4 is false. Then for every $n \in \mathbb{N}$ there exists $x_n \in \dot V_{1/n}(a) \cap D$ with $g(x_n) \le 0$.

But $x_n \to a$. Then $g(x_n) \to B$ $\Rightarrow$ by the theorem on passage to the limit in an inequality for sequences, $B \le 0$ (circled), which contradicts the assumption $B > 0$ (red arrow "contradiction").

### Typed slide 6. Arithmetic operations on functions

**Theorem 2.4.5.** Let $f, g : D \subset \mathbb{R} \to \mathbb{R}$, let $a$ be a limit point of $D$, $A, B \in \mathbb{R}$, $f(x) \xrightarrow[x\to a]{} A$, $g(x) \xrightarrow[x\to a]{} B$. Then

1. $f(x) \pm g(x) \to A \pm B$;
2. $f(x) g(x) \to AB$;
3. $|f(x)| \to |A|$;
4. if, in addition, $B \ne 0$, then $\dfrac{f(x)}{g(x)} \to \dfrac{A}{B}$.

### Handwritten pages 7–8 (PDF p. 7–8). Proof of item 1 and a remark

**Proof (Theorem 2.4.5).** We prove item ① for the sum.

Take $\{x_n\}$ with $x_n \in D$, $x_n \ne a$, $x_n \to a$. By the Heine definition, $f(x_n) \to A$ and $g(x_n) \to B$. By the theorem on the limit of a sum for sequences, $f(x_n) + g(x_n) \to A + B$.

Since $\{x_n\}$ was arbitrary, $f(x) + g(x) \to A + B$ as $x \to a$.

**Remark (handwritten).** In proving item ④ (the limit of a quotient) one should take into account that by Theorem 2.4.4 there is $V(a)$ on which $\dfrac{f}{g}$ is defined, at least on $\dot V(a) \cap D$.

**Remark (handwritten, page 8).** Theorem 2.4.5 holds also for infinite limits, except for the indeterminate forms $\infty - \infty$, $0 \cdot \infty$, $\dfrac{0}{0}$ and $\dfrac{\infty}{\infty}$. Circled: $\dfrac{\infty}{0} = \infty$.

### Typed slide 9. Infinitesimal and infinitely large functions

The definition of an infinitesimal and of an infinitely large quantity carries over to functions. Thus a function tending to zero at $a$ is called **infinitesimal** at $a$. The statements that the product of an infinitesimal function and a bounded function is infinitesimal, and the connection between infinitesimal and infinitely large functions, remain valid.

### Typed slide 10. Limit of a composition

**Theorem 2.4.6.** Let $f : D \subset \mathbb{R} \to \mathbb{R}$, $g : E \subset \mathbb{R} \to \mathbb{R}$, $f(D) \subset E$, $a, A, B \in \overline{\mathbb{R}}$, and suppose:

1. $a$ is a limit point of $D$, and $f(x) \xrightarrow[x\to a]{} A$;
2. $A$ is a limit point of $E$, and $g(x) \xrightarrow[x\to A]{} B$;
3. there is a neighbourhood $V(a)$ of $a$ such that $f(x) \ne A$ for every $x \in \dot V(a) \cap D$.

Then $(g \circ f)(x) \xrightarrow[x\to a]{} B$.

### Handwritten page 11 (PDF p. 11). Proof of Theorem 2.4.6

**Proof (Theorem 2.4.6).** Take $\{x_n\}$ with $x_n \in D$, $x_n \ne a$, $x_n \to a$, and denote $f(x_n) = y_n$.

Then $y_n \in E$, $y_n \to A$ (by the Heine definition). Moreover, starting from some index, $x_n \in V(a)$. Then $y_n \ne A$ for such $n$.

Hence $\{y_n\}$ has the properties $y_n \in E$, $y_n \ne A$, $y_n \to A$ $\Rightarrow$ by the Heine definition $g(y_n) \to B$, i.e. $(g \circ f)(x_n) \to B$.

Since $\{x_n\}$ was arbitrary, $(g \circ f)(x) \to B$ as $x \to a$.

> **Editor's note.** In the handwriting, the line with $y_n \to A$ reads "$x_n \mapsto A$"; by meaning this is $y_n \to A$.

### Typed slide 12 with a blue handwritten note. Passage to the limit in an inequality

**Theorem 2.4.7.** Let $f, g : D \subset \mathbb{R} \to \mathbb{R}$, let $a$ be a limit point of $D$, let $f(x) \le g(x)$ for all $x \in D \setminus \{a\}$, let $A, B \in \overline{\mathbb{R}}$, $f(x) \xrightarrow[x\to a]{} A$, $g(x) \xrightarrow[x\to a]{} B$. Then $A \le B$.

Handwritten (in blue): "Proof: take $\{x_n\}$ with $x_n \in D$, $x_n \ne a$, $x_n \to a$ $\Rightarrow$ $f(x_n) \to A$, $g(x_n) \to B$. For all $x \in D \setminus \{a\}$: $f(x) \le g(x)$ $\Rightarrow$ $f(x_n) \le g(x_n)$ $\Rightarrow$ by the theorem on passage to the limit in an inequality, $A \le B$."

### Typed slide 13. The squeeze theorem for functions

**Theorem 2.4.8.** Let $f, g, h : D \subset \mathbb{R} \to \mathbb{R}$, let $a$ be a limit point of $D$, let $f(x) \le g(x) \le h(x)$ for all $x \in D \setminus \{a\}$, let $A \in \mathbb{R}$, $f(x) \xrightarrow[x\to a]{} A$ and $h(x) \xrightarrow[x\to a]{} A$. Then also $g(x) \xrightarrow[x\to a]{} A$.

### Handwritten page 14 (PDF p. 14). Remark on comparison of limits

If $f(x) \le g(x)$ for all $x \in D \setminus \{a\}$ and $f(x) \to +\infty$ as $x \to a$, then also $g(x) \to +\infty$ as $x \to a$.

Similarly: if $f(x) \le g(x)$ for all $x \in D \setminus \{a\}$ and $g(x) \to -\infty$ as $x \to a$, then also $f(x) \to -\infty$ as $x \to a$.

## §4. One-sided limits

### Typed slide 15. Limit along a set

**Definition 2.4.5.** Let $f : D \subset \mathbb{R} \to \mathbb{R}$, $D_1 \subset D$, and let $a$ be a limit point of $D_1$. The limit $\lim\limits_{x\to a} f\big|_{D_1}(x)$ is called the **limit of the function $f$ at the point $a$ along the set $D_1$**.

### Typed slide 16. Left-hand and right-hand limits

**Definition 2.4.6.** Let $f : D \subset \mathbb{R} \to \mathbb{R}$, $a \in \mathbb{R}$.

1. If $a$ is a limit point of the set $D_1 = D \cap (-\infty, a)$, the limit of $f$ at $a$ along $D_1$ is called the **left-hand limit** of $f$ at $a$, denoted $\lim\limits_{x\to a^-} f(x)$.
2. If $a$ is a limit point of the set $D_2 = D \cap (a, +\infty)$, the limit of $f$ at $a$ along $D_2$ is called the **right-hand limit** of $f$ at $a$, denoted $\lim\limits_{x\to a^+} f(x)$.

### Handwritten page 17 (PDF p. 17). The $\varepsilon$–$\delta$ definitions and an example

$\lim\limits_{x\to a^-} f(x) = A$ means: $\forall \varepsilon > 0\ \exists \delta > 0\ \forall x \in D$: $0 < a - x < \delta$ $\Rightarrow$ $|f(x) - A| < \varepsilon$.

$\lim\limits_{x\to a^+} f(x) = A$ means: $\forall \varepsilon > 0\ \exists \delta > 0\ \forall x \in D$: $0 < x - a < \delta$ $\Rightarrow$ $|f(x) - A| < \varepsilon$.

**Example (handwritten).** The graph of $f(x)$ with a jump at $x = 2$: $f(2) = 100$ (filled point), left-hand limit $50$ (open circle on the line from $(0, 0)$). Labels: $\lim\limits_{x\to 2^-} f(x) = 50$; $\lim\limits_{x\to 2^+} f(x) = 100$.

### Typed slide 18 with a blue handwritten note. The limit through one-sided limits

**Remark (typed).** Let $f : D \subset \mathbb{R} \to \mathbb{R}$, $a \in \mathbb{R}$, $D_1 = D \cap (-\infty, a)$, $D_2 = D \cap (a, +\infty)$, and let $a$ be a limit point of both $D_1$ and $D_2$. Then, for the limit of $f$ at $a$ to exist, it is necessary and sufficient that the one-sided limits of $f$ at $a$ exist and are equal to each other.

Handwritten (in blue):

"Proof.
(⇒) $\exists \lim\limits_{x\to a} f(x) = A$ $\Rightarrow$ $\exists \lim\limits_{x\to a^-} f(x) = \lim\limits_{x\to a^+} f(x) = A$.
(⇐) $\exists \lim\limits_{x\to a^-} f = \lim\limits_{x\to a^+} f = A$ $\Rightarrow$ $\forall V(A)$ $\exists \delta_1, \delta_2 > 0$ such that $f(x) \in V(A)$ for all $x \in D$ with $0 < a - x < \delta_1$, and for all $x \in D$ with $0 < x - a < \delta_2$ $\Rightarrow$ with $\delta = \min\{\delta_1, \delta_2\}$: $f(x) \in V(a)$ for all $x \in D$ with $|x - a| < \delta$."

> **Editor's note.** In the last line of the handwriting it is written $V(a)$; by meaning this is $V(A)$.

## §4. Monotone functions

### Typed slide 19. The limit of a monotone function

**Theorem 2.4.9.** Let $f : D \subset \mathbb{R} \to \mathbb{R}$, $a \in (-\infty, +\infty]$, $D_1 = D \cap (-\infty, a)$, and let $a$ be a limit point of $D_1$.

1. If $f$ is increasing and bounded above on $D_1$, then the finite limit $\lim\limits_{x\to a^-} f(x)$ exists.
2. If $f$ is decreasing and bounded below on $D_1$, then the finite limit $\lim\limits_{x\to a^-} f(x)$ exists.

### Handwritten pages 20–21 (PDF p. 20–21). Proof of Theorem 2.4.9

**Proof (Theorem 2.4.9).** We prove ①; ② is proved similarly.

Put $A = \sup\limits_{x \in D_1} f(x)$ $\Rightarrow$ $A \in \mathbb{R}$, since $f$ is bounded above on $D_1$. We show that $f(a^-) = A$.

Take $\varepsilon > 0$. By the definition of the least upper bound, $\exists x_0 \in D_1$: $f(x_0) > A - \varepsilon$.

Recall that $f$ is increasing on $D_1$ $\Rightarrow$ $\forall x \in D_1$, $x > x_0$: $A - \varepsilon < f(x_0) \le f(x) \le A < A + \varepsilon$.

Put $\delta = a - x_0$ when $a \in \mathbb{R}$, or $\Delta = \max\{x_0, 1\}$ when $a = +\infty$. Then for all $x \in D_1$ with $0 < a - x < \delta$ (or for all $x \in D_1$ with $x > \Delta$ when $a = +\infty$) we have $A - \varepsilon < f(x) < A + \varepsilon$, i.e. $|f(x) - A| < \varepsilon$.

**Remark (handwritten, page 21).** An analogous statement holds for the right-hand limit. Let $f : D \subset \mathbb{R} \to \mathbb{R}$, $a \in [-\infty, +\infty)$, $D_2 = D \cap (a, +\infty)$, and let $a$ be a limit point of $D_2$.

1. If $f$ is increasing and bounded below on $D_2$, then the finite limit $\lim\limits_{x\to a^+} f(x)$ exists.
2. If $f$ is decreasing and bounded above on $D_2$, then the finite limit $\lim\limits_{x\to a^+} f(x)$ exists.
3. If $f$ is increasing and not bounded above on $D_1$, then $\lim\limits_{x\to a^-} f(x) = +\infty$.
4. If $f$ is decreasing and not bounded below on $D_1$, then $\lim\limits_{x\to a^-} f(x) = -\infty$.

For $D_2$, statements analogous to items 3 and 4 hold.

## §4. The Bolzano–Cauchy criterion for functions

### Typed slide 22. The Bolzano–Cauchy criterion

**Theorem 2.4.10.** Let $f : D \subset \mathbb{R} \to \mathbb{R}$, and let $a$ be a limit point of $D$. Then the existence of a finite limit of $f$ at $a$ is equivalent to the following statement:

$$
\forall \varepsilon > 0\ \exists V(a)\ \forall x, \hat{x} \in \dot V(a) \cap D: \quad |f(x) - f(\hat{x})| < \varepsilon.
$$

### Handwritten pages 23–24 (PDF p. 23–24). Proof of Theorem 2.4.10

**Proof (Theorem 2.4.10).**

**①** Let $\lim\limits_{x\to a} f(x) = A \in \mathbb{R}$. Take $\varepsilon > 0$. By the definition of the limit, $\exists V(a)$: $|f(x) - A| < \frac{\varepsilon}{2}$ for all $x \in \dot V(a) \cap D$.

Then for $x, \hat x \in \dot V(a) \cap D$:

$$
|f(x) - f(\hat x)| = |f(x) - A + A - f(\hat x)| \le |f(x) - A| + |A - f(\hat x)| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
$$

Since $\varepsilon$ was arbitrary, we get: for all $x, \hat x \in \dot V(a) \cap D$, $|f(x) - f(\hat x)| < \varepsilon$.

**②** Suppose condition $(*)$ holds: $\forall \varepsilon > 0\ \exists V(a)$: $\forall x, \hat x \in \dot V(a) \cap D$: $|f(x) - f(\hat x)| < \varepsilon$.

Take $\{x_n\}$ with $x_n \in D$, $x_n \ne a$, $x_n \to a$.

$x_n \to a$ $\Rightarrow$ by the definition of the limit of a sequence, $\exists N$: $\forall n > N$, $x_n \in \dot V(a) \cap D$.

By $(*)$: $\forall n, l > N$: $|f(x_n) - f(x_l)| < \varepsilon$ $\Rightarrow$ $\{f(x_n)\}$ is a Cauchy sequence $\Rightarrow$ $\{f(x_n)\}$ has a finite limit.

(The handwriting does not record the proof of uniqueness of the limit for different sequences.)

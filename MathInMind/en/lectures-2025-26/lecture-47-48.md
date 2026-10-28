---
title: "Lectures 47–48 — Integral inequalities and improper integrals"
lang: en
course: "Mathematical Analysis, 2025/26"
lecture: 47-48
semester: 2
date: 2026-04-02
source: "ma25_26-lectures_47-48_notes.pdf"
pdf_pages: 41
typed_slides: 25
archive_file: "Лекция 47-48 1.md"
---
# Lectures 47–48 — Integral inequalities and improper integrals

[← Lectures 45–46](lecture-45-46.md) · [Lecture index](index.md) · [Lectures 49–50 →](lecture-49-50.md) · [Terms & theorems](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-47-48.md) · [Español](../../es/lectures-2025-26/lecture-47-48.md)

> **Source:** `ma25_26-lectures_47-48_notes.pdf` — 41 PDF pages, 25 printed slides; the printed date is 2 April 2026. Printed pages: 1–4, 7–13, 15, 17–18, 20–23, 25–26, 29, 31–32, 34, 36. Handwritten pages: 5–6, 14, 16, 19, 24, 27–28, 30, 33, 35, 37–41. Every PDF page is attributed exactly once; slide and PDF-page numbers are distinct.
>
> **Semester-2 duplication.** Semester 1 ends with lecture 32; semester 2 spans lectures 33–64. The complete material overlaps [§4.4, “Taylor, Wallis, and integral inequalities”](../../ru/lectures/05-taylor-wallis-inequalities-4-4.md) and [§4.5, “Improper integrals”](../../ru/lectures/06-improper-integrals-4-5.md), and also appears in the [semester-2 register](../../ru/lectures/index.md). The preserved archive original is [“Лекция 47-48 1.md”](../../../source/MathInMind/МАТАН_Л/Лекция%2047-48%201.md). This full illustrated transcription is not replaced by pointers to the thematic notes.
>
> **Important qualifications.** An [improper integral](#def-4-5-2) here means an ordinary [one-sided limit](lecture-15.md#def-2-4-5), not a [Cauchy principal value](../09-improper-integrals-applications.md#sec-9-1). At multiple singularities, each one-sided part must be checked independently. Convergence means a finite limit. Do not apply [Newton–Leibniz](lecture-43-44.md#thm-4-3-2) across a singularity without verifying its hypotheses.

## Printed slide 1 (PDF p. 1). Title

“Mathematical Analysis,” lectures 47–48, 2 April 2026; D. E. Apushkinskaya, RUDN University.

## Printed slide 2 (PDF p. 2). Quote of the day

The slide contrasts the [differential](lecture-24-25-26.md#def-3-3-1) symbol $`\partial z/\partial x`$ with the integral $`\int f(x)\,dx`$.

**BRO.** “This cutie is the differential. It is very useful, and calculating it is a pleasure. You can differentiate any function effortlessly—its formulas are easy to remember and will come to your rescue again and again. Definitely, the differential is your BRO!”

**NOT BRO.** “This is concentrated evil, straight from the deepest pits of hell, and it will troll you all your life. The calculations take precious years of your life and kilometres of paper. One of its signs resembles a torture device, which is exactly what it is. Run away in terror—it is not your bro!”

## Printed slide 3 (PDF p. 3). Lecture goals

Integral inequalities; improper integrals; substitution and [integration by parts](lecture-37-38.md#thm-4-1-4) for improper integrals; convergence tests for improper integrals.

## Chapter 4, §4. Integral inequalities

### Printed slide 4 (PDF p. 4). Hölder's inequality

Conjugate exponents $`p,q\in(1,+\infty)`$ satisfy $`1/p+1/q=1`$.

<a id="thm-4-4-5"></a>**Theorem 4.4.5.** Let $`f,g\in C[a,b]`$ and let $`p,q`$ be conjugate exponents. Then

```math
\left|\int_a^b fg\right|
\le\left(\int_a^b|f|^p\right)^{1/p}
\left(\int_a^b|g|^q\right)^{1/q}.
```

A handwritten note on the slide identifies the case $`p=q=2`$ as the [Cauchy–Bunyakovsky](#thm-4-4-6) inequality.

### Handwritten page (PDF p. 5). Hölder for sums and preparation of Riemann sums

The proof uses [Hölder's inequality](#thm-4-4-5) for finite sums:

```math
\left|\sum_{k=0}^{n-1}a_kb_k\right|
\le\left(\sum_{k=0}^{n-1}|a_k|^p\right)^{1/p}
\left(\sum_{k=0}^{n-1}|b_k|^q\right)^{1/q}.
```

Take the uniform [partition](lecture-37-38.md#def-4-2-2) $`x_k=a+k(b-a)/n`$, $`\Delta x_k=(b-a)/n`$, and set $`a_k=f(x_k)(\Delta x_k)^{1/p}`$, $`b_k=g(x_k)(\Delta x_k)^{1/q}`$. Then $`a_kb_k=f(x_k)g(x_k)\Delta x_k`$; the powers on the right give $`|f(x_k)|^p\Delta x_k`$ and $`|g(x_k)|^q\Delta x_k`$.

### Handwritten page (PDF p. 6). Limit of the sums in Hölder's proof

For these $`a_k,b_k`$, the finite-sum inequality becomes

```math
\left|\sum f(x_k)g(x_k)\Delta x_k\right|
\le\left(\sum |f(x_k)|^p\Delta x_k\right)^{1/p}
\left(\sum |g(x_k)|^q\Delta x_k\right)^{1/q}.
```

As $`n\to\infty`$, all three sums tend to their corresponding [Riemann integrals](lecture-39-40.md#def-4-2-6). Continuity of the integrands justifies passage to the limit and proves [Theorem 4.4.5](#thm-4-4-5).

### Printed slide 5 (PDF p. 7). Cauchy–Bunyakovsky inequality

<a id="cor-4-4-1"></a>**Corollary 4.4.1.** If $`f,g\in C[a,b]`$, then

```math
\left|\int_a^bfg\right|
\le\sqrt{\int_a^b f^2}\sqrt{\int_a^b g^2}.
```

### Printed slide 6 (PDF p. 8). Minkowski's inequality

<a id="thm-4-4-6"></a>**Theorem 4.4.6.** Let $`f,g\in C[a,b]`$, $`p\ge1`$. Then

```math
\left(\int_a^b|f+g|^p\right)^{1/p}
\le\left(\int_a^b|f|^p\right)^{1/p}
+\left(\int_a^b|g|^p\right)^{1/p}.
```

The slide also gives the case $`p=2`$ by hand:

```math
\sqrt{\int_a^b|f+g|^2}\le\sqrt{\int_a^b f^2}+\sqrt{\int_a^b g^2}.
```

## Chapter 4, §5. Improper integrals

### Printed slide 7 (PDF p. 9). Section heading

“§5. Improper integrals.”

### Printed slide 8 (PDF p. 10). Local Riemann integrability

For $`f\in C([a,b])`$, the Riemann integral is defined. What changes for $`f\in C([a,b))`$ or when $`b=+\infty`$?

<a id="def-4-5-1"></a>**Definition 4.5.1.** A function $`f`$ is locally Riemann integrable on an interval $`\langle a,b\rangle`$ if it is Riemann integrable on every closed segment contained in that interval. The class is denoted by $`\mathcal R_{loc}(\langle a,b\rangle)`$. Clearly, $`C(\langle a,b\rangle)\subset\mathcal R_{loc}(\langle a,b\rangle)`$.

### Printed slide 9 (PDF p. 11). Improper integral at the right endpoint

<a id="def-4-5-2"></a>**Definition 4.5.2.** Let $`-\infty<a<b\le+\infty`$ and $`f\in\mathcal R_{loc}([a,b))`$. Define

```math
\int_a^{\to b}f(x)\,dx:=\lim_{B\to b-}\int_a^Bf(x)\,dx.
```

This limit defines the improper integral. If it exists in $`\mathbb R`$ and equals $`I`$, the integral converges and is assigned the value $`I`$. If the limit is infinite or does not exist, no finite value is assigned and the integral diverges.

### Printed slide 10 (PDF p. 12). A singularity at the left endpoint

Symmetrically, for $`-\infty\le a<b<+\infty`$ and $`f\in\mathcal R_{loc}((a,b])`$:

```math
\int_{\to a}^{b}f(x)\,dx:=\lim_{A\to a+}\int_A^bf(x)\,dx.
```

The integral converges when the limit is finite. An integral with an infinite value or no limit is called divergent.

### Printed slide 11 (PDF p. 13). Power-integral examples

1. $`\displaystyle\int_{\to0}^{1}\frac{dx}{x}=\lim_{t\to0+}\int_t^1\frac{dx}{x}=\lim_{t\to0+}[\ln x]_t^1=+\infty`$.
2. $`\displaystyle\int_{\to0}^{1}x^{-p}\,dx`$ converges for $`p<1`$ and diverges for $`p\ge1`$.
3. $`\displaystyle\int_1^{\to+\infty}x^{-p}\,dx`$ converges for $`p>1`$ and diverges for $`p\le1`$.

### Handwritten page (PDF p. 14). Evaluation of a power integral

The board evaluates $`\int_2^B x^{-p}\,dx`$ for $`p\ne1`$:

```math
\int_2^B x^{-p}\,dx
=\left.\frac{x^{1-p}}{1-p}\right|_2^B
=\frac1{1-p}\left(B^{1-p}-2^{1-p}\right).
```

For $`p=1`$, the [antiderivative](lecture-36.md#def-4-1-1) is $`\ln x`$. The limit as $`B\to+\infty`$ is finite exactly when $`p>1`$; at $`p=1`$ the logarithm grows without bound, and for $`p<1`$ the term $`B^{1-p}`$ is also unbounded. The analogous formula at zero gives the threshold $`p<1`$; equality $`p=1`$ diverges logarithmically.

### Printed slide 12 (PDF p. 15). Proper integrals as a special case

<a id="lem-4-5-1"></a>**Lemma 4.5.1.** If $`f\in C([a,b])`$, then

```math
\int_a^{\to b}f(x)\,dx=\int_a^bf(x)\,dx.
```

### Handwritten page (PDF p. 16). Proof of Lemma 4.5.1

Since $`f`$ is continuous, it has an antiderivative $`F`$, and $`\int_a^bf=F(b)-F(a)`$. On the other hand,

```math
\int_a^{\to b}f=\lim_{t\to b-}(F(t)-F(a))=F(b)-F(a),
```

by continuity of $`F`$ at $`b`$.

### Printed slide 13 (PDF p. 17). When an integral is improper

There are two cases: (a) $`b=+\infty`$; (b) $`b<+\infty`$, but $`f\notin\mathcal R([a,b])`$. Case (b) occurs exactly when $`f`$ is unbounded in every left-hand neighbourhood of $`b`$.

### Printed slide 14 (PDF p. 18). Additivity over an interval

<a id="lem-4-5-2"></a>**Lemma 4.5.2.** Let $`f\in C([a,b))`$ and $`a<c<b`$. Then

```math
\int_a^{\to b}f(x)\,dx=\int_a^cf(x)\,dx+\int_c^{\to b}f(x)\,dx.\tag{4.5.1}
```

Convergence of the integral from $`a`$ to $`b`$ is equivalent to convergence of the tail from $`c`$ to $`b`$.

### Handwritten page (PDF p. 19). Proof of Lemma 4.5.2

For every $`B\in(c,b)`$, additivity of the proper integral gives

```math
\int_a^Bf=\int_a^cf+\int_c^Bf.\tag{4.5.2}
```

As $`B\to b-`$ the first term remains fixed, so the left-hand side has a finite limit if and only if the last term does. Passing to the limit in (4.5.2) gives (4.5.1).

### Printed slide 15 (PDF p. 20). Remainder of a convergent improper integral

<a id="def-4-5-3"></a>**Definition 4.5.3.** The integral $`\int_A^{\to b}f(x)\,dx`$ is called the remainder of $`\int_a^{\to b}f(x)\,dx`$.

<a id="lem-4-5-3"></a>**Lemma 4.5.3.** If $`\int_a^{\to b}f`$ converges, then

```math
\int_A^{\to b}f(x)\,dx\longrightarrow0\quad(A\to b-).
```

In other words, the remainder of a convergent integral tends to zero.

![PDF p. 20: original diagram of the improper-integral tail from a to b](../../assets/lectures-2025-26/lec47-48-p20-improper-tail.jpg)

### Printed slide 16 (PDF p. 21). Linearity of the improper integral

<a id="lem-4-5-4"></a>**Lemma 4.5.4.** Let $`f,g\in C([a,b))`$ and $`\alpha,\beta\in\mathbb R`$. The slide states

```math
\int_a^{\to b}(\alpha f+\beta g)
=\alpha\int_a^{\to b}f+\beta\int_a^{\to b}g.
```

It also says that the three integrals converge and diverge simultaneously, and that when they converge the values satisfy this linear identity.

#### Handwritten annotation on the same printed slide. Qualification of linearity

The handwritten note says to pass to the limit as $`B\to b-`$ in the identity for proper integrals on $`[a,B]`$. This yields linearity when both original improper integrals have limits. The adjacent printed claim of “simultaneous” convergence without qualification is false for arbitrary $`\alpha,\beta`$: coefficients may be zero, and divergent terms may cancel. The correct statement is: if $`\int_a^{\to b}f`$ and $`\int_a^{\to b}g`$ converge, the integral of their linear combination converges to the corresponding linear combination of values; if one diverges and the other converges, their sum diverges. The integrands $`f`$ and $`g`$ are tracked separately in this statement. Two divergent terms can cancel.

### Printed slide 17 (PDF p. 22). Sum of a divergent and a convergent integral

If $`\int_a^{\to b}f`$ diverges and $`\int_a^{\to b}g`$ converges, then $`\int_a^{\to b}(f+g)`$ diverges. The slide argues that convergence of the sum would, by linearity, imply convergence of $`f=(f+g)-g`$, a contradiction.

### Printed slide 18 (PDF p. 23). Change of variable

<a id="thm-4-5-1"></a>**Theorem 4.5.1.** Let $`f\in C([a,b))`$, $`\varphi\in C^1([\alpha,\beta))`$, let $`\varphi`$ be monotone, $`\varphi(\alpha)=a`$, and $`\lim_{x\to\beta-0}\varphi(x)=b`$. Then

```math
\int_\alpha^{\to\beta}f(\varphi(x))\varphi'(x)\,dx
=\int_a^{\to b}f(t)\,dt.\tag{4.5.3}
```

The theorem is understood to mean that existence of either integral implies existence of the other and the equality holds.

### Handwritten page (PDF p. 24). Proof of substitution

For a finite $`y<\beta`$, apply the proper change-of-variable formula:

```math
\int_\alpha^y f(\varphi(x))\varphi'(x)\,dx
=\int_{\varphi(\alpha)}^{\varphi(y)}f(t)\,dt.
```

As $`y\to\beta-`$, $`\varphi(y)\to b`$. Passing to the limit on both sides proves (4.5.3) whenever the finite limit exists. Monotonicity ensures the endpoint approaches $`b`$ without overshooting.

### Printed slide 19 (PDF p. 25). A substitution that turns an improper integral into a proper one

Sometimes substitution turns an improper integral into a proper integral. Example:

```math
\int_0^{+\infty}\frac{\arctan x}{1+x^2}\,dx
=\int_0^{\pi/2}t\,dt,
\qquad t=\arctan x,\quad dt=\frac{dx}{1+x^2}.
```

At $`x=0`$, $`t=0`$, while $`x\to+\infty`$ implies $`t\to\pi/2`$. Thus the value is $`\pi^2/8`$.

### Printed slide 20 (PDF p. 26). Integration by parts

<a id="thm-4-5-2"></a>**Theorem 4.5.2.** Let $`u,v\in C^1([a,b))`$ and suppose $`\lim_{x\to b-0}u(x)v(x)`$ exists. Then

```math
\int_a^{\to b}u(x)v'(x)\,dx
=\left.uv\right|_a^{\to b}-\int_a^{\to b}v(x)u'(x)\,dx,\tag{4.5.4}
```

where $`\left.uv\right|_a^{\to b}=\lim_{x\to b-0}u(x)v(x)-u(a)v(a)`$. If the right-hand side of (4.5.4) converges, then the left-hand side converges as well.

### Handwritten page (PDF p. 27). Proof of integration by parts

For each $`B<b`$, the proper formula gives

```math
\int_a^B u(x)v'(x)\,dx=[u(x)v(x)]_a^B-\int_a^Bv(x)u'(x)\,dx.
```

Let $`B\to b-`$, using the assumed limit of $`uv`$ and convergence of the right-hand side, to obtain (4.5.4). Convergence of the right-hand side is a hypothesis from which convergence of the left is deduced; it does not follow just from existence of the endpoint limit of $`uv`$.

### Handwritten page (PDF p. 28). A substitution removing a right-endpoint singularity

For $`a<b`$, consider $`\int_a^b f(x)\,dx`$ with a singularity at $`x=b`$. Set

```math
x=b-\frac1t,\qquad dx=\frac{dt}{t^2}.
```

Then $`x=a`$ corresponds to $`t=1/(b-a)`$, while $`x\to b-`$ gives $`t\to+\infty`$. The substitution therefore transforms the integral into

```math
\int_{1/(b-a)}^{+\infty} f\!\left(b-\frac1t\right)\frac{dt}{t^2}.
```

### Printed slide 21 (PDF p. 29). Nonnegative integrands

<a id="lem-4-5-5"></a>**Lemma 4.5.5.** Let $`f\in\mathcal R_{loc}[a,b)`$, $`f\ge0`$. Then convergence of $`\int_a^{\to b}f`$ is equivalent to boundedness above on $`[a,b)`$ of

```math
F(A)=\int_a^A f
```

### Handwritten page (PDF p. 30). Proof of Lemma 4.5.5

Since $`f\ge0`$, the function $`F(A)=\int_a^A f`$ is nondecreasing: for $`a\le A<B<b`$,

```math
F(B)-F(A)=\int_A^B f\ge0.
```

Convergence of $`\int_a^{\to b}f`$ is equivalent to existence of the finite limit of $`F(A)`$ as $`A\to b-`$. If this limit is finite, $`F`$ is [bounded above](lecture-05-06.md#def-1-3-7). Conversely, if the increasing function $`F`$ is bounded above, the [monotone convergence theorem](lecture-11-12.md#thm-2-3-3) for functions gives a finite limit as $`A\to b-`$; this is the value of the improper integral.

### Printed slide 22 (PDF p. 31). Remarks on the criterion

1. For $`f\ge0`$, the integral either converges or diverges to $`+\infty`$, and

```math
\int_a^{\to b}f=\sup_{A\in[a,b)}\int_a^A f.
```

2. To bound the increasing function $`F`$ above, it suffices to bound a sequence $`F(A_n)`$ where $`A_n\in[a,b)`$ increases to $`b`$. Indeed,

```math
\sup_nF(A_n)=\lim_{n\to\infty}F(A_n)=\lim_{A\to b-}F(A)=\sup_{A\in[a,b)}F(A).
```

### Printed slide 23 (PDF p. 32). Comparison test

<a id="thm-4-5-3"></a>**Theorem 4.5.3.** Let $`f,g\in\mathcal R_{loc}[a,b)`$, $`f,g\ge0`$, and $`f(x)=O(g(x))`$ as $`x\to b-`$. Then:

1. If $`\int_a^{\to b}g`$ converges, $`\int_a^{\to b}f`$ converges.
2. If $`\int_a^{\to b}f`$ diverges, $`\int_a^{\to b}g`$ diverges.

### Handwritten page (PDF p. 33). Proof of comparison

From $`f=O(g)`$ at the right endpoint, there are $`\Delta<b`$ and $`K>0`$ such that $`f(x)\le Kg(x)`$ for $`x\in[\Delta,b)`$. If $`\int_a^{\to b}g`$ converges, its tail is finite; for $`B\ge\Delta`$,

```math
\int_a^Bf=\int_a^\Delta f+\int_\Delta^Bf
\le\int_a^\Delta f+K\int_\Delta^Bg.
```

The partial integrals $`\int_a^Bf`$ are bounded above. [Lemma 4.5.5](#lem-4-5-5) implies convergence of the integral of $`f`$. The second statement is the contrapositive of the first.

### Printed slide 24 (PDF p. 34). Limit comparison test

<a id="cor-4-5-1"></a>**Corollary 4.5.1.** Let $`f,g\in\mathcal R_{loc}[a,b)`$, $`f,g>0`$, and suppose

```math
\lim_{x\to b-}\frac{f(x)}{g(x)}=\ell\in[0,+\infty].
```

1. If $`\ell<+\infty`$ and $`\int g`$ converges, then $`\int f`$ converges.
2. If $`\ell>0`$ and $`\int f`$ converges, then $`\int g`$ converges.
3. If $`0<\ell<+\infty`$, the two integrals converge or diverge together.

### Handwritten page (PDF p. 35). Proof of limit comparison

1. If $`\ell=0`$ or is finite and positive, $`f/g`$ is bounded above in a left neighbourhood of $`b`$, so $`f=O(g)`$ and [Theorem 4.5.3](#thm-4-5-3) applies.
2. If $`\ell>0`$, $`g/f`$ is bounded above near the endpoint; apply comparison to $`g`$ and $`f`$.
3. For $`0<\ell<+\infty`$, both ratios are bounded above near the endpoint, giving equivalence of convergence behaviour.

### Printed slide 25 (PDF p. 36). Remarks on convergence

1. Integrals of nonnegative functions equivalent at a singular point converge or diverge together.
2. Convergence of $`\int_a^{+\infty}f`$ does not imply $`f(x)\to0`$ as $`x\to+\infty`$, even when $`f\ge0`$ and continuous.
3. Bounded partial integrals are necessary but not sufficient. For example,

```math
\int_0^{+\infty}\cos x\,dx
```

diverges because $`\int_0^A\cos x\,dx=\sin A`$ has no limit as $`A\to+\infty`$.

### Handwritten pages (PDF pp. 37–41). Examples and qualification of the remarks

**PDF pp. 37–38.** Consider

```math
\int_2^{+\infty}\frac{dx}{x^\alpha(\ln x)^\beta},\qquad \alpha,\beta\in\mathbb R.
```

Use $`\ln x=o(x^q)`$ for every $`q>0`$. If $`\alpha>1`$, the logarithmic factor does not change convergence: for a suitable $`q>0`$, the integrand is bounded above on a tail by a power $`x^{-1-q/2}`$, so the integral converges. If $`\alpha<1`$, comparison from below with a divergent power gives divergence. If $`\alpha=1`$, substituting $`t=\ln x`$ reduces the question to $`\int_{\ln2}^{+\infty}t^{-\beta}\,dt`$, which converges exactly when $`\beta>1`$.

**PDF pp. 39–40.** The calculation of $`\int_2^B x^{-p}\,dx`$ again gives the threshold $`p>1`$ at infinity. An example follows of a continuous nonnegative function on $`[0,+\infty)`$ with narrow triangular spikes near positive integers, of height $`k`$. Their areas are of order $`1/k^2`$, so $`\sum 1/k^2`$ converges, although the values at the peaks do not tend to zero. The original sketch is reproduced below.

The board defines the union of intervals

```math
E=\bigcup_{k=1}^{\infty}\left(k-\frac{1}{k^2(k+1)},k+\frac{1}{k^2(k+1)}\right).
```

At each peak, $`f(k)=k`$; outside $`E`$ the function is zero, and on each side of each interval the graph is linear, producing triangular spikes.

![PDF p. 40: handwritten graph of narrow increasing spikes, showing integrability need not imply f(x)→0](../../assets/lectures-2025-26/lec47-48-p40-spike-graph.jpg)

**PDF p. 41.** Each triangular spike of height $`k`$ has half-width $`1/(k^2(k+1))`$, so its area is

```math
\frac12\cdot\frac{2}{k^2(k+1)}\cdot k=\frac1{k(k+1)}.
```

For $`N\in\mathbb N`$ the areas telescope:

```math
\int_0^{N+1/2}f=\sum_{k=1}^{N}\frac1{k(k+1)}
=\sum_{k=1}^{N}\left(\frac1k-\frac1{k+1}\right)
=1-\frac1{N+1}\longrightarrow1.
```

Thus the improper integral equals $`1`$ although $`f(k)=k`$ is unbounded as $`x\to+\infty`$. A red handwritten note stresses: “But $`f`$ is not bounded in any neighbourhood of $`+\infty`$!” This does not contradict printed slide 25, which assumes continuity but does not assert boundedness.

---

**Navigation:** [Lectures 45–46](lecture-45-46.md) · [Lectures 49–50](lecture-49-50.md) · [Index](index.md).

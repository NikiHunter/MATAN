---
title: "Lectures 63–64: Continuous differentiability and higher derivatives"
lang: en
course: "Mathematical Analysis 2025/26"
lecture: 63-64
semester: 2
date: 2026-05-28
source: "ma25_26-lectures_63-64_notes.pdf.txt"
pdf_pages: 42
typed_slides: 21
---
# Lectures 63–64 — Continuous differentiability and higher derivatives

> **Source and numbering.** Transcribed solely from the attached PDF `ma25_26-lectures_63-64_notes.pdf.txt`; the source archive was not consulted. Sections follow physical PDF pages 1–42 in order. “Printed slide” numbers are the footer sequence 1–21 and remain distinct from PDF pages; handwritten pages are not assigned slide numbers. Typed slides were checked against both text layer and image; handwritten proofs, examples and annotations were read from the rendered pages. See the [page inventory, source hash and crop provenance](../../assets/lectures-2025-26/provenance-61-64.md) and [machine-readable manifest](../../assets/lectures-2025-26/figures-61-64.json).
>
> **Semester 2 duplication.** These notes overlap the Russian thematic register for §§6.3–6.4 and intentionally preserve the sequential PDF transcript separately. Semester 2 spans lectures **33–64**. Cross-references: [register index](../../ru/lectures/index.md), [§6.3](../../ru/lectures/16-continuous-differentiability-6-3.md), and [§6.4](../../ru/lectures/17-higher-derivatives-6-4.md).

## Printed slide 1 (PDF p. 1). Title

Mathematical Analysis, lectures 63–64; 28 May 2026.

## Printed slide 2 (PDF p. 2). Quote of the day

“The one who laughs best at the exam is the one who is giving it.”

## Printed slide 3 (PDF p. 3). Lecture goals

The lecture continues the study of continuous differentiability and proves a formula expressing a multivariable increment through partial derivatives. It defines higher-order partial derivatives and differentials for maps of several variables and establishes the connection between them.

## Printed slide 4 (PDF p. 4). Coordinate-increment lemma — Lemma 6.3.1

Let $E\subset\mathbb R^n$, $a\in E$, $\delta>0$, $V_\delta(a)\subset E$, and $h\in V_\delta(0)$. Suppose all first partial derivatives of the scalar function $f:E\to\mathbb R$ are defined on $V_\delta(a)$. Then there exist $c_1,\ldots,c_n\in V_\delta(a)$ such that

$$
f(a+h)-f(a)=\sum_{k=1}^{n}\frac{\partial f}{\partial x_k}(c_k)h_k.
$$

## Handwritten page (PDF p. 5). Proof by coordinate increments

Starting from $x^1=a$, change its coordinates one at a time, defining successive points $x^2,x^3,\ldots,x^{n+1}=a+h$. On the $k$th segment consider

$$
F_k(t)=f(x^k+t h_k e^k),\qquad t\in[0,1].
$$

The one-variable mean value theorem gives some $\theta_k\in(0,1)$ and $c_k=x^k+\theta_kh_ke^k$ for which the increment on that segment is $\frac{\partial f}{\partial x_k}(c_k)h_k$. Summing these coordinate increments telescopes to the formula in Lemma 6.3.1. Since $\|h\|<\delta$, each point used stays in $V_\delta(a)$.

![Handwritten coordinate-increment proof](../../assets/lectures-2025-26/lec63-64-p05-coordinate-increment-proof.jpg)

## Handwritten page (PDF p. 6). Continuity consequence of the increment lemma

For a scalar function, continuity of each first partial derivative at $a$ makes these derivatives bounded on a sufficiently small neighborhood of $a$. Applying Lemma 6.3.1 to nearby points gives a bound for each increment by a constant times the sum of the coordinate changes, which tends to zero with the increment. Thus $f$ is continuous throughout a smaller neighborhood of $a$. For a map $f:E\to\mathbb R^m$, apply the scalar argument to each coordinate function.

## Printed slide 5 (PDF p. 7). Continuous differentiability implies differentiability — Theorem 6.3.1

Let $E\subset\mathbb R^n$, let $a$ be an interior point, and suppose $f:E\to\mathbb R^m$ is continuously differentiable at $a$. Then:

1. $f$ is continuous in some neighborhood $V(a)$ of $a$;
2. $f$ is differentiable at $a$.

## Handwritten page (PDF p. 8). Proof of local continuity

It is enough to prove the scalar case; apply it to each coordinate of a vector-valued map. The partial derivatives are bounded by some $M$ in a neighborhood $V(a)$. For $x\in V(a)$ choose a sufficiently small ball $V_{\|h\|}(x)\subset V(a)$; the coordinate-increment lemma and the one-variable mean value theorem give

$$
f(x+h)-f(x)=\sum_{k=1}^{n}\frac{\partial f}{\partial x_k}(c_k)h_k,
$$

with each $c_k$ in that neighborhood. Hence $|f(x+h)-f(x)|\le M\sum_{k=1}^{n}|h_k|\to0$ as $h\to0$. The handwritten blue-and-yellow sketch shows the small ball around a point inside the larger neighborhood $V(a)$.

![Handwritten local-continuity proof and neighborhood diagram](../../assets/lectures-2025-26/lec63-64-p08-local-continuity-proof.jpg)

## Handwritten page (PDF p. 9). Differentiability proof: remainder setup

Apply the coordinate-increment lemma at $a$ and write $c_k=c_k(h)$. Subtract the proposed linear part from the increment:

$$
R(h)=f(a+h)-f(a)-\sum_{k=1}^{n}\frac{\partial f}{\partial x_k}(a)h_k
=\sum_{k=1}^{n}\left[\frac{\partial f}{\partial x_k}(c_k)-\frac{\partial f}{\partial x_k}(a)\right]h_k.
$$

As $h\to0$, each $c_k(h)\to a$. Continuity of the partial derivatives at $a$ makes $R(h)=o(\|h\|)$.

## Handwritten page (PDF p. 10). Remainder estimate and corollary

Given $\varepsilon>0$, choose $h$ small enough that every bracketed difference in the preceding expression has absolute value at most $\varepsilon/\sqrt n$. Cauchy–Schwarz then yields

$$
|R(h)|\le\sqrt{\sum_{k=1}^{n}\left(\frac{\varepsilon}{\sqrt n}\right)^2}\,\sqrt{\sum_{k=1}^{n}h_k^2}=\varepsilon\|h\|.
$$

Thus $R(h)=o(\|h\|)$ and $f$ is differentiable at $a$. In particular, if $E$ is open and $f\in C^1(E,\mathbb R^m)$, then $f$ is differentiable on $E$.

![Handwritten differentiability remainder estimate](../../assets/lectures-2025-26/lec63-64-p10-differentiability-remainder.jpg)

## Printed slide 6 (PDF p. 11). Higher-order partial derivatives — Definition 6.4.1

Let $E\subset\mathbb R^n$, let $a$ be an interior point, let $f:E\to\mathbb R^m$, $s\in\mathbb N$, $\ell\in\{1,\ldots,s\}$, and $i_\ell\in\{1,\ldots,n\}$. The value

$$
\frac{\partial^s f}{\partial x_{i_1}\cdots\partial x_{i_s}}(a)
$$

is a partial derivative of order $s$ with respect to the listed variables. If all indices coincide, it is a pure partial derivative; otherwise it is mixed. The blue handwritten annotations give $\frac{\partial^3 f}{\partial x_2^3}$ as pure and $\frac{\partial^2 f}{\partial x_1\partial x_2}$ as mixed.

![Printed definition with handwritten pure/mixed examples](../../assets/lectures-2025-26/lec63-64-p11-pure-mixed-annotation.jpg)

## Printed slide 7 (PDF p. 12). Repeated differentiability — Definition 6.4.2

The slide states the definition for $E\subset\mathbb R^n$, an interior point $a$, $f:E\to\mathbb R^n$, and $s\in\mathbb N$. The displayed codomain is transcribed as printed; Definition 6.4.1 and Lemma 6.4.1 on the following slides use the general codomain $\mathbb R^m$, so this is an apparent source notation mismatch.

The map $f$ is $s$-times differentiable at $a$ if:

1. all partial derivatives of orders $0,\ldots,s-2$ are differentiable in some neighborhood of $a$;
2. all partial derivatives of order $s-1$ are differentiable at $a$.

If $E$ is open and $f$ is $s$-times differentiable at every point of $E$, it is $s$-times differentiable on $E$. A map differentiable on $E$ any number of times is infinitely differentiable there.

## Handwritten page (PDF p. 13). Example for $s=4$ and the case $s=1$

For $f:\mathbb R^2\to\mathbb R$, the handwritten example unpacks four-times differentiability at $a$: $f$, its first partial derivatives, and its four ordered second partial derivatives must be differentiable in a neighborhood of $a$; all eight ordered third partial derivatives must be differentiable at $a$. The note adds that for $s=1$ the first condition is vacuous and the second is exactly ordinary differentiability at the point.

## Printed slide 8 (PDF p. 14). Lower-order derivatives — Lemma 6.4.1

Let $E\subset\mathbb R^n$, let $a$ be an interior point, $s\in\mathbb Z_+$, $f:E\to\mathbb R^m$, and suppose all partial derivatives of $f$ of order $s$ are differentiable on a neighborhood $V(a)$. Then for every $k\in\{0,\ldots,s\}$ all partial derivatives of $f$ of order $k$ are also differentiable on $V(a)$.

## Handwritten page (PDF p. 15). Proof of Lemma 6.4.1

Proceed by downward induction on $k$. The case $k=s$ is the hypothesis. Suppose $0\le k<s$ and the derivatives of order $k+1$ are differentiable on $V(a)$. Then each derivative of order $k$ has all first partial derivatives on $V(a)$ and is differentiable there. This yields the assertion for every lower order down to $0$.

![Handwritten proof of the lower-order derivative lemma](../../assets/lectures-2025-26/lec63-64-p15-order-derivative-lemma.jpg)

## Printed slide 9 (PDF p. 16). Continuous differentiability of order $s$

For open $E\subset\mathbb R^n$, $F\subset\mathbb R^m$ and $s\in\mathbb Z_+$, $C^s(E,F)$ denotes the class of maps from $E$ to $F$ with continuous partial derivatives through order $s$. Define

$$
C^\infty(E,F)=\bigcap_{s=0}^{\infty}C^s(E,F).
$$

For $k,s\in\mathbb N$ with $k<s$, the slide states the equivalence:

1. $f\in C^s(E,\mathbb R^m)$;
2. every partial derivative of $f$ of order $k$ belongs to $C^{s-k}(E,\mathbb R^m)$.

## Handwritten page (PDF p. 17). Notes on the classes $C^s$

For example, if $E\subset\mathbb R^2$ and $f\in C^3(E,\mathbb R)$, every second-order partial derivative belongs to $C^1(E,\mathbb R)$. The notes add:

1. $s=1$ is the class of continuously differentiable maps;
2. the partial derivative of order zero is $f$ itself;
3. $f$ is $s$-times continuously differentiable at $a$ exactly when each coordinate function of $f$ is $s$-times continuously differentiable at $a$.

## Printed slide 10 (PDF p. 18). Inclusions of smoothness classes — Lemma 6.4.2

For open $E\subset\mathbb R^n$:

1. if $k,s\in\mathbb Z_+\cup\{\infty\}$ and $k\le s$, then $C^s(E,\mathbb R^m)\subset C^k(E,\mathbb R^m)$;
2. if $s\in\mathbb N$ and $f\in C^s(E,\mathbb R^m)$, then $f$ is $s$-times differentiable on $E$.

The slide’s hand-drawn nested bands illustrate the inclusions among the classes.

## Handwritten page (PDF p. 19). Proof of the class inclusion

For a finite $s$, prove the first statement by induction on $s-k$. The case $k=s$ is immediate. If $k<s$ and $f\in C^{k+1}(E,\mathbb R^m)$, then every partial derivative of order $k$ is continuously differentiable, hence continuous; therefore $f\in C^k(E,\mathbb R^m)$. This proves $C^s(E,\mathbb R^m)\subset C^k(E,\mathbb R^m)$.

## Handwritten page (PDF p. 20). Proof that $C^s$ implies $s$-fold differentiability

Fix $k\in\{0,\ldots,s-1\}$. By the first part of Lemma 6.4.2, $f\in C^{k+1}(E,\mathbb R^m)$. Hence all partial derivatives of order $k$ are continuously differentiable on $E$. Applying this successively through order $s-1$ proves that $f$ is $s$-times differentiable on $E$.

## Printed slide 11 (PDF p. 21). Symmetry of mixed partial derivatives

Let $E\subset\mathbb R^2$, let $a$ be an interior point and $f:E\to\mathbb R$. Denote the variables by $x,y$ and suppose the second mixed partial derivatives $\frac{\partial^2 f}{\partial x\partial y}(a)$ and $\frac{\partial^2 f}{\partial y\partial x}(a)$ are defined. Must they be equal?

## Handwritten page (PDF p. 22). A counterexample to equality without hypotheses

Consider

$$
f(x,y)=\begin{cases}xy\,\dfrac{x^2-y^2}{x^2+y^2},&(x,y)\ne(0,0),\\0,&(x,y)=(0,0).\end{cases}
$$

The handwritten calculation differentiates the formula away from the origin and then computes the mixed partials at $(0,0)$. The first partial derivatives at the origin are both zero, but the two mixed derivatives are different (their values are calculated on the next page).

![Handwritten mixed-partial counterexample](../../assets/lectures-2025-26/lec63-64-p22-mixed-partials-counterexample.jpg)

## Handwritten page (PDF p. 23). The mixed partials have different values

For the preceding function,

$$
\frac{\partial f}{\partial x}(0,0)=\frac{\partial f}{\partial y}(0,0)=0,
$$

$$
\frac{\partial^2 f}{\partial x\partial y}(0,0)=\lim_{y\to0}\frac{-y}{y}=-1,\qquad
\frac{\partial^2 f}{\partial y\partial x}(0,0)=\lim_{x\to0}\frac{x}{x}=1.
$$

Thus both mixed partial derivatives exist but do not coincide.

## Printed slide 12 (PDF p. 24). Double increment

Mixed partial derivatives computed in different orders need not agree in general, but they do agree for sufficiently regular functions. Either continuity of the mixed partials or twice differentiability will provide a sufficient condition.

For $a=(x_0,y_0)$ define the double increment

$$
\Delta_a^2f(u,v)=f(x_0+u,y_0+v)-f(x_0+u,y_0)-f(x_0,y_0+v)+f(x_0,y_0).
$$

## Printed slide 13 (PDF p. 25). Double increment and mixed partials — Lemma 6.4.3

Let $E\subset\mathbb R^2$, $a=(x_0,y_0)$ be an interior point, $f:E\to\mathbb R$, $\delta>0$, and suppose the first partial derivatives of $f$ are defined on $V_\delta(a)$; let $(u,v)\in V_\delta(0,0)$. Then:

1. there is $\theta\in(0,1)$ such that

$$
\Delta_a^2f(u,v)=\left(\frac{\partial f}{\partial x}(x_0+\theta u,y_0+v)-\frac{\partial f}{\partial x}(x_0+\theta u,y_0)\right)u;
$$

2. if both mixed partial derivatives are also defined on $V_\delta(a)$, there are $\theta_x,\theta_y\in(0,1)$ such that

$$
\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial x\partial y}(x_0+\theta_xu,y_0+\theta_yv)uv.
$$

## Handwritten page (PDF p. 26). Proof of Lemma 6.4.3

First hold $y=y_0+v$ fixed and apply the one-variable mean value theorem in $x$ to the difference $f(x_0+u,y_0+v)-f(x_0,y_0+v)$, subtracting the corresponding difference at $y_0$. This gives item 1. Next apply the mean value theorem in $y$ to the resulting difference of $f_x$; this yields the mixed-partial formula in item 2 with intermediate coordinates $x_0+\theta_xu$ and $y_0+\theta_yv$.

![Handwritten proof of the double-increment lemma](../../assets/lectures-2025-26/lec63-64-p26-double-increment-mean-value.jpg)

## Printed slide 14 (PDF p. 27). Symmetric form of Lemma 6.4.3

Interchanging $x$ and $y$ in the proof gives $\tilde\theta,\tilde\theta_x,\tilde\theta_y\in(0,1)$ such that

$$
\Delta_a^2f(u,v)=\left(\frac{\partial f}{\partial y}(x_0+u,y_0+\tilde\theta v)-\frac{\partial f}{\partial y}(x_0,y_0+\tilde\theta v)\right)v,
$$

$$
\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial y\partial x}(x_0+\tilde\theta_xu,y_0+\tilde\theta_yv)uv.
$$

## Printed slide 15 (PDF p. 28). Criterion for equality — Lemma 6.4.4

Suppose $f:E\to\mathbb R$, $E\subset\mathbb R^2$, has both second mixed partial derivatives at the interior point $a$. If, as $(u,v)\to(0,0)$,

$$
\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial x\partial y}(a)uv+o(u^2+v^2),
$$

$$
\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial y\partial x}(a)uv+o(u^2+v^2),
$$

then

$$
\frac{\partial^2f}{\partial x\partial y}(a)=\frac{\partial^2f}{\partial y\partial x}(a).
$$

## Handwritten page (PDF p. 29). Proof of Lemma 6.4.4

Subtract the two expansions. With $D=\frac{\partial^2f}{\partial x\partial y}(a)-\frac{\partial^2f}{\partial y\partial x}(a)$, we have $Duv=o(u^2+v^2)$. Set $u=v=t$; then $Dt^2=o(2t^2)$, so $D=0$ and the mixed partials are equal.

![Handwritten proof of the mixed-partial equality criterion](../../assets/lectures-2025-26/lec63-64-p29-double-increment-criterion.jpg)

## Printed slide 16 (PDF p. 30). Sufficient conditions for equality — Theorem 6.4.1

Let $E\subset\mathbb R^2$, let $a$ be an interior point, and let $f:E\to\mathbb R$. If either of the following holds:

1. both $\frac{\partial^2f}{\partial x\partial y}$ and $\frac{\partial^2f}{\partial y\partial x}$ are defined in a neighborhood of $a$ and continuous at $a$;
2. $f$ is twice differentiable at $a$;

then

$$
\frac{\partial^2f}{\partial x\partial y}(a)=\frac{\partial^2f}{\partial y\partial x}(a).
$$

## Handwritten page (PDF p. 31). Theorem 6.4.1, condition 1

By Lemma 6.4.3,

$$
\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial x\partial y}(x_0+\theta_xu,y_0+\theta_yv)uv.
$$

Continuity at $a$ gives

$$
\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial x\partial y}(a)uv+\alpha(u,v)uv,\qquad\alpha(u,v)\to0.
$$

Since $|uv|\le\frac12(u^2+v^2)$, the last term is $o(u^2+v^2)$. Interchanging $x,y$ gives the analogous expansion with $f_{yx}(a)$; Lemma 6.4.4 then proves the equality.

![Handwritten proof under the continuity hypothesis](../../assets/lectures-2025-26/lec63-64-p31-mixed-partial-symmetry-proof.jpg)

## Handwritten page (PDF p. 32). Theorem 6.4.1, condition 2: expansion

Now suppose $f$ is twice differentiable at $a$. Apply the first identity of Lemma 6.4.3 and expand the differentiable function $f_x$ at $a$. The increment has the form

$$
\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial x\partial y}(a)uv+\beta(u,v)u,
$$

where the error term comes from the remainders in the differentiability expansions of $f_x$ at $(x_0+\theta u,y_0+v)$ and $(x_0+\theta u,y_0)$.

## Handwritten page (PDF p. 33). Error estimate in condition 2

The handwritten proof writes the remainder as

$$
\beta(u,v)=\alpha(\theta u,v)\sqrt{\theta^2u^2+v^2}-\alpha(\theta u,0)|\theta u|,
$$

with $\alpha(h)\to0$. Since $|\theta u|\,|u|\le u^2\le u^2+v^2$ and $|u|\sqrt{\theta^2u^2+v^2}\le u^2+v^2$, it follows that

$$
\beta(u,v)u=o(u^2+v^2).
$$

Hence $\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial x\partial y}(a)uv+o(u^2+v^2)$. Interchanging $x,y$ gives the corresponding expression with $f_{yx}(a)$, so Lemma 6.4.4 completes the proof.

![Handwritten remainder estimate for Theorem 6.4.1](../../assets/lectures-2025-26/lec63-64-p33-differentiability-remainder-proof.jpg)

## Printed slide 17 (PDF p. 34). Continuous second derivatives — Corollary

If $f$ is twice continuously differentiable at $a$, then

$$
\frac{\partial^2f}{\partial x\partial y}(a)=\frac{\partial^2f}{\partial y\partial x}(a).
$$

## Printed slide 18 (PDF p. 35). Remarks on Theorem 6.4.1

Neither condition in Theorem 6.4.1 is necessary for symmetry of the mixed partial derivatives. Conditions 1 and 2 are independent: neither follows from the other. The source slide highlights the phrase “is not necessary” in red.

## Handwritten page (PDF p. 36). Example: mixed partials can be unbounded

Let

$$
\varphi(t)=\begin{cases}t^2\sin(1/t^2),&t\ne0,\\0,&t=0,\end{cases}\qquad f(x,y)=\varphi(x)\varphi(y).
$$

The function $\varphi$ is differentiable on $\mathbb R$, with

$$
\varphi'(t)=\begin{cases}2\left(t\sin(1/t^2)-\frac1t\cos(1/t^2)\right),&t\ne0,\\0,&t=0.\end{cases}
$$

All first- and second-order partial derivatives of $f$ at $(0,0)$ are zero. But

$$
\frac{\partial^2f}{\partial x\partial y}\left(\frac1{\sqrt{2\pi k}},\frac1{\sqrt{2\pi k}}\right)=\left(\varphi'\left(\frac1{\sqrt{2\pi k}}\right)\right)^2=8\pi k\to+\infty.
$$

Thus the mixed partial is unbounded near the origin and condition 1 of Theorem 6.4.1 is not satisfied.

## Handwritten page (PDF p. 37). The first partial derivative need not be differentiable

For $f(x,y)=\varphi(x)\varphi(y)$, the handwritten estimate along $(t,t)$ is

$$
\frac{f_x(t,t)}{\|(t,t)\|}=\sqrt2\left(t^2\sin^2(1/t^2)-\sin(1/t^2)\cos(1/t^2)\right)\not\to0.
$$

If $f_x$ were differentiable at $(0,0)$, then, since $f_x(0,0)=0$, this quotient would tend to zero. Therefore $f_x$ is not differentiable at the origin, so $f$ is not twice differentiable there.

## Handwritten page (PDF p. 38). Examples separating regularity properties

For the same $\varphi$ and $a=(0,0)$, the page records two examples:

1. $f(x,y)=\varphi(x)+\varphi(y)$ has continuous mixed partial derivatives at $a$ but is not twice differentiable at $a$.
2. $g(x,y)=\varphi(x)\varphi(y)$ is differentiable at $a$, but its mixed partial derivatives are unbounded near $a$.

These examples illustrate that the hypotheses in Theorem 6.4.1 are sufficient rather than necessary. The handwritten page labels the second construction as an exercise.

![Handwritten examples concerning mixed-partial hypotheses](../../assets/lectures-2025-26/lec63-64-p38-mixed-partial-independence-examples.jpg)

## Printed slide 19 (PDF p. 39). Higher-order differentials — Definition 6.4.3

Let $E\subset\mathbb R^n$, let $a$ be an interior point and $f:E\to\mathbb R^m$.

1. Set $d_a^0f(h)=f(a)$ for every $h\in\mathbb R^n$. The map $d_a^0f$ is the zero-order differential at $a$. For each $h$, the map $x\mapsto d_x^0f(h)$, defined at least at $a$, is the zero-order differential on increment $h$, denoted $d^0f(h)$. The slide highlights the phrase “at least at the point $a$” in red.
2. If $s\in\mathbb N$ and $d^{s-1}f(h)$ has already been defined, and for every $h\in\mathbb R^n$ the map $x\mapsto d_x^{s-1}f(h)$ is defined in a neighborhood of $a$ and differentiable at $a$, set

$$
d_a^sf(h)=d_a\bigl(d^{s-1}f(h)\bigr)(h)\qquad\text{for every }h\in\mathbb R^n.
$$

## Printed slide 20 (PDF p. 40). Higher-order differentials — Definition 6.4.3 (continued)

The map $d_a^sf$ is the differential of order $s$ at $a$. For every $h\in\mathbb R^n$, the map $x\mapsto d_x^sf(h)$, defined at least at $a$, is the differential of order $s$ on increment $h$, denoted $d^sf(h)$.

## Printed slide 21 (PDF p. 41). Computing higher differentials — Theorem 6.4.2

If $f:E\to\mathbb R^m$ is $s$-times differentiable at the interior point $a\in E\subset\mathbb R^n$, then its differential of order $s$ exists and

$$
d_a^sf(h)=\sum_{(i_1,\ldots,i_s)\in I_s}\frac{\partial^sf(a)}{\partial x_{i_1}\cdots\partial x_{i_s}}h_{i_1}\cdots h_{i_s}\qquad(h\in\mathbb R^n),
$$

$$
d_a^sf(h)=\sum_{\alpha\in M_s}\frac{s!}{\alpha!}\frac{\partial^\alpha f(a)}{\partial x^\alpha}h^\alpha\qquad(h\in\mathbb R^n).
$$

**Source correction.** The printed second formula omits the factor $h^\alpha$. It is included here because it is required for the multi-index formula to agree with the first formula and to be homogeneous of degree $s$ in $h$.

## Handwritten page (PDF p. 42). Multi-indices and the second differential

A multi-index is $\alpha=(\alpha_1,\ldots,\alpha_n)$ with $|\alpha|=\alpha_1+\cdots+\alpha_n=s$. Its factorial is $\alpha!=\alpha_1!\cdots\alpha_n!$, $x^\alpha=x_1^{\alpha_1}\cdots x_n^{\alpha_n}$, and $h^\alpha=h_1^{\alpha_1}\cdots h_n^{\alpha_n}$. The partial derivative $\partial^\alpha f/\partial x^\alpha$ means

$$
\frac{\partial^{|\alpha|}f}{\partial x_1^{\alpha_1}\cdots\partial x_n^{\alpha_n}}(a).
$$

If $\alpha_k=0$, no differentiation with respect to $x_k$ is performed. The handwritten page also records

$$
d_a^2f(h)=\sum_{i=1}^{n}\sum_{j=1}^{n}\frac{\partial^2f}{\partial x_i\partial x_j}(a)h_ih_j\qquad(h\in\mathbb R^n).
$$

![Handwritten multi-index definition and second differential](../../assets/lectures-2025-26/lec63-64-p42-multi-index-differential.jpg)

## Cross-references

This transcription duplicates the corresponding thematic chapters for semester 2 (lectures 33–64): [§6.3 — continuous differentiability](../../ru/lectures/16-continuous-differentiability-6-3.md) and [§6.4 — higher derivatives and differentials](../../ru/lectures/17-higher-derivatives-6-4.md). See also the [Russian register index](../../ru/lectures/index.md).

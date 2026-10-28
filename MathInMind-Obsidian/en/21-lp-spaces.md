---
title: "Lp Spaces and Modes of Convergence"
lang: en
chapter: 21
part: "Modern analysis"
aliases: ["Lp Spaces and Modes of Convergence (en)"]
tags: [mathinmind/en, mathinmind/chapter]
---
# 21. $L^p$ Spaces and Modes of Convergence

[[en/20-lebesgue-integration|← 20. Lebesgue Integration and Convergence Theorems]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]]

> [!abstract] Goal
> Treat functions as points of [[en/14-several-variables#14.1 Euclidean space and norms|normed spaces]] and relate $L^p$, almost-everywhere, and mean-square convergence.

## 21.1 Definition and basic inequalities

For $1\le p<\infty$, define

$$
\|f\|_p=\left(\int_X|f|^p\,d\mu\right)^{1/p},
\qquad
L^p(\mu)=\{f\text{ measurable}:\|f\|_p<\infty\}.
$$

For $p=\infty$, $\|f\|_\infty$ is the essential supremum: the smallest $M$ such that $|f|\le M$ [[en/19-measure-theory#19.4 Measurable functions|almost everywhere]]. Functions equal almost everywhere are identified; this makes $\|\cdot\|_p$ a norm rather than only a seminorm.

> [!theorem] Hölder's inequality
> If $1/p+1/q=1$, then
> $$
> \int_X|fg|\,d\mu\le\|f\|_p\|g\|_q.
> $$

^holder-inequality

For $p=q=2$, this is [[#21.4 The Hilbert space L2|Cauchy–Schwarz]]. **Minkowski's inequality** is the triangle inequality

$$
\|f+g\|_p\le\|f\|_p+\|g\|_p.
$$

These inequalities show that $L^p$ is a normed vector space and help estimate products and perturbations.

## 21.2 Completeness and convergence

> [!theorem] Riesz–Fischer theorem
> Every $L^p$ space, $1\le p\le\infty$, is complete; thus it is a [[#21.1 Definition and basic inequalities|Banach space]].

^riesz-fischer-theorem

Convergence $\|f_n-f\|_p\to0$ is called convergence in $p$-th mean, or mean-square convergence when $p=2$. It implies convergence in [[en/19-measure-theory#19.2 Measures|measure]] and the existence of a [[en/03-sequences#3.4 Subsequences and Cauchy sequences|subsequence]] converging to $f$ almost everywhere. It does not imply that the original full sequence converges a.e.

Conversely, a.e. convergence does not imply $L^p$ convergence without an additional condition. [[en/20-lebesgue-integration#^dominated-convergence-theorem|Dominated convergence]] supplies one when $|f_n|^p\le g\in L^1$.

On a finite measure space and $1\le r<p\le\infty$,

$$
\|f\|_r\le\mu(X)^{1/r-1/p}\|f\|_p
$$

with the natural interpretation at endpoints. Hence $L^p\subseteq L^r$ and $L^p$ convergence implies $L^r$ convergence. These inclusions generally fail on infinite measure spaces.

## 21.3 Density and approximation

For $1\le p<\infty$, integrable simple functions are dense in $L^p$. Continuous compactly supported functions are dense in $L^p(\mathbb R^n)$. Consequently, many identities can first be proved for convenient functions and then extended by approximation.

Density of continuous functions fails in $L^\infty$ with the essential-sup norm: a [[en/10-function-sequences-series#^uniform-limit-continuity|uniform limit of continuous functions]] is continuous, so a discontinuous step function cannot be approximated arbitrarily well.

Truncation, mollification, and approximation by simple functions are standard techniques. They turn analytic problems into estimates on a dense subclass.

## 21.4 The Hilbert space L2

The space $L^2$ has inner product

$$
\langle f,g\rangle=\int_Xf\overline{g}\,d\mu,
\qquad \|f\|_2=\sqrt{\langle f,f\rangle}.
$$

Because it is complete, $L^2$ is a Hilbert space. If $K\subseteq L^2$ is closed and convex, every $f$ has a unique nearest point in $K$, the orthogonal projection. For a closed subspace $M$,

$$
f=P_Mf+(f-P_Mf),\qquad f-P_Mf\perp M.
$$

If $(e_n)$ is an orthonormal basis, then

$$
f=\sum_n\langle f,e_n\rangle e_n
\quad\text{in }L^2,
\qquad
\|f\|_2^2=\sum_n|\langle f,e_n\rangle|^2.
$$

[[en/12-fourier-series#12.1 Trigonometric system and coefficients|Fourier series]] are the trigonometric realization of this theory. Orthogonal projection also explains why Fourier [[en/04-numeric-series#4.1 Convergence through partial sums|partial sums]] give optimal mean-square approximations.

## Worked example

On $(0,1)$, $f(x)=x^{-\alpha}$ belongs to $L^p$ for finite $p$ exactly when

$$
\int_0^1x^{-\alpha p}\,dx<\infty
\iff \alpha p<1.
$$

On $(1,\infty)$, the same function belongs to $L^p$ exactly when $\alpha p>1$. Thus singularities near a point and decay at infinity impose opposite conditions.

## Common pitfalls

1. $L^p$ elements are equivalence classes modulo null sets, not pointwise-distinct functions.
2. Neither a.e. convergence nor $L^p$ convergence automatically implies the other for the full sequence.
3. Inclusion $L^p\subseteq L^r$ for $r<p$ requires finite measure.

## Exercises

1. Compute $\|x\|_p$ on $[0,1]$ for $1\le p<\infty$.
2. Show that $\int_0^1|f|\,dx\le\|f\|_p$ on $[0,1]$.
3. For $f_n=n^{1/p}1_{(0,1/n)}$, find the a.e. limit and $\|f_n\|_p$.

> [!answer]- Short answers
> 1. $\|x\|_p=(1/(p+1))^{1/p}$.
> 2. Apply Hölder with $g=1$ and $\|1\|_q=1$ on a measure-one space.
> 3. $f_n\to0$ a.e., while $\|f_n\|_p=1$ for every $n$; hence there is no $L^p$ convergence to zero.

---

[[en/20-lebesgue-integration|← 20. Lebesgue Integration and Convergence Theorems]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]]

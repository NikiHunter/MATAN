---
title: "Functions of Several Variables"
lang: en
chapter: 14
part: "Several variables and topology"
---
# 14. Functions of Several Variables

[← 13. Metric Spaces, Compactness, and Completeness](13-metric-spaces.md) · [Course index](index.md) · [Terms & theorems](term-index.md) · [15. Differentiation of Several-Variable Mappings →](15-multivariable-differentiation.md)

> **Goal.** Study limits and continuity in $`\mathbb R^n`$ and distinguish joint behavior from coordinate-wise behavior.

<a id="sec-14-1"></a>
## 14.1 Euclidean space and norms

A point of $`\mathbb R^n`$ is $`x=(x_1,\ldots,x_n)`$. The Euclidean norm and distance are

```math
\|x\|_2=\left(\sum_{i=1}^{n}x_i^2\right)^{1/2},
\qquad d(x,y)=\|x-y\|_2.
```

The [Cauchy–Schwarz inequality](21-lp-spaces.md#sec-21-4) $`|x\cdot y|\le\|x\|_2\|y\|_2`$ gives the triangle inequality. Other common norms are $`\|x\|_1=\sum|x_i|`$ and $`\|x\|_\infty=\max|x_i|`$.

All norms on a finite-dimensional real vector space are equivalent: for any two norms there are constants $`c,C>0`$ with $`c\|x\|_a\le\|x\|_b\le C\|x\|_a`$. Thus convergence, openness, and continuity do not depend on the chosen norm in $`\mathbb R^n`$.

A scalar function is $`f:D\to\mathbb R`$ with $`D\subseteq\mathbb R^n`$; a vector-valued mapping is $`F:D\to\mathbb R^m`$. Level sets $`\{x:f(x)=c\}`$ and graphs are useful geometric descriptions.

<a id="sec-14-2"></a>
## 14.2 Limits

For $`f:D\to\mathbb R`$ and a limit point $`a`$ of $`D`$,

```math
\lim_{x\to a}f(x)=L
```

means that for every $`\varepsilon>0`$ there is $`\delta>0`$ such that $`x\in D`$ and $`0<\|x-a\|<\delta`$ imply $`|f(x)-L|<\varepsilon`$.

For $`F=(F_1,\ldots,F_m)`$, convergence is equivalent to convergence of every component. The [sequential criterion](05-limits-continuity.md#sec-5-1) and the usual algebra laws remain valid.

> <a id="iterated-limit-warning"></a>**Iterated-limit warning.** Existence of
> ```math
> \lim_{x\to a}\lim_{y\to b}f(x,y),\qquad
> \lim_{y\to b}\lim_{x\to a}f(x,y)
> ```
> does not imply existence of the joint limit as $`(x,y)\to(a,b)`$.

Checking finitely many straight lines is never a proof of a joint limit. A positive proof usually uses an estimate in terms of $`\|x-a\|`$.

<a id="sec-14-3"></a>
## 14.3 Continuity and compact domains

A function is continuous at $`a`$ if $`f(x)\to f(a)`$ as $`x\to a`$. Sums, products, quotients away from zero denominators, and compositions preserve continuity. Polynomials are continuous everywhere; rational functions are continuous where their denominators are nonzero.

On a [compact](13-metric-spaces.md#sec-13-4) $`K\subseteq\mathbb R^n`$, a continuous real function is bounded and attains its extrema. It is also [uniformly continuous](05-limits-continuity.md#sec-5-4):

```math
\forall\varepsilon>0\;\exists\delta>0:\quad
\|x-y\|<\delta\implies|f(x)-f(y)|<\varepsilon.
```

On a [connected](13-metric-spaces.md#sec-13-5) set, a continuous function has the [intermediate-value property](05-limits-continuity.md#intermediate-value-theorem). Coordinate projections and [norms](#sec-14-1) are continuous, which helps establish many other examples.

<a id="sec-14-4"></a>
## 14.4 Two diagnostic examples

For

```math
f(x,y)=\frac{xy}{x^2+y^2},\qquad (x,y)\ne(0,0),
```

the value along $`y=kx`$ is $`k/(1+k^2)`$ for $`x\ne0`$. Different slopes give different limits, so no joint limit exists at the origin. Both [iterated limits](#iterated-limit-warning), however, are zero.

By contrast, for

```math
g(x,y)=\frac{x^2y}{x^2+y^2},
```

we have $`|g(x,y)|\le|y|`$ because $`x^2/(x^2+y^2)\le1`$. Hence $`g(x,y)\to0`$ as $`(x,y)\to(0,0)`$, and setting $`g(0,0)=0`$ makes it continuous.

## Worked example

Show that

```math
\lim_{(x,y)\to(0,0)}\frac{x^3+y^3}{x^2+y^2}=0.
```

Using $`|x|,|y|\le r=\sqrt{x^2+y^2}`$,

```math
\frac{|x^3+y^3|}{x^2+y^2}
\le\frac{|x|r^2+|y|r^2}{r^2}\le2r\to0.
```

This radial estimate proves the limit for every approach path simultaneously.

## Common pitfalls

1. Iterated limits and joint limits are different objects.
2. A path check can disprove a limit but generally cannot prove it.
3. Continuity in each variable separately does not imply joint continuity.

## Exercises

1. Show that $`xy/(x^2+y^2)^{1/2}`$ tends to zero at the origin.
2. Investigate the limit of $`x^2y/(x^4+y^2)`$ at the origin along $`y=kx^2`$.
3. Prove that $`F(x,y)=(x+y,xy)`$ is continuous.

<details>
<summary>Short answers</summary>

1. With $`r=\sqrt{x^2+y^2}`$, $`|xy|\le r^2/2`$, so the absolute value is at most $`r/2`$.
2. Along that path the value is $`k/(1+k^2)`$ for $`x\ne0`$, so the joint limit does not exist.
3. Its components are sums and products of continuous coordinate projections.
</details>

---

[← 13. Metric Spaces, Compactness, and Completeness](13-metric-spaces.md) · [Course index](index.md) · [Terms & theorems](term-index.md) · [15. Differentiation of Several-Variable Mappings →](15-multivariable-differentiation.md)

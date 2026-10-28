---
title: "Improper Integrals and Applications"
lang: en
chapter: 9
part: "One-variable calculus"
---
# 9. Improper Integrals and Applications

[← 8. The Riemann Integral](08-riemann-integration.md) · [Course index](index.md) · [Terms & theorems](term-index.md) · [10. Sequences and Series of Functions →](10-function-sequences-series.md)

> **Goal.** Treat unbounded intervals and integrands through limits, and use integrals for geometric and physical quantities.

<a id="sec-9-1"></a>
## 9.1 Definitions

For an unbounded interval, define

```math
\int_a^\infty f(x)\,dx
=\lim_{R\to\infty}\int_a^R f(x)\,dx
```

when the limit exists finitely. For an integrand unbounded near $`b`$, define

```math
\int_a^b f(x)\,dx
=\lim_{t\to b^-}\int_a^t f(x)\,dx.
```

If both endpoints are problematic, split at an [interior point](13-metric-spaces.md#sec-13-2) and require convergence of both pieces independently. On $`(-\infty,\infty)`$, the two tails must converge separately. The symmetric limit called the **principal value** may exist even when the improper integral does not.

For example,

```math
\int_1^\infty\frac{dx}{x^p}<\infty\iff p>1,
\qquad
\int_0^1\frac{dx}{x^p}<\infty\iff p<1.
```

<a id="sec-9-2"></a>
## 9.2 Convergence tests

For nonnegative integrands, boundedness of the truncated integrals is equivalent to convergence. Comparison and limit comparison work as for series: on an infinite interval, $`f\sim C/x^p`$ gives convergence for $`p>1`$.

[Absolute convergence](04-numeric-series.md#sec-4-3) means $`\int|f|`$ converges and implies ordinary convergence under the usual local-integrability assumptions. Conditional convergence can occur for oscillatory integrands.

> <a id="dirichlet-test-for-integrals"></a>**Dirichlet's test for integrals.** If $`F(T)=\int_a^T f`$ is bounded and $`g`$ decreases to zero with suitable regularity, then $`\int_a^\infty f(x)g(x)\,dx`$ converges.

Thus $`\int_1^\infty\sin x/x\,dx`$ converges conditionally: [integration by parts](08-riemann-integration.md#sec-8-4) or [Dirichlet's test](#dirichlet-test-for-integrals) proves convergence, while comparison on intervals around multiples of $`\pi`$ shows that $`\int|\sin x|/x`$ diverges.

The [Cauchy criterion](03-sequences.md#sec-3-4) for $`\int_a^\infty f`$ requires that $`\int_S^T f`$ become arbitrarily small for all sufficiently large $`S<T`$.

<a id="sec-9-3"></a>
## 9.3 Area, arc length, and volume

For $`f\ge g`$ on $`[a,b]`$, the area between graphs is

```math
A=\int_a^b(f(x)-g(x))\,dx.
```

In [polar coordinates](17-multiple-integrals.md#sec-17-3), the area swept by $`r=r(\theta)`$ is

```math
A=\frac12\int_\alpha^\beta r(\theta)^2\,d\theta.
```

The length of a [continuously differentiable](15-multivariable-differentiation.md#sec-15-1) curve $`\gamma(t)=(x(t),y(t))`$ is

```math
L=\int_a^b\sqrt{x'(t)^2+y'(t)^2}\,dt.
```

For a graph this becomes $`L=\int_a^b\sqrt{1+f'(x)^2}\,dx`$. In polar form,

```math
L=\int_\alpha^\beta\sqrt{r^2+(dr/d\theta)^2}\,d\theta.
```

If a solid has cross-sectional area $`A(x)`$, its volume is $`V=\int_a^b A(x)\,dx`$. Rotation of $`0\le y=f(x)`$ about the $`x`$-axis gives

```math
V=\pi\int_a^b f(x)^2\,dx,
```

while cylindrical shells about the $`y`$-axis give $`V=2\pi\int_a^b x f(x)\,dx`$ when $`x\ge0`$.

<a id="sec-9-4"></a>
## 9.4 Work and average value

A variable force $`F(x)`$ acting along a straight path performs work

```math
W=\int_a^b F(x)\,dx.
```

More generally, work along a curve is a [line integral](18-vector-calculus.md#sec-18-1), developed in Chapter 18. The average value of an integrable function is

```math
f_{\mathrm{avg}}=\frac1{b-a}\int_a^b f(x)\,dx.
```

These formulas are obtained by partitioning, approximating each small contribution, and passing to the limit; the same idea explains many integral applications.

## Worked example

The length of $`y=\frac23x^{3/2}`$ from $`0`$ to $`3`$ has $`y'=\sqrt x`$, hence

```math
L=\int_0^3\sqrt{1+x}\,dx
=\left.\frac23(1+x)^{3/2}\right|_0^3
=\frac{14}{3}.
```

## Common pitfalls

1. Never substitute infinity directly into an [antiderivative](08-riemann-integration.md#sec-8-3); take a limit.
2. Convergence of two symmetric pieces does not replace independent tail convergence.
3. [Arc length](#sec-9-3) uses $`\sqrt{1+(y')^2}`$, not $`1+y'`$.

## Exercises

1. Decide whether $`\int_0^\infty dx/(1+x^2)`$ converges and compute it.
2. Find the area inside one petal of $`r=\cos(2\theta)`$.
3. Compute the volume obtained by rotating $`y=\sqrt x`$, $`0\le x\le1`$, about the $`x`$-axis.

<details>
<summary>Short answers</summary>

1. It converges and equals $`\pi/2`$.
2. One petal corresponds to $`-\pi/4\le\theta\le\pi/4`$; its area is $`\pi/8`$.
3. $`V=\pi\int_0^1x\,dx=\pi/2`$.
</details>

---

[← 8. The Riemann Integral](08-riemann-integration.md) · [Course index](index.md) · [Terms & theorems](term-index.md) · [10. Sequences and Series of Functions →](10-function-sequences-series.md)

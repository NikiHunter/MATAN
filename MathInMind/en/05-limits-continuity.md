---
title: "Limits and Continuity of Functions"
lang: en
chapter: 5
part: "One-variable calculus"
---
# 5. Limits and Continuity of Functions

[← 4. Numerical Series](04-numeric-series.md) · [Course index](index.md) · [Terms & theorems](term-index.md) · [6. Differentiation in One Variable →](06-derivatives.md)

> **Goal.** Compute and prove functional limits, and use the global theorems for continuous functions on intervals.

<a id="sec-5-1"></a>
## 5.1 Limit at a point

Let $`f`$ be defined in a punctured neighborhood of $`a`$. We say $`f(x)\to L`$ as $`x\to a`$ if

```math
\forall\varepsilon>0\;\exists\delta>0:\quad
0<|x-a|<\delta\implies |f(x)-L|<\varepsilon.
```

The value $`f(a)`$, even if defined, does not affect this limit. A **sequential criterion** is often more convenient:

```math
f(x)\to L\iff \bigl(x_n\to a,\ x_n\ne a\implies f(x_n)\to L\bigr).
```

Right and left limits use $`a<x<a+\delta`$ and $`a-\delta<x<a`$. A two-sided limit exists exactly when both one-sided limits exist and coincide.

For example, $`|x|/x`$ has left limit $`-1`$ and right limit $`1`$ at $`0`$, so it has no two-sided limit. In contrast,

```math
\left|x\sin\frac1x\right|\le |x|\implies x\sin\frac1x\to0
```

by the [squeeze theorem](03-sequences.md#sec-3-2).

<a id="sec-5-2"></a>
## 5.2 Algebra, composition, and asymptotic behavior

If $`f(x)\to A`$ and $`g(x)\to B`$, then sums, products, and scalar multiples have the expected limits; quotients require $`B\ne0`$. If $`f(x)\to b`$ and $`g`$ is continuous at $`b`$, then $`g(f(x))\to g(b)`$.

Important standard limits include

```math
\lim_{x\to0}\frac{\sin x}{x}=1,
\qquad
\lim_{x\to0}\frac{e^x-1}{x}=1,
\qquad
\lim_{x\to0}(1+x)^{1/x}=e.
```

Infinite limits and limits at infinity use the same [quantifier](01-logic-sets-functions.md#sec-1-1) pattern with $`|x|`$ large or $`f(x)`$ large. Polynomial behavior at infinity is governed by the highest-degree term; for rational functions, compare the degrees.

<a id="sec-5-3"></a>
## 5.3 Continuity

A function $`f`$ is continuous at $`a`$ if $`f(a)`$ is defined and

```math
\lim_{x\to a}f(x)=f(a).
```

Equivalently, for every $`\varepsilon>0`$ there is $`\delta>0`$ such that $`|x-a|<\delta`$ implies $`|f(x)-f(a)|<\varepsilon`$. Continuity is preserved by sums, products, quotients away from zeros, and composition.

A removable discontinuity can be repaired by redefining $`f(a)`$. A jump has finite but unequal [one-sided limits](#sec-5-1). An essential discontinuity includes [oscillation](08-riemann-integration.md#sec-8-1) or infinite behavior.

> <a id="intermediate-value-theorem"></a>**Intermediate value theorem.** If $`f:[a,b]\to\mathbb R`$ is continuous and $`y`$ lies between $`f(a)`$ and $`f(b)`$, then there is $`c\in[a,b]`$ with $`f(c)=y`$.

In particular, a continuous function taking values of opposite signs has a zero. The proof follows by bisecting intervals and using completeness.

> <a id="extreme-value-theorem"></a>**Extreme value theorem.** A continuous function on a closed bounded interval is bounded and attains both its maximum and minimum.

[Compactness](13-metric-spaces.md#sec-13-4), not merely continuity, is the key. On $`(0,1)`$, the continuous function $`1/x`$ is unbounded.

<a id="sec-5-4"></a>
## 5.4 Uniform continuity

A function $`f`$ is uniformly continuous on $`E`$ if

```math
\forall\varepsilon>0\;\exists\delta>0\;\forall x,y\in E:
|x-y|<\delta\implies |f(x)-f(y)|<\varepsilon.
```

Here $`\delta`$ works for all pairs of points. Ordinary continuity allows $`\delta`$ to depend on the base point.

> <a id="heine-cantor-theorem"></a>**Heine–Cantor theorem.** A continuous function on a compact set is uniformly continuous. In particular, this holds on $`[a,b]`$.

The function $`x^2`$ is not uniformly continuous on $`\mathbb R`$, while a function with bounded [derivative](06-derivatives.md#sec-6-1) is uniformly continuous by the [mean value theorem](07-taylor-convexity.md#lagrange-mean-value-theorem). On $`(0,1)`$, $`\sin(1/x)`$ is continuous but not uniformly continuous.

## Worked example

Show that $`f(x)=x^2`$ is continuous at $`a`$. Estimate

```math
|x^2-a^2|=|x-a|\,|x+a|.
```

If $`|x-a|<1`$, then $`|x+a|\le2|a|+1`$. Therefore $`\delta=\min\{1,\varepsilon/(2|a|+1)\}`$ gives the required bound. The factor depending on $`a`$ also explains why this proof is not uniform on $`\mathbb R`$.

## Common pitfalls

1. A limit at $`a`$ does not use the value $`f(a)`$; continuity does.
2. Checking one path or one sequence is not a proof of a functional limit.
3. Continuity on every compact subset does not automatically give a single uniform $`\delta`$ on an unbounded domain.

## Exercises

1. Prove directly that $`\lim_{x\to2}(3x-1)=5`$.
2. Show that a continuous $`f:[0,1]\to[0,1]`$ has a fixed point.
3. Determine whether $`f(x)=1/x`$ is uniformly continuous on $`(1,\infty)`$ and on $`(0,1)`$.

<details>
<summary>Short answers</summary>

1. $`|f(x)-5|=3|x-2|`$; take $`\delta=\varepsilon/3`$.
2. Apply the [intermediate value theorem](#intermediate-value-theorem) to $`g(x)=f(x)-x`$; its endpoint values have opposite signs or one is zero.
3. It is uniformly continuous on $`(1,\infty)`$ because $`|f'(x)|\le1`$, but not on $`(0,1)`$; take points close to zero with increasingly small spacing.
</details>

---

[← 4. Numerical Series](04-numeric-series.md) · [Course index](index.md) · [Terms & theorems](term-index.md) · [6. Differentiation in One Variable →](06-derivatives.md)

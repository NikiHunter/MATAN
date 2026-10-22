---
title: "Mean Value Theorems, Taylor Expansion, and Convexity"
lang: en
chapter: 7
part: "One-variable calculus"
---
# 7. Mean Value Theorems, Taylor Expansion, and Convexity

[Previous](06-derivatives.md) · [Course index](index.md) · [Next](08-riemann-integration.md)

> **Goal.** Turn local derivative information into global estimates, approximations, and shape information.

## 7.1 Mean value theorems

> **Rolle's theorem.** If $f$ is continuous on $[a,b]$, differentiable on $(a,b)$, and $f(a)=f(b)$, then $f'(c)=0$ for some $c\in(a,b)$.

Apply the extreme value theorem: unless $f$ is constant, an interior maximum or minimum supplies the point.

> **Lagrange's mean value theorem.** Under the same continuity and differentiability assumptions, there is $c\in(a,b)$ such that
> $$f(b)-f(a)=f'(c)(b-a).$$

Consequences include: zero derivative on an interval implies constancy; equal derivatives imply difference by a constant; and $|f'|\le M$ implies the Lipschitz estimate $|f(x)-f(y)|\le M|x-y|$.

> **Cauchy's mean value theorem.** For suitable $f,g$ with $g'(x)\ne0$ on $(a,b)$, there is $c$ such that
> $$\frac{f(b)-f(a)}{g(b)-g(a)}=\frac{f'(c)}{g'(c)}.$$

## 7.2 L'Hôpital's rule

For indeterminate forms $0/0$ or $\infty/\infty$, under the standard differentiability and denominator conditions,

$$
\lim_{x\to a}\frac{f(x)}{g(x)}
=\lim_{x\to a}\frac{f'(x)}{g'(x)}
$$

if the latter limit exists (finite or infinite). The rule also applies at infinity and to one-sided limits. It does not apply to every quotient, and nonexistence of the derivative quotient does not automatically disprove the original limit.

For $0\cdot\infty$, $\infty-\infty$, $1^\infty$, $0^0$, or $\infty^0$, first rewrite the expression using algebra or logarithms.

## 7.3 Taylor's formula

If $f$ has enough derivatives near $a$, its Taylor polynomial is

$$
P_n(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k.
$$

Taylor's formula with Lagrange remainder states

$$
f(x)=P_n(x)+R_n(x),\qquad
R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}
$$

for some $\xi$ between $a$ and $x$, under the corresponding regularity assumptions. The Peano form is $R_n(x)=o((x-a)^n)$ as $x\to a$.

At zero, useful expansions are

$$
e^x=\sum_{k=0}^{n}\frac{x^k}{k!}+O(x^{n+1}),
$$
$$
\sin x=\sum_{k=0}^{n}\frac{(-1)^kx^{2k+1}}{(2k+1)!}+O(x^{2n+3}),
$$
$$
\log(1+x)=\sum_{k=1}^{n}\frac{(-1)^{k-1}x^k}{k}+O(x^{n+1}).
$$

Remainder estimates justify numerical approximations; the polynomial alone does not prove convergence of an infinite Taylor series.

## 7.4 Convex functions

A function $f$ is convex on an interval $I$ if for all $x,y\in I$ and $t\in[0,1]$,

$$
f((1-t)x+ty)\le(1-t)f(x)+tf(y).
$$

Geometrically, each chord lies above the graph. Strict convexity uses strict inequality for $x\ne y$ and $0<t<1$.

- A differentiable $f$ is convex exactly when $f'$ is nondecreasing.
- If $f''\ge0$, then $f$ is convex; $f''>0$ gives strict convexity.
- Convexity is equivalent to the tangent-line inequality
  $$f(y)\ge f(x)+f'(x)(y-x)$$
  for differentiable $f$.

> **Jensen's inequality.** For convex $f$, weights $\lambda_i\ge0$ with sum $1$, and points $x_i$,
> $$f\left(\sum_{i=1}^{n}\lambda_i x_i\right)\le\sum_{i=1}^{n}\lambda_i f(x_i).$$

Applying Jensen to $-\log x$ gives the arithmetic–geometric mean inequality. A point where concavity changes is an inflection point; $f''(a)=0$ alone is not sufficient.

## Worked example

Prove $e^x\ge1+x$. The function $e^x$ is convex, and its tangent at $0$ is $1+x$, so the tangent inequality gives the result immediately. Equality holds only at $x=0$.

## Common pitfalls

1. The point $c$ in a mean value theorem is not generally unique or explicit.
2. A finite Taylor polynomial and an infinite Taylor series are different claims.
3. $f''(a)=0$ does not by itself prove an inflection point.

## Exercises

1. Show that $|\sin x-\sin y|\le|x-y|$.
2. Approximate $\sqrt{1+x}$ through second order and estimate the error for small $x>0$.
3. Prove $x\log x\ge x-1$ for $x>0$ using convexity or a tangent line.

<details>
<summary>Short answers</summary>

1. Apply Lagrange's theorem and use $|\cos c|\le1$.
2. $\sqrt{1+x}=1+x/2-x^2/8+O(x^3)$; bound the third derivative on the relevant interval for a Lagrange-remainder estimate.
3. The tangent to $x\log x$ at $x=1$ is $x-1$; the second derivative $1/x$ is positive.
</details>

---

[Previous](06-derivatives.md) · [Course index](index.md) · [Next](08-riemann-integration.md)

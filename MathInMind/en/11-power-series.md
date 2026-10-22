---
title: "Power Series and Analytic Functions"
lang: en
chapter: 11
part: "Infinite processes"
---
# 11. Power Series and Analytic Functions

[Previous](10-function-sequences-series.md) · [Course index](index.md) · [Next](12-fourier-series.md)

> **Goal.** Determine convergence regions, manipulate power series term by term, and distinguish smoothness from analyticity.

## 11.1 Radius of convergence

A power series centered at $a$ has the form

$$
\sum_{n=0}^{\infty}c_n(x-a)^n.
$$

Its radius of convergence $R\in[0,\infty]$ is given by the Cauchy–Hadamard formula

$$
\frac1R=\limsup_{n\to\infty}\sqrt[n]{|c_n|},
$$

with the conventions $1/0=\infty$ and $1/\infty=0$. The series converges absolutely for $|x-a|<R$ and diverges for $|x-a|>R$. At $|x-a|=R$, each endpoint must be tested separately.

If the ratio limit exists, a practical alternative is

$$
R=\lim_{n\to\infty}\left|\frac{c_n}{c_{n+1}}\right|.
$$

More directly, apply the ratio or root test to the terms $c_n(x-a)^n$, including the factor involving $x$.

## 11.2 Uniform convergence and calculus

On every closed subinterval of $(a-R,a+R)$, a power series converges uniformly. Consequently its sum is continuous on the open interval of convergence. For $|x-a|<R$,

$$
\frac{d}{dx}\sum_{n=0}^{\infty}c_n(x-a)^n
=\sum_{n=1}^{\infty}nc_n(x-a)^{n-1},
$$
$$
\int_a^x\sum_{n=0}^{\infty}c_n(t-a)^n\,dt
=\sum_{n=0}^{\infty}\frac{c_n}{n+1}(x-a)^{n+1}.
$$

The differentiated and integrated series have the same radius $R$. Repeating differentiation shows that the sum is infinitely differentiable inside the interval and

$$
c_n=\frac{f^{(n)}(a)}{n!}.
$$

This uniqueness result means that coefficients can often be found from any valid expansion, not only by computing derivatives.

## 11.3 Standard expansions

The following identities are especially useful:

$$
e^x=\sum_{n=0}^{\infty}\frac{x^n}{n!},\qquad x\in\mathbb R,
$$
$$
\sin x=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+1}}{(2n+1)!},
\qquad
\cos x=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n}}{(2n)!},
$$
$$
\log(1+x)=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}x^n}{n},
\qquad -1<x\le1,
$$
$$
\arctan x=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+1}}{2n+1},
\qquad |x|\le1.
$$

For the binomial series,

$$
(1+x)^\alpha=\sum_{n=0}^{\infty}\binom{\alpha}{n}x^n,
\qquad |x|<1,
$$

where $\binom{\alpha}{n}=\alpha(\alpha-1)\cdots(\alpha-n+1)/n!$.

> **Abel's theorem.** If a power series converges at an endpoint, its sum is continuous from inside the interval up to that endpoint. This justifies taking one-sided limits in identities valid for $|x-a|<R$.

## 11.4 Analytic does not mean merely smooth

A function is **analytic** near $a$ if it equals a convergent power series in some neighborhood of $a$. Analytic functions are infinitely differentiable, but the converse is false.

Define $f(x)=e^{-1/x^2}$ for $x\ne0$ and $f(0)=0$. Then $f\in C^\infty(\mathbb R)$ and every derivative at zero is zero. Its Taylor series centered at zero is identically zero, so it does not represent $f$ in any neighborhood of zero.

Thus, to prove an infinite Taylor expansion, one must show convergence of the series and that its sum equals the function, usually by estimating the remainder.

## Worked example

Start with

$$
\frac1{1+x^2}=\sum_{n=0}^{\infty}(-1)^n x^{2n},
\qquad |x|<1.
$$

Multiplication by $x$ gives $x/(1+x^2)=\sum(-1)^n x^{2n+1}$. Integrating from $0$ to $x$ yields

$$
\frac12\log(1+x^2)
=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+2}}{2n+2}.
$$

All operations are valid inside the same open interval of convergence.

## Common pitfalls

1. The radius gives no answer at the endpoints.
2. Termwise differentiation is automatic only inside the open interval, not automatically at an endpoint.
3. Infinite differentiability does not guarantee equality with the Taylor series.

## Exercises

1. Find the radius and interval of convergence of $\sum n x^n/2^n$.
2. Find the interval of convergence of $\sum x^n/n^2$.
3. Evaluate $\sum_{n=1}^{\infty}n/2^n$.

<details>
<summary>Short answers</summary>

1. $R=2$; both $x=2$ and $x=-2$ diverge, so the interval is $(-2,2)$.
2. $R=1$; both endpoints converge absolutely, giving $[-1,1]$.
3. Use $\sum nx^{n-1}=(1-x)^{-2}$ or $\sum nx^n=x/(1-x)^2$ at $x=1/2$; the sum is $2$.
</details>

---

[Previous](10-function-sequences-series.md) · [Course index](index.md) · [Next](12-fourier-series.md)

---
title: "Fourier Series"
lang: en
chapter: 12
part: "Infinite processes"
---
# 12. Fourier Series

[Previous](11-power-series.md) · [Course index](index.md) · [Next](13-metric-spaces.md)

> **Goal.** Represent periodic functions by orthogonal trigonometric modes and distinguish pointwise from mean-square convergence.

## 12.1 Trigonometric system and coefficients

For a $2\pi$-periodic integrable function $f$, define

$$
a_0=\frac1\pi\int_{-\pi}^{\pi}f(x)\,dx,
$$
$$
a_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos(nx)\,dx,
\qquad
b_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin(nx)\,dx.
$$

Its Fourier series is

$$
f(x)\sim \frac{a_0}{2}
+\sum_{n=1}^{\infty}\bigl(a_n\cos(nx)+b_n\sin(nx)\bigr).
$$

The symbol $\sim$ initially means only that these are the associated coefficients; equality requires a convergence theorem.

The system $\{1,\cos nx,\sin nx\}$ is orthogonal under the inner product

$$
\langle f,g\rangle=\int_{-\pi}^{\pi}f(x)g(x)\,dx.
$$

For example, $\int_{-\pi}^{\pi}\cos(nx)\sin(mx)\,dx=0$, while $\int_{-\pi}^{\pi}\cos^2(nx)\,dx=\pi$ for $n\ge1$.

For a period $2L$, replace $nx$ by $n\pi x/L$ and integrate over an interval of length $2L$ with the corresponding normalization.

## 12.2 Symmetry

If $f$ is even, all $b_n=0$ and

$$
a_n=\frac2\pi\int_0^\pi f(x)\cos(nx)\,dx.
$$

If $f$ is odd, all $a_n=0$ and

$$
b_n=\frac2\pi\int_0^\pi f(x)\sin(nx)\,dx.
$$

Half-range sine and cosine expansions represent, respectively, odd and even periodic extensions of a function defined on $(0,L)$. Their boundary behavior must be read from the extension.

## 12.3 Convergence

> **Dirichlet's pointwise theorem.** If a periodic $f$ is piecewise continuous and piecewise continuously differentiable, its Fourier series converges at every point to
> $$\frac{f(x^-)+f(x^+)}2.$$
> At points of continuity this is simply $f(x)$.

At a jump, the Fourier series chooses the midpoint, regardless of how $f(x)$ is defined at the point.

For square-integrable functions, Fourier partial sums give the best mean-square approximation by trigonometric polynomials of the same degree, and

$$
\int_{-\pi}^{\pi}|f(x)-s_N(x)|^2\,dx\to0.
$$

This does not by itself imply pointwise convergence. Uniform convergence requires stronger hypotheses; near jumps, partial sums exhibit the Gibbs overshoot.

## 12.4 Parseval's identity

For $f\in L^2([-\pi,\pi])$,

$$
\frac1\pi\int_{-\pi}^{\pi}|f(x)|^2\,dx
=\frac{a_0^2}{2}+\sum_{n=1}^{\infty}(a_n^2+b_n^2).
$$

Parseval's identity is the infinite-dimensional Pythagorean theorem. It also turns coefficient computations into sums of numerical series.

Formal differentiation requires care. If $f$ is continuous, periodic, and piecewise smooth, with a suitably integrable derivative, then the Fourier series of $f'$ is obtained by termwise differentiation. Integration is generally more forgiving and introduces a zero-mean condition for periodicity.

## Worked example

For $f(x)=x$ on $(-\pi,\pi)$, extended periodically, oddness gives $a_n=0$. Integration by parts gives

$$
b_n=\frac2\pi\int_0^\pi x\sin(nx)\,dx
=\frac{2(-1)^{n+1}}n.
$$

Therefore

$$
x=2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}n\sin(nx),
\qquad -\pi<x<\pi.
$$

At $x=\pi$, the series is zero, the midpoint of the jump between $\pi$ and $-\pi$. Setting $x=\pi/2$ gives $\sum_{k=0}^{\infty}(-1)^k/(2k+1)=\pi/4$. Parseval gives $\sum_{n=1}^{\infty}1/n^2=\pi^2/6$.

## Common pitfalls

1. Writing an equals sign before proving convergence is unjustified.
2. At a jump, the limit is the average of one-sided values.
3. Mean-square convergence does not automatically imply pointwise convergence everywhere.

## Exercises

1. Find the Fourier series of $f(x)=x^2$ on $(-\pi,\pi)$.
2. Explain why the Fourier series of an even function contains only cosines.
3. Use Parseval for $f(x)=x$ to verify $\sum1/n^2=\pi^2/6$.

<details>
<summary>Short answers</summary>

1. $x^2=\pi^2/3+4\sum_{n=1}^{\infty}(-1)^n\cos(nx)/n^2$ on $[-\pi,\pi]$, with periodic extension understood.
2. Products $f(x)\sin(nx)$ are odd, so their symmetric integrals vanish.
3. Use $b_n=2(-1)^{n+1}/n$ and $(1/\pi)\int_{-\pi}^{\pi}x^2\,dx=2\pi^2/3$.
</details>

---

[Previous](11-power-series.md) · [Course index](index.md) · [Next](13-metric-spaces.md)

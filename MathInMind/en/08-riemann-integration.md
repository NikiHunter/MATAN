---
title: "The Riemann Integral"
lang: en
chapter: 8
part: "One-variable calculus"
---
# 8. The Riemann Integral

[Previous](07-taylor-convexity.md) · [Course index](index.md) · [Next](09-improper-integrals-applications.md)

> **Goal.** Define integration through partitions, connect it with differentiation, and evaluate definite integrals rigorously.

## 8.1 Partitions and Darboux sums

Let $f:[a,b]\to\mathbb R$ be bounded. For a partition

$$
P:a=x_0<x_1<\cdots<x_n=b,
$$

write $\Delta x_i=x_i-x_{i-1}$, $m_i=\inf_{[x_{i-1},x_i]}f$, and $M_i=\sup_{[x_{i-1},x_i]}f$. The lower and upper Darboux sums are

$$
L(f,P)=\sum_{i=1}^{n}m_i\Delta x_i,
\qquad
U(f,P)=\sum_{i=1}^{n}M_i\Delta x_i.
$$

Refining a partition increases lower sums and decreases upper sums. Define

$$
\underline{\int_a^b}f=\sup_P L(f,P),
\qquad
\overline{\int_a^b}f=\inf_P U(f,P).
$$

The function is **Riemann integrable** when these quantities coincide; their common value is $\int_a^b f(x)\,dx$.

> **Integrability criterion.** A bounded $f$ is integrable exactly when for every $\varepsilon>0$ there is a partition $P$ such that $U(f,P)-L(f,P)<\varepsilon$.

Continuous functions and monotone functions on $[a,b]$ are integrable. More generally, Lebesgue's criterion states that a bounded function is Riemann integrable exactly when its set of discontinuities has Lebesgue measure zero.

## 8.2 Riemann sums and properties

A Riemann sum uses sample points $\xi_i\in[x_{i-1},x_i]$:

$$
S(f,P,\xi)=\sum_{i=1}^{n}f(\xi_i)\Delta x_i.
$$

For integrable $f$, these sums approach the integral as the mesh $\max_i\Delta x_i$ tends to zero. In particular, for continuous $f$,

$$
\int_a^b f(x)\,dx
=\lim_{n\to\infty}\frac{b-a}{n}\sum_{k=1}^{n}f\left(a+k\frac{b-a}{n}\right).
$$

For integrable $f,g$,

$$
\int_a^b(\alpha f+\beta g)=\alpha\int_a^b f+\beta\int_a^b g,
$$
$$
\int_a^b f=\int_a^c f+\int_c^b f,
$$

and $f\le g$ implies $\int f\le\int g$. Also,

$$
\left|\int_a^b f(x)\,dx\right|\le\int_a^b|f(x)|\,dx.
$$

By convention $\int_b^a f=-\int_a^b f$ and $\int_a^a f=0$.

> **Mean value theorem for integrals.** If $f$ is continuous on $[a,b]$, there is $c\in[a,b]$ with
> $$f(c)=\frac1{b-a}\int_a^b f(x)\,dx.$$

## 8.3 Fundamental theorem of calculus

> **First part.** If $f$ is continuous on $[a,b]$ and $F(x)=\int_a^x f(t)\,dt$, then $F$ is differentiable and $F'(x)=f(x)$.

The proof uses

$$
\frac{F(x+h)-F(x)}h=\frac1h\int_x^{x+h}f(t)\,dt\to f(x).
$$

> **Second part (Newton–Leibniz formula).** If $F'=f$ and $f$ is integrable, then
> $$\int_a^b f(x)\,dx=F(b)-F(a).$$

Consequently, integration by parts and substitution become

$$
\int_a^b u\,dv=[uv]_a^b-\int_a^b v\,du,
$$
$$
\int_a^b f(\varphi(x))\varphi'(x)\,dx
=\int_{\varphi(a)}^{\varphi(b)}f(t)\,dt
$$

under standard continuous-differentiability assumptions.

## 8.4 Computation techniques

Indefinite integration seeks an antiderivative: $\int f(x)\,dx=F(x)+C$. Useful methods include algebraic simplification, substitution, integration by parts, partial fractions for rational functions, and trigonometric substitution. A definite integral can sometimes be evaluated by symmetry even without an elementary antiderivative.

For example,

$$
\int_{-a}^{a}f(x)\,dx=2\int_0^a f(x)\,dx
$$

for even $f$, while the integral is zero for odd $f$.

## Worked example

Compute $\int_0^1 x^2\,dx$ from equal partitions. Since

$$
\frac1n\sum_{k=1}^{n}\left(\frac{k}{n}\right)^2
=\frac{n(n+1)(2n+1)}{6n^3}\to\frac13,
$$

the integral is $1/3$. The Newton–Leibniz formula confirms it with $F(x)=x^3/3$.

## Common pitfalls

1. An antiderivative formula alone does not justify crossing a discontinuity.
2. Reversing limits changes the sign.
3. The constant $C$ belongs to an indefinite integral, not to a definite one.

## Exercises

1. Evaluate $\int_0^\pi x\sin x\,dx$ by parts.
2. Compute $\lim_{n\to\infty}\frac1n\sum_{k=1}^n\frac1{1+k/n}$ as an integral.
3. Prove that if $f\ge0$ is continuous and $\int_a^b f=0$, then $f\equiv0$.

<details>
<summary>Short answers</summary>

1. The value is $\pi$.
2. It equals $\int_0^1(1+x)^{-1}\,dx=\log2$.
3. If $f(c)>0$, continuity makes $f$ positive on a subinterval, forcing a positive integral.
</details>

---

[Previous](07-taylor-convexity.md) · [Course index](index.md) · [Next](09-improper-integrals-applications.md)

---
title: "Numerical Series"
lang: en
chapter: 4
part: "Foundations"
---
# 4. Numerical Series

[Previous](03-sequences.md) · [Course index](index.md) · [Next](05-limits-continuity.md)

> **Goal.** Distinguish types of convergence and select an appropriate convergence test.

## 4.1 Convergence through partial sums

For $\sum_{n=1}^{\infty}a_n$, define $s_N=\sum_{n=1}^N a_n$. The series converges to $s$ if $s_N\to s$. If it converges, then $a_n=s_n-s_{n-1}\to0$. The converse is false, as the harmonic series shows.

The geometric series satisfies

$$
\sum_{n=0}^{\infty}q^n=\frac1{1-q}\quad(|q|<1),
$$

and diverges when $|q|\ge1$. A telescoping example is

$$
\sum_{n=1}^{\infty}\frac1{n(n+1)}
=\sum_{n=1}^{\infty}\left(\frac1n-\frac1{n+1}\right)=1.
$$

The Cauchy criterion says that for every $\varepsilon>0$ there is $N$ such that $m\ge n\ge N$ implies $|a_n+\cdots+a_m|<\varepsilon$.

## 4.2 Nonnegative terms

For $a_n\ge0$, partial sums are increasing, so the series converges exactly when they are bounded.

- **Comparison:** eventually $0\le a_n\le b_n$; convergence of $\sum b_n$ implies convergence of $\sum a_n$, and divergence of $\sum a_n$ implies divergence of $\sum b_n$.
- **Limit comparison:** if $a_n,b_n>0$ and $a_n/b_n\to c\in(0,\infty)$, both series behave alike.
- **Ratio test:** if $\lim |a_{n+1}/a_n|=r$, then $r<1$ gives absolute convergence and $r>1$ divergence. The case $r=1$ is inconclusive.
- **Root test:** if $\limsup\sqrt[n]{|a_n|}=r$, the same conclusions hold.
- **Integral test:** for positive decreasing $f$, $\sum f(n)$ and $\int_1^\infty f(x)\,dx$ converge or diverge together.

In particular,

$$
\sum_{n=1}^{\infty}\frac1{n^p}<\infty\iff p>1.
$$

Cauchy condensation is also useful for positive decreasing $a_n$: $\sum a_n$ converges exactly when $\sum 2^k a_{2^k}$ converges.

## 4.3 Absolute and conditional convergence

A series converges **absolutely** if $\sum|a_n|$ converges. Absolute convergence implies convergence by the Cauchy criterion. Convergence without absolute convergence is **conditional**.

> **Alternating-series test.** If $b_n\ge0$ decreases to zero, then $\sum(-1)^{n-1}b_n$ converges. Its sum lies between consecutive partial sums, and the remainder satisfies $|R_N|\le b_{N+1}$.

Thus $\sum(-1)^{n-1}/n$ converges conditionally. More generally:

- **Dirichlet:** if partial sums of $\sum a_n$ are bounded and $b_n$ decreases to $0$, then $\sum a_nb_n$ converges.
- **Abel:** if $\sum a_n$ converges and $(b_n)$ is monotone and bounded, then $\sum a_nb_n$ converges.

> **Rearrangement warning.** Rearrangements preserve the sum of an absolutely convergent series. A conditionally convergent real series can be rearranged to converge to any prescribed real number or to diverge (Riemann's theorem).

## Worked example

Test $\sum_{n=2}^{\infty}1/(n(\log n)^p)$. Condensation gives

$$
\sum_k 2^k\frac1{2^k(k\log2)^p}
=C\sum_k\frac1{k^p},
$$

so convergence holds exactly for $p>1$. This example is useful because the ordinary ratio test is inconclusive.

## Common pitfalls

1. $a_n\to0$ is necessary, not sufficient.
2. Ratio and root tests with limit $1$ give no conclusion.
3. Conditional convergence does not permit arbitrary rearrangement or term grouping without justification.

## Exercises

1. Determine convergence of $\sum n!/(n^n)$.
2. Show that $\sum(-1)^n/\sqrt n$ converges conditionally.
3. Determine whether $\sum(\sqrt{n^2+1}-n)$ converges.

<details>
<summary>Short answers</summary>

1. The ratio tends to $1/e<1$, so the series converges by the ratio test.
2. The alternating test applies, but $\sum1/\sqrt n$ diverges.
3. Rationalize: the term is $1/(\sqrt{n^2+1}+n)\sim1/(2n)$, so the series diverges.
</details>

---

[Previous](03-sequences.md) · [Course index](index.md) · [Next](05-limits-continuity.md)

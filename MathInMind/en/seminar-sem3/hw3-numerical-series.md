---
title: "Seminar NM-204. HW 3 — numerical series: solutions"
lang: en
hw: 3
---
# HW 3. Numerical series and convergence tests — solutions

[Русский](../../ru/seminar-sem3/hw3-numerical-series.md) · **English** · [Español](../../es/seminar-sem3/hw3-numerical-series.md)

[← HW 2](hw2-conditional-extremum.md) · [All assignments](index.md) · [HW 4 →](hw4-series-inequalities-bases.md) · [Lectures 67–68, §7.1–§7.2](../lectures-2025-26/lecture-67-68.md) · [Lectures 69–70, §7.3](../lectures-2025-26/lecture-69-70.md)

This page solves problems 3.1–3.11. Problems 1.2 and 2.2 from the "old" section are solved in [HW 1](hw1-taylor.md) and [HW 2](hw2-conditional-extremum.md), the series 2'.1–2'.3 in [HW 2](hw2-conditional-extremum.md).

## Three facts everything rests on

Notation: $`S_n=\sum_{k=1}^na_k`$ is the partial sum.

> **(F1) Necessary condition.** If the series $`\sum a_k`$ converges, then $`a_k\to0`$. Indeed, $`a_k=S_k-S_{k-1}\to S-S=0`$.

> **(F2) Criterion for non-negative series.** If $`a_k\ge0`$ for all $`k`$, the series converges if and only if the sequence $`(S_n)`$ is bounded above. Reason: $`S_{n+1}-S_n=a_{n+1}\ge0`$, the sequence $`(S_n)`$ is non-decreasing, and a monotone sequence converges if and only if it is bounded.

> **(F3) Finitely many terms do not affect convergence.** The series $`\sum_{k\ge1}a_k`$ and $`\sum_{k\ge N+1}a_k`$ converge or diverge together: their partial sums differ by the constant $`S_N`$.

(F2) and (F3) give the **classical comparison test**: if $`0\le a_k\le C\,b_k`$ for $`k>N`$ and $`\sum b_k`$ converges, then $`\sum a_k`$ converges (the partial sums of the tail of $`\sum a_k`$ are bounded by $`C\sum_{k>N}b_k`$).

The whole chain of problems 3.4 → 3.6 → 3.7, 3.9 is built the same way: each next test is the previous one applied to a well-chosen "reference" series.

## Problem 3.1

**Statement.** The series $`\sum a_k`$ converges. Prove that the sequence of partial sums is bounded.

**Proof.** By the definition of convergence there is a finite limit $`S=\lim S_n`$. Take $`\varepsilon=1`$: there is $`N`$ such that $`|S_n-S|<1`$ for all $`n>N`$, i.e. $`|S_n|<|S|+1`$. Put
```math
C=\max\{|S_1|,\dots,|S_N|,\ |S|+1\}.
```
Then $`|S_n|\le C`$ for all $`n\in\mathbb N`$. $`\blacksquare`$

**Why it works.** This is just the theorem "a convergent sequence is bounded" applied to $`(S_n)`$: the far terms are squeezed near the limit, and only finitely many remain. The converse is false: the series $`\sum(-1)^k`$ has bounded partial sums $`-1,0,-1,0,\dots`$ and diverges. Boundedness of partial sums is equivalent to convergence only for series of constant sign (F2). Problems 3.2 and 3.3 give two more examples of bounded partial sums of divergent series.

## Problem 3.2

**Statement.** $`x_0\in\mathbb R`$. Prove that the partial sums of $`\sum_{k=1}^\infty\sin(kx_0)`$ are bounded.

**Proof.** Let $`S_n=\sum_{k=1}^n\sin(kx_0)`$.

*Case $`x_0=2\pi m`$, $`m\in\mathbb Z`$.* Then $`\sin(kx_0)=0`$ for all $`k`$, and $`S_n=0`$.

*Case $`x_0\notin2\pi\mathbb Z`$.* Then $`\sin\frac{x_0}2\ne0`$. We prove by induction the identity
```math
2\sin\frac{x_0}2\cdot S_n=\cos\frac{x_0}2-\cos\Bigl(\bigl(n+\tfrac12\bigr)x_0\Bigr).\tag{1}
```
It rests on the formula $`2\sin\alpha\sin\beta=\cos(\beta-\alpha)-\cos(\beta+\alpha)`$ with $`\alpha=\frac{x_0}2`$, $`\beta=kx_0`$:
```math
2\sin\frac{x_0}2\sin(kx_0)=\cos\Bigl(\bigl(k-\tfrac12\bigr)x_0\Bigr)-\cos\Bigl(\bigl(k+\tfrac12\bigr)x_0\Bigr).\tag{2}
```
Base $`n=1`$: (1) coincides with (2) for $`k=1`$. Step: if (1) holds for $`n`$, then adding (2) with $`k=n+1`$,
```math
2\sin\frac{x_0}2\,S_{n+1}=\cos\frac{x_0}2-\cos\Bigl(\bigl(n+\tfrac12\bigr)x_0\Bigr)+\cos\Bigl(\bigl(n+\tfrac12\bigr)x_0\Bigr)-\cos\Bigl(\bigl(n+\tfrac32\bigr)x_0\Bigr),
```
which is (1) for $`n+1`$. From (1):
```math
|S_n|=\frac{\bigl|\cos\frac{x_0}2-\cos\bigl((n+\frac12)x_0\bigr)\bigr|}{2\bigl|\sin\frac{x_0}2\bigr|}\le\frac{1}{\bigl|\sin\frac{x_0}2\bigr|}.
```
The bound does not depend on $`n`$. $`\blacksquare`$

**Why it works.** Multiplying by $`2\sin\frac{x_0}2`$ turns each term into a difference of two "neighbouring" values of one sequence $`c_k=\cos\bigl((k-\frac12)x_0\bigr)`$: the term equals $`c_k-c_{k+1}`$. In the sum everything inside cancels (telescoping), only the ends remain. Geometrically, $`\sin(kx_0)`$ are projections of a vector that turns by the angle $`x_0`$ each time; the sum of such vectors walks along a circle of radius $`\frac1{2|\sin(x_0/2)|}`$ and does not escape to infinity. As $`x_0\to2\pi m`$ the bound gets worse (the radius grows), but at $`2\pi m`$ itself all terms are zero. The bound depends on $`x_0`$ but not on $`n`$ — that is enough.

## Problem 3.3

**Statement.** $`x_0\in\mathbb R`$. Prove that the series $`\sum_{k=1}^\infty\cos(kx_0)`$ diverges. $`^*`$ For which $`x_0`$ are its partial sums bounded?

**Divergence.** We show that the necessary condition (F1) fails: $`\cos(kx_0)\not\to0`$. Suppose the contrary: $`\cos(kx_0)\to0`$ as $`k\to\infty`$. Then the subsequence with even indices also tends to zero: $`\cos(2kx_0)\to0`$. But
```math
\cos(2kx_0)=2\cos^2(kx_0)-1\ \longrightarrow\ 2\cdot0-1=-1 .
```
A contradiction ($`0\ne-1`$). So the general term does not tend to zero, and the series diverges for every $`x_0`$. $`\blacksquare`$

In the terms of the hint: for $`\cos x_0=1`$ ($`x_0=2\pi m`$) all terms equal $`1`$; for $`\cos x_0=-1`$ ($`x_0=\pi+2\pi m`$) the terms are $`(-1)^k`$; otherwise the terms have no limit at all. The argument above covers all three cases at once.

**Boundedness of partial sums.** Let $`S_n=\sum_{k=1}^n\cos(kx_0)`$.

- If $`x_0=2\pi m`$, then $`S_n=n`$ — unbounded.
- If $`x_0\notin2\pi\mathbb Z`$, then $`\sin\frac{x_0}2\ne0`$, and the right factor is again $`2\sin\frac{x_0}2`$: by the formula $`2\sin\alpha\cos\beta=\sin(\beta+\alpha)-\sin(\beta-\alpha)`$
```math
2\sin\frac{x_0}2\cos(kx_0)=\sin\Bigl(\bigl(k+\tfrac12\bigr)x_0\Bigr)-\sin\Bigl(\bigl(k-\tfrac12\bigr)x_0\Bigr),
```
and by induction (as in 3.2)
```math
2\sin\frac{x_0}2\cdot S_n=\sin\Bigl(\bigl(n+\tfrac12\bigr)x_0\Bigr)-\sin\frac{x_0}2,\qquad|S_n|\le\frac{1}{\bigl|\sin\frac{x_0}2\bigr|}.
```
This includes the case $`\cos x_0=-1`$: there $`S_n\in\{-1,0\}`$.

**Answer.** The series diverges for all $`x_0`$. The partial sums are bounded if and only if $`x_0\notin\{2\pi m:\ m\in\mathbb Z\}`$.

**Why it works.** Cosines cancel each other "on average" just like sines, so the sums are bounded. But the terms do not decay, and the sum never settles: it wanders forever over a bounded set. The only exception is $`x_0=2\pi m`$, where all terms equal $`1`$ and nothing cancels. Compare with 3.2: the series of sines consists of zeros and converges for $`x_0\in\pi\mathbb Z`$, and diverges for $`x_0\notin\pi\mathbb Z`$ for the same reason. If $`\sin(kx_0)\to0`$, then $`\cos(2kx_0)=1-2\sin^2(kx_0)\to1`$ and $`\sin(2kx_0)\to0`$, whence $`\sin((2k+1)x_0)=\sin(2kx_0)\cos x_0+\cos(2kx_0)\sin x_0\to\sin x_0\ne0`$, although this is a subsequence of a sequence tending to zero.

## Problem 3.4 (generalised comparison test)

**Statement.** For $`n>N_0`$: $`a_n>0`$, $`b_n>0`$ and $`\dfrac{a_{n+1}}{a_n}\le\dfrac{b_{n+1}}{b_n}`$. Prove: a) if $`\sum b_k`$ converges, then $`\sum a_k`$ converges; b) if $`\sum a_k`$ diverges, then $`\sum b_k`$ diverges.

**Proof.** Rewrite the condition: for $`n>N_0`$
```math
\frac{a_{n+1}}{b_{n+1}}\le\frac{a_n}{b_n}
```
(both sides were multiplied by the positive number $`\frac{a_n}{b_{n+1}}`$). So the sequence $`\frac{a_n}{b_n}`$ is non-increasing for $`n>N_0`$, and for all $`n\ge N_0+1`$
```math
\frac{a_n}{b_n}\le\frac{a_{N_0+1}}{b_{N_0+1}}=:C,\qquad\text{that is,}\qquad0<a_n\le C\,b_n .
```
(The same follows by multiplying the inequalities $`\frac{a_{j+1}}{a_j}\le\frac{b_{j+1}}{b_j}`$ over $`j=N_0+1,\dots,n-1`$: the products telescope to $`\frac{a_n}{a_{N_0+1}}\le\frac{b_n}{b_{N_0+1}}`$.)

a) Let $`\sum b_k`$ converge. By (F3) the tail $`\sum_{k>N_0}b_k`$ converges; let its sum be $`B`$. For $`n>N_0`$
```math
\sum_{k=N_0+1}^na_k\le C\sum_{k=N_0+1}^nb_k\le C\,B .
```
The partial sums of the positive series $`\sum_{k>N_0}a_k`$ are bounded, by (F2) it converges, and by (F3) so does $`\sum_{k\ge1}a_k`$.

b) This is the contrapositive of a): if $`\sum b_k`$ converged, then by a) $`\sum a_k`$ would converge, contrary to the hypothesis. $`\blacksquare`$

**Why it works.** The ratio $`\frac{a_{n+1}}{a_n}`$ is the "rate of decay" of the series per step. The condition says that at each step $`a_n`$ decays no slower than $`b_n`$. But then over many steps $`a_n`$ also decays no slower, i.e. $`a_n`$ is at most $`b_n`$ up to a constant factor — and a constant factor does not affect convergence. The generalised test is the classical one with ratios compared instead of the terms themselves; it is convenient when the ratio $`\frac{a_{n+1}}{a_n}`$ is simpler than $`a_n`$ itself (factorials, products).

## Problem 3.5

**Statement.** Prove that $`\sum_{k=1}^\infty\frac1{k!}`$ converges: a) by the classical comparison test; b) by the generalised one.

Reference: the series $`\sum_{k=1}^\infty\frac{1}{k(k+1)}`$ converges (its partial sums equal $`1-\frac1{n+1}`$).

**a)** For $`k\ge1`$ we have $`(k+1)!=(k+1)\cdot k\cdot(k-1)!\ge k(k+1)`$, whence
```math
0<\frac1{(k+1)!}\le\frac1{k(k+1)} .
```
By the classical comparison test the series $`\sum_{k=1}^\infty\frac1{(k+1)!}=\sum_{k=2}^\infty\frac1{k!}`$ converges, and with it, by (F3), $`\sum_{k=1}^\infty\frac1{k!}`$. $`\blacksquare`$

**b)** Let $`a_k=\frac1{k!}`$, $`b_k=\frac1{k(k+1)}`$. Then
```math
\frac{a_{k+1}}{a_k}=\frac1{k+1},\qquad\frac{b_{k+1}}{b_k}=\frac{k(k+1)}{(k+1)(k+2)}=\frac{k}{k+2}.
```
The inequality $`\frac1{k+1}\le\frac k{k+2}`$ is equivalent to $`k+2\le k^2+k`$, i.e. $`k^2\ge2`$; it holds for all $`k\ge2`$. The hypothesis of problem 3.4 holds with $`N_0=1`$, the series $`\sum b_k`$ converges, hence $`\sum a_k`$ converges. $`\blacksquare`$

**Why it works.** The factorial grows faster than any polynomial, so $`\frac1{k!}`$ is comfortably below a $`\frac1{k^2}`$-like reference. Part b) shows what the generalised test is good for: the ratio of consecutive terms $`\frac1{k+1}`$ of the factorial series tends to zero, that of the reference, $`\frac k{k+2}`$, tends to one, and they are easier to compare than the terms themselves. For $`k=1`$ the ratio inequality fails ($`\frac12>\frac13`$), but the test only needs it from some index on.

## Problem 3.6 (Kummer's test)

**Statement.** $`x_n>0`$ for all $`n`$; $`a_n>0`$ for $`n>N_0`$.

1) If for some $`\alpha>0`$ and all $`n>N_1`$ (where $`N_1>N_0`$) we have $`x_n\dfrac{a_n}{a_{n+1}}-x_{n+1}\ge\alpha`$, then $`\sum a_k`$ converges.

2) If $`\sum\dfrac1{x_k}`$ diverges and for all $`n>N_2`$ (where $`N_2>N_0`$) we have $`x_n\dfrac{a_n}{a_{n+1}}-x_{n+1}\le0`$, then $`\sum a_k`$ diverges.

**Proof of 1).** Multiply the inequality by $`a_{n+1}>0`$: for $`n>N_1`$
```math
x_na_n-x_{n+1}a_{n+1}\ge\alpha\,a_{n+1}.\tag{3}
```
Sum (3) over $`n=N_1+1,\dots,N_1+m`$. The left-hand side telescopes:
```math
\alpha\sum_{n=N_1+1}^{N_1+m}a_{n+1}\le x_{N_1+1}a_{N_1+1}-x_{N_1+m+1}a_{N_1+m+1}<x_{N_1+1}a_{N_1+1},
```
since the subtracted term is positive. So for every $`m`$
```math
\sum_{k=1}^ma_{k+N_1+1}<x_{N_1+1}\cdot\frac{a_{N_1+1}}{\alpha}.
```
The partial sums of the positive series $`\sum_{k\ge1}a_{k+N_1+1}`$ are bounded, by (F2) it converges, and by (F3) $`\sum a_k`$ converges. $`\blacksquare`$

**Proof of 2).** For $`n>N_2`$ the condition gives $`x_na_n\le x_{n+1}a_{n+1}`$, i.e.
```math
\frac{a_{n+1}}{a_n}\ge\frac{x_n}{x_{n+1}}=\frac{1/x_{n+1}}{1/x_n}.
```
Put $`c_n=\frac1{x_n}>0`$. Then $`\frac{c_{n+1}}{c_n}\le\frac{a_{n+1}}{a_n}`$ for $`n>N_2`$, and the series $`\sum c_k`$ diverges. By problem 3.4 b) (with $`c`$ in the role of "$`a`$" and $`a`$ in the role of "$`b`$") the series $`\sum a_k`$ diverges. $`\blacksquare`$

**Why it works.** The quantity $`x_na_n`$ is a "weighted" term of the series. Inequality (3) says: at each step the weighted term decreases by at least $`\alpha a_{n+1}`$. But $`x_na_n`$ is positive and cannot decrease in total by more than its initial value. So the sum of all the "decreases", i.e. $`\alpha\sum a_{n+1}`$, is finite. It is a conservation argument: the series pays for each of its terms out of the limited budget $`x_{N_1+1}a_{N_1+1}`$.

In part 2 the weighted term $`x_na_n`$ does not decrease, so $`a_n\ge\frac{\mathrm{const}}{x_n}`$: the series dominates the divergent series $`\sum\frac1{x_n}`$ from above. The divergence of $`\sum\frac1{x_k}`$ is needed exactly here, and without it the statement is false: for $`x_n=n^2`$ and $`a_n=\frac1{n^2}`$ the left-hand side equals $`n^2\cdot\frac{(n+1)^2}{n^2}-(n+1)^2=0\le0`$, yet the series converges.

Kummer's test is not a single test but a template: every sequence $`(x_n)`$ gives its own test. The slower $`\sum\frac1{x_n}`$ diverges, the finer the test: $`x_n=1`$ gives d'Alembert (3.7), $`x_n=n`$ gives Raabe (3.9), $`x_n=n\ln n`$ gives Bertrand's test.

## Problem 3.7 (d'Alembert's test)

**Statement.** $`a_n>0`$ for $`n>N_0`$. 1) If $`\dfrac{a_n}{a_{n+1}}\ge1+\beta`$ for $`n>N_1`$, $`\beta>0`$, the series converges. 2) If $`\dfrac{a_n}{a_{n+1}}\le1`$ for $`n>N_2`$, the series diverges.

**Proof.** Apply Kummer's test with $`x_n=1`$ for all $`n`$. Then
```math
x_n\frac{a_n}{a_{n+1}}-x_{n+1}=\frac{a_n}{a_{n+1}}-1 .
```
1) By hypothesis this quantity is $`\ge\beta`$ for $`n>N_1`$; by 3.6, 1) with $`\alpha=\beta`$ the series converges.
2) The series $`\sum\frac1{x_k}=\sum1`$ diverges, and $`\frac{a_n}{a_{n+1}}-1\le0`$ for $`n>N_2`$; by 3.6, 2) the series diverges. $`\blacksquare`$

**Why it works.** In part 1) $`a_{n+1}\le\frac{a_n}{1+\beta}`$: the terms decay no slower than a geometric progression with ratio $`q=\frac1{1+\beta}<1`$. In part 2) $`a_{n+1}\ge a_n>0`$: the terms do not decrease and do not tend to zero, so (F1) fails. It matters that 1) needs a gap $`\beta>0`$ independent of $`n`$: the condition $`\frac{a_n}{a_{n+1}}>1`$ is not enough (harmonic series: $`\frac{a_n}{a_{n+1}}=1+\frac1n>1`$, and the series diverges). This "gap tending to zero" is what Raabe's test handles.

## Problem 3.8

**Statement.** $`a_k=2^{-k}`$ for odd $`k`$, $`a_k=3^{-k}`$ for even $`k`$. Prove: 1) the series converges; 2) the sets $`\bigl\{k:\ \frac{a_k}{a_{k+1}}\le1\bigr\}`$ and $`\bigl\{k:\ \frac{a_k}{a_{k+1}}\ge\frac92\bigr\}`$ are countable.

**Proof.** 1) For all $`k`$ we have $`0<a_k\le2^{-k}`$, and the geometric series $`\sum2^{-k}`$ converges; by the classical comparison test the series converges.

2) *$`k`$ even.* Then $`k+1`$ is odd and
```math
\frac{a_k}{a_{k+1}}=\frac{3^{-k}}{2^{-(k+1)}}=2\Bigl(\frac23\Bigr)^k\le2\cdot\frac49=\frac89<1 .
```
*$`k`$ odd.* Then $`k+1`$ is even and
```math
\frac{a_k}{a_{k+1}}=\frac{2^{-k}}{3^{-(k+1)}}=3\Bigl(\frac32\Bigr)^k\ge3\cdot\frac32=\frac92 .
```
So the first set is all even numbers and the second is all odd numbers. Each is an infinite subset of $`\mathbb N`$, hence countable (bijections $`m\mapsto2m`$ and $`m\mapsto2m-1`$). $`\blacksquare`$

**Why it works.** The series is made of two geometric progressions interleaved. Passing from the "slow" progression to the "fast" one gives a huge ratio; passing back gives a ratio below one, i.e. the term **grows**. So the inequality $`\frac{a_k}{a_{k+1}}\le1`$ from d'Alembert's divergence condition holds for infinitely many $`k`$, yet the series converges. Conclusion: in d'Alembert's test the words "from some index on" cannot be replaced by "for infinitely many indices".

For Cauchy's root test such a replacement is legitimate: if $`\sqrt[k]{a_k}\ge1`$ for infinitely many $`k`$, then $`a_k\ge1`$ for infinitely many $`k`$, the general term does not tend to zero, and the series diverges. The difference is that the root estimates the term **itself**, while the ratio only sees its change over one step: one step up does not prevent the series from decaying overall. For our series $`\sqrt[k]{a_k}\le\frac12`$, so Cauchy's test gives convergence at once, while d'Alembert's gives nothing (neither of its conditions holds from some index on).

## Problem 3.9 (Raabe's test)

**Statement.** $`a_n>0`$ for $`n>N_0`$. 1) If $`\dfrac{a_n}{a_{n+1}}\ge1+\dfrac{1+\gamma}n`$ for $`n>N_1`$, $`\gamma>0`$, the series converges. 2) If $`\dfrac{a_n}{a_{n+1}}\le1+\dfrac1n`$ for $`n>N_2`$, the series diverges.

**Proof.** Apply Kummer's test with $`x_n=n`$.

1) For $`n>N_1`$
```math
x_n\frac{a_n}{a_{n+1}}-x_{n+1}\ge n\Bigl(1+\frac{1+\gamma}n\Bigr)-(n+1)=\gamma .
```
By 3.6, 1) with $`\alpha=\gamma`$ the series converges.

2) The series $`\sum\frac1{x_k}=\sum\frac1k`$ diverges (harmonic), and for $`n>N_2`$
```math
x_n\frac{a_n}{a_{n+1}}-x_{n+1}\le n\Bigl(1+\frac1n\Bigr)-(n+1)=0 .
```
By 3.6, 2) the series diverges. $`\blacksquare`$

**Why it works.** The reference here is the series $`\sum\frac1{n^p}`$: for them $`\frac{a_n}{a_{n+1}}=\bigl(1+\frac1n\bigr)^p\approx1+\frac pn`$. Raabe's test measures the coefficient of $`\frac1n`$ in the ratio of consecutive terms: if it exceeds one with a margin ($`1+\gamma`$), the series behaves like $`\sum\frac1{n^{1+\gamma}}`$ and converges; if it is at most one, the series is no better than the harmonic one. Condition 2) means exactly $`(n+1)a_{n+1}\ge na_n`$, i.e. $`na_n`$ is non-decreasing and $`a_n\ge\frac{\mathrm{const}}n`$.

Raabe's test is stronger than d'Alembert's (problem 4.4 of HW 4): it works where $`\frac{a_n}{a_{n+1}}\to1`$ and d'Alembert is silent. But it has its own "dead zone": a coefficient of $`\frac1n`$ tending to $`1`$ from above (for example, $`a_n=\frac1{n\ln^2n}`$).

## Problem 3.10$`^*`$

**Statement.** Give an example of a convergent series for which the set $`\bigl\{k:\ \frac{a_k}{a_{k+1}}\le1+\frac1k\bigr\}`$ is countable.

**Solution.** The series of problem 3.8 works: $`a_k=2^{-k}`$ for odd $`k`$ and $`a_k=3^{-k}`$ for even $`k`$. It converges, all its terms are positive, and, as shown there:

- for even $`k`$: $`\dfrac{a_k}{a_{k+1}}\le\dfrac89<1<1+\dfrac1k`$ — such $`k`$ belong to the set;
- for odd $`k`$: $`\dfrac{a_k}{a_{k+1}}\ge\dfrac92>2\ge1+\dfrac1k`$ — such $`k`$ do not.

The set equals the set of all even numbers, which is countable. $`\blacksquare`$

**Why it works.** The problem shows for Raabe's test what 3.8 shows for d'Alembert's: the divergence condition $`\frac{a_k}{a_{k+1}}\le1+\frac1k`$ must hold **for all** sufficiently large $`k`$; an infinite set of indices is not enough. The example is deliberately taken with positive terms: if sign-changing series are allowed, the problem becomes empty (for $`\sum\frac{(-1)^k}{k^2}`$ all ratios are negative and the set is $`\mathbb N`$).

A finer example, where the ratio lies in the half-open interval $`(1;1+\frac1k]`$ for infinitely many $`k`$ (the terms decrease, but slowly), is built in problem 4.5 of [HW 4](hw4-series-inequalities-bases.md); it fits here as well.

## Problem 3.11$`^{**}`$

**Statement.** $`\alpha\in\mathbb R`$, $`0<M_1\le C_k\le M_2`$, $`a_k=\dfrac{C_k}{k^\alpha}`$. For which $`\alpha`$ does $`\sum a_k`$ converge?

**Answer.** The series converges for $`\alpha>1`$ and diverges for $`\alpha\le1`$.

**Solution.** From the hypothesis
```math
\frac{M_1}{k^\alpha}\le a_k\le\frac{M_2}{k^\alpha}.\tag{4}
```

*$`\alpha\le0`$.* Then $`k^{-\alpha}\ge1`$ and $`a_k\ge M_1>0`$: the general term does not tend to zero, the series diverges by (F1).

*$`0<\alpha\le1`$.* Then $`k^\alpha\le k`$ and $`a_k\ge\frac{M_1}{k}`$. The harmonic series diverges, so by the classical comparison test (if $`\sum a_k`$ converged, so would $`\sum\frac1k`$) the series diverges.

*$`\alpha>1`$.* We prove convergence of the reference $`b_k=\frac1{k^\alpha}`$ by Raabe's test. The ratio is
```math
\frac{b_k}{b_{k+1}}=\Bigl(1+\frac1k\Bigr)^\alpha .
```
By Taylor's formula with the Lagrange remainder for $`g(x)=(1+x)^\alpha`$, for $`x>0`$ there is $`\theta\in(0,1)`$ with
```math
(1+x)^\alpha=1+\alpha x+\frac{\alpha(\alpha-1)}2(1+\theta x)^{\alpha-2}x^2\ \ge\ 1+\alpha x,
```
since the remainder is non-negative for $`\alpha>1`$. With $`x=\frac1k`$:
```math
\frac{b_k}{b_{k+1}}\ge1+\frac\alpha k=1+\frac{1+\gamma}k,\qquad\gamma=\alpha-1>0,
```
for all $`k\in\mathbb N`$. By problem 3.9, 1) the series $`\sum\frac1{k^\alpha}`$ converges. From the right-hand side of (4), by the classical comparison test, $`\sum a_k`$ converges too. $`\blacksquare`$

**Why it works.** A factor $`C_k`$ that is bounded and bounded away from zero does not affect convergence: the series is squeezed between two multiples of the reference $`\sum\frac1{k^\alpha}`$. The threshold $`\alpha=1`$ is exactly the threshold in Raabe's test: the coefficient of $`\frac1k`$ in the ratio $`\frac{b_k}{b_{k+1}}\approx1+\frac\alpha k`$ is $`\alpha`$.

Why can Raabe's test not be applied to $`a_k`$ directly? Because $`\frac{a_k}{a_{k+1}}=\frac{C_k}{C_{k+1}}\bigl(1+\frac1k\bigr)^\alpha`$, and nothing is known about the ratio $`\frac{C_k}{C_{k+1}}`$: it may jump (for example, $`C_k=2+(-1)^k`$ gives the ratios $`3`$ and $`\frac13`$). Ratio-based tests are sensitive to such oscillations, the comparison test is not. The right order of actions: first get rid of $`C_k`$ by comparison, then study the smooth reference.

The result will often be used in this form: if $`a_k=\frac{C_k}{k^\alpha}`$ with $`C_k`$ between two positive constants (in particular, if $`C_k`$ has a positive finite limit), then the series converges exactly when $`\alpha>1`$.

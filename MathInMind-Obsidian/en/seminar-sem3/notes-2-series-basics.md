---
title: "Seminar NM-204. Notes, part 2: basics of series"
lang: en
tags: [mathinmind/en, mathinmind/other]
---
# Seminar notes, part 2: basics of series

[[ru/seminar-sem3/notes-2-series-basics|Русский]] · **English** · [[es/seminar-sem3/notes-2-series-basics|Español]]

[[en/seminar-sem3/notes-1-taylor-extremum|← Part 1: Taylor and extrema]] · [[en/seminar-sem3/index|All homework and notes]] · [[en/seminar-sem3/notes-3-kummer-dalembert-raabe|Part 3: Kummer, d'Alembert, Raabe →]]

> [!note] What this is
> A reworked record of the seminars of 2, 3 and 7 October 2026, based on the transcription in [`sem3_notes`](https://github.com/NikiHunter/matan/blob/main/sem3_notes/README.md). Statement numbers are as on the board. This part collects everything the convergence tests rest on: the definition, three basic facts, the comparison test, Cauchy's root test and the generalised comparison test.

| Date | What was covered | Homework |
|---|---|---|
| 2 Oct | [[#Definition 6.1. Series, partial sums, convergence\|Definition 6.1]], [[#Proposition 6.2. Linearity\|Propositions 6.2–6.4]], [[#Corollary 6.5. Necessary condition for convergence\|necessary condition 6.5]], [[#^ex-6-6\|harmonic series 6.6]] | facts (F1), (F3) of [[en/seminar-sem3/hw3-numerical-series#Three facts everything rests on\|HW 3]] |
| 3 Oct | [[#Proposition 7.1. Convergence criterion for a non-negative series\|non-negative series 7.1]], [[#^ex-7-2\|Examples 7.2–7.4]], [[#Proposition 7.5. The comparison test\|comparison test 7.5]] | (F2), [[en/seminar-sem3/hw3-numerical-series#Problem 3.1\|3.1]], [[en/seminar-sem3/hw3-numerical-series#Problem 3.5\|3.5]] |
| 7 Oct | [[#^ex-8-1\|the sine series 8.1]], [[#Theorem 8.2. Cauchy's (root) test\|Cauchy's test 8.2]], [[#^thm-8-3\|generalised comparison 8.3]] | [[en/seminar-sem3/hw3-numerical-series#Problem 3.3\|3.3]], [[en/seminar-sem3/hw3-numerical-series#Problem 3.4 (generalised comparison test)\|3.4]] |

## Seminar of 2 October: what convergence of a series means

### Definition 6.1. Series, partial sums, convergence

For a sequence $(a_n)$, the **partial sums** of the series $\sum_{n=1}^{\infty}a_n$ are $S_n=a_1+\dots+a_n$. The series **converges** if the finite limit $S=\lim_{n\to\infty}S_n$ exists; $S$ is called the sum of the series. If there is no limit or it is infinite, the series **diverges**.

**Meaning.** A series is not an "infinite sum" but the sequence $(S_n)$. Everything known about limits of sequences carries over to series at once; that is how Propositions 6.2–6.5 are proved.

### Proposition 6.2. Linearity

If $\sum a_n$ and $\sum b_n$ converge and $c\in\mathbb R$, then $\sum(a_n+b_n)$ and $\sum ca_n$ converge, and
$$
\sum(a_n+b_n)=\sum a_n+\sum b_n,\qquad\sum ca_n=c\sum a_n.
$$

**Proof.** $S_n^{(a+b)}=S_n^{(a)}+S_n^{(b)}$ and $S_n^{(ca)}=c\,S_n^{(a)}$; pass to the limit. $\blacksquare$

### Proposition 6.3. Finitely many terms do not affect convergence

For every $N$ the series $\sum_{n\ge1}a_n$ and $\sum_{n\ge N+1}a_n$ converge or diverge together. If they converge, $\sum_{n\ge1}a_n=\sum_{n=1}^Na_n+\sum_{n\ge N+1}a_n$.

**Proof.** Let $\tilde S_m=a_{N+1}+\dots+a_{N+m}$. Then $S_{N+m}=S_N+\tilde S_m$: the two sequences differ by the constant $S_N$. $\blacksquare$

### Proposition 6.4. Cauchy's criterion

The series $\sum a_n$ converges if and only if
$$
\forall\varepsilon>0\ \exists N\ \forall n>N\ \forall p\in\mathbb N:\qquad\Bigl|\sum_{k=n+1}^{n+p}a_k\Bigr|<\varepsilon.
$$

**Proof.** This is Cauchy's criterion for the sequence $(S_n)$, since $S_{n+p}-S_n=\sum_{k=n+1}^{n+p}a_k$. $\blacksquare$

**Meaning.** Convergence is decided by the "tails": every block of the series far from the start is small, whatever its length $p$.

### Corollary 6.5. Necessary condition for convergence

a) If $\sum a_n$ converges, then $a_n\to0$. b) If $a_n\not\to0$ (no limit, or a non-zero limit), the series diverges.

**Proof.** a) $a_n=S_n-S_{n-1}\to S-S=0$. b) This is the contrapositive of a). $\blacksquare$

### Example 6.6. The harmonic series $\sum\frac1n$ diverges

**Solution.** We show that Cauchy's criterion fails for $\varepsilon=\frac12$. For any $N$ take $n=N$ and $p=N$:
$$
\sum_{k=N+1}^{2N}\frac1k\ge N\cdot\frac1{2N}=\frac12,
$$
because each of the $N$ terms is at least $\frac1{2N}$. $\blacksquare$ ^ex-6-6

**Why it works.** Here $a_n=\frac1n\to0$, yet the series diverges: the necessary condition is not sufficient. The terms decrease too slowly — every block $\frac1{N+1}+\dots+\frac1{2N}$ contributes at least $\frac12$, and there are infinitely many such blocks.

## Seminar of 3 October: series with non-negative terms

### Proposition 7.1. Convergence criterion for a non-negative series

If $a_n\ge0$ for all $n$, then $\sum a_n$ converges if and only if its partial sums are bounded above: there is $K$ with $S_n\le K$ for all $n$.

**Proof.** $S_{n+1}=S_n+a_{n+1}\ge S_n$, so $(S_n)$ is non-decreasing. A monotone sequence converges if and only if it is bounded (Weierstrass's theorem). $\blacksquare$

**Why it works.** The partial sums of a non-negative series can only grow. There are exactly two options: the growth hits a ceiling (convergence) or goes to $+\infty$. This is the main tool behind all the tests below: to prove convergence it is enough to bound $S_n$ from above.

### Example 7.2. The telescoping series $\sum\frac1{n(n+1)}=1$

Since $\frac1{n(n+1)}=\frac1n-\frac1{n+1}$,
$$
S_n=\Bigl(1-\frac12\Bigr)+\Bigl(\frac12-\frac13\Bigr)+\dots+\Bigl(\frac1n-\frac1{n+1}\Bigr)=1-\frac1{n+1}\ \longrightarrow\ 1.\qquad\blacksquare
$$

^ex-7-2

This series is the reference series for comparison in [[en/seminar-sem3/hw3-numerical-series#Problem 3.5|Problem 3.5]] and in [[en/seminar-sem3/notes-3-kummer-dalembert-raabe#^ex-9-1|Example 9.1]].

### Proposition 7.3. The geometric series

The series $\sum_{n\ge1}q^n$ converges if and only if $|q|<1$, and then its sum is $\frac q{1-q}$.

**Proof.** For $|q|\ge1$ the general term does not tend to zero: $q^n=1$ for $q=1$, $(-1)^n$ has no limit, and $|q^n|\to\infty$ for $|q|>1$. By Corollary 6.5 the series diverges. For $|q|<1$ we have $qS_n=S_n+q^{n+1}-q$, so
$$
S_n=\frac{q(1-q^n)}{1-q}\ \longrightarrow\ \frac q{1-q},
$$
because $q^n\to0$. $\blacksquare$

**Why it works.** The geometric progression is the main reference series. Cauchy's and d'Alembert's tests essentially compare a series with it: "the terms decrease at least as fast as $q^n$ for some $q<1$".

### Example 7.4. $\sum(-1)^n$: bounded partial sums, yet the series diverges

$S_{2m}=\sum_{l=1}^m\bigl((-1)^{2l-1}+(-1)^{2l}\bigr)=0$ and $S_{2m-1}=S_{2m-2}+(-1)^{2m-1}=-1$. So $|S_n|\le1$, but $(S_n)$ has two partial limits, $0$ and $-1$, and the series diverges. $\blacksquare$ ^ex-7-4

**Why it works.** Proposition 7.1 cannot be applied to series whose terms have different signs: there bounded partial sums do not give convergence. The series $\sum\sin(kx_0)$ and $\sum\cos(kx_0)$ show the same effect ([[en/seminar-sem3/notes-4-examples-tests#^ex-12-3|Example 12.3]], Problems [[en/seminar-sem3/hw3-numerical-series#Problem 3.2|3.2]] and [[en/seminar-sem3/hw3-numerical-series#Problem 3.3|3.3]]).

### Proposition 7.5. The comparison test

Let $0\le p_n\le q_n$ for all $n>N_0$. Then: 1) if $\sum p_n$ diverges, so does $\sum q_n$; 2) if $\sum q_n$ converges, so does $\sum p_n$.

**Proof.** 2) By Proposition 6.3 the tail $\sum_{n\ge1}q_{N_0+n}$ converges, and by Proposition 7.1 its partial sums are bounded by some $K$. Then
$$
\sum_{n=1}^mp_{N_0+n}\le\sum_{n=1}^mq_{N_0+n}\le K,
$$
so the partial sums of the non-negative series $\sum p_{N_0+n}$ are bounded; it converges (7.1), and so does $\sum p_n$ (6.3).
1) This is the contrapositive of item 2: if $\sum q_n$ converged, $\sum p_n$ would converge too. $\blacksquare$

## Seminar of 7 October: the sine series, Cauchy's test, the generalised comparison test

### Example 8.1. $\sum\sin(kx_0)$ converges if and only if $x_0\in\pi\mathbb Z$

**Claim.** For $x_0\in\mathbb R$ the following are equivalent: 1) the series $\sum_{k\ge1}\sin(kx_0)$ converges; 2) $x_0=m\pi$ for some $m\in\mathbb Z$.

^ex-8-1

**Proof.** 2) ⟹ 1). If $x_0=m\pi$, then $kx_0\in\pi\mathbb Z$, all terms vanish and $S_n=0$.

1) ⟹ 2). By contradiction: suppose the series converges but $\sin x_0\ne0$. By the necessary condition $\sin(kx_0)\to0$, hence also $y_k=\sin\bigl((k+1)x_0\bigr)\to0$ (the same sequence without its first term). By the addition formula
$$
y_k=\sin(kx_0)\cos x_0+\cos(kx_0)\sin x_0\quad\Longrightarrow\quad\cos(kx_0)=\frac{y_k-\cos x_0\cdot\sin(kx_0)}{\sin x_0}\ \longrightarrow\ 0.
$$
Then $\sin^2(kx_0)+\cos^2(kx_0)\to0$, while this sum is identically $1$. A contradiction. $\blacksquare$

**Why it works.** If $\sin(kx_0)$ tended to zero, so would the shifted sines, and the cosines are expressed through them. The sine and the cosine of the same angle cannot both be small. The same trick for cosines is in [[en/seminar-sem3/hw3-numerical-series#Problem 3.3|Problem 3.3]].

### Theorem 8.2. Cauchy's (root) test

Let $a_n\ge0$ for $n\ge N_0$.

1. If there is $q\in[0;1)$ such that $\sqrt[n]{a_n}\le q$ for all $n>N_1$ (where $N_1\ge N_0$), then $\sum a_n$ converges.
2. If $\sqrt[n]{a_n}\ge1$ for infinitely many $n$, then $\sum a_n$ diverges.

**Proof.** 1) For $n>N_1$ we have $a_n=\bigl(\sqrt[n]{a_n}\bigr)^n\le q^n$, because $t\mapsto t^n$ is non-decreasing on $[0;+\infty)$. The series $\sum q^n$ converges (7.3), so by the comparison test (7.5) $\sum a_n$ converges.
2) If $\sqrt[n]{a_n}\ge1$, then $a_n\ge1$. There are infinitely many such $n$, so $a_n\not\to0$, and the series diverges by Corollary 6.5. $\blacksquare$

**Why it works.** The inequality $\sqrt[n]{a_n}\le q$ is exactly $a_n\le q^n$: Cauchy's test is comparison with a geometric progression written in a convenient form. In item 2 infinitely many indices are enough because the root bounds the term itself, not the ratio of neighbouring terms. For d'Alembert's test this replacement does not work ([[en/seminar-sem3/notes-3-kummer-dalembert-raabe#^ex-10-4|Example 10.4]]).

### Theorem 8.3. The generalised comparison test (= [[en/seminar-sem3/hw3-numerical-series#Problem 3.4 (generalised comparison test)|Problem 3.4]])

Let $a_n$ and $b_n$ be positive for $n>N_0$ with $\frac{a_{n+1}}{a_n}\le\frac{b_{n+1}}{b_n}$. Then: 1) if $\sum b_n$ converges, so does $\sum a_n$; 2) if $\sum a_n$ diverges, so does $\sum b_n$. ^thm-8-3

**Proof.** Multiply the inequalities for $k=N_0+1,\dots,m$. The products telescope (an induction on the number of factors checks this):
$$
\frac{a_{m+1}}{a_{N_0+1}}=\prod_{k=N_0+1}^{m}\frac{a_{k+1}}{a_k}\le\prod_{k=N_0+1}^{m}\frac{b_{k+1}}{b_k}=\frac{b_{m+1}}{b_{N_0+1}}.
$$
So $a_{m+1}\le C\,b_{m+1}$ for all $m>N_0$, where $C=\frac{a_{N_0+1}}{b_{N_0+1}}>0$ does not depend on $m$.

1) If $\sum b_n$ converges, so does $\sum C\,b_{n+1}$; by the comparison test 7.5, $\sum a_{n+1}$ converges, and with it $\sum a_n$ (6.3).
2) If $\sum a_n$ diverges, so does $\sum\frac1C\,a_{n+1}$, and $\frac1C\,a_{m+1}\le b_{m+1}$; by 7.5, $\sum b_n$ diverges. $\blacksquare$

**Why it works.** The ratio $\frac{a_{n+1}}{a_n}$ is the factor by which the term is multiplied in one step. If $a_n$ decreases at least as fast as $b_n$ at every step, then over many steps $a_n\le Cb_n$, and a constant factor $C$ does not affect convergence. Kummer's, d'Alembert's and Raabe's tests are built on this test ([[en/seminar-sem3/notes-3-kummer-dalembert-raabe|part 3]]).

## What was corrected compared with the OCR transcription

The transcription of these three seminars has almost no errors. Mixed-up indices were fixed ($n$ and $k$ in the proof of 8.2, $n_0$ and $N_0$ in 8.3, $l$ and $k$ in 7.4), and repetitions were cut. The records of 2 and 3 October were made from screenshots of the Zoom board; their content was checked against HW 3 and the lectures.

[[en/seminar-sem3/notes-1-taylor-extremum|← Part 1]] · [[en/seminar-sem3/index|All homework and notes]] · [[en/seminar-sem3/notes-3-kummer-dalembert-raabe|Part 3 →]]

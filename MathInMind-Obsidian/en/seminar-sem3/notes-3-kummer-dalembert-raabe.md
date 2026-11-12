---
title: "Seminar NM-204. Notes, part 3: Kummer's, d'Alembert's and Raabe's tests"
lang: en
tags: [mathinmind/en, mathinmind/other]
---
# Seminar notes, part 3: Kummer's, d'Alembert's and Raabe's tests

[[ru/seminar-sem3/notes-3-kummer-dalembert-raabe|Русский]] · **English** · [[es/seminar-sem3/notes-3-kummer-dalembert-raabe|Español]]

[[en/seminar-sem3/notes-2-series-basics|← Part 2: basics of series]] · [[en/seminar-sem3/index|All homework and notes]] · [[en/seminar-sem3/notes-4-examples-tests|Part 4: examples and comparing the tests →]]

> [!note] What this is
> A reworked record of the seminars of 16, 21 and 28 October 2026, based on the transcription in [`sem3_notes`](https://github.com/NikiHunter/matan/blob/main/sem3_notes/README.md). Statement numbers are as on the board. The record of 14 October is empty (two blank pages) and is not included. The end of the proof of Theorem 12.1, done on 30 October, has been moved here.

| Date | What was covered | Homework |
|---|---|---|
| 16 Oct | [[#^ex-9-1\|$\sum\frac1{k!}$]], [[#The idea of Kummer's test\|Kummer's idea]], [[#Definition 10.1. Eventually positive sequences\|eventually positive sequences]], [[#^thm-10-2\|Kummer's test 10.2]], [[#^cor-10-3\|d'Alembert 10.3]], [[#^ex-10-4\|Example 10.4]] | [[en/seminar-sem3/hw3-numerical-series#Problem 3.5\|3.5]]–[[en/seminar-sem3/hw3-numerical-series#Problem 3.8\|3.8]] |
| 21 Oct | [[#^cor-11-1\|Raabe's test 11.1]], [[#^rem-11-2\|Remark 11.2]], [[#^lem-11-3\|Lemma 11.3]] | [[en/seminar-sem3/hw3-numerical-series#Problem 3.9 (Raabe's test)\|3.9]], [[en/seminar-sem3/hw3-numerical-series#^p-3-10\|3.10]], [[en/seminar-sem3/hw3-numerical-series#Problem 3.1\|3.1]] |
| 28 Oct | [[#^thm-12-1\|series $\sum\frac{c_k}{k^d}$]], [[#Remark 12.2. What to look at for an eventually positive series\|what to look at in the tests]] | [[en/seminar-sem3/hw3-numerical-series#^p-3-11\|3.11]], [[en/seminar-sem3/hw4-series-inequalities-bases#Problem 4.6 (limit forms of the tests)\|4.6]] |

**Seminar notation.** The tests use the ratio $\frac{a_n}{a_{n+1}}$ — the previous term over the next one — rather than the more familiar $\frac{a_{n+1}}{a_n}$. So "the ratio is greater than one" means that the terms decrease.

## Seminar of 16 October: Kummer's and d'Alembert's tests

### Example 9.1. $\sum\frac1{k!}$ converges (= [[en/seminar-sem3/hw3-numerical-series#Problem 3.5|Problem 3.5]], b)

Compare $a_k=\frac1{k!}$ with $b_k=\frac1{k(k+1)}$; the series of $b_k$ converges ([[en/seminar-sem3/notes-2-series-basics#^ex-7-2|Example 7.2]]).
$$
\frac{a_{k+1}}{a_k}=\frac1{k+1},\qquad\frac{b_{k+1}}{b_k}=\frac{k}{k+2}.
$$
The inequality $\frac1{k+1}\le\frac k{k+2}$ is equivalent to $\frac{k^2-2}{(k+1)(k+2)}\ge0$, that is, $k^2\ge2$; it holds for $k\ge2$. By the generalised comparison test ([[en/seminar-sem3/notes-2-series-basics#^thm-8-3|Theorem 8.3]]) the series $\sum\frac1{k!}$ converges. $\blacksquare$ ^ex-9-1

**Why it works.** The ratio of neighbouring terms of the factorial series, $\frac1{k+1}$, tends to zero, while for the reference series $\frac k{k+2}$ tends to one: at every step the factorial series decreases faster. Comparing ratios is easier than comparing the terms themselves. That the inequality fails for $k=1$ does not matter: the test only needs it from some index on.

### The idea of Kummer's test

Let $x_n>0$ and, for large $n$,
$$
x_n\frac{a_n}{a_{n+1}}-x_{n+1}\ge d>0.
$$
Multiply by $a_{n+1}>0$: $x_na_n-x_{n+1}a_{n+1}\ge d\,a_{n+1}$. Add these inequalities for $n=n_0+1,\dots,m$. On the left the sum telescopes:
$$
d\sum_{n=n_0+1}^{m}a_{n+1}\le x_{n_0+1}a_{n_0+1}-x_{m+1}a_{m+1}\le x_{n_0+1}a_{n_0+1}.
$$
The partial sums are bounded, so the series converges ([[en/seminar-sem3/notes-2-series-basics#Proposition 7.1. Convergence criterion for a non-negative series|Proposition 7.1]]).

### Definition 10.1. Eventually positive sequences

A sequence $(a_n)$ is **eventually positive from index $N_0$** if $a_n>0$ for all $n>N_0$, and simply **eventually positive** if this holds for some $N_0$.

**Connection with bases.** "From some index on" is the same as "on some element of the base $n\to\infty$". The base on $\mathbb N$ is the family $\{M_k\}$ with $M_k=\{m\in\mathbb N:\ m>k\}$; this is the family $\mathcal M_2$ of [[en/seminar-sem3/hw4-series-inequalities-bases#Problem 4.3 (bases of sets)|Problem 4.3]].

### Theorem 10.2. Kummer's test (= [[en/seminar-sem3/hw3-numerical-series#Problem 3.6 (Kummer's test)|Problem 3.6]])

Let $x_n>0$ for all $n$, and let $(a_n)$ be eventually positive from index $N_0$. ^thm-10-2

1. If there are $d>0$ and $N_1\ge N_0$ such that $x_n\frac{a_n}{a_{n+1}}-x_{n+1}\ge d$ for all $n>N_1$, then $\sum a_n$ converges.
2. If the series $\sum\frac1{x_n}$ diverges and $x_n\frac{a_n}{a_{n+1}}-x_{n+1}\le0$ for all $n>N_2$ (where $N_2\ge N_0$), then $\sum a_n$ diverges.

**Proof of item 1.** For $n>N_1$ multiply the inequality by $a_{n+1}>0$:
$$
x_na_n-x_{n+1}a_{n+1}\ge d\,a_{n+1}.\tag{*}
$$
Add $(*)$ for $n=N_1+1,\dots,N_1+k$. The left-hand side telescopes:
$$
d\sum_{l=1}^{k}a_{N_1+1+l}\le x_{N_1+1}a_{N_1+1}-x_{N_1+k+1}a_{N_1+k+1}<x_{N_1+1}a_{N_1+1},
$$
because the subtracted term is positive. Hence for every $k$
$$
\sum_{l=1}^{k}a_{N_1+1+l}<\frac{x_{N_1+1}\,a_{N_1+1}}{d},
$$
and the right-hand side does not depend on $k$. The partial sums of the positive series $\sum_l a_{N_1+1+l}$ are bounded, so it converges (7.1), and with it $\sum a_n$ (6.3).

**Proof of item 2.** For $n>N_2$ the hypothesis gives $x_n\frac{a_n}{a_{n+1}}\le x_{n+1}$, that is,
$$
\frac{a_{n+1}}{a_n}\ge\frac{x_n}{x_{n+1}}=\frac{1/x_{n+1}}{1/x_n}.
$$
This is the hypothesis of [[en/seminar-sem3/notes-2-series-basics#^thm-8-3|Theorem 8.3]] for the pair in which $\frac1{x_n}$ plays the role of "$a$" and $a_n$ the role of "$b$". The series $\sum\frac1{x_n}$ diverges, so $\sum a_n$ diverges. $\blacksquare$

**Why it works.** The quantity $x_na_n$ is a "weighted" term of the series. In item 1 it decreases at every step by at least $d\,a_{n+1}$ but stays positive. So all the decreases together are at most its initial value: the series "pays" for its terms out of a finite budget. In item 2 the weighted term does not decrease, so $a_n\ge\frac{\mathrm{const}}{x_n}$, and the series is at least the divergent $\sum\frac1{x_n}$. Each sequence $(x_n)$ gives its own test: $x_n=1$ gives d'Alembert ([[#^cor-10-3|10.3]]), $x_n=n$ gives Raabe ([[#^cor-11-1|11.1]]).

### Corollary 10.3. D'Alembert's test (= [[en/seminar-sem3/hw3-numerical-series#Problem 3.7 (d'Alembert's test)|Problem 3.7]])

Let $(a_n)$ be eventually positive from index $N_0$. ^cor-10-3

1. If there are $\beta>0$ and $N_1\ge N_0$ such that $\frac{a_n}{a_{n+1}}\ge1+\beta$ for all $n>N_1$, then $\sum a_n$ converges.
2. If $\frac{a_n}{a_{n+1}}\le1$ for all $n>N_2$ (where $N_2\ge N_0$), then $\sum a_n$ diverges.

**Proof.** Kummer's test with $x_n=1$: then $x_n\frac{a_n}{a_{n+1}}-x_{n+1}=\frac{a_n}{a_{n+1}}-1$. In item 1 this quantity is at least $\beta$; take $d=\beta$. In item 2 it is $\le0$, and the series $\sum\frac1{x_n}=\sum1$ diverges: its partial sums $S_n=n$ are unbounded. $\blacksquare$

**Important.** In item 2 the inequality $\frac{a_n}{a_{n+1}}\le1$ must hold for **all** $n$ from some index on. Infinitely many indices are not enough, as [[#^ex-10-4|Example 10.4]] shows.

### Example 10.4. Cauchy's test works, d'Alembert's does not (= [[en/seminar-sem3/hw3-numerical-series#Problem 3.8|Problem 3.8]])

$$
a_k=\begin{cases}2^{-k}, & k\ \text{odd},\\ 3^{-k}, & k\ \text{even}.\end{cases}
$$

^ex-10-4

1) **The series converges.** $\sqrt[k]{a_k}$ equals $\frac12$ for odd $k$ and $\frac13$ for even $k$, so $\sqrt[k]{a_k}\le\frac12$ for all $k$. By Cauchy's test ([[en/seminar-sem3/notes-2-series-basics#Theorem 8.2. Cauchy's (root) test|Theorem 8.2]]) with $q=\frac12$ the series converges.

2) **D'Alembert's test does not apply.** For all $m\in\mathbb N$
$$
\frac{a_{2m}}{a_{2m+1}}=\frac{2^{2m+1}}{3^{2m}}=2\Bigl(\frac23\Bigr)^{2m}\le\frac89<1,\qquad\frac{a_{2m-1}}{a_{2m}}=\frac{3^{2m}}{2^{2m-1}}=2\Bigl(\frac32\Bigr)^{2m}\ge\frac92.
$$
So the set $\bigl\{k:\ \frac{a_k}{a_{k+1}}\le1\bigr\}$ contains all even numbers and $\bigl\{k:\ \frac{a_k}{a_{k+1}}\ge\frac92\bigr\}$ all odd ones; both are infinite. Neither condition of d'Alembert's test holds for all $n$ from some index on. $\blacksquare$

**Why it works.** The series is two geometric progressions interleaved. Stepping from the "slow" progression to the "fast" one gives a large ratio, the step back makes the term grow. D'Alembert looks at one step and sees contradictory signals. Cauchy bounds the term itself and sees that all terms are at most $2^{-k}$.

## Seminar of 21 October: Raabe's test

### Corollary 11.1. Raabe's test (= [[en/seminar-sem3/hw3-numerical-series#Problem 3.9 (Raabe's test)|Problem 3.9]])

Let $(a_n)$ be eventually positive from index $N_0$. ^cor-11-1

1. If there are $\delta>0$ and $N_1\ge N_0$ such that $\frac{a_n}{a_{n+1}}\ge1+\frac{1+\delta}n$ for all $n>N_1$, then $\sum a_n$ converges.
2. If $\frac{a_n}{a_{n+1}}\le1+\frac1n$ for all $n>N_2$ (where $N_2\ge N_0$), then $\sum a_n$ diverges.

**Proof.** Kummer's test with $x_n=n$. The series $\sum\frac1{x_n}=\sum\frac1n$ diverges ([[en/seminar-sem3/notes-2-series-basics#^ex-6-6|Example 6.6]]), and
$$
x_n\frac{a_n}{a_{n+1}}-x_{n+1}=n\frac{a_n}{a_{n+1}}-(n+1)=n\Bigl(\frac{a_n}{a_{n+1}}-1-\frac1n\Bigr).
$$
1) For $n>N_1$ this is at least $n\cdot\frac\delta n=\delta$; take $d=\delta$. 2) For $n>N_2$ it is $\le0$. $\blacksquare$

**Why it works.** Here the ratio $\frac{a_n}{a_{n+1}}$ may tend to $1$; what matters is how fast. The reference series are $\sum\frac1{n^p}$, for which $\frac{a_n}{a_{n+1}}=\bigl(1+\frac1n\bigr)^p\approx1+\frac pn$. Raabe's test reads off the coefficient of $\frac1n$: greater than one with a margin means convergence, at most one means divergence.

**An example from the seminar: d'Alembert is silent, Raabe answers.** Let $a_1=1$ and $a_{n+1}=\frac{2n}{2n+1}a_n$, so $\frac{a_n}{a_{n+1}}=1+\frac1{2n}$. D'Alembert's divergence condition $\frac{a_n}{a_{n+1}}\le1$ fails for every $n$, and the convergence condition with a constant $\beta>0$ fails for large $n$. Raabe's condition 2 holds: $1+\frac1{2n}\le1+\frac1n$, so the series diverges. (In fact $a_n\sqrt n\to\frac{\sqrt\pi}2$, so $a_n$ behaves like $\frac{\mathrm{const}}{\sqrt n}$.) A similar series is $b_k$ in [[en/seminar-sem3/hw4-series-inequalities-bases#Problem 4.9|Problem 4.9]].

### Remark 11.2. "For infinitely many $n$" is not enough for Raabe either (= [[en/seminar-sem3/hw3-numerical-series#^p-3-10|Problem 3.10]])

Take the series of [[#^ex-10-4|Example 10.4]]. It converges, but the set $\bigl\{k:\ \frac{a_k}{a_{k+1}}\le1\bigr\}$ is infinite. This set lies inside $\bigl\{k:\ \frac{a_k}{a_{k+1}}\le1+\frac1k\bigr\}$, because $1<1+\frac1k$. So the second set is infinite too, hence countable as an infinite subset of $\mathbb N$. Thus the bound of condition 2 of Raabe's test holds for infinitely many indices, yet the series converges. $\blacksquare$ ^rem-11-2

**Why it works.** Divergence conditions in ratio-based tests must hold for all sufficiently large $n$: one step up does not prevent the series from decreasing overall. Cauchy's test is different — infinitely many indices suffice there ([[en/seminar-sem3/notes-2-series-basics#Theorem 8.2. Cauchy's (root) test|Theorem 8.2]], item 2).

### Lemma 11.3. A convergent series has bounded partial sums (= [[en/seminar-sem3/hw3-numerical-series#Problem 3.1|Problem 3.1]])

If $\sum a_n$ converges, then $(S_n)$ is a convergent sequence, and every convergent sequence is bounded. $\blacksquare$ ^lem-11-3

The converse is false: [[en/seminar-sem3/notes-2-series-basics#^ex-7-4|Example 7.4]].

## Seminar of 28 October: series of the form $\sum\frac{c_k}{k^d}$

### Theorem 12.1. When $\sum\frac{c_k}{k^d}$ converges (= [[en/seminar-sem3/hw3-numerical-series#^p-3-11|Problem 3.11]])

Let $d\in\mathbb R$, and let the numbers $c_k$ lie between two positive constants: $0<M_1\le c_k\le M_2$ for all $k$. Then the series $\sum_{k\ge1}\frac{c_k}{k^d}$ converges if and only if $d>1$.

^thm-12-1

**Proof.** Write $a_k=\frac{c_k}{k^d}$.

*Case $d\le0$.* Then $k^{-d}\ge1$ and $a_k\ge c_k\ge M_1>0$. The general term does not tend to zero; the series diverges (6.5).

*Case $0<d\le1$.* Then $k^d\le k$ and $a_k\ge\frac{M_1}{k^d}\ge\frac{M_1}k$. The series $\sum\frac{M_1}k$ diverges (the harmonic series times $M_1\ne0$), so by the comparison test $\sum a_k$ diverges.

*Case $d>1$.* Compare with $b_k=\frac{M_2}{k^d}\ge a_k$ and prove that $\sum b_k$ converges by Raabe's test. The ratio is
$$
\frac{b_k}{b_{k+1}}=\Bigl(1+\frac1k\Bigr)^d.
$$
By Taylor's formula with the Peano remainder for $\varphi(x)=(1+x)^d$ there is a sequence $x_k\to0$ with
$$
\Bigl(1+\frac1k\Bigr)^d=1+\frac dk+\frac{d(d-1)}{2k^2}+\frac{x_k}{k^2},\qquad k\Bigl(\frac{b_k}{b_{k+1}}-1\Bigr)=d+\frac1k\Bigl(\frac{d(d-1)}2+x_k\Bigr).
$$
Since $x_k\to0$ and $\frac{d(d-1)}2>0$, for large $k$ (when $|x_k|<\frac{d(d-1)}4$) the bracket is positive, and
$$
\frac{b_k}{b_{k+1}}\ge1+\frac dk=1+\frac{1+(d-1)}k.
$$
This is condition 1 of Raabe's test with $\delta=d-1>0$. The series $\sum b_k$ converges, and since $0<a_k\le b_k$, so does $\sum a_k$. $\blacksquare$

**Shorter, via Bernoulli's inequality.** For $d>1$ and $x>0$ we have $(1+x)^d\ge1+dx$, which gives $\frac{b_k}{b_{k+1}}\ge1+\frac dk$ for all $k$ at once. This is how [[en/seminar-sem3/hw3-numerical-series#^p-3-11|Problem 3.11]] does it.

**Why it works.** A factor $c_k$ squeezed between positive constants does not affect convergence: the series is squeezed between $M_1\sum\frac1{k^d}$ and $M_2\sum\frac1{k^d}$. So one first removes $c_k$ with the comparison test and only then applies Raabe to a smooth reference series. Applying Raabe directly to $a_k$ does not work: the ratio $\frac{c_k}{c_{k+1}}$ can jump around (for example, for $c_k=2+(-1)^k$). The first attempt at the seminar went exactly that way and was dropped in favour of comparison with $b_k$.

### Remark 12.2. What to look at for an eventually positive series

| Test | Quantity | Converges if, from some index on | Diverges if |
|---|---|---|---|
| Cauchy ([[en/seminar-sem3/notes-2-series-basics#Theorem 8.2. Cauchy's (root) test\|8.2]]) | $\sqrt[k]{a_k}$ | $\sqrt[k]{a_k}\le q<1$ | $\sqrt[k]{a_k}\ge1$ for infinitely many $k$ |
| d'Alembert ([[#^cor-10-3\|10.3]]) | $\frac{a_k}{a_{k+1}}$ | $\frac{a_k}{a_{k+1}}\ge1+\beta$, $\beta>0$ | $\frac{a_k}{a_{k+1}}\le1$ from some index on |
| Raabe ([[#^cor-11-1\|11.1]]) | $k\bigl(\frac{a_k}{a_{k+1}}-1\bigr)$ | $k\bigl(\frac{a_k}{a_{k+1}}-1\bigr)\ge1+\delta$, $\delta>0$ | $k\bigl(\frac{a_k}{a_{k+1}}-1\bigr)\le1$ from some index on |

The limits of these quantities give the limit forms of the tests: [[en/seminar-sem3/notes-4-examples-tests#^prop-14-3|Proposition 14.3]].

## What was corrected compared with the OCR transcription

| Place | In the transcription | Correct |
|---|---|---|
| [[#^cor-10-3\|10.3]], note | "in condition 2) it is enough that the bound holds for infinitely many terms" | not enough: the bound is needed for all $n$ from some index on ([[#^ex-10-4\|Example 10.4]]) |
| [[#^cor-10-3\|10.3]], proof of item 2 | the index $N_1$ | $N_2$ |
| [[#^cor-11-1\|11.1]], example | $a_{k+1}=\frac{2n}{2n+1}a_k$ | $a_{n+1}=\frac{2n}{2n+1}a_n$ |
| [[#^rem-11-2\|11.2]] | a reference to "Example 7.4" | [[#^ex-10-4\|Example 10.4]] |
| [[#^thm-12-1\|12.1]], case $d>1$ | an unfinished attempt to bound $k\bigl(\frac{a_k}{a_{k+1}}-1\bigr)$ directly, then the same proof again on 30 October | one proof via $b_k=\frac{M_2}{k^d}$ is kept |

[[en/seminar-sem3/notes-2-series-basics|← Part 2]] · [[en/seminar-sem3/index|All homework and notes]] · [[en/seminar-sem3/notes-4-examples-tests|Part 4 →]]

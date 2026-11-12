---
title: "Seminar NM-204. Notes, part 4: examples and comparing the tests"
lang: en
tags: [mathinmind/en, mathinmind/other]
---
# Seminar notes, part 4: examples and comparing the tests

[[ru/seminar-sem3/notes-4-examples-tests|Русский]] · **English** · [[es/seminar-sem3/notes-4-examples-tests|Español]]

[[en/seminar-sem3/notes-3-kummer-dalembert-raabe|← Part 3: Kummer, d'Alembert, Raabe]] · [[en/seminar-sem3/index|All homework and notes]] · [[en/seminar-sem3/test1-guide|How to prepare for the test →]]

> [!note] What this is
> A reworked record of the seminars of 28 and 30 October and 11 November 2026, based on the transcription in [`sem3_notes`](https://github.com/NikiHunter/matan/blob/main/sem3_notes/README.md). Statement numbers are as on the board. Example 12.3 was started on 28 October and finished on 30 October; here it is in one piece. At the end there is a summary of which test is stronger; it replaces an incorrect conclusion in the transcription.

| Date | What was covered | Homework |
|---|---|---|
| 28 Oct, 30 Oct | [[#^ex-12-3\|sums of sines 12.3]], [[#^ex-12-4\|sums of cosines 12.4]] | [[en/seminar-sem3/hw3-numerical-series#Problem 3.2\|3.2]], [[en/seminar-sem3/hw3-numerical-series#Problem 3.3\|3.3]] |
| 30 Oct | [[#^ex-13-1\|$\sum\frac{\beta^kk!}{k^k}$]], [[#^ex-13-2\|$\sum\frac{\sqrt{k+1}-\sqrt{k-1}}{k^d}$]] | [[en/seminar-sem3/hw4-series-inequalities-bases#Problem 4.8\|4.8]] |
| 11 Nov | [[#^ex-14-1\|a series with $c_k\to1$]], [[#^rem-14-2\|Raabe ⟹ d'Alembert]], [[#^prop-14-3\|limit forms]] | [[en/seminar-sem3/hw4-series-inequalities-bases#Problem 4.7\|4.7]], [[en/seminar-sem3/hw4-series-inequalities-bases#Problem 4.4\|4.4]], [[en/seminar-sem3/hw4-series-inequalities-bases#Problem 4.6 (limit forms of the tests)\|4.6]] |

## Seminars of 28 and 30 October: trigonometric sums

### Example 12.3. The partial sums of $\sum\sin(kx_0)$ are bounded (= [[en/seminar-sem3/hw3-numerical-series#Problem 3.2|Problem 3.2]])

**Claim.** For every $x_0\in\mathbb R$ the sequence $S_n=\sum_{k=1}^n\sin(kx_0)$ is bounded, although the series itself converges only for $x_0\in\pi\mathbb Z$ ([[en/seminar-sem3/notes-2-series-basics#^ex-8-1|Example 8.1]]).

^ex-12-3

**Proof.** *Case $x_0\in2\pi\mathbb Z$.* All terms vanish, $S_n=0$.

*Case $x_0\notin2\pi\mathbb Z$.* Then $\frac{x_0}2\notin\pi\mathbb Z$ and $\sin\frac{x_0}2\ne0$. By $\sin\alpha\sin\beta=\frac12\bigl(\cos(\alpha-\beta)-\cos(\alpha+\beta)\bigr)$,
$$
\sin(kx_0)\,\sin\frac{x_0}2=\frac12\Bigl(\cos\bigl((k-\tfrac12)x_0\bigr)-\cos\bigl((k+\tfrac12)x_0\bigr)\Bigr).
$$
The sum over $k=1,\dots,n$ telescopes. By induction: going from $n$ to $n+1$ adds $\cos\bigl((n+\frac12)x_0\bigr)-\cos\bigl((n+\frac32)x_0\bigr)$, and $\cos\bigl((n+\frac12)x_0\bigr)$ cancels. The result is
$$
S_n\sin\frac{x_0}2=\frac12\Bigl(\cos\frac{x_0}2-\cos\bigl((n+\tfrac12)x_0\bigr)\Bigr).
$$
Divide by $\sin\frac{x_0}2\ne0$ and bound the numerator by the triangle inequality:
$$
|S_n|=\frac{\bigl|\cos\frac{x_0}2-\cos\bigl((n+\frac12)x_0\bigr)\bigr|}{2\bigl|\sin\frac{x_0}2\bigr|}\le\frac{1+1}{2\bigl|\sin\frac{x_0}2\bigr|}=\frac1{\bigl|\sin\frac{x_0}2\bigr|}.
$$
The bound does not depend on $n$. $\blacksquare$

**Why it works.** Multiplying by $\sin\frac{x_0}2$ turns every term into a difference of neighbouring values of one sequence, and the sum "collapses". Geometrically, the vectors $(\cos kx_0;\sin kx_0)$ turn by the angle $x_0$ each time, and their sum stays in a bounded region. For $x_0\notin\pi\mathbb Z$ the series still diverges: the sum does not settle down but keeps wandering through a bounded set.

### Example 12.4. The partial sums of $\sum\cos(kx_0)$ (cf. [[en/seminar-sem3/hw3-numerical-series#Problem 3.3|Problem 3.3]])

> The statement of Example 12.4 did not survive in the record; only a comment on it from 30 October did. By its content it is Problem 3.3.

^ex-12-4

The identity from the seminar: $2\sin\frac{x_0}2\cos(kx_0)=\sin\bigl((k+\frac12)x_0\bigr)-\sin\bigl((k-\frac12)x_0\bigr)$. After telescoping (induction, as above)
$$
2\sin\frac{x_0}2\sum_{k=1}^n\cos(kx_0)=\sin\bigl((n+\tfrac12)x_0\bigr)-\sin\frac{x_0}2.
$$
So for $x_0\notin2\pi\mathbb Z$ the partial sums are bounded by $\frac1{|\sin(x_0/2)|}$, while for $x_0\in2\pi\mathbb Z$ all terms equal $1$ and $S_n=n$ is unbounded. The series itself diverges for every $x_0$, because $\cos(kx_0)\not\to0$ ([[en/seminar-sem3/hw3-numerical-series#Problem 3.3|Problem 3.3]]).

## Seminar of 30 October: two series with a parameter (Problem 4.8)

### Example 13.1. $\sum\frac{\beta^kk!}{k^k}$ converges for $\beta<e$ and diverges for $\beta\ge e$

Let $\beta>0$ and $b_k=\frac{\beta^kk!}{k^k}>0$. The ratio is
$$
\frac{b_k}{b_{k+1}}=\frac{\beta^kk!}{k^k}\cdot\frac{(k+1)^{k+1}}{\beta^{k+1}(k+1)!}=\frac1\beta\Bigl(1+\frac1k\Bigr)^k=:c_k\ \xrightarrow[k\to\infty]{}\ \frac e\beta.
$$

^ex-13-1

*Case $\beta<e$.* The limit is $\frac e\beta>1$. Take $\varepsilon=\frac{e-\beta}{2\beta}$; for large $k$
$$
c_k>\frac e\beta-\varepsilon=\frac{e+\beta}{2\beta}=1+\frac{e-\beta}{2\beta}.
$$
D'Alembert's convergence condition ([[en/seminar-sem3/notes-3-kummer-dalembert-raabe#^cor-10-3|Corollary 10.3]]) holds with the constant $\frac{e-\beta}{2\beta}>0$.

*Case $\beta\ge e$.* The sequence $\bigl(1+\frac1k\bigr)^k$ increases strictly to $e$ (first semester), so $\bigl(1+\frac1k\bigr)^k<e$ for all $k$ and $c_k<\frac e\beta\le1$. D'Alembert's divergence condition holds for every $k$. $\blacksquare$

**Why it works.** By Stirling's formula $b_k\approx\sqrt{2\pi k}\,\bigl(\frac\beta e\bigr)^k$ — almost a geometric progression with ratio $\frac\beta e$, hence the threshold $\beta=e$. At the threshold itself the limit of the ratio is $1$ and the limit form of the test fails. The non-limit form works: $c_k<1$ exactly, so the terms grow and do not tend to zero.

### Example 13.2. $\sum\frac{\sqrt{k+1}-\sqrt{k-1}}{k^d}$ converges if and only if $d>\frac12$

Multiply by the conjugate:
$$
a_k=\frac{\sqrt{k+1}-\sqrt{k-1}}{k^d}=\frac{2}{\bigl(\sqrt{k+1}+\sqrt{k-1}\bigr)\,k^d}.
$$
*Upper bound:* $\sqrt{k+1}+\sqrt{k-1}\ge\sqrt{k+1}>\sqrt k$, so $a_k<\frac2{k^{d+1/2}}$.
*Lower bound:* the inequality $\frac{\sqrt p+\sqrt q}2\le\sqrt{\frac{p+q}2}$ (equivalent to $\bigl(\frac{\sqrt p-\sqrt q}2\bigr)^2\ge0$) gives $\sqrt{k+1}+\sqrt{k-1}\le2\sqrt k$, so $a_k\ge\frac1{k^{d+1/2}}$.

^ex-13-2

Hence $a_k=\frac{d_k}{k^{d+1/2}}$ with $1\le d_k<2$, and by [[en/seminar-sem3/notes-3-kummer-dalembert-raabe#^thm-12-1|Theorem 12.1]] the series converges if and only if $d+\frac12>1$, that is, $d>\frac12$. $\blacksquare$

**Why it works.** Each root is of order $\sqrt k$, while their difference is of order $\frac1{\sqrt k}$: it is the increment of $\sqrt x$ over an interval of length $2$, roughly $2\cdot\frac1{2\sqrt k}$. Multiplying by the conjugate makes this order explicit. At the seminar the comparison test was first applied twice (from below and from above), and then it was noted that Theorem 12.1 gives the answer at once.

## Seminar of 11 November: comparing the tests

### Example 14.1. $\sum\frac{k^{k+1/k}}{(k+1/k)^k}$ diverges (= [[en/seminar-sem3/hw4-series-inequalities-bases#Problem 4.7|Problem 4.7]], 3)

$$
c_k=\frac{k^{k+\frac1k}}{\bigl(k+\frac1k\bigr)^k}=\frac{k^k\cdot k^{1/k}}{k^k\bigl(1+\frac1{k^2}\bigr)^k}=\frac{k^{1/k}}{\bigl(1+\frac1{k^2}\bigr)^k}\ \longrightarrow\ \frac11=1,
$$
because $k^{1/k}\to1$ and $1\le\bigl(1+\frac1{k^2}\bigr)^k\le e^{1/k}\to1$. The general term does not tend to zero, so the series diverges ([[en/seminar-sem3/notes-2-series-basics#Corollary 6.5. Necessary condition for convergence|Corollary 6.5]]). $\blacksquare$ ^ex-14-1

> [!note] How the board was deciphered
> The OCR transcription read the exponent $\frac1k$ as $\frac72$ and the answer "$\lim c_k=\frac11=1$" as "$\frac77=1$". With $\frac72$ the computation does not work out (it gives $c_k\to+\infty$), while with $\frac1k$ everything is consistent and matches Problem 4.7, 3) of HW 4.

**Why it works.** The numerator and the denominator are huge but almost equal: $k+\frac1k$ differs from $k$ by the factor $1+\frac1{k^2}$, and after raising to the power $k$ what is left is a factor tending to $1$.

### Remark 14.2. Raabe's test implies d'Alembert's (= [[en/seminar-sem3/hw4-series-inequalities-bases#Problem 4.4|Problem 4.4]])

Let $(a_n)$ be eventually positive. ^rem-14-2

1) Suppose $\frac{a_n}{a_{n+1}}\ge1+\beta$ for $n>N_1$. Take, say, $\delta=5$. Since $\frac6n\to0$, there is $N_2$ after which $\frac6n<\beta$. Then for $n>\max(N_1,N_2)$
$$
\frac{a_n}{a_{n+1}}\ge1+\beta>1+\frac6n=1+\frac{1+\delta}n,
$$
condition 1 of Raabe's test holds, and the series converges.

2) Suppose $\frac{a_n}{a_{n+1}}\le1$ for $n>N_4$. Then all the more $\frac{a_n}{a_{n+1}}\le1+\frac1n$, condition 2 of Raabe's test holds, and the series diverges. $\blacksquare$

**Why it works.** D'Alembert requires a constant gap $\beta$ between the ratio and one, Raabe a gap $\frac{1+\delta}n$ that itself tends to zero. A constant gap sooner or later exceeds any $\frac cn$, so everything d'Alembert decides, Raabe decides too. The converse is false: for $\sum\frac1{n^2}$ d'Alembert is silent and Raabe gives convergence.

### Proposition 14.3. Limit forms of the tests (= [[en/seminar-sem3/hw4-series-inequalities-bases#Problem 4.6 (limit forms of the tests)|Problem 4.6]])

Let $(a_k)$ be eventually positive from index $N_0$. Put $C_k=D_k=R_k=0$ for $k\le N_0$ and
$$
C_k=\sqrt[k]{a_k},\qquad D_k=\frac{a_k}{a_{k+1}},\qquad R_k=k\Bigl(\frac{a_k}{a_{k+1}}-1\Bigr)\qquad\text{for }k>N_0.
$$
The values for $k\le N_0$ do not matter; they are set to zero so that the sequences are defined for all $k$. ^prop-14-3

| If | then $\sum a_k$ | Why |
|---|---|---|
| $C_k\to L<1$ | converges | from some index on $C_k\le\frac{1+L}2<1$; Cauchy's test |
| $C_k\to L>1$ | diverges | from some index on $a_k>1$; the general term does not tend to zero |
| $D_k\to L>1$ | converges | from some index on $D_k\ge1+\frac{L-1}2$; d'Alembert |
| $D_k\to L<1$ | diverges | from some index on $D_k<1$; d'Alembert |
| $R_k\to L>1$ | converges | from some index on $R_k\ge1+\frac{L-1}2$; Raabe |
| $R_k\to L<1$ | diverges | from some index on $R_k<1$; Raabe |

> [!note] About the record
> Of this proposition the OCR transcription kept only the definitions of $C_k$, $D_k$, $R_k$; after that the transcriber added a conclusion of their own about a "hierarchy Cauchy ⟹ d'Alembert ⟹ Raabe", which is wrong as stated. The six items have been restored from Problem 4.6 of HW 4, which introduces the same notation. Full proofs are in [[en/seminar-sem3/hw4-series-inequalities-bases#Problem 4.6 (limit forms of the tests)|Problem 4.6]].

For $L=1$ all three limit forms are silent. For $\sum\frac1k$ and $\sum\frac1{k^2}$ we have $C_k\to1$ and $D_k\to1$, and for $\sum\frac1{k\ln k}$ and $\sum\frac1{k\ln^2k}$ we have $R_k\to1$; in each pair one series diverges and the other converges.

### How the tests compare

This is not a record of the board but a summary; it replaces the incorrect conclusion of the transcription.

- **Raabe is stronger than d'Alembert** ([[#^rem-14-2|Remark 14.2]]): whenever d'Alembert's condition holds, so does Raabe's. The converse is false: for $\sum\frac1{k^2}$, $D_k\to1$ while $R_k\to2$.
- **Cauchy is stronger than d'Alembert for convergence.** If $\frac{a_n}{a_{n+1}}\ge1+\beta$ for $n>N$, then $a_n\le Cq^n$ with $q=\frac1{1+\beta}$, and $\sqrt[n]{a_n}\le C^{1/n}q\to q<1$. The converse is false: in [[en/seminar-sem3/notes-3-kummer-dalembert-raabe#^ex-10-4|Example 10.4]] Cauchy works and d'Alembert does not. In limit form: if $D_k\to L>0$, then $C_k\to\frac1L$.
- **Cauchy and Raabe are incomparable.** In Example 10.4 Cauchy gives convergence, while $R_k$ jumps between negative and very large values and Raabe is silent. For $\sum\frac1{k^2}$ it is the other way round: $C_k=k^{-2/k}\to1$, Cauchy is silent, and Raabe gives convergence.
- **None of the three is universal.** Series with $R_k\to1$, such as $\sum\frac1{k\ln k}$ and $\sum\frac1{k\ln^2k}$, are settled by Kummer's test with $x_n=n\ln n$ (Bertrand's test) or by the integral test ([[en/seminar-sem3/hw4-series-inequalities-bases#Problem 4.10 (Cauchy's integral test)|Problem 4.10]]).

In short: d'Alembert's is the weakest; Cauchy's and Raabe's tests decide everything it decides plus a class of series of their own, but neither replaces the other.

## What was corrected compared with the OCR transcription

| Place | In the transcription | Correct |
|---|---|---|
| [[#^ex-12-3\|12.3]] | the second case first "$x_0\notin2\pi\mathbb Z$", then "$x_0\notin\pi\mathbb Z$, hence $\frac{x_0}2\notin\frac\pi2\mathbb Z$" | exactly the case $x_0\notin2\pi\mathbb Z$ is needed: then $\frac{x_0}2\notin\pi\mathbb Z$ and $\sin\frac{x_0}2\ne0$ |
| [[#^ex-12-3\|12.3]] | the proof is split between 28 and 30 October and partly repeated | merged into one |
| [[#^ex-13-1\|13.1]] | a reference "d'Alembert's test (§3.4)" | [[en/seminar-sem3/notes-3-kummer-dalembert-raabe#^cor-10-3\|Corollary 10.3]], Problem 3.7 |
| [[#^ex-13-2\|13.2]] | $2(\sqrt{k+1}+\sqrt{k-1})\le2\sqrt k$ | $\sqrt{k+1}+\sqrt{k-1}\le2\sqrt k$ |
| [[#^ex-14-1\|14.1]] | $c_k=\frac{k^{k+7/2}}{(k+7/2)^k}$, "$\lim c_k=\frac77=1$" and long attempts to recompute | $c_k=\frac{k^{k+1/k}}{(k+1/k)^k}$, $\lim c_k=\frac11=1$ |
| [[#^prop-14-3\|14.3]] | the conclusion "Cauchy ⟹ d'Alembert ⟹ Raabe, each next one finer" | see the [[#How the tests compare\|summary]]: d'Alembert is weaker than both, Cauchy and Raabe are incomparable |

[[en/seminar-sem3/notes-3-kummer-dalembert-raabe|← Part 3]] · [[en/seminar-sem3/index|All homework and notes]] · [[en/seminar-sem3/test1-guide|How to prepare for the test →]]

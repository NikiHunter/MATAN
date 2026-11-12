---
title: "Seminar NM-204. Test 1 — how to prepare"
lang: en
tags: [mathinmind/en, mathinmind/other]
---
# Test 1: how to prepare

[[ru/seminar-sem3/test1-guide|Русский]] · **English** · [[es/seminar-sem3/test1-guide|Español]]

[[en/seminar-sem3/index|All assignments]] · [[en/seminar-sem3/index#Seminar notes|Seminar notes]] · [[en/seminar-sem3/test1-variants|Practice variants →]]

> [!note] What this is
> A preparation plan for test 1 based on homework 1–4. The structure of the test is as reported: four tasks, items **1.1, 1.2, 2.1, 2.2, 3, 4**; tasks 1 and 2 are on Taylor's formula and extrema, tasks 3 and 4 on series. There are no real papers: the problem types below are a forecast from the homework, not a leak. The assignment of topics to items is a guess.

## Likely structure

| Item | What will probably be asked | Prototypes in the homework |
|---|---|---|
| 1.1 | Expand a polynomial by Taylor's formula at a given point (a finite sum) | [[en/seminar-sem3/hw1-taylor\|1.1, 1.2]] |
| 1.2 | Expansion of a non-polynomial function up to degree 2 or 3 with the Lagrange remainder | [[en/seminar-sem3/hw1-taylor\|1.3, 1.4]] |
| 2.1 | Constrained extremum where the constraint can be solved explicitly (line, plane) | [[en/seminar-sem3/hw2-conditional-extremum\|2.1, 2.3]] |
| 2.2 | Constrained extremum on a compact set by the Lagrange method (ellipsoid, circle) | [[en/seminar-sem3/hw2-conditional-extremum\|2.2, 2'.1]] |
| 3 | A proof: a test or a property of series | [[en/seminar-sem3/hw3-numerical-series\|3.1–3.9]], [[en/seminar-sem3/hw4-series-inequalities-bases\|4.4, 4.6, 4.10, 4.11]] |
| 4 | Test 2–3 concrete series for convergence | [[en/seminar-sem3/hw3-numerical-series\|3.11]], [[en/seminar-sem3/hw4-series-inequalities-bases\|4.7–4.9, 4.12]] |

Less likely but possible: problems with a parameter ([[en/seminar-sem3/hw2-conditional-extremum|2'.2, 2'.3]], [[en/seminar-sem3/hw4-series-inequalities-bases|4.8]]), Hölder's inequality ([[en/seminar-sem3/hw4-series-inequalities-bases|4.1, 4.2]]), examples and counterexamples ([[en/seminar-sem3/hw3-numerical-series|3.8, 3.10]], [[en/seminar-sem3/hw4-series-inequalities-bases|4.5]]), bases ([[en/seminar-sem3/hw4-series-inequalities-bases|4.3]]).

## Task 1: Taylor's formula

**What to know by heart.**
$$
f(a+h)=\sum_{k=0}^{s}\frac{d_a^kf(h)}{k!}+\frac{d_c^{s+1}f(h)}{(s+1)!},\qquad c=a+\theta h,\ \theta\in(0,1),
$$
$$
d^kf(h)=\sum_{|\alpha|=k}\frac{k!}{\alpha!}\,\partial^\alpha f\cdot h^\alpha .
$$
For two variables: $d^2f=f_{xx}h_1^2+2f_{xy}h_1h_2+f_{yy}h_2^2$, $d^3f=f_{xxx}h_1^3+3f_{xxy}h_1^2h_2+3f_{xyy}h_1h_2^2+f_{yyy}h_2^3$. For three variables the coefficients in $d^3f$ are $1$ (pure), $3$ (of the form $\partial_i^2\partial_j$) and $6$ (for $f_{xyz}$).

**Method for a polynomial (item 1.1).**

1. Introduce $h_1=x-a_1$, $h_2=y-a_2$, …
2. Either substitute $x=a_1+h_1$, … and multiply out, or compute the derivatives at the point and assemble $d^kf/k!$.
3. Say that the sum stops at the degree of the polynomial: all higher derivatives vanish, the remainder is zero, the equality is exact.
4. Check: the top homogeneous part must coincide with the top part of the original polynomial; substitute one simple $h$ (for example $(1,0)$) into both sides.

**Method for the Lagrange remainder (item 1.2).**

1. Compute the value and the derivatives up to order $s$ at $a$ — this gives the polynomial.
2. Compute **all** derivatives of order $s+1$ in general form (not at $a$!).
3. Write the remainder: $\frac1{(s+1)!}d^{s+1}f$ with the derivatives taken at $c=(a_1+\theta h_1,\dots)$, and do write "$\theta\in(0,1)$".
4. If the function is a composition $e^{u}$, $\ln u$, $\sin u$ with a polynomial $u$, it is faster to work with $F(t)=f(a+th)$: $F^{(k)}(0)/k!$ are the terms of the expansion, $F^{(s+1)}(\theta)/(s+1)!$ is the remainder (this is how [[en/seminar-sem3/hw1-taylor|problem 1.3]] is solved).

**Typical mistakes.**

- A forgotten factor $\frac1{k!}$ or multinomial coefficient ($2$ for $f_{xy}$, $3$ for $f_{xxy}$, $6$ for $f_{xyz}$).
- The remainder written at $a$ instead of the intermediate point $c$; $\theta\in(0,1)$ not stated.
- The Lagrange remainder confused with the Peano remainder $o(|h|^s)$: "in Lagrange form" asks for the explicit expression.
- The answer left in $x,y$ without saying what $h$ is.

## Task 2: extrema

**What to know.**

- Necessary condition for an unconstrained extremum: $\nabla f=0$. Sufficient: the sign of $d^2f$ (positive definite — minimum, negative definite — maximum, indefinite — no extremum, semi-definite — the test is silent).
- Sylvester's criterion for $2\times2$: $\Delta_1=f_{xx}$, $\Delta_2=f_{xx}f_{yy}-f_{xy}^2$. $\Delta_2>0,\ \Delta_1>0$ — minimum; $\Delta_2>0,\ \Delta_1<0$ — maximum; $\Delta_2<0$ — saddle; $\Delta_2=0$ — examine by hand.
- Constrained extremum: $L=f-\sum\lambda_j\varphi_j$, the system $\nabla L=0$ plus the constraint equations; the sufficient condition is the sign of $d^2L$ **on the tangent space** $\{h:\ d\varphi_j(h)=0\}$. At the seminar the same condition was checked through the signs of the minors of the bordered Hessian; the method is below.

**Method when the constraint can be solved explicitly (item 2.1).**

1. Parametrise $M$ (for example, $y=x$) and get a function $g$ of fewer variables.
2. Find the stationary points of $g$ and examine them with the second differential.
3. If the second differential is degenerate, look at the sign of the increment directly (as in [[en/seminar-sem3/hw2-conditional-extremum|2.3]]: the term $2x^3$ changes sign, so there is no extremum).
4. Go back to the original coordinates; state the type (maximum or minimum, strict or not, local or global) and the value.

**The Lagrange method (item 2.2).**

1. Check regularity: the gradients of the constraints are linearly independent on $M$ (usually "they vanish only at a point not on $M$").
2. Solve the Lagrange system. Do not divide by an expression that may be zero without treating that case: write $(x-y)(z+2\lambda)=0$ and handle both alternatives.
3. Determine the type of the points. The fastest way when $M$ is compact (sphere, ellipsoid, circle): "$f$ is continuous on a compact set, so it attains its greatest and least values, and they are attained at stationary points" — then compare the values.
4. Write the answer: the points, the type, the extremal values.

**The bordered-Hessian method (as done at the seminar, [[en/seminar-sem3/notes-1-taylor-extremum#Theorem 3.1. Conditional extrema and the bordered Hessian|Theorem 3.1]]).**

1. Write $\mathcal L=f+\sum_k\lambda_kg_k$ and solve the system of $n+m$ equations: all partial derivatives of $\mathcal L$ in $x_j$ and in $\lambda_k$ vanish.
2. Form $\widetilde H=\begin{pmatrix}0&J_g\\ J_g^{T}&H_{\mathcal L}\end{pmatrix}$ and find the minors $\Delta_{2m+1},\dots,\Delta_{n+m}$ at a general point first, as the seminar advised.
3. Substitute each stationary point together with its $\lambda$. All signs equal to $(-1)^m$ — a minimum; the sign of $\Delta_k$ equal to $(-1)^{k-m}$ — a maximum; non-zero minors with other signs — no extremum; $\Delta_{n+m}=0$ — the test is silent, examine by hand.
4. The most common case $n=2$, $m=1$: $\det\widetilde H<0$ — a minimum, $\det\widetilde H>0$ — a maximum ([[en/seminar-sem3/notes-1-taylor-extremum#^ex-4-2|Example 4.2]]). For $n=4$, $m=2$: a minimum is $\Delta_5>0$, $\Delta_6>0$; a maximum is $\Delta_5<0$, $\Delta_6>0$ ([[en/seminar-sem3/notes-1-taylor-extremum#^ex-5-1|Example 5.1]]).

**Typical mistakes.**

- A stationary point declared an extremum without verification (the Lagrange system is only a necessary condition).
- $d^2L$ examined on the whole space instead of the tangent space.
- Solutions lost when dividing; the second point with the opposite sign lost.
- The compactness argument applied to a non-compact $M$ (a line, a plane): there may be no greatest value there.
- Regularity of the constraints not checked.

## Task 3: proofs about series

**Three facts from which almost everything follows** (details at the beginning of [[en/seminar-sem3/hw3-numerical-series|HW 3]]):

1. the necessary condition: the series converges ⟹ $a_k\to0$;
2. a series with non-negative terms converges ⟺ its partial sums are bounded above;
3. finitely many terms do not affect convergence.

**What to be able to prove with the notebook closed** (in decreasing order of likelihood):

| Statement | Key idea in one line | Where |
|---|---|---|
| A convergent series has bounded partial sums | a convergent sequence is bounded | [[en/seminar-sem3/hw3-numerical-series\|3.1]] |
| Generalised comparison test | $\frac{a_n}{b_n}$ is non-increasing ⟹ $a_n\le Cb_n$ | [[en/seminar-sem3/hw3-numerical-series\|3.4]] |
| Kummer's test | multiply by $a_{n+1}$, add up, the sum telescopes | [[en/seminar-sem3/hw3-numerical-series\|3.6]] |
| D'Alembert's test | Kummer with $x_n=1$ | [[en/seminar-sem3/hw3-numerical-series\|3.7]] |
| Raabe's test | Kummer with $x_n=n$ | [[en/seminar-sem3/hw3-numerical-series\|3.9]] |
| Raabe ⟹ d'Alembert | $1+\beta\ge1+\frac2n$ for $n\ge\frac2\beta$ | [[en/seminar-sem3/hw4-series-inequalities-bases\|4.4]] |
| Limit forms of the tests | a limit ⟹ an inequality from some index on | [[en/seminar-sem3/hw4-series-inequalities-bases\|4.6]] |
| Leibniz's test | $S_{2m}$ is monotone and bounded, $S_{2m+1}=S_{2m}+a_{2m+1}$ | [[en/seminar-sem3/hw4-series-inequalities-bases\|4.11]] |
| Integral test | $f(k+1)\le\int_k^{k+1}f\le f(k)$ | [[en/seminar-sem3/hw4-series-inequalities-bases\|4.10]] |
| Boundedness of the sums $\sum\sin(kx_0)$ | multiply by $2\sin\frac{x_0}2$, telescoping | [[en/seminar-sem3/hw3-numerical-series\|3.2]] |
| $\sum\cos(kx_0)$ diverges | $\cos(2kx_0)=2\cos^2(kx_0)-1$, the general term does not tend to zero | [[en/seminar-sem3/hw3-numerical-series\|3.3]] |
| Cauchy's root test | $\sqrt[n]{a_n}\le q$ ⟺ $a_n\le q^n$; for divergence infinitely many $n$ are enough | [[en/seminar-sem3/notes-2-series-basics#Theorem 8.2. Cauchy's (root) test\|Theorem 8.2]] |
| $\sum\sin(kx_0)$ converges ⟺ $x_0\in\pi\mathbb Z$ | $\cos(kx_0)$ is expressed through $\sin(kx_0)$ and $\sin((k+1)x_0)$ | [[en/seminar-sem3/notes-2-series-basics#^ex-8-1\|Example 8.1]] |
| $\sum\frac{c_k}{k^d}$ converges ⟺ $d>1$ | comparison with $\frac{M_2}{k^d}$, then Raabe | [[en/seminar-sem3/hw3-numerical-series#^p-3-11\|3.11]], [[en/seminar-sem3/notes-3-kummer-dalembert-raabe#^thm-12-1\|Theorem 12.1]] |

**The tests in the seminar's notation.** Note: the seminar uses the ratio $\dfrac{a_n}{a_{n+1}}$ (previous to next), not $\dfrac{a_{n+1}}{a_n}$.

| Test | Converges if, from some index on, | Diverges if, from some index on, |
|---|---|---|
| Kummer | $x_n\frac{a_n}{a_{n+1}}-x_{n+1}\ge\alpha>0$ | $x_n\frac{a_n}{a_{n+1}}-x_{n+1}\le0$ and $\sum\frac1{x_n}$ diverges |
| d'Alembert | $\frac{a_n}{a_{n+1}}\ge1+\beta$, $\beta>0$ | $\frac{a_n}{a_{n+1}}\le1$ |
| Raabe | $\frac{a_n}{a_{n+1}}\ge1+\frac{1+\gamma}n$, $\gamma>0$ | $\frac{a_n}{a_{n+1}}\le1+\frac1n$ |
| Cauchy | $\sqrt[n]{a_n}\le q<1$ | $\sqrt[n]{a_n}\ge1$ for infinitely many $n$ |
| Cauchy (limit form) | $\sqrt[k]{a_k}\to L<1$ | $\sqrt[k]{a_k}\to L>1$ |
| Leibniz | signs alternate, $\lvert a_k\rvert$ is non-increasing, $a_k\to0$ | — |

**How to write a proof so as not to lose marks.**

- Name explicitly the index from which the inequality holds, and refer to "finitely many terms do not matter".
- Before multiplying or dividing an inequality, say that the factor is positive.
- At the end name the criterion used: "the partial sums of a non-negative series are bounded, hence it converges".

## Task 4: testing series for convergence

**Order of actions.**

1. **Does the general term tend to zero?** If not — divergent, done ([[en/seminar-sem3/hw4-series-inequalities-bases|4.7, 3)]]).
2. **Sign-changing?** Check Leibniz. If the series has zeros or the signs alternate in groups, drop the zeros or group the terms ([[en/seminar-sem3/hw4-series-inequalities-bases|4.12]]).
3. **Factorials, powers $q^k$, $k^k$?** Compute $\frac{a_k}{a_{k+1}}$. Limit greater than $1$ — converges, less than $1$ — diverges.
4. **The limit of the ratio equals $1$?** D'Alembert does not work. Compute $R_k=k\bigl(\frac{a_k}{a_{k+1}}-1\bigr)$: limit greater than $1$ — converges, less than $1$ — diverges ([[en/seminar-sem3/hw4-series-inequalities-bases|4.9]]).
5. **Powers, roots, rational expressions in $k$?** Bring to the form $\frac{C_k}{k^\alpha}$ with $0<M_1\le C_k\le M_2$; converges ⟺ $\alpha>1$ ([[en/seminar-sem3/hw3-numerical-series|3.11]], [[en/seminar-sem3/hw4-series-inequalities-bases|4.8]]). A difference of roots — multiply by the conjugate.
6. **A $k$-th power as a whole?** Cauchy's root test.
7. **Logarithms of the form $\frac1{k\ln^pk}$?** The integral test.
8. **An irregular series** (terms defined piecewise)? Estimate the partial sums directly ([[en/seminar-sem3/hw4-series-inequalities-bases|4.7, 2)]]).

**Reference series.**

| Series | Converges |
|---|---|
| $\sum q^k$ | for $\lvert q\rvert<1$ |
| $\sum\frac1{k^\alpha}$ | for $\alpha>1$ |
| $\sum\frac{1}{k\ln^pk}$ | for $p>1$ |
| $\sum\frac1{k(k+1)}$, $\sum\frac1{k!}$ | yes |
| $\sum\frac{(-1)^k}{k^\alpha}$ | for $\alpha>0$ (absolutely for $\alpha>1$) |

**Useful limits and inequalities.** $\bigl(1+\frac1k\bigr)^k\uparrow e$, so $\bigl(1+\frac1k\bigr)^k<e$ for all $k$; $\sqrt[k]k\to1$; $1+t\le e^t$; $(1+x)^\alpha\ge1+\alpha x$ for $\alpha\ge1$, $x\ge0$; $\ln(k!)\le k\ln k$.

**Typical mistakes.**

- The ratio upside down: with $\frac{a_k}{a_{k+1}}\to L$ the series converges for $L>1$, not for $L<1$.
- The conclusion "the limit of the ratio is $1$, hence divergent" — no, the test simply does not apply.
- Leibniz's test applied without checking monotonicity of the absolute values, or in the presence of zero terms.
- "$a_k\to0$, hence convergent" — the necessary condition is not sufficient.
- Comparison $a_k\le b_k$ for sign-changing series — comparison tests only work for non-negative ones.
- The borderline value of a parameter not treated separately ($\beta=e$ in [[en/seminar-sem3/hw4-series-inequalities-bases|4.8]]).

## What to review in the seminar notes

The [[en/seminar-sem3/index#Seminar notes|notes]] show the form in which the theory was given at the seminar. At the test it is sensible to write in the same notation: eventually positive sequences, the ratio $\frac{a_n}{a_{n+1}}$, the Lagrange function with a plus sign, the bordered Hessian.

| Item | What to review | Where |
|---|---|---|
| 1.1 | Taylor's formula with multi-indices; why the remainder of a polynomial is zero | [[en/seminar-sem3/notes-1-taylor-extremum#^ex-2-2\|Example 2.2]] |
| 1.2 | the table of derivatives, the factors $\frac1{\alpha!}$, the remainder at $u+t_0h$ | [[en/seminar-sem3/notes-1-taylor-extremum#^ex-4-1\|Example 4.1]], [[en/seminar-sem3/notes-1-taylor-extremum#Remark 2.1. A segment is the set of convex combinations of its endpoints\|Remark 2.1]] |
| 2.1 | the bordered Hessian for linear constraints: one constraint and two | [[en/seminar-sem3/notes-1-taylor-extremum#^ex-4-2\|Example 4.2]], [[en/seminar-sem3/notes-1-taylor-extremum#^ex-5-1\|Example 5.1]] |
| 2.2 | the statement of the theorem and the sign table of the minors | [[en/seminar-sem3/notes-1-taylor-extremum#Theorem 3.1. Conditional extrema and the bordered Hessian\|Theorem 3.1]], [[en/seminar-sem3/notes-1-taylor-extremum#^ex-3-2\|Example 3.2]] |
| 3 | the proofs from the board: comparison, Cauchy, generalised comparison, Kummer, d'Alembert, Raabe, Raabe ⟹ d'Alembert | [[en/seminar-sem3/notes-2-series-basics\|part 2]], [[en/seminar-sem3/notes-3-kummer-dalembert-raabe#^thm-10-2\|Theorem 10.2 and its corollaries]], [[en/seminar-sem3/notes-4-examples-tests#^rem-14-2\|Remark 14.2]] |
| 4 | series with a parameter and examples where the tests fail | [[en/seminar-sem3/notes-4-examples-tests#^ex-13-1\|Examples 13.1, 13.2]], [[en/seminar-sem3/notes-4-examples-tests#^ex-14-1\|14.1]], [[en/seminar-sem3/notes-3-kummer-dalembert-raabe#^ex-10-4\|10.4]], [[en/seminar-sem3/notes-3-kummer-dalembert-raabe#Remark 12.2. What to look at for an eventually positive series\|Remark 12.2]] |

At the seminar Problem 2.3 was solved in the $y^2$ variant ([[en/seminar-sem3/notes-1-taylor-extremum#^ex-5-1|Example 5.1]]), while HW 2 has $y^3$. If a similar problem comes up, check the power in the statement first: the answers differ.

## Preparation plan

**Day 1 — Taylor and extrema.**

1. Read the sections "The general idea" in [[en/seminar-sem3/hw1-taylor|HW 1]] and "Why the Lagrange method works" in [[en/seminar-sem3/hw2-conditional-extremum|HW 2]], then [[en/seminar-sem3/notes-1-taylor-extremum|part 1 of the notes]], especially Theorem 3.1 with its sign table.
2. Solve 1.2 and 1.4 again without looking at the solution, then 2.2 and 2'.1. Compare.
3. Solve items 1.1, 1.2, 2.1, 2.2 of [[en/seminar-sem3/test1-variants|variant A]] against the clock: 40 minutes.

**Day 2 — series.**

1. Learn the table of tests and the three basic facts; read [[en/seminar-sem3/notes-2-series-basics|parts 2–4 of the notes]].
2. In writing, with the notebook closed, prove 3.4, 3.6, 3.7, 3.9, 4.11 and Cauchy's root test ([[en/seminar-sem3/notes-2-series-basics#Theorem 8.2. Cauchy's (root) test|Theorem 8.2]]). Compare with the solutions.
3. Work through 4.7–4.9 and 4.12 again.
4. Solve tasks 3 and 4 of [[en/seminar-sem3/test1-variants|variant A]]: 40 minutes.

**Day 3 — a run-through.**

1. [[en/seminar-sem3/test1-variants|Variant B]] in full against the clock (80–90 minutes), check against the solutions.
2. Go over the mistakes and revise the corresponding places.
3. [[en/seminar-sem3/test1-variants|Variant C]] in full against the clock.

## Self-check before the test

1. What is the coefficient of $h_1h_2h_3$ in $d^3f(h)$?
2. At which point are the derivatives in the Lagrange remainder taken?
3. Why is the Taylor expansion of a polynomial a finite sum?
4. When can one say "the stationary point is a maximum" without computing the second differential?
5. On which vectors is $d^2L$ examined?
6. Which sequence $x_n$ in Kummer's test gives Raabe's test?
7. What does Raabe's test say about a series with $\frac{a_n}{a_{n+1}}=1+\frac1{2n+1}$?
8. Does $\sum\frac{e^kk!}{k^k}$ converge, and why does the limit form not help here?
9. Which three conditions does Leibniz's test need?
10. Give an example of a divergent series with bounded partial sums.
11. Which minors of the bordered Hessian are checked for $n=4$, $m=2$, and which signs mean a maximum?
12. Why are "infinitely many $n$" enough for divergence in Cauchy's test but not in d'Alembert's?

> [!answer]- Answers
> 1. $6f_{xyz}$: the multinomial coefficient $\frac{3!}{1!\,1!\,1!}$.
> 2. At the intermediate point $c=a+\theta h$, $\theta\in(0,1)$.
> 3. All derivatives of order above the degree of the polynomial vanish, so the remainder is zero.
> 4. When the set $M$ is compact: the greatest value is attained and must be attained at a stationary point; it remains to compare the values.
> 5. On tangent vectors: $d\varphi_j(h)=0$ for all constraints.
> 6. $x_n=n$.
> 7. It diverges: $1+\frac1{2n+1}\le1+\frac1n$.
> 8. It diverges. The limit of the ratio is $1$, but $\frac{a_k}{a_{k+1}}=\frac1e\bigl(1+\frac1k\bigr)^k<1$ for all $k$ — the pre-limit form of d'Alembert's test applies.
> 9. The signs alternate, the absolute values are non-increasing, the general term tends to zero.
> 10. $\sum(-1)^k$, or $\sum\cos(kx_0)$ for $x_0\notin2\pi\mathbb Z$.
> 11. $\Delta_5$ and $\Delta_6$; a maximum is $\Delta_5<0$, $\Delta_6>0$, that is, the sign of $\Delta_k$ is $(-1)^{k-m}$ ([[en/seminar-sem3/notes-1-taylor-extremum#^ex-5-1|Example 5.1]]).
> 12. $\sqrt[n]{a_n}\ge1$ means $a_n\ge1$, and infinitely many such terms prevent $a_n\to0$. A ratio only describes one step: the series of [[en/seminar-sem3/notes-3-kummer-dalembert-raabe#^ex-10-4|Example 10.4]] grows infinitely often and still converges.

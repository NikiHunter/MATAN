---
title: "Seminar NM-204. Test 1 — how to prepare"
lang: en
---
# Test 1: how to prepare

[Русский](../../ru/seminar-sem3/test1-guide.md) · **English** · [Español](../../es/seminar-sem3/test1-guide.md)

[All assignments](index.md) · [Practice variants →](test1-variants.md)

> **What this is.** A preparation plan for test 1 based on homework 1–4. The structure of the test is as reported: four tasks, items **1.1, 1.2, 2.1, 2.2, 3, 4**; tasks 1 and 2 are on Taylor's formula and extrema, tasks 3 and 4 on series. There are no real papers: the problem types below are a forecast from the homework, not a leak. The assignment of topics to items is a guess.

## Likely structure

| Item | What will probably be asked | Prototypes in the homework |
|---|---|---|
| 1.1 | Expand a polynomial by Taylor's formula at a given point (a finite sum) | [1.1, 1.2](hw1-taylor.md) |
| 1.2 | Expansion of a non-polynomial function up to degree 2 or 3 with the Lagrange remainder | [1.3, 1.4](hw1-taylor.md) |
| 2.1 | Constrained extremum where the constraint can be solved explicitly (line, plane) | [2.1, 2.3](hw2-conditional-extremum.md) |
| 2.2 | Constrained extremum on a compact set by the Lagrange method (ellipsoid, circle) | [2.2, 2'.1](hw2-conditional-extremum.md) |
| 3 | A proof: a test or a property of series | [3.1–3.9](hw3-numerical-series.md), [4.4, 4.6, 4.10, 4.11](hw4-series-inequalities-bases.md) |
| 4 | Test 2–3 concrete series for convergence | [3.11](hw3-numerical-series.md), [4.7–4.9, 4.12](hw4-series-inequalities-bases.md) |

Less likely but possible: problems with a parameter ([2'.2, 2'.3](hw2-conditional-extremum.md), [4.8](hw4-series-inequalities-bases.md)), Hölder's inequality ([4.1, 4.2](hw4-series-inequalities-bases.md)), examples and counterexamples ([3.8, 3.10](hw3-numerical-series.md), [4.5](hw4-series-inequalities-bases.md)), bases ([4.3](hw4-series-inequalities-bases.md)).

## Task 1: Taylor's formula

**What to know by heart.**
```math
f(a+h)=\sum_{k=0}^{s}\frac{d_a^kf(h)}{k!}+\frac{d_c^{s+1}f(h)}{(s+1)!},\qquad c=a+\theta h,\ \theta\in(0,1),
```
```math
d^kf(h)=\sum_{|\alpha|=k}\frac{k!}{\alpha!}\,\partial^\alpha f\cdot h^\alpha .
```
For two variables: $`d^2f=f_{xx}h_1^2+2f_{xy}h_1h_2+f_{yy}h_2^2`$, $`d^3f=f_{xxx}h_1^3+3f_{xxy}h_1^2h_2+3f_{xyy}h_1h_2^2+f_{yyy}h_2^3`$. For three variables the coefficients in $`d^3f`$ are $`1`$ (pure), $`3`$ (of the form $`\partial_i^2\partial_j`$) and $`6`$ (for $`f_{xyz}`$).

**Method for a polynomial (item 1.1).**

1. Introduce $`h_1=x-a_1`$, $`h_2=y-a_2`$, …
2. Either substitute $`x=a_1+h_1`$, … and multiply out, or compute the derivatives at the point and assemble $`d^kf/k!`$.
3. Say that the sum stops at the degree of the polynomial: all higher derivatives vanish, the remainder is zero, the equality is exact.
4. Check: the top homogeneous part must coincide with the top part of the original polynomial; substitute one simple $`h`$ (for example $`(1,0)`$) into both sides.

**Method for the Lagrange remainder (item 1.2).**

1. Compute the value and the derivatives up to order $`s`$ at $`a`$ — this gives the polynomial.
2. Compute **all** derivatives of order $`s+1`$ in general form (not at $`a`$!).
3. Write the remainder: $`\frac1{(s+1)!}d^{s+1}f`$ with the derivatives taken at $`c=(a_1+\theta h_1,\dots)`$, and do write "$`\theta\in(0,1)`$".
4. If the function is a composition $`e^{u}`$, $`\ln u`$, $`\sin u`$ with a polynomial $`u`$, it is faster to work with $`F(t)=f(a+th)`$: $`F^{(k)}(0)/k!`$ are the terms of the expansion, $`F^{(s+1)}(\theta)/(s+1)!`$ is the remainder (this is how [problem 1.3](hw1-taylor.md) is solved).

**Typical mistakes.**

- A forgotten factor $`\frac1{k!}`$ or multinomial coefficient ($`2`$ for $`f_{xy}`$, $`3`$ for $`f_{xxy}`$, $`6`$ for $`f_{xyz}`$).
- The remainder written at $`a`$ instead of the intermediate point $`c`$; $`\theta\in(0,1)`$ not stated.
- The Lagrange remainder confused with the Peano remainder $`o(|h|^s)`$: "in Lagrange form" asks for the explicit expression.
- The answer left in $`x,y`$ without saying what $`h`$ is.

## Task 2: extrema

**What to know.**

- Necessary condition for an unconstrained extremum: $`\nabla f=0`$. Sufficient: the sign of $`d^2f`$ (positive definite — minimum, negative definite — maximum, indefinite — no extremum, semi-definite — the test is silent).
- Sylvester's criterion for $`2\times2`$: $`\Delta_1=f_{xx}`$, $`\Delta_2=f_{xx}f_{yy}-f_{xy}^2`$. $`\Delta_2>0,\ \Delta_1>0`$ — minimum; $`\Delta_2>0,\ \Delta_1<0`$ — maximum; $`\Delta_2<0`$ — saddle; $`\Delta_2=0`$ — examine by hand.
- Constrained extremum: $`L=f-\sum\lambda_j\varphi_j`$, the system $`\nabla L=0`$ plus the constraint equations; the sufficient condition is the sign of $`d^2L`$ **on the tangent space** $`\{h:\ d\varphi_j(h)=0\}`$.

**Method when the constraint can be solved explicitly (item 2.1).**

1. Parametrise $`M`$ (for example, $`y=x`$) and get a function $`g`$ of fewer variables.
2. Find the stationary points of $`g`$ and examine them with the second differential.
3. If the second differential is degenerate, look at the sign of the increment directly (as in [2.3](hw2-conditional-extremum.md): the term $`2x^3`$ changes sign, so there is no extremum).
4. Go back to the original coordinates; state the type (maximum or minimum, strict or not, local or global) and the value.

**The Lagrange method (item 2.2).**

1. Check regularity: the gradients of the constraints are linearly independent on $`M`$ (usually "they vanish only at a point not on $`M`$").
2. Solve the Lagrange system. Do not divide by an expression that may be zero without treating that case: write $`(x-y)(z+2\lambda)=0`$ and handle both alternatives.
3. Determine the type of the points. The fastest way when $`M`$ is compact (sphere, ellipsoid, circle): "$`f`$ is continuous on a compact set, so it attains its greatest and least values, and they are attained at stationary points" — then compare the values.
4. Write the answer: the points, the type, the extremal values.

**Typical mistakes.**

- A stationary point declared an extremum without verification (the Lagrange system is only a necessary condition).
- $`d^2L`$ examined on the whole space instead of the tangent space.
- Solutions lost when dividing; the second point with the opposite sign lost.
- The compactness argument applied to a non-compact $`M`$ (a line, a plane): there may be no greatest value there.
- Regularity of the constraints not checked.

## Task 3: proofs about series

**Three facts from which almost everything follows** (details at the beginning of [HW 3](hw3-numerical-series.md)):

1. the necessary condition: the series converges ⟹ $`a_k\to0`$;
2. a series with non-negative terms converges ⟺ its partial sums are bounded above;
3. finitely many terms do not affect convergence.

**What to be able to prove with the notebook closed** (in decreasing order of likelihood):

| Statement | Key idea in one line | Where |
|---|---|---|
| A convergent series has bounded partial sums | a convergent sequence is bounded | [3.1](hw3-numerical-series.md) |
| Generalised comparison test | $`\frac{a_n}{b_n}`$ is non-increasing ⟹ $`a_n\le Cb_n`$ | [3.4](hw3-numerical-series.md) |
| Kummer's test | multiply by $`a_{n+1}`$, add up, the sum telescopes | [3.6](hw3-numerical-series.md) |
| D'Alembert's test | Kummer with $`x_n=1`$ | [3.7](hw3-numerical-series.md) |
| Raabe's test | Kummer with $`x_n=n`$ | [3.9](hw3-numerical-series.md) |
| Raabe ⟹ d'Alembert | $`1+\beta\ge1+\frac2n`$ for $`n\ge\frac2\beta`$ | [4.4](hw4-series-inequalities-bases.md) |
| Limit forms of the tests | a limit ⟹ an inequality from some index on | [4.6](hw4-series-inequalities-bases.md) |
| Leibniz's test | $`S_{2m}`$ is monotone and bounded, $`S_{2m+1}=S_{2m}+a_{2m+1}`$ | [4.11](hw4-series-inequalities-bases.md) |
| Integral test | $`f(k+1)\le\int_k^{k+1}f\le f(k)`$ | [4.10](hw4-series-inequalities-bases.md) |
| Boundedness of the sums $`\sum\sin(kx_0)`$ | multiply by $`2\sin\frac{x_0}2`$, telescoping | [3.2](hw3-numerical-series.md) |
| $`\sum\cos(kx_0)`$ diverges | $`\cos(2kx_0)=2\cos^2(kx_0)-1`$, the general term does not tend to zero | [3.3](hw3-numerical-series.md) |

**The tests in the seminar's notation.** Note: the seminar uses the ratio $`\dfrac{a_n}{a_{n+1}}`$ (previous to next), not $`\dfrac{a_{n+1}}{a_n}`$.

| Test | Converges if, from some index on, | Diverges if, from some index on, |
|---|---|---|
| Kummer | $`x_n\frac{a_n}{a_{n+1}}-x_{n+1}\ge\alpha>0`$ | $`x_n\frac{a_n}{a_{n+1}}-x_{n+1}\le0`$ and $`\sum\frac1{x_n}`$ diverges |
| d'Alembert | $`\frac{a_n}{a_{n+1}}\ge1+\beta`$, $`\beta>0`$ | $`\frac{a_n}{a_{n+1}}\le1`$ |
| Raabe | $`\frac{a_n}{a_{n+1}}\ge1+\frac{1+\gamma}n`$, $`\gamma>0`$ | $`\frac{a_n}{a_{n+1}}\le1+\frac1n`$ |
| Cauchy (limit form) | $`\sqrt[k]{a_k}\to L<1`$ | $`\sqrt[k]{a_k}\to L>1`$ |
| Leibniz | signs alternate, $`\lvert a_k\rvert`$ is non-increasing, $`a_k\to0`$ | — |

**How to write a proof so as not to lose marks.**

- Name explicitly the index from which the inequality holds, and refer to "finitely many terms do not matter".
- Before multiplying or dividing an inequality, say that the factor is positive.
- At the end name the criterion used: "the partial sums of a non-negative series are bounded, hence it converges".

## Task 4: testing series for convergence

**Order of actions.**

1. **Does the general term tend to zero?** If not — divergent, done ([4.7, 3)](hw4-series-inequalities-bases.md)).
2. **Sign-changing?** Check Leibniz. If the series has zeros or the signs alternate in groups, drop the zeros or group the terms ([4.12](hw4-series-inequalities-bases.md)).
3. **Factorials, powers $`q^k`$, $`k^k`$?** Compute $`\frac{a_k}{a_{k+1}}`$. Limit greater than $`1`$ — converges, less than $`1`$ — diverges.
4. **The limit of the ratio equals $`1`$?** D'Alembert does not work. Compute $`R_k=k\bigl(\frac{a_k}{a_{k+1}}-1\bigr)`$: limit greater than $`1`$ — converges, less than $`1`$ — diverges ([4.9](hw4-series-inequalities-bases.md)).
5. **Powers, roots, rational expressions in $`k`$?** Bring to the form $`\frac{C_k}{k^\alpha}`$ with $`0<M_1\le C_k\le M_2`$; converges ⟺ $`\alpha>1`$ ([3.11](hw3-numerical-series.md), [4.8](hw4-series-inequalities-bases.md)). A difference of roots — multiply by the conjugate.
6. **A $`k`$-th power as a whole?** Cauchy's root test.
7. **Logarithms of the form $`\frac1{k\ln^pk}`$?** The integral test.
8. **An irregular series** (terms defined piecewise)? Estimate the partial sums directly ([4.7, 2)](hw4-series-inequalities-bases.md)).

**Reference series.**

| Series | Converges |
|---|---|
| $`\sum q^k`$ | for $`\lvert q\rvert<1`$ |
| $`\sum\frac1{k^\alpha}`$ | for $`\alpha>1`$ |
| $`\sum\frac{1}{k\ln^pk}`$ | for $`p>1`$ |
| $`\sum\frac1{k(k+1)}`$, $`\sum\frac1{k!}`$ | yes |
| $`\sum\frac{(-1)^k}{k^\alpha}`$ | for $`\alpha>0`$ (absolutely for $`\alpha>1`$) |

**Useful limits and inequalities.** $`\bigl(1+\frac1k\bigr)^k\uparrow e`$, so $`\bigl(1+\frac1k\bigr)^k<e`$ for all $`k`$; $`\sqrt[k]k\to1`$; $`1+t\le e^t`$; $`(1+x)^\alpha\ge1+\alpha x`$ for $`\alpha\ge1`$, $`x\ge0`$; $`\ln(k!)\le k\ln k`$.

**Typical mistakes.**

- The ratio upside down: with $`\frac{a_k}{a_{k+1}}\to L`$ the series converges for $`L>1`$, not for $`L<1`$.
- The conclusion "the limit of the ratio is $`1`$, hence divergent" — no, the test simply does not apply.
- Leibniz's test applied without checking monotonicity of the absolute values, or in the presence of zero terms.
- "$`a_k\to0`$, hence convergent" — the necessary condition is not sufficient.
- Comparison $`a_k\le b_k`$ for sign-changing series — comparison tests only work for non-negative ones.
- The borderline value of a parameter not treated separately ($`\beta=e`$ in [4.8](hw4-series-inequalities-bases.md)).

## Preparation plan

**Day 1 — Taylor and extrema.**

1. Read the sections "The general idea" in [HW 1](hw1-taylor.md) and "Why the Lagrange method works" in [HW 2](hw2-conditional-extremum.md).
2. Solve 1.2 and 1.4 again without looking at the solution, then 2.2 and 2'.1. Compare.
3. Solve items 1.1, 1.2, 2.1, 2.2 of [variant A](test1-variants.md) against the clock: 40 minutes.

**Day 2 — series.**

1. Learn the table of tests and the three basic facts.
2. In writing, with the notebook closed, prove 3.4, 3.6, 3.7, 3.9, 4.11. Compare with the solutions.
3. Work through 4.7–4.9 and 4.12 again.
4. Solve tasks 3 and 4 of [variant A](test1-variants.md): 40 minutes.

**Day 3 — a run-through.**

1. [Variant B](test1-variants.md) in full against the clock (80–90 minutes), check against the solutions.
2. Go over the mistakes and revise the corresponding places.
3. [Variant C](test1-variants.md) in full against the clock.

## Self-check before the test

1. What is the coefficient of $`h_1h_2h_3`$ in $`d^3f(h)`$?
2. At which point are the derivatives in the Lagrange remainder taken?
3. Why is the Taylor expansion of a polynomial a finite sum?
4. When can one say "the stationary point is a maximum" without computing the second differential?
5. On which vectors is $`d^2L`$ examined?
6. Which sequence $`x_n`$ in Kummer's test gives Raabe's test?
7. What does Raabe's test say about a series with $`\frac{a_n}{a_{n+1}}=1+\frac1{2n+1}`$?
8. Does $`\sum\frac{e^kk!}{k^k}`$ converge, and why does the limit form not help here?
9. Which three conditions does Leibniz's test need?
10. Give an example of a divergent series with bounded partial sums.

<details>
<summary>Answers</summary>

1. $`6f_{xyz}`$: the multinomial coefficient $`\frac{3!}{1!\,1!\,1!}`$.
2. At the intermediate point $`c=a+\theta h`$, $`\theta\in(0,1)`$.
3. All derivatives of order above the degree of the polynomial vanish, so the remainder is zero.
4. When the set $`M`$ is compact: the greatest value is attained and must be attained at a stationary point; it remains to compare the values.
5. On tangent vectors: $`d\varphi_j(h)=0`$ for all constraints.
6. $`x_n=n`$.
7. It diverges: $`1+\frac1{2n+1}\le1+\frac1n`$.
8. It diverges. The limit of the ratio is $`1`$, but $`\frac{a_k}{a_{k+1}}=\frac1e\bigl(1+\frac1k\bigr)^k<1`$ for all $`k`$ — the pre-limit form of d'Alembert's test applies.
9. The signs alternate, the absolute values are non-increasing, the general term tends to zero.
10. $`\sum(-1)^k`$, or $`\sum\cos(kx_0)`$ for $`x_0\notin2\pi\mathbb Z`$.
</details>

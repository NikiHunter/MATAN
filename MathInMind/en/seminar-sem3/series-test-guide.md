---
title: "Seminar NM-204. Series test — how to prepare"
lang: en
---
# Series test: how to prepare

[Русский](../../ru/seminar-sem3/series-test-guide.md) · **English** · [Español](../../es/seminar-sem3/series-test-guide.md)

[All assignments](index.md) · [Seminar notes](index.md#seminar-notes) · [← Test of 20 Nov (Taylor and extrema)](test1-guide.md)

> **What this is.** At the consultation before the test of 20 November 2026 the instructor said that the series problem of that test and the series problem of the next one will be combined into a separate test at the end of November or the beginning of December; the problem «on constant sign», which took a long time at the seminars, goes there too. The exact format has not been announced yet. Below is the material on series from the earlier version of the test 1 guide (series were then expected in tasks 3 and 4) and the practice problems from the earlier variants. This page will be updated once the format is known.

## What to expect

| Problem type | What will probably be asked | Prototypes in the homework |
|---|---|---|
| proofs | A proof: a test or a property of series | [3.1–3.9](hw3-numerical-series.md), [4.4, 4.6, 4.10, 4.11](hw4-series-inequalities-bases.md) |
| testing series | Test 2–3 concrete series for convergence | [3.11](hw3-numerical-series.md), [4.7–4.9, 4.12](hw4-series-inequalities-bases.md) |

Less likely but possible: series with a parameter ([4.8](hw4-series-inequalities-bases.md)), examples and counterexamples ([3.8, 3.10](hw3-numerical-series.md), [4.5](hw4-series-inequalities-bases.md)). This is a forecast from the homework, not an announced format.

## Proofs about series

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
| Cauchy's root test | $`\sqrt[n]{a_n}\le q`$ ⟺ $`a_n\le q^n`$; for divergence infinitely many $`n`$ are enough | [Theorem 8.2](notes-2-series-basics.md#thm-8-2) |
| $`\sum\sin(kx_0)`$ converges ⟺ $`x_0\in\pi\mathbb Z`$ | $`\cos(kx_0)`$ is expressed through $`\sin(kx_0)`$ and $`\sin((k+1)x_0)`$ | [Example 8.1](notes-2-series-basics.md#ex-8-1) |
| $`\sum\frac{c_k}{k^d}`$ converges ⟺ $`d>1`$ | comparison with $`\frac{M_2}{k^d}`$, then Raabe | [3.11](hw3-numerical-series.md#p-3-11), [Theorem 12.1](notes-3-kummer-dalembert-raabe.md#thm-12-1) |

**The tests in the seminar's notation.** Note: the seminar uses the ratio $`\dfrac{a_n}{a_{n+1}}`$ (previous to next), not $`\dfrac{a_{n+1}}{a_n}`$.

| Test | Converges if, from some index on, | Diverges if, from some index on, |
|---|---|---|
| Kummer | $`x_n\frac{a_n}{a_{n+1}}-x_{n+1}\ge\alpha>0`$ | $`x_n\frac{a_n}{a_{n+1}}-x_{n+1}\le0`$ and $`\sum\frac1{x_n}`$ diverges |
| d'Alembert | $`\frac{a_n}{a_{n+1}}\ge1+\beta`$, $`\beta>0`$ | $`\frac{a_n}{a_{n+1}}\le1`$ |
| Raabe | $`\frac{a_n}{a_{n+1}}\ge1+\frac{1+\gamma}n`$, $`\gamma>0`$ | $`\frac{a_n}{a_{n+1}}\le1+\frac1n`$ |
| Cauchy | $`\sqrt[n]{a_n}\le q<1`$ | $`\sqrt[n]{a_n}\ge1`$ for infinitely many $`n`$ |
| Cauchy (limit form) | $`\sqrt[k]{a_k}\to L<1`$ | $`\sqrt[k]{a_k}\to L>1`$ |
| Leibniz | signs alternate, $`\lvert a_k\rvert`$ is non-increasing, $`a_k\to0`$ | — |

**How to write a proof so as not to lose marks.**

- Name explicitly the index from which the inequality holds, and refer to "finitely many terms do not matter".
- Before multiplying or dividing an inequality, say that the factor is positive.
- At the end name the criterion used: "the partial sums of a non-negative series are bounded, hence it converges".

## Testing series for convergence

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

## What to review in the seminar notes

The [notes](index.md#seminar-notes) show the form in which the theory was given at the seminar. At the test it is sensible to write in the same notation: eventually positive sequences, the ratio $`\frac{a_n}{a_{n+1}}`$.

| Topic | What to review | Where |
|---|---|---|
| proofs | the proofs from the board: comparison, Cauchy, generalised comparison, Kummer, d'Alembert, Raabe, Raabe ⟹ d'Alembert | [part 2](notes-2-series-basics.md), [Theorem 10.2 and its corollaries](notes-3-kummer-dalembert-raabe.md#thm-10-2), [Remark 14.2](notes-4-examples-tests.md#rem-14-2) |
| testing series | series with a parameter and examples where the tests fail | [Examples 13.1, 13.2](notes-4-examples-tests.md#ex-13-1), [14.1](notes-4-examples-tests.md#ex-14-1), [10.4](notes-3-kummer-dalembert-raabe.md#ex-10-4), [Remark 12.2](notes-3-kummer-dalembert-raabe.md#rem-12-2) |

## Preparation plan

A detailed plan will follow once the format of the test is known. For now, a day of revising series:

1. Learn the table of tests and the three basic facts; read [parts 2–4 of the notes](notes-2-series-basics.md).
2. In writing, with the notebook closed, prove 3.4, 3.6, 3.7, 3.9, 4.11 and Cauchy's root test ([Theorem 8.2](notes-2-series-basics.md#thm-8-2)). Compare with the solutions.
3. Work through 4.7–4.9 and 4.12 again.
4. Solve one set of the [practice problems](#practice): 40 minutes.

## Self-check

1. Which sequence $`x_n`$ in Kummer's test gives Raabe's test?
2. What does Raabe's test say about a series with $`\frac{a_n}{a_{n+1}}=1+\frac1{2n+1}`$?
3. Does $`\sum\frac{e^kk!}{k^k}`$ converge, and why does the limit form not help here?
4. Which three conditions does Leibniz's test need?
5. Give an example of a divergent series with bounded partial sums.
6. Why are "infinitely many $`n`$" enough for divergence in Cauchy's test but not in d'Alembert's?

<details>
<summary>Answers</summary>

1. $`x_n=n`$.
2. It diverges: $`1+\frac1{2n+1}\le1+\frac1n`$.
3. It diverges. The limit of the ratio is $`1`$, but $`\frac{a_k}{a_{k+1}}=\frac1e\bigl(1+\frac1k\bigr)^k<1`$ for all $`k`$ — the pre-limit form of d'Alembert's test applies.
4. The signs alternate, the absolute values are non-increasing, the general term tends to zero.
5. $`\sum(-1)^k`$, or $`\sum\cos(kx_0)`$ for $`x_0\notin2\pi\mathbb Z`$.
6. $`\sqrt[n]{a_n}\ge1`$ means $`a_n\ge1`$, and infinitely many such terms prevent $`a_n\to0`$. A ratio only describes one step: the series of [Example 10.4](notes-3-kummer-dalembert-raabe.md#ex-10-4) grows infinitely often and still converges.
</details>

<a id="practice"></a>
## Practice problems

Tasks 3 and 4 of the earlier practice variants of test 1. In every set, problem 1 is a proof and problem 2 asks to test concrete series for convergence. Aim for 40 minutes per set.

### Set A

**1.** Let $`a_n>0`$, $`b_n>0`$ and $`\dfrac{a_{n+1}}{a_n}\le\dfrac{b_{n+1}}{b_n}`$ for all $`n>N_0`$. Prove that convergence of $`\sum b_k`$ implies convergence of $`\sum a_k`$. Using this statement, prove that $`\sum\limits_{k=1}^\infty\dfrac1{k!}`$ converges.

**2.** Test the series for convergence:
```math
\text{a)}\ \sum_{k=1}^\infty\frac{(k!)^2}{(2k)!};\qquad\text{b)}\ \sum_{k=1}^\infty\frac{(2k-1)!!}{(2k+2)!!};\qquad\text{c)}\ \sum_{k=1}^\infty\frac{(-1)^k}{\ln(k+1)} .
```

<details>
<summary>Solutions of set A</summary>

**1.** Multiplying the inequality by $`\frac{a_n}{b_{n+1}}>0`$ gives $`\frac{a_{n+1}}{b_{n+1}}\le\frac{a_n}{b_n}`$ for $`n>N_0`$: the sequence $`\frac{a_n}{b_n}`$ is non-increasing, so $`a_n\le Cb_n`$ for $`n\ge N_0+1`$, where $`C=\frac{a_{N_0+1}}{b_{N_0+1}}`$. Let $`B`$ be the sum of $`\sum_{k>N_0}b_k`$ (it converges together with $`\sum b_k`$). Then $`\sum_{k=N_0+1}^na_k\le C\sum_{k=N_0+1}^nb_k\le CB`$. The partial sums of the positive series $`\sum_{k>N_0}a_k`$ are bounded, so it converges; adding finitely many terms does not change convergence.

Application: $`a_k=\frac1{k!}`$, $`b_k=\frac1{k(k+1)}`$ (the series $`\sum b_k`$ converges: its partial sums equal $`1-\frac1{n+1}`$). $`\frac{a_{k+1}}{a_k}=\frac1{k+1}`$, $`\frac{b_{k+1}}{b_k}=\frac k{k+2}`$; the inequality $`\frac1{k+1}\le\frac k{k+2}`$ is equivalent to $`k^2\ge2`$ and holds for $`k\ge2`$, i.e. $`N_0=1`$.

**2.** a) $`\dfrac{a_k}{a_{k+1}}=\dfrac{(2k+2)(2k+1)}{(k+1)^2}=\dfrac{2(2k+1)}{k+1}\ge3`$ for all $`k\ge1`$ (and tends to $`4`$). By d'Alembert's test with $`\beta=2`$ the series **converges**.

b) $`\dfrac{a_k}{a_{k+1}}=\dfrac{2k+4}{2k+1}=1+\dfrac3{2k+1}\to1`$ — d'Alembert does not work. $`R_k=\dfrac{3k}{2k+1}\to\dfrac32>1`$: by Raabe's test the series **converges**. (Without a limit: $`\frac3{2k+1}\ge\frac{5/4}k`$ for $`k\ge3`$, $`\gamma=\frac14`$.)

c) The signs alternate, $`\frac1{\ln(k+1)}`$ decreases and tends to zero: by Leibniz's test the series **converges**. There is no absolute convergence: $`\ln(k+1)\le k`$, so $`\frac1{\ln(k+1)}\ge\frac1k`$. The convergence is conditional.
</details>

### Set B

**1.** State and prove Leibniz's test. Does it remain true if the condition $`a_ka_{k+1}<0`$ is replaced by $`a_ka_{k+1}\le0`$?

**2.** Test the series for convergence ($`\alpha\in\mathbb R`$ is a parameter):
```math
\text{a)}\ \sum_{k=1}^\infty\frac{k^k}{3^k\,k!};\qquad\text{b)}\ \sum_{k=1}^\infty\frac{\sqrt{k^2+1}-k}{k^\alpha};\qquad\text{c)}\ \sum_{k=1}^\infty\frac{\sin\frac{k\pi}2}{\sqrt[3]k} .
```

<details>
<summary>Solutions of set B</summary>

**1.** *Statement.* If for all $`k`$ we have $`a_ka_{k+1}<0`$, $`|a_{k+1}|\le|a_k|`$ and $`a_k\to0`$, then the series $`\sum a_k`$ converges.

*Proof.* We may assume $`a_1>0`$ (otherwise multiply the series by $`-1`$); then $`a_{2j-1}>0`$, $`a_{2j}<0`$. The brackets $`a_{2j-1}+a_{2j}=|a_{2j-1}|-|a_{2j}|\ge0`$, so $`S_{2m}=\sum_{j=1}^m(a_{2j-1}+a_{2j})`$ is non-decreasing. On the other hand, $`S_{2m}=a_1+\sum_{j=1}^{m-1}(a_{2j}+a_{2j+1})+a_{2m}\le a_1`$, since $`a_{2j}+a_{2j+1}=-|a_{2j}|+|a_{2j+1}|\le0`$ and $`a_{2m}<0`$. The monotone bounded sequence $`S_{2m}`$ converges to some $`S`$. Then $`S_{2m+1}=S_{2m}+a_{2m+1}\to S`$, since $`a_k\to0`$. The subsequences with even and odd indices converge to the same limit, hence $`S_n\to S`$.

*The question.* Yes. If all $`a_k\ne0`$, the condition $`\le0`$ coincides with $`<0`$. If $`a_K=0`$, then $`|a_{k+1}|\le|a_k|`$ gives $`a_k=0`$ for $`k\ge K`$, and the series is a finite sum.

**2.** a) $`\dfrac{a_k}{a_{k+1}}=\dfrac{k^k}{3^kk!}\cdot\dfrac{3^{k+1}(k+1)!}{(k+1)^{k+1}}=\dfrac{3}{\bigl(1+\frac1k\bigr)^k}>\dfrac3e>1`$ for all $`k`$, since $`\bigl(1+\frac1k\bigr)^k<e`$. By d'Alembert's test with $`\beta=\frac3e-1`$ the series **converges**.

b) $`\sqrt{k^2+1}-k=\dfrac{1}{\sqrt{k^2+1}+k}`$, so $`a_k=\dfrac{C_k}{k^{\alpha+1}}`$, $`C_k=\dfrac{k}{\sqrt{k^2+1}+k}`$. Since $`k<\sqrt{k^2+1}\le\sqrt2\,k`$, we have $`\dfrac1{1+\sqrt2}\le C_k<\dfrac12`$. By problem 3.11 the series **converges for $`\alpha>0`$ and diverges for $`\alpha\le0`$**.

c) For even $`k`$ the terms are zero; for $`k=2j-1`$ the numerator is $`(-1)^{j-1}`$. The non-zero terms $`c_j=\dfrac{(-1)^{j-1}}{\sqrt[3]{2j-1}}`$ form a series that converges by Leibniz's test; inserting zeros does not change the partial sums ($`S_{2m-1}=S_{2m}=T_m`$). The series **converges** (conditionally: $`\sum\frac1{\sqrt[3]{2j-1}}`$ diverges).
</details>

### Set C

**1.** Let $`x_n>0`$ and $`a_n>0`$ for all $`n`$, and let there be $`\alpha>0`$ and $`N`$ such that $`x_n\dfrac{a_n}{a_{n+1}}-x_{n+1}\ge\alpha`$ for all $`n>N`$. Prove that the series $`\sum a_k`$ converges. Derive from this d'Alembert's convergence test. Why does d'Alembert's test say nothing about the series $`\sum\frac1{k^2}`$?

**2.** Test the series for convergence:
```math
\text{a)}\ \sum_{k=1}^\infty\Bigl(\frac{k+1}{2k+3}\Bigr)^k;\qquad\text{b)}\ \sum_{k=2}^\infty\frac{1}{k\ln^2k};\qquad\text{c)}\ \sum_{k=1}^\infty\frac{(-1)^kk}{k^2+1} .
```

<details>
<summary>Solutions of set C</summary>

**1.** Multiply the inequality by $`a_{n+1}>0`$: $`x_na_n-x_{n+1}a_{n+1}\ge\alpha a_{n+1}`$ for $`n>N`$. Add over $`n=N+1,\dots,N+m`$; the left-hand side telescopes:

```math
\alpha\sum_{n=N+1}^{N+m}a_{n+1}\le x_{N+1}a_{N+1}-x_{N+m+1}a_{N+m+1}<x_{N+1}a_{N+1}.
```

The partial sums of the positive series $`\sum_{k\ge N+2}a_k`$ are bounded by $`\frac{x_{N+1}a_{N+1}}{\alpha}`$, so it converges, and with it $`\sum a_k`$.

*D'Alembert.* Take $`x_n=1`$: the condition becomes $`\frac{a_n}{a_{n+1}}-1\ge\alpha`$, i.e. $`\frac{a_n}{a_{n+1}}\ge1+\beta`$ with $`\beta=\alpha`$. So if $`\frac{a_n}{a_{n+1}}\ge1+\beta`$ for $`n>N`$, $`\beta>0`$, the series converges.

*The series $`\sum\frac1{k^2}`$.* $`\frac{a_k}{a_{k+1}}=\bigl(1+\frac1k\bigr)^2\to1`$. This ratio exceeds $`1`$ for all $`k`$, so the divergence condition $`\frac{a_k}{a_{k+1}}\le1`$ fails; and it tends to $`1`$, so for no constant $`\beta>0`$ does $`\frac{a_k}{a_{k+1}}\ge1+\beta`$ hold for all large $`k`$. D'Alembert's test compares the series with a geometric progression, and $`\frac1{k^2}`$ decays slower than any progression. Raabe's test works here: $`\bigl(1+\frac1k\bigr)^2\ge1+\frac2k`$, $`\gamma=1`$.

**2.** a) $`\dfrac{k+1}{2k+3}<\dfrac12`$ for all $`k`$ (since $`2k+2<2k+3`$), so $`0<a_k<2^{-k}`$. By comparison with a geometric progression the series **converges**. (Cauchy's test: $`\sqrt[k]{a_k}\to\frac12<1`$.)

b) The function $`f(x)=\dfrac1{x\ln^2x}`$ is positive and decreasing on $`[2;+\infty)`$ (the denominator increases). $`\displaystyle\int_2^x\frac{dy}{y\ln^2y}=\frac1{\ln2}-\frac1{\ln x}\to\frac1{\ln2}`$. The integral converges, so by the integral test the series **converges**. (D'Alembert and Raabe are silent here: $`R_k\to1`$.)

c) The signs alternate. The absolute values $`\frac{k}{k^2+1}`$ decrease: the inequality $`\frac{k}{k^2+1}\ge\frac{k+1}{(k+1)^2+1}`$ is equivalent to $`k^2+k\ge1`$. The absolute values tend to zero. By Leibniz's test the series **converges**. There is no absolute convergence: $`\frac{k}{k^2+1}\ge\frac1{2k}`$. The convergence is conditional.
</details>

### What each set tests

| Problem | Set A | Set B | Set C |
|---|---|---|---|
| 1 | generalised comparison | Leibniz | Kummer ⟹ d'Alembert |
| 2 | d'Alembert, Raabe, Leibniz | d'Alembert with $`e`$, a parameter, Leibniz with zeros | comparison (Cauchy), integral test, Leibniz |

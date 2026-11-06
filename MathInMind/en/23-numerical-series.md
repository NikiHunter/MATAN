---
title: "Numerical Series"
lang: en
chapter: 23
part: "Semester 3: the lecturer's chapters"
numbering: lecture
lecturer_chapter: 7
---
# 23. Numerical Series

[← 22. Taylor's Formula in ℝⁿ, Implicit Maps, Extrema](22-taylor-implicit-extrema.md) · [Course index](index.md) · [Terms & theorems](term-index.md) · [24. Functional and Power Series →](24-functional-power-series.md)

> **Goal.** Present the lecturer's chapter 7 (§7.1–§7.5, [lectures 67–68](lectures-2025-26/lecture-67-68.md), [69–70](lectures-2025-26/lecture-69-70.md) and the beginning of [71–72](lectures-2025-26/lecture-71-72.md)), keeping the lecturer's numbering: convergence of a series and its properties, the [Bolzano–Cauchy criterion](03-sequences.md#sec-3-4), convergence tests for positive series, the Leibniz, Dirichlet and Abel tests, [rearrangements](04-numeric-series.md#rearrangement-warning) of series. The lecturer does not number the convergence tests, so here they are named. A condensed treatment of the same topics is in [chapter 4](04-numeric-series.md).

<a id="sec-7-1"></a>
## §7.1. Numerical series

> <a id="def-7-1-1"></a>**Definition 7.1.1.** Let a sequence $`(a_n)`$, $`a_n\in\mathbb R`$, $`n\in\mathbb N`$ be given. Then $`S_n=a_1+a_2+\ldots+a_n`$ is called a [partial sum](04-numeric-series.md#sec-4-1) of the series, $`S=\lim_{n\to\infty}S_n`$ the sum of the series; the notation $`S:=\sum_{n=1}^{\infty}a_n`$ is used for the sum; $`a_n`$ is called the general term of the series.

> <a id="def-7-1-2"></a>**Definition 7.1.2.** The series $`\sum_{n=1}^{\infty}a_n`$ converges if the sum of the series $`S`$ exists and is finite. Otherwise the series diverges.

Thus a series is the sequence of its partial sums, and its convergence is the convergence of this sequence. Examples: the series $`\sum_{k=1}^{\infty}1`$ diverges ($`S_n=n\to+\infty`$); the series $`\sum_{k=0}^{\infty}(-1)^k`$ diverges (its partial sums are alternately $`1`$ and $`0`$); the series with general term $`\frac{1}{k(k+1)}=\frac1k-\frac{1}{k+1}`$ converges, since
```math
S_n=\sum_{k=1}^{n}\Bigl(\frac1k-\frac1{k+1}\Bigr)=1-\frac{1}{n+1}\to1 .
```
The geometric series $`\sum_{k=0}^{\infty}q^k`$ converges for $`|q|<1`$ to $`\frac{1}{1-q}`$ and diverges for $`|q|\ge1`$.

<a id="sec-7-2"></a>
## §7.2. Properties of series

*Property 1 (necessary condition for convergence).* If the series $`\sum_{n=1}^{\infty}a_n`$ converges, then $`a_n\to0`$: indeed, $`a_n=S_n-S_{n-1}\to S-S=0`$. The converse is false: the harmonic series $`\sum_{k=1}^{\infty}\frac1k`$ diverges although $`\frac1k\to0`$; grouping the terms of the partial sum $`S_{2^m}`$ into blocks of length $`2^{j-1}`$ gives $`S_{2^m}\ge1+\frac m2`$.

*Property 2.* A series converges if and only if any (or at least one) of its remainders $`\sum_{n=k+1}^{\infty}a_n`$ converges; moreover, the remainder of a convergent series tends to zero as $`k\to\infty`$. Dropping or adding finitely many terms does not affect convergence.

*Properties 3 and 4 (linearity).* For $`k\ne0`$ the series $`\sum a_n`$ and $`\sum ka_n`$ converge or diverge together, and $`\sum ka_n=k\sum a_n`$; if the series $`\sum a_n`$ and $`\sum b_n`$ converge, then the series $`\sum(a_n+b_n)`$ converges and its sum equals $`\sum a_n+\sum b_n`$. The sum of a convergent and a divergent series diverges.

> **Bolzano–Cauchy criterion.** The series $`\sum_{n=1}^{\infty}a_n`$ converges if and only if
> ```math
> \forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n>N\ \forall p\in\mathbb N\qquad\Bigl|\sum_{k=n+1}^{n+p}a_k\Bigr|<\varepsilon .
> ```

This is the Cauchy criterion for the sequence $`(S_n)`$, since $`S_{n+p}-S_n=a_{n+1}+\ldots+a_{n+p}`$. Hence a way to prove divergence: find indices $`m_n>n`$ (often $`m_n=2n`$) with $`\sum_{k=n}^{m_n}a_k\not\to0`$. For the harmonic series $`\sum_{k=n}^{2n}\frac1k\ge\frac{n+1}{2n}>\frac12`$.

> <a id="def-7-2-1"></a>**Definition 7.2.1.** The series $`\sum_{n=1}^{\infty}a_n`$ is called [absolutely convergent](04-numeric-series.md#sec-4-3) if the series $`\sum_{n=1}^{\infty}|a_n|`$ converges.

An absolutely convergent series converges: by the triangle inequality $`|a_{n+1}+\ldots+a_{n+p}|\le|a_{n+1}|+\ldots+|a_{n+p}|`$, and the condition of the Bolzano–Cauchy criterion for $`\sum|a_n|`$ implies it for $`\sum a_n`$.

<a id="sec-7-3"></a>
## §7.3. Positive series

> <a id="def-7-3-1"></a>**Definition 7.3.1.** The series $`\sum_{n=1}^{\infty}a_n`$ is called positive if $`a_n\ge0`$ for all $`n`$.

The partial sums of a positive series do not decrease, so a positive series always has a sum (finite or $`+\infty`$), and it converges if and only if the sequence $`(S_N)`$ is bounded (boundedness of some subsequence $`(S_{N_k})`$ suffices).

> **First comparison test.** Let $`0\le a_n\le b_n`$ for all $`n`$. If the series $`\sum b_n`$ converges, then the series $`\sum a_n`$ converges too; if the series $`\sum a_n`$ diverges, then the series $`\sum b_n`$ diverges too.

> **Second comparison test.** Let $`a_n\ge0`$, $`b_n>0`$ and suppose that $`\lim_{n\to\infty}\frac{a_n}{b_n}=:L\in[0,+\infty]`$ exists. If $`L<+\infty`$, then convergence of $`\sum b_n`$ implies convergence of $`\sum a_n`$; if $`L>0`$, then convergence of $`\sum a_n`$ implies convergence of $`\sum b_n`$. For $`L\in(0,+\infty)`$ the series converge or diverge together.

> **D'Alembert's test.** Let $`a_n>0`$ and suppose that $`\lim_{n\to\infty}\frac{a_{n+1}}{a_n}=:D`$ exists. If $`D<1`$, the series converges; if $`D>1`$, the series diverges; for $`D=1`$ (or if there is no limit) the test gives no answer.

> **Cauchy's test.** Let $`a_n>0`$ and suppose that $`\lim_{n\to\infty}\sqrt[n]{a_n}=:C`$ exists. If $`C<1`$, the series converges; if $`C>1`$, the series diverges; for $`C=1`$ (or if there is no limit) the test gives no answer.

In both tests, when the value is less than one, the series is compared with a geometric progression with ratio $`q=\frac{1+D}{2}`$ (respectively $`q=\frac{1+C}{2}`$); when the value is greater than one, the necessary condition $`a_n\to0`$ fails. The series $`\sum\frac1n`$ and $`\sum\frac1{n^2}`$ show that both outcomes are possible when the value is $`1`$.

> **Cauchy's lemma (condensation).** Let $`a_n\ge a_{n+1}\ge0`$ for all $`n`$. Then the series $`\sum_{n=1}^{\infty}a_n`$ converges if and only if the series $`\sum_{n=1}^{\infty}2^na_{2^n}`$ converges.

*Proof idea.* The block of indices $`2^{k-1}+1,\ldots,2^k`$ contains exactly $`2^{k-1}`$ terms, each lying between $`a_{2^k}`$ and $`a_{2^{k-1}}`$; summing over the blocks gives $`\frac12T_m\le S_{2^m}`$ and $`S_{2^{m+1}-1}\le a_1+T_m`$, where $`T_m=\sum_{k=1}^{m}2^ka_{2^k}`$.

For $`a_n=\frac1{n^p}`$, $`p>0`$, the condensed series is a geometric progression with ratio $`2^{1-p}`$, so
```math
\sum_{n=1}^{\infty}\frac{1}{n^p}\quad\text{converges for } p>1\text{ and diverges for } p\le1 .
```

<a id="sec-7-4"></a>
## §7.4. Series with terms of arbitrary sign

> <a id="def-7-4-1"></a>**Definition 7.4.1.** If the series $`\sum_{n=1}^{\infty}a_n`$ converges while the corresponding series $`\sum_{n=1}^{\infty}|a_n|`$ diverges, then the original series $`\sum_{n=1}^{\infty}a_n`$ is called conditionally convergent.

> **Leibniz test.** Let $`c_n>0`$, $`c_{n+1}\le c_n`$ for all $`n`$ and $`c_n\to0`$. Then the alternating series $`\sum_{n=0}^{\infty}(-1)^nc_n`$ converges, and its remainder $`R_n=\sum_{k=n+1}^{\infty}(-1)^kc_k`$ satisfies the estimate $`|R_n|\le c_{n+1}`$.

*Proof idea.* The odd partial sums $`S_{2m+1}`$ do not decrease and lie between $`0`$ and $`c_0`$, so they have a limit $`S`$; the even ones differ from them by $`c_{2m+2}\to0`$. For example, $`\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k}=\ln2`$: $`S_{2n}=H_{2n}-H_n`$, where $`H_n=1+\frac12+\ldots+\frac1n=\ln n+\gamma+o(1)`$.

> **Abel transformation.** Let $`(a_k)`$, $`(b_k)`$ be numerical sequences, $`B_k=b_1+\ldots+b_k`$, $`B_0:=0`$. Then for $`m>n\ge0`$
> ```math
> \sum_{k=n+1}^{m}a_kb_k=a_mB_m-a_{n+1}B_n+\sum_{k=n+1}^{m-1}(a_k-a_{k+1})B_k .
> ```

This is a discrete analogue of [integration by parts](08-riemann-integration.md#sec-8-4): substitute $`b_k=B_k-B_{k-1}`$ and regroup.

> **Dirichlet test.** Let $`a_n\downarrow0`$ (i.e. $`a_{n+1}\le a_n`$ and $`a_n\to0`$) and let the partial sums $`B_n=b_1+\ldots+b_n`$ be bounded: $`|B_n|\le M`$ for all $`n`$. Then the series $`\sum_{n=1}^{\infty}a_nb_n`$ converges.

By the Abel transformation $`\bigl|\sum_{k=n+1}^{m}a_kb_k\bigr|\le2Ma_{n+1}`$, and the Bolzano–Cauchy criterion holds. The [Leibniz test](04-numeric-series.md#alternating-series-test) is a special case: $`b_n=(-1)^n`$.

> **Abel test.** Let the sequence $`(a_n)`$ be monotone and bounded, and let the series $`\sum_{n=1}^{\infty}b_n`$ converge. Then the series $`\sum_{n=1}^{\infty}a_nb_n`$ converges.

It reduces to the Dirichlet test: if $`a_n\to a`$ monotonically, then $`a_nb_n=(a_n-a)b_n+ab_n`$, and $`|a_n-a|\downarrow0`$.

<a id="sec-7-5"></a>
## §7.5. Rearrangements of series

> <a id="def-7-5-1"></a>**Definition 7.5.1.** Let a series $`\sum_{n=1}^{\infty}a_n`$ and a [bijective](01-logic-sets-functions.md#sec-1-4) map $`\sigma:\mathbb N\to\mathbb N`$ be given. The series $`\sum_{n=1}^{\infty}a_{\sigma(n)}`$ is called a rearrangement of the original series $`\sum_{n=1}^{\infty}a_n`$.

> <a id="def-7-5-2"></a>**Definition 7.5.2.** We say that the series $`\sum_{n=1}^{\infty}a_n`$ has the commutative property if for every bijection $`\sigma:\mathbb N\to\mathbb N`$ the series $`\sum_{n=1}^{\infty}a_{\sigma(n)}`$ converges or diverges together with the original series and, moreover,
> ```math
> \sum_{n=1}^{\infty}a_n=\sum_{n=1}^{\infty}a_{\sigma(n)} .
> ```

The lecturer's example: if in the series $`1-\frac12+\frac13-\frac14+\ldots=\ln2`$ every positive term is followed by two negative ones,
```math
1-\frac12-\frac14+\frac13-\frac16-\frac18+\frac15-\frac1{10}-\frac1{12}+\ldots ,
```
then the partial sums $`T_{3m}`$ equal $`\frac12S_{2m}`$, and the sum of the rearranged series is $`\frac12\ln2`$.

> **Commutative properties of series.**
> 1. Positive series have the commutative property.
> 2. Absolutely convergent series have the commutative property.
> 3. (Riemann's theorem.) A conditionally convergent series does not have the commutative property: for every $`B\in\overline{\mathbb R}`$ there is a bijection $`\sigma`$ with $`\sum_{n=1}^{\infty}a_{\sigma(n)}=B`$.

For item 2 the series is split into its positive and negative parts $`a_n=a_n^+-a_n^-`$, each of which converges and is rearranged by item 1. For item 3 both parts diverge to $`+\infty`$, while $`a_n\to0`$: positive terms are taken until the sum exceeds $`B`$, then negative ones until the sum becomes less than $`B`$, and so on.

## Worked example

**The series $`\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^p}`$.** For $`p>1`$ the series of absolute values $`\sum\frac1{n^p}`$ converges ([Cauchy's lemma](#sec-7-3)), and the series converges absolutely. For $`0<p\le1`$ the numbers $`\frac1{n^p}`$ decrease monotonically to zero, so the series converges by the Leibniz test, while the series of absolute values diverges: the convergence is conditional, and by Riemann's theorem a rearrangement can produce any sum. For $`p\le0`$ the general term does not tend to zero, so the series diverges.

**The series $`\sum_{n=1}^{\infty}\frac{\sin n}{n}`$.** The partial sums of the sines are bounded:
```math
\Bigl|\sum_{k=1}^{n}\sin k\Bigr|=\Bigl|\frac{\sin\frac n2\,\sin\frac{n+1}{2}}{\sin\frac12}\Bigr|\le\frac{1}{\sin\frac12},
```
and $`\frac1n\downarrow0`$, so the series converges by the [Dirichlet test](#sec-7-4). The convergence is conditional: $`\frac{|\sin n|}{n}\ge\frac{\sin^2n}{n}=\frac{1}{2n}-\frac{\cos2n}{2n}`$, where $`\sum\frac{\cos2n}{2n}`$ converges (the Dirichlet test again) and $`\sum\frac1{2n}`$ diverges.

## Common pitfalls

1. Treating the condition $`a_n\to0`$ as sufficient for convergence (the harmonic series).
2. Drawing a conclusion from the d'Alembert or Cauchy test when the limit equals $`1`$.
3. Applying [comparison tests](04-numeric-series.md#sec-4-2) to series whose terms change sign: they are proved only for positive series.
4. Forgetting monotonicity in the Leibniz test: the series with terms $`\frac{1}{\sqrt n}`$ in odd places and $`-\frac1n`$ in even places alternates and its terms tend to zero, but it diverges.
5. Rearranging or regrouping the terms of a conditionally convergent series as if it were a finite sum: a rearrangement can change the sum.

## Exercises

1. Investigate the convergence of the series $`\sum_{n=1}^{\infty}\frac{n!}{n^n}`$.
2. Investigate the convergence of the series $`\sum_{n=2}^{\infty}\frac{1}{n\ln n}`$.
3. Does the series $`\sum_{n=1}^{\infty}\frac{(-1)^n}{\sqrt n}`$ converge absolutely? conditionally?
4. Prove that the series $`\sum_{n=1}^{\infty}\frac{\cos n}{n}`$ converges.

<details>
<summary>Short answers</summary>

1. It converges by d'Alembert's test: $`\frac{a_{n+1}}{a_n}=\bigl(1+\frac1n\bigr)^{-n}\to\frac1e<1`$.
2. It diverges: the terms decrease monotonically, and the condensed series $`\sum\frac{2^n}{2^nn\ln2}=\sum\frac{1}{n\ln2}`$ diverges (Cauchy's lemma).
3. It converges conditionally: the Leibniz test gives convergence, while $`\sum\frac1{\sqrt n}`$ diverges ($`p=\frac12\le1`$).
4. The Dirichlet test: $`\frac1n\downarrow0`$, and $`\bigl|\sum_{k=1}^{n}\cos k\bigr|\le\frac{1}{\sin\frac12}`$.
</details>

---

[← 22. Taylor's Formula in ℝⁿ, Implicit Maps, Extrema](22-taylor-implicit-extrema.md) · [Course index](index.md) · [Terms & theorems](term-index.md) · [24. Functional and Power Series →](24-functional-power-series.md)

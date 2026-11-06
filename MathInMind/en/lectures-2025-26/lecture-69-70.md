---
title: "Lectures 69–70 — positive series, convergence tests, series with terms of arbitrary sign, rearrangements"
lang: en
course: "Mathematical Analysis, 2025/26"
lecture: 69-70
semester: 3
source: "handwritten notebook, pages p022–p029"
source_pages: "p022, p023, p024, p025, p026, p027, p028, p029"
course_chapter: 23
---
# Lectures 69–70 — positive series, convergence tests, series with terms of arbitrary sign, rearrangements

[← Lectures 67–68](lecture-67-68.md) · [Lecture index](index.md) · [Lectures 71–72 →](lecture-71-72.md) · [Terms & theorems](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-69-70.md) · [Español](../../es/lectures-2025-26/lecture-69-70.md)

> **Source and numbering.** These notes were copied from a handwritten notebook (pages p022–p029; the raw page text is in [`ocr/raw/`](../../../ocr/raw/p022.md)). Page p022 contains only the heading “Lectures 69–70” and a short two-item plan of the class, read only partially (“… conv.”, “Oth. ex. covered”); the rest of the page is empty. Therefore the definition of a positive series and the statements of its properties, whose proofs begin on page p023, are restored from the slides of the 2024/25 course. Between pages p025 and p026 the statement of the Cauchy test and the beginning of its proof are lost, between pages p028 and p029 [Abel's transformation](../23-numerical-series.md#sec-7-4), the Dirichlet test and the statement of the Abel test; these places are restored as well. The numbering of definitions is the lecturer's; the lecturer does not number the convergence tests. Slips in the notes are corrected and marked with “Source correction” blocks; lost passages are restored and marked with “Restored” blocks; the tags match [`ocr/RESOLVED.md`](../../../ocr/RESOLVED.md). Places that still have to be checked against the notebook are listed in [`ocr/ISSUES.md`](../../../ocr/ISSUES.md).

## §7.3. Positive series

<a id="p022"></a>

> **Restored** (from the slides of the 2024/25 course, FS p54; cf. the 2022 notes, M3S p40). Page p022 of the notebook is empty after the heading and the plan; below are the definition and the properties whose proofs are written on page p023.
>
> <a id="def-7-3-1"></a>**Definition 7.3.1.** A series $`\sum_{n=1}^{\infty}a_n`$ is called positive if $`a_n\ge0`$ for all $`n`$.
>
> **Properties.**
>
> 1. Every positive series has a sum (finite or infinite).
> 2. A positive series converges if and only if the sequence of its [partial sums](../04-numeric-series.md#sec-4-1) $`(S_N)_{N\in\mathbb N}`$ is bounded.

<a id="p023"></a>

**Proof of property 2.** Let $`S_N=\sum_{n=1}^{N}a_n`$. The sequence $`(S_N)`$ is non-decreasing, since $`S_{N+1}-S_N=a_{N+1}\ge0`$. By the theorem on the limit of a [monotone sequence](lecture-11-12.md#def-2-3-5), a non-decreasing sequence converges if and only if it is [bounded above](lecture-05-06.md#def-1-3-7); since moreover $`S_N\ge0`$, the convergence of $`(S_N)`$, i.e. the convergence of the series, is equivalent to the boundedness of $`(S_N)`$. $`\square`$

**Proof of property 1.** By the theorem on the limit of a monotone sequence, the non-decreasing sequence $`(S_N)`$ has a limit — finite or equal to $`+\infty`$. Hence either the series $`\sum_{n=1}^{\infty}a_n`$ converges, or $`S:=\lim_{N\to\infty}S_N=+\infty`$. $`\square`$

> **Source correction** (S090). The notes have the heading “Pf (prop. II)”. What is proved here is property 1 (the existence of the sum); this item is labelled so in the lecturer's notes as well (FS p54, M3S p40).

**Remark.** For the sequence $`(S_N)`$ to be bounded above it suffices that some [subsequence](lecture-11-12.md#def-2-3-7) $`(S_{N_k})`$ of it be bounded above. Indeed, let $`S_{N_k}\le M`$ for all $`k`$. For every $`N`$ one can find $`k`$ such that $`N_k>N`$, and then, since $`(S_N)`$ is non-decreasing, $`S_N\le S_{N_k}\le M`$.

### The first comparison test

Let two positive series $`\sum_{n=1}^{\infty}a_n`$ and $`\sum_{n=1}^{\infty}b_n`$ be given ($`a_n\ge0`$, $`b_n\ge0`$ for all $`n`$), and let $`b_n\ge a_n`$ for all $`n`$. Then:

1. if the series $`\sum_{n=1}^{\infty}b_n`$ converges, the series $`\sum_{n=1}^{\infty}a_n`$ converges;
2. if the series $`\sum_{n=1}^{\infty}a_n`$ diverges, the series $`\sum_{n=1}^{\infty}b_n`$ diverges.

**Proof.** Put $`A_N=\sum_{n=1}^{N}a_n`$, $`B_N=\sum_{n=1}^{N}b_n`$. Since $`a_n\le b_n`$ for all $`n`$, we have $`A_N\le B_N`$ for all $`N`$.

1. Let the series $`\sum b_n`$ converge, i.e. $`B_N\to B<+\infty`$. The sequence $`(B_N)`$ is non-decreasing, so $`B_N\le B`$ and $`A_N\le B_N\le B`$ for all $`N`$. The non-decreasing sequence $`(A_N)`$ is bounded above, hence there is a finite limit $`\lim_{N\to\infty}A_N\le B<+\infty`$, i.e. the series $`\sum a_n`$ converges.
2. Statement 2 is equivalent to statement 1 (it is its contrapositive): if the series $`\sum b_n`$ converged, then by item 1 the series $`\sum a_n`$ would converge too. $`\square`$

<a id="p024"></a>

### The second comparison test

Let two positive series $`\sum_{n=1}^{\infty}a_n`$ and $`\sum_{n=1}^{\infty}b_n`$ be given, with $`b_n>0`$ for all $`n`$. If the limit $`\lim_{n\to\infty}\frac{a_n}{b_n}=:L`$ exists (finite or equal to $`+\infty`$), then:

1. if $`L<+\infty`$, i.e. $`L\in[0,+\infty)`$, the convergence of the series $`\sum_{n=1}^{\infty}b_n`$ implies the convergence of the series $`\sum_{n=1}^{\infty}a_n`$;
2. if $`L>0`$, i.e. $`L\in(0,+\infty]`$, the convergence of the series $`\sum_{n=1}^{\infty}a_n`$ implies the convergence of the series $`\sum_{n=1}^{\infty}b_n`$.

**Remark.** If $`L\in(0,+\infty)`$, the series $`\sum_{n=1}^{\infty}a_n`$ and $`\sum_{n=1}^{\infty}b_n`$ converge and diverge simultaneously.

**Proof.**

1. Since $`\frac{a_n}{b_n}\to L<+\infty`$, the sequence $`\left(\frac{a_n}{b_n}\right)`$ is bounded: there is $`M`$ such that $`\frac{a_n}{b_n}\le M`$, i.e. $`a_n\le Mb_n`$, for all $`n`$. If the series $`\sum b_n`$ converges, the series $`\sum Mb_n`$ converges too, and then by the first comparison test the series $`\sum a_n`$ converges.
2. Since $`\frac{a_n}{b_n}\to L>0`$, starting from some index $`K`$ we have $`a_n\ge cb_n`$ with a constant $`c>0`$ (one can take $`c=L/2`$ for $`L<+\infty`$ and $`c=1`$ for $`L=+\infty`$). Hence for $`n>K`$ we have $`a_n\ge cb_n>0`$ and $`b_n\le\frac1c\,a_n`$. This is item 1 with the roles of $`a_n`$ and $`b_n`$ exchanged: by the first comparison test applied to the terms with indices $`n>K`$ (discarding finitely many terms does not affect convergence), the convergence of $`\sum a_n`$ implies the convergence of $`\sum b_n`$. $`\square`$

<a id="p025"></a>

### The d'Alembert test

D'Alembert's convergence test. Let $`\sum_{n=1}^{\infty}a_n`$ be a series with positive terms ($`a_n>0`$), and let the limit $`\lim_{n\to\infty}\frac{a_{n+1}}{a_n}=:D`$ exist. Then:

1. if $`D<1`$, the series $`\sum_{n=1}^{\infty}a_n`$ converges;
2. if $`D>1`$, the series $`\sum_{n=1}^{\infty}a_n`$ diverges;
3. if $`D=1`$ or the limit $`D`$ does not exist, the series has to be studied further by other means.

A note in the margin says that the case “the limit does not exist” is separate: the test in this form then asserts nothing.

**Proof.**

1. Let $`D<1`$; put $`q:=\frac{1+D}{2}`$. By the definition of the limit, for every $`\varepsilon>0`$ starting from some index we have $`\left|\frac{a_{n+1}}{a_n}-D\right|<\varepsilon`$. Take $`\varepsilon:=\frac{1-D}{2}>0`$; there is $`N`$ such that for all $`n\ge N`$
```math
\frac{a_{n+1}}{a_n}<D+\varepsilon=D+\frac{1-D}{2}=\frac{1+D}{2}=q .
```
Since $`0\le D<1`$, we have $`q\in\left[\tfrac12,1\right)`$.

> **Source correction** (S101). The notes say “$`q\in(1/2;1)`$”. For $`D=0`$ one gets $`q=\frac12`$, so $`q\in\left[\frac12,1\right)`$; all that matters in the proof is that $`q<1`$.

Thus $`a_{n+1}<qa_n`$ for all $`n\ge N`$, whence by [induction](../01-logic-sets-functions.md#example-induction) $`a_n\le q^{\,n-N}a_N`$ for all $`n\ge N`$. Compare the series $`\sum_n a_n`$ and $`\sum_n q^{\,n-N}a_N=a_Nq^{-N}\sum_n q^n`$: the latter converges, being a geometric progression with ratio $`q\in(0,1)`$. By the first comparison test (applied to the terms with indices $`n\ge N`$) the series $`\sum_{n=1}^{\infty}a_n`$ converges.

2. Let $`D>1`$. Then there is $`M`$ such that $`\frac{a_{n+1}}{a_n}>1`$, i.e. $`a_{n+1}>a_n`$, for all $`n\ge M`$. Consequently $`a_n\ge a_M>0`$ for all $`n\ge M`$, hence $`a_n\not\to0`$, and the series $`\sum_{n=1}^{\infty}a_n`$ diverges by the necessary condition for convergence.

3. For $`D=1`$ both cases are possible. The series $`\sum_{k=1}^{\infty}\frac1{k^2}`$ converges, and $`\frac{a_{k+1}}{a_k}=\frac{k^2}{(k+1)^2}\to1`$; the series $`\sum_{k=1}^{\infty}\frac1k`$ diverges, and $`\frac{a_{k+1}}{a_k}=\frac{k}{k+1}\to1`$. $`\square`$

> **Source correction** (T505). In the notes the inequality $`a_{n+1}<qa_n`$, known for $`n>N`$, is used to derive “$`a_n<q^{n-N}a_N`$ $`\forall n>N`$” (this needs the further step $`n=N`$); in item 2 “$`a_n>a_M>0`$ for $`n>M`$” is written similarly, and the line “$`a_{n+1}<qa_n`$ $`\forall q\in(1/2,1)`$” contains a superfluous [quantifier](../01-logic-sets-functions.md#sec-1-1) over $`q`$ (the number $`q`$ is fixed). The indices $`N`$ and $`M`$ are chosen so that the inequalities hold for $`n\ge N`$ (respectively $`n\ge M`$); this is always possible, and the conclusions do not change.

### The Cauchy test

> **Restored** (from the slides of the 2024/25 course, FS p55; the 2022 notes, M3S p47). The statement of the Cauchy test and the beginning of its proof are lost in the notebook (between pages p025 and p026); the end of item 2 and item 3 of the proof have survived.
>
> *Cauchy's convergence test.* Let $`\sum_{n=1}^{\infty}a_n`$ be a series with positive terms ($`a_n>0`$), and let the limit $`\lim_{n\to\infty}\sqrt[n]{a_n}=:C`$ exist. Then:
>
> 1. if $`C<1`$, the series $`\sum_{n=1}^{\infty}a_n`$ converges;
> 2. if $`C>1`$, the series $`\sum_{n=1}^{\infty}a_n`$ diverges;
> 3. if $`C=1`$ or the limit $`C`$ does not exist, the series has to be studied further by other means.
>
> **Proof.**
>
> 1. Let $`C<1`$. Take $`\varepsilon:=\frac{1-C}{2}>0`$; there is $`N`$ such that for all $`n>N`$ we have $`\sqrt[n]{a_n}-C<\varepsilon`$, i.e. $`\sqrt[n]{a_n}<C+\varepsilon=\frac{1+C}{2}=:q`$, where $`q\in(0,1)`$. Then $`a_n<q^n`$ for $`n>N`$; the series $`\sum q^n`$ converges (a geometric progression), and by the first comparison test the series $`\sum a_n`$ converges.
> 2. Let $`C>1`$. Then there is $`M`$ such that $`\sqrt[n]{a_n}>1`$, i.e. $`a_n>1`$, for all $`n>M`$. Consequently $`a_n\not\to0`$ for $`n\to\infty`$.

<a id="p026"></a>

Hence the series $`\sum_{n=1}^{\infty}a_n`$ diverges by the necessary condition for convergence.

3. The series $`\sum_{n=1}^{\infty}\frac1{n^2}`$ converges, the series $`\sum_{n=1}^{\infty}\frac1n`$ diverges, but for both series $`\lim_{n\to\infty}\sqrt[n]{a_n}=1`$:
```math
\sqrt[n]{\frac1{n^2}}=\frac1{\left(\sqrt[n]{n}\right)^2}\to1,\qquad \sqrt[n]{\frac1n}=\frac1{\sqrt[n]{n}}\to1,
```
since $`\sqrt[n]{n}\to1`$. Hence for $`C=1`$ the test allows no conclusion. $`\square`$

> **Source correction** (T105). In the second line of item 3 the notes say “$`\sum1/n`$ — div., $`\sum1/n^2`$ — conv.”, i.e. the limit of the root is not given for the divergent series. In accordance with the example (and with the lecturer's note, FS p55) it must be noted that $`\lim\sqrt[n]{1/n}=1`$ holds for $`\sum\frac1n`$ as well; added.

### Cauchy's lemma

Let $`a_n\ge a_{n+1}\ge0`$ for all $`n`$. Then the series $`\sum_{n=1}^{\infty}a_n`$ converges if and only if the series $`\sum_{n=1}^{\infty}2^na_{2^n}`$ converges.

**Idea of the proof.** Each of the terms $`a_1,a_2,\dots,a_{2^n}`$ is at least $`a_{2^n}`$, so the sum of $`2^n`$ terms $`a_{2^n}`$ is estimated as follows:
```math
2^na_{2^n}=\underbrace{a_{2^n}+a_{2^n}+\dots+a_{2^n}}_{2^n}\le a_1+a_2+\dots+a_{2^n-1}+a_{2^n}.
```

> **Source correction** (S108). In the transcription of the notebook the right-hand side is written as “$`a_{2^n}+a_{2^n+1}+\ldots+a_{2^{n+1}}+a_1`$”. In this form the estimate is false: the terms with indices greater than $`2^n`$ do not exceed $`a_{2^n}`$ (for example, for $`a_k=1`$ with $`k\le2^n`$ and $`a_k=0`$ for $`k>2^n`$ the right-hand side equals $`2`$, while the left-hand side is $`2^n>2`$ for $`n\ge2`$). Corrected according to the lecturer's notes (FS p56, M3S p49).

> **Restored** (by the standard proof, cf. Zorich/Fichtenholz; on the 2024/25 slide the lecturer left the proof as an exercise: “Finish the proof”).
>
> **Proof.** Write $`S_N=\sum_{n=1}^{N}a_n`$ and $`T_m=\sum_{k=1}^{m}2^ka_{2^k}`$. Split the terms of the series into blocks. The block with indices $`2^{k-1}+1,\dots,2^k`$ ($`k\ge1`$) contains exactly $`2^{k-1}`$ terms, each at least $`a_{2^k}`$; the block with indices $`2^k,\dots,2^{k+1}-1`$ ($`k\ge0`$) contains exactly $`2^k`$ terms, each at most $`a_{2^k}`$. Therefore
> ```math
> 2^{k-1}a_{2^k}\le a_{2^{k-1}+1}+\dots+a_{2^k},\qquad a_{2^k}+\dots+a_{2^{k+1}-1}\le2^ka_{2^k}.
> ```
> Summing the first inequality over $`k=1,\dots,m`$ and the second over $`k=0,\dots,m`$, we get
> ```math
> \tfrac12\,T_m\le S_{2^m}-a_1\le S_{2^m},\qquad S_{2^{m+1}-1}\le a_1+T_m .
> ```
> If the series $`\sum a_n`$ converges to $`S`$, then $`T_m\le2S_{2^m}\le2S`$ for all $`m`$: the partial sums of the positive series $`\sum2^ka_{2^k}`$ are bounded, and by property 2 of positive series it converges. Conversely, if the series $`\sum2^ka_{2^k}`$ converges to $`T`$, then $`S_{2^{m+1}-1}\le a_1+T`$ for all $`m`$; by the remark to the properties of positive series (boundedness of a subsequence of partial sums suffices) the sequence $`(S_N)`$ is bounded, and the series $`\sum a_n`$ converges. $`\square`$
>
> **Example.** Let $`p>0`$ and $`a_n=\frac1{n^p}`$. Then $`2^na_{2^n}=\left(2^{1-p}\right)^n`$, and the series $`\sum2^na_{2^n}`$ is a geometric progression with ratio $`2^{1-p}`$; it converges for $`p>1`$ and diverges for $`p\le1`$. By [Cauchy's lemma](../23-numerical-series.md#sec-7-3) the series $`\sum_{n=1}^{\infty}\frac1{n^p}`$ converges for $`p>1`$ and diverges for $`0<p\le1`$ (for $`p\le0`$ it diverges, since $`\frac1{n^p}\not\to0`$). In particular, the series $`\sum\frac1{n^2}`$ converges and $`\sum\frac1n`$ diverges — these facts are used in the examples to the d'Alembert and Cauchy tests.

## §7.4. Series with terms of arbitrary sign

<a id="def-7-4-1"></a>**Definition 7.4.1.** If the series $`\sum_{n=1}^{\infty}a_n`$ converges while the corresponding series $`\sum_{n=1}^{\infty}|a_n|`$ diverges, the original series $`\sum_{n=1}^{\infty}a_n`$ is called conditionally convergent.

<a id="p027"></a>

Now consider series of the form $`\sum_{n=0}^{\infty}(-1)^nc_n`$, $`c_n\ge0`$, whose terms change sign alternately. Such series are more often called alternating.

### The Leibniz test

Let $`c_n>0`$ for all $`n`$ and $`c_n\downarrow0`$, i.e. $`c_{n+1}\le c_n`$ for all $`n`$ and $`c_n\to0`$ as $`n\to\infty`$. Then the series $`\sum_{n=0}^{\infty}(-1)^nc_n`$ converges. Moreover, the remainder of the series $`R_n:=\sum_{k=n+1}^{\infty}(-1)^kc_k`$ satisfies the estimate $`|R_n|\le c_{n+1}`$.

**Example.** $`1-\frac12+\frac13-\frac14+\dots+\frac{(-1)^{n+1}}{n}+\dots=\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}=\ln2`$ (the sum is computed below).

**Proof.** Write $`S_n=\sum_{k=0}^{n}(-1)^kc_k`$ and consider the partial sums with odd indices. They are non-decreasing:
```math
S_{2m+1}-S_{2m-1}=\sum_{n=0}^{2m+1}(-1)^nc_n-\sum_{n=0}^{2m-1}(-1)^nc_n=c_{2m}-c_{2m+1}\ge0 .
```
They are bounded above by the number $`c_0`$:
```math
S_{2m+1}=c_0-c_1+c_2-c_3+\dots+c_{2m}-c_{2m+1}=c_0+(c_2-c_1)+(c_4-c_3)+\dots+(c_{2m}-c_{2m-1})-c_{2m+1}\le c_0,
```
since every bracket is non-positive ($`c_{n+1}\le c_n`$) and $`-c_{2m+1}\le0`$.

> **Source correction** (M504). The notes say “$`\ldots=c_0+(c_2-c_1)+(c_4-c_3)+\ldots+(c_{2m}-c_{2m+1})\le c_0`$”. With this grouping the last bracket is $`(c_{2m}-c_{2m-1})`$, and the term $`-c_{2m+1}`$ stays separate (as in the lecturer's notes: M3S p51, FS p57); moreover the bracket $`(c_{2m}-c_{2m+1})`$ is non-negative, not $`\le0`$ as noted in the margin.

> **Restored** (from the slides of the 2024/25 course, FS p57; the 2022 notes, M3S p52). Completion of the proof. The non-decreasing sequence $`(S_{2m+1})`$, bounded above, has a finite limit by the theorem on the limit of a monotone sequence: $`S_{2m+1}\to S`$ as $`m\to\infty`$. Next, $`S_{2m+2}=S_{2m+1}+c_{2m+2}\to S`$, since $`c_n\to0`$. The partial sums with even and with odd indices tend to the same number $`S`$, hence $`S_n\to S`$, i.e. the series $`\sum_{n=0}^{\infty}(-1)^nc_n`$ converges. The estimate of the remainder is proved below, in remark 2. $`\square`$

**Remark 1.** Grouping the terms differently, we get
```math
S_{2m+1}=(c_0-c_1)+(c_2-c_3)+\dots+(c_{2m}-c_{2m+1})\ge0,
```
since every bracket is non-negative. Together with the estimate $`S_{2m+1}\le c_0`$ this gives $`0\le S_{2m+1}\le c_0`$. Passing to the limit in the inequalities as $`m\to\infty`$ (the limit exists by the theorem on the limit of a monotone sequence), we get $`0\le S\le c_0`$: the sum of a Leibniz series lies between zero and its first term.

**Remark 2.** Let us estimate the remainder of the Leibniz series $`R_n=\sum_{k=n+1}^{\infty}(-1)^kc_k`$.

<a id="p028"></a>

We have
```math
|R_n|=|S-S_n|=\bigl|(-1)^{n+1}(S-S_n)\bigr|\le c_{n+1}.
```

> **Restored** (by the standard proof). Justification of the last inequality: $`(-1)^{n+1}R_n=\sum_{j=0}^{\infty}(-1)^jc_{n+1+j}=c_{n+1}-c_{n+2}+c_{n+3}-\dots`$ is a series of the same kind with terms $`c_{n+1}\ge c_{n+2}\ge\dots\to0`$ and first term $`c_{n+1}`$. By remark 1 its sum lies in the segment $`[0,c_{n+1}]`$, i.e. $`0\le(-1)^{n+1}(S-S_n)\le c_{n+1}`$.

**Example.** Let us compute the sum of the series $`\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k}=1-\frac12+\frac13-\frac14+\dots`$ (it converges by the Leibniz test). Write each negative term in the form $`-\frac1{2k}=\frac1{2k}-2\cdot\frac1{2k}`$ (for example, $`-\frac12=\frac12-2\cdot\frac12`$, $`-\frac14=\frac14-2\cdot\frac14`$); then for a partial sum with an even index
```math
S_{2n}=1-\frac12+\dots+\frac1{2n-1}-\frac1{2n}=1+\frac12+\frac13+\dots+\frac1{2n-1}+\frac1{2n}-2\left(\frac12+\frac14+\dots+\frac1{2n}\right).
```
Put $`H_n=1+\frac12+\dots+\frac1n`$. Then $`H_{2n}=1+\frac12+\dots+\frac1{2n-1}+\frac1{2n}`$ and $`2\left(\frac12+\frac14+\dots+\frac1{2n}\right)=H_n`$, i.e.
```math
S_{2n}=H_{2n}-H_n .
```
By the Euler–[Maclaurin formula](../07-taylor-convexity.md#sec-7-3) for the asymptotics of sums
```math
H_n=\ln n+C_0+\delta_n,\qquad \delta_n\to0,
```
where $`C_0=\gamma\approx0{,}5772`$ is Euler's constant.

> **Restored** (in the notes the computation breaks off at this formula; completed by the standard argument). Substituting, we get
> ```math
> S_{2n}=H_{2n}-H_n=\bigl(\ln(2n)+C_0+\delta_{2n}\bigr)-\bigl(\ln n+C_0+\delta_n\bigr)=\ln2+\delta_{2n}-\delta_n\xrightarrow[n\to\infty]{}\ln2,
> ```
> and $`S_{2n+1}=S_{2n}+\frac1{2n+1}\to\ln2`$. Hence $`S_n\to\ln2`$, i.e.
> ```math
> \sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k}=\ln2 .
> ```
> Without Euler's constant one can argue as follows: $`H_{2n}-H_n=\sum_{j=1}^{n}\frac1{n+j}=\frac1n\sum_{j=1}^{n}\frac1{1+j/n}`$ is an [integral sum](lecture-37-38.md#def-4-2-4) of the function $`\frac1{1+x}`$ on $`[0,1]`$ for the [partition](lecture-37-38.md#def-4-2-2) into $`n`$ equal parts, so $`H_{2n}-H_n\to\int_0^1\frac{dx}{1+x}=\ln2`$.

### Abel's transformation. The Dirichlet and Abel tests

> **Restored** (from the slides of the 2024/25 course, FS p58–p59; the 2022 notes, M3S p53–p56). Between pages p028 and p029 the notebook has lost Abel's transformation, the Dirichlet test with its proof and the statement of the Abel test; page p029 has kept the proof of the Abel test. The statements are given according to the lecturer's slides, the proofs according to the notes to them.
>
> *Abel's transformation.* Let $`(a_k)`$ and $`(b_k)`$ be numerical sequences, $`B_k=b_1+b_2+\dots+b_k`$, $`B_0:=0`$. Then for $`m>n\ge0`$
> ```math
> \sum_{k=n+1}^{m}a_kb_k=a_mB_m-a_{n+1}B_n+\sum_{k=n+1}^{m-1}(a_k-a_{k+1})B_k .
> ```
>
> **Proof.** Since $`b_k=B_k-B_{k-1}`$,
> ```math
> \begin{aligned}
> \sum_{k=n+1}^{m}a_kb_k&=a_{n+1}(B_{n+1}-B_n)+a_{n+2}(B_{n+2}-B_{n+1})+\dots+a_m(B_m-B_{m-1})\\
> &=-a_{n+1}B_n+(a_{n+1}-a_{n+2})B_{n+1}+\dots+(a_{m-1}-a_m)B_{m-1}+a_mB_m ,
> \end{aligned}
> ```
> as required. $`\square`$
>
> *Dirichlet's convergence test.* Let the following conditions hold:
>
> 1. $`a_n\downarrow0`$, i.e. $`a_{n+1}\le a_n`$ for all $`n`$ and $`a_n\to0`$;
> 2. there is $`M`$ such that $`|B_n|=|b_1+\dots+b_n|\le M`$ for all $`n`$.
>
> Then the series $`\sum_{n=1}^{\infty}a_nb_n`$ converges.
>
> **Proof.** We use the Bolzano–Cauchy criterion for the convergence of a series: the series $`\sum d_k`$ converges if and only if for every $`\varepsilon>0`$ there is $`N`$ such that $`\bigl|\sum_{k=n+1}^{n+p}d_k\bigr|<\varepsilon`$ for all $`n>N`$ and $`p\in\mathbb N`$. Put $`d_k=a_kb_k`$, $`m=n+p`$. By Abel's transformation, condition 2 and condition 1 (which gives $`a_k\ge0`$ and $`a_k-a_{k+1}\ge0`$)
> ```math
> \begin{aligned}
> \Bigl|\sum_{k=n+1}^{m}a_kb_k\Bigr|&\le|a_m|\,|B_m|+|a_{n+1}|\,|B_n|+\sum_{k=n+1}^{m-1}|a_k-a_{k+1}|\,|B_k|\\
> &\le M\Bigl(a_m+a_{n+1}+\sum_{k=n+1}^{m-1}(a_k-a_{k+1})\Bigr)=M\bigl(a_m+a_{n+1}+a_{n+1}-a_m\bigr)=2Ma_{n+1},
> \end{aligned}
> ```
> since $`\sum_{k=n+1}^{m-1}(a_k-a_{k+1})=(a_{n+1}-a_{n+2})+\dots+(a_{m-1}-a_m)=a_{n+1}-a_m`$. Since $`a_n\to0`$, for every $`\varepsilon>0`$ there is $`N`$ such that $`2Ma_{n+1}<\varepsilon`$ for all $`n>N`$. The Bolzano–Cauchy criterion is satisfied, and the series $`\sum a_nb_n`$ converges. $`\square`$
>
> *Abel's convergence test.* Let the following conditions hold:
>
> 1. the sequence $`(a_n)`$ is bounded and monotone;
> 2. the series $`\sum_{n=1}^{\infty}b_n`$ converges.
>
> Then the series $`\sum_{n=1}^{\infty}a_nb_n`$ converges.

<a id="p029"></a>

**Proof of the Abel test.** By hypothesis the sequence $`(a_n)`$ is bounded and monotone. For definiteness let it be non-increasing ($`a_1\ge a_2\ge a_3\ge\dots\ge a_n\ge\dots`$) and bounded below. Then by the theorem on the limit of a monotone sequence there is a finite limit $`\lim_{n\to\infty}a_n=a`$. Put $`\alpha_n:=a_n-a`$; then $`\alpha_n\downarrow0`$. The series $`\sum_{n=1}^{\infty}\alpha_nb_n`$ and $`a\sum_{n=1}^{\infty}b_n`$ converge: the first by the Dirichlet test ($`\alpha_n\downarrow0`$, and the partial sums of the convergent series $`\sum b_n`$ are bounded), the second by hypothesis. Therefore the series
```math
\sum_{n=1}^{\infty}a_nb_n=\sum_{n=1}^{\infty}(\alpha_n+a)b_n=\sum_{n=1}^{\infty}\alpha_nb_n+a\sum_{n=1}^{\infty}b_n .
```
converges too. If $`(a_n)`$ is non-decreasing and bounded above, the argument is the same with $`\alpha_n:=a-a_n\downarrow0`$ and $`a_nb_n=ab_n-\alpha_nb_n`$. $`\square`$

## §7.5. Rearrangements of series

<a id="def-7-5-1"></a>**Definition 7.5.1.** Let a series $`\sum_{n=1}^{\infty}a_n`$ and a bijective map $`\sigma:\mathbb N\to\mathbb N`$ be given. The series $`\sum_{n=1}^{\infty}a_{\sigma(n)}`$ is called a rearrangement of the original series $`\sum_{n=1}^{\infty}a_n`$.

### The commutative property of a series

<a id="def-7-5-2"></a>**Definition 7.5.2.** We say that a series $`\sum_{n=1}^{\infty}a_n`$ has the commutative property if for every bijection $`\sigma:\mathbb N\to\mathbb N`$ the series $`\sum_{n=1}^{\infty}a_{\sigma(n)}`$ converges and diverges together with the original series and, moreover,
```math
\sum_{n=1}^{\infty}a_n=\sum_{n=1}^{\infty}a_{\sigma(n)} .
```

An example of a rearrangement that changes the sum of a series and the commutative properties of series are discussed at the beginning of the next class (lectures 71–72).

## Cross-references

- Course topic: [chapter 4 “Numerical series”](../04-numeric-series.md) — [§4.2 “Series with terms of constant sign”](../04-numeric-series.md#sec-4-2), [§4.3 “Absolute and conditional convergence”](../04-numeric-series.md#sec-4-3), [the Leibniz test](../04-numeric-series.md#alternating-series-test), [rearrangements of the terms of a series](../04-numeric-series.md#rearrangement-warning).
- The beginning of chapter 7 (numerical series, properties of series, the Bolzano–Cauchy criterion for series, absolute convergence): [lectures 67–68](lecture-67-68.md).
- Facts used: [Theorem 2.3.3](lecture-11-12.md#thm-2-3-3) on the limit of a monotone sequence; [Theorem 2.3.7](lecture-13.md#thm-2-3-7), the Bolzano–Cauchy criterion for sequences.
- The Dirichlet and Abel tests for [improper integrals](lecture-47-48.md#def-4-5-2): [Theorem 4.5.4](lecture-49-50.md#thm-4-5-4) (lectures 49–50).
- Continuation: an example of a rearrangement of a series and the commutative properties — [lectures 71–72](lecture-71-72.md).

---

[← Lectures 67–68](lecture-67-68.md) · [Lecture index](index.md) · [Lectures 71–72 →](lecture-71-72.md) · [Terms & theorems](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-69-70.md) · [Español](../../es/lectures-2025-26/lecture-69-70.md)

---
title: "Lectures 81–82 — Lebesgue's criterion, Darboux sums, the integral over a set, Jordan measure, general properties of the integral"
lang: en
course: "Mathematical Analysis, 2025/26"
lecture: 81-82
semester: 3
source: "handwritten notebook, pages p074–p082"
source_pages: "p074, p075, p076, p077, p078, p079, p080, p081, p082"
course_chapter: 26
---
# Lectures 81–82 — Lebesgue's criterion, Darboux sums, the integral over a set, Jordan measure, general properties of the integral

[← Lectures 79–80](lecture-79-80.md) · [Lecture index](index.md) · [Lectures 83–84 →](lecture-83-84.md) · [Terms & theorems](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-81-82.md) · [Español](../../es/lectures-2025-26/lecture-81-82.md)

> **Source and numbering.** These notes were copied from a handwritten notebook (pages p074–p082; the raw page text is in [`ocr/raw/`](../../../ocr/raw/p074.md)). Page p074 begins with the proof of [Theorem 10.1.1](lecture-79-80.md#thm-10-1-1), stated at the end of lectures 79–80; after it, in the margin, there is the framed mark “20 October” (apparently the date of the class; lectures 79–80 are dated 22 October in the notebook, so “29 October” is probably meant) and, in red, the heading “Lectures 81–82” with the plan of the class: [Lebesgue's criterion](lecture-41-42.md#thm-4-2-5); [Darboux sums](lecture-39-40.md#def-4-2-8); the [Riemann integral](lecture-39-40.md#def-4-2-6) over a set; Jordan measure; properties of the integral; Fubini's theorem and its corollaries; Cavalieri's principle (the last two items are covered in lectures 83–84). The photographs of pages p078–p081, judging by their content, were taken in pairs in reverse order (by meaning the record runs p079, p078, p081, p080). The text below follows the page numbering, but the remark on the independence of the integral from the choice of the box (begun at the end of page p078, continued at the beginning of page p081) is given in full right after [Definition 10.2.4](#def-10-2-4), and the proof of [Theorem 10.2.1](#thm-10-2-1) (beginning of page p080) after its statement (end of page p081); the Darboux sums (page p079, numbering of §10.1) are left in place, although on the 2024/25 slides they come before §10.2. [Definitions 10.1.9](#def-10-1-9), [10.1.10](#def-10-1-10), [10.2.3](#def-10-2-3), [10.2.4](#def-10-2-4) and [Theorem 10.2.1](#thm-10-2-1) are unfinished in the notebook (“// to add”) and are restored from the slides of the 2024/25 course (FS p93, p95). The numbering of definitions and theorems is the lecturer's. Slips in the notes are corrected and marked with “Source correction” blocks; lost passages are restored and marked with “Restored” blocks; the tags match [`ocr/RESOLVED.md`](../../../ocr/RESOLVED.md). Places that still have to be checked against the notebook are listed in [`ocr/ISSUES.md`](../../../ocr/ISSUES.md).

## §10.1. The Riemann integral over an n-dimensional box (continued)

<a id="p074"></a>

Recall [Theorem 10.1.1](lecture-79-80.md#thm-10-1-1) (the necessary condition for integrability), stated at the end of lectures 79–80: if $`f\in R(I)`$, then $`f`$ is bounded on the box $`I`$. Its proof is written at the beginning of page p074.

**Proof of [Theorem 10.1.1](lecture-79-80.md#thm-10-1-1).** We show that if $`f`$ is unbounded on $`I`$, then $`f\notin R(I)`$. Let $`P`$ be some partition of $`I`$. The box $`I`$ is the union of finitely many boxes of the partition, so there is a box $`I_{i_0}\in P`$ on which $`f`$ is unbounded.

*Figure in the notes (page p074): the box $`I`$ with the grid of the partition, in which the box $`I_{i_0}`$ is highlighted.*

Let $`\xi'`$ and $`\xi''`$ be two sets of marked points for $`P`$ that (for simplicity) differ only in the choice of the point in $`I_{i_0}`$: in $`I_{i_0}`$ the points $`\xi'_{i_0}`$ and $`\xi''_{i_0}`$ are marked respectively. Then
```math
|\sigma(f,P,\xi')-\sigma(f,P,\xi'')|=|f(\xi'_{i_0})-f(\xi''_{i_0})|\cdot\mu(I_{i_0}).
```
Fix $`\xi'_{i_0}`$, and let the point $`\xi''_{i_0}`$ move over $`I_{i_0}`$. Since $`f`$ is unbounded on $`I_{i_0}`$, the difference $`|f(\xi'_{i_0})-f(\xi''_{i_0})|`$ can become arbitrarily large, and $`\mu(I_{i_0})>0`$; hence the difference of the [integral sums](lecture-37-38.md#def-4-2-4) can be made, for example, greater than $`1`$. This holds for every partition $`P`$, including arbitrarily fine ones, and by the Cauchy criterion the limit of the integral sums as $`\lambda(P)\to0`$ does not exist, i.e. $`f\notin R(I)`$. $`\square`$

### Lebesgue's criterion for Riemann integrability

> **Restored** (the definition is written neither in the notes nor on the 2024/25 slides; it is given by analogy with the one-dimensional [Definition 4.2.11](lecture-41-42.md#def-4-2-11) from lectures 41–42). A set $`E\subset\mathbb R^n`$ is called a *set of measure zero* (in the sense of Lebesgue) if for every $`\varepsilon>0`$ it can be covered by a finite or [countable](lecture-01-02.md#def-1-2-5) system of boxes $`I_1,I_2,\dots`$ with the sum of measures $`\sum_k\mu(I_k)<\varepsilon`$. One writes $`\mu(E)=0`$; the notation $`\mu(E)\ne0`$ means that $`E`$ is not a set of measure zero. The boxes of the covering may be taken either closed or open: each box $`I_k`$ is contained in an open box of measure less than $`\mu(I_k)+\varepsilon/2^k`$, so the notion does not change.

<a id="def-10-1-8"></a>**Definition 10.1.8.** We say that some property holds almost everywhere on a set $`M`$ if the subset of $`M`$ where this property may fail has measure zero.

<a id="p075"></a>

<a id="thm-10-1-2"></a>**Theorem 10.1.2 (Lebesgue's criterion).** A function $`f:I\to\mathbb R`$ is Riemann integrable on the box $`I`$, i.e. $`f\in R(I)`$, if and only if $`f`$ is bounded on $`I`$ and continuous almost everywhere on $`I`$.

> **Source correction** (T374). The notes say: “$`f\in R(I)\Leftrightarrow f`$ integr. [almost everywhere](../19-measure-theory.md#sec-19-4) on $`I`$”. Corrected according to the slide FS p92: the condition of the criterion is the boundedness of $`f`$ on $`I`$ and continuity almost everywhere on $`I`$ (cf. the one-dimensional Lebesgue criterion, [Theorem 4.2.5](lecture-41-42.md#thm-4-2-5)); the words “integrable almost everywhere” make no sense here.

**Remark (on sets of measure zero).**

① A point (or finitely many points) has measure zero. For example, for $`n=2`$ the point $`a=(a_1,a_2)`$ is the degenerate box $`I_{a,a}`$; it can be covered by the rectangle $`(a_1-\delta,a_1+\delta)\times(a_2-\delta,a_2+\delta)`$ of area $`4\delta^2`$, arbitrarily small for small $`\delta`$.

② In $`\mathbb R^2`$ a smooth curve (or finitely many smooth curves) has measure zero.

③ In $`\mathbb R^3`$ a smooth surface (or finitely many smooth surfaces) has measure zero.

> **Source correction** (U376, U377). In the notes items ② and ③ are written for arbitrary curves and surfaces (“Surf-ty” in item ③ is “surface”), and under item ③ there is, in red in the margin, an illegible clarification “in the sense of s…”, apparently about smoothness. The word “smooth” has been added: for smooth (class $`C^1`$) curves and surfaces the statements are true, while for arbitrary continuous curves they are not: the Peano curve maps a segment continuously onto the whole square.

④ The union of a finite or countable number of sets of measure zero is a set of measure zero.

⑤ Every subset of a set of measure zero has measure zero.

⑥ A non-degenerate box $`I_{a,b}=\{x\in\mathbb R^n:\ a_i\le x_i\le b_i\}`$, where $`a_i<b_i`$ for all $`i`$, is not a set of measure zero: $`\mu(I_{a,b})\ne0`$.

> **Restored** (justification of properties ①, ④–⑥ by the standard scheme; in the notes and on the slide FS p92 they are given without proof). ① Each of the $`m`$ points can be covered by a cube of measure less than $`\varepsilon/m`$. ④ If $`\mu(E_k)=0`$, $`k=1,2,\dots`$, then $`E_k`$ is covered by boxes with the sum of measures less than $`\varepsilon/2^k`$; all these boxes together form a countable system covering $`\bigcup_kE_k`$ with the sum of measures less than $`\sum_k\varepsilon/2^k=\varepsilon`$. ⑤ A covering of a set also covers any of its subsets. ⑥ Let $`I=I_{a,b}\subset\bigcup_kI_k`$ and $`\varepsilon>0`$. Replace each $`I_k`$ by an open box $`J_k\supset I_k`$ with $`\mu(J_k)<\mu(I_k)+\varepsilon/2^k`$. The [compact set](lecture-57-58.md#def-5-3-7) $`I`$ is covered by a finite number of them, say $`J_1,\dots,J_N`$, and by the property of the measure of a box (lectures 79–80) $`\mu(I)\le\sum_{k=1}^N\mu(J_k)<\sum_k\mu(I_k)+\varepsilon`$. Since $`\varepsilon`$ is arbitrary, the sum of measures of any covering of $`I`$ is at least $`\mu(I)=\prod_i(b_i-a_i)>0`$.

**Proof of [Theorem 10.1.2](#thm-10-1-2).** *Necessity.* Let $`f\in R(I)`$. By [Theorem 10.1.1](lecture-79-80.md#thm-10-1-1) $`f`$ is bounded on $`I`$: $`|f|\le M`$ on $`I`$. Let us check that $`f`$ is continuous almost everywhere on $`I`$, i.e. that the set $`E`$ of points of discontinuity of the function $`f`$ on $`I`$ has measure zero.

> **Source correction** (M380). In the notes the aim is written as “let us show that $`E=`$ the set of points of discontinuity of the fn $`I\Rightarrow f\in R(I)`$”; in meaning, it is proved that $`\mu(E)=0`$ (by contradiction: $`f\notin R(I)`$ is derived from $`\mu(E)\ne0`$).

Recall the notion of oscillation. For a function $`f:I\to\mathbb R`$ and a set $`X\subset I`$ the quantity
```math
\omega(f,X)=\sup_{x,y\in X}|f(x)-f(y)|
```
is called the oscillation of the function $`f`$ on the set $`X`$, and the quantity
```math
\omega(f,x)=\lim_{\delta\to0}\omega\bigl(f,V_\delta(x)\bigr),
```
where $`V_\delta(x)=\{y\in I:\ |y-x|<\delta\}`$ is the $`\delta`$-neighbourhood of the point $`x`$ in $`I`$, is called the oscillation of the function $`f`$ at the point $`x`$ (the limit exists, since $`\omega(f,V_\delta(x))`$ does not increase as $`\delta`$ decreases). The function $`f`$ is [continuous at the point](lecture-16.md#def-2-5-1) $`x`$ if and only if $`\omega(f,x)=0`$.

Consider the sets
```math
E_n=\Bigl\{x\in I:\ \omega(f,x)\ge\frac1n\Bigr\},\qquad n\in\mathbb N .
```
Then $`E=\bigcup_{n=1}^{\infty}E_n`$. If $`\mu(E)\ne0`$, then by property ④ there is $`n_0\in\mathbb N`$ such that $`\mu(E_{n_0})\ne0`$. Let us show that this contradicts the integrability of $`f`$.

Let $`P`$ be an arbitrary partition of $`I`$ into boxes $`I_i`$. Divide the boxes of the partition into two groups:
```math
A=\Bigl\{I_i\in P:\ I_i\cap E_{n_0}\ne\varnothing,\ \ \omega(f,I_i)\ge\frac1{2n_0}\Bigr\},\qquad B=P\setminus A .
```

<a id="p076"></a>

The system of boxes $`A`$ forms a covering of $`E_{n_0}`$. Indeed, let $`y\in E_{n_0}`$. If $`y`$ is an interior (relative to $`I`$) point of some box $`I_i\in P`$, then $`I_i\supset V_\delta(y)`$ for small $`\delta`$, hence $`\omega(f,I_i)\ge\omega(f,y)\ge\frac1{n_0}`$, and $`I_i\in A`$. If $`y`$ lies on the boundary of the boxes of the partition, an argument is needed — this is why the definition of $`A`$ has the threshold $`\frac1{2n_0}`$ and not $`\frac1{n_0}`$.

> **Restored** (by the standard proof; in the notes the case of a [boundary point](lecture-57-58.md#def-5-3-4) breaks off: “$`\to y\in`$ boundary $`I_i`$:”). Let $`I_{i_1},\dots,I_{i_m}`$ be all the boxes of the partition containing $`y`$. The other boxes are closed and do not contain $`y`$, so for small $`\delta>0`$ the neighbourhood $`V_\delta(y)`$ lies in $`I_{i_1}\cup\dots\cup I_{i_m}`$. If $`\omega(f,I_{i_s})<\frac1{2n_0}`$ for all $`s`$, then for any points $`x\in I_{i_s}`$, $`x'\in I_{i_t}`$ of $`V_\delta(y)`$ we would have
> ```math
> |f(x)-f(x')|\le|f(x)-f(y)|+|f(y)-f(x')|\le\omega(f,I_{i_s})+\omega(f,I_{i_t})\le2\max_{s}\omega(f,I_{i_s}),
> ```
> whence $`\omega(f,y)\le\omega(f,V_\delta(y))\le2\max_s\omega(f,I_{i_s})<\frac1{n_0}`$ — a contradiction with $`y\in E_{n_0}`$. Hence $`\omega(f,I_{i_s})\ge\frac1{2n_0}`$ for some $`s`$; this box contains $`y\in E_{n_0}`$ and therefore belongs to $`A`$.

Choose two sets of marked points $`\xi'`$ and $`\xi''`$ such that:

1) for $`I_i\in B`$ the marked points coincide: $`\xi'_i=\xi''_i`$;
2) for $`I_i\in A`$ the inequality $`f(\xi'_i)-f(\xi''_i)\ge\frac1{3n_0}`$ holds (this is possible, since $`\omega(f,I_i)\ge\frac1{2n_0}>\frac1{3n_0}`$).

Then
```math
|\sigma(f,P,\xi')-\sigma(f,P,\xi'')|=\sum_{I_i\in A}\bigl(f(\xi'_i)-f(\xi''_i)\bigr)\mu(I_i)\ge\frac1{3n_0}\sum_{I_i\in A}\mu(I_i).
```

> **Source correction** (M386). In the notes the factor $`\mu(I_i)`$ is missing in the middle part: “$`=\left|\sum_{I_i\in A}\left(f(\xi'_i)-f(\xi''_i)\right)\right|>\frac1{3n_0}\sum_{I_i\in A}\mu(I_i)`$”. The difference of the integral sums consists of the terms $`\bigl(f(\xi'_i)-f(\xi''_i)\bigr)\mu(I_i)`$ over the boxes of the group $`A`$ (over the group $`B`$ the terms are zero); all of them are non-negative, and each is at least $`\frac1{3n_0}\mu(I_i)`$.

The sum $`\sum_{I_i\in A}\mu(I_i)`$ is [bounded below](lecture-05-06.md#def-1-3-7) by a positive constant independent of $`P`$. This follows from the assumption $`\mu(E_{n_0})\ne0`$ and the fact that the boxes from $`A`$ cover $`E_{n_0}`$: since $`E_{n_0}`$ is not a set of measure zero, there is $`c>0`$ such that the sum of measures of any finite or countable system of boxes covering $`E_{n_0}`$ is at least $`c`$. Therefore $`\sum_{I_i\in A}\mu(I_i)\ge c`$ and
```math
|\sigma(f,P,\xi')-\sigma(f,P,\xi'')|\ge\frac{c}{3n_0}.
```
The partition $`P`$ is arbitrary (in particular, arbitrarily fine), so by the Cauchy criterion the integral sums $`\sigma(f,P,\xi)`$ have no limit as $`\lambda(P)\to0`$, i.e. $`f\notin R(I)`$ — a contradiction. Consequently $`\mu(E)=0`$.

*Sufficiency.* Let $`f`$ be bounded on $`I`$, $`|f|\le M`$, and continuous almost everywhere on $`I`$, i.e. $`\mu(E)=0`$. If $`M=0`$, then $`f\equiv0`$ and $`f\in R(I)`$; further $`M>0`$. Fix $`\varepsilon>0`$ and put
```math
E_\varepsilon=\{x\in I:\ \omega(f,x)\ge\varepsilon\}.
```
Since $`E_\varepsilon\subset E`$, we have $`\mu(E_\varepsilon)=0`$ (property ⑤). The set $`E_\varepsilon`$ is closed in $`I`$; being bounded, it is compact. And for compact sets every covering by [open sets](lecture-55-56.md#def-5-3-1) has a finite subcovering (the lecturer's remark in the margin). Therefore there is a finite set of boxes $`I_1,\dots,I_k`$ such that
```math
E_\varepsilon\subset\bigcup_{i=1}^kI_i,\qquad\sum_{i=1}^k\mu(I_i)<\varepsilon .
```

> **Restored** (by the standard proof; the notes say: “Obviously $`E_\varepsilon`$ is closed in $`I\Rightarrow E_\varepsilon`$ — compact!”). *Closedness.* Let $`x_s\in E_\varepsilon`$ and $`x_s\to x`$; then $`x\in I`$. For every $`\delta>0`$, for sufficiently large $`s`$ we have $`|x_s-x|<\delta/2`$, hence $`V_{\delta/2}(x_s)\subset V_\delta(x)`$ and
> ```math
> \omega\bigl(f,V_\delta(x)\bigr)\ge\omega\bigl(f,V_{\delta/2}(x_s)\bigr)\ge\omega(f,x_s)\ge\varepsilon .
> ```
> As $`\delta\to0`$ we get $`\omega(f,x)\ge\varepsilon`$, i.e. $`x\in E_\varepsilon`$. *A finite covering.* Since $`\mu(E_\varepsilon)=0`$, the set $`E_\varepsilon`$ is covered by a countable system of boxes with the sum of measures less than $`\varepsilon/2`$; replace the $`m`$-th of them by an open box containing it whose measure is larger by less than $`\varepsilon/2^{m+1}`$. We get a covering of the compact set $`E_\varepsilon`$ by open boxes with the sum of measures less than $`\varepsilon`$; the [closures](lecture-55-56.md#def-5-3-2) of the boxes of its finite subcovering are the $`I_1,\dots,I_k`$. All of them are non-degenerate.

Consider two partitions $`P'=\{I'_i\}`$ and $`P''=\{I''_j\}`$ of the box $`I`$ with marked points $`\xi'`$, $`\xi''`$ and small mesh $`\lambda(P')`$, $`\lambda(P'')`$ (recall that the mesh is the largest of the diameters of the boxes of the partition; how small it has to be will be indicated below). Let $`P`$ be the partition obtained by intersecting the boxes of the partitions $`P'`$ and $`P''`$: $`P=\{I_{ij}=I'_i\cap I''_j\}`$ (non-degenerate intersections are taken), and let $`\xi=\{\xi_{ij}\}`$ be some set of marked points for $`P`$.

<a id="p077"></a>

Put $`C_1=\bigcup_{i=1}^kI_i`$, and denote by $`C_2`$ and $`C_3`$ the unions of the boxes $`2I_i`$ and respectively $`3I_i`$ obtained from $`I_i`$ by a homothety with ratio $`2`$ and $`3`$ centred at the centre of $`I_i`$. Then $`E_\varepsilon\subset C_1\subset C_2\subset C_3`$, and $`E_\varepsilon`$ lies strictly inside $`C_2`$, while the distance between the boundaries of $`C_2`$ and $`C_3`$ is strictly positive.

*Figure in the notes (page p077): a box of the covering inside its dilations; labels $`C_2`$, $`C_3`$.*

Note that $`\mu(I'_i)=\sum_j\mu(I_{ij})`$. Therefore
```math
|\sigma(f,P',\xi')-\sigma(f,P,\xi)|=\Bigl|\sum_{i,j}\bigl(f(\xi'_i)-f(\xi_{ij})\bigr)\mu(I_{ij})\Bigr|\le\Sigma_1+\Sigma_2,
```
where $`\Sigma_1`$ is the sum of the terms $`|f(\xi'_i)-f(\xi_{ij})|\,\mu(I_{ij})`$ over those $`i`$ for which $`I'_i`$ intersects $`C_2`$, and $`\Sigma_2`$ is the sum of the same terms over the remaining $`i`$. The terms $`\Sigma_1`$ are estimated from above crudely, without considering cases (a note in the margin).

> **Source correction** (M392, U394, U395, U396). In the notes the right-hand side of the estimate is written as “$`\le\sum_1+\sum_2\left|f(\xi'_i)-f(\xi_{ij})\right|\mu(I_{ij})+\sum\left|f(\xi_i)-f(\xi_{ij})\right|\mu(I_{ij})`$”: in fact this is one sum $`\sum_{i,j}|f(\xi'_i)-f(\xi_{ij})|\,\mu(I_{ij})`$ split into two groups of terms, and the second group must have $`\xi'_i`$. The definitions of $`C_1`$, $`C_2`$, $`C_3`$ in the notes are illegible (“union of intervals $`I_{ij}`$ with centres at $`\xi'`$…”, “…coord. 2”) and are read according to the standard proof (cf. V. A. Zorich, “Mathematical Analysis”, part II, ch. 11, §1): this is the covering of $`E_\varepsilon`$ and its dilations by the factors $`2`$ and $`3`$. In the notes they are introduced after the splitting of the sum; here, before it, since $`\Sigma_1`$ and $`\Sigma_2`$ are defined through $`C_2`$.

> **Restored** (the end of the proof by the standard scheme, cf. Zorich, ibid.; in the notes the estimates of $`\Sigma_1`$ and $`\Sigma_2`$ are not completed, and in lectures 83–84 the lecturer proved sufficiency in the one-dimensional case).
>
> Let $`d`$ be half the smallest of the edges of the boxes $`I_1,\dots,I_k`$. If a set of diameter less than $`d`$ intersects $`2I_l`$, it lies in $`3I_l`$: in each coordinate $`3I_l`$ is wider than $`2I_l`$ on each side by half of the corresponding edge of $`I_l`$. This is the precise meaning of the words “the distance between the boundaries of $`C_2`$ and $`C_3`$ is positive”.
>
> *Estimate of $`\Sigma_1`$.* Let $`\lambda(P')<d`$. Every box $`I'_i`$ intersecting $`C_2`$ intersects some $`2I_l`$ and therefore lies in $`3I_l`$; assign it to one such $`l`$. Non-overlapping boxes lying in $`3I_l`$ have total measure at most $`\mu(3I_l)=3^n\mu(I_l)`$, so the sum of measures of all such $`I'_i`$ is less than $`3^n\sum_l\mu(I_l)<3^n\varepsilon`$. Since $`|f(\xi'_i)-f(\xi_{ij})|\le2M`$,
> ```math
> \Sigma_1\le2M\sum_{I'_i\cap C_2\ne\varnothing}\mu(I'_i)<2\cdot3^nM\varepsilon .
> ```
> *Estimate of $`\Sigma_2`$.* The set $`K=I\setminus\operatorname{int}C_2`$ is compact and does not intersect $`E_\varepsilon`$, so $`\omega(f,x)<\varepsilon`$ at every point of $`x\in K`$. It follows that there is $`\delta_0>0`$ such that $`\omega(f,V_{\delta_0}(x))<\varepsilon`$ for all $`x\in K`$. Indeed, for each point $`x\in K`$ choose $`\delta(x)>0`$ so that $`\omega(f,V_{2\delta(x)}(x))<\varepsilon`$. The open balls of radii $`\delta(x)`$ centred at $`x\in K`$ cover the compact set $`K`$; choose a finite subcovering by balls centred at $`x_1,\dots,x_m`$ and put $`\delta_0=\min_s\delta(x_s)`$. If $`x\in K`$ lies in the ball centred at $`x_s`$, then $`V_{\delta_0}(x)\subset V_{2\delta(x_s)}(x_s)`$, and hence $`\omega(f,V_{\delta_0}(x))<\varepsilon`$.
>
> Let, moreover, $`\lambda(P')<\delta_0`$. If $`I'_i`$ does not intersect $`C_2`$, then $`I'_i\subset K`$ and $`I'_i\subset V_{\delta_0}(\xi'_i)`$, since the diameter of $`I'_i`$ is less than $`\delta_0`$. Since $`\xi_{ij}\in I_{ij}\subset I'_i`$, we have $`|f(\xi'_i)-f(\xi_{ij})|<\varepsilon`$, and
> ```math
> \Sigma_2\le\varepsilon\sum_{i,j}\mu(I_{ij})=\varepsilon\,\mu(I).
> ```
> *Conclusion.* Thus, if $`\lambda(P')<\min(d,\delta_0)`$, then $`|\sigma(f,P',\xi')-\sigma(f,P,\xi)|<(2\cdot3^nM+\mu(I))\,\varepsilon`$. The partition $`P`$ is also finer than the partition $`P''`$, so for $`\lambda(P'')<\min(d,\delta_0)`$ the same holds for $`P''`$. Consequently, for $`\lambda(P'),\lambda(P'')<\min(d,\delta_0)`$
> ```math
> |\sigma(f,P',\xi')-\sigma(f,P'',\xi'')|<2\bigl(2\cdot3^nM+\mu(I)\bigr)\varepsilon .
> ```
> The number $`\varepsilon>0`$ is arbitrary, and the factor $`2(2\cdot3^nM+\mu(I))`$ does not depend on it; by the Cauchy criterion the integral sums have a limit as $`\lambda(P)\to0`$, i.e. $`f\in R(I)`$. $`\square`$

**Remark (on the proof of sufficiency).** In the notes (page p077) the proof of sufficiency is written once more, with the constants normalised so that the final estimate is immediately less than $`\varepsilon`$; here $`|f|\le M`$ on $`I`$ (if $`M=0`$, then $`f\equiv0`$ and is integrable). To this end we cover the set $`E_\eta`$, where $`\eta=\frac{\varepsilon}{2\mu(I)}`$, by a finite set of boxes $`I_1,\dots,I_k`$ with $`\sum\mu(I_i)<\frac{\varepsilon}{4\cdot3^nM}`$. Outside the covering, at each point $`x`$, the oscillation is $`\omega(f,x)<\eta`$, so it has a neighbourhood $`V_\delta(x)`$ in which the oscillation of the function is $`\omega(f,V_\delta(x))<\eta`$. Then, in the notation of the proof, $`\Sigma_1<2\cdot3^nM\cdot\frac{\varepsilon}{4\cdot3^nM}=\frac{\varepsilon}2`$ and $`\Sigma_2\le\eta\,\mu(I)=\frac{\varepsilon}2`$.

> **Source correction** (M530, U400). The notes say “$`\sum\mu(I_i)<\frac{\varepsilon}{4M}`$” for the covering of $`E_\varepsilon`$ and further “outside $`I_i`$ $`f`$ is continuous at every point ⇒ … $`\omega(f,D(x))<\frac{\varepsilon}{2\mu(I)}`$”. Outside the covering of the set $`E_\varepsilon`$ the function need not be continuous: there one only knows that $`\omega(f,x)<\varepsilon`$ ([points of discontinuity](lecture-16.md#def-2-5-4) with smaller oscillation may lie outside the covering), and it is this estimate that is used. For the oscillation outside the covering to be less than $`\frac{\varepsilon}{2\mu(I)}`$, one has to cover $`E_\eta`$ with $`\eta=\frac{\varepsilon}{2\mu(I)}`$, and because of the dilation of the covering by the factor $`3`$, the sum of measures of the covering must be less than $`\frac{\varepsilon}{4\cdot3^nM}`$, not $`\frac{\varepsilon}{4M}`$.

## §10.2. The integral over a set

<a id="p078"></a>

### Admissible sets. The characteristic function of a set

<a id="def-10-2-1"></a>**Definition 10.2.1.** A set $`\Omega\subset\mathbb R^n`$ is called admissible if it is bounded in $`\mathbb R^n`$ and its boundary $`\partial\Omega`$ is a set of measure zero.

<a id="def-10-2-2"></a>**Definition 10.2.2.** Let $`\Omega\subset\mathbb R^n`$ be an admissible set. The function
```math
\chi_\Omega(x)=\begin{cases}1, & x\in\Omega,\\ 0, & x\notin\Omega\end{cases}
```
is called the characteristic function of the set $`\Omega`$.

**Remark.** The function $`\chi_\Omega`$ has discontinuities only on $`\partial\Omega`$: at the [interior points](lecture-57-58.md#def-5-3-3) of $`\Omega`$ it is locally equal to $`1`$, at the exterior points it is locally equal to $`0`$, and at every boundary point it is discontinuous (every neighbourhood of it contains points of $`\Omega`$ and of the complement). If $`\Omega`$ is an admissible set, then $`\mu(\partial\Omega)=0`$, and therefore $`\chi_\Omega`$ is continuous almost everywhere in $`\mathbb R^n`$.

### The integral over a set

Let $`\Omega\subset\mathbb R^n`$ and $`f:\Omega\to\mathbb R`$.

> **Restored** (from the slides of the 2024/25 course, FS p95; in the notes both definitions are unfinished — “// to add”; of [Definition 10.2.3](#def-10-2-3) only the beginning “The fn $`f`$ is defined on the set $`\Omega`$. Then.” is written, and the line “$`\Omega=\mathbb R^n`$, $`f:\Omega\to\mathbb R`$” before them is read as $`\Omega\subset\mathbb R^n`$, as on the slide).
>
> <a id="def-10-2-3"></a>**Definition 10.2.3.** Let the function $`f`$ be defined on the set $`\Omega`$. Then
> ```math
> f\chi_\Omega(x)=\begin{cases}f(x), & x\in\Omega,\\ 0, & x\notin\Omega\end{cases}
> ```
> (although $`f`$ is not defined outside $`\Omega`$).
>
> <a id="def-10-2-4"></a>**Definition 10.2.4.** The integral of the function $`f`$ over a (bounded) set $`\Omega`$ is defined by the relation
> ```math
> \int_\Omega f(x)\,dx:=\int_{I\supset\Omega}f\chi_\Omega(x)\,dx,
> ```
> where $`I`$ is an arbitrary box containing the set $`\Omega`$; the integral on the left exists if the integral on the right exists. The set of functions integrable on $`\Omega`$ is denoted by $`R(\Omega)`$.

**Remark (on independence of the choice of the box).** Let $`\Omega\subset I_1`$ and $`\Omega\subset I_2`$, where $`I_1`$, $`I_2`$ are boxes. Then the integrals
```math
\int_{I_1}f\chi_\Omega\,dx,\qquad\int_{I_2}f\chi_\Omega\,dx
```
exist or do not exist simultaneously, and if they exist, their values coincide. Thus [Definition 10.2.4](#def-10-2-4) is correct.

Consider the box $`I_1\cap I_2\supset\Omega`$. What can be said about the points of discontinuity of the function $`f\chi_\Omega`$? These are

① the points of discontinuity of $`f`$ in $`\Omega`$;

② the points of discontinuity of $`\chi_\Omega`$, i.e. the points of $`\partial\Omega`$.

All of them lie in $`\overline\Omega\subset I_1\cap I_2`$, and outside $`I_1\cap I_2`$ the function $`f\chi_\Omega`$ is zero. Therefore, by Lebesgue's criterion ([Theorem 10.1.2](#thm-10-1-2)), the three integrals
```math
\int_{I_1\cap I_2}f\chi_\Omega\,dx,\qquad\int_{I_1}f\chi_\Omega\,dx,\qquad\int_{I_2}f\chi_\Omega\,dx
```
exist or do not exist simultaneously.

*Figure in the notes (page p081): two overlapping rectangles $`I_1`$ and $`I_2`$; the set $`\Omega`$ lies in the shaded intersection.*

Let the integrals exist. We consider only those partitions $`I_1`$ and $`I_2`$ that are obtained by completing partitions of $`I_1\cap I_2`$ (i.e. the boxes of the partition lying in $`I_1\cap I_2`$ form a partition of $`I_1\cap I_2`$). Note that outside $`I_1\cap I_2`$ the function $`f\chi_\Omega`$ is zero, so the integral sums for $`I_1`$ and $`I_2`$ are in fact integral sums for $`I_1\cap I_2`$:
```math
\sum_if\chi_\Omega(\xi_i)\,\mu(I_{1i})=\sum_{I_{1i}\subset I_1\cap I_2}f\chi_\Omega(\xi_i)\,\mu(I_{1i}),\qquad
\sum_if\chi_\Omega(\eta_i)\,\mu(I_{2i})=\sum_{I_{2i}\subset I_1\cap I_2}f\chi_\Omega(\eta_i)\,\mu(I_{2i}).
```
Passing to the limit as the mesh of the partitions tends to zero, we get
```math
\int_{I_1}f\chi_\Omega\,dx=\int_{I_1\cap I_2}f\chi_\Omega\,dx=\int_{I_2}f\chi_\Omega\,dx .
```

> **Source correction** (S423, M424, T427). The notes say: “① pts of discontinuity of $`f`$ outside $`\Omega`$”, “These are always pts of discontinuity of $`\chi_\Omega\in I_1\cap I_2`$”, “The integral sums for $`I_1`$ and $`I_2`$ are the same integral sum for $`I_1\cap I_2`$”. Corrected by the meaning and according to the record of the 2024/25 lecture (FS p95): the points of discontinuity of $`f`$ are taken in $`\Omega`$ (outside $`\Omega`$ the function $`f`$ is not defined, and $`f\chi_\Omega=0`$); $`I_1\cap I_2`$ contains all the points of discontinuity of $`f\chi_\Omega`$, not only $`\chi_\Omega`$; the integral sum for $`I_1`$ and the integral sum for $`I_2`$ — each its own — are integral sums for $`I_1\cap I_2`$.

> **Restored** (refinements of the lecturer's argument, by the standard proof). 1) Points of the boundary of the box $`J=I_1\cap I_2`$ may be points of discontinuity of the restriction of $`f\chi_\Omega`$ to $`J`$ without being points of discontinuity on $`I_1`$ (or vice versa), but the boundary of a box has measure zero, so this does not affect the application of Lebesgue's criterion; the boundedness of $`f\chi_\Omega`$ on $`I_1`$, on $`I_2`$ and on $`J`$ is equivalent to the boundedness of $`f`$ on $`\Omega`$. 2) The equality of the integral sums in the formula above holds if in the boxes not lying in $`J`$ the marked points are chosen outside $`J`$ (otherwise a marked point may fall on a common face with $`J`$, where $`f\chi_\Omega`$ need not equal zero). Since the integrals exist, they can be computed as limits of integral sums for any such choice of marked points and any partitions of the indicated kind whose mesh tends to zero; the equality of the integrals follows.

<a id="p079"></a>

### Darboux integral sums (to §10.1)

This item belongs to §10.1 (hence the numbering 10.1.9, 10.1.10 and [Theorem 10.1.3](#thm-10-1-3)); in the notebook it is written on page p079, among the definitions of §10.2.

Let $`f`$ be a real-valued function on the box $`I`$, and $`P=\{I_i\}`$ a partition of the box $`I`$. Put
```math
m_i=\inf_{x\in I_i}f(x),\qquad M_i=\sup_{x\in I_i}f(x).
```

> **Restored** (from the slides of the 2024/25 course, FS p93; in the notes the definition is unfinished — “// to add”: only “The quantity $`s(f,P)=\sum m_i\mu(I_i)`$, $`S(f,P)`$” is written).
>
> <a id="def-10-1-9"></a>**Definition 10.1.9.** The quantities
> ```math
> s(f,P)=\sum_im_i\,\mu(I_i),\qquad S(f,P)=\sum_iM_i\,\mu(I_i)
> ```
> are called respectively the lower and the upper (Darboux) integral sum of the function $`f`$ on the box $`I`$ corresponding to the partition $`P`$ of this box.

![A column over a box of the partition under the graph of the function (page p079)](../../assets/lectures-2025-26/lec81-82-p079-darboux-column.jpg)

### The lower and upper Darboux integrals

> **Restored** (from the slides of the 2024/25 course, FS p93; the notes have only the heading “Def (10.1.10) // to add”).
>
> <a id="def-10-1-10"></a>**Definition 10.1.10.** The lower and upper (Darboux) integrals of the function $`f:I\to\mathbb R`$ on the box $`I`$ are respectively the quantities
> ```math
> \underline J=\sup_Ps(f,P),\qquad\overline J=\inf_PS(f,P),
> ```
> where the [infimum](lecture-11-12.md#def-2-3-2) and [supremum](lecture-11-12.md#def-2-3-1) are taken over all possible partitions $`P`$ of the box $`I`$.

> **Restored** (the statement of the exercise is from the slide FS p93; the notes say: “Exercise. The rectangles $`I`$ have the following prop.: // to add”, then only “$`s`$” and the lecturer's hint “$`\sup\inf\le\inf\sup`$”; the solution follows the standard scheme).
>
> **Exercise.** For every partition $`P`$ of the box $`I`$ the inequalities
> ```math
> s(f,P)\le\underline J\le\overline J\le S(f,P).
> ```
> hold. The lecturer's hint: $`\sup\inf\le\inf\sup`$. Solution: when new division points are added, lower sums do not decrease and upper sums do not increase (the infimum over a smaller set is not smaller, the supremum is not larger). Therefore, for any partitions $`P_1`$, $`P_2`$ and their common refinement $`P`$
> ```math
> s(f,P_1)\le s(f,P)\le S(f,P)\le S(f,P_2).
> ```
> Taking the supremum over $`P_1`$ and the infimum over $`P_2`$, we get $`\underline J\le\overline J`$; the outer inequalities follow from the definition of the infimum and supremum.

### Darboux's criterion for the integrability of a real-valued function

<a id="thm-10-1-3"></a>**Theorem 10.1.3 (Darboux's criterion).** A function $`f:I\to\mathbb R`$ is integrable on the box $`I`$ if and only if $`f`$ is bounded on $`I`$ and $`\underline J=\overline J`$.

The theorem is given without proof.

> **Source correction** (A413, U414). The notes say “Theorem (10.1.13)” and “$`f\in R(I)\Leftrightarrow\underline{J}=\overline{J}`$”. The number is corrected to 10.1.3 (as on the slide FS p93; there are no other theorems in §10.1); the mark after the number, read as “form.”, is apparently “w/o pf” (without proof). The missing condition of boundedness has been added (as on the slide): without it the statement is false. For example, for $`I=[0,1]`$, $`f(x)=\frac1x`$ for $`0<x\le1`$, $`f(0)=0`$ we have $`S(f,P)=+\infty`$ for every $`P`$, while for the partition by the points $`0<2^{-N}<2^{-N+1}<\dots<\frac12<1`$ we get $`s(f,P)=\frac N2`$; hence $`\underline J=\overline J=+\infty`$, although $`f\notin R(I)`$ by [Theorem 10.1.1](lecture-79-80.md#thm-10-1-1).

<a id="p080"></a>

### The measure (volume) of an admissible set

<a id="def-10-2-5"></a>**Definition 10.2.5.** The (Jordan) measure, or volume, of a bounded set $`\Omega\subset\mathbb R^n`$ is the quantity
```math
\mu(\Omega):=\int_\Omega1\,dx=\int_I\chi_\Omega(x)\,dx\qquad(I\supset\Omega),
```
if the indicated (Riemann) integral exists.

> **Source correction** (S417, T532). The notes say “$`\mu(\Omega):=\int_I1\,dx`$”, and in the remark below “$`\int_I1\,dx=\int_{I\ni\Omega}\chi_\Omega(x)\,dx`$”. The integral of one over the box $`I`$ equals $`\mu(I)`$, not the volume $`\Omega`$; it should be $`\int_\Omega1\,dx`$, which by [Definition 10.2.4](#def-10-2-4) equals $`\int_I\chi_\Omega(x)\,dx`$ for any box $`I\supset\Omega`$ (as on the slide FS p96).

<a id="def-10-2-6"></a>**Definition 10.2.6.** A set $`\Omega\subset\mathbb R^n`$ is called a set of measure zero in the sense of Jordan, or a set of volume zero, if for every $`\varepsilon>0`$ it can be covered by a finite system of boxes (rectangles) $`I_1,\dots,I_k`$ such that
```math
\sum_{i=1}^k\mu(I_i)<\varepsilon .
```

**Remark.** By [Definition 10.2.4](#def-10-2-4)
```math
\int_\Omega1\,dx=\int_{I\supset\Omega}\chi_\Omega(x)\,dx .
```
Since the points of discontinuity of $`\chi_\Omega`$ are exactly the points of $`\partial\Omega`$, by Lebesgue's criterion ([Theorem 10.1.2](#thm-10-1-2)) this integral exists if and only if $`\mu(\partial\Omega)=0`$. Therefore the measure $`\mu(\Omega)`$ of a bounded set $`\Omega`$ is defined only for admissible sets (and for all of them).

**Remark.** Only admissible sets are (Jordan) measurable.

*Figure in the margin (page p080): two nested ovals — “sets of Jordan measure zero” inside “sets of Lebesgue measure zero”.*

> **Restored** (an explanation of the figure — according to the record of the 2024/25 lecture, FS p96, and a standard example). A set of Jordan measure zero is a set of Lebesgue measure zero: a finite system of boxes is a special case of an at most countable one. The converse is false: the set of rational points of the segment $`[0,1]`$ is countable and therefore has Lebesgue measure zero (properties ① and ④), but a finite system of segments covering all its points also covers the whole segment $`[0,1]`$ (its union is closed), so the sum of the lengths is at least $`1`$. For compact sets both notions coincide: from a covering by open boxes one can choose a finite subcovering (this is how it was used in the proof of sufficiency in [Theorem 10.1.2](#thm-10-1-2)).

<a id="p081"></a>

### The criterion for integrability over a set

> **Restored** (from the slides of the 2024/25 course, FS p95; the notes have the heading “Theorem (10.2.1) // to add” and an illegible beginning of the statement “… $`f:\Omega\to\mathbb R`$ is integrable on an admissible set”).
>
> <a id="thm-10-2-1"></a>**Theorem 10.2.1.** A function $`f:\Omega\to\mathbb R`$ is integrable on an admissible set $`\Omega`$ if and only if it is bounded and continuous at almost all points of the set $`\Omega`$.

**Proof.** Take a box $`I\supset\Omega`$; by [Definition 10.2.4](#def-10-2-4) we have to find out when $`f\chi_\Omega\in R(I)`$. The points of discontinuity of the function $`f\chi_\Omega`$ are the points of discontinuity of $`f`$ in $`\Omega`$ and the points of discontinuity of $`\chi_\Omega`$ lying on $`\partial\Omega`$. More precisely, outside $`\partial\Omega`$ the points of discontinuity of $`f\chi_\Omega`$ are exactly the points of discontinuity of $`f`$ lying inside $`\Omega`$ (at exterior points $`f\chi_\Omega`$ is locally zero), and $`\mu(\partial\Omega)=0`$, since $`\Omega`$ is admissible. Therefore the set of points of discontinuity of $`f\chi_\Omega`$ has measure zero if and only if the set of points of discontinuity of $`f`$ in $`\Omega`$ has measure zero. Moreover, $`f\chi_\Omega`$ is bounded on $`I`$ if and only if $`f`$ is bounded on $`\Omega`$. It remains to apply Lebesgue's criterion ([Theorem 10.1.2](#thm-10-1-2)). $`\square`$

## §10.3. General properties of the integral

<a id="p082"></a>

<a id="thm-10-3-1"></a>**Theorem 10.3.1.** Let $`\Omega_1`$, $`\Omega_2`$ be admissible sets in $`\mathbb R^n`$, and let $`f`$ be a function defined on $`\Omega_1\cup\Omega_2`$. Then:

① the existence of the integrals is related as follows:
```math
\exists\int_{\Omega_1\cup\Omega_2}f(x)\,dx\iff\exists\int_{\Omega_i}f(x)\,dx\ \ (i=1,2)\implies\exists\int_{\Omega_1\cap\Omega_2}f(x)\,dx;
```

② if $`\mu(\Omega_1\cap\Omega_2)=0`$, then, provided the integrals exist,
```math
\int_{\Omega_1\cup\Omega_2}f(x)\,dx=\int_{\Omega_1}f(x)\,dx+\int_{\Omega_2}f(x)\,dx .
```

**Proof of item ②.** Let $`\mu(\Omega_1\cap\Omega_2)=0`$ and let the integrals exist. Take a box $`I\supset\Omega_1\cup\Omega_2`$. By [Definition 10.2.4](#def-10-2-4)
```math
\int_{\Omega_1\cup\Omega_2}f(x)\,dx=\int_If\chi_{\Omega_1\cup\Omega_2}(x)\,dx .
```
Note that
```math
\chi_{\Omega_1\cup\Omega_2}(x)=\chi_{\Omega_1}(x)+\chi_{\Omega_2}(x)-\chi_{\Omega_1\cap\Omega_2}(x)
```
(at points of both sets: $`1=1+1-1`$; of exactly one of them: $`1=1+0-0`$; outside both: $`0=0`$). Therefore, using the linearity of the integral over a box (it follows from the linearity of integral sums),
```math
\int_If\chi_{\Omega_1\cup\Omega_2}\,dx=\underbrace{\int_If\chi_{\Omega_1}\,dx}_{=\int_{\Omega_1}f\,dx}+\underbrace{\int_If\chi_{\Omega_2}\,dx}_{=\int_{\Omega_2}f\,dx}-\underbrace{\int_If\chi_{\Omega_1\cap\Omega_2}\,dx}_{=0},
```
where the last integral exists by item ① and equals zero, since $`\mu(\Omega_1\cap\Omega_2)=0`$. $`\square`$

> **Source correction** (T531, S432). In the notes the proof is entitled “Pf (item ① Th. 10.3.1)”, but it is item ② that is proved (likewise in the record of the 2024/25 lecture, FS p97: “Pf (item ②)”). The signs “⇔” in the last line (“$`\int_{\Omega_1}f\,dx`$ ⇔ $`\int_{\Omega_2}f\,dx`$ − … ⇔ $`0`$”) are vertical equality signs under curly brackets, connecting the terms with the integrals over $`\Omega_1`$, $`\Omega_2`$ and with zero, and the circled sign at the beginning of this line marks the continuation of the equality.

> **Restored** (by the standard proof; in the notes and on the slide FS p97 item ① is not proved, and the vanishing of the last integral is not justified). *Item ①.* The sets $`\Omega_1\cup\Omega_2`$ and $`\Omega_1\cap\Omega_2`$ are bounded, and their boundaries lie in $`\partial\Omega_1\cup\partial\Omega_2`$, so they are admissible (properties ④, ⑤). Let $`I\supset\Omega_1\cup\Omega_2`$ be a box. A sum and a product of functions are continuous at every point where all the summands (factors) are continuous, and $`\chi_\Omega`$ is discontinuous only on $`\partial\Omega`$. Therefore, if $`f\chi_{\Omega_1\cup\Omega_2}\in R(I)`$, the functions $`f\chi_{\Omega_i}=f\chi_{\Omega_1\cup\Omega_2}\cdot\chi_{\Omega_i}`$ and $`f\chi_{\Omega_1\cap\Omega_2}=f\chi_{\Omega_1\cup\Omega_2}\cdot\chi_{\Omega_1\cap\Omega_2}`$ are bounded, and their points of discontinuity lie in the union of the set of points of discontinuity of $`f\chi_{\Omega_1\cup\Omega_2}`$ and the set $`\partial\Omega_1\cup\partial\Omega_2`$, i.e. in a set of measure zero; by Lebesgue's criterion they are integrable on $`I`$. Conversely, if $`f\chi_{\Omega_1},f\chi_{\Omega_2}\in R(I)`$, then $`f\chi_{\Omega_1\cap\Omega_2}=f\chi_{\Omega_1}\cdot\chi_{\Omega_2}\in R(I)`$ by the same argument, and $`f\chi_{\Omega_1\cup\Omega_2}=f\chi_{\Omega_1}+f\chi_{\Omega_2}-f\chi_{\Omega_1\cap\Omega_2}\in R(I)`$. *Vanishing.* The function $`f`$ is bounded on $`\Omega_1\cup\Omega_2`$, $`|f|\le M`$ (the integral over $`\Omega_1\cup\Omega_2`$ exists). For every partition $`P`$ of the box $`I`$ with marked points $`\xi`$
> ```math
> \bigl|\sigma(f\chi_{\Omega_1\cap\Omega_2},P,\xi)\bigr|\le M\,\sigma(\chi_{\Omega_1\cap\Omega_2},P,\xi)\xrightarrow[\lambda(P)\to0]{}M\int_I\chi_{\Omega_1\cap\Omega_2}\,dx=M\,\mu(\Omega_1\cap\Omega_2)=0 .
> ```

### An estimate of the integral

<a id="prop-10-3-1"></a>**Proposition 10.3.1.** If $`f\in R(\Omega)`$, then $`|f|\in R(\Omega)`$ and the following inequality holds:
```math
\Bigl|\int_\Omega f(x)\,dx\Bigr|\le\int_\Omega|f(x)|\,dx .
```
Here $`R(\Omega)`$ is the set of functions Riemann integrable on the set $`\Omega`$.

**Proof.** 1) The integrability of $`|f|`$ on $`\Omega`$ follows from the definition of the integral over the set $`\Omega`$ and Lebesgue's criterion: if $`I\supset\Omega`$ and $`f\chi_\Omega\in R(I)`$, the function $`|f|\chi_\Omega=|f\chi_\Omega|`$ is bounded on $`I`$ and continuous at every point where $`f\chi_\Omega`$ is continuous, hence $`|f\chi_\Omega|\in R(I)`$.

2) The inequality is obtained by passing to the limit in the inequality for integral sums: for every partition $`P`$ of the box $`I`$ with marked points $`\xi`$
```math
|\sigma(f\chi_\Omega,P,\xi)|\le\sigma(|f|\chi_\Omega,P,\xi),
```
and as $`\lambda(P)\to0`$ we get $`\bigl|\int_\Omega f\,dx\bigr|\le\int_\Omega|f|\,dx`$. $`\square`$

## Cross-references

- Course topic: [chapter 17 “Multiple integrals and change of variables”](../17-multiple-integrals.md) — [§17.1 “Definition and iterated integrals”](../17-multiple-integrals.md#sec-17-1); Darboux sums in the one-dimensional case — [§8.1 “Partitions and Darboux sums”](../08-riemann-integration.md#sec-8-1); [Lebesgue measure](lecture-51-52.md#def-4-6-6) — [§19.3 “Lebesgue measure”](../19-measure-theory.md#sec-19-3).
- The one-dimensional case: a set of measure zero ([Definition 4.2.11](lecture-41-42.md#def-4-2-11)) and Lebesgue's criterion ([Theorem 4.2.5](lecture-41-42.md#thm-4-2-5)) — [lectures 41–42](lecture-41-42.md).
- The beginning of §10.1 (a box and its measure, partitions, integral sums, [Definitions 10.1.1](lecture-79-80.md#def-10-1-1)–[10.1.7](lecture-79-80.md#def-10-1-7), the statement of [Theorem 10.1.1](lecture-79-80.md#thm-10-1-1)): [lectures 79–80](lecture-79-80.md).
- The end of §10.3 (properties of the integral), the proof of sufficiency in Lebesgue's criterion in the one-dimensional case, Fubini's theorem and Cavalieri's principle (§10.4): [lectures 83–84](lecture-83-84.md).

---

[← Lectures 79–80](lecture-79-80.md) · [Lecture index](index.md) · [Lectures 83–84 →](lecture-83-84.md) · [Terms & theorems](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-81-82.md) · [Español](../../es/lectures-2025-26/lecture-81-82.md)

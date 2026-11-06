---
title: "Lectures 71–72 — rearrangements of series, uniform convergence, properties of limit functions, functional series"
lang: en
course: "Mathematical Analysis, 2025/26"
lecture: 71-72
semester: 3
source: "handwritten notebook, pages p030–p041"
source_pages: "p030, p031, p034, p035, p036, p037, p038, p039, p040, p041"
course_chapter: 24
aliases: ["Lectures 71–72 (en)"]
tags: [mathinmind/en, mathinmind/lecture]
---
# Lectures 71–72 — rearrangements of series, uniform convergence, properties of limit functions, functional series

[[en/lectures-2025-26/lecture-69-70|← Lectures 69–70]] · [[en/lectures-2025-26/index|Lecture index]] · [[en/lectures-2025-26/lecture-73-74|Lectures 73–74 →]] · [[en/term-index|Terms & theorems]] · [[ru/lectures-2025-26/lecture-71-72|Русский]] · [[es/lectures-2025-26/lecture-71-72|Español]]

> [!info] Source and numbering
> These notes were copied from a handwritten notebook (pages p030, p031, p034–p041; the raw page text is in [`ocr/raw/`](https://github.com/NikiHunter/matan/blob/main/ocr/raw/p030.md); pages p032 and p033 are technical duplicates of p030 and p031). Page p030 begins with the end of §7.5 (an example of a rearrangement and the commutative properties of series); in the margin of the same page the record “Lectures 71–72” begins with the plan of the class: functional series; uniform convergence of functional sequences; the Bolzano–Cauchy criterion and the Weierstrass test; properties of uniformly convergent functional series. The transcription of page p031 breaks off at the word “Example:”, although the page contains the example $f_n(x)=x^n$ and two drawn “$\varepsilon$-tubes” (see [`ocr/MANIFEST.md`](https://github.com/NikiHunter/matan/blob/main/ocr/MANIFEST.md)); the example and the figures are restored from the slides of the 2024/25 course. The end of example 4 of §8.2 is written in the notebook on page p039, already after [[#^thm-8-2-3|Theorem 8.2.3]] and [[#^def-8-3-1|Definition 8.3.1]], and is kept in that place. Between pages p039 and p040 [[#^def-8-3-2|Definition 8.3.2]], the statement of the Bolzano–Cauchy criterion for the uniform convergence of a series and the beginning of its proof are lost; they are restored. The numbering of definitions and theorems is the lecturer's. Slips in the notes are corrected and marked with “Source correction” blocks; lost passages are restored and marked with “Restored” blocks; the tags match [`ocr/RESOLVED.md`](https://github.com/NikiHunter/matan/blob/main/ocr/RESOLVED.md). Places that still have to be checked against the notebook are listed in [`ocr/ISSUES.md`](https://github.com/NikiHunter/matan/blob/main/ocr/ISSUES.md).

## §7.5. Rearrangements of series (conclusion)


**Example.** The series
$$
\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k}=1-\frac12+\frac13-\frac14+\dots
$$
converges conditionally (it converges by the [[en/04-numeric-series#^alternating-series-test|Leibniz test]], while the series of absolute values — the harmonic series — diverges), and its sum is $\ln2$ (lectures 69–70). Denote its [[en/04-numeric-series#4.1 Convergence through partial sums|partial sums]]
$$
S_n=\sum_{k=1}^{n}\frac{(-1)^{k-1}}{k},\qquad S_n\to\ln2 .
$$

^p030

> [!info] Source correction
> (T506). The notes say “$S_n=\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k}$”. A partial sum is the sum of the first $n$ terms, so the [[en/lectures-2025-26/lecture-13#Definition 2.3.9 (upper and lower limits)|upper limit]] of summation is corrected to $n$.

Rearrange the terms of the series so that every positive term is followed by two negative ones:
$$
1-\frac12-\frac14+\frac13-\frac16-\frac18+\frac15-\frac1{10}-\frac1{12}+\dots
$$
The positive terms $\frac1{2k-1}$ and the negative terms $-\frac1{2k}$ keep their order, and every term of the original series occurs exactly once, so this is a rearrangement in the sense of [[en/lectures-2025-26/lecture-69-70#^def-7-5-1|Definition 7.5.1]]. Let $T_n$ be a partial sum of the new series.

Group the terms in threes: $T_{3m}=\left(1-\frac12-\frac14\right)+\left(\frac13-\frac16-\frac18\right)+\dots$; the $k$-th triple contains the positive term $\frac1{2k-1}$ and the negative terms $-\frac1{4k-2}$, $-\frac1{4k}$. Since $\frac1{2k-1}-\frac1{4k-2}=\frac2{4k-2}-\frac1{4k-2}=\frac1{4k-2}$, we get
$$
T_{3m}=\sum_{k=1}^{m}\left(\frac1{2k-1}-\frac1{4k-2}-\frac1{4k}\right)=\sum_{k=1}^{m}\left(\frac1{4k-2}-\frac1{4k}\right)=\frac12\sum_{k=1}^{m}\left(\frac1{2k-1}-\frac1{2k}\right)=\frac12\,S_{2m}.
$$
Since $S_n\to\ln2$,
$$
T_{3m}=\frac12\,S_{2m}\to\frac12\ln2,\qquad T_{3m+1}=T_{3m}+\frac1{2m+1}\to\frac12\ln2,\qquad T_{3m+2}=T_{3m+1}-\frac1{4m+2}\to\frac12\ln2 .
$$

> [!note] Restored
> (from the slides of the 2024/25 course, FS p60; the 2022 notes, M3S p58). The [[en/lectures-2025-26/lecture-11-12#^def-2-3-7|subsequences]] $(T_{3m})$, $(T_{3m+1})$, $(T_{3m+2})$ exhaust all indices and have a common limit, hence $T_n\to\frac12\ln2$. But $S_n\to\ln2$: rearranging the terms of a [[en/04-numeric-series#4.3 Absolute and conditional convergence|conditionally convergent]] series has changed its sum.

### Commutative properties of series

1. Positive series have the commutative property.
2. Absolutely convergent series have the commutative property.
3. Riemann's theorem. If a series converges conditionally, it does not have the commutative property. Moreover, for every $B\in\overline{\mathbb R}=\mathbb R\cup\{-\infty,+\infty\}$ there is a [[en/lectures-2025-26/lecture-01-02#^def-1-1-6|bijection]] $\sigma:\mathbb N\to\mathbb N$ such that $\sum_{n=1}^{\infty}a_{\sigma(n)}=B$.

> [!note] Restored
> (by the standard proof, cf. Zorich/Fichtenholz; in the notes and on the 2024/25 slides the properties are stated without proof).
>
> **Proof of property 1.** Let $a_n\ge0$, $A=\sum_{n=1}^{\infty}a_n\in[0,+\infty]$, and let $\sigma$ be a bijection. For every $N$ put $K=\max\{\sigma(1),\dots,\sigma(N)\}$; then $\sum_{n=1}^{N}a_{\sigma(n)}\le\sum_{k=1}^{K}a_k\le A$. The partial sums of the positive series $\sum a_{\sigma(n)}$ do not exceed $A$, hence $\sum a_{\sigma(n)}\le A$. The original series, in turn, is obtained from the series $\sum a_{\sigma(n)}$ by the rearrangement $\sigma^{-1}$, hence $A\le\sum a_{\sigma(n)}$ too. So the sums are equal (both finite or both equal to $+\infty$), i.e. the series converge and diverge simultaneously. $\square$
>
> **Proof of property 2.** Put $a_n^+=\max\{a_n,0\}$, $a_n^-=\max\{-a_n,0\}$; then $a_n=a_n^+-a_n^-$ and $0\le a_n^{\pm}\le|a_n|$. If the series $\sum|a_n|$ converges, then by the first comparison test the positive series $\sum a_n^+$ and $\sum a_n^-$ converge, and by property 1, for every bijection $\sigma$ the series $\sum a_{\sigma(n)}^{\pm}$ converge, with $\sum a_{\sigma(n)}^{\pm}=\sum a_n^{\pm}$ (and $\sum|a_{\sigma(n)}|=\sum|a_n|$, i.e. the rearrangement also converges absolutely). Therefore
> $$
> \sum_{n=1}^{\infty}a_{\sigma(n)}=\sum_{n=1}^{\infty}a_{\sigma(n)}^+-\sum_{n=1}^{\infty}a_{\sigma(n)}^-=\sum_{n=1}^{\infty}a_n^+-\sum_{n=1}^{\infty}a_n^-=\sum_{n=1}^{\infty}a_n .
> $$
> $\square$
>
> **Proof of Riemann's theorem.** Let the series $\sum a_n$ converge conditionally. Then $a_n\to0$ and $\sum a_n^+=\sum a_n^-=+\infty$: if, for example, the series $\sum a_n^+$ converged, then the series $\sum a_n^-=\sum(a_n^+-a_n)$ would converge, and with it $\sum|a_n|=\sum(a_n^++a_n^-)$ — a contradiction (similarly for $\sum a_n^-$). In particular, there are infinitely many non-negative terms and infinitely many negative terms. Write out, in increasing order of indices, the non-negative terms of the series $p_1,p_2,\dots$ and the absolute values of the negative terms $q_1,q_2,\dots$; then $p_k\to0$, $q_k\to0$ and $\sum p_k=\sum q_k=+\infty$.
>
> Let $B\in\mathbb R$. We take the terms $p_1,p_2,\dots$ one after another until the sum first exceeds $B$; then the terms $-q_1,-q_2,\dots$ until the sum first becomes smaller than $B$; then positive terms again, and so on. Each stage ends after finitely many steps, since $\sum p_k=\sum q_k=+\infty$, and from the second stage on each stage uses at least one term; hence the new series contains all the terms of the original series, each exactly once, i.e. it is a rearrangement. Within a stage the partial sums change monotonically, and at the end of a stage they differ from $B$ by at most the last term taken; therefore during a stage a partial sum differs from $B$ by at most the largest of the last terms taken at this and at the previous stage. Since $p_k\to0$ and $q_k\to0$, the partial sums tend to $B$.
>
> For $B=+\infty$ we take positive terms until the sum exceeds $1$, then one negative term, then positive terms until the sum exceeds $2$, then one negative term, and so on; the partial sums tend to $+\infty$. The case $B=-\infty$ is symmetric. Finally, taking any $B\ne\sum a_n$ we get a rearrangement with a different sum: the series does not have the commutative property. $\square$

## §8.1. Uniform convergence

Chapter 8 “Functional sequences and series” begins. Consider a sequence of functions $(f_n)_{n\in\mathbb N}$, $f_n:X\to\mathbb R$, and a function $f:X\to\mathbb R$.

> [!info] Source correction
> (S129). The notes say “$f_n:X\to\overline{\mathbb R}$, $\overline{\mathbb R}:=\mathbb R\cup\{\pm\infty\}$”, and the same for $f$. Further on the differences $|f_n(x)-f(x)|$ are used everywhere, which are undefined for infinite values; on the slide of the 2024/25 course (FS p62) the functions are real-valued. Corrected to $f_n,f:X\to\mathbb R$.


> [!definition] Definition 8.1.1
> We say that the sequence $(f_n)$ converges on $X$ to $f$ pointwise if for each $x\in X$ the numerical sequence $a_n:=f_n(x)$ converges to the number $a:=f(x)$ as $n\to\infty$.

^def-8-1-1

> [!definition] Definition 8.1.1a
> $f_n\to f$ pointwise on the set $E\subset X$ if
> $$
> \forall x\in E\ \ \forall\varepsilon>0\ \ \exists N=N(x,\varepsilon)\ \ \forall n>N:\quad |f_n(x)-f(x)|<\varepsilon .
> $$

> [!definition] Definition 8.1.2
> $f_n\to f$ uniformly on the set $E\subset X$ if
> $$
> \forall\varepsilon>0\ \ \exists N=N(\varepsilon)\ \ \forall x\in E\ \ \forall n>N:\quad |f_n(x)-f(x)|<\varepsilon .
> $$

^def-8-1-2

Notation: $f_n\rightrightarrows f$ for uniform convergence, $f_n\to f$ for pointwise convergence. Let $E=X$. If $f_n\rightrightarrows f$ on $X$, then $f_n\to f$ pointwise on $X$: uniform convergence implies pointwise convergence (the index $N(\varepsilon)$ from [[#^def-8-1-2|Definition 8.1.2]] works in the definition of pointwise convergence for each $x$).

*The converse is false in general!*

> [!note] Restored
> (from the slides of the 2024/25 course, FS p62). The transcription of page p031 breaks off at the word “Example:”; according to the description of this page and of its duplicate p033 in [`ocr/MANIFEST.md`](https://github.com/NikiHunter/matan/blob/main/ocr/MANIFEST.md), it contains the example $f_n(x)=x^n$ and two drawn “$\varepsilon$-tubes”. They are given below according to the lecturer's notes to the slide.
>
> **Example.** $X=[0,1]$, $f_n(x)=x^n$. Then
> $$
> f_n(x)\xrightarrow[n\to\infty]{}f(x)=\begin{cases}0,&x\in[0,1),\\1,&x=1,\end{cases}
> $$
> i.e. the sequence converges pointwise on $[0,1]$; there is no uniform convergence on $[0,1]$ here (see example 3 in §8.2).
>
> *Figures in the notes (page p031).* In the first figure the graphs of $y=f(x)-\varepsilon$, $y=f(x)$, $y=f(x)+\varepsilon$ bound a strip (an “$\varepsilon$-tube”) around the graph of $f$ labelled “$\forall n>N$”: under uniform convergence, starting from some index $N+1$, the graphs of all the functions $f_n$ lie in this strip. In the second figure the points $x_1$, $x_2$ are marked with the labels “$\forall n>N_1$”, “$\forall n>N_2$”: for pointwise convergence the index $N_i$ depends on the point $x_i$.


Questions arise naturally. ^p034

1. Let $X\subset\mathbb R$ and let all $f_n$ be continuous (at a point or on a set). Will $f$ be continuous?
2. Let $X\subset\mathbb R$ and let all $f_n$ be [[en/lectures-2025-26/lecture-22-23#^def-3-2-1|differentiable]] (at a point or on a set). Will $f$ be differentiable? If so, is it true that $f_n'\to f'$?
3. Let all $f_n$ be integrable on $[a,b]$. Will $f$ be integrable? If so, is it true that $\int_a^bf_n\to\int_a^bf$?

### Uniform convergence in terms of an ε-neighbourhood

(On the course slides this item is called “Uniform convergence and the Chebyshev deviation”.) Consider functions $f,g:X\to\mathbb R$.

> [!definition] Definition 8.1.3
> The quantity
> $$
> \rho(f,g)=\sup_{x\in X}|f(x)-g(x)|
> $$
> is called the uniform deviation of the functions $f$ and $g$ (on the slides, the Chebyshev deviation).

^def-8-1-3

> [!info] Source correction
> (A134). In the notes the number is written as “Def (8.3)”; by its place in the exposition and by the slide of the 2024/25 course (FS p62) this is [[#^def-8-1-3|Definition 8.1.3]].

> [!definition] Definition 8.1.4
> $f_n\rightrightarrows f$ if for every $\varepsilon>0$ there is $N$ such that $\rho(f_n,f)<\varepsilon$ for all $n>N$.

^def-8-1-4

> [!definition] Definition 8.1.4a
> $f_n\rightrightarrows f$ if $\alpha_n:=\rho(f_n,f)\to0$ as $n\to\infty$.

> [!info] Source correction
> (M507). The notes say: “$f_n\to f$ if $\rho(f_n,f)\to0$”. What is being defined here is uniform convergence, so it must be $f_n\rightrightarrows f$ (as on the slide FS p62); pointwise convergence is not described by the condition $\rho(f_n,f)\to0$.

## §8.2. Uniform convergence and properties of limit functions

Let $f_n\to f$ on the set $X$, and let all $f_n$ have some property. The question is whether the limit function $f$ has the same property.

### Continuity of the limit function

> [!theorem] Theorem 8.2.1 (continuity of the limit function)
> Let
>
> 1. $f_n\in C([a,b])$ for all $n$;
> 2. $f_n\rightrightarrows f$ on $[a,b]$.

^thm-8-2-1

Then $f\in C([a,b])$.


**Proof.** Take an arbitrary point $x_0\in[a,b]$ and prove that $f$ is continuous at $x_0$, i.e. that
$$
\forall\varepsilon>0\ \ \exists\delta>0\ \ \forall x\in[a,b]:\quad |x-x_0|<\delta\ \Rightarrow\ |f(x)-f(x_0)|<\varepsilon .
$$
Take any $\varepsilon>0$. Since $f_n\rightrightarrows f$, there is $N=N\left(\frac\varepsilon3\right)$ such that $|f_n(x)-f(x)|<\frac\varepsilon3$ for all $n>N$ and all $x\in[a,b]$. ^p035

Fix some index $n>N$. The function $f_n$ is [[en/lectures-2025-26/lecture-16#^def-2-5-1|continuous at the point]] $x_0$ (recall that by hypothesis all $f_n$ are continuous), so there is $\delta=\delta\left(\frac\varepsilon3\right)>0$ such that $|f_n(x)-f_n(x_0)|<\frac\varepsilon3$ for all $x\in[a,b]$, $|x-x_0|<\delta$. Then for all such $x$
$$
\begin{aligned}
|f(x)-f(x_0)|&=|f(x)-f_n(x)+f_n(x)-f_n(x_0)+f_n(x_0)-f(x_0)|\\
&\le|f(x)-f_n(x)|+|f_n(x)-f_n(x_0)|+|f_n(x_0)-f(x_0)|<\frac\varepsilon3+\frac\varepsilon3+\frac\varepsilon3=\varepsilon .
\end{aligned}
$$
$\square$

**Corollary.** Let $f_n\in C([a,b])$ for all $n$ and $f_n\rightrightarrows f$ on $[a,b]$. Then for every point $x_0\in[a,b]$
$$
\lim_{x\to x_0}\lim_{n\to\infty}f_n(x)=\lim_{n\to\infty}\lim_{x\to x_0}f_n(x).
$$

> [!info] Source correction
> (M508). In the statement of the corollary in the notes the point $x_0$ is not introduced; “for every point $x_0\in[a,b]$” has been added (the limits in $x\to x_0$ are taken over $x\in[a,b]$).

**Proof.** Uniform convergence implies pointwise convergence, so $\lim_{n\to\infty}f_n(x)=f(x)$ for each $x\in[a,b]$. By [[#^thm-8-2-1|Theorem 8.2.1]] the function $f$ is continuous, so $\lim_{x\to x_0}f(x)=f(x_0)$. Hence
$$
\lim_{x\to x_0}\lim_{n\to\infty}f_n(x)=\lim_{x\to x_0}f(x)=f(x_0).
$$
On the other hand, by the continuity of $f_n$ we have $\lim_{x\to x_0}f_n(x)=f_n(x_0)$, and $\lim_{n\to\infty}f_n(x_0)=f(x_0)$, since uniform convergence implies pointwise convergence. Hence
$$
\lim_{n\to\infty}\lim_{x\to x_0}f_n(x)=\lim_{n\to\infty}f_n(x_0)=f(x_0).
$$
The [[en/lectures-2025-26/lecture-57-58#^def-5-4-2|iterated limits]] coincide. $\square$


### Passage to the limit under the integral sign

> [!theorem] Theorem 8.2.2 (passage to the limit under the integral sign)
> Let
>
> 1. $f_n\in C([a,b])$ for all $n$;
> 2. $f_n\rightrightarrows f$ on $[a,b]$.

^thm-8-2-2

Then $\int_a^bf_n(x)\,dx\to\int_a^bf(x)\,dx$ as $n\to\infty$, or
$$
\lim_{n\to\infty}\int_a^bf_n(x)\,dx=\int_a^b\Bigl(\lim_{n\to\infty}f_n(x)\Bigr)dx .
$$

**Proof.** By [[#^thm-8-2-1|Theorem 8.2.1]] $f\in C([a,b])$; in particular, $f$ is integrable on $[a,b]$. We have
$$
\Bigl|\int_a^bf_n-\int_a^bf\Bigr|=\Bigl|\int_a^b(f_n-f)\Bigr|\le\int_a^b|f_n-f| .
$$
If $|f_n-f|<\varepsilon$ everywhere on $[a,b]$, then the last integral is smaller than $\varepsilon(b-a)$; so it is convenient to take $\frac{\varepsilon}{b-a}$ instead of $\varepsilon$. By hypothesis $f_n\rightrightarrows f$ on $[a,b]$, i.e. for every $\varepsilon>0$ there is $N$ such that $|f_n(x)-f(x)|<\frac{\varepsilon}{b-a}$ for all $n>N$ and all $x\in[a,b]$. Then for $n>N$
$$
\Bigl|\int_a^bf_n-\int_a^bf\Bigr|\le\int_a^b|f_n-f|<\int_a^b\frac{\varepsilon}{b-a}\,dx=\frac{\varepsilon}{b-a}\,(b-a)=\varepsilon ,
$$
i.e. $\int_a^bf_n\to\int_a^bf$ as $n\to\infty$. $\square$

**Remark.** In the proof of [[#^thm-8-2-2|Theorem 8.2.2]] not only pointwise but uniform convergence was important. The following examples show that pointwise convergence alone is not enough.

**Example 1.** $f_n(x)=n^2x(1-x^2)^n$, $x\in[0,1]$. For each $x\in[0,1]$ we have $f_n(x)\to0$ as $n\to\infty$, i.e. the sequence $(f_n)$ converges pointwise to $0$ on $[0,1]$. At the same time
$$
\begin{aligned}
\int_0^1f_n&=n^2\int_0^1x(1-x^2)^n\,dx=\frac{n^2}{2}\int_0^1(1-x^2)^n\,d(x^2)=-\frac{n^2}{2}\cdot\frac{(1-x^2)^{n+1}}{n+1}\bigg|_0^1\\
&=\frac{n^2}{2(n+1)}\xrightarrow[n\to\infty]{}+\infty ,
\end{aligned}
$$
while the integral of the limit function equals $0$. The contradiction with the conclusion of [[#^thm-8-2-2|Theorem 8.2.2]] shows that the convergence $f_n\to0$ on $[0,1]$ is not uniform.


**Example 2.** $f_n(x)=nx(1-x^2)^n$, $x\in[0,1]$. The sequence $(f_n)$ converges pointwise to $0$ on $[0,1]$, but
$$
\int_0^1f_n=n\int_0^1x(1-x^2)^n\,dx=\frac{n}{2(n+1)}\xrightarrow[n\to\infty]{}\frac12\ne0 .
$$
Here the integrals have a finite limit, but it is not equal to the integral of the limit function. ^p037

**Example 3.** $f_n(x)=x^n$ on $[0,1]$. The limit function is
$$
f(x)=\begin{cases}0,&x\in[0,1),\\1,&x=1.\end{cases}
$$
Since $|f_n(x)-f(x)|=x^n$ for $x\in[0,1)$ and $|f_n(1)-f(1)|=0$,
$$
\sup_{[0,1]}|f_n-f|=\sup_{x\in[0,1)}x^n=1\not\to0 ,
$$
i.e. $\rho(f_n,f)\not\to0$, and the convergence on $[0,1]$ is not uniform. But for every $q\in(0,1)$
$$
\sup_{[0,q]}|f_n-f|=\sup_{[0,q]}x^n=q^n\xrightarrow[n\to\infty]{}0 ,
$$
hence $f_n\rightrightarrows0$ on $[0,q]$.

**Example 4.** $f_n:[0,1]\to\mathbb R$, $f_n(0)=0$, $f_n(x)=0$ for $x>\frac1n$, while on the interval $\left(0,\frac1n\right)$ the function is positive: its graph is a “tooth”, a triangle with base $\left[0,\frac1n\right]$ and apex of height $n$.

*Figure in the notes (page p037): coordinate axes, a triangular “tooth” over the segment $[0,1/n]$; the height of the apex $n$ is marked on the vertical axis.*

> [!note] Restored
> (from the figure; in the transcription the value on $(0,1/n)$ is not read, the lecturer wrote “$>0$, $0<x<1/n$”, M3S p72). An explicit formula for the “tooth” with apex at the point $\frac1{2n}$:
> $$
> f_n(x)=\begin{cases}2n^2x,&0\le x\le\frac1{2n},\\ 2n-2n^2x,&\frac1{2n}\le x\le\frac1n,\\ 0,&\frac1n\le x\le1;\end{cases}
> $$
> all $f_n$ are continuous on $[0,1]$.

The end of example 4 is written in the notebook after [[#^thm-8-2-3|Theorem 8.2.3]] (page p039) and is given below in its place.


### Differentiation of the limit function

> [!theorem] Theorem 8.2.3 (differentiation of the limit function)
> Let
>
> 1. $f_n\in C^1([a,b])$ for all $n$;
> 2. $f_n\to f$ (pointwise on $[a,b]$) as $n\to\infty$;
> 3. $f\in C^1([a,b])$;
> 4. $f_n'\rightrightarrows\varphi$ on $[a,b]$.

^thm-8-2-3

Then $\varphi\in C([a,b])$ and $f'=\varphi$, or
$$
\frac{d}{dx}\Bigl(\lim_{n\to\infty}f_n(x)\Bigr)=\lim_{n\to\infty}\Bigl(\frac{d}{dx}f_n(x)\Bigr).
$$

> [!info] Source correction
> (A143). Condition 3 is written both in the notes and on the slide of the 2024/25 course (FS p65), but it is not used in the proof and follows from the other conditions: the proof shows that $f(x)=f(a)+\int_a^x\varphi$ with a continuous $\varphi$, whence $f\in C^1([a,b])$. So the theorem holds without condition 3, and $f\in C^1([a,b])$ can be included in the conclusion.

**Proof.** By the Newton–Leibniz formula $\int_a^bf_n'=f_n(b)-f_n(a)$; replacing $b$ by an arbitrary $x\in[a,b]$, we get $\int_a^xf_n'=f_n(x)-f_n(a)$, i.e.
$$
f_n(x)=f_n(a)+\int_a^xf_n'(t)\,dt\qquad(x\in[a,b]).
$$
Let $n\to\infty$: $f_n(x)\to f(x)$ and $f_n(a)\to f(a)$ by condition 2, and $\int_a^xf_n'\to\int_a^x\varphi$ by [[#^thm-8-2-2|Theorem 8.2.2]] on passing to the limit under the integral sign (applied on the segment $[a,x]$: $f_n'\in C([a,x])$, $f_n'\rightrightarrows\varphi$ on $[a,x]$). We get
$$
f(x)=f(a)+\int_a^x\varphi(t)\,dt\qquad(x\in[a,b]).
$$

> [!note] Restored
> (from the slides of the 2024/25 course, FS p65; in the notes the proof breaks off at this formula). The function $\varphi$ is continuous on $[a,b]$ by [[#^thm-8-2-1|Theorem 8.2.1]] (as a [[en/10-function-sequences-series#^uniform-limit-continuity|uniform limit of continuous functions]] $f_n'$). By Barrow's theorem the integral of a continuous function with a variable upper limit is differentiable and $\frac{d}{dx}\int_a^x\varphi(t)\,dt=\varphi(x)$. Therefore
> $$
> f'(x)=\frac{d}{dx}\Bigl(f(a)+\int_a^x\varphi(t)\,dt\Bigr)=\varphi(x),\qquad x\in[a,b],
> $$
> i.e. $f'=\varphi$ (and, consequently, $f\in C^1([a,b])$). $\square$

## §8.3. Functional series

> [!definition] Definition 8.3.1
> Let a sequence of functions $u_n:X\to\mathbb R$, $n\in\mathbb N$, be given. The expression $\sum_{n=1}^{\infty}u_n(x)$ is called a functional series. Put
> $$
> S_n(x)=\sum_{k=1}^{n}u_k(x),\qquad S(x)=\lim_{n\to\infty}S_n(x),\qquad S:X\to\mathbb R .
> $$
> A functional series is called convergent on the set $X$ if it converges at every point of this set.

^def-8-3-1


**Example 4 (conclusion).** Let us return to the “teeth” of §8.2. For every $x>0$ and all $n>\frac1x$ we have $x>\frac1n$, i.e. $f_n(x)=0$; moreover, $f_n(0)=0$. Hence $f_n\to0$ pointwise on $[0,1]$, i.e. $f=\lim_{n\to\infty}f_n=0$. But (the area of a triangle with base $\frac1n$ and height $n$)
$$
\int_0^1f_n(x)\,dx=\frac12\cdot\frac1n\cdot n=\frac12\not\to0,\qquad \int_0^1f(x)\,dx=0 ,
$$
i.e. $\int_0^1f_n\not\to\int_0^1f$. By [[#^thm-8-2-2|Theorem 8.2.2]] this means that the convergence $f_n\to0$ on $[0,1]$ is not uniform. ^p039

> [!note] Restored
> (from the slides of the 2024/25 course, FS p66; cf. the 2022 notes, M3S p76–p78). Between pages p039 and p040 the notebook has lost the definition of a uniformly convergent series, the statement about the remainder of the series, the statement of the Bolzano–Cauchy criterion and the beginning of its proof (page p040 starts in the middle of the proof of necessity).
>
> **Definition 8.3.2.** The series $\sum_{n=1}^{\infty}u_n(x)$ is called uniformly convergent on the set $E\subset X$ if $S_n\rightrightarrows S$ on $E$.
>
> The function $r_n(x):=\sum_{k=n+1}^{\infty}u_k(x)=S(x)-S_n(x)$ is called the remainder of the functional series; the series $\sum_{n=1}^{\infty}u_n(x)$ converges uniformly on the set $E$ if and only if $r_n\rightrightarrows0$ on $E$.
>
> *The Bolzano–Cauchy criterion (for the uniform convergence of a functional series).* The series $\sum_{n=1}^{\infty}u_n(x)$ converges uniformly on the set $E$ if and only if
> $$
> \forall\varepsilon>0\ \ \exists N\ \ \forall n>m>N\ \ \forall x\in E:\quad |S_n(x)-S_m(x)|<\varepsilon .
> $$
>
> **Proof.** *Necessity.* Let the series converge uniformly on $E$, i.e. $S_n\rightrightarrows S$ on $E$. For $\varepsilon>0$ there is $N$ such that $|S_n(x)-S(x)|<\frac\varepsilon2$ for all $x\in E$ and all $n>N$; in particular, for $n>m>N$ also $|S_m(x)-S(x)|<\frac\varepsilon2$. Then for all $n>m>N$ and $x\in E$

^def-8-3-2


$$
|S_n(x)-S_m(x)|=|S_n(x)-S(x)+S(x)-S_m(x)|\le|S_n(x)-S(x)|+|S(x)-S_m(x)|<\frac\varepsilon2+\frac\varepsilon2=\varepsilon .
$$

^p040

*Sufficiency.* Fix $x\in E$. Then $(S_n(x))_{n\in\mathbb N}$ is a numerical [[en/lectures-2025-26/lecture-13#^def-2-3-10|Cauchy sequence]], and by the Bolzano–Cauchy criterion for numerical sequences there is $S(x)$ such that $S_n(x)\to S(x)$. Since the fixed $x\in E$ was arbitrary, $S$ is a function on $E$, and the series converges to it pointwise. Further, by hypothesis, for every $\varepsilon>0$ there is $N$ such that $|S_n(x)-S_m(x)|<\varepsilon$ for all $x\in E$ and all $n>m>N$. Let $n\to\infty$ in this inequality (passage to the limit in an inequality): $|S(x)-S_m(x)|\le\varepsilon<2\varepsilon$ for all $x\in E$ and all $m>N$. This means exactly that $S_m\rightrightarrows S$ on $E$, i.e. the series converges uniformly. $\square$

Thus the Bolzano–Cauchy criterion is proved (in the notes it is written out after the proof): the series $\sum_{n=1}^{\infty}u_n(x)$ converges uniformly on $E$ if and only if for every $\varepsilon>0$ there is $N$ such that $|S_n(x)-S_m(x)|<\varepsilon$ for all $n>m>N$ and all $x\in E$, where $S_n(x)=\sum_{k=1}^{n}u_k(x)$, $S_m(x)=\sum_{k=1}^{m}u_k(x)$.

> [!info] Source correction
> (M509). In the statement of the criterion in the notes the [[en/01-logic-sets-functions#1.1 Propositions and quantifiers|quantifier]] “$\forall x\in E$” is missing: “$\forall\varepsilon>0\ \exists N\ \forall n>m>N\ |S_n(x)-S_m(x)|<\varepsilon$”. Without it (or if $N$ depends on $x$) the condition expresses only pointwise convergence; the quantifier is added, as in the proof and on the slide FS p66.

This criterion is usually used to disprove the uniform convergence of a series.

**Example.** The series $\sum_{k=0}^{\infty}x^k$ converges to $\frac1{1-x}$ on $[0,1)$ non-uniformly, since $x^k$ does not converge to zero uniformly on $[0,1)$.

> [!note] Restored
> (by the standard argument; in the notes the connection with the criterion is not spelled out). If the series $\sum u_k(x)$ converges uniformly on $E$, then taking $n=m+1$ in the Bolzano–Cauchy criterion we get $|u_{m+1}(x)|=|S_{m+1}(x)-S_m(x)|<\varepsilon$ for all $m>N$ and $x\in E$, i.e. $u_k\rightrightarrows0$ on $E$. Here, however, $\sup_{x\in[0,1)}x^k=1$ for all $k$, so $x^k$ does not converge to zero uniformly on $[0,1)$, and the series cannot converge uniformly.

### The Weierstrass test

Let a sequence of functions $u_n:X\to\mathbb R$, $n\in\mathbb N$, and a numerical sequence $(C_n)_{n\in\mathbb N}$, $C_n>0$, be given such that

1. $|u_n(x)|\le C_n$ for all $x\in E\subset X$ and all $n\in\mathbb N$;
2. the series $\sum_{n=1}^{\infty}C_n$ converges.

Then the series $\sum_{n=1}^{\infty}u_n(x)$ converges uniformly on $E$.

**Proof.**


For any $m\in\mathbb N$, $p\in\mathbb N$ and $x\in E$, by condition 1
$$
\Bigl|\sum_{n=m+1}^{m+p}u_n(x)\Bigr|\le\sum_{n=m+1}^{m+p}|u_n(x)|\le\sum_{n=m+1}^{m+p}C_n .
$$
By hypothesis the series $\sum C_n$ converges, so by the Bolzano–Cauchy criterion for numerical series, for every $\varepsilon>0$ there is $N$ such that $\sum_{n=m+1}^{m+p}C_n<\varepsilon$ for all $m>N$ and $p\in\mathbb N$. Then for all $m>N$, $p\in\mathbb N$ and $x\in E$
$$
|S_{m+p}(x)-S_m(x)|=\Bigl|\sum_{k=m+1}^{m+p}u_k(x)\Bigr|\le\sum_{k=m+1}^{m+p}C_k<\varepsilon .
$$
Note that here $n=m+p$ in the Bolzano–Cauchy criterion (every $n>m>N$ has this form). By the Bolzano–Cauchy criterion for functional series, the series $\sum_{n=1}^{\infty}u_n(x)$ converges uniformly on $E$. $\square$ ^p041

> [!info] Source correction
> (M510). In the notes the last estimate is written as “$\left|\sum_{n=m+1}^{m+p}u_n(x)\right|\le\left|\sum_{k=m+1}^{m+p}u_k(x)\right|<\varepsilon$” — the same sum stands on both sides, and the needed link (the comparison with $\sum C_k$) is missing; corrected according to the lecturer's note (FS p67). Moreover, the margin has “$p>1$” instead of $p\in\mathbb N$ ($p\ge1$).

**Examples.** The series $\sum_{k=1}^{\infty}\frac{\sin kx}{k^2}$ and $\sum_{k=1}^{\infty}\frac{\cos kx}{k^2}$ converge uniformly on $\mathbb R$ by the Weierstrass test, since for all $x\in\mathbb R$ ($E=\mathbb R$)
$$
\left|\frac{\sin kx}{k^2}\right|\le\frac1{k^2},\qquad \left|\frac{\cos kx}{k^2}\right|\le\frac1{k^2},
$$
and the series $\sum\frac1{k^2}$ converges.

**Remark.** Under the hypotheses of the Weierstrass test the series $\sum_{k=1}^{\infty}u_k(x)$ converges on $E$ not only uniformly but also absolutely. Moreover, the series $\sum_{k=1}^{\infty}|u_k(x)|$ also converges uniformly on $E$, since it satisfies the hypotheses of the Weierstrass test (with the same $C_k$).

**Remark.** Uniform and absolute convergence do not imply each other.

1. There are series that converge absolutely but not uniformly. For example, $\sum_{k=0}^{\infty}x^k$ on $(-1,1)$.
2. There are series that converge uniformly but not absolutely. For example, any conditionally convergent numerical series regarded as a functional one (with constant terms).

### Continuity of the sum of a uniformly convergent series

> [!theorem] Theorem 8.3.1
> Let a series of functions $u_n\in C([a,b])$, $n\in\mathbb N$, be given, and $\sum_{n=1}^{\infty}u_n(x)=S(x)$. If the series $\sum_{n=1}^{\infty}u_n(x)$ converges uniformly on $[a,b]$, then $S\in C([a,b])$.

^thm-8-3-1

**Proof.** The partial sums $S_n(x)=u_1(x)+u_2(x)+\dots+u_n(x)$ are continuous on $[a,b]$ as finite sums of continuous functions: $S_n\in C([a,b])$ for all $n\in\mathbb N$. Moreover, $S(x)=\lim_{n\to\infty}S_n(x)$ for all $x\in[a,b]$. By hypothesis the series $\sum_{k=1}^{\infty}u_k(x)$ converges uniformly on $[a,b]$, i.e. $S_n\rightrightarrows S$ on $[a,b]$. By [[#^thm-8-2-1|Theorem 8.2.1]] (continuity of the limit function) $S\in C([a,b])$. $\square$

## Cross-references

- Course topic: [[en/10-function-sequences-series|chapter 10 “Sequences and series of functions”]] — [[en/10-function-sequences-series#10.1 Two modes of convergence|§10.1 “Two kinds of convergence”]], [[en/10-function-sequences-series#10.2 Uniform Cauchy criterion|§10.2 “The uniform Cauchy criterion”]], [[en/10-function-sequences-series#^weierstrass-m-test|the Weierstrass test]], [[en/10-function-sequences-series#10.3 Continuity and integration|§10.3 “Continuity and integration”]], [[en/10-function-sequences-series#10.4 Differentiation|§10.4 “Differentiation”]].
- Rearrangements of series: [[en/lectures-2025-26/lecture-69-70#^def-7-5-1|Definitions 7.5.1]] and [[en/lectures-2025-26/lecture-69-70#^def-7-5-2|7.5.2]], the Leibniz test and the sum of the series $\sum\frac{(-1)^{k-1}}{k}=\ln2$ — [[en/lectures-2025-26/lecture-69-70|lectures 69–70]]; [[en/04-numeric-series#^rearrangement-warning|rearrangements of the terms of a series]] in chapter 4.
- Facts used: [[en/lectures-2025-26/lecture-13#^thm-2-3-7|Theorem 2.3.7]], the Bolzano–Cauchy criterion for sequences; [[en/lectures-2025-26/lecture-43-44#^thm-4-3-2|Theorem 4.3.2]], the Newton–Leibniz formula; Barrow's theorem — [[en/lectures-2025-26/lecture-43-44|lectures 43–44]].
- Continuation of §8.3 (termwise integration and differentiation of series, [[en/11-power-series#11.1 Radius of convergence|power series]]): [[en/lectures-2025-26/lecture-73-74|lectures 73–74]].

---

[[en/lectures-2025-26/lecture-69-70|← Lectures 69–70]] · [[en/lectures-2025-26/index|Lecture index]] · [[en/lectures-2025-26/lecture-73-74|Lectures 73–74 →]] · [[en/term-index|Terms & theorems]] · [[ru/lectures-2025-26/lecture-71-72|Русский]] · [[es/lectures-2025-26/lecture-71-72|Español]]

---
title: "Lectures 73–74 — properties of uniformly convergent series, power series, Abel's theorem"
lang: en
course: "Mathematical Analysis, 2025/26"
lecture: 73-74
semester: 3
source: "handwritten notebook, pages p042–p049"
source_pages: "p042, p044, p045, p046, p047, p048, p049"
course_chapter: 24
aliases: ["Lectures 73–74 (en)"]
tags: [mathinmind/en, mathinmind/lecture]
---
# Lectures 73–74 — properties of uniformly convergent series, power series, Abel's theorem

[[en/lectures-2025-26/lecture-71-72|← Lectures 71–72]] · [[en/lectures-2025-26/index|Lecture index]] · [[en/term-index|Terms & theorems]] · [[ru/lectures-2025-26/lecture-73-74|Русский]] · [[es/lectures-2025-26/lecture-73-74|Español]]

> [!info] Source and numbering
> These notes were copied from a handwritten notebook (pages p042, p044–p049; the raw page text is in [`ocr/raw/`](https://github.com/NikiHunter/matan/blob/main/ocr/raw/p042.md); page p043 is a technical duplicate of p042). The record “Lectures 73–74” begins in the margin of page p042 with the plan of the class: properties of uniformly convergent functional series; the Cauchy–Hadamard formula; power series; Abel's theorem. [[#^thm-8-3-2|Theorem 8.3.2]] is written twice on page p042 (at the end of the previous class and once more — with a heading and the hypothesis — before the proof) and is given here once. In the notebook the coefficients of a power series are denoted $C_k$; here, as on the lecturer's slides, they are denoted $c_k$ (the letter $C_n$ denotes the majorants in the [[en/10-function-sequences-series#^weierstrass-m-test|Weierstrass test]]). The numbering of definitions and theorems is the lecturer's. Slips in the notes are corrected and marked with “Source correction” blocks; lost passages are restored and marked with “Restored” blocks; the tags match [`ocr/RESOLVED.md`](https://github.com/NikiHunter/matan/blob/main/ocr/RESOLVED.md). Places that still have to be checked against the notebook are listed in [`ocr/ISSUES.md`](https://github.com/NikiHunter/matan/blob/main/ocr/ISSUES.md).

## §8.3. Functional series (conclusion)


### Integration of uniformly convergent series

> [!theorem] Theorem 8.3.2 (termwise integration)
> Let $u_n\in C([a,b])$ for all $n\in\mathbb N$, and $\sum_{n=1}^{\infty}u_n(x)=S(x)$. If the series $\sum_{n=1}^{\infty}u_n(x)$ converges uniformly on $[a,b]$, then
> $$
> \int_a^b S(x)\,dx=\sum_{n=1}^{\infty}\int_a^b u_n(x)\,dx .
> $$

^thm-8-3-2

**Proof.** Put $S_n(x)=u_1(x)+u_2(x)+\dots+u_n(x)$. The functions $S_n$ are continuous on $[a,b]$ as finite sums of continuous functions, and by the linearity of the integral
$$
\int_a^b S_n(x)\,dx=\int_a^b u_1(x)\,dx+\int_a^b u_2(x)\,dx+\dots+\int_a^b u_n(x)\,dx=\sum_{k=1}^{n}\int_a^b u_k(x)\,dx .
$$
By hypothesis $S_n\rightrightarrows S$ on $[a,b]$, so by [[en/lectures-2025-26/lecture-71-72#^thm-8-2-2|Theorem 8.2.2]] (passage to the limit under the integral sign) the left-hand side tends to $\int_a^b S(x)\,dx$ as $n\to\infty$. The right-hand side is the $n$-th [[en/04-numeric-series#4.1 Convergence through partial sums|partial sum]] of the numerical series $\sum_{k=1}^{\infty}\int_a^b u_k(x)\,dx$; hence it has the same limit, i.e. this series converges and
$$
\int_a^b S(x)\,dx=\sum_{k=1}^{\infty}\int_a^b u_k(x)\,dx .
$$
$\square$

**Remark.** [[en/10-function-sequences-series#10.1 Two modes of convergence|Uniform convergence]], and even convergence at every point, is not a necessary condition for termwise integration of a series.


In other words (a note in red in the margin), if a series can be integrated termwise, this does not mean that it converges uniformly: the equality $\sum_{n=1}^{\infty}\int_a^b u_n(x)\,dx=\int_a^b S(x)\,dx$ does not imply that the series $\sum_{n=1}^{\infty}u_n(x)$ converges uniformly on $[a,b]$. ^p044

> [!info] Source correction
> (M164). The notes say “$\sum_{n=1}^{\infty}\int_a^bu_n(x)\,dx-\int_a^bS(x)\,dx\nRightarrow\sum_{n=1}^{\infty}u_n(x)$ conv. unif. on $[a,b]$”. Between the sum of the integrals and the integral of the sum there must be an equality sign — what is meant is the equality of [[#^thm-8-3-2|Theorem 8.3.2]] (as in the lecturer's note, M3S p86).

**Example.** For each $x\in(-1,1)$ the series $\sum_{k=0}^{\infty}(-1)^kx^k=1-x+x^2-\dots$ (a geometric progression with ratio $-x$) converges to $\frac1{1+x}$, while for $x=1$ the series $\sum_{k=0}^{\infty}(-1)^k$ diverges. But
$$
\int_0^1\frac{dx}{1+x}=\ln|1+x|\Big|_0^1=\ln2 ,
$$
and termwise integration over the segment $[0,1]$ gives the same number:
$$
\sum_{k=0}^{\infty}(-1)^k\int_0^1x^k\,dx=\sum_{k=0}^{\infty}\left.\frac{(-1)^kx^{k+1}}{k+1}\right|_0^1=\sum_{k=0}^{\infty}\frac{(-1)^k}{k+1}=1-\frac12+\frac13-\dots=\ln2
$$
(the sum of this series was computed in lectures 69–70).

> [!info] Source correction
> (T166). In the notes the last equality is written as “$\sum_{k=0}^{\infty}\frac{(-1)^k}{k+1}-\ln(2)$”; it should be “$=\ln2$”.

So there is no uniform convergence here: at the point $x=1$ the series even diverges, and on $[0,1)$ (and on $(-1,1)$) the convergence is non-uniform, since $\sup_{x\in[0,1)}|(-1)^kx^k|=1\not\to0$, i.e. the general term does not tend to zero uniformly. Nevertheless this series can be integrated termwise over the segment $[0,1]$ (the sum $\frac1{1+x}$ is defined on $[0,1)$; the value at one point does not affect the integral).

### Differentiation of uniformly convergent series

> [!theorem] Theorem 8.3.3 (termwise differentiation)
> Let $u_n\in C^1([a,b])$ for all $n\in\mathbb N$, and $\sum_{n=1}^{\infty}u_n(x)=S(x)$. If
>
> 1. the series $\sum_{n=1}^{\infty}u_n(x)$ converges (at every point of the segment $[a,b]$);
> 2. the series $\sum_{n=1}^{\infty}u_n'(x)$ converges uniformly on $[a,b]$,

^thm-8-3-3

then $S\in C^1([a,b])$ and
$$
\Bigl(\sum_{n=1}^{\infty}u_n(x)\Bigr)'=\sum_{n=1}^{\infty}u_n'(x)=S'(x),\qquad x\in[a,b].
$$

> [!info] Source correction
> (S169). The second assertion of the theorem is written in the margin as “$\sum u_n(x)=\sum u'_n(x)=S(x)$” — without the derivative signs; corrected according to the slide of the 2024/25 course (FS p69).

**Proof.** Put $S_n(x)=u_1(x)+\dots+u_n(x)$. Then $S_n\in C^1([a,b])$, and by condition 1 $S_n\to S$ pointwise on $[a,b]$. Further,
$$
S_n'(x)=u_1'(x)+\dots+u_n'(x),
$$
i.e. $S_n'$ are the partial sums of the series $\sum u_n'(x)$, and by condition 2, as $n\to\infty$, we have $S_n'\rightrightarrows\varphi$ on $[a,b]$, where $\varphi(x):=\sum_{n=1}^{\infty}u_n'(x)$.

By [[en/lectures-2025-26/lecture-71-72#^thm-8-2-3|Theorem 8.2.3]] (differentiation of the limit function), applied to the sequence $(S_n)$, we get
$$
S'(x)=\varphi(x)=\sum_{k=1}^{\infty}u_k'(x)\in C([a,b]).
$$
The condition “$S\in C^1([a,b])$” from the statement of [[en/lectures-2025-26/lecture-71-72#^thm-8-2-3|Theorem 8.2.3]] is not known in advance here, but it need not be checked: as noted after [[en/lectures-2025-26/lecture-71-72#^thm-8-2-3|Theorem 8.2.3]] (lectures 71–72), its proof gives $S(x)=S(a)+\int_a^x\varphi(t)\,dt$ without this condition. The function $\varphi$ is continuous by [[en/lectures-2025-26/lecture-71-72#^thm-8-2-1|Theorem 8.2.1]] as a [[en/10-function-sequences-series#^uniform-limit-continuity|uniform limit of continuous functions]] $S_n'$. Thus $S'=\varphi\in C([a,b])$, i.e. $S\in C^1([a,b])$, and $\bigl(\sum u_n\bigr)'=\sum u_n'$. $\square$


**Example.** The series $\sum_{k=1}^{\infty}1$ diverges, while the series of derivatives $\sum_{k=1}^{\infty}(1)'=\sum_{k=1}^{\infty}0$ converges uniformly on any interval.

^p045

> [!note] Restored
> (from the 2022 notes, M3S p84). Conclusion of the example: the functions $u_k\equiv1$ belong to $C^1$, the series of their derivatives converges uniformly, but the series $\sum u_k$ itself diverges. Therefore in [[#^thm-8-3-3|Theorem 8.3.3]] condition 1 (convergence of the series $\sum_{k=1}^{\infty}u_k(x)$) cannot be dropped.

## §8.4. Power series

> [!definition] Definition 8.4.1
> A series of the form
> $$
> \sum_{k=0}^{\infty}c_k(x-a)^k,\qquad\qquad(8.4.1)
> $$
> where $c_k,x,a\in\mathbb R$, is called a (real) power series; the numbers $c_k$ are called its coefficients, and $a$ its centre.

^def-8-4-1

A power series is a generalisation of the polynomial $\sum_{k=0}^{n}c_k(x-a)^k$ and reduces to it if $c_k=0$ from some index on.

> [!info] Source correction
> (T519). In the notes the polynomial is written as “$\sum_{k=0}^{\infty}C_k(x-a)^k$”. A polynomial is a finite sum, so the upper limit of summation is $n$ (as on the slide FS p72).

Note that for $x=a$ series (8.4.1) converges to the sum $c_0$, since the terms with indices $k\in\mathbb N$ vanish (here $(x-a)^0=1$).

### The radius of convergence

> [!definition] Definition 8.4.2
> The quantity $R\in[0,+\infty]$ is called the radius of convergence of the series $\sum_{k=0}^{\infty}c_k(x-a)^k$ if
>
> 1. the series converges for all $x$ such that $|x-a|<R$;
> 2. the series diverges for all $x$ such that $|x-a|>R$.

^def-8-4-2

**Remark.** The inequality $|x-a|<R$ defines on the real line the interval $(a-R,a+R)$ — the interval of convergence.

- If $R=+\infty$, the interval of convergence coincides with $\mathbb R$, and the series $\sum c_k(x-a)^k$ converges absolutely for all $x\in\mathbb R$.
- If $R=0$, the interval of convergence is empty, and the series converges only for $x=a$.
- If $0<R<+\infty$, the series $\sum c_k(x-a)^k$ converges absolutely for $|x-a|<R$ and diverges for $|x-a|>R$, i.e. it converges on the interval of convergence $(a-R,a+R)$ and diverges outside the segment $[a-R,a+R]$; at the endpoints $x=a\pm R$ both convergence and divergence are possible.

Absolute convergence for $|x-a|<R$ is justified below ([[#^rem-8-4-1|Remark 8.4.1]]).

> [!info] Source correction
> (S176). In the notes the last item ends with the words “i.e. the set of conv. $(a-R,a+R)$” (uncertain reading; the same in the 2022 notes, M3S p88). The set of convergence contains the interval $(a-R,a+R)$ and is contained in the segment $[a-R,a+R]$, but it may contain the endpoints: for example, the series $\sum_{k=1}^{\infty}\frac{x^k}{k^2}$ (example below) has $R=1$ and converges on the whole segment $[-1,1]$, since $\left|\frac{x^k}{k^2}\right|\le\frac1{k^2}$ for $|x|\le1$. The behaviour of the series at the points $x=a\pm R$ is not determined by the radius and is studied separately.


### The Cauchy–Hadamard formula

The following theorem uses the conventions $\frac1{+\infty}=0$, $\frac10=+\infty$.

> [!theorem] Theorem 8.4.1 (Cauchy–Hadamard formula)
> Every power series $\sum_{k=0}^{\infty}c_k(x-a)^k$ has a radius of convergence, and it is given by the formula
> $$
> R=\frac{1}{\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}} .
> $$

^thm-8-4-1

> [!info] Source correction
> (A178). In the notes (and further in the proof) an ordinary limit stands instead of the upper limit: “$R=\frac{1}{\lim_{n\to\infty}\sqrt[n]{|C_n|}}$”. The limit $\lim\sqrt[n]{|c_n|}$ does not always exist: for example, the series $1+x^2+x^4+\dots$ has coefficients alternately equal to $1$ and $0$, and $\sqrt[n]{|c_n|}$ takes the values $1$ and $0$. The upper limit ([[en/lectures-2025-26/lecture-13#Definition 2.3.9 (upper and lower limits)|Definition 2.3.9]]) always exists in $[0,+\infty]$; the Cauchy–Hadamard formula is written with it (as on the slide FS p73).

**Proof.** We prove that the quantity $R$ given by the Cauchy–Hadamard formula satisfies the definition of the radius of convergence. Put $L:=\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}\in[0,+\infty]$, so that $R=\frac1L$. For $x=a$ the series converges; let $x\ne a$. Consider
$$
K=\varlimsup_{n\to\infty}\sqrt[n]{|c_n(x-a)^n|}=\varlimsup_{n\to\infty}\bigl(|x-a|\sqrt[n]{|c_n|}\bigr)=|x-a|\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}=|x-a|\,L .
$$
The positive factor $|x-a|$ can be taken outside the upper limit, since $\sup_{k\ge n}\bigl(|x-a|\,y_k\bigr)=|x-a|\sup_{k\ge n}y_k$; if $L=+\infty$, then also $K=+\infty$ (for $\infty$ — by definition: $|x-a|\cdot(+\infty)=+\infty$ for $|x-a|>0$).

If $|x-a|<R$, then $K<1$: for $L=0$ we have $K=0$, and for $0<L<+\infty$ we have $K=|x-a|\,L<RL=1$ (the case $L=+\infty$ is impossible here, since then $R=0$). By the [[en/04-numeric-series#4.2 Nonnegative terms|Cauchy test]] the series $\sum|c_k(x-a)^k|$ converges, hence the series $\sum c_k(x-a)^k$ converges (absolutely).

If $|x-a|>R$, then $K>1$: for $L=+\infty$ we have $K=+\infty$, and for $0<L<+\infty$ we have $K=|x-a|\,L>RL=1$ (the case $L=0$ is impossible, since then $R=+\infty$). By the Cauchy test the terms of the series do not tend to zero, and the series $\sum c_k(x-a)^k$ diverges. $\square$

> [!note] Restored
> (by the standard proof, cf. Zorich/Fichtenholz). In lectures 69–70 the Cauchy test was proved in the case when the limit $\lim\sqrt[n]{a_n}$ exists; here it is applied in the form with the upper limit. *Let $a_n\ge0$ and $K=\varlimsup_{n\to\infty}\sqrt[n]{a_n}$. If $K<1$, the series $\sum a_n$ converges; if $K>1$, then $a_n\not\to0$.* Put $z_n=\sup_{k\ge n}\sqrt[k]{a_k}$; the sequence $(z_n)$ is non-increasing and $z_n\to K$. If $K<1$, take $q:=\frac{1+K}{2}\in(K,1)$; there is $N$ such that $z_N<q$, i.e. $a_k<q^k$ for all $k\ge N$, and by the first comparison test with the geometric progression $\sum q^k$ the series $\sum a_n$ converges. If $K>1$ (including $K=+\infty$), then $z_n\ge K>1$ for all $n$, i.e. for each $n$ there is $k\ge n$ with $\sqrt[k]{a_k}>1$; hence $a_k>1$ for infinitely many $k$, and $a_k\not\to0$. In the proof of [[#^thm-8-4-1|Theorem 8.4.1]] $a_n=|c_n(x-a)^n|$: for $K>1$ the terms $c_n(x-a)^n$ do not tend to zero, and the series $\sum c_n(x-a)^n$ diverges by the necessary condition for convergence.

### Absolute convergence of a power series

> [!remark] Remark 8.4.1
> By the Cauchy test, for $|x-a|<R$ the series $\sum_{k=0}^{\infty}c_k(x-a)^k$ converges absolutely (in the proof of Theorem 8.4.1 the convergence of the series $\sum|c_k(x-a)^k|$ was established for $|x-a|<R$).

^rem-8-4-1

### The interval of convergence

[[#^thm-8-4-1|Theorem 8.4.1]] allows us to draw conclusions about the convergence of a power series:

- the inequality $|x-a|<R$ defines on the real line the interval $(a-R,a+R)$, called the interval of convergence of the power series;
- if $R=+\infty$, the interval of convergence coincides with $\mathbb R$, and the series converges absolutely for all $x\in\mathbb R$;
- if $R=0$, the interval of convergence is empty, and the series converges only for $x=a$;
- if $R\in(0,+\infty)$, the series converges absolutely for $|x-a|<R$ and diverges for $|x-a|>R$.


### The radius of convergence and the d'Alembert test

Often the radius of convergence can be found not only by the Cauchy–Hadamard formula but also by the d'Alembert test. Namely,
$$
R=\lim_{n\to\infty}\left|\frac{c_n}{c_{n+1}}\right|,
$$
if the limit on the right exists.

> [!note] Restored
> (by the standard proof; in the notes and on the slide FS p74 the formula is given without justification). The existence of the limit presupposes that $c_n\ne0$ for all sufficiently large $n$; the limit may be infinite. Let $\lim_{n\to\infty}\left|\frac{c_n}{c_{n+1}}\right|=\rho\in[0,+\infty]$ and $x\ne a$. For the absolute values of the terms of the series $a_n=|c_n(x-a)^n|$
> $$
> \frac{a_{n+1}}{a_n}=|x-a|\left|\frac{c_{n+1}}{c_n}\right|\xrightarrow[n\to\infty]{}\frac{|x-a|}{\rho}
> $$
> (with the conventions $\frac{|x-a|}{+\infty}=0$, $\frac{|x-a|}{0}=+\infty$). If $|x-a|<\rho$, this limit is less than $1$, and by the d'Alembert test the series converges absolutely; if $|x-a|>\rho$, the limit is greater than $1$, then $a_{n+1}>a_n$ from some index on, the terms of the series do not tend to zero, and the series diverges. By [[#^def-8-4-2|Definition 8.4.2]] the number $\rho$ is the radius of convergence.

**Example.** For the series $\sum_{k=1}^{\infty}\frac{x^k}{k^2}$ we have $c_k=\frac1{k^2}$, $c_{k+1}=\frac1{(k+1)^2}$,
$$
R=\lim_{k\to\infty}\left|\frac{c_k}{c_{k+1}}\right|=\lim_{k\to\infty}\frac{(k+1)^2}{k^2}=1 .
$$
Thus $R=1$: the series converges for $|x|<1$ and diverges for $|x|>1$.

### A remark on the centre of a power series

> [!remark] Remark 8.4.2
> The substitution $x-a=y$ reduces series (8.4.1) to a power series in powers of $y$ with centre at zero:
> $$
> \sum_{k=0}^{\infty}c_k(x-a)^k\ \longrightarrow\ \sum_{k=0}^{\infty}c_ky^k,\qquad y=x-a .
> $$
> Therefore, when deriving the properties of power series, we may assume without loss of generality that $a=0$.

^rem-8-4-2

### Uniform convergence of a power series

> [!theorem] Theorem 8.4.2 (uniform convergence of power series)
> Let a power series $\sum_{k=0}^{\infty}c_k(x-a)^k$ be given, and let $R\in(0,+\infty]$ be its radius of convergence. Then for every $r\in(0,R)$ the power series converges uniformly on the set $|x-a|\le r$, i.e. on the segment $[a-r,a+r]\subset(a-R,a+R)$.

^thm-8-4-2

**Proof.** If $|x-a|\le r$, then
$$
|c_k(x-a)^k|=|c_k|\,|x-a|^k\le|c_k|\,r^k .
$$

*Figure in the notes (page p047): the points $a-R$, $a$, $a+r$, $a+R$ are marked on the number line; the segment $|x-a|\le r$ lies strictly inside the interval of convergence $(a-R,a+R)$.*

Since $0<r<R$, the point $x=a+r$ lies in the interval of convergence, and by [[#^rem-8-4-1|Remark 8.4.1]] the series $\sum_{k=0}^{\infty}c_kr^k$ converges absolutely, i.e. the series $\sum_{k=0}^{\infty}|c_k|\,r^k$ converges.


Recall the statement of the Weierstrass test (lectures 71–72): if $u_n:X\to\mathbb R$, $|u_n(x)|\le C_n$ for all $x\in E\subset X$ and all $n$, and the series $\sum_{n=1}^{\infty}C_n$ converges, then the series $\sum_{n=1}^{\infty}u_n(x)$ converges uniformly on $E$. Apply it to $u_k(x)=c_k(x-a)^k$, $C_k=|c_k|\,r^k$ and $E=\{x:|x-a|\le r\}$: by the Weierstrass test the series $\sum_{k=0}^{\infty}c_k(x-a)^k$ converges uniformly on the set $|x-a|\le r$. $\square$ ^p048

### Abel's theorem

> [!theorem] Theorem 8.4.3 (Abel's theorem on power series)
> Let a power series $\sum_{k=0}^{\infty}c_k(x-a)^k$ be given, and let $R\in(0,+\infty)$ be its radius of convergence. If the power series converges for $x=a+R$ (respectively for $x=a-R$), then it converges uniformly on the segment $[a,a+R]$ (respectively on $[a-R,a]$), and its sum is continuous from the left at the point $a+R$ (respectively from the right at the point $a-R$).

^thm-8-4-3

*Figure in the margin (page p048): the points $a-R$, $a$, $a+R$ are marked on the axis; under the endpoints of the interval the numerical series $\sum c_k(-R)^k$ and $\sum c_kR^k$ are written — the power series turns into them for $x=a-R$ and for $x=a+R$.*

The proof needs [[en/lectures-2025-26/lecture-49-50#^thm-4-5-4|Abel's test]] for uniform convergence (in the notes it is written as “Abel's theorem (hint)” and given without proof; on the slides, “Abel's theorem on the uniform convergence of series”).

### Abel's test for uniform convergence

Let

1. the series $\sum_{k=1}^{\infty}f_k(x)$ converge uniformly on $X$;
2. for each $x\in X$ the sequence $\{g_k(x)\}$ be monotone, and the sequence of functions $\{g_k\}$ be uniformly bounded on $X$, i.e. there is $M$ such that $|g_k(x)|\le M$ for all $k\in\mathbb N$ and all $x\in X$.

Then the series $\sum_{k=1}^{\infty}f_k(x)g_k(x)$ converges uniformly on $X$.

> [!note] Restored
> (by the standard proof, cf. Zorich/Fichtenholz; in the notes and on the slides the test is given without proof).
>
> **Proof.** Fix $n$ and put $F_n(x):=0$, $F_m(x):=\sum_{j=n+1}^{m}f_j(x)$ for $m>n$. Since $f_k=F_k-F_{k-1}$ for $k>n$, for $m>n$ (Abel's transformation, lectures 69–70)
> $$
> \sum_{k=n+1}^{m}f_k(x)g_k(x)=\sum_{k=n+1}^{m}\bigl(F_k(x)-F_{k-1}(x)\bigr)g_k(x)=F_m(x)g_m(x)+\sum_{k=n+1}^{m-1}F_k(x)\bigl(g_k(x)-g_{k+1}(x)\bigr).
> $$
> By the Bolzano–Cauchy criterion (for the uniformly convergent series $\sum f_k$), for every $\varepsilon>0$ there is $N$ such that $|F_k(x)|<\varepsilon$ for all $k>n>N$ and all $x\in X$. For fixed $x$ all the differences $g_k(x)-g_{k+1}(x)$ have the same sign (the sequence is monotone), so
> $$
> \sum_{k=n+1}^{m-1}\bigl|g_k(x)-g_{k+1}(x)\bigr|=\bigl|g_{n+1}(x)-g_m(x)\bigr|\le2M .
> $$
> Consequently, for all $m>n>N$ and all $x\in X$
> $$
> \Bigl|\sum_{k=n+1}^{m}f_k(x)g_k(x)\Bigr|\le\varepsilon M+\varepsilon\cdot2M=3M\varepsilon .
> $$
> Since $\varepsilon>0$ is arbitrary, by the Bolzano–Cauchy criterion the series $\sum_{k=1}^{\infty}f_k(x)g_k(x)$ converges uniformly on $X$. $\square$

**Proof of [[#^thm-8-4-3|Theorem 8.4.3]].** Without loss of generality $a=0$ ([[#^rem-8-4-2|Remark 8.4.2]]), i.e. we consider the series $\sum_{k=0}^{\infty}c_kx^k$. Let it converge at the point $x=R$. Transform the terms of the series:
$$
c_kx^k=c_kR^k\cdot\left(\frac{x}{R}\right)^k .
$$


$\sum_{k=0}^{\infty}c_kR^k$ is a numerical series, and it converges (by the hypothesis of the theorem the series $\sum c_k(x-a)^k$ converges for $x=a+R$). Since the terms $f_k(x):=c_kR^k$ of this series do not depend on $x$, its convergence can be regarded as uniform on $[0,R]$: the condition of the Bolzano–Cauchy criterion holds for all $x$ at once. ^p049

The sequence $g_k(x):=\left(\frac{x}{R}\right)^k$: if $0\le x\le R$, then $0\le\left(\frac{x}{R}\right)^k\le1$. Hence the sequence $\{g_k\}$ is uniformly bounded on $[0,R]$ and monotone for each $x\in[0,R]$ (non-increasing in $k$, since $0\le\frac xR\le1$).

> [!info] Source correction
> (U193, T195). The notes say: “$\sum_{k=0}^{\infty}R^k$ is a numerical series ⇒ its conv. can be regarded as unif[orm] on $[0,R]$” — meaning the series $\sum c_kR^k$ from the previous line (the factor $c_k$ is omitted); then “$0<x<R$, [then] $0\le(x/R)^k\le1$ ⇒ the seq. $(x/R)^k$ is bdd on $[0,R]$”. The estimate is needed on the whole segment $[0,R]$, including the endpoints, so the condition is $0\le x\le R$ (as in the lecturer's note, FS p76).

By Abel's test for uniform convergence the series $\sum_{k=0}^{\infty}c_kx^k=\sum_{k=0}^{\infty}c_kR^k\left(\frac xR\right)^k$ converges uniformly on $[0,R]$.

Continuity of the sum follows from the continuity of each term of the series $\sum c_kx^k$ and the uniform convergence of the series on $[0,R]$: by [[en/lectures-2025-26/lecture-71-72#^thm-8-3-1|Theorem 8.3.1]] the sum of the series is continuous on $[0,R]$, in particular [[en/lectures-2025-26/lecture-16#^def-2-5-1|continuous at the point]] $R$ from the left. $\square$

> [!note] Restored
> (by the standard argument; in the notes and in the lecturer's note only the case $x=a+R$ is worked out). Let the series converge for $x=a-R$, i.e. (for $a=0$) at the point $x=-R$. The power series $\sum_{k=0}^{\infty}(-1)^kc_kt^k$ has the same radius of convergence $R$ (by the Cauchy–Hadamard formula, since $|(-1)^kc_k|=|c_k|$) and converges for $t=R$. By what has been proved, it converges uniformly on $[0,R]$, and its sum is continuous from the left at the point $R$. Since $\sum(-1)^kc_kt^k=\sum c_k(-t)^k$, after the substitution $x=-t$ we get: the series $\sum c_kx^k$ converges uniformly on $[-R,0]$, and its sum is continuous from the right at the point $-R$.

### Examples of computing the radius of convergence

**Example 1.** $\sum_{n=0}^{\infty}(-2)^n(x-3)^n$. Here $c_n=(-2)^n$ and
$$
R=\lim_{n\to\infty}\left|\frac{c_n}{c_{n+1}}\right|=\lim_{n\to\infty}\frac{2^n}{2^{n+1}}=\frac12 .
$$
The interval of convergence is $\left(3-\frac12,\,3+\frac12\right)=(2{,}5;\ 3{,}5)$.

> [!info] Source correction
> (M197). The notes say “$R=\lim\left|\frac{C_n}{C_{n+1}}\right|=\lim\left(\frac{2^nn}{(-2)^{n+1}(n+1)}\right)=\lim\left|\frac{2}{2(n+1)}\right|=\frac12$”. For the series as written, $c_n=(-2)^n$: there are no factors $n$ and $n+1$, and $\left|\frac{c_n}{c_{n+1}}\right|=\frac12$ for all $n$; besides, $\lim\frac{2}{2(n+1)}=0$, not $\frac12$. The answer $R=\frac12$ is correct (the Cauchy–Hadamard formula gives the same: $\sqrt[n]{|c_n|}=2$; and for $c_n=(-2)^nn$ it would be $\left|\frac{c_n}{c_{n+1}}\right|=\frac{n}{2(n+1)}\to\frac12$).

**Example 2.** $\sum_{n=0}^{\infty}\left(-\frac32\right)^n(x-2)^n$. Here $c_n=\left(-\frac32\right)^n$, $\sqrt[n]{|c_n|}=\frac32$ for all $n$ and
$$
R=\frac{1}{\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}}=\frac{1}{3/2}=\frac23 .
$$
The interval of convergence is $\left(2-\frac23,\,2+\frac23\right)=\left(\frac43,\frac83\right)$.

> [!info] Source correction
> (T199, U200). The notes say “$R=\frac{1}{\lim\sqrt[n]{|C_n|}}=\frac{1}{\lim|3/2|^{n/n}}=\left|\frac23\right|=a$”, and then “The series conv. at $x=-2$, int[erval] of conv. $\varnothing$”. The radius $R=\frac23$ is found correctly (“$=a$” is a slip; here $\sqrt[n]{|c_n|}=\frac32$ for all $n$, so the limit exists and coincides with the upper one). The conclusion, however, contradicts the radius found: for $R=\frac23>0$ the interval of convergence $\left(\frac43,\frac83\right)$ is not empty. The conclusion “the interval of convergence is empty, the series converges at a single point” is correct for example 3, where $R=0$, and the only point of convergence is the centre $x=2$.

**Example 3.** $\sum_{n=0}^{\infty}2^{n^2}(x-2)^n$. Here $c_n=2^{n^2}$, $\sqrt[n]{|c_n|}=2^n\to+\infty$, hence
$$
R=\frac{1}{\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}}=\frac{1}{+\infty}=0 .
$$
The interval of convergence is empty: the series converges only for $x=2$ (at the centre).

> [!info] Source correction
> (T201). The notes say “$R=\frac{1}{\lim\sqrt[n]{|C_n|}}=\frac{1}{\lim2^n}=\infty$ — int. of conv. $\mathbb R$, conv. only on $\mathbb R$”. Since $2^n\to+\infty$, the convention $\frac1{+\infty}=0$ gives $R=0$, not $+\infty$. Check: for $x\ne2$ we have $|2^{n^2}(x-2)^n|=\bigl(2^n|x-2|\bigr)^n\ge1$ as soon as $2^n|x-2|\ge1$, i.e. for all sufficiently large $n$; the terms of the series do not tend to zero, and the series diverges.

> [!note] Restored
> (study of the endpoints of the intervals of convergence; not done in the notes). In example 1, for $x=\frac52$ the terms of the series equal $(-2)^n\left(-\frac12\right)^n=1$, and for $x=\frac72$ they equal $(-2)^n\left(\frac12\right)^n=(-1)^n$; in both cases they do not tend to zero, and the series diverges, so the set of convergence is the interval $\left(\frac52,\frac72\right)$. In example 2, for $x=\frac83$ the terms equal $\left(-\frac32\right)^n\left(\frac23\right)^n=(-1)^n$, and for $x=\frac43$ they equal $\left(-\frac32\right)^n\left(-\frac23\right)^n=1$; the series diverges at both endpoints, the set of convergence is $\left(\frac43,\frac83\right)$.

## Cross-references

- Course topic: [[en/10-function-sequences-series|chapter 10 “Sequences and series of functions”]] — [[en/10-function-sequences-series#10.3 Continuity and integration|§10.3 “Continuity and integration”]], [[en/10-function-sequences-series#10.4 Differentiation|§10.4 “Differentiation”]]; [[en/11-power-series|chapter 11 “Power series and analytic functions”]] — [[en/11-power-series#11.1 Radius of convergence|§11.1 “Radius of convergence”]], [[en/11-power-series#11.2 Uniform convergence and calculus|§11.2 “Uniform convergence and operations”]], [[en/11-power-series#^abel-theorem|Abel's theorem]].
- Facts used: [[en/lectures-2025-26/lecture-71-72#^thm-8-2-1|Theorems 8.2.1]]–[[en/lectures-2025-26/lecture-71-72#^thm-8-2-3|8.2.3]] and [[en/lectures-2025-26/lecture-71-72#^thm-8-3-1|8.3.1]], the Weierstrass test and the Bolzano–Cauchy criterion for uniform convergence — [[en/lectures-2025-26/lecture-71-72|lectures 71–72]]; the Cauchy and d'Alembert tests, Abel's transformation, the sum of the series $\sum\frac{(-1)^{k-1}}{k}=\ln2$ — [[en/lectures-2025-26/lecture-69-70|lectures 69–70]]; the [[en/lectures-2025-26/lecture-13#Definition 2.3.9 (upper and lower limits)|upper limit]] ([[en/lectures-2025-26/lecture-13#Definition 2.3.9 (upper and lower limits)|Definition 2.3.9]]).
- Continuation of §8.4 (integration and differentiation of power series, [[en/11-power-series#11.3 Standard expansions|Taylor series]], [[en/11-power-series#11.4 Analytic does not mean merely smooth|analytic functions]]): [[ru/lectures-2025-26/lecture-75-76|lectures 75–76]].

---

[[en/lectures-2025-26/lecture-71-72|← Lectures 71–72]] · [[en/lectures-2025-26/index|Lecture index]] · [[en/term-index|Terms & theorems]] · [[ru/lectures-2025-26/lecture-73-74|Русский]] · [[es/lectures-2025-26/lecture-73-74|Español]]

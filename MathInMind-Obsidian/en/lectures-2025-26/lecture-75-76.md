---
title: "Lectures 75–76 — integration and differentiation of power series, Taylor series, integrals depending on a parameter"
lang: en
course: "Mathematical Analysis, 2025/26"
lecture: 75-76
semester: 3
source: "handwritten notebook, pages p050–p057"
source_pages: "p050, p051, p052, p053, p054, p055, p056, p057"
course_chapter: 24
aliases: ["Lectures 75–76 (en)"]
tags: [mathinmind/en, mathinmind/lecture]
---
# Lectures 75–76 — integration and differentiation of power series, Taylor series, integrals depending on a parameter

[[en/lectures-2025-26/lecture-73-74|← Lectures 73–74]] · [[en/lectures-2025-26/index|Lecture index]] · [[en/lectures-2025-26/lecture-77-78|Lectures 77–78 →]] · [[en/term-index|Terms & theorems]] · [[ru/lectures-2025-26/lecture-75-76|Русский]] · [[es/lectures-2025-26/lecture-75-76|Español]]

> [!info] Source and numbering
> These notes were copied from a handwritten notebook (pages p050–p057; the raw page text is in [`ocr/raw/`](https://github.com/NikiHunter/matan/blob/main/ocr/raw/p050.md)). Page p050 begins with an example to the [[en/11-power-series#11.1 Radius of convergence|Cauchy–Hadamard formula]] that completes the previous class; next to it in the margin, in red, are the heading “Lectures 75–76” and the plan of the class, read only partially (integration of power series; radii, power series and the Taylor series, analytic functions; the third item is illegible), and in a frame the mark “80 (15 Oct)” (apparently a page number and the date of the class). The coefficients of power series, denoted $C_k$ in the notebook, are denoted $c_k$ here, as on the lecturer's slides. The numbering of definitions and theorems is the lecturer's. Slips in the notes are corrected and marked with “Source correction” blocks; lost passages are restored and marked with “Restored” blocks; the tags match [`ocr/RESOLVED.md`](https://github.com/NikiHunter/matan/blob/main/ocr/RESOLVED.md). Places that still have to be checked against the notebook are listed in [`ocr/ISSUES.md`](https://github.com/NikiHunter/matan/blob/main/ocr/ISSUES.md).

## §8.4. Power series (conclusion)


**Example (to the Cauchy–Hadamard formula).** Consider the series $\sum_{n=0}^{\infty}c_nx^n$, where $c_{2n+1}=0$, $c_{2n}=1$, i.e.
$$
\sum_{n=0}^{\infty}c_nx^n=1+x^2+x^4+x^6+\dots
$$
The sequence $\sqrt[n]{|c_n|}$ ($n\ge1$) equals $0$ for odd $n$ and $1$ for even $n$:
$$
\lim_{n\to\infty}\sqrt[2n+1]{|c_{2n+1}|}=0,\qquad \lim_{n\to\infty}\sqrt[2n]{|c_{2n}|}=1 .
$$
Its [[en/lectures-2025-26/lecture-11-12#^def-2-3-8|partial limits]] are $0$ and $1$; the limit $\lim\sqrt[n]{|c_n|}$ does not exist, and $\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}=1$. By the Cauchy–Hadamard formula ([[en/lectures-2025-26/lecture-73-74#^thm-8-4-1|Theorem 8.4.1]]) $R=1$. This agrees with a direct computation: for $|x|<1$ the series is a geometric progression with ratio $x^2$, and $1+x^2+x^4+\dots=\frac1{1-x^2}$, while for $|x|\ge1$ the general term $x^{2n}$ does not tend to zero, and the series diverges. ^p050

> [!info] Source correction
> (M202, U203). The notes say “$\lim_{n\to\infty}S_n=\lim_{n\to\infty}S_{n+1}=0\Rightarrow R=\infty$”, then “$\lim_{n\to\infty}S_n=\lim_{n\to\infty}S_{2n}=\ldots$” (here $S_n$ denotes $\sqrt[n]{|c_n|}$). The [[en/lectures-2025-26/lecture-11-12#^def-2-3-7|subsequence]] with odd indices does tend to $0$, but the Cauchy–Hadamard formula contains the [[en/lectures-2025-26/lecture-13#Definition 2.3.9 (upper and lower limits)|upper limit]], i.e. the largest partial limit; it equals $1$ (over even indices). Therefore $\varlimsup\sqrt[n]{|c_n|}=1$ and $R=1$, not $\infty$: for example, for $x=1$ the series $1+1+1+\dots$ diverges.

### Integration of power series

> [!theorem] Theorem 8.4.4 (integration of power series)
> Let a power series $\sum_{k=0}^{\infty}c_k(x-a)^k$ be given, and let $R\in(0,+\infty]$ be its radius of convergence. Then the power series can be integrated termwise over any segment lying in the interval of convergence: if $[A,B]\subset(a-R,a+R)$, then
> $$
> \int_A^B\sum_{k=0}^{\infty}c_k(x-a)^k\,dx=\sum_{k=0}^{\infty}c_k\,\frac{(B-a)^{k+1}-(A-a)^{k+1}}{k+1}.\qquad\qquad(8.4.2)
> $$
> If, moreover, $R<+\infty$ and the power series converges for $x=a+R$ (respectively for $x=a-R$), then equality (8.4.2) also holds for $B=a+R$ (respectively for $A=a-R$); if the series converges at both endpoints, then (8.4.2) also holds for the segment $[a-R,a+R]$.

^thm-8-4-4

**Proof.** Without loss of generality $a=0$ ([[en/lectures-2025-26/lecture-73-74#^rem-8-4-2|Remark 8.4.2]]). Write $r=\max\{|A|,|B|\}$. Then $r<R$ and
$$
[A,B]\subset[-r,r]\subset(-R,R).
$$
By [[en/lectures-2025-26/lecture-73-74#^thm-8-4-2|Theorem 8.4.2]] the series $\sum c_kx^k$ [[en/10-function-sequences-series#10.1 Two modes of convergence|converges uniformly]] on $[-r,r]$, hence on $[A,B]$ too. Its terms $c_kx^k$ are continuous, so by [[en/lectures-2025-26/lecture-73-74#^thm-8-3-2|Theorem 8.3.2]] (termwise integration) the series can be integrated termwise over $[A,B]$:
$$
\int_A^B\sum_{k=0}^{\infty}c_kx^k\,dx=\sum_{k=0}^{\infty}c_k\int_A^Bx^k\,dx=\sum_{k=0}^{\infty}c_k\,\frac{B^{k+1}-A^{k+1}}{k+1}.
$$


Now let $R<+\infty$, let the series converge for $x=R$, $B=R$ and $A\in(-R,R)$. By [[en/11-power-series#^abel-theorem|Abel's theorem]] ([[en/lectures-2025-26/lecture-73-74#^thm-8-4-3|Theorem 8.4.3]]) the series $\sum c_kx^k$ converges uniformly on $[0,R]$. If $A<0$, then, in addition, by [[en/lectures-2025-26/lecture-73-74#^thm-8-4-2|Theorem 8.4.2]] (with $r=|A|<R$) the series converges uniformly on $[A,0]$. A series that converges uniformly on each of two segments converges uniformly on their union (it suffices to take the larger of the two indices $N$ in the definition of uniform convergence); hence the series converges uniformly on $[A,R]$, and by [[en/lectures-2025-26/lecture-73-74#^thm-8-3-2|Theorem 8.3.2]] it can be integrated termwise over $[A,R]$, which gives (8.4.2) for $B=R$. The case $A=-R$ is treated similarly (with uniform convergence on $[-R,0]$ by Abel's theorem), and if the series converges at both endpoints, it converges uniformly on $[-R,0]$ and on $[0,R]$, i.e. on $[-R,R]$. $\square$ ^p051

> [!info] Source correction
> (S209, S210). In the notes, after “$\sum C_kx^k$ conv. unif. on $[-r,r]$ (by Th. 8.4.2)”, the termwise integration is also justified by the reference “(by Th. 8.4.2)”; it follows from [[en/lectures-2025-26/lecture-73-74#^thm-8-3-2|Theorem 8.3.2]] on termwise integration. In the case $B=R$ the notes say “by Th. (8.4.2) the series … conv. unif. on $[A,B]=[-r,r]$”, but [[en/lectures-2025-26/lecture-73-74#^thm-8-4-2|Theorem 8.4.2]] gives uniform convergence only on a segment $[A,0]$ lying inside the interval of convergence; on $[0,R]$ it follows from Abel's theorem (as in the lecturer's note, FS p77).

### Radii of convergence of the differentiated and integrated series

> [!theorem] Theorem 8.4.5 (radii of power series)
> The radii of convergence of the power series
> $$
> \sum_{k=0}^{\infty}c_k(x-a)^k,\qquad \sum_{k=1}^{\infty}kc_k(x-a)^{k-1},\qquad \sum_{k=0}^{\infty}\frac{c_k}{k+1}(x-a)^{k+1}
> $$
> are equal. (The second series is obtained from the first by termwise differentiation, the third by termwise integration from $a$ to $x$.)

^thm-8-4-5

**Proof.** We prove that the radii of convergence of the first two series coincide. For $x\ne a$ the series $\sum_{k=1}^{\infty}kc_k(x-a)^{k-1}$ converges if and only if the series $\sum_{k=1}^{\infty}kc_k(x-a)^k$ converges (their terms differ by the constant factor $x-a\ne0$), so the radii of convergence of these two series coincide; the coefficient of the second of them at $(x-a)^n$ equals $nc_n$. By the Cauchy–Hadamard formula it suffices to check the equality
$$
\varlimsup_{n\to\infty}\sqrt[n]{n|c_n|}=\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}.
$$
Fix an arbitrary $\varepsilon>0$. Since $\sqrt[n]n\to1$, there is $N$ such that $\sqrt[n]n\le1+\varepsilon$ for all $n>N$, i.e. $n\le(1+\varepsilon)^n$, and then
$$
\sqrt[n]{|c_n|}\le\sqrt[n]{n|c_n|}\le\sqrt[n]{(1+\varepsilon)^n|c_n|}=(1+\varepsilon)\sqrt[n]{|c_n|}\qquad(n>N).
$$
Passing to upper limits (an inequality between the terms of sequences for $n>N$ is preserved for the upper limits, and the positive factor $1+\varepsilon$ can be taken outside the upper limit), we get
$$
\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}\le\varlimsup_{n\to\infty}\sqrt[n]{n|c_n|}\le(1+\varepsilon)\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}.
$$
Since $\varepsilon>0$ is arbitrary, the upper limits are equal (including the case when they equal $0$ or $+\infty$), and the radii of convergence of the first two series coincide.

That the radii of convergence of the first and third series coincide is checked similarly: for $x\ne a$ the third series converges together with the series $\sum_{k=0}^{\infty}\frac{c_k}{k+1}(x-a)^k$, and since $\sqrt[n]{n+1}\to1$, for all sufficiently large $n$
$$
\frac1{1+\varepsilon}\sqrt[n]{|c_n|}\le\sqrt[n]{\frac{|c_n|}{n+1}}\le\sqrt[n]{|c_n|}.
$$
$\square$

> [!info] Source correction
> (T212, U213, M214). In the notes, as in the Cauchy–Hadamard formula (lectures 73–74), ordinary limits stand instead of upper ones, and the final chain is written as “$\lim\sqrt[n]{|nC_n|}\le\lim\sqrt[n]{|C_n|}\le(1+\varepsilon)\lim\sqrt[n]{|C_n|}$” — the first two members are swapped. Correctly: $\varlimsup\sqrt[n]{|c_n|}\le\varlimsup\sqrt[n]{n|c_n|}\le(1+\varepsilon)\varlimsup\sqrt[n]{|c_n|}$ (FS p78). The line “$\forall\varepsilon>0$, $\exists k\in\mathbb N$: $k>1$, by $\exists N:\forall n>N$” is read as “fix $\varepsilon>0$; since $\sqrt[n]n\to1$, there is $N$ such that for all $n>N$…”.

> [!note] Restored
> (an explanation of the statement, according to the standard exposition). [[#^thm-8-4-5|Theorem 8.4.5]] asserts only the equality of the radii; the behaviour of the three series at the endpoints of the interval of convergence can differ. For example, the series $\sum_{k=1}^{\infty}\frac{x^k}{k^2}$ ($R=1$) converges for $x=1$, while the differentiated series $\sum_{k=1}^{\infty}\frac{x^{k-1}}{k}$ turns into the harmonic series for $x=1$ and diverges.

### Differentiation of power series

> [!theorem] Theorem 8.4.6 (differentiation of power series)
> Let $R\in(0,+\infty]$ be the radius of convergence of the series
> $$
> f(x)=\sum_{k=0}^{\infty}c_k(x-a)^k .
> $$
> Then the function $f$ is infinitely [[en/lectures-2025-26/lecture-22-23#^def-3-2-1|differentiable]] on the set $|x-a|<R$, and the series can be differentiated termwise any number of times:
> $$
> f^{(m)}(x)=\sum_{k=m}^{\infty}k(k-1)\dots(k-m+1)\,c_k(x-a)^{k-m},\qquad |x-a|<R,\quad m\in\mathbb N .
> $$

^thm-8-4-6

**Proof.** Without loss of generality $a=0$. By [[#^thm-8-4-5|Theorem 8.4.5]] termwise differentiation does not change the radius of convergence: the series $\sum_{k=1}^{\infty}kc_kx^{k-1}$ again has radius of convergence $R$. Therefore it suffices to prove the statement for $m=1$: the general case is obtained by applying the case $m=1$ successively to the series for $f',f'',\dots$ ([[en/01-logic-sets-functions#^example-induction|induction]] on $m$).


So $f(x)=\sum_{k=0}^{\infty}c_kx^k$, $|x|<R$. Consider a point $x_1\in(-R,R)$ and prove that $f$ is differentiable at $x_1$ and $f'(x_1)=\sum_{k=1}^{\infty}kc_kx_1^{k-1}$. Fix a number $\rho$ such that $|x_1|<\rho<R$, and let $|x|\le\rho$, $x\ne x_1$. Then
$$
\frac{f(x)-f(x_1)}{x-x_1}=\sum_{k=1}^{\infty}c_k\,\frac{x^k-x_1^k}{x-x_1}=\sum_{k=1}^{\infty}c_k\bigl(x^{k-1}+x^{k-2}x_1+\dots+xx_1^{k-2}+x_1^{k-1}\bigr).
$$
Write $\psi_k(x):=c_k\bigl(x^{k-1}+x^{k-2}x_1+\dots+x_1^{k-1}\bigr)$ — these are polynomials, i.e. continuous functions. For $|x|\le\rho$ each of the $k$ terms in the bracket has absolute value at most $\rho^{k-1}$, hence
$$
|\psi_k(x)|=\bigl|c_k\bigl(x^{k-1}+x^{k-2}x_1+\dots+x_1^{k-1}\bigr)\bigr|\le k|c_k|\rho^{k-1}\qquad(|x|\le\rho).
$$
Since $\rho<R$, and the series $\sum kc_kx^{k-1}$ has radius of convergence $R$ by [[#^thm-8-4-5|Theorem 8.4.5]], it converges absolutely at the point $x=\rho$ (a power series converges absolutely in its interval of convergence, [[en/lectures-2025-26/lecture-73-74#^rem-8-4-1|Remark 8.4.1]]), i.e. the series $\sum_{k=1}^{\infty}k|c_k|\rho^{k-1}$ converges. By the [[en/10-function-sequences-series#^weierstrass-m-test|Weierstrass test]] the series $\sum_{k=1}^{\infty}\psi_k(x)$ converges uniformly on $[-\rho,\rho]$ (all the more on $[-\rho,\rho]\setminus\{x_1\}$), and by [[en/lectures-2025-26/lecture-71-72#^thm-8-3-1|Theorem 8.3.1]] its sum $\Psi(x)$ is continuous on $[-\rho,\rho]$. For $x\ne x_1$ we have $\Psi(x)=\frac{f(x)-f(x_1)}{x-x_1}$, and $\psi_k(x_1)=kc_kx_1^{k-1}$. Hence (termwise passage to the limit)
$$
\lim_{x\to x_1}\frac{f(x)-f(x_1)}{x-x_1}=\lim_{x\to x_1}\Psi(x)=\Psi(x_1)=\sum_{k=1}^{\infty}\lim_{x\to x_1}c_k\bigl(x^{k-1}+x^{k-2}x_1+\dots+x_1^{k-1}\bigr)=\sum_{k=1}^{\infty}kc_kx_1^{k-1}.
$$
Since $x_1$ is any point of the interval $(-R,R)$, the function $f$ is differentiable on $(-R,R)$, and the series can be differentiated termwise. $\square$ ^p052

> [!info] Source correction
> (M218, S220). In the notes the estimate of a term of the series is written as a continuation of the equality (“$=\left|C_k\left(x^{k-1}+x^{k-2}x_1+\ldots+x_1^{k-1}\right)\right|\le k|C_k|\rho^{k-1}$”), whereas it is a separate estimate of each term. Uniform convergence is written “for $(-\rho,\rho)$, all the more $\forall(-S,S)\times(x_1)$”, i.e. on $(-\rho,\rho)$ and all the more on $(-\rho,\rho)\setminus\{x_1\}$; here it is obtained on the segment $[-\rho,\rho]$, which allows one to refer to [[en/lectures-2025-26/lecture-71-72#^thm-8-3-1|Theorem 8.3.1]].

### Uniqueness of the expansion of a function in a power series

> [!theorem] Theorem 8.4.7 (uniqueness of the expansion of a function in a power series)
> Let $a\in\mathbb R$, and let $R\in(0,+\infty]$ be the radius of convergence of the series
> $$
> f(x)=\sum_{k=0}^{\infty}c_k(x-a)^k .
> $$
> Then $f\in C^\infty(a-R,a+R)$, and the coefficients $c_k$ are uniquely determined by the formula
> $$
> c_k=\frac{f^{(k)}(a)}{k!} .
> $$

^thm-8-4-7

**Proof.** By [[#^thm-8-4-6|Theorem 8.4.6]] the function $f$ is infinitely differentiable on $(a-R,a+R)$ (each of its [[en/lectures-2025-26/lecture-22-23#^def-3-1-1|derivatives]] is differentiable and hence continuous, i.e. $f\in C^\infty(a-R,a+R)$) and
$$
f^{(m)}(x)=\sum_{k=m}^{\infty}k(k-1)\dots(k-m+1)\,c_k(x-a)^{k-m}\qquad\forall m\in\mathbb N,\ |x-a|<R .
$$
Substitute $x=a$:
$$
f^{(m)}(a)=m(m-1)\dots(m-m+1)\,c_m+\sum_{k=m+1}^{\infty}k(k-1)\dots(k-m+1)\,c_k(a-a)^{k-m}=m!\,c_m ,
$$
since all terms of the sum with $k\ge m+1$ vanish. Hence $f^{(m)}(a)=m!\,c_m$, i.e. $c_m=\frac{f^{(m)}(a)}{m!}$; for $m=0$ the substitution $x=a$ into the series itself gives $c_0=f(a)$. The coefficients are expressed through the function $f$ itself, so two power series with centre $a$ whose sums coincide in some neighbourhood of the point $a$ have the same coefficients. $\square$

> [!info] Source correction
> (T222, M223). In the notes the factor $c_k$ is missing in the sum after the substitution, and the conclusion is written as “$\Rightarrow f^{(m)}(a)+m!C_m\Rightarrow C_m=\frac{f^{(m)}(a)}{m!}$”; it should be $f^{(m)}(a)=m!\,c_m$ (FS p80).


### The Taylor series

> [!definition] Definition 8.4.3
> Let $f$ have derivatives of all orders at the point $a$. The numbers $c_k=\frac{f^{(k)}(a)}{k!}$ are called the Taylor coefficients, and the series
> $$
> \sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k
> $$
> is called the Taylor series of the function $f$ centred at the point $a$. A Taylor series centred at zero is called a [[en/07-taylor-convexity#7.3 Taylor's formula|Maclaurin series]].

^def-8-4-3

### Representation of functions by real power series

[[#^thm-8-4-6|Theorems 8.4.6]] and [[#^thm-8-4-7|8.4.7]] imply that if a function expands in a power series in a neighbourhood of the point $a$, then it is infinitely differentiable in this neighbourhood, and the series is its Taylor series.

Let $a\in\mathbb R$, $R\in(0,+\infty]$, $f\in C^\infty(a-R,a+R)$. Then one can form the Taylor series of the function $f$
$$
\sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k
$$
and ask about its behaviour. For $x=a$ the series converges to $f(a)$. For $x\ne a$ three cases are possible:

1. the series converges to $f(x)$;
2. the series diverges;
3. the series converges, but not to $f(x)$.

### The Taylor polynomial

The [[en/04-numeric-series#4.1 Convergence through partial sums|partial sum]] of the Taylor series
$$
T_{n,f}(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k
$$
is the [[en/lectures-2025-26/lecture-27-28#^thm-3-6-3|Taylor polynomial]]. By the definition of the sum of a series, convergence of the Taylor series to $f(x)$ means that $T_{n,f}(x)\to f(x)$ as $n\to\infty$, i.e. that the remainder $R_{n,f}(x):=f(x)-T_{n,f}(x)$ tends to zero.

> [!theorem] Theorem 8.4.8 (a test for the expandability of a function in a Taylor series)
> Let
>
> 1. $f\in C^\infty(A,B)$;
> 2. $a,x\in(A,B)$, $a\ne x$;
> 3. there exist $M\in(0,\infty)$ such that $|f^{(n)}(t)|\le M$ for all $n\in\mathbb N$ and all $t$ lying between $a$ and $x$.

^thm-8-4-8


Then
$$
\sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k=f(x).
$$

^p054

> [!info] Source correction
> (A227). In the notes (and on the slide FS p81) condition 3 is written for “$\forall t\in(x-a,x+a)$”. This interval is not related to the segment between $a$ and $x$ (for $a=0$ it is even empty). The proof uses the estimate of the remainder of Taylor's formula, in which the derivative is taken at points between $a$ and $x$, so the condition is needed precisely for such $t$ (it holds, for example, if $|f^{(n)}(t)|\le M$ for all $n$ and all $t\in(A,B)$).

**Proof.** By the lemma on the estimate of the remainder in Taylor's formula proved (much) earlier ([[en/lectures-2025-26/lecture-29-30#^lem-3-6-2|Lemma 3.6.2]], lectures 29–30) we have
$$
|f(x)-T_{n,f}(x)|=|R_{n,f}(x)|\le\frac{M|x-a|^{n+1}}{(n+1)!},
$$
which gives the required convergence: $\frac{q^{n+1}}{(n+1)!}\to0$ as $n\to\infty$ for every $q\ge0$ (here $q=|x-a|$), since the series $\sum_{n}\frac{q^n}{n!}$ converges by the [[en/04-numeric-series#4.2 Nonnegative terms|d'Alembert test]] ($\frac{q^{n+1}/(n+1)!}{q^n/n!}=\frac{q}{n+1}\to0$), and its general term tends to zero. $\square$

### An example of a function whose Taylor series diverges at all points except the centre

**Example.** Let ($a=0$)
$$
f(x)=\sum_{n=0}^{\infty}e^{-\sqrt{2^n}}\cos(2^nx),\qquad x\in\mathbb R .
$$
Form the Taylor series of this function at the point $x=0$. Its constant term is $f(0)=\sum_{n=0}^{\infty}e^{-\sqrt{2^n}}$. The Taylor coefficients $c_n$ grow so fast that the Taylor series diverges for all $x\ne0$.

> [!note] Restored
> (by the standard proof; in the notes the estimate of the coefficients is only sketched: “$C_n$ — … $n!$”).
>
> *The function $f$ is infinitely differentiable.* The derivative of order $k$ of the term $e^{-\sqrt{2^n}}\cos(2^nx)$ equals $e^{-\sqrt{2^n}}2^{nk}\cos\left(2^nx+\frac{k\pi}{2}\right)$ and has absolute value at most $e^{-\sqrt{2^n}}2^{nk}$. Put $t_n=\sqrt{2^n}=2^{n/2}$; then $e^{-\sqrt{2^n}}2^{nk}=t_n^{2k}e^{-t_n}$. Since $t^{2k+2}e^{-t}\to0$ as $t\to+\infty$, there is a constant $A_k$ such that $t_n^{2k}e^{-t_n}\le A_kt_n^{-2}=A_k2^{-n}$, and the series $\sum_ne^{-\sqrt{2^n}}2^{nk}$ converges for each $k$. By the Weierstrass test all the series of derivatives converge uniformly on $\mathbb R$, and by [[en/lectures-2025-26/lecture-73-74#^thm-8-3-3|Theorem 8.3.3]] (applied successively on any segment) $f\in C^\infty(\mathbb R)$, the derivatives being computed termwise.
>
> *The Taylor coefficients.* At the point $0$ all derivatives of odd order vanish, and
> $$
> f^{(2k)}(0)=(-1)^k\sum_{n=0}^{\infty}e^{-\sqrt{2^n}}\,2^{2nk},\qquad c_{2k}=\frac{f^{(2k)}(0)}{(2k)!}.
> $$
> All the terms of the sum are positive, so for every $n$ we have $|c_{2k}|\ge\frac{t_n^{4k}e^{-t_n}}{(2k)!}$. The numbers $t_n=2^{n/2}$ form a geometric progression with ratio $\sqrt2<2$, so for each $k\in\mathbb N$ there is $n$ with $k\le t_n\le2k$. For such $n$, taking into account $(2k)!\le(2k)^{2k}$, we get
> $$
> |c_{2k}|\ge\frac{k^{4k}e^{-2k}}{(2k)^{2k}}=\left(\frac{k}{2e}\right)^{2k},
> $$
> i.e. $\sqrt[2k]{|c_{2k}|}\ge\frac{k}{2e}\to+\infty$ as $k\to\infty$. Consequently $\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}=+\infty$, and by the Cauchy–Hadamard formula the radius of convergence of the Taylor series is $0$: the series converges only for $x=0$ (where its sum equals $f(0)$).

### Analytic functions

> [!definition] Definition 8.4.4
> Let $-\infty\le A<B\le+\infty$, $f:(A,B)\to\mathbb R$, $a\in(A,B)$. The function $f$ is called analytic at the point $a$ if it expands in a power series in some neighbourhood of the point $a$, i.e. there exist numbers $r>0$ and $c_k\in\mathbb R$ such that
> $$
> f(x)=\sum_{k=0}^{\infty}c_k(x-a)^k,\qquad x\in(a-r,a+r).
> $$
> The function $f:(A,B)\to\mathbb R$ is called analytic on the interval $(A,B)$ if it is analytic at every point $(A,B)$.

^def-8-4-4

> [!info] Source correction
> (A233). The notes say: “expands in a power series $f(x)=\sum C_k(x-a)^k$, $x\in(a-r,a+r)$” — without saying that $r>0$ and the coefficients $c_k$ exist (the [[en/01-logic-sets-functions#1.1 Propositions and quantifiers|quantifiers]] are restored according to the slide FS p82); moreover, the notes have $-\infty<A<B<+\infty$, while the slide also allows infinite endpoints of the interval.

By [[#^thm-8-4-6|Theorems 8.4.6]] and [[#^thm-8-4-7|8.4.7]] a function analytic at the point $a$ is infinitely differentiable in a neighbourhood of $a$, and its power series is its Taylor series.

## §9.1. Proper integrals depending on a parameter


Chapter 9 “[[#^def-9-1-1|Integrals depending on a parameter]]” begins. First an example showing what questions arise when working with such integrals. ^p055

**Example.** Consider
$$
I(y)=\int_0^{+\infty}e^{-xy}\,\frac{\sin x}{x}\,dx,\qquad x\in(0,+\infty),\quad y\in[0,+\infty).
$$
We want to compute $I'(y)$, and then the integral itself. For now we do not deal with justification (uniform convergence) and formally differentiate with respect to $y$ under the integral sign (step ❶):
$$
I'(y)=\int_0^{+\infty}\frac{\partial}{\partial y}\Bigl(e^{-xy}\,\frac{\sin x}{x}\Bigr)dx=-\int_0^{+\infty}e^{-xy}\sin x\,dx .
$$
A note in red in the margin: “❶ The passage has to be justified separately!! — will be done later”.

> [!info] Source correction
> (T236). In the notes the first integral has $dy$ instead of $dx$: the integration is with respect to $x$, and the differentiation with respect to the parameter $y$.

Step ❷: for $y>0$ we compute the integral $J(y):=\int_0^{+\infty}e^{-xy}\sin x\,dx$ by integrating by parts twice (the boundary terms at infinity vanish, since $e^{-xy}\to0$ as $x\to+\infty$):
$$
\begin{aligned}
-J(y)=\int_0^{+\infty}e^{-xy}\,d\cos x&=e^{-xy}\cos x\Big|_0^{+\infty}-\int_0^{+\infty}\cos x\,de^{-xy}=-1+y\int_0^{+\infty}e^{-xy}\cos x\,dx\\
&=-1+y\Bigl(e^{-xy}\sin x\Big|_0^{+\infty}-\int_0^{+\infty}\sin x\,de^{-xy}\Bigr)=-1+y^2\int_0^{+\infty}e^{-xy}\sin x\,dx=-1+y^2J(y).
\end{aligned}
$$

> [!info] Source correction
> (T520). In the notes the first [[en/lectures-2025-26/lecture-37-38#^thm-4-1-4|integration by parts]] is written as “$e^{-xy}\cos x\big|_0^{+\infty}+\int_0^{+\infty}\cos x\,de^{-xy}=-1+\dots$”: there must be a minus sign before the integral. The final expression $-1+y\int_0^{+\infty}e^{-xy}\cos x\,dx$ in the notes is correct.

So $I'(y)=-J(y)=-1+y^2J(y)$, whence $J(y)(1+y^2)=1$,
$$
J(y)=\frac{1}{1+y^2},\qquad I'(y)=-\frac{1}{1+y^2}\qquad(y>0).
$$
Thus we have computed $I'(y)$. Hence
$$
I(y)=-\int\frac{dy}{1+y^2}=-\operatorname{arctg}y+C .
$$
Let us find the constant $C$. As $y\to+\infty$ (again formally passing to the limit under the integral sign)
$$
I(y)=\int_0^{+\infty}e^{-xy}\,\frac{\sin x}{x}\,dx\xrightarrow[y\to+\infty]{}\int_0^{+\infty}0\,dx=0 ,
$$
so $-\operatorname{arctg}y+C\to-\frac\pi2+C=0$, i.e. $C=\frac\pi2$ and
$$
I(y)=\frac\pi2-\operatorname{arctg}y .
$$
In particular,
$$
I(0)=\int_0^{+\infty}\frac{\sin x}{x}\,dx=\frac\pi2-\operatorname{arctg}0=\frac\pi2 .
$$
A note in red at the bottom of the page: “❶ The above has to be justified”.

> [!info] Source correction
> (T239, T521). In the notes the [[en/lectures-2025-26/lecture-36#^def-4-1-1|antiderivative]] is written as “$I'(y)=-\int\frac{dy}{1+y^2}=-\operatorname{arctg}y+C$” — on the left there should be $I(y)$. The line “$\Rightarrow I(y)=-\int_0^{+\infty}e^{-xy}\frac{\sin x}{x}dx+\int_0^{+\infty}0\,dx=0$” is garbled; in meaning it is the passage to the limit as $y\to+\infty$: $I(y)\to\int_0^{+\infty}0\,dx=0$.

> [!note] Restored
> (by standard estimates; in the notes these steps are marked as requiring justification). The limit as $y\to+\infty$ is justified at once: since $\left|\frac{\sin x}{x}\right|\le1$, for $y>0$ we have $|I(y)|\le\int_0^{+\infty}e^{-xy}\,dx=\frac1y\to0$. The other passages — differentiation under the sign of an [[en/lectures-2025-26/lecture-47-48#^def-4-5-2|improper integral]] (step ❶) and the equality $I(0)=\lim_{y\to0+}I(y)$, which is needed because the formula for $I'(y)$ was derived only for $y>0$ (for $y=0$ the integral $J(0)=\int_0^{+\infty}\sin x\,dx$ diverges) — require [[en/lectures-2025-26/lecture-77-78#^def-9-2-1|uniform convergence of an improper integral]] with respect to a parameter and will be justified later (§9.2).


> [!definition] Definition 9.1.1
> An integral depending on a parameter is a function of the form
> $$
> I(y)=\int_{E_y}f(x,y)\,dx ,
> $$
> where $y$ plays the role of a parameter ranging over the set $Y$.

^def-9-1-1

**Remark.** If for each $y\in Y$ the integral $\int_{E_y}f(x,y)\,dx$ is proper, then the function $I(y)$ is a proper integral depending on a parameter.

> [!info] Source correction
> (T242). In the notes (and on the slide FS p83) the integral in the remark is written as “$\int f(x,y)\,dy$”; the integration is with respect to $x$, so $dx$. The abbreviation “abs.” before “proper” is read as “is”.

### Continuity of an integral with respect to a parameter

For now we assume that the set $E_y$ does not depend on $y$.

> [!info] Source correction
> (T522). The heading of this item in the notes is “Differentiation of the integral with respect to the parameter $y$”, but it proves continuity ([[#^thm-9-1-1|Theorem 9.1.1]]); the next item is devoted to differentiation. The heading is corrected according to the slide FS p83 (“On the continuity of an integral with respect to a parameter”).

> [!theorem] Theorem 9.1.1
> Let $P=\{(x,y)\in\mathbb R^2:\ a\le x\le b,\ c\le y\le d\}$ and $f=f(x,y)\in C(P)$. Then the function $I(y)=\int_a^bf(x,y)\,dx$ is continuous at every point $y\in[c,d]$, i.e. $I\in C([c,d])$.

^thm-9-1-1

> [!info] Source correction
> (T244). In the notes the conclusion of the theorem reads: “the function $I(y)=\int_a^bf(x,y)\,dx$ is integrable $\forall y\in[c,d]$”. The theorem asserts (and proves) the continuity of $I$ on $[c,d]$ (as on the slide FS p83); the integrability of $I$ in $[c,d]$ is a separate statement that follows from continuity.

*Figure in the margin (page p056): the rectangle $P$ in the plane of the variables $(x,y)$, with the points $a$, $b$, $c$, $d$ marked on the axes.*

**Proof.** Take any point $y_0\in[c,d]$. By the definition of continuity we must prove that $I(y_0)=\lim_{y\to y_0}I(y)$, i.e. that
$$
I(y_0)=\int_a^bf(x,y_0)\,dx=\lim_{y\to y_0}\int_a^bf(x,y)\,dx=\lim_{y\to y_0}I(y)
$$
(the limits are taken over $y\in[c,d]$).

The function $f$ is continuous on $P$ by hypothesis, and the rectangle $P$ is a [[en/lectures-2025-26/lecture-57-58#^def-5-3-7|compact set]]; by Cantor's theorem $f$ is [[en/lectures-2025-26/lecture-17-18#^def-2-5-7|uniformly continuous]] on $P$: for every $\varepsilon>0$ there is $\delta>0$ such that $|f(x',y')-f(x'',y'')|<\varepsilon$ for any points $(x',y'),(x'',y'')\in P$ whose distance is less than $\delta$. In particular, if $y\in[c,d]$ and $|y-y_0|<\delta$, then
$$
|f(x,y)-f(x,y_0)|<\varepsilon\qquad\forall x\in[a,b],
$$
i.e. the functions $\varphi_y(x):=f(x,y)$ converge to $\varphi_{y_0}(x)=f(x,y_0)$ uniformly on $[a,b]$ as $y\to y_0$: $\varphi_y\rightrightarrows\varphi_{y_0}$. For each $y\in[c,d]$ the function $\varphi_y$ is continuous in $x$ on $[a,b]$, hence integrable on $[a,b]$. Therefore the theorem on passage to the limit under the integral sign applies ([[en/lectures-2025-26/lecture-71-72#^thm-8-2-2|Theorem 8.2.2]]; its proof carries over verbatim to a continuous parameter $y\to y_0$): as $|y-y_0|<\delta$
$$
|I(y)-I(y_0)|\le\int_a^b|f(x,y)-f(x,y_0)|\,dx\le\varepsilon(b-a),
$$
i.e. $I(y)\to I(y_0)$ as $y\to y_0$. Since the point $y_0\in[c,d]$ is arbitrary, $I\in C([c,d])$. $\square$

> [!info] Source correction
> (M245). In the notes the last link of the chain is written as “$\lim\int_a^bf(x,y)\,dx-\lim I(y)$”; it should be the equality $\lim_{y\to y_0}\int_a^bf(x,y)\,dx=\lim_{y\to y_0}I(y)$ (FS p83).


### Differentiation of an integral with respect to a parameter

> [!theorem] Theorem 9.1.2
> Let $P=\{(x,y)\in\mathbb R^2:\ a\le x\le b,\ c\le y\le d\}$, $f=f(x,y)\in C(P)$ and $\frac{\partial f}{\partial y}\in C(P)$. Then the function $I(y)=\int_a^bf(x,y)\,dx$ belongs to $C^1([c,d])$ and
> $$
> I'(y)=\int_a^b\frac{\partial f}{\partial y}(x,y)\,dx .
> $$
> On the lecturer's slide this formula is called Leibniz's formula (rule); a note in red in the margin of the notes refers to [[en/lectures-2025-26/lecture-71-72#^thm-8-2-3|Theorem 8.2.3]] (differentiation of the limit function).

^thm-9-1-2

**Proof.** Take $y_0\in[c,d]$ and $h\ne0$ such that $y_0+h\in[c,d]$ (at the endpoints of the segment the derivative is one-sided). Then
$$
\frac{I(y_0+h)-I(y_0)}{h}=\frac1h\int_a^b\bigl(f(x,y_0+h)-f(x,y_0)\bigr)\,dx .
$$
For each $x\in[a,b]$ the function $t\mapsto f(x,t)$ is differentiable on $[c,d]$, and by [[en/lectures-2025-26/lecture-24-25-26#^thm-3-4-3|Lagrange's theorem]]
$$
\frac{f(x,y_0+h)-f(x,y_0)}{h}=\frac{\partial f}{\partial y}(x,y_0+\theta h),\qquad 0<\theta<1
$$
(the number $\theta$ depends on $x$ and $h$). Therefore
$$
\begin{aligned}
\left|\frac{I(y_0+h)-I(y_0)}{h}-\int_a^b\frac{\partial f}{\partial y}(x,y_0)\,dx\right|
&=\left|\int_a^b\left[\frac{f(x,y_0+h)-f(x,y_0)}{h}-\frac{\partial f}{\partial y}(x,y_0)\right]dx\right|\\
&\le(b-a)\sup_{x\in[a,b],\ 0<\theta<1}\left|\frac{\partial f}{\partial y}(x,y_0+\theta h)-\frac{\partial f}{\partial y}(x,y_0)\right|=:\varphi(y_0,h).
\end{aligned}
$$
By hypothesis $\frac{\partial f}{\partial y}\in C(P)$, and $P$ is compact, so $\frac{\partial f}{\partial y}$ is uniformly continuous on $P$, and $\frac{\partial f}{\partial y}(x,y)\rightrightarrows\frac{\partial f}{\partial y}(x,y_0)$ on $[a,b]$ as $y\to y_0$: for every $\varepsilon>0$ there is $\delta>0$ such that $\left|\frac{\partial f}{\partial y}(x,y)-\frac{\partial f}{\partial y}(x,y_0)\right|<\varepsilon$ for all $x\in[a,b]$ if $|y-y_0|<\delta$. Since $|\theta h|<|h|$, for $|h|<\delta$ we get $\varphi(y_0,h)\le\varepsilon(b-a)$. Hence $\varphi(y_0,h)\to0$ as $h\to0$, i.e.
$$
I'(y_0)=\int_a^b\frac{\partial f}{\partial y}(x,y_0)\,dx .
$$
$\square$

> [!info] Source correction
> (M251, T253). In the notes the estimate is written as “$\le\int_a^b\sup\left|\frac{\partial f}{\partial y}(x,y_0+h)-\frac{\partial f}{\partial y}(x,y_0)\right|dx$”; by Lagrange's theorem (a note in the margin) the derivative is taken at an intermediate point $y_0+\theta h$, $0<\theta<1$, so the [[en/lectures-2025-26/lecture-11-12#^def-2-3-1|supremum]] has to be taken over $\theta$ (here, at once over $x$ and $\theta$, with the factor $b-a$, so as not to discuss the integrability of the supremum function). At the end of the proof the notes say “$\varphi(y_0,h)\xrightarrow[h\to\infty]{}0$”; it should be $h\to0$.

> [!note] Restored
> (by the standard proof; the notes do not prove that $I'$ is continuous). The function $I'(y)=\int_a^b\frac{\partial f}{\partial y}(x,y)\,dx$ is continuous on $[c,d]$ by [[#^thm-9-1-1|Theorem 9.1.1]] applied to the function $\frac{\partial f}{\partial y}\in C(P)$. Therefore $I\in C^1([c,d])$.

**Example (Bessel's equation).** Let us check that for integer $n$ the function
$$
u(x)=\int_0^{\pi}\cos(n\varphi-x\sin\varphi)\,d\varphi
$$
satisfies Bessel's equation
$$
x^2u''+xu'+(x^2-n^2)u=0 .
$$
The integrand $\cos(n\varphi-x\sin\varphi)$ and its [[en/lectures-2025-26/lecture-61-62#Printed slide 8 (PDF p. 9). Partial derivatives — Definition 6.1.5|partial derivatives]] in $x$ of any order are continuous on every rectangle $[0,\pi]\times[c,d]$, so by [[#^thm-9-1-2|Theorem 9.1.2]] (applied twice; the variable of integration here is $\varphi$, the parameter is $x$) $u\in C^2(\mathbb R)$, and the derivatives can be computed by differentiation under the integral sign:
$$
u'(x)=\int_0^{\pi}\frac{\partial}{\partial x}\cos(n\varphi-x\sin\varphi)\,d\varphi=\int_0^{\pi}\bigl(-\sin(n\varphi-x\sin\varphi)\bigr)(-\sin\varphi)\,d\varphi=\int_0^{\pi}\sin\varphi\,\sin(n\varphi-x\sin\varphi)\,d\varphi ,
$$
$$
u''(x)=-\int_0^{\pi}\sin^2\varphi\,\cos(n\varphi-x\sin\varphi)\,d\varphi .
$$

> [!info] Source correction
> (T254). In the notes the first formula starts with “$u(x)=\int_0^\pi\cos x\cos(n\varphi-x\sin\varphi)\,d\varphi$”; what is computed here is the derivative $u'(x)=\int_0^\pi\frac{\partial}{\partial x}\cos(n\varphi-x\sin\varphi)\,d\varphi$; the rest is as in the notes.

Substitute into the left-hand side of the equation:
$$
x^2u''+xu'+(x^2-n^2)u=\int_0^{\pi}\Bigl[-x^2\sin^2\varphi\cos(n\varphi-x\sin\varphi)+x\sin\varphi\sin(n\varphi-x\sin\varphi)+(x^2-n^2)\cos(n\varphi-x\sin\varphi)\Bigr]d\varphi .
$$

> [!info] Source correction
> (M255, M523). In the notes the integrand lacks the term $(x^2-n^2)\cos(n\varphi-x\sin\varphi)$ corresponding to the term $(x^2-n^2)u$. Moreover, the statement of the example does not say that $n$ is an integer; without this the statement is false (see the computation below: the left-hand side equals $-(n-x)\sin(n\pi)$).

> [!note] Restored
> (by the standard computation; in the notes the computation breaks off at this formula). Put $\psi(\varphi)=n\varphi-x\sin\varphi$, so that $\psi'(\varphi)=n-x\cos\varphi$. Since $-x^2\sin^2\varphi+x^2=x^2\cos^2\varphi$, the integrand equals
> $$
> (x^2\cos^2\varphi-n^2)\cos\psi+x\sin\varphi\sin\psi=-\frac{d}{d\varphi}\Bigl[(n+x\cos\varphi)\sin\psi(\varphi)\Bigr],
> $$
> since
> $$
> \frac{d}{d\varphi}\Bigl[(n+x\cos\varphi)\sin\psi\Bigr]=-x\sin\varphi\sin\psi+(n+x\cos\varphi)(n-x\cos\varphi)\cos\psi=(n^2-x^2\cos^2\varphi)\cos\psi-x\sin\varphi\sin\psi .
> $$
> Therefore (for $\varphi=0$ the expression in square brackets equals $(n+x)\sin0=0$)
> $$
> x^2u''+xu'+(x^2-n^2)u=-\Bigl[(n+x\cos\varphi)\sin(n\varphi-x\sin\varphi)\Bigr]_{\varphi=0}^{\varphi=\pi}=-(n-x)\sin(n\pi)=0 ,
> $$
> since $n$ is an integer.

## Cross-references

- Course topic: [[en/11-power-series|chapter 11 “Power series and analytic functions”]] — [[en/11-power-series#11.2 Uniform convergence and calculus|§11.2 “Uniform convergence and operations”]], [[en/11-power-series#11.3 Standard expansions|§11.3 “Standard expansions”]], [[en/11-power-series#11.4 Analytic does not mean merely smooth|§11.4 “Analyticity is not smoothness”]] (it also has the function $e^{-1/x^2}$, whose Taylor series converges, but not to it: case 3 of the list above); [[en/09-improper-integrals-applications#^dirichlet-test-for-integrals|the Dirichlet test for integrals]] (convergence of the integral $\int_0^{+\infty}\frac{\sin x}{x}\,dx$).
- The beginning of §8.4 ([[en/lectures-2025-26/lecture-73-74#^def-8-4-1|Definitions 8.4.1]], [[en/lectures-2025-26/lecture-73-74#^def-8-4-2|8.4.2]], the Cauchy–Hadamard formula, [[en/lectures-2025-26/lecture-73-74#^thm-8-4-2|Theorems 8.4.2]] and Abel's [[en/lectures-2025-26/lecture-73-74#^thm-8-4-3|8.4.3]]): [[en/lectures-2025-26/lecture-73-74|lectures 73–74]]; [[en/lectures-2025-26/lecture-71-72#^thm-8-2-2|Theorems 8.2.2]], [[en/lectures-2025-26/lecture-71-72#^thm-8-3-1|8.3.1]]–[[en/lectures-2025-26/lecture-73-74#^thm-8-3-3|8.3.3]] and the Weierstrass test — [[en/lectures-2025-26/lecture-71-72|lectures 71–72]] and [[en/lectures-2025-26/lecture-73-74|lectures 73–74]].
- Taylor's formula and [[en/lectures-2025-26/lecture-29-30#^lem-3-6-2|Lemma 3.6.2]] on the estimate of the remainder: [[en/lectures-2025-26/lecture-29-30|lectures 29–30]].
- Continuation of chapter 9 (improper integrals depending on a parameter): [[en/lectures-2025-26/lecture-77-78|lectures 77–78]].

---

[[en/lectures-2025-26/lecture-73-74|← Lectures 73–74]] · [[en/lectures-2025-26/index|Lecture index]] · [[en/lectures-2025-26/lecture-77-78|Lectures 77–78 →]] · [[en/term-index|Terms & theorems]] · [[ru/lectures-2025-26/lecture-75-76|Русский]] · [[es/lectures-2025-26/lecture-75-76|Español]]

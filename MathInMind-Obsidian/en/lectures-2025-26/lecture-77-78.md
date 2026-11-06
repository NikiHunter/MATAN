---
title: "Lectures 77–78 — integration with respect to a parameter, improper integrals depending on a parameter, Feynman's method"
lang: en
course: "Mathematical Analysis, 2025/26"
lecture: 77-78
semester: 3
source: "handwritten notebook, pages p058–p066"
source_pages: "p058, p059, p060, p061, p062, p063, p064, p065, p066"
course_chapter: 25
aliases: ["Lectures 77–78 (en)"]
tags: [mathinmind/en, mathinmind/lecture]
---
# Lectures 77–78 — integration with respect to a parameter, improper integrals depending on a parameter, Feynman's method

[[en/lectures-2025-26/lecture-75-76|← Lectures 75–76]] · [[en/lectures-2025-26/index|Lecture index]] · [[en/lectures-2025-26/lecture-79-80|Lectures 79–80 →]] · [[en/term-index|Terms & theorems]] · [[ru/lectures-2025-26/lecture-77-78|Русский]] · [[es/lectures-2025-26/lecture-77-78|Español]]

> [!info] Source and numbering
> These notes were copied from a handwritten notebook (pages p058–p066; the raw page text is in [`ocr/raw/`](https://github.com/NikiHunter/matan/blob/main/ocr/raw/p058.md)). Page p058 begins with the end of the example with Bessel's equation from §9.1 (its beginning is in lectures 75–76); in the margin of the same page the record “Lectures 77–78” begins in red with the plan of the class: integration of an integral with respect to a parameter for proper integrals; theorems on [[en/lectures-2025-26/lecture-47-48#^def-4-5-2|improper integrals]] depending on a parameter; properties of the gamma function (in the notebook the gamma function is written already in lectures 79–80). The numbering of definitions and theorems is the lecturer's; the statements are checked against the slides of the 2024/25 course (FS p84–p87). [[#^thm-9-1-3|Theorems 9.1.3]], [[#^thm-9-2-2|9.2.2]] and [[#^thm-9-2-3|9.2.3]] are given in the notes without proof ([[#^thm-9-1-3|Theorem 9.1.3]] was also given “without proof” in 2024/25, FS p84), for [[#^thm-9-2-1|Theorem 9.2.1]] only the idea of the proof is written, and the Bolzano–Cauchy criterion is proved briefly; the missing proofs are restored from standard courses (Fichtenholz, vol. II, ch. XIV; Zorich, vol. II, ch. XVII). The motivating example at the beginning of §9.2, badly garbled in the transcription, is restored by its meaning. The figures in the margin of page p060 (number axes for the Bolzano–Cauchy criterion) are described in words. Slips in the notes are corrected and marked with “Source correction” blocks; lost passages are restored and marked with “Restored” blocks; the tags match [`ocr/RESOLVED.md`](https://github.com/NikiHunter/matan/blob/main/ocr/RESOLVED.md). Places that still have to be checked against the notebook are listed in [`ocr/ISSUES.md`](https://github.com/NikiHunter/matan/blob/main/ocr/ISSUES.md).

## §9.1. Proper integrals depending on a parameter (conclusion)


**Example (Bessel's equation, conclusion).** For the function $u(x)=\int_0^{\pi}\cos(n\varphi-x\sin\varphi)\,d\varphi$ ($n$ an integer) we obtained in lectures 75–76
$$
x^2u''+xu'+(x^2-n^2)u=\int_0^{\pi}\Bigl[-x^2\sin^2\varphi\cos(n\varphi-x\sin\varphi)+x\sin\varphi\sin(n\varphi-x\sin\varphi)+(x^2-n^2)\cos(n\varphi-x\sin\varphi)\Bigr]d\varphi .
$$
Collect like terms and note that the integrand is a derivative with respect to $\varphi$:
$$
\begin{aligned}
x^2u''+xu'+(x^2-n^2)u&=\int_0^{\pi}\Bigl[(1-\sin^2\varphi)x^2\cos(n\varphi-x\sin\varphi)+x\sin\varphi\sin(n\varphi-x\sin\varphi)-n^2\cos(n\varphi-x\sin\varphi)\Bigr]d\varphi\\
&=\int_0^{\pi}\frac{d}{d\varphi}\Bigl[-(n+x\cos\varphi)\sin(n\varphi-x\sin\varphi)\Bigr]d\varphi=-(n+x\cos\varphi)\sin(n\varphi-x\sin\varphi)\Big|_{\varphi=0}^{\varphi=\pi}=0 ,
\end{aligned}
$$
since $\sin0=0$ and $\sin n\pi=0$ for integer $n$. Thus $u$ satisfies Bessel's equation $x^2u''+xu'+(x^2-n^2)u=0$. ^p058

> [!info] Source correction
> (M256, T524). In the notes the integrand contains “$+n^2\cos(n\varphi-x\sin\varphi)$”, and the result is written as “$\left.0\right|_{0}^{\pi}$ ✓”. The term $(x^2-n^2)u$ gives $-n^2\cos(n\varphi-x\sin\varphi)$ under the integral, and only with this sign is the integrand a derivative: for $\psi(\varphi)=n\varphi-x\sin\varphi$, $\psi'(\varphi)=n-x\cos\varphi$,
> $$
> \frac{d}{d\varphi}\Bigl[-(n+x\cos\varphi)\sin\psi\Bigr]=x\sin\varphi\sin\psi-(n+x\cos\varphi)(n-x\cos\varphi)\cos\psi=x^2\cos^2\varphi\cos\psi+x\sin\varphi\sin\psi-n^2\cos\psi .
> $$
> The integral of a derivative equals the difference of the values of the [[en/lectures-2025-26/lecture-36#^def-4-1-1|antiderivative]] at $\varphi=\pi$ and $\varphi=0$; both are zero.

### On integrating an integral with respect to a parameter

> [!theorem] Theorem 9.1.3
> Let $P=\{(x,y)\in\mathbb R^2:\ a\le x\le b,\ c\le y\le d\}$ and $f=f(x,y)\in C(P)$. Then the function $I(y)=\int_a^bf(x,y)\,dx$ is integrable on $[c,d]$, and
> $$
> \int_c^d\left(\int_a^bf(x,y)\,dx\right)dy=\int_a^b\left(\int_c^df(x,y)\,dy\right)dx .
> $$

^thm-9-1-3

> [!note] Restored
> (by the standard proof, cf. Fichtenholz, vol. II, ch. XIV; there is no proof in the notes, and on the slide of the 2024/25 course, FS p84, the theorem is marked “without proof”).
>
> **Proof.** By [[en/lectures-2025-26/lecture-75-76#^thm-9-1-1|Theorem 9.1.1]] the function $I$ is continuous on $[c,d]$, hence integrable on $[c,d]$; by the same theorem (with the roles of the variables exchanged) the function $x\mapsto\int_c^df(x,y)\,dy$ is continuous on $[a,b]$. For $u\in[c,d]$ put
> $$
> \Phi(u)=\int_c^u\left(\int_a^bf(x,y)\,dx\right)dy,\qquad\Psi(u)=\int_a^bF(x,u)\,dx,\qquad F(x,u)=\int_c^uf(x,y)\,dy .
> $$
> Since $I$ is continuous, by Barrow's theorem $\Phi'(u)=I(u)=\int_a^bf(x,u)\,dx$. The function $F$ is continuous on $P$: if $M=\max_P|f|$, then
> $$
> |F(x',u')-F(x,u)|\le\left|\int_u^{u'}f(x',y)\,dy\right|+\int_c^d|f(x',y)-f(x,y)|\,dy\le M|u'-u|+(d-c)\max_{y\in[c,d]}|f(x',y)-f(x,y)| ,
> $$
> and the last term tends to zero as $x'\to x$, since $f$ is [[en/lectures-2025-26/lecture-17-18#^def-2-5-7|uniformly continuous]] on the [[en/lectures-2025-26/lecture-57-58#^def-5-3-7|compact set]] $P$ (Cantor's theorem). By Barrow's theorem $\frac{\partial F}{\partial u}(x,u)=f(x,u)$, and this function is also continuous on $P$. Therefore, by [[en/lectures-2025-26/lecture-75-76#^thm-9-1-2|Theorem 9.1.2]] (with the parameter $u$), the function $\Psi$ is differentiable on $[c,d]$ and $\Psi'(u)=\int_a^b\frac{\partial F}{\partial u}(x,u)\,dx=\int_a^bf(x,u)\,dx$. Thus $\Phi'=\Psi'$ on $[c,d]$ and $\Phi(c)=\Psi(c)=0$ (since $F(x,c)=0$); consequently $\Phi\equiv\Psi$ on $[c,d]$. For $u=d$ we get the required equality. $\square$

**Example.** Let us compute the integral
$$
I(b)=\int_0^1\frac{x^b-x^a}{\ln x}\,dx ,\qquad a,b>-1 .
$$
We regard $a$ as fixed and $b$ as variable. The idea: represent the integrand as an integral over an auxiliary variable $z$. Since $\frac{\partial}{\partial z}\left(\frac{x^z}{\ln x}\right)=\frac{\ln x\cdot x^z}{\ln x}=x^z$ for $0<x<1$, we have
$$
\int_a^bx^z\,dz=\frac{x^z}{\ln x}\Big|_{z=a}^{z=b}=\frac{x^b-x^a}{\ln x},
$$
i.e.
$$
I(b)=\int_0^1\left(\int_a^bx^z\,dz\right)dx .
$$
The integral $\int_0^1x^s\,dx$ converges if and only if $s>-1$, and then equals $\frac1{s+1}$; hence for $a,b>-1$ the integrals $\int_0^1x^z\,dx$ converge for all $z$ between $a$ and $b$. Changing the order of integration ([[#^thm-9-1-3|Theorem 9.1.3]]), we get
$$
I(b)=\int_a^b\left(\int_0^1x^z\,dx\right)dz=\int_a^b\frac{dz}{z+1}=\ln|1+z|\,\Big|_a^b=\ln\frac{b+1}{a+1} .
$$

> [!info] Source correction
> (M262). The notes say “Cons. $\int_0^1x^s\,dx<+\infty\Rightarrow b>-1$”, then “$\int_a^b>-1\Rightarrow I(b)=\int_0^1\left(\int_a^bx^z\,dz\right)dx=\int_a^b\left(\int_0^1x^z\,dx\right)dx$”. The condition of convergence is $s>-1$, and it is needed for all $z$ between $a$ and $b$, i.e. $a,b>-1$; after the interchange the outer integral is taken over $z$ (the differential $dz$, not $dx$).

> [!note] Restored
> (by the standard argument; in the notes the interchange of integrals is not justified). [[#^thm-9-1-3|Theorem 9.1.3]] concerns a function continuous on a rectangle, while for $\min\{a,b\}\le0$ the function $x^z$ is not continuous (or not bounded) near $x=0$, and the integral $I(b)$ may be improper at zero. So we apply [[#^thm-9-1-3|Theorem 9.1.3]] to the continuous function $x^z$ on the rectangle $[\varepsilon,1]\times[\min\{a,b\},\max\{a,b\}]$, $0<\varepsilon<1$ (for $x=1$ the integrand $I(b)$ is extended by its limit $b-a$, which agrees with $\int_a^b1^z\,dz=b-a$):
> $$
> \int_\varepsilon^1\frac{x^b-x^a}{\ln x}\,dx=\int_a^b\left(\int_\varepsilon^1x^z\,dx\right)dz=\int_a^b\frac{1-\varepsilon^{z+1}}{z+1}\,dz .
> $$
> Let $m=\min\{a,b\}>-1$. For $z$ between $a$ and $b$ we have $0<\varepsilon^{z+1}\le\varepsilon^{m+1}$, hence $\left|\int_a^b\frac{\varepsilon^{z+1}}{z+1}\,dz\right|\le\varepsilon^{m+1}\left|\ln\frac{b+1}{a+1}\right|\to0$ as $\varepsilon\to0+$. Thus the integral $I(b)$ converges and equals $\ln\frac{b+1}{a+1}$.

## §9.2. Improper integrals depending on a parameter


### A motivating example

**Example.** For $y\in[0,+\infty)$ consider the integral
$$
I(y)=\int_0^1\frac{x+y}{x^{1-y}}\,dx=\int_0^1(x+y)\,x^{y-1}\,dx ,\qquad x\in(0,1] .
$$
For $y>0$
$$
I(y)=\int_0^1x^{y}\,dx+y\int_0^1x^{y-1}\,dx=\frac{x^{y+1}}{y+1}\Big|_0^1+y\,\frac{x^{y}}{y}\Big|_0^1=\frac1{y+1}+1 ,
$$
i.e. $I(y)\to2$ for $y\to0+$. On the other hand, for $y=0$
$$
I(0)=\int_0^1\frac xx\,dx=\int_0^1 1\,dx=1 .
$$
So $\lim_{y\to0+}I(y)=2\ne1=I(0)$: the function $I$ is discontinuous at the point $y=0$, although the integrand is continuous in $y$ for each $x\in(0,1]$.

> [!note] Restored
> (by the meaning of the record; the transcription of the example in the notebook is badly garbled — tags U264–M268). The transcription has “$I(y)=\int_0^1\frac{x+y}{x^{y/3}}\,dx$”, “$=\int_0^1x^{-y}dx+\int_0^1x^{y-3}dx=\left.\frac{x^{y+1}}{y+1}\right|_0^1+\left.y\frac{x^3}{3}\right|_0^1=\frac1{y+1}+1$”, “i.e. $x\in(0,1]\Rightarrow I(y)\to2$”, “$\Rightarrow\left|I(y)-\frac{2}{y\to0}\right|\not\to I(0)$”. The integrand is restored as $(x+y)x^{y-1}$: only with it is $f(x,0)=\frac xx$ (as in the line for $I(0)$), the first term gives the recorded $\frac{x^{y+1}}{y+1}\Big|_0^1=\frac1{y+1}$, the second (with the surviving factor $y$) gives one, and the result $\frac1{y+1}+1$ agrees with the notes; the last line means $I(y)\to2\ne I(0)$ for $y\to0$. The reason for the discontinuity lies in the behaviour of the integral near the singular point $x=0$: for every $\delta\in(0,1]$
> $$
> \int_0^{\delta}(x+y)\,x^{y-1}\,dx=\frac{\delta^{y+1}}{y+1}+\delta^{y}\ \ge\ \delta^{y}\to1\qquad(y\to0+),
> $$
> i.e. the “tail” of the integral near the singular point cannot be made small for all $y>0$ at once. This leads to the notion of [[en/10-function-sequences-series#10.1 Two modes of convergence|uniform convergence]] of an improper integral ([[#^def-9-2-1|Definition 9.2.1]]; here the singularity is at the [[en/lectures-2025-26/lecture-13#Definition 2.3.9 (upper and lower limits)|lower limit]], see the remark after the examples).

### Improper integrals depending on a parameter

Let the function $f(x,y)$ be defined on the set $[a,b)\times Y$, where $-\infty<a<b\le+\infty$. We assume that the function $f$ is continuous in $x$ for each fixed $y\in Y$. Consider the improper integral
$$
I(y):=\int_a^{\to b}f(x,y)\,dx=\lim_{\omega\to b}\int_a^{\omega}f(x,y)\,dx=\lim_{\omega\to b}I_\omega(y),\qquad I_\omega(y):=\int_a^{\omega}f(x,y)\,dx,\quad\omega\in[a,b) .
$$
From now on we write such an integral simply as $\int_a^bf(x,y)\,dx$ and assume that it converges for each $y\in Y$.

> [!definition] Definition 9.2.1
> We say that $I(y)$ converges uniformly with respect to $y\in Y$ (uniformly on $Y$) if
> $$
> \forall\varepsilon>0\ \ \exists b_0\in[a,b)\ \ \forall b'\in(b_0,b)\ \ \forall y\in Y:\quad |I_{b'}(y)-I(y)|=\left|\int_{b'}^{b}f(x,y)\,dx\right|<\varepsilon .
> $$
> In other words, uniform convergence of the improper integral $I(y)$ requires that $I_{b'}(y)\rightrightarrows I(y)$ on $Y$ as $b'\to b$.

^def-9-2-1

> [!info] Source correction
> (S271, T272). The notes say (likewise the slide FS p85): “$\forall\varepsilon>0\ \exists b_0\in[a,b)$ such that $\forall b'>b_0\ |I_{b'}(y)-I(y)|<\varepsilon$” — without a [[en/01-logic-sets-functions#1.1 Propositions and quantifiers|quantifier]] over $y$ and without stating that $b'<b$; then “$I_{b'}(y)\rightrightarrows I(y)$, $b\to b$”. The quantifiers $\forall b'\in(b_0,b)$ and $\forall y\in Y$ are added, with $\forall y$ placed after the choice of $b_0$ — this is exactly what the next remark expresses; the passage to the limit is $b'\to b$.

**Remark.** In [[#^def-9-2-1|Definition 9.2.1]] it is essential that $b_0$ does not depend on $y$, but only on $\varepsilon$.

Recall that a functional series $\sum_{n=1}^{\infty}a_n(y)=S(y)$ converges uniformly on $Y$ if $S_n(y)=\sum_{k=1}^{n}a_k(y)\rightrightarrows S(y)$ on $Y$.

> [!info] Source correction
> (T273). The notes say “A functional series … conv. if: $S_n(y)=\sum a_n(y)\rightrightarrows S(y)$”. What is meant is uniform convergence, and the [[en/04-numeric-series#4.1 Convergence through partial sums|partial sum]] is $S_n(y)=\sum_{k=1}^{n}a_k(y)$ (as on the slide FS p85).


Thus uniform convergence of an integral and of a series are described in the same way: ^p060

| Integral | Series |
|---|---|
| $I_t(y)\rightrightarrows I(y)$ on $Y$ as $t\to b$ | $S_n(y)\rightrightarrows S(y)$ on $Y$ as $n\to\infty$ |

### The Bolzano–Cauchy criterion

The improper integral $I(y)=\int_a^bf(x,y)\,dx$ converges uniformly on $Y$ if and only if
$$
\forall\varepsilon>0\ \ \exists b_0\in[a,b)\ \ \forall t_1,t_2\in(b_0,b)\ \ \forall y\in Y:\quad\left|\int_{t_1}^{t_2}f(x,y)\,dx\right|<\varepsilon .
$$
Similarly, the series $\sum_{k=1}^{\infty}a_k(y)$ converges uniformly on $Y$ if and only if
$$
\forall\varepsilon>0\ \ \exists n_0\in\mathbb N\ \ \forall m>n>n_0\ \ \forall y\in Y:\quad\left|\sum_{k=n}^{m}a_k(y)\right|<\varepsilon .
$$

*Figures in the notes (page p060): next to the condition for the integral, a number axis with the points $a<b_0<t_1<t_2<b$; next to the condition for the series, an axis with the indices $n_0<n<m$.*

> [!info] Source correction
> (M525). In the notes (likewise on the slide FS p85) the conditions of the criterion lack the quantifier “$\forall y\in Y$”, and without it the condition does not express uniformity. $\forall y\in Y$ is added after the choice of $b_0$ (respectively $n_0$); the final lines of the proof of the Dirichlet test are completed in the same way.

**Proof** (for the integral). The inequality $\left|\int_{t_1}^{t_2}f(x,y)\,dx\right|<\varepsilon$ is equivalent to the inequality $|I_{t_2}(y)-I_{t_1}(y)|<\varepsilon$. Therefore the statement is the Bolzano–Cauchy criterion for the uniform convergence of the functions $I_t(y)$ depending on the parameter $t$, as $t\to b$.

> [!note] Restored
> (by the standard proof, cf. Zorich/Fichtenholz; in the notes the proof is brief, and the Bolzano–Cauchy criterion was proved for sequences of functions).
>
> *Necessity.* Let $I(y)$ converge uniformly on $Y$, and $\varepsilon>0$. By [[#^def-9-2-1|Definition 9.2.1]] there is $b_0\in[a,b)$ such that $\left|\int_t^bf(x,y)\,dx\right|<\frac{\varepsilon}2$ for all $t\in(b_0,b)$ and $y\in Y$. Then for $t_1,t_2\in(b_0,b)$ and $y\in Y$
> $$
> \left|\int_{t_1}^{t_2}f(x,y)\,dx\right|=\left|\int_{t_1}^{b}f(x,y)\,dx-\int_{t_2}^{b}f(x,y)\,dx\right|<\frac{\varepsilon}2+\frac{\varepsilon}2=\varepsilon .
> $$
> *Sufficiency.* Let the condition of the criterion hold. For each fixed $y\in Y$ it is the [[en/lectures-2025-26/lecture-13#^def-2-3-10|Cauchy condition]] for the existence of a finite limit of the function $t\mapsto I_t(y)$ as $t\to b$; hence the integral $I(y)$ converges for each $y\in Y$. Passing to the limit as $t_2\to b$ in the inequality $\left|\int_{t_1}^{t_2}f(x,y)\,dx\right|<\varepsilon$, we get $|I(y)-I_{t_1}(y)|=\left|\int_{t_1}^{b}f(x,y)\,dx\right|\le\varepsilon$ for all $t_1\in(b_0,b)$ and $y\in Y$. Since $\varepsilon>0$ is arbitrary, the integral $I(y)$ converges uniformly on $Y$. $\square$
>
> For series the criterion was proved in lectures 71–72.

### The Weierstrass test

Suppose there is a function $\varphi:[a,b)\to[0,+\infty)$, integrable on every segment $[a,t]\subset[a,b)$, such that

1. $|f(x,y)|\le\varphi(x)$ for all $x\in[a,b)$ and $y\in Y$;
2. the improper integral $\int_a^b\varphi(x)\,dx$ converges.

Then the integral $I(y)=\int_a^bf(x,y)\,dx$ converges uniformly on $Y$.

For series: if there are numbers $C_n>0$ such that $|a_n(y)|\le C_n$ for all $n\in\mathbb N$ and $y\in Y$, and the series $\sum_{n=1}^{\infty}C_n$ converges, then the series $\sum_{n=1}^{\infty}a_n(y)$ converges uniformly on $Y$ (lectures 71–72).

> [!info] Source correction
> (U277). In the notes the conditions for the integral are written as “∃ fn $Y$ such that $\forall x\in[a,b),\forall y\in Y\ |f(x,y)|\le\varphi(x)$; 1) $\int_a^b\varphi(x)\,dx\le\infty$”, and the numbers 1), 2) are mixed with the lines for the series. It is read as on the slide FS p85: “$\exists$ a function $\varphi$ such that 1) $|f(x,y)|\le\varphi(x)$ …; 2) $\int_a^b\varphi(x)\,dx<\infty$” — the integral of the majorant converges (“$\le\infty$” makes no sense).

**Proof.** The statement follows from the estimate
$$
\left|\int_{t_1}^{t_2}f(x,y)\,dx\right|\le\int_{t_1}^{t_2}|f(x,y)|\,dx\le\int_{t_1}^{t_2}\varphi(x)\,dx\qquad(a\le t_1<t_2<b)
$$
and the Bolzano–Cauchy criterion. Indeed, since $\int_a^b\varphi(x)\,dx$ converges, for every $\varepsilon>0$ there is $b_0\in[a,b)$ such that $\int_{t_1}^{t_2}\varphi(x)\,dx<\varepsilon$ for $b_0<t_1<t_2<b$; the right-hand side of the estimate does not depend on $y$, so the condition of the Bolzano–Cauchy criterion holds. $\square$


**Example.** The integral $\int_0^{\infty}\frac{\cos(\alpha x)}{1+x^2}\,dx$ converges uniformly in $\alpha\in\mathbb R$: for all $x\ge0$ and $\alpha\in\mathbb R$
$$
\left|\frac{\cos(\alpha x)}{1+x^2}\right|\le\frac1{1+x^2},
$$
and the integral $\int_0^{\infty}\frac{dx}{1+x^2}=\frac{\pi}2$ converges; it remains to apply the [[en/10-function-sequences-series#^weierstrass-m-test|Weierstrass test]]. ^p061

### The Dirichlet test

Let the functions $f$ and $g$ be defined on $[a,b)\times Y$, continuous in $x$ for each $y\in Y$, and

1. for each $y\in Y$ the function $f(\cdot,y)$ be monotone on $[a,b)$, and $f(x,y)\rightrightarrows0$ on $Y$ as $x\to b$, i.e. $\sup_{y\in Y}|f(x,y)|\to0$ as $x\to b$;
2. the antiderivatives $G(t,y):=\int_a^tg(x,y)\,dx$ be uniformly bounded: there is $C>0$ such that $|G(t,y)|\le C$ for all $t\in[a,b)$ and $y\in Y$.

Then the integral $\int_a^bf(x,y)g(x,y)\,dx$ converges uniformly on $Y$.

For series: if for each $y\in Y$ the sequence $a_n(y)$ is monotone in $n$ and $a_n(y)\rightrightarrows0$ on $Y$, and the partial sums $B_n(y):=\sum_{k=1}^{n}b_k(y)$ are uniformly bounded ($\exists C>0:\ |B_n(y)|\le C$ for all $n\in\mathbb N$, $y\in Y$), then the series $\sum_{n=1}^{\infty}a_n(y)b_n(y)$ converges uniformly on $Y$.

> [!info] Source correction
> (T280). The notes say “1) $f(x,y)\to0$ uniformly on $Y$” and for the series “1) $a_n(y)\to0$ uniformly on $Y$” — without monotonicity, and the partial sums of the series are written as “$b_n(y):=\sum b_k(g)$; $\exists C>0: |b_n(y)|\le C$”. The proof uses the monotonicity of $f$ in $x$ (the [[en/lectures-2025-26/lecture-43-44#^thm-4-3-1|second mean value theorem]]; in the notes themselves, “$f(x,y)\downarrow0$ uniformly on $Y$”), and on the slide FS p86 the condition is written as “$f(x,y)\searrow0$ uniformly on $Y$”, “$a_n(y)\searrow0$ uniformly on $Y$”. Monotonicity is added (either direction of monotonicity works); the partial sums are $B_n(y)=\sum_{k=1}^{n}b_k(y)$.

**Proof** (for the integral). We use the Bolzano–Cauchy criterion for the uniform convergence of an improper integral. To this end we estimate, for $a\le t_1<t_2<b$, the integral $\left|\int_{t_1}^{t_2}f(x,y)g(x,y)\,dx\right|$.

Recall the second mean value theorem ([[en/lectures-2025-26/lecture-45-46#^thm-4-4-3|Theorem 4.4.3]], Bonnet): if $\varphi\in C([\alpha,\beta])$, $\psi\in C^1([\alpha,\beta])$ and $\psi$ is monotone on $[\alpha,\beta]$, then there is $\xi\in[\alpha,\beta]$ such that
$$
\int_\alpha^\beta\varphi\psi=\psi(\alpha)\int_\alpha^\xi\varphi+\psi(\beta)\int_\xi^\beta\varphi .
$$
The formula remains true if $\varphi$ is integrable on $[\alpha,\beta]$ and $\psi$ is merely monotone on $[\alpha,\beta]$. (The second mean value theorem also has other formulations.)

> [!info] Source correction
> (M283). The notes say “$\int_a^bf\cdot\hat g=\hat g(a)\int_a^bf+\hat g(b)\int_c^bf$”. In the first term the integral is taken over $[a,c]$, not over $[a,b]$ ([[en/lectures-2025-26/lecture-45-46#^thm-4-4-3|Theorem 4.4.3]]; otherwise for $\hat g\equiv1$ one would get $\int_a^bf=\int_a^bf+\int_c^bf$).

Apply it for fixed $y\in Y$ to $\varphi=g(\cdot,y)$ and the monotone function $\psi=f(\cdot,y)$ on the segment $[t_1,t_2]$: there is $\xi\in[t_1,t_2]$ such that
$$
\left|\int_{t_1}^{t_2}f(x,y)g(x,y)\,dx\right|=\left|f(t_1,y)\int_{t_1}^{\xi}g(x,y)\,dx+f(t_2,y)\int_{\xi}^{t_2}g(x,y)\,dx\right|\le|f(t_1,y)|\left|\int_{t_1}^{\xi}g(x,y)\,dx\right|+|f(t_2,y)|\left|\int_{\xi}^{t_2}g(x,y)\,dx\right| .
$$


By condition 2
$$
\left|\int_{t_1}^{\xi}g(x,y)\,dx\right|=|G(\xi,y)-G(t_1,y)|\le|G(\xi,y)|+|G(t_1,y)|\le C+C=2C,
$$
$$
\left|\int_{\xi}^{t_2}g(x,y)\,dx\right|=|G(t_2,y)-G(\xi,y)|\le|G(t_2,y)|+|G(\xi,y)|\le C+C=2C .
$$
Consequently,
$$
\left|\int_{t_1}^{t_2}f(x,y)g(x,y)\,dx\right|\le2C\bigl(|f(t_1,y)|+|f(t_2,y)|\bigr).
$$

^p062

> [!info] Source correction
> (M289). The notes say “$\left|\int_{n_1}^{n_2}f(x,y)g(x,y)\,dx\right|<2C\cdot\left[|f(n_1,y)|+f(n_2,y)\right]$”. The absolute value is missing in the second term ($f$ may be negative), and the estimates with “$\le$” give a non-strict inequality.

Fix $\varepsilon>0$. Since $f(x,y)\rightrightarrows0$ on $Y$ as $x\to b$, there is $\eta\in[a,b)$ such that $|f(x,y)|<\frac{\varepsilon}{4C}$ for all $x\in[\eta,b)$ and $y\in Y$. Let $\eta<t_1<t_2<b$ (without loss of generality $a\le\eta<t_1<t_2<b$). Then for all $y\in Y$
$$
\left|\int_{t_1}^{t_2}f(x,y)g(x,y)\,dx\right|\le2C\bigl(|f(t_1,y)|+|f(t_2,y)|\bigr)<2C\left[\frac{\varepsilon}{4C}+\frac{\varepsilon}{4C}\right]=\varepsilon .
$$
Thus for every $\varepsilon>0$ there is $\eta\in[a,b)$ such that for all $t_1,t_2$ with $\eta<t_1<t_2<b$ and all $y\in Y$ we have $\left|\int_{t_1}^{t_2}f(x,y)g(x,y)\,dx\right|<\varepsilon$. By the Bolzano–Cauchy criterion the integral converges uniformly on $Y$. $\square$

### The Abel test

Let the functions $f$ and $g$ be defined on $[a,b)\times Y$, continuous in $x$ for each $y\in Y$, and

1. for each $y\in Y$ the function $f(\cdot,y)$ be monotone on $[a,b)$, and $f$ be uniformly bounded: there is $M>0$ such that $|f(x,y)|\le M$ for all $x\in[a,b)$ and $y\in Y$;
2. the integral $\int_a^bg(x,y)\,dx$ converge uniformly on $Y$.

Then the integral $\int_a^bf(x,y)g(x,y)\,dx$ converges uniformly on $Y$.

For series: if for each $y\in Y$ the sequence $a_n(y)$ is monotone in $n$, the sequence of functions $a_n$ is uniformly bounded on $Y$, and the series $\sum_{n=1}^{\infty}b_n(y)$ converges uniformly on $Y$, then the series $\sum_{n=1}^{\infty}a_n(y)b_n(y)$ converges uniformly on $Y$ (lectures 73–74).

> [!info] Source correction
> (T291). In the “Integral” part of the notes the conclusion is written the same way as for the series: “$\Rightarrow\sum a_n(y)b_n(y)$ conv. uniformly on $Y$”. For the integral the conclusion is the uniform convergence of the integral $\int_a^bf(x,y)g(x,y)\,dx$ (slide FS p86).


**Remark.** Unlike the Dirichlet test, here it is not required that $f(x,y)\to0$. Monotonicity and uniform boundedness of $f$ suffice, and all the “convergence” is provided by the uniform convergence of the integral of $g$.

^p063

**Proof** (for the integral). We use the Bolzano–Cauchy criterion for the uniform convergence of an improper integral. By condition 1 the function $f$ is uniformly bounded: $|f(x,y)|\le M$. Fix $\varepsilon>0$. Since $\int_a^bg(x,y)\,dx$ converges uniformly on $Y$, by the Bolzano–Cauchy criterion there is $\eta\in[a,b)$ such that for all $s_1,s_2\in(\eta,b)$ and all $y\in Y$
$$
\left|\int_{s_1}^{s_2}g(x,y)\,dx\right|<\frac{\varepsilon}{2M} .
$$
Let $\eta<t_1<t_2<b$ and $y\in Y$. Since the function $f(\cdot,y)$ is monotone, the second mean value theorem applies to the integral over $[t_1,t_2]$: there is $\xi\in[t_1,t_2]$ such that
$$
\begin{aligned}
\left|\int_{t_1}^{t_2}f(x,y)g(x,y)\,dx\right|&=\left|f(t_1,y)\int_{t_1}^{\xi}g(x,y)\,dx+f(t_2,y)\int_{\xi}^{t_2}g(x,y)\,dx\right|\\
&\le|f(t_1,y)|\cdot\left|\int_{t_1}^{\xi}g(x,y)\,dx\right|+|f(t_2,y)|\cdot\left|\int_{\xi}^{t_2}g(x,y)\,dx\right|<M\cdot\frac{\varepsilon}{2M}+M\cdot\frac{\varepsilon}{2M}=\varepsilon
\end{aligned}
$$
(the points $t_1,\xi,t_2$ lie in $(\eta,b)$, so both integrals of $g$ have absolute value less than $\frac{\varepsilon}{2M}$).

> [!info] Source correction
> (T296). In the notes the second term of the first line contains “$f(n_1,y)\int_\xi^{n_2}g(x,y)\,dx$”. By the second mean value theorem, the factor at $\int_\xi^{t_2}$ is the value of $f$ at the right endpoint, $f(t_2,y)$ (the next line of the notes has exactly that).

Thus for every $\varepsilon>0$ there is $\eta\in[a,b)$ such that for all $t_1,t_2$ with $a\le\eta<t_1<t_2<b$ and all $y\in Y$
$$
\left|\int_{t_1}^{t_2}f(x,y)g(x,y)\,dx\right|<\varepsilon ,
$$
i.e. the condition of the Bolzano–Cauchy criterion holds, and the integral converges uniformly on $Y$. $\square$


### Examples

**Example 1.** Consider the integral
$$
I_1(y)=\int_0^{+\infty}\frac{\sin x}{x}\,e^{-xy}\,dx .
$$
It converges for $y\ge0$. Does $I_1(y)$ converge uniformly on $Y=[0,+\infty)$? Yes: apply the Abel test to $f(x,y)=e^{-xy}$ and $g(x,y)=\frac{\sin x}{x}$ (for $x=0$ we extend $g$ by one):

1. for each $y\ge0$ the function $f(\cdot,y)=e^{-xy}$ is monotone (non-increasing) in $x$;
2. $|f(x,y)|\le1$ for all $x\ge0$, $y\ge0$;
3. the integral $\int_0^{\infty}\frac{\sin x}{x}\,dx$ converges, and since $g$ does not depend on $y$, it converges uniformly on $Y$.

Consequently $I_1(y)$ converges uniformly on $[0,+\infty)$ by the Abel test.

> [!info] Source correction
> (T298). In the notes the line for $f$ is repeated for $g$: “$g(x,y)=\frac{\sin x}{x}$, then $\forall y_0>0$, $f(x,y)\downarrow0$ $(x\to+\infty)$”. For the Abel test $f$ must be monotone in $x$ and uniformly bounded (for $y=0$ the function $f\equiv1$ does not tend to zero, so on $[0,+\infty)$ the Abel test is applied, not the Dirichlet test), and $g$ must have a uniformly convergent integral, i.e. here the convergence of $\int_0^\infty\frac{\sin x}{x}\,dx$ (item 3 of the notes).

**Example 2.** Consider the integral
$$
I_2(\alpha)=\int_1^{+\infty}\frac{\sin x}{x^{\alpha}}\,dx .
$$
For $\alpha\le0$ it diverges. Let us prove that for every $\alpha_0>0$ it converges uniformly on $[\alpha_0,+\infty)$. Apply the Dirichlet test to $f(x,\alpha)=x^{-\alpha}$ and $g(x,\alpha)=\sin x$:

1. for each $\alpha\ge\alpha_0$ the function $x^{-\alpha}$ decreases on $[1,+\infty)$, and $0<x^{-\alpha}\le x^{-\alpha_0}\to0$ for $x\to+\infty$, i.e. $x^{-\alpha}\rightrightarrows0$ on $[\alpha_0,+\infty)$;
2. $|G(t,\alpha)|=\left|\int_1^t\sin x\,dx\right|=\left|-\cos x\,\Big|_1^t\right|=|\cos1-\cos t|\le2$.

The conditions of the Dirichlet test for the uniform convergence of an improper integral depending on a parameter are satisfied; hence $I_2(\alpha)$ converges uniformly on $[\alpha_0,+\infty)$.

> [!info] Source correction
> (A299, A300, T301). The notes say: “$I_2(\alpha)=\int_0^{+\infty}\frac{\sin x}{x^\alpha}\,dx$, $\alpha<0$ — undefined”, “Let us prove uniform conv. on $[x_0,+\infty)$ ($x_0>0$)”, “$x^{-\alpha}\downarrow0$ ($\forall x>x_0$)”, “$|G(t,\alpha)|=\left|\int_0^t\sin x\,dx\right|=\dots=|-\cos t+\cos1|\le2$”. The final expression $|\cos1-\cos t|$ corresponds to the integral $\int_1^t\sin x\,dx$, and the integral over $[0,+\infty)$ cannot be considered here: for $\alpha\ge2$ it diverges at zero ($\frac{\sin x}{x^\alpha}\sim x^{1-\alpha}$), and the function $x^{-\alpha}$ is unbounded near zero. Therefore the integral is taken over $[1,+\infty)$ (uniform convergence is determined by the behaviour near the singular point $+\infty$), and the set of parameters is $[\alpha_0,+\infty)$, $\alpha_0>0$: on it $x^{-\alpha}\le x^{-\alpha_0}$, which gives the uniform tending to zero; for $\alpha\le0$ the integral diverges (“undefined”).

**Remark.** 1) An improper integral $I(y)=\int_{\to a}^{b}f(x,y)\,dx$ with a singularity at the lower limit ($a=-\infty$, or $f$ unbounded near $a$) is defined and studied similarly. 2) An integral $I(y)=\int_{\to a}^{\to b}f(x,y)\,dx$ with singularities at both endpoints is defined as the sum $I(y)=I_1(y)+I_2(y)$, where $I_1(y)=\int_{\to a}^{c}f(x,y)\,dx$, $I_2(y)=\int_{c}^{\to b}f(x,y)\,dx$, $c\in(a,b)$.


Such an integral is studied in parts: it converges (uniformly on $Y$) if both $I_1$ and $I_2$ converge (uniformly on $Y$). The convergence and the value of $I(y)$ do not depend on the choice of the point $c\in(a,b)$, i.e. the definition is correct. ^p065

> [!note] Restored
> (from the notes to the slides of the 2024/25 course, FS p86; the transcription of the end of the remark in the notebook is illegible). The transcription has: “2) $I(y)=\int_a^bf(x,y)\,dx$ the fn is defined and studied differently depending on the choice of application”, “Simultaneously taking $I_1$, and for $I_2$”. The 2024/25 notes have: “$\int_{\to a}^{\to b}f(x,y)\,dx=\int_{\to a}^{c}f(x,y)\,dx+\int_{c}^{\to b}f(x,y)\,dx$, where $c\in(a,b)$; one can show that the value of $\int_{\to a}^{\to b}f(x,y)\,dx$ does not depend on the choice of $c\in(a,b)$”.

### Continuity of an improper integral with respect to a parameter

> [!theorem] Theorem 9.2.1
> Let the function $f$ be continuous on $[a,b)\times[c,d]$, $y_0\in[c,d]$, and let the improper integral $I(y)=\int_a^bf(x,y)\,dx$ converge uniformly on $[c,d]\cap(y_0-\delta_0,y_0+\delta_0)$ for some $\delta_0>0$, i.e. in some neighbourhood of the point $y_0$. Then the function $I$ is continuous at the point $y_0$. In particular, if $I(y)$ converges uniformly on $[c,d]$, then $I\in C([c,d])$.

^thm-9-2-1

> [!info] Source correction
> (M526). The notes say: “[Let] $f(x,y)$ integr. in $x$ unif. $y_0$”, the slide FS p87: “Let the function $f(x,y)$ be continuous in $y$ at the point $y_0$”. Continuity in $y$ at a single point is not enough even for a proper integral: the proof needs the continuity of the integral $\int_a^\eta f(x,y)\,dx$ at the point $y_0$, which [[en/lectures-2025-26/lecture-75-76#^thm-9-1-1|Theorem 9.1.1]] gives for a function continuous on a rectangle. The standard condition is added: $f$ is continuous on $[a,b)\times[c,d]$.

### Differentiation of an improper integral with respect to a parameter

> [!theorem] Theorem 9.2.2
> Let the following conditions hold:
>
> 1. the functions $f(x,y)$ and $f'_y(x,y)$ are continuous on $[a,b)\times[c,d]$;
> 2. the integral $\int_a^bf'_y(x,y)\,dx$ converges uniformly on $[c,d]$;
> 3. the integral $I(y)=\int_a^bf(x,y)\,dx$ converges for at least one value $y_0\in[c,d]$.

^thm-9-2-2

Then $I(y)$ converges uniformly on the whole segment $[c,d]$, the function $I$ is differentiable on $[c,d]$, and
$$
I'(y)=\left(\int_a^bf(x,y)\,dx\right)'_y=\int_a^bf'_y(x,y)\,dx .
$$

> [!info] Source correction
> (M527). The notes (and the slide FS p87) say: “1) the fns $f(x,y)$ and $f'_y(x,y)$ are integr. [continuous] in $x$”, and the set of parameters is an arbitrary $Y$. Continuity in $x$ is not enough (already for proper integrals in [[en/lectures-2025-26/lecture-75-76#^thm-9-1-2|Theorem 9.1.2]] $f$ and $f'_y$ are continuous on a rectangle); condition 1 is replaced by the standard one. The set of parameters is taken to be a segment: on an unbounded set the conclusion about the uniform convergence of $I$ can be false (for example, $f(x,y)=ye^{-x}$ on $[0,+\infty)\times\mathbb R$: $\int_0^\infty f'_y\,dx=\int_0^\infty e^{-x}\,dx$ converges uniformly, but $\int_t^{\infty}ye^{-x}\,dx=ye^{-t}$ is not small uniformly in $y\in\mathbb R$). Since differentiability is a local property, on an arbitrary interval $Y$ the theorem is applied on each segment $[c,d]\subset Y$.

### Integration of an improper integral with respect to a parameter

> [!theorem] Theorem 9.2.3
> Let the following conditions hold:
>
> 1. the function $f(x,y)$ is continuous on $[a,b)\times[c,d]$;
> 2. the integral $I(y)=\int_a^bf(x,y)\,dx$ converges uniformly on $Y=[c,d]$.

^thm-9-2-3

Then $I$ is integrable on $[c,d]$, the improper integral on the right-hand side of the following equality converges, and
$$
\int_c^dI(y)\,dy=\int_a^b\left(\int_c^df(x,y)\,dy\right)dx .
$$

> [!info] Source correction
> (T307, M528). The notes say “$\int_c^dI(y)\,dy=\int_c^d\left(\int_a^bf(x,y)\,dy\right)dx$” — the limits of integration are mixed up: the inner integral is taken over $y$ from $c$ to $d$, the outer (improper) one over $x$ from $a$ to $b$ (slide FS p87). Condition 1 in the notes and on the slide is “$f(x,y)$ is continuous in $x$”; as in [[#^thm-9-2-1|Theorem 9.2.1]], continuity of $f$ on $[a,b)\times[c,d]$ is needed (it guarantees the continuity of $I$ and the applicability of [[#^thm-9-1-3|Theorem 9.1.3]] on the rectangles $[a,t]\times[c,d]$).

### Proofs of Theorems 9.2.1–9.2.3

**Proof of [[#^thm-9-2-1|Theorem 9.2.1]] (idea).** The proof rests on two steps.

1) By uniform convergence, for every $\varepsilon>0$ there is $\eta\in[a,b)$, independent of $y$, such that $\sup_{y}\left|\int_\eta^bf(x,y)\,dx\right|<\varepsilon$, where the [[en/lectures-2025-26/lecture-11-12#^def-2-3-1|supremum]] is taken over $y$ in a neighbourhood of the point $y_0$.

2) The increment of the integral is estimated through a proper integral over $[a,\eta]$ and two “tails”:
$$
|I(y_0+\Delta y)-I(y_0)|\le\left|\int_a^{\eta}\bigl[f(x,y_0+\Delta y)-f(x,y_0)\bigr]dx\right|+\left|\int_\eta^bf(x,y_0+\Delta y)\,dx\right|+\left|\int_\eta^bf(x,y_0)\,dx\right| .
$$


Having fixed $\varepsilon$, we find $\eta$ and then $\delta$: the sum of the two “tails” is less than $2\varepsilon$, and the proper integral over $[a,\eta]$ is small for small $|\Delta y|$. ^p066

> [!note] Restored
> (by the standard proof, cf. Fichtenholz, vol. II, ch. XIV; Zorich, vol. II, ch. XVII; in the notes only the idea is written, and [[#^thm-9-2-2|Theorems 9.2.2]] and [[#^thm-9-2-3|9.2.3]] are given without proof).
>
> **Proof of [[#^thm-9-2-1|Theorem 9.2.1]].** Let $\varepsilon>0$. The set $K=[c,d]\cap\left[y_0-\frac{\delta_0}2,\,y_0+\frac{\delta_0}2\right]$ is a segment containing $y_0$ and lying in the neighbourhood from the hypothesis. By [[#^def-9-2-1|Definition 9.2.1]] there is $\eta\in[a,b)$ such that $\left|\int_\eta^bf(x,y)\,dx\right|<\varepsilon$ for all $y\in K$. The function $f$ is continuous on the rectangle $[a,\eta]\times K$, so by [[en/lectures-2025-26/lecture-75-76#^thm-9-1-1|Theorem 9.1.1]] the proper integral $J(y)=\int_a^\eta f(x,y)\,dx$ is continuous on $K$, and there is $\delta\in\left(0,\frac{\delta_0}2\right]$ such that $|J(y)-J(y_0)|<\varepsilon$ for $y\in[c,d]$, $|y-y_0|<\delta$ (such $y$ lie in $K$). For these $y$
> $$
> |I(y)-I(y_0)|\le|J(y)-J(y_0)|+\left|\int_\eta^bf(x,y)\,dx\right|+\left|\int_\eta^bf(x,y_0)\,dx\right|<\varepsilon+\varepsilon+\varepsilon=3\varepsilon .
> $$
> Since $\varepsilon>0$ is arbitrary, $I$ is [[en/lectures-2025-26/lecture-16#^def-2-5-1|continuous at the point]] $y_0$. $\square$
>
> **Proof of [[#^thm-9-2-3|Theorem 9.2.3]].** The hypothesis of [[#^thm-9-2-1|Theorem 9.2.1]] holds at every point $y_0\in[c,d]$, so $I\in C([c,d])$; in particular, $I$ is integrable on $[c,d]$. Let $t\in[a,b)$. The function $f$ is continuous on the rectangle $[a,t]\times[c,d]$, and by [[#^thm-9-1-3|Theorem 9.1.3]]
> $$
> \int_a^t\left(\int_c^df(x,y)\,dy\right)dx=\int_c^d\left(\int_a^tf(x,y)\,dx\right)dy=\int_c^dI_t(y)\,dy .
> $$
> Let $\varepsilon>0$ and let $b_0$ be from [[#^def-9-2-1|Definition 9.2.1]]. For $t\in(b_0,b)$
> $$
> \left|\int_c^dI(y)\,dy-\int_a^t\left(\int_c^df(x,y)\,dy\right)dx\right|=\left|\int_c^d\bigl(I(y)-I_t(y)\bigr)dy\right|\le\int_c^d\left|\int_t^bf(x,y)\,dx\right|dy\le\varepsilon(d-c) .
> $$
> Consequently $\lim_{t\to b}\int_a^t\left(\int_c^df(x,y)\,dy\right)dx=\int_c^dI(y)\,dy$: the improper integral on the right-hand side converges, and the equality is proved. $\square$
>
> **Proof of [[#^thm-9-2-2|Theorem 9.2.2]].** For $t\in[a,b)$ put
> $$
> I_t(y)=\int_a^tf(x,y)\,dx,\qquad J_t(y)=\int_a^tf'_y(x,y)\,dx,\qquad J(y)=\int_a^bf'_y(x,y)\,dx .
> $$
> The functions $f$ and $f'_y$ are continuous on the rectangle $[a,t]\times[c,d]$, so by [[en/lectures-2025-26/lecture-75-76#^thm-9-1-2|Theorem 9.1.2]] $I_t\in C^1([c,d])$ and $I_t'=J_t$, and by the [[en/lectures-2025-26/lecture-43-44#^thm-4-3-2|Newton–Leibniz formula]]
> $$
> I_t(y)=I_t(y_0)+\int_{y_0}^{y}J_t(s)\,ds,\qquad y\in[c,d].\qquad(*)
> $$
> *Uniform convergence of $I$.* Let $\varepsilon>0$. Since the integral $I(y_0)$ converges and $\int_a^bf'_y(x,y)\,dx$ converges uniformly on $[c,d]$, by the Bolzano–Cauchy criterion there is $b_0\in[a,b)$ such that for all $t_1,t_2\in(b_0,b)$ and $s\in[c,d]$
> $$
> \left|\int_{t_1}^{t_2}f(x,y_0)\,dx\right|<\varepsilon,\qquad\left|\int_{t_1}^{t_2}f'_y(x,s)\,dx\right|<\varepsilon .
> $$
> Subtracting the equalities $(*)$ for $t=t_2$ and $t=t_1$, we get for all $y\in[c,d]$
> $$
> \left|\int_{t_1}^{t_2}f(x,y)\,dx\right|\le\left|\int_{t_1}^{t_2}f(x,y_0)\,dx\right|+\left|\int_{y_0}^{y}\left(\int_{t_1}^{t_2}f'_y(x,s)\,dx\right)ds\right|<\varepsilon+\varepsilon|y-y_0|\le\varepsilon(1+d-c) .
> $$
> By the Bolzano–Cauchy criterion $I(y)$ converges uniformly on $[c,d]$.
>
> *The formula for the derivative.* By [[#^thm-9-2-1|Theorem 9.2.1]] (applied to $f'_y$) the function $J$ is continuous on $[c,d]$. Since $J_t\rightrightarrows J$ on $[c,d]$ as $t\to b$,
> $$
> \left|\int_{y_0}^{y}J_t(s)\,ds-\int_{y_0}^{y}J(s)\,ds\right|\le(d-c)\sup_{s\in[c,d]}|J_t(s)-J(s)|\to0\qquad(t\to b) .
> $$
> Passing to the limit in $(*)$ as $t\to b$, we get $I(y)=I(y_0)+\int_{y_0}^{y}J(s)\,ds$ for all $y\in[c,d]$. The integral of the continuous function $J$ with a variable upper limit is differentiable (Barrow's theorem), so $I$ is differentiable on $[c,d]$ and $I'(y)=J(y)=\int_a^bf'_y(x,y)\,dx$. $\square$

### Feynman's method

[[#^thm-9-2-2|Theorem 9.2.2]] underlies the idea of computing integrals by passing to an integral with a parameter — Feynman's method: the integral is embedded in a family of integrals depending on a parameter and differentiated with respect to the parameter under the integral sign.

**Example.** Let us compute
$$
\int_0^\infty\frac{e^{-x}-e^{-2x}}{x}\,dx .
$$
Consider
$$
I(\alpha)=\int_0^\infty\frac{e^{-x}-e^{-\alpha x}}{x}\,dx ,\qquad\alpha\in Y=[1,2] ;
$$
the required integral equals $I(2)$, and $I(1)=0$. The integrand $f(x,\alpha)=\frac{e^{-x}-e^{-\alpha x}}{x}$ has the finite limit $\alpha-1$ as $x\to0$; setting $f(0,\alpha)=\alpha-1$, we get a function continuous on $[0,+\infty)\times[1,2]$ together with its derivative
$$
\frac{\partial f}{\partial\alpha}(x,\alpha)=e^{-\alpha x}
$$
(for $x=0$ both formulas give $1$). Let us check the hypotheses of [[#^thm-9-2-2|Theorem 9.2.2]]:

1. $f$ and $\frac{\partial f}{\partial\alpha}$ are continuous on $[0,+\infty)\times[1,2]$;
2. the integral $\int_0^\infty e^{-\alpha x}\,dx$ converges uniformly on $[1,2]$ by the Weierstrass test: $0<e^{-\alpha x}\le e^{-x}$ for $x\ge0$, $\alpha\ge1$, and $\int_0^\infty e^{-x}\,dx=1$ converges;
3. the integral $I(1)=0$ converges.

Consequently, for $\alpha\in[1,2]$
$$
I'(\alpha)=\int_0^\infty\frac{\partial f}{\partial\alpha}\,dx=\int_0^\infty e^{-\alpha x}\,dx=\frac{e^{-\alpha x}}{-\alpha}\Big|_0^{\infty}=\frac1\alpha ,
$$
whence $I(\alpha)=\int\frac{d\alpha}{\alpha}+C=\ln|\alpha|+C=\ln\alpha+C$. Since $I(1)=0$, we have $C=0$, and
$$
\int_0^\infty\frac{e^{-x}-e^{-2x}}{x}\,dx=I(2)=\ln2 .
$$

> [!info] Source correction
> (S313, T314, U315, T316, M317, T318, T529). In the notes the convergence of $I(\alpha)$ is checked by the splitting “$I_1+I_2(\alpha)$: $I_2(\alpha)=\int_0^\infty\frac{e^{\alpha x}}{x}\,dx$” with the estimate “$|f(\alpha,x)|\le\frac{e^{\alpha x}+e^{-x}}{x}\le\frac{?}{x}=g(x)$” and the claim “$\int_0^\infty\frac{e^{-x}}{x}\,dx$ — conv.”. This is wrong: $\frac{e^{-x}}{x}\sim\frac1x$ as $x\to0+$, so the integrals $\int_0^\infty\frac{e^{-x}}{x}\,dx$ and $\int_0^\infty\frac{e^{-\alpha x}}{x}\,dx$ diverge (besides, a minus sign is missing in the exponent $e^{\alpha x}$), and a majorant of the form $\frac{C}{x}$ is integrable neither near zero nor at infinity. There is no need to split the integral: the singularity at zero is removable, and condition 3 of [[#^thm-9-2-2|Theorem 9.2.2]] requires convergence at just one point ($I(1)=0$); the uniform convergence of $I(\alpha)$ on $[1,2]$ is already a conclusion of the theorem. The lines “$I_2e^{-x}\,dx=e^{-\alpha x}\,dx$” and “$\int_0^\infty e^{-x}\,dx<\int_0^\infty e^{-x}\,dx\Rightarrow$ is uniform conv.” are read as the majorant $e^{-\alpha x}\le e^{-x}$ ($\alpha\ge1$) and the convergence of $\int_0^\infty e^{-x}\,dx$, which give the uniform convergence of the integral of $\frac{\partial f}{\partial\alpha}$ (condition 2). Finally, the notes have “$\frac{df}{d\alpha}=-e^{-\alpha x}$”; correct is $\frac{\partial f}{\partial\alpha}=+e^{-\alpha x}$ (the next line of the notes uses exactly $\int_0^\infty e^{-\alpha x}\,dx=\frac1\alpha$).

**Exercise (Feynman's method).** Compute explicitly
$$
I(a)=\int_0^{\infty}\frac{dx}{(a^2+x^2)^2},\qquad a>0 ,
$$
using the integral
$$
\int_0^{+\infty}\frac{dx}{a^2+x^2}=\frac1a\arctan\frac xa\,\Big|_0^{+\infty}=\frac{\pi}{2a} .
$$
Idea: $\left(\frac1{a^2+x^2}\right)'_a=-\frac{2a}{(a^2+x^2)^2}$, and differentiation with respect to the parameter under the integral sign is allowed for $a\in[a_0,+\infty)$, $a_0>0$.

> [!info] Source correction
> (U319, T320, S321). The notes say: “$\int_0^\infty\frac{dx}{(a+x^2)^2}=I(a)$ — derive the closed form”, “$\left(\frac1{a+x^2}\right)'_a=2a-\frac1{(a+x^2)^2}$”, “$\alpha\in[0,+\infty)$, $a_0>0$: idea”, “Using $\int_0^{+\infty}\frac{dx}{a^2+x^2}$”. Since the reference integral contains $a^2$ (and the factor $2a$ appears when $\frac1{a^2+x^2}$ is differentiated), the exercise has $(a^2+x^2)^2$, and the derivative equals $-\frac{2a}{(a^2+x^2)^2}$; the parameter is $a\in[a_0,+\infty)$, $a_0>0$ (for $a=0$ the integral diverges).

> [!note] Restored
> (solution of the exercise; in the notes the exercise is only posed). Let $0<a_0<a_1$. On $[0,+\infty)\times[a_0,a_1]$ the functions $\frac1{a^2+x^2}$ and $-\frac{2a}{(a^2+x^2)^2}$ are continuous, and since $(a^2+x^2)^2\ge a^2(a^2+x^2)$,
> $$
> \frac{2a}{(a^2+x^2)^2}\le\frac{2}{a(a^2+x^2)}\le\frac{2}{a_0(a_0^2+x^2)},\qquad\int_0^\infty\frac{2\,dx}{a_0(a_0^2+x^2)}=\frac{\pi}{a_0^2}<\infty ,
> $$
> the integral of the derivative converges uniformly on $[a_0,a_1]$ (Weierstrass test). By [[#^thm-9-2-2|Theorem 9.2.2]]
> $$
> -\frac{\pi}{2a^2}=\left(\frac{\pi}{2a}\right)'=\int_0^\infty\left(\frac1{a^2+x^2}\right)'_a\,dx=-2a\int_0^\infty\frac{dx}{(a^2+x^2)^2}=-2a\,I(a),
> $$
> whence $I(a)=\frac{\pi}{4a^3}$ for all $a>0$ (since $a_0$ and $a_1$ are arbitrary). Check: for $a=1$ the substitution $x=\tan u$ gives $\int_0^{\pi/2}\cos^2u\,du=\frac{\pi}4$.

## Cross-references

- Course topic: [[en/09-improper-integrals-applications|chapter 9 “Improper integrals and applications”]] — [[en/09-improper-integrals-applications#9.1 Definitions|§9.1 “Definitions”]], [[en/09-improper-integrals-applications#9.2 Convergence tests|§9.2 “Convergence tests”]], [[en/09-improper-integrals-applications#^dirichlet-test-for-integrals|the Dirichlet test for integrals]]; changing the order of integration (cf. [[#^thm-9-1-3|Theorem 9.1.3]]) — [[en/17-multiple-integrals#^fubini-theorem-continuous|Fubini's theorem for continuous functions]] in chapter 17.
- The beginning of chapter 9 ([[en/lectures-2025-26/lecture-75-76#^def-9-1-1|Definition 9.1.1]], [[en/lectures-2025-26/lecture-75-76#^thm-9-1-1|Theorems 9.1.1]] and [[en/lectures-2025-26/lecture-75-76#^thm-9-1-2|9.1.2]], the beginning of the example with Bessel's equation): [[en/lectures-2025-26/lecture-75-76|lectures 75–76]].
- Uniform convergence of functional sequences and series, the Bolzano–Cauchy criterion and the Weierstrass test for series — [[en/lectures-2025-26/lecture-71-72|lectures 71–72]]; Abel's test for the uniform convergence of series — [[en/lectures-2025-26/lecture-73-74|lectures 73–74]].
- Facts used: the second mean value theorem — [[en/lectures-2025-26/lecture-45-46#^thm-4-4-3|Theorem 4.4.3]] (Bonnet), [[en/lectures-2025-26/lecture-45-46|lectures 45–46]]; the Dirichlet and Abel tests for improper integrals without a parameter — [[en/lectures-2025-26/lecture-49-50#^thm-4-5-4|Theorems 4.5.4]] and [[en/lectures-2025-26/lecture-49-50#^thm-4-5-5|4.5.5]], [[en/lectures-2025-26/lecture-49-50|lectures 49–50]].
- Continuation of chapter 9 (the gamma and beta functions) and the beginning of chapter 10: [[en/lectures-2025-26/lecture-79-80|lectures 79–80]].

---

[[en/lectures-2025-26/lecture-75-76|← Lectures 75–76]] · [[en/lectures-2025-26/index|Lecture index]] · [[en/lectures-2025-26/lecture-79-80|Lectures 79–80 →]] · [[en/term-index|Terms & theorems]] · [[ru/lectures-2025-26/lecture-77-78|Русский]] · [[es/lectures-2025-26/lecture-77-78|Español]]

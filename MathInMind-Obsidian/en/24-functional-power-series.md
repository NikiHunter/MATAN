---
title: "Functional and Power Series"
lang: en
chapter: 24
part: "Semester 3: the lecturer's chapters"
numbering: lecture
lecturer_chapter: 8
aliases: ["Functional and Power Series (en)"]
tags: [mathinmind/en, mathinmind/chapter]
---
# 24. Functional and Power Series

[[en/23-numerical-series|← 23. Numerical Series]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]] · [[en/25-parameter-integrals|25. Integrals Depending on a Parameter →]]

> [!abstract] Goal
> Present the lecturer's chapter 8 (§8.1–§8.4, [[en/lectures-2025-26/lecture-71-72|lectures 71–72]], [[en/lectures-2025-26/lecture-73-74|73–74]] and [[en/lectures-2025-26/lecture-75-76|75–76]]), keeping the lecturer's numbering: pointwise and [[en/10-function-sequences-series#10.1 Two modes of convergence|uniform convergence]], passing continuity, integration and differentiation to the limit, functional series and the [[en/10-function-sequences-series#^weierstrass-m-test|Weierstrass test]], [[en/11-power-series#11.1 Radius of convergence|power series]], the [[en/11-power-series#11.3 Standard expansions|Taylor series]] and [[en/11-power-series#11.4 Analytic does not mean merely smooth|analytic functions]]. A condensed treatment of the same topics is in chapters [[en/10-function-sequences-series|10]] and [[en/11-power-series|11]].

## §8.1. Uniform convergence

Let $X$ be a set, $f_n,f:X\to\mathbb R$, $n\in\mathbb N$.

> [!definition] Definition 8.1.1
> We say that the sequence $(f_n)$ converges on $X$ to $f$ pointwise if for each $x\in X$ the numerical sequence $a_n:=f_n(x)$ converges to the number $a:=f(x)$ as $n\to\infty$.

^def-8-1-1

> [!definition] Definition 8.1.2
> $f_n\to f$ uniformly on the set $E\subset X$ if
> $$
> \forall\varepsilon>0\ \ \exists N=N(\varepsilon)\ \ \forall x\in E\ \ \forall n>N:\quad |f_n(x)-f(x)|<\varepsilon .
> $$

^def-8-1-2

The difference from pointwise convergence lies in the order of the [[en/01-logic-sets-functions#1.1 Propositions and quantifiers|quantifiers]]: for pointwise convergence the index $N$ may depend on $x$, for uniform convergence one index works for all $x\in E$. Geometrically: for $n>N$ the graph of $f_n$ lies entirely in the "$\varepsilon$-tube" around the graph of $f$.

> [!definition] Definition 8.1.3
> The quantity
> $$
> \rho(f,g)=\sup_{x\in X}|f(x)-g(x)|
> $$
> is called the uniform (Chebyshev) deviation of the functions $f$ and $g$.

^def-8-1-3

> [!definition] Definition 8.1.4
> $f_n\rightrightarrows f$ if for every $\varepsilon>0$ there is $N$ such that $\rho(f_n,f)<\varepsilon$ for all $n>N$.

^def-8-1-4

Thus $f_n\rightrightarrows f$ is equivalent to $\rho(f_n,f)\to0$. Example: $f_n(x)=x^n$ on $[0,1]$ converges pointwise to the function equal to $0$ on $[0,1)$ and to $1$ at the point $1$; here $\rho(f_n,f)=\sup_{[0,1)}x^n=1$, and the convergence is not uniform, while on $[0,q]$ with $q<1$ we have $\rho(f_n,0)=q^n\to0$.

## §8.2. Uniform convergence and properties of limit functions

> [!theorem] Theorem 8.2.1 (continuity of the limit function)
> Let
> 1. $f_n\in C([a,b])$ for all $n$;
> 2. $f_n\rightrightarrows f$ on $[a,b]$.
>
> Then $f\in C([a,b])$.

^thm-8-2-1

*Proof idea* ("$\varepsilon/3$"): $|f(x)-f(x_0)|\le|f(x)-f_n(x)|+|f_n(x)-f_n(x_0)|+|f_n(x_0)-f(x_0)|$, where the outer terms are small uniformly in $x$ for a large fixed $n$, and the middle one is small by the continuity of $f_n$. Corollary: $\lim_{x\to x_0}\lim_{n\to\infty}f_n(x)=\lim_{n\to\infty}\lim_{x\to x_0}f_n(x)$.

> [!theorem] Theorem 8.2.2 (passage to the limit under the integral sign)
> Let
> 1. $f_n\in C([a,b])$ for all $n$;
> 2. $f_n\rightrightarrows f$ on $[a,b]$.
>
> Then
> $$
> \lim_{n\to\infty}\int_a^bf_n(x)\,dx=\int_a^b\Bigl(\lim_{n\to\infty}f_n(x)\Bigr)dx .
> $$

^thm-8-2-2

The proof is the estimate $\bigl|\int_a^bf_n-\int_a^bf\bigr|\le(b-a)\,\rho(f_n,f)$. Pointwise convergence alone is not enough: the "spikes" $f_n$, triangles over $[0,\frac1n]$ of height $n$, tend to zero at every point, but $\int_0^1f_n=\frac12$.

> [!theorem] Theorem 8.2.3 (differentiation of the limit function)
> Let
> 1. $f_n\in C^1([a,b])$ for all $n$;
> 2. $f_n\to f$ (pointwise on $[a,b]$) as $n\to\infty$;
> 3. $f\in C^1([a,b])$;
> 4. $f_n'\rightrightarrows\varphi$ on $[a,b]$.
>
> Then $\varphi\in C([a,b])$ and $f'=\varphi$, i.e.
> $$
> \frac{d}{dx}\Bigl(\lim_{n\to\infty}f_n(x)\Bigr)=\lim_{n\to\infty}\Bigl(\frac{d}{dx}f_n(x)\Bigr).
> $$

^thm-8-2-3

*Proof idea.* Passing to the limit in the equality $f_n(x)=f_n(a)+\int_a^xf_n'(t)\,dt$ by [[#^thm-8-2-2|theorem 8.2.2]] we get $f(x)=f(a)+\int_a^x\varphi(t)\,dt$, and it remains to differentiate an [[en/08-riemann-integration#8.3 Fundamental theorem of calculus|integral with a variable upper limit]]. Condition 3 follows from the other conditions (as the lecture notes also point out): it can be moved to the conclusion.

## §8.3. Functional series

> [!definition] Definition 8.3.1
> Let a sequence of functions $u_n:X\to\mathbb R$, $n\in\mathbb N$ be given. The expression $\sum_{n=1}^{\infty}u_n(x)$ is called a functional series. Put
> $$
> S_n(x)=\sum_{k=1}^{n}u_k(x),\qquad S(x)=\lim_{n\to\infty}S_n(x),\qquad S:X\to\mathbb R .
> $$
> A functional series is called convergent on the set $X$ if it converges at every point of this set.

^def-8-3-1

> [!definition] Definition 8.3.2
> The series $\sum_{n=1}^{\infty}u_n(x)$ is called uniformly convergent on the set $E\subset X$ if $S_n\rightrightarrows S$ on $E$.

^def-8-3-2

> [!theorem] Bolzano–Cauchy criterion for uniform convergence
> The series $\sum_{n=1}^{\infty}u_n(x)$ converges uniformly on $E$ if and only if
> $$
> \forall\varepsilon>0\ \exists N\ \forall n>N\ \forall p\in\mathbb N\ \forall x\in E\qquad\Bigl|\sum_{k=n+1}^{n+p}u_k(x)\Bigr|<\varepsilon .
> $$

> [!theorem] Weierstrass test
> Let $|u_n(x)|\le C_n$ for all $x\in E$ and all $n$, and let the [[en/04-numeric-series#4.1 Convergence through partial sums|numerical series]] $\sum_{n=1}^{\infty}C_n$ converge. Then the series $\sum_{n=1}^{\infty}u_n(x)$ converges on $E$ uniformly (and absolutely).

Uniform and [[en/04-numeric-series#4.3 Absolute and conditional convergence|absolute convergence]] do not imply each other: the series $\sum\frac{(-1)^{n}}{n}$ (with constant terms) converges uniformly but not absolutely, while the series $\sum_{n=0}^{\infty}x^n$ on $[0,1)$ converges absolutely but not uniformly.

> [!theorem] Theorem 8.3.1
> Let a series of functions $u_n\in C([a,b])$, $n\in\mathbb N$, be given, and $\sum_{n=1}^{\infty}u_n(x)=S(x)$. If the series $\sum_{n=1}^{\infty}u_n(x)$ converges uniformly on $[a,b]$, then $S\in C([a,b])$.

^thm-8-3-1

> [!theorem] Theorem 8.3.2 (termwise integration)
> Let $u_n\in C([a,b])$ for all $n\in\mathbb N$ and $\sum_{n=1}^{\infty}u_n(x)=S(x)$. If the series $\sum_{n=1}^{\infty}u_n(x)$ converges uniformly on $[a,b]$, then
> $$
> \int_a^b S(x)\,dx=\sum_{n=1}^{\infty}\int_a^b u_n(x)\,dx .
> $$

^thm-8-3-2

> [!theorem] Theorem 8.3.3 (termwise differentiation)
> Let $u_n\in C^1([a,b])$ for all $n\in\mathbb N$ and $\sum_{n=1}^{\infty}u_n(x)=S(x)$. If the series $\sum_{n=1}^{\infty}u_n(x)$ converges at every point of $[a,b]$ and the series $\sum_{n=1}^{\infty}u_n'(x)$ converges uniformly on $[a,b]$, then $S\in C^1([a,b])$ and
> $$
> \Bigl(\sum_{n=1}^{\infty}u_n(x)\Bigr)'=\sum_{n=1}^{\infty}u_n'(x),\qquad x\in[a,b].
> $$

^thm-8-3-3

[[#^thm-8-3-1|Theorems 8.3.1]]–[[#^thm-8-3-3|8.3.3]] are [[#^thm-8-2-1|theorems 8.2.1]]–[[#^thm-8-2-3|8.2.3]] applied to the partial sums $S_n$.

## §8.4. Power series

> [!definition] Definition 8.4.1
> A series of the form
> $$
> \sum_{k=0}^{\infty}c_k(x-a)^k,\qquad\qquad(8.4.1)
> $$
> where $c_k,x,a\in\mathbb R$, is called a (real) power series; the numbers $c_k$ are called its coefficients, and $a$ its centre.

^def-8-4-1

> [!definition] Definition 8.4.2
> A quantity $R\in[0,+\infty]$ is called the radius of convergence of the series $\sum_{k=0}^{\infty}c_k(x-a)^k$ if
> 1. for all $x$ with $|x-a|<R$ the series converges;
> 2. for all $x$ with $|x-a|>R$ the series diverges.

^def-8-4-2

The interval $(a-R,a+R)$ is called the interval of convergence; at its endpoints both convergence and divergence are possible.

> [!theorem] Theorem 8.4.1 (Cauchy–Hadamard formula)
> Every power series $\sum_{k=0}^{\infty}c_k(x-a)^k$ has a radius of convergence, and it is given by the formula
> $$
> R=\frac{1}{\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}} .
> $$

^thm-8-4-1

Here $\frac10=+\infty$, $\frac1{+\infty}=0$. The proof is Cauchy's test for the series $\sum|c_k(x-a)^k|$ in its upper-limit form. If $\lim_{n\to\infty}\bigl|\frac{c_n}{c_{n+1}}\bigr|$ exists, it equals $R$ ([[en/04-numeric-series#4.2 Nonnegative terms|d'Alembert's test]]).

> [!remark] Remark 8.4.1
> By Cauchy's test, for $|x-a|<R$ the series $\sum_{k=0}^{\infty}c_k(x-a)^k$ converges absolutely.

^rem-8-4-1

> [!remark] Remark 8.4.2
> The substitution $x-a=y$ turns series (8.4.1) into the power series $\sum_{k=0}^{\infty}c_ky^k$ centred at zero, so when deriving properties of power series one may assume $a=0$.

^rem-8-4-2

> [!theorem] Theorem 8.4.2 (uniform convergence of power series)
> Let $R\in(0,+\infty]$ be the radius of convergence of the power series $\sum_{k=0}^{\infty}c_k(x-a)^k$. Then for every $r\in(0,R)$ the power series converges uniformly on the segment $[a-r,a+r]$.

^thm-8-4-2

The proof is the Weierstrass test with $C_k=|c_k|r^k$ (the series $\sum|c_k|r^k$ converges by [[#^rem-8-4-1|remark 8.4.1]]). On the whole interval of convergence there may be no uniform convergence: $\sum x^k$ on $(-1,1)$.

> [!theorem] Theorem 8.4.3 (Abel's theorem on power series)
> Let $R\in(0,+\infty)$ be the radius of convergence of the power series $\sum_{k=0}^{\infty}c_k(x-a)^k$. If the power series converges at $x=a+R$ (respectively at $x=a-R$), then it converges uniformly on the segment $[a,a+R]$ (respectively on $[a-R,a]$), and its sum is [[en/05-limits-continuity#5.3 Continuity|continuous at the point]] $a+R$ from the left (respectively at the point $a-R$ from the right).

^thm-8-4-3

The proof relies on **Abel's test for uniform convergence**: if the series $\sum f_k(x)$ converges uniformly on $X$, and for each $x$ the sequence $(g_k(x))$ is monotone, with $|g_k(x)|\le M$ for all $k$ and $x\in X$, then the series $\sum f_k(x)g_k(x)$ converges uniformly on $X$. Here $f_k=c_kR^k$ (a convergent numerical series), $g_k(x)=\bigl(\frac{x-a}{R}\bigr)^k$, $x\in[a,a+R]$.

> [!theorem] Theorem 8.4.4 (integration of power series)
> Let $R\in(0,+\infty]$ be the radius of convergence of the power series $\sum_{k=0}^{\infty}c_k(x-a)^k$. If $[A,B]\subset(a-R,a+R)$, then
> $$
> \int_A^B\sum_{k=0}^{\infty}c_k(x-a)^k\,dx=\sum_{k=0}^{\infty}c_k\,\frac{(B-a)^{k+1}-(A-a)^{k+1}}{k+1}.\qquad\qquad(8.4.2)
> $$
> If, moreover, $R<+\infty$ and the series converges at $x=a+R$ (respectively at $x=a-R$), then equality (8.4.2) also holds for $B=a+R$ (respectively for $A=a-R$).

^thm-8-4-4

> [!theorem] Theorem 8.4.5 (radii of power series)
> The radii of convergence of the power series
> $$
> \sum_{k=0}^{\infty}c_k(x-a)^k,\qquad \sum_{k=1}^{\infty}kc_k(x-a)^{k-1},\qquad \sum_{k=0}^{\infty}\frac{c_k}{k+1}(x-a)^{k+1}
> $$
> are equal.

^thm-8-4-5

This follows from the Cauchy–Hadamard formula, since $\sqrt[k]{k}\to1$ and $\sqrt[k]{k+1}\to1$.

> [!theorem] Theorem 8.4.6 (differentiation of power series)
> Let $R\in(0,+\infty]$ be the radius of convergence of the series $f(x)=\sum_{k=0}^{\infty}c_k(x-a)^k$. Then $f$ is infinitely [[en/06-derivatives#6.1 Definition and linear approximation|differentiable]] on the interval $|x-a|<R$, and the series can be differentiated termwise any number of times:
> $$
> f^{(m)}(x)=\sum_{k=m}^{\infty}k(k-1)\dots(k-m+1)\,c_k(x-a)^{k-m},\qquad |x-a|<R,\quad m\in\mathbb N .
> $$

^thm-8-4-6

> [!theorem] Theorem 8.4.7 (uniqueness of the expansion of a function in a power series)
> Let $R\in(0,+\infty]$ be the radius of convergence of the series $f(x)=\sum_{k=0}^{\infty}c_k(x-a)^k$. Then $f\in C^\infty(a-R,a+R)$, and the coefficients are uniquely determined:
> $$
> c_k=\frac{f^{(k)}(a)}{k!} .
> $$

^thm-8-4-7

Substitute $x=a$ into the formula of [[#^thm-8-4-6|theorem 8.4.6]]: all terms with $k>m$ vanish, and $f^{(m)}(a)=m!\,c_m$.

> [!definition] Definition 8.4.3
> Let $f$ have derivatives of all orders at the point $a$. The numbers $c_k=\frac{f^{(k)}(a)}{k!}$ are called the Taylor coefficients, and the series
> $$
> \sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k
> $$
> is called the Taylor series of the function $f$ centred at the point $a$. The Taylor series centred at zero is called the [[en/07-taylor-convexity#7.3 Taylor's formula|Maclaurin series]].

^def-8-4-3

> [!theorem] Theorem 8.4.8 (a test for the expandability of a function in a Taylor series)
> Let $f\in C^\infty(A,B)$, $a,x\in(A,B)$, $a\ne x$, and suppose there is $M\in(0,\infty)$ such that $|f^{(n)}(t)|\le M$ for all $n\in\mathbb N$ and all $t$ lying between $a$ and $x$. Then
> $$
> \sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k=f(x).
> $$

^thm-8-4-8

The proof is the estimate of the Lagrange remainder: $|f(x)-T_{a,n}f(x)|\le\frac{M|x-a|^{n+1}}{(n+1)!}\to0$. This gives the expansions of $e^x$, $\sin x$, $\cos x$ on the whole line.

> [!definition] Definition 8.4.4
> Let $-\infty\le A<B\le+\infty$, $f:(A,B)\to\mathbb R$, $a\in(A,B)$. The function $f$ is called analytic at the point $a$ if there exist numbers $r>0$ and $c_k\in\mathbb R$ such that
> $$
> f(x)=\sum_{k=0}^{\infty}c_k(x-a)^k,\qquad x\in(a-r,a+r).
> $$
> A function is called analytic on $(A,B)$ if it is analytic at every point of $(A,B)$.

^def-8-4-4

By [[#^thm-8-4-6|theorems 8.4.6]] and [[#^thm-8-4-7|8.4.7]] an analytic function is infinitely differentiable, and its power series is its Taylor series. The converse is false: the function $e^{-1/x^2}$ (extended by zero at zero) has the zero Maclaurin series; the function $\sum_{n=0}^{\infty}e^{-\sqrt{2^n}}\cos(2^nx)$ from the lecture has a Taylor series at zero that diverges for all $x\ne0$.

## Worked example

**The series $\sum_{k=1}^{\infty}\frac{x^k}{k}$.** By the Cauchy–Hadamard formula $R=1$, since $\sqrt[k]{1/k}\to1$. On $(-1,1)$ termwise differentiation ([[#^thm-8-4-6|theorem 8.4.6]]) gives $f'(x)=\sum_{k=1}^{\infty}x^{k-1}=\frac{1}{1-x}$, and taking $f(0)=0$ into account,
$$
\sum_{k=1}^{\infty}\frac{x^k}{k}=-\ln(1-x),\qquad |x|<1 .
$$
At $x=1$ we get the harmonic series, which diverges. At $x=-1$ the series $\sum\frac{(-1)^k}{k}$ converges by the [[en/04-numeric-series#^alternating-series-test|Leibniz test]], so by [[en/11-power-series#^abel-theorem|Abel's theorem]] the sum is continuous at the point $-1$ from the right: $\sum_{k=1}^{\infty}\frac{(-1)^k}{k}=-\ln2$. The set of convergence is $[-1,1)$.

**Is the convergence uniform?** Let $f_n(x)=\frac{nx}{1+n^2x^2}$ on $[0,1]$. Pointwise $f_n\to0$, but $f_n\bigl(\frac1n\bigr)=\frac12$, so $\rho(f_n,0)\ge\frac12$, and the convergence is not uniform. On $[\delta,1]$ with $\delta>0$ we have $0\le f_n(x)\le\frac{1}{nx}\le\frac{1}{n\delta}\to0$, so the convergence is uniform.

## Common pitfalls

1. Assuming that a pointwise limit of continuous functions is continuous: $x^n$ on $[0,1]$.
2. Interchanging a limit and an integral without uniform convergence (the "spikes" example).
3. Differentiating a series termwise after checking uniform convergence of the series itself rather than of the series of derivatives: $\sum\frac{\sin(n^2x)}{n^2}$ converges uniformly, while the series of derivatives $\sum\cos(n^2x)$ diverges, for instance, at $x=0$.
4. Drawing conclusions about the endpoints of the interval from the radius: $\sum\frac{x^k}{k^2}$ converges at both endpoints, $\sum x^k$ at neither, $\sum\frac{x^k}{k}$ at one.
5. Treating every infinitely differentiable function as analytic ($e^{-1/x^2}$).

## Exercises

1. Find the radius and the set of convergence of the series $\sum_{k=1}^{\infty}\frac{(x-2)^k}{k\,3^k}$.
2. Does the sequence $f_n(x)=x^n(1-x)$ converge uniformly on $[0,1]$?
3. Prove that the function $\sum_{n=1}^{\infty}\frac{\sin nx}{n^2}$ is continuous on $\mathbb R$.
4. Expand $\operatorname{arctg}x$ into a Maclaurin series and find the sum $\sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1}$.

> [!answer]- Short answers
> 1. $R=3$; at $x=5$ the harmonic series (diverges), at $x=-1$ a Leibniz series (converges); the set of convergence is $[-1,5)$.
> 2. Yes: the maximum of $f_n$ is attained at $x=\frac{n}{n+1}$ and does not exceed $\frac{1}{n+1}\to0$.
> 3. The Weierstrass test with $C_n=\frac1{n^2}$ and [[#^thm-8-3-1|theorem 8.3.1]] on every segment $[a,b]$.
> 4. Termwise integration of the series $\frac1{1+t^2}=\sum_{k=0}^{\infty}(-1)^kt^{2k}$ over $[0,x]$ ([[#^thm-8-4-4|theorem 8.4.4]]) gives $\operatorname{arctg}x=\sum_{k=0}^{\infty}\frac{(-1)^kx^{2k+1}}{2k+1}$ for $|x|<1$; at $x=1$ the series converges, and by Abel's theorem its sum equals $\frac\pi4$.

---

[[en/23-numerical-series|← 23. Numerical Series]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]] · [[en/25-parameter-integrals|25. Integrals Depending on a Parameter →]]

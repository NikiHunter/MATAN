---
title: "Integrals Depending on a Parameter"
lang: en
chapter: 25
part: "Semester 3: the lecturer's chapters"
numbering: lecture
lecturer_chapter: 9
aliases: ["Integrals Depending on a Parameter (en)"]
tags: [mathinmind/en, mathinmind/chapter]
---
# 25. Integrals Depending on a Parameter

[[en/24-functional-power-series|← 24. Functional and Power Series]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]] · [[en/26-multiple-riemann-integral|26. The Multiple Riemann Integral →]]

> [!abstract] Goal
> Present the lecturer's chapter 9 (§9.1–§9.3, [[en/lectures-2025-26/lecture-75-76|lectures 75–76]], [[en/lectures-2025-26/lecture-77-78|77–78]] and [[en/lectures-2025-26/lecture-79-80|79–80]]), keeping the lecturer's numbering: continuity, differentiation and integration of proper and [[en/09-improper-integrals-applications#9.1 Definitions|improper integrals]] with respect to a parameter, [[#^def-9-2-1|uniform convergence of an improper integral]] and its tests, the gamma and [[#§9.3. The gamma function|beta functions]]. Related topics of the course: improper integrals in [[en/09-improper-integrals-applications|chapter 9]], [[en/10-function-sequences-series#10.1 Two modes of convergence|uniform convergence]] of series in [[en/10-function-sequences-series|chapter 10]], changing the order of integration in [[en/17-multiple-integrals|chapter 17]].

## §9.1. Proper integrals depending on a parameter

> [!definition] Definition 9.1.1
> An integral depending on a parameter is a function of the form
> $$
> I(y)=\int_{E_y}f(x,y)\,dx ,
> $$
> where $y$ plays the role of a parameter ranging over a set $Y$.

^def-9-1-1

The main questions are whether $I$ is continuous and whether one may differentiate and integrate with respect to $y$ under the integral sign. The lecturer's example: for $I(y)=\int_0^{+\infty}e^{-xy}\frac{\sin x}{x}\,dx$ formal differentiation gives $I'(y)=-\int_0^{+\infty}e^{-xy}\sin x\,dx=-\frac{1}{1+y^2}$, whence $I(0)=\int_0^{+\infty}\frac{\sin x}{x}\,dx=\frac\pi2$; justifying these steps is the aim of §9.2 (see the worked example below). Throughout §9.1
$$
P=\{(x,y)\in\mathbb R^2:\ a\le x\le b,\ c\le y\le d\},\qquad I(y)=\int_a^bf(x,y)\,dx .
$$

> [!theorem] Theorem 9.1.1
> Let $f\in C(P)$. Then the function $I(y)=\int_a^bf(x,y)\,dx$ is continuous at every point $y\in[c,d]$, i.e. $I\in C([c,d])$.

^thm-9-1-1

The proof is the [[en/05-limits-continuity#5.4 Uniform continuity|uniform continuity]] of $f$ on the [[en/13-metric-spaces#13.4 Compactness|compact]] set $P$ (Cantor's theorem): $|I(y)-I(y_0)|\le\int_a^b|f(x,y)-f(x,y_0)|\,dx<\varepsilon(b-a)$ for $|y-y_0|<\delta$.

> [!theorem] Theorem 9.1.2
> Let $f\in C(P)$ and $\frac{\partial f}{\partial y}\in C(P)$. Then $I\in C^1([c,d])$ and
> $$
> I'(y)=\int_a^b\frac{\partial f}{\partial y}(x,y)\,dx .
> $$

^thm-9-1-2

This is Leibniz's formula (rule). By [[en/07-taylor-convexity#^lagrange-mean-value-theorem|Lagrange's theorem]] the difference quotient $\frac{f(x,y+h)-f(x,y)}{h}=f'_y(x,y+\theta h)$ converges to $f'_y(x,y)$ uniformly in $x$ (uniform continuity again), and it remains to pass to the limit under the integral sign.

> [!theorem] Theorem 9.1.3
> Let $f\in C(P)$. Then $I$ is integrable on $[c,d]$ and
> $$
> \int_c^d\left(\int_a^bf(x,y)\,dx\right)dy=\int_a^b\left(\int_c^df(x,y)\,dy\right)dx .
> $$

^thm-9-1-3

*Proof idea.* Both sides, regarded as functions of the [[en/03-sequences#3.5 Limit superior and inferior|upper limit]] $t\in[c,d]$ in place of $d$, vanish at $t=c$ and have the same [[en/06-derivatives#6.1 Definition and linear approximation|derivative]] $\int_a^bf(x,t)\,dx$ (for the right-hand side by [[#^thm-9-1-2|theorem 9.1.2]]).

## §9.2. Improper integrals depending on a parameter

Let $-\infty<a<b\le+\infty$, let the function $f$ be defined on $[a,b)\times Y$, integrable for each $y\in Y$ on every segment $[a,b']\subset[a,b)$, and let the improper integral $I(y)=\int_a^bf(x,y)\,dx$ converge for each $y\in Y$. Put $I_{b'}(y)=\int_a^{b'}f(x,y)\,dx$.

> [!definition] Definition 9.2.1
> We say that $I(y)$ converges uniformly with respect to $y\in Y$ (uniformly on $Y$) if
> $$
> \forall\varepsilon>0\ \ \exists b_0\in[a,b)\ \ \forall b'\in(b_0,b)\ \ \forall y\in Y:\quad |I_{b'}(y)-I(y)|=\left|\int_{b'}^{b}f(x,y)\,dx\right|<\varepsilon .
> $$
> In other words, $I_{b'}(y)\rightrightarrows I(y)$ on $Y$ as $b'\to b$.

^def-9-2-1

> [!theorem] Bolzano–Cauchy criterion
> The integral $I(y)$ converges uniformly on $Y$ if and only if for every $\varepsilon>0$ there is $b_0\in[a,b)$ such that $\bigl|\int_{t_1}^{t_2}f(x,y)\,dx\bigr|<\varepsilon$ for all $t_1,t_2\in(b_0,b)$ and all $y\in Y$.

> [!theorem] Weierstrass test
> Suppose there is a function $\varphi:[a,b)\to[0,+\infty)$, integrable on every segment $[a,t]\subset[a,b)$, such that $|f(x,y)|\le\varphi(x)$ for all $x\in[a,b)$, $y\in Y$, and the integral $\int_a^b\varphi(x)\,dx$ converges. Then $I(y)$ converges uniformly on $Y$.

> [!theorem] Dirichlet test
> Let the functions $f$ and $g$ be defined on $[a,b)\times Y$ and continuous in $x$ for each $y$; for each $y$ let the function $f(\cdot,y)$ be monotone, and $\sup_{y\in Y}|f(x,y)|\to0$ as $x\to b$; let the [[en/08-riemann-integration#8.3 Fundamental theorem of calculus|antiderivatives]] $\int_a^tg(x,y)\,dx$ be uniformly bounded for $t\in[a,b)$, $y\in Y$. Then the integral $\int_a^bf(x,y)g(x,y)\,dx$ converges uniformly on $Y$.

> [!theorem] Abel test
> Let the functions $f$ and $g$ be defined on $[a,b)\times Y$ and continuous in $x$ for each $y$; for each $y$ let the function $f(\cdot,y)$ be monotone, and $|f(x,y)|\le M$ everywhere; let the integral $\int_a^bg(x,y)\,dx$ converge uniformly on $Y$. Then the integral $\int_a^bf(x,y)g(x,y)\,dx$ converges uniformly on $Y$.

The Dirichlet and Abel tests are proved with the [[en/08-riemann-integration#^mean-value-theorem-for-integrals|second mean value theorem]] (Bonnet) in the same way as the tests of the same name for series are proved with the [[en/23-numerical-series#§7.4. Series with terms of arbitrary sign|Abel transformation]]. Example: $\int_0^{\infty}\frac{\cos(\alpha x)}{1+x^2}\,dx$ converges uniformly in $\alpha\in\mathbb R$ by the [[en/10-function-sequences-series#^weierstrass-m-test|Weierstrass test]] with $\varphi(x)=\frac1{1+x^2}$.

> [!theorem] Theorem 9.2.1
> Let the function $f$ be continuous on $[a,b)\times[c,d]$, $y_0\in[c,d]$, and let the improper integral $I(y)=\int_a^bf(x,y)\,dx$ converge uniformly on $[c,d]\cap(y_0-\delta_0,y_0+\delta_0)$ for some $\delta_0>0$. Then the function $I$ is [[en/05-limits-continuity#5.3 Continuity|continuous at the point]] $y_0$. In particular, if $I(y)$ converges uniformly on $[c,d]$, then $I\in C([c,d])$.

^thm-9-2-1

> [!theorem] Theorem 9.2.2
> Let the functions $f(x,y)$ and $f'_y(x,y)$ be continuous on $[a,b)\times[c,d]$, let the integral $\int_a^bf'_y(x,y)\,dx$ converge uniformly on $[c,d]$, and let the integral $I(y)=\int_a^bf(x,y)\,dx$ converge for at least one value $y_0\in[c,d]$. Then $I(y)$ converges uniformly on the whole segment $[c,d]$, the function $I$ is differentiable on $[c,d]$, and
> $$
> I'(y)=\int_a^bf'_y(x,y)\,dx .
> $$

^thm-9-2-2

> [!theorem] Theorem 9.2.3
> Let the function $f(x,y)$ be continuous on $[a,b)\times[c,d]$, and let the integral $I(y)=\int_a^bf(x,y)\,dx$ converge uniformly on $[c,d]$. Then $I$ is integrable on $[c,d]$, the improper integral on the right converges, and
> $$
> \int_c^dI(y)\,dy=\int_a^b\left(\int_c^df(x,y)\,dy\right)dx .
> $$

^thm-9-2-3

All three theorems reduce to [[en/24-functional-power-series#^thm-8-2-1|theorems 8.2.1]]–[[en/24-functional-power-series#^thm-8-2-3|8.2.3]] on sequences of functions: $I_{b_n}\rightrightarrows I$ for every sequence $b_n\to b$, and the theorems of §9.1 apply to the proper integrals $I_{b_n}$.

**Feynman's method** is to embed an integral in a family and differentiate with respect to the parameter. For $I(\alpha)=\int_0^\infty\frac{e^{-x}-e^{-\alpha x}}{x}\,dx$, $\alpha\in[1,2]$, we have $I(1)=0$, and the integral $\int_0^\infty e^{-\alpha x}\,dx=\frac1\alpha$ of the derivative with respect to $\alpha$ converges uniformly (majorant $e^{-x}$). By [[#^thm-9-2-2|theorem 9.2.2]] $I'(\alpha)=\frac1\alpha$, so
$$
\int_0^\infty\frac{e^{-x}-e^{-2x}}{x}\,dx=I(2)=\ln2 .
$$

## §9.3. The gamma function

> [!definition] Definition 9.3.1
> The gamma function (at the point $y$) is the function given by the formula
> $$
> \Gamma(y)=\int_0^{\infty}x^{y-1}e^{-x}\,dx\qquad(y>0).
> $$

^def-9-3-1

The integral converges for $y>0$: near zero $x^{y-1}e^{-x}\sim\frac{1}{x^{1-y}}$, and at infinity $x^{y-1}e^{-x}=o\bigl(\frac1{x^2}\bigr)$. Properties of the [[#^def-9-3-1|gamma function]]:

1. $\Gamma(1)=1$, $\Gamma\bigl(\tfrac12\bigr)=\sqrt\pi$ (the substitution $x=t^2$ and the Euler–Poisson integral $\int_0^\infty e^{-t^2}\,dt=\frac{\sqrt\pi}2$).
2. $\Gamma(y+1)=y\,\Gamma(y)$ for $y>0$ ([[en/08-riemann-integration#8.4 Computation techniques|integration by parts]]); hence $\Gamma(n+1)=n!$ and $\Gamma\bigl(n+\tfrac12\bigr)=\frac{(2n-1)!!}{2^n}\sqrt\pi$ for $n\in\mathbb N$.
3. $\Gamma\in C^\infty(0,+\infty)$, and the derivatives are computed under the integral sign: $\Gamma''(y)=\int_0^{\infty}x^{y-1}e^{-x}\ln^2x\,dx>0$, i.e. $\Gamma$ is convex; $\Gamma(y)\to+\infty$ as $y\to0+$ and as $y\to+\infty$.
4. Stirling's formula: $\Gamma(y+1)\sim\sqrt{2\pi y}\,\frac{y^y}{e^y}$ as $y\to+\infty$; in particular, $n!\sim\sqrt{2\pi n}\,\frac{n^n}{e^n}$.
5. The reflection formula: $\Gamma(y)\,\Gamma(1-y)=\frac{\pi}{\sin(\pi y)}$ for $0<y<1$.
6. Euler's formula: $\frac{\Gamma(y)}{b^y}=\int_0^{\infty}u^{y-1}e^{-ub}\,du$ for $y>0$, $b>0$ (the substitution $x=bu$).

**The beta function** $B(y,z)=\int_0^1x^{y-1}(1-x)^{z-1}\,dx$ ($y,z>0$) is expressed through the gamma function:
$$
B(y,z)=\frac{\Gamma(y)\,\Gamma(z)}{\Gamma(y+z)} .
$$
The derivation uses Euler's formula for $\Gamma(y+z)$, a change of the order of integration and the substitution $b=\frac{x}{1-x}$.

## Worked example

**The Dirichlet integral.** Let $I(y)=\int_0^{+\infty}e^{-xy}\frac{\sin x}{x}\,dx$, $y\ge0$ (the integrand is extended by one at $x=0$ and is continuous).

1. *Uniform convergence on $[0,+\infty)$.* By the [[en/09-improper-integrals-applications#^dirichlet-test-for-integrals|Abel test]]: $\int_0^\infty\frac{\sin x}{x}\,dx$ converges (uniformly, since it does not depend on $y$), and $e^{-xy}$ is monotone in $x$ and does not exceed $1$. By [[#^thm-9-2-1|theorem 9.2.1]], $I$ is continuous on $[0,+\infty)$.
2. *The derivative for $y>0$.* For $y\ge y_0>0$ we have $|f'_y|=|e^{-xy}\sin x|\le e^{-xy_0}$, and by the Weierstrass test and [[#^thm-9-2-2|theorem 9.2.2]]
$$
I'(y)=-\int_0^{\infty}e^{-xy}\sin x\,dx=-\frac{1}{1+y^2},\qquad I(y)=C-\operatorname{arctg}y .
$$
3. *The constant.* $|I(y)|\le\int_0^\infty e^{-xy}\,dx=\frac1y\to0$ as $y\to+\infty$, hence $C=\frac\pi2$.
4. *Answer.* By continuity at zero, $\int_0^{+\infty}\frac{\sin x}{x}\,dx=I(0)=\frac\pi2$.

**The gamma function in computations.** With the substitution $t=x^2$:
$$
\int_0^\infty x^4e^{-x^2}\,dx=\frac12\int_0^\infty t^{3/2}e^{-t}\,dt=\frac12\,\Gamma\Bigl(\frac52\Bigr)=\frac12\cdot\frac34\sqrt\pi=\frac{3\sqrt\pi}{8}.
$$

## Common pitfalls

1. Differentiating an improper integral under the integral sign without checking the uniform convergence of the integral of $f'_y$.
2. Confusing convergence for each $y$ with uniform convergence: $\int_0^\infty ye^{-xy}\,dx=1$ for all $y>0$, but $\int_{b'}^\infty ye^{-xy}\,dx=e^{-b'y}$, and $\sup_{y\in(0,1]}e^{-b'y}=1$, so the convergence on $(0,1]$ is not uniform (and the limit function is discontinuous at zero on $[0,1]$).
3. Writing $\Gamma(n)=n!$ instead of $\Gamma(n)=(n-1)!$.
4. Applying the theorems of §9.1 when $f$ is continuous only in $x$ for each $y$: continuity on the whole rectangle $P$ is needed.
5. Forgetting that the integral defining $\Gamma(y)$ converges only for $y>0$.

## Exercises

1. Find $\lim_{y\to0}\int_0^1\sqrt{x^2+y^2}\,dx$.
2. Compute $\int_0^1\frac{x^b-x^a}{\ln x}\,dx$ for $0<a<b$.
3. Compute $\int_0^1x^2(1-x)^3\,dx$ using the beta function.
4. Prove that $\int_0^\infty e^{-x^2}\cos(xy)\,dx$ converges uniformly on $\mathbb R$.

> [!answer]- Short answers
> 1. $\frac12$: by [[#^thm-9-1-1|theorem 9.1.1]] the limit equals $\int_0^1x\,dx$.
> 2. $\ln\frac{b+1}{a+1}$: the integrand equals $\int_a^bx^y\,dy$, and by [[#^thm-9-1-3|theorem 9.1.3]] the order of integration can be changed: $\int_a^b\frac{dy}{y+1}$.
> 3. $B(3,4)=\frac{\Gamma(3)\Gamma(4)}{\Gamma(7)}=\frac{2\cdot6}{720}=\frac1{60}$.
> 4. The Weierstrass test with $\varphi(x)=e^{-x^2}$.

---

[[en/24-functional-power-series|← 24. Functional and Power Series]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]] · [[en/26-multiple-riemann-integral|26. The Multiple Riemann Integral →]]

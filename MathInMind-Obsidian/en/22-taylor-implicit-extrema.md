---
title: "Taylor's Formula in ℝⁿ, Implicit Maps, Extrema"
lang: en
chapter: 22
part: "Semester 3: the lecturer's chapters"
numbering: lecture
lecturer_chapter: 6
aliases: ["Taylor's Formula in ℝⁿ, Implicit Maps, Extrema (en)"]
tags: [mathinmind/en, mathinmind/chapter]
---
# 22. Taylor's Formula in ℝⁿ, Implicit Maps, Extrema

[[en/21-lp-spaces|← 21. Lᵖ Spaces and Modes of Convergence]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]] · [[en/23-numerical-series|23. Numerical Series →]]

> [!abstract] Goal
> Present the end of the lecturer's chapter 6 (§6.5–§6.7, [[en/lectures-2025-26/lecture-65-66|lectures 65–66]] and [[en/lectures-2025-26/lecture-67-68|67–68]]), keeping the lecturer's numbering: the multivariate [[#^def-6-5-1|Taylor formula]], the [[#^thm-6-6-1|implicit map theorem]], unconstrained and [[en/16-implicit-functions-extrema#16.4 Lagrange multipliers|constrained extrema]]. A shorter treatment of the same topics without the lecturer's numbering is in chapters [[en/15-multivariable-differentiation|15]] and [[en/16-implicit-functions-extrema|16]].

## §6.5. Taylor's formula

For a multi-index $\alpha=(\alpha_1,\ldots,\alpha_n)\in\mathbb Z_+^n$ put
$$
|\alpha|=\alpha_1+\ldots+\alpha_n,\qquad\alpha!=\alpha_1!\cdots\alpha_n!,\qquad h^\alpha=h_1^{\alpha_1}\cdots h_n^{\alpha_n},\qquad\partial^\alpha f=\frac{\partial^{|\alpha|}f}{\partial x_1^{\alpha_1}\cdots\partial x_n^{\alpha_n}}.
$$
A polynomial of degree at most $s$ in $n$ variables with values in $\mathbb R^m$ is $p(x)=\sum_{|\alpha|\le s}c_\alpha x^\alpha$, $c_\alpha\in\mathbb R^m$. We look for a polynomial that approximates $f$ near $a$ with accuracy
$$
f(x)=p(x)+o(\|x-a\|^s)\qquad(x\to a).\qquad(6.5.1)
$$

> [!definition] Definition 6.5.1
> Let $E\subset\mathbb R^n$, let $a$ be an [[en/13-metric-spaces#13.2 Open and closed sets|interior point]] of $E$, $f:E\to\mathbb R^m$, $s\in\mathbb Z_+$. A polynomial of degree at most $s$ satisfying condition (6.5.1) is called the Taylor polynomial of $f$ of order $s$ at the point $a$ and is denoted by $T_{a,s}f$.

^def-6-5-1

The Taylor polynomial, if it exists, is unique: the difference of two such polynomials is a polynomial of degree at most $s$ equal to $o(\|h\|^s)$, and such a polynomial is zero (substitute $h=te$, $t\to0$, homogeneous part by homogeneous part). For $s=0$ condition (6.5.1) is the continuity of $f$ at $a$, for $s=1$ it is differentiability.

> [!lemma] Lemma 6.5.1
> Let $E\subset\mathbb R^n$, let $a$ be an interior point of $E$, $s\in\mathbb N$, let the map $f:E\to\mathbb R^m$ be $s$ times differentiable at the point $a$, and let $f$ together with all its [[en/15-multivariable-differentiation#15.2 Partial and directional derivatives|partial derivatives]] of order at most $s$ vanish at the point $a$. Then $f(a+h)=o(\|h\|^s)$ as $h\to0$.

^lem-6-5-1

The proof is by [[en/01-logic-sets-functions#^example-induction|induction]] on $s$: the induction hypothesis is applied to the first-order partial derivatives, and the increment of $f$ is expressed through partial derivatives at intermediate points ([[en/lectures-2025-26/lecture-63-64#Printed slide 4 (PDF p. 4). Coordinate-increment lemma — Lemma 6.3.1|lemma 6.3.1]] on the increment along coordinates).

> [!theorem] Theorem 6.5.1 (Taylor–Peano formula)
> Let $E\subset\mathbb R^n$, let $a$ be an interior point of $E$, $s\in\mathbb N$, and let the map $f:E\to\mathbb R^m$ be $s$ times differentiable at the point $a$. Then
> $$
> f(x)=\sum_{|\alpha|\le s}\frac{\partial^\alpha f(a)}{\alpha!}(x-a)^\alpha+o(\|x-a\|^s)=\sum_{k=0}^{s}\frac{d_a^kf(x-a)}{k!}+o(\|x-a\|^s)\qquad(x\to a),
> $$
> i.e. the Taylor polynomial $T_{a,s}f$ exists and is given by the first sum.

^thm-6-5-1

*Proof idea.* The difference $g=f-T$, where $T$ is the sum on the right, is $s$ times differentiable at $a$, and all its partial derivatives of order at most $s$ at the point $a$ vanish (for a $s$ times [[en/15-multivariable-differentiation#15.1 The total derivative|differentiable map]], [[en/15-multivariable-differentiation#^clairaut-schwarz-theorem|mixed derivatives]] do not depend on the order); it remains to apply [[#^lem-6-5-1|lemma 6.5.1]].

For the segment with endpoints $a,x$ we write $\Delta_{a,x}=\{a+t(x-a):\ t\in[0,1]\}$, and $\hat\Delta_{a,x}$ is the same segment without its endpoints.

> [!theorem] Theorem 6.5.2 (Taylor–Lagrange formula)
> Let the set $E$ be open in $\mathbb R^n$, $s\in\mathbb Z_+$, let the function $f:E\to\mathbb R$ be $s+1$ times differentiable on $E$, $a,x\in E$, $a\ne x$, $\Delta_{a,x}\subset E$. Then there is $c\in\hat\Delta_{a,x}$ such that
> $$
> f(x)=\sum_{k=0}^{s}\frac{d_a^kf(x-a)}{k!}+\frac{d_c^{s+1}f(x-a)}{(s+1)!}.
> $$

^thm-6-5-2

*Proof idea.* The function $\varphi(t)=f(a+t(x-a))$ is $s+1$ times differentiable on $[0,1]$, and by induction $\varphi^{(k)}(t)=d^k_{a+t(x-a)}f(x-a)$; the one-variable Taylor formula with the Lagrange remainder is applied to $\varphi$.

> [!theorem] Theorem 6.5.3 (mean value theorem)
> Let the set $E$ be open in $\mathbb R^n$, let the function $f:E\to\mathbb R$ be differentiable on $E$, $a,b\in E$, $a\ne b$, $\Delta_{a,b}\subset E$. Then there is $c\in\hat\Delta_{a,b}$ such that $f(b)-f(a)=d_cf(b-a)$.

^thm-6-5-3

This is the case $s=0$ of [[#^thm-6-5-2|theorem 6.5.2]]. For maps the equality fails: for $\gamma(t)=(\cos t,\sin t)$ on $[0,2\pi]$ we have $\gamma(2\pi)-\gamma(0)=0$, while $\|\gamma'(t)\|=1$ for all $t$. An estimate remains true.

> [!theorem] Theorem 6.5.4 (Taylor–Lagrange formula for maps)
> Let the set $E$ be open in $\mathbb R^n$, $s\in\mathbb Z_+$, let the map $f:E\to\mathbb R^m$ be $s+1$ times differentiable on $E$, $a,x\in E$, $a\ne x$, $\Delta_{a,x}\subset E$. Then
> $$
> \Bigl\|f(x)-\sum_{k=0}^{s}\frac{d_a^kf(x-a)}{k!}\Bigr\|\le\frac{1}{(s+1)!}\sup_{c\in\hat\Delta_{a,x}}\bigl\|d_c^{s+1}f(x-a)\bigr\|.\qquad(6.5.2)
> $$

^thm-6-5-4

*Proof idea.* For the unit vector $e$ pointing in the direction of the left-hand side (under the [[en/14-several-variables#14.1 Euclidean space and norms|norm]] sign), the function $g=\langle f,e\rangle$ is scalar; [[#^thm-6-5-2|theorem 6.5.2]] is applied to it, followed by the [[en/21-lp-spaces#^sec-21-4|Cauchy–Schwarz inequality]] $|\langle v,e\rangle|\le\|v\|$.

> [!theorem] Theorem 6.5.5 (estimate of the remainder)
> Let the set $E$ be open in $\mathbb R^n$, $s\in\mathbb Z_+$, $f\in C^{s+1}(E,\mathbb R^m)$, $a,x\in E$, $a\ne x$, $\Delta_{a,x}\subset E$, and
> $$
> M=\max_{|\alpha|=s+1}\ \sup_{c\in\hat\Delta_{a,x}}\bigl\|\partial^\alpha f(c)\bigr\|.
> $$
> Then $M<+\infty$ and the remainder $R_{a,s}f(x)=f(x)-T_{a,s}f(x)$ satisfies the inequality
> $$
> \|R_{a,s}f(x)\|\le\frac{M}{(s+1)!}\bigl(\sqrt n\,\|x-a\|\bigr)^{s+1}.
> $$

^thm-6-5-5

The finiteness of $M$ follows from the continuity of the derivatives on the [[en/13-metric-spaces#13.4 Compactness|compact]] segment; the estimate follows from (6.5.2), since $\|d_c^{s+1}f(h)\|\le M\bigl(|h_1|+\ldots+|h_n|\bigr)^{s+1}\le M(\sqrt n\,\|h\|)^{s+1}$.

## §6.6. Implicit maps

Let $E\subset\mathbb R^{n+m}$ be open, $f:E\to\mathbb R^m$, and write points as $(x,y)$, $x\in\mathbb R^n$, $y\in\mathbb R^m$. A system of $m$ equations
$$
f(x,y)=0\qquad(6.6.3)
$$
defines $y$ as a function of $x$ only locally and under a nondegeneracy condition. The linear approximation near a solution $(x^0,y^0)$ is the system $f'_x(x^0,y^0)h+f'_y(x^0,y^0)k=0$, uniquely solvable for $k$ when $\det f'_y(x^0,y^0)\ne0$.

> [!theorem] Theorem 6.6.1 (implicit map theorem)
> Let the set $E$ be open in $\mathbb R^{n+m}$, $(x^0,y^0)\in E$, $s\in\mathbb N$, $f\in C^s(E,\mathbb R^m)$, $f(x^0,y^0)=0$ and $\det f'_y(x^0,y^0)\ne0$. Then there exist a neighbourhood $V$ of the point $(x^0,y^0)$, an open set $U\ni x^0$ in $\mathbb R^n$ and a map $\psi\in C^s(U,\mathbb R^m)$ such that
> $$
> \{(x,y)\in V:\ f(x,y)=0\}=\{(x,\psi(x)):\ x\in U\}.
> $$

^thm-6-6-1

> [!definition] Definition 6.6.1
> The map $\psi$ of [[#^thm-6-6-1|theorem 6.6.1]] is called the implicit map defined by the equation $f(x,y)=0$ in a neighbourhood of the point $(x^0,y^0)$.

^def-6-6-1

The derivative of the [[#^def-6-6-1|implicit map]] is found by differentiating the identity $f(x,\psi(x))\equiv0$: $f'_x+f'_y\psi'=0$, i.e.
$$
\psi'(x)=-\bigl[f'_y(x,\psi(x))\bigr]^{-1}f'_x(x,\psi(x)).
$$
Example: the equation $x^2+y^2=1$ near $(0,1)$ defines $\psi(x)=\sqrt{1-x^2}$, $\psi'(x)=-x/y$; at the points $(\pm1,0)$, where $f'_y=2y=0$, the theorem does not apply.

## §6.7. Extrema of functions of several variables

> [!definition] Definition 6.7.1
> Let $E\subset\mathbb R^n$, $a\in E$, $f:E\to\mathbb R$. The point $a$ is called a point of minimum (maximum) of $f$ if for some neighbourhood $V$ of the point $a$ we have $f(x)\ge f(a)$ (respectively $f(x)\le f(a)$) for all $x\in V\cap E$; a point of strict minimum (maximum) if the inequality is strict for $x\ne a$. Points of minimum and maximum are called extremum points.

^def-6-7-1

> [!theorem] Theorem 6.7.1 (necessary condition for an extremum)
> Let $E\subset\mathbb R^n$, let $a$ be an interior point of $E$, and let the function $f:E\to\mathbb R$ be differentiable at the point $a$. If $a$ is an extremum point of $f$, then $d_af=0$, i.e. $\frac{\partial f}{\partial x_i}(a)=0$ for all $i$.

^thm-6-7-1

The proof reduces to [[en/06-derivatives#^fermat-theorem|Fermat's theorem]] for $t\mapsto f(a+th)$. Points with $d_af=0$ are called stationary.

> [!theorem] Theorem 6.7.2 (sufficient condition for an extremum)
> Let $E\subset\mathbb R^n$, let $a$ be an interior point of $E$, let $f:E\to\mathbb R$ be twice differentiable at the point $a$, and $d_af=0$.
> 1. If the quadratic form $d_a^2f$ is positive definite, then $a$ is a point of strict minimum.
> 2. If $d_a^2f$ is negative definite, then $a$ is a point of strict maximum.
> 3. If $d_a^2f$ takes values of both signs, then there is no extremum at $a$.

^thm-6-7-2

*Proof idea.* By [[#^thm-6-5-1|theorem 6.5.1]] $f(a+h)-f(a)=\frac12d_a^2f(h)+o(\|h\|^2)$, and by compactness of the unit sphere a positive definite form satisfies $d_a^2f(h)\ge c\|h\|^2$, $c>0$.

In the two-dimensional case, with $A=f''_{xx}(a)$, $B=f''_{xy}(a)$, $C=f''_{yy}(a)$: if $AC-B^2>0$, then $A>0$ gives a minimum and $A<0$ a maximum; if $AC-B^2<0$, there is no extremum; if $AC-B^2=0$, higher-order terms are needed.

> [!definition] Definition 6.7.2
> Let $E\subset\mathbb R^n$, $a\in E$, $m<n$, $f,\varphi_1,\ldots,\varphi_m:E\to\mathbb R$. If $a$ is an extremum point of the restriction of $f$ to the set $\{x\in E:\ \varphi_k(x)=\varphi_k(a),\ k=1,\ldots,m\}$, then $a$ is called a point of conditional (relative) extremum of $f$ subject to the constraint equations $\varphi_k(x)=\varphi_k(a)$.

^def-6-7-2

From now on $\Phi=(\varphi_1,\ldots,\varphi_m)$, and the constraints are written as $\Phi=0$.

> [!theorem] Theorem 6.7.3 (necessary condition for a relative extremum)
> Let $m<n$, let the set $E$ be open in $\mathbb R^n$, $a\in E$, $f\in C^1(E)$, $\Phi\in C^1(E,\mathbb R^m)$, $\operatorname{rank}\Phi'(a)=m$, and let $a$ be a point of conditional extremum of $f$ subject to the constraints $\Phi=0$. Then there exist $\lambda_1,\ldots,\lambda_m\in\mathbb R$ (Lagrange multipliers) such that
> $$
> \operatorname{grad}f(a)=\sum_{k=1}^{m}\lambda_k\operatorname{grad}\varphi_k(a).\qquad(6.7.1)
> $$

^thm-6-7-3

*Proof idea.* By [[#^thm-6-6-1|theorem 6.6.1]] the constraints can be solved near $a$ for $m$ variables, the restriction of $f$ becomes a function of $n-m$ free variables, and [[#^thm-6-7-1|theorem 6.7.1]] is applied to it.

> [!theorem] Theorem 6.7.4
> Under the assumptions of [[#^thm-6-7-3|theorem 6.7.3]], for the Lagrange function
> $$
> L(x,\lambda)=f(x)-\sum_{k=1}^{m}\lambda_k\varphi_k(x)\qquad(x\in E,\ \lambda\in\mathbb R^m)
> $$
> there is $\lambda\in\mathbb R^m$ such that $\operatorname{grad}L(a,\lambda)=0$ (the gradient with respect to all $n+m$ variables).

^thm-6-7-4

A conditional extremum is sought among the solutions of the system $\operatorname{grad}L=0$: these are $n+m$ equations in $n+m$ unknowns.

> [!definition] Definition 6.7.3
> A quadratic form $Q$ on $\mathbb R^n$ is called positive (negative) definite on a linear subspace $N$ if $Q(h)>0$ (respectively $Q(h)<0$) for all $h\in N\setminus\{0\}$.

^def-6-7-3

> [!theorem] Theorem 6.7.5 (sufficient condition for a relative extremum)
> Let $m<n$, let the set $E$ be open in $\mathbb R^n$, $a\in E$, $f\in C^2(E)$, $\Phi\in C^2(E,\mathbb R^m)$, $\Phi(a)=0$, $\operatorname{rank}\Phi'(a)=m$, let $\lambda$ satisfy (6.7.1), $L(x)=f(x)-\sum_k\lambda_k\varphi_k(x)$ and $N=\{h:\ d_a\Phi(h)=0\}$.
> 1. If $d_a^2L$ is positive (negative) definite on $N$, then $a$ is a point of conditional minimum (maximum).
> 2. If $d_a^2L$ takes values of both signs on $N$, then there is no conditional extremum at $a$.

^thm-6-7-5

## Worked example

**Unconstrained extremum.** For $f(x,y)=x^3+y^3-3xy$ the stationary points are found from $3x^2-3y=0$, $3y^2-3x=0$: they are $(0,0)$ and $(1,1)$. At $(0,0)$: $A=C=0$, $B=-3$, $AC-B^2=-9<0$, so there is no extremum. At $(1,1)$: $A=C=6$, $B=-3$, $AC-B^2=27>0$, $A>0$, a strict minimum $f(1,1)=-1$.

**Constrained extremum.** For $f=xy$ subject to $\varphi=x^2+y^2-2=0$: $L=xy-\lambda(x^2+y^2-2)$, condition (6.7.1) gives $y=2\lambda x$, $x=2\lambda y$, whence $\lambda=\pm\frac12$. For $\lambda=\frac12$ we get the points $\pm(1,1)$; here $N=\{h:\ h_1+h_2=0\}$ and $d^2L(h)=2h_1h_2-(h_1^2+h_2^2)=-4h_1^2<0$ on $N\setminus\{0\}$, a conditional maximum $1$. For $\lambda=-\frac12$ we get the points $\pm(1,-1)$, $d^2L=4h_1^2>0$ on $N$, a conditional minimum $-1$.

## Common pitfalls

1. Confusing the Peano remainder $o(\|h\|^s)$ (only $s$-fold differentiability at the point is needed) with the estimate $O(\|h\|^{s+1})$, which requires more smoothness.
2. Writing the mean value theorem for a map as an equality: for $\mathbb R^m$-valued maps only the estimate (6.5.2) holds.
3. Applying [[#^thm-6-6-1|theorem 6.6.1]] without checking $\det f'_y(x^0,y^0)\ne0$, or treating its conclusion as global.
4. Drawing a conclusion about an extremum when the form $d_a^2f$ is only semidefinite (compare $x^2+y^4$ and $x^2-y^4$).
5. In a conditional extremum problem, checking the sign of $d_a^2L$ on the whole of $\mathbb R^n$ instead of on the subspace $N$ (the condition "on the whole space" is sufficient but often fails).

## Exercises

1. Write down $T_{0,2}f$ for $f(x,y)=e^x\cos y$.
2. The equation $e^y+y+x^2=1$ defines a function $y(x)$ near $(0,0)$. Find $y'(0)$ and $y''(0)$.
3. Find the extrema of $f(x,y)=x^2+xy+y^2-3x$.
4. Find the largest and the smallest values of $f=x+2y+2z$ on the sphere $x^2+y^2+z^2=9$.

> [!answer]- Short answers
> 1. $1+x+\frac{x^2-y^2}{2}$.
> 2. $y'=-\frac{2x}{e^y+1}$, $y'(0)=0$; $y''(0)=-1$.
> 3. Stationary point $(2,-1)$: $A=C=2$, $B=1$, $AC-B^2=3>0$, $A>0$, a minimum $f(2,-1)=-3$.
> 4. $\operatorname{grad}f=2\lambda(x,y,z)$ gives $\pm(1,2,2)$: maximum $9$, minimum $-9$.

---

[[en/21-lp-spaces|← 21. Lᵖ Spaces and Modes of Convergence]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]] · [[en/23-numerical-series|23. Numerical Series →]]

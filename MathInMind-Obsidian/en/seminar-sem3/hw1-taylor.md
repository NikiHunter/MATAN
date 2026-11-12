---
title: "Seminar NM-204. HW 1 — Taylor's formula: solutions"
lang: en
hw: 1
tags: [mathinmind/en, mathinmind/other]
---
# HW 1. Taylor's formula in $\mathbb R^n$ — solutions

[[ru/seminar-sem3/hw1-taylor|Русский]] · **English** · [[es/seminar-sem3/hw1-taylor|Español]]

[[en/seminar-sem3/index|All assignments]] · [[en/seminar-sem3/hw2-conditional-extremum|HW 2 →]] · [[en/lectures-2025-26/lecture-65-66|Lectures 65–66, §6.5]]

> [!note] Reference
> [[en/lectures-2025-26/lecture-65-66#^thm-6-5-2|Theorem 6.5.2 (Taylor–Lagrange formula)]]: if $f$ is $s+1$ times differentiable, then
> $$
> f(a+h)=\sum_{k=0}^{s}\frac{d_a^kf(h)}{k!}+\frac{d_c^{s+1}f(h)}{(s+1)!},\qquad c=a+\theta h,\ \theta\in(0,1).
> $$
> Throughout, $a$ is the expansion point and $h=(h_1,h_2,h_3)=(x,y,z)-a$ is the increment.

## The general idea: why everything reduces to one variable

Fix $a$ and $h$ and consider the function of one variable $F(t)=f(a+th)$, $t\in[0,1]$. By the chain rule
$$
F^{(k)}(t)=d^k_{a+th}f(h)=\sum_{|\alpha|=k}\frac{k!}{\alpha!}\,\partial^\alpha f(a+th)\,h^\alpha .
$$
So Taylor's formula for $f$ at $a$ is the ordinary one-dimensional Taylor formula for $F$ at zero, taken at $t=1$:
$$
f(a+h)=F(1)=\sum_{k=0}^{s}\frac{F^{(k)}(0)}{k!}+\frac{F^{(s+1)}(\theta)}{(s+1)!}.
$$
Two practical consequences follow.

1. **The homogeneous part of degree $k$ of the expansion equals $d^k_af(h)/k!$** and is uniquely determined: if $f(a+h)=\sum_{k\le s}P_k(h)+o(|h|^s)$ with $P_k$ a homogeneous polynomial of degree $k$, then $P_k(h)=d_a^kf(h)/k!$ (uniqueness of the Taylor polynomial). So computing partial derivatives is not mandatory: any legitimate manipulation that produces a polynomial in $h$ with the right remainder produces exactly the Taylor polynomial.
2. **For a polynomial of degree $N$ the sum terminates:** all derivatives of order $N+1$ vanish, so the Lagrange remainder with $s=N$ is identically zero. Expanding a polynomial is just substituting $x=a_1+h_1,\dots$ and multiplying out; the "Taylor series" is finite and equals $f$ exactly, for all $h$, not only for small ones.

## Problem 1.1

> [!note] At the seminar
> [[en/seminar-sem3/notes-1-taylor-extremum#^ex-2-2|Example 2.2]] (4 Sep): the same problem; the board works out the point $(1;-1;2)$.

**Statement.** $f(x,y,z)=x^3+y^3+z^3-3xyz$. Expand by Taylor's formula at the points $(1;1;1)$ and $(1;-1;2)$.

**Solution.** Partial derivatives:
$$
f_x=3x^2-3yz,\quad f_y=3y^2-3xz,\quad f_z=3z^2-3xy;
$$
$$
f_{xx}=6x,\ f_{yy}=6y,\ f_{zz}=6z,\qquad f_{xy}=-3z,\ f_{xz}=-3y,\ f_{yz}=-3x;
$$
$$
f_{xxx}=f_{yyy}=f_{zzz}=6,\qquad f_{xyz}=-3,
$$
the other third-order derivatives are zero, and all fourth-order derivatives are zero.

The third differential does not depend on the point:
$$
\frac{d^3f(h)}{3!}=\frac{1}{6}\bigl(6h_1^3+6h_2^3+6h_3^3+6\cdot(-3)h_1h_2h_3\bigr)=h_1^3+h_2^3+h_3^3-3h_1h_2h_3 .
$$
(The coefficient $6$ of $h_1h_2h_3$ is the number $3!/(1!\,1!\,1!)$ of orderings of the mixed derivative $f_{xyz}$.)

*Point $a=(1;1;1)$.* Here $f(a)=0$, $\nabla f(a)=(0,0,0)$, and the second derivatives are $f_{xx}=f_{yy}=f_{zz}=6$, $f_{xy}=f_{xz}=f_{yz}=-3$. Hence
$$
\frac{d_a^2f(h)}{2!}=\frac12\bigl(6h_1^2+6h_2^2+6h_3^2-6h_1h_2-6h_1h_3-6h_2h_3\bigr),
$$
$$
\boxed{f(1+h_1,1+h_2,1+h_3)=3\bigl(h_1^2+h_2^2+h_3^2-h_1h_2-h_1h_3-h_2h_3\bigr)+h_1^3+h_2^3+h_3^3-3h_1h_2h_3 .}
$$

*Point $a=(1;-1;2)$.* Here $f(a)=1-1+8+6=14$, $\nabla f(a)=(3+6,\ 3-6,\ 12+3)=(9,-3,15)$; $f_{xx}=6$, $f_{yy}=-6$, $f_{zz}=12$, $f_{xy}=-6$, $f_{xz}=3$, $f_{yz}=-3$. Hence
$$
\boxed{\begin{aligned}f(1+h_1,-1+h_2,2+h_3)={}&14+9h_1-3h_2+15h_3\\&+3h_1^2-3h_2^2+6h_3^2-6h_1h_2+3h_1h_3-3h_2h_3\\&+h_1^3+h_2^3+h_3^3-3h_1h_2h_3 .\end{aligned}}
$$
In the original variables $h_1=x-1$, $h_2=y+1$, $h_3=z-2$.

**Why it works.** The top (cubic) part of the expansion coincides with $f$ itself evaluated at the increments: shifting the argument does not change the top homogeneous part of a polynomial. At $(1;1;1)$ the constant and linear terms vanish because $f=(x+y+z)\cdot\frac12\bigl((x-y)^2+(y-z)^2+(z-x)^2\bigr)$ vanishes on the line $x=y=z$ together with its gradient; the quadratic part $\frac32\bigl((h_1-h_2)^2+(h_2-h_3)^2+(h_3-h_1)^2\bigr)$ is non-negative — on that line $f$ has a non-strict minimum.

**Check.** For $h=(1,0,0)$ at the first point: $f(2,1,1)=8+1+1-6=4$, the formula gives $3+1=4$. At the second point: $f(2,-1,2)=8-1+8+12=27$, the formula gives $14+9+3+1=27$.

## Problem 1.2

**Statement.** $f(x,y)=5x^4-4x^2y^2+3y^4-2xy+1$. Expand by Taylor's formula at the point $(-3;2)$.

**Solution.** Put $x=-3+h_1$, $y=2+h_2$ and find the differentials at $a=(-3;2)$.

Value: $f(a)=5\cdot81-4\cdot9\cdot4+3\cdot16-2\cdot(-6)+1=405-144+48+12+1=322$.

First derivatives: $f_x=20x^3-8xy^2-2y$, $f_y=-8x^2y+12y^3-2x$;
$$
f_x(a)=-540+96-4=-448,\qquad f_y(a)=-144+96+6=-42 .
$$

Second: $f_{xx}=60x^2-8y^2$, $f_{xy}=-16xy-2$, $f_{yy}=-8x^2+36y^2$;
$$
f_{xx}(a)=540-32=508,\qquad f_{xy}(a)=96-2=94,\qquad f_{yy}(a)=-72+144=72 .
$$

Third: $f_{xxx}=120x$, $f_{xxy}=-16y$, $f_{xyy}=-16x$, $f_{yyy}=72y$;
$$
f_{xxx}(a)=-360,\quad f_{xxy}(a)=-32,\quad f_{xyy}(a)=48,\quad f_{yyy}(a)=144 .
$$

Fourth (constant): $f_{xxxx}=120$, $f_{xxyy}=-16$, $f_{yyyy}=72$, $f_{xxxy}=f_{xyyy}=0$.

Assemble $d^k_af(h)/k!$ with binomial coefficients:
$$
\frac{d^2}{2!}=\frac12\bigl(508h_1^2+2\cdot94h_1h_2+72h_2^2\bigr)=254h_1^2+94h_1h_2+36h_2^2,
$$
$$
\frac{d^3}{3!}=\frac16\bigl(-360h_1^3+3\cdot(-32)h_1^2h_2+3\cdot48h_1h_2^2+144h_2^3\bigr)=-60h_1^3-16h_1^2h_2+24h_1h_2^2+24h_2^3,
$$
$$
\frac{d^4}{4!}=\frac1{24}\bigl(120h_1^4+6\cdot(-16)h_1^2h_2^2+72h_2^4\bigr)=5h_1^4-4h_1^2h_2^2+3h_2^4 .
$$

**Answer.** With $h_1=x+3$, $h_2=y-2$
$$
\boxed{\begin{aligned}f(x,y)={}&322-448h_1-42h_2+254h_1^2+94h_1h_2+36h_2^2\\&-60h_1^3-16h_1^2h_2+24h_1h_2^2+24h_2^3+5h_1^4-4h_1^2h_2^2+3h_2^4 .\end{aligned}}
$$

**Why it works.** $f$ is a polynomial of degree four, so $d^5f\equiv0$ and the remainder is zero: the equality is exact. The top part $5h_1^4-4h_1^2h_2^2+3h_2^4$ repeats the top part of $f$. Multiplying out $f(-3+h_1,2+h_2)$ directly gives the same answer — by uniqueness of the Taylor polynomial.

**Check.** $h=(1,0)$: $f(-2,2)=80-64+48+8+1=73$; the formula gives $322-448+254-60+5=73$. $h=(0,1)$: $f(-3,3)=405-324+243+18+1=343$; the formula gives $322-42+36+24+3=343$.

## Problem 1.3

**Statement.** $f(x,y,z)=e^{xy+z^2}$. Find the explicit Taylor expansion up to degree three with the Lagrange remainder at the point $a=(-2;0;3)$.

**Solution.** Substitute $x=-2+h_1$, $y=h_2$, $z=3+h_3$ into the exponent:
$$
xy+z^2=(-2+h_1)h_2+(3+h_3)^2=9+\underbrace{(-2h_2+6h_3)}_{L}+\underbrace{(h_1h_2+h_3^2)}_{Q}.
$$
Here $L$ is a linear and $Q$ a quadratic form in $h$; the exponent is a polynomial of degree two, so this equality is exact. Along the segment $a+th$:
$$
F(t)=f(a+th)=e^{u(t)},\qquad u(t)=9+Lt+Qt^2,\quad u'=L+2Qt,\quad u''=2Q,\quad u'''=0 .
$$
Differentiate the exponential of a function (each time $(e^u)'=e^uu'$, and $u'''=0$):
$$
F'=e^uu',\qquad F''=e^u\bigl(u'^2+u''\bigr),\qquad F'''=e^u\bigl(u'^3+3u'u''\bigr),\qquad F^{(4)}=e^u\bigl(u'^4+6u'^2u''+3u''^2\bigr).
$$
At $t=0$: $u=9$, $u'=L$, $u''=2Q$, so
$$
F(0)=e^9,\quad F'(0)=e^9L,\quad \frac{F''(0)}{2!}=e^9\Bigl(\frac{L^2}{2}+Q\Bigr),\quad \frac{F'''(0)}{3!}=e^9\Bigl(\frac{L^3}{6}+LQ\Bigr).
$$
Multiplying out:
$$
\frac{L^2}{2}+Q=2h_2^2-12h_2h_3+18h_3^2+h_1h_2+h_3^2=h_1h_2+2h_2^2-12h_2h_3+19h_3^2,
$$
$$
\frac{L^3}{6}+LQ=-2h_1h_2^2+6h_1h_2h_3-\frac43h_2^3+12h_2^2h_3-38h_2h_3^2+42h_3^3 .
$$

**Answer.** With $h_1=x+2$, $h_2=y$, $h_3=z-3$ there is $\theta\in(0,1)$ (depending on $h$) such that
$$
\boxed{\begin{aligned}e^{xy+z^2}=e^9\Bigl[&1+(-2h_2+6h_3)+\bigl(h_1h_2+2h_2^2-12h_2h_3+19h_3^2\bigr)\\&+\Bigl(-2h_1h_2^2+6h_1h_2h_3-\frac43h_2^3+12h_2^2h_3-38h_2h_3^2+42h_3^3\Bigr)\Bigr]+R_3(h),\end{aligned}}
$$
$$
\boxed{R_3(h)=\frac{d^4_{a+\theta h}f(h)}{4!}=\frac{e^{\,9+L\theta+Q\theta^2}}{24}\Bigl[(L+2Q\theta)^4+12\,Q\,(L+2Q\theta)^2+12\,Q^2\Bigr],}
$$
where $L=-2h_2+6h_3$, $Q=h_1h_2+h_3^2$.

**Why it works.** The Lagrange remainder is $F^{(4)}(\theta)/4!$, and $F^{(4)}(\theta)$ is exactly the fourth differential of $f$ at the intermediate point $c=a+\theta h$ on the vector $h$. In the coordinates of $c=(\xi,\eta,\zeta)$ the same thing reads: $L+2Q\theta=\eta h_1+\xi h_2+2\zeta h_3=d_c u(h)$ for $u=xy+z^2$, and $9+L\theta+Q\theta^2=\xi\eta+\zeta^2$, that is
$$
R_3(h)=\frac{e^{\xi\eta+\zeta^2}}{24}\Bigl[(\eta h_1+\xi h_2+2\zeta h_3)^4+12(h_1h_2+h_3^2)(\eta h_1+\xi h_2+2\zeta h_3)^2+12(h_1h_2+h_3^2)^2\Bigr].
$$
This is the same sum $\frac1{4!}\sum_{|\alpha|=4}\frac{4!}{\alpha!}\partial^\alpha f(c)h^\alpha$ of 15 terms, already collected. The Taylor polynomial can also be obtained by substituting $w=L+Q$ into $e^w=1+w+\frac{w^2}2+\frac{w^3}6+\dots$ and dropping terms of degree above three — the result is the same by uniqueness.

**Check.** $h=(0,0,h_3)$: $f=e^{(3+h_3)^2}=e^9e^{6h_3+h_3^2}=e^9\bigl(1+6h_3+19h_3^2+42h_3^3+\dots\bigr)$, since $\frac{36}{2}+1=19$ and $\frac{216}{6}+6=42$.

## Problem 1.4

> [!note] At the seminar
> [[en/seminar-sem3/notes-1-taylor-extremum#^ex-4-1|Example 4.1]] (18 Sep): all derivatives up to order two and their values at the point, collected in one table.

**Statement.** $f(x,y,z)=x^2\sin(xy)\,e^{y+z}$. Find the explicit Taylor expansion up to degree two with the Lagrange remainder at the point $a=(-1;\pi;2)$.

**Solution.** Write $E=e^{y+z}$, $S=\sin(xy)$, $C=\cos(xy)$. Since $f$ depends on $z$ only through the factor $e^{z}$, we have $\partial_zf=f$: each differentiation in $z$ changes nothing. The other derivatives:
$$
f_x=E\,(2xS+x^2yC),\qquad f_y=E\,(x^2S+x^3C),
$$
$$
f_{xx}=E\,\bigl((2-x^2y^2)S+4xyC\bigr),\quad f_{xy}=E\,\bigl((2x-x^3y)S+(3x^2+x^2y)C\bigr),\quad f_{yy}=E\,\bigl((x^2-x^4)S+2x^3C\bigr),
$$
$$
f_{xz}=f_x,\qquad f_{yz}=f_y,\qquad f_{zz}=f .
$$
At $a$: $xy=-\pi$, $S=0$, $C=-1$, $E=e^{\pi+2}$, $x=-1$, $y=\pi$. Hence
$$
f(a)=0,\qquad f_x(a)=-\pi e^{\pi+2},\quad f_y(a)=e^{\pi+2},\quad f_z(a)=0,
$$
$$
f_{xx}(a)=4\pi e^{\pi+2},\quad f_{xy}(a)=-(3+\pi)e^{\pi+2},\quad f_{yy}(a)=2e^{\pi+2},\quad f_{xz}(a)=-\pi e^{\pi+2},\quad f_{yz}(a)=e^{\pi+2},\quad f_{zz}(a)=0 .
$$
Therefore
$$
\frac{d_a^2f(h)}{2!}=e^{\pi+2}\bigl(2\pi h_1^2+h_2^2-(3+\pi)h_1h_2-\pi h_1h_3+h_2h_3\bigr).
$$

The remainder needs the third-order derivatives:
$$
f_{xxx}=E\,\bigl(-6xy^2S+(6y-x^2y^3)C\bigr),
$$
$$
f_{xxy}=E\,\bigl((2-6x^2y-x^2y^2)S+(6x+4xy-x^3y^2)C\bigr),
$$
$$
f_{xyy}=E\,\bigl((2x-4x^3-2x^3y)S+(6x^2+x^2y-x^4y)C\bigr),
$$
$$
f_{yyy}=E\,\bigl((x^2-3x^4)S+(3x^3-x^5)C\bigr),
$$
$$
f_{xxz}=f_{xx},\quad f_{xyz}=f_{xy},\quad f_{yyz}=f_{yy},\quad f_{xzz}=f_x,\quad f_{yzz}=f_y,\quad f_{zzz}=f .
$$

**Answer.** With $h_1=x+1$, $h_2=y-\pi$, $h_3=z-2$ there is $\theta\in(0,1)$ such that
$$
\boxed{f(x,y,z)=e^{\pi+2}\Bigl[-\pi h_1+h_2+2\pi h_1^2+h_2^2-(3+\pi)h_1h_2-\pi h_1h_3+h_2h_3\Bigr]+R_2(h),}
$$
$$
\boxed{\begin{aligned}R_2(h)=\frac{d^3_cf(h)}{3!}=\frac16\Bigl[&f_{xxx}h_1^3+f_{yyy}h_2^3+f\,h_3^3+3f_{xxy}h_1^2h_2+3f_{xyy}h_1h_2^2\\&+3f_{xx}h_1^2h_3+3f_{yy}h_2^2h_3+3f_xh_1h_3^2+3f_yh_2h_3^2+6f_{xy}h_1h_2h_3\Bigr]_{c},\end{aligned}}
$$
where all derivatives (written out above) are taken at the point $c=(-1+\theta h_1,\ \pi+\theta h_2,\ 2+\theta h_3)$.

**Why it works.** The coefficients $1,3,6$ in the remainder are the multinomial numbers $3!/\alpha!$: there is one "pure" derivative of each kind, three derivatives of the form $\partial^2_i\partial_j$, and $f_{xyz}$ occurs $3!=6$ times. The degree-two polynomial is easiest to check by multiplying one-dimensional expansions. Since $xy=-\pi+s$ with $s=\pi h_1-h_2+h_1h_2$, we have $\sin(xy)=-\sin s=-s+O(|h|^3)$, and
$$
x^2=1-2h_1+h_1^2,\qquad e^{y+z}=e^{\pi+2}\bigl(1+h_2+h_3+\dots\bigr).
$$
The factor $\sin(xy)$ vanishes at $a$, so from the other factors only terms up to first order are needed:
$$
f=-e^{\pi+2}\bigl[(\pi h_1-h_2+h_1h_2)+(\pi h_1-h_2)(-2h_1+h_2+h_3)\bigr]+o(|h|^2),
$$
which after multiplying out coincides with the answer. This is no accident: the Taylor polynomial of a product equals the product of the Taylor polynomials truncated by degree (uniqueness).

**Check.** $h=(0,h_2,0)$: $f=\sin(-\pi-h_2)\,e^{\pi+2+h_2}=\sin h_2\cdot e^{\pi+2}e^{h_2}=e^{\pi+2}(h_2+h_2^2+\dots)$ — it matches.

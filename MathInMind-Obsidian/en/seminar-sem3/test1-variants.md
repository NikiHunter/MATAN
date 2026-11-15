---
title: "Seminar NM-204. Test of 20 Nov — practice variants"
lang: en
tags: [mathinmind/en, mathinmind/other]
---
# Test of 20 November 2026: practice variants with solutions

[[ru/seminar-sem3/test1-variants|Русский]] · **English** · [[es/seminar-sem3/test1-variants|Español]]

[[en/seminar-sem3/index|All assignments]] · [[en/seminar-sem3/test1-guide|← How to prepare]]

> [!note] What this is
> Three practice variants in the format announced at the consultation: problem 1a — a polynomial (degree 3 in three variables or degree 4 in two), 1b — a non-polynomial function of three variables up to order two with the Lagrange remainder in general form, 2 — a constrained extremum of a function of three variables under one polynomial condition. The problems are modelled on the consultation examples; there are no real papers. As the instructor promised, every problem 2 has a maximum, a minimum and a point with no extremum, all minors to be checked are non-zero, and the equations for $\lambda$ are of degree at most two. Solve them in writing, without a calculator, and only then open the solutions; all computations were checked in sympy. The series problems from the earlier version of this page moved to the [[en/seminar-sem3/series-test-guide#Practice problems|series test]].

Notation in the solutions: $D^{\alpha}f$ is the partial derivative with multi-index $\alpha$, $\widetilde H$ is the bordered Hessian with the border in the first row and column, $\Delta_3$ and $\Delta_4$ are its leading minors. A minimum is $\Delta_3<0$, $\Delta_4<0$; a maximum is $\Delta_3>0$, $\Delta_4<0$; otherwise there is no extremum ([[en/seminar-sem3/test1-guide#Problem 2: constrained extremum|table]]).

## Variant A

**1a.** Expand by Taylor's formula at the point $P=(1;-1;2)$ the function $f(x;y;z)=x^3-2xyz+y^2z+3z-1$.

**1b.** Find the Taylor expansion of $f(x;y;z)=x\,e^{y+2z}+\sin(xy)$ up to degree two at the point $P=(1;0;0)$ with the remainder in Lagrange form.

**2.** Find all points of constrained local extremum of $f(x;y;z)=x^2+2y+6z$ on the set $M=\{(x;y;z)\in\mathbb R^3:\ x^2+y^2+9z^2=18\}$.

> [!answer]- Solutions of variant A
> **1a.** Derivatives at an arbitrary point:
> $$
> D^{(1;0;0)}f=3x^2-2yz,\qquad D^{(0;1;0)}f=-2xz+2yz,\qquad D^{(0;0;1)}f=-2xy+y^2+3;
> $$
> $$
> D^{(2;0;0)}f=6x,\quad D^{(1;1;0)}f=-2z,\quad D^{(1;0;1)}f=-2y,\quad D^{(0;2;0)}f=2z,\quad D^{(0;1;1)}f=-2x+2y,\quad D^{(0;0;2)}f=0;
> $$
> $$
> D^{(3;0;0)}f=6,\qquad D^{(1;1;1)}f=-2,\qquad D^{(0;2;1)}f=2,
> $$
> the other third-order derivatives and all fourth-order ones are zero, so the sum is finite and there is no remainder.
>
> At $P$: $f(P)=1-2\cdot1\cdot(-1)\cdot2+(-1)^2\cdot2+3\cdot2-1=12$; $D^{(1;0;0)}f(P)=3+4=7$, $D^{(0;1;0)}f(P)=-4-4=-8$, $D^{(0;0;1)}f(P)=2+1+3=6$; $D^{(2;0;0)}f(P)=6$, $D^{(1;1;0)}f(P)=-4$, $D^{(1;0;1)}f(P)=2$, $D^{(0;2;0)}f(P)=4$, $D^{(0;1;1)}f(P)=-4$. Divide by $\alpha!$: $\frac62=3$, $\frac42=2$, $\frac{6}{3!}=1$, $\frac{2}{(0;2;1)!}=1$.
>
> **Answer.** For all $(x;y;z)\in\mathbb R^3$
> $$
> \begin{aligned}f={}&12+7(x-1)-8(y+1)+6(z-2)+3(x-1)^2-4(x-1)(y+1)+2(x-1)(z-2)+2(y+1)^2-4(y+1)(z-2)\\&+(x-1)^3-2(x-1)(y+1)(z-2)+(y+1)^2(z-2).\end{aligned}
> $$
> Check: the top part repeats $x^3-2xyz+y^2z$; at the point $(2;-1;2)$ the left side is $8+8+2+6-1=23$, the right side $12+7+3+1=23$.
>
> **1b.** Derivatives:
> $$
> D^{(1;0;0)}f=e^{y+2z}+y\cos(xy),\qquad D^{(0;1;0)}f=x\,e^{y+2z}+x\cos(xy),\qquad D^{(0;0;1)}f=2x\,e^{y+2z};
> $$
> $$
> D^{(2;0;0)}f=-y^2\sin(xy),\qquad D^{(1;1;0)}f=e^{y+2z}+\cos(xy)-xy\sin(xy),\qquad D^{(1;0;1)}f=2e^{y+2z},
> $$
> $$
> D^{(0;2;0)}f=x\,e^{y+2z}-x^2\sin(xy),\qquad D^{(0;1;1)}f=2x\,e^{y+2z},\qquad D^{(0;0;2)}f=4x\,e^{y+2z}.
> $$
> At $P$ ($e^0=1$, $\sin0=0$, $\cos0=1$): $f=1$; first order: $1$, $2$, $2$; second order: $0$, $2$, $2$, $1$, $2$, $4$.
>
> **Answer.** $f\in C^\infty(\mathbb R^3)$, so for every $(x;y;z)$ there is $t_0\in(0;1)$:
> $$
> \begin{aligned}x\,e^{y+2z}+\sin(xy)={}&1+(x-1)+2y+2z+2(x-1)y+2(x-1)z+\tfrac12y^2+2yz+2z^2\\&+\sum_{|\alpha|=3}\frac{D^{\alpha}f\bigl(1+t_0(x-1);\ t_0y;\ t_0z\bigr)}{\alpha!}\,(x-1)^{\alpha_1}y^{\alpha_2}z^{\alpha_3}.\end{aligned}
> $$
> Check: for $y=z=0$ the function equals $x=1+(x-1)$ — there is no quadratic term in $x-1$, just as $D^{(2;0;0)}f(P)=0$.
>
> **2.** $\mathcal L=x^2+2y+6z-\lambda(x^2+y^2+9z^2-18)$. The system:
> $$
> 2x-2\lambda x=0,\qquad 2-2\lambda y=0,\qquad 6-18\lambda z=0,\qquad x^2+y^2+9z^2=18 .
> $$
> From the second, $\lambda\ne0$ and $y=\frac1\lambda$; from the third, $z=\frac1{3\lambda}$; the first: $2x(1-\lambda)=0$.
>
> - $x=0$: $\frac1{\lambda^2}+\frac1{\lambda^2}=18$, $\lambda=\pm\frac13$. The points $(0;3;1)$ with $\lambda=\frac13$ and $(0;-3;-1)$ with $\lambda=-\frac13$.
> - $\lambda=1$: $y=1$, $z=\frac13$, $x^2=18-1-1=16$. The points $(\pm4;1;\frac13)$.
>
> $\varphi_x=2x$, $\varphi_y=2y$, $\varphi_z=18z$; $\mathcal L_{xx}=2-2\lambda$, $\mathcal L_{yy}=-2\lambda$, $\mathcal L_{zz}=-18\lambda$, no mixed derivatives. By the quick formulas
> $$
> \Delta_3=8\lambda x^2-8(1-\lambda)y^2,\qquad \Delta_4=-144\lambda^2x^2+144\lambda(1-\lambda)y^2+1296\lambda(1-\lambda)z^2 .
> $$
>
> | Point | $\lambda$ | $\Delta_3$ | $\Delta_4$ | Conclusion | $f$ |
> |---|---|---|---|---|---|
> | $(0;3;1)$ | $\frac13$ | $-48$ | $576$ | no extremum | $12$ |
> | $(0;-3;-1)$ | $-\frac13$ | $-96$ | $-1152$ | minimum | $-12$ |
> | $(4;1;\frac13)$, $(-4;1;\frac13)$ | $1$ | $128$ | $-2304$ | maximum | $20$ |
>
> **Answer.** $(\pm4;1;\frac13)$ are points of constrained local maximum, $f=20$; $(0;-3;-1)$ is a point of constrained local minimum, $f=-12$; at $(0;3;1)$ there is no extremum.
>
> **Why it works.** $M$ is an ellipsoid, a compact set, so $f$ attains its greatest and least values on it — they are $20$ and $-12$. But compactness says nothing about the point $(0;3;1)$: there $d^2\mathcal L=\frac43dx^2-\frac23(dy^2+9dz^2)$ is indefinite on the tangent plane.

## Variant B

**1a.** Expand by Taylor's formula at the point $P=(-1;2)$ the function $f(x;y)=x^4-2x^2y+3xy^2-y^3+5$.

**1b.** Find the Taylor expansion of $f(x;y;z)=\ln(x^2+yz)$ up to degree two at the point $P=(1;0;2)$ with the remainder in Lagrange form.

**2.** Find all points of constrained local extremum of $f(x;y;z)=x^2+8y+4z$ on the set $M=\{(x;y;z)\in\mathbb R^3:\ y^2-x^2-z^2=3\}$.

> [!answer]- Solutions of variant B
> **1a.** Derivatives:
> $$
> D^{(1;0)}f=4x^3-4xy+3y^2,\qquad D^{(0;1)}f=-2x^2+6xy-3y^2;
> $$
> $$
> D^{(2;0)}f=12x^2-4y,\qquad D^{(1;1)}f=-4x+6y,\qquad D^{(0;2)}f=6x-6y;
> $$
> $$
> D^{(3;0)}f=24x,\quad D^{(2;1)}f=-4,\quad D^{(1;2)}f=6,\quad D^{(0;3)}f=-6,\quad D^{(4;0)}f=24,
> $$
> the other fourth-order derivatives and all fifth-order ones are zero.
>
> At $P$: $f(P)=1-4-12-8+5=-18$; $D^{(1;0)}f(P)=-4+8+12=16$, $D^{(0;1)}f(P)=-2-12-12=-26$; $D^{(2;0)}f(P)=4$, $D^{(1;1)}f(P)=16$, $D^{(0;2)}f(P)=-18$; $D^{(3;0)}f(P)=-24$, $D^{(2;1)}f(P)=-4$, $D^{(1;2)}f(P)=6$, $D^{(0;3)}f(P)=-6$; $D^{(4;0)}f(P)=24$. Coefficients: $2$, $16$, $-9$; $-4$, $-2$, $3$, $-1$; $1$.
>
> **Answer.** For all $(x;y)\in\mathbb R^2$
> $$
> \begin{aligned}f={}&-18+16(x+1)-26(y-2)+2(x+1)^2+16(x+1)(y-2)-9(y-2)^2\\&-4(x+1)^3-2(x+1)^2(y-2)+3(x+1)(y-2)^2-(y-2)^3+(x+1)^4 .\end{aligned}
> $$
> Check: at the point $(0;2)$ the left side is $-8+5=-3$, the right side $-18+16+2-4+1=-3$.
>
> **1b.** Write $u=x^2+yz$; $f$ is defined and infinitely differentiable on the open set $\{u>0\}$, and $u(P)=1$.
> $$
> D^{(1;0;0)}f=\frac{2x}u,\qquad D^{(0;1;0)}f=\frac zu,\qquad D^{(0;0;1)}f=\frac yu;
> $$
> $$
> D^{(2;0;0)}f=\frac{2(yz-x^2)}{u^2},\quad D^{(1;1;0)}f=-\frac{2xz}{u^2},\quad D^{(1;0;1)}f=-\frac{2xy}{u^2},\quad D^{(0;2;0)}f=-\frac{z^2}{u^2},\quad D^{(0;1;1)}f=\frac{x^2}{u^2},\quad D^{(0;0;2)}f=-\frac{y^2}{u^2}.
> $$
> At $P$: $f=0$; first order: $2$, $2$, $0$; second order: $-2$, $-4$, $0$, $-4$, $1$, $0$.
>
> **Answer.** For those $(x;y;z)$ whose segment from $P$ lies in the region $x^2+yz>0$ (for example, for all points of a ball centred at $P$ inside this region), there is $t_0\in(0;1)$:
> $$
> \ln(x^2+yz)=2(x-1)+2y-(x-1)^2-4(x-1)y-2y^2+y(z-2)+\sum_{|\alpha|=3}\frac{D^{\alpha}f\bigl(1+t_0(x-1);\ t_0y;\ 2+t_0(z-2)\bigr)}{\alpha!}\,(x-1)^{\alpha_1}y^{\alpha_2}(z-2)^{\alpha_3}.
> $$
> Check: for $y=0$ we get $\ln x^2=2\ln\bigl(1+(x-1)\bigr)=2(x-1)-(x-1)^2+\dots$; for $x=1$, $z=2$ — $\ln(1+2y)=2y-2y^2+\dots$
>
> **2.** $\mathcal L=x^2+8y+4z-\lambda(y^2-x^2-z^2-3)$. The system:
> $$
> 2x+2\lambda x=0,\qquad 8-2\lambda y=0,\qquad 4+2\lambda z=0,\qquad y^2-x^2-z^2=3 .
> $$
> From the second, $\lambda\ne0$ and $y=\frac4\lambda$; from the third, $z=-\frac2\lambda$; the first: $2x(1+\lambda)=0$.
>
> - $x=0$: $\frac{16}{\lambda^2}-\frac4{\lambda^2}=3$, $\lambda^2=4$. The points $(0;2;-1)$ with $\lambda=2$ and $(0;-2;1)$ with $\lambda=-2$.
> - $\lambda=-1$: $y=-4$, $z=2$, $x^2=16-4-3=9$. The points $(\pm3;-4;2)$.
>
> $\varphi_x=-2x$, $\varphi_y=2y$, $\varphi_z=-2z$; $\mathcal L_{xx}=2+2\lambda$, $\mathcal L_{yy}=-2\lambda$, $\mathcal L_{zz}=2\lambda$.
> $$
> \Delta_3=8\lambda x^2-8(1+\lambda)y^2,\qquad \Delta_4=16\lambda^2x^2-16\lambda(1+\lambda)y^2+16\lambda(1+\lambda)z^2 .
> $$
>
> | Point | $\lambda$ | $\Delta_3$ | $\Delta_4$ | Conclusion | $f$ |
> |---|---|---|---|---|---|
> | $(0;2;-1)$ | $2$ | $-96$ | $-288$ | minimum | $12$ |
> | $(0;-2;1)$ | $-2$ | $32$ | $-96$ | maximum | $-12$ |
> | $(3;-4;2)$, $(-3;-4;2)$ | $-1$ | $-72$ | $144$ | no extremum | $-15$ |
>
> **Answer.** $(0;2;-1)$ is a point of constrained local minimum, $f=12$; $(0;-2;1)$ is a point of constrained local maximum, $f=-12$; at the points $(\pm3;-4;2)$ there is no extremum.
>
> **Why it works.** $M$ is a hyperboloid of two sheets ($y^2=3+x^2+z^2$, so $\lvert y\rvert\ge\sqrt3$); it is unbounded, and the compactness argument is not available — only the minors work. The minimum ($12$) is larger than the maximum ($-12$), and there is no contradiction: the extrema are local, and the points lie on different sheets of the hyperboloid ($y>0$ and $y<0$).

## Variant C

**1a.** Expand by Taylor's formula at the point $P=(2;1;-1)$ the function $f(x;y;z)=x^2z+xyz-y^3+2x$.

**1b.** Find the Taylor expansion of $f(x;y;z)=e^z\sin(x+2y)$ up to degree two at the point $P=\bigl(\frac\pi4;0;0\bigr)$ with the remainder in Lagrange form.

**2.** Find all points of constrained local extremum of $f(x;y;z)=6x+6y-3z^2$ on the set $M=\{(x;y;z)\in\mathbb R^3:\ x^2+y^2+z^2=18\}$.

> [!answer]- Solutions of variant C
> **1a.** Derivatives:
> $$
> D^{(1;0;0)}f=2xz+yz+2,\qquad D^{(0;1;0)}f=xz-3y^2,\qquad D^{(0;0;1)}f=x^2+xy;
> $$
> $$
> D^{(2;0;0)}f=2z,\quad D^{(1;1;0)}f=z,\quad D^{(1;0;1)}f=2x+y,\quad D^{(0;2;0)}f=-6y,\quad D^{(0;1;1)}f=x,\quad D^{(0;0;2)}f=0;
> $$
> $$
> D^{(2;0;1)}f=2,\qquad D^{(1;1;1)}f=1,\qquad D^{(0;3;0)}f=-6,
> $$
> the other third-order derivatives and all fourth-order ones are zero.
>
> At $P$: $f(P)=-4-2-1+4=-3$; first order: $-4-1+2=-3$, $-2-3=-5$, $4+2=6$; second order: $-2$, $-1$, $5$, $-6$, $2$, $0$. Second-order coefficients: $-1$, $-1$, $5$, $-3$, $2$; third-order: $\frac2{(2;0;1)!}=1$, $1$, $\frac{-6}{3!}=-1$.
>
> **Answer.** For all $(x;y;z)\in\mathbb R^3$
> $$
> \begin{aligned}f={}&-3-3(x-2)-5(y-1)+6(z+1)-(x-2)^2-(x-2)(y-1)+5(x-2)(z+1)-3(y-1)^2+2(y-1)(z+1)\\&+(x-2)^2(z+1)+(x-2)(y-1)(z+1)-(y-1)^3 .\end{aligned}
> $$
> Check: at the point $(2;1;0)$ the left side is $0+0-1+4=3$, the right side $-3+6=3$.
>
> **1b.** $f\in C^\infty(\mathbb R^3)$. Derivatives: first order — $e^z\cos(x+2y)$, $2e^z\cos(x+2y)$, $e^z\sin(x+2y)$; second order —
> $$
> D^{(2;0;0)}f=-e^z\sin(x+2y),\quad D^{(1;1;0)}f=-2e^z\sin(x+2y),\quad D^{(1;0;1)}f=e^z\cos(x+2y),
> $$
> $$
> D^{(0;2;0)}f=-4e^z\sin(x+2y),\quad D^{(0;1;1)}f=2e^z\cos(x+2y),\quad D^{(0;0;2)}f=e^z\sin(x+2y).
> $$
> At $P$: $\sin\frac\pi4=\cos\frac\pi4=\frac1{\sqrt2}$, $e^0=1$. Values: $f=\frac1{\sqrt2}$; first order $\frac1{\sqrt2}$, $\frac2{\sqrt2}$, $\frac1{\sqrt2}$; second order $-\frac1{\sqrt2}$, $-\frac2{\sqrt2}$, $\frac1{\sqrt2}$, $-\frac4{\sqrt2}$, $\frac2{\sqrt2}$, $\frac1{\sqrt2}$.
>
> **Answer.** For every $(x;y;z)$ there is $t_0\in(0;1)$:
> $$
> \begin{aligned}e^z\sin(x+2y)={}&\frac1{\sqrt2}\Bigl[1+\bigl(x-\tfrac\pi4\bigr)+2y+z-\tfrac12\bigl(x-\tfrac\pi4\bigr)^2-2\bigl(x-\tfrac\pi4\bigr)y+\bigl(x-\tfrac\pi4\bigr)z-2y^2+2yz+\tfrac12z^2\Bigr]\\&+\sum_{|\alpha|=3}\frac{D^{\alpha}f\bigl(\frac\pi4+t_0(x-\frac\pi4);\ t_0y;\ t_0z\bigr)}{\alpha!}\,\bigl(x-\tfrac\pi4\bigr)^{\alpha_1}y^{\alpha_2}z^{\alpha_3}.\end{aligned}
> $$
> Check: $\sin\bigl(\frac\pi4+w\bigr)=\frac1{\sqrt2}\bigl(1+w-\frac{w^2}2+\dots\bigr)$ with $w=(x-\frac\pi4)+2y$, and $e^z=1+z+\frac{z^2}2+\dots$; their product up to degree two gives the same bracket.
>
> **2.** $\mathcal L=6x+6y-3z^2-\lambda(x^2+y^2+z^2-18)$. The system:
> $$
> 6-2\lambda x=0,\qquad 6-2\lambda y=0,\qquad -6z-2\lambda z=0,\qquad x^2+y^2+z^2=18 .
> $$
> From the first two, $\lambda\ne0$ and $x=y=\frac3\lambda$; the third: $-2z(3+\lambda)=0$.
>
> - $z=0$: $\frac9{\lambda^2}+\frac9{\lambda^2}=18$, $\lambda=\pm1$. The points $(3;3;0)$ with $\lambda=1$ and $(-3;-3;0)$ with $\lambda=-1$.
> - $\lambda=-3$: $x=y=-1$, $z^2=18-2=16$. The points $(-1;-1;\pm4)$.
>
> $\varphi_x=2x$, $\varphi_y=2y$, $\varphi_z=2z$; $\mathcal L_{xx}=\mathcal L_{yy}=-2\lambda$, $\mathcal L_{zz}=-6-2\lambda$.
> $$
> \Delta_3=8\lambda(x^2+y^2),\qquad \Delta_4=-16\lambda(\lambda+3)(x^2+y^2)-16\lambda^2z^2 .
> $$
>
> | Point | $\lambda$ | $\Delta_3$ | $\Delta_4$ | Conclusion | $f$ |
> |---|---|---|---|---|---|
> | $(3;3;0)$ | $1$ | $144$ | $-1152$ | maximum | $36$ |
> | $(-3;-3;0)$ | $-1$ | $-144$ | $576$ | no extremum | $-36$ |
> | $(-1;-1;4)$, $(-1;-1;-4)$ | $-3$ | $-48$ | $-2304$ | minimum | $-60$ |
>
> **Answer.** $(3;3;0)$ is a point of constrained local maximum, $f=36$; $(-1;-1;\pm4)$ are points of constrained local minimum, $f=-60$; at $(-3;-3;0)$ there is no extremum.
>
> **Why it works.** Here it is the equation in $z$ that factorises, not the one in $x$ — look for where it is convenient. At $(-3;-3;0)$ the function $6(x+y)$ is minimal along the circle $z=0$, while moving in $z$ the term $-3z^2$ decreases it — hence a saddle.

## What each variant tests

| Problem | Variant A | Variant B | Variant C |
|---|---|---|---|
| 1a | degree 3 in three variables, the mixed $D^{(1;1;1)}f$ | degree 4 in two variables | degree 3 in three variables, $D^{(2;0;1)}f$ and $D^{(1;1;1)}f$ |
| 1b | an exponential and the sine of a product | a logarithm: the domain and the segment $[P;X]$ | the point $\frac\pi4$, values $\pm\frac1{\sqrt2}$ |
| 2 | an ellipsoid; the cases $x=0$ and $\lambda=1$; two maxima | a hyperboloid of two sheets, not compact; the minimum is larger than the maximum | a sphere; the factor in $z$; two minima |

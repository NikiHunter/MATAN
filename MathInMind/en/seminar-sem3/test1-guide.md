---
title: "Seminar NM-204. Test of 20 Nov — how to prepare"
lang: en
---
# Test of 20 November 2026: Taylor's formula and constrained extrema

[Русский](../../ru/seminar-sem3/test1-guide.md) · **English** · [Español](../../es/seminar-sem3/test1-guide.md)

[All assignments](index.md) · [Seminar notes](index.md#seminar-notes) · [Practice variants →](test1-variants.md) · [Series test](series-test-guide.md)

> **What this is.** Preparation for the test of 20 November 2026, based on the consultation. The format is now known: problem 1 (a — a polynomial, b — a non-polynomial function with the Lagrange remainder) and problem 2 (a constrained extremum). Sources: the board frames of the consultation and a summary of its audio recording ([`sem3_notes`, files 14](../../../sem3_notes/README.md), in Russian), the [seminar notes](index.md#seminar-notes) and homework 1–2. All computations below were checked in sympy. There will be no series on this test: they were moved to a separate test, which has [its own page](series-test-guide.md).

<a id="format"></a>
## What will be on the test

| Problem | What is given | What to do | Models |
|---|---|---|---|
| 1a | a polynomial: degree 4 in two variables **or** degree 3 in three; a point $`P`$ | expand it by Taylor's formula at $`P`$ completely; there is no remainder | [Example 1'.1](#ex-1p-1), HW [1.1](hw1-taylor.md#p-1-1), [1.2](hw1-taylor.md#p-1-2) |
| 1b | a non-polynomial $`f\colon\mathbb R^3\to\mathbb R`$ (sine, cosine, exponential, logarithm, powers); a point $`P`$ | the expansion up to order two with the remainder in Lagrange form; the remainder in general form | [Example 1'.2](#ex-1p-2), HW [1.4](hw1-taylor.md#p-1-4) |
| 2 | $`f\colon\mathbb R^3\to\mathbb R`$, a set $`M=\{\varphi=0\}`$ given by one polynomial condition | find all points of constrained local extremum and say for each: maximum, minimum or no extremum | [Example 1'.3](#ex-1p-3), HW [2.1](hw2-conditional-extremum.md#p-2-1) |

**What the instructor promised** (according to the recording of the consultation):

- in problem 2 all minors to be checked are non-zero — there will be no "the determinant is zero, further investigation needed" case;
- problem 2 deliberately contains a maximum, a minimum and a point with no extremum: if all your points came out as extrema, look for a mistake;
- there will be no cubic equations for $`\lambda`$, only quadratic ones or simpler (Example 1'.3 had a cubic, with the root $`\lambda=1`$ chosen on purpose);
- in problem 1b the explicit form of the third-order derivatives in the remainder is **not needed**; the remainder is written in general form;
- the values of sines and cosines will be simple: $`0`$, $`1`$ or $`\pm\frac1{\sqrt2}`$ (angles such as $`\frac\pi4`$, $`\frac{3\pi}4`$, $`\frac{5\pi}4`$);
- calculators are not allowed. The reasoning is marked: correct logic with one arithmetic slip gets almost full marks, while a solution its author cannot explain gets zero for the whole paper (an oral check is possible).

**What will not be there.** Series: the series problem of this test and that of the next one were combined into a separate test at the end of November or the beginning of December, together with the problem «on constant sign» that took a long time at the seminars ([how to prepare](series-test-guide.md)). Parameter integrals and the rest after series go into a small test at the end of December.

<a id="task-1"></a>
## Problem 1: Taylor's formula

**The formula in the board's notation.** For $`P=(p_1;p_2;p_3)`$, $`X=(x;y;z)`$ and $`f`$ continuously differentiable $`N+1`$ times (on the board, "$`f\in C^\infty(\mathbb R^3)`$"), for **every** point $`X`$ there is $`t_0=t_0(X)\in(0;1)`$ such that
```math
f(X)=\sum_{|\alpha|\le N}\frac{D^{\alpha}f(P)}{\alpha!}\,(X-P)^{\alpha}+\sum_{|\alpha|=N+1}\frac{D^{\alpha}f\bigl(P+t_0(X-P)\bigr)}{\alpha!}\,(X-P)^{\alpha}.
```
Here $`\alpha=(\alpha_1;\alpha_2;\alpha_3)`$ is a multi-index, $`|\alpha|=\alpha_1+\alpha_2+\alpha_3`$, $`\alpha!=\alpha_1!\,\alpha_2!\,\alpha_3!`$, $`(X-P)^{\alpha}=(x-p_1)^{\alpha_1}(y-p_2)^{\alpha_2}(z-p_3)^{\alpha_3}`$, and $`D^{\alpha}f`$ is the derivative taken $`\alpha_1`$ times in $`x`$, $`\alpha_2`$ times in $`y`$ and $`\alpha_3`$ times in $`z`$.

- Divide by $`\alpha!`$, not by $`|\alpha|!`$: for $`\alpha=(2;1;1)`$ it is $`2`$, not $`24`$. Pure second derivatives are divided by $`2`$, mixed ones such as $`D^{(1;1;0)}f`$ by $`1`$.
- Each multi-index enters the sum once; there is no need to count how many times a mixed derivative occurs — $`\alpha!`$ takes care of that. The form with differentials $`\frac{d^kf}{k!}`$ and coefficients $`\frac{k!}{\alpha!}`$ ([HW 1](hw1-taylor.md)) gives the same thing.
- List the multi-indices in order so as not to miss any: with three variables there are $`6`$ of order $`2`$ and $`10`$ of order $`3`$: $`(3;0;0)`$, $`(0;3;0)`$, $`(0;0;3)`$, $`(2;1;0)`$, $`(2;0;1)`$, $`(1;2;0)`$, $`(0;2;1)`$, $`(1;0;2)`$, $`(0;1;2)`$, $`(1;1;1)`$. With two variables there are $`k+1`$ of order $`k`$.
- First the derivatives at an **arbitrary** point, then substitute $`P`$. If you substitute the point earlier, there is nothing left to differentiate.

**Method for 1a (a polynomial).**

1. Find all derivatives up to the order equal to the degree of the polynomial, in general form.
2. Write down the non-zero ones and settle the rest in one sentence: "the other derivatives of order $`k`$ are zero".
3. Substitute $`P`$ showing the intermediate steps: $`20\cdot3^3-8\cdot3\cdot(-2)^2-2\cdot(-2)=448`$, not just $`448`$.
4. Divide by $`\alpha!`$ — a table is convenient — and assemble the answer.
5. Say why there is no remainder: the derivatives of order above the degree vanish identically, so the equality is exact for all $`X`$ and the Taylor series is a finite sum.
6. Check: the top homogeneous part of the answer coincides with the top part of $`f`$ (it does not change when the point moves), and one simple point, for example $`X=P+(1;0;0)`$, gives the same value on both sides.

**Method for 1b (a non-polynomial function).**

1. Derivatives up to order two in general form: $`f`$, three first-order and six second-order ones. Then their values at $`P`$.
2. The Taylor polynomial of order two: coefficients $`\frac{D^\alpha f(P)}{\alpha!}`$ for $`|\alpha|\le2`$.
3. The remainder **in general form**, with the intermediate point written out coordinatewise, as on the board:
```math
R_2(X)=\sum_{|\alpha|=3}\frac{D^{\alpha}f\bigl(p_1+t_0(x-p_1);\ p_2+t_0(y-p_2);\ p_3+t_0(z-p_3)\bigr)}{\alpha!}\,(x-p_1)^{\alpha_1}(y-p_2)^{\alpha_2}(z-p_3)^{\alpha_3},\qquad t_0\in(0;1).
```
4. Refer to the theorem: $`f`$ is infinitely (at least three times) continuously differentiable. If $`f`$ contains a logarithm or a root, state that the formula holds for those $`X`$ whose whole segment $`[P;X]`$ lies in the domain.

Do not find the explicit third-order derivatives: it is not a mistake, but it takes time away from problem 2.

<a id="ex-1p-1"></a>
### Example 1'.1 (consultation): a polynomial of degree four

**Statement.** $`f(x;y)=5x^4-4x^2y^2+3y^4-2xy+1`$. Expand it into a (finite) Taylor series at the point $`P=(3;-2)`$. This is the polynomial of [problem 1.2](hw1-taylor.md#p-1-2) of HW 1, where the point is $`(-3;2)`$.

**Derivatives at an arbitrary point.**
```math
D^{(1;0)}f=20x^3-8xy^2-2y,\qquad D^{(0;1)}f=-8x^2y+12y^3-2x;
```
```math
D^{(2;0)}f=60x^2-8y^2,\qquad D^{(1;1)}f=-16xy-2,\qquad D^{(0;2)}f=-8x^2+36y^2;
```
```math
D^{(3;0)}f=120x,\qquad D^{(2;1)}f=-16y,\qquad D^{(1;2)}f=-16x,\qquad D^{(0;3)}f=72y;
```
```math
D^{(4;0)}f=120,\qquad D^{(2;2)}f=-16,\qquad D^{(0;4)}f=72,\qquad D^{(3;1)}f=D^{(1;3)}f=0;
```
the fifth-order derivatives are zero.

**Values and coefficients.** $`f(P)=5\cdot3^4-4\cdot3^2\cdot(-2)^2+3\cdot(-2)^4-2\cdot3\cdot(-2)+1=405-144+48+12+1=322`$.

| Order | $`D^\alpha f(P)`$ | $`\frac{D^\alpha f(P)}{\alpha!}`$ |
|---|---|---|
| 1 | $`D^{(1;0)}=540-96+4=448`$, $`D^{(0;1)}=144-96-6=42`$ | $`448`$, $`42`$ |
| 2 | $`D^{(2;0)}=508`$, $`D^{(1;1)}=94`$, $`D^{(0;2)}=72`$ | $`254`$, $`94`$, $`36`$ |
| 3 | $`D^{(3;0)}=360`$, $`D^{(2;1)}=32`$, $`D^{(1;2)}=-48`$, $`D^{(0;3)}=-144`$ | $`60`$, $`16`$, $`-24`$, $`-24`$ |
| 4 | $`D^{(4;0)}=120`$, $`D^{(2;2)}=-16`$, $`D^{(0;4)}=72`$ | $`5`$, $`-4`$, $`3`$ |

**Answer.** For all $`(x;y)\in\mathbb R^2`$
```math
\begin{aligned}f(x;y)={}&322+448(x-3)+42(y+2)+254(x-3)^2+94(x-3)(y+2)+36(y+2)^2\\&+60(x-3)^3+16(x-3)^2(y+2)-24(x-3)(y+2)^2-24(y+2)^3\\&+5(x-3)^4-4(x-3)^2(y+2)^2+3(y+2)^4 .\end{aligned}
```

**Why it works.** The top part $`5(x-3)^4-4(x-3)^2(y+2)^2+3(y+2)^4`$ repeats the top part of $`f`$. In an intermediate line the board had $`\frac{42}{(0;2)!}(y+2)^2`$ — a slip: $`D^{(0;2)}f(P)=72`$, the coefficient is $`36`$, as in the board's final answer. Since $`f(-x;-y)=f(x;y)`$, the answer of HW 1.2 at $`(-3;2)`$ differs only in the signs of the odd-degree terms.

<a id="ex-1p-2"></a>
### Example 1'.2 (consultation): $`x^2e^{xy}+y\sin(yz^2)`$

**Statement.** Expand $`f(x;y;z)=x^2e^{xy}+y\sin(yz^2)`$ at $`P=(2;0;1)`$ with the remainder in Lagrange form. At the consultation it was done up to order three; the test asks for order two, so the answer in the test format comes first.

**Derivatives up to order two** at an arbitrary point:
```math
D^{(1;0;0)}f=(x^2y+2x)e^{xy},\qquad D^{(0;1;0)}f=x^3e^{xy}+\sin(yz^2)+yz^2\cos(yz^2),\qquad D^{(0;0;1)}f=2y^2z\cos(yz^2);
```
```math
D^{(2;0;0)}f=(x^2y^2+4xy+2)e^{xy},\qquad D^{(1;1;0)}f=(x^3y+3x^2)e^{xy},\qquad D^{(1;0;1)}f=0;
```
```math
D^{(0;2;0)}f=x^4e^{xy}+2z^2\cos(yz^2)-yz^4\sin(yz^2),\qquad D^{(0;1;1)}f=4yz\cos(yz^2)-2y^2z^3\sin(yz^2),\qquad D^{(0;0;2)}f=2y^2\cos(yz^2)-4y^3z^2\sin(yz^2).
```
**At $`P`$** ($`e^0=1`$, $`\sin0=0`$, $`\cos0=1`$): $`f(P)=4`$; $`D^{(1;0;0)}f(P)=4`$, $`D^{(0;1;0)}f(P)=8`$, $`D^{(0;0;1)}f(P)=0`$; $`D^{(2;0;0)}f(P)=2`$, $`D^{(1;1;0)}f(P)=12`$, $`D^{(0;2;0)}f(P)=16+2=18`$, the other second-order ones are zero.

**Answer up to order two (the test format).** $`f\in C^\infty(\mathbb R^3)`$, so for every $`(x;y;z)\in\mathbb R^3`$ there is $`t_0\in(0;1)`$ such that
```math
f(x;y;z)=4+4(x-2)+8y+(x-2)^2+12(x-2)y+9y^2+\sum_{|\alpha|=3}\frac{D^{\alpha}f\bigl(2+t_0(x-2);\ t_0y;\ 1+t_0(z-1)\bigr)}{\alpha!}\,(x-2)^{\alpha_1}y^{\alpha_2}(z-1)^{\alpha_3}.
```
Coefficients: $`\frac{2}{(2;0;0)!}=1`$, $`\frac{12}{(1;1;0)!}=12`$, $`\frac{18}{(0;2;0)!}=9`$.

**Up to order three (as at the consultation).** The non-zero third-order derivatives at $`P`$ are $`D^{(0;3;0)}f(P)=32`$, $`D^{(2;1;0)}f(P)=12`$, $`D^{(1;2;0)}f(P)=32`$, $`D^{(0;2;1)}f(P)=4`$. The polynomial gains the terms
```math
\frac{16}{3}y^3+6(x-2)^2y+16(x-2)y^2+2y^2(z-1),
```
and the remainder becomes a sum over $`|\alpha|=4`$. The board's line for $`D^{(0;1;2)}f`$ is wrong: the correct one is $`4y(1-y^2z^4)\cos(yz^2)-14y^2z^2\sin(yz^2)`$; at $`P`$ it is $`0`$ anyway.

**Why it works.** Almost everything vanished because $`y=0`$. The instructor warned that the point on the test will be "fairer": values $`\pm\frac1{\sqrt2}`$ are possible, and then the coefficients contain $`\sqrt2`$ (as in [variant C](test1-variants.md#variant-c)).

<a id="task-2"></a>
## Problem 2: constrained extremum

**The scheme (as at the consultation).**

1. **The Lagrange function:** $`\mathcal L(x;y;z;\lambda)=f(x;y;z)-\lambda\,\varphi(x;y;z)`$, where $`M=\{\varphi=0\}`$. The sign in front of $`\lambda`$ does not matter: the seminar of 9 September used "plus", the consultation "minus". Changing the sign only changes the sign of $`\lambda`$, and the matrix $`\widetilde H`$ at a stationary point stays the same.
2. **Stationary points of $`\mathcal L`$:** all four first-order partial derivatives vanish; the fourth equation is the condition $`\varphi=0`$ itself.
3. **Solve the system.** There is no general method; the problems are chosen so that they can be solved. The usual move: the equation in one variable factorises ($`6x(1-\lambda x)=0`$) — treat both cases; express the other variables through $`\lambda`$ and substitute them into the condition — this gives an equation for $`\lambda`$. Prove $`\lambda\ne0`$ first (usually "otherwise $`2=0`$"), and only then divide. Dropping $`\lambda`$ gives the candidate points in $`\mathbb R^3`$.
4. **The bordered Hessian** at an arbitrary point; the border goes into the first row and the first column, as on the board:
```math
\widetilde H=\begin{pmatrix}0&\varphi_x&\varphi_y&\varphi_z\\ \varphi_x&\mathcal L_{xx}&\mathcal L_{xy}&\mathcal L_{xz}\\ \varphi_y&\mathcal L_{xy}&\mathcal L_{yy}&\mathcal L_{yz}\\ \varphi_z&\mathcal L_{xz}&\mathcal L_{yz}&\mathcal L_{zz}\end{pmatrix}.
```
5. **Minors.** For $`n=3`$, $`m=1`$ one checks $`n-m=2`$ leading minors: $`\Delta_3`$ — the top-left $`3\times3`$ (border, $`x`$, $`y`$) — and $`\Delta_4=\det\widetilde H`$. First in general form, then substitute each point together with its $`\lambda`$.
6. **Conclusion** from the table.

| $`\Delta_3`$ | $`\Delta_4`$ | Conclusion |
|---|---|---|
| $`<0`$ | $`<0`$ | constrained local minimum: both signs equal $`(-1)^m=-1`$ |
| $`>0`$ | $`<0`$ | constrained local maximum: the signs alternate, starting with $`(-1)^{m+1}=+1`$ |
| $`<0`$ | $`>0`$ | no extremum |
| $`>0`$ | $`>0`$ | no extremum |

This is [Theorem 3.1](notes-1-taylor-extremum.md#thm-3-1) with $`n=3`$, $`m=1`$. The theorem does not cover $`\Delta_k=0`$, but this case will not occur on the test: a zero is a reason to recheck the arithmetic.

**Quick formulas.** If $`f`$ and $`\varphi`$ are sums of functions of single variables (as in all the examples below), there are no mixed derivatives: $`\mathcal L_{xy}=\mathcal L_{xz}=\mathcal L_{yz}=0`$. Expansion along the first row gives
```math
\Delta_3=-\bigl(\varphi_x^2\,\mathcal L_{yy}+\varphi_y^2\,\mathcal L_{xx}\bigr),\qquad
\Delta_4=-\bigl(\varphi_x^2\,\mathcal L_{yy}\mathcal L_{zz}+\varphi_y^2\,\mathcal L_{xx}\mathcal L_{zz}+\varphi_z^2\,\mathcal L_{xx}\mathcal L_{yy}\bigr).
```
On the test, better write out this line of the expansion rather than only its result.

**Careful: where the border goes.** If the gradient of $`\varphi`$ is written in the last row and the last column (as in some notes), the top-left minor of order three is the determinant of the block $`\mathcal L_{xx},\dots`$ without the border, and it gives a wrong answer: in Example 1'.3 it equals $`-216`$ at the maximum point, and the maximum "turns into" a minimum. In that layout $`\Delta_3`$ is the minor on the rows and columns of $`x`$, $`y`$ and the border. It is simpler to put the border first.

**A check without minors.** The minors encode the sign of $`d^2\mathcal L`$ on the tangent plane $`\{\varphi_x\,dx+\varphi_y\,dy+\varphi_z\,dz=0\}`$: positive definite — a minimum, negative definite — a maximum, indefinite — no extremum. If $`H_{\mathcal L}`$ is diagonal and all its entries have the same sign, the sign is visible at once.

<a id="ex-1p-3"></a>
### Example 1'.3 (consultation): $`3x^2+2y+6z`$ on $`2x^3+y^2+9z^2=4`$

**Statement.** Find all points of constrained local extremum of $`f(x;y;z)=3x^2+2y+6z`$ on the set $`M=\{(x;y;z)\in\mathbb R^3:\ 2x^3+y^2+9z^2=4\}`$. Here $`n=3`$, $`m=1`$.

**1. The Lagrange function.** $`\mathcal L=3x^2+2y+6z-\lambda\,(2x^3+y^2+9z^2-4)`$.

**2. The system.**
```math
\begin{cases}6x-6\lambda x^2=0,\\ 2-2\lambda y=0,\\ 6-18\lambda z=0,\\ 2x^3+y^2+9z^2=4.\end{cases}
```
From the second equation $`\lambda y=1`$, so $`\lambda\ne0`$ and $`y=\frac1\lambda`$; from the third $`z=\frac1{3\lambda}`$. The first one: $`6x(1-\lambda x)=0`$.

- *Case $`x=0`$.* The condition gives $`\frac1{\lambda^2}+9\cdot\frac1{9\lambda^2}=4`$, that is, $`\lambda^2=\frac12`$, $`\lambda=\pm\frac1{\sqrt2}`$. The points $`v^{(1)}=\bigl(0;-\sqrt2;-\frac{\sqrt2}3\bigr)`$ with $`\lambda=-\frac1{\sqrt2}`$ and $`v^{(2)}=\bigl(0;\sqrt2;\frac{\sqrt2}3\bigr)`$ with $`\lambda=\frac1{\sqrt2}`$.
- *Case $`x=\frac1\lambda`$.* The condition gives $`\frac2{\lambda^3}+\frac2{\lambda^2}=4`$, that is, $`2\lambda^3-\lambda-1=0`$. The root $`\lambda=1`$ is guessed, and $`2\lambda^3-\lambda-1=(\lambda-1)(2\lambda^2+2\lambda+1)`$ with $`2\lambda^2+2\lambda+1=2\bigl(\lambda+\frac12\bigr)^2+\frac12>0`$. The point $`v^{(3)}=\bigl(1;1;\frac13\bigr)`$ with $`\lambda=1`$. (There will be no cubic equations on the test.)

**3. The matrix and the minors.** $`\varphi_x=6x^2`$, $`\varphi_y=2y`$, $`\varphi_z=18z`$; $`\mathcal L_{xx}=6-12\lambda x`$, $`\mathcal L_{yy}=-2\lambda`$, $`\mathcal L_{zz}=-18\lambda`$, the mixed ones are zero.
```math
\widetilde H=\begin{pmatrix}0&6x^2&2y&18z\\6x^2&6-12\lambda x&0&0\\2y&0&-2\lambda&0\\18z&0&0&-18\lambda\end{pmatrix},
```
```math
\Delta_3=72\lambda x^4-4y^2(6-12\lambda x),\qquad
\Delta_4=-1296\lambda^2x^4+72\lambda(6-12\lambda x)\,y^2+648\lambda(6-12\lambda x)\,z^2 .
```

**4. Signs.**

| Point | $`\lambda`$ | $`\Delta_3`$ | $`\Delta_4`$ | Conclusion | $`f`$ |
|---|---|---|---|---|---|
| $`v^{(1)}=\bigl(0;-\sqrt2;-\frac{\sqrt2}3\bigr)`$ | $`-\frac1{\sqrt2}`$ | $`-48`$ | $`-864\sqrt2`$ | minimum | $`-4\sqrt2`$ |
| $`v^{(2)}=\bigl(0;\sqrt2;\frac{\sqrt2}3\bigr)`$ | $`\frac1{\sqrt2}`$ | $`-48`$ | $`864\sqrt2`$ | no extremum | $`4\sqrt2`$ |
| $`v^{(3)}=\bigl(1;1;\frac13\bigr)`$ | $`1`$ | $`96`$ | $`-2160`$ | maximum | $`7`$ |

For example, at $`v^{(1)}`$: $`x=0`$, $`6-12\lambda x=6`$, $`y^2=2`$, $`z^2=\frac29`$, so $`\Delta_3=-4\cdot2\cdot6=-48`$ and $`\Delta_4=72\cdot\bigl(-\frac1{\sqrt2}\bigr)\cdot6\cdot2+648\cdot\bigl(-\frac1{\sqrt2}\bigr)\cdot6\cdot\frac29=-\frac{864}{\sqrt2}-\frac{864}{\sqrt2}=-864\sqrt2`$.

**Answer.** $`\bigl(0;-\sqrt2;-\frac{\sqrt2}3\bigr)`$ is a point of constrained local minimum, $`f=-4\sqrt2`$; $`\bigl(1;1;\frac13\bigr)`$ is a point of constrained local maximum, $`f=7`$; at $`\bigl(0;\sqrt2;\frac{\sqrt2}3\bigr)`$ there is no extremum. The sign check is not on the consultation frames; it was recomputed here.

**Why it works.** At $`v^{(1)}`$ the matrix $`H_{\mathcal L}=\operatorname{diag}(6;\sqrt2;9\sqrt2)`$ is positive definite on the whole of $`\mathbb R^3`$, at $`v^{(3)}`$ the matrix $`\operatorname{diag}(-6;-2;-18)`$ is negative definite — the minors confirm this. At $`v^{(2)}`$ the tangent plane is given by $`dy=-3\,dz`$, and on it $`d^2\mathcal L=6\,dx^2-18\sqrt2\,dz^2`$ takes both signs. The set $`M`$ is unbounded ($`x\to-\infty`$ is allowed), so the argument "the greatest value is attained on a compact set" does not work here — the minors are needed.

## Typical mistakes

**Problem 1.**

- Dividing by $`|\alpha|!`$ instead of $`\alpha!`$; a forgotten division by $`2`$ for pure second derivatives or an extra one for mixed derivatives.
- The point substituted before differentiating.
- The remainder written at $`P`$ instead of the intermediate point; $`t_0\in(0;1)`$ not stated; the quantifiers swapped ("$`\exists\,t_0`$ for all $`X`$" instead of "for every $`X`$ there is $`t_0`$").
- A remainder written in problem 1a, or no explanation of why there is none.
- Numbers without intermediate steps: the marker cannot see where they came from.

**Problem 2.**

- A case lost when factorising: $`x=0`$ **or** $`1-\lambda x=0`$.
- Dividing by $`\lambda`$ without proving $`\lambda\ne0`$.
- The border in the last row and the "top-left minor" — a wrong $`\Delta_3`$.
- The sign rule for unconstrained extrema ("all minors positive — a minimum") instead of the rule with $`(-1)^m`$.
- A stationary point declared an extremum without a check; the answer does not say that a point has no extremum.

<a id="seminar-notes"></a>
## What to review in the seminar notes

The [notes](index.md#seminar-notes) show the form in which the theory was given at the seminar. At the test it is sensible to write in the same notation: $`D^\alpha f`$ and $`\alpha!`$, the intermediate point $`P+t_0(X-P)`$, the bordered Hessian with the border first.

| Problem | What to review | Where |
|---|---|---|
| 1a | Taylor's formula with multi-indices; why the remainder of a polynomial is zero | [Example 2.2](notes-1-taylor-extremum.md#ex-2-2), [Example 1'.1](#ex-1p-1) |
| 1b | the table of derivatives, the factors $`\frac1{\alpha!}`$, the remainder at $`u+t_0h`$ | [Example 4.1](notes-1-taylor-extremum.md#ex-4-1), [Remark 2.1](notes-1-taylor-extremum.md#rem-2-1), [Example 1'.2](#ex-1p-2) |
| 2 | the statement of the theorem and the sign table of the minors | [Theorem 3.1](notes-1-taylor-extremum.md#thm-3-1), [Example 3.2](notes-1-taylor-extremum.md#ex-3-2) |
| 2 | the bordered Hessian in examples: $`n=2`$; $`n=4`$, $`m=2`$; $`n=3`$, $`m=1`$, as on the test | [Example 4.2](notes-1-taylor-extremum.md#ex-4-2), [Example 5.1](notes-1-taylor-extremum.md#ex-5-1), [Example 1'.3](#ex-1p-3) |

## Preparation plan (16–19 November)

**Day 1 — Taylor.**

1. Read the section ["Problem 1"](#task-1) and "The general idea" in [HW 1](hw1-taylor.md).
2. Without looking at the solutions, expand Example 1'.1 and HW 1.2 (the answers differ in the signs of the odd terms — a good check).
3. Example 1'.2 and HW 1.4 up to order two, the remainder in general form only.

**Day 2 — constrained extremum.**

1. Read [Theorem 3.1](notes-1-taylor-extremum.md#thm-3-1) and the section ["Problem 2"](#task-2); derive the quick formulas for $`\Delta_3`$, $`\Delta_4`$ yourself.
2. Solve Example 1'.3 completely, with the minors, without looking at the solution.
3. As a warm-up, HW 2.1 by the bordered Hessian ($`n=2`$, one minor).

**Day 3 — practice variants.** [Variant A](test1-variants.md#variant-a) against the clock, without a calculator (aim for an hour and a half; check the actual length of the test), then check against the solutions; then [variant B](test1-variants.md#variant-b).

**Day 4 — a run-through.** [Variant C](test1-variants.md#variant-c) against the clock; go over the mistakes of all three variants; answer the self-check questions below.

## Self-check before the test

1. What is $`(2;0;1)!`$, and what is $`D^{(1;1;1)}f(P)`$ divided by in Taylor's formula?
2. How many multi-indices $`\alpha`$ with $`|\alpha|=3`$ does a function of three variables have? And with $`|\alpha|=2`$?
3. Why is there no remainder in problem 1a?
4. How is the intermediate point of the remainder written for $`P=(2;0;1)`$?
5. Why can one not write "$`\exists\,t_0\in(0;1)`$: the equality holds for all $`(x;y;z)`$"?
6. How many minors of the bordered Hessian are checked for $`n=3`$, $`m=1`$, and of which orders?
7. The signs of $`(\Delta_3;\Delta_4)`$ are $`(+;-)`$. Conclusion? And $`(-;-)`$? And $`(-;+)`$?
8. The matrix was written with the border in the last row and column. Which minor of order three should be taken?
9. Does the answer change if one takes $`\mathcal L=f+\lambda\varphi`$ instead of $`f-\lambda\varphi`$?
10. All three stationary points came out as maxima. What to do?
11. What are $`\sin\frac{3\pi}4`$ and $`\cos\frac{5\pi}4`$?
12. When may one refer to the compactness of $`M`$ in problem 2, and what does it not replace?

<details>
<summary>Answers</summary>

1. $`(2;0;1)!=2!\cdot0!\cdot1!=2`$; $`D^{(1;1;1)}f(P)`$ is divided by $`(1;1;1)!=1`$.
2. $`10`$ and $`6`$.
3. The derivatives of order above the degree of the polynomial vanish identically, so the remainder is zero for every $`t_0`$ and the equality is exact.
4. $`\bigl(2+t_0(x-2);\ t_0y;\ 1+t_0(z-1)\bigr)`$, $`t_0\in(0;1)`$.
5. $`t_0`$ depends on the point: every point $`(x;y;z)`$ has its own.
6. Two: $`\Delta_3`$ and $`\Delta_4`$ (orders $`2m+1,\dots,n+m`$).
7. $`(+;-)`$ — a maximum, $`(-;-)`$ — a minimum, $`(-;+)`$ — no extremum.
8. The minor on the rows and columns of $`x`$, $`y`$ and the border, not the top-left one.
9. No: $`\lambda`$ changes sign, and $`\widetilde H`$ at the stationary point stays the same.
10. Recheck: the instructor promised that problem 2 has a maximum, a minimum and a point with no extremum.
11. $`\frac1{\sqrt2}`$ and $`-\frac1{\sqrt2}`$.
12. If $`M`$ is compact (a sphere, an ellipsoid), $`f`$ attains its greatest and least values on it, and they are among the stationary points. But this does not show that the other points are not extrema: a point with no extremum still needs the minors. In Example 1'.3 the set $`M`$ is not compact.
</details>

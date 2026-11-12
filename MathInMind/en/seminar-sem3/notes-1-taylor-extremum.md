---
title: "Seminar NM-204. Notes, part 1: Taylor's formula and conditional extrema"
lang: en
---
# Seminar notes, part 1: Taylor's formula and conditional extrema

[Русский](../../ru/seminar-sem3/notes-1-taylor-extremum.md) · **English** · [Español](../../es/seminar-sem3/notes-1-taylor-extremum.md)

[All homework and notes](index.md) · [Part 2: basics of series →](notes-2-series-basics.md)

> **What this is.** A reworked record of the seminars of 4, 9, 18 and 20 September 2026. It is based on the OCR transcription of the handwritten boards in [`sem3_notes`](../../../sem3_notes/README.md) (in Russian). Statement numbers are kept as on the board (2.1, 3.1, …) so that they match the teacher's references. Formal phrasing has been replaced by plain language, and every statement gets a "why it works" note and a link to the homework problem. All computations were checked in sympy. Recognition errors have been corrected and are listed [at the end of the page](#fixes).

| Date | What was covered | Homework |
|---|---|---|
| 4 Sep | [Remark 2.1](#rem-2-1) (segments), [Example 2.2](#ex-2-2) (Taylor for a polynomial), [Definition 2.3](#def-2-3) (conditional extremum) | [1.1](hw1-taylor.md#p-1-1) |
| 9 Sep | [Theorem 3.1](#thm-3-1) (bordered Hessian), [Example 3.2](#ex-3-2) | the method for all of [HW 2](hw2-conditional-extremum.md) |
| 18 Sep | [Example 4.1](#ex-4-1) (Taylor with remainder), [Example 4.2](#ex-4-2) (extremum on a line) | [1.4](hw1-taylor.md#p-1-4), [2.1](hw2-conditional-extremum.md#p-2-1) |
| 20 Sep | [Example 5.1](#ex-5-1) (extremum in $`\mathbb R^4`$, two constraints) | [2.3](hw2-conditional-extremum.md#p-2-3), the $`y^2`$ variant |

<a id="sem-09-04"></a>
## Seminar of 4 September: segments, Taylor's formula, conditional extrema

<a id="rem-2-1"></a>
### Remark 2.1. A segment is the set of convex combinations of its endpoints

**Claim.** If $`a<b`$, then $`[a;b]=\{\lambda a+(1-\lambda)b\mid 0\le\lambda\le1\}`$.

**Proof.** Inclusion "$`\subset`$": let $`a\le x\le b`$ and put $`\lambda=\frac{b-x}{b-a}`$. From $`a\le x\le b`$ we get $`0\le\lambda\le1`$, and
```math
\lambda a+(1-\lambda)b=b-\lambda(b-a)=b-(b-x)=x.
```
Inclusion "$`\supset`$": if $`x=\lambda a+(1-\lambda)b`$ with $`\lambda\in[0;1]`$, then $`x-a=(1-\lambda)(b-a)\ge0`$ and $`b-x=\lambda(b-a)\ge0`$. $`\blacksquare`$

**Why we need it.** In the multivariable Taylor formula the intermediate point lies on the segment $`[u;u+h]=\{u+th\mid t\in[0;1]\}`$. This is the same description through convex combinations of the endpoints (with $`\lambda=1-t`$). So the region where the formula is applied must contain the whole segment, for instance by being convex; that is exactly what [Theorem 3.1](#thm-3-1) assumes.

<a id="ex-2-2"></a>
### Example 2.2. Taylor's formula for $`x^3+y^3+z^3-3xyz`$ (= [Problem 1.1](hw1-taylor.md#p-1-1))

**Statement.** $`f(x;y;z)=x^3+y^3+z^3-3xyz`$. Expand it by Taylor's formula at $`(1;1;1)`$ and at $`(1;-1;2)`$.

**The formula.** For a point $`u\in\mathbb R^n`$, an increment $`h`$ and multi-indices $`\alpha=(\alpha_1,\dots,\alpha_n)`$,
```math
f(u+h)=\sum_{|\alpha|\le m}D^\alpha f(u)\,\frac{h^\alpha}{\alpha!}+R_m(h),\qquad h^\alpha=h_1^{\alpha_1}\cdots h_n^{\alpha_n},\quad \alpha!=\alpha_1!\cdots\alpha_n!,
```
```math
R_m(h)=\sum_{|\alpha|=m+1}D^\alpha f(u+t_0h)\,\frac{h^\alpha}{\alpha!}\quad\text{for some }t_0\in(0;1)\quad\text{(Lagrange form of the remainder)}.
```
For example, $`D^{(1;1;0)}f=f''_{xy}`$ and $`(1;1;0)!=1!\cdot1!\cdot0!=1`$.

**Derivatives.**
```math
f'_x=3x^2-3yz,\qquad f'_y=3y^2-3xz,\qquad f'_z=3z^2-3xy;
```
```math
f''_{xx}=6x,\quad f''_{yy}=6y,\quad f''_{zz}=6z,\quad f''_{xy}=-3z,\quad f''_{xz}=-3y,\quad f''_{yz}=-3x;
```
```math
f'''_{xxx}=f'''_{yyy}=f'''_{zzz}=6,\qquad f'''_{xyz}=-3.
```
All other third-order derivatives and all derivatives of order $`\ge4`$ vanish. Hence for $`m=3`$ the remainder $`R_3\equiv0`$ and the expansion is exact.

**The point $`(1;-1;2)`$**, $`h=(x-1;\,y+1;\,z-2)`$. Values: $`f=1-1+8+6=14`$; $`f'_x=9`$, $`f'_y=-3`$, $`f'_z=15`$; $`\frac{f''_{xx}}{2!}=3`$, $`\frac{f''_{yy}}{2!}=-3`$, $`\frac{f''_{zz}}{2!}=6`$, $`f''_{xy}=-6`$, $`f''_{xz}=3`$, $`f''_{yz}=-3`$. Result:
```math
f=14+9h_1-3h_2+15h_3+3h_1^2-3h_2^2+6h_3^2-6h_1h_2+3h_1h_3-3h_2h_3+h_1^3+h_2^3+h_3^3-3h_1h_2h_3.
```

**The point $`(1;1;1)`$** (not done on the board; the answer is from the homework): $`f(1;1;1)=0`$, all first derivatives vanish, and
```math
f=3\bigl(h_1^2+h_2^2+h_3^2-h_1h_2-h_1h_3-h_2h_3\bigr)+h_1^3+h_2^3+h_3^3-3h_1h_2h_3.
```

**Why it works.** A cubic polynomial has all fourth-order derivatives equal to zero, so the Lagrange remainder vanishes for every $`t_0`$. Here Taylor's formula is just the polynomial rewritten in powers of $`h`$. The cubic part $`h_1^3+h_2^3+h_3^3-3h_1h_2h_3`$ is the same at both points: it is the top-degree homogeneous part of $`f`$ itself, which a shift does not change.

<a id="def-2-3"></a>
### Definition 2.3. Conditional local extremum

Let $`f\colon\mathbb R^n\to\mathbb R`$ and let $`M\subset\mathbb R^n`$ be non-empty. A point $`u^{(0)}\in M`$ is a point of **conditional local minimum of $`f`$ on $`M`$** if there is $`r_0>0`$ such that $`f(u^{(0)})\le f(u)`$ for all $`u\in B_{r_0}(u^{(0)})\cap M`$. A **conditional local maximum** is defined in the same way with $`f(u^{(0)})\ge f(u)`$. Here $`B_r(u^{(0)})=\{v:\ \|v-u^{(0)}\|<r\}`$ is the Euclidean ball.

**Meaning.** The value at $`u^{(0)}`$ is compared only with values at points of $`M`$, not at all points of a neighbourhood. So a point can be a conditional extremum without being an ordinary one. In [Problem 2.1](hw2-conditional-extremum.md#p-2-1) the origin is a saddle of the function on the plane, but a maximum on the line $`y=x`$.

At the end of the seminar the exercise was: find the conditional extrema of $`x^2+y^2`$ on the line $`\frac xa+\frac yb=1`$, where $`a,b>0`$. Hint: the constraint is $`g_1(x;y)=\frac xa+\frac yb-1=0`$, and $`M`$ is a line. The solution is [Example 3.2](#ex-3-2).

> **In the margin.** The board mentioned E. Landau's "Foundations of Analysis" and the construction of the integers from pairs of natural numbers: $`(k_1;m_1)\sim(k_2;m_2)\iff k_1+m_2=k_2+m_1`$, where the pair $`(k;m)`$ stands for $`k-m`$. This is not part of the test material.

<a id="sem-09-09"></a>
## Seminar of 9 September: the theorem on conditional extrema

<a id="thm-3-1"></a>
### Theorem 3.1. Conditional extrema and the bordered Hessian

**Hypotheses.** $`m<n`$; $`D\subset\mathbb R^n`$ is a convex open region; $`f,g_1,\dots,g_m\in C^2(D)`$; $`M=\{x\in D:\ g_1(x)=\dots=g_m(x)=0\}`$; the point $`u\in M`$ is such that the gradients $`\nabla g_1(u),\dots,\nabla g_m(u)`$ are linearly independent.

**Lagrange function** (at the seminar, with a plus sign):
```math
\mathcal L(x;\lambda)=f(x)+\sum_{k=1}^m\lambda_kg_k(x),\qquad x\in\mathbb R^n,\ \lambda\in\mathbb R^m.
```

**The bordered Hessian** is an $`(m+n)\times(m+n)`$ matrix: the first $`m`$ rows and columns belong to the constraints, the next $`n`$ to the variables:
```math
\widetilde H(x;\lambda)=\begin{pmatrix}0_{m\times m}&J_g(x)\\ J_g(x)^{T}&H_{\mathcal L}(x;\lambda)\end{pmatrix},\qquad J_g=\Bigl(\frac{\partial g_k}{\partial x_j}\Bigr)_{m\times n},\qquad H_{\mathcal L}=\Bigl(\frac{\partial^2\mathcal L}{\partial x_i\,\partial x_j}\Bigr)_{n\times n}.
```
Let $`\Delta_k`$ be its leading principal minor of order $`k`$. Only the last $`n-m`$ minors are checked: $`\Delta_{2m+1},\dots,\Delta_{n+m}`$.

**Statements.**

1. *Necessary condition.* If $`u`$ is a point of conditional local extremum, then there is a unique $`\lambda^{(0)}\in\mathbb R^m`$ for which all $`n+m`$ partial derivatives of $`\mathcal L`$ vanish at $`(u;\lambda^{(0)})`$.
2. *Minimum.* If $`(u;\lambda)`$ is a stationary point of $`\mathcal L`$ and every minor $`\Delta_k`$, $`k=2m+1,\dots,n+m`$, has the sign $`(-1)^m`$, then $`u`$ is a point of conditional local minimum.
3. *Maximum.* If $`(u;\lambda)`$ is a stationary point of $`\mathcal L`$ and the minor $`\Delta_k`$ has the sign $`(-1)^{k-m}`$ for $`k=2m+1,\dots,n+m`$, then $`u`$ is a point of conditional local maximum. The signs alternate, starting from $`(-1)^{m+1}`$; the last minor has the sign $`(-1)^n`$.
4. *No extremum.* If $`(u;\lambda)`$ is a stationary point of $`\mathcal L`$, all $`\Delta_k\ne0`$ for $`k=2m+1,\dots,n+m`$, but neither item 2 nor item 3 holds, then $`u`$ is not a point of conditional extremum.

On item 4: if $`\Delta_{2m+1}`$ has the sign $`(-1)^m`$ but a later minor has the other sign, it is not a minimum; if $`\Delta_{2m+1}`$ has the sign $`(-1)^{m+1}`$ but the alternation breaks later, it is not a maximum.

**Sign cheat sheet.**

| Sizes | Minors | Minimum | Maximum |
|---|---|---|---|
| $`n=2`$, $`m=1`$ | $`\Delta_3=\det\widetilde H`$ | $`\Delta_3<0`$ | $`\Delta_3>0`$ |
| $`n=3`$, $`m=1`$ | $`\Delta_3`$, $`\Delta_4`$ | $`\Delta_3<0`$, $`\Delta_4<0`$ | $`\Delta_3>0`$, $`\Delta_4<0`$ |
| $`n=3`$, $`m=2`$ | $`\Delta_5`$ | $`\Delta_5>0`$ | $`\Delta_5<0`$ |
| $`n=4`$, $`m=2`$ | $`\Delta_5`$, $`\Delta_6`$ | $`\Delta_5>0`$, $`\Delta_6>0`$ | $`\Delta_5<0`$, $`\Delta_6>0`$ |

**Why it works.** The sufficient condition is the sign of the second differential $`d^2\mathcal L`$, not on all of $`\mathbb R^n`$ but only on the tangent subspace $`\{h:\ J_g(u)h=0\}`$ of dimension $`n-m`$. That is why there are exactly $`n-m`$ minors. Where the factor $`(-1)^m`$ comes from is visible in the Schur complement formula: if $`H_{\mathcal L}`$ is positive definite, then
```math
\det\widetilde H=\det H_{\mathcal L}\cdot\det\bigl(-J_gH_{\mathcal L}^{-1}J_g^{T}\bigr)=(-1)^m\det H_{\mathcal L}\cdot\det\bigl(J_gH_{\mathcal L}^{-1}J_g^{T}\bigr),
```
and both determinants on the right are positive. If $`\Delta_{n+m}=0`$, the theorem says nothing, and the function is examined directly, as in [Problem 2.3](hw2-conditional-extremum.md#p-2-3).

<a id="ex-3-2"></a>
### Example 3.2. $`x^2+y^2`$ on the line $`\frac xa+\frac yb=1`$

**Statement.** $`a,b>0`$, $`f(x;y)=x^2+y^2`$, $`M=\bigl\{(x;y):\ \frac xa+\frac yb=1\bigr\}`$. Find the points of conditional local extremum.

**Solution.** $`n=2`$, $`m=1`$, $`g_1=\frac xa+\frac yb-1`$; the gradient $`\nabla g_1=\bigl(\frac1a;\frac1b\bigr)`$ never vanishes, so the independence condition holds.
```math
\mathcal L=x^2+y^2+\lambda\Bigl(\frac xa+\frac yb-1\Bigr),\qquad\widetilde H=\begin{pmatrix}0&\frac1a&\frac1b\\ \frac1a&2&0\\ \frac1b&0&2\end{pmatrix}.
```
Stationary points of $`\mathcal L`$:
```math
2x+\frac\lambda a=0,\qquad 2y+\frac\lambda b=0,\qquad \frac xa+\frac yb=1.
```
The first two equations give $`x=-\frac{\lambda}{2a}`$, $`y=-\frac{\lambda}{2b}`$. Substituting into the third gives $`-\frac\lambda2\bigl(\frac1{a^2}+\frac1{b^2}\bigr)=1`$, so
```math
\lambda=-\frac{2a^2b^2}{a^2+b^2},\qquad x=\frac{ab^2}{a^2+b^2},\qquad y=\frac{a^2b}{a^2+b^2}.
```
The determinant does not depend on the point:
```math
\det\widetilde H=-\frac2{a^2}-\frac2{b^2}<0.
```
Its sign equals $`(-1)^m=-1`$, so by Theorem 3.1 this is a **conditional local minimum**, $`f_{\min}=\frac{a^2b^2}{a^2+b^2}`$.

**Why it works.** $`x^2+y^2`$ is the squared distance to the origin, so the problem asks for the point of the line closest to the origin. The value $`\frac{a^2b^2}{a^2+b^2}`$ is the squared distance from $`0`$ to the line. There is no maximum: $`f`$ is unbounded on the line. The equation $`\nabla\mathcal L=0`$ says that $`\nabla f\parallel\nabla g_1`$, that is, at the closest point the position vector is perpendicular to the line.

<a id="sem-09-18"></a>
## Seminar of 18 September: Problems 1.4 and 2.1

<a id="ex-4-1"></a>
### Example 4.1. $`x^2\sin(xy)\,e^{y+z}`$ at $`(-1;\pi;2)`$ (= [Problem 1.4](hw1-taylor.md#p-1-4))

**Statement.** $`f(x;y;z)=x^2\sin(xy)\,e^{y+z}\in C^\infty(\mathbb R^3)`$. Expand it by Taylor's formula up to degree two at $`u=(-1;\pi;2)`$, with the remainder in Lagrange form.

**Derivatives.**
```math
f'_x=\bigl(2x\sin(xy)+x^2y\cos(xy)\bigr)e^{y+z},\qquad f'_y=x^2\bigl(x\cos(xy)+\sin(xy)\bigr)e^{y+z},\qquad f'_z=f,
```
```math
f''_{xx}=\bigl(2\sin(xy)+4xy\cos(xy)-x^2y^2\sin(xy)\bigr)e^{y+z},\qquad f''_{yy}=x^2\bigl(2x\cos(xy)+(1-x^2)\sin(xy)\bigr)e^{y+z},
```
```math
f''_{xy}=\bigl(2x\sin(xy)+3x^2\cos(xy)+x^2y\cos(xy)-x^3y\sin(xy)\bigr)e^{y+z},\qquad f''_{xz}=f'_x,\qquad f''_{yz}=f'_y,\qquad f''_{zz}=f.
```

**Values at the point** (using $`\sin(-\pi)=0`$, $`\cos(-\pi)=-1`$), in units of $`e^{\pi+2}`$:

| $`f`$ | $`f'_x`$ | $`f'_y`$ | $`f'_z`$ | $`f''_{xx}`$ | $`f''_{yy}`$ | $`f''_{zz}`$ | $`f''_{xy}`$ | $`f''_{xz}`$ | $`f''_{yz}`$ |
|---|---|---|---|---|---|---|---|---|---|
| $`0`$ | $`-\pi`$ | $`1`$ | $`0`$ | $`4\pi`$ | $`2`$ | $`0`$ | $`-(\pi+3)`$ | $`-\pi`$ | $`1`$ |

**Answer.** With $`h=(x+1;\,y-\pi;\,z-2)`$,
```math
f(x;y;z)=e^{\pi+2}\Bigl(-\pi h_1+h_2+2\pi h_1^2+h_2^2-(\pi+3)h_1h_2-\pi h_1h_3+h_2h_3\Bigr)+R_2,
```
```math
R_2=\sum_{|\alpha|=3}D^\alpha f\bigl(-1+t_0h_1;\ \pi+t_0h_2;\ 2+t_0h_3\bigr)\,\frac{h^\alpha}{\alpha!},\qquad t_0\in(0;1).
```

**Why it works.** The quadratic terms carry the factor $`\frac1{\alpha!}`$. The coefficient of $`h_1^2`$ is $`\frac{f''_{xx}}{2!}=2\pi`$, not $`4\pi`$. The mixed term $`h_1h_2`$ gets $`f''_{xy}`$ itself, because $`(1;1;0)!=1`$. The remainder contains third-order derivatives at an intermediate point $`u+t_0h`$ of the segment $`[u;u+h]`$ ([Remark 2.1](#rem-2-1)). The explicit form of the remainder is written out in [Problem 1.4](hw1-taylor.md#p-1-4).

<a id="ex-4-2"></a>
### Example 4.2. $`x^3+y^3-3xy`$ on the line $`x=y`$ (= [Problem 2.1](hw2-conditional-extremum.md#p-2-1))

**Statement.** $`f(x;y)=x^3+y^3-3xy`$, $`M=\{(x;y):\ x=y\}`$. Find the points of conditional local extremum.

**Solution with the bordered Hessian.** $`n=2`$, $`m=1`$, $`g=x-y`$, $`\nabla g=(1;-1)\ne0`$.
```math
\mathcal L=x^3+y^3-3xy+\lambda(x-y),\qquad \widetilde H=\begin{pmatrix}0&1&-1\\ 1&6x&-3\\ -1&-3&6y\end{pmatrix},\qquad \det\widetilde H=6(1-x-y).
```
Stationary points: $`3x^2-3y+\lambda=0`$, $`3y^2-3x-\lambda=0`$, $`x=y`$. Hence $`\lambda=3x-3x^2`$ and $`\lambda=3x^2-3x`$, that is, $`6x(x-1)=0`$. We get the points $`(0;0)`$ and $`(1;1)`$, both with $`\lambda=0`$.

- $`(0;0)`$: $`\det\widetilde H=6>0`$, the sign $`(-1)^{3-1}=+1`$: a **conditional local maximum**, $`f=0`$.
- $`(1;1)`$: $`\det\widetilde H=-6<0`$, the sign $`(-1)^m=-1`$: a **conditional local minimum**, $`f=-1`$.

> **Tip from the seminar.** It is almost always easier to find the determinant of $`\widetilde H`$ at an arbitrary point first and only then substitute the stationary points.

**Why it works.** Substituting $`y=x`$ gives $`g(x)=2x^3-3x^2`$ with $`g''(x)=12x-6`$: $`g''(0)<0`$ and $`g''(1)>0`$, the same conclusions. That is how the homework solves it. The bordered Hessian is needed when the constraint cannot be solved explicitly. In connection with this method the board mentioned the notes of Keith Conrad.

<a id="sem-09-20"></a>
## Seminar of 20 September: a conditional extremum in $`\mathbb R^4`$

<a id="ex-5-1"></a>
### Example 5.1. $`x^3+y^2+z^3+2t^2`$ subject to $`x=y`$, $`z=t`$ (cf. [Problem 2.3](hw2-conditional-extremum.md#p-2-3))

> **Note: a variant of the statement.** The seminar solved the function with $`y^2`$. In HW 2, Problem 2.3 has $`y^3`$, and there the answer is different: there are no extrema ([solution](hw2-conditional-extremum.md#p-2-3)). The $`y^2`$ variant matches the short file of HW 3.

**Statement.** $`f(x;y;z;t)=x^3+y^2+z^3+2t^2`$, $`M=\{x=y,\ z=t\}`$. Find the points of conditional local extremum.

**Solution.** $`n=4`$, $`m=2`$, so $`\Delta_5`$ and $`\Delta_6`$ are checked. The constraints are $`g_1=x-y`$, $`g_2=z-t`$; their gradients $`(1;-1;0;0)`$ and $`(0;0;1;-1)`$ are linearly independent everywhere.
```math
\mathcal L=x^3+y^2+z^3+2t^2+\lambda_1(x-y)+\lambda_2(z-t),
```
```math
\widetilde H=\begin{pmatrix}0&0&1&-1&0&0\\0&0&0&0&1&-1\\1&0&6x&0&0&0\\-1&0&0&2&0&0\\0&1&0&0&6z&0\\0&-1&0&0&0&4\end{pmatrix}.
```
Stationary points:
```math
3x^2+\lambda_1=0,\quad 2y-\lambda_1=0,\quad 3z^2+\lambda_2=0,\quad 4t-\lambda_2=0,\quad x=y,\quad z=t.
```
Hence $`3x^2+2x=0`$ and $`3z^2+4z=0`$, that is, $`x\in\{0;-\frac23\}`$, $`z\in\{0;-\frac43\}`$; $`\lambda_1=-3x^2`$, $`\lambda_2=-3z^2`$. There are four points.

The minors are computed by expanding along rows and columns with few non-zero entries:
```math
\Delta_5=6x+2,\qquad\Delta_6=(6x+2)(6z+4).
```
For $`m=2`$ a minimum means $`\Delta_5>0`$, $`\Delta_6>0`$; a maximum means $`\Delta_5<0`$, $`\Delta_6>0`$.

| Point $`(x;y;z;t)`$ | $`\Delta_5`$ | $`\Delta_6`$ | Conclusion | $`f`$ |
|---|---|---|---|---|
| $`(0;0;0;0)`$ | $`2`$ | $`8`$ | minimum | $`0`$ |
| $`(-\frac23;-\frac23;0;0)`$ | $`-2`$ | $`-8`$ | no extremum | $`\frac4{27}`$ |
| $`(0;0;-\frac43;-\frac43)`$ | $`2`$ | $`-8`$ | no extremum | $`\frac{32}{27}`$ |
| $`(-\frac23;-\frac23;-\frac43;-\frac43)`$ | $`-2`$ | $`8`$ | maximum | $`\frac43`$ |

**Why it works.** On $`M`$ the function splits into a sum: $`f(x;x;z;z)=\varphi(x)+\psi(z)`$ with $`\varphi(x)=x^3+x^2`$, $`\psi(z)=z^3+2z^2`$. The minors show exactly this: $`\Delta_5=\varphi''(x)`$ and $`\Delta_6=\varphi''(x)\,\psi''(z)`$. We get a minimum when both summands are at a minimum, a maximum when both are at a maximum, and a minimum of one summand together with a maximum of the other gives a saddle. In the HW 2 variant with $`y^3`$ we get $`\varphi(x)=2x^3`$; at both stationary points $`\Delta_5=\Delta_6=0`$, the theorem is silent, and indeed there is no extremum.

<a id="fixes"></a>
## What was corrected compared with the OCR transcription

| Place | In the transcription | Correct |
|---|---|---|
| [3.1](#thm-3-1), definition of $`\widetilde H`$ | row numbers $`m+1\le k\le n`$ | $`m+1\le k\le n+m`$ |
| [3.2](#ex-3-2) | $`x=-\frac{2\lambda}{a}`$, $`\lambda=-\frac{a^2b^2}{2(a^2+b^2)}`$ | $`x=-\frac{\lambda}{2a}`$, $`\lambda=-\frac{2a^2b^2}{a^2+b^2}`$ (the point itself was right) |
| [4.1](#ex-4-1), answer | $`4\pi(x+1)^2+2(y-\pi)^2`$ | $`2\pi h_1^2+h_2^2`$: the factor $`\frac1{2!}`$ was forgotten |
| [4.1](#ex-4-1), formula for $`f''_{xy}`$ | it coincided with $`f'_x`$ | the formula above; the value $`-(\pi+3)e^{\pi+2}`$ was right |
| [4.2](#ex-4-2), statement | $`M=\{x=y^3\}`$ | $`M=\{x=y\}`$: the constraint is $`g=x-y`$, as in Problem 2.1 |
| [5.1](#ex-5-1), statement | $`2t^3`$ | $`2t^2`$: so in the Lagrange function and in the answer $`f=\frac43`$ |

[All homework and notes](index.md) · [Part 2: basics of series →](notes-2-series-basics.md)

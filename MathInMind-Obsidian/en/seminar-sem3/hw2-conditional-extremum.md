---
title: "Seminar NM-204. HW 2 — constrained extrema: solutions"
lang: en
hw: 2
tags: [mathinmind/en, mathinmind/other]
---
# HW 2. Constrained extrema — solutions

[[ru/seminar-sem3/hw2-conditional-extremum|Русский]] · **English** · [[es/seminar-sem3/hw2-conditional-extremum|Español]]

[[en/seminar-sem3/hw1-taylor|← HW 1]] · [[en/seminar-sem3/index|All assignments]] · [[en/seminar-sem3/hw3-numerical-series|HW 3 →]] · [[en/lectures-2025-26/lecture-67-68|Lectures 67–68, §6.7]]

This page solves problems 2.1–2.3 (HW 2) and 2'.1–2'.3 (the constrained-extremum series from HW 3). Problems 1.2 and 1.4, repeated in HW 2, are solved in [[en/seminar-sem3/hw1-taylor|HW 1]].

> [!note] Reference
> [[en/lectures-2025-26/lecture-67-68#^thm-6-7-4|Theorem 6.7.4]] (necessary condition): if $a$ is a point of constrained extremum of $f$ under the constraints $\varphi_1=\dots=\varphi_m=0$ and the gradients of the constraints at $a$ are linearly independent, then $\nabla f(a)=\sum_j\lambda_j\nabla\varphi_j(a)$. [[en/lectures-2025-26/lecture-67-68#^thm-6-7-5|Theorem 6.7.5]] (sufficient condition): the sign of $d^2L$ of the Lagrange function $L=f-\sum\lambda_j\varphi_j$ on the tangent space $\{h:\ d\varphi_j(h)=0\}$.

## Why the Lagrange method works

> [!note] At the seminar
> On 9 Sep the sufficient condition was stated through the bordered Hessian: [[en/seminar-sem3/notes-1-taylor-extremum#Theorem 3.1. Conditional extrema and the bordered Hessian|Theorem 3.1]], with a table of the signs of the minors. It is handy when the constraint cannot be solved explicitly.

On the set $M=\{\varphi=0\}$ not every displacement is allowed, only those tangent to $M$: the vectors $h$ with $d\varphi_j(h)=0$. At an extremum $f$ must not change to first order along allowed directions, that is, $df(h)=0$ for every tangent $h$. This means precisely that $\nabla f$ is orthogonal to the tangent space, i.e. lies in the span of the normals $\nabla\varphi_j$. The independence of the gradients is needed so that the tangent space really describes $M$ near the point ([[en/lectures-2025-26/lecture-65-66#^thm-6-6-1|implicit mapping theorem]]).

Three consequences used below.

- If the constraint can be solved explicitly (for example, $y=x$), the problem becomes an ordinary extremum problem in fewer variables. It is the same method: a parametrisation of $M$ instead of multipliers.
- The Lagrange condition is **necessary**. A stationary point still has to be examined: by the second differential, by a direct estimate, or by compactness (a continuous function on a compact set attains its greatest and least values, and those points must be among the stationary ones).
- If $d^2L$ is degenerate on the tangent space, the sufficient condition is silent and one has to look at the function itself (problems 2.3 and 2'.3).

## Problem 2.1

> [!note] At the seminar
> [[en/seminar-sem3/notes-1-taylor-extremum#^ex-4-2|Example 4.2]] (18 Sep): the same problem with the bordered Hessian, $\det\widetilde H=6(1-x-y)$.

**Statement.** $f(x,y)=x^3+y^3-3xy$, $M=\{x=y\}$. Find all points of constrained local extremum.

**Solution.** The line $M$ is parametrised as $(x,x)$, $x\in\mathbb R$, and this is a homeomorphism $\mathbb R\to M$. So the points of constrained extremum of $f$ on $M$ are exactly the points of local extremum of
$$
g(x)=f(x,x)=2x^3-3x^2 .
$$
$g'(x)=6x^2-6x=6x(x-1)$, zeros: $x=0$ and $x=1$. $g''(x)=12x-6$: $g''(0)=-6<0$ — a strict local maximum, $g''(1)=6>0$ — a strict local minimum.

*The same by the Lagrange method.* $\varphi=x-y$, $\nabla\varphi=(1,-1)\ne0$. System: $3x^2-3y=\lambda$, $3y^2-3x=-\lambda$, $x=y$. From the first two with $x=y$: $3x^2-3x=\lambda=-(3x^2-3x)$, so $\lambda=0$ and $x\in\{0,1\}$. The second differential $d^2L=6x\,dx^2-6\,dx\,dy+6y\,dy^2$ on tangent vectors $dx=dy$ equals $(12x-6)\,dx^2$ — the same sign as $g''$.

**Answer.** $(0;0)$ is a point of strict constrained local maximum, $f=0$; $(1;1)$ is a point of strict constrained local minimum, $f=-1$. There are no others.

**Why it works.** Both extrema are local, not global: $g(x)\to\pm\infty$ as $x\to\pm\infty$. It is instructive to compare with the unconstrained problem: $(1;1)$ is an unconstrained minimum of $f$, so it remains a minimum on any curve through it. But $(0;0)$ is a saddle of $f$ in the plane (the Hessian $\begin{pmatrix}0&-3\\-3&0\end{pmatrix}$ is indefinite), while along the line $x=y$ the form $-6\,dx\,dy$ equals $-6\,dx^2<0$: restricting to $M$ "selects" the direction along which the saddle looks like a maximum. A constrained extremum can appear where there is no unconstrained one.

## Problem 2.2

**Statement.** $a>0$, $f(x,y,z)=e^{x+2y+3z}$, $M=\{x^2+2y^2+3z^2=a\}$. Find all points of constrained local extremum.

**Solution.** The constraint is $\varphi=x^2+2y^2+3z^2-a$, and $\nabla\varphi=(2x,4y,6z)$ vanishes only at the origin, which does not lie on $M$ (since $a>0$). So the regularity condition holds everywhere on $M$, and every point of constrained extremum satisfies the Lagrange system. Put $u=x+2y+3z$; $\nabla f=e^u(1,2,3)$:
$$
e^u=2\lambda x,\qquad 2e^u=4\lambda y,\qquad 3e^u=6\lambda z .
$$
Since $e^u\ne0$, we get $\lambda\ne0$ and $x=y=z=\dfrac{e^u}{2\lambda}$. Substituting $x=y=z=t$ into the constraint: $6t^2=a$, $t=\pm\sqrt{a/6}$. There are two stationary points:
$$
P_\pm=\pm\sqrt{\frac a6}\,(1;1;1),\qquad u(P_\pm)=\pm6\sqrt{\frac a6}=\pm\sqrt{6a} .
$$
$M$ is an ellipsoid; it is closed and bounded, hence compact; $f$ is continuous, so it attains its greatest and least values on $M$. The points where they are attained are points of constrained extremum, so they are among $P_\pm$. Since $f(P_+)>f(P_-)$, the maximum is at $P_+$ and the minimum at $P_-$. There are no other points of constrained local extremum: any such point is stationary, and there are only two stationary points.

**Answer.** $P_+=\bigl(\sqrt{a/6};\sqrt{a/6};\sqrt{a/6}\bigr)$ is the point of constrained maximum, $f=e^{\sqrt{6a}}$; $P_-=-P_+$ is the point of constrained minimum, $f=e^{-\sqrt{6a}}$. Both extrema are strict and global on $M$.

**Why it works.** The exponential is strictly increasing, so the extrema of $f$ are the extrema of the linear function $u=x+2y+3z$ on the ellipsoid. Geometrically: the planes $u=\mathrm{const}$ are parallel, and the extremum is attained where a plane touches the ellipsoid, i.e. where the normal $(2x,4y,6z)$ to the ellipsoid is parallel to $(1,2,3)$ — which gives $x=y=z$. An independent check is the Cauchy–Schwarz inequality:
$$
(x+2y+3z)^2=\bigl(1\cdot x+\sqrt2\cdot\sqrt2y+\sqrt3\cdot\sqrt3z\bigr)^2\le(1+2+3)(x^2+2y^2+3z^2)=6a,
$$
with equality only when $x=y=z$. Strictness is visible from here too.

## Problem 2.3

> [!note] At the seminar
> [[en/seminar-sem3/notes-1-taylor-extremum#^ex-5-1|Example 5.1]] (20 Sep) solves the $y^2$ variant: a minimum at $(0;0;0;0)$, a maximum at $(-\frac23;-\frac23;-\frac43;-\frac43)$ and two saddle points.

**Statement.** $f(x,y,z,t)=x^3+y^3+z^3+2t^2$, $M=\{x=y,\ z=t\}$. Find all points of constrained local extremum.

**Solution.** $M$ is a two-dimensional plane; parametrise it as $(x,x,z,z)$, $(x,z)\in\mathbb R^2$. The problem is equivalent to finding the local extrema of
$$
g(x,z)=f(x,x,z,z)=2x^3+z^3+2z^2 .
$$
Necessary condition: $g_x=6x^2=0$, $g_z=3z^2+4z=0$, whence $x=0$ and $z\in\{0,-\tfrac43\}$. Stationary points: $(0,0)$ and $(0,-\tfrac43)$.

The Hessian of $g$ is $\operatorname{diag}(12x,\ 6z+4)$; at both points the first entry is zero, the form is only semi-definite, and the sufficient condition says nothing. Look at the function itself: for fixed $z=z_0$
$$
g(x,z_0)-g(0,z_0)=2x^3,
$$
which is positive for $x>0$ and negative for $x<0$. So in every neighbourhood of each of the two stationary points $g$ takes values both greater and smaller than at the point itself. There is no extremum.

**Answer.** There are no points of constrained local extremum. The stationary points of the Lagrange function are $(0;0;0;0)$ and $(0;0;-\tfrac43;-\tfrac43)$, but neither is an extremum.

**Why it works.** In the variable $z$ everything is "fine": $z^3+2z^2$ has a minimum at $z=0$ and a maximum at $z=-\frac43$. The term $2x^3$ spoils it: the stationary point of a cube is an inflection. An extremum of a function of several variables requires an extremum along every direction at once; one "bad" direction is enough. This is an example showing that the Lagrange equations do not guarantee an extremum.

> [!remark] Remark on a variant of the statement
> In the shortened HW 3 file the same problem is typeset with $y^2$ instead of $y^3$: $f=x^3+y^2+z^3+2t^2$. Then $g(x,z)=(x^3+x^2)+(z^3+2z^2)$, the stationary points are $x\in\{0,-\tfrac23\}$, $z\in\{0,-\tfrac43\}$, the Hessian is $\operatorname{diag}(6x+2,\ 6z+4)$, and the answer is different: $(0;0;0;0)$ is a strict constrained local minimum ($f=0$), $(-\tfrac23;-\tfrac23;-\tfrac43;-\tfrac43)$ is a strict constrained local maximum ($f=\tfrac4{27}+\tfrac{32}{27}=\tfrac43$), and $(0;0;-\tfrac43;-\tfrac43)$ and $(-\tfrac23;-\tfrac23;0;0)$ are saddles. The solution above follows HW 2, which has $y^3$. The seminar on 20 Sep worked out exactly the $y^2$ variant ([[en/seminar-sem3/notes-1-taylor-extremum#^ex-5-1|Example 5.1]]), so the $y^3$ in HW 2 may be a typo; worth checking with the teacher.

## Problem 2'.1

**Statement.** $f=xyz$, $M=\{x^2+y^2+z^2=1,\ x+y-z=0\}$. Find all points of constrained extremum and the extremal values.

**Solution.** *Regularity.* The gradients of the constraints $(2x,2y,2z)$ and $(1,1,-1)$ are linearly dependent only if $(x,y,z)=c\,(1,1,-1)$; then $x+y-z=3c=0$, i.e. the point is the origin, which is not on the sphere. So the rank is 2 everywhere on $M$.

*Lagrange system* with $L=xyz-\lambda(x^2+y^2+z^2-1)-\mu(x+y-z)$:
$$
yz=2\lambda x+\mu,\qquad xz=2\lambda y+\mu,\qquad xy=2\lambda z-\mu .
$$
Subtracting the second equation from the first: $z(y-x)=2\lambda(x-y)$, i.e. $(x-y)(z+2\lambda)=0$.

- If $x=y$, the constraints give $z=2x$ and $6x^2=1$: the points $\pm\frac1{\sqrt6}(1;1;2)$.
- If $z=-2\lambda$, add the first and third equations: $y(x+z)=2\lambda(x+z)=-z(x+z)$, i.e. $(x+z)(y+z)=0$. For $x=-z$ the plane gives $y=2z$, and $6z^2=1$: the points $\pm\frac1{\sqrt6}(-1;2;1)$. For $y=-z$ similarly $x=2z$: the points $\pm\frac1{\sqrt6}(2;-1;1)$.

Altogether six stationary points. Values of $f$:
$$
f=\frac{1}{3\sqrt6}=\frac{\sqrt6}{18}\ \text{ at the points }\ \tfrac1{\sqrt6}(1;1;2),\ \tfrac1{\sqrt6}(1;-2;-1),\ \tfrac1{\sqrt6}(-2;1;-1);
$$
$$
f=-\frac{1}{3\sqrt6}=-\frac{\sqrt6}{18}\ \text{ at the points }\ \tfrac1{\sqrt6}(-1;-1;-2),\ \tfrac1{\sqrt6}(-1;2;1),\ \tfrac1{\sqrt6}(2;-1;1).
$$
$M$ is a circle (a section of the sphere by a plane through the centre), a compact set. The greatest and least values of $f$ on $M$ are attained, and attained at stationary points, so they equal $\pm\frac1{3\sqrt6}$. Each of the six points is a point where $f$ equals its greatest or least value on $M$, i.e. a point of global (hence local) extremum.

**Answer.** The constrained maximum $f_{\max}=\dfrac{1}{3\sqrt6}$ is attained at the three points $\frac1{\sqrt6}(1;1;2)$, $\frac1{\sqrt6}(1;-2;-1)$, $\frac1{\sqrt6}(-2;1;-1)$; the constrained minimum $f_{\min}=-\dfrac{1}{3\sqrt6}$ at the three opposite points. There are no other points of constrained extremum.

**Why it works.** The substitution $w=-z$ makes the problem symmetric: the constraints $x+y+w=0$, $x^2+y^2+w^2=1$ and the function $-xyw$ are unchanged by permutations of $x,y,w$. Hence the "triples" of points. The circle can be parametrised explicitly:
$$
x=\sqrt{\tfrac23}\cos\varphi,\qquad y=\sqrt{\tfrac23}\cos\bigl(\varphi+\tfrac{2\pi}3\bigr),\qquad w=\sqrt{\tfrac23}\cos\bigl(\varphi-\tfrac{2\pi}3\bigr),
$$
and then the identity $\cos\varphi\cos(\varphi+\frac{2\pi}3)\cos(\varphi-\frac{2\pi}3)=\frac14\cos3\varphi$ gives
$$
f=-xyw=-\frac{\cos3\varphi}{3\sqrt6}.
$$
On the circle $f$ is just $\cos3\varphi$ up to a factor: three maxima and three minima alternate every $60^\circ$, and there can be no other extrema. Opposite points give opposite values because $f$ is odd and $M$ is symmetric about the origin.

## Problem 2'.2

**Statement.** $n,m\in\mathbb N$, $a>0$, $f_m(x)=\sum_{k=1}^nx_k^m$, $M=\{\sum_{k=1}^nx_k=a\}$. Find all points of constrained extremum and the extremal values.

**Solution.** The constraint is $\varphi=\sum x_k-a$, $\nabla\varphi=(1,\dots,1)\ne0$ — regular everywhere.

**Case $n=1$.** $M=\{a\}$ is a single point; formally it is a point of both maximum and minimum, with value $a^m$.

**Case $m=1$** (the trivial case from the hint). On $M$ the function is constant: $f_1=\sum x_k=a$. Every point of $M$ is a point of non-strict constrained maximum and minimum at once; the extremal value is $a$.

**Case $n\ge2$, $m\ge2$.** Lagrange system: $m\,x_k^{m-1}=\lambda$ for all $k$, i.e. **all the numbers $x_k^{m-1}$ are equal**.

*$m$ even.* Then $m-1$ is odd, the function $t\mapsto t^{m-1}$ is strictly increasing, so all $x_k$ are equal: $x_k=\frac an$. The only stationary point is $P=(\frac an,\dots,\frac an)$, $f_m(P)=n\bigl(\frac an\bigr)^m=\frac{a^m}{n^{m-1}}$. It is a global minimum: for even $m$ the function $t\mapsto t^m$ is convex on the whole line, and by Jensen's inequality
$$
\frac1n\sum_{k=1}^nx_k^m\ \ge\ \Bigl(\frac1n\sum_{k=1}^nx_k\Bigr)^m=\Bigl(\frac an\Bigr)^m,
$$
with equality only for equal $x_k$ (strict convexity). There is no maximum: at the points $(a+T,-T,0,\dots,0)\in M$ the value $(a+T)^m+T^m\to+\infty$ as $T\to+\infty$; and there are no other extremum points since the stationary point is unique.

*$m$ odd, $m\ge3$.* Then $m-1$ is even, and $x_k^{m-1}=\mathrm{const}$ only gives $|x_k|=r$ for all $k$. Let $q$ coordinates be $-r$ and the remaining $p=n-q$ be $+r$. The constraint: $(p-q)r=a>0$, so $r>0$, $p>q$ and $r=\frac{a}{n-2q}$. Stationary points: for each set of $q<\frac n2$ indices, the point whose coordinates with those indices equal $-\frac{a}{n-2q}$ and the others $+\frac{a}{n-2q}$.

Examine them with the second differential of the Lagrange function:
$$
d^2L(h)=m(m-1)\sum_{k=1}^nx_k^{m-2}h_k^2=m(m-1)\,r^{m-2}\Bigl(\sum_{k:\,x_k>0}h_k^2-\sum_{k:\,x_k<0}h_k^2\Bigr)
$$
(the exponent $m-2$ is odd, so the sign of a coefficient is the sign of $x_k$), on the tangent space $\sum h_k=0$.

- $q=0$ (all coordinates equal $\frac an$): the form is positive definite, a strict local minimum, $f_m=\frac{a^m}{n^{m-1}}$.
- $q\ge1$. Then $p\ge2$, and on the vector $h=e_i-e_j$ with two "positive" indices the form is positive. On the other hand, take $h$ with $-1$ at one "negative" index and $\frac1p$ at each of the $p$ "positive" ones: the coordinates sum to zero and the bracket equals $p\cdot\frac1{p^2}-1=\frac1p-1<0$. The form is indefinite — no extremum.

So for odd $m\ge3$ the only extremum point is $P=(\frac an,\dots,\frac an)$, a strict local minimum.

**Answer.**

| Case | Points of constrained extremum | Value |
|---|---|---|
| $n=1$ | the single point $x_1=a$ | $a^m$ |
| $m=1$ | all points of $M$ (non-strict maximum and minimum) | $a$ |
| $n\ge2$, $m$ even | $(\frac an,\dots,\frac an)$ — strict global minimum; no maximum | $\dfrac{a^m}{n^{m-1}}$ |
| $n\ge2$, $m\ge3$ odd | $(\frac an,\dots,\frac an)$ — strict local minimum; no others | $\dfrac{a^m}{n^{m-1}}$ |

**Why it works.** The Lagrange equality $x_k^{m-1}=\mathrm{const}$ says: at an extremum the "marginal price" of each coordinate is the same, otherwise one could pour a little from one coordinate into another without violating $\sum x_k=a$ and change $f_m$ to first order. For even $m$ this forces equal coordinates; for odd $m$ only equal absolute values, and extra stationary points with negative coordinates appear. They turn out to be saddles: near a negative $x_k$ the function $t^m$ is concave, near a positive one convex, and on the hyperplane there is always a direction of each kind.

Is the minimum global for odd $m$? For $n=2$ — yes: $f_m(a-T,T)=(a-T)^m+T^m$ is a polynomial of even degree $m-1$ with leading coefficient $ma>0$; it is bounded below and has the single stationary point $T=\frac a2$. For $n\ge3$ — no: at the points $(T,T,a-2T,0,\dots,0)$ the value $2T^m+(a-2T)^m$ behaves like $(2-2^m)T^m\to-\infty$ as $T\to+\infty$. For odd $m\ge3$ and $n\ge2$, $f_m$ is never bounded above.

## Problem 2'.3

**Statement.** $n\in\mathbb N$, $m_k\in\mathbb N$, $m_k\ge2$, $a>0$, $f(x)=\prod_{k=1}^nx_k^{m_k}$, $M=\{\sum_{k=1}^nx_k=a\}$. Find all points of constrained extremum and the extremal values.

**Solution.** Put $m=\sum_{k=1}^nm_k$. For $n=1$ the set $M=\{a\}$ is one point with value $a^{m_1}$; from now on $n\ge2$. Regularity is as in 2'.2.

*Stationary points.* The Lagrange condition: $\partial_kf=\lambda$ for all $k$, where
$$
\partial_kf=m_kx_k^{m_k-1}\prod_{j\ne k}x_j^{m_j}.
$$

**(A) All $x_k\ne0$.** Then $\partial_kf=\dfrac{m_kf}{x_k}=\lambda$ and $f\ne0$, whence $\lambda\ne0$ and $x_k=\dfrac{f}{\lambda}m_k$: the coordinates are proportional to the exponents. The constraint gives $\frac f\lambda\,m=a$, i.e.
$$
x_k^*=\frac{a\,m_k}{m},\qquad k=1,\dots,n .
$$
This is the only stationary point without zero coordinates; all its coordinates are positive.

**(B) There is a zero coordinate, $x_i=0$.** Since $m_i\ge2$, every partial derivative contains the factor $x_i^{m_i}$ or $x_i^{m_i-1}$ and vanishes. So $\nabla f=0$, and **every** point of $M$ with at least one zero coordinate is stationary (with $\lambda=0$); there $f=0$.

*The point $P^*$.* On the set $\Delta=\{x\in M:\ x_k\ge0\ \forall k\}$ (a simplex, compact) the function $f$ is continuous, positive inside and zero on the boundary. Its greatest value on $\Delta$ is attained, and attained inside, hence at a stationary point, i.e. at $P^*$. The interior of $\Delta$ is open in $M$, so $P^*$ is a point of strict constrained local maximum, and
$$
f(P^*)=\prod_{k=1}^n\Bigl(\frac{a\,m_k}{m}\Bigr)^{m_k}=\Bigl(\frac am\Bigr)^{m}\prod_{k=1}^nm_k^{m_k}.
$$

*Points of type (B).* Let $x\in M$, $Z=\{k:\ x_k=0\}\ne\varnothing$. Not all coordinates are zero (their sum is $a>0$), so the complement of $Z$ is non-empty. Write a nearby point of $M$ as $x+h$:
$$
f(x+h)=\underbrace{\prod_{k\notin Z}(x_k+h_k)^{m_k}}_{A(h)}\cdot\prod_{k\in Z}h_k^{m_k}.
$$
For small $h$ the factor $A(h)$ keeps the sign of the number $\sigma=\prod_{k\notin Z}(\operatorname{sign}x_k)^{m_k}=\pm1$. The increments $h_k$, $k\in Z$, can be any small numbers: the condition $\sum h_k=0$ is met at the expense of a coordinate outside $Z$.

- If **all $m_k$, $k\in Z$, are even**, then $\prod_{k\in Z}h_k^{m_k}\ge0$, and near $x$ the function $f$ has sign $\sigma$ or is zero. Since $f(x)=0$: for $\sigma=+1$ this is a local minimum, for $\sigma=-1$ a local maximum.
- If **some $m_i$, $i\in Z$, is odd**, take all $h_k=\varepsilon>0$ for $k\in Z$, $k\ne i$, and $h_i=\pm\varepsilon$. The product takes both signs for arbitrarily small $\varepsilon$. No extremum.

The number $\sigma$ equals $(-1)^N$, where $N$ is the number of indices $k\notin Z$ with $x_k<0$ and $m_k$ odd.

**Answer** (for $n\ge2$).

1. The point $P^*=\Bigl(\dfrac{a\,m_1}{m};\dots;\dfrac{a\,m_n}{m}\Bigr)$, $m=\sum m_k$, is a strict constrained local maximum, $f(P^*)=\Bigl(\dfrac am\Bigr)^m\prod\limits_{k=1}^nm_k^{m_k}$.
2. A point $x\in M$ with a non-empty set $Z$ of zero coordinates is a point of constrained extremum if and only if all $m_k$ with $k\in Z$ are even. The extremal value is $0$; it is a minimum if the number of negative coordinates with odd exponents is even, and a maximum if it is odd.
3. There are no other points of constrained extremum.

**Why it works.** In the region $x_k>0$ the answer is dictated by the weighted AM–GM inequality: $\prod\bigl(\frac{x_k}{m_k}\bigr)^{m_k}\le\bigl(\frac{\sum x_k}{m}\bigr)^m$ with equality when $\frac{x_k}{m_k}=\mathrm{const}$ — the sum must be split in proportion to the exponents. Taking logarithms gives the same: $\ln f=\sum m_k\ln x_k$, and the Lagrange condition is $\frac{m_k}{x_k}=\mathrm{const}$.

The condition $m_k\ge2$ is essential: because of it $f$ vanishes on the hyperplane $x_k=0$ together with its gradient, and that whole hyperplane consists of stationary points. The second differential is degenerate there, so one has to look at the sign of $f$ directly. An even power $h_k^{m_k}$ does not change sign ("touching zero"), an odd one does ("crossing zero") — hence the criterion.

The extrema in item 2 are non-strict for $n\ge3$ (nearby there are other points with $x_k=0$, where also $f=0$) and strict for $n=2$. The local maximum at $P^*$ is, in general, not global: for example, for $n=2$, $m_1=m_2=2$ we have $f(T,a-T)=T^2(a-T)^2\to+\infty$. It is global only for $n=2$ with odd $m_1,m_2$ (then $f\le0$ outside the segment between $(a;0)$ and $(0;a)$). If all $m_k$ are even, then $f\ge0$ everywhere and all points with a zero coordinate are points of global minimum.

**Example.** $n=2$, $f=x^2y^3$, $x+y=a$. $P^*=(\frac{2a}5;\frac{3a}5)$ is a local maximum, $f=\frac{108a^5}{3125}$. The point $(0;a)$: $Z=\{1\}$, $m_1=2$ is even, $\sigma=+1$ — a strict local minimum, $f=0$. The point $(a;0)$: $Z=\{2\}$, $m_2=3$ is odd — no extremum. This agrees with the graph of $g(x)=x^2(a-x)^3$: $g'(x)=x(a-x)^2(2a-5x)$.

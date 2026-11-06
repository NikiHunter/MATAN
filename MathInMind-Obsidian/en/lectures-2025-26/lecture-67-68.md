---
title: "Lectures 67–68 — sufficient conditions for an extremum, conditional extremum, numerical series"
lang: en
course: "Mathematical Analysis, 2025/26"
lecture: 67-68
semester: 3
source: "handwritten notebook, pages p012–p021"
source_pages: "p012, p013, p014, p015, p016, p017, p018, p019, p020, p021"
course_chapter: 22
aliases: ["Lectures 67–68 (en)"]
tags: [mathinmind/en, mathinmind/lecture]
---
# Lectures 67–68 — sufficient conditions for an extremum, conditional extremum, numerical series

[[en/lectures-2025-26/lecture-65-66|← Lectures 65–66]] · [[en/lectures-2025-26/index|Lecture index]] · [[en/lectures-2025-26/lecture-69-70|Lectures 69–70 →]] · [[en/term-index|Terms & theorems]] · [[ru/lectures-2025-26/lecture-67-68|Русский]] · [[es/lectures-2025-26/lecture-67-68|Español]]

> [!info] Source and numbering
> These notes were copied from a handwritten notebook (pages p012–p021; the raw page text is in [`ocr/raw/`](https://github.com/NikiHunter/matan/blob/main/ocr/raw/p012.md)) and checked against the scans of those pages. Page p012 begins with the end of the proof of [[en/lectures-2025-26/lecture-65-66#^thm-6-7-1|Theorem 6.7.1]] from [[en/lectures-2025-26/lecture-65-66|lectures 65–66]]. It is followed by the date “17 September” in a frame, then the heading “Lectures 67–68” and the plan of the class: extrema; [[en/04-numeric-series#4.1 Convergence through partial sums|numerical series]]; convergent and divergent series; the [[en/04-numeric-series#4.2 Nonnegative terms|Cauchy]] and d'Alembert tests. The Cauchy and d'Alembert tests were not covered in this class, see [[en/lectures-2025-26/lecture-69-70|lectures 69–70]]. [[#^thm-6-7-2|Theorem 6.7.2]] carries the mark “(must know!)” in the notebook; the notebook has no proof, it has been restored. The heading of §7.1 has not survived on the slides of the 2024/25 course, so the notebook heading “Numerical series” is used. The numbering of definitions and theorems is the lecturer's (checked against the slides of the 2024/25 course). Slips in the notes are corrected and marked with “Source correction” blocks; lost passages are restored and marked with “Restored” blocks; the tags match [`ocr/RESOLVED.md`](https://github.com/NikiHunter/matan/blob/main/ocr/RESOLVED.md). Places that still have to be checked against the notebook are listed in [`ocr/ISSUES.md`](https://github.com/NikiHunter/matan/blob/main/ocr/ISSUES.md).

## §6.7. Extrema of functions of several variables (conclusion)


**Proof of [[en/lectures-2025-26/lecture-65-66#^thm-6-7-1|Theorem 6.7.1]] (conclusion).** Recall: $a$ is a minimum point of $f$, $V_\delta(a)\subset E$ and $f(x)\ge f(a)$ for $x\in V_\delta(a)$, $h\ne0$, $F(t)=f(a+th)$ for $|t|<\frac{\delta}{\|h\|}$. The function $F$ is differentiable at zero as the composition of the affine map $t\mapsto a+th$ and the map $f$, which is differentiable at the point $a$, and $F'(0)=d_af(h)$. Note that for $|t|<\frac{\delta}{\|h\|}$
$$
\|a+th-a\|=\|th\|=|t|\,\|h\|<\delta ,
$$
hence
$$
F(t)=f(a+th)\ge f(a)=F(0)\qquad\forall t\in\left(-\frac{\delta}{\|h\|},\frac{\delta}{\|h\|}\right).
$$
Thus $0$ is a minimum point of the function $F$ that is interior to its domain, and by [[en/lectures-2025-26/lecture-24-25-26#^thm-3-4-1|Fermat's theorem]] $F'(0)=0$, i.e. $d_af(h)=0$ for all $h\in\mathbb R^n\setminus\{0\}$ (for $h=0$ this is obvious). Therefore $d_af=0$. $\square$ ^p012

### Sufficient condition for an extremum of a function of several variables

> [!theorem] Theorem 6.7.2 (sufficient condition for an extremum)
> Let $E\subset\mathbb R^n$, let $a$ be an interior point of $E$, and let the function $f:E\to\mathbb R$ be twice differentiable at the point $a$, with $d_af=0$. Then the following statements hold.
>
> 1. If the quadratic form $d_a^2f$ is positive definite (i.e. $d_a^2f(h)>0$ for all $h\ne0$), then $a$ is a strict minimum point of $f$.
> 2. If $d_a^2f$ is negative definite (i.e. $d_a^2f(h)<0$ for all $h\ne0$), then $a$ is a strict maximum point of $f$.
> 3. If $d_a^2f$ takes both positive and negative values, then $f$ has no extremum at the point $a$.

^thm-6-7-2

For example, for a function of two variables $f=f(x_1,x_2)$
$$
\nabla f=\left(\frac{\partial f}{\partial x_1},\frac{\partial f}{\partial x_2}\right),\qquad D^2f=\begin{pmatrix}\dfrac{\partial^2f}{\partial x_1^2}&\dfrac{\partial^2f}{\partial x_1\partial x_2}\\[2mm]\dfrac{\partial^2f}{\partial x_2\partial x_1}&\dfrac{\partial^2f}{\partial x_2^2}\end{pmatrix},
$$
and $d_a^2f$ is the quadratic form with matrix $D^2f(a)$: $d_a^2f(h)=\sum_{i,j=1}^{2}\frac{\partial^2f}{\partial x_i\partial x_j}(a)h_ih_j$.

> [!note] Restored
> (by the standard proof, cf. Zorich, vol. 1, ch. VIII; in the notebook the theorem is written without proof).
>
> **Proof.** Since $f$ is twice differentiable at the point $a$ and $d_af=0$, by the Taylor–Peano formula ([[en/lectures-2025-26/lecture-65-66#^thm-6-5-1|Theorem 6.5.1]] for $s=2$, written through differentials)
> $$
> f(a+h)-f(a)=\frac12\,d_a^2f(h)+r(h),\qquad r(h)=o(\|h\|^2)\quad(h\to0).
> $$
> *1)* Let $d_a^2f$ be positive definite. A quadratic form is continuous and the unit sphere $S=\{h\in\mathbb R^n:\ \|h\|=1\}$ is [[en/lectures-2025-26/lecture-57-58#^def-5-3-7|compact]], so $\mu=\min_{h\in S}d_a^2f(h)$ is attained and $\mu>0$. By homogeneity $d_a^2f(h)=\|h\|^2\,d_a^2f\bigl(h/\|h\|\bigr)\ge\mu\|h\|^2$ for $h\ne0$. Choose $\delta>0$ so that $V_\delta(a)\subset E$ and $|r(h)|\le\frac{\mu}{4}\|h\|^2$ for $\|h\|<\delta$. Then for $0<\|h\|<\delta$
> $$
> f(a+h)-f(a)\ge\frac{\mu}{2}\|h\|^2-\frac{\mu}{4}\|h\|^2=\frac{\mu}{4}\|h\|^2>0 ,
> $$
> i.e. $a$ is a strict minimum point of $f$.
>
> *2)* Apply statement 1) to the function $-f$.
>
> *3)* Let $d_a^2f(h_1)>0$ and $d_a^2f(h_2)<0$. For fixed $h\ne0$ and $t\to0$
> $$
> f(a+th)-f(a)=\frac{t^2}{2}\,d_a^2f(h)+o(t^2)=\frac{t^2}{2}\bigl(d_a^2f(h)+o(1)\bigr),
> $$
> so for all sufficiently small $t\ne0$ we have $f(a+th_1)>f(a)$ and $f(a+th_2)<f(a)$. Hence every neighbourhood of the point $a$ contains points where $f>f(a)$ and points where $f<f(a)$, and $a$ is not an extremum point of $f$. $\square$

**Remark.** [[#^thm-6-7-2|Theorem 6.7.2]] does not cover the situation when $d_a^2f$ keeps its sign but is neither positive nor negative definite. In particular, the theorem says nothing in the case $d_a^2f\equiv0$.


**Corollary.** Let $E\subset\mathbb R^2$, let $a$ be an [[en/lectures-2025-26/lecture-57-58#Printed slide 4 (PDF p. 4) — The interior of a set — Definition 5.3.3|interior point]] of $E$, and let $f:E\to\mathbb R$ be a function twice differentiable at the point $a$, $d_af=0$. Put
$$
A=\frac{\partial^2f}{\partial x^2}(a),\qquad B=\frac{\partial^2f}{\partial x\partial y}(a),\qquad C=\frac{\partial^2f}{\partial y^2}(a).
$$
Then the following statements hold. ^p013

1. If $A>0$ and $AC>B^2$, then $a$ is a strict minimum point of $f$.
2. If $A<0$ and $AC>B^2$, then $a$ is a strict maximum point of $f$.
3. If $AC<B^2$, then $f$ has no extremum at the point $a$.

**Proof.** First we check statements 1) and 2). By the formula
$$
d_a^2f(h)=\sum_{i=1}^{2}\sum_{j=1}^{2}\frac{\partial^2f}{\partial x_i\partial x_j}(a)h_ih_j\qquad(h\in\mathbb R^2)
$$
the second differential $d_a^2f$ is the quadratic form with the [[en/15-multivariable-differentiation#15.4 Higher derivatives and Taylor's formula|Hessian matrix]]
$$
H=\begin{pmatrix}A&B\\B&C\end{pmatrix}
$$
(the [[en/lectures-2025-26/lecture-63-64#Printed slide 16 (PDF p. 30). Sufficient conditions for equality — Theorem 6.4.1|mixed derivatives]] at the point $a$ are equal by [[en/lectures-2025-26/lecture-63-64#Printed slide 16 (PDF p. 30). Sufficient conditions for equality — Theorem 6.4.1|Theorem 6.4.1]], since $f$ is twice differentiable at $a$). Compute the leading principal minors of $H$: $\Delta_1=A$, $\Delta_2=\det H=AC-B^2$. By Sylvester's criterion and its corollary:

- $\Delta_1>0$, $\Delta_2>0$ $\Rightarrow$ $d_a^2f$ is positive definite $\Rightarrow$ 1) holds (by [[#^thm-6-7-2|Theorem 6.7.2]]);
- $\Delta_1<0$, $\Delta_2>0$ $\Rightarrow$ $d_a^2f$ is negative definite $\Rightarrow$ 2) holds (by [[#^thm-6-7-2|Theorem 6.7.2]]).

Now we prove 3). By the formula
$$
d_a^2f(h)=\sum_{i=1}^{2}\frac{\partial^2f}{\partial x_i^2}(a)h_i^2+2\sum_{1\le i<j\le2}\frac{\partial^2f}{\partial x_i\partial x_j}(a)h_ih_j\qquad(h\in\mathbb R^2)
$$
writing $h=(dx,dy)$, we get
$$
d_a^2f(dx,dy)=A\,dx^2+2B\,dx\,dy+C\,dy^2 .
$$
Fix $dy\ne0$. If $A\ne0$, this is a quadratic trinomial in $dx$ with discriminant
$$
(2B\,dy)^2-4A\,C\,dy^2=4dy^2(B^2-AC)>0 ,
$$
so it has two distinct real roots and takes both positive and negative values. If $A=0$, then $B\ne0$ (since $B^2>AC=0$), and $2B\,dy\cdot dx+C\,dy^2$ is a non-constant linear function of $dx$, which also takes values of both signs. Thus $d_a^2f$ takes both positive and negative values, and by [[#^thm-6-7-2|Theorem 6.7.2]] $f$ has no extremum at the point $a$. $\square$

> [!info] Source correction
> (M051). The notes say: “For fixed $dy\ne0$ we have: $4dy^2(B^2-AC)>0$” — without explaining that this is the discriminant of the trinomial in $dx$, and without the case $A=0$, in which the expression is not a quadratic trinomial. Both points have been added.


**Remark.** The classification in the corollary does not cover the case $AC-B^2=0$. This is the case when $d_a^2f(h)$ is a perfect square, i.e. has the form
$$
d_a^2f(dx,dy)=\pm(\alpha\,dx+\beta\,dy)^2,\qquad\alpha,\beta\in\mathbb R .
$$
In particular, when the second differential vanishes we cannot draw conclusions about an extremum of $f$ at the point $a$. ^p014

**Example.** Let $f(x,y)=x^4+3xy^2+y^4$, $a=(0,0)$. We have
$$
\nabla f(x,y)=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}\right)=(4x^3+3y^2,\ 4y^3+6xy),
$$
$\nabla f(0,0)=(0,0)$, i.e. $d_af=0$ and $(0,0)$ is a stationary point. The second differential is given by the Hessian matrix
$$
H_f=\begin{pmatrix}\dfrac{\partial^2f}{\partial x^2}&\dfrac{\partial^2f}{\partial x\partial y}\\[2mm]\dfrac{\partial^2f}{\partial y\partial x}&\dfrac{\partial^2f}{\partial y^2}\end{pmatrix}=\begin{pmatrix}12x^2&6y\\6y&12y^2+6x\end{pmatrix},\qquad H_f(0,0)=\begin{pmatrix}0&0\\0&0\end{pmatrix}.
$$
The matrix is zero — a degenerate case: $d_a^2f\equiv0$, and [[#^thm-6-7-2|Theorem 6.7.2]] gives nothing. Compute the third derivatives:
$$
\frac{\partial^3f}{\partial x^3}=24x,\qquad\frac{\partial^3f}{\partial x^2\partial y}=0,\qquad\frac{\partial^3f}{\partial x\partial y^2}=6,\qquad\frac{\partial^3f}{\partial y^3}=24y ;
$$
at the point $(0,0)$ only $\frac{\partial^3f}{\partial x\partial y^2}(0,0)=6$ is nonzero. By [[en/lectures-2025-26/lecture-63-64#Printed slide 21 (PDF p. 41). Computing higher differentials — Theorem 6.4.2|Theorem 6.4.2]] the multi-index $(1,2)$ enters $d_a^3f$ with the coefficient $\frac{3!}{1!\,2!}=C_3^1=3$, so
$$
d_a^3f(dx,dy)=C_3^1\,\frac{\partial^3f}{\partial x\,\partial y^2}(0,0)\,dx\,dy^2=3\cdot6\,dx\,dy^2=18\,dx\,dy^2 ,
$$
i.e. $d_a^3f(h)=18\,h_1h_2^2$.

> [!info] Source correction
> (A056). The notes say “$d_a^3f(dx,dy)=C_3^1\frac{\partial^2f}{\partial x\partial y^2}(0,0)\,dx\,dy^2=18\,dx\,dy^2$” (in the page transcription, $\frac{\partial^3f}{\partial x^2\partial y}$). The coefficient of $dx\,dy^2$ is the third-order derivative $\frac{\partial^3f}{\partial x\partial y^2}(0,0)=6$ (and $\frac{\partial^3f}{\partial x^2\partial y}\equiv0$); with $C_3^1=3$ one gets $3\cdot6=18$.

Consider $h\in\mathbb R^2\setminus\{(0,0)\}$ with $d_a^3f(h)\ne0$ (for example, $h=(1,1)$). Put $\varphi(t)=f(th)$, $t\in\mathbb R$. By formula (∗) from the proof of [[en/lectures-2025-26/lecture-65-66#^thm-6-5-2|Theorem 6.5.2]] we have $\varphi^{(k)}(0)=d_a^kf(h)$, so
$$
\varphi'(0)=\varphi''(0)=0,\qquad\varphi'''(0)=d_a^3f(h)\ne0 .
$$
The first nonzero derivative of the function $\varphi$ at zero has odd order, so $\varphi$ has no extremum at zero. Hence $f$ has no extremum at the point $(0,0)$ either: if $(0,0)$ were an extremum point of $f$, then $0$ would be an extremum point of $\varphi$. Directly: $\varphi(t)=f(t,t)=3t^3+2t^4$ changes sign when passing through $0$.


### The conditional extremum problem

Let $f:E\subset\mathbb R^n\to\mathbb R$, let $a\in E$ be an extremum point of $f$. Then in some neighbourhood $V(a)$ either $f(x)\ge f(a)$ for all $x\in V(a)\cap E$, or $f(x)\le f(a)$ for all $x\in V(a)\cap E$. Suppose now that we are interested not in all points $x\in V(a)$ but only in those that satisfy some additional equalities called constraint equations. Then one speaks of a conditional, or relative, extremum subject to these constraint equations. For example, $f:\mathbb R^n\to\mathbb R$, $a$ is an extremum point under $m$ additional conditions
$$
\begin{cases}\varphi_1(x_1,\ldots,x_n)=\varphi_1(a),\\ \ldots\ldots\ldots\ldots\ldots\\ \varphi_m(x_1,\ldots,x_n)=\varphi_m(a).\end{cases}
$$

> [!info] Source correction
> (M058). In the notes the number of additional conditions in this line is denoted $k$, and the last condition $\varphi_k$; in [[#^def-6-7-2|Definition 6.7.2]] and below the number of conditions is $m$, and $k$ is the index of a condition. The notation has been unified.

### Conditional (relative) extremum

> [!definition] Definition 6.7.2
> Let $E\subset\mathbb R^n$, $a\in E$, $m\in\mathbb N$, $m<n$, $f,\varphi_1,\ldots,\varphi_m:E\to\mathbb R$. Suppose that $a$ is an extremum point of the restriction of the function $f$ to the set
> $$
> \{x\in E:\ \varphi_k(x)=\varphi_k(a),\ k=1,\ldots,m\}.
> $$
> Then $a$ is called a point of conditional (relative) extremum of $f$ of the corresponding type (minimum or maximum) subject to the constraint equations $\varphi_k(x)=\varphi_k(a)$, where $k\in\{1,\ldots,m\}$, $x\in E$.

^def-6-7-2

**Remark.** Without loss of generality we assume that $\varphi_k(a)=0$ for all $k\in\{1,\ldots,m\}$ (otherwise replace $\varphi_k$ by $\varphi_k-\varphi_k(a)$).

### Necessary condition for a relative extremum

Write $\Phi=(\varphi_1,\ldots,\varphi_m)$, i.e. $\Phi:E\subset\mathbb R^n\to\mathbb R^m$; the constraint equations take the form $\Phi=0$.

> [!theorem] Theorem 6.7.3 (necessary condition for a relative extremum)
> Let $m,n\in\mathbb N$, $m<n$, let the set $E$ be open in $\mathbb R^n$, $a\in E$, $f\in C^1(E)$, $\Phi\in C^1(E,\mathbb R^m)$, $\operatorname{rank}\Phi'(a)=m$. Suppose also that $a$ is a point of conditional extremum of $f$ subject to the constraint equations $\Phi=0$ (in particular, $\Phi(a)=0$). Then there exist $\lambda_1,\ldots,\lambda_m\in\mathbb R$ such that
> $$
> \operatorname{grad}f(a)=\sum_{k=1}^{m}\lambda_k\operatorname{grad}\varphi_k(a).\qquad(6.7.1)
> $$

^thm-6-7-3


**Remark.** The numbers $\lambda_1,\ldots,\lambda_m$ satisfying (6.7.1) are called [[en/16-implicit-functions-extrema#16.4 Lagrange multipliers|Lagrange multipliers]].

^p016

**Proof of [[#^thm-6-7-3|Theorem 6.7.3]].** Since $\operatorname{rank}\Phi'(a)=m$, among the $n$ columns of the matrix $\Phi'(a)$ (of size $m\times n$) there are $m$ linearly independent ones; renumbering the coordinates, we may assume that these are the last $m$ columns. We write the elements of $\mathbb R^n$ as $(x,y)$, where $x\in\mathbb R^{n-m}$, $y\in\mathbb R^m$, and let $a=(x^0,y^0)$. Then $\det\Phi'_y(a)\ne0$.

> [!info] Source correction
> (M517). The notes do not mention the choice of the numbering of coordinates, and without it the implicit map theorem cannot be applied: the matrix $\Phi'_y(a)$ must be invertible. This is guaranteed by the condition $\operatorname{rank}\Phi'(a)=m$.

Put
$$
M=\{(x,y)\in E:\ \varphi_k(x,y)=0\ \ \forall k\in\{1,\ldots,m\}\}.
$$
By the implicit map theorem ([[en/lectures-2025-26/lecture-65-66#^thm-6-6-1|Theorem 6.6.1]] for $s=1$, applied to the equation $\Phi(x,y)=0$) there exist a neighbourhood $V(a)\subset E$, a neighbourhood $U(x^0)\subset\mathbb R^{n-m}$ and a map $\psi\in C^1(U(x^0),\mathbb R^m)$ such that
$$
M\cap V(a)=\{(x,\psi(x)):\ x\in U(x^0)\}.
$$

*Step 1.* The restriction $f|_M$ has an extremum at the point $a$. Since $\psi$ is continuous and $\psi(x^0)=y^0$, the points $(x,\psi(x))\in M$ for $x$ close to $x^0$ are arbitrarily close to $a$; hence the function $F(x)=f(x,\psi(x))$, $x\in U(x^0)$, has an extremum at the point $x^0$. By [[en/lectures-2025-26/lecture-65-66#^thm-6-7-1|Theorem 6.7.1]] $\nabla F(x^0)=0$, and by the formula from the remark to [[en/lectures-2025-26/lecture-65-66#^thm-6-6-1|Theorem 6.6.1]] (the second term comes from differentiation with respect to the second argument)
$$
f'_x(a)+f'_y(a)\,\psi'(x^0)=0 .
$$

*Step 2.* Moreover, the implicit map theorem gives $\Phi(x,\psi(x))=0$ for all $x\in U(x^0)$, whence (by the same remark to [[en/lectures-2025-26/lecture-65-66#^thm-6-6-1|Theorem 6.6.1]])
$$
\Phi'_x(a)+\Phi'_y(a)\,\psi'(x^0)=0 .
$$
Here $\Phi=\begin{pmatrix}\varphi_1\\ \vdots\\ \varphi_m\end{pmatrix}$, $\varphi_i:E\to\mathbb R$, and
$$
\Phi'_x=\begin{pmatrix}\dfrac{\partial\varphi_1}{\partial x_1}&\dfrac{\partial\varphi_1}{\partial x_2}&\cdots&\dfrac{\partial\varphi_1}{\partial x_{n-m}}\\ \vdots&\vdots&&\vdots\\ \dfrac{\partial\varphi_m}{\partial x_1}&\dfrac{\partial\varphi_m}{\partial x_2}&\cdots&\dfrac{\partial\varphi_m}{\partial x_{n-m}}\end{pmatrix}
$$
is a matrix of size $m\times(n-m)$; similarly $\Phi'_y$ is a square matrix of order $m$, $f'_x(a)$ and $f'_y(a)$ are rows of length $n-m$ and $m$, and $\psi'(x^0)$ is a matrix of size $m\times(n-m)$.

*Step 3.* Thus
$$
\begin{cases}f'_x(a)+f'_y(a)\,\psi'(x^0)=0,\\ \Phi'_x(a)+\Phi'_y(a)\,\psi'(x^0)=0.\end{cases}
$$
Let $\lambda=(\lambda_1,\ldots,\lambda_m)$ be an arbitrary row. Multiplying the second equality on the left by $\lambda$ and subtracting it from the first, we get
$$
\bigl[f'_x(a)-\lambda\Phi'_x(a)\bigr]+\bigl[f'_y(a)-\lambda\Phi'_y(a)\bigr]\psi'(x^0)=0.\qquad(*)
$$
Put $\lambda=f'_y(a)\,[\Phi'_y(a)]^{-1}$. Then the second term in (∗) vanishes, hence the first term in (∗) vanishes too: $f'_x(a)=\lambda\Phi'_x(a)$; moreover, $f'_y(a)=\lambda\Phi'_y(a)$ by the choice of $\lambda$. Thus for all $i\in\{1,\ldots,n-m\}$ and $j\in\{1,\ldots,m\}$
$$
\frac{\partial f}{\partial x_i}(a)=\sum_{k=1}^{m}\lambda_k\frac{\partial\varphi_k}{\partial x_i}(a),\qquad\frac{\partial f}{\partial y_j}(a)=\sum_{k=1}^{m}\lambda_k\frac{\partial\varphi_k}{\partial y_j}(a).
$$


Consequently,
$$
\begin{aligned}
\nabla f(a)&=\left(\frac{\partial f}{\partial x_1}(a),\ldots,\frac{\partial f}{\partial x_{n-m}}(a),\frac{\partial f}{\partial y_1}(a),\ldots,\frac{\partial f}{\partial y_m}(a)\right)\\
&=\sum_{k=1}^{m}\lambda_k\left(\frac{\partial\varphi_k}{\partial x_1}(a),\ldots,\frac{\partial\varphi_k}{\partial x_{n-m}}(a),\frac{\partial\varphi_k}{\partial y_1}(a),\ldots,\frac{\partial\varphi_k}{\partial y_m}(a)\right)=\sum_{k=1}^{m}\lambda_k\nabla\varphi_k(a).
\end{aligned}
$$
Returning to the original numbering of the coordinates permutes the components of all [[en/lectures-2025-26/lecture-61-62#Printed slide 11 (PDF p. 14). Jacobian matrix and gradient — Definition 6.1.6|gradients]] in the same way, so equality (6.7.1) is preserved. $\square$ ^p017

### Stationarity of the Lagrange function

> [!theorem] Theorem 6.7.4
> Let $m,n\in\mathbb N$, $m<n$, let the set $E$ be open in $\mathbb R^n$, $a\in E$, $f\in C^1(E)$, $\Phi\in C^1(E,\mathbb R^m)$, $\operatorname{rank}\Phi'(a)=m$. Suppose also that $a$ is a point of conditional extremum of $f$ subject to the constraint equations $\Phi=0$. Put
> $$
> L(x,\lambda)=f(x)-\sum_{k=1}^{m}\lambda_k\varphi_k(x)\qquad(x\in E,\ \lambda\in\mathbb R^m).
> $$
> Then there exists $\lambda\in\mathbb R^m$ such that $\operatorname{grad}L(a,\lambda)=0$.

^thm-6-7-4

> [!note] Restored
> (from the notes to the slides of the 2024/25 course, FS p47; there is no proof in the notebook).
>
> **Proof.** Take $\lambda=(\lambda_1,\ldots,\lambda_m)$ from [[#^thm-6-7-3|Theorem 6.7.3]]. Then by (6.7.1)
> $$
> \operatorname{grad}_xL(a,\lambda)=\operatorname{grad}f(a)-\sum_{k=1}^{m}\lambda_k\operatorname{grad}\varphi_k(a)=0 .
> $$
> Moreover, $\frac{\partial L}{\partial\lambda_k}(a,\lambda)=-\varphi_k(a)=0$, since $a$ satisfies the constraint equations. Hence the gradient of $L$ with respect to all $n+m$ variables $(x,\lambda)$ vanishes as well. $\square$
>
> Thus the points of conditional extremum should be sought among the solutions of the system $\operatorname{grad}L(x,\lambda)=0$: these are $n+m$ equations (condition (6.7.1) and the constraint equations) in $n+m$ unknowns $x_1,\ldots,x_n,\lambda_1,\ldots,\lambda_m$.

### Sufficient condition for a relative extremum

> [!definition] Definition 6.7.3
> Let $N$ be a linear subspace of $\mathbb R^n$, and $f$ a quadratic form on $\mathbb R^n$ (here $f$ is an arbitrary quadratic form, not the objective function). The form $f$ is called positive definite on $N$ if $f(x)>0$ for all $x\in N\setminus\{0\}$, and negative definite on $N$ if $f(x)<0$ for all $x\in N\setminus\{0\}$.

^def-6-7-3

**Remark.** If $f$ is positive definite on $\mathbb R^n$, it is positive definite on every linear subspace $\mathbb R^n$. The converse is false.


> [!theorem] Theorem 6.7.5 (sufficient condition for a relative extremum)
> Let $m,n\in\mathbb N$, $m<n$, let the set $E$ be open in $\mathbb R^n$, $a\in E$, $f\in C^2(E)$, $\Phi\in C^2(E,\mathbb R^m)$, $\Phi(a)=0$, $\operatorname{rank}\Phi'(a)=m$. Put
> $$
> N=\{h\in\mathbb R^n:\ d_a\Phi(h)=0\},\qquad L(x)=f(x)-\sum_{k=1}^{m}\lambda_k\varphi_k(x)\quad(x\in E),
> $$
> where $\lambda_1,\ldots,\lambda_m$ satisfy condition (6.7.1) at the point $a$. Then the following statements hold.
>
> 1. If $d_a^2L$ is positive (negative) definite on $N$, then $f$ has at the point $a$ a conditional minimum (maximum) subject to the constraint equations $\Phi=0$.
> 2. If $d_a^2L$ takes both positive and negative values on $N$, then $f$ has no conditional extremum at the point $a$ subject to the constraint equations $\Phi=0$.

^thm-6-7-5

Condition (6.7.1) means that $a$ is a stationary point of the function $L$: $d_aL=0$. The proof of [[#^thm-6-7-5|Theorem 6.7.5]] is not given in the notes.

## §7.1. Numerical series

> [!definition] Definition 7.1.1
> Let a sequence $(a_n)$, $a_n\in\mathbb R$, $n\in\mathbb N$ be given. Then $S_n=a_1+a_2+\ldots+a_n$ is called a partial sum of the series, $S=\lim_{n\to\infty}S_n$ the sum of the series; for the sum the notation $S:=\sum_{n=1}^{\infty}a_n$ is used; $a_n$ is called the general term of the series.

^def-7-1-1

> [!definition] Definition 7.1.2
> The series $\sum_{n=1}^{\infty}a_n$ converges if the sum of the series $S$ exists and is finite. Otherwise the series diverges.

^def-7-1-2

So if $S_n=\sum_{k=1}^{n}a_k$ and $S=\lim_{n\to\infty}S_n$, three cases are possible:

1. $S$ exists and is finite ($S\in\mathbb R$) — the series converges;
2. $S$ exists and is infinite ($S=+\infty$ or $S=-\infty$) — the series diverges;
3. $S$ does not exist — the series diverges.

**Example 1.** The series $\sum_{n=1}^{\infty}0$ converges, and its sum is $0$, since all partial sums are $S_n=0$.


**Example 2.** The series $\sum_{k=1}^{\infty}1$ diverges: $S_n=\sum_{k=1}^{n}1=n$, $\lim_{n\to\infty}S_n=\lim_{n\to\infty}n=+\infty$.

^p019

**Example 3.** The series $\sum_{k=0}^{\infty}(-1)^k=1-1+1-1+1-1+\ldots$ diverges. Its partial sums $S_n=\sum_{k=0}^{n}(-1)^k$ equal $1$ for even $n$ and $0$ for odd $n$, so the sequence $(S_n)$ has neither a finite nor an infinite limit.

**Example 4.** The series $\sum_{k=1}^{\infty}\frac{1}{k(k+1)}$ converges, and $S=1$:
$$
S_n=\sum_{k=1}^{n}\frac{1}{k(k+1)}=\sum_{k=1}^{n}\left(\frac1k-\frac{1}{k+1}\right)=1-\frac{1}{n+1}\to1\qquad(n\to\infty).
$$

## §7.2. Properties of series

*Property 1.* If the series $\sum_{n=1}^{\infty}a_n$ converges, then $a_n\to0$ as $n\to\infty$.

**Remark.** (a) If $a_n\not\to0$ as $n\to\infty$, then the series $\sum_{n=1}^{\infty}a_n$ diverges (the necessary condition for convergence). (b) If $a_n\to0$ as $n\to\infty$, the series $\sum_{n=1}^{\infty}a_n$ need not converge (see the example of the harmonic series below).

*Property 2.* The series $\sum_{n=1}^{\infty}a_n$ converges if and only if for every $k\in\mathbb N$ the series $\sum_{n=k+1}^{\infty}a_n$ — the remainder of the series after the $k$-th term — converges.

**Proof of property 1.** Let $\sum_{k=1}^{\infty}a_k=S$, $S_N=\sum_{k=1}^{N}a_k$. The series converges, so $S$ exists and $-\infty<S<+\infty$. Then $a_N=S_N-S_{N-1}\to S-S=0$ as $N\to\infty$. $\square$

**Example.** The harmonic series
$$
\sum_{k=1}^{\infty}\frac1k=1+\frac12+\frac13+\frac14+\ldots
$$
diverges, although $a_k=\frac1k\to0$. Indeed, group the terms of the partial sum $S_{2^m}$:
$$
S_{2^m}=1+\frac12+\left(\frac13+\frac14\right)+\left(\frac15+\ldots+\frac18\right)+\ldots+\left(\frac{1}{2^{m-1}+1}+\ldots+\frac{1}{2^m}\right).
$$
After the one there are $m$ groups: the $j$-th group ($j=1,\ldots,m$) consists of $2^{j-1}$ terms, each of which is at least $\frac{1}{2^j}$, so the sum of the $j$-th group is at least $\frac{2^{j-1}}{2^j}=\frac12$. For example, $\frac13+\frac14>\frac12$, $\frac15+\ldots+\frac18>\frac12$, …, $\frac{1}{2^{m-1}+1}+\ldots+\frac{1}{2^m}\ge\frac{2^{m-1}}{2^m}=\frac12$. Therefore
$$
S_{2^m}\ge1+\underbrace{\frac12+\frac12+\ldots+\frac12}_{m}=1+\frac m2\to+\infty\qquad(m\to\infty).
$$
Thus $S_{2^m}\ge1+\frac m2$ for all $m$ and $S_{2^m}\to+\infty$. Hence the sequence of partial sums $(S_n)$ is unbounded and has no finite limit, i.e. the harmonic series diverges (and since $S_n$ increases, $S_n\to+\infty$).

**Proof of property 2.** Let $n>m$. Then
$$
\sum_{k=1}^{n}a_k=\sum_{k=1}^{m}a_k+\sum_{k=m+1}^{n}a_k ,\qquad(*)
$$
and the first term on the right is a fixed number independent of $n$. Let $n\to\infty$ in (∗): the limits of the right- and left-hand sides of (∗) exist (or do not exist) simultaneously.


Write $A=\sum_{k=1}^{m}a_k$. If $\sum_{k=m+1}^{n}a_k\to S_1=\sum_{k=m+1}^{\infty}a_k$, then $\sum_{k=1}^{n}a_k\to A+S_1$, i.e.
$$
\sum_{k=1}^{\infty}a_k=A+S_1=\sum_{k=1}^{m}a_k+\sum_{k=m+1}^{\infty}a_k ;
$$
conversely, if $\sum_{k=1}^{n}a_k\to S$, then $\sum_{k=m+1}^{n}a_k\to S-A$. Hence the convergence of the series $\sum_{k=1}^{\infty}a_k$ and $\sum_{k=m+1}^{\infty}a_k$ is equivalent. $\square$ ^p020

**Corollary (of property 2).** If the series $\sum_{k=1}^{\infty}a_k$ converges, its remainder tends to zero: $\sum_{k=m+1}^{\infty}a_k\to0$ as $m\to\infty$.

**Proof.** Let $S=\sum_{k=1}^{\infty}a_k$, $S_m=\sum_{k=1}^{m}a_k$. By property 2, for every $m$ the remainder converges, and passing to the limit as $n\to\infty$ in the equality
$$
\sum_{k=m+1}^{n}a_k=\sum_{k=1}^{n}a_k-\sum_{k=1}^{m}a_k
$$
gives $\sum_{k=m+1}^{\infty}a_k=S-S_m$. As $m\to\infty$ we have $S_m\to S$, hence $\sum_{k=m+1}^{\infty}a_k=S-S_m\to S-S=0$. $\square$

*Property 3.* Let $k\in\mathbb R$, $k\ne0$. The series $\sum_{n=1}^{\infty}a_n=:(\mathrm{I})$ and $\sum_{n=1}^{\infty}ka_n=:(\mathrm{II})$ converge and diverge simultaneously. If (I) and (II) converge, then $\sum_{n=1}^{\infty}ka_n=k\sum_{n=1}^{\infty}a_n$.

> [!info] Source correction
> (M518). The notes say “$k\in\mathbb R$”. For $k=0$ series (II) always converges, while series (I) may diverge, so simultaneous convergence holds only for $k\ne0$. If series (I) converges, then series (II) converges and $\sum ka_n=k\sum a_n$ for every $k\in\mathbb R$.

*Property 4.* Let two series $\sum_{n=1}^{\infty}a_n$ and $\sum_{n=1}^{\infty}b_n$ converge. Then the series $\sum_{n=1}^{\infty}(a_n+b_n)$ converges and
$$
\sum_{n=1}^{\infty}(a_n+b_n)=\sum_{n=1}^{\infty}a_n+\sum_{n=1}^{\infty}b_n .
$$

**Proof of properties 3 and 4.** For every $N$
$$
\sum_{n=1}^{N}ka_n=k\sum_{n=1}^{N}a_n,\qquad\sum_{n=1}^{N}(a_n+b_n)=\sum_{n=1}^{N}a_n+\sum_{n=1}^{N}b_n .
$$
If series (I) converges (respectively, the series $\sum a_n$ and $\sum b_n$ converge), the right-hand sides have finite limits as $N\to\infty$; by the properties of [[en/lectures-2025-26/lecture-08#^def-2-1-2|limits of sequences]] the left-hand sides have limits too, and
$$
\sum_{n=1}^{\infty}ka_n=k\sum_{n=1}^{\infty}a_n,\qquad\sum_{n=1}^{\infty}(a_n+b_n)=\sum_{n=1}^{\infty}a_n+\sum_{n=1}^{\infty}b_n .
$$
If series (II) converges and $k\ne0$, then the partial sums of series (I) equal the partial sums of series (II) multiplied by $\frac1k$ and also have a finite limit. $\square$

**Remark.** If the series $\sum_{n=1}^{\infty}a_n$ diverges and the series $\sum_{n=1}^{\infty}b_n$ converges, then the series $\sum_{n=1}^{\infty}(a_n+b_n)$ diverges. Indeed, if it converged, then by properties 3 and 4 the series with terms $a_n=(a_n+b_n)-b_n$ would converge too. A contradiction.


### The Bolzano–Cauchy criterion

The series $\sum_{n=1}^{\infty}a_n$ converges if and only if
$$
\forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n>N\ \forall p\in\mathbb N\qquad\left|\sum_{k=n+1}^{n+p}a_k\right|=|a_{n+1}+\ldots+a_{n+p}|<\varepsilon .
$$

> [!info] Source correction
> (T078). The notes say “$\forall p>0$”. Here $p$ is the number of terms, i.e. $p\in\mathbb N$ (as in the proof).

**Proof.** By definition the series $\sum_{n=1}^{\infty}a_n$ converges if and only if the sequence of its partial sums $S_m:=\sum_{n=1}^{m}a_n$ has a finite limit as $m\to\infty$. By the Bolzano–Cauchy criterion for sequences (proved earlier) this is equivalent to the condition
$$
\forall\varepsilon>0\ \exists N\in\mathbb N:\ \forall m,n>N\qquad|S_m-S_n|<\varepsilon .
$$
Without loss of generality $m>n$ (for $m=n$ the difference is zero, and $|S_m-S_n|=|S_n-S_m|$). Put $p:=m-n\in\mathbb N$; then $S_m-S_n=\sum_{k=n+1}^{n+p}a_k$, and the last condition coincides with the condition of the criterion. $\square$

### How to prove that a series diverges

The Bolzano–Cauchy criterion gives a way to prove the divergence of a series: one has to find a sequence of integers $(m_n)$, $m_n>n$, such that
$$
\sum_{k=n}^{m_n}a_k\not\to0\qquad(n\to\infty).
$$
If the series converged, such sums would tend to zero by the Bolzano–Cauchy criterion.

**Remark.** Often one chooses $m_n=\alpha n$, where $\alpha>1$ (for example, $m_n=2n$).

**Example.** For the harmonic series take $m_n=2n$:
$$
\sum_{k=n}^{2n}\frac1k=\frac1n+\frac{1}{n+1}+\ldots+\frac{1}{2n}\ge\underbrace{\frac{1}{2n}+\frac{1}{2n}+\ldots+\frac{1}{2n}}_{n+1}=\frac{n+1}{2n}>\frac12 ,
$$
so $\sum_{k=n}^{2n}\frac1k\not\to0$, and the harmonic series diverges (one more proof).

> [!info] Source correction
> (T080). The page transcription has “$\sum_{k=n}^{2n}\frac1k\to(n+1)\frac{1}{2n}\to0$”; the notebook has “$\ge(n+1)\frac{1}{2n}\not\to0$” (the arrow is crossed out). The correct estimate is $\sum_{k=n}^{2n}\frac1k\ge\frac{n+1}{2n}\to\frac12$, i.e. these sums do not tend to zero.

### Absolute convergence

> [!definition] Definition 7.2.1
> The series $\sum_{n=1}^{\infty}a_n$ is called absolutely convergent if the series $\sum_{n=1}^{\infty}|a_n|$ converges.

^def-7-2-1

*Property 5.* If a series converges absolutely, it converges.

**Proof of property 5.** Take an arbitrary $\varepsilon>0$ and apply the Bolzano–Cauchy criterion. We know that the series $\sum_{k=1}^{\infty}|a_k|$ converges; by the Bolzano–Cauchy criterion there is $N\in\mathbb N$ such that $\sum_{k=n+1}^{n+p}|a_k|<\varepsilon$ for all $n>N$ and $p\in\mathbb N$. But then
$$
\left|\sum_{k=n+1}^{n+p}a_k\right|\le\sum_{k=n+1}^{n+p}|a_k|<\varepsilon\qquad(n>N,\ p\in\mathbb N),
$$
and by the Bolzano–Cauchy criterion the series $\sum_{k=1}^{\infty}a_k$ converges. $\square$

## Cross-references

- Course topic: [[en/16-implicit-functions-extrema|chapter 16 “Inverse and implicit functions; extrema”]], [[en/04-numeric-series|chapter 4 “Numerical series”]].
- Facts used: the Taylor–Peano formula ([[en/lectures-2025-26/lecture-65-66#^thm-6-5-1|Theorem 6.5.1]]), statement (∗) from the proof of [[en/lectures-2025-26/lecture-65-66#^thm-6-5-2|Theorem 6.5.2]], the [[en/lectures-2025-26/lecture-65-66#^def-6-6-1|implicit map]] [[en/lectures-2025-26/lecture-65-66#^thm-6-6-1|Theorem 6.6.1]] and the remark to it — [[en/lectures-2025-26/lecture-65-66|lectures 65–66]]; [[en/lectures-2025-26/lecture-63-64#Printed slide 16 (PDF p. 30). Sufficient conditions for equality — Theorem 6.4.1|Theorem 6.4.1]] on the equality of mixed derivatives and [[en/lectures-2025-26/lecture-63-64#Printed slide 21 (PDF p. 41). Computing higher differentials — Theorem 6.4.2|Theorem 6.4.2]] on higher-order differentials — [[en/lectures-2025-26/lecture-63-64|lectures 63–64]]; the Bolzano–Cauchy criterion for sequences — [[en/lectures-2025-26/lecture-13#^thm-2-3-7|Theorem 2.3.7]].
- Continuation: positive series, comparison tests, the d'Alembert and Cauchy tests — [[en/lectures-2025-26/lecture-69-70|lectures 69–70]].

---

[[en/lectures-2025-26/lecture-65-66|← Lectures 65–66]] · [[en/lectures-2025-26/index|Lecture index]] · [[en/lectures-2025-26/lecture-69-70|Lectures 69–70 →]] · [[en/term-index|Terms & theorems]] · [[ru/lectures-2025-26/lecture-67-68|Русский]] · [[es/lectures-2025-26/lecture-67-68|Español]]

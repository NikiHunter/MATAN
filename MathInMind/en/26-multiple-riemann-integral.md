---
title: "The Multiple Riemann Integral"
lang: en
chapter: 26
part: "Semester 3: the lecturer's chapters"
numbering: lecture
lecturer_chapter: 10
---
# 26. The Multiple Riemann Integral

[← 25. Integrals Depending on a Parameter](25-parameter-integrals.md) · [Course index](index.md) · [Terms & theorems](term-index.md)

> **Goal.** Present the lecturer's chapter 10 (§10.1–§10.4, [lectures 79–80](lectures-2025-26/lecture-79-80.md), [81–82](lectures-2025-26/lecture-81-82.md) and [83–84](lectures-2025-26/lecture-83-84.md)), keeping the lecturer's numbering: the [Riemann integral](08-riemann-integration.md#sec-8-2) over an $`n`$-dimensional [brick](#def-10-1-1), the Lebesgue and Darboux criteria, the [integral over an admissible set](#def-10-2-4) and the [Jordan measure](#def-10-2-5), properties of the integral, [Fubini's theorem](17-multiple-integrals.md#fubini-theorem-continuous) and [Cavalieri's principle](#thm-10-4-2). A condensed treatment is in [chapter 17](17-multiple-integrals.md); the [Lebesgue measure](19-measure-theory.md#sec-19-3) and the [Lebesgue integral](20-lebesgue-integration.md#sec-20-1) are in chapters [19](19-measure-theory.md) and [20](20-lebesgue-integration.md).

<a id="sec-10-1"></a>
## §10.1. The Riemann integral over an n-dimensional brick

> <a id="def-10-1-1"></a>**Definition 10.1.1.** The set
> ```math
> I=I_{a,b}=\{x\in\mathbb R^n:\ a_i\le x_i\le b_i,\ i=1,\ldots,n\},\qquad a=(a_1,\ldots,a_n),\ b=(b_1,\ldots,b_n)\in\mathbb R^n,\ a_i\le b_i ,
> ```
> is called a brick (or a box, an interval) in $`\mathbb R^n`$.

> <a id="def-10-1-2"></a>**Definition 10.1.2.** To a brick $`I=I_{a,b}`$ one assigns the number
> ```math
> \mu(I):=\prod_{i=1}^n(b_i-a_i),
> ```
> called the measure of the brick.

Split each segment $`[a_i,b_i]`$ by points into smaller segments; the products of these segments are bricks $`I_1,\ldots,I_k`$ whose union is $`I`$ and which pairwise intersect only along faces, so that $`\mu(I)=\sum_j\mu(I_j)`$.

> <a id="def-10-1-3"></a>**Definition 10.1.3.** A representation of a brick $`I`$ as a union $`I=\bigcup_{j=1}^kI_j`$ of smaller bricks $`I_j`$ is called a partition of the brick $`I`$ and is denoted by $`P`$.

The mesh of a partition is $`\lambda(P)=\max_jd(I_j)`$, where $`d(I_j)`$ is the diameter (the length of the main diagonal) of the brick $`I_j`$.

> <a id="def-10-1-4"></a>**Definition 10.1.4.** If in each brick $`I_j`$ of a [partition](#def-10-1-3) $`P`$ a point $`\xi_j\in I_j`$ is fixed, one speaks of a tagged partition.

> <a id="def-10-1-5"></a>**Definition 10.1.5.** The sum
> ```math
> \sigma(f,P,\xi):=\sum_{i=1}^kf(\xi_i)\,\mu(I_i)
> ```
> is called the (Riemann) integral sum of the function $`f`$ corresponding to the partition of the brick $`I`$ with tags $`\xi`$.

> <a id="def-10-1-6"></a>**Definition 10.1.6.** The quantity
> ```math
> \int_If(x)\,dx:=\lim_{\lambda(P)\to0}\sigma(f,P,\xi)=\lim_{\lambda(P)\to0}\sum_{i=1}^kf(\xi_i)\,\mu(I_i),
> ```
> if the limit exists, is called the (Riemann) integral of the function $`f`$ over the brick $`I\subset\mathbb R^n`$.

The limit is understood as follows: for every $`\varepsilon>0`$ there is $`\delta>0`$ such that $`|\sigma(f,P,\xi)-J|<\varepsilon`$ for all partitions with $`\lambda(P)<\delta`$ and every choice of tags.

> <a id="def-10-1-7"></a>**Definition 10.1.7.** If for a function $`f:I\to\mathbb R`$ the finite limit of [definition 10.1.6](#def-10-1-6) exists, then $`f`$ is called (Riemann) integrable on the brick $`I`$. The set of all such functions is denoted by $`R(I)`$.

> <a id="thm-10-1-1"></a>**Theorem 10.1.1 (necessary condition for integrability).** If $`f\in R(I)`$, then $`f`$ is bounded on $`I`$.

If $`f`$ is unbounded on one of the bricks $`I_{i_0}`$ of a partition (with $`\mu(I_{i_0})>0`$), then moving the point $`\xi_{i_0}`$ makes the integral sum arbitrarily large.

A set $`E\subset\mathbb R^n`$ has (Lebesgue) measure zero if for every $`\varepsilon>0`$ it can be covered by a finite or [countable](01-logic-sets-functions.md#sec-1-5) family of bricks with total measure less than $`\varepsilon`$. Points, smooth curves in $`\mathbb R^2`$ and smooth surfaces in $`\mathbb R^3`$ have measure zero; a countable union and a subset of sets of measure zero have measure zero; a nondegenerate brick does not have measure zero.

> <a id="def-10-1-8"></a>**Definition 10.1.8.** A property holds [almost everywhere](19-measure-theory.md#sec-19-4) on a set $`M`$ if the subset of $`M`$ where it may fail has measure zero.

> <a id="thm-10-1-2"></a>**Theorem 10.1.2 (Lebesgue's criterion).** A function $`f:I\to\mathbb R`$ is Riemann integrable on the brick $`I`$ if and only if $`f`$ is bounded on $`I`$ and continuous almost everywhere on $`I`$.

For a bounded $`f`$ and a partition $`P`$ put $`m_i=\inf_{I_i}f`$, $`M_i=\sup_{I_i}f`$.

> <a id="def-10-1-9"></a>**Definition 10.1.9.** The quantities
> ```math
> s(f,P)=\sum_im_i\,\mu(I_i),\qquad S(f,P)=\sum_iM_i\,\mu(I_i)
> ```
> are called the lower and the upper (Darboux) sum of the function $`f`$ on the brick $`I`$ corresponding to the partition $`P`$.

> <a id="def-10-1-10"></a>**Definition 10.1.10.** The lower and the upper (Darboux) integral of a function $`f:I\to\mathbb R`$ on the brick $`I`$ are the quantities
> ```math
> \underline J=\sup_Ps(f,P),\qquad\overline J=\inf_PS(f,P),
> ```
> where the [supremum](02-real-numbers.md#sec-2-2) and the infimum are taken over all partitions $`P`$ of the brick $`I`$.

> <a id="thm-10-1-3"></a>**Theorem 10.1.3 (Darboux's criterion).** A function $`f:I\to\mathbb R`$ is integrable on the brick $`I`$ if and only if $`f`$ is bounded on $`I`$ and $`\underline J=\overline J`$.

As in the one-dimensional case, $`s(f,P)\le\sigma(f,P,\xi)\le S(f,P)`$; under refinement of a partition the [lower sums](08-riemann-integration.md#sec-8-1) do not decrease and the upper sums do not increase, and always $`\underline J\le\overline J`$.

<a id="sec-10-2"></a>
## §10.2. The integral over a set

> <a id="def-10-2-1"></a>**Definition 10.2.1.** A set $`\Omega\subset\mathbb R^n`$ is called admissible if it is bounded in $`\mathbb R^n`$ and its boundary $`\partial\Omega`$ is a set of measure zero.

> <a id="def-10-2-2"></a>**Definition 10.2.2.** Let $`\Omega\subset\mathbb R^n`$ be an [admissible set](#def-10-2-1). The function
> ```math
> \chi_\Omega(x)=\begin{cases}1, & x\in\Omega,\\ 0, & x\notin\Omega\end{cases}
> ```
> is called the characteristic function of the set $`\Omega`$.

> <a id="def-10-2-3"></a>**Definition 10.2.3.** Let a function $`f`$ be defined on a set $`\Omega`$. Then
> ```math
> f\chi_\Omega(x)=\begin{cases}f(x), & x\in\Omega,\\ 0, & x\notin\Omega\end{cases}
> ```
> (although $`f`$ is not defined outside $`\Omega`$).

> <a id="def-10-2-4"></a>**Definition 10.2.4.** The integral of a function $`f`$ over a bounded set $`\Omega`$ is defined by
> ```math
> \int_\Omega f(x)\,dx:=\int_{I\supset\Omega}f\chi_\Omega(x)\,dx,
> ```
> where $`I`$ is an arbitrary brick containing $`\Omega`$; the integral on the left exists if the integral on the right exists. The set of functions integrable on $`\Omega`$ is denoted by $`R(\Omega)`$.

The value does not depend on the choice of the brick $`I\supset\Omega`$: outside $`\Omega`$ the integrand is zero.

> <a id="def-10-2-5"></a>**Definition 10.2.5.** The (Jordan) measure, or volume, of a bounded set $`\Omega\subset\mathbb R^n`$ is the quantity
> ```math
> \mu(\Omega):=\int_\Omega1\,dx=\int_I\chi_\Omega(x)\,dx\qquad(I\supset\Omega),
> ```
> if this (Riemann) integral exists.

> <a id="def-10-2-6"></a>**Definition 10.2.6.** A set $`\Omega\subset\mathbb R^n`$ is called a set of Jordan measure zero, or a set of volume zero, if for every $`\varepsilon>0`$ it can be covered by a finite system of bricks $`I_1,\dots,I_k`$ such that
> ```math
> \sum_{i=1}^k\mu(I_i)<\varepsilon .
> ```

The function $`\chi_\Omega`$ is discontinuous exactly at the points of $`\partial\Omega`$, so by Lebesgue's criterion a bounded set has a Jordan measure if and only if it is admissible. A [compact](13-metric-spaces.md#sec-13-4) set of Lebesgue measure zero also has Jordan measure zero (a finite subcover can be extracted from a countable cover by open bricks), but, for example, $`\mathbb Q\cap[0,1]`$ has Lebesgue measure zero and no Jordan measure: its boundary is the whole segment $`[0,1]`$.

> <a id="thm-10-2-1"></a>**Theorem 10.2.1.** A function $`f:\Omega\to\mathbb R`$ is integrable on an admissible set $`\Omega`$ if and only if it is bounded and continuous at almost all points of the set $`\Omega`$.

Indeed, the discontinuities of $`f\chi_\Omega`$ lie in the union of the set of discontinuities of $`f`$ in $`\Omega`$ and the boundary $`\partial\Omega`$, and the latter has measure zero.

<a id="sec-10-3"></a>
## §10.3. General properties of the integral

The integral over an admissible set is linear. Let $`\Omega`$ be admissible and $`f,g\in R(\Omega)`$. Then:

1. if $`f\ge0`$ on $`\Omega`$, then $`\int_\Omega f\,dx\ge0`$;
2. if $`f\le g`$ on $`\Omega`$, then $`\int_\Omega f\,dx\le\int_\Omega g\,dx`$;
3. if $`m\le f\le M`$ on $`\Omega`$, then $`m\,\mu(\Omega)\le\int_\Omega f\,dx\le M\,\mu(\Omega)`$;
4. for $`m=\inf_\Omega f`$, $`M=\sup_\Omega f`$ there is $`\theta\in[m,M]`$ such that $`\int_\Omega f\,dx=\theta\,\mu(\Omega)`$;
5. if $`\Omega`$ is [connected](13-metric-spaces.md#sec-13-5) and $`f`$ is continuous, then $`\int_\Omega f\,dx=f(\xi)\,\mu(\Omega)`$ for some point $`\xi\in\Omega`$ (the mean value theorem);
6. if $`m\le f\le M`$ and $`g\ge0`$ on $`\Omega`$, then $`m\int_\Omega g\,dx\le\int_\Omega fg\,dx\le M\int_\Omega g\,dx`$.

> <a id="thm-10-3-1"></a>**Theorem 10.3.1.** Let $`\Omega_1`$, $`\Omega_2`$ be admissible sets in $`\mathbb R^n`$, and let $`f`$ be a function defined on $`\Omega_1\cup\Omega_2`$. Then:
>
> ① the existence of the integrals is related as follows:
> ```math
> \exists\int_{\Omega_1\cup\Omega_2}f(x)\,dx\iff\exists\int_{\Omega_i}f(x)\,dx\ \ (i=1,2)\implies\exists\int_{\Omega_1\cap\Omega_2}f(x)\,dx;
> ```
>
> ② if $`\mu(\Omega_1\cap\Omega_2)=0`$, then, provided the integrals exist,
> ```math
> \int_{\Omega_1\cup\Omega_2}f(x)\,dx=\int_{\Omega_1}f(x)\,dx+\int_{\Omega_2}f(x)\,dx .
> ```

Item ① follows from Lebesgue's criterion, item ② from the identity $`\chi_{\Omega_1\cup\Omega_2}=\chi_{\Omega_1}+\chi_{\Omega_2}-\chi_{\Omega_1\cap\Omega_2}`$ and the fact that the integral over a set of measure zero is zero.

> <a id="prop-10-3-1"></a>**Proposition 10.3.1.** If $`f\in R(\Omega)`$, then $`|f|\in R(\Omega)`$ and
> ```math
> \Bigl|\int_\Omega f(x)\,dx\Bigr|\le\int_\Omega|f(x)|\,dx .
> ```

The function $`|f|`$ is bounded and continuous wherever $`f`$ is; the inequality follows from property 2 applied to $`-|f|\le f\le|f|`$.

<a id="sec-10-4"></a>
## §10.4. Fubini's theorem

> <a id="thm-10-4-1"></a>**Theorem 10.4.1 (Fubini).** Let $`I=I_x\times I_y\subset\mathbb R^n`$, where $`I_x`$ is a brick in $`\mathbb R^m`$, $`I_y`$ is a brick in $`\mathbb R^k`$, $`m+k=n`$. If the function $`f`$ is integrable on $`I`$ and, moreover,
>
> $`(\ast)`$ for each $`x\in I_x`$ the function $`y\mapsto f(x,y)`$ is integrable on $`I_y`$,
>
> then the function $`F(x)=\int_{I_y}f(x,y)\,dy`$ is integrable on $`I_x`$ and
> ```math
> \int_If(x,y)\,dx\,dy=\int_{I_x}\Bigl(\int_{I_y}f(x,y)\,dy\Bigr)dx .
> ```

*Proof idea.* For a partition $`P=P_x\times P_y`$ we have $`s(f,P)\le s(F,P_x)\le S(F,P_x)\le S(f,P)`$, where in the middle are the Darboux sums of the function $`F`$; the outer sums converge to $`\int_If`$, and Darboux's criterion finishes the proof.

> <a id="cor-10-4-1"></a>**Corollary 10.4.1.** Let $`I=I_1\times\dots\times I_n\subset\mathbb R^n`$, $`I_i=[a_i,b_i]`$, let the function $`f`$ be integrable on $`I`$, and let condition $`(\ast)`$ hold at every step (for example, $`f`$ is continuous on $`I`$). Then
> ```math
> \int_If(x)\,dx=\int_{a_n}^{b_n}dx_n\int_{a_{n-1}}^{b_{n-1}}dx_{n-1}\dots\int_{a_1}^{b_1}f(x_1,x_2,\dots,x_n)\,dx_1 .
> ```

> <a id="cor-10-4-2"></a>**Corollary 10.4.2.** Let $`D\subset\mathbb R^{n-1}`$ be an admissible set, let the functions $`\varphi_1,\varphi_2`$ be continuous on $`\overline D`$ with $`\varphi_1\le\varphi_2`$ on $`\overline D`$, and let
> ```math
> E=\{(x,y)\in\mathbb R^n:\ x\in D,\ \varphi_1(x)\le y\le\varphi_2(x)\}.
> ```
> If $`f\in R(E)`$ and for each $`x\in D`$ the integral $`\int_{\varphi_1(x)}^{\varphi_2(x)}f(x,y)\,dy`$ exists, then
> ```math
> \int_Ef(x,y)\,dx\,dy=\int_Ddx\int_{\varphi_1(x)}^{\varphi_2(x)}f(x,y)\,dy .
> ```

> <a id="cor-10-4-3"></a>**Corollary 10.4.3.** Under the assumptions of [corollary 10.4.2](#cor-10-4-2) the set $`E`$ is admissible, and its volume is
> ```math
> \mu(E)=\int_D\bigl(\varphi_2(x)-\varphi_1(x)\bigr)\,dx .
> ```

> <a id="thm-10-4-2"></a>**Theorem 10.4.2 (Cavalieri's principle).** Let $`A`$ and $`B`$ be two bodies in $`\mathbb R^3`$ having volume (Jordan measurable), and let $`A_c`$ and $`B_c`$ be their sections by the plane $`z=c`$. If for each $`c\in\mathbb R`$ the sections $`A_c`$, $`B_c`$ are measurable and have the same area, then the bodies $`A`$ and $`B`$ have the same volume.

By Fubini's theorem $`\mu(A)=\int\mu(A_c)\,dc`$, and the same holds for $`B`$.

## Worked example

**An integral over a curvilinear region.** Let $`E=\{(x,y):\ 0\le x\le1,\ x^2\le y\le x\}`$. By [corollary 10.4.2](#cor-10-4-2) with $`D=[0,1]`$, $`\varphi_1=x^2`$, $`\varphi_2=x`$:
```math
\iint_Exy\,dx\,dy=\int_0^1x\,dx\int_{x^2}^{x}y\,dy=\int_0^1\frac{x^3-x^5}{2}\,dx=\frac12\Bigl(\frac14-\frac16\Bigr)=\frac1{24}.
```

**The volume of a ball.** The section of the unit ball $`B\subset\mathbb R^3`$ by the plane $`z=c`$, $`|c|\le1`$, is a disc of radius $`\sqrt{1-c^2}`$ and area $`\pi(1-c^2)`$. By Fubini's theorem (as in Cavalieri's principle)
```math
\mu(B)=\int_{-1}^{1}\pi(1-c^2)\,dc=\pi\Bigl(2-\frac23\Bigr)=\frac{4\pi}{3}.
```

## Common pitfalls

1. Confusing Lebesgue measure zero (countable covers) with Jordan measure zero (finite covers): $`\mathbb Q\cap[0,1]`$ has the former but not the latter.
2. Believing that every bounded set has a volume: a set with a non-admissible boundary (for example, $`\mathbb Q^2\cap[0,1]^2`$) has no Jordan measure.
3. Applying Fubini's theorem without checking condition $`(\ast)`$: the function equal to $`1`$ for $`x=\frac12`$, $`y\in\mathbb Q`$ and to $`0`$ at the other points of $`[0,1]^2`$ is integrable (its discontinuities lie on a segment), but for $`x=\frac12`$ the inner integral in $`y`$ does not exist.
4. Setting the limits wrongly when changing the order of integration: the region must be described anew as a "curvilinear trapezoid" with respect to the other variable.
5. Adding integrals over overlapping sets: equality ② of [theorem 10.3.1](#thm-10-3-1) requires $`\mu(\Omega_1\cap\Omega_2)=0`$.

## Exercises

1. Compute $`\iint_{[0,1]\times[0,2]}(x+y^2)\,dx\,dy`$.
2. Change the order of integration in $`\int_0^1dx\int_x^1f(x,y)\,dy`$.
3. Find the volume of the tetrahedron $`\{x,y,z\ge0,\ x+y+z\le1\}`$.
4. Does the set $`\{(x,y)\in[0,1]^2:\ x\in\mathbb Q\}`$ have a Jordan measure?

<details>
<summary>Short answers</summary>

1. $`\int_0^2\bigl(\frac12+y^2\bigr)dy=1+\frac83=\frac{11}3`$.
2. $`\int_0^1dy\int_0^yf(x,y)\,dx`$.
3. By [corollary 10.4.3](#cor-10-4-3) with $`D=\{x,y\ge0,\ x+y\le1\}`$, $`\varphi_1=0`$, $`\varphi_2=1-x-y`$: $`\int_0^1\frac{(1-x)^2}{2}\,dx=\frac16`$.
4. No: its boundary is the whole square $`[0,1]^2`$, which is not a set of measure zero, i.e. the set is not admissible.
</details>

---

[← 25. Integrals Depending on a Parameter](25-parameter-integrals.md) · [Course index](index.md) · [Terms & theorems](term-index.md)

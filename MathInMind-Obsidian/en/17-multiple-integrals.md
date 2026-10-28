---
title: "Multiple Integrals and Change of Variables"
lang: en
chapter: 17
part: "Integration in several variables"
aliases: ["Multiple Integrals and Change of Variables (en)"]
tags: [mathinmind/en, mathinmind/chapter]
---
# 17. Multiple Integrals and Change of Variables

[[en/16-implicit-functions-extrema|← 16. Inverse and Implicit Functions; Extrema]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]] · [[en/18-vector-calculus|18. Vector Calculus and Integral Theorems →]]

> [!abstract] Goal
> Evaluate integrals over multidimensional regions using iteration, symmetry, and geometric coordinate changes.

## 17.1 Definition and iterated integrals

For a bounded function on a rectangle $R=\prod_{i=1}^{n}[a_i,b_i]$, [[en/08-riemann-integration#8.1 Partitions and Darboux sums|partitions]] into small rectangles define lower and upper Darboux sums using volumes $\Delta V_j$. Integrability again means that upper and lower sums can be made arbitrarily close. Continuous functions on closed bounded Jordan-measurable regions are integrable.

> [!theorem] Fubini's theorem — continuous case
> If $f$ is continuous on $R=[a,b]\times[c,d]$, then
> $$
> \iint_R f(x,y)\,dA
> =\int_a^b\left(\int_c^d f(x,y)\,dy\right)dx
> =\int_c^d\left(\int_a^b f(x,y)\,dx\right)dy.
> $$

^fubini-theorem-continuous

For general Lebesgue-integrable functions, absolute integrability justifies changing the order; [[en/20-lebesgue-integration#20.4 Product measures and Fubini–Tonelli|Tonelli's theorem]] permits it for nonnegative measurable functions. See Chapters 19–20.

Over a region

$$
D=\{(x,y):a\le x\le b,\ \varphi_1(x)\le y\le\varphi_2(x)\},
$$

we have $\iint_Df\,dA=\int_a^b\int_{\varphi_1(x)}^{\varphi_2(x)}f(x,y)\,dy\,dx$. Sketch the region before choosing limits.

## 17.2 Change of variables

Let $T:U\to V$ be a $C^1$ coordinate transformation, [[en/01-logic-sets-functions#1.4 Functions|injective]] except possibly on a negligible set, with $DT$ invertible. Then

$$
\int_V f(v)\,dv
=\int_U f(T(u))\,|\det DT(u)|\,du.
$$

The absolute Jacobian determinant measures local volume scaling. Forgetting it changes the value; using the signed determinant is incorrect for unoriented area and volume integrals.

Important substitutions are:

$$
(x,y)=(r\cos\theta,r\sin\theta),\qquad dA=r\,dr\,d\theta;
$$
$$
(x,y,z)=(r\cos\theta,r\sin\theta,z),\qquad dV=r\,dr\,d\theta\,dz;
$$

and [[#17.3 Choosing coordinates|spherical coordinates]]

$$
(x,y,z)=(\rho\sin\varphi\cos\theta,
\rho\sin\varphi\sin\theta,\rho\cos\varphi),
$$
$$
dV=\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta,
$$

where $\rho\ge0$, $0\le\varphi\le\pi$, and usually $0\le\theta<2\pi$.

## 17.3 Choosing coordinates

Polar or cylindrical coordinates suit disks, sectors, cylinders, and radial integrands. Spherical coordinates suit balls, cones, and shells. Symmetry often eliminates odd contributions before any calculation.

Double and [[#17.1 Definition and iterated integrals|triple integrals]] compute

$$
\operatorname{area}(D)=\iint_D1\,dA,
\qquad
\operatorname{vol}(\Omega)=\iiint_\Omega1\,dV.
$$

With density $\rho$, mass is $M=\int_\Omega\rho\,dV$, and the center of mass has coordinates

$$
\bar x_i=\frac1M\int_\Omega x_i\rho\,dV.
$$

Moments of inertia have the form $I=\int_\Omega r^2\rho\,dV$, where $r$ is distance to the rotation axis.

## Worked example

The volume of a ball $B_R$ follows from spherical coordinates:

$$
V=\int_0^{2\pi}\int_0^\pi\int_0^R
\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta.
$$

The factors integrate independently:

$$
V=\left(\int_0^{2\pi}d\theta\right)
\left(\int_0^\pi\sin\varphi\,d\varphi\right)
\left(\int_0^R\rho^2\,d\rho\right)
=2\pi\cdot2\cdot\frac{R^3}{3}
=\frac{4\pi R^3}{3}.
$$

## Common pitfalls

1. [[en/14-several-variables#^iterated-limit-warning|Iterated limits]] describe a region; they are not interchangeable without checking the domain or integrability.
2. Always include the absolute [[#17.2 Change of variables|Jacobian]] factor.
3. In spherical coordinates, $\varphi$ here is the polar angle from the positive $z$-axis, not the azimuth.

## Exercises

1. Evaluate $\iint_T x\,dA$ over the triangle $x,y\ge0$, $x+y\le1$.
2. Compute the area of a disk of radius $R$ using polar coordinates.
3. Set up an integral for the volume inside $x^2+y^2+z^2\le2Rz$.

> [!answer]- Short answers
> 1. $\int_0^1\int_0^{1-x}x\,dy\,dx=\int_0^1x(1-x)\,dx=1/6$.
> 2. $\int_0^{2\pi}\int_0^Rr\,dr\,d\theta=\pi R^2$.
> 3. The sphere is $\rho\le2R\cos\varphi$ with $0\le\varphi\le\pi/2$; use $V=\int_0^{2\pi}\int_0^{\pi/2}\int_0^{2R\cos\varphi}\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta$.

---

[[en/16-implicit-functions-extrema|← 16. Inverse and Implicit Functions; Extrema]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]] · [[en/18-vector-calculus|18. Vector Calculus and Integral Theorems →]]

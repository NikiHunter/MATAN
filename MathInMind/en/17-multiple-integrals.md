---
title: "Multiple Integrals and Change of Variables"
lang: en
chapter: 17
part: "Integration in several variables"
---
# 17. Multiple Integrals and Change of Variables

[← 16. Inverse and Implicit Functions; Extrema](16-implicit-functions-extrema.md) · [Course index](index.md) · [Terms & theorems](term-index.md) · [18. Vector Calculus and Integral Theorems →](18-vector-calculus.md)

> **Goal.** Evaluate integrals over multidimensional regions using iteration, symmetry, and geometric coordinate changes.

<a id="sec-17-1"></a>
## 17.1 Definition and iterated integrals

For a bounded function on a rectangle $`R=\prod_{i=1}^{n}[a_i,b_i]`$, [partitions](08-riemann-integration.md#sec-8-1) into small rectangles define lower and upper Darboux sums using volumes $`\Delta V_j`$. Integrability again means that upper and lower sums can be made arbitrarily close. Continuous functions on closed bounded Jordan-measurable regions are integrable.

> <a id="fubini-theorem-continuous"></a>**Fubini's theorem — continuous case.** If $`f`$ is continuous on $`R=[a,b]\times[c,d]`$, then
> ```math
> \iint_R f(x,y)\,dA
> =\int_a^b\left(\int_c^d f(x,y)\,dy\right)dx
> =\int_c^d\left(\int_a^b f(x,y)\,dx\right)dy.
> ```

For general Lebesgue-integrable functions, absolute integrability justifies changing the order; [Tonelli's theorem](20-lebesgue-integration.md#sec-20-4) permits it for nonnegative measurable functions. See Chapters 19–20.

Over a region

```math
D=\{(x,y):a\le x\le b,\ \varphi_1(x)\le y\le\varphi_2(x)\},
```

we have $`\iint_Df\,dA=\int_a^b\int_{\varphi_1(x)}^{\varphi_2(x)}f(x,y)\,dy\,dx`$. Sketch the region before choosing limits.

<a id="sec-17-2"></a>
## 17.2 Change of variables

Let $`T:U\to V`$ be a $`C^1`$ coordinate transformation, [injective](01-logic-sets-functions.md#sec-1-4) except possibly on a negligible set, with $`DT`$ invertible. Then

```math
\int_V f(v)\,dv
=\int_U f(T(u))\,|\det DT(u)|\,du.
```

The absolute Jacobian determinant measures local volume scaling. Forgetting it changes the value; using the signed determinant is incorrect for unoriented area and volume integrals.

Important substitutions are:

```math
(x,y)=(r\cos\theta,r\sin\theta),\qquad dA=r\,dr\,d\theta;
```
```math
(x,y,z)=(r\cos\theta,r\sin\theta,z),\qquad dV=r\,dr\,d\theta\,dz;
```

and [spherical coordinates](#sec-17-3)

```math
(x,y,z)=(\rho\sin\varphi\cos\theta,
\rho\sin\varphi\sin\theta,\rho\cos\varphi),
```
```math
dV=\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta,
```

where $`\rho\ge0`$, $`0\le\varphi\le\pi`$, and usually $`0\le\theta<2\pi`$.

<a id="sec-17-3"></a>
## 17.3 Choosing coordinates

Polar or cylindrical coordinates suit disks, sectors, cylinders, and radial integrands. Spherical coordinates suit balls, cones, and shells. Symmetry often eliminates odd contributions before any calculation.

Double and [triple integrals](#sec-17-1) compute

```math
\operatorname{area}(D)=\iint_D1\,dA,
\qquad
\operatorname{vol}(\Omega)=\iiint_\Omega1\,dV.
```

With density $`\rho`$, mass is $`M=\int_\Omega\rho\,dV`$, and the center of mass has coordinates

```math
\bar x_i=\frac1M\int_\Omega x_i\rho\,dV.
```

Moments of inertia have the form $`I=\int_\Omega r^2\rho\,dV`$, where $`r`$ is distance to the rotation axis.

## Worked example

The volume of a ball $`B_R`$ follows from spherical coordinates:

```math
V=\int_0^{2\pi}\int_0^\pi\int_0^R
\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta.
```

The factors integrate independently:

```math
V=\left(\int_0^{2\pi}d\theta\right)
\left(\int_0^\pi\sin\varphi\,d\varphi\right)
\left(\int_0^R\rho^2\,d\rho\right)
=2\pi\cdot2\cdot\frac{R^3}{3}
=\frac{4\pi R^3}{3}.
```

## Common pitfalls

1. [Iterated limits](14-several-variables.md#iterated-limit-warning) describe a region; they are not interchangeable without checking the domain or integrability.
2. Always include the absolute [Jacobian](#sec-17-2) factor.
3. In spherical coordinates, $`\varphi`$ here is the polar angle from the positive $`z`$-axis, not the azimuth.

## Exercises

1. Evaluate $`\iint_T x\,dA`$ over the triangle $`x,y\ge0`$, $`x+y\le1`$.
2. Compute the area of a disk of radius $`R`$ using polar coordinates.
3. Set up an integral for the volume inside $`x^2+y^2+z^2\le2Rz`$.

<details>
<summary>Short answers</summary>

1. $`\int_0^1\int_0^{1-x}x\,dy\,dx=\int_0^1x(1-x)\,dx=1/6`$.
2. $`\int_0^{2\pi}\int_0^Rr\,dr\,d\theta=\pi R^2`$.
3. The sphere is $`\rho\le2R\cos\varphi`$ with $`0\le\varphi\le\pi/2`$; use $`V=\int_0^{2\pi}\int_0^{\pi/2}\int_0^{2R\cos\varphi}\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta`$.
</details>

---

[← 16. Inverse and Implicit Functions; Extrema](16-implicit-functions-extrema.md) · [Course index](index.md) · [Terms & theorems](term-index.md) · [18. Vector Calculus and Integral Theorems →](18-vector-calculus.md)

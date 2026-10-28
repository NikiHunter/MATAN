---
title: "Differentiation of Several-Variable Mappings"
lang: en
chapter: 15
part: "Several variables and topology"
aliases: ["Differentiation of Several-Variable Mappings (en)"]
tags: [mathinmind/en, mathinmind/chapter]
---
# 15. Differentiation of Several-Variable Mappings

[[en/14-several-variables|← 14. Functions of Several Variables]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]] · [[en/16-implicit-functions-extrema|16. Inverse and Implicit Functions; Extrema →]]

> [!abstract] Goal
> Use the [[#15.1 The total derivative|total derivative]] as a linear map and connect it with [[#15.2 Partial and directional derivatives|partial derivatives]], gradients, and higher approximations.

## 15.1 The total derivative

For $F:D\subseteq\mathbb R^n\to\mathbb R^m$ and an [[en/13-metric-spaces#13.2 Open and closed sets|interior point]] $a$, the derivative is a linear map $DF(a):\mathbb R^n\to\mathbb R^m$ such that

$$
F(a+h)=F(a)+DF(a)h+o(\|h\|)\qquad(h\to0).
$$

Equivalently, $\|F(a+h)-F(a)-DF(a)h\|/\|h\|\to0$. Differentiability implies continuity. The matrix representing $DF(a)$ in standard coordinates is the **Jacobian matrix**.

For scalar $f$, the derivative is represented by the gradient $\nabla f(a)$, and

$$
f(a+h)=f(a)+\nabla f(a)\cdot h+o(\|h\|).
$$

The gradient points in the direction of greatest increase among unit directions, with maximum directional derivative $\|\nabla f(a)\|$.

## 15.2 Partial and directional derivatives

Partial derivatives are

$$
\frac{\partial f}{\partial x_i}(a)
=\lim_{t\to0}\frac{f(a+te_i)-f(a)}t.
$$

If $F$ is differentiable, all partial derivatives exist and

$$
DF(a)=\left(\frac{\partial F_i}{\partial x_j}(a)\right)_{i,j}.
$$

The converse requires care: existence of partial derivatives, even near $a$, does not guarantee differentiability. A sufficient condition is that all partial derivatives exist near $a$ and are continuous at $a$; then $F$ is differentiable at $a$.

The directional derivative along a vector $v$ is

$$
D_vf(a)=\left.\frac{d}{dt}f(a+tv)\right|_{t=0}.
$$

If $f$ is differentiable, $D_vf(a)=\nabla f(a)\cdot v$. Existence of every directional derivative alone still does not imply differentiability.

## 15.3 Chain rule and tangent planes

If $F$ is differentiable at $a$ and $G$ at $F(a)$, then

$$
D(G\circ F)(a)=DG(F(a))\,DF(a),
$$

where the product is matrix multiplication. This single formula contains all multivariable chain rules.

For a scalar $f(x,y)$ differentiable at $(a,b)$, the tangent plane to its graph is

$$
z=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b).
$$

A level surface $F(x,y,z)=c$ with $\nabla F(a)\ne0$ has tangent plane $\nabla F(a)\cdot(x-a)=0$. Thus the gradient is normal to the level set.

## 15.4 Higher derivatives and Taylor's formula

A function is $C^k$ if all partial derivatives through order $k$ exist and are continuous.

> [!theorem] Clairaut–Schwarz theorem
> If mixed second partial derivatives are continuous near a point, their order can be interchanged: $f_{xy}=f_{yx}$.

^clairaut-schwarz-theorem

For $f\in C^2$, the Hessian $Hf(a)$ is the symmetric matrix of second partial derivatives. Second-order Taylor expansion is

$$
f(a+h)=f(a)+\nabla f(a)\cdot h
+\frac12h^{T}Hf(a)h+o(\|h\|^2).
$$

The quadratic form $h^THh$ governs local curvature and is central to extrema in the next chapter.

## Worked example

Let $f(x,y)=x^2e^y$ and $a=(1,0)$. Then

$$
f(a)=1,\qquad \nabla f=(2xe^y,x^2e^y),\qquad \nabla f(a)=(2,1).
$$

The first-order approximation is $f(1+h,k)\approx1+2h+k$. For the unit direction $v=(3/5,4/5)$,

$$
D_vf(a)=(2,1)\cdot(3/5,4/5)=2.
$$

## Common pitfalls

1. Partial derivatives alone do not prove total differentiability.
2. The [[en/17-multiple-integrals#17.2 Change of variables|Jacobian]] is a matrix of a linear map, not merely a table of numbers.
3. For a level set, the gradient is normal; for a graph $z=f(x,y)$, the [[#15.3 Chain rule and tangent planes|tangent plane]] uses the linear approximation.

## Exercises

1. Compute the Jacobian and determinant of $F(r,\theta)=(r\cos\theta,r\sin\theta)$.
2. Find the tangent plane to $z=x^2+y^2$ at $(1,1,2)$.
3. Compute the Hessian of $f(x,y)=x^2e^y$ at $(1,0)$.

> [!answer]- Short answers
> 1. The Jacobian rows are $(\cos\theta,-r\sin\theta)$ and $(\sin\theta,r\cos\theta)$; its determinant is $r$.
> 2. $z-2=2(x-1)+2(y-1)$.
> 3. The Hessian at $(1,0)$ is $\begin{pmatrix}2&2\\2&1\end{pmatrix}$.

---

[[en/14-several-variables|← 14. Functions of Several Variables]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]] · [[en/16-implicit-functions-extrema|16. Inverse and Implicit Functions; Extrema →]]

---
title: "Inverse and Implicit Functions; Extrema"
lang: en
chapter: 16
part: "Several variables and topology"
---
# 16. Inverse and Implicit Functions; Extrema

[Previous](15-multivariable-differentiation.md) · [Course index](index.md) · [Next](17-multiple-integrals.md)

> **Goal.** Apply nondegenerate derivative conditions and find local or constrained extrema systematically.

## 16.1 Unconstrained local extrema

Let $f$ be differentiable on an open set. If $f$ has a local extremum at an interior point $a$, then $\nabla f(a)=0$. Such points are called stationary or critical. Endpoints and boundary points require a separate investigation.

For $f\in C^2$, inspect the Hessian $H=Hf(a)$ at a critical point:

- $H$ positive definite $\implies$ strict local minimum;
- $H$ negative definite $\implies$ strict local maximum;
- $H$ indefinite $\implies$ saddle point;
- $H$ semidefinite or singular $\implies$ the test is inconclusive.

In two variables, with $D=f_{xx}f_{yy}-f_{xy}^2$, a minimum occurs when $D>0$ and $f_{xx}>0$, a maximum when $D>0$ and $f_{xx}<0$, and a saddle when $D<0$.

For example, $f(x,y)=x^2-y^2$ has Hessian $\operatorname{diag}(2,-2)$ at the origin, hence a saddle. The functions $x^4+y^4$ and $-x^4-y^4$ show why $D=0$ requires further analysis.

## 16.2 Inverse function theorem

> **Theorem.** Let $F:\mathbb R^n\to\mathbb R^n$ be $C^1$ near $a$, and suppose $DF(a)$ is invertible. Then $F$ maps a neighborhood of $a$ bijectively onto a neighborhood of $F(a)$, the inverse is $C^1$, and
> $$DF^{-1}(F(a))=(DF(a))^{-1}.$$

In coordinates, invertibility means $\det DF(a)\ne0$. The theorem is local: a nonvanishing Jacobian determinant everywhere does not by itself imply global injectivity.

This result explains when a coordinate change is locally reversible and underlies the implicit-function theorem.

## 16.3 Implicit function theorem

Suppose $F(x,y)$ takes values in $\mathbb R^k$, where $x\in\mathbb R^n$ and $y\in\mathbb R^k$. Assume $F$ is $C^1$, $F(a,b)=0$, and the partial Jacobian $D_yF(a,b)$ is invertible. Then near $(a,b)$ the equation

$$
F(x,y)=0
$$

defines $y$ uniquely as a $C^1$ function $y=g(x)$, with $g(a)=b$. Moreover,

$$
Dg(a)=-(D_yF(a,b))^{-1}D_xF(a,b).
$$

For one equation $F(x,y)=0$ with $F_y\ne0$, this reduces to

$$
\frac{dy}{dx}=-\frac{F_x}{F_y}.
$$

The theorem guarantees existence and smoothness, not necessarily an explicit elementary formula.

## 16.4 Lagrange multipliers

For one smooth constraint $g(x)=c$, assume $\nabla g(a)\ne0$. If $f$ has a local extremum on the constraint surface at $a$, then there is $\lambda$ such that

$$
\nabla f(a)=\lambda\nabla g(a),\qquad g(a)=c.
$$

Geometrically, the gradients are normal to the same level surface, so they must be parallel. For several independent constraints $g_1,\ldots,g_k$,

$$
\nabla f(a)=\sum_{i=1}^{k}\lambda_i\nabla g_i(a),
$$

provided the constraint gradients are linearly independent.

The multiplier condition is necessary, not always sufficient. Compare all critical points, singular points where the rank condition fails, and boundary behavior; use compactness to establish global extrema when applicable.

## Worked example

Optimize $f(x,y)=x+y$ subject to $x^2+y^2=1$. Lagrange's equations give

$$
1=2\lambda x,\qquad 1=2\lambda y,
$$

so $x=y$. On the circle, the candidates are $\pm(1/\sqrt2,1/\sqrt2)$. The maximum is $\sqrt2$ and the minimum is $-\sqrt2$. This agrees with Cauchy–Schwarz: $|x+y|\le\sqrt2\sqrt{x^2+y^2}$.

## Common pitfalls

1. A critical point is not automatically an extremum.
2. Lagrange multipliers require a nondegenerate constraint and do not replace comparison of candidates.
3. The inverse and implicit function theorems are local statements.

## Exercises

1. Classify the origin for $f(x,y)=x^2+2y^2$.
2. For $x^2+y^2=1$ near $(0,1)$, find $dy/dx$ implicitly.
3. Find the extrema of $xy$ on $x^2+y^2=1$.

<details>
<summary>Short answers</summary>

1. The Hessian $\operatorname{diag}(2,4)$ is positive definite: strict local and global minimum.
2. $2x+2yy'=0$, hence $y'=-x/y$ and $y'(0)=0$ at $(0,1)$.
3. Maximum $1/2$ at $x=y=\pm1/\sqrt2$ with equal signs; minimum $-1/2$ at opposite signs.
</details>

---

[Previous](15-multivariable-differentiation.md) · [Course index](index.md) · [Next](17-multiple-integrals.md)

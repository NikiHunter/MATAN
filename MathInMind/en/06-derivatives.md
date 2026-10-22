---
title: "Differentiation in One Variable"
lang: en
chapter: 6
part: "One-variable calculus"
---
# 6. Differentiation in One Variable

[Previous](05-limits-continuity.md) · [Course index](index.md) · [Next](07-taylor-convexity.md)

> **Goal.** Interpret the derivative as local linear approximation and apply the rules of differentiation reliably.

## 6.1 Definition and linear approximation

The derivative of $f$ at $a$ is

$$
f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}h
$$

when this finite limit exists. Equivalently,

$$
f(a+h)=f(a)+f'(a)h+o(h)\qquad(h\to0).
$$

Thus $L(h)=f(a)+f'(a)h$ is the best linear approximation near $a$. The tangent line is $y=f(a)+f'(a)(x-a)$.

Differentiability implies continuity because

$$
f(a+h)-f(a)=h\frac{f(a+h)-f(a)}h\to0.
$$

The converse fails: $|x|$ is continuous but not differentiable at zero, since its one-sided difference quotients are $-1$ and $1$.

One-sided derivatives are defined by one-sided limits. A finite two-sided derivative exists exactly when both exist and agree.

## 6.2 Differentiation rules

For differentiable $f,g$ and constants $\alpha,\beta$,

$$
(\alpha f+\beta g)'=\alpha f'+\beta g',
$$
$$
(fg)'=f'g+fg',
\qquad
\left(\frac fg\right)'=\frac{f'g-fg'}{g^2}\quad(g\ne0).
$$

> **Chain rule.** If $f$ is differentiable at $a$ and $g$ at $f(a)$, then
> $$(g\circ f)'(a)=g'(f(a))f'(a).$$

For an inverse function, if $f$ is differentiable and strictly monotone near $a$, with $f'(a)\ne0$, then

$$
(f^{-1})'(f(a))=\frac1{f'(a)}.
$$

Standard derivatives include

$$
(x^p)'=px^{p-1},\quad (e^x)'=e^x,\quad(\log x)'=\frac1x,
$$
$$
(\sin x)'=\cos x,\quad(\cos x)'=-\sin x,\quad(\arctan x)'=\frac1{1+x^2}.
$$

For $f(x)>0$, logarithmic differentiation gives
$(f^g)'=f^g(g'\log f+gf'/f)$.

## 6.3 Differentials and parametric curves

The differential $df(a;h)=f'(a)h$ is the linear part of the increment. Writing $dy=f'(x)\,dx$ is useful for approximation and substitution, but $dy/dx$ is defined through the derivative, not as a literal quotient of numbers.

If $x=\varphi(t)$, $y=\psi(t)$ are differentiable and $\varphi'(t)\ne0$, then

$$
\frac{dy}{dx}=\frac{\psi'(t)}{\varphi'(t)}.
$$

Higher derivatives are defined recursively by $f^{(n+1)}=(f^{(n)})'$. Leibniz's product formula is

$$
(fg)^{(n)}=\sum_{k=0}^{n}\binom nk f^{(k)}g^{(n-k)}.
$$

## 6.4 Local information from the derivative

> **Fermat's theorem.** If $f$ has a local extremum at an interior point $a$ and is differentiable there, then $f'(a)=0$.

The converse is false: $x^3$ has zero derivative at zero but no extremum. If $f'(x)>0$ throughout an interval, $f$ is strictly increasing there; this follows from the mean value theorem in the next chapter.

> **Darboux property.** A derivative need not be continuous, but on an interval it attains every value between any two of its values.

Therefore a derivative cannot have a jump discontinuity, though it can oscillate. A classic example is $x^2\sin(1/x)$ away from zero, completed by zero at zero.

## Worked example

Differentiate $f(x)=x^x$ for $x>0$. Write $f(x)=e^{x\log x}$. By the chain and product rules,

$$
f'(x)=e^{x\log x}(\log x+1)=x^x(\log x+1).
$$

The derivative is negative on $(0,1/e)$ and positive on $(1/e,\infty)$, so the minimum occurs at $x=1/e$.

## Common pitfalls

1. Continuity does not imply differentiability.
2. The chain rule requires a product by the inner derivative.
3. $f'(a)=0$ identifies a stationary point, not automatically an extremum.

## Exercises

1. Use the definition to find the derivative of $1/x$ at $a\ne0$.
2. Differentiate $\arcsin x$ by the inverse-function rule.
3. Find the tangent line to the curve $x=t^2$, $y=t^3$ at $t=1$.

<details>
<summary>Short answers</summary>

1. The difference quotient is $-1/(a(a+h))$, which tends to $-1/a^2$.
2. $(\arcsin x)'=1/\sqrt{1-x^2}$ for $|x|<1$.
3. $dy/dx=3t/2$, so the slope is $3/2$ at $(1,1)$; the line is $y-1=\frac32(x-1)$.
</details>

---

[Previous](05-limits-continuity.md) · [Course index](index.md) · [Next](07-taylor-convexity.md)

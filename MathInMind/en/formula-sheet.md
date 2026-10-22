---
title: "Mathematical Analysis Formula Sheet"
lang: en
---
# Mathematical Analysis Formula Sheet

[Course index](index.md) · [Notation](00-notation.md) · [Glossary](glossary.md)

> **Use with care.** This sheet recalls formulas, not their hypotheses. Follow the chapter links before applying a theorem.

## Sequences and series — [Chapters 3–4](03-sequences.md)

$$
a_n\to a,\ b_n\to b\implies a_nb_n\to ab,\quad a_n+b_n\to a+b.
$$

Monotone + bounded $\implies$ convergent. In $\mathbb R$, convergent $\iff$ Cauchy.

$$
\sum_{n=0}^{\infty}q^n=\frac1{1-q}\quad(|q|<1),
\qquad
\sum_{n=1}^{\infty}\frac1{n^p}<\infty\iff p>1.
$$

If $b_n\downarrow0$, then $\sum(-1)^{n-1}b_n$ converges and $|R_N|\le b_{N+1}$.

## Derivatives and Taylor — [Chapters 6–7](06-derivatives.md)

$$
(fg)'=f'g+fg',\qquad
(g\circ f)'(a)=g'(f(a))f'(a),\qquad
(f^{-1})'(f(a))=\frac1{f'(a)}.
$$

$$
f(b)-f(a)=f'(c)(b-a),\qquad
f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n(x).
$$

$$
e^x=\sum_{n=0}^{\infty}\frac{x^n}{n!},\qquad
\sin x=\sum_{n=0}^{\infty}\frac{(-1)^nx^{2n+1}}{(2n+1)!},
$$
$$
\cos x=\sum_{n=0}^{\infty}\frac{(-1)^nx^{2n}}{(2n)!},\qquad
\log(1+x)=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}x^n}{n}\quad(-1<x\le1).
$$

Convex differentiable $f$ satisfies $f(y)\ge f(x)+f'(x)(y-x)$ and Jensen's inequality.

## One-variable integration — [Chapters 8–9](08-riemann-integration.md)

$$
\frac{d}{dx}\int_a^x f(t)\,dt=f(x),
\qquad
\int_a^b f(x)\,dx=F(b)-F(a)\quad(F'=f).
$$

$$
\int_a^b u\,dv=[uv]_a^b-\int_a^b v\,du,
\qquad
\int_a^b f(\varphi(x))\varphi'(x)\,dx=\int_{\varphi(a)}^{\varphi(b)}f(t)\,dt.
$$

$$
\int_1^\infty\frac{dx}{x^p}<\infty\iff p>1,
\qquad
\int_0^1\frac{dx}{x^p}<\infty\iff p<1.
$$

Area $A=\int(f-g)\,dx$, length $L=\int\sqrt{1+(y')^2}\,dx$, volume of revolution $V=\pi\int f^2\,dx$.

## Function and power series — [Chapters 10–12](10-function-sequences-series.md)

Uniform convergence means $\sup_E|f_n-f|\to0$. Weierstrass: $|f_n|\le M_n$ and $\sum M_n<\infty$ imply uniform absolute convergence.

$$
\frac1R=\limsup\sqrt[n]{|c_n|},\qquad
\frac{d}{dx}\sum c_n(x-a)^n=\sum nc_n(x-a)^{n-1}\quad(|x-a|<R).
$$

Fourier coefficients on $(-\pi,\pi)$:

$$
a_n=\frac1\pi\int_{-\pi}^{\pi}f\cos(nx)\,dx,
\qquad
b_n=\frac1\pi\int_{-\pi}^{\pi}f\sin(nx)\,dx.
$$

$$
\frac1\pi\int_{-\pi}^{\pi}|f|^2\,dx
=\frac{a_0^2}{2}+\sum_{n=1}^{\infty}(a_n^2+b_n^2).
$$

## Several variables — [Chapters 14–18](14-several-variables.md)

$$
F(a+h)=F(a)+DF(a)h+o(\|h\|),
\qquad
D(G\circ F)=DG(F(a))DF(a).
$$

$$
f(a+h)=f(a)+\nabla f(a)\cdot h+\frac12h^THf(a)h+o(\|h\|^2).
$$

Implicit differentiation: $F(x,y)=0\implies y'=-F_x/F_y$ when $F_y\ne0$. Lagrange: $\nabla f=\lambda\nabla g$ on $g=c$.

$$
dA=r\,dr\,d\theta,\qquad
dV=r\,dr\,d\theta\,dz,\qquad
dV=\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta.
$$

General change of variables: $dv=|\det DT|\,du$.

$$
\oint_{\partial D}P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dA,
$$
$$
\oint_{\partial\Sigma}F\cdot dr=\iint_\Sigma(\nabla\times F)\cdot n\,dS,
\qquad
\iint_{\partial\Omega}F\cdot n\,dS=\iiint_\Omega\nabla\cdot F\,dV.
$$

## Measure, Lebesgue, and Lp — [Chapters 19–21](19-measure-theory.md)

- Monotone convergence: $0\le f_n\uparrow f\implies\int f_n\uparrow\int f$.
- Fatou: $\int\liminf f_n\le\liminf\int f_n$ for $f_n\ge0$.
- Dominated convergence: $f_n\to f$ a.e. and $|f_n|\le g\in L^1$ imply $\int f_n\to\int f$.

$$
\|f\|_p=\left(\int|f|^p\,d\mu\right)^{1/p},
\qquad
\int|fg|\,d\mu\le\|f\|_p\|g\|_q\quad(1/p+1/q=1),
$$
$$
\|f+g\|_p\le\|f\|_p+\|g\|_p,
\qquad
\langle f,g\rangle_{L^2}=\int f\overline g\,d\mu.
$$

On finite measure spaces, $r<p\implies L^p\subseteq L^r$. Every $L^p$ is complete; $L^2$ is a Hilbert space.

---
title: "Hoja de fórmulas de análisis matemático"
lang: es
---
# Hoja de fórmulas de análisis matemático

[Índice](index.md) · [Notación](00-notation.md) · [Glosario](glossary.md)

> **Atención.** Esta hoja recuerda fórmulas, no las hipótesis. Consulta los capítulos antes de aplicar un teorema.

## Sucesiones y series — [capítulos 3–4](03-sequences.md)

```math
a_n\to a,\ b_n\to b\implies a_nb_n\to ab,\quad a_n+b_n\to a+b.
```

Monótona + acotada $`\implies`$ convergente. En $`\mathbb R`$, convergente $`\iff`$ de Cauchy.

```math
\sum_{n=0}^{\infty}q^n=\frac1{1-q}\quad(|q|<1),
\qquad
\sum_{n=1}^{\infty}\frac1{n^p}<\infty\iff p>1.
```

Si $`b_n\downarrow0`$, entonces $`\sum(-1)^{n-1}b_n`$ converge y $`|R_N|\le b_{N+1}`$.

## Derivadas y Taylor — [capítulos 6–7](06-derivatives.md)

```math
(fg)'=f'g+fg',\qquad
(g\circ f)'(a)=g'(f(a))f'(a),\qquad
(f^{-1})'(f(a))=\frac1{f'(a)}.
```

```math
f(b)-f(a)=f'(c)(b-a),\qquad
f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n(x).
```

```math
e^x=\sum_{n=0}^{\infty}\frac{x^n}{n!},\qquad
\sin x=\sum_{n=0}^{\infty}\frac{(-1)^nx^{2n+1}}{(2n+1)!},
```
```math
\cos x=\sum_{n=0}^{\infty}\frac{(-1)^nx^{2n}}{(2n)!},\qquad
\log(1+x)=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}x^n}{n}\quad(-1<x\le1).
```

Una $`f`$ convexa [derivable](06-derivatives.md#sec-6-1) cumple $`f(y)\ge f(x)+f'(x)(y-x)`$ y la [desigualdad de Jensen](07-taylor-convexity.md#jensen-inequality).

## Integral de una variable — [capítulos 8–9](08-riemann-integration.md)

```math
\frac{d}{dx}\int_a^x f(t)\,dt=f(x),
\qquad
\int_a^b f(x)\,dx=F(b)-F(a)\quad(F'=f).
```

```math
\int_a^b u\,dv=[uv]_a^b-\int_a^b v\,du,
\qquad
\int_a^b f(\varphi(x))\varphi'(x)\,dx=\int_{\varphi(a)}^{\varphi(b)}f(t)\,dt.
```

```math
\int_1^\infty\frac{dx}{x^p}<\infty\iff p>1,
\qquad
\int_0^1\frac{dx}{x^p}<\infty\iff p<1.
```

Área $`A=\int(f-g)\,dx`$, longitud $`L=\int\sqrt{1+(y')^2}\,dx`$, volumen de revolución $`V=\pi\int f^2\,dx`$.

## Series funcionales y de potencias — [capítulos 10–12](10-function-sequences-series.md)

[Convergencia uniforme](10-function-sequences-series.md#sec-10-1): $`\sup_E|f_n-f|\to0`$. Weierstrass: $`|f_n|\le M_n`$ y $`\sum M_n<\infty`$ implican [convergencia absoluta](04-numeric-series.md#sec-4-3) uniforme.

```math
\frac1R=\limsup\sqrt[n]{|c_n|},\qquad
\frac{d}{dx}\sum c_n(x-a)^n=\sum nc_n(x-a)^{n-1}\quad(|x-a|<R).
```

[Coeficientes de Fourier](12-fourier-series.md#sec-12-1) en $`(-\pi,\pi)`$:

```math
a_n=\frac1\pi\int_{-\pi}^{\pi}f\cos(nx)\,dx,
\qquad
b_n=\frac1\pi\int_{-\pi}^{\pi}f\sin(nx)\,dx.
```

```math
\frac1\pi\int_{-\pi}^{\pi}|f|^2\,dx
=\frac{a_0^2}{2}+\sum_{n=1}^{\infty}(a_n^2+b_n^2).
```

## Varias variables — [capítulos 14–18](14-several-variables.md)

```math
F(a+h)=F(a)+DF(a)h+o(\|h\|),
\qquad
D(G\circ F)=DG(F(a))DF(a).
```

```math
f(a+h)=f(a)+\nabla f(a)\cdot h+\frac12h^THf(a)h+o(\|h\|^2).
```

Derivación implícita: $`F(x,y)=0\implies y'=-F_x/F_y`$ si $`F_y\ne0`$. Lagrange: $`\nabla f=\lambda\nabla g`$ en $`g=c`$.

```math
dA=r\,dr\,d\theta,\qquad
dV=r\,dr\,d\theta\,dz,\qquad
dV=\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta.
```

Cambio general: $`dv=|\det DT|\,du`$.

```math
\oint_{\partial D}P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dA,
```
```math
\oint_{\partial\Sigma}F\cdot dr=\iint_\Sigma(\nabla\times F)\cdot n\,dS,
\qquad
\iint_{\partial\Omega}F\cdot n\,dS=\iiint_\Omega\nabla\cdot F\,dV.
```

## Medida, Lebesgue y Lp — [capítulos 19–21](19-measure-theory.md)

- Convergencia monótona: $`0\le f_n\uparrow f\implies\int f_n\uparrow\int f`$.
- Fatou: $`\int\liminf f_n\le\liminf\int f_n`$ para $`f_n\ge0`$.
- [Convergencia dominada](20-lebesgue-integration.md#dominated-convergence-theorem): $`f_n\to f`$ [c.t.p.](19-measure-theory.md#sec-19-4) y $`|f_n|\le g\in L^1`$ implican $`\int f_n\to\int f`$.

```math
\|f\|_p=\left(\int|f|^p\,d\mu\right)^{1/p},
\qquad
\int|fg|\,d\mu\le\|f\|_p\|g\|_q\quad(1/p+1/q=1),
```
```math
\|f+g\|_p\le\|f\|_p+\|g\|_p,
\qquad
\langle f,g\rangle_{L^2}=\int f\overline g\,d\mu.
```

En [espacios de medida](19-measure-theory.md#sec-19-2) finita, $`r<p\implies L^p\subseteq L^r`$. Todo $`L^p`$ es completo; $`L^2`$ es un [espacio de Hilbert](21-lp-spaces.md#sec-21-4).

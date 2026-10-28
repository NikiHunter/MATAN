---
title: "Hoja de fórmulas de análisis matemático"
lang: es
tags: [mathinmind/es, mathinmind/support]
---
# Hoja de fórmulas de análisis matemático

[[es/index|Índice]] · [[es/00-notation|Notación]] · [[es/glossary|Glosario]]

> [!note] Atención
> Esta hoja recuerda fórmulas, no las hipótesis. Consulta los capítulos antes de aplicar un teorema.

## Sucesiones y series — [[es/03-sequences|capítulos 3–4]]

$$
a_n\to a,\ b_n\to b\implies a_nb_n\to ab,\quad a_n+b_n\to a+b.
$$

Monótona + acotada $\implies$ convergente. En $\mathbb R$, convergente $\iff$ de Cauchy.

$$
\sum_{n=0}^{\infty}q^n=\frac1{1-q}\quad(|q|<1),
\qquad
\sum_{n=1}^{\infty}\frac1{n^p}<\infty\iff p>1.
$$

Si $b_n\downarrow0$, entonces $\sum(-1)^{n-1}b_n$ converge y $|R_N|\le b_{N+1}$.

## Derivadas y Taylor — [[es/06-derivatives|capítulos 6–7]]

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

Una $f$ convexa [[es/06-derivatives#6.1 Definición y aproximación lineal|derivable]] cumple $f(y)\ge f(x)+f'(x)(y-x)$ y la [[es/07-taylor-convexity#^jensen-inequality|desigualdad de Jensen]].

## Integral de una variable — [[es/08-riemann-integration|capítulos 8–9]]

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

Área $A=\int(f-g)\,dx$, longitud $L=\int\sqrt{1+(y')^2}\,dx$, volumen de revolución $V=\pi\int f^2\,dx$.

## Series funcionales y de potencias — [[es/10-function-sequences-series|capítulos 10–12]]

[[es/10-function-sequences-series#10.1 Dos modos de convergencia|Convergencia uniforme]]: $\sup_E|f_n-f|\to0$. Weierstrass: $|f_n|\le M_n$ y $\sum M_n<\infty$ implican [[es/04-numeric-series#4.3 Convergencia absoluta y condicional|convergencia absoluta]] uniforme.

$$
\frac1R=\limsup\sqrt[n]{|c_n|},\qquad
\frac{d}{dx}\sum c_n(x-a)^n=\sum nc_n(x-a)^{n-1}\quad(|x-a|<R).
$$

[[es/12-fourier-series#12.1 Sistema trigonométrico y coeficientes|Coeficientes de Fourier]] en $(-\pi,\pi)$:

$$
a_n=\frac1\pi\int_{-\pi}^{\pi}f\cos(nx)\,dx,
\qquad
b_n=\frac1\pi\int_{-\pi}^{\pi}f\sin(nx)\,dx.
$$

$$
\frac1\pi\int_{-\pi}^{\pi}|f|^2\,dx
=\frac{a_0^2}{2}+\sum_{n=1}^{\infty}(a_n^2+b_n^2).
$$

## Varias variables — [[es/14-several-variables|capítulos 14–18]]

$$
F(a+h)=F(a)+DF(a)h+o(\|h\|),
\qquad
D(G\circ F)=DG(F(a))DF(a).
$$

$$
f(a+h)=f(a)+\nabla f(a)\cdot h+\frac12h^THf(a)h+o(\|h\|^2).
$$

Derivación implícita: $F(x,y)=0\implies y'=-F_x/F_y$ si $F_y\ne0$. Lagrange: $\nabla f=\lambda\nabla g$ en $g=c$.

$$
dA=r\,dr\,d\theta,\qquad
dV=r\,dr\,d\theta\,dz,\qquad
dV=\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta.
$$

Cambio general: $dv=|\det DT|\,du$.

$$
\oint_{\partial D}P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dA,
$$
$$
\oint_{\partial\Sigma}F\cdot dr=\iint_\Sigma(\nabla\times F)\cdot n\,dS,
\qquad
\iint_{\partial\Omega}F\cdot n\,dS=\iiint_\Omega\nabla\cdot F\,dV.
$$

## Medida, Lebesgue y Lp — [[es/19-measure-theory|capítulos 19–21]]

- Convergencia monótona: $0\le f_n\uparrow f\implies\int f_n\uparrow\int f$.
- Fatou: $\int\liminf f_n\le\liminf\int f_n$ para $f_n\ge0$.
- [[es/20-lebesgue-integration#^dominated-convergence-theorem|Convergencia dominada]]: $f_n\to f$ [[es/19-measure-theory#19.4 Funciones medibles|c.t.p.]] y $|f_n|\le g\in L^1$ implican $\int f_n\to\int f$.

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

En [[es/19-measure-theory#19.2 Medidas|espacios de medida]] finita, $r<p\implies L^p\subseteq L^r$. Todo $L^p$ es completo; $L^2$ es un [[es/21-lp-spaces#21.4 El espacio de Hilbert L2|espacio de Hilbert]].

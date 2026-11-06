---
title: "Integrales dependientes de un parámetro"
lang: es
chapter: 25
part: "Semestre 3: capítulos del profesor"
numbering: lecture
lecturer_chapter: 9
aliases: ["Integrales dependientes de un parámetro (es)"]
tags: [mathinmind/es, mathinmind/chapter]
---
# 25. Integrales dependientes de un parámetro

[[es/24-functional-power-series|← 24. Series funcionales y de potencias]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/26-multiple-riemann-integral|26. La integral múltiple de Riemann →]]

> [!abstract] Objetivo
> Exponer el capítulo 9 del profesor (§9.1–§9.3, [[es/lectures-2025-26/lecture-75-76|clases 75–76]], [[es/lectures-2025-26/lecture-77-78|77–78]] y [[es/lectures-2025-26/lecture-79-80|79–80]]) conservando la numeración del profesor: continuidad, derivación e integración respecto de un parámetro de integrales propias e impropias, [[#^def-9-2-1|convergencia uniforme de una integral impropia]] y sus criterios, las [[#^def-9-3-1|funciones gamma]] y beta. Temas relacionados del curso: [[es/09-improper-integrals-applications#9.1 Definiciones|integrales impropias]] en el [[es/09-improper-integrals-applications|capítulo 9]], [[es/10-function-sequences-series#10.1 Dos modos de convergencia|convergencia uniforme]] de series en el [[es/10-function-sequences-series|capítulo 10]], cambio del orden de integración en el [[es/17-multiple-integrals|capítulo 17]].

## §9.1. Integrales propias dependientes de un parámetro

> [!definition] Definición 9.1.1
> Una integral dependiente de un parámetro es una función de la forma
> $$
> I(y)=\int_{E_y}f(x,y)\,dx ,
> $$
> donde $y$ desempeña el papel de un parámetro que recorre un conjunto $Y$.

^def-9-1-1

Las preguntas principales son si $I$ es continua y si se puede derivar e integrar respecto de $y$ bajo el signo integral. Ejemplo del profesor: para $I(y)=\int_0^{+\infty}e^{-xy}\frac{\sin x}{x}\,dx$ la derivación formal da $I'(y)=-\int_0^{+\infty}e^{-xy}\sin x\,dx=-\frac{1}{1+y^2}$, de donde $I(0)=\int_0^{+\infty}\frac{\sin x}{x}\,dx=\frac\pi2$; justificar estos pasos es el objetivo de §9.2 (véase el ejemplo resuelto más abajo). En todo §9.1
$$
P=\{(x,y)\in\mathbb R^2:\ a\le x\le b,\ c\le y\le d\},\qquad I(y)=\int_a^bf(x,y)\,dx .
$$

> [!theorem] Teorema 9.1.1
> Sea $f\in C(P)$. Entonces la función $I(y)=\int_a^bf(x,y)\,dx$ es continua en cada punto $y\in[c,d]$, es decir, $I\in C([c,d])$.

^thm-9-1-1

La demostración es la [[es/05-limits-continuity#5.4 Continuidad uniforme|continuidad uniforme]] de $f$ en el [[es/13-metric-spaces#13.4 Compacidad|compacto]] $P$ (teorema de Cantor): $|I(y)-I(y_0)|\le\int_a^b|f(x,y)-f(x,y_0)|\,dx<\varepsilon(b-a)$ para $|y-y_0|<\delta$.

> [!theorem] Teorema 9.1.2
> Sean $f\in C(P)$ y $\frac{\partial f}{\partial y}\in C(P)$. Entonces $I\in C^1([c,d])$ y
> $$
> I'(y)=\int_a^b\frac{\partial f}{\partial y}(x,y)\,dx .
> $$

^thm-9-1-2

Es la fórmula (regla) de Leibniz. Por el [[es/07-taylor-convexity#^lagrange-mean-value-theorem|teorema de Lagrange]] el cociente incremental $\frac{f(x,y+h)-f(x,y)}{h}=f'_y(x,y+\theta h)$ converge a $f'_y(x,y)$ uniformemente en $x$ (de nuevo la continuidad uniforme), y basta pasar al límite bajo el signo integral.

> [!theorem] Teorema 9.1.3
> Sea $f\in C(P)$. Entonces $I$ es integrable en $[c,d]$ y
> $$
> \int_c^d\left(\int_a^bf(x,y)\,dx\right)dy=\int_a^b\left(\int_c^df(x,y)\,dy\right)dx .
> $$

^thm-9-1-3

*Idea de la demostración.* Ambos miembros, vistos como funciones del [[es/03-sequences#3.5 Límite superior e inferior|límite superior]] $t\in[c,d]$ en lugar de $d$, se anulan en $t=c$ y tienen la misma [[es/06-derivatives#6.1 Definición y aproximación lineal|derivada]] $\int_a^bf(x,t)\,dx$ (para el miembro derecho, por el [[#^thm-9-1-2|teorema 9.1.2]]).

## §9.2. Integrales impropias dependientes de un parámetro

Sean $-\infty<a<b\le+\infty$, la función $f$ definida en $[a,b)\times Y$, integrable para cada $y\in Y$ en cada segmento $[a,b']\subset[a,b)$, y la integral impropia $I(y)=\int_a^bf(x,y)\,dx$ convergente para cada $y\in Y$. Pongamos $I_{b'}(y)=\int_a^{b'}f(x,y)\,dx$.

> [!definition] Definición 9.2.1
> Diremos que $I(y)$ converge uniformemente respecto de $y\in Y$ (uniformemente en $Y$) si
> $$
> \forall\varepsilon>0\ \ \exists b_0\in[a,b)\ \ \forall b'\in(b_0,b)\ \ \forall y\in Y:\quad |I_{b'}(y)-I(y)|=\left|\int_{b'}^{b}f(x,y)\,dx\right|<\varepsilon .
> $$
> En otras palabras, $I_{b'}(y)\rightrightarrows I(y)$ en $Y$ cuando $b'\to b$.

^def-9-2-1

> [!theorem] Criterio de Bolzano–Cauchy
> La integral $I(y)$ converge uniformemente en $Y$ si y solo si para todo $\varepsilon>0$ existe $b_0\in[a,b)$ tal que $\bigl|\int_{t_1}^{t_2}f(x,y)\,dx\bigr|<\varepsilon$ para todo $t_1,t_2\in(b_0,b)$ y todo $y\in Y$.

> [!theorem] Criterio de Weierstrass
> Supongamos que existe una función $\varphi:[a,b)\to[0,+\infty)$, integrable en cada segmento $[a,t]\subset[a,b)$, tal que $|f(x,y)|\le\varphi(x)$ para todo $x\in[a,b)$, $y\in Y$, y la integral $\int_a^b\varphi(x)\,dx$ converge. Entonces $I(y)$ converge uniformemente en $Y$.

> [!theorem] Criterio de Dirichlet
> Sean las funciones $f$ y $g$ definidas en $[a,b)\times Y$ y continuas en $x$ para cada $y$; para cada $y$ la función $f(\cdot,y)$ es monótona, y $\sup_{y\in Y}|f(x,y)|\to0$ cuando $x\to b$; las [[es/08-riemann-integration#8.3 Teorema fundamental del cálculo|primitivas]] $\int_a^tg(x,y)\,dx$ están uniformemente acotadas para $t\in[a,b)$, $y\in Y$. Entonces la integral $\int_a^bf(x,y)g(x,y)\,dx$ converge uniformemente en $Y$.

> [!theorem] Criterio de Abel
> Sean las funciones $f$ y $g$ definidas en $[a,b)\times Y$ y continuas en $x$ para cada $y$; para cada $y$ la función $f(\cdot,y)$ es monótona, y $|f(x,y)|\le M$ en todas partes; la integral $\int_a^bg(x,y)\,dx$ converge uniformemente en $Y$. Entonces la integral $\int_a^bf(x,y)g(x,y)\,dx$ converge uniformemente en $Y$.

Los criterios de Dirichlet y de Abel se demuestran con el [[es/08-riemann-integration#^mean-value-theorem-for-integrals|segundo teorema del valor medio]] (de Bonnet), igual que los criterios homónimos para series se demuestran con la [[es/23-numerical-series#§7.4. Series de términos de signo arbitrario|transformación de Abel]]. Ejemplo: $\int_0^{\infty}\frac{\cos(\alpha x)}{1+x^2}\,dx$ converge uniformemente en $\alpha\in\mathbb R$ por el [[es/10-function-sequences-series#^weierstrass-m-test|criterio de Weierstrass]] con $\varphi(x)=\frac1{1+x^2}$.

> [!theorem] Teorema 9.2.1
> Sean la función $f$ continua en $[a,b)\times[c,d]$, $y_0\in[c,d]$, y la integral impropia $I(y)=\int_a^bf(x,y)\,dx$ uniformemente convergente en $[c,d]\cap(y_0-\delta_0,y_0+\delta_0)$ para algún $\delta_0>0$. Entonces la función $I$ es [[es/05-limits-continuity#5.3 Continuidad|continua en el punto]] $y_0$. En particular, si $I(y)$ converge uniformemente en $[c,d]$, entonces $I\in C([c,d])$.

^thm-9-2-1

> [!theorem] Teorema 9.2.2
> Sean las funciones $f(x,y)$ y $f'_y(x,y)$ continuas en $[a,b)\times[c,d]$, la integral $\int_a^bf'_y(x,y)\,dx$ uniformemente convergente en $[c,d]$, y la integral $I(y)=\int_a^bf(x,y)\,dx$ convergente para al menos un valor $y_0\in[c,d]$. Entonces $I(y)$ converge uniformemente en todo el segmento $[c,d]$, la función $I$ es diferenciable en $[c,d]$, y
> $$
> I'(y)=\int_a^bf'_y(x,y)\,dx .
> $$

^thm-9-2-2

> [!theorem] Teorema 9.2.3
> Sean la función $f(x,y)$ continua en $[a,b)\times[c,d]$, y la integral $I(y)=\int_a^bf(x,y)\,dx$ uniformemente convergente en $[c,d]$. Entonces $I$ es integrable en $[c,d]$, la integral impropia del miembro derecho converge, y
> $$
> \int_c^dI(y)\,dy=\int_a^b\left(\int_c^df(x,y)\,dy\right)dx .
> $$

^thm-9-2-3

Los tres teoremas se reducen a los [[es/24-functional-power-series#^thm-8-2-1|teoremas 8.2.1]]–[[es/24-functional-power-series#^thm-8-2-3|8.2.3]] sobre sucesiones de funciones: $I_{b_n}\rightrightarrows I$ para toda sucesión $b_n\to b$, y a las integrales propias $I_{b_n}$ se les aplican los teoremas de §9.1.

**El método de Feynman** consiste en incluir una integral en una familia y derivar respecto del parámetro. Para $I(\alpha)=\int_0^\infty\frac{e^{-x}-e^{-\alpha x}}{x}\,dx$, $\alpha\in[1,2]$, tenemos $I(1)=0$, y la integral $\int_0^\infty e^{-\alpha x}\,dx=\frac1\alpha$ de la derivada respecto de $\alpha$ converge uniformemente (mayorante $e^{-x}$). Por el [[#^thm-9-2-2|teorema 9.2.2]] $I'(\alpha)=\frac1\alpha$, por lo que
$$
\int_0^\infty\frac{e^{-x}-e^{-2x}}{x}\,dx=I(2)=\ln2 .
$$

## §9.3. La función gamma

> [!definition] Definición 9.3.1
> La función gamma (en el punto $y$) es la función dada por la fórmula
> $$
> \Gamma(y)=\int_0^{\infty}x^{y-1}e^{-x}\,dx\qquad(y>0).
> $$

^def-9-3-1

La integral converge para $y>0$: cerca de cero $x^{y-1}e^{-x}\sim\frac{1}{x^{1-y}}$, y en el infinito $x^{y-1}e^{-x}=o\bigl(\frac1{x^2}\bigr)$. Propiedades de la función gamma:

1. $\Gamma(1)=1$, $\Gamma\bigl(\tfrac12\bigr)=\sqrt\pi$ (el cambio $x=t^2$ y la integral de Euler–Poisson $\int_0^\infty e^{-t^2}\,dt=\frac{\sqrt\pi}2$).
2. $\Gamma(y+1)=y\,\Gamma(y)$ para $y>0$ ([[es/08-riemann-integration#8.4 Técnicas de cálculo|integración por partes]]); por tanto $\Gamma(n+1)=n!$ y $\Gamma\bigl(n+\tfrac12\bigr)=\frac{(2n-1)!!}{2^n}\sqrt\pi$ para $n\in\mathbb N$.
3. $\Gamma\in C^\infty(0,+\infty)$, y las derivadas se calculan bajo el signo integral: $\Gamma''(y)=\int_0^{\infty}x^{y-1}e^{-x}\ln^2x\,dx>0$, es decir, $\Gamma$ es convexa; $\Gamma(y)\to+\infty$ cuando $y\to0+$ y cuando $y\to+\infty$.
4. La fórmula de Stirling: $\Gamma(y+1)\sim\sqrt{2\pi y}\,\frac{y^y}{e^y}$ cuando $y\to+\infty$; en particular, $n!\sim\sqrt{2\pi n}\,\frac{n^n}{e^n}$.
5. La fórmula de reflexión: $\Gamma(y)\,\Gamma(1-y)=\frac{\pi}{\sin(\pi y)}$ para $0<y<1$.
6. La fórmula de Euler: $\frac{\Gamma(y)}{b^y}=\int_0^{\infty}u^{y-1}e^{-ub}\,du$ para $y>0$, $b>0$ (el cambio $x=bu$).

**La función beta** $B(y,z)=\int_0^1x^{y-1}(1-x)^{z-1}\,dx$ ($y,z>0$) se expresa mediante la función gamma:
$$
B(y,z)=\frac{\Gamma(y)\,\Gamma(z)}{\Gamma(y+z)} .
$$
La deducción usa la fórmula de Euler para $\Gamma(y+z)$, un cambio del orden de integración y el cambio $b=\frac{x}{1-x}$.

## Ejemplo resuelto

**La integral de Dirichlet.** Sea $I(y)=\int_0^{+\infty}e^{-xy}\frac{\sin x}{x}\,dx$, $y\ge0$ (el integrando se extiende por uno en $x=0$ y es continuo).

1. *Convergencia uniforme en $[0,+\infty)$.* Por el [[es/09-improper-integrals-applications#^dirichlet-test-for-integrals|criterio de Abel]]: $\int_0^\infty\frac{\sin x}{x}\,dx$ converge (uniformemente, pues no depende de $y$), y $e^{-xy}$ es monótona en $x$ y no supera $1$. Por el [[#^thm-9-2-1|teorema 9.2.1]], $I$ es continua en $[0,+\infty)$.
2. *La derivada para $y>0$.* Para $y\ge y_0>0$ tenemos $|f'_y|=|e^{-xy}\sin x|\le e^{-xy_0}$, y por el criterio de Weierstrass y el [[#^thm-9-2-2|teorema 9.2.2]]
$$
I'(y)=-\int_0^{\infty}e^{-xy}\sin x\,dx=-\frac{1}{1+y^2},\qquad I(y)=C-\operatorname{arctg}y .
$$
3. *La constante.* $|I(y)|\le\int_0^\infty e^{-xy}\,dx=\frac1y\to0$ cuando $y\to+\infty$, luego $C=\frac\pi2$.
4. *Respuesta.* Por continuidad en cero, $\int_0^{+\infty}\frac{\sin x}{x}\,dx=I(0)=\frac\pi2$.

**La función gamma en los cálculos.** Con el cambio $t=x^2$:
$$
\int_0^\infty x^4e^{-x^2}\,dx=\frac12\int_0^\infty t^{3/2}e^{-t}\,dt=\frac12\,\Gamma\Bigl(\frac52\Bigr)=\frac12\cdot\frac34\sqrt\pi=\frac{3\sqrt\pi}{8}.
$$

## Errores frecuentes

1. Derivar una integral impropia bajo el signo integral sin comprobar la convergencia uniforme de la integral de $f'_y$.
2. Confundir la convergencia para cada $y$ con la uniforme: $\int_0^\infty ye^{-xy}\,dx=1$ para todo $y>0$, pero $\int_{b'}^\infty ye^{-xy}\,dx=e^{-b'y}$, y $\sup_{y\in(0,1]}e^{-b'y}=1$, así que la convergencia en $(0,1]$ no es uniforme (y la función límite es discontinua en cero en $[0,1]$).
3. Escribir $\Gamma(n)=n!$ en lugar de $\Gamma(n)=(n-1)!$.
4. Aplicar los teoremas de §9.1 cuando $f$ es continua solo en $x$ para cada $y$: hace falta la continuidad en todo el rectángulo $P$.
5. Olvidar que la integral que define $\Gamma(y)$ converge solo para $y>0$.

## Ejercicios

1. Halle $\lim_{y\to0}\int_0^1\sqrt{x^2+y^2}\,dx$.
2. Calcule $\int_0^1\frac{x^b-x^a}{\ln x}\,dx$ para $0<a<b$.
3. Calcule $\int_0^1x^2(1-x)^3\,dx$ mediante la función beta.
4. Demuestre que $\int_0^\infty e^{-x^2}\cos(xy)\,dx$ converge uniformemente en $\mathbb R$.

> [!answer]- Respuestas breves
> 1. $\frac12$: por el [[#^thm-9-1-1|teorema 9.1.1]] el límite es $\int_0^1x\,dx$.
> 2. $\ln\frac{b+1}{a+1}$: el integrando es igual a $\int_a^bx^y\,dy$, y por el [[#^thm-9-1-3|teorema 9.1.3]] se puede cambiar el orden de integración: $\int_a^b\frac{dy}{y+1}$.
> 3. $B(3,4)=\frac{\Gamma(3)\Gamma(4)}{\Gamma(7)}=\frac{2\cdot6}{720}=\frac1{60}$.
> 4. El criterio de Weierstrass con $\varphi(x)=e^{-x^2}$.

---

[[es/24-functional-power-series|← 24. Series funcionales y de potencias]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/26-multiple-riemann-integral|26. La integral múltiple de Riemann →]]

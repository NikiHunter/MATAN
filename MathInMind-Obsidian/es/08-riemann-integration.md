---
title: "La integral de Riemann"
lang: es
chapter: 8
part: "Cálculo de una variable"
aliases: ["La integral de Riemann (es)"]
tags: [mathinmind/es, mathinmind/chapter]
---
# 8. La integral de Riemann

[[es/07-taylor-convexity|← 7. Teoremas del valor medio, Taylor y convexidad]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/09-improper-integrals-applications|9. Integrales impropias y aplicaciones →]]

> [!abstract] Objetivo
> Definir la integral mediante [[#8.1 Particiones y sumas de Darboux|particiones]], relacionarla con la derivación y calcular [[#8.2 Sumas de Riemann y propiedades|integrales definidas]] con rigor.

## 8.1 Particiones y sumas de Darboux

Sea $f:[a,b]\to\mathbb R$ acotada. Para una partición

$$
P:a=x_0<x_1<\cdots<x_n=b,
$$

escribimos $\Delta x_i=x_i-x_{i-1}$, $m_i=\inf_{[x_{i-1},x_i]}f$ y $M_i=\sup_{[x_{i-1},x_i]}f$. Las sumas inferior y superior de Darboux son

$$
L(f,P)=\sum_{i=1}^{n}m_i\Delta x_i,
\qquad
U(f,P)=\sum_{i=1}^{n}M_i\Delta x_i.
$$

Al refinar una partición, las sumas inferiores crecen y las superiores decrecen. Definimos

$$
\underline{\int_a^b}f=\sup_P L(f,P),
\qquad
\overline{\int_a^b}f=\inf_P U(f,P).
$$

La función es **integrable Riemann** cuando ambas cantidades coinciden; su valor común es $\int_a^b f(x)\,dx$.

> [!theorem] Criterio de integrabilidad
> Una $f$ acotada es integrable exactamente cuando para todo $\varepsilon>0$ hay una partición $P$ con $U(f,P)-L(f,P)<\varepsilon$.

^integrability-criterion

Las funciones continuas y monótonas en $[a,b]$ son integrables. Según el criterio de Lebesgue, una función acotada es integrable Riemann exactamente cuando su conjunto de discontinuidades tiene [[es/19-measure-theory#19.3 Medida de Lebesgue|medida de Lebesgue]] cero.

## 8.2 Sumas de Riemann y propiedades

Una suma de Riemann usa puntos $\xi_i\in[x_{i-1},x_i]$:

$$
S(f,P,\xi)=\sum_{i=1}^{n}f(\xi_i)\Delta x_i.
$$

Para $f$ integrable, estas sumas se aproximan a la integral cuando la norma $\max_i\Delta x_i$ tiende a cero. En particular, para $f$ continua,

$$
\int_a^b f(x)\,dx
=\lim_{n\to\infty}\frac{b-a}{n}\sum_{k=1}^{n}f\left(a+k\frac{b-a}{n}\right).
$$

Para $f,g$ integrables,

$$
\int_a^b(\alpha f+\beta g)=\alpha\int_a^b f+\beta\int_a^b g,
$$
$$
\int_a^b f=\int_a^c f+\int_c^b f,
$$

y $f\le g$ implica $\int f\le\int g$. Además,

$$
\left|\int_a^b f(x)\,dx\right|\le\int_a^b|f(x)|\,dx.
$$

Por convenio, $\int_b^a f=-\int_a^b f$ y $\int_a^a f=0$.

> [!theorem] Teorema del valor medio integral
> Si $f$ es continua en $[a,b]$, existe $c\in[a,b]$ con
> $$
> f(c)=\frac1{b-a}\int_a^b f(x)\,dx.
> $$

^mean-value-theorem-for-integrals

## 8.3 Teorema fundamental del cálculo

> [!theorem] Primera parte
> Si $f$ es continua en $[a,b]$ y $F(x)=\int_a^x f(t)\,dt$, entonces $F$ es [[es/06-derivatives#6.1 Definición y aproximación lineal|derivable]] y $F'(x)=f(x)$.

^ftc-first-part

La prueba utiliza

$$
\frac{F(x+h)-F(x)}h=\frac1h\int_x^{x+h}f(t)\,dt\to f(x).
$$

> [!theorem] Segunda parte (Newton–Leibniz)
> Si $F'=f$ y $f$ es integrable, entonces
> $$
> \int_a^b f(x)\,dx=F(b)-F(a).
> $$

^newton-leibniz-formula

En consecuencia, la [[#8.4 Técnicas de cálculo|integración por partes]] y la sustitución dan

$$
\int_a^b u\,dv=[uv]_a^b-\int_a^b v\,du,
$$
$$
\int_a^b f(\varphi(x))\varphi'(x)\,dx
=\int_{\varphi(a)}^{\varphi(b)}f(t)\,dt
$$

bajo las hipótesis habituales de derivabilidad continua.

## 8.4 Técnicas de cálculo

La integración indefinida busca una [[#8.3 Teorema fundamental del cálculo|primitiva]]: $\int f(x)\,dx=F(x)+C$. Los métodos útiles incluyen simplificación algebraica, sustitución, partes, fracciones simples y sustituciones trigonométricas. A veces una integral definida se calcula por simetría sin una primitiva elemental.

Por ejemplo,

$$
\int_{-a}^{a}f(x)\,dx=2\int_0^a f(x)\,dx
$$

para $f$ par, mientras que la integral es cero para $f$ impar.

## Ejemplo resuelto

Calculamos $\int_0^1 x^2\,dx$ con particiones iguales:

$$
\frac1n\sum_{k=1}^{n}\left(\frac{k}{n}\right)^2
=\frac{n(n+1)(2n+1)}{6n^3}\to\frac13.
$$

La integral vale $1/3$. [[#^newton-leibniz-formula|Newton–Leibniz]] lo confirma mediante $F(x)=x^3/3$.

## Errores frecuentes

1. Una fórmula de primitiva no justifica por sí sola atravesar una discontinuidad.
2. Invertir los límites cambia el signo.
3. La constante $C$ pertenece a la integral indefinida, no a la definida.

## Ejercicios

1. Calcula $\int_0^\pi x\sin x\,dx$ por partes.
2. Expresa $\lim_{n\to\infty}\frac1n\sum_{k=1}^n\frac1{1+k/n}$ como integral y calcúlalo.
3. Prueba que si $f\ge0$ es continua y $\int_a^b f=0$, entonces $f\equiv0$.

> [!answer]- Respuestas breves
> 1. El valor es $\pi$.
> 2. Es $\int_0^1(1+x)^{-1}\,dx=\log2$.
> 3. Si $f(c)>0$, la continuidad hace que $f$ sea positiva en un subintervalo y la integral sea positiva.

---

[[es/07-taylor-convexity|← 7. Teoremas del valor medio, Taylor y convexidad]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/09-improper-integrals-applications|9. Integrales impropias y aplicaciones →]]

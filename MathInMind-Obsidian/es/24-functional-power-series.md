---
title: "Series funcionales y de potencias"
lang: es
chapter: 24
part: "Semestre 3: capítulos del profesor"
numbering: lecture
lecturer_chapter: 8
aliases: ["Series funcionales y de potencias (es)"]
tags: [mathinmind/es, mathinmind/chapter]
---
# 24. Series funcionales y de potencias

[[es/23-numerical-series|← 23. Series numéricas]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/25-parameter-integrals|25. Integrales dependientes de un parámetro →]]

> [!abstract] Objetivo
> Exponer el capítulo 8 del profesor (§8.1–§8.4, [[es/lectures-2025-26/lecture-71-72|clases 71–72]], [[es/lectures-2025-26/lecture-73-74|73–74]] y [[es/lectures-2025-26/lecture-75-76|75–76]]) conservando la numeración del profesor: [[es/10-function-sequences-series#10.1 Dos modos de convergencia|convergencia puntual]] y uniforme, paso al límite de la continuidad, la integración y la derivación, series funcionales y el [[es/10-function-sequences-series#^weierstrass-m-test|criterio de Weierstrass]], [[es/11-power-series#11.1 Radio de convergencia|series de potencias]], la [[es/11-power-series#11.3 Desarrollos fundamentales|serie de Taylor]] y las [[es/11-power-series#11.4 Analítica no significa solamente suave|funciones analíticas]]. Una exposición condensada de los mismos temas está en los capítulos [[es/10-function-sequences-series|10]] y [[es/11-power-series|11]].

## §8.1. Convergencia uniforme

Sean $X$ un conjunto, $f_n,f:X\to\mathbb R$, $n\in\mathbb N$.

> [!definition] Definición 8.1.1
> Diremos que la sucesión $(f_n)$ converge en $X$ a $f$ puntualmente si para cada $x\in X$ la sucesión numérica $a_n:=f_n(x)$ converge al número $a:=f(x)$ cuando $n\to\infty$.

^def-8-1-1

> [!definition] Definición 8.1.2
> $f_n\to f$ uniformemente en el conjunto $E\subset X$ si
> $$
> \forall\varepsilon>0\ \ \exists N=N(\varepsilon)\ \ \forall x\in E\ \ \forall n>N:\quad |f_n(x)-f(x)|<\varepsilon .
> $$

^def-8-1-2

La diferencia con la convergencia puntual está en el orden de los [[es/01-logic-sets-functions#1.1 Proposiciones y cuantificadores|cuantificadores]]: en la convergencia puntual el índice $N$ puede depender de $x$; en la uniforme, un mismo índice sirve para todos los $x\in E$. Geométricamente: para $n>N$ la gráfica de $f_n$ está entera dentro del «tubo de radio $\varepsilon$» alrededor de la gráfica de $f$.

> [!definition] Definición 8.1.3
> La magnitud
> $$
> \rho(f,g)=\sup_{x\in X}|f(x)-g(x)|
> $$
> se llama desviación uniforme (de Chebyshov) de las funciones $f$ y $g$.

^def-8-1-3

> [!definition] Definición 8.1.4
> $f_n\rightrightarrows f$ si para todo $\varepsilon>0$ existe $N$ tal que $\rho(f_n,f)<\varepsilon$ para todo $n>N$.

^def-8-1-4

Así, $f_n\rightrightarrows f$ equivale a $\rho(f_n,f)\to0$. Ejemplo: $f_n(x)=x^n$ en $[0,1]$ converge puntualmente a la función igual a $0$ en $[0,1)$ y a $1$ en el punto $1$; aquí $\rho(f_n,f)=\sup_{[0,1)}x^n=1$, y la convergencia no es uniforme, mientras que en $[0,q]$ con $q<1$ tenemos $\rho(f_n,0)=q^n\to0$.

## §8.2. Convergencia uniforme y propiedades de las funciones límite

> [!theorem] Teorema 8.2.1 (continuidad de la función límite)
> Sean
> 1. $f_n\in C([a,b])$ para todo $n$;
> 2. $f_n\rightrightarrows f$ en $[a,b]$.
>
> Entonces $f\in C([a,b])$.

^thm-8-2-1

*Idea de la demostración* («$\varepsilon/3$»): $|f(x)-f(x_0)|\le|f(x)-f_n(x)|+|f_n(x)-f_n(x_0)|+|f_n(x_0)-f(x_0)|$, donde los términos extremos son pequeños uniformemente en $x$ para un $n$ grande fijo, y el del medio es pequeño por la continuidad de $f_n$. Corolario: $\lim_{x\to x_0}\lim_{n\to\infty}f_n(x)=\lim_{n\to\infty}\lim_{x\to x_0}f_n(x)$.

> [!theorem] Teorema 8.2.2 (paso al límite bajo el signo integral)
> Sean
> 1. $f_n\in C([a,b])$ para todo $n$;
> 2. $f_n\rightrightarrows f$ en $[a,b]$.
>
> Entonces
> $$
> \lim_{n\to\infty}\int_a^bf_n(x)\,dx=\int_a^b\Bigl(\lim_{n\to\infty}f_n(x)\Bigr)dx .
> $$

^thm-8-2-2

La demostración es la estimación $\bigl|\int_a^bf_n-\int_a^bf\bigr|\le(b-a)\,\rho(f_n,f)$. La convergencia puntual sola no basta: los «dientes» $f_n$, triángulos sobre $[0,\frac1n]$ de altura $n$, tienden a cero en cada punto, pero $\int_0^1f_n=\frac12$.

> [!theorem] Teorema 8.2.3 (derivación de la función límite)
> Sean
> 1. $f_n\in C^1([a,b])$ para todo $n$;
> 2. $f_n\to f$ (puntualmente en $[a,b]$) cuando $n\to\infty$;
> 3. $f\in C^1([a,b])$;
> 4. $f_n'\rightrightarrows\varphi$ en $[a,b]$.
>
> Entonces $\varphi\in C([a,b])$ y $f'=\varphi$, es decir,
> $$
> \frac{d}{dx}\Bigl(\lim_{n\to\infty}f_n(x)\Bigr)=\lim_{n\to\infty}\Bigl(\frac{d}{dx}f_n(x)\Bigr).
> $$

^thm-8-2-3

*Idea de la demostración.* Pasando al límite en la igualdad $f_n(x)=f_n(a)+\int_a^xf_n'(t)\,dt$ por el [[#^thm-8-2-2|teorema 8.2.2]] se obtiene $f(x)=f(a)+\int_a^x\varphi(t)\,dt$, y basta derivar una [[es/08-riemann-integration#8.3 Teorema fundamental del cálculo|integral con límite superior variable]]. La condición 3 se deduce de las demás (así se señala también en los apuntes de la clase): puede pasarse a la conclusión.

## §8.3. Series funcionales

> [!definition] Definición 8.3.1
> Sea dada una sucesión de funciones $u_n:X\to\mathbb R$, $n\in\mathbb N$. La expresión $\sum_{n=1}^{\infty}u_n(x)$ se llama serie funcional. Pongamos
> $$
> S_n(x)=\sum_{k=1}^{n}u_k(x),\qquad S(x)=\lim_{n\to\infty}S_n(x),\qquad S:X\to\mathbb R .
> $$
> Una serie funcional se llama convergente en el conjunto $X$ si converge en cada punto de ese conjunto.

^def-8-3-1

> [!definition] Definición 8.3.2
> La serie $\sum_{n=1}^{\infty}u_n(x)$ se llama uniformemente convergente en el conjunto $E\subset X$ si $S_n\rightrightarrows S$ en $E$.

^def-8-3-2

> [!theorem] Criterio de Bolzano–Cauchy de convergencia uniforme
> La serie $\sum_{n=1}^{\infty}u_n(x)$ converge uniformemente en $E$ si y solo si
> $$
> \forall\varepsilon>0\ \exists N\ \forall n>N\ \forall p\in\mathbb N\ \forall x\in E\qquad\Bigl|\sum_{k=n+1}^{n+p}u_k(x)\Bigr|<\varepsilon .
> $$

> [!theorem] Criterio de Weierstrass
> Sea $|u_n(x)|\le C_n$ para todo $x\in E$ y todo $n$, y sea convergente la [[es/04-numeric-series#4.1 Sumas parciales|serie numérica]] $\sum_{n=1}^{\infty}C_n$. Entonces la serie $\sum_{n=1}^{\infty}u_n(x)$ converge en $E$ uniformemente (y absolutamente).

La convergencia uniforme y la absoluta no se implican mutuamente: la serie $\sum\frac{(-1)^{n}}{n}$ (de términos constantes) converge uniformemente pero no absolutamente, y la serie $\sum_{n=0}^{\infty}x^n$ en $[0,1)$ [[es/04-numeric-series#4.3 Convergencia absoluta y condicional|converge absolutamente]] pero no uniformemente.

> [!theorem] Teorema 8.3.1
> Sea dada una serie de funciones $u_n\in C([a,b])$, $n\in\mathbb N$, y $\sum_{n=1}^{\infty}u_n(x)=S(x)$. Si la serie $\sum_{n=1}^{\infty}u_n(x)$ converge uniformemente en $[a,b]$, entonces $S\in C([a,b])$.

^thm-8-3-1

> [!theorem] Teorema 8.3.2 (integración término a término)
> Sean $u_n\in C([a,b])$ para todo $n\in\mathbb N$ y $\sum_{n=1}^{\infty}u_n(x)=S(x)$. Si la serie $\sum_{n=1}^{\infty}u_n(x)$ converge uniformemente en $[a,b]$, entonces
> $$
> \int_a^b S(x)\,dx=\sum_{n=1}^{\infty}\int_a^b u_n(x)\,dx .
> $$

^thm-8-3-2

> [!theorem] Teorema 8.3.3 (derivación término a término)
> Sean $u_n\in C^1([a,b])$ para todo $n\in\mathbb N$ y $\sum_{n=1}^{\infty}u_n(x)=S(x)$. Si la serie $\sum_{n=1}^{\infty}u_n(x)$ converge en cada punto de $[a,b]$ y la serie $\sum_{n=1}^{\infty}u_n'(x)$ converge uniformemente en $[a,b]$, entonces $S\in C^1([a,b])$ y
> $$
> \Bigl(\sum_{n=1}^{\infty}u_n(x)\Bigr)'=\sum_{n=1}^{\infty}u_n'(x),\qquad x\in[a,b].
> $$

^thm-8-3-3

Los [[#^thm-8-3-1|teoremas 8.3.1]]–[[#^thm-8-3-3|8.3.3]] son los [[#^thm-8-2-1|teoremas 8.2.1]]–[[#^thm-8-2-3|8.2.3]] aplicados a las sumas parciales $S_n$.

## §8.4. Series de potencias

> [!definition] Definición 8.4.1
> Una serie de la forma
> $$
> \sum_{k=0}^{\infty}c_k(x-a)^k,\qquad\qquad(8.4.1)
> $$
> donde $c_k,x,a\in\mathbb R$, se llama serie de potencias (real); los números $c_k$ se llaman sus coeficientes, y $a$, su centro.

^def-8-4-1

> [!definition] Definición 8.4.2
> Una magnitud $R\in[0,+\infty]$ se llama radio de convergencia de la serie $\sum_{k=0}^{\infty}c_k(x-a)^k$ si
> 1. para todo $x$ con $|x-a|<R$ la serie converge;
> 2. para todo $x$ con $|x-a|>R$ la serie diverge.

^def-8-4-2

El intervalo $(a-R,a+R)$ se llama intervalo de convergencia; en sus extremos son posibles tanto la convergencia como la divergencia.

> [!theorem] Teorema 8.4.1 (fórmula de Cauchy–Hadamard)
> Toda serie de potencias $\sum_{k=0}^{\infty}c_k(x-a)^k$ tiene radio de convergencia, y este viene dado por la fórmula
> $$
> R=\frac{1}{\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}} .
> $$

^thm-8-4-1

Aquí $\frac10=+\infty$, $\frac1{+\infty}=0$. La demostración es el criterio de Cauchy para la serie $\sum|c_k(x-a)^k|$ en su forma con [[es/03-sequences#3.5 Límite superior e inferior|límite superior]]. Si existe $\lim_{n\to\infty}\bigl|\frac{c_n}{c_{n+1}}\bigr|$, es igual a $R$ ([[es/04-numeric-series#4.2 Términos no negativos|criterio de d'Alembert]]).

> [!remark] Observación 8.4.1
> Por el criterio de Cauchy, para $|x-a|<R$ la serie $\sum_{k=0}^{\infty}c_k(x-a)^k$ converge absolutamente.

^rem-8-4-1

> [!remark] Observación 8.4.2
> El cambio $x-a=y$ transforma la serie (8.4.1) en la serie de potencias $\sum_{k=0}^{\infty}c_ky^k$ centrada en cero, por lo que al deducir propiedades de las series de potencias puede suponerse $a=0$.

^rem-8-4-2

> [!theorem] Teorema 8.4.2 (convergencia uniforme de las series de potencias)
> Sea $R\in(0,+\infty]$ el radio de convergencia de la serie de potencias $\sum_{k=0}^{\infty}c_k(x-a)^k$. Entonces para todo $r\in(0,R)$ la serie de potencias converge uniformemente en el segmento $[a-r,a+r]$.

^thm-8-4-2

La demostración es el criterio de Weierstrass con $C_k=|c_k|r^k$ (la serie $\sum|c_k|r^k$ converge por la [[#^rem-8-4-1|observación 8.4.1]]). En todo el intervalo de convergencia puede no haber convergencia uniforme: $\sum x^k$ en $(-1,1)$.

> [!theorem] Teorema 8.4.3 (teorema de Abel sobre series de potencias)
> Sea $R\in(0,+\infty)$ el radio de convergencia de la serie de potencias $\sum_{k=0}^{\infty}c_k(x-a)^k$. Si la serie de potencias converge en $x=a+R$ (respectivamente en $x=a-R$), entonces converge uniformemente en el segmento $[a,a+R]$ (respectivamente en $[a-R,a]$), y su suma es [[es/05-limits-continuity#5.3 Continuidad|continua en el punto]] $a+R$ por la izquierda (respectivamente en el punto $a-R$ por la derecha).

^thm-8-4-3

La demostración se apoya en el **criterio de Abel de convergencia uniforme**: si la serie $\sum f_k(x)$ converge uniformemente en $X$ y, para cada $x$, la sucesión $(g_k(x))$ es monótona, con $|g_k(x)|\le M$ para todo $k$ y $x\in X$, entonces la serie $\sum f_k(x)g_k(x)$ converge uniformemente en $X$. Aquí $f_k=c_kR^k$ (una serie numérica convergente), $g_k(x)=\bigl(\frac{x-a}{R}\bigr)^k$, $x\in[a,a+R]$.

> [!theorem] Teorema 8.4.4 (integración de series de potencias)
> Sea $R\in(0,+\infty]$ el radio de convergencia de la serie de potencias $\sum_{k=0}^{\infty}c_k(x-a)^k$. Si $[A,B]\subset(a-R,a+R)$, entonces
> $$
> \int_A^B\sum_{k=0}^{\infty}c_k(x-a)^k\,dx=\sum_{k=0}^{\infty}c_k\,\frac{(B-a)^{k+1}-(A-a)^{k+1}}{k+1}.\qquad\qquad(8.4.2)
> $$
> Si además $R<+\infty$ y la serie converge en $x=a+R$ (respectivamente en $x=a-R$), la igualdad (8.4.2) vale también para $B=a+R$ (respectivamente para $A=a-R$).

^thm-8-4-4

> [!theorem] Teorema 8.4.5 (sobre los radios de las series de potencias)
> Los radios de convergencia de las series de potencias
> $$
> \sum_{k=0}^{\infty}c_k(x-a)^k,\qquad \sum_{k=1}^{\infty}kc_k(x-a)^{k-1},\qquad \sum_{k=0}^{\infty}\frac{c_k}{k+1}(x-a)^{k+1}
> $$
> son iguales.

^thm-8-4-5

Se deduce de la fórmula de Cauchy–Hadamard, ya que $\sqrt[k]{k}\to1$ y $\sqrt[k]{k+1}\to1$.

> [!theorem] Teorema 8.4.6 (derivación de series de potencias)
> Sea $R\in(0,+\infty]$ el radio de convergencia de la serie $f(x)=\sum_{k=0}^{\infty}c_k(x-a)^k$. Entonces $f$ es infinitamente [[es/06-derivatives#6.1 Definición y aproximación lineal|diferenciable]] en el intervalo $|x-a|<R$, y la serie puede derivarse término a término cualquier número de veces:
> $$
> f^{(m)}(x)=\sum_{k=m}^{\infty}k(k-1)\dots(k-m+1)\,c_k(x-a)^{k-m},\qquad |x-a|<R,\quad m\in\mathbb N .
> $$

^thm-8-4-6

> [!theorem] Teorema 8.4.7 (unicidad del desarrollo de una función en serie de potencias)
> Sea $R\in(0,+\infty]$ el radio de convergencia de la serie $f(x)=\sum_{k=0}^{\infty}c_k(x-a)^k$. Entonces $f\in C^\infty(a-R,a+R)$, y los coeficientes están determinados de manera única:
> $$
> c_k=\frac{f^{(k)}(a)}{k!} .
> $$

^thm-8-4-7

Sustituya $x=a$ en la fórmula del [[#^thm-8-4-6|teorema 8.4.6]]: todos los términos con $k>m$ se anulan, y $f^{(m)}(a)=m!\,c_m$.

> [!definition] Definición 8.4.3
> Sea $f$ con derivadas de todos los órdenes en el punto $a$. Los números $c_k=\frac{f^{(k)}(a)}{k!}$ se llaman coeficientes de Taylor, y la serie
> $$
> \sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k
> $$
> se llama serie de Taylor de la función $f$ centrada en el punto $a$. La serie de Taylor centrada en cero se llama [[es/07-taylor-convexity#7.3 Fórmula de Taylor|serie de Maclaurin]].

^def-8-4-3

> [!theorem] Teorema 8.4.8 (criterio de desarrollabilidad de una función en serie de Taylor)
> Sean $f\in C^\infty(A,B)$, $a,x\in(A,B)$, $a\ne x$, y supongamos que existe $M\in(0,\infty)$ tal que $|f^{(n)}(t)|\le M$ para todo $n\in\mathbb N$ y todo $t$ situado entre $a$ y $x$. Entonces
> $$
> \sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k=f(x).
> $$

^thm-8-4-8

La demostración es la estimación del resto de Lagrange: $|f(x)-T_{a,n}f(x)|\le\frac{M|x-a|^{n+1}}{(n+1)!}\to0$. Así se obtienen los desarrollos de $e^x$, $\sin x$, $\cos x$ en toda la recta.

> [!definition] Definición 8.4.4
> Sean $-\infty\le A<B\le+\infty$, $f:(A,B)\to\mathbb R$, $a\in(A,B)$. La función $f$ se llama analítica en el punto $a$ si existen números $r>0$ y $c_k\in\mathbb R$ tales que
> $$
> f(x)=\sum_{k=0}^{\infty}c_k(x-a)^k,\qquad x\in(a-r,a+r).
> $$
> Una función se llama analítica en $(A,B)$ si es analítica en cada punto de $(A,B)$.

^def-8-4-4

Por los [[#^thm-8-4-6|teoremas 8.4.6]] y [[#^thm-8-4-7|8.4.7]] una función analítica es infinitamente diferenciable, y su serie de potencias es su serie de Taylor. El recíproco es falso: la función $e^{-1/x^2}$ (extendida por cero en cero) tiene serie de Maclaurin nula; la función $\sum_{n=0}^{\infty}e^{-\sqrt{2^n}}\cos(2^nx)$ de la clase tiene una serie de Taylor en cero que diverge para todo $x\ne0$.

## Ejemplo resuelto

**La serie $\sum_{k=1}^{\infty}\frac{x^k}{k}$.** Por la fórmula de Cauchy–Hadamard $R=1$, ya que $\sqrt[k]{1/k}\to1$. En $(-1,1)$ la derivación término a término ([[#^thm-8-4-6|teorema 8.4.6]]) da $f'(x)=\sum_{k=1}^{\infty}x^{k-1}=\frac{1}{1-x}$, y teniendo en cuenta $f(0)=0$
$$
\sum_{k=1}^{\infty}\frac{x^k}{k}=-\ln(1-x),\qquad |x|<1 .
$$
En $x=1$ se obtiene la serie armónica, que diverge. En $x=-1$ la serie $\sum\frac{(-1)^k}{k}$ converge por el [[es/04-numeric-series#^alternating-series-test|criterio de Leibniz]], así que por el [[es/11-power-series#^abel-theorem|teorema de Abel]] la suma es continua en el punto $-1$ por la derecha: $\sum_{k=1}^{\infty}\frac{(-1)^k}{k}=-\ln2$. El conjunto de convergencia es $[-1,1)$.

**¿Es uniforme la convergencia?** Sea $f_n(x)=\frac{nx}{1+n^2x^2}$ en $[0,1]$. Puntualmente $f_n\to0$, pero $f_n\bigl(\frac1n\bigr)=\frac12$, luego $\rho(f_n,0)\ge\frac12$, y la convergencia no es uniforme. En $[\delta,1]$ con $\delta>0$ tenemos $0\le f_n(x)\le\frac{1}{nx}\le\frac{1}{n\delta}\to0$, así que la convergencia es uniforme.

## Errores frecuentes

1. Suponer que el límite puntual de funciones continuas es continuo: $x^n$ en $[0,1]$.
2. Intercambiar un límite y una integral sin convergencia uniforme (el ejemplo de los «dientes»).
3. Derivar una serie término a término tras comprobar la convergencia uniforme de la propia serie y no la de la serie de derivadas: $\sum\frac{\sin(n^2x)}{n^2}$ converge uniformemente, mientras que la serie de derivadas $\sum\cos(n^2x)$ diverge, por ejemplo, en $x=0$.
4. Sacar conclusiones sobre los extremos del intervalo a partir del radio: $\sum\frac{x^k}{k^2}$ converge en ambos extremos, $\sum x^k$ en ninguno, $\sum\frac{x^k}{k}$ en uno.
5. Considerar analítica toda función infinitamente diferenciable ($e^{-1/x^2}$).

## Ejercicios

1. Halle el radio y el conjunto de convergencia de la serie $\sum_{k=1}^{\infty}\frac{(x-2)^k}{k\,3^k}$.
2. ¿Converge la sucesión $f_n(x)=x^n(1-x)$ uniformemente en $[0,1]$?
3. Demuestre que la función $\sum_{n=1}^{\infty}\frac{\sin nx}{n^2}$ es continua en $\mathbb R$.
4. Desarrolle $\operatorname{arctg}x$ en serie de Maclaurin y halle la suma $\sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1}$.

> [!answer]- Respuestas breves
> 1. $R=3$; en $x=5$ la serie armónica (diverge), en $x=-1$ una serie de Leibniz (converge); el conjunto de convergencia es $[-1,5)$.
> 2. Sí: el máximo de $f_n$ se alcanza en $x=\frac{n}{n+1}$ y no supera $\frac{1}{n+1}\to0$.
> 3. El criterio de Weierstrass con $C_n=\frac1{n^2}$ y el [[#^thm-8-3-1|teorema 8.3.1]] en cada segmento $[a,b]$.
> 4. La integración término a término de la serie $\frac1{1+t^2}=\sum_{k=0}^{\infty}(-1)^kt^{2k}$ sobre $[0,x]$ ([[#^thm-8-4-4|teorema 8.4.4]]) da $\operatorname{arctg}x=\sum_{k=0}^{\infty}\frac{(-1)^kx^{2k+1}}{2k+1}$ para $|x|<1$; en $x=1$ la serie converge y, por el teorema de Abel, su suma es $\frac\pi4$.

---

[[es/23-numerical-series|← 23. Series numéricas]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/25-parameter-integrals|25. Integrales dependientes de un parámetro →]]

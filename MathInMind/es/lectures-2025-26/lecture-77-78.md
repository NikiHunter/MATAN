---
title: "Lecciones 77–78 — integración respecto de un parámetro, integrales impropias dependientes de un parámetro, método de Feynman"
lang: es
course: "Análisis matemático, 2025/26"
lecture: 77-78
semester: 3
source: "cuaderno manuscrito, págs. p058–p066"
source_pages: "p058, p059, p060, p061, p062, p063, p064, p065, p066"
course_chapter: 25
---
# Lecciones 77–78 — integración respecto de un parámetro, integrales impropias dependientes de un parámetro, método de Feynman

[← Lecciones 75–76](lecture-75-76.md) · [Índice de lecciones](index.md) · [Lecciones 79–80 →](lecture-79-80.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-77-78.md) · [English](../../en/lectures-2025-26/lecture-77-78.md)

> **Fuente y numeración.** Los apuntes se copiaron de un cuaderno manuscrito (págs. p058–p066; el texto bruto de las páginas está en [`ocr/raw/`](../../../ocr/raw/p058.md)). La pág. p058 comienza con el final del ejemplo de la ecuación de Bessel de §9.1 (su comienzo está en las lecciones 75–76); en el margen de la misma página empieza en rojo la anotación «Lecciones 77–78» con el plan de la clase: integración de una integral respecto de un parámetro para integrales propias; teoremas sobre [integrales impropias](lecture-47-48.md#def-4-5-2) dependientes de un parámetro; propiedades de la [función gamma](lecture-79-80.md#def-9-3-1) (en el cuaderno la función gamma figura ya en las lecciones 79–80). La numeración de definiciones y teoremas es la del profesor; los enunciados se cotejaron con las diapositivas del curso 2024/25 (FS p84–p87). Los [teoremas 9.1.3](#thm-9-1-3), [9.2.2](#thm-9-2-2) y [9.2.3](#thm-9-2-3) figuran en los apuntes sin demostración (el [teorema 9.1.3](#thm-9-1-3) se dio también «sin dem.» en 2024/25, FS p84), del [teorema 9.2.1](#thm-9-2-1) solo se anota la idea de la demostración y el criterio de Bolzano–Cauchy se demuestra brevemente; las demostraciones que faltan se restauran según cursos estándar (Fichtenholz, t. II, cap. XIV; Zorich, t. II, cap. XVII). El ejemplo motivador del comienzo de §9.2, muy deformado en la transcripción, se restaura por su sentido. Las figuras del margen de la pág. p060 (ejes numéricos para el criterio de Bolzano–Cauchy) se describen con palabras. Los lapsus de los apuntes se corrigen y se marcan con bloques «Corrección de la fuente»; los pasajes perdidos se restauran y se marcan con bloques «Restaurado»; las etiquetas corresponden a [`ocr/RESOLVED.md`](../../../ocr/RESOLVED.md). Los lugares que aún hay que cotejar con el cuaderno se enumeran en [`ocr/ISSUES.md`](../../../ocr/ISSUES.md).

## §9.1. Integrales propias dependientes de un parámetro (conclusión)

<a id="p058"></a>

**Ejemplo (ecuación de Bessel, conclusión).** Para la función $`u(x)=\int_0^{\pi}\cos(n\varphi-x\sin\varphi)\,d\varphi`$ ($`n`$ entero) en las lecciones 75–76 se obtuvo
```math
x^2u''+xu'+(x^2-n^2)u=\int_0^{\pi}\Bigl[-x^2\sin^2\varphi\cos(n\varphi-x\sin\varphi)+x\sin\varphi\sin(n\varphi-x\sin\varphi)+(x^2-n^2)\cos(n\varphi-x\sin\varphi)\Bigr]d\varphi .
```
Agrupemos términos semejantes y observemos que el integrando es una [derivada](lecture-22-23.md#def-3-1-1) respecto de $`\varphi`$:
```math
\begin{aligned}
x^2u''+xu'+(x^2-n^2)u&=\int_0^{\pi}\Bigl[(1-\sin^2\varphi)x^2\cos(n\varphi-x\sin\varphi)+x\sin\varphi\sin(n\varphi-x\sin\varphi)-n^2\cos(n\varphi-x\sin\varphi)\Bigr]d\varphi\\
&=\int_0^{\pi}\frac{d}{d\varphi}\Bigl[-(n+x\cos\varphi)\sin(n\varphi-x\sin\varphi)\Bigr]d\varphi=-(n+x\cos\varphi)\sin(n\varphi-x\sin\varphi)\Big|_{\varphi=0}^{\varphi=\pi}=0 ,
\end{aligned}
```
ya que $`\sin0=0`$ y $`\sin n\pi=0`$ para $`n`$ entero. Así, $`u`$ satisface la ecuación de Bessel $`x^2u''+xu'+(x^2-n^2)u=0`$.

> **Corrección de la fuente** (M256, T524). En los apuntes el integrando contiene «$`+n^2\cos(n\varphi-x\sin\varphi)`$», y el resultado se escribe «$`\left.0\right|_{0}^{\pi}`$ ✓». El término $`(x^2-n^2)u`$ da bajo la integral $`-n^2\cos(n\varphi-x\sin\varphi)`$, y solo con este signo el integrando es una derivada: para $`\psi(\varphi)=n\varphi-x\sin\varphi`$, $`\psi'(\varphi)=n-x\cos\varphi`$,
> ```math
> \frac{d}{d\varphi}\Bigl[-(n+x\cos\varphi)\sin\psi\Bigr]=x\sin\varphi\sin\psi-(n+x\cos\varphi)(n-x\cos\varphi)\cos\psi=x^2\cos^2\varphi\cos\psi+x\sin\varphi\sin\psi-n^2\cos\psi .
> ```
> La integral de una derivada es la diferencia de los valores de la [primitiva](lecture-36.md#def-4-1-1) en $`\varphi=\pi`$ y $`\varphi=0`$; ambos son nulos.

### Sobre la integración de una integral respecto de un parámetro

<a id="thm-9-1-3"></a>**Teorema 9.1.3.** Sean $`P=\{(x,y)\in\mathbb R^2:\ a\le x\le b,\ c\le y\le d\}`$ y $`f=f(x,y)\in C(P)`$. Entonces la función $`I(y)=\int_a^bf(x,y)\,dx`$ es integrable en $`[c,d]`$ y se cumple la igualdad
```math
\int_c^d\left(\int_a^bf(x,y)\,dx\right)dy=\int_a^b\left(\int_c^df(x,y)\,dy\right)dx .
```

> **Restaurado** (según la demostración estándar, cf. Fichtenholz, t. II, cap. XIV; en los apuntes no hay demostración, y en la diapositiva del curso 2024/25, FS p84, el teorema lleva la marca «sin dem.»).
>
> **Demostración.** Por el [teorema 9.1.1](lecture-75-76.md#thm-9-1-1) la función $`I`$ es continua en $`[c,d]`$ y, por tanto, integrable en $`[c,d]`$; por el mismo teorema (intercambiando los papeles de las variables) la función $`x\mapsto\int_c^df(x,y)\,dy`$ es continua en $`[a,b]`$. Para $`u\in[c,d]`$ pongamos
> ```math
> \Phi(u)=\int_c^u\left(\int_a^bf(x,y)\,dx\right)dy,\qquad\Psi(u)=\int_a^bF(x,u)\,dx,\qquad F(x,u)=\int_c^uf(x,y)\,dy .
> ```
> Como $`I`$ es continua, por el teorema de Barrow $`\Phi'(u)=I(u)=\int_a^bf(x,u)\,dx`$. La función $`F`$ es continua en $`P`$: si $`M=\max_P|f|`$, entonces
> ```math
> |F(x',u')-F(x,u)|\le\left|\int_u^{u'}f(x',y)\,dy\right|+\int_c^d|f(x',y)-f(x,y)|\,dy\le M|u'-u|+(d-c)\max_{y\in[c,d]}|f(x',y)-f(x,y)| ,
> ```
> y el último sumando tiende a cero cuando $`x'\to x`$, ya que $`f`$ es [uniformemente continua](lecture-17-18.md#def-2-5-7) en el [compacto](lecture-57-58.md#def-5-3-7) $`P`$ (teorema de Cantor). Por el teorema de Barrow $`\frac{\partial F}{\partial u}(x,u)=f(x,u)`$, y esta función también es continua en $`P`$. Por tanto, por el [teorema 9.1.2](lecture-75-76.md#thm-9-1-2) (con el parámetro $`u`$), la función $`\Psi`$ es [derivable](lecture-22-23.md#def-3-2-1) en $`[c,d]`$ y $`\Psi'(u)=\int_a^b\frac{\partial F}{\partial u}(x,u)\,dx=\int_a^bf(x,u)\,dx`$. Así, $`\Phi'=\Psi'`$ en $`[c,d]`$ y $`\Phi(c)=\Psi(c)=0`$ (ya que $`F(x,c)=0`$); en consecuencia, $`\Phi\equiv\Psi`$ en $`[c,d]`$. Para $`u=d`$ se obtiene la igualdad buscada. $`\square`$

**Ejemplo.** Calculemos la integral
```math
I(b)=\int_0^1\frac{x^b-x^a}{\ln x}\,dx ,\qquad a,b>-1 .
```
Consideramos $`a`$ fijo y $`b`$ variable. La idea: representar el integrando como una integral respecto de una variable auxiliar $`z`$. Como $`\frac{\partial}{\partial z}\left(\frac{x^z}{\ln x}\right)=\frac{\ln x\cdot x^z}{\ln x}=x^z`$ para $`0<x<1`$, se tiene
```math
\int_a^bx^z\,dz=\frac{x^z}{\ln x}\Big|_{z=a}^{z=b}=\frac{x^b-x^a}{\ln x},
```
es decir,
```math
I(b)=\int_0^1\left(\int_a^bx^z\,dz\right)dx .
```
La integral $`\int_0^1x^s\,dx`$ converge si y solo si $`s>-1`$, y entonces vale $`\frac1{s+1}`$; por tanto, para $`a,b>-1`$ las integrales $`\int_0^1x^z\,dx`$ convergen para todo $`z`$ entre $`a`$ y $`b`$. Cambiando el orden de integración ([teorema 9.1.3](#thm-9-1-3)), obtenemos
```math
I(b)=\int_a^b\left(\int_0^1x^z\,dx\right)dz=\int_a^b\frac{dz}{z+1}=\ln|1+z|\,\Big|_a^b=\ln\frac{b+1}{a+1} .
```

> **Corrección de la fuente** (M262). En los apuntes: «Cons. $`\int_0^1x^s\,dx<+\infty\Rightarrow b>-1`$», y luego «$`\int_a^b>-1\Rightarrow I(b)=\int_0^1\left(\int_a^bx^z\,dz\right)dx=\int_a^b\left(\int_0^1x^z\,dx\right)dx`$». La condición de convergencia es $`s>-1`$, y hace falta para todo $`z`$ entre $`a`$ y $`b`$, es decir, $`a,b>-1`$; tras el intercambio la integral exterior se toma respecto de $`z`$ (la [diferencial](lecture-24-25-26.md#def-3-3-1) $`dz`$, y no $`dx`$).

> **Restaurado** (según el razonamiento estándar; en los apuntes el intercambio de integrales no se justifica). El [teorema 9.1.3](#thm-9-1-3) se refiere a una función continua en un rectángulo, mientras que para $`\min\{a,b\}\le0`$ la función $`x^z`$ no es continua (o no está acotada) cerca de $`x=0`$, y la integral $`I(b)`$ puede ser impropia en cero. Por eso aplicamos el [teorema 9.1.3](#thm-9-1-3) a la función continua $`x^z`$ en el rectángulo $`[\varepsilon,1]\times[\min\{a,b\},\max\{a,b\}]`$, $`0<\varepsilon<1`$ (para $`x=1`$ el integrando $`I(b)`$ se prolonga por su límite $`b-a`$, lo que concuerda con $`\int_a^b1^z\,dz=b-a`$):
> ```math
> \int_\varepsilon^1\frac{x^b-x^a}{\ln x}\,dx=\int_a^b\left(\int_\varepsilon^1x^z\,dx\right)dz=\int_a^b\frac{1-\varepsilon^{z+1}}{z+1}\,dz .
> ```
> Sea $`m=\min\{a,b\}>-1`$. Para $`z`$ entre $`a`$ y $`b`$ se tiene $`0<\varepsilon^{z+1}\le\varepsilon^{m+1}`$, por lo que $`\left|\int_a^b\frac{\varepsilon^{z+1}}{z+1}\,dz\right|\le\varepsilon^{m+1}\left|\ln\frac{b+1}{a+1}\right|\to0`$ cuando $`\varepsilon\to0+`$. Así, la integral $`I(b)`$ converge y vale $`\ln\frac{b+1}{a+1}`$.

## §9.2. Integrales impropias dependientes de un parámetro

<a id="p059"></a>

### Un ejemplo motivador

**Ejemplo.** Para $`y\in[0,+\infty)`$ consideremos la integral
```math
I(y)=\int_0^1\frac{x+y}{x^{1-y}}\,dx=\int_0^1(x+y)\,x^{y-1}\,dx ,\qquad x\in(0,1] .
```
Para $`y>0`$
```math
I(y)=\int_0^1x^{y}\,dx+y\int_0^1x^{y-1}\,dx=\frac{x^{y+1}}{y+1}\Big|_0^1+y\,\frac{x^{y}}{y}\Big|_0^1=\frac1{y+1}+1 ,
```
es decir, $`I(y)\to2`$ para $`y\to0+`$. Por otra parte, para $`y=0`$
```math
I(0)=\int_0^1\frac xx\,dx=\int_0^1 1\,dx=1 .
```
Así, $`\lim_{y\to0+}I(y)=2\ne1=I(0)`$: la función $`I`$ es discontinua en el punto $`y=0`$, aunque el integrando es continuo respecto de $`y`$ para cada $`x\in(0,1]`$.

> **Restaurado** (por el sentido de la anotación; la transcripción del ejemplo en el cuaderno está muy deformada: etiquetas U264–M268). En la transcripción: «$`I(y)=\int_0^1\frac{x+y}{x^{y/3}}\,dx`$», «$`=\int_0^1x^{-y}dx+\int_0^1x^{y-3}dx=\left.\frac{x^{y+1}}{y+1}\right|_0^1+\left.y\frac{x^3}{3}\right|_0^1=\frac1{y+1}+1`$», «es decir, $`x\in(0,1]\Rightarrow I(y)\to2`$», «$`\Rightarrow\left|I(y)-\frac{2}{y\to0}\right|\not\to I(0)`$». El integrando se restaura como $`(x+y)x^{y-1}`$: solo con él $`f(x,0)=\frac xx`$ (como en la línea para $`I(0)`$), el primer sumando da el $`\frac{x^{y+1}}{y+1}\Big|_0^1=\frac1{y+1}`$ anotado, el segundo (con el factor conservado $`y`$) da uno, y el resultado $`\frac1{y+1}+1`$ coincide con los apuntes; la última línea significa $`I(y)\to2\ne I(0)`$ para $`y\to0`$. La causa de la discontinuidad está en el comportamiento de la integral cerca del punto singular $`x=0`$: para todo $`\delta\in(0,1]`$
> ```math
> \int_0^{\delta}(x+y)\,x^{y-1}\,dx=\frac{\delta^{y+1}}{y+1}+\delta^{y}\ \ge\ \delta^{y}\to1\qquad(y\to0+),
> ```
> es decir, la «cola» de la integral cerca del punto singular no puede hacerse pequeña a la vez para todo $`y>0`$. Esto conduce a la noción de [convergencia uniforme](../10-function-sequences-series.md#sec-10-1) de una integral impropia ([definición 9.2.1](#def-9-2-1); aquí la singularidad está en el [límite inferior](lecture-13.md#def-2-3-9), véase la observación tras los ejemplos).

### Integrales impropias dependientes de un parámetro

Sea la función $`f(x,y)`$ definida en el conjunto $`[a,b)\times Y`$, donde $`-\infty<a<b\le+\infty`$. Supondremos que la función $`f`$ es continua respecto de $`x`$ para cada $`y\in Y`$ fijo. Consideremos la integral impropia
```math
I(y):=\int_a^{\to b}f(x,y)\,dx=\lim_{\omega\to b}\int_a^{\omega}f(x,y)\,dx=\lim_{\omega\to b}I_\omega(y),\qquad I_\omega(y):=\int_a^{\omega}f(x,y)\,dx,\quad\omega\in[a,b) .
```
En adelante escribimos tal integral simplemente como $`\int_a^bf(x,y)\,dx`$ y suponemos que converge para cada $`y\in Y`$.

<a id="def-9-2-1"></a>**Definición 9.2.1.** Diremos que $`I(y)`$ converge uniformemente respecto de $`y\in Y`$ (uniformemente en $`Y`$) si
```math
\forall\varepsilon>0\ \ \exists b_0\in[a,b)\ \ \forall b'\in(b_0,b)\ \ \forall y\in Y:\quad |I_{b'}(y)-I(y)|=\left|\int_{b'}^{b}f(x,y)\,dx\right|<\varepsilon .
```
En otras palabras, para la convergencia uniforme de la integral impropia $`I(y)`$ se requiere que $`I_{b'}(y)\rightrightarrows I(y)`$ en $`Y`$ cuando $`b'\to b`$.

> **Corrección de la fuente** (S271, T272). En los apuntes (también en la diapositiva FS p85): «$`\forall\varepsilon>0\ \exists b_0\in[a,b)`$ tal que $`\forall b'>b_0\ |I_{b'}(y)-I(y)|<\varepsilon`$», sin [cuantificador](../01-logic-sets-functions.md#sec-1-1) sobre $`y`$ y sin indicar que $`b'<b`$; luego «$`I_{b'}(y)\rightrightarrows I(y)`$, $`b\to b`$». Se añaden los cuantificadores $`\forall b'\in(b_0,b)`$ y $`\forall y\in Y`$, con $`\forall y`$ situado tras la elección de $`b_0`$: es justo lo que expresa la observación siguiente; el paso al límite es $`b'\to b`$.

**Observación.** En la [definición 9.2.1](#def-9-2-1) es esencial que $`b_0`$ no dependa de $`y`$, sino solo de $`\varepsilon`$.

Recordemos que una serie funcional $`\sum_{n=1}^{\infty}a_n(y)=S(y)`$ converge uniformemente en $`Y`$ si $`S_n(y)=\sum_{k=1}^{n}a_k(y)\rightrightarrows S(y)`$ en $`Y`$.

> **Corrección de la fuente** (T273). En los apuntes: «Una serie funcional … conv. si: $`S_n(y)=\sum a_n(y)\rightrightarrows S(y)`$». Se trata de la convergencia uniforme, y la [suma parcial](../04-numeric-series.md#sec-4-1) es $`S_n(y)=\sum_{k=1}^{n}a_k(y)`$ (así en la diapositiva FS p85).

<a id="p060"></a>

Así, la convergencia uniforme de una integral y la de una serie se describen de la misma manera:

| Integral | Serie |
|---|---|
| $`I_t(y)\rightrightarrows I(y)`$ en $`Y`$ cuando $`t\to b`$ | $`S_n(y)\rightrightarrows S(y)`$ en $`Y`$ cuando $`n\to\infty`$ |

### Criterio de Bolzano–Cauchy

La integral impropia $`I(y)=\int_a^bf(x,y)\,dx`$ converge uniformemente en $`Y`$ si y solo si
```math
\forall\varepsilon>0\ \ \exists b_0\in[a,b)\ \ \forall t_1,t_2\in(b_0,b)\ \ \forall y\in Y:\quad\left|\int_{t_1}^{t_2}f(x,y)\,dx\right|<\varepsilon .
```
Análogamente, la serie $`\sum_{k=1}^{\infty}a_k(y)`$ converge uniformemente en $`Y`$ si y solo si
```math
\forall\varepsilon>0\ \ \exists n_0\in\mathbb N\ \ \forall m>n>n_0\ \ \forall y\in Y:\quad\left|\sum_{k=n}^{m}a_k(y)\right|<\varepsilon .
```

*Figuras de los apuntes (pág. p060): junto a la condición para la integral, un eje numérico con los puntos $`a<b_0<t_1<t_2<b`$; junto a la condición para la serie, un eje con los índices $`n_0<n<m`$.*

> **Corrección de la fuente** (M525). En los apuntes (también en la diapositiva FS p85) a las condiciones del criterio les falta el cuantificador «$`\forall y\in Y`$», y sin él la condición no expresa uniformidad. Se añade $`\forall y\in Y`$ tras la elección de $`b_0`$ (respectivamente $`n_0`$); del mismo modo se completan las líneas finales de la demostración del criterio de Dirichlet.

**Demostración** (para la integral). La desigualdad $`\left|\int_{t_1}^{t_2}f(x,y)\,dx\right|<\varepsilon`$ equivale a la desigualdad $`|I_{t_2}(y)-I_{t_1}(y)|<\varepsilon`$. Por tanto, la afirmación es el criterio de Bolzano–Cauchy de convergencia uniforme de las funciones $`I_t(y)`$, dependientes del parámetro $`t`$, cuando $`t\to b`$.

> **Restaurado** (según la demostración estándar, cf. Zorich/Fichtenholz; en los apuntes la demostración es breve, y el criterio de Bolzano–Cauchy se demostró para sucesiones de funciones).
>
> *Necesidad.* Supongamos que $`I(y)`$ converge uniformemente en $`Y`$, y sea $`\varepsilon>0`$. Por la [definición 9.2.1](#def-9-2-1) existe $`b_0\in[a,b)`$ tal que $`\left|\int_t^bf(x,y)\,dx\right|<\frac{\varepsilon}2`$ para todo $`t\in(b_0,b)`$ y $`y\in Y`$. Entonces, para $`t_1,t_2\in(b_0,b)`$ y $`y\in Y`$
> ```math
> \left|\int_{t_1}^{t_2}f(x,y)\,dx\right|=\left|\int_{t_1}^{b}f(x,y)\,dx-\int_{t_2}^{b}f(x,y)\,dx\right|<\frac{\varepsilon}2+\frac{\varepsilon}2=\varepsilon .
> ```
> *Suficiencia.* Supongamos que se cumple la condición del criterio. Para cada $`y\in Y`$ fijo es la [condición de Cauchy](lecture-13.md#def-2-3-10) de existencia de límite finito de la función $`t\mapsto I_t(y)`$ cuando $`t\to b`$; por tanto, la integral $`I(y)`$ converge para cada $`y\in Y`$. Pasando al límite cuando $`t_2\to b`$ en la desigualdad $`\left|\int_{t_1}^{t_2}f(x,y)\,dx\right|<\varepsilon`$, obtenemos $`|I(y)-I_{t_1}(y)|=\left|\int_{t_1}^{b}f(x,y)\,dx\right|\le\varepsilon`$ para todo $`t_1\in(b_0,b)`$ y $`y\in Y`$. Como $`\varepsilon>0`$ es arbitrario, la integral $`I(y)`$ converge uniformemente en $`Y`$. $`\square`$
>
> Para las series el criterio se demostró en las lecciones 71–72.

### Criterio de Weierstrass

Supongamos que existe una función $`\varphi:[a,b)\to[0,+\infty)`$, integrable en cada segmento $`[a,t]\subset[a,b)`$, tal que

1. $`|f(x,y)|\le\varphi(x)`$ para todo $`x\in[a,b)`$ y $`y\in Y`$;
2. la integral impropia $`\int_a^b\varphi(x)\,dx`$ converge.

Entonces la integral $`I(y)=\int_a^bf(x,y)\,dx`$ converge uniformemente en $`Y`$.

Para series: si existen números $`C_n>0`$ tales que $`|a_n(y)|\le C_n`$ para todo $`n\in\mathbb N`$ y $`y\in Y`$, y la serie $`\sum_{n=1}^{\infty}C_n`$ converge, entonces la serie $`\sum_{n=1}^{\infty}a_n(y)`$ converge uniformemente en $`Y`$ (lecciones 71–72).

> **Corrección de la fuente** (U277). En los apuntes las condiciones para la integral se escriben «∃ fn $`Y`$ tal que $`\forall x\in[a,b),\forall y\in Y\ |f(x,y)|\le\varphi(x)`$; 1) $`\int_a^b\varphi(x)\,dx\le\infty`$», y los números 1), 2) se mezclan con las líneas para la serie. Se lee como en la diapositiva FS p85: «$`\exists`$ una función $`\varphi`$ tal que 1) $`|f(x,y)|\le\varphi(x)`$ …; 2) $`\int_a^b\varphi(x)\,dx<\infty`$»: la integral de la mayorante converge («$`\le\infty`$» carece de sentido).

**Demostración.** La afirmación se deduce de la estimación
```math
\left|\int_{t_1}^{t_2}f(x,y)\,dx\right|\le\int_{t_1}^{t_2}|f(x,y)|\,dx\le\int_{t_1}^{t_2}\varphi(x)\,dx\qquad(a\le t_1<t_2<b)
```
y del criterio de Bolzano–Cauchy. En efecto, como $`\int_a^b\varphi(x)\,dx`$ converge, para todo $`\varepsilon>0`$ existe $`b_0\in[a,b)`$ tal que $`\int_{t_1}^{t_2}\varphi(x)\,dx<\varepsilon`$ para $`b_0<t_1<t_2<b`$; el miembro derecho de la estimación no depende de $`y`$, por lo que se cumple la condición del criterio de Bolzano–Cauchy. $`\square`$

<a id="p061"></a>

**Ejemplo.** La integral $`\int_0^{\infty}\frac{\cos(\alpha x)}{1+x^2}\,dx`$ converge uniformemente respecto de $`\alpha\in\mathbb R`$: para todo $`x\ge0`$ y $`\alpha\in\mathbb R`$
```math
\left|\frac{\cos(\alpha x)}{1+x^2}\right|\le\frac1{1+x^2},
```
y la integral $`\int_0^{\infty}\frac{dx}{1+x^2}=\frac{\pi}2`$ converge; basta aplicar el [criterio de Weierstrass](../10-function-sequences-series.md#weierstrass-m-test).

### Criterio de Dirichlet

Sean las funciones $`f`$ y $`g`$ definidas en $`[a,b)\times Y`$, continuas respecto de $`x`$ para cada $`y\in Y`$, y supongamos que

1. para cada $`y\in Y`$ la función $`f(\cdot,y)`$ es monótona en $`[a,b)`$, y $`f(x,y)\rightrightarrows0`$ en $`Y`$ cuando $`x\to b`$, es decir, $`\sup_{y\in Y}|f(x,y)|\to0`$ cuando $`x\to b`$;
2. las primitivas $`G(t,y):=\int_a^tg(x,y)\,dx`$ están uniformemente acotadas: existe $`C>0`$ tal que $`|G(t,y)|\le C`$ para todo $`t\in[a,b)`$ y $`y\in Y`$.

Entonces la integral $`\int_a^bf(x,y)g(x,y)\,dx`$ converge uniformemente en $`Y`$.

Para series: si para cada $`y\in Y`$ la sucesión $`a_n(y)`$ es monótona en $`n`$ y $`a_n(y)\rightrightarrows0`$ en $`Y`$, y las sumas parciales $`B_n(y):=\sum_{k=1}^{n}b_k(y)`$ están uniformemente acotadas ($`\exists C>0:\ |B_n(y)|\le C`$ para todo $`n\in\mathbb N`$, $`y\in Y`$), entonces la serie $`\sum_{n=1}^{\infty}a_n(y)b_n(y)`$ converge uniformemente en $`Y`$.

> **Corrección de la fuente** (T280). En los apuntes: «1) $`f(x,y)\to0`$ uniformemente en $`Y`$» y para la serie «1) $`a_n(y)\to0`$ uniformemente en $`Y`$», sin monotonía, y las sumas parciales de la serie se escriben «$`b_n(y):=\sum b_k(g)`$; $`\exists C>0: |b_n(y)|\le C`$». La demostración usa la monotonía de $`f`$ respecto de $`x`$ (el [segundo teorema del valor medio](lecture-43-44.md#thm-4-3-1); en los propios apuntes, «$`f(x,y)\downarrow0`$ uniformemente en $`Y`$»), y en la diapositiva FS p86 la condición figura como «$`f(x,y)\searrow0`$ uniformemente en $`Y`$», «$`a_n(y)\searrow0`$ uniformemente en $`Y`$». Se añade la monotonía (sirve cualquier sentido de monotonía); las sumas parciales son $`B_n(y)=\sum_{k=1}^{n}b_k(y)`$.

**Demostración** (para la integral). Usemos el criterio de Bolzano–Cauchy de convergencia uniforme de una integral impropia. Para ello estimemos, para $`a\le t_1<t_2<b`$, la integral $`\left|\int_{t_1}^{t_2}f(x,y)g(x,y)\,dx\right|`$.

Recordemos el segundo teorema del valor medio ([teorema 4.4.3](lecture-45-46.md#thm-4-4-3), Bonnet): si $`\varphi\in C([\alpha,\beta])`$, $`\psi\in C^1([\alpha,\beta])`$ y $`\psi`$ es monótona en $`[\alpha,\beta]`$, existe $`\xi\in[\alpha,\beta]`$ tal que
```math
\int_\alpha^\beta\varphi\psi=\psi(\alpha)\int_\alpha^\xi\varphi+\psi(\beta)\int_\xi^\beta\varphi .
```
La fórmula sigue siendo válida si $`\varphi`$ es integrable en $`[\alpha,\beta]`$ y $`\psi`$ es solo monótona en $`[\alpha,\beta]`$. (El segundo teorema del valor medio tiene también otras formulaciones.)

> **Corrección de la fuente** (M283). En los apuntes: «$`\int_a^bf\cdot\hat g=\hat g(a)\int_a^bf+\hat g(b)\int_c^bf`$». En el primer sumando la integral se toma sobre $`[a,c]`$, y no sobre $`[a,b]`$ ([teorema 4.4.3](lecture-45-46.md#thm-4-4-3); de lo contrario, para $`\hat g\equiv1`$ se obtendría $`\int_a^bf=\int_a^bf+\int_c^bf`$).

Apliquémoslo, para $`y\in Y`$ fijo, a $`\varphi=g(\cdot,y)`$ y a la función monótona $`\psi=f(\cdot,y)`$ en el segmento $`[t_1,t_2]`$: existe $`\xi\in[t_1,t_2]`$ tal que
```math
\left|\int_{t_1}^{t_2}f(x,y)g(x,y)\,dx\right|=\left|f(t_1,y)\int_{t_1}^{\xi}g(x,y)\,dx+f(t_2,y)\int_{\xi}^{t_2}g(x,y)\,dx\right|\le|f(t_1,y)|\left|\int_{t_1}^{\xi}g(x,y)\,dx\right|+|f(t_2,y)|\left|\int_{\xi}^{t_2}g(x,y)\,dx\right| .
```

<a id="p062"></a>

Por la condición 2
```math
\left|\int_{t_1}^{\xi}g(x,y)\,dx\right|=|G(\xi,y)-G(t_1,y)|\le|G(\xi,y)|+|G(t_1,y)|\le C+C=2C,
```
```math
\left|\int_{\xi}^{t_2}g(x,y)\,dx\right|=|G(t_2,y)-G(\xi,y)|\le|G(t_2,y)|+|G(\xi,y)|\le C+C=2C .
```
En consecuencia,
```math
\left|\int_{t_1}^{t_2}f(x,y)g(x,y)\,dx\right|\le2C\bigl(|f(t_1,y)|+|f(t_2,y)|\bigr).
```

> **Corrección de la fuente** (M289). En los apuntes: «$`\left|\int_{n_1}^{n_2}f(x,y)g(x,y)\,dx\right|<2C\cdot\left[|f(n_1,y)|+f(n_2,y)\right]`$». Al segundo sumando le falta el valor absoluto ($`f`$ puede ser negativa), y de las estimaciones con «$`\le`$» se deduce una desigualdad no estricta.

Fijemos $`\varepsilon>0`$. Como $`f(x,y)\rightrightarrows0`$ en $`Y`$ cuando $`x\to b`$, existe $`\eta\in[a,b)`$ tal que $`|f(x,y)|<\frac{\varepsilon}{4C}`$ para todo $`x\in[\eta,b)`$ y $`y\in Y`$. Sea $`\eta<t_1<t_2<b`$ (sin pérdida de generalidad $`a\le\eta<t_1<t_2<b`$). Entonces, para todo $`y\in Y`$
```math
\left|\int_{t_1}^{t_2}f(x,y)g(x,y)\,dx\right|\le2C\bigl(|f(t_1,y)|+|f(t_2,y)|\bigr)<2C\left[\frac{\varepsilon}{4C}+\frac{\varepsilon}{4C}\right]=\varepsilon .
```
Así, para todo $`\varepsilon>0`$ existe $`\eta\in[a,b)`$ tal que para todos $`t_1,t_2`$ con $`\eta<t_1<t_2<b`$ y todo $`y\in Y`$ se cumple $`\left|\int_{t_1}^{t_2}f(x,y)g(x,y)\,dx\right|<\varepsilon`$. Por el criterio de Bolzano–Cauchy la integral converge uniformemente en $`Y`$. $`\square`$

### Criterio de Abel

Sean las funciones $`f`$ y $`g`$ definidas en $`[a,b)\times Y`$, continuas respecto de $`x`$ para cada $`y\in Y`$, y supongamos que

1. para cada $`y\in Y`$ la función $`f(\cdot,y)`$ es monótona en $`[a,b)`$, y $`f`$ está uniformemente acotada: existe $`M>0`$ tal que $`|f(x,y)|\le M`$ para todo $`x\in[a,b)`$ y $`y\in Y`$;
2. la integral $`\int_a^bg(x,y)\,dx`$ converge uniformemente en $`Y`$.

Entonces la integral $`\int_a^bf(x,y)g(x,y)\,dx`$ converge uniformemente en $`Y`$.

Para series: si para cada $`y\in Y`$ la sucesión $`a_n(y)`$ es monótona en $`n`$, la sucesión de funciones $`a_n`$ está uniformemente acotada en $`Y`$ y la serie $`\sum_{n=1}^{\infty}b_n(y)`$ converge uniformemente en $`Y`$, entonces la serie $`\sum_{n=1}^{\infty}a_n(y)b_n(y)`$ converge uniformemente en $`Y`$ (lecciones 73–74).

> **Corrección de la fuente** (T291). En la parte «Integral» de los apuntes la conclusión se escribe igual que para la serie: «$`\Rightarrow\sum a_n(y)b_n(y)`$ conv. uniformemente en $`Y`$». Para la integral la conclusión es la convergencia uniforme de la integral $`\int_a^bf(x,y)g(x,y)\,dx`$ (diapositiva FS p86).

<a id="p063"></a>

**Observación.** A diferencia del criterio de Dirichlet, aquí no se exige que $`f(x,y)\to0`$. Bastan la monotonía y la acotación uniforme de $`f`$, y toda la «convergencia» la proporciona la convergencia uniforme de la integral de $`g`$.

**Demostración** (para la integral). Usemos el criterio de Bolzano–Cauchy de convergencia uniforme de una integral impropia. Por la condición 1 la función $`f`$ está uniformemente acotada: $`|f(x,y)|\le M`$. Fijemos $`\varepsilon>0`$. Como $`\int_a^bg(x,y)\,dx`$ converge uniformemente en $`Y`$, por el criterio de Bolzano–Cauchy existe $`\eta\in[a,b)`$ tal que para todos $`s_1,s_2\in(\eta,b)`$ y todo $`y\in Y`$ se cumple
```math
\left|\int_{s_1}^{s_2}g(x,y)\,dx\right|<\frac{\varepsilon}{2M} .
```
Sean $`\eta<t_1<t_2<b`$ y $`y\in Y`$. Como la función $`f(\cdot,y)`$ es monótona, a la integral sobre $`[t_1,t_2]`$ se le aplica el segundo teorema del valor medio: existe $`\xi\in[t_1,t_2]`$ tal que
```math
\begin{aligned}
\left|\int_{t_1}^{t_2}f(x,y)g(x,y)\,dx\right|&=\left|f(t_1,y)\int_{t_1}^{\xi}g(x,y)\,dx+f(t_2,y)\int_{\xi}^{t_2}g(x,y)\,dx\right|\\
&\le|f(t_1,y)|\cdot\left|\int_{t_1}^{\xi}g(x,y)\,dx\right|+|f(t_2,y)|\cdot\left|\int_{\xi}^{t_2}g(x,y)\,dx\right|<M\cdot\frac{\varepsilon}{2M}+M\cdot\frac{\varepsilon}{2M}=\varepsilon
\end{aligned}
```
(los puntos $`t_1,\xi,t_2`$ están en $`(\eta,b)`$, por lo que ambas integrales de $`g`$ tienen valor absoluto menor que $`\frac{\varepsilon}{2M}`$).

> **Corrección de la fuente** (T296). En los apuntes, en el segundo sumando de la primera línea figura «$`f(n_1,y)\int_\xi^{n_2}g(x,y)\,dx`$». Por el segundo teorema del valor medio, junto a $`\int_\xi^{t_2}`$ va el valor de $`f`$ en el extremo derecho, $`f(t_2,y)`$ (en la línea siguiente de los apuntes así se escribe).

Así, para todo $`\varepsilon>0`$ existe $`\eta\in[a,b)`$ tal que para todos $`t_1,t_2`$ con $`a\le\eta<t_1<t_2<b`$ y todo $`y\in Y`$
```math
\left|\int_{t_1}^{t_2}f(x,y)g(x,y)\,dx\right|<\varepsilon ,
```
es decir, se cumple la condición del criterio de Bolzano–Cauchy, y la integral converge uniformemente en $`Y`$. $`\square`$

<a id="p064"></a>

### Ejemplos

**Ejemplo 1.** Consideremos la integral
```math
I_1(y)=\int_0^{+\infty}\frac{\sin x}{x}\,e^{-xy}\,dx .
```
Converge para $`y\ge0`$. ¿Converge $`I_1(y)`$ uniformemente en $`Y=[0,+\infty)`$? Sí: apliquemos el criterio de Abel a $`f(x,y)=e^{-xy}`$ y $`g(x,y)=\frac{\sin x}{x}`$ (para $`x=0`$ prolongamos $`g`$ con el valor uno):

1. para cada $`y\ge0`$ la función $`f(\cdot,y)=e^{-xy}`$ es monótona (no creciente) respecto de $`x`$;
2. $`|f(x,y)|\le1`$ para todo $`x\ge0`$, $`y\ge0`$;
3. la integral $`\int_0^{\infty}\frac{\sin x}{x}\,dx`$ converge y, como $`g`$ no depende de $`y`$, converge uniformemente en $`Y`$.

En consecuencia, $`I_1(y)`$ converge uniformemente en $`[0,+\infty)`$ por el criterio de Abel.

> **Corrección de la fuente** (T298). En los apuntes, para $`g`$ se repite la línea de $`f`$: «$`g(x,y)=\frac{\sin x}{x}`$, entonces $`\forall y_0>0`$, $`f(x,y)\downarrow0`$ $`(x\to+\infty)`$». Para el criterio de Abel, $`f`$ debe ser monótona respecto de $`x`$ y estar uniformemente acotada (para $`y=0`$ la función $`f\equiv1`$ no tiende a cero, por lo que en $`[0,+\infty)`$ se aplica el criterio de Abel y no el de Dirichlet), y $`g`$ debe tener integral uniformemente convergente, es decir, aquí la convergencia de $`\int_0^\infty\frac{\sin x}{x}\,dx`$ (punto 3 de los apuntes).

**Ejemplo 2.** Consideremos la integral
```math
I_2(\alpha)=\int_1^{+\infty}\frac{\sin x}{x^{\alpha}}\,dx .
```
Para $`\alpha\le0`$ diverge. Probemos que para todo $`\alpha_0>0`$ converge uniformemente en $`[\alpha_0,+\infty)`$. Apliquemos el criterio de Dirichlet a $`f(x,\alpha)=x^{-\alpha}`$ y $`g(x,\alpha)=\sin x`$:

1. para cada $`\alpha\ge\alpha_0`$ la función $`x^{-\alpha}`$ es decreciente en $`[1,+\infty)`$, y $`0<x^{-\alpha}\le x^{-\alpha_0}\to0`$ para $`x\to+\infty`$, es decir, $`x^{-\alpha}\rightrightarrows0`$ en $`[\alpha_0,+\infty)`$;
2. $`|G(t,\alpha)|=\left|\int_1^t\sin x\,dx\right|=\left|-\cos x\,\Big|_1^t\right|=|\cos1-\cos t|\le2`$.

Se cumplen las condiciones del criterio de Dirichlet de convergencia uniforme de una integral impropia dependiente de un parámetro; por tanto, $`I_2(\alpha)`$ converge uniformemente en $`[\alpha_0,+\infty)`$.

> **Corrección de la fuente** (A299, A300, T301). En los apuntes: «$`I_2(\alpha)=\int_0^{+\infty}\frac{\sin x}{x^\alpha}\,dx`$, $`\alpha<0`$ — no definida», «Probemos la conv. uniforme en $`[x_0,+\infty)`$ ($`x_0>0`$)», «$`x^{-\alpha}\downarrow0`$ ($`\forall x>x_0`$)», «$`|G(t,\alpha)|=\left|\int_0^t\sin x\,dx\right|=\dots=|-\cos t+\cos1|\le2`$». La expresión final $`|\cos1-\cos t|`$ corresponde a la integral $`\int_1^t\sin x\,dx`$, y aquí no puede considerarse la integral sobre $`[0,+\infty)`$: para $`\alpha\ge2`$ diverge en cero ($`\frac{\sin x}{x^\alpha}\sim x^{1-\alpha}`$), y la función $`x^{-\alpha}`$ no está acotada cerca de cero. Por eso la integral se toma sobre $`[1,+\infty)`$ (la convergencia uniforme la determina el comportamiento cerca del punto singular $`+\infty`$), y el conjunto de parámetros es $`[\alpha_0,+\infty)`$, $`\alpha_0>0`$: en él $`x^{-\alpha}\le x^{-\alpha_0}`$, lo que da la tendencia uniforme a cero; para $`\alpha\le0`$ la integral diverge («no definida»).

**Observación.** 1) De modo análogo se define y se estudia una integral impropia $`I(y)=\int_{\to a}^{b}f(x,y)\,dx`$ con singularidad en el límite inferior ($`a=-\infty`$, o $`f`$ no acotada cerca de $`a`$). 2) Una integral $`I(y)=\int_{\to a}^{\to b}f(x,y)\,dx`$ con singularidades en ambos extremos se define como la suma $`I(y)=I_1(y)+I_2(y)`$, donde $`I_1(y)=\int_{\to a}^{c}f(x,y)\,dx`$, $`I_2(y)=\int_{c}^{\to b}f(x,y)\,dx`$, $`c\in(a,b)`$.

<a id="p065"></a>

Tal integral se estudia por partes: converge (uniformemente en $`Y`$) si convergen a la vez (uniformemente en $`Y`$) $`I_1`$ y $`I_2`$. La convergencia y el valor de $`I(y)`$ no dependen de la elección del punto $`c\in(a,b)`$, es decir, la definición es correcta.

> **Restaurado** (según las notas a las diapositivas del curso 2024/25, FS p86; la transcripción del final de la observación en el cuaderno es ilegible). En la transcripción: «2) $`I(y)=\int_a^bf(x,y)\,dx`$ la fn se define y se estudia de otro modo según la elección de la aplicación», «A la vez tomando $`I_1`$, y para $`I_2`$». En las notas de 2024/25: «$`\int_{\to a}^{\to b}f(x,y)\,dx=\int_{\to a}^{c}f(x,y)\,dx+\int_{c}^{\to b}f(x,y)\,dx`$, donde $`c\in(a,b)`$; puede probarse que el valor de $`\int_{\to a}^{\to b}f(x,y)\,dx`$ no depende de la elección de $`c\in(a,b)`$».

### Continuidad de una integral impropia respecto de un parámetro

<a id="thm-9-2-1"></a>**Teorema 9.2.1.** Sean la función $`f`$ continua en $`[a,b)\times[c,d]`$, $`y_0\in[c,d]`$, y la integral impropia $`I(y)=\int_a^bf(x,y)\,dx`$ uniformemente convergente en $`[c,d]\cap(y_0-\delta_0,y_0+\delta_0)`$ para algún $`\delta_0>0`$, es decir, en algún entorno del punto $`y_0`$. Entonces la función $`I`$ es continua en el punto $`y_0`$. En particular, si $`I(y)`$ converge uniformemente en $`[c,d]`$, entonces $`I\in C([c,d])`$.

> **Corrección de la fuente** (M526). En los apuntes: «[Sea] $`f(x,y)`$ integr. respecto de $`x`$ unif. $`y_0`$»; en la diapositiva FS p87: «Sea la función $`f(x,y)`$ continua respecto de $`y`$ en el punto $`y_0`$». La continuidad respecto de $`y`$ en un solo punto no basta ni siquiera para una integral propia: la demostración necesita la continuidad de la integral $`\int_a^\eta f(x,y)\,dx`$ en el punto $`y_0`$, que da el [teorema 9.1.1](lecture-75-76.md#thm-9-1-1) para una función continua en un rectángulo. Se añade la condición estándar: $`f`$ es continua en $`[a,b)\times[c,d]`$.

### Derivación de una integral impropia respecto de un parámetro

<a id="thm-9-2-2"></a>**Teorema 9.2.2.** Supongamos que se cumplen las condiciones siguientes:

1. las funciones $`f(x,y)`$ y $`f'_y(x,y)`$ son continuas en $`[a,b)\times[c,d]`$;
2. la integral $`\int_a^bf'_y(x,y)\,dx`$ converge uniformemente en $`[c,d]`$;
3. la integral $`I(y)=\int_a^bf(x,y)\,dx`$ converge al menos para un valor $`y_0\in[c,d]`$.

Entonces $`I(y)`$ converge uniformemente en todo el segmento $`[c,d]`$, la función $`I`$ es derivable en $`[c,d]`$ y se cumple la igualdad
```math
I'(y)=\left(\int_a^bf(x,y)\,dx\right)'_y=\int_a^bf'_y(x,y)\,dx .
```

> **Corrección de la fuente** (M527). En los apuntes (y en la diapositiva FS p87): «1) las fns $`f(x,y)`$ y $`f'_y(x,y)`$ integr. [continuas] respecto de $`x`$», y el conjunto de parámetros es un $`Y`$ arbitrario. La continuidad respecto de $`x`$ no basta (ya para integrales propias, en el [teorema 9.1.2](lecture-75-76.md#thm-9-1-2), $`f`$ y $`f'_y`$ son continuas en un rectángulo); la condición 1 se sustituye por la estándar. El conjunto de parámetros se toma como un segmento: en un conjunto no acotado la conclusión sobre la convergencia uniforme de $`I`$ puede ser falsa (por ejemplo, $`f(x,y)=ye^{-x}`$ en $`[0,+\infty)\times\mathbb R`$: $`\int_0^\infty f'_y\,dx=\int_0^\infty e^{-x}\,dx`$ converge uniformemente, pero $`\int_t^{\infty}ye^{-x}\,dx=ye^{-t}`$ no es pequeña uniformemente en $`y\in\mathbb R`$). Como la derivabilidad es una propiedad local, en un intervalo arbitrario $`Y`$ el teorema se aplica en cada segmento $`[c,d]\subset Y`$.

### Integración de una integral impropia respecto de un parámetro

<a id="thm-9-2-3"></a>**Teorema 9.2.3.** Supongamos que se cumplen las condiciones siguientes:

1. la función $`f(x,y)`$ es continua en $`[a,b)\times[c,d]`$;
2. la integral $`I(y)=\int_a^bf(x,y)\,dx`$ converge uniformemente en $`Y=[c,d]`$.

Entonces $`I`$ es integrable en $`[c,d]`$, la integral impropia del miembro derecho de la igualdad siguiente converge y se cumple
```math
\int_c^dI(y)\,dy=\int_a^b\left(\int_c^df(x,y)\,dy\right)dx .
```

> **Corrección de la fuente** (T307, M528). En los apuntes: «$`\int_c^dI(y)\,dy=\int_c^d\left(\int_a^bf(x,y)\,dy\right)dx`$»: los límites de integración están intercambiados; la integral interior se toma respecto de $`y`$ de $`c`$ a $`d`$, y la exterior (impropia), respecto de $`x`$ de $`a`$ a $`b`$ (diapositiva FS p87). La condición 1 en los apuntes y en la diapositiva es «$`f(x,y)`$ continua respecto de $`x`$»; como en el [teorema 9.2.1](#thm-9-2-1), hace falta la continuidad de $`f`$ en $`[a,b)\times[c,d]`$ (garantiza la continuidad de $`I`$ y la aplicabilidad del [teorema 9.1.3](#thm-9-1-3) en los rectángulos $`[a,t]\times[c,d]`$).

### Demostraciones de los teoremas 9.2.1–9.2.3

**Demostración del [teorema 9.2.1](#thm-9-2-1) (idea).** La demostración se basa en dos pasos.

1) Por la convergencia uniforme, para todo $`\varepsilon>0`$ existe $`\eta\in[a,b)`$, independiente de $`y`$, tal que $`\sup_{y}\left|\int_\eta^bf(x,y)\,dx\right|<\varepsilon`$, donde el [supremo](lecture-11-12.md#def-2-3-1) se toma sobre $`y`$ en un entorno del punto $`y_0`$.

2) El incremento de la integral se estima mediante una integral propia sobre $`[a,\eta]`$ y dos «colas»:
```math
|I(y_0+\Delta y)-I(y_0)|\le\left|\int_a^{\eta}\bigl[f(x,y_0+\Delta y)-f(x,y_0)\bigr]dx\right|+\left|\int_\eta^bf(x,y_0+\Delta y)\,dx\right|+\left|\int_\eta^bf(x,y_0)\,dx\right| .
```

<a id="p066"></a>

Fijado $`\varepsilon`$, hallamos $`\eta`$ y después $`\delta`$: la suma de las dos «colas» es menor que $`2\varepsilon`$, y la integral propia sobre $`[a,\eta]`$ es pequeña para $`|\Delta y|`$ pequeños.

> **Restaurado** (según la demostración estándar, cf. Fichtenholz, t. II, cap. XIV; Zorich, t. II, cap. XVII; en los apuntes solo se anota la idea, y los [teoremas 9.2.2](#thm-9-2-2) y [9.2.3](#thm-9-2-3) se dan sin demostración).
>
> **Demostración del [teorema 9.2.1](#thm-9-2-1).** Sea $`\varepsilon>0`$. El conjunto $`K=[c,d]\cap\left[y_0-\frac{\delta_0}2,\,y_0+\frac{\delta_0}2\right]`$ es un segmento que contiene a $`y_0`$ y está contenido en el entorno de la hipótesis. Por la [definición 9.2.1](#def-9-2-1) existe $`\eta\in[a,b)`$ tal que $`\left|\int_\eta^bf(x,y)\,dx\right|<\varepsilon`$ para todo $`y\in K`$. La función $`f`$ es continua en el rectángulo $`[a,\eta]\times K`$, por lo que, por el [teorema 9.1.1](lecture-75-76.md#thm-9-1-1), la integral propia $`J(y)=\int_a^\eta f(x,y)\,dx`$ es continua en $`K`$, y existe $`\delta\in\left(0,\frac{\delta_0}2\right]`$ tal que $`|J(y)-J(y_0)|<\varepsilon`$ para $`y\in[c,d]`$, $`|y-y_0|<\delta`$ (tales $`y`$ están en $`K`$). Para esos $`y`$
> ```math
> |I(y)-I(y_0)|\le|J(y)-J(y_0)|+\left|\int_\eta^bf(x,y)\,dx\right|+\left|\int_\eta^bf(x,y_0)\,dx\right|<\varepsilon+\varepsilon+\varepsilon=3\varepsilon .
> ```
> Como $`\varepsilon>0`$ es arbitrario, $`I`$ es [continua en el punto](lecture-16.md#def-2-5-1) $`y_0`$. $`\square`$
>
> **Demostración del [teorema 9.2.3](#thm-9-2-3).** La hipótesis del [teorema 9.2.1](#thm-9-2-1) se cumple en cada punto $`y_0\in[c,d]`$, por lo que $`I\in C([c,d])`$; en particular, $`I`$ es integrable en $`[c,d]`$. Sea $`t\in[a,b)`$. La función $`f`$ es continua en el rectángulo $`[a,t]\times[c,d]`$, y por el [teorema 9.1.3](#thm-9-1-3)
> ```math
> \int_a^t\left(\int_c^df(x,y)\,dy\right)dx=\int_c^d\left(\int_a^tf(x,y)\,dx\right)dy=\int_c^dI_t(y)\,dy .
> ```
> Sean $`\varepsilon>0`$ y $`b_0`$ el de la [definición 9.2.1](#def-9-2-1). Para $`t\in(b_0,b)`$
> ```math
> \left|\int_c^dI(y)\,dy-\int_a^t\left(\int_c^df(x,y)\,dy\right)dx\right|=\left|\int_c^d\bigl(I(y)-I_t(y)\bigr)dy\right|\le\int_c^d\left|\int_t^bf(x,y)\,dx\right|dy\le\varepsilon(d-c) .
> ```
> En consecuencia, $`\lim_{t\to b}\int_a^t\left(\int_c^df(x,y)\,dy\right)dx=\int_c^dI(y)\,dy`$: la integral impropia del miembro derecho converge, y la igualdad queda probada. $`\square`$
>
> **Demostración del [teorema 9.2.2](#thm-9-2-2).** Para $`t\in[a,b)`$ pongamos
> ```math
> I_t(y)=\int_a^tf(x,y)\,dx,\qquad J_t(y)=\int_a^tf'_y(x,y)\,dx,\qquad J(y)=\int_a^bf'_y(x,y)\,dx .
> ```
> Las funciones $`f`$ y $`f'_y`$ son continuas en el rectángulo $`[a,t]\times[c,d]`$, por lo que, por el [teorema 9.1.2](lecture-75-76.md#thm-9-1-2), $`I_t\in C^1([c,d])`$ y $`I_t'=J_t`$, y por la [fórmula de Newton–Leibniz](lecture-43-44.md#thm-4-3-2)
> ```math
> I_t(y)=I_t(y_0)+\int_{y_0}^{y}J_t(s)\,ds,\qquad y\in[c,d].\qquad(*)
> ```
> *Convergencia uniforme de $`I`$.* Sea $`\varepsilon>0`$. Como la integral $`I(y_0)`$ converge y $`\int_a^bf'_y(x,y)\,dx`$ converge uniformemente en $`[c,d]`$, por el criterio de Bolzano–Cauchy existe $`b_0\in[a,b)`$ tal que para todos $`t_1,t_2\in(b_0,b)`$ y $`s\in[c,d]`$
> ```math
> \left|\int_{t_1}^{t_2}f(x,y_0)\,dx\right|<\varepsilon,\qquad\left|\int_{t_1}^{t_2}f'_y(x,s)\,dx\right|<\varepsilon .
> ```
> Restando las igualdades $`(*)`$ para $`t=t_2`$ y $`t=t_1`$, obtenemos para todo $`y\in[c,d]`$
> ```math
> \left|\int_{t_1}^{t_2}f(x,y)\,dx\right|\le\left|\int_{t_1}^{t_2}f(x,y_0)\,dx\right|+\left|\int_{y_0}^{y}\left(\int_{t_1}^{t_2}f'_y(x,s)\,dx\right)ds\right|<\varepsilon+\varepsilon|y-y_0|\le\varepsilon(1+d-c) .
> ```
> Por el criterio de Bolzano–Cauchy $`I(y)`$ converge uniformemente en $`[c,d]`$.
>
> *La fórmula de la derivada.* Por el [teorema 9.2.1](#thm-9-2-1) (aplicado a $`f'_y`$) la función $`J`$ es continua en $`[c,d]`$. Como $`J_t\rightrightarrows J`$ en $`[c,d]`$ cuando $`t\to b`$,
> ```math
> \left|\int_{y_0}^{y}J_t(s)\,ds-\int_{y_0}^{y}J(s)\,ds\right|\le(d-c)\sup_{s\in[c,d]}|J_t(s)-J(s)|\to0\qquad(t\to b) .
> ```
> Pasando al límite en $`(*)`$ cuando $`t\to b`$, obtenemos $`I(y)=I(y_0)+\int_{y_0}^{y}J(s)\,ds`$ para todo $`y\in[c,d]`$. La integral con límite superior variable de la función continua $`J`$ es derivable (teorema de Barrow), por lo que $`I`$ es derivable en $`[c,d]`$ y $`I'(y)=J(y)=\int_a^bf'_y(x,y)\,dx`$. $`\square`$

### Método de Feynman

En el [teorema 9.2.2](#thm-9-2-2) se basa la idea de calcular integrales pasando a una integral con parámetro, el método de Feynman: la integral se incluye en una familia de integrales dependientes de un parámetro y se deriva respecto del parámetro bajo el signo integral.

**Ejemplo.** Calculemos
```math
\int_0^\infty\frac{e^{-x}-e^{-2x}}{x}\,dx .
```
Consideremos
```math
I(\alpha)=\int_0^\infty\frac{e^{-x}-e^{-\alpha x}}{x}\,dx ,\qquad\alpha\in Y=[1,2] ;
```
la integral buscada es $`I(2)`$, y $`I(1)=0`$. El integrando $`f(x,\alpha)=\frac{e^{-x}-e^{-\alpha x}}{x}`$ tiene límite finito $`\alpha-1`$ cuando $`x\to0`$; definiendo $`f(0,\alpha)=\alpha-1`$, obtenemos una función continua en $`[0,+\infty)\times[1,2]`$ junto con su derivada
```math
\frac{\partial f}{\partial\alpha}(x,\alpha)=e^{-\alpha x}
```
(para $`x=0`$ ambas fórmulas dan $`1`$). Comprobemos las hipótesis del [teorema 9.2.2](#thm-9-2-2):

1. $`f`$ y $`\frac{\partial f}{\partial\alpha}`$ son continuas en $`[0,+\infty)\times[1,2]`$;
2. la integral $`\int_0^\infty e^{-\alpha x}\,dx`$ converge uniformemente en $`[1,2]`$ por el criterio de Weierstrass: $`0<e^{-\alpha x}\le e^{-x}`$ para $`x\ge0`$, $`\alpha\ge1`$, y $`\int_0^\infty e^{-x}\,dx=1`$ converge;
3. la integral $`I(1)=0`$ converge.

En consecuencia, para $`\alpha\in[1,2]`$
```math
I'(\alpha)=\int_0^\infty\frac{\partial f}{\partial\alpha}\,dx=\int_0^\infty e^{-\alpha x}\,dx=\frac{e^{-\alpha x}}{-\alpha}\Big|_0^{\infty}=\frac1\alpha ,
```
de donde $`I(\alpha)=\int\frac{d\alpha}{\alpha}+C=\ln|\alpha|+C=\ln\alpha+C`$. Como $`I(1)=0`$, se tiene $`C=0`$, y
```math
\int_0^\infty\frac{e^{-x}-e^{-2x}}{x}\,dx=I(2)=\ln2 .
```

> **Corrección de la fuente** (S313, T314, U315, T316, M317, T318, T529). En los apuntes la convergencia de $`I(\alpha)`$ se comprueba mediante la división «$`I_1+I_2(\alpha)`$: $`I_2(\alpha)=\int_0^\infty\frac{e^{\alpha x}}{x}\,dx`$» con la estimación «$`|f(\alpha,x)|\le\frac{e^{\alpha x}+e^{-x}}{x}\le\frac{?}{x}=g(x)`$» y la afirmación «$`\int_0^\infty\frac{e^{-x}}{x}\,dx`$ — conv.». Esto es incorrecto: $`\frac{e^{-x}}{x}\sim\frac1x`$ cuando $`x\to0+`$, de modo que las integrales $`\int_0^\infty\frac{e^{-x}}{x}\,dx`$ y $`\int_0^\infty\frac{e^{-\alpha x}}{x}\,dx`$ divergen (además, en el exponente $`e^{\alpha x}`$ falta un signo menos), y una mayorante de la forma $`\frac{C}{x}`$ no es integrable ni cerca de cero ni en el infinito. No hace falta dividir la integral: la singularidad en cero es evitable, y la condición 3 del [teorema 9.2.2](#thm-9-2-2) exige convergencia solo en un punto ($`I(1)=0`$); la convergencia uniforme de $`I(\alpha)`$ en $`[1,2]`$ es ya una conclusión del teorema. Las líneas «$`I_2e^{-x}\,dx=e^{-\alpha x}\,dx`$» y «$`\int_0^\infty e^{-x}\,dx<\int_0^\infty e^{-x}\,dx\Rightarrow`$ es conv. uniforme» se leen como la mayorante $`e^{-\alpha x}\le e^{-x}`$ ($`\alpha\ge1`$) y la convergencia de $`\int_0^\infty e^{-x}\,dx`$, que dan la convergencia uniforme de la integral de $`\frac{\partial f}{\partial\alpha}`$ (condición 2). Por último, en los apuntes figura «$`\frac{df}{d\alpha}=-e^{-\alpha x}`$»; lo correcto es $`\frac{\partial f}{\partial\alpha}=+e^{-\alpha x}`$ (en la línea siguiente de los apuntes se usa precisamente $`\int_0^\infty e^{-\alpha x}\,dx=\frac1\alpha`$).

**Ejercicio (método de Feynman).** Calcular explícitamente
```math
I(a)=\int_0^{\infty}\frac{dx}{(a^2+x^2)^2},\qquad a>0 ,
```
apoyándose en la integral
```math
\int_0^{+\infty}\frac{dx}{a^2+x^2}=\frac1a\arctan\frac xa\,\Big|_0^{+\infty}=\frac{\pi}{2a} .
```
Idea: $`\left(\frac1{a^2+x^2}\right)'_a=-\frac{2a}{(a^2+x^2)^2}`$, y derivar respecto del parámetro bajo el signo integral está permitido para $`a\in[a_0,+\infty)`$, $`a_0>0`$.

> **Corrección de la fuente** (U319, T320, S321). En los apuntes: «$`\int_0^\infty\frac{dx}{(a+x^2)^2}=I(a)`$ — deducir la forma explícita», «$`\left(\frac1{a+x^2}\right)'_a=2a-\frac1{(a+x^2)^2}`$», «$`\alpha\in[0,+\infty)`$, $`a_0>0`$: idea», «Apoyándose en $`\int_0^{+\infty}\frac{dx}{a^2+x^2}`$». Como la integral de referencia contiene $`a^2`$ (y el factor $`2a`$ aparece al derivar $`\frac1{a^2+x^2}`$), el ejercicio tiene $`(a^2+x^2)^2`$, y la derivada vale $`-\frac{2a}{(a^2+x^2)^2}`$; el parámetro es $`a\in[a_0,+\infty)`$, $`a_0>0`$ (para $`a=0`$ la integral diverge).

> **Restaurado** (solución del ejercicio; en los apuntes el ejercicio solo se plantea). Sea $`0<a_0<a_1`$. En $`[0,+\infty)\times[a_0,a_1]`$ las funciones $`\frac1{a^2+x^2}`$ y $`-\frac{2a}{(a^2+x^2)^2}`$ son continuas y, como $`(a^2+x^2)^2\ge a^2(a^2+x^2)`$,
> ```math
> \frac{2a}{(a^2+x^2)^2}\le\frac{2}{a(a^2+x^2)}\le\frac{2}{a_0(a_0^2+x^2)},\qquad\int_0^\infty\frac{2\,dx}{a_0(a_0^2+x^2)}=\frac{\pi}{a_0^2}<\infty ,
> ```
> la integral de la derivada converge uniformemente en $`[a_0,a_1]`$ (criterio de Weierstrass). Por el [teorema 9.2.2](#thm-9-2-2)
> ```math
> -\frac{\pi}{2a^2}=\left(\frac{\pi}{2a}\right)'=\int_0^\infty\left(\frac1{a^2+x^2}\right)'_a\,dx=-2a\int_0^\infty\frac{dx}{(a^2+x^2)^2}=-2a\,I(a),
> ```
> de donde $`I(a)=\frac{\pi}{4a^3}`$ para todo $`a>0`$ (ya que $`a_0`$ y $`a_1`$ son arbitrarios). Comprobación: para $`a=1`$ el cambio $`x=\tan u`$ da $`\int_0^{\pi/2}\cos^2u\,du=\frac{\pi}4`$.

## Referencias cruzadas

- Tema en el curso: [capítulo 9 «Integrales impropias y aplicaciones»](../09-improper-integrals-applications.md) — [§9.1 «Definiciones»](../09-improper-integrals-applications.md#sec-9-1), [§9.2 «Criterios de convergencia»](../09-improper-integrals-applications.md#sec-9-2), [el criterio de Dirichlet para integrales](../09-improper-integrals-applications.md#dirichlet-test-for-integrals); el cambio del orden de integración (cf. el [teorema 9.1.3](#thm-9-1-3)) — el [teorema de Fubini para funciones continuas](../17-multiple-integrals.md#fubini-theorem-continuous) del capítulo 17.
- Comienzo del capítulo 9 ([definición 9.1.1](lecture-75-76.md#def-9-1-1), [teoremas 9.1.1](lecture-75-76.md#thm-9-1-1) y [9.1.2](lecture-75-76.md#thm-9-1-2), comienzo del ejemplo de la ecuación de Bessel): [lecciones 75–76](lecture-75-76.md).
- Convergencia uniforme de sucesiones y series funcionales, criterio de Bolzano–Cauchy y criterio de Weierstrass para series — [lecciones 71–72](lecture-71-72.md); criterio de Abel de convergencia uniforme de series — [lecciones 73–74](lecture-73-74.md).
- Hechos usados: el segundo teorema del valor medio — [teorema 4.4.3](lecture-45-46.md#thm-4-4-3) (Bonnet), [lecciones 45–46](lecture-45-46.md); los criterios de Dirichlet y de Abel para integrales impropias sin parámetro — [teoremas 4.5.4](lecture-49-50.md#thm-4-5-4) y [4.5.5](lecture-49-50.md#thm-4-5-5), [lecciones 49–50](lecture-49-50.md).
- Continuación del capítulo 9 (funciones gamma y beta) y comienzo del capítulo 10: [lecciones 79–80](lecture-79-80.md).

---

[← Lecciones 75–76](lecture-75-76.md) · [Índice de lecciones](index.md) · [Lecciones 79–80 →](lecture-79-80.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-77-78.md) · [English](../../en/lectures-2025-26/lecture-77-78.md)

---
title: "Lecciones 41–42 — Clases de funciones integrables y criterio de Lebesgue"
lang: es
course: "Análisis matemático, 2025/26"
lecture: 41-42
semester: 2
date: 2026-03-12
source: "ma25_26-lectures_41-42_notes.pdf"
pdf_pages: 25
typed_slides: 11
---
# Lecciones 41–42 — Clases de funciones integrables

[← Lecciones 39–40](lecture-39-40.md) · [Índice de lecciones](index.md) · [Lecciones 43–44 →](lecture-43-44.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-41-42.md) · [English](../../en/lectures-2025-26/lecture-41-42.md)

> **Fuente:** `ma25_26-lectures_41-42_notes.pdf` — 25 páginas, 11 diapositivas impresas. Páginas manuscritas: 5–6, 8–9, 11, 13–15, 17–18, 22–25. Se incluyen los dibujos y las anotaciones sobre las diapositivas. Fecha: 12 de marzo de 2026. Las siete ilustraciones se han extraído del PDF y comprobado individualmente.
>
> **Semestre 2: lecciones 33–64; el semestre 1 terminó con la lección 32. Existe material duplicado a partir de la lección 33** en la [carpeta rusa `ru/lectures/`](../../ru/lectures/index.md). Esta lección se solapa con [§4.2 «Integral de Riemann»](../../ru/lectures/03-riemann-integral-4-2.md); se conserva la [«Lección 41-42» archivada](../../../source/MathInMind/МАТАН_Л/Лекция%2041-42.md). Aquí se ofrece una transcripción ilustrada completa e independiente del nuevo PDF, incluidas las demostraciones manuscritas.
>
> **Notación.** $`a<b`$; $`\mathcal R[a,b]`$ designa las funciones [integrables según Riemann](lecture-39-40.md#def-4-2-6); $`C[a,b]`$ las funciones continuas; $`\lambda_\tau`$ es la norma de una [partición](lecture-37-38.md#def-4-2-2); $`\omega_k(f)`$ es la [oscilación](lecture-39-40.md#def-4-2-9) en su subintervalo. El criterio mediante sumas de oscilaciones y las definiciones están en las [lecciones 39–40](lecture-39-40.md).

## Diapositivas impresas 1–3 (pp. PDF 1–3). Introducción

**Cita del día:**

> — Tome esta integral.
>
> — No, gracias, no puedo con ella…
>
> — Tómela a crédito, a plazos, con hipoteca si hace falta: es buena.

**Objetivos:** continuar los criterios de integrabilidad; estudiar restricciones y funciones continuas a trozos; definir los conjuntos de [medida nula](#def-4-2-11) y enunciar el [criterio de Lebesgue](#thm-4-2-5); considerar operaciones aritméticas con funciones integrables.

## Capítulo 4, §2. Integral de Riemann — continuación

### Diapositiva impresa 4 (p. PDF 4). Funciones continuas

<a id="thm-4-2-2"></a>**Teorema 4.2.2.** Una función continua en un intervalo cerrado es integrable en él:

```math
C[a,b]\subset\mathcal R[a,b].
```

### Páginas manuscritas (pp. PDF 5–6). Demostración del teorema 4.2.2

Por el [teorema de Heine–Cantor](lecture-17-18.md#thm-2-5-4), $`f`$ es [uniformemente continua](lecture-17-18.md#def-2-5-7) en $`[a,b]`$. Para cada $`\varepsilon>0`$, existe $`\delta>0`$ tal que

```math
x,y\in[a,b],\quad |x-y|<\delta
\quad\Longrightarrow\quad
|f(x)-f(y)|<\frac{\varepsilon}{b-a}.
```

En cualquier subintervalo de longitud menor que $`\delta`$, la oscilación es menor que $`\varepsilon/(b-a)`$: el máximo y el mínimo se alcanzan. Para toda partición con $`\lambda_\tau<\delta`$,

```math
\sum_{k=0}^{n-1}\omega_k(f)\Delta x_k
<\sum_{k=0}^{n-1}\frac{\varepsilon}{b-a}\Delta x_k
=\frac{\varepsilon}{b-a}(b-a)=\varepsilon.
```

El [teorema 4.2.1](lecture-39-40.md#thm-4-2-1) da la integrabilidad. $`\blacksquare`$

### Diapositiva impresa 5 (p. PDF 7). Funciones monótonas

<a id="thm-4-2-3"></a>**Teorema 4.2.3.** Una función monótona en un intervalo cerrado es integrable en él.

### Páginas manuscritas (pp. PDF 8–9). Demostración del teorema 4.2.3

Para fijar ideas, supongamos que $`f`$ no decrece. Entonces $`f(a)\le f(x)\le f(b)`$.

1. Si $`f(a)=f(b)`$, la función es constante, luego continua e integrable por el [teorema 4.2.2](#thm-4-2-2).
2. Si $`f(a)<f(b)`$, dado $`\varepsilon>0`$, ponemos

```math
\delta=\frac{\varepsilon}{f(b)-f(a)}>0.
```

Para toda partición con $`\lambda_\tau<\delta`$, la monotonía da

```math
\omega_k(f)=f(x_{k+1})-f(x_k).
```

Por tanto,

```math
\begin{aligned}
\sum_{k=0}^{n-1}\omega_k(f)\Delta x_k
&\le\lambda_\tau\sum_{k=0}^{n-1}\bigl(f(x_{k+1})-f(x_k)\bigr)\\
&=\lambda_\tau\bigl(f(b)-f(a)\bigr)
<\delta\bigl(f(b)-f(a)\bigr)=\varepsilon.
\end{aligned}
```

La suma de diferencias es telescópica. Se cumple el [criterio de integrabilidad](lecture-39-40.md#thm-4-2-1). Para una función no creciente, la demostración es análoga, invirtiendo las diferencias. $`\blacksquare`$

### Diapositiva impresa 6 (p. PDF 10). Cambio de un número finito de valores

**Observación.** Cambiar los valores de una función integrable en un número finito de puntos conserva tanto su integrabilidad como su integral.

![P. PDF 10: los valores en tres puntos aislados se desplazan respecto al gráfico original](../../assets/lectures-2025-26/lec41-42-p10-finite-changes.jpg)

### Página manuscrita (p. PDF 11). Demostración de la observación

Sea $`f\in\mathcal R[a,b]`$, y sea $`\widetilde f:[a,b]\to\mathbb R`$ distinta de ella solo en $`t_1,\ldots,t_m`$. La acotación de $`f`$ da $`|f|\le A`$, y entonces

```math
|\widetilde f|\le\widetilde A
=\max\{A,|\widetilde f(t_1)|,\ldots,|\widetilde f(t_m)|\}.
```

Para una misma partición etiquetada, pueden diferir como máximo $`2m`$ sumandos: cada punto modificado puede pertenecer a dos subintervalos adyacentes. Por ello,

```math
|\sigma_\tau(f,\xi)-\sigma_\tau(\widetilde f,\xi)|
\le2m(A+\widetilde A)\lambda_\tau
\xrightarrow[\lambda_\tau\to0]{}0.
```

Como las sumas para $`f`$ convergen a su integral, resulta

```math
\lim_{\lambda_\tau\to0}\sigma_\tau(\widetilde f,\xi)
=\int_a^b f,
\qquad
\int_a^b\widetilde f=\int_a^b f.
```

Esto demuestra a la vez la integrabilidad de la función modificada y la igualdad de las integrales. $`\blacksquare`$

> **Corrección del manuscrito.** En la última línea de la p. 11 se indica por error, bajo la flecha, que la norma tiende a infinito. Debe tender a cero. La conclusión rigurosa es que la diferencia de sumas tiende a cero y ambas tienen un mismo límite fijo; la suma variable de la función original no es, por sí misma, un número límite.

### Diapositiva impresa 7 (p. PDF 12). Restricción y unión de intervalos

<a id="thm-4-2-4"></a>**Teorema 4.2.4.**

1. Si $`f\in\mathcal R[a,b]`$ y $`[\alpha,\beta]\subset[a,b]`$, entonces $`f\in\mathcal R[\alpha,\beta]`$.
2. Si $`a<c<b`$ y $`f:[a,b]\to\mathbb R`$ es integrable en $`[a,c]`$ y en $`[c,b]`$, entonces $`f\in\mathcal R[a,b]`$.

![P. PDF 12: selección de un subintervalo con extremos α y β](../../assets/lectures-2025-26/lec41-42-p12-restriction.jpg)

![P. PDF 12: unión de dos partes por su extremo común c](../../assets/lectures-2025-26/lec41-42-p12-gluing.jpg)

> **Alcance del enunciado.** Se trata de la **integrabilidad**, no de la fórmula de aditividad de la integral. La igualdad entre la integral y la suma de las integrales sobre las partes aparece en las [lecciones 43–44](lecture-43-44.md).

### Página manuscrita (p. PDF 13). Demostración de la parte 1

Sean $`\alpha<\beta`$. Dado $`\varepsilon>0`$, elegimos $`\delta>0`$ mediante el criterio de integrabilidad de $`f`$ en $`[a,b]`$. Tomamos **cualquier** partición $`\tau_0`$ de $`[\alpha,\beta]`$ con norma menor que $`\delta`$. Añadimos puntos en las partes exteriores hasta obtener una partición $`\tau`$ de todo el intervalo con $`\lambda_\tau<\delta`$.

![P. PDF 13: partición original del subintervalo en verde y partes exteriores añadidas en rojo](../../assets/lectures-2025-26/lec41-42-p13-extended-partition.jpg)

Todos los términos de una suma de oscilaciones son no negativos. Los términos del subintervalo están incluidos en la suma de la partición completa, de modo que

```math
\sum_{[x_k,x_{k+1}]\subset[\alpha,\beta]}\omega_k(f)\Delta x_k
\le\sum_{k=0}^{n-1}\omega_k(f)\Delta x_k<\varepsilon.
```

El criterio se cumple para todas las particiones suficientemente finas del subintervalo. $`\blacksquare`$

> **Explicación editorial.** Si coinciden los extremos exteriores, se omiten simplemente las partes exteriores vacías. Un subintervalo degenerado queda cubierto por la convención de integral nula introducida en las lecciones 43–44.

### Páginas manuscritas (pp. PDF 14–15). Demostración de la parte 2

La integrabilidad en ambas partes da la acotación en todo el intervalo. Denotemos su oscilación total por $`\omega=\omega(f)_{[a,b]}`$. Si $`\omega=0`$, la función es constante y el resultado ya está demostrado. Supongamos $`\omega>0`$.

Dado $`\varepsilon>0`$, elegimos $`\delta_1,\delta_2>0`$ para que las sumas de oscilaciones en las partes respectivas sean menores que $`\varepsilon/3`$, y ponemos

```math
\delta=\min\left\{\delta_1,\delta_2,\frac{\varepsilon}{3\omega}\right\}.
```

Consideremos cualquier partición $`\tau`$ con $`\lambda_\tau<\delta`$. Si $`c`$ es un nodo, la suma se divide directamente en dos partes. Pero $`c`$ **no tiene por qué** ser un nodo: en tal caso hay un único subintervalo $`[x_\nu,x_{\nu+1}]`$ que lo atraviesa.

![P. PDF 15: el punto de unión c en el interior de un subintervalo de una partición arbitraria](../../assets/lectures-2025-26/lec41-42-p15-crossing-interval.jpg)

La contribución de ese subintervalo es como máximo $`\omega\lambda_\tau`$. Los términos restantes se acotan por las sumas de particiones de ambas partes, obtenidas añadiendo el punto de unión:

```math
\sum_{k=0}^{n-1}\omega_k(f)\Delta x_k
<\frac{\varepsilon}{3}+\frac{\varepsilon}{3}
+\omega\lambda_\tau<\varepsilon.
```

Si el punto de unión ya es un nodo, no hace falta el tercer término. Volvemos a aplicar el criterio de integrabilidad. $`\blacksquare`$

### Diapositiva impresa 8 (p. PDF 16). Funciones continuas a trozos

<a id="def-4-2-10"></a>**Definición 4.2.10.** Una función $`f:[a,b]\to\mathbb R`$ es **continua a trozos** si su conjunto de discontinuidades es vacío o finito y todas sus discontinuidades son de primera especie.

**Corolario (sin número).** Una función continua a trozos en un intervalo cerrado es integrable en él.

### Páginas manuscritas (pp. PDF 17–18). Demostración del corolario y observaciones

Si no hay discontinuidades, aplicamos el [teorema 4.2.2](#thm-4-2-2). En caso contrario, enumeramos los finitos [puntos de discontinuidad](lecture-16.md#def-2-5-4) interiores $`a_1<\cdots<a_m`$, y ponemos $`a_0=a`$, $`a_{m+1}=b`$.

![P. PDF 17: división en un número finito de intervalos de continuidad](../../assets/lectures-2025-26/lec41-42-p17-piecewise-partition.jpg)

En cada intervalo abierto la función es continua y tiene [límites laterales](lecture-15.md#def-2-4-5) finitos en sus extremos. La extendemos continuamente al intervalo cerrado correspondiente:

```math
g_i(x)=
\begin{cases}
f(x),&a_i<x<a_{i+1},\\
f(a_i+0),&x=a_i,\\
f(a_{i+1}-0),&x=a_{i+1},
\end{cases}
\qquad i=0,\ldots,m.
```

Entonces $`g_i\in C[a_i,a_{i+1}]\subset\mathcal R[a_i,a_{i+1}]`$. La función original puede diferir de la extensión en los extremos, pero son como máximo dos puntos; la observación sobre modificaciones finitas da la integrabilidad de la función original en cada parte. Aplicando repetidamente la parte 2 del [teorema 4.2.4](#thm-4-2-4), obtenemos la integrabilidad en todo el intervalo. $`\blacksquare`$

Observación manuscrita: la integrabilidad **no implica** continuidad ni la existencia de solo un número finito de discontinuidades. La inclusión de clases va en un único sentido.

![P. PDF 18: la clase de funciones continuas dentro de la clase de funciones integrables según Riemann](../../assets/lectures-2025-26/lec41-42-p18-continuous-integrable-classes.jpg)

### Diapositiva impresa 9 (p. PDF 19). Conjuntos de medida nula

<a id="def-4-2-11"></a>**Definición 4.2.11.** Un conjunto $`E\subset\mathbb R`$ tiene **medida nula** si, para todo $`\varepsilon>0`$, puede cubrirse con una unión a lo sumo numerable de intervalos abiertos cuya longitud total sea menor que $`\varepsilon`$:

```math
E\subset\bigcup_j(\alpha_j,\beta_j),\qquad
\sum_j(\beta_j-\alpha_j)<\varepsilon.
```

La familia de intervalos de la cubierta puede ser finita o [numerable](lecture-01-02.md#def-1-2-5).

### Diapositiva impresa 10 (p. PDF 20). Criterio de Lebesgue

<a id="thm-4-2-5"></a>**Teorema 4.2.5.** Una función $`f:[a,b]\to\mathbb R`$ es integrable según Riemann si y solo si está acotada en el intervalo y su conjunto de discontinuidades tiene medida nula.

Este PDF enuncia el criterio **sin demostración**. No afirma que una función integrable deba tener un conjunto finito o numerable de discontinuidades: la condición es precisamente la medida nula.

### Diapositiva impresa 11 (p. PDF 21). Operaciones aritméticas

<a id="thm-4-2-6"></a>**Teorema 4.2.6.** Sean $`f,g\in\mathcal R[a,b]`$. Entonces:

1. $`f+g\in\mathcal R[a,b]`$;
2. $`fg\in\mathcal R[a,b]`$;
3. $`\alpha f\in\mathcal R[a,b]`$ para todo $`\alpha\in\mathbb R`$;
4. $`|f|\in\mathcal R[a,b]`$;
5. si $`\inf_{x\in[a,b]}|g(x)|>0`$, entonces $`f/g\in\mathcal R[a,b]`$.

Aquí se establece la estabilidad de la clase de funciones integrables; las fórmulas para los valores de las integrales se estudian en la lección siguiente.

### Páginas manuscritas (pp. PDF 22–23). Demostración del punto 1: suma

Para cualquier conjunto no vacío $`E\subset[a,b]`$ y $`x,y\in E`$, la desigualdad triangular da

```math
\begin{aligned}
|(f+g)(x)-(f+g)(y)|
&\le |f(x)-f(y)|+|g(x)-g(y)|\\
&\le\omega(f)_E+\omega(g)_E.
\end{aligned}
```

Tomando el [supremo](lecture-11-12.md#def-2-3-1), obtenemos

```math
\omega(f+g)_E\le\omega(f)_E+\omega(g)_E,
\qquad
\omega_k(f+g)\le\omega_k(f)+\omega_k(g).
```

Multiplicamos por las longitudes de los subintervalos y sumamos:

```math
0\le\sum_{k=0}^{n-1}\omega_k(f+g)\Delta x_k
\le\sum_{k=0}^{n-1}\omega_k(f)\Delta x_k
+\sum_{k=0}^{n-1}\omega_k(g)\Delta x_k
\xrightarrow[\lambda_\tau\to0]{}0.
```

Las dos sumas de la derecha tienden a cero por la integrabilidad de las funciones originales. El criterio demuestra la integrabilidad de su suma. $`\blacksquare`$

### Página manuscrita (p. PDF 24). Demostración del punto 2: producto

Por el [lema 4.2.1](lecture-39-40.md#lem-4-2-1), existen constantes finitas $`K,L\ge0`$ con $`|f|\le K`$, $`|g|\le L`$. Sumando y restando un producto mixto, obtenemos

```math
\begin{aligned}
|f(x)g(x)-f(y)g(y)|
&=|[f(x)-f(y)]g(x)+f(y)[g(x)-g(y)]|\\
&\le L|f(x)-f(y)|+K|g(x)-g(y)|.
\end{aligned}
```

Así,

```math
\omega_k(fg)\le L\omega_k(f)+K\omega_k(g).
```

Después de multiplicar por las longitudes y sumar, el miembro derecho tiende a cero como en el punto 1. Por tanto, el producto es integrable. $`\blacksquare`$

> **Corrección del manuscrito.** La última estimación de la p. 24 escribe por error $`\omega_k(f+g)`$ en lugar de $`\omega_k(fg)`$. Todo el cálculo anterior y el punto demostrado se refieren al producto.

### Página manuscrita (p. PDF 25). Demostraciones de los puntos 3–5

**3. Multiplicación por un escalar.** Es el punto 2 con la función constante $`g\equiv\alpha`$, que es continua y, por tanto, integrable. También se admite un coeficiente nulo.

**4. Valor absoluto.** La desigualdad triangular inversa da

```math
\bigl||f(x)|-|f(y)|\bigr|\le|f(x)-f(y)|
\quad\Longrightarrow\quad
\omega_k(|f|)\le\omega_k(f).
```

El criterio de oscilaciones completa la demostración.

**5. Cociente.** Escribimos $`f/g=f\cdot(1/g)`$. Basta demostrar la integrabilidad de la recíproca y aplicar el punto 2. Sea

```math
m=\inf_{x\in[a,b]}|g(x)|>0.
```

La función recíproca está acotada y, para cualesquiera dos puntos,

```math
\left|\frac1{g(x)}-\frac1{g(y)}\right|
=\left|\frac{g(y)-g(x)}{g(x)g(y)}\right|
\le\frac{|g(y)-g(x)|}{m^2}.
```

En consecuencia,

```math
\omega_k\!\left(\frac1g\right)\le\frac{\omega_k(g)}{m^2}.
```

La suma de oscilaciones de la recíproca tiende a cero; esta es integrable y, por tanto, el cociente también lo es. $`\blacksquare`$

> **Explicación editorial.** Para una función integrable arbitraria no basta con que no tenga ceros: el teorema exige que el denominador esté **separado de cero**. Si es continuo y no se anula en el intervalo cerrado, la [cota inferior](../02-real-numbers.md#sec-2-2) positiva se deduce del [teorema de Weierstrass](../05-limits-continuity.md#extreme-value-theorem).

## Estructura de la lección

```mermaid
flowchart TD
    A["4.2.2: funciones continuas"] --> C["Las modificaciones finitas conservan la integral"]
    B["4.2.3: funciones monótonas"] --> H["Clase de funciones integrables"]
    C --> D["4.2.4: restricción y unión de intervalos"]
    D --> E["4.2.10: continuidad a trozos"]
    E --> H
    F["4.2.11: medida nula"] --> G["4.2.5: criterio de Lebesgue"]
    G --> H
    H --> I["4.2.6: suma, producto, escalar, módulo, cociente"]
    I --> J["Estimaciones de oscilaciones y condición del denominador"]
```

---

Anteriores: [lecciones 39–40](lecture-39-40.md) · Siguientes: [lecciones 43–44](lecture-43-44.md) · [Procedencia de las ilustraciones](../../assets/lectures-2025-26/provenance-39-44.md).

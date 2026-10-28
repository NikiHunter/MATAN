---
title: "Lecciones 63–64: diferenciabilidad continua y derivadas de orden superior"
lang: es
course: "Análisis matemático 2025/26"
lecture: 63-64
semester: 2
date: 2026-05-28
source: "ma25_26-lectures_63-64_notes.pdf.txt"
pdf_pages: 42
typed_slides: 21
---
# Lecciones 63–64 — diferenciabilidad continua y derivadas de orden superior

> **Fuente y numeración.** Transcripción elaborada exclusivamente a partir del PDF adjunto `ma25_26-lectures_63-64_notes.pdf.txt`; no se consultó la carpeta de fuentes. Las secciones siguen el orden de las páginas físicas 1–42 del PDF. Los números de «diapositiva impresa» son la secuencia del pie de página 1–21 y se distinguen de las páginas PDF; las páginas manuscritas no reciben número de diapositiva. Las diapositivas impresas se cotejaron con la capa de texto y las imágenes; las demostraciones, ejemplos y anotaciones manuscritos se leyeron en los renderizados. Véanse el [inventario de páginas, hash de la fuente y procedencia de recortes](../../assets/lectures-2025-26/provenance-61-64.md) y el [manifiesto legible por máquina](../../assets/lectures-2025-26/figures-61-64.json).
>
> **Duplicación del semestre 2.** Estas notas se solapan con el registro temático ruso de §§6.3–6.4; se conserva intencionadamente una transcripción secuencial aparte. El semestre 2 abarca las lecciones **33–64**. Véanse el [índice del registro](../../ru/lectures/index.md), [§6.3](../../ru/lectures/16-continuous-differentiability-6-3.md) y [§6.4](../../ru/lectures/17-higher-derivatives-6-4.md).

## Diapositiva impresa 1 (pp. PDF 1). Portada

Análisis matemático, lecciones 63–64; 28 de mayo de 2026.

## Diapositiva impresa 2 (pp. PDF 2). Cita del día

«En el examen se ríe mejor quien lo está tomando».

## Diapositiva impresa 3 (pp. PDF 3). Objetivos de la lección

Se continúa el estudio de la diferenciabilidad continua y se demuestra una fórmula que expresa el incremento de una función multivariable mediante [derivadas parciales](lecture-61-62.md#def-6-1-5). Se definen las derivadas parciales y los diferenciales de orden superior para aplicaciones de varias variables y se establece la relación entre ellos.

<a id="lem-6-3-1"></a>
## Diapositiva impresa 4 (pp. PDF 4). Lema del incremento coordenado — lema 6.3.1

Sean $`E\subset\mathbb R^n`$, $`a\in E`$, $`\delta>0`$, $`V_\delta(a)\subset E`$ y $`h\in V_\delta(0)`$. Supongamos que todas las derivadas parciales primeras de la función escalar $`f:E\to\mathbb R`$ están definidas en $`V_\delta(a)`$. Entonces existen $`c_1,\ldots,c_n\in V_\delta(a)`$ tales que

```math
f(a+h)-f(a)=\sum_{k=1}^{n}\frac{\partial f}{\partial x_k}(c_k)h_k.
```

## Página manuscrita (pp. PDF 5). Demostración mediante incrementos coordenados

Partimos de $`x^1=a`$ y cambiamos las coordenadas de una en una, formando los puntos sucesivos $`x^2,x^3,\ldots,x^{n+1}=a+h`$. En el $`k`$-ésimo segmento consideramos

```math
F_k(t)=f(x^k+t h_k e^k),\qquad t\in[0,1].
```

Por el teorema del valor medio de una variable, existen $`\theta_k\in(0,1)`$ y $`c_k=x^k+\theta_kh_ke^k`$ tales que el incremento en ese segmento es $`\frac{\partial f}{\partial x_k}(c_k)h_k`$. Al sumar, los incrementos se telescopan y se obtiene la fórmula del [lema 6.3.1](#lem-6-3-1). Como $`\|h\|<\delta`$, todos los puntos considerados permanecen en $`V_\delta(a)`$.

![Demostración manuscrita del incremento coordenado](../../assets/lectures-2025-26/lec63-64-p05-coordinate-increment-proof.jpg)

## Página manuscrita (pp. PDF 6). Consecuencia de continuidad del lema del incremento

Basta probar el caso escalar; para una aplicación $`f:E\to\mathbb R^m`$ se aplica el argumento a cada función coordenada. La continuidad de las derivadas parciales primeras en $`a`$ las acota en algún entorno de $`a`$. El [lema 6.3.1](#lem-6-3-1), aplicado a puntos próximos, acota cada incremento por una constante multiplicada por la suma de los cambios de coordenadas, cantidad que tiende a cero con el incremento. Por tanto, $`f`$ es continua en un entorno suficientemente pequeño de $`a`$.

## Diapositiva impresa 5 (pp. PDF 7). La diferenciabilidad continua implica diferenciabilidad — teorema 6.3.1

Sea $`E\subset\mathbb R^n`$, sea $`a`$ un punto interior y supongamos que $`f:E\to\mathbb R^m`$ es [continuamente diferenciable](../15-multivariable-differentiation.md#sec-15-1) en $`a`$. Entonces:

1. $`f`$ es continua en algún entorno $`V(a)`$ de $`a`$;
2. $`f`$ es diferenciable en $`a`$.

## Página manuscrita (pp. PDF 8). Demostración de la continuidad local

Basta demostrar el caso escalar; el caso vectorial se reduce a las coordenadas. En algún entorno $`V(a)`$ las derivadas parciales están acotadas por $`M`$. Para $`x\in V(a)`$ elegimos una bola suficientemente pequeña $`V_{\|h\|}(x)\subset V(a)`$; el lema del incremento coordenado y el teorema del valor medio dan

```math
f(x+h)-f(x)=\sum_{k=1}^{n}\frac{\partial f}{\partial x_k}(c_k)h_k,
```

con cada $`c_k`$ en ese entorno. Por tanto, $`|f(x+h)-f(x)|\le M\sum_{k=1}^{n}|h_k|\to0`$ cuando $`h\to0`$. El dibujo manuscrito azul y amarillo muestra una bola pequeña alrededor de un punto dentro del entorno mayor $`V(a)`$.

![Demostración manuscrita de continuidad local y diagrama de entornos](../../assets/lectures-2025-26/lec63-64-p08-local-continuity-proof.jpg)

## Página manuscrita (pp. PDF 9). Demostración de diferenciabilidad: resto

Aplicamos el lema del incremento coordenado en $`a`$ y escribimos $`c_k=c_k(h)`$. Restamos la parte lineal propuesta del incremento:

```math
R(h)=f(a+h)-f(a)-\sum_{k=1}^{n}\frac{\partial f}{\partial x_k}(a)h_k
=\sum_{k=1}^{n}\left[\frac{\partial f}{\partial x_k}(c_k)-\frac{\partial f}{\partial x_k}(a)\right]h_k.
```

Cuando $`h\to0`$, cada $`c_k(h)\to a`$. La continuidad de las derivadas parciales en $`a`$ hará que $`R(h)=o(\|h\|)`$.

## Página manuscrita (pp. PDF 10). Cota del resto y corolario

Dado $`\varepsilon>0`$, tomamos $`h`$ suficientemente pequeño para que el valor absoluto de cada diferencia entre corchetes sea como máximo $`\varepsilon/\sqrt n`$. Por [Cauchy–Schwarz](lecture-47-48.md#thm-4-4-6),

```math
|R(h)|\le\sqrt{\sum_{k=1}^{n}\left(\frac{\varepsilon}{\sqrt n}\right)^2}\,\sqrt{\sum_{k=1}^{n}h_k^2}=\varepsilon\|h\|.
```

Así, $`R(h)=o(\|h\|)`$ y $`f`$ es diferenciable en $`a`$. En particular, si $`E`$ es abierto y $`f\in C^1(E,\mathbb R^m)`$, entonces $`f`$ es diferenciable en $`E`$.

![Estimación manuscrita del resto de diferenciabilidad](../../assets/lectures-2025-26/lec63-64-p10-differentiability-remainder.jpg)

<a id="def-6-4-1"></a>
## Diapositiva impresa 6 (pp. PDF 11). Derivadas parciales de orden superior — definición 6.4.1

Sean $`E\subset\mathbb R^n`$, $`a`$ un punto interior, $`f:E\to\mathbb R^m`$, $`s\in\mathbb N`$, $`\ell\in\{1,\ldots,s\}`$ e $`i_\ell\in\{1,\ldots,n\}`$. El valor

```math
\frac{\partial^s f}{\partial x_{i_1}\cdots\partial x_{i_s}}(a)
```

se llama derivada parcial de orden $`s`$ respecto de las variables indicadas. Si todos los índices coinciden, la derivada es pura; en otro caso, es mixta. Las anotaciones manuscritas azules dan $`\frac{\partial^3 f}{\partial x_2^3}`$ como pura y $`\frac{\partial^2 f}{\partial x_1\partial x_2}`$ como mixta.

![Definición impresa con ejemplos manuscritos de derivadas puras y mixtas](../../assets/lectures-2025-26/lec63-64-p11-pure-mixed-annotation.jpg)

<a id="def-6-4-2"></a>
## Diapositiva impresa 7 (pp. PDF 12). Diferenciabilidad repetida — definición 6.4.2

La diapositiva formula la definición para $`E\subset\mathbb R^n`$, un punto interior $`a`$, $`f:E\to\mathbb R^n`$ y $`s\in\mathbb N`$. Se transcribe literalmente el codominio de la diapositiva; la [definición 6.4.1](#def-6-4-1) y el [lema 6.4.1](#lem-6-4-1) posteriores usan el codominio general $`\mathbb R^m`$, así que parece haber una discrepancia de notación en la fuente.

La aplicación $`f`$ es $`s`$ veces diferenciable en $`a`$ si:

1. todas las derivadas parciales de órdenes $`0,\ldots,s-2`$ son diferenciables en algún entorno de $`a`$;
2. todas las derivadas parciales de orden $`s-1`$ son diferenciables en $`a`$.

Si $`E`$ es abierto y $`f`$ es $`s`$ veces diferenciable en cada punto de $`E`$, es $`s`$ veces diferenciable en $`E`$. Una [aplicación diferenciable](lecture-59-60.md#def-6-1-2) en $`E`$ cualquier número de veces se llama infinitamente diferenciable.

## Página manuscrita (pp. PDF 13). Ejemplo para $`s=4`$ y caso $`s=1`$

Para $`f:\mathbb R^2\to\mathbb R`$, la página manuscrita desarrolla la condición de diferenciabilidad de orden cuatro en $`a`$: $`f`$, sus derivadas parciales primeras y sus cuatro derivadas parciales ordenadas de segundo orden deben ser diferenciables en un entorno de $`a`$; las ocho derivadas parciales ordenadas de tercer orden deben ser diferenciables en $`a`$. La nota añade que, para $`s=1`$, la primera condición es vacía y la segunda coincide con la diferenciabilidad ordinaria en el punto.

<a id="lem-6-4-1"></a>
## Diapositiva impresa 8 (pp. PDF 14). Derivadas de órdenes inferiores — lema 6.4.1

Sean $`E\subset\mathbb R^n`$, $`a`$ un punto interior, $`s\in\mathbb Z_+`$, $`f:E\to\mathbb R^m`$, y supongamos que todas las derivadas parciales de $`f`$ de orden $`s`$ son diferenciables en algún entorno $`V(a)`$. Entonces, para cada $`k\in\{0,\ldots,s\}`$, todas las derivadas parciales de $`f`$ de orden $`k`$ también son diferenciables en $`V(a)`$.

## Página manuscrita (pp. PDF 15). Demostración del lema 6.4.1

Procedemos por [inducción](../01-logic-sets-functions.md#example-induction) descendente sobre $`k`$. El caso $`k=s`$ es la hipótesis. Sea $`0\le k<s`$ y supongamos que las derivadas de orden $`k+1`$ son diferenciables en $`V(a)`$. Entonces cada derivada de orden $`k`$ tiene todas sus primeras derivadas parciales en $`V(a)`$ y es diferenciable allí. Esto demuestra la afirmación para todos los órdenes menores que $`s`$, hasta el orden $`0`$.

![Demostración manuscrita del lema sobre derivadas de orden inferior](../../assets/lectures-2025-26/lec63-64-p15-order-derivative-lemma.jpg)

## Diapositiva impresa 9 (pp. PDF 16). Diferenciabilidad continua de orden $`s`$

Para $`E\subset\mathbb R^n`$ abierto, $`F\subset\mathbb R^m`$ y $`s\in\mathbb Z_+`$, $`C^s(E,F)`$ denota la clase de aplicaciones de $`E`$ en $`F`$ con derivadas parciales continuas hasta orden $`s`$. Definimos

```math
C^\infty(E,F)=\bigcap_{s=0}^{\infty}C^s(E,F).
```

Para $`k,s\in\mathbb N`$, $`k<s`$, la diapositiva afirma la equivalencia:

1. $`f\in C^s(E,\mathbb R^m)`$;
2. cada derivada parcial de $`f`$ de orden $`k`$ pertenece a $`C^{s-k}(E,\mathbb R^m)`$.

## Página manuscrita (pp. PDF 17). Observaciones sobre las clases $`C^s`$

Por ejemplo, si $`E\subset\mathbb R^2`$ y $`f\in C^3(E,\mathbb R)`$, cada derivada parcial de segundo orden pertenece a $`C^1(E,\mathbb R)`$. También se anota:

1. el caso $`s=1`$ corresponde a una aplicación continuamente diferenciable;
2. la derivada parcial de orden cero es la propia función $`f`$;
3. $`f`$ es continuamente diferenciable $`s`$ veces en $`a`$ si y solo si cada función coordenada de $`f`$ es continuamente diferenciable $`s`$ veces en $`a`$.

<a id="lem-6-4-2"></a>
## Diapositiva impresa 10 (pp. PDF 18). Inclusiones de clases de regularidad — lema 6.4.2

Sea $`E\subset\mathbb R^n`$ abierto. Entonces:

1. si $`k,s\in\mathbb Z_+\cup\{\infty\}`$ y $`k\le s`$, se tiene $`C^s(E,\mathbb R^m)\subset C^k(E,\mathbb R^m)`$;
2. si $`s\in\mathbb N`$ y $`f\in C^s(E,\mathbb R^m)`$, entonces $`f`$ es $`s`$ veces diferenciable en $`E`$.

Las bandas anidadas dibujadas a mano ilustran estas inclusiones.

## Página manuscrita (pp. PDF 19). Demostración de la inclusión de clases

Para $`s`$ finito, la primera afirmación se prueba por inducción sobre $`s-k`$. El caso $`k=s`$ es inmediato. Si $`k<s`$ y $`f\in C^{k+1}(E,\mathbb R^m)`$, cada derivada parcial de orden $`k`$ es continuamente diferenciable y, por tanto, continua; así, $`f\in C^k(E,\mathbb R^m)`$. Luego $`C^s(E,\mathbb R^m)\subset C^k(E,\mathbb R^m)`$.

## Página manuscrita (pp. PDF 20). Demostración de que $`C^s`$ implica diferenciabilidad repetida

Fijemos $`k\in\{0,\ldots,s-1\}`$. Por la primera parte del [lema 6.4.2](#lem-6-4-2), $`f\in C^{k+1}(E,\mathbb R^m)`$. Por tanto, todas las derivadas parciales de orden $`k`$ son continuamente diferenciables en $`E`$. Aplicando sucesivamente este razonamiento a los órdenes hasta $`s-1`$, se concluye que $`f`$ es $`s`$ veces diferenciable en $`E`$.

## Diapositiva impresa 11 (pp. PDF 21). Simetría de las derivadas mixtas

Sean $`E\subset\mathbb R^2`$, $`a`$ un punto interior y $`f:E\to\mathbb R`$. Denotemos las variables por $`x,y`$ y supongamos que existen las [derivadas mixtas](#thm-6-4-1) de segundo orden $`\frac{\partial^2 f}{\partial x\partial y}(a)`$ y $`\frac{\partial^2 f}{\partial y\partial x}(a)`$. ¿Tienen que ser iguales?

## Página manuscrita (pp. PDF 22). Contraejemplo al intercambio sin hipótesis

Consideremos

```math
f(x,y)=\begin{cases}xy\,\dfrac{x^2-y^2}{x^2+y^2},&(x,y)\ne(0,0),\\0,&(x,y)=(0,0).\end{cases}
```

En la página manuscrita se derivan las expresiones fuera del origen y luego se calculan las derivadas mixtas en $`(0,0)`$. Las primeras derivadas parciales en el origen son nulas, pero las derivadas mixtas difieren; sus valores se obtienen en la página siguiente.

![Contraejemplo manuscrito para las derivadas mixtas](../../assets/lectures-2025-26/lec63-64-p22-mixed-partials-counterexample.jpg)

## Página manuscrita (pp. PDF 23). Las derivadas mixtas tienen valores distintos

Para la función anterior

```math
\frac{\partial f}{\partial x}(0,0)=\frac{\partial f}{\partial y}(0,0)=0,
```

```math
\frac{\partial^2 f}{\partial x\partial y}(0,0)=\lim_{y\to0}\frac{-y}{y}=-1,\qquad
\frac{\partial^2 f}{\partial y\partial x}(0,0)=\lim_{x\to0}\frac{x}{x}=1.
```

Por tanto, ambas derivadas mixtas existen, pero no coinciden.

## Diapositiva impresa 12 (pp. PDF 24). Incremento doble

En general, las derivadas mixtas calculadas en órdenes distintos pueden no coincidir, pero sí lo hacen para funciones suficientemente regulares. Basta exigir continuidad de las derivadas mixtas o diferenciabilidad de segundo orden.

Para $`a=(x_0,y_0)`$ definimos el incremento doble

```math
\Delta_a^2f(u,v)=f(x_0+u,y_0+v)-f(x_0+u,y_0)-f(x_0,y_0+v)+f(x_0,y_0).
```

<a id="lem-6-4-3"></a>
## Diapositiva impresa 13 (pp. PDF 25). Incremento doble y derivadas mixtas — lema 6.4.3

Sean $`E\subset\mathbb R^2`$, $`a=(x_0,y_0)`$ un punto interior, $`f:E\to\mathbb R`$, $`\delta>0`$, con las primeras derivadas parciales de $`f`$ definidas en $`V_\delta(a)`$, y sea $`(u,v)\in V_\delta(0,0)`$. Entonces:

1. existe $`\theta\in(0,1)`$ tal que

```math
\Delta_a^2f(u,v)=\left(\frac{\partial f}{\partial x}(x_0+\theta u,y_0+v)-\frac{\partial f}{\partial x}(x_0+\theta u,y_0)\right)u;
```

2. si ambas derivadas mixtas también están definidas en $`V_\delta(a)`$, existen $`\theta_x,\theta_y\in(0,1)`$ tales que

```math
\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial x\partial y}(x_0+\theta_xu,y_0+\theta_yv)uv.
```

## Página manuscrita (pp. PDF 26). Demostración del lema 6.4.3

Primero fijamos $`y=y_0+v`$ y aplicamos el teorema del valor medio en $`x`$ al incremento $`f(x_0+u,y_0+v)-f(x_0,y_0+v)`$, restando el incremento correspondiente en $`y_0`$. Se obtiene el apartado 1. Después aplicamos el teorema del valor medio en $`y`$ a la diferencia resultante de $`f_x`$; así se obtiene la fórmula con la derivada mixta del apartado 2 y coordenadas intermedias $`x_0+\theta_xu`$, $`y_0+\theta_yv`$.

![Demostración manuscrita del lema del incremento doble](../../assets/lectures-2025-26/lec63-64-p26-double-increment-mean-value.jpg)

## Diapositiva impresa 14 (pp. PDF 27). Forma simétrica del lema 6.4.3

Intercambiar $`x`$ e $`y`$ en la demostración proporciona $`\tilde\theta,\tilde\theta_x,\tilde\theta_y\in(0,1)`$ tales que

```math
\Delta_a^2f(u,v)=\left(\frac{\partial f}{\partial y}(x_0+u,y_0+\tilde\theta v)-\frac{\partial f}{\partial y}(x_0,y_0+\tilde\theta v)\right)v,
```

```math
\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial y\partial x}(x_0+\tilde\theta_xu,y_0+\tilde\theta_yv)uv.
```

<a id="lem-6-4-4"></a>
## Diapositiva impresa 15 (pp. PDF 28). Criterio de igualdad — lema 6.4.4

Supongamos que $`f:E\to\mathbb R`$, $`E\subset\mathbb R^2`$, tiene ambas derivadas mixtas de segundo orden en $`a`$. Si cuando $`(u,v)\to(0,0)`$

```math
\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial x\partial y}(a)uv+o(u^2+v^2),
```

```math
\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial y\partial x}(a)uv+o(u^2+v^2),
```

entonces

```math
\frac{\partial^2f}{\partial x\partial y}(a)=\frac{\partial^2f}{\partial y\partial x}(a).
```

## Página manuscrita (pp. PDF 29). Demostración del lema 6.4.4

Restamos los dos desarrollos. Si $`D=\frac{\partial^2f}{\partial x\partial y}(a)-\frac{\partial^2f}{\partial y\partial x}(a)`$, tenemos $`Duv=o(u^2+v^2)`$. Tomando $`u=v=t`$, se obtiene $`Dt^2=o(2t^2)`$; por tanto, $`D=0`$ y las derivadas mixtas coinciden.

![Demostración manuscrita del criterio de igualdad de derivadas mixtas](../../assets/lectures-2025-26/lec63-64-p29-double-increment-criterion.jpg)

<a id="thm-6-4-1"></a>
## Diapositiva impresa 16 (pp. PDF 30). Condiciones suficientes de igualdad — teorema 6.4.1

Sean $`E\subset\mathbb R^2`$, $`a`$ un punto interior y $`f:E\to\mathbb R`$. Si se cumple una de las condiciones siguientes:

1. ambas derivadas $`\frac{\partial^2f}{\partial x\partial y}`$ y $`\frac{\partial^2f}{\partial y\partial x}`$ están definidas en un entorno de $`a`$ y son continuas en $`a`$;
2. la función $`f`$ es dos veces diferenciable en $`a`$,

entonces

```math
\frac{\partial^2f}{\partial x\partial y}(a)=\frac{\partial^2f}{\partial y\partial x}(a).
```

## Página manuscrita (pp. PDF 31). Teorema 6.4.1 bajo la condición 1

Por el [lema 6.4.3](#lem-6-4-3)

```math
\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial x\partial y}(x_0+\theta_xu,y_0+\theta_yv)uv.
```

La continuidad en $`a`$ implica

```math
\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial x\partial y}(a)uv+\alpha(u,v)uv,\qquad\alpha(u,v)\to0.
```

Como $`|uv|\le\frac12(u^2+v^2)`$, el último término es $`o(u^2+v^2)`$. Al intercambiar $`x,y`$ se obtiene el desarrollo análogo con $`f_{yx}(a)`$; el [lema 6.4.4](#lem-6-4-4) completa la demostración.

![Demostración manuscrita bajo la hipótesis de continuidad](../../assets/lectures-2025-26/lec63-64-p31-mixed-partial-symmetry-proof.jpg)

## Página manuscrita (pp. PDF 32). Teorema 6.4.1 bajo la condición 2: desarrollo

Supongamos ahora que $`f`$ es dos veces diferenciable en $`a`$. Aplicamos la primera identidad del [lema 6.4.3](#lem-6-4-3) y desarrollamos la función diferenciable $`f_x`$ en $`a`$. El incremento tiene la forma

```math
\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial x\partial y}(a)uv+\beta(u,v)u,
```

donde el resto procede de los desarrollos de diferenciabilidad de $`f_x`$ en $`(x_0+\theta u,y_0+v)`$ y $`(x_0+\theta u,y_0)`$.

## Página manuscrita (pp. PDF 33). Estimación del resto bajo la condición 2

La demostración manuscrita escribe el resto como

```math
\beta(u,v)=\alpha(\theta u,v)\sqrt{\theta^2u^2+v^2}-\alpha(\theta u,0)|\theta u|,
```

con $`\alpha(h)\to0`$. Puesto que $`|\theta u|\,|u|\le u^2\le u^2+v^2`$ y $`|u|\sqrt{\theta^2u^2+v^2}\le u^2+v^2`$, se sigue que

```math
\beta(u,v)u=o(u^2+v^2).
```

Por tanto, $`\Delta_a^2f(u,v)=\frac{\partial^2f}{\partial x\partial y}(a)uv+o(u^2+v^2)`$. Intercambiar $`x,y`$ da la expresión correspondiente con $`f_{yx}(a)`$; el [lema 6.4.4](#lem-6-4-4) concluye la demostración.

![Estimación manuscrita del resto en la demostración del teorema 6.4.1](../../assets/lectures-2025-26/lec63-64-p33-differentiability-remainder-proof.jpg)

## Diapositiva impresa 17 (pp. PDF 34). Derivadas continuas de segundo orden — corolario

Si $`f`$ es dos veces continuamente diferenciable en $`a`$, entonces

```math
\frac{\partial^2f}{\partial x\partial y}(a)=\frac{\partial^2f}{\partial y\partial x}(a).
```

## Diapositiva impresa 18 (pp. PDF 35). Observaciones sobre el teorema 6.4.1

Ninguna de las dos condiciones del [teorema 6.4.1](#thm-6-4-1) es necesaria para la simetría de las derivadas mixtas. Las condiciones 1 y 2 son independientes: ninguna se deduce de la otra. En la diapositiva se resalta en rojo la frase «no es necesaria».

## Página manuscrita (pp. PDF 36). Ejemplo: las derivadas mixtas pueden ser no acotadas

Sea

```math
\varphi(t)=\begin{cases}t^2\sin(1/t^2),&t\ne0,\\0,&t=0,\end{cases}\qquad f(x,y)=\varphi(x)\varphi(y).
```

La función $`\varphi`$ es diferenciable en $`\mathbb R`$ y

```math
\varphi'(t)=\begin{cases}2\left(t\sin(1/t^2)-\frac1t\cos(1/t^2)\right),&t\ne0,\\0,&t=0.\end{cases}
```

Todas las derivadas parciales de primer y segundo orden de $`f`$ en $`(0,0)`$ son nulas. Sin embargo,

```math
\frac{\partial^2f}{\partial x\partial y}\left(\frac1{\sqrt{2\pi k}},\frac1{\sqrt{2\pi k}}\right)=\left(\varphi'\left(\frac1{\sqrt{2\pi k}}\right)\right)^2=8\pi k\to+\infty.
```

Por tanto, la derivada mixta no está acotada cerca del origen y no se cumple la condición 1 del [teorema 6.4.1](#thm-6-4-1).

## Página manuscrita (pp. PDF 37). La primera derivada parcial puede no ser diferenciable

Para $`f(x,y)=\varphi(x)\varphi(y)`$, la estimación manuscrita sobre la diagonal $`(t,t)`$ es

```math
\frac{f_x(t,t)}{\|(t,t)\|}=\sqrt2\left(t^2\sin^2(1/t^2)-\sin(1/t^2)\cos(1/t^2)\right)\not\to0.
```

Si $`f_x`$ fuera diferenciable en $`(0,0)`$, como $`f_x(0,0)=0`$, este cociente tendría que tender a cero. Por tanto, $`f_x`$ no es diferenciable en el origen y $`f`$ no es dos veces diferenciable allí.

## Página manuscrita (pp. PDF 38). Ejemplos sobre las condiciones de regularidad

Para la misma $`\varphi`$ y $`a=(0,0)`$, la página incluye dos ejemplos:

1. $`f(x,y)=\varphi(x)+\varphi(y)`$ tiene derivadas mixtas continuas en $`a`$, pero no es dos veces diferenciable en $`a`$.
2. $`g(x,y)=\varphi(x)\varphi(y)`$ es diferenciable en $`a`$, pero sus derivadas mixtas no están acotadas cerca de $`a`$.

Estos ejemplos ilustran que las hipótesis del [teorema 6.4.1](#thm-6-4-1) son suficientes, no necesarias. La página manuscrita señala el segundo ejemplo como ejercicio.

![Ejemplos manuscritos sobre las hipótesis de las derivadas mixtas](../../assets/lectures-2025-26/lec63-64-p38-mixed-partial-independence-examples.jpg)

<a id="def-6-4-3"></a>
## Diapositiva impresa 19 (pp. PDF 39). Diferenciales de orden superior — definición 6.4.3

Sean $`E\subset\mathbb R^n`$, $`a`$ un punto interior y $`f:E\to\mathbb R^m`$.

1. Definimos $`d_a^0f(h)=f(a)`$ para cada $`h\in\mathbb R^n`$. El mapa $`d_a^0f`$ se llama diferencial de orden cero en $`a`$. Para cada $`h`$, el mapa $`x\mapsto d_x^0f(h)`$, definido al menos en $`a`$, se llama diferencial de orden cero sobre el incremento $`h`$ y se denota $`d^0f(h)`$. La diapositiva resalta en rojo «al menos en el punto $`a`$».
2. Sea $`s\in\mathbb N`$ y supongamos definido el diferencial $`d^{s-1}f(h)`$. Si para cada $`h\in\mathbb R^n`$ el mapa $`x\mapsto d_x^{s-1}f(h)`$ está definido en un entorno de $`a`$ y es diferenciable en $`a`$, ponemos

```math
d_a^sf(h)=d_a\bigl(d^{s-1}f(h)\bigr)(h)\qquad\text{para cada }h\in\mathbb R^n.
```

## Diapositiva impresa 20 (pp. PDF 40). Diferenciales de orden superior — definición 6.4.3 (continuación)

El mapa $`d_a^sf`$ se llama diferencial de orden $`s`$ en $`a`$. Para cada $`h\in\mathbb R^n`$, el mapa $`x\mapsto d_x^sf(h)`$, definido al menos en $`a`$, se llama diferencial de orden $`s`$ sobre el incremento $`h`$ y se denota $`d^sf(h)`$.

<a id="thm-6-4-2"></a>
## Diapositiva impresa 21 (pp. PDF 41). Cálculo de diferenciales de orden superior — teorema 6.4.2

Si la aplicación $`f:E\to\mathbb R^m`$ es $`s`$ veces diferenciable en el punto interior $`a\in E\subset\mathbb R^n`$, existe el diferencial de orden $`s`$ y

```math
d_a^sf(h)=\sum_{(i_1,\ldots,i_s)\in I_s}\frac{\partial^sf(a)}{\partial x_{i_1}\cdots\partial x_{i_s}}h_{i_1}\cdots h_{i_s}\qquad(h\in\mathbb R^n),
```

```math
d_a^sf(h)=\sum_{\alpha\in M_s}\frac{s!}{\alpha!}\frac{\partial^\alpha f(a)}{\partial x^\alpha}h^\alpha\qquad(h\in\mathbb R^n).
```

**Corrección de la fuente.** En la segunda fórmula impresa falta el factor $`h^\alpha`$. Se incorpora porque es necesario para que la fórmula multiíndice coincida con la primera y sea homogénea de grado $`s`$ respecto de $`h`$.

## Página manuscrita (pp. PDF 42). Multiíndices y segundo diferencial

Un multiíndice es $`\alpha=(\alpha_1,\ldots,\alpha_n)`$ con $`|\alpha|=\alpha_1+\cdots+\alpha_n=s`$. Su factorial es $`\alpha!=\alpha_1!\cdots\alpha_n!`$, $`x^\alpha=x_1^{\alpha_1}\cdots x_n^{\alpha_n}`$ y $`h^\alpha=h_1^{\alpha_1}\cdots h_n^{\alpha_n}`$. La derivada parcial $`\partial^\alpha f/\partial x^\alpha`$ significa

```math
\frac{\partial^{|\alpha|}f}{\partial x_1^{\alpha_1}\cdots\partial x_n^{\alpha_n}}(a).
```

Si $`\alpha_k=0`$, no se deriva respecto de $`x_k`$. En esta misma página manuscrita se anota

```math
d_a^2f(h)=\sum_{i=1}^{n}\sum_{j=1}^{n}\frac{\partial^2f}{\partial x_i\partial x_j}(a)h_ih_j\qquad(h\in\mathbb R^n).
```

![Definición manuscrita del multiíndice y segundo diferencial](../../assets/lectures-2025-26/lec63-64-p42-multi-index-differential.jpg)

## Referencias cruzadas

Esta transcripción se solapa con los capítulos temáticos correspondientes del semestre 2 (lecciones 33–64): [§6.3 — diferenciabilidad continua](../../ru/lectures/16-continuous-differentiability-6-3.md) y [§6.4 — derivadas y diferenciales de orden superior](../../ru/lectures/17-higher-derivatives-6-4.md). Para navegar, véase el [índice del registro ruso](../../ru/lectures/index.md).

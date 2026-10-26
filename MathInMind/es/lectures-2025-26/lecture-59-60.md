---
title: "Lecciones 59–60 — aplicaciones continuas y diferenciabilidad en un punto"
lang: es
course: "Análisis matemático, 2025/26"
lecture: 59-60
semester: 2
date: 2026-05-14
source: "ma25_26-lectures_59-60_notes.pdf.txt"
pdf_pages: 28
typed_slides: 17
---

# Lecciones 59–60 — aplicaciones continuas y diferenciabilidad en un punto

[Índice de lecciones](index.md) · [Русский](../../ru/lectures-2025-26/lecture-59-60.md) · [English](../../en/lectures-2025-26/lecture-59-60.md) · [Anterior: 57–58](lecture-57-58.md)


> **Fuente y cobertura.** `ma25_26-lectures_59-60_notes.pdf.txt`: 28 páginas del PDF, 17 diapositivas impresas y 11 páginas manuscritas; fecha 14 de mayo de 2026. Las diapositivas impresas 1–6 ocupan las páginas 1–6 del PDF; después, la diapositiva 7 está en la página 8, la 8 en la 10, la 9 en la 14, la 10 en la 16, la 11 en la 18, la 12 en la 21, la 13 en la 22, la 14 en la 23, la 15 en la 24, la 16 en la 26 y la 17 en la 27. Se incluyen las páginas manuscritas del PDF 7, 9, 11, 12, 13, 15, 17, 19, 20, 25 y 28. Las anotaciones manuscritas sobre las diapositivas 15 y 16 se atribuyen a sus diapositivas. Solo se utilizó el PDF entregado en el chat; no se consultó la carpeta de origen, por lo que no se indican nombres de archivo ni enlaces de archivo.

> **Duplicación del semestre 2.** La lección se solapa temáticamente con [§5.5](../../ru/lectures/13-continuity-rn-5-5.md) y [§6.1](../../ru/lectures/14-differentiability-6-1.md); véase también el [registro](../../ru/lectures/index.md). El semestre 2 abarca las lecciones 33–64.

## Diapositiva impresa 1 (pp. PDF 1) — Diapositiva de título

«Análisis matemático», lecciones 59–60; D. E. Apushkinskaya, Universidad RUDN; 14 de mayo de 2026.

## Diapositiva impresa 2 (pp. PDF 2) — Cita del día

«En la vida a una persona le debe sonreír la suerte al menos 3 veces: 1 con quién nacer, 2 con quién estudiar, 3 y con quién casarse».

## Diapositiva impresa 3 (pp. PDF 3) — Objetivo de la lección

Se define la noción de continuidad para aplicaciones de varias variables y se generalizan para ellas varias afirmaciones unidimensionales. Se introduce la noción de diferenciabilidad de una aplicación de varias variables en un punto.

## Diapositiva impresa 4 (pp. PDF 4) — §5. Aplicaciones continuas de varias variables — definición 5.5.1

**Definición 5.5.1.** Sean $E\subset\mathbb R^n$, $a\in E$, $f:E\to\mathbb R^m$. La aplicación $f$ se llama continua en el punto $a$ si

$$
\forall\varepsilon>0\ \ \exists\delta>0\ \ \forall x\in V_\delta(a)\cap E\ \ f(x)\in V_\varepsilon(f(a)).
$$

Esta definición puede reescribirse en el lenguaje de las desigualdades:

$$
\forall\varepsilon>0\ \ \exists\delta>0\ \ \forall x\in E:\ \ \|x-a\|<\delta\ \Rightarrow\ \|f(x)-f(a)\|<\varepsilon.
$$

## Diapositiva impresa 5 (pp. PDF 5) — Observaciones sobre la continuidad en un punto

1) Sea el punto $a$ de acumulación para $E$. Entonces la continuidad de $f$ en el punto $a$ es equivalente a la igualdad $\lim_{x\to a}f(x)=f(a)$. 2) Si $a$ es un punto aislado del conjunto $E$, entonces la aplicación $f$ es continua en el punto $a$. 3) La continuidad de la aplicación $f$ en el punto $a$ es equivalente a la afirmación siguiente: para toda sucesión $\{x^k\}_{k=1}^{\infty}\subset E$, de $x^k\to a$ se sigue $f(x^k)\to f(a)$ cuando $k\to\infty$.

$$
\lim_{x\to a}f(x)=f(a)
$$

## Diapositiva impresa 6 (pp. PDF 6) — Continuidad de una composición

**Teorema 5.5.1.** Sean $E\subset\mathbb R^n$, $F\subset\mathbb R^m$, $a\in E$, $f:E\to F$, $g:F\to\mathbb R^s$. Si $f$ es continua en el punto $a$ y $g$ es continua en el punto $f(a)$, entonces $g\circ f$ es continua en el punto $a$.

## Página manuscrita (pp. PDF 7) — Demostración del teorema 5.5.1

Sea $\{x^k\}_{k=1}^{\infty}$ una sucesión en $E$ tal que $x^k\to a$ cuando $k\to\infty$. Aplicando la observación 3 primero a $f$ y luego a $g$, obtenemos

$$
f(x^k)\to f(a),\qquad g\left(f(x^k)\right)\to g\left(f(a)\right)\quad\text{cuando } k\to\infty.
$$

Así pues, $(g\circ f)(x^k)\to(g\circ f)(a)$ cuando $k\to\infty$. De aquí, en virtud de la observación 3, se sigue la continuidad de $g\circ f$ en el punto $a$.

$$
(g\circ f)(x^k)\to(g\circ f)(a)\quad\text{cuando } k\to\infty
$$

![Demostración de la continuidad de una composición (pp. PDF 7)](../../assets/lectures-2025-26/lec59-60-p07-composition-proof.jpg)

## Diapositiva impresa 7 (pp. PDF 8) — Continuidad y operaciones aritméticas

**Teorema 5.5.2.** Sean $E\subset\mathbb R^n$, $a\in E$, y sean las aplicaciones $f,g:E\to\mathbb R^m$ continuas en el punto $a$. Entonces se cumplen las afirmaciones siguientes. 1) La aplicación $f+g$ es continua en el punto $a$. 2) Si la función $\lambda:E\to\mathbb R$ es continua en el punto $a$, entonces la aplicación $\lambda f$ es continua en el punto $a$. 3) La aplicación $f\cdot g$ es continua en el punto $a$. 4) Si $m=1$ y $g(a)\ne0$, entonces la función $\frac fg$ es continua en el punto $a$.

## Página manuscrita (pp. PDF 9) — Demostración del teorema 5.5.2

Si $a$ es punto de acumulación de $E$, todas las afirmaciones se siguen del teorema 5.4.2, y para un punto aislado son válidas en virtud de la observación 2.

$$
\left.\begin{aligned} &a\ \text{es punto de acumulación de } E\\ &\text{teorema 5.4.2}\end{aligned}\right\}\Longrightarrow\ \text{todas las afirmaciones del teorema 5.5.2}
$$

## Diapositiva impresa 8 (pp. PDF 10) — Continuidad de una aplicación en un conjunto

**Definición 5.5.2.** Sean $E\subset\mathbb R^n$, $f:E\to\mathbb R^m$. La aplicación $f$ se llama continua en el conjunto $E$ si es continua en todo punto de $E$.

**Teorema 5.5.3.** Sean $E\subset\mathbb R^n$, $f:E\to\mathbb R^m$. Entonces son equivalentes las afirmaciones siguientes. 1) La aplicación $f$ es continua en $E$. 2) Si el conjunto $G$ es abierto en $\mathbb R^m$, entonces $f^{-1}(G)$ es abierto en $E$.

Así pues, la continuidad de $f$ en $E$ significa que la imagen inversa de todo conjunto abierto en $\mathbb R^m$ es abierta en $E$.

$$
f^{-1}(G)
$$

## Página manuscrita (pp. PDF 11) — Demostración del teorema 5.5.3: 1) ⇒ 2)

En la figura: un conjunto $E$ en $\mathbb R^n$, su imagen bajo la aplicación continua $f\in C(E,\mathbb R^m)$ y un conjunto $G$ abierto en $\mathbb R^m$; la imagen inversa $f^{-1}(G)$ está marcada como conjunto abierto en $E$.

Por la hipótesis se sabe que $f\in C(E,\mathbb R^m)$. Sea $G\subset\mathbb R^m$ abierto; denotemos $F:=f^{-1}(G)$. Si $a\in F$, entonces $f(a)\in G$, ya que $a$ pertenece a la imagen inversa de $G$.

**Importante:** $f^{-1}(G)$ es abierto en $E$, ¡no en $\mathbb R^n$!

$$
F:=f^{-1}(G),\qquad a\in F\ \Rightarrow\ f(a)\in G
$$

![La imagen inversa de un conjunto abierto (pp. PDF 11)](../../assets/lectures-2025-26/lec59-60-p11-preimage-open-diagram.jpg)

## Página manuscrita (pp. PDF 12) — Final de 1) ⇒ 2)

Como $f(a)\in G$ y $G$ es abierto, por la propiedad de un conjunto abierto $\exists\varepsilon>0$: $V_\varepsilon(f(a))\subset G$. Como $f$ es continua, $\exists\delta>0$:

$$
f\left(V_\delta(a)\cap E\right)\subset V_\varepsilon\left(f(a)\right).
$$

Entonces

$$
V_\delta(a)\cap E\subset f^{-1}\left(V_\varepsilon(f(a))\right)\subset f^{-1}(G)=F,
$$

es decir, $\forall a\in F$ es punto interior para $F$ en $E$; en consecuencia, $F$ es abierto en $E$.

$$
V_\delta(a)\cap E\subset f^{-1}\left(V_\varepsilon(f(a))\right)\subset f^{-1}(G)=F
$$

![La inclusión de la imagen inversa (pp. PDF 12)](../../assets/lectures-2025-26/lec59-60-p12-preimage-inclusion.jpg)

## Página manuscrita (pp. PDF 13) — Demostración de 2) ⇒ 1) y una observación

Sean $a\in E$ y $\varepsilon>0$. Entonces $f^{-1}\left(V_\varepsilon(f(a))\right)$ es abierto en $E$ en virtud de 2), de donde $\exists\delta>0$:

$$
V_\delta(a)\cap E\subset f^{-1}\left(V_\varepsilon(f(a))\right),
$$

es decir, $f\left(V_\delta(a)\cap E\right)\subset V_\varepsilon\left(f(a)\right)$. En consecuencia, $f$ es continua en el punto $a$.

**Suya:** la afirmación 2) del teorema 5.5.3 no cambia si se supone que $G$ es abierto en $f(E)$ y no en $\mathbb R^m$.

$$
f\left(V_\delta(a)\cap E\right)\subset V_\varepsilon\left(f(a)\right)
$$

## Diapositiva impresa 9 (pp. PDF 14) — La imagen continua de un compacto

**Teorema 5.5.4.** Sean $E\subset\mathbb R^n$, $f\in C(E,\mathbb R^m)$. Si el conjunto $E$ es compacto, entonces $f(E)$ también es compacto.

**Corolario.** Sean $a,b\in\mathbb R^n$. Entonces el conjunto

$$
\Delta_{a,b}:=\{a+t(b-a):\ t\in[0,1]\}
$$

es compacto en $\mathbb R^n$.

**Observación.** Si $n=1$, entonces $\Delta_{a,b}=[a,b]$.

$$
\Delta_{a,b}:=\{a+t(b-a):\ t\in[0,1]\}
$$

## Página manuscrita (pp. PDF 15) — Demostración del teorema 5.5.4

Sea $\{y^k\}_{k=1}^{\infty}$ una sucesión en $f(E)$. Entonces $\exists\{x^k\}_{k=1}^{\infty}$ — una sucesión en $E$ tal que $f(x^k)=y^k$ para todo $k\in\mathbb N$. Como $E$ es compacto y $\{x^k\}_{k=1}^{\infty}$ es una sucesión en $E$, se puede elegir una subsucesión $\{x^{k_i}\}_{i=1}^{\infty}$ tal que $x^{k_i}\to a\in E$ cuando $i\to\infty$. De aquí, como $f$ es continua, $y^{k_i}=f(x^{k_i})\to f(a)\in f(E)$ cuando $i\to\infty$. Así pues, la sucesión $\{y^{k_i}\}$ tiene límite en $f(E)$, es decir, $f(E)$ es compacto.

$$
x^{k_i}\to a\in E\ \Longrightarrow\ y^{k_i}=f(x^{k_i})\to f(a)\in f(E)
$$

![La imagen continua de un compacto (pp. PDF 15)](../../assets/lectures-2025-26/lec59-60-p15-compact-image-proof.jpg)

## Diapositiva impresa 10 (pp. PDF 16) — El teorema de Weierstrass

**Teorema 5.5.5.** Sea el conjunto $E\subset\mathbb R^n$ compacto y $f\in C(E,\mathbb R^m)$. Entonces se cumplen las afirmaciones siguientes. 1) La aplicación $f$ está acotada en $E$. 2) Si $m=1$ (es decir, $f$ es una función), entonces $f$ alcanza en $E$ su valor máximo y su valor mínimo.

## Página manuscrita (pp. PDF 17) — Demostración del teorema 5.5.5

Pongamos $F=f(E)$. Por el teorema 5.5.4 el conjunto $F$ es compacto y, por tanto, acotado en $\mathbb R^m$. Con ello queda demostrada la acotación de $f$.

Comprobemos la afirmación 2) ($m=1$, es decir, $f:E\to\mathbb R^1$). Pongamos $M=\sup_E f$. El conjunto $F$ está acotado en $\mathbb R$, por lo que $M\in\mathbb R$. Entonces

$$
\forall k\in\mathbb N\ \ \exists y^k\in F:\ \ M-\frac1k<y^k\le M.
$$

Por el teorema del emparedado $y^k\to M$ cuando $k\to\infty$. Como $F$ es cerrado (teorema 5.3.1), $M\in F$, es decir, $M\in f(E)$. La inclusión $\inf_E f\in f(E)$ se demuestra de manera análoga.

$$
\forall k\in\mathbb N\ \ \exists y^k\in F:\ \ M-\frac1k<y^k\le M
$$

## Diapositiva impresa 11 (pp. PDF 18) — Continuidad uniforme y el teorema de Cantor

**Definición 5.5.3.** Sean $E\subset\mathbb R^n$, $f:E\to\mathbb R^m$. La aplicación $f$ se llama uniformemente continua en $E$ si

$$
\forall\varepsilon>0\ \ \exists\delta>0\ \ \forall x,y\in E:\ \ \|x-y\|<\delta\ \Rightarrow\ \|f(x)-f(y)\|<\varepsilon.
$$

**Teorema 5.5.6.** Sea $E$ un subconjunto compacto de $\mathbb R^n$ y $f\in C(E,\mathbb R^m)$. Entonces $f$ es uniformemente continua en $E$.

## Página manuscrita (pp. PDF 19) — Demostración del teorema 5.5.6, comienzo

Sea $\varepsilon>0$. Busquemos un $\delta>0$ que satisfaga la definición 5.5.3. Primero, para cada punto tenemos la afirmación ✳:

$$
\forall a\in E\ \ \exists\delta_a>0:\ \ \|x-a\|<2\delta_a\ \Rightarrow\ \|f(x)-f(a)\|<\frac{\varepsilon}{2}.
$$

La familia $\left\{V_{\delta(a)}(a)\right\}_{a\in E}$ forma un recubrimiento abierto de $E$; como $E$ es compacto, de ella se puede extraer un subrecubrimiento finito, es decir, $\exists$ un subconjunto finito $F\subset E$:

$$
E\subset\bigcup_{a\in F}V_{\delta_a}(a).
$$

Pongamos $\delta=\min_{a\in F}\delta_a$. Como $F$ es finito, $\delta>0$ está bien definido. Probemos que este $\delta$ es el buscado.

$$
E\subset\bigcup_{a\in F}V_{\delta_a}(a),\qquad \delta=\min_{a\in F}\delta_a>0
$$

> **Notación del manuscrito.** En la familia del recubrimiento y en la unión la pizarra muestra $V_{\delta(a)}(a)$ y $V_{\delta_a}(a)$ — dos escrituras distintas de un mismo radio; en la fórmula siguiente se usa $\delta_a$, coherente con el mínimo $\delta=\min_{a\in F}\delta_a$.

![Demostración del teorema de Cantor (pp. PDF 19)](../../assets/lectures-2025-26/lec59-60-p19-cantor-uniform-continuity.jpg)

## Página manuscrita (pp. PDF 20) — Demostración del teorema 5.5.6, final

En efecto, sean $x,y\in E$, $\|x-y\|<\delta$. Entonces $\exists a\in F$: $\|x-a\|<\delta_a$. Además,

$$
\|y-a\|\le\|y-x\|+\|x-a\|<\delta+\delta_a\le 2\delta_a.
$$

Aplicando ✳, obtenemos

$$
\|f(x)-f(y)\|\le\|f(x)-f(a)\|+\|f(y)-f(a)\|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon.
$$

Por tanto $f$ es uniformemente continua en $E$.

$$
\|y-a\|\le\|y-x\|+\|x-a\|<\delta+\delta_a\le 2\delta_a
$$

$$
\|f(x)-f(y)\|\le\|f(x)-f(a)\|+\|f(y)-f(a)\|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon
$$

## Diapositiva impresa 12 (pp. PDF 21) — Capítulo 6. Cálculo diferencial

En la diapositiva se anuncia el capítulo 6: «Cálculo diferencial de aplicaciones de varias variables». Sin embargo, el encabezado de página lleva otra formulación — «Cálculo diferencial-2»; la discrepancia entre el encabezado y el título de la diapositiva se señala, pero no se corrige.

## Diapositiva impresa 13 (pp. PDF 22) — §1. Diferenciabilidad de una aplicación en un punto — definición 6.1.1

**Definición 6.1.1.** Sean $E\subset\mathbb R^n$, el punto $a\in\mathbb R^n$ de acumulación para $E$, $f:E\to\mathbb R^m$, $N\in\mathbb N$. Pongamos $\alpha(x)=f(x)\cdot\|x-a\|^{-N}=\frac{f(x)}{\|x-a\|^N}$. 1) Si la aplicación $\alpha(x)$ está acotada en algún entorno perforado $\dot V(a)$ del punto $a$, se dice que $f(x)=O(\|x-a\|^N)$ cuando $x\to a$. 2) Si $\lim_{x\to a}\alpha(x)=0$, se dice que $f(x)=o(\|x-a\|^N)$ cuando $x\to a$.

$$
f(x)=O(\|x-a\|^N)\quad (x\to a),\qquad f(x)=o(\|x-a\|^N)\quad (x\to a)
$$

## Diapositiva impresa 14 (pp. PDF 23) — Observaciones sobre los símbolos $o$ y $O$

Sea $a\in E$. Aunque en la definición del símbolo $o$ el valor $\alpha(a)$ es irrelevante, es cómodo poner $\alpha(a)=0$, es decir, considerar la aplicación $\alpha$ continua en el punto $a$. En lo sucesivo siempre lo haremos así. Si $N=1$, entonces en lugar de $o(\|x-a\|)$ escribiremos simplemente $o(x-a)$, como en el caso de funciones de una variable. Esta observación se refiere también al símbolo $O$.

$$
o(x-a):=o(\|x-a\|)
$$

## Diapositiva impresa 15 (pp. PDF 24) — Diferenciabilidad en un punto — definiciones 6.1.2 y 6.1.3

**Definición 6.1.2.** Sean $E\subset\mathbb R^n$, sea $a$ un punto interior de $E$, $f:E\to\mathbb R^m$. La aplicación $f$ se llama diferenciable en el punto $a$ si $\exists$ un operador lineal $T\in\mathcal L(\mathbb R^n,\mathbb R^m)$ para el cual

$$
f(x)=f(a)+T(x-a)+o(x-a)\qquad\text{cuando } x\to a. \tag{6.1.1}
$$

El operador $T$ se llama diferencial de $f$ en el punto $a$ y se denota con el símbolo $d_af$.

**Definición 6.1.3.** Sea la aplicación $T:\mathbb R^n\to\mathbb R^m$ que satisface la condición de linealidad: $T(\lambda x+\mu y)=\lambda T(x)+\mu T(y)$ para todos $x,y\in\mathbb R^n$ y $\lambda,\mu\in\mathbb R$. Entonces $T$ se llama operador lineal.

Nota manuscrita en la diapositiva: «Notación $T\in\mathcal L(\mathbb R^n,\mathbb R^m)$» con una flecha hacia la entrada $\mathcal L(\mathbb R^n,\mathbb R^m)$ de la definición 6.1.2.

$$
T(\lambda x+\mu y)=\lambda T(x)+\mu T(y)
$$

## Página manuscrita (pp. PDF 25) — Aclaración de la definición 6.1.2

La relación (6.1.1) es equivalente a la representación

$$
f(x)=f(a)+T(x-a)+\beta(x),
$$

donde

$$
\frac{\beta(x)}{\|x-a\|}\to0\qquad\text{cuando } x\to a,\ x\ne a.
$$

$$
\frac{\beta(x)}{\|x-a\|}\to0\qquad (x\to a,\ x\ne a)
$$

## Diapositiva impresa 16 (pp. PDF 26) — Observaciones sobre la fórmula (6.1.1)

La fórmula (6.1.1) se escribe a menudo con ayuda del incremento del argumento $h$:

$$
f(a+h)=f(a)+d_af(h)+o(h)\qquad (h\to0) \tag{6.1.2}
$$

o, con más detalle,

$$
f(a+h)=f(a)+d_af(h)+\alpha(h)\|h\|, \tag{6.1.3}
$$

donde la aplicación $\alpha$ es continua en cero y $\alpha(0)=0$.

En el caso $n=1$ el operador $d_af$ representa una función vectorial lineal, es decir, una aplicación de la forma $h\mapsto k\cdot h$, donde $k\in\mathbb R^m$. El coeficiente $k$ se llama derivada de $f$ en el punto $a$ y se denota con el símbolo $f'(a)$.

Nota manuscrita al pie de la diapositiva: $h=x-a$.

$$
f(a+h)=f(a)+d_af(h)+\alpha(h)\|h\|
$$

## Diapositiva impresa 17 (pp. PDF 27) — La diferenciabilidad implica continuidad

**Observación.** De la diferenciabilidad de la aplicación $f$ en el punto $a$ se sigue su continuidad en el punto $a$. En efecto, por la fórmula (6.1.3)

$$
f(a+h)-f(a)=d_af(h)+\alpha(h)\cdot\|h\|\to0\qquad (h\to0)
$$

en virtud de la continuidad de $d_af$ y del teorema 6.4.2.

Como en el caso unidimensional, ¡de la continuidad **NO SE SIGUE** la diferenciabilidad!

$$
f(a+h)-f(a)=d_af(h)+\alpha(h)\cdot\|h\|\to0\qquad (h\to0)
$$

> **Referencia a una afirmación aún no estudiada.** Aquí se cita el «teorema 6.4.2», que no se había formulado hasta este punto del curso; al parecer se tiene en mente la propiedad de que un operador lineal es continuo (o que un operador lineal es acotado). La referencia se conserva tal como en la fuente.

## Página manuscrita (pp. PDF 28) — Ejemplos 1 y 2

**Ejemplo 1.** Sea $f:\mathbb R^n\to\mathbb R^m$, $f(x)=C=\text{const}$ (donde $C\in\mathbb R^m$). Entonces $\forall h\in\mathbb R^n$

$$
f(a+h)=f(a)=f(a)+\mathbf{0}\cdot h,
$$

donde $\mathbf{0}$ es el operador nulo. En consecuencia $d_af=\mathbf{0}$ y $\alpha(x)\equiv0$. Por tanto la aplicación $f=\text{const}$ es diferenciable en todo punto $a\in\mathbb R^n$.

**Ejemplo 2.** Sea $f\in\mathcal L(\mathbb R^n,\mathbb R^m)$. Entonces $\forall h\in\mathbb R^n$

$$
f(a+h)-f(a)=f(a+h-a)=f(h)
$$

en virtud de la linealidad. En este caso $d_af=f$ y $\alpha\equiv0$, en consecuencia la aplicación lineal $f$ es diferenciable en todo punto $a\in\mathbb R^n$.

$$
f(a+h)=f(a)+\mathbf{0}\cdot h,\qquad d_af=\mathbf{0}
$$

$$
f(a+h)-f(a)=f(h),\qquad d_af=f
$$

![Ejemplos: una constante y una aplicación lineal (pp. PDF 28)](../../assets/lectures-2025-26/lec59-60-p28-differentiability-examples.jpg)

---

[Índice de lecciones](index.md) · [Русский](../../ru/lectures-2025-26/lecture-59-60.md) · [English](../../en/lectures-2025-26/lecture-59-60.md) · [Anterior: 57–58](lecture-57-58.md)

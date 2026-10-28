---
title: "Lecciones 55–56 — Límite de una subsucesión, compacidad y topología de $\\mathbb R^n$"
lang: es
course: "Análisis matemático, 2025/26"
lecture: 55-56
semester: 2
date: 2026-04-30
source: "MA25-26_ktrwbb_55-56_notes.pdf.txt"
pdf_pages: 31
typed_slides: 18
aliases: ["Lecciones 55–56 (es)"]
tags: [mathinmind/es, mathinmind/lecture]
---

# Lecciones 55–56 — Límite de una subsucesión, compacidad y topología de $\mathbb R^n$

[[es/lectures-2025-26/lecture-54|← Lección 54]] · [[es/lectures-2025-26/index|Índice de lecciones]] · [[es/lectures-2025-26/lecture-57-58|Lecciones 57–58 →]] · [[es/term-index|Términos y teoremas]] · [[ru/lectures-2025-26/lecture-55-56|Русский]] · [[en/lectures-2025-26/lecture-55-56|English]]


> [!info] Fuente y cobertura
> `MA25-26_ktrwbb_55-56_notes.pdf.txt`: 31 páginas del PDF, 18 diapositivas impresas y 13 páginas manuscritas; fecha 30 de abril de 2026. Las diapositivas impresas 1–9 ocupan las páginas 1–9 del PDF; después, la diapositiva 10 está en la página 13, la 11 en la 16, la 12 en la 17, la 13 en la 19, la 14 en la 20, la 15 en la 22, la 16 en la 26, la 17 en la 29 y la 18 en la 30. Se incluyen las páginas manuscritas del PDF 10, 11, 12, 14, 15, 18, 21, 23, 24, 25, 27, 28 y 31. Las anotaciones manuscritas sobre las diapositivas impresas 4, 5, 7, 8, 19 y 26 se incluyen y se atribuyen a sus diapositivas, no a páginas separadas del PDF. Solo se utilizó el PDF entregado en el chat; no se consultó la carpeta de origen, por lo que no se indican nombres de archivo ni enlaces de archivo.

> [!info] Duplicación del semestre 2
> La lección se solapa temáticamente con [[ru/lectures/10-vector-sequences-5-2|§5.2]] y [[ru/lectures/11-topology-rn-5-3|§5.3]]; véase también el [[ru/lectures/index|registro]]. El semestre 2 abarca las lecciones 33–64.

## Diapositiva impresa 1 (pp. PDF 1) — Diapositiva de título

«Análisis matemático», lecciones 55–56; D. E. Apushkinskaya, Universidad RUDN; 30 de abril de 2026.

## Diapositiva impresa 2 (pp. PDF 2) — Cita del día

«El bien vencerá al mal si duerme lo suficiente y descansa..»

## Diapositiva impresa 3 (pp. PDF 3) — Objetivo de la lección

Continúa el traslado al caso multidimensional de afirmaciones demostradas antes para sucesiones numéricas unidimensionales. Se trata de encontrar en $\mathbb R^n$ análogos razonables de los intervalos abiertos y cerrados y de los conjuntos [[es/lectures-2025-26/lecture-57-58#^def-5-3-7|compactos]].

## Diapositiva impresa 4 (pp. PDF 4) — §2. Límite de una subsucesión — teorema 5.2.3

> [!theorem] Teorema 5.2.3
> Sea $\{x^k\}_{k=1}^{\infty}$ una sucesión en $\mathbb R^n$, sea $\{x^{k_i}\}_{i=1}^{\infty}$ una [[es/lectures-2025-26/lecture-11-12#^def-2-3-7|subsucesión]] suya y sea $a\in\overline{\mathbb R^n}$. Si $\lim_{k\to\infty}x^k=a$, entonces $\lim_{i\to\infty}x^{k_i}$ también existe y es igual a $a$.

> [!remark] Nota editorial sobre la capa de texto
> En la diapositiva impresa el punto $a$ se toma del espacio ampliado $\overline{\mathbb R^n}$; la capa de texto del PDF pierde la barra superior y lee $a\in\mathbb R^n$. Aquí y en adelante las barras superiores se restauran a partir de la imagen de la página (véase también la diapositiva 16, donde se pierden las barras sobre $B_\delta$).

**Demostración manuscrita (parte inferior de la misma diapositiva).** Sea $a\in\mathbb R^n$. Entonces

$$
\lim_{i\to\infty}\|x^{k_i}-a\|=\lim_{k\to\infty}\|x^k-a\|=0,
$$

de donde

$$
\lim_{i\to\infty}x^{k_i}=a.
$$

El caso $a=\infty$ se trata de manera análoga.

![Demostración manuscrita del teorema 5.2.3 (pp. PDF 4)](../../assets/lectures-2025-26/lec55-56-p04-subsequence-limit-proof.jpg)

## Diapositiva impresa 5 (pp. PDF 5) — Acotación en $\mathbb R^n$ — definición 5.2.2

> [!definition] Definición 5.2.2
> 1) Sea $E$ un subconjunto de $\mathbb R^n$. Se dice que es acotado si existe $C>0$ tal que $E\subset V_C(0)$, es decir, $\|x\|<C$ para todo $x\in E$. 2) Sea $f:E\subset\mathbb R^n\to\mathbb R^m$. La aplicación $f$ se dice acotada si su imagen $f(E)$ es acotada en $\mathbb R^m$.
>
> $$
> E\subset V_C(0)\iff\|x\|<C\ \ \forall x\in E
> $$

^def-5-2-2

Nota manuscrita bajo la diapositiva: «es decir, si $f(E)$ es acotado en $\mathbb R^m$».

## Diapositiva impresa 6 (pp. PDF 6) — Acotación como supremo finito

Un conjunto $E\subset\mathbb R^n$ es acotado si y solo si $\sup_{x\in E}\|x\|<+\infty$, y una aplicación $f:E\subset\mathbb R^n\to\mathbb R^m$ es acotada si y solo si $\sup_{x\in E}\|f(x)\|<+\infty$. En particular, una sucesión $\{x^k\}_{k=1}^{\infty}$ es acotada en $\mathbb R^n$ exactamente cuando $\sup_{k\in\mathbb N}\|x^k\|<+\infty$.

$$
\sup_{x\in E}\|x\|<+\infty,\qquad \sup_{x\in E}\|f(x)\|<+\infty
$$

$$
\sup_{k\in\mathbb N}\|x^k\|<+\infty
$$

## Diapositiva impresa 7 (pp. PDF 7) — Acotación y proyecciones

1) Sea $E\subset\mathbb R^n$ y $j\in\{1,\ldots,n\}$. La proyección de $E$ sobre el $j$-ésimo eje es el conjunto $E_j=\{x_j:x\in E\}$. El conjunto $E$ es acotado si y solo si lo son todas sus proyecciones $E_j$, $j=1,\ldots,n$; esto se sigue directamente de la estimación siguiente. 2) En virtud del punto 1, una aplicación $f:E\subset\mathbb R^n\to\mathbb R^n$ es acotada si y solo si lo son todas sus funciones coordenadas. En particular, una sucesión $\{x^k\}$ en $\mathbb R^n$ es acotada exactamente cuando lo son todas sus sucesiones coordenadas.

$$
E_j=\{x_j:\ x\in E\}
$$

$$
|x_j|\le\|x\|\le\sqrt{n}\max_{1\le i\le n}|x_i|
$$

> [!info] Inconsistencia de la fuente y aclaración editorial
> En el punto 2 la diapositiva impresa vuelve a escribir la aplicación como $f:E\subset\mathbb R^n\to\mathbb R^n$, aunque la [[#^def-5-2-2|definición 5.2.2]] y el resto de la exposición toman valores en $\mathbb R^m$. La discrepancia no se corrige en silencio: más abajo se usa la notación $f:E\subset\mathbb R^n\to\mathbb R^m$.

Nota manuscrita: $x=(x_1,x_2,\ldots,x_n)\in E$.

## Diapositiva impresa 8 (pp. PDF 8) — Lema 5.2.2

> [!lemma] Lema 5.2.2
> Toda sucesión $\{x^k\}$ convergente en $\mathbb R^n$ es acotada.

**Demostración manuscrita (en la misma diapositiva).** En efecto, por el [[es/lectures-2025-26/lecture-54#^thm-5-2-1|teorema 5.2.1]] todas las sucesiones coordenadas $\{x_i^k\}$ convergen y por tanto son acotadas (según la teoría unidimensional). Pero entonces, por el punto 2 de la diapositiva anterior, la propia sucesión $\{x^k\}$ es acotada.

## Diapositiva impresa 9 (pp. PDF 9) — Principio de selección de Bolzano–Weierstrass

> [!theorem] Teorema 5.2.4
> Sea $\{x^k\}_{k=1}^{\infty}$ una sucesión en $\mathbb R^n$. Entonces: 1) si es acotada, de ella se puede extraer una subsucesión convergente; 2) si no es acotada, tiene una subsucesión $\{x^{k_i}\}$ que tiende a infinito.

^thm-5-2-4

## Página manuscrita (pp. PDF 10) — Demostración del teorema 5.2.4, parte 1

Sea la sucesión $\{x^k\}$ acotada en $\mathbb R^n$. Entonces todas sus sucesiones coordenadas también son acotadas y para cada una de ellas se puede usar el [[es/lectures-2025-26/lecture-11-12#^thm-2-3-4|principio de Bolzano–Weierstrass]] unidimensional. Se elige de $\{x_1^k\}$ una subsucesión convergente $\{x_1^{k_i}\}$; de $\{x_2^{k_i}\}$ se elige una subsucesión convergente $\{x_2^{s_i}\}$, observando que $\{x_1^{s_i}\}$ también converge por ser subsucesión de la [[es/lectures-2025-26/lecture-08#^def-2-1-3|sucesión convergente]] $\{x_1^{k_i}\}$. Continuando estos razonamientos para las demás sucesiones coordenadas, se obtiene finalmente una subsucesión $\{x^{t_i}\}$ cuyas sucesiones coordenadas convergen todas; entonces $\{x^{t_i}\}$ converge en $\mathbb R^n$ por el [[es/lectures-2025-26/lecture-54#^thm-5-2-1|teorema 5.2.1]].

$$
\{x_1^{k}\}\supset\{x_1^{k_i}\}\supset\{x_1^{s_i}\}\supset\cdots
$$

![Selección diagonal de una subsucesión (pp. PDF 10)](../../assets/lectures-2025-26/lec55-56-p10-bolzano-weierstrass-proof.jpg)

## Página manuscrita (pp. PDF 11) — Esquema de la selección diagonal

La página contiene un esquema de selección correspondiente a la demostración anterior. El vector se escribe por coordenadas; en azul se rodean los términos de la primera sucesión coordenada de la que se extrae la subsucesión convergente; en verde se muestra el retorno a los índices elegidos, adelgazando la primera sucesión coordenada para conservar solo los índices usados en la segunda coordenada. Más abajo se repite el mismo procedimiento para la tercera coordenada; en rojo se marca el siguiente paso de adelgazamiento.

$$
x^k=\left(x_1^k,x_2^k,\ldots,x_n^k\right)
$$

![Esquema de la selección diagonal (pp. PDF 11)](../../assets/lectures-2025-26/lec55-56-p11-diagonal-subsequence-diagram.jpg)

## Página manuscrita (pp. PDF 12) — Demostración del teorema 5.2.4, parte 2

Como la sucesión numérica $\{\|x^k\|\}_{k=1}^{\infty}$ no está [[es/lectures-2025-26/lecture-05-06#^def-1-3-7|acotada superiormente]], tiene una subsucesión $\{\|x^{k_i}\|\}_{i=1}^{\infty}$ que tiende a $+\infty$. Entonces

$$
\lim_{i\to\infty}\|x^{k_i}\|=+\infty\ \Longrightarrow\ \lim_{i\to\infty}x^{k_i}=\infty.
$$

## Diapositiva impresa 10 (pp. PDF 13) — Criterio de Bolzano–Cauchy

> [!theorem] Teorema 5.2.5
> Sea $\{x^k\}_{k=1}^{\infty}$ una sucesión en $\mathbb R^n$. Entonces son equivalentes las afirmaciones: 1) la sucesión $\{x^k\}$ converge en $\mathbb R^n$; 2) para todo $\varepsilon>0$ existe $N\in\mathbb N$ tal que $\|x^k-x^m\|<\varepsilon$ para todos $k,m>N$.

^thm-5-2-5

**Observación.** Una sucesión en $\mathbb R^n$ que cumple la condición 2 se llama [[es/lectures-2025-26/lecture-13#^def-2-3-10|sucesión de Cauchy]].

$$
\forall\varepsilon>0\ \ \exists N\in\mathbb N\ \ \forall k,m>N:\ \|x^k-x^m\|<\varepsilon
$$

## Página manuscrita (pp. PDF 14) — Demostración de 1) ⇒ 2)

Por el [[es/lectures-2025-26/lecture-54#^thm-5-2-1|teorema 5.2.1]] todas las sucesiones coordenadas $\{x_i^k\}$ convergen y, por el criterio de Bolzano–Cauchy unidimensional, son de Cauchy. Por ello, dado $\varepsilon>0$, se puede elegir $N\in\mathbb N$ tal que para todo $i\in\{1,\ldots,n\}$

$$
|x_i^k-x_i^m|<\frac{\varepsilon}{\sqrt n}
$$

para todos $k,m\ge N$. De aquí, por la desigualdad (5.2.1)

$$
|x_i|\le\|x\|\le\sqrt{n}\max_{1\le i\le n}|x_i|,
$$

es decir,

$$
\|x^k-x^m\|\le\sqrt{n}\max_{1\le i\le n}|x_i^k-x_i^m|<\sqrt n\,\frac{\varepsilon}{\sqrt n}=\varepsilon,
$$

obtenemos $\|x^k-x^m\|<\varepsilon$, lo que da la afirmación 2.

![Demostración del criterio de Bolzano–Cauchy (pp. PDF 14)](../../assets/lectures-2025-26/lec55-56-p14-cauchy-criterion-proof.jpg)

## Página manuscrita (pp. PDF 15) — Demostración de 2) ⇒ 1)

La condición 2 significa que $\forall\varepsilon>0$ $\exists N\in\mathbb N$ $\forall k,m\in\mathbb N$ se cumple $\|x^k-x^m\|<\varepsilon$. En virtud de (5.2.1), para todos $k,m\in\mathbb N$ e $i\in\{1,\ldots,n\}$,

$$
|x_i^k-x_i^m|\le\|x^k-x^m\|<\varepsilon.
$$

Por tanto la condición 2 implica que las sucesiones coordenadas $\{x_i^k\}$ son de Cauchy. Por el criterio de Bolzano–Cauchy unidimensional todas convergen en $\mathbb R$, y entonces, por el [[es/lectures-2025-26/lecture-54#^thm-5-2-1|teorema 5.2.1]], la sucesión $\{x^k\}$ converge en $\mathbb R^n$.

## Diapositiva impresa 11 (pp. PDF 16) — Puntos de acumulación y puntos aislados

> [!definition] Definición 5.2.3
> Sea $E\subset\mathbb R^n$. 1) El punto $a\in\overline{\mathbb R^n}$ se llama punto de acumulación de $E$ si para todo $\varepsilon>0$ el conjunto $E\cap\dot V_\varepsilon(a)$ no es vacío. 2) El punto $a\in E$ se llama aislado para $E$ si no es punto de acumulación de $E$.
>
> $$
> E\cap\dot V_\varepsilon(a)\ne\varnothing
> $$

^def-5-2-3

> [!note] Discrepancia de la capa de texto
> Aquí y en adelante la capa de texto pierde los puntos sobre los símbolos de [[es/lectures-2025-26/lecture-14#^def-2-4-2|entorno perforado]] y las barras superiores: la línea impresa tiene $\dot V_\varepsilon(a)$ y $a\in\overline{\mathbb R^n}$, mientras que el texto extraído da $V_\varepsilon(a)$ y $a\in\mathbb R^n$.

## Diapositiva impresa 12 (pp. PDF 17) — Caracterización de los puntos de acumulación

> [!theorem] Teorema 5.2.6
> Sean $E\subset\mathbb R^n$ y $a\in\overline{\mathbb R^n}$. Entonces son equivalentes las afirmaciones: 1) el punto $a$ es punto de acumulación de $E$; 2) existe una sucesión $\{x^k\}_{k=1}^{\infty}$ en $E\setminus\{a\}$ tal que $\lim_{k\to\infty}x^k=a$.

^thm-5-2-6

## Página manuscrita (pp. PDF 18) — Demostración del teorema 5.2.6

La demostración se realiza solo para $a\in\mathbb R^n$; el caso $a=\infty$ queda como ejercicio. 1) ⇒ 2) Sea $a$ un punto de acumulación de $E$, es decir, $\forall\varepsilon>0$ el conjunto $E\cap\dot V_\varepsilon(a)\ne\varnothing$. Entonces para cada $k$ existe un punto $x^k\in E\setminus\{a\}$ con $\|x^k-a\|<1/k$. De aquí $\lim_{k\to\infty}\|x^k-a\|=0$, es decir, $\lim_{k\to\infty}x^k=a$. 2) ⇒ 1) Sea $\{x^k\}_{k=1}^{\infty}$ una sucesión en $E\setminus\{a\}$ que converge a $a$. Para todo $\varepsilon>0$ existe $k\in\mathbb N$ con $\|x^k-a\|<\varepsilon$. Por ello $x^k\in V_\varepsilon(a)\cap\left(E\setminus\{a\}\right)$, es decir, $x^k\in\dot V_\varepsilon(a)\cap E$. Entonces para todo $\varepsilon>0$ el conjunto $E\cap\dot V_\varepsilon(a)\ne\varnothing$, así que $a$ es punto de acumulación de $E$.

$$
\forall\varepsilon>0\ \ E\cap\dot V_\varepsilon(a)\ne\varnothing
$$

$$
\|x^k-a\|<\frac1k,\qquad x^k\in E\setminus\{a\}
$$

## Diapositiva impresa 13 (pp. PDF 19) — §3. Conjuntos abiertos, cerrados y compactos

> [!definition] Definición 5.3.1
> Sea $E\subset\mathbb R^n$. 1) El punto $a\in E$ se llama interior para $E$ si tiene un entorno contenido en $E$. 2) El conjunto $E$ se llama abierto en $\mathbb R^n$ si cada uno de sus puntos es interior para $E$. 3) El conjunto $E$ se llama cerrado en $\mathbb R^n$ si su complementario $\mathbb R^n\setminus E$ es abierto en $\mathbb R^n$.

^def-5-3-1

**Observación.** El complementario de cualquier [[#^def-5-3-1|conjunto abierto]] en $\mathbb R^n$ es a su vez cerrado; así pues, los [[#^thm-5-3-1|conjuntos cerrados]] y los abiertos son mutuamente complementarios.

Esquema manuscrito en la diapositiva: se dibuja un conjunto $E$ con un punto interior $a$ y su entorno $V(a)\subset E$; se marca aparte un [[es/lectures-2025-26/lecture-57-58#Diapositiva impresa 5 (pp. PDF 7) — La frontera de un conjunto — definición 5.3.4|punto frontera]] que no es interior.

$$
V(a)\subset E
$$

![Definición 5.3.1 y un punto interior (pp. PDF 19)](../../assets/lectures-2025-26/lec55-56-p19-open-set-interior.jpg)

## Diapositiva impresa 14 (pp. PDF 20) — Caracterización de los conjuntos cerrados

> [!theorem] Teorema 5.3.1
> Sea $E\subset\mathbb R^n$. Entonces son equivalentes las afirmaciones: 1) $E$ es cerrado en $\mathbb R^n$; 2) $E$ contiene todos sus puntos de acumulación en $\mathbb R^n$; 3) si $\{x^k\}_{k=1}^{\infty}$ es una sucesión convergente en $E$, entonces $\lim_{k\to\infty}x^k\in E$.

^thm-5-3-1

## Página manuscrita (pp. PDF 21) — Demostración del teorema 5.3.1

La demostración sigue el esquema 1) ⇒ 3) ⇒ 2) ⇒ 1). 1) ⇒ 3): sea $\{x^k\}$ una sucesión en $E$, $a\in\mathbb R^n$, $\lim_{k\to\infty}x^k=a$; probemos que $a\in E$. Si no es así, es decir, $a\notin E$, entonces de la cerradez de $E$ se sigue la existencia de un entorno $V(a)\subset\mathbb R^n\setminus E$. Por la definición de límite, para todo $k\in\mathbb N$ suficientemente grande se tiene $x^k\in V(a)\subset\mathbb R^n\setminus E$; por otra parte, para todo $k\in\mathbb N$ se tiene $x^k\in E$ — contradicción. 3) ⇒ 2): sea $a\in\mathbb R^n$ un punto de acumulación de $E$. Por el [[#^thm-5-2-6|teorema 5.2.6]] existe una sucesión $\{x^k\}\subset E$ que converge a $a$; entonces, en virtud de 3), obtenemos $a\in E$. 2) ⇒ 1): probemos que $\mathbb R^n\setminus E$ es abierto. Sea $a\in\mathbb R^n\setminus E$; comprobemos que existe un entorno $V(a)\subset\mathbb R^n\setminus E$. Si no es así, entonces para todo $\varepsilon>0$ el conjunto $\dot V_\varepsilon(a)\cap E\ne\varnothing$, es decir, $a$ es punto de acumulación de $E$ y, por 2), $a\in E$ — contradicción.

$$
\mathbb R^n\setminus E
$$

## Diapositiva impresa 15 (pp. PDF 22) — Teorema 5.3.2 sobre familias de conjuntos

> [!theorem] Teorema 5.3.2
> Sea $A$ un conjunto de índices y sean $\{E_\alpha\}_{\alpha\in A}$ y $\{F_\alpha\}_{\alpha\in A}$ familias de subconjuntos abiertos y cerrados de $\mathbb R^n$ respectivamente. Entonces: 1) la unión de todos los $E_\alpha$ es abierta y la intersección de todos los $F_\alpha$ es cerrada en $\mathbb R^n$; 2) si el conjunto de índices $A$ es finito, entonces la intersección de todos los $E_\alpha$ es abierta y la unión de todos los $F_\alpha$ es cerrada en $\mathbb R^n$.

**Corolario.** Sean $E$ abierto y $F$ cerrado en $\mathbb R^n$. Entonces $E\setminus F$ es abierto y $F\setminus E$ es cerrado en $\mathbb R^n$.

$$
\bigcup_{\alpha\in A}E_\alpha,\qquad \bigcap_{\alpha\in A}F_\alpha
$$

$$
E\setminus F,\qquad F\setminus E
$$

## Página manuscrita (pp. PDF 23) — Demostración del teorema 5.3.2, parte 1

Pongamos $E:=\bigcup_{\alpha\in A}E_\alpha$ y $F:=\bigcap_{\alpha\in A}F_\alpha$. Si $a\in E$, entonces $a\in E_\alpha$ para cierto $\alpha\in A$; como $E_\alpha$ es abierto y $a\in E_\alpha$, existe un entorno $V(a)\subset E_\alpha$ y, por tanto, $V(a)\subset E$, es decir, $E$ es abierto. Para probar que $F$ es cerrado, observemos que por la regla de de Morgan

$$
\mathbb R^n\setminus F=\mathbb R^n\setminus\bigcap_{\alpha\in A}F_\alpha=\bigcup_{\alpha\in A}\left(\mathbb R^n\setminus F_\alpha\right).
$$

Cada conjunto $\mathbb R^n\setminus F_\alpha$ es abierto por el punto 1, al ser el complementario del cerrado $F_\alpha$, por lo que su unión es abierta; en consecuencia, $F$ es cerrado.

## Página manuscrita (pp. PDF 24) — Demostración del teorema 5.3.2, parte 2

Sea el conjunto de índices $A$ finito y $E:=\bigcap_{\alpha\in A}E_\alpha$. Si $a\in E$, entonces $a\in E_\alpha$ para todo $\alpha\in A$; como cada $E_\alpha$ es abierto, para cada $\alpha\in A$ existe $\delta_\alpha>0$ con $V_{\delta_\alpha}(a)\subset E_\alpha$. Pongamos $\delta:=\min_{\alpha\in A}\delta_\alpha$; como $A$ es finito, este mínimo existe y es positivo. Entonces $V_\delta(a)\subset E_\alpha$ para todo $\alpha\in A$, es decir, $V_\delta(a)\subset E$, y $E$ es abierto. La cerradez de la unión $\bigcup_{\alpha\in A}F_\alpha$ se deduce de la apertura de $E$ mediante la regla de de Morgan de manera análoga al punto 1.

$$
\delta:=\min_{\alpha\in A}\delta_\alpha>0,\qquad V_\delta(a)\subset E_\alpha\ \ \forall\alpha\in A
$$

## Página manuscrita (pp. PDF 25) — Demostración del corolario del teorema 5.3.2

Se tiene $E\setminus F=E\cap\left(\mathbb R^n\setminus F\right)$. El conjunto $\mathbb R^n\setminus F$ es abierto porque $F$ es cerrado, por lo que, por el [[#Diapositiva impresa 15 (pp. PDF 22) — Teorema 5.3.2 sobre familias de conjuntos|teorema 5.3.2]], la intersección de dos conjuntos abiertos es abierta y $E\setminus F$ es abierto. La segunda afirmación se demuestra de manera análoga.

$$
E\setminus F=E\cap\left(\mathbb R^n\setminus F\right)
$$

## Diapositiva impresa 16 (pp. PDF 26) — Ejemplos

1) Los conjuntos $\mathbb R^n$ y $\varnothing$ son a la vez abiertos y cerrados en $\mathbb R^n$. 2) Todo subconjunto finito de $\mathbb R^n$ es cerrado. 3) Sean $a\in\mathbb R^n$, $\delta>0$ y pongamos $\overline{B_\delta(a)}=\{x\in\mathbb R^n:\|x-a\|\le\delta\}$. Entonces el conjunto $B_\delta(a)$ es abierto en $\mathbb R^n$ y el conjunto $\overline{B_\delta(a)}$ es cerrado en $\mathbb R^n$. 4) Sean $a\in\mathbb R^n$, $\delta>0$ y pongamos $S_\delta(a)=\{x\in\mathbb R^n:\|x-a\|=\delta\}$. Entonces $S_\delta(a)$ es cerrado en $\mathbb R^n$.

>
> **Inconsistencia de la fuente y aclaración editorial.** En la capa de texto del PDF los puntos 3.1 y 3.2 aparecen sin las barras, es decir, como «$B_\delta(a)$ es abierto» y «$B_\delta(a)$ es cerrado», lo que no puede cumplirse simultáneamente. Según la imagen de la página, la primera aparición es la bola abierta $B_\delta(a)$ y la segunda es la bola cerrada $\overline{B_\delta(a)}$; más abajo se usa esa lectura y la discrepancia se declara aquí explícitamente.

Notas manuscritas: «bola en $\mathbb R^n$» junto al símbolo $\overline{B_\delta(a)}$, «esfera en $\mathbb R^n$» junto a $S_\delta(a)$, la fórmula $S_\delta(a)=\overline{B_\delta(a)}\setminus B_\delta(a)$ y una anotación en azul: «Importante: si $E\subset\mathbb R^n$, $E$ es a la vez abierto y cerrado, entonces o bien $E=\mathbb R^n$, o bien $E=\varnothing$».

$$
S_\delta(a)=\overline{B_\delta(a)}\setminus B_\delta(a)
$$

![Ejemplos de conjuntos abiertos y cerrados (pp. PDF 26)](../../assets/lectures-2025-26/lec55-56-p26-ball-sphere-examples.jpg)

## Página manuscrita (pp. PDF 27) — Ejemplo 3: apertura de la bola $B_\delta(a)$

Probemos que $B_\delta(a)$ es abierto en $\mathbb R^n$. Sea $b\in B_\delta(a)$; hay que comprobar que $b$ es punto interior de $B_\delta(a)$. Pongamos $\sigma:=\delta-\|b-a\|>0$; este número es positivo porque $B_\delta(a)=\{x\in\mathbb R^n:\|x-a\|<\delta\}$ y $b\in B_\delta(a)$, es decir, $\|b-a\|<\delta$. Consideremos la bola $B_\sigma(b)$. Para todo $x\in B_\sigma(b)$ se tiene

$$
\|x-a\|=\|x-b+b-a\|\le\|x-b\|+\|b-a\|<\sigma+\|b-a\|=\delta,
$$

por lo que $x\in B_\delta(a)$, es decir, $B_\sigma(b)\subset B_\delta(a)$. Así pues, $b$ es punto interior y $B_\delta(a)$ es abierto.

$$
\sigma:=\delta-\|b-a\|>0,\qquad \|x-a\|\le\|x-b\|+\|b-a\|<\sigma+\|b-a\|=\delta
$$

## Página manuscrita (pp. PDF 28) — Ejemplo 3: cerradez de $\overline{B_\delta(a)}$ y una observación

Sea $\{x^k\}$ una sucesión en $\overline{B_\delta(a)}$ que converge a $x\in\mathbb R^n$. Entonces

$$
\|x-a\|=\lim_{k\to\infty}\|x^k-a\|\le\delta,
$$

así que $x\in\overline{B_\delta(a)}$ y $\overline{B_\delta(a)}$ es cerrado. Nota en azul al pie: «Importante: el conjunto $[0,1)$ no es ni abierto ni cerrado en $\mathbb R$, es decir, no hay que pensar que todo subconjunto de $\mathbb R^n$ sea abierto o cerrado».

## Diapositiva impresa 17 (pp. PDF 29) — La clausura de un conjunto

> [!definition] Definición 5.3.2
> Sea $E\subset\mathbb R^n$. Se llama clausura de $E$ al conjunto cerrado $F\subset\mathbb R^n$ que satisface dos condiciones: 1) $F\supset E$; 2) si $A$ es otro subconjunto cerrado de $\mathbb R^n$ que contiene $E$, entonces $A\supset F$. La clausura de $E$ se denota habitualmente por $\overline E$ o $\operatorname{Cl}E$.

^def-5-3-2

**Observación.** $\overline E$ es el menor conjunto cerrado que contiene a $E$ respecto de la inclusión. Además, se cumple la igualdad siguiente.

$$
\overline E=\bigcap\{F\subset\mathbb R^n:\ F\supset E,\ F=\overline F\}
$$

## Diapositiva impresa 18 (pp. PDF 30) — Descripción de la clausura

La descripción anterior es incómoda para fines prácticos, por lo que la caracterización de la [[#^def-5-3-2|clausura]] se formula en términos de sucesiones y puntos de acumulación.

> [!theorem] Teorema 5.3.3
> Sean $E\subset\mathbb R^n$ y $a\in\mathbb R^n$. Entonces son equivalentes las afirmaciones: 1) $a\in\overline E$; 2) el punto $a$ pertenece a $E$ o es punto de acumulación de $E$; 3) existe en $E$ una sucesión que converge a $a$.
>
> $$
> a\in\overline E
> $$

^thm-5-3-3

## Página manuscrita (pp. PDF 31) — Demostración del teorema 5.3.3

La demostración sigue el esquema 1) ⇒ 2) ⇒ 3) ⇒ 1). 1) ⇒ 2): si $a\notin E$ y $a$ no es punto de acumulación de $E$, entonces existe $\delta>0$ tal que $V_\delta(a)\subset\mathbb R^n\setminus E$. Reescribamos esta inclusión como $E\subset\mathbb R^n\setminus V_\delta(a)$. De aquí, en virtud de la cerradez de $\mathbb R^n\setminus V_\delta(a)$, se sigue que $\overline E\subset\mathbb R^n\setminus V_\delta(a)$. Pero esto es imposible, ya que $a\in\overline E$. 2) ⇒ 3): si $a$ es punto de acumulación de $E$, la sucesión requerida existe por el teorema sobre la caracterización de los puntos de acumulación; en el caso $a\in E$ sirve la sucesión constante cuyos términos son todos iguales a $a$. 3) ⇒ 1): sea $\{x^k\}$ una sucesión en $E$ que converge a $a$. Entonces $\{x^k\}\subset\overline E$ por el [[#^thm-5-3-1|teorema 5.3.1]], de donde $a\in\overline E$.

$$
\overline E\subset\mathbb R^n\setminus V_\delta(a)
$$

![Demostración del teorema 5.3.3 (pp. PDF 31)](../../assets/lectures-2025-26/lec55-56-p31-closure-criterion-proof.jpg)

---

[[es/lectures-2025-26/lecture-54|← Lección 54]] · [[es/lectures-2025-26/index|Índice de lecciones]] · [[es/lectures-2025-26/lecture-57-58|Lecciones 57–58 →]] · [[es/term-index|Términos y teoremas]] · [[ru/lectures-2025-26/lecture-55-56|Русский]] · [[en/lectures-2025-26/lecture-55-56|English]]

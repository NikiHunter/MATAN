---
title: "Lecciones 49–50 — Convergencia absoluta y criterios de Dirichlet y Abel"
lang: es
course: "Análisis matemático, 2025/26"
lecture: 49-50
semester: 2
date: 2026-04-09
source: "ma25_26-lectures_49-50_notes.pdf"
pdf_pages: 14
typed_slides: 10
archive_file: "Лекция 49-50.md"
---
# Lecciones 49–50 — Convergencia absoluta y criterios de Dirichlet y Abel

[← Lecciones 47–48](lecture-47-48.md) · [Índice de lecciones](index.md) · [Lecciones 51–52 →](lecture-51-52.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-49-50.md) · [English](../../en/lectures-2025-26/lecture-49-50.md) · [Continuación: lecciones 51–52](../../../source/MathInMind/МАТАН_Л/Лекция%2051-52.md)

> **Fuente:** `ma25_26-lectures_49-50_notes.pdf` — 14 páginas PDF, 10 diapositivas impresas; la fecha impresa es 9 de abril de 2026. Páginas impresas: 1–7, 9, 12 y 14. Páginas manuscritas: 8, 10–11 y 13. Todas se enumeran una sola vez. Las anotaciones manuscritas en las diapositivas 6 y 7 se señalan por separado.
>
> **Duplicación del semestre 2.** El semestre 1 termina con la lección 32; el semestre 2 abarca las lecciones 33–64. El contenido coincide con [§4.5, «Integrales impropias»](../../ru/lectures/06-improper-integrals-4-5.md) y también forma parte del [registro del semestre 2](../../ru/lectures/index.md). Se conserva, sin renombrarlo, el original archivado [«Лекция 49-50.md»](../../../source/MathInMind/МАТАН_Л/Лекция%2049-50.md). Este enlace no sustituye la transcripción independiente completa.
>
> **Límites y condiciones.** La convergencia de una [integral impropia](lecture-47-48.md#def-4-5-2) significa un límite unilateral ordinario y finito. No se presupone [valor principal](../09-improper-integrals-applications.md#sec-9-1) de Cauchy. En una singularidad interior o bilateral hay que verificar por separado cada lado; no se aplica [Newton–Leibniz](lecture-43-44.md#thm-4-3-2) a través de una singularidad sin demostración.

## Diapositiva impresa 1 (PDF p. 1). Portada

«Análisis matemático», lecciones 49–50, 9 de abril de 2026; D. E. Apushkinskaya, Universidad RUDN.

## Diapositiva impresa 2 (PDF p. 2). Cita e ilustración

«Una integral en la que aparece el infinito se llama integral impropia. No es un nombre muy acertado, porque las demás integrales tampoco pertenecen a nadie».

En la caricatura original, un gran signo integral sostiene el símbolo del infinito y dice: «¡Pobres huérfanas!»; los signos integrales pequeños gritan: «¡Ay!». La ilustración procede del PDF y no se ha redibujado.

![Caricatura original sobre integrales impropias, diapositiva impresa 2 (PDF p. 2)](../../assets/lectures-2025-26/lec49-50-p02-improper-integral-cartoon.jpg)

## Diapositiva impresa 3 (PDF p. 3). Objetivos

Integrales impropias; sustitución e [integración por partes](lecture-37-38.md#thm-4-1-4) para integrales impropias; criterios de convergencia; [convergencia absoluta](../04-numeric-series.md#sec-4-3); criterios de Dirichlet y Abel.

## Capítulo 4, §5. Integrales impropias

### Diapositiva impresa 4 (PDF p. 4). Observaciones sobre convergencia

1. Las integrales de funciones no negativas equivalentes cerca de una singularidad convergen o divergen simultáneamente.
2. Que converja $`\int_a^{+\infty}f`$ no implica que $`f(x)\to0`$ cuando $`x\to+\infty`$, aunque $`f\ge0`$ y sea continua.
3. La acotación de las integrales parciales es necesaria, pero no suficiente. Por ejemplo, $`\int_0^{+\infty}\cos x\,dx`$ diverge porque $`\int_0^A\cos x\,dx=\sin A`$ no tiene límite cuando $`A\to+\infty`$.

### Diapositiva impresa 5 (PDF p. 5). Definición de convergencia absoluta

<a id="def-4-5-4"></a>**Definición 4.5.4.** Sean $`-\infty<a<b\le+\infty`$, $`f\in\mathcal R_{loc}[a,b)`$. La integral $`\int_a^b f`$ converge absolutamente si converge $`\int_a^b|f|`$.

### Diapositiva impresa 6 (PDF p. 6). Propiedades de convergencia absoluta

1. Si $`\int_a^b f`$ y $`\int_a^b g`$ convergen absolutamente y $`\alpha,\beta\in\mathbb R`$, entonces $`\int_a^b(\alpha f+\beta g)`$ converge absolutamente. Una nota manuscrita en la diapositiva indica

```math
|\alpha f+\beta g|\le|\alpha|\,|f|+|\beta|\,|g|,
```

y luego aplica el criterio de comparación.

2. Si $`\int_a^b f`$ existe en la [recta real ampliada](lecture-05-06.md#def-1-3-4), entonces

```math
\left|\int_a^b f\right|\le\int_a^b|f|.
```

### Diapositiva impresa 7 (PDF p. 7). Convergencia ordinaria y absoluta

<a id="lem-4-5-6"></a>**Lema 4.5.6.** La convergencia absoluta implica convergencia.

1. La recíproca es falsa: una integral puede converger sin hacerlo absolutamente.
2. Si una integral converge, pero no absolutamente, se llama condicionalmente (o no absolutamente) convergente.
3. Si $`\int_a^b f`$ converge condicionalmente y $`\int_a^b g`$ converge absolutamente, entonces $`\int_a^b(f+g)`$ converge condicionalmente. La diapositiva señala la identidad $`f=(f+g)-g`$.

### Página manuscrita (PDF p. 8). Demostración del lema 4.5.6

Sea $`\varepsilon>0`$. Por el [criterio de Cauchy](lecture-13.md#thm-2-3-7) para la convergencia absoluta, elijamos $`\Delta\in(a,b)`$ de modo que, para todos $`A,B\in(\Delta,b)`$ con $`A<B`$,

```math
\int_A^B|f|<\varepsilon.
```

Entonces

```math
\left|\int_A^Bf\right|\le\int_A^B|f|<\varepsilon,
```

así que se cumple el criterio de Cauchy para $`\int_a^b f`$ y la integral original converge.

### Diapositiva impresa 8 (PDF p. 9). Criterio de Dirichlet

<a id="thm-4-5-4"></a>**Teorema 4.5.4.** Sean $`f\in C([a,b))`$, $`g\in C^1([a,b))`$ y $`g`$ monótona. Supóngase que

1. $`g(x)\to0`$ cuando $`x\to b-`$;
2. existe $`M>0`$ tal que

```math
\left|\int_a^Bf(x)\,dx\right|\le M\qquad\text{para todo }B<b,
```

Entonces converge la integral impropia $`\int_a^{\to b}f(x)g(x)\,dx`$.

### Páginas manuscritas (PDF pp. 10–11). Demostración del criterio de Dirichlet

Sea $`F(x)=\int_a^x f`$, de modo que $`F(a)=0`$ y $`|F(x)|\le M`$. Para todo $`B<b`$ finito, la integración por partes da

```math
\int_a^Bfg=F(B)g(B)-\int_a^BFg'.
```

El primer término tiende a cero, pues $`F`$ está acotada y $`g(B)\to0`$. Como $`g`$ es [diferenciable](lecture-22-23.md#def-3-2-1) y monótona, su [derivada](lecture-22-23.md#def-3-1-1) $`g'`$ tiene signo constante. Por tanto,

```math
\int_a^{\to b}|Fg'|
\le M\int_a^{\to b}|g'|
=M\left|g(b-)-g(a)\right|<+\infty.
```

Así, $`\int Fg'`$ converge absolutamente, y la integración por partes demuestra la convergencia de $`\int fg`$. Las páginas manuscritas justifican explícitamente el término del extremo y la convergencia absoluta de la integral con $`Fg'`$.

### Diapositiva impresa 9 (PDF p. 12). Criterio de Abel

<a id="thm-4-5-5"></a>**Teorema 4.5.5.** Sean $`f\in C([a,b))`$, $`g\in C^1([a,b))`$ y $`g`$ monótona. Si $`g`$ está acotada y converge $`\int_a^{\to b}f(x)\,dx`$, entonces converge $`\int_a^{\to b}f(x)g(x)\,dx`$.

### Página manuscrita (PDF p. 13). Demostración del criterio de Abel

Una función monótona y acotada tiene un límite finito $`\alpha=\lim_{x\to b-}g(x)`$. La función $`g-\alpha`$ es monótona y tiende a cero; las integrales parciales $`F(B)=\int_a^Bf`$ están acotadas porque converge la integral de $`f`$. Por el [criterio de Dirichlet](#thm-4-5-4) converge $`\int_a^{\to b}f(g-\alpha)`$. Por hipótesis también converge $`\alpha\int_a^{\to b}f`$. Al sumarlas,

```math
\int_a^{\to b}fg
=\int_a^{\to b}f(g-\alpha)+\alpha\int_a^{\to b}f
```

converge.

### Diapositiva impresa 10 (PDF p. 14). Hipótesis más débiles

Los [teoremas 4.5.4](#thm-4-5-4) y [4.5.5](#thm-4-5-5) siguen siendo válidos bajo hipótesis menos restrictivas: $`f\in\mathcal R_{loc}([a,b))`$ y $`g`$ es monótona en $`[a,b)`$.

---

**Navegación:** [Lecciones 47–48](lecture-47-48.md) · [Índice](index.md) · [Lecciones 51–52 archivadas](../../../source/MathInMind/МАТАН_Л/Лекция%2051-52.md) · [Fuente e ilustraciones](../../assets/lectures-2025-26/provenance-45-50.md).

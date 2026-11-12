---
title: "Seminario NM-204, semestre 3 — soluciones de las tareas"
lang: es
---
# Seminario NM-204, semestre 3: soluciones de las tareas

[Русский](../../ru/seminar-sem3/index.md) · [English](../../en/seminar-sem3/index.md) · **Español**

[Índice del curso](../index.md) · [Lecciones 2025/26](../lectures-2025-26/index.md) · [Examen, semestre 3 (en ruso)](../../ru/exam-sem3/EXAM_SEM3.md)

Soluciones de las tareas 1–4 de la asignatura «Análisis matemático» (NM-204, 2026). Cada problema tiene la misma estructura: enunciado breve, solución o demostración, respuesta y un párrafo **«Por qué funciona»** que explica en qué se apoya el resultado y qué ocurre si se cambian las hipótesis. Los enunciados se cotejaron con los PDF originales (que están en ruso); las respuestas numéricas y los desarrollos se comprobaron por sustitución.

Los problemas pasan de una tarea a la siguiente con los mismos números, así que cada uno está resuelto una sola vez.

| Tarea | Archivo | Problemas | Tema |
|---|---|---|---|
| Tarea 1 | [Fórmula de Taylor](hw1-taylor.md) | 1.1–1.4 | polinomio de Taylor en $`\mathbb R^n`$, resto de Lagrange |
| Tarea 2 | [Extremos condicionados](hw2-conditional-extremum.md) | 2.1–2.3, 2'.1–2'.3 | multiplicadores de Lagrange, condiciones suficientes |
| Tarea 3 | [Series numéricas](hw3-numerical-series.md) | 3.1–3.11 | comparación, Kummer, d'Alembert, Raabe |
| Tarea 4 | [Series, desigualdades, bases](hw4-series-inequalities-bases.md) | 4.1–4.12 | Hölder, bases, criterios en forma límite, criterio integral, Leibniz |

**Control 1.** [Cómo prepararse](test1-guide.md): la estructura probable, métodos para cada ejercicio, errores típicos y un plan de tres días; [variantes de práctica](test1-variants.md): tres variantes con el formato 1.1, 1.2, 2.1, 2.2, 3, 4 y sus soluciones.

## Respuestas en una página

**Tarea 1.** Notación: $`h`$ es el incremento desde el punto del desarrollo.

- 1.1. En $`(1;1;1)`$: $`3(h_1^2+h_2^2+h_3^2-h_1h_2-h_1h_3-h_2h_3)+h_1^3+h_2^3+h_3^3-3h_1h_2h_3`$. En $`(1;-1;2)`$: $`14+9h_1-3h_2+15h_3+3h_1^2-3h_2^2+6h_3^2-6h_1h_2+3h_1h_3-3h_2h_3+h_1^3+h_2^3+h_3^3-3h_1h_2h_3`$.
- 1.2. $`322-448h_1-42h_2+254h_1^2+94h_1h_2+36h_2^2-60h_1^3-16h_1^2h_2+24h_1h_2^2+24h_2^3+5h_1^4-4h_1^2h_2^2+3h_2^4`$.
- 1.3. $`e^9\bigl[1+L+\bigl(\tfrac{L^2}2+Q\bigr)+\bigl(\tfrac{L^3}6+LQ\bigr)\bigr]+R_3`$, donde $`L=-2h_2+6h_3`$, $`Q=h_1h_2+h_3^2`$, $`R_3=\tfrac1{24}e^{9+L\theta+Q\theta^2}\bigl[(L+2Q\theta)^4+12Q(L+2Q\theta)^2+12Q^2\bigr]`$.
- 1.4. $`e^{\pi+2}\bigl[-\pi h_1+h_2+2\pi h_1^2+h_2^2-(3+\pi)h_1h_2-\pi h_1h_3+h_2h_3\bigr]+R_2`$; el resto $`R_2=\tfrac16d^3_cf(h)`$ está escrito en la solución.

**Tarea 2.**

- 2.1. $`(0;0)`$ es un máximo local condicionado ($`f=0`$), $`(1;1)`$ un mínimo local condicionado ($`f=-1`$).
- 2.2. $`\pm\sqrt{a/6}\,(1;1;1)`$: máximo $`e^{\sqrt{6a}}`$ y mínimo $`e^{-\sqrt{6a}}`$.
- 2.3. No hay puntos de extremo condicionado (hay puntos estacionarios, pero estorba el sumando $`2x^3`$). En la variante con $`y^2`$ la respuesta es otra; se trata en una observación.
- 2'.1. $`\max=\frac1{3\sqrt6}`$ en $`\frac1{\sqrt6}(1;1;2)`$, $`\frac1{\sqrt6}(1;-2;-1)`$, $`\frac1{\sqrt6}(-2;1;-1)`$; $`\min=-\frac1{3\sqrt6}`$ en los puntos opuestos.
- 2'.2. Para $`m=1`$ la función es constante sobre $`M`$. Para $`n,m\ge2`$ el único punto de extremo es $`(\frac an;\dots;\frac an)`$, un mínimo $`\frac{a^m}{n^{m-1}}`$ (global si $`m`$ es par, local si es impar).
- 2'.3. Un máximo local en $`x_k=\frac{a\,m_k}{m_1+\dots+m_n}`$; además, los puntos con coordenadas nulas para los que todos los $`m_k`$ correspondientes son pares son extremos con valor $`0`$.

**Tarea 3.**

- 3.3. La serie $`\sum\cos(kx_0)`$ diverge siempre; las sumas parciales están acotadas si y solo si $`x_0\notin2\pi\mathbb Z`$.
- 3.7 y 3.9. Criterio de Kummer con $`x_n=1`$ y $`x_n=n`$.
- 3.10. El ejemplo es la serie de 3.8.
- 3.11. Converge si y solo si $`\alpha>1`$.

**Tarea 4.**

- 4.1. Máximo $`1`$ en $`x_k=b_k^{\,p'-1}`$; mínimo $`\min_kb_k`$ en los vértices $`e_j`$ (o $`0`$ en la cara donde $`b_k=0`$).
- 4.5. $`a_{2m}=\frac1{m!}`$, $`a_{2m-1}=\bigl(1+\frac1{2m-1}\bigr)\frac1{m!}`$.
- 4.7. Las dos primeras series convergen, la tercera diverge ($`c_k\to1`$).
- 4.8. $`\sum a_k`$ converge para $`\alpha>\frac12`$; $`\sum b_k`$ converge para $`\beta<e`$.
- 4.9. $`\sum a_k`$ y $`\sum d_k`$ convergen, $`\sum b_k`$ y $`\sum c_k`$ divergen.
- 4.11$`^*`$. Sí, la afirmación sigue siendo cierta con $`a_ka_{k+1}\le0`$.

## Qué conviene aclarar con el profesor

1. **Problema 4.3, familias $`\mathcal M_3`$ y $`\mathcal M_5`$.** Con el parámetro $`r\in(0;+\infty)`$ sus uniones son $`\mathbb R\setminus\{0\}`$ y $`(0;+\infty)`$, no $`\mathbb R`$, de modo que la primera condición de la definición de base sobre $`\mathbb R`$ literalmente no se cumple. En la solución se demuestra lo que es cierto y se indica cómo corregir el enunciado.
2. **Problema 2.3.** En la tarea 2 figura $`y^3`$; en el archivo abreviado de la tarea 3, $`y^2`$. Las respuestas difieren; están resueltas ambas variantes, con $`y^3`$ como principal.
3. **Problema 2'.2, la indicación.** «El caso trivial $`k=1`$» se ha leído como $`m=1`$ ($`k`$ es el índice de sumación en el enunciado).

## Cómo encajan las tareas

```mermaid
flowchart LR
    T["Fórmula de Taylor (tarea 1)"] --> E["Extremos condicionados (tarea 2)"]
    E --> H["4.1 → Hölder 4.2"]
    C["Comparación 3.4"] --> K["Kummer 3.6"]
    K --> D["d'Alembert 3.7"]
    K --> R["Raabe 3.9"]
    R --> D
    D --> L["Formas límite 4.6"]
    R --> L
    R --> P["3.11: series 1/k^α"]
    P --> A["4.8, 4.9"]
    L --> A
    I["Criterio integral 4.10"]
    Z["Leibniz 4.11"] --> Z2["4.12"]
```

Las series de signo constante se estudian con una sola herramienta, la acotación de las sumas parciales, y con una cadena de series patrón cada vez más finas: la progresión geométrica (Cauchy, d'Alembert), las series de potencias $`\sum k^{-\alpha}`$ (Raabe). Las series de signo variable convergen por otra razón, las cancelaciones, y necesitan un criterio propio (Leibniz).

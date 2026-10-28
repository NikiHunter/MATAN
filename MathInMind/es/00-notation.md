---
title: "Uso del vault y notación"
lang: es
---
# Uso del vault y notación

[Índice](index.md) · [Fórmulas](formula-sheet.md) · [Glosario](glossary.md)

## Obsidian y GitHub

El curso existe en dos vistas, generadas a partir del mismo texto con `python3 scripts/build_views.py`:

| | Vista GitHub — `MathInMind/` | Vista Obsidian — `MathInMind-Obsidian/` |
|---|---|---|
| Cómo abrirla | navegar por el repositorio en GitHub | **Open folder as vault** en Obsidian |
| Enlaces | enlaces Markdown relativos con `#anclas` | `[[wikienlaces]]` con vista previa al pasar el ratón, retroenlaces y grafo |
| Fórmula en línea | `` $`...`$ `` (resiste el procesado Markdown de GitHub) | `$...$` (MathJax) |
| Fórmula destacada | un bloque ```` ```math ```` | `$$...$$` |
| Definiciones y teoremas | citas con una etiqueta en negrita | recuadros de color (`[!definition]`, `[!theorem]`, …) |
| Respuestas | bloques `<details>` | recuadros plegados `[!answer]-` |

Cualquier término, teorema con nombre o enunciado numerado de las lecciones está a un clic: la primera mención de un término en cada nota enlaza con su definición, las referencias como «[teorema 2.3.5](lectures-2025-26/lecture-13.md#thm-2-3-5)» enlazan con el enunciado y el [índice de términos y teoremas](term-index.md) los reúne todos. Los diagramas son bloques Mermaid `flowchart` sencillos que ambas vistas muestran. Intenta cada ejercicio antes de abrir su respuesta.

No se necesitan complementos comunitarios ni un preámbulo MathJax personalizado. Si Obsidian muestra las ecuaciones como texto, comprueba que abriste `MathInMind-Obsidian/` (no `MathInMind/`) y que MathJax esté activado en el editor.

## Lógica y conjuntos

| Notación | Significado |
|---|---|
| $`\forall`$, $`\exists`$ | para todo, existe |
| $`\neg`$, $`\land`$, $`\lor`$, $`\implies`$, $`\iff`$ | no, y, o, implica, si y solo si |
| $`\varnothing`$, $`A^c`$, $`A\setminus B`$ | vacío, complemento, diferencia |
| $`A\subseteq B`$ | subconjunto, permitiendo igualdad |
| $`\mathcal P(A)`$ | conjunto potencia de $`A`$ |
| $`1_A`$ | indicador: $`1_A(x)=1`$ si $`x\in A`$, si no $`0`$ |

## Conjuntos numéricos e intervalos

Usamos $`\mathbb N=\{1,2,3,\ldots\}`$ y $`\mathbb N_0=\{0,1,2,\ldots\}`$. Los símbolos $`\mathbb Z,\mathbb Q,\mathbb R,\mathbb C`$ denotan enteros, racionales, reales y complejos. La recta ampliada es $`\overline{\mathbb R}=\mathbb R\cup\{-\infty,+\infty\}`$.

Los intervalos son $`(a,b)`$ abierto, $`[a,b]`$ cerrado y $`[a,b)`$ o $`(a,b]`$ semiabiertos. Salvo indicación contraria, $`\log x`$ es el logaritmo natural.

## Notación del análisis

| Notación | Significado |
|---|---|
| $`\sup A`$, $`\inf A`$ | menor [cota superior](02-real-numbers.md#sec-2-2), mayor cota inferior |
| $`\limsup a_n`$, $`\liminf a_n`$ | [límite superior](03-sequences.md#sec-3-5), límite inferior |
| $`a_n\sim b_n`$ | $`a_n/b_n\to1`$ para términos finalmente no nulos |
| $`f=O(g)`$ | $`\vert f\vert \le C\vert g\vert`$ en el régimen límite indicado |
| $`f=o(g)`$ | $`f/g\to0`$ en el régimen límite indicado |
| $`f'`$, $`\partial_i f`$, $`Df`$ | [derivada](06-derivatives.md#sec-6-1) ordinaria, parcial y total |
| $`\nabla f`$, $`Hf`$ | [gradiente](15-multivariable-differentiation.md#sec-15-2) y [hessiana](15-multivariable-differentiation.md#sec-15-4) |
| $`\Vert x\Vert _p`$ | norma $`p`$; $`\Vert x\Vert`$ suele ser la [norma euclidiana](14-several-variables.md#sec-14-1) |
| $`\langle f,g\rangle`$ | [producto interno](21-lp-spaces.md#sec-21-4), especificado en el contexto |
| [c.t.p.](19-measure-theory.md#sec-19-4) | casi en todas partes, fuera de un [conjunto nulo](08-riemann-integration.md#sec-8-2) |
| $`C^k`$, $`C^\infty`$ | $`k`$ veces [continuamente derivable](15-multivariable-differentiation.md#sec-15-1), infinitamente derivable |

En notación asintótica, indica siempre el régimen, como $`x\to0`$ o $`n\to\infty`$. En integrales, $`dA`$ y $`dV`$ son elementos de área y volumen; $`d\mu`$ identifica la medida.

## Lista de comprobación de una prueba

Antes de usar un teorema, pregunta:

1. ¿Se cumplen las hipótesis de dominio y regularidad?
2. ¿La convergencia es puntual, uniforme, absoluta, casi en todas partes o en norma?
3. ¿Importan los extremos, la orientación, la [compacidad](13-metric-spaces.md#sec-13-4) y la finitud?
4. ¿Un ejemplo demuestra la afirmación o solo la ilustra?
5. ¿Puede un contraejemplo mostrar que una hipótesis omitida es necesaria?

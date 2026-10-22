---
title: "Uso del vault y notación"
lang: es
---
# Uso del vault y notación

[Índice](index.md) · [Fórmulas](formula-sheet.md) · [Glosario](glossary.md)

## Obsidian y GitHub

Abre el directorio `MathInMind` como vault de Obsidian. La navegación usa enlaces Markdown relativos ordinarios, que también funcionan en GitHub. Las fórmulas en línea usan `$...$`, las destacadas `$$...$$` y los diagramas bloques Mermaid `flowchart` sencillos. Las respuestas están dentro de `<details>`; expándelas solo después de intentar el ejercicio.

No se necesitan complementos comunitarios ni un preámbulo MathJax personalizado. Si Obsidian muestra las ecuaciones como texto, comprueba que MathJax esté activado en el editor.

## Lógica y conjuntos

| Notación | Significado |
|---|---|
| $\forall$, $\exists$ | para todo, existe |
| $\neg$, $\land$, $\lor$, $\implies$, $\iff$ | no, y, o, implica, si y solo si |
| $\varnothing$, $A^c$, $A\setminus B$ | vacío, complemento, diferencia |
| $A\subseteq B$ | subconjunto, permitiendo igualdad |
| $\mathcal P(A)$ | conjunto potencia de $A$ |
| $1_A$ | indicador: $1_A(x)=1$ si $x\in A$, si no $0$ |

## Conjuntos numéricos e intervalos

Usamos $\mathbb N=\{1,2,3,\ldots\}$ y $\mathbb N_0=\{0,1,2,\ldots\}$. Los símbolos $\mathbb Z,\mathbb Q,\mathbb R,\mathbb C$ denotan enteros, racionales, reales y complejos. La recta ampliada es $\overline{\mathbb R}=\mathbb R\cup\{-\infty,+\infty\}$.

Los intervalos son $(a,b)$ abierto, $[a,b]$ cerrado y $[a,b)$ o $(a,b]$ semiabiertos. Salvo indicación contraria, $\log x$ es el logaritmo natural.

## Notación del análisis

| Notación | Significado |
|---|---|
| $\sup A$, $\inf A$ | menor cota superior, mayor cota inferior |
| $\limsup a_n$, $\liminf a_n$ | límite superior, límite inferior |
| $a_n\sim b_n$ | $a_n/b_n\to1$ para términos finalmente no nulos |
| $f=O(g)$ | $|f|\le C|g|$ en el régimen límite indicado |
| $f=o(g)$ | $f/g\to0$ en el régimen límite indicado |
| $f'$, $\partial_i f$, $Df$ | derivada ordinaria, parcial y total |
| $\nabla f$, $Hf$ | gradiente y hessiana |
| $\|x\|_p$ | norma $p$; $\|x\|$ suele ser la norma euclidiana |
| $\langle f,g\rangle$ | producto interno, especificado en el contexto |
| c.t.p. | casi en todas partes, fuera de un conjunto nulo |
| $C^k$, $C^\infty$ | $k$ veces continuamente derivable, infinitamente derivable |

En notación asintótica, indica siempre el régimen, como $x\to0$ o $n\to\infty$. En integrales, $dA$ y $dV$ son elementos de área y volumen; $d\mu$ identifica la medida.

## Lista de comprobación de una prueba

Antes de usar un teorema, pregunta:

1. ¿Se cumplen las hipótesis de dominio y regularidad?
2. ¿La convergencia es puntual, uniforme, absoluta, casi en todas partes o en norma?
3. ¿Importan los extremos, la orientación, la compacidad y la finitud?
4. ¿Un ejemplo demuestra la afirmación o solo la ilustra?
5. ¿Puede un contraejemplo mostrar que una hipótesis omitida es necesaria?

---
id: conditional-extremum-definition
type: definition
semester: 3
lang: es
aliases: ["extremo relativo", "ecuaciones de ligadura"]
tags: [analysis/extrema, sem3, definition]
source_pages: [p015]
translations: ["[[ru/Понятия/Условный экстремум]]", "[[en/Concepts/Conditional extremum]]"]
status: draft
---

# Extremo condicional

Sean $f: E\subset\mathbb{R}^n\to\mathbb{R}$ y $a\in E$ un punto de extremo de $f$. Si interesan no todos los puntos $x\in V(a)$ sino solo los que satisfacen igualdades adicionales — las ecuaciones de ligadura —, se habla de un extremo condicional (relativo).

> [!definition] Definición 6.7.2
> Sean $E\subset\mathbb{R}^n$, $a\in E$, $m\in\mathbb{N}$, $m<n$, $f,\varphi_1,\ldots,\varphi_m: E\to\mathbb{R}$. Supongamos que $a$ es un punto de extremo de la restricción de $f$ al conjunto
> $$\{x\in E:\ \varphi_k(x)=\varphi_k(a)\ \forall k=1..m\}.$$
> Entonces $a$ se llama punto de extremo condicional (relativo) de $f$ del tipo correspondiente, sujeto a las ecuaciones de ligadura $\varphi_k(x)=\varphi_k(a)$, $k\in\{1,\ldots,m\}$, $x\in E$.

Sin pérdida de generalidad puede suponerse $\varphi_k(a)=0$ para todo $k$.

## Relaciones

- [[Multiplicadores de Lagrange]]
- [[Puntos de extremo]]

> [!warning] Marcas abiertas: ⟦S057⟧, ⟦M058⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Условный экстремум — `ru/Понятия/Условный экстремум.md`
- en: Conditional extremum — `en/Concepts/Conditional extremum.md`

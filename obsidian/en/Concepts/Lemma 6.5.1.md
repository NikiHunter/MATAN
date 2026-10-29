---
id: lemma-remainder-zero-derivatives
type: lemma
semester: 3
lang: en
aliases: ["lemma on the vanishing remainder"]
tags: [analysis/taylor, sem3, lemma]
source_pages: [p003, p004]
translations: ["[[ru/Понятия/Лемма 6.5.1]]", "[[es/Conceptos/Lema 6.5.1]]"]
status: draft
---

# Lemma 6.5.1

> [!lemma] Lemma 6.5.1
> Let $E\subset\mathbb{R}^n$, let $a$ be an interior point of $E$, $s\in\mathbb{N}$, and let $f: E\to\mathbb{R}^m$ be differentiable at $a$, with $f$ and all its partial derivatives of order at most $s$ equal to zero at $a$. Then
> $$f(a+h)=o(\|h\|^s)\quad \text{as } h\to0.$$

> [!proof]- Outline from the notes
> It suffices to check the statement for coordinate functions, so $m=1$; the proof is by induction on $s$.
>
> Base $s=1$: $f(a+h)=f(a)+\sum_{k=1}^{n}\dfrac{\partial f}{\partial x_k}(a)h_k+o(\|h\|)=o(\|h\|)$.
>
> Step $s\mapsto s+1$: the first-order partial derivatives are $s$ times differentiable, the induction hypothesis applies to them, and lemma 6.4.1 produces points $c^k\in V_\delta(a)$ giving $\left|f(a+h)\right|\le\varepsilon\|h\|^{s+1}$. $\blacksquare$

## Related

- [[Taylor–Peano theorem]]

> [!warning] Open markers: ⟦S013⟧, ⟦S015⟧, ⟦S017⟧, ⟦T014⟧, ⟦T016⟧, ⟦U012⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Лемма 6.5.1 — `ru/Понятия/Лемма 6.5.1.md`
- es: Lema 6.5.1 — `es/Conceptos/Lema 6.5.1.md`

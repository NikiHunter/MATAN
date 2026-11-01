---
id: taylor-polynomial-uniqueness
type: theorem
semester: 3
lang: es
aliases: []
tags: [analysis/taylor, sem3, theorem]
source_pages: [p002]
translations: ["[[ru/Понятия/Единственность многочлена Тейлора]]", "[[en/Concepts/Uniqueness of the Taylor polynomial]]"]
status: draft
---

# Unicidad del polinomio de Taylor

> [!theorem] Unicidad
> Si el polinomio de Taylor existe, es único.

> [!proof]- Demostración tal como está en los apuntes
> Sean $p$ y $q$ dos polinomios de este tipo con $\deg p\le s$, $\deg q\le s$. Sea $r:=p-q$; hay que probar $r\equiv0$.
>
> Sin pérdida de generalidad $a=0$. Entonces $0=r(x)+o(\|x\|^s)$ cuando $x\to0$, de donde $r(x)=o(\|x\|^s)$ y $r(x)=\alpha(x)\cdot\|x\|^s$ con $\alpha(x)\to0$ cuando $x\to0$.
>
> Además $r(x)=\sum_{k=0}^{s}r_k$, donde $r_k$ es un polinomio homogéneo de grado $k$, y
> $$\sum_{k=0}^{s}r_k(x)t^k=\sum_{k=0}^{s}r_k(tx)=r(tx)=|t|^s\alpha(tx)\|x\|^s,$$
> por lo que todos los coeficientes son nulos: $r_k(x)\equiv0$ para todo $k$, es decir $r(x)\equiv0$. $\blacksquare$

La homogeneidad de un polinomio de grado $k$ significa $\hat{p}(tx)=t^k\hat{p}(x)$.

## Relaciones

- [[Polinomio de Taylor]]
- [[Lema 6.5.1]]

> [!warning] Marcas abiertas: ⟦A007⟧, ⟦A011⟧, ⟦M008⟧, ⟦M009⟧, ⟦S005⟧, ⟦S006⟧, ⟦T010⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Единственность многочлена Тейлора — `ru/Понятия/Единственность многочлена Тейлора.md`
- en: Uniqueness of the Taylor polynomial — `en/Concepts/Uniqueness of the Taylor polynomial.md`

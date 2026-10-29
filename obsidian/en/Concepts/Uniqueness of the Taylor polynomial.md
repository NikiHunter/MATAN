---
id: taylor-polynomial-uniqueness
type: theorem
semester: 3
lang: en
aliases: []
tags: [analysis/taylor, sem3, theorem]
source_pages: [p002]
translations: ["[[ru/Понятия/Единственность многочлена Тейлора]]", "[[es/Conceptos/Unicidad del polinomio de Taylor]]"]
status: draft
---

# Uniqueness of the Taylor polynomial

> [!theorem] Uniqueness
> If a Taylor polynomial exists, it is unique.

> [!proof]- Proof as written in the notes
> Let $p$ and $q$ be two such polynomials with $\deg p\le s$, $\deg q\le s$. Put $r:=p-q$; we must show $r\equiv0$.
>
> Without loss of generality $a=0$. Then $0=r(x)+o(\|x\|^s)$ as $x\to0$, hence $r(x)=o(\|x\|^s)$ and $r(x)=\alpha(x)\cdot\|x\|^s$ with $\alpha(x)\to0$ as $x\to0$.
>
> Next $r(x)=\sum_{k=0}^{s}r_k$, where $r_k$ is a homogeneous polynomial of degree $k$, and
> $$\sum_{k=0}^{s}r_k(x)t^k=\sum_{k=0}^{s}r_k(tx)=r(tx)=|t|^s\alpha(tx)\|x\|^s,$$
> so every coefficient vanishes: $r_k(x)\equiv0$ for all $k$, that is $r(x)\equiv0$. $\blacksquare$

Homogeneity of a polynomial of degree $k$ means $\hat{p}(tx)=t^k\hat{p}(x)$.

## Related

- [[Taylor polynomial]]
- [[Lemma 6.5.1]]

> [!warning] Open markers: ⟦A007⟧, ⟦A011⟧, ⟦M008⟧, ⟦M009⟧, ⟦S005⟧, ⟦S006⟧, ⟦T010⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Единственность многочлена Тейлора — `ru/Понятия/Единственность многочлена Тейлора.md`
- es: Unicidad del polinomio de Taylor — `es/Conceptos/Unicidad del polinomio de Taylor.md`

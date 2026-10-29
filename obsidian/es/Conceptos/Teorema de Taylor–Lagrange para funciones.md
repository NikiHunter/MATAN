---
id: taylor-lagrange-scalar
type: theorem
semester: 3
lang: es
aliases: []
tags: [analysis/taylor, sem3, theorem]
source_pages: [p005, p006]
translations: ["[[ru/Понятия/Теорема Тейлора–Лагранжа для функций]]", "[[en/Concepts/Taylor–Lagrange theorem for functions]]"]
status: draft
---

# Teorema de Taylor–Lagrange para funciones

Sean $\Delta_{a,b}=\{a+t(b-a):t\in[0,1]\}$ y $\hat{\Delta}_{a,b}=\Delta_{a,b}\setminus\{a,b\}$.

> [!theorem] Teorema 6.5.2
> Sean $E$ abierto en $\mathbb{R}^n$, $s\in\mathbb{N}$ y $f: E\to\mathbb{R}$ $s+1$ veces diferenciable en $E$, con $a\in E$ y $\Delta_{a,x}\subset E$. Entonces existe $c\in\hat{\Delta}_{a,x}$ tal que
> $$f(x)=\sum_{k=0}^{s}\frac{d_a^kf(x-a)}{k!}+\frac{d_c^{s+1}f(x-a)}{(s+1)!}.$$

> [!proof]- Demostración tal como está en los apuntes
> Se pone $h:=x-a$ y $F(t)=f(a+th)$, $t\in[0,1]$; entonces $F^{(k)}(t)=d_{a+th}^kf(h)$. A $F$ se le aplica la fórmula de Taylor–Lagrange unidimensional en el punto $1$, y basta tomar $c=a+\theta h$. $\blacksquare$

## Relaciones

- [[Teorema de Taylor–Peano]]
- [[Teorema del valor medio]]
- [[Estimación del resto de Taylor]]

> [!warning] Marcas abiertas: ⟦T023⟧, ⟦T024⟧, ⟦T025⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Теорема Тейлора–Лагранжа для функций — `ru/Понятия/Теорема Тейлора–Лагранжа для функций.md`
- en: Taylor–Lagrange theorem for functions — `en/Concepts/Taylor–Lagrange theorem for functions.md`

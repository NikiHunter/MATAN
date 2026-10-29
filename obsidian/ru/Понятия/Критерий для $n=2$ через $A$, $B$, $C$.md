---
id: hessian-criterion-dim2
type: theorem
semester: 3
lang: ru
aliases: ["критерий Сильвестра для матрицы 2×2"]
tags: [analysis/extrema, sem3, theorem]
source_pages: [p013]
translations: ["[[en/Concepts/Criterion for $n=2$ via $A$, $B$, $C$]]", "[[es/Conceptos/Criterio para $n=2$ mediante $A$, $B$, $C$]]"]
status: draft
---

# Критерий для $n=2$ через $A$, $B$, $C$

Пусть $E\subset\mathbb{R}^2$, $a$ — внутренняя точка $E$, $f: E\to\mathbb{R}$ дважды дифференцируема в точке $a$, $d_af=0$. Положим
$$A=\frac{\partial^2f}{\partial x^2}(a),\qquad B=\frac{\partial^2f}{\partial x\partial y}(a),\qquad C=\frac{\partial^2f}{\partial y^2}(a).$$

> [!theorem] Следствие
> 1) Если $A>0$ и $AC>B^2$, то $a$ — точка строгого минимума $f$.
> 2) Если $A<0$ и $AC>B^2$, то $a$ — точка строгого максимума $f$.
> 3) Если $AC<B^2$, то $f$ не имеет экстремума в точке $a$.

> [!proof]- Доказательство из конспекта
> Квадратичная форма $d_a^2f(h)$ имеет матрицу Гессе $H=\begin{pmatrix}A & B\\ B & C\end{pmatrix}$ с главными минорами $\Delta_1=A$, $\Delta_2=\det H=AC-B^2$; по критерию Сильвестра $\Delta_1>0,\Delta_2>0$ дают положительную определённость, $\Delta_1<0,\Delta_2>0$ — отрицательную. В случае $AC<B^2$ форма $A\,dx^2+2B\,dxdy+C\,dy^2$ принимает значения разных знаков. $\blacksquare$

> [!example] Пример из конспекта
> Для $f(x,y)=x^4+3xy^2+y^4$ в точке $(0,0)$ матрица Гессе нулевая (вырожденная), но $d_a^3f\not\equiv0$, поэтому экстремума в $(0,0)$ нет.

## Связи

- [[Достаточное условие экстремума]]
- [[Определённость квадратичной формы на подпространстве]]

> [!warning] Открытые пометки: ⟦S050⟧, ⟦M051⟧, ⟦A052⟧, ⟦A053⟧, ⟦A054⟧, ⟦G055⟧, ⟦A056⟧ — см. `ocr/ISSUES.md`

## Другие языки

- en: Criterion for $n=2$ via $A$, $B$, $C$ — `en/Concepts/Criterion for $n=2$ via $A$, $B$, $C$.md`
- es: Criterio para $n=2$ mediante $A$, $B$, $C$ — `es/Conceptos/Criterio para $n=2$ mediante $A$, $B$, $C$.md`

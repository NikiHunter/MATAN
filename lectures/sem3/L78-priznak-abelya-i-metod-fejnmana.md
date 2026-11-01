---
semester: 3
lecture: 78
topic: "Признак Абеля, непрерывность и дифференцирование по параметру, метод Фейнмана"
source_pages: [p063, p064, p065, p066]
lang: ru
status: draft
---

# Лекция 78 — Признак Абеля, непрерывность и дифференцирование по параметру, метод Фейнмана

> [!info] Происхождение текста
> Текст переписан со страниц `p063`–`p066` рукописной тетради
> (см. [`ocr/raw/`](../../ocr/raw), [`ocr/MANIFEST.md`](../../ocr/MANIFEST.md)).
> В тетради этот материал помечен как «Лекции 77–78»: пара лекций не разделена.
> Разбиение на отдельные файлы L77 и L78 проведено по границе p066/p067 (смена темы); текст не переставлялся и не дополнялся.
> Решений в `My decision` (`ocr/ISSUES.md`) нет, поэтому все пометки остаются `open`
> и продублированы предупреждениями. Ничего не добавлено: ни доказательств,
> ни примеров, ни «пропущенных шагов».

## p063

### Замечание

В отличии от пр. Дирихле, здесь не требуется чтобы $f(x,y)\downarrow0$.
Достаточно лишь монотонности и равномерной ограниченности $f$, а вся
«сх-ть» обеспечивается равномерной сх-тью интеграла от $g$. ⟦S292⟧

### Д-во (пр. Абеля)

Воспользуемся крит. Б-К равномерной сх-ти несобств. интегр.

Получ. $f$ равномерно ограничено, т.е. $|f(x,y)|\le M$

$\varphi$ фиксируем $\varepsilon>0$, т.к. $\int_a^bg(x,y)\,dx$ сх-ся равномерно $\forall y\in Y$ по ⟦U293⟧

$\Rightarrow\exists\eta\in[a,b)$ такое, что $\forall n_1,n_2:\eta<n_1<n_2<b$ и $\forall y\in Y$
выполнено $\left|\int_{n_1}^{n_2}g(x,y)\,dx\right|<\dfrac{\varepsilon}{2M}$ ⟦S294⟧

Замечание: применим т.к. м.б. $f$ — монотонна? ⟦S295⟧

$\Rightarrow\exists\xi\in[n_1,n_2]$:
$\left|\int_{n_1}^{n_2}f(x,y)g(x,y)\,dx\right|=\left|f(n_1,y)\int_{n_1}^{\xi}g(x,y)\,dx+f(n_1,y)\int_\xi^{n_2}g(x,y)\,dx\right|\le$
$\le|f(n_1,y)|\cdot\left|\int_{n_1}^{\xi}g(x,y)\,dx\right|+|f(n_2,y)|\cdot\left|\int_\xi^{n_2}g(x,y)\,dx\right|<$
$<M\cdot\dfrac{\varepsilon}{2M}+M\cdot\dfrac{\varepsilon}{2M}=\varepsilon$ ⟦T296⟧

Итак, $\forall\varepsilon>0\ \exists\eta\in[a,b)$ такое, что
$\forall n_1,n_2:a<\eta<n_1<n_2<b$ и $\forall y\in Y$:
$\left|\int_{n_1}^{n_2}f(x,y)g(x,y)\,dx\right|<\varepsilon$.

(т.е. усп. крит. Б-К выполнено ⇒ равномерная сх-ть!) $\square$

> [!warning] Неразрешённые пометки страницы p063 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S292: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U293: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S294: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S295: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> T296: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`

## p064

### Пример:

1) $I_1(y)=\int_0^{+\infty}\dfrac{\sin x}{x}e^{-xy}\,dx=I_1(y)$

Очевидно, что $I_1(y)$ задана для $y\ge0$

Сх-ся ли $I_1(y)$ равномерно на $Y=[0,+\infty)$? ⟦S297⟧

$\left[f(x,y)=e^{-xy},\ \text{тогда}\ \forall y_0>0,\ f(x,y)\downarrow0\ (x\to+\infty)\right.$
$\left[g(x,y)=\dfrac{\sin x}{x},\ \text{тогда}\ \forall y_0>0,\ f(x,y)\downarrow0\ (x\to+\infty)\right.$ ⟦T298⟧

2) $|f(x,y)|\le1$

3) $\int_0^\infty\dfrac{\sin x}{x}\,dx$ — сх-ся

$\Rightarrow I_1(y)$ — сх-ся равномерно по пр. Абеля.

2) $I_2(\alpha)=\int_0^{+\infty}\dfrac{\sin x}{x^\alpha}\,dx$, $\alpha<0$ — неопределён. ⟦A299⟧

Докажем равномерную сх-ть на $[x_0,+\infty)$ ($x_0>0$)

Применим пр. Дирихле. $\left[f(x,\alpha)=x^{-\alpha}\right.$, $\left.g(x,\alpha)=\sin x\right.$

1) $x^{-\alpha}\downarrow0\ (\forall x>x_0)$ ⟦A300⟧
2) $g(x,\alpha)=\sin x$
$|G(t,\alpha)|=\left|\int_0^t\sin x\,dx\right|=\left|-\cos x\right|_0^t\left|=|-\cos t+\cos 1|\le2$. ⟦T301⟧

Выполнены усл. пр. равномерной сх-ти Дирихле
для несобств. интегр. от параметра ⟦S302⟧

### Замечание:

1) Аналогично определяется и исследуется несобственный
интеграл с особенностью на нижнем пределе $\int_a^bf(x,y)\,dx=I(y)$
($a=-\infty$ или ф неогр.) ⟦U303⟧
2) $I(y)=\int_a^bf(x,y)\,dx$ ф-я определена и исследуется по-
другому в зависимости от выбора применения ⟦U304⟧

> [!warning] Неразрешённые пометки страницы p064 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S297: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> T298: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> A299: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> A300: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> T301: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> S302: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U303: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U304: нечитаемо (illegible), см. `ocr/ISSUES.md`

## p065

Одновременно учел $I_1$, а для $I_2$. ⟦U305⟧

### Непрерывность интеграла по параметру

### Теорема (9.2.1)

1) ср. $f(x,y)$ интегр. по $x$ б. у. $y_0$, а несобств. интеграл
$I(y)=\int_a^bf(x,y)\,dx$ равномерно сх-ся в некоторой окрестности $y_0$.
Тогда $I(y)$ непрерывен б.ч. $y_0$. ⟦U306⟧

### Дифференцирование интеграла по параметру

### Теорема (9.2.2)

1) выполняются след. усл.:

1) ср-я $f(x,y)$ и $f'_y(x,y)$ интегр. по $x$
2) интеграл $\int_a^bf'_y(x,y)\,dx$ сх-ся равномерно на $Y$
3) интеграл $I(y)$ сх-ся хотя бы при одном значении $y_0\in Y$

Тогда $I(y)$ сх-ся равномерно на всей мн-ве $Y$, при этом ф-я
$I(y)$ оказывается диффер-мой и справедливо рав-во:

$I'(y)=\left(\int_a^bf(x,y)\,dx\right)'=\int_a^bf'_y(x,y)\,dx$

### Инт-сть несобств. интегр. по параметру

### Теорема (9.2.3)

1) выполнены след. усл.:

1) ср-я $f(x,y)$ интегр. по $x$
2) интеграл $I(y)$ сх-ся равномерно на $Y=[c,d]$

Тогда $I(y)$ интегрируема на $[c,d]$ и справедливо рав-во
$\int_c^dI(y)\,dy=\int_c^d\left(\int_a^bf(x,y)\,dy\right)dx$ ⟦T307⟧

### Д-во (т. 9.2.1) (идея)

Основано из двух этапах:

1) $\forall\varepsilon>0\ \exists\eta\in[a,b):\sup\left|\int_\eta^bf(x,y)\,dx\right|<\varepsilon$
(независимо от равномерной сх-ти) $\forall y\in U_\delta(y_0)$ ⟦S308⟧
2) $\left|\int_a^b g(y_0+\Delta y)-I(y_0)\right|\le\left|\int_{y_0}^{y_0+\Delta y}\left[f(x,y_0+\Delta y)-f(x,y_0)\right]dx\right|+\ldots$ ⟦U309⟧

> [!warning] Неразрешённые пометки страницы p065 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U305: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U306: нечитаемо (illegible), см. `ocr/ISSUES.md`
> T307: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> S308: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U309: нечитаемо (illegible), см. `ocr/ISSUES.md`

## p066

Зафиксируем $\varepsilon$, находим $\delta$ ⟦S310⟧

① $\left|\int_\eta^bf(x,y_0)\,dx\right|<2\varepsilon$: ⟦A311⟧

На основе т. 9.2.2. основная идея вычисления
интегралов с помощью перехода к интегралу с
параметром — метод Фейнмана ⟦A312⟧

### Метод Фейнмана (пример)

$\int_0^\infty\dfrac{e^{-x}-e^{-2x}}{x}\,dx=?$

$I(2)=?$

Рассм. $I(\alpha)=\int_0^\infty\dfrac{e^{-x}-e^{-\alpha x}}{x}\,dx$ ⟦S313⟧

$I(1)=0$

$\gamma=[1,2]$

① $I_1+I_2(\alpha)$: $I_2(\alpha)=\int_0^\infty\dfrac{e^{\alpha x}}{x}\,dx$ ⟦T314⟧

$I_2(\alpha)$ сх-ся, равномерно на $\gamma$ по пр. Вейер-
штрасса: $|f(\alpha,x)|\le\dfrac{e^{\alpha x}+e^{-x}}{x}\le\dfrac{?}{x}=g(x)$ ⟦U315⟧

$I_2 e^{-x}\,dx=e^{-\alpha x}\,dx$ ⟦T316⟧

$\int_0^\infty\dfrac{e^{-x}}{x}\,dx$ — сх-ся ⟦M317⟧

$\dfrac{df}{d\alpha}=-e^{-\alpha x}$

$\int_0^\infty e^{-x}\,dx<\int_0^\infty e^{-x}\,dx\Rightarrow$ есть равномерная
сх-ть ⟦T318⟧

$\Rightarrow I'(\alpha)=\int_0^\infty\dfrac{\partial f}{\partial\alpha}\,dx=\int_0^\infty e^{-\alpha x}\,dx=\left.\dfrac{e^{-\alpha x}}{-\alpha}\right|_0^\infty=\dfrac1\alpha$

$\Rightarrow I(\alpha)=\int\dfrac1\alpha\,d\alpha+C=\ln|\alpha|+C$, т.к. $I(1)=0$

$\Rightarrow C=0$. $\Rightarrow I(2)=\ln2$.

### Упр (м. Фейнмана)

- $\int_0^\infty\dfrac{dx}{(a+x^2)^2}=I(a)$ — вывести значную форму ⟦U319⟧
- $\left(\dfrac{1}{a+x^2}\right)'_a=2a-\dfrac{1}{(a+x^2)^2}$ ⟦T320⟧
- $\alpha\in[0,+\infty)$, $a_0>0$: идея
- Опираясь на $\int_0^{+\infty}\dfrac{dx}{a^2+x^2}$ ⟦S321⟧

> [!warning] Неразрешённые пометки страницы p066 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S310: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> A311: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> A312: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> S313: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> T314: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> U315: нечитаемо (illegible), см. `ocr/ISSUES.md`
> T316: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> M317: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> T318: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> U319: нечитаемо (illegible), см. `ocr/ISSUES.md`
> T320: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> S321: неясная структура (unclear structure), см. `ocr/ISSUES.md`

---

Source: pages p063–p066

---
semester: 3
lecture: 74
topic: "Радиус сходимости, равномерная сходимость степенных рядов, теорема Абеля"
source_pages: [p047, p048, p049]
lang: ru
status: draft
---

# Лекция 74 — Радиус сходимости, равномерная сходимость степенных рядов, теорема Абеля

> [!info] Происхождение текста
> Текст переписан со страниц `p047`–`p049` рукописной тетради
> (см. [`ocr/raw/`](../../ocr/raw), [`ocr/MANIFEST.md`](../../ocr/MANIFEST.md)).
> В тетради этот материал помечен как «Лекции 73–74»: пара лекций не разделена.
> Разбиение на отдельные файлы L73 и L74 проведено по границе p049/p050 (смена темы); текст не переставлялся и не дополнялся.
> Решений в `My decision` (`ocr/ISSUES.md`) нет, поэтому все пометки остаются `open`
> и продублированы предупреждениями. Ничего не добавлено: ни доказательств,
> ни примеров, ни «пропущенных шагов».

## p047

### Радиус сх-ти и пр. Даламбера

Часто о радиусе сх-ти можно судить не только по ф-ле Коши – Адамара,
но и с помощью пр. Даламбера. Имеем
$R=\lim\limits_{n\to\infty}\left|\dfrac{C_n}{C_{n+1}}\right|$, если предел правой части существует.

### Пример:

$\sum\limits_{k=1}^{\infty}\dfrac{x^k}{k^2}$

$C_k=\dfrac{1}{k^2}$, $C_{k+1}=\dfrac{1}{(k+1)^2}$

$R=\lim\limits_{k\to\infty}\left|\dfrac{C_k}{C_{k+1}}\right|=\lim\left|\dfrac{(k+1)^2}{k^2}\right|=1$
$\Rightarrow R=1$, ряд сх-ся $|x|<R$ ⟦A183⟧

### Запишем в форме степенного ряда

### Замечание (8.4.2)

Заменой $x-a=y$ ряд (8.4.1) приводится к степенному ряду
по степеням $y$ с центром в нуле. ⟦S184⟧

Поэтому при выводе св-в степенных рядов можно, не уменьшая общности, считать $a=0$.

$x-a=y$, $\sum\limits_{k=1}^{\infty}C_k(x-a)^k\to\sum\limits_{k=1}^{\infty}C_ky^k$ ⟦A185⟧

### Теорема (8.4.2) (о равномерной сх-ти степенных рядов)

Имеется степенной ряд $\sum\limits_{k=0}^{\infty}C_k(x-a)^k$, $R\in(0,+\infty]$ его радиус сх-ти.
Тогда $\forall r\in(0,R)$ степенной ряд равномерно сх-ся на мн-ве $|x-a|\le r$.

### Д-во (т. 8.4.2):

> [!note] На полях
> [схема: ось, точки $a-R$, $a$, $a+r$, $a+R$] ⟦G186⟧

Если $|x-a|\le r$, то $|C_k(x-a)^k|\le|C_k|\,|x-a|^k\le|C_k|\,r^k$

Возвращаемся к 8.4.1: $\sum|C_k|r^k$ — сх-ся. ⟦S187⟧

> [!warning] Неразрешённые пометки страницы p047 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> A183: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> S184: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> A185: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> G186: нетривиальный рисунок (non-obvious figure), см. `ocr/ISSUES.md`
> S187: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p048

$\sum\limits_{k=0}^{\infty}C_k(x-a)^k$ на $|x-a|\le r$

По пр. Вейерштрасса:

$u_n(x):X\to\mathbb{R}$

$|u_n(x)|\le C_n$

$\sum\limits_{n=1}^{\infty}C_n$ сх-ся $\Rightarrow\sum\limits_{n=1}^{\infty}u_n(x)$ сх-ся равномерно

> [!note] На полях
> [красным, со стрелкой на $|u_n(x)|\le C_n$] формулировка пр. Вейерштрасса ⟦S188⟧

По пр. Вейерштрасса ряд $\sum C_k(x-a)^k$ сх-ся равномерно ⟦S189⟧

### Теорема (8.4.3) (Абеля о степенных рядах)

Любой степенной ряд $\sum\limits_{k=0}^{\infty}C_k(x-a)^k$, $R\in(0,+\infty)$ его радиус сх-ти.
Если степенной ряд сх-ся при $x=a+R$ или $x=a-R$, то он равномерно сх-ся
на $[a,a+R]$ или $[a-R,a]$ соответственно, а его сумма непрер. в т. $a+R$ слева
(соотв. в т. $a-R$ справа). ⟦S190⟧

> [!note] На полях
> [слева, под точками $a-R$, $a$, $a+R$] $\sum C_k(-R)^k$, $\sum C_kR^k$ ⟦G191⟧

### Теорема Абеля (подсказка)

Если: ① $\sum\limits_{k=1}^{\infty}f_k(x)$ равномерно сх-ся на $X$

② $\forall x\in X$ посл-ть $\{g_k(x)\}$ — монотонна и равномерно огр. на $X$,

то ряд $\sum\limits_{k=1}^{\infty}f_k(x)g_k(x)$ равномерно сх-ся на $X$

### Д-во (т. 8.4.3):

Не умаляя общности, будем считать $a=0$

$\sum\limits_{k=0}^{\infty}C_kx^k$

Преобразуем каждый ряд: $C_kx^k=C_kR^k\cdot\left(\dfrac{x}{R}\right)^k$

> [!warning] Неразрешённые пометки страницы p048 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S188: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S189: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S190: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> G191: нетривиальный рисунок (non-obvious figure), см. `ocr/ISSUES.md`

## p049

$C_kx^k=C_kR^k\cdot\left(\dfrac{x}{R}\right)^k$

$\sum\limits_{k=0}^{\infty}C_kR^k$ — числовой ряд, сх-ся (по усл. ф-лы ряд
$\sum C_k(x-a)^k$ сх-ся при $x=a-R$ или $x=a+R$) ⟦S192⟧

$\sum\limits_{k=0}^{\infty}R^k$ — числовой ряд $\Rightarrow$ его сх-ть можно рассм. как равно? ⟦U193⟧
идео на $[0,R]$ ⟦U194⟧

Посп-ть $\left(\dfrac{x}{R}\right)^k$: $0<x<R$, го $0\le\left(\dfrac{x}{R}\right)^k\le1$
$\Rightarrow$ посл-ть $\left(\dfrac{x}{R}\right)^k$ огр. на $[0,R]$ и монотонна $\forall x\in[0,R]$ ⟦T195⟧

$\Rightarrow$ В силу пр. равномерной сх-ти Абеля ряд $\sum C_kx^k$ равномерно сх-ся на $[0,R]$ ⟦S196⟧

Непрер-ть каждой суммы следует из непрер-ти каждого члена ряда $\sum C_kx^k$
и равномерной сх-ти ряда на $[0,R]$ $\square$

### Пример:

1) $\sum\limits_{n=0}^{\infty}(-2)^n(x-3)^n$

$R=\lim\left|\dfrac{C_n}{C_{n+1}}\right|=\lim\left(\dfrac{2^nn}{(-2)^{n+1}(n+1)}\right)=\lim\left|\dfrac{2}{2(n+1)}\right|=\dfrac12$ ⟦M197⟧

$(2{,}5;3{,}5)$ — интервал сх-ти ⟦A198⟧

2) $\sum\limits_{n=0}^{\infty}\left(-\dfrac32\right)^n(x-2)^n$

$R=\dfrac{1}{\lim\sqrt[n]{|C_n|}}=\dfrac{1}{\lim|3/2|^{n/n}}=\left|\dfrac23\right|=a$ ⟦T199⟧

Ряд сх-ся в $x=-2$, или сх-ти $\varnothing$ ⟦U200⟧

3) $\sum\limits_{n=0}^{\infty}2^{n^2}(x-2)^n$

$R=\dfrac{1}{\lim\sqrt[n]{|C_n|}}=\dfrac{1}{\lim 2^n}=\infty$ — инт. сх-ти $\mathbb{R}$,
сх-ся только на $\mathbb{R}$ ⟦T201⟧

> [!warning] Неразрешённые пометки страницы p049 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S192: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U193: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U194: нечитаемо (illegible), см. `ocr/ISSUES.md`
> T195: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> S196: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> M197: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> A198: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> T199: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> U200: нечитаемо (illegible), см. `ocr/ISSUES.md`
> T201: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`

---

Source: pages p047–p049

---
semester: 3
lecture: 68
topic: "Числовые ряды, критерий Больцано–Коши, абсолютная сходимость"
source_pages: [p018, p019, p020, p021]
lang: ru
status: draft
---

# Лекция 68 — Числовые ряды, критерий Больцано–Коши, абсолютная сходимость

> [!info] Происхождение текста
> Текст переписан со страниц `p018`–`p021` рукописной тетради
> (см. [`ocr/raw/`](../../ocr/raw), [`ocr/MANIFEST.md`](../../ocr/MANIFEST.md)).
> В тетради этот материал помечен как «Лекции 67–68»: пара лекций не разделена.
> Разбиение на отдельные файлы L67 и L68 проведено по границе p021/p022 (смена темы); текст не переставлялся и не дополнялся.
> Решений в `My decision` (`ocr/ISSUES.md`) нет, поэтому все пометки остаются `open`
> и продублированы предупреждениями. Ничего не добавлено: ни доказательств,
> ни примеров, ни «пропущенных шагов».

## p018

### Теорема (6.7.5)

$m,n\in\mathbb{N}$, $m<n$, мн-во $E$ открыто в $\mathbb{R}^n$, $a\in E$, $f\in C^2(E)$, $\Phi\in C^2(E,\mathbb{R}^m)$,
$\Phi(a)=0$, $\operatorname{rank}\Phi'(a)=m$. Положим
$N=\{h\in\mathbb{R}^n:\ d_a\Phi(h)=0\}$, $L(x)=f(x)-\sum\limits_{k=1}^{m}\lambda_k\varphi_k(x)$ $(x\in E)$, где
$\lambda_1,\ldots,\lambda_m$ удовл. усл. (6.7.1) в т. $a$. Тогда справедливы след. утв.:
1) Если $d_a^2L$ положительно/отрицательно определена на $N$, то $f$ имеет в т. $a$
условный минимум/максимум, подчиненный ур-ям связи $\Phi=0$. ⟦S067⟧
2) Если $d_a^2L$ принимает на $N$ как положительные, так и отрицательные
значения, то $f$ не имеет в т. $a$ условного экстремума, подчиненного ур-ям
связи $\Phi=0$.

### Числовые ряды

### Опр (7.1.1)

Дана посл-ть $(a_n)$, $n\in\mathbb{N}$. $\ S_n=a_1+a_2+\ldots+a_n$ - частичная сумма ряда
$\lim\limits_{n\to\infty}S_n=S$ - сумма ряда
$S:=\sum\limits_{n=1}^{\infty}a_n$ - обозначение
$a_n$ - общий член ряда ⟦S068⟧

### Опр (7.1.2)

Ряд $\sum\limits_{n=1}^{\infty}a_n$ сходится, если сумма ряда $S$ сущ. и конечна. В противном
случае - ряд расходится.

$S_n=\sum\limits_{k=1}^{n}a_k$ $\ S=\lim\limits_{n\to\infty}S_n$
1) $S$ - сущ., $S<\infty\Rightarrow$ ряд сх-ся.
2) $S$ - сущ., $S=\infty\Rightarrow$ ряд расходится
3) $S$ - не сущ. $\Rightarrow$ ряд расходится

### Примеры:

Ряд $\sum\limits_{n=1}^{\infty}0=0\Rightarrow$ т. к. все частичные суммы $S_n=0$

> [!warning] Неразрешённые пометки страницы p018 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S067: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S068: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p019

2) $\sum\limits_{k=1}^{\infty}1$ - расходящийся, т. е. $S_n=\sum\limits_{k=1}^{n}1=n$, $\lim\limits_{n\to\infty}S_n=\lim\limits_{n\to\infty}n=+\infty$
3) $\sum\limits_{k=0}^{\infty}(-1)^k=1-1+1-1+1-1+\ldots$ - расх-ся. $\ S_n=\left\{\begin{array}{l}1,\ n-\text{чет}\\ 0,\ n-\text{нечет}\end{array}\right.$
$\{S_n\}$ не имеет ни конечного, ни бесконечного предела $\Rightarrow$ ряд расх. ⟦S069⟧
4) $\sum\limits_{k=1}^{\infty}\dfrac{1}{k(k+1)}$ - сходится и $S=1$
$S_n=\sum\limits_{k=1}^{n}\dfrac{1}{k(k+1)}=\sum\limits_{k=1}^{n}\left(\dfrac{1}{k}-\dfrac{1}{k+1}\right)=1-\dfrac{1}{n+1}\to1$ при $n\to\infty$

### Св-ва рядов:

1) $\sum\limits_{n=1}^{\infty}a_n$ сх-ся, тогда $a_n\to0$ при $n\to\infty$
**Замечание:** 1) Если $a_n\nrightarrow0$ при $n\to\infty$, то $\sum\limits_{n=1}^{\infty}a_n$ - расх-ся. ⟦S070⟧
2) Если $a_n\to0$ при $n\to\infty$, то не обязательно $\sum\limits_{n=1}^{\infty}a_n$ - сх-ся
2) $\sum\limits_{n=1}^{\infty}a_n$ сх-ся $\Leftrightarrow$ $\forall k$ $\sum\limits_{n=k+1}^{\infty}a_n$ - сх-ся
> [!note] На полях
> [красным, в кружке справа] остаток ряда (после $k$-го члена)

### Д-во (св-ва 1):

$\sum\limits_{k=1}^{\infty}a_k=S$ $\ S_N=\sum\limits_{k=1}^{N}a_k$
Ряд сх-ся $\Rightarrow S$ - сущ., $-\infty<S<+\infty$
$a_N=S_N-S_{N-1}\to S-S=0$. $\blacksquare$

**Пример:** $\sum\limits_{k=1}^{\infty}\dfrac{1}{k}=1+\dfrac{1}{2}+\dfrac{1}{3}+\dfrac{1}{4}+\ldots$ - гармонический ряд, расх-ся
$a_k=\dfrac{1}{k}\to0$
$S_{2^m}=1+\dfrac{1}{2}+\left(\dfrac{1}{3}+\dfrac{1}{4}\right)+\left(\dfrac{1}{5}+\ldots+\dfrac{1}{8}\right)+\ldots+\left(\dfrac{1}{2^{m-1}+1}+\ldots+\dfrac{1}{2^m}\right)\ge1+\dfrac{1}{2}+\dfrac{1}{2}+\dfrac{1}{2}+\ldots+\dfrac{1}{2}=$ ⟦M071⟧
> [!note] На полях
> [над слагаемыми, коричневым] $\dfrac{1}{3}+\dfrac{1}{4}>\dfrac{1}{2}$; $\dfrac{1}{5}+\ldots+\dfrac{1}{8}>\dfrac{1}{2}$; $\dfrac{1}{2^{m-1}+1}+\ldots+\dfrac{1}{2^m}>\dfrac{1}{2}$

$=1+\dfrac{m}{2}\to+\infty$ при $m\to\infty$
> [!note] На полях
> [справа, мелко] $R^{m-1}$? ⟦U072⟧

$\{S_{2^m}\}$ $\forall m$ $S_{2^m}\ge1+\dfrac{m}{2}\Rightarrow S_{2^m}\to+\infty\Rightarrow S_m$ - расх-ся ⟦M073⟧

**Д-во (св-ва 2):** $n>m$
$\sum\limits_{k=1}^{n}a_k=\sum\limits_{k=1}^{m}a_k+\sum\limits_{k=m+1}^{n}a_k$ $(*)$
> [!note] На полях
> [красным, под формулой] конечное число при $n\to\infty$

Перейдём в $(*)$ к пределу при $n\to\infty$. Предел в правой и ле-
вой частях $(*)$ сущ. (имеет смысл) одновременно.

> [!warning] Неразрешённые пометки страницы p019 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S069: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S070: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> M071: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> U072: нечитаемо (illegible), см. `ocr/ISSUES.md`
> M073: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`

## p020

$\sum\limits_{k=1}^{n}a_k\to S$; $\left(\sum\limits_{k=1}^{m}a_k\right)=A$; $\sum\limits_{k=m+1}^{n}a_k=A$; $\sum\limits_{k=m+1}^{n}a_k\to S_1=\sum\limits_{k=m+1}^{\infty}a_k$ ⟦S074⟧
$A+S_1=\sum\limits_{k=m+1}^{\infty}a_k$
> [!note] На полях
> [справа] сх-ть $\sum\limits_{k=1}^{\infty}a_k$ и $\sum\limits_{k=m+1}^{\infty}a_k$ $\Rightarrow$ равносильны

### Следствие (св-ва 2)

Если $\sum\limits_{k=1}^{\infty}a_k$ - сх-ся, то $\sum\limits_{k=m+1}^{\infty}a_k\to0$ при $m\to\infty$
> [!note] На полях
> [под формулой] остаток сх-ся ряда $\to0$

### Д-во (сл. из св-ва 2)

$\sum\limits_{k=m+1}^{n}a_k=\sum\limits_{k=1}^{n}a_k-\sum\limits_{k=1}^{m}a_k\to0$
$\downarrow\ \downarrow$
$\sum\limits_{k=1}^{\infty}a_k-\sum\limits_{k=1}^{\infty}a_k$ $\blacksquare$ ⟦S075⟧

### Св-ва рядов:

3) Ряды $\sum\limits_{n=1}^{\infty}a_n=:(I)$ и $\sum\limits_{n=1}^{\infty}ka_n=:(II)$, $k\in\mathbb{R}$ сх-ся и расх-ся одновременно.
Если $(I)$ и $(II)$ сх-ся, то $\sum\limits_{n=1}^{\infty}ka_n=k\sum\limits_{n=1}^{\infty}a_n$
4) Два ряда $\sum\limits_{n=1}^{\infty}a_n$ и $\sum\limits_{n=1}^{\infty}b_n$ сх-ся. Тогда ряд $\sum\limits_{n=1}^{\infty}(a_n+b_n)$ сх-ся и
$\sum\limits_{n=1}^{\infty}(a_n+b_n)=\sum\limits_{n=1}^{\infty}a_n+\sum\limits_{n=1}^{\infty}b_n$ ⟦S076⟧

**Д-во (св-в 3 и 4):** $k\in\mathbb{R}$
$\sum\limits_{n=1}^{N}ka_n=k\sum\limits_{n=1}^{N}a_n$ $\ \left|\ \sum\limits_{n=1}^{N}(a_n+b_n)=\sum\limits_{n=1}^{N}a_n+\sum\limits_{n=1}^{N}b_n\right.$
$N\to\infty\ \downarrow\ \downarrow$ $\ \left|\ N\to\infty\ \downarrow\ \downarrow\right.$
$\sum\limits_{n=1}^{\infty}ka_n=k\sum\limits_{n=1}^{\infty}a_n$ $\ \left|\ \sum\limits_{n=1}^{\infty}(a_n+b_n)=\sum\limits_{n=1}^{\infty}a_n+\sum\limits_{n=1}^{\infty}b_n\right.$ $\blacksquare$ ⟦S077⟧

### Замечание

Если $\sum\limits_{n=1}^{\infty}a_n$ - расх-ся, $\sum\limits_{n=1}^{\infty}b_n$ - сх-ся, то $\sum\limits_{n=1}^{\infty}(a_n+b_n)$ - расх-ся, т.к.
если бы $\sum\limits_{n=1}^{\infty}(a_n+b_n)$ сх-ся, то тогда сходился бы ряд с членами
$a_n=(a_n+b_n)-b_n$. Противоречие.

> [!warning] Неразрешённые пометки страницы p020 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S074: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S075: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S076: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S077: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p021

### Критерий Больцано-Коши

$\sum\limits_{n=1}^{\infty}a_n$ - сх-ся $\Leftrightarrow\forall\varepsilon>0\ \exists N\in\mathbb{N}\ \forall n>N\ \forall p>0$ $\left|\sum\limits_{k=n+1}^{n+p}a_k\right|=\left|a_{n+1}+\ldots+a_{n+p}\right|<\varepsilon$ ⟦T078⟧

### Д-во (Б-К):

По опр. $\sum\limits_{n=1}^{\infty}a_n$ - сх-ся $\Leftrightarrow\{S_m\}$ - имеет конечный предел при $m\to\infty$,
$S_m:=\sum\limits_{n=1}^{m}a_n$
$\Leftarrow$ крит. Б-К для посл-ти $\{S_m\}$ (доказан)
$\forall\varepsilon>0\ \exists N\in\mathbb{N}:\ \forall m,n>N$ $|S_m-S_n|<\varepsilon$.
Без ограничения общности можно считать, что $m>n\Rightarrow$
$\Rightarrow p:=m-n$, $p\in\mathbb{N}\Rightarrow S_m-S_n=\sum\limits_{k=n+1}^{m}a_k$ $\blacksquare$

### Как-во расх-ся ряда с перепис. членами ⟦U079⟧

Нужно найти посл-ть $\{m_n\}$: $m_n>n$ и $\sum\limits_{k=n}^{m_n}a_k\nrightarrow0$ при $m_n\to\infty$
> [!note] На полях
> [справа, мелко] $k=n$, $m_n\to\infty$

### Замечание

Часто выбирают $m_n=\alpha\cdot n$, где $\alpha>1$

**Пример:** $\sum\limits_{k=n}^{2n}\dfrac{1}{k}\to(n+1)\dfrac{1}{2n}\to0$ ⟦T080⟧
$\sum\limits_{k=n}^{2n}\dfrac{1}{k}=\dfrac{1}{n}+\dfrac{1}{n+1}+\ldots+\dfrac{1}{2n}\ge\dfrac{1}{2n}+\dfrac{1}{2n}+\ldots+\dfrac{1}{2n}=\dfrac{n+1}{2n}$

### Абсолютная сх-ть

### Опр (7.2.1)

Ряд $\sum\limits_{n=1}^{\infty}a_n$ наз. абсолютно сходящимся, если ряд $\sum\limits_{n=1}^{\infty}|a_n|$ сх-ся.

5) Если ряд абсолютно сх-ся, то он сх-ся

**Д-во (св-ва 5):** $\forall\varepsilon>0$ и применяем Б-К ⟦U081⟧
Шаг доказан: $\sum\limits_{k=1}^{\infty}|a_k|$ - сх-ся $\Leftrightarrow\exists N\in\mathbb{N}:\ \forall n>N\ \forall p\in\mathbb{N}\ \sum\limits_{k=n+1}^{n+p}|a_k|<\varepsilon$
Но тогда $\left|\sum\limits_{k=n+1}^{n+p}a_k\right|\le\sum\limits_{k=n+1}^{n+p}|a_k|\Rightarrow$ критерий Б-К $\Rightarrow\sum\limits_{k=1}^{\infty}a_k$ - сх-ся. $\blacksquare$ ⟦U082⟧

> [!warning] Неразрешённые пометки страницы p021 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> T078: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> U079: нечитаемо (illegible), см. `ocr/ISSUES.md`
> T080: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> U081: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U082: нечитаемо (illegible), см. `ocr/ISSUES.md`

---

Source: pages p018–p021

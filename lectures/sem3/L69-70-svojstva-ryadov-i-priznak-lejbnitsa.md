---
semester: 3
lecture: "69-70"
topic: "Свойства сходящихся рядов, признаки сравнения и Даламбера, лемма Коши; Ряды с членами произвольного знака, признак Лейбница, перестановки рядов"
source_pages: [p022, p023, p024, p025, p026, p027, p028, p029]
lang: ru
status: draft
---

# Лекции 69–70 — Свойства рядов, признаки сравнения, признак Лейбница, перестановки

> [!info] Происхождение текста
> Текст переписан со страниц `p022`–`p029` рукописной тетради
> (см. [`ocr/raw/`](../../ocr/raw), [`ocr/MANIFEST.md`](../../ocr/MANIFEST.md)).
> В тетради материал помечен как «Лекции 69–70»: пара лекций не разделена.
> Страницы приведены в исходном порядке, без перестановки и без добавления текста.
> Один файл на пару: ранее созданные одиночные файлы заменены этим файлом,
> их содержимое перенесено без изменений.
> Решений в `My decision` (`ocr/ISSUES.md`) нет, поэтому все пометки остаются `open`
> и продублированы предупреждениями. Ничего не добавлено: ни доказательств,
> ни примеров, ни «пропущенных шагов».

## p022

### Лекции 69–70

· _[?]_ сх-ть ⟦U083⟧
· Др. ср. разобр. ⟦U084⟧

> [!note] На полях
> [ниже заголовка — пустая страница: содержание отсутствует]
> Проверено: локальное растяжение контраста по участкам листа (x8 по диапазону 120–255) не выявляет
> прозрачного или выцветшего текста; видны только линии сетки и следы соседнего листа. ⟦S085⟧

⟦S086⟧

> [!warning] Неразрешённые пометки страницы p022 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U083: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U084: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S085: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S086: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p023

### Д-во (св-ва [2]): ⟦S087⟧

$S_N=\sum\limits_{n=1}^{N}a_n$

Посл-ть $(S_N)\uparrow$, т.к. $S_{N+1}-S_N=a_{N+1}>0$ ⟦U088⟧

Сх-ть $(S_N)\Leftrightarrow$ ограниченность сверху $(S_N)$
> [!note] На полях
> [ниже строки, со стрелкой вверх к слову «ограниченность»] ограниченность монотонной посл-ти ⟦S089⟧

$\\blacksquare$

### Д-во (св-ва II): ⟦S090⟧

По т. о пределе монотонной посл-ти $\Rightarrow$ либо $\sum\limits_{n=1}^{\infty}a_n$ - сх-ся,
либо $S:=\lim\limits_{N\to\infty}S_N=+\infty$.
$\\blacksquare$

### Замечание

Для огр. сверху $(S_N)$ достаточно огр. сверху некоторой подпосл-ти $(S_{N_k})$, т.е. $\exists S_{N_k}\le M\ \forall k$. Тогда $\forall N$ можно найти $k$ такое, что $N_k>N$, что тогда $S_N\le S_{N_k}\le M$. ⟦S091⟧

### Первый признак сравнения положительных рядов

Пусть имеются два положительных ряда $\sum\limits_{n=1}^{\infty}a_n$ и $\sum\limits_{n=1}^{\infty}b_n$ ($\forall n\ a_n\ge0,\ b_n\ge0$) и пусть $\forall n\ b_n\ge a_n$. Тогда: ⟦S092⟧

❶ $\sum\limits_{n=1}^{\infty}b_n$ - сх-ся $\Rightarrow\sum\limits_{n=1}^{\infty}a_n$ - сх-ся

❷ $\sum\limits_{n=1}^{\infty}a_n$ - расх-ся $\Rightarrow\sum\limits_{n=1}^{\infty}b_n$ - расх-ся

### Д-во (первый пр. ср.)

$A_N=\sum\limits_{n=1}^{N}a_n$, $B_N=\sum\limits_{n=1}^{N}b_n$.

$\forall n\ a_n\le b_n\Rightarrow A_N\le B_N$

❶ $B_N\to B$ (т.е. $\sum\limits_{n=1}^{\infty}b_n$ - сх-ся) } $\Rightarrow\exists\lim\limits_{N\to\infty}A_N\le B<+\infty\Rightarrow$
$(A_N)\uparrow$
$A_N\le B_N\le B\ \forall n$ } $\Rightarrow\sum\limits_{n=1}^{\infty}a_n$ - сх-ся ⟦S093⟧

❷ доказывается отрицанием ❶ ⟦S094⟧

> [!warning] Неразрешённые пометки страницы p023 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S087: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U088: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S089: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S090: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S091: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S092: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S093: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S094: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p024

### Второй признак сравнения положительных рядов

Пусть имеются два положительных ряда $\sum\limits_{n=1}^{\infty}a_n$ и $\sum\limits_{n=1}^{\infty}b_n$ и пусть $\forall n\ b_n>0$. Если сущ. $\lim\limits_{n\to\infty}\dfrac{a_n}{b_n}=:L$, то: ⟦S095⟧

❶ $L<+\infty$, т.е. $L\in[0,+\infty)$:
$\sum\limits_{n=1}^{\infty}b_n$ - сх-ся $\Rightarrow\sum\limits_{n=1}^{\infty}a_n$ - сх-ся ⟦M096⟧

❷ $L>0$, т.е. $L\in(0,+\infty]$:
$\sum\limits_{n=1}^{\infty}a_n$ - сх-ся $\Rightarrow\sum\limits_{n=1}^{\infty}b_n$ - сх-ся

### Замечание

Если $L\in(0,+\infty)$, то $\sum\limits_{n=1}^{\infty}a_n$ и $\sum\limits_{n=1}^{\infty}b_n$ сх-ся и расх-ся одновременно.

### Д-во (второй пр. ср.)

❶ $\lim\limits_{n\to\infty}\dfrac{a_n}{b_n}=L<+\infty\Rightarrow\left(\dfrac{a_n}{b_n}\right)$ - ограничена, т.е. $\exists M:\ \forall n\ \dfrac{a_n}{b_n}\le M\Rightarrow\forall n\ a_n\le Mb_n$
$\sum\limits_{n=1}^{\infty}b_n$ - сх-ся $\Rightarrow\sum\limits_{n=1}^{\infty}Mb_n$ - сх-ся $\overset{\text{I пр. ср.}}{\Rightarrow}\sum\limits_{n=1}^{\infty}a_n$ - сх-ся ⟦S097⟧

❷ $\lim\limits_{n\to\infty}\dfrac{a_n}{b_n}=L>0\Rightarrow$ начиная с некоторого номера $K$ имеем $a_n\ge cb_n$ ⟦U098⟧
$\Rightarrow$ Для $n>K$ имеем $a_n\ge cb_n\Rightarrow$ применим ❶, поменяв $a_n$ и $b_n$ местами ⟦U099⟧

$\\blacksquare$

> [!warning] Неразрешённые пометки страницы p024 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S095: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> M096: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> S097: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U098: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U099: нечитаемо (illegible), см. `ocr/ISSUES.md`

## p025

**Признак сх-ти Даламбера** ($\sum\limits_{n=1}^{\infty}a_n$, $a_n>0$) (D'Alembert)

Пусть $\lim\limits_{n\to\infty}\dfrac{a_{n+1}}{a_n}=:D$. Тогда:

❶ Если $D<1$, то ряд $\sum\limits_{n=1}^{\infty}a_n$ сх-ся.
❷ Если $D>1$, то ряд $\sum\limits_{n=1}^{\infty}a_n$ расх-ся.
❸ Если $D=1$ или $D$ не сущ., то необходимо дальнейшее исследование ряда другими средствами.

> [!note] На полях
> [внизу справа, у слов «D=1 или D не сущ.»] (не сущ. — др. случай)

### Д-во (пр. Даламбера):

❶ $D<1$. Положим $q:=\dfrac{1+D}{2}$
$\left|\dfrac{a_{n+1}}{a_n}-D\right|<\varepsilon$ ⟦S100⟧
Возьмём $\varepsilon:=\dfrac{1-D}{2}$ $\exists N:\forall n>N$ $\dfrac{a_{n+1}}{a_n}-D<\varepsilon\Rightarrow\dfrac{a_{n+1}}{a_n}<D+\varepsilon=\dfrac{1-D}{2}+D=\dfrac{1+D}{2}=q$
$q\in(1/2;1)$ ⟦S101⟧
$\forall n>N\ a_{n+1}<qa_n\ \forall q\in(1/2,1)\Rightarrow$
$\Rightarrow a_n<q^{n-N}a_N\ \forall n>N$
> [!note] На полях
> [справа от последней строки, красным] по индукции

Сравним ряды $\sum\limits_{n=1}^{\infty}q^{n-N}a_N$ и $\sum\limits_{n=1}^{\infty}q^n$ - сх-ся, т.к. геом. прогрессия ⟦S102⟧
По пр. ср. $\sum\limits_{n=1}^{\infty}a_n$ - сх-ся.

❷ $D>1$. $\lim\limits_{n\to\infty}\dfrac{a_{n+1}}{a_n}=D\Rightarrow\exists M:\ \forall n>M\ \dfrac{a_{n+1}}{a_n}>1\Rightarrow a_{n+1}>a_n\ \forall n>M$
$\Rightarrow\forall n>M\ a_n>a_M>0\Rightarrow\lim\limits_{n\to\infty}a_n\ne0\Rightarrow\sum\limits_{n=1}^{\infty}a_n$ - расх-ся по необходимому усл. сх-ти.

❸ $\sum\limits_{k=1}^{\infty}\dfrac{1}{k^2}$ - сх-ся, $\lim\limits_{k\to\infty}\dfrac{a_{k+1}}{a_k}=\lim\limits_{k\to\infty}\dfrac{k^2}{(k+1)^2}=1$
$\sum\limits_{k=1}^{\infty}\dfrac{1}{k}$ - расх-ся, $\lim\limits_{k\to\infty}\dfrac{a_{k+1}}{a_k}=\lim\limits_{k\to\infty}\dfrac{k}{k+1}=1$ ⟦M103⟧

$\\blacksquare$

> [!warning] Неразрешённые пометки страницы p025 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S100: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S101: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S102: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> M103: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`

## p026

$\Rightarrow\sum\limits_{n=1}^{\infty}a_n$ - расх-ся по необходимому усл. сх-ти.

❸ $\sum\limits_{n=1}^{\infty}\dfrac{1}{n^2}$ - сх-ся, $\lim\limits_{n\to\infty}\sqrt[n]{\dfrac{1}{n^2}}=1$ ⟦U104⟧

$\sum\limits_{n=1}^{\infty}\dfrac{1}{n}$ - расх-ся, $\sum\limits_{n=1}^{\infty}\dfrac{1}{n^2}$ - сх-ся. $\\blacksquare$ ⟦T105⟧

### Лемма Коши

Пусть $a_n\ge a_{n+1}\ge0\ \forall n$. Тогда:
$$\sum\limits_{n=1}^{\infty}a_n\ \text{- сх-ся}\ \Leftrightarrow\ \sum\limits_{n=1}^{\infty}2^na_{2^n}\ \text{- сх-ся}$$
⟦S106⟧

### Идея док-ва (л. Коши) ⟦U107⟧

$2^na_{2^n}=\underbrace{a_{2^n}+a_{2^n}+\ldots+a_{2^n}}_{2^n\ \text{раз}}\le a_{2^n}+a_{2^n+1}+\ldots+a_{2^{n+1}}+a_1$
> [!note] На полях
> [под левой частью неравенства, подпись к скобке] $2^n$ раз
> [!note] На полях
> [над правой частью, мелко] … $+a_{2^{n+1}}$ … ⟦S108⟧

### Ряды с членами произвольного знака

### Опр (7.4.1) ⟦A109⟧

Если ряд $\sum\limits_{n=1}^{\infty}a_n$ сх-ся, а соотв. ряд $\sum\limits_{n=1}^{\infty}|a_n|$ расх-ся, то исходный ряд $\sum\limits_{n=1}^{\infty}a_n$ наз. условно сходящимся. ⟦S110⟧

> [!warning] Неразрешённые пометки страницы p026 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U104: нечитаемо (illegible), см. `ocr/ISSUES.md`
> T105: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> S106: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U107: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S108: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> A109: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> S110: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p027

Рассм. теперь ряд с произвольными членами $\sum\limits_{n=0}^{\infty}(-1)^nc_n$, $c_n\ge0$. Чаще такие ряды наз. **_знакочередующимися_**.

**Признак Лейбница** ($c_n>0\ \forall n$)

$\exists c_n\downarrow0$, т.е. $c_{n+1}\le c_n\ \forall n$ и $c_n\xrightarrow[n\to\infty]{}0$. Тогда ряд $\sum\limits_{n=0}^{\infty}(-1)^nc_n$ сх-ся.

Рассм. остаток ряда $R_n:=\sum\limits_{k=n+1}^{\infty}(-1)^kc_k$. Для ряда Лейбница справедлива ф-ла $|R_n|\le c_{n+1}$. ⟦S111⟧

**Пример:** $1-1/2+1/3-1/4+\ldots+\dfrac{(-1)^{n+1}}{n}+\ldots=\sum\limits_{n=1}^{\infty}\dfrac{(-1)^{n+1}}{n}=\ln 2$.

### Д-во (пр. Лейбница):

Рассм. $S_{2m+1}=\sum\limits_{n=0}^{2m+1}(-1)^nc_n$; $S_{2m+1}-S_{2m-1}=\sum\limits_{n=0}^{2m+1}(-1)^nc_n-\sum\limits_{n=0}^{2m-1}(-1)^nc_n=c_{2m}-c_{2m+1}\ge0$ ⟦M112⟧

$S_{2m+1}=c_0-c_1+c_2-c_3+\ldots+c_{2m}-c_{2m+1}=c_0+(c_2-c_1)+(c_4-c_3)+\ldots+(c_{2m}-c_{2m+1})\le c_0$
> [!note] На полях
> [под скобками $(c_2-c_1)$, $(c_4-c_3)$, $\ldots$, $(c_{2m}-c_{2m+1})$] $\le0$; $\le0$; $\le0$
> [!note] На полях
> [справа от строки] т.к. $c_{n+1}\le c_n$ ⟦S113⟧

### Замечание 1

$S_{2m+1}=(c_0-c_1)+(c_2-c_3)+\ldots+(c_{2m}-c_{2m+1})\ge0$
> [!note] На полях
> [под скобками] $\ge0$; $\ge0$; $\ge0$

С другой стороны, $S_{2m+1}\le c_0\Rightarrow0\le S_{2m+1}\le c_0$
> [!note] На полях
> [стрелки вниз от $S_{2m+1}$ и от $c_0$] $m\to\infty$; $\downarrow$; $\downarrow$
> [!note] На полях
> [справа внизу] $0\le S\le c_0$
> [!note] На полях
> [внизу справа] по т. опред. монот. посл-ти переход в нер-ве ⟦S114⟧

### Замечание 2 ⟦S115⟧

$R_n=\sum\limits_{k=n+1}^{\infty}(-1)^kc_k$

> [!warning] Неразрешённые пометки страницы p027 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S111: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> M112: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> S113: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S114: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S115: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p028

$|R_n|=|S-S_n|=|(-1)^{n+1}(S-S_n)|\le c_{n+1}$ ⟦S116⟧

### Пример:

$\sum\limits_{k=1}^{\infty}\dfrac{(-1)^{k-1}}{k}=1-1/2+1/3-1/4+\ldots$

$S_{2n}=1-1/2+\ldots+\dfrac{1}{2n-1}-\dfrac{1}{2n}=1+1/2+1/3+\ldots+\dfrac{1}{2n-1}+\dfrac{1}{2n}-2\left(1/2+1/4+\ldots+\dfrac{1}{2n}\right)$
$-1/2=1/2-2\cdot1/2$
$-1/4=1/4-2\cdot1/4$ ⟦S117⟧

Положим $H_n=1+\dfrac{1}{2}+\ldots+\dfrac{1}{n}$
$H_{2n}=1+\dfrac{1}{2}+\ldots+\dfrac{1}{2n-1}+\dfrac{1}{2n}$

❶ $H_{2n}-H_n$

Формула Эйлера-Маклорена асимптотических сумм: $H_n=\ln n+C_0+\delta_n$, где $\delta_n\to0$. ⟦U118⟧

> [!warning] Неразрешённые пометки страницы p028 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S116: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S117: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U118: нечитаемо (illegible), см. `ocr/ISSUES.md`

## p029

По усл. $(a_n)$ - огр. и монотонна.

Пусть (для определенности) огр. снизу и монот. $\downarrow$
$a_1>a_2>a_3>\ldots>a_n>\ldots\ge$ ограничена снизу ⟦U119⟧
$\Rightarrow\exists$ конечный предел $\lim\limits_{n\to\infty}a_n=a$

$\alpha_n:=a_n-a\Rightarrow\alpha_n\downarrow0$

$\sum\limits_{n=1}^{\infty}a_nb_n=\sum\limits_{n=1}^{\infty}(\alpha_n+a)b_n=\sum\limits_{n=1}^{\infty}\alpha_nb_n+a\sum\limits_{n=1}^{\infty}b_n$ - сх-ся
> [!note] На полях
> [под первым слагаемым, со стрелкой] сх-ся по пр. Дирихле
> [!note] На полях
> [под вторым слагаемым, со стрелкой] сх-ся по усл. ⟦S120⟧

$\\blacksquare$

### Перестановки рядов

### Опр (7.5.1)

Пусть имеется ряд $\sum\limits_{n=1}^{\infty}a_n$ и биективное отображение $\sigma:\mathbb{N}\to\mathbb{N}$. Ряд $\sum\limits_{n=1}^{\infty}a_{\sigma(n)}$ наз. **_перестановкой_** исходного ряда $\sum\limits_{n=1}^{\infty}a_n$. ⟦S121⟧

### Переместительное св-во ряда

### Опр (7.5.2)

Будем говорить, что ряд $\sum\limits_{n=1}^{\infty}a_n$ обладает **_переместительным св-вом_**, если $\forall$ биекции $\sigma:\mathbb{N}\to\mathbb{N}$ ряд $\sum\limits_{n=1}^{\infty}a_{\sigma(n)}$ сх-ся и расх-ся одновременно с исходным рядом, и при этом $\sum\limits_{n=1}^{\infty}a_n=\sum\limits_{n=1}^{\infty}a_{\sigma(n)}$. ⟦S122⟧

> [!warning] Неразрешённые пометки страницы p029 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U119: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S120: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S121: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S122: неясная структура (unclear structure), см. `ocr/ISSUES.md`

---

Source: pages p022–p029

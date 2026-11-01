---
semester: 3
lecture: 71
topic: "Функциональные последовательности и ряды: равномерная сходимость"
source_pages: [p030, p031, p032, p033, p034, p035]
lang: ru
status: draft
---

# Лекция 71 — Функциональные последовательности и ряды: равномерная сходимость

> [!info] Происхождение текста
> Текст переписан со страниц `p030`–`p035` рукописной тетради
> (см. [`ocr/raw/`](../../ocr/raw), [`ocr/MANIFEST.md`](../../ocr/MANIFEST.md)).
> В тетради этот материал помечен как «Лекции 71–72»: пара лекций не разделена.
> Разбиение на отдельные файлы L71 и L72 проведено по границе p035/p036 (смена темы); текст не переставлялся и не дополнялся.
> Решений в `My decision` (`ocr/ISSUES.md`) нет, поэтому все пометки остаются `open`
> и продублированы предупреждениями. Ничего не добавлено: ни доказательств,
> ни примеров, ни «пропущенных шагов».

## p030

### Пример:

$\sum\limits_{k=1}^{\infty}\dfrac{(-1)^{k-1}}{k}=1-1/2+1/3-1/4+\ldots$

$S_n=\sum\limits_{k=1}^{\infty}\dfrac{(-1)^{k-1}}{k}$

$T_n$ - частичная сумма ряда, полученного перестановкой.

$1-1/2-1/4+1/3-1/6-1/8+1/5-\dfrac{1}{10}-\dfrac{1}{12}+\ldots=:T_n$ ⟦U123⟧

$T_{3m}=\sum\limits_{k=1}^{m}\left(\dfrac{1}{2k-1}-\dfrac{1}{4k-2}-\dfrac{1}{4k}\right)=\sum\limits_{k=1}^{m}\left(\dfrac{1}{4k-2}-\dfrac{1}{4k}\right)=\dfrac{1}{2}\sum\limits_{k=1}^{m}\left(\dfrac{1}{2k-1}-\dfrac{1}{2k}\right)=\dfrac{1}{2}S_{2m}$ ⟦M124⟧
> [!note] На полях
> [первое слагаемое в первой скобке обведено овалом] $\dfrac{1}{2k-1}$ ⟦S125⟧
> [!note] На полях
> [ниже, отдельной строкой с выносом] $\left(1-\dfrac{1}{2}-\dfrac{1}{4}\right)+\left(\dfrac{1}{3}-\dfrac{1}{6}-\dfrac{1}{8}\right)+\ldots$

$S_n\to\ln 2$

$T_{3m}=\dfrac{1}{2}S_{2m}\to\dfrac{1}{2}\ln 2$
$T_{3m+1}=T_{3m}+\dfrac{1}{2m+1}\to\dfrac{1}{2}\ln 2$
$T_{3m+2}=T_{3m+1}-\dfrac{1}{4m+2}\to\dfrac{1}{2}\ln 2$ ⟦S126⟧

### Переместительные св-ва рядов

1) Положительные ряды обладают переместительным св-вом
2) Абсолютно-сх-ся ряды обладают переместительным св-вом
3) Т. Римана: Если ряд сх-ся условно, то он переместительным св-вом не обладает. Более того, $\forall B\in\overline{\mathbb{R}}\ \exists\sigma:\mathbb{N}\to\mathbb{N}\ \sum\limits_{n=1}^{\infty}a_{\sigma(n)}=B$. ⟦S127⟧

> [!note] На полях
> [справа, отдельным блоком; начало следующей лекции] **_Лекции 71–72_**

· Функциональные ряды
· Равномер. сх-ть для функций посл-ти
· крит. Б-К и пр. Вейерштрасса
· Св-ва равном. сх-ся функц. рядов ⟦U128⟧

### Функциональные посл-ти и ряды. Равномерная сх-ть.

Рассм. посл-ть ф-ций $(f_n)_{n\in\mathbb{N}}$, $f_n: X\to\overline{\mathbb{R}}$, $\overline{\mathbb{R}}:=\mathbb{R}\cup\{\pm\infty\}$. Рассм. $f: X\to\overline{\mathbb{R}}$. ⟦S129⟧

> [!warning] Неразрешённые пометки страницы p030 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U123: нечитаемо (illegible), см. `ocr/ISSUES.md`
> M124: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> S125: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S126: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S127: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U128: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S129: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p031

### Опр (8.1.1)

Будем говорить, что $(f_n)$ сх-ся в $X$ к $f$ **_поточечно_**, если:
$\forall x\in X\ f_n(x)=:a_n\to a:=f(x)$ при $n\to\infty$

### Опр (8.1.1а) ⟦S130⟧

$f_n\to f$ **_поточечно на мн-ве_** $E\subset X$, если:
$\forall x\in E\subset X\ \forall\varepsilon>0\ \exists N=N(x,\varepsilon)\ \forall n>N\ |f_n(x)-f(x)|<\varepsilon$

### Опр (8.1.2)

$f_n\to f$ **_равномерно на мн-ве_** $E\subset X$, если
$\forall\varepsilon>0\ \exists N=N(\varepsilon)\ \forall x\in E\ \forall n>N\ |f_n(x)-f(x)|<\varepsilon$

Обозн.: $f_n\rightrightarrows f$ - равномерная сх-ть; $f_n\to f$ - поточечная сх-ть ⟦S131⟧
$\exists E=X\ f_n\rightrightarrows f$ на $X\Rightarrow f_n\to f$ поточечно на $X$
> [!note] На полях
> [справа от следования, две вставки со стрелками] $\Rightarrow$ равномерная сх-ть $\Rightarrow$ поточечная сх-ть

**_Обратное, вообще говоря, неверно!_**

### Пример:

> [!warning] Неразрешённые пометки страницы p031 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S130: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S131: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p032

> [!note] Технический дубликат
> Повторная съёмка страницы `p030` (тот же текст: пример с перестановкой ряда, «Переместительные св-ва рядов», заголовок «Лекции 71–72»).
> Сравнение по dHash даёт для пары p030/p032 расстояние 41 из 256 при лучшем из 16 поворотов; у всех остальных пар минимум 84, то есть эти два кадра — один и тот же лист.
> Транскрипция здесь не дублируется, чтобы не удваивать пометки в `ocr/ISSUES.md`.

> [!note] Пометок неопределённости на этой странице нет.

## p033

> [!note] Технический дубликат
> Повторная съёмка страницы `p031` (тот же текст: Опр. 8.1.1, 8.1.1а, 8.1.2, обозначение $f_n\rightrightarrows f$, пример с $f_n(x)=x^n$ и рисунки «$\varepsilon$-трубки»).
> Сравнение по dHash: минимальное расстояние для этой пары среди всех пар кадров.
> Транскрипция здесь не дублируется, чтобы не удваивать пометки в `ocr/ISSUES.md`.

> [!note] Пометок неопределённости на этой странице нет.

## p034

❶ $\exists X\subset\mathbb{R}$, $\forall n$ $f_n$ - непрерывна (в т. или на мн-ве). Будет ли $f$ непрерывна?
❷ $\exists X\subset\mathbb{R}$, $\forall n$ $f_n$ - дифф-ма (в т. или на мн-ве). Будет ли $f$ дифф-ма? Если да, то верно ли, что $f_n'\to f'$?
❸ Пусть $f_n$ интегрируемы на $[a,b]$. Будет ли интегрируема $f$? Если да, то верно ли, что $\int_a^b f_n\to\int_a^b f$? ⟦S132⟧

### Равномерная сх-ть в терминах $\varepsilon$-окрестности ⟦U133⟧

Рассм. ф-ии $f,g: X\to\mathbb{R}$

**Опр (8.3)** $\rho(f,g)=\sup\limits_{x\in X}|f(x)-g(x)|$ - равномерное уклонение ⟦A134⟧

### Опр (8.1.4)

$f_n\rightrightarrows f$, если $\forall\varepsilon>0\ \exists N\ \forall n>N\ \rho(f_n,f)<\varepsilon$

### Опр (8.1.4а)

$f_n\to f$, если $\rho(f_n,f)\to0$ при $n\to\infty$

### Равномерная сх-ть и св-ва предельных ф-ций

$f_n\to f$ на мн-ве $X$
· все $f_n$ обладают некоторым св-вом
· Спрашивается, будет ли предельная ф-ция $f$ обладать этими же св-вами?

### Непрер-ть предельной ф-ции

### Теорема (8.2.1) (о непрер-ти предельной ф-ции)

Пусть: ❶ $f_n$, $f_n\in C([a,b])$
❷ $f_n\rightrightarrows f$ на $[a,b]$.
Тогда $f\in C([a,b])$. ⟦S135⟧

> [!warning] Неразрешённые пометки страницы p034 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S132: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U133: нечитаемо (illegible), см. `ocr/ISSUES.md`
> A134: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> S135: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p035

### Д-во (т. 8.2.1):

Рассм. произвольную т. $x_0\in[a,b]$.
Докажем, что $f$ непрер. в т. $x_0$, т.е. покажем, что
$\forall\varepsilon>0\ \exists\delta>0:\ \forall x\ |x-x_0|<\delta\Rightarrow|f(x)-f(x_0)|<\varepsilon$

Возьмём $\forall\varepsilon>0$
$\exists N=N\left(\dfrac{\varepsilon}{3}\right):\ \forall n>N\ \forall x\in[a,b]\Rightarrow|f_n(x)-f(x)|<\varepsilon/3$
> [!note] На полях
> [под строкой, со стрелкой к ней] т.к. $f_n\rightrightarrows f$

◉ Рассмотрим $n$: $f_n$ (напомним, что все $f_n$ непрер. в т. $x_0$)
$\exists\delta=\delta(\varepsilon/3)\ \forall x:|x-x_0|<\delta\Rightarrow|f_n(x)-f_n(x_0)|<\varepsilon/3$

Далее, $\forall x:|x-x_0|<\delta\Rightarrow$
$\Rightarrow|f(x)-f(x_0)|=|f(x)-f_n(x)+f_n(x)-f_n(x_0)+f_n(x_0)-f(x_0)|\le$
$\le|f(x)-f_n(x)|+|f_n(x)-f_n(x_0)|+|f_n(x_0)-f(x_0)|<\varepsilon$
> [!note] На полях
> [под тремя модулями соответственно] $<\varepsilon/3$; $<\varepsilon/3$; $<\varepsilon/3$

$\\blacksquare$

### Следствие

Пусть: ❶ $f_n$, $f_n\in C([a,b])$
❷ $f_n\rightrightarrows f$ на $[a,b]$
Тогда $\lim\limits_{x\to x_0}\lim\limits_{n\to\infty}f_n(x)=\lim\limits_{n\to\infty}\lim\limits_{x\to x_0}f_n(x)$

### Д-во (сл.):

$\lim\limits_{n\to\infty}f_n(x)=f(x)$
> [!note] На полях
> [под строкой] т.к. $f_n\rightrightarrows f$, а из равномерной сх-ти следует поточечная
$\lim\limits_{x\to x_0}f(x)=f(x_0)$
> [!note] На полях
> [под строкой] в силу непрер-ти $f$, кот. следует из т. 8.2.1
$\Rightarrow\lim\limits_{x\to x_0}\lim\limits_{n\to\infty}f_n(x)=f(x_0)$

С др. стороны, имеем:
$\lim\limits_{x\to x_0}f_n(x)=f_n(x_0)$
> [!note] На полях
> [под строкой] в силу непрер-ти $f_n$
$\lim\limits_{n\to\infty}f_n(x_0)=f(x_0)$
> [!note] На полях
> [под строкой] $f_n\rightrightarrows f$, а из равномерной сх-ти следует поточечная
$\Rightarrow\lim\limits_{n\to\infty}\lim\limits_{x\to x_0}f_n(x)=f(x_0)$. $\\blacksquare$ ⟦S136⟧

> [!warning] Неразрешённые пометки страницы p035 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S136: неясная структура (unclear structure), см. `ocr/ISSUES.md`

---

Source: pages p030–p035

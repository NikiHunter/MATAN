---
semester: 3
lecture: "73-74"
topic: "Интегрирование и дифференцирование равномерно сходящихся рядов, степенные ряды, формула Коши–Адамара; Радиус сходимости, равномерная сходимость степенных рядов, теорема Абеля"
source_pages: [p042, p043, p044, p045, p046, p047, p048, p049]
lang: ru
status: draft
---

# Лекции 73–74 — Степенные ряды, формула Коши–Адамара, теорема Абеля

> [!info] Происхождение текста
> Текст переписан со страниц `p042`–`p049` рукописной тетради
> (см. [`ocr/raw/`](../../ocr/raw), [`ocr/MANIFEST.md`](../../ocr/MANIFEST.md)).
> В тетради материал помечен как «Лекции 73–74»: пара лекций не разделена.
> Страницы приведены в исходном порядке, без перестановки и без добавления текста.
> Один файл на пару: ранее созданные одиночные файлы заменены этим файлом,
> их содержимое перенесено без изменений.
> Решений в `My decision` (`ocr/ISSUES.md`) нет, поэтому все пометки остаются `open`
> и продублированы предупреждениями. Ничего не добавлено: ни доказательств,
> ни примеров, ни «пропущенных шагов».

## p042

### Интегрирование равномерно сх-ся рядов

### Теорема (8.3.2)

Имеется посл-ть ф-ций $u_n\in C([a,b])$, $\forall n\in\mathbb{N}$, и пусть $\sum\limits_{n=1}^{\infty}u_n(x)=S(x)$. Если $\sum\limits_{n=1}^{\infty}u_n(x)$ равномерно сх-ся на $[a,b]$, то $\int_a^b S(x)\,dx=\sum\limits_{n=1}^{\infty}\int_a^b u_n(x)\,dx$ ⟦S159⟧

> [!note] На полях
> [справа, отдельным блоком; начало следующей лекции] **_Лекции 73–74_**

· Св-ва равном. сх-ся функц. рядов
· Коши – Адамар
· Степенные ряды
· Абель ⟦U160⟧

### Интегрирование равномерно сх-ся рядов

### Теорема (8.3.2)

Имеется посл-ть ф-ций $u_n\in C([a,b])$, $\forall n\in\mathbb{N}$, и $\sum\limits_{n=1}^{\infty}u_n(x)=S(x)$

### Д-во (т. 8.3.2):

$S_n(x)=u_1(x)+u_2(x)+\ldots+u_n(x)$
$\int_a^b S_n(x)\,dx=\int_a^b u_1(x)\,dx+\int_a^b u_2(x)\,dx+\ldots+\int_a^b u_n(x)\,dx$

По усл. $S_n\rightrightarrows S$ на $[a,b]\Rightarrow$ по т. 8.2.2 (о предельном переходе под знаком интеграла) $\Rightarrow\int_a^b S_n(x)\,dx=\sum\limits_{k=1}^{n}\int_a^b u_k(x)\,dx$
> [!note] На полях
> [под $S_n$, стрелка вниз] $n\to\infty$ $\downarrow$
> [!note] На полях
> [под знаком суммы, стрелка вниз] $\downarrow$
> [!note] На полях
> [ниже] $\int_a^b S(x)\,dx=\sum\limits_{k=1}^{\infty}\int_a^b u_k(x)\,dx$ ⟦S161⟧

### Замечание

Условие равномерной сх-ти и даже сх-ти в каждой т. не является необходимым усл. для почленного интегрирования ряда. ⟦S162⟧

> [!warning] Неразрешённые пометки страницы p042 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S159: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U160: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S161: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S162: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p043

> [!note] Технический дубликат
> Повторная съёмка страницы `p042` (тот же текст: «Интегрирование равномерно сх-ся рядов»,
> теорема 8.3.2 с доказательством, замечание, а на полях справа — заголовок **_Лекции 73–74_**
> с программой: «Св-ва равном. сх-ся функц. рядов», «Коши – Адамар», «Степенные ряды», «Абель»).
> Транскрипция здесь не дублируется, чтобы не удваивать пометки в `ocr/ISSUES.md`.

> [!note] Пометок неопределённости на этой странице нет.

## p044

> [!note] На полях
> [красным, сверху] Если ряд можно почленно интегрировать, это не значит, что ряд равномерно сх-ся ⟦S163⟧

$\sum\limits_{n=1}^{\infty}\int_a^b u_n(x)\,dx-\int_a^b S(x)\,dx\ \nRightarrow\ \sum\limits_{n=1}^{\infty}u_n(x)$ равн. сх-ся на $[a,b]$ ⟦M164⟧

### Пример:

$\forall x$: $\sum\limits_{k=0}^{\infty}(-1)^kx^k$ или $(-1,1)$ сх-ся к $\dfrac{1}{1+x}$ ⟦U165⟧

при $x=1$ ряд расх-ся

Но! $\int_0^1\dfrac{dx}{1+x}=\ln|1+x|\Big|_0^1=\ln 2$

$\sum\limits_{k=0}^{\infty}(-1)^k\int_0^1 x^k\,dx=\sum\limits_{k=0}^{\infty}\left.\dfrac{(-1)^kx^{k+1}}{k+1}\right|_0^1=\sum\limits_{k=0}^{\infty}\dfrac{(-1)^k}{k+1}-\ln(2)$ ⟦T166⟧

Итак, равн. сх-ти нет в т. $(-1,1)$, но nevertheless почленно интегрировать можно ⟦U167⟧

### Дифференцирование равномерно сх-ся рядов

### Теорема (8.3.3)

Имеется посл-ть ф-ций $u_n\in C^1([a,b])$, $\forall n\in\mathbb{N}$ и $\sum\limits_{n=1}^{\infty}u_n(x)=S(x)$

Если: 1) $\sum u_n(x)$ сх-ся
2) $\sum u'_n(x)$ равн. сх-ся на $[a,b]$, то: $S\in C^1([a,b])$ ⟦S168⟧

> [!note] На полях
> [справа, отдельным блоком] · $\sum u_n(x)=\sum u'_n(x)=S(x)$ ⟦S169⟧

### Д-во (т. 8.3.3):

$S_n(x)=u_1(x)+\ldots+u_n(x)$

$S_n\rightrightarrows S$ поточечно ⟦A170⟧

$S'_n(x)=u'_1(x)+\ldots+u'_n(x)$

> [!note] На полях
> [под $S'_n$, стрелка вниз] $n\to\infty$ $\downarrow$
> [!note] На полях
> [ниже] $\varphi=\sum\limits_{n=1}^{\infty}u'_n(x)$

По т. о дифференцировании предельной ф-ции:

$S'(x)=\varphi(x)=\sum u'_k(x)\in C([a,b])$. $\square$ ⟦S171⟧

> [!warning] Неразрешённые пометки страницы p044 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S163: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> M164: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> U165: нечитаемо (illegible), см. `ocr/ISSUES.md`
> T166: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> U167: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S168: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S169: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> A170: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> S171: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p045

### Пример:

$\sum\limits_{k=1}^{\infty}1$ — расх-ся

$\sum\limits_{k=1}^{\infty}q^k=\sum\limits_{k=1}^{\infty}0$ — сх-ся равномерно на $[?]$ промежутка ⟦U172⟧

### Степенные ряды

### Опр (8.4.1)

Ряд вида $\sum\limits_{k=0}^{\infty}C_k(x-a)^k$, где $C_k,\ x,\ a\in\mathbb{R}$ наз. рядом
степенным рядом, числа $C_k$ наз. его коэфф-тами, а $a$ — центром. ⟦T173⟧

Степенной ряд явл. обобщением многочлена $\sum\limits_{k=0}^{\infty}C_k(x-a)^k$ и сводится
к последнему, если, начиная с некот-рого номера, $C_k=0$.

Заметим, что при $x=a$ ряд (8.4.1) сх-ся к сумме $C_0$, т.к. слагаемые с номерами $k\in\mathbb{N}$ равны нулю.

### Радиус сх-ти

### Опр (8.4.2) ⟦A174⟧

Величина $R\in[0,+\infty]$ наз. радиусом сходимости ряда $\sum\limits_{k=0}^{\infty}C_k(x-a)^k$,
если: 1) $\forall x: |x-a|<R$ ряд сх-ся
2) $\forall x: |x-a|>R$, ряд расх-ся

### Замечание

$|x-a|<R\Rightarrow(a-R,a+R)$ — интервал сх-ти для веществ. прямой

Если $R=+\infty$, то интервал сх-ти $=R$, а ряд $\sum C_k(x-a)^k$ абс. сх-ся $\forall x\in\mathbb{R}$.

Если $R=0$, то инт. сх-ти $=\varnothing$, и ряд сх-ся только при $x=a$ ⟦T175⟧

Если $0<R<+\infty$, то ряд $\sum C_k(x-a)^k$ абс. сх-ся при $|x-a|<R$,
расх-ся при $|x-a|>R$, т.е. либ. сх-ся $(a-R,a+R)$ ⟦S176⟧

> [!warning] Неразрешённые пометки страницы p045 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U172: нечитаемо (illegible), см. `ocr/ISSUES.md`
> T173: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> A174: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> T175: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> S176: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p046

### Ф-ла Коши – Адамара

В след. т. будет применено соглашение: $\dfrac{1}{+\infty}=0$, $\dfrac{1}{0}=+\infty$. ⟦A177⟧

### Теорема (8.4.1) (ф-ла Коши – Адамара)

Всякий степенной ряд $\sum\limits_{k=0}^{\infty}C_k(x-a)^k$ имеет радиус сх-ти,
и он выражается ф-лой $R=\dfrac{1}{\lim\limits_{n\to\infty}\sqrt[n]{|C_n|}}$. ⟦A178⟧

### Д-во (т. 8.4.1):

Докажем, что величина $R$, задаваемая ф-лой Коши – Адамара, ра удобн. опр. радиуса сх-ти. ⟦U179⟧

> [!note] На полях
> [слева] $|x\neq a|$ ⟦A180⟧

$k=\lim\limits_{n\to\infty}\sqrt[n]{|C_n(x-a)^n|}=\lim\left(|x-a|\sqrt[n]{|C_n|}\right)=|x-a|\lim\sqrt[n]{|C_n|}$

> [!note] На полях
> [красным, под корнем] (для $\infty$ по определению) ⟦S181⟧

Если $|x-a|<R\Rightarrow k=|x-a|\lim\sqrt[n]{|C_n|}<1\Rightarrow$ по пр. Коши ряд сх-ся

Если $|x-a|>R\Rightarrow k>1\Rightarrow$ по пр. Коши ряд расх-ся $\square$

### Абс сх-ть степенного ряда

### Замечание (8.4.1)

По пр. Коши при $|x-a|<R$ ряд $\sum\limits_{k=0}^{\infty}C_k(x-a)^k$ сх-ся абсолютно.

### Интервал сх-ти

Т. 8.4.1 позволяет сделать выводы о сх-ти степенного ряда:

- пер-во $|x-a|<R$ задаёт интервал $(a-R,a+R)$ для вещественной прямой,
  наз. интервалом сх-ти степенного ряда
- Если $R=+\infty$, то он совпадает с $\mathbb{R}$, а ряд сх-ся абс. $\forall x\in\mathbb{R}$
- Если $R=0$, то интервал сх-ти пуст, а ряд сх-ся только при $x=a$
- Если $R\in(0,\infty)$, то ряд абс. сх-ся при $|x-a|<R$ и расх-ся при $|x-a|>R$ ⟦S182⟧

> [!warning] Неразрешённые пометки страницы p046 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> A177: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> A178: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> U179: нечитаемо (illegible), см. `ocr/ISSUES.md`
> A180: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> S181: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S182: неясная структура (unclear structure), см. `ocr/ISSUES.md`

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

Source: pages p042–p049

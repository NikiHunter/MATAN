---
semester: 3
lecture: 72
topic: "Предельный переход под знаком интеграла, дифференцирование предельной функции, функциональные ряды"
source_pages: [p036, p037, p038, p039, p040, p041]
lang: ru
status: draft
---

# Лекция 72 — Предельный переход под знаком интеграла, дифференцирование предельной функции, функциональные ряды

> [!info] Происхождение текста
> Текст переписан со страниц `p036`–`p041` рукописной тетради
> (см. [`ocr/raw/`](../../ocr/raw), [`ocr/MANIFEST.md`](../../ocr/MANIFEST.md)).
> В тетради этот материал помечен как «Лекции 71–72»: пара лекций не разделена.
> Разбиение на отдельные файлы L71 и L72 проведено по границе p041/p042 (смена темы); текст не переставлялся и не дополнялся.
> Решений в `My decision` (`ocr/ISSUES.md`) нет, поэтому все пометки остаются `open`
> и продублированы предупреждениями. Ничего не добавлено: ни доказательств,
> ни примеров, ни «пропущенных шагов».

## p036

### Предельный переход под знаком интеграла

### Теорема (8.2.2) (о предельном переходе под знаком интеграла)

Пусть: ❶ $f_n$, $f_n\in C([a,b])$
❷ $f_n\rightrightarrows f$ на $[a,b]$.
Тогда: $\int_a^b f_n(x)\,dx\to\int_a^b f(x)\,dx$ при $n\to\infty$,
или $\lim\limits_{n\to\infty}\int_a^b f_n(x)\,dx=\int_a^b\left(\lim\limits_{n\to\infty}f_n(x)\right)dx$.

### Д-во (т. 8.2.2):

По т. 8.2.1 $\Rightarrow f\in C([a,b])$
$\left|\int_a^b f_n-\int_a^b f\right|=\left|\int_a^b(f_n-f)\right|\le\int_a^b|f_n-f|$
> [!note] На полях
> [под интегралом] $<\varepsilon(b-a)$ ⟦S137⟧

По усл. теоремы $f_n\rightrightarrows f$ на $[a,b]$, т.е.
$\forall\varepsilon>0\ \exists N:\ \forall n>N\ \forall x\in[a,b]\Rightarrow|f_n(x)-f(x)|<\dfrac{\varepsilon}{b-a}$
$\Rightarrow\left|\int_a^b f_n-\int_a^b f\right|\le\int_a^b|f_n-f|<\int_a^b\dfrac{\varepsilon}{b-a}\,dx=\dfrac{\varepsilon}{b-a}(b-a)=\varepsilon$

Т.е. $\int_a^b f_n\to\int_a^b f$ при $n\to\infty$. $\\blacksquare$

### Замечание

Для доказательства т. 8.2.2 была важна не только поточечная сх-ть, но и равномерная сх-ть.

### Пример:

❶ $f_n(x)=n^2x(1-x^2)^n$, $x\in[0,1]$
$f_n(x)\xrightarrow[n\to\infty]{}0\ \forall x\in[0,1]$
> [!note] На полях
> [под стрелкой, подпись к скобке] т.е. посл-ть $f_n$ поточечно сходится к 0 на $[0,1]$

В то же время
$\int_0^1 f_n=n^2\int_0^1 x(1-x^2)^n\,dx=\dfrac{n^2}{2}\int_0^1(1-x^2)^n\,d(x^2)=-\dfrac{n^2}{2}\left.\dfrac{(1-x^2)^{n+1}}{n+1}\right|_0^1=$
$=\dfrac{n^2}{2(n+1)}\xrightarrow[n\to\infty]{}+\infty$
Противоречие. ⟦S138⟧

> [!warning] Неразрешённые пометки страницы p036 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S137: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S138: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p037

❷ $f_n(x)=nx(1-x^2)^n$, $x\in[0,1]$
$f_n$ поточечно сходится к 0 на $[0,1]$
$\int_0^1 f_n=n\int_0^1 x(1-x^2)^n\,dx=\dfrac{n}{2(n+1)}\xrightarrow[n\to\infty]{}1/2$ ⟦S139⟧

❸ $f_n(x)=x^n$ на $[0,1]$
Предельная функция $f(x)=\begin{cases}0, & x\in[0,1)\\1, & x=1\end{cases}$

$\sup\limits_{[0,1]}|f_n-f|=\sup\limits_{[0,1]}x^n=1\ne0\Rightarrow f_n\ne\rightrightarrows0$ на $[0,1]$.

Но! Для любого $q\in(0,1)$
$\sup\limits_{[0,q]}|f_n-f|=\sup\limits_{[0,q]}x^n=q^n\xrightarrow[n\to\infty]{}0$
Поэтому $f_n\rightrightarrows0$ на $[0,q]$. ⟦S140⟧

❹ $f_n:[0,1]\to\mathbb{R}$
$f_n(x)=\begin{cases}0, & x>\dfrac{1}{n}\\ ?[?], & x\in(0,1/n)\\ 0, & x=0\end{cases}$ ⟦U141⟧

![](../../ocr/crops/p037_fig1.jpg)
> [!note] На полях
> [слева от ❹ — график: оси; треугольный «зубец» с основанием $[0,1/n]$, вершиной высоты $n$; подпись по оси ординат $n$] ⟦G142⟧

> [!warning] Неразрешённые пометки страницы p037 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S139: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S140: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U141: нечитаемо (illegible), см. `ocr/ISSUES.md`
> G142: нетривиальный рисунок (non-obvious figure), см. `ocr/ISSUES.md`

## p038

### Дифференцирование предельной ф-ции

### Теорема (8.2.3) (о диффер-нии предельной ф-ции)

Пусть: ❶ $\forall n$ $f_n\in C^1([a,b])$
❷ $f_n\to f$ при $n\to\infty$
❸ $f\in C^1([a,b])$ ⟦A143⟧
❹ $f_n'\rightrightarrows\varphi$ на $[a,b]$.
Тогда $\varphi\in C([a,b])$ и $f'=\varphi$,
или $\dfrac{d}{dx}\left(\lim\limits_{n\to\infty}f_n(x)\right)=\lim\limits_{n\to\infty}\left(\dfrac{d}{dx}f_n(x)\right)$. ⟦S144⟧

### Д-во (т. 8.2.3):

$\int_a^b f_n'=f_n(b)-f_n(a)$

$\int_a^x f_n'=f_n(x)-f_n(a)\ \forall x\in[a,b]$
$f_n(x)=f_n(a)+\int_a^x f_n'$
> [!note] На полях
> [под $f_n(a)$, стрелка вниз] $\downarrow$
> [!note] На полях
> [под $f_n(a)$, ниже] $f(a)$
> [!note] На полях
> [под интегралом, стрелка вниз] $\downarrow$
> [!note] На полях
> [под интегралом, ниже] $\int_a^x\varphi$
> [!note] На полях
> [справа] при $n\to\infty$ ⟦S145⟧

$f(x)=f(a)+\int_a^x\varphi$
> [!note] На полях
> [слева под строкой] по т. 8.2.2 о предельном переходе под знаком интеграла ⟦S146⟧

### Функциональные ряды ⟦A147⟧

### Опр (8.3.1)

Имеется посл-ть ф-ций $u_n(x): X\to\mathbb{R}$, $\forall n\in\mathbb{N}$
$\sum\limits_{n=1}^{\infty}u_n(x)$ - функциональный ряд.
$S_n(x)=\sum\limits_{k=1}^{n}u_k(x)$, $S(x)=\lim\limits_{n\to\infty}S_n(x)$, $S: X\to\mathbb{R}$.
Функциональный ряд сходится на мн-ве $X$, если он сх-ся в каждой т. этого мн-ва. ⟦S148⟧

> [!warning] Неразрешённые пометки страницы p038 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> A143: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> S144: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S145: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S146: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> A147: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> S148: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p039

$\forall x>0\ \forall n>1/x$ $f_n(x)=0\Rightarrow f_n\xrightarrow[n\to\infty]{}0\Rightarrow f=\lim\limits_{n\to\infty}f_n=0$.
$\int_0^1 f_n(x)\,dx=\dfrac{1}{2}\cdot\dfrac{1}{n}\cdot n=\dfrac{1}{2}\not\to0$ ⟦M149⟧
$\int_0^1 f(x)\,dx=0$
$\Rightarrow\int_0^1 f_n\not\to\int_0^1 f$ ⟦S150⟧

> [!warning] Неразрешённые пометки страницы p039 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> M149: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> S150: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p040

$\Rightarrow|S_n(x)-S_m(x)|=|S_n(x)-S(x)+S(x)-S_m(x)|\le$
$\le|S_n(x)-S(x)|+|S(x)-S_m(x)|<\varepsilon$
> [!note] На полях
> [под первым модулем] $<\varepsilon/2$
> [!note] На полях
> [под вторым модулем] $<\varepsilon/2$

⟲ Фикс. $x\in E\Rightarrow(S_n(x))_{n\in\mathbb{N}}$ - числовая посл-ть Коши
$\Rightarrow$ По крит. Б-К для числовой посл-ти $\Rightarrow$
$\Rightarrow\exists S(x):S_n(x)\to S(x)$
$S(x)$ - ф-я, т.к. фиксированное $x\in E$ было выбрано произвольно.

$\forall\varepsilon>0\ \exists N\ \forall x\in E\ \forall n>m>N\ |S_n(x)-S_m(x)|<\varepsilon$
перейдём в нер-ве $|S_n(x)-S_m(x)|<\varepsilon$ к пределу при $n\to\infty$
> [!note] На полях
> [под $|S_n(x)-S_m(x)|$, стрелка вниз] $\downarrow$
> [!note] На полях
> [под $\varepsilon$ второй строки, стрелка вниз] $\downarrow$
> [!note] На полях
> [между стрелками] $n\to\infty$
> [!note] На полях
> [ниже] $|S(x)-S_m(x)|\le\varepsilon<2\varepsilon$
> [!note] На полях
> [внизу] предельный переход в нер-ве ⟦S151⟧

**Критерий Б-К:** $\sum\limits_{n=1}^{\infty}u_n(x)$ равномерно сх-ся на $E\Leftrightarrow$
$\Leftrightarrow\forall\varepsilon>0\ \exists N\ \forall n>m>N\ |S_n(x)-S_m(x)|<\varepsilon$, где $S_n(x)=\sum\limits_{k=1}^{n}u_k(x)$
$S_m(x)=\sum\limits_{k=1}^{m}u_k(x)$

обычно используется для опровержения равномерной сх-ти ряда ⟦S152⟧

**Пример:** $\sum\limits_{k=0}^{\infty}x^k$ сх-ся к $\dfrac{1}{1-x}$ неравномерно на $[0,1)$, т.к. $x^k\not\rightrightarrows0$ на $[0,1)$

### Признак Вейерштрасса

Имеется посл-ть ф-ций $u_n(x): X\to\mathbb{R}$, $\forall n\in\mathbb{N}$ и посл-ть $(C_n)_{n\in\mathbb{N}}$, $C_n>0$ такие, что:
❶ $|u_n(x)|\le C_n$, $\forall x\in E\subset X$, $\forall n\in\mathbb{N}$
❷ Ряд $\sum\limits_{n=1}^{\infty}C_n$ сх-ся
Тогда $\sum\limits_{n=1}^{\infty}u_n(x)$ равномерно сх-ся на $E$.

### Д-во (пр. Вейерштрасса):

> [!warning] Неразрешённые пометки страницы p040 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S151: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S152: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p041

$\left|\sum\limits_{n=m+1}^{m+p}u_n(x)\right|\le\sum\limits_{n=m+1}^{m+p}|u_n(x)|\le\sum\limits_{n=m+1}^{m+p}C_n$ ⟦S153⟧
> [!note] На полях
> [под последней суммой, мелко] $p\in\mathbb{N}$, $p>1$
> [!note] На полях
> [слева внизу] $\left|\sum\limits_{n=m+1}^{m+p}u_n(x)\right|\le\sum\limits_{n=m+1}^{m+p}|u_n(x)|\le\sum\limits_{n=m+1}^{m+p}C_n$

По усл. $\sum\limits_{n=1}^{\infty}C_n$ - сх-ся $\Rightarrow\forall\varepsilon>0\ \exists N\ \forall m>N\ \left|\sum\limits_{n=m+1}^{m+p}C_n\right|<\varepsilon$
$\Rightarrow\left|\sum\limits_{n=m+1}^{m+p}u_n(x)\right|\le\left|\sum\limits_{k=m+1}^{m+p}u_k(x)\right|<\varepsilon$

**Замечание**: Ранее мы здесь в крит. Б-К $n=m+p$ ($\forall n=m+p>m>N$)
$\Rightarrow$ согласно крит. Б-К для функциональных рядов
$\sum\limits_{n=1}^{\infty}u_n(x)$ равномерно сх-ся на $E$. $\\blacksquare$ ⟦S154⟧

### Примеры:

$\sum\limits_{k=1}^{\infty}\dfrac{\sin(kx)}{k^2}$ и $\sum\limits_{k=1}^{\infty}\dfrac{\cos(kx)}{k^2}$ равномерно сх-ся на $\mathbb{R}$ по пр. Вейерштрасса, т.к. $\forall x\in\mathbb{R}$ ($E=\mathbb{R}$) $\left|\dfrac{\sin(kx)}{k^2}\right|\le\dfrac{1}{k^2}$, $\left|\dfrac{\cos(kx)}{k^2}\right|\le\dfrac{1}{k^2}$, а ряд $\sum\dfrac{1}{k^2}$ сх-ся ⟦S155⟧

### Замечание

Призн. пр. Вейерштрасса ряд $\sum\limits_{k=1}^{\infty}u_k(x)$ сх-ся на $E$ не только равномерно, но и абсолютно.
Более того, $\sum\limits_{k=1}^{\infty}|u_k(x)|$ сх-ся равномерно на мн-ве $E$, т.к. он тогда тоже удовл. усл. пр. Вейерштрасса. ⟦S156⟧

### Замечание

Случаи:
❶ Ряды, кот. сх-ся абсолютно, но не равномерно.
Например, $\sum\limits_{k=0}^{\infty}x^k$ на $(-1;1)$
❷ Ряды, кот. сх-ся равномерно, но не абсолютно.
Например, любой условно-сх-ся числовой ряд, кот. мы рассматриваем как функциональный. ⟦S157⟧

### Непрерывность суммы (равномерно сх-ся) ряда ⟦U158⟧

### Теорема (8.3.1)

Имеется ряд из ф-ций $u_n\in C([a,b])$, $\forall n\in\mathbb{N}$ и $\sum\limits_{n=1}^{\infty}u_n(x)=S(x)$. Если $\sum\limits_{n=1}^{\infty}u_n(x)$ равномерно сх-ся на $[a,b]$, то $S\in C([a,b])$

### Д-во (т. 8.3.1):

$S_n(x)=u_1(x)+u_2(x)+\ldots+u_n(x)\Rightarrow S_n(x)\in C([a,b])\ \forall n\in\mathbb{N}$
$S(x)=\lim\limits_{n\to\infty}S_n(x)\ \forall x\in[a,b]$
По усл. $\sum\limits_{k=1}^{\infty}u_k(x)$ - равномерно сх-ся на $[a,b]\Rightarrow S_n\rightrightarrows S$ на $[a,b]$.
По т. 8.2.1 (о непрер-ти предельной ф-ции) имеем: $S\in C([a,b])$. $\\blacksquare$

> [!warning] Неразрешённые пометки страницы p041 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S153: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S154: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S155: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S156: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S157: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U158: нечитаемо (illegible), см. `ocr/ISSUES.md`

---

Source: pages p036–p041

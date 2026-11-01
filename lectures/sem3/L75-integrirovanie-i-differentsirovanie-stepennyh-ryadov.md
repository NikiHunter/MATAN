---
semester: 3
lecture: 75
topic: "Интегрирование и дифференцирование степенных рядов, единственность разложения, ряд Тейлора"
source_pages: [p050, p051, p052, p053]
lang: ru
status: draft
---

# Лекция 75 — Интегрирование и дифференцирование степенных рядов, единственность разложения, ряд Тейлора

> [!info] Происхождение текста
> Текст переписан со страниц `p050`–`p053` рукописной тетради
> (см. [`ocr/raw/`](../../ocr/raw), [`ocr/MANIFEST.md`](../../ocr/MANIFEST.md)).
> В тетради этот материал помечен как «Лекции 75–76»: пара лекций не разделена.
> Разбиение на отдельные файлы L75 и L76 проведено по границе p053/p054 (смена темы); текст не переставлялся и не дополнялся.
> Решений в `My decision` (`ocr/ISSUES.md`) нет, поэтому все пометки остаются `open`
> и продублированы предупреждениями. Ничего не добавлено: ни доказательств,
> ни примеров, ни «пропущенных шагов».

## p050

### Пример на Коши – Адамара:

$\sum\limits_{n=0}^{\infty}C_nx^n$, $C_{2n+1}=0$, $C_{2n}=1$

$=1+x^2+x^4+x^6+\ldots$

$\lim\limits_{n\to\infty}S_n=\lim\limits_{n\to\infty}S_{n+1}=0\Rightarrow R=\infty$ ⟦M202⟧

$\lim\limits_{n\to\infty}S_n=\lim\limits_{n\to\infty}S_{2n}=\ldots$ ⟦U203⟧

> [!note] На полях
> [в рамке, справа вверху] 80 (15 окт) ⟦A204⟧
> [!note] На полях
> [красным, справа, отдельным блоком; начало следующей лекции] **_Лекции 75–76_**
· инт-е ф-ций ф. в абс. ?? рядов ⟦U205⟧
· радиус, ст. ряды в тейлоров, анализа ?? ⟦U206⟧
· 4 ⟦U207⟧

### Теорема (8.4.4) (об интегрировании степенных рядов)

Имеется степенной ряд $\sum C_k(x-a)^k$ и $\exists R\in(0,+\infty]$ — его радиус
сх-ти. Тогда для степенной ряд можно интегрировать почленно в интервале сх-ти, если
$[A,B]\subset(a-R,a+R)$:

$\int_A^B\sum\limits_{k=0}^{\infty}C_k(x-a)^k\,dx=\sum\limits_{k=0}^{\infty}C_k\dfrac{(B-a)^{k+1}-(A-a)^{k+1}}{k+1}$ (8.4.2)

Если, кроме того, или степенной ряд сх-ся при $x=a+R$ или $x=a-R$,
то равно (8.4.2) верно и при $B=a+R$ или $A=a-R$ соответственно. ⟦T208⟧

### Д-во (т. 8.4.4):

Не умаляя общности, считаем $a=0$.

Обозначим $r=\max\{|A|,|B|\}$. Тогда $[A,B]\subset[-r,r]\subset(-R,R)$

$\sum C_kx^k$ — равномерно сх-ся на $[-r,r]$ (по т. 8.4.2)

$\Rightarrow\sum C_kx^k$ можно почленно интегрировать по $[A,B]\subset[-r,r]$
(по т. 8.4.2), а если $[A,B]\subset(-R,R)$

Пусть $B=R\Rightarrow$ по т. Абеля (8.4.3) ряд $\sum C_kx^k$ равномерно ⟦S209⟧

> [!warning] Неразрешённые пометки страницы p050 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> M202: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> U203: нечитаемо (illegible), см. `ocr/ISSUES.md`
> A204: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> U205: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U206: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U207: нечитаемо (illegible), см. `ocr/ISSUES.md`
> T208: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> S209: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p051

сх-ся на $[0,R]$ + по т. (8.4.2) ряд $\sum\limits_{k=0}^{\infty}C_kx^k$
равномерно сх-ся на $[A,B]=[-r,r]\Rightarrow$ можно интегрировать почленно ⟦S210⟧

Случай $A=-R$ рассматривается аналогично. $\square$

### Теорема (8.4.5) (о радиусах степенных рядов)

Радиус сх-ти рядов: $\sum\limits_{k=0}^{\infty}C_k(x-a)^k$,
$\sum\limits_{k=1}^{\infty}kC_k(x-a)^{k-1}$,
$\sum\limits_{k=0}^{\infty}\dfrac{C_k}{k+1}(x-a)^{k+1}$ равны. ⟦A211⟧

### Д-во (т. 8.4.5):

Докажем совпадение радиусов сх-ти первых двух рядов

По ф-ле Коши – Адамара достаточно проверить равно:
$\lim\sqrt[n]{|nC_n|}=\lim\sqrt[n]{|C_n|}$ ⟦T212⟧

Рассмотрим $\forall\varepsilon>0$, $\exists k\in\mathbb{N}$: $k>1$, по $\exists N:\forall n>N$ ⟦U213⟧

$\sqrt[n]{|nC_n|}\le\sqrt[n]{(1+\varepsilon)^n|C_n|}$

$\lim\sqrt[n]{|nC_n|}\le\lim\sqrt[n]{|C_n|}\le(1+\varepsilon)\lim\sqrt[n]{|C_n|}$ ⟦M214⟧

Совпадение радиусов первого и третьего рядов проверяется аналогично. $\square$

### Теорема (8.4.6) (о дифференцировании степенных рядов)

Пусть $R\in(0,+\infty]$ — радиус сх-ти ряда $f(x)=\sum\limits_{k=0}^{\infty}C_k(x-a)^k$.
Тогда ф-я $(-\infty)$ цифр-ма на мн-ве $|x-a|<R$ и ряд можно
диффер-ть почленно любое число раз ⟦U215⟧

$f^{(m)}(x)=\sum\limits_{k=m}^{\infty}k(k-1)\ldots(k-m+1)C_k(x-a)^{k-m}$, $|x-a|<R$ $\forall m\in\mathbb{N}$

### Д-во (8.4.6):

Не умаляя общности, считаем, что $a=0$.

По т. 8.4.5 при дифференцировании радиус сх-ти не меняется ⇒ ф-ла
$\varphi(t)=\dfrac{t}{?}$ при $m=1$ ⟦U216⟧

> [!warning] Неразрешённые пометки страницы p051 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S210: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> A211: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> T212: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> U213: нечитаемо (illegible), см. `ocr/ISSUES.md`
> M214: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> U215: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U216: нечитаемо (illegible), см. `ocr/ISSUES.md`

## p052

Итак, $f(x)=\sum C_kx^k$, $|x|<R$

Рассм. $x_1\in(-R,R)$ и фиксируем число $f$ без $x_1$ и ф-му где, производной ⟦U217⟧

$\exists|x|<R$, $x\neq x_1$, фиксируем $\rho>0$ такое, что $|x|,|x_1|<\rho<R$

$\dfrac{f(x)-f(x_1)}{x-x_1}=\sum\limits_{k=0}^{\infty}C_k\dfrac{x^k-x_1^k}{x-x_1}=\sum C_k\left(x^{k-1}+x^{k-2}x_1+\ldots+x_1^{k-1}\right)$

$=\left|C_k\left(x^{k-1}+x^{k-2}x_1+\ldots+x_1^{k-1}\right)\right|\le k|C_k|\rho^{k-1}$ ⟦M218⟧

$\rho<R\Rightarrow\sum k|C_k|\rho^{k-1}$ — сх-ся

> [!note] На полях
> [справа] Вид интеграла: степенной ряд сх-ся абсолютно ⟦S219⟧

$\varphi(x)=\sum C_k\left(x^{k-1}+x^{k-2}x_1+\ldots+x_1^{k-1}\right)$ — равномерно
сх-ся при $(-\rho,\rho)$, тем более $\forall(-S,S)\times(x_1)$ ⟦S220⟧

По т. о почленном переходе к пределу:

$\lim\limits_{x\to x_1}\dfrac{f(x)-f(x_1)}{x-x_1}=\sum\lim C_k\left(x^{k-1}+x^{k-2}x_1+\ldots+x_1^{k-1}\right)=\sum kC_kx_1^{k-1}$

Т.к. $x_1$ — любая т. $\in(-R,R)\Rightarrow$ ф-я диффер-ма на $(-R,R)$ и ряд дифференцируем почленно. $\square$

### Теорема (8.4.7) (о единственности разложения ф-ции в степенной ряд)

Пусть $a\in\mathbb{R}$, $R\in(0,+\infty]$ — радиус сх-ти ряда $f(x)=\sum\limits_{k=0}^{\infty}C_k(x-a)^k$.
Тогда $f\in C^\infty(a-R,a+R)$, а各式? $C_k$ определяются единств-
вечным образом по ф-ле $C_k=\dfrac{f^{(k)}(a)}{k!}$ ⟦U221⟧

### Д-во (т. 8.4.7):

По т. 8.4.6 ⇒ $f^{(m)}(x)=\sum\limits_{k=m}^{\infty}k(k-1)\ldots(k-m+1)C_k(x-a)^{k-m}$ $\forall m\in\mathbb{N}$, $|x-a|<R$

Сделаем подстановку $x=a$:

$f^{(m)}(a)=m(m-1)\ldots(m-m+1)C_m+\sum\limits_{k=m+1}^{\infty}k(k-1)\ldots(k-m+1)(a-a)^{k-m}$ ⟦T222⟧

$\Rightarrow f^{(m)}(a)+m!C_m\Rightarrow C_m=\dfrac{f^{(m)}(a)}{m!}$. $\square$ ⟦M223⟧

> [!warning] Неразрешённые пометки страницы p052 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U217: нечитаемо (illegible), см. `ocr/ISSUES.md`
> M218: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> S219: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S220: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U221: нечитаемо (illegible), см. `ocr/ISSUES.md`
> T222: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> M223: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`

## p053

### Ряд Тейлора

### Опр (8.4.3)

Пусть $f$ имеет б.ч. производные всех порядков.

Числа $C_k=\dfrac{f^{(k)}(a)}{k!}$ наз. коэфф-тами Тейлора, а ряд
$\sum\limits_{k=0}^{\infty}\dfrac{f^{(k)}(a)}{k!}(x-a)^k$ — рядом Тейлора ф-ции $f$ с центром в точке $a$. ⟦A224⟧

Ряд Тейлора с центром в нуле наз. рядом Маклорена.

### Представление ф-ции вещественным степенным рядом

Из т. 8.4.6 и 8.4.7 следует, что если ф-я раскладывается в степенной
ряд в окр. т. $a$, то она бесконечно дифференцируема в этой окр., а ряд есть
её ряд Тейлора.

Пусть $a\in\mathbb{R}$, $R\in(0,+\infty]$, $f\in C^\infty(a-R,a+R)$. Тогда можно построить
ряд Тейлора ф-ции $f$: $\sum\dfrac{f^{(k)}(a)}{k!}(x-a)^k$
и задаться вопросом о её поведении. ⟦S225⟧

При $x=a$ ряд сх-ся к $f(a)$

При $x\neq a$ возможны три случая:

1) Ряд сх-ся к $f(x)$
2) Ряд расх-ся
3) Ряд сх-ся, но не к $f(x)$

### Многочлен Тейлора

Частичная сумма ряда Тейлора $T_{n,f}(x)=\sum\limits_{k=0}^{n}\dfrac{f^{(k)}(a)}{k!}(x-a)^k$ есть многочлен Тейлора.

По осп. Сумма ряда сх-ся в ряд Тейлора $f$ означает, что $T_{n,f}(x)\to f(x)$ ⟦U226⟧

### Теорема (8.4.8) (пр. разложимости ф-ции в ряд Тейлора)

Пусть: ① $f\in C^\infty(A,B)$

② $a,x\in(A,B)$, $a\neq x$

③ $\exists M\in(0,\infty)$ такое, что $\forall n\in\mathbb{N}$ и $\forall t\in(x-a,x+a)$: $|f^{(n)}(t)|\le M$ ⟦A227⟧

> [!warning] Неразрешённые пометки страницы p053 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> A224: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> S225: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U226: нечитаемо (illegible), см. `ocr/ISSUES.md`
> A227: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`

---

Source: pages p050–p053

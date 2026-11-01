---
semester: 3
lecture: "65-66"
topic: "Многомерный полином Тейлора: постановка задачи, мультииндексы, единственность; Тейлор–Пеано, Тейлор–Лагранж, неявные отображения, необходимое условие экстремума"
source_pages: [p001, p002, p003, p004, p005, p006, p007, p008, p009, p010, p011]
lang: ru
status: draft
---

# Лекции 65–66 — Многомерный полином Тейлора, формулы Тейлора, неявные отображения, экстремумы

> [!info] Происхождение текста
> Текст переписан со страниц `p001`–`p011` рукописной тетради
> (см. [`ocr/raw/`](../../ocr/raw), [`ocr/MANIFEST.md`](../../ocr/MANIFEST.md)).
> В тетради материал помечен как «Лекции 65–66»: пара лекций не разделена.
> Страницы приведены в исходном порядке, без перестановки и без добавления текста.
> Один файл на пару: ранее созданные одиночные файлы заменены этим файлом,
> их содержимое перенесено без изменений.
> Решений в `My decision` (`ocr/ISSUES.md`) нет, поэтому все пометки остаются `open`
> и продублированы предупреждениями. Ничего не добавлено: ни доказательств,
> ни примеров, ни «пропущенных шагов».

## p001

> [!note] На полях
> [в рамке, справа вверху] 3 семестр

### Лекции 65–66

· 1! многомерного полинома Тейлора
· Тейлор Пеано, Тейлор-Лагранж
· Неявная ф-я
· Экстремумы

### Формула Тейлора

$\square$ $f: E\subset \mathbb{R}^n \to \mathbb{R}^m$, $a$ - внутр. т. $E$, $s\in \mathbb{Z}_+$.

Надо построить многочлен $p:\mathbb{R}^n\to\mathbb{R}^m$ степени не выше $s$, знают ⟦U001⟧

$p(a)=f(a)$ и $f(x)=p(x)+o(\|x-a\|^s)$ $(x\to a)$ (6.5.1)

$\|x-a\|=\sqrt{(x_1-a_1)^2+(x_2-a_2)^2+\ldots+(x_n-a_n)^2}$ ⟦S002⟧

### Замечание

· $\forall \alpha\in\mathbb{Z}_+^n$ наз. мультииндексом размерности $n$.
Порядком мультииндекса $\alpha$ наз. величина $|\alpha|=\alpha_1+\ldots+\alpha_n$
· $M$ - конечное мн-во мультииндексов размерности $n$,
$\{C_\alpha\}_{\alpha\in M}$ - семейство эл-тов $\mathbb{R}^m$. Тогда отображение

$p(x)=\sum\limits_{\alpha\in M}C_\alpha x^\alpha=\sum\limits_{\alpha\in M}C_\alpha x_1^{\alpha_1}x_2^{\alpha_2}\ldots x_n^{\alpha_n}$

наз. многочленом $n$ переменных со значениями в $\mathbb{R}^m$

### Пример

$\left.\begin{array}{l} n=3 \\ m=1 \\ s=3 \end{array}\right\}$ $x=\begin{pmatrix} x_1\\ x_2\\ x_3\end{pmatrix}^{T}\in\mathbb{R}^3$, $p:\mathbb{R}^3\to\mathbb{R}^1$ ⟦S003⟧

$p(x)=p(x_1,x_2,x_3)=C_{I}x_1^3+C_{II}x_2x_3+C_{III}x_1^2x_2+C_{IV}x_1x_2x_3$

$M=\{(3,0,0),(0,1,1),(2,1,0),(1,1,1)\}$
$\underbrace{|\alpha|=3}_{}\ \underbrace{|\alpha|=2}_{}\ \underbrace{|\alpha|=3}_{}\ \underbrace{|\alpha|=3}_{}$

$\{C_\alpha\}_{\alpha\in M}=\{C_I, C_{II}, C_{III}, C_{IV}\}\ \ \forall i\ C_i\in\mathbb{R}^1$

$M_1=M\cup\{(2,1,1)\}\Rightarrow S=4$ ⟦T004⟧
> [!note] На полях
> [красным, справа] макс. порядок мультииндекса

$p_1(x)=C_V x_1^2x_2x_3+p(x)$

> [!warning] Неразрешённые пометки страницы p001 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U001: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S002: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S003: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> T004: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`

## p002

### Замечание

Если $p\neq 0$, то степенью многочлена наз. число
$\deg p=\max\{|\alpha|:\ \alpha\in M,\ C_\alpha\neq 0\}$
В противном случае мы полагаем степень $p$ равной $-\infty$.

### Опр(6.5.1)

$E\subset\mathbb{R}^n$, $a$ - внутр. т. $E$, $f: E\to\mathbb{R}^m$, $s\in\mathbb{Z}_+$. Многочлен $p:\mathbb{R}^n\to\mathbb{R}^m$
степени не выше $s$, удовлет. усл. (6.5.1), наз. многочленом Тейлора
$f$ порядка $s$ в т. $a$ и обозн. $T_{a,s}f$

### Замечание

Если многочлен Тейлора сущ., то он единственный
(D-во единственности) ⟦S005⟧

$\square$ Многочлены $p$ и $q$, $\deg p\le s$, $\deg q\le s$, ⟦S006⟧
$p(a)=f(a)$, $f(x)=p(x)+o(\|x-a\|^s)$ при $x\to a$.
$q(a)=f(a)$, $f(x)=q(x)+o(\|x-a\|^s)$ при $x\to a$
Положим $r:=p-q$. Надо показать, что $r\equiv 0$.
Не умаляя общности, считаем $a=0$.
$0=r(x)+o(\|x\|^s)$ при $x\to 0$
$\Rightarrow r(x)=o(\|x\|^s)$ при $x\to 0$
$\Rightarrow r(x)=\alpha(x)\cdot\|x\|^s$, где $\alpha(x)\to 0$ при $x\to 0$ ⟦A007⟧
$r(x)=\sum\limits_{k=0}^{s}r_k$, где $r_k$ - однородный полином степени $k$. ⟦M008⟧
$\sum\limits_{k=0}^{s}r_k(x)t^k=\sum\limits_{k=0}^{s}r_k(tx)=r(tx)=\alpha(tx)\cdot\|tx\|^s=|t|^s\alpha(tx)\|x\|^s$, $t\in\mathbb{R}$, $x\in\mathbb{R}^n$ ⟦M009⟧
$\Rightarrow r_k(x)\equiv 0$ при всех $k\in\{1,\ldots,s\}\Rightarrow r(x)\equiv 0$
$\sum\limits_{k=0}^{s}r_k(x)t^k$ - тождественный полином по $t$ степени не выше $s$ $\Rightarrow$
$\Rightarrow$ каждый коэффициент ф-и этого полинома $=0$. $o(|t|^s)=o(1)$ при $t\to 0$ ⟦T010⟧

Однородность полинома степени $k$: $\hat{p}(tx)=t^k\hat{p}(x)$ ⟦A011⟧
$\hat{p}$ - однородный полином

> [!warning] Неразрешённые пометки страницы p002 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S005: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S006: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> A007: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> M008: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> M009: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> T010: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> A011: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`

## p003

### Усиление многомерного Тейлора

· Ррч $s=0$ соотв. (6.5.1) равносильно непр-ти $f$ в т. $a$ ⟦U012⟧
$\left(f(x)=p(x)+o(\|x-a\|^0)=p(x)+o(1)\right)$
· Ррч $s=1$ соотв. (6.5.1) равносильно дифф-ти $f$ в т. $a$
$\left(f(x)=p(x)+o(\|x-a\|)\right)$
· Случай $s\ge 2$ исследуется сложнее
· Для ф-и одной переменной известно, что сущ-е $T_{a,s}f$ влечет
сущ-е $s$-кратной дифф-ти $f$ в т. $a$. Аналогичный результат
будет справедлив и в многомерном случае

### Лемма (6.5.1)

$\square$ $E\subset\mathbb{R}^n$, $a$ - внутр. т. $E$, $s\in\mathbb{N}$, отображение $f: E\to\mathbb{R}^m$ дифф-мо в т. $a$,
причем $f$ и все ее частные производные по-
рядка не больше $s$ равны нулю в т. $a$. Тогда
$f(a+h)=o(\|h\|^s)$ при $h\to 0$.

### D-во (леммы 6.5.1)

Т.к. достаточно проверить утв. для координатных ф-й $f$, то
можно считать $m=1$. ⟦S013⟧
Д-во проведем индукцией по $s$.
База: $s=1$. $f(a+h)=f(a)+\sum\limits_{k=1}^{n}\dfrac{\partial f}{\partial x_k}(a)h_k+o(\|h\|)=o(\|h\|)\ (h\to 0)$ ⟦T014⟧
Шаг. предполож.: утв. верно для некоторого $s$.
Шаг. переход: $s\mapsto s+1$
$f$ - дифф-ма $s+1$ раз в т. $a$ $\Rightarrow$ все частные производные $f$ первого порядка
$s$ раз дифф-мы в т. $a$.
Применим к частным производным $f$ 1-го порядка инд. предположение
$\dfrac{\partial f}{\partial x_k}(a+h)=o(\|h\|^s)$ при $h\to 0$ при всех $k\in\{1,\ldots,n\}$ $\Rightarrow$
$\forall \varepsilon>0\ \exists\delta>0$ такое что $\forall k\in\{1,\ldots,n\}$ $\left|\dfrac{\partial f}{\partial x_k}(a+h)\right|\le\dfrac{\varepsilon}{n}\|h\|^s$ при всех $\|h\|<\delta$ ⟦S015⟧
Пусть $h\in V_\delta(0)$. По лемме 6.4.1 $\exists c^1,\ldots,c^n\in V_\delta(a)$ такие, что

> [!warning] Неразрешённые пометки страницы p003 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U012: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S013: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> T014: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> S015: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p004

$f(a+h)=f(a+h)-f(a)=\sum\limits_{k=1}^{n}\dfrac{\partial f}{\partial x_k}(c^k)h_k$ ⟦T016⟧
$\underbrace{\qquad\qquad}_{0\ \text{по усл.}}$
Тогда $\left|f(a+h)\right|=\left|\sum\limits_{k=1}^{n}\dfrac{\partial f}{\partial x_k}(c^k)h_k\right|\le\sum\limits_{k=1}^{n}\left|\dfrac{\partial f}{\partial x_k}(c^k)\right||h_k|\le\sum\limits_{k=1}^{n}\dfrac{\varepsilon}{n}\|h\|^s|h|\le$ ⟦S017⟧
$=\varepsilon\|h\|^{s+1}\Rightarrow f(a+h)=o(\|h\|^{s+1})$ при $h\to 0$. $\blacksquare$

### Р-во Тейлора-Пеано

### Теорема (6.5.1)

$\square$ $E\subset\mathbb{R}^n$, $a$ - внутр. т. $E$, $s\in\mathbb{Z}_+$, отображение $f: E\to\mathbb{R}^m$ $s$ раз
дифф-мо в т. $a$. Тогда справедливо равенство

$f(x)=\sum\limits_{|\alpha|\le s}\dfrac{1}{\alpha!}\dfrac{\partial^\alpha f}{\partial x^\alpha}(a)(x-a)^\alpha+o(\|x-a\|^s)$ при $x\to a$.

Иными словами, многочлен Тейлора порядка $s$ в т. $a$ сущ. и
вычисляется по формуле $T_{a,s}f(x)=\sum\limits_{|\alpha|\le s}\dfrac{1}{\alpha!}\dfrac{\partial^\alpha f}{\partial x^\alpha}(a)(x-a)^\alpha$.
Суммирование здесь ведется по всем мультииндексам порядка $\le s$.

$\dfrac{\partial^\alpha f}{\partial x^\alpha}(a)=\dfrac{\partial^{\alpha_1+\alpha_2+\ldots+\alpha_n}}{\partial x_1^{\alpha_1}\partial x_2^{\alpha_2}\ldots\partial x_n^{\alpha_n}}$ ⟦T018⟧ $\alpha=(\alpha_1,\alpha_2,\ldots,\alpha_n)$

### Пример:
$\alpha=(0,2,3,1)$; $\dfrac{\partial^{(0,2,3,1)}f}{\partial x^{(0,2,3,1)}}=\dfrac{\partial^0}{\partial x_1^0}\dfrac{\partial^2}{\partial x_2^2}\dfrac{\partial^3}{\partial x_3^3}\dfrac{\partial^1}{\partial x_4^1}f$ ⟦T019⟧

$D^2u=\begin{pmatrix}\dfrac{\partial^2u}{\partial x_1^2} & \dfrac{\partial^2u}{\partial x_1\partial x_2}\\[2mm] \dfrac{\partial^2u}{\partial x_2x_1} & \dfrac{\partial^2u}{\partial x_2^2}\end{pmatrix}$ ⟦S020⟧

$\dfrac{1}{\alpha!}=\dfrac{1}{\alpha_1!\,\alpha_2!\ldots\alpha_n!}$ ⟦A021⟧ $\ |\alpha|=\alpha_1+\alpha_2+\ldots+\alpha_n$

### D-во (теоремы 6.5.1)

Положим $p(x)=\sum\limits_{|\alpha|\le s}\dfrac{1}{\alpha!}\dfrac{\partial^\alpha f}{\partial x^\alpha}(a)(x-a)^\alpha$, $F:=f-p$
Если $\alpha$ - мультииндекс порядка не больше $s$, то
$\dfrac{\partial^\alpha F}{\partial x^\alpha}(a)=\dfrac{\partial^\alpha f}{\partial x^\alpha}(a)-\dfrac{\partial^\alpha p}{\partial x^\alpha}(a)=0$
Применим к $F$ лемму 6.5.1. Получим
$F(x)=f(x)-p(x)=F(a+x-a)=o(\|x-a\|^s)$ при $x\to a$. $\blacksquare$

> [!warning] Неразрешённые пометки страницы p004 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> T016: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> S017: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> T018: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> T019: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> S020: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> A021: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`

## p005

### Замечание

· Отображение $R_{a,s}f=f-T_{a,s}f$ наз. остатком в формуле Тейлора
· Т. о. т. 6.5.1 можно записать как $R_{a,s}f(x)=O(\|x-a\|^s)$ $(x\to a)$ ⟦T022⟧
· Многочлен Тейлора можно выразить через дифференциалы
высших порядков: $T_{a,s}f(x)=\sum\limits_{k=0}^{s}\dfrac{d_a^kf(x-a)}{k!}$
· Если отображение $f$ есть многочлен степени не выше $s$, то $R_{a,s}f\equiv 0$, т. е. $f(x)=\sum\limits_{|\alpha|\le s}\dfrac{1}{\alpha!}\dfrac{\partial^\alpha f}{\partial x^\alpha}(a)(x-a)^\alpha$

### Формулы Тейлора-Лагранжа для ф-ий

Положим $\Delta_{a,b}=\{a+t(b-a):t\in[0,1]\}$, $\hat{\Delta}_{a,b}=\Delta_{a,b}\setminus\{a,b\}$

### Теорема (6.5.2)

$\square$ Тип-во $E$ открыто в $\mathbb{R}^n$, $s\in\mathbb{N}$, $s\in\mathbb{Z}_+$, ф-я $f: E\to\mathbb{R}$ дифф-ма ⟦T023⟧
$s+1$ раз на $E$, причем $a\in E$ и $\Delta_{a,x}\subset E$. Тогда $\exists c\in\hat{\Delta}_{a,x}$, для кот.

$f(x)=\sum\limits_{k=0}^{s}\dfrac{d_a^kf(x-a)}{k!}+\dfrac{d_c^{s+1}f(x-a)}{(s+1)!}$ ⟦T024⟧

### D-во (теорема 6.5.2)

$h:=x-a$, $F(t)=f(a+th)$, $t\in[0,1]\Rightarrow F'(t)=d_{a+th}f(h)$

> [!warning] Неразрешённые пометки страницы p005 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> T022: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> T023: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> T024: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`

## p006

$=d_{a+th}^kf(h)$, т.е. $(*)$ доказана
Теперь имея $(*)$, можно сказать, что $F$ $(s+1)$ раз дифф-ма на $[0,1]$, и
$F^{(k)}(t)=d_{a+th}^kf(h)$
Применим к $F$ одномерную ф-лу Тейлора-Лагранжа

$\Rightarrow F(1)=\sum\limits_{k=0}^{s}\dfrac{F^{(k)}(0)}{k!}(1-0)^k+\dfrac{F^{(s+1)}(\theta)}{(s+1)!}(1-0)^{s+1}$

$f(a+h)=f(x)$ ⟦T025⟧

$\sum\limits_{k=0}^{s}\dfrac{F^{(k)}(0)}{k!}(1-0)^k=\sum\limits_{k=0}^{s}\dfrac{d_a^kf(x-a)}{k!}$

$\dfrac{F^{(s+1)}(\theta)}{(s+1)!}(1-0)^{s+1}=\dfrac{d_{a+\theta h}^{s+1}f(x-a)}{(s+1)!}$

$\Rightarrow f(x)=\sum\limits_{k=0}^{s}\dfrac{d_a^kf(x-a)}{k!}+\dfrac{d_{a+\theta h}^{s+1}f(x-a)}{(s+1)!}$

Осталось положить $c=a+\theta h$. $\blacksquare$

### Следствие

В усл. т. 6.5.2 справедлива оценка
$\left|R_{a,s}f(x)\right|\le\sup\limits_{c\in\hat{\Delta}_{a,x}}\dfrac{\left|d_c^{s+1}f(x-a)\right|}{(s+1)!}$

### Теорема о среднем

### Теорема (6.5.3)

$\square$ Тип-во $E$ открыто в $\mathbb{R}^n$, $s\in\mathbb{Z}_+$, ф-я $f: E\to\mathbb{R}$ дифф-ма на $E$, $a,b\in E$,
причем $a\neq b$ и $\Delta_{a,b}\subset E$. Тогда $\exists c\in\hat{\Delta}_{a,b}$, для кот.
$f(b)-f(a)=d_cf(b-a)$
> [!note] На полях
> [красным, под теоремой] Это частный случай т. 6.5.2 соответствующий $s=0$

### Пример:

Для отобр. мест. перест. неверны ч. 6.5.2 и т. 6.5.3 ⟦U026⟧
$\square$ Д-ть-р-ери $f:\mathbb{R}\to\mathbb{R}^2$: $f(x)=(\cos x,\sin x)$, $x\in\mathbb{R}$ ⟦U027⟧
Тогда отобр. $f$ дифф-мо на $\mathbb{R}$ и $f'(x)=(-\sin x,\cos x)\ \forall x\in\mathbb{R}$ ⟦S028⟧

> [!warning] Неразрешённые пометки страницы p006 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> T025: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> U026: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U027: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S028: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p007

### Ф-ла Тейлора-Лагранжа для отображений

### Теорема (6.5.4)

$\square$ Тип-во $E$ открыто в $\mathbb{R}^n$, $s\in\mathbb{Z}_+$, отображение $f: E\to\mathbb{R}^m$
дифференцируемо $s+1$ раз на $E$, $a,x\in E$ причем $a\neq x$ и $\Delta_{a,x}\subset E$. Тогда

$\left\|f(x)-\sum\limits_{k=0}^{s}\dfrac{d_a^kf(x-a)}{k!}\right\|\le\dfrac{1}{(s+1)!}\sup\limits_{c\in\hat{\Delta}_{a,x}}\left\|d_c^{s+1}f(x-a)\right\|$ (6.5.2)

### Оценка остатка в ф-ле Тейлора

В усл. т. 6.5.4 неясно, будет ли правая часть (6.5.2) конечна.
Ответ на этот вопрос накладывается на отображение $C^{s+1}(E,\mathbb{R}^m)$ ⟦U029⟧

### Теорема (6.5.5)

$\square$ Тип-во $E$ открыто в $\mathbb{R}^n$, $s\in\mathbb{Z}_+$, $f\in C^{s+1}(E,\mathbb{R}^m)$, $a,x\in E$ причем
$a\neq x$ и $\Delta_{a,x}\subset E$. Положим $M=\max\limits_{\alpha\in M_{s+1}}\sup\limits_{c\in\hat{\Delta}_{a,x}}\left\|\dfrac{\partial^\alpha f}{\partial x^\alpha}(c)\right\|$. ⟦A030⟧
Тогда $M<\infty$ и справедливо нер-во:

$\left\|R_{a,s}f(x)\right\|\le\dfrac{M}{(s+1)!}\left(\sqrt{n}\,\|x-a\|\right)^{s+1}$

### Неявные отображения

Пусть дано $f: E\subset\mathbb{R}^2\to\mathbb{R}$. Рассм. ур-е отн. переменных $x$ и $y$
$f(x,y)=0$, $(x,y)\in E$ (6.6.1)
Ур-е (6.6.1) задает зависимость м/у $x$ и $y$, кот. наз.
неявной.
Предположим, что из (6.6.1) можно однозначно выразить одну
переменную через другую. Тогда мн-во решений (6.6.1)
представляет собой график некоторой ф-и $\varphi$, т. е. имеет вид
$\{(x,y)\in E:\ y=\varphi(x)\}$
Такую ф-ю $\varphi$ наз. неявной ф-ей, порожденной ур-ем (6.6.1)

$x^2+y^2=1$
$\left\{\begin{array}{l}y=\sqrt{1-x^2},\ y>0\\ y=-\sqrt{1-x^2},\ y<0\end{array}\right.$ $\ y=f(x)$ ⟦A031⟧

> [!warning] Неразрешённые пометки страницы p007 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U029: нечитаемо (illegible), см. `ocr/ISSUES.md`
> A030: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> A031: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`

## p008

· Вопрос о неявной ф-и всегда сложен
· В многих приложениях достаточно рассм. (6.6.1) не на всей $E$, а
только в некоторой окрестности какой-либо т. или-бо т. $E$ ⟦U032⟧
· Если вблизи любой т. $E$ ур-е (6.6.1) порождает неявную ф-ю,
то оно наз. локально разрешимым, а сама неявная ф-я - локальной.
· Для изучения локальной разрешимости удобно использовать
теорему дифференцируемого исчисления ⟦A033⟧

Пусть $a=(x^0,y^0)$ - внутр. т. мн-ва $E$, $f(x^0,y^0)=0$ и $f$ дифф-ма в т. $a$.
Если $f(x,y)=0$ и $(x,y)$ достаточно близко к $a$, то можно записать
$0=f(x,y)-f(x^0,y^0)\approx\dfrac{\partial f}{\partial x}(a)(x-x^0)+\dfrac{\partial f}{\partial y}(a)(y-y^0)$
Рассм. лин. ур-е: $\dfrac{\partial f}{\partial x}(a)(x-x^0)+\dfrac{\partial f}{\partial y}(a)(y-y^0)=0$
Из него можно однозначно выразить $y$ через $x$, если
$\dfrac{\partial f}{\partial y}(a)\neq 0$, и $x$ через $y$, если $\dfrac{\partial f}{\partial x}(a)\neq 0\Rightarrow$ Дост. усл. локаль-
ной разрешимости (6.6.1) вблизи $a$ явл. соотн. $\operatorname{grad}f(a)\neq 0$

### Задача о неявной ф-и

Обобщим теперь постановку задачи о неявной ф-и. $m,n\in\mathbb{N}$,
$f: E\subset\mathbb{R}^{n+m}\to\mathbb{R}^m$. Рассм. систему ур-й
$\left\{\begin{array}{l}f_1(x_1,\ldots,x_n,y_1,\ldots,y_m)=0\\ \ldots\\ f_m(x_1,\ldots,x_n,y_1,\ldots,y_m)=0\end{array}\right.$ (6.6.2)
Будем записывать эл-ты $\mathbb{R}^{n+m}$ в виде $(x,y)$, где $x\in\mathbb{R}^n$, $y\in\mathbb{R}^m$.
Тогда система (6.6.2) эквив. векторному ур-ю отн. двух
векторных переменных: $f(x,y)=0$, $(x,y)\in E$. (6.6.3)

### Локальная разрешимость (6.6.3) отн. $y$

Пусть $a=(x^0,y^0)$ - внутр. т. мн-ва $E$, кот. удовлет. (6.6.3), а отобр. $f$ дифф-мо в т. $a$.
Заметим, что $\forall$ в-ра $(dx,dy)\in\mathbb{R}^n\times\mathbb{R}^m$ ⟦A034⟧

> [!warning] Неразрешённые пометки страницы p008 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U032: нечитаемо (illegible), см. `ocr/ISSUES.md`
> A033: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> A034: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`

## p009

$d_af(dx,dy)=\sum\limits_{i=1}^{n}\dfrac{\partial f}{\partial x_i}(a)dx_i+\sum\limits_{j=1}^{m}\dfrac{\partial f}{\partial y_j}(a)dy_j=f'_x(a)dx+f'_y(a)dy$ (6.6.4)
$f'_x(a)=\left(\dfrac{\partial f_k}{\partial x_i}(a)\right)$, $f'_y(a)=\left(\dfrac{\partial f_k}{\partial y_j}(a)\right)$ ⟦S035⟧
Если $(x,y)$ - решение ур-я (6.6.3), достаточно близкое к $a$, то
$0=f(x,y)-f(x^0,y^0)\approx d_af(x-x^0,y-y^0)$
Это эквив. лин. системе: $f'_x(a)(x-x^0)+f'_y(a)(y-y^0)=0$
Эта система разрешима отн. $y$, если матрица $f'_y(a)$ обратима. Оказывается,
что при этом ун. ур-е (6.6.3) также однозначно разрешимо вблизи т. $a$ отн. $y$. ⟦U036⟧

### Теорема о неявном отображении

### Теорема (6.6.1)

$\square$ Тип-во $E$ открыто в $\mathbb{R}^{n+m}$, $(x^0,y^0)\in E$, $s\in\mathbb{N}$, $f\in C^s(E,\mathbb{R}^m)$, причем
$f(x^0,y^0)=0$ и $\det f'_y(x^0,y^0)\neq 0$
Тогда $\exists V(x^0,y^0)$, открытое в $\mathbb{R}^n$ мн-во $U$, содержащее $x^0$, и отобр.
$\varphi\in C^s(U,\mathbb{R}^m)$, для кот.
$\{(x,y)\in V(x^0,y^0):\ f(x,y)=0\}=\{(x,\varphi(x)):\ x\in U\}$
Т. о. мн-во решений (6.6.3) вблизи $(x^0,y^0)$ представляет собой
график отобр. $\varphi$, имеющего тот же класс гладкости, что и $f$. ⟦T037⟧

![[p009_fig1]]

> [!note] На полях
> [подпись рисунка, слева внизу] $U\times\varphi(U)=V(x^0,y^0)$ ⟦G038⟧

> [!warning] Неразрешённые пометки страницы p009 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S035: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U036: нечитаемо (illegible), см. `ocr/ISSUES.md`
> T037: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> G038: нетривиальный рисунок (non-obvious figure), см. `ocr/ISSUES.md`

## p010

### Опр (6.6.1)

Отображение $\varphi$, введенное в т. 6.6.1 наз. неявным отображением, порож-
денным ур-ем $f(x,y)=0$ в окр. т. $(x^0,y^0)$

### Замечание

Т. обозн. т. 6.6.1 отобр. $f: E\to\mathbb{R}^m$ дифф-мо на $V(x^0,y^0)$ и ⟦U039⟧
$g(x)=f(x,\varphi(x))$ $(x\in U)$
Тогда справедлива ф-ла:
$g'(x)=f'_x(x,\varphi(x))+f'_y(x,\varphi(x))\varphi'(x)$ ⟦M040⟧

### Экстремум ф-и нескольких переменных

Для иссл. ур-и 1 переменной: ⟦U041⟧
1) С помощью необходимого усл. отбрасываются точки, в кот. экстремума за-
ведомо не может быть.
2) Затем для каждой из оставшихся точек мы с помощью достаточного усл.
проверяем, есть ли в ней экстремум и какого он типа.
Аналогичная схема реализуется и для ф-и нескольких переменных.
Другая важная задача - нахождение наибольшего и наименьшего
значений ф-и, заданной на компактном мн-ве $\mathbb{R}^n$
Для нахождения экстремума ф-и на отрезке сравнивают её значения
внутри отрезка и на концах промежутка.
Если ф-я задана на компактном мн-ве $E\subset\mathbb{R}^n$, то вместо концов отрезка
нужно рассм. мн-во всех т. $E$, не явл. внутренними, т. е. границу $E$.
Исследование ф-и на границе $E$ приводит к понятию условного экстре-
мума, кот. бессодержательно в одномерном случае. ⟦A042⟧

> [!warning] Неразрешённые пометки страницы p010 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U039: нечитаемо (illegible), см. `ocr/ISSUES.md`
> M040: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> U041: нечитаемо (illegible), см. `ocr/ISSUES.md`
> A042: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`

## p011

### Экстремумы ф-и

### Опр. (6.7.1)

Предположим, что $E\subset\mathbb{R}^n$, $a\in E$, $f: E\to\mathbb{R}$.
· $\exists$ такая $V(a)$ с.о., что $f(x)\ge f(a)\ \forall x\in V(a)\cap E$. Тогда $a$ наз. ⟦S043⟧
т. минимума $f$.
· Если $f(x)\le f(a)\ \forall x\in V(a)\cap E$, то $a$ наз. т. максимума $f$
· $\exists$ такая $V(a)$ с.о., что $f(x)>f(a)\ \forall x\in\mathring{V}(a)\cap E$. Тогда $a$ наз. точкой
строгого минимума $f$
· Если $f(x)<f(a)\ \forall x\in\mathring{V}(a)\cap E$, то $a$ наз. т. строгого максимума $f$.
· Если $a$ явл. т. минимума или максимума $f$, то ее наз. т. экстремума
$f$ ⟦S044⟧

### Необходимое усл. экстремума ф-и нескольких переменных

### Теорема (6.7.1)

$\square$ $E\subset\mathbb{R}^n$, $a$ - внутр. т. $E$, ф-я $f: E\to\mathbb{R}$ дифф-ма в т. $a$. Если
$a$ явл. т. экстремума $f$, то $d_af=0$

### Замечание

Утв. т. означает, что $\operatorname{grad}f(a)=0$, или, более подробно,
$\dfrac{\partial f}{\partial x_k}(a)=0\ \forall k\in\{1,\ldots,n\}$. Такую т. $a$ наз. стационарной т. ф-и $f$.

### D-во (т. 6.7.1):

Будем считать для определенности, что $a$ - т. минимума $f\Rightarrow$
$\exists\delta>0$ такое, что $f(x)\ge f(a)\ \forall x\in V_\delta(a)$
$\exists h\in\mathbb{R}^n\setminus\{0\}$, т. е. $h=(h_1,\ldots,h_n)$ и хотя бы одна из $h_i\neq 0\Rightarrow$
$\Rightarrow\|h\|\neq 0$.
Положим $F(t)=f(a+th)$, где $t\in\left(-\dfrac{\delta}{\|h\|},\dfrac{\delta}{\|h\|}\right)\Rightarrow$

> [!warning] Неразрешённые пометки страницы p011 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S043: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S044: неясная структура (unclear structure), см. `ocr/ISSUES.md`

---

Source: pages p001–p011

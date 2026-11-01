---
semester: 3
lecture: 77
topic: "Интегрирование интеграла по параметру, несобственные интегралы, критерии равномерной сходимости"
source_pages: [p058, p059, p060, p061, p062]
lang: ru
status: draft
---

# Лекция 77 — Интегрирование интеграла по параметру, несобственные интегралы, критерии равномерной сходимости

> [!info] Происхождение текста
> Текст переписан со страниц `p058`–`p062` рукописной тетради
> (см. [`ocr/raw/`](../../ocr/raw), [`ocr/MANIFEST.md`](../../ocr/MANIFEST.md)).
> В тетради этот материал помечен как «Лекции 77–78»: пара лекций не разделена.
> Разбиение на отдельные файлы L77 и L78 проведено по границе p062/p063 (смена темы); текст не переставлялся и не дополнялся.
> Решений в `My decision` (`ocr/ISSUES.md`) нет, поэтому все пометки остаются `open`
> и продублированы предупреждениями. Ничего не добавлено: ни доказательств,
> ни примеров, ни «пропущенных шагов».

## p058

$+(x^2-n^2)\cos(n\varphi-x\sin\varphi)]\,d\varphi=\int_0^\pi\left[(1-\sin^2\varphi)x^2\times\right.$
$\left.\times\cos(n\varphi-x\sin\varphi)+x\sin\varphi\sin(n\varphi-x\sin\varphi)+n^2\cos(n\varphi-x\sin\varphi)\right]d\varphi$

$=\int_0^\pi[-(n+x\cos\varphi)\sin(n\varphi-x\sin\varphi)]'_\varphi=\left.0\right|_{0}^{\pi}$ $\checkmark$ ⟦M256⟧

> [!note] На полях
> [красным, справа, отдельным блоком; начало следующей лекции] **_Лекции 77–78_**
· инт-е инт-ла по параметру для собств. интегр. ⟦U257⟧
· т-бы о несобств. интегр. зависящего от параметра ⟦U258⟧
· св-ва Ганна-ф-ций ⟦U259⟧

### Об интегрировании интеграла по параметру

### Теорема (9.1.3)

$|P=\{(x,y)\in\mathbb{R}^2: a\le x\le b,\ c\le y\le d\}$. Далее $f=f(x,y)\in C(P)$.
Тогда ф-я $I(y)=\int_a^b f(x,y)\,dx$ интегрируема $\forall[c,d]$ и имеет
место равно:

$\int_c^d\left(\int_a^b f(x,y)\,dx\right)dy=\int_a^b\left(\int_c^d f(x,y)\,dy\right)dx$

### Пример

$I(b)=\int_0^1\dfrac{x^b-x^a}{\ln x}\,dx$

> [!note] На полях
> [оранжевым] /b- граница, а- параметр ⟦A260⟧
> [!note] На полях
> [оранжевым, ниже] // Идея: представить подынтегральную ф-цию интегралом ⟦S261⟧

$I(b)=\int_0^1\left(\int_a^b\varphi(z)\,dz\right)dx$

Рассм. $\int_0^1x^s dx<+\infty\Rightarrow b>-1$

$\int_a^b>-1\Rightarrow I(b)=\int_0^1\left(\int_a^bx^z\,dz\right)dx=\int_a^b\left(\int_0^1 x^z\,dx\right)dx$ ⟦M262⟧

$\left[\left(\dfrac{x}{\ln x}\right)b-\dfrac{\ln x\cdot x^b}{\ln x}=\dfrac{x^b}{?}\right]_0^1=\int_a^b\dfrac{dz}{z+1}=\ln|1+z|\Big|_a^b=\ln\dfrac{b+1}{a+1}$ ⟦U263⟧

> [!warning] Неразрешённые пометки страницы p058 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> M256: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> U257: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U258: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U259: нечитаемо (illegible), см. `ocr/ISSUES.md`
> A260: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> S261: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> M262: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> U263: нечитаемо (illegible), см. `ocr/ISSUES.md`

## p059

### Мотивирующий пример наособенности-апп. сходимости: ⟦U264⟧

$I(y)=\int_0^1\dfrac{x+y}{x^{y/3}}\,dx$, $x\in(0,1]$, $y\in[0,+\infty)$ ⟦U265⟧

$I(y)=\int_0^1x^{-y}dx+\int_0^1x^{y-3}dx=\left.\dfrac{x^{y+1}}{y+1}\right|_0^1+\left.y\dfrac{x^3}{3}\right|_0^1=\dfrac{1}{y+1}+1$ ⟦U266⟧

т.е. $x\in(0,1]\Rightarrow I(y)\to2$ ⟦U267⟧

С другой стороны, $y=0$: $I(0)=\int_0^1\dfrac{x}{x}dx=\int_0^1 1\,dx=1\Rightarrow$
$\Rightarrow\left|I(y)-\dfrac{2}{y\to0}\right|\not\to I(0)$ ⟦M268⟧

### Несобств. интегр., зависящие от параметра

I∞-я $f(x,y)$ задана на мн-ве $[a,b)\times Y$. Будем считать,
что $\forall$ фиксированном $y$. ⟦U269⟧

Рассм. несобств. инт.
$I(y):=\int_a^b f(x,y)\,dx=\lim\limits_{\omega\to b}\int_a^\omega f(x,y)\,dx=\lim I_\omega(y)$ ⟦A270⟧

### Опр (9.2.1)

Будем говорить, что $I(y)$ сходится равномерно отн. $Y$,
если $\forall\varepsilon>0\ \exists b_0\in[a,b)$ такое, что
$\forall b'>b_0\ |I_{b'}(y)-I(y)|<\varepsilon$ ⟦S271⟧

Другими словами, для равномерной сх-ти несобств. интеграла $I(y)$
требуется, чтобы $I_{b'}(y)\rightrightarrows I(y)$, $b\to b$. ⟦T272⟧

### Замечание

В опр. (9.2.1) существенно, что $b_0$ не зависит от $y$, а зависит только от $\varepsilon$.

Функциональный ряд $\sum\limits_{n=1}^{\infty}a_n(y)=S(y)$ сх-ся, если:
$S_n(y)=\sum a_n(y)\rightrightarrows S(y)$ ⟦T273⟧

> [!warning] Неразрешённые пометки страницы p059 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U264: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U265: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U266: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U267: нечитаемо (illegible), см. `ocr/ISSUES.md`
> M268: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> U269: нечитаемо (illegible), см. `ocr/ISSUES.md`
> A270: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> S271: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> T272: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> T273: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`

## p060

Интеграл $I_t(y)\rightrightarrows I(y)$ | Ряд $S_n(y)\rightrightarrows S(y)$

### Критерий Больцано – Коши

> Интеграл: $\forall\varepsilon>0\ \exists b_0\in[a,b):\forall t_1,t_2\in(b_0,b)$
> $\left|\int_{t_1}^{t_2}f(x,y)\,dx\right|<\varepsilon$
> Ряд: $\forall\varepsilon>0\ \exists n_0\in\mathbb{N}:\forall m>n>n_0$
> $\left|\sum\limits_{k=n}^{m}a_k(y)\right|<\varepsilon$
> [!note] На полях
> [слева от интеграла, ось с точками $a$, $b_0$, $t_1$, $b_2$, $b$] ⟦G274⟧
> [!note] На полях
> [справа от ряда, ось с точками $n_0$, $n$, $m$] ⟦G275⟧

### Д-во (крит. Б-К для несобств. интегр.) вкратце

$\left|\int_{t_1}^{t_2}f(x,y)\,dx\right|<\varepsilon\Leftrightarrow$ соотношению $|I_{t_2}(y)-I_{t_1}(y)|<\varepsilon$

$\Rightarrow$ Утверждению о равномерной сх-ти на $Y$ следует опираться
ф-ций $I_t(y)$, зависящих от параметра $t$. ⟦S276⟧

### Признак Вейерштрасса

> Интеграл: Э ф-я $Y$ такая, что $\forall x\in[a,b),\forall y\in Y\ |f(x,y)|\le\varphi(x)$
> 1) $\int_a^b\varphi(x)\,dx\le\infty$ $\Rightarrow I(y)$ равномерно сх-ся на $Y$
> Ряд: $\exists C_n>0$ такое, что $\forall n\in\mathbb{N},\forall y\in Y\ |a_n(y)|\le C_n$
> 2) $\sum\limits_{n=1}^{\infty}C_n<\infty$ $\Rightarrow\sum\limits_{n=1}^{\infty}a_n(y)$ равномерно сх-ся на $Y$ ⟦U277⟧

Идея φ-ва (пр. Вейерштрасса для несобств. интегр.): ⟦U278⟧

Следует из оценки: $\left|\int_{t_1}^{t_2}f(x,y)\,dx\right|\le\int_{t_1}^{t_2}|f(x,y)|\,dx\le\int_{t_1}^{t_2}\varphi(x)\,dx$

2) по крит. Б-К. ⟦S279⟧

> [!warning] Неразрешённые пометки страницы p060 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> G274: нетривиальный рисунок (non-obvious figure), см. `ocr/ISSUES.md`
> G275: нетривиальный рисунок (non-obvious figure), см. `ocr/ISSUES.md`
> S276: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U277: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U278: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S279: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p061

### Пример:

$\int_0^\infty\dfrac{\cos(\alpha x)}{1+x^2}\,dx$

$\left|\dfrac{\cos(\alpha x)}{1+x^2}\right|\le\dfrac1{1+x^2}\Rightarrow\int_0^\infty\dfrac{\cos(\alpha x)}{1+x^2}\,dx$ сх-ся равномерно

$\int_0^\infty\dfrac{dx}{1+x^2}$ — сх-ся

### Пр. Дирихле

> Интеграл: 1) $f(x,y)\to0$ равномерно на $Y$
> 2) $G(t,y):=\int_a^tg(x,y)\,dx$; $\exists C>0: |G(t,y)|\le C\ \forall t,\forall y\in Y$
> $\Rightarrow\int_a^bf(x,y)g(x,y)\,dx$ равномерно сх-ся на $Y$
> Ряд: 1) $a_n(y)\to0$ равномерно на $Y$
> 2) $b_n(y):=\sum b_k(g)$; $\exists C>0: |b_n(y)|\le C\ \forall n,\forall y\in Y$
> $\Rightarrow\sum a_n(y)b_n(y)$ равномерно сх-ся на $Y$ ⟦T280⟧

### Д-во (пр. Дирихле для несобств. интегр.):

Воспользуемся крит. Б-К равномерной сх-ти несобств. интегр.

Оценим для этого $a<n_1<n_2<b$ интеграл $\left|\int_{t_1}^{t_2}f(x,y)g(x,y)\,dx\right|$ ⟦A281⟧

$\left[\begin{array}{l}2\ \forall t\ \text{огр. или мера?}\\ g\in C([a,b]),\ \hat g\in C^1([a,b]),\ \hat g-\text{монотонна на }[a,b]\end{array}\right.$ ⟦U282⟧

Тогда $\exists c\in[a,b]$ такое, что
$\int_a^bf\cdot\hat g=\hat g(a)\int_a^bf+\hat g(b)\int_c^bf$ ⟦M283⟧

Запишем, что если $\hat g\in C([a,b])$, а $f$ интегрируема и
монотонна на $[a,b]$, по 2-я т. о среднем интегральном ⟦U284⟧

Замечание: у 2^-й т. о среднем еще много формулировок ⟦S285⟧

③ $|f(n_1,y)|\left|\int_{n_1}^{\xi}g(x,y)\,dx\right|+|f(n_2,y)|\left|\int_{\xi}^{n_2}g(x,y)\,dx\right|\le$ ⟦S286⟧

> [!warning] Неразрешённые пометки страницы p061 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> T280: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> A281: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> U282: нечитаемо (illegible), см. `ocr/ISSUES.md`
> M283: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> U284: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S285: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S286: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p062

$\left|\dfrac12\int_{n_1}^{n_2}g(x,y)\,dx\right|-1\ G(\xi,y)-G(n_1,y)|<|G(\xi,y)|+|G(n_2,y)|$ ⟦U287⟧

$\dfrac{2}{C}+C=2C$ ⟦U288⟧

по усл.

$\left|\int_\xi^{n_2}g(x,y)\,dx\right|=|G(n_2,y)-G(\xi,y)|<|G(n_2,y)|+|G(\xi,y)|<C+C=2C$

Следовательно, $\left|\int_{n_1}^{n_2}f(x,y)g(x,y)\,dx\right|<2C\cdot\left[|f(n_1,y)|+f(n_2,y)\right]$ ⟦M289⟧

[Фиксируем $\varepsilon>0$. Т.к. $f(x,y)\downarrow0$ равномерно на $Y\Rightarrow$
$\Rightarrow\exists\eta\in[a,b)$ такое, что $|f(x,y)|<\dfrac{\varepsilon}{4C}\ \forall x\in[\eta,b),\forall y\in Y$ ⟦S290⟧

Замечание: не умаляя общности, можно считать $a\le\eta<n_1<n_2<b$.

$\otimes 2C\left[\dfrac{\varepsilon}{4C}+\dfrac{\varepsilon}{4C}\right]=\varepsilon$

Итак, мы получили, что $\forall\varepsilon>0\ \exists\eta\in[a,b)$:
$\forall n_1,n_2:\eta<n_1<n_2<b$ $\left|\int_{n_1}^{n_2}f(x,y)g(x,y)\,dx\right|<\varepsilon\Rightarrow$

$\Rightarrow$ по крит. Б-К получаем равномерную сх-ть интеграла. $\square$

### Пр. Абеля

> Интеграл: 1) $f(x,y)$ монотонна по $x$ и равномерно огр.
> 2) $\int_a^bg(x,y)\,dx$ сх-ся равномерно на $Y$
> $\Rightarrow\sum a_n(y)b_n(y)$ равномерно сх-ся на $Y$ ⟦T291⟧

> [!warning] Неразрешённые пометки страницы p062 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U287: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U288: нечитаемо (illegible), см. `ocr/ISSUES.md`
> M289: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> S290: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> T291: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`

---

Source: pages p058–p062

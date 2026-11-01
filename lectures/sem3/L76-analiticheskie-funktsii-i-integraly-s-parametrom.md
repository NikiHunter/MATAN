---
semester: 3
lecture: 76
topic: "Разложимость в ряд Тейлора, аналитические функции, интегралы, зависящие от параметра"
source_pages: [p054, p055, p056, p057]
lang: ru
status: draft
---

# Лекция 76 — Разложимость в ряд Тейлора, аналитические функции, интегралы, зависящие от параметра

> [!info] Происхождение текста
> Текст переписан со страниц `p054`–`p057` рукописной тетради
> (см. [`ocr/raw/`](../../ocr/raw), [`ocr/MANIFEST.md`](../../ocr/MANIFEST.md)).
> В тетради этот материал помечен как «Лекции 75–76»: пара лекций не разделена.
> Разбиение на отдельные файлы L75 и L76 проведено по границе p057/p058 (смена темы); текст не переставлялся и не дополнялся.
> Решений в `My decision` (`ocr/ISSUES.md`) нет, поэтому все пометки остаются `open`
> и продублированы предупреждениями. Ничего не добавлено: ни доказательств,
> ни примеров, ни «пропущенных шагов».

## p054

Тогда $\sum\limits_{k=0}^{\infty}\dfrac{f^{(k)}(a)}{k!}(x-a)^k\to f(x)$.

### Д-во (т. 8.4.8):

Согласно (сильно ранее) доказанной лемме об оценке остатка
в ф-ле Тейлора имеет:

$|f(x)-T_{n,f}(x)|=|R_{n,f}(x)|\le\dfrac{M|x-a|^{n+1}}{(n+1)!}$, что даёт требуемую сх-ть. $\square$ ⟦S228⟧

### Пример ф-ции, у кот. ряд Тейлора расх-ся в любой т. кроме центра

> [!note] На полях
> [справа] $(a=0)$

$f(x)=\sum\limits_{n=0}^{\infty}e^{-\sqrt{2^n}}\cos(2^nx)$ ⟦U229⟧

Обзавелись рядом Тейлора б.ч. $x=0$ ⟦U230⟧

$f(0)=\sum\limits_{n=0}^{\infty}e^{-\sqrt{2^n}}$ ⟦U231⟧

$C_n$ — раз? в два раза меньше $n!$ ⟦U232⟧

$\Rightarrow$ расх-ся $\forall x\neq0$

### Аналитические ф-ции

### Опр (8.4.4)

Пусть $-\infty<A<B<+\infty$, $f:(A,B)\to\mathbb{R}$, $a\in(A,B)$

Ф-я $f$ наз. аналитической в т. $a$, если она раскладывается в степенной
ряд $f(x)=\sum C_k(x-a)^k$, $x\in(a-r,a+r)$. ⟦A233⟧

Ф-я $f:(A,B)\to\mathbb{R}$ наз. аналитической на промежутке $(A,B)$,
если она аналитична в каждой т. $(A,B)$. ⟦S234⟧

> [!warning] Неразрешённые пометки страницы p054 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S228: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U229: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U230: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U231: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U232: нечитаемо (illegible), см. `ocr/ISSUES.md`
> A233: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> S234: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p055

### Интегралы зависящие от параметра

### Пример:

$I(y)=\int_0^{+\infty}e^{-xy}\dfrac{\sin x}{x}\,dx$, $x\in(0,+\infty)$, $y\in[0,+\infty)$

Хотим вычислить $I'(y)$.

Занимаемся неравномерной сходимостью: ⟦U235⟧

$I'(y)=\int_0^{+\infty}\left(e^{-xy}\dfrac{\sin x}{x}\right)'_y\,dy=-\int e^{-xy}\sin x\,dx$ ⟦T236⟧

> [!note] На полях
> [красным, ❶] Переход надо дополни обосновать!! → будет сделано позднее ⟦S237⟧

❷ $\int_0^{+\infty}e^{-xy}d\cos x=\left.e^{-xy}\cos x\right|_0^{+\infty}+\int_0^{+\infty}\cos x\,de^{-xy}=-1+$

$+y\int_0^{+\infty}e^{-xy}\cos x\,dx=-1+\left.ye^{-xy}\sin x\right|_0^{+\infty}-y\int_0^{+\infty}\sin x\,d e^{-xy}=-1+y^2\int_0^{+\infty}\sin x\,e^{-xy}dx$

Обозначим $J(y):=\int_0^{+\infty}e^{-xy}\sin x\,dx$.

$I'(y)=-J(y)=-1+y^2J(y)$

$J(y)=\dfrac{1}{y^2+1}\Rightarrow I'(y)=-\dfrac{1}{1+y^2}$

Хотя вычислили $I'(y)$ ⟦S238⟧

С другой стороны, $I'(y)=-\int\dfrac{dy}{1+y^2}=-\operatorname{arctg}y+C$

$\Rightarrow I(y)=-\int_0^{+\infty}e^{-xy}\dfrac{\sin x}{x}dx+\int_0^{+\infty}0\,dx=0$ ⟦T239⟧

$-\operatorname{arctg}y+C\to-\dfrac\pi2+C=0\Rightarrow C=\dfrac\pi2$

$I(y)=\dfrac\pi2-\operatorname{arctg}y$

$I(0)=\int_0^{+\infty}\dfrac{\sin x}{x}\,dx=\dfrac\pi2-\operatorname{arctg}0=\dfrac\pi2$

> [!note] На полях
> [красным, внизу] приблизительно ❶ Выше надо обосновать ⟦S240⟧

> [!warning] Неразрешённые пометки страницы p055 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U235: нечитаемо (illegible), см. `ocr/ISSUES.md`
> T236: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> S237: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S238: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> T239: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> S240: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p056

### Собственные интегралы, зависящие от параметра

### Опр (9.1.1)

Интеграл, зависящий от параметра, это ф-я вида $I(y)=\int_{Eg}f(x,y)\,dx$,
где у некот-го параметра, пробегающего мн-во ⟦U241⟧

### Замечание

Если $\forall y\in Y$ интеграл $\int f(x,y)dy$ абс. собств., то ф-я $I(y)$ есть
собственный интеграл, зависящий от параметра. ⟦T242⟧

### Дифференцирование интеграла по параметру $y$

Будем пока считать, что $E_y$ не зависит от $y$. ⟦S243⟧

### Теорема (9.1.1)

$|P=\{(x,y)\in\mathbb{R}^2: a\le x\le b,\ c\le y\le d\}$. Далее $f=f(x,y)\in C(P)$.
Тогда ф-я $I(y)=\int_a^b f(x,y)\,dx$ интегрируема $\forall y\in[c,d]$. ⟦T244⟧

### Д-во (т. 9.1.1):

$\forall y_0\in[c,d]$ $I(y)=\lim\limits_{y\to y_0}I(y)$ — из опр.

верно, т.е. $I(y_0)=\int_a^b f(x,y_0)dx=\lim\int_a^b f(x,y)dx-\lim I(y)$ ⟦M245⟧

$f$ — интегр. на $P$ по условию? $f$ — равномерно непрерывна на $P$ ⟦A246⟧

> [!note] На полях
> [слева] $\Rightarrow$ по т. ⟦S247⟧

$\Rightarrow\forall y(x): d(x,y)\rightrightarrows\varphi_{y_0}(x)=f(x,y)$ интегр. по $x$ на $[a,b]$ ⟦U248⟧

$\Rightarrow\forall y\in[c,d]\int\varphi$-я $\varphi_y(x)=f(x,y)$ интегр. по $x$ на $[a,b]$
$\Rightarrow$ можно применить т. о предельном переходе под знаком интеграла.

> [!note] На полях
> [слева, рисунок: прямоугольник $P$ с осями, $a$, $b$, $c$, $d$] ⟦G249⟧

> [!warning] Неразрешённые пометки страницы p056 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U241: нечитаемо (illegible), см. `ocr/ISSUES.md`
> T242: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> S243: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> T244: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> M245: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> A246: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> S247: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U248: нечитаемо (illegible), см. `ocr/ISSUES.md`
> G249: нетривиальный рисунок (non-obvious figure), см. `ocr/ISSUES.md`

## p057

### Дифференцирование интеграла по параметру

### Теорема (9.1.2)

$|P=\{(x,y)\in\mathbb{R}^2: a\le x\le b,\ c\le y\le d\}$. Далее $f=f(x,y)\in C(P)$ и
$\dfrac{\partial f}{\partial y}\in C(P)$, тогда ф-я
$I(y)=\int_a^b f(x,y)\,dx\in C^1([c,d])$ и
$I'(y)=\int_a^b\dfrac{\partial f}{\partial y}(x,y)\,dx$

> [!note] На полях
> [красным, под $I'(y)$] с т. 8.2.3 (?) ⟦A250⟧

### Д-во (т. 9.1.2):

$\forall y_0\in[c,d]$:

$\dfrac{I(y_0+h)-I(y_0)}{h}=\dfrac1h\int_a^b\left(f(x,y_0+h)-f(x,y_0)\right)dx$

$\left|\dfrac{I(y_0+h)-I(y_0)}{h}-\int_a^b\dfrac{\partial f}{\partial y}(x,y_0)dx\right|=$
$\left|\int_a^b\left[\dfrac{f(x,y_0+h)-f(x,y_0)}{h}-\dfrac{\partial f}{\partial y}(x,y_0)\right]dx\right|\le$
$\le\int_a^b\sup\left|\dfrac{\partial f}{\partial y}(x,y_0+h)-\dfrac{\partial f}{\partial y}(x,y_0)\right|dx=:\varphi(y_0,h)$ ⟦M251⟧

> [!note] На полях
> [красным, справа] по т. Лагранжа $=\dfrac{\partial f}{\partial y}(x,y_0+\theta h)$, $0<\theta<1$ ⟦S252⟧

Получ. $\dfrac{\partial f}{\partial y}\in C(P)\Rightarrow\dfrac{\partial f}{\partial y}(x,y)\rightrightarrows\dfrac{\partial f}{\partial y}(x,y_0)$
$\forall x\in[a,b]$ при $y\to y_0$

$\Rightarrow\varphi(y_0,h)\xrightarrow[h\to\infty]{}0$. $\square$ ⟦T253⟧

### Пример:

Проверим, что ф-я $u(x)=\int_0^\pi\cos(n\varphi-x\sin\varphi)\,d\varphi$ удовл.
ур-ю Бесселя $x^2u''+xu'+(x^2-n^2)u=0$

$u(x)=\int_0^\pi\cos x\cos(n\varphi-x\sin\varphi)\,d\varphi=\int_0^\pi-\sin(n\varphi-x\sin\varphi)(-\sin\varphi)\,d\varphi$ ⟦T254⟧

$u''(x)=-\int_0^\pi\sin^2\varphi\cos(n\varphi-x\sin\varphi)\,d\varphi$

$x^2u''+xu'+(x^2-n^2)u=\int_0^\pi\left[-x^2\sin^2\varphi\cos(n\varphi-x\sin\varphi)+x\sin\varphi\sin(n\varphi-x\sin\varphi)\right]d\varphi$ ⟦M255⟧

> [!warning] Неразрешённые пометки страницы p057 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> A250: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> M251: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> S252: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> T253: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> T254: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> M255: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`

---

Source: pages p054–p057

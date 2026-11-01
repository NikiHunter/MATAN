---
semester: 3
lecture: "67-68"
topic: "Достаточные условия экстремума, условный экстремум и множители Лагранжа; Числовые ряды, критерий Больцано–Коши, абсолютная сходимость"
source_pages: [p012, p013, p014, p015, p016, p017, p018, p019, p020, p021]
lang: ru
status: draft
---

# Лекции 67–68 — Условия экстремума, числовые ряды и абсолютная сходимость

> [!info] Происхождение текста
> Текст переписан со страниц `p012`–`p021` рукописной тетради
> (см. [`ocr/raw/`](../../ocr/raw), [`ocr/MANIFEST.md`](../../ocr/MANIFEST.md)).
> В тетради материал помечен как «Лекции 67–68»: пара лекций не разделена.
> Страницы приведены в исходном порядке, без перестановки и без добавления текста.
> Один файл на пару: ранее созданные одиночные файлы заменены этим файлом,
> их содержимое перенесено без изменений.
> Решений в `My decision` (`ocr/ISSUES.md`) нет, поэтому все пометки остаются `open`
> и продублированы предупреждениями. Ничего не добавлено: ни доказательств,
> ни примеров, ни «пропущенных шагов».

## p012

$\Rightarrow F$ дифф-ма в нуле, причем $F'(0)=d_af(h)$
Заметим, что при $|t|<\dfrac{\delta}{\|h\|}$ верно $\|a+th-a\|<\delta\Rightarrow$
$\|a+th-a\|=\|th\|=|t|\,\|h\|<\delta$
$\Rightarrow F(t)=f(a+th)\ge f(a)=f(0)\ \forall t\in\left(-\dfrac{\delta}{\|h\|},\dfrac{\delta}{\|h\|}\right)$
Тогда $F'(0)=0$, т. е. $d_af(h)=0\ \forall h\in\mathbb{R}^n\setminus\{0\}\Rightarrow d_af=0\ \blacksquare$

> [!note] На полях
> [в рамке, справа, после конца доказательства] 17 сентября ⟦S045⟧

### Лекции 67–68

· Экстремумы
· Числовые ряды
· Сх-ся и расх-ся ряды
· Коши, Даламбер ⟦U046⟧

### Дост. усл. экстремума ф-и нескольких переменных

### Теорема (6.7.2)</u> <u>(набросок!) ⟦S047⟧

$\square$ $E\subset\mathbb{R}^n$, $a$ - внутр. т. $E$, ф-я $f: E\to\mathbb{R}$ дважды дифф-ма в т. $a$,
причем $d_af=0$. Тогда справедливы след. утв.:
1) Если $d_a^2f$ положит. опр., то $a$ - т. строгого минимума $f$
2) Если $d_a^2f$ отриц. опр., то $a$ - т. строгого максимума $f$
3) Если $d_a^2f$ принимает как положит., так и отриц. знач., то $f$ не имеет экстремума в т. $a$
$f:\mathbb{R}^2\to\mathbb{R}$ $\ f=f(x_1,x_2)$
$\nabla f=\left(\dfrac{\partial f}{\partial x_1},\dfrac{\partial f}{\partial x_2}\right)$
$D^2f=\begin{pmatrix}\dfrac{\partial^2f}{\partial x_1^2} & \dfrac{\partial^2f}{\partial x_1\partial x_2}\\[2mm] \dfrac{\partial^2f}{\partial x_2\partial x_1} & \dfrac{\partial^2f}{\partial x_2^2}\end{pmatrix}$

### Замечание

Т. 6.7.2 не охватывает ситуацию, когда $d_a^2f$ сохраняет знак,
но не явл. положительно или отриц. опр. В таблице, помимо не утвер- ⟦S048⟧

> [!warning] Неразрешённые пометки страницы p012 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S045: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U046: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S047: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S048: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p013

ждается случай вырожден $d_a^2f=0$ ⟦U049⟧

### Следствие

$\square$ $E\subset\mathbb{R}^2$, $a$ - внутр. т. $E$, $f: E\to\mathbb{R}$ ф-я дважды дифф-ма в т. $a$, $d_af=0$.
Положим: $A=\dfrac{\partial^2f}{\partial x^2}(a)$; $B=\dfrac{\partial^2f}{\partial x\partial y}(a)$; $C=\dfrac{\partial^2f}{\partial y^2}(a)$
Тогда справедливы след. утв.:
1) Если $A>0$ и $AC>B^2$, $a$ - т. строгого минимума $f$.
2) Если $A<0$ и $AC>B^2$, $a$ - т. строгого максимума $f$.
3) Если $AC<B^2$, то $f$ не имеет экстремума в т. $a$.

### D-во (сл.):

Проверим сначала утв. 1) и 2).
В силу ф-лы $d_a^2f(h)=\sum\limits_{i=1}^{2}\sum\limits_{j=1}^{2}\dfrac{\partial^2f}{\partial x_i\partial x_j}(a)h_ih_j$ $\ (n=2,\ h\in\mathbb{R}^2)$
Известно, что $d_a^2f(h)$ - квадратичная форма с матрицей Гессе.
$H=\begin{pmatrix}A & B\\ B & C\end{pmatrix}$
Вычислим главные миноры $H$: $\Delta_1=A$, $\Delta_2=\det H=AC-B^2$
По критерию Сильвестра и его следствию, имеем:
$\Delta_1>0$, $\Delta_2>0\Rightarrow$ положительная определенность $d_a^2f(h)\Rightarrow$ 1)
$\Delta_1<0$, $\Delta_2>0\Rightarrow$ отрицательная определенность $d_a^2f(h)\Rightarrow$ 2)
Докажем теперь 3).
$d_a^2f(h)=\sum\limits_{i=1}^{2}\dfrac{\partial^2f}{\partial x_i^2}(a)h_i^2+2\sum\limits_{1\le i<j\le 2}\dfrac{\partial^2f}{\partial x_i\partial x_j}(a)h_ih_j$ $\ (n=2,\ h\in\mathbb{R}^2)$
получим $d_a^2f(h)=A\,dx^2+2B\,dxdy+C\,dy^2$ ⟦S050⟧
При фикс. $dy\neq 0$ имеем: $4dy^2(B^2-AC)>0$ ⟦M051⟧
Поэтому $d_a^2f(h)$ принимает как положительные, так и отрица-
тельные значения $\Rightarrow$ у $f$ нет экстремума в т. $a$. $\blacksquare$

> [!warning] Неразрешённые пометки страницы p013 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U049: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S050: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> M051: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`

## p014

### Замечание

Приведенная в сл. классификация не охватывает случай $AC-B^2=0$. Это
есть случай, когда $d_a^2f(h)$ явл. полным квадратом, т. е. имеет вид
$d_a^2f(dx,dy)=\pm(\alpha\,dx+\beta\,dy)^2$, $\alpha,\beta\in\mathbb{R}$
В частности, при нулевой диагонали мы не можем сделать выводов
о наличии у $f$ экстремума в т. $a$. ⟦A052⟧

### Пример:

$f(x,y)=x^4+3xy^2+y^4$, $a=(0,0)$
$\nabla f(x,y)=\left(\dfrac{\partial f}{\partial x},\dfrac{\partial f}{\partial y}\right)=(4x^3+3y^2,\,4y^3+6xy)$ ⟦A053⟧
$\nabla f(0,0)=(0,0)\Rightarrow d_af=0\Rightarrow(0,0)$ - стационарная т.

$[d_a^2f]$ $H_f=\begin{pmatrix}\dfrac{\partial^2f}{\partial x^2} & \dfrac{\partial^2f}{\partial x\partial y}\\[2mm] \dfrac{\partial^2f}{\partial y\partial x} & \dfrac{\partial^2f}{\partial y^2}\end{pmatrix}=\begin{pmatrix}12x^2 & 6y\\ 6y & 12y^2+6x\end{pmatrix}$ ⟦A054⟧

$H_f(0,0)=\begin{pmatrix}0 & 0\\ 0 & 0\end{pmatrix}\Rightarrow$ вырожденная $\Rightarrow$ ‹рисунок: кружок со смайликом› ⟦G055⟧

$[d_a^3f]$ $\dfrac{\partial^3f}{\partial x^3}=24x\Rightarrow\dfrac{\partial^3f}{\partial x^3}(0,0)=0$
$\dfrac{\partial^3f}{\partial x^2\partial y}=0$ $\ \dfrac{\partial^3f}{\partial x\partial y^2}=6$
$\dfrac{\partial^3f}{\partial y^3}=24y\Rightarrow\dfrac{\partial^3f}{\partial y^3}(0,0)=0$
$d_a^3f(dx,dy)=C_3^1\dfrac{\partial^3f}{\partial x^2\partial y}(0,0)dx\,dy^2=18\,dx\,dy^2$ ⟦A056⟧

> [!note] На полях
> [мелко, над строкой] $18\cdot h_1h_2^2$

Рассм. $h\in\mathbb{R}^2\setminus\{(0,0)\}$, для кот. $d_a^3f(h)\neq 0$.
Положим $\varphi(t)=f(th)$, $t\in\mathbb{R}\Rightarrow\varphi'(0)=\varphi''(0)=0$, $\varphi'''(0)=d_a^3f(h)\neq 0$
$\Rightarrow\varphi$ не имеет экстремума в $0\Rightarrow f$ не имеет экстре-
мума в т. $(0,0)$

> [!warning] Неразрешённые пометки страницы p014 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> A052: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> A053: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> A054: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> G055: нетривиальный рисунок (non-obvious figure), см. `ocr/ISSUES.md`
> A056: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`

## p015

### Задача об условном экстремуме

$f: E\subset\mathbb{R}^n\to\mathbb{R}$, $a\in E$ - т. экстремума $f$. Тогда $\forall x\in V(a)$ $f(x)\ge f(a)$ или
$f(x)\le f(a)$ ⟦S057⟧
Предположим теперь, что нас интересует не все т. $x\in V(a)$, а только те,
кот. удовл. некоторым доп. рав-вам, наз. уравнениями связи.
Тогда говорят об условном или относительном экстремуме, подчиненном
этим ур-ям связи.
$f:\mathbb{R}^n\to\mathbb{R}$, $a$ - т. экстр., $k$ доп. усл. $\left\{\begin{array}{l}\varphi_1(x_1,\ldots,x_n)=\varphi_1(a)\\ \ldots\\ \varphi_m(\ldots)=\varphi_m(a)\end{array}\right.$ ⟦M058⟧

### Условный (относительный) экстремум

### Опр. (6.7.2)

$\square$ $E\subset\mathbb{R}^n$, $a\in E$, $m\in\mathbb{N}$, $m<n$, $f,\varphi_1,\ldots,\varphi_m: E\to\mathbb{R}$.
Предположим, что $a$ явл. т. экстремума сужения ф-и $f$ на мн-во
$\{x\in E:\ \varphi_k(x)=\varphi_k(a)\ \forall k=1..m\}$
Тогда $a$ наз. т. условного (относительного) экстремума $f$ соотв. типа,
подчиненного уравнениям связи $\varphi_k(x)=\varphi_k(a)$, где $k\in\{1,\ldots,m\}$, $x\in E$

### Замечание

Без ограничения общности будем считать, что $\varphi_k(a)=0\ \forall k\in\{1,\ldots,m\}$

### Необходимое усл. относительного экстремума

$\Phi=(\varphi_1,\ldots,\varphi_m)$, т.е. $\Phi: E\subset\mathbb{R}^n\to\mathbb{R}^m$

### Теорема (6.7.3)

$m,n\in\mathbb{N}$, $m<n$, мн-во $E$ открыто в $\mathbb{R}^n$, $a\in E$, $f\in C^1(E)$, $\Phi\in C^1(E,\mathbb{R}^m)$, $\operatorname{rank}\Phi'(a)=m$
Предположим также, что $a$ явл. т. усл. экстремума $f$, подчиненного ур-ям
связи $\Phi=0$. Тогда $\exists\lambda_1,\ldots,\lambda_m\in\mathbb{R}$, для кот. $\operatorname{grad}f(a)=\sum\limits_{k=1}^{m}\lambda_k\operatorname{grad}\varphi_k(a)$ (6.7.1)

> [!warning] Неразрешённые пометки страницы p015 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S057: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> M058: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`

## p016

### Замечание

Числа $\lambda_1,\ldots,\lambda_m$ удовл. (6.7.1) наз. множителями Лагранжа.

### D-во (т. 6.7.3):

Будем записывать эл-ты $\mathbb{R}^n$ в виде $(x,y)$, где $x\in\mathbb{R}^{n-m}$, $y\in\mathbb{R}^m$, и
пусть $a=(x^0,y^0)$
Обозн. $M=\{(x,y)\in E:\ \varphi_k(x,y)=0\ \forall k\in\{1,\ldots,m\}\}$ — поверхность, т.е. ‹?› ⟦U059⟧

Т. о. неявная ф-я: $\exists V(a)\subset\mathbb{R}^n$ $\exists U(x^0)\subset\mathbb{R}^{n-m}$, $\exists\varphi\in C^1(U,\mathbb{R}^m)$
такие, что $M\cap V(a)=\{(x,\psi(x)),\ x\in U(x^0)\}$ ⟦M060⟧

1) $f|_M$ имеет экстремум в т. $a\Rightarrow F(x)=f(x,\psi(x))$, $x\in U(x^0)$ имеет
экстремум в т. $x^0\Rightarrow\nabla F(x^0)=0\Rightarrow f'_x(a)+f'_y(a)\psi'(x^0)=0$
> [!note] На полях
> [красным, под формулой] докажем поз. ‹?› ⟦U061⟧

Кроме того, из т. о неявной ф-и также следует, что
$\Phi(x,\psi(x))=0\ \forall x\in U(x^0)$
$\Rightarrow\Phi'_x(a)+\Phi'_y(a)\psi'(x^0)=0$
> [!note] На полях
> [слева, мелко] замечание 2-е т. 6.6.1

$\Phi=\begin{pmatrix}\varphi_1\\ \vdots\\ \varphi_m\end{pmatrix}$ $\varphi_i: E\to\mathbb{R}$, $x\in\mathbb{R}^{n-m}$, $\Phi'_x=\begin{pmatrix}\dfrac{\partial\varphi_1}{\partial x_1} & \dfrac{\partial\varphi_1}{\partial x_2} & \cdots & \dfrac{\partial\varphi_1}{\partial x_{n-m}}\\[2mm] \dfrac{\partial\varphi_m}{\partial x_1} & \dfrac{\partial\varphi_m}{\partial x_2} & \cdots & \dfrac{\partial\varphi_m}{\partial x_{n-m}}\end{pmatrix}$ ⟦S062⟧

$\left\{\begin{array}{l}f'_x(a)+f'_y(a)\psi'(x^0)=0\\ \Phi'_x(a)+\Phi'_y(a)\psi'(x^0)=0\end{array}\right.$

$\lambda=(\lambda_1,\ldots,\lambda_m)$

$[f'_x(a)-\lambda\Phi'_x(a)]+[f'_y(a)-\lambda\Phi'_y(a)]\cdot\psi'(x^0)=0$ $(*)$
Положим $\lambda=f'_y(a)[\Phi'_y(a)]^{-1}\Rightarrow$ 2-е слагаемое в $(*)=0\Rightarrow$
1-е слагаемое в $(*)=0$. ⟦A063⟧
Т. о. $\forall i\in\{1,\ldots,n-m\}$ $\forall j\in\{1,\ldots,m\}$ имеем:
$\dfrac{\partial f}{\partial x_i}(a)=\sum\limits_{k=1}^{m}\lambda_k\dfrac{\partial\varphi_k}{\partial x_i}(a)$; $\dfrac{\partial f}{\partial y_j}(a)=\sum\limits_{k=1}^{m}\lambda_k\dfrac{\partial\varphi_k}{\partial y_j}(a)$

> [!warning] Неразрешённые пометки страницы p016 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U059: нечитаемо (illegible), см. `ocr/ISSUES.md`
> M060: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> U061: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S062: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> A063: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`

## p017

$\dfrac{\partial f}{\partial y_j}=\sum\limits_{k=1}^{m}\lambda_k\dfrac{\partial\varphi_k}{\partial y_j}(a)$
$\dfrac{\partial f}{\partial y_m}=\sum\limits_{k=1}^{m}\lambda_k\dfrac{\partial\varphi_k}{\partial y_m}(a)$
$\Rightarrow\nabla f(a)=\left(\dfrac{\partial f}{\partial x_i}(a),\dfrac{\partial f}{\partial y_j}(a)\right)=\left(\sum\limits_{k=1}^{m}\lambda_k\dfrac{\partial\varphi_k}{\partial x_i}(a),\sum\limits_{k=1}^{m}\lambda_k\dfrac{\partial\varphi_k}{\partial y_j}(a)\right)=$
$=\sum\limits_{k=1}^{m}\lambda_k\left(\dfrac{\partial\varphi_k}{\partial x_i}(a),\dfrac{\partial\varphi_k}{\partial y_j}(a)\right)=\sum\limits_{k=1}^{m}\lambda_k\nabla\varphi_k(a)$. $\blacksquare$ ⟦S064⟧

### Необходимое усл. относительного экстремума

### Теорема (6.7.4)

$m,n\in\mathbb{N}$, $m<n$, мн-во $E$ открыто в $\mathbb{R}^n$, $a\in E$, $f\in C^1(E)$, $\Phi\in C^1(E,\mathbb{R}^m)$, $\operatorname{rank}\Phi'(a)=m$.
Предположим также, что $a$ явл. т. усл. экстремума $f$, подчиненного
ур-ям связи $\Phi=0$. Обозн. $L(x,\lambda)=f(x)-\sum\limits_{k=1}^{m}\lambda_k\varphi_k(x)$ $(x\in E,\ \lambda\in\mathbb{R}^m)$
Тогда $\exists\lambda\in\mathbb{R}^m$, для кот. $\operatorname{grad}L(a,\lambda)=0$. ⟦T065⟧

### Достаточные усл. относительного экстремума

### Опр (6.7.3)

$N$ - лин. подпр-во в $\mathbb{R}^n$. Квадратичная форма в $\mathbb{R}^n$ наз. положи-
тельно определенной на $N$, если $f(x)>0\ \forall x\in N\setminus\{0\}$, и отрицательно опре-
деленной на $N$, если $f(x)<0\ \forall x\in N\setminus\{0\}$. ⟦S066⟧

### Замечание

Если $f$ положительно определена в $\mathbb{R}^n$, то она положительно определена
на любом лин. подпр-ве $\mathbb{R}^n$. Обратное неверно.

> [!warning] Неразрешённые пометки страницы p017 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S064: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> T065: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> S066: неясная структура (unclear structure), см. `ocr/ISSUES.md`

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

Source: pages p012–p021

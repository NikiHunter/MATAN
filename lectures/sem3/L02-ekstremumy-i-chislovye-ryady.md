---
semester: 3
lecture: 67-68
topic: "Достаточные условия экстремума, условный экстремум, числовые ряды"
source_pages: [p012, p013, p014, p015, p016, p017, p018, p019, p020, p021]
lang: ru
status: draft
---

# Лекции 67–68 — достаточные условия экстремума, условный экстремум, числовые ряды

> [!info] Происхождение текста
> Конспект переписан с рукописных страниц `p012`–`p021` (см. [`ocr/raw/`](../../ocr/raw) и [`ocr/MANIFEST.md`](../../ocr/MANIFEST.md)). Заголовок «Лекции 67–68» стоит в середине `p012`, поэтому эта страница отнесена к обеим лекциям. Формулы приведены так, как они записаны; спорные места помечены `⟦ID⟧`.

## План лекций 67–68

- Экстремумы
- Числовые ряды
- Сх-ся и расх-ся ряды
- Коши, Даламбер ⟦U046⟧

> [!warning] U046 — см. ocr/ISSUES.md
> U046: фамилия записана без апострофа; признак Даламбера в записи далее не встречается.

## 1. Теорема 6.7.2 (достаточное условие экстремума)

> [!warning] S047 — см. ocr/ISSUES.md
> S047: в тетради теорема помечена красным «(набросок!)»; полного доказательства нет (⟦S047⟧, см. ocr/ISSUES.md).

### Теорема 6.7.2

Пусть $E\subset\mathbb{R}^n$, $a$ — внутренняя точка $E$, функция $f: E\to\mathbb{R}$ дважды дифференцируема в точке $a$, причём $d_af=0$. Тогда справедливы следующие утверждения:

1) если $d_a^2f$ положительно определена, то $a$ — точка строгого минимума $f$;
2) если $d_a^2f$ отрицательно определена, то $a$ — точка строгого максимума $f$;
3) если $d_a^2f$ принимает как положительные, так и отрицательные значения, то $f$ не имеет экстремума в точке $a$.

Для $f:\mathbb{R}^2\to\mathbb{R}$, $f=f(x_1,x_2)$:

$$\nabla f=\left(\frac{\partial f}{\partial x_1},\frac{\partial f}{\partial x_2}\right),\qquad D^2f=\begin{pmatrix}\dfrac{\partial^2f}{\partial x_1^2} & \dfrac{\partial^2f}{\partial x_1\partial x_2}\\[2mm] \dfrac{\partial^2f}{\partial x_2\partial x_1} & \dfrac{\partial^2f}{\partial x_2^2}\end{pmatrix}.$$

### Замечание

Теорема 6.7.2 не охватывает ситуацию, когда $d_a^2f$ сохраняет знак, но не является положительно или отрицательно определённой. В таблице, помимо не утвер- … ⟦S048⟧ ⟦U049⟧

> [!warning] S048, U049 — см. ocr/ISSUES.md
> S048: фраза обрывается на переносе страницы.
> U049: продолжение на p013 («…случай вырожден $d_a^2f=0$») не складывается в целое предложение.

## 2. Следствие для $n=2$ (критерий через $A$, $B$, $C$)

Пусть $E\subset\mathbb{R}^2$, $a$ — внутренняя точка $E$, $f: E\to\mathbb{R}$ — функция, дважды дифференцируемая в точке $a$, $d_af=0$. Положим

$$A=\frac{\partial^2f}{\partial x^2}(a),\qquad B=\frac{\partial^2f}{\partial x\partial y}(a),\qquad C=\frac{\partial^2f}{\partial y^2}(a).$$

Тогда справедливы следующие утверждения:

1) если $A>0$ и $AC>B^2$, то $a$ — точка строгого минимума $f$;
2) если $A<0$ и $AC>B^2$, то $a$ — точка строгого максимума $f$;
3) если $AC<B^2$, то $f$ не имеет экстремума в точке $a$.

**Доказательство.** Проверим сначала утверждения 1) и 2). В силу формулы

$$d_a^2f(h)=\sum_{i=1}^{2}\sum_{j=1}^{2}\frac{\partial^2f}{\partial x_i\partial x_j}(a)h_ih_j\quad (n=2,\ h\in\mathbb{R}^2).$$

Известно, что $d_a^2f(h)$ — квадратичная форма с матрицей Гессе

$$H=\begin{pmatrix}A & B\\ B & C\end{pmatrix}.$$

Вычислим главные миноры $H$: $\Delta_1=A$, $\Delta_2=\det H=AC-B^2$. По критерию Сильвестра и его следствию имеем:

$$\Delta_1>0,\ \Delta_2>0\ \Rightarrow\ \text{положительная определённость } d_a^2f(h)\ \Rightarrow\ 1),$$

$$\Delta_1<0,\ \Delta_2>0\ \Rightarrow\ \text{отрицательная определённость } d_a^2f(h)\ \Rightarrow\ 2).$$

Докажем теперь 3).

$$d_a^2f(h)=\sum_{i=1}^{2}\frac{\partial^2f}{\partial x_i^2}(a)h_i^2+2\sum_{1\le i<j\le 2}\frac{\partial^2f}{\partial x_i\partial x_j}(a)h_ih_j\quad (n=2,\ h\in\mathbb{R}^2),$$

получим

$$d_a^2f(h)=A\,dx^2+2B\,dxdy+C\,dy^2.$$

⟦S050⟧

При фиксированном $dy\neq 0$ имеем: $4dy^2(B^2-AC)>0$. Поэтому $d_a^2f(h)$ принимает как положительные, так и отрицательные значения $\Rightarrow$ у $f$ нет экстремума в точке $a$. $\blacksquare$ ⟦M051⟧

> [!warning] S050, M051 — см. ocr/ISSUES.md
> S050: переход от $h_i$ к $dx,dy$ не оговорён.
> M051: как получено неравенство $4dy^2(B^2-AC)>0$, в записи не видно.

## 3. Вырожденный случай и пример

### Замечание

Приведённая в следствии классификация не охватывает случай $AC-B^2=0$. Это есть случай, когда $d_a^2f(h)$ является полным квадратом, то есть имеет вид

$$d_a^2f(dx,dy)=\pm(\alpha\,dx+\beta\,dy)^2,\quad \alpha,\beta\in\mathbb{R}.$$

В частности, при нулевой диагонали мы не можем сделать выводов о наличии у $f$ экстремума в точке $a$. ⟦A052⟧

### Пример

$$f(x,y)=x^4+3xy^2+y^4,\qquad a=(0,0),$$

$$\nabla f(x,y)=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}\right)=(4x^3+3y^2,\,4y^3+6xy),$$

⟦A053⟧

$$\nabla f(0,0)=(0,0)\ \Rightarrow\ d_af=0\ \Rightarrow\ (0,0)\ \text{— стационарная точка}.$$

Далее выписана матрица Гессе:

$$H_f=\begin{pmatrix}\dfrac{\partial^2f}{\partial x^2} & \dfrac{\partial^2f}{\partial x\partial y}\\[2mm] \dfrac{\partial^2f}{\partial y\partial x} & \dfrac{\partial^2f}{\partial y^2}\end{pmatrix}=\begin{pmatrix}12x^2 & 6y\\ 6y & 12y^2+6x\end{pmatrix},$$

⟦A054⟧

$$H_f(0,0)=\begin{pmatrix}0 & 0\\ 0 & 0\end{pmatrix}\ \Rightarrow\ \text{вырожденная}\ \Rightarrow\ \text{‹рисунок: кружок со смайликом›}$$

⟦G055⟧

и дифференциал третьего порядка:

$$\frac{\partial^3f}{\partial x^3}=24x\Rightarrow\frac{\partial^3f}{\partial x^3}(0,0)=0,\qquad \frac{\partial^3f}{\partial x^2\partial y}=0,\qquad \frac{\partial^3f}{\partial x\partial y^2}=6,$$

$$\frac{\partial^3f}{\partial y^3}=24y\Rightarrow\frac{\partial^3f}{\partial y^3}(0,0)=0,$$

$$d_a^3f(dx,dy)=C_3^1\frac{\partial^3f}{\partial x^2\partial y}(0,0)dx\,dy^2=18\,dx\,dy^2.$$

⟦A056⟧

Рассмотрим $h\in\mathbb{R}^2\setminus\{(0,0)\}$, для которого $d_a^3f(h)\neq 0$. Положим $\varphi(t)=f(th)$, $t\in\mathbb{R}$. Тогда

$$\varphi'(0)=\varphi''(0)=0,\quad \varphi'''(0)=d_a^3f(h)\neq 0\ \Rightarrow\ \varphi\ \text{не имеет экстремума в } 0\ \Rightarrow\ f\ \text{не имеет экстремума в точке } (0,0).$$

> [!warning] A052, A053, A054, G055, A056 — см. ocr/ISSUES.md
> A052: слово прочитывается как «диагонали»; возможно, имелась в виду диагональ матрицы Гессе.
> A053: вторая компонента градиента записана с трудом (возможны другие коэффициенты).
> A054: в левой верхней ячейке виден дополнительный штрих после $12x^2$.
> G055: после вывода о вырожденности нарисован кружок с неразборчивым знаком внутри.
> A056: коэффициент записан как $C_3^1$, но применён к $dx\,dy^2$; индекс при $\partial^3f$ указан как $x^2\partial y$.

## 4. Условный (относительный) экстремум

Пусть $f: E\subset\mathbb{R}^n\to\mathbb{R}$, $a\in E$ — точка экстремума $f$. Тогда $\forall x\in V(a)$ выполнено $f(x)\ge f(a)$ или $f(x)\le f(a)$. ⟦S057⟧
Предположим теперь, что нас интересует не все точки $x\in V(a)$, а только те, которые удовлетворяют некоторым дополнительным равенствам, называемым уравнениями связи. Тогда говорят об условном или относительном экстремуме, подчинённом этим уравнениям связи.
Для $f:\mathbb{R}^n\to\mathbb{R}$, $a$ — точка экстремума, $k$ дополнительных условий: ⟦M058⟧

$$\left\{\begin{array}{l}\varphi_1(x_1,\ldots,x_n)=\varphi_1(a)\\ \ldots\\ \varphi_m(\ldots)=\varphi_m(a)\end{array}\right.$$

### Определение 6.7.2

Пусть $E\subset\mathbb{R}^n$, $a\in E$, $m\in\mathbb{N}$, $m<n$, $f,\varphi_1,\ldots,\varphi_m: E\to\mathbb{R}$. Предположим, что $a$ является точкой экстремума сужения функции $f$ на множество

$$\{x\in E:\ \varphi_k(x)=\varphi_k(a)\ \forall k=1..m\}.$$

Тогда $a$ называется точкой условного (относительного) экстремума $f$ соответствующего типа, подчинённого уравнениям связи $\varphi_k(x)=\varphi_k(a)$, где $k\in\{1,\ldots,m\}$, $x\in E$.

### Замечание

Без ограничения общности будем считать, что $\varphi_k(a)=0$ $\forall k\in\{1,\ldots,m\}$.

> [!warning] S057, M058 — см. ocr/ISSUES.md
> S057: не сказано, какая окрестность имеется в виду и почему выполняется одно из двух неравенств.
> M058: число условий обозначено то как $k$, то как $m$; далее всюду используется $m$.

## 5. Теорема 6.7.3 (необходимое условие относительного экстремума)

Обозначим $\Phi=(\varphi_1,\ldots,\varphi_m)$, то есть $\Phi: E\subset\mathbb{R}^n\to\mathbb{R}^m$.

### Теорема 6.7.3

Пусть $m,n\in\mathbb{N}$, $m<n$, множество $E$ открыто в $\mathbb{R}^n$, $a\in E$, $f\in C^1(E)$, $\Phi\in C^1(E,\mathbb{R}^m)$, $\operatorname{rank}\Phi'(a)=m$. Предположим также, что $a$ является точкой условного экстремума $f$, подчинённого уравнениям связи $\Phi=0$. Тогда существуют $\lambda_1,\ldots,\lambda_m\in\mathbb{R}$, для которых

$$\operatorname{grad}f(a)=\sum_{k=1}^{m}\lambda_k\operatorname{grad}\varphi_k(a). \tag{6.7.1}$$

### Замечание

Числа $\lambda_1,\ldots,\lambda_m$, удовлетворяющие (6.7.1), называются множителями Лагранжа.

**Доказательство.** Будем записывать элементы $\mathbb{R}^n$ в виде $(x,y)$, где $x\in\mathbb{R}^{n-m}$, $y\in\mathbb{R}^m$, и пусть $a=(x^0,y^0)$.
Обозначим

$$M=\{(x,y)\in E:\ \varphi_k(x,y)=0\ \forall k\in\{1,\ldots,m\}\}$$

— поверхность, то есть ‹?› ⟦U059⟧.
Далее используется теорема о неявной функции: существуют $V(a)\subset\mathbb{R}^n$, $U(x^0)\subset\mathbb{R}^{n-m}$, $\varphi\in C^1(U,\mathbb{R}^m)$ такие, что

$$M\cap V(a)=\{(x,\psi(x)),\ x\in U(x^0)\}.$$

⟦M060⟧

1) Так как $f|_M$ имеет экстремум в точке $a$, то $F(x)=f(x,\psi(x))$, $x\in U(x^0)$, имеет экстремум в точке $x^0$, поэтому

$$\nabla F(x^0)=0\ \Rightarrow\ f'_x(a)+f'_y(a)\psi'(x^0)=0.$$

⟦U061⟧

Кроме того, из теоремы о неявной функции также следует, что $\Phi(x,\psi(x))=0$ $\forall x\in U(x^0)$, откуда

$$\Rightarrow\ \Phi'_x(a)+\Phi'_y(a)\psi'(x^0)=0.$$

Здесь

$$\Phi=\begin{pmatrix}\varphi_1\\ \vdots\\ \varphi_m\end{pmatrix},\quad \varphi_i: E\to\mathbb{R},\quad x\in\mathbb{R}^{n-m},\quad \Phi'_x=\begin{pmatrix}\dfrac{\partial\varphi_1}{\partial x_1} & \dfrac{\partial\varphi_1}{\partial x_2} & \cdots & \dfrac{\partial\varphi_1}{\partial x_{n-m}}\\[2mm] \dfrac{\partial\varphi_m}{\partial x_1} & \dfrac{\partial\varphi_m}{\partial x_2} & \cdots & \dfrac{\partial\varphi_m}{\partial x_{n-m}}\end{pmatrix}.$$

⟦S062⟧

Итак, имеем систему

$$\left\{\begin{array}{l}f'_x(a)+f'_y(a)\psi'(x^0)=0\\ \Phi'_x(a)+\Phi'_y(a)\psi'(x^0)=0\end{array}\right.$$

и обозначение $\lambda=(\lambda_1,\ldots,\lambda_m)$. Тогда

$$[f'_x(a)-\lambda\Phi'_x(a)]+[f'_y(a)-\lambda\Phi'_y(a)]\cdot\psi'(x^0)=0. \tag{$*$}$$

Положим $\lambda=f'_y(a)[\Phi'_y(a)]^{-1}$. Тогда второе слагаемое в $(*)$ равно $0$, следовательно первое слагаемое в $(*)$ равно $0$. ⟦A063⟧
Таким образом, $\forall i\in\{1,\ldots,n-m\}$ $\forall j\in\{1,\ldots,m\}$ имеем:

$$\frac{\partial f}{\partial x_i}(a)=\sum_{k=1}^{m}\lambda_k\frac{\partial\varphi_k}{\partial x_i}(a),\qquad \frac{\partial f}{\partial y_j}(a)=\sum_{k=1}^{m}\lambda_k\frac{\partial\varphi_k}{\partial y_j}(a),$$

$$\frac{\partial f}{\partial y_m}=\sum_{k=1}^{m}\lambda_k\frac{\partial\varphi_k}{\partial y_m}(a),$$

$$\Rightarrow\ \nabla f(a)=\left(\frac{\partial f}{\partial x_i}(a),\frac{\partial f}{\partial y_j}(a)\right)=\left(\sum_{k=1}^{m}\lambda_k\frac{\partial\varphi_k}{\partial x_i}(a),\sum_{k=1}^{m}\lambda_k\frac{\partial\varphi_k}{\partial y_j}(a)\right)=$$

$$=\sum_{k=1}^{m}\lambda_k\left(\frac{\partial\varphi_k}{\partial x_i}(a),\frac{\partial\varphi_k}{\partial y_j}(a)\right)=\sum_{k=1}^{m}\lambda_k\nabla\varphi_k(a).\ \blacksquare$$

⟦S064⟧

> [!warning] U059, M060, U061, S062, A063, S064 — см. ocr/ISSUES.md
> U059: после «т.е.» стоит нечитаемое слово из 2–3 букв.
> M060: неявное отображение обозначено здесь $\psi$, в теореме 6.6.1 — $\varphi$.
> U061: красная пометка под формулой не читается (вероятно «докажем позже»).
> S062: матрица $\Phi'_x$ выписана только крайними строками.
> A063: второе следствие в цепочке прочитывается неуверенно.
> S064: индексы $i$ и $j$ не связаны с разбиением координат.

## 6. Теорема 6.7.4 (через функцию Лагранжа)

> [!warning] T065 — см. ocr/ISSUES.md
> T065: заголовок «Необходимое условие относительного экстремума» повторён второй раз, а содержание теоремы 6.7.4 — переформулировка 6.7.3 через $L$. ⟦T065⟧

### Теорема 6.7.4

Пусть $m,n\in\mathbb{N}$, $m<n$, множество $E$ открыто в $\mathbb{R}^n$, $a\in E$, $f\in C^1(E)$, $\Phi\in C^1(E,\mathbb{R}^m)$, $\operatorname{rank}\Phi'(a)=m$. Предположим также, что $a$ является точкой условного экстремума $f$, подчинённого уравнениям связи $\Phi=0$. Обозначим

$$L(x,\lambda)=f(x)-\sum_{k=1}^{m}\lambda_k\varphi_k(x)\quad (x\in E,\ \lambda\in\mathbb{R}^m).$$

Тогда существует $\lambda\in\mathbb{R}^m$, для которого $\operatorname{grad}L(a,\lambda)=0$.

## 7. Определение 6.7.3 (определённость на подпространстве)

Пусть $N$ — линейное подпространство в $\mathbb{R}^n$. Квадратичная форма в $\mathbb{R}^n$ называется положительно определённой на $N$, если $f(x)>0$ $\forall x\in N\setminus\{0\}$, и отрицательно определённой на $N$, если $f(x)<0$ $\forall x\in N\setminus\{0\}$. ⟦S066⟧

### Замечание

Если $f$ положительно определена в $\mathbb{R}^n$, то она положительно определена на любом линейном подпространстве $\mathbb{R}^n$. Обратное неверно.

> [!warning] S066 — см. ocr/ISSUES.md
> S066: внутри определения квадратичная форма обозначена $f$, хотя $f$ на всей странице — целевая функция.

## 8. Теорема 6.7.5 (достаточное условие условного экстремума)

### Теорема 6.7.5

Пусть $m,n\in\mathbb{N}$, $m<n$, множество $E$ открыто в $\mathbb{R}^n$, $a\in E$, $f\in C^2(E)$, $\Phi\in C^2(E,\mathbb{R}^m)$, $\Phi(a)=0$, $\operatorname{rank}\Phi'(a)=m$. Положим

$$N=\{h\in\mathbb{R}^n:\ d_a\Phi(h)=0\},\qquad L(x)=f(x)-\sum_{k=1}^{m}\lambda_k\varphi_k(x)\quad (x\in E),$$

где $\lambda_1,\ldots,\lambda_m$ удовлетворяют условию (6.7.1) в точке $a$. Тогда справедливы следующие утверждения:

1) если $d_a^2L$ положительно/отрицательно определена на $N$, то $f$ имеет в точке $a$ условный минимум/максимум, подчинённый уравнениям связи $\Phi=0$ ; ⟦S067⟧
2) если $d_a^2L$ принимает на $N$ как положительные, так и отрицательные значения, то $f$ не имеет в точке $a$ условного экстремума, подчинённого уравнениям связи $\Phi=0$.

> [!warning] S067 — см. ocr/ISSUES.md
> S067: два утверждения записаны через косую черту в одной строке.

## 9. Числовые ряды

### Определение 7.1.1

Дана последовательность $(a_n)$, $n\in\mathbb{N}$.

$$S_n=a_1+a_2+\ldots+a_n\ \text{— частичная сумма ряда},\qquad \lim_{n\to\infty}S_n=S\ \text{— сумма ряда},$$

$$S:=\sum_{n=1}^{\infty}a_n\ \text{— обозначение},\qquad a_n\ \text{— общий член ряда}.$$

⟦S068⟧

### Определение 7.1.2

Ряд $\sum\limits_{n=1}^{\infty}a_n$ сходится, если сумма ряда $S$ существует и конечна. В противном случае ряд расходится.

$$S_n=\sum_{k=1}^{n}a_k,\qquad S=\lim_{n\to\infty}S_n.$$

1) $S$ существует, $S<\infty$ $\Rightarrow$ ряд сходится;
2) $S$ существует, $S=\infty$ $\Rightarrow$ ряд расходится;
3) $S$ не существует $\Rightarrow$ ряд расходится.

**Примеры.**

$$\text{Ряд } \sum_{n=1}^{\infty}0=0\ \Rightarrow\ \text{так как все частичные суммы } S_n=0;$$

$$2)\ \sum_{k=1}^{\infty}1\ \text{— расходящийся, то есть } S_n=\sum_{k=1}^{n}1=n,\quad \lim_{n\to\infty}S_n=\lim_{n\to\infty}n=+\infty;$$

$$3)\ \sum_{k=0}^{\infty}(-1)^k=1-1+1-1+1-1+\ldots\ \text{— расходится},\quad S_n=\left\{\begin{array}{l}1,\ n-\text{чёт}\\ 0,\ n-\text{нечёт}\end{array}\right.$$

Последовательность $\{S_n\}$ не имеет ни конечного, ни бесконечного предела $\Rightarrow$ ряд расходится; ⟦S069⟧

$$4)\ \sum_{k=1}^{\infty}\frac{1}{k(k+1)}\ \text{— сходится и } S=1,$$

$$S_n=\sum_{k=1}^{n}\frac{1}{k(k+1)}=\sum_{k=1}^{n}\left(\frac{1}{k}-\frac{1}{k+1}\right)=1-\frac{1}{n+1}\to1\ \text{при } n\to\infty.$$

> [!warning] S068, S069 — см. ocr/ISSUES.md
> S068: три определения ($S_n$, $S$, $a_n$) записаны справа от основного текста без явных связей.
> S069: слово «расх.» дописано в конце строки под наклоном.

## 10. Свойства рядов 1) и 2)

**Свойство 1.** Если $\sum\limits_{n=1}^{\infty}a_n$ сходится, тогда $a_n\to0$ при $n\to\infty$.

### Замечание

1) Если $a_n\nrightarrow0$ при $n\to\infty$, то $\sum\limits_{n=1}^{\infty}a_n$ расходится ; ⟦S070⟧
2) если $a_n\to0$ при $n\to\infty$, то не обязательно $\sum\limits_{n=1}^{\infty}a_n$ сходится.

**Свойство 2.**

$$\sum_{n=1}^{\infty}a_n\ \text{сходится}\ \Leftrightarrow\ \forall k\ \sum_{n=k+1}^{\infty}a_n\ \text{сходится}$$

(остаток ряда, после $k$-го члена).

**Доказательство свойства 1.** Пусть $\sum\limits_{k=1}^{\infty}a_k=S$, $S_N=\sum\limits_{k=1}^{N}a_k$. Ряд сходится $\Rightarrow$ $S$ существует, $-\infty<S<+\infty$. Тогда

$$a_N=S_N-S_{N-1}\to S-S=0.\ \blacksquare$$

**Пример.** $\sum\limits_{k=1}^{\infty}\dfrac{1}{k}=1+\dfrac{1}{2}+\dfrac{1}{3}+\dfrac{1}{4}+\ldots$ — гармонический ряд, расходится. При этом $a_k=\dfrac{1}{k}\to0$.

$$S_{2^m}=1+\frac{1}{2}+\left(\frac{1}{3}+\frac{1}{4}\right)+\left(\frac{1}{5}+\ldots+\frac{1}{8}\right)+\ldots+\left(\frac{1}{2^{m-1}+1}+\ldots+\frac{1}{2^m}\right)\ge1+\frac{1}{2}+\frac{1}{2}+\frac{1}{2}+\ldots+\frac{1}{2}=$$

⟦M071⟧

(в тетради над группами слагаемых надписано: $\dfrac{1}{3}+\dfrac{1}{4}>\dfrac{1}{2}$; $\dfrac{1}{5}+\ldots+\dfrac{1}{8}>\dfrac{1}{2}$; $\dfrac{1}{2^{m-1}+1}+\ldots+\dfrac{1}{2^m}>\dfrac{1}{2}$)

$$=1+\frac{m}{2}\to+\infty\ \text{при } m\to\infty.$$

Далее: $\{S_{2^m}\}$, $\forall m$ $S_{2^m}\ge1+\dfrac{m}{2}$ $\Rightarrow$ $S_{2^m}\to+\infty$ $\Rightarrow$ $S_m$ расходится (на полях пометка ). ⟦M073⟧ ⟦U072⟧

**Доказательство свойства 2.** Пусть $n>m$:

$$\sum_{k=1}^{n}a_k=\sum_{k=1}^{m}a_k+\sum_{k=m+1}^{n}a_k. \tag{$*$}$$

(под формулой отмечено: конечное число при $n\to\infty$.) Перейдём в $(*)$ к пределу при $n\to\infty$. Предел в правой и левой частях $(*)$ существует (имеет смысл) одновременно:

$$\sum_{k=1}^{n}a_k\to S;\qquad \left(\sum_{k=1}^{m}a_k\right)=A;\qquad \sum_{k=m+1}^{n}a_k\to S_1=\sum_{k=m+1}^{\infty}a_k,$$

⟦S074⟧

$$A+S_1=\sum_{k=m+1}^{\infty}a_k.$$

На полях отмечено: сходимость $\sum\limits_{k=1}^{\infty}a_k$ и $\sum\limits_{k=m+1}^{\infty}a_k$ равносильны.

**Следствие (из свойства 2).** Если $\sum\limits_{k=1}^{\infty}a_k$ сходится, то $\sum\limits_{k=m+1}^{\infty}a_k\to0$ при $m\to\infty$ (остаток сходящегося ряда стремится к $0$).

**Доказательство следствия.**

$$\sum_{k=m+1}^{n}a_k=\sum_{k=1}^{n}a_k-\sum_{k=1}^{m}a_k\to0,\qquad \sum_{k=1}^{\infty}a_k-\sum_{k=1}^{\infty}a_k. \ \blacksquare$$

⟦S075⟧

> [!warning] S070, M071, U072, M073, S074, S075 — см. ocr/ISSUES.md
> S070: нумерация 1), 2) внутри «Замечания» совпадает с нумерацией самих свойств.
> M071: число групп и их границы в записи не согласованы.
> U072: надпись на полях мелкая и перечёркнутая.
> M073: после вывода о подпоследовательности $S_{2^m}$ вывод делается про $S_m$.
> S074: схема со стрелками; часть подписей перекрывается стрелками.
> S075: стрелки и разность пределов набраны без пояснений.

## 11. Свойства рядов 3) и 4)

**Свойство 3.** Ряды $\sum\limits_{n=1}^{\infty}a_n=:(I)$ и $\sum\limits_{n=1}^{\infty}ka_n=:(II)$, $k\in\mathbb{R}$, сходятся и расходятся одновременно. Если $(I)$ и $(II)$ сходятся, то $\sum\limits_{n=1}^{\infty}ka_n=k\sum\limits_{n=1}^{\infty}a_n$.

**Свойство 4.** Если два ряда $\sum\limits_{n=1}^{\infty}a_n$ и $\sum\limits_{n=1}^{\infty}b_n$ сходятся, то ряд $\sum\limits_{n=1}^{\infty}(a_n+b_n)$ сходится и

$$\sum_{n=1}^{\infty}(a_n+b_n)=\sum_{n=1}^{\infty}a_n+\sum_{n=1}^{\infty}b_n.$$

⟦S076⟧

**Доказательство свойств 3 и 4.** Пусть $k\in\mathbb{R}$. Тогда при $N\to\infty$

$$\sum_{n=1}^{N}ka_n=k\sum_{n=1}^{N}a_n\ \longrightarrow\ \sum_{n=1}^{\infty}ka_n=k\sum_{n=1}^{\infty}a_n,$$

$$\sum_{n=1}^{N}(a_n+b_n)=\sum_{n=1}^{N}a_n+\sum_{n=1}^{N}b_n\ \longrightarrow\ \sum_{n=1}^{\infty}(a_n+b_n)=\sum_{n=1}^{\infty}a_n+\sum_{n=1}^{\infty}b_n.\ \blacksquare$$

⟦S077⟧

### Замечание

Если $\sum\limits_{n=1}^{\infty}a_n$ расходится, а $\sum\limits_{n=1}^{\infty}b_n$ сходится, то $\sum\limits_{n=1}^{\infty}(a_n+b_n)$ расходится, так как если бы $\sum\limits_{n=1}^{\infty}(a_n+b_n)$ сходился, то тогда сходился бы ряд с членами $a_n=(a_n+b_n)-b_n$. Противоречие.

> [!warning] S076, S077 — см. ocr/ISSUES.md
> S076: свойства 3) и 4) записаны подряд без заголовка.
> S077: два доказательства записаны параллельно в две колонки; границы колонок восстановлены по расположению.

## 12. Критерий Больцано–Коши

$$\sum_{n=1}^{\infty}a_n\ \text{сходится}\ \Leftrightarrow\ \forall\varepsilon>0\ \exists N\in\mathbb{N}\ \forall n>N\ \forall p>0:\ \left|\sum_{k=n+1}^{n+p}a_k\right|=\left|a_{n+1}+\ldots+a_{n+p}\right|<\varepsilon.$$

⟦T078⟧

**Доказательство.** По определению, $\sum\limits_{n=1}^{\infty}a_n$ сходится $\Leftrightarrow$ $\{S_m\}$ имеет конечный предел при $m\to\infty$, где $S_m:=\sum\limits_{n=1}^{m}a_n$. Далее используется критерий Больцано–Коши для последовательности $\{S_m\}$ (он доказан):

$$\forall\varepsilon>0\ \exists N\in\mathbb{N}:\ \forall m,n>N\ |S_m-S_n|<\varepsilon.$$

Без ограничения общности можно считать, что $m>n$, следовательно $p:=m-n$, $p\in\mathbb{N}$ и

$$S_m-S_n=\sum_{k=n+1}^{m}a_k.\ \blacksquare$$

> [!warning] T078 — см. ocr/ISSUES.md
> T078: сказано «$p>0$», хотя $p$ — число слагаемых и должно быть натуральным.

## 13. Расходимость и переписанные члены ряда

Заголовок в тетради: «Как-во расх-ся ряда с перепис. членами» ⟦U079⟧.
Нужно найти последовательность $\{m_n\}$ такую, что $m_n>n$ и $\sum\limits_{k=n}^{m_n}a_k\nrightarrow0$ при $m_n\to\infty$ (на полях: $k=n$, $m_n\to\infty$).

### Замечание

Часто выбирают $m_n=\alpha\cdot n$, где $\alpha>1$.

**Пример.**

$$\sum_{k=n}^{2n}\frac{1}{k}\to(n+1)\frac{1}{2n}\to0,$$

⟦T080⟧

$$\sum_{k=n}^{2n}\frac{1}{k}=\frac{1}{n}+\frac{1}{n+1}+\ldots+\frac{1}{2n}\ge\frac{1}{2n}+\frac{1}{2n}+\ldots+\frac{1}{2n}=\frac{n+1}{2n}.$$

> [!warning] U079, T080 — см. ocr/ISSUES.md
> U079: заголовок не читается как осмысленная фраза.
> T080: записано «$\to$» там, где ниже стоит оценка «$\ge$», и предел $0$, а не $\frac12$.

## 14. Абсолютная сходимость

### Определение 7.2.1

Ряд $\sum\limits_{n=1}^{\infty}a_n$ называется абсолютно сходящимся, если ряд $\sum\limits_{n=1}^{\infty}|a_n|$ сходится.

**Свойство 5.** Если ряд абсолютно сходится, то он сходится.

**Доказательство.** Фиксируем $\forall\varepsilon>0$ и применяем критерий Больцано–Коши. Ранее доказано: ⟦U081⟧ ⟦U082⟧

$$\sum_{k=1}^{\infty}|a_k|\ \text{сходится}\ \Leftrightarrow\ \exists N\in\mathbb{N}:\ \forall n>N\ \forall p\in\mathbb{N}\ \sum_{k=n+1}^{n+p}|a_k|<\varepsilon.$$

Но тогда

$$\left|\sum_{k=n+1}^{n+p}a_k\right|\le\sum_{k=n+1}^{n+p}|a_k|\ \Rightarrow\ \text{критерий Больцано–Коши}\ \Rightarrow\ \sum_{k=1}^{\infty}a_k\ \text{сходится}.\ \blacksquare$$

> [!warning] U081, U082 — см. ocr/ISSUES.md
> U081: перед «и применяем» пропущено сказуемое; восстановить нельзя.
> U082: первое слово прочитывается как «Шаг», но по смыслу ожидается ссылка на уже доказанное.

---

Source: pages p012–p021.

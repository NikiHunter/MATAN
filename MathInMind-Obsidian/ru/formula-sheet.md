---
title: "Формулы математического анализа"
lang: ru
tags: [mathinmind/ru, mathinmind/support]
---
# Формулы математического анализа

[[ru/index|Оглавление]] · [[ru/00-notation|Обозначения]] · [[ru/glossary|Глоссарий]]

> [!note] Внимание
> Здесь собраны формулы, а не условия теорем. Перед применением обращайтесь к соответствующей главе.

## Последовательности и ряды — [[ru/03-sequences|главы 3–4]]

$$
a_n\to a,\ b_n\to b\implies a_nb_n\to ab,\quad a_n+b_n\to a+b.
$$

Монотонность + ограниченность $\implies$ сходимость. В $\mathbb R$: сходимость $\iff$ фундаментальность.

$$
\sum_{n=0}^{\infty}q^n=\frac1{1-q}\quad(|q|<1),
\qquad
\sum_{n=1}^{\infty}\frac1{n^p}<\infty\iff p>1.
$$

Если $b_n\downarrow0$, то $\sum(-1)^{n-1}b_n$ сходится и $|R_N|\le b_{N+1}$.

## Производные и Тейлор — [[ru/06-derivatives|главы 6–7]]

$$
(fg)'=f'g+fg',\qquad
(g\circ f)'(a)=g'(f(a))f'(a),\qquad
(f^{-1})'(f(a))=\frac1{f'(a)}.
$$

$$
f(b)-f(a)=f'(c)(b-a),\qquad
f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n(x).
$$

$$
e^x=\sum_{n=0}^{\infty}\frac{x^n}{n!},\qquad
\sin x=\sum_{n=0}^{\infty}\frac{(-1)^nx^{2n+1}}{(2n+1)!},
$$
$$
\cos x=\sum_{n=0}^{\infty}\frac{(-1)^nx^{2n}}{(2n)!},\qquad
\log(1+x)=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}x^n}{n}\quad(-1<x\le1).
$$

[[ru/06-derivatives#6.1 Определение и линейное приближение|Дифференцируемая]] выпуклая $f$ удовлетворяет $f(y)\ge f(x)+f'(x)(y-x)$ и [[ru/07-taylor-convexity#^jensen-inequality|неравенству Йенсена]].

## Интеграл одной переменной — [[ru/08-riemann-integration|главы 8–9]]

$$
\frac{d}{dx}\int_a^x f(t)\,dt=f(x),
\qquad
\int_a^b f(x)\,dx=F(b)-F(a)\quad(F'=f).
$$

$$
\int_a^b u\,dv=[uv]_a^b-\int_a^b v\,du,
\qquad
\int_a^b f(\varphi(x))\varphi'(x)\,dx=\int_{\varphi(a)}^{\varphi(b)}f(t)\,dt.
$$

$$
\int_1^\infty\frac{dx}{x^p}<\infty\iff p>1,
\qquad
\int_0^1\frac{dx}{x^p}<\infty\iff p<1.
$$

Площадь $A=\int(f-g)\,dx$, длина $L=\int\sqrt{1+(y')^2}\,dx$, объём вращения $V=\pi\int f^2\,dx$.

## Функциональные и степенные ряды — [[ru/10-function-sequences-series|главы 10–12]]

[[ru/10-function-sequences-series#10.1 Два вида сходимости|Равномерная сходимость]]: $\sup_E|f_n-f|\to0$. Вейерштрасс: $|f_n|\le M_n$ и $\sum M_n<\infty$ влекут равномерную [[ru/04-numeric-series#4.3 Абсолютная и условная сходимость|абсолютную сходимость]].

$$
\frac1R=\limsup\sqrt[n]{|c_n|},\qquad
\frac{d}{dx}\sum c_n(x-a)^n=\sum nc_n(x-a)^{n-1}\quad(|x-a|<R).
$$

[[ru/12-fourier-series#12.1 Тригонометрическая система и коэффициенты|Коэффициенты Фурье]] на $(-\pi,\pi)$:

$$
a_n=\frac1\pi\int_{-\pi}^{\pi}f\cos(nx)\,dx,
\qquad
b_n=\frac1\pi\int_{-\pi}^{\pi}f\sin(nx)\,dx.
$$

$$
\frac1\pi\int_{-\pi}^{\pi}|f|^2\,dx
=\frac{a_0^2}{2}+\sum_{n=1}^{\infty}(a_n^2+b_n^2).
$$

## Несколько переменных — [[ru/14-several-variables|главы 14–18]]

$$
F(a+h)=F(a)+DF(a)h+o(\|h\|),
\qquad
D(G\circ F)=DG(F(a))DF(a).
$$

$$
f(a+h)=f(a)+\nabla f(a)\cdot h+\frac12h^THf(a)h+o(\|h\|^2).
$$

Неявное дифференцирование: $F(x,y)=0\implies y'=-F_x/F_y$ при $F_y\ne0$. Лагранж: $\nabla f=\lambda\nabla g$ на $g=c$.

$$
dA=r\,dr\,d\theta,\qquad
dV=r\,dr\,d\theta\,dz,\qquad
dV=\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta.
$$

Общая замена: $dv=|\det DT|\,du$.

$$
\oint_{\partial D}P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dA,
$$
$$
\oint_{\partial\Sigma}F\cdot dr=\iint_\Sigma(\nabla\times F)\cdot n\,dS,
\qquad
\iint_{\partial\Omega}F\cdot n\,dS=\iiint_\Omega\nabla\cdot F\,dV.
$$

## Мера, Лебег и $L^p$ — [[ru/19-measure-theory|главы 19–21]]

- Монотонная сходимость: $0\le f_n\uparrow f\implies\int f_n\uparrow\int f$.
- Фату: $\int\liminf f_n\le\liminf\int f_n$ для $f_n\ge0$.
- [[ru/20-lebesgue-integration#^dominated-convergence-theorem|Мажорированная сходимость]]: $f_n\to f$ [[ru/19-measure-theory#19.4 Измеримые функции|п.в.]] и $|f_n|\le g\in L^1$ влекут $\int f_n\to\int f$.

$$
\|f\|_p=\left(\int|f|^p\,d\mu\right)^{1/p},
\qquad
\int|fg|\,d\mu\le\|f\|_p\|g\|_q\quad(1/p+1/q=1),
$$
$$
\|f+g\|_p\le\|f\|_p+\|g\|_p,
\qquad
\langle f,g\rangle_{L^2}=\int f\overline g\,d\mu.
$$

На пространстве конечной [[ru/19-measure-theory#19.2 Меры|меры]] $r<p\implies L^p\subseteq L^r$. Все $L^p$ полны; $L^2$ — [[ru/21-lp-spaces#^sec-21-4|гильбертово пространство]].

## Таблица производных и приёмы дифференцирования

Определения и доказательства — в [[ru/06-derivatives#6.1 Определение и линейное приближение|главе 6]], [[ru/15-multivariable-differentiation#15.2 Частные производные и производные по направлению|частные производные]] — в [[ru/15-multivariable-differentiation#15.5 Частные производные: вычисление, примеры, приёмы|§15.5]]. Здесь $\ln$ — натуральный логарифм; в главах курса он же обозначается $\log$ (см. [[ru/00-notation|обозначения]]).

### Таблица 1. Производные основных функций

| Функция | Производная | Где верно |
|---|---|---|
| $x^\alpha$, $\alpha\in\mathbb R$ | $\alpha x^{\alpha-1}$ | $x>0$; при $\alpha\in\mathbb N$ — все $x\in\mathbb R$; при целом $\alpha<0$ — все $x\ne0$ |
| $a^x$ | $a^x\ln a$ | $x\in\mathbb R$; $a>0$, $a\ne1$ |
| $e^x$ | $e^x$ | $x\in\mathbb R$ |
| $\ln\lvert x\rvert$ | $\dfrac1x$ | $x\ne0$ |
| $\log_a\lvert x\rvert$ | $\dfrac1{x\ln a}$ | $x\ne0$; $a>0$, $a\ne1$ |
| $\sin x$ | $\cos x$ | $x\in\mathbb R$ |
| $\cos x$ | $-\sin x$ | $x\in\mathbb R$ |
| $\operatorname{tg}x$ | $\dfrac1{\cos^2x}=1+\operatorname{tg}^2x$ | $x\ne\frac\pi2+\pi k$, $k\in\mathbb Z$ |
| $\operatorname{ctg}x$ | $-\dfrac1{\sin^2x}=-(1+\operatorname{ctg}^2x)$ | $x\ne\pi k$, $k\in\mathbb Z$ |
| $\arcsin x$ | $\dfrac1{\sqrt{1-x^2}}$ | $-1<x<1$ |
| $\arccos x$ | $-\dfrac1{\sqrt{1-x^2}}$ | $-1<x<1$ |
| $\operatorname{arctg}x$ | $\dfrac1{1+x^2}$ | $x\in\mathbb R$ |
| $\operatorname{arcctg}x$ | $-\dfrac1{1+x^2}$ | $x\in\mathbb R$ |
| $\operatorname{sh}x=\frac{e^x-e^{-x}}2$ | $\operatorname{ch}x$ | $x\in\mathbb R$ |
| $\operatorname{ch}x=\frac{e^x+e^{-x}}2$ | $\operatorname{sh}x$ | $x\in\mathbb R$ |

Если $x^\alpha$ определена и при $x<0$ (например, $\alpha=p/q$ с нечётным $q$), формула $(x^\alpha)'=\alpha x^{\alpha-1}$ верна при всех $x\ne0$. В нуле производная тогда существует при $\alpha\ge1$ и не существует при $0<\alpha<1$: для $\sqrt[3]x$ разностное отношение $\sqrt[3]h/h\to+\infty$.

### Таблица 2. Правила дифференцирования

| Правило | Формула | Условия |
|---|---|---|
| Линейность | $(\alpha f+\beta g)'=\alpha f'+\beta g'$ | $f$, $g$ дифференцируемы в точке; $\alpha,\beta\in\mathbb R$ |
| Произведение | $(fg)'=f'g+fg'$ | $f$, $g$ дифференцируемы в точке |
| Частное | $\left(\dfrac fg\right)'=\dfrac{f'g-fg'}{g^2}$ | $f$, $g$ дифференцируемы в точке, $g\ne0$ |
| [[ru/06-derivatives#^chain-rule\|Правило цепочки]] | $\bigl(g(f(x))\bigr)'=g'(f(x))\,f'(x)$ | $f$ дифференцируема в $x$, $g$ — в $f(x)$ |
| [[ru/06-derivatives#6.2 Правила дифференцирования\|Обратная функция]] | $(f^{-1})'(y_0)=\dfrac1{f'(x_0)}$, где $y_0=f(x_0)$ | $f$ непрерывна и строго монотонна около $x_0$, $f'(x_0)\ne0$ |
| [[ru/16-implicit-functions-extrema#16.3 Теорема о неявной функции\|Неявная функция]] | $F(x,y(x))\equiv0\ \Rightarrow\ y'=-\dfrac{F_x}{F_y}$ | $F\in C^1$ около точки, $F_y\ne0$ в ней |
| Логарифмическое дифференцирование | $(u^v)'=\bigl(e^{v\ln u}\bigr)'=u^v\Bigl(v'\ln u+\dfrac{v\,u'}u\Bigr)$ | $u>0$; $u$, $v$ дифференцируемы |
| [[ru/06-derivatives#6.3 Дифференциал и параметрические кривые\|Формула Лейбница]] | $(fg)^{(n)}=\sum_{k=0}^{n}\binom nk f^{(k)}g^{(n-k)}$ | $f$, $g$ дифференцируемы $n$ раз |

### Приёмы

- **Сначала перепишите, потом дифференцируйте.** Корни и дроби с $x$ в знаменателе — в степени: $\left(\frac1{x^3}\right)'=(x^{-3})'=-3x^{-4}=-\frac3{x^4}$, $(x\sqrt x)'=(x^{3/2})'=\frac32\sqrt x$. Правило частного дало бы тот же ответ, но длиннее.
- **Произведения, частные и степени логарифмируйте.** Там, где $y\ne0$, $y'=y\,(\ln\lvert y\rvert)'$, а $\ln\lvert y\rvert$ распадается в сумму: для $y=\frac{x^2(x+1)^3}{(x-1)^4}$ получаем $y'=y\left(\frac2x+\frac3{x+1}-\frac4{x-1}\right)$. Степень $u^v$ всегда переписывайте как $e^{v\ln u}$: $(x^{\sin x})'=x^{\sin x}\left(\cos x\ln x+\frac{\sin x}x\right)$ при $x>0$. Для запоминания: $(u^v)'=v\,u^{v-1}u'+u^v\ln u\cdot v'$, то есть сумма производной «как от степени» и «как от показательной функции»; любое из двух слагаемых по отдельности — ошибка.
- **Разбирайте «матрёшку».** Определите порядок операций снаружи внутрь; каждый слой даёт один множитель: $\bigl(e^{\sin(x^2)}\bigr)'=e^{\sin(x^2)}\cdot\cos(x^2)\cdot2x$. Потерянный множитель от внутренней функции — самая частая ошибка.
- **Обратную функцию дифференцируйте в соответствующей точке.** $(f^{-1})'(y_0)=\frac1{f'(x_0)}$, где $x_0$ находят из $f(x_0)=y_0$; явная формула для $f^{-1}$ не нужна. Для $f(x)=x^3+x$: $f(1)=2$, $f'(1)=4$, поэтому $(f^{-1})'(2)=\frac14$, а не $\frac1{f'(2)}=\frac1{13}$.
- **Неявную функцию дифференцируйте вместе с тождеством.** Помните, что $y=y(x)$, поэтому $(y^2)'=2y\,y'$. Из $x^2+y^2=1$ получаем $2x+2y\,y'=0$ и $y'=-\frac xy$ при $y\ne0$; это то же, что $-F_x/F_y$.
- **В формуле Лейбница берите многочлен за $f$.** У многочлена степени $m$ производные порядка больше $m$ равны нулю, и в сумме остаётся не больше $m+1$ ненулевых слагаемых: $(x^2e^x)^{(n)}=e^x\bigl(x^2+2nx+n(n-1)\bigr)$.
- **Проверяйте ответ.** Производная чётной функции нечётна, нечётной — чётна, $T$-периодической — $T$-периодична. Численная проверка: $f'(x_0)\approx\frac{f(x_0+h)-f(x_0-h)}{2h}$ при малом $h$.

### Самопроверка

1. Найдите $\left(\dfrac1{\sqrt[3]{x^2}}\right)'$ при $x>0$.
2. Почему $(\ln\lvert x\rvert)'=\dfrac1x$ и при $x<0$?
3. Пусть $f(x)=x+e^x$. Найдите $(f^{-1})'(1)$.
4. Найдите $\bigl(x^{x^2}\bigr)'$ при $x>0$.
5. Найдите $(x\sin x)^{(10)}$.

> [!answer]- Ответы
> 1. $\bigl(x^{-2/3}\bigr)'=-\frac23x^{-5/3}$.
> 2. При $x<0$ имеем $\ln\lvert x\rvert=\ln(-x)$, и по правилу цепочки $\bigl(\ln(-x)\bigr)'=\frac1{-x}\cdot(-1)=\frac1x$.
> 3. $f'(x)=1+e^x>0$, так что $f$ строго возрастает и $f^{-1}$ определена. $f(0)=1$ и $f'(0)=2$, поэтому $(f^{-1})'(1)=\frac12$.
> 4. $x^{x^2}=e^{x^2\ln x}$, поэтому $\bigl(x^{x^2}\bigr)'=x^{x^2}(2x\ln x+x)=x^{x^2+1}(2\ln x+1)$.
> 5. По формуле Лейбница с $f=x$ остаются два слагаемых: $x\,(\sin x)^{(10)}+10\,(\sin x)^{(9)}$. Так как $(\sin x)^{(n)}=\sin\bigl(x+\frac{\pi n}2\bigr)$, получаем $-x\sin x+10\cos x$.

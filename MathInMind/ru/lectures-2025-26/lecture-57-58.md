---
title: "Лекции 57–58 — внутренность, граница, компактность и предел отображения"
lang: ru
course: "Математический анализ, 2025/26"
lecture: 57-58
semester: 2
date: 2026-05-07
source: "ma25_26-lectures_57-58_notes.pdf.txt"
pdf_pages: 37
typed_slides: 18
---

# Лекции 57–58 — внутренность, граница, компактность и предел отображения

[Индекс лекций](index.md) · [English](../../en/lectures-2025-26/lecture-57-58.md) · [Español](../../es/lectures-2025-26/lecture-57-58.md) · [Назад: 55–56](lecture-55-56.md) · [Далее: 59–60](lecture-59-60.md)


> **Источник и охват.** `ma25_26-lectures_57-58_notes.pdf.txt`: 37 страниц PDF, 18 печатных слайдов и 19 рукописных страниц; дата 07 мая 2026. Печатные слайды 1–4 занимают страницы PDF 1–4; далее слайд 5 — страница 7, слайд 6 — 10, слайд 7 — 13, слайд 8 — 14, слайд 9 — 15, слайд 10 — 17, слайд 11 — 22, слайд 12 — 23, слайд 13 — 24, слайд 14 — 25, слайд 15 — 29, слайд 16 — 32, слайд 17 — 33 и слайд 18 — 35. Рукописные страницы PDF 5, 6, 8, 9, 11, 12, 16, 18, 19, 20, 21, 26, 27, 28, 30, 31, 34, 36 и 37 включены. Рукописные пометки на слайдах 4, 5 и 11 отнесены к своим слайдам. Использован только PDF из чата; исходная папка не просматривалась, поэтому архивные имена и ссылки не указываются.

> **Дублирование семестра 2.** Лекции тематически пересекаются с [§5.3](../../ru/lectures/11-topology-rn-5-3.md) и [§5.4](../../ru/lectures/12-mapping-limits-5-4.md); см. также [регистр](../../ru/lectures/index.md). Семестр 2 охватывает лекции 33–64.

## Печатный слайд 1 (стр. PDF 1) — Титульный слайд

«Математический анализ», лекции 57–58; Д. Е. Апушкинская, РУДН; 07 мая 2026.

## Печатный слайд 2 (стр. PDF 2) — Цитата дня

«Три яблока изменили наш мир: первым соблазнили Еву, второе разбудило Ньютона, а третье попалось на глаза Стиву Джобсу». Под цитатой на слайде размещена обложка книги «Три яблока, которые изменили мир» с портретами Ньютона, Евы и Джобса; это декоративная иллюстрация, а не математический материал.

## Печатный слайд 3 (стр. PDF 3) — Цель лекции

Продолжается описание в $\mathbb R^n$ разумных аналогов открытых и замкнутых промежутков и компактных множеств. Вводится понятие предела отображения нескольких переменных и доказываются для таких отображений аналоги некоторых одномерных утверждений.

## Печатный слайд 4 (стр. PDF 4) — Внутренность множества — определение 5.3.3

**Определение 5.3.3.** Пусть $E\subset\mathbb R^n$. Множество всех внутренних точек $E$ называется внутренностью $E$ и обозначается $\operatorname{Int}E$.

**Замечания.** 1) Для любого $E\subset\mathbb R^n$ множество $\operatorname{Int}E$ открыто в $\mathbb R^n$. 2) Если $G$ открыто в $\mathbb R^n$ и $G\subset E$, то $G\subset\operatorname{Int}E$. 3) Для любого $E\subset\mathbb R^n$

$$
\mathbb R^n\setminus\overline E=\operatorname{Int}\left(\mathbb R^n\setminus E\right),
$$

$$
\mathbb R^n\setminus\operatorname{Int}E=\overline{\left(\mathbb R^n\setminus E\right)}.
$$

4) Если $E$ открыто, то $\operatorname{Int}E=E$. 5) Если $E\subset\mathbb R^n$, то $\operatorname{Int}E$ — наибольшее по включению открытое множество, содержащееся в $E$.

![Определение 5.3.3 и замечания (стр. PDF 4)](../../assets/lectures-2025-26/lec57-58-p04-interior-remarks.jpg)

> **Пометки на слайде.** У замечания 3 стоит пометка «упр!» — равенства предлагается доказать самостоятельно. Внизу от руки дописано: «Если $E$ — открыто, то $\operatorname{Int}E=E$» — это замечание 4, вынесенное на поля. В текстовом слое PDF надчёркивания в замечании 3 частично теряются; здесь они восстановлены по изображению.

## Рукописная страница (стр. PDF 5) — Замечание 1: $\operatorname{Int}E$ открыто

Утверждение: $\forall E\subset\mathbb R^n\Rightarrow\operatorname{Int}E$ открыто в $\mathbb R^n$.

Доказательство. Пусть $a\in\operatorname{Int}E$; тогда по определению внутренней точки $\exists\delta>0$: $V_\delta(a)\subset E$. Множество $V_\delta(a)$ открыто, поэтому $\forall x\in V_\delta(a)$ является внутренней точкой для $V_\delta(a)$ и, тем более, для $E$. Следовательно, $V_\delta(a)\subset\operatorname{Int}E$; значит, каждая точка $\operatorname{Int}E$ имеет окрестность, лежащую в $\operatorname{Int}E$, то есть $\operatorname{Int}E$ открыто.

$$
a\in\operatorname{Int}E\ \Longrightarrow\ \exists\delta>0:\ V_\delta(a)\subset E
$$

$$
V_\delta(a)\subset\operatorname{Int}E
$$

![Доказательство открытости внутренности (стр. PDF 5)](../../assets/lectures-2025-26/lec57-58-p05-interior-open-proof.jpg)

## Рукописная страница (стр. PDF 6) — Замечание 2: $G\subset\operatorname{Int}E$

Утверждение: если $G$ открыто в $\mathbb R^n$ и $G\subset E$, то $G\subset\operatorname{Int}E$.

Доказательство. Пусть $a\in G$; так как $G$ открыто, $a$ — внутренняя точка $G$. Поскольку $G\subset E$, точка $a$ является внутренней и для $E$. Значит, $a\in\operatorname{Int}E$, то есть $G\subset\operatorname{Int}E$.

$$
\left.\begin{aligned} a&\in G\\ G&\text{ — открыто}\end{aligned}\right\}\Longrightarrow a\ \text{— внутренняя точка } G
$$

$$
a\in\operatorname{Int}E
$$

## Печатный слайд 5 (стр. PDF 7) — Граница множества — определение 5.3.4

**Определение 5.3.4.** Пусть $E\subset\mathbb R^n$. Множество $E\setminus\operatorname{Int}E$ называется границей $E$ и обозначается $\partial E$.

**Замечание.** Граница $\partial E$ любого множества $E\subset\mathbb R^n$ замкнута.

**Пример.** Пусть $a\in\mathbb R^n$, $\delta>0$. Тогда справедливы следующие утверждения. 1) $\operatorname{Int}B_\delta(a)=B_\delta(a)$. 2) $\partial\left(\overline{B_\delta(a)}\right)=\partial B_\delta(a)=S_\delta(a)$.

$$
\partial E:=E\setminus\operatorname{Int}E
$$

Рукописные пометки на слайде: у замечания — «разность замкнутого и открытого», у примера — «1) $B_\delta(a)$ — открытое мн-во».

## Рукописная страница (стр. PDF 8) — Первая часть примера: $\operatorname{Int}\overline{B_\delta(a)}=B_\delta(a)$

Требуется доказать, что $\operatorname{Int}\overline{B_\delta(a)}=B_\delta(a)$. Напомним обозначения:

$$
B_\delta(a)=\{x\in\mathbb R^n:\ \|x-a\|<\delta\},
$$

$$
\overline{B_\delta(a)}=\{x\in\mathbb R^n:\ \|x-a\|\le\delta\},
$$

$$
S_\delta(a)=\{x\in\mathbb R^n:\ \|x-a\|=\delta\}.
$$

Множество $B_\delta(a)$ открыто, поэтому $B_\delta(a)\subset\operatorname{Int}\overline{B_\delta(a)}$. Проверим обратное включение. Так как $\overline{B_\delta(a)}\setminus B_\delta(a)=S_\delta(a)$, достаточно показать, что никакая точка сферы $S_\delta(a)$ не является внутренней для $\overline{B_\delta(a)}$.

$$
B_\delta(a)\subset\operatorname{Int}\overline{B_\delta(a)}
$$

## Рукописная страница (стр. PDF 9) — Точки сферы не внутренние

Пусть $x\in S_\delta(a)$; положим

$$
x^k=a+\left(1+\frac1k\right)(x-a),\qquad k\in\mathbb N.
$$

Тогда $\forall k\in\mathbb N$ точка $x^k\notin\overline{B_\delta(a)}$, поскольку

$$
\|x^k-a\|=\left(1+\frac1k\right)\|x-a\|=\left(1+\frac1k\right)\delta>\delta,
$$

так как $x\in S_\delta(a)\Rightarrow\|x-a\|=\delta$. Далее, $\lim_{k\to\infty}x^k=x$, поэтому любая окрестность точки $x$ содержит точки $\{x^k\}$, то есть $x\notin\operatorname{Int}\overline{B_\delta(a)}$. Следовательно,

$$
\operatorname{Int}\overline{B_\delta(a)}\subset B_\delta(a).
$$

![Точки сферы не являются внутренними (стр. PDF 9)](../../assets/lectures-2025-26/lec57-58-p09-sphere-not-interior.jpg)

## Печатный слайд 6 (стр. PDF 10) — Открытые и замкнутые подмножества

**Определение 5.3.5.** Пусть $E\subset\mathbb R^n$, $F\subset E$. 1) Точка $a\in F$ называется внутренней для $F$ в $E$, если у неё есть окрестность $(V_\delta(a)\cap E)\subset F$. 2) Множество $F$ называется открытым в $E$, если любая его точка является внутренней для $F$ в $E$. 3) Множество $F$ называется замкнутым в $E$, если его дополнение $E\setminus F$ открыто в $E$.

**Теорема 5.3.4.** Пусть $F\subset E\subset\mathbb R^n$. Тогда равносильны следующие утверждения. 1) Множество $F$ открыто в $E$. 2) Существует открытое в $\mathbb R^n$ множество $G$, для которого $F=E\cap G$.

$$
\left(V_\delta(a)\cap E\right)\subset F
$$

$$
F=E\cap G
$$

## Рукописная страница (стр. PDF 11) — Доказательство теоремы 5.3.4: 1) ⇒ 2)

Пусть $F$ открыто в $E$. Тогда $\forall a\in F$ точка $a$ является внутренней для $F$ в $E$, то есть

$$
\exists\delta_a>0:\ \left(V_{\delta_a}(a)\cap E\right)\subset F.
$$

Положим

$$
G=\bigcup_{a\in F}V_{\delta_a}(a).
$$

Множество $G$ открыто в $\mathbb R^n$ как объединение открытых шаров. Далее,

$$
G\cap E=\bigcup_{a\in F}\left(V_{\delta_a}(a)\cap E\right)\subset F,
$$

а включение $F\subset G\cap E$ очевидно, так как $F\subset G$ и $F\subset E$. Следовательно, $F=E\cap G$ — точнее, $F=G\cap E$.

$$
G\cap E=\bigcup_{a\in F}\left(V_{\delta_a}(a)\cap E\right)\subset F
$$

## Рукописная страница (стр. PDF 12) — Доказательство теоремы 5.3.4: 2) ⇒ 1)

Пусть $F=E\cap G$, где $G$ открыто в $\mathbb R^n$. Проверим, что $F$ открыто в $E$. Пусть $a\in F=E\cap G$; поскольку $G$ открыто, $\exists\delta>0$: $V_\delta(a)\subset G$. Тогда

$$
V_\delta(a)\cap E\subset G\cap E=F,
$$

то есть $a$ — внутренняя точка $F$ в $E$. Значит, $F$ открыто в $E$.

$$
V_\delta(a)\cap E\subset G\cap E=F
$$

## Печатный слайд 7 (стр. PDF 13) — Замечания к теореме 5.3.4

1) Пусть $F\subset E\subset\mathbb R^n$. Если $E$ открыто в $\mathbb R^n$, то по теоремам 5.3.2 и 5.3.4 открытость множества $F$ в $E$ эквивалентна его открытости в $\mathbb R^n$. Для произвольного $E$ это уже не так: например, множество $(0,1)\cap\mathbb Q$ открыто в $\mathbb Q$, но не в $\mathbb R$. 2) Утверждение, аналогичное теореме 5.3.4, справедливо и для замкнутых в $E$ множеств.

$$
(0,1)\cap\mathbb Q
$$

## Печатный слайд 8 (стр. PDF 14) — Покрытие множества и компактность

**Определение 5.3.6.** Пусть $E\subset\mathbb R^n$. 1) Если $\Omega$ — такое семейство подмножеств $\mathbb R^n$, что $\bigcup_{A\in\Omega}A\supset E$, то говорят, что $\Omega$ является покрытием $E$ (или $\Omega$ покрывает $E$). 2) Пусть $\tilde\Omega$ — подсемейство $\Omega$, которое также покрывает $E$. Тогда $\tilde\Omega$ называют подпокрытием $\Omega$.

**Определение 5.3.7.** Множество $E\subset\mathbb R^n$ называется компактным (или компактом), если из любого открытого покрытия $E$ можно выбрать конечное подпокрытие.

![Определения покрытия и компактности (стр. PDF 14)](../../assets/lectures-2025-26/lec57-58-p14-compact-cover.jpg)

$$
\bigcup_{A\in\Omega}A\supset E
$$

## Печатный слайд 9 (стр. PDF 15) — Замечания о компактных множествах

1) Если множество $E\subset\mathbb R^n$ компактно, то любое замкнутое подмножество $E$ также компактно. 2) Любой замкнутый куб $K\subset\mathbb R^n$ компактен.

## Рукописная страница (стр. PDF 16) — Доказательство замечания 1

Пусть $F$ — замкнутое подмножество компакта $E$, а $\Omega$ — открытое покрытие $F$. Покажем, что из $\Omega$ можно выбрать конечное подпокрытие. Семейство

$$
\Omega\cup\left\{\mathbb R^n\setminus F\right\}
$$

является открытым покрытием компакта $E$: множества из $\Omega$ и множество $\mathbb R^n\setminus F$ открыты, а точки $E\setminus F$ покрываются последним из них. Выберем из этого покрытия конечное подсемейство $\tilde\Omega$, покрывающее $E$ — это можно сделать, так как $E$ компактно. Если $\mathbb R^n\setminus F$ входит в $\tilde\Omega$, удалим его; оставшиеся множества покрывают $F$. Итак, из $\Omega$ выбрано конечное подпокрытие $F$, то есть $F$ компактно.

$$
\Omega\cup\left\{\mathbb R^n\setminus F\right\},\qquad \tilde\Omega
$$

> **Расхождение в рукописи.** На первой строке добавленное множество записано верно, как $\mathbb R^n\setminus F$, а при выборе конечного подсемейства — как $\Omega\cup\left\{\mathbb R^n\setminus E\right\}$. Второе написание неверно: дополнение $\mathbb R^n\setminus E$ не покрывает $E$ и не помогает применить компактность $E$; далее используется $\mathbb R^n\setminus F$. Расхождение отмечено, но не исправлено в тексте рукописи.

![Доказательство компактности замкнутого подмножества (стр. PDF 16)](../../assets/lectures-2025-26/lec57-58-p16-closed-subset-compact.jpg)

## Печатный слайд 10 (стр. PDF 17) — Критерий компактности в $\mathbb R^n$

**Теорема 5.3.5.** Пусть $E\subset\mathbb R^n$. Тогда равносильны следующие утверждения. 1) $E$ компактно. 2) $E$ замкнуто и ограничено. 3) Из любой последовательности элементов $E$ можно выбрать сходящуюся подпоследовательность, предел которой также лежит в $E$.

**Замечание.** Импликацию 2) ⇒ 1) принято называть теоремой Гейне–Бореля.

## Рукописная страница (стр. PDF 18) — Доказательство теоремы 5.3.5: 1) ⇒ 3)

Схема доказательства: 1) ⇒ 3) ⇒ 2) ⇒ 1). Пусть $E$ компактно, и пусть $\{x^k\}_{k=1}^{\infty}$ — последовательность в $E$. Тогда по принципу выбора Больцано–Вейерштрасса $\exists\{x^{k_\ell}\}$ такая, что $x^{k_\ell}\to a$ и $a\in\mathbb R^n$. Проверим, что $a\in E$. Пусть $a\notin E$; рассмотрим семейство

$$
\Omega=\left\{\mathbb R^n\setminus\overline{V_\varepsilon(a)}\right\}_{\varepsilon>0},
$$

состоящее из открытых множеств. В силу закона де Моргана

$$
\bigcup_{A\in\Omega}A=\mathbb R^n\setminus\bigcap_{\varepsilon>0}\overline{V_\varepsilon(a)}=\mathbb R^n\setminus\{a\}\supset E,
$$

поэтому $\Omega$ — открытое покрытие $E$.

$$
\bigcup_{A\in\Omega}A=\mathbb R^n\setminus\bigcap_{\varepsilon>0}\overline{V_\varepsilon(a)}=\mathbb R^n\setminus\{a\}\supset E
$$

## Рукописная страница (стр. PDF 19) — Окончание 1) ⇒ 3): противоречие с компактностью

Итак, $\Omega$ покрывает $E$. Пусть теперь $\tilde\Omega$ — произвольное конечное подсемейство $\Omega$. Тогда $\exists m\in\mathbb N$ и $\varepsilon_1,\ldots,\varepsilon_m>0$ такие, что

$$
\tilde\Omega=\left\{\mathbb R^n\setminus\overline{V_{\varepsilon_k}(a)}\right\}_{k=1}^{m},
$$

следовательно,

$$
V(a):=\bigcap_{k=1}^{m}V_{\varepsilon_k}(a)
$$

— окрестность точки $a$. Заметим, что

$$
\bigcup_{A\in\tilde\Omega}A=\mathbb R^n\setminus\bigcap_{k=1}^{m}\overline{V_{\varepsilon_k}(a)}\subset\mathbb R^n\setminus V(a).
$$

Но $x^{k_\ell}\to a$, то есть при достаточно больших $\ell$ имеем $x^{k_\ell}\in E\cap V(a)$. Значит, $\tilde\Omega$ не покрывает $E$, что противоречит компактности $E$. Следовательно, $a\in E$.

$$
\bigcup_{A\in\tilde\Omega}A=\mathbb R^n\setminus\bigcap_{k=1}^{m}\overline{V_{\varepsilon_k}(a)}\subset\mathbb R^n\setminus V(a)
$$

## Рукописная страница (стр. PDF 20) — Доказательство теоремы 5.3.5: 3) ⇒ 2)

Проверим замкнутость $E$. Пусть $\{x^k\}$ — последовательность, $x^k\in E$, $x^k\to a\in\mathbb R^n$. По условию 3) $\exists\{x^{k_\ell}\}$ такая, что $x^{k_\ell}\to b$, $b\in E$. Но так как $\{x^{k_\ell}\}$ — подпоследовательность $\{x^k\}$, то $a=b\in E$; значит, $E$ замкнуто.

Проверим ограниченность $E$. Пусть $E$ не ограничено; тогда $\forall k\in\mathbb N$ $\exists x^k\in E$: $\|x^k\|\ge k$. Последовательность $\{x^k\}$ такова, что $x^k\to\infty$. Но тогда для любой подпоследовательности $\{x^{k_\ell}\}$ имеем $x^{k_\ell}\to\infty$, что противоречит условию 3). Следовательно, $E$ ограничено.

**Редакторское уточнение.** В рукописи обе стрелки к противоречию помечены знаком «$\not\Rightarrow$» (перечёркнутая стрелка); в тексте они переданы словами «что противоречит».

## Рукописная страница (стр. PDF 21) — Доказательство теоремы 5.3.5: 2) ⇒ 1)

Пусть $E$ замкнуто и ограничено в $\mathbb R^n$. Из ограниченности следует, что $\exists c>0$:

$$
E\subset[-c,c]\times[-c,c]\times\ldots\times[-c,c]=[-c,c]^n,
$$

то есть $E$ лежит в замкнутом кубе в $\mathbb R^n$. Куб $[-c,c]^n$ компактен в $\mathbb R^n$, а $E$ — замкнутое подмножество $[-c,c]^n$; по замечанию 1 множество $E$ компактно.

$$
E\subset[-c,c]\times[-c,c]\times\ldots\times[-c,c]=[-c,c]^n
$$

> **Редакторское примечание.** В рукописи включение записано знаком равенства: «$E=[-c,c]^n$». Для произвольного ограниченного $E$ это неверно; по смыслу строки речь идёт о включении $E\subset[-c,c]^n$, которое и используется в доказательстве. Рукописное равенство сохранено в описании как расхождение и здесь не тиражируется.

## Печатный слайд 11 (стр. PDF 22) — §4. Предел отображения нескольких переменных

Рассматриваются отображения вида

$$
f:E\subset\mathbb R^n\to\mathbb R^m,\qquad m,n\in\mathbb N.
$$

Такие отображения называются отображениями нескольких переменных. Если $m=1$, то $f$ называется функцией нескольких переменных. Если $n=1$, то $f$ называется вектор-функцией.

Рукописные пометки: $f:E\subset\mathbb R^n\to\mathbb R$ и $f:E\subset\mathbb R^n\to\mathbb R^m$.

$$
f:E\subset\mathbb R^n\to\mathbb R^m,\qquad m,n\in\mathbb N
$$

## Печатный слайд 12 (стр. PDF 23) — Предел отображения по Коши

**Определение 5.4.1.** Пусть $E\subset\mathbb R^n$, $f:E\to\mathbb R^m$, точка $a\in\mathbb R^n$ является предельной для $E$, $A\in\mathbb R^m$. Будем говорить, что $\lim_{x\to a}f(x)=A$ (или $f(x)\to A$ при $x\to a$) в смысле Коши, если

$$
\forall\varepsilon>0\ \ \exists\delta>0\ \ \forall x\in\dot B_\delta(a)\cap E:\ \ f(x)\in B_\varepsilon(A).
$$

**Замечание.** Если $a\in\mathbb R^n$ и $A\in\mathbb R^m$, то соотношение $\lim_{x\to a}f(x)=A$ означает, что

$$
\forall\varepsilon>0\ \ \exists\delta>0\ \ \forall x\in E:\ \ 0<\|x-a\|<\delta\ \Rightarrow\ \|f(x)-A\|<\varepsilon,
$$

а при $a=\infty$ и $A=\infty$ оно эквивалентно

$$
\forall\varepsilon>0\ \ \exists\delta>0\ \ \forall x\in E:\ \ \|x\|>\delta\ \Rightarrow\ \|f(x)\|>\varepsilon.
$$

> **Опечатка в источнике.** В основном определении напечатано $f(x)\in B_\varepsilon(a)$, хотя образом служит точка $A\in\mathbb R^m$; по изображению страницы и по смыслу должно быть $f(x)\in B_\varepsilon(A)$. В изложении используется $B_\varepsilon(A)$, опечатка отмечена здесь.

## Печатный слайд 13 (стр. PDF 24) — Предел отображения по Гейне

**Определение 5.4.2.** Пусть $E\subset\mathbb R^n$, $f:E\to\mathbb R^m$, точка $a\in\mathbb R^n$ является предельной для $E$, $A\in\mathbb R^m$. Будем говорить, что $\lim_{x\to a}f(x)=A$ (или $f(x)\to A$ при $x\to a$) в смысле Гейне, если для любой последовательности $\{x^k\}_{k=1}^{\infty}\subset E\setminus\{a\}$, стремящейся к $a$, выполняется условие

$$
\lim_{k\to\infty}f(x^k)=A.
$$

## Печатный слайд 14 (стр. PDF 25) — Эквивалентность двух определений предела

**Теорема 5.4.1.** Пусть $E\subset\mathbb R^n$, $f:E\to\mathbb R^m$, точка $a\in\mathbb R^n$ является предельной для $E$, $A\in\mathbb R^m$. Тогда равносильны следующие утверждения. 1) $\lim_{x\to a}f(x)=A$ в смысле Коши. 2) $\lim_{x\to a}f(x)=A$ в смысле Гейне.

## Рукописная страница (стр. PDF 26) — Доказательство теоремы 5.4.1: 1) ⇒ 2)

Пусть $\lim_{x\to a}f(x)=A$ в смысле Коши. Возьмём $\{x^k\}_{k=1}^{\infty}$ в $E\setminus\{a\}$, стремящуюся к $a$. Покажем, что $f(x^k)\to A$ при $k\to\infty$.

В силу 1) имеем утверждение ❋:

$$
\forall\varepsilon>0\ \ \exists\delta>0:\ \ \forall x\in\dot V_\delta(a)\cap E\ \ f(x)\in V_\varepsilon(A).
$$

Так как $x^k\to a$, то $\exists N\in\mathbb N$ такое, что $\forall k>N$

$$
x^k\in V_\delta(a).
$$

Кроме того, $x^k\in E\setminus\{a\}$. Итак,

$$
\left.\begin{aligned} x^k&\in V_\delta(a)\\ x^k&\in E\setminus\{a\}\end{aligned}\right\}\Longrightarrow x^k\in\dot V_\delta(a)\cap E.
$$

![Доказательство эквивалентности определений предела (стр. PDF 26)](../../assets/lectures-2025-26/lec57-58-p26-cauchy-heine-proof.jpg)

## Рукописная страница (стр. PDF 27) — Окончание 1) ⇒ 2) и начало 2) ⇒ 1)

Поэтому в силу ❋ имеем

$$
f(x^k)\in V_\varepsilon(A)\qquad\forall k>N.
$$

Таким образом, $f(x^k)\to A$ при $k\to\infty$, то есть $\lim_{x\to a}f(x)=A$ и в смысле Гейне.

Теперь пусть $\lim_{x\to a}f(x)=A$ в смысле Гейне. Докажем, что предел $f$ по Коши также существует и равен $A$. Предположим противное, то есть утверждение ❋❋:

$$
\exists\varepsilon>0\ \ \forall\delta>0\ \ \exists x\in\dot V_\delta(a)\cap E:\ \ f(x)\notin V_\varepsilon(A).
$$

Положим

$$
F:=\{x\in E\setminus\{a\}:\ f(x)\notin V_\varepsilon(A)\}.
$$

Условие ❋❋ означает, что $\dot V_\delta(a)\cap F\ne\varnothing$ при $\forall\delta>0$, то есть $a$ — предельная точка $F$.

$$
F:=\{x\in E\setminus\{a\}:\ f(x)\notin V_\varepsilon(A)\}
$$

## Рукописная страница (стр. PDF 28) — Окончание 2) ⇒ 1)

По теореме 5.2.6 $\exists\{x^k\}_{k=1}^{\infty}\subset F$ (и, значит, в $E\setminus\{a\}$), стремящаяся к $a$. Тогда по определению 5.4.2 имеем

$$
\lim_{k\to\infty}f(x^k)=A,
$$

что невозможно, так как $f(x^k)\notin V_\varepsilon(A)$ при $\forall k\in\mathbb N$. Полученное противоречие завершает доказательство.

$$
\lim_{k\to\infty}f(x^k)=A,\qquad f(x^k)\notin V_\varepsilon(A)
$$

## Печатный слайд 15 (стр. PDF 29) — Единственность предела; предел и покоординатный предел

**Следствие.** Если $A,B\in\mathbb R^m$, $f(x)\to A$ и $f(x)\to B$ при $x\to a$, то $A=B$.

**Следствие.** Пусть в условиях теоремы 5.4.1 $A\in\mathbb R^m$. Тогда равносильны следующие утверждения. 1) $\lim_{x\to a}f(x)=A$. 2) $\forall i\in\{1,\ldots,m\}$ верно равенство $\lim_{x\to a}f_i(x)=A_i$.

## Рукописная страница (стр. PDF 30) — Доказательства следствий

**Следствие 1.** Пусть $\{x^k\}_{k=1}^{\infty}$ — последовательность в $E\setminus\{a\}$ такая, что $x^k\to a$ при $k\to\infty$. Тогда

$$
\left.\begin{aligned} \lim_{k\to\infty}f(x^k)&=A\\ \lim_{k\to\infty}f(x^k)&=B\end{aligned}\right\}\Longrightarrow A=B
$$

в силу единственности предела последовательности.

**Следствие 2.** Пусть $\{x^k\}_{k=1}^{\infty}$ — последовательность в $E\setminus\{a\}$ такая, что $x^k\to a$ при $k\to\infty$. Для $f:E\subset\mathbb R^n\to\mathbb R^m$ запишем вектор и его образ по координатам:

$$
x=\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix},\qquad f(x)=\begin{pmatrix}f_1(x)\\f_2(x)\\\vdots\\f_m(x)\end{pmatrix},\qquad A=\begin{pmatrix}A_1\\A_2\\\vdots\\A_m\end{pmatrix}.
$$

## Рукописная страница (стр. PDF 31) — Окончание следствия 2 и пример

Утверждение 1) означает, что $\lim_{k\to\infty}f(x^k)=A$; утверждение 2) означает, что $\lim_{k\to\infty}f_i(x^k)=A_i$. Равносильность следует из определения и свойств пределов последовательностей в $\mathbb R^n$.

**Пример.** Пусть

$$
f(x,y)=\frac{xy}{x^2+y^2},\qquad (x,y)\in\mathbb R^2\setminus\{(0,0)\}.
$$

Отображение $f$ не имеет предела в точке $(0,0)$. Действительно, положим

$$
z^k=\left(\frac1k,0\right),\qquad \omega^k=\left(\frac1k,\frac1k\right),\qquad k\in\mathbb N.
$$

Тогда $z^k\to(0,0)$ и $\omega^k\to(0,0)$ при $k\to\infty$, но

$$
f(z^k)=0\to0,
$$

$$
f(\omega^k)=\frac{\frac1{k^2}}{\frac2{k^2}}=\frac12\to\frac12,
$$

то есть пределы вдоль разных последовательностей различны. На рисунке справа от текста показаны две траектории приближения к началу координат: точки $z^k$ лежат на оси $Ox$ (зелёные), точки $\omega^k$ — на прямой $y=x$ (красные).

![Контрпример: разные пределы вдоль разных путей (стр. PDF 31)](../../assets/lectures-2025-26/lec57-58-p31-limit-counterexample.jpg)

## Печатный слайд 16 (стр. PDF 32) — Предел и арифметические операции

**Теорема 5.4.2.** Пусть $E\subset\mathbb R^n$, $a\in\mathbb R^n$ — предельная точка для $E$, $f,g:E\to\mathbb R^m$. Предположим, что $f$, $g$ имеют в точке $a$ пределы $A$, $B\in\mathbb R^m$ соответственно. Тогда справедливы следующие утверждения. 1) $\lim_{x\to a}(f(x)+g(x))=A+B$. 2) Если $\lambda:E\to\mathbb R$, $\alpha\in\mathbb R$, $\lim_{x\to a}\lambda(x)=\alpha$, то $\lim_{x\to a}\lambda(x)f(x)=\alpha A$. 3) $\lim_{x\to a}f(x)\cdot g(x)=A\cdot B$. 4) Если $m=1$ и $B\ne0$, то $\lim_{x\to a}\frac{f(x)}{g(x)}=\frac AB$.

$$
\lim_{x\to a}(f(x)+g(x))=A+B
$$

$$
\lim_{x\to a}\lambda(x)f(x)=\alpha A
$$

$$
\lim_{x\to a}f(x)\cdot g(x)=A\cdot B,\qquad \lim_{x\to a}\frac{f(x)}{g(x)}=\frac AB
$$

## Печатный слайд 17 (стр. PDF 33) — Предел композиции

**Теорема 5.4.3.** Пусть $E\subset\mathbb R^n$, $F\subset\mathbb R^m$, $a\in\mathbb R^n$ и $b\in F$ — предельные точки $E$ и $F$ соответственно. Если $f:E\to F$, $g:F\to\mathbb R^s$, $\lim_{x\to a}f(x)=b$, $\lim_{x\to b}g(x)=g(b)$, то

$$
\lim_{x\to a}(g\circ f)(x)=g(b).
$$

## Рукописная страница (стр. PDF 34) — Доказательство теоремы 5.4.3

Пусть $\varepsilon>0$. Тогда выполнено утверждение ▲:

$$
\exists\delta>0\ \text{такое, что}\ g(y)\in V_\varepsilon(g(b))\ \ \forall y\in V_\delta(b)\cap F.
$$

Действительно, для $y\ne b$ это включение вытекает из определения предела $g$ ($\lim_{y\to b}g(y)=g(b)$), а при $y=b$ оно очевидно. Подберём теперь такое $\delta>0$, что

$$
f(x)\in V_\delta(b)\qquad\forall x\in\dot V_\delta(a)\cap E;
$$

это можно сделать, так как $\lim_{x\to a}f(x)=b$. Подставляя в ▲ $y=f(x)$, получим

$$
g(f(x))\in V_\varepsilon(g(b))\qquad\forall x\in\dot V_\delta(a)\cap E.
$$

Таким образом,

$$
\lim_{x\to a}(g\circ f)(x)=g(b).
$$

$$
g(f(x))\in V_\varepsilon(g(b))\qquad\forall x\in\dot V_\delta(a)\cap E
$$

> **Обозначения рукописи.** В последней выкладке для окрестности аргумента и для радиуса из определения предела $g$ использована одна и та же буква $\delta$; в рукописи это совпадение букв не оговаривается. Формула приведена так, как написана на доске.

## Печатный слайд 18 (стр. PDF 35) — Критерий Больцано–Коши для отображений

**Теорема 5.4.4.** Пусть $E\subset\mathbb R^n$, $a\in\mathbb R^n$ — предельная точка для $E$, $f:E\to\mathbb R^m$. Тогда равносильны следующие утверждения. 1) Отображение $f$ имеет предел в $\mathbb R^m$. 2) $\forall\varepsilon>0$ $\exists V(a)$: $\forall x,y\in\dot V(a)\cap E$ выполнено $\|f(x)-f(y)\|<\varepsilon$.

**Замечание.** Утверждение 2) называется сходимостью $f$ в себе в точке $a$.

$$
\forall\varepsilon>0\ \ \exists V(a)\ \ \forall x,y\in\dot V(a)\cap E:\ \ \|f(x)-f(y)\|<\varepsilon
$$

## Рукописная страница (стр. PDF 36) — Доказательство теоремы 5.4.4: 1) ⇒ 2) и начало 2) ⇒ 1)

Пусть $\lim_{x\to a}f(x)=A$. Тогда $\forall\varepsilon>0$ $\exists V(a)$ такая, что

$$
\|f(x)-A\|<\frac{\varepsilon}{2}\qquad\forall x\in\dot V(a)\cap E.
$$

Тогда для всех $x,y\in\dot V(a)\cap E$

$$
\|f(x)-f(y)\|=\|f(x)-A+A-f(y)\|\le\|f(x)-A\|+\|f(y)-A\|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon.
$$

Обратно, пусть $\forall\varepsilon>0$ $\exists V(a)$ такая, что

$$
\forall x,y\in\dot V(a)\cap E\qquad\|f(x)-f(y)\|<\varepsilon.
$$

Пусть $\{x^k\}_{k=1}^{\infty}$ — последовательность в $E\setminus\{a\}$ такая, что $x^k\to a$ при $k\to\infty$. Тогда $\exists N\in\mathbb N$: $\forall k>N$ имеем $x^k\in V(a)$ и $\|f(x^k)-f(x^m)\|<\varepsilon$ для всех $k,m>N$.

$$
\|f(x)-f(y)\|=\|f(x)-A+A-f(y)\|\le\|f(x)-A\|+\|f(y)-A\|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon
$$

## Рукописная страница (стр. PDF 37) — Окончание доказательства теоремы 5.4.4

Значит, последовательность $\{f(x^k)\}$ сходится в себе, поэтому $\{f(x^k)\}$ имеет предел в $\mathbb R^m$, и, следовательно, отображение $f$ имеет предел в точке $a$.

$$
\{f(x^k)\}\ \text{сходится в себе}\ \Longrightarrow\ \{f(x^k)\}\ \text{имеет предел в}\ \mathbb R^m
$$

---

[Индекс лекций](index.md) · [English](../../en/lectures-2025-26/lecture-57-58.md) · [Español](../../es/lectures-2025-26/lecture-57-58.md) · [Назад: 55–56](lecture-55-56.md) · [Далее: 59–60](lecture-59-60.md)

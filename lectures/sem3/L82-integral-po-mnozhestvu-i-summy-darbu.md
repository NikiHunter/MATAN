---
semester: 3
lecture: 82
topic: "Интеграл по множеству, суммы Дарбу, мера Жордана, общие свойства интеграла"
source_pages: [p078, p079, p080, p081, p082]
lang: ru
status: draft
---

# Лекция 82 — Интеграл по множеству, суммы Дарбу, мера Жордана, общие свойства интеграла

> [!info] Происхождение текста
> Текст переписан со страниц `p078`–`p082` рукописной тетради
> (см. [`ocr/raw/`](../../ocr/raw), [`ocr/MANIFEST.md`](../../ocr/MANIFEST.md)).
> В тетради этот материал помечен как «Лекции 81–82»: пара лекций не разделена.
> Разбиение на отдельные файлы проведено по границе тем; текст не переставлялся и не дополнялся.
> Решений в `My decision` (`ocr/ISSUES.md`) нет, поэтому все пометки остаются `open`
> и продублированы предупреждениями. Ничего не добавлено: ни доказательств,
> ни примеров, ни «пропущенных шагов».

## p078

### Интеграл по мн-ву

### Опр (10.2.1)

Мн-во $\Omega\subset\mathbb{R}^n$ наз. допустимым, если оно огр. в $\mathbb{R}^n$
и его граница $\partial\Omega$ есть мн-во меры нуль

### Опр (10.2.2)

Пусть $\Omega\subset\mathbb{R}^n$ — допустимое мн-во. Ф-я
$\chi_\Omega(x)=\begin{cases}1,\ \text{если }x\in\Omega\\0,\ \text{если }x\notin\Omega\end{cases}$
наз. характеристической ф-ей мн-ва $\Omega$.

### Замечание

$\chi_\Omega(x)$ имеет разрыв только на $\partial\Omega\Rightarrow$

$\Rightarrow$ Если $\Omega$ — допустимое мн-во ⇒ $\mu(\partial\Omega)=0\Rightarrow$

$\Rightarrow\chi_\Omega$ непрер. почти всюду в $\mathbb{R}^n$ ⟦S402⟧

### Интеграл по мн-ву

$\Omega=\mathbb{R}^n$, $f:\Omega\to\mathbb{R}$

### Опр (10.2.3) // допис. ⟦U403⟧

Ф-я $f$ определена на мн-ве $\Omega$. Тогда. ⟦U404⟧

### Опр (10.2.4) // допис. ⟦U405⟧

### Замечание

$\exists\Omega\subset I_1$, $\Omega\subset I_2$ ⟦S406⟧

> [!warning] Неразрешённые пометки страницы p078 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S402: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U403: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U404: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U405: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S406: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p079

### Интегральные суммы Дарбу

Пусть $f$ — вещественнозначная ф-я на промежутке $I$, а
$P=\{I_i\}$ — разбиение промежутка $I$.
Положим $m_i:=\inf\limits_{x\in I_i}f(x)$, $M_i=\sup\limits_{x\in I_i}f(x)$ ⟦A407⟧

### Опр (10.1.9) // допис. ⟦U408⟧

Величина $s(f,P)=\sum m_i\mu(I_i)$, $S(f,P)$ ⟦U409⟧

> [!note] На полях
> [рисунок: объёмный столбик над ячейкой разбиения, подпись $f(\xi_i)$, $I_i$] ⟦G410⟧

![](../../ocr/crops/p079_fig1.jpg)

### Нижний и верхний интегралы Дарбу

### Опр (10.1.10) // допис ⟦U411⟧

### Упражнение. Прямоугольники $I$ имеют следующее св-во: // допис ⟦U412⟧

$s$

Замечание: $\sup\inf\le\inf\sup$

### Крит Дарбу интегрируемости вещественнозначной ф-ции

### Теорема (10.1.13) ф-ла ⟦A413⟧

$f\in R(I)\Leftrightarrow\underline{J}=\overline{J}$ ⟦U414⟧

> [!warning] Неразрешённые пометки страницы p079 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> A407: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> U408: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U409: нечитаемо (illegible), см. `ocr/ISSUES.md`
> G410: нетривиальный рисунок (non-obvious figure), см. `ocr/ISSUES.md`
> U411: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U412: нечитаемо (illegible), см. `ocr/ISSUES.md`
> A413: неоднозначный символ (ambiguous symbol), см. `ocr/ISSUES.md`
> U414: нечитаемо (illegible), см. `ocr/ISSUES.md`

## p080

### Д-во (т. 10.2.1):

Т. разрыва ф-ции $f\chi_\Omega$ в $\Omega$ ⟦U415⟧

$\sum$. разрыв $f\chi_\Omega$ в $\Omega$ или $\partial\Omega$. ⟦S416⟧

### Мера (объём) допустимого мн-ва

### Опр (10.2.5)

Мерой (Жордана) или объёмом ограниченного мн-ва $\Omega\subset\mathbb{R}^n$ наз.
величина $\mu(\Omega):=\int_I1\,dx$, если указанный интеграл (Римана) сущ. ⟦S417⟧

### Опр (10.2.6)

Мн-во $\Omega\subset\mathbb{R}^n$ назов. мн-вом меры нуль в смысле Жордана
или мн-вом объёма нуль, если $\forall\varepsilon>0$ его можно покрыть такой
конечной системой прямоугольников $I_1,\ldots,I_k$, что
$\sum\limits_{i=1}^k\mu(I_i)<\varepsilon$ ⟦S418⟧

### Замечание:

$\int_I1\,dx=\int_{I\ni\Omega}\chi_\Omega(x)\,dx$

Поскольку т. разрыва $\chi_\Omega$ лежат на $\partial\Omega\Rightarrow\mu(\Omega)$
определена только для допустимых мн-в ⟦S419⟧

### Замечание:

Только допустимые мн-ва явл. измеримыми!

> [!note] На полях
> [в овале, внизу] в смысле меры нуль Лебега или Жордана до информации ⟦U420⟧

> [!warning] Неразрешённые пометки страницы p080 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U415: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S416: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S417: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S418: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S419: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U420: нечитаемо (illegible), см. `ocr/ISSUES.md`

## p081

Упоминание типа характеристической ф-ции $\int_{I_1}f\chi_\Omega\,dx$ ⟦U421⟧

$\int_{I_1}f\chi_\Omega\,dx$, $\int_{I_2}f\chi_\Omega\,dx$ — Эти интегралы $\sum$ одновременно

Причём если они сущ., то их значения совпадают.

Рассм. $I_1\cap I_2\supset\Omega$

Про можно сказать о разрыве $\chi_\Omega$ ⟦U422⟧

① т. разрыва $f$ вне $\Omega$ ⟦S423⟧
② т. разрыва $\chi_\Omega$

Это всегда т. разрыва $\chi_\Omega\in I_1\cap I_2$ ⟦M424⟧

$\int_{I_1\cap I_2}f\chi_\Omega$, $\int_{I_1}f\chi_\Omega$, $\int_{I_2}f\chi_\Omega$
— три интеграла $\sum$ одновременно.

> [!note] На полях
> [рисунок: два перекрывающихся прямоугольника $I_1$, $I_2$, внутри $\Omega$, заштриховано пересечение] ⟦G425⟧

Интегралы $\sum$

Исключим рассм. только те разбиения $I_1$, $I_2$, кот. получаются
дополнением разбиения $I_1\cap I_2$ ⟦S426⟧

Заметим, что вне $I_1\cap I_2$ ∨ $\chi_\Omega=0\Rightarrow$ Интегральные суммы
для $I_1$ и $I_2$ Это одна и та же интегральная сумма для $I_1\cap I_2$ ⟦T427⟧

$\sum f\chi_\Omega(\xi_i)\mu(I_{1i})=\sum f\chi_\Omega(\xi_i)\mu(I_1\cap I_{2i})$

$\sum f\chi_\Omega(\eta_i)\mu(I_{2i})=\sum f\chi_\Omega(\eta_i)\mu(I_{1i}\cap I_{2i})$

Переходя к пределу с разбиением интегралов ⟦S428⟧

### Крит. интегрируемости по мн-ву

### Теорема (10.2.1) // допис ⟦U429⟧

$\forall_\exists f:\Omega\to\mathbb{R}$ интегрируема на допустимом мн-ве ⟦U430⟧

> [!warning] Неразрешённые пометки страницы p081 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U421: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U422: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S423: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> M424: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> G425: нетривиальный рисунок (non-obvious figure), см. `ocr/ISSUES.md`
> S426: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> T427: возможная описка в конспекте (probable typo in the notes), см. `ocr/ISSUES.md`
> S428: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U429: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U430: нечитаемо (illegible), см. `ocr/ISSUES.md`

## p082

### Общие св-ва интеграла

### Теорема (10.3.1)

Пусть $\Omega_1,\Omega_2$ — допустимые мн-ва в $\mathbb{R}^n$, $f$ — ф-я,
определённая на $\Omega_1\cup\Omega_2$. Тогда:

① $\int_{\Omega_1\cup\Omega_2}f(x)\,dx\Leftrightarrow\exists\int_{\Omega_i}f(x)\,dx,\ i=1,2\Rightarrow\exists\int_{\Omega_1\cap\Omega_2}f(x)\,dx$

② Если при $\mu(\Omega_1\cap\Omega_2)=0$, dopри усл. сущ. интегралов имеет
место рав-во: $\int_{\Omega_1\cup\Omega_2}f(x)\,dx=\int_{\Omega_1}f(x)\,dx+\int_{\Omega_2}f(x)\,dx$ ⟦U431⟧

### Д-во (п ① т. 10.3.1):

$\mu(\Omega_1\cap\Omega_2)=0$

$\int_{\Omega_1\cup\Omega_2}f(x)\,dx=\int_{I\supset\Omega_1\cup\Omega_2}f\chi_{\Omega_1\cup\Omega_2}\,dx$

Запишем, что $\chi_{\Omega_1\cup\Omega_2}(x)=\chi_{\Omega_1}(x)+\chi_{\Omega_2}(x)-\chi_{\Omega_1\cap\Omega_2}(x)$

① $\int f\chi_{\Omega_1}(x)\,dx+\int f\chi_{\Omega_2}(x)\,dx-\int f\chi_{\Omega_1\cap\Omega_2}(x)\,dx$

⇔ $\int_{\Omega_1}f\,dx$ ⇔ $\int_{\Omega_2}f\,dx$ − Φ т.к. $\mu(\Omega_1\cap\Omega_2)=0$ ⇔ $0$ ⟦S432⟧

### Оценка интеграла

### Утв (10.3.1)

Если $f\in R(\Omega)$, то $|f|\in R(\Omega)$ и имеет место нер-во:
$\left|\int_\Omega f(x)\,dx\right|\le\int_\Omega|f(x)|\,dx$

### Д-во (утв. 10.3.1):

$|f|\in R(\Omega)\Leftarrow$ опр интеграла по $\Omega$ + крит. Лебега

Переходный переход из нер-ва для интегральных сумм. → ⟦U433⟧

2) чер-во ⟦U434⟧

> [!warning] Неразрешённые пометки страницы p082 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U431: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S432: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U433: нечитаемо (illegible), см. `ocr/ISSUES.md`
> U434: нечитаемо (illegible), см. `ocr/ISSUES.md`

---

Source: pages p078–p082

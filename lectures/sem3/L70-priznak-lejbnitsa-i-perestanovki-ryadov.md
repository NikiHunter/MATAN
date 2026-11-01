---
semester: 3
lecture: 70
topic: "Ряды с членами произвольного знака, признак Лейбница, перестановки рядов"
source_pages: [p027, p028, p029]
lang: ru
status: draft
---

# Лекция 70 — Ряды с членами произвольного знака, признак Лейбница, перестановки рядов

> [!info] Происхождение текста
> Текст переписан со страниц `p027`–`p029` рукописной тетради
> (см. [`ocr/raw/`](../../ocr/raw), [`ocr/MANIFEST.md`](../../ocr/MANIFEST.md)).
> В тетради этот материал помечен как «Лекции 69–70»: пара лекций не разделена.
> Разбиение на отдельные файлы L69 и L70 проведено по границе p029/p030 (смена темы); текст не переставлялся и не дополнялся.
> Решений в `My decision` (`ocr/ISSUES.md`) нет, поэтому все пометки остаются `open`
> и продублированы предупреждениями. Ничего не добавлено: ни доказательств,
> ни примеров, ни «пропущенных шагов».

## p027

Рассм. теперь ряд с произвольными членами $\sum\limits_{n=0}^{\infty}(-1)^nc_n$, $c_n\ge0$. Чаще такие ряды наз. **_знакочередующимися_**.

**Признак Лейбница** ($c_n>0\ \forall n$)

$\exists c_n\downarrow0$, т.е. $c_{n+1}\le c_n\ \forall n$ и $c_n\xrightarrow[n\to\infty]{}0$. Тогда ряд $\sum\limits_{n=0}^{\infty}(-1)^nc_n$ сх-ся.

Рассм. остаток ряда $R_n:=\sum\limits_{k=n+1}^{\infty}(-1)^kc_k$. Для ряда Лейбница справедлива ф-ла $|R_n|\le c_{n+1}$. ⟦S111⟧

**Пример:** $1-1/2+1/3-1/4+\ldots+\dfrac{(-1)^{n+1}}{n}+\ldots=\sum\limits_{n=1}^{\infty}\dfrac{(-1)^{n+1}}{n}=\ln 2$.

### Д-во (пр. Лейбница):

Рассм. $S_{2m+1}=\sum\limits_{n=0}^{2m+1}(-1)^nc_n$; $S_{2m+1}-S_{2m-1}=\sum\limits_{n=0}^{2m+1}(-1)^nc_n-\sum\limits_{n=0}^{2m-1}(-1)^nc_n=c_{2m}-c_{2m+1}\ge0$ ⟦M112⟧

$S_{2m+1}=c_0-c_1+c_2-c_3+\ldots+c_{2m}-c_{2m+1}=c_0+(c_2-c_1)+(c_4-c_3)+\ldots+(c_{2m}-c_{2m+1})\le c_0$
> [!note] На полях
> [под скобками $(c_2-c_1)$, $(c_4-c_3)$, $\ldots$, $(c_{2m}-c_{2m+1})$] $\le0$; $\le0$; $\le0$
> [!note] На полях
> [справа от строки] т.к. $c_{n+1}\le c_n$ ⟦S113⟧

### Замечание 1

$S_{2m+1}=(c_0-c_1)+(c_2-c_3)+\ldots+(c_{2m}-c_{2m+1})\ge0$
> [!note] На полях
> [под скобками] $\ge0$; $\ge0$; $\ge0$

С другой стороны, $S_{2m+1}\le c_0\Rightarrow0\le S_{2m+1}\le c_0$
> [!note] На полях
> [стрелки вниз от $S_{2m+1}$ и от $c_0$] $m\to\infty$; $\downarrow$; $\downarrow$
> [!note] На полях
> [справа внизу] $0\le S\le c_0$
> [!note] На полях
> [внизу справа] по т. опред. монот. посл-ти переход в нер-ве ⟦S114⟧

### Замечание 2 ⟦S115⟧

$R_n=\sum\limits_{k=n+1}^{\infty}(-1)^kc_k$

> [!warning] Неразрешённые пометки страницы p027 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S111: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> M112: математическое несоответствие (mathematical inconsistency), см. `ocr/ISSUES.md`
> S113: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S114: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S115: неясная структура (unclear structure), см. `ocr/ISSUES.md`

## p028

$|R_n|=|S-S_n|=|(-1)^{n+1}(S-S_n)|\le c_{n+1}$ ⟦S116⟧

### Пример:

$\sum\limits_{k=1}^{\infty}\dfrac{(-1)^{k-1}}{k}=1-1/2+1/3-1/4+\ldots$

$S_{2n}=1-1/2+\ldots+\dfrac{1}{2n-1}-\dfrac{1}{2n}=1+1/2+1/3+\ldots+\dfrac{1}{2n-1}+\dfrac{1}{2n}-2\left(1/2+1/4+\ldots+\dfrac{1}{2n}\right)$
$-1/2=1/2-2\cdot1/2$
$-1/4=1/4-2\cdot1/4$ ⟦S117⟧

Положим $H_n=1+\dfrac{1}{2}+\ldots+\dfrac{1}{n}$
$H_{2n}=1+\dfrac{1}{2}+\ldots+\dfrac{1}{2n-1}+\dfrac{1}{2n}$

❶ $H_{2n}-H_n$

Формула Эйлера-Маклорена асимптотических сумм: $H_n=\ln n+C_0+\delta_n$, где $\delta_n\to0$. ⟦U118⟧

> [!warning] Неразрешённые пометки страницы p028 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> S116: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S117: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> U118: нечитаемо (illegible), см. `ocr/ISSUES.md`

## p029

По усл. $(a_n)$ - огр. и монотонна.

Пусть (для определенности) огр. снизу и монот. $\downarrow$
$a_1>a_2>a_3>\ldots>a_n>\ldots\ge$ ограничена снизу ⟦U119⟧
$\Rightarrow\exists$ конечный предел $\lim\limits_{n\to\infty}a_n=a$

$\alpha_n:=a_n-a\Rightarrow\alpha_n\downarrow0$

$\sum\limits_{n=1}^{\infty}a_nb_n=\sum\limits_{n=1}^{\infty}(\alpha_n+a)b_n=\sum\limits_{n=1}^{\infty}\alpha_nb_n+a\sum\limits_{n=1}^{\infty}b_n$ - сх-ся
> [!note] На полях
> [под первым слагаемым, со стрелкой] сх-ся по пр. Дирихле
> [!note] На полях
> [под вторым слагаемым, со стрелкой] сх-ся по усл. ⟦S120⟧

$\\blacksquare$

### Перестановки рядов

### Опр (7.5.1)

Пусть имеется ряд $\sum\limits_{n=1}^{\infty}a_n$ и биективное отображение $\sigma:\mathbb{N}\to\mathbb{N}$. Ряд $\sum\limits_{n=1}^{\infty}a_{\sigma(n)}$ наз. **_перестановкой_** исходного ряда $\sum\limits_{n=1}^{\infty}a_n$. ⟦S121⟧

### Переместительное св-во ряда

### Опр (7.5.2)

Будем говорить, что ряд $\sum\limits_{n=1}^{\infty}a_n$ обладает **_переместительным св-вом_**, если $\forall$ биекции $\sigma:\mathbb{N}\to\mathbb{N}$ ряд $\sum\limits_{n=1}^{\infty}a_{\sigma(n)}$ сх-ся и расх-ся одновременно с исходным рядом, и при этом $\sum\limits_{n=1}^{\infty}a_n=\sum\limits_{n=1}^{\infty}a_{\sigma(n)}$. ⟦S122⟧

> [!warning] Неразрешённые пометки страницы p029 (см. [`ocr/ISSUES.md`](../../ocr/ISSUES.md))
> U119: нечитаемо (illegible), см. `ocr/ISSUES.md`
> S120: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S121: неясная структура (unclear structure), см. `ocr/ISSUES.md`
> S122: неясная структура (unclear structure), см. `ocr/ISSUES.md`

---

Source: pages p027–p029

"""Terminology and theorem registry used for automatic cross-linking.

Each entry names one concept, the place in the 21-chapter course where it is
explained (``"NN#anchor"``; the same anchor exists in all three languages),
optionally the numbered statement of the 2025/26 lectures that states it
(``lec``), and the phrases that mention it in each language.

Phrases are case-insensitive regular expressions matched on whole words.
An en dash in a phrase also matches a hyphen.  Russian and Spanish phrases
spell out the inflected endings explicitly (``\\w*`` after a stem).

To add a term: append a ``T(...)`` line, then run
``python3 scripts/build_views.py`` and check the report for terms that were
never matched.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Term:
    id: str
    target: str  # "NN#anchor" inside {lang}/NN-*.md
    en: tuple[str, ...]
    ru: tuple[str, ...]
    es: tuple[str, ...]
    lec: str | None = None  # anchor of the lecture statement, e.g. "thm-2-3-4"
    kind: str = "term"  # "term" or "theorem"
    chapters: tuple[int, int] | None = None  # restrict linking to these chapters
    labels: dict = field(default_factory=dict, compare=False)

    def phrases(self, lang: str) -> tuple[str, ...]:
        return getattr(self, lang)


def T(id, target, en, ru, es, **kw):
    as_tuple = lambda v: (v,) if isinstance(v, str) else tuple(v)
    return Term(id, target, as_tuple(en), as_tuple(ru), as_tuple(es), **kw)


def TH(id, target, en, ru, es, **kw):
    return T(id, target, en, ru, es, kind="theorem", **kw)


# Anchors of the labelled blockquote statements in each chapter, in order
# (the "Goal" blockquote that opens every chapter is skipped).  The three
# language editions are structurally parallel, so position fixes the anchor.
CHAPTER_STATEMENTS = {
    1: [("example-induction", "example"), ("cantor-theorem", "theorem")],
    2: [("completeness-axiom", "axiom"), ("archimedean-property", "theorem"),
        ("density-of-rationals", "theorem"), ("nested-interval-theorem", "theorem")],
    3: [("monotone-convergence-theorem", "theorem"), ("bolzano-weierstrass-theorem", "theorem")],
    4: [("alternating-series-test", "theorem"), ("rearrangement-warning", "warning")],
    5: [("intermediate-value-theorem", "theorem"), ("extreme-value-theorem", "theorem"),
        ("heine-cantor-theorem", "theorem")],
    6: [("chain-rule", "theorem"), ("fermat-theorem", "theorem"), ("darboux-property", "theorem")],
    7: [("rolle-theorem", "theorem"), ("lagrange-mean-value-theorem", "theorem"),
        ("cauchy-mean-value-theorem", "theorem"), ("jensen-inequality", "theorem")],
    8: [("integrability-criterion", "theorem"), ("mean-value-theorem-for-integrals", "theorem"),
        ("ftc-first-part", "theorem"), ("newton-leibniz-formula", "theorem")],
    9: [("dirichlet-test-for-integrals", "theorem")],
    10: [("weierstrass-m-test", "theorem"), ("uniform-limit-continuity", "theorem"),
         ("uniform-limit-integration", "theorem")],
    11: [("abel-theorem", "theorem")],
    12: [("dirichlet-pointwise-theorem", "theorem")],
    13: [("heine-borel-theorem", "theorem"), ("baire-category-theorem", "theorem")],
    14: [("iterated-limit-warning", "warning")],
    15: [("clairaut-schwarz-theorem", "theorem")],
    16: [("inverse-function-theorem", "theorem")],
    17: [("fubini-theorem-continuous", "theorem")],
    18: [("green-theorem", "theorem"), ("stokes-theorem", "theorem"), ("divergence-theorem", "theorem")],
    19: [],
    20: [("lebesgue-monotone-convergence-theorem", "theorem"), ("fatou-lemma", "lemma"),
         ("dominated-convergence-theorem", "theorem")],
    21: [("holder-inequality", "theorem"), ("riesz-fischer-theorem", "theorem")],
}

LEBESGUE = (19, 21)
BEFORE_LEBESGUE = (0, 18)

TERMS: list[Term] = [
    # 1. Logic, sets, functions
    T("quantifier", "01#sec-1-1", r"quantifiers?", r"квантор\w*", r"cuantificador(?:es)?"),
    T("mathematical-induction", "01#example-induction", r"(?:mathematical )?induction",
      r"(?:математическ\w* )?индукци\w*", r"inducción(?: matemática)?"),
    T("injective", "01#sec-1-4", (r"injective", r"injections?"), (r"инъективн\w*", r"инъекци\w*"),
      (r"inyectiv[ao]s?", r"inyecci(?:ón|ones)"), lec="def-1-1-4"),
    T("surjective", "01#sec-1-4", (r"surjective", r"surjections?"), (r"сюръективн\w*", r"сюръекци\w*"),
      (r"sobreyectiv[ao]s?", r"suprayectiv[ao]s?", r"sobreyecci(?:ón|ones)"), lec="def-1-1-5"),
    T("bijective", "01#sec-1-4", (r"bijective", r"bijections?"), (r"биективн\w*", r"биекци\w*"),
      (r"biyectiv[ao]s?", r"biyecci(?:ón|ones)"), lec="def-1-1-6"),
    T("inverse-map", "01#sec-1-4", (r"inverse (?:map|function)s?",), (r"обратн\w* (?:отображени|функци)\w*",),
      (r"(?:aplicaci|funci)(?:ón|ones) inversas?",), lec="def-1-1-8", chapters=(0, 15)),
    T("equinumerous", "01#sec-1-5", (r"equinumer\w+", r"equipotent"), (r"равномощн\w*",),
      (r"equipotentes?", r"equipotencia"), lec="def-1-2-1"),
    T("countable-set", "01#sec-1-5", (r"countable sets?", r"countably infinite", r"countable"),
      (r"счётн\w*", r"счетн\w*"), (r"numerables?",), lec="def-1-2-5"),
    T("uncountable", "01#sec-1-5", r"uncountable", (r"несчётн\w*", r"несчетн\w*"), r"no numerables?",
      lec="thm-1-2-5"),
    TH("cantor-theorem", "01#cantor-theorem", (r"Cantor's theorem",), (r"теорем\w* Кантора о мощности",),
       (r"teorema de Cantor",), chapters=(0, 2)),

    # 2. Real numbers
    T("ordered-field", "02#sec-2-1", r"ordered fields?", r"упорядоченн\w* пол\w*", r"cuerpos? ordenados?"),
    T("upper-bound", "02#sec-2-2", (r"upper bounds?", r"lower bounds?"), (r"верхн\w* границ\w*", r"нижн\w* границ\w*"),
      (r"cotas? superior(?:es)?", r"cotas? inferior(?:es)?")),
    T("bounded-set", "02#sec-2-2", (r"bounded (?:above|below)",), (r"ограничен\w* (?:сверху|снизу)",),
      (r"acotad[ao]s? (?:superior|inferior)mente",), lec="def-1-3-7"),
    T("supremum", "02#sec-2-2", (r"suprem(?:um|a)", r"least upper bound"), (r"супремум\w*", r"точн\w* верхн\w* гран\w*"),
      (r"suprem(?:o|os)",), lec="def-2-3-1"),
    T("infimum", "02#sec-2-2", (r"infim(?:um|a)", r"greatest lower bound"), (r"инфимум\w*", r"точн\w* нижн\w* гран\w*"),
      (r"ínfim(?:o|os)",), lec="def-2-3-2"),
    TH("completeness-axiom", "02#completeness-axiom",
       (r"completeness axiom", r"axiom of completeness", r"least-upper-bound property"),
       (r"аксиом\w* полноты", r"аксиом\w* непрерывности"), (r"axioma de (?:completitud|continuidad|supremo)",)),
    TH("archimedean-property", "02#archimedean-property", (r"Archimedean (?:property|axiom)",),
       (r"архимедовост\w*", r"аксиом\w* Архимеда", r"принцип\w* Архимеда"),
       (r"propiedad arquimediana", r"axioma de Arquímedes"), lec="def-1-3-5"),
    TH("density-of-rationals", "02#density-of-rationals", (r"density of (?:the )?rationals",),
       (r"плотност\w* рациональных чисел",), (r"densidad de los racionales",), lec="thm-1-3-3"),
    TH("nested-interval-theorem", "02#nested-interval-theorem",
       (r"nested[- ]intervals? (?:theorem|principle|lemma|property)", r"Cantor's (?:nested-interval )?principle"),
       (r"(?:теорем|лемм|принцип)\w* о вложенных отрезках", r"вложенн\w* отрезк\w*"),
       (r"(?:teorema|principio) de (?:los )?intervalos encajados", r"intervalos encajados"), lec="thm-2-3-1"),
    T("extended-real-line", "02#sec-2-4", (r"extended real line",), (r"расширенн\w* числов\w* прям\w*",),
      (r"recta real (?:ampliada|extendida)",), lec="def-1-3-4"),

    # 3. Sequences
    T("limit-of-sequence", "03#sec-3-1", (r"limits? of (?:a|the) sequence", r"limit of a numerical sequence"),
      (r"предел\w* (?:числов\w* )?последовательност\w*",), (r"límites? de (?:una|la) sucesión",), lec="def-2-1-2"),
    T("convergent-sequence", "03#sec-3-1", (r"convergent sequences?",), (r"сходящ\w* последовательност\w*",),
      (r"sucesi(?:ón|ones) convergentes?",), lec="def-2-1-3"),
    T("neighbourhood", "03#sec-3-1", (r"ε-neighbou?rhoods?", r"epsilon-neighbou?rhoods?"),
      (r"ε-окрестност\w*", r"эпсилон-окрестност\w*"), (r"ε-entornos?", r"ε-vecindad(?:es)?"), lec="def-2-1-4"),
    TH("squeeze-theorem", "03#sec-3-2", (r"squeeze (?:theorem|principle|lemma)", r"sandwich (?:theorem|principle|lemma)",
                                          r"two policemen"),
       (r"теорем\w* о (?:двух милиционерах|двух полицейских|сжатой переменной|трёх последовательностях)",
        r"принцип\w* двусторонней оценки"),
       (r"teorema del (?:sándwich|emparedado|encaje)", r"criterio del (?:sándwich|encaje)"), lec="thm-2-1-4"),
    T("infinitesimal", "03#sec-3-2", (r"infinitesimals?",), (r"бесконечно мал\w*",), (r"infinitesimal(?:es)?",),
      lec="def-2-2-1"),
    T("infinitely-large", "03#sec-3-2", (r"infinitely large",), (r"бесконечно больш\w*",), (r"infinitamente grandes?",),
      lec="def-2-2-4"),
    TH("monotone-convergence-sequences", "03#monotone-convergence-theorem",
       (r"monotone convergence theorem", r"Weierstrass(?:'s)? theorem on monotone sequences"),
       (r"теорем\w* Вейерштрасса о монотонн\w* последовательност\w*", r"теорем\w* о монотонн\w* последовательност\w*"),
       (r"teorema de (?:la )?convergencia monótona",), chapters=BEFORE_LEBESGUE, lec="thm-2-3-3"),
    T("monotone-sequence", "03#sec-3-3", (r"monotone sequences?", r"increasing sequences?", r"decreasing sequences?"),
      (r"монотонн\w* последовательност\w*", r"возрастающ\w* последовательност\w*", r"убывающ\w* последовательност\w*"),
      (r"sucesi(?:ón|ones) monótonas?", r"sucesi(?:ón|ones) crecientes?", r"sucesi(?:ón|ones) decrecientes?"),
      lec="def-2-3-5"),
    T("subsequence", "03#sec-3-4", (r"subsequences?",), (r"подпоследовательност\w*",), (r"subsucesi(?:ón|ones)",),
      lec="def-2-3-7"),
    T("partial-limit", "03#sec-3-5", (r"partial limits?", r"subsequential limits?", r"limit points? of (?:a|the) sequence"),
      (r"частичн\w* предел\w*",), (r"límites? parcial(?:es)?",), lec="def-2-3-8"),
    TH("bolzano-weierstrass", "03#bolzano-weierstrass-theorem",
       (r"Bolzano–Weierstrass(?: (?:theorem|principle|selection principle|lemma|property))?",),
       (r"(?:теорем|принцип|лемм)\w* Больцано–Вейерштрасса", r"Больцано–Вейерштрасса"),
       (r"(?:teorema|principio) de Bolzano–Weierstrass", r"Bolzano–Weierstrass"), lec="thm-2-3-4"),
    T("cauchy-sequence", "03#sec-3-4", (r"Cauchy sequences?", r"fundamental sequences?", r"converges? in itself",
                                        r"Cauchy condition"),
      (r"фундаментальн\w* последовательност\w*", r"последовательност\w* Коши", r"сходящ\w*ся в себе",
       r"условие Коши"),
      (r"sucesi(?:ón|ones) de Cauchy", r"sucesi(?:ón|ones) fundamental(?:es)?", r"condición de Cauchy"),
      lec="def-2-3-10"),
    TH("cauchy-criterion-sequences", "03#sec-3-4",
       (r"Cauchy criterion(?: for (?:the convergence of )?sequences)?", r"Bolzano–Cauchy criterion"),
       (r"критери\w* Коши(?! равномерн)", r"критери\w* Больцано–Коши"),
       (r"criterio de Cauchy(?! uniforme)", r"criterio de Bolzano–Cauchy"), lec="thm-2-3-7", chapters=(0, 9)),
    T("limsup", "03#sec-3-5", (r"upper and lower limits", r"limits? superior and inferior",
                               r"limits? superior", r"limits? inferior", r"upper limits?", r"lower limits?",
                               r"lim ?sup", r"lim ?inf"),
      (r"верхн\w* и нижн\w* предел\w*", r"верхн\w* предел\w*", r"нижн\w* предел\w*"),
      (r"límites? superior(?:es)? e inferior(?:es)?", r"límites? superior(?:es)?", r"límites? inferior(?:es)?"),
      lec="def-2-3-9"),

    # 4. Numeric series
    T("series", "04#sec-4-1", (r"partial sums?", r"numerical series", r"number series"),
      (r"частичн\w* сумм\w*", r"числов\w* ряд\w*"), (r"sumas? parcial(?:es)?", r"series? numéricas?")),
    T("comparison-test", "04#sec-4-2", (r"comparison tests?", r"limit comparison"),
      (r"признак\w* сравнения",), (r"criterios? de comparación",), chapters=(0, 8)),
    T("ratio-test", "04#sec-4-2", (r"ratio test", r"d'Alembert(?:'s)? test", r"root test", r"Cauchy's root test"),
      (r"признак\w* Даламбера", r"радикальн\w* признак\w*", r"признак\w* Коши(?! для)"),
      (r"criterio (?:del cociente|de d'Alembert|de la raíz|de Cauchy de la raíz)",)),
    T("absolute-convergence", "04#sec-4-3", (r"absolute(?:ly)? converge\w*", r"absolute convergence"),
      (r"абсолютн\w* сходи\w*", r"абсолютно сход\w*"), (r"convergencia absoluta", r"absolutamente convergentes?",
                                                        r"converge absolutamente"), chapters=(0, 12)),
    T("conditional-convergence", "04#sec-4-3", (r"conditional(?:ly)? converge\w*",),
      (r"условн\w* сходи\w*", r"условно сход\w*"), (r"convergencia condicional", r"condicionalmente convergentes?",
                                                    r"converge condicionalmente")),
    TH("alternating-series-test", "04#alternating-series-test", (r"alternating[- ]series test", r"Leibniz(?:'s)? (?:test|criterion)"),
       (r"признак\w* Лейбница",), (r"criterio de Leibniz",)),
    TH("riemann-rearrangement", "04#rearrangement-warning", (r"Riemann(?:'s)? rearrangement theorem", r"rearrangements?"),
       (r"теорем\w* Римана о перестановке", r"перестановк\w* (?:член\w* )?ряд\w*"),
       (r"teorema de reordenación de Riemann", r"reordenaci(?:ón|ones)")),

    # 5. Limits and continuity
    T("limit-point", "05#sec-5-1", (r"limit points?", r"accumulation points?", r"cluster points?"),
      (r"предельн\w* точк\w*",), (r"puntos? de acumulación", r"puntos? límite"), lec="def-2-4-1", chapters=(0, 12)),
    T("punctured-neighbourhood", "05#sec-5-1", (r"punctured neighbou?rhoods?", r"deleted neighbou?rhoods?"),
      (r"проколот\w* окрестност\w*",), (r"entornos? perforados?", r"entornos? reducidos?"), lec="def-2-4-2"),
    T("limit-of-function", "05#sec-5-1", (r"limits? of (?:a|the) function", r"Cauchy definition of the limit",
                                          r"Heine definition"),
      (r"предел\w* функци\w*", r"определени\w* (?:предела )?по (?:Коши|Гейне)"),
      (r"límites? de (?:una|la) función", r"definición de (?:Cauchy|Heine)"), lec="def-2-4-4", chapters=(0, 12)),
    TH("sequential-criterion", "05#sec-5-1", (r"sequential criterion", r"Heine(?:'s)? criterion"),
       (r"критери\w* Гейне", r"языке последовательностей"), (r"criterio (?:secuencial|de Heine)",), lec="thm-2-4-1"),
    T("one-sided-limit", "05#sec-5-1", (r"one-sided limits?",), (r"односторонн\w* предел\w*",),
      (r"límites? laterales?",), lec="def-2-4-5"),
    T("asymptotic-notation", "05#sec-5-2", (r"asymptotically equivalent", r"little-o", r"big-O", r"o-small"),
      (r"эквивалентн\w* (?:бесконечно мал|функци)\w*", r"о-малое", r"о-большое"),
      (r"asintóticamente equivalentes?", r"o pequeña", r"O grande")),
    T("continuity", "05#sec-5-3", (r"continuous at (?:a|the) point", r"continuity at a point"),
      (r"непрерывн\w* в точке", r"непрерывност\w* в точке"), (r"continu[ao]s? en (?:un|el) punto", r"continuidad en un punto"),
      lec="def-2-5-1"),
    T("discontinuity", "05#sec-5-3", (r"removable discontinuit\w+", r"jump discontinuit\w+", r"points? of discontinuity",
                                      r"discontinuities of the (?:first|second) kind"),
      (r"устраним\w* разрыв\w*", r"разрыв\w* (?:первого|второго) рода", r"точк\w* разрыва"),
      (r"discontinuidad(?:es)? (?:evitables?|de salto|de (?:primera|segunda) especie)", r"puntos? de discontinuidad"),
      lec="def-2-5-4"),
    TH("intermediate-value-theorem", "05#intermediate-value-theorem",
       (r"intermediate[- ]value (?:theorem|property)", r"Bolzano–Cauchy (?:theorem|intermediate)"),
       (r"теорем\w* (?:Больцано–Коши )?о промежуточн\w* значени\w*", r"теорем\w* Больцано–Коши"),
       (r"teorema (?:del valor intermedio|de Bolzano(?:–Cauchy)?)", r"valores? intermedios?"), lec="thm-2-5-5"),
    TH("extreme-value-theorem", "05#extreme-value-theorem",
       (r"extreme[- ]value theorem", r"Weierstrass(?:'s)? (?:extreme[- ]value )?theorem(?! on monotone)"),
       (r"теорем\w* Вейерштрасса о (?:наибольшем|ограниченности|достижении)\w*", r"теорем\w* о наибольшем и наименьшем"),
       (r"teorema (?:de los valores extremos|de Weierstrass)",), chapters=(0, 18)),
    T("uniform-continuity", "05#sec-5-4", (r"uniform(?:ly)? continu\w+",), (r"равномерн\w* непрерывн\w*",),
      (r"continuidad uniforme", r"uniformemente continu[ao]s?"), lec="def-2-5-7"),
    TH("heine-cantor-theorem", "05#heine-cantor-theorem", (r"Heine–Cantor(?: theorem)?", r"Cantor's theorem on uniform continuity"),
       (r"теорем\w* Кантора о равномерн\w* непрерывност\w*", r"теорем\w* Гейне–Кантора"),
       (r"teorema de Heine–Cantor", r"Heine–Cantor"), lec="thm-2-5-4"),
    T("asymptote", "05#sec-5-2", (r"asymptotes?",), (r"асимптот(?:а|ы|е|у|ой|ам|ами|ах)?",), (r"asíntotas?",), lec="thm-2-6-2",
      chapters=(0, 9)),

    # 6. Derivatives
    T("derivative", "06#sec-6-1", (r"derivatives?(?! (?:along|in the direction))",), (r"производн\w*",), (r"derivadas?",),
      lec="def-3-1-1", chapters=(0, 12)),
    T("differentiable", "06#sec-6-1", (r"differentiab\w+",), (r"дифференцируем\w*",), (r"derivables?", r"diferenciables?"),
      lec="def-3-2-1", chapters=(0, 12)),
    T("one-sided-derivative", "06#sec-6-1", (r"one-sided derivatives?", r"left derivatives?", r"right derivatives?"),
      (r"односторонн\w* производн\w*", r"(?:левая|правая|левой|правой|левую|правую) производн\w*"),
      (r"derivadas? laterales?",)),
    T("differential", "06#sec-6-3", (r"differentials?(?! equation)",), (r"дифференциал\w*(?! уравнен)",),
      (r"diferencial(?:es)?(?! ecuaci)",), lec="def-3-3-1", chapters=(0, 12)),
    TH("chain-rule", "06#chain-rule", (r"chain rule", r"derivative of (?:a|the) composition"),
       (r"правил\w* цепочки", r"производн\w* композиции", r"производн\w* сложной функции"),
       (r"regla de la cadena", r"derivada de (?:una|la) composición"), chapters=(0, 12), lec="thm-3-3-1"),
    T("inverse-function-derivative", "06#sec-6-2", (r"derivative of (?:the|an) inverse function",),
      (r"производн\w* обратн\w* функци\w*",), (r"derivada de la función inversa",), lec="thm-3-3-2"),
    T("local-extremum", "06#sec-6-4", (r"local (?:extrem(?:um|a)|maxim(?:um|a)|minim(?:um|a))",),
      (r"локальн\w* (?:экстремум|максимум|минимум)\w*",), (r"(?:extremos?|máximos?|mínimos?) locales?",),
      lec="def-3-7-1", chapters=(0, 13)),
    TH("fermat-theorem", "06#fermat-theorem", (r"Fermat's theorem", r"Fermat theorem"), (r"теорем\w* Ферма",),
       (r"teorema de Fermat",), lec="thm-3-4-1"),
    TH("darboux-property", "06#darboux-property", (r"Darboux(?:'s)? (?:property|theorem)",),
       (r"свойств\w* Дарбу", r"теорем\w* Дарбу"), (r"(?:propiedad|teorema) de Darboux",), lec="thm-3-7-6"),

    # 7. Mean values, Taylor, convexity
    TH("rolle-theorem", "07#rolle-theorem", (r"Rolle's theorem", r"Rolle theorem"), (r"теорем\w* Ролля",),
       (r"teorema de Rolle",), lec="thm-3-4-2"),
    TH("lagrange-mvt", "07#lagrange-mean-value-theorem",
       (r"Lagrange's (?:mean value )?theorem", r"Lagrange mean value theorem", r"Lagrange formula",
        r"formula of finite increments", r"finite-increment formula", r"mean value theorem(?! for integrals)"),
       (r"теорем\w* Лагранжа(?! о множ)", r"формул\w* Лагранжа", r"формул\w* конечных приращений"),
       (r"teorema de Lagrange", r"teorema del valor medio(?! integral| para integrales)", r"fórmula de los incrementos finitos"),
       lec="thm-3-4-3", chapters=(0, 14)),
    TH("cauchy-mvt", "07#cauchy-mean-value-theorem", (r"Cauchy's mean value theorem", r"Cauchy mean value theorem",
                                                    r"generalized mean value theorem"),
       (r"теорем\w* Коши о среднем", r"теорем\w* Коши о конечных приращениях", r"обобщённ\w* формул\w* конечных приращений"),
       (r"teorema del valor medio de Cauchy", r"teorema de Cauchy del valor medio"), lec="thm-3-4-4"),
    TH("lhopital-rule", "07#sec-7-2", (r"L'Hôpital's rule", r"L'Hospital's rule", r"L'Hôpital rule"),
       (r"правил\w* Лопиталя",), (r"regla de L'Hôpital", r"regla de L'Hospital"), lec="thm-3-4-5"),
    T("taylor-formula", "07#sec-7-3", (r"Taylor(?:'s)? (?:formula|polynomials?|expansions?|theorem)",
                                       r"Peano (?:form|remainder)", r"Lagrange (?:form|remainder)"),
      (r"формул\w* Тейлора", r"многочлен\w* Тейлора", r"остаточн\w* член\w*(?! ряда)", r"форм\w* Пеано"),
      (r"fórmula de Taylor", r"polinomios? de Taylor", r"restos? de (?:Peano|Lagrange)", r"término complementario"),
      lec="thm-3-6-3", chapters=(0, 14)),
    T("maclaurin", "07#sec-7-3", (r"Maclaurin(?:'s)? (?:formula|series|expansion)",), (r"формул\w* Маклорена", r"ряд\w* Маклорена"),
      (r"fórmula de Maclaurin", r"series? de Maclaurin")),
    T("convex-function", "07#sec-7-4", (r"convex functions?", r"concave functions?", r"convexity", r"concavity"),
      (r"выпукл\w* функци\w*", r"вогнут\w* функци\w*", r"выпуклост\w*", r"вогнутост\w*"),
      (r"funci(?:ón|ones) convexas?", r"funci(?:ón|ones) cóncavas?", r"convexidad", r"concavidad"), lec="def-3-8-1"),
    T("inflection-point", "07#sec-7-4", (r"inflection points?", r"points? of inflection"), (r"точк\w* перегиба",),
      (r"puntos? de inflexión",), lec="def-3-8-3"),
    TH("jensen-inequality", "07#jensen-inequality", (r"Jensen's inequality", r"Jensen inequality"), (r"неравенств\w* Йенсена",),
       (r"desigualdad de Jensen",), lec="thm-4-4-4"),

    # 8. Riemann integration
    T("antiderivative", "08#sec-8-3", (r"antiderivatives?", r"primitives?", r"indefinite integrals?"),
      (r"первообразн\w*", r"неопределённ\w* интеграл\w*", r"неопределенн\w* интеграл\w*"),
      (r"primitivas?", r"antiderivadas?", r"integral(?:es)? indefinidas?"), lec="def-4-1-1"),
    T("partition", "08#sec-8-1", (r"partitions?", r"mesh of (?:a|the) partition"), (r"разбиени\w*", r"ранг\w* разбиения"),
      (r"particiones", r"partición", r"diámetro de (?:la|una) partición"), lec="def-4-2-2", chapters=(0, 17)),
    T("darboux-sums", "08#sec-8-1", (r"(?:upper|lower) (?:Darboux )?sums?", r"Darboux sums?", r"Darboux integrals?"),
      (r"(?:верхн|нижн)\w* (?:сумм|интеграл)\w* Дарбу", r"сумм\w* Дарбу", r"интеграл\w* Дарбу"),
      (r"sumas? (?:superior(?:es)?|inferior(?:es)?) de Darboux", r"sumas? de Darboux", r"integral(?:es)? de Darboux"),
      lec="def-4-2-8"),
    TH("integrability-criterion", "08#integrability-criterion",
       (r"integrability criterion", r"Riemann(?:'s)? criterion", r"Darboux criterion"),
       (r"критери\w* интегрируемост\w*", r"критери\w* Римана", r"критери\w* Дарбу"),
       (r"criterio de integrabilidad", r"criterio de Riemann", r"criterio de Darboux"), lec="thm-4-2-1"),
    T("riemann-sum", "08#sec-8-2", (r"Riemann sums?", r"integral sums?", r"tagged partitions?"),
      (r"интегральн\w* сумм\w*", r"сумм\w* Римана", r"оснащени\w*"),
      (r"sumas? de Riemann", r"sumas? integral(?:es)?", r"particiones? marcadas?"), lec="def-4-2-4"),
    T("riemann-integral", "08#sec-8-2", (r"Riemann[- ]integra\w+", r"definite integrals?"),
      (r"интеграл\w* Римана", r"интегрируем\w* по Риману", r"определённ\w* интеграл\w*", r"определенн\w* интеграл\w*"),
      (r"integral(?:es)? de Riemann", r"integrables? (?:según|en el sentido de) Riemann", r"integral(?:es)? definidas?"),
      lec="def-4-2-6"),
    T("oscillation", "08#sec-8-1", (r"oscillations? of (?:a|the) function", r"oscillation"), (r"колебани\w*",),
      (r"oscilaci(?:ón|ones)",), lec="def-4-2-9", chapters=(0, 17)),
    T("measure-zero-riemann", "08#sec-8-2", (r"(?:Lebesgue )?measure zero", r"null sets?", r"sets? of measure zero"),
      (r"мер\w* нуль", r"мер\w* ноль", r"множеств\w* меры (?:нуль|ноль)", r"лебеговой меры нуль"),
      (r"medida (?:nula|cero)", r"conjuntos? nulos?"), lec="def-4-2-11", chapters=(0, 18)),
    TH("lebesgue-criterion-riemann", "08#sec-8-2", (r"Lebesgue(?:'s)? criterion",), (r"критери\w* Лебега",),
       (r"criterio de Lebesgue",), lec="thm-4-2-5"),
    TH("mean-value-integrals", "08#mean-value-theorem-for-integrals",
       (r"mean value theorems? for integrals", r"integral mean value theorem", r"first mean value theorem",
        r"second mean value theorem", r"Bonnet(?:'s)? (?:formula|theorem)"),
       (r"(?:первая|вторая|первой|второй) теорем\w* о среднем", r"теорем\w* о среднем для интеграл\w*",
        r"формул\w* Бонне", r"теорем\w* Бонне"),
       (r"teorema del valor medio (?:integral|para integrales)", r"(?:primer|segundo) teorema del valor medio",
        r"fórmula de Bonnet", r"teorema de Bonnet"), lec="thm-4-3-1"),
    TH("ftc", "08#sec-8-3", (r"fundamental theorem of (?:calculus|analysis)", r"integral with a variable upper limit"),
       (r"основн\w* теорем\w* (?:анализа|интегрального исчисления)", r"интеграл\w* с переменным верхним пределом"),
       (r"teorema fundamental del cálculo", r"integral con límite superior variable"), lec="thm-4-3-2"),
    TH("newton-leibniz", "08#newton-leibniz-formula", (r"Newton–Leibniz(?: formula)?",), (r"формул\w* Ньютона–Лейбница",),
       (r"(?:fórmula|regla) de Newton–Leibniz", r"Newton–Leibniz"), lec="thm-4-3-2"),
    T("integration-by-parts", "08#sec-8-4", (r"integration by parts", r"integrat\w+ by parts"),
      (r"интегрировани\w* по частям", r"формул\w* интегрирования по частям"), (r"integración por partes",),
      lec="thm-4-1-4"),
    T("substitution", "08#sec-8-4", (r"change of variables? in (?:the|an|definite) integrals?", r"substitution rule",
                                     r"integration by substitution"),
      (r"замен\w* переменн\w* в (?:определённом |неопределённом )?интеграл\w*",),
      (r"cambio de variable en (?:la|una) integral", r"integración por sustitución"),
      lec="thm-4-1-5", chapters=(0, 12)),
    TH("cauchy-schwarz-integral", "21#sec-21-4", (r"Cauchy–Schwarz(?:–Bunyakovsky)?(?: inequality)?", r"Cauchy–Bunyakovsky"),
       (r"неравенств\w* Коши–Буняковского(?:–Шварца)?", r"Коши–Буняковского", r"Коши–Шварца"),
       (r"desigualdad de Cauchy–Schwarz(?:–Bunyakovski)?", r"Cauchy–Schwarz"), lec="thm-4-4-6"),

    # 9. Improper integrals and applications
    T("improper-integral", "09#sec-9-1", (r"improper integrals?",), (r"несобственн\w* интеграл\w*",),
      (r"integral(?:es)? impropias?",), lec="def-4-5-2"),
    T("principal-value", "09#sec-9-1", (r"(?:Cauchy )?principal values?",), (r"главн\w* значени\w*",),
      (r"valor(?:es)? principal(?:es)?",)),
    T("comparison-test-integrals", "09#sec-9-2", (r"comparison tests? for (?:improper )?integrals",),
      (r"признак\w* сравнения для (?:несобственных )?интеграл\w*",), (r"criterios? de comparación para integrales",),
      lec="thm-4-5-3"),
    T("absolute-convergence-integral", "09#sec-9-2", (r"absolutely convergent integrals?", r"absolute convergence of (?:the|an) integral"),
      (r"абсолютн\w* сходи\w* интеграл\w*",), (r"integral(?:es)? absolutamente convergentes?",), lec="def-4-5-4"),
    TH("dirichlet-abel-integrals", "09#dirichlet-test-for-integrals",
       (r"Dirichlet(?:'s)? test(?: for integrals)?", r"Abel(?:'s)? test(?: for integrals)?", r"Dirichlet–Abel tests?"),
       (r"признак\w* Дирихле", r"признак\w* Абеля", r"признак\w* Абеля–Дирихле"),
       (r"criterio de Dirichlet", r"criterio de Abel", r"criterios de Abel–Dirichlet"), lec="thm-4-5-4"),
    T("arc-length", "09#sec-9-3", (r"arc lengths?", r"lengths? of (?:a|the) (?:curve|path)", r"rectifiable"),
      (r"длин\w* (?:дуги|кривой|пути)", r"спрямляем\w*"), (r"longitud(?:es)? de (?:arco|una curva|la curva|un camino)",
                                                       r"rectificables?"), lec="thm-4-7-1"),
    T("path", "09#sec-9-3", (r"smooth paths?", r"parametri[sz]ed curves?"), (r"гладк\w* пут\w*", r"параметризованн\w* крив\w*"),
      (r"caminos? suaves?", r"curvas? parametrizadas?"), lec="def-4-6-1"),

    # 10. Function sequences and series
    T("pointwise-convergence", "10#sec-10-1", (r"pointwise converge\w*", r"converges? pointwise"),
      (r"поточечн\w* сходи\w*", r"сходи\w* поточечно"), (r"convergencia puntual", r"converge puntualmente")),
    T("uniform-convergence", "10#sec-10-1", (r"uniform(?:ly)? converge\w*", r"converges? uniformly", r"uniform limits?"),
      (r"равномерн\w* сходи\w*", r"сходи\w* равномерно", r"равномерн\w* предел\w*"),
      (r"convergencia uniforme", r"converge uniformemente", r"uniformemente convergentes?", r"límites? uniformes?")),
    TH("uniform-cauchy-criterion", "10#sec-10-2", (r"uniform Cauchy criterion", r"Cauchy criterion for uniform convergence"),
       (r"равномерн\w* критери\w* Коши", r"критери\w* Коши равномерн\w* сходимости"),
       (r"criterio uniforme de Cauchy", r"criterio de Cauchy uniforme")),
    TH("weierstrass-m-test", "10#weierstrass-m-test", (r"Weierstrass M-test", r"M-test", r"Weierstrass test"),
       (r"признак\w* Вейерштрасса",), (r"criterio M de Weierstrass", r"criterio de Weierstrass", r"prueba M")),
    TH("uniform-limit-continuity", "10#uniform-limit-continuity", (r"uniform limit of continuous functions",),
       (r"равномерн\w* предел\w* непрерывн\w* функций",), (r"límite uniforme de funciones continuas",)),

    # 11. Power series
    T("power-series", "11#sec-11-1", (r"power series",), (r"степенн\w* ряд\w*",), (r"series? de potencias",)),
    T("radius-of-convergence", "11#sec-11-1", (r"radi(?:us|i) of convergence", r"Cauchy–Hadamard(?: formula)?",
                                               r"intervals? of convergence"),
      (r"радиус\w* сходимости", r"формул\w* Коши–Адамара", r"интервал\w* сходимости"),
      (r"radios? de convergencia", r"fórmula de Cauchy–Hadamard", r"intervalos? de convergencia")),
    TH("abel-theorem", "11#abel-theorem", (r"Abel's theorem", r"Abel theorem"), (r"теорем\w* Абеля",), (r"teorema de Abel",)),
    T("analytic-function", "11#sec-11-4", (r"analytic functions?", r"real-analytic"),
      (r"аналитическ\w* функци\w*",), (r"funci(?:ón|ones) analíticas?",)),
    T("taylor-series", "11#sec-11-3", (r"Taylor series",), (r"ряд\w* Тейлора",), (r"series? de Taylor",)),

    # 12. Fourier series
    T("fourier-series", "12#sec-12-1", (r"Fourier series", r"Fourier coefficients?", r"trigonometric system"),
      (r"ряд\w* Фурье", r"коэффициент\w* Фурье", r"тригонометрическ\w* систем\w*"),
      (r"series? de Fourier", r"coeficientes? de Fourier", r"sistema trigonométrico")),
    TH("dirichlet-pointwise", "12#dirichlet-pointwise-theorem", (r"Dirichlet's (?:pointwise )?theorem", r"Dirichlet theorem"),
       (r"теорем\w* Дирихле",), (r"teorema (?:puntual )?de Dirichlet",)),
    TH("parseval", "12#sec-12-4", (r"Parseval's (?:identity|equality|theorem)", r"Parseval identity", r"Bessel's inequality"),
       (r"равенств\w* Парсеваля", r"неравенств\w* Бесселя"), (r"identidad de Parseval", r"igualdad de Parseval",
                                                            r"desigualdad de Bessel")),

    # 13. Metric spaces
    T("metric-space", "13#sec-13-1", (r"metric spaces?", r"metrics?"), (r"метрическ\w* пространств\w*", r"метрик\w*"),
      (r"espacios? métricos?", r"métricas?")),
    T("open-set", "13#sec-13-2", (r"open sets?", r"open balls?"), (r"открыт\w* множеств\w*", r"открыт\w* шар\w*"),
      (r"conjuntos? abiertos?", r"bolas? abiertas?"), lec="def-5-3-1"),
    T("closed-set", "13#sec-13-2", (r"closed sets?",), (r"замкнут\w* множеств\w*",), (r"conjuntos? cerrados?",),
      lec="thm-5-3-1"),
    T("interior", "13#sec-13-2", (r"interior points?", r"interiors? of (?:a|the) set"),
      (r"внутренн\w* точк\w*", r"внутренност\w*"), (r"puntos? interiores?", r"interior de (?:un|el) conjunto"),
      lec="def-5-3-3"),
    T("closure", "13#sec-13-2", (r"closures? of (?:a|the) set", r"closure"), (r"замыкани\w*",), (r"clausuras?", r"adherencias?"),
      lec="def-5-3-2"),
    T("boundary", "13#sec-13-2", (r"boundary points?", r"boundar(?:y|ies) of (?:a|the) set"),
      (r"граничн\w* точк\w*", r"границ\w* множества"), (r"puntos? frontera", r"fronteras? de (?:un|el) conjunto"),
      lec="def-5-3-4"),
    T("complete-space", "13#sec-13-3", (r"complete (?:metric )?spaces?", r"completeness of (?:the )?space"),
      (r"полн\w* (?:метрическ\w* )?пространств\w*",), (r"espacios? (?:métricos? )?completos?",)),
    T("compact", "13#sec-13-4", (r"compact(?:ness)?", r"open covers?", r"finite subcovers?"),
      (r"компакт\w*", r"открыт\w* покрыти\w*", r"конечн\w* подпокрыти\w*"),
      (r"compact[oa]s?", r"compacidad", r"recubrimientos? abiertos?", r"subrecubrimientos? finitos?"), lec="def-5-3-7"),
    TH("heine-borel", "13#heine-borel-theorem", (r"Heine–Borel(?: theorem| lemma)?", r"Borel–Lebesgue lemma"),
       (r"теорем\w* Гейне–Бореля", r"лемм\w* Гейне–Бореля", r"лемм\w* Бореля–Лебега"),
       (r"teorema de Heine–Borel", r"Heine–Borel"), lec="thm-5-3-5"),
    T("connected", "13#sec-13-5", (r"connected(?:ness)?", r"path-connected"), (r"связн\w*", r"линейно связн\w*"),
      (r"conex[oa]s?", r"conexión", r"conexidad"), chapters=(0, 21)),
    TH("baire", "13#baire-category-theorem", (r"Baire(?:'s)? (?:category )?theorem",), (r"теорем\w* Бэра",),
       (r"teorema (?:de categoría )?de Baire",)),

    # 14. Several variables
    T("euclidean-norm", "14#sec-14-1", (r"Euclidean (?:norm|space|distance)",), (r"евклидов\w* (?:норм|пространств|расстояни)\w*",),
      (r"(?:norma|espacio|distancia) euclidian[ao]", r"(?:norma|espacio|distancia) euclíde[ao]"), lec="def-5-1-1"),
    T("norm", "14#sec-14-1", (r"norms?(?! of a partition)", r"normed spaces?"), (r"норм(?:а|ы|е|у|ой|ами|ах|ам)", r"нормированн\w* пространств\w*"),
      (r"normas?", r"espacios? normados?"), chapters=(13, 21)),
    T("iterated-limit", "14#iterated-limit-warning", (r"iterated limits?", r"repeated limits?"),
      (r"повторн\w* предел\w*",), (r"límites? iterados?", r"límites? reiterados?"), lec="def-5-4-2"),

    # 15. Multivariable differentiation
    T("total-derivative", "15#sec-15-1", (r"total derivatives?", r"Fréchet derivatives?", r"differentiable maps?"),
      (r"полн\w* производн\w*", r"дифференцируем\w* отображени\w*"), (r"derivadas? totales?", r"aplicaci(?:ón|ones) diferenciables?"),
      lec="def-6-1-2"),
    T("partial-derivative", "15#sec-15-2", (r"partial derivatives?", r"partials"), (r"частн\w* производн\w*",),
      (r"derivadas? parciales?",), lec="def-6-1-5"),
    T("directional-derivative", "15#sec-15-2", (r"directional derivatives?", r"derivatives? along (?:a|the) vector",
                                                r"derivatives? in the direction"),
      (r"производн\w* по направлени\w*", r"производн\w* по вектор\w*"), (r"derivadas? direccional(?:es)?",
                                                                    r"derivadas? según (?:un|el) vector"),
      lec="def-6-1-4"),
    T("gradient", "15#sec-15-2", (r"gradients?",), (r"градиент\w*",), (r"gradientes?",), lec="def-6-1-6"),
    T("jacobian-matrix", "15#sec-15-1", (r"Jacobian matri(?:x|ces)", r"Jacobi matri(?:x|ces)"), (r"матриц\w* Якоби",),
      (r"matri(?:z|ces) jacobianas?", r"matri(?:z|ces) de Jacobi"), lec="def-6-1-6"),
    T("tangent-plane", "15#sec-15-3", (r"tangent planes?",), (r"касательн\w* плоскост\w*",), (r"planos? tangentes?",)),
    T("hessian", "15#sec-15-4", (r"Hessians?", r"Hessian matri(?:x|ces)"), (r"гессиан\w*", r"матриц\w* Гессе"),
      (r"hessianas?", r"matri(?:z|ces) hessianas?")),
    T("mixed-partials", "15#clairaut-schwarz-theorem", (r"mixed (?:partial )?derivatives?", r"mixed partials"),
      (r"смешанн\w* (?:частн\w* )?производн\w*",), (r"derivadas? (?:parciales )?cruzadas?", r"derivadas? mixtas?"),
      lec="thm-6-4-1"),
    TH("clairaut-schwarz", "15#clairaut-schwarz-theorem", (r"Clairaut–Schwarz(?: theorem)?", r"Schwarz(?:'s)? theorem",
                                                        r"Clairaut's theorem"),
       (r"теорем\w* (?:Клеро–)?Шварца", r"Клеро–Шварца"), (r"teorema de (?:Clairaut–)?Schwarz", r"Clairaut–Schwarz"),
       lec="thm-6-4-1"),
    T("continuously-differentiable", "15#sec-15-1", (r"continuously differentiable", r"C\^1 maps"),
      (r"непрерывно дифференцируем\w*",), (r"continuamente (?:derivables?|diferenciables?)", r"de clase C"),
      lec="thm-6-3-1"),

    # 16. Implicit functions and extrema
    TH("inverse-function-theorem", "16#inverse-function-theorem", (r"inverse function theorem",),
       (r"теорем\w* об обратн\w* (?:функци|отображени)\w*",), (r"teorema de la función inversa",)),
    TH("implicit-function-theorem", "16#sec-16-3", (r"implicit function theorem", r"implicit functions?"),
       (r"теорем\w* о неявн\w* функци\w*", r"неявн\w* функци\w*"), (r"teorema de la función implícita",
                                                                   r"funci(?:ón|ones) implícitas?")),
    T("lagrange-multipliers", "16#sec-16-4", (r"Lagrange multipliers?", r"Lagrangian", r"constrained extrem(?:um|a)",
                                               r"conditional extrem(?:um|a)"),
      (r"множител\w* Лагранжа", r"функци\w* Лагранжа", r"условн\w* экстремум\w*"),
      (r"multiplicadores? de Lagrange", r"lagrangiana", r"extremos? condicionados?")),

    # 17. Multiple integrals
    T("multiple-integral", "17#sec-17-1", (r"multiple integrals?", r"double integrals?", r"triple integrals?",
                                           r"iterated integrals?"),
      (r"кратн\w* интеграл\w*", r"двойн\w* интеграл\w*", r"тройн\w* интеграл\w*", r"повторн\w* интеграл\w*"),
      (r"integral(?:es)? múltiples?", r"integral(?:es)? dobles?", r"integral(?:es)? triples?", r"integral(?:es)? iteradas?")),
    TH("fubini", "17#fubini-theorem-continuous", (r"Fubini's theorem", r"Fubini theorem"), (r"теорем\w* Фубини",),
       (r"teorema de Fubini",), chapters=(0, 18)),
    T("change-of-variables", "17#sec-17-2", (r"change of variables(?! in (?:the|an|definite) integral)",
                                             r"Jacobian determinants?", r"Jacobian"),
      (r"замен\w* переменн\w*(?! в (?:определённом |неопределённом )?интеграл)", r"якобиан\w*"),
      (r"cambio de variables?(?! en (?:la|una) integral)", r"determinantes? jacobianos?", r"jacobianos?"),
      chapters=(14, 21)),
    T("polar-coordinates", "17#sec-17-3", (r"polar coordinates", r"spherical coordinates", r"cylindrical coordinates"),
      (r"полярн\w* координат\w*", r"сферическ\w* координат\w*", r"цилиндрическ\w* координат\w*"),
      (r"coordenadas (?:polares|esféricas|cilíndricas)",)),

    # 18. Vector calculus
    T("line-integral", "18#sec-18-1", (r"line integrals?", r"curvilinear integrals?", r"work integrals?"),
      (r"криволинейн\w* интеграл\w*",), (r"integral(?:es)? de línea", r"integral(?:es)? curvilíneas?")),
    T("conservative-field", "18#sec-18-1", (r"conservative (?:vector )?fields?", r"potential functions?",
                                            r"potential fields?"),
      (r"потенциальн\w* (?:векторн\w* )?пол\w*", r"консервативн\w* пол\w*"),
      (r"campos? (?:vectoriales? )?conservativos?", r"funci(?:ón|ones) potencial(?:es)?")),
    T("surface-integral", "18#sec-18-2", (r"surface integrals?", r"flux"), (r"поверхностн\w* интеграл\w*", r"поток\w*"),
      (r"integral(?:es)? de superficie", r"flujos?"), chapters=(14, 21)),
    T("divergence", "18#sec-18-3", (r"divergence of (?:a|the) (?:vector )?field", r"curl", r"rotor"),
      (r"дивергенци\w*", r"ротор\w*"), (r"divergencia de (?:un|el) campo", r"rotacional(?:es)?")),
    TH("green-theorem", "18#green-theorem", (r"Green's theorem", r"Green theorem", r"Green's formula"),
       (r"теорем\w* Грина", r"формул\w* Грина"), (r"teorema de Green", r"fórmula de Green")),
    TH("stokes-theorem", "18#stokes-theorem", (r"Stokes'? theorem", r"Stokes' formula"),
       (r"теорем\w* Стокса", r"формул\w* Стокса"), (r"teorema de Stokes", r"fórmula de Stokes")),
    TH("divergence-theorem", "18#divergence-theorem", (r"divergence theorem", r"Gauss(?:'s)? theorem",
                                                      r"Gauss–Ostrogradsky(?: theorem| formula)?"),
       (r"теорем\w* о дивергенции", r"формул\w* Гаусса–Остроградского", r"теорем\w* Гаусса–Остроградского"),
       (r"teorema de la divergencia", r"teorema de Gauss", r"fórmula de Gauss–Ostrogradski")),

    # 19. Measure theory
    T("sigma-algebra", "19#sec-19-1", (r"sigma-algebras?", r"σ-algebras?"), (r"сигма-алгебр\w*", r"σ-алгебр\w*"),
      (r"sigma-álgebras?", r"σ-álgebras?")),
    T("measure", "19#sec-19-2", (r"countably additive", r"measure spaces?", r"(?<!Lebesgue )measures?(?! zero)"),
      (r"счётно-аддитивн\w*", r"счетно-аддитивн\w*", r"пространств\w* с мерой", r"мер(?:а|ы|у|ой|ами|ах|ам)(?! нуль| ноль| Лебега)"),
      (r"numerablemente aditiv[ao]s?", r"espacios? de medida", r"medidas?(?! nula| cero| de Lebesgue)"),
      chapters=(19, 21)),
    T("lebesgue-measure", "19#sec-19-3", (r"Lebesgue measures?", r"outer measures?", r"Jordan measures?"),
      (r"мер\w* Лебега", r"лебегов\w* мер\w*", r"внешн\w* мер\w*", r"мер\w* Жордана"),
      (r"medidas? de Lebesgue", r"medidas? exteriores?", r"medidas? de Jordan"), lec="def-4-6-6"),
    T("measurable-function", "19#sec-19-4", (r"measurable (?:functions?|sets?)", r"measurable"),
      (r"измерим\w*",), (r"medibles?",), chapters=(19, 21)),
    T("almost-everywhere", "19#sec-19-4", (r"almost everywhere", r"a\.e\."), (r"почти всюду", r"п\.в\."),
      (r"casi en todas partes", r"c\.t\.p\.", r"en casi todo punto")),
    T("simple-function", "19#sec-19-4", (r"simple functions?",), (r"прост\w* функци\w*",), (r"funci(?:ón|ones) simples?",)),

    # 20. Lebesgue integration
    T("lebesgue-integral", "20#sec-20-1", (r"Lebesgue integra\w+",), (r"интеграл\w* Лебега", r"интегрируем\w* по Лебегу"),
      (r"integral(?:es)? de Lebesgue", r"integrables? (?:según|en el sentido de) Lebesgue")),
    TH("lebesgue-mct", "20#lebesgue-monotone-convergence-theorem",
       (r"monotone convergence theorem", r"Beppo Levi(?:'s)? theorem", r"Levi's theorem"),
       (r"теорем\w* (?:Беппо )?Леви", r"теорем\w* о монотонн\w* сходимост\w*"),
       (r"teorema de (?:la )?convergencia monótona", r"teorema de (?:Beppo )?Levi"), chapters=LEBESGUE),
    TH("fatou", "20#fatou-lemma", (r"Fatou's lemma", r"Fatou lemma"), (r"лемм\w* Фату",), (r"lema de Fatou",)),
    TH("dominated-convergence", "20#dominated-convergence-theorem",
       (r"dominated convergence theorem", r"Lebesgue(?:'s)? dominated convergence", r"dominated convergence"),
       (r"теорем\w* Лебега о мажорированн\w* сходимост\w*", r"мажорированн\w* сходимост\w*"),
       (r"teorema de (?:la )?convergencia dominada", r"convergencia dominada")),
    TH("fubini-tonelli", "20#sec-20-4", (r"Fubini–Tonelli(?: theorem)?", r"Tonelli's theorem", r"product measures?"),
       (r"теорем\w* Фубини–Тонелли", r"Фубини–Тонелли", r"теорем\w* Тонелли", r"произведени\w* мер"),
       (r"teorema de Fubini–Tonelli", r"Fubini–Tonelli", r"teorema de Tonelli", r"medidas? producto")),

    # 21. Lp spaces
    T("lp-space", "21#sec-21-1", (r"L\^?p[ -]spaces?", r"Lebesgue spaces?", r"Banach spaces?"),
      (r"пространств\w* L\^?p", r"банахов\w* пространств\w*"), (r"espacios? L\^?p", r"espacios? de Banach")),
    TH("holder", "21#holder-inequality", (r"Hölder's inequality", r"Hölder inequality"), (r"неравенств\w* Гёльдера", r"неравенств\w* Гельдера"),
       (r"desigualdad de Hölder",), lec="thm-4-4-5"),
    TH("minkowski", "21#sec-21-1", (r"Minkowski's inequality", r"Minkowski inequality"), (r"неравенств\w* Минковского",),
       (r"desigualdad de Minkowski",)),
    T("essential-supremum", "21#sec-21-1", (r"essential supremum", r"ess ?sup"), (r"существенн\w* супремум\w*",),
      (r"supremo esencial",)),
    TH("riesz-fischer", "21#riesz-fischer-theorem", (r"Riesz–Fischer(?: theorem)?",), (r"теорем\w* Рисса–Фишера",),
       (r"teorema de Riesz–Fischer",)),
    T("hilbert-space", "21#sec-21-4", (r"Hilbert spaces?", r"inner products?", r"orthonormal (?:bases|basis|systems?)",
                                       r"orthogonal projections?"),
      (r"гильбертов\w* пространств\w*", r"скалярн\w* произведени\w*", r"ортонормированн\w* (?:базис|систем)\w*",
       r"ортогональн\w* проекци\w*"),
      (r"espacios? de Hilbert", r"productos? (?:internos?|escalar(?:es)?)", r"(?:bases?|sistemas?) ortonormal(?:es)?",
       r"proyecci(?:ón|ones) ortogonal(?:es)?")),
    T("dense-subset", "21#sec-21-3", (r"dense (?:subsets?|subspaces?|sets?)",), (r"плотн\w* (?:подмножеств|множеств|подпространств)\w*",),
      (r"(?:subconjuntos?|conjuntos?|subespacios?) dens[oa]s?",), chapters=(13, 21)),
]

# Glossary rows (English column) -> term id, for linking the trilingual table.
GLOSSARY = {
    "absolute convergence": "absolute-convergence", "almost everywhere": "almost-everywhere",
    "analytic function": "analytic-function", "boundary": "boundary", "bounded": "bounded-set",
    "Cauchy sequence": "cauchy-sequence", "closed set": "closed-set", "closure": "closure",
    "compact": "compact", "complete space": "complete-space", "connected": "connected",
    "continuity": "continuity", "convergence": "convergent-sequence", "convex function": "convex-function",
    "countable set": "countable-set", "derivative": "derivative", "differentiable": "differentiable",
    "divergence of a sequence": "convergent-sequence", "divergence of a vector field": "divergence",
    "essential supremum": "essential-supremum", "gradient": "gradient", "Hessian": "hessian",
    "implicit function": "implicit-function-theorem", "infimum": "infimum", "inner product": "hilbert-space",
    "integrable": "riemann-integral", "interior": "interior", "Jacobian determinant": "change-of-variables",
    "Jacobian matrix": "jacobian-matrix", "limit": "limit-of-sequence", "limit inferior": "limsup",
    "limit superior": "limsup", "mean value theorem": "lagrange-mvt", "measurable function": "measurable-function",
    "measure": "measure", "metric": "metric-space", "norm": "norm", "null set": "measure-zero-riemann",
    "open set": "open-set", "orthogonal projection": "hilbert-space", "orthonormal basis": "hilbert-space",
    "power series": "power-series", "sequence": "limit-of-sequence", "series": "series",
    "simple function": "simple-function", "supremum": "supremum", "support": None,
    "uniform convergence": "uniform-convergence", "uniform continuity": "uniform-continuity",
    "pointwise convergence": "pointwise-convergence", "sigma-algebra": "sigma-algebra",
    "Lebesgue measure": "lebesgue-measure", "Riemann integral": "riemann-integral", "Taylor series": "taylor-series",
    "Fourier series": "fourier-series", "partial derivative": "partial-derivative",
    "directional derivative": "directional-derivative", "line integral": "line-integral",
    "surface integral": "surface-integral", "flux": "surface-integral", "curl": "divergence",
    "subsequence": "subsequence", "antiderivative": "antiderivative", "improper integral": "improper-integral",
    "radius of convergence": "radius-of-convergence", "Hilbert space": "hilbert-space",
    "Banach space": "lp-space", "conservative field": "conservative-field", "partition": "partition",
    "Riemann sum": "riemann-sum", "Darboux sum": "darboux-sums", "monotone sequence": "monotone-sequence",
    "neighborhood": "neighbourhood", "neighbourhood": "neighbourhood", "limit point": "limit-point",
    "uniformly continuous": "uniform-continuity", "metric space": "metric-space",
}

# Display names for the generated term index: id | English | Русский | Español.
_LABELS = """
quantifier | quantifier | квантор | cuantificador
mathematical-induction | mathematical induction | математическая индукция | inducción matemática
injective | injective map | инъективное отображение | aplicación inyectiva
surjective | surjective map | сюръективное отображение | aplicación sobreyectiva
bijective | bijective map | биективное отображение | aplicación biyectiva
inverse-map | inverse map | обратное отображение | aplicación inversa
equinumerous | equinumerous sets | равномощные множества | conjuntos equipotentes
countable-set | countable set | счётное множество | conjunto numerable
uncountable | uncountable set | несчётное множество | conjunto no numerable
cantor-theorem | Cantor's theorem (power set) | теорема Кантора о мощности булеана | teorema de Cantor (conjunto potencia)
ordered-field | ordered field | упорядоченное поле | cuerpo ordenado
upper-bound | upper and lower bounds | верхняя и нижняя границы | cotas superior e inferior
bounded-set | bounded set | ограниченное множество | conjunto acotado
supremum | supremum | супремум (точная верхняя грань) | supremo
infimum | infimum | инфимум (точная нижняя грань) | ínfimo
completeness-axiom | completeness axiom | аксиома полноты | axioma de completitud
archimedean-property | Archimedean property | архимедовость | propiedad arquimediana
density-of-rationals | density of the rationals | плотность рациональных чисел | densidad de los racionales
nested-interval-theorem | nested-interval theorem | теорема о вложенных отрезках | teorema de los intervalos encajados
extended-real-line | extended real line | расширенная числовая прямая | recta real ampliada
limit-of-sequence | limit of a sequence | предел последовательности | límite de una sucesión
convergent-sequence | convergent sequence | сходящаяся последовательность | sucesión convergente
neighbourhood | ε-neighbourhood | ε-окрестность | ε-entorno
squeeze-theorem | squeeze theorem | теорема о двух милиционерах | teorema del sándwich
infinitesimal | infinitesimal sequence | бесконечно малая | infinitesimal
infinitely-large | infinitely large sequence | бесконечно большая | sucesión infinitamente grande
monotone-convergence-sequences | monotone convergence theorem (sequences) | теорема Вейерштрасса о монотонной последовательности | teorema de convergencia monótona (sucesiones)
monotone-sequence | monotone sequence | монотонная последовательность | sucesión monótona
subsequence | subsequence | подпоследовательность | subsucesión
partial-limit | partial (subsequential) limit | частичный предел | límite parcial
bolzano-weierstrass | Bolzano–Weierstrass theorem | теорема Больцано–Вейерштрасса | teorema de Bolzano–Weierstrass
cauchy-sequence | Cauchy (fundamental) sequence | фундаментальная последовательность (последовательность Коши) | sucesión de Cauchy (fundamental)
cauchy-criterion-sequences | Cauchy criterion for sequences | критерий Коши для последовательностей | criterio de Cauchy para sucesiones
limsup | limit superior and inferior | верхний и нижний пределы | límites superior e inferior
series | numerical series, partial sums | числовой ряд, частичные суммы | serie numérica, sumas parciales
comparison-test | comparison test (series) | признак сравнения (ряды) | criterio de comparación (series)
ratio-test | ratio and root tests | признаки Даламбера и Коши | criterios del cociente y de la raíz
absolute-convergence | absolute convergence | абсолютная сходимость | convergencia absoluta
conditional-convergence | conditional convergence | условная сходимость | convergencia condicional
alternating-series-test | alternating-series (Leibniz) test | признак Лейбница | criterio de Leibniz
riemann-rearrangement | rearrangement of series | перестановка членов ряда | reordenación de series
limit-point | limit point of a set | предельная точка множества | punto de acumulación
punctured-neighbourhood | punctured neighbourhood | проколотая окрестность | entorno perforado
limit-of-function | limit of a function | предел функции | límite de una función
sequential-criterion | sequential (Heine) criterion | критерий Гейне | criterio secuencial (de Heine)
one-sided-limit | one-sided limit | односторонний предел | límite lateral
asymptotic-notation | asymptotic notation (o, O, ~) | асимптотические обозначения (o, O, ~) | notación asintótica (o, O, ~)
continuity | continuity at a point | непрерывность в точке | continuidad en un punto
discontinuity | points of discontinuity | точки разрыва | puntos de discontinuidad
intermediate-value-theorem | intermediate value theorem | теорема Больцано–Коши о промежуточном значении | teorema del valor intermedio
extreme-value-theorem | extreme value theorem (Weierstrass) | теорема Вейерштрасса о наибольшем и наименьшем значениях | teorema de los valores extremos (Weierstrass)
uniform-continuity | uniform continuity | равномерная непрерывность | continuidad uniforme
heine-cantor-theorem | Heine–Cantor theorem | теорема Кантора о равномерной непрерывности | teorema de Heine–Cantor
asymptote | asymptote | асимптота | asíntota
derivative | derivative | производная | derivada
differentiable | differentiable function | дифференцируемая функция | función derivable
one-sided-derivative | one-sided derivatives | односторонние производные | derivadas laterales
differential | differential | дифференциал | diferencial
chain-rule | chain rule | правило цепочки (производная композиции) | regla de la cadena
inverse-function-derivative | derivative of the inverse function | производная обратной функции | derivada de la función inversa
local-extremum | local extremum | локальный экстремум | extremo local
fermat-theorem | Fermat's theorem | теорема Ферма | teorema de Fermat
darboux-property | Darboux's theorem (intermediate values of f′) | теорема Дарбу (промежуточные значения f′) | teorema de Darboux (valores intermedios de f′)
rolle-theorem | Rolle's theorem | теорема Ролля | teorema de Rolle
lagrange-mvt | Lagrange's mean value theorem | теорема Лагранжа (формула конечных приращений) | teorema del valor medio de Lagrange
cauchy-mvt | Cauchy's mean value theorem | теорема Коши о среднем | teorema del valor medio de Cauchy
lhopital-rule | L'Hôpital's rule | правило Лопиталя | regla de L'Hôpital
taylor-formula | Taylor's formula and remainders | формула Тейлора и остаточные члены | fórmula de Taylor y restos
maclaurin | Maclaurin formula | формула Маклорена | fórmula de Maclaurin
convex-function | convex function | выпуклая функция | función convexa
inflection-point | inflection point | точка перегиба | punto de inflexión
jensen-inequality | Jensen's inequality | неравенство Йенсена | desigualdad de Jensen
antiderivative | antiderivative, indefinite integral | первообразная, неопределённый интеграл | primitiva, integral indefinida
partition | partition and its mesh | разбиение и его ранг | partición y su diámetro
darboux-sums | Darboux sums | суммы Дарбу | sumas de Darboux
integrability-criterion | integrability criterion (Riemann–Darboux) | критерий интегрируемости (Римана–Дарбу) | criterio de integrabilidad (Riemann–Darboux)
riemann-sum | Riemann (integral) sum | интегральная сумма Римана | suma de Riemann
riemann-integral | Riemann integral | интеграл Римана | integral de Riemann
oscillation | oscillation of a function | колебание функции | oscilación de una función
measure-zero-riemann | set of measure zero | множество меры нуль | conjunto de medida nula
lebesgue-criterion-riemann | Lebesgue criterion for Riemann integrability | критерий Лебега интегрируемости по Риману | criterio de Lebesgue de integrabilidad
mean-value-integrals | mean value theorems for integrals | теоремы о среднем для интегралов | teoremas del valor medio integral
ftc | fundamental theorem of calculus | основная теорема анализа | teorema fundamental del cálculo
newton-leibniz | Newton–Leibniz formula | формула Ньютона–Лейбница | fórmula de Newton–Leibniz
integration-by-parts | integration by parts | интегрирование по частям | integración por partes
substitution | change of variables in an integral | замена переменной в интеграле | cambio de variable en una integral
cauchy-schwarz-integral | Cauchy–Schwarz inequality | неравенство Коши–Буняковского | desigualdad de Cauchy–Schwarz
improper-integral | improper integral | несобственный интеграл | integral impropia
principal-value | principal value | главное значение | valor principal
comparison-test-integrals | comparison test for integrals | признак сравнения для интегралов | criterio de comparación para integrales
absolute-convergence-integral | absolutely convergent integral | абсолютно сходящийся интеграл | integral absolutamente convergente
dirichlet-abel-integrals | Dirichlet and Abel tests | признаки Дирихле и Абеля | criterios de Dirichlet y Abel
arc-length | arc length, rectifiable curve | длина дуги, спрямляемая кривая | longitud de arco, curva rectificable
path | smooth path | гладкий путь | camino suave
pointwise-convergence | pointwise convergence | поточечная сходимость | convergencia puntual
uniform-convergence | uniform convergence | равномерная сходимость | convergencia uniforme
uniform-cauchy-criterion | uniform Cauchy criterion | равномерный критерий Коши | criterio uniforme de Cauchy
weierstrass-m-test | Weierstrass M-test | признак Вейерштрасса | criterio M de Weierstrass
uniform-limit-continuity | uniform limit of continuous functions | равномерный предел непрерывных функций | límite uniforme de funciones continuas
power-series | power series | степенной ряд | serie de potencias
radius-of-convergence | radius of convergence | радиус сходимости | radio de convergencia
abel-theorem | Abel's theorem | теорема Абеля | teorema de Abel
analytic-function | analytic function | аналитическая функция | función analítica
taylor-series | Taylor series | ряд Тейлора | serie de Taylor
fourier-series | Fourier series and coefficients | ряд Фурье и коэффициенты Фурье | serie y coeficientes de Fourier
dirichlet-pointwise | Dirichlet's pointwise theorem | теорема Дирихле о поточечной сходимости | teorema puntual de Dirichlet
parseval | Parseval's identity, Bessel's inequality | равенство Парсеваля, неравенство Бесселя | identidad de Parseval, desigualdad de Bessel
metric-space | metric space | метрическое пространство | espacio métrico
open-set | open set | открытое множество | conjunto abierto
closed-set | closed set | замкнутое множество | conjunto cerrado
interior | interior point, interior | внутренняя точка, внутренность | punto interior, interior
closure | closure | замыкание | clausura
boundary | boundary | граница множества | frontera
complete-space | complete space | полное пространство | espacio completo
compact | compact set | компакт | conjunto compacto
heine-borel | Heine–Borel theorem | теорема Гейне–Бореля | teorema de Heine–Borel
connected | connected set | связное множество | conjunto conexo
baire | Baire category theorem | теорема Бэра | teorema de Baire
euclidean-norm | Euclidean norm and space | евклидова норма и пространство | norma y espacio euclidianos
norm | norm | норма | norma
iterated-limit | iterated limits | повторные пределы | límites iterados
total-derivative | total derivative (differential of a map) | полная производная (дифференциал отображения) | derivada total
partial-derivative | partial derivative | частная производная | derivada parcial
directional-derivative | directional derivative | производная по направлению | derivada direccional
gradient | gradient | градиент | gradiente
jacobian-matrix | Jacobian matrix | матрица Якоби | matriz jacobiana
tangent-plane | tangent plane | касательная плоскость | plano tangente
hessian | Hessian | гессиан (матрица Гессе) | hessiana
mixed-partials | mixed partial derivatives | смешанные производные | derivadas cruzadas
clairaut-schwarz | Clairaut–Schwarz theorem | теорема Клеро–Шварца | teorema de Clairaut–Schwarz
continuously-differentiable | continuously differentiable map | непрерывно дифференцируемое отображение | aplicación de clase C¹
inverse-function-theorem | inverse function theorem | теорема об обратной функции | teorema de la función inversa
implicit-function-theorem | implicit function theorem | теорема о неявной функции | teorema de la función implícita
lagrange-multipliers | Lagrange multipliers | множители Лагранжа | multiplicadores de Lagrange
multiple-integral | multiple and iterated integrals | кратные и повторные интегралы | integrales múltiples e iteradas
fubini | Fubini's theorem | теорема Фубини | teorema de Fubini
change-of-variables | change of variables, Jacobian | замена переменных, якобиан | cambio de variables, jacobiano
polar-coordinates | polar, cylindrical, spherical coordinates | полярные, цилиндрические, сферические координаты | coordenadas polares, cilíndricas, esféricas
line-integral | line integral | криволинейный интеграл | integral de línea
conservative-field | conservative field | потенциальное поле | campo conservativo
surface-integral | surface integral and flux | поверхностный интеграл и поток | integral de superficie y flujo
divergence | divergence and curl | дивергенция и ротор | divergencia y rotacional
green-theorem | Green's theorem | теорема Грина | teorema de Green
stokes-theorem | Stokes' theorem | теорема Стокса | teorema de Stokes
divergence-theorem | divergence theorem (Gauss–Ostrogradsky) | теорема Гаусса–Остроградского | teorema de la divergencia (Gauss)
sigma-algebra | sigma-algebra | сигма-алгебра | sigma-álgebra
measure | measure | мера | medida
lebesgue-measure | Lebesgue measure | мера Лебега | medida de Lebesgue
measurable-function | measurable function | измеримая функция | función medible
almost-everywhere | almost everywhere | почти всюду | casi en todas partes
simple-function | simple function | простая функция | función simple
lebesgue-integral | Lebesgue integral | интеграл Лебега | integral de Lebesgue
lebesgue-mct | monotone convergence theorem (Lebesgue) | теорема Леви о монотонной сходимости | teorema de convergencia monótona (Lebesgue)
fatou | Fatou's lemma | лемма Фату | lema de Fatou
dominated-convergence | dominated convergence theorem | теорема Лебега о мажорированной сходимости | teorema de convergencia dominada
fubini-tonelli | Fubini–Tonelli theorem | теорема Фубини–Тонелли | teorema de Fubini–Tonelli
lp-space | L^p space | пространство L^p | espacio L^p
holder | Hölder's inequality | неравенство Гёльдера | desigualdad de Hölder
minkowski | Minkowski's inequality | неравенство Минковского | desigualdad de Minkowski
essential-supremum | essential supremum | существенный супремум | supremo esencial
riesz-fischer | Riesz–Fischer theorem | теорема Рисса–Фишера | teorema de Riesz–Fischer
hilbert-space | Hilbert space, inner product | гильбертово пространство, скалярное произведение | espacio de Hilbert, producto interno
dense-subset | dense subset | плотное подмножество | subconjunto denso
"""

LABELS = {}
for _row in _LABELS.strip().splitlines():
    _id, _en, _ru, _es = (part.strip() for part in _row.split("|"))
    LABELS[_id] = {"en": _en, "ru": _ru, "es": _es}

import sys
from collections import OrderedDict
from lib import *
from lib import _ppr
from contenido import CLASES, CAPS, UNIDADES, ETAPA1, verificar

assert not verificar()
T = 20  # 10 pt en tablas apaisadas
doc = nuevo_documento("horizontal", (1.5, 1.5, 1.4, 1.5),
                      pie="Química 3.º · Plan Específico CBT · Plan Anual 2026")
BL = {"color": "FFFFFF", "b": True}


def titulo(txt, salto=False):
    p = doc.add_paragraph(style="Plan de Clase")
    _ppr(p, keep_next=True, page_break=salto, before=160, after=60)
    add_runs(p, [(txt, {})], size=24)


def texto(txt, after=60):
    return parrafo(doc, txt, size=T, before=0, after=after, line=252)


# Portada compacta e identificación
p = doc.add_paragraph(style="Plan de Clase")
_ppr(p, keep_next=True, before=0, after=40, jc="center")
add_runs(p, [("PLAN ANUAL DE QUÍMICA · 2026", {})], size=32)
parrafo(doc, "3.er curso · Bachillerato Científico · Plan Específico: Ciencias Básicas y Tecnología",
        size=22, jc="center", before=0, after=120, keep_next=True)
t = tabla(doc, [3.6, 9.75, 3.6, 9.75])
for a, b, c, d in [("Institución", "______________________________", "Docente", "______________________________"),
                   ("Disciplina", "Química (Plan Específico)", "Sección y turno", "______________  ______________"),
                   ("Carga horaria", "2 HC semanales · 36 encuentros · 72 HC (provisional; ver «Distribución temporal»)",
                    "Fecha de revisión", "____ / ____ / 2026")]:
    fila(t, [dict(txt=[(a, BL)], fill=MEDIO, size=T), dict(txt=b, size=T),
             dict(txt=[(c, BL)], fill=MEDIO, size=T), dict(txt=d, size=T)])

titulo("Fundamentación")
texto("La planificación profundiza la representación de las transformaciones químicas, los modelos de enlace y las "
      "expresiones de concentración para resolver problemas y explicar fenómenos del entorno. Articula cálculo, "
      "nomenclatura, representación de mecanismos y argumentación con decisiones de seguridad: toda actividad con "
      "sustancias peligrosas se resuelve en papel y cada clase tiene una alternativa de aula que no depende de un "
      "laboratorio equipado. Los saberes del Plan Común se retoman como punto de partida, sin presentarlos como "
      "capacidades del Plan Específico.")

titulo("Competencias")
texto("Competencia específica de la disciplina (p. 27): Resuelve situaciones problemáticas referidas a fenómenos "
      "acontecidos en el entorno aplicando los principios y las ecuaciones de las funciones químicas.")
texto("Competencias generales pertinentes (p. 18): Utilicen con actitud científica y ética las metodologías científica e "
      "investigativa en la comprensión y expresión de principios, leyes, teorías y fenómenos acontecidos en el medio "
      "ambiente y en la solución de situaciones problemáticas del entorno. Planteen y resuelvan problemas con actitud "
      "crítica y ética, utilizando el pensamiento lógico y el lenguaje matemático, para formular, deducir y realizar "
      "inferencias que contribuyan al desarrollo personal y social.")
texto("Las páginas corresponden a la transcripción pública del programa usada en versiones anteriores; el cotejo con "
      "el PDF oficial sigue pendiente.", after=40)

titulo("Capacidades del programa y encuentros que las desarrollan")
t = tabla(doc, [1.4, 1.6, 17.2, 6.5], header_repeat=True)
fila(t, [dict(txt=[("Cód.", BL)], fill=OSCURO, size=T), dict(txt=[("Pág.", BL)], fill=OSCURO, size=T),
         dict(txt=[("CAPACIDAD (transcripción pública)", BL)], fill=OSCURO, size=T),
         dict(txt=[("ENCUENTROS", BL)], fill=OSCURO, size=T)], header=True)
for k, (pag, txt) in CAPS.items():
    ns = [str(c["n"]) for c in CLASES if k in c["caps"]]
    fila(t, [dict(txt=[(k, {"b": True})], size=T), dict(txt=pag, size=T), dict(txt=txt, size=T),
             dict(txt=", ".join(ns), size=T)])

titulo("Distribución temporal")
meses = OrderedDict()
for c in CLASES:
    meses.setdefault(c["mes"], []).append(c["n"])
t = tabla(doc, [2.67] * 10)
fila(t, [dict(txt=[(m, BL)], fill=MEDIO, size=T, jc="center") for m in meses], keep_next=True)
fila(t, [dict(txt=f"{len(v)} enc. · {v[0]}–{v[-1]}" if len(v) > 1 else f"1 enc. · {v[0]}", size=T, jc="center")
         for v in meses.values()])
assert sum(len(v) for v in meses.values()) == 36
separador(doc, 120, keep_next=False)
texto("Se proponen 36 encuentros de 2 HC (72 HC). Para la secuencia didáctica se supone una hora cátedra de 40 minutos: "
      "80 minutos por encuentro. Ni la carga semanal ni la duración de la hora cátedra pudieron verificarse en el "
      "programa oficial (malla de la p. 20 pendiente); si la institución usa otra duración, se reajustan los minutos "
      "de cada momento manteniendo las proporciones.")
texto("Calendario: según comunicaciones públicas sobre el calendario escolar 2026 (Resolución MEC N.º 2065/2025, no "
      "consultada en su texto oficial), las clases se desarrollan del 23 de febrero al 30 de noviembre, con receso de "
      "invierno del 13 al 24 de julio. Los encuentros 1–16 corresponden a la primera etapa y 17–36 a la segunda. "
      "La reserva mensual es orientativa: las fechas se ajustan al día semanal de clase, a los feriados y al calendario "
      "institucional. Si se pierde un encuentro, no se suprime una capacidad: se integra la revisión con la práctica o "
      "se gestiona la recuperación y se registra el cambio en este plan y en el plan de clase.")

titulo("Estrategias metodológicas y recursos")
texto("Modelización docente seguida de práctica guiada y aplicación individual en cada encuentro; representación con "
      "estructuras de Lewis, modelos manipulables y diagramas de orbitales; análisis de datos de cinética y de una "
      "simulación de semivida; problemas graduados de concentración; circuito de estaciones; mecanismos con flechas "
      "curvas. Recursos comunes: pizarrón, tabla periódica, calculadora, cuaderno, tarjetas y plantillas impresas. "
      "Materiales opcionales (pastillas efervescentes, sal de mesa, balanza) solo con supervisión docente.")

titulo("Evaluación")
texto("Los indicadores de logro de cada encuentro son los criterios de evaluación; los instrumentos indicados en la "
      "secuencia registran el desempeño individual aunque la actividad se haya preparado en grupo. Evaluación "
      "diagnóstica en el encuentro 1; seguimiento formativo en todos; evaluación integradora en el 12 (C1–C4); valoración "
      "de la primera etapa en el 16 (C3–C6); prueba práctica por estaciones en el 24; valoración de la segunda etapa en "
      "el 35 (C7–C10) y recuperación con transferencia en el 36. La escala 0–2 de las rúbricas es didáctica: la "
      "calificación se ajusta a la normativa de evaluación vigente en la institución. La planificación declara la "
      "cobertura prevista; el logro se afirma solo con las evidencias recogidas.")

titulo("Atención a la diversidad")
texto("Lectura guiada de consignas, fragmentación de los cálculos, fórmulas ampliadas, modelos manipulables y tiempo "
      "ajustado a las necesidades identificadas. Las respuestas orales no eximen de representar fórmulas, cargas y "
      "unidades cuando el indicador lo exige. Los agrupamientos sirven de apoyo; la evidencia de logro es individual.")


titulo("Bibliografía")
for b in ["Ministerio de Educación y Cultura (2014). Actualización Curricular del Bachillerato Científico de la Educación "
          "Media. Plan Específico: Énfasis en Ciencias Básicas y Tecnología. Asunción: MEC. (Original pendiente de cotejo.)",
          "Química. Equilibrio ácido/base en soluciones acuosas (2012). Buenos Aires: Eudeba.",
          "Química. Problemas y ejercicios de aplicación para química (2010). Buenos Aires: Eudeba.",
          "Física y Química 3. Materia, estructura y transformaciones (2012). Buenos Aires: Santillana.",
          "Chemistry 2e (2019). Houston: OpenStax, Rice University. https://openstax.org/details/books/chemistry-2e"]:
    texto("• " + b, after=30)


# Secuencia anual
titulo("Secuencia anual de encuentros", salto=True)
W = [1.0, 4.6, 7.4, 2.1, 4.1, 4.5, 3.0]
t = tabla(doc, W)
hdr = ["N.º", "TEMA Y CAPACIDADES", "INDICADORES DE LOGRO", "TIEMPO", "PROCEDIMIENTOS", "INSTRUMENTOS", "OBSERVACIONES"]
fila(t, [dict(txt=[(h, BL)], fill=OSCURO, size=18, jc="center") for h in hdr], header=True, keep_next=True)
OBS = {12: "Evaluación integradora (C1–C4).", 16: "Valoración y devolución de la 1.ª etapa.",
       24: "Integración de soluciones.", 35: "Valoración de la 2.ª etapa.",
       36: "Recuperación de C7–C10. C1–C6 se documentan en sus clases."}
u_prev = None
for c in CLASES:
    n = c["n"]
    if n == 1 or n == 17:
        txt = "PRIMERA ETAPA · febrero a junio" if n == 1 else "SEGUNDA ETAPA · junio a noviembre"
        fila(t, [dict(txt=[(txt, BL)], fill=OSCURO, span=7, size=T)], keep_next=True)
    if c["u"] != u_prev:
        nom, caps = UNIDADES[c["u"]]
        fila(t, [dict(txt=[(f"Unidad {c['u']} · {nom}", {"b": True, "color": OSCURO}),
                           (f"   ({', '.join(caps)})", {"color": OSCURO})], fill=BANDA_UNIDAD, span=7, size=T)],
             keep_next=True)
        u_prev = c["u"]
    ti, td, tc = c["t"]
    obs = ["Fecha: ___/___"]
    if n in OBS:
        obs.append(OBS[n])
    fila(t, [dict(txt=[(str(n), {"b": True})], size=T, jc="center"),
             dict(pars=[[(c["tema"], {"b": True})], ", ".join(c["caps"])], size=T),
             dict(pars=[f"• {i}" for i in c["ind"]], size=T),
             dict(pars=["2 HC", c["mes"]], size=T),
             dict(txt=c["proc"], size=T), dict(txt=c["inst"], size=T),
             dict(pars=obs, size=T)])

separador(doc, 240, keep_next=True)
parrafo(doc, "Firma docente: ______________________________          Dirección: ______________________________          "
        "Fecha: ____ / ____ / 2026", size=T, keep_lines=True)

guardar(doc, sys.argv[1])
print("ok")

import sys
from lib import *
from lib import _ppr
from contenido import CLASES, CAPS, CONTENIDOS, verificar

assert not verificar()
T = 20
doc = nuevo_documento("horizontal", (1.5, 1.5, 1.4, 1.5),
                      pie="Química 3.º · Plan Específico CBT · Matriz curricular 2026")
BL = {"color": "FFFFFF", "b": True}


def titulo(txt, salto=False, before=160):
    p = doc.add_paragraph(style="Plan de Clase")
    _ppr(p, keep_next=True, page_break=salto, before=before, after=60)
    add_runs(p, [(txt, {})], size=24)


def texto(partes, after=60):
    return parrafo(doc, partes, size=T, before=0, after=after, line=252)


p = doc.add_paragraph(style="Plan de Clase")
_ppr(p, keep_next=True, before=0, after=40, jc="center")
add_runs(p, [("MATRIZ DE CAPACIDADES Y COBERTURA CURRICULAR", {})], size=30)
parrafo(doc, "Química · 3.er curso · Plan Específico: Ciencias Básicas y Tecnología · 2026",
        size=22, jc="center", before=0, after=100, keep_next=True)
texto("Las capacidades y los contenidos se transcriben de la copia pública del programa utilizada en las versiones "
      "anteriores (páginas impresas 27–28); no se cambian verbos ni alcance. El cotejo con el PDF oficial sigue pendiente. "
      "«Encuentros» y «Evidencias» describen la cobertura planificada en los planes de clase v3, no aprendizajes ya "
      "logrados. Las incidencias I1–I8 se detallan al final.")

INC = {"C1": "I3", "C6": "I4", "C8": "I5"}
W = [5.3, 5.8, 2.3, 9.5, 3.8]
t = tabla(doc, W)
fila(t, [dict(txt=[(h, BL)], fill=OSCURO, size=18, jc="center") for h in
         ["CAPACIDAD", "CONTENIDOS (transcripción)", "ENCUENTROS", "EVIDENCIAS EVALUABLES PLANIFICADAS", "ESTADO"]],
     header=True, keep_next=True)
for k, (pag, txt) in CAPS.items():
    clases = [c for c in CLASES if k in c["caps"]]
    evid = []
    for c in clases:
        e = c["ev"] if isinstance(c["ev"], str) else c["ev"][k]
        evid.append([(f"Cl. {c['n']}: ", {"b": True}), (e + ".", {})])
    estado = ["Cobertura planificada completa.", "Cotejo con el original pendiente (I1)."]
    if k in INC:
        estado.append(f"Ver incidencia {INC[k]}.")
    fila(t, [dict(pars=[[(f"{k} · {pag}", {"b": True, "color": OSCURO})], txt], size=T),
             dict(txt=CONTENIDOS[k], size=T),
             dict(txt=", ".join(str(c["n"]) for c in clases), size=T),
             dict(pars=evid, size=T), dict(pars=estado, size=T)])

titulo("Síntesis de verificación de la matriz")
texto("Cada una de las diez capacidades tiene al menos tres encuentros y una evidencia evaluable por encuentro. En las "
      "clases con varias capacidades (5, 6, 12, 15–18, 24, 30–36) la evidencia se declara por capacidad. La clase 36 "
      "documenta solo C7–C10; C1–C6 se documentan en las clases 1–18. Las capacidades C1 y C2 se valoran en la "
      "evaluación integradora de la clase 12; C3–C6 en la valoración de la primera etapa (clase 16); C7–C10 en la de la "
      "segunda etapa (clase 35).")

titulo("Competencias y orientaciones (según transcripción pública)")
texto([("Competencia específica (p. 27): ", {"b": True}),
       ("Resuelve situaciones problemáticas referidas a fenómenos acontecidos en el entorno aplicando los principios y "
        "las ecuaciones de las funciones químicas.", {})])
texto([("Competencias generales (p. 18): ", {"b": True}),
       ("Utilicen con actitud científica y ética las metodologías científica e investigativa en la comprensión y "
        "expresión de principios, leyes, teorías y fenómenos acontecidos en el medio ambiente y en la solución de "
        "situaciones problemáticas del entorno. Planteen y resuelvan problemas con actitud crítica y ética, utilizando "
        "el pensamiento lógico y el lenguaje matemático, para formular, deducir y realizar inferencias que contribuyan "
        "al desarrollo personal y social.", {})])
texto([("Orientación metodológica (p. 43): ", {"b": True}),
       ("«En cuanto a la disciplina de Química, se debe seguir afianzando la notación y nomenclatura científica, la "
        "notación y el balanceo de ecuaciones químicas, y el planteo y resolución de problemas químicos. Así mismo, en "
        "el proceso de enseñanza-aprendizaje debe brindarse un espacio importante al diseño y ejecución de "
        "experiencias, a fin de otorgar el carácter vivencial a la enseñanza de esta disciplina.»", {})])
texto([("Orientación de evaluación (p. 44): ", {"b": True}),
       ("sugiere rúbrica, lista de control, registro de secuencias de aprendizaje, pruebas de libro abierto, fichas de "
        "investigación, pruebas escritas y pruebas prácticas; las pruebas escritas orientadas principalmente a la "
        "resolución de problemas y generación de preguntas. Los instrumentos de los planes v3 (listas de cotejo, "
        "rúbricas, pruebas escritas, prueba práctica por estaciones y portafolio) se ajustan a esa orientación.", {})])
texto([("Fuente: ", {"b": True}), ("Ministerio de Educación y Cultura (2014). Actualización Curricular del Bachillerato "
       "Científico de la Educación Media. Plan Específico: Énfasis en Ciencias Básicas y Tecnología. Asunción: MEC "
       "(pp. 18, 20, 26–28, 43–46). Transcripciones de versiones anteriores, no cotejadas con el original en esta revisión.", {})])

titulo("Incidencias que requieren cierre documental")
t = tabla(doc, [1.1, 13.6, 12.0])
fila(t, [dict(txt=[(h, BL)], fill=OSCURO, size=18) for h in ["N.º", "INCIDENCIA", "TRATAMIENTO EN v3"]], header=True,
     keep_next=True)
for a, b, c in [
    ("I1", "No se dispone del PDF oficial completo. En esta revisión el repositorio del CONACYT (dspacereva.conacyt.gov.py, "
           "archivo «enfasiscienciasbasicasytecnologia.pdf») apareció en la búsqueda, pero la red del entorno bloqueó la descarga.",
     "Capacidades y páginas se mantienen como transcripción; ningún dato se presenta como verificado en la fuente oficial."),
    ("I2", "Malla curricular de la p. 20 sin lectura verificable: no se confirmó la carga semanal de Química específica.",
     "Se mantienen 2 HC semanales como propuesta provisional (36 encuentros, 72 HC)."),
    ("I3", "«Fusion nuclear» y «Fusión nuclear» aparecen consecutivamente; por el contexto (reactores, bomba atómica) la primera "
           "remite a fisión.", "Clase 8 enseña fisión y fusión y lo indica en una nota docente; no se corrige la fuente en silencio."),
    ("I4", "El título de hibridación está en la p. 27 y el desglose «Atómicos y moleculares» en la p. 28.",
     "Clases 15, 17 y 18 distinguen orbital híbrido (atómico) de orbital molecular."),
    ("I5", "«Bases cuaternarias y polinucleados en combinaciones» tiene alcance ambiguo.",
     "Clase 29 declara su interpretación: hidróxidos de amonio cuaternario y sistemas aromáticos polinucleares, "
     "carbocíclicos (naftaleno) y nitrogenados (quinolina)."),
    ("I6", "No se pudo comprobar si existe una actualización curricular posterior a 2014 que modifique el programa.",
     "No se usa la priorización curricular 2021 como reemplazo."),
    ("I7", "Una copia pública presenta numeración final «49» y otra «48»; no se certifica la integridad del original.",
     "Las páginas citadas son las impresas en la copia de 48 páginas."),
    ("I8", "Duración de la hora cátedra no verificada en fuente oficial.",
     "Los planes suponen HC de 40 min (80 min por encuentro) y lo declaran en la identificación de cada plan."),
]:
    fila(t, [dict(txt=[(a, {"b": True})], size=T), dict(txt=b, size=T), dict(txt=c, size=T)])

guardar(doc, sys.argv[1])
print("ok")

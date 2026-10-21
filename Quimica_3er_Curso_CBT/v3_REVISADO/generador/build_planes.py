import sys
from lib import *
from lib import _ppr
from contenido import CLASES, CAPS, UNIDADES, ETAPA1, verificar

assert not verificar(), verificar()

doc = nuevo_documento("vertical", (1.6, 2.0, 1.4, 2.0),
                      pie="Química 3.º · Plan Específico CBT · Planes de clase 2026")
W_ID = [2.3, 7.0, 2.0, 5.7]
W_2 = [3.3, 13.7]
W_M = [2.3, 13.0, 1.7]

BL = {"color": "FFFFFF", "b": True}


def rot(txt):
    return [(txt, BL)]


for c in CLASES:
    n = c["n"]
    etapa = "1.ª etapa" if n in ETAPA1 else "2.ª etapa"
    # 1. Título
    p = doc.add_paragraph(style="Plan de Clase")
    _ppr(p, keep_next=True, page_break=(n > 1), before=0, after=60)
    add_runs(p, [(f"Plan de Clase N.º {n}  ·  {c['tema']}", {})], size=26)

    # 2. Identificación
    t = tabla(doc, W_ID)
    unidad = f"{c['u']} · {UNIDADES[c['u']][0]}"
    ti, td, tc = c["t"]
    filas = [("Docente", "__________________________", "Disciplina", f"Química · {etapa} · {c['mes'].lower()}"),
             ("Curso", "3.º · Plan Específico Ciencias Básicas y Tecnología", "Tiempo", f"2 HC · {ti + td + tc} min (HC de 40 min)"),
             ("Unidad", unidad, "Sección", "____________"),
             ("Institución", "__________________________", "Fecha", "____ / ____ / 2026")]
    for a, b, c2, d in filas:
        fila(t, [dict(txt=rot(a), fill=MEDIO), dict(txt=b), dict(txt=rot(c2), fill=MEDIO), dict(txt=d)], keep_next=True)
    separador(doc)

    # 3. Capacidad e indicadores
    t = tabla(doc, W_2)
    caps_pars = [[(f"{k} · ", {"b": True}), (CAPS[k][1], {})] for k in c["caps"]]
    fila(t, [dict(pars=[rot("Capacidad"), rot("(programa MEC)")], fill=MEDIO), dict(pars=caps_pars)], keep_next=True)
    fila(t, [dict(pars=[rot("Indicadores"), rot("de logro")], fill=MEDIO), dict(pars=[f"• {i}" for i in c["ind"]])],
         keep_next=True)
    separador(doc)

    # 4. Momentos didácticos
    t = tabla(doc, W_M)
    fila(t, [dict(txt=rot("MOMENTO"), fill=OSCURO, jc="center"), dict(txt=rot("ACTIVIDADES"), fill=OSCURO),
             dict(txt=rot("TIEMPO"), fill=OSCURO, jc="center")], header=True, keep_next=True)
    fila(t, [dict(txt=[("Inicio", {"b": True})], fill=SUAVE), dict(txt=c["ini"]), dict(txt=f"{ti} min", jc="center")],
         keep_next=True)
    dev_pars = [[(f"{lab} ({m} min). ", {"b": True}), (txt, {})] for lab, m, txt in c["dev"]]
    fila(t, [dict(txt=[("Desarrollo", {"b": True})], fill=SUAVE), dict(pars=dev_pars, after=30),
             dict(txt=f"{td} min", jc="center")], cant_split=False)
    fila(t, [dict(txt=[("Cierre", {"b": True})], fill=SUAVE), dict(txt=c["cie"]), dict(txt=f"{tc} min", jc="center")],
         keep_next=True)
    fila(t, [dict(txt=[("Total", {"b": True})], fill=SUAVE, span=2, jc="right"),
             dict(txt=[(f"{ti + td + tc} min", {"b": True})], jc="center")], keep_next=True)
    separador(doc)

    # 5. Recursos
    t = tabla(doc, W_2)
    fila(t, [dict(txt=rot("Recursos"), fill=MEDIO), dict(txt=c["rec"])], keep_next=True)
    separador(doc)

    # 6. Evaluación
    t = tabla(doc, W_2)
    fila(t, [dict(txt=rot("EVALUACIÓN"), fill=OSCURO, span=2, jc="center")], keep_next=True)
    fila(t, [dict(txt=rot("Procedimientos"), fill=MEDIO), dict(txt=c["proc"])], keep_next=True)
    fila(t, [dict(txt=rot("Instrumentos"), fill=MEDIO), dict(txt=c["inst"])], keep_next=True)

    # 7. Observaciones y firmas
    parrafo(doc, "Observaciones y ajustes: " + "_" * 66,
            keep_next=True, keep_lines=True, before=80, after=0)
    parrafo(doc, "Firma docente: ______________________          Visto bueno: ______________________",
            keep_lines=True, before=120, after=0)

guardar(doc, sys.argv[1])
print("ok", sys.argv[1])

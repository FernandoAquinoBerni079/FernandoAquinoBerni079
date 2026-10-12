"""Correcciones de contenido de la auditoría FINAL OFICIO (Informe 03 del compendio, 11/10/2026).

Uso: python3 -I correcciones_v2.py LIBRO_FO.docx SOL_FO.docx LIBRO_V2.docx SOL_V2.docx
Trabaja sobre los .docx FINAL OFICIO (fuente única). Cada reemplazo debe encontrar su texto
exactamente UNA vez; si no, aborta. Conserva el formato de los runs (el texto nuevo queda en el
run donde empieza el texto viejo). Hallazgos: 01 (capacidad transversal), 02 (Ev. U4 ítem 7),
03 (Integradora 2 ítem 8), 05 (Access/Office 2016), 08 (Práctica 3).
"""
import sys, copy, docx
from docx.oxml.ns import qn

CAP = '«Reconoce la importancia de la práctica Conductual en el desarrollo de las actividades.»'

LIBRO = [
    # 05 — Access / Office 2016
    ('La verificación editorial se realizó sobre una instalación con licencia Office 2016 actualizada mediante '
     'Click-to-Run; según la versión y el canal de actualización, algunos nombres o ubicaciones de comandos pueden variar ligeramente.',
     'La navegación se contrastó históricamente en Microsoft Access de Office 2016, versión fuera de soporte desde el '
     '14 de octubre de 2025. Para el trabajo escolar de 2026 se recomienda utilizar Access incluido en Microsoft 365 o '
     'Access 2024 con licencia válida y soporte vigente. Los nombres de comandos pueden variar según la versión; el docente '
     'verificará las rutas en su instalación.'),
    # 08 — Práctica 3: datos propios (otra semana) para que no repita la segunda semana de la Práctica 21
    ('la suma de los seis importes de la semana del 9 al 11 de marzo y su promedio',
     'la suma de los seis importes de la semana del 16 al 18 de marzo y su promedio'),
    ('19.000 · 17.000 · 29.000 · 19.000 · 9.000 · 42.000', '15.000 · 21.000 · 27.000 · 24.000 · 18.000 · 39.000'),
    # 02 — Evaluación de la Unidad 4, ítem 7
    ('7. Calculá, agrupando por categoría, el importe de Panificados, Salados y Bebidas, y verificá que sumen la recaudación '
     'total (importes por producto: Chipa 18.000, Mbeju 5.000, Empanada 18.000, Milanesa 45.000, Cocido 8.000, Gaseosa 40.000).',
     '7. En una jornada distinta, se vendieron: 3 chipas a G. 4.000 cada una; 2 mbeju a G. 7.000; 4 empanadas a G. 8.000; '
     '2 milanesas a G. 16.000; 3 cocidos a G. 4.500; y 2 jugos a G. 8.500. Agrupá los importes en Panificados, Salados y '
     'Bebidas, y calculá la recaudación total.'),
    # 03 — Evaluación integradora de la 2.ª etapa, ítem 8
    ('8. Con los totales por venta (V1 14.000, V2 19.000, V3 34.000, V4 17.000, V5 50.000) y sabiendo que V1 y V3 son de Rosa, '
     'V2 de Luis, V4 de Ana y V5 de Miguel, calculá la recaudación de cada cliente, la total y la venta promedio.',
     '8. En un nuevo local se registraron cinco ventas: F1 G. 17.000, F2 G. 22.000, F3 G. 39.000, F4 G. 18.000 y F5 G. 57.000. '
     'F1 y F3 corresponden a Rosa; F2 a Luis; F4 a Ana; F5 a Miguel. Calculá la recaudación por cliente, el total y el promedio por venta.'),
]

SOL = [
    ('La interfaz se contrastó con una instalación con licencia Office 2016 actualizada mediante Click-to-Run; los resultados '
     'de las consultas se verificaron con un script sobre los mismos datos. Algunos rótulos pueden variar ligeramente según la '
     'versión y el canal de actualización.',
     'La navegación se contrastó históricamente en Microsoft Access de Office 2016, versión fuera de soporte desde el 14 de '
     'octubre de 2025. Para el trabajo escolar de 2026 se recomienda utilizar Access incluido en Microsoft 365 o Access 2024 con '
     'licencia válida y soporte vigente. Los resultados de las consultas se verificaron con un script sobre los mismos datos. '
     'Los nombres de comandos pueden variar según la versión; el docente verificará las rutas en su instalación.'),
    ('Act. 2: traza 19.000 → 36.000 → 65.000 → 84.000 → 93.000 → 135.000; total G. 135.000; promedio G. 22.500 '
     '(PSeInt muestra «Total: 135000» y «Promedio: 22500»). Desafío: 2 ventas (29.000 y 42.000).',
     'Act. 2: traza 15.000 → 36.000 → 63.000 → 87.000 → 105.000 → 144.000; total G. 144.000; promedio G. 24.000 '
     '(PSeInt muestra «Total: 144000» y «Promedio: 24000»). Desafío: 4 ventas (21.000, 27.000, 24.000 y 39.000).'),
    ('el programa termina mostrando solo el último importe, 42000)', 'el programa termina mostrando solo el último importe, 39000)'),
    ('7. Panificados 18.000 + 5.000 = 23.000; Salados 18.000 + 45.000 = 63.000; Bebidas 8.000 + 40.000 = 48.000; suma G. 134.000.',
     '7. Panificados 3 × 4.000 + 2 × 7.000 = 12.000 + 14.000 = 26.000; Salados 4 × 8.000 + 2 × 16.000 = 32.000 + 32.000 = 64.000; '
     'Bebidas 3 × 4.500 + 2 × 8.500 = 13.500 + 17.000 = 30.500; total G. 120.500 (26.000 + 64.000 + 30.500).'),
    ('8. Rosa 48.000; Luis 19.000; Ana 17.000; Miguel 50.000; total G. 134.000; promedio 134.000 / 5 = G. 26.800.',
     '8. Rosa 17.000 + 39.000 = 56.000; Luis 22.000; Ana 18.000; Miguel 57.000; total G. 153.000 '
     '(56.000 + 22.000 + 18.000 + 57.000); promedio 153.000 / 5 = G. 30.600.'),
]


def texto(p):
    return ''.join(t.text or '' for t in p.iter(qn('w:t')))


def reemplazar(d, viejo, nuevo):
    ps = [p for p in d.element.body.iter(qn('w:p')) if viejo in texto(p)]
    assert len(ps) == 1, (len(ps), viejo[:80])
    p = ps[0]
    ts = list(p.iter(qn('w:t')))
    full = ''.join(t.text or '' for t in ts)
    ini = full.index(viejo); fin = ini + len(viejo)
    pos = 0; primero = True
    for t in ts:
        a, b = pos, pos + len(t.text or ''); pos = b
        if b <= ini or a >= fin:
            continue
        s = t.text
        izq = s[:max(0, ini - a)]; der = s[min(len(s), fin - a):]
        t.text = izq + (nuevo if primero else '') + der
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        primero = False
    assert nuevo in texto(p)


def parrafo_tras(ancla, molde, partes):
    """Inserta después de `ancla` un párrafo con el formato de `molde`; partes = [(texto, negrita)]."""
    p = copy.deepcopy(molde)
    rs = p.findall(qn('w:r'))
    for r in rs[1:]:
        p.remove(r)
    for el in list(p):
        if el.tag not in (qn('w:pPr'), qn('w:r')):
            p.remove(el)
    base = rs[0]
    for el in list(base):
        if el.tag != qn('w:rPr'):
            base.remove(el)
    p.remove(base)
    for txt, neg in partes:
        r = copy.deepcopy(base)
        rPr = r.find(qn('w:rPr'))
        if rPr is None:
            rPr = r.makeelement(qn('w:rPr'), {}); r.insert(0, rPr)
        for b in rPr.findall(qn('w:b')):
            rPr.remove(b)
        if neg:
            rPr.insert(0, rPr.makeelement(qn('w:b'), {}))
        t = r.makeelement(qn('w:t'), {}); t.text = txt
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve'); r.append(t)
        p.append(r)
    ancla.addnext(p)
    return p


def unico(d, empieza):
    ps = [p for p in d.element.body if p.tag == qn('w:p') and texto(p).startswith(empieza)]
    assert len(ps) == 1, (len(ps), empieza)
    return ps[0]


AUTOEVAL = {  # 09 — cierre de las Clases 6 y 19: indicadores literales de la ficha, sin respuestas
    'Clase 6 — Tipos y aplicaciones de bases de datos': 'Práctica 6',
    'Clase 19 — Filtros y consultas de selección': 'Práctica 19',
}


def celda_txt(tc, txt):
    ps = tc.findall(qn('w:p'))
    for p in ps[1:]:
        tc.remove(p)
    ts = list(ps[0].iter(qn('w:t')))
    for t in ts[1:]:
        t.getparent().getparent().remove(t.getparent())
    ts[0].text = txt


def autoevaluacion(d, clase, practica):
    """Tras el Desafío de la clase: subtítulo, consigna y tabla «Puedo… / Sí / Todavía no» con los
    indicadores de logro de su ficha (leídos del propio libro, no transcritos)."""
    body = d.element.body; els = list(body)
    ini = max(i for i, e in enumerate(els) if texto(e) == clase)
    fin = next(i for i in range(ini + 1, len(els)) if texto(els[i]).startswith(practica + ' — '))
    ficha = next(e for e in els[ini:fin] if e.tag == qn('w:tbl') and 'Indicadores de logro' in texto(e))
    inds = [texto(p)[2:].strip() for p in ficha.iter(qn('w:p')) if texto(p).startswith('• ')]
    assert len(inds) == 3, inds
    ult = els[fin - 1]; assert texto(ult).startswith('10. '), texto(ult)
    sub = next(e for e in els[ini:fin] if texto(e) == 'Actividades de aplicación')
    h = copy.deepcopy(sub); next(h.iter(qn('w:t'))).text = 'Autoevaluación antes de la ' + practica
    ult.addnext(h)
    con = copy.deepcopy(ult)
    ind = con.find(qn('w:pPr')).find(qn('w:ind'))
    if ind is not None: ind.getparent().remove(ind)
    for t in list(con.iter(qn('w:t')))[1:]:
        t.text = ''
    next(con.iter(qn('w:t'))).text = ('Marcá con una X. Si algo queda en «Todavía no», repasá esa parte de la clase '
                                     'antes de empezar la ' + practica + '.')
    h.addnext(con)
    molde = next(e for e in body.iter(qn('w:tbl')) if texto(e).startswith('AspectoBase localBase en servidor'))
    t = copy.deepcopy(molde)
    trs = t.findall(qn('w:tr'))
    for tr in trs[4:]:
        t.remove(tr)
    filas = [('Puedo…', 'Sí', 'Todavía no')] + [(x, '', '') for x in inds]
    for tr, fila in zip(t.findall(qn('w:tr')), filas):
        for tc, v in zip(tr.findall(qn('w:tc')), fila):
            celda_txt(tc, v)
    # columnas: 75 % / 12,5 % / 12,5 % del ancho de la tabla
    cols = t.find(qn('w:tblGrid')).findall(qn('w:gridCol'))
    tot = sum(int(c.get(qn('w:w'))) for c in cols)
    ws = [round(tot * 0.75), round(tot * 0.125)]; ws.append(tot - ws[0] - ws[1])
    for c, w in zip(cols, ws):
        c.set(qn('w:w'), str(w))
    for tr in t.findall(qn('w:tr')):
        for tc, w in zip(tr.findall(qn('w:tc')), ws):
            tcw = tc.find(qn('w:tcPr')).find(qn('w:tcW'))
            if tcw is not None:
                tcw.set(qn('w:w'), str(w)); tcw.set(qn('w:type'), 'dxa')
    con.addnext(t)
    return inds


def libro(ent, sal):
    d = docx.Document(ent)
    for v, n in LIBRO:
        reemplazar(d, v, n)
    # 01 — capacidad transversal en la Presentación (tras el párrafo del caso) …
    caso = unico(d, 'El caso que nos acompaña es el Copetín Karumbé')
    parrafo_tras(caso, caso, [('Capacidad transversal del programa MEC: ', True), (CAP[1:-1], False),
                              (' Esta capacidad se desarrolla al cumplir procedimientos, compartir roles, proteger datos, '
                               'verificar resultados, documentar cambios y participar responsablemente en las prácticas y el proyecto.', False)])
    # … y en el Proyecto Final Integrador, con su evidencia en el proyecto
    tit = unico(d, 'Pautas para el equipo')
    ult = unico(d, '• Preparen una explicación breve y clara')
    h = copy.deepcopy(tit)
    for t in h.iter(qn('w:t')):
        t.text = ''
    next(h.iter(qn('w:t'))).text = 'Capacidad transversal del programa'
    ult.addnext(h)
    parrafo_tras(h, ult, [('Capacidad transversal MEC: ', True), (CAP[1:-1], False),
                          (' En el proyecto se evidencia al cumplir los procedimientos acordados, sostener el rol asignado en el '
                           'equipo, resguardar los datos del emprendimiento, verificar cada consulta con un control cruzado y '
                           'registrar los cambios en la carpeta del proyecto.', False)])
    for clase, practica in AUTOEVAL.items():
        autoevaluacion(d, clase, practica)
    d.save(sal)


def solucionario(ent, sal):
    d = docx.Document(ent)
    for v, n in SOL:
        reemplazar(d, v, n)
    anc = unico(d, '• Exigir un control cruzado por consulta')
    parrafo_tras(anc, anc, [('• Observar la capacidad transversal del programa, ' + CAP + ', con evidencias concretas: '
                             'cumplimiento de procedimientos y roles, resguardo de los datos, control cruzado de las consultas '
                             'y registro de cambios en la carpeta. Se informa como apreciación cualitativa y no modifica los pesos de la rúbrica.', False)])
    d.save(sal)


if __name__ == '__main__':
    libro(sys.argv[1], sys.argv[3])
    solucionario(sys.argv[2], sys.argv[4])
    print('correcciones aplicadas:', len(LIBRO), 'reemplazos + 2 inserciones en el libro;', len(SOL), 'reemplazos + 1 inserción en el solucionario')

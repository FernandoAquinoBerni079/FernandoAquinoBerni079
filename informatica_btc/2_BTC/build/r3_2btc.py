# -*- coding: utf-8 -*-
"""Informática 2.º BTC — copias R3 a partir de R2 (R2 queda intacta: se abre solo para lectura).

Cierre de la revisión: legibilidad de figuras en el laboratorio, figuras 1 y 2, y las observaciones editoriales que
no requieren decisión institucional (ver `CIERRE_R3_2BTC.md`). Renderiza, recalcula índices y deja DOCX y PDF en
2_BTC/R3 y 2_BTC/pdf_revision_R3.
Uso: python3 r3_2btc.py
"""
import copy, json, os, re, sys
import docx
from docx.oxml.ns import qn
AQUI = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(os.path.dirname(BASE), 'build_comun'))
import docx_util as U

R2 = os.path.join(BASE, 'R2'); R3 = os.path.join(BASE, 'R3'); PDF = os.path.join(BASE, 'pdf_revision_R3')
FIG = os.path.join(BASE, 'figuras_R3')
SALIDA = ('Tomo', 'Laboratorio', 'Plan_anual', 'Solucionario', 'Planes_de_clase')
VERSION = ('Revisión R2, 22 de octubre de 2026.', 'Revisión R3, 22 de octubre de 2026.')
ANCHO = 15.5          # ancho del tomo
# Cuerpo del texto más chico de cada figura a 15,5 cm (medición en LEGIBILIDAD_R3_2BTC.md). Vectoriales (5, 8, 9):
# cuerpo de diseño. El ancho mínimo admitido para cada figura es el que deja ese texto en 7 pt.
MIN_PT = {1: 8.2, 2: 9.8, 3: 8.6, 4: 9.3, 5: 8.5, 6: 8.8, 7: 11.4, 8: 9.5, 9: 9.5, 10: 9.7, 11: 7.8, 12: 8.2, 13: 9.0}
PISO_PT = 7.0
ANCHO_MIN = {n: round(ANCHO * PISO_PT / pt + 0.05, 1) for n, pt in MIN_PT.items()}


def abrir(k):
    return docx.Document(os.path.join(R2, 'Informatica_2_BTC_%s_R2.docx' % k))


def ruta(k):
    return os.path.join(R3, 'Informatica_2_BTC_%s_R3.docx' % k)


def R(doc, k, viejo, nuevo, veces=1, motivo=''):
    U.reemplazar(doc, viejo, nuevo, veces, k, motivo)


def reg(doc, antes, despues, n, motivo):
    U.REGISTRO.append({'documento': doc, 'antes': antes, 'despues': despues, 'apariciones': n, 'motivo': motivo})


# ================================================================== TOMO
def tomo():
    d = abrir('Tomo'); k = 'Tomo'
    R(d, k, *VERSION, 1, 'Identificación de la versión')
    R(d, k, '4.2 Proponé un nombre correcto para el libro de sueldos del estudio de este año y justificalo.',
      '4.2 Si el estudio quisiera llevar los sueldos de 2027 en un libro aparte, ¿qué nombre le pondrías? Justificalo.', 1,
      'R3-2-03 (O-2-01): en el caso, Sueldos es una hoja del libro Honorarios_Arandu_2026, no un libro propio')
    R(d, k, 'Es la puerta de entrada a las planillas que deciden.',
      'Es la puerta de entrada a las planillas que deciden. Con solo dos resultados posibles, este primer ejemplo también rotularía como SIMPLE a los clientes GENERAL; para tres categorías hace falta el SI anidado del párrafo siguiente.', 1,
      'R3-2-06 (O-2-04): el ejemplo de dos salidas no alcanza para tres categorías y conviene decirlo')
    for n in (1, 2):
        U.reemplazar_imagen(d, n, os.path.join(FIG, 'R3_Figura_%02d.png' % n), ANCHO)
    reg(k, 'Figuras 1 y 2 R2', 'Figuras 1 y 2 R3', 2,
        'R3-2-02 (O-2-05): ícono neutro en la Figura 1 · R3-2-04: la celda B3 de la Figura 2 muestra un régimen, no un importe')
    return d


# ================================================================== LABORATORIO
def lab(anchos=None, extra=None):
    anchos = anchos or {n: ANCHO for n in range(1, 14)}
    extra = extra or {}                 # {n.º de práctica: renglones de anotaciones adicionales}
    d = abrir('Laboratorio'); k = 'Laboratorio'
    R(d, k, *VERSION, 1, 'Identificación de la versión')
    R(d, k, '7. Escribí un párrafo breve, como si fuera la respuesta del estudio a un cliente, explicando desde cuándo debe emitir electrónicamente y cómo lo verifica.',
      '7. Escribí un párrafo breve, como si fuera la respuesta del estudio a un cliente, explicando desde cuándo debe emitir electrónicamente y cómo lo verifica: en el cronograma vigente del portal y en su buzón tributario Marandu.', 1,
      'R3-2-07: el punto de control exige mencionar el buzón tributario, pero ningún paso lo pedía')
    for n in range(1, 14):
        U.reemplazar_imagen(d, n, os.path.join(FIG, 'R3_Figura_%02d.png' % n), anchos[n])
    reg(k, 'Figuras a 12 cm (Práctica 10: 8 cm; Práctica 14: 9,5 cm): textos de 4,5 a 6,6 pt',
        'Figuras entre %.1f y 15,5 cm; ningún texto de figura por debajo de 7 pt (detalle por figura en LEGIBILIDAD_R3_2BTC.md)' % min(anchos.values()), 13,
        'R3-2-01: legibilidad; una práctica puede ocupar dos páginas antes que achicar la figura por debajo de 7 pt')
    restaurados = 0
    for prac in ('Práctica 10 ·', 'Práctica 14 ·'):
        ps = d.paragraphs
        i = next(j for j, p in enumerate(ps) if p.text.startswith(prac) and p.style.name.startswith('Heading'))
        j = next(j for j in range(i, len(ps)) if ps[j].text == 'Anotaciones')
        renglon = ps[j + 1]._p
        for _ in range(2):
            renglon.addnext(copy.deepcopy(renglon)); restaurados += 1
    reg(k, 'Prácticas 10 y 14 con un solo renglón de anotaciones', 'Tres renglones, como en las demás prácticas', restaurados,
        'R3-2-01: no se recorta espacio de trabajo para que la práctica entre en una página')
    n_extra = 0
    for p, cant in extra.items():
        ps = d.paragraphs
        i = next(j for j, q in enumerate(ps) if q.text.startswith('Práctica %d ·' % p) and q.style.name.startswith('Heading'))
        j = next(j for j in range(i, len(ps)) if ps[j].text == 'Anotaciones')
        renglon = ps[j + 1]._p
        for _ in range(cant):
            renglon.addnext(copy.deepcopy(renglon)); n_extra += 1
    if extra:
        reg(k, 'Prácticas %s: segunda página con solo el desafío y tres renglones' % ', '.join(map(str, sorted(extra))),
            'Renglones de anotaciones hasta el pie de esa página', n_extra,
            'R3-2-01: esas prácticas ocupan dos páginas para no bajar la figura de 7 pt; la segunda se usa como espacio de trabajo')
    return d


# ================================================================== PLAN ANUAL
def plan():
    d = abrir('Plan_anual')
    R(d, 'Plan_anual', *VERSION, 1, 'Identificación de la versión')
    return d


# ================================================================== SOLUCIONARIO
def sol():
    d = abrir('Solucionario'); k = 'Solucionario'
    R(d, k, *VERSION, 1, 'Identificación de la versión')
    R(d, k, '4.2 Debe decir contenido y período, p. ej. Sueldos_Arandu_2026;', '4.2 Debe decir contenido y período, p. ej. Sueldos_Arandu_2027;', 1,
      'R3-2-03: clave sincronizada con la nueva consigna')
    # Orientaciones duplicadas: se elimina el bloque breve (P4, P5, P9, P10, P14, P16, P17, P18), cuyo contenido ya está
    # completo en las orientaciones de las veinte prácticas, y ese bloque pasa a llevar el título de sección.
    ps = d.paragraphs
    i = next(j for j, p in enumerate(ps) if p.text == 'Orientaciones sobre los desafíos' and p.style.name.startswith('Heading'))
    j = next(j for j, p in enumerate(ps) if p.text == 'Orientaciones complementarias para los veinte desafíos')
    borrados = [p.text[:4] for p in ps[i + 1:j]]
    for p in ps[i + 1:j + 1]:
        p._p.getparent().remove(p._p)
    reg(k, 'Dos bloques de orientaciones de desafíos que se repetían (%s)' % ' '.join(borrados),
        'Un solo bloque «Orientaciones sobre los desafíos» con las veinte prácticas', len(borrados) + 1,
        'R3-2-05 (O-2-02): toda orientación eliminada figura con igual o mayor detalle en el bloque que queda')
    return d


# ================================================================== PLANES DE CLASE
def planes():
    d = abrir('Planes_de_clase'); k = 'Planes_de_clase'
    R(d, k, *VERSION, 1, 'Identificación de la versión')
    body = list(d.element.body.iterchildren())
    i = next(n for n, el in enumerate(body) if el.tag == qn('w:p') and
             ''.join(x.text or '' for x in el.iter(qn('w:t'))).startswith('Plan de Clase N.º 16 — ')
             and body[n + 1].tag == qn('w:tbl'))           # el título del plan, no su entrada en el índice
    tabs = [docx.table.Table(e, d._body) for e in body[i + 1:i + 9] if e.tag == qn('w:tbl')]
    hecho = 0
    for t in tabs:
        for r in t.rows:
            cs = list(U.celdas_unicas(r))
            if cs[0].text.strip() == 'Instrumentos' and 'Evaluación de la Unidad 3' in cs[1].text:
                U.poner_celda(cs[1], ['Lista de cotejo del armado de la hoja Resultado: vínculos entre hojas correctos y control cruzado de las tres cifras del informe. La Evaluación de la Unidad 3 se aplica en el encuentro siguiente (Plan 17).'])
                hecho += 1
    if hecho != 1:
        raise SystemExit('Plan 16: instrumento no encontrado')
    reg(k, 'Plan 16: instrumento «Evaluación de la Unidad 3», que se aplica en el Plan 17',
        'Plan 16: lista de cotejo de la hoja Resultado', 1, 'R3-2-08 (O-2-03): el instrumento corresponde a lo que se hace en ese encuentro')
    return d


def practicas_por_pagina(pdf):
    """{n.º de práctica: [páginas que ocupa]} a partir del texto del PDF (títulos «Práctica N ·» fuera del índice)."""
    import pymupdf
    pags = [p.get_text() for p in pymupdf.open(pdf)]
    ini = {}
    for i, t in enumerate(pags):
        if i < 3:
            continue
        for l in t.split('\n'):
            m = re.match(r'Práctica (\d+) · ', l.strip())
            if m and int(m.group(1)) not in ini:
                ini[int(m.group(1))] = i
    orden = sorted(ini.items(), key=lambda x: x[1])
    res = {}
    for j, (n, p) in enumerate(orden):
        fin = orden[j + 1][1] if j + 1 < len(orden) else len(pags)
        res[n] = list(range(p + 1, fin + 1))
    return res


def ajustar_laboratorio():
    """Busca, práctica por práctica, el ancho de figura más grande (paso 0,5 cm, nunca por debajo de ANCHO_MIN) con
    el que la práctica entra en una página. Si ni con el ancho mínimo entra, vuelve a 15,5 cm y la práctica ocupa dos
    páginas. La figura n de la práctica n (13 figuras en las prácticas 1, 2, 4, 5, 8, 10, 11, 13, 14, 16, 17, 19, 20)."""
    import docx as _d
    d = _d.Document(ruta('Laboratorio'))
    figura_de = {}                                    # n.º de práctica → n.º de figura, por orden en el cuerpo
    prac = None; nfig = 0
    for el in d.element.body.iterchildren():
        t = ''.join(x.text or '' for x in el.iter(qn('w:t')))
        m = re.match(r'Práctica (\d+) · ', t)
        if m and el.tag == qn('w:p') and 'Heading' in (el.find('.//' + qn('w:pStyle')).get(qn('w:val')) if el.find('.//' + qn('w:pStyle')) is not None else ''):
            prac = int(m.group(1))
        for _ in el.iter(qn('w:drawing')):
            nfig += 1; figura_de[prac] = nfig
    anchos = {n: ANCHO for n in range(1, 14)}
    fijas = set()
    for vuelta in range(12):
        U.REGISTRO_TMP = len(U.REGISTRO)
        lab(anchos).save(ruta('Laboratorio')); del U.REGISTRO[U.REGISTRO_TMP:]
        paginas = practicas_por_pagina(U.a_pdf(ruta('Laboratorio'), PDF))
        cambio = False
        for p, pags in paginas.items():
            f = figura_de.get(p)
            if len(pags) > 1 and f and f not in fijas:
                nuevo = round(anchos[f] - 0.5, 1)
                if nuevo >= ANCHO_MIN[f]:
                    anchos[f] = nuevo; cambio = True
                else:
                    anchos[f] = ANCHO; fijas.add(f)
                    cambio = True
        if not cambio:
            break
    n0 = len(U.REGISTRO); lab(anchos).save(ruta('Laboratorio')); del U.REGISTRO[n0:]
    paginas = practicas_por_pagina(U.a_pdf(ruta('Laboratorio'), PDF))
    # prácticas en dos páginas: se agregan renglones de anotaciones mientras no se cree una tercera página
    dobles = [p for p, pg in paginas.items() if len(pg) > 1]
    extra = {p: 0 for p in dobles}
    for paso in (16, 8, 4, 2, 1):
        for p in dobles:
            prueba = dict(extra); prueba[p] += paso
            n0 = len(U.REGISTRO); lab(anchos, prueba).save(ruta('Laboratorio')); del U.REGISTRO[n0:]
            pg = practicas_por_pagina(U.a_pdf(ruta('Laboratorio'), PDF))
            if len(pg[p]) == len(paginas[p]) and sum(map(len, pg.values())) == sum(map(len, paginas.values())):
                extra = prueba
    n0 = len(U.REGISTRO); lab(anchos, extra).save(ruta('Laboratorio')); del U.REGISTRO[n0:]
    paginas = practicas_por_pagina(U.a_pdf(ruta('Laboratorio'), PDF))
    globals()['EXTRA_LAB'] = extra
    json.dump({'anchos_cm': anchos, 'ancho_minimo_cm': ANCHO_MIN, 'paginas_por_practica': paginas,
               'figura_de_practica': figura_de},
              open(os.path.join(AQUI, 'ajuste_laboratorio_r3_2btc.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    return anchos


# ================================================================== construcción
CLAVE = lambda t: t.rstrip('…').strip()

if __name__ == '__main__':
    os.makedirs(R3, exist_ok=True); os.makedirs(PDF, exist_ok=True)
    docs = {'Tomo': tomo(), 'Plan_anual': plan(), 'Solucionario': sol(), 'Planes_de_clase': planes()}
    for k, d in docs.items():
        d.save(ruta(k))
    n0 = len(U.REGISTRO); lab().save(ruta('Laboratorio')); del U.REGISTRO[n0:]   # base para el ajuste
    anchos = ajustar_laboratorio()
    lab(anchos, EXTRA_LAB).save(ruta('Laboratorio'))           # versión final, la única registrada en la bitácora
    indices = {}
    for pasada in (1, 2):
        for k in ('Tomo', 'Laboratorio', 'Solucionario', 'Planes_de_clase'):
            pdf = U.a_pdf(ruta(k), PDF)
            d = docx.Document(ruta(k))
            indices[k] = U.recalcular_indice(d, pdf, clave=CLAVE)
            d.save(ruta(k))
    for k in SALIDA:
        U.a_pdf(ruta(k), PDF)
    json.dump({'cambios': U.REGISTRO, 'indices': indices}, open(os.path.join(AQUI, 'registro_r3_2btc.json'), 'w', encoding='utf8'),
              ensure_ascii=False, indent=1)
    print(len(U.REGISTRO), 'cambios registrados')
    for k, v in indices.items():
        print(k, 'entradas', len(v))

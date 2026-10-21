# -*- coding: utf-8 -*-
"""Equivalencia de los documentos anuales con los documentos aprobados de los seis lotes → coleccion/EQUIVALENCIA.json.

Cada documento se lee como una secuencia de bloques, en orden:
  - párrafo: estilo, texto, alineación, sangría, formato de cada tramo (negrita, cursiva, tamaño, color) e imágenes;
  - tabla: texto de cada celda, fila por fila, anchos de columna, sombreado de las celdas e imágenes.
Las imágenes se comparan por sus píxeles y por su tamaño en la página (las figuras se vuelven a generar con los scripts
de los lotes). No se comparan los párrafos vacíos ni las propiedades de paginación (saltos de página, «conservar con el
siguiente»), que son la diferencia D-03.

Segmentos que se comparan:
  - libro: los preliminares, las seis aperturas de unidad y los 18 capítulos, cada uno con el documento aprobado de su
    lote (lote 1: la candidata O3), después de aplicar al texto aprobado la lista cerrada de reemplazos (D-05 a D-11);
  - guía: cada parte con la guía aprobada de su lote, sin la portada; se admiten solo el título de la parte (D-13), las
    notas de integración de las Partes V y VI (D-14, D-15) y el número de página del diagnóstico (D-16);
  - cuaderno: cada práctica con la misma práctica del libro anual y con su versión aprobada (el cuaderno del lote o, para
    las Prácticas 1 a 3, el libro del lote 1).
Cualquier otra diferencia es un fallo. Uso: python3 -B coleccion/build/equivalencia.py   (sale con 1 si hay fallos)"""
import os, re, sys, json, hashlib, io, collections
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
COL = os.path.dirname(AQUI)
ADS = os.path.dirname(COL)
sys.path.insert(0, AQUI)
import docx
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from docx.table import Table
import fuentes as FU
import piezas_coleccion as PC
import diferencias_coleccion as DF

ANUAL = {'libro': os.path.join(COL, 'ADS_3BTI_LIBRO_ANUAL_ESTUDIANTE_OFICIO_O3.docx'),
         'guia': os.path.join(COL, 'ADS_3BTI_GUIA_DOCENTE_ANUAL_OFICIO_O3.docx'),
         'cuaderno': os.path.join(COL, 'ADS_3BTI_CUADERNO_ANUAL_PRACTICAS_OFICIO_O3.docx')}
_IMG = {}


def _imagenes(doc, el):
    out = []
    for blip in el.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}blip'):
        rid = blip.get(qn('r:embed'))
        blob = doc.part.related_parts[rid].blob
        k = hashlib.sha256(blob).hexdigest()
        if k not in _IMG:
            from PIL import Image
            im = Image.open(io.BytesIO(blob)).convert('RGBA')
            _IMG[k] = '%dx%d:%s' % (im.size[0], im.size[1], hashlib.sha256(im.tobytes()).hexdigest()[:16])
        out.append(_IMG[k])
    for ext in el.iter('{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}extent'):
        out.append('extent %s×%s' % (ext.get('cx'), ext.get('cy')))
    return out


def _fmt_run(r):
    c = r.font.color.rgb if r.font.color is not None and r.font.color.type is not None else None
    return (bool(r.bold), bool(r.italic), r.font.size.pt if r.font.size else None, str(c) if c else None, r.font.name)


def bloques(ruta):
    d = docx.Document(ruta)
    out = []
    for el in d.element.body.iterchildren():
        if el.tag == qn('w:p'):
            p = Paragraph(el, d)
            img = _imagenes(d, el)
            if not p.text.strip() and not img:
                continue
            pf = p.paragraph_format
            out.append({'k': 'p', 'st': p.style.name, 'tx': p.text, 'img': img,
                        'al': str(pf.alignment), 'sang': pf.left_indent.cm if pf.left_indent is not None else None,
                        'fmt': [_fmt_run(r) for r in p.runs if r.text]})
        elif el.tag == qn('w:tbl'):
            t = Table(el, d)
            filas = [[''.join(x.text or '' for x in tc.iter(qn('w:t'))) if False else '\n'.join(
                ''.join(x.text or '' for x in pp.iter(qn('w:t'))) for pp in tc.iter(qn('w:p'))) for tc in tr.findall(qn('w:tc'))]
                for tr in el.findall(qn('w:tr'))]
            anchos = [g.get(qn('w:w')) for g in el.find(qn('w:tblGrid')).findall(qn('w:gridCol'))]
            sombra = [s.get(qn('w:fill')) for s in el.iter(qn('w:shd'))]
            fmt = [_fmt_run(r) for tc in t._cells for pp in tc.paragraphs for r in pp.runs if r.text] if len(t.rows) < 80 else []
            out.append({'k': 't', 'filas': filas, 'anchos': anchos, 'sombra': sombra, 'img': _imagenes(d, el), 'fmt': fmt})
    return json.loads(json.dumps(out))   # tuplas como listas, igual en los dos lados de la comparación


def _texto(b):
    return b['tx'] if b['k'] == 'p' else (b['filas'][0][0] if b['filas'] and b['filas'][0] else '')


def _es_h1(b, pat):
    return b['k'] == 'p' and b['st'] == 'Heading 1' and re.match(pat, b['tx'])


def segmentos_libro(bs, con_prelim):
    """{nombre: [bloques]} — preliminares, aperturas de unidad y capítulos, cortados en los títulos de nivel 1."""
    cortes = []
    for i, b in enumerate(bs):
        m = _es_h1(b, r'^(Capítulo (\d+)|Unidad ([IVX]+)) — ')
        if m:
            cortes.append((i, 'Capítulo %s' % m.group(2) if m.group(2) else 'Apertura de la Unidad %s' % m.group(3)))
    out = {}
    if con_prelim:
        ini = next(i for i, b in enumerate(bs) if _es_h1(b, re.escape(FU.LOTES[1].P.TITULOS[0]) + '$'))
        out['Preliminares'] = bs[ini:cortes[0][0]]
    for k, (i, nombre) in enumerate(cortes):
        out[nombre] = bs[i:cortes[k + 1][0] if k + 1 < len(cortes) else len(bs)]
    return out


def segmento_practica(bs, titulo):
    """De «Práctica N — …» hasta la caja «Punto de control», inclusive."""
    ini = next(i for i, b in enumerate(bs) if b['k'] == 'p' and b['tx'] == titulo and b['st'].startswith('Heading'))
    fin = next(i for i in range(ini, len(bs)) if bs[i]['k'] == 't' and _texto(bs[i]).startswith('Punto de control'))
    return bs[ini:fin + 1]


def _transformar_aprobado(b):
    """Aplica al bloque aprobado la lista cerrada de reemplazos del libro (D-05 a D-11)."""
    b = json.loads(json.dumps(b))
    if b['k'] == 'p':
        b['tx'] = PC.reemplazar_texto(b['tx'])
    else:
        b['filas'] = [[PC.reemplazar_texto(c) for c in f] for f in b['filas']]
    return b


def comparar(nombre, aprobado, armado, transformar=True):
    if transformar:
        apl = [_transformar_aprobado(b) for b in aprobado]
        cambios = sum(1 for a, b in zip(aprobado, apl) if _textos(a) != _textos(b))
    else:
        apl, cambios = aprobado, 0
    difs = []
    for i in range(max(len(apl), len(armado))):
        a = apl[i] if i < len(apl) else None
        b = armado[i] if i < len(armado) else None
        if a != b:
            difs.append({'bloque': i + 1, 'aprobado': _resumen(a), 'armado': _resumen(b),
                         'campos': sorted(k for k in set(a or {}) | set(b or {}) if (a or {}).get(k) != (b or {}).get(k))})
    return {'segmento': nombre, 'bloques_aprobados': len(aprobado), 'bloques_armados': len(armado),
            'parrafos': sum(1 for x in armado if x['k'] == 'p'), 'tablas': sum(1 for x in armado if x['k'] == 't'),
            'imagenes': sum(len([y for y in x['img'] if not y.startswith('extent')]) for x in armado),
            'reemplazos_aplicados': cambios, 'identico': not difs, 'diferencias': difs[:6], 'n_diferencias': len(difs)}


def _textos(b):
    return b['tx'] if b['k'] == 'p' else b['filas']


def _resumen(b):
    if b is None:
        return None
    return ('párrafo [%s] %s' % (b['st'], b['tx'][:90])) if b['k'] == 'p' else ('tabla %d×%d «%s»' % (
        len(b['filas']), len(b['filas'][0]) if b['filas'] else 0, _texto(b)[:70]))


def ruta_aprobado(n, clave):
    r = FU.APROBADOS[n][clave]
    return os.path.join(ADS, r) if r else None


def main():
    FU.cargar()
    res = {'libro': [], 'guia': [], 'cuaderno': []}
    # ------------------------------------------------ libro
    anual = bloques(ANUAL['libro'])
    seg_anual = segmentos_libro(anual, True)
    for n in range(1, 7):
        seg_lote = segmentos_libro(bloques(ruta_aprobado(n, 'libro')), n == 1)
        for nombre, bs in seg_lote.items():
            res['libro'].append(dict(comparar(nombre, bs, seg_anual.get(nombre, [])), lote=n))
    esperados = {'Preliminares'} | {'Apertura de la Unidad %s' % u for u in FU.UNIDADES.values()} | {'Capítulo %d' % c for c in range(1, 19)}
    res['segmentos_libro'] = {'esperados': len(esperados), 'en_el_libro_anual': sorted(seg_anual) == sorted(esperados),
                              'comparados': sorted(r['segmento'] for r in res['libro']) == sorted(esperados)}
    # ------------------------------------------------ guía
    guia = bloques(ANUAL['guia'])
    partes = [i for i, b in enumerate(guia) if _es_h1(b, r'^Parte [IVX]+ — ')]
    for k, n in enumerate(range(1, 7)):
        ini, fin = partes[k], partes[k + 1] if k + 1 < len(partes) else len(guia)
        armado = guia[ini:fin]
        apr = bloques(ruta_aprobado(n, 'guia'))
        i0 = next(i for i, b in enumerate(apr) if _es_h1(b, re.escape(PC.ENCABEZADO_GUIA_LOTE % n) + '$'))
        apr = apr[i0:]
        titulo_ok = armado[0]['tx'] == PC.titulo_parte(n) and apr[0]['tx'] == PC.ENCABEZADO_GUIA_LOTE % n
        armado, apr = armado[1:], apr[1:]
        nota = None
        if n in PC.NOTAS_PARTE:
            nota = armado[0]
            nota_ok = nota['k'] == 't' and _texto(nota).startswith(PC.NOTAS_PARTE[n][0])
            armado = armado[1:]
        else:
            nota_ok = True
        norm = lambda bs: [dict(b, tx=re.sub(r'\(libro, pág\. \S+\)', '(libro, pág. N)', b['tx'])) if b['k'] == 'p' else b for b in bs]
        pag_diag = [b['tx'] for b in armado if b['k'] == 'p' and '(libro, pág.' in b['tx']]
        r = comparar('Parte %s' % FU.UNIDADES[n], norm(apr), norm(armado), transformar=False)
        r.update(lote=n, titulo_de_parte=titulo_ok, nota_de_integracion=(n in PC.NOTAS_PARTE) and nota_ok,
                 pagina_del_diagnostico=[re.search(r'pág\. (\S+)\)', t).group(1) for t in pag_diag])
        r['identico'] = r['identico'] and titulo_ok and nota_ok
        res['guia'].append(r)
    # ------------------------------------------------ cuaderno
    import armar_coleccion as AC
    cuad = bloques(ANUAL['cuaderno'])
    for n, C, _ in AC.practicas():
        t = C.PRACTICA_TITULO
        armado = segmento_practica(cuad, t)
        en_libro = segmento_practica(anual, t)
        if n == 1:
            apr = segmento_practica(bloques(ruta_aprobado(1, 'libro')), t)
        else:
            apr = segmento_practica(bloques(ruta_aprobado(n, 'cuaderno')), t)
        r1 = comparar(t, en_libro, armado, transformar=False)
        r2 = comparar(t, apr, armado)
        res['cuaderno'].append({'practica': t, 'lote': n, 'igual_al_libro_anual': r1['identico'],
                                'igual_a_la_version_aprobada': r2['identico'], 'bloques': r1['bloques_armados'],
                                'diferencias': r1['diferencias'] + r2['diferencias']})
    sin_eval = not any(b['k'] == 'p' and b['tx'].startswith('Evaluación del Capítulo') for b in cuad)
    res['cuaderno_sin_evaluaciones'] = sin_eval
    fallos = ([r['segmento'] for r in res['libro'] if not r['identico']] + [r['segmento'] for r in res['guia'] if not r['identico']]
              + [r['practica'] for r in res['cuaderno'] if not (r['igual_al_libro_anual'] and r['igual_a_la_version_aprobada'])])
    if not (res['segmentos_libro']['en_el_libro_anual'] and res['segmentos_libro']['comparados']):
        fallos.append('segmentos del libro')
    if not sin_eval:
        fallos.append('hay una evaluación en el cuaderno')
    res['fallos'] = fallos
    res['diferencias_autorizadas'] = DF.IDS
    json.dump(res, open(os.path.join(COL, 'EQUIVALENCIA.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    for r in res['libro']:
        print('%s libro   %-26s lote %d: %3d bloques (%d párrafos, %d tablas, %d imágenes)%s%s' % (
            'IGUAL ' if r['identico'] else 'DIFIERE', r['segmento'], r['lote'], r['bloques_armados'], r['parrafos'], r['tablas'],
            r['imagenes'], ' · reemplazos admitidos en %d bloques' % r['reemplazos_aplicados'] if r['reemplazos_aplicados'] else '',
            '' if r['identico'] else ' — %s' % r['diferencias'][:2]))
    for r in res['guia']:
        print('%s guía    %-26s lote %d: %3d bloques (%d párrafos, %d tablas, %d imágenes)%s%s' % (
            'IGUAL ' if r['identico'] else 'DIFIERE', r['segmento'], r['lote'], r['bloques_armados'], r['parrafos'], r['tablas'],
            r['imagenes'], ' · nota de integración' if r['nota_de_integracion'] else '',
            '' if r['identico'] else ' — %s' % r['diferencias'][:2]))
    for r in res['cuaderno']:
        print('%s cuaderno %-60s = libro anual: %s · = aprobada (lote %d): %s%s' % (
            'IGUAL ' if r['igual_al_libro_anual'] and r['igual_a_la_version_aprobada'] else 'DIFIERE', r['practica'][:60],
            r['igual_al_libro_anual'], r['lote'], r['igual_a_la_version_aprobada'], '' if not r['diferencias'] else ' — %s' % r['diferencias'][:2]))
    print('Cuaderno sin evaluaciones:', sin_eval)
    print('Resultado: %d segmentos del libro, %d partes de la guía y %d prácticas comparados; %d fallos'
          % (len(res['libro']), len(res['guia']), len(res['cuaderno']), len(fallos)))
    return 1 if fallos else 0


if __name__ == '__main__':
    sys.exit(main())

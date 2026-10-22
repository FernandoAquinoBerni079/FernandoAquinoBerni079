# -*- coding: utf-8 -*-
"""Lee los tres documentos aprobados de la colección v0.2 (commit 88c5cb5) y escribe planificacion/build/datos_coleccion.json.

No modifica nada de coleccion/: abre los DOCX para el texto y la estructura, y los PDF para las páginas impresas.
Todo lo que el plan anual y los planes de clase citan del libro, de la guía y del cuaderno sale de este archivo:
- del libro: ficha de cada capítulo (capacidades con su rótulo, tema, indicadores, tiempo), encuentros, secciones,
  conceptos clave, ejemplos resueltos, tablas, figuras, códigos, actividades, prácticas, evaluaciones, revisiones de
  hito, «Para repasar» y «Si el calendario se acorta», cada uno con su página;
- de la guía: la secuencia de cada encuentro (momento, tiempo y qué se hace), la tabla de instrumentos con su página y la
  página de cada sección;
- del cuaderno: la página de cada práctica.
Uso: python3 -B planificacion/build/extraer_coleccion.py
"""
import hashlib, json, os, re, sys
sys.dont_write_bytecode = True
import docx
import pymupdf
from docx.table import Table
from docx.text.paragraph import Paragraph

AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(os.path.dirname(os.path.dirname(AQUI)))
CUADERNO_V1 = os.path.join(ADS, 'edicion_v1_0', 'salida', 'ADS_3BTI_CUADERNO_DE_PRACTICAS_v1_0.pdf')
COL = os.path.join(ADS, 'coleccion')
DOC = {'libro': 'ADS_3BTI_LIBRO_ANUAL_ESTUDIANTE_OFICIO_O3', 'guia': 'ADS_3BTI_GUIA_DOCENTE_ANUAL_OFICIO_O3',
       'cuaderno': 'ADS_3BTI_CUADERNO_ANUAL_PRACTICAS_OFICIO_O3'}
norm = lambda s: re.sub(r'\s+', ' ', s or '').strip()
ROMANOS = ['I', 'II', 'III', 'IV', 'V', 'VI']


def huella(ruta):
    return hashlib.sha256(open(ruta, 'rb').read()).hexdigest()


def elementos(d):
    """Párrafos y tablas del cuerpo, en orden."""
    for el in d.element.body.iterchildren():
        tag = el.tag.split('}')[1]
        if tag == 'p':
            yield 'p', Paragraph(el, d)
        elif tag == 'tbl':
            yield 't', Table(el, d)


class Paginas:
    """Busca en qué página impresa aparece un texto, a partir de una página dada."""
    def __init__(self, ruta):
        self.pdf = pymupdf.open(ruta)
        self.txt = [norm(p.get_text()) for p in self.pdf]

    def de(self, texto, desde=1, hasta=None):
        t = norm(texto)
        for i in range(desde - 1, hasta or len(self.txt)):
            if t in self.txt[i]:
                return i + 1
        return None


def primera_oracion(t, maximo=260):
    t = norm(t)
    m = re.match(r'(.+?[.?!])(\s|$)', t)
    s = m.group(1) if m else t
    return s if len(s) <= maximo else s[:maximo].rsplit(' ', 1)[0] + '…'


# ---------------------------------------------------------------- libro
def libro():
    d = docx.Document(os.path.join(COL, DOC['libro'] + '.docx'))
    pg = Paginas(os.path.join(COL, DOC['libro'] + '.pdf'))
    rc = json.load(open(os.path.join(COL, 'resultado_construccion.json'), encoding='utf8'))
    indice = rc['indice_libro']
    pag_indice = {t: p for t, p in indice}
    caps, cap, enc, bloque = {}, None, None, None
    categoria = None
    en_cuerpo = False
    for tipo, x in elementos(d):
        if tipo == 'p':
            t, st = x.text, x.style.name
            if st == 'Heading 1' and t.startswith('Capítulo 1 —'):
                en_cuerpo = True
            if not en_cuerpo or not t.strip():
                continue
            m = re.match(r'Capítulo (\d+) — (.+)', t)
            if st == 'Heading 1' and m:
                n = int(m.group(1))
                cap = caps[n] = {'num': n, 'titulo': m.group(2), 'pagina': pag_indice[t], 'encuentros': [], 'practica': None,
                                 'evaluacion': None, 'hito': None, 'repaso': [], 'calendario': [], 'conexion': []}
                enc = bloque = None
                continue
            m = re.match(r'Encuentro (\d+) — (.+)', t)
            if st == 'Heading 1' and m:
                enc = {'num': int(m.group(1)), 'titulo': m.group(2), 'pagina': pag_indice[t], 'secciones': [], 'conceptos': [],
                       'ejemplos': [], 'tablas': [], 'figuras': [], 'codigos': [], 'actividades': [], 'otros': []}
                cap['encuentros'].append(enc); bloque = enc; categoria = None
                continue
            if st == 'Heading 1' and t.startswith('Práctica '):
                cap['practica'] = {'titulo': t, 'pagina': pag_indice[t], 'niveles': []}
                bloque = cap['practica']
                continue
            if st.startswith('Heading') and t.startswith(('Revisión de la Unidad', 'Evaluación integradora', 'Hito H')):
                cap['hito'] = {'titulo': t, 'pagina': pag_indice[t], 'encuentro': enc['num'] if enc else None}
                continue
            if st.startswith('Heading') and t.startswith('Evaluación del Capítulo'):
                cap['evaluacion'] = {'titulo': t, 'pagina': pag_indice[t]}
                bloque = None
                continue
            if st == 'Heading 2' and re.match(r'\d+\.\d+ ', t) and enc:
                enc['secciones'].append({'titulo': t, 'pagina': pag_indice.get(t)})
                continue
            if st == 'Heading 3' and t.startswith('Nivel') and bloque is cap.get('practica'):
                cap['practica']['niveles'].append(t)
                continue
            if st == 'Heading 3' and t.startswith('Actividades del Encuentro'):
                enc['pagina_actividades'] = pg.de(t, enc['pagina'])
                categoria = ''
                continue
            if enc is None or bloque is not enc:
                continue
            m = re.match(r'(Tabla|Figura|Código) (\d+\.\d+) — (.+)', t)
            if m:
                clave = {'Tabla': 'tablas', 'Figura': 'figuras', 'Código': 'codigos'}[m.group(1)]
                enc[clave].append({'id': '%s %s' % (m.group(1), m.group(2)), 'titulo': norm(m.group(3)),
                                   'pagina': pg.de('%s %s — %s' % (m.group(1), m.group(2), m.group(3)[:40]), enc['pagina'])})
                continue
            if categoria is not None:
                if t in ('Ejercitá', 'Resolvé', 'Pensá y decidí', 'Desafío'):
                    categoria = t
                    continue
                m = re.match(r'(\d+)\. (.+)', t)
                if m:
                    enc['actividades'].append({'num': int(m.group(1)), 'tipo': categoria, 'consigna': primera_oracion(m.group(2))})
        else:
            if not en_cuerpo or cap is None:
                continue
            primera = x.rows[0].cells[0].text
            linea = primera.split('\n')[0]
            if primera.startswith(('Capacidades propuestas', 'Capacidad propuesta')) and len(x.columns) == 2:
                cap['ficha'] = {'rotulo_capacidad': primera, 'capacidad': x.rows[0].cells[1].text}
                for r in x.rows[1:]:
                    k = r.cells[0].text
                    v = r.cells[1].text
                    if k.startswith('Indicador'):
                        cap['ficha']['indicadores'] = [norm(i.lstrip('•')) for i in v.split('\n') if i.strip()]
                    else:
                        cap['ficha'][k.lower()] = v
                continue
            if len(x.columns) != 1:
                continue
            cuerpo = [norm(c.text) for r in x.rows for c in r.cells]
            if linea.startswith('Para repasar'):
                cap['repaso'] = [norm(primera.split('\n', 1)[1])] + cuerpo[1:] if '\n' in primera else cuerpo[1:]
                cap['pagina_repaso'] = pg.de(cap['repaso'][0][:50], cap['encuentros'][-1]['pagina'])
            elif linea.startswith('Si el calendario se acorta'):
                cap['calendario'] = [norm(primera.split('\n', 1)[1])] + cuerpo[1:] if '\n' in primera else cuerpo[1:]
                cap['pagina_calendario'] = pg.de(cap['calendario'][0][:50], cap['encuentros'][-1]['pagina'])
            elif linea.startswith('Con qué se conecta'):
                cap['conexion'] = cuerpo
            elif enc is not None and bloque is enc:
                if linea.startswith('Concepto clave — '):
                    defin = primera.split('\n', 1)[1] if '\n' in primera else ''
                    enc['conceptos'].append({'titulo': linea[len('Concepto clave — '):], 'definicion': norm(defin),
                                             'pagina': pg.de(linea, enc['pagina'])})
                elif linea.startswith('Ejemplo resuelto'):
                    enc['ejemplos'].append({'titulo': norm(linea), 'pagina': pg.de(linea[:45], enc['pagina'])})
                elif linea.startswith(('Estado del entorno', 'Antes de presentar', 'Antes de relevar', 'En Paraguay')):
                    enc['otros'].append({'titulo': norm(linea), 'pagina': pg.de(linea[:40], enc['pagina'])})
    # páginas finales de cada encuentro: hasta la página anterior al siguiente elemento del índice que no sea una sección
    orden = [(t, p) for t, p in indice]
    for n, c in caps.items():
        for e in c['encuentros']:
            k = next(i for i, (t, _) in enumerate(orden) if t.startswith('Encuentro %d —' % e['num']))
            sig = next(((t, p) for t, p in orden[k + 1:] if not re.match(r'\d+\.\d+ ', t)
                        and not t.startswith(('Revisión de la Unidad', 'Evaluación integradora', 'Hito H'))), None)
            e['pagina_fin'] = max(e['pagina'], sig[1] - 1 if sig and sig[1] > e['pagina'] else (sig[1] if sig else e['pagina']))
        if c['practica']:
            k = next(i for i, (t, _) in enumerate(orden) if t == c['practica']['titulo'])
            sig = orden[k + 1] if k + 1 < len(orden) else None
            c['practica']['pagina_fin'] = sig[1] - 1 if sig and sig[1] > c['practica']['pagina'] else c['practica']['pagina']
        if c['evaluacion']:
            k = next(i for i, (t, _) in enumerate(orden) if t == c['evaluacion']['titulo'])
            sig = orden[k + 1] if k + 1 < len(orden) else None
            c['evaluacion']['pagina_fin'] = sig[1] - 1 if sig and sig[1] > c['evaluacion']['pagina'] else c['evaluacion']['pagina']
    unidades = [{'num': ROMANOS.index(m.group(1)) + 1, 'titulo': m.group(2), 'pagina': p}
                for t, p in indice for m in [re.match(r'Unidad (I|II|III|IV|V|VI) — (.+)', t)] if m]
    prelim = [{'titulo': t, 'pagina': p} for t, p in indice[:indice.index(next(x for x in indice if x[0].startswith('Unidad I —')))]]
    return {'capitulos': [caps[n] for n in sorted(caps)], 'unidades': unidades, 'preliminares': prelim,
            'paginas': len(pg.txt)}


# ---------------------------------------------------------------- guía
REFERENCIAS_GUIA = [
    ('acuerdo_algoritmica', 'Antes del Encuentro 13: acuerdo con Algorítmica 3.º', 'Parte III'),
    ('laboratorio_iv', '0.1 Coordinación con Laboratorio', 'Parte IV'),
    ('ficha_entorno', '0.2 Prueba de campo y ficha de entorno', 'Parte IV'),
    ('otro_entorno', '0.3 Si el entorno de referencia no funciona', 'Parte IV'),
    ('concurrencia', '0.4 Protocolo de concurrencia para Windows', 'Parte IV'),
    ('distribuciones', '0.5 Las dos distribuciones de la base de proyecto', 'Parte IV'),
    ('nota_e30', 'Nota de integración: preparación del Encuentro 30 y conjunto reservado', 'Parte V'),
    ('copias', '0.1 Las copias descartables y el cargador DP', 'Parte V'),
    ('dr', '0.2 El conjunto reservado DR (exclusivo del docente)', 'Parte V'),
    ('laboratorio_v', '0.3 Coordinación con Laboratorio y sesiones de uso', 'Parte V'),
    ('codigo_recibido', 'Nota de integración: pruebas de código recibido de otros', 'Parte VI'),
    ('paquete_modelo', '0.1 El paquete de entrega modelo y las herramientas del docente', 'Parte VI'),
    ('licencias', '0.2 Licencias y procedencia (borrador)', 'Parte VI'),
    ('instalacion_otro', '0.3 La instalación por otro equipo', 'Parte VI'),
    ('mbokaja_p17', '0.4 El paquete de Mbokaja de la Práctica 17', 'Parte VI'),
    ('variantes', '0.5 Variantes reservadas para la defensa individual', 'Parte VI'),
    ('tiempos_e35', '0.6 Preparación y tiempos del Encuentro 35', 'Parte VI'),
    ('alternativas_e35', 'Alternativas para el Encuentro 35', 'Parte VI'),
    ('mapa_apoyos', 'Mapa de apoyos del curso (modelo)', 'Parte I'),
    ('coordinacion_i', 'Coordinación con otras asignaturas', 'Parte I'),
]


def guia():
    d = docx.Document(os.path.join(COL, DOC['guia'] + '.docx'))
    pg = Paginas(os.path.join(COL, DOC['guia'] + '.pdf'))
    rc = json.load(open(os.path.join(COL, 'resultado_construccion.json'), encoding='utf8'))
    previo, secuencias, parte = None, {}, None
    tablas = {'claves_encuentro': {}, 'cotejo': {}, 'evidencias_hito': {}, 'rubrica': {}, 'errores_capitulo': {}}
    patrones = [('claves_encuentro', r'Claves de las actividades del Encuentro (\d+)$'),
                ('cotejo', r'Lista de cotejo de la Práctica (\d+)$'),
                ('evidencias_hito', r'Evidencias de cada criterio(?: del H(\d))?$'),
                ('rubrica', r'Rúbrica del H(\d): descriptores por nivel$'),
                ('errores_capitulo', r'Errores frecuentes del Capítulo (\d+)$')]
    desde = 1
    for tipo, x in elementos(d):
        if tipo == 'p':
            if x.text.strip():
                previo = x.text
            m = re.match(r'Parte (I|II|III|IV|V|VI) — ', x.text)
            if m and x.style.name.startswith('Heading'):
                parte = m.group(1)
            continue
        for clave, pat in patrones:
            m = re.match(pat, previo or '')
            if m:
                n = int(m.group(1)) if m.group(1) else 1   # la tabla del H1 no lleva número en su rótulo
                pagina = pg.de(previo, desde)
                desde = pagina or desde
                tablas[clave][n] = {'rotulo': previo, 'pagina': pagina, 'parte': parte,
                                    'filas': [[norm(c.text) for c in r.cells] for r in x.rows[1:]]}
        if previo and previo.startswith('Encuentro ') and [c.text for c in x.rows[0].cells] == ['Momento', 'Tiempo', 'Qué se hace']:
            m = re.match(r'Encuentro (\d+) — (.+?) \((.+)\)$', previo)
            n = int(m.group(1))
            secuencias[n] = {'num': n, 'titulo': m.group(2), 'hc': m.group(3), 'parte': parte, 'rotulo': previo,
                             'pagina': pg.de(previo[:60]),
                             'momentos': [{'momento': r.cells[0].text, 'tiempo': r.cells[1].text, 'que_se_hace': norm(r.cells[2].text)}
                                          for r in x.rows[1:]]}
    # secciones previas de cada parte que citan los planes (no figuran en el índice de dos niveles)
    referencias = {}
    for clave, texto, desde_titulo in REFERENCIAS_GUIA:
        desde_p = next(p for t, p in rc['indice_guia'] if t.startswith(desde_titulo))
        referencias[clave] = {'texto': texto, 'pagina': pg.de(texto, desde_p)}
    return {'secuencias': [secuencias[n] for n in sorted(secuencias)], 'instrumentos': rc['instrumentos_guia'],
            'referencias': referencias,
            'tablas': {k: {str(n): v for n, v in sorted(t.items())} for k, t in tablas.items()},
            'indice': rc['indice_guia'], 'paginas': len(pg.txt)}


# ---------------------------------------------------------------- cuaderno
def cuaderno():
    rc = json.load(open(os.path.join(COL, 'resultado_construccion.json'), encoding='utf8'))
    # edición v1.0: el cuaderno tiene renglones de 8 mm y otra paginación; las páginas se leen de su PDF
    pg = Paginas(CUADERNO_V1)
    indice, pend = [], []
    for t, _ in rc['indice_cuaderno']:
        if t.startswith('Práctica'):
            p = pg.de(t[:50], 3)
            indice += [[u, p] for u in pend] + [[t, p]]; pend = []
        else:
            pend.append(t)
    return {'indice': indice, 'paginas': len(pg.txt), 'pdf': os.path.relpath(CUADERNO_V1, ADS)}


if __name__ == '__main__':
    datos = {'fuente': {'commit_base': '88c5cb5', 'documentos': {k: {f: huella(os.path.join(COL, v + f)) for f in ('.docx', '.pdf')}
                                                                for k, v in DOC.items()},
                        'cuaderno_v1_0': huella(CUADERNO_V1)},
             'libro': libro(), 'guia': guia(), 'cuaderno': cuaderno()}
    json.dump(datos, open(os.path.join(AQUI, 'datos_coleccion.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    L = datos['libro']
    print('capítulos %d · encuentros %d · secuencias %d · instrumentos %d' % (
        len(L['capitulos']), sum(len(c['encuentros']) for c in L['capitulos']), len(datos['guia']['secuencias']),
        len(datos['guia']['instrumentos'])))

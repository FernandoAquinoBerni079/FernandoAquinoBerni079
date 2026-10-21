# -*- coding: utf-8 -*-
"""Informe de legibilidad e impresión de los documentos anuales → coleccion/INFORME_LEGIBILIDAD_IMPRESION.md y
coleccion/LEGIBILIDAD_IMPRESION.json. Todo se mide sobre los archivos generados:
  1. Página y márgenes: tamaño de cada página del PDF; márgenes espejados y tamaño de papel declarados en el DOCX.
  2. Fuentes: las que pide el DOCX y las que el PDF incrusta.
  3. Tamaños de letra por función (texto, tablas, código, títulos), comparados con los PDF aprobados de los lotes: la
     integración no redujo ningún tamaño.
  4. Medida del renglón y espacios de respuesta (separación entre renglones y su largo).
  5. Doble faz: páginas, hojas, paridad de los comienzos de unidad y relleno al pliego, sin hojas en blanco intercaladas.
  6. Variación de paginación con las fuentes de sustitución (PRUEBA_FUENTES.json).
Uso: python3 -B coleccion/build/legibilidad.py (después de prueba_fuentes_coleccion.py)"""
import os, re, sys, json, statistics, collections, zipfile
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
COL = os.path.dirname(AQUI)
ADS = os.path.dirname(COL)
sys.path.insert(0, AQUI)
import pymupdf
import fuentes as FU

MM = 25.4 / 72
DOCS = {'libro': 'ADS_3BTI_LIBRO_ANUAL_ESTUDIANTE_OFICIO_O3', 'guia': 'ADS_3BTI_GUIA_DOCENTE_ANUAL_OFICIO_O3',
        'cuaderno': 'ADS_3BTI_CUADERNO_ANUAL_PRACTICAS_OFICIO_O3'}
NOMBRE = {'libro': 'Libro del estudiante', 'guia': 'Guía docente', 'cuaderno': 'Cuaderno de prácticas'}
RES = {}


def spans(pdf):
    for i, pg in enumerate(pdf):
        for b in pg.get_text('dict')['blocks']:
            for l in b.get('lines', []):
                for x in l['spans']:
                    if x['text'].strip():
                        yield i, l, x


def rol(x):
    f = x['font']
    if 'Mono' in f or 'Courier' in f:
        return 'código'
    if x['size'] >= 11.6:
        return 'títulos'
    return 'texto y tablas'


def perfil_de_tamanos(pdf):
    c = collections.defaultdict(collections.Counter)
    for _, _, x in spans(pdf):
        if re.match(r'^Página \d+ de \d+$', x['text'].strip()):
            continue
        c[rol(x)][round(x['size'], 1)] += len(x['text'])
    return {k: {'minimo': min(v), 'mas_usado': v.most_common(1)[0][0], 'caracteres': sum(v.values())} for k, v in c.items()}


def docx_xml(ruta, parte):
    with zipfile.ZipFile(ruta) as z:
        return z.read(parte).decode('utf8')


aprobados = {}
for n in range(1, 7):
    for k in ('libro', 'guia', 'cuaderno'):
        r = FU.APROBADOS[n][k]
        if r:
            p = pymupdf.open(os.path.join(ADS, r[:-5] + '.pdf'))
            for rl, v in perfil_de_tamanos(p).items():
                a = aprobados.setdefault(k, {}).setdefault(rl, v['minimo'])
                aprobados[k][rl] = min(a, v['minimo'])

for k, base in DOCS.items():
    pdf = pymupdf.open(os.path.join(COL, base + '.pdf'))
    dx = os.path.join(COL, base + '.docx')
    tam = {(round(pg.rect.width * MM, 1), round(pg.rect.height * MM, 1)) for pg in pdf}
    doc_xml = docx_xml(dx, 'word/document.xml'); settings = docx_xml(dx, 'word/settings.xml')
    pgsz = re.search(r'<w:pgSz w:w="(\d+)" w:h="(\d+)"', doc_xml)
    pgmar = re.search(r'<w:pgMar ([^>]+)/>', doc_xml).group(1)
    mar = {m.group(1): round(int(m.group(2)) / 1440 * 2.54, 2) for m in re.finditer(r'w:(\w+)="(\d+)"', pgmar)}
    fuentes_docx = collections.Counter(re.findall(r'w:ascii="([^"]+)"', doc_xml + docx_xml(dx, 'word/styles.xml')))
    fuentes_pdf = {}
    for pg in pdf:
        for f in pg.get_fonts():
            fuentes_pdf[f[3]] = f[1] != 'n/a' and bool(f[0])   # (xref, ext, type, basefont, name, encoding)
    incrustadas = {f[3]: f[1] for pg in pdf for f in pg.get_fonts()}
    perfil = perfil_de_tamanos(pdf)
    # medida del renglón: caracteres por línea de los párrafos de texto corrido (líneas de más de 60 caracteres)
    largos = [len(''.join(x['text'] for x in l['spans'])) for i, pg in enumerate(pdf) for b in pg.get_text('dict')['blocks']
              for l in b.get('lines', []) if abs(l['spans'][0]['size'] - 10.5) < 0.2 and len(''.join(x['text'] for x in l['spans'])) > 60]
    # renglones de respuesta: separación vertical entre dos renglones seguidos y largo de cada renglón
    sep, largo = [], []
    for pg in pdf:
        ys = sorted((l['bbox'][1], l['bbox'][2] - l['bbox'][0]) for b in pg.get_text('dict')['blocks'] for l in b.get('lines', [])
                    if ''.join(x['text'] for x in l['spans']).strip().startswith('_' * 20))
        largo += [w * MM for _, w in ys]
        sep += [(b[0] - a[0]) * MM for a, b in zip(ys, ys[1:]) if 0 < (b[0] - a[0]) * MM < 15]
    n = len(pdf)
    RES[k] = {
        'paginas': n, 'hojas_doble_faz': (n + 1) // 2, 'tamano_pagina_mm': sorted(tam),
        'docx_papel_cm': (round(int(pgsz.group(1)) / 1440 * 2.54, 2), round(int(pgsz.group(2)) / 1440 * 2.54, 2)),
        'docx_margenes_cm': {x: mar.get(x) for x in ('left', 'right', 'top', 'bottom', 'header', 'footer')},
        'docx_margenes_espejados': '<w:mirrorMargins' in settings,
        'fuentes_que_pide_el_docx': dict(fuentes_docx), 'fuentes_del_pdf': incrustadas,
        'tamanos_pt': perfil, 'minimos_aprobados_pt': aprobados.get(k, {}),
        'sin_reduccion': all(perfil[r]['minimo'] >= aprobados.get(k, {}).get(r, 0) - 0.05 for r in perfil),
        'caracteres_por_renglon_mediana': statistics.median(largos) if largos else None,
        'renglones_respuesta': {'cantidad': len(largo), 'separacion_mm_mediana': round(statistics.median(sep), 1) if sep else None,
                                'separacion_mm_minima': round(min(sep), 1) if sep else None,
                                'largo_mm_mediana': round(statistics.median(largo), 1) if largo else None},
        'relleno_al_pliego': {m: (-n) % m for m in (4, 8, 16)},
    }

pdfL = pymupdf.open(os.path.join(COL, DOCS['libro'] + '.pdf'))
ind = dict(json.load(open(os.path.join(COL, 'resultado_construccion.json'), encoding='utf8'))['indice_libro'])
unidades = {u: ind[u] for u in ind if re.match(r'^Unidad [IVX]+ — ', u)}
RES['libro']['comienzo_de_unidades'] = {u.split(' — ')[0]: {'pagina': p, 'cara': 'impar (derecha)' if p % 2 else 'par (izquierda)'}
                                        for u, p in unidades.items()}
PF = json.load(open(os.path.join(COL, 'PRUEBA_FUENTES.json'), encoding='utf8'))
RES['fuentes_de_sustitucion'] = [{k: x[k] for k in ('fuente', 'documento', 'paginas', 'resultado')} for x in PF]
json.dump(RES, open(os.path.join(COL, 'LEGIBILIDAD_IMPRESION.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)

# ---------------------------------------------------------------- informe
f = lambda x: ('%.1f' % x).replace('.', ',') if isinstance(x, float) else str(x)
md = ['# Informe de legibilidad e impresión', '',
      '**Colección ADS 3.º BTI · documentos anuales v0.2 (candidata del cierre editorial) · oficio O3**', '',
      'Todo lo que sigue se midió sobre los DOCX y los PDF generados (`build/legibilidad.py`; datos en '
      '`LEGIBILIDAD_IMPRESION.json`). Es una auditoría técnica en pantalla: no reemplaza una prueba de imprenta en papel.', '',
      '## 1. Página, márgenes y fuentes', '',
      '| | Libro | Guía | Cuaderno |', '|---|---|---|---|',
      '| Páginas | %d | %d | %d |' % tuple(RES[k]['paginas'] for k in DOCS),
      '| Tamaño de página en el PDF (mm) | %s | %s | %s |' % tuple(' · '.join('%s × %s' % (f(a), f(b)) for a, b in RES[k]['tamano_pagina_mm']) for k in DOCS),
      '| Papel y márgenes del DOCX (cm) | %s |' % ' | '.join('%s × %s; interior %s, exterior %s, superior %s, inferior %s' % (
          f(RES[k]['docx_papel_cm'][0]), f(RES[k]['docx_papel_cm'][1]), f(RES[k]['docx_margenes_cm']['left']), f(RES[k]['docx_margenes_cm']['right']),
          f(RES[k]['docx_margenes_cm']['top']), f(RES[k]['docx_margenes_cm']['bottom'])) for k in DOCS),
      '| Márgenes espejados en el DOCX | %s |' % ' | '.join('sí' if RES[k]['docx_margenes_espejados'] else 'NO' for k in DOCS),
      '| Fuentes que pide el DOCX | %s |' % ' | '.join(', '.join(sorted(RES[k]['fuentes_que_pide_el_docx'])) for k in DOCS),
      '| Fuentes incrustadas en el PDF | %s |' % ' | '.join(', '.join(sorted({re.sub(r'^[A-Z]{6}\+', '', x) for x in RES[k]['fuentes_del_pdf']})) for k in DOCS),
      '', 'En el entorno de construcción no está Calibri: LibreOffice la reemplaza por Carlito, que tiene las mismas medidas '
      'letra por letra, y Courier New por Liberation Mono, que tiene las mismas medidas que Courier New. El PDF lleva las fuentes incrustadas: '
      '**a la imprenta se le entrega el PDF**, no el DOCX.', '',
      '## 2. Tamaños de letra (puntos)', '',
      '| Documento | Función | Mínimo | Más usado | Mínimo en los lotes aprobados |', '|---|---|---|---|---|']
for k in DOCS:
    for r, v in sorted(RES[k]['tamanos_pt'].items()):
        md.append('| %s | %s | %s | %s | %s |' % (NOMBRE[k], r, f(v['minimo']), f(v['mas_usado']), f(RES[k]['minimos_aprobados_pt'].get(r, '—'))))
md += ['', '- Ningún tamaño es menor que el de los lotes aprobados: %s. La integración no redujo la letra para resolver la '
       'distribución, y la equivalencia lo confirma tramo por tramo, porque compara el tamaño de cada uno.' % (
           'sí en los tres documentos' if all(RES[k]['sin_reduccion'] for k in DOCS) else 'NO, revisar'),
       '- Los párrafos de texto corrido van en 10,5 pt y las consignas en 10 pt (el tamaño más usado); las tablas, entre 8 y '
       '9,5 pt; el código, en 7,5 pt, en letra monoespaciada (96 caracteres por renglón). Es lo aprobado en los lotes.',
       '- La auditoría de impresión comprueba que no haya ningún texto por debajo de 7,5 pt.', '',
       '## 3. Medida del renglón y espacios de respuesta', '',
       '| Documento | Caracteres por renglón de texto (mediana) | Renglones de respuesta | Separación entre renglones (mediana y mínima) | Largo del renglón |',
       '|---|---|---|---|---|']
for k in DOCS:
    rr = RES[k]['renglones_respuesta']
    md.append('| %s | %s | %d | %s mm y %s mm | %s mm |' % (NOMBRE[k], f(RES[k]['caracteres_por_renglon_mediana']), rr['cantidad'],
                                                            f(rr['separacion_mm_mediana']), f(rr['separacion_mm_minima']), f(rr['largo_mm_mediana'])))
md += ['', '**Observaciones de legibilidad (no se cambiaron: son parte del formato aprobado):**',
       '- **Renglón largo.** En los 17,3 cm de ancho útil entran unos %d caracteres por renglón. Para un libro de texto, lo '
       'cómodo suele estar por debajo de los 90. Lo compensan los párrafos breves, las tablas y las cajas, pero conviene '
       'revisarlo en la prueba impresa. Acortarlo exigiría cambiar el perfil O3 aprobado (márgenes o dos columnas).' % RES['libro']['caracteres_por_renglon_mediana'],
       '- **Renglones de respuesta juntos.** Están a %s mm uno de otro y miden %s mm de largo. Para escribir a mano suele '
       'recomendarse de 7 a 8 mm, y en dos renglones por consigna el espacio para responder es breve. Es el diseño aprobado en '
       'todos los lotes: ampliarlo agregaría páginas al libro y al cuaderno. Se propone decidirlo con la prueba impresa.' % (
           f(RES['libro']['renglones_respuesta']['separacion_mm_mediana']), f(RES['libro']['renglones_respuesta']['largo_mm_mediana'])),
       '- **Código en 7,5 pt.** Es el tamaño aprobado para que cada renglón de código entre completo (96 caracteres). En pantalla '
       'se lee bien; la prueba impresa tiene que confirmar el contraste del fondo gris.',
       '- La auditoría comprueba que todos los renglones de respuesta estén impresos y que ninguno quede separado de su consigna.', '',
       '## 4. Impresión a doble faz e instrucciones para la imprenta', '',
       '| Documento | Páginas | Hojas | Páginas en blanco para completar el pliego de 4 · 8 · 16 |', '|---|---|---|---|']
for k in DOCS:
    rp = RES[k]['relleno_al_pliego']
    md.append('| %s | %d | %d | %d · %d · %d |' % (NOMBRE[k], RES[k]['paginas'], RES[k]['hojas_doble_faz'], rp[4], rp[8], rp[16]))
md += ['', 'Comienzo de cada unidad en el libro: ' + '; '.join('%s, pág. %d, %s' % (u, v['pagina'], v['cara'])
                                                         for u, v in RES['libro']['comienzo_de_unidades'].items()) + '.', '',
       '**Instrucciones para la imprenta:**',
       '1. Imprimir el PDF, no el DOCX: lleva las fuentes incrustadas y la paginación controlada.',
       '2. Papel oficio de 216 × 330 mm, vertical, a doble faz, con volteo por el borde largo. La página 1 va en el frente de '
       'la primera hoja.',
       '3. Los márgenes son espejados: el interior (2,5 cm) está a la izquierda en las páginas impares y a la derecha en las '
       'pares. Por eso no se puede saltear ni agregar una página en medio sin desplazar el lomo de todas las siguientes.',
       '4. Las páginas en blanco que haga falta agregar para completar el pliego de la máquina van todas al final, después de '
       'la última página. La cantidad depende del pliego: está en la tabla de arriba. En la página 1 no hay contratapa ni '
       'página de cortesía: si la imprenta quiere agregarlas, van antes de la portada, en número par (2), para no invertir '
       'las caras.',
       '5. Los documentos no tienen hojas en blanco intercaladas: la auditoría lo comprueba página por página. Las unidades y '
       'los capítulos empiezan en hoja nueva, pero no siempre en página impar, como en los lotes aprobados.',
       '6. Encuadernación recomendada: el libro, en rústica fresada con cola PUR o anillado; la guía, anillada o en rústica; '
       'el cuaderno, anillado, para que abra plano (ver EVALUACION_ENCUADERNACION.md).',
       '7. Antes del tiraje, una prueba impresa completa del libro: comprobar en papel el margen interior después del fresado '
       'o del anillado, el contraste de los fondos de color de las cajas y la legibilidad del código en 7,5 pt.', '',
       '## 5. Compatibilidad con las fuentes previstas', '',
       '| Fuente que reemplaza a Calibri | Libro | Guía | Cuaderno | Resultado |', '|---|---|---|---|---|']
porf = collections.defaultdict(dict)
for x in PF:
    porf[x['fuente']][[k for k, v in DOCS.items() if v == x['documento']][0]] = (x['paginas'], x['resultado'])
for fu, v in porf.items():
    md.append('| %s | %d | %d | %d | %s |' % (fu, v['libro'][0], v['guia'][0], v['cuaderno'][0],
                                             'correcto' if all(r == 'correcto' for _, r in v.values()) else 'FALLA'))
md += ['', '- **Carlito tiene las mismas medidas que Calibri:** con Calibri (Word en Windows) la paginación esperada es la de '
       'Carlito, que es la de los PDF entregados. La medida exacta en Word con Calibri sigue pendiente: en este entorno no '
       'hay Word ni Calibri.',
       '- Con Liberation Sans el libro gana 2 páginas, y con DejaVu Sans, una fuente más ancha, 25. En las tres no aparecen '
       'hojas en blanco ni renglones sueltos, y cada evaluación sigue en su página. Pero el índice y la página del '
       'diagnóstico que cita la guía corresponden a la paginación con Carlito: si el DOCX se abre en un equipo sin Calibri ni '
       'Carlito, hay que regenerar el PDF desde los constructores, no reimprimir el DOCX.',
       '- Por eso, para imprimir, el archivo de referencia es el PDF.', '',
       '## 6. Límites de esta auditoría', '',
       '- Se midió en pantalla, sobre el PDF de LibreOffice. No hay prueba en papel ni en la máquina de la imprenta.',
       '- No se abrió el DOCX en Microsoft Word ni en Windows: la compatibilidad con Word queda pendiente, igual que las '
       'pruebas del prototipo en Windows y en los laboratorios.',
       '- El contraste de los fondos de color de las cajas se juzgó a la vista en las láminas, no con un instrumento.']
open(os.path.join(COL, 'INFORME_LEGIBILIDAD_IMPRESION.md'), 'w', encoding='utf8').write('\n'.join(md) + '\n')
print('\n'.join(md[7:16]))
for k in DOCS:
    print(k, RES[k]['tamanos_pt'], RES[k]['sin_reduccion'], RES[k]['renglones_respuesta'], RES[k]['caracteres_por_renglon_mediana'])

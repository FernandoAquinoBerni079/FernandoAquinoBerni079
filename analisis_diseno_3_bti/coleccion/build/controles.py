# -*- coding: utf-8 -*-
"""Auditoría de impresión de los tres documentos anuales, sobre TODAS sus páginas → coleccion/CONTROLES_IMPRESION.json.
Usa los mismos controles de la candidata O3 y de los lotes (lote_1_oficio_candidata/build/controles_impresion.py,
lote_6/build/controles_finales.py), extendidos a todo el documento:
  1. Filas de tablas: cada fila de cada tabla de 2 o más columnas del DOCX, en orden, en el PDF; tablas repartidas
     entre páginas con todas sus filas y el encabezado repetido.
  2. Párrafos impresos y palabras de celda enteras.
  3. Figuras: cada epígrafe «Figura N.M —» del DOCX impreso una vez, con su imagen encima en la misma página.
  4. Índice: cada entrada del índice impreso en la página que indica, y en el orden del documento.
  5. Paginación continua: «Página X de Y» en cada página, con X = número de página e Y = total.
  6. Márgenes espejados en cada página con texto: impares con el interior (2,5 cm) a la izquierda, pares a la derecha.
  7. Hojas en blanco: ninguna página sin contenido además del pie.
  8. Cortes de tabla: ninguna tabla deja menos de dos filas de datos en una página.
  9. Bloques de código: cada línea impresa entera, en letra monoespaciada, dentro de los márgenes, y cada bloque en la
     página de su rótulo y su ficha (libro: Códigos; guía: Referencias).
 10. Legibilidad: ningún texto por debajo de 7,5 pt; renglones de respuesta nunca sueltos al comienzo de una página;
     cada evaluación del libro en página propia.
Uso: python3 -B coleccion/build/controles.py   (sale con 1 si algo falla)"""
import os, re, sys, json, collections
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
COL = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
import pymupdf, docx
import fuentes as FU
O, LOTES, GUIA, DIAG = FU.cargar()
CI = O.CI
import armar_coleccion as AC

DOCS = {k: v[:-5] for k, v in AC.RUTA.items()}
RES, FALLOS = {}, []
CM = 72 / 2.54


def chk(clave, cond, detalle):
    RES.setdefault(clave, []).append({'resultado': 'correcto' if cond else 'FALLA', 'detalle': detalle})
    if not cond:
        FALLOS.append('%s: %s' % (clave, detalle))
    print(('CORRECTO ' if cond else 'FALLA    ') + '[%s] %s' % (clave, detalle))


def lineas(pg):
    return [l.strip() for l in pg.get_text().split('\n') if l.strip()]


def sin_pie(pg):
    return [l for l in lineas(pg) if not re.match(r'^Página \d+ de \d+$', l)]


PDFS = {k: pymupdf.open(b + '.pdf') for k, b in DOCS.items()}
TABLAS = {}

# 1 y 2 ---------------------------------------------------------------------------------------------------
for k, base in DOCS.items():
    filas = CI.filas_de_tablas(base + '.docx', base + '.pdf')
    TABLAS[k] = filas
    malas = [f for f in filas if f['filas_impresas'] != f['filas_docx']]
    chk('1. Filas de tablas', not malas, '%s: %d tablas de 2 o más columnas, %d filas, todas impresas%s' % (
        k, len(filas), sum(f['filas_docx'] for f in filas), '' if not malas else ' — incompletas: %s' % [(m['rotulo'][:40], m['filas_faltantes']) for m in malas]))
    rep = [f for f in filas if len(f['paginas']) > 1]
    malas_r = [f for f in rep if not (f['filas_impresas'] == f['filas_docx'] and f['encabezado_repetido'] >= len(f['paginas']) - 1)]
    chk('1. Tablas repartidas entre páginas', not malas_r, '%s: %d tablas repartidas, todas con sus filas y el encabezado repetido%s'
        % (k, len(rep), '' if not malas_r else ' — %s' % [(m['rotulo'][:40], m['paginas']) for m in malas_r]))
    no = CI.parrafos_no_impresos(base + '.docx', base + '.pdf')
    chk('2. Párrafos impresos', not no, '%s: ningún párrafo del DOCX falta en el PDF%s' % (k, '' if not no else ' — faltan %s' % no[:3]))
    part = CI.palabras_partidas(base + '.docx', base + '.pdf')
    chk('2. Palabras enteras', not part, '%s: ninguna palabra de celda partida%s' % (k, '' if not part else ' — %s' % dict(list(part.items())[:5])))

# 3 -------------------------------------------------------------------------------------------------------
FIG = re.compile(r'Figura \d+\.\d+ —')
for k in ('libro', 'guia'):
    pdf = PDFS[k]
    d = docx.Document(DOCS[k] + '.docx')
    esperadas = [m.group(0) for p in d.paragraphs for m in [FIG.match(p.text)] if m]
    epis = [(i + 1, m.group(0)) for i, pg in enumerate(pdf) for m in FIG.finditer(pg.get_text()) if any(
        l.startswith(m.group(0)) for l in lineas(pg))]
    dib = {i + 1: [x['bbox'] for x in pg.get_image_info()] for i, pg in enumerate(pdf)}

    def sobre(p, e, pdf=pdf, dib=dib):
        r = pdf[p - 1].search_for(e)
        return bool(r) and any(b[3] <= r[0].y0 + 2 and b[2] - b[0] > 150 for b in dib[p])
    sin_img = [(e, p) for p, e in epis if not sobre(p, e)]
    chk('3. Figuras', [e for _, e in epis] == esperadas and not sin_img,
        '%s: %d figuras, cada una impresa una vez con su imagen encima de su epígrafe en la misma página%s'
        % (k, len(esperadas), '' if not sin_img and [e for _, e in epis] == esperadas else ' — %s / %s' % (sin_img[:3], len(epis))))

# 4 -------------------------------------------------------------------------------------------------------
res_c = json.load(open(os.path.join(COL, 'resultado_construccion.json'), encoding='utf8'))
for k in DOCS:
    pdf = PDFS[k]
    fin = AC.PC.fin_del_indice(pdf)
    texto_ind = '\n'.join(pdf[i].get_text() for i in range(1, fin + 1))
    impresas = [(m.group(1).strip(), int(m.group(2))) for m in re.finditer(r'^(.+?)\s*\.{3,}\s*(\d+)\s*$', texto_ind, re.M)]
    esperadas = res_c['indice_' + k]
    norm = lambda s: re.sub(r'\s+', ' ', s)
    titulos = {p_.text for p_ in docx.Document(DOCS[k] + '.docx').paragraphs if p_.style.name.startswith('Heading')}
    # los grupos por unidad del índice del cuaderno no son títulos del documento: llevan la página de su primera práctica
    malas = [(t, p) for i, (t, p) in enumerate(esperadas) if (norm(t)[:40] not in norm(pdf[p - 1].get_text()) if t in titulos
                                                              else not (i + 1 < len(esperadas) and esperadas[i + 1][1] == p))]
    orden = [p for _, p in esperadas] == sorted(p for _, p in esperadas)
    chk('4. Índice', len(impresas) == len(esperadas) and [p for _, p in impresas] == [p for _, p in esperadas] and not malas and orden,
        '%s: %d entradas en %d páginas de índice; cada una en la página que indica y en orden creciente%s' % (
            k, len(esperadas), fin, '' if not malas and len(impresas) == len(esperadas) else ' — impresas %d; no coinciden: %s' % (len(impresas), malas[:4])))

pG_ = PDFS['guia']
ins = res_c['instrumentos_guia']
mal_ins = [(r, p) for r, p_, p in ins if re.sub(r'\s+', ' ', r) not in re.sub(r'\s+', ' ', pG_[p - 1].get_text())]
chk('4. Índice', len(ins) > 40 and not mal_ins, 'guia: los %d instrumentos de la tabla «Instrumentos del año», cada uno en la página que indica%s'
    % (len(ins), '' if not mal_ins else ' — %s' % mal_ins[:4]))

# 5, 6, 7 -------------------------------------------------------------------------------------------------
for k, pdf in PDFS.items():
    n = len(pdf)
    pies = [i + 1 for i, pg in enumerate(pdf) if ('Página %d de %d' % (i + 1, n)) not in lineas(pg)]
    chk('5. Paginación continua', not pies, '%s: las %d páginas llevan «Página X de %d» con su número%s' % (k, n, n, '' if not pies else ' — fallan: %s' % pies[:8]))
    W = pdf[0].rect.width; malas, medidas = [], 0
    for i, pg in enumerate(pdf):
        if i == 0:
            continue
        bl = [b for b in pg.get_text('blocks') if b[4].strip() and not re.match(r'^Página \d+ de \d+\s*$', b[4].strip())]
        if not bl:
            continue
        iz, de = min(b[0] for b in bl) / CM, (W - max(b[2] for b in bl)) / CM
        medidas += 1
        impar = (i + 1) % 2 == 1
        if not ((iz >= 2.45 and de >= 1.6) if impar else (de >= 2.3 and iz >= 1.75)):
            malas.append((i + 1, round(iz, 2), round(de, 2)))
    chk('6. Márgenes espejados', not malas and medidas == n - 1,
        '%s: %d páginas medidas; impares con el interior a la izquierda y pares a la derecha%s' % (k, medidas, '' if not malas else ' — %s' % malas[:6]))
    vacias = [i + 1 for i, pg in enumerate(pdf) if not sin_pie(pg) and not pg.get_image_info()]
    chk('7. Hojas en blanco', not vacias, '%s: ninguna página en blanco%s' % (k, '' if not vacias else ' — %s' % vacias))


# 8 -------------------------------------------------------------------------------------------------------
def filas_por_pagina(dx, pdfp):
    pf = [(i + 1, [c or '' for c in r]) for i, pg in enumerate(pymupdf.open(pdfp))
          for tb in sorted(pg.find_tables().tables, key=lambda x: x.bbox[1]) if tb.col_count >= 2 for r in tb.extract()]
    k = 0; out = []
    for rot, filas in CI._tablas_docx(dx):
        pags = []
        for fila in filas:
            j = k
            while j < len(pf) and not (len(pf[j][1]) == len(fila) and all(CI._igual(a, b) for a, b in zip(fila, pf[j][1]))):
                j += 1
            if j < len(pf):
                pags.append(pf[j][0]); k = j + 1
        out.append((rot or filas[0][0], pags[1:]))
    return out


for k, base in DOCS.items():
    cortes = [(r[:50], dict(collections.Counter(p))) for r, p in filas_por_pagina(base + '.docx', base + '.pdf') if len(set(p)) > 1]
    solas = [c for c in cortes if min(c[1].values()) < 2]
    chk('8. Cortes de tabla', not solas, '%s: %d tablas repartidas, ninguna deja menos de dos filas de datos en una página%s'
        % (k, len(cortes), '' if not solas else ' — %s' % solas[:4]))

# 9 -------------------------------------------------------------------------------------------------------
import fragmentos as F4
import fragmentos_u5 as F5
import fragmentos_u6 as F6
MODS = (F4, F5, F6)
norm = lambda t: re.sub(r'[ \t]+', ' ', t)
for k, grupo in (('libro', 'FRAGMENTOS'), ('guia', 'REFERENCIA')):
    pdf = PDFS[k]
    impresas = norm('\n'.join(pg.get_text() for pg in pdf))
    ids = [(m, f) for m in MODS for f in getattr(m, grupo)]
    faltan = [(f, l) for m, f in ids for l in m.extraer(f) if l.strip() and re.sub(r'\s+', ' ', l.strip()) not in impresas]
    total = sum(1 for m, f in ids for l in m.extraer(f) if l.strip())
    chk('9. Bloques de código', not faltan, '%s: %d líneas de %d bloques, todas impresas enteras%s' % (k, total, len(ids), '' if not faltan else ' — %s' % faltan[:3]))
    W = pdf[0].rect.width
    mono = [(i + 1, x) for i, pg in enumerate(pdf) for b in pg.get_text('dict')['blocks'] for l in b.get('lines', []) for x in l['spans']
            if ('Mono' in x['font'] or 'Courier' in x['font']) and x['text'].strip()]
    fuera = [(p, x['text'][:30]) for p, x in mono if x['bbox'][2] > W - 1.6 * CM or x['bbox'][0] < 1.6 * CM]
    chk('9. Bloques de código', bool(mono) and not fuera, '%s: %d tramos en letra monoespaciada, todos dentro de los márgenes%s' % (k, len(mono), '' if not fuera else ' — %s' % fuera[:3]))
    cortes = []
    for m, f in ids:
        pag = [i for i, pg in enumerate(pdf) if (f + ' —') in pg.get_text()]
        ls = [re.sub(r'\s+', ' ', l.strip()) for l in m.extraer(f) if l.strip()]
        if len(pag) != 1 or not all(l in norm(pdf[pag[0]].get_text()) for l in ls):
            cortes.append((f, [p + 1 for p in pag]))
    chk('9. Bloques de código', not cortes, '%s: cada uno de los %d bloques entero en la página de su rótulo y su ficha%s' % (k, len(ids), '' if not cortes else ' — %s' % cortes))

# 10 ------------------------------------------------------------------------------------------------------
for k, pdf in PDFS.items():
    chicos = collections.Counter()
    for i, pg in enumerate(pdf):
        for b in pg.get_text('dict')['blocks']:
            for l in b.get('lines', []):
                for x in l['spans']:
                    if x['text'].strip() and x['size'] < 7.4:
                        chicos[(i + 1, round(x['size'], 1))] += 1
    chk('10. Legibilidad', not chicos, '%s: ningún texto por debajo de 7,5 pt%s' % (k, '' if not chicos else ' — %s' % list(chicos)[:5]))
    sueltos = [i + 1 for i, pg in enumerate(pdf) if sin_pie(pg) and sin_pie(pg)[0].startswith('_' * 20)]
    chk('10. Legibilidad', not sueltos, '%s: ningún renglón de respuesta suelto al comienzo de una página%s' % (k, '' if not sueltos else ' — %s' % sueltos))
pL = PDFS['libro']
evals = [FU.capitulo(c).EVAL_TITULO for c in range(1, 19) if FU.capitulo(c).EVAL_TITULO]
propias = {e: [i + 1 for i, pg in enumerate(pL) if e in sin_pie(pg)[:2]] for e in evals}
chk('10. Legibilidad', all(len(v) == 1 for v in propias.values()) and len(evals) == 17,
    'libro: las %d evaluaciones, cada una al comienzo de su página propia%s' % (len(evals), '' if all(len(v) == 1 for v in propias.values()) else ' — %s' % {k: v for k, v in propias.items() if len(v) != 1}))

RES['tablas'] = {k: [f for f in v if len(f['paginas']) > 1] for k, v in TABLAS.items()}
RES['paginas'] = {k: len(p) for k, p in PDFS.items()}
json.dump({'fallos': FALLOS, 'controles': RES}, open(os.path.join(COL, 'CONTROLES_IMPRESION.json'), 'w', encoding='utf8'),
          ensure_ascii=False, indent=1)
n = sum(len(v) for k, v in RES.items() if k[0].isdigit())
print('\nResultado: %d controles sobre %d páginas, %d fallos' % (n, sum(len(p) for p in PDFS.values()), len(FALLOS)))
sys.exit(1 if FALLOS else 0)

# -*- coding: utf-8 -*-
"""Controles finales de la candidata O3 del lote 1 → lote_1_oficio_candidata/CONTROLES_FINALES.json y .txt,
más las láminas de revisión visual en lote_1_oficio_candidata/revision_visual/.

1. Texto del DOCX idéntico al del A4 original y al de la prueba O3 (párrafos y celdas, en orden), salvo los números
   de página del índice y la línea de versión de la portada.
2. Impresión (controles_impresion.py): filas de todas las tablas de 2 o más columnas, con la Tabla 3.5 y las tablas
   repartidas entre páginas detalladas; párrafos no impresos; palabras partidas en celdas.
3. Figuras: mismas dimensiones en píxeles que las del lote 1 y la cantidad esperada de imágenes en el PDF.
4. Índice: cada entrada apunta a la página donde está su título.
5. Márgenes espejados: medidos en el PDF en páginas enfrentadas.
Uso: python3 lote_1_oficio_candidata/build/controles_finales.py   (sale con 1 si algo falla)"""
import os, re, sys, json, glob
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__)); CAND = os.path.dirname(AQUI); ADS = os.path.dirname(CAND)
sys.path.insert(0, AQUI)
import controles_impresion as CI
import docx, pymupdf
from docx.oxml.ns import qn
from PIL import Image

EST = os.path.join(CAND, 'ADS_3BTI_LOTE1_ESTUDIANTE_OFICIO_O3_CANDIDATA')
GUI = os.path.join(CAND, 'ADS_3BTI_LOTE1_GUIA_DOCENTE_OFICIO_O3_CANDIDATA')
A4 = {'libro': os.path.join(ADS, 'lote_1', 'ADS_3BTI_LOTE1_ESTUDIANTE'), 'guia': os.path.join(ADS, 'lote_1', 'ADS_3BTI_LOTE1_GUIA_DOCENTE')}
PRUEBA = {'libro': os.path.join(ADS, 'lote_1_oficio', 'O3', 'ADS_3BTI_LOTE1_ESTUDIANTE_OFICIO_O3'),
          'guia': os.path.join(ADS, 'lote_1_oficio', 'O3', 'ADS_3BTI_LOTE1_GUIA_DOCENTE_OFICIO_O3')}
CAN = {'libro': EST, 'guia': GUI}
VERSION = re.compile(r'^Versión v1\.0 \(lote 1, para auditoría\)( · .*)?$')
INDICE = re.compile(r'^(.*?)\t(\d+|—)$')
RES = {}; FALLOS = []


def chk(clave, cond, detalle):
    RES.setdefault(clave, []).append({'resultado': 'correcto' if cond else 'FALLA', 'detalle': detalle})
    if not cond:
        FALLOS.append('%s: %s' % (clave, detalle))
    print(('CORRECTO ' if cond else 'FALLA    ') + '[%s] %s' % (clave, detalle))


def texto(ruta):
    out = []
    for p in docx.Document(ruta).element.body.iter(qn('w:p')):
        s = ''.join((c.text or '') if c.tag == qn('w:t') else '\t' for r in p.iter(qn('w:r')) for c in r if c.tag in (qn('w:t'), qn('w:tab')))
        m = INDICE.match(s)
        if m: s = m.group(1) + '\t«pág.»'
        if VERSION.match(s.strip()): s = '«versión»'
        if s.strip(): out.append(s)
    return out


# 1. texto idéntico
for doc in ('libro', 'guia'):
    c = texto(CAN[doc] + '.docx')
    for nom, ref in (('A4 original', A4[doc]), ('prueba O3', PRUEBA[doc])):
        r = texto(ref + '.docx')
        dif = next((i for i, (x, y) in enumerate(zip(r, c)) if x != y), None)
        chk('1. Texto idéntico', r == c, '%s: %d párrafos con texto, igual que %s%s' % (doc, len(c), nom, '' if r == c else ' — primera diferencia en %s' % dif))

# 2. impresión
for doc, base in (('libro', EST), ('guia', GUI)):
    filas = CI.filas_de_tablas(base + '.docx', base + '.pdf')
    malas = [f for f in filas if f['filas_impresas'] != f['filas_docx']]
    chk('2. Filas de tablas', not malas, '%s: %d tablas de 2 o más columnas, todas con todas sus filas impresas (%d filas)%s'
        % (doc, len(filas), sum(f['filas_docx'] for f in filas), '' if not malas else ' — incompletas: %s' % [(m['primera_celda'], m['filas_faltantes']) for m in malas]))
    for f in filas:
        if len(f['paginas']) > 1:
            chk('2. Tablas repartidas entre páginas', f['filas_impresas'] == f['filas_docx'] and f['encabezado_repetido'] >= len(f['paginas']) - 1,
                '%s: «%s» (%s), págs. %s: %d de %d filas, encabezado repetido %d vez/veces'
                % (doc, f['rotulo'] or f['primera_celda'], f['primera_celda'], f['paginas'], f['filas_impresas'], f['filas_docx'], f['encabezado_repetido']))
    if doc == 'libro':
        t35 = [f for f in filas if f['rotulo'].startswith('Tabla 3.5')]
        chk('2. Tabla 3.5', len(t35) == 1 and t35[0]['filas_impresas'] == t35[0]['filas_docx'] == 8,
            'Tabla 3.5 «Alcance mínimo del proyecto (núcleo)»: %d de 8 filas impresas, pág. %s' % (t35[0]['filas_impresas'], t35[0]['paginas']) if t35 else 'Tabla 3.5 no encontrada')
        RES['tablas_libro'] = filas
    else:
        RES['tablas_guia'] = filas
    no = CI.parrafos_no_impresos(base + '.docx', base + '.pdf')
    chk('2. Párrafos impresos', not no, '%s: ningún párrafo del DOCX falta en el PDF%s' % (doc, '' if not no else ' — faltan %s' % no[:3]))
    part = CI.palabras_partidas(base + '.docx', base + '.pdf')
    chk('2. Palabras enteras', not part, '%s: ninguna palabra de celda partida en el PDF%s' % (doc, '' if not part else ' — %s' % part))

# 3. figuras
orig = {os.path.basename(f): Image.open(f).size for f in glob.glob(os.path.join(ADS, 'lote_1', 'build', 'figs', '*.png'))}
nuevas = {os.path.basename(f): Image.open(f).size for f in glob.glob(os.path.join(AQUI, 'figs', '*.png'))}
chk('3. Figuras', nuevas == orig, '%d figuras regeneradas con las mismas dimensiones que las del lote 1' % len(nuevas))
pE = pymupdf.open(EST + '.pdf')
pags_fig = [i + 1 for i, pg in enumerate(pE) if pg.get_images()]
epis = [(i + 1, m.group(0)) for i, pg in enumerate(pE) for m in re.finditer(r'Figura \d\.\d —', pg.get_text())]
chk('3. Figuras', len(epis) == len(orig) and all(p in pags_fig for p, _ in epis),
    'cada figura impresa con su epígrafe en la misma página: %s' % ', '.join('%s pág. %d' % (e[:10], p) for p, e in epis))

# 4. índice
ind = pE[1].get_text()
entradas = [(m.group(1).strip(), int(m.group(2))) for m in re.finditer(r'^(.+?)\s*\.{3,}\s*(\d+)\s*$', ind, re.M)]
malas = [(t, n) for t, n in entradas if t[:30] not in re.sub(r'\s+', ' ', pE[n - 1].get_text())]
chk('4. Índice', entradas and not malas, '%d entradas; cada una en la página que indica%s' % (len(entradas), '' if not malas else ' — no coinciden: %s' % malas[:5]))

# 5. márgenes espejados
W = pE[0].rect.width; med = []
for n in range(10, 18):
    bl = [b for b in pE[n - 1].get_text('blocks') if len(b[4]) > 80]
    if bl:
        med.append((n, round(min(b[0] for b in bl) / 72 * 2.54, 2), round((W - max(b[2] for b in bl)) / 72 * 2.54, 2)))
ok = all((iz >= 2.45 if n % 2 else de >= 2.3) and (de >= 1.6 if n % 2 else iz >= 1.75) for n, iz, de in med)
chk('5. Márgenes espejados', ok, 'impares con el interior (2,5 cm) a la izquierda y pares a la derecha: %s' % med)

# láminas de revisión visual
RV = os.path.join(CAND, 'revision_visual'); os.makedirs(RV, exist_ok=True)


def lamina(nombre, pags, pdf=pE, dpi=60):
    ims = []
    for n in pags:
        pix = pdf[n - 1].get_pixmap(dpi=dpi); im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples); ims.append(im)
    c = Image.new('RGB', (sum(i.width for i in ims) + 12 * (len(ims) - 1), max(i.height for i in ims)), (130, 130, 130)); x = 0
    for i in ims:
        c.paste(i, (x, 0)); x += i.width + 12
    ruta = os.path.join(RV, nombre); c.save(ruta); return os.path.basename(ruta)


lams = {'indice': lamina('01_indice.png', [2], dpi=80),
        'diagramas': lamina('02_diagramas.png', sorted({p for p, _ in epis})),
        'evaluaciones': lamina('03_evaluaciones.png', [i + 1 for i, pg in enumerate(pE) if pg.get_text().strip().startswith('Evaluación del Capítulo')]),
        'tabla_3_5': lamina('04_tabla_3_5.png', RES['tablas_libro'][[f['rotulo'].startswith('Tabla 3.5') for f in RES['tablas_libro']].index(True)]['paginas'], dpi=80),
        'margenes': lamina('05_margenes_espejados_pags_10_11.png', [10, 11], dpi=70),
        'tablas_repartidas_libro': lamina('06_tablas_repartidas_libro.png', sorted({p for f in RES['tablas_libro'] if len(f['paginas']) > 1 for p in f['paginas']})),
        'tablas_repartidas_guia': lamina('07_tablas_repartidas_guia.png', sorted({p for f in RES['tablas_guia'] if len(f['paginas']) > 1 for p in f['paginas']}), pdf=pymupdf.open(GUI + '.pdf'))}
RES['laminas'] = lams
json.dump({'fallos': FALLOS, 'controles': RES}, open(os.path.join(CAND, 'CONTROLES_FINALES.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
n = sum(len(v) for k, v in RES.items() if k[0].isdigit())
print('\nResultado: %d controles, %d fallos' % (n, len(FALLOS)))
sys.exit(1 if FALLOS else 0)

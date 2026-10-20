# -*- coding: utf-8 -*-
"""Controles de impresión del lote 2 y láminas de revisión visual → lote_2/CONTROLES_FINALES.json y .txt,
lote_2/revision_visual/*.png.

1. Filas de tablas (control de la candidata O3, `lote_1_oficio_candidata/build/controles_impresion.py`, sin cambios):
   cada fila de cada tabla de 2 o más columnas del DOCX se busca en orden en el PDF; se detallan las tablas repartidas
   entre páginas (todas sus filas y el encabezado repetido).
2. Párrafos no impresos y palabras partidas en celdas.
3. Figuras: cada figura impresa con su epígrafe en la misma página, y la cantidad de imágenes esperada.
4. Índice: cada entrada en la página que indica.
5. Márgenes espejados medidos en el PDF.
Uso: python3 lote_2/build/controles_finales.py   (sale con 1 si algo falla)"""
import os, re, sys, json
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
L2 = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
sys.path.insert(1, os.path.join(L2, 'caso'))
import oficio as O
CI = O.CI
import construir as B
import pymupdf
from PIL import Image

DOCS = {'libro': B.RUTA_EST[:-5], 'guia': B.RUTA_GUIA[:-5], 'cuaderno': B.RUTA_CUAD[:-5]}
RES = {}; FALLOS = []


def chk(clave, cond, detalle):
    RES.setdefault(clave, []).append({'resultado': 'correcto' if cond else 'FALLA', 'detalle': detalle})
    if not cond:
        FALLOS.append('%s: %s' % (clave, detalle))
    print(('CORRECTO ' if cond else 'FALLA    ') + '[%s] %s' % (clave, detalle))


TABLAS = {}
for doc, base in DOCS.items():
    filas = CI.filas_de_tablas(base + '.docx', base + '.pdf')
    TABLAS[doc] = filas
    malas = [f for f in filas if f['filas_impresas'] != f['filas_docx']]
    chk('1. Filas de tablas', not malas, '%s: %d tablas de 2 o más columnas, todas con todas sus filas impresas (%d filas)%s'
        % (doc, len(filas), sum(f['filas_docx'] for f in filas), '' if not malas else ' — incompletas: %s' % [(m['rotulo'][:40], m['filas_faltantes']) for m in malas]))
    for f in filas:
        if len(f['paginas']) > 1:
            chk('1. Tablas repartidas entre páginas', f['filas_impresas'] == f['filas_docx'] and f['encabezado_repetido'] >= len(f['paginas']) - 1,
                '%s: «%s», págs. %s: %d de %d filas, encabezado repetido %d vez/veces'
                % (doc, (f['rotulo'] or f['primera_celda'])[:70], f['paginas'], f['filas_impresas'], f['filas_docx'], f['encabezado_repetido']))
    no = CI.parrafos_no_impresos(base + '.docx', base + '.pdf')
    chk('2. Párrafos impresos', not no, '%s: ningún párrafo del DOCX falta en el PDF%s' % (doc, '' if not no else ' — faltan %s' % no[:3]))
    part = CI.palabras_partidas(base + '.docx', base + '.pdf')
    chk('2. Palabras enteras', not part, '%s: ninguna palabra de celda partida en el PDF%s' % (doc, '' if not part else ' — %s' % part))

pE = pymupdf.open(DOCS['libro'] + '.pdf')
epis = [(i + 1, m.group(0)) for i, pg in enumerate(pE) for m in re.finditer(r'Figura \d\.\d —', pg.get_text())]
# imágenes realmente dibujadas en cada página (LibreOffice comparte los recursos entre páginas: get_images no sirve)
dib = {i + 1: [x['bbox'] for x in pg.get_image_info()] for i, pg in enumerate(pE)}
def figura_sobre_epigrafe(p, e):
    pg = pE[p - 1]; r = pg.search_for(e)
    return r and any(b[3] <= r[0].y0 + 2 and b[2] - b[0] > 150 for b in dib[p])
chk('3. Figuras', [e for _, e in epis] == ['Figura %s —' % n for n in ('4.1', '4.2', '5.1', '5.2', '5.3', '5.4', '6.1', '6.2')]
    and all(figura_sobre_epigrafe(p, e) for p, e in epis),
    'las 8 figuras impresas, cada una con su imagen encima de su epígrafe, en la misma página: %s' % ', '.join('%s pág. %d' % (e[:10], p) for p, e in epis))
n_img = sum(len(v) for v in dib.values())
chk('3. Figuras', n_img == 8 + 13, 'imágenes dibujadas en el libro: %d (8 figuras y los 13 símbolos de las tres leyendas)' % n_img)

ind = pE[1].get_text()
entradas = [(m.group(1).strip(), int(m.group(2))) for m in re.finditer(r'^(.+?)\s*\.{3,}\s*(\d+)\s*$', ind, re.M)]
malas = [(t, n) for t, n in entradas if t[:30] not in re.sub(r'\s+', ' ', pE[n - 1].get_text())]
chk('4. Índice', entradas and not malas and len(entradas) == len(B.entradas_indice()),
    '%d entradas; cada una en la página que indica%s' % (len(entradas), '' if not malas else ' — no coinciden: %s' % malas[:5]))

W = pE[0].rect.width; med = []
for n in range(4, 12):
    bl = [b for b in pE[n - 1].get_text('blocks') if len(b[4]) > 80]
    if bl:
        med.append((n, round(min(b[0] for b in bl) / 72 * 2.54, 2), round((W - max(b[2] for b in bl)) / 72 * 2.54, 2)))
ok = med and all((iz >= 2.45 if n % 2 else de >= 2.3) and (de >= 1.6 if n % 2 else iz >= 1.75) for n, iz, de in med)
chk('5. Márgenes espejados', ok, 'impares con el interior (2,5 cm) a la izquierda y pares a la derecha: %s' % med)

# ---------------------------------------------------------------- láminas
RV = os.path.join(L2, 'revision_visual'); os.makedirs(RV, exist_ok=True)


def lamina(nombre, pags, pdf=pE, dpi=60):
    ims = []
    for n in pags:
        pix = pdf[n - 1].get_pixmap(dpi=dpi); ims.append(Image.frombytes('RGB', (pix.width, pix.height), pix.samples))
    filas = [ims[i:i + 4] for i in range(0, len(ims), 4)]
    w, h = ims[0].size
    c = Image.new('RGB', (min(4, len(ims)) * (w + 12) - 12, len(filas) * (h + 12) - 12), (130, 130, 130))
    for r, fila in enumerate(filas):
        for k, im in enumerate(fila):
            c.paste(im, (k * (w + 12), r * (h + 12)))
    c.save(os.path.join(RV, nombre)); return nombre


def pags_con(pdf, texto):
    return [i + 1 for i, pg in enumerate(pdf) if texto in pg.get_text()]


pG, pC = pymupdf.open(DOCS['guia'] + '.pdf'), pymupdf.open(DOCS['cuaderno'] + '.pdf')
import cap4, cap5, cap6
lams = {
    'indice': lamina('01_indice_y_apertura.png', [2, 3], dpi=70),
    'diagramas_capitulo_5': lamina('02_diagramas_capitulo_5.png', sorted({p for p, e in epis if e.startswith('Figura 5')}), dpi=75),
    'leyendas': lamina('03_leyendas_de_notacion.png', sorted(set(pags_con(pE, cap5.LEYENDA_ACTIVIDAD) + pags_con(pE, cap5.LEYENDA_CONTEXTO) + pags_con(pE, cap5.LEYENDA_CU))), dpi=70),
    'casos_de_uso': lamina('04_plantillas_de_casos_de_uso.png', sorted(set(pags_con(pE, 'Caso de uso CU-01') + pags_con(pE, 'Caso de uso CU-03'))), dpi=70),
    'trazabilidad_y_cambio': lamina('05_trazabilidad_y_solicitud_de_cambio.png', sorted(set(pags_con(pE, cap6.TABLA_62_ROTULO) + pags_con(pE, cap6.TABLA_65_ROTULO) + pags_con(pE, 'Figura 6.2 —'))), dpi=65),
    'practicas': lamina('06_practicas.png', [i + 1 for i, pg in enumerate(pE) if pg.get_text().startswith('Práctica ')], dpi=55),
    'evaluaciones': lamina('07_evaluaciones.png', [i + 1 for i, pg in enumerate(pE) if pg.get_text().startswith('Evaluación del Capítulo')], dpi=55),
    'h2': lamina('08_revision_unidad_II_H2.png', sorted(set(pags_con(pE, 'Antes de presentar: lista de verificación del equipo') + pags_con(pE, 'Criterios del H2'))), dpi=70),
    'rubrica_guia': lamina('09_guia_rubrica_H2_y_banco.png', sorted(set(pags_con(pG, 'Rúbrica del H2: descriptores por nivel') + pags_con(pG, 'Banco de necesidades nuevas'))), pdf=pG, dpi=70),
    'margenes': lamina('10_margenes_espejados_pags_6_7.png', [6, 7], dpi=60),
    'tablas_repartidas': lamina('11_tablas_repartidas.png', sorted({p for f in TABLAS['libro'] if len(f['paginas']) > 1 for p in f['paginas']}) or [4], dpi=55),
    'cuaderno': lamina('12_cuaderno_de_practicas.png', list(range(1, len(pC) + 1)), pdf=pC, dpi=45),
}
RES['laminas'] = lams
RES['tablas'] = TABLAS
json.dump({'fallos': FALLOS, 'controles': RES}, open(os.path.join(L2, 'CONTROLES_FINALES.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
n = sum(len(v) for k, v in RES.items() if k[0].isdigit())
print('\nResultado: %d controles, %d fallos' % (n, len(FALLOS)))
sys.exit(1 if FALLOS else 0)

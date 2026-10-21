# -*- coding: utf-8 -*-
"""Controles de impresión del lote 3 y láminas de revisión visual → lote_3/CONTROLES_FINALES.json y .txt,
lote_3/revision_visual/*.png. Mismo programa que el del lote 2 (lote_2/build/controles_finales.py), con las figuras
y las láminas de la Unidad III.

1. Filas de tablas (control de la candidata O3, `lote_1_oficio_candidata/build/controles_impresion.py`, sin cambios):
   cada fila de cada tabla de 2 o más columnas del DOCX se busca en orden en el PDF; se detallan las tablas repartidas
   entre páginas (todas sus filas y el encabezado repetido).
2. Párrafos no impresos y palabras partidas en celdas.
3. Figuras: cada figura impresa con su epígrafe en la misma página, y la cantidad de imágenes esperada.
4. Índice: cada entrada en la página que indica.
5. Márgenes espejados medidos en el PDF.
Uso: python3 lote_3/build/controles_finales.py   (sale con 1 si algo falla)"""
import os, re, sys, json, collections
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
L2 = os.path.dirname(AQUI)   # carpeta del lote 3
sys.path.insert(0, AQUI)
sys.path.insert(1, os.path.join(L2, 'caso'))
sys.path.insert(2, os.path.join(os.path.dirname(L2), 'lote_2', 'build'))
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

def filas_por_pagina(dx, pdf):
    """Página de cada fila de datos de cada tabla, con el mismo emparejamiento DOCX-PDF que CI.filas_de_tablas."""
    pf = [(i + 1, [c or '' for c in r]) for i, pg in enumerate(pymupdf.open(pdf))
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


for doc, base in DOCS.items():
    cortes = [(r[:50], dict(collections.Counter(p))) for r, p in filas_por_pagina(base + '.docx', base + '.pdf') if len(set(p)) > 1]
    solas = [c for c in cortes if min(c[1].values()) < 2]
    chk('6. Cortes de tabla', not solas, '%s: %d tablas repartidas, ninguna deja menos de dos filas de datos en una página%s'
        % (doc, len(cortes), '' if not solas else ' — %s' % solas))

pE = pymupdf.open(DOCS['libro'] + '.pdf')
epis = [(i + 1, m.group(0)) for i, pg in enumerate(pE) for m in re.finditer(r'Figura \d\.\d —', pg.get_text())]
# imágenes realmente dibujadas en cada página (LibreOffice comparte los recursos entre páginas: get_images no sirve)
dib = {i + 1: [x['bbox'] for x in pg.get_image_info()] for i, pg in enumerate(pE)}
def figura_sobre_epigrafe(p, e):
    pg = pE[p - 1]; r = pg.search_for(e)
    return r and any(b[3] <= r[0].y0 + 2 and b[2] - b[0] > 150 for b in dib[p])
chk('3. Figuras', [e for _, e in epis] == ['Figura %s —' % n for n in ('7.1', '7.2', '7.3', '8.1', '8.2', '8.3', '9.1')]
    and all(figura_sobre_epigrafe(p, e) for p, e in epis),
    'las 7 figuras impresas, cada una con su imagen encima de su epígrafe, en la misma página: %s' % ', '.join('%s pág. %d' % (e[:10], p) for p, e in epis))
n_img = sum(len(v) for v in dib.values())
chk('3. Figuras', n_img == 7 + 14, 'imágenes dibujadas en el libro: %d (7 figuras y los 14 símbolos de las cuatro leyendas)' % n_img)

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
import cap7, cap8, cap9
fig_p = lambda pref: sorted({p for p, e in epis if e.startswith(pref)})
lams = {
    'indice': lamina('01_indice_y_apertura.png', [2, 3], dpi=70),
    'modelo_de_datos': lamina('02_modelo_de_datos_y_diccionario.png', sorted(set(fig_p('Figura 7') + pags_con(pE, cap7.DICCIONARIO_ROTULO))), dpi=70),
    'leyendas': lamina('03_leyendas_de_notacion.png', sorted(set(pags_con(pE, cap7.LEYENDA_DER) + pags_con(pE, cap8.LEYENDA_NAV) + pags_con(pE, cap8.LEYENDA_BOC) + pags_con(pE, cap9.LEYENDA_CAPAS))), dpi=65),
    'mapa_y_bocetos': lamina('04_mapa_bocetos_y_estados.png', fig_p('Figura 8'), dpi=75),
    'mensajes_y_accesibilidad': lamina('05_mensajes_accesibilidad_y_sesion.png', sorted(set(pags_con(pE, cap8.TABLA_MENSAJES_ROTULO) + pags_con(pE, cap8.TABLA_ACC_ROTULO) + pags_con(pE, cap8.TABLA_OBS_ROTULO))), dpi=65),
    'arquitectura': lamina('06_capas_contratos_y_decision_tecnica.png', sorted(set(fig_p('Figura 9') + pags_con(pE, cap9.TABLA_94_ROTULO) + pags_con(pE, cap9.TABLA_95_ROTULO))), dpi=65),
    'coherencia': lamina('07_matriz_de_coherencia.png', pags_con(pE, cap9.TABLA_96_ROTULO) or [4], dpi=65),
    'practicas': lamina('08_practicas.png', [i + 1 for i, pg in enumerate(pE) if pg.get_text().startswith('Práctica ')], dpi=55),
    'evaluaciones': lamina('09_evaluaciones.png', [i + 1 for i, pg in enumerate(pE) if pg.get_text().startswith('Evaluación del Capítulo')], dpi=55),
    'h3': lamina('10_evaluacion_integradora_H3.png', sorted(set(pags_con(pE, 'Antes de presentar: lista de verificación del equipo') + pags_con(pE, 'Criterios del H3'))), dpi=70),
    'rubrica_guia': lamina('11_guia_rubrica_H3_y_banco.png', sorted(set(pags_con(pG, 'Rúbrica del H3: descriptores por nivel') + pags_con(pG, 'Banco de variantes'))), pdf=pG, dpi=70),
    'tarjetas_guia': lamina('12_guia_tarjetas_de_rol.png', pags_con(pG, 'Tarjetas de rol del Encuentro 16'), pdf=pG, dpi=70),
    'margenes': lamina('13_margenes_espejados_pags_6_7.png', [6, 7], dpi=60),
    'tablas_repartidas': lamina('14_tablas_repartidas.png', sorted({p for f in TABLAS['libro'] if len(f['paginas']) > 1 for p in f['paginas']}) or [4], dpi=55),
    'cuaderno': lamina('15_cuaderno_de_practicas.png', list(range(1, len(pC) + 1)), pdf=pC, dpi=45),
}
RES['laminas'] = lams
RES['tablas'] = TABLAS
json.dump({'fallos': FALLOS, 'controles': RES}, open(os.path.join(L2, 'CONTROLES_FINALES.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
n = sum(len(v) for k, v in RES.items() if k[0].isdigit())
print('\nResultado: %d controles, %d fallos' % (n, len(FALLOS)))
sys.exit(1 if FALLOS else 0)

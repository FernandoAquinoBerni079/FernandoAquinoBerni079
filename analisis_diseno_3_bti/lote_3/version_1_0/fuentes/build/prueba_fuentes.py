# -*- coding: utf-8 -*-
"""Prueba de robustez de la maqueta del lote 3 con tres fuentes de sustitución (Carlito, Liberation Sans, DejaVu Sans),
igual que la del lote 1 (lote_1/build/prueba_fuentes.py). Reemplaza Calibri en una copia de cada DOCX, la convierte a
PDF y comprueba: ninguna página en blanco, ningún renglón de respuesta suelto al comienzo de una página y, en el libro,
cada evaluación en página propia. Uso: python3 lote_3/build/prueba_fuentes.py  →  lote_3/prueba_fuentes_resultado.json"""
import os, re, sys, json, zipfile, tempfile, shutil
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
L2 = os.path.dirname(AQUI)
sys.path.insert(0, AQUI); sys.path.insert(1, os.path.join(L2, 'caso'))
sys.path.insert(2, os.path.join(os.path.dirname(L2), 'lote_2', 'build'))
import pymupdf
import construir as B

FUENTES = ['Carlito', 'Liberation Sans', 'DejaVu Sans']
DOCS = [B.RUTA_EST, B.RUTA_GUIA, B.RUTA_CUAD]


def sustituir(origen, destino, fuente):
    with zipfile.ZipFile(origen) as zi, zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED) as zo:
        for item in zi.infolist():
            datos = zi.read(item.filename)
            if item.filename.endswith('.xml'):
                datos = datos.decode('utf8').replace('Calibri', fuente).encode('utf8')
            zo.writestr(item, datos)


def lineas(pg):
    return [l.strip() for l in pg.get_text().split('\n') if l.strip() and not re.match(r'^Página \d+ de \d+$', l.strip())]


tmp = tempfile.mkdtemp(prefix='fuentes_'); res = []; fallos = 0
try:
    for f in FUENTES:
        for ruta in DOCS:
            nombre = os.path.basename(ruta)[:-5]
            copia = os.path.join(tmp, '%s_%s.docx' % (nombre, f.replace(' ', '')))
            sustituir(ruta, copia, f)
            pdf = pymupdf.open(B.K.a_pdf(copia, tmp))
            usadas = {x['font'] for pg in pdf for b in pg.get_text('dict')['blocks'] for l in b.get('lines', []) for x in l['spans']}
            vacias = [i + 1 for i, pg in enumerate(pdf) if not lineas(pg)]
            sueltos = [i + 1 for i, pg in enumerate(pdf) if lineas(pg) and lineas(pg)[0].startswith('_' * 20)]
            fila = dict(fuente=f, documento=nombre, paginas=len(pdf), vacias=vacias, renglones_sueltos=sueltos,
                        fuente_aplicada=any(f.split()[0] in u for u in usadas))
            if 'ESTUDIANTE' in nombre:
                fila['evaluaciones_en_pagina_propia'] = all(
                    len([i for i, pg in enumerate(pdf) if C.EVAL_TITULO in lineas(pg)[:2]]) == 1 for C in B.CAPS)
            bien = not vacias and not sueltos and fila['fuente_aplicada'] and fila.get('evaluaciones_en_pagina_propia', True)
            fallos += not bien
            fila['resultado'] = 'correcto' if bien else 'FALLA'
            res.append(fila)
            print('%-16s %-44s %3d págs.  en blanco: %s  sueltos: %s  eval. propia: %s  %s' % (
                f, nombre, len(pdf), vacias or 'ninguna', sueltos or 'ninguno', fila.get('evaluaciones_en_pagina_propia', '—'), fila['resultado']))
finally:
    shutil.rmtree(tmp, ignore_errors=True)
json.dump(res, open(os.path.join(L2, 'prueba_fuentes_resultado.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('Resultado: %d combinaciones, %d con fallos' % (len(res), fallos))
sys.exit(1 if fallos else 0)

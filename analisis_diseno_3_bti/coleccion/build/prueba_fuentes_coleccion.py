# -*- coding: utf-8 -*-
"""Prueba de robustez de la maqueta de los tres documentos anuales con tres fuentes de sustitución (Carlito, Liberation
Sans, DejaVu Sans), con el mismo procedimiento de los lotes (lote_6/build/prueba_fuentes.py): reemplaza Calibri en una
copia de cada DOCX, la convierte a PDF y comprueba que no haya páginas en blanco ni renglones de respuesta sueltos al
comienzo de una página, que la fuente se haya aplicado y, en el libro, que cada evaluación esté en página propia.
Uso: python3 -B coleccion/build/prueba_fuentes_coleccion.py  →  coleccion/PRUEBA_FUENTES.json"""
import os, re, sys, json, zipfile, tempfile, shutil
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
COL = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
import pymupdf
import fuentes as FU
O, L, G, D = FU.cargar()
import armar_coleccion as AC

FUENTES = ['Carlito', 'Liberation Sans', 'DejaVu Sans']


def sustituir(origen, destino, fuente):
    with zipfile.ZipFile(origen) as zi, zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED) as zo:
        for item in zi.infolist():
            datos = zi.read(item.filename)
            if item.filename.endswith('.xml'):
                datos = datos.decode('utf8').replace('Calibri', fuente).encode('utf8')
            zo.writestr(item, datos)


def lineas(pg):
    return [l.strip() for l in pg.get_text().split('\n') if l.strip() and not re.match(r'^Página \d+ de \d+$', l.strip())]


evals = [FU.capitulo(c).EVAL_TITULO for c in range(1, 19) if FU.capitulo(c).EVAL_TITULO]
tmp = tempfile.mkdtemp(prefix='fuentes_col_'); res = []; fallos = 0
try:
    for f in FUENTES:
        for clave, ruta in AC.RUTA.items():
            nombre = os.path.basename(ruta)[:-5]
            copia = os.path.join(tmp, '%s_%s.docx' % (nombre, f.replace(' ', '')))
            sustituir(ruta, copia, f)
            pdf = pymupdf.open(O.K.a_pdf(copia, tmp))
            usadas = {x['font'] for pg in pdf for b in pg.get_text('dict')['blocks'] for l in b.get('lines', []) for x in l['spans']}
            vacias = [i + 1 for i, pg in enumerate(pdf) if not lineas(pg) and not pg.get_image_info()]
            sueltos = [i + 1 for i, pg in enumerate(pdf) if lineas(pg) and lineas(pg)[0].startswith('_' * 20)]
            fila = dict(fuente=f, documento=nombre, paginas=len(pdf), vacias=vacias, renglones_sueltos=sueltos,
                        fuente_aplicada=any(f.split()[0] in u for u in usadas))
            if clave == 'libro':
                fila['evaluaciones_en_pagina_propia'] = all(
                    len([i for i, pg in enumerate(pdf) if e in lineas(pg)[:2]]) == 1 for e in evals)
            bien = not vacias and not sueltos and fila['fuente_aplicada'] and fila.get('evaluaciones_en_pagina_propia', True)
            fallos += not bien
            fila['resultado'] = 'correcto' if bien else 'FALLA'
            res.append(fila)
            print('%-16s %-46s %3d págs.  en blanco: %s  sueltos: %s  eval. propia: %s  %s' % (
                f, nombre, len(pdf), vacias or 'ninguna', sueltos or 'ninguno', fila.get('evaluaciones_en_pagina_propia', '—'), fila['resultado']))
finally:
    shutil.rmtree(tmp, ignore_errors=True)
json.dump(res, open(os.path.join(COL, 'PRUEBA_FUENTES.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('Resultado: %d combinaciones, %d con fallos' % (len(res), fallos))
sys.exit(1 if fallos else 0)

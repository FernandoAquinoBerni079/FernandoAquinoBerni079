# -*- coding: utf-8 -*-
"""Prueba de robustez de la maqueta con tres fuentes de sustitución (Carlito, Liberation Sans, DejaVu Sans).
Reemplaza Calibri en una copia de cada DOCX, la convierte a PDF y comprueba: evaluaciones en página propia,
ninguna página en blanco y ningún renglón de respuesta suelto al comienzo de una página.
Uso: python3 build/prueba_fuentes.py   →  build/prueba_fuentes_resultado.json"""
import os, re, sys, json, zipfile, tempfile, shutil
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import pymupdf
import comun as K
import cap1, cap2, cap3

FUENTES = ['Carlito', 'Liberation Sans', 'DejaVu Sans']
DOCS = ['ADS_3BTI_LOTE1_ESTUDIANTE', 'ADS_3BTI_LOTE1_GUIA_DOCENTE']


def sustituir(origen, destino, fuente):
    with zipfile.ZipFile(origen) as zi, zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED) as zo:
        for item in zi.infolist():
            datos = zi.read(item.filename)
            if item.filename.endswith('.xml'):
                datos = datos.decode('utf8').replace('Calibri', fuente).encode('utf8')
            zo.writestr(item, datos)


def lineas(pg):
    return [l.strip() for l in pg.get_text().split('\n') if l.strip() and not re.match(r'^Página \d+ de \d+$', l.strip())]


def main():
    tmp = tempfile.mkdtemp(prefix='fuentes_')
    res, fallos = [], 0
    try:
        for f in FUENTES:
            for nombre in DOCS:
                copia = os.path.join(tmp, '%s_%s.docx' % (nombre, f.replace(' ', '')))
                sustituir(os.path.join(K.RAIZ, nombre + '.docx'), copia, f)
                pdf = pymupdf.open(K.a_pdf(copia, tmp))
                usadas = sorted({x['font'] for pg in pdf for b in pg.get_text('dict')['blocks'] for l in b.get('lines', []) for x in l['spans']})
                vacias = [i + 1 for i, pg in enumerate(pdf) if not lineas(pg)]
                sueltos = [i + 1 for i, pg in enumerate(pdf) if lineas(pg) and lineas(pg)[0].startswith('_' * 20)]
                fila = dict(fuente=f, documento=nombre, paginas=len(pdf), vacias=vacias, renglones_sueltos=sueltos,
                            fuente_aplicada=any(f.split()[0] in u for u in usadas))
                if nombre.endswith('ESTUDIANTE'):
                    fila['evaluaciones_en_pagina_propia'] = all(
                        len([i for i, pg in enumerate(pdf) if C.EVAL_TITULO in lineas(pg)[:2]]) == 1 for C in (cap1, cap2, cap3))
                bien = not vacias and not sueltos and fila['fuente_aplicada'] and fila.get('evaluaciones_en_pagina_propia', True)
                fallos += not bien
                fila['resultado'] = 'correcto' if bien else 'FALLA'
                res.append(fila)
                print('%-16s %-28s %3d págs.  en blanco: %s  sueltos: %s  eval. propia: %s  %s' % (
                    f, nombre[-14:], len(pdf), vacias or 'ninguna', sueltos or 'ninguno',
                    fila.get('evaluaciones_en_pagina_propia', '—'), fila['resultado']))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    json.dump(res, open(os.path.join(AQUI, 'prueba_fuentes_resultado.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print('Resultado: %d combinaciones, %d con fallos' % (len(res), fallos))
    sys.exit(1 if fallos else 0)


if __name__ == '__main__':
    main()

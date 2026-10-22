# -*- coding: utf-8 -*-
"""Compatibilidad del DOCX con otras fuentes: el mismo procedimiento de coleccion/build/prueba_fuentes_coleccion.py.
Reemplaza Calibri en una copia del plan anual y de los planes de clase (Carlito, Liberation Sans, DejaVu Sans), convierte
a PDF y comprueba que la fuente se aplicó, que no queden páginas en blanco, que cada plan siga empezando en página propia
y termine con sus firmas antes del plan siguiente, y cuántas páginas cambia la paginación.
Uso: python3 -B planificacion/build/prueba_fuentes_plan.py  →  planificacion/PRUEBA_FUENTES_PLAN.json"""
import json, os, re, shutil, sys, tempfile, zipfile
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import pymupdf
import maqueta_plan as MP
import plan_anual as PA
import planes_clase as PC

PLAN = os.path.join(os.path.dirname(os.path.dirname(AQUI)), 'salida')
FUENTES = ['Carlito', 'Liberation Sans', 'DejaVu Sans']


def sustituir(origen, destino, fuente):
    with zipfile.ZipFile(origen) as zi, zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED) as zo:
        for item in zi.infolist():
            datos = zi.read(item.filename)
            if item.filename.endswith('.xml'):
                datos = datos.decode('utf8').replace('Calibri', fuente).encode('utf8')
            zo.writestr(item, datos)


tmp = tempfile.mkdtemp(prefix='fuentes_plan_'); res = []; fallos = 0
try:
    for f in FUENTES:
        for nombre in (PA.NOMBRE, PC.NOMBRE):
            copia = os.path.join(tmp, '%s_%s.docx' % (nombre, f.replace(' ', '')))
            sustituir(os.path.join(PLAN, nombre + '.docx'), copia, f)
            MP.a_pdf(copia, tmp)
            pdf = pymupdf.open(copia[:-5] + '.pdf')
            usadas = {x['font'] for pg in pdf for b in pg.get_text('dict')['blocks'] for l in b.get('lines', []) for x in l['spans']}
            txt = [re.sub(r'\s+', ' ', pg.get_text()).strip() for pg in pdf]
            vacias = [i + 1 for i, t in enumerate(txt) if len(re.sub(r'Página \d+', '', t)) < 120]
            fila = dict(fuente=f, documento=nombre, paginas=len(pdf), vacias=vacias, fuente_aplicada=any(f.split()[0] in u for u in usadas))
            bien = not vacias and fila['fuente_aplicada']
            if nombre == PC.NOMBRE:
                inicio = PC.paginas_planes(copia[:-5] + '.pdf')
                propios = all(txt[p - 1].startswith('Plan de Clase N.º %d —' % n) for n, p in inicio.items())
                firmas = all('Docente ____' in ' '.join(txt[inicio[n] - 1:inicio.get(n + 1, len(pdf) + 1) - 1]) for n in range(1, 37))
                fila.update(planes=len(inicio), plan_en_pagina_propia=propios, firmas_en_cada_plan=firmas,
                            max_paginas_por_plan=max(inicio.get(n + 1, len(pdf) + 1) - inicio[n] for n in range(1, 37)))
                bien = bien and len(inicio) == 36 and propios and firmas
            fallos += not bien
            fila['resultado'] = 'correcto' if bien else 'FALLA'
            res.append(fila)
            print('%-16s %-36s %3d págs.  en blanco: %s  %s%s' % (f, nombre, len(pdf), vacias or 'ninguna',
                  ('planes %d, máx. %d págs. por plan  ' % (fila['planes'], fila['max_paginas_por_plan'])) if 'planes' in fila else '', fila['resultado']))
finally:
    shutil.rmtree(tmp, ignore_errors=True)
json.dump(res, open(os.path.join(PLAN, 'PRUEBA_FUENTES_PLAN.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('Resultado: %d combinaciones, %d con fallos' % (len(res), fallos))
sys.exit(1 if fallos else 0)

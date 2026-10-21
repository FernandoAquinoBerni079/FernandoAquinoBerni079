# -*- coding: utf-8 -*-
"""Comprobaciones de la adenda de cierre de la colección v0.2. Solo lee: no escribe nada dentro de coleccion/.

1. Instrumentos de la guía: cuenta las filas de la tabla «Instrumentos del año», las tablas de calendario citadas en la
   parte general y las entradas que comprobó el control de impresión (resultado_construccion.json), y verifica en el PDF
   que cada una esté en la página que indica.
2. Manifiesto y ZIP de entrega: compara la lista de MANIFIESTO_COLECCION.json con el ZIP y con los archivos del
   repositorio, por SHA-256.
Uso: python3 -B planificacion/00_cierre_v0_2/verificar_cierre_v0_2.py [ruta del ZIP]
Escribe planificacion/00_cierre_v0_2/VERIFICACION_CIERRE_v0_2.json.
"""
import hashlib, json, os, re, subprocess, sys, zipfile
import docx
import pymupdf as fitz
from docx.table import Table

AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(os.path.dirname(AQUI))
COL = os.path.join(ADS, 'coleccion')
ZIP = sys.argv[1] if len(sys.argv) > 1 else '/home/user/ADS_3BTI_COLECCION_v0_2_CIERRE_EDITORIAL.zip'
sha = lambda b: hashlib.sha256(b).hexdigest()
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
res = {}

# ---------------------------------------------------------------- 1. instrumentos
rc = json.load(open(os.path.join(COL, 'resultado_construccion.json'), encoding='utf8'))
ins = rc['instrumentos_guia']
es_cal = lambda t: t.startswith('Unidad ') and t.endswith('en 36 y en 28 encuentros')
d = docx.Document(os.path.join(COL, 'ADS_3BTI_GUIA_DOCENTE_ANUAL_OFICIO_O3.docx'))
tabla_ins = tabla_cal = None
for t in d.tables:
    enc = [c.text for c in t.rows[0].cells]
    if enc == ['Instrumento', 'Parte', 'Página']: tabla_ins = [[c.text for c in r.cells] for r in t.rows[1:]]
    if enc[:2] == ['Parte', 'Encuentros ordinarios']: tabla_cal = [[c.text for c in r.cells] for r in t.rows[1:]]
pdf = fitz.open(os.path.join(COL, 'ADS_3BTI_GUIA_DOCENTE_ANUAL_OFICIO_O3.pdf'))
en_su_pagina = [r for r, _, p in ins if norm(r) in norm(pdf[p - 1].get_text())]
sin_cal = [[a, b, str(c)] for a, b, c in ins if not es_cal(a)]
cal = [x for x in ins if es_cal(x[0])]
res['instrumentos'] = {
    'entradas_comprobadas_por_el_control': len(ins),
    'en_la_pagina_que_indican': len(en_su_pagina),
    'filas_de_la_tabla_instrumentos_del_anio': len(tabla_ins),
    'tablas_de_calendario': len(cal),
    'la_tabla_coincide_con_las_entradas_sin_calendario': tabla_ins == sin_cal,
    'paginas_de_calendario_en_la_tabla_de_la_seccion_1': [r[3] for r in tabla_cal if r[0] != 'Total'] == [str(p) for _, _, p in cal],
    'texto_del_control': [c['detalle'] for c in json.load(open(os.path.join(COL, 'CONTROLES_IMPRESION.json'), encoding='utf8'))['controles']['4. Índice'] if 'instrumentos' in c['detalle']],
}

# ---------------------------------------------------------------- 2. manifiesto y ZIP
man = json.load(open(os.path.join(COL, 'MANIFIESTO_COLECCION.json'), encoding='utf8'))
lista = {a['ruta']: a['sha256'] for a in man['archivos']}
repo_ok = [r for r, h in lista.items() if sha(open(os.path.join(COL, r), 'rb').read()) == h]
z = zipfile.ZipFile(ZIP)
entradas = z.namelist()
carpetas = [n for n in entradas if n.endswith('/')]
archivos = [n for n in entradas if not n.endswith('/')]
en_ambos = [n for n in archivos if n in lista]
iguales = [n for n in en_ambos if sha(z.read(n)) == lista[n]]
solo_zip = [n for n in archivos if n not in lista]
fuera_zip = sorted(r for r in lista if r not in archivos)
grupos = {}
for r in fuera_zip:
    grupos[os.path.dirname(r)] = grupos.get(os.path.dirname(r), 0) + 1
en_git = subprocess.run(['git', 'ls-files', 'coleccion/build/figs'], cwd=ADS, capture_output=True, text=True).stdout.split()
res['manifiesto_y_zip'] = {
    'zip': os.path.basename(ZIP), 'zip_sha256': sha(open(ZIP, 'rb').read()),
    'entradas_del_zip': len(entradas), 'carpetas_del_zip': carpetas, 'archivos_del_zip': len(archivos),
    'archivos_del_manifiesto': len(lista), 'manifiesto_igual_al_repositorio': len(repo_ok),
    'en_el_zip_y_en_el_manifiesto': len(en_ambos), 'con_el_mismo_sha256': len(iguales),
    'solo_en_el_zip': solo_zip, 'del_manifiesto_fuera_del_zip': len(fuera_zip), 'fuera_del_zip_por_carpeta': grupos,
    'todos_los_de_fuera_estan_en_build_figs': all(r.startswith('build/figs/') for r in fuera_zip),
    'fuera_del_zip_por_tipo': {e: sum(1 for r in fuera_zip if r.endswith('.' + e)) for e in sorted({r.rsplit('.', 1)[-1] for r in fuera_zip})},
    'figuras_de_build_figs_en_git': len(en_git),
    'rotulo_interno_del_manifiesto': man['coleccion'],
}
json.dump(res, open(os.path.join(AQUI, 'VERIFICACION_CIERRE_v0_2.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))

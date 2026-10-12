# -*- coding: utf-8 -*-
"""Muestra comercial v1.2 (hallazgo 04): sólo documentos íntegros y hojas completas.
Libro: portada, presentación, índice, prueba diagnóstica, Unidad 1 · Clase 1 y Práctica 1 completas, contraportada;
portada del solucionario (sin claves); portada y primera hoja de la tabla del Plan Anual; portada y Plan de Clase N.º 1
íntegro (una hoja, con firmas). Al final se controla que ninguna hoja interior quede casi vacía y que no haya claves."""
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); import rutas as RT
import pymupdf, json, os, re
import ocupacion
O = RT.OUT; B = RT.B
L = pymupdf.open(O + 'Algoritmica_2do_Curso_LIBRO_ESENCIAL_COMERCIAL_2026.pdf')
S = pymupdf.open(O + 'Algoritmica_2do_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026.pdf')
P = pymupdf.open(O + 'Algoritmica_2do_Curso_PLANES_DE_CLASE_COMERCIAL_2026.pdf')
A = pymupdf.open(O + 'Algoritmica_2do_Curso_PLAN_ANUAL_COMERCIAL_2026.pdf')
ji = json.load(open(B + 'indice_libro.json')); pg = {t: p for (n, t), p in zip(ji['entradas'], ji['paginas'])}
c2 = [p for t, p in pg.items() if t.startswith('Clase 2 —')][0]
pr1 = [p for t, p in pg.items() if t.startswith('Práctica 1 —')][0]
jp = json.load(open(B + 'indice_planes.json')); p1, p2 = jp['paginas'][0], jp['paginas'][1]
assert p2 == p1 + 1, 'el Plan N.º 1 debe ocupar una sola hoja'
assert 'Clase 2 —' not in L[c2 - 2].get_text(), 'la última hoja de la Práctica 1 no debe compartirse con la Clase 2'
M = pymupdf.open()
for doc, a, b in ((L, 0, c2 - 2), (L, L.page_count - 1, L.page_count - 1), (S, 0, 0), (A, 0, 1), (P, 0, 0), (P, p1 - 1, p1 - 1)):
    M.insert_pdf(doc, from_page=a, to_page=b)
M.set_metadata({'title': 'Algorítmica · 2.º Curso · Muestra comercial', 'author': 'Equipo editorial', 'subject': 'Edición Esencial Comercial 2026'})
M.subset_fonts()
out = O + 'Algoritmica_2do_Curso_MUESTRA_COMERCIAL_2026.pdf'
M.save(out, garbage=4, deflate=True, deflate_images=True, deflate_fonts=True, clean=True)
txt = ' '.join(p.get_text() for p in M)
assert not re.search(r'Clave|Resultado esperado|Opción correcta', txt), 'la muestra no lleva claves del solucionario'
bajos = [x for x in ocupacion.medir(out) if x[1] < 0.30 and x[2] > 0]
print('muestra', M.page_count, 'págs', round(os.path.getsize(out) / 1e6, 2), 'MB · hojas casi vacías', len(bajos), bajos)

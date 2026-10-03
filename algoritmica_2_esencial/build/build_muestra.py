# -*- coding: utf-8 -*-
"""Muestra comercial: portada, presentación, índice, prueba diagnóstica, Unidad 1 · Clase 1 y Práctica 1,
contraportada del libro; portada del solucionario; portada y primera página del Plan Anual; portada y Plan N.º 1."""
import pymupdf, json, os
O = '/home/claude/alg2/salida/'; B = '/home/claude/alg2/build/'
N = 'Algoritmica_2do_Curso_%s_ESENCIAL_COMERCIAL_2026.pdf'
L = pymupdf.open(O + N % 'LIBRO'); S = pymupdf.open(O + N % 'SOLUCIONARIO_DOCENTE')
P = pymupdf.open(O + N % 'PLANES_DE_CLASE'); A = pymupdf.open(O + N % 'PLAN_ANUAL')
ji = json.load(open(B + 'indice_libro.json')); pg = {t: p for (n, t), p in zip(ji['entradas'], ji['paginas'])}
c2 = [p for t, p in pg.items() if t.startswith('Clase 2 —')][0]
jp = json.load(open(B + 'indice_planes.json')); p1, p2 = jp['paginas'][0], jp['paginas'][1]
M = pymupdf.open()
for doc, a, b in ((L, 0, c2 - 2), (L, L.page_count - 1, L.page_count - 1), (S, 0, 0), (A, 0, 1), (P, 0, 0), (P, p1 - 1, p2 - 2)):
    M.insert_pdf(doc, from_page=a, to_page=b)
M.set_metadata({'title': 'Algorítmica · 2.º Curso · Muestra comercial', 'author': 'Equipo editorial', 'subject': 'Edición Esencial Comercial 2026'})
M.subset_fonts()
out = O + 'Algoritmica_2do_Curso_MUESTRA_COMERCIAL_2026.pdf'
M.save(out, garbage=4, deflate=True, deflate_images=True, deflate_fonts=True, clean=True)
print('muestra', M.page_count, 'págs', round(os.path.getsize(out) / 1e6, 2), 'MB')

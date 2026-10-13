"""Muestra comercial FINAL OFICIO v3 (misma composición que la v2) (hallazgo 06): el Plan N.º 1 entra en UNA página (los Planes ya no
tienen continuaciones) y la hoja liberada se usa para la primera página de la Clase 18 (ficha + Access).
Sin claves del docente."""
import pymupdf, json, os, docx
O = '/home/claude/alg3/salida_FINAL_OFICIO_v3/'; B = '/home/claude/alg3/build/'; N = 'Algoritmica_3er_Curso_'; V = '_FINAL_OFICIO_v3'
L = pymupdf.open(O + N + 'LIBRO_ESENCIAL_COMERCIAL_2026' + V + '.pdf')
S = pymupdf.open(O + N + 'SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026' + V + '.pdf')
P = pymupdf.open(O + N + 'PLANES_DE_CLASE_COMERCIAL_2026' + V + '.pdf')
A = pymupdf.open(O + N + 'PLAN_ANUAL_COMERCIAL_2026' + V + '.pdf')
D = docx.Document(O + N + 'LIBRO_ESENCIAL_COMERCIAL_2026' + V + '.docx')
pg = {p.text.rsplit('\t', 1)[0]: int(p.text.rsplit('\t', 1)[1]) for p in D.paragraphs if p.style.name.startswith('toc') and '\t' in p.text}
c2 = pg['Clase 2 — Niveles de lenguaje: de la máquina al alto nivel']
c18 = pg['Clase 18 — Crear la base en Access: tablas y relaciones']
jp = json.load(open(B + 'indice_planes_v2.json')); p1, p2 = jp['paginas'][0], jp['paginas'][1]
assert p2 == p1 + 1, 'el Plan N.º 1 debe ocupar una sola página'
M = pymupdf.open()
for doc, a, b in ((L, 0, c2 - 2), (L, c18 - 1, c18 - 1), (L, L.page_count - 1, L.page_count - 1), (S, 0, 0), (A, 0, 1), (P, 0, 0), (P, p1 - 1, p1 - 1)):
    M.insert_pdf(doc, from_page=a, to_page=b)
M.set_metadata({'title': 'Algorítmica · 3.er Curso · Muestra comercial', 'author': 'Equipo editorial', 'subject': 'Edición Esencial Comercial 2026'})
M.subset_fonts()
out = O + N + 'MUESTRA_COMERCIAL_2026' + V + '.pdf'
M.save(out, garbage=4, deflate=True, deflate_images=True, deflate_fonts=True, clean=True)
txt = ' '.join(p.get_text() for p in M)
for k in ('Opción correcta', 'Resultado esperado', 'Solucionario', 'Clave —', '✓', '✗', '✅', '✔'):
    assert k not in txt or k == 'Solucionario', k
print('muestra', M.page_count, 'págs', round(os.path.getsize(out) / 1e6, 2), 'MB', '· libro 1..', c2 - 1, '+ Clase 18 pág.', c18, '· Plan N.º 1 pág.', p1)

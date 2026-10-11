# -*- coding: utf-8 -*-
"""Auditoría automática del paquete Software 2.º Esencial (libro, solucionario, plan anual, planes, muestra)."""
import os, re, sys, json, glob, hashlib, io, zipfile
import docx, pymupdf
from docx.oxml.ns import qn
B = '/home/claude/sw2/build/'; S = '/home/claude/sw2/src_md/'; O = '/home/claude/sw2/salida/'
sys.path.insert(0, B)
from mec import MEC
import palabras
N = 'Gabinete_Informatica_Software_2do_Curso_'
F = {'L': O + N + 'LIBRO_ESENCIAL_COMERCIAL_2026', 'S': O + N + 'SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026',
     'A': O + N + 'PLAN_ANUAL_COMERCIAL_2026', 'P': O + N + 'PLANES_DE_CLASE_COMERCIAL_2026'}
RES = []


def ok(nombre, cond, det=''):
    RES.append((bool(cond), nombre, det))


def texto_docx(path):
    d = docx.Document(path)
    return re.sub(r'\s+', ' ', ' '.join(t.text or '' for t in d.element.body.iter(qn('w:t'))))


def texto_pdf(path):
    return re.sub(r'\s+', ' ', ' '.join(p.get_text() for p in pymupdf.open(path)))


T = {k: texto_docx(v + '.docx') for k, v in F.items()}
TP = {k: texto_pdf(v + '.pdf') for k, v in F.items()}
norm = lambda s: re.sub(r'\s+', ' ', s)

# 1. Formato oficio en todas las páginas
for k, v in list(F.items()) + [('M', O + N + 'MUESTRA_COMERCIAL_2026')]:
    d = pymupdf.open(v + '.pdf')
    tam = {(round(p.rect.width / 72 * 2.54, 1), round(p.rect.height / 72 * 2.54, 1)) for p in d}
    ok('PDF %s en oficio en todas las páginas' % k, tam <= {(21.6, 33.0), (33.0, 21.6)}, str(tam))
    if k in F:
        dd = docx.Document(v + '.docx')
        for i, s in enumerate(dd.sections):
            w, h = round(s.page_width.cm, 1), round(s.page_height.cm, 1)
            ok('DOCX %s sección %d oficio y márgenes 1,27' % (k, i + 1), {w, h} == {21.6, 33.0} and abs(s.left_margin.cm - 1.27) < 0.02 and abs(s.top_margin.cm - 1.27) < 0.02)
        ok('Metadatos %s: autor Equipo editorial' % k, dd.core_properties.author == 'Equipo editorial')

# 2. Capacidades MEC textuales
for k in ('L', 'A', 'P'):
    for i, c in enumerate(MEC, 1):
        ok('Capacidad %d textual en %s' % (i, k), c in T[k])
for k in T:
    ok('Sin capacidad inventada «almacenamiento óptico» en %s' % k, 'almacenamiento óptico.' not in T[k])
    ok('Sin resumen «Reconoce, analiza e identifica» en %s' % k, 'Reconoce, analiza e identifica' not in T[k])

# 3. Estructura del libro
L = T['L']
for n in range(1, 21):
    ok('Clase %d presente' % n, re.search(r'Clase %d — ' % n, L))
    ok('Práctica %d presente' % n, re.search(r'Práctica %d — ' % n, L))
for x in 'ABCDEFGHIJKL':
    ok('Ficha %s presente' % x, 'Ficha %s — ' % x in L)
for t in ['Prueba diagnóstica', 'Evaluación de la Unidad 1', 'Evaluación integradora de la 1.ª etapa', 'Evaluación de la Unidad 2', 'Evaluación integradora de la 2.ª etapa', 'Proyecto Final Integrador']:
    ok('%s presente' % t, t in L)

# 4. Extensión mínima (750 palabras de desarrollo)
for n in range(1, 21):
    w = palabras.dev_words(n)
    ok('Clase %d ≥ 750 palabras de desarrollo' % n, w >= 750, str(w))
    t = open(S + 'tomo_clase%02d.md' % n).read()
    ok('Clase %d: ficha, Concepto clave, Ejemplo, En Paraguay, Errores frecuentes, tabla y 12 actividades' % n,
       all(x in t for x in ('[[FICHA]]', 'Concepto clave', '[[CAJA Ejemplo', 'En Paraguay', 'Errores frecuentes', '[[TABLA]]')) and re.search(r'^12\. ', t, re.M))

# 5. Prohibidos
for k in T:
    for pat, nom in [(r'[✅✓✔✗]', 'íconos ✓/✗/✅'), (r'generada con IA', '«generada con IA»'), (r'Ctrl\+E', 'leyenda Ctrl+E/F9'),
                     (r'\b[Tt]omo del estudiante|Cuaderno de Laboratorio', 'tomo/cuaderno'), (r'python-docx', 'python-docx')]:
        ok('%s: sin %s' % (k, nom), not re.search(pat, T[k]))

# 6. Correcciones técnicas T1–T16
chk = [('T1', 'S', 'V-F: 8) F — No hay una regla absoluta'), ('T2', 'S', 'fuente 450 W 80 Plus Bronze: eficiencia certificada'),
       ('T3', 'L', 'Resolución 1035/2025'), ('T4', 'L', 'Core Ultra 5, 7 y 9'), ('T5', 'L', 'el primer lanzamiento comercial fue el de Claro'),
       ('T6', 'L', '1,385 MB/s'), ('T7', 'L', '2.000–14.000 MB/s'), ('T8', 'L', 'ranuras PCIe y SSD M.2'), ('T9', 'L', 'USB 5 Gb/s (USB 3.2 Gen 1)'),
       ('T10', 'L', '172.16.0.0 a 172.31.255.255'), ('T11', 'L', 'si el centro es un hub'), ('T12', 'L', 'memoria flash no volátil'),
       ('T13', 'S', 'En general sí, por las distancias cortas'), ('T14', 'S', '11 patch cords (5 × 2 + 1'), ('T15', 'S', '550 ÷ 0,80 = 687,5 GB'),
       ('T16', 'L', 'la mayoría de las placas nuevas ya no traen VGA')]
for t, k, s in chk:
    ok('Corrección %s aplicada' % t, s in T[k])
ok('T6: sin 1,35 MB/s ni 21,6 MB/s', not re.search(r'1,35 MB/s|21,6 MB/s', L + T['S']))
ok('T7: sin 80–160 MB/s', '80–160' not in L)
ok('T2: sin «potencia real certificada»', 'potencia real certificada' not in T['S'])
ok('T4: sin «Intel Core (i3, i5, i7, i9)»', 'Intel Core (i3, i5, i7, i9)' not in L)

# 7. Figuras: numeración correlativa por clase y epígrafes
caps = re.findall(r'^Figura (\d+)\.(\d+) — ', '\n'.join(open(f).read() for f in sorted(glob.glob(S + 'tomo_clase*.md')) + sorted(glob.glob(S + 'lab_practica*.md'))), re.M)
por = {}
for n, k in caps:
    por.setdefault(int(n), []).append(int(k))
for n in range(1, 21):
    ks = sorted(por.get(n, []))
    ok('Figuras de la Clase %d numeradas 1..k sin saltos' % n, ks == list(range(1, len(ks) + 1)), str(ks))
ok('Sin «Fotografía N.k» ni «Fotografía PN»', not re.search(r'Fotografía (\d|P)', L))

# 8. Imágenes de Gemini conservadas (bytes idénticos o PNG con píxeles idénticos)
from PIL import Image
import numpy as np
orig = {}
for f in glob.glob(B + 'figs_src/*'):
    orig[os.path.basename(f)] = f
z = zipfile.ZipFile(F['L'] + '.docx')
media = {n: z.read(n) for n in z.namelist() if n.startswith('word/media/')}
hs = {hashlib.sha256(v).hexdigest() for v in media.values()}
pix = []
for nombre, f in orig.items():
    b = open(f, 'rb').read()
    if hashlib.sha256(b).hexdigest() in hs:
        continue
    a = np.asarray(Image.open(f))
    igual = any(v[:8] == b'\x89PNG\r\n\x1a\n' and Image.open(io.BytesIO(v)).size == Image.open(f).size and np.array_equal(np.asarray(Image.open(io.BytesIO(v))), a) for v in media.values())
    pix.append((nombre, igual))
ok('Las 52 imágenes originales están en el libro (idénticas o PNG sin pérdida)', all(i for _, i in pix) and len(orig) == 52, str([n for n, i in pix if not i]))
ok('JPEG originales byte a byte', all(hashlib.sha256(open(f, 'rb').read()).hexdigest() in hs for n, f in orig.items() if n.endswith('.jpg')))

# 9. Índices contra el PDF
for k, js in (('L', 'indice_libro.json'), ('S', 'indice_sol.json'), ('P', 'indice_planes.json')):
    j = json.load(open(B + js))
    import maqueta as M
    d0 = pymupdf.open(F[k] + '.pdf')
    ini = next(i for i, p in enumerate(d0) if i > 1 and not re.search(r'\.{8,}', p.get_text()) and any(e[1] in p.get_text() for e in j['entradas'][:1])) + 1
    pags, tot = M.paginas_de(F[k] + '.pdf', [t for _, t in j['entradas']], desde=ini)
    ok('Índice %s coincide con el PDF (%d entradas)' % (k, len(pags)), pags == j['paginas'], str([(a, b) for a, b in zip(pags, j['paginas']) if a != b][:3]))

# 10. Páginas casi vacías del libro y del solucionario
for k in ('L', 'S'):
    d0 = pymupdf.open(F[k] + '.pdf'); malas = []
    for i, pg in enumerate(d0):
        if i < 2 or i == len(d0) - 1:
            continue
        bl = [b for b in pg.get_text('blocks') if not b[4].strip().startswith('Página')]
        ys = [b[3] for b in bl] + [r.y1 for im in pg.get_images(full=True) for r in pg.get_image_rects(im[0])]
        if ys and max(ys) / pg.rect.height < 0.2:
            malas.append(i + 1)
    ok('%s sin páginas casi vacías (<20 %%)' % k, not malas, str(malas))

# 11. Plan Anual y Planes
pa = json.load(open(B + 'pa_rows.json'))
ok('Plan Anual: 36 secuencias de 2 h (72 HC)', len(pa) == 36 and all(r['tiempo'] == '2 h' for r in pa))
ok('Plan Anual: procedimientos únicos', len({r['proc'] for r in pa}) == 36)
ok('Plan Anual: instrumentos únicos', len({r['inst'] for r in pa}) == 36)
ok('Planes: 36 planes N.º 1 a 36', sorted({int(x) for x in re.findall(r'Plan de Clase N\.º (\d+) de 36', T['P'])}) == list(range(1, 37)))
for r in pa:
    ok('Plan Anual fila %d: indicadores presentes en los Planes' % r['n'], all(norm(i) in T['P'] for i in r['indicadores']))
ok('Planes: sin datos viejos de prácticas (132 discos, G. 686, 98 + 4)', not re.search(r'132 discos|G\. 686|98 \+ 4|10 PC, la impresora, el access point y el router quedan', T['P']))

dP = pymupdf.open(F['P'] + '.pdf')
ok('Planes: cada plan en una sola hoja (sin páginas de continuación)', not [i for i, pg in enumerate(dP) if i > 1 and not re.search(r'Plan de Clase N\.º \d+ de 36', pg.get_text())])
dA = pymupdf.open(F['A'] + '.pdf')
ok('Plan Anual: tabla en oficio horizontal', all(round(pg.rect.width / 72 * 2.54, 1) == 33.0 for pg in list(dA)[1:]))
# 12. Solucionario: cobertura
Sx = T['S']
for n in range(1, 21):
    ok('Solucionario: Clase %d y Práctica %d' % (n, n), ('Clase %d — ' % n) in Sx and ('Práctica %d — Resultado esperado' % n) in Sx)
for x in 'ABCDEFGHIJKL':
    ok('Solucionario: Ficha %s' % x, ('Ficha %s — ' % x) in Sx)
ok('Solucionario: rúbrica analítica con 4 niveles', all(t in Sx for t in ('Logrado (100 %)', 'En proceso (60 %)', 'Inicial (30 %)', 'No presentado (0 %)')))

# 13. Prácticas: puntos de control sin resultados numéricos revelados
for n in range(1, 21):
    t = open(S + 'lab_practica%02d.md' % n).read()
    pcs = re.findall(r'^Punto de control: (.*)$', t, re.M)
    ok('Práctica %d: puntos de control sin resultados («≈», «Resultados:»)' % n, pcs and not any(re.search(r'≈|Resultados:|muestra \d', p) for p in pcs))

# 14. Aritmética de casos y ejemplos nuevos
ok('Caso 1: total 3.450.000', 280000 + 390000 + 720000 + 1150000 + 480000 + 430000 == 3450000)
ok('Clase 10: costos de primer año', 1100000 + 7200 * 21 == 1251200 and 1450000 + 7200 * 112 == 2256400)
ok('Clase 16: cable de la biblioteca', 12 + 15 + 18 + 21 + 24 + 27 == 117)
ok('Práctica 16: cable de la farmacia', 7 + 11 + 14 + 19 + 23 + 28 + 41 + 52 == 195)
ok('Clase 19: canales del salón', (78 + 5, 86 + 5, 94 + 5) == (83, 91, 99))
ok('Práctica 10: costo por página', round(210000 / 300) == 700 and round(540000 / 2700) == 200)

# 15. Matriz trazable de respuestas numéricas (datos del enunciado → cálculo → clave)
import verif_trazable as VT
for item, datos, op, res, enc, b in VT.FILAS:
    ok('Trazable %s: %s está en la clave' % (item, res), enc, str(b))
lineas = ['| Ítem | Datos del enunciado | Operación | Resultado | En la clave |', '|---|---|---|---|---|']
lineas += ['| %s | %s | %s | %s | %s |' % (i, d, o, r, 'Sí' if e else 'NO') for i, d, o, r, e, _ in VT.FILAS]
open(B + 'verificacion_trazable.md', 'w').write('# Verificación trazable de respuestas numéricas\n\n' + '\n'.join(lineas) + '\n')
# 16. Reutilización de datos entre bloques (clase, práctica, ficha, evaluación)
import subprocess
dup = subprocess.run(['python3', B + 'dups_md.py'], capture_output=True, text=True).stdout.strip().splitlines()
graves = [l for l in dup if int(l.split(' |')[0]) >= 3]
ok('Sin bloques que compartan 3 o más datos no constantes', not graves, '; '.join(graves))

fallos = [r for r in RES if not r[0]]
out = ['Auditoría Software 2.º Esencial — %d controles · %d fallos' % (len(RES), len(fallos)), '']
out += ['FALLO  %s  %s' % (n, d) for c, n, d in RES if not c]
out += ['ok     %s' % n for c, n, d in RES if c]
open(B + 'auditoria_resultado.txt', 'w').write('\n'.join(out) + '\n')
print(out[0])
for l in out[2:2 + len(fallos)]:
    print(l)

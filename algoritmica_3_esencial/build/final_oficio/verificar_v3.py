"""Verificación de la entrega FINAL OFICIO v3: controles del Informe 03 (11/10/2026) y de la reauditoría 04 (12/10/2026).
Uso: python3 -I verificar_v3.py   → imprime los controles y escribe build/verificacion_v3.txt
Todos los datos se leen de los entregables (docx/pdf); las cuentas se rehacen a partir del enunciado."""
import re, os, glob, json, zipfile, difflib, sys
import docx, pymupdf
from docx.oxml.ns import qn
sys.path.insert(0, os.path.dirname(__file__))
import indice

R = '/home/claude/alg3/'; O1 = R + 'salida_FINAL_OFICIO/'; O2 = R + 'salida_FINAL_OFICIO_v3/'; N = 'Algoritmica_3er_Curso_'
V1 = {'L': O1 + N + 'LIBRO_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO', 'S': O1 + N + 'SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO',
      'P': O1 + N + 'PLANES_DE_CLASE_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO', 'A': O1 + N + 'PLAN_ANUAL_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO'}
V2 = {'L': O2 + N + 'LIBRO_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO_v3', 'S': O2 + N + 'SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO_v3',
      'P': O2 + N + 'PLANES_DE_CLASE_COMERCIAL_2026_FINAL_OFICIO_v3', 'A': O2 + N + 'PLAN_ANUAL_COMERCIAL_2026_FINAL_OFICIO_v3'}
MUE = O2 + N + 'MUESTRA_COMERCIAL_2026_FINAL_OFICIO_v3.pdf'
RES = []
CAP = 'Reconoce la importancia de la práctica Conductual en el desarrollo de las actividades.'


def chk(h, nombre, ok, det=''):
    RES.append((h, nombre, bool(ok), det))


def pars(path):
    d = docx.Document(path + '.docx')
    return [''.join(x.text or '' for x in p.iter(qn('w:t'))) for p in d.element.body.iter(qn('w:p'))]


def ptxt(path):
    return [pg.get_text() for pg in pymupdf.open(path if path.endswith('.pdf') else path + '.pdf')]


def g(s):  # «G. 12.000» / «12.000» → 12000
    return int(s.replace('.', ''))


def fill(p):
    bl = [b for b in p.get_text('blocks') if not b[4].strip().startswith('Página')]
    ys = [b[3] for b in bl] + [dr['rect'].y1 for dr in p.get_drawings()]
    for im in p.get_images(full=True):
        ys += [r.y1 for r in p.get_image_rects(im[0])]
    return max(ys) / p.rect.height if ys else 0


T = {k: pars(v) for k, v in V2.items()}; T1 = {k: pars(v) for k, v in V1.items()}
J = {k: '\n'.join(v) for k, v in T.items()}
PDF = {k: ptxt(v) for k, v in V2.items()}; PJ = {k: '\n'.join(v) for k, v in PDF.items()}

# ---- 01 capacidad transversal
for k, nom in (('L', 'Libro'), ('P', 'Planes'), ('A', 'Plan Anual'), ('S', 'Solucionario')):
    n = J[k].count(CAP)
    chk('01', 'frase oficial literal en %s (docx)' % nom, n >= 1, n)
    chk('01', 'frase oficial literal en %s (pdf)' % nom, re.sub(r'\s+', ' ', PJ[k]).count(CAP) >= 1)
chk('01', 'Libro: en Presentación y en Proyecto Final', sum(CAP in t for t in T['L']) == 2)

# ---- 02 Evaluación U4 ítem 7: recálculo desde el enunciado
it7 = next(t for t in T['L'] if t.startswith('7. En una jornada distinta'))
q = {k: (int(a), g(b)) for a, k, b in re.findall(r'(\d+) (chipas|mbeju|empanadas|milanesas|cocidos|jugos) a G\. ([\d.]+)', it7)}
chk('02', 'ítem 7: seis productos leídos', len(q) == 6, q)
pan = sum(q[k][0] * q[k][1] for k in ('chipas', 'mbeju')); sal = sum(q[k][0] * q[k][1] for k in ('empanadas', 'milanesas'))
beb = sum(q[k][0] * q[k][1] for k in ('cocidos', 'jugos')); tot = pan + sal + beb
k7 = next(t for t in T['S'] if t.startswith('7. Panificados'))
for nom, v in (('Panificados', pan), ('Salados', sal), ('Bebidas', beb), ('total', tot)):
    chk('02', 'clave ítem 7: %s = %s' % (nom, f'{v:,}'.replace(',', '.')), f'{v:,}'.replace(',', '.') in k7)
chk('02', 'clave ítem 7 = propuesta del auditor (26.000/64.000/30.500/120.500)', (pan, sal, beb, tot) == (26000, 64000, 30500, 120500))
chk('02', 'ítem 7 ya no reutiliza los importes de la Clase 21', 'Chipa 18.000' not in J['L'])
# ---- 03 Integradora 2 ítem 8
it8 = next(t for t in T['L'] if t.startswith('8. En un nuevo local'))
F = {a: g(b) for a, b in re.findall(r'(F\d) G\. ([\d.]+)', it8)}
cli = {'Rosa': F['F1'] + F['F3'], 'Luis': F['F2'], 'Ana': F['F4'], 'Miguel': F['F5']}
tot8 = sum(F.values()); prom = tot8 / len(F)
k8 = next(t for t in T['S'] if t.startswith('8. Rosa'))
for nom, v in list(cli.items()) + [('total', tot8), ('promedio', int(prom))]:
    chk('03', 'clave ítem 8: %s = %s' % (nom, f'{v:,}'.replace(',', '.')), f'{v:,}'.replace(',', '.') in k8)
chk('03', 'clave ítem 8 = propuesta del auditor', (cli['Rosa'], tot8, prom) == (56000, 153000, 30600))
chk('03', 'ítem 8 ya no reutiliza V1–V5 de la Clase 21', 'V1 14.000' not in J['L'] and '26.800' not in k8 and '134.000' not in k8)
# independencia: los resultados nuevos no aparecen resueltos en el libro
for v in ('120.500', '30.500', '64.000', '153.000', '30.600', '56.000'):
    chk('02/03', 'resultado %s no figura en el libro del estudiante' % v, v not in J['L'])
# ---- 04 Planes sin continuaciones
pl = pymupdf.open(V2['P'] + '.pdf')
cont = [i + 1 for i, pg in enumerate(pl) if '· continuación' in pg.get_text()]
chk('04', 'Planes: 0 hojas de continuación', not cont, cont)
inicios = [i for i, pg in enumerate(pl) if re.search(r'^Plan de Clase N\.º \d+ —', pg.get_text(), re.M) and 'Índice' not in pg.get_text()]
chk('04', 'Planes: 36 planes, uno por hoja', len(inicios) == 36 and pl.page_count == 38, (len(inicios), pl.page_count))
for i in inicios:
    t = pl[i].get_text()
    if not ('Dirección — Visto bueno' in t and 'Observaciones' in t and 'Criterios' in t):
        chk('04', 'plan de la pág. %d con criterios, observaciones y firmas' % (i + 1), False)
chk('04', 'los 36 planes cierran con criterios, observaciones y firmas en su hoja', all('Dirección — Visto bueno' in pl[i].get_text() for i in inicios))
niv = json.load(open(R + 'build/indice_planes_v2.json'))['niveles']
chk('04', 'letra mínima 8,5 pt o más (nivel ≤ 3)', all(v <= 3 for v in niv.values()), niv)
dif = [l for l in difflib.unified_diff([x for x in T1['P'] if x.strip()], [x for x in T['P'] if x.strip()], lineterm='', n=0)
       if l[:1] in '+-' and not l.startswith(('+++', '---'))]
sin_num = lambda xs: [re.sub(r'\d+$', '', x) if x.startswith('Plan de Clase N.º') else x for x in xs if x.strip()]
dif = [l for l in difflib.unified_diff(sin_num(T1['P']), sin_num(T['P']), lineterm='', n=0)
       if l[:1] in '+-' and not l.startswith(('+++', '---'))]
chk('04', 'Planes: 0 diferencias de texto con FINAL OFICIO (salvo números del índice)', not dif, dif[:4])
idx = json.load(open(R + 'build/indice_planes_v2.json'))
chk('04', 'Planes: índice verificado contra el PDF', [i + 1 for i in inicios] == idx['paginas'], idx['paginas'][:5])
# ---- 05 Access / Office 2016
for k, nom in (('L', 'Libro'), ('S', 'Solucionario')):
    chk('05', '%s: sin «Click-to-Run»' % nom, 'Click-to-Run' not in J[k] and 'Click-to-Run' not in PJ[k])
    ok = all('fuera de soporte desde el 14 de octubre de 2025' in t for t in T[k] if 'Office 2016' in t)
    chk('05', '%s: toda mención de Office 2016 lleva el fin de soporte' % nom, ok and 'Office 2016' in J[k])
    chk('05', '%s: recomienda Microsoft 365 o Access 2024' % nom, 'Access incluido en Microsoft 365 o Access 2024' in J[k])
# ---- 06 Muestra
mu = pymupdf.open(MUE); mt = [p.get_text() for p in mu]
chk('06', 'Muestra: 15 páginas', mu.page_count == 15, mu.page_count)
chk('06', 'Muestra: ninguna continuación ni página < 25 %', not any('· continuación' in t for t in mt) and min(fill(p) for p in list(mu)[1:]) >= 0 and
    all(fill(p) >= 0.25 for p, t in zip(mu, mt) if t.strip()))
chk('06', 'Muestra: Plan N.º 1 en una sola página', sum('Plan de Clase N.º 1 —' in t for t in mt) == 1)
chk('06', 'Muestra: sin claves docentes', not any(k in t for t in mt for k in ('Opción correcta', 'Resultado esperado', 'Clave —')))
# ---- 07 nombres compartidos
for f in glob.glob(O2 + '*'):
    b = os.path.basename(f)
    if 'PLAN_ANUAL' in b or 'PLANES_DE_CLASE' in b:
        chk('07', 'nombre sin edición: ' + b, 'ESENCIAL' not in b and 'COMPLETA' not in b)
difA = [l for l in difflib.unified_diff(T1['A'], T['A'], lineterm='', n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
chk('07', 'Plan Anual: 0 diferencias de texto con FINAL OFICIO', not difA, difA[:3])
# ---- 08 Práctica 3 vs Práctica 21
mod = next(t for t in T['L'] if re.fullmatch(r'[\d.]+( · [\d.]+){5}', t.strip()))
imp = [g(x) for x in mod.split(' · ')]
traza = [sum(imp[:i + 1]) for i in range(6)]
kp3 = next(t for t in T['S'] if t.startswith('Resultado esperado: Act. 1: (a) estructurado'))
chk('08', 'Práctica 3: traza %s' % traza, ' → '.join(f'{v:,}'.replace(',', '.') for v in traza) in kp3)
chk('08', 'Práctica 3: total y promedio', 'total G. %s' % f'{traza[-1]:,}'.replace(',', '.') in kp3 and
    'promedio G. %s' % f'{traza[-1] // 6:,}'.replace(',', '.') in kp3 and traza[-1] % 6 == 0)
may = [v for v in imp if v > 20000]
chk('08', 'Práctica 3: desafío %d ventas > 20.000' % len(may), 'Desafío: %d ventas' % len(may) in kp3)
chk('08', 'Práctica 3: error de inicialización muestra el último importe', 'último importe, %d)' % imp[-1] in J['S'])
p21 = sorted([19000, 17000, 29000, 19000, 9000, 42000])
chk('08', 'Práctica 3 ya no repite los importes de la segunda semana (P21)', sorted(imp) != p21 and traza[-1] != 135000)
chk('08', 'Práctica 3 en otra semana que la de Access (9 al 11 de marzo)', 'semana del 16 al 18 de marzo' in J['L'])
# ---- 09 ocupación del libro
lp = pymupdf.open(V2['L'] + '.pdf')
bajas = [(i + 1, round(fill(p), 2)) for i, p in enumerate(lp) if 0 < fill(p) < 0.25]
chk('09', 'Libro: 0 páginas con ocupación < 25 %', not bajas, bajas)
for n in (33, 102):
    chk('09', 'Libro pág. %d: cierre de clase con autoevaluación' % n, 'Autoevaluación antes de la Práctica' in lp[n - 1].get_text())
# ---- 10 (reauditoría 04): tabla cruzada — coherencia no es exactitud
for frase in ('auditor incorporado', 'las dos sumas no coincidirían', 'la esquina que audita', 'y su doble control'):
    chk('10', 'Libro: sin «%s»' % frase, frase not in J['L'] and frase not in re.sub(r'\s+', ' ', PJ['L']))
for frase in ('Esta igualdad permite detectar errores de suma o presentación, pero NO demuestra que cada celda sea correcta.',
              'Concepto clave — coherencia no es exactitud',
              'Una tabla cruzada facilita comprobar la coherencia de sus subtotales. La exactitud de cada importe exige además validarlo contra los datos de origen.'):
    chk('10', 'Libro: «%s…»' % frase[:50], frase in J['L'])
chk('10', 'Libro pág. 110: paso 5 y concepto clave en la misma hoja que la Figura 21.2',
    all(k in re.sub(r'\s+', ' ', PDF['L'][109]) for k in ('Figura 21.2', '5. Control de sumas', 'coherencia no es exactitud')))
# ---- 11 (reauditoría 04): un solo encabezado de la capacidad en el PFI
pfi = T['L'][[i for i, t in enumerate(T['L']) if t.startswith('Proyecto Final Integrador — La solución')][-1]:]
chk('11', 'PFI: encabezado único «Capacidad transversal del programa MEC»',
    pfi.count('Capacidad transversal del programa MEC') == 1 and 'Capacidad transversal del programa' not in [t for t in pfi if t != 'Capacidad transversal del programa MEC'])
chk('11', 'PFI: sin el rótulo repetido «Capacidad transversal MEC:»', not any(t.startswith('Capacidad transversal MEC:') for t in T['L']))
k = pfi.index('Capacidad transversal del programa MEC')
chk('11', 'PFI: la frase oficial en párrafo propio, seguida de la evidencia', pfi[k + 1] == CAP and pfi[k + 2].startswith('En el proyecto se evidencia'))

# ---- generales
for k, nom in (('L', 'Libro'), ('S', 'Solucionario')):
    d = docx.Document(V2[k] + '.docx')
    res = indice.hallar(d, V2[k] + '.pdf')
    mal = [p.text for p, n in res if str(n) != p.text.rsplit('\t', 1)[1]]
    chk('gen', '%s: índice %d/%d contra el PDF' % (nom, len(res) - len(mal), len(res)), not mal, mal[:3])
for k, v in list(V2.items()) + [('M', MUE[:-4])]:
    d = pymupdf.open(v + '.pdf')
    ok = all({round(p.rect.width), round(p.rect.height)} == {612, 936} for p in d)
    chk('gen', 'oficio 612×936 pt: ' + os.path.basename(v), ok)
    chk('gen', 'sin ✓ ✗ ✅ ✔: ' + os.path.basename(v), not any(c in pg.get_text() for pg in d for c in '✓✗✅✔'))
for k in ('L', 'S', 'P', 'A'):
    d = docx.Document(V2[k] + '.docx')
    chk('gen', 'márgenes 1,27 cm: ' + k, all(abs(s.top_margin.cm - 1.27) < 0.01 and abs(s.left_margin.cm - 1.27) < 0.01 for s in d.sections))
for k, nom, pags in (('L', 'Libro', 117), ('S', 'Solucionario', 18), ('A', 'Plan Anual', 6)):
    chk('gen', '%s: %d páginas' % (nom, pags), len(PDF[k]) == pags, len(PDF[k]))
# diferencias de texto del libro y solucionario: solo las previstas
for k, nom, esperadas in (('L', 'Libro', 38), ('S', 'Solucionario', 11)):
    a = [x for x in T1[k] if x.strip()]; b = [x for x in T[k] if x.strip()]
    ch = [l for l in difflib.unified_diff(a, b, lineterm='', n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    chk('gen', '%s: %d líneas de texto distintas de FINAL OFICIO, todas revisadas y de esta corrección' % (nom, len(ch)), len(ch) == esperadas, ch)
# v3 frente a v2: solo cambian el Libro (hallazgos 10 y 11) y la Muestra regenerada
import hashlib
Ov2 = R + 'salida_FINAL_OFICIO_v2/'
a = [x for x in pars(Ov2 + N + 'LIBRO_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO_v2') if x.strip()]
b = [x for x in T['L'] if x.strip()]
ch = [l for l in difflib.unified_diff(a, b, lineterm='', n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
chk('v3', 'Libro v3 frente a v2: 13 líneas distintas, todas de los hallazgos 10 y 11', len(ch) == 13, ch)
for f in sorted(glob.glob(O2 + '*')):
    b3 = os.path.basename(f)
    if 'LIBRO' in b3 or 'MUESTRA' in b3: continue
    f2 = Ov2 + b3.replace('_v3.', '_v2.')
    chk('v3', 'idéntico byte a byte a la v2: ' + b3, hashlib.sha256(open(f, 'rb').read()).digest() == hashlib.sha256(open(f2, 'rb').read()).digest())

if __name__ == '__main__':
    out = ['VERIFICACIÓN FINAL OFICIO v3 — Algorítmica 3.º · Informe 03 (11/10/2026) y reauditoría 04 (12/10/2026)',
           'Controles: %d · Fallos: %d' % (len(RES), sum(not r[2] for r in RES)), '']
    for h, n, ok, det in RES:
        out.append('%-5s %s  %s%s' % (h, 'OK ' if ok else 'FALLA', n, '' if ok else '  → %s' % (det,)))
    txt = '\n'.join(out); print(txt)
    open(R + 'build/verificacion_v3.txt', 'w').write(txt + '\n')

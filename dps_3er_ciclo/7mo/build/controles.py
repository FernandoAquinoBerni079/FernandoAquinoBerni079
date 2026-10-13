# -*- coding: utf-8 -*-
"""Controles internos del paquete de Desarrollo Personal y Social 7.º (información del productor; no sustituyen la auditoría).
Fuentes, curriculum, figuras, coherencia libro–solucionario–planes–Plan Anual y archivos de salida.
Escribe verificacion/CONTROLES.md y termina con código 1 si hay fallos."""
import os, re, json, glob, hashlib, zipfile, io, sys
import curriculo as C

B = os.path.dirname(os.path.abspath(__file__)) + '/'
F = B + '../fuente/'; OUT = B + '../salida/'; V = B + '../verificacion/'
OK, FALLOS, INFO = [], [], []


def ok(c, msg):
    (OK if c else FALLOS).append(msg)
    return c


def leer(p):
    return open(p, encoding='utf-8').read().split('\n')


def prosa(L):
    """Palabras de prosa explicada: párrafos fuera de fichas, cajas, tablas y del bloque de actividades."""
    n, dentro, act = 0, False, False
    for l in L:
        s = l.strip()
        if s.startswith('[[FICHA') or s.startswith('[[CAJA') or s == '[[TABLA]]':
            dentro = True; continue
        if s.startswith('[[/'):
            dentro = False; continue
        if s.startswith('### '):
            act = True; continue
        if s.startswith('## '):
            act = False; continue
        if dentro or act or not s or s.startswith(('[[', '@@', 'Figura ')) or re.match(r'^(\d+\.|[a-e]\))\s', s):
            continue
        n += len(s.split())
    return n


def items(L):
    """Consignas numeradas del libro y sus opciones."""
    out, cur = [], None
    for l in L:
        m = re.match(r'^(\d+)\. (.*)', l.strip())
        if m and not l.startswith('    '):
            cur = {'n': int(m.group(1)), 't': m.group(2), 'ops': []}; out.append(cur); continue
        m = re.match(r'^\s{4}([a-e])\) (.*)', l)
        if m and cur:
            cur['ops'].append((m.group(1), m.group(2)))
    return out


TUTEO = r'\b(tú|tienes|puedes|eres|debes|quieres|sabes|piensa|escribe|observa|lee|responde|completa|marca|elige|explica|une|ordena|dibuja|imagina|recuerda|busca|anota|comparte|subraya|relaciona|identifica)\b'
SIMBOLOS = '✓✗✅✔✘☑'
LEYES_OK = ('1680', '1264', '4633', '5777', '6202')  # 6202 y 5777 solo si aparecen con su nombre correcto (se revisan a mano)

# ---------- 1. Fuentes del libro ----------
letras = {}
for e in C.ENCUENTROS:
    n, t, k, u, caps_n, tit, _ = e
    p = F + 'tomo/e%02d.md' % n
    if not ok(os.path.exists(p), 'E%02d: existe la fuente del libro' % n):
        continue
    L = leer(p); txt = '\n'.join(L)
    ok(L[0].strip() == '@@ENC %02d' % n, 'E%02d: cabecera @@ENC' % n)
    if t in 'CP':
        tag = '[[FICHA]]' if t == 'C' else '[[FICHA_PEC]]'
        ok(tag in L, 'E%02d: ficha %s' % (n, tag))
        i = L.index(tag); j = L.index(tag.replace('[[', '[[/'))
        blk = L[i + 1:j]
        caps = [x[len('Capacidad: '):].strip() for x in blk if x.startswith('Capacidad: ')]
        ok(caps == [C.CAP[c] for c in caps_n], 'E%02d: capacidades literales del MEC (%s)' % (n, caps_n))
        inds = [x for x in blk if x.startswith('- ')]
        ok(len(inds) == 3, 'E%02d: tres indicadores de logro (%d)' % (n, len(inds)))
        w = prosa(L); minimo = 800 if t == 'C' else 900
        ok(w >= minimo, 'E%02d: prosa explicada ≥ %d palabras (%d)' % (n, minimo, w))
        INFO.append(('E%02d' % n, C.rotulo(e), w, len(txt.split())))
        ok('### Actividades' in txt, 'E%02d: bloque de actividades' % n)
        if t == 'C':
            for caja in ('ejemplo', 'concepto'):
                ok('[[CAJA %s]]' % caja in txt, 'E%02d: caja %s' % (n, caja))
            ok('[[CAJA paraguay]]' in txt or '[[CAJA cuidado]]' in txt, 'E%02d: caja En Paraguay o Para cuidarte' % n)
            ok('[[CAJA mirate]]' in txt, 'E%02d: Mirate' % n)
            ok('[[TABLA]]' in txt, 'E%02d: al menos una tabla' % n)
            ok('[[IMG ' in txt, 'E%02d: figura' % n)
        else:
            ok('[[CAJA bitacora]]' in txt, 'E%02d: caja de la bitácora del proyecto' % n)
    else:
        ok('Puntaje total' in txt, 'E%02d: puntaje total declarado' % n)
        pts = sum(int(x) for x in re.findall(r'\((\d+) puntos?[):]', txt))
        tot = re.search(r'Puntaje total: (\d+)', txt)
        ok(tot and pts == int(tot.group(1)), 'E%02d: los puntajes suman el total (%s de %s)' % (n, pts, tot.group(1) if tot else '?'))
        ok(txt.count('### Parte') >= 3, 'E%02d: tres partes' % n)
    its = items(L)
    nums = [x['n'] for x in its]
    ok(nums == list(range(1, len(nums) + 1)), 'E%02d: consignas numeradas en forma continua' % n)
    for x in its:
        if x['ops'] and not re.search(r'V \(verdadero\)|V o F|verdadero', x['t'], re.I) and not x['ops'][0][1].rstrip().endswith('____'):
            ok(len(x['ops']) == 4 and [o[0] for o in x['ops']] == list('abcd'), 'E%02d: consigna %d con 4 opciones a–d' % (n, x['n']))
    for s in SIMBOLOS:
        ok(s not in txt, 'E%02d: sin el símbolo %s' % (n, s))
    tut = [m.group(0) for l in L for m in re.finditer(TUTEO, l, re.I) if re.match(r'^\s*(\d+\.|[a-e]\))\s', l) and m.start() < 40 and m.group(0)[0].isupper()]
    ok(not tut, 'E%02d: consignas sin tuteo %s' % (n, tut[:3]))
    ok(not re.search(r'aprobad[oa] por el (MEC|Ministerio)|certificad[oa] por el (MEC|Ministerio)', txt), 'E%02d: sin atribuir aprobación del MEC' % n)
    # clave de opción múltiple en el solucionario
    ps = F + 'sol/e%02d.md' % n
    if ok(os.path.exists(ps), 'E%02d: existe la fuente del solucionario' % n):
        S = '\n'.join(leer(ps))
        for x in its:
            ok(re.search(r'(^|\n)\s*(\|\s*)?%d[\.\s|]' % x['n'], S) is not None, 'E%02d: la consigna %d tiene respuesta en el solucionario' % (n, x['n']))
            if len(x['ops']) == 4:
                m = re.search(r'(?:^|\n)\s*(?:\|\s*)?%d[\.\s|][^\n]*?(?:Respuesta|Clave)?[^\n]*?\b([abcd])\)' % x['n'], S)
                if m:
                    letras.setdefault(m.group(1), 0); letras[m.group(1)] += 1
    pj = F + 'planes/e%02d.json' % n
    if ok(os.path.exists(pj), 'E%02d: existe el plan de clase' % n):
        try:
            j = json.load(open(pj, encoding='utf-8'))
            ok(j['inicio']['min'] + j['desarrollo']['min'] + j['cierre']['min'] == 120, 'E%02d: momentos del plan suman 120 min' % n)
            ok(all(j[k_] for k_ in ('recursos', 'procedimientos', 'instrumentos', 'criterios')), 'E%02d: plan con recursos, procedimientos, instrumentos y criterios' % n)
        except Exception as ex:
            ok(False, 'E%02d: plan JSON válido (%s)' % (n, ex))
INFO.append(('letras correctas en opción múltiple', letras))
if letras:
    ok(len(letras) == 4 and max(letras.values()) <= 2.2 * min(letras.values()), 'Respuestas correctas de opción múltiple repartidas entre a, b, c y d %s' % letras)

# ---------- 2. Figuras ----------
import render as R
usadas = []
for e in C.ENCUENTROS:
    p = F + 'tomo/e%02d.md' % e[0]
    if os.path.exists(p):
        L = leer(p)
        for i, l in enumerate(L):
            m = re.match(r'\[\[IMG (\S+)\|', l.strip())
            if m:
                usadas.append(m.group(1))
                try:
                    R.figura(m.group(1)); hay = True
                except FileNotFoundError:
                    hay = False
                ok(hay, 'Figura %s: archivo disponible' % m.group(1))
                ok(L[i + 1].startswith('Figura '), 'Figura %s: epígrafe numerado' % m.group(1))
                prev = [x for x in L[:i] if x.strip()][-1]
                ok(re.search(r'[Ff]igura|[Oo]bservá|[Mm]irá', prev) is not None, 'Figura %s: párrafo previo que la anuncia' % m.group(1))
ok(len(usadas) == len(set(usadas)), 'Cada figura se usa una sola vez')
orig = sorted(os.listdir(B + '../figs/originales'))
INFO.append(('figuras originales no usadas', [x for x in orig if x not in usadas]))
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
for l in open(B + '../originales/SHA256.txt'):
    h, nombre = l.split()
    ok(sha(B + '../' + nombre) == h, 'Original intacto: %s' % nombre)

# ---------- 3. Plan Anual: unicidad ----------
pa = B + 'pa_rows.json'
if os.path.exists(pa):
    rows = json.load(open(pa))
    ok(len(rows) == 36, 'Plan Anual: 36 filas')
    ok(len({r['proc'] for r in rows}) == 36, 'Plan Anual: 36 procedimientos distintos')
    ok(len({r['inst'] for r in rows}) == 36, 'Plan Anual: 36 instrumentos distintos')

# ---------- 4. Salidas ----------
esperados = ['Desarrollo_Personal_y_Social_7mo_Grado_LIBRO_DEL_ESTUDIANTE_2026.docx', 'Desarrollo_Personal_y_Social_7mo_Grado_LIBRO_DEL_ESTUDIANTE_2026.pdf',
             'Desarrollo_Personal_y_Social_7mo_Grado_PLAN_ANUAL_2026.docx', 'Desarrollo_Personal_y_Social_7mo_Grado_PLANES_DE_CLASE_2026.docx',
             'Desarrollo_Personal_y_Social_7mo_Grado_SOLUCIONARIO_DOCENTE_2026.docx', 'Desarrollo_Personal_y_Social_7mo_Grado_SOLUCIONARIO_DOCENTE_2026.pdf']
if os.path.isdir(OUT) and any(f.endswith('.docx') for f in os.listdir(OUT)):
    ok(sorted(os.listdir(OUT)) == sorted(esperados), 'salida/ tiene exactamente los seis archivos (%s)' % sorted(os.listdir(OUT)))
    import docx, pymupdf
    for f in esperados:
        if not os.path.exists(OUT + f):
            continue
        if f.endswith('.docx'):
            d = docx.Document(OUT + f)
            for i, s in enumerate(d.sections):
                w, h = round(s.page_width.cm, 1), round(s.page_height.cm, 1)
                ok(sorted((w, h)) == [21.6, 33.0], '%s: sección %d en oficio (%s × %s)' % (f, i + 1, w, h))
                if i > 0:
                    ok(all(abs(x.cm - 1.27) < 0.01 for x in (s.left_margin, s.right_margin, s.top_margin, s.bottom_margin)), '%s: sección %d con márgenes de 1,27 cm' % (f, i + 1))
            xml = zipfile.ZipFile(OUT + f).read('word/document.xml').decode('utf8')
            for s in SIMBOLOS:
                ok(s not in xml, '%s: sin el símbolo %s' % (f, s))
            ok(not re.search(r'\b(e\d\d\.md|image\d+\.png|@@ENC|\[\[)', xml), '%s: sin residuos de marcado' % f)
        else:
            doc = pymupdf.open(OUT + f)
            tam = {(round(p.rect.width), round(p.rect.height)) for p in doc}
            ok(tam == {(612, 935)} or tam == {(612, 936)}, '%s: todas las páginas en oficio %s' % (f, tam))

# ---------- informe ----------
os.makedirs(V, exist_ok=True)
R_ = ['# Controles internos del paquete — Desarrollo Personal y Social 7.º', '', 'Generado por `build/controles.py`. Son controles del productor: no sustituyen la auditoría independiente.', '',
      '**%d controles correctos · %d fallos**' % (len(OK), len(FALLOS)), '']
if FALLOS:
    R_ += ['## Fallos', ''] + ['- ' + x for x in FALLOS] + ['']
R_ += ['## Extensión por encuentro (clases y talleres)', '', '| Encuentro | Título | Palabras de prosa explicada | Palabras totales de la fuente |', '|---|---|---|---|']
R_ += ['| %s | %s | %d | %d |' % x for x in INFO if len(x) == 4]
R_ += ['', '## Otros datos', ''] + ['- %s: %s' % x for x in INFO if len(x) == 2]
open(V + 'CONTROLES.md', 'w').write('\n'.join(R_) + '\n')
print('%d OK · %d fallos' % (len(OK), len(FALLOS)))
for x in FALLOS[:60]:
    print('  FALLO', x)
sys.exit(1 if FALLOS else 0)

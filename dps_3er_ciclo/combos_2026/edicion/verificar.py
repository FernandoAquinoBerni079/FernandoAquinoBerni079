# -*- coding: utf-8 -*-
"""Controles del combo editado de un grado (información del productor; no sustituye la auditoría independiente).
Uso: python3 verificar.py 7|8|9  → verificacion/<grado>/CONTROLES.md (código 1 si hay fallos)."""
import sys, os, re, json, zipfile, hashlib
import docx, pymupdf
from docx.oxml.ns import qn
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import docx_ops as O
import config_grados as G

g = sys.argv[1]; C = G.GRADOS[g]; B = O.E
OUT = B + '../%s/' % C['carpeta']; V = B + '../verificacion/%s/' % C['carpeta']
OK, F, INFO = [], [], []


def ok(c, m):
    (OK if c else F).append(m)


nombres = [C['nombre_tomo'] + '.docx', C['nombre_tomo'] + '.pdf', C['nombre_pa'] + '.docx', C['nombre_planes'] + '.docx',
           C['nombre_sol'] + '.docx', C['nombre_sol'] + '.pdf']
ok(sorted(os.listdir(OUT)) == sorted(nombres), 'La carpeta del grado tiene exactamente los seis archivos: %s' % sorted(os.listdir(OUT)))
ok(not any(n.startswith((C['nombre_pa'], C['nombre_planes'])) and n.endswith('.pdf') for n in os.listdir(OUT)),
   'Sin PDF del Plan Anual ni de los Planes de Clase en la entrega')
CAPS = set(C['CAP'].values())
PROHIBIDOS = '✓✗✅✔✘☑'
RESIDUOS = (['continuación práctica', 'continuaciones prácticas'] if g == '9' else []) + ['Vinculado a la unidad de Orientación correspondiente', 'no capacidad literal MEC', 'fichas 1–7', 'articulado con la unidad correspondiente',
            'MINNA y el MITIC', 'Índice resumido. En Word', 'Mes 1:', 'Continuación práctica',
            'Vinculado a la unidad']

for n in nombres:
    if not n.endswith('.docx'):
        continue
    d = docx.Document(OUT + n)
    for i, s in enumerate(d.sections):
        w, h = round(s.page_width.cm, 1), round(s.page_height.cm, 1)
        ok(sorted((w, h)) == [21.6, 33.0], '%s · sección %d en oficio (%s × %s cm)' % (n, i + 1, w, h))
        ok(all(abs(x.cm - 1.27) < 0.02 for x in (s.left_margin, s.right_margin, s.top_margin, s.bottom_margin)),
           '%s · sección %d con márgenes de 1,27 cm' % (n, i + 1))
    xml = zipfile.ZipFile(OUT + n).read('word/document.xml').decode('utf8')
    for s_ in PROHIBIDOS:
        ok(s_ not in xml, '%s · sin el símbolo %s' % (n, s_))
    txt = '\n'.join(O.texto(p) for p in d.element.body.iter(qn('w:p')))
    for r in RESIDUOS:
        ok(r not in txt, '%s · sin el residuo «%s»' % (n, r))
    ok('[[' not in txt and '@@' not in txt, '%s · sin marcado sin procesar' % n)
    ok(d.element.body[0].find('.//' + qn('w:drawing')) is not None, '%s · portada con imagen en la primera página' % n)
    ok(not d.settings.element.findall(qn('w:updateFields')), '%s · sin pedido de actualizar campos al abrir (índices estáticos)' % n)
    ok(not any('presionar Ctrl+E' in O.texto(p) or 'presioná Ctrl+E' in O.texto(p) for p in d.element.body.iter(qn('w:p'))),
       '%s · sin índice dinámico vacío o desactualizado' % n)
    # bandas de unidad y filas PEC: «Capacidades…: «…» «…»» solo con capacidades del programa (sin paráfrasis)
    for p in d.element.body.iter(qn('w:p')):
        for t in [O.texto(p)] + [x.text or '' for x in p.iter(qn('w:t'))]:
            m = re.search(r'Capacidades[^:«]{0,60}: (.*)$', t)
            if m and not t.startswith(('Capacidades del área vinculadas', 'Capacidades evaluadas')) or (m and '«' in m.group(1)[:2]):
                resto = m.group(1).split(' Indicadores:')[0]
                if not resto.startswith('«'):
                    if t.startswith(('Capacidades:', 'Capacidades de la unidad')):
                        ok(False, '%s · banda de capacidades parafraseada: «%s»' % (n, t[:90]))
                    continue
                citas = re.findall(r'«([^»]+)»', resto)
                ok(citas and all(c in CAPS for c in citas), '%s · capacidades citadas del programa: «%s»' % (n, resto[:90]))
                break
    # capacidades: cada celda de ficha rotulada «Capacidad/es…» contiene solo capacidades literales del programa
    for t in d.element.body.iter(qn('w:tbl')):
        for tr in t.findall(qn('w:tr')):
            tcs = tr.findall(qn('w:tc'))
            if len(tcs) >= 2 and O.texto(tcs[0]).strip() in ('Capacidad', 'Capacidades', 'Capacidades evaluadas', 'Capacidades del área vinculadas'):
                for p in tcs[1].findall(qn('w:p')):
                    x = O.texto(p).strip().lstrip('• ').strip()
                    if not x or x.startswith('Objetivo del taller (elaboración editorial'):
                        continue
                    ok(x in CAPS, '%s · capacidad literal del programa: «%s»' % (n, x[:90]))

# concordancia PEC: indicadores de cada taller iguales en tomo (fuente), Plan Anual y Planes
import render as R
L = R.leer(C['pec_tomo']); IND = []; i = 0
while '[[FICHA_PEC]]' in L[i:]:
    i = L.index('[[FICHA_PEC]]', i); blk, i = R.bloque(L, i, '[[/FICHA_PEC]]')
    IND.append(['• ' + x[2:].strip() for x in blk if x.startswith('- ')])
IND = dict(zip('ABCDEF', IND))
pa = docx.Document(OUT + C['nombre_pa'] + '.docx')
for tr in pa.element.body.iter(qn('w:tr')):
    tcs = tr.findall(qn('w:tc'))
    m = re.match(r'^Taller PEC ([A-F]) — ', O.texto(tcs[1]).strip()) if len(tcs) >= 3 else None
    if m:
        ok([O.texto(p).strip() for p in tcs[2].findall(qn('w:p'))] == IND[m.group(1)], 'Plan Anual · indicadores del Taller %s iguales a la ficha del tomo' % m.group(1))
pl = docx.Document(OUT + C['nombre_planes'] + '.docx')
fs = [t for t in pl.element.body.iter(qn('w:tbl')) if O.texto(t.find('.//' + qn('w:tc'))).strip() == 'Capacidades del área vinculadas']
ok(len(fs) == 6, 'Planes · seis fichas de taller PEC')
for letra, t in zip('ABCDEF', fs):
    ok([O.texto(p).strip() for p in O.celda_de(t, 'Indicadores').findall(qn('w:p'))] == IND[letra], 'Planes · indicadores del Taller %s iguales a la ficha del tomo' % letra)
sol = '\n'.join(O.texto(p) for p in docx.Document(OUT + C['nombre_sol'] + '.docx').element.body.iter(qn('w:p')))
for letra, (enc, _) in C['talleres'].items():
    ok('Encuentro %d de 36 · Taller PEC %s' % (enc, letra) in sol, 'Solucionario · Taller %s en el encuentro %d' % (letra, enc))

# estructura PEC: cada taller abre con su ficha y el Solucionario trae respuestas para los seis
tomo = docx.Document(OUT + C['nombre_tomo'] + '.docx'); els = list(tomo.element.body)
for i, el in enumerate(els):
    t = O.texto(el).strip()
    if el.tag == qn('w:p') and re.match(r'^TALLER PEC [A-F] · ', t) and el.find('.//' + qn('w:tab')) is None:
        sig = els[i + 1]
        ok(sig.tag == qn('w:tbl') and O.texto(sig.find('.//' + qn('w:tc'))).strip() == 'Componente', 'Tomo · %s abre con su ficha PEC' % t[:14])
ok(len(re.findall(r'Respuestas esperadas', sol)) >= 6, 'Solucionario · respuestas esperadas para los seis talleres')

# cotejo literal: cada capacidad de la configuración figura tal cual en el PDF del programa MEC del grado
if C.get('programa'):
    f_, pags_ = C['programa']
    prog = pymupdf.open(B + '../fuentes_mec/' + f_)
    # se quita el número de página con que empieza cada página, para que una capacidad partida entre dos páginas se lea entera
    fuente = re.sub(r'\s+', ' ', ' '.join(re.sub(r'^\s*\d+\s', '', prog[i].get_text()) for i in pags_))
    INFO.append('Programa: %s (%s), págs. %d-%d' % (f_, re.sub(r'\s+', ' ', prog[1].get_text()).strip()[:90], pags_[0] + 1, pags_[-1] + 1))
    for k_, cap_ in C['CAP'].items():
        ok(re.sub(r'\s+', ' ', cap_).rstrip('.') in fuente, 'Capacidad %d literal en el programa MEC: «%s»' % (k_, cap_[:70]))

# DPS-03: TIEMPO = «3 HC» en los 36 encuentros del Plan Anual, con la nota de equivalencia
pa_ = docx.Document(OUT + C['nombre_pa'] + '.docx'); tiempos_ = []
for tb in pa_.element.body.iter(qn('w:tbl')):
    hdr = [O.texto(c_).strip() for c_ in tb.findall(qn('w:tr'))[0].findall(qn('w:tc'))]
    if 'TIEMPO' in hdr:
        j_ = hdr.index('TIEMPO')
        tiempos_ += [O.texto(tr.findall(qn('w:tc'))[j_]).strip() for tr in tb.findall(qn('w:tr'))[1:]
                     if len(tr.findall(qn('w:tc'))) > j_ and re.match(r'^\d+$', O.texto(tr.findall(qn('w:tc'))[0]).strip())]
ok(len(tiempos_) == 36 and set(tiempos_) == {'3 HC'}, 'Plan Anual · TIEMPO «3 HC» en los 36 encuentros %s' % sorted(set(tiempos_)))
ok(any('equivalen a 120 minutos' in O.texto(p) for p in pa_.element.body.iter(qn('w:p'))), 'Plan Anual · nota: 3 HC equivalen a 120 minutos')
ok(all(tr.find('.//' + qn('w:cantSplit')) is not None for tb in pa_.element.body.iter(qn('w:tbl')) for tr in tb.findall(qn('w:tr'))),
   'Plan Anual · ninguna fila puede partirse entre páginas')
# índice de los Planes de Clase contra el PDF de control (las páginas del índice son las de esa renderización)
ctrl = B + '../verificacion/%s/control_pdf/%s.pdf' % (C['carpeta'], C['nombre_planes'])
pl_ = docx.Document(OUT + C['nombre_planes'] + '.docx')
def con_tab(p):
    """«título\tpágina» si el párrafo es una entrada de índice (título, tabulación, número)."""
    partes, tab = ['', ''], 0
    for el in p.iter(qn('w:t'), qn('w:tab')):
        if el.tag == qn('w:tab'):
            if el.getparent().tag == qn('w:r'):     # el tabulador del texto, no la definición de la tabulación
                tab = 1
        else:
            partes[tab] += el.text or ''
    return partes[0] + '\t' + partes[1] if tab and partes[1].strip().isdigit() else None
ent_ = [con_tab(p) for p in pl_.element.body.iter(qn('w:p')) if re.match(r'^(Plan de Clase|PLAN DE CLASE) N\.º \d+', O.texto(p))]
ent_ = [e for e in ent_ if e]
if ent_ and os.path.exists(ctrl):
    pdfp = [re.sub(r'\s+', '', p_.get_text()) for p_ in pymupdf.open(ctrl)]
    mal_ = [e for e in ent_ if re.sub(r'\s+', '', e.split('\t')[0])[:30] not in pdfp[int(e.split('\t')[-1]) - 1]]
    ok(len(ent_) == 36 and not mal_, 'Planes · índice de %d planes con su página %s' % (len(ent_), mal_[:2]))

# imágenes del tomo: todas las de la base candidata siguen, byte a byte
base = O.media_sha(C['base_tomo']); nuevo = O.media_sha(OUT + C['nombre_tomo'] + '.docx')
corr = C.get('imagenes_corregidas', {})
faltan = {h for n_, h in base.items() if n_ not in corr} - set(nuevo.values())
ok(not faltan, 'Tomo: las %d imágenes de la base candidata se conservan idénticas (SHA-256)%s' % (len(base) - len(corr), ' salvo las corregidas a propósito' if corr else ''))
for n_, ruta in corr.items():
    ok(nuevo.get(n_) == hashlib.sha256(open(ruta, 'rb').read()).hexdigest(), 'Tomo: %s reemplazada por su versión corregida' % n_)
INFO.append('Imágenes del tomo: base %d · editado %d (la diferencia es la portada)' % (len(base), len(nuevo)))

# PDF
for n in (C['nombre_tomo'] + '.pdf', C['nombre_sol'] + '.pdf'):
    doc = pymupdf.open(OUT + n)
    tam = {(round(p.rect.width), round(p.rect.height)) for p in doc}
    ok(tam <= {(612, 936), (612, 935)}, '%s · todas las páginas en oficio %s' % (n, tam))
    INFO.append('%s: %d páginas' % (n, doc.page_count))
    vac = [i + 1 for i, p in enumerate(doc) if 0 < i < len(doc) - 1 and O.llenado(p) < 0.12]
    ok(not vac, '%s · sin páginas en blanco o residuales (llenado < 12 %%): %s' % (n, vac))
    solo = [i + 1 for i, p in enumerate(doc) if p.get_text().strip().startswith('Espacio para anotaciones')]
    ok(not solo, '%s · ninguna página contiene solo el espacio para anotaciones: %s' % (n, solo))

# índice del tomo contra el PDF
J = json.load(open(V + 'indice_tomo.json'))
doc = pymupdf.open(OUT + C['nombre_tomo'] + '.pdf')
norm = [re.sub(r'\s+', '', p.get_text()) for p in doc]
mal = [t for (niv, t), pg in zip(J['entradas'], J['paginas']) if re.sub(r'\s+', '', t.split(' / ')[0])[:40] not in norm[pg - 1]]
ok(not mal, 'Índice del tomo: las %d entradas coinciden con la página del PDF %s' % (len(J['entradas']), mal[:3]))

# índice del Solucionario contra su PDF; la portada de texto de la candidata no se repite
if os.path.exists(V + 'indice_sol.json'):
    J = json.load(open(V + 'indice_sol.json'))
    doc = pymupdf.open(OUT + C['nombre_sol'] + '.pdf')
    norm = [re.sub(r'\s+', '', p.get_text()) for p in doc]
    mal = [t for (niv, t, _), pg in zip(J['entradas'], J['paginas']) if re.sub(r'\s+', '', t)[:40] not in norm[pg - 1]]
    ok(not mal, 'Índice del Solucionario: las %d entradas coinciden con la página del PDF %s' % (len(J['entradas']), mal[:3]))
doc = pymupdf.open(OUT + C['nombre_sol'] + '.pdf')
ok('Material exclusivo del docente' not in doc[1].get_text()[:300] or 'DESARROLLO PERSONAL Y SOCIAL' not in doc[1].get_text()[:60],
   'Solucionario · la portada de texto anterior no se repite después de la portada')

# DOCX ↔ PDF: el texto de cada título del índice está en el PDF; el PDF se generó desde el .docx entregado
for n in (C['nombre_tomo'], C['nombre_sol']):
    ok(os.path.getmtime(OUT + n + '.pdf') >= os.path.getmtime(OUT + n + '.docx') - 5, '%s · PDF generado a partir del .docx entregado' % n)

os.makedirs(V, exist_ok=True)
R = ['# Controles del combo %s — Desarrollo Personal y Social' % C['grado'], '',
     'Generado por `edicion/verificar.py`. Son controles del productor: no reemplazan la auditoría independiente.', '',
     '**%d controles correctos · %d fallos**' % (len(OK), len(F)), '']
if F:
    R += ['## Fallos', ''] + ['- ' + x for x in F] + ['']
R += ['## Datos', ''] + ['- ' + x for x in INFO] + ['', '## Controles correctos', ''] + ['- ' + x for x in OK]
open(V + 'CONTROLES.md', 'w').write('\n'.join(R) + '\n')
sha = ['| Archivo | Bytes | SHA-256 |', '|---|---|---|'] + ['| %s | %d | `%s` |' % (n, os.path.getsize(OUT + n), hashlib.sha256(open(OUT + n, 'rb').read()).hexdigest()) for n in nombres]
open(V + 'SHA256_ENTREGA.md', 'w').write('\n'.join(sha) + '\n')
print('%d OK · %d fallos' % (len(OK), len(F)))
for x in F[:40]:
    print('  FALLO', x)
for x in INFO:
    print('  ', x)
sys.exit(1 if F else 0)

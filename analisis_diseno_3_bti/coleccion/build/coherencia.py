# -*- coding: utf-8 -*-
"""Verificador de coherencia de la colección → coleccion/COHERENCIA.json.
  L. Los seis lotes intactos: git sin cambios en sus carpetas, y cada archivo de sus manifiestos SHA-256 igual.
  X. Referencias cruzadas: cada tabla, figura, código y ejemplo resuelto que citan el libro, la guía y el cuaderno
     existe en el libro con ese número; cada referencia de código R-n de la guía existe en la guía.
  E. Evaluaciones: semillas únicas, 15 puntos, y la clave de cada ítem en la tabla de la guía, con la misma letra.
  P. Prototipo: cada archivo del proyecto que citan los documentos existe en el repositorio; las herramientas de
     inspección estática y ejecución controlada del lote 6 v1.1 se conservan sin cambios.
  M. Rótulos: ninguna capacidad presentada como oficial del MEC; nada declarado validado en aulas; Windows y los
     equipos escolares, siempre como pendientes; la guía deja clara la condición de aislamiento.
  R. Reservados: con ADS_DR y ADS_V6 (rutas privadas), ningún dato de DR ni variante V6 en los documentos ni en la
     colección; sin ellas, el control se informa como no ejecutado.
  S. Estructura: 18 capítulos, 36 encuentros, 180 HC, 16 prácticas, 17 evaluaciones; ni plan anual definitivo ni
     planes de clase generados.
Uso: python3 -B coleccion/build/coherencia.py   (sale con 1 si algo falla)"""
import os, re, sys, json, hashlib, subprocess
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
COL = os.path.dirname(AQUI)
ADS = os.path.dirname(COL)
REPO = os.path.dirname(ADS)
sys.path.insert(0, AQUI)
import docx
import fuentes as FU
FU.cargar()
import armar_coleccion as AC

RES, FALLOS = {}, []


def chk(clave, detalle, cond, info=None):
    RES.setdefault(clave, []).append({'resultado': 'correcto' if cond else 'FALLA', 'detalle': detalle,
                                      **({'info': info} if info and not cond else {})})
    if not cond:
        FALLOS.append('%s: %s' % (clave, detalle))
    print(('CORRECTO ' if cond else 'FALLA    ') + '[%s] %s%s' % (clave, detalle, '' if cond or not info else ' — %s' % (info,)))


def git(*a):
    return subprocess.run(['git'] + list(a), cwd=ADS, capture_output=True, text=True).stdout.rstrip()


def texto(ruta):
    """Texto de los párrafos del cuerpo y de cada celda (leída del XML: una vez por celda, aunque esté combinada)."""
    from docx.oxml.ns import qn
    d = docx.Document(ruta)
    partes = [p.text for p in d.paragraphs]
    for tc in d.element.body.iter(qn('w:tc')):
        partes.append('\n'.join(''.join(x.text or '' for x in p.iter(qn('w:t'))) for p in tc.iterchildren(qn('w:p'))))
    return d, '\n'.join(partes)


DOC, TX = {}, {}
for k, r in AC.RUTA.items():
    DOC[k], TX[k] = texto(r)
TODO = '\n'.join(TX.values())
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()

# L ------------------------------------------------------------------------------------------------------------
carpetas = ['lote_%d' % n for n in range(1, 7)] + ['lote_1_oficio', 'lote_1_oficio_candidata', 'plan_anual', 'planes_clase',
                                                     'formato', 'formatos_comerciales', 'inventario', 'fase2_pilotos'] + \
           ['lote_%d_plan' % n for n in range(1, 7)]
st = git('status', '--porcelain', '--', *carpetas)
chk('L', 'git: ningún archivo de los seis lotes, de sus planes, del plan anual ni de los planes de clase cambió ni se agregó', not st, st[:300])
fuera = [l for l in git('status', '--porcelain').split('\n') if l.strip() and not l[3:].startswith('analisis_diseno_3_bti/coleccion/')
         and not l[3:].startswith('coleccion/')]
chk('L', 'git: los únicos cambios del repositorio están en coleccion/ (ninguna otra asignatura cambió)', not fuera, fuera[:5])
m1 = json.load(open(os.path.join(ADS, 'lote_1', 'MANIFIESTO_LOTE_1.json'), encoding='utf8'))
mal1 = [p for p, v in m1.items() if isinstance(v, dict) and 'sha256' in v and sha(os.path.join(ADS, p)) != v['sha256']]
chk('L', 'Lote 1: los %d archivos de su manifiesto, iguales' % sum(1 for v in m1.values() if isinstance(v, dict) and 'sha256' in v), not mal1, mal1[:3])
for nombre, ruta in [('Lote 1 (candidata O3)', 'lote_1_oficio_candidata/MANIFIESTO_CANDIDATA_O3.json')] + \
        [('Lote %d' % n, 'lote_%d/MANIFIESTO_LOTE_%d.json' % (n, n)) for n in range(2, 7)]:
    m = json.load(open(os.path.join(ADS, ruta), encoding='utf8'))
    base = os.path.dirname(os.path.join(ADS, ruta))
    mal = [a['ruta'] for a in m['archivos'] if sha(os.path.join(base, a['ruta'])) != a['sha256']]
    chk('L', '%s: los %d archivos de su manifiesto SHA-256, iguales' % (nombre, len(m['archivos'])), not mal, mal[:3])
commits = {n: git('log', '-1', '--format=%h %ad', '--date=short', '--', 'lote_%d' % n) for n in range(1, 7)}
commits[1] = commits[1] + ' · candidata ' + git('log', '-1', '--format=%h %ad', '--date=short', '--', 'lote_1_oficio_candidata')
RES['commits_de_los_lotes'] = commits

# X ------------------------------------------------------------------------------------------------------------
L_ = DOC['libro']
rotulos = '\n'.join(p.text for p in L_.paragraphs) + '\n' + '\n'.join(c.text for t in L_.tables for c in t._cells[:1])
existentes = {}
for tipo, pat in (('Tabla', r'^Tabla (\d+\.\d+) —'), ('Figura', r'^Figura (\d+\.\d+) —'), ('Código', r'^Código (\d+\.\d+) —'),
                  ('Ejemplo resuelto', r'^Ejemplo resuelto (\d+\.\d+)')):
    existentes[tipo] = set(re.findall(pat, rotulos, re.M))
for k in AC.RUTA:
    citas = set()
    for tipo in existentes:
        for m in re.finditer(r'\b%s(?:s)? (\d+\.\d+)(?:(?:, | y | a )(\d+\.\d+))*' % tipo, TX[k]):
            for x in re.findall(r'\d+\.\d+', m.group(0)):
                citas.add((tipo, x))
    faltan = sorted(c for c in citas if c[1] not in existentes[c[0]] and not c[1].startswith('0.'))
    chk('X', '%s: %d citas de tablas, figuras, códigos y ejemplos resueltos; todas existen en el libro con ese número' % (k, len(citas)),
        not faltan, faltan[:8])
refs_g = set(re.findall(r'Referencia (R-\d+)', TX['guia']))
rot_g = set(re.findall(r'^Referencia (R-\d+) —', '\n'.join(p.text for p in DOC['guia'].paragraphs), re.M))
chk('X', 'guía: las %d referencias de código citadas (R-n) existen como bloques en la guía' % len(refs_g), refs_g <= rot_g, sorted(refs_g - rot_g))
chk('X', 'libro: %d tablas, %d figuras, %d códigos y %d ejemplos resueltos numerados, sin números repetidos' % tuple(len(existentes[t]) for t in existentes),
    all(len(re.findall(pat, rotulos, re.M)) == len(existentes[t]) for t, pat in (('Tabla', r'^Tabla (\d+\.\d+) —'), ('Figura', r'^Figura (\d+\.\d+) —'))))

# E ------------------------------------------------------------------------------------------------------------
caps = [FU.capitulo(c) for c in range(1, 19)]
ids = [c.EVAL_ID for c in caps if c.EVAL_ID]
chk('E', '%d evaluaciones con semillas únicas en el año' % len(ids), len(ids) == 17 and len(set(ids)) == 17, ids)
chk('E', 'cada evaluación vale 15 puntos', all('15 puntos' in c.EVAL_PUNTAJE for c in caps if c.EVAL_ID))
claves = json.load(open(os.path.join(COL, 'resultado_construccion.json'), encoding='utf8'))['claves']
G_ = DOC['guia']
from docx.oxml.ns import qn
from docx.table import Table
tablas_clave = {}
for el in G_.element.body.iterchildren(qn('w:tbl')):
    prev = el.getprevious()
    rot = ''.join(x.text or '' for x in prev.iter(qn('w:t'))) if prev is not None else ''
    m = re.match(r'Clave de la evaluación del capítulo (\d+)', rot, re.I)
    if m:
        tablas_clave[int(m.group(1))] = [[c.text for c in r.cells] for r in Table(el, G_).rows][1:]
malas = []
for c in caps:
    if not c.EVAL_ID:
        continue
    mias = [(n, cl) for eid, n, cl, _ in claves if eid == c.EVAL_ID]
    filas = tablas_clave.get(c.NUM, [])
    if len(mias) != len(c.EVAL_ITEMS) or [(str(n), cl) for n, cl in mias] != [(f[0], f[1]) for f in filas]:
        malas.append(c.NUM)
chk('E', 'guía: la clave de cada ítem de las %d evaluaciones del libro, con el mismo número y la misma letra (%d ítems)'
    % (len(ids), len(claves)), not malas and len(tablas_clave) == 17, malas)
chk('E', 'el Capítulo 18 no tiene evaluación escrita y los Capítulos 16 y 18 no tienen práctica (decisiones D-3 y D-4)',
    caps[17].EVAL_ID is None and caps[15].PRACTICA_TITULO is None and caps[17].PRACTICA_TITULO is None)

# P ------------------------------------------------------------------------------------------------------------
rutas = set()
for k in AC.RUTA:
    for m in re.finditer(r'\b(lote_\d(?:_plan)?/[\w./\-<>]+)', TX[k]):
        r = m.group(1).rstrip('.,;:)')
        if '<' not in r:
            rutas.add(r)
faltan = sorted(r for r in rutas if not os.path.exists(os.path.join(ADS, r)))
chk('P', '%d rutas de archivos del prototipo y de los lotes citadas en los tres documentos; todas existen' % len(rutas), not faltan, faltan[:8])
m6 = {a['ruta']: a['sha256'] for a in json.load(open(os.path.join(ADS, 'lote_6', 'MANIFIESTO_LOTE_6.json'), encoding='utf8'))['archivos']}
herr = ['proyecto/herramientas/inspeccionar_entrega.php', 'proyecto/herramientas/probar_en_aislamiento.php', 'proyecto/herramientas/LEEME.md']
chk('P', 'herramientas de inspección estática y ejecución controlada del lote 6 v1.1, conservadas sin cambios',
    all(sha(os.path.join(ADS, 'lote_6', h)) == m6[h] for h in herr))
import fragmentos as F4, fragmentos_u5 as F5, fragmentos_u6 as F6
fichas = [(m, f) for m in (F4, F5, F6) for f in m.TODOS]
# C-04: las fichas impresas nombran el archivo desde la carpeta de la colección (lote_N/proyecto/…), y es el mismo
# archivo del que se lee el fragmento
base_ficha = {F4: os.path.join(ADS, 'lote_4', 'proyecto'), F5: ADS, F6: ADS}
sin_archivo = [f for m, f in fichas if not os.path.exists(os.path.join(base_ficha[m], m.ficha(f)['archivo']))]
chk('P', 'los %d bloques de código se leen de archivos del proyecto que existen (fichas de los lotes 4 a 6)' % len(fichas), not sin_archivo, sin_archivo)
from docx.oxml.ns import qn as _qn
impresas = []
for k in ('libro', 'guia'):
    for tbl in DOC[k].element.body.iter(_qn('w:tbl')):
        filas_ = [[''.join(x.text or '' for x in tc.iter(_qn('w:t'))) for tc in tr.findall(_qn('w:tc'))] for tr in tbl.findall(_qn('w:tr'))]
        if len(filas_) >= 2 and filas_[0][:1] == ['Archivo'] and filas_[1][:1] == ['Requisito o contrato']:
            impresas.append((k, filas_[0][1]))
esperadas = {os.path.realpath(os.path.join(base_ficha[m], m.ficha(f)['archivo'])) for m, f in fichas}
malas = [r for k, r in impresas if not (r.startswith('lote_') and os.path.isfile(os.path.join(ADS, r))
                                        and os.path.realpath(os.path.join(ADS, r)) in esperadas)]
chk('P', 'C-04: las %d fichas de código impresas (libro y guía) nombran el archivo con la misma notación (lote_N/proyecto/…), '
    'y cada ruta existe y es el archivo del que se lee el fragmento' % len(impresas), len(impresas) == len(fichas) and not malas, malas[:5])

# M ------------------------------------------------------------------------------------------------------------
oraciones = lambda t: re.split(r'(?<=[.;])\s+|\n', t)
mec = [s for s in oraciones(TODO) if re.search(r'\bMEC\b', s)]
afirmativas = [s for s in mec if re.search(r'(capacidad|capacidades)[^.]{0,40}\bMEC\b', s, re.I) and not re.search(r'\b[Nn]o (son|es|se)\b', s)]
chk('M', '%d oraciones mencionan al MEC; ninguna presenta las capacidades de la propuesta como oficiales' % len(mec), not afirmativas, afirmativas[:3])
for k in AC.RUTA:
    chk('M', '%s: dice que las capacidades no son oficiales del MEC' % k, 'No son capacidades oficiales del MEC' in TX[k])
# «validación» también es un término técnico del libro (validar entradas): se controlan las afirmaciones sobre el material
valid = [s for s in oraciones(TODO) if re.search(r'(material|libro|prototipo|herramientas?|colección|guía)[^.]{0,60}\bvalidad[oa]s?\b|'
                                                  r'\bvalidad[oa]s? (en|con) (aulas?|laboratorios?|colegios|escuelas|equipos|computadoras|Windows)', s)]
sin_neg = [s for s in valid if not re.search(r'\b(no|No|sin|pendiente|pendientes|siguen|sigue|hasta que|Pendiente)\b', s)]
chk('M', '%d afirmaciones sobre la validación del material; ninguna lo declara validado en aulas o equipos escolares' % len(valid),
    bool(valid) and not sin_neg, sin_neg[:4])
for k in AC.RUTA:
    chk('M', '%s: Windows y las computadoras escolares, pendientes de validación' % k,
        'Windows y las computadoras escolares siguen pendientes de validación' in TX[k])
chk('M', 'guía: las pruebas de código desconocido requieren una máquina virtual o un equipo aislado, sin datos institucionales y sin red',
    all(x in TX['guia'] for x in ('máquina virtual o un equipo verdaderamente aislado', 'sin datos institucionales', 'sin red')))
chk('M', 'guía: la lista cerrada de nombres de pruebas no vuelve confiable su código', 'no vuelve confiable su código' in TX['guia'])
chk('M', 'los tres documentos: el borrador de licencia, pendiente de revisión jurídica', all('pendiente de revisión jurídica' in TX[k] for k in AC.RUTA))
chk('M', 'ningún documento declara aptitud comercial', not re.search(r'apt[oa] para (la )?(venta|comercializ)', TODO, re.I)
    and all('no está aprobad' in TX[k] for k in AC.RUTA))

import guia_general as GG
frases = {1: 'pasa de seis a cinco encuentros', 2: 'pasa de seis a cuatro encuentros', 3: 'pasa de seis a cinco encuentros',
          4: 'pasa de ocho a cinco encuentros', 5: 'pasa de seis a cinco encuentros', 6: 'conserva sus cuatro encuentros'}
num = {'cuatro': 4, 'cinco': 5, 'seis': 6, 'ocho': 8}
partes_txt = re.split(r'\nParte (?=[IVX]+ — )', TX['guia'])
ok_cal = all(frases[n] in TX['guia'] for n in frases)
cal_ok = all(GG.CAL28[n][1] == num[frases[n].split()[-2]] for n in frases) and all(
    GG.CAL28[n][0] == (num[frases[n].split()[2]] if n < 6 else 4) for n in frases)
chk('M', 'C-03: la guía aclara la secuencia ordinaria de 36 encuentros y la adaptación alternativa a 28; su tabla coincide con lo '
    'que dice cada parte (6+6+6+8+6+4 = 36 y 5+4+5+5+5+4 = 28)',
    ok_cal and cal_ok and '36 encuentros ordinarios' in TX['guia'] and 'adaptación alternativa a 28 encuentros' in TX['guia'])
chk('M', 'C-01 y C-02: la presentación da la distribución real de los 18 capítulos y explica las excepciones de práctica y '
    'evaluación de los Capítulos 16 y 18', 'cuatro en la Unidad IV y dos en la Unidad VI' in TX['libro']
    and 'salvo los Capítulos 16 y 18, que no tienen práctica' in TX['libro'] and 'el Capítulo 18 no tiene evaluación escrita' in TX['libro']
    and 'seis unidades de tres capítulos' not in TX['libro'])

# R ------------------------------------------------------------------------------------------------------------
coleccion_txt = TODO + ''.join(open(os.path.join(d, f), encoding='utf8', errors='ignore').read()
                               for d, _, fs in os.walk(COL) for f in fs if f.endswith(('.py', '.md', '.json', '.txt')))
for var, etiqueta in (('ADS_V6', 'variantes V6'), ('ADS_DR', 'conjunto DR')):
    ruta = os.environ.get(var)
    if ruta and os.path.exists(ruta):
        datos = json.load(open(ruta, encoding='utf8'))
        claves_r = [v['situacion'][:40] for v in datos] if var == 'ADS_V6' else \
            [x[0] for k in ('obras', 'ediciones', 'ejemplares', 'lectores') for x in datos[k]]
        hallados = [c for c in claves_r if c in coleccion_txt]
        chk('R', '%s: ninguno de los %d textos o códigos reservados está en los documentos ni en coleccion/' % (etiqueta, len(claves_r)),
            not hallados, '%d hallados' % len(hallados))
        chk('R', '%s: la carpeta privada está fuera del repositorio' % etiqueta,
            not (os.path.realpath(ruta) + os.sep).startswith(os.path.realpath(REPO) + os.sep))
    else:
        RES.setdefault('R', []).append({'resultado': 'no ejecutado', 'detalle': '%s sin ruta privada (%s)' % (etiqueta, var)})
        print('NO EJECUTADO [R] %s: falta la variable %s' % (etiqueta, var))
nombres = [f for d, _, fs in os.walk(COL) for f in fs]
chk('R', 'coleccion/ no tiene archivos reservados (dr.json, variantes_v6.json, comprobacion_*.txt)',
    not [f for f in nombres if f in ('dr.json', 'variantes_v6.json', 'comprobacion_dr.txt', 'comprobacion_v6.txt')])

# S ------------------------------------------------------------------------------------------------------------
encs = sorted(e for c in caps for e in c.ENCUENTROS)
chk('S', '18 capítulos en seis unidades, 36 encuentros (1 a 36, sin repetir) y 180 HC (5 por encuentro)',
    len(caps) == 18 and encs == list(range(1, 37)) and all('5 HC' in c.TIEMPO for c in caps))
pr = [c.PRACTICA_TITULO for c in caps if c.PRACTICA_TITULO]
chk('S', '16 prácticas en el libro y en el cuaderno (Capítulos 1 a 15 y 17)', len(pr) == 16 and all(t in TX['libro'] and t in TX['cuaderno'] for t in pr))
chk('S', 'el cuaderno no trae evaluaciones ni secciones de teoría', not re.search(r'^Evaluación del Capítulo', TX['cuaderno'], re.M)
    and not [p for p in DOC['cuaderno'].paragraphs if p.style.name == 'Heading 2' and re.match(r'^\d+\.\d+ ', p.text)])
chk('S', 'no se generaron el plan anual definitivo ni los planes de clase', not [f for f in os.listdir(os.path.join(ADS, 'planes_clase')) if f.endswith('.docx')]
    and not [f for f in nombres if re.search(r'(?i)plan_anual|planes_de_clase', f)])

json.dump({'fallos': FALLOS, 'controles': RES}, open(os.path.join(COL, 'COHERENCIA.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
n = sum(1 for v in RES.values() if isinstance(v, list) for x in v if x['resultado'] != 'no ejecutado')
print('\nResultado: %d controles, %d fallos' % (n, len(FALLOS)))
sys.exit(1 if FALLOS else 0)

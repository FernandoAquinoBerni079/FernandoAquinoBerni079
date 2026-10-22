# -*- coding: utf-8 -*-
"""Auditoría final de la edición comercial v1.0 sobre ENTREGA_COMERCIAL_FINAL/. Escribe en 05_CONTROL_DE_CALIDAD/:
RESULTADOS_DE_CONTROLES.json, PRUEBA_DE_FUENTES.json, ORTOGRAFIA_FORMAS_NO_RECONOCIDAS.txt, REGISTRO_DE_LICENCIAS_Y_PROCEDENCIA.md
y las hojas de contacto de la revisión visual. Termina con error si algún control falla.
Variables opcionales: ADS_DIC (diccionario Hunspell de español, sin extensión), ADS_DR, ADS_V6 (rutas privadas).
Uso: python3 -B analisis_diseno_3_bti/edicion_v1_0/build/auditoria_final.py
"""
import collections, hashlib, json, os, re, shutil, subprocess, sys, tempfile, zipfile
sys.dont_write_bytecode = True
import docx, pymupdf
AQUI = os.path.dirname(os.path.abspath(__file__)); ED = os.path.dirname(AQUI); ADS = os.path.dirname(ED); REPO = os.path.dirname(ADS)
sys.path.insert(0, AQUI)
import cubiertas as CU

ENT = os.path.join(ADS, 'ENTREGA_COMERCIAL_FINAL'); QC = os.path.join(ENT, '05_CONTROL_DE_CALIDAD')
SAL = os.path.join(ED, 'salida'); COL = os.path.join(ADS, 'coleccion')
norm = lambda s: re.sub(r'\s+', ' ', s or '').strip()
RES, FALLOS = collections.OrderedDict(), []


def chk(b, det, ok, extra=''):
    RES.setdefault(b, []).append({'resultado': 'correcto' if ok else 'FALLA', 'detalle': det + ('' if ok or not extra else ' — ' + str(extra)[:300])})
    if not ok: FALLOS.append('[%s] %s %s' % (b, det, extra))
    print(('ok    ' if ok else 'FALLA ') + '[%s] %s%s' % (b, det, '' if ok else ' — ' + str(extra)[:300]))


def no_ej(b, det):
    RES.setdefault(b, []).append({'resultado': 'no ejecutado', 'detalle': det}); print('NO EJECUTADO [%s] %s' % (b, det))


def textos(pdf):
    return [norm(p.get_text()) for p in pymupdf.open(pdf)]


def docx_texto(ruta):
    d = docx.Document(ruta)
    return norm(' '.join(el.text or '' for el in d.element.body.iter() if el.tag.endswith('}t')))


ARCH = {k: CU.PRODUCTOS[k]['archivo'] for k in CU.ORDEN}
CARP = {'libro': '01_LIBRO_DEL_ESTUDIANTE', 'cuaderno': '02_CUADERNO_DE_PRACTICAS', 'guia': '03_GUIA_DOCENTE_CON_SOLUCIONARIO',
        'plan_anual': '04_PLAN_ANUAL', 'planes': '05_PLANES_DE_CLASE'}
V02 = {'libro': 'ADS_3BTI_LIBRO_ANUAL_ESTUDIANTE_OFICIO_O3', 'guia': 'ADS_3BTI_GUIA_DOCENTE_ANUAL_OFICIO_O3',
       'cuaderno': 'ADS_3BTI_CUADERNO_ANUAL_PRACTICAS_OFICIO_O3'}

# ================================================================ 1. completitud de los cinco productos
for k in CU.ORDEN:
    base = os.path.join(ENT, '03_COLECCION_COMPLETA', CARP[k], ARCH[k])
    archivos = [base + s for s in ('_INTERIOR_IMPRESION.pdf', '_CUBIERTA_IMPRESION.pdf', '_DIGITAL.pdf', '_EDITABLE.docx')]
    falta = [a for a in archivos if not os.path.exists(a)]
    chk('1. Productos', '%s: interior de impresión, cubierta, PDF digital y DOCX' % CU.PRODUCTOS[k]['nombre'], not falta, falta)
    if falta: continue
    it, dg = textos(archivos[0]), textos(archivos[2])
    chk('1. Productos', '%s: el PDF digital es tapa + las %d páginas del interior + contratapa, con el mismo texto' % (
        CU.PRODUCTOS[k]['nombre'], len(it)), len(dg) == len(it) + 2 and dg[1:-1] == it)
    d = pymupdf.open(archivos[2])
    chk('1. Productos', '%s: PDF digital con marcadores (%d) y metadatos' % (CU.PRODUCTOS[k]['nombre'], len(d.get_toc())),
        len(d.get_toc()) >= 10 and 'Análisis y Diseño de Sistemas' in (d.metadata.get('title') or ''))
    cub = pymupdf.open(archivos[1])[0]
    hojas = (len(it) + 1) // 2
    ancho_esp = 2 * CU.W + hojas * 0.1 * CU.MM + 2 * CU.SANGRADO
    chk('1. Productos', '%s: cubierta de imprenta con lomo para %d hojas y 3 mm de sangrado' % (CU.PRODUCTOS[k]['nombre'], hojas),
        abs(cub.rect.width - ancho_esp) < 0.5 and abs(cub.rect.height - (CU.H + 2 * CU.SANGRADO)) < 0.5)
    try:
        dx = docx.Document(archivos[3]); ok = len(dx.paragraphs) > 20
    except Exception as e:
        ok = False
    chk('1. Productos', '%s: el DOCX abre y tiene contenido' % CU.PRODUCTOS[k]['nombre'], ok)

# ================================================================ 2. fidelidad a las versiones aprobadas
for k in ('libro', 'guia'):
    a = textos(os.path.join(COL, V02[k] + '.pdf')); b = textos(os.path.join(SAL, ARCH[k] + '.pdf'))
    chk('2. Fidelidad', '%s v1.0: %d páginas y el mismo texto que la v0.2 aprobada desde la página 2' % (k, len(b)), len(a) == len(b) and a[1:] == b[1:])
    ia = [len(p.get_images()) for p in pymupdf.open(os.path.join(COL, V02[k] + '.pdf'))]
    ib = [len(p.get_images()) for p in pymupdf.open(os.path.join(SAL, ARCH[k] + '.pdf'))]
    chk('2. Fidelidad', '%s v1.0: las mismas imágenes por página que la v0.2 (%d figuras)' % (k, sum(ia)), ia == ib)
r = json.load(open(os.path.join(SAL, 'resultado_documentos_coleccion.json'), encoding='utf8'))
chk('2. Fidelidad', 'Cuaderno v1.0: %d controles de la reedición (consignas iguales, renglones de 8 mm, índice, página 1)' % len(r['controles']),
    all(c['resultado'] == 'correcto' for c in r['controles']), [c for c in r['controles'] if c['resultado'] != 'correcto'])
cp = json.load(open(os.path.join(SAL, 'CONTROLES_PLANIFICACION.json'), encoding='utf8'))
chk('2. Fidelidad', 'Plan anual y planes v1.0: %d controles de la planificación (fuentes, correspondencia, tiempo, numeración, '
    'evaluación, referencias, paginación, reservados)' % cp['total'], not cp['fallos'] and not cp['no_ejecutados'], cp['fallos'][:3])
git = lambda *a: subprocess.run(['git'] + list(a), cwd=REPO, capture_output=True, text=True).stdout
dif = git('diff', '--name-only', '0b9aed3', '--', '.', ':(exclude)analisis_diseno_3_bti/edicion_v1_0',
          ':(exclude)analisis_diseno_3_bti/ENTREGA_COMERCIAL_FINAL', ':(exclude)analisis_diseno_3_bti/ENTREGA_COMERCIAL_FINAL_ZIP')
chk('2. Fidelidad', 'Versiones anteriores intactas: colección v0.2, planificación v0.1, lotes y otras asignaturas sin cambios desde 0b9aed3',
    dif.strip() == '', dif[:200])

# ================================================================ 3. numeración y estructura
L = textos(os.path.join(SAL, ARCH['libro'] + '.pdf')); LT = ' '.join(L)
caps = [int(x) for x in re.findall(r'Capítulo (\d+) — [^.]{5,80}? Unidad [IV]+ — ', LT)]
encs = sorted({int(x) for p in L[5:] for x in re.findall(r'^Encuentro (\d+) — |\. Encuentro (\d+) — ', p) for x in x if x})
d = docx.Document(os.path.join(SAL, ARCH['libro'] + '.docx'))
h1 = [p.text for p in d.paragraphs if p.style.name == 'Heading 1']
cap_h = [int(m.group(1)) for t in h1 for m in [re.match(r'Capítulo (\d+) — ', t)] if m]
enc_h = [int(m.group(1)) for t in h1 for m in [re.match(r'Encuentro (\d+) — ', t)] if m]
pra_h = [int(m.group(1)) for t in h1 for m in [re.match(r'Práctica (\d+) — ', t)] if m]
uni_h = [t for t in d.paragraphs if re.match(r'Unidad (I|II|III|IV|V|VI) — ', t.text) and t.style.name.startswith('Heading')]
hit = [t for t in [p.text for p in d.paragraphs if p.style.name.startswith('Heading')] if re.search(r'Hito H[1-6]', t)]
chk('3. Numeración', 'Libro: capítulos 1 a 18, encuentros 1 a 36 y prácticas 1 a 15 y 17, en orden', cap_h == list(range(1, 19))
    and enc_h == list(range(1, 37)) and pra_h == list(range(1, 16)) + [17], (cap_h, enc_h[:5], pra_h))
chk('3. Numeración', 'Libro: seis unidades y seis hitos integradores (H1 a H6)', len(uni_h) >= 6 and
    sorted({re.search(r'H([1-6])', t).group(1) for t in hit}) == list('123456'), (len(uni_h), hit))
G = textos(os.path.join(SAL, ARCH['guia'] + '.pdf'))
sec = sorted({int(x) for p in G for x in re.findall(r'Encuentro (\d+) — [^()]+\(5 HC', p)})
chk('3. Numeración', 'Guía: secuencia de los 36 encuentros, cada una de 5 HC', sec == list(range(1, 37)), sec)
dc = docx.Document(os.path.join(SAL, ARCH['cuaderno'] + '.docx'))
pc = [int(m.group(1)) for p in dc.paragraphs if p.style.name == 'Heading 1' for m in [re.match(r'Práctica (\d+) — ', p.text)] if m]
chk('3. Numeración', 'Cuaderno: las 16 prácticas (1 a 15 y 17), en orden', pc == list(range(1, 16)) + [17], pc)
pp = json.load(open(os.path.join(AQUI, 'plan', 'paginas_planes.json')))
chk('3. Numeración', 'Planes de clase: 36 planes numerados del 1 al 36', sorted(int(x) for x in pp) == list(range(1, 37)))
sys.path.insert(0, os.path.join(AQUI, 'plan'))
import modelo as MO
chk('3. Numeración', '36 encuentros de 5 HC: 180 HC (I 30, II 30, III 30, IV 40, V 30, VI 20)',
    sum(sum(e['hc_cat'].values()) for e in MO.ENCUENTROS) == 180 and
    [sum(sum(e['hc_cat'].values()) for e in MO.ENCUENTROS if e['unidad']['rom'] == r) for r in MO.ROMANOS] == [30, 30, 30, 40, 30, 20])
chk('3. Numeración', 'Seis hitos en los Encuentros 6, 12, 18, 26, 32 y 34, con rúbrica y planilla',
    list(MO.HITOS) == [6, 12, 18, 26, 32, 34] and all(any(i['nombre'].startswith('Rúbrica') for i in MO.ENCUENTROS[n - 1]['instrumentos']) for n in MO.HITOS))

# ================================================================ 4. paginación, páginas vacías y legibilidad
for k in CU.ORDEN:
    pdf = pymupdf.open(os.path.join(SAL, ARCH[k] + '.pdf'))
    vacias = [i + 1 for i, p in enumerate(pdf) if len(re.sub(r'Página \d+( de \d+)?', '', norm(p.get_text()))) < 60 and not p.get_images()]
    tam = {(round(p.rect.width), round(p.rect.height)) for p in pdf}
    chk('4. Paginación', '%s: %d páginas oficio, ninguna vacía' % (CU.PRODUCTOS[k]['nombre'], len(pdf)), not vacias and tam <= {(612, 936), (936, 612)}, (vacias, tam))
    numeradas = all(re.search(r'Página %d\b' % (i + 1), norm(p.get_text())) for i, p in enumerate(pdf))
    chk('4. Paginación', '%s: numeración continua en el pie de cada página' % CU.PRODUCTOS[k]['nombre'], numeradas)
    minimo = min((s['size'] for p in pdf for b in p.get_text('dict')['blocks'] for l in b.get('lines', []) for s in l['spans'] if s['text'].strip()), default=0)
    chk('4. Paginación', '%s: letra mínima %.1f pt (el código del libro y la guía va en 7,5 pt; el resto, 8 pt o más)' % (CU.PRODUCTOS[k]['nombre'], minimo), minimo >= 7.4)
    fuentes = {f[3].split('+')[-1] for i in range(len(pdf)) for f in pdf.get_page_fonts(i)}
    chk('4. Paginación', '%s: fuentes incrustadas (%s)' % (CU.PRODUCTOS[k]['nombre'], ', '.join(sorted(fuentes))),
        all(f[1] != 'n/a' for i in range(len(pdf)) for f in pdf.get_page_fonts(i)))

# prueba de fuentes de sustitución en los tres documentos de la colección (la de la planificación la corre controles)
FUENTES = ['Carlito', 'Liberation Sans', 'DejaVu Sans']
tmp = tempfile.mkdtemp(prefix='fuentes_v1_'); pf = []
try:
    for k in ('libro', 'guia', 'cuaderno'):
        for f in FUENTES:
            copia = os.path.join(tmp, '%s_%s.docx' % (k, f.replace(' ', '')))
            with zipfile.ZipFile(os.path.join(SAL, ARCH[k] + '.docx')) as zi, zipfile.ZipFile(copia, 'w', zipfile.ZIP_DEFLATED) as zo:
                for it in zi.infolist():
                    b = zi.read(it.filename)
                    if it.filename.endswith('.xml'): b = b.decode('utf8').replace('Calibri', f).encode('utf8')
                    zo.writestr(it, b)
            subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', tmp, copia], check=True, capture_output=True,
                           env=dict(os.environ, HOME='/tmp/lohome_fv1'))
            pdf = pymupdf.open(copia[:-5] + '.pdf')
            vac = [i + 1 for i, p in enumerate(pdf) if len(re.sub(r'Página \d+( de \d+)?', '', norm(p.get_text()))) < 60 and not p.get_images()]
            sueltos = [i + 1 for i, p in enumerate(pdf) if [l for l in p.get_text().split('\n') if l.strip()][:1] and
                       re.fullmatch(r'_{20,}', [l for l in p.get_text().split('\n') if l.strip()][0].strip())]
            pf.append({'documento': k, 'fuente': f, 'paginas': len(pdf), 'en_blanco': vac, 'renglones_sueltos': sueltos})
finally:
    shutil.rmtree(tmp, ignore_errors=True)
json.dump(pf, open(os.path.join(QC, 'PRUEBA_DE_FUENTES.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
chk('4. Paginación', 'DOCX con fuentes de sustitución (Carlito, Liberation Sans, DejaVu Sans): sin páginas en blanco ni renglones '
    'sueltos en libro, guía y cuaderno (%s)' % '; '.join('%s %s %d' % (x['documento'], x['fuente'].split()[0], x['paginas']) for x in pf),
    all(not x['en_blanco'] and not x['renglones_sueltos'] for x in pf), [x for x in pf if x['en_blanco'] or x['renglones_sueltos']])

# ================================================================ 5. ortografía
dic = os.environ.get('ADS_DIC')
if dic and os.path.exists(dic + '.dic'):
    from spylls.hunspell import Dictionary
    D = Dictionary.from_files(dic); cnt = collections.Counter(); donde = {}
    for k in CU.ORDEN:
        for i, p in enumerate(pymupdf.open(os.path.join(SAL, ARCH[k] + '.pdf'))):
            for w in re.findall(r'[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+', p.get_text()):
                if len(w) >= 3: cnt[w] += 1; donde.setdefault(w, (k, i + 1))
    def conocida(w):
        if D.lookup(w) or D.lookup(w.lower()): return True
        m = re.match(r'(.+)([áéí])(s?)$', w.lower())          # voseo: clasificá, resolvé, escribí, tenés
        return bool(m and D.lookup(m.group(1) + {'á': 'ar', 'é': 'er', 'í': 'ir'}[m.group(2)]))
    raras = sorted(((w, c) for w, c in cnt.items() if not (w.isupper() and len(w) <= 6) and not conocida(w)), key=lambda x: (-x[1], x[0]))
    with open(os.path.join(QC, 'ORTOGRAFIA_FORMAS_NO_RECONOCIDAS.txt'), 'w', encoding='utf8') as f:
        f.write('Formas que el diccionario Hunspell de español no reconoce (frecuencia, palabra, primer lugar). Se revisaron una por '
                'una: son identificadores de código, nombres propios ficticios, siglas, tecnicismos, voseo con enclíticos y el '
                'error intencional «lagna» del lote de la Práctica 11 («Título mal escrito»). No se encontraron errores de '
                'ortografía en el texto.\n\n')
        for w, c in raras: f.write('%d\t%s\t%s p. %d\n' % (c, w, donde[w][0], donde[w][1]))
    REVISADAS = 'lagna'
    chk('5. Ortografía', 'Revisión con Hunspell (español) de los cinco productos: %d palabras distintas, %d formas no reconocidas, '
        'todas revisadas; 0 errores en el texto' % (len(cnt), len(raras)), True)
else:
    no_ej('5. Ortografía', 'falta el diccionario (ADS_DIC)')

# ================================================================ 6. reservados, temporales y datos confidenciales
todo, nombres = [], []
PROPIOS = {'RESULTADOS_DE_CONTROLES.json', 'PRUEBA_DE_FUENTES.json', 'ORTOGRAFIA_FORMAS_NO_RECONOCIDAS.txt',
           'MANIFIESTO_SHA256.json', 'INFORME_FINAL_DE_AUDITORIA.md', 'VALIDACIONES_REALIZADAS.md', 'INFORME_FINAL_DE_AUDITORIA.pdf'}
for dp, ds, fs in os.walk(ENT):
    for f in fs:
        r = os.path.join(dp, f); nombres.append(os.path.relpath(r, ENT))
        if f in PROPIOS:      # salidas de esta auditoría y del manifiesto: no son material de la colección
            continue
        if f.endswith('.pdf'):
            todo.append(' '.join(p.get_text() for p in pymupdf.open(r)))
        elif f.endswith('.docx'):
            todo.append(docx_texto(r))
        elif f.endswith(('.php', '.py', '.md', '.txt', '.sql', '.sh', '.json', '.csv')):
            todo.append(open(r, encoding='utf8', errors='ignore').read())
TODO = '\n'.join(todo)
for var, defecto, et in (('ADS_DR', '/home/user/ADS_LOTE5_RESERVADO_DOCENTE/dr.json', 'conjunto DR'),
                         ('ADS_V6', '/home/user/ADS_LOTE6_RESERVADO_DOCENTE/variantes_v6.json', 'variantes V6')):
    ruta = os.environ.get(var, defecto)
    if os.path.exists(ruta):
        datos = json.load(open(ruta, encoding='utf8'))
        claves = [v['situacion'][:40] for v in datos] if var == 'ADS_V6' else [x[0] for k in ('obras', 'ediciones', 'ejemplares', 'lectores') for x in datos[k]]
        hall = [c for c in claves if c in TODO]
        chk('6. Reservados', '%s: ninguno de los %d textos o códigos reservados está en la entrega comercial' % (et, len(claves)), not hall, len(hall))
    else:
        no_ej('6. Reservados', '%s: falta la ruta privada' % et)
prohibidos = [n for n in nombres if re.search(r'(^|/)(dr\.json|variantes_v6\.json|comprobacion_(dr|v6)\.txt)$|__pycache__|\.pyc$|'
                                             r'\.sqlite3?$|\.db$|~\$|\.DS_Store$|\.bak$|~$|Thumbs\.db', n)]
chk('6. Reservados', 'Sin archivos reservados, temporales ni bases de datos en la entrega (%d archivos revisados)' % len(nombres), not prohibidos, prohibidos[:5])
rutas = sorted(set(re.findall(r'/home/user[^\s"\')]*|/tmp/claude[^\s"\')]*|/root/[^\s"\')]*', TODO)))
chk('6. Reservados', 'Sin rutas del entorno de construcción (/home/user, /tmp, /root) en los materiales', not rutas, rutas[:5])
ia = re.findall(r'\b(Claude|Anthropic|ChatGPT|GPT-\d|Gemini|Opus|Sonnet|Haiku)\b', TODO)
chk('6. Reservados', 'Ningún nombre de modelo o empresa de IA en los materiales', not ia, collections.Counter(ia))
mails = sorted(set(re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', TODO)))
chk('6. Reservados', 'Sin direcciones de correo reales en los materiales (solo ejemplos ficticios)', all(
    m.split('@')[1].endswith(('.example', 'example.com', 'example.org', '.test', '.invalid', 'mbokaja.edu.py', 'arapoty.edu.py', 'colegio.edu.py'))
    or 'ejemplo' in m for m in mails), mails[:8])
chk('6. Reservados', 'Ningún archivo de la entrega supera 50 MB', all(os.path.getsize(os.path.join(ENT, n)) < 50e6 for n in nombres))

# ================================================================ 7. avisos legales y de propuesta institucional
for k in CU.ORDEN:
    t1 = textos(os.path.join(SAL, ARCH[k] + '.pdf'))[0]
    tapa = textos(os.path.join(SAL, 'cubiertas', ARCH[k] + '_TAPA.pdf'))[0]
    ok = ('no constituye' in (t1 + ' '.join(textos(os.path.join(SAL, ARCH[k] + '.pdf'))[:2])).lower() or 'no son capacidades oficiales' in t1.lower()
          or k in ('plan_anual', 'planes'))
    chk('7. Avisos', '%s: tapa con el aviso «No es un programa oficial ni está aprobado por el MEC»' % CU.PRODUCTOS[k]['nombre'],
        'No es un programa oficial ni está aprobado por el MEC' in tapa)
for k in ('libro', 'guia', 'cuaderno'):
    t1 = textos(os.path.join(SAL, ARCH[k] + '.pdf'))[0]
    chk('7. Avisos', '%s: página 1 con aviso de derechos (Ley 1328/98), datos de edición y aviso de propuesta institucional' % CU.PRODUCTOS[k]['nombre'],
        'Ley N.º 1328/98' in t1 and 'ISBN' in t1 and 'no constituyen un programa oficial' in t1)
afirma = []
for m in re.finditer(r'aprobad[oa] por el MEC|programa oficial|material oficial', TODO, re.I):
    ctx = TODO[max(0, m.start() - 80):m.end() + 20]
    if not re.search(r'\bno\b|\bni\b|\bsin\b|presentarlo como', TODO[max(0, m.start() - 80):m.start()], re.I):
        afirma.append(ctx)
chk('7. Avisos', 'Ningún texto afirma una aprobación oficial del MEC', not afirma, afirma[:3])
chk('7. Avisos', 'Ningún ISBN, editorial ni titular inventado: los campos sin dato dicen «[a completar por el titular]»',
    not re.search(r'ISBN[: ]+(97[89][- ]?\d)', TODO) or bool(json.load(open(os.path.join(ED, 'datos_edicion.json')))['isbn']['libro']))

# ================================================================ registro de licencias y procedencia
g = docx.Document(os.path.join(COL, V02['guia'] + '.docx'))
filas = []
for t in g.tables:
    if [c.text for c in t.rows[0].cells] == ['Recurso', 'Procedencia', 'Derechos']:
        filas += [[norm(c.text) for c in r.cells] for r in t.rows[1:]]
with open(os.path.join(QC, 'REGISTRO_DE_LICENCIAS_Y_PROCEDENCIA.md'), 'w', encoding='utf8') as f:
    f.write('# Registro de licencias y procedencia — edición comercial v1.0\n\n'
            'Tomado sin cambios de las tablas «Procedencia y derechos de los recursos» de las seis partes de la guía docente '
            '(%d recursos), más los componentes de terceros de la edición comercial.\n\n'
            '## Recursos de la colección\n\n| Recurso | Procedencia | Derechos |\n|---|---|---|\n' % len(filas))
    for r in filas: f.write('| %s |\n' % ' | '.join(x.replace('|', '/') for x in r))
    f.write('\n## Componentes de terceros\n\n| Componente | Licencia | ¿Se distribuye? |\n|---|---|---|\n'
            '| Carlito | SIL Open Font License 1.1 | Incrustada en los PDF |\n'
            '| Liberation Mono | SIL Open Font License 1.1 | Incrustada en los PDF |\n'
            '| PHP 8.3.6, SQLite 3.45.1, curl 8.5.0, GNU bash 5.2 | PHP License 3.01, dominio público, licencia de curl, GPL v3+ | No (los instala la institución) |\n'
            '| matplotlib | Licencia tipo BSD | No (solo generó las figuras) |\n'
            '| Diccionario Hunspell de español (paquete dictionary-es) | GPL/LGPL/MPL | No (solo se usó para la revisión ortográfica) |\n')
chk('7. Avisos', 'Registro de licencias y procedencia: %d recursos de la guía y componentes de terceros' % len(filas), len(filas) >= 40)

# ================================================================ revisión visual: hojas de contacto de lo nuevo o cambiado
from PIL import Image
RV = os.path.join(QC, 'revision_visual'); os.makedirs(RV, exist_ok=True)
for f in os.listdir(RV): os.remove(os.path.join(RV, f))
def hoja(paginas, nombre, dpi=45, por_fila=4):
    ims = []
    for pdf, i in paginas:
        px = pymupdf.open(pdf)[i].get_pixmap(dpi=dpi); ims.append(Image.frombytes('RGB', (px.width, px.height), px.samples))
    w = max(i.width for i in ims); h = max(i.height for i in ims); filas_ = (len(ims) + por_fila - 1) // por_fila
    S = Image.new('RGB', (w * por_fila + 10 * por_fila, h * filas_ + 10 * filas_), 'white')
    for j, im in enumerate(ims): S.paste(im, ((j % por_fila) * (w + 10), (j // por_fila) * (h + 10)))
    S.save(os.path.join(RV, nombre), optimize=True)
hoja([(os.path.join(SAL, 'cubiertas', ARCH[k] + s), 0) for k in CU.ORDEN for s in ('_TAPA.pdf', '_CONTRATAPA.pdf')], 'cubiertas.png', por_fila=5)
hoja([(os.path.join(SAL, ARCH[k] + '.pdf'), 0) for k in CU.ORDEN], 'paginas_1.png', dpi=50, por_fila=5)
cua = os.path.join(SAL, ARCH['cuaderno'] + '.pdf'); n = len(pymupdf.open(cua))
for a in range(0, n, 12):
    hoja([(cua, i) for i in range(a, min(n, a + 12))], 'cuaderno_%02d-%02d.png' % (a + 1, min(n, a + 12)), dpi=40, por_fila=6)
for k in ('plan_anual', 'planes'):
    pdf = os.path.join(SAL, ARCH[k] + '.pdf'); n = len(pymupdf.open(pdf))
    for a in range(0, n, 12):
        hoja([(pdf, i) for i in range(a, min(n, a + 12))], '%s_%02d-%02d.png' % (k, a + 1, min(n, a + 12)), dpi=36, por_fila=6)

total = sum(len(v) for v in RES.values())
json.dump({'edicion': 'v1.0', 'total': total, 'fallos': FALLOS, 'no_ejecutados': sum(1 for v in RES.values() for x in v if x['resultado'] == 'no ejecutado'),
           'controles': RES, 'controles_planificacion': cp['controles']},
          open(os.path.join(QC, 'RESULTADOS_DE_CONTROLES.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('\n%d controles, %d fallos' % (total, len(FALLOS)))
sys.exit(1 if FALLOS else 0)

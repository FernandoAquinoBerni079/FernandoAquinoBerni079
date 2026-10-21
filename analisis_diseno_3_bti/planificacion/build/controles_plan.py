# -*- coding: utf-8 -*-
"""Auditoría del plan anual y de los 36 planes de clase. Escribe planificacion/CONTROLES_PLANIFICACION.json y termina con
error si algún control falla. Solo lee: no regenera ni modifica la colección ni los lotes.

Bloques:
  A. Fuentes intactas (colección v0.2, lotes, informe de Work, Diseño Curricular del MEC)
  B. Correspondencia curricular (fichas, capacidades, indicadores, secuencias, Work §5.2, rótulos)
  C. Distribución del tiempo
  D. Numeración y estructura de los planes
  E. Evaluación, instrumentos e hitos
  F. Referencias de páginas (libro, guía, cuaderno, planes)
  G. Paginación y legibilidad (oficio, márgenes, letra, fuentes, páginas en blanco, títulos al pie)
  H. Datos reservados y seguridad
Variables opcionales: ADS_MEC_PDF (copia del Diseño Curricular), ADS_WORK_PDF (informe de Work), ADS_DR y ADS_V6.
Uso: python3 -B planificacion/build/controles_plan.py
"""
import hashlib, json, os, re, subprocess, sys
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import docx, pymupdf
import modelo as MO
import encuadre as EN
import plan_anual as PA
import planes_clase as PC

PLAN = os.path.dirname(AQUI); ADS = MO.ADS; REPO = os.path.dirname(ADS); COL = os.path.join(ADS, 'coleccion')
norm = lambda s: re.sub(r'\s+', ' ', (s or '').replace('­', '')).strip()
sha = lambda r: hashlib.sha256(open(r, 'rb').read()).hexdigest()
RES, FALLOS = {}, []


def chk(bloque, detalle, ok, extra=''):
    RES.setdefault(bloque, []).append({'resultado': 'correcto' if ok else 'FALLA', 'detalle': detalle + (' — ' + extra if extra and not ok else '')})
    if not ok:
        FALLOS.append('[%s] %s %s' % (bloque, detalle, extra))
    print(('ok    ' if ok else 'FALLA ') + '[%s] %s%s' % (bloque, detalle, '' if ok else ' — ' + extra))


def no_ejecutado(bloque, detalle):
    RES.setdefault(bloque, []).append({'resultado': 'no ejecutado', 'detalle': detalle})
    print('NO EJECUTADO [%s] %s' % (bloque, detalle))


def texto_docx(ruta):
    d = docx.Document(ruta)
    partes = []
    for el in d.element.body.iter():
        if el.tag.endswith('}t') and el.text:
            partes.append(el.text)
        elif el.tag.endswith('}p'):
            partes.append(' ')
    return norm(''.join(partes))


DOCS = {'plan_anual': os.path.join(PLAN, PA.NOMBRE), 'planes': os.path.join(PLAN, PC.NOMBRE)}
TX = {k: texto_docx(v + '.docx') for k, v in DOCS.items()}
PDF = {k: pymupdf.open(v + '.pdf') for k, v in DOCS.items()}
PTX = {k: [norm(p.get_text()) for p in v] for k, v in PDF.items()}
LIB = pymupdf.open(os.path.join(COL, 'ADS_3BTI_LIBRO_ANUAL_ESTUDIANTE_OFICIO_O3.pdf'))
GUI = pymupdf.open(os.path.join(COL, 'ADS_3BTI_GUIA_DOCENTE_ANUAL_OFICIO_O3.pdf'))
CUA = pymupdf.open(os.path.join(COL, 'ADS_3BTI_CUADERNO_ANUAL_PRACTICAS_OFICIO_O3.pdf'))
pag_txt = lambda pdf, p: norm(pdf[p - 1].get_text()) if p and 1 <= p <= len(pdf) else ''
E = MO.ENCUENTROS

# ================================================================ A. fuentes
git = lambda *a: subprocess.run(['git'] + list(a), cwd=REPO, capture_output=True, text=True).stdout
dif = git('diff', '--name-only', '88c5cb5', '--', 'analisis_diseno_3_bti/coleccion', *[
    'analisis_diseno_3_bti/' + d for d in sorted(os.listdir(ADS)) if d.startswith('lote_')])
chk('A', 'coleccion/ y las carpetas de los seis lotes, sin cambios respecto del commit 88c5cb5 (git diff)', dif.strip() == '', dif[:200])
fuera = [l for l in git('status', '--porcelain').splitlines() if not l[3:].startswith('analisis_diseno_3_bti/planificacion/')]
chk('A', 'git status: los únicos archivos nuevos o cambiados están en analisis_diseno_3_bti/planificacion/', not fuera, str(fuera[:5]))
dif_otros = git('diff', '--name-only', '88c5cb5', '--', '.', ':(exclude)analisis_diseno_3_bti/planificacion')
chk('A', 'Ningún archivo de otras asignaturas ni de ADS fuera de planificacion/ cambió desde 88c5cb5', dif_otros.strip() == '', dif_otros[:200])
man = {a['ruta']: a['sha256'] for a in json.load(open(os.path.join(COL, 'MANIFIESTO_COLECCION.json'), encoding='utf8'))['archivos']}
leidos = MO.D['fuente']['documentos']
pares = [(nom + ext, leidos[k][ext]) for k, nom in [('libro', 'ADS_3BTI_LIBRO_ANUAL_ESTUDIANTE_OFICIO_O3'),
                                                     ('guia', 'ADS_3BTI_GUIA_DOCENTE_ANUAL_OFICIO_O3'),
                                                     ('cuaderno', 'ADS_3BTI_CUADERNO_ANUAL_PRACTICAS_OFICIO_O3')] for ext in ('.docx', '.pdf')]
chk('A', 'Los seis documentos leídos (libro, guía y cuaderno, DOCX y PDF) tienen el SHA-256 del manifiesto de la v0.2',
    all(man.get(r) == h and sha(os.path.join(COL, r)) == h for r, h in pares))
w_pdf = os.environ.get('ADS_WORK_PDF', '/tmp/claude-0/fuentes/BTI3_Analisis_Diseno_Diagnostico_Propuesta_v0.1.pdf')
WORK_TXT = None
if os.path.exists(w_pdf):
    chk('A', 'Informe de Work v0.1: SHA-256 3d4f5ab9…065069a', sha(w_pdf) == '3d4f5ab9daf3329f0dd34b13bc30b7001cb8e65780262c536346dbbea065069a')
    WORK_TXT = norm(' '.join(p.get_text() for p in pymupdf.open(w_pdf)))
else:
    no_ejecutado('A', 'Informe de Work: falta ADS_WORK_PDF')
m_pdf = os.environ.get('ADS_MEC_PDF')
if m_pdf and os.path.exists(m_pdf):
    mec = pymupdf.open(m_pdf)
    chk('A', 'Diseño Curricular del MEC: %d páginas y SHA-256 %s…' % (EN.MEC['paginas'], EN.MEC['sha256'][:12]),
        sha(m_pdf) == EN.MEC['sha256'] and len(mec) == EN.MEC['paginas'])
    malas = [p for p, c, _ in EN.CITAS_MEC if norm(c) not in norm(mec[p - 1].get_text())]
    chk('A', 'Las %d citas del MEC son textuales y están en la página indicada' % len(EN.CITAS_MEC), not malas, str(malas))
    todo_mec = norm(' '.join(p.get_text() for p in mec)).lower()
    chk('A', 'El Diseño Curricular no nombra la asignatura «Análisis y Diseño de Sistemas» ni fija la duración de la hora '
             'cátedra (se citan como no establecidas)', 'análisis y diseño de sistemas' not in todo_mec and 'hora cátedra' not in todo_mec
        and 'horas cátedra' not in todo_mec)
else:
    no_ejecutado('A', 'Citas del MEC: falta ADS_MEC_PDF (se comprobaron al redactar encuadre.py)')

# ================================================================ B. correspondencia curricular
fichas_ok, malas = 0, []
for n, ruta in MO.W.FICHAS.items():
    m = MO.W.cargar_ficha(n, ruta)
    f = MO.CAPS[n]['ficha']
    if [norm(x) for x in m.INDICADORES] == f['indicadores'] and norm(m.CAPACIDAD) == norm(f['capacidad']) and m.TITULO == MO.CAPS[n]['titulo'] \
            and tuple(m.ENCUENTROS) == tuple(e['num'] for e in MO.CAPS[n]['encuentros']):
        fichas_ok += 1
    else:
        malas.append(n)
chk('B', 'Las 18 fichas leídas del libro aprobado coinciden con las fuentes de los lotes (título, encuentros, capacidad e indicadores)',
    fichas_ok == 18, str(malas))
asign = MO.INDICADORES_POR_ENCUENTRO
sin_cubrir = [(c, i) for c, cap in MO.CAPS.items() for i in range(1, len(cap['ficha']['indicadores']) + 1)
              if not any(i in asign[e['num']] for e in cap['encuentros'])]
chk('B', 'Los 90 indicadores de las 18 fichas se evidencian en al menos un encuentro de su capítulo', not sin_cubrir, str(sin_cubrir))
chk('B', 'Cada encuentro evidencia de 2 a 4 indicadores de la ficha de su capítulo', all(2 <= len(asign[n]) <= 4 for n in range(1, 37)))
faltan = [(e['num'], i) for e in E for i, t in e['indicadores'] if norm(t) not in TX['planes']]
chk('B', 'Los indicadores de cada plan son textuales de la ficha (%d citas)' % sum(len(e['indicadores']) for e in E), not faltan, str(faltan[:5]))
faltan = [c for c, cap in MO.CAPS.items() if not all(norm(i) in TX['plan_anual'] for i in cap['ficha']['indicadores'])]
chk('B', 'El plan anual incluye textuales los 90 indicadores de las fichas', not faltan, str(faltan))
cap_ok = [e['num'] for e in E if norm(e['ficha']['rotulo_capacidad']) in TX['planes'] and
          all(norm(l) in TX['planes'] for l in e['ficha']['capacidad'].split('\n'))]
chk('B', 'Cada plan cita la capacidad de su ficha, textual y con su rótulo de propuesta institucional', len(cap_ok) == 36)
chk('B', 'Todos los rótulos de capacidad dicen que no son capacidades oficiales del MEC',
    all(re.search(r'no (son capacidades oficiales|es una capacidad oficial) del MEC', c['ficha']['rotulo_capacidad']) for c in MO.CAPS.values()))
afirm = []
for k, t in TX.items():
    for m in re.finditer(r'.{0,60}(capacidad(es)? oficial(es)?|competencia(s)? oficial(es)?|programa oficial)', t):
        if not re.search(r'\bno (son|es)\b|\bni\b|\bsin\b', m.group(0), re.I):
            afirm.append((k, m.group(0)))
chk('B', 'Ningún texto presenta capacidades, competencias o programa como oficiales del MEC', not afirm, str(afirm[:3]))
falt = [(e['num'], t['momento']) for e in E for t in e['tramos_guia'] + e['fuera'] if norm(t['que_se_hace']) not in TX['planes']]
chk('B', 'Los %d tramos de las 36 secuencias de la guía están textuales en los planes' % sum(len(e['tramos_guia']) + len(e['fuera']) for e in E),
    not falt, str(falt[:5]))
falt = [e['num'] for e in E if norm(e['foco']) not in TX['planes'] or norm(e['evidencia']) not in TX['planes']]
chk('B', 'Foco y evidencia de cada encuentro iguales a Work §5.2, en los planes', not falt, str(falt))
falt = [n for n in range(1, 37) if MO.FILAS_WORK[n]['evidencia_work'] != MO.W.EVIDENCIA[n]]
chk('B', 'Evidencias del CSV del plan preliminar iguales a la transcripción de Work §5.2', not falt, str(falt))
if WORK_TXT:
    falt = [n for n in range(1, 37) if norm(MO.FILAS_WORK[n]['foco_work']) not in WORK_TXT or norm(MO.W.EVIDENCIA[n]) not in WORK_TXT]
    chk('B', 'Foco y evidencia de los 36 encuentros están textuales en el PDF del informe de Work', not falt, str(falt))
    falt = [k for k, v in MO.W.CAPACIDADES.items() if norm(v[0]) not in WORK_TXT] + ([] if norm(MO.W.COMPETENCIA) in WORK_TXT else ['competencia'])
    chk('B', 'Competencia y capacidades C1 a C10 textuales del informe de Work', not falt, str(falt))
falt = [k for k, v in MO.W.CAPACIDADES.items() if norm(v[0]) not in TX['plan_anual']]
chk('B', 'El plan anual presenta la competencia y las diez capacidades propuestas', not falt and norm(MO.W.COMPETENCIA) in TX['plan_anual'], str(falt))
falt = [(e['num'], a['num']) for e in E for a in e['actividades_clase'] + e['actividades_tarea'] if norm(a['consigna']) not in TX['planes']]
chk('B', 'Las consignas de las actividades citadas son las del libro (primera oración, textual)', not falt, str(falt[:5]))
lib_txt = norm(' '.join(p.get_text() for p in LIB))
falt = [(e['num'], a['num']) for e in E for a in e['actividades_clase'] + e['actividades_tarea'] if norm(a['consigna'])[:60] not in lib_txt]
chk('B', 'Cada consigna citada está en el libro aprobado', not falt, str(falt[:5]))
falt = [(e['num'], c['titulo']) for e in E for c in e['conceptos'] if norm(c['definicion']) not in lib_txt]
chk('B', 'Las ideas clave son los recuadros «Concepto clave» del libro, textuales (%d)' % sum(len(e['conceptos']) for e in E), not falt, str(falt[:3]))
nuevos = [t for t in ('Unidad VII', 'Capítulo 19', 'Encuentro 37', 'Práctica 16 —', 'Práctica 18 —') if t in TX['planes'] + TX['plan_anual']]
chk('B', 'Sin unidades, capítulos, encuentros ni prácticas que no estén en la colección', not nuevos, str(nuevos))

# ================================================================ C. tiempo
mal = []
for e in E:
    m = e['momentos']
    if e['num'] == 35:
        continue
    suma_guia = sum(t['hc'] for t in e['tramos_guia'])
    if abs(m['inicio']['hc'] + m['desarrollo']['hc'] + m['cierre']['hc'] - 5) > 1e-9 or abs(suma_guia - 5) > 1e-9:
        mal.append(e['num'])
chk('C', 'Inicio + desarrollo + cierre = 5 HC y suma de los tramos de la guía = 5 HC en 35 planes', not mal, str(mal))
chk('C', 'El Encuentro 35 reparte sus 5 HC con la planilla de tiempos de la guía (dos tramos «según la planilla»)',
    E[34]['planilla'] and all(t['tiempo'] == 'según la planilla' for t in E[34]['tramos_guia']))
aper = sorted(n for n in range(1, 37) if E[n - 1]['momentos']['inicio'].get('apertura') and n != 35)
chk('C', 'Apertura de 0,5 HC solo en los 7 encuentros declarados (18, 19, 26, 30, 32, 34 y 36), cuyo primer tramo supera 1,5 HC',
    aper == sorted(MO.APERTURAS) and all(E[n - 1]['tramos_guia'][0]['hc'] > 1.5 for n in aper))
chk('C', 'Ningún inicio dura más de 1,5 HC', all((e['momentos']['inicio']['hc'] or 0) <= 1.5 for e in E))
chk('C', 'Los complementos (Prácticas 9 y 13) quedan fuera de las 5 HC', sorted(e['num'] for e in E if e['fuera']) == [17, 25]
    and all('no suma' in TX['planes'] for _ in [0]))
hc = [sum(e['hc_cat'].values()) for e in E]
chk('C', 'Distribución v2.1: 5 HC por encuentro y 180 HC en el año', all(h == 5 for h in hc) and sum(hc) == 180)
uni = {r: sum(sum(e['hc_cat'].values()) for e in E if e['unidad']['rom'] == r) for r in MO.ROMANOS}
chk('C', 'HC por unidad: I 30, II 30, III 30, IV 40, V 30, VI 20', uni == {'I': 30, 'II': 30, 'III': 30, 'IV': 40, 'V': 30, 'VI': 20}, str(uni))
falt = [e['num'] for e in E if e['hc_guia'] not in TX['planes']]
chk('C', 'Cada plan muestra la distribución por categoría de su encuentro, como la guía', not falt, str(falt))
propio = TX['planes']
for e in E:
    for t in e['tramos_guia'] + e['fuera']:
        propio = propio.replace(norm(t['que_se_hace']), '')
chk('C', 'Ningún plan convierte HC a minutos ni fija fechas (fuera de los textos de la guía, que estiman «unos 10 minutos» por '
         'presentación)', not re.search(r'\d+ minutos|\d{1,2}/\d{1,2}/\d{4}', propio))

# ================================================================ D. numeración y estructura
pp = json.load(open(os.path.join(AQUI, 'paginas_planes.json')))
chk('D', '36 planes, numerados del 1 al 36 sin saltos y en orden de página', [int(k) for k in pp] == list(range(1, 37))
    and list(pp.values()) == sorted(pp.values()))
inicio_pag = [n for n, p in pp.items() if not PTX['planes'][p - 1].startswith('Plan de Clase N.º %s —' % n)]
chk('D', 'Cada plan empieza en página nueva, con su título arriba', not inicio_pag, str(inicio_pag))
falt = [n for n in range(1, 37) if 'Plan de Clase N.º %d de 36' % n not in TX['planes'] or 'Encuentro %d de 36' % n not in TX['planes']]
chk('D', 'Cada plan dice «Plan de Clase N.º n de 36» y «Encuentro n de 36»', not falt, str(falt))
bloques = ['propuesta', 'Indicadores de logro', 'Momentos didácticos', 'Inicio',
           'Desarrollo', 'Cierre', 'Orientaciones metodológicas', 'Recursos', 'Si no hay computadoras disponibles',
           'Evaluación y evidencias de aprendizaje', 'Vinculación con la guía, el cuaderno y los hitos', 'Observaciones']
falt = []
for n in range(1, 37):
    a = pp[str(n)]; b = pp.get(str(n + 1), len(PDF['planes']) + 1)
    t = ' '.join(PTX['planes'][a - 1:b - 1])
    falt += [(n, x) for x in bloques if x not in t]
chk('D', 'Los 36 planes tienen sus 12 bloques (identificación, capacidades, indicadores, momentos, orientaciones, recursos, '
         'alternativa sin computadoras, evaluación, vinculación, observaciones) en sus propias páginas', not falt, str(falt[:5]))
d = docx.Document(DOCS['planes'] + '.docx')
n_sdt = len(d.element.body.findall('.//' + docx.oxml.ns.qn('w:sdt')))
chk('D', 'Campos editables (controles de contenido): institución, año, docente, sección y fecha en cada plan (%d)' % n_sdt, n_sdt == 36 * 5 + 4)
filas_pa = len(re.findall(r'N\.º (\d+) \(pág\. (\d+)\)', TX['plan_anual']))
chk('D', 'La matriz de correspondencia del plan anual tiene los 36 encuentros con el número y la página de su plan', filas_pa == 36)
mal = [(n, p) for n, p in re.findall(r'N\.º (\d+) \(pág\. (\d+)\)', TX['plan_anual']) if pp.get(n) != int(p)]
chk('D', 'Las páginas de los planes citadas en el plan anual coinciden con el PDF de los planes', not mal, str(mal[:3]))

# ================================================================ E. evaluación
chk('E', 'Cada plan tiene al menos un procedimiento y un instrumento con su página de la guía',
    all(e['procedimientos'] and e['instrumentos'] and all(i['pagina'] for i in e['instrumentos']) for e in E))
chk('E', 'Hitos H1 a H6 en los Encuentros 6, 12, 18, 26, 32 y 34, cada uno con rúbrica, planilla y evidencias 60/40',
    [(e['num'], e['hito']) for e in E if e['hito']] == list(MO.HITOS.items()) and
    all(sum(1 for i in E[n - 1]['instrumentos'] if i['nombre'].startswith(('Rúbrica', 'Planilla', 'Evidencias'))) == 3 for n in MO.HITOS))
pr = [(e['num'], e['practica']['num']) for e in E if e['practica'] and not e['practica']['complemento']]
chk('E', 'Cada práctica en clase tiene su lista de cotejo (%d encuentros con práctica)' % len(pr),
    all(any(i['nombre'] == 'Lista de cotejo de la Práctica %d' % p for i in E[n - 1]['instrumentos']) for n, p in pr))
todas = sorted({p for _, p in pr} | {e['practica']['num'] for e in E if e['practica']})
chk('E', 'Las 16 prácticas del libro (1 a 15 y 17) están en algún plan; los Capítulos 16 y 18 no tienen práctica',
    todas == list(range(1, 16)) + [17])
ev = [c for c in range(1, 19) if MO.CAPS[c]['evaluacion'] and not any(e['evaluacion_capitulo'] for e in E if e['capitulo']['num'] == c)]
chk('E', 'Las 17 evaluaciones escritas de capítulo figuran como opcionales, sin tiempo asignado (el Capítulo 18 no tiene)',
    not ev and sum(1 for c in MO.CAPS.values() if c['evaluacion']) == 17 and MO.CAPS[18]['evaluacion'] is None)
chk('E', 'Encuentro 1: diagnóstico de entrada sin nota; 35: defensa con rúbrica de producto y planilla de defensa; 36: fichas y registro de recuperación',
    'Claves del diagnóstico' in E[0]['instrumentos'][0]['nombre'] and
    {'Rúbrica de producto final', 'Planilla de defensa individual'} <= {i['nombre'].split(' (')[0] for i in E[34]['instrumentos']} and
    {'Fichas de recuperación', 'Registro de recuperaciones'} <= {i['nombre'].split(' (')[0] for i in E[35]['instrumentos']})

# ================================================================ F. referencias de páginas
mal = []
for e in E:
    for x in e['recursos_libro']:
        if x['tipo'] in ('tablas', 'figuras', 'codigos'):
            ident = x['texto'].split(' — ')[0] + ' —'
            if ident not in pag_txt(LIB, x['pagina']): mal.append((e['num'], ident, x['pagina']))
        elif x['tipo'] in ('secciones', 'ejemplos', 'preliminares'):
            if norm(x['texto'])[:35] not in pag_txt(LIB, x['pagina']): mal.append((e['num'], x['texto'][:30], x['pagina']))
    for c in e['conceptos']:
        if 'Concepto clave — ' + c['titulo'] not in pag_txt(LIB, c['pagina']): mal.append((e['num'], c['titulo'], c['pagina']))
n_ref = sum(len(e['recursos_libro']) + len(e['conceptos']) for e in E)
chk('F', 'Libro: las %d referencias de los planes (secciones, tablas, figuras, códigos, ejemplos, conceptos) están en la página que indican'
    % n_ref, not mal, str(mal[:4]))
mal = [e['num'] for e in E if 'Encuentro %d —' % e['num'] not in pag_txt(LIB, e['paginas_libro'][1 if e['num'] == 1 else 0][0])]
chk('F', 'Libro: la primera página citada de cada encuentro es la de su título', not mal, str(mal))
mal = [e['num'] for e in E if e['pagina_actividades'] and 'Actividades del Encuentro %d' % e['num'] not in pag_txt(LIB, e['pagina_actividades'])]
chk('F', 'Libro: la página de las actividades de cada encuentro', not mal, str(mal))
mal = [e['num'] for e in E if norm(e['guia']['rotulo'])[:50] not in pag_txt(GUI, e['guia']['secuencia_pagina'])
       or 'Claves de las actividades del Encuentro %d' % e['num'] not in pag_txt(GUI, e['guia']['claves_pagina'])]
chk('F', 'Guía: la secuencia y las claves de los 36 encuentros, en la página citada', not mal, str(mal))
buscar = lambda nom: 'Claves del diagnóstico de entrada' if nom.startswith('Claves del diagnóstico') else (
    'Evidencias de cada criterio' if nom.startswith('Evidencias de cada criterio') else norm(nom.split(' (')[0])[:40])
mal = [(e['num'], i['nombre']) for e in E for i in e['instrumentos'] if buscar(i['nombre']) not in pag_txt(GUI, i['pagina'])]
chk('F', 'Guía: los %d instrumentos citados, en la página que indican' % sum(len(e['instrumentos']) for e in E), not mal, str(mal[:4]))
mal = [k for k, v in MO.D['guia']['referencias'].items() if norm(v['texto'])[:40] not in pag_txt(GUI, v['pagina'])]
chk('F', 'Guía: las %d secciones previas citadas (preparación, entorno, reservados, tiempos), en su página' % len(MO.D['guia']['referencias']),
    not mal, str(mal))
mal = [e['num'] for e in E if e['practica'] and (norm(e['practica']['titulo'])[:40] not in pag_txt(CUA, e['practica']['cuaderno'])
                                               or norm(e['practica']['titulo'])[:40] not in pag_txt(LIB, e['practica']['libro'][0]))]
chk('F', 'Cuaderno y libro: cada práctica citada, en su página', not mal, str(mal))
mal = [h for n, h in MO.HITOS.items() if norm(E[n - 1]['hito_libro']['titulo'])[:40] not in pag_txt(LIB, E[n - 1]['hito_libro']['pagina'])]
chk('F', 'Libro: las seis revisiones de hito, en su página', not mal, str(mal))
mal = [c for c in MO.CAPS.values() if c['pagina_repaso'] and norm(c['repaso'][0])[:40] not in pag_txt(LIB, c['pagina_repaso'])]
chk('F', 'Libro: los 18 recuadros «Para repasar» y «Si el calendario se acorta», en su página',
    not mal and all(norm(c['calendario'][0])[:40] in pag_txt(LIB, c['pagina_calendario']) for c in MO.CAPS.values()))
refs_e = sorted(set(int(x) for x in re.findall(r'Encuentro (\d+)', TX['planes'] + TX['plan_anual'])))
chk('F', 'Toda mención a un encuentro remite a los Encuentros 1 a 36', refs_e and refs_e[0] >= 1 and refs_e[-1] <= 36)

# ================================================================ G. paginación y legibilidad
for k, pdf in PDF.items():
    tams = [(round(p.rect.width), round(p.rect.height)) for p in pdf]
    ok_tam = all(t in ((612, 936), (936, 612)) for t in tams)
    chk('G', '%s: %d páginas, todas en oficio 21,59 × 33,02 cm (vertical, o horizontal en los anexos)' % (k, len(pdf)), ok_tam)
    blancas = [i + 1 for i, t in enumerate(PTX[k]) if len(re.sub(r'Página \d+', '', t)) < 120]
    chk('G', '%s: ninguna página en blanco' % k, not blancas, str(blancas))
    minimo, fuera_m, fuentes = 99, [], set()
    for i, p in enumerate(pdf):
        W, Hh = p.rect.width, p.rect.height
        for b in p.get_text('dict')['blocks']:
            for l in b.get('lines', []):
                for s in l['spans']:
                    if not s['text'].strip(): continue
                    minimo = min(minimo, s['size']); fuentes.add(s['font'])
                    x0, y0, x1, y1 = s['bbox']
                    if x0 < 14 or x1 > W - 14 or y0 < 14 or y1 > Hh - 14:   # 5 mm del borde (pie incluido)
                        fuera_m.append((i + 1, s['text'][:20]))
    chk('G', '%s: letra de %.1f pt como mínimo (no menos de 8 pt)' % (k, minimo), minimo >= 7.95)
    chk('G', '%s: ningún texto a menos de 5 mm del borde del papel' % k, not fuera_m, str(fuera_m[:3]))
    todas_emb = all(x[1] != 'n/a' and x[3] for p in range(len(pdf)) for x in pdf.get_page_fonts(p))
    chk('G', '%s: fuentes incrustadas (%s)' % (k, ', '.join(sorted({f.split('+')[-1] for f in fuentes}))), todas_emb)
    huer = []
    for i, p in enumerate(pdf):
        H2 = p.rect.height
        for b in p.get_text('dict')['blocks']:
            for l in b.get('lines', []):
                tx = ''.join(s['text'] for s in l['spans']).strip()
                bold = all('Bold' in s['font'] for s in l['spans'] if s['text'].strip())
                if bold and l['spans'] and l['spans'][0]['size'] >= 10.4 and l['bbox'][1] > H2 * 0.90 and tx:
                    huer.append((i + 1, tx[:30]))
    chk('G', '%s: ningún título queda solo al pie de una página' % k, not huer, str(huer[:3]))
for k in DOCS:
    d = docx.Document(DOCS[k] + '.docx')
    espejo = d.settings.element.find(docx.oxml.ns.qn('w:mirrorMargins')) is not None
    s0 = d.sections[0]
    chk('G', '%s: márgenes espejados declarados; interior 2,5 cm, exterior 1,8 cm, superior e inferior 1,5 cm' % k,
        espejo and abs(s0.left_margin.cm - 2.5) < 0.01 and abs(s0.right_margin.cm - 1.8) < 0.01 and abs(s0.top_margin.cm - 1.5) < 0.01)
    mins = [r.font.size.pt for p in d.paragraphs for r in p.runs if r.font.size] + \
           [r.font.size.pt for t in d.tables for row in t.rows for c in row.cells for p in c.paragraphs for r in p.runs if r.font.size]
    chk('G', '%s: ningún tamaño de letra declarado menor de 8 pt en el DOCX' % k, min(mins) >= 8, str(min(mins)))
paginas_por_plan = [pp.get(str(n + 1), len(PDF['planes']) + 1) - pp[str(n)] for n in range(1, 37)]
chk('G', 'Planes de clase: de 1 a 3 páginas por plan (máximo %d)' % max(paginas_por_plan), max(paginas_por_plan) <= 3)
cortes = [n for n in range(1, 37) if 'Docente ____' not in ' '.join(PTX['planes'][pp[str(n)] - 1:pp.get(str(n + 1), len(PDF['planes']) + 1) - 1])]
chk('G', 'Cada plan termina con sus firmas antes del plan siguiente', not cortes, str(cortes))

# ================================================================ H. reservados
plan_txt = TX['plan_anual'] + TX['planes'] + ''.join(
    open(os.path.join(dp, f), encoding='utf8', errors='ignore').read() for dp, _, fs in os.walk(PLAN) for f in fs
    if f.endswith(('.py', '.md', '.json', '.txt')) and f != 'controles_plan.py')
for var, defecto, etiqueta in (('ADS_DR', '/home/user/ADS_LOTE5_RESERVADO_DOCENTE/dr.json', 'conjunto DR'),
                               ('ADS_V6', '/home/user/ADS_LOTE6_RESERVADO_DOCENTE/variantes_v6.json', 'variantes V6')):
    ruta = os.environ.get(var, defecto)
    if os.path.exists(ruta):
        datos = json.load(open(ruta, encoding='utf8'))
        claves = [v['situacion'][:40] for v in datos] if var == 'ADS_V6' else \
            [x[0] for k in ('obras', 'ediciones', 'ejemplares', 'lectores') for x in datos[k]]
        hall = [c for c in claves if c in plan_txt]
        chk('H', '%s: ninguno de los %d textos o códigos reservados está en la planificación' % (etiqueta, len(claves)), not hall, str(len(hall)))
        chk('H', '%s: la carpeta privada está fuera del repositorio' % etiqueta,
            not (os.path.realpath(ruta) + os.sep).startswith(os.path.realpath(REPO) + os.sep))
    else:
        no_ejecutado('H', '%s: falta la ruta privada (%s)' % (etiqueta, var))
nombres = [f for dp, _, fs in os.walk(PLAN) for f in fs]
chk('H', 'planificacion/ no tiene archivos reservados ni copias del PDF del MEC o del informe de Work',
    not [f for f in nombres if f in ('dr.json', 'variantes_v6.json') or f.lower().endswith('.pdf') and 'ADS_3BTI' not in f])
chk('H', 'Los planes recuerdan que un paquete recibido es código desconocido (Encuentro 34) y que el DR no se entrega (Encuentro 30)',
    'código desconocido' in TX['planes'] and 'El DR no se entrega ni se publica' in TX['planes'])
chk('H', 'Ningún nombre de modelo de IA en la planificación', not re.search(r'\b(Claude|Opus|Sonnet|Haiku|GPT|ChatGPT|Gemini)\b', plan_txt.replace('claude.ai/code', '')))

total = sum(len(v) for v in RES.values())
json.dump({'controles': RES, 'fallos': FALLOS, 'total': total,
           'no_ejecutados': sum(1 for v in RES.values() for x in v if x['resultado'] == 'no ejecutado'),
           'documentos': {k: {'paginas': len(PDF[k]), 'sha256_docx': sha(v + '.docx'), 'sha256_pdf': sha(v + '.pdf')} for k, v in DOCS.items()}},
          open(os.path.join(PLAN, 'CONTROLES_PLANIFICACION.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('\n%d controles, %d fallos' % (total, len(FALLOS)))
sys.exit(1 if FALLOS else 0)

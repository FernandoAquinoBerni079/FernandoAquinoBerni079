# -*- coding: utf-8 -*-
"""Controles automáticos del lote 1. Uso: python3 build/verificar.py   (sale con código 1 si hay fallos)
Bloques: A índice de Work · B capacidades · C trazabilidad de fuentes · D integración del Capítulo 2 ·
E Algorítmica 3.º · F voseo y residuos · G maqueta (DOCX) · H maqueta (PDF) · I evaluaciones · J numeración."""
import os, re, sys, json, hashlib, collections
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from docx import Document
from docx.oxml.ns import qn
import pymupdf

import comun as K
import prelim as P
import cap1, cap2, cap3
import importlib.util
D = K.D
MB = cap1.MB
RAIZ = K.RAIZ
ADS = os.path.dirname(RAIZ)
CAPS = (cap1, cap2, cap3)
EST = os.path.join(RAIZ, 'ADS_3BTI_LOTE1_ESTUDIANTE')
GUI = os.path.join(RAIZ, 'ADS_3BTI_LOTE1_GUIA_DOCENTE')

ok = fallos = 0
RES = collections.OrderedDict()
def chk(bloque, desc, cond, detalle=''):
    global ok, fallos
    RES.setdefault(bloque, [0, 0])
    if cond:
        ok += 1; RES[bloque][0] += 1
        print('CORRECTO [%s] %s' % (bloque, desc))
    else:
        fallos += 1; RES[bloque][1] += 1
        print('FALLA    [%s] %s %s' % (bloque, desc, detalle))

def texto_docx(ruta):
    d = Document(ruta)
    partes = [p.text for p in d.paragraphs]
    for t in d.tables:
        for r in t.rows:
            vistos = set()
            for c in r.cells:
                if id(c._tc) in vistos:
                    continue
                vistos.add(id(c._tc))
                partes.append(c.text)
    return d, '\n'.join(partes)

dE, tE = texto_docx(EST + '.docx')
dG, tG = texto_docx(GUI + '.docx')
pE = pymupdf.open(EST + '.pdf'); pG = pymupdf.open(GUI + '.pdf')
res_build = json.load(open(os.path.join(AQUI, 'resultado_construccion.json'), encoding='utf8'))

# ---------------------------------------------------------------- A. índice de Work
WORK = {
    1: ('Un sistema comienza con una necesidad', (1, 2), ['1.1 De la dificultad cotidiana al problema de información',
        '1.2 Personas, procesos, datos, recursos y límites del sistema',
        '1.3 Actores e interesados: necesidades diferentes, decisiones compartidas',
        '1.4 Diagnóstico de conocimientos previos y plan de apoyo'],
        'describir una biblioteca y separar hechos, supuestos y soluciones anticipadas'),
    2: ('Investigar antes de diseñar', (3, 4), ['2.1 Entrevistar para comprender tareas y problemas',
        '2.2 Observar un proceso y analizar documentos',
        '2.3 Contrastar fuentes, contradicciones y necesidades no expresadas',
        '2.4 Registrar evidencia con respeto por las personas y sus datos'],
        'dossier de relevamiento con roles de bibliotecario, lector y dirección'),
    3: ('Elegir un alcance posible', (5, 6), ['3.1 Objetivos y resultados esperados',
        '3.2 Comparación de alternativas y factibilidad básica',
        '3.3 Recursos, riesgos, límites y exclusiones',
        '3.4 Acuerdo de proyecto y organización del equipo'], None),
}
heads = [(p.style.name, p.text) for p in dE.paragraphs if p.style.name.startswith('Heading')]
htexts = [t for _, t in heads]
for C in CAPS:
    tit, enc, secs, prac = WORK[C.NUM]
    chk('A', 'Capítulo %d: título de Work «%s»' % (C.NUM, tit), C.TITULO == tit and '%s — %s' % (C.CAPITULO, tit) in htexts)
    chk('A', 'Capítulo %d: encuentros %s' % (C.NUM, enc), tuple(C.ENCUENTROS) == enc)
    chk('A', 'Capítulo %d: secciones de Work, textuales y en orden' % C.NUM,
        C.SECCIONES == secs and [h for h in htexts if h in secs] == secs)
    if prac:
        chk('A', 'Capítulo %d: práctica de Work («%s»)' % (C.NUM, prac), C.PRACTICA_WORK == prac)
chk('A', 'Capítulo 3 cierra con la revisión de la Unidad I y el hito H1', cap3.H1_TITULO in htexts and 'H1' in cap3.H1_TITULO)
chk('A', 'Preliminares: los ocho de Work, en orden', [h for h in htexts if h in P.TITULOS] == P.TITULOS)
pos = {t: htexts.index(t) for t in htexts}
orden = [P.TITULOS[0]] + ['%s — %s' % (C.CAPITULO, C.TITULO) for C in CAPS]
chk('A', 'Orden: preliminares, Capítulo 1, 2 y 3', [pos[t] for t in orden] == sorted(pos[t] for t in orden))

# ---------------------------------------------------------------- B. capacidades
for C in CAPS:
    r = C.ROTULO_CAPACIDAD
    chk('B', 'Capítulo %d: rótulo «propuesta para el programa institucional» y «no oficial del MEC»' % C.NUM,
        re.search(r'propuestas? para el programa institucional', r) and re.search(r'no (es una capacidad oficial|son capacidades oficiales) del MEC', r))
    chk('B', 'Capítulo %d: el rótulo figura en la ficha del libro y de la guía' % C.NUM, r in tE and r in tG)
CAPW = {'C1': 'Delimita un problema y evalúa la factibilidad de una solución.',
        'C2': 'Obtiene y contrasta información sobre necesidades de usuarios.',
        'C7': 'Organiza y registra el trabajo colaborativo'}
for C, cods in ((cap1, ('C1', 'C7')), (cap2, ('C2',)), (cap3, ('C1', 'C2', 'C7'))):
    chk('B', 'Capítulo %d: capacidades %s con el texto de Work' % (C.NUM, ', '.join(cods)), all(CAPW[c] in C.CAPACIDAD for c in cods))
chk('B', 'Mapa de capacidades: C1 a C10 con la nota «no son capacidades oficiales del MEC»',
    [f[0] for f in P.CAPACIDADES[1]] == ['C%d' % i for i in range(1, 11)] and 'no son capacidades oficiales del MEC' in tE)
malas_of = [tx[max(0, m.start() - 40):m.end()] for tx in (tE, tG) for m in re.finditer(r'(?i)capacidad(es)? oficial', tx)
            if not re.search(r'\b[Nn]o (es|son)\b', tx[max(0, m.start() - 40):m.start()])]
chk('B', 'Ninguna capacidad presentada como oficial del MEC (cada mención va precedida de «no es» / «no son»)', not malas_of, malas_of)

# ---------------------------------------------------------------- C. trazabilidad de fuentes
locales = dict(MB.FUENTES)
for C in CAPS:
    locales.update(C.EVAL_FUENTES)
def fuente(c):
    return D.TEXTO.get(c) or D.NECESIDAD.get(c) or locales.get(c)
PAT = r'(?:E\d-L\d+|O1-\d+|D\d-A?\d+|N-\d\d|V-\d\d|M-[NF]\d|MN-\d\d|[ATK]-\d|T\d-L?\d)'
for nombre, tx in (('libro', tE), ('guía', tG)):
    usados = sorted(set(re.findall(r'(?<![\w-])' + PAT + r'(?![\w-])', tx)))
    falt = [c for c in usados if fuente(c) is None]
    chk('C', '%s: los %d códigos de fuente citados existen en el caso o en la situación de evaluación' % (nombre, len(usados)), not falt, falt)
    citas = re.findall(r'«([^»]{6,})»\s*\(((?:%s)(?:,\s*%s)*)\)' % (PAT, PAT), tx)
    malas = []
    for q, cods in citas:
        cs = [c.strip() for c in cods.split(',')]
        if not any(fuente(c) and q.strip().rstrip('.') in fuente(c) for c in cs):
            malas.append((q[:50], cods))
    chk('C', '%s: %d citas textuales «…» (código) coinciden con la línea citada' % (nombre, len(citas)), not malas, malas)
for C in CAPS:
    for nivel, items in C.NIVELES:
        pass
chk('C', 'El libro reproduce todos los registros del dossier (D0, E1 a E5, O1, D1, D2) con todas sus líneas',
    all(('%s  ' % c) in tE for r in D.REGISTROS for c, _, _ in r['lineas']))
chk('C', 'Tabla 2.7: las trece necesidades con sus fuentes', all(c in tE and t in tE for c, t, _, _ in D.NECESIDADES))
chk('C', 'N-02 = «Evitar entregar a dos lectores el mismo ejemplar.», fuente E4-L4 (cadena del Capítulo 4)',
    D.NECESIDAD['N-02'] in tE and 'E4-L4' in dict((c, f) for c, _, f, _ in D.NECESIDADES)['N-02'])
chk('C', 'El Capítulo 3 presenta las reglas sin numerar y con el texto del caso',
    all(t in tE for _, t in D.REGLAS) and not re.search(r'\bRN-\d', tE))
chk('C', 'Sin requisitos numerados en el lote (RF, RNF, RS: Capítulo 4)', not re.search(r'\b(RF|RNF|RS)-\d', tE))
chk('C', 'Alcance mínimo con permisos mínimos (Work §7.2) y las ocho exclusiones tratadas',
    'Permisos mínimos' in tE and all(f in tE.lower() for f in ('pagos y multas', 'reservas en línea', 'códigos de barras', 'catálogo nacional')))
caso = os.path.join(RAIZ, 'caso', 'verificar_caso.py')
import subprocess
r = subprocess.run([sys.executable, caso], capture_output=True, text=True)
chk('C', 'caso/verificar_caso.py (incluye el control contra el Capítulo 4 v2): %s' % r.stdout.strip().split('\n')[-1], r.returncode == 0)

# ---------------------------------------------------------------- D. integración del Capítulo 2
spec = importlib.util.spec_from_file_location('cand', os.path.join(ADS, 'fase2_pilotos', 'A1_candidato_capitulo2', 'build', 'contenido.py'))
CC = importlib.util.module_from_spec(spec); spec.loader.exec_module(CC)
cuenta = collections.Counter(a for _, _, a in cap2.INTEGRACION)
chk('D', '31 elementos del candidato con destino: %s' % dict(cuenta),
    len(cap2.INTEGRACION) == 31 and cuenta == {'Adaptar': 15, 'Conservar': 8, 'Dividir': 1, 'Retirar': 4, 'Trasladar': 3})
chk('D', 'Conservar: TABLA_TECNICAS idéntica', cap2.TABLA_TECNICAS == CC.TABLA_TECNICAS)
chk('D', 'Conservar: TABLA_PREGUNTAS idéntica', cap2.TABLA_PREGUNTAS == CC.TABLA_PREGUNTAS)
chk('D', 'Conservar: EN_PARAGUAY idéntico', cap2.EN_PARAGUAY == CC.EN_PARAGUAY)
chk('D', 'Conservar: S44 (párrafos) idéntico', cap2.S44 == CC.S44[1])
chk('D', 'Conservar: EJ2 (cuerpo) idéntico como Ejemplo resuelto 2.1', cap2.EJ21[1] == CC.EJ2[1])
chk('D', 'Conservar: TRANSCRIPCION_E1, TRANSCRIPCION_E2 y OBSERVACION_O1 en el dossier (verificar_caso, bloque C)', r.returncode == 0)
chk('D', 'Trasladar: mapa de interesados en 1.3 con los valores del candidato', cap1.TABLA_14[1] == [[f[0], f[1], f[2], f[3], f[4]] for f in CC.TABLA_EJ1[1]])
chk('D', 'Retirar: el Capítulo 2 no redacta requisitos candidatos', 'requisito candidato' not in tE.lower() and not re.search(r'\bRC-\d', tE))
chk('D', 'Plan de integración: el dossier incluye E4 y E5 y cierra con N-01…', 'Registro E4' in tE and 'Registro E5' in tE and 'N-01' in tE)
chk('D', 'Semilla nueva de la evaluación del Capítulo 2 (distinta de ADS3-C4-1)', cap2.EVAL_ID != CC.EVAL_ID)

# ---------------------------------------------------------------- E. Algorítmica 3.º
todo = tE + '\n' + tG
chk('E', 'Sin personas ni títulos del caso de biblioteca de Algorítmica 3.º', not [p for p in D.PROHIBIDOS_ALGORITMICA if p in todo], [p for p in D.PROHIBIDOS_ALGORITMICA if p in todo])
chk('E', 'Sin matriz ponderada: ni «ponderad…» ni pesos 0,5 / 0,3 / 0,2', not re.search(r'(?i)ponderad', todo) and not re.search(r'\b0,[235]\b', todo))
pesos = re.findall(r'(?i)\bpesos?\b', todo)
chk('E', '«pesos» aparece solo en la remisión a Algorítmica 3.º (Práctica 4)', len(re.findall(r'(?i)\bpesos?\b', tE)) == 1 and 'asignar pesos a los criterios, esa técnica se trabaja en Algorítmica 3.º (Práctica 4)' in tE and not re.search(r'(?i)\bpesos?\b', tG))
chk('E', 'La comparación de alternativas no compara tecnologías (web, escritorio, app nativa)', not re.search(r'(?i)(sistema web|programa de escritorio|app android)', tE))
chk('E', 'La Tabla 3.3 no tiene números (fuera de los códigos de fuente)', not re.search(r'\d', re.sub(PAT, '', ' '.join(' '.join(f[1:]) for f in cap3.TABLA_33[1]))))

# ---------------------------------------------------------------- F. voseo y residuos
# Formas de tú inequívocas en cualquier posición, e imperativos de tú al comienzo de una consigna numerada.
# (Al comienzo de una oración cualquiera pueden ser tercera persona: «Anota la necesidad», dicho del analista.)
TUTEO = (r'\b(tienes|puedes|debes|sabes|quieres|eres|propón|tú)\b|(?:^\d+\.\s+|^\([a-h]\)\s+)'
         r'(Escribe|Lee|Completa|Indica|Explica|Clasifica|Responde|Anota|Marca|Elige|Justifica|Redacta|Compara|Describe|Identifica|Resume|Haz)\b')
for nombre, tx in (('libro', tE), ('guía', tG)):
    m = [x.group(0) for x in re.finditer(TUTEO, tx, re.M)]
    chk('F', '%s: sin formas de tuteo frecuentes' % nombre, not m, m[:5])
    chk('F', '%s: sin identificadores de modelos de IA' % nombre, not re.search(r'(?i)\b(claude|gpt|gemini|opus|sonnet|codex|chatgpt)\b', tx))
    chk('F', '%s: sin símbolos ✓ ✗' % nombre, not re.search('[✓✔✗✘✅]', tx))
    chk('F', '%s: sin marcadores sin reemplazar' % nombre, '§§' not in tx and 'TODO' not in tx and 'XXX' not in tx)
    chk('F', '%s: no se declara apto ni aprobado para la venta' % nombre, not re.search(r'(?i)\bapto\b|aprobado para (la )?(venta|comercializ)', tx.replace('No está aprobado para la venta', '')))

# ---------------------------------------------------------------- G. maqueta (DOCX)
for p in ('helpers.py', 'maqueta.py'):
    a = hashlib.sha256(open(os.path.join(AQUI, p), 'rb').read()).hexdigest()
    b = hashlib.sha256(open(os.path.join(ADS, 'fase2_pilotos', 'A2_capitulo4_v2_1', 'build', p), 'rb').read()).hexdigest()
    chk('G', '%s idéntico al del Capítulo 4 v2.1 (comportamiento de maqueta sin cambios)' % p, a == b)
for nombre, d in (('libro', dE), ('guía', dG)):
    filas = [r for t in d.tables for r in t.rows]
    chk('G', '%s: %d filas de tabla, todas «no dividir»' % (nombre, len(filas)),
        all(r._tr.trPr is not None and r._tr.trPr.find(qn('w:cantSplit')) is not None for r in filas))
    multi = [t for t in d.tables if len(t.columns) > 1]
    malas = [i for i, t in enumerate(multi) if abs(sum(int(g.get(qn('w:w'))) for g in t._tbl.tblGrid) - 9411) > 15]
    chk('G', '%s: %d tablas de varias columnas con tblGrid de 16,6 cm' % (nombre, len(multi)), not malas, malas)
    sin_enc = [t.rows[0].cells[0].text[:30] for t in multi if t.rows[0]._tr.trPr.find(qn('w:tblHeader')) is None]
    chk('G', '%s: toda tabla de datos repite su encabezado (las únicas sin encabezado son las %d fichas)' % (nombre, len(sin_enc)),
        all(s.startswith('Capacidad') for s in sin_enc), sin_enc)

# ---------------------------------------------------------------- H. maqueta (PDF)
def lineas(pg):
    return [l.strip() for l in pg.get_text().split('\n') if l.strip() and not re.match(r'^Página \d+ de \d+$', l.strip())]
for nombre, pdf in (('libro', pE), ('guía', pG)):
    vacias = [i + 1 for i, pg in enumerate(pdf) if not lineas(pg)]
    chk('H', '%s: ninguna página en blanco' % nombre, not vacias, vacias)
    sueltos = [i + 1 for i, pg in enumerate(pdf) if lineas(pg) and lineas(pg)[0].startswith('_' * 20)]
    chk('H', '%s: ninguna página empieza con renglones de respuesta sueltos' % nombre, not sueltos, sueltos)
for C in CAPS:
    pags = [i + 1 for i, pg in enumerate(pE) if C.EVAL_TITULO in lineas(pg)[:2]]
    chk('H', '%s: empieza en página propia (pág. %s)' % (C.EVAL_TITULO, pags), len(pags) == 1)
    pp = [i + 1 for i, pg in enumerate(pE) if any(l.startswith(C.PRACTICA_TITULO[:25]) for l in lineas(pg)[:1])]
    chk('H', '%s: empieza en página nueva' % C.PRACTICA_TITULO.split(' —')[0], len(pp) == 1)
paginas = res_build['paginas_libro']
indice = pE[1].get_text()
chk('H', 'El índice ocupa una sola página y la siguiente es «Presentación y alcance»', lineas(pE[2])[0] == P.TITULOS[0])
nums_ok = all(paginas[t] >= 3 for t in paginas)
chk('H', 'Índice: %d entradas con página, verificadas sobre el PDF final' % len(paginas), nums_ok and len(paginas) == len(set(paginas)) or nums_ok)
recalc, _ = K.paginas_de_titulos(EST + '.pdf', list(paginas), desde=2)
chk('H', 'Índice estable: las páginas del índice coinciden con el PDF', recalc == paginas)
n_est, n_gui = len(pE), len(pG)
chk('H', 'Extensión del libro: %d págs. (plan: 45 a 55 de capítulos + 6 a 8 de preliminares, con portada e índice)' % n_est, 51 <= n_est <= 65)
chk('H', 'Extensión de la guía: %d págs. (plan: 18 a 22)' % n_gui, 18 <= n_gui <= 22)

# ---------------------------------------------------------------- I. evaluaciones
claves = res_build['claves']
for C in CAPS:
    ks = [c for c in claves if c[0] == C.EVAL_ID]
    mc = [c[2] for c in ks if c[2] in 'abcd' and len(c[2]) == 1]
    chk('I', '%s: %d ítems con clave; opción múltiple con claves %s' % (C.EVAL_TITULO, len(ks), ''.join(mc)), len(ks) == len(C.EVAL_ITEMS) and len(set(mc)) >= 3)
    pts = sum(1 for it in C.EVAL_ITEMS if it[0] in ('mc', 'vf')) + sum(it[3] for it in C.EVAL_ITEMS if it[0] == 'ab')
    chk('I', '%s: suma 15 puntos, como dice su remisión' % C.EVAL_TITULO, pts == 15 and 'Puntaje total: 15 puntos' in C.EVAL_PUNTAJE)
    chk('I', '%s: la guía trae su clave y los criterios de los ítems abiertos' % C.EVAL_TITULO, ('Clave de la %s' % C.EVAL_TITULO.lower()) in tG)
chk('I', 'Semillas de evaluación distintas entre sí y del Capítulo 4', len({C.EVAL_ID for C in CAPS} | {'ADS3-C4v2-2'}) == 4)
chk('I', 'Rúbrica del H1: cuatro niveles de Work y cinco criterios con evidencia del equipo e individual',
    [n for n, _ in cap3.NIVELES_DESEMPENO] == ['4. Sólido', '3. Logrado', '2. En desarrollo', '1. Inicial'] and len(cap3.RUBRICA_H1) == 5
    and all(len(r[2]) == 4 and r[3] and r[4] for r in cap3.RUBRICA_H1))
chk('I', 'Proporción 60/40 rotulada como propuesta editorial (libro y guía)', '60 %' in tE and '40 %' in tE and 'propuesta editorial' in tE and '60 %' in tG and 'propuesta editorial' in tG)
chk('I', 'Ausencia de evidencia registrada aparte (Work §4.3)', 'ausencia de evidencia' in tG.lower() and 'Si falta una evidencia' in tE)
chk('I', 'Prácticas en tres niveles en cada capítulo', all([n.split(' —')[0] for n, _ in C.NIVELES] == ['Nivel 1', 'Nivel 2', 'Nivel 3'] for C in CAPS))
chk('I', 'Las prácticas usan el caso Mbokaja, distinto de los ejemplos (Arapoty)', all(MB.INSTITUCION in ' '.join(C.PRACTICA_INTRO) or 'Mbokaja' in ' '.join(C.PRACTICA_INTRO) or C is cap1 for C in CAPS) and MB.VISITA_TITULO in tE)
chk('I', 'Guía: secuencia en HC de los seis encuentros', all(('Encuentro %d' % n) in tG for n in range(1, 7)) and tG.count('aprox.') >= 18)
chk('I', 'Guía: tarjetas de rol de la Práctica 2 (solo en la guía)', all(t in tG and t not in tE for t, _ in MB.TARJETAS))
chk('I', 'Calendario de 28 encuentros: recuadro en cada capítulo y tabla en la guía', tE.count('Si el calendario se acorta') == 3 and 'Unidad I en 36 y en 28 encuentros' in tG)

# ---------------------------------------------------------------- J. numeración
for C in CAPS:
    n = C.NUM
    for tipo in ('Tabla', 'Figura', 'Ejemplo resuelto'):
        sec = []
        for m in re.finditer(r'^%s %d\.(\d+)(?: —|:)' % (tipo, n), tE, re.M):
            sec.append(int(m.group(1)))
        chk('J', 'Capítulo %d: %s %d.1 a %d.%d correlativas, sin repetir' % (n, tipo.lower(), n, n, len(sec)), sec == list(range(1, len(sec) + 1)) and len(sec) >= (1 if tipo == 'Figura' else 2), sec)
    refs = set(int(x) for x in re.findall(r'Tabla %d\.(\d+)' % n, tE))
    defs = set(int(x) for x in re.findall(r'^Tabla %d\.(\d+) —' % n, tE, re.M))
    chk('J', 'Capítulo %d: toda tabla mencionada existe' % n, refs <= defs, refs - defs)
    refs = set(int(x) for x in re.findall(r'Ejemplo resuelto %d\.(\d+)' % n, tE + tG))
    defs = set(int(x) for x in re.findall(r'^Ejemplo resuelto %d\.(\d+):' % n, tE, re.M))
    chk('J', 'Capítulo %d: todo ejemplo resuelto mencionado existe' % n, refs <= defs, refs - defs)

print('\nResultado por bloque:')
for b, (o, f) in RES.items():
    print('  %s: %d correctos, %d fallos' % (b, o, f))
print('Resultado: %d correctos, %d fallos' % (ok, fallos))
json.dump({'correctos': ok, 'fallos': fallos, 'bloques': RES}, open(os.path.join(AQUI, 'verificacion_resultado.json'), 'w'), indent=1)
sys.exit(1 if fallos else 0)

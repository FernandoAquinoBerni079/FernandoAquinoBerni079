# -*- coding: utf-8 -*-
"""Controles automáticos del lote 4 (Unidad IV). Uso: python3 lote_4/build/verificar.py   (sale con 1 si hay fallos)

Bloques de los lotes 2 y 3, extendidos a los Capítulos 10 a 13: A índice de Work · B capacidades · C trazabilidad de
fuentes · E no duplicar Laboratorio ni Algorítmica · F voseo y residuos · G maqueta (DOCX) · H maqueta (PDF) ·
I evaluaciones, prácticas e instrumentos · J numeración · L notaciones · Q lotes 1 a 3 intactos.
Bloques nuevos (plan del lote 4, §12, y decisiones de Fernando del 21-oct-2026): K contratos implementados ·
R autorización (ME-12 y ME-13) · S RI-01, historial y garantías de instalación y restauración · T fragmentos de código ·
U distribuciones de la base · V pruebas y entorno."""
import os, re, sys, json, collections, subprocess, hashlib, shutil, tempfile
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
L4 = os.path.dirname(AQUI)
ADS = os.path.dirname(L4)
sys.path.insert(0, AQUI)
from docx import Document
from docx.oxml.ns import qn
import pymupdf

import construir as B
import oficio as O
K = O.K
import cap10, cap11, cap12, cap13, guia_u4 as GU
import fragmentos as F
import diagramas_u4 as G
C, X, MB = B.C, B.X, B.MB
R, D = X.R, X.D
CAPS = (cap10, cap11, cap12, cap13)
EST, GUI, CUA = B.RUTA_EST[:-5], B.RUTA_GUIA[:-5], B.RUTA_CUAD[:-5]
REF, BASE = os.path.join(C.PROY, 'referencia_docente'), os.path.join(C.PROY, 'base_estudiante')

ok = fallos = 0
RES = collections.OrderedDict()
DETALLE = []


def chk(bloque, desc, cond, detalle=''):
    global ok, fallos
    RES.setdefault(bloque, [0, 0])
    cond = bool(cond)
    if cond:
        ok += 1; RES[bloque][0] += 1
        print('CORRECTO [%s] %s' % (bloque, desc))
    else:
        fallos += 1; RES[bloque][1] += 1
        print('FALLA    [%s] %s %s' % (bloque, desc, detalle))
    DETALLE.append({'bloque': bloque, 'control': desc, 'resultado': 'correcto' if cond else 'FALLA'})


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


def leer(*p):
    return open(os.path.join(*p), encoding='utf8').read()


dE, tE = texto_docx(EST + '.docx')
dG, tG = texto_docx(GUI + '.docx')
dC, tC = texto_docx(CUA + '.docx')
pE, pG, pC = pymupdf.open(EST + '.pdf'), pymupdf.open(GUI + '.pdf'), pymupdf.open(CUA + '.pdf')
res_build = json.load(open(os.path.join(L4, 'resultado_construccion.json'), encoding='utf8'))
todo = tE + '\n' + tG + '\n' + tC
j = lambda x: json.dumps(x, ensure_ascii=False)
heads = [p.text for d in (dE, dG, dC) for p in d.paragraphs if p.style.name.startswith('Heading')]
reglas_ref, reglas_base = leer(REF, 'src', 'reglas.php'), leer(BASE, 'src', 'reglas.php')
esquema = leer(REF, 'src', 'esquema.sql')


def funcion(src, nombre):
    """Cuerpo de una función PHP de nivel superior (desde «function nombre(» hasta la llave de cierre en la columna 0)."""
    i = src.index('function %s(' % nombre)
    return src[i:src.index('\n}', i) + 2]


# ---------------------------------------------------------------- A. índice de Work (§6, textual; §5.2)
WORK = {
    10: ('Del diseño a la primera operación funcional', (19, 20),
         ['10.1. Preparación del entorno y estructura del proyecto.', '10.2. Versiones, bitácora y conjunto inicial de datos ficticios.',
          '10.3. Una operación completa: formulario, procesamiento y almacenamiento.', '10.4. Validación, consulta parametrizada y evidencia de persistencia.'],
         'demostrar una operación y vincularla con su requisito y prueba'),
    11: ('Catálogo, ejemplares y lectores', (21, 22),
         ['11.1. Implementación de tareas priorizadas a partir de los bocetos.', '11.2. Datos obligatorios, códigos, duplicados y mensajes útiles.',
          '11.3. Permisos mínimos y comprobaciones del servidor.', '11.4. Edición y baja lógica sin pérdida de historial.'],
         'registrar un lote distinto del ejemplo y resolver entradas inválidas'),
    12: ('Préstamos y devoluciones consistentes', (23, 24),
         ['12.1. Precondiciones y reglas de la operación de préstamo.', '12.2. Doble envío, disponibilidad y operaciones atómicas.',
          '12.3. Devolución, estado del ejemplar y conservación de historial.', '12.4. Fallos previsibles y comprobación de resultados.'],
         'resolver dos solicitudes incompatibles y explicar la protección elegida'),
    13: ('Información útil e integración', (25, 26),
         ['13.1. Búsqueda de ejemplares disponibles y préstamos activos.', '13.2. Vencimientos y fecha de referencia.',
          '13.3. Integración de módulos y revisión del alcance mínimo.', '13.4. Demostración del incremento y registro de pendientes.'],
         None),
}
work_txt = leer('/tmp/claude-0/fuentes/work.txt') if os.path.exists('/tmp/claude-0/fuentes/work.txt') else ''
for Cm in CAPS:
    t, enc, secs, prac = WORK[Cm.NUM]
    chk('A', 'Capítulo %d: título y encuentros %s de Work §6' % (Cm.NUM, enc), Cm.TITULO == t and Cm.ENCUENTROS == enc
        and ('%s — %s' % (Cm.CAPITULO, t)) in tE)
    chk('A', 'Capítulo %d: las cuatro secciones con el texto de Work §6, como títulos del libro' % Cm.NUM,
        [s.replace('. ', ' ', 1).rstrip('.') for s in secs] == Cm.SECCIONES and all(s in heads for s in Cm.SECCIONES))
    if prac:
        chk('A', 'Capítulo %d: la práctica es la de Work §6 («%s»)' % (Cm.NUM, prac), Cm.PRACTICA_WORK == prac)
chk('A', 'Capítulo 13: cierre de Work «Revisión de unidad IV: circuito funcional completo; H4»',
    cap13.REVISION_WORK == 'Revisión de unidad IV: circuito funcional completo; H4' and 'circuito funcional completo' in cap13.H4_TITULO)
chk('A', 'Capítulo 13: la práctica es un complemento editorial rotulado como tal, en el Encuentro 25 o complementaria',
    'complemento editorial' in cap13.PRACTICA_TITULO and 'no figura en el índice de Work' in cap13.PRACTICA_INTRO[0]
    and 'Encuentro 25 o como actividad complementaria' in cap13.PRACTICA_INTRO[0])
if work_txt:
    w = re.sub(r'\s+', ' ', work_txt)
    chk('A', 'Las 16 secciones están textuales en el informe de Work', all(s in w for v in WORK.values() for s in v[2]),
        [s for v in WORK.values() for s in v[2] if s not in w])
chk('A', 'Resultado de la unidad de Work §5.1 en la apertura («circuito funcional integrado y persistente»)',
    'circuito funcional integrado y persistente' in tE)
chk('A', 'Apertura: las evidencias de Work §5.2 de los ocho encuentros',
    all(x in tE for x in ('Ejecución inicial reproducible', 'prueba de persistencia', 'rechazo de acceso indebido',
                          'Operación coherente ante reenvío o segunda solicitud', 'Reporte correcto con fecha de referencia definida',
                          'prototipo completo mínimo y lista de incidencias')))

# ---------------------------------------------------------------- B. capacidades
CAPW = {'C3': 'Especifica y prioriza requisitos verificables.', 'C5': 'Justifica el modelo de información y sus reglas de integridad.',
        'C6': 'Diseña la interacción y la arquitectura del prototipo.', 'C7': 'Organiza y registra el trabajo colaborativo.',
        'C8': 'Integra un prototipo funcional con persistencia.', 'C9': 'Verifica y mejora la solución a partir de evidencia.'}
ESPERADAS = {10: ('C6', 'C7', 'C8', 'C9'), 11: ('C5', 'C6', 'C8'), 12: ('C5', 'C8', 'C9'), 13: ('C3', 'C8')}   # Work §5.2, enc. 19 a 25
for Cm in CAPS:
    r = Cm.ROTULO_CAPACIDAD
    chk('B', 'Capítulo %d: rótulo «propuestas para el programa institucional» y «no son capacidades oficiales del MEC»' % Cm.NUM,
        'propuestas para el programa institucional' in r and 'no son capacidades oficiales del MEC' in r and r in tE and r in tG)
    chk('B', 'Capítulo %d: capacidades %s de Work §5.2, con su texto de §4.2' % (Cm.NUM, ', '.join(ESPERADAS[Cm.NUM])),
        all(('%s. %s' % (c, CAPW[c])) in Cm.CAPACIDAD and c in r for c in ESPERADAS[Cm.NUM]))
chk('B', 'Encuentros 19 (C7, C8), 20 (C6, C8, C9), 21 (C5, C8), 22 (C6, C8) en los rótulos',
    'C7 y C8 en el Encuentro 19; C6, C8 y C9' in cap10.ROTULO_CAPACIDAD and 'C5 y C8 en el Encuentro 21; C6 y C8' in cap11.ROTULO_CAPACIDAD)
chk('B', 'Capítulo 13: el H4 evalúa C7 a C9', 'C7 a C9' in cap13.CAPACIDAD and 'C7 a' in cap13.ROTULO_CAPACIDAD)
malas_of = [tx[max(0, m.start() - 40):m.end()] for tx in (tE, tG, tC) for m in re.finditer(r'(?i)capacidad(es)? oficial', tx)
            if not re.search(r'\b[Nn]o (es|son)( una)?\b', tx[max(0, m.start() - 40):m.start()])]
chk('B', 'Ninguna capacidad presentada como oficial del MEC', not malas_of, malas_of)

# ---------------------------------------------------------------- C. trazabilidad de fuentes
locales = dict(MB.FUENTES)
for Cm in CAPS:
    locales.update(Cm.EVAL_FUENTES)
locales.update({m[0]: m[4] for m in X.MENSAJES})
locales.update(C.MENSAJES_PHP)
locales.update({i[0]: i[2] for i in C.INCIDENCIAS})
locales.update({e[0]: e[1] for e in C.FICHA_ENTORNO})


def fuente(c):
    return (R.TEXTO.get(c) or D.NECESIDAD.get(c) or X.REGLA.get(c) or locales.get(c) or (c if C.existe(c) else None)
            or (c if c in ('E-6', 'P-06a', 'P-06b') else None))


PAT = (r'(?:E\d-L\d+|D\d-A?\d+|N-\d\d|V-\d\d|M-[NF]\d\d?|MN-\d\d|MP-\d|MS-\d|MC-\d|MR-\d\d|OBS-\d|MD-\d\d|ML-\d|MI-\d\d|IN-\d\d'
       r'|V4-\d|EF-\d|AV-\d|CA-\d|E-\d+[ab]?|OA-\d\d|PA-\d\d|MA-\d\d|MV-\d\d'
       r'|RI-\d\d|PT-\d\d|ME-\d\d|OP-\d\d|DT-\d\d|CU-\d\d|P-\d\d[ab]?|RF-\d\d|RNF-\d\d|RS-\d\d|RN-\d\d)')
for nombre, tx in (('libro', tE), ('guía', tG), ('cuaderno', tC)):
    usados = sorted(set(re.findall(r'(?<![\w-])' + PAT + r'(?![\w-])', tx)))
    falt = [c for c in usados if fuente(c) is None]
    chk('C', '%s: los %d códigos citados existen en las fuentes' % (nombre, len(usados)), not falt, falt)
nuevos = set(MB.FUENTES) - set(MB.MB3.FUENTES)
chk('C', 'Mbokaja U4: %d códigos nuevos (M-F10, M-F11, MD, ML, MS-6, MI) que no repiten ninguno anterior' % len(nuevos),
    len(nuevos) == 2 + len(MB.LOTE) + len(MB.LECTORES) + len(MB.SITUACIONES) + len(MB.SEMANA))
chk('C', 'Datos de prueba ficticios: los lectores de la base se nombran por descripción y llevan «ficticio»',
    all('ficticio' in l[1] for l in C.DATOS_INICIALES['lectores']) and all('ficti' in o[2] for o in C.DATOS_INICIALES['obras']))
chk('C', 'Los mensajes ME de mensajes.php reproducen exactamente los de la Tabla 8.6 (lote 3 v1.1), con los datos del diseño',
    all(C.con_datos(m[0], *C.EJEMPLOS_ME.get(m[0], ())) == m[4] for m in X.MENSAJES if m[0] != 'ME-11'))
chk('C', 'Cada mensaje MA y MV tiene su uso documentado', set(k for k in C.MENSAJES_PHP if k[:2] in ('MA', 'MV')) == set(C.USO_MENSAJE))

# ---------------------------------------------------------------- K. contratos implementados
FUNC = {'OP-01': 'registrar_prestamo', 'OP-02': 'registrar_devolucion', 'OP-03': 'consultar_disponibilidad',
        'OP-04': 'listar_prestamos_activos', 'OP-05': 'informe_mensual', 'OP-06': 'inactivar',
        'OA-01': 'alta_ejemplar', 'OA-02': 'alta_obra_edicion', 'OA-03': 'alta_lector', 'OA-04': 'editar_lector', 'OA-05': 'editar_obra'}
AUXF = {'registrar_prestamo': ['comprobar_prestamo'], 'alta_lector': ['validar_lector'], 'editar_lector': ['validar_lector']}
for op, fn in FUNC.items():
    cuerpo = funcion(reglas_ref, fn) + ''.join(funcion(reglas_ref, a) for a in AUXF.get(fn, []))
    if op == 'OP-03':   # ME-09 lo muestra la pantalla para cada obra sin disponibles (resultado del contrato)
        cuerpo += leer(REF, 'public', 'index.php').replace("mensaje('ME-09')", "'ME-09'")
    errores = (re.findall(r'ME-\d\d', ' '.join(X.OPERACION[op][5])) if op.startswith('OP') else
               [e for e in C.AUX[op][6]])
    faltan = [e for e in errores if e != 'ME-13' and ("'%s'" % e) not in cuerpo]
    chk('K', '%s (%s): implementado y con todos los errores de su contrato (%s)' % (op, fn, ', '.join(errores)), not faltan, faltan)
    chk('K', '%s: la base del estudiante trae el contrato y responde PENDIENTE' % op, 'return pendiente(' in funcion(reglas_base, fn))
chk('K', 'Cada operación auxiliar tiene su prueba (PA-01 a PA-05) en prueba_contratos.php',
    all(('%s:' % a[8]) in leer(REF, 'pruebas', 'prueba_contratos.php') for a in C.AUXILIARES))
chk('K', 'Las operaciones auxiliares no se atribuyen a contratos existentes: códigos OA propios y PT-08',
    all(a[0].startswith('OA-') and a[2] == 'PT-08' for a in C.AUXILIARES) and 'operación auxiliar' in tE)
chk('K', 'Las pruebas previstas del lote 2 que se ejecutan en la unidad están en prueba_contratos.php',
    all(p in leer(REF, 'pruebas', 'prueba_contratos.php') for p in ('P-01', 'P-02', 'P-03', 'P-04', 'P-05', 'P-06a', 'P-06b', 'P-07', 'P-08', 'P-09', 'P-10', 'P-11', 'P-12')))

# ---------------------------------------------------------------- R. autorización
chk('R', 'Ninguna operación usa ME-12 (src/reglas.php, referencia y base)', "'ME-12'" not in reglas_ref and "'ME-12'" not in reglas_base)
for op, fn in FUNC.items():
    roles = X.ROLES_OP.get(op, ['bibliotecaria'])
    cuerpo = funcion(reglas_ref, fn)
    if not roles:
        chk('R', '%s es pública: no comprueba rol ni devuelve ME-13' % op, 'sin_permiso' not in cuerpo and 'ME-13' not in cuerpo)
    else:
        php = sorted('direccion' if r == 'dirección' else r for r in roles)
        m = re.search(r'sin_permiso\(\$cuenta, array\(([^)]*)\)\)', cuerpo)
        chk('R', '%s: primera comprobación sin_permiso con los roles de su contrato (%s)' % (op, ', '.join(php)),
            m and sorted(re.findall(r"'(\w+)'", m.group(1))) == php and cuerpo.index('sin_permiso') < cuerpo.index('$pdo->', cuerpo.index('{')) if '$pdo->' in cuerpo else m)
ZONA_PHP = {'PT-01': 'index.php', 'PT-03': 'login.php', 'PT-04': 'inicio.php', 'PT-05': 'prestamo.php', 'PT-06': 'devolucion.php',
            'PT-07': 'activos.php', 'PT-08': 'lectores.php', 'PT-09': 'informe.php'}
for pt, arch in ZONA_PHP.items():
    zona = X.PANTALLA[pt][2]
    s = leer(REF, 'public', arch)
    if zona == 'Pública':
        chk('R', '%s (%s) es pública: no exige zona' % (pt, arch), 'exigir_zona(' not in s)
    else:
        chk('R', '%s (%s) exige la zona «%s»' % (pt, arch, zona), "exigir_zona('%s')" % zona in s)
auth = leer(REF, 'src', 'auth.php')
chk('R', 'ROLES_ZONA del código coincide con el diseño v1.1 (PT-09 para bibliotecaria y dirección)',
    "'Bibliotecaria o dirección' => array('bibliotecaria', 'direccion')" in auth and "'Bibliotecaria' => array('bibliotecaria')" in auth)
chk('R', 'ME-12 solo en el ingreso (auth.php: ingresar) y ME-13 en exigir_zona', 'ME-12' in funcion(auth, 'ingresar') and 'ME-13' in funcion(auth, 'exigir_zona'))
_t12 = todo.replace('ingreso (ME-12), zonas y permisos (ME-13)', '').replace('Usar ME-12 para un permiso que falta', '')
chk('R', 'Ningún texto asocia ME-12 con falta de permiso (salvo el error frecuente que lo corrige)', not re.search(r'ME-12[^.\n]{0,40}(permiso|autoriz)', _t12),
    re.findall(r'ME-12[^.\n]{0,40}(?:permiso|autoriz)', _t12))
chk('R', 'Libro: Tabla 11.3 con ME-13 para cada operación protegida y permitida para OP-03',
    cap11.TABLA_113_ROTULO in tE and all(f[1] == 'Permitida' for f in cap11.TABLA_113[1] if f[0].startswith('OP-03')))

# ---------------------------------------------------------------- S. RI-01, historial y garantías
pr = funcion(reglas_ref, 'registrar_prestamo')
chk('S', 'RI-01, primera barrera: comprobación y registro entre BEGIN IMMEDIATE y COMMIT',
    pr.index("exec('BEGIN IMMEDIATE')") < pr.index('comprobar_prestamo') < pr.index('INSERT INTO prestamos') < pr.index("exec('COMMIT')"))
chk('S', 'RI-01, segunda barrera: índice único parcial sobre los préstamos sin devolución',
    re.search(r'CREATE UNIQUE INDEX \w+ ON prestamos\(ejemplar_id\)\s*WHERE fecha_devolucion IS NULL', esquema))
chk('S', 'Si actúa la segunda barrera, la operación deshace y responde ME-03', "'UNIQUE'" in pr and 'ROLLBACK' in pr and "'ME-03'" in pr)
chk('S', 'El libro explica las dos barreras (Códigos 12.1 y 12.2) y P-07', 'Código 12.1' in tE and 'Código 12.2' in tE and 'dos protecciones' in tE)
chk('S', 'Ninguna operación borra datos (sin DELETE en src/reglas.php)', 'DELETE' not in reglas_ref.upper().replace('NO SE BORRA', ''))
chk('S', 'La base protege el historial: préstamos sin borrado, datos fijos, devolución única y códigos con historial',
    all(('CREATE TRIGGER %s' % t) in esquema for t in ('prestamos_sin_borrado', 'prestamos_datos_fijos', 'devolucion_unica',
                                                      'ejemplar_con_historial', 'lector_con_historial', 'codigo_ejemplar_con_historial')))
chk('S', 'Devolución única: una sola sentencia sobre el préstamo activo y ME-06 si no cambió ninguna fila',
    'fecha_devolucion IS NULL' in funcion(reglas_ref, 'registrar_devolucion') and 'rowCount() !== 1' in funcion(reglas_ref, 'registrar_devolucion'))


def _php(cwd, *args, entrada=None):
    return subprocess.run(['php'] + list(args), cwd=cwd, capture_output=True, text=True, input=entrada, timeout=120)


tmp = tempfile.mkdtemp(prefix='l4_garantias_')
try:
    copia = os.path.join(tmp, 'base')
    shutil.copytree(BASE, copia, ignore=shutil.ignore_patterns('biblioteca.sqlite*'))
    r1 = _php(copia, 'instalar.php', '--clave=solo-prueba-local')
    bd = os.path.join(copia, 'datos', 'biblioteca.sqlite')
    h1 = hashlib.sha256(open(bd, 'rb').read()).hexdigest()
    r2 = _php(copia, 'instalar.php')
    chk('S', 'Instalar sobre una base existente no la toca (sale con error y el archivo queda igual)',
        r1.returncode == 0 and r2.returncode != 0 and hashlib.sha256(open(bd, 'rb').read()).hexdigest() == h1, r2.stderr[:200])
    r3 = _php(copia, 'instalar.php', '--reiniciar', entrada='no\n')
    chk('S', 'Reiniciar sin escribir REINICIAR no cambia nada',
        r3.returncode != 0 and hashlib.sha256(open(bd, 'rb').read()).hexdigest() == h1)
    falso = os.path.join(tmp, 'no_es_respaldo.sqlite'); open(falso, 'w').write('texto')
    r4 = _php(copia, 'restaurar.php', falso, '--si')
    chk('S', 'Restaurar un archivo que no es un respaldo válido se rechaza sin tocar la base',
        r4.returncode != 0 and hashlib.sha256(open(bd, 'rb').read()).hexdigest() == h1, (r4.stdout + r4.stderr)[:200])
    r5 = _php(copia, 'restaurar.php', bd, '--si')
    chk('S', 'Restaurar la base sobre sí misma se rechaza', r5.returncode != 0 and hashlib.sha256(open(bd, 'rb').read()).hexdigest() == h1)
finally:
    shutil.rmtree(tmp, ignore_errors=True)
chk('S', 'Sin contraseñas en los materiales: la clave de demostración se genera al instalar y la de prueba no aparece',
    'prueba-solo-local' not in todo and re.search(r'random_bytes', leer(REF, 'src', 'datos_ejemplo.php')))

# ---------------------------------------------------------------- T. fragmentos de código
codigo_libro = {}
for fid in F.TODOS:
    ls = F.extraer(fid)
    archivo = os.path.join(C.PROY, F.TODOS[fid][0])
    chk('T', '%s: leído tal cual de %s (%d líneas), ninguna de más de %d caracteres' % (fid, F.TODOS[fid][0], len(ls), F.ANCHO),
        '\n'.join(ls) in leer(archivo).replace('\r', '') and max(len(l) for l in ls) <= F.ANCHO and len(ls) <= 40)
    dest, otro = (tE, tG) if fid in F.FRAGMENTOS else (tG, tE)
    con_ficha = all(v in dest for v in F.ficha(fid).values())
    chk('T', '%s: con su ficha (archivo, propósito, requisito o contrato, entradas, resultado y prueba) en %s'
        % (fid, 'el libro' if fid in F.FRAGMENTOS else 'la guía'), con_ficha and all(l.strip() in dest for l in ls if l.strip()))
for fid in F.REFERENCIA:
    del_libro = {l.strip() for f in F.FRAGMENTOS for l in F.extraer(f)}
    propias = [l.strip() for l in F.extraer(fid) if len(l.strip()) > 25 and l.strip() not in del_libro]
    chk('T', '%s no se publica en el libro ni en el cuaderno (es actividad de los equipos)' % fid,
        not [l for l in propias if l in tE or l in tC])
_citas = re.sub(r'^Código \d+\.\d+ —', '', tE, flags=re.M)
chk('T', 'Cada fragmento del libro se cita en el texto y tiene explicación', all(re.search(r'Códigos? (?:\d+\.\d+(?:,| y) )*%s\b' % re.escape(f.split()[1]), _citas) for f in F.FRAGMENTOS)
    and all(f in getattr(Cm, 'EXPLICA', {}) for Cm in CAPS for f in F.del_capitulo(Cm.NUM)))
num = [tuple(map(int, f.split()[1].split('.'))) for f in F.FRAGMENTOS]
orden = [tuple(map(int, m.group(1).split('.'))) for m in re.finditer(r'^Código (\d+\.\d+) —', tE, re.M)]
chk('T', 'Códigos numerados por capítulo, correlativos y en orden de aparición (%d)' % len(orden),
    orden == sorted(num) and all(b == (a[0], a[1] + 1) or b == (a[0] + 1, 1) for a, b in zip(orden, orden[1:])), orden)
chk('T', 'Fragmentos breves: ninguno de más de 20 líneas en el libro y menos de 200 líneas en total',
    max(len(F.extraer(f)) for f in F.FRAGMENTOS) <= 20 and sum(len(F.extraer(f)) for f in F.FRAGMENTOS) < 200,
    sum(len(F.extraer(f)) for f in F.FRAGMENTOS))
chk('T', 'El libro no publica resueltas comprobar_prestamo (salvo la llamada), validar_lector ni la consulta del informe',
    "return $sale(resultado(false, 'ME-01'))" not in tE and "'MV-03');" not in tE and 'GROUP BY grupo' not in tE)

# ---------------------------------------------------------------- U. distribuciones de la base
comunes = [a for a in GU._archivos(REF) if os.path.exists(os.path.join(BASE, a))]
distintos = [a for a in comunes if leer(REF, a) != leer(BASE, a)]
chk('U', 'Archivos comunes idénticos en las dos distribuciones salvo reglas, inicio, índice y PT-08 (%d comunes)' % len(comunes),
    sorted(distintos) == sorted(['src/reglas.php', 'public/index.php', 'public/inicio.php', 'public/lectores.php', 'LEEME.txt']), distintos)
solo_ref = sorted(a for a in GU._archivos(REF) if not os.path.exists(os.path.join(BASE, a)))
chk('U', 'Las páginas de las operaciones del curso no están en la base (%s)' % ', '.join(solo_ref),
    {'public/prestamo.php', 'public/devolucion.php', 'public/activos.php', 'public/informe.php'} <= set(solo_ref))
resueltas = [fn for fn in FUNC.values() if 'return pendiente(' not in funcion(reglas_base, fn)]
chk('U', 'La base del estudiante no trae ninguna operación resuelta', not resueltas, resueltas)
_, (ta, tb, ha, hb) = GU.tabla_lineas()
chk('U', 'Base del estudiante: %d líneas de código PHP de arranque, por debajo de 400 (%d con comentarios y vacías)' % (tb, ta), tb < 400)
chk('U', 'La guía informa el tamaño y justifica el exceso de las herramientas de seguridad y respaldo (%d líneas)' % ha,
    'Tamaño de la base del estudiante (PHP propio)' in tG and 'no se recortaron' in tG)

# ---------------------------------------------------------------- V. pruebas y entorno
res = C.resultados_pruebas()
chk('V', 'Última ejecución de build/reproducir.py sin fallos y con el entorno registrado',
    res and res['fallos'] == 0 and res['entorno']['php'] and 'NO es una computadora escolar' in res['entorno']['tipo'])
chk('V', 'Cada resultado de prueba guardado tiene su línea de entorno',
    all('Entorno' in leer(L4, 'resultados_pruebas', f) or f == 'resumen.json' for f in os.listdir(os.path.join(L4, 'resultados_pruebas'))))
chk('V', 'Base del estudiante: las operaciones pendientes no cuentan como falla; E-6b separada de E-6a',
    res['base_estudiante']['prueba_mis_operaciones.php']['pendientes'] > 0 and res['base_estudiante']['prueba_mis_operaciones.php']['codigo_salida'] == 0
    and 'prueba_base.sh' in res['base_estudiante'] and 'prueba_http.sh' in res['referencia_docente'])
chk('V', 'Ficha de entorno: E-6 separada en E-6a (docente completo) y E-6b (base, sin exigir operaciones)',
    [f[0] for f in C.FICHA_ENTORNO].count('E-6a') == 1 and 'no exige las operaciones' in j(C.FICHA_ENTORNO) and 'E-6' not in [f[0] for f in C.FICHA_ENTORNO])
chk('V', 'Cada capítulo advierte que el entorno no se probó en la institución', tE.count(C.AVISO_ENTORNO[0]) >= 5)
chk('V', 'Tabla 12.2: la prueba de carrera con el entorno donde corrió y Windows pendiente',
    res['entorno']['sqlite'] in j(cap12.TABLA_122) and 'Pendiente' in j(cap12.TABLA_122) and 'No se declara aprobado' in j(cap12.TABLA_122))
chk('V', 'Concurrencia en Windows: procesos independientes, no el servidor incorporado; pendientes sin declararlos aprobados',
    'procesos independientes' in tG and 'de a uno' in tG and 'No se declara aprobada' in j(C.PROTOCOLO_CONCURRENCIA))
malas = re.findall(r'(?i)(?:entorno|base|sistema|prototipo|computadora)[^.\n]{0,40}\bvalidad[oa]s?\b|probad[oa]s? en (?:los )?colegios|\bapto para todos', todo)
chk('V', 'Ningún entorno se declara validado ni probado en colegios', not [m for m in malas], malas[:5])
chk('V', 'Guía: evidencias equivalentes para otro entorno y sin una segunda colección', 'Evidencias equivalentes (Work §7.5)' in tG
    and all(e[0] in tG for e in C.EVIDENCIAS_EQUIVALENTES))
chk('V', 'Guía: resultados de las pruebas por distribución, con el entorno', 'Resultados de las pruebas (build/reproducir.py)' in tG and res['entorno']['sistema'] in tG)

# ---------------------------------------------------------------- E. no duplicar Laboratorio ni Algorítmica
chk('E', 'Sin unidad de sintaxis PHP ni manual de SQL (ningún título lo es)', not [h for h in heads if re.search(r'(?i)sintaxis|manual de sql|introducci[oó]n a php', h)])
chk('E', 'Sin Access ni tablas «Socios» (la guía solo los nombra para decir que no se usan)', 'Access' not in tE + tC and 'Socios' not in todo
    and all(re.search(r'\bni\b[^.]*Access', s) for s in re.findall(r'[^.]*Access[^.]*\.', tG)))
chk('E', 'Sin personas, títulos ni archivos del caso de Algorítmica 3.º', not [p for p in D.PROHIBIDOS_ALGORITMICA if p in todo])
chk('E', 'Guía: coordinación con Laboratorio antes del Encuentro 19 (Work §3)', 'Antes del Encuentro 19' in tG and 'Laboratorio confirma' in tG)

# ---------------------------------------------------------------- F. voseo y residuos
TUTEO = (r'\b(tienes|puedes|debes|sabes|quieres|eres|propón|tú)\b|(?:^\d+\.\s+|^\([a-h]\)\s+)'
         r'(Escribe|Lee|Completa|Indica|Explica|Clasifica|Responde|Anota|Marca|Elige|Justifica|Redacta|Compara|Describe|Identifica|Resume|Haz|Dibuja|Construye|Ejecuta|Registra|Señala|Decide|Diseña|Aplica|Revisa|Agrega|Calcula|Demuestra)\b')
for nombre, tx in (('libro', tE), ('guía', tG), ('cuaderno', tC)):
    m = [x.group(0) for x in re.finditer(TUTEO, tx, re.M)]
    chk('F', '%s: sin formas de tuteo frecuentes' % nombre, not m, m[:5])
    chk('F', '%s: sin identificadores de modelos de IA' % nombre, not re.search(r'(?i)\b(claude|gpt|gemini|opus|sonnet|codex|chatgpt)\b', tx))
    chk('F', '%s: sin símbolos ✓ ✗' % nombre, not re.search('[✓✔✗✘✅]', tx))
    chk('F', '%s: sin marcadores sin reemplazar' % nombre, '§§' not in tx and 'TODO' not in tx and 'XXX' not in tx)
    chk('F', '%s: no se declara apto ni aprobado para la venta' % nombre,
        not re.search(r'(?i)\bapto\b|aprobado para (la )?(venta|comercializ)', tx.replace('No está aprobado para la venta', '')))

# ---------------------------------------------------------------- G. maqueta (DOCX)
tw = int(O.Cm(O.ANCHO).twips)
for nombre, d in (('libro', dE), ('guía', dG), ('cuaderno', dC)):
    s = d.sections[0]
    chk('G', '%s: oficio 21,59 × 33,02 cm, márgenes O3 y espejados' % nombre,
        abs(s.page_width.cm - 21.59) < 0.01 and abs(s.page_height.cm - 33.02) < 0.01 and abs(s.left_margin.cm - 2.5) < 0.01
        and abs(s.right_margin.cm - 1.8) < 0.01 and abs(s.top_margin.cm - 1.5) < 0.01 and d.settings.element.find(qn('w:mirrorMargins')) is not None)
    filas = [r for t in d.tables for r in t.rows]
    chk('G', '%s: %d filas de tabla, todas «no dividir»' % (nombre, len(filas)), all(r._tr.trPr is not None and r._tr.trPr.find(qn('w:cantSplit')) is not None for r in filas))
    tablas = [t for t in d.tables if len(t.columns) > 1 or t.rows[0].cells[0].paragraphs[0].runs and
              t.rows[0].cells[0].paragraphs[0].runs[0].font.name == 'Courier New']
    malas = [i for i, t in enumerate(tablas) if abs(sum(int(g.get(qn('w:w'))) for g in t._tbl.tblGrid) - tw) > 15]
    chk('G', '%s: %d tablas de varias columnas y bloques de código al ancho útil' % (nombre, len(tablas)), not malas, malas)
bloques = [t for t in dE.tables if len(t.columns) == 1 and t.rows[0].cells[0].paragraphs[0].runs
           and t.rows[0].cells[0].paragraphs[0].runs[0].font.name == 'Courier New']
chk('G', 'Libro: %d bloques de código, uno por fragmento, en letra monoespaciada de 7,5 pt' % len(bloques),
    len(bloques) == len(F.FRAGMENTOS) and all(r.font.size.pt == 7.5 for t in bloques for p in t.rows[0].cells[0].paragraphs for r in p.runs))
chk('G', 'Se usan la maqueta del lote 1 y el perfil O3 del lote 2 (sin copias)',
    os.path.dirname(O.H.__file__).endswith(os.path.join('lote_1', 'build')) and os.path.dirname(O.__file__).endswith(os.path.join('lote_2', 'build')))


# ---------------------------------------------------------------- H. maqueta (PDF)
def lineas(pg):
    return [l.strip() for l in pg.get_text().split('\n') if l.strip() and not re.match(r'^Página \d+ de \d+$', l.strip())]


for nombre, pdf in (('libro', pE), ('guía', pG), ('cuaderno', pC)):
    vacias = [i + 1 for i, pg in enumerate(pdf) if not lineas(pg)]
    chk('H', '%s: ninguna página en blanco' % nombre, not vacias, vacias)
    sueltos = [i + 1 for i, pg in enumerate(pdf) if lineas(pg) and lineas(pg)[0].startswith('_' * 20)]
    chk('H', '%s: ninguna página empieza con renglones de respuesta sueltos' % nombre, not sueltos, sueltos)
for Cm in CAPS:
    pags = [i + 1 for i, pg in enumerate(pE) if Cm.EVAL_TITULO in lineas(pg)[:2]]
    sig = pags and pags[0] < len(pE) and lineas(pE[pags[0]])
    entra = pags and (pags[0] == len(pE) or (sig and (sig[0].startswith('Capítulo') or sig[0].startswith('Unidad'))))
    chk('H', '%s: en página propia y entera en esa página (pág. %s)' % (Cm.EVAL_TITULO, pags), len(pags) == 1 and entra)
    pp = [i + 1 for i, pg in enumerate(pE) if lineas(pg)[:1] and lineas(pg)[0].startswith(Cm.PRACTICA_TITULO[:25])]
    chk('H', '%s: empieza en página nueva' % Cm.PRACTICA_TITULO.split(' —')[0], len(pp) == 1)
    pc = [i + 1 for i, pg in enumerate(pC) if lineas(pg)[:1] and lineas(pg)[0].startswith(Cm.PRACTICA_TITULO[:25])]
    chk('H', 'Cuaderno: %s empieza en página nueva' % Cm.PRACTICA_TITULO.split(' —')[0], len(pc) == 1)
p26 = [i + 1 for i, pg in enumerate(pE) if lineas(pg)[:1] == [cap13.E26_TITULO]]
chk('H', 'El Encuentro 26 (H4) empieza en página nueva (pág. %s)' % p26, len(p26) == 1)
paginas = res_build['paginas_libro']
chk('H', 'El índice ocupa una sola página y la siguiente es la apertura de la Unidad IV', lineas(pE[2])[0] == B.UNIDAD_IV)
recalc, _ = K.paginas_de_titulos(EST + '.pdf', list(paginas), desde=2)
chk('H', 'Índice estable: las %d entradas apuntan a la página donde está su título' % len(paginas), recalc == paginas and len(paginas) == len(B.entradas_indice()))
chk('H', 'Extensión del libro: %d págs. (plan: 40 a 50)' % len(pE), 40 <= len(pE) <= 50)
chk('H', 'Extensión de la guía: %d págs. (plan: 18 a 24)' % len(pG), 18 <= len(pG) <= 24)
chk('H', 'Extensión del cuaderno: %d págs. (plan: 8 a 12)' % len(pC), 8 <= len(pC) <= 12)
txtpdf = '\n'.join(pg.get_text() for pg in pE)
faltan_cod = [l for f in F.FRAGMENTOS for l in F.extraer(f) if l.strip() and re.sub(r'\s+', ' ', l.strip()) not in re.sub(r'[ \t]+', ' ', txtpdf)]
chk('H', 'Cada línea de código del libro está impresa entera en el PDF, sin cortes ni caracteres perdidos', not faltan_cod, faltan_cod[:3])

# ---------------------------------------------------------------- I. evaluaciones, prácticas e instrumentos
claves = res_build['claves']
semillas_prev = ['ADS3-L1-C1', 'ADS3-L1-C2-i', 'ADS3-L1-C3', 'ADS3-C4v2-2', 'ADS3-L2-C5-c', 'ADS3-L2-C6', 'ADS3-L3-C7', 'ADS3-L3-C8', 'ADS3-L3-C9']
for Cm in CAPS:
    ks = [c for c in claves if c[0] == Cm.EVAL_ID]
    mc = [c[2] for c in ks if c[2] in 'abcd' and len(c[2]) == 1]
    chk('I', '%s: %d ítems con clave; opción múltiple con claves %s' % (Cm.EVAL_TITULO, len(ks), ''.join(mc)), len(ks) == len(Cm.EVAL_ITEMS) and len(set(mc)) >= 3)
    pts = sum(1 for it in Cm.EVAL_ITEMS if it[0] in ('mc', 'vf')) + sum(it[3] for it in Cm.EVAL_ITEMS if it[0] == 'ab')
    chk('I', '%s: suma 15 puntos, como dice su remisión' % Cm.EVAL_TITULO, pts == 15 and 'Puntaje total: 15 puntos' in Cm.EVAL_PUNTAJE)
    chk('I', '%s: la guía trae su clave y los criterios de los ítems abiertos' % Cm.EVAL_TITULO, ('Clave de la %s' % Cm.EVAL_TITULO.lower()) in tG)
    chk('I', 'Capítulo %d: práctica en tres niveles con el caso Mbokaja' % Cm.NUM,
        [n.split(' —')[0] for n, _ in Cm.NIVELES] == ['Nivel 1', 'Nivel 2', 'Nivel 3'] and 'Mbokaja' in j(Cm.PRACTICA_INTRO))
semillas = [Cm.EVAL_ID for Cm in CAPS]
chk('I', 'Semillas de evaluación distintas entre sí y de las de los lotes 1 a 3 (%s)' % ', '.join(semillas), len(set(semillas + semillas_prev)) == 13)
ejemplos = j([getattr(Cm, n) for Cm in CAPS for n in dir(Cm) if n.startswith(('EJ', 'S10', 'S11', 'S12', 'S13', 'TABLA'))])
chk('I', 'Los datos nuevos de las prácticas (M-F10, M-F11, MD, ML, MS-6, MI) no aparecen en los ejemplos resueltos ni en las secciones',
    not re.search(r'\b(?:M-F1[01]|MD-\d\d|ML-\d|MS-6|MI-\d\d)\b', ejemplos))
chk('I', 'Práctica 13: usa datos nuevos (MI-01 a MI-07) y exige comprobar una integración o una incidencia',
    'MI-0' in j(cap13.NIVELES) and 'incidencia' in j(cap13.NIVELES) and 'integración' in cap13.PRACTICA_TITULO)
chk('I', 'Encuentro 26: las 2 HC de evaluación se conservan (P2 V1 E2) y la Práctica 13 queda fuera de ellas',
    '2 de evaluación' in cap13.TIEMPO and '2 de evaluación (H4)' in tG and 'No ocupa tiempo del Encuentro 26' in tG)
rh = cap13.RUBRICA_H4
chk('I', 'Rúbrica del H4: seis criterios que cubren C7, C8 y C9, cuatro niveles, evidencia del equipo e individual',
    len(rh) == 6 and all(len(r[2]) == 4 and r[3] and r[4] for r in rh) and sorted(set(r[1] for r in rh)) == ['C7', 'C8', 'C9']
    and all(('%s (%s)' % (r[0], r[1])) in tG for r in rh))
chk('I', 'H4: 60/40 como propuesta editorial, ausencia de evidencia aparte y pendientes del entorno separados de las fallas',
    '60 %' in tE and '40 %' in tE and 'propuesta editorial' in tE and 'Si falta una evidencia' in tE
    and 'no se confunde con un desempeño de nivel inicial' in tE and 'pendiente del entorno' in tE)
chk('I', 'H4: condiciones mínimas de Work §4.3 que corresponden a la unidad', all(x in tE for x in (
    'circuito de préstamo y devolución ejecutable', 'persistencia comprobada', 'ninguna pérdida de historial',
    'rechazo del préstamo simultáneo del mismo ejemplar', 'evidencia de las pruebas de cada incremento')))
textos_previos = list(R.TEXTO.values()) + list(MB.FUENTES.values()) + [v[1] for v in X.BANCO_H3]
chk('I', 'Banco del H4: cinco variantes que no están en el dossier, el buzón, el banco del H3 ni las prácticas',
    len(C.BANCO_H4) >= 5 and not any(v[1][:30] in t for v in C.BANCO_H4 for t in textos_previos)
    and not any(v[1][:30] in j([Cm.NIVELES, Cm.PRACTICA_INTRO]) for v in C.BANCO_H4 for Cm in CAPS))
chk('I', 'Guía: planilla de registro del H4 con columna AE', 'Planilla de registro del H4' in tG and 'AE' in tG)
chk('I', 'Guía: secuencia en HC de los Encuentros 19 a 26 con las categorías de la v2.1 (19 P3 G2; 20 a 25 D1 P3 V1; 26 P2 V1 E2)',
    all(('Encuentro %d' % n) in tG for n in range(19, 27)) and '(5 HC: 3 de práctica y 2 de gestión)' in tG
    and tG.count('(5 HC: 1 de diseño, 3 de práctica y 1 de verificación)') == 6 and '(5 HC: 2 de práctica, 1 de verificación y 2 de evaluación)' in tG)
chk('I', 'Guía: claves de todas las actividades de los Encuentros 19 a 26',
    all(len(k) == sum(len(items) for _, items in acts) for k, acts in (
        (GU.CLAVES_E19, cap10.ACT_E19), (GU.CLAVES_E20, cap10.ACT_E20), (GU.CLAVES_E21, cap11.ACT_E21), (GU.CLAVES_E22, cap11.ACT_E22),
        (GU.CLAVES_E23, cap12.ACT_E23), (GU.CLAVES_E24, cap12.ACT_E24), (GU.CLAVES_E25, cap13.ACT_E25), (GU.CLAVES_E26, cap13.ACT_E26))))
chk('I', 'Guía: claves por nivel y lista de cotejo de las cuatro prácticas', all(('Lista de cotejo de la Práctica %d' % n) in tG for n in (10, 11, 12, 13)))
chk('I', 'Calendario de 28 encuentros: recuadro en cada capítulo y tabla en la guía (15 = 19+20, 16 = 21+22, 17, 18, 19 = 25+26)',
    tE.count('Si el calendario se acorta') == 4 and 'Unidad IV en 36 y en 28 encuentros' in tG
    and [f[1] for f in GU.CALENDARIO_28[1]] == ['15', '16', '17', '18', '19'])
chk('I', 'Cuaderno: las cuatro prácticas con el mismo texto que el libro y sin evaluaciones',
    all(t in tC for Cm in CAPS for t in [Cm.PRACTICA_TITULO, Cm.PRACTICA_CONTROL] + Cm.PRACTICA_INTRO + [i.split('\n')[0] for _, items in Cm.NIVELES for i in items])
    and not any(Cm.EVAL_TITULO in tC for Cm in CAPS))

# ---------------------------------------------------------------- J. numeración
for Cm in CAPS:
    n = Cm.NUM
    for tipo in ('Tabla', 'Figura', 'Ejemplo resuelto'):
        sec = [int(m.group(1)) for m in re.finditer(r'^%s %d\.(\d+)(?: —|:)' % (tipo, n), tE, re.M)]
        chk('J', 'Capítulo %d: %s %d.1 a %d.%d correlativas, en orden de aparición' % (n, tipo.lower(), n, n, len(sec)),
            sec == list(range(1, len(sec) + 1)) and (len(sec) >= 1 or tipo == 'Figura'), sec)
    for tipo, pat in (('tabla', r'^Tabla %d\.(\d+) —'), ('figura', r'^Figura %d\.(\d+) —'), ('ejemplo resuelto', r'^Ejemplo resuelto %d\.(\d+):'),
                      ('código', r'^Código %d\.(\d+) —')):
        refs = set(int(x) for x in re.findall(r'%s %d\.(\d+)' % (tipo.capitalize(), n), tE + tG + tC))
        defs = set(int(x) for x in re.findall(pat % n, tE, re.M))
        chk('J', 'Capítulo %d: toda %s mencionada existe' % (n, tipo), refs <= defs, refs - defs)
lotes = {}
for ruta in ('lote_1_oficio_candidata/ADS_3BTI_LOTE1_ESTUDIANTE_OFICIO_O3_CANDIDATA.docx', 'lote_2/ADS_3BTI_LOTE2_ESTUDIANTE_OFICIO_O3.docx',
             'lote_3/ADS_3BTI_LOTE3_ESTUDIANTE_OFICIO_O3.docx'):
    lotes[ruta] = texto_docx(os.path.join(ADS, ruta))[1]
otras = sorted(set(re.findall(r'\b(?:Tabla|Figura) [1-9]\.\d+', tE + tG + tC)))
chk('J', 'Las tablas y figuras de los lotes 1 a 3 que se citan existen allí (%s)' % ', '.join(otras),
    all(re.search(r'^%s —' % re.escape(o), '\n'.join(lotes.values()), re.M) for o in otras),
    [o for o in otras if not re.search(r'^%s —' % re.escape(o), '\n'.join(lotes.values()), re.M)])

# ---------------------------------------------------------------- L. notaciones
reg = json.load(open(os.path.join(AQUI, 'figs', 'simbolos.json'), encoding='utf8'))
u = reg['fig_10_2']['simbolos']
chk('L', 'Figura 10.2 usa solo la notación de capas de la Tabla 9.1 (%s)' % ', '.join(sorted(u)),
    reg['fig_10_2']['notacion'] == 'capas' and u and all(G.SIMBOLOS[s][0] == 'capas' for s in u))
for f in ('fig_10_1', 'fig_12_1', 'fig_13_1'):
    chk('L', '%s (esquema didáctico) no usa símbolos de ninguna notación' % f, reg[f]['notacion'] == 'esquema' and not reg[f]['simbolos'])
chk('L', 'Guía: leyenda de la notación de capas con los símbolos que usa la Figura 10.2', all(G.SIMBOLOS[s][1] in tG for s in u))

# ---------------------------------------------------------------- W. Práctica 11 reproducible (v1.1, cierre de auditoría)
chk('W', 'La Práctica 11 ya no supone un sistema adaptado a MB-: se carga en una copia de práctica con correspondencia fija',
    'ya acepta las etiquetas MB-' not in tE + tC and 'copia de práctica' in j(cap11.PRACTICA_INTRO) and 'correspondencia fija' in j(cap11.PRACTICA_INTRO))
chk('W', 'Libro y cuaderno: tabla de correspondencia y tabla de qué se ejecuta y qué se resuelve en papel',
    all(t in x for t in (MB.CORRESPONDENCIA_TITULO, MB.EJECUCION_TITULO) for x in (tE, tC)) and all(c[1] in tC for c in MB.CORRESPONDENCIA))
sec = json.load(open(os.path.join(L4, 'practica_11', 'secuencia.json'), encoding='utf8'))
chk('W', 'practica_11/secuencia.json sale de caso/mbokaja_u4.py (PASOS_P11 y CONSULTAS_P11)',
    sec == {'pasos': [list(x) for x in MB.PASOS_P11], 'consultas': [list(c) for c in MB.CONSULTAS_P11]})
chk('W', 'La secuencia se comprobó sin fallos en una base temporal: %s' % res['practica_11']['resultado'],
    res['practica_11']['ok'] and 'Entorno' in leer(L4, 'resultados_pruebas', 'practica_11_mbokaja.txt'))
chk('W', 'Cada paso usa solo códigos que la base entregada acepta o rechaza con su mensaje (EJ-, OB-, ED-, LE- o el formato inválido MB205)',
    all(all(re.match(r'^(EJ|OB|ED|LE)-\d{4}$', x) or not re.match(r'^[A-Z]{2}-?\d', x) or x == 'MB205' for x in p_[3]) for p_ in MB.PASOS_P11))
diff_p = subprocess.run(['git', 'diff', '--stat', '10c877a', '--', 'lote_4/proyecto'], cwd=ADS, capture_output=True, text=True).stdout.strip()
chk('W', 'La base Arapoty (referencia docente y base del estudiante) no cambió desde la v1.0 (10c877a)', not diff_p, diff_p[:200])
chk('W', 'La guía trae la secuencia comprobada, con el mensaje esperado de cada paso', 'Práctica 11: secuencia comprobada del nivel 2' in tG
    and all(('%s' % x[4]) in tG for x in MB.PASOS_P11))
chk('W', 'El nivel 3 de la Práctica 11 se resuelve en papel y lo dice', 'en papel' in cap11.NIVELES[2][0] and 'no se programa' in j(cap11.NIVELES[2]))
chk('W', 'Las Prácticas 10, 12 y 13 dicen qué se ejecuta y qué se resuelve en papel; la 13 rotula sus datos como simulados',
    'copia de práctica' in j(cap10.PRACTICA_INTRO) and 'en papel' in j(cap12.PRACTICA_INTRO) and 'datos simulados' in j(cap13.PRACTICA_INTRO))
m10 = json.load(open(os.path.join(L4, 'version_1_0', 'MANIFIESTO_LOTE_4.json'), encoding='utf8'))
d10 = [x for x in m10['archivos'] if x['ruta'].startswith('ADS_3BTI_LOTE4_')]
chk('W', 'Versión 1.0 conservada: los seis DOCX y PDF de version_1_0/ coinciden con su manifiesto SHA-256',
    len(d10) == 6 and all(hashlib.sha256(open(os.path.join(L4, 'version_1_0', x['ruta']), 'rb').read()).hexdigest() == x['sha256'] for x in d10))
chk('W', 'Versión 1.1 en la portada de los tres documentos', all('v1.1 (lote 4, cierre de auditoría)' in t for t in (tE, tG, tC)))

# ---------------------------------------------------------------- Q. lotes 1 a 3 intactos
st = subprocess.run(['git', 'status', '--porcelain', '--', 'lote_1', 'lote_2', 'lote_3', 'lote_1_oficio_candidata'], cwd=ADS,
                    capture_output=True, text=True).stdout.strip()
chk('Q', 'git: ningún archivo de los lotes 1, 2 y 3 cambió ni se agregó', not st, st[:300])
m3 = json.load(open(os.path.join(ADS, 'lote_3', 'MANIFIESTO_LOTE_3.json'), encoding='utf8'))
docs3 = [a for a in m3['archivos'] if a['ruta'].startswith('ADS_3BTI_LOTE3_')]
chk('Q', 'Lote 3 v1.1: sus seis DOCX y PDF coinciden con su manifiesto SHA-256',
    len(docs3) == 6 and all(hashlib.sha256(open(os.path.join(ADS, 'lote_3', a['ruta']), 'rb').read()).hexdigest() == a['sha256'] for a in docs3))

print('\nResultado por bloque:')
for b, (o_, f_) in RES.items():
    print('  %s: %d correctos, %d fallos' % (b, o_, f_))
print('Resultado: %d correctos, %d fallos' % (ok, fallos))
json.dump({'correctos': ok, 'fallos': fallos, 'bloques': RES, 'controles': DETALLE},
          open(os.path.join(L4, 'verificacion_resultado.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
sys.exit(1 if fallos else 0)

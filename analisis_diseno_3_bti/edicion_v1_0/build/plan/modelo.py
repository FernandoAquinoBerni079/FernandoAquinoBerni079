# -*- coding: utf-8 -*-
"""Modelo único de la planificación: arma, para cada uno de los 36 encuentros, todo lo que usan el plan anual y los
planes de clase. Las fuentes son tres, y ninguna se modifica:
- datos_coleccion.json: libro, guía y cuaderno aprobados (v0.2, commit 88c5cb5), leídos por extraer_coleccion.py;
- plan_anual/plan_anual_preliminar.py y su CSV: transcripción del informe de Work v0.1 (foco, evidencia y capacidades
  de cada encuentro, competencia y capacidades C1 a C10, HC por categoría);
- encuadre.py: citas del MEC y decisiones institucionales pendientes.

Las únicas decisiones de esta planificación están declaradas abajo:
- INDICADORES_POR_ENCUENTRO: qué indicadores de la ficha de cada capítulo se evidencian en cada encuentro (2 a 4);
- APERTURAS: en los 7 encuentros cuyo primer tramo de la guía dura más de 1,5 HC, el inicio toma 0,5 HC de ese tramo
  para organizar la sesión. La suma del tramo no cambia.
Todo lo demás (tramos, tiempos, actividades, evidencias, instrumentos, páginas) se copia de las fuentes.
"""
import csv, importlib.util, json, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(os.path.dirname(os.path.dirname(AQUI)))
D = json.load(open(os.path.join(AQUI, 'datos_coleccion.json'), encoding='utf8'))

_spec = importlib.util.spec_from_file_location('work_pa', os.path.join(ADS, 'plan_anual', 'plan_anual_preliminar.py'))
W = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(W)
FILAS_WORK = {int(f['encuentro']): f for f in csv.DictReader(open(os.path.join(ADS, 'plan_anual', 'plan_anual_preliminar.csv'), encoding='utf-8'))}
CATS = [('A', 'análisis'), ('D', 'diseño'), ('P', 'programación'), ('V', 'verificación y validación'),
        ('Doc', 'documentación de entrega'), ('G', 'gestión del proyecto'), ('E', 'evaluación')]
ROMANOS = ['I', 'II', 'III', 'IV', 'V', 'VI']
HITOS = {6: 'H1', 12: 'H2', 18: 'H3', 26: 'H4', 32: 'H5', 34: 'H6'}
ROTULO = ('Capacidades propuestas para el programa institucional del Plan Optativo. No son capacidades oficiales del MEC.')
norm = lambda s: re.sub(r'\s+', ' ', s or '').strip()

# ---------------------------------------------------------------- decisiones de esta planificación
# Índices (desde 1) de los indicadores de la ficha del capítulo que se evidencian en cada encuentro.
INDICADORES_POR_ENCUENTRO = {
    1: [1, 2, 5], 2: [3, 4, 5],          # Cap. 1: 1.1-1.2 y diagnóstico | 1.3-1.4 y Práctica 1
    3: [1, 2, 5], 4: [3, 4, 5],          # Cap. 2: guion y resguardo | contraste, registro y Práctica 2
    5: [1, 2, 3], 6: [3, 4, 5],          # Cap. 3: objetivos, alternativas, riesgos | acuerdo y H1
    7: [1, 2], 8: [3, 4, 5],             # Cap. 4
    9: [1, 2], 10: [3, 4, 5],            # Cap. 5
    11: [1, 2, 3], 12: [4, 5],           # Cap. 6: prioridad, trazabilidad, incrementos | cambio y H2
    13: [1, 2], 14: [3, 4, 5],           # Cap. 7
    15: [1, 2], 16: [3, 4, 5],           # Cap. 8
    17: [1, 2, 3, 4], 18: [4, 5],        # Cap. 9: las cuatro secciones | H3
    19: [1, 2, 3], 20: [4, 5],           # Cap. 10
    21: [1, 2, 3], 22: [3, 4, 5],        # Cap. 11: el alta de obras y ediciones (E21) y de lectores (E22)
    23: [1, 2, 3], 24: [4, 5],           # Cap. 12
    25: [1, 2, 3], 26: [4, 5],           # Cap. 13: consultas e informe | integración y H4
    27: [1, 2, 3], 28: [4, 5],           # Cap. 14
    29: [1, 2, 3], 30: [4, 5],           # Cap. 15
    31: [1, 2, 3, 4], 32: [4, 5],        # Cap. 16: diagnóstico, impacto, corrección, actualización | H5
    33: [1, 2], 34: [3, 4, 5],           # Cap. 17
    35: [1, 2, 3], 36: [2, 3, 4, 5],     # Cap. 18: demostración y defensa | recuperación y retrospectiva
}
# Inicio de 0,5 HC tomado del primer tramo de la guía cuando ese tramo dura más de 1,5 HC.
APERTURAS = {
    18: 'Organización de la defensa: orden de presentación de los equipos, criterios de la rúbrica del H3 y planilla de '
        'registro. Mientras un equipo defiende, los demás repasan su dossier.',
    19: 'Apertura del capítulo y aviso de entorno (recuadro «Estado del entorno» del libro): qué está comprobado y qué no.',
    26: 'Propósito de la sesión: integrar los módulos, demostrar el incremento y revisar la Unidad IV con el H4. Se '
        'presenta la sección 13.3 y el orden de las demostraciones.',
    30: 'Preparación de las sesiones de uso: sección 15.3, roles de cada equipo, tareas nuevas impresas y la Tabla 15.3 '
        'para registrar lo que la persona hace.',
    32: 'Sección 16.4 y Tabla 16.7: cada equipo identifica qué condición mínima le falta antes de empezar la recuperación.',
    34: 'Organización de la instalación por otro equipo: parejas de equipos (guía, Parte VI, sección 0.3), reglas de la '
        'instalación sin ayuda y acta de la Tabla 17.5.',
    36: 'Organización: defensas que pasan del Encuentro 35 (alternativa B) y orden de las recuperaciones por prioridad.',
}
APERTURA_HC = 0.5
PRELIMINARES_USADOS = ('Acuerdo de trabajo', 'Diagnóstico de entrada', 'Presentación del caso')


# ---------------------------------------------------------------- utilidades
def hc_de(tiempo):
    m = re.search(r'(\d+(?:,\d+)?) HC', tiempo)
    return float(m.group(1).replace(',', '.')) if m else None


def fmt_hc(x):
    if x is None:
        return None
    s = ('%.2f' % x).rstrip('0').rstrip('.').replace('.', ',')
    return '%s HC' % s


def lista_numeros(texto):
    """«1 a 3» → [1,2,3]; «1, 2 y 5» → [1,2,5]; «1 (a) a (c) y 2» → [1,2]."""
    t = re.sub(r'\([a-z]\)( a \([a-z]\))?', '', texto)
    nums = []
    for parte in re.split(r',| y ', t):
        parte = parte.strip()
        m = re.match(r'(\d+) a (\d+)', parte)
        if m:
            nums += list(range(int(m.group(1)), int(m.group(2)) + 1))
        elif re.match(r'\d+$', parte):
            nums.append(int(parte))
    return nums


REF_ACT = re.compile(r'Actividad(?:es)? ((?:\d+(?: \([a-z]\))?(?: a \([a-z]\))?(?:, | y | a )?)+)(?: del Encuentro (\d+))?')


def referencias_actividades(texto, enc):
    """[(encuentro, número, es_tarea)] citadas en un texto de la guía."""
    salida = []
    for oracion in re.split(r'(?<=\.) ', texto):
        tarea = bool(ES_TAREA.search(oracion))
        if re.search(r'Actividades[;.]', oracion):
            salida += [(enc, a['num'], tarea) for a in LIBRO_ENC[enc]['actividades']]
        anterior = oracion.startswith('Corrección de la Actividad')   # la tarea que dejó el encuentro anterior
        for m in REF_ACT.finditer(oracion):
            n_enc = int(m.group(2)) if m.group(2) else (enc - 1 if anterior else enc)
            for n in lista_numeros(m.group(1)):
                salida.append((n_enc, n, tarea))
        if 'Desafío' in oracion:
            salida.append((enc, 'Desafío', tarea))
    return salida


ES_TAREA = re.compile(r'como tarea')


def oraciones_tarea(texto):
    return [o for o in re.split(r'(?<=\.) ', texto) if ES_TAREA.search(o)]


# ---------------------------------------------------------------- datos por encuentro
CAPS = {c['num']: c for c in D['libro']['capitulos']}
ENC_CAP = {e['num']: c['num'] for c in D['libro']['capitulos'] for e in c['encuentros']}
LIBRO_ENC = {e['num']: e for c in D['libro']['capitulos'] for e in c['encuentros']}
SEC = {s['num']: s for s in D['guia']['secuencias']}
TAB = D['guia']['tablas']
INSTR = D['guia']['instrumentos']
CUAD = {t: p for t, p in D['cuaderno']['indice']}
IND_GUIA = {t: p for t, p in D['guia']['indice']}


def unidad_de(e):
    n = next(i for i, (a, b) in enumerate([W.UNIDADES[r][1] for r in ROMANOS]) if a <= e <= b)
    return ROMANOS[n], W.UNIDADES[ROMANOS[n]][0], next(u['pagina'] for u in D['libro']['unidades'] if u['num'] == n + 1)


def instrumento(nombre_empieza):
    for t, parte, p in INSTR:
        if t.startswith(nombre_empieza):
            return {'nombre': t, 'parte': parte, 'pagina': p}
    return None


def pagina_guia_capitulo(c):
    t = next(t for t, _ in D['guia']['indice'] if re.match(r'\d+\. Capítulo %d — ' % c, t))
    return t, IND_GUIA[t]


def practicas_citadas(texto):
    return sorted({int(m) for m in re.findall(r'Práctica (\d+)', texto)})


# Computadoras que necesita cada encuentro según su secuencia en la guía (Unidades I a III: ninguna).
COMPUTADORAS = {n: 'equipo' for n in range(19, 35)}
COMPUTADORAS.update({35: 'demostracion', 36: 'recuperacion'})


def encuentro(n):
    cnum = ENC_CAP[n]; cap = CAPS[cnum]; L = LIBRO_ENC[n]; S = SEC[n]; F = FILAS_WORK[n]
    rom, titulo_u, pag_u = unidad_de(n)
    ficha = cap['ficha']
    primero = cap['encuentros'][0]['num'] == n
    ultimo = cap['encuentros'][-1]['num'] == n

    # tramos de la guía: los del encuentro y los complementos fuera de las 5 HC
    tramos = [dict(t, hc=hc_de(t['tiempo'])) for t in S['momentos']]
    fuera = [t for t in tramos if t['momento'].startswith('Complemento')]
    dentro = [t for t in tramos if not t['momento'].startswith('Complemento')]
    planilla = all(t['hc'] is None for t in dentro)
    # inicio, desarrollo y cierre
    if n in APERTURAS:
        assert dentro[0]['hc'] > 1.5
        inicio = {'hc': APERTURA_HC, 'tramos': [], 'apertura': APERTURAS[n], 'desde': dentro[0]['momento']}
        resto = dict(dentro[0], hc=dentro[0]['hc'] - APERTURA_HC, parcial=True)
        medio = [resto] + dentro[1:-1]
    else:
        assert planilla or dentro[0]['hc'] <= 1.5, n
        inicio = {'hc': dentro[0]['hc'], 'tramos': [dentro[0]], 'apertura': None}
        medio = dentro[1:-1]
    cierre = {'hc': dentro[-1]['hc'], 'tramos': [dentro[-1]]}
    desarrollo = {'hc': None if planilla else sum(t['hc'] for t in medio), 'tramos': medio}
    if n == 35:   # dos tramos «según la planilla»: el inicio y el cierre son la organización y el registro, dentro de ella
        inicio = {'hc': None, 'tramos': [], 'apertura': 'Organización: orden de las demostraciones y de las defensas '
                  'calculado con la planilla de tiempos (guía, Parte VI, sección 0.6), guiones revisados en el Encuentro 34 '
                  'y variantes impresas del banco reservado, una por estudiante.', 'desde': dentro[0]['momento']}
        desarrollo = {'hc': None, 'tramos': dentro}
        cierre = {'hc': None, 'tramos': [], 'cierre_planilla': 'Registro en la planilla de defensa individual y en la '
                  'planilla anual H1 a H6. Si la planilla de tiempos indicó la alternativa B, se anuncia qué defensas pasan '
                  'al comienzo del Encuentro 36. Se retiran las variantes impresas.'}
    total = None if planilla else inicio['hc'] + desarrollo['hc'] + cierre['hc']

    # actividades del libro citadas por la guía
    texto_guia = ' '.join(t['que_se_hace'] for t in dentro)
    refs = referencias_actividades(texto_guia, n)
    acts_libro = {a['num']: a for a in L['actividades']}
    desafio = next((a for a in L['actividades'] if a['tipo'] == 'Desafío'), None)

    def act(ref_enc, num):
        if num == 'Desafío':
            return desafio and dict(desafio, encuentro=n)
        A = {a['num']: a for a in LIBRO_ENC[ref_enc]['actividades']}
        return A.get(num) and dict(A[num], encuentro=ref_enc)
    en_clase, tarea = [], []
    for ref_enc, num, es_tarea in refs:
        a = act(ref_enc, num)
        if a is None:
            continue
        destino = tarea if es_tarea else en_clase
        if not any(x['encuentro'] == a['encuentro'] and x['num'] == a['num'] for x in destino):
            destino.append(a)
    for a in en_clase:   # una actividad puede empezar en clase y terminar como tarea (por ejemplo, la 1 (d) del Encuentro 8)
        a['sigue_como_tarea'] = any(t['encuentro'] == a['encuentro'] and t['num'] == a['num'] for t in tarea)
    tarea_texto = [o for t in dentro for o in oraciones_tarea(t['que_se_hace'])]
    citadas = {(a['encuentro'], a['num']) for a in en_clase + tarea}

    # prácticas
    pract_en = practicas_citadas(texto_guia + ' ' + ' '.join(t['momento'] for t in dentro))
    pract_fuera = practicas_citadas(' '.join(t['que_se_hace'] for t in fuera))
    practica = None
    if cap['practica']:
        pn = int(re.match(r'Práctica (\d+)', cap['practica']['titulo']).group(1))
        if pn in pract_en or pn in pract_fuera:
            cuad = next((p for t, p in CUAD.items() if t.startswith('Práctica %d —' % pn)), None)
            cot = TAB['cotejo'].get(str(pn))
            practica = {'num': pn, 'titulo': cap['practica']['titulo'], 'libro': (cap['practica']['pagina'], cap['practica']['pagina_fin']),
                        'cuaderno': cuad, 'cotejo': cot, 'complemento': pn in pract_fuera and pn not in pract_en,
                        'niveles': cap['practica']['niveles']}

    # páginas del libro que usa el encuentro
    paginas = [(L['pagina'], max(L['pagina_fin'], L.get('pagina_actividades') or 0))]
    prelim = []
    if 'preliminares' in texto_guia:   # Encuentro 1: acuerdo de trabajo, diagnóstico de entrada y presentación del caso
        prelim = [x for x in D['libro']['preliminares'] if x['titulo'] in PRELIMINARES_USADOS]
        paginas.insert(0, (min(x['pagina'] for x in prelim), max(x['pagina'] for x in prelim)))
    if practica:
        paginas.append(practica['libro'])
    hito = HITOS.get(n)
    if cap['hito'] and cap['hito']['encuentro'] == n:
        paginas.append((cap['hito']['pagina'], cap['hito']['pagina']))

    # recursos del libro
    recursos_libro = [{'tipo': 'preliminares', 'texto': x['titulo'], 'pagina': x['pagina']} for x in prelim]
    for clave, nombre in (('secciones', None), ('tablas', None), ('figuras', None), ('codigos', None), ('ejemplos', None), ('otros', None)):
        for x in L[clave]:
            recursos_libro.append({'tipo': clave, 'texto': x.get('titulo') if clave in ('secciones', 'ejemplos', 'otros')
                                   else '%s — %s' % (x['id'], x['titulo']), 'pagina': x['pagina']})
    # computadoras
    requiere = COMPUTADORAS.get(n)
    pruebas = sorted(set(re.findall(r'\b(?:PA?|E)-\d+[ab]?\b', texto_guia)), key=lambda s: (s[0], int(re.sub(r'\D', '', s))))
    comandos = sorted(set(re.findall(r'(?:php|bash) [\w/.]+', texto_guia)))

    # evaluación
    instrumentos = []
    k = TAB['claves_encuentro'][str(n)]
    instrumentos.append({'nombre': 'Claves de las actividades del Encuentro %d (respuesta esperada y error frecuente)' % n, 'pagina': k['pagina']})
    if n == 1:
        instrumentos[0:0] = [dict(instrumento('Claves del diagnóstico de entrada')),
                             {'nombre': 'Mapa de apoyos del curso (modelo)', 'parte': 'I',
                              'pagina': D['guia']['referencias']['mapa_apoyos']['pagina']}]
    if practica and practica['cotejo']:
        instrumentos.append({'nombre': 'Lista de cotejo de la Práctica %d' % practica['num'], 'pagina': practica['cotejo']['pagina']})
    if hito:
        h = hito[1]
        for pref in ('Rúbrica del %s' % hito, 'Planilla de registro del %s' % hito):
            i = instrumento(pref)
            instrumentos.append({'nombre': i['nombre'], 'pagina': i['pagina']})
        ev = TAB['evidencias_hito'][h]
        instrumentos.append({'nombre': 'Evidencias de cada criterio del %s (60 %% equipo, 40 %% individual)' % hito, 'pagina': ev['pagina']})
    if n == 35:
        for pref in ('Planilla de tiempos', 'Rúbrica de producto final', 'Planilla de defensa individual'):
            i = instrumento(pref); instrumentos.append({'nombre': i['nombre'], 'pagina': i['pagina']})
    if n == 36:
        for pref in ('Fichas de recuperación', 'Registro de recuperaciones'):
            i = instrumento(pref); instrumentos.append({'nombre': i['nombre'], 'pagina': i['pagina']})
    procedimientos = []
    if n == 1:
        procedimientos.append('Diagnóstico de entrada, individual y sin nota, con autoevaluación por área.')
    if hito:
        procedimientos.append('Revisión del hito %s: presentación del equipo con su evidencia, revisión con la rúbrica y '
                              'evidencia individual de cada integrante (pregunta, variante o reporte del banco).' % hito)
    if n == 35:
        procedimientos.append('Demostración por equipo con guion y tiempo fijo; defensa individual (una decisión, una prueba '
                              'y una variante del banco reservado).')
    if n == 36:
        procedimientos.append('Defensas pendientes (alternativa B) y recuperación por fichas, según prioridad.')
    if practica and not practica['complemento']:
        procedimientos.append('Revisión de la Práctica %d con su lista de cotejo, en el nivel asignado.' % practica['num'])
    elif practica:
        procedimientos.append('Si se asigna la Práctica %d (complemento, fuera de las 5 HC), se revisa con su lista de cotejo.'
                              % practica['num'])
    procedimientos.append('Observación del trabajo durante la práctica y revisión de las actividades con sus claves.')
    if ultimo and cap['evaluacion']:
        procedimientos.append('Evaluación escrita opcional del capítulo (15 puntos). No ocupa tiempo de este encuentro: si la '
                              'institución la aplica, define cuándo.')
    indicadores = [(i, ficha['indicadores'][i - 1]) for i in INDICADORES_POR_ENCUENTRO[n]]

    # vinculación
    t_guia, p_guia = pagina_guia_capitulo(cnum)
    prox_hito = next((h for e, h in sorted(HITOS.items()) if e >= n), None)
    e_hito = next((e for e, h in HITOS.items() if h == prox_hito), None)

    return {
        'num': n, 'unidad': {'rom': rom, 'titulo': titulo_u, 'pagina': pag_u},
        'capitulo': {'num': cnum, 'titulo': cap['titulo'], 'pagina': cap['pagina'], 'primero': primero, 'ultimo': ultimo},
        'titulo': L['titulo'], 'foco': F['foco_work'], 'evidencia': F['evidencia_work'], 'capacidades_enc': F['capacidades_encuentro'],
        'hc_guia': S['hc'], 'hc_cat': {c: int(F['hc_' + c]) for c, _ in CATS},
        'ficha': ficha, 'indicadores': indicadores,
        'secciones': L['secciones'], 'conceptos': L['conceptos'], 'ejemplos': L['ejemplos'],
        'paginas_libro': paginas, 'pagina_actividades': L.get('pagina_actividades'),
        'momentos': {'inicio': inicio, 'desarrollo': desarrollo, 'cierre': cierre}, 'fuera': fuera, 'planilla': planilla,
        'total_hc': total, 'tramos_guia': dentro,
        'actividades_clase': en_clase, 'actividades_tarea': tarea, 'tarea_texto': tarea_texto, 'citadas': citadas,
        'practica': practica, 'hito': hito, 'hito_libro': cap['hito'] if cap['hito'] and cap['hito']['encuentro'] == n else None,
        'recursos_libro': recursos_libro, 'requiere_computadoras': requiere, 'pruebas': pruebas, 'comandos': comandos,
        'procedimientos': procedimientos, 'instrumentos': instrumentos,
        'errores': [(f[0], f[2]) for f in k['filas'] if len(f) > 2 and f[2]],
        'guia': {'parte': S['parte'], 'secuencia_pagina': S['pagina'], 'capitulo': t_guia, 'capitulo_pagina': p_guia,
                 'claves_pagina': k['pagina'], 'rotulo': S['rotulo']},
        'proximo_hito': (prox_hito, e_hito),
        'repaso': (cap['repaso'], cap.get('pagina_repaso')) if ultimo else None,
        'calendario': (cap['calendario'], cap.get('pagina_calendario')) if ultimo else None,
        'evaluacion_capitulo': cap['evaluacion'] if ultimo else None,
        'antecedentes': F['antecedentes_mec'],
    }


ENCUENTROS = [encuentro(n) for n in range(1, 37)]
# actividades del libro que ninguna secuencia de la guía cita (ni en su encuentro ni en otro)
_todas = set().union(*[e['citadas'] for e in ENCUENTROS])
for _e in ENCUENTROS:
    _e['actividades_no_citadas'] = [dict(a, encuentro=_e['num']) for a in LIBRO_ENC[_e['num']]['actividades']
                                    if (_e['num'], a['num']) not in _todas]

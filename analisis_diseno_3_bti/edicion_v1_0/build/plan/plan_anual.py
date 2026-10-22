# -*- coding: utf-8 -*-
"""Plan anual de Análisis y Diseño de Sistemas, 3.º BTI (36 encuentros, 180 HC), en oficio O3: DOCX editable y PDF de
control. Todo el contenido sale de modelo.py (colección v0.2 aprobada e informe de Work) y de encuadre.py (citas del MEC).
Uso: python3 -B planificacion/build/plan_anual.py
"""
import os, sys
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import modelo as MO
import encuadre as EN
import maqueta_plan as MP
from docx.shared import Pt

PLAN = os.path.join(os.path.dirname(os.path.dirname(AQUI)), 'salida')
NOMBRE = 'ADS_3BTI_PLAN_ANUAL_v1_0'
VERSION = 'Edición comercial v1.0'
ESTADO = ('**Edición comercial v1.0.** Plan anual para 5 horas cátedra semanales: 36 encuentros y 180 HC, con la secuencia '
          'del libro del estudiante, la guía docente y el cuaderno de prácticas de la misma colección. Es una propuesta para '
          'el programa institucional del Plan Optativo: la institución la adopta en su PCI y completa los datos de la '
          'sección 1.3. No constituye un programa oficial aprobado por el MEC.')
E = MO.ENCUENTROS
L = MO.D['libro']; G = MO.D['guia']
REF = {k: v['pagina'] for k, v in G['referencias'].items()}
import json
PAG_PLANES = json.load(open(os.path.join(AQUI, 'paginas_planes.json'))) if os.path.exists(os.path.join(AQUI, 'paginas_planes.json')) else {}


def pags(rangos):
    out = []
    for a, b in rangos:
        s = str(a) if a == b else '%d-%d' % (a, b)
        if s not in out: out.append(s)
    return ', '.join(out)


def etapa(n):
    return 'Primera' if n <= 18 else 'Segunda'


def construir():
    d = MP.documento()
    MP.F.identificacion(d, 'PLAN ANUAL')
    MP.parrafo(d, VERSION + ' · 36 encuentros de 5 HC (180 HC) · Plan Optativo', 9.5, centro=True, antes=4)
    MP.recuadro(d, 'Sobre esta edición', [ESTADO])

    # ------------------------------------------------------------ 1. encuadre
    MP.titulo(d, '1. Encuadre curricular e institucional')
    MP.parrafo(d, 'El plan distingue tres niveles. Solo el primero es una disposición oficial del MEC; el segundo es la '
                  'propuesta editorial de la colección, y el tercero lo decide la institución.')
    MP.titulo(d, '1.1 Disposiciones oficiales del MEC', 2)
    MP.parrafo(d, 'Fuente: %s. Copia identificada: %d páginas, %s bytes, SHA-256 %s…%s (la misma que usó el informe de '
                  'Work). Las citas son textuales y se comprobaron en la página indicada.' % (
                      EN.MEC['titulo'], EN.MEC['paginas'], f"{EN.MEC['bytes']:,}".replace(',', '.'), EN.MEC['sha256'][:12],
                      EN.MEC['sha256'][-8:]), 9)
    MP.tabla(d, ['Pág.', 'Cita textual', 'Qué se toma para este plan'],
             [[str(p), '«%s»' % c, q] for p, c, q in EN.CITAS_MEC], [1.1, 9.6, MP.UTIL - 10.7])
    MP.parrafo(d, '**El documento no establece** (se revisaron sus 111 páginas):', 9.5, antes=4, seguir=True)
    MP.lista(d, EN.NO_ESTABLECE, 9.5)
    MP.titulo(d, '1.2 Propuesta editorial de la colección', 2)
    MP.parrafo(d, 'Estos elementos son decisiones editoriales del informe de Work v0.1, desarrolladas en la colección. '
                  'No son programa ni capacidades oficiales del MEC; la institución puede adoptarlos o adaptarlos en su PCI. '
                  'En este plan, «Work» designa ese informe de diagnóstico y propuesta curricular (v0.1, 14 de octubre de 2026).', 9.5)
    MP.tabla(d, ['Elemento', 'Propuesta', 'Fuente'], [list(x) for x in EN.PROPUESTA_EDITORIAL], [3.6, 9.4, MP.UTIL - 13.0])
    MP.titulo(d, '1.3 Datos que completa la institución al adoptar el plan', 2)
    MP.parrafo(d, 'La carga horaria está confirmada: 5 HC semanales, 36 encuentros y 180 HC. Los demás datos dependen de cada '
                  'institución: este plan no fija fechas, minutos ni períodos de calificación. Los campos de la derecha se '
                  'completan en la institución.', 9.5)
    t = MP.tabla(d, ['Dato', 'Qué se define', 'Registro de la institución'],
                 [[a, b, ''] for a, b in EN.INSTITUCIONAL], [3.6, 9.0, MP.UTIL - 12.6])
    for (a, _), row in zip(EN.INSTITUCIONAL, t.rows[1:]):
        if a == 'Carga horaria':
            MP.celda(row.cells[2], 'Confirmada: 5 HC semanales', 8.5)
        else:
            MP.campo(row.cells[2].paragraphs[0], 'fecha y responsable')

    # ------------------------------------------------------------ 2. competencia y capacidades
    MP.titulo(d, '2. Competencia y capacidades propuestas', nueva_pagina=True)
    MP.parrafo(d, MO.ROTULO + ' Fuente: informe de Work v0.1, §4.1 y §4.2; libro, «Mapa de capacidades y evidencias» (pág. %d).'
               % next(p['pagina'] for p in L['preliminares'] if p['titulo'].startswith('Mapa de capacidades')), 9, italica=True)
    MP.parrafo(d, '**Competencia general propuesta.** ' + MO.W.COMPETENCIA, 10, antes=3)
    MP.tabla(d, ['Cód.', 'Capacidad propuesta', 'Contenidos esenciales', 'Indicadores observables y evidencia', 'Criterio de evaluación'],
             [[k, v[0], v[1], v[2], v[3]] for k, v in MO.W.CAPACIDADES.items()], [1.0, 3.2, 3.8, 5.3, MP.UTIL - 13.3], tam=8)
    MP.parrafo(d, 'Los indicadores de logro de cada capítulo (sección 6) son los de la ficha del libro, sin cambios.', 9, antes=3)

    # ------------------------------------------------------------ 3. organización anual
    MP.titulo(d, '3. Organización anual y distribución del tiempo', nueva_pagina=True)
    filas = []
    for r in MO.ROMANOS:
        tit, (a, b), hc, res = MO.W.UNIDADES[r]
        caps = sorted({e['capitulo']['num'] for e in E if a <= e['num'] <= b})
        hitos = [MO.HITOS[n] + ' (E%d)' % n for n in MO.HITOS if a <= n <= b]
        filas.append(['%s. %s' % (r, tit), '%d a %d' % (a, b), str(hc), '%d a %d' % (caps[0], caps[-1]),
                      res, ', '.join(hitos) or '—', etapa(a)])
    filas.append(['Total', '36', '180', '18', '', 'H1 a H6', ''])
    MP.tabla(d, ['Unidad', 'Encuentros', 'HC', 'Capítulos', 'Resultado de la unidad (Work §5.1)', 'Hitos', 'Etapa'],
             filas, [4.2, 1.7, 1.0, 1.6, 4.9, 2.2, MP.UTIL - 15.6])
    MP.parrafo(d, '**Etapas.** La colección organiza el año en dos etapas, cada una con su evaluación integradora: la '
                  'primera cierra en el Encuentro 18 (hito H3) y la segunda en el Encuentro 36. No son períodos '
                  'institucionales de calificación: la institución los hace coincidir con su calendario.', 9.5, antes=4)
    MP.parrafo(d, '**Distribución del tiempo.** Cada encuentro tiene 5 HC, que pueden repartirse en varios bloques '
                  'semanales. El Anexo A detalla las HC de cada encuentro por categoría (distribución v2.1) y deja una '
                  'columna para la semana o fecha que fije la institución. Totales del año: ' +
               ', '.join('%s %d HC' % (nom, sum(e['hc_cat'][c] for e in E)) for c, nom in MO.CATS) + '.', 9.5)
    MP.parrafo(d, '**Adaptación a 28 encuentros.** Es una alternativa para un año con menos semanas efectivas y no '
                  'reemplaza a la secuencia ordinaria. Cada parte de la guía trae su tabla «Unidad … en 36 y en 28 '
                  'encuentros» (guía, págs. %s) y cada capítulo del libro, su recuadro «Si el calendario se acorta». Este '
                  'plan desarrolla la secuencia ordinaria de 36.' % ', '.join(
                      str(p) for t, _, p in G['instrumentos'] if t.endswith('en 36 y en 28 encuentros')), 9.5)

    # ------------------------------------------------------------ 4. metodología y recursos
    MP.titulo(d, '4. Metodología y recursos')
    MP.lista(d, [
        '**Aprendizaje basado en proyectos.** El curso analiza, diseña, construye, verifica y entrega un sistema de préstamos '
        'para la biblioteca de un colegio ficticio (Arapoty). Las prácticas usan otro caso, Mbokaja, con datos distintos '
        '(MEC, p. 96: ABP; Work §7).',
        '**Estructura de taller de cada encuentro** (Work §5.1): 1 HC de problema y explicación, 3 HC de práctica y 1 HC de '
        'revisión, evidencia y cierre. En diagnósticos, relevamientos, hitos y defensas se redistribuye; la secuencia de cada '
        'encuentro está en la guía docente y en el plan de clase.',
        '**Actividades en cuatro bloques** (libro, pág. 6): «Ejercitá», «Resolvé», «Pensá y decidí» y «Desafío».',
        '**Prácticas en tres niveles** (libro, pág. 6): el Nivel 1 es el piso que todo el curso alcanza, el Nivel 2 es el '
        'esperado y el Nivel 3 es ampliación. Los Capítulos 16 y 18 no tienen práctica; las Prácticas 9 y 13 son '
        'complementos editoriales, fuera de las 5 HC.',
        '**Trabajo en equipo con evidencia individual.** Bitácora del equipo desde el primer día, versiones identificables y '
        'revisión entre pares. En cada hito, cada integrante resuelve una pregunta, variante o reporte individual.',
        '**Diagnóstico y apoyos.** El Encuentro 1 empieza con el diagnóstico de entrada sin nota; con él se arma el mapa de '
        'apoyos del curso (guía, pág. %d) y el plan de apoyo de cada estudiante.' % REF['mapa_apoyos'],
        '**Coordinación con otras disciplinas** (Work §3): Algorítmica 3.º informa antes del Encuentro 13 qué modelado ya '
        'trabajó (guía, pág. %d); Laboratorio 3.º confirma antes del Encuentro 19 el lenguaje, la conexión a la base y el '
        'entorno (guía, pág. %d). Cada disciplina evalúa su propia capacidad.' % (REF['acuerdo_algoritmica'], REF['laboratorio_iv']),
    ], 9.5)
    MP.titulo(d, 'Recursos', 3)
    MP.lista(d, [
        'Libro del estudiante anual (%d págs.), cuaderno anual de prácticas (%d págs.) y guía docente anual con solucionario '
        '(%d págs.), colección v0.2.' % (L['paginas'], MO.D['cuaderno']['paginas'], G['paginas']),
        'Unidades I a III (Encuentros 1 a 18): libro, cuaderno, papel y materiales impresos de la guía (tarjetas de rol, '
        'planillas). No requieren computadoras.',
        'Unidades IV a VI (Encuentros 19 a 36): una computadora por equipo con el entorno de la base de proyecto (HTML y CSS, '
        'PHP y SQLite, sin servicios pagos), verificado antes con la ficha de entorno E-1 a E-12 (guía, pág. %d). Es una '
        'referencia editorial provisional, no probada todavía en Windows ni en computadoras escolares.' % REF['ficha_entorno'],
        '**Sin computadoras suficientes:** rotación documentada de los equipos, sin omitir evidencias esenciales (guía, pág. '
        '%d); si ningún entorno funciona, una sola computadora preparada por el docente para demostraciones y pruebas, con la '
        'adaptación de 28 encuentros, registrado como limitación (guía, pág. %d). Ningún camino se declara probado si no se '
        'probó. Cada plan de clase indica la alternativa del encuentro.' % (REF['nota_e30'], REF['otro_entorno']),
        'Materiales reservados del docente, fuera del repositorio y de las carpetas del alumnado: conjunto DR (Unidad V, '
        'guía, pág. %d) y variantes V6 de la defensa (guía, pág. %d).' % (REF['dr'], REF['variantes']),
    ], 9.5)

    # ------------------------------------------------------------ 5. evaluación
    MP.titulo(d, '5. Evaluación', nueva_pagina=True)
    MP.lista(d, [
        '**Continua y basada en evidencias** (MEC, p. 101; Work §4.3): diagnóstico inicial, retroalimentación sobre productos, '
        'revisiones de unidad, evaluación intermedia (H3) y entrega final. Las actividades prácticas son fuente de evidencia.',
        '**Ponderación editorial sugerida** (Work §4.3): problema y relevamiento 15 %; requisitos y trazabilidad 20 %; modelos y '
        'diseño 20 %; prototipo e integración 20 %; pruebas y mejora 15 %; documentación y defensa 10 %. No es una escala '
        'oficial del MEC ni reemplaza el régimen institucional de calificación y promoción.',
        '**60 % producto compartido y 40 % evidencia individual** en cada criterio (explicación, resolución de un cambio '
        'acotado, bitácora y observación docente). La coevaluación orienta, pero no sustituye la valoración docente.',
        '**Niveles de desempeño:** 4 Sólido, 3 Logrado, 2 En desarrollo, 1 Inicial. La ausencia de evidencia se registra aparte. '
        'La conversión a calificaciones la hace la institución.',
        '**Evaluaciones escritas de capítulo:** opcionales, de 15 puntos, en página propia del libro, con su clave en la guía. '
        'El Capítulo 18 no tiene evaluación escrita. No ocupan tiempo de los encuentros: si la institución las aplica, define '
        'cuándo.',
        '**Condiciones mínimas de aceptación del prototipo** (Work §4.3): circuito de préstamo y devolución ejecutable; '
        'persistencia comprobada; ninguna pérdida de historial; rechazo del préstamo simultáneo del mismo ejemplar; evidencia '
        'de pruebas; instalación y restauración reproducibles. Son criterios del proyecto, no reglas de promoción.',
    ], 9.5)
    MP.titulo(d, 'Hitos integradores', 3)
    filas = []
    for n, h in MO.HITOS.items():
        e = E[n - 1]
        rub = next(i for i in e['instrumentos'] if i['nombre'].startswith('Rúbrica'))
        pla = next(i for i in e['instrumentos'] if i['nombre'].startswith('Planilla'))
        ev = next(i for i in e['instrumentos'] if i['nombre'].startswith('Evidencias'))
        desde = 1 if h == 'H1' else max(k for k in MO.HITOS if k < n) + 1
        caps = sorted({x['capitulo']['num'] for x in E if desde <= x['num'] <= n})
        filas.append([h, str(n), '%d a %d' % (caps[0], caps[-1]), e['hito_libro']['titulo'] if e['hito_libro'] else e['titulo'],
                      e['capacidades_enc'], str(e['hito_libro']['pagina'] if e['hito_libro'] else e['paginas_libro'][0][0]),
                      '%d · %d · %d' % (rub['pagina'], pla['pagina'], ev['pagina'])])
    MP.tabla(d, ['Hito', 'Enc.', 'Capítulos', 'Qué se evalúa (libro)', 'Capacidades (Work §5.2)', 'Libro, pág.',
                 'Guía: rúbrica · planilla · evidencias'], filas, [1.1, 1.0, 1.7, 6.0, 2.4, 1.5, MP.UTIL - 13.7])
    e35, e36 = E[34], E[35]
    MP.parrafo(d, '**Cierre del año.** Encuentro 35: demostración por equipo y defensa individual, con la rúbrica de producto '
                  'final y la planilla de defensa (guía, pág. %d); los tiempos se calculan con la planilla de tiempos (guía, '
                  'pág. %d) y la alternativa A, B o B+ (guía, pág. %d). Encuentro 36: defensas pendientes, recuperación por '
                  'fichas y evaluación integradora de la segunda etapa (libro, pág. %d).' % (
                      next(i['pagina'] for i in e35['instrumentos'] if i['nombre'].startswith('Rúbrica de producto')),
                      REF['tiempos_e35'], REF['alternativas_e35'], e36['paginas_libro'][-1][0]), 9.5, antes=4)

    # ------------------------------------------------------------ 6. desarrollo por unidad y capítulo
    MP.titulo(d, '6. Desarrollo por unidad, capítulo y encuentro', nueva_pagina=True)
    MP.parrafo(d, 'Para cada capítulo: la ficha del libro (capacidades con su rótulo, tema e indicadores, sin cambios), las '
                  'secciones y la articulación con otras disciplinas; para cada encuentro, su foco, la secuencia de la guía, '
                  'la evidencia y los instrumentos. El plan de clase del mismo número desarrolla cada fila.', 9.5)
    for r in MO.ROMANOS:
        tit, (a, b), hc, res = MO.W.UNIDADES[r]
        u = next(x for x in L['unidades'] if x['num'] == MO.ROMANOS.index(r) + 1)
        MP.titulo(d, 'Unidad %s — %s (Encuentros %d a %d, %d HC; libro, pág. %d)' % (r, tit, a, b, hc, u['pagina']), 2)
        for cnum in sorted({e['capitulo']['num'] for e in E if a <= e['num'] <= b}):
            es = [e for e in E if e['capitulo']['num'] == cnum]
            c = MO.CAPS[cnum]; f = c['ficha']
            MP.titulo(d, 'Capítulo %d — %s (libro, pág. %d)' % (cnum, c['titulo'], c['pagina']), 3)
            secs = ['%s (pág. %s)' % (s['titulo'], s['pagina']) for e in es for s in e['secciones']]
            extra = []
            if c['practica']: extra.append('%s (libro, pág. %d; cuaderno, pág. %s)' % (
                c['practica']['titulo'], c['practica']['pagina'],
                next((p for t, p in MO.CUAD.items() if t == c['practica']['titulo']), '—')))
            if c['evaluacion']: extra.append('%s, opcional (libro, pág. %d)' % (c['evaluacion']['titulo'], c['evaluacion']['pagina']))
            if c['hito']: extra.append('%s (libro, pág. %d)' % (c['hito']['titulo'], c['hito']['pagina']))
            MP.tabla(d, ['', ''], [
                [f['rotulo_capacidad'], f['capacidad']],
                ['Tema (contenidos)', f['tema']],
                ['Indicadores de logro', [('lista', f['indicadores'])]],
                ['Secciones', [('lista', secs)]],
                ['Práctica, evaluación e hito', [('lista', extra)] if extra else '—'],
                ['Articulación con otras disciplinas (Diseño Curricular MEC, páginas según Work §3)', e_ant(es[0])],
            ], [4.2, MP.UTIL - 4.2], encabezado=False, fondo_primera_col=True)
            MP.parrafo(d, '', 4, despues=1)
            filas = []
            for e in es:
                tramos = ['**%s** (%s)' % (t['momento'], t['tiempo']) for t in e['tramos_guia']]
                if e['fuera']:
                    tramos += ['%s: %s' % (t['momento'], t['que_se_hace'].split(':')[0]) for t in e['fuera']]
                ins = ['%s (guía, pág. %d)' % (i['nombre'], i['pagina']) for i in e['instrumentos']]
                filas.append([str(e['num']),
                              ['**%s**' % e['titulo'], 'Foco (Work): ' + e['foco'], 'Libro, págs. %s' % pags(e['paginas_libro'])],
                              [('lista', tramos)] + ['Guía, pág. %d · %s' % (e['guia']['secuencia_pagina'], e['hc_guia'])]
                              + actividades_y_recursos(e),
                              ['Capacidades: ' + e['capacidades_enc'],
                               'Indicadores de la ficha: ' + ', '.join(str(i) for i, _ in e['indicadores']),
                               'Evidencia: ' + e['evidencia']],
                              [('lista', ins)]])
            MP.tabla(d, ['Enc.', 'Encuentro, foco y páginas', 'Secuencia (guía docente)', 'Capacidades, indicadores y evidencia',
                         'Instrumentos'], filas, [1.0, 4.0, 4.5, 3.9, MP.UTIL - 13.4], tam=8)

    # ------------------------------------------------------------ 7. pendientes
    MP.titulo(d, '7. Adopción del plan en la institución')
    MP.lista(d, [
        'Incorporar el programa en el PCI de la institución (MEC, p. 24) y completar los datos de la sección 1.3.',
        'Completar en el Anexo A la semana o la fecha de cada encuentro, según el calendario institucional.',
        'Si el año tiene menos semanas efectivas, usar la adaptación a 28 encuentros de la guía docente.',
        'Antes del Encuentro 19, hacer la prueba de campo del entorno en las computadoras de la institución (guía, Parte IV, '
        'sección 0.2) y coordinar con Laboratorio y Algorítmica.',
    ], 9.5)

    # ------------------------------------------------------------ anexos horizontales
    MP.seccion_horizontal(d)
    MP.titulo(d, 'Anexo A — Distribución temporal: HC por categoría y capacidades de cada encuentro')
    MP.parrafo(d, 'HC por categoría según la distribución v2.1; capacidades según Work §5.2. La última columna la completa la '
                  'institución con la semana o la fecha prevista: este plan no fija fechas.', 8.5)
    cods = list(MO.W.CAPACIDADES)
    filas = []
    for e in E:
        caps = capacidades_de(e['capacidades_enc'])
        filas.append([str(e['num']), e['unidad']['rom'], str(e['capitulo']['num']), e['titulo']] +
                     [str(e['hc_cat'][c]) if e['hc_cat'][c] else '' for c, _ in MO.CATS] + [str(sum(e['hc_cat'].values()))] +
                     ['×' if k in caps else '' for k in cods] + [''])
    filas.append(['', '', '', 'Total'] + [str(sum(e['hc_cat'][c] for e in E)) for c, _ in MO.CATS] + ['180'] +
                 [str(sum(1 for e in E if k in capacidades_de(e['capacidades_enc']))) for k in cods] + [''])
    cm = [0.9, 0.9, 0.9, 8.6] + [0.95] * 7 + [1.05] + [0.85] * 10 + [0]
    cm[-1] = MP.UTIL_H - sum(cm)
    t = MP.tabla(d, ['Enc.', 'Un.', 'Cap.', 'Encuentro (libro)'] + [c for c, _ in MO.CATS] + ['Total'] + cods +
                 ['Semana o fecha (institución)'], filas, cm, tam=8)
    for row in t.rows[1:-1]:
        MP.campo(row.cells[-1].paragraphs[0], 'fecha')
    MP.parrafo(d, ' · '.join('%s %s' % (c, nom) for c, nom in MO.CATS) + '.', 8.5, antes=3)

    MP.titulo(d, 'Anexo B — Matriz de correspondencia: plan anual, libro, guía docente, prácticas e hitos', nueva_pagina=True)
    MP.parrafo(d, 'Cada fila es un encuentro y su plan de clase (mismo número). Las páginas son las de los documentos de la '
                  'colección v0.2.', 8.5)
    filas = []
    for e in E:
        p = e['practica']
        ins = {i['nombre'].split(' (')[0]: i['pagina'] for i in e['instrumentos']}
        hito = '—'
        if e['hito']:
            rub = next(v for k, v in ins.items() if k.startswith('Rúbrica')); pla = next(v for k, v in ins.items() if k.startswith('Planilla'))
            hito = '%s · libro %d · rúbrica %d · planilla %d' % (e['hito'], e['hito_libro']['pagina'], rub, pla)
        else:
            h, n = e['proximo_hito']
            if h: hito = 'prepara %s (E%d)' % (h, n)
        evc = e['evaluacion_capitulo']
        clave = next((p_ for t_, _, p_ in G['instrumentos'] if t_ == 'Clave de la evaluación del capítulo %d' % e['capitulo']['num']), None)
        filas.append([str(e['num']), '%s · %d' % (e['unidad']['rom'], e['capitulo']['num']), pags(e['paginas_libro']),
                      '%s · %d · %d' % (e['guia']['parte'], e['guia']['secuencia_pagina'], e['guia']['claves_pagina']),
                      ('P%d%s · libro %d-%d · cuaderno %s · cotejo %s' % (
                          p['num'], ' (complemento)' if p['complemento'] else '', p['libro'][0], p['libro'][1], p['cuaderno'],
                          p['cotejo']['pagina'] if p['cotejo'] else '—')) if p else '—',
                      ('libro %d · clave %s' % (evc['pagina'], clave)) if evc else '—', hito, e['capacidades_enc'],
                      'N.º %d (pág. %s)' % (e['num'], PAG_PLANES.get(str(e['num']), '—'))])
    MP.tabla(d, ['Enc.', 'Unidad · cap.', 'Libro, págs.', 'Guía: parte · secuencia · claves', 'Práctica',
                 'Evaluación del capítulo (opcional)', 'Hito', 'Capacidades', 'Plan de clase'],
             filas, [1.0, 1.7, 2.6, 2.8, 6.4, 3.4, 6.2, 3.6, MP.UTIL_H - 27.7], tam=8)
    MP.pie(d.sections[0], 'Análisis y Diseño de Sistemas · 3.º BTI · Edición 2026 · Plan anual · %s' % VERSION)
    ruta = os.path.join(PLAN, NOMBRE + '.docx')
    d.save(ruta)
    MP.a_pdf(ruta, PLAN)
    return ruta


def capacidades_de(texto):
    """«C1-C7» → C1 a C7; «C7-C9» → C7, C8, C9."""
    import re
    out = set()
    for parte in re.split(r',\s*', texto):
        m = re.match(r'C(\d+)-C(\d+)', parte.strip())
        if m:
            out |= {'C%d' % i for i in range(int(m.group(1)), int(m.group(2)) + 1)}
        elif parte.strip():
            out.add(parte.strip())
    return out


def actividades_y_recursos(e):
    out = []
    propias = sorted(a['num'] for a in e['actividades_clase'] if a['encuentro'] == e['num'] and isinstance(a['num'], int))
    tarea = [str(a['num']) for a in e['actividades_tarea'] if a['encuentro'] == e['num']]
    if propias or tarea:
        out.append('Actividades del libro: %s%s' % (', '.join(map(str, propias)) or '—', ' · tarea: %s' % ', '.join(tarea) if tarea else ''))
    if e['practica']:
        out.append('Práctica %d%s' % (e['practica']['num'], ' (complemento, fuera de las 5 HC)' if e['practica']['complemento'] else ''))
    out.append({None: 'Sin computadoras: libro, cuaderno y papel', 'equipo': 'Una computadora por equipo (alternativa en el plan de clase)',
                'demostracion': 'Computadora de la demostración', 'recuperacion': 'Computadoras según la recuperación'}[e['requiere_computadoras']])
    return out


def e_ant(e):
    return e['antecedentes'] + ' La asignación al capítulo es propuesta editorial.'


if __name__ == '__main__':
    print(construir())

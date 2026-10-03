# -*- coding: utf-8 -*-
"""Datos de los 36 planes (y de las 36 filas del Plan Anual) de la Edición Esencial.
Fuente: planes vigentes (planes_old.json) + libro nuevo (fichas, actividades, prácticas, figuras).
Reglas: el material es «el libro»; figuras renumeradas por clase; puntos de control y actividades
según la edición nueva; continuaciones reescritas a partir de las Actividades 2 y 3 de cada práctica."""
import json, re
from estructura import cargar
import ediciones, ediciones_v2, actividades, practicas, evaluaciones

P_OLD = {p['n']: p for p in json.load(open('/home/claude/alg3/build/planes_old.json'))}
_pre, C, _ev, U = cargar()
OLDFIG = {}
for n, c in C.items():
    for b in c['cuerpo']:
        if b['t'] == 'img':
            m = re.match(r'Figura (\d+\.\d+)', b.get('epigrafe', ''))
            if m:
                OLDFIG[b['file']] = m.group(1)
ediciones.aplicar(C)
NEWFIG = ediciones.fig_refs(C)
FIGMAP = {OLDFIG[f]: NEWFIG[f].replace('Figura ', '') for f in OLDFIG}

# orden de los 36 encuentros: ('C', n) clase · ('P', n) continuación práctica · ('E', id) · ('T', k) taller PFI
ORDEN = []
for n in range(1, 22):
    ORDEN.append(('C', n))
    if n in (4, 5, 6, 7, 8, 9, 10, 18, 19, 21):
        ORDEN.append(('P', n))
    if n == 10:
        ORDEN.append(('E', 'E1'))
ORDEN += [('T', 1), ('T', 2), ('T', 3), ('E', 'E2')]
assert len(ORDEN) == 36
CONT = {4, 5, 6, 7, 8, 9, 10, 18, 19, 21}
EVAL_UNIDAD_EN = {('P', 4): 'U1', ('P', 10): 'U2', ('C', 17): 'U3', ('P', 21): 'U4'}
UNIDAD_DE = {n: C[n]['unidad'] for n in C}


def _fam(n):
    it = actividades.items(n)
    er = [k for f, k, *_ in it if f.startswith('Ejercit') or f.startswith('Resolv')]
    pd = [k for f, k, *_ in it if f.startswith('Pens')]
    de = [k for f, k, *_ in it if f.startswith('Desaf')]
    return er, pd, de, len(it)


def _rango(lst):
    return '%d a %d' % (lst[0], lst[-1]) if len(lst) > 1 else str(lst[0])


def _y(lst):
    return ' y '.join(str(x) for x in lst) if len(lst) <= 2 else ', '.join(str(x) for x in lst[:-1]) + ' y ' + str(lst[-1])


def transformar(t, n=None):
    t = t.replace('que abre el cuadernillo', 'que abre el libro').replace('hoja propia del cuadernillo', 'hoja propia del libro')
    t = t.replace('Cuadernillo del estudiante', 'Libro del estudiante').replace('Cuadernillo de Algorítmica 3.er Curso', 'Libro del estudiante').replace('cuadernillo', 'libro')
    t = re.sub(r'Práctica (\d+) «[^»]+» del Cuaderno', lambda m: 'Práctica %s «%s» del libro' % (m.group(1), practicas.PR[int(m.group(1))]['titulo']), t)
    t = re.sub(r'Práctica (\d+) «[^»]+»', lambda m: 'Práctica %s «%s»' % (m.group(1), practicas.PR[int(m.group(1))]['titulo']), t)
    t = t.replace('del Cuaderno de Prácticas', 'del libro').replace('Cuaderno de Prácticas, ', '').replace('Cuaderno de Prácticas ·', '')
    t = re.sub(r'(figuras?) (\d+\.\d+)((?:,? (?:y )?\d+\.\d+)*)',
               lambda m: m.group(1) + ' ' + re.sub(r'\d+\.\d+', lambda q: FIGMAP.get(q.group(0), q.group(0)), m.group(2) + m.group(3)), t)
    for (cn, tit), acc in ediciones_v2.RECUADROS.items():
        if acc == 'keep' or tit not in t:
            continue
        if isinstance(acc, tuple):
            t = t.replace('«%s»' % tit, '«%s»' % acc[1])
        else:
            q = re.escape(tit)
            t = re.sub(r'cajas «([^»]+)» y «%s»' % q, r'caja «\1»', t)
            t = re.sub(r'las cajas «%s» y «([^»]+)»' % q, r'la caja «\1»', t)
            t = re.sub(r',? y de «%s»' % q, '', t)
            t = re.sub(r',? caja «%s»' % q, '', t)
        assert tit not in t, (tit, t)
    if n:
        er, pd, de, tot = _fam(n)
        t = re.sub(r'actividades 1 a \d+(?! y)', 'actividades 1 a %d' % er[-1], t)
        t = re.sub(r'actividades 1 a \d+ y \d+ a \d+', 'actividades 1 a %d' % tot, t)
        t = re.sub(r'afirmaciones \d+ y \d+', 'afirmaciones %s' % _y(pd), t)
    return t


# anulaciones puntuales de viñetas (plan, momento, índice) → texto nuevo (None = borrar)
OVR = {
 (2, 'Desarrollo', 3): 'Lectura de «El proceso de traducción por dentro» con la figura 2.3, la cadena de compilación del código fuente al ejecutable, y resolución de las actividades 1 a 7, incluida la consigna del caso: por qué «subtotal = 3 * 6000» no se ejecuta tal cual.',
 (4, 'Desarrollo', 3): 'Elaboración individual de la ficha de decisión de lenguaje para el caso de la ferretería (actividad 5), recálculo de la matriz del Copetín con otros pesos (actividad 7) y resolución de las actividades 1 a 4 y 6.',
 (12, 'Desarrollo', 3): 'Resolución de las actividades 1 a 8, con seguimiento explícito de la clave foránea de la venta V4 hasta la tabla Clientes y asignación de tipos de datos.',
 (14, 'Desarrollo', 3): 'Resolución de casos permitido/prohibido de las actividades 1 a 7, incluido el intento de borrar a Ana Gómez (C03), que tiene la venta V4, con restricción y con cascada.',
 (28, 'Desarrollo', 1): 'Construcción de la consulta en la cuadrícula de diseño siguiendo el ejemplo resuelto «las ventas del primer día, con control», con la figura 19.1 como modelo de la cuadrícula y su resultado.',
 (30, 'Desarrollo', 1): 'Escritura del parámetro en la fila Criterios y ejecución con dos valores distintos, con el ejemplo «las ventas de un cliente» como modelo.',
}


def _es_practica(x):
    return re.search(r'Práctica \d+ «|punto de control de la Práctica|Resolución de la Práctica|Preparación de la continuación', x) is not None


def _bullet_practica(n, cont):
    p = practicas.PR[n]
    a1 = p['acts'][0]
    if cont:
        return 'Práctica %d del libro, «%s» (%s): Actividad 1, «%s». Las actividades siguientes se trabajan en el encuentro de continuación.' % (n, p['titulo'], p['entorno'], a1['titulo'])
    return 'Práctica %d del libro, «%s» (%s): Actividad 1, «%s», y Actividad 2, «%s».' % (n, p['titulo'], p['entorno'], a1['titulo'], p['acts'][1]['titulo'])


def _cierre_practica(n, cont):
    p = practicas.PR[n]
    acts = p['acts'][:1] if cont else p['acts'][:2]
    txt = '; '.join('Actividad %d: «%s»' % (k, a['control']) for k, a in enumerate(acts, 1))
    return 'Verificación de los puntos de control de la Práctica %d (%s).' % (n, txt)


ALT_PAPEL = ' Alternativa sin equipamiento disponible: la actividad se resuelve en papel con la consigna impresa de la práctica y se ejecuta en la máquina en la primera sesión de laboratorio disponible.'


def plan_clase(idx, n):
    old = P_OLD[idx]
    cont = n in CONT
    m = {}
    for mom in ('Inicio', 'Desarrollo', 'Cierre'):
        out = []
        for i, x in enumerate(old['momentos'][mom]):
            # las viñetas con «•» internos se separan
            for j, y in enumerate([s.strip() for s in re.split(r'\n?•\s*', x) if s.strip()]):
                key = (idx, mom, i)
                if key in OVR and j == 0:
                    if OVR[key] is not None:
                        out.append(OVR[key])
                    continue
                elif _es_practica(y):
                    continue
                if 'evaluación de la Unidad' in y and 'se aplicará al cierre' in y:
                    continue
                out.append(transformar(y, n))
        m[mom] = out
    m['Desarrollo'].append(_bullet_practica(n, cont))
    er, pd, de, tot = _fam(n)
    m['Cierre'].insert(0, _cierre_practica(n, cont))
    if cont:
        m['Cierre'].append('Anuncio del encuentro de continuación: Actividades 2 y 3 y desafío final de la Práctica %d.' % n)
    if ('C', n) in EVAL_UNIDAD_EN:
        ev = EVAL_UNIDAD_EN[('C', n)]
        if not any('evaluación de la Unidad' in x for x in m['Cierre']):
            m['Cierre'].append('Aplicación de la evaluación de la Unidad %s, fotocopiable, en su hoja propia del libro.' % ev[1])
    elif any(('P', n) == k for k in EVAL_UNIDAD_EN):
        m['Cierre'].append('Anuncio: la evaluación de la Unidad %d se aplica al cierre del encuentro de continuación.' % UNIDAD_DE[n])
    rec = transformar(old['recursos'], n)
    rec = re.sub(r'actividades 1 a \d+', 'actividades 1 a %d' % tot, rec)
    rec = rec.replace('Cuaderno de Prácticas', '').replace('  ', ' ')
    rec = re.sub(r'·\s*Práctica \d+\s*·', '·', rec)
    rec = rec.rstrip('. ') + ' · Práctica %d del libro (%s).' % (n, practicas.PR[n]['entorno'])
    if practicas.PR[n]['entorno'] != 'papel y lápiz':
        rec += ALT_PAPEL
    f = C[n]['ficha']
    inst = transformar(old['inst'], n)
    inst = re.sub(r'\s*·\s*Punto\(s\) de control de la Práctica \d+\.?', '', inst)
    inst = inst.replace(' Evaluación de la unidad (fotocopiable).', '')
    if ('C', n) in EVAL_UNIDAD_EN:
        inst = inst.rstrip('.') + '. Evaluación de la Unidad %d (fotocopiable).' % UNIDAD_DE[n]
    proc = transformar(old['proc'], n)
    proc = re.sub(r'\s*·\s*(Práctica \d+ integrada en este mismo encuentro|Continuación en encuentro propio: Práctica \d+ del libro)\.?', '', proc)
    return dict(idx=idx, tipo='C', n=n, titulo=C[n]['titulo'], tema=f['tema'], capacidad=f['capacidad'], indicadores=f['indicadores'],
                unidad='UNIDAD %d — %s' % (UNIDAD_DE[n], U[UNIDAD_DE[n]]), material='Libro del estudiante · Clase %d y Práctica %d' % (n, n),
                momentos=m, tiempos=(40, 90, 30), recursos=rec, proc=proc, inst=inst, criterios=old['criterios'])


# Procedimientos e instrumentos propios de cada continuación (únicos en todo el Plan Anual)
CONT_EVAL = {
 4: ('Recálculo de la matriz con pesos de la cooperadora y chequeo de ecosistema de la opción ganadora.', 'Ficha de decisión documentada (siete campos) revisada con lista de cotejo.'),
 5: ('Detección de problemas de calidad en el cuaderno de préstamos y clasificación dato/información/conocimiento.', 'Tabla de problemas de calidad con su dimensión, evaluada con escala de estimación.'),
 6: ('Elección de modelo e infraestructura para cinco escenarios y planificación de los objetos de una base.', 'Cuadro de escenarios justificados y plan de objetos del archivo, con rúbrica breve.'),
 7: ('Construcción de la matriz de permisos con mínimo privilegio y simulación de una transacción con falla.', 'Matriz de permisos y relato de la transacción, evaluados con lista de cotejo ACID.'),
 8: ('Recorrido de claves foráneas con datos y búsqueda de la clave compuesta de un horario.', 'Diagrama de flechas FK → PK y respuesta a tres preguntas de recorrido.'),
 9: ('Cálculo de los efectos de la eliminación en cascada y clasificación de violaciones por integridad.', 'Resolución escrita de casos con cascada y nulos, corregida en coevaluación.'),
 10: ('Clasificación de tipos de usuario y diseño de vistas con predicción del nivel afectado por cada cambio.', 'Propuesta de dos vistas con justificación de privacidad, evaluada con rúbrica.'),
 18: ('Definición de relaciones con sus casillas de cascada y carga ordenada de 33 registros de la segunda semana.', 'Base Copetin_Semana2.accdb verificada en el puesto (relaciones, conteo de registros y precio histórico de V8).'),
 19: ('Diseño, anticipación y verificación de cuatro consultas de selección y lectura de fechas en la vista SQL.', 'Hoja de anticipación contra resultado de cuatro consultas guardadas, con control por complemento.'),
 21: ('Construcción de totales por cuatro caminos, referencia cruzada y detección del error de precio de catálogo.', 'Informe breve de control cruzado (135.000 por tres caminos y diferencia de G. 1.000 explicada).'),
}


def plan_continuacion(idx, n):
    p = practicas.PR[n]
    acts = p['acts'][1:]
    ev = EVAL_UNIDAD_EN.get(('P', n))
    ini = ['Recuperación del punto de control de la Actividad 1 de la Práctica %d y organización de los puestos o de las parejas de trabajo.' % n,
           'Presentación del objetivo de la Actividad 2: %s' % acts[0]['objetivo']]
    des = []
    for k, a in enumerate(acts, 2):
        des.append('Actividad %d, «%s»: %s Acompañamiento docente en los pasos con más dificultad: %s' % (k, a['titulo'], a['objetivo'], a['pasos'][0][0].lower() + a['pasos'][0][1:]))
    if p.get('transfer'):
        des.append('Transferencia y revisión entre pares (30 a 40 minutos): mini-caso «%s» con datos diferentes; intercambio con otro equipo, detección de al menos un error, corrección y justificación escrita de la versión final.' % p['transfer']['caso'][0])
    des.append('Desafío final para quienes terminan antes: %s' % p['desafio'])
    cie = ['Verificación de los puntos de control: %s.' % '; '.join(['Actividad %d, «%s»' % (k, a['control']) for k, a in enumerate(acts, 2)] + (['transferencia entre pares, «%s»' % p['transfer']['control']] if p.get('transfer') else [])),
           'Registro breve de dificultades y corrección colectiva de los errores frecuentes de la práctica.']
    tiempos = (20, 120, 20)
    if ev:
        cie.append('Aplicación de la evaluación de la Unidad %s, fotocopiable, en su hoja propia del libro.' % ev[1])
        tiempos = (20, 100, 40)
    rec = 'Libro del estudiante, Práctica %d (Actividades %s y desafío final) · %s' % (n, _y(list(range(2, len(p['acts']) + 1))), p['entorno'])
    if p.get('datos'):
        rec += ' · datos para cargar de la práctica'
    rec += ' · pizarra y marcadores.'
    if p['entorno'] != 'papel y lápiz':
        rec += ALT_PAPEL
    f = C[n]['ficha']
    proc, inst = CONT_EVAL[n]
    if ev:
        inst = inst.rstrip('.') + '. Evaluación de la Unidad %s (fotocopiable).' % ev[1]
    crit = ['Cumple el punto de control de cada actividad sin ayuda externa.', 'Justifica sus decisiones con los conceptos de la Clase %d.' % n,
            'Corrige sus errores a partir de la verificación y deja el trabajo documentado.']
    return dict(idx=idx, tipo='P', n=n, titulo='Continuación práctica de la Clase %d: %s' % (n, p['titulo']), tema=f['tema'], capacidad=f['capacidad'],
                indicadores=f['indicadores'], unidad='UNIDAD %d — %s' % (UNIDAD_DE[n], U[UNIDAD_DE[n]]), material='Libro del estudiante · Práctica %d' % n,
                momentos={'Inicio': ini, 'Desarrollo': des, 'Cierre': cie}, tiempos=tiempos, recursos=rec, proc=proc, inst=inst, criterios=crit)


def plan_viejo(idx):
    old = P_OLD[idx]
    m = {k: [transformar(s.strip()) for x in v for s in re.split(r'\n?•\s*', x) if s.strip()] for k, v in old['momentos'].items()}
    for k in m:
        m[k] = [x.replace('Cuaderno de Prácticas', 'libro') for x in m[k]]
    t = tuple(int(old['tiempos'][k].split()[0]) for k in ('Inicio', 'Desarrollo', 'Cierre'))
    mat = transformar(old['info'].get('Material', '')).replace('Cuaderno de Prácticas · ', 'Libro del estudiante · ')
    return dict(idx=idx, titulo=old['titulo'], tema=old['info'].get('Tema', ''), capacidad=old['capacidad'], indicadores=old['indicadores'],
                unidad=old['info'].get('Unidad', ''), material=mat, momentos=m, tiempos=t,
                recursos=transformar(old['recursos']).replace('Cuaderno de Prácticas · ', 'Libro del estudiante · '), proc=transformar(old['proc']),
                inst=transformar(old['inst']), criterios=old['criterios'])


PFI_DES = {
 1: ['Lectura del Proyecto Final Integrador del libro: competencia, requisitos mínimos de la solución y etapas.',
     'Elección del emprendimiento y redacción de al menos cuatro preguntas del negocio que la base debe responder.',
     'Delimitación del mini-mundo y dibujo del DER con al menos una relación N:M; revisión con la lista de control de la Clase 14.',
     'Traducción del DER a tablas y verificación de la 3FN con las dependencias funcionales principales escritas.'],
 2: ['Creación de la base en Access: tablas con tipos y propiedades, clave compuesta en la tabla puente y relaciones con integridad referencial.',
     'Carga de datos de prueba propios del equipo (no los del libro) en el orden que exige la integridad referencial.',
     'Formulación de las cinco consultas mínimas: selección con criterio, paramétrica, totales, campo calculado y referencias cruzadas.',
     'Integración con las otras materias: logo, planilla de cálculos, presentación y resguardo de los archivos.'],
 3: ['Control cruzado de cada consulta (por ejemplo, total por cliente igual a total por categoría) y corrección de errores.',
     'Extensión recomendada (no es requisito para aprobar): formulario de carga e informe, con exportación del informe a PDF.',
     'Ensayo de la demostración de cinco minutos con reparto de roles y guion.',
     'Coevaluación entre equipos con la rúbrica del Proyecto Final Integrador.'],
}


def plan_taller(idx, k):
    p = plan_viejo(idx)
    p['momentos']['Desarrollo'] = PFI_DES[k]
    p['material'] = 'Libro del estudiante · Proyecto Final Integrador · Solucionario docente (rúbrica)'
    p['recursos'] = ('Libro del estudiante, Proyecto Final Integrador (requisitos mínimos, etapas, aportes de cada materia y Figura PFI.1) · computadoras con Microsoft Access · '
                     'carpeta del proyecto · rúbrica del Solucionario docente.' + ALT_PAPEL)
    p['tipo'] = 'T'; p['n'] = k
    p['capacidad'] = ediciones_v2.caps(ediciones_v2.CAP_TALLER)
    return p


def plan_eval(idx, eid):
    p = plan_viejo(idx)
    p['tipo'] = 'E'; p['n'] = eid
    p['capacidad'] = ediciones_v2.caps(ediciones_v2.CAP_EVAL[eid])
    if eid == 'E1':
        p['momentos']['Desarrollo'][0] = 'Resolución individual de la Parte A, de diagnóstico rápido: tres consignas de opción múltiple sobre el paradigma dirigido por eventos, el modelo relacional y la redundancia.'
        p['momentos']['Desarrollo'][1] = 'Resolución individual de la Parte B, de resolución y aplicación: necesidad del traductor y estrategias de ejecución, elección justificada de lenguaje para la secretaría de un club, diseño de la tabla Socios con su clave principal, integridad referencial en la tabla Pagos y cálculo paso a paso del total de una venta.'
    else:
        p['momentos']['Desarrollo'][0] = 'Resolución individual de la parte de diseño: DER del Copetín con la cardinalidad de cada relación y los atributos de la relación «contiene», y traducción del DER a las cuatro tablas con sus claves.'
        p['momentos']['Desarrollo'][1] = 'Resolución individual de la parte de normalización: explicación, con un ejemplo del caso, de una anomalía de actualización y de cómo la evita la normalización.'
        p['momentos']['Desarrollo'][2] = 'Resolución individual de la parte de consultas: escritura de un criterio paramétrico con su resultado e interpretación de totales por cliente, recaudación total y venta promedio.'
    p['proc'] = 'Resolución individual de la prueba integradora de la %s.' % ('1.ª etapa (Unidades 1 y 2)' if eid == 'E1' else '2.ª etapa (Unidades 3 y 4)')
    p['material'] = 'Libro del estudiante · evaluación integradora fotocopiable en hoja propia'
    return p


def planes():
    out = []
    for idx, (t, n) in enumerate(ORDEN, 1):
        if t == 'C':
            out.append(plan_clase(idx, n))
        elif t == 'P':
            out.append(plan_continuacion(idx, n))
        elif t == 'T':
            out.append(plan_taller(idx, n))
        else:
            out.append(plan_eval(idx, n))
    # coherencia: los títulos de los planes viejos coinciden con el orden
    for p in out:
        assert p['idx'] == P_OLD[p['idx']]['n']
        assert sum(p['tiempos']) == 160, (p['idx'], p['tiempos'])
    return out


if __name__ == '__main__':
    PL = planes()
    print('Mapa de figuras viejas → nuevas:', FIGMAP)
    import itertools
    for p in PL:
        txt = json.dumps(p, ensure_ascii=False)
        for bad in ('Cuaderno', 'cuadernillo', 'Cuadernillo', '14.000', 'V1 y V3', 'Prolog → lógico, Java'):
            if bad in txt and p.get('tipo') != 'E':
                print('RESIDUO', p['idx'], bad)
    procs = [p['proc'] for p in PL]; insts = [p['inst'] for p in PL]
    print('procedimientos únicos', len(set(procs)), 'de', len(procs), '· instrumentos únicos', len(set(insts)), 'de', len(insts))

# -*- coding: utf-8 -*-
"""Los 36 planes de clase de Análisis y Diseño de Sistemas, 3.º BTI, en un solo DOCX editable (y su PDF de control), en
oficio O3. Cada plan empieza en página nueva y se arma con modelo.py: secuencia de la guía aprobada (tramos y tiempos),
ficha del capítulo (capacidades e indicadores sin cambios), actividades, recursos y páginas del libro, claves e
instrumentos de la guía, prácticas del cuaderno e hitos. Lo que agrega la planificación (organización del inicio en siete
encuentros, orientaciones y alternativas sin computadoras) remite siempre a su fuente.
Uso: python3 -B planificacion/build/planes_clase.py
"""
import os, re, sys
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import modelo as MO
import maqueta_plan as MP
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor

PLAN = os.path.dirname(AQUI)
NOMBRE = 'ADS_3BTI_PLANES_DE_CLASE_OFICIO_O3'
VERSION = 'Versión 0.1 para revisión'
G = MO.D['guia']
REF = {k: v['pagina'] for k, v in G['referencias'].items()}
E = MO.ENCUENTROS
DISCIPLINA = 'Análisis y Diseño de Sistemas (Plan Optativo, programa institucional)'


def pags(rangos):
    out = []
    for a, b in rangos:
        s = str(a) if a == b else '%d-%d' % (a, b)
        if s not in out: out.append(s)
    return ', '.join(out)


def act_txt(a, propio):
    pre = 'Act. %s' % a['num'] if a['encuentro'] == propio else 'Act. %s del Encuentro %d' % (a['num'], a['encuentro'])
    return '%s (%s): %s%s' % (pre, a['tipo'] or 'actividad', a['consigna'], ' Se termina como tarea.' if a.get('sigue_como_tarea') else '')


def tramo_txt(t, resto=None):
    tiempo = 'resto del tramo, %s' % MO.fmt_hc(resto) if resto is not None else t['tiempo']
    return '**%s** (%s). %s' % (t['momento'], tiempo, t['que_se_hace'])


# ---------------------------------------------------------------- bloques del plan
def momentos(e):
    n = e['num']; m = e['momentos']
    ini = ['**Propósito para comunicar al curso.** %s' % e['foco']]
    previo = E[n - 2] if n > 1 else None
    if previo and previo['actividades_tarea']:
        ini.append('**Tarea del Encuentro %d.** Se recoge al comenzar: %s. Claves: guía, pág. %d.' % (
            n - 1, ', '.join('Act. %s' % a['num'] for a in previo['actividades_tarea']), previo['guia']['claves_pagina']))
    if m['inicio'].get('apertura'):
        nota = ('dentro de la planilla de tiempos' if n == 35 else
                '%s tomadas del tramo «%s» de la guía' % (MO.fmt_hc(MO.APERTURA_HC), m['inicio']['desde']))
        ini.append('**Apertura** (%s). %s' % (nota, m['inicio']['apertura']))
    ini += [tramo_txt(t) for t in m['inicio']['tramos']]

    des = []
    for t in m['desarrollo']['tramos']:
        des.append(tramo_txt(t, t['hc'] if t.get('parcial') else None))
    if e['conceptos']:
        des.append('**Ideas clave para explicar** (recuadros «Concepto clave» del libro):')
        des.append(('lista', ['%s: %s (pág. %s)' % (c['titulo'], c['definicion'], c['pagina']) for c in e['conceptos']]))
    if e['ejemplos']:
        des.append('**Procedimiento modelado** (se explica con los ejemplos resueltos antes de que trabajen solos): ' +
                   '; '.join('%s (pág. %s)' % (x['titulo'].split(':')[0], x['pagina']) for x in e['ejemplos']) + '.')
    if e['actividades_clase']:
        des.append('**Actividades del libro en clase** (desde la pág. %s):' % e['pagina_actividades'])
        des.append(('lista', [act_txt(a, n) for a in e['actividades_clase']]))
    p = e['practica']
    if p and not p['complemento']:
        des.append('**%s** (libro, págs. %d-%d; cuaderno, pág. %s): %s.' % (
            p['titulo'], p['libro'][0], p['libro'][1], p['cuaderno'], ', '.join(p['niveles'])))

    cie = [tramo_txt(t) for t in m['cierre']['tramos']]
    if m['cierre'].get('cierre_planilla'):
        cie.append(m['cierre']['cierre_planilla'])
    cie.append('**Evidencia del encuentro** (Work §5.2): %s' % e['evidencia'])
    if e['repaso']:
        items, pg = e['repaso']
        cie.append('**Síntesis del capítulo** (recuadro «Para repasar», libro, pág. %s):' % pg)
        cie.append(('lista', items))
    if e['actividades_tarea']:
        cie.append('**Tarea:**')
        cie.append(('lista', [act_txt(a, n) for a in e['actividades_tarea']]))
    else:
        cie.append('**Tarea:** la guía no asigna tarea en este encuentro.')

    hc = lambda x: MO.fmt_hc(x) if x is not None else 'según la planilla de tiempos'
    filas = [['**Inicio**', ini, hc(m['inicio']['hc'])], ['**Desarrollo**', des, hc(m['desarrollo']['hc'])],
             ['**Cierre**', cie, hc(m['cierre']['hc'])]]
    for t in e['fuera']:
        filas.append(['**Fuera de las 5 HC**', [tramo_txt(t)], 'no suma'])
    filas.append(['**Total**', '' if e['total_hc'] else 'El reparto entre demostraciones y defensas lo calcula la planilla de '
                  'tiempos (guía, pág. %d), con la alternativa A, B o B+ (guía, pág. %d).' % (REF['tiempos_e35'], REF['alternativas_e35']),
                  '**5 HC**'])
    return filas


MODALIDADES = [(r'en parejas', 'en parejas'), (r'individual', 'individual'), (r'plenario|puesta en común', 'en plenario'),
               (r'cada equipo|los equipos|del equipo|entre equipos', 'por equipos'),
               (r'revisión cruzada|entre pares|otro equipo|entre equipos', 'revisión entre equipos o pares')]

PREPARACION = {
    1: 'Leer las claves del diagnóstico de entrada (guía, pág. %d) y el modelo del mapa de apoyos (guía, pág. %d), y la '
       'coordinación con otras asignaturas (guía, pág. %d).' % (MO.instrumento('Claves del diagnóstico')['pagina'],
                                                              REF['mapa_apoyos'], REF['coordinacion_i']),
    4: 'Fotocopiar y recortar las tarjetas de rol de la Práctica 2 (guía, Parte I, sección 3): cada tarjeta la recibe solo '
       'quien hace ese papel.',
    13: 'Acuerdo con Algorítmica 3.º antes del encuentro (guía, pág. %d): según lo que ya trabajó el curso se sigue la ruta A '
        'o la B de la sección 7.1.' % REF['acuerdo_algoritmica'],
    16: 'Tarjetas de rol para la sesión con usuarios simulados (guía, Parte III, sección 2).',
    19: 'Antes del encuentro: coordinación con Laboratorio (guía, pág. %d), prueba de campo y ficha de entorno E-1 a E-12 en '
        'las computadoras que se van a usar (guía, pág. %d) y las dos distribuciones de la base (guía, pág. %d). Lo que no se '
        'pudo probar se anota como pendiente.' % (REF['laboratorio_iv'], REF['ficha_entorno'], REF['distribuciones']),
    23: 'La simultaneidad se prueba con procesos independientes, no con dos pestañas: protocolo de concurrencia (guía, pág. %d).'
        % REF['concurrencia'],
    27: 'Antes del encuentro: copias descartables y cargador de datos de prueba (guía, pág. %d).' % REF['copias'],
    29: 'Confirmar con Laboratorio que en los equipos se puede respaldar y restaurar (guía, pág. %d).' % REF['laboratorio_v'],
    30: 'El docente prepara las copias de evaluación con el conjunto reservado DR, las cuentas, las tareas impresas y las '
        'planillas (guía, págs. %d-%d). El DR no se entrega ni se publica: se usa solo en esas copias.' % (REF['nota_e30'], REF['dr']),
    33: 'Paquete de entrega modelo, herramientas del docente y borrador de licencia (guía, págs. %d-%d); copias del paquete de '
        'Mbokaja para la Práctica 17 (guía, pág. %d).' % (REF['paquete_modelo'], REF['licencias'], REF['mbokaja_p17']),
    34: 'Armar las parejas de equipos antes del encuentro (guía, pág. %d). Un paquete recibido es código desconocido: sus '
        'pruebas se corren solo después de la inspección estática y en un equipo aislado (guía, pág. %d).' % (
            REF['instalacion_otro'], REF['codigo_recibido']),
    35: 'Preparación del Encuentro 35 (guía, pág. %d): guiones revisados, una variante del banco reservado por estudiante '
        '(guía, pág. %d), planillas impresas, paquetes instalados en la computadora de la demostración y orden calculado con '
        'la planilla de tiempos.' % (REF['tiempos_e35'], REF['variantes']),
    36: 'Si la planilla indicó la alternativa B, las defensas pendientes van al comienzo, antes de las recuperaciones (guía, '
        'pág. %d).' % REF['alternativas_e35'],
}


def orientaciones(e):
    n = e['num']
    texto = ' '.join(t['que_se_hace'] for t in e['tramos_guia']).lower()
    mods = []
    for pat, nombre in MODALIDADES:
        if re.search(pat, texto) and nombre not in mods:
            mods.append(nombre)
    out = []
    if mods:
        out.append('**Organización del trabajo** (según la secuencia de la guía): %s.' % ', '.join(mods))
    if n in PREPARACION:
        out.append('**Preparación.** ' + PREPARACION[n])
    if e['hito']:
        out.append('**Hito %s.** Imprimir la rúbrica y una planilla por estudiante; registrar por separado la evidencia del '
                   'equipo (60 %%) y la individual (40 %%) y, aparte, la ausencia de evidencia.' % e['hito'])
    p = e['practica']
    if p:
        if p['complemento']:
            out.append('**%s:** complemento editorial, fuera de las 5 HC: como tarea o actividad complementaria.' % p['titulo'])
        else:
            out.append('**Niveles de la práctica** (libro, pág. 6): el Nivel 1 es el piso que todo el curso alcanza, el Nivel 2 es '
                       'el esperado y el Nivel 3 es ampliación. Todos usan los mismos datos, distintos de los ejemplos.')
    if e['actividades_no_citadas']:
        out.append('**Actividades del libro que la secuencia de la guía no programa** (libro, desde la pág. %s): %s. Quedan a '
                   'criterio del docente como ampliación, preparación o tarea; no ocupan tiempo de las 5 HC.' % (
                       e['pagina_actividades'], '; '.join(act_txt(a, e['num']) for a in e['actividades_no_citadas'])))
    if e['errores']:
        out.append('**Errores frecuentes que conviene anticipar** (claves de la guía, pág. %d):' % e['guia']['claves_pagina'])
        out.append(('lista', ['Act. %s: %s' % (a, err) for a, err in e['errores']]))
    if e['calendario']:
        items, pg = e['calendario']
        out.append('**Si el calendario se acorta** (libro, pág. %s): %s' % (pg, ' '.join(items)))
    return out


def recursos(e):
    L = e['recursos_libro']
    por = lambda tipo: ['%s (pág. %s)' % (x['texto'], x['pagina']) for x in L if x['tipo'] == tipo]
    out = ['**Libro, págs. %s.** Secciones: %s.' % (pags(e['paginas_libro']), '; '.join(por('secciones')) or
                                                    'ninguna nueva; se usa el dossier o el prototipo de los encuentros anteriores')]
    for tipo, nombre in (('preliminares', 'Preliminares'), ('tablas', 'Tablas'), ('figuras', 'Figuras'), ('codigos', 'Códigos'), ('ejemplos', 'Ejemplos resueltos'), ('otros', 'Recuadros')):
        if por(tipo):
            out.append('**%s:** %s.' % (nombre, '; '.join(
                re.sub(r' — .*? \(pág', ' (pág', x) if tipo in ('tablas', 'figuras', 'codigos') else x for x in por(tipo))))
    if e['pagina_actividades']:
        out.append('**Actividades del Encuentro %d:** libro, desde la pág. %s.' % (e['num'], e['pagina_actividades']))
    p = e['practica']
    out.append('**Cuaderno de prácticas:** %s.' % ('%s, pág. %s' % (p['titulo'].split(' — ')[0], p['cuaderno']) if p else
                                                   'este encuentro no lo usa'))
    out.append('**Guía docente:** secuencia (pág. %d), claves (pág. %d)%s.' % (
        e['guia']['secuencia_pagina'], e['guia']['claves_pagina'],
        ''.join('; %s (pág. %d)' % (i['nombre'].split(' (')[0].lower(), i['pagina']) for i in e['instrumentos'][1:] if 'Claves de las actividades' not in i['nombre'])))
    comp = {None: 'No se usan computadoras.', 'equipo': 'Una computadora por equipo con el entorno del proyecto.',
            'demostracion': 'La computadora de la demostración, con el paquete de cada equipo instalado.',
            'recuperacion': 'Las computadoras que pida cada recuperación técnica; la retrospectiva no las necesita.'}
    out.append('**Equipamiento:** ' + comp[e['requiere_computadoras']])
    return out


def sin_computadoras(e):
    req = e['requiere_computadoras']
    if req is None:
        return ['No requiere computadoras: todo se hace con el libro, el cuaderno, papel y los materiales impresos de la guía.']
    out = []
    if req == 'equipo':
        out.append('**Si hay menos computadoras que equipos:** rotación documentada de los equipos, sin omitir evidencias '
                   'esenciales (guía, pág. %d).' % REF['nota_e30'])
        cod = [x['texto'].split(' — ')[0] for x in e['recursos_libro'] if x['tipo'] == 'codigos']
        tab = [x['texto'].split(' — ')[0] for x in e['recursos_libro'] if x['tipo'] == 'tablas']
        partes = ['**Si no funciona ningún entorno:** una sola computadora preparada por el docente para las demostraciones y las '
                  'pruebas, con la adaptación de 28 encuentros, y se registra como limitación (guía, pág. %d).' % REF['otro_entorno']]
        if cod:
            partes.append('Los equipos leen en el libro %s y explican qué requisito o contrato cumple cada uno.' % ', '.join(cod))
        if tab:
            partes.append('Completan en papel %s.' % ', '.join(tab))
        if e['pruebas'] or e['comandos']:
            partes.append('El docente ejecuta en su computadora %s y cada equipo registra el resultado esperado y el obtenido.'
                          % ', '.join(e['pruebas'] + e['comandos']))
        partes.append('Lo que exige trabajar en la computadora del equipo no se da por cumplido: ningún camino se declara '
                      'probado si no se probó. Queda registrado como pendiente para la recuperación técnica del Encuentro 32.'
                      if e['num'] < 32 else 'Ningún camino se declara probado si no se probó: lo que falte queda registrado '
                      'como pendiente del entorno, con el mensaje exacto.')
        out.append(' '.join(partes))
    elif req == 'demostracion':
        out.append('Basta la computadora de la demostración. Si falla, el equipo demuestra con su evidencia registrada y se '
                   'anota como limitación del entorno; la defensa individual no necesita computadora.')
    else:
        out.append('La retrospectiva y las recuperaciones de evidencia escrita no requieren computadoras; la recuperación de '
                   'una condición técnica usa la computadora del docente si no hay otra.')
    return out


def evaluacion(e):
    crit = ['Indicadores %s de la ficha del capítulo (arriba).' % ', '.join(str(i) for i, _ in e['indicadores']),
            'Evidencia: %s' % e['evidencia']]
    p = e['practica']
    if p and p['cotejo'] and not p['complemento']:
        crit.append('Lista de cotejo de la Práctica %d:' % p['num'])
        crit.append(('lista', ['%s (%s)' % (f[0], f[1]) for f in p['cotejo']['filas']]))
    if e['hito']:
        h = e['hito'][1]
        crit.append('Criterios de la rúbrica del %s: %s.' % (e['hito'], '; '.join(f[0] for f in MO.TAB['rubrica'][h]['filas'])))
    ins = [('lista', ['%s (guía, pág. %d)' % (i['nombre'], i['pagina']) for i in e['instrumentos']])]
    return [[[('lista', e['procedimientos'])], ins, crit]]


def vinculacion(e):
    g = e['guia']
    out = ['**Guía docente:** Parte %s, «%s» (pág. %d).' % (g['parte'], g['capitulo'], g['capitulo_pagina'])]
    p = e['practica']
    out.append('**Cuaderno:** %s.' % ('%s (pág. %s)' % (p['titulo'], p['cuaderno']) if p else 'sin práctica en este encuentro'))
    if e['hito']:
        hl = e['hito_libro']
        out.append('**Hito:** este encuentro es el %s, «%s» (libro, pág. %d).' % (e['hito'], hl['titulo'], hl['pagina']))
    elif e['proximo_hito'][0]:
        h, k = e['proximo_hito']
        out.append('**Hito:** prepara el %s del Encuentro %d.' % (h, k))
    else:
        out.append('**Cierre del año:** %s.' % ('demostración y defensa individual' if e['num'] == 35 else
                                                'recuperación, retrospectiva y evaluación integradora de la segunda etapa'))
    out.append('**Plan anual:** sección 6, Unidad %s, Capítulo %d, Encuentro %d.' % (e['unidad']['rom'], e['capitulo']['num'], e['num']))
    return out


# ---------------------------------------------------------------- un plan
def plan(d, e, primero):
    n = e['num']
    t = MP.titulo(d, 'Plan de Clase N.º %d — %s' % (n, e['titulo']), 1, nueva_pagina=not primero)
    b = d.add_paragraph(); MP.campo(b, 'institución')
    r = b.add_run('  ·  Plan de Clase N.º %d de 36  ·  Año lectivo ' % n); r.font.size = Pt(9.5)
    MP.campo(b, 'año de uso')
    tb = MP.tabla(d, None, [
        ['**Docente**', '', '**Disciplina**', DISCIPLINA],
        ['**Curso**', '3.º BTI', '**Tiempo**', '5 HC · Encuentro %d de 36 · %s' % (n, e['hc_guia'])],
        ['**Organizador curricular**', 'Unidad %s — %s · Capítulo %d — %s' % (e['unidad']['rom'], e['unidad']['titulo'],
                                                                             e['capitulo']['num'], e['capitulo']['titulo']),
         '**Sección y turno**', ''],
        ['**Material**', 'Libro, págs. %s · Cuaderno: %s · Guía, págs. %d y %d' % (
            pags(e['paginas_libro']), ('pág. %s' % e['practica']['cuaderno']) if e['practica'] else '—',
            e['guia']['secuencia_pagina'], e['guia']['claves_pagina']), '**Fecha**', ''],
        ['**Tema**', 'Foco del encuentro (Work §5.2): ' + e['foco'], '', ''],
    ], [3.0, 6.4, 2.4, MP.UTIL - 11.8], tam=8.5, encabezado=False)
    MP.campo(tb.rows[0].cells[1].paragraphs[0], 'nombre y apellido')
    MP.campo(tb.rows[2].cells[3].paragraphs[0], 'sección y turno')
    MP.campo(tb.rows[3].cells[3].paragraphs[0], 'fecha')
    for i in range(5):
        MP.sombrear(tb.rows[i].cells[0], MP.CLARO)
        if i < 4: MP.sombrear(tb.rows[i].cells[2], MP.CLARO)
    c = tb.rows[4].cells[1].merge(tb.rows[4].cells[3])
    for p in c.paragraphs[1:]:
        if not p.text: p._p.getparent().remove(p._p)

    f = e['ficha']
    MP.parrafo(d, '**%s**' % f['rotulo_capacidad'], 9, antes=5, seguir=True, color=MP.VERDE)
    for linea in f['capacidad'].split('\n'):
        MP.parrafo(d, linea, 9.5, despues=1)
    MP.parrafo(d, 'En este encuentro (Work §5.2): %s.' % e['capacidades_enc'], 9, italica=True)
    MP.parrafo(d, '**Indicadores de logro** (ficha del Capítulo %d, los que se evidencian en este encuentro):' % e['capitulo']['num'],
               9.5, antes=3, seguir=True, color=MP.VERDE)
    MP.lista(d, ['%d. %s' % (i, txt) for i, txt in e['indicadores']], 9.5)

    MP.parrafo(d, '**Momentos didácticos**', 10, antes=5, seguir=True, color=MP.VERDE)
    tm = MP.tabla(d, ['Momento', 'Actividades, explicaciones y orientaciones', 'Tiempo'], momentos(e), [2.2, MP.UTIL - 4.7, 2.5],
                  tam=8.5, dividir_filas=True)
    for row in tm.rows[1:]:
        MP.sombrear(row.cells[0], MP.CLARO)

    for titulo_, bloques in (('Orientaciones metodológicas', orientaciones(e)), ('Recursos', recursos(e)),
                             ('Si no hay computadoras disponibles', sin_computadoras(e))):
        MP.parrafo(d, '**%s**' % titulo_, 10, antes=5, seguir=True, color=MP.VERDE)
        for bl in bloques:
            if isinstance(bl, tuple):
                MP.lista(d, bl[1], 8.5)
            else:
                MP.parrafo(d, bl, 9, despues=1)

    MP.parrafo(d, '**Evaluación y evidencias de aprendizaje**', 10, antes=5, seguir=True, color=MP.VERDE)
    MP.tabla(d, ['Procedimientos', 'Instrumentos', 'Criterios y evidencias'], evaluacion(e), [4.6, 5.2, MP.UTIL - 9.8],
             tam=8.5, dividir_filas=True)
    MP.parrafo(d, '**Vinculación con la guía, el cuaderno y los hitos**', 10, antes=5, seguir=True, color=MP.VERDE)
    for v in vinculacion(e):
        MP.parrafo(d, v, 9, despues=1)
    MP.parrafo(d, 'Observaciones: ' + '_' * 86, 9, antes=6)
    fr = MP.parrafo(d, 'Docente ______________________________          Dirección — Visto bueno ______________________________',
                    9, antes=14, centro=True)


def paginas_planes(ruta_pdf):
    import pymupdf
    pdf = pymupdf.open(ruta_pdf)
    out = {}
    for i, pg in enumerate(pdf):
        for m in re.finditer(r'Plan de Clase N\.º (\d+) — ', pg.get_text()):
            out.setdefault(int(m.group(1)), i + 1)
    return out


def construir():
    """Dos vueltas: la primera calcula en qué página empieza cada plan; la segunda la escribe en la tabla inicial."""
    import json
    paginas = {}
    for vuelta in range(3):
        ruta = construir_doc(paginas)
        nuevas = paginas_planes(ruta.replace('.docx', '.pdf'))
        if nuevas == paginas:
            break
        paginas = nuevas
    else:
        raise SystemExit('las páginas de los planes no se estabilizaron')
    assert sorted(paginas) == list(range(1, 37))
    json.dump({str(k): v for k, v in paginas.items()}, open(os.path.join(AQUI, 'paginas_planes.json'), 'w'), indent=0)
    return ruta


def construir_doc(paginas):
    d = MP.documento()
    MP.F.identificacion(d, 'PLANES DE CLASE — 36 ENCUENTROS')
    MP.parrafo(d, VERSION + ' · Encuentros 1 a 36 · 5 HC por encuentro', 9.5, centro=True, antes=4)
    MP.recuadro(d, 'Cómo usar estos planes', [
        '**Versión para revisión, no definitiva:** se declara definitiva cuando la institución confirme el encuadre institucional '
        'y la carga horaria (plan anual, sección 1.3). La duración de la hora cátedra la fija la institución; los tiempos se '
        'dan en HC, como en la guía.',
        'Cada plan corresponde a un encuentro de la secuencia ordinaria de 36 y sigue la secuencia aprobada de la guía docente '
        '(tramos y tiempos), con la ficha del capítulo del libro sin cambios. Las capacidades son propuestas para el programa '
        'institucional del Plan Optativo; no son capacidades oficiales del MEC.',
        'Las consignas de las actividades se citan abreviadas: el texto completo está en el libro, en la página indicada. Las '
        'respuestas esperadas y los criterios están en la guía docente.',
        'En siete encuentros (18, 19, 26, 30, 32, 34 y 36) el primer tramo de la guía dura más de 1,5 HC: el inicio toma 0,5 HC '
        'de ese tramo para organizar la sesión, sin cambiar la suma. En el 35, todo el reparto lo calcula la planilla de tiempos.',
        'Si el calendario tiene menos encuentros, se usa la adaptación a 28 de la guía; estos planes no la reemplazan.',
    ])
    tabla_indice(d, paginas)
    for i, e in enumerate(E):
        plan(d, e, primero=False)
    MP.pie(d.sections[0], 'Análisis y Diseño de Sistemas · 3.º BTI · Edición 2026 · Planes de clase · %s' % VERSION)
    ruta = os.path.join(PLAN, NOMBRE + '.docx')
    d.save(ruta)
    MP.a_pdf(ruta, PLAN)
    return ruta


def tabla_indice(d, paginas):
    MP.parrafo(d, '**Planes de este documento**', 10, antes=6, seguir=True, color=MP.VERDE)
    MP.tabla(d, ['N.º', 'Encuentro', 'Unidad · capítulo', 'Libro, págs.', 'Hito', 'Página'],
             [[str(e['num']), e['titulo'], '%s · %d' % (e['unidad']['rom'], e['capitulo']['num']), pags(e['paginas_libro']),
               e['hito'] or '', str(paginas.get(e['num'], ''))] for e in E], [1.0, 8.6, 2.2, 2.6, 1.2, MP.UTIL - 15.6], tam=8)


if __name__ == '__main__':
    print(construir())

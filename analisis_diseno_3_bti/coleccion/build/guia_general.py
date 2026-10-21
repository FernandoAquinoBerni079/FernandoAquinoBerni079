# -*- coding: utf-8 -*-
"""Parte general de la guía docente anual (texto nuevo de la colección, declarado en la lista de diferencias).
Explica cómo se organiza la guía, de qué versión aprobada sale cada parte, dónde está cada instrumento del año, las
condiciones de seguridad para probar código recibido, los datos reservados y lo que sigue pendiente. No agrega ni
cambia teoría, claves, puntajes, indicadores ni soluciones: esos están en las partes, tal como se aprobaron."""
import fuentes as FU
import piezas_coleccion as PC
H, M, K = PC.H, PC.M, PC.K

TITULO = 'Parte general — Cómo usar esta guía anual'
SECCIONES = ['1. Organización de la guía, versión de cada parte y calendario', '2. Dónde está cada instrumento del año',
             '3. Seguridad: pruebas de código recibido de otros', '4. Datos reservados y variantes privadas',
             '5. Lo que sigue pendiente']

ORGANIZACION = [
    'Esta guía reúne, en seis partes, las guías docentes aprobadas de las seis unidades. Cada parte conserva lo que se '
    'aprobó: la secuencia de cada encuentro en HC, las claves de las actividades, de las prácticas y de las evaluaciones, '
    'las listas de cotejo, la rúbrica del hito, las referencias de código, el calendario de 28 encuentros y la '
    'procedencia de los recursos.',
    'La numeración de las secciones vuelve a empezar en cada parte. Para citar una sección se nombra la parte, por '
    'ejemplo «Parte IV, sección 2». Las tablas, figuras, códigos, ejemplos y actividades que se citan son los del libro '
    'del estudiante anual, con la misma numeración, y las páginas que se indican son las de ese libro.',
    'Las partes nombran a veces el «lote» y sus carpetas, por ejemplo lote_4/proyecto/. Esas menciones remiten a la '
    'carpeta del repositorio de cada unidad y a la versión aprobada que indica la tabla siguiente. Los archivos del '
    'prototipo están en esas carpetas y no cambiaron.',
]
CALENDARIO = [   # C-03 (cierre editorial)
    'El año tiene 36 encuentros ordinarios de 5 HC (180 HC). Es la secuencia de referencia del libro y de esta guía: cada '
    'capítulo ocupa dos encuentros y cada parte detalla la secuencia de los suyos.',
    'Para un año escolar con menos encuentros existe una adaptación alternativa a 28 encuentros. No reemplaza a la '
    'secuencia ordinaria: la institución elige una u otra según su calendario. Cada parte trae su adaptación en la '
    'sección «Calendario con menos encuentros», con la tabla de su unidad en 36 y en 28 encuentros, y cada capítulo del '
    'libro tiene su recuadro «Si el calendario se acorta». La tabla siguiente reúne lo que dicen las partes; no cambia '
    'ninguna de ellas.',
]
# (parte, encuentros ordinarios, encuentros en la adaptación) según la sección «Calendario con menos encuentros» de cada parte
CAL28 = {1: (6, 5), 2: (6, 4), 3: (6, 5), 4: (8, 5), 5: (6, 5), 6: (4, 4)}
assert sum(a for a, _ in CAL28.values()) == 36 and sum(b for _, b in CAL28.values()) == 28
ES_CALENDARIO = lambda rot: rot.startswith('Unidad ') and rot.endswith('en 36 y en 28 encuentros')
RESERVADOS = [
    'El conjunto de datos reservados DR (Unidad V) y las variantes definitivas V6 de la defensa individual (Unidad VI) son '
    'exclusivos del docente. No están en esta guía, ni en el libro, ni en el cuaderno, ni en el repositorio público, ni '
    'en los paquetes que reciben los estudiantes.',
    'Las Partes V (sección 0) y VI (sección 0.5) traen solo el procedimiento, la plantilla y los ejemplos públicos. El '
    'docente guarda sus archivos reservados en una carpeta privada y los comprueba con los validadores de cada unidad, que '
    'se niegan a usar una ruta dentro del repositorio.',
]
PENDIENTES = [
    'Las capacidades C1 a C10 son propuestas para el programa institucional del Plan Optativo. No son capacidades '
    'oficiales del MEC.',
    'El material no está validado en aulas. Las pruebas del prototipo y de las herramientas corrieron solo en el entorno '
    'de construcción (Linux). Siguen pendientes: Windows, las computadoras escolares, la instalación y la restauración en '
    'el laboratorio, la concurrencia real y la instalación por otro equipo, que hace el curso.',
    'El borrador de licencia de la Unidad VI está pendiente de revisión jurídica.',
]


def tabla_versiones():
    filas = []
    for n in range(1, 7):
        caps = FU.CAPITULOS[n]
        hc = 40 if n == 4 else (20 if n == 6 else 30)
        filas.append(['Parte %s' % FU.UNIDADES[n], '%d a %d' % (caps[0], caps[-1]), '%s (%d HC)' % (PC.ENCUENTROS[n], hc),
                      'Lote %d, %s' % (n, FU.VERSIONES[n])])
    return (['Parte', 'Capítulos', 'Encuentros', 'Guía aprobada de origen'], filas)


def construir(doc, instrumentos):
    """instrumentos: [(instrumento, parte, página de la guía)] de la vuelta anterior (vacío en la primera)."""
    K.titulo_en_pagina_nueva(doc, TITULO)
    doc.add_heading(SECCIONES[0], level=2)
    for t in ORGANIZACION:
        H.p_texto(doc, t)
    M.tabla(doc, tabla_versiones(), [2.2, 2.4, 3.6, 8.4], rotulo='Versión aprobada de cada parte')
    for t in CALENDARIO:
        H.p_texto(doc, t)
    pag_cal = {b: c for a, b, c in instrumentos if ES_CALENDARIO(a)}
    filas = [['Parte %s' % FU.UNIDADES[n], str(o), str(r), str(pag_cal.get(FU.UNIDADES[n], '—'))] for n, (o, r) in CAL28.items()]
    filas.append(['Total', '36', '28', ''])
    M.tabla(doc, (['Parte', 'Encuentros ordinarios', 'Encuentros en la adaptación', 'Página de la tabla'], filas),
            [3.4, 4.4, 4.8, 4.0], rotulo='Secuencia ordinaria de 36 encuentros y adaptación alternativa a 28')
    doc.add_heading(SECCIONES[1], level=2)
    H.p_texto(doc, 'Cada instrumento está en la parte de su unidad. La página es la de esta guía.')
    instrumentos = [x for x in instrumentos if not ES_CALENDARIO(x[0])]
    M.tabla(doc, (['Instrumento', 'Parte', 'Página'], [[a, b, str(c)] for a, b, c in instrumentos] or [['—', '—', '—']]),
            [11.6, 2.6, 2.4], rotulo='Instrumentos del año en esta guía', size=8.5)
    doc.add_heading(SECCIONES[2], level=2)
    for t in PC.NOTA_UNIDAD_VI[1]:
        H.p_texto(doc, t)
    H.p_texto(doc, 'El procedimiento completo está en la Parte VI (sección 0.1) y en lote_6/proyecto/herramientas/LEEME.md.')
    doc.add_heading(SECCIONES[3], level=2)
    for t in RESERVADOS:
        H.p_texto(doc, t)
    doc.add_heading(SECCIONES[4], level=2)
    for t in PENDIENTES:
        H.p_texto(doc, t)

# -*- coding: utf-8 -*-
"""Construye el lote 3 (Unidad III, Capítulos 7 a 9) en oficio O3: libro del estudiante, guía docente con solucionario
y cuaderno de prácticas, en DOCX, con PDF de control. Todo sale de las mismas fuentes: caso/ (diseño y Mbokaja U3,
que amplían sin modificarlas las fuentes de los lotes 1 y 2) y build/cap7.py a cap9.py (contenido).

Mismo ciclo que el lote 2: el índice se calcula sobre el PDF hasta que la paginación queda estable, y el control de
filas de la candidata O3 manda a hoja nueva el rótulo de toda tabla a la que le falte alguna fila.
Uso: python3 lote_3/build/construir.py   →  lote_3/ADS_3BTI_LOTE3_*.docx y .pdf"""
import os, sys, json
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
L3 = os.path.dirname(AQUI)
ADS = os.path.dirname(L3)
sys.path.insert(0, AQUI)
sys.path.insert(1, os.path.join(L3, 'caso'))
sys.path.insert(2, os.path.join(ADS, 'lote_2', 'build'))

import oficio as O
H, M, K = O.H, O.M, O.K
import piezas_u3 as Z
import diagramas_u3 as G
import cap7, cap8, cap9
import guia_u3
X, MB = Z.X, Z.MB
R, D, MO = X.R, X.D, X.MO

RUTA_EST = os.path.join(L3, 'ADS_3BTI_LOTE3_ESTUDIANTE_OFICIO_O3.docx')
RUTA_GUIA = os.path.join(L3, 'ADS_3BTI_LOTE3_GUIA_DOCENTE_OFICIO_O3.docx')
RUTA_CUAD = os.path.join(L3, 'ADS_3BTI_LOTE3_CUADERNO_PRACTICAS_OFICIO_O3.docx')
CAPS = (cap7, cap8, cap9)
UNIDAD_III = 'Unidad III — Diseñar una solución coherente'

ESTADO = [
    'Lote editorial 3 para auditoría independiente. No está aprobado para la venta ni para uso en aula; la aprobación '
    'final corresponde a Fernando y se hará sobre el conjunto completo.',
    'Sigue el índice del informe de Work v0.1: Unidad III (Capítulos 7 a 9, Encuentros 13 a 18). Formato oficio O3.',
    'Las capacidades C1 a C10 son propuestas para el programa institucional. No son capacidades oficiales del MEC. '
    'El entorno técnico del Capítulo 9 es un ejemplo provisional: no se probó todavía en equipos escolares.',
]


def apertura_unidad(doc):
    K.titulo_en_pagina_nueva(doc, UNIDAD_III)
    H.p_texto(doc, 'Resultado de la unidad (Work §5.1): modelo de datos, interacción y arquitectura revisados. Tres '
                   'capítulos, seis encuentros y 30 HC. La unidad parte del catálogo v1.1 y de los casos de uso de la '
                   'Unidad II, y cierra con el hito H3: el dossier de las Unidades I a III, consistente y defendido, con '
                   'evidencia individual.')
    M.tabla(doc, (['Capítulo', 'Encuentros', 'Evidencias (Work §5.2)'],
                  [['7. Datos que representan las reglas', '13 y 14', 'Obras/ediciones, ejemplares, lectores y préstamos; revisión del modelo con ejemplos y contraejemplos'],
                   ['8. Diseñar para las tareas de las personas', '15 y 16', 'Tres tareas completas en prototipo de baja fidelidad; registro de problemas y bocetos corregidos'],
                   ['9. Arquitectura y revisión del diseño', '17 y 18', 'Esquema de arquitectura y decisión técnica; H3: dossier consistente y evidencia individual']]),
            [5.4, 2.2, 9.0], rotulo='La Unidad III en un vistazo')
    H.caja(doc, 'Qué usa esta unidad de la Unidad II', [
        'El catálogo de requisitos en su versión 1.1, con la solicitud SC-01 ya aprobada (RF-11, tipo de lector, y la regla '
        'RN-02 modificada), las plantillas de los casos de uso CU-01 a CU-03 con sus flujos alternativos, la matriz de '
        'trazabilidad y las pruebas previstas P-01 a P-15. En las prácticas, la Escuela Básica Mbokaja sigue como caso de '
        'transferencia.'], tipo='neutra')


def practica(doc, C, cuerpo):
    K.titulo_en_pagina_nueva(doc, C.PRACTICA_TITULO)
    for t in C.PRACTICA_INTRO:
        H.p_texto(doc, t)
    cuerpo(doc)
    for nivel, items in C.NIVELES:
        M.actividades(doc, nivel, [('Consignas', items)])
    H.caja(doc, 'Punto de control', [C.PRACTICA_CONTROL], tipo='neutra')


def evaluacion(doc, C):
    H.evaluacion(doc, C.EVAL_ID, C.EVAL_TITULO, False, C.EVAL_TEXTO_BASE, C.EVAL_ITEMS,
                 remision='Evaluación opcional. Evalúa los indicadores del capítulo. ' + C.EVAL_PUNTAJE)


def _pares(*cods):
    return [(c, MB.FUENTES[c]) for c in cods]


# ---------------------------------------------------------------- prácticas (libro y cuaderno)
def cuerpo7(doc):
    Z.codigos(doc, MB.DATOS_TITULO, MB.DATOS)
    Z.codigos(doc, MB.SITUACIONES_TITULO, [s for s in MB.SITUACIONES if s[0] in ('MS-3', 'MS-4')])
    Z.codigos(doc, 'Datos de Mbokaja que vas a necesitar (caso de práctica, ficticio)',
              _pares('M-N1', 'M-N5', 'M-F5', 'M-F7', 'V-11', 'MC-1'))
    Z.Z2.catalogo_mbokaja(doc)


def cuerpo8(doc):
    M.tabla(doc, (['Código', 'Quién', 'Tarea', 'Qué se observó'], [list(o) for o in MB.OBSERVACIONES]),
            [1.6, 3.4, 3.4, 8.2], rotulo=MB.OBSERVACIONES_TITULO)
    Z.codigos(doc, 'Datos de Mbokaja que vas a necesitar (caso de práctica, ficticio)', _pares('MS-5', 'MN-05', 'MR-07'))


def cuerpo9(doc):
    Z.codigos(doc, 'Datos de Mbokaja que vas a necesitar (caso de práctica, ficticio)',
              _pares('MS-1', 'M-N5', 'M-F2', 'M-F3', 'M-F4', 'M-F7', 'M-F9', 'MR-02', 'MR-08'))


PRACTICAS = ((cap7, cuerpo7), (cap8, cuerpo8), (cap9, cuerpo9))


def ej(doc, e):
    H.caja(doc, e[0], e[1], tipo='neutra')


# ---------------------------------------------------------------- capítulo 7
def capitulo7(doc, figs):
    C = cap7
    K.encabezado_capitulo(doc, C)
    doc.add_heading(C.E13_TITULO, level=1)
    M.seccion(doc, C.S71)
    H.caja(doc, *C.FICHA_RECUPERACION, tipo='concepto')
    Z.tabla_leyenda(doc, 'der', C.LEYENDA_DER, figs)
    M.seccion(doc, C.S72)
    H.imagen(doc, figs['fig_7_1'], C.LEAD_FIG71, C.EPI_FIG71, ancho_cm=15.5)
    M.tabla(doc, C.TABLA_72, [2.0, 4.4, 3.4, 4.2, 2.6], rotulo=C.TABLA_72_ROTULO)
    H.imagen(doc, figs['fig_7_2'], C.LEAD_FIG72, C.EPI_FIG72, ancho_cm=13.5)
    ej(doc, C.EJ71)
    ej(doc, C.EJ72)
    M.actividades(doc, 'Actividades del Encuentro 13', C.ACT_E13)

    doc.add_heading(C.E14_TITULO, level=1)
    M.seccion(doc, C.S73)
    M.tabla(doc, C.TABLA_73, [1.6, 11.0, 4.0], rotulo=C.TABLA_73_ROTULO)
    H.imagen(doc, figs['fig_7_3'], C.LEAD_FIG73, C.EPI_FIG73, ancho_cm=15.5)
    M.tabla(doc, C.TABLA_74, [3.6, 5.0, 2.2, 5.8], rotulo=C.TABLA_74_ROTULO)
    M.tabla(doc, C.DICCIONARIO, [1.9, 2.7, 5.3, 2.1, 2.4, 2.2], rotulo=C.DICCIONARIO_ROTULO, size=8.5)
    ej(doc, C.EJ73)
    M.seccion(doc, C.S74)
    M.tabla(doc, C.TABLA_75, [4.0, 3.2, 6.2, 3.2], rotulo=C.TABLA_75_ROTULO)
    M.tabla(doc, C.TABLA_ANOM, [3.4, 5.6, 7.6], rotulo=C.TABLA_ANOM_ROTULO)
    ej(doc, C.EJ74)
    M.tabla(doc, C.TABLA_76, [3.2, 10.4, 3.0], rotulo=C.TABLA_76_ROTULO)
    M.actividades(doc, 'Actividades del Encuentro 14', C.ACT_E14)
    H.caja(doc, *C.REPASO, tipo='neutra')
    H.caja(doc, *C.CALENDARIO, tipo='neutra')
    practica(doc, C, cuerpo7)
    evaluacion(doc, C)


# ---------------------------------------------------------------- capítulo 8
def capitulo8(doc, figs):
    C = cap8
    K.encabezado_capitulo(doc, C)
    doc.add_heading(C.E15_TITULO, level=1)
    M.seccion(doc, C.S81)
    Z.tabla_leyenda(doc, 'navegacion', C.LEYENDA_NAV, figs)
    M.tabla(doc, C.TABLA_DIFERENCIAS, [3.6, 4.8, 3.8, 4.4], rotulo=C.TABLA_DIFERENCIAS_ROTULO)
    H.imagen(doc, figs['fig_8_1'], C.LEAD_FIG81, C.EPI_FIG81, ancho_cm=16.5)
    H.p_texto(doc, C.NOTA_MAPA, italic=True, size=9.5)
    M.tabla(doc, C.TABLA_PANTALLAS, [1.7, 3.4, 2.4, 6.5, 2.6], rotulo=C.TABLA_PANTALLAS_ROTULO)
    M.tabla(doc, C.TABLA_RECORRIDOS, [1.9, 1.2, 1.7, 5.9, 5.9], rotulo=C.TABLA_RECORRIDOS_ROTULO)
    ej(doc, C.EJ81)
    M.seccion(doc, C.S82)
    Z.tabla_leyenda(doc, 'boceto', C.LEYENDA_BOC, figs)
    H.imagen(doc, figs['fig_8_2'], C.LEAD_FIG82, C.EPI_FIG82, ancho_cm=16.5)
    ej(doc, C.EJ82)
    M.actividades(doc, 'Actividades del Encuentro 15', C.ACT_E15)

    doc.add_heading(C.E16_TITULO, level=1)
    M.seccion(doc, C.S83)
    H.imagen(doc, figs['fig_8_3'], C.LEAD_FIG83, C.EPI_FIG83, ancho_cm=15.5)
    M.tabla(doc, C.TABLA_MENSAJES, [1.6, 1.7, 2.2, 4.3, 6.8], rotulo=C.TABLA_MENSAJES_ROTULO, size=8.5)
    ej(doc, C.EJ83)
    M.seccion(doc, C.S84)
    M.tabla(doc, C.TABLA_ACC, [1.8, 14.8], rotulo=C.TABLA_ACC_ROTULO)
    M.tabla(doc, C.TABLA_OBS, [2.8, 5.0, 4.0, 4.8], rotulo=C.TABLA_OBS_ROTULO)
    ej(doc, C.EJ84)
    M.actividades(doc, 'Actividades del Encuentro 16', C.ACT_E16)
    H.caja(doc, *C.REPASO, tipo='neutra')
    H.caja(doc, *C.CALENDARIO, tipo='neutra')
    practica(doc, C, cuerpo8)
    evaluacion(doc, C)


# ---------------------------------------------------------------- capítulo 9
def capitulo9(doc, figs):
    import cap3   # lote_1/build/cap3.py: niveles de desempeño del H1 (Work §4.3), sin copiarlos
    C = cap9
    K.encabezado_capitulo(doc, C)
    doc.add_heading(C.E17_TITULO, level=1)
    M.seccion(doc, C.S91)
    Z.tabla_leyenda(doc, 'capas', C.LEYENDA_CAPAS, figs)
    H.imagen(doc, figs['fig_9_1'], C.LEAD_FIG91, C.EPI_FIG91, ancho_cm=14.5)
    M.tabla(doc, C.TABLA_92, [4.6, 3.8, 4.2, 4.0], rotulo=C.TABLA_92_ROTULO)
    M.seccion(doc, C.S92)
    M.tabla(doc, C.TABLA_93, [1.6, 3.4, 7.2, 4.4], rotulo=C.TABLA_93_ROTULO)
    ej(doc, C.EJ91)
    M.tabla(doc, C.TABLA_94, [2.8, 3.4, 6.6, 3.8], rotulo=C.TABLA_94_ROTULO)
    M.seccion(doc, C.S93)
    M.tabla(doc, C.TABLA_95, [3.8, 12.8], rotulo=C.TABLA_95_ROTULO)
    ej(doc, C.EJ92)
    M.seccion(doc, C.S94)
    M.tabla(doc, C.TABLA_96, [2.0, 4.6, 4.0, 3.6, 2.4], rotulo=C.TABLA_96_ROTULO, size=8.5)
    ej(doc, C.EJ93)
    M.actividades(doc, 'Actividades del Encuentro 17', C.ACT_E17)
    practica(doc, C, cuerpo9)

    K.titulo_en_pagina_nueva(doc, C.E18_TITULO)
    doc.add_heading(C.H3_TITULO, level=2)
    for t in C.H3_TEXTO:
        H.p_texto(doc, t)
    H.caja(doc, *C.H3_LISTA, tipo='neutra')
    H.caja(doc, *C.H3_EVALUACION, tipo='concepto')
    M.tabla(doc, (['Criterio del H3', 'Capacidades'], [[r[0], r[1]] for r in C.RUBRICA_H3]), [12.6, 4.0],
            rotulo='Criterios del H3 (la rúbrica completa está en la guía docente)')
    M.tabla(doc, (['Nivel de desempeño', 'Descriptor común'], [list(x) for x in cap3.NIVELES_DESEMPENO]), [3.6, 13.0],
            rotulo='Niveles de desempeño (propuesta editorial)')
    M.actividades(doc, 'Actividades del Encuentro 18', C.ACT_E18)
    H.caja(doc, *C.REPASO, tipo='neutra')
    H.caja(doc, *C.CALENDARIO, tipo='neutra')
    evaluacion(doc, C)


# ---------------------------------------------------------------- libro
ENCS = {cap7: (cap7.E13_TITULO, cap7.E14_TITULO), cap8: (cap8.E15_TITULO, cap8.E16_TITULO),
        cap9: (cap9.E17_TITULO, cap9.E18_TITULO)}


def entradas_indice():
    e = [(1, UNIDAD_III)]
    for C in CAPS:
        e.append((1, '%s — %s' % (C.CAPITULO, C.TITULO)))
        a, b = ENCS[C]; secs = list(C.SECCIONES)
        if C is cap9:
            e.append((2, a)); e += [(3, s) for s in secs]
            e.append((2, C.PRACTICA_TITULO))
            e.append((2, b)); e.append((3, cap9.H3_TITULO))
        else:
            e.append((2, a)); e += [(3, s) for s in secs[:2]]
            e.append((2, b)); e += [(3, s) for s in secs[2:]]
            e.append((2, C.PRACTICA_TITULO))
        e.append((2, C.EVAL_TITULO))
    return e


def libro_estudiante(figs, paginas=None):
    doc = H.new_doc()
    Z.portada(doc, 'Libro del estudiante', ESTADO)
    K.indice_marcador(doc)
    H.CLAVES.clear()
    apertura_unidad(doc)
    capitulo7(doc, figs)
    capitulo8(doc, figs)
    capitulo9(doc, figs)
    M.pegar_renglones(doc)
    Z.encadenar_inicio(doc)
    K.saltos_a_titulos(doc)
    K.rellenar_indice(doc, entradas_indice(), paginas or {})
    H.finalizar(doc, RUTA_EST)
    return list(H.CLAVES)


def construir_estudiante(figs):
    titulos = [t for _, t in entradas_indice()]
    paginas = {}
    for vuelta in range(6):
        claves = libro_estudiante(figs, paginas)
        pdf = K.a_pdf(RUTA_EST, L3)
        nuevas, total = K.paginas_de_titulos(pdf, titulos, desde=2)
        faltan = [t for t in titulos if t not in nuevas]
        assert not faltan, 'títulos del índice no encontrados en el PDF: %s' % faltan
        if nuevas == paginas:
            break
        paginas = nuevas
    else:
        raise AssertionError('la paginación del índice no se estabilizó')
    return claves, paginas, total


def cuaderno():
    doc = H.new_doc()
    Z.portada(doc, 'Cuaderno de prácticas', [
        'Extracción imprimible de las Prácticas 7, 8 y 9 del libro del estudiante, generada desde la misma fuente. '
        'No está aprobado para la venta ni para uso en aula; la aprobación final corresponde a Fernando.',
        'Cada práctica trabaja con datos que no aparecen en los ejemplos resueltos del libro. Tiene tres niveles que usan '
        'los mismos datos: tu docente te indica en cuál trabajar. Si el trabajo es un diagrama o un boceto, hacelo en una '
        'hoja aparte y adjuntala. Las tablas y figuras que se citan son las del libro del estudiante.',
        'La Práctica 9 es un complemento editorial al índice de Work: se hace en el Encuentro 17 o como actividad '
        'complementaria, y no reemplaza el H3.'])
    for C, cuerpo in PRACTICAS:
        practica(doc, C, cuerpo)
    M.pegar_renglones(doc)
    Z.encadenar_inicio(doc)
    K.saltos_a_titulos(doc)
    H.finalizar(doc, RUTA_CUAD)


if __name__ == '__main__':
    import pymupdf
    figs = G.generar()
    for vuelta in range(8):
        claves, paginas, total = construir_estudiante(figs)
        guia_u3.construir(RUTA_GUIA, claves, paginas, ESTADO, figs)
        pdf_g = K.a_pdf(RUTA_GUIA, L3)
        cuaderno()
        pdf_c = K.a_pdf(RUTA_CUAD, L3)
        nuevas = set()
        for dx, pdf in ((RUTA_EST, RUTA_EST[:-5] + '.pdf'), (RUTA_GUIA, pdf_g), (RUTA_CUAD, pdf_c)):
            inc = O.incompletas(dx, pdf)
            if inc:
                nuevas.add(inc[0])
        if not nuevas - O.HOJA_NUEVA:
            assert not nuevas, 'tablas que siguen perdiendo filas: %s' % nuevas
            break
        O.HOJA_NUEVA.update(nuevas)
    else:
        raise AssertionError('no se pudo evitar la pérdida de filas: %s' % O.HOJA_NUEVA)
    n_g, n_c = len(pymupdf.open(pdf_g)), len(pymupdf.open(pdf_c))
    print('Libro del estudiante: %d págs. · guía docente: %d págs. · cuaderno de prácticas: %d págs.' % (total, n_g, n_c))
    print('tablas que empiezan en hoja nueva para no perder filas:', sorted(O.HOJA_NUEVA))
    print('columnas ensanchadas para no partir palabras:', len(dict.fromkeys(O.AJUSTES)))
    json.dump({'perfil': O.PERFIL, 'ancho_util': O.ANCHO, 'tablas_en_hoja_nueva': sorted(O.HOJA_NUEVA),
               'columnas_ensanchadas': [{'tabla': a, 'columna': b, 'antes_cm': c, 'despues_cm': d} for a, b, c, d in dict.fromkeys(O.AJUSTES)],
               'paginas_libro': paginas, 'paginas': {'libro': total, 'guia': n_g, 'cuaderno': n_c}, 'claves': claves,
               'simbolos': G.REGISTRO},
              open(os.path.join(L3, 'resultado_construccion.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)

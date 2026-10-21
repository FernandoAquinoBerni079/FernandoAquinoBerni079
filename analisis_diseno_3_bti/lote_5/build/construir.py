# -*- coding: utf-8 -*-
"""Construye el lote 5 (Unidad V, Capítulos 14 a 16) en oficio O3: libro del estudiante, guía docente con solucionario
y cuaderno de prácticas, en DOCX, con PDF de control. Todo sale de las mismas fuentes: caso/ (verificación, datos de
prueba DP y Mbokaja U5, que amplían sin modificarlas las fuentes de los lotes 1 a 4), proyecto/ (los fragmentos de
código se leen de los archivos), resultados_pruebas/ (las tablas de resultados salen de la ejecución real, que hace
build/reproducir.py) y build/cap14.py a cap16.py (contenido).

Mismo ciclo que los lotes 2 a 4: el índice se calcula sobre el PDF hasta que la paginación queda estable, y el control
de filas de la candidata O3 manda a hoja nueva el rótulo de toda tabla a la que le falte alguna fila.
Uso: python3 lote_5/build/reproducir.py && python3 lote_5/build/construir.py  →  lote_5/ADS_3BTI_LOTE5_*.docx y .pdf"""
import os, sys, json
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
L5 = os.path.dirname(AQUI)
ADS = os.path.dirname(L5)
sys.path.insert(0, AQUI)
sys.path.insert(1, os.path.join(L5, 'caso'))
sys.path.insert(2, os.path.join(ADS, 'lote_4', 'build'))
sys.path.insert(3, os.path.join(ADS, 'lote_4', 'caso'))
sys.path.insert(4, os.path.join(ADS, 'lote_3', 'build'))
sys.path.insert(5, os.path.join(ADS, 'lote_3', 'caso'))
sys.path.insert(6, os.path.join(ADS, 'lote_2', 'build'))

import oficio as O
H, M, K = O.H, O.M, O.K
import piezas_u5 as Z
import diagramas_u5 as G
import cap14, cap15, cap16
import guia_u5
V = cap14.V
MB = cap14.MB

RUTA_EST = os.path.join(L5, 'ADS_3BTI_LOTE5_ESTUDIANTE_OFICIO_O3.docx')
RUTA_GUIA = os.path.join(L5, 'ADS_3BTI_LOTE5_GUIA_DOCENTE_OFICIO_O3.docx')
RUTA_CUAD = os.path.join(L5, 'ADS_3BTI_LOTE5_CUADERNO_PRACTICAS_OFICIO_O3.docx')
CAPS = (cap14, cap15, cap16)
UNIDAD_V = 'Unidad V — Verificar, validar y mejorar'

ESTADO = [
    'Lote editorial 5 para auditoría independiente. No está aprobado para la venta ni para uso en aula; la aprobación '
    'final corresponde a Fernando y se hará sobre la colección completa.',
    'Sigue el índice del informe de Work v0.1: Unidad V (Capítulos 14 a 16, Encuentros 27 a 32). Formato oficio O3.',
    'Las capacidades C1 a C10 son propuestas para el programa institucional. No son capacidades oficiales del MEC. '
    'Las pruebas que se informan corrieron solo en el entorno de construcción (Linux): no se probaron en las '
    'computadoras de ninguna institución ni en Windows, y eso se dice en cada resultado.',
]


def apertura_unidad(doc):
    K.titulo_en_pagina_nueva(doc, UNIDAD_V)
    H.p_texto(doc, 'Resultado de la unidad (Work §5.1): evidencia de pruebas, correcciones y aceptación. Tres capítulos, seis '
                   'encuentros y 30 HC. La unidad prueba el prototipo de la Unidad IV con datos independientes, lo hace '
                   'usar por otras personas, corrige lo que encuentra sin romper lo que andaba y cierra con el hito H5: la '
                   'versión candidata con sus límites conocidos.')
    M.tabla(doc, (['Capítulo', 'Encuentros', 'Evidencias (Work §5.2)'],
                  [['14. Probar con criterios y datos independientes', '27 y 28', 'Matriz con resultados esperados y requisitos cubiertos; resultados obtenidos e incidencias reproducibles'],
                   ['15. Probar el sistema completo con usuarios', '29 y 30', 'Evidencia del circuito completo y recuperación; observaciones de dos usuarios o roles y prioridades'],
                   ['16. Corregir y volver a comprobar', '31 y 32', 'Registro de regresión y trazabilidad actualizada; H5: versión candidata con límites conocidos']]),
            [5.4, 2.2, 9.0], rotulo='La Unidad V en un vistazo')
    Z.aviso_entorno(doc)
    H.caja(doc, 'Cómo se lee un resultado en esta unidad', [
        'Cada resultado lleva su condición: comprobado (se ejecutó y quedó registrado, con su entorno), reproducido (una '
        'incidencia que se volvió a provocar con pasos que se repiten), simulado (un dato de práctica) o pendiente (todavía '
        'no se probó). Lo que no se probó no se da por bueno.',
        'Las tablas de resultados del equipo modelo salen de una ejecución real sobre copias descartables, en el entorno de '
        'construcción de este libro. Las de tu equipo salen de tus propias ejecuciones.'], tipo='neutra')
    H.caja(doc, 'Las copias descartables', [
        'Todas las pruebas de la unidad se hacen sobre copias: el cargador de datos de prueba crea una carpeta nueva con el '
        'código de tu base y una base con datos ficticios. La base de la clase y la del lote anterior no cambian.',
        'Las cuentas son de demostración y sus claves se generan al azar en cada copia. No se usan datos personales reales.'],
        tipo='neutra')


def practica(doc, C_, cuerpo):
    K.titulo_en_pagina_nueva(doc, C_.PRACTICA_TITULO)
    for t in C_.PRACTICA_INTRO:
        H.p_texto(doc, t)
    cuerpo(doc)
    for nivel, items in C_.NIVELES:
        M.actividades(doc, nivel, [('Consignas', items)])
    H.caja(doc, 'Punto de control', [C_.PRACTICA_CONTROL], tipo='neutra')


def evaluacion(doc, C_):
    H.evaluacion(doc, C_.EVAL_ID, C_.EVAL_TITULO, False, C_.EVAL_TEXTO_BASE, C_.EVAL_ITEMS,
                 remision='Evaluación opcional. Evalúa los indicadores del capítulo. ' + C_.EVAL_PUNTAJE)


def ej(doc, e):
    H.caja(doc, e[0], e[1], tipo='neutra')


def codigos_de(doc, C_, ids):
    for fid in ids:
        Z.codigo(doc, fid, C_.EXPLICA[fid])


def nota(doc, texto):
    H.p_texto(doc, texto, italic=True, size=9.5)


# ---------------------------------------------------------------- prácticas (libro y cuaderno)
def filas_p14():
    d = MB.P14
    obra = {o[0]: o[1] for o in d['obras']}
    ed = {e[0]: e[1] for e in d['ediciones']}
    filas = [['Obras', ' · '.join('%s «%s»' % (o[0], o[1]) for o in d['obras'])],
             ['Ejemplares', ' · '.join('%s (%s%s)' % (x[0], obra[ed[x[1]]], '' if x[2] else ', dado de baja') for x in d['ejemplares'])],
             ['Lectores', ' · '.join('%s (%s%s)' % (l[0], l[2], ', ' + l[3] if l[3] else '') for l in d['lectores'])]]
    for p in d['prestamos']:
        filas.append(['Préstamo', '%s a %s: salió el %s, vence el %s%s' % (
            p[0], p[1], X_fecha(p[3]), X_fecha(p[4]), ', devuelto el %s' % X_fecha(p[5]) if p[5] else ', activo')])
    filas.append(['Fecha de referencia', X_fecha(d['fecha_referencia'])])
    return (['Dato', 'Qué carga la copia de práctica'], filas)


def X_fecha(iso):
    a, m, d = iso.split('-')
    return '%s/%s/%s' % (d, m, a)


def cuerpo14(doc):
    Z.codigos(doc, MB.DATOS_TITULO, MB.DATOS)
    Z.codigos(doc, MB.SITUACIONES_TITULO, MB.SITUACIONES)
    M.tabla(doc, filas_p14(), [3.4, 13.2], rotulo='Datos de la copia de práctica de Mbokaja (mbokaja_p14.json, ficticios)')


def cuerpo15(doc):
    M.tabla(doc, cap15.PLANTILLA, [4.4, 12.2], rotulo=cap15.PLANTILLA_ROTULO)


PRACTICAS = ((cap14, cuerpo14), (cap15, cuerpo15))


# ---------------------------------------------------------------- capítulo 14
def capitulo14(doc, figs):
    C_ = cap14
    K.encabezado_capitulo(doc, C_)
    Z.aviso_entorno(doc)
    doc.add_heading(C_.E27_TITULO, level=1)
    M.seccion(doc, C_.S141)
    M.tabla(doc, C_.TABLA_141, [4.4, 4.0, 8.2], rotulo=C_.TABLA_141_ROTULO)
    ej(doc, C_.EJ141)
    M.seccion(doc, C_.S142)
    M.tabla(doc, C_.TABLA_142, [3.0, 13.6], rotulo=C_.TABLA_142_ROTULO)
    H.imagen(doc, figs['fig_14_1'], C_.LEAD_FIG141, C_.EPI_FIG141, ancho_cm=16.0)
    M.tabla(doc, C_.TABLA_143, [3.2, 8.4, 5.0], rotulo=C_.TABLA_143_ROTULO)
    M.tabla(doc, C_.TABLA_144, [2.4, 9.4, 4.8], rotulo=C_.TABLA_144_ROTULO)
    H.caja(doc, *C_.COPIA, tipo='concepto')
    ej(doc, C_.EJ142)
    M.actividades(doc, 'Actividades del Encuentro 27', C_.ACT_E27)

    doc.add_heading(C_.E28_TITULO, level=1)
    M.seccion(doc, C_.S143)
    M.tabla(doc, C_.TABLA_145, [3.0, 13.6], rotulo=C_.TABLA_145_ROTULO)
    M.tabla(doc, C_.tabla_146(), [1.4, 1.6, 1.8, 4.8, 4.4, 2.6], rotulo=C_.TABLA_146_ROTULO, size=8)
    nota(doc, C_.NOTA_146 % V.entorno_texto())
    ej(doc, C_.EJ143)
    M.seccion(doc, C_.S144)
    M.tabla(doc, C_.tabla_147(), [1.6, 2.4, 3.6, 2.4, 6.6], rotulo=C_.TABLA_147_ROTULO, size=8.5)
    H.imagen(doc, figs['fig_14_2'], C_.LEAD_FIG142, C_.EPI_FIG142, ancho_cm=16.0)
    M.tabla(doc, C_.TABLA_148, [3.6, 13.0], rotulo=C_.TABLA_148_ROTULO)
    M.tabla(doc, C_.TABLA_149, [1.8, 1.6, 5.0, 2.2, 6.0], rotulo=C_.TABLA_149_ROTULO, size=8.5)
    M.actividades(doc, 'Actividades del Encuentro 28', C_.ACT_E28)
    H.caja(doc, *C_.REPASO, tipo='neutra')
    H.caja(doc, *C_.CALENDARIO, tipo='neutra')
    practica(doc, C_, cuerpo14)
    evaluacion(doc, C_)


# ---------------------------------------------------------------- capítulo 15
def capitulo15(doc, figs):
    C_ = cap15
    K.encabezado_capitulo(doc, C_)
    Z.aviso_entorno(doc)
    doc.add_heading(C_.E29_TITULO, level=1)
    M.seccion(doc, C_.S151)
    M.tabla(doc, C_.tabla_151(), [3.0, 6.4, 4.6, 2.6], rotulo=C_.TABLA_151_ROTULO)
    nota(doc, C_.NOTA_151 % V.entorno_texto())
    M.seccion(doc, C_.S152)
    M.tabla(doc, C_.tabla_152(), [3.6, 4.2, 4.4, 4.4], rotulo=C_.TABLA_152_ROTULO)
    ej(doc, C_.EJ151)
    M.actividades(doc, 'Actividades del Encuentro 29', C_.ACT_E29)

    doc.add_heading(C_.E30_TITULO, level=1)
    M.seccion(doc, C_.S153)
    M.tabla(doc, C_.SESIONES, [1.2, 2.6, 3.6, 5.0, 2.4, 1.8], rotulo=C_.SESIONES_ROTULO, size=8.5)
    nota(doc, V.SESIONES_NOTA)
    H.caja(doc, *C_.PERSONA_REAL, tipo='concepto')
    M.seccion(doc, C_.S154)
    M.tabla(doc, C_.tabla_154(), [1.6, 8.0, 4.4, 2.6], rotulo=C_.TABLA_154_ROTULO, size=8.5)
    M.tabla(doc, C_.TABLA_155, [1.8, 2.4, 3.6, 1.6, 7.2], rotulo=C_.TABLA_155_ROTULO)
    ej(doc, C_.EJ152)
    M.actividades(doc, 'Actividades del Encuentro 30', C_.ACT_E30)
    H.caja(doc, *C_.REPASO, tipo='neutra')
    H.caja(doc, *C_.CALENDARIO, tipo='neutra')
    practica(doc, C_, cuerpo15)
    evaluacion(doc, C_)


# ---------------------------------------------------------------- capítulo 16
def capitulo16(doc, figs):
    import cap3   # lote_1/build/cap3.py: niveles de desempeño de los hitos (Work §4.3), sin copiarlos
    C_ = cap16
    r = V.resumen()
    K.encabezado_capitulo(doc, C_)
    Z.aviso_entorno(doc)
    doc.add_heading(C_.E31_TITULO, level=1)
    M.seccion(doc, C_.S161)
    H.imagen(doc, figs['fig_16_1'], C_.LEAD_FIG161, C_.EPI_FIG161, ancho_cm=16.0)
    M.tabla(doc, C_.TABLA_161, [4.2, 2.4, 1.4, 4.4, 4.2], rotulo=C_.TABLA_161_ROTULO, size=8.5)
    ej(doc, C_.EJ161)
    M.seccion(doc, C_.S162)
    codigos_de(doc, C_, C_.CODIGOS_S162)
    M.tabla(doc, C_.TABLA_162, [8.0, 8.6], rotulo=C_.TABLA_162_ROTULO)
    M.tabla(doc, C_.tabla_163(), [6.6, 10.0], rotulo=C_.TABLA_163_ROTULO)
    nota(doc, C_.NOTA_163 % (r['in02']['lote4'].replace('Resultado: ', ''), V.entorno_texto()))
    ej(doc, C_.EJ162)
    M.seccion(doc, C_.S163)
    M.tabla(doc, C_.TABLA_164, [3.6, 13.0], rotulo=C_.TABLA_164_ROTULO)
    codigos_de(doc, C_, C_.CODIGOS_S163)
    M.tabla(doc, C_.tabla_165(), [6.6, 10.0], rotulo=C_.TABLA_165_ROTULO)
    M.tabla(doc, C_.TABLA_166, [1.8, 3.6, 4.0, 3.8, 3.4], rotulo=C_.TABLA_166_ROTULO, size=8.5)
    M.actividades(doc, 'Actividades del Encuentro 31', C_.ACT_E31)

    K.titulo_en_pagina_nueva(doc, C_.E32_TITULO)
    M.seccion(doc, C_.S164)
    M.tabla(doc, C_.tabla_167(), [5.0, 8.0, 3.6], rotulo=C_.TABLA_167_ROTULO)
    M.tabla(doc, C_.TABLA_168, [7.0, 2.4, 7.2], rotulo=C_.TABLA_168_ROTULO)
    H.caja(doc, *C_.RECUPERACION, tipo='concepto')
    doc.add_heading(C_.H5_TITULO, level=2)
    for t in C_.H5_TEXTO:
        H.p_texto(doc, t)
    H.caja(doc, *C_.H5_LISTA, tipo='neutra')
    H.caja(doc, *C_.H5_EVALUACION, tipo='concepto')
    M.tabla(doc, (['Criterio del H5', 'Capacidad'], [[x[0], x[1]] for x in C_.RUBRICA_H5]), [12.6, 4.0],
            rotulo='Criterios del H5 (la rúbrica completa está en la guía docente)')
    M.tabla(doc, (['Nivel de desempeño', 'Descriptor común'], [list(x) for x in cap3.NIVELES_DESEMPENO]), [3.6, 13.0],
            rotulo='Niveles de desempeño (propuesta editorial)')
    M.actividades(doc, 'Actividades del Encuentro 32', C_.ACT_E32)
    H.caja(doc, *C_.REPASO, tipo='neutra')
    H.caja(doc, *C_.CALENDARIO, tipo='neutra')
    evaluacion(doc, C_)


# ---------------------------------------------------------------- libro
ENCS = {cap14: (cap14.E27_TITULO, cap14.E28_TITULO), cap15: (cap15.E29_TITULO, cap15.E30_TITULO),
        cap16: (cap16.E31_TITULO, cap16.E32_TITULO)}


def entradas_indice():
    e = [(1, UNIDAD_V)]
    for C_ in CAPS:
        e.append((1, '%s — %s' % (C_.CAPITULO, C_.TITULO)))
        a, b = ENCS[C_]; secs = list(C_.SECCIONES)
        corte = 3 if C_ is cap16 else 2
        e.append((2, a)); e += [(3, s) for s in secs[:corte]]
        e.append((2, b)); e += [(3, s) for s in secs[corte:]]
        if C_ is cap16:
            e.append((3, cap16.H5_TITULO))
        else:
            e.append((2, C_.PRACTICA_TITULO))
        e.append((2, C_.EVAL_TITULO))
    return e


def libro_estudiante(figs, paginas=None):
    doc = H.new_doc()
    Z.portada(doc, 'Libro del estudiante', ESTADO)
    K.indice_marcador(doc)
    H.CLAVES.clear()
    apertura_unidad(doc)
    capitulo14(doc, figs)
    capitulo15(doc, figs)
    capitulo16(doc, figs)
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
        pdf = K.a_pdf(RUTA_EST, L5)
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
        'Extracción imprimible de las Prácticas 14 y 15 del libro del estudiante, generada desde la misma fuente. '
        'No está aprobado para la venta ni para uso en aula; la aprobación final corresponde a Fernando.',
        'La Práctica 14 trabaja con datos de Mbokaja que no aparecen en los ejemplos resueltos del libro. La Práctica 15 usa '
        'datos reservados que entrega el docente en el momento: no están en este cuaderno. Cada práctica tiene tres niveles: '
        'tu docente te indica en cuál trabajar.',
        'El Capítulo 16 no tiene práctica: su actividad integradora es el hito H5, que está en el libro.'])
    for C_, cuerpo in PRACTICAS:
        practica(doc, C_, cuerpo)
    M.pegar_renglones(doc)
    Z.encadenar_inicio(doc)
    K.saltos_a_titulos(doc)
    H.finalizar(doc, RUTA_CUAD)


if __name__ == '__main__':
    import pymupdf
    figs = G.generar(os.path.join(AQUI, 'figs'))
    for vuelta in range(8):
        claves, paginas, total = construir_estudiante(figs)
        guia_u5.construir(RUTA_GUIA, claves, paginas, ESTADO, figs)
        pdf_g = K.a_pdf(RUTA_GUIA, L5)
        cuaderno()
        pdf_c = K.a_pdf(RUTA_CUAD, L5)
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
              open(os.path.join(L5, 'resultado_construccion.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)

# -*- coding: utf-8 -*-
"""Construye el lote 4 (Unidad IV, Capítulos 10 a 13) en oficio O3: libro del estudiante, guía docente con solucionario
y cuaderno de prácticas, en DOCX, con PDF de control. Todo sale de las mismas fuentes: caso/ (construcción y Mbokaja
U4, que amplían sin modificarlas las fuentes de los lotes 1 a 3), proyecto/ (los fragmentos de código se leen de los
archivos) y build/cap10.py a cap13.py (contenido).

Mismo ciclo que los lotes 2 y 3: el índice se calcula sobre el PDF hasta que la paginación queda estable, y el control
de filas de la candidata O3 manda a hoja nueva el rótulo de toda tabla a la que le falte alguna fila.
Uso: python3 lote_4/build/construir.py   →  lote_4/ADS_3BTI_LOTE4_*.docx y .pdf"""
import os, sys, json
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
L4 = os.path.dirname(AQUI)
ADS = os.path.dirname(L4)
sys.path.insert(0, AQUI)
sys.path.insert(1, os.path.join(L4, 'caso'))
sys.path.insert(2, os.path.join(ADS, 'lote_3', 'build'))
sys.path.insert(3, os.path.join(ADS, 'lote_3', 'caso'))
sys.path.insert(4, os.path.join(ADS, 'lote_2', 'build'))

import oficio as O
H, M, K = O.H, O.M, O.K
import piezas_u4 as Z
import diagramas_u4 as G
import cap10, cap11, cap12, cap13
import guia_u4
C, X = Z.C, Z.X
MB = cap10.MB

RUTA_EST = os.path.join(L4, 'ADS_3BTI_LOTE4_ESTUDIANTE_OFICIO_O3.docx')
RUTA_GUIA = os.path.join(L4, 'ADS_3BTI_LOTE4_GUIA_DOCENTE_OFICIO_O3.docx')
RUTA_CUAD = os.path.join(L4, 'ADS_3BTI_LOTE4_CUADERNO_PRACTICAS_OFICIO_O3.docx')
CAPS = (cap10, cap11, cap12, cap13)
UNIDAD_IV = 'Unidad IV — Construir el prototipo por incrementos'

ESTADO = [
    'Lote editorial 4 para auditoría independiente. No está aprobado para la venta ni para uso en aula; la aprobación '
    'final corresponde a Fernando y se hará sobre la colección completa.',
    'Sigue el índice del informe de Work v0.1: Unidad IV (Capítulos 10 a 13, Encuentros 19 a 26). Formato oficio O3.',
    'Las capacidades C1 a C10 son propuestas para el programa institucional. No son capacidades oficiales del MEC. '
    'El entorno técnico (HTML y CSS, PHP y SQLite) es una referencia provisional: no se probó en las computadoras de '
    'ninguna institución ni en Windows. Las pruebas de la base corrieron solo en el entorno de construcción.',
]


def apertura_unidad(doc):
    K.titulo_en_pagina_nueva(doc, UNIDAD_IV)
    H.p_texto(doc, 'Resultado de la unidad (Work §5.1): circuito funcional integrado y persistente. Cuatro capítulos, ocho '
                   'encuentros y 40 HC. La unidad construye el prototipo por incrementos, con el diseño de la Unidad III '
                   'tal como quedó en su versión 1.1, y cierra con el hito H4: el prototipo mínimo completo y la lista de '
                   'incidencias.')
    M.tabla(doc, (['Capítulo', 'Encuentros', 'Evidencias (Work §5.2)'],
                  [['10. Del diseño a la primera operación funcional', '19 y 20', 'Ejecución inicial reproducible y ficha de entorno; formulario-servidor-base de datos y prueba de persistencia'],
                   ['11. Catálogo, ejemplares y lectores', '21 y 22', 'Alta, consulta y edición con reglas de validación; validación en el servidor y rechazo de acceso indebido'],
                   ['12. Préstamos y devoluciones consistentes', '23 y 24', 'Operación coherente ante reenvío o segunda solicitud; devolución única, conservación de referencias y pruebas'],
                   ['13. Información útil e integración', '25 y 26', 'Reporte correcto con fecha de referencia definida; H4: prototipo completo mínimo y lista de incidencias']]),
            [5.4, 2.2, 9.0], rotulo='La Unidad IV en un vistazo')
    Z.aviso_entorno(doc)
    H.caja(doc, 'Qué usa esta unidad de la Unidad III', [
        'El diseño en su versión 1.1: el modelo de datos con sus restricciones RI-01 a RI-08, las pantallas PT-01 a PT-09 '
        'con sus zonas (PT-09 en la zona «Bibliotecaria o dirección»), los mensajes ME-01 a ME-13 (ME-12 solo para el '
        'ingreso y ME-13 para la falta de permiso) y los contratos de OP-01 a OP-06. Nada de eso cambia: se construye.',
        'Las operaciones auxiliares que necesita la pantalla PT-08 (altas y correcciones, OA-01 a OA-05) tienen su propio '
        'contrato y su propia prueba (PA-01 a PA-05), y mensajes propios (MA y MV).'], tipo='neutra')
    H.caja(doc, 'La base de proyecto', [
        'Tu equipo trabaja con la base del estudiante: trae la estructura, la conexión, el esquema, el ingreso del personal, '
        'los permisos por zona, la instalación, el respaldo y la restauración. Las operaciones las construye el equipo, '
        'capítulo por capítulo. Tu docente tiene además la referencia docente, con el sistema completo, para comparar y '
        'para las pruebas.',
        'Los datos de la base son ficticios y las cuentas son de demostración: sus claves se reemplazan antes de usar el '
        'sistema con datos que no sean de prueba.'], tipo='neutra')


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


def _pares(*cods):
    return [(c, MB.FUENTES[c]) for c in cods]


DATOS_MB = 'Datos de Mbokaja que vas a necesitar (caso de práctica, ficticio)'


# ---------------------------------------------------------------- prácticas (libro y cuaderno)
def cuerpo10(doc):
    Z.codigos(doc, MB.DATOS_TITULO, MB.DATOS)
    Z.codigos(doc, DATOS_MB, _pares('M-F4', 'M-F7', 'M-F9', 'MR-05', 'MR-08'))


def cuerpo11(doc):
    M.tabla(doc, (['Código', 'Etiqueta', 'Título en la planilla', 'Autor', 'Observación'],
                  [[c, e, t, a or '(vacío)', o or '—'] for c, e, t, a, o in MB.LOTE]),
            [1.7, 2.0, 4.6, 4.3, 4.0], rotulo=MB.LOTE_TITULO)
    Z.codigos(doc, MB.LECTORES_TITULO, MB.LECTORES)
    Z.codigos(doc, DATOS_MB, _pares('M-F11', 'MS-5', 'MN-05'))
    M.tabla(doc, (['Dato de Mbokaja', 'Cómo se escribe en la copia de práctica', 'Por qué'], [list(c) for c in MB.CORRESPONDENCIA]),
            [4.6, 5.6, 6.4], rotulo=MB.CORRESPONDENCIA_TITULO)
    M.tabla(doc, (['Nivel', 'Dónde se hace', 'Qué se hace'], [list(e) for e in MB.EJECUCION]), [2.2, 5.0, 9.4],
            rotulo=MB.EJECUCION_TITULO)


def cuerpo12(doc):
    Z.codigos(doc, MB.SITUACIONES_TITULO, MB.SITUACIONES)
    Z.codigos(doc, DATOS_MB, _pares('MS-1', 'M-N5', 'OBS-4', 'MR-04'))


def cuerpo13(doc):
    Z.codigos(doc, MB.SEMANA_TITULO, MB.SEMANA)
    Z.codigos(doc, DATOS_MB, _pares('M-N1', 'M-F8'))


PRACTICAS = ((cap10, cuerpo10), (cap11, cuerpo11), (cap12, cuerpo12), (cap13, cuerpo13))


def ej(doc, e):
    H.caja(doc, e[0], e[1], tipo='neutra')


def codigos_de(doc, C_, ids):
    for fid in ids:
        Z.codigo(doc, fid, C_.EXPLICA[fid])


# ---------------------------------------------------------------- capítulo 10
def capitulo10(doc, figs):
    C_ = cap10
    K.encabezado_capitulo(doc, C_)
    Z.aviso_entorno(doc)
    doc.add_heading(C_.E19_TITULO, level=1)
    M.seccion(doc, C_.S101)
    M.tabla(doc, C_.FICHA, [1.4, 3.6, 7.4, 4.2], rotulo=C_.FICHA_ROTULO, size=8.5)
    H.imagen(doc, figs['fig_10_1'], C_.LEAD_FIG101, C_.EPI_FIG101, ancho_cm=15.5)
    M.tabla(doc, C_.TABLA_102, [4.6, 4.8, 5.0, 2.2], rotulo=C_.TABLA_102_ROTULO)
    H.caja(doc, *C_.FICHA_RECUPERACION, tipo='concepto')
    ej(doc, C_.EJ101)
    M.seccion(doc, C_.S102)
    M.tabla(doc, C_.TABLA_103, [2.2, 5.6, 6.2, 2.6], rotulo=C_.TABLA_103_ROTULO)
    M.tabla(doc, C_.TABLA_104, [2.2, 6.6, 2.6, 2.6, 2.6], rotulo=C_.TABLA_104_ROTULO)
    M.tabla(doc, C_.BITACORA, [3.6, 13.0], rotulo=C_.BITACORA_ROTULO)
    ej(doc, C_.EJ102)
    M.actividades(doc, 'Actividades del Encuentro 19', C_.ACT_E19)

    doc.add_heading(C_.E20_TITULO, level=1)
    M.seccion(doc, C_.S103)
    Z.contrato_aux(doc, 'OA-01')
    H.imagen(doc, figs['fig_10_2'], C_.LEAD_FIG102, C_.EPI_FIG102, ancho_cm=16.0)
    codigos_de(doc, C_, C_.CODIGOS_E20)
    ej(doc, C_.EJ103)
    M.seccion(doc, C_.S104)
    codigos_de(doc, C_, C_.CODIGOS_S104)
    M.tabla(doc, C.tabla_pa01(), [1.8, 7.6, 2.2, 5.0], rotulo=C_.TABLA_106_ROTULO)
    ej(doc, C_.EJ104)
    M.actividades(doc, 'Actividades del Encuentro 20', C_.ACT_E20)
    H.caja(doc, *C_.REPASO, tipo='neutra')
    H.caja(doc, *C_.CALENDARIO, tipo='neutra')
    practica(doc, C_, cuerpo10)
    evaluacion(doc, C_)


# ---------------------------------------------------------------- capítulo 11
def capitulo11(doc, figs):
    C_ = cap11
    K.encabezado_capitulo(doc, C_)
    Z.aviso_entorno(doc)
    doc.add_heading(C_.E21_TITULO, level=1)
    M.seccion(doc, C_.S111)
    M.tabla(doc, C_.TABLA_111, [1.0, 5.0, 2.2, 2.0, 3.4, 3.0], rotulo=C_.TABLA_111_ROTULO, size=8.5)
    for op in C_.CONTRATOS_E21:
        Z.contrato_aux(doc, op)
    M.seccion(doc, C_.S112)
    M.tabla(doc, C_.TABLA_112, [4.6, 4.4, 3.8, 3.8], rotulo=C_.TABLA_112_ROTULO)
    Z.contrato_aux(doc, 'OA-03')
    ej(doc, C_.EJ111)
    ej(doc, C_.EJ112)
    M.actividades(doc, 'Actividades del Encuentro 21', C_.ACT_E21)

    doc.add_heading(C_.E22_TITULO, level=1)
    M.seccion(doc, C_.S113)
    codigos_de(doc, C_, C_.CODIGOS_S113)
    M.tabla(doc, C_.TABLA_113, [7.0, 3.2, 3.2, 3.2], rotulo=C_.TABLA_113_ROTULO)
    ej(doc, C_.EJ113)
    M.seccion(doc, C_.S114)
    Z.contrato_aux(doc, 'OA-04')
    Z.contrato(doc, 'OP-06')
    codigos_de(doc, C_, C_.CODIGOS_S114)
    M.tabla(doc, C_.TABLA_114, [4.4, 2.8, 3.0, 6.4], rotulo=C_.TABLA_114_ROTULO)
    ej(doc, C_.EJ114)
    M.actividades(doc, 'Actividades del Encuentro 22', C_.ACT_E22)
    H.caja(doc, *C_.REPASO, tipo='neutra')
    H.caja(doc, *C_.CALENDARIO, tipo='neutra')
    practica(doc, C_, cuerpo11)
    evaluacion(doc, C_)


# ---------------------------------------------------------------- capítulo 12
def capitulo12(doc, figs):
    C_ = cap12
    K.encabezado_capitulo(doc, C_)
    Z.aviso_entorno(doc)
    doc.add_heading(C_.E23_TITULO, level=1)
    M.seccion(doc, C_.S121)
    for op in C_.CONTRATOS_S121:
        Z.contrato(doc, op)
    M.tabla(doc, C_.TABLA_121, [1.2, 5.6, 3.4, 3.6, 2.8], rotulo=C_.TABLA_121_ROTULO)
    ej(doc, C_.EJ121)
    ej(doc, C_.EJ122)
    M.seccion(doc, C_.S122)
    H.imagen(doc, figs['fig_12_1'], C_.LEAD_FIG121, C_.EPI_FIG121, ancho_cm=16.0)
    codigos_de(doc, C_, C_.CODIGOS_S122)
    M.tabla(doc, C_.TABLA_122, [2.8, 4.8, 5.0, 4.0], rotulo=C_.RONDAS_ROTULO)
    H.caja(doc, *C_.PROTOCOLO, tipo='concepto')
    M.actividades(doc, 'Actividades del Encuentro 23', C_.ACT_E23)

    doc.add_heading(C_.E24_TITULO, level=1)
    M.seccion(doc, C_.S123)
    for op in C_.CONTRATOS_S123:
        Z.contrato(doc, op)
    codigos_de(doc, C_, C_.CODIGOS_S123)
    ej(doc, C_.EJ123)
    M.seccion(doc, C_.S124)
    codigos_de(doc, C_, C_.CODIGOS_S124)
    M.tabla(doc, C_.TABLA_123, [4.2, 4.4, 4.0, 4.0], rotulo=C_.TABLA_123_ROTULO)
    ej(doc, C_.EJ124)
    M.actividades(doc, 'Actividades del Encuentro 24', C_.ACT_E24)
    H.caja(doc, *C_.REPASO, tipo='neutra')
    H.caja(doc, *C_.CALENDARIO, tipo='neutra')
    practica(doc, C_, cuerpo12)
    evaluacion(doc, C_)


# ---------------------------------------------------------------- capítulo 13
def capitulo13(doc, figs):
    import cap3   # lote_1/build/cap3.py: niveles de desempeño del H1 (Work §4.3), sin copiarlos
    C_ = cap13
    K.encabezado_capitulo(doc, C_)
    Z.aviso_entorno(doc)
    doc.add_heading(C_.E25_TITULO, level=1)
    M.seccion(doc, C_.S131)
    for op in ('OP-03', 'OP-04'):
        Z.contrato(doc, op)
    codigos_de(doc, C_, C_.CODIGOS_S131)
    ej(doc, C_.EJ131)
    M.seccion(doc, C_.S132)
    H.imagen(doc, figs['fig_13_1'], C_.LEAD_FIG131, C_.EPI_FIG131, ancho_cm=16.0)
    codigos_de(doc, C_, C_.CODIGOS_S132)
    M.tabla(doc, C_.TABLA_131, [2.6, 2.8, 3.2, 4.0, 4.0], rotulo=C_.TABLA_131_ROTULO)
    Z.contrato(doc, 'OP-05')
    ej(doc, C_.EJ132)
    M.actividades(doc, 'Actividades del Encuentro 25', C_.ACT_E25)
    practica(doc, C_, cuerpo13)

    K.titulo_en_pagina_nueva(doc, C_.E26_TITULO)
    M.seccion(doc, C_.S133)
    M.tabla(doc, C_.TABLA_132, [2.6, 4.4, 4.4, 2.6, 2.6], rotulo=C_.TABLA_132_ROTULO, size=8.5)
    ej(doc, C_.EJ133)
    M.seccion(doc, C_.S134)
    M.tabla(doc, C_.TABLA_133, [1.5, 1.6, 7.3, 2.0, 2.0, 2.2], rotulo=C_.TABLA_133_ROTULO)
    doc.add_heading(C_.H4_TITULO, level=2)
    for t in C_.H4_TEXTO:
        H.p_texto(doc, t)
    H.caja(doc, *C_.H4_LISTA, tipo='neutra')
    H.caja(doc, *C_.H4_EVALUACION, tipo='concepto')
    M.tabla(doc, (['Criterio del H4', 'Capacidades'], [[r[0], r[1]] for r in C_.RUBRICA_H4]), [12.6, 4.0],
            rotulo='Criterios del H4 (la rúbrica completa está en la guía docente)')
    M.tabla(doc, (['Nivel de desempeño', 'Descriptor común'], [list(x) for x in cap3.NIVELES_DESEMPENO]), [3.6, 13.0],
            rotulo='Niveles de desempeño (propuesta editorial)')
    M.actividades(doc, 'Actividades del Encuentro 26', C_.ACT_E26)
    H.caja(doc, *C_.REPASO, tipo='neutra')
    H.caja(doc, *C_.CALENDARIO, tipo='neutra')
    evaluacion(doc, C_)


# ---------------------------------------------------------------- libro
ENCS = {cap10: (cap10.E19_TITULO, cap10.E20_TITULO), cap11: (cap11.E21_TITULO, cap11.E22_TITULO),
        cap12: (cap12.E23_TITULO, cap12.E24_TITULO), cap13: (cap13.E25_TITULO, cap13.E26_TITULO)}


def entradas_indice():
    e = [(1, UNIDAD_IV)]
    for C_ in CAPS:
        e.append((1, '%s — %s' % (C_.CAPITULO, C_.TITULO)))
        a, b = ENCS[C_]; secs = list(C_.SECCIONES)
        e.append((2, a)); e += [(3, s) for s in secs[:2]]
        if C_ is cap13:
            e.append((2, C_.PRACTICA_TITULO))
            e.append((2, b)); e += [(3, s) for s in secs[2:]]
            e.append((3, cap13.H4_TITULO))
        else:
            e.append((2, b)); e += [(3, s) for s in secs[2:]]
            e.append((2, C_.PRACTICA_TITULO))
        e.append((2, C_.EVAL_TITULO))
    return e


def libro_estudiante(figs, paginas=None):
    doc = H.new_doc()
    Z.portada(doc, 'Libro del estudiante', ESTADO)
    K.indice_marcador(doc)
    H.CLAVES.clear()
    apertura_unidad(doc)
    capitulo10(doc, figs)
    capitulo11(doc, figs)
    capitulo12(doc, figs)
    capitulo13(doc, figs)
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
        pdf = K.a_pdf(RUTA_EST, L4)
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
        'Extracción imprimible de las Prácticas 10 a 13 del libro del estudiante, generada desde la misma fuente. '
        'No está aprobado para la venta ni para uso en aula; la aprobación final corresponde a Fernando.',
        'Cada práctica trabaja con datos que no aparecen en los ejemplos resueltos del libro. Tiene tres niveles que usan '
        'los mismos datos: tu docente te indica en cuál trabajar. Las tablas, figuras y códigos que se citan son los del '
        'libro del estudiante.',
        'La Práctica 13 es un complemento editorial al índice de Work: se hace en el Encuentro 25 o como actividad '
        'complementaria, y no reemplaza ni reduce el H4.'])
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
        guia_u4.construir(RUTA_GUIA, claves, paginas, ESTADO, figs)
        pdf_g = K.a_pdf(RUTA_GUIA, L4)
        cuaderno()
        pdf_c = K.a_pdf(RUTA_CUAD, L4)
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
              open(os.path.join(L4, 'resultado_construccion.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)

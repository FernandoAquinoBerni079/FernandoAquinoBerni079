# -*- coding: utf-8 -*-
"""Construye el lote 2 (Unidad II, Capítulos 4 a 6) en oficio O3: libro del estudiante, guía docente con solucionario
y cuaderno de prácticas, en DOCX, con PDF de control. Todo sale de las mismas fuentes: caso/ (datos del caso y
modelos) y build/cap4.py a cap6.py (contenido).

El índice del libro se calcula sobre el PDF y se repite hasta que la paginación queda estable. Después de cada vuelta,
el control de filas de la candidata O3 busca cada fila de cada tabla en el PDF; si a una tabla le falta alguna, su
rótulo abre hoja nueva y se reconstruye.
Uso: python3 lote_2/build/construir.py   →  lote_2/ADS_3BTI_LOTE2_*.docx y .pdf"""
import os, sys, json
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
L2 = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
sys.path.insert(1, os.path.join(L2, 'caso'))

import oficio as O
H, M, K = O.H, O.M, O.K
import piezas as Z
import diagramas as G
import cap4, cap5, cap6
import guia
R, MO, MB = Z.R, Z.MO, Z.MB
D = R.D
MB1 = MB.MB

RUTA_EST = os.path.join(L2, 'ADS_3BTI_LOTE2_ESTUDIANTE_OFICIO_O3.docx')
RUTA_GUIA = os.path.join(L2, 'ADS_3BTI_LOTE2_GUIA_DOCENTE_OFICIO_O3.docx')
RUTA_CUAD = os.path.join(L2, 'ADS_3BTI_LOTE2_CUADERNO_PRACTICAS_OFICIO_O3.docx')
CAPS = (cap4, cap5, cap6)
UNIDAD_II = 'Unidad II — Especificar qué debe resolver el sistema'

ESTADO = [
    'Lote editorial 2 para auditoría independiente. No está aprobado para la venta ni para uso en aula; la aprobación '
    'final corresponde a Fernando y se hará sobre el conjunto completo.',
    'Sigue el índice del informe de Work v0.1: Unidad II (Capítulos 4 a 6, Encuentros 7 a 12). Formato oficio O3.',
    'Las capacidades C1 a C10 son propuestas para el programa institucional. No son capacidades oficiales del MEC.',
]


def apertura_unidad(doc):
    K.titulo_en_pagina_nueva(doc, UNIDAD_II)
    H.p_texto(doc, 'Resultado de la unidad: requisitos, procesos y trazabilidad inicial. Tres capítulos, seis encuentros y '
                   '30 HC. La unidad parte del dossier y del alcance de la Unidad I, y cierra con el hito H2: los requisitos '
                   'y los modelos funcionales, versionados y defendidos.')
    M.tabla(doc, (['Capítulo', 'Encuentros', 'Evidencias (Work §5.2)'],
                  [['4. Requisitos que se pueden comprobar', '7 y 8', 'Catálogo con identificadores y fuente; requisitos comprobables y revisión entre pares'],
                   ['5. Procesos, contexto y casos de uso', '9 y 10', 'Flujos comentados y decisiones justificadas; préstamo, devolución y consulta con alternativas'],
                   ['6. Priorizar y mantener la coherencia', '11 y 12', 'Requisito-modelo-prueba; tareas y responsables; H2: requisitos y modelos funcionales versionados']]),
            [5.4, 2.2, 9.0], rotulo='La Unidad II en un vistazo')
    H.caja(doc, 'Qué usa esta unidad de la Unidad I', [
        'El dossier del caso (registros E1 a E5, O1, D0 a D2 y necesidades N-01 a N-13), las reglas a negociar y el '
        'alcance mínimo del Capítulo 3. En las prácticas, la Escuela Básica Mbokaja sigue como caso de transferencia.'],
        tipo='neutra')


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


# ---------------------------------------------------------------- prácticas (libro y cuaderno)
def cuerpo4(doc):
    C = cap4
    M.tabla(doc, (['Código', 'Quién lo pidió', 'Pedido'], [list(b) for b in C.BUZON]), [1.8, 4.0, 10.8], rotulo=C.BUZON_TITULO)
    M.actividades(doc, C.CONSIGNA_COMUN_TITULO, [('Consigna común', C.CONSIGNA_COMUN)])


def cuerpo5(doc):
    Z.codigos(doc, cap5.DATO_NUEVO_TITULO, [MB.DATO_NUEVO] + [x for x in MB1.DATOS if x[0] in ('M-F2', 'M-F4')])
    Z.codigos(doc, MB.PROCESO_TITULO, MB.PROCESO)
    Z.codigos(doc, MB.SITUACIONES_TITULO, MB.SITUACIONES)
    Z.catalogo_mbokaja(doc)
    M.tabla(doc, (['Cód.', 'Necesidad', 'De dónde sale'], [list(x) for x in MB1.NECESIDADES]), [1.6, 9.6, 5.4],
            rotulo=MB1.NECESIDADES_TITULO)


def cuerpo6(doc):
    Z.codigos(doc, MB.CAMBIO_TITULO, MB.CAMBIO)
    Z.codigos(doc, 'Datos de Mbokaja que vas a necesitar (caso de práctica, ficticio)',
              [x for x in MB1.NORMAS if x[0] == 'M-N1'] + [x for x in MB1.DATOS if x[0] in ('M-F4', 'M-F5')])


PRACTICAS = ((cap4, cuerpo4), (cap5, cuerpo5), (cap6, cuerpo6))


# ---------------------------------------------------------------- capítulo 4
def capitulo4(doc, figs):
    C = cap4
    K.encabezado_capitulo(doc, C)
    Z.extracto(doc, C)
    doc.add_heading(C.E7_TITULO, level=1).paragraph_format.page_break_before = True
    M.seccion(doc, C.S41)
    M.tabla(doc, C.TABLA_41, [2.8, 4.0, 6.0, 3.8], rotulo='Tabla 4.1 — Cuatro categorías que no hay que mezclar')
    H.caja(doc, *C.CONCEPTO_REQ, tipo='concepto')
    H.caja(doc, C.EJ1[0], C.EJ1[1], tipo='neutra')
    M.seccion(doc, C.S42)
    H.imagen(doc, figs['fig_4_1'], C.LEAD_FIG1, C.EPI_FIG1, ancho_cm=15.0)
    M.tabla(doc, C.TABLA_42, [3.0, 3.6, 4.4, 5.6], rotulo='Tabla 4.2 — Tipos de requisitos')
    H.caja(doc, C.EJ2[0], C.EJ2[1], tipo='neutra')
    M.tabla(doc, (['Id.', 'Tipo', 'Enunciado', 'Fuente', 'Prioridad'], [[i, t, e, ', '.join(f), p] for i, t, e, f, p in C.CATALOGO]),
            [1.5, 2.3, 7.8, 2.4, 2.6], rotulo='Tabla 4.3 — Catálogo inicial de requisitos del caso')
    M.tabla(doc, (['Fuente', 'Pedido', 'Prioridad', 'Razón'], [list(x) for x in C.POSTERGADOS]), [1.6, 4.4, 2.2, 8.4],
            rotulo='Tabla 4.4 — Pedidos registrados fuera del catálogo inicial')
    M.actividades(doc, 'Actividades del Encuentro 7', C.ACT_E7)

    doc.add_heading(C.E8_TITULO, level=1)
    M.seccion(doc, C.S43)
    H.imagen(doc, figs['fig_4_2'], C.LEAD_FIG2, C.EPI_FIG2, ancho_cm=15.5)
    H.caja(doc, *C.CONCEPTO_CA, tipo='concepto')
    H.caja(doc, C.EJ3[0], C.EJ3[1], tipo='neutra')
    M.tabla(doc, C.TABLA_43, [1.5, 10.2, 4.9], rotulo='Tabla 4.5 — Criterios de aceptación y prioridades de otros requisitos')
    M.seccion(doc, C.S44)
    M.tabla(doc, C.TABLA_44, [2.9, 3.9, 3.9, 5.9], rotulo='Tabla 4.6 — Ambigüedades frecuentes')
    H.caja(doc, C.EJ4[0], C.EJ4[1], tipo='neutra')
    H.caja(doc, *C.REVISION_PARES, tipo='neutra')
    M.actividades(doc, 'Actividades del Encuentro 8', C.ACT_E8)
    H.caja(doc, *C.REPASO, tipo='neutra')
    H.caja(doc, *C.CALENDARIO, tipo='neutra')
    practica(doc, C, cuerpo4)
    evaluacion(doc, C)


# ---------------------------------------------------------------- capítulo 5
def capitulo5(doc, figs):
    C = cap5
    K.encabezado_capitulo(doc, C)
    doc.add_heading(C.E9_TITULO, level=1)
    M.seccion(doc, C.S51)
    Z.tabla_leyenda(doc, 'actividad', C.LEYENDA_ACTIVIDAD, figs)
    H.p_texto(doc, C.NOTA_LEYENDA_ACTIVIDAD, italic=True, size=9.5)
    H.imagen(doc, figs['fig_5_1'], C.LEAD_FIG51, C.EPI_FIG51, ancho_cm=12.0)
    M.tabla(doc, C.TABLA_52, [1.4, 3.6, 8.4, 3.2], rotulo=C.TABLA_52_ROTULO)
    H.caja(doc, C.EJ51[0], C.EJ51[1], tipo='neutra')
    H.imagen(doc, figs['fig_5_2'], C.LEAD_FIG52, C.EPI_FIG52, ancho_cm=15.5)
    M.tabla(doc, C.TABLA_53, [3.0, 3.8, 4.8, 5.0], rotulo=C.TABLA_53_ROTULO)
    H.caja(doc, C.EJ52[0], C.EJ52[1], tipo='neutra')
    M.seccion(doc, C.S52)
    Z.tabla_leyenda(doc, 'contexto', C.LEYENDA_CONTEXTO, figs)
    H.imagen(doc, figs['fig_5_3'], C.LEAD_FIG53, C.EPI_FIG53, ancho_cm=15.5)
    M.tabla(doc, C.TABLA_55, [3.0, 3.0, 6.4, 4.2], rotulo=C.TABLA_55_ROTULO)
    H.caja(doc, C.EJ53[0], C.EJ53[1], tipo='neutra')
    M.actividades(doc, 'Actividades del Encuentro 9', C.ACT_E9)

    doc.add_heading(C.E10_TITULO, level=1)
    M.seccion(doc, C.S53)
    Z.tabla_leyenda(doc, 'casos_de_uso', C.LEYENDA_CU, figs)
    H.imagen(doc, figs['fig_5_4'], C.LEAD_FIG54, C.EPI_FIG54, ancho_cm=14.0)
    H.caja(doc, C.EJ54[0], C.EJ54[1], tipo='neutra')
    M.seccion(doc, C.S54)
    H.caja(doc, C.EJ55[0], C.EJ55[1], tipo='neutra')
    H.keep_next(H.p_texto(doc, 'Estas son las plantillas completas de los tres casos de uso prioritarios, con su escenario '
                               'principal y sus flujos alternativos.'))
    for cu in MO.PRIORITARIOS:
        Z.plantilla(doc, cu)
    M.actividades(doc, 'Actividades del Encuentro 10', C.ACT_E10)
    H.caja(doc, *C.REPASO, tipo='neutra')
    H.caja(doc, *C.CALENDARIO, tipo='neutra')
    practica(doc, C, cuerpo5)
    evaluacion(doc, C)


# ---------------------------------------------------------------- capítulo 6
def capitulo6(doc, figs):
    C = cap6
    K.encabezado_capitulo(doc, C)
    doc.add_heading(C.E11_TITULO, level=1)
    M.seccion(doc, C.S61)
    M.tabla(doc, C.TABLA_61, [3.6, 2.2, 2.2, 4.8, 3.8], rotulo=C.TABLA_61_ROTULO)
    H.caja(doc, C.EJ61[0], C.EJ61[1], tipo='neutra')
    M.seccion(doc, C.S62)
    H.imagen(doc, figs['fig_6_1'], C.LEAD_FIG61, C.EPI_FIG61, ancho_cm=15.5)
    M.tabla(doc, C.TABLA_62, [1.7, 1.9, 1.5, 4.2, 4.9, 2.4], rotulo=C.TABLA_62_ROTULO, size=8.5)
    H.caja(doc, C.EJ62[0], C.EJ62[1], tipo='neutra')
    M.seccion(doc, C.S63)
    M.tabla(doc, C.TABLA_63, [3.2, 1.9, 5.5, 3.4, 2.6], rotulo=C.TABLA_63_ROTULO)
    M.tabla(doc, C.TABLA_64, [6.4, 2.6, 1.2, 3.6, 2.8], rotulo=C.TABLA_64_ROTULO)
    H.caja(doc, C.EJ63[0], C.EJ63[1], tipo='neutra')
    M.actividades(doc, 'Actividades del Encuentro 11', C.ACT_E11)

    doc.add_heading(C.E12_TITULO, level=1)
    M.seccion(doc, C.S64)
    Z.registro(doc, 'D3', lead=C.D3_LEAD)
    M.tabla(doc, C.TABLA_65, [4.2, 12.4], rotulo=C.TABLA_65_ROTULO)
    H.imagen(doc, figs['fig_6_2'], C.LEAD_FIG62, C.EPI_FIG62, ancho_cm=15.0)
    H.caja(doc, C.EJ64[0], C.EJ64[1], tipo='neutra')
    M.tabla(doc, C.TABLA_66, [2.4, 3.6, 10.6], rotulo=C.TABLA_66_ROTULO)
    doc.add_heading(C.H2_TITULO, level=2)
    for t in C.H2_TEXTO:
        H.p_texto(doc, t)
    H.caja(doc, *C.H2_LISTA, tipo='neutra')
    H.caja(doc, *C.H2_EVALUACION, tipo='concepto')
    M.tabla(doc, (['Criterio del H2', 'Capacidad'], [[r[0], r[1]] for r in C.RUBRICA_H2]), [12.6, 4.0],
            rotulo='Criterios del H2 (la rúbrica completa está en la guía docente)')
    M.tabla(doc, (['Nivel de desempeño', 'Descriptor común'], [list(x) for x in K_NIVELES()]), [3.6, 13.0],
            rotulo='Niveles de desempeño (propuesta editorial)')
    M.actividades(doc, 'Actividades del Encuentro 12', C.ACT_E12)
    H.caja(doc, *C.REPASO, tipo='neutra')
    H.caja(doc, *C.CALENDARIO, tipo='neutra')
    practica(doc, C, cuerpo6)
    evaluacion(doc, C)


def K_NIVELES():
    import cap3   # lote_1/build/cap3.py: los niveles de desempeño del H1 (Work §4.3), sin copiarlos
    return cap3.NIVELES_DESEMPENO


# ---------------------------------------------------------------- libro
def entradas_indice():
    e = [(1, UNIDAD_II)]
    encs = {cap4: (cap4.E7_TITULO, cap4.E8_TITULO), cap5: (cap5.E9_TITULO, cap5.E10_TITULO), cap6: (cap6.E11_TITULO, cap6.E12_TITULO)}
    for C in CAPS:
        e.append((1, '%s — %s' % (C.CAPITULO, C.TITULO)))
        a, b = encs[C]; secs = list(C.SECCIONES)
        corte = 3 if C is cap6 else 2
        e.append((2, a)); e += [(3, s) for s in secs[:corte]]
        e.append((2, b)); e += [(3, s) for s in secs[corte:]]
        if C is cap6:
            e.append((3, cap6.H2_TITULO))
        e.append((2, C.PRACTICA_TITULO)); e.append((2, C.EVAL_TITULO))
    return e


def libro_estudiante(figs, paginas=None):
    doc = H.new_doc()
    Z.portada(doc, 'Libro del estudiante', ESTADO)
    K.indice_marcador(doc)
    H.CLAVES.clear()
    apertura_unidad(doc)
    capitulo4(doc, figs)
    capitulo5(doc, figs)
    capitulo6(doc, figs)
    M.pegar_renglones(doc)
    K.saltos_a_titulos(doc)
    K.rellenar_indice(doc, entradas_indice(), paginas or {})
    H.finalizar(doc, RUTA_EST)
    return list(H.CLAVES)


def construir_estudiante(figs):
    titulos = [t for _, t in entradas_indice()]
    paginas = {}
    for vuelta in range(6):
        claves = libro_estudiante(figs, paginas)
        pdf = K.a_pdf(RUTA_EST, L2)
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
        'Extracción imprimible de las Prácticas 4, 5 y 6 del libro del estudiante, generada desde la misma fuente. '
        'No está aprobado para la venta ni para uso en aula; la aprobación final corresponde a Fernando.',
        'Cada práctica trabaja con datos que no aparecen en los ejemplos resueltos del libro. Tiene tres niveles que usan '
        'los mismos datos: tu docente te indica en cuál trabajar. Si el trabajo es un diagrama, hacelo en una hoja aparte '
        'y adjuntala. Las tablas y figuras que se citan son las del libro del estudiante.'])
    for C, cuerpo in PRACTICAS:
        practica(doc, C, cuerpo)
    M.pegar_renglones(doc)
    K.saltos_a_titulos(doc)
    H.finalizar(doc, RUTA_CUAD)


if __name__ == '__main__':
    import pymupdf
    figs = G.generar()
    for vuelta in range(8):
        claves, paginas, total = construir_estudiante(figs)
        guia.construir(RUTA_GUIA, claves, paginas, ESTADO, figs)
        pdf_g = K.a_pdf(RUTA_GUIA, L2)
        cuaderno()
        pdf_c = K.a_pdf(RUTA_CUAD, L2)
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
              open(os.path.join(L2, 'resultado_construccion.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)

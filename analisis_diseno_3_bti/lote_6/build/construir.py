# -*- coding: utf-8 -*-
"""Construye el lote 6 (Unidad VI, Capítulos 17 y 18) en oficio O3: libro del estudiante, guía docente con solucionario
y cuaderno de prácticas, en DOCX, con PDF de control, y la planilla de tiempos del Encuentro 35 (XLSX con fórmulas).
Todo sale de las mismas fuentes: caso/ (entrega, Mbokaja U6 e instrumentos, que amplían sin modificarlas las fuentes de
los lotes 1 a 5), proyecto/ (los fragmentos de código se leen del paquete modelo), resultados_pruebas/ (las tablas de
resultados salen de la ejecución real, que hace build/reproducir.py) y build/cap17.py y cap18.py (contenido).
Mismo ciclo que los lotes 2 a 5 (índice estable sobre el PDF y control de filas de la candidata O3).
Uso: python3 lote_6/build/reproducir.py && python3 lote_6/build/construir.py  →  lote_6/ADS_3BTI_LOTE6_*.docx y .pdf"""
import os, sys, json
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
L6 = os.path.dirname(AQUI)
ADS = os.path.dirname(L6)
sys.path.insert(0, AQUI)
sys.path.insert(1, os.path.join(L6, 'caso'))
sys.path.insert(2, os.path.join(ADS, 'lote_4', 'build'))
sys.path.insert(3, os.path.join(ADS, 'lote_4', 'caso'))
sys.path.insert(4, os.path.join(ADS, 'lote_3', 'build'))
sys.path.insert(5, os.path.join(ADS, 'lote_3', 'caso'))
sys.path.insert(6, os.path.join(ADS, 'lote_2', 'build'))

import oficio as O
H, M, K = O.H, O.M, O.K
import piezas_u6 as Z
import diagramas_u6 as G
import cap17, cap18
import guia_u6
import planilla_tiempos
E, MB, I = cap17.E, cap17.MB, cap17.I

RUTA_EST = os.path.join(L6, 'ADS_3BTI_LOTE6_ESTUDIANTE_OFICIO_O3.docx')
RUTA_GUIA = os.path.join(L6, 'ADS_3BTI_LOTE6_GUIA_DOCENTE_OFICIO_O3.docx')
RUTA_CUAD = os.path.join(L6, 'ADS_3BTI_LOTE6_CUADERNO_PRACTICAS_OFICIO_O3.docx')
CAPS = (cap17, cap18)
UNIDAD_VI = 'Unidad VI — Entregar y comunicar'

ESTADO = [
    'Lote editorial 6 para auditoría independiente. No está aprobado para la venta ni para uso en aula; la aprobación '
    'final corresponde a Fernando y se hará sobre la colección completa.',
    'Sigue el índice del informe de Work v0.1: Unidad VI (Capítulos 17 y 18, Encuentros 33 a 36). Formato oficio O3.',
    'Las capacidades C1 a C10 son propuestas para el programa institucional. No son capacidades oficiales del MEC. '
    'Las pruebas que se informan corrieron solo en el entorno de construcción (Linux): no se probaron en las '
    'computadoras de ninguna institución ni en Windows, y la instalación por otro equipo la hace el curso.',
]


def apertura_unidad(doc):
    K.titulo_en_pagina_nueva(doc, UNIDAD_VI)
    H.p_texto(doc, 'Resultado de la unidad (Work §5.1): paquete reproducible, defensa y recuperación. Dos capítulos, cuatro '
                   'encuentros y 20 HC. La unidad entrega el sistema a otras personas, lo demuestra, lo defiende y cierra '
                   'el proyecto: el hito H6 y la evaluación integradora de la segunda etapa.')
    M.tabla(doc, (['Capítulo', 'Encuentros', 'Evidencias (Work §5.2)'],
                  [['17. Preparar una entrega reproducible', '33 y 34', 'Documentación probada por el propio equipo; H6: paquete reproducible y ajustes finales'],
                   ['18. Demostrar, defender y aprender del proyecto', '35 y 36', 'Rúbrica de producto y preguntas de transferencia; evidencia faltante, balance y propuesta de continuidad']]),
            [5.4, 2.2, 9.0], rotulo='La Unidad VI en un vistazo')
    Z.aviso_entorno(doc)
    H.caja(doc, 'Cómo se lee un resultado en esta unidad', [
        'Como en la Unidad V, cada resultado lleva su condición: comprobado, reproducido, simulado o pendiente.',
        'Una ejecución automática de la guía de instalación es una comprobación técnica. La evidencia de que una entrega es '
        'reproducible la da otro equipo, que instala sin ayuda: esa la produce tu curso.'], tipo='neutra')


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


def cuerpo17(doc):
    Z.codigos(doc, MB.DATOS_TITULO, MB.DATOS)
    Z.codigos(doc, MB.SITUACIONES_TITULO, MB.SITUACIONES)
    M.tabla(doc, (['Archivo', 'Qué es'], [[a, d] for a, d in E.ARCHIVOS_LISTA if a.startswith('ENTREGA/') or a == 'LEEME.txt']),
            [5.4, 11.2], rotulo='Documentos que trae el paquete del voluntario')


PRACTICAS = ((cap17, cuerpo17),)


# ---------------------------------------------------------------- capítulo 17
def capitulo17(doc, figs):
    C_ = cap17
    K.encabezado_capitulo(doc, C_)
    Z.aviso_entorno(doc)
    doc.add_heading(C_.E33_TITULO, level=1)
    M.seccion(doc, C_.S171)
    M.tabla(doc, C_.tabla_171(), [1.2, 4.2, 6.0, 5.2], rotulo=C_.TABLA_171_ROTULO, size=8.5)
    ej(doc, C_.EJ171)
    M.seccion(doc, C_.S172)
    M.tabla(doc, C_.tabla_172(), [4.8, 3.6, 4.4, 3.8], rotulo=C_.TABLA_172_ROTULO, size=8.5)
    ej(doc, C_.EJ172)
    H.imagen(doc, figs['fig_17_1'], C_.LEAD_FIG171, C_.EPI_FIG171, ancho_cm=16.0)
    M.actividades(doc, 'Actividades del Encuentro 33', C_.ACT_E33)
    practica(doc, C_, cuerpo17)

    K.titulo_en_pagina_nueva(doc, C_.E34_TITULO)
    M.seccion(doc, C_.S173)
    M.tabla(doc, C_.tabla_173(), [4.4, 4.2, 4.6, 3.4], rotulo=C_.TABLA_173_ROTULO, size=8.5)
    codigos_de(doc, C_, C_.CODIGOS_S173)
    H.caja(doc, *C_.LICENCIA, tipo='concepto')
    ej(doc, C_.EJ173)
    M.seccion(doc, C_.S174)
    M.tabla(doc, C_.TABLA_174, [2.0, 14.6], rotulo=C_.TABLA_174_ROTULO)
    codigos_de(doc, C_, C_.CODIGOS_S174)
    M.tabla(doc, C_.TABLA_175, [7.0, 9.6], rotulo=C_.TABLA_175_ROTULO, size=8.5)
    M.tabla(doc, C_.tabla_176(), [7.2, 4.4, 5.0], rotulo=C_.TABLA_176_ROTULO, size=8.5)
    nota(doc, C_.NOTA_176 % C_.entorno_texto())
    ej(doc, C_.EJ174)
    doc.add_heading(C_.H6_TITULO, level=2)
    for t in C_.H6_TEXTO:
        H.p_texto(doc, t)
    H.caja(doc, *C_.H6_LISTA, tipo='neutra')
    H.caja(doc, *C_.H6_EVALUACION, tipo='concepto')
    M.tabla(doc, (['Criterio del H6', 'Capacidad'], [[x[0], x[1]] for x in C_.RUBRICA_H6]), [12.6, 4.0],
            rotulo='Criterios del H6 (la rúbrica completa está en la guía docente)')
    M.actividades(doc, 'Actividades del Encuentro 34', C_.ACT_E34)
    H.caja(doc, *C_.REPASO, tipo='neutra')
    H.caja(doc, *C_.CALENDARIO, tipo='neutra')
    evaluacion(doc, C_)


# ---------------------------------------------------------------- capítulo 18
def capitulo18(doc, figs):
    import cap3   # lote_1/build/cap3.py: niveles de desempeño (Work §4.3), sin copiarlos
    C_ = cap18
    K.encabezado_capitulo(doc, C_)
    Z.aviso_entorno(doc)
    doc.add_heading(C_.E35_TITULO, level=1)
    M.seccion(doc, C_.S181)
    M.tabla(doc, C_.TABLA_181, [2.6, 4.6, 4.0, 3.6, 1.8], rotulo=C_.TABLA_181_ROTULO, size=8.5)
    H.imagen(doc, figs['fig_18_1'], C_.LEAD_FIG181, C_.EPI_FIG181, ancho_cm=16.0)
    ej(doc, C_.EJ181)
    M.seccion(doc, C_.S182)
    M.tabla(doc, C_.TABLA_182, [2.8, 3.6, 3.4, 3.4, 3.4], rotulo=C_.TABLA_182_ROTULO, size=8.5)
    ej(doc, C_.EJ182)
    M.tabla(doc, C_.TABLA_183, [4.6, 12.0], rotulo=C_.TABLA_183_ROTULO)
    M.actividades(doc, 'Actividades del Encuentro 35', C_.ACT_E35)

    K.titulo_en_pagina_nueva(doc, C_.E36_TITULO)
    M.seccion(doc, C_.S183)
    M.tabla(doc, C_.TABLA_184, [1.4, 4.2, 5.6, 3.6, 1.8], rotulo=C_.TABLA_184_ROTULO, size=8.5)
    M.tabla(doc, C_.TABLA_185, [1.8, 2.0, 6.6, 2.0, 1.4, 2.8], rotulo=C_.TABLA_185_ROTULO, size=8.5)
    H.caja(doc, *C_.RECUPERACION, tipo='concepto')
    M.seccion(doc, C_.S184)
    M.tabla(doc, C_.TABLA_186, [4.4, 2.8, 3.2, 4.4, 1.8], rotulo=C_.TABLA_186_ROTULO, size=8.5)
    nota(doc, I.RETRO_NOTA)
    ej(doc, C_.EJ183)
    M.actividades(doc, 'Actividades del Encuentro 36', C_.ACT_E36)
    doc.add_heading(C_.INTEGRADORA_TITULO, level=2)
    for t in C_.INTEGRADORA_TEXTO:
        H.p_texto(doc, t)
    M.tabla(doc, C_.TABLA_187, [4.4, 1.6, 8.0, 2.6], rotulo=C_.TABLA_187_ROTULO)
    M.tabla(doc, (['Nivel de desempeño', 'Descriptor común'], [list(x) for x in cap3.NIVELES_DESEMPENO]), [3.6, 13.0],
            rotulo='Niveles de desempeño (propuesta editorial)')
    H.caja(doc, *C_.CIERRE, tipo='neutra')
    H.caja(doc, *C_.REPASO, tipo='neutra')
    H.caja(doc, *C_.CALENDARIO, tipo='neutra')


# ---------------------------------------------------------------- libro
def entradas_indice():
    e = [(1, UNIDAD_VI)]
    e.append((1, '%s — %s' % (cap17.CAPITULO, cap17.TITULO)))
    s = cap17.SECCIONES
    e += [(2, cap17.E33_TITULO), (3, s[0]), (3, s[1]), (2, cap17.PRACTICA_TITULO),
          (2, cap17.E34_TITULO), (3, s[2]), (3, s[3]), (3, cap17.H6_TITULO), (2, cap17.EVAL_TITULO)]
    e.append((1, '%s — %s' % (cap18.CAPITULO, cap18.TITULO)))
    s = cap18.SECCIONES
    e += [(2, cap18.E35_TITULO), (3, s[0]), (3, s[1]), (2, cap18.E36_TITULO), (3, s[2]), (3, s[3]),
          (3, cap18.INTEGRADORA_TITULO)]
    return e


def libro_estudiante(figs, paginas=None):
    doc = H.new_doc()
    Z.portada(doc, 'Libro del estudiante', ESTADO)
    K.indice_marcador(doc)
    H.CLAVES.clear()
    apertura_unidad(doc)
    capitulo17(doc, figs)
    capitulo18(doc, figs)
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
        pdf = K.a_pdf(RUTA_EST, L6)
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
        'Extracción imprimible de la Práctica 17 del libro del estudiante, generada desde la misma fuente. No está aprobado '
        'para la venta ni para uso en aula; la aprobación final corresponde a Fernando.',
        'La práctica trabaja con un paquete de Mbokaja que no aparece en los ejemplos resueltos del libro. Tiene tres niveles: '
        'tu docente te indica en cuál trabajar.',
        'El Capítulo 18 no tiene práctica: sus instrumentos son la demostración, la defensa individual y la evaluación '
        'integradora, que están en el libro.'])
    for C_, cuerpo in PRACTICAS:
        practica(doc, C_, cuerpo)
    M.pegar_renglones(doc)
    Z.encadenar_inicio(doc)
    K.saltos_a_titulos(doc)
    H.finalizar(doc, RUTA_CUAD)


if __name__ == '__main__':
    import pymupdf
    figs = G.generar(os.path.join(AQUI, 'figs'))
    planilla_tiempos.escribir()
    for vuelta in range(8):
        claves, paginas, total = construir_estudiante(figs)
        guia_u6.construir(RUTA_GUIA, claves, paginas, ESTADO, figs)
        pdf_g = K.a_pdf(RUTA_GUIA, L6)
        cuaderno()
        pdf_c = K.a_pdf(RUTA_CUAD, L6)
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
              open(os.path.join(L6, 'resultado_construccion.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)

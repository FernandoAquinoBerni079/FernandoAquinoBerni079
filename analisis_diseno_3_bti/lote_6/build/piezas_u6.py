# -*- coding: utf-8 -*-
"""Piezas de armado del lote 6. Reutiliza sin modificarlas las piezas del lote 4 (lote_4/build/piezas_u4.py): portada,
bloques de código con su ficha, contratos y encadenado de tablas. Solo cambian la versión y la línea de la portada, y
el origen de los fragmentos de código: los del lote 6 se leen de lote_6/proyecto/ con build/fragmentos_u6.py."""
import piezas_u4 as Z4
import fragmentos_u6 as FU6

VERSION = 'v1.1 (lote 6, cierre de auditoría) · oficio O3'
LINEA = 'LOTE EDITORIAL 6 — UNIDAD VI (CAPÍTULOS 17 Y 18)'
H, M, K, C, X = Z4.H, Z4.M, Z4.K, Z4.C, Z4.X
codigos, contrato, encadenar_inicio, aviso_entorno = Z4.codigos, Z4.contrato, Z4.encadenar_inicio, Z4.aviso_entorno


def portada(doc, tipo_doc, estado):
    Z4.Z2.VERSION = VERSION
    Z4.Z2.portada(doc, tipo_doc, estado, linea=LINEA)


def codigo(doc, fid, explicacion=None):
    """El mismo bloque de código del lote 4 (rótulo, ficha y código juntos), con el fragmento leído del proyecto del
    lote 6. El módulo de fragmentos del lote 4 se restituye al terminar."""
    anterior = Z4.F
    Z4.F = FU6
    try:
        Z4.codigo(doc, fid, explicacion)
    finally:
        Z4.F = anterior

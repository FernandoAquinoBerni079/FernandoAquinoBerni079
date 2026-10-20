# -*- coding: utf-8 -*-
"""Perfiles de página para la prueba en oficio del lote 1 (decisión de Fernando del 20-oct-2026: papel oficio
21,59 × 33,02 cm, vertical; comparar el margen de 1,27 cm con variantes de margen interior ampliado antes de fijarlo).

Medidas en cm. «espejo» = márgenes simétricos para impresión a doble cara: el interior queda del lado del lomo.
El perfil A4 es el del lote 1 original y se usa solo como referencia de comparación."""

PERFILES = {
    'A4': dict(nombre='A4 del lote 1 (referencia)', papel=(21.0, 29.7),
               interior=2.2, exterior=2.2, superior=2.0, inferior=2.0, espejo=False),
    'O1': dict(nombre='Oficio, márgenes estrechos de 1,27 cm (perfil de Algorítmica 3.º)', papel=(21.59, 33.02),
               interior=1.27, exterior=1.27, superior=1.27, inferior=1.27, espejo=False),
    'O2': dict(nombre='Oficio, interior de 2,0 cm para encuadernación (resto 1,27 cm, márgenes espejados)', papel=(21.59, 33.02),
               interior=2.0, exterior=1.27, superior=1.27, inferior=1.27, espejo=True),
    'O3': dict(nombre='Oficio, interior de 2,5 cm y exterior de 1,8 cm (márgenes espejados; línea parecida a la del A4)',
               papel=(21.59, 33.02), interior=2.5, exterior=1.8, superior=1.5, inferior=1.5, espejo=True),
}
ENCABEZADO_PIE = 0.6   # distancia del encabezado y del pie al borde, cm (perfiles oficio)
ANCHO_A4 = 16.6        # ancho útil para el que están escritos los anchos de tabla de las fuentes


def ancho_util(p):
    return round(p['papel'][0] - p['interior'] - p['exterior'], 2)

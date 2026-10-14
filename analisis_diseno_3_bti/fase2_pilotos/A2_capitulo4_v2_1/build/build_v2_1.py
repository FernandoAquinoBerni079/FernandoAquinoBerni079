# -*- coding: utf-8 -*-
"""Construye solo la guía docente v2.1 del Capítulo 4. El libro del estudiante no cambia (sigue siendo la v2
de A2_capitulo4_v2/). Las claves de la evaluación se obtienen construyendo el libro en una carpeta temporal,
con el mismo contenido y la misma semilla que la v2.
Uso: python3 build_v2_1.py  →  ../ADS_3BTI_CAP4_v2_1_GUIA_DOCENTE.docx"""
import os, tempfile
import build_v2
import guia_v2_1

AQUI = os.path.dirname(os.path.abspath(__file__))
ESTADO = [
    'Guía docente corregida (versión 2.1) para el cierre de la Fase 2. No está aprobada para la venta ni para uso en aula.',
    'Cambio respecto de la v2: nueva sección 3, con la correspondencia entre los 15 requisitos del catálogo y sus '
    'criterios de aceptación. El libro del estudiante no cambia.',
    'La capacidad de la ficha es una propuesta para el programa institucional (C3 del informe de Work). '
    'No es una capacidad oficial del MEC.',
]

if __name__ == '__main__':
    figs = build_v2.diagramas.generar()
    with tempfile.TemporaryDirectory() as tmp:
        claves = build_v2.libro_estudiante(figs, os.path.join(tmp, 'estudiante.docx'))
    ruta = os.path.join(os.path.dirname(AQUI), 'ADS_3BTI_CAP4_v2_1_GUIA_DOCENTE.docx')
    guia_v2_1.construir(ruta, claves, ESTADO)
    print(ruta)

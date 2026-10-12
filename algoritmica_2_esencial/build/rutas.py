# -*- coding: utf-8 -*-
"""Rutas del build, derivadas de la ubicación de este archivo (el build ya no depende de /home/claude).
SALIDA = carpeta donde se escriben DOCX/PDF; por defecto salida_v1_2 (v1.2). Se puede cambiar con la variable de entorno SALIDA."""
import os
B = os.path.dirname(os.path.abspath(__file__)) + '/'
RAIZ = os.path.dirname(B.rstrip('/')) + '/'
OUT = RAIZ + os.environ.get('SALIDA', 'salida_v1_2') + '/'
PS = RAIZ + 'pseint/'
SRC = RAIZ + 'src/'
TEMPLATE = B + 'plantilla_base.docx'

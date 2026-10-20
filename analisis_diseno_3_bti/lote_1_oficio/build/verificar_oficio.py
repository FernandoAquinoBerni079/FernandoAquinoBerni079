# -*- coding: utf-8 -*-
"""Ejecuta el verificador del lote 1 (`lote_1/build/verificar.py`, sin modificarlo en disco) sobre la prueba en oficio.

Uso: python3 lote_1_oficio/build/verificar_oficio.py O1|O2|O3

Se aplican solo estas sustituciones, todas por geometría o ruta (cada una debe aparecer exactamente una vez):
1. rutas del libro, la guía y el resultado de construcción → carpeta del perfil;
2. ancho esperado de las tablas de varias columnas: 16,6 cm (9411 twips) → ancho útil del perfil;
3. extensión esperada (libro 51 a 65 págs.; guía 18 a 22) → mismos rangos escalados por la razón entre el área útil
   del A4 y la del perfil (redondeo hacia afuera);
4. archivo de resultado → carpeta del perfil.
Todos los demás controles (A a J) quedan iguales, incluido G: helpers.py y maqueta.py deben seguir idénticos a los del
Capítulo 4 v2.1, y lo están, porque la prueba no los modifica."""
import os, sys, math
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
OFI = os.path.dirname(AQUI)
FUENTE = os.path.join(os.path.dirname(OFI), 'lote_1', 'build')
sys.path.insert(0, AQUI)
import perfiles as PF
from docx.shared import Cm

clave = sys.argv[1]
P = PF.PERFILES[clave]; A4 = PF.PERFILES['A4']
ANCHO = PF.ancho_util(P)
alto = lambda p: p['papel'][1] - p['superior'] - p['inferior']
r = (PF.ancho_util(A4) * alto(A4)) / (ANCHO * alto(P))
lib = (math.floor(51 * r), math.ceil(65 * r)); gui = (math.floor(18 * r), math.ceil(22 * r))
SAL = os.path.join(OFI, clave)
tw = int(Cm(ANCHO).twips)
src = open(os.path.join(FUENTE, 'verificar.py'), encoding='utf8').read()
SUST = [
    ("EST = os.path.join(RAIZ, 'ADS_3BTI_LOTE1_ESTUDIANTE')", "EST = %r" % os.path.join(SAL, 'ADS_3BTI_LOTE1_ESTUDIANTE_OFICIO_' + clave)),
    ("GUI = os.path.join(RAIZ, 'ADS_3BTI_LOTE1_GUIA_DOCENTE')", "GUI = %r" % os.path.join(SAL, 'ADS_3BTI_LOTE1_GUIA_DOCENTE_OFICIO_' + clave)),
    ("open(os.path.join(AQUI, 'resultado_construccion.json'), encoding='utf8')", "open(%r, encoding='utf8')" % os.path.join(SAL, 'resultado_construccion.json')),
    ("- 9411) > 15]", "- %d) > 15]" % tw),
    ("con tblGrid de 16,6 cm'", "con tblGrid de %s cm'" % str(ANCHO).replace('.', ',')),
    ("51 <= n_est <= 65)", "%d <= n_est <= %d)" % lib),
    ("(plan: 45 a 55 de capítulos + 6 a 8 de preliminares, con portada e índice)", "(rango A4 51 a 65, escalado al área útil del perfil: %d a %d)" % lib),
    ("18 <= n_gui <= 22)", "%d <= n_gui <= %d)" % gui),
    ("(plan: 18 a 22)", "(rango A4 18 a 22, escalado: %d a %d)" % gui),
    ("open(os.path.join(AQUI, 'verificacion_resultado.json'), 'w')", "open(%r, 'w')" % os.path.join(SAL, 'verificacion_resultado.json')),
]
for a, b in SUST:
    assert src.count(a) == 1, 'sustitución no aplicable: ' + a
    src = src.replace(a, b)
print('Perfil %s: ancho útil %.2f cm (%d twips); extensión libro %d-%d, guía %d-%d' % (clave, ANCHO, tw, *lib, *gui))
sys.argv = [os.path.join(FUENTE, 'verificar.py')]
exec(compile(src, os.path.join(FUENTE, 'verificar.py'), 'exec'), {'__file__': os.path.join(FUENTE, 'verificar.py'), '__name__': '__main__'})

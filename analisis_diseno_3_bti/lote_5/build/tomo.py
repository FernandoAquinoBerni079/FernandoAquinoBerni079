# -*- coding: utf-8 -*-
"""Índice de la fuente editable del tomo anual (18 capítulos, seis unidades). No construye nada: dice de dónde sale cada
capítulo construido y con qué función se arma, para que el constructor del tomo unificado use las mismas fuentes que
los lotes, sin copiarlas. Los capítulos que todavía no existen quedan marcados como pendientes.

Todos los lotes comparten: la maqueta del lote 1 (helpers.py y maqueta.py, idénticos a los del Capítulo 4 v2.1), el
perfil O3 (lote_2/build/oficio.py) y la fuente única del caso (lote_1/caso/dossier.py y mbokaja.py, ampliados por
lote_2/caso/requisitos.py, modelos.py y mbokaja_u2.py, y por lote_3/caso/diseno.py y mbokaja_u3.py).
Versión del lote 5: amplía la del lote 4 (lote_4/build/tomo.py, que no se modifica) con los Capítulos 14 a 16, que
además leen lote_5/caso/ (verificación, datos de prueba DP y Mbokaja U5), los resultados de las pruebas
(lote_5/resultados_pruebas/) y los fragmentos de código de las copias v2 de la referencia (lote_5/proyecto/).
El Capítulo 16 no tiene práctica independiente (el H5 es la actividad integradora): sus atributos de práctica existen y
están vacíos, y el armado del tomo no tiene que generar una «Práctica 16».
Uso: python3 lote_5/build/tomo.py   (comprueba que cada módulo construido tenga los atributos que usa el armado)"""
import os, sys, importlib.util
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(os.path.dirname(AQUI))

UNIDADES = [
    ('I', 'Comprender el problema y su contexto', (1, 3)),
    ('II', 'Especificar qué debe resolver el sistema', (4, 6)),
    ('III', 'Diseñar una solución coherente', (7, 9)),
    ('IV', 'Construir el prototipo por incrementos', (10, 13)),
    ('V', 'Verificar, validar y mejorar', (14, 16)),
    ('VI', 'Entregar y comunicar', (17, 18)),
]
# capítulo → (módulo de contenido, función de armado en el constructor del lote, estado)
CAPITULOS = {
    1: ('lote_1/build/cap1.py', 'lote_1/build/construir.py: capitulo1', 'versión de referencia (candidata O3 del lote 1)'),
    2: ('lote_1/build/cap2.py', 'lote_1/build/construir.py: capitulo2', 'versión de referencia (candidata O3 del lote 1)'),
    3: ('lote_1/build/cap3.py', 'lote_1/build/construir.py: capitulo3', 'versión de referencia (candidata O3 del lote 1)'),
    4: ('lote_2/build/cap4.py', 'lote_2/build/construir.py: capitulo4', 'versión de referencia (lote 2)'),
    5: ('lote_2/build/cap5.py', 'lote_2/build/construir.py: capitulo5', 'versión de referencia (lote 2)'),
    6: ('lote_2/build/cap6.py', 'lote_2/build/construir.py: capitulo6', 'versión de referencia (lote 2)'),
    7: ('lote_3/build/cap7.py', 'lote_3/build/construir.py: capitulo7', 'lote 3 v1.1, aceptado para integración'),
    8: ('lote_3/build/cap8.py', 'lote_3/build/construir.py: capitulo8', 'lote 3 v1.1, aceptado para integración'),
    9: ('lote_3/build/cap9.py', 'lote_3/build/construir.py: capitulo9', 'lote 3 v1.1, aceptado para integración'),
    10: ('lote_4/build/cap10.py', 'lote_4/build/construir.py: capitulo10', 'lote 4 v1.1, referencia para la integración'),
    11: ('lote_4/build/cap11.py', 'lote_4/build/construir.py: capitulo11', 'lote 4 v1.1, referencia para la integración'),
    12: ('lote_4/build/cap12.py', 'lote_4/build/construir.py: capitulo12', 'lote 4 v1.1, referencia para la integración'),
    13: ('lote_4/build/cap13.py', 'lote_4/build/construir.py: capitulo13', 'lote 4 v1.1, referencia para la integración'),
    14: ('lote_5/build/cap14.py', 'lote_5/build/construir.py: capitulo14', 'lote 5, para auditoría'),
    15: ('lote_5/build/cap15.py', 'lote_5/build/construir.py: capitulo15', 'lote 5, para auditoría'),
    16: ('lote_5/build/cap16.py', 'lote_5/build/construir.py: capitulo16', 'lote 5, para auditoría (sin práctica: H5)'),
}
SIN_PRACTICA = {16}
PRELIMINARES = ('lote_1/build/prelim.py', 'lote_1/build/construir.py: preliminares')
ATRIBUTOS = ['NUM', 'UNIDAD', 'CAPITULO', 'TITULO', 'ENCUENTROS', 'SECCIONES', 'ROTULO_CAPACIDAD', 'CAPACIDAD', 'TEMA',
             'INDICADORES', 'TIEMPO', 'APERTURA', 'ARTICULACION', 'PRACTICA_TITULO', 'PRACTICA_INTRO', 'NIVELES',
             'PRACTICA_CONTROL', 'REPASO', 'CALENDARIO', 'EVAL_ID', 'EVAL_TITULO', 'EVAL_TEXTO_BASE', 'EVAL_ITEMS', 'EVAL_PUNTAJE']

if __name__ == '__main__':
    sys.path[:0] = [os.path.join(ADS, 'lote_5', 'caso'), os.path.join(ADS, 'lote_4', 'caso'), os.path.join(ADS, 'lote_3', 'caso'), os.path.join(ADS, 'lote_2', 'caso'), os.path.join(ADS, 'lote_1', 'build'), os.path.join(ADS, 'lote_1', 'caso')]
    fallos = 0
    for n, (ruta, armado, estado) in sorted(CAPITULOS.items()):
        spec = importlib.util.spec_from_file_location('cap%d_tomo' % n, os.path.join(ADS, ruta))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        falta = [a for a in ATRIBUTOS if not hasattr(m, a)]
        if n in SIN_PRACTICA:   # los atributos de práctica existen, vacíos
            falta += [a for a in ('PRACTICA_TITULO', 'PRACTICA_CONTROL') if getattr(m, a, 0) is not None]
            falta += [a for a in ('PRACTICA_INTRO', 'NIVELES') if getattr(m, a, 0) != []]
        fallos += bool(falta) or m.NUM != n
        print('Capítulo %2d  %-24s %-40s %s%s' % (n, ruta, armado, estado, ('  FALTAN: %s' % falta) if falta else ''))
    print('Pendientes: capítulos %s' % ', '.join(str(n) for n in range(17, 19)))
    sys.exit(1 if fallos else 0)

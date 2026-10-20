# -*- coding: utf-8 -*-
"""Índice de la fuente editable del tomo anual (18 capítulos, seis unidades). No construye nada: dice de dónde sale cada
capítulo construido y con qué función se arma, para que el constructor del tomo unificado use las mismas fuentes que
los lotes, sin copiarlas. Los capítulos que todavía no existen quedan marcados como pendientes.

Todos los lotes comparten: la maqueta del lote 1 (helpers.py y maqueta.py, idénticos a los del Capítulo 4 v2.1), el
perfil O3 (lote_2/build/oficio.py) y la fuente única del caso (lote_1/caso/dossier.py y mbokaja.py, ampliados por
lote_2/caso/requisitos.py, modelos.py y mbokaja_u2.py).
Uso: python3 lote_2/build/tomo.py   (comprueba que cada módulo construido tenga los atributos que usa el armado)"""
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
    1: ('lote_1/build/cap1.py', 'lote_1/build/construir.py: capitulo1', 'aprobado (candidata O3 del lote 1)'),
    2: ('lote_1/build/cap2.py', 'lote_1/build/construir.py: capitulo2', 'aprobado (candidata O3 del lote 1)'),
    3: ('lote_1/build/cap3.py', 'lote_1/build/construir.py: capitulo3', 'aprobado (candidata O3 del lote 1)'),
    4: ('lote_2/build/cap4.py', 'lote_2/build/construir.py: capitulo4', 'lote 2, para auditoría'),
    5: ('lote_2/build/cap5.py', 'lote_2/build/construir.py: capitulo5', 'lote 2, para auditoría'),
    6: ('lote_2/build/cap6.py', 'lote_2/build/construir.py: capitulo6', 'lote 2, para auditoría'),
}
PRELIMINARES = ('lote_1/build/prelim.py', 'lote_1/build/construir.py: preliminares')
ATRIBUTOS = ['NUM', 'UNIDAD', 'CAPITULO', 'TITULO', 'ENCUENTROS', 'SECCIONES', 'ROTULO_CAPACIDAD', 'CAPACIDAD', 'TEMA',
             'INDICADORES', 'TIEMPO', 'APERTURA', 'ARTICULACION', 'PRACTICA_TITULO', 'PRACTICA_INTRO', 'NIVELES',
             'PRACTICA_CONTROL', 'REPASO', 'CALENDARIO', 'EVAL_ID', 'EVAL_TITULO', 'EVAL_TEXTO_BASE', 'EVAL_ITEMS', 'EVAL_PUNTAJE']

if __name__ == '__main__':
    sys.path[:0] = [os.path.join(ADS, 'lote_2', 'caso'), os.path.join(ADS, 'lote_1', 'build'), os.path.join(ADS, 'lote_1', 'caso')]
    fallos = 0
    for n, (ruta, armado, estado) in sorted(CAPITULOS.items()):
        spec = importlib.util.spec_from_file_location('cap%d_tomo' % n, os.path.join(ADS, ruta))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        falta = [a for a in ATRIBUTOS if not hasattr(m, a)]
        fallos += bool(falta) or m.NUM != n
        print('Capítulo %2d  %-24s %-40s %s%s' % (n, ruta, armado, estado, ('  FALTAN: %s' % falta) if falta else ''))
    print('Pendientes: capítulos %s' % ', '.join(str(n) for n in range(7, 19)))
    sys.exit(1 if fallos else 0)

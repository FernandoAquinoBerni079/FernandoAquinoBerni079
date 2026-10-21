# -*- coding: utf-8 -*-
"""Carga de las fuentes aprobadas de los seis lotes, sin copiarlas ni modificarlas.

Cada lote tiene su constructor (lote_N/build/construir.py) con las funciones de armado de sus capítulos, su apertura
de unidad y sus prácticas, y su guía (guia.py o guia_uN.py). Los seis constructores se llaman igual («construir»), y
los lotes 1 y 2 comparten además los nombres «guia» y «diagramas». Por eso cada lote se carga con su propio espacio de
nombres: antes de cargarlo se retiran de sys.modules esos nombres repetidos, y el módulo cargado queda guardado como
construir_lN. Los módulos con nombre propio (cap1 a cap18, piezas_uN, guia_uN, caso/…) se comparten, igual que la
maqueta del lote 1 (helpers, maqueta, comun) y el perfil O3 del lote 2 (oficio), que son los mismos en todos los lotes.

Versiones que se cargan (las aprobadas): lote 1 en su candidata O3 (las funciones del lote 1 con el perfil O3, el mismo
que aplicó lote_1_oficio_candidata/build/construir_candidata.py), lote 2 v1.0, lote 3 v1.1, lote 4 v1.1, lote 5 v1.0 y
lote 6 v1.1. No se escribe nada dentro de las carpetas de los lotes: las figuras se generan en coleccion/build/figs/."""
import os, sys, importlib.util
sys.dont_write_bytecode = True

AQUI = os.path.dirname(os.path.abspath(__file__))
COL = os.path.dirname(AQUI)
ADS = os.path.dirname(COL)
REPETIDOS = ('construir', 'guia', 'diagramas')
GUIAS = {1: 'guia', 2: 'guia', 3: 'guia_u3', 4: 'guia_u4', 5: 'guia_u5', 6: 'guia_u6'}
DIAGRAMAS = {1: 'diagramas', 2: 'diagramas', 3: 'diagramas_u3', 4: 'diagramas_u4', 5: 'diagramas_u5', 6: 'diagramas_u6'}
UNIDADES = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI'}
CAPITULOS = {1: (1, 2, 3), 2: (4, 5, 6), 3: (7, 8, 9), 4: (10, 11, 12, 13), 5: (14, 15, 16), 6: (17, 18)}
APROBADOS = {   # documentos aprobados de cada lote (base de la equivalencia)
    1: {'libro': 'lote_1_oficio_candidata/ADS_3BTI_LOTE1_ESTUDIANTE_OFICIO_O3_CANDIDATA.docx',
        'guia': 'lote_1_oficio_candidata/ADS_3BTI_LOTE1_GUIA_DOCENTE_OFICIO_O3_CANDIDATA.docx', 'cuaderno': None},
}
for _n in range(2, 7):
    APROBADOS[_n] = {k: 'lote_%d/ADS_3BTI_LOTE%d_%s_OFICIO_O3.docx' % (_n, _n, v)
                     for k, v in (('libro', 'ESTUDIANTE'), ('guia', 'GUIA_DOCENTE'), ('cuaderno', 'CUADERNO_PRACTICAS'))}
VERSIONES = {1: 'candidata O3 (lote_1_oficio_candidata)', 2: 'v1.0', 3: 'v1.1 (cierre de auditoría)',
             4: 'v1.1 (cierre de auditoría)', 5: 'v1.0', 6: 'v1.1 (cierre de auditoría)'}

LOTES, GUIA, DIAG = {}, {}, {}
O = None


def _cargar_lote(n):
    # «construir» se repite en los seis lotes; «guia» y «diagramas», solo en los lotes 1 y 2 (los lotes 3 a 6 usan los
    # del lote 2, que quedan cargados)
    for nombre in REPETIDOS if n == 2 else ('construir',):
        sys.modules.pop(nombre, None)
    build = os.path.join(ADS, 'lote_%d' % n, 'build')
    if build in sys.path:
        sys.path.remove(build)
    sys.path.insert(0, build)
    spec = importlib.util.spec_from_file_location('construir', os.path.join(build, 'construir.py'))
    m = importlib.util.module_from_spec(spec)
    sys.modules['construir'] = m
    spec.loader.exec_module(m)
    assert os.path.dirname(m.__file__) == build
    sys.modules['construir_l%d' % n] = m
    g = sys.modules[GUIAS[n]]
    d = sys.modules[DIAGRAMAS[n]]
    assert os.path.dirname(g.__file__) == build and os.path.dirname(d.__file__) == build, (n, g.__file__, d.__file__)
    return m, g, d


def cargar():
    """Carga los seis lotes en orden y devuelve (O, LOTES, GUIA, DIAG). El perfil O3 se carga primero, como en los
    lotes 2 a 6; el lote 1 lo recibe igual que en su candidata O3."""
    global O
    if LOTES:
        return O, LOTES, GUIA, DIAG
    sys.path.insert(0, os.path.join(ADS, 'lote_2', 'build'))
    import oficio as O
    for n in range(1, 7):
        LOTES[n], GUIA[n], DIAG[n] = _cargar_lote(n)
    # los nombres repetidos quedan apuntando al lote 2, que es lo que esperan los lotes 3 a 6
    sys.modules.pop('construir', None)
    assert sys.modules['diagramas'] is DIAG[2] and sys.modules['guia'] is GUIA[2]
    for n in range(1, 7):
        assert LOTES[n].H is O.H if hasattr(LOTES[n], 'H') else True
    return O, LOTES, GUIA, DIAG


def capitulo(n):
    """Módulo de contenido del capítulo n (cap1 a cap18), el mismo que usa su lote."""
    return sys.modules['cap%d' % n]


def lote_de(cap):
    return next(n for n, caps in CAPITULOS.items() if cap in caps)


if __name__ == '__main__':
    O, L, G_, D_ = cargar()
    for n in range(1, 7):
        print('lote %d: %s · %s · %s · capítulos %s' % (n, os.path.relpath(L[n].__file__, ADS), os.path.relpath(G_[n].__file__, ADS),
                                                      os.path.relpath(D_[n].__file__, ADS), CAPITULOS[n]))
    for c in range(1, 19):
        print('cap%d' % c, os.path.relpath(capitulo(c).__file__, ADS), hasattr(L[lote_de(c)], 'capitulo%d' % c))
    print('helpers:', os.path.relpath(O.H.__file__, ADS), '· oficio:', os.path.relpath(O.__file__, ADS))

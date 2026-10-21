# -*- coding: utf-8 -*-
"""Fragmentos de código del lote 6, LEÍDOS del paquete de entrega modelo (lote_6/proyecto/), con el mismo método y la
misma ficha que los de los lotes 4 y 5 (que no se modifican).
FRAGMENTOS van en el libro: dos comprobaciones del comprobador de entrega. REFERENCIA va solo en la guía docente."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(AQUI)), 'lote_4', 'build'))
import fragmentos as F4
PROY = os.path.join(os.path.dirname(AQUI), 'proyecto')
ANCHO = F4.ANCHO
ARCHIVO = 'paquete_entrega_modelo/comprobar_entrega.php'

FRAGMENTOS = {
    'Código 17.1': (ARCHIVO, '// D. Recursos', '}', 1,
                    'Cada recurso que no es código tiene que estar en la ficha de procedencia.',
                    'RS-02; 17.3 (procedencia y licencias)', 'Los archivos de public/ y ENTREGA/PROCEDENCIA.md',
                    'Una incoherencia [D] por cada recurso sin su fila', 'php comprobar_entrega.php (paquete de Mbokaja)'),
    'Código 17.2': (ARCHIVO, '// A. Comandos', '}', 1,
                    'Cada comando de la guía de instalación nombra un archivo que existe en el paquete.',
                    'C10; 17.1 (guía de instalación)', 'Los bloques de comandos de ENTREGA/INSTALAR.md',
                    'Una incoherencia [A] por cada comando que nombra un archivo inexistente',
                    'php comprobar_entrega.php (paquete de Mbokaja)'),
}
REFERENCIA = {
    'Referencia R-8': (ARCHIVO, "preg_match_all('/^- prueba", '}', 1,
                       'Las pruebas de la lista de entrega se ejecutan y tienen que dar su línea «Resultado:».',
                       '17.4; coherencia del paquete (H6)', 'La lista de entrega', 'Una incoherencia [C] por prueba que falla',
                       'php comprobar_entrega.php'),
    'Referencia R-9': (ARCHIVO, '// F. La misma', '}', 2,
                       'La versión declarada tiene que ser la misma en todos los documentos.',
                       '17.4; coherencia del paquete (H6)', 'LEEME.txt y los documentos de ENTREGA/',
                       'Una incoherencia [F] si alguno no declara su versión o si difieren', 'php comprobar_entrega.php'),
}
TODOS = dict(FRAGMENTOS, **REFERENCIA)


def extraer(fid):
    archivo, desde, hasta, ocurrencia = TODOS[fid][:4]
    lineas = open(os.path.join(PROY, archivo), encoding='utf8').read().split('\n')
    i = next(k for k, l in enumerate(lineas) if l.startswith(desde))
    vistas = 0
    for j in range(i, len(lineas)):
        if lineas[j].startswith(hasta) and (j > i or desde.startswith(hasta)):
            vistas += 1
            if vistas == ocurrencia:
                return [l.rstrip() for l in lineas[i:j + 1]]
    raise ValueError('fragmento sin final: %s' % fid)


def ficha(fid):
    a, _, _, _, prop, req, ent, res, prueba = TODOS[fid]
    return {'archivo': 'lote_6/proyecto/' + a, 'proposito': prop, 'requisito': req, 'entradas': ent, 'resultado': res,
            'prueba': prueba}


def del_capitulo(n):
    return [f for f in FRAGMENTOS if f.startswith('Código %d.' % n)]


if __name__ == '__main__':
    for f in TODOS:
        ls = extraer(f)
        print('%-15s %3d líneas, máx. %d' % (f, len(ls), max(len(l) for l in ls)))

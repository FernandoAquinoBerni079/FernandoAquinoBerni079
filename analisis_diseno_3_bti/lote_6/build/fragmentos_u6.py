# -*- coding: utf-8 -*-
"""Fragmentos de código del lote 6, LEÍDOS del paquete de entrega modelo (lote_6/proyecto/), con el mismo método y la
misma ficha que los de los lotes 4 y 5 (que no se modifican).
FRAGMENTOS van en el libro: dos revisiones de la inspección estática del docente. REFERENCIA va solo en la guía docente.
v1.1 (auditoría del lote 6): los fragmentos se leen de las herramientas del docente (proyecto/herramientas/), que viven
fuera del paquete; el comprobador que traía el paquete se retiró (queda en version_1_0/)."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(AQUI)), 'lote_4', 'build'))
import fragmentos as F4
PROY = os.path.join(os.path.dirname(AQUI), 'proyecto')
ANCHO = F4.ANCHO
INSPECTOR = 'herramientas/inspeccionar_entrega.php'
EJECUTOR = 'herramientas/probar_en_aislamiento.php'
INSPECCIONAR = 'php herramientas/inspeccionar_entrega.php paquete_mbokaja'

FRAGMENTOS = {
    'Código 17.1': (INSPECTOR, '// D. Recursos', '}', 2,
                    'Cada recurso que no es código tiene que estar en la ficha de procedencia.',
                    'RS-02; 17.3 (procedencia y licencias)', 'Los archivos de public/ y ENTREGA/PROCEDENCIA.md',
                    'Una incoherencia [D] por cada recurso sin su fila', INSPECCIONAR),
    'Código 17.2': (INSPECTOR, '// A. Comandos', '}', 1,
                    'Cada comando de la guía tiene una forma conocida y nombra un archivo que existe en el paquete. '
                    'La guía solo se lee: ningún comando se ejecuta.',
                    'C10; 17.1 (guía de instalación)', 'Los bloques de comandos de ENTREGA/INSTALAR.md',
                    'Una incoherencia [A] por cada comando de forma desconocida o que nombra un archivo inexistente',
                    INSPECCIONAR),
}
REFERENCIA = {
    'Referencia R-8': (EJECUTOR, '// Solo las pruebas', '}', 1,
                       'Solo se ejecutan las pruebas de la lista cerrada de la herramienta, armadas como lista de '
                       'argumentos (sin consola), en la copia descartable y con tiempo límite.',
                       '17.4; coherencia del paquete (H6); herramientas/LEEME.md', 'La copia descartable del paquete',
                       'Una incoherencia [C] por cada prueba de la lista que no termina bien',
                       'php herramientas/probar_en_aislamiento.php paquete_mbokaja (en aislamiento)'),
    'Referencia R-9': (INSPECTOR, '// C. Pruebas declaradas', '}', 1,
                       'Cada prueba declarada en la lista de entrega tiene que estar en la lista cerrada. No se ejecuta.',
                       '17.4; coherencia del paquete (H6)', 'ENTREGA/LISTA_ENTREGA.md',
                       'Una incoherencia [C] por cada prueba declarada fuera de la lista cerrada o que falta',
                       INSPECCIONAR),
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

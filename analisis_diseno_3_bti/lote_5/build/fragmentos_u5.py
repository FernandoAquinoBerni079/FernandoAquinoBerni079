# -*- coding: utf-8 -*-
"""Fragmentos de código del lote 5, LEÍDOS de las copias v2 de la referencia docente (lote_5/proyecto/), con el mismo
método y la misma ficha que los del lote 4 (lote_4/build/fragmentos.py, que no se modifica).

FRAGMENTOS van en el libro: lo necesario para entender la corrección de IN-02 y el cambio SC-02 (decisión 3 de
Fernando). REFERENCIA va solo en la guía docente: la solución completa."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(AQUI)), 'lote_4', 'build'))
import fragmentos as F4
PROY = os.path.join(os.path.dirname(AQUI), 'proyecto')
ANCHO = F4.ANCHO

FRAGMENTOS = {
    'Código 16.1': ('referencia_docente_v2/public/_plantilla.php', '// Patrón POST-redirección-GET', '}', 1,
                    'Corrección de IN-02: si la operación falló, se guarda también lo escrito para volver a mostrarlo.',
                    'IN-02; RNF-01; patrón POST-redirección-GET (Capítulo 12)', 'Resultado, destino y datos enviados',
                    'Aviso y, si hubo error, los datos escritos (sin la ficha CSRF ni la contraseña)', 'prueba_in02.sh'),
    'Código 16.2': ('referencia_docente_v2/public/lectores.php', '<label>Tipo <select name="tipo">', '</select></label>', 1,
                    'El formulario vuelve a mostrar el tipo que estaba elegido.',
                    'IN-02; RF-11', 'Los datos del último envío fallido del alta de lector', 'La opción elegida, marcada',
                    'prueba_in02.sh'),
    'Código 16.3': ('referencia_docente_v2_sc02/src/reglas.php', "    if ((int) $total['n'] === 0) {", '    }', 1,
                    'SC-02, cambio aprobado: un mes sin préstamos da un resultado correcto con el mensaje de vacío ME-14.',
                    'SC-02; OP-05 v1.2; RF-09 (criterio nuevo)', 'El total del mes, contado de nuevo',
                    'ME-14 sin filas, o el informe de siempre', 'P-09 (caso del mes vacío)'),
}
REFERENCIA = {
    'Referencia R-4': ('referencia_docente_v2/public/_plantilla.php', '// v2 (IN-02): los datos del último', '}', 3,
                       'Los datos del último envío fallido, una sola vez, y las funciones que los muestran escapados.',
                       'IN-02; seguridad de la salida (e())', 'La sesión', 'Datos del formulario o un arreglo vacío',
                       'prueba_in02.sh'),
    'Referencia R-5': ('referencia_docente_v2/public/lectores.php', '<h2>Alta de un lector</h2>', '</form>', 1,
                       'El formulario completo del alta de lector, corregido.', 'IN-02; OA-03', 'Los datos conservados',
                       'Campos con lo escrito y el tipo elegido', 'prueba_in02.sh'),
    'Referencia R-6': ('referencia_docente_v2_sc02/src/mensajes.php', '    // SC-02 (Unidad V)', "    'ME-14'", 1,
                       'El mensaje nuevo de SC-02, con la regla de los mensajes del Capítulo 8.', 'SC-02; Tabla 8.6 v1.2',
                       'El mes', 'Texto de ME-14', 'P-09 (caso del mes vacío)'),
    'Referencia R-7': ('referencia_docente_v2_sc02/public/informe.php', "<?php if ($r['ok'] && $r['total'] > 0)", "<?php if", 1,
                       'PT-09 muestra la tabla solo si el mes tiene préstamos; si no, ME-14.', 'SC-02; PT-09',
                       'El resultado de OP-05', 'La tabla o el mensaje', 'prueba_http.sh y P-09'),
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
    return {'archivo': 'lote_5/proyecto/' + a, 'proposito': prop, 'requisito': req, 'entradas': ent, 'resultado': res,
            'prueba': prueba}


def del_capitulo(n):
    return [f for f in FRAGMENTOS if f.startswith('Código %d.' % n)]


if __name__ == '__main__':
    for f in TODOS:
        ls = extraer(f)
        print('%-15s %-48s %3d líneas, máx. %d' % (f, TODOS[f][0][-40:], len(ls), max(len(l) for l in ls)))
        if len(ls) < 6:
            print('\n'.join(ls))

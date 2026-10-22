# -*- coding: utf-8 -*-
"""PDF de aprobación de 2.º BTC: 13 figuras (R1 → R3), planes 33-35 y filas 19-20 del plan anual (R1 → R3).
Uso: python3 comparacion_2btc.py <carpeta Antes_R1 de las figuras> <carpeta PDF R1 de 2.º>"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(os.path.dirname(BASE), 'build_comun'))
import comparacion as C

ANT, PDF1 = sys.argv[1], sys.argv[2]
FIG = os.path.join(BASE, 'figuras_R3'); PDF3 = os.path.join(BASE, 'pdf_revision_R3')
FIGURAS = [
    (1, 'Partes de la planilla', 'Clase 1 · Práctica 1', 'Propuesta incorporada; en R3, ícono neutro en la barra de título.',
     'Más legible que R1. El ícono verde se parecía al de una planilla comercial (O-2-05).'),
    (2, 'Dirección de celda y rango', 'Clase 2 · Práctica 2', 'Propuesta incorporada; en R3 la celda B3 muestra «SIMPLE» en lugar de «900.000».',
     'En el caso, la columna B es Régimen y el importe está en C: un importe en B3 contradecía la Figura 1.'),
    (3, 'Cómo se lee una fórmula', 'Clase 4 · Práctica 4', 'Propuesta incorporada sin cambios.',
     '=SUMA(C2:C17)*12 sobre la columna del honorario: 12.150.000 × 12 = 145.800.000.'),
    (4, 'Referencias relativas y absolutas', 'Clase 5 · Práctica 5', 'Propuesta con el subtítulo corregido («absoliutas» → «absolutas»).',
     'Errata de la propuesta.'),
    (5, 'Elegí el gráfico según la pregunta', 'Clase 8 · Práctica 8', 'Reconstruida en vector con los datos del caso.',
     'La propuesta usaba cifras que no salen del caso.'),
    (6, 'Del dato al informe', 'Clase 10 · Práctica 10', 'Propuesta incorporada sin cambios.', '145.800.000 − 91.800.000 = 54.000.000, coherente con la práctica.'),
    (7, 'Vector o mapa de bits', 'Clase 11 · Práctica 11', 'Propuesta incorporada sin cambios.', 'La figura R1 tenía texto superpuesto.'),
    (8, 'Nodos y manijas', 'Clase 13 · Práctica 13', 'Reconstruida en vector con una curva Bézier exacta y la variante con la manija desplazada.',
     'La geometría de la propuesta no mostraba manijas tangentes reales.'),
    (9, 'Alinear, agrupar y soldar', 'Clase 14 · Práctica 14', 'Reconstruida en vector con los mismos tamaños antes y después.',
     'La propuesta cambiaba el tamaño de los objetos y confundía soldar con escalar.'),
    (10, 'SI anidado', 'Clase 16 · Práctica 16', 'Propuesta incorporada sin cambios.', 'Usa la columna C (honorario); la figura R1 del laboratorio usaba B.'),
    (11, 'Tabla dinámica', 'Clase 17 · Práctica 17', 'Propuesta incorporada sin cambios.', 'Totales del caso y control de cierre.'),
    (12, 'Portal de la DNIT', 'Clase 19 · Práctica 19', 'Propuesta incorporada sin cambios.', 'Mapa esquemático: no reproduce la interfaz oficial.'),
    (13, 'Factura electrónica', 'Clase 20 · Práctica 20', 'Propuesta incorporada sin cambios; pie actualizado.', 'Distingue DE, DTE y KuDE, y la entrega según el receptor.'),
]
paginas = []
for n, tit, uso, cambio, motivo in FIGURAS:
    paginas.append(dict(codigo='Figura %d' % n, titulo='%s (%s)' % (tit, uso), antes=os.path.join(ANT, 'Figura_%02d.png' % n),
                        despues=os.path.join(FIG, 'R3_Figura_%02d.png' % n), rot_antes='R1', rot_despues='R3 (propuesta para aprobar)',
                        cambio=cambio, motivo=motivo))
P1 = os.path.join(PDF1, 'Informatica_2_BTC_Planes_de_clase_corregidos.pdf')
P3 = os.path.join(PDF3, 'Informatica_2_BTC_Planes_de_clase_R3.pdf')
ENC = [
    (33, 'R1: Clase 19 sola (teoría del portal DNIT). La Práctica 19 tenía encuentro propio (Plan 34).',
     'R3: Clase 19 con la Práctica 19 integrada en el mismo encuentro.'),
    (34, 'R1: continuación práctica de la Clase 19 (Práctica 19).', 'R3: teoría de la Clase 20 (factura electrónica) en encuentro propio.'),
    (35, 'R1: Clase 20 + Práctica 20 + Evaluación de la Unidad 6 en 80 minutos.',
     'R3: Práctica 20 (50 min) + Evaluación de la Unidad 6 (20 min).'),
]
for n, a, b in ENC:
    paginas.append(dict(codigo='Encuentro %d' % n, titulo='Plan de Clase N.º %d' % n, antes=(P1, n + 1, ('Plan de Clase N.º %d —' % n, 'Recursos')), despues=(P3, n + 1, ('Plan de Clase N.º %d —' % n, 'Recursos')),
                        rot_antes='R1', rot_despues='R3 (igual que R2)', cambio=a + ' → ' + b,
                        motivo='En 80 min (2 HC) no entraban la teoría de la Clase 20, la Práctica 20 y la evaluación de unidad (H-2-05). '
                               'Se redistribuye sin cambiar los 36 encuentros ni las 72 HC.'))
paginas.append(dict(apilar=True, codigo='Plan anual', titulo='Filas 19 y 20 (Unidad 6)', antes=(os.path.join(PDF1, 'Informatica_2_BTC_Plan_anual_corregido.pdf'), 3, (20, 285, 915, 420)),
                    despues=(os.path.join(PDF3, 'Informatica_2_BTC_Plan_anual_R3.pdf'), 3, (20, 285, 915, 420)), rot_antes='R1', rot_despues='R3 (igual que R2)',
                    cambio='Fila 19: 2 h con la Práctica 19 integrada. Fila 20: 4 h con la Práctica 20 en encuentro propio. Bandas de unidad con su capacidad.',
                    motivo='Sincronía con los planes 33-35 (H-2-05) y capacidades del programa en el plan anual (H-2-07).'))
salida = os.path.join(BASE, 'COMPARACION_PARA_APROBACION_2BTC.pdf')
print(C.armar(paginas, salida, 'Informática 2.º BTC · Comparación para aprobación · R1 → R3 · 22 de octubre de 2026'), 'páginas →', salida)

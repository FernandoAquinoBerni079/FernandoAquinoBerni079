# -*- coding: utf-8 -*-
"""Evaluación técnica del grosor y la encuadernación de los documentos anuales → coleccion/EVALUACION_ENCUADERNACION.md.
Las páginas salen de los PDF y del índice del libro (páginas de inicio de cada unidad). Los espesores y gramajes son
valores de referencia del papel obra o bond corriente y se declaran como supuestos: el dato final lo da la imprenta
con su papel. No divide el libro: solo estima cómo quedarían dos volúmenes por etapa.
Uso: python3 -B coleccion/build/encuadernacion.py"""
import os, json, math
AQUI = os.path.dirname(os.path.abspath(__file__))
COL = os.path.dirname(AQUI)
import pymupdf

PAPEL = [(75, 0.100), (80, 0.105), (90, 0.115)]   # gramaje (g/m²) y espesor por hoja (mm), supuestos de referencia
TAPA_MM = 0.6                                     # dos tapas de cartulina de unos 0,3 mm
AREA = 0.2159 * 0.3302                            # oficio, m²
r = json.load(open(os.path.join(COL, 'resultado_construccion.json'), encoding='utf8'))
pags = r['paginas']
ind = dict(r['indice_libro'])
UNI = ['Unidad I — Comprender el problema y su contexto', 'Unidad II — Especificar qué debe resolver el sistema',
       'Unidad III — Diseñar una solución coherente', 'Unidad IV — Construir el prototipo por incrementos',
       'Unidad V — Verificar, validar y mejorar', 'Unidad VI — Entregar y comunicar']
ini = [ind[u] for u in UNI]
total = pags['libro']
por_unidad = [(UNI[k].split(' — ')[0], ini[k], (ini[k + 1] - 1) if k < 5 else total) for k in range(6)]
prelim = ini[0] - 1
vol1 = ini[3] - 1               # portada, índice, preliminares y Unidades I a III (corte en el H3, Encuentro 18)
vol2 = total - ini[3] + 1 + 4   # Unidades IV a VI, más portada e índice propios (unas 4 páginas)


def hojas(p):
    return math.ceil(p / 2)


def fila(nombre, p):
    h = hojas(p)
    lomos = ' · '.join(('%.1f mm (%d g)' % (h * e + TAPA_MM, g)).replace('.', ',') for g, e in PAPEL)
    peso = h * AREA * 80 + 2 * AREA * 250   # con papel de 80 g y tapas de 250 g
    return '| %s | %d | %d | %s | %.0f g |' % (nombre, p, h, lomos, peso)


def peso(p, g):
    return round(hojas(p) * AREA * g + 2 * AREA * 250)


md = ['# Evaluación técnica del grosor y la encuadernación', '',
      '**Colección ADS 3.º BTI · documentos anuales v0.2 · oficio 21,59 × 33,02 cm, impresión a doble faz**', '',
      'Este informe compara un tomo anual con dos volúmenes por etapa. **Decisión aprobada (cierre editorial): un único tomo anual.** '
      'Los espesores y los gramajes son supuestos de referencia del papel obra o bond corriente; la imprenta tiene '
      'que confirmarlos con su papel antes de fijar el lomo.', '',
      '## 1. Extensión medida', '',
      '| Documento | Páginas | Hojas | Lomo estimado (interior + tapas) | Peso estimado (80 g, tapas de 250 g) |',
      '|---|---|---|---|---|',
      fila('Libro del estudiante (tomo anual)', total), fila('Guía docente anual', pags['guia']),
      fila('Cuaderno anual de prácticas', pags['cuaderno']), '',
      'Páginas del libro por parte:', '',
      '| Parte | Desde | Hasta | Páginas |', '|---|---|---|---|',
      '| Portada, índice y preliminares | 1 | %d | %d |' % (prelim, prelim)]
md += ['| %s | %d | %d | %d |' % (u, a, b, b - a + 1) for u, a, b in por_unidad]
md += ['', '## 2. Opciones para el libro del estudiante', '',
       '**A. Un tomo anual (situación actual).**',
       '- %d páginas, %d hojas: un lomo de unos %.0f a %.0f mm según el papel.' % (
           total, hojas(total), hojas(total) * PAPEL[0][1] + TAPA_MM, hojas(total) * PAPEL[-1][1] + TAPA_MM),
       '- Ese grosor entra con holgura en la encuadernación rústica fresada (con cola PUR, que abre mejor y retiene las hojas '
       'con el uso diario) y en el anillado de espiral o doble alambre (aro de unos 16 a 19 mm).',
       '- El margen interior de 2,5 cm del perfil O3 alcanza para el fresado, que consume unos 3 a 5 mm del lomo, y para '
       'los agujeros del anillado.',
       '- Ventajas: una sola compra, una sola paginación (la que citan la guía, el cuaderno y el índice) y un solo lomo.',
       '- Riesgo: el peso para llevarlo todos los días: unos %d g con papel de 80 g y unos %d g con papel de 75 g.' % (
           peso(total, 80), peso(total, 75)),
       '',
       '**B. Dos volúmenes por etapa (Unidades I a III y IV a VI).**',
       '- El corte natural es el H3 (Encuentro 18), al cierre de la primera etapa.',
       '- Volumen 1: unas %d páginas (%d hojas). Volumen 2: unas %d páginas (%d hojas), con portada e índice propios.' % (
           vol1, hojas(vol1), vol2, hojas(vol2)),
       '- Los volúmenes quedan desparejos, porque la primera etapa trae los preliminares.',
       '- Costos que agrega: una portada, un índice y una tapa más, y una segunda paginación. La guía cita páginas del '
       'libro (por ejemplo, la del diagnóstico de entrada), así que habría que rehacer esas remisiones por volumen. El '
       'cuaderno cita tablas y figuras por su número, que no cambia.',
       '- Conviene solo si la editorial quiere vender por etapa o si la escuela pide un libro más liviano.',
       '', '## 3. Guía docente y cuaderno', '',
       '- **Guía docente anual** (%d páginas, %d hojas): un solo tomo; rústica o anillado. El anillado deja la guía abierta '
       'sobre el escritorio durante la clase.' % (pags['guia'], hojas(pags['guia'])),
       '- **Cuaderno de prácticas** (%d páginas, %d hojas): el estudiante escribe en él, así que conviene que abra plano: '
       'anillado de espiral o doble alambre. El grapado al lomo en oficio necesita pliegos del doble del tamaño oficio, que no '
       'todas las imprentas manejan.' % (pags['cuaderno'], hojas(pags['cuaderno'])),
       '', '## 4. Recomendación técnica', '',
       '- **Mantener el tomo anual**, en rústica fresada con cola PUR o en anillado, porque el grosor (unos %d mm) no exige '
       'dividirlo.' % round(hojas(total) * PAPEL[1][1] + TAPA_MM),
       '- La división en dos volúmenes queda como opción comercial, no técnica. Si se decide, el corte va en el H3 y hay que '
       'rehacer las remisiones de página de la guía.',
       '', '## 5. Puntos para decidir con la imprenta', '',
       '- El papel exacto (gramaje y espesor) y, con él, el lomo final.',
       '- Si las unidades tienen que empezar en página impar. Hoy empiezan en la página siguiente a la anterior, como en los '
       'lotes aprobados. Pasarlas a página impar agregaría hasta 6 páginas en blanco intencionales.',
       '- La cantidad final de páginas ajustada al pliego de la imprenta: múltiplo de 4, de 8 o de 16, según la máquina.',
       '- La tapa: el diseño de tapa no forma parte de este paso.']
open(os.path.join(COL, 'EVALUACION_ENCUADERNACION.md'), 'w', encoding='utf8').write('\n'.join(md) + '\n')
print('\n'.join(md))

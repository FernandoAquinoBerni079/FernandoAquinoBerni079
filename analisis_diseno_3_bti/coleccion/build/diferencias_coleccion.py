# -*- coding: utf-8 -*-
"""Lista cerrada de las diferencias autorizadas entre los documentos anuales y los documentos aprobados de los lotes
(portada, índice, apertura de unidad, paginación, remisiones y referencias editoriales). La equivalencia
(build/equivalencia.py) admite solo estas: cualquier otra diferencia de texto, formato de párrafo, tabla, ancho de
columna o figura es un fallo. DIFERENCIAS.md se genera desde esta lista y desde las apariciones que encontró la
equivalencia."""
import piezas_coleccion as PC

# (id, documento, categoría, qué cambia, dónde, cómo lo controla la equivalencia)
DIFERENCIAS = [
    ('D-01', 'Los tres', 'Portada', 'Una sola portada por documento, con la versión de la colección y su estado, en lugar de '
     'las portadas de los lotes.', 'Primera página', 'Las portadas de los lotes no se comparan.'),
    ('D-02', 'Los tres', 'Índice', 'Un índice general con las páginas del documento anual, en lugar de los índices de cada '
     'lote (la guía y el cuaderno de los lotes no tenían índice). El índice sigue el orden real de los títulos: en el del '
     'lote 1, la sección 3.3 figuraba bajo el Encuentro 6, aunque en el texto está en el Encuentro 5. En el cuaderno, los '
     'títulos de unidad agrupan las prácticas y llevan la página de su primera práctica.', 'Después de la portada',
     'Los índices no se comparan; el control de impresión comprueba cada entrada en su página y el orden creciente.'),
    ('D-03', 'Los tres', 'Paginación', 'Paginación continua; las tablas que empiezan en hoja nueva para no perder filas se '
     'recalculan sobre el documento anual; el encadenado de tablas largas de los lotes 3 a 6 se aplica también a las '
     'Unidades I y II.', 'Todo el documento', 'Solo cambian saltos de página y «conservar con el siguiente»: el texto, '
     'los estilos y los anchos de las tablas se comparan igual.'),
    ('D-04', 'Libro', 'Apertura de unidad', 'Las seis aperturas de unidad, cada una de su lote, en un solo libro.',
     'Antes del primer capítulo de cada unidad', 'Se comparan con la de su lote; solo admiten R-05.'),
] + [('D-%02d' % (5 + i), 'Libro', 'Referencia editorial' if r[0] != 'R-01' else 'Remisión (alcance)',
      '%s: «%s» → «%s» (%d %s).' % (r[0], r[2], r[3], r[4], 'aparición' if r[4] == 1 else 'apariciones'), r[1], r[5])
     for i, r in enumerate(PC.REEMPLAZOS[:7])] + [
    ('D-12', 'Guía', 'Referencia editorial', 'Parte general nueva: organización, versión de cada parte, dónde está cada '
     'instrumento, seguridad del código recibido, datos reservados y pendientes.', 'Después del índice',
     'Texto nuevo de coleccion/build/guia_general.py; no se compara con ningún lote.'),
    ('D-13', 'Guía', 'Referencia editorial', 'El título «Guía docente — Lote N» de cada guía pasa a ser el título de su parte '
     '(«Parte N — …»), en hoja nueva.', 'Primer título de cada parte', 'Se admite solo ese título.'),
    ('D-14', 'Guía', 'Referencia editorial', 'Nota de integración de la Parte V: preparación del Encuentro 30 y conjunto '
     'reservado (observaciones de la auditoría del lote 5, previstas en la estrategia de cierre).', 'Después del título de '
     'la Parte V', 'Se admite solo esa caja.'),
    ('D-15', 'Guía', 'Referencia editorial', 'Nota de integración de la Parte VI: las pruebas de código recibido requieren '
     'una máquina virtual o un equipo aislado, y la lista cerrada no vuelve confiable el código.', 'Después del título de '
     'la Parte VI', 'Se admite solo esa caja.'),
    ('D-16', 'Guía', 'Remisión', 'La página del diagnóstico de entrada en el libro («libro, pág. N») es la del libro anual.',
     'Parte I, sección 1', 'Se admite solo el número.'),
    ('D-17', 'Cuaderno', 'Referencia editorial', 'Las Prácticas 1 a 3, que estaban solo en el libro del lote 1, se agregan '
     'al cuaderno con la misma función de práctica de los lotes 2 a 6; el estado de la portada resume lo que decían las '
     'portadas de los cuadernos de los lotes.', 'Prácticas 1 a 3 y portada', 'Cada práctica se compara con la del libro '
     'anual y con la versión aprobada de su lote.'),
]
# v0.2 · cierre editorial: correcciones autorizadas C-01 a C-04 (los identificadores anteriores no cambian)
DIFERENCIAS += [('D-%02d' % (18 + i), 'Libro', 'Corrección editorial autorizada (%s)' % ('C-01' if r[0] == 'R-08' else 'C-02'),
                 '%s: «%s» → «%s» (%d aparición).' % (r[0], r[2], r[3], r[4]), r[1], r[5])
                for i, r in enumerate(PC.REEMPLAZOS[7:])]
DIFERENCIAS += [
    ('D-21', 'Libro y guía', 'Corrección editorial autorizada (C-04)', 'La celda «Archivo» de las fichas de los bloques de '
     'código del lote 4 se escribe desde la carpeta de la colección, como en los lotes 5 y 6: «referencia_docente/…» → '
     '«lote_4/proyecto/referencia_docente/…» y «base_estudiante/…» → «lote_4/proyecto/base_estudiante/…» (%d fichas del '
     'libro y %d de la guía).' % (PC.FICHAS_ESPERADAS['libro'], PC.FICHAS_ESPERADAS['guia']),
     'Fichas de los Códigos 10.1 a 13.2 y de las Referencias R-1 a R-3', 'El armado comprueba que cada ruta nueva exista y '
     'sea el mismo archivo real que la anterior. No cambian el código, las pruebas, las instrucciones de ejecución ni las '
     'rutas del texto: solo esa celda.'),
    ('D-22', 'Guía', 'Corrección editorial autorizada (C-03)', 'Parte general, sección 1: aclara que el año tiene 36 '
     'encuentros ordinarios y una adaptación alternativa a 28, con una tabla que reúne los encuentros de cada parte en las '
     'dos secuencias y la página de su tabla de calendario.', 'Parte general', 'Texto nuevo de guia_general.py; las '
     'secciones «Calendario con menos encuentros» de las partes no cambian (la equivalencia las compara) y la coherencia '
     'comprueba que los números de la tabla coincidan con lo que dice cada parte.'),
]
IDS = [d[0] for d in DIFERENCIAS]
assert len(IDS) == len(set(IDS))

"""Encuentro 9 — Evaluación de la Unidad 2 (asociación curricular: H2).

Devolución con claves en los primeros 20 minutos del encuentro 10 (Plan 10,
Bloque II), cuando todas las pruebas están entregadas.
"""

TITULO = 'Evaluación de la Unidad 2 — La prehistoria americana'
CLAVE = 'EVALUACIÓN DE LA UNIDAD 2'
PUNTAJE = 22

TOMO = [
    ('banda', 'EVALUACIÓN DE LA UNIDAD 2', 'La prehistoria americana: poblamiento y civilizaciones'),
    ('datos',),
    ('p', f'Tiempo: 70 minutos. Puntaje total: {PUNTAJE} puntos. Todo lo que necesitás está en esta prueba, incluido el mapa de la Parte C.'),
    ('consigna', 'Parte A — Marcá la opción correcta (1 punto cada una).'),
    ('item', '1. Según lo que se sabe hoy, los antepasados de los pueblos originarios de América llegaron…'),
    ('opc', ['desde Australia, por la Antártida', 'desde el nordeste de Asia', 'desde Europa, por el océano Atlántico',
             'desde África, navegando por el océano']),
    ('item', '2. Beringia quedó al descubierto porque…'),
    ('opc', ['durante la glaciación bajó el nivel del mar', 'se formó una cadena de volcanes', 'se secaron los grandes ríos',
             'se levantó el fondo del océano Atlántico']),
    ('item', '3. La teoría oceánica de Paul Rivet proponía…'),
    ('opc', ['que la humanidad se originó en América', 'un único origen asiático por Bering',
             'llegadas desde Asia y también desde Melanesia y Polinesia', 'una llegada desde Australia por la Antártida']),
    ('item', '4. Los mayas del período clásico…'),
    ('opc', ['formaron un imperio con capital en Tenochtitlan', 'vivían en ciudades-estado y tenían escritura propia',
             'habitaban las montañas de los Andes', 'construyeron el camino del Qhapaq Ñan']),
    ('item', '5. El ayllu era…'),
    ('opc', ['un templo en la cima de una pirámide maya', 'el título del gobernante mexica', 'el calendario de los incas',
             'una comunidad de familias emparentadas en los Andes']),
    ('item', '6. Tenochtitlan fue conquistada por los españoles y sus aliados indígenas en…'),
    ('opc', ['1325', '1438', '1521', '1533']),
    ('consigna', 'Parte B — Verdadero o falso. Justificá las falsas (1 punto cada una: si es verdadera, 1 punto por marcarla bien; '
                 'si es falsa, 0,5 por marcarla y 0,5 por la justificación).'),
    ('item', '7. (....) Hoy se acepta que la cultura Clovis fue la primera de América.'),
    ('item', '8. (....) Las chinampas eran canteros construidos con barro y plantas en lagos poco profundos.'),
    ('item', '9. (....) El imperio inca y el período clásico maya existieron al mismo tiempo.'),
    ('item', '10. (....) Los incas registraban datos con cuerdas anudadas llamadas quipus.'),
    ('consigna', 'Parte C — Mapa (3 puntos: 1 por fila; 0,5 por el nombre de la ciudad y 0,5 por la civilización).'),
    ('fig', 'eval_u2_mapa.png', 'Mapa para la Parte C. Elaboración propia con datos de Natural Earth (dominio público); mapa aproximado.', 10.0),
    ('item', '11. Escribí el nombre de las ciudades 1, 2 y 3 del mapa y la civilización a la que pertenecía cada una.'),
    ('cuadro', ['N.º', 'Ciudad', 'Civilización'], ['1', '2', '3'], [1.2, 4.4, 4.4], 1.0),
    ('consigna', 'Parte D — Comparación (4 puntos: 1 por cada casilla correcta).'),
    ('item', '12. Completá el cuadro.'),
    ('cuadro', ['Criterio', 'Mayas', 'Incas'], ['Forma de gobierno', 'Un aporte cultural'], [2.6, 3.7, 3.7]),
    ('consigna', 'Parte E — Desarrollo (5 puntos).'),
    ('item', '13. Explicá cómo se pobló América según lo que se sabe hoy. Escribí entre 6 y 8 líneas. Se tendrá en cuenta '
             '(1 punto cada uno): el origen en el nordeste de Asia, el paso por Beringia durante la glaciación, una prueba '
             'arqueológica con su fecha aproximada, una diferencia con alguna teoría clásica y un texto ordenado.', 8),
    ('h3', 'Al terminar la prueba: autoevaluación de la unidad'),
    ('p', 'Completala cuando termines la prueba, antes de entregarla. No lleva nota: sirve para saber qué repasar.'),
    ('tabla', ['Puedo…', 'Sí', 'Con ayuda', 'Todavía no'], [['Explicar cómo se pobló América con pruebas actuales.', '', '', ''], ['Comparar las teorías clásicas con lo que se sabe hoy.', '', '', ''], ['Ubicar en el mapa y en el tiempo a mayas, mexicas e incas.', '', '', ''], ['Comparar la organización y los aportes de dos civilizaciones.', '', '', '']], [5.5, 1.5, 1.5, 1.5]),
    ('p', 'La parte de la prueba que me resultó más difícil fue… y la voy a repasar así:'),
    ('renglones', 4)
]

PLAN = {
    'material': 'Tomo: Evaluación de la Unidad 2 (fotocopiada o en el cuadernillo; ya incluye el mapa de la Parte C)',
    'tema': 'Evaluación de las Clases 4 y 5 y de la Continuación B.',
    'indicadores': ['Explica el poblamiento de América con pruebas actuales y lo compara con las teorías clásicas.',
                    'Ubica en el mapa ciudades de mayas, mexicas e incas.',
                    'Compara la organización y los aportes de dos civilizaciones.',
                    'Ubica en el tiempo las civilizaciones sin confundir sus épocas.'],
    'proposito': 'Comprobar los logros de la Unidad 2 en condiciones iguales para todos y preparar la devolución del encuentro 10.',
    'funciones': {
        'Material que recibe cada estudiante': 'La prueba del tomo, que ya incluye el mapa. No se usa ninguna otra ficha.',
        'Criterios de puntaje': f'Figuran en cada parte de la prueba: A 6, B 4, C 3, D 4 y E 5 (total {PUNTAJE}).',
        'Devolución': 'Con claves y criterios, en los primeros 20 minutos del encuentro 10, cuando todas las pruebas están entregadas.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Explica la estructura (Partes A a E), el puntaje de cada parte y el tiempo. Lee en voz alta los criterios de la Parte E.',
             'Leen toda la prueba y preguntan dudas de consigna.', '—'),
        ]),
        ('Desarrollo', [
            ('10–80', 'Supervisa la resolución individual; solo aclara consignas.', 'Resuelven las Partes A a E.', 'Prueba.'),
            ('80–95', 'Tiempo adicional supervisado para quienes lo necesitan (hasta 15 minutos). Los demás completan la autoevaluación, entregan y pasan a la lectura sin claves.',
             'Quienes tienen tiempo adicional siguen la prueba; el resto lee en silencio la clase siguiente.', 'Entrega de todas las pruebas.'),
        ]),
        ('Cierre', [
            ('95–120', 'Con todas las pruebas entregadas, propone una actividad sin claves: lectura de anticipación de la Clase 6 y comentario oral sobre qué parte resultó más difícil, sin hablar de respuestas. No se corrige ni se comentan respuestas.',
             'Leen y comentan.', 'Comentario oral (no lleva nota).'),
        ]),
    ],
    'diversidad': [
        'Tiempo adicional de hasta 15 minutos (80 a 95), supervisado y sin corrección simultánea: nadie recibe respuestas antes de que terminen todos.',
        'Si un estudiante necesita más de 15 minutos adicionales, completa la prueba antes del encuentro 10 en un horario de apoyo acordado con la dirección, bajo supervisión y con la prueba custodiada por el docente. La devolución con claves se hace recién cuando esa prueba está entregada.',
        'Lectura en voz alta de las consignas para quien lo necesite, sin explicar contenidos.',
    ],
    'evaluacion': {
        'tipo': 'Sumativa de unidad; devolución formativa en el encuentro 10.',
        'procedimientos': 'Prueba escrita; lectura de mapa; cuadro comparativo; respuesta desarrollada.',
        'instrumentos': 'Prueba de la Unidad 2 del tomo; claves, criterios y matriz ítem-capacidad-puntaje del solucionario.',
        'criterios': [f'Total: {PUNTAJE} puntos (A 6; B 4; C 3; D 4; E 5). La calificación se obtiene con la escala de la institución.',
                      'La Parte E se corrige con los cinco criterios impresos en la consigna.'],
    },
    'precisiones': [
        'La prueba evalúa la capacidad H2 (Clases 4 y 5 y Continuación B).',
        'Primeros 20 minutos del encuentro 10: devolución con claves y criterios; el Plan 10 reserva ese tiempo.',
    ],
    'tarea': 'Observar el mapa de los viajes de la Clase 6 (sin actividades).',
}

SOL = {
    'puntaje': PUNTAJE,
    'bloques': [
        ('Parte A — 1 punto cada una', [
            ('1', 'b) desde el nordeste de Asia', ''),
            ('2', 'a) durante la glaciación bajó el nivel del mar', ''),
            ('3', 'c) llegadas desde Asia y también desde Melanesia y Polinesia', ''),
            ('4', 'b) vivían en ciudades-estado y tenían escritura propia', ''),
            ('5', 'd) una comunidad de familias emparentadas en los Andes', ''),
            ('6', 'c) 1521', ''),
        ]),
        ('Parte B — 1 punto cada una', [
            ('7', 'Falso: se acepta que hubo pobladores anteriores, como los de Monte Verde (unos 14.500 años).',
             'Criterio anunciado en la Parte B: si es verdadera, 1 punto por marcarla bien; si es falsa, 0,5 por marcarla y 0,5 por la justificación.'),
            ('8', 'Verdadero.', ''),
            ('9', 'Falso: el clásico maya terminó hacia el 900 y el imperio inca comenzó hacia 1438.', ''),
            ('10', 'Verdadero.', ''),
        ]),
        ('Parte C — 3 puntos', [
            ('11', '1: Tenochtitlan, mexicas (aztecas). 2: Tikal, mayas. 3: Cuzco, incas.',
             'Criterio anunciado en la Parte C: 1 por fila; 0,5 por el nombre de la ciudad y 0,5 por la civilización. Ver la clave gráfica.'),
        ]),
        ('Parte D — 4 puntos', [
            ('12', 'Gobierno: mayas, ciudades-estado independientes con reyes sagrados; incas, un imperio con un solo soberano, el Sapa Inca. '
                   'Aporte: mayas, escritura, el cero o el calendario; incas, caminos, terrazas de cultivo o quipus.',
             'Criterio anunciado en la Parte D: 1 por cada casilla correcta. Se aceptan otros aportes estudiados.'),
        ]),
        ('Parte E — 5 puntos', [
            ('13', 'Ejemplo: «Los primeros americanos vinieron del nordeste de Asia. Durante la última glaciación el mar bajó y '
                   'apareció Beringia, una franja de tierra entre Siberia y Alaska, por donde pasaron. Después avanzaron hacia el sur: '
                   'en Monte Verde, en Chile, hay un campamento de unos 14.500 años. Esto muestra que Ameghino se equivocaba al pensar '
                   'que la humanidad se originó en América.»',
             'Criterio anunciado en la consigna (1 punto cada uno): el origen en el nordeste de Asia, el paso por Beringia durante la '
             'glaciación, una prueba arqueológica con su fecha aproximada, una diferencia con alguna teoría clásica y un texto ordenado.'),
        ]),
    ],
    'mapas': [('eval_u2_mapa_clave.png', 10.0, 'Clave gráfica de la Parte C: 1 Tenochtitlan (mexicas), 2 Tikal (mayas), 3 Cuzco '
               '(incas). Las áreas pintadas son aproximadas y no se exigen en la prueba.')],
    'matriz': [
        ('1 a 3', 'H2', 'Antigüedad y teorías acerca del origen del hombre americano.', 3),
        ('4 a 6', 'H2', 'Organización y cronología de mayas, mexicas e incas.', 3),
        ('7 a 10', 'H2', 'Poblamiento, chinampas, cronología y quipus.', 4),
        ('11', 'H2', 'Espacios territoriales ocupados por aztecas, mayas e incas.', 3),
        ('12', 'H2', 'Aportes culturales y organización de mayas e incas.', 4),
        ('13', 'H2', 'Poblamiento de América con pruebas actuales y teorías clásicas.', 5),
    ],
}

VERIFICACION = []

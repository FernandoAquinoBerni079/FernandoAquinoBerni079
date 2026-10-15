"""Encuentro 36 — Evaluación Integradora de la 2.ª etapa (asociación curricular: H5, H6, G1, G2, G3 y G4).

Cubre contenidos efectivamente enseñados en las Unidades 4, 5 y 6. No evalúa
la Guerra Guaranítica (ampliación optativa de la Continuación E, condición
A05). Los primeros 20 minutos son la devolución de la Evaluación de la Unidad
6; la integradora no repite ítems de la U6, cuyas claves se acaban de
comentar.
"""

TITULO = 'Evaluación Integradora de la 2.ª etapa — Unidades 4 a 6'
CLAVE = 'EVALUACIÓN INTEGRADORA DE LA 2.ª ETAPA'
PUNTAJE = 28

TOMO = [
    ('banda', 'EVALUACIÓN INTEGRADORA DE LA 2.ª ETAPA', 'Unidades 4, 5 y 6: el siglo XVII y el espacio geográfico'),
    ('datos',),
    ('p', f'Tiempo: 70 minutos. Puntaje total: {PUNTAJE} puntos. La prueba recorre las tres unidades de la etapa.'),
    ('consigna', 'Parte A — Marcá la opción correcta (1 punto cada una).'),
    ('item', '1. La batalla de Mbororé (1641)…'),
    ('opc', ['enfrentó a guaraníes de las reducciones con bandeirantes paulistas', 'fue un levantamiento de los encomenderos de Asunción',
             'dio origen a la ciudad de Asunción', 'dividió la provincia en dos gobernaciones']),
    ('item', '2. Los habitantes de las reducciones jesuíticas…'),
    ('opc', ['estaban encomendados a vecinos de Asunción', 'trabajaban por turnos en las minas de Potosí',
             'pagaban un tributo directamente a la Corona', 'no hablaban guaraní']),
    ('item', '3. Jamestown, fundada en 1607, fue una colonia de…'),
    ('opc', ['Francia', 'Inglaterra', 'Holanda', 'Portugal']),
    ('item', '4. La posición relativa del Paraguay se describe diciendo que…'),
    ('opc', ['está entre los 19° 18\' y los 27° 36\' de latitud sur', 'tiene costas sobre el océano Atlántico',
             'está en el hemisferio norte', 'está en el centro de América del Sur, sin litoral marítimo']),
    ('item', '5. El cerro Tres Kandú…'),
    ('opc', ['es el punto más alto del Paraguay', 'está en el Chaco Seco', 'es un volcán activo', 'es el punto más alto de América']),
    ('item', '6. La Hidrovía Paraguay-Paraná va desde…'),
    ('opc', ['Asunción hasta Buenos Aires', 'Encarnación hasta Posadas', 'Cáceres (Brasil) hasta Nueva Palmira (Uruguay)',
             'Bahía Negra hasta Pilar']),
    ('item', '7. La altitud influye en el clima porque…'),
    ('opc', ['cerca del mar llueve más', 'cerca del Ecuador hace más calor', 'las corrientes marinas son frías',
             'cuanto más alto, más baja la temperatura']),
    ('item', '8. El Ministerio del Ambiente y Desarrollo Sostenible (MADES)…'),
    ('opc', ['controla la navegación de las barcazas', 'es la autoridad ambiental nacional', 'cobra los impuestos de los puertos',
             'fija el precio de la yerba']),
    ('consigna', 'Parte B — Verdadero o falso. Justificá las falsas (1 punto cada una: si es verdadera, 1 punto por marcarla bien; '
                 'si es falsa, 0,5 por marcarla y 0,5 por la justificación).'),
    ('item', '9. (....) Las Ordenanzas de Alfaro (1611) se cumplieron plenamente en la provincia.'),
    ('item', '10. (....) En las plantaciones de azúcar del Brasil trabajaban sobre todo africanos esclavizados.'),
    ('item', '11. (....) Todo el territorio paraguayo pertenece a la Cuenca del Plata.'),
    ('item', '12. (....) El Chaco recibe más lluvias que la Región Oriental.'),
    ('consigna', 'Parte C — Línea de tiempo (3 puntos: 0,5 por cada hecho bien ubicado).'),
    ('item', '13. Ordená del 1 al 6, del más antiguo al más reciente, escribiendo el número en el paréntesis:'),
    ('lista_orden', ['División de la provincia en dos gobernaciones', 'Éxodo de las reducciones del Guairá', 'Batalla de Mbororé',
                     'Ordenanzas de Alfaro', 'Fundación de Quebec', 'Descubrimiento de la plata de Potosí']),
    ('consigna', 'Parte D — Cuadro (4 puntos: 1 por cada casilla correcta).'),
    ('item', '14. Completá el cuadro con una característica y una actividad humana relacionada.'),
    ('cuadro', ['Elemento del espacio paraguayo', 'Una característica', 'Una actividad relacionada'],
     ['Río Paraná', 'Clima del Chaco'], [3.0, 3.5, 3.5], 1.4),
    ('consigna', 'Parte E — Desarrollo (6 puntos).'),
    ('item', '15. Explicá cómo influye la condición mediterránea del Paraguay en su historia y en su economía, desde la división de 1617 '
             'hasta la Hidrovía actual. Escribí entre 8 y 10 líneas. Se tendrá en cuenta (1 punto cada uno): qué es la '
             'mediterraneidad, la división de 1617 y la dependencia de Buenos Aires, una consecuencia en el siglo XVII, la importancia '
             'actual de los ríos o de la Hidrovía, un costo o cuidado ambiental de los ríos y un texto ordenado.', 10),
    ('consigna', 'Parte F — Respuesta breve (3 puntos: 1 por cada elemento).'),
    ('item', '16. Nombrá una región natural del Paraguay, una característica de su clima y una medida de gestión ambiental para cuidarla.', 4),
    ('h3', 'Al terminar la prueba: autoevaluación de la etapa'),
    ('p', 'Completala cuando termines la prueba, antes de entregarla. No lleva nota: sirve para saber qué repasar.'),
    ('tabla', ['Puedo…', 'Sí', 'Con ayuda', 'Todavía no'],
     [['Explicar los hechos principales del siglo XVII paraguayo.', '', '', ''],
      ['Explicar la economía y las colonizaciones de la América colonial.', '', '', ''],
      ['Describir la posición, el relieve y los ríos del Paraguay.', '', '', ''],
      ['Describir el clima y las regiones naturales del Paraguay.', '', '', ''],
      ['Proponer medidas de cuidado del ambiente con normas e instituciones.', '', '', '']],
     [5.5, 1.5, 1.5, 1.5]),
    ('p', 'La unidad que más necesito repasar es… porque…'),
    ('renglones', 3),
]

PLAN = {
    'material': 'La Evaluación de la Unidad 6 corregida (para la devolución); tomo: Evaluación Integradora de la 2.ª etapa (fotocopiada o en el cuadernillo)',
    'tema': 'Devolución de la Evaluación de la Unidad 6 y Evaluación Integradora de las Unidades 4 a 6.',
    'indicadores': ['Explica hechos del siglo XVII paraguayo: división de 1617, reducciones, malocas y Mbororé.',
                    'Reconoce rasgos de la América colonial del siglo XVII: economía y otras colonizaciones.',
                    'Describe la posición, el relieve y la hidrografía del Paraguay y su influencia en las actividades.',
                    'Describe el clima y las regiones naturales del Paraguay y propone medidas de gestión ambiental.'],
    'proposito': 'Devolver la Evaluación de la Unidad 6 y comprobar los logros de la segunda etapa en condiciones iguales para todos.',
    'funciones': {
        'Material que recibe cada estudiante': 'Su Evaluación de la Unidad 6 corregida (devolución) y la prueba integradora del tomo.',
        'Criterios de puntaje': f'Figuran en cada parte de la prueba: A 8, B 4, C 3, D 4, E 6 y F 3 (total {PUNTAJE}).',
        'Devolución': 'De la integradora: con claves y criterios, en el encuentro de cierre o en la entrega de resultados que fije la institución, cuando todas las pruebas, incluidas las de apoyo excepcional, están entregadas.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–20', 'Devolución de la Evaluación de la Unidad 6: entrega las pruebas corregidas, explica las claves y los criterios de la Parte E y comenta los errores más frecuentes. Al terminar, guarda las pruebas corregidas.',
             'Revisan su prueba y anotan en qué deben mejorar.', 'Devolución de la evaluación.'),
            ('20–30', 'Encuadre de la integradora: explica la estructura (Partes A a F), el puntaje y el tiempo. Lee los criterios de la Parte E.',
             'Leen toda la prueba y preguntan dudas de consigna.', '—'),
        ]),
        ('Desarrollo', [
            ('30–100', 'Supervisa la resolución individual; solo aclara consignas.', 'Resuelven las Partes A a F.', 'Prueba.'),
            ('100–115', 'Tiempo adicional supervisado para quienes lo necesitan (hasta 15 minutos). Los demás completan la autoevaluación de la etapa y entregan.',
             'Quienes tienen tiempo adicional siguen la prueba; el resto lee en silencio.', 'Entrega de todas las pruebas.'),
        ]),
        ('Cierre', [
            ('115–120', 'Con todas las pruebas entregadas, cierre sin claves: comentario oral sobre qué unidad resultó más difícil, sin hablar de respuestas.',
             'Comentan.', 'Comentario oral (no lleva nota).'),
        ]),
    ],
    'diversidad': [
        'Tiempo adicional de hasta 15 minutos (100 a 115), supervisado y sin corrección simultánea: nadie recibe respuestas antes de que terminen todos.',
        'Si un estudiante necesita más de 15 minutos adicionales, completa la prueba en un horario de apoyo acordado con la dirección, bajo supervisión y con la prueba custodiada por el docente. La devolución con claves se hace recién cuando esa prueba está entregada.',
        'Si un estudiante no participó de la devolución de la U6 por estar rindiéndola en apoyo, la integradora se le administra después, también sin claves a la vista.',
        'Lectura en voz alta de las consignas para quien lo necesite, sin explicar contenidos.',
    ],
    'evaluacion': {
        'tipo': 'Sumativa de etapa; devolución formativa en el encuentro de cierre.',
        'procedimientos': 'Prueba escrita integradora; ordenamiento cronológico; cuadro; respuesta desarrollada y respuesta breve.',
        'instrumentos': 'Prueba integradora del tomo; claves, criterios y matriz ítem-capacidad-puntaje del solucionario.',
        'criterios': [f'Total: {PUNTAJE} puntos (A 8; B 4; C 3; D 4; E 6; F 3). La calificación se obtiene con la escala de la institución.',
                      'La Parte E se corrige con los seis criterios impresos en la consigna.'],
    },
    'precisiones': [
        'La integradora evalúa las capacidades H5, H6, G1, G2, G3 y G4 con contenidos enseñados en las Unidades 4 a 6; la matriz del solucionario muestra el peso de cada una.',
        'No se evalúa la Guerra Guaranítica: el recuadro de la Continuación E es ampliación optativa (A05).',
        'Ningún ítem repite los de la Evaluación de la Unidad 6, cuyas claves se comentan en los primeros 20 minutos.',
    ],
    'tarea': 'Sin tarea: cierre del año.',
}

SOL = {
    'puntaje': PUNTAJE,
    'bloques': [
        ('Parte A — 1 punto cada una', [
            ('1', 'a) enfrentó a guaraníes de las reducciones con bandeirantes paulistas', ''),
            ('2', 'c) pagaban un tributo directamente a la Corona', ''),
            ('3', 'b) Inglaterra', ''),
            ('4', 'd) está en el centro de América del Sur, sin litoral marítimo', ''),
            ('5', 'a) es el punto más alto del Paraguay', ''),
            ('6', 'c) Cáceres (Brasil) hasta Nueva Palmira (Uruguay)', ''),
            ('7', 'd) cuanto más alto, más baja la temperatura', ''),
            ('8', 'b) es la autoridad ambiental nacional', ''),
        ]),
        ('Parte B — 1 punto cada una', [
            ('9', 'Falso: se cumplieron poco por la resistencia de los encomenderos y la lejanía de las autoridades.',
             'Criterio anunciado en la Parte B: si es verdadera, 1 punto por marcarla bien; si es falsa, 0,5 por marcarla y 0,5 por la justificación.'),
            ('10', 'Verdadero.', ''),
            ('11', 'Verdadero.', ''),
            ('12', 'Falso: llueve más en la Región Oriental (unos 1.800 mm al año en el este) que en el Chaco (unos 400 mm en el noroeste).', ''),
        ]),
        ('Parte C — 3 puntos', [
            ('13', 'Orden: 1 Descubrimiento de la plata de Potosí (1545); 2 Fundación de Quebec (1608); 3 Ordenanzas de Alfaro (1611); '
                   '4 División de la provincia (1617); 5 Éxodo del Guairá (1631); 6 Batalla de Mbororé (1641).',
             'Criterio anunciado en la Parte C: 0,5 por cada hecho bien ubicado. En el paréntesis de cada hecho: División 4; Éxodo 5; '
             'Mbororé 6; Alfaro 3; Quebec 2; Potosí 1.'),
        ]),
        ('Parte D — 4 puntos', [
            ('14', 'Río Paraná: límite con el Brasil y la Argentina, caudaloso; energía en Itaipú y Yacyretá, navegación. Clima del Chaco: '
                   'seco y muy caluroso; ganadería.', 'Criterio anunciado en la Parte D: 1 por cada casilla correcta. Se aceptan otras '
                   'características y actividades estudiadas.'),
        ]),
        ('Parte E — 6 puntos', [
            ('15', 'Ejemplo: «El Paraguay es mediterráneo: no tiene costa y su salida al mar es por los ríos Paraguay y Paraná. En 1617 '
                   'la provincia se dividió y el puerto de Buenos Aires quedó en otra gobernación, por eso el Paraguay pasó a depender '
                   'de Buenos Aires y Santa Fe para comerciar. En el siglo XVII su yerba llegaba cara a los mercados. Hoy la Hidrovía '
                   'Paraguay-Paraná es la vía de su comercio exterior. Pero los ríos deben cuidarse: el dragado o la contaminación '
                   'pueden dañar los humedales y la pesca.»',
             'Criterio anunciado en la consigna (1 punto cada uno): qué es la mediterraneidad, la división de 1617 y la dependencia de '
             'Buenos Aires, una consecuencia en el siglo XVII, la importancia actual de los ríos o de la Hidrovía, un costo o cuidado '
             'ambiental de los ríos y un texto ordenado.'),
        ]),
        ('Parte F — 3 puntos', [
            ('16', 'Por ejemplo: Chaco Seco; pocas lluvias y mucho calor; controlar el desmonte con planes del INFONA y evaluación de '
                   'impacto ambiental.', 'Criterio anunciado en la Parte F: 1 por cada elemento.'),
        ]),
    ],
    'matriz': [
        ('1, 2 y 9', 'H5', 'Mbororé, reducciones y Ordenanzas de Alfaro.', 3),
        ('3 y 10', 'H6', 'Otras colonizaciones y trabajo esclavizado en las plantaciones.', 2),
        ('4', 'G1', 'Posición relativa del Paraguay.', 1),
        ('5, 6 y 11', 'G2', 'Relieve, Hidrovía y Cuenca del Plata.', 3),
        ('7 y 12', 'G3', 'Factores del clima y lluvias en el Paraguay.', 2),
        ('8', 'G4', 'Instituciones ambientales.', 1),
        ('13', 'H5, H6', 'Cronología del siglo XVII paraguayo y americano.', 3),
        ('14', 'G2, G3', 'Río Paraná y clima del Chaco con sus actividades.', 4),
        ('15', 'H5, G1, G2', 'Mediterraneidad: de la división de 1617 a la Hidrovía.', 6),
        ('16', 'G3, G4', 'Región natural, clima y gestión ambiental.', 3),
    ],
}

VERIFICACION = []

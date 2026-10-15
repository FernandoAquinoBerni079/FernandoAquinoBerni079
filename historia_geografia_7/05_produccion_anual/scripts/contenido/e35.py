"""Encuentro 35 — Evaluación de la Unidad 6 (asociación curricular: G3 y G4).

Devolución con claves en los primeros 20 minutos del encuentro 36 (Plan 36),
cuando todas las pruebas están entregadas.
"""

TITULO = 'Evaluación de la Unidad 6 — Clima, regiones naturales y ambiente'
CLAVE = 'EVALUACIÓN DE LA UNIDAD 6'
PUNTAJE = 25

TOMO = [
    ('banda', 'EVALUACIÓN DE LA UNIDAD 6', 'Clima, regiones naturales y ambiente'),
    ('datos',),
    ('p', f'Tiempo: 70 minutos. Puntaje total: {PUNTAJE} puntos. Todo lo que necesitás está en esta prueba, incluido el mapa de la Parte C.'),
    ('consigna', 'Parte A — Marcá la opción correcta (1 punto cada una).'),
    ('item', '1. Un factor del clima es…'),
    ('opc', ['la temperatura', 'la humedad', 'las precipitaciones', 'la altitud']),
    ('item', '2. Cerca del Ecuador, en la Amazonía, predomina el clima…'),
    ('opc', ['ecuatorial', 'polar', 'desértico', 'templado frío']),
    ('item', '3. En el Paraguay, las lluvias son mayores en…'),
    ('opc', ['el noroeste del Chaco', 'el este de la Región Oriental', 'el Pantanal', 'el centro del Chaco']),
    ('item', '4. La sabana con árboles dispersos del Brasil central se llama…'),
    ('opc', ['pampa', 'taiga', 'Cerrado', 'tundra']),
    ('item', '5. La Ley 294/1993…'),
    ('opc', ['exige una evaluación de impacto ambiental antes de ciertas obras', 'crea el Ministerio del Ambiente',
             'prohíbe la ganadería en el Chaco', 'divide el país en ecorregiones']),
    ('item', '6. Un costo socioambiental del desmonte es…'),
    ('opc', ['el aumento de la biodiversidad', 'más agua en las nacientes', 'suelos más fértiles', 'la erosión de los suelos']),
    ('consigna', 'Parte B — Verdadero o falso. Justificá las falsas (1 punto cada una: si es verdadera, 1 punto por marcarla bien; '
                 'si es falsa, 0,5 por marcarla y 0,5 por la justificación).'),
    ('item', '7. (....) El viento sur trae aire cálido y húmedo al Paraguay.'),
    ('item', '8. (....) El clima se describe con datos de muchos años.'),
    ('item', '9. (....) El Pantanal es un gran humedal del norte del Chaco.'),
    ('item', '10. (....) La gestión ambiental es tarea exclusiva del Estado.'),
    ('consigna', 'Parte C — Mapa (3 puntos: 1 por fila; 0,5 por el ecosistema y 0,5 por una característica).'),
    ('fig', 'eval_u6_mapa.png', 'Mapa para la Parte C. Elaboración propia con datos de Natural Earth (dominio público); mapa aproximado.', 10.0),
    ('item', '11. Escribí qué ecosistema se encuentra en los lugares 1, 2 y 3 del mapa y una característica de cada uno.'),
    ('cuadro', ['N.º', 'Ecosistema', 'Una característica'], ['1', '2', '3'], [1.2, 3.8, 5.0], 1.2),
    ('consigna', 'Parte D — Cuadro (4 puntos: 1 por cada casilla correcta).'),
    ('item', '12. Completá el cuadro.'),
    ('cuadro', ['Criterio', 'Región Occidental (Chaco)', 'Región Oriental'], ['Clima', 'Un ecosistema'], [2.8, 3.6, 3.6], 1.2),
    ('consigna', 'Parte E — Desarrollo (5 puntos).'),
    ('item', '13. Elegí una región del Paraguay y explicá cómo se relacionan su clima, su ecosistema y el uso de la tierra. Escribí entre '
             '6 y 8 líneas. Se tendrá en cuenta (1 punto cada uno): una característica del clima, el ecosistema de la región, una '
             'actividad económica, un costo socioambiental y un texto ordenado.', 8),
    ('consigna', 'Parte F — Respuesta breve (3 puntos: 1 por cada elemento).'),
    ('item', '14. Nombrá una institución ambiental del Paraguay, una ley ambiental con lo que establece y una acción de la ciudadanía '
             'para cuidar el ambiente.', 4),
    ('h3', 'Al terminar la prueba: autoevaluación de la unidad'),
    ('p', 'Completala cuando termines la prueba, antes de entregarla. No lleva nota: sirve para saber qué repasar.'),
    ('tabla', ['Puedo…', 'Sí', 'Con ayuda', 'Todavía no'],
     [['Distinguir elementos y factores del clima.', '', '', ''],
      ['Describir el clima del Paraguay y los climas de América.', '', '', ''],
      ['Diferenciar las regiones naturales del Paraguay y de América.', '', '', ''],
      ['Explicar costos del uso de la tierra y normas para el ambiente.', '', '', '']],
     [5.5, 1.5, 1.5, 1.5]),
    ('p', 'La parte de la prueba que me resultó más difícil fue… y la voy a repasar así:'),
    ('renglones', 3),
]

PLAN = {
    'material': 'Tomo: Evaluación de la Unidad 6 (fotocopiada o en el cuadernillo; ya incluye el mapa de la Parte C)',
    'tema': 'Evaluación de las Clases 19, 20 y 21 y de la Continuación G.',
    'indicadores': ['Distingue elementos y factores del clima y describe el clima del Paraguay.',
                    'Describe regiones naturales de América y ecosistemas del Paraguay.',
                    'Explica costos socioambientales del uso de la tierra.',
                    'Reconoce instituciones y normas ambientales del Paraguay.'],
    'proposito': 'Comprobar los logros de la Unidad 6 en condiciones iguales para todos y preparar la devolución del encuentro 36.',
    'funciones': {
        'Material que recibe cada estudiante': 'La prueba del tomo, que ya incluye el mapa. No se usa ninguna otra ficha.',
        'Criterios de puntaje': f'Figuran en cada parte de la prueba: A 6, B 4, C 3, D 4, E 5 y F 3 (total {PUNTAJE}).',
        'Devolución': 'Con claves y criterios, en los primeros 20 minutos del encuentro 36, cuando todas las pruebas están entregadas.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Explica la estructura (Partes A a F), el puntaje de cada parte y el tiempo. Lee en voz alta los criterios de la Parte E.',
             'Leen toda la prueba y preguntan dudas de consigna.', '—'),
        ]),
        ('Desarrollo', [
            ('10–80', 'Supervisa la resolución individual; solo aclara consignas.', 'Resuelven las Partes A a F.', 'Prueba.'),
            ('80–95', 'Tiempo adicional supervisado para quienes lo necesitan (hasta 15 minutos). Los demás completan la autoevaluación, entregan y pasan a la actividad sin claves.',
             'Quienes tienen tiempo adicional siguen la prueba; el resto lee en silencio.', 'Entrega de todas las pruebas.'),
        ]),
        ('Cierre', [
            ('95–120', 'Con todas las pruebas entregadas, propone una actividad sin claves: repaso de anticipación de las Unidades 4 y 5 para la Evaluación Integradora (los estudiantes releen sus autoevaluaciones) y comentario oral sobre qué parte resultó más difícil, sin hablar de respuestas. No se corrige ni se comentan respuestas.',
             'Releen y comentan.', 'Comentario oral (no lleva nota).'),
        ]),
    ],
    'diversidad': [
        'Tiempo adicional de hasta 15 minutos (80 a 95), supervisado y sin corrección simultánea: nadie recibe respuestas antes de que terminen todos.',
        'Si un estudiante necesita más de 15 minutos adicionales, completa la prueba antes del encuentro 36 en un horario de apoyo acordado con la dirección, bajo supervisión y con la prueba custodiada por el docente. La devolución con claves se hace recién cuando esa prueba está entregada.',
        'Lectura en voz alta de las consignas para quien lo necesite, sin explicar contenidos.',
    ],
    'evaluacion': {
        'tipo': 'Sumativa de unidad; devolución formativa en el encuentro 36.',
        'procedimientos': 'Prueba escrita; lectura de mapa; cuadro; respuesta desarrollada y respuesta breve.',
        'instrumentos': 'Prueba de la Unidad 6 del tomo; claves, criterios, clave gráfica y matriz ítem-capacidad-puntaje del solucionario.',
        'criterios': [f'Total: {PUNTAJE} puntos (A 6; B 4; C 3; D 4; E 5; F 3). La calificación se obtiene con la escala de la institución.',
                      'La Parte E se corrige con los cinco criterios impresos en la consigna.'],
    },
    'precisiones': [
        'La prueba evalúa las capacidades G3 y G4 (Clases 19 a 21 y Continuación G).',
        'Primeros 20 minutos del encuentro 36: devolución con claves y criterios; el Plan 36 reserva ese tiempo antes de la Evaluación Integradora.',
    ],
    'tarea': 'Repasar las Unidades 4, 5 y 6 (autoevaluaciones y actividades esenciales) para la Evaluación Integradora de la 2.ª etapa.',
}

SOL = {
    'puntaje': PUNTAJE,
    'bloques': [
        ('Parte A — 1 punto cada una', [
            ('1', 'd) la altitud', ''),
            ('2', 'a) ecuatorial', ''),
            ('3', 'b) el este de la Región Oriental', ''),
            ('4', 'c) Cerrado', ''),
            ('5', 'a) exige una evaluación de impacto ambiental antes de ciertas obras', ''),
            ('6', 'd) la erosión de los suelos', ''),
        ]),
        ('Parte B — 1 punto cada una', [
            ('7', 'Falso: el viento sur trae aire frío y seco; el norte, cálido y húmedo.',
             'Criterio anunciado en la Parte B: si es verdadera, 1 punto por marcarla bien; si es falsa, 0,5 por marcarla y 0,5 por la justificación.'),
            ('8', 'Verdadero.', ''),
            ('9', 'Verdadero.', ''),
            ('10', 'Falso: también participan las empresas, las organizaciones, las comunidades y cada persona.', ''),
        ]),
        ('Parte C — 3 puntos', [
            ('11', '1: Chaco Seco (bosques bajos y espinosos, pocas lluvias). 2: Bosque Atlántico del Alto Paraná (selva alta y muy '
                   'diversa, muy deforestada). 3: Humedales del Ñeembucú (esteros y terrenos bajos con agua).',
             'Criterio anunciado en la Parte C: 1 por fila; 0,5 por el ecosistema y 0,5 por una característica. Ver la clave gráfica.'),
        ]),
        ('Parte D — 4 puntos', [
            ('12', 'Clima: Chaco, más seco y caluroso; Región Oriental, más húmeda. Ecosistema: Chaco, Chaco Seco, Chaco Húmedo o '
                   'Pantanal; Región Oriental, Bosque Atlántico del Alto Paraná, Cerrado o humedales del Ñeembucú.',
             'Criterio anunciado en la Parte D: 1 por cada casilla correcta.'),
        ]),
        ('Parte E — 5 puntos', [
            ('13', 'Ejemplo: «En el este de la Región Oriental llueve mucho, unos 1.800 mm al año, y había una selva alta: el Bosque '
                   'Atlántico del Alto Paraná. Hoy esa zona se usa para la agricultura, sobre todo de soja. El desmonte hizo perder gran '
                   'parte del bosque y el hábitat de muchas especies, y los suelos se erosionan.»',
             'Criterio anunciado en la consigna (1 punto cada uno): una característica del clima, el ecosistema de la región, una '
             'actividad económica, un costo socioambiental y un texto ordenado.'),
        ]),
        ('Parte F — 3 puntos', [
            ('14', 'Por ejemplo: MADES; Ley 294/1993, que exige evaluación de impacto ambiental (o la Ley 2524/2004, que prohíbe '
                   'desmontar bosques en la Región Oriental); denunciar daños ambientales, no quemar basura, cuidar los arroyos.',
             'Criterio anunciado en la Parte F: 1 por cada elemento.'),
        ]),
    ],
    'mapas': [('eval_u6_mapa_clave.png', 12.0, 'Clave gráfica de la Parte C: 1 Chaco Seco, 2 Bosque Atlántico del Alto Paraná, 3 Humedales '
               'del Ñeembucú. Ubicación aproximada; se acepta el ecosistema si el número está dentro de su zona en la clave.')],
    'matriz': [
        ('1 a 3, 7 y 8', 'G3', 'Factores y tipos de clima; lluvias y vientos del Paraguay.', 5),
        ('4 a 6, 9 y 10', 'G4', 'Regiones naturales, normas, costos del uso de la tierra y gestión ambiental.', 5),
        ('11', 'G4', 'Ecosistemas del Paraguay en el mapa.', 3),
        ('12', 'G3, G4', 'Clima y ecosistemas de las dos regiones.', 4),
        ('13', 'G3, G4', 'Clima, ecosistema y uso de la tierra en una región.', 5),
        ('14', 'G4', 'Instituciones, normas y participación ciudadana.', 3),
    ],
}

VERIFICACION = []

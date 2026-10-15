"""Encuentro 24 — Clase 15: Otras colonizaciones; indígenas y africanos (H6; temas H6b y H6c).

Corrige el maestro: desarrolla la colonización portuguesa (capitanías,
azúcar, esclavitud, bandeirantes), inglesa, francesa y holandesa con datos;
da ejemplos concretos de lucha por la libertad (Palmares, Benkos Biohó,
Calchaquíes, Pueblo); corrige el origen de Kamba Kua (lanceros de Artigas,
1820) y agrega un ejemplo de la población afrodescendiente colonial del
Paraguay; la fuente lleva autor y fecha.
"""
import curriculo as C

TITULO = 'Clase 15 — Otras colonizaciones; indígenas y africanos en América'
CLAVE = 'Clase 15 —'
INDICADORES = [
    'Compara las colonizaciones portuguesa, inglesa, francesa y holandesa en América.',
    'Explica la trata de africanos esclavizados y el comercio triangular.',
    'Reconoce formas de lucha por la libertad de indígenas y africanos con ejemplos concretos.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H6'], C.TEMAS['H6b'] + ' ' + C.TEMAS['H6c'], INDICADORES),

    ('h2', 'Portugal en el Brasil'),
    ('p', 'Portugal ocupó la costa del Brasil, que le correspondía por el Tratado de Tordesillas. Desde 1534 la dividió en '
          'capitanías, grandes franjas de tierra entregadas a particulares, y en 1549 creó un gobierno general con sede en Salvador '
          'de Bahía. En el nordeste se desarrollaron enormes plantaciones de caña de azúcar trabajadas por africanos esclavizados: '
          'el Brasil fue el principal destino de la trata en toda América. Desde São Paulo, los bandeirantes avanzaron hacia el '
          'interior, como viste en la Continuación E.'),

    ('h2', 'Inglaterra, Francia y Holanda'),
    ('p', 'En el siglo XVII, otros reinos europeos fundaron colonias en las zonas que España no ocupaba:'),
    ('tabla', ['Potencia', 'Dónde y cuándo', 'Características'],
     [['Inglaterra', 'Jamestown (1607) y Plymouth (1620), en América del Norte; Barbados (1627) y Jamaica (1655), en el Caribe.',
       'Colonos que llegaban con sus familias a trabajar la tierra; algunos huían de persecuciones religiosas. En el Caribe, '
       'plantaciones de azúcar con esclavizados.'],
      ['Francia', 'Quebec (1608), en Nueva Francia (actual Canadá); Martinica y Guadalupe (1635), en el Caribe.',
       'Pocos colonos; comercio de pieles con los pueblos indígenas; misiones; plantaciones en las islas.'],
      ['Holanda', 'Nueva Ámsterdam (1625, hoy Nueva York); Curazao (1634); nordeste del Brasil (1630-1654).',
       'Compañías de comercio; puertos para el comercio, también el de esclavizados.']],
     [2.0, 4.0, 4.0]),
    ('fig', 'fig_15_1_colonias.png', 'Figura 15.1 — Colonias de Inglaterra, Francia, Holanda y Portugal en el siglo XVII (posiciones aproximadas).', 12.0),

    ('h2', 'La trata de africanos esclavizados'),
    ('p', 'Para trabajar en las plantaciones y las minas, los europeos trajeron por la fuerza a millones de africanos. Entre los '
          'siglos XVI y XIX fueron embarcadas en África más de doce millones de personas; muchas murieron durante la travesía del '
          'Atlántico, encerradas en las bodegas de los barcos. Funcionaba un comercio triangular: los barcos llevaban de Europa a '
          'África armas, telas y bebidas; de África a América, personas esclavizadas; y de América a Europa, azúcar, tabaco y otros '
          'productos.'),

    ('h2', 'Indígenas y africanos: la lucha por la libertad'),
    ('lista', ['Palmares, en el nordeste del Brasil: un quilombo (comunidad de africanos que habían huido) que resistió durante casi '
               'todo el siglo XVII; su último líder, Zumbi, murió en 1695.',
               'San Basilio de Palenque, en la actual Colombia: comunidad libre fundada por africanos que se rebelaron a comienzos del '
               'siglo XVII, guiados por Benkos Biohó.',
               'Los pueblos calchaquíes, en el noroeste de la actual Argentina, resistieron a los españoles en grandes levantamientos '
               'entre 1630 y 1665.',
               'La Rebelión de los Pueblo (1680), en el norte de Nueva España: los indígenas expulsaron a los españoles durante doce años.']),
    ('caja', 'paraguay', 'En Paraguay — ',
     'En el Paraguay colonial también hubo africanos y afrodescendientes esclavizados, por ejemplo en las estancias de las órdenes '
     'religiosas y en las casas de los vecinos de Asunción. La comunidad Kamba Kua, de Fernando de la Mora, tiene otro origen: '
     'desciende de los lanceros afrodescendientes que acompañaron a José Artigas cuando se asiló en el Paraguay en 1820.'),
    ('caja', 'concepto', 'Concepto clave — ',
     'Quilombo (Brasil) o palenque (América española): comunidad formada por africanos que huían de la esclavitud. Comercio '
     'triangular: circuito comercial entre Europa, África y América, en el que las personas esclavizadas eran tratadas como mercancía.'),

    ('fuente', 'Documento de época · Olaudah Equiano, Narración de la vida (Londres, 1789). Versión escolar resumida: no es cita textual.',
     ['Equiano, nacido en África y capturado cuando era niño, cuenta que fue llevado a un barco donde muchas personas estaban '
      'encadenadas y amontonadas bajo cubierta. El calor y el aire irrespirable hacían enfermar a muchos, y algunos preferían morir '
      'antes que seguir esa vida. Años después compró su libertad y luchó contra la trata.'],
     'Vocabulario: travesía, viaje por mar; trata, comercio de personas esclavizadas.',
     ['¿Quién escribió este relato y por qué su testimonio es valioso?',
      '¿Qué condiciones del viaje describe?',
      'Equiano escribió su libro cuando ya era libre y para convencer a los ingleses de abolir la trata. ¿Cómo influye eso en la '
      'lectura de la fuente?']),
    ('renglones', 6),
    ('ubicate', 'Ubicate  ·  Mapa (Figura 15.1)',
     'Ubicá una colonia de cada potencia. ¿Cuáles están en América del Norte y cuáles en el Caribe? ¿Dónde estaba Palmares?'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. Las capitanías del Brasil eran…'),
    ('opc', ['ciudades fundadas por holandeses', 'franjas de tierra entregadas por Portugal a particulares',
             'comunidades de africanos libres', 'puertos autorizados por España']),
    ('item', '2. Quebec, fundada en 1608, fue una colonia de…'),
    ('opc', ['Inglaterra', 'Holanda', 'Portugal', 'Francia']),
    ('item', '3. El comercio triangular unía…'),
    ('opc', ['Europa, África y América', 'el Paraguay, el Perú y Chile', 'Asia, Oceanía y América', 'España, Portugal y Francia']),
    ('item', '4. Palmares fue…'),
    ('opc', ['una plantación de azúcar holandesa', 'una ciudad inglesa del Caribe', 'un quilombo de africanos que resistió en el Brasil',
             'una reducción jesuítica']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. Los holandeses fundaron Nueva ________, que hoy es Nueva York.'),
    ('item', '6. El último líder de Palmares fue ________, que murió en 1695.'),
    ('item', '7. En 1549, Portugal creó un gobierno general para el Brasil con sede en Salvador de ________.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) El Brasil fue el principal destino de los africanos esclavizados en América.'),
    ('item', '9. (....) La comunidad Kamba Kua desciende de esclavizados llegados en el siglo XVI.'),
    ('item', '10. (....) Holanda ocupó parte del nordeste del Brasil entre 1630 y 1654.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. Elegí dos potencias y compará cómo colonizaron: dónde se instalaron y qué actividad principal desarrollaron.', 4),
    ('item', '12. Escribí un texto de 6 a 8 líneas sobre la lucha por la libertad de indígenas y africanos. Se tendrá en cuenta: un '
             'ejemplo de resistencia africana (1 punto), un ejemplo de resistencia indígena (1 punto), la explicación de qué '
             'buscaban (1 punto) y un texto ordenado (1 punto).', 8),
]

PLAN = {
    'material': 'Tomo: Clase 15 (Figura 15.1) y Figura E.1 de la Continuación E; planisferio',
    'tema': C.TEMAS['H6b'] + ' ' + C.TEMAS['H6c'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes comparen las colonizaciones europeas no españolas y expliquen la trata y la lucha por la '
                 'libertad de indígenas y africanos con ejemplos concretos.',
    'funciones': {
        'Esenciales': 'En clase: Ubicate; fuente (preguntas 1 a 3); actividades 1, 2, 3, 4 y 11.',
        'Consolidación': 'Actividades 5, 6, 8 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 25).',
        'Complementarias o domiciliarias': 'Actividades 7, 10 y 12.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 14. Pregunta: «¿Por qué en los Estados Unidos y en Canadá se habla inglés y francés?».',
             'Responden con lo que saben.', 'Ideas en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–30', 'Lectura de «Portugal en el Brasil» y del cuadro de Inglaterra, Francia y Holanda, con la Figura 15.1.',
             'Resuelven el «Ubicate» y las actividades 1 y 2.', 'Ubicate y actividades 1 y 2 (esenciales).'),
            ('30–45', 'Acompaña la comparación.', 'Resuelven la actividad 11 en parejas.', 'Actividad 11 (esencial).'),
            ('45–60', 'Lectura de «La trata de africanos esclavizados». Dibuja en el planisferio el comercio triangular.',
             'Resuelven la actividad 3.', 'Actividad 3 (esencial).'),
            ('60–80', 'Lectura de «La lucha por la libertad», de la caja «En Paraguay» y presentación del relato de Equiano (versión resumida).',
             'Resuelven la actividad 4 y las preguntas 1 a 3 de la fuente.', 'Actividad 4 y fuente (esenciales).'),
            ('80–100', 'Acompaña; quien termina antes sigue con la consolidación.', 'Resuelven las actividades 5, 6, 8 y 9.',
             'Actividades de consolidación.'),
        ]),
        ('Cierre', [
            ('100–120', 'Puesta en común de la pregunta 3 de la fuente. Recuerda que el próximo encuentro es la Evaluación de la Unidad 4. Lee los criterios de la actividad 12 y asigna la tarea.',
             'Comentan y corrigen.', 'Fuente revisada.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en la actividad 11: cuadro de dos columnas en la pizarra («dónde» / «actividad principal»).',
        'Apoyo en la lectura: el docente lee en voz alta la fuente y el glosario (trata, quilombo, palenque, capitanía).',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: averiguar qué es hoy la comunidad Kamba Kua y cómo conserva su herencia cultural.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Lectura de mapa; cuadro comparativo; análisis de fuente; respuesta breve.',
        'instrumentos': 'Lista de cotejo con los tres indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Compara dos colonizaciones con datos de lugar y actividad.',
                      'Explica la trata y el comercio triangular.',
                      'Da ejemplos concretos de resistencia indígena y africana.'],
    },
    'precisiones': [
        'Kamba Kua: su origen es la llegada de los lanceros de Artigas en 1820, no la esclavitud colonial. El tomo da otro ejemplo de esclavitud en el Paraguay colonial.',
        'Tratar la trata con respeto: las personas esclavizadas fueron víctimas, no mercancía; el término «esclavizado» subraya que la esclavitud fue impuesta.',
        'El relato de Equiano va en versión escolar resumida, no como cita textual.',
    ],
    'tarea': 'Actividades 7, 10 y 12 de la Clase 15. Repasar las Clases 11 a 15 y la Continuación E para la Evaluación de la Unidad 4.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente', [
            ('F1', 'Olaudah Equiano, un africano que fue esclavizado. Su testimonio es valioso porque cuenta en primera persona lo que vivió.', ''),
            ('F2', 'Personas encadenadas y amontonadas bajo cubierta, calor, aire irrespirable, enfermedades y desesperación.', ''),
            ('F3', 'Que quería mostrar la crueldad de la trata para lograr su abolición: es un testimonio verdadero pero escrito con '
                   'una intención; conviene compararlo con otras fuentes.', ''),
        ]),
        ('Ubicate (Figura 15.1)', [
            ('U', 'Por ejemplo: Inglaterra, Jamestown; Francia, Quebec; Holanda, Curazao; Portugal, Salvador de Bahía. En América del '
                  'Norte: Quebec, Plymouth, Jamestown y Nueva Ámsterdam; en el Caribe: Barbados, Martinica, Curazao y Jamaica. Palmares '
                  'estaba en el nordeste del Brasil.', ''),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'b) franjas de tierra entregadas por Portugal a particulares', ''),
            ('2', 'd) Francia', ''),
            ('3', 'a) Europa, África y América', ''),
            ('4', 'c) un quilombo de africanos que resistió en el Brasil', ''),
        ]),
        ('Completá los espacios', [
            ('5', 'Ámsterdam', ''),
            ('6', 'Zumbi', ''),
            ('7', 'Bahía', ''),
        ]),
        ('Verdadero o falso', [
            ('8', 'Verdadero.', ''),
            ('9', 'Falso: desciende de los lanceros de Artigas que llegaron al Paraguay en 1820.', 'Justificación obligatoria.'),
            ('10', 'Verdadero.', ''),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'Ejemplo: Inglaterra se instaló en la costa este de América del Norte, con colonos y familias que trabajaban la tierra; '
                   'Francia, en Quebec y el valle del San Lorenzo, con pocos colonos dedicados al comercio de pieles.',
             'Dos potencias, cada una con lugar y actividad.'),
            ('12', 'Ejemplo: «Los africanos esclavizados huían y formaban quilombos, como Palmares, en el Brasil, que resistió hasta 1695. '
                   'Los indígenas también se rebelaron: los calchaquíes lucharon contra los españoles entre 1630 y 1665. Todos buscaban '
                   'recuperar su libertad y vivir según sus propias costumbres.»',
             'Criterio anunciado en la consigna: un ejemplo de resistencia africana (1 punto), un ejemplo de resistencia indígena '
             '(1 punto), la explicación de qué buscaban (1 punto) y un texto ordenado (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Capitanías (1534); gobierno general en Salvador (1549)', 'Fechas habituales; cotejar.'),
    ('Fechas de Jamestown, Plymouth, Quebec, Nueva Ámsterdam, Barbados, Martinica, Guadalupe, Curazao, Jamaica y del Brasil holandés', 'Fechas habituales; cotejar.'),
    ('Más de doce millones de africanos embarcados (siglos XVI-XIX)', 'Estimación habitual de las bases de datos de la trata; cotejar.'),
    ('Palmares y Zumbi (1695); Benkos Biohó; levantamientos calchaquíes (1630-1665); Rebelión de los Pueblo (1680)', 'Fechas habituales; cotejar.'),
    ('Kamba Kua y los lanceros de Artigas (1820); esclavizados en estancias de órdenes religiosas', 'Bibliografía habitual; cotejar.'),
    ('Relato de Equiano (1789)', 'Versión escolar resumida y declarada como no textual; cotejar con una edición.'),
]

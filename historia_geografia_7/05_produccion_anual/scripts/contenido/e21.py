"""Encuentro 21 — Clase 13: Franciscanos y jesuitas en la cultura paraguaya (H5; tema H5d).

Corrige el maestro: distingue los pueblos franciscanos (cuyos habitantes
seguían sirviendo a los encomenderos) de las reducciones jesuíticas (exentas
de la encomienda); nombra a Bolaños y a Ruiz de Montoya; aclara que la
imprenta misionera es del siglo XVIII y que los Treinta Pueblos se reparten
entre el Paraguay, la Argentina y el Brasil actuales. La pérdida del Guairá y
Mbororé se desarrollan en la Continuación E.
"""
import curriculo as C

TITULO = 'Clase 13 — Franciscanos y jesuitas en la cultura paraguaya'
CLAVE = 'Clase 13 —'
INDICADORES = [
    'Diferencia los pueblos franciscanos de las reducciones jesuíticas.',
    'Describe la organización de una reducción jesuítico-guaraní.',
    'Reconoce aportes de franciscanos y jesuitas a la cultura paraguaya, en especial a la lengua guaraní.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H5'], C.TEMAS['H5d'], INDICADORES),

    ('h2', 'Los franciscanos y los pueblos de indios'),
    ('p', 'Los franciscanos llegaron al Paraguay en el siglo XVI. En 1575 arribaron fray Luis de Bolaños y fray Alonso de San '
          'Buenaventura, que recorrieron la región y reunieron a familias guaraníes en pueblos cercanos a Asunción, como Altos, '
          'Itá, Yaguarón y Tobatí, y más al sur Caazapá y Yuty.'),
    ('p', 'Bolaños aprendió el guaraní y tradujo a esa lengua el catecismo, es decir, el libro con las enseñanzas básicas de la fe. '
          'En 1603, el Sínodo de Asunción —una reunión de sacerdotes presidida por el obispo— dispuso que se enseñara la doctrina '
          'en guaraní con esa traducción. Fue un paso decisivo para que el guaraní se escribiera y se conservara.'),
    ('p', 'Atención: en los pueblos franciscanos, los indígenas seguían encomendados. Por turnos, debían ir a trabajar para los '
          'encomenderos, en sus chacras o en los yerbales.'),

    ('h2', 'Los jesuitas y las reducciones'),
    ('p', 'Los jesuitas, sacerdotes de la Compañía de Jesús, llegaron a fines del siglo XVI. Con el apoyo del gobernador '
          'Hernandarias y de la Corona, fundaron desde 1609 las reducciones: pueblos donde reunían a los guaraníes para '
          'evangelizarlos. La primera fue San Ignacio Guazú, al sur de Asunción; poco después fundaron otras en el Guairá.'),
    ('p', 'A diferencia de los pueblos franciscanos, los habitantes de las reducciones no estaban encomendados a particulares: '
          'pagaban un tributo directamente a la Corona. Por eso los encomenderos veían a los jesuitas como rivales, y hubo '
          'conflictos entre ellos durante todo el período colonial.'),
    ('fig', 'fig_13_1_reduccion.png', 'Figura 13.1 — Plano esquemático de una reducción jesuítico-guaraní.', 15.0),
    ('h2', 'Cómo era una reducción'),
    ('p', 'Cada reducción se organizaba alrededor de una gran plaza, con la iglesia, el colegio, los talleres y el cementerio a un '
          'lado, y las casas de las familias en hileras. La gobernaba un cabildo indígena, con corregidor, alcaldes y regidores '
          'guaraníes, bajo la conducción de dos sacerdotes. Las tierras se dividían en abambaé, parcelas de cada familia, y '
          'tupambaé, tierras comunes cuyos frutos se usaban para las viudas, los enfermos, el culto y el pago del tributo.'),
    ('p', 'En los talleres, los guaraníes trabajaron como carpinteros, herreros, tejedores, escultores y constructores. La música '
          'tuvo un lugar muy importante: fabricaban instrumentos, cantaban y tocaban en coros y orquestas. Ya en el siglo XVIII, las '
          'reducciones tuvieron incluso una imprenta propia.'),
    ('caja', 'concepto', 'Concepto clave — ',
     'Reducción: pueblo organizado por misioneros para reunir a indígenas dispersos y evangelizarlos. Las reducciones jesuíticas '
     'estaban exentas de la encomienda; los pueblos franciscanos, no. En ambos casos se transformó profundamente la vida de los '
     'guaraníes, que adoptaron el cristianismo y conservaron su lengua.'),

    ('h2', 'Aportes a la cultura paraguaya'),
    ('lista', ['La lengua: Bolaños tradujo el catecismo; Antonio Ruiz de Montoya, jesuita, publicó en 1639 y 1640 obras sobre la '
               'gramática y el vocabulario del guaraní. Gracias a ellos el guaraní tuvo escritura y diccionarios.',
               'El arte: las tallas de madera, la arquitectura de las iglesias y la música barroca de las misiones.',
               'Los oficios: carpintería, herrería, tejido y construcción.',
               'Los pueblos: muchas ciudades actuales nacieron como pueblos franciscanos o reducciones, como Yaguarón, Itá, Caazapá, '
               'San Ignacio, Santa María de Fe y Trinidad.']),
    ('caja', 'paraguay', 'En Paraguay — ',
     'Las reducciones jesuíticas llegaron a ser treinta pueblos en el siglo XVIII, repartidos entre territorios que hoy son del '
     'Paraguay, de la Argentina y del Brasil; ocho están en el Paraguay actual. Las ruinas de Trinidad y de Jesús, en Itapúa, son '
     'Patrimonio de la Humanidad de la UNESCO desde 1993. En 1767, el rey Carlos III expulsó a los jesuitas de todos los dominios '
     'españoles, incluido el Paraguay.'),

    ('fuente', 'Documento de época · Constituciones del Sínodo de Asunción (1603). Versión escolar resumida: no es cita textual.',
     ['El sínodo ordena que en todas las parroquias y pueblos de indios de la provincia se enseñe la doctrina cristiana en la lengua '
      'de los indios, usando el catecismo traducido al guaraní por fray Luis de Bolaños, y que no se use otra traducción.'],
     'Vocabulario: sínodo es una reunión de sacerdotes con el obispo para dictar normas; doctrina, las enseñanzas de la religión.',
     ['¿En qué lengua debía enseñarse la doctrina según el sínodo?',
      '¿Por qué creés que se ordenó usar una sola traducción?',
      '¿Qué consecuencia tuvo esta decisión para la lengua guaraní?']),
    ('renglones', 5),
    ('ubicate', 'Ubicate  ·  Plano (Figura 13.1)',
     'En el plano, ¿qué edificio ocupa el lugar principal frente a la plaza? ¿Dónde están las casas de las familias? ¿Para qué se '
     'usaban los frutos del tupambaé?'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. Fray Luis de Bolaños es recordado sobre todo por…'),
    ('opc', ['traducir el catecismo al guaraní', 'fundar la primera reducción jesuítica', 'expulsar a los jesuitas', 'dividir la provincia']),
    ('item', '2. Una diferencia entre las reducciones jesuíticas y los pueblos franciscanos es que en las reducciones…'),
    ('opc', ['no había iglesia', 'los indígenas no hablaban guaraní', 'los indígenas no estaban encomendados a particulares',
             'gobernaba un encomendero']),
    ('item', '3. El tupambaé era…'),
    ('opc', ['la parcela de cada familia', 'la tierra común cuyos frutos servían a viudas, enfermos, el culto y el tributo',
             'el nombre del cabildo indígena', 'el taller de los escultores']),
    ('item', '4. Los jesuitas fueron expulsados de los dominios españoles en…'),
    ('opc', ['1609', '1639', '1641', '1767']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. La primera reducción jesuítica, fundada en 1609, fue San Ignacio ________.'),
    ('item', '6. El jesuita Antonio Ruiz de ________ escribió obras sobre la gramática y el vocabulario del guaraní.'),
    ('item', '7. En las reducciones gobernaba un ________ indígena, con corregidor, alcaldes y regidores.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) Los habitantes de los pueblos franciscanos estaban libres de la encomienda.'),
    ('item', '9. (....) Las ruinas de Trinidad y de Jesús son Patrimonio de la Humanidad.'),
    ('item', '10. (....) Los treinta pueblos jesuíticos estaban todos en el territorio del Paraguay actual.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. ¿Por qué los encomenderos veían a los jesuitas como rivales?', 4),
    ('item', '12. Escribí un texto de 6 a 8 líneas sobre los aportes de franciscanos y jesuitas a la cultura paraguaya. Se tendrá en '
             'cuenta: un aporte de cada orden (2 puntos), la relación con la lengua guaraní (1 punto) y un texto ordenado (1 punto).', 8),
]

PLAN = {
    'material': 'Tomo: Clase 13 (Figura 13.1); si es posible, imágenes de las ruinas de Trinidad o de tallas misioneras con su fuente',
    'tema': C.TEMAS['H5d'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes distingan pueblos franciscanos y reducciones jesuíticas, describan una reducción y reconozcan '
                 'los aportes de ambas órdenes a la cultura paraguaya.',
    'funciones': {
        'Esenciales': 'En clase: Ubicate; fuente (preguntas 1 a 3); actividades 1, 2, 3 y 11.',
        'Consolidación': 'Actividades 4, 5, 8 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 22).',
        'Complementarias o domiciliarias': 'Actividades 6, 7, 10 y 12.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 12. Pregunta: «¿Conocen pueblos del Paraguay que tengan nombre de santo? ¿Por qué será?».',
             'Nombran pueblos (San Ignacio, Santa Rosa, Santiago…).', 'Lista en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–28', 'Lectura de «Los franciscanos y los pueblos de indios». Destaca que sus habitantes seguían encomendados.',
             'Resuelven la actividad 1.', 'Actividad 1 (esencial).'),
            ('28–50', 'Lectura de «Los jesuitas y las reducciones» y de «Cómo era una reducción» con la Figura 13.1.',
             'Resuelven el «Ubicate» y las actividades 2 y 3.', 'Ubicate y actividades 2 y 3 (esenciales).'),
            ('50–68', 'Presenta la versión resumida de las Constituciones del Sínodo de 1603.',
             'Responden las preguntas 1 a 3 de la fuente.', 'Fuente (esencial).'),
            ('68–82', 'Lectura de «Aportes a la cultura paraguaya» y de la caja «En Paraguay».',
             'Resuelven la actividad 11.', 'Actividad 11 (esencial).'),
            ('82–100', 'Acompaña; quien termina antes sigue con la consolidación.', 'Resuelven las actividades 4, 5, 8 y 9.',
             'Actividades de consolidación.'),
        ]),
        ('Cierre', [
            ('100–120', 'Cuadro en la pizarra «franciscanos / jesuitas» completado entre todos. Anticipa la Continuación E (los ataques bandeirantes). Lee los criterios de la actividad 12 y asigna la tarea.',
             'Completan el cuadro en el cuaderno.', 'Cuadro comparativo.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en vocabulario: glosario en la pizarra (reducción, catecismo, sínodo, tupambaé, abambaé, corregidor).',
        'Apoyo en la actividad 2: cuadro de dos columnas ya dibujado en la pizarra para completar.',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: buscar una palabra guaraní que figure en el Tesoro de la lengua guaraní de Montoya y explicar su significado.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Lectura de plano; análisis de fuente; cuadro comparativo; respuesta breve.',
        'instrumentos': 'Lista de cotejo con los tres indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Distingue pueblos franciscanos y reducciones por su relación con la encomienda.',
                      'Describe la organización de una reducción.',
                      'Nombra aportes de ambas órdenes, en especial a la lengua guaraní.'],
    },
    'precisiones': [
        'No generalizar: la exención de la encomienda vale para las reducciones jesuíticas, no para los pueblos franciscanos.',
        'La imprenta misionera es de comienzos del siglo XVIII; los Treinta Pueblos corresponden a su apogeo en ese siglo.',
        'La versión del Sínodo de 1603 es escolar y resumida; no leerla como cita textual.',
    ],
    'tarea': 'Actividades 6, 7, 10 y 12 de la Clase 13.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente', [
            ('F1', 'En la lengua de los indios, el guaraní.', ''),
            ('F2', 'Para que todos aprendieran lo mismo y no hubiera errores ni diferencias entre traducciones.', 'Se acepta una razón coherente.'),
            ('F3', 'El guaraní se escribió, se unificó y se siguió usando en la enseñanza y en la vida de los pueblos.', ''),
        ]),
        ('Ubicate (Figura 13.1)', [
            ('U', 'La iglesia. Las casas de las familias están en hileras a los costados de la plaza. Los frutos del tupambaé servían '
                  'para las viudas, los enfermos, el culto y el pago del tributo.', ''),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'a) traducir el catecismo al guaraní', ''),
            ('2', 'c) los indígenas no estaban encomendados a particulares', ''),
            ('3', 'b) la tierra común cuyos frutos servían a viudas, enfermos, el culto y el tributo', ''),
            ('4', 'd) 1767', ''),
        ]),
        ('Completá los espacios', [
            ('5', 'Guazú', ''),
            ('6', 'Montoya', ''),
            ('7', 'cabildo', ''),
        ]),
        ('Verdadero o falso', [
            ('8', 'Falso: seguían encomendados y trabajaban por turnos para los encomenderos.', 'Justificación obligatoria.'),
            ('9', 'Verdadero.', ''),
            ('10', 'Falso: estaban repartidos entre territorios del Paraguay, la Argentina y el Brasil actuales.', 'Justificación obligatoria.'),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'Porque los indígenas de las reducciones no estaban encomendados a particulares: los encomenderos no podían usar '
                   'su trabajo, y además los jesuitas defendían a los guaraníes frente a sus abusos.', 'Debe mencionar la encomienda.'),
            ('12', 'Ejemplo: «Los franciscanos, con fray Luis de Bolaños, fundaron pueblos como Yaguarón e Itá y tradujeron el catecismo al '
                   'guaraní. Los jesuitas organizaron las reducciones, con talleres y música, y Ruiz de Montoya escribió una gramática y '
                   'un vocabulario del guaraní. Gracias a ellos, el guaraní tuvo escritura y se conservó.»',
             'Criterio anunciado en la consigna: un aporte de cada orden (2 puntos), la relación con la lengua guaraní (1 punto) y un '
             'texto ordenado (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Llegada de Bolaños y San Buenaventura (1575); pueblos franciscanos (Altos, Itá, Yaguarón, Tobatí, Caazapá, Yuty)', 'Bibliografía habitual; cotejar fechas de fundación.'),
    ('Sínodo de Asunción (1603) y el catecismo de Bolaños', 'Versión escolar resumida y declarada como no textual; cotejar con una edición de las constituciones sinodales.'),
    ('San Ignacio Guazú (1609); primeras reducciones del Guairá', 'Fechas habituales; cotejar.'),
    ('Obras de Ruiz de Montoya sobre el guaraní (1639-1640)', 'Tesoro de la lengua guaraní (1639) y Arte y Vocabulario (1640); cotejar.'),
    ('Treinta pueblos y ocho en el Paraguay actual; UNESCO 1993; expulsión de 1767', 'Datos habituales; cotejar.'),
]

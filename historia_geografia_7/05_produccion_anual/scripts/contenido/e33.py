"""Encuentro 33 — Clase 21: La gestión ambiental en el Paraguay (G4; tema G4c).

Leyes e instituciones nombradas por número y año, con la advertencia de
cotejarlas en la Biblioteca y Archivo Central del Congreso (BACN). La única
cita textual es la primera oración del art. 7 de la Constitución; el resto
son paráfrasis declaradas.
"""
import curriculo as C

TITULO = 'Clase 21 — La gestión ambiental en el Paraguay'
CLAVE = 'Clase 21 —'
INDICADORES = [
    'Explica qué es la gestión ambiental y qué es una política ambiental.',
    'Reconoce las principales instituciones encargadas del ambiente y sus funciones.',
    'Relaciona normas ambientales vigentes con problemas ambientales concretos.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['G4'], C.TEMAS['G4c'], INDICADORES),

    ('h2', 'Qué es la gestión ambiental'),
    ('p', 'La gestión ambiental es el conjunto de acciones para usar los recursos naturales sin agotarlos y para prevenir, controlar '
          'y reparar los daños al ambiente. La realizan el Estado, mediante leyes e instituciones, pero también las empresas, las '
          'organizaciones, las comunidades y cada persona. Una política ambiental es el conjunto de objetivos y reglas que orienta '
          'esas acciones en un país.'),

    ('h2', 'El ambiente en la Constitución'),
    ('p', 'La Constitución Nacional de 1992 reconoce el derecho de las personas a un ambiente sano. Su artículo 7 comienza así: '
          '«Toda persona tiene derecho a habitar en un ambiente saludable y ecológicamente equilibrado». El artículo 8 establece, '
          'con palabras de esta síntesis, que las actividades que puedan dañar el ambiente deben ser reguladas por la ley y que '
          'el delito ecológico será castigado y el daño, reparado.'),

    ('h2', 'Las instituciones'),
    ('lista', ['El Ministerio del Ambiente y Desarrollo Sostenible (MADES) es la autoridad ambiental nacional. Fue creado en 2018 '
               'sobre la base de la Secretaría del Ambiente (SEAM), que funcionaba desde 2000. Formula la política ambiental, revisa '
               'las evaluaciones de impacto ambiental y administra las áreas silvestres protegidas.',
               'El Instituto Forestal Nacional (INFONA) se ocupa de los bosques: controla los planes de uso de la tierra y promueve '
               'la reforestación.',
               'El Ministerio Público tiene fiscalías especializadas en delitos ambientales, y el Poder Judicial juzga esos delitos.',
               'Las gobernaciones y municipalidades se ocupan de temas locales, como la recolección de residuos y el cuidado de '
               'arroyos y espacios verdes.']),
    ('fig', 'fig_21_1_gestion.png', 'Figura 21.1 — Instituciones y normas de la gestión ambiental en el Paraguay (esquema simplificado).', 15.0),

    ('h2', 'Algunas normas vigentes'),
    ('tabla', ['Norma', 'Qué establece (síntesis)', 'Ejemplo de aplicación'],
     [['Ley 294/1993', 'Las obras y actividades que puedan dañar el ambiente necesitan una evaluación de impacto ambiental aprobada.',
       'Antes de construir un puerto o una ruta, se estudian sus efectos.'],
      ['Ley 352/1994', 'Crea el sistema de áreas silvestres protegidas: parques nacionales, reservas y monumentos naturales.',
       'Parques nacionales como el Defensores del Chaco o el Ybycuí.'],
      ['Ley 716/1996', 'Castiga los delitos contra el medio ambiente, como contaminar ríos o talar bosques protegidos.',
       'Una industria que vierte residuos tóxicos a un arroyo.'],
      ['Ley 2524/2004', 'Prohíbe transformar bosques en tierras de cultivo o de pastoreo en la Región Oriental (fue prorrogada).',
       'No se puede desmontar un bosque del Alto Paraná para sembrar.']],
     [2.2, 4.4, 3.4]),
    ('caja', 'concepto', 'Concepto clave — ',
     'Gestión ambiental: acciones para usar los recursos sin agotarlos y prevenir, controlar y reparar daños. Evaluación de impacto '
     'ambiental: estudio previo de los efectos de una obra. Área silvestre protegida: territorio que la ley protege por su valor natural.'),
    ('caja', 'paraguay', 'En Paraguay — ',
     'Las leyes no alcanzan si no se cumplen. La participación de la ciudadanía es clave: cualquier persona puede denunciar un daño '
     'ambiental ante el MADES, la municipalidad o el Ministerio Público.'),

    ('fuente', 'Documento · Constitución Nacional (1992), art. 7. Cita textual de la primera oración (cotejar con la edición oficial de la BACN).',
     ['«Toda persona tiene derecho a habitar en un ambiente saludable y ecológicamente equilibrado.»'],
     'Vocabulario: ecológicamente equilibrado quiere decir que sus seres vivos y su ambiente se mantienen en armonía, sin daños graves.',
     ['¿Qué derecho reconoce el artículo?',
      '¿A quiénes se aplica ese derecho? Citá la palabra que lo muestra.',
      'Nombrá una institución y una ley que ayudan a cumplir ese derecho.']),
    ('renglones', 5),
    ('ubicate', 'Ubicate  ·  Esquema (Figura 21.1)',
     'En la Figura 21.1, ¿qué norma está en el lugar más alto? ¿Qué institución se ocupa de los bosques? ¿Quiénes participan además del Estado?'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. La autoridad ambiental nacional del Paraguay es…'),
    ('opc', ['el Ministerio de Educación', 'la Municipalidad de Asunción', 'el Instituto Forestal Nacional',
             'el Ministerio del Ambiente y Desarrollo Sostenible']),
    ('item', '2. La Ley 294/1993 exige…'),
    ('opc', ['plantar un árbol por persona', 'una evaluación de impacto ambiental antes de ciertas obras',
             'cerrar todas las industrias', 'prohibir la pesca']),
    ('item', '3. Un parque nacional es…'),
    ('opc', ['un área silvestre protegida por ley', 'una plaza de una ciudad', 'una zona de cultivo', 'un puerto de la Hidrovía']),
    ('item', '4. La ley de 2004 que se aplica en la Región Oriental prohíbe…'),
    ('opc', ['la ganadería', 'la construcción de casas', 'transformar bosques en tierras de cultivo o pastoreo', 'la navegación']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. El artículo ________ de la Constitución reconoce el derecho a un ambiente saludable.'),
    ('item', '6. El INFONA se ocupa sobre todo de los ________.'),
    ('item', '7. Los delitos contra el ambiente los investiga el Ministerio ________.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) La gestión ambiental es tarea solo del Estado.'),
    ('item', '9. (....) Cualquier persona puede denunciar un daño ambiental.'),
    ('item', '10. (....) El MADES se creó en 1992 con la Constitución.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. Elegí un problema ambiental de tu localidad y decí qué institución y qué norma podrían ayudar a resolverlo.', 4),
    ('item', '12. Escribí un texto de 6 a 8 líneas sobre por qué son necesarias las leyes ambientales. Se tendrá en cuenta: el '
             'derecho que protegen (1 punto), un ejemplo de norma con lo que establece (1 punto), el papel de la ciudadanía '
             '(1 punto) y un texto ordenado (1 punto).', 8),
]

PLAN = {
    'material': 'Tomo: Clase 21 (Figura 21.1); un ejemplar de la Constitución Nacional si la escuela lo tiene',
    'tema': C.TEMAS['G4c'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes reconozcan las instituciones y normas ambientales del Paraguay y las relacionen con problemas concretos.',
    'funciones': {
        'Esenciales': 'En clase: Ubicate; fuente (preguntas 1 a 3); actividades 1, 2, 4 y 11.',
        'Consolidación': 'Actividades 3, 5, 8 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 34).',
        'Complementarias o domiciliarias': 'Actividades 6, 7, 10 y 12.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 20. Pregunta: «Si alguien tira residuos a un arroyo del barrio, ¿a quién se puede recurrir?».',
             'Proponen respuestas.', 'Ideas en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–25', 'Lectura de «Qué es la gestión ambiental» y de «El ambiente en la Constitución».',
             'Responden las preguntas 1 a 3 de la fuente.', 'Fuente (esencial).'),
            ('25–45', 'Lectura de «Las instituciones» con la Figura 21.1.',
             'Resuelven el «Ubicate» y la actividad 1.', 'Ubicate y actividad 1 (esenciales).'),
            ('45–65', 'Lectura del cuadro «Algunas normas vigentes» y del Concepto clave.',
             'Resuelven las actividades 2 y 4.', 'Actividades 2 y 4 (esenciales).'),
            ('65–85', 'Organiza parejas para relacionar un problema local con una institución y una norma.',
             'Resuelven la actividad 11 y la comparten con otra pareja.', 'Actividad 11 (esencial).'),
            ('85–100', 'Acompaña; quien termina antes sigue con la consolidación.', 'Resuelven las actividades 3, 5, 8 y 9.',
             'Actividades de consolidación.'),
        ]),
        ('Cierre', [
            ('100–120', 'Puesta en común de la actividad 11: lista de problemas locales con su institución y su norma. Lee los criterios de la actividad 12 y asigna la tarea.',
             'Comparan y corrigen.', 'Lista de problemas y soluciones.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en la actividad 11: tarjetas con problemas frecuentes (basura, quema, desmonte, arroyo contaminado) para elegir.',
        'Apoyo en la lectura del cuadro de normas: el docente lee cada fila con un ejemplo cercano.',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: buscar en el sitio del MADES qué área silvestre protegida está más cerca de la localidad.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Análisis de fuente; lectura de esquema; relación problema-institución-norma.',
        'instrumentos': 'Lista de cotejo con los tres indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Explica qué es la gestión ambiental.',
                      'Reconoce instituciones ambientales y sus funciones.',
                      'Relaciona una norma con un problema ambiental concreto.'],
    },
    'precisiones': [
        'La primera oración del art. 7 se cita textualmente; el art. 8 y las leyes van en síntesis de la editorial. Cotejar en la BACN.',
        'Las leyes y su vigencia (prórrogas de la Ley 2524/2004, creación del MADES en 2018) deben verificarse antes de cada edición.',
    ],
    'tarea': 'Actividades 6, 7, 10 y 12 de la Clase 21.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente', [
            ('F1', 'El derecho a habitar en un ambiente saludable y ecológicamente equilibrado.', ''),
            ('F2', 'A todas las personas: «Toda persona».', 'Debe citar la expresión.'),
            ('F3', 'Por ejemplo, el MADES y la Ley 294/1993 de evaluación de impacto ambiental.', 'Se acepta cualquier institución y ley estudiadas.'),
        ]),
        ('Ubicate (Figura 21.1)', [
            ('U', 'La Constitución Nacional (arts. 7 y 8). El INFONA. Los gobiernos departamentales y municipales, las organizaciones de '
                  'la sociedad civil, las comunidades indígenas y cada ciudadano.', ''),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'd) el Ministerio del Ambiente y Desarrollo Sostenible', ''),
            ('2', 'b) una evaluación de impacto ambiental antes de ciertas obras', ''),
            ('3', 'a) un área silvestre protegida por ley', ''),
            ('4', 'c) transformar bosques en tierras de cultivo o pastoreo', ''),
        ]),
        ('Completá los espacios', [
            ('5', '7', ''),
            ('6', 'bosques', ''),
            ('7', 'Público', ''),
        ]),
        ('Verdadero o falso', [
            ('8', 'Falso: también participan las empresas, las organizaciones, las comunidades y cada persona.', 'Justificación obligatoria.'),
            ('9', 'Verdadero.', ''),
            ('10', 'Falso: se creó en 2018, sobre la base de la Secretaría del Ambiente (desde 2000).', 'Justificación obligatoria.'),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'Ejemplo: un arroyo contaminado por una industria; puede intervenir el MADES o el Ministerio Público; norma: Ley '
                   '716/1996 de delitos contra el medio ambiente.', 'Problema, institución y norma coherentes entre sí.'),
            ('12', 'Ejemplo: «Las leyes ambientales protegen el derecho a vivir en un ambiente sano, que reconoce la Constitución. Por '
                   'ejemplo, la Ley 294/1993 exige estudiar los efectos de una obra antes de hacerla. Pero las leyes solo funcionan si '
                   'la ciudadanía las conoce, las respeta y denuncia los daños.»',
             'Criterio anunciado en la consigna: el derecho que protegen (1 punto), un ejemplo de norma con lo que establece (1 punto), '
             'el papel de la ciudadanía (1 punto) y un texto ordenado (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Constitución, art. 7 (primera oración, cita textual) y art. 8 (síntesis)', 'Cotejar con la edición oficial (BACN).'),
    ('MADES (2018, sobre la base de la SEAM, creada en 2000); INFONA', 'Leyes 6123/2018, 1561/2000 y 3464/2008 según la bibliografía; cotejar.'),
    ('Leyes 294/1993, 352/1994, 716/1996 y 2524/2004 (prorrogada por la Ley 6676/2020)', 'Cotejar números, años, contenido y vigencia en la BACN.'),
    ('Parques nacionales Defensores del Chaco e Ybycuí', 'Cotejar en el registro del MADES.'),
]

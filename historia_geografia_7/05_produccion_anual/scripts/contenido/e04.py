"""Encuentro 4 — Continuación A: Taller de fuentes sobre los guaraníes (H1; tema H1c).

Profundiza la Clase 3 con un taller de análisis de fuentes. Corrige el
problema del maestro (un taller que describía fuentes sin mostrarlas): las
cuatro fuentes están impresas y cada una dice qué es y de dónde viene.
"""
import curriculo as C

TITULO = 'Continuación A — Taller de fuentes sobre los guaraníes'
CLAVE = 'Continuación A —'
INDICADORES = [
    'Distingue fuentes materiales, escritas, lingüísticas y legales, y quién las produjo.',
    'Diferencia en un texto un dato, una interpretación y una opinión.',
    'Relaciona afirmaciones sobre los guaraníes con la evidencia que las sostiene y con sus límites.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H1'], C.TEMAS['H1c'], INDICADORES),
    ('h2', 'Pensar como investigadores'),
    ('p', 'En la Clase 3 leíste muchas afirmaciones sobre los guaraníes. ¿Cómo sabemos que son ciertas? En este taller vas a '
          'trabajar como un equipo de investigación: vas a relacionar cada afirmación con una evidencia, es decir, con una fuente '
          'que la sostiene, y vas a pensar también qué no puede decirnos esa fuente.'),
    ('caja', 'concepto', 'Concepto clave — ',
     'Un dato es una información que se puede comprobar en una fuente («los carios cultivaban mandioca»). Una interpretación '
     'explica o relaciona datos («la reciprocidad daba prestigio al líder»). Una opinión es una valoración personal («era la '
     'mejor forma de vivir»). Las tres son útiles, pero no valen lo mismo como prueba.'),
    ('tabla', ['Pregunta', 'Para qué sirve'],
     [['¿Quién produjo la fuente y cuándo?', 'Para saber si es primaria o secundaria y desde qué mirada fue hecha.'],
      ['¿Qué dice o muestra?', 'Para extraer datos.'],
      ['¿Qué no dice o qué deja afuera?', 'Para reconocer sus límites.'],
      ['¿Coincide con otras fuentes?', 'Para confirmar o discutir una afirmación.']],
     [4.0, 6.0]),

    ('fuente', 'Cuatro fuentes para el taller',
     ['Fuente A · Síntesis arqueológica (fuente secundaria, elaborada por la editorial a partir de la bibliografía arqueológica '
      'regional). En los sitios guaraníes de la cuenca del Paraná se hallan con frecuencia grandes vasijas de cerámica, algunas '
      'con la superficie marcada por los dedos (corrugada) y otras pintadas; urnas con restos humanos; hachas de piedra pulida y '
      'tembetás.',
      'Fuente B · Crónica: versión escolar resumida del relato de Ulrico Schmidl (publicado en 1567), leída en la Clase 3. '
      'Los carios tenían maíz, mandioca, batatas, maní, pescado, carne y miel; hacían la guerra y comían a algunos prisioneros.',
      'Fuente C · Topónimos actuales del Paraguay (nombres de lugares): Ypacaraí, Ypané, Itá, Itauguá, Itapúa, Caaguazú, '
      'Yvytyruzú. En guaraní, y significa «agua»; ita, «piedra»; ka\'a, «hierba» o «monte»; guasu, «grande»; yvyty, «cerro».',
      'Fuente D · Constitución Nacional (1992), artículo 140: «El Paraguay es un país pluricultural y bilingüe. Son idiomas '
      'oficiales el castellano y el guaraní.»'],
     '',
     ['Clasificá cada fuente: ¿material, escrita, lingüística o legal? ¿Primaria o secundaria para estudiar a los guaraníes de 1500?',
      '¿Qué fuente aporta datos sobre la alimentación? ¿Y sobre la cerámica?',
      '¿Qué nos dice la Fuente C sobre la relación de los guaraníes con su ambiente?',
      '¿Cuál de las cuatro fuentes fue producida por alguien ajeno a la cultura guaraní? ¿Qué cuidado hay que tener al leerla?']),
    ('renglones', 8),

    ('h2', 'Consignas del taller'),
    ('p', 'Trabajen en grupos de cuatro. Usen las cuatro fuentes y lo que estudiaron en la Clase 3. Cada grupo completa la matriz '
          'de la Ficha A y escribe una conclusión.'),
    ('consigna', 'Consignas del taller:'),
    ('item', '1. En la oración «Los guaraníes cultivaban maíz y mandioca; seguramente era la mejor dieta de América», '
             'subrayá el dato y encerrá la opinión. Explicá la diferencia.', 3),
    ('item', '2. Completá en la Ficha A tres afirmaciones con su evidencia y su límite. Una ya está resuelta como ejemplo.'),
    ('item', '3. ¿Qué afirmación de la Clase 3 no puede comprobarse con estas cuatro fuentes? ¿Qué otra fuente haría falta?', 3),
    ('item', '4. Escribí una conclusión del grupo de 5 a 7 líneas: ¿qué sabemos de los guaraníes de 1500 y cómo lo sabemos? '
             'Se tendrá en cuenta: dos afirmaciones con su fuente (2 puntos), un límite de alguna fuente (1 punto) y '
             'redacción clara (1 punto).', 7),
    ('h3', 'Autoevaluación del taller'),
    ('tabla', ['Criterio', 'Lo logré', 'En proceso', 'Todavía no'],
     [['Distinguí un dato de una opinión.', '', '', ''],
      ['Relacioné cada afirmación con una fuente.', '', '', ''],
      ['Reconocí qué no puede decir una fuente.', '', '', ''],
      ['Escuché y tuve en cuenta las ideas de mi grupo.', '', '', '']],
     [5.5, 1.5, 1.5, 1.5]),
]

FICHAS = [
    ('ficha_repro', 'Ficha reproducible A — Matriz de evidencias',
     [('p', 'Completen una fila por afirmación. La primera fila es un ejemplo.'),
      ('tabla', ['Afirmación', 'Evidencia (fuente)', 'Límite: qué no puede decir esa fuente'],
       [['Los guaraníes fabricaban cerámica para cocinar, guardar y enterrar a sus muertos.', 'Fuente A: vasijas y urnas halladas en sitios guaraníes.',
         'No dice qué significado tenía cada vasija para quienes la usaban.']],
       [3.4, 3.3, 3.3]),
      ('cuadro', ['Afirmación', 'Evidencia (fuente)', 'Límite: qué no puede decir esa fuente'], ['', '', ''], [3.4, 3.3, 3.3]),
      ('p', 'Conclusión del grupo:'),
      ('renglones', 7)]),
]

PLAN = {
    'material': 'Tomo: Continuación A y Ficha reproducible A (una copia por grupo, preparada antes del encuentro)',
    'tema': C.TEMAS['H1c'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes analicen críticamente fuentes sobre los guaraníes y distingan dato, interpretación y opinión.',
    'funciones': {
        'Esenciales': 'En clase: fuente (preguntas 1 a 4); consignas 1, 2 y 4 del taller; Ficha A.',
        'Consolidación': 'En clase: consigna 3 y autoevaluación del taller.',
        'Complementarias o domiciliarias': 'Pasar en limpio la conclusión individual (optativo); buscar el significado de dos topónimos de su departamento.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 3. Escribe en la pizarra: «¿Cómo sabemos lo que sabemos de los guaraníes?».',
             'Proponen respuestas.', 'Ideas en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–25', 'Lectura de «Pensar como investigadores», del Concepto clave y del cuadro de preguntas.',
             'Resuelven la consigna 1 en parejas.', 'Consigna 1 (esencial).'),
            ('25–50', 'Organiza grupos de 4 y lee en voz alta las cuatro fuentes.',
             'Responden las preguntas 1 a 4 de la fuente.', 'Fuente (esencial).'),
            ('50–75', 'Entrega la Ficha A y modela la fila de ejemplo.',
             'Completan la matriz (consigna 2) y resuelven la consigna 3.', 'Ficha A; consignas 2 y 3.'),
            ('75–95', 'Lee los criterios de la consigna 4 y acompaña la escritura.',
             'Escriben la conclusión del grupo (consigna 4).', 'Consigna 4 (esencial).'),
        ]),
        ('Cierre', [
            ('95–110', 'Dos grupos leen su conclusión; el docente señala qué afirmación tiene mejor evidencia.',
             'Comparan conclusiones.', 'Exposición oral.'),
            ('110–120', 'Explica la autoevaluación y asigna la tarea.',
             'Completan la autoevaluación del taller.', 'Autoevaluación.'),
        ]),
    ],
    'diversidad': [
        'Roles en el grupo: lector, secretario, buscador de evidencias y portavoz; quien tiene dificultades de lectura puede ser portavoz.',
        'Apoyo en la matriz: tarjetas con tres afirmaciones ya escritas para que el grupo solo busque evidencia y límite.',
        'Desafío: proponer una quinta fuente (por ejemplo, una entrevista a un hablante de guaraní) y explicar qué aportaría.',
    ],
    'evaluacion': {
        'tipo': 'Formativa, con producto.',
        'procedimientos': 'Análisis de fuentes; matriz de evidencias; conclusión escrita.',
        'instrumentos': 'Ficha A; autoevaluación; consigna 4 con los criterios de su consigna.',
        'criterios': ['Clasifica las fuentes y reconoce su origen.',
                      'Distingue dato y opinión.',
                      'Relaciona al menos dos afirmaciones con su evidencia y nombra un límite.'],
    },
    'precisiones': [
        'La Fuente A es secundaria (síntesis de la editorial) y la Fuente B es una versión resumida: decirlo es parte del aprendizaje.',
        'No se califica la opinión del grupo sobre los guaraníes, sino el uso de la evidencia.',
    ],
    'tarea': 'Buscar el significado de dos topónimos guaraníes de su departamento (optativo).',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente', [
            ('F1', 'A: material descrita en una síntesis; es secundaria (la escribió la editorial), aunque se basa en restos materiales '
                   'que son primarios. B: escrita, primaria en su origen (un testigo del siglo XVI), aunque aquí está resumida. '
                   'C: lingüística, actual: secundaria para 1500, pero conserva palabras antiguas. D: legal, de 1992: no sirve como '
                   'fuente primaria sobre 1500.', 'Se valora que explique la diferencia entre el objeto original y su descripción.'),
            ('F2', 'Alimentación: Fuente B. Cerámica: Fuente A.', ''),
            ('F3', 'Que nombraban los lugares por sus rasgos naturales: agua, piedras, montes, cerros. Muestra un conocimiento '
                   'cercano del ambiente.', ''),
            ('F4', 'La Fuente B: la escribió un soldado europeo de la conquista. Hay que tener en cuenta su mirada y sus intereses, y '
                   'compararla con otras fuentes.', ''),
        ]),
        ('Consignas del taller', [
            ('1', 'Dato: «Los guaraníes cultivaban maíz y mandioca». Opinión: «seguramente era la mejor dieta de América». El dato '
                  'puede comprobarse en fuentes; la opinión es una valoración.', ''),
            ('2', 'Ejemplos: «Los carios cultivaban maíz y mandioca» – Fuente B – la escribió un europeo y está resumida. «Los '
                  'guaraníes nombraban los lugares por el agua y las piedras» – Fuente C – los nombres actuales pueden haber '
                  'cambiado. «El guaraní es idioma oficial» – Fuente D – no informa sobre los guaraníes de 1500.',
             'Se aceptan otras afirmaciones si la evidencia corresponde.'),
            ('3', 'Por ejemplo, el papel de los niños o las creencias religiosas: harían falta otras crónicas o estudios '
                  'etnográficos de comunidades guaraníes actuales.', ''),
            ('4', 'Ejemplo: «Sabemos que los guaraníes cultivaban maíz y mandioca por los relatos de cronistas como Schmidl, y que '
                  'fabricaban cerámica por los hallazgos arqueológicos. Pero los cronistas eran conquistadores y miraban desde '
                  'afuera, por eso hay que comparar sus relatos con otras fuentes.»',
             'Criterio anunciado en la consigna: dos afirmaciones con su fuente (2 puntos), un límite de alguna fuente (1 punto) y redacción clara (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Significado de y, ita, ka\'a, guasu, yvyty', 'Vocabulario guaraní básico; cotejar con un diccionario (por ejemplo, el de la Academia de la Lengua Guaraní).'),
    ('Hallazgos arqueológicos guaraníes (cerámica corrugada y pintada, urnas, hachas pulidas, tembetás)', 'Síntesis de la arqueología regional; cotejar.'),
]

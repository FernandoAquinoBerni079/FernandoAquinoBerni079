"""Encuentro 10 — Clase 6: Los avances náuticos y la llegada de los europeos (H4; temas H4a y H4b).

Los primeros 20 minutos se reservan para la devolución de la Evaluación de la
Unidad 2 (regla de equidad A10); la clase dispone de 100 minutos.
Corrige el maestro: se retira el «diario de un navegante» inventado y se usa
un fragmento del Diario de Colón; se agregan los viajes portugueses,
Magallanes-Elcano y la conquista de México y del Perú; se evita el anacronismo
«España» para la Corona de Castilla de 1492.
"""
import curriculo as C

TITULO = 'Clase 6 — Los avances náuticos y la llegada de los europeos'
CLAVE = 'Clase 6 —'
INDICADORES = [
    'Explica qué avances técnicos permitieron navegar mar adentro y ampliar el conocimiento geográfico.',
    'Distingue causas y consecuencias de la llegada de los europeos a América.',
    'Describe la mentalidad del conquistador a partir de una fuente de la época.',
    'Ubica en un mapa y en el tiempo los principales viajes de exploración.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H4'], C.TEMAS['H4a'] + ' ' + C.TEMAS['H4b'], INDICADORES),

    ('h2', 'Europa busca nuevas rutas'),
    ('p', 'En el siglo XV, los comerciantes europeos compraban en Asia especias (pimienta, clavo, canela), seda y piedras '
          'preciosas. Esas mercaderías llegaban por largas rutas terrestres y por el Mediterráneo oriental, pasando por muchos '
          'intermediarios que encarecían los productos. Después de que el Imperio otomano tomó Constantinopla en 1453, los '
          'europeos tuvieron todavía más interés en llegar a Asia por mar, sin depender de otros.'),
    ('p', 'A ese motivo económico se sumaban otros: la búsqueda de oro y plata, el deseo de extender la fe cristiana, el '
          'interés de los reyes por aumentar su poder y sus territorios, y la curiosidad por conocer el mundo.'),

    ('h2', 'Los avances que permitieron navegar mar adentro'),
    ('p', 'Para alejarse de la costa y volver con seguridad hacían falta barcos resistentes y formas de orientarse en alta mar '
          '(Figura 6.1). La carabela combinaba velas cuadradas, útiles con viento a favor, y velas triangulares o latinas, que '
          'permitían avanzar aun con viento en contra. La brújula indicaba el norte aunque no se viera la costa, y el astrolabio '
          'y el cuadrante medían la altura del Sol o de la estrella Polar para calcular la latitud. Las cartas náuticas reunían '
          'lo que cada viaje aprendía sobre costas, puertos y vientos, y la imprenta difundió mapas y relatos por toda Europa.'),
    ('fig', 'fig_6_2_navegacion.png', 'Figura 6.1 — Avances que permitieron navegar mar adentro.', 15.0),

    ('h2', 'Los viajes de Portugal y de Castilla'),
    ('p', 'Portugal fue el primero en explorar el Atlántico. Impulsados por el príncipe Enrique, llamado el Navegante, sus '
          'marinos avanzaron por la costa de África. En 1488, Bartolomeu Dias llegó al extremo sur de África, al cabo de Buena '
          'Esperanza, y en 1498 Vasco da Gama llegó a la India por mar. En 1500, Pedro Álvares Cabral llegó a la costa del Brasil.'),
    ('p', 'Cristóbal Colón propuso llegar a Asia navegando hacia el oeste. Los Reyes Católicos, Isabel de Castilla y Fernando de '
          'Aragón, aceptaron su proyecto, y el viaje se hizo por cuenta de la Corona de Castilla (todavía no existía España como '
          'un Estado unificado como hoy). El 12 de octubre de 1492, Colón llegó a una isla de las Bahamas, que los habitantes '
          'llamaban Guanahaní. Hizo cuatro viajes y murió en 1506 convencido de haber llegado a Asia.'),
    ('p', 'Otros navegantes comprendieron que se trataba de un continente desconocido para los europeos. Américo Vespucio lo '
          'describió como un «nuevo mundo», y en 1507 un mapa lo llamó América en su honor. En 1513, Vasco Núñez de Balboa '
          'cruzó Panamá y vio el océano Pacífico. Entre 1519 y 1522, la expedición de Fernando de Magallanes, completada por '
          'Juan Sebastián Elcano tras la muerte de Magallanes, dio la primera vuelta al mundo (Figura 6.2).'),
    ('fig', 'fig_6_1_viajes.png', 'Figura 6.2 — Principales viajes de exploración de Portugal y de Castilla (trazados aproximados).', 16.0),

    ('h2', 'La conquista: de las islas a los imperios'),
    ('p', 'Desde las islas del Caribe, los castellanos avanzaron sobre el continente. Entre 1519 y 1521, Hernán Cortés conquistó '
          'Tenochtitlan con la ayuda de miles de guerreros indígenas enemigos de los mexicas, como los tlaxcaltecas. Entre 1532 y '
          '1533, Francisco Pizarro capturó y ejecutó al Inca Atahualpa, aprovechando una guerra civil en el imperio. Las '
          'epidemias de viruela y otras enfermedades traídas de Europa, contra las que los americanos no tenían defensas, '
          'debilitaron a los pueblos antes y durante las guerras.'),

    ('h2', 'Consecuencias de la llegada europea'),
    ('tabla', ['Para los pueblos americanos', 'Para Europa', 'Para el mundo'],
     [['Conquista, pérdida de tierras y trabajo forzado.', 'Llegada de oro y plata americanos.',
       'Intercambio de plantas y animales entre continentes.'],
      ['Caída enorme de la población por guerras, epidemias y abusos.', 'Nuevos alimentos: maíz, papa, tomate, cacao.',
       'Primeras rutas que unen todos los océanos.'],
      ['Mestizaje e imposición de la religión y la lengua de los conquistadores.', 'Más poder de los reyes de Castilla y Portugal.',
       'Nueva imagen de la Tierra en los mapas.']],
     [3.4, 3.3, 3.3]),
    ('caja', 'concepto', 'Concepto clave — ',
     '¿«Descubrimiento» o «encuentro»? Para los europeos fue un descubrimiento, porque no conocían América. Pero el continente '
     'estaba habitado desde hacía miles de años. Hoy muchos historiadores hablan de «llegada de los europeos» o de «encuentro», '
     'sin olvidar que fue también una conquista violenta.'),

    ('h2', 'La mentalidad del conquistador'),
    ('p', 'Muchos conquistadores venían de una España que acababa de terminar la guerra contra el último reino musulmán de la '
          'península (Granada, 1492). Buscaban riqueza, honor y ascenso social, y creían que conquistar y convertir a otros pueblos '
          'al cristianismo era justo. Algunos creían en lugares legendarios llenos de oro. Desde 1513, antes de atacar, se leía a '
          'los indígenas un texto en castellano, el Requerimiento, que les exigía aceptar al rey y a la Iglesia; casi nunca lo '
          'entendían.'),
    ('p', 'También hubo voces críticas dentro de la propia sociedad española, como la del fraile Bartolomé de las Casas, que '
          'denunció los abusos contra los indígenas.'),

    ('fuente', 'Fuente escrita · Diario de a bordo del primer viaje de Cristóbal Colón, entrada del 11 al 12 de octubre de 1492. '
               'Fragmento en versión modernizada. El diario original se perdió: lo conocemos por un resumen hecho por Bartolomé de las Casas.',
     ['«Ellos deben ser buenos servidores y de buen ingenio, que veo que muy presto dicen todo lo que les decía, y creo que '
      'ligeramente se harían cristianos, que me pareció que ninguna secta tenían.»'],
     'Vocabulario: presto, rápido; ligeramente, fácilmente; secta, aquí religión.',
     ['¿Quién escribió el diario, en qué fecha y en qué situación?',
      '¿Qué piensa Colón que podrían ser los habitantes de la isla? Citá las palabras.',
      '¿Qué muestra este fragmento sobre la mentalidad del conquistador? ¿Por qué hay que tener en cuenta que lo conocemos por un resumen?']),
    ('renglones', 6),
    ('ubicate', 'Ubicate  ·  Mapa (Figura 6.2)',
     'Seguí con el dedo el viaje de Vasco da Gama y el de Colón. ¿Hacia dónde navegó cada uno para llegar a Asia? ¿Por qué el '
     'viaje de Magallanes y Elcano demostró que la Tierra se puede rodear por mar?'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. El astrolabio servía para…'),
    ('opc', ['calcular la latitud midiendo la altura de los astros', 'medir la profundidad del mar', 'impulsar el barco con viento en contra',
             'imprimir mapas']),
    ('item', '2. El primer navegante que llegó a la India por mar, rodeando África, fue…'),
    ('opc', ['Cristóbal Colón', 'Vasco da Gama', 'Fernando de Magallanes', 'Américo Vespucio']),
    ('item', '3. Una consecuencia de la llegada europea para los pueblos americanos fue…'),
    ('opc', ['el aumento de su población', 'la libertad para elegir a sus autoridades', 'la caída de su población por epidemias y guerras',
             'el fin de toda forma de trabajo']),
    ('item', '4. El primer viaje de Colón se hizo por cuenta de…'),
    ('opc', ['la república de Venecia', 'el rey de Portugal', 'el Imperio otomano', 'la Corona de Castilla']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. La primera vuelta al mundo fue completada en 1522 por Juan Sebastián ________.'),
    ('item', '6. El texto que se leía a los indígenas exigiéndoles aceptar al rey y a la Iglesia se llamaba ________.'),
    ('item', '7. Colón llegó el 12 de octubre de 1492 a la isla de ________.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) Colón murió sabiendo que había llegado a un continente nuevo.'),
    ('item', '9. (....) Cortés conquistó Tenochtitlan con la ayuda de pueblos indígenas enemigos de los mexicas.'),
    ('item', '10. (....) La brújula fue inventada por los navegantes portugueses.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. Completá un esquema de causa y consecuencia: escribí dos causas de los viajes de exploración y dos '
             'consecuencias para los pueblos americanos.'),
    ('cuadro', ['Causas', 'Consecuencias para los pueblos americanos'], ['1.', '2.'], [5.0, 5.0]),
    ('item', '12. ¿«Descubrimiento» o «encuentro»? Escribí tu posición en 6 a 8 líneas. Se tendrá en cuenta: una posición clara '
             '(1 punto), dos argumentos con datos de la clase (2 puntos) y un texto ordenado (1 punto).', 8),
]

PLAN = {
    'material': 'Tomo: Clase 6 (Figuras 6.1 y 6.2); planisferio o globo terráqueo; la Evaluación de la Unidad 2 corregida para la devolución',
    'tema': C.TEMAS['H4a'] + ' ' + C.TEMAS['H4b'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes expliquen cómo y por qué los europeos llegaron a América y reconozcan las consecuencias '
                 'de ese proceso desde distintos puntos de vista.',
    'funciones': {
        'Esenciales': 'En clase: fuente (preguntas 1 a 3); Ubicate; actividades 1, 2, 3 y 11.',
        'Consolidación': 'Actividades 4, 5, 8 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 11).',
        'Complementarias o domiciliarias': 'Actividades 6, 7, 10 y 12.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–20', 'Devolución de la Evaluación de la Unidad 2: entrega las pruebas, explica las claves y los criterios de la Parte E, y comenta los errores más frecuentes.',
             'Revisan su prueba y anotan en qué deben mejorar.', 'Devolución de la evaluación.'),
            ('20–27', 'Pregunta: «¿Qué necesitarías para cruzar un océano sin ver la costa durante semanas?».',
             'Proponen ideas.', 'Ideas en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('27–40', 'Lectura de «Europa busca nuevas rutas» y de los avances náuticos con la Figura 6.1.',
             'Resuelven la actividad 1 y empiezan la columna de causas de la actividad 11.', 'Actividad 1 (esencial).'),
            ('40–55', 'Lectura de «Los viajes de Portugal y de Castilla» con el planisferio y la Figura 6.2.',
             'Resuelven el «Ubicate» y la actividad 2.', 'Ubicate y actividad 2 (esenciales).'),
            ('55–70', 'Lectura de la conquista y de las consecuencias, con el cuadro y el Concepto clave.',
             'Resuelven la actividad 3 y completan la actividad 11.', 'Actividades 3 y 11 (esenciales).'),
            ('70–88', 'Lectura de «La mentalidad del conquistador» y del fragmento de Colón; explica por qué lo conocemos por un resumen.',
             'Responden las preguntas 1 a 3 de la fuente.', 'Fuente (esencial).'),
            ('88–100', 'Acompaña; quien termina antes sigue con la consolidación.', 'Resuelven las actividades 4, 5, 8 y 9.',
             'Actividades de consolidación.'),
        ]),
        ('Cierre', [
            ('100–120', 'Debate breve: «¿descubrimiento o encuentro?». Retoma los errores frecuentes, lee los criterios de la actividad 12 y asigna la tarea.',
             'Dan argumentos y anotan la tarea.', 'Argumentos orales.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en la lectura del mapa: el docente traza con colores los viajes en un planisferio grande.',
        'Apoyo en la fuente: dos opciones por pregunta en la pizarra (2: «servidores» / «conquistadores»; 3: «quería conocerlos» / «pensaba en usarlos y convertirlos»).',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: averiguar qué productos americanos (papa, maíz, tomate, cacao) cambiaron la alimentación de Europa.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Lectura de mapa; análisis de fuente; esquema causa-consecuencia.',
        'instrumentos': 'Lista de cotejo con los cuatro indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Explica la función de al menos dos avances náuticos.',
                      'Distingue causas de consecuencias.',
                      'Reconoce en la fuente la intención de dominar y convertir.',
                      'Ubica los viajes de Dias, Da Gama, Colón y Magallanes-Elcano.'],
    },
    'precisiones': [
        'En 1492 no existía «España» como Estado unificado: el viaje fue de la Corona de Castilla.',
        'El fragmento de Colón se conoce por el resumen de Las Casas y está en versión modernizada: es parte del análisis.',
    ],
    'tarea': 'Actividades 6, 7, 10 y 12 de la Clase 6.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente', [
            ('F1', 'Cristóbal Colón, el 11 y 12 de octubre de 1492, al llegar a la primera isla del Caribe en su primer viaje.', ''),
            ('F2', 'Piensa que serían «buenos servidores» y que «ligeramente se harían cristianos».', 'Debe citar al menos una expresión.'),
            ('F3', 'Que el conquistador veía a los habitantes como gente que podía servirle y ser convertida, sin preguntarse por su '
                   'cultura ni por su religión. Como lo conocemos por un resumen de Las Casas, puede haber cambios o selecciones del resumidor.',
             'Se valora que relacione la fuente con la mentalidad y con su forma de transmisión.'),
        ]),
        ('Ubicate (Figura 6.2)', [
            ('U', 'Vasco da Gama navegó hacia el sur, rodeó África y llegó a la India por el este. Colón navegó hacia el oeste. '
                  'Magallanes y Elcano salieron de Castilla, cruzaron el Atlántico, el Pacífico y el Índico y volvieron al punto de partida.', ''),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'a) calcular la latitud midiendo la altura de los astros', ''),
            ('2', 'b) Vasco da Gama', ''),
            ('3', 'c) la caída de su población por epidemias y guerras', ''),
            ('4', 'd) la Corona de Castilla', ''),
        ]),
        ('Completá los espacios', [
            ('5', 'Elcano', ''),
            ('6', 'Requerimiento', ''),
            ('7', 'Guanahaní', ''),
        ]),
        ('Verdadero o falso', [
            ('8', 'Falso: murió en 1506 convencido de haber llegado a Asia.', 'Justificación obligatoria.'),
            ('9', 'Verdadero.', ''),
            ('10', 'Falso: la brújula vino de China; los europeos la adoptaron y mejoraron.', 'Justificación obligatoria.'),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'Causas: llegar a Asia por mar para comprar especias sin intermediarios; buscar oro y plata; extender la fe '
                   'cristiana. Consecuencias: conquista y trabajo forzado; caída de la población por epidemias y guerras; mestizaje.',
             'Dos causas y dos consecuencias correctas; se aceptan otras de la clase.'),
            ('12', 'Ejemplo: «Prefiero hablar de encuentro, porque América estaba habitada desde hacía miles de años, por ejemplo por '
                   'mayas, mexicas e incas. Pero no fue un encuentro pacífico: hubo conquista y la población americana cayó por las '
                   'epidemias y las guerras.» También es válida una posición a favor de «descubrimiento» desde el punto de vista europeo, si se fundamenta.',
             'Criterio anunciado en la consigna: una posición clara (1 punto), dos argumentos con datos de la clase (2 puntos) y un texto ordenado (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Fragmento del Diario de Colón (11-12 de octubre de 1492)', 'Versión modernizada de difusión escolar, transmitida por Las Casas; cotejar la literalidad con una edición crítica.'),
    ('Fechas: Constantinopla 1453; Dias 1488; Da Gama 1498; Cabral 1500; mapa de 1507 (Waldseemüller); Balboa 1513; Magallanes-Elcano 1519-1522; Requerimiento 1513', 'Fechas habituales; cotejar.'),
    ('Trazados de los viajes (Figura 6.2)', 'Recorridos aproximados de la editorial.'),
]

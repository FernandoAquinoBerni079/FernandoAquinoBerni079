"""Encuentro 15 — Clase 10: La Real Provisión de 1537 y las instituciones coloniales (H3; temas H3d y H3e).

Base: Clase 10 de la muestra 3 (commit 841f5bc9). Cambios de producción:
- A19: los dos fragmentos salen de una misma transcripción identificable
  (Rivarola Paoli), con URL, edición, localizador y fecha de consulta;
- las figuras se renumeran según el orden de lectura (10.1 línea de tiempo,
  10.2 autoridades);
- N02: el tramo de la línea de tiempo del Plan 15 se amplía y la
  consolidación pasa a la casa, con revisión al abrir el encuentro 16;
- el repaso de Mendoza y Ayolas remite a la Clase 8, que ya lo desarrolla.
"""
import curriculo as C

TITULO = 'Clase 10 — La Real Provisión de 1537 y las instituciones coloniales'
CLAVE = 'Clase 10 —'
INDICADORES = [
    'Explica en qué situación la Real Provisión de 1537 autorizaba elegir un gobernador y quiénes podían hacerlo.',
    'Diferencia la elección colonial de 1537 de una elección democrática actual.',
    'Reconoce las funciones del gobernador, el Cabildo y el Obispado, y los tipos de encomienda.',
]
URL_RIVAROLA = ('https://www.portalguarani.com/1067_juan_bautista_rivarola_paoli__/'
                '12674_la_cedula_real_del_12_de_setiembre_de_1537_por_juan_bautista_rivarola_paoli_.html')

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H3'], C.TEMAS['H3d'] + ' ' + C.TEMAS['H3e'], INDICADORES),

    ('h2', 'Una provincia lejana y sin gobernador'),
    ('p', 'En la Clase 8 viste que Pedro de Mendoza fundó Buenos Aires en 1536 y que el hambre y los enfrentamientos hicieron muy '
          'difícil la vida allí. Enfermo, Mendoza decidió volver a España en 1537 y murió durante el viaje. Antes de partir dejó '
          'como lugarteniente (su reemplazante) a Juan de Ayolas.'),
    ('p', 'Ayolas remontó el río Paraguay y entró en el Chaco en busca de las tierras de los metales. Mientras tanto, en agosto de '
          '1537, Juan de Salazar y Espinosa levantó la casa fuerte de Asunción. Ayolas murió al regresar del Chaco, pero durante '
          'meses nadie supo si seguía vivo: la provincia quedó sin una autoridad segura. Desde España, a miles de kilómetros y con '
          'meses de viaje por medio, la Corona no podía saber qué ocurría. Para ese problema dictó una norma especial.'),

    ('h2', 'Qué decía la Real Provisión de 1537'),
    ('p', 'La Real Provisión fue firmada en Valladolid el 12 de septiembre de 1537, en nombre de la reina Juana y de su hijo, '
          'el rey Carlos I. La trajo al Río de la Plata el veedor Alonso Cabrera, que llegó en 1538. Decía que, si Mendoza '
          'no había dejado lugarteniente, o si este había muerto sin nombrar a otro, los conquistadores y pobladores debían '
          'reunirse y elegir un gobernador «en nombre» del rey.'),
    ('p', 'Fijate en tres condiciones: la elección solo se hacía cuando faltaba la autoridad nombrada por el rey; elegían los '
          'conquistadores y pobladores españoles, no todos los habitantes; y el elegido gobernaba en nombre del rey, no como '
          'un gobernante independiente.'),
    ('h2', 'Después de 1537: Irala y Cabeza de Vaca'),
    ('p', 'Hacia 1539, cuando se confirmó la muerte de Ayolas, Domingo Martínez de Irala, que había sido su lugarteniente, fue '
          'reconocido como gobernador por los conquistadores reunidos en Asunción. '
          'Los historiadores discuten cómo llegó al cargo: algunos lo presentan como una aplicación de la Real Provisión y otros '
          'subrayan que se impuso con el apoyo de sus partidarios y de los oficiales reales. Por eso conviene no afirmar que hubo '
          'una «elección» en el sentido actual.'),
    ('p', 'En 1542 llegó a Asunción, por tierra desde la costa del Brasil, Álvar Núñez Cabeza de Vaca, nombrado adelantado '
          'por el rey. Sus decisiones lo enfrentaron con muchos vecinos y oficiales: en 1544 fue depuesto, apresado y enviado a '
          'España, e Irala volvió a gobernar. Más adelante, en distintos momentos del período colonial, vecinos de Asunción '
          'invocaron la Real Provisión para reclamar el derecho a designar autoridades cuando faltaban, lo que generó '
          'conflictos con gobernadores enviados por la Corona.'),
    ('fuente', 'Documento de época · Real Provisión del 12 de septiembre de 1537. Dos fragmentos tomados de una misma transcripción.',
     ['Fragmento 1: «…elijan por Gobernador en nuestro Nombre, y Capitán general de aquella provincia…»',
      'Fragmento 2 (adaptación escolar: se simplificaron la redacción y la puntuación; no es cita literal): que elijan a la '
      'persona que, según Dios y sus conciencias, les pareciere más suficiente para el cargo.',
      'Fuente: J. B. Rivarola Paoli, «La Cédula Real del 12 de setiembre de 1537», en La economía '
      'colonial, Asunción, 1986, nota 105. Reproducción digital en Portal Guaraní: ' + URL_RIVAROLA +
      ' (consulta: 14 de octubre de 2026). El texto literal del fragmento 2 puede leerse en esa fuente.'],
     'Vocabulario: «suficiente» quiere decir aquí capaz, apto. «En nuestro nombre» significa en representación del rey.',
     ['¿A quién se refiere «nuestro» en «en nuestro Nombre»?',
      '¿Qué criterio debían usar los electores para elegir a la persona?',
      '¿El elegido gobernaba por su cuenta o en representación de otro? Citá la frase que lo muestra.']),
    ('renglones', 6),

    ('fig', 'fig_10_1_linea_1534_1556.png', 'Figura 10.1 — Del viaje de Mendoza al reparto de encomiendas (1534-1556).', 11.5),
    ('caja', 'concepto', 'Concepto clave — ',
     'El programa del MEC habla del «ejercicio del derecho a la autonomía». En este caso, autonomía quiere decir que los '
     'vecinos de una provincia lejana podían resolver por sí mismos quién los gobernaría mientras faltara la autoridad nombrada '
     'por el rey. No era independencia ni democracia: seguían siendo súbditos de la Corona y solo votaban los españoles.'),

    ('h2', 'Elegir en 1537 y elegir hoy'),
    ('tabla', ['Aspecto', 'Elección prevista en 1537', 'Elección democrática actual en el Paraguay'],
     [['¿Quiénes votan?', 'Los conquistadores y pobladores españoles. No votaban los indígenas ni las mujeres.',
       'Todas las ciudadanas y los ciudadanos desde los 18 años.'],
      ['¿Cuándo se vota?', 'Solo si faltaba la autoridad nombrada por el rey.', 'En fechas fijadas por la ley, de forma periódica.'],
      ['¿En nombre de quién se gobierna?', 'En nombre del rey.', 'En representación del pueblo, según la Constitución.'],
      ['¿Cuánto dura el cargo?', 'Provisional: hasta que el rey decidiera otra cosa.', 'Un período fijo establecido por la Constitución.']],
     [2.2, 3.9, 3.9]),

    ('h2', 'Quién gobernaba: del rey al Cabildo'),
    ('p', 'El rey gobernaba sus territorios americanos con el consejo del Consejo de Indias. En América, la autoridad mayor era '
          'el virrey: desde 1542, el Paraguay formó parte del Virreinato del Perú. Más tarde, la Audiencia de Charcas, creada '
          'en 1559, funcionó como tribunal superior para la región. La provincia tenía un gobernador con sede en Asunción.'),
    ('fig', 'fig_10_2_autoridades.png', 'Figura 10.2 — Autoridades de la provincia en el siglo XVI (esquema simplificado). La encomienda no era una institución de gobierno.', 15.0),
    ('h2', 'El Cabildo: tipos e importancia'),
    ('p', 'El Cabildo de Asunción se creó en 1541. Estaba formado por alcaldes, que impartían justicia en los asuntos de la '
          'ciudad, y por regidores, que se ocupaban del gobierno local: el abastecimiento, los precios, las obras y la '
          'limpieza. Era la institución más cercana a los vecinos y muchas veces defendió sus intereses ante los gobernadores. '
          'En situaciones graves podía reunirse un cabildo abierto, con la participación de vecinos principales.'),
    ('p', 'Hubo dos tipos de cabildo: el de españoles, que gobernaba las ciudades y villas, y el cabildo de indios, que '
          'funcionaba en los pueblos indígenas con autoridades elegidas entre sus habitantes, bajo el control de funcionarios '
          'españoles.'),

    ('h2', 'El Obispado'),
    ('p', 'En 1547 se creó el Obispado del Río de la Plata, con sede en Asunción. El primer obispo nombrado no llegó a viajar; el '
          'primero que llegó a Asunción, fray Pedro Fernández de la Torre, lo hizo en 1556. El obispado '
          'organizaba la vida religiosa: las parroquias, los sacerdotes y la enseñanza de la doctrina cristiana. En la colonia, '
          'la Iglesia y la Corona estaban unidas: el rey intervenía en la elección de los obispos.'),

    ('h2', 'La encomienda: tipos y características'),
    ('p', 'La encomienda no gobernaba: era una institución que asignaba a un español, el encomendero, un grupo de indígenas '
          'que debían trabajar para él o entregarle tributo. A cambio, el encomendero debía protegerlos y enseñarles la religión. '
          'En la práctica, la encomienda fue una forma de trabajo forzado y causó abusos, enfermedades y la disminución de la '
          'población indígena. En 1556, Irala repartió encomiendas entre los españoles de Asunción.'),
    ('tabla', ['Tipo de encomienda', 'Cómo vivían los indígenas', 'Cómo trabajaban'],
     [['Originaria (de yanaconas)', 'En la casa o en la chacra del encomendero.', 'De manera permanente, para el encomendero.'],
      ['Mitaya', 'En sus propios pueblos.', 'Por turnos (la mita): una parte del año para el encomendero.']],
     [3.0, 3.5, 3.5]),
    ('caja', 'paraguay', 'En Paraguay — ',
     'En 1542, las Leyes Nuevas de Carlos I intentaron limitar los abusos de la encomienda en toda América. En el Paraguay, '
     'la encomienda siguió vigente mucho tiempo; en el siglo XVII, las Ordenanzas de Alfaro (1611) volvieron a intentar '
     'regularla. Lo vas a estudiar en la Unidad 4.'),

    ('ubicate', 'Ubicate  ·  Línea de tiempo',
     'Ubicá en la Figura 10.1 la fundación de Asunción (15 de agosto de 1537) y la firma de la Real Provisión (12 de septiembre '
     'de 1537). ¿Cuántos días las separan? ¿Podía el rey conocer la fundación de Asunción cuando firmó la provisión? Explicá por qué.'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. La Real Provisión de 1537 autorizaba elegir un gobernador cuando…'),
    ('opc', ['moría cualquier vecino de la provincia', 'faltaba el gobernador nombrado por el rey o su lugarteniente',
             'el Cabildo lo pedía cada año', 'los caciques guaraníes lo exigían']),
    ('item', '2. Según la Real Provisión, elegían al gobernador…'),
    ('opc', ['todos los habitantes de la provincia', 'solo los sacerdotes', 'los conquistadores y pobladores españoles',
             'los caciques guaraníes']),
    ('item', '3. El gobernador elegido de esa manera gobernaba…'),
    ('opc', ['en nombre del rey', 'como presidente independiente', 'en nombre del Cabildo de Buenos Aires',
             'por un período fijo de cuatro años']),
    ('item', '4. En la encomienda originaria, los indígenas…'),
    ('opc', ['vivían en sus pueblos y trabajaban por turnos', 'elegían a sus encomenderos', 'quedaban libres de todo trabajo',
             'vivían en la casa o la chacra del encomendero']),
    ('item', '5. El Obispado del Río de la Plata, con sede en Asunción, se creó en…'),
    ('opc', ['1537', '1541', '1547', '1556']),
    ('item', '6. El adelantado que llegó por tierra en 1542 y fue depuesto en 1544 fue…'),
    ('opc', ['Domingo Martínez de Irala', 'Álvar Núñez Cabeza de Vaca', 'Juan de Ayolas', 'Pedro de Mendoza']),
    ('item', '7. Ordená del 1 al 6, del más antiguo al más reciente, escribiendo el número en el paréntesis:'),
    ('lista_orden', ['Cabeza de Vaca es depuesto', 'Fundación de Asunción', 'Reparto de encomiendas de Irala',
                     'Fundación de Buenos Aires', 'Creación del Cabildo de Asunción', 'Firma de la Real Provisión']),
    ('consigna', 'Completá los espacios:'),
    ('item', '8. El cabildo de ________ gobernaba las ciudades; el cabildo de ________ funcionaba en los pueblos indígenas.'),
    ('item', '9. Los indígenas ________ vivían en sus pueblos y trabajaban por turnos para el encomendero.'),
    ('item', '10. En el Cabildo, los ________ impartían justicia y los ________ se ocupaban del gobierno de la ciudad.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '11. (....) La Real Provisión estableció elecciones periódicas para todos los habitantes de la provincia.'),
    ('item', '12. (....) Cuando se firmó la Real Provisión, en España todavía no se sabía de la fundación de Asunción.'),
    ('item', '13. (....) La encomienda era una institución de gobierno de la ciudad.'),
    ('item', '14. (....) Las Leyes Nuevas de 1542 buscaron limitar los abusos de la encomienda.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '15. ¿Por qué el programa llama a la Real Provisión «ejercicio del derecho a la autonomía»? Explicá qué podían decidir los vecinos de Asunción y cuáles eran los límites de esa autonomía (nombrá al menos dos límites).', 5),
    ('item', '16. ¿Fue la encomienda una forma de protección o de explotación de los indígenas? Respondé en un párrafo de 6 a 8 líneas, con dos datos de esta clase. Se tendrá en cuenta: que tu posición sea clara (1 punto), que uses dos datos correctos de la clase (2 puntos) y que el párrafo esté ordenado (1 punto).', 8),
    ('h3', 'Autoevaluación de la clase'),
    ('tabla', ['Puedo…', 'Sí', 'Con ayuda', 'Todavía no'],
     [['Explicar en qué situación la Real Provisión permitía elegir un gobernador y quiénes votaban.', '', '', ''],
      ['Señalar dos diferencias entre la elección de 1537 y una elección actual.', '', '', ''],
      ['Distinguir el Cabildo y el Obispado de la encomienda.', '', '', ''],
      ['Explicar los dos tipos de encomienda.', '', '', ''],
      ['Ubicar en la línea de tiempo los hechos de 1534 a 1556.', '', '', '']],
     [5.5, 1.5, 1.5, 1.5]),
]

PLAN = {
    'material': 'Tomo: Clase 10 (Figuras 10.1 y 10.2); planisferio o mapamundi del aula (para la distancia entre España y el Río de la Plata)',
    'tema': C.TEMAS['H3d'] + ' ' + C.TEMAS['H3e'],
    'indicadores': INDICADORES,
    'proposito': 'Que lean un documento de época, entiendan qué autonomía tenían los vecinos de Asunción y sus límites, y distingan el gobierno de la encomienda.',
    'funciones': {
        'Esenciales': 'En clase: fuente (preguntas 1 a 3); Ubicate; actividades 1, 2, 3, 4, 7, 13 y 15.',
        'Consolidación': 'Actividades 5, 8, 9 y 10, en casa, con revisión breve al abrir el encuentro 16.',
        'Complementarias o domiciliarias': 'Actividades 6, 11, 12 y 14 (repaso breve), actividad 16 (párrafo) y autoevaluación de la clase.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 9. Plantea un problema: «Si la dirección de la escuela queda vacía y no llega nadie de afuera, ¿quién decide? ¿Con qué límites?».',
             'Proponen respuestas y discuten los límites de esa decisión.', 'Ideas en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–23', 'Lectura guiada de «Una provincia lejana y sin gobernador». Muestra en el planisferio la distancia entre España, Buenos Aires y Asunción.',
             'En parejas escriben en dos líneas cuál era el problema de la provincia en 1537.', 'Problema escrito.'),
            ('23–33', 'Lectura de «Qué decía la Real Provisión» y de «Después de 1537»: destaca las tres condiciones y explica que los historiadores discuten cómo llegó Irala al cargo.',
             'Subrayan las tres condiciones de la provisión.', 'Texto subrayado.'),
            ('33–48', 'Lee en voz alta los dos fragmentos de «Trabajá con la fuente», explica el vocabulario y muestra cómo se lee la referencia de la fuente.',
             'Responden individualmente las preguntas 1 a 3 de la fuente, en los renglones del recuadro.', 'Fuente (esencial).'),
            ('48–60', 'Presenta la Figura 10.1 (línea de tiempo) y modela cómo contar los días entre dos fechas.',
             'Resuelven el «Ubicate» y la actividad 7 (ordenar hechos).', 'Ubicate y actividad 7 (esenciales).'),
            ('60–76', 'Organiza grupos de 4 para analizar el cuadro «Elegir en 1537 y elegir hoy» y lee el Concepto clave sobre autonomía.',
             'Cada grupo escribe en el cuaderno una fila nueva para el cuadro y resuelve las actividades 1, 2 y 3.', 'Fila agregada; actividades 1 a 3 (esenciales).'),
            ('76–96', 'Explica las autoridades con la Figura 10.2, el Cabildo (tipos), el Obispado y la encomienda (tipos).',
             'Resuelven las actividades 4 y 13.', 'Actividades 4 y 13 (esenciales).'),
        ]),
        ('Cierre', [
            ('96–110', 'Retoma solo los errores frecuentes de las esenciales, que se comprobaron por parejas al cerrar cada bloque.',
             'Corrigen con otro color lo que haga falta.', 'Errores frecuentes corregidos.'),
            ('110–120', 'Boleto de salida con la actividad 15. Asigna la consolidación y la tarea, y lee los criterios de la actividad 16.',
             'Escriben la actividad 15 y la entregan.', 'Actividad 15 (esencial).'),
        ]),
    ],
    'diversidad': [
        'Apoyo para la lectura: el docente lee los fragmentos en voz alta y deja un glosario en la pizarra (capitulación, adelantado, cabildo, encomienda, mita, yanacona).',
        'Apoyo en la fuente: las preguntas 1 a 3 pueden responderse eligiendo entre dos opciones escritas en la pizarra (1: al rey / a los vecinos; 2: que fuera el más capaz / que fuera el más rico; 3: por su cuenta / en nombre del rey), con la misma exigencia de citar la frase.',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: comparar cómo llegó Irala al gobierno en 1539 y en 1544, y por qué los historiadores no coinciden.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Análisis de fuente; cuadro comparativo; ordenamiento cronológico; boleto de salida.',
        'instrumentos': 'Lista de cotejo con los tres criterios; actividad 16 con los criterios de su consigna.',
        'criterios': [
            'Nombra las tres condiciones de la Real Provisión: falta de autoridad, electores españoles y gobierno en nombre del rey.',
            'Señala al menos dos diferencias entre la elección de 1537 y una elección actual.',
            'Distingue las instituciones de gobierno (gobernador, Cabildo) de la encomienda y explica sus dos tipos.',
        ],
    },
    'precisiones': [
        'El programa del MEC dice «Ejercicio del derecho a la autonomía»; el tomo lo explica en el Concepto clave. No presentarlo como democracia ni como independencia.',
        'Los dos fragmentos vienen de la transcripción de Rivarola Paoli; el segundo es una adaptación escolar declarada en el tomo (no es cita literal). Sobre 1539, el tomo presenta el debate sin tomar partido: no afirmar que hubo una elección.',
    ],
    'tarea': 'Consolidación (actividades 5, 8, 9 y 10), actividades 6, 11, 12 y 14 (repaso breve) y actividad 16 (párrafo con los criterios de la consigna).',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente', [
            ('F1', 'Al rey: «nuestro» es la forma en que el rey habla de sí mismo en los documentos oficiales.', ''),
            ('F2', 'Elegir a la persona que, «según Dios y sus conciencias», pareciera más capaz («suficiente») para el cargo.', 'Debe citar o parafrasear la expresión del documento.'),
            ('F3', 'En representación del rey: «elijan por Gobernador en nuestro Nombre».', 'Sin la cita, la respuesta es parcial.'),
        ]),
        ('Ubicate (Figura 10.1)', [
            ('U', 'Las separan 28 días. No: el rey firmó la provisión en España sin saber que Asunción se había fundado, porque las noticias tardaban meses en cruzar el océano.',
             'Se acepta 27 o 28 días si explica cómo contó. Lo esencial es la segunda parte.'),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'b) faltaba el gobernador nombrado por el rey o su lugarteniente', ''),
            ('2', 'c) los conquistadores y pobladores españoles', ''),
            ('3', 'a) en nombre del rey', ''),
            ('4', 'd) vivían en la casa o la chacra del encomendero', ''),
            ('5', 'c) 1547', ''),
            ('6', 'b) Álvar Núñez Cabeza de Vaca', 'Antes de su llegada, hacia 1539, Irala había quedado al frente de la provincia; si un estudiante lo menciona, no se lo considera error.'),
        ]),
        ('Ordená', [
            ('7', 'Orden: 1 Fundación de Buenos Aires (1536); 2 Fundación de Asunción (agosto de 1537); 3 Firma de la Real Provisión (septiembre de 1537); 4 Creación del Cabildo de Asunción (1541); 5 Cabeza de Vaca es depuesto (1544); 6 Reparto de encomiendas de Irala (1556).',
             'En el paréntesis de cada hecho: Cabeza de Vaca 5; Asunción 2; Reparto 6; Buenos Aires 1; Cabildo 4; Real Provisión 3.'),
        ]),
        ('Completá los espacios', [
            ('8', 'españoles / indios', ''),
            ('9', 'mitayos', ''),
            ('10', 'alcaldes / regidores', ''),
        ]),
        ('Verdadero o falso', [
            ('11', 'Falso: solo autorizaba una elección cuando faltaba la autoridad, y votaban los conquistadores y pobladores españoles.', 'Justificación obligatoria.'),
            ('12', 'Verdadero.', ''),
            ('13', 'Falso: la encomienda asignaba trabajo indígena a un español; el gobierno de la ciudad era tarea del Cabildo.', 'Justificación obligatoria.'),
            ('14', 'Verdadero.', ''),
        ]),
        ('Respondé y fundamentá', [
            ('15', 'Porque los vecinos de una provincia lejana podían elegir por sí mismos un gobernador cuando faltaba la autoridad nombrada por el rey. Límites: solo en caso de vacancia, solo votaban los españoles y el elegido gobernaba en nombre del rey, de manera provisional.',
             'Lo que pide la consigna: qué podían decidir y al menos dos límites. Completo: ambos aspectos. Parcial: solo uno. No se acepta «era una democracia».'),
            ('16', 'Respuesta argumentativa. Se espera que reconozca que la encomienda se presentaba como protección y evangelización, pero en la práctica fue trabajo forzado, con abusos y disminución de la población; puede usar como datos los tipos de encomienda, el reparto de 1556 o las Leyes Nuevas de 1542.',
             'Criterio anunciado en la consigna (4 puntos): que tu posición sea clara (1 punto), que uses dos datos correctos de la clase (2 puntos) y que el párrafo esté ordenado (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Fragmentos de la Real Provisión (A19)', 'Los dos se toman de la transcripción de Rivarola Paoli (La economía colonial, 1986, nota 105), '
     'según su reproducción en Portal Guaraní (URL en el tomo). La página no se abre desde el entorno de edición. Corrección del 15/10/2026: '
     'la revisión de Fernando, con acceso directo a la fuente, comprobó que la versión anterior del segundo fragmento no la reproducía '
     'exactamente (la fuente escribe «más suficiente», con tilde, y difiere en redacción y puntuación). Como la grafía literal no puede '
     'cotejarse desde aquí, el fragmento 2 se presenta como adaptación escolar declarada, sin comillas de cita. El fragmento 1 no fue '
     'objetado en esa revisión; su cotejo literal queda a cargo de la auditoría. Transcripción concordante: portal del MEC, '
     'https://www.mec.gov.py/cms_v2/recursos/4844-la-cedula-real-del-12-de-septiembre-de-1537-llega-al-paraguay (tampoco accesible desde el entorno).'),
    ('Muerte de Mendoza en el viaje de regreso (1537); llegada de Alonso Cabrera (1538); Irala hacia 1539 y el debate sobre la aplicación de la provisión',
     'Contrastar con ISEPOL, Síntesis de Geografía e Historia (2024) y el estudio publicado por el CEHJ, señalados por la auditoría.'),
    ('Cabildo 1541; Obispado 1547 y primer obispo en 1556; Audiencia de Charcas 1559; Virreinato del Perú 1542', 'Fechas de manual; cotejar.'),
    ('Tipos de encomienda y reparto de 1556; Leyes Nuevas 1542; Ordenanzas de Alfaro 1611', 'Bibliografía paraguaya habitual; cotejar.'),
]

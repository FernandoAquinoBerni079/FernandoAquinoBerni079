"""Encuentro 12 — Clase 8: La conquista del Río de la Plata y la fundación de Asunción (H3; temas H3a y H3b).

Corrige el maestro: explica la fundación sin omitir a Mendoza, Ayolas e Irala;
agrega el Cabildo de 1541 y el abandono de Buenos Aires.
"""
import curriculo as C

TITULO = 'Clase 8 — La conquista del Río de la Plata y la fundación de Asunción'
CLAVE = 'Clase 8 —'
INDICADORES = [
    'Explica la trascendencia de las expediciones de Alejo García y de Sebastián Gaboto.',
    'Ordena en el tiempo y ubica en el mapa las expediciones al Río de la Plata.',
    'Describe las características de la conquista en el Río de la Plata.',
    'Explica por qué Asunción se convirtió en el centro de la conquista.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H3'], C.TEMAS['H3a'] + ' ' + C.TEMAS['H3b'], INDICADORES),

    ('h2', 'Un río que prometía plata'),
    ('p', 'En 1516, el navegante Juan Díaz de Solís, al servicio de Castilla, entró en un enorme estuario buscando un paso hacia '
          'el océano Pacífico. Murió en la costa al enfrentarse con sus habitantes. Al volver, uno de los barcos de la expedición '
          'naufragó cerca de la isla de Santa Catalina, en la costa del actual Brasil, y algunos sobrevivientes se quedaron a vivir '
          'con los guaraníes de la región. Entre ellos estaba Alejo García.'),

    ('h2', 'Alejo García: el primer europeo en el territorio paraguayo'),
    ('p', 'Los guaraníes de la costa hablaban de tierras al oeste donde había metales. Hacia 1524, Alejo García partió de la costa '
          'atlántica acompañado por muchos guaraníes, atravesó la región del Guairá, cruzó el río Paraguay y llegó hasta la '
          'frontera del Imperio inca, en la región de Charcas. Volvió con objetos de plata, pero fue muerto en el regreso, cerca '
          'del río Paraguay.'),
    ('p', 'Su viaje tuvo una gran trascendencia: fue el primer europeo que recorrió el territorio paraguayo, demostró que había un '
          'camino desde el Atlántico hasta las tierras de la plata y dio origen a la leyenda de la «Sierra de la Plata» y del '
          '«Rey Blanco», que atrajo a otras expediciones. El estuario de Solís pasó a llamarse Río de la Plata.'),

    ('h2', 'Sebastián Gaboto y el primer fuerte'),
    ('p', 'En 1526, Sebastián Gaboto salió de España hacia las islas de las especias, en Asia. Al llegar a la costa del Brasil '
          'supo de la plata y cambió su rumbo. Entró al Río de la Plata y en 1527 levantó el fuerte de Sancti Spiritus, junto al '
          'río Paraná, el primer establecimiento español en la región. Remontó el Paraná y el Paraguay, pero en 1529 el fuerte fue '
          'destruido por los indígenas y en 1530 Gaboto volvió a España. Su expedición dio a conocer los grandes ríos de la cuenca '
          'del Plata.'),

    ('h2', 'Pedro de Mendoza y la fundación de Asunción'),
    ('p', 'En 1534, el rey firmó una capitulación con Pedro de Mendoza, que llegó con una gran expedición y fundó Buenos Aires a '
          'comienzos de 1536. El hambre y los enfrentamientos con los pueblos del lugar hicieron muy difícil la vida allí. Mendoza '
          'envió río arriba a Juan de Ayolas en busca de la Sierra de la Plata. Ayolas remontó el Paraguay, fundó el puerto de '
          'Candelaria y se internó en el Chaco hacia el oeste.'),
    ('p', 'Juan de Salazar y Espinosa, que había subido el río en busca de Ayolas, levantó en agosto de 1537 una casa fuerte en la '
          'orilla del río Paraguay, en tierra de los guaraníes carios: así nació Asunción, cuya fundación se recuerda el 15 de '
          'agosto. Ayolas murió al regresar del Chaco. Domingo Martínez de Irala, que había quedado a cargo de Candelaria, quedó '
          'hacia 1539 al frente de la provincia.'),

    ('fig', 'fig_8_1_rutas_plata.png', 'Figura 8.1 — Expediciones al Río de la Plata y al Paraguay, 1516-1537 (recorridos aproximados).', 12.0),
    ('h2', 'Asunción, centro de la conquista'),
    ('p', 'En 1541, Irala ordenó despoblar Buenos Aires y concentrar a todos los españoles en Asunción, donde ese mismo año se '
          'formó el Cabildo. ¿Por qué Asunción? Tenía alimentos gracias a la agricultura guaraní, estaba más cerca del camino hacia '
          'las tierras de la plata y contaba con la alianza de los carios, que entregaban alimentos, trabajo y mujeres a los españoles '
          'según sus costumbres de parentesco. Esa alianza, desigual y llena de abusos, es la base del mestizaje que vas a estudiar '
          'en la Clase 9.'),
    ('p', 'Desde Asunción partieron expediciones que fundaron muchas ciudades: por eso se la llama «madre de ciudades». Entre ellas, '
          'Santa Cruz de la Sierra (1561), Santa Fe (1573) y la segunda fundación de Buenos Aires (1580), hecha por Juan de Garay.'),
    ('fig', 'fig_8_2_linea_1516_1541.png', 'Figura 8.2 — Del viaje de Solís a la creación del Cabildo de Asunción (1516-1541).', 11.5),
    ('caja', 'concepto', 'Concepto clave — ',
     'La conquista del Río de la Plata fue distinta de la de México y del Perú: no había un gran imperio con ciudades y metales '
     'para conquistar. Los españoles eran pocos, estaban aislados y dependían de la alianza con los guaraníes para sobrevivir.'),

    ('fuente', 'Fuente secundaria · Ciudades fundadas por expediciones salidas de Asunción en el siglo XVI (síntesis de la bibliografía histórica)',
     ['Ciudad Real del Guairá (1557) · Santa Cruz de la Sierra (1561) · Villa Rica del Espíritu Santo (1570) · Santa Fe (1573) · '
      'Buenos Aires, segunda fundación (1580) · Concepción del Bermejo (1585) · San Juan de Vera de las Siete Corrientes (1588).'],
     '',
     ['¿Cuántos años pasaron entre la fundación de Asunción y la segunda fundación de Buenos Aires?',
      '¿Por qué se dice que Asunción fue «madre de ciudades»?',
      '¿Qué indica esta lista sobre el lugar que ocupaba Asunción en la conquista del Río de la Plata?']),
    ('renglones', 5),
    ('ubicate', 'Ubicate  ·  Mapa (Figura 8.1)',
     'Seguí el recorrido de Alejo García desde la isla de Santa Catalina hasta Charcas. ¿Qué ríos cruzó? Ubicá Sancti Spiritus, '
     'Buenos Aires y Asunción. ¿Cuál quedaba más cerca del camino a las tierras de la plata?'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. Alejo García fue importante porque…'),
    ('opc', ['fundó Asunción en 1537', 'fue el primer europeo que recorrió el territorio paraguayo',
             'firmó el Tratado de Tordesillas', 'conquistó el Imperio inca']),
    ('item', '2. El fuerte de Sancti Spiritus (1527) fue levantado por…'),
    ('opc', ['Pedro de Mendoza', 'Juan de Ayolas', 'Sebastián Gaboto', 'Domingo Martínez de Irala']),
    ('item', '3. En 1541, Irala ordenó…'),
    ('opc', ['despoblar Buenos Aires y concentrar a los españoles en Asunción', 'fundar Santa Fe', 'volver a España',
             'atacar a los carios']),
    ('item', '4. Una característica de la conquista en el Río de la Plata fue que…'),
    ('opc', ['los españoles encontraron un gran imperio rico en oro', 'llegaron miles de colonos europeos cada año',
             'no hubo contacto con los pueblos indígenas', 'los españoles dependían de la alianza con los guaraníes']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. El navegante que entró en 1516 al estuario del Río de la Plata fue Juan Díaz de ________.'),
    ('item', '6. La casa fuerte que dio origen a Asunción fue levantada por Juan de Salazar y ________.'),
    ('item', '7. La leyenda de la «Sierra de la ________» atrajo a varias expediciones.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) Buenos Aires fue fundada por primera vez por Pedro de Mendoza a comienzos de 1536.'),
    ('item', '9. (....) El Cabildo de Asunción se creó en 1541.'),
    ('item', '10. (....) Asunción fue fundada por Alejo García.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. ¿Por qué Asunción se convirtió en el centro de la conquista del Río de la Plata y no Buenos Aires? Nombrá dos '
             'razones.', 4),
    ('item', '12. Escribí un breve texto (6 a 8 líneas) sobre la trascendencia de la expedición de Alejo García. Se tendrá en '
             'cuenta: qué recorrido hizo (1 punto), dos consecuencias de su viaje (2 puntos) y un texto ordenado (1 punto).', 8),
]

PLAN = {
    'material': 'Tomo: Clase 8 (Figuras 8.1 y 8.2); mapa de América del Sur',
    'tema': C.TEMAS['H3a'] + ' ' + C.TEMAS['H3b'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes reconstruyan cómo llegaron los europeos al Río de la Plata y expliquen por qué Asunción '
                 'fue el centro de la conquista.',
    'funciones': {
        'Esenciales': 'En clase: Ubicate; fuente (preguntas 1 a 3); actividades 1, 2, 3, 4 y 11.',
        'Consolidación': 'Actividades 5, 6, 8 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 13).',
        'Complementarias o domiciliarias': 'Actividades 7, 10 y 12.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 7. Pregunta: «¿Por qué el río se llama de la Plata si casi no tiene plata?».',
             'Proponen hipótesis.', 'Hipótesis en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–30', 'Lectura de Solís, Alejo García y Gaboto con la Figura 8.1.',
             'Resuelven el «Ubicate» y las actividades 1 y 2.', 'Ubicate y actividades 1 y 2 (esenciales).'),
            ('30–50', 'Lectura de «Pedro de Mendoza y la fundación de Asunción» con la Figura 8.2.',
             'Resuelven la actividad 3.', 'Actividad 3 (esencial).'),
            ('50–68', 'Lectura de «Asunción, centro de la conquista» y del Concepto clave.',
             'Resuelven las actividades 4 y 11.', 'Actividades 4 y 11 (esenciales).'),
            ('68–85', 'Presenta la lista de ciudades y aclara que es una fuente secundaria.',
             'Responden las preguntas 1 a 3 de la fuente.', 'Fuente (esencial).'),
            ('85–100', 'Acompaña; quien termina antes sigue con la consolidación.', 'Resuelven las actividades 5, 6, 8 y 9.',
             'Actividades de consolidación.'),
        ]),
        ('Cierre', [
            ('100–120', 'Puesta en común de la actividad 11; retoma errores (quién fundó Asunción, fechas). Lee los criterios de la actividad 12 y asigna la tarea.',
             'Corrigen con otro color.', 'Actividad 11 revisada.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en el mapa: el docente traza con tiza de colores cada recorrido en un mapa grande, en el mismo orden de la Figura 8.2.',
        'Apoyo en la escritura de la actividad 11: comienzo dado «Asunción fue el centro porque…».',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: averiguar quiénes fueron los payaguáes y qué papel tuvieron en la muerte de Ayolas.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Lectura de mapa y de línea de tiempo; análisis de fuente secundaria; respuesta breve.',
        'instrumentos': 'Lista de cotejo con los cuatro indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Explica la importancia de García y de Gaboto.',
                      'Ordena las expediciones de 1516 a 1541.',
                      'Caracteriza la conquista del Río de la Plata.',
                      'Da dos razones de la centralidad de Asunción.'],
    },
    'precisiones': [
        'Las fechas del viaje de Alejo García son aproximadas (hacia 1524-1525).',
        'Asunción no tiene un acta de fundación conservada: se recuerda el 15 de agosto de 1537 por la casa fuerte de Salazar y Espinosa.',
    ],
    'tarea': 'Actividades 7, 10 y 12 de la Clase 8.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente', [
            ('F1', '43 años (de 1537 a 1580).', ''),
            ('F2', 'Porque desde allí partieron las expediciones que fundaron muchas otras ciudades de la región.', ''),
            ('F3', 'Que Asunción era la base de la conquista: allí estaban los españoles, los recursos y las alianzas para fundar nuevas ciudades.', ''),
        ]),
        ('Ubicate (Figura 8.1)', [
            ('U', 'Cruzó el Paraná (y otros ríos de la región del Guairá) y el río Paraguay. Asunción quedaba más cerca del camino '
                  'hacia Charcas, la tierra de la plata.', 'Se aceptan los ríos que el estudiante identifique en el mapa si son correctos.'),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'b) fue el primer europeo que recorrió el territorio paraguayo', ''),
            ('2', 'c) Sebastián Gaboto', ''),
            ('3', 'a) despoblar Buenos Aires y concentrar a los españoles en Asunción', ''),
            ('4', 'd) los españoles dependían de la alianza con los guaraníes', ''),
        ]),
        ('Completá los espacios', [
            ('5', 'Solís', ''),
            ('6', 'Espinosa', ''),
            ('7', 'Plata', ''),
        ]),
        ('Verdadero o falso', [
            ('8', 'Verdadero.', ''),
            ('9', 'Verdadero.', ''),
            ('10', 'Falso: la casa fuerte de Asunción la levantó Juan de Salazar y Espinosa en 1537; García había muerto antes.', 'Justificación obligatoria.'),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'Porque tenía alimentos gracias a la agricultura guaraní; porque contaba con la alianza de los carios; porque estaba '
                   'más cerca del camino a las tierras de la plata. En Buenos Aires había hambre y enfrentamientos.', 'Dos razones correctas.'),
            ('12', 'Ejemplo: «Hacia 1524, Alejo García salió de la costa del Brasil con muchos guaraníes, cruzó el Paraguay y llegó a la '
                   'frontera inca. Fue el primer europeo en recorrer el territorio paraguayo. Su viaje mostró el camino a la plata y '
                   'creó la leyenda de la Sierra de la Plata, que atrajo a Gaboto y a Mendoza.»',
             'Criterio anunciado en la consigna: qué recorrido hizo (1 punto), dos consecuencias de su viaje (2 puntos) y un texto ordenado (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Solís 1516; García hacia 1524; Sancti Spiritus 1527 y su destrucción en 1529; capitulación de Mendoza 1534; Buenos Aires 1536; Asunción 1537; Cabildo 1541', 'Fechas habituales; cotejar (Peña Villamil, citado por la auditoría, para 1539-1541).'),
    ('Ciudades fundadas desde Asunción y sus fechas', 'Síntesis de la bibliografía; cotejar cada fecha.'),
    ('Recorridos de la Figura 8.1', 'Trazados aproximados de la editorial.'),
]

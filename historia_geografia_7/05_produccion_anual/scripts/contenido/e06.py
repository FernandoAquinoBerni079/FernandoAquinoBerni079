"""Encuentro 6 — Clase 4: El poblamiento de América (H2; tema H2a).

Los primeros 20 minutos se reservan para la devolución de la Evaluación de la
Unidad 1 (regla de equidad A10); la clase dispone de 100 minutos.
"""
import curriculo as C

TITULO = 'Clase 4 — El poblamiento de América'
CLAVE = 'Clase 4 —'
INDICADORES = [
    'Explica por qué se sabe que los primeros americanos llegaron desde Asia y cuándo, aproximadamente.',
    'Compara las teorías clásicas sobre el origen del hombre americano con lo que se sabe hoy.',
    'Interpreta datos arqueológicos y reconoce que algunos siguen en debate.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H2'], C.TEMAS['H2a'], INDICADORES),

    ('h2', 'El último continente habitado'),
    ('p', 'Los seres humanos modernos (Homo sapiens) surgieron en África hace unos 300.000 años y desde allí se expandieron por el '
          'mundo. América fue el último de los continentes habitados en ser poblado, sin contar la Antártida, que nunca tuvo '
          'población permanente. No hubo una evolución humana propia de América: no se encontraron allí restos de especies humanas '
          'anteriores, como sí ocurrió en África, Asia y Europa.'),
    ('p', 'Durante la última glaciación, gran parte del agua del planeta estaba congelada en enormes capas de hielo y el nivel del '
          'mar era mucho más bajo que hoy. Entre Siberia y Alaska quedó al descubierto una amplia franja de tierra, llamada '
          'Beringia, por donde pudieron pasar animales y grupos humanos desde Asia (Figura 4.1).'),

    ('h2', 'Las teorías clásicas'),
    ('p', 'Desde fines del siglo XIX, varios científicos propusieron teorías para explicar el origen del hombre americano. Con los '
          'datos de su época, llegaron a conclusiones distintas:'),
    ('tabla', ['Teoría', 'Autor y época', 'Qué proponía', 'Qué se sabe hoy'],
     [['Autoctonista', 'Florentino Ameghino (Argentina, fines del siglo XIX)', 'Que la humanidad se originó en América, en la llanura pampeana.',
       'Descartada: no hay restos de especies humanas anteriores en América.'],
      ['Asiática', 'Aleš Hrdlička (Estados Unidos, principios del siglo XX)', 'Un único origen: grupos de Asia que cruzaron por el estrecho de Bering.',
       'Su idea central se confirmó: el origen principal es asiático.'],
      ['Oceánica', 'Paul Rivet (Francia, primera mitad del siglo XX)', 'Varios orígenes: además de Asia, navegantes de Melanesia y Polinesia por el Pacífico.',
       'No hay pruebas de migraciones oceánicas que poblaran América.'],
      ['Australiana', 'António Mendes Correia (Portugal, primera mitad del siglo XX)', 'Una llegada desde Australia por la Antártida hasta el extremo sur.',
       'Descartada: la Antártida no pudo atravesarse.']],
     [1.6, 2.6, 3.0, 2.8]),

    ('h2', 'Lo que se sabe hoy'),
    ('p', 'Hoy se combinan varias clases de pruebas: los restos arqueológicos, la genética (el ADN de poblaciones antiguas y '
          'actuales) y la geología, que reconstruye cómo eran las costas y los hielos. Las investigaciones coinciden en que los '
          'antepasados de los pueblos originarios americanos vinieron del nordeste de Asia, cruzando Beringia.'),
    ('p', 'Durante mucho tiempo se creyó que los primeros fueron los cazadores de la cultura Clovis, en América del Norte, hace unos '
          '13.000 años. Pero en Monte Verde, al sur de Chile, se hallaron restos de un campamento de unos 14.500 años, y en 1997 '
          'un grupo de especialistas aceptó esa antigüedad. Hoy la mayoría acepta que hubo poblamiento anterior a Clovis. Lo que '
          'sigue en debate es cuánto antes llegaron y por qué rutas: algunos proponen una ruta por la costa del Pacífico, en '
          'canoas o caminando por la orilla, y otros un corredor por el interior, entre los hielos. Huellas humanas halladas en '
          'White Sands (Estados Unidos), fechadas en más de 20.000 años, todavía se discuten.'),
    ('fig', 'fig_4_1_poblamiento.png', 'Figura 4.1 — Rutas propuestas para el poblamiento de América y algunos sitios arqueológicos (esquema).', 12.0),
    ('caja', 'concepto', 'Concepto clave — ',
     'Una teoría científica es una explicación basada en pruebas, que puede cambiar cuando aparecen nuevos datos. Por eso '
     'Clovis dejó de ser «la primera cultura» cuando se aceptó la antigüedad de Monte Verde.'),
    ('caja', 'paraguay', 'En Paraguay — ',
     'Los grupos que llegaron a la cuenca del Paraná y del Paraguay hace miles de años (Clase 2) eran descendientes de aquellos '
     'primeros pobladores que, a lo largo de muchas generaciones, se fueron extendiendo hasta el extremo sur del continente.'),

    ('fuente', 'Fuente científica · Algunos sitios arqueológicos de América y su antigüedad aproximada (síntesis de publicaciones '
               'científicas; las fechas son las de uso más frecuente)',
     ['Monte Verde (sur de Chile): restos de un campamento con viviendas, plantas y huesos de animales; unos 14.500 años. '
      'Investigaciones de Tom Dillehay; antigüedad aceptada por un grupo de especialistas en 1997.',
      'Clovis (Nuevo México, Estados Unidos): puntas de piedra acanaladas para cazar grandes animales; unos 13.000 años.',
      'Cueva Fell (Patagonia chilena): herramientas y restos de animales extinguidos; más de 11.000 años.',
      'White Sands (Nuevo México, Estados Unidos): huellas humanas fechadas en 21.000 a 23.000 años (publicado en 2021; '
      'la fecha sigue en discusión).'],
     '',
     ['Ordená los cuatro sitios del más antiguo al más reciente.',
      '¿Qué sitio hizo dudar de que Clovis fuera la primera cultura de América? ¿Por qué?',
      '¿Por qué los científicos todavía discuten la fecha de White Sands? Pensá qué haría falta para aceptarla.']),
    ('renglones', 6),
    ('ubicate', 'Ubicate  ·  Mapa (Figura 4.1)',
     'Ubicá Beringia y Monte Verde. ¿En qué dirección general avanzó el poblamiento? ¿Por qué Monte Verde, en el extremo sur, '
     'es una prueba importante sobre la antigüedad del poblamiento?'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. Beringia era…'),
    ('opc', ['una isla del océano Pacífico', 'una franja de tierra entre Siberia y Alaska que quedó al descubierto en la glaciación',
             'el nombre de la primera aldea de América', 'una cordillera de América del Sur']),
    ('item', '2. La teoría de Florentino Ameghino sostenía que la humanidad…'),
    ('opc', ['llegó desde Australia', 'llegó por el océano Pacífico', 'se originó en América', 'llegó desde Europa por el Atlántico']),
    ('item', '3. Hoy la mayoría de los especialistas acepta que…'),
    ('opc', ['la cultura Clovis fue la primera de América', 'América se pobló desde Australia', 'no hubo cazadores en América',
             'hubo poblamiento anterior a Clovis']),
    ('item', '4. Monte Verde se encuentra en…'),
    ('opc', ['el sur de Chile', 'Alaska', 'el Paraguay', 'México']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. Los seres humanos modernos surgieron en el continente de ________.'),
    ('item', '6. Durante la glaciación, el nivel del mar era más ________ que hoy.'),
    ('item', '7. El científico que propuso un único origen asiático fue ________.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) En América se encontraron restos de especies humanas anteriores al Homo sapiens.'),
    ('item', '9. (....) La genética ayuda a saber de dónde vinieron los primeros americanos.'),
    ('item', '10. (....) La fecha de las huellas de White Sands está aceptada por todos los especialistas.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. ¿Qué parte de la teoría de Hrdlička se confirmó y qué cambió con los nuevos descubrimientos?', 4),
    ('item', '12. Explicá por qué una teoría científica puede cambiar. Usá el caso de Clovis y Monte Verde como ejemplo. '
             'Se tendrá en cuenta: qué se creía antes (1 punto), qué dato nuevo apareció (1 punto) y qué se acepta hoy (1 punto).', 5),
]

PLAN = {
    'material': 'Tomo: Clase 4 (Figura 4.1); un planisferio o globo terráqueo; la Evaluación de la Unidad 1 corregida para la devolución',
    'tema': C.TEMAS['H2a'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes expliquen el origen asiático del poblamiento americano con pruebas actuales y comprendan '
                 'cómo cambian las teorías científicas.',
    'funciones': {
        'Esenciales': 'En clase: fuente (preguntas 1 a 3); Ubicate; actividades 1, 2, 3, 8 y 12.',
        'Consolidación': 'Actividades 4, 5, 6 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 7).',
        'Complementarias o domiciliarias': 'Actividades 7, 10 y 11.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–20', 'Devolución de la Evaluación de la Unidad 1: entrega las pruebas, explica las claves y los criterios de la Parte E, y comenta los errores más frecuentes.',
             'Revisan su prueba y anotan en qué deben mejorar.', 'Devolución de la evaluación.'),
            ('20–28', 'Pregunta: «Si los primeros humanos surgieron en África, ¿cómo llegaron a América?». Muestra el planisferio.',
             'Proponen hipótesis.', 'Hipótesis en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('28–40', 'Lectura de «El último continente habitado»: explica la glaciación y Beringia.',
             'Resuelven la actividad 1.', 'Actividad 1 (esencial).'),
            ('40–55', 'Explica el cuadro de las teorías clásicas.',
             'Resuelven la actividad 2 y comparan cada teoría con lo que se sabe hoy.', 'Actividad 2 (esencial).'),
            ('55–72', 'Lectura de «Lo que se sabe hoy» con la Figura 4.1 y el Concepto clave.',
             'Resuelven el «Ubicate» y las actividades 3 y 8.', 'Ubicate; actividades 3 y 8 (esenciales).'),
            ('72–90', 'Presenta la fuente científica y aclara que las fechas son aproximadas.',
             'Responden las preguntas 1 a 3 de la fuente.', 'Fuente (esencial).'),
            ('90–104', 'Lee los criterios de la actividad 12 y acompaña la escritura.',
             'Escriben la actividad 12; quien termina sigue con las actividades 4, 5, 6 y 9.', 'Actividad 12 (esencial); consolidación.'),
        ]),
        ('Cierre', [
            ('104–120', 'Puesta en común de la actividad 12 y de la pregunta 3 de la fuente: «¿qué haría falta para aceptar un dato?». Asigna la tarea.',
             'Leen respuestas y corrigen.', 'Respuestas revisadas.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en la lectura del cuadro de teorías: el docente lo lee fila por fila y los estudiantes subrayan «qué proponía».',
        'Apoyo en la fuente: línea de tiempo dibujada en la pizarra con las cuatro fechas para ordenarlas.',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: averiguar qué es el carbono 14 y para qué sirve en arqueología.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Lectura de mapa; análisis de fuente científica; producción escrita breve.',
        'instrumentos': 'Lista de cotejo con los tres indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Explica el cruce por Beringia en la última glaciación.',
                      'Distingue las teorías clásicas y cuál se confirmó en lo central.',
                      'Usa fechas aproximadas y reconoce cuáles están en debate.'],
    },
    'precisiones': [
        'Pre-Clovis ya no está «en debate»: es la posición mayoritaria. Lo que se discute es cuánto antes y por qué rutas.',
        'Las rutas del mapa son propuestas, no caminos documentados.',
    ],
    'tarea': 'Actividades 7, 10 y 11 de la Clase 4.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente', [
            ('F1', 'White Sands (21.000-23.000 años, en discusión), Monte Verde (14.500), Clovis (13.000), Cueva Fell (más de 11.000).',
             'Si deja White Sands aparte por estar en discusión, también es correcto.'),
            ('F2', 'Monte Verde, porque es más antiguo que Clovis (14.500 frente a 13.000 años) y su antigüedad fue aceptada.', ''),
            ('F3', 'Porque una sola fecha no alcanza: los científicos piden repetir los análisis con otros métodos y encontrar más '
                   'sitios con fechas parecidas.', 'Se acepta cualquier criterio razonable de comprobación.'),
        ]),
        ('Ubicate (Figura 4.1)', [
            ('U', 'Beringia entre Siberia y Alaska; Monte Verde en el sur de Chile. El poblamiento avanzó de norte a sur. Monte '
                  'Verde es importante porque, si hace 14.500 años ya había gente en el extremo sur, los primeros grupos debieron '
                  'entrar al continente antes todavía.', ''),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'b) una franja de tierra entre Siberia y Alaska que quedó al descubierto en la glaciación', ''),
            ('2', 'c) se originó en América', ''),
            ('3', 'd) hubo poblamiento anterior a Clovis', ''),
            ('4', 'a) el sur de Chile', ''),
        ]),
        ('Completá los espacios', [
            ('5', 'África', ''),
            ('6', 'bajo', ''),
            ('7', 'Aleš Hrdlička', 'Se acepta «Hrdlička».'),
        ]),
        ('Verdadero o falso', [
            ('8', 'Falso: no se encontraron restos de especies humanas anteriores en América.', 'Justificación obligatoria.'),
            ('9', 'Verdadero.', ''),
            ('10', 'Falso: la fecha sigue en discusión.', 'Justificación obligatoria.'),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'Se confirmó el origen asiático y el paso por la zona de Bering. Cambió la idea de una sola migración reciente: hoy '
                   'se piensa en varios grupos, posibles rutas por la costa y una llegada anterior a Clovis.', ''),
            ('12', 'Ejemplo: «Antes se creía que la cultura Clovis, de hace unos 13.000 años, era la primera de América. Después se '
                   'estudió Monte Verde, en Chile, con unos 14.500 años. Hoy se acepta que hubo pobladores antes de Clovis. Una teoría '
                   'cambia cuando aparecen pruebas nuevas.»',
             'Criterio anunciado en la consigna: qué se creía antes (1 punto), qué dato nuevo apareció (1 punto) y qué se acepta hoy (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Homo sapiens hace unos 300.000 años en África', 'Dato habitual (hallazgos de Jebel Irhoud); cotejar.'),
    ('Monte Verde ≈ 14.500 años; aceptación de 1997', 'Bibliografía arqueológica (Dillehay); cotejar.'),
    ('Clovis ≈ 13.000 años; Cueva Fell más de 11.000; White Sands 21.000-23.000 (2021, en discusión)', 'Cotejar con publicaciones científicas.'),
    ('Autores y épocas de las teorías clásicas (Ameghino, Hrdlička, Rivet, Mendes Correia)', 'Contenido habitual de manuales; cotejar.'),
]

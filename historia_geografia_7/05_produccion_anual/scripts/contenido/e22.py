"""Encuentro 22 — Continuación E: Bandeirantes, pérdida del Guairá y Mbororé (H5; temas H5c y H5d).

Condición A05/N05 del dictamen: el núcleo del encuentro es el siglo XVII
(malocas bandeirantes, destrucción de las reducciones del Guairá, éxodo de
1631, abandono de Villa Rica y Ciudad Real, Mbororé 1641). La Guerra
Guaranítica (1754-1756) aparece solo como recuadro de ampliación optativa del
siglo XVIII, que no se evalúa. La selección de estos hechos es editorial,
dentro de los temas literales H5c y H5d del programa: no se atribuye al MEC.
"""
import curriculo as C

TITULO = 'Continuación E — Bandeirantes, pérdida del Guairá y Mbororé (siglo XVII)'
CLAVE = 'Continuación E —'
INDICADORES = [
    'Explica qué eran las malocas bandeirantes y cómo afectaron a los guaraníes y a las reducciones del Guairá.',
    'Ordena y ubica en el mapa los hechos de 1609 a 1641: reducciones, malocas, éxodo, abandono de las ciudades del Guairá y Mbororé.',
    'Explica las causas y consecuencias de la batalla de Mbororé para la provincia del Paraguay.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H5'], C.TEMAS['H5c'] + ' ' + C.TEMAS['H5d'], INDICADORES),

    ('h2', 'Los bandeirantes'),
    ('p', 'En la Clase 12 viste que llegaban malocas desde São Paulo. Los bandeirantes eran grupos armados de paulistas —portugueses, '
          'mestizos y muchos indígenas tupí a su servicio— que se internaban en el interior del continente. Una de sus principales '
          'actividades era capturar indígenas para venderlos como esclavos en las plantaciones de azúcar del Brasil.'),
    ('p', 'Las reducciones jesuíticas del Guairá, fundadas desde 1610 entre los ríos Paranapanema, Paraná e Iguazú, eran un blanco '
          'fácil: reunían a miles de guaraníes en un mismo lugar y no tenían armas de fuego. Entre 1628 y 1631, las malocas, '
          'encabezadas por jefes como Antonio Raposo Tavares, destruyeron casi todas esas reducciones y se llevaron a miles de '
          'personas.'),

    ('h2', 'El éxodo de 1631 y la pérdida del Guairá'),
    ('p', 'Ante la destrucción, el jesuita Antonio Ruiz de Montoya organizó en 1631 la huida de los guaraníes de las reducciones '
          'que quedaban. Miles de personas bajaron por el río Paraná en balsas y canoas; al llegar a los Saltos del Guairá tuvieron '
          'que seguir a pie por la selva. Muchas murieron de hambre y enfermedades durante el viaje. Los sobrevivientes fundaron '
          'nuevos pueblos más al sur, entre los ríos Paraná y Uruguay.'),
    ('p', 'Sin la protección de las reducciones, en 1632 los vecinos españoles abandonaron Villa Rica del Espíritu Santo y Ciudad '
          'Real del Guairá y se trasladaron hacia el oeste. Desde São Paulo, las malocas siguieron hacia el Itatín, al norte de '
          'Asunción. La provincia del Paraguay perdió así el control del Guairá, que con el tiempo quedó en manos portuguesas.'),
    ('fig', 'fig_E_1_guaira_mborore.png', 'Figura E.1 — Malocas, éxodo y Mbororé en el siglo XVII (trazados aproximados).', 13.0),

    ('h2', 'Mbororé, 1641'),
    ('p', 'Los jesuitas pidieron a la Corona permiso para entregar armas de fuego a los guaraníes de las reducciones y lo '
          'obtuvieron. Los guaraníes se organizaron como milicia, se entrenaron y construyeron canoas armadas. En marzo de 1641, '
          'una gran bandeira que bajaba por el río Uruguay fue derrotada en Mbororé por un ejército guaraní dirigido por el '
          'cacique Nicolás Ñeenguirú.'),
    ('p', 'La victoria de Mbororé detuvo las grandes malocas sobre las reducciones del Paraná y del Uruguay. Desde entonces, las '
          'milicias guaraníes defendieron esa frontera durante más de un siglo, y las reducciones pudieron crecer.'),
    ('fig', 'fig_E_2_linea_1609_1641.png', 'Figura E.2 — De las primeras reducciones a Mbororé (1609-1641).', 11.5),
    ('caja', 'concepto', 'Concepto clave — ',
     'Maloca: expedición armada para capturar indígenas y esclavizarlos. Éxodo: salida masiva de un pueblo de su territorio. '
     'La pérdida del Guairá fue una consecuencia de las malocas; Mbororé fue la respuesta guaraní que puso límite a esa amenaza.'),
    ('caja', 'ejemplo', 'Ampliación optativa (siglo XVIII; no se evalúa) — ',
     'Más de un siglo después, el Tratado de Madrid (1750) entre España y Portugal entregaba a Portugal siete pueblos de las '
     'reducciones, en el actual Rio Grande do Sul, a cambio de la Colonia del Sacramento. Los guaraníes se negaron a abandonar '
     'sus pueblos y resistieron entre 1754 y 1756: es la Guerra Guaranítica. El líder Sepé Tiarajú murió en 1756 y los '
     'guaraníes fueron derrotados en Caiboaté. En 1761 el tratado fue anulado. Este recuadro sirve para quien quiera saber más.'),

    ('fuente', 'Documento de época · Antonio Ruiz de Montoya, Conquista espiritual (Madrid, 1639). Versión escolar resumida: no es cita textual.',
     ['Montoya cuenta que, después de la destrucción de las reducciones del Guairá por los paulistas, decidió con los demás padres '
      'sacar a los indios que quedaban. Embarcaron a miles de personas en balsas por el río Paraná. Al llegar a los grandes saltos '
      'debieron abandonar las embarcaciones y caminar por la selva. Muchos murieron de hambre y de enfermedad, y los que llegaron '
      'fundaron nuevos pueblos.'],
     'Vocabulario: paulistas, habitantes de São Paulo; padres, los sacerdotes jesuitas.',
     ['¿Quién escribió esta obra y qué papel tuvo en los hechos que cuenta?',
      '¿Qué dificultades del viaje menciona la fuente?',
      'Montoya era jesuita y quería que el rey protegiera las reducciones. ¿Qué cuidado hay que tener al leer su relato?']),
    ('renglones', 6),

    ('h2', 'Consignas del taller'),
    ('p', 'Trabajá en parejas con la Ficha reproducible E, las Figuras E.1 y E.2 y la fuente.'),
    ('consigna', 'Consignas del taller:'),
    ('item', '1. En el mapa mudo de la Ficha E: marcá con un punto São Paulo, Asunción, los Saltos del Guairá y Mbororé, y '
             'sombreá la región del Guairá. Dibujá en rojo una maloca y en verde el éxodo de 1631. Completá el título y la leyenda.'),
    ('item', '2. Completá la cadena de causas y consecuencias.'),
    ('cuadro', ['Hecho', '¿Por qué ocurrió?', '¿Qué consecuencia tuvo?'],
     ['Malocas al Guairá (1628-1631)', 'Éxodo por el Paraná (1631)', 'Abandono de Villa Rica y Ciudad Real (1632)', 'Batalla de Mbororé (1641)'],
     [3.2, 3.4, 3.4], 1.4),
    ('item', '3. ¿Qué tiene que ver la pérdida del Guairá con la mediterraneidad y la división de 1617 que estudiaste en la Clase 11? '
             'Escribí una relación.', 4),
    ('item', '4. Escribí un comentario de 6 a 8 líneas: ¿por qué fue importante Mbororé para los guaraníes y para la provincia del '
             'Paraguay? Se tendrá en cuenta: qué amenaza detuvo (1 punto), cómo se preparó la defensa (1 punto), una consecuencia '
             'posterior (1 punto) y el uso de datos de la Figura E.2 (1 punto).', 8),
    ('h3', 'Autoevaluación del taller'),
    ('tabla', ['Criterio', 'Lo logré', 'En proceso', 'Todavía no'],
     [['Mi mapa tiene título, lugares, recorridos y leyenda.', '', '', ''],
      ['Expliqué por qué ocurrió cada hecho y qué consecuencia tuvo.', '', '', ''],
      ['Analicé la fuente teniendo en cuenta quién la escribió.', '', '', ''],
      ['Usé fechas para explicar la importancia de Mbororé.', '', '', '']],
     [5.5, 1.5, 1.5, 1.5]),
]

FICHAS = [
    ('ficha_repro', 'Ficha reproducible E — Mapa mudo del Guairá y de las reducciones',
     [('p', 'Título del mapa: ______________________________________________'),
      ('fig', 'ficha_E_mapa_mudo.png', 'Mapa mudo para la consigna 1. Elaboración propia con datos de Natural Earth (dominio público); mapa aproximado.', 15.0),
      ('cuadro', ['Leyenda: color o símbolo', 'Qué representa'], ['', '', '', '', ''], [3.0, 7.0], 0.9)]),
]

PLAN = {
    'material': 'Tomo: Continuación E (Figuras E.1 y E.2) y Clases 11 a 13; Ficha reproducible E (una por pareja, preparada antes del encuentro); lápices rojo y verde',
    'tema': C.TEMAS['H5c'] + ' ' + C.TEMAS['H5d'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes expliquen el hecho central del siglo XVII paraguayo: las malocas bandeirantes, la pérdida del '
                 'Guairá y la victoria de Mbororé, con mapa, cronología y fuente.',
    'funciones': {
        'Esenciales': 'En clase: fuente (preguntas 1 a 3); consignas 1, 2 y 4; Ficha E.',
        'Consolidación': 'La consigna 3 y la autoevaluación del taller (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 23).',
        'Complementarias o domiciliarias': 'Lectura optativa del recuadro de ampliación sobre la Guerra Guaranítica (no se evalúa).',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 13. Pregunta: «¿Por qué miles de personas abandonarían sus pueblos de un día para otro?».',
             'Proponen hipótesis.', 'Hipótesis en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–28', 'Lectura de «Los bandeirantes» y de «El éxodo de 1631» con la Figura E.1.',
             'Señalan en la Figura E.1 São Paulo, el Guairá y el recorrido del éxodo.', 'Lectura del mapa.'),
            ('28–48', 'Entrega la Ficha E y modela el trazado de la primera maloca.',
             'Resuelven la consigna 1 en parejas.', 'Ficha E (esencial).'),
            ('48–62', 'Lectura de «Mbororé, 1641» con la Figura E.2.',
             'Resuelven la consigna 2.', 'Consigna 2 (esencial).'),
            ('62–78', 'Presenta el fragmento de Montoya y aclara que es una versión resumida, no una cita textual.',
             'Responden las preguntas 1 a 3 de la fuente.', 'Fuente (esencial).'),
            ('78–98', 'Lee los criterios de la consigna 4 y acompaña la escritura.',
             'Escriben el comentario.', 'Consigna 4 (esencial).'),
        ]),
        ('Cierre', [
            ('98–112', 'Puesta en común: dos comentarios leídos en voz alta y la pregunta 3 de la fuente. Señala el recuadro de ampliación como lectura optativa.',
             'Comparan y corrigen.', 'Comentarios revisados.'),
            ('112–120', 'Explica la autoevaluación y asigna lo que quedó pendiente.',
             'Completan la autoevaluación.', 'Autoevaluación.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en el mapa: algunas copias de la Ficha E llevan marcados con un punto los cuatro lugares; el estudiante escribe los nombres.',
        'Apoyo en la consigna 2: la primera fila resuelta en la pizarra como modelo.',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: leer el recuadro de ampliación y explicar qué tienen en común Mbororé y la Guerra Guaranítica, y en qué se diferencian.',
    ],
    'evaluacion': {
        'tipo': 'Formativa, con producto.',
        'procedimientos': 'Mapa histórico; cadena causal; análisis de fuente; comentario.',
        'instrumentos': 'Ficha E; autoevaluación; consigna 4 con los criterios de su consigna.',
        'criterios': ['El mapa tiene título, lugares, recorridos diferenciados y leyenda.',
                      'Explica causas y consecuencias de las malocas, el éxodo y Mbororé.',
                      'Analiza la fuente considerando la intención de su autor.'],
    },
    'precisiones': [
        'Núcleo del encuentro: siglo XVII (condición A05/N05). La Guerra Guaranítica (1754-1756) es solo ampliación optativa del siglo XVIII y no se evalúa como contenido obligatorio.',
        'La selección de hechos (bandeirantes, Guairá, Mbororé) es editorial, dentro de los temas H5c y H5d del programa; no se presenta como selección del MEC.',
        'El fragmento de Montoya es una versión escolar resumida, no una cita textual. Las cifras del éxodo varían según las fuentes: el tomo no las da.',
    ],
    'tarea': 'Terminar la consigna 3 y la autoevaluación si quedaron pendientes.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente', [
            ('F1', 'Antonio Ruiz de Montoya, jesuita. Fue protagonista: organizó y encabezó el éxodo.', ''),
            ('F2', 'Abandonar las embarcaciones en los saltos, caminar por la selva, el hambre y las enfermedades.', ''),
            ('F3', 'Que es una fuente parcial: el autor defendía a los jesuitas y quería convencer al rey; hay que compararla con otras '
                   'fuentes, por ejemplo documentos de los paulistas o de las autoridades españolas.', ''),
        ]),
        ('Consignas del taller', [
            ('1', 'São Paulo en el planalto interior del sudeste brasileño, próximo al litoral; Asunción sobre el río Paraguay; los Saltos del Guairá sobre el Paraná; '
                  'Mbororé junto al río Uruguay. El Guairá, al este del Paraná, entre el Paranapanema y el Iguazú. Maloca de São Paulo al '
                  'Guairá; éxodo por el Paraná hacia el sur.',
             'Lista de cotejo: título; cuatro lugares; región sombreada; dos recorridos con colores distintos; leyenda. Se compara con la Figura E.1.'),
            ('2', 'Malocas: buscaban esclavos para las plantaciones; consecuencia, destrucción de las reducciones del Guairá. Éxodo: para '
                  'escapar de las malocas; consecuencia, nuevos pueblos entre el Paraná y el Uruguay, con muchas muertes en el camino. '
                  'Abandono de las ciudades: quedaron sin protección; consecuencia, la provincia perdió el Guairá. Mbororé: los guaraníes '
                  'armados enfrentaron una gran bandeira; consecuencia, se detuvieron las grandes malocas.',
             'Por qué y consecuencia de cada fila; se aceptan expresiones equivalentes.'),
            ('3', 'La provincia era mediterránea y, después de 1617, dependía de Buenos Aires: tenía pocos recursos y poca ayuda para '
                  'defender sus ciudades del este. Por eso no pudo frenar las malocas y perdió el Guairá.',
             'Una relación coherente entre la debilidad de la provincia y la pérdida del Guairá.'),
            ('4', 'Ejemplo: «Mbororé fue importante porque en 1641 los guaraníes derrotaron a una gran bandeira y se detuvieron las '
                  'malocas que, entre 1628 y 1631, habían destruido las reducciones del Guairá. La victoria fue posible porque los '
                  'jesuitas consiguieron armas y los guaraníes se organizaron como milicia. Después, las reducciones crecieron y las '
                  'milicias guaraníes defendieron la frontera.»',
             'Criterio anunciado en la consigna: qué amenaza detuvo (1 punto), cómo se preparó la defensa (1 punto), una consecuencia '
             'posterior (1 punto) y el uso de datos de la Figura E.2 (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Malocas al Guairá 1628-1631 (Raposo Tavares); éxodo de 1631; abandono de Villa Rica y Ciudad Real en 1632; malocas al Itatín', 'Fechas habituales; cotejar.'),
    ('Mbororé: marzo de 1641; cacique Nicolás Ñeenguirú; permiso de armas de fuego', 'Bibliografía habitual; cotejar la fecha del permiso real y la grafía Ñeenguirú / Neenguirú.'),
    ('Fragmento de la Conquista espiritual (1639)', 'Versión escolar resumida y declarada como no textual; cotejar con una edición de la obra.'),
    ('Ampliación optativa: Tratado de Madrid 1750, Guerra Guaranítica 1754-1756, Sepé Tiarajú y Caiboaté 1756, Tratado de El Pardo 1761',
     'Fechas habituales; contenido de ampliación, no evaluable.'),
    ('Trazados de la Figura E.1 y de la Ficha E', 'Aproximados de la editorial.'),
]

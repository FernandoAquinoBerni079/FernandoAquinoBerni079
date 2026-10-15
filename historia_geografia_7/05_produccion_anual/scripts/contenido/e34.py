"""Encuentro 34 — Continuación G: Clima, ecosistemas y gestión ambiental (G3 y G4; temas G3b, G4b y G4c).

Taller integrador de la Unidad 6. El caso del taller es didáctico y ficticio,
y se declara así: no describe un lugar real ni usa cifras reales.
"""
import curriculo as C

TITULO = 'Continuación G — Clima, ecosistemas y gestión ambiental'
CLAVE = 'Continuación G —'
INDICADORES = [
    'Relaciona el clima del Paraguay con sus grandes ecosistemas y las actividades de cada región.',
    'Representa en un mapa el gradiente de lluvias y la ubicación de los ecosistemas, con leyenda.',
    'Propone medidas de gestión ambiental fundamentadas en normas e instituciones vigentes.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['G3'] + ' ' + C.CAPACIDADES['G4'], C.TEMAS['G3b'] + ' ' + C.TEMAS['G4b'] + ' ' + C.TEMAS['G4c'], INDICADORES),
    ('h2', 'Todo está relacionado'),
    ('p', 'En las Clases 19, 20 y 21 estudiaste el clima, las regiones naturales y la gestión ambiental. En este taller vas a '
          'relacionar los tres temas: el clima explica en buena parte qué ecosistemas hay en cada región; los ecosistemas condicionan '
          'qué actividades se hacen; y esas actividades producen cambios que la gestión ambiental debe prevenir y controlar.'),
    ('tabla', ['Región', 'Clima', 'Ecosistemas', 'Actividad principal'],
     [['Noroeste del Chaco', 'Seco y muy caluroso (unos 400 mm de lluvia al año)', 'Chaco Seco', 'Ganadería'],
      ['Este del Chaco', 'Más húmedo, con inundaciones', 'Chaco Húmedo, palmares y esteros', 'Ganadería'],
      ['Este de la Región Oriental', 'Húmedo (unos 1.800 mm al año)', 'Bosque Atlántico del Alto Paraná', 'Agricultura']],
     [2.6, 3.0, 2.6, 1.8]),

    ('h2', 'Un caso para analizar'),
    ('p', 'Caso didáctico ficticio, preparado para el taller: no describe un lugar real ni usa cifras reales.'),
    ('p', 'En un distrito del Chaco Húmedo hay una laguna que abastece de agua al ganado y a una comunidad indígena cercana. En los '
          'últimos años, un establecimiento desmontó parte del bosque que rodeaba la laguna para ampliar sus pasturas. Después de '
          'una sequía, la laguna bajó mucho, aparecieron peces muertos y la comunidad denunció que el agua estaba turbia. El '
          'establecimiento afirma que tenía permiso para el desmonte.'),
    ('caja', 'concepto', 'Concepto clave — ',
     'Una buena gestión ambiental combina prevención (estudiar antes de actuar), control (verificar que se cumplan las normas) y '
     'reparación (recomponer el daño). Participan el Estado, las empresas y la ciudadanía.'),

    ('h2', 'Consignas del taller'),
    ('p', 'Trabajá en parejas. Usá la Ficha reproducible G, las Figuras 19.3, 20.2 y 21.1 y el cuadro de este taller.'),
    ('consigna', 'Consignas del taller:'),
    ('item', '1. En el mapa mudo de la Ficha G: dibujá una flecha que muestre hacia dónde aumentan las lluvias y escribí los valores '
             'aproximados en sus extremos; ubicá con un número el Chaco Seco, el Chaco Húmedo, el Pantanal y el Bosque Atlántico del '
             'Alto Paraná; completá el título y la leyenda.'),
    ('item', '2. Explicá con el cuadro por qué en el noroeste del Chaco predomina la ganadería y en el este de la Región Oriental, la '
             'agricultura. Nombrá también otro factor que influya además del clima.', 6),
    ('item', '3. Completá la matriz del caso.'),
    ('cuadro', ['Problema', '¿Qué norma se relaciona?', '¿Qué institución debe intervenir?', 'Medida propuesta'],
     ['Desmonte alrededor de la laguna', 'Agua turbia y peces muertos', 'Comunidad sin agua segura'], [2.6, 2.5, 2.5, 2.4], 1.8),
    ('item', '4. Escribí una propuesta de 6 a 8 líneas para resolver el caso. Se tendrá en cuenta: la relación entre clima, ecosistema y '
             'problema (1 punto), una norma y una institución bien elegidas (1 punto), una medida de prevención o de reparación '
             'coherente (1 punto) y la participación de la comunidad (1 punto).', 8),
    ('h3', 'Autoevaluación del taller'),
    ('tabla', ['Criterio', 'Lo logré', 'En proceso', 'Todavía no'],
     [['Mi mapa muestra el aumento de las lluvias y los ecosistemas, con leyenda.', '', '', ''],
      ['Relacioné el clima con los ecosistemas y las actividades.', '', '', ''],
      ['Elegí normas e instituciones adecuadas para el caso.', '', '', ''],
      ['Mi propuesta incluye prevención o reparación y participación.', '', '', '']],
     [5.5, 1.5, 1.5, 1.5]),
    ('p', 'Lo que más me sirvió de esta unidad para entender el lugar donde vivo fue…'),
    ('renglones', 3),
]

FICHAS = [
    ('ficha_repro', 'Ficha reproducible G — Mapa mudo del Paraguay: lluvias y ecosistemas',
     [('p', 'Título del mapa: ______________________________________________'),
      ('fig', 'ficha_G_mapa_mudo.png', 'Mapa mudo para la consigna 1. Elaboración propia con datos de Natural Earth (dominio público); mapa aproximado.', 15.0),
      ('cuadro', ['Leyenda: color, número o símbolo', 'Qué representa'], ['', '', '', '', ''], [3.4, 6.6], 0.9)]),
]

PLAN = {
    'material': 'Tomo: Continuación G y Figuras 19.3, 20.2 y 21.1; Ficha reproducible G (una por pareja, preparada antes del encuentro); lápices de colores',
    'tema': C.TEMAS['G3b'] + ' ' + C.TEMAS['G4b'] + ' ' + C.TEMAS['G4c'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes integren clima, ecosistemas y gestión ambiental en un mapa, un análisis de caso y una propuesta fundamentada.',
    'funciones': {
        'Esenciales': 'En clase: consignas 1, 3 y 4 del taller; Ficha G.',
        'Consolidación': 'La consigna 2 y la autoevaluación del taller (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 35).',
        'Complementarias o domiciliarias': 'Repasar las Clases 19 a 21 y la Continuación G para la Evaluación de la Unidad 6.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 21. Pregunta: «¿Qué tiene que ver la lluvia con el tipo de bosque?».',
             'Proponen relaciones.', 'Ideas en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–22', 'Lectura de «Todo está relacionado» y del cuadro de regiones.',
             'Subrayan en el cuadro el clima y la actividad de cada región.', 'Cuadro subrayado.'),
            ('22–48', 'Entrega la Ficha G y modela cómo dibujar la flecha de las lluvias.',
             'Resuelven la consigna 1 en parejas.', 'Ficha G (esencial).'),
            ('48–58', 'Acompaña la explicación escrita.', 'Resuelven la consigna 2.', 'Consigna 2 (consolidación).'),
            ('58–80', 'Lectura del caso y del Concepto clave. Aclara que el caso es ficticio.',
             'Completan la matriz (consigna 3) con la Figura 21.1 y el cuadro de normas de la Clase 21.', 'Consigna 3 (esencial).'),
            ('80–100', 'Lee los criterios de la consigna 4 y acompaña la escritura.', 'Escriben la propuesta.', 'Consigna 4 (esencial).'),
        ]),
        ('Cierre', [
            ('100–112', 'Dos parejas muestran su mapa y leen su propuesta; el grupo comprueba leyenda y criterios.', 'Comparan y corrigen.', 'Mapas y propuestas revisados.'),
            ('112–120', 'Explica la autoevaluación y recuerda que el próximo encuentro es la Evaluación de la Unidad 6.',
             'Completan la autoevaluación.', 'Autoevaluación.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en el mapa: algunas copias de la Ficha G llevan marcados los cuatro números; el estudiante escribe el ecosistema en la leyenda.',
        'Apoyo en la consigna 3: la primera fila resuelta en la pizarra como modelo.',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: investigar si en la localidad hay un problema ambiental parecido al del caso y qué se hizo.',
    ],
    'evaluacion': {
        'tipo': 'Formativa, con producto.',
        'procedimientos': 'Mapa temático; análisis de caso; matriz; propuesta escrita.',
        'instrumentos': 'Ficha G; matriz de la consigna 3; consigna 4 con los criterios de su consigna; autoevaluación.',
        'criterios': ['El mapa muestra el gradiente de lluvias y los ecosistemas, con leyenda.',
                      'Relaciona clima, ecosistema y actividad.',
                      'Propone medidas fundadas en normas e instituciones.'],
    },
    'precisiones': [
        'El caso es ficticio y no tiene cifras: se evalúa el razonamiento, no una única respuesta.',
        'Los valores de lluvia son aproximados (Clase 19).',
    ],
    'tarea': 'Terminar la consigna 2 y la autoevaluación si quedaron pendientes. Repasar las Clases 19 a 21 y la Continuación G.',
}

SOL = {
    'bloques': [
        ('Consignas del taller', [
            ('1', 'Flecha del noroeste del Chaco (unos 400 mm) hacia el este de la Región Oriental (unos 1.800 mm). Chaco Seco al '
                  'noroeste; Chaco Húmedo cerca del río Paraguay; Pantanal al norte, junto al río Paraguay; Bosque Atlántico al este, '
                  'junto al Paraná.',
             'Lista de cotejo: título; flecha con valores; cuatro ecosistemas; leyenda. Se compara con las Figuras 19.3 y 20.2.'),
            ('2', 'En el noroeste del Chaco llueve poco y hace mucho calor: hay bosques secos y pasturas, por eso predomina la ganadería. '
                  'En el este de la Región Oriental llueve mucho y los suelos son fértiles: se cultiva. Otros factores: los suelos, la '
                  'tecnología, los caminos y los mercados.', 'Clima y otro factor.'),
            ('3', 'Desmonte: Ley 294/1993 (evaluación de impacto ambiental); INFONA y MADES; verificar el permiso y reforestar la orilla. '
                  'Agua turbia y peces muertos: Ley 716/1996 (delitos ambientales); MADES y Ministerio Público; análisis del agua y '
                  'sanción si hubo delito. Comunidad sin agua: Constitución, art. 7; gobernación, municipalidad y MADES; provisión '
                  'segura de agua y consulta a la comunidad.', 'Se aceptan otras normas e instituciones coherentes.'),
            ('4', 'Ejemplo: «El Chaco Húmedo tiene períodos de sequía; sin el bosque, la laguna pierde protección y se calienta. El MADES '
                  'debe revisar si el desmonte tenía evaluación de impacto ambiental (Ley 294/1993) y el INFONA, el plan de uso de la '
                  'tierra. Propongo reforestar la orilla y controlar el agua, y que la comunidad indígena participe en las decisiones.»',
             'Criterio anunciado en la consigna: la relación entre clima, ecosistema y problema (1 punto), una norma y una institución '
             'bien elegidas (1 punto), una medida de prevención o de reparación coherente (1 punto) y la participación de la comunidad (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Caso del taller', 'Caso didáctico ficticio, declarado en el tomo.'),
    ('Normas e instituciones citadas en la solución', 'Las de la Clase 21; cotejar en la BACN.'),
]

"""Encuentro 23 — Clase 14: Haciendas, minería y comercio en la América colonial (H6; tema H6a).

Corrige el maestro: el Paraguay no estaba al margen de la plata (vendía yerba
a Potosí); agrega la mita minera, el azogue de Huancavelica, Zacatecas, el
sistema de flotas y galeones, el contrabando por Buenos Aires y la aduana de
Córdoba; distingue hacienda y plantación; la fuente lleva autor y fecha.
"""
import curriculo as C

TITULO = 'Clase 14 — Haciendas, minería y comercio en la América colonial'
CLAVE = 'Clase 14 —'
INDICADORES = [
    'Describe la minería de la plata y la mita minera, y sus consecuencias para los pueblos indígenas.',
    'Diferencia la hacienda de la plantación.',
    'Explica el monopolio comercial, el sistema de flotas y el contrabando, y cómo se vinculaba el Paraguay con ese sistema.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H6'], C.TEMAS['H6a'], INDICADORES),

    ('h2', 'La plata: Potosí y Zacatecas'),
    ('p', 'La riqueza que más le interesaba a la Corona española era la plata. En 1545 se descubrió el cerro de Potosí, en el Alto '
          'Perú (actual Bolivia), y en 1546 las minas de Zacatecas, en Nueva España (actual México). Potosí llegó a ser una de las '
          'ciudades más pobladas del mundo en el siglo XVII.'),
    ('p', 'Para separar la plata de la roca se usaba el azogue (mercurio), que se extraía de las minas de Huancavelica, en el Perú. '
          'En la década de 1570, el virrey Francisco de Toledo organizó la mita minera: cada año, miles de indígenas de los pueblos '
          'andinos debían ir por turnos a trabajar en las minas. Las condiciones eran durísimas: los accidentes, las enfermedades y '
          'el envenenamiento con mercurio causaron muchísimas muertes.'),

    ('h2', 'Haciendas y plantaciones'),
    ('tabla', ['', 'Hacienda', 'Plantación'],
     [['Qué producía', 'Ganado, cereales, mulas y otros productos para las ciudades y las minas.', 'Un solo producto para exportar, sobre todo azúcar.'],
      ['Dónde', 'En casi toda la América española (Nueva España, el Perú, el Río de la Plata).', 'En el nordeste del Brasil y en las islas del Caribe.'],
      ['Quiénes trabajaban', 'Indígenas encomendados o mitayos, peones con salario o endeudados, y algunos esclavizados.',
       'Sobre todo africanos esclavizados.']],
     [2.2, 3.9, 3.9]),
    ('p', 'Las haciendas abastecían a las ciudades y a los centros mineros: Potosí, por ejemplo, necesitaba alimentos, tejidos y '
          'miles de mulas que llegaban desde regiones lejanas, como Tucumán y Córdoba.'),

    ('h2', 'El monopolio y el sistema de flotas'),
    ('p', 'La Corona impuso el monopolio comercial: las colonias solo podían comerciar con España, a través de la Casa de '
          'Contratación de Sevilla. Para proteger la plata de los piratas y corsarios, los barcos viajaban juntos en flotas '
          'custodiadas por buques de guerra. La flota de Nueva España iba a Veracruz; los galeones de Tierra Firme, a Cartagena y '
          'Portobelo, adonde llegaba la plata del Perú desde el puerto del Callao. Al regreso, las flotas se reunían en La Habana '
          'y cruzaban juntas el Atlántico.'),
    ('h2', 'El contrabando y el Paraguay'),
    ('p', 'Buenos Aires no era un puerto autorizado para el gran comercio, y en 1622 se creó la aduana de Córdoba para impedir que '
          'la plata del Potosí saliera por allí. Aun así, por Buenos Aires salía plata de contrabando y entraban mercaderías '
          'europeas y africanos esclavizados traídos por comerciantes portugueses, holandeses e ingleses.'),
    ('p', 'El Paraguay no tenía minas, pero no estaba al margen de este sistema: vendía yerba mate, tabaco y lienzos que llegaban '
          'hasta Potosí y Chile. Con lo obtenido, los comerciantes compraban productos europeos.'),
    ('fig', 'fig_14_1_plata.png', 'Figura 14.1 — Minas, puertos y rutas del comercio colonial en el siglo XVII (esquema aproximado).', 16.0),
    ('caja', 'concepto', 'Concepto clave — ',
     'Monopolio comercial: sistema en el que un solo país controla todo el comercio de sus colonias. Contrabando: comercio '
     'prohibido, hecho a escondidas para no pagar impuestos o para comerciar con quien la ley no permite.'),

    ('ubicate', 'Ubicate  ·  Mapa (Figura 14.1)',
     'Ubicá Potosí y Asunción. ¿En qué dirección está Potosí respecto de Asunción? Seguí el recorrido de la plata desde Potosí '
     'hasta Sevilla: ¿por qué puertos pasaba?'),
    ('renglones', 3),

    ('fuente', 'Documento de época · Carta de fray Domingo de Santo Tomás al Consejo de Indias (1550). Versión escolar resumida: no es cita textual, salvo la expresión entre comillas.',
     ['El fraile cuenta que hace pocos años se descubrió en el Perú una «boca del infierno», a la que cada año llevan a gran '
      'cantidad de indios para sacar la plata, y que muchos de ellos mueren o no vuelven a sus pueblos. Pide al rey que remedie '
      'esa situación.'],
     'Vocabulario: Consejo de Indias, organismo que asesoraba al rey sobre América.',
     ['¿Qué lugar llama el fraile «boca del infierno»? ¿Por qué usa esa expresión?',
      '¿Qué le pide al rey?',
      'La carta es de 1550, antes de la mita de Toledo. ¿Qué te dice eso sobre el trabajo en las minas antes y después de la década de 1570?']),
    ('renglones', 6),
    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. Las minas de plata más importantes de la América española en el siglo XVII estaban en…'),
    ('opc', ['La Habana y Cartagena', 'Asunción y Buenos Aires', 'Sevilla y Cádiz', 'Potosí y Zacatecas']),
    ('item', '2. La mita minera era…'),
    ('opc', ['un barco que llevaba plata a Sevilla', 'el trabajo obligatorio por turnos de indígenas en las minas',
             'el nombre del mercurio de Huancavelica', 'un impuesto que pagaban los comerciantes']),
    ('item', '3. A diferencia de la hacienda, la plantación…'),
    ('opc', ['producía un solo producto para exportar con trabajo esclavizado', 'producía alimentos para las ciudades cercanas',
             'no tenía trabajadores', 'estaba solo en el Río de la Plata']),
    ('item', '4. El monopolio comercial significaba que las colonias…'),
    ('opc', ['podían comerciar con cualquier país', 'no podían producir nada', 'solo podían comerciar con España',
             'comerciaban solo con Portugal']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. El mercurio, llamado ________, se usaba para separar la plata de la roca.'),
    ('item', '6. Al regreso, las flotas se reunían en el puerto de ________ antes de cruzar el Atlántico.'),
    ('item', '7. El comercio prohibido, hecho a escondidas, se llama ________.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) El Paraguay estaba totalmente al margen de la economía de la plata.'),
    ('item', '9. (....) La mita minera fue organizada por el virrey Francisco de Toledo en la década de 1570.'),
    ('item', '10. (....) Buenos Aires era el principal puerto autorizado para la plata en el siglo XVII.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. ¿Por qué creció el contrabando por Buenos Aires a pesar de las prohibiciones?', 4),
    ('item', '12. Escribí un texto de 6 a 8 líneas sobre la plata de Potosí. Se tendrá en cuenta: dónde y cuándo se descubrió '
             '(1 punto), cómo se organizaba el trabajo (1 punto), una consecuencia para los indígenas (1 punto) y cómo se vinculaba '
             'el Paraguay con Potosí (1 punto).', 8),
]

PLAN = {
    'material': 'Tomo: Clase 14 (Figura 14.1); planisferio',
    'tema': C.TEMAS['H6a'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes expliquen las transformaciones económicas de la América colonial y ubiquen al Paraguay en ese sistema.',
    'funciones': {
        'Esenciales': 'En clase: Ubicate; fuente (preguntas 1 a 3); actividades 1, 2, 3, 4 y 11.',
        'Consolidación': 'Actividades 5, 6, 8 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 24).',
        'Complementarias o domiciliarias': 'Actividades 7, 10 y 12.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Continuación E. Pregunta: «¿De dónde salía la plata de las monedas que circulaban en Europa en el siglo XVII?».',
             'Proponen hipótesis.', 'Hipótesis en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–28', 'Lectura de «La plata: Potosí y Zacatecas» con la Figura 14.1.',
             'Resuelven el «Ubicate» y las actividades 1 y 2.', 'Ubicate y actividades 1 y 2 (esenciales).'),
            ('28–42', 'Lectura del cuadro «Haciendas y plantaciones».',
             'Resuelven la actividad 3.', 'Actividad 3 (esencial).'),
            ('42–60', 'Lectura de «El monopolio y el sistema de flotas» y de «El contrabando y el Paraguay». Explica el Concepto clave.',
             'Resuelven las actividades 4 y 11.', 'Actividades 4 y 11 (esenciales).'),
            ('60–80', 'Presenta la carta de Domingo de Santo Tomás y aclara que es una versión resumida.',
             'Responden las preguntas 1 a 3 de la fuente.', 'Fuente (esencial).'),
            ('80–100', 'Acompaña; quien termina antes sigue con la consolidación.', 'Resuelven las actividades 5, 6, 8 y 9.',
             'Actividades de consolidación.'),
        ]),
        ('Cierre', [
            ('100–120', 'Puesta en común de la actividad 11 y de la pregunta 3 de la fuente. Lee los criterios de la actividad 12 y asigna la tarea.',
             'Corrigen con otro color.', 'Actividad 11 revisada.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en el mapa: el docente traza con tiza en un planisferio el recorrido de la plata desde Potosí hasta Sevilla.',
        'Apoyo en la actividad 11: dos causas escritas en la pizarra para completar («Buenos Aires estaba lejos de…», «Los productos que llegaban por Portobelo eran…»).',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: averiguar cuántos metros de altura tiene la ciudad de Potosí y cómo influía eso en la vida de los mitayos.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Lectura de mapa; cuadro comparativo; análisis de fuente; respuesta breve.',
        'instrumentos': 'Lista de cotejo con los tres indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Describe la minería de la plata y la mita minera.',
                      'Diferencia la hacienda de la plantación.',
                      'Explica el monopolio, el contrabando y el vínculo del Paraguay con Potosí.'],
    },
    'precisiones': [
        'Error frecuente: «el Paraguay quedó al margen de la plata». Se vinculaba con Potosí vendiendo yerba, tabaco y lienzos.',
        'En la actividad del Ubicate se acepta «oeste» o «noroeste»: Potosí está al noroeste de Asunción.',
        'La carta de Santo Tomás va en versión resumida; solo la expresión «boca del infierno» se presenta entre comillas.',
    ],
    'tarea': 'Actividades 7, 10 y 12 de la Clase 14.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente', [
            ('F1', 'Las minas de plata de Potosí. Usa esa expresión porque allí muchos indígenas sufrían y morían.', ''),
            ('F2', 'Que remedie la situación de los indígenas obligados a trabajar en las minas.', ''),
            ('F3', 'Que el trabajo ya era muy duro y causaba muertes antes de que la mita lo organizara; con la mita, el trabajo forzado '
                   'se volvió sistemático y alcanzó a más pueblos.', 'Se acepta una respuesta que relacione las dos fechas.'),
        ]),
        ('Ubicate (Figura 14.1)', [
            ('U', 'Potosí está al noroeste de Asunción. La plata iba de Potosí al Callao, por mar a Panamá, de allí a Portobelo, y luego '
                  'con los galeones a La Habana y Sevilla.', 'Se acepta «oeste» o «noroeste».'),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'd) Potosí y Zacatecas', ''),
            ('2', 'b) el trabajo obligatorio por turnos de indígenas en las minas', ''),
            ('3', 'a) producía un solo producto para exportar con trabajo esclavizado', ''),
            ('4', 'c) solo podían comerciar con España', ''),
        ]),
        ('Completá los espacios', [
            ('5', 'azogue', ''),
            ('6', 'La Habana', ''),
            ('7', 'contrabando', ''),
        ]),
        ('Verdadero o falso', [
            ('8', 'Falso: vendía yerba, tabaco y lienzos que llegaban hasta Potosí.', 'Justificación obligatoria.'),
            ('9', 'Verdadero.', ''),
            ('10', 'Falso: no era un puerto autorizado para el gran comercio; por allí salía plata de contrabando.', 'Justificación obligatoria.'),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'Porque Buenos Aires estaba mucho más cerca de Potosí y de Europa que el camino oficial por Portobelo, y los productos '
                   'que llegaban por la ruta legal eran escasos y muy caros. Comerciantes portugueses, holandeses e ingleses ofrecían '
                   'mercaderías y esclavizados a cambio de plata.', 'Dos razones correctas.'),
            ('12', 'Ejemplo: «La plata de Potosí, en el Alto Perú, se descubrió en 1545. Desde la década de 1570, la mita obligaba a miles '
                   'de indígenas a trabajar por turnos en las minas, donde muchos morían. El Paraguay no tenía minas, pero vendía yerba '
                   'a Potosí y así participaba del comercio de la plata.»',
             'Criterio anunciado en la consigna: dónde y cuándo se descubrió (1 punto), cómo se organizaba el trabajo (1 punto), una '
             'consecuencia para los indígenas (1 punto) y cómo se vinculaba el Paraguay con Potosí (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Potosí 1545; Zacatecas 1546; Huancavelica; mita de Toledo (década de 1570)', 'Fechas habituales; cotejar.'),
    ('Carta de fray Domingo de Santo Tomás (1550) y la expresión «boca del infierno»', 'Versión resumida; cotejar la expresión y la fecha con una edición de la carta.'),
    ('Sistema de flotas (Veracruz, Cartagena, Portobelo, Callao, La Habana); aduana de Córdoba (1622)', 'Datos habituales; cotejar.'),
    ('Trazados de la Figura 14.1', 'Esquema aproximado de la editorial.'),
]

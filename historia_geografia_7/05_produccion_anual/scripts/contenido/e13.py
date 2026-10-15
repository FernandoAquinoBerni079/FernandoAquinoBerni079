"""Encuentro 13 — Continuación C: rutas, decisiones y alianzas (H3; temas H3a y H3b).

Taller de consolidación de la Clase 8: el tomo trae el cuadro de datos de las
expediciones y la Ficha reproducible C con el mapa mudo, para que la consigna
de mapa se pueda resolver sin material externo.
"""
import curriculo as C

TITULO = 'Continuación C — Rutas, decisiones y alianzas en el Río de la Plata'
CLAVE = 'Continuación C —'
INDICADORES = [
    'Representa en un mapa histórico las expediciones de García, Gaboto y Mendoza-Ayolas, con leyenda.',
    'Compara Buenos Aires y Asunción como bases de la conquista con datos de ubicación, recursos y alianzas.',
    'Explica las causas y consecuencias de las decisiones de los conquistadores entre 1524 y 1541.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H3'], C.TEMAS['H3a'] + ' ' + C.TEMAS['H3b'], INDICADORES),
    ('h2', 'Del relato al análisis'),
    ('p', 'En la Clase 8 leíste cómo llegaron los europeos al Río de la Plata y cómo nació Asunción. En este taller vas a '
          'trabajar con esa información de tres maneras: en un mapa (¿por dónde fueron?), en un cuadro comparativo (¿por qué una '
          'ciudad y no otra?) y en una cadena de decisiones (¿qué decidieron y qué consecuencias tuvo?).'),
    ('h2', 'Los datos que vas a usar'),
    ('tabla', ['Expedición', 'Cuándo', 'Recorrido aproximado', 'Qué buscaba y qué resultado tuvo'],
     [['Alejo García', 'Hacia 1524', 'De la isla de Santa Catalina, por el Guairá, al río Paraguay y a Charcas.',
       'Los metales del oeste. Llegó a la frontera inca y murió al volver.'],
      ['Sebastián Gaboto', '1526-1530', 'Del Río de la Plata por el Paraná y el Paraguay; fuerte de Sancti Spiritus.',
       'Iba a Asia y cambió de rumbo por la plata. El fuerte fue destruido en 1529.'],
      ['Pedro de Mendoza y Juan de Ayolas', '1536-1537', 'Buenos Aires; luego, río arriba por el Paraná y el Paraguay hasta Candelaria y el Chaco.',
       'Poblar la región y llegar a la Sierra de la Plata. Ayolas murió al volver del Chaco.'],
      ['Juan de Salazar y Espinosa', '1537', 'Del Paraná al río Paraguay, en busca de Ayolas.',
       'Levantó la casa fuerte de Asunción, en tierra de los carios.']],
     [2.6, 1.6, 3.2, 3.2]),
    ('caja', 'concepto', 'Concepto clave — ',
     'Una alianza es un acuerdo entre grupos que se necesitan. Para los carios, aliarse con los españoles era sumar fuerza '
     'contra sus enemigos y crear lazos de parentesco; para los españoles, era la única manera de conseguir alimentos y '
     'trabajo. La alianza fue desigual: con el tiempo, los españoles impusieron sus condiciones.'),

    ('h2', 'Consignas del taller'),
    ('p', 'Trabajá en parejas. Usá la Ficha reproducible C, el cuadro de datos y las Figuras 8.1 y 8.2 de la Clase 8.'),
    ('consigna', 'Consignas del taller:'),
    ('item', '1. En el mapa mudo de la Ficha C: marcá con un punto y escribí el nombre de la isla de Santa Catalina, Sancti '
             'Spiritus, Buenos Aires, Asunción y Potosí (Charcas). Dibujá con tres colores los recorridos de Alejo García, de '
             'Gaboto y de Mendoza-Ayolas. Completá el título y la leyenda.'),
    ('item', '2. Completá el cuadro comparativo de Buenos Aires y Asunción.'),
    ('cuadro', ['Criterio', 'Buenos Aires (1536)', 'Asunción (1537)'],
     ['Ubicación', 'Alimentos', 'Relación con los pueblos del lugar', 'Distancia a las tierras de la plata', 'Qué pasó en 1541'],
     [3.2, 3.4, 3.4], 1.4),
    ('item', '3. Completá la cadena de decisiones: escribí por qué se tomó cada decisión y qué consecuencia tuvo.'),
    ('cuadro', ['Decisión', '¿Por qué la tomó?', '¿Qué consecuencia tuvo?'],
     ['Gaboto cambia de rumbo (1526)', 'Mendoza envía a Ayolas río arriba (1536)', 'Salazar levanta una casa fuerte entre los carios (1537)',
      'Irala despuebla Buenos Aires (1541)'],
     [3.2, 3.4, 3.4], 1.5),
    ('item', '4. Escribí un comentario de 6 a 8 líneas: ¿por qué Asunción, y no Buenos Aires, se convirtió en el centro de la '
             'conquista del Río de la Plata? Se tendrá en cuenta: dos causas con datos del cuadro (2 puntos), una consecuencia '
             'para la región (1 punto) y el uso de conectores de causa como «porque» o «por eso» (1 punto).', 8),
    ('h3', 'Revisión entre pares del mapa'),
    ('p', 'Intercambiá tu Ficha C con otra pareja. Marcá cada criterio y escribí una sugerencia breve.'),
    ('tabla', ['Criterio', 'Sí', 'No', 'Sugerencia'],
     [['Tiene un título que dice qué muestra y de qué años.', '', '', ''],
      ['Los cinco lugares están marcados y nombrados.', '', '', ''],
      ['Cada recorrido tiene un color distinto.', '', '', ''],
      ['La leyenda explica todos los colores y símbolos.', '', '', '']],
     [4.6, 0.9, 0.9, 3.6]),
    ('h3', 'Autoevaluación del taller'),
    ('tabla', ['Criterio', 'Lo logré', 'En proceso', 'Todavía no'],
     [['Mi mapa tiene título, lugares, recorridos y leyenda.', '', '', ''],
      ['Comparé las dos ciudades con datos.', '', '', ''],
      ['Expliqué por qué se tomó cada decisión.', '', '', ''],
      ['Usé conectores de causa en mi comentario.', '', '', '']],
     [5.5, 1.5, 1.5, 1.5]),
]

FICHAS = [
    ('ficha_repro', 'Ficha reproducible C — Mapa mudo del Río de la Plata y del Paraguay',
     [('p', 'Título del mapa: ______________________________________________'),
      ('fig', 'ficha_C_mapa_mudo.png', 'Mapa mudo para la consigna 1. Elaboración propia con datos de Natural Earth (dominio público); mapa aproximado.', 15.0),
      ('cuadro', ['Leyenda: color o símbolo', 'Qué representa'], ['', '', '', '', ''], [3.0, 7.0], 0.9)]),
]

PLAN = {
    'material': 'Tomo: Continuación C; Ficha reproducible C (una por pareja, preparada antes del encuentro); Figuras 8.1 y 8.2; lápices de tres colores',
    'tema': C.TEMAS['H3a'] + ' ' + C.TEMAS['H3b'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes organicen en un mapa, un cuadro y una cadena de decisiones lo estudiado sobre la conquista '
                 'del Río de la Plata y expliquen con causas la centralidad de Asunción.',
    'funciones': {
        'Esenciales': 'En clase: consignas 1, 2 y 4 del taller; Ficha C.',
        'Consolidación': 'Consigna 3 y autoevaluación del taller (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 14).',
        'Complementarias o domiciliarias': 'Pasar en limpio el comentario causal si quedó en borrador (optativo).',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 8. Pregunta: «¿Qué necesitaba un grupo de españoles para sobrevivir lejos del mar?».',
             'Responden con lo estudiado.', 'Ideas en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–20', 'Lee el cuadro de datos y el Concepto clave de alianza.',
             'Subrayan en cada fila el recorrido y el resultado.', 'Datos subrayados.'),
            ('20–48', 'Entrega la Ficha C y modela con tiza el primer tramo del recorrido de García.',
             'Resuelven la consigna 1 en parejas.', 'Ficha C (esencial).'),
            ('48–68', 'Acompaña el cuadro comparativo; recuerda usar las Figuras 8.1 y 8.2.',
             'Resuelven la consigna 2.', 'Cuadro comparativo (esencial).'),
            ('68–80', 'Explica con la primera fila cómo se arma una cadena de decisiones.',
             'Resuelven la consigna 3.', 'Consigna 3 (consolidación).'),
            ('80–100', 'Lee los criterios de la consigna 4 y acompaña la escritura.',
             'Escriben el comentario.', 'Consigna 4 (esencial).'),
        ]),
        ('Cierre', [
            ('100–113', 'Organiza la revisión entre pares del mapa y la lectura de dos comentarios; el grupo comprueba causas y conectores.',
             'Revisan el mapa de otra pareja y corrigen el propio.', 'Revisión entre pares; comentarios revisados.'),
            ('113–120', 'Explica la autoevaluación y asigna lo que quedó pendiente.',
             'Completan la autoevaluación.', 'Autoevaluación.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en el mapa: algunas copias de la Ficha C llevan marcados con un punto los cinco lugares; el estudiante escribe los nombres.',
        'Apoyo en el comentario: comienzo dado «Asunción se convirtió en el centro porque…, en cambio Buenos Aires…».',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: agregar al mapa el recorrido de Cabeza de Vaca en 1541-1542 desde la costa del Brasil hasta Asunción.',
    ],
    'evaluacion': {
        'tipo': 'Formativa, con producto.',
        'procedimientos': 'Mapa histórico; cuadro comparativo; cadena de decisiones; comentario causal.',
        'instrumentos': 'Ficha C; revisión entre pares; autoevaluación; consigna 4 con los criterios de su consigna.',
        'criterios': ['El mapa tiene título, cinco lugares, tres recorridos diferenciados y leyenda.',
                      'El cuadro compara las dos ciudades con datos correctos.',
                      'El comentario da dos causas, una consecuencia y usa conectores de causa.'],
    },
    'precisiones': [
        'Los recorridos que dibujan los estudiantes son aproximados, como los de la Figura 8.1; no se evalúa precisión del trazado.',
        'La alianza con los carios se presenta como desigual: no idealizarla como amistad ni reducirla a sometimiento.',
    ],
    'tarea': 'Terminar la consigna 3 y la autoevaluación si quedaron pendientes.',
}

SOL = {
    'bloques': [
        ('Consignas del taller', [
            ('1', 'Santa Catalina en la costa atlántica del Brasil; Sancti Spiritus sobre el Paraná; Buenos Aires en el Río de la Plata; '
                  'Asunción sobre el río Paraguay; Potosí al noroeste, en Charcas. García: de la costa al oeste, cruzando el Paraguay, '
                  'hasta Charcas. Gaboto: del Río de la Plata por el Paraná y el Paraguay. Mendoza-Ayolas: de Buenos Aires río arriba '
                  'hasta el Chaco.',
             'Lista de cotejo: título; cinco lugares; tres recorridos con colores distintos; leyenda completa. Se compara con la Figura 8.1.'),
            ('2', 'Ubicación: Buenos Aires junto al estuario, lejos de Charcas; Asunción sobre el río Paraguay, más al norte. Alimentos: en '
                  'Buenos Aires, hambre; en Asunción, abundantes por la agricultura guaraní. Relación: en Buenos Aires, enfrentamientos; '
                  'en Asunción, alianza con los carios. Distancia: Asunción más cerca del camino a la plata. 1541: Buenos Aires se '
                  'despuebla; en Asunción se forma el Cabildo.',
             'Una casilla por criterio y ciudad; se aceptan expresiones equivalentes.'),
            ('3', 'Gaboto: supo de la plata en la costa del Brasil; descubrió los grandes ríos y levantó Sancti Spiritus. Mendoza: buscaba '
                  'la Sierra de la Plata y en Buenos Aires había hambre; Ayolas fundó Candelaria y murió en el Chaco. Salazar: buscaba a '
                  'Ayolas y necesitaba un lugar seguro con alimentos; nació Asunción. Irala: Buenos Aires no se sostenía y Asunción '
                  'tenía alimentos y aliados; Asunción quedó como centro de la conquista.',
             'Por qué y consecuencia de cada fila; se aceptan otras consecuencias estudiadas en la Clase 8.'),
            ('4', 'Ejemplo: «Asunción se convirtió en el centro porque tenía alimentos gracias a la agricultura de los carios y porque '
                  'contaba con su alianza, mientras que en Buenos Aires había hambre y enfrentamientos. Además, estaba más cerca del '
                  'camino a la plata. Por eso, en 1541 Irala despobló Buenos Aires y desde Asunción salieron expediciones que fundaron '
                  'otras ciudades.»',
             'Criterio anunciado en la consigna: dos causas con datos del cuadro (2 puntos), una consecuencia para la región (1 punto) '
             'y el uso de conectores de causa como «porque» o «por eso» (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Recorridos del cuadro de datos y del mapa mudo', 'Síntesis de la Clase 8; trazados aproximados (ver VERIFICACION de la Clase 8).'),
]

# -*- coding: utf-8 -*-
"""Referencias para el docente (hallazgo COM-02 del dictamen de Work sobre 88a0970).

Solo se listan ediciones, páginas y enlaces identificados. Cuando una fuente se usa en el tomo pero su edición no
fue cotejada, se dice «edición por cotejar»: no se inventan ediciones ni páginas.
Uso en el libro: «cita textual» (entre comillas, palabra por palabra), «versión escolar» (resumen o adaptación
declarada en el tomo), «síntesis» (explicación propia de la editorial apoyada en la fuente) o «dato» (cifra o hecho).
"""

INTRO = ('Esta lista permite rehacer el cotejo de las fuentes y los datos que el tomo usa. La columna «Uso en el libro» '
         'distingue la cita textual de la versión escolar resumida o adaptada y de la síntesis editorial. Las fuentes '
         'marcadas «edición por cotejar» se usan como versiones escolares: antes de una edición comercial hay que '
         'cotejarlas con una edición identificada.')

# (tema, referencia, uso en el libro, estado)
REFERENCIAS = [
    ('Poblamiento: White Sands (Clase 4)',
     'Pigati, J. S. y otros (2023). «Independent age estimates resolve the controversy of ancient human footprints at '
     'White Sands». Science 382, 73-75. DOI 10.1126/science.adh5007.',
     'Dato', 'Identificada'),
    ('Arqueología regional y teorías del poblamiento (Clase 4 y Continuación B)',
     'Síntesis de manuales y de la bibliografía arqueológica (Monte Verde: Dillehay).',
     'Síntesis', 'Edición por cotejar'),
    ('Colón, diario del primer viaje (Clase 6)', 'Fragmento resumido.', 'Versión escolar', 'Edición por cotejar'),
    ('Cortés, cartas de relación (Clases 5 y 6)', 'Fragmento resumido.', 'Versión escolar', 'Edición por cotejar'),
    ('Requerimiento (Clase 6)', 'Fragmento resumido.', 'Versión escolar', 'Edición por cotejar'),
    ('Schmidl, relato del viaje al Río de la Plata (Clase 3 y Continuación A)', 'Fragmento resumido.', 'Versión escolar', 'Edición por cotejar'),
    ('Real Provisión de 1537 (Clase 10)',
     'Fragmento 1: transcripción citada por Portal Guaraní (portalguarani.com). Fragmento 2: adaptación escolar declarada.',
     'Cita textual (fragmento 1); adaptación (fragmento 2)', 'Cotejo paleográfico pendiente'),
    ('Testamento de Domingo Martínez de Irala (Clase 9)', 'Fragmento resumido.', 'Versión escolar', 'Edición por cotejar'),
    ('Levantamientos de Aracaré y Tabaré, 1542-1543 (Clase 9 e Integradora 1)',
     'Roulet, F. (1990). Cuadernos Americanos 2(20), 205-228.',
     'Síntesis', 'Identificada'),
    ('Síntesis sobre la sociedad guaraní (Clase 3)', 'Síntesis de la bibliografía etnohistórica (Melià, Susnik).',
     'Síntesis', 'Obra y páginas por cotejar'),
    ('Ordenanzas de Alfaro (Clase 12)',
     'Rivarola Paoli, J. B. El sistema de las encomiendas (Portal Guaraní). Ordenanzas dadas en Asunción en 1611; no '
     'confundir con las disposiciones de Tucumán de 1612.',
     'Versión escolar', 'Fuente identificada; texto por cotejar'),
    ('Sínodo de Asunción de 1603 (Clase 13)',
     '«Los primitivos catecismos hispanoamericanos». Revista Teología LIX/139 (2022), 193-220, p. 213 (portal.amelica.org).',
     'Versión escolar', 'Identificada'),
    ('Antonio Ruiz de Montoya, Conquista espiritual, 1639 (Clase 13 y Continuación E)',
     'ISARM: «Antonio Ruiz de Montoya y su legado» (infomontoya.isparm.edu.ar). Exilio de 1631, obra y contexto.',
     'Versión escolar', 'Contexto identificado; paráfrasis por cotejar con la edición de 1639'),
    ('Fray Domingo de Santo Tomás, carta de 1550 sobre Potosí (Clase 14)', 'Carta al Consejo de Indias (1550). Fragmento resumido; solo «boca del infierno» va entre comillas.', 'Versión escolar', 'Edición por cotejar'),
    ('Olaudah Equiano (Clase 15)',
     'Equiano, O. (1789). The Interesting Narrative, cap. 2 (extracto en history.hanover.edu). El tomo indica que el texto '
     'es posterior a los hechos.',
     'Versión escolar', 'Identificada'),
    ('Jamaica, 1655 (Clase 15)',
     'Royal Museums Greenwich: ocupación inglesa de una colonia española, 1655 (rmg.co.uk).',
     'Dato', 'Identificada'),
    ('Yerba mate: rutas de comercialización (Clase 12)',
     'Hilgert, N., Stampella, P., Pochettino, M. L. y Hernández Bermejo, J. E. (eds.) (2022). Las Misiones del Noreste '
     'Argentino. EDUNaM / Universidad de Córdoba, cap. VIII, p. 227 (editorial.unam.edu.ar).',
     'Síntesis', 'Identificada'),
    ('São Paulo en el planalto (Continuación E)',
     'Prefeitura de São Paulo: documento municipal sobre disponibilidad hídrica (participemais.prefeitura.sp.gov.br).',
     'Dato', 'Identificada'),
    ('Límite con Bolivia: río Negro u Otuquis (Clase 16)',
     'Ministerio de Relaciones Exteriores del Paraguay: «Paraguay y Bolivia aprueban la demarcación final de su frontera '
     'común» (mre.gov.py): 704 km terrestres y 38 km fluviales sobre el río Negro. CNDL-MRE: relevamiento para la '
     'cartografía del río Negro u Otuquis (www2.mre.gov.py). En el mapa, solo se marca la confluencia aproximada.',
     'Dato', 'Identificada'),
    ('Lluvias: normales 1971-2000 (Clase 19 y Continuación G)',
     'Grassi, B. (2020). Estado del Clima Paraguay 2019. MADES-STP, p. 20 impresa (p. 22 del PDF), fig. 7 '
     '(transparenciaclimatica.mades.gov.py): aprox. 600 a 1.800 mm anuales.',
     'Dato', 'Identificada'),
    ('Bosques de la Región Oriental (Clases 20 y 21)',
     'Ley 2524/2004 y su prórroga por la Ley 6676/2020, que prohíbe las actividades de transformación y conversión de '
     'superficies con cobertura de bosques (bacn.gov.py). La fecha de caducidad no se afirma sin cotejo.',
     'Dato', 'Identificada; vigencia a cotejar antes de cada edición'),
]

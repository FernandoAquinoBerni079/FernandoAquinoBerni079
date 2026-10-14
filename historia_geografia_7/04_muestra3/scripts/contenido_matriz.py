"""Matriz curricular de los 36 encuentros.

Programa: MEC (2014), Programa de Estudio: Historia y Geografía - 7.º grado,
EEB (reproducción en PDF, 92 págs., SHA-256 389190d3…c8d27e). Capacidades y
temas transcriptos de las págs. 55 a 57.
"""

CAPACIDADES = {
    'H1': 'Reconoce los procesos fundamentales que configuran la prehistoria paraguaya.',
    'H2': 'Interpreta las características destacadas de la prehistoria americana.',
    'H3': 'Investiga los principales acontecimientos que caracterizan la realidad paraguaya del siglo XVI.',
    'H4': 'Identifica los hechos relevantes del siglo XVI que incidieron en las transformaciones del contexto americano.',
    'H5': 'Analiza los rasgos relevantes que influyeron en la realidad paraguaya del siglo XVII.',
    'H6': 'Describe los rasgos históricos distintivos de la realidad americana del siglo XVII.',
    'G1': 'Analiza la posición geográfica de Paraguay y América y sus incidencias en las actividades humanas.',
    'G2': 'Relaciona las características de las unidades orohidrográficas de Paraguay y América.',
    'G3': 'Identifica las características climáticas de Paraguay y América y su influencia en las actividades humanas.',
    'G4': 'Describe las características de las regiones naturales de Paraguay y América.',
}

TEMAS = {
    'H1a': 'Antigüedad de los grupos humanos. Formaciones cazadoras-recolectoras y tribales.',
    'H1b': 'Primeros pobladores de las regiones Oriental y Occidental.',
    'H1c': 'Características de los guaraníes; importancia de la lengua guaraní.',
    'H2a': 'Antigüedad; teorías del origen del hombre americano.',
    'H2b': 'Aztecas, mayas e incas: territorios y aportes.',
    'H3a': 'Expediciones de Alejo García y Sebastián Gaboto.',
    'H3b': 'Conquista del Río de la Plata; Asunción como centro.',
    'H3c': 'Mestizaje; resistencia indígena; situación de los indígenas y de la mujer guaraní.',
    'H3d': 'Ejercicio del derecho a la autonomía (Real Provisión de 1537).',
    'H3e': 'Instituciones coloniales: Cabildo, Obispado, Encomienda (tipos).',
    'H4a': 'Avances tecnológicos y conocimientos geográficos.',
    'H4b': 'Llegada de los europeos: causas, consecuencias, mentalidad del conquistador.',
    'H4c': 'Distribución de los territorios; colonialismo español; repercusión.',
    'H4d': 'Absolutismo; autoridades en América; pertenencia al Virreinato del Perú.',
    'H5a': 'División de la Provincia; mediterraneidad.',
    'H5b': 'Sistema económico de la Provincia.',
    'H5c': 'Situación político-social de los aborígenes.',
    'H5d': 'Aportes de franciscanos y jesuitas.',
    'H6a': 'Haciendas, minería, comercio.',
    'H6b': 'Colonización inglesa, francesa y portuguesa.',
    'H6c': 'Situación de indígenas y negros; lucha por la libertad.',
    'G1a': 'Ubicación, límites y extensión de Paraguay y América.',
    'G1b': 'Posición absoluta y relativa de Paraguay y América.',
    'G1c': 'Posición geográfica y actividades de la población.',
    'G2a': 'Orografía de Paraguay y América; influencia en las actividades.',
    'G2b': 'Hidrografía de Paraguay y América; Hidrovía; impactos.',
    'G2c': 'Recursos naturales y necesidad de su preservación.',
    'G3a': 'Elementos y factores del clima.',
    'G3b': 'Tipos de clima de América; clima del Paraguay.',
    'G3c': 'Influencias del clima en las actividades humanas.',
    'G4a': 'Regiones naturales de América.',
    'G4b': 'Regiones naturales de Paraguay.',
    'G4c': 'Gestión ambiental del Estado paraguayo.',
    'G4d': 'Cambios y costes socio-ambientales del uso de la tierra.',
}

# (n, sección (como en el tomo), capacidad, temas, ampliación prevista o estado en la muestra 3)
ENCUENTROS = [
    (1, 'Clase 1', '—', [], 'Clase introductoria editorial (no hay capacidad del MEC para ella). Corregir la regla del siglo (años terminados en 00); citar la obra de Villoro.'),
    (2, 'Clase 2', 'H1', ['H1a', 'H1b'], 'Fuente arqueológica real (con autor); organización de los primeros pobladores del Chaco y de la Región Oriental; corregir el tuteo de la actividad 12.'),
    (3, 'Clase 3', 'H1', ['H1c'], 'Fuente con cronista identificado; papel de niños y mujeres; importancia de la lengua guaraní; antropofagia ritual tratada con contexto.'),
    (4, 'Continuación A', 'H1', ['H1c'], 'Usar la capacidad literal; incluir las fuentes del taller (hoy solo se describen).'),
    (5, 'Evaluación de la Unidad 1', 'H1', ['H1a', 'H1b', 'H1c'], 'Ampliar a 60-70 min con ítems de fuente, mapa y desarrollo; claves balanceadas; ficha de evaluación.'),
    (6, 'Clase 4', 'H2', ['H2a'], 'Fechas y sitios con fuente (Monte Verde); fuente científica identificada.'),
    (7, 'Clase 5', 'H2', ['H2b'], 'Corregir las chinampas (no flotaban); fechas de mayas, mexicas e incas; mapa de territorios con datos reales; crónica identificada.'),
    (8, 'Continuación B', 'H2', ['H2a', 'H2b'], 'Agregar la tabla de fechas para la línea de tiempo comparativa; mapa base reproducible.'),
    (9, 'Evaluación de la Unidad 2', 'H2', ['H2a', 'H2b'], 'Corregir la clave de las chinampas; ampliar y balancear claves.'),
    (10, 'Clase 6', 'H4', ['H4a', 'H4b'], 'Reemplazar el «diario de un navegante» inventado por un fragmento del Diario de Colón con referencia; mentalidad del conquistador.'),
    (11, 'Clase 7', 'H4', ['H4c', 'H4d'], 'Corregir la opción múltiple con dos respuestas; absolutismo sin contradicciones; Virreinato del Perú (1542) con fecha.'),
    (12, 'Clase 8', 'H3', ['H3a', 'H3b'], 'Pedro de Mendoza, Ayolas e Irala explicados; despoblamiento de Buenos Aires (1541); Cabildo de 1541.'),
    (13, 'Continuación C', 'H3', ['H3a', 'H3b'], 'Explicar quiénes fueron Solís, García y Gaboto; mapa reproducible de rutas.'),
    (14, 'Clase 9', 'H3', ['H3c'], 'Fuente identificada; verificar la guarania y la UNESCO; resistencia indígena con casos.'),
    (15, 'Clase 10', 'H3', ['H3d', 'H3e'], 'MUESTRA 3: contexto de 1534-1556; dos fragmentos con su referencia; Irala hacia 1539 como debate historiográfico; tipos de cabildo y de encomienda; Obispado; Figura 10.1 (línea de tiempo nueva) y 10.2 (esquema); 16 actividades con criterios anunciados.'),
    (16, 'Continuación D', 'H3', ['H3d', 'H3e'], 'Evitar repetir la Clase 10: casos de aplicación (1539, 1544), lectura de los fragmentos y comparación con la elección actual.'),
    (17, 'Evaluación de la Unidad 3', 'H3, H4', ['H3a', 'H3b', 'H3c', 'H3d', 'H3e', 'H4a', 'H4b', 'H4c', 'H4d'], 'Agregar ítems de cronología y resistencia; corregir el ítem sobre la Real Provisión.'),
    (18, 'Integradora 1.ª etapa', 'H1, H2, H3, H4', [], 'Cubre las Unidades 1 a 3. Revisar ítems reciclados; escala de calificación.'),
    (19, 'Clase 11', 'H5', ['H5a'], 'Corregir la causalidad de la mediterraneidad (1617); Hernandarias; testimonio con fuente.'),
    (20, 'Clase 12', 'H5', ['H5b', 'H5c'], 'Ordenanzas de Alfaro (1611); yerba mate con fuente.'),
    (21, 'Clase 13', 'H5', ['H5d'], 'Diferenciar la protección de las reducciones jesuíticas y franciscanas; bandeirantes, pérdida del Guairá y Mbororé.'),
    (22, 'Continuación E', '— (ampliación)', [], 'AMPLIACIÓN EDITORIAL (siglo XVIII): la Guerra Guaranítica no figura en el programa MEC 2014, cuyo alcance son los siglos XVI y XVII (pág. 54). Núcleo recomendado para el encuentro: bandeirantes, pérdida del Guairá y Mbororé (H5, tema H5d); la Guerra Guaranítica, como ampliación optativa.'),
    (23, 'Clase 14', 'H6', ['H6a'], 'Potosí con fuente identificada; monopolio y contrabando.'),
    (24, 'Clase 15', 'H6', ['H6b', 'H6c'], 'Desarrollar la colonización portuguesa; Kamba Kua con el origen correcto (1820).'),
    (25, 'Evaluación de la Unidad 4', 'H5, H6', ['H5a', 'H5b', 'H5c', 'H5d', 'H6a', 'H6b', 'H6c'], 'Ítems sobre la Clase 14; jesuitas expulsados de los dominios españoles (1767).'),
    (26, 'Clase 16', 'G1', ['G1a', 'G1b', 'G1c'], 'Posición de América (falta); longitud en la posición absoluta; Laudo Hayes (1878); dato con fuente (INE o IGM).'),
    (27, 'Clase 17', 'G2', ['G2a'], 'Serranías del Paraguay con nombres; relieve de América; fuente real.'),
    (28, 'Clase 18', 'G2', ['G2b', 'G2c'], 'MUESTRA 3: cuencas y vertientes; río Paraguay como límite; afluentes; lagos, esteros y acuíferos; hidrografía de América; 2 mapas con escala, leyenda y límites legibles en blanco y negro; ficha reproducible; 15 actividades con criterios anunciados.'),
    (29, 'Continuación F', 'G2', ['G2b', 'G2c'], 'MUESTRA 3: remite al mapa de la Hidrovía de la Clase 18; evaluación de impacto ambiental; caso con zona de notas, tarjetas de rol recortables y matriz en fichas reproducibles; la decisión se califica solo en la Ficha F-C, con la rúbrica de 8 puntos impresa en la consigna 4; autoevaluación.'),
    (30, 'Evaluación de la Unidad 5', 'G1, G2', ['G1a', 'G1b', 'G2a', 'G2b', 'G2c'], 'MUESTRA 3: 14 ítems en 6 partes (28 puntos); los dos mapas impresos en la prueba; criterios de puntaje en cada parte; tiempo adicional sin devolución de claves hasta el encuentro 31.'),
    (31, 'Clase 19', 'G3', ['G3a', 'G3b', 'G3c'], 'Capacidad abreviada en el maestro: usar la literal. Corregir el «Ubicate» del Trópico y la clave de la fuente; tipos de clima de América; tabla climática con datos de la DMH.'),
    (32, 'Clase 20', 'G4', ['G4a', 'G4b', 'G4d'], 'Chaco Húmedo y Chaco Seco; regiones de América desarrolladas; costes del uso de la tierra.'),
    (33, 'Clase 21', 'G4', ['G4c'], 'Capacidad literal completa; artículos 7 y 8 de la Constitución; SEAM y MADES; Ley 294/1993.'),
    (34, 'Continuación G', 'G3, G4', ['G3b', 'G4b', 'G4c'], 'Agregar el mapa, la tabla climática y la ficha del proyecto que pide el taller.'),
    (35, 'Evaluación de la Unidad 6', 'G3, G4', ['G3a', 'G3b', 'G3c', 'G4a', 'G4b', 'G4c', 'G4d'], 'Claves balanceadas; ítems sobre América; análisis de datos.'),
    (36, 'Integradora 2.ª etapa', 'H5, H6, G1, G2, G3, G4', [], 'Cubre las Unidades 4 a 6. El ítem 3 del maestro evalúa la Continuación E (ampliación editorial): en la producción, reemplazarlo por un ítem de H5 o marcarlo como optativo. Ítems nuevos (hoy 5 de 6 son copias); escala.'),
]

MUESTRA3 = {15: 'Clase 10', 28: 'Clase 18', 29: 'Continuación F', 30: 'EVALUACIÓN DE LA UNIDAD 5'}

RECURSOS_M3 = {
    15: 'Fig. 10.1 (línea de tiempo nueva) y 10.2 (esquema nuevo); la figura original del maestro se retiró; fuente documental con dos fragmentos y referencias; cuadro comparativo; tabla de tipos de encomienda.',
    28: 'Fig. 18.1, 18.2 y 18.3 (mapas nuevos con datos de Natural Earth; la figura de la Hidrovía del maestro se reemplazó); cuadro de ríos; fuente cartográfica; Ficha reproducible 18-A.',
    29: 'Remite a la Fig. 18.2 (mapa de la Hidrovía); cuadro de tres dimensiones; Fichas reproducibles F-A (caso), F-B (roles) y F-C (matriz); autoevaluación.',
    30: 'Mapa mudo (Parte C) y mapa numerado de América (Parte D) impresos en la prueba; cuadros para completar; criterios de puntaje en cada parte.',
}


# Tipo de vínculo curricular de cada encuentro (tercera muestra).
# - Capacidad literal MEC: el encuentro desarrolla temas del programa bajo una capacidad citada literalmente.
# - Asociación curricular: el encuentro no tiene capacidad propia; integra o evalúa capacidades literales.
# - Formulación editorial: propósito redactado por la editorial, sin capacidad del programa.
# - Ampliación editorial: contenido que el programa no exige.
VINCULOS = ('Capacidad literal MEC', 'Asociación curricular', 'Formulación editorial', 'Ampliación editorial')


def vinculo(n, seccion):
    if n == 1:
        return 'Formulación editorial'
    if n == 22:
        return 'Ampliación editorial'
    if seccion.startswith(('Evaluación', 'Integradora')):
        return 'Asociación curricular'
    return 'Capacidad literal MEC'


# Estado de la ficha en el maestro del 3 de octubre, corregido respecto del JSON de la muestra 2:
# la Clase 19 está abreviada (no es una formulación editorial) y las evaluaciones no tienen ficha
# (el JSON de la muestra 2 les asignaba «H1» con coincidencia 0).
ESTADO_FICHA = {'literal': 'Literal', 'truncada': 'Truncada', 'variante': 'Variante', 'editorial': 'Editorial',
                'abreviada': 'Abreviada', 'sin_ficha': 'Sin ficha'}


def estado_ficha(seccion, cot):
    if not cot or not cot['cap_tomo']:
        return 'sin_ficha'
    if seccion.startswith('Clase 19'):
        return 'abreviada'
    return cot['estado']

"""Arquitectura curricular de la producción anual (36 encuentros).

Programa: MEC (2014), Programa de Estudio: Historia y Geografía, 7.º grado,
EEB. Reproducción en PDF aportada por Fernando (92 págs., SHA-256
389190d3…c8d27e). Capacidades y temas transcriptos de las págs. 55 a 57;
alcance histórico (prehistoria y siglos XVI y XVII) en la pág. 54; tres horas
cátedra semanales de 40 minutos en la pág. 46.

Los códigos H1-H6 y G1-G4 y las letras de los temas (H1a, H1b…) son
identificadores editoriales de esta colección, no códigos oficiales del MEC.
La división en 36 encuentros es arquitectura editorial: 21 clases, 7
continuaciones, 6 evaluaciones de unidad y 2 integradoras de etapa.
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

PAGINA_CAPACIDAD = {'H1': 55, 'H2': 55, 'H3': 55, 'H4': 56, 'H5': 56, 'H6': 56, 'G1': 56, 'G2': 57, 'G3': 57, 'G4': 57}

# Temas del programa, transcriptos literalmente (págs. 55 a 57)
TEMAS = {
    'H1a': 'Antigüedad de los grupos humanos. Formaciones o sociedades cazadoras-recolectoras y formaciones tribales.',
    'H1b': 'Primeros pobladores de las regiones Oriental y Occidental. Organización política, social, económica y religiosa.',
    'H1c': 'Características de los guaraníes. Espacio territorial ocupado, organización basada en la reciprocidad y el '
           'parentesco, papel cumplido por los niños y las mujeres en la familia y la sociedad, elementos constitutivos de '
           'la religión, antropofagia, cultura material y legado. Importancia de la lengua guaraní.',
    'H2a': 'Antigüedad de los grupos humanos. Teorías acerca del origen del hombre americano.',
    'H2b': 'Espacios territoriales ocupados y aportes culturales de los aztecas, mayas e incas.',
    'H3a': 'Trascendencia de la expedición de Alejo García y de Sebastián Gaboto.',
    'H3b': 'Características de la conquista en el Río de la Plata. Asunción como centro de la conquista del Río de la Plata.',
    'H3c': 'Mestizaje hispano guaraní. Formas de resistencia indígena. Situación general de los indígenas y de la mujer guaraní.',
    'H3d': 'Ejercicio del derecho a la autonomía (Real Provisión del 12 de septiembre de 1537).',
    'H3e': 'Instituciones coloniales: Cabildo (tipos e importancia). Obispado. Encomienda (tipos y características).',
    'H4a': 'Importancia de los avances tecnológicos que permitieron aumentar los conocimientos geográficos.',
    'H4b': 'Llegada de los europeos a América. Causas y consecuencias. Mentalidad del conquistador europeo.',
    'H4c': 'Distribución de los territorios americanos entre las potencias europeas. Características del colonialismo '
           'español. Repercusión entre los naturales.',
    'H4d': 'Estados europeos con gobierno absolutista y su proyección en las colonias americanas. Autoridades políticas '
           'residentes en América. Adaptación de los naturales a las autoridades españolas. Pertenencia política del '
           'Paraguay al Virreinato del Perú.',
    'H5a': 'División del territorio de la Provincia del Paraguay. Causas y consecuencias. Secuelas de la mediterraneidad.',
    'H5b': 'Sistema económico implementado en los territorios de la Provincia del Paraguay.',
    'H5c': 'Situación político-social de los aborígenes.',
    'H5d': 'Aportes de los franciscanos y jesuitas en la constitución de la cultura paraguaya.',
    'H6a': 'Transformaciones económicas (establecimiento de haciendas, explotación minera, comercio).',
    'H6b': 'Características de la colonización inglesa, francesa y portuguesa.',
    'H6c': 'Situación de los indígenas y de los negros. Lucha por la libertad.',
    'G1a': 'Ubicación, límites y extensión de Paraguay y América.',
    'G1b': 'Posición absoluta y relativa de Paraguay y América.',
    'G1c': 'Interrelaciones entre la posición geográfica y las actividades desarrolladas por la población.',
    'G2a': 'Orografía de Paraguay y América. Formas que adquiere el relieve terrestre americano. Influencia de la '
           'orografía en las actividades humanas.',
    'G2b': 'Hidrografía de Paraguay y América. Importancia y utilidad de los cauces hídricos. Hidrovía Paraná-Paraguay. '
           'Impacto ecológico, social y económico.',
    'G2c': 'Potencialidad de los recursos naturales y necesidad de su preservación.',
    'G3a': 'Elementos del clima. Factores que influyen en el clima.',
    'G3b': 'Tipos de clima de América. Características climáticas del Paraguay.',
    'G3c': 'Influencias del clima en las actividades humanas.',
    'G4a': 'Regiones naturales de América. Principales características.',
    'G4b': 'Regiones naturales de Paraguay. Características diferenciadoras.',
    'G4c': 'Gestión ambiental desarrollada por el Estado paraguayo. Política nacional ambiental. Instituciones encargadas '
           'de velar por el medio ambiente. Normativas vigentes en relación al medio ambiente.',
    'G4d': 'Cambios y costes socio-ambientales derivados del uso de la tierra.',
}

UNIDADES = {
    1: 'Unidad 1 — Cómo mirar el tiempo y el espacio',
    2: 'Unidad 2 — La prehistoria americana',
    3: 'Unidad 3 — El Paraguay y América en el siglo XVI',
    4: 'Unidad 4 — Paraguay y América colonial: siglo XVII',
    5: 'Unidad 5 — El espacio geográfico: posición, relieve e hidrografía',
    6: 'Unidad 6 — Clima, regiones naturales y ambiente',
}

# Tipos de vínculo curricular
LITERAL, ASOCIACION, EDITORIAL, AMPLIACION = ('Capacidad literal MEC', 'Asociación curricular',
                                              'Formulación editorial', 'Ampliación editorial')

# (n, tipo, sección, unidad, capacidades, temas, vínculo)
# tipo: clase | continuacion | evaluacion | integradora
ENCUENTROS = [
    (1, 'clase', 'Clase 1', 1, [], [], EDITORIAL),
    (2, 'clase', 'Clase 2', 1, ['H1'], ['H1a', 'H1b'], LITERAL),
    (3, 'clase', 'Clase 3', 1, ['H1'], ['H1c'], LITERAL),
    (4, 'continuacion', 'Continuación A', 1, ['H1'], ['H1c'], LITERAL),
    (5, 'evaluacion', 'Evaluación de la Unidad 1', 1, ['H1'], [], ASOCIACION),
    (6, 'clase', 'Clase 4', 2, ['H2'], ['H2a'], LITERAL),
    (7, 'clase', 'Clase 5', 2, ['H2'], ['H2b'], LITERAL),
    (8, 'continuacion', 'Continuación B', 2, ['H2'], ['H2a', 'H2b'], LITERAL),
    (9, 'evaluacion', 'Evaluación de la Unidad 2', 2, ['H2'], [], ASOCIACION),
    (10, 'clase', 'Clase 6', 3, ['H4'], ['H4a', 'H4b'], LITERAL),
    (11, 'clase', 'Clase 7', 3, ['H4'], ['H4c', 'H4d'], LITERAL),
    (12, 'clase', 'Clase 8', 3, ['H3'], ['H3a', 'H3b'], LITERAL),
    (13, 'continuacion', 'Continuación C', 3, ['H3'], ['H3a', 'H3b'], LITERAL),
    (14, 'clase', 'Clase 9', 3, ['H3'], ['H3c'], LITERAL),
    (15, 'clase', 'Clase 10', 3, ['H3'], ['H3d', 'H3e'], LITERAL),
    (16, 'continuacion', 'Continuación D', 3, ['H3'], ['H3d', 'H3e'], LITERAL),
    (17, 'evaluacion', 'Evaluación de la Unidad 3', 3, ['H3', 'H4'], [], ASOCIACION),
    (18, 'integradora', 'Integradora 1.ª etapa', None, ['H1', 'H2', 'H3', 'H4'], [], ASOCIACION),
    (19, 'clase', 'Clase 11', 4, ['H5'], ['H5a'], LITERAL),
    (20, 'clase', 'Clase 12', 4, ['H5'], ['H5b', 'H5c'], LITERAL),
    (21, 'clase', 'Clase 13', 4, ['H5'], ['H5d'], LITERAL),
    (22, 'continuacion', 'Continuación E', 4, ['H5'], ['H5c', 'H5d'], LITERAL),
    (23, 'clase', 'Clase 14', 4, ['H6'], ['H6a'], LITERAL),
    (24, 'clase', 'Clase 15', 4, ['H6'], ['H6b', 'H6c'], LITERAL),
    (25, 'evaluacion', 'Evaluación de la Unidad 4', 4, ['H5', 'H6'], [], ASOCIACION),
    (26, 'clase', 'Clase 16', 5, ['G1'], ['G1a', 'G1b', 'G1c'], LITERAL),
    (27, 'clase', 'Clase 17', 5, ['G2'], ['G2a'], LITERAL),
    (28, 'clase', 'Clase 18', 5, ['G2'], ['G2b', 'G2c'], LITERAL),
    (29, 'continuacion', 'Continuación F', 5, ['G2'], ['G2b', 'G2c'], LITERAL),
    (30, 'evaluacion', 'Evaluación de la Unidad 5', 5, ['G1', 'G2'], [], ASOCIACION),
    (31, 'clase', 'Clase 19', 6, ['G3'], ['G3a', 'G3b', 'G3c'], LITERAL),
    (32, 'clase', 'Clase 20', 6, ['G4'], ['G4a', 'G4b', 'G4d'], LITERAL),
    (33, 'clase', 'Clase 21', 6, ['G4'], ['G4c'], LITERAL),
    (34, 'continuacion', 'Continuación G', 6, ['G3', 'G4'], ['G3b', 'G4b', 'G4c'], LITERAL),
    (35, 'evaluacion', 'Evaluación de la Unidad 6', 6, ['G3', 'G4'], [], ASOCIACION),
    (36, 'integradora', 'Integradora 2.ª etapa', None, ['H5', 'H6', 'G1', 'G2', 'G3', 'G4'], [], ASOCIACION),
]

BLOQUES = {1: range(1, 10), 2: range(10, 19), 3: range(19, 28), 4: range(28, 37)}


def encuentro(n):
    e = ENCUENTROS[n - 1]
    assert e[0] == n
    return dict(zip(('n', 'tipo', 'seccion', 'unidad', 'caps', 'temas', 'vinculo'), e))


def texto_capacidades(caps):
    return ' '.join(CAPACIDADES[c] for c in caps)


assert len(ENCUENTROS) == 36
assert sum(1 for e in ENCUENTROS if e[1] == 'clase') == 21
assert sum(1 for e in ENCUENTROS if e[1] == 'continuacion') == 7
assert sum(1 for e in ENCUENTROS if e[1] == 'evaluacion') == 6
assert sum(1 for e in ENCUENTROS if e[1] == 'integradora') == 2

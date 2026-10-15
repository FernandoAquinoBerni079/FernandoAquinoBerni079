# -*- coding: utf-8 -*-
"""Fuente única del caso conductor — Colegio Técnico Arapoty (institución y personas ficticias).

Todos los capítulos de la colección toman de acá los datos del caso: institución, personas, registros de
relevamiento numerados por línea (entrevistas E1 a E5, observación O1, documentos D1 y D2), necesidades
N-xx, interesados, reglas a negociar y alcance mínimo. Un código citado en el libro (E1-L4, O1-3, D1-A5,
N-02…) tiene que existir acá, y la cita textual tiene que coincidir con la línea: lo comprueban
caso/verificar_caso.py (contra el Capítulo 4 v2 y el candidato del Capítulo 2) y build/verificar.py
(contra los Capítulos 1 a 3).

Origen de los datos:
  - E1, E2, O1 y E3: candidato del Capítulo 2 (fase2_pilotos/A1_candidato_capitulo2), sin cambios en el texto.
  - E4 y E5: las líneas que cita el Capítulo 4 v2 se copian sin cambios; las preguntas del analista y las
    líneas E4-L11, E4-L12, E5-L7 y E5-L8 son nuevas.
  - D0, D1, D2, las necesidades y los datos de cada registro (fecha, lugar, autorización): nuevos en este lote.
  - Reglas e interesados: Capítulo 4 v2 y candidato del Capítulo 2. Alcance mínimo: informe de Work §7.2.
Ningún dato procede del caso de biblioteca de Algorítmica 3.º."""

INSTITUCION = 'Colegio Técnico Arapoty'
UBICACION = 'Colegio ficticio de gestión oficial, con Educación Escolar Básica (7.º a 9.º) y Bachillerato Técnico en Informática (1.º a 3.º BTI).'
AVISO_FICCION = ('La institución, las personas, las cifras y los diálogos del caso son inventados para este libro. '
                 'Cualquier parecido con una institución o una persona real es casual.')

# ------------------------------------------------------------------ personas
# código, nombre, rol. Los códigos P-xx se usan solo en la guía y en los controles.
PERSONAS = [
    ('P-01', 'Lic. Mirta Escobar', 'bibliotecaria'),
    ('P-02', 'Lic. Teresa Vega', 'directora'),
    ('P-03', 'Sr. Ramón Ibarra', 'encargado de informática'),
    ('P-04', 'Prof. Estela Duarte', 'docente de Castellano, responsable del plan lector'),
    ('P-05', 'Iván Ortellado', 'estudiante, delegado de 2.º BTI (lector)'),
]
NOMBRE = {c: n for c, n, _ in PERSONAS}

CASO_PRESENTACION = [
    'Durante todo el libro trabajamos con la biblioteca del Colegio Técnico Arapoty, un colegio ficticio. '
    'La atiende la Lic. Mirta Escobar, bibliotecaria. La directora es la Lic. Teresa Vega y el encargado de '
    'informática es el Sr. Ramón Ibarra. Todos los nombres, cifras y diálogos del caso son inventados para '
    'este libro.',
    'La biblioteca registra los préstamos en un cuaderno. Los lectores no siempre saben qué libros están '
    'disponibles, aparecen devoluciones que no se sabe a qué préstamo corresponden y cuesta reconstruir el '
    'historial. La bibliotecaria necesita registrar las operaciones y saber qué está vencido; los lectores '
    'necesitan saber qué hay; la dirección necesita información de conjunto para organizar el servicio.',
]

# ------------------------------------------------------------------ registros de relevamiento
# Cada registro: código, tipo, título, persona (o None), datos de contexto, líneas [(código, hablante, texto)].
# En las entrevistas, «hablante» es 'Analista' o el nombre de pila del entrevistado.
# El relevamiento lo hizo un equipo ficticio de 3.º BTI del mismo colegio: es el modelo del libro.

REGISTROS = [
    # D0 abre el proyecto (Capítulo 1): es el reto que la dirección le plantea al curso.
    dict(cod='D0', tipo='documento', titulo='Nota de la dirección al curso de 3.º BTI (pedido inicial)', persona='P-02',
         contexto='Nota firmada por la directora y entregada al curso al comenzar las clases. Se citan sus párrafos '
                   'por número: D0-3 es el párrafo 3.',
         lineas=[
             ('D0-1', None, 'La biblioteca registra los préstamos en un cuaderno, y cada vez cuesta más saber qué libros hay y quién los tiene.'),
             ('D0-2', None, 'Pedimos al curso de 3.º BTI que estudie el problema y proponga una mejora que el colegio pueda sostener.'),
             ('D0-3', None, 'Hace falta, al menos, que la bibliotecaria pueda registrar los préstamos y las devoluciones, y que la dirección reciba cada mes los préstamos por curso.'),
             ('D0-4', None, 'Algunos docentes sugieren comprar lectores de códigos de barras.'),
             ('D0-5', None, 'Toda propuesta debe cuidar los datos de los estudiantes y contar con la conformidad de la bibliotecaria.'),
             ('D0-6', None, 'El curso presentará el problema y el alcance de su propuesta en la sexta semana de clases.'),
         ]),
    dict(cod='E1', tipo='entrevista', titulo='Entrevista a la Lic. Mirta Escobar, bibliotecaria', persona='P-01',
         contexto='Primera semana de marzo, en la biblioteca, fuera del horario de recreo. Duración: 25 minutos. '
                  'La entrevistada autorizó tomar notas; no se grabó audio.',
         lineas=[
             ('E1-L1', 'Analista', '¿Cómo es un día normal en la biblioteca?'),
             ('E1-L2', 'Mirta', 'Abro a las siete, y en el primer recreo se llena. Anoto los préstamos en un cuaderno; cuando hay fila, anoto apurada y después no entiendo mi letra.'),
             ('E1-L3', 'Analista', '¿Qué pasa cuando un libro no vuelve?'),
             ('E1-L4', 'Mirta', 'Tengo que hojear el cuaderno hacia atrás hasta encontrar quién lo llevó. A veces tardo media hora. A fin de año faltan unos cuarenta libros y no sé quién los tiene.'),
             ('E1-L5', 'Analista', '¿Cómo sabe hoy si un libro está disponible?'),
             ('E1-L6', 'Mirta', 'Voy al estante. Si no está, puede estar prestado, mal ubicado o perdido.'),
             ('E1-L7', 'Analista', '¿Qué le pide la dirección?'),
             ('E1-L8', 'Mirta', 'Un informe a fin de cada mes con cuántos préstamos hubo por curso. Lo hago contando a mano y me lleva una tarde.'),
             ('E1-L9', 'Analista', 'Si pudiera cambiar una sola cosa, ¿cuál sería?'),
             ('E1-L10', 'Mirta', 'Saber al instante quién tiene cada libro. Y que el sistema sea fácil, porque yo no soy de computadoras.'),
             ('E1-L11', 'Analista', '¿No le parece que conviene una aplicación para el celular?'),
             ('E1-L12', 'Mirta', 'Si usted dice… sí, capaz.'),
         ]),
    dict(cod='E2', tipo='entrevista', titulo='Entrevista a la Prof. Estela Duarte, docente de Castellano', persona='P-04',
         contexto='Primera semana de marzo, en la sala de profesores. Duración: 15 minutos. La entrevistada autorizó '
                  'tomar notas.',
         lineas=[
             ('E2-L1', 'Analista', '¿Para qué usa la biblioteca con sus cursos?'),
             ('E2-L2', 'Estela', 'Para el plan lector: cada mes todo el curso lee la misma novela. Necesito treinta ejemplares juntos.'),
             ('E2-L3', 'Analista', '¿Cómo lo hace hoy?'),
             ('E2-L4', 'Estela', 'Le pido a Mirta con una semana de anticipación. Ella cuenta los ejemplares en el estante y a veces faltan cinco o seis.'),
             ('E2-L5', 'Analista', '¿Qué pasa cuando faltan?'),
             ('E2-L6', 'Estela', 'Algunos chicos leen en fotocopias o en el celular, y se atrasan.'),
             ('E2-L7', 'Analista', '¿Cuánto tiempo necesita los libros?'),
             ('E2-L8', 'Estela', 'Tres semanas, como mínimo. Y lo ideal sería que nadie más pueda llevar ese título mientras tanto.'),
             ('E2-L9', 'Analista', '¿Hay otra cosa que le complique?'),
             ('E2-L10', 'Estela', 'Cuando devuelven, Mirta tiene que contar uno por uno, y siempre aparece alguno que no es de la biblioteca.'),
             ('E2-L11', 'Estela', 'Ah, y el sistema tiene que ser rápido.'),
         ]),
    dict(cod='E3', tipo='entrevista', titulo='Entrevista a Iván Ortellado, delegado de 2.º BTI (lector)', persona='P-05',
         contexto='Segunda semana de marzo, en el patio, durante el segundo recreo. Duración: 5 minutos. El delegado '
                  'aceptó responder y su docente guía estaba informada. Se registraron solo sus respuestas.',
         lineas=[
             ('E3-L1', 'Iván', 'Vengo a buscar un libro y no sé si está.'),
             ('E3-L2', 'Iván', 'Pierdo el recreo esperando en la fila para que me digan que está prestado.'),
             ('E3-L3', 'Iván', 'Me gustaría saber antes de venir si lo hay.'),
             ('E3-L4', 'Iván', 'Y que se pueda renovar el préstamo sin traer el libro.'),
         ]),
    dict(cod='O1', tipo='observación', titulo='Observación en la biblioteca, martes, primer recreo', persona=None,
         contexto='Segunda semana de marzo. Dos observadores del equipo, sentados al fondo, sin intervenir. La '
                  'bibliotecaria sabía que se la iba a observar y lo autorizó. No se anotaron nombres de estudiantes.',
         lineas=[
             ('O1-1', None, 'Al tocar el timbre de salida al recreo había 14 estudiantes en fila.'),
             ('O1-2', None, 'La bibliotecaria registró 9 préstamos en el cuaderno durante el recreo.'),
             ('O1-3', None, '5 estudiantes se fueron sin libro cuando tocó el timbre de entrada.'),
             ('O1-4', None, '2 estudiantes pidieron un libro que según la bibliotecaria «tenía que estar», y no estaba en el estante.'),
         ]),
    dict(cod='D1', tipo='documento', titulo='Reglamento de la biblioteca (vigente, aprobado por la dirección)', persona=None,
         contexto='Hoja impresa pegada junto al mostrador. Copia facilitada por la bibliotecaria. Se citan sus artículos '
                  'por número: D1-A3 es el artículo 3.',
         lineas=[
             ('D1-A1', None, 'La biblioteca atiende de lunes a viernes, de 7:00 a 12:30.'),
             ('D1-A2', None, 'Pueden retirar libros los estudiantes y los docentes de la institución.'),
             ('D1-A3', None, 'El plazo de préstamo es de una semana. Los docentes pueden pedir un plazo mayor con autorización de la dirección.'),
             ('D1-A4', None, 'Cada préstamo se anota en el cuaderno de préstamos con el nombre del lector, su curso, el título y la fecha.'),
             ('D1-A5', None, 'Quien pierda o dañe un libro debe reponerlo.'),
             ('D1-A6', None, 'Todos los libros deben devolverse antes del cierre del año lectivo.'),
         ]),
    dict(cod='D2', tipo='documento', titulo='Informe mensual de préstamos por curso, mes de marzo', persona=None,
         contexto='Hoja manuscrita que la bibliotecaria entregó a la dirección. Copia facilitada por la bibliotecaria, '
                  'sin datos personales. Se citan sus renglones por número.',
         lineas=[
             ('D2-1', None, '7.º grado: 21 préstamos.'),
             ('D2-2', None, '8.º grado: 17 préstamos.'),
             ('D2-3', None, '9.º grado: 14 préstamos.'),
             ('D2-4', None, '1.º BTI: 19 préstamos.'),
             ('D2-5', None, '2.º BTI: 15 préstamos.'),
             ('D2-6', None, '3.º BTI: 11 préstamos.'),
             ('D2-7', None, 'Docentes: 9 préstamos.'),
             ('D2-8', None, 'Sin curso anotado: 6 préstamos.'),
             ('D2-9', None, 'Total del mes: 115 préstamos.'),
         ]),
    dict(cod='E4', tipo='entrevista', titulo='Segunda entrevista a la bibliotecaria', persona='P-01',
         contexto='Tercera semana de marzo, en la biblioteca. Duración: 20 minutos. Se preparó después de leer el '
                  'reglamento (D1), el informe de marzo (D2) y la observación O1. La entrevistada autorizó tomar notas.',
         lineas=[
             ('E4-L1', 'Analista', 'El reglamento dice que se anota el título. Cuando le devuelven un libro, ¿cómo encuentra el préstamo?'),
             ('E4-L2', 'Mirta', 'De las lecturas obligatorias tenemos varios ejemplares. Cuando me devuelven uno, no sé de cuál préstamo es, porque en el cuaderno solo anoto el título.'),
             ('E4-L3', 'Analista', 'El martes vimos que en el recreo había fila. ¿Alguna vez se equivocó al anotar con apuro?'),
             ('E4-L4', 'Mirta', 'En hora pico me pasó de anotar el mismo libro a dos chicos distintos, y después no sabía cuál de los dos lo tenía.'),
             ('E4-L5', 'Analista', '¿Qué pasa con los lectores que ya no están en el colegio?'),
             ('E4-L6', 'Mirta', 'A los que ya se fueron del colegio no les presto. Pero siguen en el cuaderno y no los puedo borrar, porque ahí está lo que se llevaron.'),
             ('E4-L7', 'Analista', '¿Quién debería poder anotar o cambiar un préstamo?'),
             ('E4-L8', 'Mirta', 'Solo yo, o quien me reemplace, debería anotar préstamos. Los chicos pueden mirar qué hay, pero no tocar los registros.'),
             ('E4-L9', 'Analista', 'Si se cambiara la forma de registrar, ¿en qué equipo trabajaría?'),
             ('E4-L10', 'Mirta', 'Trabajaría en la computadora de la biblioteca, que es vieja y no siempre tiene internet.'),
             ('E4-L11', 'Analista', 'En el informe de marzo, la suma de los cursos da 112 y el total dice 115. ¿Cómo arma el informe?'),
             ('E4-L12', 'Mirta', 'Cuento hoja por hoja y sumo a mano; algún mes me equivoco. Los que no tienen curso los pongo aparte, porque no sé de dónde son.'),
         ]),
    dict(cod='E5', tipo='entrevista', titulo='Entrevista a la Lic. Teresa Vega, directora', persona='P-02',
         contexto='Tercera semana de marzo, en la dirección. Duración: 15 minutos. La entrevistada autorizó tomar notas '
                  'y pidió revisar el registro antes de que se use.',
         lineas=[
             ('E5-L1', 'Analista', '¿Qué información necesita de la biblioteca?'),
             ('E5-L2', 'Teresa', 'Necesito saber cada mes cuántos préstamos hubo por curso, para organizar las horas de biblioteca.'),
             ('E5-L3', 'Analista', '¿Con qué recursos cuenta el colegio para mejorar el registro de préstamos?'),
             ('E5-L4', 'Teresa', 'No hay presupuesto para comprar programas ni para pagar un servicio en internet.'),
             ('E5-L5', 'Analista', '¿Hay algo que le preocupe de registrar los préstamos de otra forma?'),
             ('E5-L6', 'Teresa', 'Los datos de los estudiantes no pueden quedar a la vista de cualquiera.'),
             ('E5-L7', 'Analista', '¿Quién decide las reglas de préstamo, como el plazo?'),
             ('E5-L8', 'Teresa', 'El reglamento lo aprobó la dirección, pero se puede revisar si la bibliotecaria y los docentes proponen un cambio.'),
         ]),
]
REGISTRO = {r['cod']: r for r in REGISTROS}
LINEA = {cod: (hab, txt) for r in REGISTROS for cod, hab, txt in r['lineas']}
TEXTO = {cod: txt for cod, (_, txt) in LINEA.items()}

# Diferencia del informe D2: los renglones D2-1 a D2-8 suman 112, el total escrito dice 115 (E4-L11).
D2_SUMA_RENGLONES = 112
D2_TOTAL_ESCRITO = 115

# ------------------------------------------------------------------ necesidades (cierre del Capítulo 2)
# código, enunciado, fuentes, estado. N-02 es el primer eslabón de la cadena de trazabilidad de Work §7.3
# y de la Figura 4.2 del Capítulo 4.
NECESIDADES = [
    ('N-01', 'Saber en todo momento qué lector tiene cada ejemplar prestado.', ['E1-L4', 'E1-L10'], 'Confirmada'),
    ('N-02', 'Evitar entregar a dos lectores el mismo ejemplar.', ['E4-L4'], 'Confirmada'),
    ('N-03', 'Saber, antes de ir al mostrador, si hay un ejemplar disponible de un título.', ['E3-L1', 'E3-L3', 'E1-L6', 'O1-3'], 'Confirmada'),
    ('N-04', 'Registrar un préstamo en hora pico sin que el dato quede ilegible.', ['E1-L2', 'O1-1', 'O1-2'], 'Confirmada'),
    ('N-05', 'Saber a qué préstamo corresponde cada ejemplar devuelto.', ['E4-L2', 'E2-L10', 'D1-A4'], 'Confirmada'),
    ('N-06', 'Obtener cada mes los préstamos por curso sin contar a mano y sin errores de suma.', ['E1-L8', 'E5-L2', 'D2-9', 'E4-L12'], 'Confirmada'),
    ('N-07', 'Que los datos personales de los lectores no queden a la vista de cualquiera.', ['E5-L6'], 'Confirmada'),
    ('N-08', 'Que solo la bibliotecaria o su reemplazo registren o modifiquen préstamos.', ['E4-L8'], 'Confirmada'),
    ('N-09', 'Dejar de prestar a quien ya no está en el colegio sin perder lo que se llevó.', ['E4-L6'], 'Confirmada'),
    ('N-10', 'Trabajar con lo que hay: la computadora de la biblioteca, sin internet seguro y sin gastos.', ['E4-L10', 'E5-L4'], 'Confirmada'),
    ('N-11', 'Que la bibliotecaria pueda usar la nueva forma de registro sin ayuda.', ['E1-L10'], 'Ambigua: «fácil» hay que precisarlo'),
    ('N-12', 'Disponer de unos treinta ejemplares de un título durante tres semanas para el plan lector.', ['E2-L2', 'E2-L8', 'D1-A3'], 'En conflicto con el plazo del reglamento'),
    ('N-13', 'Renovar un préstamo sin llevar el libro.', ['E3-L4'], 'Pedido de un lector; falta acordar la regla'),
]
NECESIDAD = {c: t for c, t, _, _ in NECESIDADES}

# Necesidades que nadie dijo y que muestran la observación o los documentos (sección 2.3).
NO_EXPRESADAS = [
    ('O1-3', 'Cinco de catorce estudiantes se fueron sin libro. Nadie mencionó en las entrevistas a los lectores '
             'que abandonan la fila: es una demanda que hoy no queda registrada.'),
    ('D2-8', 'Seis préstamos de marzo no tienen curso. El informe por curso que pide la dirección (E5-L2) no puede '
             'ser exacto si el curso del lector no se anota siempre.'),
    ('D2-9', 'Los renglones del informe suman 112 y el total escrito dice 115. Contar a mano produce errores que '
             'nadie había mencionado como problema.'),
]

# ------------------------------------------------------------------ interesados (Capítulo 1, sección 1.3)
# Mapa de interés e influencia (0 a 10), trasladado del candidato del Capítulo 2 sin cambios en los valores.
INTERESADOS = [
    ('Bibliotecaria', 9, 8, 'Usa el sistema todo el día; nadie lo adopta si ella no lo acepta.', 'Gestionar de cerca'),
    ('Directora', 4, 9, 'No lo usa a diario, pero aprueba gastos y reglas.', 'Mantener satisfecha'),
    ('Encargado de informática', 2.5, 6.5, 'Decide qué se instala en las computadoras.', 'Mantener satisfecho'),
    ('Docentes', 6.5, 3.6, 'Piden lotes de libros para sus cursos.', 'Mantener informados'),
    ('Estudiantes', 8.5, 2.2, 'Son los que más piden libros; individualmente deciden poco.', 'Mantener informados'),
    ('Familias', 2.5, 1.5, 'Se enteran por sus hijos; no usan el sistema.', 'Observar'),
]

# ------------------------------------------------------------------ reglas
# Texto de las reglas iniciales para negociar en clase (Work §7.2). Supuestos didácticos del proyecto:
# no son normas del MEC ni políticas de una biblioteca real. El Capítulo 3 las presenta SIN numerar;
# la numeración RN-01 a RN-06 se usa desde el Capítulo 4 (texto idéntico al del Capítulo 4 v2).
REGLAS = [
    ('RN-01', 'Un ejemplar solo puede tener un préstamo activo.'),
    ('RN-02', 'Cada lector puede tener como máximo dos préstamos activos.'),
    ('RN-03', 'El plazo inicial de préstamo es de siete días.'),
    ('RN-04', 'Los lectores inactivos no reciben nuevos préstamos.'),
    ('RN-05', 'La devolución no elimina el préstamo: queda en el historial.'),
    ('RN-06', 'No se borran lectores ni ejemplares con historial: se inactivan.'),
]

# ------------------------------------------------------------------ alcance mínimo (Work §7.2)
ALCANCE_NUCLEO = [
    ('Catálogo y ejemplares', 'Distingue la descripción del libro (título, autor, edición) de cada ejemplar físico y muestra su disponibilidad.'),
    ('Lectores', 'Registra lectores ficticios con un código interno y los datos mínimos del caso.'),
    ('Préstamo', 'Registra un ejemplar para un lector habilitado, con fecha de vencimiento, y lo valida antes de guardarlo.'),
    ('Devolución', 'Cierra el préstamo correcto una sola vez y conserva su historial.'),
    ('Consultas', 'Lista préstamos activos, vencidos y ejemplares disponibles.'),
    ('Permisos mínimos', 'La consulta del catálogo no permite modificar préstamos; las operaciones requieren un rol autorizado.'),
    ('Persistencia y entrega', 'Conserva la información entre usos y puede instalarse y restaurarse siguiendo una guía.'),
]
FUERA_DEL_NUCLEO = ['pagos y multas', 'catálogo nacional', 'códigos de barras', 'reservas en línea',
                    'notificaciones externas', 'aplicación móvil nativa', 'múltiples sedes', 'publicación pública']

# ------------------------------------------------------------------ datos que el lote no puede usar
# Personas y títulos del caso de biblioteca de Algorítmica 3.º (Práctica 5) y de su matriz ponderada (Práctica 4).
PROHIBIDOS_ALGORITMICA = ['Lucía Ortiz', 'Lucia Ortiz', 'Marcos Rojas', 'Ana Paula Vera', 'Hijo de hombre',
                          'El trueno entre las hojas', 'La babosa', 'Yo el Supremo', 'Roa Bastos', 'Casaccia',
                          'Kotlin', 'C#', 'Biblioteca.accdb']


def citar(cod):
    """Texto citable de un código: línea de registro, necesidad o regla."""
    if cod in TEXTO:
        return TEXTO[cod]
    if cod in NECESIDAD:
        return NECESIDAD[cod]
    return dict(REGLAS)[cod]


def existe(cod):
    return cod in TEXTO or cod in NECESIDAD or cod in dict(REGLAS)

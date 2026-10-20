# -*- coding: utf-8 -*-
"""Fuente única del caso para la Unidad II — Colegio Técnico Arapoty (caso ficticio).

Amplía `lote_1/caso/dossier.py` (que no se modifica y se importa tal cual) con lo que la Unidad II agrega al caso:
  - el catálogo de requisitos v1.0 del Capítulo 4, los pedidos postergados y el buzón de pedidos B-01 a B-08,
    trasladados del Capítulo 4 v2 (`fase2_pilotos/A2_capitulo4_v2/build/contenido.py`) SIN cambios de texto;
  - la correspondencia entre requisitos y criterios de aceptación de la guía v2.1, más la fila RNF-04 que agrega la
    especificación de evidencia C3;
  - la trazabilidad necesidad → regla → requisito → caso de uso → criterio → prueba prevista (Capítulo 6) y las pruebas
    previstas P-01 a P-15 (P-07 es la de Work §7.3);
  - el documento D3 (nota de la dirección con un cambio de regla), la solicitud de cambio SC-01 y la versión v1.1 del
    catálogo que resulta de ella.
lote_2/build/verificar.py comprueba que el catálogo, los postergados y el buzón son idénticos a los del piloto, que toda
fuente citada existe y que la trazabilidad no cita requisitos, reglas, necesidades ni pruebas inexistentes."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(ADS, 'lote_1', 'caso'))
import dossier as D

# ------------------------------------------------------------------ catálogo v1.0 (Capítulo 4, Tabla 4.3)
# (id, tipo, enunciado, fuentes, prioridad). Texto idéntico al del Capítulo 4 v2.
CATALOGO = [
    ('RF-01', 'Funcional', 'El sistema debe registrar cada préstamo con el ejemplar, el lector y la fecha de salida.', ['E1-L2', 'E4-L2'], 'Imprescindible'),
    ('RF-02', 'Funcional', 'El sistema debe calcular la fecha de vencimiento de cada préstamo según el plazo vigente.', ['RN-03'], 'Imprescindible'),
    ('RF-03', 'Funcional', 'El sistema debe registrar la devolución identificando el ejemplar devuelto y su préstamo.', ['E4-L2', 'RN-05'], 'Imprescindible'),
    ('RF-04', 'Funcional', 'El sistema debe rechazar el préstamo de un ejemplar que ya tiene un préstamo activo.', ['E4-L4', 'RN-01'], 'Imprescindible'),
    ('RF-05', 'Funcional', 'El sistema debe rechazar un nuevo préstamo a un lector que ya alcanzó el máximo vigente de préstamos activos.', ['RN-02'], 'Imprescindible'),
    ('RF-06', 'Funcional', 'El sistema debe rechazar préstamos a lectores inactivos.', ['E4-L6', 'RN-04'], 'Imprescindible'),
    ('RF-07', 'Funcional', 'El sistema debe permitir a cualquier lector consultar si hay ejemplares disponibles de un título.', ['E3-L1', 'E3-L3', 'E1-L6'], 'Imprescindible'),
    ('RF-08', 'Funcional', 'El sistema debe mostrar a la bibliotecaria qué lector tiene cada ejemplar prestado.', ['E1-L4', 'E1-L10'], 'Imprescindible'),
    ('RF-09', 'Funcional', 'El sistema debe informar la cantidad de préstamos de cada curso en un mes elegido.', ['E1-L8', 'E5-L2'], 'Importante'),
    ('RF-10', 'Funcional', 'El sistema debe permitir inactivar un lector o un ejemplar sin borrar su historial.', ['E4-L6', 'RN-06'], 'Imprescindible'),
    ('RNF-01', 'Calidad: uso', 'La bibliotecaria debe poder registrar un préstamo y una devolución sin ayuda, después de una práctica guiada.', ['E1-L10'], 'Importante'),
    ('RNF-02', 'Calidad: seguridad', 'Solo la bibliotecaria o su reemplazo autorizado deben poder registrar o modificar préstamos.', ['E4-L8'], 'Imprescindible'),
    ('RNF-03', 'Calidad: privacidad', 'La consulta pública no debe mostrar datos personales de los lectores.', ['E5-L6'], 'Imprescindible'),
    ('RS-01', 'Restricción', 'El sistema debe funcionar en la computadora de la biblioteca sin conexión a internet.', ['E4-L10'], 'Imprescindible'),
    ('RS-02', 'Restricción', 'La solución no debe requerir licencias ni servicios pagos.', ['E5-L4'], 'Imprescindible'),
]
REQ = {r[0]: r for r in CATALOGO}
POSTERGADOS = [
    ('E3-L4', 'Renovar el préstamo sin traer el libro', 'Deseable', 'El circuito de préstamo y devolución funciona sin esto; exige además una regla nueva de renovación. Se lleva al Capítulo 6.'),
]

# ------------------------------------------------------------------ buzón de pedidos (Práctica 4)
# Datos nuevos del mismo caso, no usados en los ejemplos resueltos (decisión de Fernando: opción A).
BUZON_TITULO = 'Buzón de pedidos de la biblioteca (caso ficticio)'
BUZON = [
    ('B-01', 'Docente de Lengua', 'Quiero ver qué libros tiene prestados cada alumno de mi curso.'),
    ('B-02', 'Auxiliar de la tarde', 'Cuando un libro vuelve roto, quiero anotarlo para que no se preste hasta arreglarlo.'),
    ('B-03', 'Estudiante de 1.º', 'El sistema tiene que avisar rápido si el libro está.'),
    ('B-04', 'Dirección', 'Necesito impresos los préstamos por curso de cada mes.'),
    ('B-05', 'Estudiante de 3.º', 'Hagan una app con inicio de sesión de Google.'),
    ('B-06', 'Bibliotecaria', 'Que no se pueda prestar nada a quien tenga un libro vencido.'),
    ('B-07', 'Encargado de informática', 'Tiene que funcionar en la computadora de la biblioteca aunque se corte internet.'),
    ('B-08', 'Docente de Historia', 'Los datos de los alumnos tienen que estar protegidos, y todos tienen que poder ver todo.'),
]
PEDIDO = {c: t for c, _, t in BUZON}

# ------------------------------------------------------------------ criterios de aceptación (guía v2.1, sección 3)
# Origen: MODELO (resuelto en el libro), ESTUDIANTE (lo escribe el estudiante), DOCENTE (referencia de la guía).
CORRESPONDENCIA = [
    ('RF-01', 'DOCENTE', 'Guía (referencia)',
     'Dado un ejemplar disponible y un lector activo sin préstamos, cuando la bibliotecaria registra el préstamo con '
     'fecha de salida 2 de marzo, entonces la lista de préstamos activos muestra ese ejemplar por su código, ese lector '
     'y esa fecha.'),
    ('RF-02', 'MODELO', 'Tabla 4.5',
     'Dado un préstamo registrado el 2 de marzo con el plazo de RN-03, cuando se consulta su vencimiento, entonces '
     'figura el 9 de marzo.'),
    ('RF-03', 'DOCENTE', 'Guía (referencia)',
     'Dado un ejemplar con un préstamo activo, cuando se registra su devolución indicando el código del ejemplar, '
     'entonces se cierra ese préstamo, con la fecha de devolución, y el ejemplar vuelve a figurar como disponible.'),
    ('RF-04', 'MODELO', 'Ejemplo resuelto 4.3 (CA-04)',
     'Dado un ejemplar con un préstamo activo, cuando se intenta registrar otro préstamo de ese ejemplar, entonces el '
     'sistema rechaza la operación, muestra el motivo y el ejemplar sigue teniendo un solo préstamo activo, el original.'),
    ('RF-05', 'ESTUDIANTE', 'Encuentro 8, Actividad 2',
     'Dado un lector con el máximo vigente de préstamos activos (dos, según RN-02), cuando se intenta registrarle otro, '
     'entonces el sistema lo rechaza, muestra el motivo y el lector sigue con dos préstamos activos.'),
    ('RF-06', 'ESTUDIANTE', 'Encuentro 8, Actividad 2',
     'Dado un lector inactivo, cuando se intenta registrarle un préstamo, entonces se rechaza con el motivo y no se crea '
     'ningún préstamo.'),
    ('RF-07', 'MODELO', 'Tabla 4.5',
     'Dado un título con un ejemplar disponible y otro prestado, cuando un lector sin sesión lo consulta, entonces ve '
     '«1 disponible» y ningún nombre de lector.'),
    ('RF-08', 'DOCENTE', 'Guía (referencia)',
     'Dados tres ejemplares prestados a tres lectores distintos, cuando la bibliotecaria consulta los préstamos activos, '
     'entonces ve, para cada ejemplar, el nombre del lector que lo tiene.'),
    ('RF-09', 'MODELO', 'Tabla 4.5',
     'Dado un mes con préstamos de tres cursos, cuando se pide el informe de ese mes, entonces aparece cada curso con su '
     'cantidad y la suma coincide con el total de préstamos del mes.'),
    ('RF-10', 'DOCENTE', 'Guía (referencia)',
     'Dado un lector con dos préstamos en el historial, cuando se lo inactiva, entonces deja de figurar entre los '
     'lectores habilitados y sus dos préstamos siguen en el historial.'),
    ('RNF-01', 'MODELO', 'Ejemplo resuelto 4.4, paso 4',
     'Dada la bibliotecaria después de una práctica guiada de 30 minutos (a confirmar con ella), cuando registra tres '
     'préstamos y dos devoluciones de una lista preparada, entonces completa las cinco operaciones sin pedir ayuda y '
     'sin errores de carga.'),
    ('RNF-02', 'DOCENTE', 'Guía (referencia)',
     'Dada una persona sin sesión de bibliotecaria, cuando intenta registrar o devolver un préstamo, entonces la '
     'operación se rechaza y no se crea ni se modifica ningún préstamo.'),
    ('RNF-03', 'ESTUDIANTE', 'Encuentro 8, Actividad 5 (Desafío)',
     'Dado un préstamo activo de un lector, cuando una persona sin sesión consulta el catálogo y busca ese título, '
     'entonces ve la cantidad de ejemplares disponibles y no ve el nombre, el curso ni el código del lector.'),
    ('RS-01', 'MODELO', 'Tabla 4.5',
     'Dada la computadora de la biblioteca desconectada de internet, cuando se registra un préstamo y una devolución, '
     'entonces ambas operaciones se completan y quedan guardadas.'),
    ('RS-02', 'DOCENTE', 'Guía (referencia)',
     'Dada la lista de componentes necesarios para instalar y usar el sistema, cuando se revisa la licencia de cada '
     'uno, entonces ninguno exige pago ni suscripción.'),
]
# Especificación de evidencia C3, §3: fila nueva de la consigna común de la Práctica 4.
CORRESPONDENCIA_C3 = ('RNF-04 (buzón, B-03)', 'ESTUDIANTE', 'Práctica 4, consigna común',
                      'Dado un título con ejemplares cargados y la computadora de la biblioteca en uso normal, cuando un '
                      'lector lo busca por su título cinco veces seguidas, entonces el resultado aparece cada vez en '
                      'menos de 3 segundos.')
ETIQUETA = {'MODELO': 'Modelo resuelto en el libro', 'ESTUDIANTE': 'Trabajo del estudiante',
            'DOCENTE': 'Referencia para el docente'}
DONDE_CA = {r[0]: (r[1], r[2]) for r in CORRESPONDENCIA}

# ------------------------------------------------------------------ pruebas previstas (se diseñan en los Capítulos 14 a 16)
PRUEBAS = [
    ('P-01', 'RF-01', 'Registrar un préstamo válido y verlo en la lista de préstamos activos.'),
    ('P-02', 'RF-02', 'Registrar un préstamo el 2 de marzo y comprobar que vence el 9 de marzo.'),
    ('P-03', 'RF-03', 'Devolver un ejemplar prestado: el préstamo se cierra, queda en el historial y el ejemplar figura disponible.'),
    ('P-04', 'RF-08', 'Consultar los préstamos activos y comprobar quién tiene cada ejemplar.'),
    ('P-05', 'RF-06', 'Intentar un préstamo a un lector inactivo: rechazo con motivo y sin préstamo nuevo.'),
    ('P-06', 'RF-05', 'Intentar un préstamo a un lector que ya tiene el máximo vigente: rechazo con motivo.'),
    ('P-07', 'RF-04', 'Enviar una segunda solicitud sobre el ejemplar recién prestado; verificar el rechazo y que no existe un segundo préstamo activo.'),
    ('P-08', 'RF-07', 'Consultar sin sesión un título con un ejemplar disponible y otro prestado.'),
    ('P-09', 'RF-09', 'Pedir el informe de un mes y comprobar que la suma por curso coincide con el total.'),
    ('P-10', 'RF-10', 'Inactivar un lector con historial y comprobar que su historial se conserva.'),
    ('P-11', 'RNF-02', 'Intentar registrar un préstamo sin sesión de bibliotecaria: rechazo.'),
    ('P-12', 'RNF-03', 'Hacer la consulta pública y comprobar que no aparece ningún dato personal.'),
    ('P-13', 'RS-01', 'Registrar un préstamo y una devolución con la computadora desconectada de internet.'),
    ('P-14', 'RNF-01', 'Sesión de uso con la bibliotecaria después de la práctica guiada.'),
    ('P-15', 'RS-02', 'Revisar la licencia de cada componente necesario para instalar y usar el sistema.'),
]
PRUEBA = {p: (r, t) for p, r, t in PRUEBAS}

# ------------------------------------------------------------------ trazabilidad (Capítulo 6, Tabla 6.3)
# requisito, necesidades, reglas, caso de uso (y paso o flujo), prueba prevista.
# «—» en necesidades: el requisito sale de una regla, no de un pedido. CU-04 y CU-05 están en el diagrama de casos de
# uso (Figura 5.4) pero no se desarrollan en el Capítulo 5: es una omisión visible que la matriz muestra.
TRAZABILIDAD = [
    ('RF-01', ['N-04'], [], 'CU-01, paso 6', 'P-01'),
    ('RF-02', [], ['RN-03'], 'CU-01, pasos 6 y 7', 'P-02'),
    ('RF-03', ['N-05'], ['RN-05'], 'CU-02, paso 4', 'P-03'),
    ('RF-04', ['N-02'], ['RN-01'], 'CU-01, flujo 5a', 'P-07'),
    ('RF-05', [], ['RN-02'], 'CU-01, flujo 4b', 'P-06'),
    ('RF-06', ['N-09'], ['RN-04'], 'CU-01, flujo 4a', 'P-05'),
    ('RF-07', ['N-03'], [], 'CU-03, paso 4', 'P-08'),
    ('RF-08', ['N-01'], [], 'CU-02, paso 2', 'P-04'),
    ('RF-09', ['N-06'], [], 'CU-04 (sin desarrollar)', 'P-09'),
    ('RF-10', ['N-09'], ['RN-06'], 'CU-05 (sin desarrollar)', 'P-10'),
    ('RNF-01', ['N-11'], [], 'CU-01 y CU-02 (todo el escenario)', 'P-14'),
    ('RNF-02', ['N-08'], [], 'CU-01 y CU-02, precondición', 'P-11'),
    ('RNF-03', ['N-07'], [], 'CU-03, paso 4 y flujo 4a', 'P-12'),
    ('RS-01', ['N-10'], [], 'Todos (entorno)', 'P-13'),
    ('RS-02', ['N-10'], [], 'Todos (entorno)', 'P-15'),
]

# ------------------------------------------------------------------ cambio de regla (Capítulo 6, sección 6.4)
REGISTROS_U2 = [
    dict(cod='D3', tipo='documento', titulo='Nota de la dirección a la biblioteca (préstamos para el aula)', persona='P-02',
         contexto='Nota firmada por la directora, entregada a la bibliotecaria y al curso de 3.º BTI en la semana del '
                  'Encuentro 11. Copia facilitada por la bibliotecaria. Se citan sus párrafos por número.',
         lineas=[
             ('D3-1', None, 'A partir del mes próximo, los docentes podrán retirar hasta cinco libros a la vez, para usarlos con su curso en el aula.'),
             ('D3-2', None, 'Para los estudiantes, el máximo sigue siendo de dos préstamos activos.'),
             ('D3-3', None, 'Pedimos al curso de 3.º BTI que revise qué cambia en su propuesta antes de seguir con el diseño.'),
         ]),
]
REGISTRO = dict(D.REGISTRO, **{r['cod']: r for r in REGISTROS_U2})
TEXTO = dict(D.TEXTO, **{c: t for r in REGISTROS_U2 for c, _, t in r['lineas']})
TEXTO.update(PEDIDO)

SC01 = [
    ('Identificador', 'SC-01'),
    ('Quién la pide y cuándo', 'La directora, Lic. Teresa Vega, por nota (D3), en la semana del Encuentro 11.'),
    ('Qué se pide', 'Que los docentes puedan tener hasta cinco préstamos activos; los estudiantes siguen con dos (D3-1, D3-2).'),
    ('Por qué', 'Los docentes usan libros con su curso en el aula (D3-1). Es un cambio de regla: lo decide la dirección (E5-L8).'),
    ('Reglas afectadas', 'RN-02 cambia de texto.'),
    ('Requisitos afectados', 'RF-05 no cambia de texto, porque dice «el máximo vigente», pero el máximo pasa a depender del tipo de lector. Hace falta un requisito nuevo: el sistema tiene que saber si cada lector es estudiante o docente (RF-11).'),
    ('Casos de uso afectados', 'CU-01: el paso 4 compara con el máximo del tipo de lector; el flujo 4b muestra ese máximo en el motivo del rechazo.'),
    ('Criterios y pruebas afectados', 'El criterio de RF-05 necesita dos situaciones (estudiante con dos préstamos y docente con cinco). P-06 se desdobla en P-06a y P-06b.'),
    ('Impacto en el plan', 'Incremento 2 (lectores): un dato más del lector. Incremento 3 (préstamo): la comprobación del máximo. Estimación: media HC más en cada uno.'),
    ('Decisión', 'Aceptada por la dirección, con la conformidad de la bibliotecaria. Se registra en la bitácora.'),
    ('Nueva versión', 'Catálogo v1.1 y modelos v1.1 (CU-01). Las versiones v1.0 se conservan.'),
]
REGLA_V11 = ('RN-02', 'Cada lector puede tener como máximo dos préstamos activos; los docentes, hasta cinco.')
RF11 = ('RF-11', 'Funcional', 'El sistema debe registrar si cada lector es estudiante o docente.', ['D3-1', 'D3-2'], 'Imprescindible')
CAMBIOS_V11 = [
    ('RN-02', 'Modificada', 'Agrega el máximo de los docentes (D3-1).'),
    ('RF-05', 'Sin cambio de texto', 'El «máximo vigente» ahora depende del tipo de lector; cambian los datos de su criterio y de P-06.'),
    ('RF-11', 'Nuevo', 'Registrar si el lector es estudiante o docente (D3-1, D3-2).'),
    ('CU-01', 'Modificado', 'Paso 4 y flujo 4b comparan con el máximo del tipo de lector.'),
    ('P-06', 'Desdoblada', 'P-06a (estudiante con dos préstamos) y P-06b (docente con cinco).'),
]


def existe(cod):
    return (cod in TEXTO or cod in D.NECESIDAD or cod in dict(D.REGLAS) or cod in REQ or cod in PRUEBA
            or cod == RF11[0] or cod.startswith('CU-0'))

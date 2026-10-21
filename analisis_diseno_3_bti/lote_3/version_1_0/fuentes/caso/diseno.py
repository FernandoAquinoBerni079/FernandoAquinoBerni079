# -*- coding: utf-8 -*-
"""Fuente única del diseño del caso Arapoty para la Unidad III (Capítulos 7 a 9). Caso ficticio.

Amplía, sin modificarlos, `lote_1/caso/dossier.py` y `lote_2/caso/requisitos.py` y `modelos.py`. Diseña para el
catálogo v1.1 (solicitud SC-01: RN-02 modificada y RF-11 nuevo). Contiene:
  - modelo de datos: entidades, relaciones, restricciones de integridad (RI-xx) con su regla o requisito, datos
    derivados, parámetros y diccionario de datos (Capítulo 7);
  - interacción: pantallas (PT-xx), zonas por rol, transiciones del mapa de navegación, recorridos de los tres casos
    de uso prioritarios, mensajes y estados (ME-xx) y lista de accesibilidad (Capítulo 8);
  - arquitectura: capas, operaciones (OP-xx) con sus contratos, registro de decisión técnica DT-01 y matriz de
    coherencia requisito-datos-interfaz-operación-prueba (Capítulo 9);
  - banco de variantes del H3 (VH-x), que la guía entrega en la defensa individual.
Códigos nuevos: RI, PT, ME, OP, DT, VH. No se reutiliza ningún código anterior (P-xx son las pruebas del Capítulo 6).
build/verificar.py comprueba que cada requisito, regla, necesidad, caso de uso, flujo y prueba citados existen."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(ADS, 'lote_2', 'caso'))
import requisitos as R
import modelos as MO
D = R.D

# ------------------------------------------------------------------ catálogo v1.1
CATALOGO_V11 = [r for r in R.CATALOGO] + [R.RF11]
REQ = {r[0]: r for r in CATALOGO_V11}
REGLAS_V11 = [R.REGLA_V11 if c == 'RN-02' else (c, t) for c, t in D.REGLAS]
REGLA = dict(REGLAS_V11)

# ================================================================== Capítulo 7: datos
# (nombre, qué representa, cómo se identifica, quién lo crea o lo cambia, requisitos)
ENTIDADES = [
    ('Obra', 'La obra como la piensa el lector: un título de un autor. Es lo que se busca en la consulta.',
     'Código interno de obra', 'La bibliotecaria, al catalogar', ['RF-07']),
    ('Edición', 'Una publicación concreta de la obra: editorial y año. Dos ediciones de la misma obra son la misma obra para el lector.',
     'Código interno de edición', 'La bibliotecaria, al catalogar', ['RF-07']),
    ('Ejemplar', 'Cada libro físico, con su etiqueta. Es lo que se presta y lo que vuelve.',
     'Código de ejemplar, pegado en el libro', 'La bibliotecaria, al dar de alta o inactivar', ['RF-03', 'RF-04', 'RF-10']),
    ('Lector', 'Quien puede retirar libros: estudiante o docente del colegio.',
     'Código interno de lector (no la cédula)', 'La bibliotecaria, al registrar o inactivar', ['RF-06', 'RF-10', 'RF-11', 'RNF-03']),
    ('Préstamo', 'La salida de un ejemplar a un lector. Se cierra con la devolución y nunca se borra.',
     'Número de préstamo', 'El sistema, cuando la bibliotecaria presta o recibe', ['RF-01', 'RF-02', 'RF-03', 'RF-05', 'RF-08', 'RF-09']),
    ('Parámetro', 'Un valor que fija una regla y puede cambiar: el plazo y los máximos de préstamos.',
     'Nombre del parámetro', 'La bibliotecaria, cuando la dirección cambia la regla', ['RF-02', 'RF-05']),
    ('Cuenta', 'Quién opera el sistema y con qué rol. Solo si se implementan sesiones (Work §7.2).',
     'Nombre de usuario', 'La dirección asigna los roles', ['RNF-02']),
]
ENTIDAD = {e[0]: e for e in ENTIDADES}

# (entidad 1, relación, entidad 2, cardinalidad 1, cardinalidad 2, explicación)
RELACIONES = [
    ('Obra', 'tiene', 'Edición', '1', 'N', 'Una obra puede tener varias ediciones; cada edición es de una sola obra.'),
    ('Edición', 'tiene', 'Ejemplar', '1', 'N', 'De una edición puede haber varios ejemplares; cada ejemplar es de una sola edición.'),
    ('Ejemplar', 'se presta en', 'Préstamo', '1', 'N', 'Un ejemplar tiene muchos préstamos en su historia; cada préstamo es de un solo ejemplar.'),
    ('Lector', 'pide', 'Préstamo', '1', 'N', 'Un lector tiene muchos préstamos en su historia; cada préstamo es de un solo lector.'),
]
SIN_RELACION = ['Parámetro', 'Cuenta']

# Restricciones de integridad: (código, enunciado, de dónde sale)
RESTRICCIONES = [
    ('RI-01', 'Un ejemplar tiene, como máximo, un préstamo sin fecha de devolución.', ['RN-01', 'RF-04']),
    ('RI-02', 'Los préstamos sin fecha de devolución de un lector no superan el máximo de su tipo, que está en Parámetro.', ['RN-02', 'RF-05', 'RF-11']),
    ('RI-03', 'No se registra un préstamo de un lector inactivo ni de un ejemplar inactivo.', ['RN-04', 'RF-06', 'RF-10']),
    ('RI-04', 'Devolver completa la fecha de devolución del préstamo; el préstamo no se borra.', ['RN-05', 'RF-03']),
    ('RI-05', 'Un lector o un ejemplar con préstamos en su historia no se borra: se inactiva.', ['RN-06', 'RF-10']),
    ('RI-06', 'El curso es obligatorio para los estudiantes y queda vacío para los docentes.', ['RF-11', 'RF-09', 'N-06']),
    ('RI-07', 'El vencimiento se calcula al prestar, con el plazo vigente ese día, y se guarda.', ['RN-03', 'RF-02']),
    ('RI-08', 'Al prestar a un estudiante se guarda su curso de ese momento en el préstamo; al prestar a un docente, no.', ['RF-09', 'N-06', 'D2-8']),
]
RESTRICCION = {c: (t, f) for c, t, f in RESTRICCIONES}

DERIVADOS = [
    ('Ejemplar disponible', 'Ejemplar activo sin préstamo sin fecha de devolución', 'RF-07', 'Si se guardara, podría contradecir los préstamos: dos datos que dicen lo mismo terminan diciendo cosas distintas.'),
    ('Préstamo vencido', 'Préstamo sin devolución cuyo vencimiento es anterior a la fecha de referencia', 'RF-08', 'Depende del día en que se consulta: no se puede guardar.'),
    ('Préstamos activos de un lector', 'Cantidad de sus préstamos sin fecha de devolución', 'RF-05', 'Se cuenta cada vez; un contador guardado se desincroniza.'),
    ('Disponibles de una obra', 'Ejemplares disponibles de todas sus ediciones', 'RF-07', 'Es lo que ve la consulta pública, sin ningún dato de lectores (RNF-03).'),
]

PARAMETROS = [
    ('plazo_dias', '7', 'RN-03', 'Días de préstamo.'),
    ('maximo_estudiante', '2', 'RN-02', 'Préstamos activos que puede tener un estudiante.'),
    ('maximo_docente', '5', 'RN-02', 'Préstamos activos que puede tener un docente (SC-01, D3-1).'),
]

# Diccionario: (entidad, campo, significado, obligatorio, ejemplo, origen)
DICCIONARIO = [
    ('Obra', 'código', 'Identificador interno de la obra', 'Sí', 'OB-0031', 'RF-07'),
    ('Obra', 'título', 'Título como figura en la tapa', 'Sí', 'Cuentos del arroyo Arapoty', 'RF-07, E3-L1'),
    ('Obra', 'autor', 'Autor o autora', 'Sí', 'Autora del caso (ficticia)', 'RF-07'),
    ('Edición', 'código', 'Identificador interno de la edición', 'Sí', 'ED-0045', 'RF-07'),
    ('Edición', 'obra', 'Obra a la que pertenece', 'Sí', 'OB-0031', 'RF-07'),
    ('Edición', 'editorial y año', 'Datos de la publicación', 'No', 'Editorial del caso, 2019', 'RF-07'),
    ('Ejemplar', 'código', 'Etiqueta pegada en el libro físico', 'Sí', 'EJ-0457', 'RF-03, E4-L2'),
    ('Ejemplar', 'edición', 'Edición a la que pertenece', 'Sí', 'ED-0045', 'RF-07'),
    ('Ejemplar', 'estado', 'Activo o inactivo; un ejemplar inactivo no se presta', 'Sí', 'activo', 'RF-10, RN-06'),
    ('Lector', 'código', 'Identificador interno; no es la cédula', 'Sí', 'LE-0123', 'RNF-03, E5-L6'),
    ('Lector', 'nombre', 'Nombre y apellido; solo lo ve la bibliotecaria', 'Sí', 'Lector del caso (ficticio)', 'RF-08, RNF-03'),
    ('Lector', 'tipo', 'Estudiante o docente', 'Sí', 'estudiante', 'RF-11, D3-1'),
    ('Lector', 'curso', 'Curso actual; solo para estudiantes', 'Si es estudiante', '2.º BTI', 'RF-09, D2-8'),
    ('Lector', 'estado', 'Activo o inactivo; un lector inactivo no recibe préstamos', 'Sí', 'activo', 'RF-06, RN-04'),
    ('Préstamo', 'número', 'Identificador del préstamo', 'Sí', '1042', 'RF-01'),
    ('Préstamo', 'ejemplar', 'Ejemplar prestado (no la obra)', 'Sí', 'EJ-0457', 'RF-01, RF-03, RN-01'),
    ('Préstamo', 'lector', 'Lector que lo retira', 'Sí', 'LE-0123', 'RF-01'),
    ('Préstamo', 'curso al prestar', 'Curso del estudiante el día del préstamo; vacío para docentes', 'Si es estudiante', '2.º BTI', 'RF-09, N-06'),
    ('Préstamo', 'fecha de salida', 'Día en que se presta', 'Sí', '02/03', 'RF-01'),
    ('Préstamo', 'fecha de vencimiento', 'Salida más el plazo vigente ese día', 'Sí', '09/03', 'RF-02, RN-03'),
    ('Préstamo', 'fecha de devolución', 'Vacía mientras está activo; se completa al devolver', 'No', '07/03', 'RF-03, RN-05'),
    ('Parámetro', 'nombre', 'Qué regla fija', 'Sí', 'maximo_docente', 'RN-02, RN-03'),
    ('Parámetro', 'valor', 'Valor vigente', 'Sí', '5', 'RN-02, RN-03'),
    ('Cuenta', 'usuario', 'Nombre con que se ingresa', 'Sí', 'biblioteca1', 'RNF-02'),
    ('Cuenta', 'rol', 'Bibliotecaria (o su reemplazo) o dirección', 'Sí', 'bibliotecaria', 'RNF-02, E4-L8'),
]

# Revisión de normalización aplicada (7.4): la línea del cuaderno (D1-A4) como una sola tabla.
CUADERNO_ROTULO = 'Tabla 7.6 — El cuaderno de préstamos como una sola tabla (D1-A4, datos ficticios)'
CUADERNO = (['Lector', 'Curso', 'Título', 'Fecha'],
            [['Lector A', '2.º BTI', 'Cuentos del arroyo Arapoty', '02/03'],
             ['Lector A', '2.º', 'Atlas escolar', '05/03'],
             ['Lector B', '', 'Cuentos del arroyo Arapoty', '05/03'],
             ['Docente C', 'Docente', 'Cuentos del arroyo Arapoty', '06/03']])
ANOMALIAS = [
    ('Repetición', 'El curso del Lector A se escribe en cada préstamo, y una vez dice «2.º BTI» y otra «2.º».', 'El curso va una vez en Lector; el préstamo guarda el curso de ese día (RI-08).'),
    ('Dato que falta', 'El préstamo del Lector B no tiene curso, como los seis de D2-8; el informe no puede contarlo.', 'El curso es obligatorio para estudiantes (RI-06): el sistema no deja guardar sin él.'),
    ('Dato forzado', 'Al docente se le anotó «Docente» en la columna del curso, que no es un curso.', 'El tipo de lector es un campo aparte (RF-11); el curso del docente queda vacío.'),
    ('Identidad ambigua', 'Hay tres préstamos del mismo título y no se sabe qué ejemplar se llevó cada uno (E4-L2).', 'El préstamo es de un ejemplar, con su código (RI-01).'),
    ('Pérdida al borrar', 'Si se tacha el único préstamo de «Atlas escolar», el cuaderno deja de mostrar que el título existe.', 'La obra existe aparte de sus préstamos, y los préstamos no se borran (RI-04).'),
]

# Informe mensual por curso (RF-09) a partir del curso guardado en cada préstamo.
INFORME_ROTULO = 'Tabla 7.8 — Informe de abril, el primer mes con el sistema, generado desde los préstamos (datos ficticios)'
_GRUPOS = [('7.º grado', '7.º', 23), ('8.º grado', '8.º', 16), ('9.º grado', '9.º', 15), ('1.º BTI', '1.º BTI', 18),
           ('2.º BTI', '2.º BTI', 17), ('3.º BTI', '3.º BTI', 12)]
_DOCENTES = 11
INFORME = (['Grupo', 'Cómo se obtiene', 'Préstamos'],
           [[g, 'Préstamos de abril con curso al prestar «%s»' % c, str(n)] for g, c, n in _GRUPOS]
           + [['Docentes', 'Préstamos de abril de lectores de tipo docente (sin curso)', str(_DOCENTES)],
              ['Total', 'Todos los préstamos de abril, contados de nuevo, no sumados a mano', str(sum(n for _, _, n in _GRUPOS) + _DOCENTES)]])
assert INFORME[1][-1][2] == '112'

# ================================================================== Capítulo 8: interacción
ZONAS = [('Pública', 'Cualquier persona, sin iniciar sesión'),
         ('Bibliotecaria', 'Solo con sesión de la bibliotecaria o su reemplazo'),
         ('Dirección', 'Solo con sesión de la dirección')]
# (código, nombre, zona, qué muestra, requisitos)
PANTALLAS = [
    ('PT-01', 'Buscar un título', 'Pública', 'Un campo «Título o parte del título» y el botón «Buscar».', ['RF-07']),
    ('PT-02', 'Disponibilidad', 'Pública', 'Los títulos que coinciden y cuántos ejemplares hay disponibles. Ningún dato de lectores.', ['RF-07', 'RNF-03']),
    ('PT-03', 'Ingreso del personal', 'Pública', 'Usuario, contraseña y el botón «Ingresar».', ['RNF-02']),
    ('PT-04', 'Inicio de la bibliotecaria', 'Bibliotecaria', 'Los accesos a prestar, devolver, préstamos activos, lectores y ejemplares, e informe.', ['RNF-01']),
    ('PT-05', 'Registrar préstamo', 'Bibliotecaria', 'Código del lector, sus préstamos activos, código del ejemplar y «Prestar».', ['RF-01', 'RF-02', 'RF-04', 'RF-05', 'RF-06']),
    ('PT-06', 'Registrar devolución', 'Bibliotecaria', 'Código del ejemplar, su préstamo activo con el lector y «Confirmar devolución».', ['RF-03', 'RF-08']),
    ('PT-07', 'Préstamos activos y vencidos', 'Bibliotecaria', 'Qué lector tiene cada ejemplar y cuáles están vencidos a la fecha.', ['RF-08']),
    ('PT-08', 'Lectores y ejemplares', 'Bibliotecaria', 'Alta, tipo y curso del lector; alta e inactivación de lectores y ejemplares.', ['RF-10', 'RF-11']),
    ('PT-09', 'Informe mensual por curso', 'Dirección', 'El mes elegido y los préstamos por curso, más la fila «Docentes».', ['RF-09']),
]
PANTALLA = {p[0]: p for p in PANTALLAS}
INICIO = 'PT-01'
# (desde, hasta, acción del usuario)
TRANSICIONES = [
    ('PT-01', 'PT-02', 'Buscar'), ('PT-02', 'PT-01', 'Buscar otro'), ('PT-01', 'PT-03', 'Ingresar como personal'),
    ('PT-03', 'PT-04', 'Ingresar (bibliotecaria)'), ('PT-03', 'PT-09', 'Ingresar (dirección)'),
    ('PT-04', 'PT-05', 'Prestar'), ('PT-04', 'PT-06', 'Devolver'), ('PT-04', 'PT-07', 'Ver préstamos'),
    ('PT-04', 'PT-08', 'Gestionar lectores'), ('PT-04', 'PT-09', 'Ver informe'),
]
NOTA_MAPA = ('Cada pantalla de la bibliotecaria vuelve a PT-04 con «Volver al inicio», y cada zona con sesión tiene '
             '«Salir», que vuelve a PT-01. No se dibujan para que el mapa se pueda leer.')

# Recorridos de las tres tareas (C6): (caso de uso, [(paso de la plantilla, pantalla, lo que hace la persona, lo que responde el sistema)])
RECORRIDOS = [
    ('CU-01', [(1, 'PT-05', 'Escribe o lee el código del lector', 'Muestra el nombre, el tipo y los préstamos activos'),
               (3, 'PT-05', 'Escribe el código del ejemplar', 'Muestra el título y la edición'),
               (6, 'PT-05', 'Pulsa «Prestar»', 'Comprueba las reglas y registra'),
               (7, 'PT-05', 'Lee la fecha de vencimiento', 'Muestra la confirmación ME-04')]),
    ('CU-02', [(1, 'PT-06', 'Escribe el código del ejemplar devuelto', 'Busca su préstamo activo'),
               (2, 'PT-06', 'Mira quién lo tenía', 'Muestra el préstamo con el lector'),
               (3, 'PT-06', 'Pulsa «Confirmar devolución»', 'Cierra el préstamo'),
               (4, 'PT-06', 'Lee la confirmación', 'Muestra ME-07')]),
    ('CU-03', [(1, 'PT-01', 'Escribe parte del título', '—'),
               (2, 'PT-02', 'Mira la lista de títulos', 'Muestra los que coinciden'),
               (3, 'PT-02', 'Elige un título', '—'),
               (4, 'PT-02', 'Lee cuántos hay', 'Muestra los disponibles, sin datos de lectores')]),
]

# Mensajes y estados: (código, pantalla, estado, cuándo: caso de uso y flujo o paso, texto, requisitos)
MENSAJES = [
    ('ME-01', 'PT-05', 'error', 'CU-01, flujo 4a', 'No se puede prestar: este lector está inactivo. Si debería poder retirar libros, consultá con la dirección.', ['RF-06']),
    ('ME-02', 'PT-05', 'error', 'CU-01, flujo 4b', 'No se puede prestar: el lector ya tiene 2 préstamos activos, el máximo para estudiantes. Tiene que devolver uno antes.', ['RF-05', 'RF-11']),
    ('ME-03', 'PT-05', 'error', 'CU-01, flujo 5a', 'No se puede prestar: el ejemplar EJ-0457 ya está prestado y vence el 12/03. Elegí otro ejemplar disponible.', ['RF-04']),
    ('ME-04', 'PT-05', 'confirmación', 'CU-01, paso 7', 'Préstamo registrado. Vence el 09/03.', ['RF-01', 'RF-02']),
    ('ME-05', 'PT-06', 'error', 'CU-02, flujo 1a', 'Ese código no corresponde a ningún ejemplar de la biblioteca. Revisá la etiqueta; si no es de la biblioteca, apartalo.', ['RF-03']),
    ('ME-06', 'PT-06', 'error', 'CU-02, flujo 2a', 'Este ejemplar no tiene un préstamo activo. No se cerró ningún préstamo: apartalo para revisarlo con el historial.', ['RF-03']),
    ('ME-07', 'PT-06', 'confirmación', 'CU-02, paso 4', 'Devolución registrada. El préstamo queda en el historial y el ejemplar está disponible.', ['RF-03']),
    ('ME-08', 'PT-02', 'vacío', 'CU-03, flujo 2a', 'No encontramos títulos con esas palabras. Probá con otra parte del título.', ['RF-07']),
    ('ME-09', 'PT-02', 'vacío', 'CU-03, flujo 4a', '0 disponibles por ahora.', ['RF-07', 'RNF-03']),
    ('ME-10', 'PT-07', 'vacío', 'Sin préstamos activos', 'No hay préstamos activos.', ['RF-08']),
    ('ME-11', 'PT-02, PT-05, PT-06', 'carga', 'Mientras el sistema busca o guarda', 'Buscando… / Guardando… (y el botón queda desactivado para no enviarlo dos veces).', ['RS-01']),
    ('ME-12', 'PT-03', 'error', 'Usuario o contraseña incorrectos', 'No pudimos iniciar la sesión. Revisá el usuario y la contraseña.', ['RNF-02']),
]
MENSAJE = {m[0]: m for m in MENSAJES}
REGLA_MENSAJE = 'Un buen mensaje dice qué pasó, por qué pasó y qué puede hacer la persona.'

ACCESIBILIDAD = [
    ('A-01', 'Cada campo tiene una etiqueta visible, escrita arriba o a la izquierda, que no desaparece al escribir.'),
    ('A-02', 'Se puede completar cada tarea solo con el teclado; Tab sigue el orden de la tarea y Enter confirma.'),
    ('A-03', 'El elemento que tiene el foco se ve con claridad.'),
    ('A-04', 'Ningún mensaje depende solo del color: el error dice en palabras qué pasó.'),
    ('A-05', 'El mensaje aparece junto al campo o la acción que lo provocó.'),
    ('A-06', 'Frases cortas y palabras de quien usa el sistema: «ejemplar» y «devolución», no «ID» ni «transacción».'),
    ('A-07', 'Ningún botón que borra o cancela queda al lado del botón que confirma.'),
    ('A-08', 'Letra de tamaño cómodo y contraste suficiente entre el texto y el fondo, también en la computadora vieja de la biblioteca (E4-L10).'),
]

# ================================================================== Capítulo 9: arquitectura
CAPAS = [
    ('Presentación', 'Muestra pantallas, recibe lo que la persona escribe y muestra los mensajes.', 'PT-01 a PT-09, ME-01 a ME-12'),
    ('Reglas de negocio', 'Decide si una operación se puede hacer: comprueba permisos, reglas y restricciones.', 'OP-01 a OP-06, RI-01 a RI-08'),
    ('Persistencia', 'Guarda y recupera los datos; protege RI-01 y el historial aunque falle otra capa.', 'Entidades del Capítulo 7'),
]
# Contratos: (código, nombre, entradas, precondiciones, resultado, errores, requisitos)
OPERACIONES = [
    ('OP-01', 'registrar préstamo',
     'Código del lector, código del ejemplar, cuenta que opera.',
     'La cuenta tiene rol de bibliotecaria (RNF-02).',
     'Existe un préstamo nuevo con fecha de salida de hoy, el curso del estudiante si corresponde (RI-08) y el vencimiento con el plazo vigente (RI-07). El ejemplar deja de estar disponible. Si dos pedidos llegan a la vez por el mismo ejemplar, se registra solo uno (RI-01).',
     ['ME-01 (lector inactivo, RI-03)', 'ME-02 (máximo del tipo, RI-02)', 'ME-03 (ejemplar ya prestado, RI-01)', 'ME-05 (ejemplar inexistente)', 'ME-12 (sin permiso)'],
     ['RF-01', 'RF-02', 'RF-04', 'RF-05', 'RF-06', 'RF-11', 'RNF-02']),
    ('OP-02', 'registrar devolución',
     'Código del ejemplar, cuenta que opera.',
     'La cuenta tiene rol de bibliotecaria (RNF-02).',
     'El préstamo sin devolución de ese ejemplar tiene ahora la fecha de devolución de hoy (RI-04). No se borra ningún dato. El ejemplar vuelve a estar disponible.',
     ['ME-05 (ejemplar inexistente)', 'ME-06 (sin préstamo activo)', 'ME-12 (sin permiso)'],
     ['RF-03', 'RF-08', 'RNF-02']),
    ('OP-03', 'consultar disponibilidad',
     'Texto del título, o parte de él.',
     'Ninguna: es pública.',
     'La lista de obras que coinciden, cada una con la cantidad de ejemplares disponibles (dato derivado). Nunca devuelve datos de lectores.',
     ['ME-08 (sin coincidencias)', 'ME-09 (0 disponibles)'],
     ['RF-07', 'RNF-03']),
    ('OP-04', 'listar préstamos activos',
     'Fecha de referencia, cuenta que opera.',
     'Rol de bibliotecaria.',
     'Los préstamos sin devolución, con el ejemplar y el lector, y marcados los vencidos a la fecha de referencia.',
     ['ME-10 (no hay préstamos activos)', 'ME-12 (sin permiso)'],
     ['RF-08', 'RNF-02']),
    ('OP-05', 'informe mensual por curso',
     'Mes y año, cuenta que opera.',
     'Rol de dirección o de bibliotecaria.',
     'Los préstamos del mes agrupados por curso al prestar, más la fila «Docentes», y el total contado de nuevo.',
     ['ME-12 (sin permiso)'],
     ['RF-09', 'RF-11', 'RNF-02']),
    ('OP-06', 'inactivar lector o ejemplar',
     'Código del lector o del ejemplar, cuenta que opera.',
     'Rol de bibliotecaria.',
     'El lector o el ejemplar queda inactivo. Su historial no cambia (RI-05).',
     ['ME-12 (sin permiso)'],
     ['RF-10', 'RNF-02']),
]
OPERACION = {o[0]: o for o in OPERACIONES}
PRIORITARIAS = ['OP-01', 'OP-02', 'OP-03']

DT01 = [
    ('Identificador', 'DT-01 — Entorno de ejecución del prototipo (decisión provisional del equipo modelo)'),
    ('Contexto', 'La computadora de la biblioteca es vieja y no siempre tiene internet (E4-L10). No hay presupuesto para programas ni servicios (E5-L4). Las reglas y los permisos se comprueban en el servidor, no solo en la pantalla (Work §7.5).'),
    ('Condiciones excluyentes', 'RS-01: funciona sin internet. RS-02: sin licencias ni servicios pagos. Una opción que no las cumple se descarta antes de comparar.'),
    ('Opciones', 'A. Aplicación web local: HTML y CSS, PHP y SQLite en la computadora de la biblioteca. B. Planilla de cálculo con hojas protegidas. C. Aplicación web en un servicio de internet gratuito. D. El entorno que ya domine el curso en Laboratorio, si cumple RS-01 y RS-02.'),
    ('Descarte', 'C no cumple RS-01. B no puede impedir el doble préstamo de forma segura (RI-01) ni separar permisos (RNF-02).'),
    ('Decisión', 'A, como ejemplo de referencia, o D si la institución domina otro entorno equivalente. Es provisional: no está verificada en los equipos de ningún colegio.'),
    ('Consecuencias', 'Hay que instalarla y probarla en la computadora real antes de la Unidad IV; respaldar el archivo de datos (Capítulo 17); recibir una base de proyecto explicada (Work §7.5).'),
    ('Requisitos que la condicionan', 'RS-01, RS-02, RNF-02, RI-01, E4-L10.'),
]

# Matriz de coherencia (9.4): requisito → datos, interfaz, operación, prueba prevista (Capítulo 6)
COHERENCIA = [
    ('RF-01', 'Préstamo', 'PT-05, ME-04', 'OP-01', 'P-01'),
    ('RF-02', 'Préstamo.vencimiento, Parámetro, RI-07', 'PT-05, ME-04', 'OP-01', 'P-02'),
    ('RF-03', 'Préstamo.devolución, RI-04', 'PT-06, ME-06, ME-07', 'OP-02', 'P-03'),
    ('RF-04', 'RI-01', 'PT-05, ME-03', 'OP-01', 'P-07'),
    ('RF-05', 'RI-02, Parámetro', 'PT-05, ME-02', 'OP-01', 'P-06'),
    ('RF-06', 'Lector.estado, RI-03', 'PT-05, ME-01', 'OP-01', 'P-05'),
    ('RF-07', 'Obra, Edición, Ejemplar; disponibles (derivado)', 'PT-01, PT-02, ME-08, ME-09', 'OP-03', 'P-08'),
    ('RF-08', 'Préstamo, Lector', 'PT-06, PT-07, ME-10', 'OP-02, OP-04', 'P-04'),
    ('RF-09', 'Préstamo.curso al prestar, RI-06, RI-08', 'PT-09', 'OP-05', 'P-09'),
    ('RF-10', 'Estado de Lector y Ejemplar, RI-05', 'PT-08', 'OP-06', 'P-10'),
    ('RF-11', 'Lector.tipo, RI-02, RI-06', 'PT-08, ME-02', 'OP-01, OP-05', 'P-06'),
    ('RNF-01', '—', 'PT-04 a PT-07; A-01 a A-08', '—', 'P-14'),
    ('RNF-02', 'Cuenta', 'PT-03, ME-12; zonas', 'Todas las de la bibliotecaria', 'P-11'),
    ('RNF-03', 'Lector.código interno', 'PT-02, ME-09', 'OP-03', 'P-12'),
    ('RS-01', '—', 'ME-11', 'DT-01', 'P-13'),
    ('RS-02', '—', '—', 'DT-01', 'P-15'),
]

# ================================================================== H3
BANCO_H3 = [
    ('VH-1', 'La dirección decide que los docentes tengan un plazo de catorce días; los estudiantes siguen con siete.',
     'Parámetro por tipo de lector; RI-07 y RF-02; ME-04; poscondición de OP-01; P-02 desdoblada.'),
    ('VH-2', 'El colegio recibe una donación de veinte ejemplares de una obra que ya está en el catálogo, en una edición nueva.',
     'Edición nueva de la misma obra; la consulta (OP-03) suma las dos ediciones; ningún préstamo cambia.'),
    ('VH-3', 'Durante febrero, la biblioteca presta también a los egresados del último año, con un máximo de un libro.',
     'Tipo de lector nuevo y su máximo en Parámetro; el curso no aplica; fila nueva en el informe (OP-05).'),
    ('VH-4', 'La bibliotecaria quiere ver los préstamos vencidos ordenados por días de atraso.',
     'Dato derivado (no se guarda); PT-07; OP-04 con la fecha de referencia.'),
    ('VH-5', 'Una ayudante del turno tarde va a registrar solo devoluciones, nunca préstamos.',
     'Rol nuevo en Cuenta; la zona y la precondición de OP-02 cambian; OP-01 no; el permiso se comprueba en el servidor.'),
]


def existe(cod):
    return (cod in REQ or cod in REGLA or cod in D.NECESIDAD or cod in R.TEXTO or cod in R.PRUEBA or cod in RESTRICCION
            or cod in PANTALLA or cod in MENSAJE or cod in OPERACION or cod == 'DT-01' or cod.startswith('CU-0'))

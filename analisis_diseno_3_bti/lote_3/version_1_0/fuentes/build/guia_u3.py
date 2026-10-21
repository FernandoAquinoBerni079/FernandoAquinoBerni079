# -*- coding: utf-8 -*-
"""Guía docente con solucionario del lote 3 (Unidad III, Capítulos 7 a 9): acuerdo previo con Algorítmica 3.º,
secuencia de cada encuentro en HC, claves de las actividades, prácticas y evaluaciones, listas de cotejo, leyendas de
las notaciones con errores frecuentes, tarjetas de rol del Encuentro 16, contratos de referencia, rúbrica del H3 con
evidencias, planilla y banco de variantes, calendario de 28 encuentros y procedencia de los recursos.
Los datos del caso se leen de caso/diseno.py y caso/mbokaja_u3.py; no se copian."""
import oficio as O
H, M, K = O.H, O.M, O.K
import piezas_u3 as Z
import cap7, cap8, cap9
X, MB, G = Z.X, Z.MB, Z.G
R, D, MO = X.R, X.D, X.MO

ANCHO_SEC = [3.2, 2.2, 11.2]

# ---------------------------------------------------------------- acuerdo con Algorítmica 3.º
ALGORITMICA = [
    'Antes del Encuentro 13, el docente de Algorítmica 3.º informa qué ya trabajó el curso: modelo entidad-relación, '
    'claves, integridad referencial, paso a tablas y anomalías (en el libro de la colección, Clases 8, 9 y 11 a 17). Es el '
    'acuerdo de articulación de Work §3.',
    'Ruta A, el curso ya trabajó el modelado: la sección 7.1 se resuelve con la ficha de recuperación y la Actividad 1 del '
    'Encuentro 13, en unos 20 minutos.',
    'Ruta B, el curso todavía no lo trabajó: el docente entrega la Figura 7.1 como esquema inicial explicado y la lee con el '
    'curso símbolo por símbolo con la Tabla 7.1. No se da una clase de bases de datos: el capítulo usa el modelo para '
    'justificar decisiones. Ninguna actividad del capítulo exige saber normalización ni SQL.',
    'En las dos rutas se evita repetir los ejercicios de Algorítmica: este capítulo no tiene tablas «Socios» ni «Libros», '
    'ni ejercicios de formas normales, ni prácticas en Access.',
]

# ---------------------------------------------------------------- capítulo 7
SEC_C7 = [
    ('Encuentro 13 — Antecedentes de Algorítmica y modelo del dominio (5 HC de diseño)', [
        ['Problema y explicación', 'aprox. 1 HC', 'Apertura del capítulo. Sección 7.1 con la ficha de recuperación y la Tabla 7.1, según la ruta A o B. Actividad 1 como diagnóstico breve.'],
        ['Práctica', 'aprox. 3 HC', 'Sección 7.2 con la Figura 7.1, la Tabla 7.2, la Figura 7.2 y los Ejemplos resueltos 7.1 y 7.2. Actividades 2 a 4. Práctica 7, Nivel 1 (aprox. 1 HC).'],
        ['Revisión y cierre', 'aprox. 1 HC', 'Plenario de la Actividad 4. Evidencia del encuentro (Work, encuentro 13): obras/ediciones, ejemplares, lectores y préstamos. El Desafío queda como tarea.'],
    ]),
    ('Encuentro 14 — Integridad, historial y diccionario (5 HC: 4 de diseño y 1 de verificación)', [
        ['Problema y explicación', 'aprox. 1 HC', 'Sección 7.3 con la Tabla 7.3, la Figura 7.3, la Tabla 7.4 y el diccionario (Tabla 7.5).'],
        ['Práctica', 'aprox. 3 HC', 'Ejemplo resuelto 7.3 y Actividades 1 a 3 (aprox. 1 HC). Sección 7.4 con las Tablas 7.6 a 7.8 y el Ejemplo resuelto 7.4 (aprox. 1 HC). Práctica 7, Niveles 2 o 3 (aprox. 1 HC).'],
        ['Revisión con contraejemplos', 'aprox. 1 HC (verificación)', 'Cada equipo le entrega a otro tres contraejemplos para su modelo; el otro equipo dice qué restricción los rechaza o corrige el modelo. Evidencia (Work, encuentro 14): revisión del modelo con ejemplos y contraejemplos. Articula con C9.'],
    ]),
]
CLAVES_E13 = [
    ['1', '(a) Obra. (b) Edición. (c) Ejemplar. (d) Préstamo. (e) Obra. (f) Ejemplar: es su estado.', 'Poner el año en la obra o la fecha de vencimiento en el ejemplar.'],
    ['2', 'Una obra tiene N ediciones; cada edición es de una obra. Una edición tiene N ejemplares; cada ejemplar es de una edición. Un ejemplar se presta en N préstamos a lo largo del tiempo; cada préstamo es de un ejemplar. Un lector pide N préstamos; cada préstamo es de un lector.', 'Leer «un ejemplar, un préstamo»: el límite de uno es para los activos (RI-01), no para el historial.'],
    ['3', 'El lector que se fue del colegio no debe recibir préstamos, pero su historial sirve para saber qué se llevó (E4-L6). Con un estado inactivo se cumplen las dos cosas (RN-06, RI-05). Si se lo borrara, se perderían sus préstamos y no se sabría qué libros faltan.', 'Proponer borrar al lector «porque ya no está».'],
    ['4', 'Primera razón: la cédula no hace falta para prestar y es un dato personal; E5-L6 pide que los datos de los estudiantes no queden a la vista y RNF-03, que la consulta no muestre datos personales. Guardar menos datos personales es la forma más segura de cumplirlos. Segunda razón: el código interno lo asigna la biblioteca y sirve igual para estudiantes y docentes (RF-11). Se acepta otra razón si se apoya en el dossier o el catálogo.', 'Decir que la cédula «se repite».'],
    ['5', 'Respuesta abierta. Opción razonable: una obra con dos ediciones o dos ejemplares marcados «Tomo 1» y «Tomo 2», según se presten juntos o no; si se prestan por separado y se buscan por separado, conviene tratarlos como dos obras. La consulta tiene que mostrar los disponibles de cada tomo.', 'Decidir sin explicar qué ve el lector en la consulta.'],
]
CLAVES_E14 = [
    ['1', '(a) RI-03. (b) RI-02 (el máximo de los estudiantes es dos). (c) RI-05. (d) RI-06.', 'Citar la regla RN y no la restricción RI.'],
    ['2', 'El diccionario ya tiene Lector.estado (activo o inactivo), que pide RN-04 a través de RF-06. Si el estudiante propone un campo nuevo, por ejemplo «fecha de inactivación», se acepta con significado, obligatoriedad, ejemplo y origen.', 'Campo sin origen.'],
    ['3', 'RI-03. Ejemplo válido: préstamo a un lector activo de un ejemplar activo. Contraejemplo: préstamo a un lector inactivo. RI-05. Ejemplo válido: inactivar un ejemplar con historial. Contraejemplo: borrar un lector con préstamos en su historia.', 'Dar dos ejemplos válidos y ningún contraejemplo.'],
    ['4', 'El campo puede contradecir los préstamos: si un préstamo se registra y el campo no se actualiza, la consulta muestra un libro disponible que está prestado. Tendría que cumplirse siempre: «disponible» es verdadero si y solo si el ejemplar está activo y no tiene un préstamo sin devolución. Por eso se calcula (Tabla 7.4).', 'Aceptar el campo «porque es más rápido» sin la condición.'],
    ['5', 'Los préstamos de marzo conservan su vencimiento de siete días: se calculó al prestar y se guardó (RI-07). Cambia el valor de Parámetro plazo_dias, de 7 a 10, y desde el cambio los préstamos nuevos vencen a los diez días. Nadie recibe una fecha distinta a la que se le comunicó.', 'Recalcular los vencimientos ya hechos.'],
]
CLAVES_P7 = [
    ['Nivel 1', 'Modelo con Obra, Edición (se acepta omitirla si se justifica que en Mbokaja no hay dos ediciones), Ejemplar, Lector y Préstamo, con las mismas relaciones de la Figura 7.1. M-F8 obliga a distinguir ejemplares: hay tres de cada lectura obligatoria. MS-3: el préstamo del ejemplar perdido queda en el historial con una marca de «perdido» o una fecha de cierre por pérdida; el ejemplar perdido queda inactivo (no se borra); el ejemplar que lo repone es un ejemplar nuevo de la misma edición, con su propio código. Ningún dato se borra.'],
    ['Nivel 2', 'Diccionario de Ejemplar (código, edición, estado: activo, inactivo o perdido) y de Préstamo (número, ejemplar, lector, fecha de salida, vencimiento, fecha de devolución, y si se registra la pérdida, cómo se cerró), con origen MR-01, MR-02, MR-04, M-N1, M-N5 o MS-3. Restricción contra MS-4: no puede haber dos préstamos sin devolución del mismo ejemplar (la misma de RI-01; MR-04). Contraejemplo: cargar el mismo ejemplar, lector y fecha dos veces: el segundo se rechaza. Pedir cuidado no alcanza: los voluntarios cambian, trabajan con fila y no ven lo que cargó el otro.'],
    ['Nivel 3', 'Con el modelo, un libro prestado tiene un préstamo sin fecha de devolución; uno que volvió y nadie registró es un préstamo abierto de un ejemplar que está en el estante. El modelo no lo distingue solo: hace falta un control físico. Decisión del encargado para los casos viejos (V-11): revisar el estante y cerrar esos préstamos con una nota, sin borrarlos, y dejar constancia de la fecha del control. Con MC-1 aceptada: un tipo de lector (estudiante o docente), los docentes como lectores, un parámetro de plazo por tipo (siete días y un mes) y el vencimiento calculado con el plazo del tipo; ninguna entidad nueva.'],
]
COTEJO_P7 = [
    ['Cada préstamo es de un ejemplar; el modelo distingue obra y ejemplar.', 'Indicador 1'],
    ['Las relaciones tienen cardinalidad y se justifican con una norma, un requisito o una situación.', 'Indicador 2'],
    ['La pérdida y la reposición se registran sin borrar nada.', 'Indicador 3'],
    ['El diccionario dice significado, obligatoriedad, ejemplo y origen de cada campo (Nivel 2 o 3).', 'Indicador 4'],
    ['La restricción contra la doble carga tiene un contraejemplo que la prueba (Nivel 2 o 3).', 'Indicadores 3 y 5'],
]
CRIT_C7 = [['8', '4: dos entidades bien elegidas (2), dos relaciones con su cardinalidad (2).', 'Un punto por cada parte. No resta dibujar o escribir.'],
           ['9', '4: no borrar la reserva (1), quién canceló (1), cuándo (1), restricción que excluye las canceladas (1).', 'Si la restricción no excluye las canceladas, 0 en esa parte.']]
ERRORES_DER = [
    ['Poner la obra como lo que se presta', 'El préstamo es de un ejemplar; la obra se busca'],
    ['Dibujar los atributos en elipses alrededor de cada entidad', 'En este libro, los atributos van en el diccionario (decisión de Fernando)'],
    ['Usar flechas o símbolos UML entre entidades', 'Líneas sin flecha, rombos y cardinalidades 1 y N'],
    ['Guardar «disponible» o la cantidad de préstamos activos', 'Son datos derivados: se calculan (Tabla 7.4)'],
    ['Resolver el historial con «eliminar en cascada»', 'Contradice RN-05 y RN-06: el préstamo se cierra y el lector se inactiva'],
    ['Anotar «Docente» en el curso', 'Tipo de lector aparte (RF-11); curso vacío para docentes (RI-06)'],
]

# ---------------------------------------------------------------- capítulo 8
SEC_C8 = [
    ('Encuentro 15 — Recorridos, pantallas y bocetos (5 HC de diseño)', [
        ['Problema y explicación', 'aprox. 1 HC', 'Sección 8.1 con las Tablas 8.1 y 8.2 y la Figura 8.1. Se insiste en la diferencia con los diagramas del Capítulo 5.'],
        ['Práctica', 'aprox. 3 HC', 'Tablas 8.3 y 8.4 y Ejemplo resuelto 8.1. Sección 8.2 con la Tabla 8.5, la Figura 8.2 y el Ejemplo resuelto 8.2. Cada equipo dibuja los bocetos de las tres tareas (evidencia). Actividades 1 a 4.'],
        ['Revisión y cierre', 'aprox. 1 HC', 'Recorrido de cada prototipo en papel con el dedo, entre equipos. Evidencia (Work, encuentro 15): tres tareas completas en prototipo de baja fidelidad. El Desafío queda como tarea.'],
    ]),
    ('Encuentro 16 — Estados, mensajes, accesibilidad y revisión con usuarios (5 HC: 3 de diseño y 2 de verificación)', [
        ['Estados y mensajes', 'aprox. 1 HC', 'Sección 8.3 con la Figura 8.3, la Tabla 8.6 y el Ejemplo resuelto 8.3. Actividad 1.'],
        ['Accesibilidad', 'aprox. 1 HC', 'Sección 8.4 con la Tabla 8.7. Actividades 2 y 3. Cada equipo agrega estados y mensajes a sus bocetos.'],
        ['Sesión con usuarios simulados', 'aprox. 2 HC (verificación)', 'Con las tarjetas de rol de esta guía: un integrante hace de usuario, otro conduce y otro observa. Registro de problemas como la Tabla 8.8. Ejemplo resuelto 8.4.'],
        ['Corrección', 'aprox. 1 HC', 'Bocetos corregidos con su versión (evidencia de Work, encuentro 16: registro de problemas y bocetos corregidos). Práctica 8 en el nivel que indique el docente; Actividad 4 y Desafío como tarea.'],
    ]),
]
TARJETAS = [
    ['Bibliotecaria en el recreo', 'Registrá el préstamo del ejemplar EJ-0458 al lector LE-0123. Hay fila: tenés dos minutos.', 'Si el lector o el ejemplar tiene un problema, ¿el mensaje te dice qué hacer?'],
    ['Bibliotecaria que solo usa el teclado', 'Registrá la devolución del ejemplar EJ-0457 sin usar el ratón.', 'Orden de Tab, foco visible y Enter para confirmar (A-02, A-03).'],
    ['Estudiante que consulta', 'Averiguá si hay algún ejemplar disponible de un libro del que solo recordás la palabra «arroyo».', 'Estado vacío (ME-08), «0 disponibles» (ME-09) y que no aparezcan datos de lectores.'],
    ['Reemplazo de la bibliotecaria', 'Es tu primer día. Encontrá qué libros están vencidos hoy.', 'Etiquetas con palabras de la biblioteca (A-06) y la meta de RNF-01: hacerlo sin ayuda.'],
    ['Observador', 'Anotá lo que la persona hace, dónde se detiene y qué pregunta. No ayudes ni expliques.', 'Cada problema con su evidencia; las opiniones van aparte.'],
]
CLAVES_E15 = [
    ['1', '(a) Mapa de navegación: acción con verbo. (b) Diagrama de contexto del Capítulo 5: flujo de información con sustantivo. (c) Boceto. (d) Mapa de navegación: zona por rol. (e) Diagrama de actividades del Capítulo 5.', 'Confundir (a) y (b) porque las dos son flechas.'],
    ['2', 'CU-05: 1 | PT-08 | escribe el código del lector o del ejemplar | muestra sus datos y su historial. 2 | PT-08 | pulsa «Inactivar» | pide confirmar. 3 | PT-08 | confirma | lo marca inactivo sin borrar su historial (RF-10, RN-06) y muestra la confirmación.', 'Usar «borrar» en un paso.'],
    ['3', 'Boceto de PT-07 con el título, una lista con ejemplar, título, lector y vencimiento (RF-08), una marca de «vencido» con texto y no solo con color (A-04) y «Volver al inicio». Se acepta un campo de fecha de referencia. Cada elemento justificado con RF-08 o con la Tabla 8.7.', 'Elementos sin requisito o vencidos marcados solo en rojo.'],
    ['4', 'No: la consulta pública no debe mostrar datos personales (RNF-03, E5-L6) y la mayoría de los lectores son menores de edad. Se puede mostrar «0 disponibles por ahora» o la fecha probable de devolución sin el nombre, si se tramita como solicitud de cambio.', 'Aceptar porque «es útil».'],
    ['5', 'Respuesta abierta. Opción esperada: PT-07 pasa a ser accesible también desde la zona de la dirección, o se agrega una pantalla «Vencidos» en esa zona, con una transición «Ver vencidos» desde PT-09. Hay que revisar qué datos ve la dirección (RNF-03) y tramitarlo como cambio.', 'Agregar la pantalla en la zona pública.'],
]
CLAVES_E16 = [
    ['1', '(a) Error. Por ejemplo: «No se pudo guardar: falta el código del ejemplar. Escribilo y volvé a pulsar Prestar.» (b) Confirmación: «Préstamo registrado. Vence el 09/03.» (c) Vacío: «Todavía no hay préstamos activos.» o «Escribí el código del lector para empezar.» (d) Carga: «Guardando… (el botón queda desactivado)».', 'Mensajes que no dicen qué hacer.'],
    ['2', 'Error: «No se puede inactivar: este lector tiene 1 préstamo activo. Registrá la devolución antes.» (se acepta otra decisión si se justifica con RN-06 y RF-10). Confirmación: «Ejemplar inactivado. Su historial se conserva y ya no aparece como disponible.»', 'Confirmar con «Borrado».'],
    ['3', 'Respuesta abierta. Ejemplos: el campo del lector de PT-05 tiene etiqueta visible (cumple A-01); hay que comprobar que Tab vaya de un código al otro y después a «Prestar» (A-02); la zona de mensaje está junto al botón (A-05). Se valora que cite el código de la lista.', 'Decir «cumple todo» sin revisar punto por punto.'],
    ['4', 'Es una opinión, no una observación: no muestra lo que la persona hizo. Para decidir con evidencia, se prueba el recorrido con las pantallas actuales y, si hace falta, con una versión en una sola pantalla, y se compara si la persona completa la tarea sin ayuda (RNF-01).', 'Cambiar el boceto porque lo dijo una persona.'],
    ['5', 'Estado de carga en PT-02: «Buscando…», el botón «Buscar» desactivado y el campo visible con lo que se escribió. No debería poder lanzar otra búsqueda ni ver resultados parciales con datos de otra consulta. Si la espera es larga, un mensaje que diga qué hacer: «La computadora está lenta: esperá un momento.»', 'Pantalla en blanco mientras carga.'],
]
CLAVES_P8 = [
    ['Nivel 1', 'OBS-1: privacidad (muestra el teléfono de la familia; MN-05). OBS-2: etiqueta (A-06). OBS-3: estado vacío sin mensaje. OBS-4: estado de carga (falta desactivar el botón; ME-11). OBS-5: teclado (A-02 y A-07: «Borrar todo» al lado del campo). OBS-6: mensaje (A-04: error solo con color). Dos correcciones, cada una con su observación: por ejemplo, «Registrar devolución» en lugar de «Cerrar transacción» (OBS-2) y botón desactivado con «Guardando…» (OBS-4).'],
    ['Nivel 2', 'Mensajes con qué pasó, por qué y qué hacer. Para OBS-6: «No se puede prestar: ese libro ya está prestado. Elegí otro ejemplar.» Confirmación: «Préstamo registrado. Vence el …». El estado de carga desactiva el botón mientras se guarda, pero no alcanza: si dos voluntarios usan dos computadoras o la pantalla falla, solo la restricción del modelo (un préstamo sin devolución por ejemplar, Práctica 7) impide el préstamo doble.'],
    ['Nivel 3', 'El voluntario (menor de edad, MS-5) trabaja con el encargado presente y con permisos mínimos: puede buscar un libro y, si la escuela lo decide, preparar un préstamo que el encargado confirma. Nunca ve teléfonos, direcciones ni historiales de otros estudiantes (MN-05, MR-07), y no tiene funciones administrativas (inactivar, informes, cuentas). Se acepta también que no use el sistema y solo ayude con el estante. Mapa: zona «Encargado» con préstamo, devolución e informe; si se justifica, una zona «Voluntario» con la búsqueda y la carga supervisada, sin acceso a datos personales.'],
]
COTEJO_P8 = [
    ['Cada observación se clasifica y se relaciona con un punto de la Tabla 8.7 o con un estado.', 'Indicadores 3 y 4'],
    ['Cada corrección cita la observación que la justifica.', 'Indicador 5'],
    ['Los mensajes dicen qué pasó, por qué y qué hacer (Nivel 2 o 3).', 'Indicador 3'],
    ['El voluntario no ve datos personales ni tiene funciones administrativas (Nivel 3).', 'Indicadores 1 y 5'],
    ['El mapa usa solo pantallas, transiciones con verbo, inicio y zonas (Nivel 3).', 'Indicador 1'],
]
CRIT_C8 = [['8', '4: recorrido completo (1), tres pantallas o más (1), flechas rotuladas con la acción (1), zona propia para la secretaria (1).', 'Un punto por cada parte.'],
           ['9', '4: un punto por cada estado con un mensaje que dice qué pasó y qué hacer.', 'Sin punto si el mensaje es «Error» o «Listo» sin más.']]
ERRORES_NAV = [
    ['Rotular las flechas del mapa con sustantivos («informe»)', 'La acción del usuario, con verbo: «Ver informe»'],
    ['Dibujar carriles o decisiones en el mapa', 'Eso es un diagrama de actividades; el mapa solo tiene pantallas, transiciones, inicio y zonas'],
    ['Poner pantallas de la bibliotecaria en la zona pública', 'Cada pantalla en la zona del rol que la puede ver (RNF-02, RNF-03)'],
    ['Bocetos con colores, logotipos o capturas de un programa real', 'Cajas grises y etiquetas; el aspecto se decide después'],
    ['Estados que faltan: solo la pantalla «cuando todo sale bien»', 'Vacío, carga, error y confirmación, con su mensaje'],
    ['Anotar opiniones en el registro de la sesión', 'Lo que la persona hizo; las opiniones van aparte'],
]

# ---------------------------------------------------------------- capítulo 9
SEC_C9 = [
    ('Encuentro 17 — Responsabilidades, contratos y entorno (5 HC de diseño)', [
        ['Problema y explicación', 'aprox. 1 HC', 'Sección 9.1 con la Tabla 9.1, la Figura 9.1 y la Tabla 9.2. Actividad 1.'],
        ['Práctica', 'aprox. 3 HC', 'Sección 9.2 con la Tabla 9.3, el Ejemplo resuelto 9.1 y la Tabla 9.4; Actividad 2 (aprox. 1 HC). Sección 9.3 con la Tabla 9.5 y el Ejemplo resuelto 9.2; Actividad 4 (aprox. 1 HC). Sección 9.4 con la Tabla 9.6 y el Ejemplo resuelto 9.3; Actividad 3 (aprox. 1 HC). Evidencia (Work, encuentro 17): esquema de arquitectura y decisión técnica.'],
        ['Revisión y cierre', 'aprox. 1 HC', 'Cada equipo aplica la lista de verificación del H3 a su dossier (Actividad 1 del Encuentro 18, adelantada) y reparte lo que falta. El Desafío queda como tarea.'],
        ['Complemento (fuera de las 5 HC)', 'aprox. 1 HC', 'Práctica 9, complemento editorial: como tarea o como actividad complementaria. No ocupa tiempo del Encuentro 18 ni reemplaza el H3.'],
    ]),
    ('Encuentro 18 — Evaluación integradora de la primera etapa, H3 (5 HC: 4 de evaluación y 1 de diseño)', [
        ['Defensa del dossier', 'aprox. 4 HC (evaluación)', 'Cada equipo presenta su dossier de las Unidades I a III (unos 15 minutos). Durante la defensa, el docente le propone a cada integrante una variante del banco (sección 4) y registra su resolución individual. Se completa la planilla.'],
        ['Corrección del dossier', 'aprox. 1 HC (diseño)', 'Cada equipo registra las observaciones en la bitácora, corrige y registra la versión nueva (Actividad 2 del Encuentro 18). Si un equipo no llegó a defender, la defensa se reprograma; no se acorta la corrección de los demás.'],
    ]),
]
CLAVES_E17 = [
    ['1', '(a) Presentación (ME-09). (b) Reglas de negocio (RI-03). (c) Persistencia (RI-04). (d) Reglas de negocio, que leen Parámetro en la persistencia. (e) Presentación (ME-11).', 'Poner (d) en la presentación.'],
    ['2', 'OP-06. Entradas: código del lector o del ejemplar y cuenta. Precondiciones: rol de bibliotecaria (RNF-02). Resultado: queda inactivo y su historial no cambia (RI-05). Errores: ME-12 (sin permiso), código inexistente (ME-05 para el ejemplar o un mensaje equivalente para el lector) y el error nuevo, «el lector tiene un préstamo activo», con un mensaje como el de la Actividad 2 del Encuentro 16. Requisitos: RF-10, RNF-02, RN-06.', 'Contrato sin errores o con «borrar».'],
    ['3', 'Ejemplos de huecos: RF-09 no tiene mensaje de vacío para un mes sin préstamos (se agrega un ME nuevo en PT-09); RS-02 no tiene pantalla, y está bien porque es una condición del entorno; RNF-01 no tiene operación, y está bien porque se verifica con la sesión de usuarios (P-14). Se acepta cualquier hueco real con su corrección.', 'Decir «no hay huecos» sin revisar fila por fila.'],
    ['4', 'Porque cualquiera puede enviar un pedido al servidor sin usar la pantalla, o la pantalla puede fallar. Las reglas y los permisos se comprueban siempre en las reglas de negocio (Work §7.5). Ocultar el botón ayuda a la persona, pero no protege los datos.', 'Aceptar que ocultar alcanza.'],
    ['5', 'Respuesta abierta. Se valora que la opción D nombre un entorno concreto, que se le apliquen RS-01 y RS-02 antes de compararla y que diga qué hay que verificar antes de la Unidad IV: que se instala en la computadora real, que funciona sin internet, que no requiere licencias, que hay quien la mantenga y cómo se respalda el archivo de datos. No se aceptan puntajes.', 'Elegir por gusto o con una tabla de puntajes.'],
]
CLAVES_E18 = [
    ['1', 'Respuesta abierta. Se valora que cada punto que no se cumple tenga qué falta, quién lo completa y para cuándo, antes de la defensa.', 'Lista sin responsables.'],
    ['2', 'Bitácora con la fecha, cada observación recibida, la corrección hecha, el documento afectado y su versión nueva (por ejemplo, catálogo v1.2 o modelo de datos v2).', 'Corregir sin registrar la versión.'],
]
CLAVES_P9 = [
    ['Nivel 1', 'Entradas: código del libro (o del ejemplar) devuelto, si vuelve dañado y la cuenta que opera. Precondiciones: la cuenta es del encargado. Resultado: el préstamo tiene su fecha de devolución y no se borra; si el libro volvió dañado, queda marcado como dañado y no disponible. Errores: libro inexistente, libro sin préstamo activo, sin permiso y libro dañado (se registra y se avisa que hay que reponerlo, M-N5). Requisitos: MR-02 (y MR-04 o MR-01 si se citan). La decisión de no prestarlo es de las reglas de negocio; que está dañado se guarda en la persistencia, en el ejemplar.'],
    ['Nivel 2', 'El préstamo se cierra con su fecha y la marca de daño; el ejemplar dañado queda inactivo o «dañado», sin borrarse; el ejemplar que lo repone es un ejemplar nuevo, con su código, vinculado a la misma obra (y si se quiere, a la reposición del dañado). Contrato «registrar reposición»: entradas, código del ejemplar dañado y datos del nuevo, cuenta; precondición, encargado y ejemplar marcado dañado; resultado, ejemplar nuevo activo y el dañado sigue en el historial; errores, ejemplar no dañado, código repetido, sin permiso; requisitos, M-N5, MR-01. Mensaje: «Devolución registrada. El libro quedó marcado como dañado y no se va a prestar hasta reponerlo.»'],
    ['Nivel 3', 'Contexto: computadora donada sin internet (M-F7, M-F2), sin dinero para programas (M-F3), el encargado con cuatro horas (M-F4) y nadie que sepa instalar (M-F9). Condiciones excluyentes: sin internet y sin costo. Opciones: una aplicación local sencilla, una planilla con hojas protegidas o seguir con fichas mejoradas. La decisión tiene que decir quién instala y mantiene (el profesor que viene una vez por mes), cómo se respalda el archivo y qué pasa si la computadora falla. Consecuencias para el encargado: aprender a usarla y hacer el respaldo; el profesor verifica la instalación, el respaldo y que funcione sin conexión. No se aceptan puntajes.'],
]
COTEJO_P9 = [
    ['El contrato tiene sus cinco partes y cada error tiene un mensaje.', 'Indicador 2'],
    ['El libro dañado no se borra ni se presta; la reposición conserva el historial (Nivel 2 o 3).', 'Indicadores 1 y 2'],
    ['La decisión técnica descarta primero lo que no cumple las condiciones excluyentes, sin puntajes (Nivel 3).', 'Indicador 3'],
    ['La decisión dice quién mantiene el entorno y cómo se respalda (Nivel 3).', 'Indicador 3'],
]
CRIT_C9 = [['8', '4: entradas (1), precondición de U-3 (1), resultado (1), errores con su fuente U-2 o U-3 (1).', 'Un punto por cada parte.'],
           ['9', '4: contexto (1), condiciones excluyentes (1), opciones (1), decisión con una consecuencia (1).', '0 en la decisión si usa puntajes.']]
ERRORES_CAPAS = [
    ['Poner las reglas en la pantalla («el botón no aparece»)', 'La regla se comprueba en las reglas de negocio; la pantalla solo ayuda'],
    ['Dibujar flechas de la persistencia a la presentación', 'La pantalla pide a las reglas; las reglas leen y guardan'],
    ['Contratos sin errores o con errores sin mensaje', 'Un error por flujo alternativo, con su ME'],
    ['Elegir el entorno con una tabla de puntajes', 'Condiciones excluyentes primero; razones, no puntajes'],
    ['Presentar el entorno de referencia como obligatorio', 'Es un ejemplo provisional, a verificar en los equipos reales'],
]

RUBRICA_EXPLICACION = [
    'El H3 se califica con la misma lógica que el H1 y el H2: para cada criterio se registran el nivel del producto del equipo '
    'y el nivel individual de cada integrante, y se combinan en la proporción 60 % (equipo) y 40 % (individual). Por ejemplo, '
    'con 4, 3, 2 y 1 puntos para Sólido, Logrado, En desarrollo e Inicial, un producto Sólido (4) con una evidencia individual '
    'En desarrollo (2) da 4 × 0,6 + 2 × 0,4 = 3,2. La conversión a calificación la decide la institución.',
    'La evidencia individual es la resolución de una variante que no se resolvió antes, propuesta por el docente durante la '
    'defensa, el aporte registrado en la bitácora y la observación del docente. Las variantes salen del banco de esta guía y '
    'no están en el dossier, en el buzón, en la nota D3 ni en las prácticas.',
    'La ausencia de evidencia se registra aparte («AE»), con la fecha acordada para entregarla; no se confunde con un '
    'desempeño de nivel Inicial. Después de la defensa, el equipo tiene la última hora del encuentro para corregir el dossier '
    'y registrar la versión nueva. La proporción 60/40 y los niveles son una propuesta editorial tomada del informe de Work '
    '(§4.3); no son una escala oficial del MEC.',
]
CALENDARIO_28 = (['Encuentro (36)', 'Encuentro (28)', 'Qué se hace'],
                 [['13', '10', 'Sin cambios: antecedentes de Algorítmica y modelo del dominio.'],
                  ['14', '11', 'Sin cambios: integridad, historial y diccionario, con la revisión con contraejemplos.'],
                  ['15 y 16', '12', 'Se unen: tres recorridos en baja fidelidad (Figura 8.2) y una sola sesión de revisión entre equipos, con las tarjetas de rol.'],
                  ['17', '13', 'Sin cambios: capas, contratos, decisión técnica y matriz de coherencia.'],
                  ['18', '14', 'Sin cambios: H3, defensa y corrección del dossier.']])
PROCEDENCIA = (['Recurso', 'Procedencia', 'Derechos'],
               [['Texto de los Capítulos 7 a 9 y de la apertura de la unidad', 'Redacción original para este libro.', 'Propios del proyecto.'],
                ['Figuras 7.1 a 9.1 y leyendas de símbolos', 'Generadas con build/diagramas_u3.py desde caso/diseno.py, una función por símbolo y por notación, con registro de símbolos.', 'Propias; sin recursos de terceros.'],
                ['Notación entidad-relación', 'La notación clásica que usa Algorítmica 3.º de la colección, simplificada: atributos en el diccionario (decisión de Fernando).', 'Conocimiento general de la disciplina; no se copiaron figuras ni ejercicios.'],
                ['Mapa de navegación y boceto de baja fidelidad', 'Símbolos aprobados por Fernando (20-oct-2026).', 'Propios.'],
                ['Caso Arapoty: modelo, pantallas, mensajes, operaciones, DT-01 y coherencia', 'Inventados. Fuente única: lote_3/caso/diseno.py, que lee sin modificarlos lote_1/caso/dossier.py y lote_2/caso/requisitos.py y modelos.py.', 'Propios del proyecto.'],
                ['Caso de práctica Mbokaja (Unidad III)', 'Inventado para este lote: lote_3/caso/mbokaja_u3.py, que amplía las fuentes de Mbokaja de los lotes 1 y 2.', 'Propio.'],
                ['Capacidades, niveles de desempeño, proporción 60/40, secuencia de encuentros y ruta técnica de referencia', 'Informe de Work v0.1 (§3, §4.2, §4.3, §5.2, §7.5), como propuesta editorial. La ruta técnica es un ejemplo provisional, no probado en equipos escolares.', 'Insumo interno del proyecto.'],
                ['Relación con Algorítmica 3.º', 'Se citan sus clases para la recuperación; no se reutilizaron ejercicios, tablas, personas ni títulos de ese libro, ni su matriz de selección tecnológica.', 'No aplica.']])


def _sec(doc, secuencia):
    for titulo, filas in secuencia:
        M.tabla(doc, (['Momento', 'Tiempo', 'Qué se hace'], filas), ANCHO_SEC, rotulo=titulo)


def _claves(doc, rotulo, filas):
    M.tabla(doc, (['Act.', 'Respuesta esperada', 'Error frecuente'], filas), [1.2, 11.0, 4.4], rotulo=rotulo)


def _eval(doc, C, claves, crit):
    filas = [[str(n), clave, detalle] for eid, n, clave, detalle in claves if eid == C.EVAL_ID]
    M.tabla(doc, (['Ítem', 'Clave', 'Respuesta o criterio'], filas), [1.2, 1.8, 13.6], rotulo='Clave de la %s' % C.EVAL_TITULO.lower())
    M.tabla(doc, (['Ítem', 'Puntaje completo', 'Puntaje parcial'], crit), [1.2, 8.4, 7.0], rotulo='Criterios de corrección de los ítems abiertos')


def _niveles(doc, rotulo, filas):
    M.tabla(doc, (['Nivel', 'Respuesta esperada'], filas), [2.2, 14.4], rotulo=rotulo)


def _errores(doc, rotulo, filas):
    M.tabla(doc, (['Error frecuente', 'Cómo se corrige'], filas), [8.6, 8.0], rotulo=rotulo)


def construir(ruta, claves, paginas, estado, figs):
    import cap3   # niveles de desempeño del lote 1
    doc = H.new_doc()
    Z.portada(doc, 'Guía docente con solucionario', estado)
    doc.add_heading('Guía docente — Lote 3', level=1)
    H.caja(doc, 'Sobre las capacidades y el entorno técnico', [
        'Las capacidades de las fichas (C5, C6 y C9 en esta unidad, y C1 a C7 en el H3) son propuestas para el programa '
        'institucional del Plan Optativo, tomadas del informe de Work. No son capacidades oficiales del MEC.',
        'El entorno del Capítulo 9 (HTML y CSS, PHP y SQLite, en una computadora local) es un ejemplo técnico provisional: no '
        'es obligatorio, no está aprobado para todos los colegios y no se probó todavía en equipos escolares. No requiere '
        'servicios pagos. La institución puede usar otro entorno que cumpla RS-01 y RS-02.'], tipo='neutra')
    H.p_texto(doc, 'Cada encuentro sigue la estructura de taller de Work: 1 HC de problema y explicación, 3 HC de práctica y '
                   '1 HC de revisión, con la distribución por categorías de la versión 2.1 (diseño, verificación y '
                   'evaluación en esta unidad). Los tiempos son aproximados y la duración de la hora cátedra la fija cada '
                   'institución.', italic=True, size=9.5)

    # 0. articulación
    doc.add_heading('Antes del Encuentro 13: acuerdo con Algorítmica 3.º', level=2)
    for t in ALGORITMICA:
        H.p_texto(doc, t)

    # 1. capítulo 7
    K.titulo_en_pagina_nueva(doc, '1. Capítulo 7 — %s' % cap7.TITULO, nivel=2)
    M.ficha(doc, cap7)
    _sec(doc, SEC_C7)
    Z.tabla_leyenda(doc, 'der', 'Leyenda: modelo entidad-relación (notación de Algorítmica 3.º)', figs)
    _errores(doc, 'Errores frecuentes con el modelo de datos', ERRORES_DER)
    _claves(doc, 'Claves de las actividades del Encuentro 13', CLAVES_E13)
    _claves(doc, 'Claves de las actividades del Encuentro 14', CLAVES_E14)
    _niveles(doc, 'Práctica 7: claves por nivel', CLAVES_P7)
    M.tabla(doc, (['Criterio', 'Indicador'], COTEJO_P7), [13.0, 3.6], rotulo='Lista de cotejo de la Práctica 7')
    _eval(doc, cap7, claves, CRIT_C7)

    # 2. capítulo 8
    K.titulo_en_pagina_nueva(doc, '2. Capítulo 8 — %s' % cap8.TITULO, nivel=2)
    M.ficha(doc, cap8)
    _sec(doc, SEC_C8)
    Z.tabla_leyenda(doc, 'navegacion', 'Leyenda: mapa de navegación', figs)
    Z.tabla_leyenda(doc, 'boceto', 'Leyenda: boceto de baja fidelidad', figs)
    _errores(doc, 'Errores frecuentes con el mapa y los bocetos', ERRORES_NAV)
    H.p_texto(doc, 'Tarjetas de rol para la sesión del Encuentro 16. Se recortan y se entregan una por integrante; el docente '
                   'puede cambiar los códigos por los del boceto de cada equipo. Ninguna tarjeta usa datos de personas '
                   'reales.', size=10)
    M.tabla(doc, (['Rol', 'Tarea', 'Qué se observa'], TARJETAS), [3.8, 7.0, 5.8], rotulo='Tarjetas de rol del Encuentro 16')
    _claves(doc, 'Claves de las actividades del Encuentro 15', CLAVES_E15)
    _claves(doc, 'Claves de las actividades del Encuentro 16', CLAVES_E16)
    _niveles(doc, 'Práctica 8: claves por nivel', CLAVES_P8)
    M.tabla(doc, (['Criterio', 'Indicador'], COTEJO_P8), [13.0, 3.6], rotulo='Lista de cotejo de la Práctica 8')
    _eval(doc, cap8, claves, CRIT_C8)

    # 3. capítulo 9
    K.titulo_en_pagina_nueva(doc, '3. Capítulo 9 — %s' % cap9.TITULO, nivel=2)
    M.ficha(doc, cap9)
    _sec(doc, SEC_C9)
    Z.tabla_leyenda(doc, 'capas', 'Leyenda: esquema de capas', figs)
    _errores(doc, 'Errores frecuentes con la arquitectura', ERRORES_CAPAS)
    H.p_texto(doc, 'Contratos de referencia de las operaciones que el libro no desarrolla (OP-04 y OP-05). OP-06 es la '
                   'Actividad 2 del Encuentro 17 y su clave está abajo.', size=10)
    for op in ('OP-04', 'OP-05'):
        Z.contrato(doc, op)
    _claves(doc, 'Claves de las actividades del Encuentro 17', CLAVES_E17)
    _claves(doc, 'Claves de las actividades del Encuentro 18', CLAVES_E18)
    H.p_texto(doc, 'La Práctica 9 es un complemento editorial al índice de Work: se asigna en el Encuentro 17 como tarea o '
                   'actividad complementaria y no se evalúa en el H3.', size=10)
    _niveles(doc, 'Práctica 9: claves por nivel', CLAVES_P9)
    M.tabla(doc, (['Criterio', 'Indicador'], COTEJO_P9), [13.0, 3.6], rotulo='Lista de cotejo de la Práctica 9')
    _eval(doc, cap9, claves, CRIT_C9)

    # 4. rúbrica H3
    K.titulo_en_pagina_nueva(doc, '4. Rúbrica del hito H3: dossier consistente y evidencia individual', nivel=2)
    for t in RUBRICA_EXPLICACION:
        H.p_texto(doc, t)
    M.tabla(doc, (['Criterio', '4. Sólido', '3. Logrado', '2. En desarrollo', '1. Inicial'],
                  [['%s (%s)' % (r[0], r[1])] + r[2] for r in cap9.RUBRICA_H3]),
            [2.8, 3.6, 3.4, 3.4, 3.4], rotulo='Rúbrica del H3: descriptores por nivel', size=8.5)
    M.tabla(doc, (['Criterio', 'Evidencia del equipo (60 %)', 'Evidencia individual (40 %)'],
                  [[r[0], r[3], r[4]] for r in cap9.RUBRICA_H3]), [4.4, 5.8, 6.4], rotulo='Evidencias de cada criterio del H3')
    M.tabla(doc, (['Nivel de desempeño', 'Descriptor común (Work §4.3)'], [list(x) for x in cap3.NIVELES_DESEMPENO]),
            [3.6, 13.0], rotulo='Niveles de desempeño (propuesta editorial)')
    M.tabla(doc, (['Estudiante (código)', 'Criterio', 'Nivel del equipo', 'Nivel individual', 'Resultado', 'AE'],
                  [['', r[0], '', '', '', ''] for r in cap9.RUBRICA_H3]),
            [3.0, 5.0, 2.2, 2.2, 2.2, 2.0], rotulo='Planilla de registro del H3 (una por estudiante)')
    M.tabla(doc, (['Código', 'Variante', 'Qué tiene que encontrar el estudiante'], [list(v) for v in X.BANCO_H3]),
            [1.6, 7.0, 8.0], rotulo='Banco de variantes para la evidencia individual del H3')
    H.p_texto(doc, 'Ninguna de estas variantes está en el dossier, en el buzón, en la nota D3 ni en las prácticas. Se asigna '
                   'una por integrante; si el curso trabaja con su propia biblioteca, el docente formula una variante '
                   'equivalente a partir del relevamiento autorizado.', italic=True, size=9.5)

    # 5. calendario y 6. procedencia
    doc.add_heading('5. Calendario con menos encuentros', level=2)
    H.p_texto(doc, 'En la adaptación de 28 encuentros (distribución v2.1), la Unidad III pasa de seis a cinco encuentros: se '
                   'unen el 15 y el 16. Cada capítulo del libro tiene su recuadro «Si el calendario se acorta».')
    M.tabla(doc, CALENDARIO_28, [2.6, 2.6, 11.4], rotulo='Unidad III en 36 y en 28 encuentros')
    doc.add_heading('6. Procedencia y derechos de los recursos', level=2)
    M.tabla(doc, PROCEDENCIA, [4.4, 7.8, 4.4], rotulo='Inventario de recursos del lote')
    M.pegar_renglones(doc)
    Z.encadenar_inicio(doc)
    K.saltos_a_titulos(doc)
    H.finalizar(doc, ruta)

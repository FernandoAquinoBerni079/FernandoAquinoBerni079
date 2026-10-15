# -*- coding: utf-8 -*-
"""Guía docente del lote 1 (preliminares y Capítulos 1 a 3): secuencia de cada encuentro en HC, claves de las
actividades, prácticas y evaluaciones, listas de cotejo, tarjetas de rol, mapa de apoyos, rúbrica del H1,
calendario de 28 encuentros, coordinación con otras asignaturas y procedencia de los recursos."""
import helpers as H
import maqueta as M
import comun as K
import prelim as P
import cap1, cap2, cap3
MB = cap1.MB
D = K.D

ANCHO_SEC = [3.2, 2.2, 11.2]

# ---------------------------------------------------------------- preliminares
DIAG_CLAVES = [
    ['1', 'Muestra 3 (los valores 9, 12 y 8 superan 7).', 'Contar también el 7.'],
    ['2', 'cupo_libre > 0 Y NO inscripto_en_mismo_horario (o una frase equivalente con «y» y la negación explícita).', 'Usar «o» en lugar de «y».'],
    ['3', 'Para reutilizar código, separar tareas, probar cada parte y cambiar una parte sin tocar el resto.', 'Responder solo «para ordenar».'],
    ['4', 'Nombre: campo de texto. Curso: lista desplegable o botones de opción. Normas: casilla de verificación.', 'Campo de texto libre para el curso.'],
    ['5', 'Se envían al servidor (por GET o POST) a la dirección que indica el formulario; quien los recibe tiene que validarlos, sin confiar en lo que mandó el navegador.', 'Creer que «quedan guardados en la página».'],
    ['6', '2 (E-03 y E-04).', 'Contar todos los de Robótica (4).'],
    ['7', 'Permite filtrar, ordenar y contar por curso sin separar textos, y evita escribir el curso de formas distintas.', '—'],
    ['8', 'Se presenta, dice para qué es, cuánto dura y que puede no aceptar; registro formal.', 'Omitir la posibilidad de negarse.'],
    ['9', 'Ejemplo: «En el primer recreo, la fila de la biblioteca hace que muchos estudiantes se vayan sin libro y que la bibliotecaria anote con errores.»', 'Copiar una oración del texto.'],
]
DIAG_AREAS = 'Programación: ítems 1 a 3. Formularios: ítems 4 y 5. Datos: ítems 6 y 7. Comunicación: ítems 8 y 9.'

# ---------------------------------------------------------------- capítulo 1
SEC_C1 = [
    ('Encuentro 1 — El reto y el sistema que ya existe (5 HC)', [
        ['Presentación y diagnóstico', 'aprox. 1,5 HC', 'Presentación del libro y del caso (preliminares). Diagnóstico de entrada, individual y sin nota: es la «resolución individual breve» de Work. Autoevaluación por área.'],
        ['Explicación y práctica', 'aprox. 2,5 HC', 'Sección 1.1 con la Tabla 1.1 y el Ejemplo resuelto 1.1 (ficha de problema). Sección 1.2 con la Figura 1.1 y el Ejemplo resuelto 1.2. Actividades 1 a 3, en parejas.'],
        ['Revisión y cierre', 'aprox. 1 HC', 'Actividad 4 en plenario. Los equipos firman el acuerdo de trabajo de los preliminares. El docente recoge los diagnósticos y arma el mapa de apoyos del curso (evidencia del Encuentro 1). La Actividad 5 queda como tarea.'],
    ]),
    ('Encuentro 2 — Interesados, punto de partida y práctica (5 HC)', [
        ['Problema y explicación', 'aprox. 1 HC', 'Devolución del diagnóstico. Sección 1.3 con la Figura 1.2, el Ejemplo resuelto 1.3 y las Tablas 1.4 y 1.5.'],
        ['Práctica', 'aprox. 3 HC', 'Sección 1.4 con el Ejemplo resuelto 1.4: cada estudiante arma su plan de apoyo (Actividad 3). Actividades 1 y 2. Práctica 1 por niveles (aprox. 1,5 HC).'],
        ['Revisión y cierre', 'aprox. 1 HC', 'Puesta en común de la Práctica 1. Entrega de la ficha de problema y del mapa de actores (evidencia del Encuentro 2). Las Actividades 4 y 5 quedan como tarea.'],
    ]),
]
CLAVES_C1_E1 = [
    ['1', '(a) síntoma; (b) problema de información: falta el dato del estado de los diccionarios; (c) problema que no es de información; (d) solución anticipada; (e) problema de información: el dato llega tarde; (f) problema que no es de información (se acepta «de información» si se justifica que registrar el estado ayudaría a decidir reposiciones). Lo que define (d) es que propone un medio antes de entender el problema.', 'Clasificar (d) como problema.'],
    ['2', 'Personas: profesor de Educación Física, cursos que retiran material, dirección (recibe el aviso). Procesos: prestar, devolver, contar faltantes a fin de mes, avisar. Datos: curso, material y hora; faltantes del mes. Recursos: la hoja, el material, el tiempo del profesor. Límite posible: préstamo, devolución y control mensual dentro; la compra de material, afuera.', 'Poner «la hoja» como dato.'],
    ['3', 'Ejemplo: «Los docentes no cuentan con información confiable sobre qué horarios de la sala de informática están reservados, porque las reservas se anotan en una hoja que se puede borrar.» Hecho: dos docentes coincidieron y una reserva hecha con lápiz fue borrada (relato). A verificar: con qué frecuencia pasa, quién borra, cuántos docentes usan la sala.', 'Proponer un sistema de reservas como problema.'],
    ['4', 'Mejorarían la rapidez y la exactitud al identificar qué ejemplar sale, si cada ejemplar tuviera su código. No dicen si un libro está disponible antes de ir, no producen el informe y no impiden el doble préstamo sin otro control; además exigen etiquetar los ejemplares y comprar equipos. No se adoptan porque es una solución anticipada: se registra y se evalúa después del relevamiento (en el Capítulo 3 queda como extensión).', 'Rechazarla sin dar razones.'],
    ['5', 'Dentro: el sistema gestionaría pedidos y compras, con nuevos actores (cooperadora, dirección) y un alcance mayor. Afuera: el problema central es el préstamo; la compra recibe del sistema información que cruza el límite, como los títulos más pedidos o los pedidos no atendidos. Se valora el argumento de cada lado y que se nombre la información que cruza.', 'Dar una sola posición.'],
]
CLAVES_C1_E2 = [
    ['1', '(a) actora, cuando reemplaza registra préstamos; (b) interesada, no actora; (c) interesado, no actor: instala y cuida los equipos (se acepta actor si se justifica que administraría cuentas); (d) ninguno de los dos para el sistema de préstamos (se acepta interesado lejano si se justifica); (e) actor: lector; (f) interesada que recibe información; es actora si consulta ella misma el informe en el sistema.', 'Confundir «importante» con «actor».'],
    ['2', 'Respuesta abierta. Ejemplos: cooperadora (interés 3, influencia 6: aporta recursos; mantener satisfecha); docente que reemplaza a la bibliotecaria (interés 7, influencia 3; mantener informada y consultarla). Se corrige la coherencia entre puntaje, razón y estrategia.', 'Puntajes sin razón.'],
    ['3', 'Plan con qué repasar, dónde (guía de consulta), con quién, antes de qué encuentro y qué evidencia va a mostrar. Incluye una ayuda que el estudiante ofrece.', 'Plan sin plazos.'],
    ['4', 'Si solo se los informa, se pierden las necesidades de los usuarios más numerosos (saber qué hay antes de ir) y el sistema corre el riesgo de no usarse. Propuestas: cuestionario breve, taller con delegados, delegados en las revisiones; consultan, no deciden solos sobre las reglas.', 'Proponer que los estudiantes voten las reglas.'],
    ['5', 'Decide la dirección (influencia alta; aprueba las reglas). Se consulta a la bibliotecaria (gestionar de cerca) y a los docentes del plan lector. Se informa a estudiantes y familias, y se consulta a los delegados. Supuesto a confirmar: que la dirección aprueba las reglas (lo confirma E5-L8 en el Capítulo 2).', 'No marcar el supuesto.'],
]
CLAVES_P1 = [
    ['Nivel 1', 'Hechos: V-01, V-02, V-03, V-05, V-08, V-09 y V-11 (V-08 y V-09 son testimonios registrados: la cifra de V-08 y el dato de V-09 hay que verificarlos con quien corresponde). Supuestos: V-04, V-06 y V-12. Soluciones anticipadas: V-07 y V-10. Verificación: V-04, comparar fichas con libros que faltan; V-06, preguntar a estudiantes del turno mañana; V-12, revisar las fichas del mes. Ficha: quién: el encargado, los lectores y la dirección; qué falta: quién tiene cada libro y qué libros se leen más (V-08, V-09, V-11); consecuencia: libros que no vuelven (V-08); soluciones anticipadas: V-07 y V-10. Actores: encargado y lectores; interesadas: dirección y la docente que comentó.'],
    ['Nivel 2', 'Lo del Nivel 1 con justificaciones; la oración con cifra a verificar es V-08 («unos quince»). Cinco elementos: personas (encargado, lectores de la tarde, docentes, dirección); procesos (prestar con ficha, devolver tachando, guardar fichas); datos (libro, lector, fechas); recursos (caja, fichas, aula, tres tardes, horas del encargado); límite: préstamo y devolución dentro, compras afuera. Enunciado, por ejemplo: «En la biblioteca de Mbokaja, el encargado y la dirección no saben con certeza quién tiene cada libro prestado ni qué libros se leen más, porque las fichas se pierden o quedan incompletas.» (V-04 es supuesto: se acepta «quedan incompletas» con fuente V-11.)'],
    ['Nivel 3', 'Respuesta abierta. Se controla que el relato no tenga nombres ni datos personales, que hechos y supuestos estén separados y que las diferencias con Mbokaja cambien el problema (por ejemplo, horario, tipo de registro, quién atiende).'],
]
COTEJO_P1 = [
    ['Clasifica cada oración del relato y justifica la clasificación.', 'Indicador 4'],
    ['La ficha de problema distingue lo que se sabe (con fuente V-xx) de lo que hay que averiguar.', 'Indicador 1'],
    ['El enunciado del problema no nombra ninguna solución.', 'Indicador 1'],
    ['Describe el sistema con sus cinco elementos (Nivel 2 o 3).', 'Indicador 2'],
    ['El mapa distingue actores de interesados que no son actores.', 'Indicador 3'],
]
CRIT_C1 = [
    ['8', '4: quién (1), qué información falta (1), consecuencia (1), qué falta averiguar (1), cada uno con fuente.', 'Cada parte por separado. 0 en la parte que propone comprar un proyector como problema.'],
    ['9', '4: enunciado sin solución (2); explicación de por qué A-4 no resuelve las reservas superpuestas ni el dato de uso (2).', '1 si el enunciado describe solo el síntoma.'],
]

# ---------------------------------------------------------------- capítulo 2
SEC_C2 = [
    ('Encuentro 3 — Preparar el relevamiento (5 HC)', [
        ['Problema y explicación', 'aprox. 1 HC', 'Sección 2.1 con la Tabla 2.1. Preparar y conducir una entrevista, Tabla 2.2 y Ejemplo resuelto 2.1. Lectura del registro E1.'],
        ['Práctica', 'aprox. 3 HC', 'Cada equipo prepara su guion y sus criterios de resguardo (Actividades 3 y 4). Sección 2.2: registro O1, documentos D1 y D2, Ejemplo resuelto 2.2. Actividades 1, 2 y 5.'],
        ['Revisión y cierre', 'aprox. 1 HC', 'Revisión cruzada de guiones con la Tabla 2.2. Entrega del guion y de los criterios para resguardar la información (evidencia del Encuentro 3). La Actividad 6 queda como tarea.'],
    ]),
    ('Encuentro 4 — Contrastar y registrar con cuidado (5 HC)', [
        ['Problema y explicación', 'aprox. 1 HC', 'Registros E2 a E5. Sección 2.3 con la Figura 2.2 y los Ejemplos resueltos 2.3 y 2.4.'],
        ['Práctica', 'aprox. 3 HC', 'Práctica 2: simulación con roles (aprox. 2 HC). Sección 2.4 con el Ejemplo resuelto 2.5 y la Tabla 2.6. Actividades 1 a 3.'],
        ['Revisión y cierre', 'aprox. 1 HC', 'Tabla 2.7 (necesidades). Entrega de notas, fuentes y registro de contradicciones (evidencia del Encuentro 4). Las Actividades 4 y 5 quedan como tarea.'],
    ]),
]
CLAVES_C2_E3 = [
    ['1', '(a) necesidad; (b) solución; (c) hecho; (d) necesidad; (e) solución; (f) hecho.', 'Clasificar (d) como solución.'],
    ['2', '(a) cerrada; (b) abierta; (c) inductora; (d) cerrada; (e) abierta.', 'Marcar (a) como abierta.'],
    ['3', 'Seis preguntas: primero abiertas («¿Qué hacés cuando necesitás un libro para una tarea?», «¿Qué te hace ir o no ir a la biblioteca?»), al final cerradas («¿Cuántas veces fuiste este año?»). Sin tecnologías ni preguntas inductoras.', 'Preguntar «¿te gustaría una app?».'],
    ['4', 'Autorización de la bibliotecaria y conocimiento de la dirección; no se anotan nombres ni cursos; solo conteos y tiempos; sin fotos de personas; notas en la carpeta del equipo, leídas solo por el equipo y el docente; se descartan al pasarlas en limpio o al terminar el proyecto.', 'Anotar nombres «para no olvidarse».'],
    ['5', '(a) cuestionario; (b) observación, completada con una entrevista; (c) análisis de documentos (reglamento); (d) taller grupal.', 'Entrevistar a todos los estudiantes para (a).'],
    ['6', '(a) «¿Cómo te gustaría enterarte de si un libro está disponible?»; (b) dos preguntas: «¿Qué libros se piden más?» y «¿En qué meses hay más pedidos?»; (c) «¿Quién debería poder registrar los préstamos?» o «¿Cómo se identifica hoy quien presta?».', 'Corregir solo una parte de (b).'],
]
CLAVES_C2_E4 = [
    ['1', '(a) hecho relatado por la docente, con una cifra estimada («cinco o seis») a verificar; (b) opinión ambigua: «rápido» hay que precisarlo; (c) supuesto: estimación de la bibliotecaria; (d) hecho observado; (e) opinión: deseo del lector, que expresa una necesidad; (f) hecho documental: lo que dice el reglamento; si se cumple, a verificar.', 'Tomar (c) como hecho.'],
    ['2', 'Título: «Lo que entendimos de nuestras charlas, para que usted lo confirme». N-01: saber en el momento quién tiene cada libro. N-02: que no se pueda anotar el mismo libro a dos chicos. N-04: poder anotar rápido en el recreo sin que después no se entienda. N-05: saber de qué préstamo es un libro que vuelve. N-06: tener el informe del mes sin contar a mano y sin errores. Preguntas: «¿Qué significa para usted que sea fácil?» y «¿En qué situaciones un préstamo queda sin curso?».', 'Usar palabras técnicas.'],
    ['3', 'D1-A4 pide anotar el curso; D2-8 muestra seis préstamos sin curso. Necesidad del reglamento y de la dirección: un informe por curso exacto (E5-L2). Necesidad de la práctica: anotar rápido en hora pico (E1-L2). Pregunta: «¿Por qué algunos préstamos quedan sin curso? ¿En qué situaciones pasa?» (E4-L12 responde en parte).', 'Culpar a la bibliotecaria.'],
    ['4', 'No hay un conflicto necesario: E5-L4 descarta gastos y servicios pagos; E3-L3 pide saber antes de ir, lo que puede resolverse sin un servicio pago (por ejemplo, una consulta en la computadora de la biblioteca o una lista publicada). Necesidades: la directora, no gastar; el lector, no perder el recreo. Al encargado de informática: si la computadora de la biblioteca puede mostrar el catálogo a otros equipos del colegio sin internet y si hay una red interna.', 'Concluir «hay que hacer una app» o «no se puede».'],
    ['5', '«¿Cómo le gustaría consultar si un libro está disponible?» o «¿Qué le ayudaría a saber quién tiene cada libro?». El analista perdió la respuesta propia de Mirta: obtuvo un «sí» de cortesía que no vale como dato (H9).', 'Reemplazar la app por otra tecnología en la pregunta.'],
]
CLAVES_P2 = [
    ['Nivel 1', 'Guion con tres abiertas y dos cerradas, sin inducir, con una pregunta sobre los docentes. Dato oculto: si se pregunta cómo presta a los docentes, el encargado cuenta que no les hace ficha y los anota en un cuaderno propio. Contradicción esperada: ese registro paralelo frente a M-N3. También vale el plazo: el encargado opina quince días, M-N1 fija siete.'],
    ['Nivel 2', 'Hallazgos de dos fuentes, con naturaleza (hecho, opinión, supuesto). Contradicciones: registro paralelo de docentes frente a M-N3; préstamo a nombre de una amiga (la lectora, si se le pregunta cómo consigue los libros) frente a M-N2; plazo de quince días (encargado) frente a siete (M-N1 y dirección). Necesidades posibles: saber quién tiene cada libro, también los de docentes; acceso del turno mañana; saber qué libros se leen más; proteger los datos de menores; que los libros vuelvan.'],
    ['Nivel 3', 'Lectora frente a dirección: la lectora quiere acceso a la mañana; la dirección no menciona el turno mañana y adelanta que el encargado tendrá menos horas (solo si se le pregunta por los recursos). Necesidad no expresada: los lectores del turno mañana no tienen acceso real (V-06, M-N4 y la tarjeta de la lectora); también vale el riesgo de menos horas. Opciones para el plazo o para el acceso, con ventajas y desventajas, sin elegir; decide la dirección. Anonimización: «Sofía» pasa a «Lectora 1»; se evalúa si «8.º, turno mañana» la identifica y se generaliza.'],
]
COTEJO_P2 = [
    ['El guion tiene objetivo, abiertas antes que cerradas y ninguna pregunta inductora, doble o técnica.', 'Indicador 1'],
    ['Usa al menos dos técnicas o dos fuentes (entrevistas y normas).', 'Indicador 2'],
    ['Cada línea del registro tiene código y los hallazgos separan hechos, opiniones y supuestos.', 'Indicador 3'],
    ['Registra al menos una contradicción con sus dos fuentes y la necesidad detrás de cada posición.', 'Indicador 4'],
    ['Los registros dicen qué autorizó cada persona y no tienen datos innecesarios.', 'Indicador 5'],
]
CRIT_C2 = [
    ['8', '4: T1-L1 hecho (1), T1-L3 hecho (1), T1-L4 opinión (1), identifica T1-L4 como propuesta (1).', 'Cada parte por separado; sin justificación, la mitad.'],
    ['9', '4: dos fuentes de la contradicción (2), necesidad no expresada (1), a quién se eleva (1).', 'Cada parte por separado.'],
]

# ---------------------------------------------------------------- capítulo 3
SEC_C3 = [
    ('Encuentro 5 — Objetivos, alternativas y riesgos (5 HC)', [
        ['Problema y explicación', 'aprox. 1 HC', 'Sección 3.1 con el Ejemplo resuelto 3.1 y la Tabla 3.1.'],
        ['Práctica', 'aprox. 3 HC', 'Sección 3.2 con las Tablas 3.2 y 3.3 y el Ejemplo resuelto 3.2. Sección 3.3 con la Tabla 3.4, la Figura 3.1, el Ejemplo resuelto 3.3 y las Tablas 3.5 y 3.6. Cada equipo arma su tabla de factibilidad y riesgos. Actividades 1 a 3.'],
        ['Revisión y cierre', 'aprox. 1 HC', 'Actividad 4 en plenario. Entrega de la tabla de factibilidad y riesgos (la «matriz de factibilidad y riesgos» de Work; evidencia del Encuentro 5). Práctica 3, Nivel 1, empieza en clase y se completa como tarea; la Actividad 5 también es tarea.'],
    ]),
    ('Encuentro 6 — Acuerdo de proyecto y revisión de la Unidad I (5 HC)', [
        ['Preparación', 'aprox. 1 HC', 'Sección 3.4 con el Ejemplo resuelto 3.4 y las Tablas 3.7 y 3.8. Los equipos terminan su acuerdo (Actividad 2) y aplican la lista de verificación del H1.'],
        ['Defensa del H1', 'aprox. 3 HC', 'Presentación de cada equipo (unos 10 minutos) y ronda de preguntas individuales, con la rúbrica. El tiempo depende de la cantidad de equipos: con más de seis, se reparte en dos bloques.'],
        ['Correcciones y cierre', 'aprox. 1 HC', 'Cada equipo registra en la bitácora las observaciones y planifica las correcciones (evidencia: H1 con correcciones). Actividades 3 y 4 como tarea.'],
    ]),
]
CLAVES_C3_E5 = [
    ['1', '(a) tarea; como objetivo: «Que los docentes sepan con anticipación si hay ejemplares suficientes para su curso». (b) objetivo. (c) solución; como objetivo: «Que los lectores consulten la disponibilidad sin ir al mostrador». (d) objetivo. (e) solución (y una decisión de recursos); como objetivo, por ejemplo: «Que la bibliotecaria registre los préstamos con el equipo disponible».', 'Aceptar (c) porque «es lo que vamos a hacer».'],
    ['2', '(a) contingencia; (b) mitigación; (c) contingencia; (d) mitigación.', 'Confundir (c) con mitigación.'],
    ['3', 'Ejemplo: «Con datos inventados, un ejemplar ya prestado se intenta prestar a otro lector: el sistema lo rechaza y la lista de préstamos activos sigue mostrando un solo préstamo de ese ejemplar.» Una persona ajena sigue los pasos y mira la lista.', 'Resultado sin algo observable.'],
    ['4', 'Probabilidad media: la bibliotecaria quiere el cambio, pero dice «yo no soy de computadoras» (E1-L10). Impacto alto: sin su uso el sistema no sirve, y la nota exige su conformidad (D0-5). Mitigación: revisiones con ella en cada unidad y práctica guiada. Contingencia: ajustar según sus observaciones y mantener el registro manual mientras tanto. Responsable: relación con los interesados.', 'Mitigación y contingencia iguales.'],
    ['5', 'No es correcto: es un supuesto sin fuente. Se marca «a verificar» y se pregunta al encargado de informática o se revisa la documentación de la herramienta. Valorar sin evidencia sesga la comparación.', 'Aceptar la valoración «porque es probable».'],
    ['6', 'La alternativa C pierde factibilidad técnica y operativa; conseguir otro equipo choca con E5-L4. B también queda comprometida. La recomendación honesta pasa a A (registro manual mejorado), con un alcance reducido: N-05 y N-09 completas, N-01 y N-06 en parte; N-02 y N-03 quedan sin resolver y se declara. El curso puede seguir construyendo el prototipo con datos inventados como ejercicio, pero la biblioteca no lo usaría.', 'Mantener C sin cambios.'],
]
CLAVES_C3_E6 = [
    ['1', '(a) registro; (b) relación con los interesados; (c) versiones y recursos; (d) coordinación.', '—'],
    ['2', 'Acuerdo con las diez secciones de la Tabla 3.7, versión y fecha, fuentes, supuestos marcados, exclusiones con razón y firmas. En la revisión cruzada, cada punto incumplido lleva una corrección concreta.', 'Copiar el acuerdo del equipo modelo.'],
    ['3', 'Se registra como solicitud de cambio: se analiza el impacto (nuevos actores y reglas, tiempo, riesgo R-04), se consulta y decide la dirección. Si se acepta, se actualiza el acuerdo (v1.1) y el alcance; si no, queda como extensión. No alcanza con «sí» (riesgo de no terminar) ni con «no» (la dirección tiene autoridad).', 'Agregarlo sin registrar.'],
    ['4', 'Ejemplos: «¿Por qué el registro manual queda como contingencia?» (respuesta: R-01 y R-02); «¿Por qué los permisos están en el núcleo?» (respuesta: E4-L8 y E5-L6); «¿Por qué se excluyen las reservas en línea?» (respuesta: E4-L10).', 'Preguntas que se responden con sí o no.'],
]
CLAVES_P3 = [
    ['Nivel 1', 'A (registro manual mejorado): operativa media o alta (el encargado ya usa fichas; voluntarios de 9.º los miércoles, M-F5); técnica alta (no necesita equipos, M-F1 y M-F2); económica alta (materiales de oficina, M-F3); calendario alta. C (prototipo propio): operativa baja (la biblioteca no tiene computadora, M-F1; el encargado tendrá menos horas, M-F4); técnica baja (M-F1, M-F2); económica baja: la cooperadora no paga una computadora (M-F3); calendario media. Objetivo para MN-01: «Que el encargado sepa qué lector tiene cada libro prestado, también los de docentes». Resultado: una planilla única de préstamos activos cuyo recuento coincide con los libros que faltan en el estante. Recomendación: A, resignando la consulta anticipada y el informe automático.'],
    ['Nivel 2', 'B (planilla en la notebook de la secretaría): la notebook se usa a la mañana (M-F1) y la biblioteca abre a la tarde; su uso a la tarde y su traslado quedan «a verificar»; sin internet (M-F2). Riesgos posibles: pérdida de fichas o planillas (mitigación: armario con llave, M-F3); menos horas del encargado (M-F4; mitigación: voluntarios, M-F5); préstamos a nombre de otro; datos de menores a la vista. Exclusiones: sistema informático propio, reservas, apertura a la mañana (requiere horas; decide la dirección). Recomendación dirigida a la directora, con lo que se resigna.'],
    ['Nivel 3', 'Datos que cambian la recomendación respecto de Arapoty: M-F1 (no hay computadora) y M-F4 (menos horas). Solución no informática para MN-02: abrir un recreo de la mañana con los voluntarios de 9.º (M-F5) bajo supervisión, o un buzón de pedidos a la mañana con entrega a la tarde; se analiza su factibilidad. Para que C fuera la mejor opción: una computadora disponible en la biblioteca, alguien que la mantenga y horas suficientes del encargado.'],
]
COTEJO_P3 = [
    ['Cada valoración de factibilidad tiene una razón y una fuente M-F, o dice «a verificar».', 'Indicadores 2 y 4'],
    ['No hay números ni sumas de puntajes en la comparación.', 'Indicador 2'],
    ['Los objetivos citan necesidades MN y tienen un resultado comprobable.', 'Indicador 1'],
    ['Los riesgos tienen probabilidad, impacto, mitigación y contingencia (Nivel 2 o 3).', 'Indicador 3'],
    ['La recomendación dice qué se resigna y quién decide.', 'Indicador 4'],
]
CRIT_C3 = [
    ['8', '4: una valoración con razón y fuente por cada celda pedida (cuatro celdas).', 'Sin fuente, medio punto. 0 si se suman puntajes.'],
    ['9', '4: riesgo con probabilidad e impacto (1), mitigación (1), contingencia (1), exclusión con razón (1).', 'Cada parte por separado.'],
]

# ---------------------------------------------------------------- otros contenidos
CALENDARIO_28 = (['Encuentro (36)', 'Encuentro (28)', 'Qué se hace'],
                 [['1', '1', 'Sin cambios: reto, diagnóstico de entrada, secciones 1.1 y 1.2.'],
                  ['2', '2', 'Sin cambios: secciones 1.3 y 1.4, Práctica 1.'],
                  ['3', '3', 'Sin cambios: preparar el relevamiento.'],
                  ['4', '4', 'Sin cambios: contrastar y registrar, Práctica 2.'],
                  ['5 y 6', '5', 'Se unen: factibilidad con dos alternativas (A y C), riesgos R-01 a R-04, alcance y exclusiones, H1 como defensa breve por equipo. El acuerdo de proyecto y la Práctica 3 pasan a tarea.']])

COORDINACION = [
    'El mapa de apoyos del Encuentro 1 se comparte con los docentes de Algorítmica y de Laboratorio de 3.º. Según '
    'el informe de Work, conviene acordar con Algorítmica antes del Encuentro 13 (modelo de datos) y con Laboratorio '
    'antes del Encuentro 19 (construcción del prototipo) qué se refuerza y quién lo hace.',
    'Los contenidos de 1.º y 2.º se diagnostican; los de 3.º son concurrentes y no se exigen como aprendidos al '
    'empezar el año. La comparación de alternativas del Capítulo 3 no reemplaza ni repite la matriz de decisión de '
    'Algorítmica 3.º (Práctica 4): allí se elige una tecnología; acá, un tipo de solución.',
]

MAPA_APOYOS = (['Estudiante (código)', 'Programación', 'Formularios', 'Datos', 'Comunicación', 'Apoyo previsto', 'Coordinar con'],
               [['E-01', '', '', '', '', '', ''], ['E-02', '', '', '', '', '', ''], ['E-03', '', '', '', '', '', '']])

RUBRICA_EXPLICACION = [
    'Para cada criterio se registran dos niveles: el del producto del equipo y el individual de cada integrante. El '
    'nivel del criterio combina los dos en la proporción 60 % (producto del equipo) y 40 % (evidencia individual). Por '
    'ejemplo, si se asignan 4, 3, 2 y 1 puntos a los niveles Sólido, Logrado, En desarrollo e Inicial, un producto '
    'Logrado (3) con una evidencia individual En desarrollo (2) da 3 × 0,6 + 2 × 0,4 = 2,6 para ese estudiante en ese '
    'criterio. La conversión a calificación la decide la institución.',
    'La evidencia individual es la explicación en la ronda de preguntas, la resolución de un cambio acotado que '
    'proponga el docente, el aporte registrado en la bitácora y la observación del docente. La coevaluación orienta '
    'la devolución, pero no reemplaza la valoración docente.',
    'La ausencia de evidencia se registra aparte («AE»), con la fecha acordada para entregarla; no se confunde con un '
    'desempeño de nivel Inicial. La proporción 60/40 y los niveles son una propuesta editorial tomada del informe de '
    'Work (§4.3); no son una escala oficial del MEC.',
]

PROCEDENCIA = (['Recurso', 'Procedencia', 'Derechos'],
               [['Texto de los preliminares y de los Capítulos 1 a 3', 'Redacción original para este libro. El Capítulo 2 integra textos del candidato del Capítulo 2 (Fase 2), según su plan de integración.', 'Propios del proyecto.'],
                ['Figuras 1.1, 2.2 y 3.1', 'Generadas con build/diagramas.py (matplotlib).', 'Propias; sin recursos de terceros.'],
                ['Figuras 1.2 y 2.1', 'Adaptadas de las figuras del candidato del Capítulo 2, generadas por código.', 'Propias.'],
                ['Caso Arapoty: institución, personas, registros y necesidades', 'Inventados. E1, E2, E3 y O1 vienen del candidato del Capítulo 2; las líneas de E4 y E5 que cita el Capítulo 4 se copiaron sin cambios; D0, D1, D2 y las necesidades son nuevos. Fuente única: caso/dossier.py.', 'Propios del proyecto.'],
                ['Caso de práctica Mbokaja', 'Inventado para este lote (caso/mbokaja.py).', 'Propio.'],
                ['Capacidades, niveles de desempeño, proporción 60/40, alcance mínimo y reglas a negociar', 'Informe de Work v0.1 (§4.2, §4.3 y §7.2), como propuesta editorial.', 'Insumo interno del proyecto.'],
                ['Constitución Nacional, art. 140', 'Referencia legal pública, citada en el recuadro «En Paraguay».', 'No aplica.'],
                ['Relación con Algorítmica 3.º', 'No se reutilizaron ejercicios, personas, títulos ni la matriz de decisión de ese libro.', 'No aplica.']])


def _sec(doc, secuencia):
    for titulo, filas in secuencia:
        M.tabla(doc, (['Momento', 'Tiempo', 'Qué se hace'], filas), ANCHO_SEC, rotulo=titulo)


def _claves(doc, rotulo, filas):
    M.tabla(doc, (['Act.', 'Respuesta esperada', 'Error frecuente'], filas), [1.2, 11.0, 4.4], rotulo=rotulo)


def _eval(doc, C, claves, crit):
    filas = [[str(n), clave, detalle] for eid, n, clave, detalle in claves if eid == C.EVAL_ID]
    M.tabla(doc, (['Ítem', 'Clave', 'Respuesta o criterio'], filas), [1.2, 1.8, 13.6], rotulo='Clave de la %s' % C.EVAL_TITULO.lower())
    M.tabla(doc, (['Ítem', 'Puntaje completo', 'Puntaje parcial'], crit), [1.2, 8.4, 7.0], rotulo='Criterios de corrección de los ítems abiertos')


def construir(ruta, claves, paginas, estado):
    doc = H.new_doc()
    K.portada(doc, 'Guía docente', estado)

    doc.add_heading('Guía docente — Lote 1', level=1)
    H.caja(doc, 'Sobre las capacidades', [
        'Las capacidades de las fichas (C1, C2 y C7 en este lote) son propuestas para el programa institucional del '
        'Plan Optativo, tomadas del informe de Work. No son capacidades oficiales del MEC. Según el informe de Work, '
        'el diseño curricular consultado (mayo de 2026, p. 29) permite que la institución elabore el programa del Plan '
        'Optativo; esa lectura no se verificó por separado en este lote.'], tipo='neutra')
    H.p_texto(doc, 'Cada encuentro sigue la estructura de taller de Work: 1 HC de problema y explicación, 3 HC de práctica '
                   'y 1 HC de revisión, redistribuida en los encuentros de diagnóstico, relevamiento y defensa. Los tiempos '
                   'son aproximados y la duración de la hora cátedra la fija cada institución. Las páginas indicadas son '
                   'las del libro del estudiante.', italic=True, size=9.5)

    # 1. preliminares
    doc.add_heading('1. Preliminares: diagnóstico de entrada y mapa de apoyos', level=2)
    H.p_texto(doc, 'El diagnóstico (libro, pág. %s) no lleva nota. Se corrige por área: %s Cada área se marca «firme» '
                   '(todos los ítems correctos), «a reforzar» (alguno) o «a enseñar» (ninguno), y se compara con la '
                   'autoevaluación del estudiante: las diferencias grandes se conversan.'
              % (paginas.get(P.TITULOS[4], '—'), DIAG_AREAS))
    M.tabla(doc, (['Ítem', 'Respuesta esperada', 'Error frecuente'], DIAG_CLAVES), [1.2, 11.0, 4.4], rotulo='Claves del diagnóstico de entrada')
    H.p_texto(doc, 'Con los resultados, el docente arma el mapa de apoyos del curso (evidencia del Encuentro 1): una fila '
                   'por estudiante, identificado por un código, el estado de cada área, el apoyo previsto y con qué '
                   'asignatura se coordina.')
    M.tabla(doc, MAPA_APOYOS, [2.8, 2.0, 2.0, 1.6, 2.2, 3.4, 2.6], rotulo='Mapa de apoyos del curso (modelo)')
    doc.add_heading('Coordinación con otras asignaturas', level=3)
    for t in COORDINACION:
        H.p_texto(doc, t)

    # 2. capítulo 1
    K.titulo_en_pagina_nueva(doc, '2. Capítulo 1 — %s' % cap1.TITULO, nivel=2)
    M.ficha(doc, cap1)
    _sec(doc, SEC_C1)
    _claves(doc, 'Claves de las actividades del Encuentro 1', CLAVES_C1_E1)
    _claves(doc, 'Claves de las actividades del Encuentro 2', CLAVES_C1_E2)
    M.tabla(doc, (['Nivel', 'Respuesta esperada'], CLAVES_P1), [2.2, 14.4], rotulo='Práctica 1: claves por nivel')
    M.tabla(doc, (['Criterio', 'Indicador'], COTEJO_P1), [13.0, 3.6], rotulo='Lista de cotejo de la Práctica 1')
    _eval(doc, cap1, claves, CRIT_C1)

    # 3. capítulo 2
    K.titulo_en_pagina_nueva(doc, '3. Capítulo 2 — %s' % cap2.TITULO, nivel=2)
    M.ficha(doc, cap2)
    _sec(doc, SEC_C2)
    _claves(doc, 'Claves de las actividades del Encuentro 3', CLAVES_C2_E3)
    _claves(doc, 'Claves de las actividades del Encuentro 4', CLAVES_C2_E4)
    doc.add_heading('Práctica 2: tarjetas de rol (para fotocopiar y recortar)', level=3)
    H.p_texto(doc, 'Cada tarjeta la recibe solo quien hace ese papel. Los analistas no las leen. Si un analista hace una '
                   'pregunta inductora, quien hace el papel responde con cortesía pero sin agregar información.', size=10)
    for titulo, lineas in MB.TARJETAS:
        H.caja(doc, titulo, lineas, tipo='referencia')
    M.tabla(doc, (['Nivel', 'Respuesta esperada'], CLAVES_P2), [2.2, 14.4], rotulo='Práctica 2: claves por nivel')
    M.tabla(doc, (['Criterio', 'Indicador'], COTEJO_P2), [13.0, 3.6], rotulo='Lista de cotejo de la Práctica 2')
    _eval(doc, cap2, claves, CRIT_C2)
    doc.add_heading('Integración del candidato del Capítulo 2', level=3)
    H.p_texto(doc, 'El capítulo se construyó con el plan de integración aprobado en la Fase 2. Destino de cada elemento del '
                   'candidato:', size=10)
    M.tabla(doc, (['Elemento del candidato', 'Destino', 'Acción'], [list(x) for x in cap2.INTEGRACION]), [5.0, 8.4, 3.2],
            rotulo='Destino de los 31 elementos del candidato', size=8.5)

    # 4. capítulo 3
    K.titulo_en_pagina_nueva(doc, '4. Capítulo 3 — %s' % cap3.TITULO, nivel=2)
    M.ficha(doc, cap3)
    _sec(doc, SEC_C3)
    _claves(doc, 'Claves de las actividades del Encuentro 5', CLAVES_C3_E5)
    _claves(doc, 'Claves de las actividades del Encuentro 6', CLAVES_C3_E6)
    M.tabla(doc, (['Nivel', 'Respuesta esperada'], CLAVES_P3), [2.2, 14.4], rotulo='Práctica 3: claves por nivel')
    M.tabla(doc, (['Criterio', 'Indicador'], COTEJO_P3), [12.4, 4.2], rotulo='Lista de cotejo de la Práctica 3')
    _eval(doc, cap3, claves, CRIT_C3)

    # 5. rúbrica H1
    K.titulo_en_pagina_nueva(doc, '5. Rúbrica del hito H1: problema y alcance defendidos', nivel=2)
    for t in RUBRICA_EXPLICACION:
        H.p_texto(doc, t)
    filas = []
    for crit, cap, niveles, eq, ind in cap3.RUBRICA_H1:
        filas.append(['%s (%s)' % (crit, cap)] + niveles)
    M.tabla(doc, (['Criterio', '4. Sólido', '3. Logrado', '2. En desarrollo', '1. Inicial'], filas),
            [2.8, 3.6, 3.4, 3.4, 3.4], rotulo='Rúbrica del H1: descriptores por nivel', size=8.5)
    M.tabla(doc, (['Criterio', 'Evidencia del equipo (60 %)', 'Evidencia individual (40 %)'],
                  [[r[0], r[3], r[4]] for r in cap3.RUBRICA_H1]), [4.4, 5.8, 6.4],
            rotulo='Evidencias de cada criterio')
    M.tabla(doc, (['Nivel de desempeño', 'Descriptor común (Work §4.3)'], [list(x) for x in cap3.NIVELES_DESEMPENO]),
            [3.6, 13.0], rotulo='Niveles de desempeño (propuesta editorial)')
    M.tabla(doc, (['Estudiante (código)', 'Criterio', 'Nivel del equipo', 'Nivel individual', 'Resultado', 'AE'],
                  [['', 'Problema delimitado', '', '', '', ''], ['', 'Evidencia del relevamiento', '', '', '', ''],
                   ['', 'Objetivos y alternativas', '', '', '', ''], ['', 'Alcance, exclusiones y riesgos', '', '', '', ''],
                   ['', 'Organización y registro', '', '', '', '']]),
            [3.0, 5.0, 2.2, 2.2, 2.2, 2.0], rotulo='Planilla de registro del H1 (una por estudiante)')

    # 6. calendario y 7. procedencia
    doc.add_heading('6. Calendario con menos encuentros', level=2)
    H.p_texto(doc, 'En la adaptación de 28 encuentros (informe de distribución del esfuerzo, Fase 2), la Unidad I pasa de '
                   'seis a cinco encuentros. Cada capítulo del libro del estudiante tiene su recuadro «Si el calendario se '
                   'acorta».')
    M.tabla(doc, CALENDARIO_28, [2.6, 2.6, 11.4], rotulo='Unidad I en 36 y en 28 encuentros')
    doc.add_heading('7. Procedencia y derechos de los recursos', level=2)
    M.tabla(doc, PROCEDENCIA, [4.4, 7.8, 4.4], rotulo='Inventario de recursos del lote')
    M.pegar_renglones(doc)
    K.saltos_a_titulos(doc)
    H.finalizar(doc, ruta)

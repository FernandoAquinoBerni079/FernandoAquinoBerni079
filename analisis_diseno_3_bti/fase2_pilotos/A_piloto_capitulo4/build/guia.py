# -*- coding: utf-8 -*-
"""Guía docente del Capítulo 4 (piloto): secuencia de los encuentros, claves,
lista de cotejo, adaptación a calendario reducido y procedencia de recursos."""
import helpers as H
import contenido as C

SECUENCIA = [
    ('Encuentro 7 — A quién escuchar y cómo preguntar (5 HC)', [
        ['Inicio', 'aprox. 0,5 HC', 'Pregunta disparadora: «Si tuvieran que mejorar la biblioteca, ¿qué le preguntarían a la '
         'bibliotecaria?». Se anotan las preguntas en la pizarra sin corregirlas: se retoman en el cierre.'],
        ['Desarrollo', 'aprox. 3,5 HC', '4.1 con la Tabla 4.1 y el Concepto clave. 4.2 con la Figura 4.1 y el Ejemplo resuelto '
         '4.1. Actividades 1 y 2 (Ejercitá), individuales. 4.3 con la Tabla 4.3 y la caja En Paraguay. 4.4 con la '
         'Tabla 4.4, el Ejemplo resuelto 4.2 y la Figura 4.2. Actividades 3 y 4 (Resolvé), en parejas.'],
        ['Cierre', 'aprox. 1 HC', 'Actividad 5 (Pensá y decidí) en plenario. Se vuelve a las preguntas del inicio y el '
         'grupo las clasifica en abiertas, cerradas o inductoras. La Actividad 6 (Desafío) queda como tarea.'],
    ]),
    ('Encuentro 8 — Del registro al requisito candidato (5 HC)', [
        ['Inicio', 'aprox. 0,5 HC', 'Corrección de la Actividad 6 del encuentro anterior.'],
        ['Desarrollo', 'aprox. 3 HC', '4.5 con el registro E1 y el Ejemplo resuelto 4.3. 4.6 con el Ejemplo resuelto 4.4. '
         'Actividad 1 del Encuentro 8 (Ejercitá). 4.7 con el Ejemplo resuelto 4.5. Práctica 4 por niveles, '
         'aprox. 1,5 HC.'],
        ['Cierre', 'aprox. 1,5 HC', 'Evaluación del capítulo (aprox. 1 HC). Lectura de 4.8 y del recuadro Para repasar. '
         'Las Actividades 2 a 5 del Encuentro 8 quedan como tarea o para el inicio del Capítulo 5. Si el tiempo '
         'no alcanza, la evaluación se toma al comienzo del encuentro 9.'],
    ]),
]

CLAVES_ACT_E7 = [
    ['1', '(a) necesidad; (b) solución; (c) requisito candidato; (d) necesidad; (e) solución; (f) requisito candidato.',
     'Tomar (b) como requisito porque «lo pidió el usuario».'],
    ['2', '(a) cerrada; (b) abierta; (c) inductora; (d) cerrada; (e) abierta.',
     'Clasificar (c) como cerrada: es cerrada, pero sobre todo inductora.'],
    ['3', 'Respuesta abierta. Ejemplos válidos: supervisión educativa (interés 2, influencia 7: mantener satisfecha); '
     'secretaría que carga las listas de cada curso (interés 5, influencia 3: mantener informada); delegados de '
     'curso (interés 8, influencia 4: mantener informados). Se exige una razón por puntaje.',
     'Puntajes sin razón; repetir un interesado de la figura.'],
    ['4', 'Respuesta abierta. Ejemplo: ¿Cuándo fue la última vez que fuiste a la biblioteca y para qué? ¿Qué hace que '
     'vayas poco? ¿Cómo te enterás de qué libros hay? ¿Qué te gustaría encontrar ahí? ¿En qué recreo podrías ir? '
     '¿Cuántas veces por mes irías si encontraras lo que buscás?',
     'Empezar con cerradas; nombrar «una app» o «una página».'],
    ['5', '(a) cuestionario: llega a muchos; (b) observación directa, completada con entrevista: muestra lo que pasa; '
     '(c) análisis de documentos: el reglamento; (d) taller grupal: reúne a las partes para acordar.',
     'Elegir entrevista para (a): no llega a toda la institución.'],
    ['6', '(a) «¿Qué pasa cuando querés un libro y no sabés si está?»; (b) dos preguntas: «¿Qué libros se piden más?» '
     'y «¿En qué meses hay más pedidos?»; (c) «¿Quiénes deberían poder ver o cambiar los datos de los préstamos?».',
     'Mantener la tecnología en la pregunta reformulada.'],
]

CLAVES_ACT_E8 = [
    ['1', 'Palabras ambiguas: (a) «rápido»; (b) «todos»; (c) «adecuados»; (d) «amigable». Versiones comprobables, por '
     'ejemplo: (a) mostrar el resultado de una búsqueda en menos de 3 segundos; (b) nombrar quiénes: la '
     'bibliotecaria y los docentes autorizados; (c) listar las columnas: curso, mes y cantidad de préstamos; (d) un '
     'estudiante de 1.º encuentra un libro por título sin ayuda en su primer intento. Toda cifra se marca «a '
     'confirmar con el interesado».',
     'Reemplazar una palabra ambigua por otra («muy rápido», «intuitivo»).'],
    ['2', 'RC-07 El sistema debe registrar la fecha de devolución de cada préstamo. Origen: H3, H4 y H5 (E1-L4, E1-L6). '
     'Funcional.',
     'Redactarlo como acción de la bibliotecaria («anotar en el cuaderno…») y no del sistema.'],
    ['3', 'Respuesta abierta. Debe incluir título, los seis requisitos en lenguaje de la bibliotecaria (sin «RC», sin '
     'jerga) y dos preguntas, por ejemplo: ¿qué significa para usted que sea fácil?, ¿cuántos libros faltan '
     'realmente según el inventario?',
     'Copiar la tabla con códigos y términos técnicos.'],
    ['4', 'No hay un conflicto directo: la directora pone una restricción de presupuesto y los estudiantes expresan '
     'una necesidad (saber si un libro está antes de ir). Puede atenderse sin comprar computadoras. Al encargado de '
     'informática se le pregunta, por ejemplo: ¿la biblioteca tiene conexión a la red del colegio?, ¿se puede '
     'publicar una página interna?, ¿qué computadora hay disponible y en qué estado?',
     'Declarar ganador a uno de los dos; proponer una compra.'],
    ['5', 'L11 reformulada: «¿Cómo le gustaría enterarse de si un libro está disponible?». Lo que se perdió: la '
     'preferencia real de Mirta. Respondió por cortesía («Si usted dice…»), así que el dato está contaminado y '
     'podría llevar a construir algo que ella no va a usar.',
     'Decir solo «estaba mal preguntado» sin explicar qué dato se perdió.'],
]

CLAVES_PRACTICA = [
    ['Nivel 1', 'Clasificación: (a) hecho, E2-L2; (b) problema, E2-L4; (c) necesidad, E2-L2; (d) problema, E2-L6; '
     '(e) necesidad (condición de plazo), E2-L8; (f) propuesta, E2-L8: la necesidad detrás es asegurar los '
     'ejemplares durante la lectura; (g) problema, E2-L10; (h) necesidad no funcional ambigua, E2-L11. '
     'Completamiento: RC-21 «treinta» u otra expresión equivalente, origen E2-L2; RC-22 «disponibles», origen E2-L4 '
     '(también O1, línea 4); RC-23 «devolución», origen E2-L10.'],
    ['Nivel 2', 'Tabla con al menos dos hallazgos de O1: 9 préstamos en un recreo (hecho); 5 de 14 estudiantes se fueron '
     'sin libro (problema); 2 libros que «tenían que estar» y no estaban (problema, coincide con H5 de E1). '
     'Requisitos posibles: registrar un préstamo en menos de un minuto (no funcional, origen O1, a confirmar); '
     'reconocer si un ejemplar devuelto pertenece a la biblioteca (funcional, E2-L10); reservar un lote de '
     'ejemplares para un curso con fecha de inicio y de fin (funcional, E2-L2, E2-L8). Expresiones ambiguas: '
     '«rápido» (E2-L11) y «a veces faltan cinco o seis» (E2-L4); también se acepta «como mínimo» (E2-L8), que no '
     'fija un máximo.'],
    ['Nivel 3', 'Conflicto: bloquear todos los ejemplares de un título durante tres semanas deja sin acceso a los demás '
     'lectores y afecta la circulación que cuida la bibliotecaria; además, puede no haber treinta ejemplares. '
     'Necesidades: la docente quiere que todo el curso lea a la vez; los demás lectores, acceder al título; la '
     'bibliotecaria, que los libros circulen y vuelvan. Opciones posibles: (a) reserva del lote con un cupo que '
     'deje ejemplares libres: ventaja, otros siguen leyendo; desventaja, puede no alcanzar para el curso. (b) '
     'Lectura escalonada por grupos: ventaja, necesita menos ejemplares; desventaja, el curso no lee al mismo '
     'tiempo. (c) Calendario del plan lector coordinado entre docentes: ventaja, evita superposiciones; '
     'desventaja, exige acuerdo institucional. Decide la dirección, o la coordinación pedagógica con la '
     'bibliotecaria. Cuestionario: cuatro cerradas, dos abiertas, sin inductoras.'],
]

LISTA_COTEJO = [
    ['Cada hallazgo tiene una fuente que se puede encontrar en los registros (E2-L…, O1).', 'Indicador 3'],
    ['Distingue hechos, problemas, necesidades y propuestas sin confundir propuestas con requisitos.', 'Indicador 3'],
    ['Redacta los requisitos con la forma «El sistema debe…», con código, origen y tipo.', 'Indicador 3'],
    ['Ningún requisito nombra una tecnología.', 'Indicador 3'],
    ['Reemplaza las expresiones ambiguas por condiciones comprobables (Nivel 2 y 3).', 'Indicador 4'],
    ['Describe el conflicto con las necesidades de cada parte y no elige por su cuenta (Nivel 3).', 'Indicador 4'],
    ['Las preguntas del cuestionario no son inductoras ni dobles (Nivel 3).', 'Indicador 2'],
]

DIFERENCIACION = [
    'Los tres niveles trabajan sobre los mismos registros, así que la puesta en común es una sola. El Nivel 1 '
    'asegura los indicadores 3 y 4 en su forma básica; es el piso que todo el curso debe alcanzar. El Nivel 2 es '
    'el esperado para la mayoría. El Nivel 3 es una ampliación: no se exige para aprobar y no suma puntaje '
    'extra en la evaluación del capítulo.',
    'Criterio sugerido para asignar niveles: quien en las Actividades 1 y 2 del Encuentro 8 confundió '
    'propuestas con requisitos empieza en el Nivel 1; quien las resolvió bien, en el Nivel 2; el Nivel 3 se '
    'ofrece a quien termina el Nivel 2 antes de tiempo.',
]

CALENDARIO = [
    'Si el calendario obliga a dar el capítulo en un solo encuentro de 5 HC, se mantiene la actividad central '
    '(Ejemplo resuelto 4.3 y Práctica 4, Niveles 1 o 2) y se pasa a lectura domiciliaria lo indicado en el '
    'recuadro final del libro del estudiante. La evaluación se reduce a los ítems 1, 2, 4, 5, 6 y 9 (10 puntos), '
    'que cubren los indicadores 1 a 3; el indicador 4 se evalúa con la Práctica 4.',
]

PROCEDENCIA = (['Recurso', 'Procedencia', 'Derechos'],
               [['Texto de todo el capítulo', 'Redacción original para este libro.', 'Propios del proyecto.'],
                ['Figura 4.1 (mapa de interesados)', 'Generada con build/diagramas.py (matplotlib).', 'Propia; sin recursos de terceros.'],
                ['Figura 4.2 (proceso de elicitación)', 'Generada con build/diagramas.py (matplotlib).', 'Propia; sin recursos de terceros.'],
                ['Caso, personas y diálogos', 'Inventados; el colegio y los nombres son ficticios.', 'Propios del proyecto.'],
                ['Constitución Nacional, art. 140', 'Paráfrasis de un texto normativo público.', 'Texto oficial de libre uso.'],
                ['Técnicas de elicitación y mapa de interés e influencia', 'Conocimiento general de la disciplina, con redacción propia.', 'No se copió material de terceros.'],
                ['Relación con Algorítmica 3.º', 'No se reutilizaron ejercicios ni datos de ese libro.', 'No aplica.']])


def construir(ruta, claves, portada, tabla, ficha):
    doc = H.new_doc()
    portada(doc, 'Guía docente — capítulo de muestra')

    doc.add_heading('Guía docente · %s' % C.CAPITULO, level=1)
    H.p_texto(doc, C.TITULO, bold=True, size=13, color=H.ID['MED'])
    ficha(doc)
    H.caja(doc, 'Sobre la capacidad', [
        'La capacidad de la ficha es una propuesta editorial para uso institucional. No se cita como capacidad '
        'oficial del MEC porque no se verificó un programa oficial de la asignatura. Si la institución tiene un '
        'programa propio aprobado, se reemplaza por la capacidad textual de ese programa.'], tipo='neutra')

    doc.add_heading('1. Secuencia de los encuentros', level=2)
    H.p_texto(doc, 'Los tiempos están expresados en horas cátedra (HC) y son aproximados. La duración de la hora '
                   'cátedra la fija cada institución.', italic=True, size=9.5)
    for titulo, filas in SECUENCIA:
        tabla(doc, (['Momento', 'Tiempo', 'Qué se hace'], filas), [2.4, 2.4, 11.8], rotulo=titulo)

    doc.add_heading('2. Claves de las actividades', level=2)
    tabla(doc, (['Act.', 'Respuesta esperada', 'Error frecuente'], CLAVES_ACT_E7), [1.2, 10.6, 4.8],
          rotulo='Encuentro 7')
    tabla(doc, (['Act.', 'Respuesta esperada', 'Error frecuente'], CLAVES_ACT_E8), [1.2, 10.6, 4.8],
          rotulo='Encuentro 8')

    doc.add_heading('3. Práctica 4: claves y diferenciación', level=2)
    for t in DIFERENCIACION:
        H.p_texto(doc, t)
    tabla(doc, (['Nivel', 'Respuesta esperada'], CLAVES_PRACTICA), [2.2, 14.4], rotulo='Claves por nivel')
    tabla(doc, (['Criterio de la lista de cotejo', 'Indicador'], LISTA_COTEJO), [13.6, 3.0],
          rotulo='Lista de cotejo de la Práctica 4')

    doc.add_heading('4. Evaluación del capítulo: clave y criterios', level=2)
    H.p_texto(doc, 'Puntaje total: 15 puntos. Ítems 1 a 7: 1 punto cada uno. Ítem 8: 3 puntos. Ítem 9: 5 puntos. '
                   'Las letras de las opciones múltiples salen del mismo barajado que el libro del estudiante.')
    filas = []
    for eval_id, n, clave, detalle in claves:
        filas.append([str(n), clave, detalle])
    tabla(doc, (['Ítem', 'Clave', 'Respuesta o criterio'], filas), [1.2, 1.8, 13.6], rotulo='Clave de la evaluación')
    tabla(doc, (['Ítem', 'Puntaje completo', 'Puntaje parcial'], [
        ['8', '3: condición medible (tiempo, cantidad o tarea) y situación concreta.', '1 o 2: hay cifra pero no situación, o al revés. 0: cambia «rápido» por otra palabra vaga.'],
        ['9', '5: problema con fuente (1), necesidad con fuente (1), requisito con la forma correcta (1), código y origen (1), tipo (1).', 'Se suma cada parte por separado. 0 en el requisito si nombra una tecnología.'],
    ]), [1.2, 8.0, 7.4], rotulo='Criterios de corrección de los ítems abiertos')

    doc.add_heading('5. Calendario con menos encuentros', level=2)
    for t in CALENDARIO:
        H.p_texto(doc, t)

    doc.add_heading('6. Procedencia y derechos de los recursos', level=2)
    tabla(doc, PROCEDENCIA, [5.0, 6.8, 4.8], rotulo='Inventario de recursos del capítulo')

    H.finalizar(doc, ruta)

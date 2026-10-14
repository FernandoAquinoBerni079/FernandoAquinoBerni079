# -*- coding: utf-8 -*-
"""Guía docente del Capítulo 4 v2: secuencia, claves, lista de cotejo, evaluación y procedencia."""
import helpers as H
import maqueta as M
import contenido as C

SECUENCIA = [
    ('Encuentro 7 — Requisitos funcionales y reglas de préstamo (5 HC)', [
        ['Problema y explicación', 'aprox. 1 HC', 'Retomar el dossier del Capítulo 2 (extracto en el libro). Sección 4.1 con la Tabla 4.1 y el Ejemplo resuelto 4.1. Actividad 1, individual.'],
        ['Práctica', 'aprox. 3 HC', 'Sección 4.2 con la Figura 4.1 y la Tabla 4.2. Ejemplo resuelto 4.2: el docente construye en la pizarra los tres primeros requisitos y los equipos completan el resto comparando con la Tabla 4.3. Actividades 2 y 3, en parejas.'],
        ['Revisión y cierre', 'aprox. 1 HC', 'Actividad 4 en plenario. Evidencia del encuentro (Work, encuentro 7): catálogo con identificadores y fuente. La Actividad 5 queda como tarea.'],
    ]),
    ('Encuentro 8 — Calidad, restricciones y criterios de aceptación (5 HC)', [
        ['Problema y explicación', 'aprox. 1 HC', 'Corrección de la Actividad 5. Sección 4.3 con la Figura 4.2, el Ejemplo resuelto 4.3 y la Tabla 4.5.'],
        ['Práctica', 'aprox. 3 HC', 'Sección 4.4 con la Tabla 4.6 y el Ejemplo resuelto 4.4. Actividades 1 y 2 del Encuentro 8. Práctica 4 por niveles (aprox. 1,5 HC).'],
        ['Revisión y cierre', 'aprox. 1 HC', 'Revisión entre pares con la lista del libro (Actividad 3). Evidencia del encuentro (Work, encuentro 8): requisitos comprobables y revisión entre pares. Las Actividades 4 y 5 quedan como tarea.'],
    ]),
]

CLAVES_E7 = [
    ['1', '(a) necesidad; (b) regla de negocio; (c) requisito funcional; (d) solución técnica; (e) regla de negocio (es RN-03); (f) solución técnica de interfaz.', 'Clasificar (e) como requisito porque tiene un número.'],
    ['2', '(a) La fuente respalda: E4-L2 dice que al devolver no sabe de cuál préstamo es. (b) No respalda: E3-L3 pide saber si un libro está antes de ir, no avisos de vencimiento; además «al celular» es una solución. Se descarta o se consulta. (c) Respalda: E4-L6 dice que no los puede borrar porque ahí está lo que se llevaron (junto con RN-06). (d) No respalda: E1-L4 habla de encontrar quién llevó un libro; las reservas no aparecen en el dossier y Work las deja fuera del núcleo.', 'Aceptar una fuente porque «tiene que ver con el tema».'],
    ['3', 'E5-L2: «El sistema debe informar la cantidad de préstamos de cada curso en un mes elegido» (coincide con RF-09). E4-L8: «Solo la bibliotecaria o su reemplazo autorizado deben poder registrar o modificar préstamos»; en el catálogo es de calidad (seguridad, RNF-02) porque limita quién opera, no agrega una operación. Se acepta como funcional si se redacta como acción del sistema y se justifica.', 'Escribir «hacer un login» (solución).'],
    ['4', 'Se registra con fuente E3-L4, pero fuera del catálogo inicial, con prioridad deseable: el circuito funciona sin renovar. Falta acordar una regla: cuántas renovaciones, por cuántos días y si se puede renovar un préstamo vencido. Se lleva al Capítulo 6.', 'Incluirlo como imprescindible porque lo pidió un lector.'],
    ['5', 'Cambia solo RN-02. RF-05 no cambia porque dice «el máximo vigente». Sí cambian los datos de su criterio de aceptación y de sus pruebas, que usan una cantidad concreta.', 'Decir que no cambia nada.'],
]

CLAVES_E8 = [
    ['1', '(a) Palabra vaga. Por ejemplo: «La consulta de disponibilidad de un título muestra el resultado en menos de 3 segundos en la computadora de la biblioteca (a confirmar)». (b) Cuantificador indefinido, y además contradice RNF-02: «Solo la bibliotecaria o su reemplazo autorizado modifican préstamos; los docentes consultan los de su curso (a confirmar)». (c) Compuesto: son dos requisitos. «Avisar» es además ambiguo, y las notificaciones externas están fuera del núcleo según Work. (d) Negación imposible de probar y palabra vaga «mal»: se reemplaza por los rechazos concretos de RF-04, RF-05 y RF-06.', 'Cambiar «rápido» por «muy rápido».'],
    ['2', 'RF-05: Dado un lector con el máximo vigente de préstamos activos (dos, según RN-02), cuando se intenta registrarle otro, entonces el sistema lo rechaza, muestra el motivo y el lector sigue con dos préstamos activos. RF-06: Dado un lector inactivo, cuando se intenta registrarle un préstamo, entonces se rechaza con el motivo y no se crea ningún préstamo.', 'Omitir el «entonces» observable.'],
    ['3', '(a) Es compuesto (punto 3), «intuitivo» es vago (punto 6), no tiene criterio (punto 5) y repite lo que ya cubren RF-01 y RNF-01. (b) Es una solución técnica (punto 4). La fuente solo respalda «sin internet», que ya es RS-01. No tiene criterio. (c) Reutiliza el identificador RF-04 (punto 1), no tiene fuente (punto 2), no tiene criterio (punto 5) ni prioridad (punto 7). La idea de fijar la fecha de referencia es correcta.', 'Marcar solo un problema por requisito.'],
    ['4', 'RF-04 imprescindible (RN-01). RF-07 imprescindible: necesidad del lector (E3-L3) y parte del alcance mínimo de Work. RF-09 importante. Renovación deseable. RNF-01 importante; se acepta imprescindible si se justifica que sin él la bibliotecaria no adopta el sistema.', 'Poner todo como imprescindible.'],
    ['5', 'Dado un préstamo activo de un lector, cuando una persona sin sesión consulta el catálogo y busca ese título, entonces ve la cantidad de ejemplares disponibles y no ve el nombre, el curso ni el código del lector.', 'Escribir «los datos están protegidos».'],
]

CLAVES_PRACTICA = [
    ['Nivel 1', 'B-01: necesidad de la docente, que da lugar a un requisito funcional. B-02: necesidad y regla nueva (no prestar un ejemplar en reparación). B-03: funcional (ya cubierto por RF-07) más calidad ambigua («rápido»). B-04: funcional (ya cubierto por RF-09); «impresos» es una preferencia de salida para confirmar. B-05: solución técnica, que además choca con RS-01. B-06: regla de negocio nueva. B-07: restricción (confirma RS-01). B-08: calidad (privacidad) con una contradicción interna. Fichas: «mostrar los préstamos activos de los lectores de un curso elegido», fuente B-01, prioridad importante. Criterio: dado un curso con dos lectores que tienen préstamos activos, cuando la docente lo consulta, entonces ve esos préstamos y ninguno de otro curso. RS: «sin conexión a internet en la computadora de la biblioteca», fuente B-07, que se suma a RS-01.'],
    ['Nivel 2', 'Catálogo posible: RF-11 préstamos activos por curso (B-01); RF-12 marcar y desmarcar un ejemplar «en reparación» (B-02); RF-13 rechazar el préstamo de un ejemplar en reparación (B-02); RF-14 informe mensual por curso en formato imprimible (B-04, o refinar RF-09); RNF-04 tiempo de respuesta de la consulta (B-03, a confirmar); RNF-05 solo los usuarios autorizados ven datos personales (B-08 y E5-L6). Restricción: B-07 confirma RS-01. Es válido anotarla como segunda fuente de RS-01 en lugar de crear RS-03, si se explica. Ambigüedades: B-03, preguntar «¿cuánto esperarías como máximo?»; B-08, preguntar «¿quién necesita ver qué datos?».'],
    ['Nivel 3', 'RN-07: un lector con un préstamo vencido no recibe nuevos préstamos hasta devolverlo. Agrega un bloqueo temporal distinto de RN-04 (inactivo) y de RN-02 (máximo). Requisito: «El sistema debe rechazar un nuevo préstamo a un lector que tiene un préstamo vencido a la fecha de la operación». Criterio con fecha de referencia. Aprueba la dirección, tras negociarlo en clase. B-02: aparece un estado temporal del ejemplar, distinto de la inactivación (RF-10). Hay que agregar requisitos para marcar y desmarcar, y RF-07 debe excluir los ejemplares en reparación. B-08: «protegidos» y «todos ven todo» se contradicen, y E5-L6 exige privacidad. Se registra el conflicto y se lleva a la dirección con opciones por rol.'],
]

LISTA_COTEJO = [
    ['Cada requisito tiene un identificador nuevo y no reutiliza uno existente.', 'Indicador 2'],
    ['La fuente citada existe y dice lo que se le atribuye.', 'Indicador 2'],
    ['Separa necesidades, reglas, requisitos y soluciones técnicas; B-05 no quedó como requisito.', 'Indicador 1'],
    ['Cada requisito expresa una sola cosa y no nombra tecnologías.', 'Indicador 2'],
    ['Cada requisito tiene un criterio «Dado… cuando… entonces…» comprobable por otra persona.', 'Indicador 3'],
    ['Cada prioridad tiene una razón basada en el criterio de 4.3.', 'Indicador 3'],
    ['Las ambigüedades se corrigen con una pregunta al interesado y una versión «a confirmar».', 'Indicador 4'],
]

C3 = [
    ['Identifica cada requisito', 'Sí: identificadores RF, RNF, RS y RN no reutilizables (4.3)'],
    ['Formula al menos ocho funcionales y cuatro no funcionales o restricciones', 'Sí en el ejemplo (10 RF, 3 RNF, 2 RS). El catálogo propio del equipo se completa entre los Capítulos 4 y 6.'],
    ['Define aceptación y prioridad', 'Sí (4.3, Tabla 4.5, Actividades 2 y 4 del Encuentro 8)'],
    ['Registra una modificación', 'No en este capítulo: corresponde a 6.4 (solicitud de cambio). El Desafío del Encuentro 7 la anticipa.'],
]

PROCEDENCIA = (['Recurso', 'Procedencia', 'Derechos'],
               [['Texto del capítulo', 'Redacción original para este libro.', 'Propios del proyecto.'],
                ['Figuras 4.1 y 4.2', 'Generadas con build/diagramas.py (matplotlib).', 'Propias; sin recursos de terceros.'],
                ['Dossier, buzón, personas y diálogos', 'Inventados; colegio y nombres ficticios. Los fragmentos E1 y E3 también aparecen en el material candidato para el Capítulo 2.', 'Propios del proyecto.'],
                ['Reglas RN-01 a RN-06 y cadena N-02, RN-01, RF-04, P-07', 'Tomadas del informe de Work (§7.2 y §7.3) como supuestos didácticos.', 'Insumo interno del proyecto.'],
                ['Forma «Dado… cuando… entonces…» y tipos de requisitos', 'Conocimiento general de la disciplina, con redacción propia.', 'No se copió material de terceros.'],
                ['Relación con Algorítmica 3.º', 'No se reutilizaron ejercicios, personas ni datos de ese libro.', 'No aplica.']])


def construir(ruta, claves, estado):
    doc = H.new_doc()
    M.portada(doc, C, 'Guía docente — capítulo de muestra, versión 2', estado)

    doc.add_heading('Guía docente · %s' % C.CAPITULO, level=1)
    H.p_texto(doc, C.TITULO, bold=True, size=13, color=H.ID['MED'])
    M.ficha(doc, C)
    H.caja(doc, 'Sobre la capacidad', [
        'La capacidad de la ficha es la C3 del programa institucional propuesto en el informe de Work. No es '
        'una capacidad oficial del MEC. Según el informe de Work, el diseño curricular que consultó (mayo de 2026, '
        'p. 29) permite que la institución elabore el programa del Plan Optativo, pero no prescribe esta '
        'asignatura; esa lectura no fue verificada por separado en esta fase.'],
        tipo='neutra')
    M.tabla(doc, (['Indicador de C3 (Work)', 'Cobertura en este capítulo'], C3), [6.6, 10.0],
            rotulo='Cobertura de los indicadores de C3')

    doc.add_heading('1. Secuencia de los encuentros', level=2)
    H.p_texto(doc, 'Estructura de taller de Work: 1 HC de problema y explicación, 3 HC de práctica y 1 HC de revisión. '
                   'Los tiempos son aproximados y la duración de la hora cátedra la fija cada institución.',
              italic=True, size=9.5)
    for titulo, filas in SECUENCIA:
        M.tabla(doc, (['Momento', 'Tiempo', 'Qué se hace'], filas), [3.0, 2.2, 11.4], rotulo=titulo)

    doc.add_heading('2. Claves de las actividades', level=2)
    M.tabla(doc, (['Act.', 'Respuesta esperada', 'Error frecuente'], CLAVES_E7), [1.2, 10.8, 4.6], rotulo='Encuentro 7')
    M.tabla(doc, (['Act.', 'Respuesta esperada', 'Error frecuente'], CLAVES_E8), [1.2, 10.8, 4.6], rotulo='Encuentro 8')

    doc.add_heading('3. Práctica 4: niveles, claves y lista de cotejo', level=2)
    H.p_texto(doc, 'Los tres niveles usan el mismo buzón, así que la puesta en común es una sola. El Nivel 1 es el '
                   'piso que todo el curso debe alcanzar. El Nivel 2 es el esperado para la mayoría. El Nivel 3 es '
                   'ampliación: no se exige para aprobar.')
    H.p_texto(doc, 'Criterio para asignar niveles: quien en la Actividad 1 del Encuentro 7 confundió reglas con '
                   'requisitos empieza en el Nivel 1; el Nivel 3 se ofrece a quien termina el Nivel 2.')
    M.tabla(doc, (['Nivel', 'Respuesta esperada'], CLAVES_PRACTICA), [2.2, 14.4], rotulo='Claves por nivel')
    M.tabla(doc, (['Criterio', 'Indicador'], LISTA_COTEJO), [13.6, 3.0], rotulo='Lista de cotejo de la Práctica 4')

    doc.add_heading('4. Evaluación del capítulo', level=2)
    H.p_texto(doc, 'Instrumento opcional y formativo: puede reemplazarse por la evidencia de la Práctica 4. Si se '
                   'toma, dura aprox. 1 HC, al final del encuentro 8 o al comienzo del 9. Alimenta el hito H2 '
                   '(encuentro 12). Puntaje: 15 puntos. Ítems 1 a 7: 1 punto cada uno. Ítem 8: 3 puntos. Ítem 9: 5 puntos.')
    filas = [[str(n), clave, detalle] for _, n, clave, detalle in claves]
    M.tabla(doc, (['Ítem', 'Clave', 'Respuesta o criterio'], filas), [1.2, 1.8, 13.6], rotulo='Clave de la evaluación')
    M.tabla(doc, (['Ítem', 'Puntaje completo', 'Puntaje parcial'], [
        ['8', '3: identificador y enunciado (1), fecha de referencia explícita (1), criterio con resultado esperado observable (1).', 'Cada parte por separado. 0 en el criterio si no dice qué se observa.'],
        ['9', '5: RN-07 con fuente R-07 (1), requisito sin tecnología (1), criterio comprobable (1), prioridad justificada (1), identificadores y fuentes correctos (1).', 'Cada parte por separado. Se valora la justificación de la prioridad, no la etiqueta.'],
    ]), [1.2, 8.4, 7.0], rotulo='Criterios de corrección de los ítems abiertos')

    doc.add_heading('5. Calendario con menos encuentros', level=2)
    H.p_texto(doc, 'En la adaptación de 28 encuentros del Piloto C, el Capítulo 4 conserva sus dos encuentros. Si se '
                   'pierde uno, se sigue el recuadro final del libro del estudiante: se mantiene la actividad central '
                   '(Ejemplos resueltos 4.2 y 4.3 y Práctica 4, Niveles 1 o 2) y se evalúa con la Práctica 4.')

    doc.add_heading('6. Procedencia y derechos de los recursos', level=2)
    M.tabla(doc, PROCEDENCIA, [4.8, 7.2, 4.6], rotulo='Inventario de recursos del capítulo')
    H.finalizar(doc, ruta)

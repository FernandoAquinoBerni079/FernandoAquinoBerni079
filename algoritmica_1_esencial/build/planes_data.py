# -*- coding: utf-8 -*-
"""Datos de los 37 planes de clase (y de las 37 filas del Plan Anual) de Algorítmica 1.º, Edición Esencial.
No hay planes de clase vigentes de 1.º: se construyen desde el libro nuevo (fichas, secciones, figuras,
actividades y prácticas) y, para procedimientos e instrumentos de las clases, desde el Plan Anual vigente
(37 encuentros de 4 HC). Las 14 clases de 8 HC del plan vigente se dividen en la clase y su continuación."""
import re
from estructura import cargar
import ediciones, actividades, practicas, evaluaciones

_pre, C, _ev, U = cargar()
U = {1: 'Teoría de Conjuntos', 2: 'Lógica Simbólica', 3: 'Introducción a la Algoritmia'}
ediciones.aplicar(C)
FIGS = ediciones.fig_refs(C)

# orden de los 37 encuentros: ('C', n) clase · ('P', n) continuación (segunda jornada de 4 HC) · ('E', id) evaluación integradora
CONT = {2, 4, 5, 7, 8, 9, 12, 14, 16, 17, 18, 19, 20, 21}
ORDEN = []
for n in range(1, 22):
    ORDEN.append(('C', n))
    if n in CONT:
        ORDEN.append(('P', n))
    if n == 12:
        ORDEN.append(('E', 'E1'))
ORDEN.append(('E', 'E2'))
N_ENC = len(ORDEN)
E1_POS = ORDEN.index(('E', 'E1')) + 1
assert N_ENC == 37 and E1_POS == 20
EVAL_UNIDAD_EN = {('P', 5): 'U1', ('P', 12): 'U2', ('P', 21): 'U3'}
UNIDAD_DE = {n: C[n]['unidad'] for n in C}
# etapas del Proyecto Final Integrador en las segundas jornadas de la Unidad 3
PFI_EN = {17: 'etapa 1, definición: el equipo elige el emprendimiento, lista sus productos y precios y los agrupa en conjuntos por tipo',
          19: 'etapa 2, construcción (primera parte): diagrama de flujo y pseudocódigo del algoritmo de caja básico del emprendimiento, con tres casos de prueba anotados',
          20: 'etapa 2, construcción (segunda parte): prueba de escritorio de los tres casos y reglas del negocio simbolizadas con su tabla de verdad',
          21: 'etapa 3, integración y ensayo: el algoritmo pasa a PSeInt, se integran los aportes de las otras materias y se ensaya la demostración'}

# procedimientos e instrumentos de las clases: Plan Anual vigente (sin la mención a la evaluación de unidad, que va en la continuación)
PROC_INST = {
 1: ('Prueba diagnóstica de saberes previos. Exploración de colecciones del entorno para distinguir cuáles están bien definidas; escritura de conjuntos del menú del copetín por extensión y por comprensión.', 'Prueba diagnóstica. Lista de cotejo de la escritura correcta de conjuntos con llaves, ∈/∉ y cardinal.'),
 2: ('Clasificación de conjuntos dados en tarjetas (finito, infinito, unitario, vacío, universal); construcción de todos los subconjuntos de conjuntos de 2 y 3 elementos.', 'Ejercicio práctico de generación de los 2ⁿ subconjuntos con verificación entre pares.'),
 3: ('Dibujo de diagramas de Venn de uno y dos conjuntos; traducción de diagramas a símbolos y de enunciados simbólicos a diagramas.', 'Rúbrica de diagramas: regiones correctas, elementos bien ubicados, rotulado completo.'),
 4: ('Cálculo de uniones e intersecciones sobre pedidos por turno del copetín; verificación de las propiedades conmutativa y asociativa con ejemplos numéricos.', 'Prueba corta de cálculo de A ∪ B y A ∩ B con conjuntos por extensión.'),
 5: ('Resolución guiada de problemas de conteo con dos conjuntos (encuesta de clientes); aplicación del control del universo como verificación obligatoria.', 'Resolución individual de un problema de Venn con control de suma de regiones.'),
 6: ('Análisis de oraciones del aula y del copetín para decidir cuáles son proposiciones; clasificación en abiertas, atómicas y moleculares con justificación oral.', 'Ejercicio de clasificación y simbolización de expresiones, con justificación escrita del criterio.'),
 7: ('Simbolización de reglas del copetín con letras, conectivos y paréntesis; cálculo del valor de verdad de compuestas con valores dados, de adentro hacia afuera.', 'Ejercicio de simbolización y evaluación paso a paso corregido en plenaria.'),
 8: ('Construcción de tablas de verdad de dos variables con el orden estándar de filas; evaluación por columnas de fórmulas con negaciones y paréntesis.', 'Tabla de verdad completa de una fórmula dada, revisada con lista de cotejo fila a fila.'),
 9: ('Construcción de tablas de 8 filas con tres variables; clasificación de fórmulas en tautología, contradicción o indeterminación señalando las filas decisivas.', 'Prueba escrita de clasificación de dos fórmulas mediante sus tablas completas.'),
 10: ('Verificación de equivalencias comparando columnas finales; negación de carteles y reglas del copetín aplicando las leyes de De Morgan.', 'Ejercicio de negación correcta de conjunciones y disyunciones con De Morgan.'),
 11: ('Conversión de funciones proposicionales en proposiciones con ∀ y ∃ sobre conjuntos de la Unidad 1; búsqueda de contraejemplos y negación de cuantificadores.', 'Ejercicio de evaluación del valor de verdad de proposiciones cuantificadas, con justificación.'),
 12: ('Identificación de la regla de inferencia en razonamientos cotidianos simbolizados; construcción de deducciones de dos pasos citando la regla usada en cada paso.', 'Producción escrita de una deducción con premisas dadas, evaluada con rúbrica de validez.'),
 13: ('Comparación de instrucciones cotidianas para detectar ambigüedad, infinitud o indefinición; clasificación de algoritmos del entorno en cualitativos y cuantitativos.', 'Lista de cotejo de las tres características sobre algoritmos redactados por el grupo.'),
 14: ('Escritura de algoritmos secuenciales en pseudocódigo y traducción a diagrama de flujo con los símbolos normalizados; lectura inversa de diagramas dados.', 'Rúbrica de diagramas de flujo: símbolo correcto por acción y flujo sin cortes.'),
 15: ('Evaluación de expresiones aritméticas con jerarquía de operadores; resolución de comparaciones relacionales y condiciones lógicas con Y, O y NO.', 'Prueba corta de evaluación de expresiones paso a paso con jerarquía explícita.'),
 16: ('Construcción del algoritmo de la compra completa (leer, asignar, escribir); primera prueba de escritorio en tabla con una columna por variable.', 'Prueba de escritorio documentada en tabla, verificada contra el resultado esperado.'),
 17: ('Diseño de decisiones simples Si–Entonces–Sino sobre descuentos del copetín; análisis del caso frontera según el operador relacional elegido.', 'Resolución de un problema con decisión probado en los caminos V, F y frontera.'),
 18: ('Construcción de decisiones anidadas para clasificar compras en tres categorías; verificación de cobertura total y de categorías disjuntas.', 'Ejercicio de clasificación anidada con pruebas de escritorio por categoría.'),
 19: ('Diseño de ciclos Mientras y Para con contadores bien inicializados; rastreo de ejecución vuelta por vuelta y detección de ciclos infinitos en ejemplos con error.', 'Prueba de escritorio de un ciclo, vuelta por vuelta, con detección del corte.'),
 20: ('Cálculo de totales y promedios con acumulador y contador; diseño de ciclos con centinela para la caja diaria y protección contra la división por cero.', 'Resolución de un problema de totalización con centinela y verificación del promedio.'),
 21: ('Desarrollo integral del sistema de caja Karumbé: análisis, diseño con decisión y repetición, prueba de escritorio con datos reales, control cruzado y puente a PSeInt mediante reproducción y modificación guiada de un modelo completo antes de la producción autónoma.', 'Proyecto integrador evaluado con rúbrica: análisis, algoritmo, prueba, control cruzado y ejecución guiada en PSeInt.'),
}

# disparador del inicio de cada clase (problema del caso, sin adelantar la respuesta)
DISPARADOR = {
 1: 'Pregunta disparadora: ¿qué tienen en común el menú del copetín, la lista de medios de pago y las letras de una palabra? Registro en la pizarra de ejemplos de «colecciones» del aula.',
 2: 'Situación: Ña Rosa quiere saber cuántos combos distintos puede armar con los productos del menú. Se anotan las primeras ideas del grupo, sin calcular.',
 3: 'Situación: los productos de la mañana y los de la siesta se cruzan en algunos casos. ¿Cómo se puede dibujar eso para verlo de un golpe de vista?',
 4: 'Situación: ¿qué se vendió en el día y qué se pidió en los dos turnos? Se escriben en la pizarra las listas de un día de ejemplo y se pide al grupo responder sin fórmulas.',
 5: 'Situación: Ña Rosa encuestó a sus clientes sobre dos bebidas y los números no le cierran. ¿Cómo contar sin contar a nadie dos veces?',
 6: 'Pregunta disparadora: ¿todas las oraciones pueden ser verdaderas o falsas? Se escriben en la pizarra una pregunta, una orden, una opinión y una afirmación del copetín.',
 7: 'Situación: un cartel del copetín dice «si comprás dos chipas, te regalo un cocido». ¿Cuándo diría el cliente que Ña Rosa no cumplió? Discusión con escenarios.',
 8: 'Situación: una promo se activa con dos condiciones. ¿En cuántas situaciones distintas puede estar un cliente y en cuáles hay promo? Se pide al grupo listarlas.',
 9: 'Situación: un sistema tiene una regla que nunca se activa y otra que se activa siempre. ¿Cómo detectar esas reglas antes de usarlas?',
 10: 'Situación: el cartel «hay chipa y hay cocido» resultó falso. ¿Qué se puede afirmar con seguridad? Se registran las respuestas del grupo sin corregir.',
 11: 'Pregunta disparadora: «todos los productos cuestan menos de 20.000». ¿Cuántos productos hay que revisar para saber si es verdad? ¿Y para saber que es falso?',
 12: 'Situación: «si es viernes, hay chipa; hoy no hay chipa». ¿Qué se puede concluir? ¿Y si hoy sí hay chipa? Debate breve con votación a mano alzada.',
 13: 'Pregunta disparadora: ¿una receta «a gusto» es un algoritmo? Se comparan dos instrucciones para preparar el mostrador: una vaga y una precisa.',
 14: 'Situación: Ña Rosa quiere que cualquiera pueda calcular el vuelto sin preguntarle nada. ¿Cómo se escriben los pasos para que no haya dudas?',
 15: 'Situación: dos estudiantes calcularon 7 + 2 × 3 y obtuvieron resultados distintos. ¿Quién tiene razón y por qué? ¿Cómo «lee» la computadora una expresión?',
 16: 'Situación: un cliente compra tres chipas y paga con un billete grande. ¿Qué pasos hace la caja, en qué orden y qué valor tiene cada dato en cada paso?',
 17: 'Situación: las compras de G. 50.000 o más tienen descuento. ¿Qué pasa con una compra de exactamente 50.000? Se anotan las respuestas del grupo antes de formalizar.',
 18: 'Situación: Ña Rosa quiere clasificar a sus clientes en tres grupos según lo que compran. ¿Alcanza con una sola pregunta de sí o no?',
 19: 'Situación: numerar las bandejas de chipa que salen del horno, una por una. ¿Cómo se escribe «repetir» sin copiar la misma línea muchas veces?',
 20: 'Situación: al cierre del día, Ña Rosa quiere el total y el promedio de sus ventas, sin saber de antemano cuántas fueron. ¿Cuándo termina la carga?',
 21: 'Situación: el encargo completo de Ña Rosa para el cierre del día. ¿Qué piezas de las clases anteriores hacen falta y en qué orden se arman?',
}

CRITERIOS_U = {
 1: ['Usa la notación de conjuntos (llaves, ∈, ⊆, ∪, ∩) con precisión.', 'Verifica los resultados de conteo con el control del universo o con un segundo camino.'],
 2: ['Simboliza con letras, conectivos y paréntesis sin ambigüedad.', 'Justifica cada valor de verdad con la tabla o la regla correspondiente.'],
 3: ['Escribe los algoritmos con la notación del libro (Inicio, Leer, ←, Escribir, Fin) y con sangría.', 'Anticipa el resultado y lo comprueba con una prueba de escritorio.'],
}

ALT = {'PSeInt': ' Alternativa sin equipamiento disponible: el algoritmo se escribe y se prueba en papel con prueba de escritorio, y se ejecuta en la primera sesión de laboratorio disponible.'}


def _alt(entorno):
    for k, v in ALT.items():
        if k in entorno:
            return v
    return ''


def _fam(n):
    it = actividades.items(n)
    er = [k for f, k, *_ in it if f.startswith(('Ejercit', 'Resolv'))]
    pd = [k for f, k, *_ in it if f.startswith('Pens')]
    de = [k for f, k, *_ in it if f.startswith('Desaf')]
    return er, pd, de


def _y(lst):
    lst = [str(x) for x in lst]
    return ' y '.join(lst) if len(lst) <= 2 else ', '.join(lst[:-1]) + ' y ' + lst[-1]


def _secciones(n):
    h2 = [b['text'] for b in C[n]['cuerpo'] if b['t'] == 'h2' and not b['text'].startswith('Ejemplo resuelto')]
    figs = [b['num'] for b in C[n]['cuerpo'] if b['t'] == 'img']
    ej = [b['text'].split(' — ', 1)[1] for b in C[n]['cuerpo'] if b['t'] == 'h2' and b['text'].startswith('Ejemplo resuelto')]
    return h2, figs, ej


def plan_clase(idx, n):
    cont = n in CONT
    p = practicas.PR[n]
    h2, figs, ej = _secciones(n)
    mitad = (len(h2) + 1) // 2
    er, pd, de = _fam(n)
    ini = [DISPARADOR[n],
           'Presentación de la capacidad, el tema y los indicadores de la ficha de la Clase %d.' % n]
    if n == 1:
        ini.insert(0, 'Aplicación de la prueba diagnóstica del libro (sin nota) para relevar saberes previos.')
    elif C[n]['unidad'] != C.get(n - 1, {}).get('unidad'):
        ini.insert(0, 'Lectura de la apertura de la Unidad %d y anticipación de lo que se va a aprender.' % C[n]['unidad'])
    else:
        ini.insert(0, 'Recuperación de la clase anterior a partir del desafío de la Clase %d.' % (n - 1))
    des = ['Desarrollo guiado: %s.' % _y(['«%s»' % x for x in h2[:mitad]])
           + (' Lectura de la %s como apoyo visual.' % _y(figs) if figs else ''),
           'Continuación del desarrollo: %s.' % _y(['«%s»' % x for x in h2[mitad:]])]
    if ej:
        des.append('Ejemplo resuelto paso a paso del libro («%s»), reproducido en la pizarra con la participación del grupo.' % ej[0])
    des.append('Resolución individual o en parejas de las actividades de aplicación %d a %d (Ejercitá y Resolvé).' % (er[0], er[-1]))
    if cont:
        des.append('Práctica %d del libro, «%s» (%s): Actividad 1, «%s». Las actividades siguientes se trabajan en el encuentro de continuación.' % (n, p['titulo'], p['entorno'], p['acts'][0]['titulo']))
    else:
        des.append('Práctica %d del libro, «%s» (%s): Actividad 1, «%s», y Actividad 2, «%s»; la Actividad 3, «%s», queda como tarea con su punto de control.' % (n, p['titulo'], p['entorno'], p['acts'][0]['titulo'], p['acts'][1]['titulo'], p['acts'][2]['titulo']))
    acts = p['acts'][:1] if cont else p['acts'][:2]
    cie = ['Verificación de los puntos de control de la Práctica %d (%s).' % (n, '; '.join('Actividad %d: «%s»' % (k, a['control']) for k, a in enumerate(acts, 1))),
           'Puesta en común de las afirmaciones %s (Pensá y decidí), con justificación oral.' % _y(pd)]
    if cont:
        cie.append('Anuncio del encuentro de continuación: Actividades 2 y 3 de la Práctica %d%s.' % (n, ', con transferencia entre pares' if p.get('transfer') else ''))
    else:
        cie.append('Asignación del desafío %d y del desafío final de la Práctica %d para quienes terminan antes.' % (de[0], n))
    if ('P', n) in EVAL_UNIDAD_EN:
        cie.append('Anuncio: la evaluación de la Unidad %d se aplica al cierre del encuentro de continuación.' % UNIDAD_DE[n])
    rec = 'Libro del estudiante, Clase %d%s, actividades 1 a %d y Práctica %d · %s · pizarra y marcadores.' % (
        n, (' (%s)' % _y(figs)) if figs else '', er[-1] + len(pd) + len(de), n, p['entorno'])
    if n == 21:
        rec = rec.rstrip('.') + ' · computadora con PSeInt para el «Puente a PSeInt».' + ALT['PSeInt']
    f = C[n]['ficha']
    proc, inst = PROC_INST[n]
    crit = CRITERIOS_U[UNIDAD_DE[n]] + ['Cumple los puntos de control de la Práctica %d sin ayuda externa.' % n]
    return dict(idx=idx, tipo='C', n=n, titulo=C[n]['titulo'], tema=f['tema'], capacidad=f['capacidad'], indicadores=f['indicadores'],
                unidad='UNIDAD %d — %s' % (UNIDAD_DE[n], U[UNIDAD_DE[n]]), material='Libro del estudiante · Clase %d y Práctica %d' % (n, n),
                momentos={'Inicio': ini, 'Desarrollo': des, 'Cierre': cie}, tiempos=(40, 90, 30), recursos=rec, proc=proc, inst=inst, criterios=crit)


# procedimientos e instrumentos propios de cada continuación (únicos en todo el Plan Anual)
CONT_EVAL = {
 2: ('Generación ordenada de subconjuntos por cantidad de elementos y distinción entre pertenencia e inclusión en afirmaciones dadas.', 'Lista de subconjuntos de un conjunto de tres elementos agrupada por tamaño y tabla de afirmaciones con ∈ y ⊆ corregidas.'),
 4: ('Operaciones combinadas con tres conjuntos numéricos, detección de pares disjuntos y verificación de propiedades sin calcular.', 'Hoja de operaciones con conjuntos numéricos y justificación escrita de los pares disjuntos.'),
 5: ('Reconstrucción de los datos de una encuesta a partir de las regiones del diagrama y transferencia a un mini-caso de biblioteca con revisión entre pares.', 'Diagrama de la biblioteca corregido tras la revisión entre pares, con control del universo.'),
 7: ('Evaluación paso a paso de compuestas con cuatro variables y análisis de los cuatro escenarios de una promesa condicional.', 'Tabla de escenarios del condicional con la fila que rompe la promesa justificada por escrito.'),
 8: ('Construcción de tablas de dos fórmulas en paralelo y lectura de la columna final como regla del negocio.', 'Dos tablas de verdad comparadas y respuesta en palabras y en símbolos al caso del copetín cerrado.'),
 9: ('Clasificación de fórmulas con tablas de cuatro filas, detección de reglas rotas y transferencia a un sistema de pedidos con revisión entre pares.', 'Tablas de las tres reglas del sistema de pedidos, con la recomendación de cada una revisada por otro equipo.'),
 12: ('Producción de conclusiones encadenadas a partir de premisas dadas y análisis de una falacia y de un razonamiento inductivo.', 'Cadena de conclusiones con la regla de cada paso y contraejemplo escrito de la falacia.'),
 14: ('Emparejamiento de acciones con símbolos y dibujo del diagrama de flujo completo de un algoritmo dado, con prueba siguiendo el diagrama.', 'Diagrama de flujo del algoritmo del área con conteo de figuras y prueba de escritorio sobre el diagrama.'),
 16: ('Rastreo de asignaciones encadenadas (intercambio sin auxiliar) y diseño de un algoritmo secuencial propio con verificación del promedio.', 'Tabla de escritorio del intercambio repetida con otros valores y algoritmo del promedio con su verificación.'),
 17: ('Uso del operador mod en una decisión, diseño de una decisión propia con frontera y definición del emprendimiento del proyecto.', 'Algoritmos de par o impar y de precio mayorista probados con frontera; ficha de definición del emprendimiento.'),
 18: ('Combinación de condiciones compuestas con decisiones y reparación del orden de una cadena anidada defectuosa.', 'Tabla de los cuatro escenarios de la promo vinculada a la conjunción y cadena corregida con sus tres pruebas.'),
 19: ('Reescritura de un ciclo Para como Mientras, reparación de ciclos infinitos y diseño del algoritmo de caja básico del proyecto.', 'Versiones corregidas de los dos ciclos con su tabla corta y pseudocódigo del algoritmo de caja del emprendimiento.'),
 20: ('Contador condicionado dentro de un ciclo con centinela, totalización completa con guarda y transferencia a la rifa con revisión entre pares.', 'Algoritmo de la rifa en sus dos versiones (original y corregida) con prueba de escritorio y justificación del cambio.'),
 21: ('Control cruzado del sistema de caja, extensión con la venta más alta y paso del algoritmo del proyecto a PSeInt con ensayo de la demostración.', 'Control cruzado que cierra al guaraní, algoritmo del proyecto ejecutado en PSeInt y guion de la demostración.'),
}
assert set(CONT_EVAL) == CONT


def plan_continuacion(idx, n):
    p = practicas.PR[n]
    acts = p['acts'][1:]
    ev = EVAL_UNIDAD_EN.get(('P', n))
    ini = ['Recuperación del punto de control de la Actividad 1 de la Práctica %d y organización de las parejas de trabajo.' % n,
           'Presentación del objetivo de la Actividad 2: %s' % acts[0]['objetivo']]
    des = []
    for k, a in enumerate(acts, 2):
        des.append('Actividad %d, «%s»: %s Acompañamiento docente en el paso que suele traer más dificultad: %s' % (k, a['titulo'], a['objetivo'], a['pasos'][0][0].lower() + a['pasos'][0][1:]))
    if p.get('transfer'):
        des.append('Transferencia y revisión entre pares (30 a 40 minutos): mini-caso «%s» con datos diferentes; intercambio con otro equipo, detección de al menos un error o mejora, corrección y justificación escrita de la versión final.' % p['transfer']['caso'][0])
    if n in PFI_EN:
        des.append('Proyecto Final Integrador, %s.' % PFI_EN[n])
    else:
        des.append('Desafío final para quienes terminan antes: %s' % p['desafio'])
    cie = ['Verificación de los puntos de control: %s.' % '; '.join(['Actividad %d, «%s»' % (k, a['control']) for k, a in enumerate(acts, 2)] + (['transferencia entre pares, «%s»' % p['transfer']['control']] if p.get('transfer') else [])),
           'Registro breve de dificultades y corrección colectiva de los errores frecuentes de la práctica.']
    tiempos = (20, 120, 20)
    if ev:
        cie.append('Aplicación de la evaluación de la Unidad %s, fotocopiable, en su hoja propia del libro.' % ev[1])
        tiempos = (20, 100, 40)
    rec = 'Libro del estudiante, Práctica %d (Actividades %s%s y desafío final) · %s' % (n, _y(list(range(2, len(p['acts']) + 1))), ', transferencia' if p.get('transfer') else '', p['entorno'])
    if n in PFI_EN:
        rec += ' · Proyecto Final Integrador del libro'
    if n == 21:
        rec += ' · computadora con PSeInt'
    rec += ' · pizarra y marcadores.' + (ALT['PSeInt'] if n == 21 else '')
    f = C[n]['ficha']
    proc, inst = CONT_EVAL[n]
    if ev:
        inst = inst.rstrip('.') + '. Evaluación de la Unidad %s (fotocopiable).' % ev[1]
    crit = ['Cumple el punto de control de cada actividad sin ayuda externa.', 'Justifica sus decisiones con los conceptos de la Clase %d.' % n,
            'Corrige sus errores a partir de la verificación y deja el trabajo documentado.']
    return dict(idx=idx, tipo='P', n=n, titulo='Continuación de la Clase %d: %s' % (n, p['titulo']), tema=f['tema'], capacidad=f['capacidad'],
                indicadores=f['indicadores'], unidad='UNIDAD %d — %s' % (UNIDAD_DE[n], U[UNIDAD_DE[n]]), material='Libro del estudiante · Práctica %d' % n,
                momentos={'Inicio': ini, 'Desarrollo': des, 'Cierre': cie}, tiempos=tiempos, recursos=rec, proc=proc, inst=inst, criterios=crit)


EV_IND = {'E1': ['Determina conjuntos y resuelve problemas de operaciones y de conteo con diagramas de Venn.', 'Simboliza proposiciones, calcula valores de verdad y construye tablas para decidir equivalencias.', 'Niega proposiciones cuantificadas y aplica reglas de inferencia nombrándolas.'],
          'E2': ['Opera con conjuntos y aplica De Morgan y las reglas de inferencia a situaciones del caso.', 'Evalúa expresiones respetando la jerarquía de operadores.', 'Diseña decisiones anidadas y realiza la prueba de escritorio del sistema de caja con control cruzado.']}
EV_DESC = {'E1': 'operaciones con conjuntos, problema de conteo con Venn, simbolización y valor de verdad, tabla para decidir una equivalencia, negación de un cuantificador y regla de inferencia',
           'E2': 'operaciones con conjuntos de días, valores de verdad con De Morgan, MTT, jerarquía de operadores, clasificación anidada de pedidos, prueba de escritorio del sistema de caja y propuesta de mejora'}


def plan_eval(idx, eid):
    e = [x for x in evaluaciones.EV if x['id'] == eid][0]
    nb = len(e['ab'])
    pts = 3 + 3 * nb
    etapa = '1.ª etapa (Unidades 1 y 2)' if eid == 'E1' else '2.ª etapa (Unidades 1 a 3)'
    des = ['Lectura en voz alta de las consignas y aclaración de dudas de redacción, sin resolver.',
           'Resolución individual de la Parte A, de diagnóstico rápido: tres consignas de opción múltiple.',
           'Resolución individual de la Parte B, de resolución y aplicación: %d consignas (%s).' % (nb, EV_DESC[eid])]
    return dict(idx=idx, tipo='E', n=eid, titulo='Evaluación integradora de la %s' % etapa, tema='Evaluación integradora de la %s' % etapa,
                capacidad=ediciones.caps(ediciones.CAP_EVAL[eid]), indicadores=EV_IND[eid],
                unidad='Evaluación integradora · %s' % ('cierre de la 1.ª etapa (junio)' if eid == 'E1' else 'cierre de la 2.ª etapa (noviembre)'),
                material='Libro del estudiante · evaluación integradora fotocopiable en hoja propia',
                momentos={'Inicio': ['Organización del aula para el trabajo individual y lectura de las pautas de la prueba (tiempo, materiales permitidos, puntaje).'],
                          'Desarrollo': des,
                          'Cierre': ['Entrega de la prueba y revisión de que todas las consignas tengan respuesta.', 'Anuncio de la fecha de devolución y de la corrección colectiva.']},
                tiempos=(15, 130, 15),
                recursos='Evaluación integradora fotocopiable del libro (hoja propia) · clave del Solucionario docente · lápiz, goma y regla.',
                proc='Resolución individual de la prueba integradora de la %s.' % etapa,
                inst='Prueba integradora fotocopiable de la %s: 3 ítems de opción múltiple y %d de resolución, con clave y puntaje sugerido (%d puntos).' % (etapa, nb, pts),
                criterios=['Resuelve cada consigna con el procedimiento pedido.', 'Muestra los cálculos, las tablas o la traza que respaldan cada resultado.', 'Expresa las respuestas con precisión y con la notación del libro.'])


def planes():
    out = []
    for idx, (t, n) in enumerate(ORDEN, 1):
        out.append({'C': plan_clase, 'P': plan_continuacion, 'E': plan_eval}[t](idx, n))
    for p in out:
        assert sum(p['tiempos']) == 160, (p['idx'], p['tiempos'])
    assert len({p['proc'] for p in out}) == N_ENC and len({p['inst'] for p in out}) == N_ENC
    return out


if __name__ == '__main__':
    import json
    PL = planes()
    for p in PL:
        txt = json.dumps(p, ensure_ascii=False)
        for bad in ('Cuaderno', 'cuadernillo', 'tomo'):
            if bad in txt:
                print('RESIDUO', p['idx'], bad)
    print(len(PL), 'planes')
    print(json.dumps(PL[0], ensure_ascii=False, indent=1)[:3000])

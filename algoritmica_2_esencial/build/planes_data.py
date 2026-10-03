# -*- coding: utf-8 -*-
"""Datos de los 36 planes de clase (y de las 36 filas del Plan Anual) de Algorítmica 2.º, Edición Esencial.
No hay planes de clase vigentes de 2.º: se construyen desde el libro nuevo (fichas, secciones, figuras,
actividades y prácticas) y, para temas, procedimientos e instrumentos de las clases, desde el Plan Anual
vigente (sin las referencias al Cuaderno de Prácticas). Orden de encuentros: el del Plan Anual vigente."""
import re
from estructura import cargar
import ediciones, actividades, practicas, evaluaciones

_pre, C, _ev, U = cargar()
ediciones.aplicar(C)
FIGS = ediciones.fig_refs(C)

# orden de los 36 encuentros: ('C', n) clase · ('P', n) continuación práctica · ('E', id) · ('T', k) taller PFI
CONT = {7, 10, 14, 15, 16, 17, 18, 19, 20, 21}
ORDEN = []
for n in range(1, 22):
    ORDEN.append(('C', n))
    if n in CONT:
        ORDEN.append(('P', n))
    if n == 14:
        ORDEN.append(('E', 'E1'))
ORDEN += [('T', 1), ('T', 2), ('T', 3), ('E', 'E2')]
assert len(ORDEN) == 36 and ORDEN.index(('E', 'E1')) == 17
EVAL_UNIDAD_EN = {('P', 7): 'U1', ('P', 14): 'U2', ('P', 18): 'U3', ('P', 21): 'U4'}
UNIDAD_DE = {n: C[n]['unidad'] for n in C}

# procedimientos e instrumentos de las clases: Plan Anual vigente, sin las menciones al Cuaderno de Prácticas
PROC_INST = {
 1: ('Prueba diagnóstica de saberes previos. Análisis de problemas; identificación de datos y tipos; escritura de algoritmos secuenciales en pseudocódigo.', 'Prueba diagnóstica. Ejercicios de clasificación de datos y traducción a pseudocódigo.'),
 2: ('Formulación de condiciones con operadores relacionales; trazado de la estructura Si simple.', 'Ejercicios de condiciones y problemas de decisión con Si simple.'),
 3: ('Construcción de estructuras Si-Sino; traza de los dos caminos sobre problemas de caja.', 'Ejercicios y problemas de resolución con Si-Sino.'),
 4: ('Evaluación de condiciones compuestas con tablas de verdad; elección del operador lógico Y/O/NO.', 'Ejercicios de operadores lógicos y problemas de decisión combinada.'),
 5: ('Construcción de estructuras anidadas y de la estructura Segun; traza hasta el camino correcto.', 'Ejercicios de clasificación en más de dos caminos; problemas con Segun.'),
 6: ('Implementación de ciclos Mientras y Repetir; uso del contador; prevención del ciclo infinito.', 'Ejercicios de ciclos y conteo; problemas de recorrido de datos.'),
 7: ('Implementación del ciclo Para; uso de acumulador, bandera y centinela; pruebas de escritorio.', 'Ejercicios y problemas con Para, acumulador y centinela.'),
 8: ('Declaración, carga y recorrido de vectores en PSeInt; acceso por índice.', 'Ejercicios de carga y acceso; problemas del caso con vectores.'),
 9: ('Recorrido de vectores para suma, promedio, máximo, mínimo y búsqueda con bandera.', 'Ejercicios de operaciones sobre vectores; problemas del caso.'),
 10: ('Declaración y recorrido de matrices con ciclos anidados; cálculo de totales por fila y columna.', 'Ejercicios de recorrido de matrices; problema de totales del caso.'),
 11: ('Aplicación de los métodos de burbuja y selección; intercambio con variable auxiliar; traza de pasadas.', 'Ejercicios de ordenación; construcción de un ranking del caso.'),
 12: ('Generación de números aleatorios; distinción entre azar y cálculo; simulación con ciclos.', 'Ejercicios de sorteo y de simulación de ventas.'),
 13: ('Definición e invocación de procedimientos y funciones; distinción entre variables locales y globales.', 'Ejercicios de subprogramas; armado de un mini-sistema modular del caso.'),
 14: ('Pasaje de parámetros por valor y por referencia; uso de funciones de cadena.', 'Ejercicios de parámetros y de manipulación de cadenas.'),
 15: ('Análisis del concepto y los tipos de archivo; comparación entre memoria principal y secundaria.', 'Ejercicios de clasificación de archivos; diseño de un archivo del caso.'),
 16: ('Secuencia de operaciones abrir/escribir/leer/cerrar; pseudocódigo de guardado y recuperación.', 'Ejercicios de operaciones de archivo; problema de guardado y lectura.'),
 17: ('Identificación de mecanismos de seguridad; distinción de tipos de acceso; función del buffer.', 'Ejercicios de seguridad de archivos; plan de protección del caso.'),
 18: ('Organización de archivos en carpetas, subcarpetas y rutas; uso del Explorador de archivos.', 'Ejercicios de rutas; diseño del árbol de carpetas del caso.'),
 19: ('Distinción entre tabla, registro y campo; aplicación de filtros por condición sobre una tabla.', 'Ejercicios de filtros sobre la tabla de productos del caso.'),
 20: ('Formulación de consultas de selección, paramétricas y de totales; definición de campos calculados en el gestor.', 'Ejercicios de consultas y campos calculados en el gestor.'),
 21: ('Formulación e interpretación de consultas de referencias cruzadas; aplicación de buenas prácticas.', 'Ejercicios de referencias cruzadas; interpretación de resultados.'),
}

# disparador del inicio de cada clase (problema del caso, sin adelantar la respuesta)
DISPARADOR = {
 1: 'Pregunta disparadora: ¿qué hace falta saber antes de poder cobrar un pedido del copetín? Registro en la pizarra de datos de entrada, proceso y resultado.',
 2: 'Situación: el copetín descuenta el 10 % solo a las ventas que llegan a G. 50.000. ¿Cómo «decide» la caja si corresponde el descuento? Lluvia de ideas sobre el «solo si».',
 3: 'Situación: un pedido de delivery paga envío o no según el monto. Se pide al grupo nombrar los dos caminos posibles y qué pasa en cada uno.',
 4: 'Situación: «envío gratis si el monto llega a 50.000 y el cliente vive en el barrio». ¿Alcanza con una sola pregunta? Discusión con dos pedidos de ejemplo.',
 5: 'Situación: clasificar ventas en chicas, medianas y grandes, y atender un menú numerado. ¿Sirve un Si… Sino para tres o más caminos?',
 6: 'Situación: el copetín quiere saber cuántas ventas hacen falta para llegar a la meta del día, sin saber de antemano cuántas serán.',
 7: 'Situación: sumar las siete ventas de la semana y avisar si algún día fue muy flojo. ¿Qué cambia cuando se sabe cuántas veces repetir?',
 8: 'Situación: guardar las siete ventas de la semana en siete variables distintas. ¿Qué pasa cuando son 30 días? Se presenta la necesidad del vector.',
 9: 'Situación: con la semana cargada, el dueño pregunta cuánto se vendió, cuál fue el mejor día y si hubo un día de exactamente 850.000.',
 10: 'Situación: la planilla de unidades vendidas por producto y por día. ¿Cómo se guarda una tabla entera en un programa?',
 11: 'Situación: el dueño quiere el ranking de productos más vendidos del mes. ¿Cómo se ordena una lista a mano? Se registra el procedimiento que usan los estudiantes.',
 12: 'Situación: el copetín sortea un premio entre los tickets del día. ¿Puede un programa elegir al azar? ¿Qué cosas no deberían dejarse al azar?',
 13: 'Situación: el programa de caja creció y repite el mismo cálculo en varios lugares. ¿Cómo se reparte un trabajo grande en partes?',
 14: 'Situación: un módulo aplica un descuento, ¿debe cambiar la variable original o no? Y: ¿cómo se separa la categoría de un código como «MIX-01»?',
 15: 'Situación: al apagar la computadora del copetín, el total del día desaparece. ¿Dónde tiene que guardarse para sobrevivir?',
 16: 'Situación: guardar el cierre de cada día y, el viernes, sumar todos los cierres. ¿Qué pasos hacen falta y en qué orden?',
 17: 'Situación: un corte de luz o un archivo sobrescrito por error. ¿Qué medidas protegen la información del copetín?',
 18: 'Situación: una carpeta con cien archivos sin orden. ¿Cuánto se tarda en encontrar el cierre de un día de julio? Se propone organizar.',
 19: 'Situación: el dueño quiere ver solo los productos que hay que reponer, sin perder los demás. ¿Filtrar es lo mismo que borrar?',
 20: 'Situación: el dueño pregunta cuántos productos hay por categoría y cuánto dinero hay en stock. ¿Alcanza con un filtro?',
 21: 'Situación: un informe que muestre a la vez categoría y nivel de stock. ¿Cómo se resume una tabla en dos dimensiones?',
}

CRITERIOS_U = {
 1: ['Escribe algoritmos con la sintaxis y la sangría trabajadas en clase.', 'Verifica el resultado con una prueba de escritorio o un cálculo anticipado.'],
 2: ['Usa índices, recorridos y módulos de forma correcta y sin salirse de rango.', 'Comprueba los resultados con un control (prueba de escritorio, total por dos caminos, invariante).'],
 3: ['Respeta la secuencia de operaciones con archivos y nombra modos y rutas con precisión.', 'Cuida la información: no modifica ni borra archivos fuera de lo pedido.'],
 4: ['Anticipa el resultado de cada filtro o consulta antes de ejecutarlo.', 'Distingue filtrar de borrar y verifica cada resultado con un control.'],
}

ALT = {'PSeInt': ' Alternativa sin equipamiento disponible: el algoritmo se escribe y se prueba en papel con prueba de escritorio, y se ejecuta en la primera sesión de laboratorio disponible.',
       'Access': ' Alternativa sin equipamiento disponible: las consultas se diseñan en papel (campos, criterios y resultado anticipado) sobre la tabla impresa y se ejecutan en la primera sesión de laboratorio disponible.',
       'Explorador': ' Alternativa sin equipamiento disponible: el árbol, las rutas y las operaciones se resuelven en papel y se verifican en la primera sesión con equipo disponible.'}


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
        des.append('Práctica %d del libro, «%s» (%s): Actividad 1, «%s», y Actividad 2, «%s».' % (n, p['titulo'], p['entorno'], p['acts'][0]['titulo'], p['acts'][1]['titulo']))
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
    rec += _alt(p['entorno'])
    f = C[n]['ficha']
    proc, inst = PROC_INST[n]
    crit = CRITERIOS_U[UNIDAD_DE[n]] + ['Cumple los puntos de control de la Práctica %d sin ayuda externa.' % n]
    return dict(idx=idx, tipo='C', n=n, titulo=C[n]['titulo'], tema=f['tema'], capacidad=f['capacidad'], indicadores=f['indicadores'],
                unidad='UNIDAD %d — %s' % (UNIDAD_DE[n], U[UNIDAD_DE[n]]), material='Libro del estudiante · Clase %d y Práctica %d' % (n, n),
                momentos={'Inicio': ini, 'Desarrollo': des, 'Cierre': cie}, tiempos=(40, 90, 30), recursos=rec, proc=proc, inst=inst, criterios=crit)


# procedimientos e instrumentos propios de cada continuación (únicos en todo el Plan Anual)
CONT_EVAL = {
 7: ('Resolución de la carga con centinela y del control con contador y bandera; transferencia a la cantina con revisión entre pares.', 'Programas TicketsDelTurno y ControlSemana ejecutados, con su prueba de escritorio y la versión corregida tras la revisión.'),
 10: ('Recorrido por columnas, detección del día de más unidades y facturación con vector paralelo; transferencia a una matriz de 2 × 3.', 'Programa MatrizVentas con control de totales por dos caminos, revisado por otro equipo.'),
 14: ('Extracción de partes de un código con Subcadena, comparación de cadenas normalizadas y validación de formato con revisión entre pares.', 'Tabla de anticipación de comparaciones de cadenas y condición de validación de códigos, con justificación escrita.'),
 15: ('Clasificación de archivos por tipo de contenido y forma de acceso, y diseño del formato del archivo de ventas.', 'Tabla de clasificación de cinco archivos y archivo de ventas abierto en una planilla, revisados con lista de cotejo.'),
 16: ('Prueba de escritorio de una lectura con FinDeArchivo y operaciones de administración en el Explorador.', 'Tabla de traza de stock.txt y registro de las operaciones copiar, renombrar, mover, eliminar y restaurar.'),
 17: ('Diseño y ejecución de un plan de respaldo con recuperación simulada y cálculo de accesos con buffer.', 'Plan de respaldo de cinco líneas con evidencia de recuperación y resolución de los casos de acceso y buffer.'),
 18: ('Escritura y comprobación de rutas absolutas y relativas y búsqueda con comodines anticipando resultados.', 'Tabla de rutas verificadas en la barra de direcciones y registro de búsquedas anticipadas contra obtenidas.'),
 19: ('Carga de registros con control de clave principal y aplicación de tres filtros con anticipación del resultado.', 'Tabla Articulos con 8 registros verificados y hoja de anticipación de filtros contra resultado.'),
 20: ('Construcción de consultas paramétricas y de totales con campo calculado, y control de sumas por categoría.', 'Cuatro consultas guardadas en Arandu.accdb con su control cruzado (8 artículos y stock total).'),
 21: ('Construcción de la consulta de origen con SiInm y de la referencia cruzada con el asistente, e informe de reposición.', 'Grilla de papel contrastada con la consulta Cruce_nivel e informe breve de reposición.'),
}


def plan_continuacion(idx, n):
    p = practicas.PR[n]
    acts = p['acts'][1:]
    ev = EVAL_UNIDAD_EN.get(('P', n))
    ini = ['Recuperación del punto de control de la Actividad 1 de la Práctica %d y organización de los puestos o de las parejas de trabajo.' % n,
           'Presentación del objetivo de la Actividad 2: %s' % acts[0]['objetivo']]
    des = []
    for k, a in enumerate(acts, 2):
        des.append('Actividad %d, «%s»: %s Acompañamiento docente en el paso que suele traer más dificultad: %s' % (k, a['titulo'], a['objetivo'], a['pasos'][0][0].lower() + a['pasos'][0][1:]))
    if p.get('transfer'):
        des.append('Transferencia y revisión entre pares (30 a 40 minutos): mini-caso «%s» con datos diferentes; intercambio con otro equipo, detección de al menos un error o mejora, corrección y justificación escrita de la versión final.' % p['transfer']['caso'][0])
    des.append('Desafío final para quienes terminan antes: %s' % p['desafio'])
    cie = ['Verificación de los puntos de control: %s.' % '; '.join(['Actividad %d, «%s»' % (k, a['control']) for k, a in enumerate(acts, 2)] + (['transferencia entre pares, «%s»' % p['transfer']['control']] if p.get('transfer') else [])),
           'Registro breve de dificultades y corrección colectiva de los errores frecuentes de la práctica.']
    tiempos = (20, 120, 20)
    if ev:
        cie.append('Aplicación de la evaluación de la Unidad %s, fotocopiable, en su hoja propia del libro.' % ev[1])
        tiempos = (20, 100, 40)
    rec = 'Libro del estudiante, Práctica %d (Actividades %s%s y desafío final) · %s' % (n, _y(list(range(2, len(p['acts']) + 1))), ', transferencia' if p.get('transfer') else '', p['entorno'])
    if p.get('datos'):
        rec += ' · datos para cargar de la práctica'
    rec += ' · pizarra y marcadores.' + _alt(p['entorno'])
    f = C[n]['ficha']
    proc, inst = CONT_EVAL[n]
    if ev:
        inst = inst.rstrip('.') + '. Evaluación de la Unidad %s (fotocopiable).' % ev[1]
    crit = ['Cumple el punto de control de cada actividad sin ayuda externa.', 'Justifica sus decisiones con los conceptos de la Clase %d.' % n,
            'Corrige sus errores a partir de la verificación y deja el trabajo documentado.']
    return dict(idx=idx, tipo='P', n=n, titulo='Continuación práctica de la Clase %d: %s' % (n, p['titulo']), tema=f['tema'], capacidad=f['capacidad'],
                indicadores=f['indicadores'], unidad='UNIDAD %d — %s' % (UNIDAD_DE[n], U[UNIDAD_DE[n]]), material='Libro del estudiante · Práctica %d' % n,
                momentos={'Inicio': ini, 'Desarrollo': des, 'Cierre': cie}, tiempos=tiempos, recursos=rec, proc=proc, inst=inst, criterios=crit)


PFI_IND = ['Diseña una solución de gestión para un emprendimiento integrando algoritmos, datos, archivos y consultas.',
           'Construye y prueba un algoritmo de caja en PSeInt y una base de datos funcional con filtros y consultas.',
           'Integra resultados, organiza la demostración y explica en equipo las decisiones técnicas del proyecto.']
TALLER = {
 1: dict(titulo='Proyecto Final Integrador · Taller 1: definición del emprendimiento',
         ini=['Presentación del Proyecto Final Integrador del libro: competencia integradora, requisitos mínimos, extensión recomendada y rúbrica.', 'Formación de equipos de 3 o 4 integrantes y reparto inicial de roles (algoritmo, base de datos, informe, presentación).'],
         des=['Elección del emprendimiento y listado de sus productos, precios y categorías (datos propios, no los del libro).', 'Definición de lo que va a resolver el sistema: el cálculo de caja, el descuento y las preguntas que deben responder las consultas.', 'Dibujo del flujograma del algoritmo de caja a partir de la Figura PFI.1, adaptado al emprendimiento.', 'Redacción de tres casos de prueba del algoritmo con su resultado anticipado.'],
         cie=['Presentación breve de cada equipo: emprendimiento, roles y casos de prueba.', 'Registro de avances en la carpeta del proyecto y tareas para el Taller 2.'],
         proc='Definición del emprendimiento, de sus datos y de los casos de prueba, con reparto de roles.',
         inst='Carpeta del proyecto (Taller 1): emprendimiento, productos, flujograma y tres casos de prueba, revisada con lista de cotejo.'),
 2: dict(titulo='Proyecto Final Integrador · Taller 2: construcción del sistema',
         ini=['Revisión de la carpeta del Taller 1 y de los casos de prueba.', 'Organización del trabajo por roles en los puestos del laboratorio.'],
         des=['Programación del algoritmo de caja en PSeInt con ciclo de carga, al menos un módulo y la decisión del descuento; ejecución de los tres casos de prueba.', 'Programación del vector de ventas de una semana (total y promedio) y del ranking ordenado de productos.', 'Creación de la base en Access: tabla de productos con tipos y clave principal, carga de datos propios y consultas mínimas (reposición, selección, totales por categoría y referencias cruzadas).', 'Extensión recomendada, si el tiempo alcanza: tabla Ventas y ticket guardado en un archivo de texto organizado en carpetas.'],
         cie=['Verificación cruzada de un resultado del algoritmo y de una consulta.', 'Registro de avances y de pendientes para el Taller 3.'],
         proc='Construcción y prueba del algoritmo de caja, del ranking y de la base con sus consultas mínimas.',
         inst='Archivos .psc y .accdb del equipo con sus casos de prueba ejecutados y las cuatro consultas mínimas guardadas.'),
 3: dict(titulo='Proyecto Final Integrador · Taller 3: integración y ensayo para la feria',
         ini=['Revisión de pendientes del Taller 2 y del estado de los aportes de las otras materias.', 'Lectura de la rúbrica analítica del Proyecto Final Integrador.'],
         des=['Control cruzado de los resultados (por ejemplo, total de la semana por el vector y a mano; conteo de la referencia cruzada igual a la cantidad de productos) y corrección de errores.', 'Integración de los aportes de Matemática Aplicada, Gabinete de Software, Gabinete de Laboratorio y Dibujo Técnico en el afiche y la presentación.', 'Ensayo de la demostración de cinco minutos con guion y reparto de roles.', 'Coevaluación entre equipos con la rúbrica analítica.'],
         cie=['Devolución docente y de pares sobre el ensayo.', 'Lista final de ajustes para la Feria de Informática.'],
         proc='Integración de aportes, control cruzado de resultados y ensayo de la demostración con coevaluación.',
         inst='Rúbrica analítica del Proyecto Final Integrador (30/25/20/15/10) aplicada en coevaluación y por el docente.'),
}


def plan_taller(idx, k):
    t = TALLER[k]
    return dict(idx=idx, tipo='T', n=k, titulo=t['titulo'], tema='Proyecto Final Integrador — El sistema de gestión de un emprendimiento',
                capacidad=ediciones.caps(ediciones.CAP_TALLER), indicadores=PFI_IND, unidad='PROYECTO FINAL INTEGRADOR — Feria de Informática',
                material='Libro del estudiante · Proyecto Final Integrador · Solucionario docente (rúbrica)',
                momentos={'Inicio': t['ini'], 'Desarrollo': t['des'], 'Cierre': t['cie']}, tiempos=(20, 120, 20),
                recursos='Libro del estudiante, Proyecto Final Integrador (requisitos, extensión recomendada, etapas, aportes de cada materia y Figuras PFI.1 y PFI.2) · computadoras con PSeInt y Microsoft Access · carpeta del proyecto · rúbrica del Solucionario docente.' + ALT['PSeInt'],
                proc=t['proc'], inst=t['inst'],
                criterios=['Cumple los requisitos mínimos del proyecto previstos para el taller.', 'Verifica cada resultado por un segundo camino.', 'Participa en su rol y registra el avance en la carpeta del equipo.'])


EV_IND = {'E1': ['Resuelve problemas de decisión y repetición con estructuras de control y verifica el resultado.', 'Opera con vectores y matrices: carga, recorrido, totales, máximo y ordenamiento.', 'Define e invoca funciones con parámetros para resolver un cálculo del caso.'],
          'E2': ['Resuelve con vectores, ordenamiento y funciones un problema de datos de stock.', 'Expresa en la notación del libro el guardado de datos en un archivo.', 'Formula filtros, consultas de totales y campos calculados y verifica que sus resultados coincidan por dos caminos.']}


def plan_eval(idx, eid):
    e = [x for x in evaluaciones.EV if x['id'] == eid][0]
    etapa = '1.ª etapa (Unidades 1 y 2)' if eid == 'E1' else '2.ª etapa (Unidades 1 a 4)'
    des = ['Lectura de los datos de la evaluación («%s») y aclaración de dudas de consigna, sin resolver.' % e['base'][0].split(' — ')[1],
           'Resolución individual de la Parte A, de diagnóstico rápido: tres consignas de opción múltiple.',
           'Resolución individual de la Parte B, de resolución y aplicación: seis consignas con datos propios de la evaluación (%s).' % ('Si… Sino con precio mayorista, vector de copias, máximo y promedio, matriz por tipo y turno, burbuja optimizada y función de importe' if eid == 'E1' else 'vector de stock con contador, ordenamiento por selección, función ValorStock, guardado en archivo, filtro y totales por categoría, y campo calculado con decisión')]
    return dict(idx=idx, tipo='E', n=eid, titulo='Evaluación integradora de la %s' % etapa, tema='Evaluación integradora de la %s' % etapa,
                capacidad=ediciones.caps(ediciones.CAP_EVAL[eid]), indicadores=EV_IND[eid],
                unidad='Evaluación integradora · %s' % ('cierre de la 1.ª etapa (junio)' if eid == 'E1' else 'cierre de la 2.ª etapa (noviembre)'),
                material='Libro del estudiante · evaluación integradora fotocopiable en hoja propia',
                momentos={'Inicio': ['Organización del aula para el trabajo individual y lectura de las pautas de la prueba (tiempo, materiales permitidos, puntaje).'],
                          'Desarrollo': des,
                          'Cierre': ['Entrega de la prueba y revisión de que todas las consignas tengan respuesta.', 'Anuncio de la fecha de devolución y de la corrección colectiva.']},
                tiempos=(15, 130, 15),
                recursos='Evaluación integradora fotocopiable del libro (hoja propia) · clave del Solucionario docente · lápiz, goma y calculadora.',
                proc='Resolución individual de la prueba integradora de la %s.' % etapa,
                inst='Prueba integradora fotocopiable de la %s: 3 ítems de opción múltiple y 6 de resolución, con clave y puntaje sugerido (21 puntos).' % etapa,
                criterios=['Resuelve cada consigna con el procedimiento pedido.', 'Muestra los cálculos o la traza que respaldan cada resultado.', 'Expresa las respuestas con precisión y con la notación del libro.'])


def planes():
    out = []
    for idx, (t, n) in enumerate(ORDEN, 1):
        out.append({'C': plan_clase, 'P': plan_continuacion, 'T': plan_taller, 'E': plan_eval}[t](idx, n))
    for p in out:
        assert sum(p['tiempos']) == 160, (p['idx'], p['tiempos'])
    assert len({p['proc'] for p in out}) == 36 and len({p['inst'] for p in out}) == 36
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

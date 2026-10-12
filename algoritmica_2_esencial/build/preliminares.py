# -*- coding: utf-8 -*-
"""Preliminares del libro de Algorítmica 2.º (presentación, uso, prueba diagnóstica, aperturas de unidad)
y Proyecto Final Integrador con su rúbrica (mismos criterios y pesos del paquete vigente: 30/25/20/15/10)."""

PRESENTACION = [
 'Este libro acompaña el segundo año de Algorítmica del Bachillerato Técnico en Servicios, Especialidad Informática, conforme al programa oficial del Ministerio de Educación y Ciencias. Reúne en un solo volumen las 21 clases del año y sus 21 prácticas: ya no hace falta un cuaderno aparte.',
 'Vas a aprender a resolver problemas con algoritmos y a escribirlos en pseudocódigo para ejecutarlos en PSeInt: decisiones, ciclos, vectores, matrices, ordenamiento, módulos y cadenas. Después vas a conocer cómo se guardan los datos en archivos y cómo los organiza el sistema operativo, y vas a terminar consultando una base de datos en Microsoft Access.',
 'Cada clase abre con una ficha de capacidad e indicadores, desarrolla el tema con ejemplos resueltos, tablas y figuras, y cierra con actividades para ejercitar, resolver y decidir. Enseguida viene la Práctica con el mismo número: se hace en PSeInt, en el Explorador de archivos o en Access, con datos nuevos, pasos guiados y puntos de control para que verifiques tu trabajo.',
 'El caso que nos acompaña en las clases es el Copetín Karumbé, un emprendimiento gastronómico paraguayo. En las prácticas trabajás con la Librería escolar Arandu, y en las evaluaciones aparecen una heladería y una fotocopiadora: los mismos algoritmos sirven para negocios distintos. El año termina con el Proyecto Final Integrador para la Feria de Informática.',
]
COMO_USAR = [
 ('Clase N', 'Ficha con la capacidad del programa oficial e indicadores · desarrollo con ejemplos resueltos · recuadros Concepto clave, Ejemplo, Errores frecuentes y, cuando corresponde, En Paraguay, Ejemplo cotidiano o Aplicación profesional · actividades de aplicación.'),
 ('Práctica N', 'Empieza en página propia y se puede fotocopiar suelta: competencia, lo que necesitás saber, actividades con objetivo, modelo, pasos y punto de control, y un desafío final. Algunas suman una transferencia con revisión entre pares.'),
 ('Punto de control', 'Te dice cómo comprobar tu trabajo, sin darte la respuesta: si no se cumple, revisá tus pasos antes de seguir.'),
 ('Evaluaciones', 'Al cierre de cada unidad (banda ámbar) y de cada etapa (banda azul), en páginas propias.'),
]

DIAGNOSTICA_INTRO = 'Esta prueba no lleva nota: sirve para que tu docente conozca tu punto de partida antes de comenzar el año. Respondé con lo que sabés, sin ayuda.'
DIAGNOSTICA = [
 ('Ordená los pasos para cobrar una venta en un copetín, numerándolos del 1 al 4: (a) entregar el vuelto · (b) recibir el pago · (c) calcular el total · (d) anotar los productos pedidos.', 'd, c, b, a: anotar los productos → calcular el total → recibir el pago → entregar el vuelto.'),
 ('Calculá el importe de una venta de 3 empanadas a G. 5.000 cada una.', '3 × 5.000 = 15.000.'),
 ('Sobre una compra de G. 60.000 se aplica un descuento del 10 %. Calculá el descuento y el monto final a pagar.', 'Descuento 6.000; monto final 54.000. Si muchos fallan, reforzar porcentajes antes de las Clases 2 y 3.'),
 ('Marcá cuáles de estos datos son números y cuáles son texto: 42 · «chipa» · 12,5 · «K».', 'Números: 42 y 12,5. Texto: «chipa» y «K».'),
 ('V o F: una computadora ejecuta las instrucciones exactamente en el orden en que se le dan.', 'Verdadero (salvo que una estructura de control indique otro camino, idea que se trabaja en la Unidad 1).'),
 ('Escribí, en tus palabras y en orden, los pasos que seguís para preparar tu mochila antes de ir al colegio (mínimo 4 pasos).', 'Respuesta abierta: se valora el orden, que cada paso sea una acción concreta y que la secuencia termine.'),
]

UNIDADES = {
 1: 'En esta unidad vas a pasar del problema al programa: planificar antes de escribir, elegir los tipos de datos y usar las tres estructuras de control —secuencia, decisión y repetición— hasta escribir y ejecutar algoritmos completos en PSeInt.',
 2: 'En esta unidad vas a guardar muchos datos juntos en vectores y matrices, a recorrerlos, buscarlos y ordenarlos, y a dividir los programas en módulos con parámetros, incluido el trabajo con cadenas de texto.',
 3: 'En esta unidad vas a ver dónde viven los datos cuando el programa termina: qué es un archivo, qué operaciones se hacen con él, cómo se protege y cómo lo organiza el sistema operativo en carpetas.',
 4: 'En esta unidad vas a consultar una base de datos en Microsoft Access: filtrar, seleccionar con criterios y parámetros, calcular totales y campos, y resumir en una referencia cruzada para tomar decisiones.',
}

PFI_INTRO = [
 'Durante todo el año trabajaste sobre un emprendimiento paraguayo: el Copetín Karumbé. Ahora, en equipo, vas a construir el sistema de gestión de un emprendimiento —el copetín u otro que elija tu grupo— y presentarlo en la Feria de Informática de fin de año.',
 'El proyecto reúne todo lo que aprendiste en Algorítmica (algoritmos, estructuras de datos, archivos y bases de datos) y se conecta con las demás materias prácticas de Informática: cada una aporta su parte para un mismo producto.',
]
PFI_COMPETENCIA = 'Diseñar y presentar, en equipo, un sistema de gestión sencillo para un emprendimiento, aplicando algoritmos, una base de datos y las herramientas de las demás asignaturas prácticas.'
PFI_APORTES = ['Un algoritmo de caja en PSeInt que lea los productos y cantidades de una venta, calcule el total, aplique el descuento del emprendimiento cuando corresponda y muestre el ticket, con condicionales, ciclos y al menos un módulo.',
               'Una base de datos en Access con la tabla de productos del emprendimiento y sus consultas.',
               'Un informe de resultados: el ranking de los productos más vendidos (ordenación) y el total y el promedio de una semana de ventas (vector y acumulador).']
PFI_FIG_LEAD = 'Este es el flujograma del algoritmo de caja que tu equipo va a programar en PSeInt. Fijate cómo reúne todo lo del año: un ciclo de carga, un módulo, una decisión y el ticket final.'
PFI_FIG_EPI = 'Figura PFI.1 — Flujograma del algoritmo de caja del proyecto: ciclo de carga, módulo CalcularTotal, descuento del 10 % cuando el total llega a 50.000 y ticket final.'
PFI_FIG2_LEAD = 'Y esta es la base de datos del proyecto en Access, en su versión ampliada: la tabla Productos y, como extensión recomendada, una tabla Ventas conectada por el campo Código.'
PFI_FIG2_EPI = 'Figura PFI.2 — Las dos tablas de la versión ampliada del proyecto: Productos (1) y Ventas (N), conectadas por el campo Código.'
PFI_REQUISITOS = [
 ('Algoritmo de caja', 'Programa en PSeInt que corre sin errores: carga de varios productos con un ciclo, al menos un módulo (función o procedimiento), decisión del descuento y ticket final. Probado con al menos tres casos anotados antes de ejecutar.'),
 ('Estructuras de datos', 'Un vector con las ventas de una semana (total y promedio) y un ranking de productos ordenado con burbuja o selección.'),
 ('Base de datos', 'Tabla de productos en Access con tipos de datos y clave principal, y datos propios del emprendimiento (no los del libro).'),
 ('Consultas', 'Al menos cuatro: un filtro o consulta de productos a reponer, una de selección con criterio, una de totales por categoría y una de referencias cruzadas.'),
 ('Presentación', 'Afiche o presentación del emprendimiento y guion de una demostración de cinco minutos.'),
]
PFI_EXTENSION = 'Extensión recomendada: agregá una tabla Ventas relacionada con Productos y guardá el ticket de cada venta en un archivo de texto organizado en carpetas. No son requisitos mínimos para aprobar el proyecto, pero acercan la solución a un sistema de gestión real.'
PFI_ETAPAS = [
 ('Taller 1 — Definición', 'Elegís el emprendimiento en equipo, listás sus productos y precios, decidís qué va a resolver el sistema y repartís los roles.'),
 ('Taller 2 — Construcción', 'Programás y probás el algoritmo de caja en PSeInt y creás la base de datos en Access con sus consultas.'),
 ('Taller 3 — Integración y ensayo', 'Sumás los aportes de las otras materias, verificás cada resultado por otro camino y ensayás la demostración para la feria.'),
]
PFI_INTERDISCIPLINA = [
 ('Algorítmica', 'El algoritmo de caja, las estructuras de datos y la base de datos con sus consultas.'),
 ('Matemática Aplicada a la Informática', 'Los cálculos y la estadística: porcentajes, promedios y los gráficos de las ventas.'),
 ('Gabinete de Software', 'El informe, la planilla con gráficos y la presentación para el stand.'),
 ('Gabinete de Laboratorio / Hardware', 'La preparación del equipo del stand, las conexiones y el resguardo de los archivos del proyecto.'),
 ('Dibujo Técnico', 'El diagrama de flujo del sistema, el logo del emprendimiento y el plano del stand.'),
]
PFI_ENTREGABLES = ['El sistema funcionando: el algoritmo en PSeInt (.psc) y la base de datos en Access (.accdb) con sus consultas guardadas.',
                   'La carpeta del proyecto con los casos de prueba del algoritmo, el informe de resultados y el reparto de roles.',
                   'Un afiche o una presentación que explique el emprendimiento y qué hace el sistema, y la demostración en vivo en el stand.']
PFI_PAUTAS = ['Trabajen en equipos de 3 o 4 integrantes, con roles claros (algoritmo, base de datos, informe, presentación).',
              'Usen el mismo emprendimiento en todas las materias.',
              'Anoten el resultado esperado de cada prueba antes de ejecutar y verifiquen cada consulta por otro camino.',
              'Sean claros y honestos en la presentación: qué resuelve el sistema y qué quedó pendiente.']

RUBRICA = [('Funcionamiento del sistema', '30 %'),
           ('Aplicación de los contenidos del año', '25 %'),
           ('Integración interdisciplinaria', '20 %'),
           ('Presentación en la feria', '15 %'),
           ('Trabajo en equipo', '10 %')]
ORIENTACIONES_PFI = ['Lanzar el proyecto al terminar la Unidad 4 y trabajarlo en los tres talleres del Plan Anual, antes de la evaluación integradora de la 2.ª etapa.',
                     'Formar equipos de 3 o 4 integrantes con roles definidos y rotativos en los ensayos.',
                     'Coordinar con las otras materias del curso para que todas trabajen sobre el mismo emprendimiento.',
                     'Pedir datos de prueba propios del equipo: no se aceptan las tablas del Copetín ni de la Librería Arandu copiadas del libro.',
                     'Exigir un control cruzado por resultado (por ejemplo, total de la semana por el vector y por la suma a mano; conteo de la referencia cruzada igual a la cantidad de productos).']

# Rúbrica analítica: mismos cinco criterios y pesos; el nivel asigna 100 %, 60 %, 30 % o 0 % del peso.
NIVELES = [('Logrado', 1.0), ('En proceso', 0.6), ('Inicial', 0.3), ('No presentado', 0.0)]
RUBRICA_ANALITICA = [
 ('Funcionamiento del sistema', 30, [
   'El algoritmo de caja corre sin errores con los tres casos de prueba anotados y la base de datos abre con su tabla y las cuatro consultas mínimas, cuyos resultados se verificaron por otro camino.',
   'El algoritmo corre, pero falla en un caso de prueba (por ejemplo, el límite del descuento), o una de las consultas da error o un resultado sin verificar.',
   'El algoritmo tiene errores de ejecución o la base tiene la tabla pero funcionan menos de dos consultas.',
   'No se entrega el algoritmo ni la base, o los archivos no abren.']),
 ('Aplicación de los contenidos del año', 25, [
   'Se usan correctamente condicionales, ciclos, al menos un módulo con parámetros, un vector con total y promedio, un ordenamiento para el ranking y consultas de selección, totales y referencias cruzadas.',
   'Están casi todos los contenidos, con uno o dos usos incorrectos (un acumulador mal inicializado, un ranking con nombres desfasados, un criterio mal escrito).',
   'Faltan varios contenidos centrales (no hay módulo, no hay vector u ordenamiento, o no hay consultas de totales).',
   'No se aplican los contenidos del año.']),
 ('Integración interdisciplinaria', 20, [
   'El proyecto suma aportes reales de las demás materias prácticas sobre el mismo emprendimiento y la presentación muestra cómo se conectan con el sistema.',
   'El emprendimiento es el mismo, pero falta el aporte de una materia o no se lo vincula con el sistema.',
   'Los aportes de las otras materias se presentan por separado, sin relación con el sistema.',
   'No hay aportes de otras materias.']),
 ('Presentación en la feria', 15, [
   'El stand, el afiche y la demostración son claros; en unos cinco minutos se muestra el sistema funcionando y se explica qué problema del emprendimiento resuelve.',
   'La demostración funciona, pero excede el tiempo o explica la parte técnica sin decir para qué le sirve al emprendimiento.',
   'La demostración se interrumpe por errores o se limita a leer el afiche sin mostrar el sistema funcionando.',
   'El equipo no presenta.']),
 ('Trabajo en equipo', 10, [
   'Todos participan, los roles se cumplen y cada integrante puede explicar su parte y la de otro compañero; la carpeta registra el reparto de tareas.',
   'Los roles se cumplen de forma despareja o algún integrante solo puede explicar su propia parte.',
   'Uno o dos integrantes concentran el trabajo y no hay registro del reparto de tareas.',
   'No hay evidencia de trabajo compartido.']),
]
assert [(c, p) for c, p, _ in RUBRICA_ANALITICA] == [(c, int(p.split()[0])) for c, p in RUBRICA]
assert sum(p for _, p, _ in RUBRICA_ANALITICA) == 100

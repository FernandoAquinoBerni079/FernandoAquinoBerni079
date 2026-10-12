# -*- coding: utf-8 -*-
"""Textos preliminares de la Edición Esencial de Algorítmica 1.º: presentación, cómo usar el libro,
prueba diagnóstica (la del tomo vigente, con sus orientaciones), introducciones de unidad y Proyecto Final
Integrador (el del cuaderno vigente, con rúbrica analítica de los mismos criterios y pesos)."""

PRESENTACION = [
 'Este libro acompaña el primer año de Algorítmica del Bachillerato Técnico en Servicios, Especialidad Informática, conforme al programa oficial del Ministerio de Educación y Ciencias. Reúne en un solo volumen las 21 clases del año y sus 21 prácticas: ya no hace falta un cuaderno aparte.',
 'Sus tres unidades —Teoría de Conjuntos, Lógica Simbólica e Introducción a la Algoritmia— construyen, en ese orden, el pensamiento que sostiene toda la programación: agrupar con precisión, razonar sin ambigüedad y ordenar soluciones en pasos exactos.',
 'Cada clase abre con una ficha de capacidad e indicadores, desarrolla el tema con ejemplos resueltos, tablas y figuras, y cierra con actividades para ejercitar, resolver y decidir. Enseguida viene la Práctica con el mismo número: datos nuevos, pasos guiados y puntos de control para que verifiques tu trabajo.',
 'El caso que nos acompaña es el Copetín Karumbé, el emprendimiento de Ña Rosa: su menú aporta los conjuntos, sus promociones aportan las proposiciones y su caja diaria aporta los algoritmos. Al final del año vas a haber diseñado, con lápiz y papel, la versión 1.0 de su sistema de caja, y vas a dar el primer paso en PSeInt. El año termina con el Proyecto Final Integrador para la Feria de Informática.',
]

COMO_USAR = [
 ('Clase N', 'Ficha con la capacidad del programa oficial e indicadores · desarrollo con ejemplos resueltos · recuadros Concepto clave, Ejemplo, Errores frecuentes y, cuando corresponde, En Paraguay, Ejemplo cotidiano o Aplicación profesional · actividades de aplicación.'),
 ('Práctica N', 'Empieza en página propia y se puede fotocopiar suelta: competencia, lo que necesitás saber, actividades con objetivo, modelo, pasos y punto de control, y un desafío final. Algunas suman una transferencia con revisión entre pares.'),
 ('Punto de control', 'Te dice cómo comprobar tu trabajo, sin darte la respuesta: si no se cumple, revisá tus pasos antes de seguir.'),
 ('Evaluaciones', 'Al cierre de cada unidad (banda ámbar) y de cada etapa (banda azul), en páginas propias.'),
]

DIAGNOSTICA_INTRO = 'Esta prueba no lleva nota: sirve para que vos y tu docente sepan de dónde partís. No hay que estudiar nada: es una foto de tu punto de partida.'
DIAGNOSTICA = [
 ('Escribí entre llaves { } el conjunto formado por las vocales de la palabra «computadora».',
  '{o, u, a}: en un conjunto los elementos no se repiten. Quien escriba {o, u, a, o, a} todavía no distingue conjunto de lista: se retoma en la Clase 1.'),
 ('Estos pasos para preparar tereré están desordenados. Numeralos del 1 al 4: (a) cargar la guampa con yerba · (b) conseguir agua bien fría y hielo · (c) tomar y volver a cargar · (d) verter el agua sobre la yerba.',
  'Orden esperado: b, a, d, c (se acepta a, b, d, c si el razonamiento es secuencial). Detecta la noción intuitiva de secuencia, base de la Unidad 3.'),
 ('Leé: «Si llueve, el partido se suspende. Hoy llueve.» ¿Qué podés concluir con seguridad? Escribilo en una línea.',
  '«El partido se suspende». Es el modus ponens que se formaliza en la Unidad 2; quien concluya otra cosa necesitará más apoyo en Lógica.'),
 ('Clasificá estas seis palabras en dos grupos y poné un nombre a cada grupo: mouse, mango, teclado, guayaba, monitor, piña.',
  'Grupos esperados: partes de la computadora {mouse, teclado, monitor} y frutas {mango, guayaba, piña}. Vale cualquier criterio coherente y explícito: se evalúa la capacidad de clasificar.'),
 ('Calculá: 3 × (8 − 5) + 4 =',
  '3 × 3 + 4 = 13. Quien obtenga otro valor no respeta la jerarquía de operaciones: anotarlo, se necesita para las pruebas de escritorio.'),
 ('¿Qué es para vos un «algoritmo»? Escribí tu idea en una línea, aunque no estés seguro.',
  'Cualquier idea del estilo «pasos para resolver algo» es un buen punto de partida; no se corrige, se recupera en la Unidad 3.'),
]
DIAGNOSTICA_CIERRE = 'Con los resultados, agrupá los errores por consigna (notación, secuencia, lógica, clasificación, jerarquía) y reforzá en las clases correspondientes. No se devuelve con nota ni con correcciones en rojo: es un insumo del docente.'

UNIDADES = {
 1: 'En esta unidad vas a aprender a definir, clasificar, representar y operar con conjuntos. Puede parecer pura matemática, pero es la base del pensamiento que usa toda computadora: agrupar cosas con precisión, sin ambigüedad.',
 2: 'En esta unidad vas a reconocer proposiciones, combinarlas con conectivos, calcular su valor de verdad con tablas y encadenar razonamientos válidos. Todo lo que una computadora «decide» se reduce a las reglas de esta unidad.',
 3: 'En esta unidad vas a diseñar algoritmos: recetas exactas que cualquiera puede seguir sin dudar. Los conjuntos definen los datos y la lógica define las condiciones. Vas a construir, paso a paso, el sistema de caja del Copetín Karumbé.',
}

PFI_TITULO = 'Presentamos nuestro emprendimiento'
PFI_INTRO = [
 'Durante el año conociste el Copetín Karumbé y aprendiste a describir y clasificar información con conjuntos y con lógica, y a dar los primeros pasos en la construcción de algoritmos. Ahora, en equipo, vas a presentar un emprendimiento —el copetín u otro que elija tu grupo— en la Feria de Informática de fin de año.',
 'Es un proyecto interdisciplinario: se arma junto con las demás materias prácticas de Informática, y cada una aporta su parte para un mismo emprendimiento.',
]
PFI_COMPETENCIA = 'Presentar en equipo un emprendimiento y un primer sistema de caja, aplicando lo aprendido en Algorítmica y en las demás materias prácticas del año.'
PFI_APORTES = ['Algoritmo de caja básico en PSeInt: un programa que lea el precio y la cantidad de una venta, calcule el importe total y aplique un descuento simple cuando la venta llegue a cierto monto. Se diseña primero en pseudocódigo y con prueba de escritorio, y después se pasa a PSeInt como en el «Puente a PSeInt» de la Clase 21.',
               'Clasificación de los productos con conjuntos y lógica: agrupá los productos del emprendimiento en conjuntos según su tipo (por ejemplo, salados y dulces), representalos en un diagrama de Venn y escribí reglas del negocio con lógica proposicional (por ejemplo, «es salado Y cuesta menos de 10.000»).']
PFI_FIG_LEAD = 'Este es el diagrama de flujo del algoritmo de caja básico que tu equipo va a programar. Reúne lo de la Unidad 3: lectura de datos, cálculo, una decisión con su caso frontera y la escritura del resultado.'
PFI_FIG_EPI = 'Figura PFI.1 — Diagrama de flujo del algoritmo de caja básico del proyecto: lectura del precio y la cantidad, cálculo del total, descuento del 10 % cuando el total llega a 50.000 y escritura del importe a cobrar.'
PFI_REQUISITOS = [
 ('Algoritmo de caja', 'Pseudocódigo y diagrama de flujo del algoritmo de caja básico, con su prueba de escritorio para tres casos (uno con descuento, uno sin descuento y el caso frontera) anotados antes de ejecutar; el mismo algoritmo, pasado a PSeInt, corre sin errores y da los resultados de la prueba.'),
 ('Conjuntos', 'Los productos del emprendimiento organizados en al menos dos conjuntos, con su diagrama de Venn, una unión, una intersección y los cardinales.'),
 ('Lógica', 'Al menos tres reglas del negocio simbolizadas con conectivos y paréntesis, y la tabla de verdad de una de ellas.'),
 ('Presentación', 'Afiche o folleto del emprendimiento y guion de una demostración de unos cinco minutos.'),
]
PFI_EXTENSION = 'Extensión recomendada: convertí el algoritmo en el sistema de caja completo de la Clase 21 (ciclo con centinela, acumulador de lo cobrado, contadores de ventas y de descuentos, promedio con guarda de división por cero y control cruzado). No son requisitos mínimos para aprobar el proyecto, pero acercan la solución a un sistema de caja real.'
PFI_ETAPAS = [
 ('Etapa 1 — Definición', 'Elegís el emprendimiento en equipo, listás sus productos y precios, los agrupás en conjuntos por tipo y repartís los roles.'),
 ('Etapa 2 — Construcción', 'Diseñás el algoritmo de caja básico con su prueba de escritorio, lo pasás a PSeInt y escribís las reglas del negocio con lógica proposicional.'),
 ('Etapa 3 — Integración y ensayo', 'Sumás los aportes de las otras materias, verificás cada resultado por otro camino y ensayás la demostración para la feria.'),
]
PFI_INTERDISCIPLINA = [
 ('Algorítmica', 'El algoritmo de caja básico y la clasificación de los productos con conjuntos y lógica.'),
 ('Matemática Aplicada a la Informática', 'Los precios, los porcentajes (descuentos, IVA) y el presupuesto del emprendimiento.'),
 ('Gabinete de Software', 'El folleto o afiche en Word, la planilla de precios en Excel y la presentación para el stand.'),
 ('Gabinete de Laboratorio', 'La preparación de la PC, la estructura de carpetas y el guardado de los archivos del proyecto.'),
 ('Dibujo Técnico', 'El logo del emprendimiento, el afiche y el plano del stand a escala.'),
]
PFI_ENTREGABLES = ['El emprendimiento presentado, con su nombre, sus productos y sus precios.',
                   'La carpeta del proyecto: pseudocódigo, diagrama de flujo y prueba de escritorio del algoritmo; los conjuntos con su diagrama de Venn y las reglas lógicas con su tabla.',
                   'El algoritmo de caja básico funcionando en PSeInt (.psc), el material de difusión (afiche o folleto) y la demostración en vivo en el stand.']
PFI_PAUTAS = ['Trabajen en equipos de 3 o 4 integrantes, con roles claros (algoritmo, conjuntos y lógica, material de difusión, presentación).',
              'Usen el mismo emprendimiento en todas las materias.',
              'Anoten el resultado esperado de cada prueba antes de ejecutar y verifiquen cada resultado por otro camino.',
              'Sean claros y honestos en la presentación: qué resuelve el algoritmo y qué quedó pendiente.']

RUBRICA = [('Funcionamiento del algoritmo', '30 %'),
           ('Aplicación de los contenidos del año', '25 %'),
           ('Integración interdisciplinaria', '20 %'),
           ('Presentación en la feria', '15 %'),
           ('Trabajo en equipo', '10 %')]
ORIENTACIONES_PFI = ['Lanzar el proyecto al inicio de la 2.ª etapa y acompañarlo en paralelo a la Unidad 3: la definición, en la segunda jornada de la Clase 17; la construcción, en las segundas jornadas de las Clases 19 y 20; la integración y el ensayo, en la segunda jornada de la Clase 21, después del Puente a PSeInt.',
                     'Formar equipos de 3 o 4 integrantes con roles definidos (algoritmo, clasificación, material de difusión, presentación).',
                     'Coordinar con los docentes de las otras materias prácticas para que todas apunten al mismo emprendimiento: así el proyecto es interdisciplinario de verdad y no una suma de trabajos sueltos.',
                     'Pedir datos propios del equipo: no se aceptan los precios del Copetín Karumbé copiados del libro.',
                     'Como es 1.er curso, valorar sobre todo que el algoritmo básico funcione y que el equipo entienda y explique lo que hizo.']

# Rúbrica analítica: mismos cinco criterios y pesos del solucionario vigente; el nivel asigna 100 %, 60 %, 30 % o 0 % del peso.
NIVELES = [('Logrado', 1.0), ('En proceso', 0.6), ('Inicial', 0.3), ('No presentado', 0.0)]
RUBRICA_ANALITICA = [
 ('Funcionamiento del algoritmo', 30, [
   'El algoritmo corre en PSeInt sin errores y calcula bien el total y el descuento en los tres casos de prueba anotados, incluido el caso frontera; la prueba de escritorio coincide con la ejecución.',
   'El algoritmo corre, pero falla en un caso (por lo general, la frontera del descuento) o la prueba de escritorio no coincide en algún valor.',
   'El algoritmo está escrito pero no corre en PSeInt, o corre con errores de cálculo en más de un caso.',
   'No se entrega el algoritmo o el archivo no abre.']),
 ('Aplicación de los contenidos del año', 25, [
   'Se usan correctamente conjuntos (con Venn, unión, intersección y cardinales), reglas lógicas simbolizadas con su tabla de verdad, y un algoritmo con lectura, cálculo y decisión con diagrama de flujo.',
   'Están los tres bloques del año, con uno o dos usos incorrectos (un cardinal mal contado, una regla sin paréntesis, un símbolo del diagrama equivocado).',
   'Falta uno de los tres bloques (conjuntos, lógica o algoritmo).',
   'No se aplican los contenidos del año.']),
 ('Integración interdisciplinaria', 20, [
   'El proyecto suma aportes reales de las demás materias prácticas sobre el mismo emprendimiento y la presentación muestra cómo se conectan con el algoritmo.',
   'El emprendimiento es el mismo, pero falta el aporte de una materia o no se lo vincula con el algoritmo.',
   'Los aportes de las otras materias se presentan por separado, sin relación con el emprendimiento.',
   'No hay aportes de otras materias.']),
 ('Presentación en la feria', 15, [
   'El stand, el afiche y la demostración son claros; en unos cinco minutos se muestra el algoritmo funcionando y se entiende el emprendimiento.',
   'La demostración funciona, pero excede el tiempo o explica la parte técnica sin decir para qué le sirve al emprendimiento.',
   'La demostración se interrumpe por errores o se limita a leer el afiche sin mostrar el algoritmo.',
   'El equipo no presenta.']),
 ('Trabajo en equipo', 10, [
   'Todos participan, los roles se cumplen y cada integrante puede explicar su parte; la carpeta registra el reparto de tareas.',
   'Los roles se cumplen de forma despareja o algún integrante no puede explicar su parte.',
   'Uno o dos integrantes concentran el trabajo y no hay registro del reparto de tareas.',
   'No hay evidencia de trabajo compartido.']),
]
assert [(c, p) for c, p, _ in RUBRICA_ANALITICA] == [(c, int(p.split()[0])) for c, p in RUBRICA]
assert sum(p for _, p, _ in RUBRICA_ANALITICA) == 100

# -*- coding: utf-8 -*-
"""Presentación, cómo usar el libro, prueba diagnóstica, aperturas de unidad y Proyecto Final Integrador."""

PRESENTACION = [
 'Este libro cierra la serie de Algorítmica del Bachillerato Técnico en Servicios, Especialidad Informática, conforme al programa oficial del Ministerio de Educación y Ciencias. Reúne en un solo volumen las 21 clases del año y sus 21 prácticas: ya no hace falta un cuaderno aparte.',
 'Vas a recorrer dos grandes temas. Primero, los lenguajes de programación: qué son, cómo se traducen, qué paradigmas existen y cómo se elige uno. Después, las bases de datos: qué resuelven, cómo se diseñan con el modelo Entidad-Relación, cómo se normalizan y cómo se crean y consultan en Microsoft Access.',
 'Cada clase abre con una ficha de capacidad e indicadores, desarrolla el tema con ejemplos resueltos, tablas y figuras, y cierra con actividades para ejercitar, resolver y decidir. Enseguida viene la Práctica con el mismo número: se hace en PSeInt, en papel o en Access, con datos nuevos, pasos guiados y puntos de control para que verifiques tu trabajo.',
 'El caso que nos acompaña es el Copetín Karumbé, un emprendimiento gastronómico paraguayo. En las prácticas aparecen además una biblioteca escolar, un club de barrio, los talleres del colegio, una cantina y una librería, porque diseñar bases de datos es reconocer los mismos patrones en negocios distintos. El año termina con el Proyecto Final Integrador para la Feria de Informática.',
]

COMO_USAR = [
 ('Clase N', 'Ficha con la capacidad del programa oficial e indicadores · desarrollo con ejemplos resueltos · recuadros Concepto clave, Ejemplo, Errores frecuentes y, cuando corresponde, En Paraguay o Aplicación profesional · actividades de aplicación.'),
 ('Práctica N', 'Empieza en página propia y se puede fotocopiar suelta: competencia, lo que necesitás saber, actividades con objetivo, modelo, pasos y punto de control, y un desafío final. Algunas suman una transferencia con revisión entre pares.'),
 ('Punto de control', 'Te dice cómo comprobar tu trabajo, sin darte la respuesta: si no se cumple, revisá tus pasos antes de seguir.'),
 ('Evaluaciones', 'Al cierre de cada unidad (banda ámbar) y de cada etapa (banda azul), en páginas propias.'),
]

DIAGNOSTICA_INTRO = 'Respondé con lo que sabés hasta hoy. Esta prueba no lleva nota: sirve para que tu docente conozca tu punto de partida.'
DIAGNOSTICA = [
 ('Escribí, con tus palabras, qué es un programa de computadora.', 'Acepta cualquier idea de «conjunto de órdenes o instrucciones que la computadora ejecuta».'),
 ('Nombrá un lenguaje de programación que hayas escuchado o usado.', 'Cualquier lenguaje real (Python, Java, C…); PSeInt se acepta como herramienta de pseudocódigo.'),
 ('Escribí, paso a paso, las órdenes para calcular el vuelto de una compra de G. 7.000 pagada con G. 10.000.', 'Secuencia ordenada: leer precio y pago → vuelto = 10.000 − 7.000 = 3.000 → mostrar 3.000.'),
 ('¿Dónde creés que guarda un negocio la lista de sus productos y precios? Nombrá un ejemplo.', 'Acepta planilla, cuaderno, sistema o base de datos; interesa ver si ya existe la noción de «datos organizados».'),
 ('Marcá V o F: «Una computadora entiende las órdenes aunque estén incompletas o sean ambiguas».', 'Falso: necesita órdenes completas y precisas.'),
 ('¿Usaste alguna vez una planilla (Excel) o un programa de gestión? Contá brevemente para qué.', 'Respuesta abierta: relevar la experiencia previa para calibrar el ritmo de la Unidad 4.'),
]

UNIDADES = {
 1: 'En esta unidad vas a conocer qué es un lenguaje de programación, cómo se traduce a lo que ejecuta la máquina, qué estilos de programación existen y con qué criterios se elige el lenguaje para un problema real.',
 2: 'En esta unidad vas a descubrir por qué los negocios pasan del cuaderno a la base de datos: qué es un SGBD, cómo se organizan las tablas con sus claves, qué protege la integridad referencial y cómo se mira una base por dentro.',
 3: 'En esta unidad vas a diseñar antes de construir: modelar con entidades, atributos y relaciones, dibujar el diagrama Entidad-Relación, traducirlo a tablas y comprobar con la normalización que cada dato vive en su lugar.',
 4: 'En esta unidad la base cobra vida: la vas a crear en Microsoft Access con sus relaciones y la vas a consultar con filtros, criterios, parámetros, totales y referencias cruzadas, hasta convertir los datos en decisiones.',
}

PFI_INTRO = [
 'Durante el año construiste, con las distintas materias, las piezas de un sistema para un emprendimiento paraguayo. En este proyecto final, que se presenta en la Feria de Informática, las juntás en una solución digital completa: la base de datos del emprendimiento, diseñada, normalizada y consultada, como corazón del sistema de gestión.',
 'El emprendimiento de referencia es el Copetín Karumbé, pero tu equipo puede elegir otro (una librería, una cantina, un club, una ferretería del barrio). Lo importante es que la solución resuelva una necesidad real: registrar lo que el negocio hace y obtener información útil para decidir.',
]
PFI_COMPETENCIA = 'Integrar el diseño, la creación y la consulta de una base de datos en una solución digital que responda a las necesidades de gestión de un emprendimiento, y presentarla con claridad ante un público.'
PFI_APORTES = ['El diagrama entidad-relación del emprendimiento y su esquema de tablas normalizado hasta 3FN.',
               'La base de datos creada en Access, con claves y relaciones con integridad referencial.',
               'Las consultas que responden las preguntas del negocio: recaudación total, ventas por cliente, producto más vendido, importe por categoría.']
PFI_REQUISITOS = [
 ('Diseño', 'Mini-mundo delimitado y lista de al menos cuatro preguntas del negocio · DER completo · al menos una relación N:M resuelta con tabla puente.'),
 ('Normalización', 'Esquema en 3FN, con las dependencias funcionales principales escritas y justificadas.'),
 ('Base en Access', 'Al menos cuatro tablas con tipos y propiedades · claves principales (una compuesta) · relaciones con integridad referencial · datos de prueba propios (no los del libro).'),
 ('Consultas', 'Al menos cinco: una de selección con criterio, una paramétrica, una de totales, una con campo calculado y una de referencias cruzadas.'),
 ('Presentación', 'Guion de demostración de cinco minutos.'),
]
PFI_EXTENSION = 'Extensión recomendada: agregá al menos un formulario de carga y un informe. No son requisitos mínimos para aprobar el proyecto, pero mejoran la usabilidad y la presentación profesional de la solución.'
PFI_ETAPAS = [
 ('Taller 1 — Definición y diseño', 'Elegís el emprendimiento, relevás sus preguntas, dibujás el DER y lo llevás a tablas normalizadas.'),
 ('Taller 2 — Construcción', 'Creás la base en Access, definís las relaciones, cargás datos de prueba y formulás las consultas.'),
 ('Taller 3 — Integración y demostración', 'Sumás las piezas de las otras materias, verificás cada consulta con un control cruzado y ensayás la presentación.'),
]
PFI_INTERDISCIPLINA = [
 ('Algorítmica', 'Diseño, creación y consulta de la base de datos del sistema.'),
 ('Matemática Aplicada', 'Cálculos del negocio: precios, porcentajes, totales y promedios.'),
 ('Gabinete de Software', 'Documentos, planillas y presentación del sistema para la feria.'),
 ('Gabinete de Laboratorio', 'Puesta a punto del equipo y resguardo de los archivos del proyecto.'),
 ('Dibujo Técnico', 'Identidad visual: logo, afiche y plano del stand a escala.'),
]
PFI_ENTREGABLES = ['Carpeta del proyecto con el documento de diseño (mini-mundo, preguntas, DER, esquema y normalización).',
                   'Archivo de la base (.accdb) con tablas, relaciones y consultas; el formulario y el informe, si se hicieron como extensión recomendada.',
                   'Guion de la demostración y reparto de roles del equipo.']
PFI_PAUTAS = ['Trabajen en equipos de 3 o 4 integrantes, con roles claros (diseño, base, consultas, presentación).',
              'Usen el mismo emprendimiento en todas las materias.',
              'Cuiden que cada consulta responda una pregunta real del negocio y que sus resultados se puedan verificar por otro camino.',
              'Preparen una explicación breve y clara: qué problema resuelve el sistema y qué información aporta al negocio.']
PFI_CONCEPTO = 'Una base de datos funcionando en Access, con sus tablas, relaciones y al menos cinco consultas útiles, presentada junto con los materiales de las otras materias alrededor del mismo emprendimiento.'

RUBRICA = [('Funcionamiento de la base y las consultas en Access', '25 %'),
           ('Aplicación de los contenidos del año (DER, normalización, consultas)', '25 %'),
           ('Integración interdisciplinaria (mismo emprendimiento en todas las materias)', '20 %'),
           ('Presentación en la feria (claridad y utilidad para el negocio)', '15 %'),
           ('Trabajo en equipo', '15 %')]
ORIENTACIONES_PFI = ['Lanzar el proyecto al inicio de la Unidad 4, cuando el diseño ya está dominado, y trabajarlo en los tres talleres del Plan Anual.',
                     'Formar equipos de 3 o 4 integrantes con roles definidos y rotativos en los ensayos.',
                     'Coordinar con las otras materias del curso para que todas trabajen sobre el mismo emprendimiento.',
                     'Pedir datos de prueba propios del equipo: no se aceptan las tablas del Copetín copiadas del libro.',
                     'Exigir un control cruzado por consulta (por ejemplo, total por cliente = total por categoría).']

# v2 · rúbrica analítica: mismos cinco criterios y pesos; el nivel asigna 100 %, 60 %, 30 % o 0 % del peso.
NIVELES = [('Logrado', 1.0), ('En proceso', 0.6), ('Inicial', 0.3), ('No presentado', 0.0)]
RUBRICA_ANALITICA = [
 ('Funcionamiento de la base y las consultas en Access', 25, [
   'La base abre sin errores; las tablas tienen tipos y claves correctos, todas las relaciones exigen integridad referencial y las cinco consultas mínimas se ejecutan con resultados verificados por un control cruzado.',
   'La base abre y las relaciones están definidas, pero alguna no exige integridad referencial, o una o dos consultas dan error o un resultado que no se verificó.',
   'Hay tablas con datos, pero faltan relaciones o la integridad está incompleta, y funcionan menos de tres de las cinco consultas mínimas.',
   'No se entrega el archivo de la base o el archivo no abre.']),
 ('Aplicación de los contenidos del año (DER, normalización, consultas)', 25, [
   'El DER tiene cardinalidad en ambos extremos y al menos una relación N:M resuelta con tabla puente; el esquema está en 3FN con las dependencias funcionales escritas y justificadas; cada consulta responde una pregunta del negocio.',
   'DER y esquema completos, con uno o dos errores (una cardinalidad mal leída, una dependencia transitiva sin resolver) o con dependencias funcionales sin justificar.',
   'Hay DER o esquema, pero no se corresponden entre sí o tienen errores que impiden reconstruir los datos (listas en una celda, clave foránea del lado equivocado).',
   'No se presenta el documento de diseño.']),
 ('Integración interdisciplinaria (mismo emprendimiento en todas las materias)', 20, [
   'El mismo emprendimiento aparece en los aportes de todas las materias participantes y la presentación muestra cómo se conectan con la base de datos.',
   'El emprendimiento es el mismo, pero falta el aporte de una materia o no se lo vincula con la base.',
   'Los aportes de las otras materias se presentan por separado, sin relación con el sistema.',
   'No hay aportes de otras materias.']),
 ('Presentación en la feria (claridad y utilidad para el negocio)', 15, [
   'La demostración dura unos cinco minutos, sigue el guion, muestra al menos dos consultas en vivo y explica qué problema del negocio resuelve, con lenguaje claro para el público.',
   'La demostración funciona, pero excede el tiempo, se aparta del guion o explica la parte técnica sin decir para qué le sirve al negocio.',
   'La demostración se interrumpe por errores o se limita a leer diapositivas sin mostrar la base funcionando.',
   'El equipo no presenta.']),
 ('Trabajo en equipo', 15, [
   'Cada integrante cumple su rol y puede explicar cualquier parte del proyecto; la carpeta registra la distribución de tareas y los avances de los tres talleres.',
   'Los roles se cumplen de forma despareja o algún integrante solo puede explicar su propia parte.',
   'Uno o dos integrantes concentran el trabajo y no hay registro de la distribución de tareas.',
   'No hay evidencia de trabajo compartido.']),
]
assert [(c, p) for c, p, _ in RUBRICA_ANALITICA] == [(c, int(p.split()[0])) for c, p in RUBRICA]

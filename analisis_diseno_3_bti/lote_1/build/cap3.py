# -*- coding: utf-8 -*-
"""Capítulo 3 — «Elegir un alcance posible» (Work §6: secciones 3.1 a 3.4 y revisión de la Unidad I con H1;
encuentros 5 y 6). Compara TIPOS de solución con una factibilidad cualitativa y una tabla de riesgos; no usa
la matriz de decisión con pesos de la Práctica 4 de Algorítmica 3.º ni compara tecnologías.
Las reglas a negociar se presentan sin numerar (se numeran RN-01 a RN-06 desde el Capítulo 4)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'caso'))
import dossier as D
import mbokaja as MB

NUM = 3
UNIDAD = 'Unidad I — Comprender el problema y su contexto'
CAPITULO = 'Capítulo 3'
TITULO = 'Elegir un alcance posible'
ENCUENTROS = (5, 6)
SECCIONES = ['3.1 Objetivos y resultados esperados',
             '3.2 Comparación de alternativas y factibilidad básica',
             '3.3 Recursos, riesgos, límites y exclusiones',
             '3.4 Acuerdo de proyecto y organización del equipo']
REVISION_WORK = 'Revisión de la Unidad I: defensa del problema y del alcance; H1'

ROTULO_CAPACIDAD = ('Capacidades propuestas para el programa institucional (C1, C2 y C7; no son capacidades oficiales '
                    'del MEC)')
CAPACIDAD = ('C1. Delimita un problema y evalúa la factibilidad de una solución.\n'
             'C2. Obtiene y contrasta información sobre necesidades de usuarios.\n'
             'C7. Organiza y registra el trabajo colaborativo.')
TEMA = ('Objetivos, resultados esperados y su relación con las necesidades. Alternativas de solución y '
        'factibilidad operativa, técnica, económica y de calendario. Recursos y riesgos: probabilidad, impacto, '
        'mitigación y contingencia. Alcance mínimo, exclusiones y reglas a negociar. Acuerdo de proyecto, roles y '
        'versiones. Revisión de la Unidad I (hito H1).')
INDICADORES = [
    'Formula objetivos y resultados esperados comprobables, cada uno vinculado a necesidades del dossier.',
    'Compara al menos dos tipos de solución según su factibilidad operativa, técnica, económica y de calendario.',
    'Identifica recursos y riesgos, con su probabilidad, su impacto y una mitigación, y delimita el alcance con sus exclusiones.',
    'Justifica cada decisión de alcance con evidencia del dossier y marca lo que todavía hay que verificar.',
    'Organiza el equipo con roles, tareas, un acuerdo de proyecto y versiones identificables de sus documentos.',
]
TIEMPO = ('Dos encuentros de 5 HC (5 y 6 de la secuencia anual). El Encuentro 6 incluye la revisión de la Unidad I '
          '(hito H1).')

APERTURA = [
    'Con el dossier del Capítulo 2 ya sabés qué necesita cada persona. Ahora hay que decidir qué se va a hacer, y '
    'sobre todo qué no. Un proyecto escolar tiene un año, un equipo de pocas personas y una computadora vieja: no '
    'puede atender todas las necesidades a la vez. Elegir un alcance posible es la decisión más importante de la '
    'Unidad I.',
    'En este capítulo formulás los objetivos, comparás tipos de solución con criterios de factibilidad, '
    'identificás los riesgos y fijás el alcance con sus exclusiones. Al final, tu equipo firma un acuerdo de proyecto '
    'y lo defiende en la revisión de la unidad: el hito H1.',
]
ARTICULACION = [
    'Con el Capítulo 2: cada objetivo y cada exclusión citan necesidades del dossier (N-01…).',
    'Con Algorítmica 3.º: allí se trabaja una matriz de decisión para elegir una tecnología. Acá no se elige '
    'tecnología: se comparan tipos de solución con razones.',
    'Con los Capítulos 4 a 6: las reglas a negociar se numeran y se usan en el Capítulo 4; los cambios de alcance se '
    'tramitan en el Capítulo 6.',
]

# ------------------------------------------------------------------ encuentro 5
E5_TITULO = 'Encuentro 5 — Objetivos, alternativas y riesgos'

S31 = ('3.1 Objetivos y resultados esperados', [
    'Un objetivo dice qué cambio busca el proyecto y para quién. No describe una tarea («hacer entrevistas») ni una '
    'solución («hacer una página web»), sino una situación mejor que la actual. El objetivo general resume el '
    'propósito; los objetivos específicos lo descomponen en cambios más concretos, y cada uno se apoya en una o más '
    'necesidades del dossier. Si un objetivo no se apoya en ninguna necesidad, sobra o falta relevar.',
    'Un resultado esperado es el producto o la evidencia que va a mostrar que el objetivo se cumplió. Tiene que '
    'poder verse: una consulta que funciona con datos de prueba, un rechazo comprobado, un informe cuya suma '
    'coincide con el total. Si no se puede decir qué se va a mostrar, el objetivo todavía es demasiado vago.',
    'Hay tres errores frecuentes. El objetivo-tarea («relevar la biblioteca») confunde el camino con el destino. El '
    'objetivo-solución («instalar una base de datos») decide la tecnología antes de comparar alternativas. Y el '
    'objetivo inabarcable («mejorar la lectura en el colegio») describe algo que ningún sistema de información '
    'puede lograr solo.',
])

EJ31 = ('Ejemplo resuelto 3.1: objetivos del proyecto de la biblioteca', [
    'Consigna: formular el objetivo general y los objetivos específicos a partir de la lista de necesidades, con el '
    'resultado esperado de cada uno.',
    'Objetivo general: mejorar el registro y la consulta de los préstamos de la biblioteca del Colegio Técnico '
    'Arapoty, para que la bibliotecaria, los lectores y la dirección cuenten con información confiable y a tiempo, '
    'con recursos que el colegio pueda sostener (D0-2).',
    'Objetivos específicos y resultados esperados: Tabla 3.1. Cada uno indica las necesidades en que se apoya.',
    'Qué quedó afuera y por qué: N-12 (lotes del plan lector) está en conflicto y depende de una decisión de la '
    'dirección; N-13 (renovar sin llevar el libro) necesita una regla que todavía no existe. No se descartan: se '
    'registran como exclusiones del alcance inicial (sección 3.3).',
])

TABLA_31 = (['Objetivo específico', 'Necesidades', 'Resultado esperado (lo que se va a mostrar)'],
            [['OE-1. Que la bibliotecaria sepa en el momento qué lector tiene cada ejemplar y a qué préstamo corresponde cada devolución', 'N-01, N-05, N-09', 'Consulta de préstamos activos por ejemplar y devolución asociada a su préstamo, con datos de prueba'],
             ['OE-2. Que ningún ejemplar quede prestado a dos lectores a la vez', 'N-02, N-04', 'Rechazo comprobado de un segundo préstamo del mismo ejemplar'],
             ['OE-3. Que los lectores sepan si hay un ejemplar disponible sin ver datos de otros lectores', 'N-03, N-07', 'Consulta de disponibilidad sin datos personales'],
             ['OE-4. Que la dirección obtenga los préstamos por curso de un mes sin contar a mano', 'N-06', 'Informe mensual por curso cuya suma coincide con el total'],
             ['OE-5. Que solo personas autorizadas registren operaciones, con los recursos que el colegio tiene', 'N-08, N-10, N-11', 'Operaciones que exigen un rol autorizado; funcionamiento sin internet en la computadora de la biblioteca (a verificar en el equipo real)']])

S32 = ('3.2 Comparación de alternativas y factibilidad básica', [
    'Antes de decidir cómo resolver el problema, conviene ver al menos dos o tres tipos de solución distintos. Acá no '
    'se comparan lenguajes ni programas concretos, sino caminos: mejorar el registro manual, adoptar una herramienta '
    'que ya existe o construir un prototipo propio. Incluir siempre la mejora del registro manual es una cuestión '
    'de honestidad: a veces alcanza, y un buen analista lo dice aunque el equipo tenga ganas de programar.',
    'Cada alternativa se analiza con cuatro preguntas de factibilidad. Operativa: ¿las personas la van a usar en su '
    'trabajo real, por ejemplo en el primer recreo? Técnica: ¿hay equipos y conocimientos para ponerla en marcha y '
    'mantenerla? Económica: ¿cuesta lo que el colegio puede pagar, contando también el tiempo de las personas? De '
    'calendario: ¿puede estar lista y probada dentro del año escolar?',
    'Cada respuesta se valora como alta, media o baja, siempre con una razón y, si se puede, con una fuente del '
    'dossier. Cuando el dato no está, se escribe «a verificar» en lugar de inventarlo. Antes de comparar, se revisan '
    'las condiciones excluyentes: lo que la institución puso como límite. Una alternativa que no cumple una condición '
    'excluyente se descarta, por buena que sea en lo demás. En el caso, son condiciones excluyentes no generar gastos '
    'en programas ni servicios (E5-L4), funcionar en la computadora de la biblioteca sin internet seguro (E4-L10) y '
    'cuidar los datos de los estudiantes (D0-5).',
    'La comparación no termina en un número. Termina en una recomendación escrita, que dice qué se propone, por qué, '
    'qué se resigna y qué queda por verificar. La decisión final no la toma el equipo sino quien tiene autoridad, '
    'en este caso la dirección, con la conformidad de la bibliotecaria (D0-5).',
])

TABLA_32 = (['Alternativa', 'En qué consiste', 'Qué necesidades puede atender'],
            [['A. Registro manual mejorado', 'Planilla impresa de préstamos con el código de cada ejemplar y una columna de devolución; fichero de lectores; lista semanal de disponibles en la puerta', 'N-05 y N-09; en parte N-01 y N-06. No impide el doble préstamo (N-02) ni informa antes de ir (N-03)'],
             ['B. Herramienta existente', 'Usar un programa ya hecho: una planilla de cálculo o un programa libre de gestión de bibliotecas, sin elegir todavía uno concreto', 'Depende de la herramienta. Una planilla sola no impide el doble préstamo (N-02) ni separa quién puede modificar (N-08)'],
             ['C. Prototipo propio', 'Aplicación construida por el curso para la computadora de la biblioteca, con el alcance mínimo de la sección 3.3', 'N-01 a N-10, si se cumple el alcance mínimo']])

TABLA_33 = (['Factibilidad', 'A. Registro manual mejorado', 'B. Herramienta existente', 'C. Prototipo propio'],
            [['Operativa', 'Media: en hora pico se sigue escribiendo a mano (E1-L2, O1-1)', 'A verificar: depende de que la bibliotecaria la use sin ayuda (N-11)', 'Media: se diseña con la bibliotecaria; exige una práctica guiada'],
             ['Técnica', 'Alta: no necesita equipos', 'A verificar: instalarla y mantenerla depende del encargado de informática, a quien no se entrevistó', 'Media: el curso aprende a construirlo este año; hay que probarlo en la computadora vieja desde el principio (E4-L10)'],
             ['Económica', 'Alta: solo papel', 'Alta si no tiene costo (E5-L4); la licencia, a verificar', 'Alta en dinero (E5-L4); el costo es el tiempo del curso'],
             ['Calendario', 'Alta: se pone en marcha en pocas semanas', 'Media: configurar y cargar los datos', 'Media: solo si se limita al alcance mínimo'],
             ['Condiciones excluyentes', 'Las cumple', 'A verificar: internet, equipo y licencia', 'Las cumple si funciona sin internet y con datos protegidos']])

CAJA_SIN_PUNTAJES = ('Por qué no sumamos puntajes', [
    'La Tabla 3.3 no suma ni promedia. Las cuatro factibilidades no se compensan entre sí: una alternativa barata y '
    'rápida que la bibliotecaria no va a usar no sirve. Por eso se comparan razones, no totales, y la recomendación '
    'explica qué se gana y qué se resigna.',
    'Si tu equipo quisiera asignar pesos a los criterios, esa técnica se trabaja en Algorítmica 3.º (Práctica 4), '
    'para elegir una tecnología. Acá la pregunta es otra: qué tipo de solución conviene, y eso se responde con '
    'evidencia del dossier.',
])

EJ32 = ('Ejemplo resuelto 3.2: de la comparación a la recomendación', [
    'Consigna: con la Tabla 3.3, escribir una recomendación para la dirección.',
    'Paso 1. Condiciones excluyentes. A y C las cumplen. B queda «a verificar»: no se sabe si la herramienta '
    'funcionaría sin internet ni quién la mantendría. No se descarta: se registra la pregunta para el encargado de '
    'informática.',
    'Paso 2. Necesidades centrales. Las que la dirección puso como mínimo (D0-3) y las confirmadas con más fuentes son '
    'N-01, N-02, N-05 y N-06. A no resuelve N-02 ni N-03; C puede resolver todas, si el alcance se limita.',
    'Paso 3. Lo que se resigna. C exige tiempo del curso y una práctica guiada para la bibliotecaria; si la '
    'computadora falla, el sistema se detiene.',
    'Paso 4. Recomendación: construir el prototipo propio (C) con el alcance mínimo, y conservar el registro manual '
    'mejorado (A) como plan de contingencia, con el mismo formato, para usarlo si se corta la luz o falla la '
    'computadora. Entrevistar al encargado de informática antes del Encuentro 7, para cerrar las dudas sobre B y '
    'sobre la computadora.',
    'Paso 5. Quién decide: la dirección, con la conformidad de la bibliotecaria (D0-5). Si el análisis hubiera '
    'mostrado que A alcanzaba, la recomendación honesta habría sido A, aunque el curso tuviera ganas de programar. La '
    'Práctica 3 muestra un caso en que pasa algo parecido.',
])

S33 = ('3.3 Recursos, riesgos, límites y exclusiones', [
    'Los recursos son lo que el proyecto tiene para trabajar: personas (el equipo, el docente, el tiempo que la '
    'bibliotecaria puede dedicar a revisar), equipos (la computadora de la biblioteca), tiempo (los encuentros del año '
    'y sus hitos) y conocimientos. Escribirlos evita prometer lo que no se puede cumplir.',
    'Un riesgo es un hecho incierto que, si ocurre, afecta al proyecto. Se describe con su probabilidad (baja, media '
    'o alta) y su impacto (bajo, medio o alto), valorados con razones. Esas dos valoraciones no se multiplican: se '
    'ubican en un mapa para ver qué riesgos requieren más atención (Figura 3.1). Para cada riesgo importante se '
    'anota una mitigación, que es lo que se hace antes para que sea menos probable o menos grave, y una contingencia, '
    'que es lo que se hace si ocurre. Cada riesgo tiene un responsable dentro del equipo.',
    'El alcance dice qué va a hacer el proyecto; las exclusiones, qué no va a hacer, con su razón. El alcance mínimo '
    'del proyecto es el núcleo que el informe de diseño del curso propone para el año: catálogo y ejemplares, '
    'lectores, préstamo, devolución, consultas, permisos mínimos, persistencia y entrega (Tabla 3.5). Los permisos '
    'mínimos están en el núcleo porque lo pidieron la bibliotecaria (E4-L8) y la directora (E5-L6): quien consulta '
    'el catálogo no puede modificar préstamos.',
    'Fuera del núcleo quedan funciones que se pueden proponer como extensiones si el núcleo se termina, y pedidos '
    'que necesitan una decisión previa, como renovar sin llevar el libro (N-13) o los lotes del plan lector (N-12). '
    'Una exclusión no es un rechazo: es un acuerdo explícito, que evita que el proyecto crezca sin control. Además, '
    'el prototipo trabaja siempre con datos inventados, nunca con los datos reales de los lectores.',
])

TABLA_34 = (['Cód.', 'Riesgo', 'Prob.', 'Impacto', 'Mitigación (antes)', 'Contingencia (si ocurre)'],
            [['R-01', 'La computadora de la biblioteca no alcanza o falla', 'Media', 'Alto', 'Probar el prototipo en esa computadora desde el principio', 'Registro manual mejorado hasta reparar'],
             ['R-02', 'Corte de energía durante una operación', 'Media', 'Alto', 'Respaldos frecuentes; procedimiento de recuperación escrito', 'Registro manual; al volver la luz, comprobar los datos antes de reabrir'],
             ['R-03', 'La bibliotecaria no adopta el nuevo registro', 'Media', 'Alto', 'Revisiones con ella en cada unidad; práctica guiada', 'Ajustar las pantallas según sus observaciones'],
             ['R-04', 'El equipo no termina el núcleo a tiempo', 'Media', 'Alto', 'Alcance mínimo y exclusiones; avance por incrementos', 'Entregar lo terminado y probado; postergar extensiones'],
             ['R-05', 'Se exponen datos personales de los estudiantes', 'Baja', 'Alto', 'Datos inventados en el prototipo; permisos mínimos', 'Retirar los datos expuestos y avisar a la dirección'],
             ['R-06', 'Cambian las reglas de préstamo durante el año', 'Media', 'Medio', 'Reglas acordadas por escrito y cambios registrados', 'Tramitar el cambio como solicitud (Capítulo 6)']])

LEAD_FIG31 = ('Observá la figura: cada riesgo de la Tabla 3.4 está ubicado según su probabilidad y su impacto. Los de la '
              'zona superior derecha son los que reciben atención primero. No hay cálculo: la ubicación sale de las '
              'razones de la tabla.')
EPI_FIG31 = 'Figura 3.1 — Mapa de riesgos del proyecto de la biblioteca (valoración cualitativa, caso ficticio).'

EJ33 = ('Ejemplo resuelto 3.3: un riesgo tratado de punta a punta', [
    'Consigna: desarrollar el riesgo R-02, corte de energía durante una operación.',
    'Por qué probabilidad media: los cortes de energía ocurren varias veces al año en muchas localidades, y la '
    'biblioteca no tiene equipo de respaldo de energía (supuesto razonable; a verificar con el encargado de '
    'informática).',
    'Por qué impacto alto: si la luz se corta mientras se registra un préstamo, puede quedar la duda de si se guardó. '
    'Si el sistema se usa sin comprobar, puede haber préstamos perdidos o duplicados, justo lo que N-02 quiere evitar.',
    'Mitigación: respaldos frecuentes y un procedimiento escrito para volver a usar el sistema después de un corte: '
    'primero se comprueba que los datos estén completos y recién después se habilita de nuevo.',
    'Contingencia: mientras no hay luz, la bibliotecaria usa la planilla impresa del registro manual mejorado (la '
    'alternativa A), con el mismo formato. Cuando vuelve la luz y se comprobaron los datos, esos préstamos se cargan.',
    'Responsable: el integrante del equipo a cargo de las versiones y los recursos (sección 3.4).',
])

REGLAS_INTRO = ('Para el alcance hacen falta reglas de préstamo. Las siguientes son las reglas iniciales para negociar en '
                'clase. Son supuestos didácticos del proyecto: no son normas del MEC ni políticas de una biblioteca real. '
                'En el Capítulo 4 se numeran y se usan para escribir requisitos.')

TABLA_36 = (['Pedido o función', 'Decisión', 'Razón'],
            [['Pagos y multas', 'Excluido', 'El reglamento pide reponer el libro (D1-A5), no cobrar; manejar dinero agrega riesgos'],
             ['Reservas en línea y notificaciones externas', 'Excluido', 'Requieren internet, que la biblioteca no siempre tiene (E4-L10)'],
             ['Aplicación móvil nativa y publicación pública', 'Excluido', 'Sin presupuesto ni servicio en internet (E5-L4); la consulta se resuelve en la computadora de la biblioteca'],
             ['Códigos de barras', 'Excluido del núcleo', 'Solución anticipada (D0-4); se puede proponer como extensión'],
             ['Catálogo nacional y múltiples sedes', 'Excluido', 'Fuera del problema de una biblioteca escolar'],
             ['Renovar sin llevar el libro (N-13)', 'Postergado', 'Falta acordar la regla de renovación (E3-L4)'],
             ['Lotes del plan lector (N-12)', 'Pendiente de decisión', 'En conflicto con el plazo; decide la dirección (E5-L8)']])

ACT_E5 = [
    ('Ejercitá', [
        'Indicá si cada enunciado es un objetivo, una tarea o una solución, y reescribí como objetivo los que no lo son:\n'
        '(a) «Entrevistar a los docentes de Castellano.»\n'
        '(b) «Que la bibliotecaria sepa qué libros están vencidos.»\n'
        '(c) «Programar una página con PHP.»\n'
        '(d) «Que la dirección conozca cuántos préstamos hubo por curso.»\n'
        '(e) «Comprar una computadora nueva.»',
        'Para cada riesgo, indicá si la medida es una mitigación o una contingencia:\n'
        '(a) Corte de energía: tener la planilla impresa a mano.\n'
        '(b) La bibliotecaria no adopta el sistema: hacer una práctica guiada antes de usarlo.\n'
        '(c) El equipo se atrasa: entregar solo lo terminado y probado.\n'
        '(d) Exposición de datos: usar datos inventados en el prototipo.',
    ]),
    ('Resolvé', [
        'Escribí el resultado esperado de OE-2 de otra manera, sin cambiar el objetivo, y explicá cómo lo comprobaría '
        'una persona que no está en el equipo.',
        'Desarrollá el riesgo R-03 como en el Ejemplo resuelto 3.3: razón de la probabilidad, razón del impacto, '
        'mitigación, contingencia y responsable.',
    ]),
    ('Pensá y decidí', [
        'Un compañero propone pasar la herramienta existente (B) a «baja» en factibilidad técnica porque «seguro que '
        'pide internet». ¿Es correcto? ¿Qué harías con esa afirmación antes de usarla en la comparación?',
    ]),
    ('Desafío', [
        'Supongamos que el encargado de informática confirma que la computadora de la biblioteca no puede usarse para '
        'el sistema. Reescribí la recomendación del Ejemplo resuelto 3.2: ¿qué alternativa propondrías y qué cambiaría '
        'en el alcance?',
    ]),
]

# ------------------------------------------------------------------ encuentro 6
E6_TITULO = 'Encuentro 6 — Acuerdo de proyecto y revisión de la Unidad I'

S34 = ('3.4 Acuerdo de proyecto y organización del equipo', [
    'El acuerdo de proyecto es el documento en el que el equipo fija a qué se compromete: el problema, los '
    'objetivos, el alcance y las exclusiones, las reglas a negociar, los supuestos y riesgos, quiénes integran el '
    'equipo y qué rol tiene cada uno, el calendario de hitos y cómo se van a registrar los cambios. Se firma por el '
    'equipo y se presenta a los interesados; en el aula, el docente puede hacer el papel de la dirección.',
    'Los roles ordenan el trabajo, no lo dividen en compartimentos: todos relevan, analizan y prueban. En este libro '
    'se proponen cuatro, que rotan en cada unidad para que todos pasen por todos. Coordinación: organiza las tareas y '
    'cuida los plazos. Registro: lleva la bitácora y las actas. Relación con los interesados: prepara las entrevistas '
    'y las revisiones. Versiones y recursos: numera las versiones de los documentos y anota el origen de cada '
    'recurso que se usa.',
    'Cada documento del proyecto lleva una versión identificable: v0.1 es el primer borrador; cada cambio importante '
    'sube el número y se anota en la bitácora qué cambió y por qué. Así, cualquiera puede saber qué versión del '
    'acuerdo se defendió en el H1 y qué se corrigió después. La bitácora registra también quién hizo qué: es la base '
    'de la parte individual de la evaluación.',
    'Después de firmado, el acuerdo puede cambiar, pero no en silencio. Un cambio de alcance se registra como '
    'solicitud de cambio, con su razón, y se acepta o se rechaza. Ese procedimiento se estudia en el Capítulo 6.',
])

EJ34 = ('Ejemplo resuelto 3.4: el acuerdo de proyecto del equipo modelo', [
    'Consigna: armar el acuerdo de proyecto del equipo modelo del libro, versión v1.0, para presentarlo en el H1.',
    'Cómo se armó: cada sección resume un producto ya hecho y remite a él, sin copiarlo entero (Tabla 3.7). El '
    'acuerdo ocupa una o dos páginas; los detalles están en el dossier y en las tablas del capítulo.',
    'Qué se cuidó: que cada decisión tenga su fuente; que los supuestos estén marcados; que las exclusiones tengan '
    'razón; que figure quién decide; y que la versión y la fecha estén a la vista.',
])

TABLA_37 = (['Sección del acuerdo', 'Contenido en el equipo modelo'],
            [['Versión y fecha', 'v1.0 — sexta semana de clases (D0-6)'],
             ['Problema', 'Enunciado del Ejemplo resuelto 1.1, confirmado con el dossier del Capítulo 2'],
             ['Objetivos', 'Objetivo general y OE-1 a OE-5 (Tabla 3.1)'],
             ['Alternativa recomendada', 'Prototipo propio con alcance mínimo y registro manual como contingencia (Ejemplo resuelto 3.2). Decide la dirección.'],
             ['Alcance y exclusiones', 'Núcleo de la Tabla 3.5; exclusiones de la Tabla 3.6'],
             ['Reglas a negociar', 'Las seis reglas iniciales del recuadro de 3.3'],
             ['Supuestos y riesgos', 'R-01 a R-06 (Tabla 3.4). Pendiente: entrevista al encargado de informática'],
             ['Equipo y roles', 'Cuatro integrantes; roles rotativos por unidad; bitácora compartida'],
             ['Hitos', 'H1 a H6 (Tabla 3.8)'],
             ['Cambios', 'Por solicitud de cambio registrada (Capítulo 6)']])

TABLA_38 = (['Hito', 'Encuentro', 'Qué se entrega o se defiende'],
            [['H1', '6', 'Problema y alcance defendidos, con correcciones'],
             ['H2', '12', 'Requisitos y modelos funcionales'],
             ['H3', '18', 'Dossier consistente y evidencia de análisis y diseño'],
             ['H4', '26', 'Prototipo completo mínimo y lista de incidencias'],
             ['H5', '32', 'Versión candidata con límites conocidos'],
             ['H6', '34', 'Paquete reproducible y ajustes finales']])

H1_TITULO = 'Revisión de la Unidad I — Hito H1: problema y alcance defendidos'
H1_TEXTO = [
    'El H1 cierra la Unidad I. Cada equipo presenta y defiende su problema y su alcance ante el docente y el curso. '
    'La presentación dura unos diez minutos y la sigue una ronda de preguntas, algunas dirigidas a cada integrante. '
    'Después, el equipo corrige lo que se le observó y entrega la versión corregida: las correcciones también son '
    'evidencia del hito.',
    'Qué se presenta: la ficha de problema actualizada con el dossier, la lista de necesidades con sus fuentes, los '
    'objetivos, la comparación de alternativas con su recomendación, el alcance con sus exclusiones, los riesgos y el '
    'acuerdo de proyecto.',
]
H1_LISTA = ('Antes de presentar: lista de verificación del equipo', [
    '1. ¿El enunciado del problema no nombra ninguna solución?',
    '2. ¿Cada objetivo cita al menos una necesidad del dossier y tiene un resultado esperado que se puede mostrar?',
    '3. ¿Comparamos al menos dos tipos de solución con las cuatro factibilidades, con razones y fuentes?',
    '4. ¿Lo que no sabemos está marcado «a verificar» en lugar de inventado?',
    '5. ¿El alcance incluye los permisos mínimos y cada exclusión tiene su razón?',
    '6. ¿Cada riesgo importante tiene mitigación, contingencia y responsable?',
    '7. ¿El acuerdo tiene versión, fecha, roles y firmas?',
    '8. ¿Cada integrante puede explicar una decisión y la evidencia que la respalda?',
])
H1_EVALUACION = ('Cómo se evalúa el H1', [
    'Se evalúan cinco criterios con cuatro niveles de desempeño: Sólido, Logrado, En desarrollo e Inicial. La rúbrica '
    'completa está en la guía docente y tu docente la comparte antes de la presentación.',
    'Cada criterio combina un 60 % de evidencia del producto del equipo y un 40 % de evidencia individual: tu '
    'explicación en la ronda de preguntas, tu aporte registrado en la bitácora y la observación del docente. Así, la '
    'nota del equipo no tapa ni el trabajo ni las dificultades de cada uno. Esta proporción y los niveles son una '
    'propuesta editorial: la institución decide cómo se convierten en calificación.',
    'Si falta una evidencia, se registra como ausente y se acuerda cuándo entregarla; no se confunde con un desempeño '
    'de nivel inicial.',
])

ACT_E6 = [
    ('Ejercitá', [
        'Asigná cada tarea al rol que corresponde (coordinación, registro, relación con los interesados, versiones y '
        'recursos):\n'
        '(a) anotar en la bitácora qué se decidió en la reunión;\n'
        '(b) pedir a la bibliotecaria un horario para la revisión;\n'
        '(c) pasar el acuerdo de v1.0 a v1.1 y anotar qué cambió;\n'
        '(d) avisar al equipo que el H1 es en dos encuentros y repartir lo que falta.',
    ]),
    ('Resolvé', [
        'Armá el acuerdo de proyecto de tu equipo, versión v1.0, con las secciones de la Tabla 3.7. Usá tu propio '
        'dossier o el del caso, según indique tu docente.',
        'Aplicá la lista de verificación del H1 al acuerdo de otro equipo y anotá, para cada punto que no se cumple, '
        'una corrección concreta.',
    ]),
    ('Pensá y decidí', [
        'Dos semanas después del H1, la directora pide agregar al sistema el préstamo de los proyectores del colegio. '
        '¿Qué hace el equipo? Explicá por qué no alcanza con decir «sí» o «no».',
    ]),
    ('Desafío', [
        'Escribí tres preguntas que el docente podría hacerle a un integrante del equipo en el H1 para comprobar que '
        'entiende una decisión del alcance, y la respuesta que esperarías.',
    ]),
]

# ------------------------------------------------------------------ práctica
PRACTICA_TITULO = 'Práctica 3 — Decidir un alcance posible para otra biblioteca'
PRACTICA_INTRO = [
    'Volvés a la Escuela Básica Mbokaja. Para que todos partan de lo mismo, la práctica usa las necesidades del '
    'relevamiento de referencia (tabla de abajo), aunque tu dossier de la Práctica 2 haya encontrado otras. Los datos '
    'para decidir son distintos de los de Arapoty, y pueden llevar a una recomendación distinta.',
]
NIVELES = [
    ('Nivel 1 — Guiado', [
        'Completá la tabla de factibilidad de Mbokaja para las alternativas A (registro manual mejorado) y C '
        '(prototipo propio), con una razón y una fuente (M-F…) en cada celda:\n'
        'Operativa: A ________ / C ________. Técnica: A ________ / C ________.\n'
        'Económica: A ________ / C ________. Calendario: A ________ / C ________.',
        'Escribí un objetivo específico para MN-01 y su resultado esperado.',
        'Escribí una recomendación de tres oraciones: qué proponés, por qué y qué resignás.',
    ]),
    ('Nivel 2 — Intermedio', [
        'Compará las tres alternativas (A, B y C) con las cuatro factibilidades y las condiciones excluyentes de '
        'Mbokaja. Cada valoración, con su razón y su fuente.',
        'Formulá tres objetivos específicos con sus resultados esperados y cuatro riesgos con su probabilidad, su '
        'impacto, una mitigación y una contingencia.',
        'Definí el alcance y tres exclusiones justificadas. Escribí la recomendación para la directora.',
    ]),
    ('Nivel 3 — Ampliación', [
        'Además de lo pedido en el Nivel 2, explicá qué dato de Mbokaja cambia la recomendación respecto de Arapoty y '
        'por qué.',
        'MN-02 pide atender al turno mañana. Proponé una solución que no sea informática y analizá su factibilidad con '
        'los mismos criterios.',
        'Escribí qué tendría que pasar (qué dato debería cambiar) para que el prototipo propio fuera la mejor opción '
        'en Mbokaja.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: cada valoración de factibilidad tiene una razón y una fuente M-F, o dice «a '
                    'verificar»; ninguna celda tiene un número ni se suman puntajes; los objetivos citan necesidades '
                    'MN; la recomendación dice qué se resigna y quién decide.')

REPASO = ('Para repasar', [
    'Un objetivo describe el cambio buscado, se apoya en necesidades y tiene un resultado esperado que se puede mostrar.',
    'Se comparan tipos de solución, incluida la mejora manual, con cuatro factibilidades valoradas con razones y fuentes, sin sumar puntajes.',
    'Las condiciones excluyentes se revisan primero; lo que no se sabe se marca «a verificar».',
    'Cada riesgo tiene probabilidad, impacto, mitigación, contingencia y responsable. El alcance tiene núcleo y exclusiones con su razón.',
    'El acuerdo de proyecto fija los compromisos del equipo, con versión y roles; el H1 se defiende en equipo y se evalúa también de forma individual.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, los Encuentros 5 y 6 se unen en uno: la factibilidad se compara con dos '
    'alternativas en lugar de tres (A y C) y el H1 es una defensa breve por equipo.',
    'En ese encuentro no se omiten: el Ejemplo resuelto 3.1 (objetivos), la Tabla 3.3 reducida a dos alternativas, '
    'los riesgos R-01 a R-04, el alcance con sus exclusiones y la defensa del H1. Pasan a lectura domiciliaria: el '
    'Ejemplo resuelto 3.3, la sección 3.4 con el Ejemplo resuelto 3.4 y la Práctica 3; el acuerdo de proyecto se '
    'completa como tarea.',
])

# ------------------------------------------------------------------ evaluación (opcional; el instrumento principal es el H1)
EVAL_ID = 'ADS3-L1-C3'
EVAL_TITULO = 'Evaluación del Capítulo 3'
EVAL_TEXTO_BASE = ('Texto base — Inscripción a talleres (situación de evaluación, ficticia)', [
    'K-1 Cada semestre, el colegio ofrece seis talleres optativos con cupo de veinte estudiantes cada uno.',
    'K-2 La inscripción se hace en una hoja por taller, pegada en la sala de profesores; algunos estudiantes se anotan en dos talleres del mismo horario.',
    'K-3 La coordinación pide saber, al cerrar la inscripción, cuántos inscriptos tiene cada taller.',
    'K-4 La sala de profesores tiene una computadora compartida, sin internet desde hace dos meses.',
    'K-5 El colegio no tiene presupuesto para comprar programas.',
    'K-6 La inscripción del próximo semestre abre en tres semanas.',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', '¿Cuál de estos enunciados es un objetivo bien formulado?',
     ['Que la coordinación conozca los inscriptos de cada taller al cerrar la inscripción.',
      'Programar un formulario de inscripción.',
      'Entrevistar a los estudiantes de 2.º.',
      'Mejorar la educación del colegio.']),
    ('mc', '¿Qué pregunta corresponde a la factibilidad operativa?',
     ['¿Las personas van a usar la solución en su trabajo real?',
      '¿Hay equipos para instalarla?',
      '¿Cuánto cuesta?',
      '¿Puede estar lista dentro del año?']),
    ('mc', 'Para el riesgo «corte de energía durante una operación», tener una planilla impresa para seguir trabajando es…',
     ['una contingencia: se usa si el riesgo ocurre.',
      'una mitigación: hace menos probable el corte.',
      'una exclusión del alcance.',
      'un objetivo específico.']),
    ('mc', 'En el texto base, ¿qué dato funciona como condición excluyente para cualquier alternativa?',
     ['K-5: no hay presupuesto para comprar programas.',
      'K-1: hay seis talleres.',
      'K-3: la coordinación quiere saber los inscriptos.',
      'K-2: la hoja está en la sala de profesores.']),
    ('vf', 'Si una alternativa obtiene «alta» en tres factibilidades y «baja» en la operativa, igual conviene elegirla.',
     False, 'Falso. Las factibilidades no se compensan: si las personas no la van a usar, la solución no sirve.'),
    ('vf', 'Una exclusión del alcance es un pedido que se rechaza para siempre.',
     False, 'Falso. Es un acuerdo explícito sobre lo que no se hace en este proyecto; puede proponerse como extensión o tramitarse como cambio.'),
    ('vf', 'La parte individual de la evaluación del H1 incluye la explicación de cada integrante y su aporte registrado en la bitácora.',
     True, 'Verdadero. Es el 40 % de evidencia individual de la propuesta editorial.'),
    ('ab', 'Con el texto base, compará dos alternativas (por ejemplo, una hoja de inscripción mejorada y un prototipo '
           'propio) en las factibilidades técnica y de calendario. Cada valoración con su razón y su fuente (K-…).',
     'Hoja mejorada: técnica alta (no necesita equipo); calendario alto (se prepara antes de K-6). Prototipo propio: '
     'técnica media o baja (computadora compartida, sin internet, K-4; habría que probar si funciona sin conexión); '
     'calendario bajo (tres semanas, K-6). Un punto por cada valoración con razón y fuente. No se aceptan puntajes '
     'sumados.', 4),
    ('ab', 'Escribí un riesgo del proyecto de inscripción con su probabilidad, su impacto, una mitigación y una '
           'contingencia, y una exclusión del alcance con su razón.',
     'Ejemplo: riesgo «inscripción duplicada en talleres del mismo horario» (fuente: K-2): probabilidad alta, impacto medio; '
     'mitigación: la hoja muestra el horario y se controla al anotar; contingencia: la coordinación resuelve los '
     'duplicados antes de publicar las listas. Exclusión: inscripción por internet, porque la computadora no tiene '
     'conexión (K-4). Un punto por cada elemento correcto (riesgo con valoraciones, mitigación, contingencia, '
     'exclusión con razón).', 4),
]
EVAL_PUNTAJE = ('Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno). '
                'Es opcional: el instrumento principal de la unidad es el H1.')

# ------------------------------------------------------------------ rúbrica del H1 (guía docente; el libro muestra el resumen)
NIVELES_DESEMPENO = [
    ('4. Sólido', 'Resuelve con autonomía, justifica decisiones, aporta evidencia reproducible y transfiere lo aprendido a una variante.'),
    ('3. Logrado', 'Cumple los criterios esenciales y explica el resultado con evidencia suficiente.'),
    ('2. En desarrollo', 'Resuelve parcialmente o con apoyo; presenta inconsistencias que requieren revisión.'),
    ('1. Inicial', 'Todavía no demuestra la capacidad; la evidencia es insuficiente o el resultado no responde al problema.'),
]
# criterio, capacidad, descriptores por nivel (Sólido, Logrado, En desarrollo, Inicial), evidencia de equipo (60 %), evidencia individual (40 %)
RUBRICA_H1 = [
    ('Problema delimitado', 'C1',
     ['Enunciado sin soluciones, con fuentes; distingue lo que el sistema puede y no puede mejorar, y lo aplica a una variante.',
      'Enunciado sin soluciones, apoyado en el dossier.',
      'Enunciado con alguna solución anticipada o sin fuentes.',
      'Describe síntomas o una solución en lugar de un problema.'],
     'Ficha de problema y enunciado', 'Explica de dónde sale el enunciado y responde una variante del docente'),
    ('Evidencia del relevamiento', 'C2',
     ['Necesidades con fuentes contrastadas, contradicciones registradas y elevadas, y una necesidad no expresada.',
      'Necesidades con fuentes existentes; hechos, opiniones y supuestos separados.',
      'Fuentes incompletas o que no respaldan; mezcla opiniones con hechos.',
      'Necesidades sin fuente o inventadas.'],
     'Dossier y lista de necesidades', 'Rastrea una necesidad hasta su línea de registro'),
    ('Objetivos y alternativas', 'C1',
     ['Objetivos con necesidades y resultados comprobables; compara tres tipos de solución con razones, fuentes y «a verificar».',
      'Objetivos vinculados a necesidades; compara al menos dos alternativas con las cuatro factibilidades.',
      'Objetivos-tarea o factibilidades sin razones.',
      'Sin comparación o con una alternativa elegida de antemano.'],
     'Tabla de objetivos, comparación y recomendación', 'Justifica la recomendación y lo que se resigna'),
    ('Alcance, exclusiones y riesgos', 'C1',
     ['Alcance con permisos mínimos, exclusiones razonadas y riesgos con mitigación, contingencia y responsable; anticipa un cambio.',
      'Alcance con exclusiones y riesgos principales tratados.',
      'Alcance impreciso o riesgos sin mitigación.',
      'Sin exclusiones o con un alcance irrealizable.'],
     'Alcance, exclusiones y tabla de riesgos', 'Explica un riesgo y su tratamiento'),
    ('Organización y registro del equipo', 'C7',
     ['Acuerdo con versión, roles y cambios registrados; bitácora al día con aportes de todos; correcciones del H1 incorporadas.',
      'Acuerdo con versión y roles; bitácora con aportes.',
      'Acuerdo incompleto o bitácora irregular.',
      'Sin acuerdo ni bitácora.'],
     'Acuerdo de proyecto y bitácora', 'Aporte propio registrado en la bitácora y observación del docente'),
]

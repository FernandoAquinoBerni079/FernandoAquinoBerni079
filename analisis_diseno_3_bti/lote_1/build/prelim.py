# -*- coding: utf-8 -*-
"""Preliminares del libro (Work §6): presentación y alcance; cómo usar el libro y las prácticas; mapa de
capacidades y evidencias; acuerdo de trabajo; diagnóstico de entrada; presentación del caso; uso responsable
de datos y recursos; guía de consulta a las asignaturas previas. Texto original."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'caso'))
import dossier as D

TITULOS = ['Presentación y alcance', 'Cómo usar el libro y las prácticas', 'Mapa de capacidades y evidencias',
           'Acuerdo de trabajo', 'Diagnóstico de entrada', 'Presentación del caso',
           'Uso responsable de datos y recursos', 'Guía de consulta a las asignaturas previas']

PRESENTACION = [
    'Este libro acompaña la asignatura Análisis y Diseño de Sistemas del 3.er curso del Bachillerato Técnico en '
    'Informática, en el espacio del Plan Optativo. El diseño curricular permite que cada institución elabore el '
    'programa de ese espacio; este libro es una propuesta para ese programa institucional. Sus capacidades (C1 a '
    'C10) son propuestas editoriales: no son capacidades oficiales del MEC.',
    'Durante el año vas a recorrer, con tu equipo, el camino completo de un sistema: entender un problema, '
    'investigarlo, especificar qué tiene que hacer la solución, diseñarla, construir un prototipo web, probarlo y '
    'entregarlo de modo que otra persona lo pueda instalar y usar. El caso conductor es la biblioteca de un colegio '
    'ficticio, el Colegio Técnico Arapoty.',
    'La referencia es de 36 encuentros de 5 horas cátedra (180 HC), organizados en seis unidades de tres capítulos; '
    'cada capítulo corresponde a dos encuentros. Si el año escolar ofrece menos encuentros, cada capítulo indica qué '
    'conservar en la adaptación de 28 encuentros. Esta edición de control contiene los preliminares y la Unidad I '
    '(Capítulos 1 a 3, Encuentros 1 a 6).',
]
UNIDADES = (['Unidad', 'Encuentros', 'HC', 'Resultado de la unidad'],
            [['I. Comprender el problema y su contexto', '1 a 6', '30', 'Problema, relevamiento y alcance viable'],
             ['II. Especificar qué debe resolver el sistema', '7 a 12', '30', 'Requisitos, procesos y trazabilidad inicial'],
             ['III. Diseñar una solución coherente', '13 a 18', '30', 'Modelo de datos, interacción y arquitectura revisados'],
             ['IV. Construir el prototipo por incrementos', '19 a 26', '40', 'Circuito funcional integrado y persistente'],
             ['V. Verificar, validar y mejorar', '27 a 32', '30', 'Evidencia de pruebas, correcciones y aceptación'],
             ['VI. Entregar y comunicar', '33 a 36', '20', 'Paquete reproducible, defensa y recuperación']])

COMO_USAR = [
    'Cada capítulo empieza con una ficha: las capacidades que trabaja, el tema, los indicadores de logro y el tiempo. '
    'Después vienen las secciones, con explicaciones, tablas, figuras y ejemplos resueltos que muestran el '
    'procedimiento paso a paso. Las actividades de cada encuentro están en cuatro bloques: «Ejercitá» fija lo '
    'básico, «Resolvé» aplica el procedimiento, «Pensá y decidí» pide una decisión justificada y «Desafío» propone '
    'algo más exigente.',
    'Cada capítulo tiene una práctica en tres niveles. Todos los niveles usan los mismos datos, que son distintos de '
    'los de los ejemplos: no alcanza con copiar un ejemplo cambiando los nombres. El Nivel 1 es el piso que todo el '
    'curso alcanza, el Nivel 2 es el esperado y el Nivel 3 es ampliación. Al final hay una evaluación opcional, en '
    'página propia, y un recuadro que indica qué conservar si el calendario se acorta.',
    'Los datos del caso tienen códigos. «E1-L4» es la línea 4 de la entrevista E1; «O1-3», el renglón 3 de la '
    'observación O1; «D1-A4», el artículo 4 del documento D1; «N-02», la necesidad 2 del dossier. Cuando el libro '
    'cita entre comillas, la cita es textual y se puede buscar en el registro. Hacé lo mismo en tus trabajos: cada '
    'afirmación importante, con su fuente.',
    'Llevá una bitácora del equipo desde el primer día: fecha, qué se hizo, quién lo hizo, qué se decidió y qué '
    'queda pendiente. La bitácora es evidencia de tu trabajo individual.',
]

CAPACIDADES = (['Código', 'Capacidad propuesta', 'Evidencia principal'],
               [['C1', 'Delimita un problema y evalúa la factibilidad de una solución.', 'Ficha de problema y factibilidad'],
                ['C2', 'Obtiene y contrasta información sobre necesidades de usuarios.', 'Dossier de relevamiento'],
                ['C3', 'Especifica y prioriza requisitos verificables.', 'Catálogo de requisitos versionado'],
                ['C4', 'Modela procesos e interacciones del sistema.', 'Modelos comentados'],
                ['C5', 'Justifica el modelo de información y sus reglas de integridad.', 'Modelo y diccionario de datos'],
                ['C6', 'Diseña la interacción y la arquitectura del prototipo.', 'Bocetos y esquema de arquitectura'],
                ['C7', 'Organiza y registra el trabajo colaborativo.', 'Bitácora y revisiones'],
                ['C8', 'Integra un prototipo funcional con persistencia.', 'Prototipo y demostración'],
                ['C9', 'Verifica y mejora la solución a partir de evidencia.', 'Matriz de pruebas e incidencias'],
                ['C10', 'Documenta, entrega y defiende el prototipo.', 'Paquete de entrega y defensa individual']])
CAPACIDADES_NOTA = ('Capacidades propuestas para el programa institucional; no son capacidades oficiales del MEC. '
                    'Fuente: informe de diseño curricular de la colección (propuesta editorial).')

ACUERDO = [
    '1. Asistencia y puntualidad. Llegamos a tiempo a los encuentros y a las reuniones; si alguien falta, avisa y deja '
    'registrado en la bitácora el estado de sus tareas.',
    '2. Roles. Repartimos los roles de coordinación, registro, relación con los interesados, y versiones y recursos. '
    'Rotan en cada unidad.',
    '3. Bitácora. Anotamos en cada encuentro qué se hizo, quién lo hizo, qué se decidió y qué queda pendiente.',
    '4. Decisiones. Buscamos el acuerdo; si no lo hay, votamos y dejamos registrada la posición que no prosperó.',
    '5. Conflictos. Los hablamos primero en el equipo; si no se resuelven, pedimos ayuda al docente.',
    '6. Autoría y recursos. Anotamos el origen de todo texto, imagen o código que no sea nuestro. Si usamos una '
    'herramienta que genera texto o código, lo declaramos en la bitácora y revisamos lo que produce.',
    '7. Datos de las personas. Pedimos autorización antes de relevar, anotamos solo lo necesario y no publicamos '
    'datos personales.',
    'Firmas de los integrantes y fecha: ____________________________________________',
]

DIAGNOSTICO_INTRO = ('Este diagnóstico no lleva nota: sirve para que vos y tu docente sepan de dónde partís. Respondé '
                     'solo, sin consultar, en el tiempo que indique tu docente (aprox. una hora cátedra). Si no sabés algo, escribí «no lo vi»: es una respuesta '
                     'útil.')
DIAGNOSTICO = [
    ('Programación', [
        'Leé el pseudocódigo y escribí qué muestra si se ingresan, en orden, los valores 3, 9, 7, 12 y 8:\n'
        'cont ← 0\n'
        'Para i desde 1 hasta 5\n'
        '    Leer dias\n'
        '    Si dias > 7 entonces cont ← cont + 1\n'
        'FinPara\n'
        'Mostrar cont',
        'Escribí en pseudocódigo o con palabras precisas la condición: «un estudiante puede inscribirse en un taller '
        'si el taller tiene cupo libre y el estudiante no está inscripto en otro taller del mismo horario».',
        '¿Para qué sirve dividir un programa en funciones o módulos que reciben parámetros? Respondé en dos líneas.',
    ]),
    ('Formularios', [
        'Un formulario de inscripción pide el nombre, el curso (una opción entre seis) y la aceptación de las '
        'normas. ¿Qué control usarías para cada dato?',
        '¿Qué pasa con los datos de un formulario web cuando se presiona «Enviar»? ¿Adónde van y qué tendría que '
        'comprobar quien los recibe?',
    ]),
    ('Datos', [
        'En esta planilla de inscripciones, ¿cuántos estudiantes de 2.º están inscriptos en Robótica?\n'
        'E-01 · 1.º · Robótica     E-02 · 2.º · Teatro     E-03 · 2.º · Robótica\n'
        'E-04 · 2.º · Robótica     E-05 · 3.º · Robótica     E-06 · 2.º · Teatro',
        '¿Qué ventaja tiene guardar el curso en una columna propia, en lugar de escribirlo junto al nombre del '
        'estudiante?',
    ]),
    ('Comunicación', [
        'Escribí un mensaje de tres o cuatro líneas a la bibliotecaria de tu colegio para pedirle una entrevista. '
        'Decí quién sos, para qué es, cuánto dura y que puede no aceptar.',
        'Resumí en una oración: «En el primer recreo se forma una fila larga en la biblioteca. Muchos estudiantes '
        'esperan para preguntar por un libro que no está, y cuando suena el timbre se van sin nada. La bibliotecaria '
        'anota rápido y a veces se equivoca.»',
    ]),
]
AUTOEVALUACION = (['Área', 'Seguro', 'Con dudas', 'No lo vi'],
                  [['Programación', '', '', ''], ['Formularios', '', '', ''], ['Datos', '', '', ''], ['Comunicación', '', '', '']])

CASO_INTRO = D.CASO_PRESENTACION
PERSONAS = (['Persona', 'Rol en el caso'], [[n, r] for _, n, r in D.PERSONAS])
CASO_D0_LEAD = ('Al comenzar las clases, la directora entregó al curso esta nota. Es el pedido que da origen al proyecto '
                'y se trabaja en el Capítulo 1.')

USO_RESPONSABLE = [
    'Datos de personas. El caso del libro es ficticio. Si tu curso investiga una biblioteca real, se hace con '
    'autorización de la institución y de cada persona entrevistada, se anota solo lo necesario y los registros se '
    'anonimizan: los nombres de estudiantes se reemplazan por códigos. El prototipo se prueba siempre con datos '
    'inventados.',
    'Fotos y grabaciones. No se fotografía ni se graba a nadie sin su permiso expreso. Las fotos de espacios no '
    'deben mostrar caras ni datos personales.',
    'Recursos ajenos. Todo texto, imagen, ícono o fragmento de código que no sea del equipo se registra con su '
    'origen y su licencia. Si no se sabe si se puede usar, no se usa.',
    'Herramientas que generan texto o código. Si las usás, declaralo en la bitácora, revisá lo que producen y '
    'asegurate de poder explicarlo: en las defensas, cada integrante responde por lo que entrega.',
    'Equipos de la institución. No se instala nada en una computadora del colegio sin autorización del encargado. '
    'La base de datos del prototipo no se copia ni se mueve mientras el sistema está en uso.',
]

CONSULTA = (['Si necesitás…', 'Consultá', 'Para qué se usa en este libro'],
            [['Pseudocódigo, decisiones y repetición', 'Algorítmica 1.º', 'Expresar reglas sin ambigüedad (Unidad II)'],
             ['Funciones, parámetros, archivos, filtros y consultas', 'Algorítmica 2.º', 'Separar reglas, datos y presentación; validar entradas'],
             ['HTML, CSS y formularios', 'Laboratorio 1.º', 'Interfaces para tareas concretas y mensajes de error (Unidades III y IV)'],
             ['Documentos colaborativos, tareas, seguridad y ética', 'Laboratorio 1.º', 'Dossier, bitácora y cuidado de los datos'],
             ['Variables, funciones, GET y POST, arreglos y archivos', 'Laboratorio 2.º', 'Implementar una regla del caso (Unidad IV)'],
             ['Redes, servidores y servidor web', 'Laboratorio 2.º', 'Operar el entorno del prototipo'],
             ['Bases de datos, consultas y restricciones', 'Laboratorio 3.º y Algorítmica 3.º (se aprenden en paralelo)', 'Modelo de datos e integración (Unidades III y IV)'],
             ['Metodologías de trabajo por iteraciones', 'Laboratorio 3.º (en paralelo)', 'Organizar incrementos y revisiones']])
CONSULTA_NOTA = ('Lo de 1.º y 2.º curso se supone visto y se diagnostica al empezar. Lo de 3.º se aprende al mismo '
                 'tiempo: este libro no lo da por sabido.')

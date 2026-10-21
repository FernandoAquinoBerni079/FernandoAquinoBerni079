# -*- coding: utf-8 -*-
"""Capítulo 7 — «Datos que representan las reglas» (Work §6: secciones 7.1 a 7.4 y práctica; encuentros 13 y 14).

Decisiones de Fernando del 20-oct-2026: notación entidad-relación clásica de Algorítmica 3.º, como representación
simplificada, con los atributos en el diccionario de datos; no se repite la enseñanza de claves, formas normales ni
bases de datos; se profundiza en obra, edición, ejemplar, préstamo, restricciones e historial; se diseña para el
catálogo v1.1 (RF-11 y RN-02 v1.1, con su trazabilidad a SC-01); el curso se exige a los estudiantes y no a los
docentes. Work §5.2 asigna C5 a los dos encuentros; la revisión con contraejemplos del Encuentro 14 se presenta como
articulación con C9, sin atribuírsela a Work.
El modelo del caso está en caso/diseno.py. La Práctica 7 usa Mbokaja (caso/mbokaja_u3.py)."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'caso'))
import diseno as X
import mbokaja_u3 as MB
R, D = X.R, X.D

NUM = 7
UNIDAD = 'Unidad III — Diseñar una solución coherente'
CAPITULO = 'Capítulo 7'
TITULO = 'Datos que representan las reglas'
ENCUENTROS = (13, 14)
SECCIONES = ['7.1 Recuperación aplicada de modelos de Algorítmica',
             '7.2 Obra/edición, ejemplar, lector y préstamo: identidad y responsabilidad',
             '7.3 Relaciones, restricciones, historial y diccionario de datos',
             '7.4 Revisión de normalización con ejemplos del proyecto']
PRACTICA_WORK = 'justificar el modelo frente a pérdida, devolución y duplicación de solicitudes'

ROTULO_CAPACIDAD = 'Capacidad propuesta para el programa institucional (C5; no es una capacidad oficial del MEC)'
CAPACIDAD = 'C5. Justifica el modelo de información y sus reglas de integridad.'
TEMA = ('Recuperación del modelo entidad-relación de Algorítmica 3.º. Obra, edición, ejemplar, lector y préstamo: '
        'identidad y responsabilidad. Relaciones, restricciones que salen de las reglas, historial, datos derivados, '
        'parámetros y diccionario de datos. Revisión aplicada de anomalías con datos del proyecto.')
INDICADORES = [
    'Distingue obra, edición y ejemplar, y vincula cada préstamo a un ejemplar físico.',
    'Justifica las claves y las relaciones del modelo con las reglas y los requisitos del catálogo v1.1.',
    'Expresa las reglas de préstamo como restricciones de integridad y conserva el historial sin borrar registros.',
    'Documenta cada dato en un diccionario con su significado, su obligatoriedad y el requisito que lo pide.',
    'Detecta una anomalía en datos del proyecto y corrige el diseño.',
]
TIEMPO = ('Dos encuentros de 5 HC (13 y 14 de la secuencia anual), de diseño; el Encuentro 14 incluye 1 HC de revisión '
          'del modelo con ejemplos y contraejemplos.')

APERTURA = [
    'Con la Unidad II, el equipo sabe qué tiene que hacer el sistema y cómo lo usan las personas. Ahora hay que decidir '
    'qué datos guarda y cómo se relacionan. La pregunta de este capítulo no es «qué tablas hay», sino «qué tiene que ser '
    'cierto en los datos para que las reglas se cumplan siempre».',
    'Vas a usar lo que ya aprendiste en Algorítmica sobre entidades, relaciones y claves, y lo vas a aplicar a un '
    'problema que allí quedó abierto: un libro no es lo mismo que cada uno de sus ejemplares. De esa diferencia dependen '
    'la devolución correcta, el doble préstamo y el historial.',
]
ARTICULACION = [
    'Con Algorítmica 3.º: allí se enseñan el modelo entidad-relación, las claves, la integridad referencial y las formas '
    'normales. Acá no se vuelven a enseñar: se usan para justificar el modelo del proyecto.',
    'Con el Capítulo 6: se diseña para el catálogo v1.1, que incluye RF-11 (tipo de lector) y la regla RN-02 '
    'modificada por la solicitud SC-01.',
    'Con los Capítulos 8 y 9: las pantallas muestran estos datos y las operaciones hacen cumplir estas restricciones.',
]

# ------------------------------------------------------------------ encuentro 13
E13_TITULO = 'Encuentro 13 — Antecedentes de Algorítmica y modelo del dominio'

S71 = ('7.1 Recuperación aplicada de modelos de Algorítmica', [
    'En Algorítmica 3.º trabajaste con el modelo entidad-relación: entidades, relaciones, cardinalidades y claves. '
    'Este libro no lo vuelve a enseñar. Lo usa con la misma notación, para que el modelo del proyecto se lea como los que '
    'ya conocés. Si alguna idea no la recordás, la ficha de abajo dice dónde repasarla.',
    'El diagrama de este capítulo es una representación simplificada: muestra entidades, relaciones y cardinalidades, y '
    'deja los atributos para el diccionario de datos (7.3). Así se puede leer de un vistazo, y cada atributo queda '
    'explicado con su significado y con el requisito que lo pide.',
])
FICHA_RECUPERACION = ('Ficha de recuperación: lo que ya sabés de Algorítmica 3.º', [
    'Entidad: una cosa de la que se guardan datos. Relación: cómo se vinculan dos entidades. Cardinalidad: cuántos de un '
    'lado se vinculan con uno del otro (1 o N). Repaso: Algorítmica 3.º, Clases 11 a 14.',
    'Clave principal: el dato que identifica a cada fila sin repetirse. Clave foránea: el dato que apunta a otra '
    'entidad. Integridad referencial: no se puede apuntar a algo que no existe. Repaso: Clases 8 y 9.',
    'Paso del diagrama a las tablas y anomalías de una tabla mal armada. Repaso: Clases 15 a 17.',
    'Lo nuevo de este capítulo: que cada decisión del modelo se justifique con una regla, un requisito o un hecho del '
    'dossier.',
])
LEYENDA_DER = 'Tabla 7.1 — Símbolos del modelo entidad-relación (notación de Algorítmica 3.º)'

S72 = ('7.2 Obra/edición, ejemplar, lector y préstamo: identidad y responsabilidad', [
    'Para el lector, «Cuentos del arroyo Arapoty» es un libro. Para la biblioteca, en cambio, hay tres cosas distintas. '
    'La obra es el título de un autor: lo que se busca. La edición es una publicación concreta de esa obra, con su '
    'editorial y su año. El ejemplar es cada libro físico, con su etiqueta: lo que se presta y lo que vuelve. De una '
    'obra puede haber varias ediciones, y de cada edición, varios ejemplares.',
    'El préstamo es siempre de un ejemplar, nunca de una obra. El dossier muestra por qué. Cuando en el cuaderno se anota '
    'solo el título, al volver un ejemplar no se sabe de qué préstamo es (E4-L2), y el mismo libro puede quedar anotado a '
    'dos lectores (E4-L4). Con el código del ejemplar, cada devolución cierra su propio préstamo y la regla RN-01 se puede '
    'comprobar.',
    'Cada entidad tiene una identidad y un responsable. La identidad es lo que la distingue de las demás, aunque cambien '
    'sus otros datos. El lector se identifica con un código interno y no con la cédula: la cédula no hace falta para '
    'prestar y es un dato personal que conviene no guardar (E5-L6, RNF-03). El responsable es quién la crea o la '
    'cambia: la bibliotecaria cataloga y registra lectores, y el sistema crea los préstamos cuando ella presta.',
])
LEAD_FIG71 = ('La Figura 7.1 muestra el modelo del núcleo. Leé cada relación en los dos sentidos: «una obra tiene N '
              'ediciones» y «cada edición es de una obra». Parámetro y Cuenta no se relacionan con las demás: guardan las '
              'reglas que pueden cambiar y los permisos.')
EPI_FIG71 = 'Figura 7.1 — Modelo de datos del núcleo (representación simplificada; los atributos están en el diccionario).'
TABLA_72_ROTULO = 'Tabla 7.2 — Entidades del núcleo: qué representan, cómo se identifican y quién responde'
TABLA_72 = (['Entidad', 'Qué representa', 'Se identifica por', 'Quién la crea o la cambia', 'Requisitos'],
            [[e, q, i, r, ', '.join(rq)] for e, q, i, r, rq in X.ENTIDADES])
LEAD_FIG72 = ('En la Figura 7.2, una obra tiene dos ediciones y cuatro ejemplares. La consulta pública cuenta los '
              'disponibles de toda la obra; el préstamo y la devolución usan el ejemplar.')
EPI_FIG72 = 'Figura 7.2 — Una obra, sus ediciones y sus ejemplares físicos (datos ficticios).'

EJ71 = ('Ejemplo resuelto 7.1: por qué el préstamo es de un ejemplar', [
    'Consigna: la docente del plan lector pidió treinta ejemplares de la misma novela (E2-L2). Explicar qué pasa con la '
    'devolución si el préstamo se guarda por título y qué cambia si se guarda por ejemplar.',
    'Por título: treinta préstamos dicen «la misma novela». Cuando vuelven veintinueve, no se sabe qué lector no devolvió, '
    'porque cualquier libro devuelto «sirve» para cualquier préstamo. Es el problema de E4-L2, multiplicado por treinta.',
    'Por ejemplar: cada préstamo tiene un código de ejemplar distinto. Cada devolución cierra el préstamo de ese ejemplar '
    '(RF-03). El que falta tiene nombre y apellido: es el préstamo que sigue sin fecha de devolución.',
    'Consecuencia en el modelo: Préstamo se relaciona con Ejemplar, y Ejemplar con Edición y Obra. La consulta de '
    'disponibilidad (RF-07) cuenta ejemplares, pero muestra obras.',
])
EJ72 = ('Ejemplo resuelto 7.2: el lector, su tipo y su curso', [
    'Consigna: decidir qué datos del lector hacen falta con el catálogo v1.1 y qué pasa con el curso de los docentes.',
    'La solicitud SC-01 agregó RF-11: el sistema tiene que saber si cada lector es estudiante o docente, porque el máximo '
    'depende del tipo (RN-02 v1.1: dos y cinco). El tipo es un dato propio del lector, no una parte del curso.',
    'El curso se exige a los estudiantes y queda vacío para los docentes (RI-06). Anotar «Docente» en el lugar del curso, '
    'como pasa hoy en el cuaderno, mezcla dos datos y ensucia el informe.',
    'El informe por curso (RF-09) agrupa los préstamos de los estudiantes por su curso, y los de los docentes en una fila '
    'propia, «Docentes», como ya hace el informe de marzo (D2-7). Nunca hace falta inventar un curso para un docente.',
])

ACT_E13 = [
    ('Ejercitá', [
        'Indicá si cada dato es de la obra, de la edición, del ejemplar o del préstamo:\n'
        '(a) el autor; (b) el año de publicación; (c) la etiqueta pegada en el lomo; (d) la fecha de vencimiento; '
        '(e) el título; (f) que el libro está inactivo.',
    ]),
    ('Resolvé', [
        'Con la Figura 7.1, escribí las cuatro relaciones en las dos direcciones, como en el ejemplo: «un lector pide N '
        'préstamos; cada préstamo es de un lector».',
        'Releé E4-L6 y RN-06. Explicá por qué el lector necesita un estado (activo o inactivo) y qué pasaría con su historial '
        'si en lugar de eso se lo borrara.',
    ]),
    ('Pensá y decidí', [
        'Un compañero propone identificar al lector con su cédula «porque no se repite». Escribí dos razones del dossier o del '
        'catálogo para usar un código interno.',
    ]),
    ('Desafío', [
        'La biblioteca recibe un diccionario en dos tomos que se prestan por separado. ¿Es una obra con dos ejemplares, o dos '
        'obras? Proponé cómo modelarlo y qué consecuencia tiene en la consulta de disponibilidad.',
    ]),
]

# ------------------------------------------------------------------ encuentro 14
E14_TITULO = 'Encuentro 14 — Integridad, historial y diccionario'

S73 = ('7.3 Relaciones, restricciones, historial y diccionario de datos', [
    'Las reglas de préstamo no se cumplen solas: el modelo tiene que hacer imposible lo que una regla prohíbe. Una '
    'restricción de integridad es una condición que los datos tienen que cumplir siempre. Cada una sale de una regla o de '
    'un requisito, y se escribe en el diccionario para que nadie la olvide al construir.',
    'El historial se conserva. Devolver no borra el préstamo: le pone la fecha de devolución (RN-05). Un lector o un '
    'ejemplar con préstamos en su historia no se borra: se inactiva (RN-06). Algorítmica 3.º muestra cómo una base puede '
    '«eliminar en cascada»; en este proyecto, esa opción violaría dos reglas acordadas, porque borraría lo que la '
    'biblioteca necesita conservar.',
    'Algunos datos no se guardan: se calculan cuando hacen falta. Si un ejemplar está disponible depende de sus préstamos '
    'sin devolución; si se guardara aparte, tarde o temprano los dos datos dirían cosas distintas. Otros datos sí conviene '
    'guardarlos aunque se puedan calcular: el vencimiento se calcula al prestar con el plazo de ese día, y se guarda, para '
    'que un cambio de plazo no altere los préstamos ya hechos.',
    'Las cifras de las reglas van en Parámetro y no escritas dentro del programa. Por eso RF-02 dice «plazo vigente» y '
    'RF-05 dice «máximo vigente»: cuando la dirección cambió el máximo de los docentes (SC-01), alcanzó con cambiar un '
    'valor.',
])
TABLA_73_ROTULO = 'Tabla 7.3 — Restricciones de integridad del modelo'
TABLA_73 = (['Código', 'Restricción', 'Sale de'], [[c, t, ', '.join(f)] for c, t, f in X.RESTRICCIONES])
LEAD_FIG73 = ('La Figura 7.3 sigue a un ejemplar durante un mes: tres préstamos, dos cerrados y uno activo. Ninguno se '
              'borra, y nunca hay dos activos a la vez.')
EPI_FIG73 = 'Figura 7.3 — Historial de un ejemplar (datos ficticios).'
TABLA_74_ROTULO = 'Tabla 7.4 — Datos que se calculan y parámetros que se guardan'
TABLA_74 = (['Dato', 'Cómo se obtiene', 'Requisito', 'Por qué'],
            [list(d) for d in X.DERIVADOS] + [['Parámetro %s = %s' % (n, v), 'Se guarda; lo cambia la bibliotecaria cuando cambia la regla', r, q] for n, v, r, q in X.PARAMETROS])
DICCIONARIO_ROTULO = 'Tabla 7.5 — Diccionario de datos del núcleo'
DICCIONARIO = (['Entidad', 'Campo', 'Significado', 'Obligatorio', 'Ejemplo', 'Origen'], [list(r) for r in X.DICCIONARIO])

EJ73 = ('Ejemplo resuelto 7.3: un contraejemplo para cada restricción', [
    'Consigna: revisar el modelo con ejemplos que deberían aceptarse y contraejemplos que deberían rechazarse.',
    'RI-01. Contraejemplo: el ejemplar EJ-0457 tiene el préstamo 1103 sin devolución y se intenta registrar otro. El '
    'modelo lo rechaza: el ejemplar ya tiene un préstamo sin fecha de devolución.',
    'RI-02. Contraejemplo: una docente con cinco préstamos activos pide otro. Se rechaza, porque el máximo de los docentes '
    'es cinco (RN-02 v1.1). Ejemplo válido: un estudiante con un préstamo activo pide otro; se acepta, porque su máximo es dos.',
    'RI-04. Contraejemplo: la devolución borra el préstamo 1042. Se rechaza el diseño: la devolución completa la fecha y '
    'conserva el préstamo.',
    'RI-06. Contraejemplo: un estudiante sin curso. El diccionario lo marca obligatorio para estudiantes. Ejemplo válido: un '
    'docente sin curso.',
    'Revisar con contraejemplos es una forma de verificar el diseño antes de construirlo: articula este capítulo con la '
    'verificación de la Unidad V.',
])

S74 = ('7.4 Revisión de normalización con ejemplos del proyecto', [
    'En Algorítmica 3.º viste por qué una tabla mal armada produce anomalías y cómo se corrigen. Acá se aplica esa '
    'revisión a los datos reales del proyecto: el cuaderno de préstamos, que según el reglamento anota en una línea el '
    'nombre del lector, su curso, el título y la fecha (D1-A4).',
    'La Tabla 7.6 copia cuatro líneas de un cuaderno como ese. Cada problema que se ve ahí ya apareció en el dossier, y '
    'cada uno tiene una corrección en el modelo de este capítulo (Tabla 7.7). No hace falta nombrar las formas '
    'normales: alcanza con encontrar la anomalía, decir qué la causa y mostrar qué parte del diseño la evita.',
])
TABLA_75_ROTULO = X.CUADERNO_ROTULO
TABLA_75 = X.CUADERNO
TABLA_ANOM_ROTULO = 'Tabla 7.7 — Anomalías del cuaderno y cómo las evita el modelo'
TABLA_ANOM = (['Anomalía', 'Dónde se ve', 'Cómo la evita el modelo'], [list(a) for a in X.ANOMALIAS])
EJ74 = ('Ejemplo resuelto 7.4: el informe por curso sin datos inventados', [
    'Consigna: mostrar cómo se obtiene con el modelo un informe mensual como el de marzo (D2, RF-09), sin la fila «Sin curso '
    'anotado» de D2-8 y sin la suma a mano que no cerraba (D2-9, E4-L12).',
    'Cada préstamo de un estudiante guarda el curso que tenía ese día (RI-08). Si el estudiante cambia de curso en julio, '
    'el informe de abril no cambia.',
    'Los préstamos de los docentes no tienen curso: el informe los cuenta por su tipo de lector, en la fila «Docentes».',
    'El total se vuelve a contar en los préstamos del mes, no se suma a mano: así siempre coincide con las filas.',
    'Resultado: la Tabla 7.8, con los préstamos de abril, el primer mes con el sistema. Ningún préstamo queda sin grupo, y a '
    'ningún docente se le inventó un curso. Los seis préstamos sin curso de marzo no se pueden reconstruir: el sistema '
    'evita que vuelva a pasar, no corrige el cuaderno viejo.',
])
TABLA_76_ROTULO = X.INFORME_ROTULO
TABLA_76 = X.INFORME

ACT_E14 = [
    ('Ejercitá', [
        'Para cada caso, indicá qué restricción de la Tabla 7.3 lo rechaza:\n'
        '(a) un préstamo a un lector inactivo;\n'
        '(b) un estudiante con dos préstamos activos que pide un tercero;\n'
        '(c) borrar un ejemplar que se prestó tres veces;\n'
        '(d) un estudiante registrado sin curso.',
    ]),
    ('Resolvé', [
        'Escribí en el formato del diccionario (Tabla 7.5) un campo nuevo que haga falta para la regla RN-04, o explicá por qué '
        'el diccionario ya lo tiene.',
        'Para RI-03 y RI-05, escribí un ejemplo que debería aceptarse y un contraejemplo que debería rechazarse.',
    ]),
    ('Pensá y decidí', [
        'Alguien propone guardar en el ejemplar un campo «disponible: sí o no» para que la consulta sea más rápida. ¿Qué '
        'riesgo tiene? ¿Qué condición tendría que cumplirse siempre para que no se contradiga con los préstamos?',
    ]),
    ('Desafío', [
        'La dirección decide que desde abril el plazo sea de diez días. Explicá qué pasa con los préstamos de marzo, qué dato '
        'cambia y por qué el diseño de RI-07 evita que cambien vencimientos ya comunicados.',
    ]),
]

# ------------------------------------------------------------------ práctica
PRACTICA_TITULO = 'Práctica 7 — Justificar el modelo de otra biblioteca frente a pérdida, devolución y duplicación'
PRACTICA_INTRO = [
    'Volvés a la Escuela Básica Mbokaja. La biblioteca va a tener una computadora (M-F7) y ya acordó los requisitos MR-01 '
    'a MR-08 (Práctica 5). Hay datos y situaciones nuevas, que no aparecen en ningún ejemplo de este capítulo: un ejemplar '
    'perdido y repuesto, y un préstamo cargado dos veces.',
]
NIVELES = [
    ('Nivel 1 — Guiado', [
        'Dibujá el modelo de Mbokaja con obra, edición, ejemplar, lector y préstamo, en la notación de la Figura 7.1. Usá '
        'M-F8 para decidir si hace falta distinguir ejemplares.',
        'Explicá con tu modelo dónde queda registrado MS-3: el ejemplar perdido, el ejemplar que lo reemplaza y el préstamo '
        'que no se devolvió. Ningún dato se borra.',
    ]),
    ('Nivel 2 — Intermedio', [
        'Escribí el diccionario de las entidades Ejemplar y Préstamo de Mbokaja (campo, significado, obligatorio, ejemplo y '
        'origen MR, V o M).',
        'Proponé la restricción que impide MS-4 (el mismo préstamo cargado dos veces) y un contraejemplo que la ponga a prueba. '
        'Explicá por qué no alcanza con pedirles cuidado a los voluntarios.',
    ]),
    ('Nivel 3 — Ampliación', [
        'V-11 muestra fichas sin la devolución anotada. Explicá cómo tu modelo distingue un libro que sigue prestado de uno que '
        'volvió y nadie registró, y qué decisión tendría que tomar el encargado con los casos viejos.',
        'Si en la Práctica 6 se aceptó MC-1 (docentes con un mes de plazo), indicá qué cambia en tu modelo: entidades, campos, '
        'parámetros y restricciones.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: cada préstamo es de un ejemplar; ningún dato con historia se borra; cada restricción '
                    'cita una norma M-N, un requisito MR o una situación MS; el diccionario tiene el origen de cada campo; '
                    'la restricción contra la doble carga se prueba con un contraejemplo.')

REPASO = ('Para repasar', [
    'La obra es lo que se busca; el ejemplar, lo que se presta. Cada préstamo es de un ejemplar.',
    'Cada entidad tiene una identidad (su código) y un responsable (quién la crea o la cambia).',
    'Las reglas se convierten en restricciones de integridad; el historial no se borra: se cierra o se inactiva.',
    'Lo que se puede calcular, como la disponibilidad, no se guarda; las cifras de las reglas van en parámetros.',
    'El diccionario explica cada dato y dice qué requisito lo pide. El curso es de los estudiantes; el tipo de lector, de todos.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, este capítulo conserva sus dos encuentros: el modelo de datos sostiene todo el '
    'prototipo.',
    'Si aun así se pierde tiempo, no se omiten: la Figura 7.1, el Ejemplo resuelto 7.1, la Tabla 7.3 y el Ejemplo resuelto '
    '7.3. Pasan a lectura domiciliaria: la sección 7.4 y el Desafío de cada encuentro.',
])

# ------------------------------------------------------------------ evaluación
EVAL_ID = 'ADS3-L3-C7'
EVAL_TITULO = 'Evaluación del Capítulo 7'
EVAL_TEXTO_BASE = ('Texto base — Reserva de espacios del colegio (situación de evaluación, ficticia)', [
    'X-1 El colegio reserva tres espacios: el salón de actos, la sala de video y el laboratorio.',
    'X-2 Un docente reserva un espacio para una fecha y una franja (primera, segunda o tercera hora).',
    'X-3 Un espacio no puede tener dos reservas en la misma fecha y franja.',
    'X-4 Si se cancela una reserva, la coordinación quiere saber quién la canceló y cuándo.',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', '¿Por qué el préstamo de la biblioteca se vincula al ejemplar y no a la obra?',
     ['Porque así cada devolución cierra el préstamo de ese libro físico.',
      'Porque la obra no tiene título.',
      'Porque así se ocupa menos espacio.',
      'Porque los lectores buscan ejemplares.']),
    ('mc', '¿Cuál de estos datos conviene calcular en lugar de guardar?',
     ['Si un ejemplar está disponible.',
      'El autor de una obra.',
      'La fecha de salida de un préstamo.',
      'El tipo de lector.']),
    ('mc', 'En el texto base, X-3 es…',
     ['una restricción de integridad.',
      'una entidad.',
      'un dato derivado.',
      'una solución técnica.']),
    ('mc', '¿Qué se guarda en el curso de un docente que es lector de la biblioteca?',
     ['Nada: el curso queda vacío y el tipo de lector dice que es docente.',
      'La palabra «Docente».',
      'El curso en el que más enseña.',
      'Un curso cualquiera, para que el informe cierre.']),
    ('vf', 'Al registrar una devolución, se borra el préstamo para que el ejemplar quede libre.',
     False, 'Falso. Se completa la fecha de devolución y el préstamo queda en el historial (RN-05).'),
    ('vf', 'El diccionario de datos dice, para cada campo, qué significa y de qué requisito sale.',
     True, 'Verdadero. También dice si es obligatorio y da un ejemplo.'),
    ('vf', 'Si cambia el plazo vigente, hay que recalcular el vencimiento de los préstamos ya hechos.',
     False, 'Falso. El vencimiento se calcula al prestar y se guarda (RI-07): los préstamos hechos no cambian.'),
    ('ab', 'Con el texto base, nombrá las entidades y las relaciones del modelo, con su cardinalidad. Podés dibujarlo.',
     'Entidades: Espacio, Docente, Reserva (y Franja, si se la modela aparte). Relaciones: un espacio tiene N reservas; un '
     'docente hace N reservas; cada reserva es de un espacio, de un docente, en una fecha y una franja. Un punto por cada '
     'entidad bien elegida (hasta 2) y uno por cada relación con su cardinalidad (hasta 2).', 4),
    ('ab', 'Explicá cómo registrar la cancelación (X-4) sin perder el historial, y escribí X-3 como restricción.',
     'La cancelación no borra la reserva: le agrega quién la canceló y la fecha, y la reserva queda cancelada. Restricción: '
     'un espacio tiene, como máximo, una reserva no cancelada por fecha y franja. Un punto por no borrar, uno por quién, uno '
     'por cuándo y uno por la restricción, que tiene que excluir las canceladas.', 4),
]
EVAL_PUNTAJE = ('Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno). '
                'Es opcional: puede reemplazarse por la evidencia de la Práctica 7.')

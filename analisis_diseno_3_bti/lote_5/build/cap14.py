# -*- coding: utf-8 -*-
"""Capítulo 14 — «Probar con criterios y datos independientes» (Work §6: secciones 14.1 a 14.4 y práctica «elaborar y
ejecutar una batería nueva de pruebas»; encuentros 27 y 28).

Decisiones de Fernando (21-oct-2026): datos de prueba independientes (DP) con un cargador que crea una copia
descartable, reproducible y que no sobrescribe; una parte de DP se carga a mano con las operaciones del equipo. Cada
prueba registra requisito, esperado, obtenido, entorno y evidencia; se distinguen resultados comprobados, incidencias
reproducidas, simulaciones y pendientes. Doce casos o más por equipo, seis de ellos rechazos o límites (C9, Work §4.2).
El «obtenido» de la matriz del equipo modelo sale de la ejecución real (build/reproducir.py). Capacidades de Work
§5.2: C9 (Encuentro 27) y C8 y C9 (Encuentro 28)."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'caso'))
import verificacion as V
import datos_prueba_u5 as DP
import mbokaja_u5 as MB
C4, X = V.C4, V.X

NUM = 14
UNIDAD = 'Unidad V — Verificar, validar y mejorar'
CAPITULO = 'Capítulo 14'
TITULO = 'Probar con criterios y datos independientes'
ENCUENTROS = (27, 28)
SECCIONES = ['14.1 Verificación, validación y aceptación',
             '14.2 Casos normales, límites, excepciones y rechazos',
             '14.3 Resultado esperado, resultado obtenido y evidencia',
             '14.4 Cobertura de requisitos y reporte de defectos']
PRACTICA_WORK = 'elaborar y ejecutar una batería nueva de pruebas'

ROTULO_CAPACIDAD = ('Capacidades propuestas para el programa institucional (C9 en el Encuentro 27; C8 y C9 en el '
                    'Encuentro 28; no son capacidades oficiales del MEC)')
CAPACIDAD = ('C8. Integra un prototipo funcional con persistencia.\n'
             'C9. Verifica y mejora la solución a partir de evidencia.')
TEMA = ('Verificación, validación y aceptación. Clases de casos: normales, límites, excepciones y rechazos, elegidos desde '
        'las reglas. Datos de prueba independientes en una copia descartable. Resultado esperado, obtenido, entorno y '
        'evidencia. Cobertura de los requisitos y reporte de defectos con su condición.')
INDICADORES = [
    'Distingue verificar, validar y aceptar, y dice contra qué se compara cada una.',
    'Diseña al menos doce casos identificados desde las reglas, seis de ellos de límite o de rechazo.',
    'Prepara una copia descartable con datos independientes y comprueba su estado antes de probar.',
    'Ejecuta los casos y registra requisito, esperado, obtenido, entorno y evidencia, sin dar por bueno lo que no se probó.',
    'Encuentra los huecos de cobertura y reporta cada defecto con pasos para reproducirlo y su condición.',
]
TIEMPO = ('Dos encuentros de 5 HC (27 y 28 de la secuencia anual), las diez de verificación: el taller es diseñar, '
          'ejecutar y registrar pruebas.')

APERTURA = [
    'El prototipo funciona. Pero «funciona» no es una prueba: es una impresión. En esta unidad el equipo demuestra qué '
    'funciona, contra qué criterio y con qué evidencia, y encuentra lo que no funciona antes de que lo encuentre la '
    'bibliotecaria.',
    'Las pruebas de la Unidad IV se hicieron con los datos de los ejemplos. Ahora se prueba con datos nuevos, que nadie usó '
    'para construir, y con los casos más incómodos: los bordes de cada regla y las operaciones que el sistema tiene que '
    'rechazar.',
]
ARTICULACION = [
    'Con el Capítulo 4: cada requisito tiene su criterio de aceptación; las pruebas previstas P-01 a P-15 son el punto de '
    'partida de la matriz.',
    'Con el Capítulo 13: la lista de incidencias del H4 se revisa, y cada una recibe su condición.',
    'Con Laboratorio de 3.º (p. 58: pruebas, TDD e integración continua): acá no se enseña una herramienta de pruebas; se '
    'diseñan casos con criterio y se registra la evidencia.',
]

AVISO_ENTORNO = C4.AVISO_ENTORNO

# ------------------------------------------------------------------ encuentro 27
E27_TITULO = 'Encuentro 27 — Cobertura y datos independientes'

S141 = ('14.1 Verificación, validación y aceptación', [
    'Verificar es comprobar que el sistema hace lo que dicen el requisito y el contrato: si el contrato de OP-01 dice que '
    'un segundo préstamo del mismo ejemplar responde ME-03, se prueba que responda ME-03. Validar es comprobar que eso '
    'resuelve la necesidad del dossier: que la bibliotecaria ya no entrega el mismo libro a dos lectores. Aceptar es '
    'comprobar los criterios acordados con quien pidió el sistema.',
    'Se pueden cumplir unas y no otras. Un sistema puede pasar todas sus pruebas y no servir, porque el requisito estaba mal '
    'o incompleto: por eso la validación mira la necesidad, no el código. La Tabla 14.1 sigue la cadena de trazabilidad '
    'de Work §7.3, del pedido de la bibliotecaria a la prueba P-07.',
])
TABLA_141_ROTULO = 'Tabla 14.1 — Verificar, validar y aceptar: la cadena de RF-04'
TABLA_141 = (['Pregunta', 'Contra qué se compara', 'En el caso Arapoty'],
             [['¿Hace lo que dice el requisito? (verificar)', 'Requisito y contrato', 'RF-04 y el contrato de OP-01: la segunda solicitud responde ME-03 (C-06)'],
              ['¿Resuelve la necesidad? (validar)', 'La necesidad y la regla del dossier', 'N-02 y RN-01: no se entrega el mismo ejemplar a dos lectores'],
              ['¿Cumple lo acordado? (aceptar)', 'El criterio de aceptación', 'Se rechaza la solicitud y se conserva el préstamo existente (consulta del estado final)'],
              ['¿Con qué evidencia?', 'Esperado, obtenido, entorno', 'Matriz C-06 y prueba de pedidos simultáneos P-07 (Capítulo 12)']])
EJ141 = ('Ejemplo resuelto 14.1: verificado, pero no validado', [
    'Consigna: el informe de un mes sin préstamos muestra «Total 0» (C-19). ¿Es un defecto?',
    'Verificación: el contrato de OP-05 v1.1 dice «los préstamos del mes agrupados por curso, la fila Docentes y el total». '
    'Con un mes vacío, eso es una tabla sin filas y total 0. Lo hace: está verificado.',
    'Validación: en una sesión de uso, la dirección pensó que el sistema había fallado (Capítulo 15). La necesidad, saber '
    'cuánto se leyó, se cumple, pero el mensaje no ayuda.',
    'Conclusión: no es un incumplimiento del contrato. Es una mejora, que se pide con una solicitud de cambio (SC-02, '
    'Capítulo 16). Confundirlo con un defecto haría creer que el equipo programó mal algo que estaba bien especificado.',
])

S142 = ('14.2 Casos normales, límites, excepciones y rechazos', [
    'Un caso de prueba se elige, no se inventa. Cada regla del sistema tiene un borde: el máximo de préstamos, el día del '
    'vencimiento, el formato del código. Los errores se esconden en los bordes, así que los casos de límite se ponen a los '
    'dos lados: el último que se acepta y el primero que se rechaza (Figura 14.1).',
    'Las clases de casos son cuatro (Tabla 14.2). Una batería sirve si tiene de todas: con solo casos normales, el sistema '
    'parece perfecto. Work pide al menos doce casos por equipo y seis de rechazo o de límite.',
    'Los datos de prueba tienen que ser independientes: no los que se usaron para construir, porque con esos el sistema ya '
    'sabe responder. El conjunto DP (Tablas 14.3 y 14.4) tiene obras, ejemplares, lectores y préstamos nuevos, preparados '
    'para que cada borde se pueda probar: un estudiante en su máximo, una docente a un préstamo del suyo, un préstamo que '
    'vence el mismo día de la fecha de referencia, un ejemplar dado de baja con historial y títulos con «%» y «_».',
])
TABLA_142_ROTULO = 'Tabla 14.2 — Clases de casos de prueba'
TABLA_142 = (['Clase', 'Qué prueba'], [list(c) for c in V.CLASES])
LEAD_FIG141 = 'La Figura 14.1 muestra cómo se eligen los casos alrededor del máximo de préstamos de un estudiante.'
EPI_FIG141 = 'Figura 14.1 — Casos a los dos lados del límite de RF-05 (máximo de dos préstamos de un estudiante).'
TABLA_143_ROTULO = 'Tabla 14.3 — Conjunto de prueba DP: lo que carga el cargador (datos ficticios)'
_esp = DP.estado_esperado()
TABLA_143 = (['Dato', 'Qué hay', 'Para probar'],
             [['Obras y ediciones', '%d obras, %d ediciones; OB-1003 «Diccionario 100%% escolar», OB-1004 «Juegos_de_patio»' % (len(DP.OBRAS), len(DP.EDICIONES)), 'La búsqueda con comodines (C-13, C-14)'],
              ['Ejemplares', '%d; EJ-1006 dado de baja, con un préstamo en su historial' % len(DP.EJEMPLARES), 'RI-03 y RI-05 (C-08)'],
              ['Lectores', 'LE-1001 y LE-1002 (estudiantes), LE-1003 (docente), LE-1004 (inactivo), LE-1005 (cambió de curso)', 'RI-02, RI-03 y RI-08'],
              ['Préstamos activos', '%d: LE-1001 tiene 1, LE-1002 tiene 2 (su máximo), LE-1003 tiene 4' % _esp['prestamos_activos'], 'Los límites de RF-05 (C-01, C-03 a C-05)'],
              ['Vencimientos', 'EJ-1001 vence el 11/05; EJ-1002, el 12/05 (la fecha de referencia)', 'El borde de RF-08 (C-12)'],
              ['Historial', 'LE-1005 retiró un libro en abril, cuando estaba en 1.º BTI', 'RI-08 en el informe (C-16)']])
TABLA_144_ROTULO = 'Tabla 14.4 — Parte manual de DP: la cargás con tus operaciones'
TABLA_144 = (['Operación', 'Entradas', 'Mensaje esperado'], [[m[0], ' · '.join(m[1]), m[2]] for m in DP.DP_MANUAL])
COPIA = ('Cómo se prepara la copia descartable', [
    'php cargar_dp.php --sistema=<carpeta de tu base> --destino=<carpeta nueva>',
    'El cargador copia el código de tu base a una carpeta nueva y crea ahí una base con DP. La base de la clase no cambia. '
    'Si la carpeta nueva ya existe, se niega y no cambia nada.',
    'Al terminar dice «Estado esperado: correcto» y una huella de los datos. Con los mismos datos, la huella es la misma en '
    'cualquier computadora: si la de tu equipo es otra, algo se cargó distinto y hay que averiguarlo antes de probar.',
    'Después cargá a mano la parte de la Tabla 14.4 con tus operaciones: esa carga también es una prueba.',
])
EJ142 = ('Ejemplo resuelto 14.2: los casos de límite de RF-05', [
    'Consigna: elegir los casos de límite del máximo de préstamos con los datos DP.',
    'Estudiantes (máximo 2): LE-1001 tiene 1 préstamo activo y pide otro: se registra (C-01). Después pide un tercero: '
    'ME-02 (C-03). Son los dos lados del borde.',
    'Docentes (máximo 5): LE-1003 tiene 4 y pide el quinto: se registra (C-04). Pide el sexto: ME-02 con el máximo de '
    'docentes (C-05).',
    'Por qué no alcanza con uno: si el sistema comparara «mayor que» en lugar de «mayor o igual», C-03 lo descubre, pero '
    'C-01 no. Hace falta el par.',
])
ACT_E27 = [
    ('Ejercitá', [
        'Clasificá cada caso como normal, límite, excepción o rechazo:\n'
        '(a) devolver un ejemplar prestado; (b) buscar «%»; (c) prestar a un lector inactivo; (d) devolver con una fecha '
        'anterior a la salida.',
    ]),
    ('Resolvé', [
        'Prepará la copia descartable de tu base con el cargador y anotá la huella que informa. Cargá a mano la parte de la '
        'Tabla 14.4 y anotá cada mensaje obtenido.',
        'Escribí la matriz de tu equipo con al menos doce casos: requisito, clase, entradas y resultado esperado, antes de '
        'ejecutar ninguno. Al menos seis tienen que ser de límite o de rechazo.',
    ]),
    ('Pensá y decidí', [
        'Un compañero propone probar con los datos de los ejemplos del libro «porque ya sabemos qué tienen». Explicá qué '
        'problema tiene.',
    ]),
]

# ------------------------------------------------------------------ encuentro 28
E28_TITULO = 'Encuentro 28 — Ejecutar, registrar y reportar'

S143 = ('14.3 Resultado esperado, resultado obtenido y evidencia', [
    'El resultado esperado se escribe antes de ejecutar; si no, se termina «esperando» lo que salió. El obtenido se anota '
    'tal como fue: el mensaje exacto y el estado de los datos, que se comprueba con una consulta de control (por ejemplo, '
    'que EJ-1001 siga con un solo préstamo activo). Y se anota el entorno: dónde se ejecutó, con qué versiones.',
    'Cada resultado tiene una condición (Tabla 14.5). «Comprobado» es lo que se ejecutó y quedó registrado. «Reproducido» '
    'es una incidencia que se volvió a provocar con pasos que se pueden repetir. «Simulado» es un dato de práctica. '
    '«Pendiente» es lo que todavía no se probó, como las pruebas en la computadora del colegio: no se da por bueno.',
    'La Tabla 14.6 es la matriz del equipo modelo, ejecutada de verdad sobre una copia con DP. Diecinueve casos coinciden. '
    'C-20 no: después de un error en el alta de un lector, la pantalla no conserva lo escrito. Es la incidencia IN-02, que '
    'se reproduce: el Capítulo 16 la corrige.',
])
TABLA_145_ROTULO = 'Tabla 14.5 — Condición de un resultado'
TABLA_145 = (['Condición', 'Qué significa'], [list(c) for c in V.CONDICIONES])
TABLA_146_ROTULO = 'Tabla 14.6 — Matriz del equipo modelo, ejecutada sobre la copia con DP (prototipo del lote 4)'


def tabla_146():
    return (['Caso', 'Req.', 'Clase', 'Esperado', 'Obtenido', 'Condición'], V.filas_matriz('v1_lote4'))


NOTA_146 = 'Entorno de la ejecución: %s. No es una computadora escolar.'
EJ143 = ('Ejemplo resuelto 14.3: registrar un caso completo', [
    'Consigna: registrar C-06 (RF-04, rechazo) como lo pide Work.',
    'Requisito: RF-04. Entradas: LE-1005 pide EJ-1001, que ya está prestado, con fecha 12/05. Esperado: ME-03 y EJ-1001 '
    'con un solo préstamo activo.',
    'Obtenido: ME-03; la consulta de control cuenta 1 préstamo activo de EJ-1001. Entorno: el de la Tabla 14.6. Evidencia: '
    'el archivo de resultados con la fecha.',
    'Condición: comprobado, en el entorno de construcción. En la computadora del colegio queda pendiente hasta que se '
    'ejecute ahí.',
])

S144 = ('14.4 Cobertura de requisitos y reporte de defectos', [
    'Cobertura es la respuesta a «¿qué requisitos probamos y cuáles no?». Se arma cruzando el catálogo con la matriz '
    '(Tabla 14.7). Un requisito sin caso es un hueco; uno con solo casos normales también es débil, porque nadie probó su '
    'borde. La matriz del equipo modelo tiene esos huecos: RF-01, RF-02 y RNF-03 solo tienen casos normales.',
    'Cuando un obtenido no coincide con el esperado, se reproduce otra vez y se escribe un reporte de defecto (Figura 14.2 y '
    'Tabla 14.8): qué pantalla y operación, qué requisito, los pasos exactos, el esperado, el obtenido, la gravedad, el '
    'entorno y la condición. Un buen reporte permite que otra persona vea el defecto sin preguntar nada.',
    'También se revisan las incidencias que quedaron de la Unidad IV (Tabla 14.9). No todas resultan lo que parecían: IN-01, '
    'tal como estaba escrita, no se reproduce, e IN-03 cumple el contrato. Por eso cada una lleva su condición.',
])
TABLA_147_ROTULO = 'Tabla 14.7 — Cobertura de los requisitos del catálogo v1.1 en la matriz del equipo modelo'


def tabla_147():
    return (['Req.', 'Prioridad', 'Casos', 'Límites y rechazos', 'Estado'], V.cobertura())


LEAD_FIG142 = 'La Figura 14.2 muestra el camino de un caso de prueba hasta un reporte de defecto.'
EPI_FIG142 = 'Figura 14.2 — Del caso de prueba al reporte de defecto, con su condición.'
TABLA_148_ROTULO = 'Tabla 14.8 — Reporte de defecto de IN-02 (equipo modelo)'
TABLA_148 = (['Campo', 'Contenido'], [list(r) for r in V.REPORTE_IN02])
TABLA_149_ROTULO = 'Tabla 14.9 — Incidencias de la Unidad IV, con su condición'
TABLA_149 = (['Código', 'Dónde', 'Qué pasa', 'Condición', 'Evidencia'], [list(i) for i in V.INCIDENCIAS_PARTIDA])
ACT_E28 = [
    ('Ejercitá', [
        'Para cada resultado, escribí su condición:\n(a) un caso que ejecutaste y dio lo esperado; (b) P-13 sin internet, que '
        'no pudiste hacer en el laboratorio; (c) un defecto que provocaste dos veces con los mismos pasos; (d) la semana de '
        'Mbokaja de la Práctica 13.',
    ]),
    ('Resolvé', [
        'Ejecutá la matriz de tu equipo sobre la copia descartable. Anotá obtenido, entorno y condición de cada caso, y la '
        'consulta de control de los que cambian datos.',
        'Armá la tabla de cobertura de tu equipo como la Tabla 14.7 y escribí un reporte de defecto completo para cada caso '
        'que no coincida.',
    ]),
    ('Pensá y decidí', [
        'Un caso dio «ME-04» cuando esperabas «ME-02». Un compañero propone cambiar el esperado «porque el sistema sabe lo '
        'que hace». Explicá qué hay que revisar antes.',
    ]),
    ('Desafío', [
        'Elegí uno de los huecos de la Tabla 14.7 (RF-01, RF-02 o RNF-03) y escribí dos casos de límite o de rechazo que lo '
        'cubran, con sus esperados.',
    ]),
]

# ------------------------------------------------------------------ práctica
PRACTICA_TITULO = 'Práctica 14 — Una batería nueva de pruebas para Mbokaja'
PRACTICA_INTRO = [
    'En Mbokaja, el encargado anota los feriados en el registro (M-F12), y hay situaciones nuevas (MS-7 y MS-8). Vas a '
    'diseñar y ejecutar una batería de pruebas con datos que no aparecen en ningún ejemplo.',
    'Se trabaja en una copia de práctica cargada con los datos de Mbokaja: php cargar_dp.php '
    '--datos=mbokaja_p14.json --sistema=<carpeta de tu base> --destino=<carpeta nueva>. %s Los niveles 1 y 2 se '
    'ejecutan en esa copia; el nivel 3 se resuelve en papel.' % MB.CORRESPONDENCIA_NOTA,
]
NIVELES = [
    ('Nivel 1 — Guiado', [
        'Escribí ocho casos para OP-01 y OP-04 con los datos de Mbokaja: requisito, clase, entradas y esperado. Incluí el '
        'segundo y el tercer préstamo de LE-0322 y el libro dado de baja (EJ-0305).',
        'Ejecutá los ocho casos en la copia de práctica y anotá obtenido, entorno y condición.',
    ]),
    ('Nivel 2 — Intermedio', [
        'Ampliá la batería a doce casos o más, seis de límite o de rechazo, e incluí MS-8 (la etiqueta MB-30). Ejecutalos y '
        'escribí un reporte de defecto para cada uno que no coincida.',
        'Pedí los préstamos activos con fecha de referencia 16 de julio. Con MS-7 y M-F12, ¿EJ-0301 tiene que figurar '
        'vencido? Decidí si es un defecto del sistema o una necesidad que el catálogo no tiene (verificar o validar).',
    ]),
    ('Nivel 3 — Ampliación (en papel)', [
        'Armá la tabla de cobertura de tu batería contra MR-01 a MR-08 de Mbokaja y señalá los huecos.',
        'Escribí la solicitud de cambio que haría falta para M-F12, con el formato de SC-01, y qué pruebas cambiarían.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: la copia se cargó con «Estado esperado: correcto»; cada caso tiene requisito, '
                    'esperado escrito antes, obtenido, entorno y condición; hay al menos seis límites o rechazos; el feriado '
                    'de M-F12 se trata como una necesidad sin requisito, no como un defecto del sistema.')

REPASO = ('Para repasar', [
    'Verificar compara con el requisito; validar, con la necesidad; aceptar, con los criterios acordados.',
    'Los casos se eligen desde las reglas, a los dos lados de cada borde; una batería tiene normales, límites, excepciones y rechazos.',
    'Los datos de prueba son independientes y se cargan en una copia descartable; la base de la clase no se toca.',
    'Cada prueba registra requisito, esperado, obtenido, entorno y evidencia, con su condición.',
    'La cobertura muestra los huecos; cada defecto se reporta con pasos para reproducirlo.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, los Encuentros 27 y 28 pasan a ser el 20 y el 21, sin cambios.',
    'No se reduce lo esencial: los doce casos con seis límites o rechazos, el registro completo de cada uno y los reportes de '
    'defecto. Pasan a lectura domiciliaria el Ejemplo resuelto 14.1 y el nivel 3 de la Práctica 14.',
])

# ------------------------------------------------------------------ evaluación
EVAL_ID = 'ADS3-L5-C14-c'
EVAL_TITULO = 'Evaluación del Capítulo 14'
EVAL_TEXTO_BASE = ('Texto base — Inscripción a talleres escolares (situación de evaluación, ficticia)', [
    'TA-1 Cada taller tiene un cupo máximo de 20 inscriptos.',
    'TA-2 Un estudiante no puede inscribirse dos veces en el mismo taller.',
    'TA-3 Solo la coordinación inscribe; los estudiantes consultan los cupos libres.',
    'TA-4 La inscripción cierra el viernes a las 12:00.',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', 'Para TA-1, ¿qué par de casos de límite conviene probar?',
     ['Con 19 inscriptos se acepta uno más; con 20, se rechaza.', 'Con 5 y con 10 inscriptos.',
      'Solo con el taller vacío.', 'Con 30 inscriptos.']),
    ('mc', 'El sistema inscribe bien, pero la coordinación necesitaba también una lista de espera que nadie pidió. ¿Qué falló?',
     ['La validación: el requisito no cubría la necesidad.', 'La verificación del código.', 'La base de datos.', 'El entorno.']),
    ('mc', 'Una prueba no se pudo ejecutar en la computadora del colegio. ¿Cómo se registra?',
     ['Pendiente, con el motivo.', 'Correcta, porque en otra computadora funcionó.', 'No se registra.', 'Falla del equipo.']),
    ('mc', '¿Qué hace falta en un reporte de defecto para que otra persona lo vea sin preguntar?',
     ['Los pasos exactos, el esperado, el obtenido y el entorno.', 'La opinión del equipo.', 'Solo el mensaje de error.',
      'El nombre de quien lo encontró.']),
    ('vf', 'El resultado esperado se puede escribir después de ejecutar, para no equivocarse.',
     False, 'Falso. Se escribe antes; si no, se espera lo que salió.'),
    ('vf', 'Probar con los mismos datos que se usaron para construir alcanza para una batería de pruebas.',
     False, 'Falso. Los datos tienen que ser independientes.'),
    ('vf', 'Inscribir dos veces al mismo estudiante en el mismo taller es un caso de rechazo (TA-2).',
     True, 'Verdadero. El sistema tiene que rechazarlo sin cambiar datos.'),
    ('ab', 'Escribí seis casos para la inscripción (TA-…): al menos dos de límite y dos de rechazo, cada uno con su '
           'requisito, entradas y resultado esperado.',
     'Por ejemplo: inscripción válida (normal); 19 → se acepta y 20 → se rechaza (límites, TA-1); inscripción repetida '
     '(rechazo, TA-2); inscripción de un estudiante (rechazo, TA-3); inscripción el viernes 12:01 (límite, TA-4). Un punto '
     'por los límites, uno por los rechazos, uno por las fuentes y uno por los esperados.', 4),
    ('ab', 'El caso «inscribir con 20 inscriptos» dio «inscripción registrada». Escribí el reporte de defecto completo.',
     'Pantalla y operación, requisito TA-1, pasos (taller con 20, inscribir uno más), esperado (rechazo con mensaje), '
     'obtenido (registrada), gravedad, entorno y condición (reproducido si se repitió). Un punto por pasos, uno por '
     'esperado y obtenido, uno por gravedad y entorno, uno por la condición.', 4),
]
EVAL_PUNTAJE = 'Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno).'

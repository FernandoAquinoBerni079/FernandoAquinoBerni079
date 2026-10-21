# -*- coding: utf-8 -*-
"""Capítulo 16 — «Corregir y volver a comprobar» (Work §6: secciones 16.1 a 16.4 y cierre «Revisión de unidad V:
evidencia de calidad y límites conocidos; H5»; encuentros 31 y 32).

Decisiones de Fernando (21-oct-2026): ejemplo central IN-02 (diagnóstico, reproducción, corrección, revisión entre pares
y regresión); IN-03 como ejemplo complementario de una solicitud de mejora SC-02, que no se presenta como
incumplimiento del contrato anterior; la corrección vive en una copia nueva de la referencia (lote_5/proyecto/), con la
del lote 4 intacta; el libro muestra los fragmentos necesarios y la guía, la solución completa. Sin práctica
independiente: el H5 es la actividad integradora (2 HC de evaluación, seis criterios, cuatro niveles, 60/40 como
propuesta editorial). Si un equipo no cumple una condición mínima, no se lo declara aprobado: se registra la recuperación.
Capacidades de Work §5.2: C7 a C9 (Encuentro 31) y C8 y C9 (Encuentro 32, H5)."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'caso'))
import verificacion as V
C4, X = V.C4, V.X

NUM = 16
UNIDAD = 'Unidad V — Verificar, validar y mejorar'
CAPITULO = 'Capítulo 16'
TITULO = 'Corregir y volver a comprobar'
ENCUENTROS = (31, 32)
SECCIONES = ['16.1 Diagnóstico de incidencias e impacto de cambios',
             '16.2 Corrección, revisión entre pares y regresión',
             '16.3 Actualización de modelos, pruebas y documentación',
             '16.4 Recuperación técnica y versión candidata']
REVISION_WORK = 'Revisión de unidad V: evidencia de calidad y límites conocidos; H5'
PRACTICA_WORK = None

ROTULO_CAPACIDAD = ('Capacidades propuestas para el programa institucional (C7 a C9 en el Encuentro 31; en el H5, C8 y '
                    'C9; no son capacidades oficiales del MEC)')
CAPACIDAD = ('C7. Organiza y registra el trabajo colaborativo.\n'
             'C8. Integra un prototipo funcional con persistencia.\n'
             'C9. Verifica y mejora la solución a partir de evidencia.\n'
             'En el H5 se evalúan C8 y C9.')
TEMA = ('Reproducción y diagnóstico de una incidencia: causa, capa e impacto. Corrección mínima, revisión entre pares y '
        'pruebas de regresión. Actualización de requisitos, contratos, mensajes y pruebas con una solicitud de cambio. '
        'Recuperación técnica, condiciones mínimas de aceptación y versión candidata con límites conocidos (H5).')
INDICADORES = [
    'Reproduce una incidencia con pasos que se repiten y distingue el síntoma de la causa y la capa.',
    'Estima el impacto de una corrección con la trazabilidad y elige las pruebas de regresión.',
    'Corrige con el cambio mínimo, hace revisar la corrección por otro integrante y ejecuta la regresión.',
    'Actualiza requisitos, contratos, mensajes, pruebas y bitácora cuando se aprueba un cambio, con su versión.',
    'Presenta una versión candidata con sus límites conocidos y revisa una por una las condiciones mínimas.',
]
TIEMPO = ('Dos encuentros de 5 HC (31 y 32 de la secuencia anual). Encuentro 31: 2 HC de práctica (corrección) y 3 de '
          'verificación (regresión). Encuentro 32: 2 HC de práctica (recuperación técnica), 1 de verificación y 2 de '
          'evaluación (H5).')

APERTURA = [
    'Las pruebas encontraron problemas. Ahora hay que corregirlos sin romper lo que andaba. Corregir no es tocar el código '
    'hasta que el error desaparezca: es entender por qué pasa, cambiar lo mínimo, pedirle a otro que lo revise y volver a '
    'probar todo lo que el cambio pudo afectar.',
    'Al final de la unidad, el equipo presenta una versión candidata: la mejor versión que tiene, con sus límites dichos '
    'con claridad. Esa versión y su evidencia de calidad son el hito H5.',
]
ARTICULACION = [
    'Con el Capítulo 6: una solicitud de cambio se tramita con el mismo formato que SC-01, con su impacto y su versión.',
    'Con el Capítulo 9: la capa de cada problema (Figura 9.1) dice dónde está la causa y qué más se puede ver afectado.',
    'Con la Unidad VI: la versión candidata es la que se documenta y se entrega a otro equipo en el Capítulo 17.',
]

AVISO_ENTORNO = C4.AVISO_ENTORNO

# ------------------------------------------------------------------ encuentro 31
E31_TITULO = 'Encuentro 31 — Diagnosticar, corregir y volver a probar'

S161 = ('16.1 Diagnóstico de incidencias e impacto de cambios', [
    'Lo primero es reproducir: seguir los pasos del reporte (Tabla 14.8) y ver el defecto otra vez. Si no se reproduce, no '
    'se corrige: se pide más información. IN-02 se reproduce siempre: prueba_in02.sh da 5 de 7 sobre el prototipo del lote '
    '4, y falla justo en lo que reporta (el tipo elegido y lo escrito se pierden).',
    'Después se distingue el síntoma de la causa. El síntoma es «el formulario aparece vacío». La causa está en la '
    'presentación: después de un envío, la página redirige (patrón POST-redirección-GET del Capítulo 12) y lo escrito no se '
    'guarda en ningún lado. Las reglas de negocio y los datos están bien: MV-04 se respondió y no se guardó nada.',
    'Por último, el impacto: qué más toca la corrección (Tabla 16.1). La redirección está en _plantilla.php, que usan todas '
    'las pantallas. Un cambio ahí puede afectar cualquier formulario, así que la regresión tiene que ser amplia.',
])
LEAD_FIG161 = 'La Figura 16.1 resume el ciclo de una corrección, desde que se reproduce hasta la versión nueva.'
EPI_FIG161 = 'Figura 16.1 — El ciclo de una corrección.'
TABLA_161_ROTULO = 'Tabla 16.1 — Impacto de la corrección de IN-02'
TABLA_161 = (['Elemento', 'Capa', 'Cambia', 'Por qué', 'Pruebas'],
             [['public/_plantilla.php: guardar_aviso()', 'Presentación', 'Sí', 'Guarda lo escrito si hubo error', 'prueba_http.sh (todas las pantallas)'],
              ['public/lectores.php: alta de lector', 'Presentación', 'Sí', 'Vuelve a mostrar lo guardado', 'prueba_in02.sh (nueva)'],
              ['OA-03 alta_lector() y validar_lector()', 'Reglas de negocio', 'No', 'Responden MV-03 y MV-04 bien', 'PA-03 (núcleo)'],
              ['Esquema y datos', 'Persistencia', 'No', 'No se guardó nada indebido', 'prueba_garantias.php'],
              ['Contratos, mensajes, catálogo', 'Documentación', 'No', 'RNF-01 ya lo pedía', '—']])
EJ161 = ('Ejemplo resuelto 16.1: síntoma, causa y capa', [
    'Consigna: separar síntoma, causa y capa de IN-02.',
    'Síntoma: después de MV-04, el formulario de alta de lector aparece vacío y con «Estudiante» elegido.',
    'Causa: la página redirige después de procesar el envío y no guarda lo que se escribió; el formulario se dibuja siempre '
    'vacío.',
    'Capa: presentación. Lo que NO es la causa: la validación (MV-04 es correcto) ni la base (no se guardó nada). Corregir '
    'la validación «para que no dé error» sería arreglar algo que no estaba roto.',
])

S162 = ('16.2 Corrección, revisión entre pares y regresión', [
    'La corrección es mínima: si la operación falló, guardar también lo escrito, sin la ficha CSRF ni la contraseña '
    '(Código 16.1), y que el formulario lo vuelva a mostrar, una sola vez (Código 16.2). No se cambia ninguna regla. La '
    'corrección completa está en la referencia docente v2, una copia nueva: la del lote 4 queda como estaba.',
    'Antes de integrarla, otro integrante la revisa con preguntas concretas (Tabla 16.2). Quien escribió el código no es el '
    'mejor para ver lo que se le escapó: la revisión entre pares busca lo que la prueba no mira.',
    'Después, la regresión: se vuelven a ejecutar la prueba nueva y todas las que el cambio pudo afectar (Tabla 16.3). Si '
    'una que pasaba ahora falla, la corrección introdujo un defecto y no se integra hasta resolverlo.',
])
CODIGOS_S162 = ['Código 16.1', 'Código 16.2']
EXPLICA = {
    'Código 16.1': 'guardar_aviso() recibe ahora también lo que se envió. Si la operación falló, lo guarda en la sesión '
                   'sin la ficha CSRF ni la contraseña; si salió bien, no guarda nada. Las demás pantallas siguen llamándola '
                   'como antes: el tercer dato es optativo.',
    'Código 16.2': 'Cada opción pregunta si era la elegida. Lo escrito se muestra escapado (con e()), como cualquier dato: '
                   'devolver lo que escribió una persona sin escapar sería un riesgo de seguridad.',
    'Código 16.3': 'Si el mes no tiene préstamos, el resultado es correcto, sin filas, con ME-14. Un mes con préstamos sigue '
                   'igual que antes.',
}
TABLA_162_ROTULO = 'Tabla 16.2 — Revisión entre pares de la corrección de IN-02'
TABLA_162 = (['Pregunta del revisor', 'Cómo se comprueba'],
             [['¿Lo escrito vuelve, con el tipo elegido?', 'prueba_in02.sh: casos 1 a 3'],
              ['¿Se guarda la contraseña o la ficha CSRF?', 'Se quitan antes de guardar; caso 4'],
              ['¿Se muestra una sola vez?', 'Al recargar, el formulario está vacío: caso 5'],
              ['¿Queda algo guardado después de un alta correcta?', 'Caso 6'],
              ['¿Un error de otro formulario llena este?', 'Cada formulario usa solo lo suyo: caso 7'],
              ['¿Lo escrito se muestra escapado?', 'Lectura del código: valor() usa e()'],
              ['¿Las demás pantallas siguen igual?', 'Regresión: prueba_http.sh completa']])
TABLA_163_ROTULO = 'Tabla 16.3 — Regresión de la corrección de IN-02 (referencia v2)'


def tabla_163():
    return (['Prueba', 'Resultado'], V.filas_regresion('v2'))


NOTA_163 = ('La misma prueba nueva sobre el prototipo del lote 4: %s (se reproduce IN-02). Entorno: %s.')
EJ162 = ('Ejemplo resuelto 16.2: elegir la regresión', [
    'Consigna: decidir qué pruebas se vuelven a ejecutar después de corregir IN-02.',
    'La prueba nueva, prueba_in02.sh, que tiene que pasar en la v2 y fallar en la versión anterior: así se sabe que prueba '
    'lo que dice.',
    'Las pantallas: la corrección tocó _plantilla.php, que usan todas. Se ejecuta el recorrido completo prueba_http.sh.',
    'El núcleo fijo (P-01, P-03, P-07 y P-11) y la matriz C-01 a C-20, aunque las reglas no cambiaron: la regresión no se '
    'achica por confianza. Resultado: todo coincide y C-20 pasa a «comprobado».',
])

S163 = ('16.3 Actualización de modelos, pruebas y documentación', [
    'Una corrección como la de IN-02 no cambia ningún requisito: RNF-01 ya pedía que la bibliotecaria pudiera trabajar sin '
    'ayuda. Se actualizan la prueba (prueba_in02.sh se suma a la batería), la bitácora y la versión del prototipo.',
    'Distinto es un cambio de lo acordado. IN-03, el informe de un mes vacío, no era un incumplimiento: el contrato de OP-05 '
    'v1.1 no pedía un mensaje para ese caso. La dirección lo pide como mejora, con la solicitud de cambio SC-02 (Tabla 16.4). '
    'Si se aprueba, cambian juntos el criterio de RF-09, el contrato de OP-05, la Tabla 8.6 con el mensaje nuevo ME-14, la '
    'pantalla PT-09 y la prueba P-09 (Código 16.3), cada uno con su versión.',
    'La trazabilidad queda completa: de cada requisito al defecto o al cambio, a la corrección y a la prueba que la '
    'comprueba (Tabla 16.6).',
])
TABLA_164_ROTULO = 'Tabla 16.4 — Solicitud de cambio SC-02'
TABLA_164 = (['Campo', 'Contenido'], [list(s) for s in V.SC02])
CODIGOS_S163 = ['Código 16.3']
TABLA_165_ROTULO = 'Tabla 16.5 — Regresión del cambio SC-02 (referencia v2 con SC-02)'


def tabla_165():
    return (['Prueba', 'Resultado'], V.filas_regresion('v2_sc02'))


TABLA_166_ROTULO = 'Tabla 16.6 — Trazabilidad requisito, defecto o cambio, corrección y prueba'
TABLA_166 = (['Requisito', 'Defecto o cambio', 'Corrección', 'Versión', 'Prueba'],
             [['RNF-01', 'IN-02 (reproducido)', '_plantilla.php y lectores.php', 'Referencia v2', 'prueba_in02.sh, C-20'],
              ['RF-09', 'SC-02 (mejora aprobada)', 'OP-05, PT-09, ME-14', 'Referencia v2 con SC-02; catálogo v1.2', 'P-09 (mes vacío), C-19'],
              ['RNF-01', 'IN-01 bis (reproducido)', 'Sin corregir', 'Límite conocido', '—']])
ACT_E31 = [
    ('Ejercitá', [
        'Para cada frase, decí si es síntoma, causa o capa:\n(a) «el formulario aparece vacío»; (b) «presentación»; (c) «la '
        'página redirige y no guarda lo escrito».',
    ]),
    ('Resolvé', [
        'Elegí la incidencia de mayor prioridad de tu equipo: reproducila, escribí su diagnóstico y su tabla de impacto, '
        'corregila con el cambio mínimo y pedí a otro integrante que la revise con preguntas como las de la Tabla 16.2.',
        'Ejecutá la regresión que corresponde y registrala como la Tabla 16.3, con el entorno.',
    ]),
    ('Pensá y decidí', [
        'Un compañero propone que, para que IN-02 «no vuelva a pasar», la validación no rechace nunca un docente con curso. '
        'Explicá qué problema tiene la propuesta.',
    ]),
    ('Desafío', [
        'Escribí una solicitud de cambio, con el formato de SC-02, para una mejora que haya aparecido en tus sesiones de uso.',
    ]),
]

# ------------------------------------------------------------------ encuentro 32 y H5
E32_TITULO = 'Encuentro 32 — Recuperación técnica y revisión de la Unidad V'

S164 = ('16.4 Recuperación técnica y versión candidata', [
    'El Encuentro 32 empieza con la recuperación técnica: cada equipo revisa, una por una, las condiciones mínimas de '
    'aceptación de Work §4.3 (Tabla 16.7). Si falta una, se usa ese tiempo para recuperarla. Si no se llega, el equipo no '
    'se declara aprobado en esa condición: se registra la recuperación pendiente, con qué falta y el procedimiento.',
    'La versión candidata es la que el equipo presenta en el H5: la mejor que tiene, con sus límites conocidos escritos '
    '(Tabla 16.8). Un límite conocido no es una falla escondida: es algo que el equipo sabe, probó o no pudo probar, y lo '
    'dice. Lo que no se probó en la computadora del colegio se anota como pendiente del entorno.',
])
TABLA_167_ROTULO = 'Tabla 16.7 — Condiciones mínimas de aceptación (Work §4.3) en la versión candidata del equipo modelo'


def tabla_167():
    r = V.resumen()
    i = r['integracion']['v2']
    reg = r['regresion']['v2']
    g = lambda p: reg[p]['resultado'].replace('Resultado: ', '')
    return (['Condición (Work §4.3)', 'Evidencia', 'Estado'],
            [['Circuito de préstamo y devolución ejecutable', 'Matriz %d de %d; prueba_http.sh %s' % (r['matriz']['v2']['correctos'], r['matriz']['v2']['total'], g('prueba_http.sh')), 'Comprobado'],
             ['Persistencia comprobada', 'Dos procesos (Tabla 15.1)', 'Comprobado' if i['persistencia'] else 'No'],
             ['Ninguna pérdida de historial', 'prueba_garantias.php %s; C-08' % g('prueba_garantias.php'), 'Comprobado'],
             ['Rechazo de préstamo simultáneo del mismo ejemplar', 'prueba_carrera.php %s (solo Linux)' % g('prueba_carrera.php'), 'Comprobado en Linux; pendiente en Windows'],
             ['Evidencia de pruebas', 'Matriz, regresión y resultados con su entorno', 'Comprobado'],
             ['Instalación y restauración reproducibles', 'Restauración comprobada (Tabla 15.1); instalación por otro equipo: Capítulo 17', 'Pendiente: instalación por otro equipo']])


TABLA_168_ROTULO = 'Tabla 16.8 — Límites conocidos de la versión candidata del equipo modelo'
TABLA_168 = (['Límite', 'Condición', 'Qué se hace'],
             [['Los demás formularios de PT-08 (obra, ejemplar, corrección, baja) no conservan lo escrito después de un error', 'Reproducido', 'Mismo patrón que IN-02; versión siguiente'],
              ['IN-01 bis: con la fecha vacía, «La fecha  no es válida», con un espacio doble', 'Reproducido', 'Prioridad baja; versión siguiente'],
              ['Pruebas en la computadora del colegio y en Windows (E-1 a E-12, P-13, concurrencia)', 'Pendiente', 'Ficha de entorno, con el responsable técnico'],
              ['Instalación por otro equipo siguiendo la guía', 'Pendiente', 'Capítulo 17 (Unidad VI)']])
RECUPERACION = ('Si falta una condición mínima', [
    'El equipo no se declara aprobado en esa condición. Se registra en la planilla: qué condición falta, qué evidencia hay, '
    'qué hay que hacer y quién lo hace.',
    'La recuperación se hace en el tiempo que la institución disponga: el Encuentro 32 la prevé en sus 2 HC de práctica. '
    'No se suponen horas extraordinarias de docentes ni de estudiantes que la institución no haya dispuesto.',
    'Un pendiente del entorno (por ejemplo, no poder probar en Windows) no es una falla del equipo: se registra como tal.',
])

H5_TITULO = 'Revisión de la Unidad V — Hito H5: evidencia de calidad y límites conocidos'
H5_TEXTO = [
    'El H5 es la revisión de la Unidad V, y en este capítulo es la actividad integradora: no hay una práctica aparte. Cada '
    'equipo presenta su versión candidata con su evidencia de calidad: la matriz de pruebas (doce casos o más, seis límites '
    'o rechazos) con esperado, obtenido, entorno y condición; los reportes de defecto; las dos sesiones de uso; el acta de '
    'aceptación; las correcciones con su regresión; y la tabla de límites conocidos.',
    'Durante la revisión, el docente le entrega a cada integrante un reporte de defecto nuevo. Cada estudiante explica, solo, '
    'la causa probable, la capa, el impacto, la corrección mínima y las pruebas de regresión. No hace falta programarla en '
    'el momento: se evalúa el razonamiento y la evidencia.',
]
H5_LISTA = ('Antes de presentar: lista de verificación del equipo', [
    '1. ¿La matriz tiene doce casos o más, seis de límite o de rechazo, cada uno con requisito, esperado, obtenido, entorno y condición?',
    '2. ¿Los datos son independientes y la copia se preparó con el cargador, con su huella anotada?',
    '3. ¿Se ejecutaron los permisos con las tres cuentas, la persistencia y la restauración?',
    '4. ¿Hay dos sesiones de uso registradas y un acta de aceptación con su evidencia?',
    '5. ¿Cada corrección tiene su diagnóstico, su revisión entre pares y su regresión?',
    '6. ¿La tabla de condiciones mínimas está completa, y lo que falta tiene su recuperación registrada?',
    '7. ¿Los límites conocidos están escritos, separados los pendientes del entorno de las fallas?',
    '8. ¿La bitácora tiene las versiones de la unidad y los aportes de cada integrante?',
])
H5_EVALUACION = ('Cómo se evalúa el H5', [
    'Se evalúan seis criterios, que cubren las capacidades C8 y C9, con los cuatro niveles de desempeño de los hitos '
    'anteriores: Sólido, Logrado, En desarrollo e Inicial. La rúbrica completa está en la guía docente.',
    'Cada criterio combina un 60 % de evidencia del producto del equipo y un 40 % de evidencia individual: la resolución de '
    'tu reporte de defecto, tu aporte registrado en la bitácora y la observación del docente. La proporción y los niveles '
    'son una propuesta editorial: la institución decide cómo se convierten en calificación.',
    'Si falta una evidencia, se registra como ausente y se acuerda cuándo entregarla; no se confunde con un desempeño de '
    'nivel inicial. Un pendiente del entorno no se cuenta como falla del equipo.',
])
RUBRICA_H5 = [
    ('Diseño y cobertura de pruebas', 'C9',
     ['Matriz con más de doce casos elegidos desde las reglas, a los dos lados de cada borde; cobertura explicada y huecos cerrados.',
      'Doce casos o más, seis de límite o de rechazo, con requisito; cobertura armada.',
      'Menos de doce casos o pocos límites; cobertura incompleta.',
      'Sin matriz o con casos sin requisito.'],
     'Matriz requisito-casos y tabla de cobertura', 'Elige los casos para el reporte de su variante'),
    ('Ejecución y evidencia reproducible', 'C9',
     ['Esperado escrito antes, obtenido, entorno, consulta de control y condición en cada caso; otra persona puede repetirlos.',
      'Esperado, obtenido, entorno y condición en cada caso.',
      'Resultados sin entorno o sin condición.',
      'Sin resultados registrados, o resultados no obtenidos presentados como comprobados.'],
     'Resultados de la matriz y de la copia con DP', 'Reproduce un caso ante el docente'),
    ('Integración, permisos, persistencia y recuperación', 'C8',
     ['Circuito, permisos con las tres cuentas, persistencia y restauración comprobados, y pendientes del entorno identificados.',
      'Circuito, permisos, persistencia y restauración comprobados.',
      'Alguna de las cuatro sin comprobar.',
      'Sin pruebas de integración.'],
     'Tablas 15.1 y 15.2 del equipo', 'Explica una protección y su prueba'),
    ('Uso y aceptación', 'C9',
     ['Dos sesiones con tareas nuevas y observaciones; acta con evidencia; prioridades justificadas y mejoras tramitadas.',
      'Dos sesiones registradas y acta de aceptación con evidencia.',
      'Una sola sesión u opiniones en lugar de observaciones.',
      'Sin sesiones ni acta.'],
     'Sesiones, acta y prioridades', 'Justifica una prioridad'),
    ('Corrección y regresión', 'C9',
     ['Diagnóstico con causa y capa, corrección mínima revisada por un par, regresión completa y trazabilidad actualizada.',
      'Corrección con diagnóstico y regresión registrada.',
      'Corrección sin regresión o sin diagnóstico.',
      'Sin correcciones, o correcciones que rompen lo que andaba.'],
     'Diagnóstico, revisión y registro de regresión', 'Diagnostica su variante y nombra la regresión'),
    ('Versión candidata y límites conocidos', 'C8',
     ['Versión identificada, condiciones mínimas revisadas, recuperación registrada si falta una y límites claros.',
      'Versión identificada con sus límites conocidos y las condiciones mínimas revisadas.',
      'Límites incompletos o condiciones sin revisar.',
      'Sin versión candidata, o límites ocultos.'],
     'Tablas de condiciones mínimas y de límites', 'Distingue falla, límite y pendiente'),
]
ACT_E32 = [
    ('Ejercitá', [
        'Clasificá cada punto como falla, límite conocido o pendiente del entorno:\n(a) la restauración no se probó en el '
        'laboratorio; (b) un caso de la matriz no coincide y no se corrigió; (c) un formulario que no conserva lo escrito, '
        'documentado.',
    ]),
    ('Resolvé', [
        'Completá la tabla de condiciones mínimas de tu equipo como la Tabla 16.7; si falta una, registrá la recuperación.',
        'Escribí la tabla de límites conocidos de tu versión candidata como la Tabla 16.8 y registrá la versión en la bitácora.',
    ]),
]

REPASO = ('Para repasar', [
    'Primero se reproduce; después se separan síntoma, causa y capa, y se estima el impacto.',
    'La corrección es mínima, la revisa otro integrante y se integra solo si pasa la regresión.',
    'Un pedido nuevo no es un defecto: va por una solicitud de cambio, que actualiza requisito, contrato, mensaje y prueba.',
    'Las condiciones mínimas se revisan una por una; si falta una, no se declara aprobada: se registra la recuperación.',
    'La versión candidata dice sus límites conocidos y separa los pendientes del entorno.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, los Encuentros 31 y 32 se reúnen en el Encuentro 24: «Sin encuentro de reserva para '
    'recuperación técnica.» Se conservan las 2 HC de evaluación del H5.',
    'Se priorizan las condiciones mínimas de aceptación, las pruebas esenciales, la corrección de mayor prioridad con su '
    'regresión y la defensa del H5. Pasan a lectura: el ejemplo complementario SC-02 (Tablas 16.4 y 16.5) y el Desafío.',
    'Si un equipo no cumple una condición mínima, no se lo declara aprobado: se registra la recuperación y se ofrece el '
    'procedimiento, en el tiempo que la institución disponga.',
])

# ------------------------------------------------------------------ evaluación
EVAL_ID = 'ADS3-L5-C16'
EVAL_TITULO = 'Evaluación del Capítulo 16'
EVAL_TEXTO_BASE = ('Texto base — Gestión de solicitudes de soporte (situación de evaluación, ficticia)', [
    'SO-1 Cada solicitud pasa por los estados abierta, en curso y cerrada, en ese orden.',
    'SO-2 Solo el técnico responsable puede cerrar una solicitud.',
    'SO-3 Un reporte dice: «al cerrar, la pantalla muestra “en curso” hasta que se recarga».',
    'SO-4 La coordinación pide un estado nuevo, «esperando repuesto».',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', '¿Qué se hace primero con el reporte SO-3?',
     ['Reproducirlo con los pasos.', 'Cambiar el código de cierre.', 'Agregar un estado nuevo.', 'Cerrarlo como resuelto.']),
    ('mc', 'Si al recargar el estado es «cerrada», ¿dónde está probablemente la causa de SO-3?',
     ['En la presentación.', 'En la base de datos.', 'En la regla SO-1.', 'En el permiso SO-2.']),
    ('mc', 'SO-4 pide un estado nuevo. ¿Cómo se trata?',
     ['Como una solicitud de cambio, con su impacto y su versión.', 'Como un defecto urgente.', 'Se agrega sin avisar.',
      'Se rechaza siempre.']),
    ('mc', 'Después de corregir SO-3, ¿qué pruebas se ejecutan?',
     ['La que reproduce SO-3 y las que el cambio pudo afectar, más el núcleo.', 'Solo la que reproduce SO-3.',
      'Ninguna, si el código compila.', 'Solo las de permisos.']),
    ('vf', 'La revisión entre pares la hace quien escribió la corrección.',
     False, 'Falso. La hace otro integrante.'),
    ('vf', 'Un límite conocido que el equipo documenta es una falla escondida.',
     False, 'Falso. Es algo que el equipo sabe y declara.'),
    ('vf', 'Si falta una condición mínima de aceptación, se registra la recuperación y no se declara aprobada.',
     True, 'Verdadero (Work §4.3).'),
    ('ab', 'Escribí el diagnóstico de SO-3: síntoma, causa probable, capa e impacto, con las fuentes (SO-…).',
     'Síntoma: la pantalla muestra «en curso» (SO-3). Causa probable: la pantalla no se actualiza después de cerrar. Capa: '
     'presentación. Impacto: la pantalla de la solicitud y quizá otras que muestren estados; regresión de SO-1 y SO-2. Un '
     'punto por cada parte.', 4),
    ('ab', 'Escribí la solicitud de cambio de SO-4: qué se pide, por qué, qué cambia (reglas, pantalla, pruebas) y la versión.',
     'Qué y quién (SO-4); por qué; qué cambia: SO-1 (orden de estados), la pantalla y las pruebas de transición; versión '
     'nueva del catálogo. Un punto por cada parte.', 4),
]
EVAL_PUNTAJE = ('Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno). '
                'Es opcional: el instrumento principal del cierre de la unidad es el H5.')

# El Capítulo 16 no tiene práctica independiente (decisión 5 de Fernando): el H5 es la actividad integradora.
PRACTICA_TITULO = None
PRACTICA_INTRO = []
NIVELES = []
PRACTICA_CONTROL = None

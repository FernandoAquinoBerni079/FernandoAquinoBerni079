# -*- coding: utf-8 -*-
"""Capítulo 17 — «Preparar una entrega reproducible» (Work §6: secciones 17.1 a 17.4 y práctica «entregar código,
datos, pruebas y documentación coherentes; H6»; encuentros 33 y 34).

Decisiones de Fernando (21-oct-2026): D-1, el equipo modelo empaqueta una copia nueva de la referencia v2 con SC-02;
D-2, licencia provisional de uso educativo institucional, como borrador, con cada recurso externo verificado según su
versión exacta; D-3, evaluación opcional de 15 puntos. La instalación por otro equipo la demuestra un equipo distinto,
sin ayuda: la ejecución automática de la guía (build/prueba_guia.py) es una comprobación técnica y se rotula así.
Capacidades de Work §5.2: C10 (Encuentro 33) y C7 y C10 (Encuentro 34)."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
L6 = os.path.dirname(AQUI)
ADS = os.path.dirname(L6)
sys.path.insert(0, os.path.join(L6, 'caso'))
import entrega_u6 as E
import mbokaja_u6 as MB
import instrumentos_u6 as I
C4 = None
try:
    import construccion as C4   # lote_4/caso, en la ruta cuando arma construir.py
except ImportError:
    pass

NUM = 17
UNIDAD = 'Unidad VI — Entregar y comunicar'
CAPITULO = 'Capítulo 17'
TITULO = 'Preparar una entrega reproducible'
ENCUENTROS = (33, 34)
SECCIONES = ['17.1 Guía de instalación, configuración y ejecución',
             '17.2 Manual breve basado en tareas',
             '17.3 Respaldo, restauración, licencias y registro de procedencia',
             '17.4 Prueba de instalación por otro equipo y acta de entrega simulada']
PRACTICA_WORK = 'entregar código, datos, pruebas y documentación coherentes; H6'

ROTULO_CAPACIDAD = ('Capacidades propuestas para el programa institucional (C10 en el Encuentro 33; C7 y C10 en el '
                    'Encuentro 34; no son capacidades oficiales del MEC)')
CAPACIDAD = ('C7. Organiza y registra el trabajo colaborativo.\n'
             'C10. Documenta, entrega y defiende el prototipo.')
TEMA = ('Guía de instalación con pasos comprobables, manual por tareas, respaldo y restauración documentados, licencias y '
        'registro de procedencia, instalación por otro equipo sin ayuda y acta de entrega simulada. Coherencia del paquete '
        'y hito H6.')
INDICADORES = [
    'Escribe una guía de instalación con requisitos, comandos exactos, resultado esperado y qué hacer si falla, y la prueba '
    'al pie de la letra en una carpeta limpia.',
    'Escribe un manual por tareas que una persona ajena al desarrollo puede seguir, con el significado de cada mensaje.',
    'Documenta el respaldo y la restauración como tareas y registra la procedencia y la licencia de cada recurso.',
    'Instala el paquete de otro equipo sin ayuda, registra cada paso con su mensaje y completa el acta de entrega.',
    'Corrige el paquete con lo observado y entrega código, datos, pruebas y documentación coherentes, con sus límites.',
]
TIEMPO = ('Dos encuentros de 5 HC (33 y 34 de la secuencia anual). Encuentro 33: 5 HC de documentación. Encuentro 34: '
          '2 HC de verificación (instalación por otro equipo), 2 de documentación (ajustes) y 1 de evaluación (H6).')

APERTURA = [
    'El sistema funciona en la computadora del equipo. La pregunta ahora es otra: ¿funciona en la de otra persona, que no '
    'lo construyó y que no puede preguntarle nada al equipo? Una entrega es reproducible cuando otra persona la instala, la '
    'usa y la recupera de un respaldo siguiendo solo lo que está escrito.',
    'En este capítulo el equipo escribe la guía y el manual, los prueba, registra de dónde sale cada recurso y entrega su '
    'paquete a otro equipo, que lo instala sin ayuda. Lo que falla en esa instalación se corrige antes del hito H6.',
]
ARTICULACION = [
    'Con el Capítulo 10: la ficha de entorno E-1 a E-12 da los requisitos de la guía.',
    'Con el Capítulo 15: la prueba de restauración (Ejemplo resuelto 15.1) pasa a ser una tarea del manual.',
    'Con el Capítulo 16: los límites conocidos de la versión candidata (Tabla 16.8) van al paquete y al acta.',
]
AVISO_ENTORNO = C4.AVISO_ENTORNO if C4 else ('Estado del entorno: no probado en la institución', [])

# ------------------------------------------------------------------ encuentro 33
E33_TITULO = 'Encuentro 33 — Escribir y probar la propia documentación'

S171 = ('17.1 Guía de instalación, configuración y ejecución', [
    'Una guía de instalación es una secuencia de pasos que otra persona sigue sin preguntar. Cada paso tiene tres partes: '
    'el comando exacto (o la acción), el resultado que tiene que aparecer y qué hacer si no aparece (Tabla 17.1). Antes de '
    'los pasos van los requisitos del entorno, que salen de la ficha de entorno del Capítulo 10.',
    'Una guía se prueba como se prueba el código: alguien la sigue al pie de la letra, en una carpeta limpia, sin hacer '
    'nada que la guía no diga. Si hay que «saber» algo que no está escrito, la guía tiene un defecto. Por eso el equipo '
    'prueba su propia guía antes de entregarla (evidencia de Work, Encuentro 33).',
    'Las claves de las cuentas de demostración se muestran una sola vez al instalar. La guía lo avisa: son de demostración '
    'y no se usan con datos reales sin cambiarlas.',
])
TABLA_171_ROTULO = 'Tabla 17.1 — Pasos de la guía de instalación del paquete modelo'


def tabla_171():
    filas = []
    for i, (t, cmd, entrada, esperado, si_falla) in enumerate(E.PASOS, start=1):
        accion = cmd.replace('NAVEGADOR ', 'Abrir ') if cmd.startswith('NAVEGADOR') else ('Ctrl+C en la ventana del paso 3' if cmd == 'DETENER' else cmd)
        if entrada:
            accion += ' (escribir %s)' % entrada
        filas.append([str(i), t, accion, '«%s»' % esperado if esperado else '—'])
    return (['Paso', 'Qué se hace', 'Comando o acción', 'Resultado esperado'], filas)


EJ171 = ('Ejemplo resuelto 17.1: corregir un paso que no se puede seguir', [
    'Consigna: una guía dice «2. Instalá la base y anotá las claves». ¿Qué le falta?',
    'Le falta el comando exacto: php instalar.php. Le falta el resultado esperado: «Base creada en:», seguido de la ruta. '
    'Y le falta qué hacer si falla: si ya existe una base, no borrarla; usar php instalar.php --reiniciar, que pide '
    'confirmación y guarda antes un respaldo.',
    'Corregido, es el paso 2 de la Tabla 17.1. Una persona que nunca vio el sistema puede hacerlo y sabe si salió bien.',
])

S172 = ('17.2 Manual breve basado en tareas', [
    'La persona que usa el sistema no piensa en pantallas: piensa en lo que quiere hacer. Por eso el manual se organiza por '
    'tareas: prestar un libro, registrar una devolución, ver los vencidos, sacar el informe del mes (Tabla 17.2). Cada '
    'tarea dice quién la hace, dónde, los pasos y qué significa cada mensaje que puede aparecer.',
    'Los mensajes del sistema ya dicen qué pasó y qué hacer (Capítulo 8). El manual no los repite enteros: explica cuándo '
    'aparecen y qué decisión tomar. Las tareas salen de los recorridos de las sesiones de uso del Capítulo 15.',
    'El respaldo y la restauración también son tareas, aunque las haga el responsable técnico: tienen pasos y una prueba.',
])
TABLA_172_ROTULO = 'Tabla 17.2 — Tareas del manual del paquete modelo'


def tabla_172():
    return (['Tarea', 'Quién', 'Dónde', 'Mensajes que explica'],
            [['%s. %s' % (c, t), q, p, ', '.join(m for m, _ in ms)] for c, t, q, p, _, ms in E.TAREAS])


EJ172 = ('Ejemplo resuelto 17.2: la tarea «registrar una devolución»', [
    'Quién: la bibliotecaria. Dónde: public/devolucion.php. Pasos: escribir el código del ejemplar que vuelve, revisar la '
    'fecha y apretar «Confirmar devolución».',
    'Mensajes: ME-07, listo (el préstamo queda en el historial); ME-06, ese ejemplar no estaba prestado (apartarlo y '
    'revisar el historial); MV-10, la fecha es anterior a la salida (corregirla).',
    'Por qué así: con ME-06 la bibliotecaria no tiene que adivinar; el manual le dice qué hacer con el libro.',
])
LEAD_FIG171 = 'La Figura 17.1 muestra el camino de una entrega, desde la guía escrita hasta el hito H6.'
EPI_FIG171 = 'Figura 17.1 — De la guía escrita al acta de entrega.'
ACT_E33 = [
    ('Ejercitá', [
        'Para cada paso, decí qué le falta (comando, resultado esperado o qué hacer si falla):\n'
        '(a) «Abrí el sistema»; (b) «php respaldar.php»; (c) «Si da error, revisá la configuración».',
    ]),
    ('Resolvé', [
        'Escribí la guía de instalación de tu paquete, con requisitos y pasos como los de la Tabla 17.1. Después seguila al pie '
        'de la letra en una carpeta limpia y corregí cada paso que tuviste que adivinar.',
        'Escribí el manual por tareas de tu sistema, con al menos cinco tareas, sus pasos y sus mensajes.',
    ]),
    ('Pensá y decidí', [
        'Un integrante propone no incluir el paso de restauración «porque nunca se va a usar». Explicá qué riesgo tiene.',
    ]),
]

# ------------------------------------------------------------------ práctica (Encuentro 33)
PRACTICA_TITULO = 'Práctica 17 — El paquete del voluntario para Mbokaja'
PRACTICA_INTRO = [
    'En Mbokaja, un voluntario preparó un paquete del sistema para la computadora donada (M-F13). El profesor del colegio '
    'vecino lo va a instalar en su visita, sin poder preguntarle nada al voluntario (M-F9). Antes de entregarlo, tu equipo '
    'lo revisa.',
    'El paquete está en lote_6/proyecto/paquete_mbokaja/ y tu docente te da una copia. Los niveles 1 y 2 se hacen en esa '
    'copia; el nivel 3 se resuelve en papel. La copia tiene datos ficticios.',
]
NIVELES = [
    ('Nivel 1 — Guiado', [
        'Sin ejecutar nada todavía, compará los documentos con los archivos: ¿cada comando de la guía nombra un archivo que '
        'está?, ¿cada archivo de la lista de entrega está?, ¿cada recurso de public/ tiene su procedencia?, ¿cada pantalla y '
        'cada mensaje del manual existen? Anotá cada incoherencia con el archivo y la línea.',
        'Ejecutá php comprobar_entrega.php en la copia y compará su resultado con tu lista.',
    ]),
    ('Nivel 2 — Intermedio', [
        'Corregí cada incoherencia en la copia y decidí, para cada una, si se corrige el documento, el código, la prueba o se '
        'quita el archivo. Justificá con MS-9 y MS-10.',
        'Seguí la guía corregida al pie de la letra en una carpeta limpia y anotá cada paso con su resultado.',
    ]),
    ('Nivel 3 — Ampliación (en papel)', [
        'Escribí el acta de entrega a la escuela, con lo que el profesor vecino tiene que comprobar en su visita y lo que '
        'queda pendiente.',
        'Escribí la fila de procedencia que haría falta para que la escuela use un logo propio, y quién tiene que autorizarlo.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: cada incoherencia tiene archivo y motivo; la corrección distingue documento, código y '
                    'prueba; nada sin procedencia queda en el paquete; la guía corregida se siguió al pie de la letra; el '
                    'acta separa lo comprobado de lo pendiente.')

# ------------------------------------------------------------------ encuentro 34
E34_TITULO = 'Encuentro 34 — Entregar a otro equipo; hito H6'

S173 = ('17.3 Respaldo, restauración, licencias y registro de procedencia', [
    'El respaldo y la restauración se documentan como tareas (T-08) y se prueban: el paso 7 de la guía restaura el respaldo '
    'del paso 6 y comprueba que la base tenga lo mismo que el respaldo.',
    'La ficha de procedencia registra cada recurso del paquete: qué es, de quién es, con qué licencia o condición se usa, '
    'dónde se verificó y si se entrega (Tabla 17.3). Se separan cuatro clases: el código propio, los datos ficticios, las '
    'herramientas de terceros que el paquete necesita pero no trae, y los recursos ajenos, como imágenes o iconos.',
    'Una licencia se verifica en su fuente primaria y para la versión exacta que se usa: las licencias cambian entre '
    'versiones. Lo que no tiene una licencia conocida no se incluye. Y el código que escribe cada estudiante es de sus '
    'autores: la ficha no se lo atribuye a nadie más. RS-02 pide que la solución no requiera licencias pagas: la ficha es '
    'la evidencia.',
])
TABLA_173_ROTULO = 'Tabla 17.3 — Ficha de procedencia del paquete modelo (licencias verificadas el %s)' % E.FECHA_CONSULTA


def tabla_173():
    return (['Recurso', 'Autor o titular', 'Licencia o condición', 'En el paquete'],
            [[f[0], f[2], f[3], f[5]] for f in E.PROCEDENCIA])


CODIGOS_S173 = ['Código 17.1']
EXPLICA = {
    'Código 17.1': 'El comprobador recorre public/ y busca cada archivo que no es código (una imagen, una hoja de estilos) '
                   'en la ficha de procedencia. Si no lo encuentra, informa una incoherencia [D].',
    'Código 17.2': 'Para cada línea de un bloque de comandos de la guía que empieza con «php», busca el archivo que nombra. '
                   'Si no existe, la guía no se puede seguir: incoherencia [A].',
}
LICENCIA_ROTULO = 'Borrador de licencia del paquete modelo (no es un texto jurídico cerrado)'
LICENCIA = ('Borrador de licencia: qué dice', [
    'Es un borrador de uso educativo institucional. El aspecto jurídico no está cerrado: lo revisan los titulares.',
    'Autoriza, dentro de la institución que adquirió el material: instalar, ejecutar, estudiar y modificar el proyecto.',
    'No autoriza la redistribución comercial del material editorial ni su entrega fuera de la institución.',
    'No cubre los componentes de terceros (tienen sus propias licencias) ni el código de los estudiantes (es de sus autores).',
])
EJ173 = ('Ejemplo resuelto 17.3: completar la ficha de procedencia', [
    'Consigna: el paquete del equipo modelo usa PHP, SQLite, su propio código, datos inventados y ninguna imagen. Completar '
    'la ficha.',
    'Código y datos: del proyecto, con el borrador de licencia. PHP 8.3.6: The PHP License, version 3.01, verificada en el '
    'archivo LICENSE de esa versión; no se entrega, lo instala la institución. SQLite 3.45.1: dedicado al dominio público, '
    'verificado en su LICENSE.md y en su página de copyright; viene con PHP.',
    'Imágenes: ninguna. Si el equipo quisiera un logo, haría falta su autor y su permiso; sin eso, no se incluye.',
])

S174 = ('17.4 Prueba de instalación por otro equipo y acta de entrega simulada', [
    'La prueba decisiva es que otro equipo instale el paquete sin ayuda. El equipo autor entrega el paquete y se retira: no '
    'explica, no corrige en el momento. El equipo receptor sigue la guía y anota cada paso como hecho, con dificultad o '
    'fallido, con el mensaje exacto. Después restaura un respaldo y ejecuta el comprobador de entrega.',
    'Con eso completa el acta de entrega simulada (Tabla 17.5): qué se entrega, la versión, lo que pasó en cada paso, los '
    'límites conocidos y sus observaciones. El equipo autor corrige la guía con lo observado y vuelve a probar el paso que '
    'falló. Así se completa la condición mínima que quedó pendiente en el H5: instalación y restauración reproducibles.',
    'Una ejecución automática de la guía, como la del equipo modelo (Tabla 17.6), comprueba que los pasos funcionan, pero '
    'no reemplaza a la persona ajena al desarrollo: no tropieza con una palabra confusa ni con un paso que da por sabido. '
    'Esa evidencia solo la da otro equipo (Código 17.2).',
])
TABLA_174_ROTULO = 'Tabla 17.4 — Lo que el comprobador de entrega revisa'
TABLA_174 = (['Bloque', 'Qué revisa'],
             [['A', 'Cada comando de la guía nombra un archivo que existe'],
              ['B', 'Cada archivo de la lista de entrega está en el paquete'],
              ['C', 'Cada prueba de la lista termina bien y da su resultado'],
              ['D', 'Cada recurso que no es código tiene su procedencia'],
              ['E', 'Cada mensaje y cada pantalla del manual existen'],
              ['F', 'Todos los documentos declaran la misma versión']])
CODIGOS_S174 = ['Código 17.2']
TABLA_175_ROTULO = 'Tabla 17.5 — Acta de entrega simulada'
TABLA_175 = (['Campo', 'Qué se anota'], [[k, v or 'Lo completa el equipo receptor'] for k, v in E.ACTA_CAMPOS])
TABLA_176_ROTULO = 'Tabla 17.6 — Comprobación técnica del paquete modelo y lo que queda pendiente'


def resumen():
    p = os.path.join(L6, 'resultados_pruebas', 'resumen.json')
    return json.load(open(p, encoding='utf8')) if os.path.exists(p) else None


def entorno_texto():
    e = resumen()['entorno']
    return '%s, PHP %s, SQLite %s (contenedor de construcción, %s)' % (e['sistema'], e['php'], e['sqlite'], e['fecha'])


def tabla_176():
    r = resumen()
    g, c = r['guia']['modelo'], r['comprobador']['modelo']
    reg = r['regresion']
    bien = sum(1 for v in reg.values() if v['codigo_salida'] == 0)
    return (['Prueba', 'Resultado', 'Condición'],
            [['La guía, seguida en una carpeta limpia por un proceso automático', '%d de %d pasos' % (g['correctos'], g['total']),
              'Comprobado (técnica, en el entorno de construcción)'],
             ['Comprobador de entrega', c['resultado'].replace('Resultado: ', ''), 'Comprobado (técnica)'],
             ['Regresión de la versión empaquetada', '%d de %d pruebas sin fallas' % (bien, len(reg)), 'Comprobado (técnica)'],
             ['Instalación por otro equipo, sin ayuda', 'La hace el curso en el Encuentro 34', 'Pendiente hasta el acta'],
             ['Instalación en Windows y en el laboratorio', '—', 'Pendiente (ficha de entorno)']])


NOTA_176 = 'Entorno: %s. Una comprobación automática no es la evaluación de una persona ajena al desarrollo.'
EJ174 = ('Ejemplo resuelto 17.4: un acta con un paso fallido (simulación del libro)', [
    'Situación simulada: el equipo receptor sigue la guía de otro equipo. En el paso 3 el puerto 8000 está ocupado y el '
    'sistema no arranca. La guía no decía qué hacer.',
    'Acta: paso 3, fallido, mensaje «Address already in use». Observación: «no sabíamos qué puerto usar». Los demás pasos, '
    'hechos. La restauración, hecha.',
    'Ajuste del equipo autor: agrega al paso 3 «si el puerto 8000 está ocupado, usá otro: localhost:8001» y vuelve a probar '
    'ese paso. En el acta se anota el ajuste y la nueva prueba.',
])

# ------------------------------------------------------------------ H6
H6_TITULO = 'Hito H6: paquete reproducible; ajustes finales'
H6_TEXTO = [
    'El H6 es el hito de la unidad. Cada equipo entrega su paquete con el acta firmada por el equipo receptor, los ajustes '
    'que hizo y el resultado del comprobador. La evidencia central es que otro equipo instaló y restauró el sistema sin '
    'ayuda.',
    'Cada integrante muestra la parte del paquete que redactó o probó, registrada en la bitácora, y responde una pregunta '
    'del docente sobre ella.',
]
H6_LISTA = ('Antes de entregar: lista de verificación del equipo', [
    '1. ¿La guía tiene requisitos y, en cada paso, comando, resultado esperado y qué hacer si falla?',
    '2. ¿La siguieron al pie de la letra en una carpeta limpia?',
    '3. ¿El manual está organizado por tareas, con sus mensajes?',
    '4. ¿El respaldo y la restauración están documentados y probados?',
    '5. ¿La ficha de procedencia tiene cada recurso, con su licencia verificada según la versión?',
    '6. ¿php comprobar_entrega.php da 0 incoherencias?',
    '7. ¿Los límites y los pendientes están escritos y separados?',
    '8. ¿El acta está completa y firmada por el equipo receptor?',
])
H6_EVALUACION = ('Cómo se evalúa el H6', [
    'Se evalúan seis criterios (C7 y C10) con los cuatro niveles de los hitos anteriores. Cada uno combina un 60 % de '
    'evidencia del paquete del equipo y un 40 % de evidencia individual. La proporción es una propuesta editorial: la '
    'institución decide cómo se convierte en calificación.',
    'Si falta una evidencia, se registra como ausente y no se confunde con un nivel Inicial. La instalación en Windows o en '
    'el laboratorio, si no se pudo hacer, es un pendiente del entorno, no una falla del equipo.',
])
RUBRICA_H6 = I.RUBRICA_H6
ACT_E34 = [
    ('Ejercitá', [
        'Clasificá cada recurso: código propio, datos ficticios, herramienta de terceros o recurso ajeno:\n'
        '(a) src/reglas.php; (b) PHP; (c) una foto de la biblioteca bajada de internet; (d) src/datos_ejemplo.php.',
    ]),
    ('Resolvé', [
        'Completá la ficha de procedencia de tu paquete como la Tabla 17.3, con la licencia de cada recurso externo verificada '
        'para la versión que usaste.',
        'Instalá el paquete de otro equipo sin ayuda y completá su acta como la Tabla 17.5. Con el acta de tu paquete, corregí '
        'la guía y volvé a probar el paso que falló.',
    ]),
    ('Pensá y decidí', [
        'El equipo receptor no pudo restaurar porque la computadora del laboratorio no deja escribir en la carpeta. ¿Es una '
        'falla del paquete o un pendiente del entorno? ¿Qué se anota en el acta?',
    ]),
]

REPASO = ('Para repasar', [
    'Una guía se prueba siguiéndola al pie de la letra: cada paso tiene comando, resultado esperado y qué hacer si falla.',
    'El manual se organiza por tareas y explica cuándo aparece cada mensaje.',
    'La ficha de procedencia registra cada recurso con su licencia, verificada para la versión exacta; lo que no tiene '
    'licencia conocida no se incluye.',
    'La instalación por otro equipo, sin ayuda, es la evidencia de una entrega reproducible; una prueba automática no la '
    'reemplaza.',
    'El acta registra lo que pasó; el equipo autor corrige y vuelve a probar antes del H6.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, los Encuentros 33 y 34 pasan a ser el 25 y el 26, sin cambios.',
    'No se reduce lo esencial: la guía probada, la instalación por otro equipo sin ayuda, el acta y el H6. Pasa a lectura '
    'el nivel 3 de la Práctica 17.',
])

# ------------------------------------------------------------------ evaluación (D-3: opcional, 15 puntos)
EVAL_ID = 'ADS3-L6-C17-e'   # semilla elegida para repartir las claves entre a, b y c
EVAL_TITULO = 'Evaluación del Capítulo 17'
EVAL_TEXTO_BASE = ('Texto base — Ludoteca escolar (situación de evaluación, ficticia)', [
    'LU-1 La ludoteca presta juegos de mesa por una semana; cada juego tiene un código JU- y tres cifras.',
    'LU-2 Un voluntario va a instalar el sistema en la computadora de la sala, que no tiene internet.',
    'LU-3 El sistema muestra la foto de la caja de cada juego, sacada del sitio de la editorial del juego.',
    'LU-4 La coordinación quiere pasarle el sistema a la ludoteca de otro colegio.',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', '¿Cuál de estos pasos de una guía de instalación puede seguir el voluntario de LU-2 sin preguntar?',
     ['«php instalar.php» — Resultado esperado: «Base creada en:»; si ya hay una base, no la borres.',
      '«Instalá el sistema como siempre.»', '«Configurá la base.»', '«Si falla, buscá en internet.»']),
    ('mc', 'Las fotos de LU-3, ¿qué necesitan para incluirse en el paquete?',
     ['Su autor y un permiso o licencia que autorice ese uso, registrados en la ficha.', 'Nada, porque están en internet.',
      'Solo cambiarles el nombre.', 'Que sean chicas.']),
    ('mc', 'Con un borrador de licencia de uso institucional como el del paquete modelo, ¿qué pasa con LU-4?',
     ['No está autorizado sin un acuerdo de los titulares: la licencia vale dentro de la institución.',
      'Se puede, porque es para educación.', 'Se puede, si se cambia el nombre.', 'Se puede, si se borra la licencia.']),
    ('mc', '¿Qué evidencia demuestra que la entrega es reproducible?',
     ['Que otro equipo la instaló y restauró sin ayuda, con su acta.', 'Que funciona en la computadora del equipo.',
      'Que el código compila.', 'Que la guía es larga.']),
    ('vf', 'El manual por tareas se organiza según las pantallas del sistema.',
     False, 'Falso. Se organiza por lo que la persona quiere hacer.'),
    ('vf', 'Una ejecución automática de la guía reemplaza la instalación por otro equipo.',
     False, 'Falso. Comprueba los pasos, pero no a la persona ajena al desarrollo.'),
    ('vf', 'La licencia de un componente externo se verifica para la versión exacta que se usa.',
     True, 'Verdadero. Las licencias pueden cambiar entre versiones.'),
    ('ab', 'Escribí tres pasos de la guía de instalación para LU-2, cada uno con su comando o acción, el resultado esperado y '
           'qué hacer si falla.',
     'Un punto por cada paso completo y uno por cuidar LU-2 (sin internet: nada que se descargue durante la instalación).', 4),
    ('ab', 'Escribí la fila de la ficha de procedencia de las fotos de LU-3 y decí si van en el paquete.',
     'Recurso, autor o titular (la editorial del juego), licencia o condición (desconocida si no hay permiso), fuente y '
     'decisión (no se incluyen sin permiso). Un punto por cada parte.', 4),
]
EVAL_PUNTAJE = 'Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno).'

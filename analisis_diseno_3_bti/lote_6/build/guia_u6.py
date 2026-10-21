# -*- coding: utf-8 -*-
"""Guía docente con solucionario del lote 6 (Unidad VI, Capítulos 17 y 18): paquete de entrega modelo y herramientas
del docente para revisarlo (v1.1: inspección estática y pruebas en aislamiento, fuera del paquete), licencias y procedencia (borrador, decisión D-2), organización de la instalación por otro equipo, paquete de Mbokaja
con la clave de sus defectos, banco reservado de variantes V6 (solo el procedimiento y los ejemplos públicos),
preparación y planilla de tiempos del Encuentro 35 (D-5), secuencia de cada encuentro en HC, claves de las actividades,
de la práctica y de la evaluación, rúbricas del H6, de la defensa y del producto final, fichas de recuperación,
planilla anual, calendario de 28 encuentros, resultados de las pruebas con su entorno y procedencia de los recursos.
Los datos se leen de caso/ y de resultados_pruebas/resumen.json (la ejecución real); no se copian."""
import os
import oficio as O
H, M, K = O.H, O.M, O.K
import piezas_u6 as Z
import cap17, cap18
import planilla_tiempos as PT
E, MB, I = cap17.E, cap17.MB, cap17.I

ANCHO_SEC = [3.2, 2.4, 11.0]


def _r(t):
    return t.replace('Resultado: ', '')


def _c(x):
    """Resultado de una herramienta sin su aclaración entre paréntesis."""
    return x['resultado'].split(' (')[0]


# ---------------------------------------------------------------- 0. antes del Encuentro 33
PAQUETE = [
    'El paquete del equipo modelo (lote_6/proyecto/paquete_entrega_modelo/) es una copia nueva de la referencia docente v2 '
    'con SC-02 del lote 5, que se conserva sin cambios con sus diferencias y su regresión (decisión D-1). El código copiado '
    'es idéntico: solo se agregan LEEME.txt y los documentos de ENTREGA/. build/reproducir.py lo '
    'comprueba archivo por archivo.',
    'Los documentos de ENTREGA/ se generan desde caso/entrega_u6.py, la misma fuente de las Tablas 17.1 a 17.3 y 17.5: el '
    'libro y el paquete dicen lo mismo.',
    'Un paquete recibido es código desconocido: no se ejecuta para decidir si es confiable. Por eso el paquete no trae '
    'un comprobador propio (lo traía la versión 1.0). El docente lo revisa con dos herramientas que viven fuera del paquete, '
    'en lote_6/proyecto/herramientas/, con su procedimiento en el LEEME de esa carpeta:',
    '• Inspección estática: php herramientas/inspeccionar_entrega.php <paquete>. Revisa los seis bloques de la Tabla 17.4 '
    'leyendo texto y nombres de archivo: no ejecuta, no incluye y no interpreta nada del paquete. Los comandos de la guía y '
    'de la lista de entrega solo se leen; los de forma desconocida se informan.',
    '• Pruebas en aislamiento: php herramientas/probar_en_aislamiento.php <paquete>. Solo ejecuta las tres pruebas de su '
    'lista cerrada (prueba_contratos, prueba_garantias y prueba_respaldo), armadas por la herramienta y nunca tomadas del '
    'paquete, en una copia descartable que borra al terminar, con entorno mínimo y tiempo límite. Se niega a correr con '
    'una cuenta de administrador o si el paquete tiene enlaces simbólicos.',
    'Las pruebas se corren siempre después de la inspección y en un equipo aislado: una computadora o máquina virtual de '
    'pruebas sin datos de la institución, sin red, con una cuenta sin permisos de administrador y una carpeta descartable. '
    'Al terminar se borra la carpeta (o se vuelve la máquina virtual a su estado inicial). El núcleo de las pruebas y el '
    'bloque C de la inspección están en las Referencias R-8 y R-9.',
]
LICENCIAS = [
    'El borrador de licencia (ENTREGA/LICENCIA_BORRADOR.md) aplica la política provisional de la decisión D-2: uso educativo '
    'institucional del código original de referencia, con derechos reservados a sus titulares, y autorización para instalar, '
    'ejecutar, estudiar y modificar el proyecto dentro de la institución adquirente. No autoriza la redistribución comercial '
    'del material editorial. Es un borrador: el aspecto jurídico no está cerrado y lo revisan los titulares.',
    'El borrador no cubre los componentes de terceros ni el código original de los estudiantes, y no los atribuye a la '
    'editorial. Cada equipo registra su propia autoría en su ficha de procedencia.',
    'Las licencias de terceros se verificaron con su fuente primaria y para la versión exacta que usaron las pruebas (tabla '
    'siguiente). Si la institución instala otra versión, se verifica la licencia de esa versión.',
]
INSTALACION_OTRO = [
    'Antes del Encuentro 34, el docente arma las parejas de equipos: cada paquete lo instala un equipo distinto del que lo '
    'hizo. El equipo autor entrega el paquete en una carpeta y se retira de la computadora: no explica ni corrige durante la '
    'instalación. El docente observa y no ayuda; si el equipo receptor se traba, lo anota en el acta y sigue con el paso '
    'siguiente si puede.',
    'El acta (Tabla 17.5) registra las condiciones reales: qué computadora, qué sistema y qué versiones. Esa instalación es '
    'la evidencia de C10 («otro equipo instala con la guía; recupera un respaldo»). Una ejecución automática de la guía, como '
    'la del equipo modelo, sirve como comprobación técnica, pero no reemplaza la evaluación de una persona ajena al '
    'desarrollo.',
    'Si la computadora del laboratorio impide un paso por una razón del entorno (permisos, PHP ausente), se anota como '
    'pendiente del entorno con el mensaje exacto; no es una falla del paquete ni del equipo.',
]
MBOKAJA = [
    'Para la Práctica 17, cada equipo recibe una copia de lote_6/proyecto/paquete_mbokaja/. El paquete tiene cinco defectos '
    'introducidos a propósito (tabla de la clave, en la sección 1). No se entrega la clave: los equipos los buscan primero a '
    'mano (nivel 1) y después con la inspección estática y las pruebas en aislamiento, que corre el docente.',
    'build/reproducir.py comprueba que las dos herramientas informen exactamente las seis incoherencias que producen esos '
    'cinco defectos (cinco la inspección y una las pruebas en aislamiento) y que, con la clave aplicada, el paquete dé 0 '
    'incoherencias y se instale siguiendo su guía.',
    'Las copias que reciben los equipos se usan con las mismas condiciones del procedimiento: cuenta estándar, carpeta '
    'descartable y datos ficticios.',
]
V6_PROCEDIMIENTO = [
    'Las variantes definitivas de la defensa individual son reservadas y no están en el repositorio, como el conjunto DR del '
    'lote 5. Acá van solo sus campos y tres ejemplos públicos para practicar, que no se usan en la defensa.',
    'El docente guarda su banco en una carpeta privada y lo comprueba con python3 lote_6/caso/v6_plantilla.py '
    '--banco=<ruta privada> --estudiantes=<cantidad>. El validador se niega a usar una ruta dentro del repositorio, revisa '
    'que cada variante tenga todos sus campos, que ninguna repita un ejemplo público ni un texto del repositorio, y avisa si '
    'hay menos variantes que estudiantes. Deja su informe junto al banco.',
    'Con este lote se entrega aparte un banco de doce variantes ya comprobado. Conviene que el docente agregue variantes '
    'propias, y que no reutilice en otro curso las que ya se usaron. Las variantes se entregan impresas en la defensa y se '
    'retiran al terminar.',
]


def tabla_paquete():
    r = cap17.resumen()['paquete_modelo']
    filas = [['Código de la referencia v2 con SC-02', 'Idéntico, archivo por archivo' if r['codigo_identico'] else 'NO coincide'],
             ['LEEME.txt', 'Reescrito para el paquete'],
             ['Archivos nuevos', ', '.join(r['nuevos'])]]
    return (['Qué', 'Estado'], filas)


def tabla_licencias():
    return (['Recurso', 'Licencia o condición', 'Fuente verificada'], [[f[0], f[3], f[4]] for f in E.PROCEDENCIA if f[4] != '—'])


# ---------------------------------------------------------------- capítulo 17
SEC_C17 = [
    ('Encuentro 33 — Escribir y probar la propia documentación (5 HC de documentación)', [
        ['Problema y explicación', 'aprox. 1 HC', 'Apertura de la unidad y del capítulo. Sección 17.1 con la Tabla 17.1 y el Ejemplo resuelto 17.1. Actividad 1.'],
        ['Redacción', 'aprox. 2 HC', 'Guía de instalación y manual por tareas del propio equipo (Actividades 2 y 3). Sección 17.2 con la Tabla 17.2 y el Ejemplo resuelto 17.2.'],
        ['Prueba de la propia guía', 'aprox. 1 HC', 'El equipo sigue su guía al pie de la letra en una carpeta limpia y la corrige. Evidencia (Work, encuentro 33): documentación probada por el propio equipo.'],
        ['Práctica 17', 'aprox. 1 HC', 'Paquete de Mbokaja en el nivel que indique el docente. Actividad 4 como cierre.'],
    ]),
    ('Encuentro 34 — Entregar a otro equipo; hito H6 (5 HC: 2 de verificación, 2 de documentación y 1 de evaluación)', [
        ['Instalación por otro equipo', 'aprox. 2 HC (verificación)', 'Sección 17.4: cada equipo instala y restaura el paquete de otro, sin ayuda, y completa el acta (Tabla 17.5, Actividad 3).'],
        ['Ajustes', 'aprox. 2 HC (documentación)', 'Sección 17.3: ficha de procedencia (Tabla 17.3, Actividad 2) y borrador de licencia. El equipo autor corrige su guía con el acta y vuelve a probar el paso que falló. Actividades 1 y 4.'],
        ['Hito H6', 'aprox. 1 HC (evaluación)', 'Lista de verificación del H6 y revisión con la rúbrica (sección 3). Evidencia (Work, encuentro 34): H6, paquete reproducible y ajustes finales.'],
    ]),
]
CLAVES_E33 = [
    ['1', '(a) Le falta todo: la acción exacta (abrir http://localhost:8000), el resultado esperado («PT-01 Buscar un título») y qué hacer si falla. (b) Le falta el resultado esperado («Respaldo guardado y verificado») y qué hacer si falla. (c) No dice qué revisar: hace falta el síntoma y la acción concreta.', 'Aceptar (b) como completo porque tiene el comando.'],
    ['2', 'Guía con requisitos y pasos con comando, resultado esperado y qué hacer si falla, como la Tabla 17.1; registro de la prueba en una carpeta limpia, con los pasos corregidos.', 'Probar la guía en la carpeta de desarrollo, donde ya está todo instalado.'],
    ['3', 'Cinco tareas o más, cada una con quién, dónde, pasos y mensajes con su significado, como la Tabla 17.2.', 'Un manual por pantallas («la pantalla de préstamo tiene dos campos»).'],
    ['4', 'Sin la restauración documentada y probada, un respaldo no sirve: nadie sabe si se puede recuperar (condición mínima de Work §4.3). La restauración es justamente lo que se usa cuando algo salió mal.', 'Aceptarlo porque «el respaldo ya está».'],
]
CLAVES_E34 = [
    ['1', '(a) Código propio. (b) Herramienta de terceros: no se entrega; su licencia se verifica para la versión. (c) Recurso ajeno: sin autor y permiso, no se incluye. (d) Datos ficticios propios.', 'Incluir (c) «porque está en internet».'],
    ['2', 'Ficha con cada recurso, autor, licencia o condición, fuente verificada con fecha y si se entrega, como la Tabla 17.3; las licencias de terceros, para la versión instalada.', 'Copiar la licencia de otra versión.'],
    ['3', 'Acta completa con cada paso (hecho, con dificultad o fallido) y el mensaje exacto, la restauración y el resultado de la revisión del docente. El equipo autor anota el ajuste y la nueva prueba del paso.', 'Ayudar al equipo receptor durante la instalación.'],
    ['4', 'Es un pendiente del entorno si la carpeta no tiene permiso de escritura por la configuración del laboratorio: se anota con el mensaje exacto y se informa al responsable técnico. Si la guía no avisaba del requisito de escritura (que sí está en los requisitos), sería además un defecto de la guía.', 'Marcarlo como falla del equipo, o como restauración comprobada.'],
]
CLAVES_P17 = [
    ['Nivel 1', 'Las incoherencias, encontradas a mano: el paso 2 dice php instalar_base.php, que no existe; la lista de entrega incluye datos/mbokaja_prueba.json, que no está; public/logo_mbokaja.png no tiene procedencia (MS-9); el manual describe la tarea «Reservar un libro», con public/reservas.php y ME-15, que no existen. La prueba vieja (MS-10) solo aparece en las pruebas en aislamiento: prueba_contratos.php no termina bien. Entre las dos herramientas se informan 6 incoherencias de 5 defectos: 5 la inspección estática y 1 las pruebas en aislamiento.'],
    ['Nivel 2', 'Correcciones: documento (paso 2: php instalar.php), lista (quitar el archivo que falta), prueba (volver a esperar ME-14: el código está bien y la prueba quedó vieja), recurso (quitar el logo: sin licencia conocida no se incluye) y manual (quitar la tarea: reservar no es una función del sistema; si se quiere, es una solicitud de cambio). Con eso, la inspección y las pruebas en aislamiento dan 0 incoherencias y la guía se sigue completa (7 de 7 pasos en la comprobación técnica).'],
    ['Nivel 3', 'En papel. Acta con: qué se entrega, versión, lo que el profesor tiene que comprobar en su visita (pasos 1 a 7 de la guía en la computadora donada, sin internet: M-F7), quién recibe y los pendientes (prueba en esa computadora; claves de demostración que hay que cambiar). Fila de procedencia del logo propio: autor (quien lo dibujó), permiso de la escuela para usarlo, fuente y fecha; la autorización la da la dirección.'],
]
COTEJO_P17 = [
    ['Cada incoherencia tiene archivo y motivo.', 'Indicador 5'],
    ['La corrección distingue documento, código, prueba y recurso (Nivel 2 o 3).', 'Indicador 5'],
    ['Nada sin procedencia queda en el paquete.', 'Indicador 3'],
    ['La guía corregida se siguió al pie de la letra (Nivel 2).', 'Indicador 1'],
    ['El acta separa lo comprobado de lo pendiente (Nivel 3).', 'Indicador 4'],
]
CRIT_C17 = [['8', '4: un punto por cada paso completo (comando o acción, resultado esperado y qué hacer si falla) y uno por cuidar LU-2.', 'Sin punto el paso que no dice qué resultado esperar.'],
            ['9', '4: recurso y titular (1), licencia o condición (1), fuente (1), decisión justificada (1).', 'Sin el punto de la decisión si las incluye sin permiso.']]
ERRORES_C17 = [
    ['Probar la guía en la carpeta donde se desarrolló', 'Carpeta limpia, siguiendo solo lo escrito'],
    ['Pasos sin resultado esperado', 'Cada paso dice qué tiene que aparecer'],
    ['Manual por pantallas', 'Manual por tareas, con el significado de los mensajes'],
    ['Copiar una licencia sin verificar la versión', 'Fuente primaria de la versión exacta, con la fecha de consulta'],
    ['Ayudar al equipo receptor', 'El equipo autor se retira; el receptor anota cada paso'],
    ['Tomar la prueba automática como instalación por otro equipo', 'Es una comprobación técnica; la evidencia es el acta del otro equipo'],
]

# ---------------------------------------------------------------- capítulo 18
SEC_C18 = [
    ('Encuentro 35 — Demostración y defensa individual (5 HC de evaluación)', [
        ['Demostraciones', 'según la planilla', 'Sección 18.1: cada equipo sigue su guion (Tabla 18.1) con tiempo fijo; Figura 18.1 y Ejemplo resuelto 18.1. Rúbrica de producto final (sección 2).'],
        ['Defensas individuales', 'según la planilla', 'Sección 18.2: una decisión, una prueba y una variante del banco reservado por estudiante, con la rúbrica de la Tabla 18.2; pregunta de transferencia (Tabla 18.3). Alternativa A o B de la sección 0.6.'],
    ]),
    ('Encuentro 36 — Recuperación, retrospectiva y cierre (5 HC: 3 de evaluación y 2 de gestión)', [
        ['Recuperación', 'aprox. 3 HC (evaluación)', 'Sección 18.3: defensas que pasaron del Encuentro 35 (alternativa B) y fichas de recuperación por prioridad (Tablas 18.4 y 18.5).'],
        ['Retrospectiva y cierre', 'aprox. 2 HC (gestión)', 'Sección 18.4: retrospectiva con la Tabla 18.6, Ejemplo resuelto 18.3, Actividades; evaluación integradora y cierre del proyecto. Evidencia (Work, encuentro 36): evidencia faltante, balance y propuesta de continuidad.'],
    ]),
]
CLAVES_E35 = [
    ['1', 'Guion con cada requisito imprescindible, su evidencia (caso, prueba o acta), lo que se muestra en vivo, qué hacer si falla y el tiempo, como la Tabla 18.1.', 'Ordenar el guion por pantallas.'],
    ['2', '(a) V6-E2: %s (b) V6-E3: %s' % (I.V6_EJEMPLOS[1]['modelo_y_contratos'], I.V6_EJEMPLOS[2]['modelo_y_contratos']), 'Resolver cambiando solo la pantalla.'],
    ['3', 'Respuesta abierta: una decisión con su alternativa y su costo, y una prueba con esperado, obtenido y evidencia.', 'Elegir algo que hizo otro integrante sin poder explicarlo.'],
]
CLAVES_E36 = [
    ['1', '(a) Hecho con evidencia (la regresión registrada). (b) Opinión. (c) Hecho: es un pendiente del entorno.', 'Tratar (b) como evidencia.'],
    ['2', 'Tabla con qué, evidencia, por qué pasó, mejora futura y prioridad; cada mejora apoyada en un límite, una incidencia o una observación.', 'Mejoras sin evidencia («hacerlo más lindo»).'],
]
ERRORES_C18 = [
    ['Demostración como paseo por las pantallas', 'Guion por requisitos y evidencias'],
    ['Ocultar un fallo en vivo', 'Decirlo y mostrar la evidencia registrada'],
    ['Programar la variante en la defensa', 'Razonar: requisito, capas, modelo, contratos y pruebas'],
    ['Usar una variante de ejemplo en la defensa', 'Variantes del banco reservado, impresas y retiradas al terminar'],
    ['Declarar aprobado lo que no se recuperó', 'Registrar qué falta, qué hacer y cuándo'],
    ['Suponer horas extraordinarias', 'Alternativa B y tiempo institucional autorizado, registrado'],
]


def tabla_tiempos_ejemplo():
    v = I.EJEMPLO_TIEMPOS
    t = I.tiempos(**v)
    entradas = [[que, str(v[k])] for k, que, _ in I.TIEMPOS_CAMPOS]
    salidas = [[et, str(t[clave]) or '—'] for et, _, clave in PT.SALIDAS]
    return (['Dato o resultado', 'Valor del ejemplo'], entradas + salidas)


def construir(ruta, claves, paginas, estado, figs):
    import cap3   # niveles de desempeño del lote 1
    r = cap17.resumen()
    doc = H.new_doc()
    Z.portada(doc, 'Guía docente con solucionario', estado)
    doc.add_heading('Guía docente — Lote 6', level=1)
    H.caja(doc, 'Sobre las capacidades y los resultados', [
        'Las capacidades de las fichas (C7 y C10 en el Capítulo 17; C1 a C10, C7, C9 y C10 en el 18) son propuestas para el '
        'programa institucional, tomadas del informe de Work. No son capacidades oficiales del MEC.',
        'Los resultados que se informan corrieron en el entorno de construcción (sección 6), no en las computadoras de '
        'ninguna institución ni en Windows. La instalación por otro equipo y la defensa las hace el curso. El material no '
        'está validado en aulas.'], tipo='neutra')
    H.p_texto(doc, 'Cada encuentro sigue la estructura de taller de Work con la distribución por categorías de la versión 2.1. '
                   'Los tiempos son aproximados y la duración de la hora cátedra la fija cada institución.', italic=True, size=9.5)

    doc.add_heading('0. Antes del Encuentro 33: paquete, licencias, instalación por otro equipo y defensa', level=2)
    doc.add_heading('0.1 El paquete de entrega modelo y las herramientas del docente', level=3)
    for t in PAQUETE:
        H.p_texto(doc, t)
    M.tabla(doc, tabla_paquete(), [5.4, 11.2], rotulo='Paquete modelo frente a la referencia v2 con SC-02', size=8.5)
    doc.add_heading('0.2 Licencias y procedencia (borrador)', level=3)
    for t in LICENCIAS:
        H.p_texto(doc, t)
    M.tabla(doc, tabla_licencias(), [4.6, 5.4, 6.6], rotulo='Licencias de terceros verificadas (fuente primaria y versión exacta)', size=8.5)
    doc.add_heading('0.3 La instalación por otro equipo', level=3)
    for t in INSTALACION_OTRO:
        H.p_texto(doc, t)
    doc.add_heading('0.4 El paquete de Mbokaja de la Práctica 17', level=3)
    for t in MBOKAJA:
        H.p_texto(doc, t)
    doc.add_heading('0.5 Variantes reservadas para la defensa individual', level=3)
    for t in V6_PROCEDIMIENTO:
        H.p_texto(doc, t)
    M.tabla(doc, (['Campo', 'Qué contiene'], [list(c) for c in I.V6_CAMPOS]), [4.0, 12.6], rotulo='Campos de una variante V6')
    M.tabla(doc, (['Ejemplo', 'Situación', 'Qué cambia y dónde', 'Pruebas', 'Nivel Sólido'],
                  [[v['id'], v['situacion'], v['que_cambia'] + ' ' + v['modelo_y_contratos'], v['pruebas'], v['criterio_solido']]
                   for v in I.V6_EJEMPLOS]),
            [1.4, 3.6, 5.0, 3.4, 3.2], rotulo='Ejemplos públicos de variantes (no se usan en la defensa)', size=8)
    doc.add_heading('0.6 Preparación y tiempos del Encuentro 35', level=3)
    H.p_texto(doc, 'El docente prepara antes del encuentro:')
    for t in I.PREPARACION_35:
        H.p_texto(doc, '• ' + t, size=10)
    H.p_texto(doc, 'La planilla lote_6/instrumentos/planilla_tiempos_encuentro_35.xlsx calcula la duración requerida con un '
                   'solo evaluador: no se supone un segundo evaluador disponible. El docente escribe sus valores; la planilla '
                   'dice qué alternativa corresponde. Las fórmulas son las de la tabla de ejemplo, que tiene valores ficticios '
                   '(no son la duración de la HC de ninguna institución).')
    M.tabla(doc, tabla_tiempos_ejemplo(), [11.6, 5.0], rotulo='Planilla de tiempos: ejemplo con valores ficticios', size=8.5)
    H.p_texto(doc, 'Los minutos que pasan al Encuentro 36 se cuentan por defensas enteras: defensas trasladadas × minutos por '
                   'defensa. En el ejemplo pasan 2 defensas (12 minutos) y, con 5 recuperaciones de 15 minutos, quedan 48 '
                   'minutos en el Encuentro 36. Si un dato no es un entero válido (por ejemplo, 0 minutos por defensa), la '
                   'planilla no calcula y lo avisa. La planilla se comprobó con estos casos:', size=10)
    M.tabla(doc, (['Caso', 'Resultado'], [[n, 'Correcto' if b else 'FALLA'] for n, b, _ in PT.comprobar_casos()]),
            [13.0, 3.6], rotulo='Planilla de tiempos: casos de límite y de datos inválidos', size=8.5)
    M.tabla(doc, (['Alternativa', 'Cuándo', 'Qué se hace'], [[a, b, c] for a, b, c in I.ALTERNATIVAS]), [2.0, 4.0, 10.6],
            rotulo='Alternativas para el Encuentro 35 (decisión D-5)', size=8.5)

    # 1. capítulo 17
    K.titulo_en_pagina_nueva(doc, '1. %s — %s' % (cap17.CAPITULO, cap17.TITULO), nivel=2)
    M.ficha(doc, cap17)
    for titulo, filas in SEC_C17:
        M.tabla(doc, (['Momento', 'Tiempo', 'Qué se hace'], filas), ANCHO_SEC, rotulo=titulo)
    M.tabla(doc, (['Error frecuente', 'Cómo se corrige'], ERRORES_C17), [8.6, 8.0], rotulo='Errores frecuentes del Capítulo 17')
    H.p_texto(doc, 'Referencia para el docente: el núcleo de las pruebas en aislamiento (R-8) y el bloque C de la inspección '
                   'estática (R-9). El libro muestra los bloques A y D de la inspección (Códigos 17.1 y 17.2).', size=10)
    Z.codigo(doc, 'Referencia R-8')
    Z.codigo(doc, 'Referencia R-9')
    for enc, cl in (('Encuentro 33', CLAVES_E33), ('Encuentro 34', CLAVES_E34)):
        M.tabla(doc, (['Act.', 'Respuesta esperada', 'Error frecuente'], cl), [1.2, 11.0, 4.4], rotulo='Claves de las actividades del %s' % enc)
    M.tabla(doc, (['Defecto', 'Qué se cambió', 'Archivo', 'Qué se informa (herramienta)', 'Corrección'],
                  [[d[0], d[1], d[2], ' · '.join(d[3]) + ' (%s)' % d[5], d[4]] for d in MB.DEFECTOS]),
            [1.4, 3.2, 3.0, 4.4, 4.6], rotulo='Práctica 17: clave de los defectos del paquete de Mbokaja', size=8)
    c = r['herramientas']
    H.p_texto(doc, 'Comprobado en el entorno de construcción: en el paquete de Mbokaja, la inspección estática da %s y las '
                   'pruebas en aislamiento, %s (exactamente las de la clave: %s); con la clave aplicada, %s y %s, y la guía se '
                   'sigue completa (%d de %d pasos).'
              % (_r(_c(c['mbokaja']['inspeccion'])), _r(_c(c['mbokaja']['aislamiento'])), 'sí' if c['mbokaja']['exactas'] else 'no',
                 _r(_c(c['mbokaja_corregido']['inspeccion'])), _r(_c(c['mbokaja_corregido']['aislamiento'])),
                 r['guia']['mbokaja_corregido']['correctos'], r['guia']['mbokaja_corregido']['total']), size=10)
    M.tabla(doc, (['Nivel', 'Respuesta esperada'], CLAVES_P17), [2.2, 14.4], rotulo='Práctica 17: claves por nivel')
    M.tabla(doc, (['Criterio', 'Indicador'], COTEJO_P17), [13.0, 3.6], rotulo='Lista de cotejo de la Práctica 17')
    filas = [[str(n), cl, det] for eid, n, cl, det in claves if eid == cap17.EVAL_ID]
    M.tabla(doc, (['Ítem', 'Clave', 'Respuesta o criterio'], filas), [1.2, 1.8, 13.6], rotulo='Clave de la evaluación del capítulo 17')
    M.tabla(doc, (['Ítem', 'Puntaje completo', 'Puntaje parcial'], CRIT_C17), [1.2, 8.4, 7.0], rotulo='Criterios de corrección de los ítems abiertos')

    # 2. capítulo 18
    K.titulo_en_pagina_nueva(doc, '2. %s — %s' % (cap18.CAPITULO, cap18.TITULO), nivel=2)
    M.ficha(doc, cap18)
    for titulo, filas in SEC_C18:
        M.tabla(doc, (['Momento', 'Tiempo', 'Qué se hace'], filas), ANCHO_SEC, rotulo=titulo)
    M.tabla(doc, (['Error frecuente', 'Cómo se corrige'], ERRORES_C18), [8.6, 8.0], rotulo='Errores frecuentes del Capítulo 18')
    for enc, cl in (('Encuentro 35', CLAVES_E35), ('Encuentro 36', CLAVES_E36)):
        M.tabla(doc, (['Act.', 'Respuesta esperada', 'Error frecuente'], cl), [1.2, 11.0, 4.4], rotulo='Claves de las actividades del %s' % enc)
    H.p_texto(doc, 'El Capítulo 18 no tiene práctica independiente ni prueba escrita adicional (decisiones D-3 y D-4): sus '
                   'instrumentos son la demostración, la defensa individual y la evaluación integradora.', size=10)
    M.tabla(doc, (['Estudiante (código)', 'Decisión', 'Prueba', 'Variante (código)', 'Límites', 'Transferencia', 'AE'],
                  [['', '', '', '', '', '', ''] for _ in range(4)]),
            [2.8, 2.4, 2.4, 2.6, 2.2, 2.4, 1.8], rotulo='Planilla de defensa individual (niveles 1 a 4 por criterio)')
    M.tabla(doc, (['Aspecto (peso)', '4', '3', '2', '1'],
                  [['%s (%d %%)' % (a, p)] + I.NIVELES_PRODUCTO for a, p, _, _ in I.PRODUCTO]),
            [3.4, 3.5, 3.1, 3.3, 3.3], rotulo='Rúbrica de producto final (propuesta editorial, Work §4.3)', size=8)
    for t in I.INTEGRADORA:
        H.p_texto(doc, t, size=10)
    H.p_texto(doc, 'Ejemplo de cálculo, con 4, 3, 2 y 1 puntos para Sólido, Logrado, En desarrollo e Inicial: en «Pruebas y '
                   'mejora», un producto Logrado (3) con una evidencia individual Sólida (4) da 3 × 0,6 + 4 × 0,4 = 3,4; con el '
                   'peso del aspecto (15 %), aporta 0,51 a un total de 4 puntos posibles. La conversión a calificación la '
                   'decide la institución.', size=10)
    M.tabla(doc, (['Ficha', 'Cuándo se usa', 'Qué se pide', 'Evidencia', 'Prioridad'],
                  [[a, b, c_, d, str(e)] for a, b, c_, d, e in I.FICHAS_RECUPERACION]),
            [1.4, 4.2, 5.6, 3.6, 1.8], rotulo='Fichas de recuperación (las mismas de la Tabla 18.4)', size=8.5)
    for t in I.REGLA_RECUPERACION:
        H.p_texto(doc, t, size=10)
    M.tabla(doc, (['Estudiante (código)', 'Ficha', 'Qué falta', 'Qué hay que hacer', 'Fecha', 'Estado'],
                  [['', '', '', '', '', ''] for _ in range(3)]),
            [2.8, 1.4, 3.8, 4.4, 1.8, 2.4], rotulo='Registro de recuperaciones')

    # 3. rúbrica H6
    K.titulo_en_pagina_nueva(doc, '3. Rúbrica del hito H6: paquete reproducible; ajustes finales', nivel=2)
    H.p_texto(doc, 'El H6 se califica con la misma lógica que los hitos H1 a H5: nivel del producto del equipo y nivel '
                   'individual de cada integrante, combinados en la proporción 60 % y 40 %, como propuesta editorial. La '
                   'ausencia de evidencia se registra aparte («AE») y un pendiente del entorno no se cuenta como falla.')
    M.tabla(doc, (['Criterio', '4. Sólido', '3. Logrado', '2. En desarrollo', '1. Inicial'],
                  [['%s (%s)' % (x[0], x[1])] + x[2] for x in I.RUBRICA_H6]),
            [2.8, 3.6, 3.4, 3.4, 3.4], rotulo='Rúbrica del H6: descriptores por nivel', size=8.5)
    M.tabla(doc, (['Criterio', 'Evidencia del equipo (60 %)', 'Evidencia individual (40 %)'],
                  [[x[0], x[3], x[4]] for x in I.RUBRICA_H6]), [4.4, 5.8, 6.4], rotulo='Evidencias de cada criterio del H6')
    M.tabla(doc, (['Nivel de desempeño', 'Descriptor común (Work §4.3)'], [list(x) for x in cap3.NIVELES_DESEMPENO]),
            [3.6, 13.0], rotulo='Niveles de desempeño (propuesta editorial)')
    M.tabla(doc, (['Estudiante (código)', 'Criterio', 'Nivel del equipo', 'Nivel individual', 'Resultado', 'AE'],
                  [['', x[0], '', '', '', ''] for x in I.RUBRICA_H6]),
            [3.0, 5.0, 2.2, 2.2, 2.2, 2.0], rotulo='Planilla de registro del H6 (una por estudiante)')

    # 4 a 7
    doc.add_heading('4. Calendario con menos encuentros', level=2)
    H.p_texto(doc, 'En la adaptación de 28 encuentros (distribución v2.1), la Unidad VI queda sin cambios: conserva sus cuatro '
                   'encuentros y sus 20 HC. El Encuentro 28 recibe además las recuperaciones técnicas de la Unidad V, que no '
                   'tuvo encuentro de reserva; se ordenan por la prioridad de la sección 2 y lo que no se recupera se registra, '
                   'sin declararlo aprobado y sin suponer horas extraordinarias. Cada cambio de alcance se anota en la '
                   'bitácora del curso.')
    M.tabla(doc, (['Encuentro (36)', 'Encuentro (28)', 'Qué se hace'],
                  [['33', '25', 'Sin cambios: guía y manual probados por el propio equipo; Práctica 17 (nivel 3 a lectura).'],
                   ['34', '26', 'Sin cambios: instalación por otro equipo, acta y H6.'],
                   ['35', '27', 'Sin cambios: demostración y defensa individual (planilla de tiempos).'],
                   ['36', '28', 'Sin cambios en HC: recuperación (incluye las técnicas de la Unidad V), retrospectiva condensada y cierre.']]),
            [2.6, 2.6, 11.4], rotulo='Unidad VI en 36 y en 28 encuentros')
    doc.add_heading('5. Condición de cada resultado de la unidad', level=2)
    H.p_texto(doc, 'Comprobado (técnica, entorno de construcción): la guía del paquete modelo seguida por un proceso '
                   'automático, la inspección estática, las pruebas en aislamiento y sus pruebas negativas, la regresión de la '
                   'versión empaquetada y la planilla de tiempos con sus casos de límite. Simulado: el '
                   'acta con un paso fallido del Ejemplo resuelto 17.4, la retrospectiva del equipo modelo y los datos de '
                   'Mbokaja. Pendiente: la instalación por otro equipo, sin ayuda (la hace el curso), y las pruebas en Windows y '
                   'en el laboratorio (E-1 a E-12, P-13, concurrencia). Jurídico: el borrador de licencia no está cerrado.')
    doc.add_heading('6. Resultados de las pruebas y entorno en que corrieron', level=2)
    e = r['entorno']
    H.p_texto(doc, 'Entorno: %s, PHP %s, SQLite %s, %s, %s (%s). %s' % (e['sistema'], e['php'], e['sqlite'], e['curl'],
                                                                     e['bash'], e['fecha'], e['tipo']), size=10)
    filas = [['Paquete modelo', 'Código frente a la referencia v2 con SC-02', 'Idéntico' if r['paquete_modelo']['codigo_identico'] else 'NO'],
             ]
    for k, nombre in (('modelo', 'Paquete modelo'), ('mbokaja', 'Paquete de Mbokaja (con defectos)'),
                      ('mbokaja_corregido', 'Paquete de Mbokaja corregido con la clave')):
        filas.append(['Inspección estática', nombre, _r(_c(c[k]['inspeccion']))])
        filas.append(['Pruebas en aislamiento', nombre, _r(_c(c[k]['aislamiento']))])
    for x in r['pruebas_negativas']:
        filas.append(['Prueba negativa', '%s. %s' % (x['caso'], x['titulo']), 'Correcta' if x['correcto'] else 'FALLA'])
    for k, nombre in (('modelo', 'paquete modelo'), ('mbokaja_corregido', 'Mbokaja corregido'), ('mbokaja_con_defectos', 'Mbokaja con defectos')):
        g = r['guia'][k]
        filas.append(['Guía como prueba (aislada)', nombre, '%d de %d pasos' % (g['correctos'], g['total'])])
    for pr, x in r['regresion'].items():
        filas.append(['Regresión', pr, _r(x['resultado'])])
    M.tabla(doc, (['Qué', 'Prueba', 'Resultado'], filas), [3.4, 7.6, 5.6], rotulo='Resultados de las pruebas (build/reproducir.py)', size=8.5)
    H.p_texto(doc, 'Los archivos de cada ejecución, con su entorno, están en lote_6/resultados_pruebas/. La guía seguida por un '
                   'proceso automático es una comprobación técnica: no reemplaza la instalación por otro equipo.',
              italic=True, size=9.5)
    doc.add_heading('7. Procedencia y derechos de los recursos del lote', level=2)
    M.tabla(doc, (['Recurso', 'Procedencia', 'Derechos'],
                  [['Texto de los Capítulos 17 y 18 y de la apertura de la unidad', 'Redacción original para este libro.', 'Propios del proyecto.'],
                   ['Figuras 17.1 y 18.1', 'Generadas con build/diagramas_u6.py sobre el lienzo de los lotes 3 y 5; esquemas didácticos.', 'Propias; sin recursos de terceros.'],
                   ['Paquete de entrega modelo', 'Copia de la referencia v2 con SC-02 del lote 5 (que no se modifica) con los documentos de entrega.', 'Borrador de uso educativo institucional (D-2).'],
                   ['Herramientas del docente (inspección estática y pruebas en aislamiento) y prueba de la guía', 'Escritas para este lote; la v1.1 reemplaza el comprobador que traía el paquete en la v1.0.', 'Propias.'],
                   ['Paquete de Mbokaja y su logo', 'Generados por build/armar_paquetes.py; el logo es un dibujo geométrico generado por código, usado como recurso sin procedencia del caso ficticio.', 'Propios.'],
                   ['Componentes de terceros (PHP, SQLite, curl, bash)', 'No se distribuyen; licencias verificadas (sección 0.2).', 'De sus titulares.'],
                   ['Variantes V6', 'Plantilla y ejemplos en lote_6/caso/v6_plantilla.py; el banco definitivo, fuera del repositorio.', 'Propias; el banco no se publica.'],
                   ['Capacidades, niveles, 60/40, ponderación, secuencia y condiciones mínimas', 'Informe de Work v0.1 (§4.2, §4.3, §5.1, §5.2, §6, §7.4), como propuesta editorial.', 'No son documentos oficiales del MEC.']]),
            [4.4, 7.8, 4.4], rotulo='Inventario de recursos del lote')
    M.pegar_renglones(doc)
    Z.encadenar_inicio(doc)
    K.saltos_a_titulos(doc)
    H.finalizar(doc, ruta)

# -*- coding: utf-8 -*-
"""Ronda de correcciones v2 (auditoría independiente de ChatGPT + decisiones de Fer, 03/10/2026).
Se aplica al final de ediciones.aplicar(C), así que la reciben el libro, el solucionario y los planes.
Cada cambio queda en LOG con el código V2-… que cita NOTAS_PILOTO_ALGORITMICA_3_ESENCIAL_v2."""
import re

# ---------------------------------------------------------------- capacidades textuales del programa MEC
# DISEÑO CURRICULAR ALGORITMICA – MAYO 2026, Tercer curso, págs. 77–79 (copiadas letra por letra).
MEC = {
 'C1': 'Reconoce los diferentes tipos de lenguajes de programación y sus campos de aplicación.',
 'C2': 'Establece diferencias entre los distintos lenguajes de programación existentes en el mercado.',
 'C3': 'Reconoce la importancia de los diferentes tipos de lenguajes de programación existentes.',
 'C4': 'Reconoce los conceptos requeridos en la programación de base de datos utilizando un gerenciador de base de datos.',
 'C5': 'Analiza la composición de una base de datos.',
 'C6': 'Utiliza conceptos de sistema de gestión de base de datos, propósitos, inconvenientes, redundancia e inconsistencia de datos en la creación de Bases de Datos.',
 'C7': 'Identifica los diferentes niveles de abstracción de los datos.',
 'C8': 'Analiza los tipos de usuarios de base de datos.',
 'C9': 'Reconoce los diferentes lenguajes de manipulación de datos más utilizados.',
 'C10': 'Analiza los diferentes modelos de datos.',
 'C11': 'Aplica los conceptos fundamentales en la construcción de entidades.',
 'C12': 'Trabaja con el modelo Entidad Relación en la representación de los datos.',
 'C13': 'Utiliza las reglas de la normalización (1FN- 2FN- 3FN) para la obtención de datos agrupados en diferentes entidades.',
 'C14': 'Ejecuta técnicas, procedimientos y normativas en el desarrollo de entidades normalizadas.',
 'C15': 'Reconoce la importancia de la práctica Conductual en el desarrollo de las actividades.',
}
# clase → capacidades del programa que desarrolla (una capacidad puede repetirse en varias clases)
CAP_CLASE = {1: ['C1'], 2: ['C1'], 3: ['C2'], 4: ['C3'], 5: ['C4'], 6: ['C4'], 7: ['C6'], 8: ['C5'], 9: ['C5'],
             10: ['C7', 'C8', 'C9'], 11: ['C10'], 12: ['C11'], 13: ['C12'], 14: ['C12'], 15: ['C14'], 16: ['C13'],
             17: ['C13'], 18: ['C14'], 19: ['C4'], 20: ['C4'], 21: ['C4']}
CAP_TALLER = ['C14', 'C4', 'C15']
CAP_EVAL = {'E1': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], 'E2': ['C10', 'C11', 'C12', 'C13', 'C14', 'C4']}
CAP_UNIDAD = {1: ['C1', 'C2', 'C3'], 2: ['C4', 'C5', 'C6', 'C7', 'C8', 'C9'], 3: ['C10', 'C11', 'C12', 'C13', 'C14'], 4: ['C14', 'C4']}


def caps(codigos):
    return [MEC[c] for c in codigos]


ACCESS_REF = ('Los procedimientos de este libro toman como referencia Access 2016 en castellano; las versiones posteriores '
              'mantienen en general los mismos conceptos, aunque algún nombre o ubicación de comando puede variar.')

# ---------------------------------------------------------------- política de recuadros «En Paraguay»
# 'keep' = contenido paraguayo concreto y verificable · ('ret', título nuevo[, cuerpo nuevo]) · 'del' = repite el desarrollo
# 'p' = se integra al cuerpo como párrafo común (aporta una idea, pero no es un recuadro de contexto)
RECUADROS = {
 (1, 'En Paraguay — software hecho en Paraguay'): ('ret', 'Aplicación profesional — programar como oficio',
     ['Empresas y emprendimientos desarrollan software para comercio, servicios, educación y administración. Saber programar abre oportunidades laborales y de emprendimiento, siempre según las tecnologías y necesidades de cada organización.']),
 (1, 'En Paraguay — aprender a programar hoy'): 'del',
 (2, 'En Paraguay — PSeInt en el aula'): ('ret', 'Ejemplo cotidiano — PSeInt en el aula', None),
 (2, 'En Paraguay — el alto nivel es la norma'): ('ret', 'Aplicación profesional — el alto nivel es la norma', None),
 (3, 'En Paraguay — qué se enseña acá'): 'del',
 (4, 'En Paraguay — el mercado local'): 'del',
 (4, 'En Paraguay — decidir con la realidad local'): ('ret', 'Aplicación profesional — decidir con la realidad del equipo', None),
 (5, 'En Paraguay — bases de datos que usás sin darte cuenta'): 'keep',
 (5, 'En Paraguay — del cuaderno a la pantalla'): 'del',
 (5, 'En Paraguay — la memoria del negocio'): ('ret', 'Aplicación profesional — la memoria del negocio', None),
 (5, 'En Paraguay — datos malos, decisiones malas'): 'p',
 (6, 'En Paraguay — Access en el laboratorio'): 'p',
 (6, 'En Paraguay — datos públicos organizados'): ('ret', 'Aplicación profesional — registros organizados', None),
 (7, 'En Paraguay — el gestor que vas a usar'): 'del',
 (7, 'En Paraguay — la copia de seguridad no es opcional'): ('ret', 'Aplicación profesional — la copia de seguridad no es opcional',
     ['Un comercio necesita conservar durante años sus registros de ventas y comprobantes, por control interno y por sus obligaciones tributarias. Un respaldo periódico y probado (verificar que la copia realmente se puede restaurar) es la diferencia entre un susto y una pérdida irreparable.']),
 (7, 'En Paraguay — auditar empieza por el diccionario'): 'p',
 (8, 'En Paraguay — una clave principal de todos los días'): 'del',
 (8, 'En Paraguay — códigos que identifican'): 'keep',
 (9, 'En Paraguay — por qué importa'): 'keep',
 (9, 'Aplicación profesional — trazabilidad e integridad'): 'del',
 (9, 'En Paraguay — validar en la entrada, no en el juicio'): 'del',
 (10, 'En Paraguay — lo que verás en Access'): ('ret', 'Ejemplo cotidiano — DDL y DML en Access', None),
 (10, 'En Paraguay — un oficio con demanda'): ('ret', 'Aplicación profesional — un oficio con demanda', None),
 (11, 'En Paraguay — diseñar ahorra trabajo'): 'del',
 (11, 'En Paraguay — modelar lo que el negocio necesita'): ('ret', 'Aplicación profesional — sistemas empaquetados y mini-mundos',
     ['Los sistemas comerciales que se venden listos (facturación, inventario, clientes) son mini-mundos empaquetados: alguien decidió qué entidades incluir para el comercio típico. Cuando un negocio tiene necesidades distintas, ese recorte deja de servir, y ahí empieza el trabajo del diseñador de bases de datos.']),
 (11, 'En Paraguay — relevar con respeto por el oficio'): 'p',
 (12, 'En Paraguay — de la entidad a la tabla'): 'del',
 (13, 'En Paraguay — las N:M piden atención'): 'p',
 (13, 'En Paraguay — cardinalidades de la vida real'): ('ret', 'Ejemplo cotidiano — cardinalidades de la vida real', None),
 (14, 'En Paraguay — una herramienta universal'): 'del',
 (14, 'En Paraguay — leerle el diagrama al cliente'): ('ret', 'Aplicación profesional — leerle el diagrama al cliente', None),
 (14, 'En Paraguay — la pizarra como herramienta de diseño'): 'del',
 (15, 'En Paraguay — el esquema final del Copetín'): 'p',
 (17, 'En Paraguay — hasta dónde normalizar'): 'p',
 (17, 'En Paraguay — esquemas que ya nacen normalizados'): 'del',
 (18, 'En Paraguay — guardá seguido'): 'p',
 (18, 'En Paraguay — Access como puerta de entrada'): ('ret', 'Aplicación profesional — Access como puerta de entrada', None),
 (18, 'En Paraguay — la migración es el bautismo'): 'p',
 (19, 'En Paraguay — consultar es trabajo DML'): 'del',
 (20, 'En Paraguay — menos consultas, más flexibles'): 'del',
 (20, 'En Paraguay — preguntas que cambian, consultas que quedan'): 'del',
 (21, 'En Paraguay — de los datos a las decisiones'): ('ret', 'Ejemplo cotidiano — de los datos a las decisiones', None),
 (21, 'En Paraguay — del dato a la decisión'): 'del',
}


def _normalizar_cajas(C):
    """Algunas cajas del tomo traen el cuerpo pegado al título (título\\ncuerpo): se separan."""
    for c in C.values():
        for b in c['cuerpo']:
            if b['t'] == 'caja' and '\n' in b['title']:
                partes = [x for x in b['title'].split('\n') if x.strip()]
                b['title'] = partes[0]
                b['body'] = partes[1:] + list(b.get('body') or [])


def _sin_marcas(t):
    t = t.replace('. ✔ — DER validado', '. Conclusión: DER validado')
    t = re.sub(r'\s*✔', '', t)
    t = re.sub(r'\((\d[\d.]*) ✓\)', r'(\1: correcto)', t)
    return t


def aplicar(C, LOG, sub, ins, borrar, reemplazar, idx, H2, P, CAJA, TABLA):
    _normalizar_cajas(C)

    # 1 · Capacidades textuales del programa MEC
    for n, cods in CAP_CLASE.items():
        C[n]['ficha']['capacidad'] = caps(cods)
    LOG.append((0, 'V2-01', 'Las 21 fichas reproducen textualmente la capacidad del programa MEC (págs. 77–79); la Clase 10 incorpora sus tres capacidades (niveles de abstracción, tipos de usuario y lenguajes de manipulación de datos).'))

    # 2 · Clave secundaria (Clase 8)
    c = C[8]
    C[8]['ficha']['tema'] = 'Tablas, campos y registros. Clave principal, clave foránea y el término «clave secundaria».'
    reemplazar(c, 'Concepto clave — «clave secundaria»: una palabra, dos usos', CAJA('Concepto clave — el término «clave secundaria»',
        'El programa oficial emplea el término «clave secundaria» sin definirlo en este apartado. En este libro usaremos el término clave foránea para el campo que referencia la clave principal de otra tabla. En otros textos, «clave secundaria» también puede referirse a una clave alternativa o a un índice secundario.',
        'Ante la duda, preguntate qué hace el campo: si apunta a otra tabla, es foránea; si identifica sin haber sido elegido como principal, es alternativa; si solo sirve para buscar más rápido, es un índice.'),
        'V2-02', 'Clase 8: se reemplaza la afirmación de que el programa usa «clave secundaria» como sinónimo de clave foránea; texto acordado con Fer.')

    # 3 · Entidad débil (Clase 12)
    c = C[12]
    reemplazar(c, 'Una entidad débil, en cambio, solo tiene sentido junto a otra', P(
        'Una entidad fuerte existe por sí misma y tiene un identificador propio: un producto o un cliente del Copetín no dependen de nadie para tener identidad. Una entidad débil, en cambio, depende de otra para existir y para identificarse: el «renglón» de una venta (2 chipas dentro de V1) no existe sin la venta que lo contiene.'),
        'V2-03', 'Clase 12: se amplía entidad fuerte/débil (dependencia de existencia, discriminante, relación identificadora, comparación con la N:M con atributos y entidad asociativa).')
    i = idx(c, 'Una entidad fuerte existe por sí misma y tiene un identificador propio')
    c['cuerpo'][i + 1:i + 1] = [
        TABLA(['Concepto', 'Qué significa', 'En el Copetín'],
              [['Entidad fuerte', 'Existe por sí misma y tiene identificador propio', 'PRODUCTO (código), VENTA (número)'],
               ['Entidad débil', 'No existe sin otra entidad, de la que depende (dependencia de existencia)', 'RENGLÓN de una venta'],
               ['Discriminante (identificador parcial)', 'Distingue a las entidades débiles que dependen de una misma entidad fuerte, pero no alcanza solo', 'nro_renglón: 1, 2, 3… dentro de cada venta'],
               ['Relación identificadora', 'Une la débil con su fuerte y le «presta» la clave', 'VENTA tiene RENGLÓN']]),
        P('En el DER, la entidad débil se dibuja con doble rectángulo, la relación identificadora con doble rombo y el discriminante se subraya con línea discontinua. La clave de la entidad débil se forma con la clave de la fuerte más el discriminante: (venta, nro_renglón).'),
        H2('Entidad débil o relación N:M con atributos'),
        P('El renglón de venta admite dos dibujos correctos. Uno, como entidad débil RENGLÓN, que depende de VENTA. Otro, como los datos (cantidad y precio_unitario) de la relación N:M «contiene» entre VENTA y PRODUCTO. La diferencia está en qué identifica a cada renglón: en la relación N:M, la pareja venta + producto; en la entidad débil, la venta más su propio discriminante.'),
        P('En este caso, si la regla del negocio establece que un mismo producto aparece como máximo una vez dentro de cada venta, ambas alternativas pueden conducir a DetalleVenta con clave venta + producto. Si el mismo producto puede aparecer en dos renglones separados, RENGLÓN necesita un discriminante propio, por ejemplo nro_renglón, y ambos modelos ya no producen exactamente la misma clave.'),
        TABLA(['Caso', 'Regla del negocio', 'Modelo', 'Clave de DetalleVenta'],
              [['A', 'Cada producto aparece una sola vez por venta (si se piden más, se suma la cantidad)', 'Relación N:M «contiene» con atributos', '(venta, producto)'],
               ['B', 'Un producto puede aparecer en dos renglones distintos (por ejemplo, 2 empanadas cobradas y 1 de cortesía a G. 0)', 'Entidad débil RENGLÓN con discriminante nro_renglón', '(venta, nro_renglón); producto queda como clave foránea común']]),
        P('El Copetín sigue la regla del Caso A; por eso, en las Clases 13 a 15, el renglón se dibuja como la relación «contiene» con sus atributos.'),
        P('A veces una relación N:M empieza a tener vida propia: se la numera, se la consulta por sí misma o se relaciona con otras entidades. Entonces conviene dibujarla como entidad asociativa, un rectángulo que nace de la relación (en algunos textos, un rombo dentro de un rectángulo). Pasa, por ejemplo, con la inscripción de un alumno a un taller cuando además se le registran las asistencias.')]
    sub(c, 'Ejemplo — fuerte y débil en el Copetín', 'El renglón «2 chipas» solo existe dentro de la venta V1: entidad débil.',
        'El renglón «2 chipas» solo existe dentro de la venta V1: si se lo modela como entidad, es débil.',
        'V2-03b', 'Clase 12: el ejemplo aclara que el renglón es débil cuando se lo modela como entidad.')

    # 4 · Histórico de precios (Clase 11)
    c = C[11]
    sub(c, '3. Pregunta 3: «¿Los precios cambian seguido?»', 'Consecuencia: el precio vive en Productos; el histórico de precios queda fuera del mini-mundo (por ahora).',
        'Consecuencia: El precio de catálogo actual vive en Productos; queda fuera del mini-mundo un historial independiente de cambios del catálogo. Cada renglón de venta sí conserva en precio_unitario el importe realmente cobrado en esa operación.',
        'V2-04', 'Clase 11: se precisa que solo queda fuera el historial del catálogo; precio_unitario conserva lo cobrado.')

    # 6 · Access 2016 en castellano
    c = C[18]
    sub(c, 'Ya tenemos el esquema del Copetín: Productos, Clientes, Ventas y DetalleVenta.', 'el tipo de dato y la clave principal.',
        'el tipo de dato y la clave principal. ' + ACCESS_REF, 'V2-06', 'Clase 18: referencia única a Access 2016 en castellano.')
    sub(c, 'Así queda la ventana Relaciones del Copetín', '(la clave principal marcada con estrella)',
        '(la clave principal identificada con el icono/indicador de clave)', 'V2-06b', 'Clase 18: la clave principal no se marca con estrella sino con el icono de clave.')
    sub(c, 'En DetalleVenta la clave es compuesta', 'aparecen dos llaves.', 'aparecen dos iconos de clave.', 'V2-06c', 'Clase 18: «dos llaves» → «dos iconos de clave».')
    sub(c, 'Muchos negocios llegan a Access con su historia en planillas de Excel.', '(pestaña Datos externos → Nuevo origen de datos)',
        '(pestaña Datos externos → grupo Importar y vincular → Excel)', 'V2-06d', 'Clase 18: ruta de importación según Access 2016 («Nuevo origen de datos» aparece en versiones posteriores).')
    c = C[15]
    sub(c, 'Errores frecuentes — al pasar del DER a las tablas', 'usa solo un autonumérico como clave', 'usa solo un campo Autonumeración como clave',
        'V2-06e', 'Clase 15: nombre del tipo de dato de Access en castellano (Autonumeración).')
    c = C[8]
    sub(c, 'Tipo de dato Guarda Ejemplo en el Copetín', 'Autonumérico', 'Autonumeración', 'V2-06f', 'Clase 8: tipo Autonumeración.')
    sub(c, 'Las claves se consiguen de dos maneras.', 'o el autonumérico que Access asigna solo', 'o el campo Autonumeración que Access numera solo',
        'V2-06g', 'Clase 8: tipo Autonumeración.')
    sub(c, 'Criterio Clave natural Clave artificial', 'P01, V1, autonumérico', 'P01, V1, Autonumeración', 'V2-06h', 'Clase 8: tipo Autonumeración.')
    c = C[21]
    sub(c, '2. Convertirla en referencia cruzada:', 'Convertirla en referencia cruzada:',
        'Convertirla en referencia cruzada (con el Asistente para consultas de la pestaña Crear o, en la vista Diseño, cambiando el tipo de consulta a referencias cruzadas):',
        'V2-06i', 'Clase 21: se indica dónde se elige la consulta de referencias cruzadas.')
    sub(c, 'El destino final de muchas consultas está fuera de Access', 'a PDF (para compartir sin que se modifique)',
        'a PDF (botón PDF o XPS, para compartir sin que se modifique)', 'V2-06j', 'Clase 21: botón PDF o XPS de Datos externos.')

    # 7 · Fechas: criterio de lectura explícito (Clase 19)
    c = C[19]
    sub(c, 'Errores frecuentes — fechas en las consultas', 'y en SQL aparece como #3/4/2026#.',
        'y en SQL aparece como #3/4/2026#. En este libro, todos los criterios de fecha están escritos en la cuadrícula de Diseño de un equipo configurado con día/mes/año.',
        'V2-07', 'Clase 19: se declara que los criterios del libro están escritos en la cuadrícula con configuración d/m/a.')

    # 11 · Recuadros «En Paraguay»
    for (n, tit), acc in RECUADROS.items():
        c = C[n]
        i = idx(c, tit, 'caja')
        b = c['cuerpo'][i]
        if acc == 'keep':
            continue
        if acc == 'del':
            del c['cuerpo'][i]
            LOG.append((n, 'V2-11', 'Recuadro «%s» eliminado: repetía el desarrollo o no era específico de Paraguay.' % tit))
        elif acc == 'p':
            c['cuerpo'][i] = P(' '.join(b['body']))
            LOG.append((n, 'V2-11', 'Recuadro «%s»: su contenido no es específico de Paraguay; se integra al texto como párrafo.' % tit))
        else:
            _, nuevo, cuerpo = acc
            b['title'] = nuevo
            if cuerpo:
                b['body'] = cuerpo
            LOG.append((n, 'V2-11', 'Recuadro «%s» → «%s» (contenido universal).' % (tit, nuevo)))
    restantes = [(n, b['title']) for n, c in C.items() for b in c['cuerpo'] if b['t'] == 'caja' and b['title'].startswith('En Paraguay')]
    assert all((n, t) in RECUADROS and RECUADROS[(n, t)] == 'keep' for n, t in restantes), restantes

    # 14 · Símbolos ✔ / ✓ del tomo (dependen de una fuente de emoji): se reemplazan por texto
    k = 0
    for c in C.values():
        for b in c['cuerpo']:
            for key in ('text', 'title'):
                if key in b and re.search('[✔✓]', b[key]):
                    b[key] = _sin_marcas(b[key]); k += 1
            if 'body' in b and any(re.search('[✔✓]', x) for x in b['body']):
                b['body'] = [_sin_marcas(x) for x in b['body']]; k += 1
    LOG.append((0, 'V2-14', 'Se quitan %d marcas ✔/✓ del texto (dependían de una fuente de emoji y podían perderse al convertir o copiar).' % k))
    return C

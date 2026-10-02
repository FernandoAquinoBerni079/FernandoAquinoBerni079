# -*- coding: utf-8 -*-
"""Correcciones y ampliaciones de las 21 clases (cada una documentada en NOTAS_PILOTO).
Opera sobre la estructura que devuelve estructura.cargar()."""
import re

LOG = []          # (clase, código, descripción) — alimenta las notas del piloto


def _txt(b):
    if b['t'] in ('p', 'h2', 'h3'):
        return b['text']
    if b['t'] == 'caja':
        return b['title'] + ' ' + ' '.join(b['body'])
    if b['t'] == 'tabla':
        return ' '.join(b['hdr']) + ' ' + ' '.join(' '.join(r) for r in b['rows'])
    if b['t'] == 'img':
        return b['file'] + ' ' + b.get('epigrafe', '')
    return ''


def idx(c, sub, t=None):
    hits = [i for i, b in enumerate(c['cuerpo']) if sub in _txt(b) and (t is None or b['t'] == t)]
    assert len(hits) == 1, ('anclaje ambiguo o ausente', c['n'], sub, hits)
    return hits[0]


def sub(c, ancla, viejo, nuevo, cod, desc):
    b = c['cuerpo'][idx(c, ancla)]
    hecho = False
    for k in ('text', 'title'):
        if k in b and viejo in b[k]:
            b[k] = b[k].replace(viejo, nuevo); hecho = True
    if 'body' in b:
        b['body'] = [x.replace(viejo, nuevo) if viejo in x else x for x in b['body']]
        hecho = hecho or any(nuevo in x for x in b['body'])
    if b['t'] == 'tabla':
        b['hdr'] = [x.replace(viejo, nuevo) for x in b['hdr']]
        b['rows'] = [[x.replace(viejo, nuevo) for x in r] for r in b['rows']]
        hecho = True
    if 'epigrafe' in b and viejo in b['epigrafe']:
        b['epigrafe'] = b['epigrafe'].replace(viejo, nuevo); hecho = True
    assert hecho, ('no se encontró', c['n'], viejo)
    LOG.append((c['n'], cod, desc))


def ins(c, ancla, bloques, cod, desc, antes=False):
    i = idx(c, ancla)
    pos = i if antes else i + 1
    c['cuerpo'][pos:pos] = bloques
    LOG.append((c['n'], cod, desc))


def borrar(c, ancla, cod, desc):
    i = idx(c, ancla)
    del c['cuerpo'][i]
    LOG.append((c['n'], cod, desc))


def reemplazar(c, ancla, bloque, cod, desc):
    c['cuerpo'][idx(c, ancla)] = bloque
    LOG.append((c['n'], cod, desc))


def H2(t): return {'t': 'h2', 'text': t}
def P(t): return {'t': 'p', 'text': t}
def CAJA(tit, *body): return {'t': 'caja', 'title': tit, 'body': list(body)}
def TABLA(hdr, rows): return {'t': 'tabla', 'hdr': hdr, 'rows': rows}
def FIG(file, lead, epi, ancho=14.5): return {'t': 'img', 'file': file, 'ancho_cm': ancho, 'lead': lead, 'epigrafe': epi, 'nueva': True}


def aplicar(C):
    # ------------------------------------------------------------------ Clase 2
    c = C[2]
    sub(c, 'En Paraguay — PSeInt en el aula', 'PSeInt, que usás para practicar algoritmos, funciona como un intérprete: ejecuta el pseudocódigo paso a paso y te muestra el resultado al instante.',
        'PSeInt, que usás para practicar algoritmos, trabaja como un intérprete: analiza el pseudocódigo, lo ejecuta en el momento (incluso paso a paso) y te muestra el resultado al instante, sin generar un ejecutable aparte.',
        'C2-1', 'Precisión sobre PSeInt: ejecuta sin generar ejecutable; se menciona la ejecución paso a paso que se usa en la Práctica 2.')

    # ------------------------------------------------------------------ Clase 3
    c = C[3]
    sub(c, 'Paradigma Idea central Propiedad clave', 'C, PSeInt', 'C, pseudocódigo de PSeInt', 'C3-1',
        'PSeInt es una herramienta que interpreta pseudocódigo, no un lenguaje de programación comercial: se precisa la celda.')

    c = C[6]
    sub(c, 'El modelo relacional no fue el primero ni es el único', 'útiles cuando los datos no encajan bien en tablas.',
        'útiles cuando los datos no encajan bien en tablas. La figura compara los mismos datos organizados como árbol jerárquico y como tablas relacionadas.',
        'C6-1', 'La Figura 6.1 no estaba anunciada en el texto: se agrega la frase que la presenta.')

    # ------------------------------------------------------------------ Clase 8
    c = C[8]
    ins(c, 'Concepto clave — clave principal y clave foránea', [
        CAJA('Concepto clave — «clave secundaria»: una palabra, dos usos',
             'El programa oficial habla de «clave principal y secundaria». En este libro, siguiendo ese uso, la clave secundaria es la clave foránea: el campo que apunta a la clave principal de otra tabla.',
             'Atención al leer otros textos: algunos autores llaman «clave secundaria» a una clave alternativa (otro campo que también sería único, como la cédula si la clave elegida es el código) o a un campo indexado para buscar más rápido. Ante la duda, preguntate qué hace el campo: si apunta a otra tabla, es foránea; si identifica sin haber sido elegido como principal, es alternativa.')],
        'C8-1', 'Aclaración terminológica «clave secundaria» (programa) = clave foránea en el libro; se advierten los otros dos usos frecuentes (clave alternativa, índice secundario).')

    # ------------------------------------------------------------------ Clase 9
    c = C[9]
    sub(c, 'Cuando una orden amenaza la integridad referencial',
        'restringir (rechazar la orden), propagar en cascada (borrar también las ventas del cliente) o anular la referencia (dejar las ventas sin cliente asignado).',
        'restringir (rechazar la orden), propagar en cascada (borrar también las ventas del cliente) o anular la referencia (dejar las ventas sin cliente asignado). En la ventana Relaciones de Access vas a encontrar dos casillas, «Actualizar en cascada los campos relacionados» y «Eliminar en cascada los registros relacionados»; si ninguna está marcada, Access restringe. La tercera reacción, anular la referencia, existe en otros gestores y no se configura desde esa ventana.',
        'C9-1', 'Se indica qué opciones ofrece realmente Access (casillas de cascada) y que «anular referencia» no se configura desde la ventana Relaciones.')

    # ------------------------------------------------------------------ Clase 10
    c = C[10]
    ins(c, 'Tres niveles de abstracción', [
        FIG('fig_10_1_niveles.png',
            'Observá la figura de arriba hacia abajo: cada usuario mira la base a través de su vista; las vistas se arman sobre las tablas del nivel lógico, y las tablas viven guardadas en el archivo del nivel físico. Seguí la flecha punteada: un cambio abajo no obliga a cambiar lo de arriba.',
            'Los tres niveles de abstracción aplicados a la base del Copetín Karumbé.', 15.0)],
        'C10-1', 'Nuevo diagrama de los tres niveles de abstracción con el caso (la clase no tenía figuras).')
    # la tabla queda después de la figura: mover la figura antes de la tabla del nivel
    i_fig = idx(c, 'fig_10_1_niveles.png'); i_tab = idx(c, 'Nivel Qué describe Quién lo usa')
    if i_tab < i_fig:
        f = c['cuerpo'].pop(i_fig); c['cuerpo'].insert(i_tab + 1, f)

    # ------------------------------------------------------------------ Clase 11
    c = C[11]
    b = c['cuerpo'][idx(c, 'Modelo de datos Idea central')]
    b['rows'].append(['Lógico basado en objetos', 'Los datos se guardan como objetos con atributos y métodos (bases orientadas a objetos)'])
    LOG.append((11, 'C11-1', 'Se agrega a la tabla el «modelo lógico basado en objetos», que figura en el programa y faltaba.'))

    # ------------------------------------------------------------------ Clase 12
    c = C[12]
    sub(c, 'Una entidad débil, en cambio, solo tiene sentido junto a otra',
        'Las entidades débiles suelen identificarse combinando su clave con la de la entidad fuerte de la que dependen.',
        'Las entidades débiles suelen identificarse combinando su clave con la de la entidad fuerte de la que dependen; en el DER se dibujan con doble rectángulo. Un mismo hecho admite a veces dos dibujos correctos: el renglón de venta puede modelarse como entidad débil RENGLÓN o como los datos de la relación N:M «contiene» entre VENTA y PRODUCTO. En este libro usamos la segunda forma (Clases 13 a 15); las dos producen exactamente la misma tabla DetalleVenta, con clave venta + producto.',
        'C12-1', 'Se reconcilia «renglón = entidad débil» (Clase 12) con «renglón = atributos de la relación contiene» (Clases 13–15): son dos modelados equivalentes que producen la misma tabla.')
    ins(c, 'Tipo de atributo Ejemplo Simple precio del producto', [
        FIG('fig_12_1_atributos.png',
            'La figura muestra cómo se dibuja cada tipo de atributo en la notación clásica. Fijate en tres detalles: el identificador va subrayado, el multivaluado lleva doble elipse y el derivado, contorno punteado.',
            'Notación de los tipos de atributo, sobre la entidad CLIENTE.', 15.0)],
        'C12-2', 'Nuevo diagrama de notación de atributos (simple, compuesto, multivaluado, derivado, identificador): la clase no tenía figuras.')

    # ------------------------------------------------------------------ Clase 13
    c = C[13]
    sub(c, 'La cardinalidad (o ligadura de correspondencia) dice cuántos',
        'y de muchos a muchos (N:M) cuando varios se vinculan con varios.',
        'y de muchos a muchos (N:M) cuando varios se vinculan con varios. El programa nombra también la ligadura «varios a uno» (N:1): no es una cuarta categoría, sino la misma 1:N leída desde el otro extremo («muchas ventas pertenecen a un cliente»).',
        'C13-1', 'Se explicita la ligadura «varios a uno» del programa como 1:N leída al revés.')
    ins(c, 'Nada impide que una entidad se relacione consigo misma', [
        H2('Grado de una relación: unaria, binaria y ternaria'),
        P('Cuántas entidades participan en una relación es su grado. Una relación recursiva, como la del empleado que supervisa a otros empleados, es de grado uno (unaria). «Cliente realiza Venta» es de grado dos (binaria), el caso más frecuente. Y existen relaciones de grado tres (ternarias), en las que el hecho solo tiene sentido si se nombran tres entidades a la vez.'),
        FIG('fig_13_3_grado.png',
            'Compará los tres dibujos de la figura: lo que cambia es cuántos rectángulos toca el rombo. En la ternaria, el rombo «dicta» une tres entidades a la vez.',
            'Grado de una relación: unaria, binaria y ternaria.', 15.0),
        TABLA(['Grado', 'Entidades que participan', 'Ejemplo'],
              [['Unaria (1)', 'Una entidad consigo misma', 'EMPLEADO supervisa EMPLEADO'],
               ['Binaria (2)', 'Dos entidades', 'CLIENTE realiza VENTA'],
               ['Ternaria (3)', 'Tres entidades a la vez', 'DOCENTE dicta MATERIA en CURSO']]),
        CAJA('Ejemplo — por qué la ternaria no se parte en dos',
             'En un colegio, la profesora Benítez dicta Algorítmica en 3.º A y Matemática en 3.º B. Si guardáramos solo «Benítez dicta Algorítmica» y «Benítez enseña en 3.º A», no sabríamos qué materia da en cada curso: el hecho «quién dicta qué y dónde» necesita las tres entidades juntas. Esa es la señal de una relación ternaria.')],
        'C13-2', 'Se agrega el «grado de relacionamiento» del programa (unaria, binaria, ternaria) con figura, tabla y ejemplo.')
    ins(c, 'Ejemplo — el contrato leído contra los datos', [
        CAJA('Errores frecuentes — al determinar cardinalidades',
             '1. Mirar un solo sentido. «Un cliente hace muchas ventas» no alcanza: falta preguntar cuántos clientes tiene una venta. La cardinalidad sale de las dos lecturas juntas.',
             '2. Decidir por los datos de hoy. Si hoy cada cliente compró una sola vez, igual la relación es 1:N: la regla del negocio permite volver a comprar.',
             '3. Confundir máximo con mínimo. «Un producto puede no haberse vendido» habla del mínimo (0); no cambia que el máximo sea N.',
             '4. Inventar una 1:1 que es 1:N. Antes de declarar 1:1, buscá un caso real donde un lado tenga dos: si existe, la relación es 1:N.')],
        'C13-3', 'Recuadro «Errores frecuentes» sobre cardinalidades (clase crítica).')

    # ------------------------------------------------------------------ Clase 14
    c = C[14]
    sub(c, 'Con tres entidades y sus vínculos, el DER del Copetín queda así',
        'que lleva el atributo cantidad.', 'que lleva los atributos cantidad y precio_unitario.',
        'C14-1', 'T1: el texto decía que «contiene» lleva solo cantidad; se iguala a la Figura y a la Clase 15 (cantidad y precio_unitario).')
    sub(c, 'Ejemplo — leer el DER del Copetín', 'indicando la cantidad».', 'indicando la cantidad y el precio unitario cobrado».',
        'C14-2', 'T1 (lectura del DER): se agrega precio_unitario.')
    sub(c, 'Paso 4 — Atributos', 'y el atributo cantidad sobre el rombo «contiene» — pertenece a la relación, no a las entidades.',
        'y los atributos cantidad y precio_unitario sobre el rombo «contiene»: pertenecen a la relación, no a las entidades.',
        'C14-3', 'T1 (paso 4 del ejemplo resuelto): se agrega precio_unitario.')
    ins(c, 'Concepto clave — el atributo que pide ser entidad', [
        H2('Cuestiones de diseño: ¿entidad, atributo o relación?'),
        P('El programa pide resolver dos «cuestiones de diseño». La primera ya la viste: un dato que tiene datos propios merece ser entidad y no atributo. La segunda es más sutil: ¿un hecho del negocio se dibuja como entidad o como relación? La pregunta que decide es si ese hecho tiene identidad propia, es decir, si se lo nombra, se lo numera y se lo consulta por sí mismo.'),
        TABLA(['Situación', 'Se modela como', 'Por qué'],
              [['El cliente tiene código, nombre y teléfono', 'Entidad CLIENTE', 'Tiene datos propios: no puede ser una elipse de VENTA'],
               ['El teléfono del cliente', 'Atributo de CLIENTE', 'Es un dato suelto, sin datos propios'],
               ['La venta tiene número, fecha y cliente', 'Entidad VENTA', 'Se la numera y se la consulta por sí misma'],
               ['Qué productos lleva cada venta', 'Relación N:M «contiene»', 'No tiene número propio: es el encuentro venta-producto'],
               ['El préstamo de un libro tiene número de recibo y fecha de devolución', 'Entidad PRÉSTAMO', 'Tiene identidad (el recibo) y vida propia (se devuelve, se renueva)']]),
        CAJA('Concepto clave — la prueba del número propio',
             'Si el negocio le pone número al hecho (venta N.º 1, recibo de préstamo N.º 58), probablemente es una entidad. Si el hecho solo existe como vínculo entre dos cosas y se identifica por ellas, es una relación, y sus datos van sobre el rombo.')],
        'C14-4', 'Se agregan las «cuestiones de diseño» del programa: entidad o atributo, y entidad o relación, con tabla de decisión.')

    # ------------------------------------------------------------------ Clase 15
    c = C[15]
    b = c['cuerpo'][idx(c, 'DetalleVenta Producto Cantidad Precio unitario')]
    b['hdr'] = ['Venta (FK)', 'Producto (FK)', 'Cantidad', 'Precio unitario (G.)']
    nombres = {'Chipa': 'P01', 'Mbeju': 'P02', 'Empanada': 'P03', 'Milanesa': 'P04', 'Cocido': 'P05', 'Gaseosa': 'P06'}
    b['rows'] = [[r[0], nombres[r[1]] + ' (' + r[1] + ')', r[2], r[3]] for r in b['rows']]
    LOG.append((15, 'C15-1', 'T3: la tabla rotulaba «DetalleVenta» la columna de la venta y mostraba nombres en lugar del código; ahora muestra las FK (venta, producto) con el nombre como ayuda.'))
    sub(c, 'Una relación N:M no se puede guardar directamente en dos tablas: se crea una tabla intermedia.',
        'se crea una tabla intermedia.', 'se crea una tabla intermedia (también llamada tabla puente o de unión).',
        'C15-2', 'Se agrega el término «tabla puente» pedido por Fer.')
    sub(c, '2. Claves foráneas: cliente en Ventas',
        'del mismo tipo (texto de 3 caracteres)', 'del mismo tipo de dato que la clave a la que apuntan (Texto corto)',
        'C15-3', 'T4: los códigos de venta tienen 2 caracteres; se corrige «texto de 3 caracteres».')
    sub(c, 'La relación 1:1 conecta registros de a uno',
        'la clave foránea puede ir en cualquiera de las dos tablas (se elige la del lado con participación obligatoria) — o directamente fusionarse las dos entidades en una tabla, si siempre van juntas.',
        'la clave foránea puede ir en cualquiera de las dos tablas (conviene la del lado con participación obligatoria, para que no queden valores vacíos) y debe declararse sin duplicados: en Access, con la propiedad Indexado = «Sí (Sin duplicados)». Sin esa restricción, dos empleados podrían apuntar a la misma cuenta y la relación se convertiría, sin aviso, en 1:N. La otra salida es fusionar las dos entidades en una sola tabla, si siempre van juntas.',
        'C15-4', 'T5: en la 1:1 la FK debe ser única (índice sin duplicados); sin eso la relación degenera en 1:N.')
    sub(c, '1:1 FK en el lado obligatorio', 'FK en el lado obligatorio, o fusión', 'FK única (sin duplicados) en el lado obligatorio, o fusión',
        'C15-5', 'T5 en la tabla resumen de reglas.')
    ins(c, 'Concepto clave — dos controles, dos preguntas distintas', [
        CAJA('Errores frecuentes — al pasar del DER a las tablas',
             '1. Poner la FK del lado equivocado. En una 1:N, la clave del «uno» viaja al «muchos». Si guardáramos el código de venta dentro de Clientes, cada cliente podría tener una sola venta.',
             '2. Meter una lista en una celda. Resolver la N:M con un campo «productos» que diga «P01, P06» en Ventas viola la 1FN y no permite guardar cantidad ni precio de cada producto.',
             '3. Olvidar los atributos del rombo. Si DetalleVenta queda solo con (venta, producto), se pierde cuántas unidades se vendieron y a qué precio.',
             '4. Clave de la tabla puente sin control. Si DetalleVenta usa solo un autonumérico como clave y nadie controla que la pareja venta + producto no se repita, el mismo producto puede cargarse dos veces en la misma venta. La clave compuesta lo impide por diseño.')],
        'C15-6', 'Recuadro «Errores frecuentes» de la transformación DER → tablas (clase crítica).')

    # ------------------------------------------------------------------ Clase 16
    c = C[16]
    b = c['cuerpo'][idx(c, 'Anomalía Qué pasa De inserción')]
    b['rows'] = [['De inserción', 'No se puede cargar un producto nuevo hasta que alguien lo compre'],
                 ['De actualización', 'Cambiar el precio obliga a corregir muchos renglones'],
                 ['De borrado', 'Al borrar la única venta de un producto o de un cliente, se pierden también sus datos']]
    LOG.append((16, 'C16-1', 'T7: la anomalía de borrado ocurre al borrar la ÚNICA venta de un producto o cliente; se corrige la generalización.'))
    reemplazar(c, 'En Paraguay — dependencia funcional', CAJA('Concepto clave — dependencia funcional',
        'Un campo A determina un campo B (se escribe A → B) si a cada valor de A le corresponde siempre un único valor de B. Ejemplo: código de producto → precio de catálogo.'),
        'C16-2', 'T9: la caja estaba rotulada «En Paraguay» pero solo definía DF; pasa a «Concepto clave».')
    reemplazar(c, 'Ejemplo — la cuenta de la redundancia', CAJA('Ejemplo — la cuenta de la redundancia',
        'Se cuenta columna por columna, comparando cuántos renglones hay con cuántos valores distintos del «dueño» del dato existen. La fecha y el cliente dependen de la venta: 11 renglones para 5 ventas, 6 celdas repetidas en cada columna (12). El nombre del cliente depende del cliente: 11 renglones para 4 clientes, 7 repetidas. Nombre, categoría y precio dependen del producto: 11 renglones para 6 productos, 5 repetidas en cada columna (15).',
        'Total: 12 + 7 + 15 = 34 celdas que repiten un dato ya escrito en otro renglón, contra 0 en el esquema normalizado, donde cada dato vive una sola vez y las claves hacen el resto.'),
        'C16-3', 'T8: el cálculo «11 × 5 ≈ 55 celdas» era incorrecto (la primera aparición no es redundante). Recalculado columna por columna: 34 celdas (verificado por script).')
    ins(c, 'Ejemplo resuelto — detectar dependencias funcionales en la tabla única', [
        FIG('fig_16_1_dependencias.png',
            'Antes de leer el ejemplo, recorré la figura: cada flecha sale de lo que determina y llega a lo que queda determinado. Las flechas verdes nacen de la clave completa (venta + producto); las ámbar, de una sola parte de la clave, y la roja pasa por un campo que no es clave.',
            'Diagrama de dependencias funcionales de la tabla única del Copetín.', 15.5)],
        'C16-4', 'Nuevo diagrama de dependencias funcionales (completa, parcial y transitiva) sobre la tabla única: la clase no tenía figuras.', antes=True)
    ins(c, 'Concepto clave — la pregunta de la parcialidad', [
        H2('Dependencia funcional: regla, no coincidencia'),
        P('Una dependencia funcional describe una regla del negocio, no una casualidad de los datos de hoy. En el Copetín, los seis precios son distintos (3.000, 5.000, 6.000, 15.000, 4.000 y 8.000), así que en esta tabla cada precio aparece con un solo producto. ¿Vale entonces «precio → producto»? No: mañana el jugo puede costar G. 6.000, igual que la empanada, y la supuesta regla se rompe. En cambio, «producto → precio de catálogo» vale siempre, porque el negocio decide un único precio de lista por producto.'),
        P('El programa usa también el nombre dependencia funcional compuesta o completa para la que necesita toda una clave compuesta, como venta + producto → cantidad. Es la que la segunda forma normal quiere conservar; la parcial, la que quiere eliminar.'),
        CAJA('Errores frecuentes — al escribir dependencias funcionales',
             '1. Leer la flecha al revés: «precio → producto» no es lo mismo que «producto → precio».',
             '2. Tomar una coincidencia de los datos por una regla: que hoy no haya dos precios iguales no crea una dependencia.',
             '3. Olvidar las dependencias de la clave compuesta: la cantidad no depende de la venta ni del producto por separado, sino de los dos juntos.',
             '4. Confundir dependencia con relación entre tablas: la DF es entre campos y se usa para decidir en qué tabla va cada uno.')],
        'C16-5', 'T10: se distingue DF (regla del negocio) de coincidencia en los datos; se usa el término del programa «DF compuesta o completa»; recuadro «Errores frecuentes».')

    # ------------------------------------------------------------------ Clase 17
    c = C[17]
    sub(c, '3. 2FN — dependencias completas de la clave',
        'Se separan Productos y Ventas; DetalleVenta conserva venta, producto, cantidad y precio_unitario, porque estos dos últimos describen el renglón de esa venta.',
        'Se separan Productos (producto, nombre, categoría, precio) y Ventas (venta, fecha, cliente, nombre del cliente); DetalleVenta conserva venta, producto, cantidad y precio_unitario, porque estos dos últimos describen el renglón de esa venta. Observá que el nombre del cliente viajó a Ventas junto con el cliente: depende de la venta, pero «de rebote».',
        'C17-1', 'T11: se hace explícito que, tras la 2FN, el nombre del cliente queda en Ventas (dependencia transitiva que la 3FN corta).')
    sub(c, '4. 3FN — sin transitividades',
        'el nombre del cliente depende de la venta a través del código de cliente. Se separa: nace Clientes (C01 a C04).',
        'en Ventas, el nombre del cliente depende de la venta a través del código de cliente (venta → cliente → nombre). Se separa: nace Clientes (C01 a C04) y en Ventas queda solo el código del cliente como clave foránea.',
        'C17-2', 'T11: se muestra la cadena transitiva venta → cliente → nombre.')
    ins(c, 'Concepto clave — las tres formas normales', [
        CAJA('Errores frecuentes — al normalizar',
             '1. Buscar dependencias parciales donde no puede haberlas. Si la clave tiene un solo campo, no existe «una parte» de la clave: una tabla en 1FN con clave simple ya está en 2FN.',
             '2. Sacar precio_unitario de DetalleVenta «porque el precio va en Productos». El precio de catálogo va en Productos; lo cobrado en cada venta es otro hecho y se queda en el renglón.',
             '3. Creer que 1FN es «separar todo en partes». Atomicidad es un valor por celda para lo que el negocio usa como unidad: dividir el nombre en nombre y apellido es una decisión de diseño, no una exigencia de la 1FN.',
             '4. Saltar pasos. Aplicar la 3FN sin haber resuelto la 2FN deja dependencias parciales escondidas.',
             '5. Perder información al partir. Toda separación debe dejar una clave para volver a unir los datos: si desde las tablas no se reconstruyen los G. 134.000, la normalización está mal hecha.')],
        'C17-3', 'Recuadro «Errores frecuentes» de normalización (incluye T13: clave simple en 1FN ⇒ 2FN).')

    # ------------------------------------------------------------------ Clase 18
    c = C[18]
    sub(c, 'Para crear la tabla Productos: en la pestaña Crear se elige Diseño de tabla',
        'con el botón Clave principal.',
        'con el botón Clave principal. En DetalleVenta la clave es compuesta: se seleccionan las dos filas venta y producto con los selectores de fila de la izquierda (manteniendo presionada la tecla Ctrl) y se pulsa una sola vez Clave principal; aparecen dos llaves.',
        'C18-1', 'T21: se explica cómo crear la clave principal compuesta en la vista Diseño.')
    sub(c, 'Con las tablas creadas, en la pestaña Herramientas de base de datos se abre Relaciones',
        'Al crear la relación se activa la casilla Exigir integridad referencial.',
        'Al crear la relación se activa la casilla Exigir integridad referencial. Debajo aparecen otras dos casillas: Actualizar en cascada los campos relacionados (recomendable) y Eliminar en cascada los registros relacionados (que conviene dejar desmarcada, por lo visto en la Clase 9).',
        'C18-2', 'Se nombran las casillas reales de cascada de Access y la recomendación coherente con la Clase 9.')
    sub(c, '3. Importación en orden de integridad', 'el mismo orden de la Figura 4.4', 'el mismo orden de la {FIG:image23.jpg}',
        'C18-3', 'Referencia cruzada a figura renumerada automáticamente.')

    # ------------------------------------------------------------------ Clase 19
    c = C[19]
    ins(c, 'Concepto clave — anticipá antes de ejecutar', [
        CAJA('Errores frecuentes — fechas en las consultas',
             '1. Día y mes cruzados. En la cuadrícula de diseño, Access interpreta la fecha según la configuración regional del equipo (en Paraguay, día/mes/año). En la vista SQL, en cambio, los literales entre numerales se escriben siempre mes/día/año: #04/03/2026# en la cuadrícula es el 4 de marzo y en SQL aparece como #3/4/2026#.',
             '2. Probar con fechas engañosas. El 03/03 se lee igual en los dos órdenes y no delata el error. Para verificar una consulta de fechas, probá con un día mayor que 12 (por ejemplo, el 15/03), que no admite dos lecturas.',
             '3. Escribir la fecha como texto. "04/03/2026" entre comillas no es una fecha: la consulta no devuelve nada o da un error de tipos. Las fechas van entre numerales.')],
        'C19-1', 'T14: advertencia sobre el formato de fechas en Access (cuadrícula regional vs. SQL mm/dd/aaaa) y cómo probar sin ambigüedad.')

    # ------------------------------------------------------------------ Clase 20 → mover tabla de totales a la Clase 21
    c = C[20]
    i = idx(c, 'Función de la fila Total')
    tabla_tot = c['cuerpo'].pop(i)
    i = idx(c, 'Concepto clave — del registro al resumen')
    caja_tot = c['cuerpo'].pop(i)
    sub(c, 'Una consulta paramétrica conviene guardarla con un nombre',
        'Así la misma consulta puede reutilizarse sin convertirla todavía en una consulta de totales; los agregados se introducen recién en la Clase 21.',
        'Así la misma consulta puede reutilizarse en otros objetos (un formulario de búsqueda, un informe) sin que nadie tenga que adivinar qué pide ni qué devuelve.',
        'C20-1', 'T15: se retira de la Clase 20 la tabla de funciones de la fila Total (anticipaba la Clase 21) y se reubica en la Clase 21.')
    sub(c, 'Como "*" & [Parte del nombre] & "*"', '«an» devuelve Empanada y Ana Gómez (según la tabla)',
        '«an» devuelve Empanada (en Productos) o Ana Gómez (en Clientes)',
        'C20-2', 'T16: el resultado mezclaba dos tablas en una misma consulta.')

    # ------------------------------------------------------------------ Clase 21
    c = C[21]
    i = idx(c, 'La recaudación total del Copetín es G. 134.000 en 5 ventas')
    c['cuerpo'][i + 1:i + 1] = [tabla_tot, caja_tot]
    LOG.append((21, 'C21-1', 'Recibe la tabla de funciones de la fila Total y la caja «del registro al resumen» que estaban adelantadas en la Clase 20.'))
    # libro único: «tomo» y «cuadernillo» pasan a «libro»
    cambios = 0
    for n, c in C.items():
        for b in c['cuerpo']:
            for k in ('text', 'title'):
                if k in b:
                    nuevo = re.sub(r'\b(tomo|cuadernillo)\b', 'libro', b[k])
                    cambios += nuevo != b[k]; b[k] = nuevo
            if 'body' in b:
                nb = [re.sub(r'\b(tomo|cuadernillo)\b', 'libro', x) for x in b['body']]
                cambios += nb != b['body']; b['body'] = nb
            if 'rows' in b:
                b['rows'] = [[re.sub(r'\b(tomo|cuadernillo)\b', 'libro', x) for x in r] for r in b['rows']]
    LOG.append((0, 'G-1', 'Libro único: %d menciones de «tomo» o «cuadernillo» pasan a «libro».' % cambios))
    return C


def fig_refs(C):
    """Numera las figuras por clase (N.M) y devuelve {archivo: 'Figura N.M'}."""
    mapa = {}
    for n, c in C.items():
        k = 0
        for b in c['cuerpo']:
            if b['t'] == 'img':
                k += 1
                num = 'Figura %d.%d' % (n, k)
                mapa[b['file']] = num
                ep = b.get('epigrafe', '')
                ep = re.sub(r'^Figura \d+\.\d+\s*[—-]\s*', '', ep)
                b['epigrafe'] = num + ' — ' + ep
                b['num'] = num
    for n, c in C.items():
        for b in c['cuerpo']:
            for k in ('text',):
                if k in b and '{FIG:' in b[k]:
                    b[k] = re.sub(r'\{FIG:([^}]+)\}', lambda m: mapa[m.group(1)], b[k])
    return mapa

# -*- coding: utf-8 -*-
"""Correcciones y ampliaciones de las 21 clases de Algorítmica 2.º (Edición Esencial Comercial 2026).
Cada cambio queda registrado en LOG con su código (C<n>-<k>) para las notas del piloto. Se aplican desde el
inicio las decisiones de Fer de la ronda v2/v2.1 del piloto de 3.º (capacidades textuales, recuadros, Access 2016)."""
import re

LOG = []

# ---------------------------------------------------------------- capacidades textuales del programa MEC
# DISEÑO CURRICULAR DE INFORMÁTICA – MAYO 2026, Algorítmica, Segundo curso, págs. 74–76 (letra por letra).
MEC = {
 'A1': 'Identifica estrategias para el planeamiento y solución de problemas con algoritmos.',
 'A2': 'Aplica estructuras selectivas anidadas en la resolución de problemas.',
 'A3': 'Utiliza un lenguaje de programación en la solución de problemas aplicando estructura de control',
 'A4': 'Resuelve problemas utilizando ciclos repetitivos, contadores, acumuladores y banderas.',
 'A5': 'Utiliza estructuras de datos estáticas (vectores y matrices) para el planeamiento y la solución de problemas de la vida diaria (lógico, matemático, comerciales, otros.)',
 'A6': 'Aplica técnicas y procedimientos adecuados de modularización para simplificar problemas complejos.',
 'A7': 'Identifica las funciones utilizadas con datos de tipo cadena.',
 'A8': 'Analiza las utilidades de un sistema de archivos.',
 'A9': 'Aplica técnicas y procedimientos adecuados para el diseño de un sistema de archivos.',
 'A10': 'Identifica los mecanismos de seguridad y protección aplicados a los sistemas de archivos',
 'A11': 'Reconoce la importancia del sistema de archivos dentro de la estructura visible de un sistema operativo.',
 'A12': 'Identifica las características principales de los filtros y consultas.',
 'A13': 'Aplica técnicas y procedimientos en la formulación de filtros y consultas a una base de datos, utilizando el gerenciador.',
 'A14': 'Reconoce la importancia de utilizar correctamente los filtros y consultas a una base de datos.',
}
CAP_CLASE = {1: ['A1'], 2: ['A3'], 3: ['A2'], 4: ['A2'], 5: ['A2'], 6: ['A4'], 7: ['A4'], 8: ['A5'], 9: ['A5'], 10: ['A5'],
             11: ['A5'], 12: ['A5'], 13: ['A6'], 14: ['A6', 'A7'], 15: ['A8'], 16: ['A9'], 17: ['A10'], 18: ['A11'],
             19: ['A12'], 20: ['A13'], 21: ['A14']}
CAP_UNIDAD = {1: ['A1', 'A2', 'A3', 'A4'], 2: ['A5', 'A6', 'A7'], 3: ['A8', 'A9', 'A10', 'A11'], 4: ['A12', 'A13', 'A14']}
CAP_TALLER = ['A1', 'A6', 'A13']
# capacidades que efectivamente evalúan los ítems de cada integradora (E2 abarca las Unidades 1 a 4, como en el paquete vigente)
CAP_EVAL = {'E1': ['A2', 'A3', 'A4', 'A5', 'A6'], 'E2': ['A5', 'A6', 'A9', 'A12', 'A13']}


def caps(cods):
    return [MEC[c] for c in cods]


ACCESS_REF = ('Los procedimientos de este libro toman como referencia Access 2016 en castellano; las versiones posteriores '
              'mantienen en general los mismos conceptos, aunque algún nombre o ubicación de comando puede variar.')

# ---------------------------------------------------------------- política de recuadros «En Paraguay» (v2 de 3.º)
# 'keep' = contenido paraguayo concreto y verificable · ('ret', título, cuerpo|None) · 'del' · ('p', cuerpo|None) = párrafo común
RECUADROS = {
 (1, 0): ('p', 'En el laboratorio vas a usar PSeInt, un programa gratuito que ejecuta pseudocódigo en español y muestra el resultado paso a paso, incluso instrucción por instrucción.'),
 (2, 0): 'del',
 (2, 1): ('ret', 'En Paraguay — guaraníes sin céntimos',
          ['En Paraguay los montos se manejan en guaraníes enteros: en la práctica diaria no circulan céntimos. Por eso los precios y las cantidades de este libro son enteros.',
           'Cuidado al aplicar un porcentaje: el 10 % de 55.555 es 5.555,5. Si la variable se definió Como Entero, PSeInt se detiene con un error de tipos al asignar 49.999,5. La solución es redondear antes de asignar: trunc(monto - monto * 0.10) da 49.999 y redon(...) da 50.000. Los ejemplos de este libro usan montos donde el 10 % es exacto.']),
 (3, 0): ('ret', 'Ejemplo cotidiano — el cajero automático', None),
 (3, 1): 'del',
 (4, 0): 'del',
 (4, 1): ('ret', 'Ejemplo cotidiano — efectivo o QR',
          ['El pago con código QR desde la billetera del celular convive hoy con el efectivo en muchos comercios. Por eso los sistemas de venta modelan el medio de pago como una condición compuesta: la venta se concreta si hay efectivo O QR.']),
 (5, 0): 'del',
 (6, 0): 'del',
 (7, 0): 'del',
 (8, 0): ('ret', 'Ejemplo cotidiano — la planilla de la despensa', None),
 (9, 0): 'del',
 (10, 0): ('ret', 'Ejemplo cotidiano — la planilla de asistencia', None),
 (11, 0): 'del',
 (12, 0): 'del',
 (13, 0): 'del',
 (13, 1): ('ret', 'Aplicación profesional — un módulo por tarea',
           ['Los sistemas de venta se construyen así: un módulo de caja, uno de stock, uno de informes. Cuando el negocio pide un cambio (otra promo, otro medio de pago), el programador toca UN módulo sin desarmar el resto.']),
 (14, 0): ('ret', 'En Paraguay — el RUC',
          ['El RUC se escribe como un número base, un guion y un dígito verificador (por ejemplo, 80012345-6). Separar esas dos partes es un trabajo típico de funciones de cadena: se busca la posición del guion y se extrae lo que está antes y lo que está después.']),
 (15, 0): ('p', 'Un comercio necesita conservar sus comprobantes y registros durante años: por eso se guardan en la memoria secundaria (disco o nube) y no en la RAM, que se borra al apagar.'),
 (15, 1): ('ret', 'Aplicación profesional — el CSV como idioma común',
           ['El intercambio de datos entre sistemas se hace muchísimo con archivos de texto separados por punto y coma o por coma (CSV): una planilla de cálculo los exporta y casi cualquier sistema los importa.']),
 (16, 0): 'del',
 (17, 0): ('ret', 'Aplicación profesional — datos sensibles',
           ['Las oficinas que manejan datos personales respaldan su información con copias periódicas y restringen quién puede abrir cada archivo. Cuando los datos son sensibles, además de los permisos se cifra la copia de respaldo.']),
 (17, 1): ('ret', 'Ejemplo cotidiano — el UPS de la caja',
           ['Los cortes y las bajadas de tensión, sobre todo con las tormentas de verano, son un riesgo para cualquier archivo abierto. Por eso los comercios que dependen de su sistema protegen la computadora de la caja con un UPS: da tiempo a cerrar los archivos y apagar bien.']),
 (18, 0): ('ret', 'Aplicación profesional — el archivo de un estudio contable',
           ['En un estudio contable, los archivos de cada cliente se guardan en carpetas por año y por tipo de trámite. Sin esa organización, encontrar un documento presentado hace tres años llevaría horas.']),
 (18, 1): 'del',
 (19, 0): ('p', 'En el laboratorio vas a trabajar con Microsoft Access, el gestor de bases de datos de escritorio incluido en algunas ediciones de Microsoft Office. ' + ACCESS_REF),
 (20, 0): ('p', None),
 (20, 1): ('p', None),
 (21, 0): ('ret', 'Aplicación profesional — informes de gestión',
           ['Los informes que preparan los comercios para analizar sus ventas por sucursal y por mes son, técnicamente, consultas de referencias cruzadas hechas en el gestor de base de datos.']),
}


def _txt(b):
    if b['t'] in ('p', 'h2', 'h3'):
        return b['text']
    if b['t'] == 'caja':
        return b['title'] + ' ' + ' '.join(b['body'])
    if b['t'] == 'tabla':
        return ' '.join(b['hdr']) + ' ' + ' '.join(' '.join(r) for r in b['rows'])
    if b['t'] == 'img':
        return b['file'] + ' ' + b.get('epigrafe', '')
    if b['t'] == 'code_md':
        return ' '.join(b['lines'])
    return ''


def idx(c, sub_, t=None):
    hits = [i for i, b in enumerate(c['cuerpo']) if sub_ in _txt(b) and (t is None or b['t'] == t)]
    assert len(hits) == 1, ('anclaje ambiguo o ausente', c['n'], sub_, hits)
    return hits[0]


def sub(c, ancla, viejo, nuevo, cod, desc):
    b = c['cuerpo'][idx(c, ancla)]
    hecho = False
    for k in ('text', 'title'):
        if k in b and viejo in b[k]:
            b[k] = b[k].replace(viejo, nuevo); hecho = True
    if 'body' in b and any(viejo in x for x in b['body']):
        b['body'] = [x.replace(viejo, nuevo) for x in b['body']]; hecho = True
    if b['t'] == 'tabla':
        hdr = [x.replace(viejo, nuevo) for x in b['hdr']]; rows = [[x.replace(viejo, nuevo) for x in r] for r in b['rows']]
        hecho = hecho or hdr != b['hdr'] or rows != b['rows']; b['hdr'] = hdr; b['rows'] = rows
    if 'epigrafe' in b and viejo in b['epigrafe']:
        b['epigrafe'] = b['epigrafe'].replace(viejo, nuevo); hecho = True
    assert hecho, ('no se encontró', c['n'], viejo)
    LOG.append((c['n'], cod, desc))


def ins(c, ancla, bloques, cod, desc, antes=False):
    i = idx(c, ancla)
    pos = i if antes else i + 1
    c['cuerpo'][pos:pos] = bloques
    LOG.append((c['n'], cod, desc))


def reemplazar(c, ancla, bloques, cod, desc):
    i = idx(c, ancla)
    c['cuerpo'][i:i + 1] = bloques if isinstance(bloques, list) else [bloques]
    LOG.append((c['n'], cod, desc))


def H2(t): return {'t': 'h2', 'text': t}
def P(t): return {'t': 'p', 'text': t}
def CAJA(tit, *body): return {'t': 'caja', 'title': tit, 'body': list(body)}
def TABLA(hdr, rows): return {'t': 'tabla', 'hdr': hdr, 'rows': rows}
def FIG(file, lead, epi, ancho=15.0): return {'t': 'img', 'file': file, 'ancho_cm': ancho, 'lead': lead, 'epigrafe': epi, 'nueva': True}
def COD(*lines): return ['§' + x for x in lines]


def _recuadros(C):
    for n, c in C.items():
        cajas = [i for i, b in enumerate(c['cuerpo']) if b['t'] == 'caja' and b['title'].startswith('En Paraguay')]
        acciones = []
        for k, i in enumerate(cajas):
            acc = RECUADROS[(n, k)]
            acciones.append((i, acc, c['cuerpo'][i]['body'][:]))
        for i, acc, body in sorted(acciones, key=lambda x: -x[0]):
            b = c['cuerpo'][i]
            if acc == 'keep':
                LOG.append((n, 'R', 'Recuadro «En Paraguay» conservado: contenido paraguayo concreto y verificable.'))
            elif acc == 'del':
                del c['cuerpo'][i]
                LOG.append((n, 'R', 'Recuadro «En Paraguay» eliminado: repetía el desarrollo o no era específico ni verificable («%s…»).' % ' '.join(body)[:70]))
            elif acc[0] == 'p':
                c['cuerpo'][i] = P(acc[1] or ' '.join(body))
                LOG.append((n, 'R', 'Recuadro «En Paraguay» integrado al texto como párrafo común (contenido no específico de Paraguay).'))
            else:
                b['title'] = acc[1]
                if acc[2]:
                    b['body'] = acc[2]
                LOG.append((n, 'R', 'Recuadro «En Paraguay» → «%s».' % acc[1]))
        assert len(cajas) == len([k for k in RECUADROS if k[0] == n]), (n, len(cajas))


def aplicar(C):
    # ------------------------------------------------ capacidades
    for n, cods in CAP_CLASE.items():
        C[n]['ficha']['capacidad'] = caps(cods)
    LOG.append((0, 'CAP', 'Las 21 fichas reproducen textualmente la capacidad del programa MEC (págs. 74–76); la Clase 14 lleva sus dos capacidades (modularización y cadenas).'))

    # ------------------------------------------------ Clase 1
    c = C[1]
    ins(c, 'Ese plan de pasos ordenados y finitos que resuelve un problema es un algoritmo.', [
        P('Dos palabras más completan el vocabulario de partida. Un programa es un algoritmo escrito en un lenguaje que la computadora puede ejecutar: el mismo plan, ahora con reglas estrictas de escritura. Un sistema es un conjunto de programas y datos que trabajan juntos para resolver las necesidades de una organización: el sistema de gestión del copetín tendrá un programa de caja, uno de stock y uno de informes, que comparten los mismos datos.')],
        'C1-1', 'Se definen «programa» y «sistema», que figuran en los conceptos del programa y no se definían.')

    # ------------------------------------------------ Clase 2
    c = C[2]
    sub(c, 'Error Síntoma Corrección', 'Confundir = con <-', 'Usar = para asignar', 'C2-1', 'T4: corrección de la fila «Confundir = con <-».')
    sub(c, 'Error Síntoma Corrección', 'la condición «asigna» en vez de comparar', 'el perfil Flexible lo acepta, pero en otros perfiles y lenguajes es un error', 'C2-1b', 'T4.')
    sub(c, 'Error Síntoma Corrección', '= compara; <- asigna', 'asigná con <- y compará con =', 'C2-1c', 'T4.')
    ins(c, 'La sangría (el bloque corrido hacia adentro) no es decorativa', [
        FIG('fig_n_si_simple.png', 'El flujograma muestra la forma del Si simple: el rombo pregunta, el camino del Sí pasa por el bloque y el camino del No lo saltea; los dos se juntan antes de seguir.',
            'Flujograma del Si simple: el descuento solo se aplica por el camino del Sí.', 13.0)],
        'C2-2', 'Nuevo diagrama del Si simple (la clase no tenía figuras).')
    ins(c, 'Un hábito profesional desde la primera clase con decisiones', [
        H2('Del pseudocódigo al lenguaje de programación'),
        P('PSeInt es un intérprete de pseudocódigo: ideal para aprender, pero no es un lenguaje de programación de los que se usan en la industria. El paso a un lenguaje real es más corto de lo que parece, porque las ideas son las mismas y cambia solo la escritura. PSeInt incluso traduce tu algoritmo: con Archivo → Exportar podés obtenerlo en Python, C, Java u otros lenguajes.'),
        CAJA('Ejemplo — el mismo algoritmo en PSeInt y en Python',
             'En PSeInt (perfil Flexible):',
             *COD('Algoritmo VentaGrande', '    // Calcula el importe de una venta de gaseosas', '    Definir precio, cantidad, importe Como Entero',
                  '    precio <- 8000', '    Escribir "Cantidad de gaseosas:"', '    Leer cantidad', '    importe <- precio * cantidad',
                  '    Si importe >= 50000 Entonces', '        Escribir "Venta grande"', '    FinSi', '    Escribir "Total a pagar: ", importe', 'FinAlgoritmo'),
             'Exportado a Python 3 por PSeInt (con el comentario agregado a mano):',
             *COD('# Calcula el importe de una venta de gaseosas', 'precio = 8000', 'print("Cantidad de gaseosas:")', 'cantidad = int(input())',
                  'importe = precio * cantidad', 'if importe >= 50000:', '    print("Venta grande")', 'print("Total a pagar: ", importe)'),
             'Con 7 gaseosas, los dos programas muestran «Venta grande» y «Total a pagar: 56000».'),
        TABLA(['Elemento del lenguaje', 'En PSeInt', 'En Python', 'Qué tener en cuenta'],
              [['Comentario', '// texto', '# texto', 'el programa lo ignora: es una nota para quien lee'],
               ['Sangría', 'recomendada (legibilidad)', 'obligatoria: define los bloques', 'en Python, un espacio de más cambia el programa'],
               ['Entrada', 'Leer cantidad', 'cantidad = int(input())', 'Python lee texto: hay que convertirlo a número'],
               ['Salida', 'Escribir "Total: ", t', 'print("Total: ", t)', 'misma idea, otra palabra'],
               ['Asignación y comparación', 'x <- 5 · Si x = 5', 'x = 5 · if x == 5', 'Python distingue = (asigna) de == (compara)'],
               ['Fin de bloque', 'FinSi, FinPara…', 'no hay: lo marca la sangría', 'olvidar un FinSi es error en PSeInt']]),
        P('Todo lenguaje impone restricciones. Los nombres de variables empiezan con una letra, no llevan espacios y no pueden ser palabras reservadas (Si, Para, Escribir; en PSeInt también Mostrar, que es sinónimo de Escribir). Cada variable tiene un tipo y no se mezclan sin conversión: «5» entre comillas es un texto, no un número. Algunos lenguajes incluyen además sentencias para la pantalla, como la que cambia el color del texto (COLOR en QBasic, textcolor en Pascal); PSeInt no tiene esa instrucción, porque se concentra en la lógica del algoritmo.'),
        CAJA('Concepto clave — pseudocódigo, programa y lenguaje', 'El pseudocódigo expresa la lógica; el lenguaje de programación la escribe con reglas estrictas para que la computadora la ejecute. Comentarios, sangría, entrada, salida y estructuras de control existen en todos los lenguajes: cambia la sintaxis, no la idea.')],
        'C2-3', 'Cobertura del programa: «Utiliza un lenguaje de programación…» (comentarios, sangría, entrada/salida, restricciones, sentencia de color) con la exportación de PSeInt a Python verificada.')

    # ------------------------------------------------ Clase 4
    c = C[4]
    ins(c, 'Cada operador se resume en una tabla de verdad', [
        FIG('fig_n_condicion.png', 'La figura evalúa la condición del envío gratis como lo hace la computadora: primero cada comparación por separado y después el operador que las une.',
            'Cómo se evalúa una condición compuesta: cada comparación da V o F y el operador Y decide.', 14.5)],
        'C4-1', 'Nuevo diagrama de evaluación de una condición compuesta (la clase no tenía figuras).')

    # ------------------------------------------------ Clase 5
    c = C[5]
    ins(c, 'Cuando la decisión depende del valor exacto de una variable', [
        FIG('fig_n_segun.png', 'Compará en la figura las dos formas de dibujar la misma decisión: a la izquierda, la cadena de Si anidados que pregunta una vez por cada valor; a la derecha, el Segun, que reparte en un solo paso según el valor de la opción.',
            'El menú del mostrador con Si anidados y con Segun: la misma decisión, dos dibujos.', 15.5)],
        'C5-1', 'Nuevo diagrama Si anidado frente a Segun (la clase no tenía figuras).')

    # ------------------------------------------------ Clase 9
    c = C[9]
    ins(c, 'Para el máximo se supone que el primer elemento es el mayor', [
        FIG('fig_n_maximo.png', 'Seguí en la figura cómo cambia la variable mayor a medida que el recorrido avanza: solo se actualiza cuando aparece un valor más grande, y con él se guarda la posición.',
            'El recorrido del máximo sobre la semana del copetín: mayor cambia en los días 2, 4, 5 y 6.', 15.5)],
        'C9-1', 'Nuevo diagrama del recorrido del máximo (la clase no tenía figuras).')
    sub(c, 'Con la semana del copetín, el recorrido termina con mayor = 1.100.000', 'Probalo con la prueba de escritorio y vas a ver el error enseguida.',
        'Probalo con la prueba de escritorio y vas a ver el error enseguida. Un detalle más: segundo arranca en 0 porque las ventas nunca son negativas; si el vector pudiera tener valores negativos, convendría arrancar con el menor de los dos primeros elementos.',
        'C9-2', 'T16: se advierte por qué segundo puede arrancar en 0 en este caso.')

    # ------------------------------------------------ Clase 11
    c = C[11]
    reemplazar(c, 'Ejemplo — intercambio y ranking descendente', [
        CAJA('Ejemplo — la burbuja optimizada, ranking descendente',
             'Unidades vendidas en el mes: unid = [123, 75, 45, 200, 90, 60]. La variable lógica hubo registra si la pasada intercambió algo; si una pasada termina sin intercambios, el vector ya está ordenado y el ciclo corta.',
             *COD('i <- 1', 'Repetir', '    hubo <- Falso', '    Para j <- 1 Hasta 6 - i Con Paso 1 Hacer', '        Si unid[j] < unid[j+1] Entonces   // < para orden descendente',
                  '            aux <- unid[j]', '            unid[j] <- unid[j+1]', '            unid[j+1] <- aux', '            hubo <- Verdadero', '        FinSi',
                  '    FinPara', '    i <- i + 1', 'Hasta Que NO hubo O i > 5'),
             'Resultado: [200, 123, 90, 75, 60, 45]. La cuarta pasada no intercambia nada y el ciclo corta: hizo 4 pasadas en lugar de 5.')],
        'C11-1', 'T1: el código presentado como «burbuja optimizada» no cortaba antes de tiempo; se reemplaza por la versión con la bandera hubo (verificada en PSeInt).')
    ins(c, 'La selección trabaja distinto que la burbuja', [
        CAJA('Ejemplo — el método de selección en pseudocódigo',
             *COD('Para i <- 1 Hasta 5 Con Paso 1 Hacer', '    posMayor <- i', '    Para j <- i + 1 Hasta 6 Con Paso 1 Hacer', '        Si unid[j] > unid[posMayor] Entonces',
                  '            posMayor <- j', '        FinSi', '    FinPara', '    Si posMayor <> i Entonces', '        aux <- unid[i]', '        unid[i] <- unid[posMayor]',
                  '        unid[posMayor] <- aux', '    FinSi', 'FinPara'),
             'En cada vuelta del ciclo exterior, el ciclo interior solo busca la posición del mayor; el intercambio se hace una vez, al final, y solo si hace falta.')],
        'C11-2', 'T2: se agrega el pseudocódigo del método de selección (verificado en PSeInt).')

    # ------------------------------------------------ Clase 12
    c = C[12]
    ins(c, 'En PSeInt, Azar(X) devuelve un entero entre 0 y X−1', [
        FIG('fig_n_azar.png', 'La figura muestra cómo se arma un rango con Azar: primero se generan tantos valores como resultados posibles y después se corre todo el rango sumando el mínimo.',
            'Del Azar(7) a un número entre 1 y 7: la cantidad de valores posibles y el corrimiento del mínimo.', 15.0)],
        'C12-1', 'Nuevo diagrama del rango de Azar (la clase no tenía figuras).')

    # ------------------------------------------------ Clase 13
    c = C[13]
    ins(c, 'Una variable local vive solo dentro del subprograma donde se declara', [
        P('En PSeInt no se pueden declarar variables globales: cada SubProceso y cada Funcion tiene sus propias variables, y el algoritmo principal también. Si un módulo usa una variable con el mismo nombre que una del principal, son dos variables distintas. Por eso, en PSeInt, los datos entran siempre por parámetros y salen por el valor que devuelve una función (o por un parámetro por referencia, que vas a ver en la Clase 14). Lenguajes como Python, C o Pascal sí permiten variables globales, con los riesgos que describe esta clase.'),
        CAJA('Ejemplo — dos variables con el mismo nombre',
             *COD('SubProceso Cambiar', '    total <- 99', '    Escribir "dentro: ", total', 'FinSubProceso', '', 'Algoritmo Principal', '    total <- 5', '    Cambiar', '    Escribir "fuera: ", total', 'FinAlgoritmo'),
             'En PSeInt se ve «dentro: 99» y después «fuera: 5»: el total del módulo es local y no toca el del principal.')],
        'C13-1', 'T12: se aclara que PSeInt no tiene variables globales, con un ejemplo verificado.')

    # ------------------------------------------------ Clase 14
    c = C[14]
    i0 = idx(c, 'Modelo ejecutable — paso por referencia')
    i1 = idx(c, 'Punto de control: al ejecutar, el programa muestra 54000')
    code = c['cuerpo'][i0 + 1]['lines'] + [''] + c['cuerpo'][i0 + 2]['lines']
    code = [re.sub(r'^\s+', lambda m: '    ' * (1 + (len(m.group(0)) > 1)), x) if x.strip() else '' for x in code]
    nuevo = CAJA('Ejemplo — paso por referencia, listo para ejecutar',
                 'En PSeInt, el parámetro que debe modificar la variable original se marca con Por Referencia:',
                 *COD('SubProceso AplicarDescuento(monto Por Referencia)', '    Si monto >= 50000 Entonces', '        monto <- monto - monto * 0.10', '    FinSi', 'FinSubProceso', '',
                      'Algoritmo ProbarReferencia', '    Definir monto Como Real', '    monto <- 60000', '    AplicarDescuento(monto)', '    Escribir monto', 'FinAlgoritmo'),
                 'Al ejecutarlo, el programa muestra 54000. Si se borra «Por Referencia», el parámetro pasa por valor y el programa muestra 60000: el módulo trabajó sobre una copia.')
    c['cuerpo'][i0:i1 + 1] = [nuevo]
    LOG.append((14, 'C14-1', 'El modelo ejecutable de paso por referencia (texto suelto y «punto de control» dentro de la clase) pasa a un recuadro de ejemplo con los dos resultados verificados (54000 / 60000).'))
    ins(c, 'Ejemplo — contar las letras a de un nombre', [
        H2('Comparar cadenas: la relación entre textos'),
        P('Las cadenas también se comparan con los operadores relacionales. El igual y el distinto preguntan si dos textos son idénticos, letra por letra. El menor y el mayor ordenan alfabéticamente, pero según el código de cada carácter: en PSeInt, como en casi todos los lenguajes, las mayúsculas van antes que las minúsculas. Por eso conviene comparar después de pasar los dos textos a mayúsculas.'),
        TABLA(['Comparación', 'Resultado en PSeInt', 'Por qué'],
              [['"chipa" < "empanada"', 'Verdadero', 'c va antes que e en el alfabeto'],
               ['"Chipa" = "chipa"', 'Falso', 'la C mayúscula es otro carácter'],
               ['Mayusculas("Chipa") = Mayusculas("chipa")', 'Verdadero', 'comparadas en mayúsculas, son iguales'],
               ['"Zapallo" < "anana"', 'Verdadero', 'las mayúsculas van antes que todas las minúsculas'],
               ['"10" < "9"', 'Verdadero', 'como texto se compara carácter por carácter: 1 va antes que 9']]),
        CAJA('Errores frecuentes — al comparar cadenas',
             '1. Comparar sin unificar mayúsculas: el cliente escribe «chipa» y el sistema busca «Chipa». La solución es comparar Mayusculas(a) = Mayusculas(b).',
             '2. Guardar números como texto: «10» < «9» da Verdadero. Si con el dato se calcula o se ordena por valor, tiene que ser numérico.',
             '3. Olvidar las comillas: categoria = salado compara con una variable llamada salado, no con el texto «salado».')],
        'C14-2', 'T13: se agrega la relación (comparación) entre cadenas, que figura en el programa, con resultados verificados en PSeInt.')

    # ------------------------------------------------ Clase 16
    c = C[16]
    sub(c, 'Ejemplo — pseudocódigo conceptual: guardar las ventas de la semana en un archivo', '    Escribir En Archivo: dias[i], ";", ventas[i]', '    Escribir Archivo dias[i], ";", ventas[i]',
        'C16-1', 'T11: notación única para el pseudocódigo conceptual de archivos.')
    sub(c, 'Ejemplo — pseudocódigo conceptual: guardar las ventas de la semana en un archivo', 'Cerrar "ventas_semana.txt"', 'Cerrar Archivo', 'C16-1b', 'T11.')
    ins(c, 'Los bloques de esta unidad usan pseudocódigo conceptual para representar esas operaciones', [
        CAJA('Concepto clave — la notación de archivos de este libro',
             'PSeInt no trabaja con archivos, así que esta unidad usa una notación conceptual, siempre la misma:',
             *COD('Abrir "nombre.txt" Para Lectura      // o Para Escritura, o Para Agregar', 'Escribir Archivo dato1, ";", dato2   // graba una línea',
                  'Leer Archivo linea                   // trae la línea siguiente', 'FinDeArchivo                         // Verdadero cuando no quedan líneas', 'Cerrar Archivo'),
             'Es una forma de pensar el procedimiento, no un programa para copiar en PSeInt. Los lenguajes reales tienen instrucciones equivalentes con otros nombres.')],
        'C16-2', 'T11: se documenta la notación conceptual de archivos que usa toda la Unidad 3.')
    ins(c, 'Todo trabajo con archivos respeta el mismo protocolo de tres tiempos', [
        FIG('fig_n_modos.png', 'La figura resume el protocolo y los tres modos de apertura: qué pasa con lo que el archivo ya tenía en cada caso.',
            'Abrir, trabajar y cerrar: los tres modos de apertura y qué pasa con el contenido anterior.', 15.5)],
        'C16-3', 'Nuevo diagrama del ciclo abrir–trabajar–cerrar y los modos (la clase no tenía figuras).')

    # ------------------------------------------------ Clase 17
    c = C[17]
    ins(c, 'Un buffer es una zona de memoria intermedia donde se juntan los datos', [
        FIG('fig_n_buffer.png', 'Seguí en la figura el camino de las siete líneas del archivo: el programa lee de a una desde la RAM, pero el disco solo se toca dos veces.',
            'El buffer en acción: 7 lecturas del programa, 2 accesos al disco.', 15.0)],
        'C17-1', 'Nuevo diagrama del buffer (la clase no tenía figuras).')

    # ------------------------------------------------ Clase 18 (ampliación: estaba por debajo de 750 palabras)
    c = C[18]
    ins(c, 'Una buena organización ahorra tiempo y evita pérdidas.', [
        H2('Lo que el sistema operativo sabe de cada archivo'),
        P('Además del nombre y la ruta, el sistema operativo guarda para cada archivo un conjunto de datos sobre el archivo, que se ven con clic derecho → Propiedades en el Explorador. No forman parte del contenido: son la ficha del archivo, y sirven para buscar, ordenar y proteger.'),
        TABLA(['Propiedad', 'Qué indica', 'Ejemplo con ventas_semana.txt'],
              [['Tipo', 'el formato, deducido de la extensión', 'Documento de texto (.txt)'],
               ['Ubicación', 'la carpeta donde vive', 'C:\\Karumbe\\Ventas\\2026\\julio'],
               ['Tamaño', 'cuántos bytes ocupa el contenido', 'unos 100 bytes: siete líneas cortas'],
               ['Creado / Modificado', 'cuándo nació y cuándo cambió por última vez', 'útil para saber cuál es la versión más nueva'],
               ['Atributos', 'marcas como Solo lectura u Oculto', 'Solo lectura una vez cerrada la semana']]),
        P('La fecha de modificación es una propiedad muy útil en el trabajo diario: ordenar una carpeta por fecha muestra arriba lo último que se tocó, y comparar fechas responde la pregunta de siempre: ¿cuál de estas dos copias es la buena? Por eso un respaldo bien hecho conserva las fechas originales de los archivos.'),
        H2('Buscar en el árbol'),
        P('Cuando la estructura crece, recorrer carpeta por carpeta se vuelve lento. El cuadro de búsqueda del Explorador busca dentro de la carpeta abierta y de todas sus subcarpetas, y admite el comodín asterisco: *.txt encuentra todos los archivos de texto, y ventas_* todos los que empiezan con «ventas_». Es el mismo comodín que vas a usar en los filtros de la Unidad 4.'),
        P('La búsqueda funciona mejor cuanto mejor son los nombres. Un archivo llamado doc1.txt solo se encuentra si alguien recuerda dónde lo dejó; uno llamado cierre_caja_2026-07-13.txt se encuentra escribiendo «cierre» o «2026-07». Organizar bien y nombrar bien son dos caras del mismo trabajo.')],
        'C18-1', 'Ampliación de la clase (701 palabras, por debajo del mínimo): propiedades de un archivo y búsqueda con comodines en el Explorador.')

    # ------------------------------------------------ Clase 20
    c = C[20]
    sub(c, 'La consulta de selección muestra los registros que cumplen un criterio fijo', 'cualquier categoría.Una consulta', 'cualquier categoría. Una consulta',
        'C20-1', 'T14: se repara el párrafo partido por la imagen sin epígrafe (que se retira).')

    # ------------------------------------------------ Clase 21 (ampliación: estaba por debajo de 750 palabras)
    c = C[21]
    ins(c, 'Ningún informe vale por sí mismo: vale por la decisión que habilita.', [
        H2('La referencia cruzada en Access, paso a paso'),
        P('En Access, la consulta de referencias cruzadas se arma de dos maneras: con el asistente (Crear → Asistente para consultas → Asistente para consultas de referencias cruzadas) o desde la vista Diseño de una consulta, cambiando el tipo con Tipo de consulta → Tabla de referencias cruzadas. El asistente es el camino más seguro la primera vez, y tiene una condición: trabaja sobre una sola tabla o consulta de origen.'),
        P('1. Preparar el origen. Si la columna de la grilla no existe en la tabla —como «poco» o «suficiente», que se deduce del stock—, primero se crea una consulta que la calcule con una expresión, por ejemplo Disponibilidad: SiInm([stock]<10;"poco";"suficiente"). En la vista SQL la misma función aparece como IIf.'),
        P('2. Elegir los encabezados de fila: el campo cuyos valores van a ser las filas (categoría).'),
        P('3. Elegir el encabezado de columna: el campo cuyos valores van a ser las columnas (Disponibilidad).'),
        P('4. Elegir el valor del cruce y la función: qué se cuenta o se suma en cada celda (Cuenta de nombre).'),
        P('5. Ejecutar y controlar: la grilla tiene que sumar los registros del origen. Si no cierra, el error está en el origen o en categorías que se solapan.'),
        CAJA('Concepto clave — el origen manda', 'La referencia cruzada solo resume lo que su origen le entrega. Si la disponibilidad se calcula mal en la consulta de origen, la grilla saldrá prolija… y equivocada. Por eso el control se hace en dos lugares: el origen (¿cada registro tiene su valor correcto?) y la grilla (¿cierra en el total?).')],
        'C21-1', 'Ampliación de la clase (722 palabras, por debajo del mínimo): la referencia cruzada en Access paso a paso, con las rutas de Access 2016.')

    # ------------------------------------------------ recuadros «En Paraguay»
    _recuadros(C)

    # ------------------------------------------------ libro único: «tomo»/«cuadernillo» → «libro»
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
    for n, c in C.items():
        for b in c['cuerpo']:
            if b['t'] == 'p':
                nuevo = b['text'].replace('es de los más usados:', 'es muy frecuente:').replace('el informe estrella de la clase siguiente', 'el informe central de la clase siguiente')
                if nuevo != b['text']:
                    LOG.append((n, 'G-3', 'Se reemplaza un superlativo no verificable («de los más usados» / «informe estrella»).'))
                    b['text'] = nuevo
    for n, c in C.items():
        for b in c['cuerpo']:
            if b['t'] == 'tabla':
                b['rows'] = [[x.replace('separadas por ; o ,', 'separadas por punto y coma o por coma') for x in r] for r in b['rows']]
    LOG.append((0, 'G-1', 'Libro único: %d menciones de «tomo» o «cuadernillo» pasan a «libro».' % cambios))
    # una sola carpeta raíz para el copetín en la Unidad 3 (el tomo mezclaba C:\Copetin y C:\Karumbe)
    k = 0
    for n, c in C.items():
        for b in c['cuerpo']:
            if 'text' in b and 'Copetin\\' in b['text']:
                b['text'] = b['text'].replace('Copetin\\', 'Karumbe\\'); k += 1
            if 'body' in b:
                nb = [x.replace('Copetin\\', 'Karumbe\\') for x in b['body']]
                k += nb != b['body']; b['body'] = nb
            if 'rows' in b:
                b['rows'] = [[x.replace('Copetin\\', 'Karumbe\\') for x in r] for r in b['rows']]
    LOG.append((18, 'G-2', 'Coherencia: la carpeta raíz del copetín es siempre C:\\Karumbe (el tomo usaba también C:\\Copetin en el texto y en la tabla de conceptos).'))
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
                ep = re.sub(r'^Figura \d+\.\d+\s*[—-]\s*', '', b.get('epigrafe', ''))
                b['epigrafe'] = num + ' — ' + ep
                b['num'] = num
    # toda figura queda anunciada en el texto (diagnóstico: varias aparecían sin mención)
    for n, c in C.items():
        for i, b in enumerate(c['cuerpo']):
            if b['t'] != 'img' or b.get('lead'):
                continue
            j = i - 1; anunciada = False
            while j >= 0 and c['cuerpo'][j]['t'] != 'h2' and not anunciada:
                q = c['cuerpo'][j]
                anunciada = q['t'] == 'p' and re.search(r'\bfigura', q['text'], re.I) is not None
                j -= 1
            if not anunciada:
                ep = b['epigrafe'].split(' — ', 1)[1].rstrip('.')
                b['lead'] = 'La %s lo muestra en forma gráfica: %s.' % (b['num'], ep[0].lower() + ep[1:])
                if not any(x[1] == 'F-1' and x[0] == n for x in LOG):
                    LOG.append((n, 'F-1', 'Figura sin mención en el texto: se agrega una frase que la anuncia.'))
    # referencias en el texto a la numeración vieja («Figura 3.2», «la figura 1.3»)
    viejo = {}
    for n, c in C.items():
        for b in c['cuerpo']:
            if b['t'] == 'img' and b.get('num_viejo'):
                viejo[b['num_viejo']] = b['num']
    for n, c in C.items():
        for b in c['cuerpo']:
            for k in ('text',):
                if k in b:
                    b[k] = re.sub(r'([Ff]igura) (\d\.\d)\b', lambda m: m.group(1) + ' ' + viejo.get(m.group(2), m.group(2)).replace('Figura ', ''), b[k])
    return mapa

# -*- coding: utf-8 -*-
"""Correcciones y ampliaciones de las 21 clases de Algorítmica 1.º (Edición Esencial Comercial 2026).
Cada cambio queda en LOG con su código para las notas del piloto. Las clases del tomo vigente tenían entre
344 y 549 palabras: se amplían con contenido real (ejemplos resueltos, casos límite, errores frecuentes) y
se agregan figuras donde no había ninguna."""
import re

LOG = []

MEC = {
 'B1': 'Analiza las características principales de la Teoría de Conjuntos',
 'B2': 'Identifica los diferentes Tipos de Subconjuntos.',
 'B3': 'Resuelve problemas sobre operaciones con conjuntos.',
 'B4': 'Reconoce la importancia del trabajo en equipo para la resolución de problemas.',
 'B5': 'Identifica los elementos del pensamiento lógico.',
 'B6': 'Emplea la lógica proposicional en la valoración de las proposiciones.',
 'B7': 'Construye proposiciones que contengan cuantificadores universales y existenciales.',
 'B8': 'Reconoce la importancia de las habilidades para buscar, procesar y analizar información procedente de fuentes diversas.',
 'B9': 'Identifica las diferentes especificaciones de los algoritmos.',
 'B10': 'Analiza las características de los algoritmos cualitativos y cuantitativos.',
 'B11': 'Describe las Expresiones Aritmético-Relacionales utilizadas en los algoritmos.',
 'B12': 'Aplica técnicas adecuadas en la interpretación, resolución y elaboración de enunciados para el desarrollo de algoritmos.',
 'B13': 'Emplea técnicas adecuadas en la Resolución de problemas utilizando el enunciado de decisión, asignación, lectura, escritura.',
 'B14': 'Aplica conocimientos de programación para la resolución de problemas mediante algoritmos utilizando ciclos repetitivos.',
 'B15': 'Manifiesta confianza y flexibilidad mental, en la resolución colectiva de situaciones problemáticas.',
}
ACTITUDINAL = {1: 'B4', 2: 'B8', 3: 'B15'}
CAP_CLASE = {1: ['B1'], 2: ['B1', 'B2'], 3: ['B3'], 4: ['B3'], 5: ['B3'], 6: ['B5'], 7: ['B5'], 8: ['B6'], 9: ['B6'], 10: ['B7'],
             11: ['B7'], 12: ['B7'], 13: ['B9', 'B10'], 14: ['B9'], 15: ['B11'], 16: ['B12'], 17: ['B13'], 18: ['B13'], 19: ['B14'],
             20: ['B14'], 21: ['B14']}
CAP_UNIDAD = {1: ['B1', 'B2', 'B3'], 2: ['B5', 'B6', 'B7'], 3: ['B9', 'B10', 'B11', 'B12', 'B13', 'B14']}
CAP_EVAL = {'E1': ['B1', 'B3', 'B5', 'B6', 'B7'], 'E2': ['B3', 'B6', 'B7', 'B11', 'B13', 'B14']}


def caps(cods):
    return [MEC[c] for c in cods]


# ---------------------------------------------------------------- política de recuadros «En Paraguay» (v2)
RECUADROS = {
 1: ('ret', 'En Paraguay — conjuntos del país', ['El Paraguay se divide en 17 departamentos, y Asunción es la capital: el conjunto de los departamentos es finito y tiene cardinal 17. El achegety, el alfabeto guaraní, es otro conjunto finito: tiene 33 letras.']),
 2: 'del', 3: ('p', 'Las tablas estadísticas que cruzan dos categorías —por ejemplo, hogares con acceso a internet y hogares con computadora— son, en el fondo, diagramas de Venn de cuatro regiones.'),
 4: ('ret', 'Aplicación profesional — filtros de una tienda en línea', ['Cuando en una tienda en línea marcás «envío a mi ciudad» y «pago con QR», el sitio calcula la intersección de dos conjuntos de productos; si marcás «uno u otro», calcula la unión.']),
 5: 'del', 6: 'del', 7: 'del', 8: ('ret', 'Aplicación profesional — 2ⁿ crece rápido', None), 9: 'del', 10: 'del', 11: 'del', 12: 'del',
 13: ('ret', 'Ejemplo cotidiano — de dónde viene la palabra', ['La palabra «algoritmo» viene del nombre del matemático persa Al-Juarismi (siglo IX), cuyos libros enseñaban procedimientos de cálculo paso a paso. Una caja registradora que calcula el total de un ticket ejecuta un algoritmo cuantitativo como los que vas a diseñar en papel.']),
 14: 'del', 15: 'del', 16: 'del', 17: 'del', 18: 'del', 19: 'del', 20: 'del', 21: 'del',
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
    return ''


def idx(c, sub_, t=None):
    hits = [i for i, b in enumerate(c['cuerpo']) if sub_ in _txt(b) and (t is None or b['t'] == t)]
    assert len(hits) == 1, ('anclaje ambiguo o ausente', c['n'], sub_, hits)
    return hits[0]


def sub(c, ancla, viejo, nuevo, cod, desc):
    b = c['cuerpo'][idx(c, ancla)]
    hecho = False
    for k in ('text', 'title', 'epigrafe'):
        if k in b and viejo in b[k]:
            b[k] = b[k].replace(viejo, nuevo); hecho = True
    if 'body' in b and any(viejo in x for x in b['body']):
        b['body'] = [x.replace(viejo, nuevo) for x in b['body']]; hecho = True
    if b['t'] == 'tabla':
        hdr = [x.replace(viejo, nuevo) for x in b['hdr']]; rows = [[x.replace(viejo, nuevo) for x in r] for r in b['rows']]
        hecho = hecho or hdr != b['hdr'] or rows != b['rows']; b['hdr'] = hdr; b['rows'] = rows
    assert hecho, ('no se encontró', c['n'], viejo)
    LOG.append((c['n'], cod, desc))


def ins(c, ancla, bloques, cod, desc, antes=False):
    i = idx(c, ancla)
    c['cuerpo'][i if antes else i + 1:i if antes else i + 1] = bloques
    LOG.append((c['n'], cod, desc))


def antes_del_final(c, bloques, cod, desc):
    """Inserta antes del recuadro «En Paraguay» de la clase (que la política v2 retira o reconvierte)."""
    ins(c, 'En Paraguay', bloques, cod, desc, antes=True)


def H2(t): return {'t': 'h2', 'text': t}
def P(t): return {'t': 'p', 'text': t}
def CAJA(tit, *body): return {'t': 'caja', 'title': tit, 'body': list(body)}
def TABLA(hdr, rows): return {'t': 'tabla', 'hdr': hdr, 'rows': rows}
def FIG(file, lead, epi, ancho=14.5): return {'t': 'img', 'file': file, 'ancho_cm': ancho, 'lead': lead, 'epigrafe': epi, 'nueva': True}
def COD(*lines): return ['§' + x for x in lines]


def aplicar(C):
    for n, cods in CAP_CLASE.items():
        C[n]['ficha']['capacidad'] = caps(cods)
    LOG.append((0, 'CAP', 'Las 21 fichas reproducen textualmente la capacidad del programa MEC (págs. 70–73). Clase 2 suma la primera capacidad (clasificación de conjuntos); Clase 13 suma «Analiza las características de los algoritmos cualitativos y cuantitativos», que no figuraba en ninguna ficha; Clase 10 pasa a la capacidad bajo la cual el programa ubica las leyes (De Morgan, adjunción, simplificación).'))

    # ================================================================ UNIDAD 1
    c = C[1]
    antes_del_final(c, [
        H2('La prueba del juez: ¿está bien definido?'),
        P('Para saber si una colección es un conjunto, imaginá a un juez que no te conoce y que tiene que decidir, objeto por objeto, si entra o no. Si el juez puede decidir siempre sin pedirte opinión, la colección está bien definida. Si para algunos objetos tendría que adivinar lo que vos pensás, no lo está.'),
        TABLA(['Colección', '¿Bien definida?', 'Por qué'], [
            ['Los días de la semana', 'Sí', 'Cualquiera decide si un día es o no uno de los siete.'],
            ['Los números pares menores que 20', 'Sí', 'La propiedad se comprueba con una cuenta.'],
            ['Los clientes simpáticos del copetín', 'No', '«Simpático» depende de quién opina.'],
            ['Los productos que cuestan menos de G. 5.000 hoy', 'Sí', 'Se decide mirando la lista de precios del día.'],
            ['Los números grandes', 'No', '¿Desde cuánto un número es «grande»? No hay criterio.']]),
        H2('Orden, repetición e igualdad'),
        P('En un conjunto no importa el orden ni la repetición: {chipa, coquito} y {coquito, chipa} son el mismo conjunto, y escribir {chipa, chipa, coquito} no agrega nada, porque la chipa ya estaba. Dos conjuntos son iguales cuando tienen exactamente los mismos elementos, aunque estén escritos de forma distinta: {x / x es vocal de «ala»} = {a}.'),
        P('Esta regla tiene consecuencias al contar. Las letras de la palabra «Paraguay» son ocho, pero el conjunto de sus letras distintas es L = {p, a, r, g, u, y}, y su cardinal es n(L) = 6: la a aparece tres veces en la palabra y una sola vez en el conjunto.'),
        CAJA('Errores frecuentes — al escribir conjuntos',
             'Repetir elementos: {o, u, a, o} se escribe {o, u, a}.',
             'Usar paréntesis o corchetes: los conjuntos se encierran entre llaves { }.',
             'Confundir el conjunto con su cardinal: M es la lista de productos; n(M) es el número 5.',
             'Describir por comprensión con una propiedad vaga: «x es un producto rico» no determina ningún conjunto.'),
        FIG('fig_n_pertenencia.png', 'La figura muestra el menú del copetín como un recinto: lo que está adentro pertenece (∈) y lo que está afuera, como la pizza, no pertenece (∉).',
            'El conjunto M del menú: cinco elementos adentro, la pizza afuera. El recinto vuelve visible la pertenencia.', 13.0)],
        'C1-1', 'Ampliación (462 palabras): conjunto bien definido con tabla de casos, orden y repetición, igualdad de conjuntos, errores frecuentes y figura de pertenencia.')

    c = C[2]
    antes_del_final(c, [
        H2('Comparar dos conjuntos: igualdad, inclusión y disjunción'),
        P('Con dos conjuntos a la vista hay pocas relaciones posibles, y conviene nombrarlas con precisión antes de calcular nada. La tabla las resume con los productos del copetín.'),
        TABLA(['Relación', 'Símbolo', 'Se cumple cuando…', 'Ejemplo'], [
            ['Igualdad', 'A = B', 'tienen exactamente los mismos elementos', '{chipa, mixta} = {mixta, chipa}'],
            ['Inclusión', 'A ⊆ B', 'todo elemento de A está en B', '{chipa} ⊆ {chipa, mixta}'],
            ['Inclusión propia', 'A ⊂ B', 'A ⊆ B y B tiene algo más', '{chipa} ⊂ {chipa, mixta}'],
            ['Disjuntos', 'A ∩ B = ∅', 'no comparten ningún elemento', '{chipa} y {gaseosa}']]),
        H2('Contar subconjuntos sin perder ninguno'),
        P('¿Por qué un conjunto de n elementos tiene 2ⁿ subconjuntos? Porque armar un subconjunto es tomar una decisión por cada elemento: entra o no entra. Con {chipa, mixta, coquito} hay dos opciones para la chipa, dos para la mixta y dos para el coquito: 2 × 2 × 2 = 8 maneras de decidir, y cada manera da un subconjunto distinto. Si decidís «no» a todo, obtenés ∅; si decidís «sí» a todo, el conjunto completo.'),
        P('Para escribirlos sin olvidos, ordenalos por tamaño: 1 subconjunto de 0 elementos (∅), 3 de un elemento ({chipa}, {mixta}, {coquito}), 3 de dos ({chipa, mixta}, {chipa, coquito}, {mixta, coquito}) y 1 de tres. La suma 1 + 3 + 3 + 1 = 8 es el control.'),
        FIG('fig_n_inclusion.png', 'La figura pone lado a lado las dos relaciones que más se confunden: un elemento pertenece a un conjunto (∈), mientras que un conjunto está incluido en otro (⊆).',
            'Pertenencia e inclusión: la empanada pertenece a M; el conjunto F de los fritos está incluido en M.', 14.5),
        CAJA('Errores frecuentes — inclusión y pertenencia',
             'Escribir empanada ⊆ M: la empanada es un elemento; lo correcto es empanada ∈ M o {empanada} ⊆ M.',
             'Olvidar ∅ y el propio conjunto al listar subconjuntos: son dos de los 2ⁿ.',
             'Confundir ∅ con {∅}: el primero no tiene elementos; el segundo tiene uno.')],
        'C2-1', 'Ampliación (510 palabras): relaciones entre conjuntos, justificación de 2ⁿ, método de conteo por tamaño, errores frecuentes y figura de pertenencia frente a inclusión.')

    c = C[3]
    antes_del_final(c, [
        H2('Tres conjuntos: ocho regiones'),
        P('Con tres óvalos que se cruzan, el rectángulo queda dividido en 8 regiones: 2³, la misma potencia de 2 de los subconjuntos. Cada región responde a tres preguntas de sí o no: ¿está en A?, ¿está en B?, ¿está en C? La región central es la de los elementos que están en los tres; la de afuera, la de los que no están en ninguno.'),
        H2('Juegos lógicos con diagramas'),
        P('Muchos acertijos se resuelven dibujando antes de calcular. Ña Rosa tiene 7 clientes habituales. Cuatro toman cocido, tres toman jugo y dos no toman ninguna de las dos bebidas. ¿Cuántos toman las dos?'),
        P('Se dibujan dos óvalos dentro de un rectángulo de 7. Afuera de los óvalos van los 2 que no toman nada, así que dentro de los óvalos quedan 7 − 2 = 5 personas. Pero si sumamos 4 + 3 = 7, contamos 7 «presencias» para solo 5 personas: las 2 de diferencia son las que están en los dos óvalos a la vez. Respuesta: 2 toman ambas; 2 solo cocido y 1 solo jugo. Control: 2 + 2 + 1 + 2 = 7.'),
        CAJA('Concepto clave — dibujar primero',
             'El diagrama ordena la información antes de hacer cuentas. En un juego lógico, cada dato del enunciado ocupa un lugar en el dibujo; si un dato no tiene dónde ir, todavía no entendiste el problema.'),
        CAJA('Errores frecuentes — al dibujar diagramas',
             'Olvidar el rectángulo del universo: sin él, no hay dónde ubicar los elementos que no están en ningún conjunto.',
             'Dibujar óvalos cruzados cuando un conjunto está incluido en otro: si A ⊆ B, el óvalo de A va adentro.',
             'Poner un elemento en dos regiones a la vez: cada elemento ocupa exactamente una.')],
        'C3-1', 'Ampliación (431 palabras): tres conjuntos y ocho regiones, juegos lógicos resueltos con diagramas (contenido del programa) y errores frecuentes.')

    c = C[4]
    antes_del_final(c, [
        H2('Tres conjuntos en una misma cuenta'),
        P('Agreguemos un tercer turno: C = {coquito, gaseosa, jugo}, los productos del turno noche. Con A = {chipa, mixta, coquito} y B = {mixta, empanada, gaseosa}, la expresión (A ∪ B) ∩ C pregunta qué productos del día también se vendieron a la noche. Primero el paréntesis: A ∪ B = {chipa, mixta, coquito, empanada, gaseosa}. Después la intersección con C: {coquito, gaseosa}.'),
        P('Calculemos por otro camino: A ∩ C = {coquito} y B ∩ C = {gaseosa}, y su unión es {coquito, gaseosa}. Llegamos al mismo resultado, y no es casualidad: es la propiedad distributiva, (A ∪ B) ∩ C = (A ∩ C) ∪ (B ∩ C). La asociativa también se puede comprobar: (A ∩ B) ∩ C = {mixta} ∩ C = ∅, y A ∩ (B ∩ C) = A ∩ {gaseosa} = ∅.'),
        TABLA(['Expresión', 'Paso 1', 'Resultado'], [
            ['(A ∪ B) ∩ C', 'A ∪ B = {chipa, mixta, coquito, empanada, gaseosa}', '{coquito, gaseosa}'],
            ['(A ∩ C) ∪ (B ∩ C)', 'A ∩ C = {coquito} ; B ∩ C = {gaseosa}', '{coquito, gaseosa}'],
            ['(A ∩ B) ∩ C', 'A ∩ B = {mixta}', '∅'],
            ['A ∩ (B ∩ C)', 'B ∩ C = {gaseosa}', '∅']]),
        FIG('fig_n_union_inter.png', 'Compará en la figura las dos operaciones sobre el mismo par de conjuntos: la unión pinta toda la superficie de los dos óvalos; la intersección, solo la zona que comparten.',
            'La unión A ∪ B (toda la superficie coloreada) y la intersección A ∩ B (solo la zona común) con los turnos mañana y siesta.', 15.0),
        CAJA('Errores frecuentes — unión e intersección',
             'Repetir en la unión los elementos comunes: la mixta se escribe una sola vez.',
             'Responder «no hay» cuando la intersección es vacía: la respuesta correcta es el conjunto ∅.',
             'Calcular fuera de orden en expresiones con paréntesis: primero lo de adentro.')],
        'C4-1', 'Ampliación (440 palabras): operaciones con tres conjuntos, propiedad distributiva y asociativa verificadas con elementos, figura de unión e intersección y errores frecuentes.')

    c = C[5]
    sub(c, 'Ña Rosa encuestó a 30 clientes', '15 compran gaseosa', '15 compran cocido', 'C5-1', 'Coherencia: el ejemplo decía «gaseosa» y la Figura 1.2 y el texto, «cocido».')
    sub(c, 'Ña Rosa encuestó a 30 clientes', 'Solo gaseosa', 'Solo cocido', 'C5-1b', 'Coherencia con la Figura 1.2.')
    sub(c, 'Ña Rosa encuestó a 30 clientes', '30 = n(U). ✓', '30 = n(U).', 'C5-1c', 'Se retira el símbolo ✓.')
    antes_del_final(c, [
        H2('Las leyes de De Morgan, comprobadas con elementos'),
        P('Con el menú U = {chipa, mixta, empanada, coquito, gaseosa}, A = {chipa, mixta, coquito} y B = {mixta, empanada, gaseosa}, verifiquemos las dos leyes. Como A ∪ B = U, su complemento es (A ∪ B)′ = ∅; y por el otro lado, A′ = {empanada, gaseosa} y B′ = {chipa, coquito} no tienen nada en común: A′ ∩ B′ = ∅. Coinciden.'),
        P('Para la segunda ley: A ∩ B = {mixta}, así que (A ∩ B)′ = {chipa, empanada, coquito, gaseosa}. Y A′ ∪ B′ = {empanada, gaseosa, chipa, coquito}: el mismo conjunto. Estas leyes vuelven en la Unidad 2 con proposiciones, y en la Unidad 3 dentro de las condiciones de los algoritmos.'),
        H2('Problemas «al revés»'),
        P('A veces el dato que falta es la intersección. En un curso de 32 estudiantes, 18 usan mensajería para estudiar, 12 usan el correo electrónico y 7 no usan ninguno de los dos. ¿Cuántos usan ambos? Los que usan al menos uno son 32 − 7 = 25. Por la fórmula, 25 = 18 + 12 − n(ambos), así que n(ambos) = 5. Entonces, solo mensajería: 18 − 5 = 13; solo correo: 12 − 5 = 7. Control del universo: 13 + 5 + 7 + 7 = 32.'),
        CAJA('Errores frecuentes — problemas de conteo',
             'Restar la intersección dos veces: «solo A» es n(A) − n(A ∩ B), una sola resta.',
             'Olvidar la región «ninguno»: sin ella, las regiones no suman el universo.',
             'Escribir en el diagrama los totales de cada conjunto en lugar de los de cada región.')],
        'C5-2', 'Ampliación (475 palabras): leyes de De Morgan verificadas con elementos, problema de conteo con la intersección desconocida y errores frecuentes.')

    # ================================================================ UNIDAD 2
    c = C[6]
    antes_del_final(c, [
        H2('Casos que exigen pensar dos veces'),
        P('Algunas oraciones parecen proposiciones y no lo son. «Esta oración es falsa» no puede ser verdadera ni falsa sin contradecirse: es una paradoja y queda fuera de la lógica proposicional. Otras dependen del contexto: «hoy llueve» o «yo tengo 15 años» no tienen un valor fijo escritas en un papel, pero dichas por una persona concreta, en un día concreto, sí lo tienen. En los ejercicios, una oración así se considera proposición cuando el contexto está fijado.'),
        H2('Del lenguaje cotidiano a las proposiciones'),
        P('Para clasificar una oración, primero se buscan sus proposiciones atómicas y después los conectivos que las unen. La tabla muestra el procedimiento.'),
        TABLA(['Oración', 'Atómicas', 'Conectivo', 'Clase'], [
            ['Hay cocido.', 'hay cocido', '—', 'atómica'],
            ['No hay coquitos.', 'hay coquitos', 'negación', 'molecular'],
            ['Hay chipa o hay mbeju.', 'hay chipa ; hay mbeju', 'disyunción', 'molecular'],
            ['Si llueve, se suspende el delivery.', 'llueve ; se suspende el delivery', 'condicional', 'molecular'],
            ['x es un producto dulce.', '—', '—', 'abierta (falta x)']]),
        FIG('fig_n_clasif_prop.png', 'El diagrama de la figura ordena las preguntas que hay que hacerse ante una oración, en el orden en que conviene hacerlas.',
            'Cómo clasificar una expresión: ¿es declarativa?, ¿tiene un único valor de verdad?, ¿contiene variables?, ¿contiene conectivos?', 15.0),
        CAJA('Errores frecuentes — al reconocer proposiciones',
             'Tomar una opinión por proposición: «el cocido es la mejor bebida» no tiene un criterio objetivo.',
             'Clasificar como atómica una oración con «no»: la negación es un conectivo.',
             'Asignarle V o F a una proposición abierta antes de darle valor a la variable.')],
        'C6-1', 'Ampliación (410 palabras): paradojas y oraciones dependientes del contexto, procedimiento de clasificación con tabla, figura nueva y errores frecuentes.')

    c = C[7]
    antes_del_final(c, [
        H2('Palabras que esconden conectivos'),
        P('En el idioma, los conectivos no siempre aparecen como «y», «o», «si… entonces». Para simbolizar bien hay que reconocerlos aunque vengan disfrazados.'),
        TABLA(['Expresión', 'Ejemplo', 'Simbolización'], [
            ['pero, aunque, sin embargo', 'Hay chipa, pero no hay cocido.', 'p ∧ ¬q'],
            ['ni… ni…', 'Ni hay chipa ni hay cocido.', '¬p ∧ ¬q'],
            ['p solo si q', 'Hay descuento solo si pagás con QR.', 'p → q'],
            ['p si q', 'Hay descuento si pagás con QR.', 'q → p'],
            ['p si y solo si q', 'Hay delivery si y solo si hay moto.', 'p ↔ q']]),
        H2('El conectivo principal'),
        P('Toda fórmula molecular tiene un conectivo principal: el que se evalúa último y que da nombre a la fórmula entera. En (p ∧ q) → r es el condicional, así que la fórmula es un condicional; en ¬(p ∨ q) es la negación. Identificarlo es el primer paso para evaluar, y también para negar correctamente en la Clase 10.'),
        FIG('fig_n_condicional.png', 'La figura recorre los cuatro escenarios de la promesa de Ña Rosa y marca el único en el que la promesa queda rota.',
            'El condicional como promesa: de los cuatro escenarios posibles, solo «compró y no recibió el regalo» hace falso a p → q.', 15.0),
        CAJA('Errores frecuentes — al simbolizar',
             'Traducir «p solo si q» como q → p: la flecha va de p hacia q.',
             'Olvidar los paréntesis: p ∧ q → r es ambiguo; se escribe (p ∧ q) → r.',
             'Usar la disyunción inclusiva cuando el enunciado excluye una opción («elegí uno»).')],
        'C7-1', 'Ampliación (464 palabras): conectivos disfrazados en el idioma, conectivo principal, figura del condicional como promesa y errores frecuentes.')

    c = C[8]
    # orden: la tabla de ¬(p ∧ q) va justo después de anunciarla; la figura, después
    cu = c['cuerpo']
    it = idx(c, '¬(p ∧ q)', 'tabla'); tb = cu.pop(it)
    ia = idx(c, 'Construyamos la tabla de ¬(p ∧ q):'); cu.insert(ia + 1, tb)
    LOG.append((8, 'C8-1', 'La tabla de ¬(p ∧ q) se ubica inmediatamente después de anunciarla (la figura de otra fórmula la separaba).'))
    antes_del_final(c, [
        H2('Una tabla completa paso a paso'),
        P('Construyamos la tabla de (p ∨ q) ∧ ¬(p ∧ q). Necesitamos tres columnas auxiliares: p ∨ q, p ∧ q y su negación. Recién al final se aplica el conectivo principal, que es la conjunción.'),
        TABLA(['p', 'q', 'p ∨ q', 'p ∧ q', '¬(p ∧ q)', '(p ∨ q) ∧ ¬(p ∧ q)'], [
            ['V', 'V', 'V', 'V', 'F', 'F'], ['V', 'F', 'V', 'F', 'V', 'V'], ['F', 'V', 'V', 'F', 'V', 'V'], ['F', 'F', 'F', 'F', 'V', 'F']]),
        P('La columna final, F V V F, es idéntica a la de la disyunción exclusiva p ⊻ q que viste en la Clase 7. La fórmula dice «al menos una, pero no las dos»: es exactamente lo que significa el «o» exclusivo, escrito con los conectivos básicos.'),
        H2('Qué columnas auxiliares conviene agregar'),
        P('Una columna por cada subfórmula, empezando por las más internas. Si una subfórmula aparece dos veces, se calcula una sola vez y se reutiliza. Con práctica se pueden saltear columnas, pero en la evaluación conviene mostrarlas: son la evidencia de tu razonamiento y permiten encontrar un error en segundos.'),
        CAJA('Errores frecuentes — al construir tablas',
             'Cambiar el orden de las filas entre una tabla y otra: siempre V V, V F, F V, F F.',
             'Aplicar el conectivo principal antes de terminar las columnas auxiliares.',
             'Negar una columna equivocada: ¬(p ∧ q) niega la columna de p ∧ q, no la de p.')],
        'C8-2', 'Ampliación (428 palabras): tabla completa paso a paso que reconstruye la disyunción exclusiva, criterio para las columnas auxiliares y errores frecuentes.')

    c = C[9]
    antes_del_final(c, [
        H2('Una tabla de ocho filas completa'),
        P('Clasifiquemos (p ∧ q) → r: «si hay harina y hay queso, entonces hay chipa». La tabla tiene 2³ = 8 filas en el orden estándar.'),
        TABLA(['p', 'q', 'r', 'p ∧ q', '(p ∧ q) → r'], [
            ['V', 'V', 'V', 'V', 'V'], ['V', 'V', 'F', 'V', 'F'], ['V', 'F', 'V', 'F', 'V'], ['V', 'F', 'F', 'F', 'V'],
            ['F', 'V', 'V', 'F', 'V'], ['F', 'V', 'F', 'F', 'V'], ['F', 'F', 'V', 'F', 'V'], ['F', 'F', 'F', 'F', 'V']]),
        P('Hay siete V y una sola F, en la fila p = V, q = V, r = F: hay harina y queso, pero no hay chipa. La fórmula es una indeterminación. Para clasificar no hace falta más: basta una V y una F para descartar tautología y contradicción.'),
        H2('Encontrar rápido la fila decisiva'),
        P('Si la fórmula es un condicional, la única forma de que sea F es antecedente V y consecuente F: se buscan primero esas filas. Si es una conjunción, alcanza con encontrar una parte F; si es una disyunción, una parte V. Este atajo no reemplaza la tabla, pero dice por dónde empezar y sirve para controlar el resultado.'),
        FIG('fig_n_arbol8.png', 'El árbol de la figura muestra de dónde salen las 8 filas: cada variable duplica los caminos, y cada camino completo es una fila de la tabla.',
            'Árbol de combinaciones de p, q y r: 2 × 2 × 2 = 8 caminos, uno por fila, en el orden estándar de la tabla.', 15.0),
        CAJA('Errores frecuentes — tres variables',
             'Escribir 6 filas en lugar de 8: con tres variables son 2³.',
             'Clasificar como tautología después de revisar solo algunas filas.',
             'Confundir indeterminación con «error»: es una clase legítima de fórmula.')],
        'C9-1', 'Ampliación (388 palabras): tabla de ocho filas resuelta, atajo para la fila decisiva, figura del árbol de combinaciones y errores frecuentes.')

    c = C[10]
    reemplazar_img(c, 'src_04', FIG('fig_n_demorgan.png', None,
        'Figura — Tabla de verdad de la ley de De Morgan: ¬(p ∧ q) ≡ ¬p ∨ ¬q. Las columnas resaltadas coinciden en las cuatro filas: F, V, V, V.', 15.0))
    LOG.append((10, 'C10-1', 'Figura de De Morgan redibujada: en la original el rótulo «columnas idénticas fila por fila» tapaba los encabezados de la tabla.'))
    antes_del_final(c, [
        H2('Más equivalencias que conviene conocer'),
        TABLA(['Equivalencia', 'Nombre', 'En palabras'], [
            ['p → q ≡ ¬p ∨ q', 'definición del condicional', 'o no se cumple la condición, o se cumple lo prometido'],
            ['p → q ≡ ¬q → ¬p', 'contrarrecíproco', 'si falta lo prometido, no se cumplió la condición'],
            ['¬(p → q) ≡ p ∧ ¬q', 'negación del condicional', 'se cumplió la condición y no lo prometido'],
            ['p ↔ q ≡ (p → q) ∧ (q → p)', 'bicondicional', 'un condicional en cada sentido']]),
        H2('Demostrar una equivalencia sin tabla'),
        P('Las leyes permiten transformar una fórmula paso a paso, como en álgebra. Partamos de ¬(p → q). Por la definición del condicional, es ¬(¬p ∨ q). Por De Morgan, ¬(¬p) ∧ ¬q. Por doble negación, p ∧ ¬q. Cada paso cita la ley que lo justifica, y el resultado coincide con la tercera fila de la tabla anterior. Si dudás, la tabla de verdad siempre confirma.'),
        P('Esta transformación tiene una aplicación directa: para mostrar que una promesa «si p entonces q» se rompió, no alcanza con mostrar que q no ocurrió; hay que mostrar que p ocurrió y q no.'),
        CAJA('Errores frecuentes — al negar',
             'Negar «p y q» como «no p y no q»: la negación correcta es «no p o no q».',
             'Negar un condicional con otro condicional: ¬(p → q) no es p → ¬q.',
             'Olvidar que la doble negación se cancela: ¬(¬p) es p.')],
        'C10-2', 'Ampliación (449 palabras): tabla de equivalencias útiles, demostración de una equivalencia por transformación y errores frecuentes al negar.')

    c = C[11]
    antes_del_final(c, [
        H2('El conjunto de referencia decide'),
        P('El valor de verdad de una proposición cuantificada depende del conjunto sobre el que se habla. ∀x: x > 0 es verdadera si x recorre los números naturales y falsa si recorre los enteros, porque −3 es un contraejemplo. Por eso siempre hay que declarar el conjunto de referencia, igual que el universo U de la Unidad 1.'),
        P('Usemos los precios del día de Ña Rosa: chipa 4.000, mixta 10.000, empanada 6.000, coquito 500 y gaseosa 8.000. Sobre el menú M, ∀x: «x cuesta menos de 12.000» es V; ∀x: «x cuesta menos de 8.000» es F (contraejemplos: mixta y gaseosa); ∃x: «x cuesta más de 9.000» es V (la mixta).'),
        H2('Cuantificadores con dos propiedades'),
        P('«Todos los productos fritos cuestan menos de 7.000» no dice que todos los productos sean fritos: dice que, si un producto es frito, entonces cuesta menos de 7.000. Se simboliza ∀x: (f(x) → c(x)). En cambio, «algún producto frito es dulce» pide un elemento que cumpla las dos cosas a la vez: ∃x: (f(x) ∧ d(x)). Con el universal va el condicional; con el existencial, la conjunción.'),
        FIG('fig_n_cuantif.png', 'La figura ubica los cinco productos del menú con sus precios y muestra cómo un solo contraejemplo alcanza para derribar un «para todo».',
            'Cuantificadores sobre el menú: ∃x: «x cuesta más de 9.000» se demuestra con un ejemplo; ∀x: «x cuesta menos de 8.000» cae con un contraejemplo.', 15.0),
        CAJA('Errores frecuentes — cuantificadores',
             'Negar «todos cumplen» con «ninguno cumple»: la negación es «alguno no cumple».',
             'Demostrar un «para todo» con un solo ejemplo: hace falta revisar todos los elementos.',
             'Simbolizar «todos los fritos son baratos» con ∧: diría que todos los productos son fritos.')],
        'C11-1', 'Ampliación (344 palabras, la más breve del tomo): conjunto de referencia, ejemplo con precios del menú, cuantificadores con dos propiedades, figura nueva y errores frecuentes.')

    c = C[12]
    antes_del_final(c, [
        H2('Una demostración de varios pasos'),
        P('Premisas: «si es feriado, abre el copetín al mediodía» (p → q); «si abre al mediodía, hornea chipa» (q → r); «hoy es feriado» (p). Queremos concluir r: «hoy hornea chipa». Se numeran las líneas y se cita la regla en cada paso.'),
        TABLA(['Línea', 'Proposición', 'Justificación'], [
            ['1', 'p → q', 'premisa'], ['2', 'q → r', 'premisa'], ['3', 'p', 'premisa'],
            ['4', 'p → r', 'silogismo hipotético (1, 2)'], ['5', 'r', 'MPP (4, 3)']]),
        P('También se podía llegar por otro camino: de 1 y 3, q por MPP; de 2 y q, r por MPP. Una demostración no es única; lo que importa es que cada paso esté justificado.'),
        H2('Dos falacias que parecen razonamientos'),
        P('La afirmación del consecuente concluye p a partir de p → q y q: «si es viernes hay chipa; hay chipa; entonces es viernes». Es inválida, porque la chipa puede haberse horneado otro día. La negación del antecedente concluye ¬q a partir de p → q y ¬p: «si es viernes hay chipa; no es viernes; entonces no hay chipa». También es inválida. Las dos se parecen a MPP y MTT, pero usan la premisa equivocada.'),
        P('Sobre los nombres: en este libro, siguiendo la convención del programa, «silogismo disyuntivo» es la regla de la tabla (p ∨ q; p → r; q → s ⊢ r ∨ s), y la regla «p ∨ q; ¬p ⊢ q» se llama Modus Tollendo Ponens. Algunos textos llaman «silogismo disyuntivo» a esta segunda: si los consultás, fijate en las premisas, no solo en el nombre.'),
        FIG('fig_n_reglas.png', 'La figura reúne las reglas de inferencia como piezas: las premisas entran por arriba y la conclusión sale por abajo.',
            'Las reglas de inferencia del programa: MPP, MTT, MTP, silogismo hipotético y silogismo disyuntivo, con sus premisas y su conclusión.', 15.5)],
        'C12-1', 'Ampliación (435 palabras): demostración numerada con justificación, falacias de afirmación del consecuente y negación del antecedente, aclaración sobre el nombre «silogismo disyuntivo» y figura de las reglas.')

    # ================================================================ UNIDAD 3
    c = C[13]
    antes_del_final(c, [
        H2('Las estructuras básicas, en los dos tipos'),
        P('Cualitativos o cuantitativos, todos los algoritmos se arman con las mismas tres estructuras: la secuencia (un paso detrás de otro), la decisión (elegir un camino según una condición) y la repetición (volver a hacer algo mientras haga falta). La diferencia está en lo que procesan, no en cómo se organizan.'),
        TABLA(['Estructura', 'En un algoritmo cualitativo', 'En un algoritmo cuantitativo'], [
            ['Secuencia', 'Lavar la guampa, cargar yerba, servir agua.', 'Leer el precio, leer la cantidad, multiplicar.'],
            ['Decisión', 'Si el agua no está fría, agregar hielo.', 'Si el total llega a 50000, descontar el 10 %.'],
            ['Repetición', 'Mientras haya clientes en la fila, atender al siguiente.', 'Mientras la venta no sea 0, sumarla al total.']]),
        H2('De una instrucción vaga a un algoritmo'),
        P('«Prepará el tereré» no es un algoritmo: falta precisión. Una versión precisa podría ser: 1) llenar la guampa con yerba hasta las tres cuartas partes; 2) cargar la jarra con agua fría y hielo; 3) servir agua hasta cubrir la yerba; 4) tomar y repetir el paso 3 mientras quede agua en la jarra; 5) terminar cuando la jarra quede vacía. Ahora cada paso dice qué hacer, la repetición tiene un final y, con los mismos materiales, el resultado es siempre el mismo.'),
        CAJA('Errores frecuentes — al escribir algoritmos',
             'Pasos que dependen del gusto o de la intuición: «servir lo necesario».',
             'Repeticiones sin condición de corte: «seguí atendiendo».',
             'Pasos fuera de orden: calcular el vuelto antes de leer el pago.')],
        'C13-1', 'Ampliación (456 palabras): las tres estructuras básicas en algoritmos cualitativos y cuantitativos (contenido del programa) y un algoritmo vago reescrito con precisión.')
    sub(c, 'La Figura 3.1 resume el esquema', 'todos los algoritmos del tomo', 'todos los algoritmos del libro', 'C13-2', 'Libro único.')

    c = C[14]
    antes_del_final(c, [
        H2('Reglas de escritura del pseudocódigo'),
        P('El pseudocódigo no tiene una sintaxis tan estricta como un lenguaje de programación, pero en este libro seguimos siempre las mismas reglas para que cualquier persona lo lea igual y para que, en la Clase 21, pasarlo a PSeInt sea casi automático.'),
        TABLA(['Regla', 'Así sí', 'Así no'], [
            ['Una acción por línea', 'Leer total', 'Leer total y después pago'],
            ['Sangría dentro de cada bloque', '    pagar ← total', 'pagar ← total (sin sangría dentro del Si)'],
            ['Nombres sin espacios ni acentos', 'precioUnidad', 'precio unidad'],
            ['Números sin separador de miles', 'total >= 50000', 'total >= 50.000'],
            ['Textos entre comillas rectas', 'Escribir "sin ventas"', 'Escribir «sin ventas»']]),
        P('La regla de los números merece una explicación: en el texto escribimos G. 50.000 con punto de miles, como se escribe en Paraguay, pero dentro del algoritmo el punto separa los decimales en casi todos los lenguajes. 50.000 sería «cincuenta», no «cincuenta mil». Por eso, en el código, los montos van sin separador.'),
        H2('Aplicaciones del diagrama de flujo'),
        P('El diagrama de flujo se usa sobre todo para comunicar: explicar un procedimiento a alguien que no programa, documentar los pasos de un trámite o revisar en equipo un algoritmo antes de escribirlo. El pseudocódigo, en cambio, está más cerca del programa final. Los dos describen el mismo algoritmo; elegir uno u otro depende de quién lo va a leer.'),
        CAJA('Errores frecuentes — pseudocódigo y diagrama',
             'Usar un rectángulo para Leer o Escribir: la entrada y la salida van en paralelogramos.',
             'Olvidar el Fin: sin enunciado de terminación, el algoritmo está incompleto.',
             'Dibujar flechas que se cruzan sin necesidad: el flujo debe leerse de arriba hacia abajo.')],
        'C14-1', 'Ampliación (451 palabras): reglas de escritura del pseudocódigo (incluida la de los números sin separador de miles y las comillas rectas), aplicaciones del diagrama de flujo y errores frecuentes.')

    c = C[15]
    sub(c, 'Las condiciones compuestas se arman con Y', '(total >= 50.000) Y (pago = «QR»)', '(total >= 50000) Y (pago = "QR")', 'C15-1', 'T1/T2: números sin separador de miles y comillas rectas dentro de una expresión.')
    antes_del_final(c, [
        H2('Números dentro de una expresión'),
        P('En una expresión, 50.000 no es «cincuenta mil». En PSeInt y en los lenguajes de programación el punto es la coma decimal: 50.000 vale 50. La comprobación es fácil de hacer: con la condición total >= 50.000, PSeInt aplica el descuento a una compra de 30.000 y cobra 27.000, porque 30.000 es mayor que 50. Por eso en las expresiones escribimos 50000, sin separador, y dejamos el punto de miles para el texto.'),
        H2('Evaluar una expresión larga'),
        P('Con precio = 4000, cantidad = 3 y envio = 2000, evaluemos (precio * cantidad + envio > 10000) Y (cantidad < 5). Se resuelve de adentro hacia afuera y respetando la jerarquía: 4000 * 3 = 12000; 12000 + 2000 = 14000; 14000 > 10000 es V; 3 < 5 es V; V Y V = V. La figura muestra el mismo cálculo como un árbol: las hojas son los datos y la raíz, el resultado.'),
        FIG('fig_n_expresion.png', None,
            'Árbol de evaluación de (precio * cantidad + envio > 10000) Y (cantidad < 5): primero la multiplicación, después la suma, las comparaciones y al final el Y.', 15.0),
        H2('División entera y resto'),
        P('Algunos problemas piden cuántas veces entra un número en otro y cuánto sobra. Con 50 chipas y bandejas de 12: 50 / 12 da 4,1666…; la parte entera, 4, son las bandejas completas, y el resto, 50 mod 12 = 2, las chipas sueltas. Control: 4 × 12 + 2 = 50.'),
        CAJA('Errores frecuentes — expresiones',
             'Calcular de izquierda a derecha sin respetar la jerarquía: 5 + 3 * 2 no es 16.',
             'Escribir montos con punto de miles dentro de una expresión.',
             'Comparar textos sin comillas: medioPago = QR compara con una variable llamada QR.')],
        'C15-2', 'Ampliación (395 palabras): números sin separador de miles en las expresiones (T1, verificado en PSeInt), evaluación de una expresión larga con árbol, división entera y resto, y errores frecuentes.')

    c = C[16]
    antes_del_final(c, [
        H2('Intercambiar dos valores: la variable auxiliar'),
        P('Un problema clásico: Ña Rosa anotó el precio de la chipa en la variable a y el del cocido en b, pero al revés. ¿Cómo se intercambian? Escribir a ← b y después b ← a no funciona: la primera asignación borra el valor viejo de a, y la segunda copia el valor nuevo. Hace falta una variable auxiliar que guarde una copia.'),
        CAJA('Ejemplo — intercambio con variable auxiliar', *COD('Inicio', '    Leer a', '    Leer b', '    aux ← a', '    a ← b', '    b ← aux', '    Escribir a, b', 'Fin'),
             'Con a = 3000 y b = 4000: aux toma 3000, a pasa a 4000 y b a 3000. Se escribe 4000, 3000.'),
        H2('El enunciado de terminación'),
        P('Fin no es un adorno: indica que el algoritmo terminó y que no hay más instrucciones. Un algoritmo sin Fin está incompleto, y uno con instrucciones escritas después del Fin tiene pasos que nunca se ejecutan. En el diagrama de flujo, el Fin es el óvalo de abajo y a él tienen que llegar todas las flechas.'),
        CAJA('Errores frecuentes — algoritmos secuenciales',
             'Usar una variable antes de darle valor: calcular total antes de Leer cantidad.',
             'Escribir la asignación al revés: total ← precio * cantidad, no precio * cantidad ← total.',
             'Pedir un dato con Escribir: Escribir muestra; Leer recibe.')],
        'C16-1', 'Ampliación (432 palabras): intercambio de valores con variable auxiliar, el enunciado de terminación y errores frecuentes.')

    c = C[17]
    antes_del_final(c, [
        H2('Si sin Sino: un solo caso especial'),
        P('No todas las decisiones tienen dos caminos. Si solo hay que hacer algo en un caso, se usa Si… Entonces sin Sino: cuando la condición es F, el algoritmo sigue de largo. Por ejemplo, el delivery cuesta 5000, pero si la distancia supera los 3 km se cobra un recargo de 3000.'),
        CAJA('Ejemplo — recargo por distancia', *COD('Inicio', '    Leer distancia', '    costo ← 5000', '    Si distancia > 3 Entonces', '        costo ← costo + 3000', '    FinSi', '    Escribir costo', 'Fin'),
             'Con distancia = 2 se escribe 5000; con distancia = 6, 8000; con distancia = 3 (frontera), 5000, porque 3 > 3 es F.'),
        H2('Decidir con textos'),
        P('La condición también puede comparar textos: Si medioPago = "QR" Entonces… La comparación es exacta: "QR" y "qr" son textos distintos. Por eso, cuando el dato lo escribe una persona, conviene ofrecer opciones fijas (por ejemplo, 1 para efectivo y 2 para QR) en lugar de dejar que escriba lo que quiera.'),
        CAJA('Errores frecuentes — decisiones simples',
             'Invertir la condición: Si total < 50000 Entonces aplicar descuento.',
             'Poner el cálculo común dentro de un solo camino: lo que se hace en los dos casos va antes o después del Si.',
             'Olvidar el FinSi: sin él, no se sabe dónde terminan las acciones del bloque.')],
        'C17-1', 'Ampliación (416 palabras): Si sin Sino con recargo por distancia, decisiones con textos y errores frecuentes.')

    c = C[18]
    antes_del_final(c, [
        H2('Condiciones compuestas o decisiones anidadas'),
        P('La misma clasificación se puede escribir sin anidar, con condiciones compuestas: Si (total >= 40000) Y (total < 80000) Entonces Escribir "frecuente". Cada categoría necesita entonces su propia condición completa, y hay que verificar a mano que los rangos no se pisen ni dejen huecos. Anidar evita ese trabajo, porque cada Sino ya sabe lo que no se cumplió.'),
        H2('Probar todas las ramas'),
        P('Una clasificación en tres categorías se prueba, como mínimo, con un dato de cada categoría y con los dos valores frontera. Para el clasificador de compras: 95000, 80000, 55000, 40000 y 12000. La tabla muestra qué condición decide cada caso.'),
        TABLA(['total', '¿total >= 80000?', '¿total >= 40000?', 'Escribe'], [
            ['95000', 'V', '(no se evalúa)', 'mayorista'], ['80000', 'V', '(no se evalúa)', 'mayorista'], ['55000', 'F', 'V', 'frecuente'],
            ['40000', 'F', 'V', 'frecuente'], ['12000', 'F', 'F', 'ocasional']]),
        FIG('fig_n_anidada.png', 'La figura dibuja el clasificador de compras: el segundo rombo vive dentro del camino F del primero, y por eso nunca recibe una compra de 80000 o más.',
            'Decisión anidada del clasificador de compras: tres caminos, uno por categoría, y cada compra recorre uno solo.', 15.0),
        CAJA('Errores frecuentes — decisiones anidadas',
             'Preguntar primero por la categoría menos exigente: una compra de 95000 terminaría en «frecuente».',
             'Cerrar los FinSi en el orden equivocado: el último Si abierto es el primero que se cierra.',
             'Dejar huecos entre rangos: con > 80000 y >= 40000, una compra de exactamente 80000 cambia de categoría.')],
        'C18-1', 'Ampliación (389 palabras): condiciones compuestas frente a decisiones anidadas, tabla de prueba con fronteras, figura nueva y errores frecuentes.')
    sub(c, 'Las condiciones se combinan con Y, O y NO', 'Si (total >= 50.000) Y (medioPago = «QR»)', 'Si (total >= 50000) Y (medioPago = "QR")', 'C18-2', 'T1/T2 en una condición del texto.')

    c = C[19]
    antes_del_final(c, [
        H2('Contar hacia atrás o de a saltos'),
        P('El ciclo Para puede avanzar de a más de uno o retroceder. Para c ← 2 Hasta 10 Con Paso 2 Hacer recorre 2, 4, 6, 8 y 10: cinco vueltas. Para c ← 5 Hasta 1 Con Paso −1 Hacer cuenta 5, 4, 3, 2, 1, como una cuenta regresiva. Si el paso no se indica, vale 1.'),
        CAJA('Ejemplo — la tabla del 7', *COD('Inicio', '    Para c ← 1 Hasta 5 Hacer', '        Escribir 7 * c', '    FinPara', 'Fin'), 'Escribe 7, 14, 21, 28 y 35: cinco vueltas, con c de 1 a 5.'),
        H2('Detectar un ciclo infinito en la prueba de escritorio'),
        P('Si en la tabla de la prueba la variable de la condición no cambia de una vuelta a otra, el ciclo no va a terminar. Por ejemplo, con c ← 1 y Mientras c <= 5 Hacer Escribir c FinMientras, la columna de c dice 1, 1, 1… para siempre. La prueba de escritorio lo muestra en la segunda vuelta, mucho antes de que haga falta ejecutar nada.'),
        CAJA('Errores frecuentes — ciclos y contadores',
             'Inicializar el contador dentro del ciclo: vuelve a empezar en cada vuelta.',
             'Usar < en lugar de <=: el ciclo da una vuelta menos.',
             'Modificar a mano la variable de un ciclo Para: el Para ya la incrementa.')],
        'C19-1', 'Ampliación (452 palabras): ciclo Para con paso distinto de 1, ejemplo de la tabla del 7 y detección del ciclo infinito en la prueba de escritorio.')

    c = C[20]
    sub(c, 'Ña Rosa carga sus ventas y termina con 0', 'Escribir «sin ventas»', 'Escribir "sin ventas"', 'C20-1', 'T2: comillas rectas en el código.')
    sub(c, 'Ña Rosa carga sus ventas y termina con 0', 'promedio = 35.000 / 3 ≈ 11.667 (redondeado al guaraní).',
        'promedio = 35.000 / 3 = 11.666,67 (el algoritmo calcula el valor con decimales; al informarlo en guaraníes se redondea a 11.667).', 'C20-2', 'T3: se aclara qué calcula el algoritmo y qué se informa.')
    antes_del_final(c, [
        H2('Contar con condición dentro del ciclo'),
        P('Un contador no siempre cuenta todas las vueltas: puede contar solo las que cumplen algo. Para saber cuántas ventas del mediodía fueron menores que 10000, se agrega un segundo contador que se incrementa dentro de un Si. Con las ventas 12000, 8000 y 15000, ese contador termina en 1.'),
        CAJA('Ejemplo — contar las ventas chicas', *COD('Inicio', '    chicas ← 0', '    Leer venta', '    Mientras venta <> 0 Hacer', '        Si venta < 10000 Entonces', '            chicas ← chicas + 1', '        FinSi', '        Leer venta', '    FinMientras', '    Escribir chicas', 'Fin')),
        H2('El promedio y los decimales'),
        P('Aunque los montos sean enteros, el promedio casi nunca lo es: 35000 / 3 = 11666,67. El algoritmo debe guardar el promedio en una variable que admita decimales; cuando se informa en guaraníes, se redondea al guaraní más cercano. Decidir dónde redondear es parte del diseño: si se redondea cada venta antes de sumar, el total puede cambiar.'),
        CAJA('Errores frecuentes — acumuladores',
             'Acumular el centinela: el 0 se compara pero no se suma.',
             'Dividir dentro del ciclo: el promedio se calcula una vez, al salir.',
             'Inicializar el acumulador en 1, como si fuera un producto.')],
        'C20-3', 'Ampliación (478 palabras): contador condicional dentro del ciclo, el promedio con decimales y errores frecuentes.')

    c = C[21]
    sub(c, 'Resultados finales: recaudación G. 134.000', '145.000 − 11.000 = 134.000. ✓', '145.000 − 11.000 = 134.000.', 'C21-1', 'Se retira el símbolo ✓.')
    ins(c, 'Todo sistema real crece.', [
        H2('Una mejora resuelta: el total de descuentos'),
        P('Ña Rosa quiere saber cuánto dinero «regaló» en descuentos. Alcanza con un acumulador más, desc, que se inicializa en 0 antes del ciclo y suma la diferencia entre la venta y lo cobrado dentro del camino V de la decisión: desc ← desc + (venta − cobrar). Al final se escribe junto con los demás resultados.'),
        P('Con el día real, desc termina en 6.000 + 5.000 = 11.000, exactamente la diferencia del control cruzado. La mejora no tocó la lógica que ya funcionaba: agregó una variable, una línea dentro del Si y un dato más en el Escribir. Así crece un sistema bien diseñado.'),
        CAJA('Concepto clave — control cruzado',
             'Un resultado se confirma calculándolo por otro camino. Si la recaudación más los descuentos no da la suma de las ventas sin descuento, hay un error en algún paso.')],
        'C21-2', 'Ampliación (549 palabras): una mejora resuelta paso a paso (acumulador de descuentos) distinta de las que piden las actividades, con su control cruzado.')
    sub(c, 'Probalo primero con precio = 20.000', 'Cuando ambos resultados coincidan, modificá una sola regla y volvé a comprobar.',
        'Cuando ambos resultados coincidan, modificá una sola regla y volvé a comprobar. El modelo se ejecutó en PSeInt 20250314 con el perfil Flexible; en PSeInt la asignación se escribe <- y no ←.', 'C21-3', 'Puente a PSeInt: se documenta la versión con la que se verificó el modelo y la diferencia de notación.')

    # ------------------------------------------------ código: números sin separador de miles y comillas rectas
    k = 0
    for n, c in C.items():
        for b in c['cuerpo']:
            if b['t'] == 'caja':
                nb = []
                for x in b['body']:
                    if x.startswith('§'):
                        y = re.sub(r'(?<=\d)\.(?=\d{3}\b)', '', x)
                        y = y.replace('«', '"').replace('»', '"')
                        k += y != x; x = y
                    nb.append(x)
                b['body'] = nb
    LOG.append((0, 'T1', 'Código: %d líneas con montos escritos con punto de miles (50.000 se lee 50 en PSeInt) o textos entre comillas angulares pasan a 50000 y comillas rectas.' % k))

    import ampliaciones2
    ampliaciones2.aplicar(C, LOG)
    ampliaciones2.aplicar3(C, LOG)
    _recuadros(C)

    cambios = 0
    for n, c in C.items():
        for b in c['cuerpo']:
            for kk in ('text', 'title'):
                if kk in b:
                    nuevo = re.sub(r'\b(tomo|cuadernillo)\b', 'libro', b[kk]).replace(' ✓', '').replace('✓', '')
                    cambios += nuevo != b[kk]; b[kk] = nuevo
            if 'body' in b:
                nb = [re.sub(r'\b(tomo|cuadernillo)\b', 'libro', x).replace(' ✓', '') for x in b['body']]
                cambios += nb != b['body']; b['body'] = nb
    LOG.append((0, 'G-1', 'Libro único y sin el símbolo ✓: %d bloques ajustados.' % cambios))
    return C


def reemplazar_img(c, archivo, fig):
    i = [k for k, b in enumerate(c['cuerpo']) if b['t'] == 'img' and b['file'].startswith(archivo)]
    assert len(i) == 1
    viejo = c['cuerpo'][i[0]]
    fig['num_viejo'] = viejo.get('num_viejo')
    c['cuerpo'][i[0]] = fig


def _recuadros(C):
    for n, c in C.items():
        cajas = [i for i, b in enumerate(c['cuerpo']) if b['t'] == 'caja' and b['title'].startswith('En Paraguay')]
        assert len(cajas) == 1, (n, len(cajas))
        i = cajas[0]; acc = RECUADROS[n]; b = c['cuerpo'][i]; body = b['body'][:]
        if acc == 'del':
            del c['cuerpo'][i]
            LOG.append((n, 'R', 'Recuadro «En Paraguay» eliminado: no era específico ni verificable o repetía el desarrollo («%s…»).' % ' '.join(body)[:70]))
        elif acc[0] == 'p':
            c['cuerpo'][i] = P(acc[1])
            LOG.append((n, 'R', 'Recuadro «En Paraguay» integrado al texto como párrafo común.'))
        else:
            b['title'] = acc[1]
            if acc[2]:
                b['body'] = acc[2]
            LOG.append((n, 'R', 'Recuadro «En Paraguay» → «%s».' % acc[1]))


def fig_refs(C):
    """Numera las figuras por clase (N.M), corrige las referencias a la numeración vieja y anuncia toda figura."""
    viejo = {}
    for n, c in C.items():
        k = 0
        for b in c['cuerpo']:
            if b['t'] == 'img':
                k += 1
                num = 'Figura %d.%d' % (n, k)
                ep = re.sub(r'^Figura(?: \d+\.\d+)?\s*[—-]\s*', '', b.get('epigrafe', ''))
                b['epigrafe'] = num + ' — ' + ep; b['num'] = num
                if b.get('num_viejo'):
                    viejo[b['num_viejo']] = num
    for n, c in C.items():
        for b in c['cuerpo']:
            if 'text' in b:
                b['text'] = re.sub(r'(Figura|figura) (\d\.\d)\b', lambda m: m.group(1) + ' ' + viejo.get(m.group(2), 'Figura ' + m.group(2)).replace('Figura ', ''), b['text'])
            if b['t'] == 'img' and b.get('lead'):
                pass
        for i, b in enumerate(c['cuerpo']):
            if b['t'] == 'img' and not b.get('lead'):
                j = i - 1; anunciada = False
                while j >= 0 and c['cuerpo'][j]['t'] != 'h2' and not anunciada:
                    q = c['cuerpo'][j]
                    anunciada = q['t'] == 'p' and re.search(r'\bfigura', q['text'], re.I) is not None
                    j -= 1
                if not anunciada:
                    ep = b['epigrafe'].split(' — ', 1)[1].rstrip('.')
                    b['lead'] = 'La %s lo muestra en forma gráfica: %s.' % (b['num'], ep[0].lower() + ep[1:])
    for n, c in C.items():
        for b in c['cuerpo']:
            if b['t'] == 'img' and b.get('lead'):
                b['lead'] = re.sub(r'^(La|El) (figura|diagrama|árbol)', lambda m: '%s %s' % (m.group(1), m.group(2)), b['lead'])
                b['lead'] = b['lead'].replace('La figura', 'La %s' % b['num'], 1).replace('El diagrama de la figura', 'El diagrama de la %s' % b['num'], 1).replace('El árbol de la figura', 'El árbol de la %s' % b['num'], 1)
    return {b['file']: b['num'] for c in C.values() for b in c['cuerpo'] if b['t'] == 'img'}

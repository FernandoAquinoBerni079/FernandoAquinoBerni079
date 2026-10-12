# -*- coding: utf-8 -*-
"""Ronda de correcciones tras la auditoría independiente de ChatGPT (v1.1):
H5 diagrama de flujo / DFD (Clase 14), H6 nombre del silogismo disyuntivo (Clase 12),
H7 expresiones no verificables («favorita», «más común») en las Clases 3, 8 y 17."""


def _rep(C, n, viejo, nuevo, LOG, cod, desc):
    hits = 0
    for b in C[n]['cuerpo']:
        for k in ('text', 'title'):
            if b.get(k) and viejo in b[k]:
                b[k] = b[k].replace(viejo, nuevo); hits += 1
        if 'body' in b:
            nb = [x.replace(viejo, nuevo) for x in b['body']]
            hits += sum(1 for a, z in zip(b['body'], nb) if a != z); b['body'] = nb
        if 'rows' in b:
            nr = [[x.replace(viejo, nuevo) for x in r] for r in b['rows']]
            hits += sum(1 for a, z in zip(b['rows'], nr) if a != z); b['rows'] = nr
        for k in ('epigrafe', 'lead'):
            if b.get(k) and viejo in b[k]:
                b[k] = b[k].replace(viejo, nuevo); hits += 1
    assert hits, (n, viejo[:50])
    LOG.append((n, cod, desc))


def aplicar(C, LOG):
    # H5 — Clase 14: el esquema que se enseña es el diagrama de flujo del algoritmo, no un DFD de análisis de sistemas
    _rep(C, 14, 'El diagrama de flujo de datos (DFD) representa el mismo algoritmo con símbolos gráficos unidos por flechas que marcan el orden de ejecución.',
         'El programa llama a esta herramienta «diagrama de flujo de datos». Lo que se dibuja en esta clase es, técnicamente, el diagrama de flujo del algoritmo: representa el mismo algoritmo con símbolos gráficos unidos por flechas que marcan el orden de ejecución. En análisis de sistemas, la sigla DFD designa otro tipo de diagrama, que muestra por dónde circulan los datos entre procesos y archivos, no el orden de los pasos.',
         LOG, 'A1-5', 'Clase 14: se aclara que la simbología enseñada es la del diagrama de flujo del algoritmo; el nombre del programa se conserva.')
    _rep(C, 14, 'Concepto clave — Pseudocódigo y DFD dicen lo mismo', 'Concepto clave — Pseudocódigo y diagrama de flujo dicen lo mismo',
         LOG, 'A1-5', 'Clase 14: título del concepto clave sin la sigla DFD.')
    # H6 — Clase 12: sin atribuir la nomenclatura al programa; la regla de tres premisas se llama dilema constructivo
    _rep(C, 12, 'Silogismo disyuntivo', 'Dilema constructivo', LOG, 'A1-6', 'Clase 12: la regla p ∨ q; p → r; q → s ⊢ r ∨ s se llama dilema constructivo en la tabla.')
    _rep(C, 12, 'Sobre los nombres: en este libro, siguiendo la convención del programa, «silogismo disyuntivo» es la regla de la tabla (p ∨ q; p → r; q → s ⊢ r ∨ s), y la regla «p ∨ q; ¬p ⊢ q» se llama Modus Tollendo Ponens. Algunos textos llaman «silogismo disyuntivo» a esta segunda: si los consultás, fijate en las premisas, no solo en el nombre.',
         'Sobre los nombres: el programa menciona el silogismo disyuntivo sin dar su forma, y los libros no coinciden. Muchos llaman «silogismo disyuntivo» al Modus Tollendo Ponens (p ∨ q; ¬p ⊢ q): de una disyunción y la negación de una de sus partes se concluye la otra. La regla de tres premisas de la tabla (p ∨ q; p → r; q → s ⊢ r ∨ s) se conoce como dilema constructivo, y algunos textos la presentan con el nombre de silogismo disyuntivo. Si consultás otra fuente, fijate en las premisas, no solo en el nombre.',
         LOG, 'A1-6', 'Clase 12: se quita «siguiendo la convención del programa» y se explican las dos denominaciones.')
    _rep(C, 12, 'silogismo hipotético y silogismo disyuntivo, con sus premisas y su conclusión.', 'silogismo hipotético y dilema constructivo, con sus premisas y su conclusión.',
         LOG, 'A1-6', 'Clase 12: epígrafe de la Figura 12.1.')
    for b in C[12]['cuerpo']:
        if b['t'] == 'p' and b['text'].startswith('El silogismo hipotético encadena condicionales'):
            b['text'] = b['text'].replace('El disyuntivo combina', 'El dilema constructivo combina', 1)
            LOG.append((12, 'A1-6', 'Clase 12: el párrafo explicativo usa «dilema constructivo».'))
    # H7 — expresiones no verificables
    _rep(C, 3, 'por eso el diagrama de Venn es la herramienta favorita para razonar antes de calcular.', 'por eso el diagrama de Venn ayuda a razonar antes de calcular.',
         LOG, 'A1-7', 'Clase 3: sin «herramienta favorita».')
    for n in C:
        for b in C[n]['cuerpo']:
            if b['t'] == 'p' and 'evita el error más común, que es aplicar el conectivo principal antes de tiempo' in b['text']:
                b['text'] = b['text'].replace('evita el error más común, que es aplicar', 'evita un error frecuente: aplicar')
                LOG.append((n, 'A1-7', 'Clase %d: «el error más común» → «un error frecuente».' % n))
    _rep(C, 17, '— es el error más común en los sistemas reales y la pregunta favorita de las evaluaciones.', '— es un error frecuente y un caso que conviene comprobar siempre.',
         LOG, 'A1-7', 'Clase 17: sin «el error más común» ni «la pregunta favorita».')
    # Revisión propia tras la auditoría: «regla estrella» y expresiones de código escritas en el texto con punto de miles
    _rep(C, 12, 'Es la regla estrella:', 'Es la regla básica:', LOG, 'A1-7', 'Clase 12: sin «regla estrella».')
    _rep(C, 15, '5.000 > 3.000', '5000 > 3000', LOG, 'A1-T1', 'Clase 15: tabla de operadores sin punto de miles en la expresión.')
    _rep(C, 15, 'Con precio = 4.000 y cantidad = 3: total ← precio * cantidad + 2.000. Primero la multiplicación: 4.000 * 3 = 12.000; después la suma: 12.000 + 2.000 = 14.000. La expresión (total > 10.000) Y (cantidad < 5)',
         'Con precio = 4000 y cantidad = 3: total ← precio * cantidad + 2000. Primero la multiplicación: 4000 * 3 = 12000; después la suma: 12000 + 2000 = 14000. La expresión (total > 10000) Y (cantidad < 5)',
         LOG, 'A1-T1', 'Clase 15: el ejemplo evaluado paso a paso escribe los números como en el código.')
    _rep(C, 16, 'total ← total + 1.000 es perfectamente válido', 'total ← total + 1000 es perfectamente válido', LOG, 'A1-T1', 'Clase 16: asignación escrita en el texto sin punto de miles.')
    _rep(C, 17, 'El límite exacto importa: total >= 50.000 incluye la compra de exactamente G. 50.000; total > 50.000 la deja afuera.',
         'El límite exacto importa: total >= 50000 incluye la compra de exactamente G. 50.000; total > 50000 la deja afuera.', LOG, 'A1-T1', 'Clase 17: condiciones escritas en el texto sin punto de miles.')
    _rep(C, 18, 'Si el ejemplo preguntara primero total >= 40.000,', 'Si el ejemplo preguntara primero total >= 40000,', LOG, 'A1-T1', 'Clase 18: condición escrita en el texto sin punto de miles.')
    return C

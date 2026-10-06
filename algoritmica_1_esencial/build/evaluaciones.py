# -*- coding: utf-8 -*-
"""Cinco evaluaciones de Algorítmica 1.º (3 de unidad + 2 integradoras de etapa) con su clave.
Se conservan la ubicación, el alcance y la forma del tomo vigente (Parte A con 3 ítems de opción múltiple
de tres opciones; Parte B de resolución), pero se reemplazan los ítems que copiaban un ejemplo resuelto de
la clase, una actividad o una práctica (U1-6, U2-7, U2-8, E1-6, E1-8, E1-9, E2-8 y varias opciones
múltiples), se elimina la ambigüedad de E1 A1 y se corrigen los números con punto de miles y las comillas
«» dentro del código (U3). 'tras' = clase después de la cual se ubica en el libro."""

EV = [
 dict(id='U1', tras=5, titulo='Evaluación de la Unidad 1', sub='Teoría de Conjuntos (Clases 1 a 5)', etapa=False,
  mc=[('n({c, h, i, p, a}) vale:', ['4', '5', '6'], 'b'),
      ('Con U = {1, 2, 3, 4, 5, 6, 7, 8} y A = {1, 2, 3, 4}, el complemento A′ es:', ['∅', '{1, 2, 3, 4}', '{5, 6, 7, 8}'], 'c'),
      ('Un conjunto de 3 elementos tiene una cantidad de subconjuntos igual a:', ['8', '6', '9'], 'a')],
  ab=[('Determiná por extensión: A = {x / x es vocal de la palabra «copetín»} y B = {x / x es par y 2 ≤ x ≤ 10}. Indicá n(A) y n(B).',
       'A = {o, e, i}, n(A) = 3. B = {2, 4, 6, 8, 10}, n(B) = 5.'),
      ('Clasificá cada conjunto (finito, infinito, unitario o vacío): a) los números naturales ; b) {x / x es capital del Paraguay} ; c) los productos del menú con precio G. 0 ; d) los días de la semana.',
       'a) infinito ; b) unitario (solo Asunción) ; c) vacío ; d) finito (7 elementos).'),
      ('Con M = {chipa, mixta, empanada, coquito, gaseosa} y D = {coquito, gaseosa} (lo que no es salado): escribí una relación de pertenencia verdadera, una de inclusión verdadera y todos los subconjuntos de D.',
       'Pertenencia: coquito ∈ M (o gaseosa ∈ D). Inclusión: D ⊂ M. Subconjuntos de D: ∅, {coquito}, {gaseosa}, {coquito, gaseosa} (4 = 2²).'),
      ('Con U = {1, ..., 10}, A = {1, 2, 3, 4, 5} y B = {4, 5, 6, 7}: calculá A ∪ B, A ∩ B, A − B, B − A y A′.',
       'A ∪ B = {1, 2, 3, 4, 5, 6, 7} ; A ∩ B = {4, 5} ; A − B = {1, 2, 3} ; B − A = {6, 7} ; A′ = {6, 7, 8, 9, 10}.'),
      ('De 35 clientes encuestados, 20 compran chipa, 14 compran cocido y 6 compran ambos. Con un diagrama de Venn, calculá cuántos compran solo chipa, solo cocido y ninguno de los dos. Verificá con el control del universo.',
       'Ambos 6 ; solo chipa 20 − 6 = 14 ; solo cocido 14 − 6 = 8 ; ninguno 35 − (14 + 6 + 8) = 7. Control: 14 + 6 + 8 + 7 = 35.')]),
 dict(id='U2', tras=12, titulo='Evaluación de la Unidad 2', sub='Lógica Simbólica (Clases 6 a 12)', etapa=False,
  mc=[('De p → q y ¬q se concluye:', ['p', '¬p', 'q'], 'b'),
      ('La fórmula p ∨ ¬p es:', ['contradicción', 'indeterminación', 'tautología'], 'c'),
      ('¬(p ∨ q) es equivalente a:', ['¬p ∧ ¬q', '¬p ∨ ¬q', 'p ∧ q'], 'a')],
  ab=[('Indicá cuáles de las siguientes expresiones son proposiciones y clasificá las que lo sean en atómicas o moleculares: a) «El guaraní es idioma oficial del Paraguay» ; b) «¿Hay cocido?» ; c) «Hay chipa y no hay gaseosa» ; d) «x > 10».',
       'a) proposición atómica (V) ; b) no es proposición (pregunta) ; c) proposición molecular (conectivos «y» y «no») ; d) no es proposición: es una expresión abierta (depende de x).'),
      ('Con p = V, q = F y r = V, calculá paso a paso: a) (p ∧ q) → r ; b) ¬p ∨ (q ↔ r) ; c) (p ⊻ q) ∧ ¬r.',
       'a) (V ∧ F) → V = F → V = V. b) ¬V ∨ (F ↔ V) = F ∨ F = F. c) (V ⊻ F) ∧ ¬V = V ∧ F = F.'),
      ('Construí la tabla de verdad completa de (p → q) ∧ ¬q y clasificá la fórmula (tautología, contradicción o indeterminación).',
       'p → q: V, F, V, V ; ¬q: F, V, F, V ; (p → q) ∧ ¬q: F, F, F, V. Mezcla V y F: indeterminación.'),
      ('Aplicá De Morgan para negar: «el copetín abre el sábado y hay feria en el colegio». Escribí la negación en símbolos y en palabras.',
       '¬(p ∧ q) ≡ ¬p ∨ ¬q: «el copetín no abre el sábado o no hay feria en el colegio» (falla al menos una).'),
      ('Simbolizá y concluí indicando la regla de inferencia: «Si hay feria, Ña Rosa abre el sábado. Ña Rosa no abre el sábado.»',
       'p = hay feria, q = Ña Rosa abre el sábado. Premisas: p → q y ¬q. Por MTT: ¬p («no hay feria»).')]),
 dict(id='E1', tras=12, titulo='Evaluación integradora de la 1.ª etapa', sub='Unidades 1 y 2 · Cierre de la 1.ª etapa (junio)', etapa=True,
  mc=[('n({x / x es par y 2 ≤ x ≤ 12}) vale:', ['7', '5', '6'], 'c'),
      ('Con p = V, q = V, r = F, el valor de (p ∧ q) → r es:', ['F', 'no se puede saber', 'V'], 'a'),
      ('La negación de «todos los jugos están fríos» es:', ['ningún jugo está frío', 'algún jugo no está frío', 'todos los jugos están calientes'], 'b')],
  ab=[('Con U = {1, ..., 12}, A = {x / x es par y x ≤ 12} y B = {3, 6, 9, 12}: escribí A por extensión y calculá A ∩ B, A ∪ B y (A ∪ B)′.',
       'A = {2, 4, 6, 8, 10, 12}. A ∩ B = {6, 12} ; A ∪ B = {2, 3, 4, 6, 8, 9, 10, 12} ; (A ∪ B)′ = {1, 5, 7, 11}.'),
      ('En una sección de 30 estudiantes, 17 usan la computadora del laboratorio, 12 usan la propia y 5 usan ambas. Calculá con Venn: solo laboratorio, solo propia y ninguna. Verificá el control del universo.',
       'Ambas 5 ; solo laboratorio 17 − 5 = 12 ; solo propia 12 − 5 = 7 ; ninguna 30 − (12 + 5 + 7) = 6. Control: 12 + 5 + 7 + 6 = 30.'),
      ('Simbolizá con p, q, r y paréntesis: «si es sábado y hay feria, entonces abre el copetín». Con p = V, q = V, r = F, calculá su valor de verdad e interpretá el resultado.',
       '(p ∧ q) → r. Con p = V, q = V, r = F: (V ∧ V) → F = V → F = F. Se cumplió la condición (sábado con feria) pero el copetín no abrió: la regla no se respetó.'),
      ('Construí la tabla de verdad de ¬p → q y decidí si es equivalente a p ∨ q comparando columnas.',
       '¬p: F, F, V, V ; ¬p → q: V, V, V, F. p ∨ q: V, V, V, F. Columnas iguales: son equivalentes.'),
      ('Negá con cuantificadores: «todos los clientes de hoy pagaron con QR». Escribí la negación en símbolos y en palabras.',
       '∀x: x pagó con QR. Negación: ∃x: x no pagó con QR («algún cliente de hoy no pagó con QR»).'),
      ('«O el cliente pagó con QR o pagó en efectivo. No pagó en efectivo.» Simbolizá, concluí e indicá la regla de inferencia aplicada.',
       'p = pagó con QR, q = pagó en efectivo. Premisas: p ∨ q y ¬q. Por MTP se concluye p: «pagó con QR».')]),
 dict(id='U3', tras=21, titulo='Evaluación de la Unidad 3', sub='Introducción a la Algoritmia (Clases 13 a 21)', etapa=False,
  mc=[('La instrucción «agregá azúcar a gusto» viola la característica de:', ['precisión', 'finitud', 'salida'], 'a'),
      ('En el diagrama de flujo, el rombo se usa para:', ['leer datos', 'calcular', 'tomar decisiones'], 'c'),
      ('Un acumulador que va a sumar valores se inicializa en:', ['1', '0', 'el primer dato'], 'b')],
  ab=[('Definí algoritmo y explicá sus tres características esenciales con un ejemplo propio de cada una.',
       'Algoritmo: secuencia finita, precisa y definida de pasos que transforma entradas en salidas. Preciso (cada paso se entiende de una sola manera), finito (termina), definido (misma entrada, mismo resultado); se aceptan ejemplos propios correctos.'),
      ('Con precio = 6000 y cantidad = 5, evaluá paso a paso: a) precio * cantidad − 5000 ; b) (precio * cantidad > 25000) Y (cantidad < 10).',
       'a) 6000 * 5 = 30000 ; 30000 − 5000 = 25000. b) 30000 > 25000 (V) Y 5 < 10 (V) = V.'),
      ('Escribí en pseudocódigo un algoritmo que lea un monto y escriba "acepta QR" si el monto es de G. 10.000 o más, y "solo efectivo" en caso contrario. Probalo con 9.000 y 10.000.',
       'Inicio / Leer monto / Si monto >= 10000 Entonces Escribir "acepta QR" Sino Escribir "solo efectivo" FinSi / Fin. Prueba: 9.000 → solo efectivo ; 10.000 → acepta QR (frontera).'),
      ('Hacé la prueba de escritorio de: s ← 0 / Para c ← 1 Hasta 4 Hacer s ← s + c * 1000 FinPara / Escribir s. ¿Qué valor se escribe?',
       'c = 1 → s = 1000 ; c = 2 → 3000 ; c = 3 → 6000 ; c = 4 → 10000. Se escribe 10000.'),
      ('Escribí un algoritmo con centinela 0 que lea ventas, acumule el total y cuente cuántas fueron menores que G. 5.000. Probalo con 4.000, 8.000, 3.000 y 0.',
       'Inicio / suma ← 0 / cm ← 0 / Leer venta / Mientras venta <> 0 Hacer suma ← suma + venta ; Si venta < 5000 Entonces cm ← cm + 1 FinSi ; Leer venta FinMientras / Escribir suma, cm / Fin. Con 4.000, 8.000, 3.000, 0: suma = 15.000, cm = 2.'),
      ('Hacé la prueba de escritorio del sistema de caja Karumbé (10 % de descuento para ventas de G. 50.000 o más, centinela 0) con las ventas 50.000, 20.000 y 0. Indicá suma, c, cd y promedio.',
       '50.000 → 45.000 (cd = 1) ; 20.000 → 20.000. suma = 65.000, c = 2, cd = 1, promedio = 65.000 / 2 = 32.500.')]),
 dict(id='E2', tras=21, titulo='Evaluación integradora de la 2.ª etapa', sub='Unidades 1 a 3 · Cierre de la 2.ª etapa (noviembre)', etapa=True,
  mc=[('Con A = {lunes, miércoles, viernes} y B = {viernes, sábado}, A ∩ B es:', ['∅', '{viernes}', '{sábado}'], 'b'),
      ('¬(p ∧ q) equivale, por De Morgan, a:', ['¬p ∨ ¬q', 'p ∨ q', '¬p ∧ ¬q'], 'a'),
      ('Con la regla «ventas de G. 50.000 o más: 10 % de descuento», una venta de G. 60.000 se cobra:', ['66.000', '60.000', '54.000'], 'c')],
  ab=[("Con A = {lunes, miércoles, viernes} (días con chipa) y B = {viernes, sábado} (días con pastel mandi'o): calculá A ∪ B, A ∩ B y A − B, e interpretá cada resultado en palabras.",
       'A ∪ B = {lunes, miércoles, viernes, sábado} (días con chipa o con pastel) ; A ∩ B = {viernes} (días con los dos) ; A − B = {lunes, miércoles} (días solo con chipa).'),
      ('Con p = V y q = F, calculá: a) ¬(p ∧ q) ; b) (p ∨ q) → q. Indicá además a qué es equivalente ¬(p ∧ q) según De Morgan.',
       'a) ¬(V ∧ F) = ¬F = V. b) (V ∨ F) → F = V → F = F. ¬(p ∧ q) ≡ ¬p ∨ ¬q.'),
      ('«Si la venta es de G. 50.000 o más, se aplica descuento. La venta de Marta no recibió descuento.» Simbolizá, concluí e indicá la regla.',
       'p = la venta es de G. 50.000 o más, q = se aplica descuento. Premisas: p → q y ¬q. Por MTT: ¬p («la venta de Marta fue menor que G. 50.000»).'),
      ('Evaluá con jerarquía de operadores: a) 4 + 6 * 2 ; b) (4 + 6) * 2 ; c) 20 − 8 / 4.',
       'a) 4 + 12 = 16 ; b) 10 * 2 = 20 ; c) 20 − 2 = 18.'),
      ('Escribí un algoritmo que clasifique un pedido de chipas por cantidad: 50 o más, "por mayor"; de 12 a 49, "por docena"; menos de 12, "suelto". Probalo con 50, 12 y 11.',
       'Inicio / Leer cantidad / Si cantidad >= 50 Entonces Escribir "por mayor" Sino Si cantidad >= 12 Entonces Escribir "por docena" Sino Escribir "suelto" FinSi FinSi / Fin. Prueba: 50 → por mayor ; 12 → por docena ; 11 → suelto (las dos primeras son fronteras).'),
      ('Hacé la prueba de escritorio completa del sistema de caja Karumbé (10 % para ventas de G. 50.000 o más, centinela 0) con las ventas 30.000, 50.000, 70.000 y 0. Indicá suma, c, cd y promedio, y verificá con el control cruzado.',
       '30.000 → 30.000 ; 50.000 → 45.000 (cd = 1) ; 70.000 → 63.000 (cd = 2). suma = 138.000, c = 3, cd = 2, promedio = 138.000 / 3 = 46.000. Control: sin descuentos 150.000 − 12.000 = 138.000.'),
      ('Proponé una mejora al sistema de caja (qué variable nueva necesitarías, dónde iría en el algoritmo y para qué le serviría a Ña Rosa).',
       'Ej.: mayor ← 0 antes del ciclo y, dentro, Si venta > mayor Entonces mayor ← venta FinSi, para informar la venta más alta del día. Otra opción: dos acumuladores por medio de pago (efectivo y QR). Se acepta toda mejora con variable, ubicación y utilidad coherentes.')]),
]

NAB = {'U1': 5, 'U2': 5, 'E1': 6, 'U3': 6, 'E2': 7}

if __name__ == '__main__':
    import re
    for e in EV:
        assert len(e['mc']) == 3 and len(e['ab']) == NAB[e['id']], e['id']
        assert all(len(o) == 3 for _, o, _ in e['mc'])
        assert len({c for *_, c in e['mc']}) == 3, e['id']
        for t in [x for a in e['ab'] for x in a] + [m[0] for m in e['mc']]:
            assert not re.search('[✓✗✅✔≈]', t)
            assert not re.search(r'(?:[<>]=?|<>|←|\*)\s*\d{1,3}\.\d{3}\b|Escribir\s*«', t), (e['id'], t)
        print(e['id'], e['titulo'], [c for *_, c in e['mc']])

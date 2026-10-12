# -*- coding: utf-8 -*-
"""Actividades de aplicación de las 21 clases de Algorítmica 1.º (fuente única libro ↔ solucionario).
Base: las 13 actividades de cada clase del tomo vigente, emparejadas con su respuesta del solucionario
(acts_base.json). Se reemplazan las que copiaban el ejemplo resuelto de la clase (mismos datos y misma
pregunta) y se corrigen las que usaban separador de miles o comillas «» dentro del código, el signo ≈
o la marca ✓. Marcador «nuevo» = ítem nuevo o modificado (notas del piloto).
Los algoritmos de las clases 14 a 21 se comprobaron por cálculo; los que también figuran en las prácticas
se ejecutaron en PSeInt (algoritmica_1_esencial/pseint/)."""
import json, re

FAM = {'Ejercitá': 'Ejercitá', 'Resolvé': 'Resolvé (caso Copetín Karumbé)', 'Pensá': 'Pensá y decidí (justificá tu respuesta)', 'Desafío': 'Desafío'}
BASE = json.load(open('/home/claude/alg1/build/acts_base.json'))

R = {}   # (clase, número) → (enunciado, respuesta)
# --- Clase 1 (el ejemplo resuelto es el menú M)
R[1, 7] = ("En el recreo largo, Ña Rosa ofrece cocido, mbeju, pastel mandi'o y jugo. Definí el conjunto R por extensión, calculá n(R) y escribí dos afirmaciones de pertenencia verdaderas (una con ∈ y otra con ∉).",
           "R = {cocido, mbeju, pastel mandi'o, jugo}; n(R) = 4. Ej.: mbeju ∈ R ; gaseosa ∉ R.")
# --- Clase 2 (ejemplo: los fritos F ⊂ M)
R[2, 7] = ('Del menú M, Ña Rosa separa los productos con queso: Q = {chipa, mixta}. Mostrá que Q ⊂ M (justificá con la definición) y escribí todos los subconjuntos de Q.',
           'Todo elemento de Q (chipa, mixta) está en M, y M tiene elementos que Q no tiene (empanada, coquito, gaseosa): por eso Q ⊂ M. Subconjuntos de Q: ∅, {chipa}, {mixta}, {chipa, mixta} (4 = 2²).')
# --- Clase 3 (ejemplo: comestibles C; Figura 3.1: turnos con la mixta en el centro)
R[3, 2] = ('Con U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} y P = {x / x es número primo}, indicá qué queda dentro del óvalo P y qué queda fuera pero dentro de U.',
           'Dentro de P: 2, 3, 5, 7. Fuera del óvalo pero dentro de U: 1, 4, 6, 8, 9, 10.')
R[3, 7] = ('En el mostrador, U = {chipa, mixta, empanada, coquito, gaseosa, jugo}. Describí el diagrama con B = bebidas = {gaseosa, jugo} e indicá qué elementos quedan fuera del óvalo.',
           'Óvalo B = {gaseosa, jugo}; fuera del óvalo, dentro del rectángulo U: chipa, mixta, empanada y coquito (pertenecen al universo, no a B).')
R[3, 8] = ('Con A = {chipa, cocido, coquito} (mañana) y B = {cocido, empanada, jugo} (siesta), ubicá cada producto en su región del diagrama de dos óvalos.',
           'solo A (mañana): chipa, coquito ; A∩B (ambos turnos): cocido ; solo B (siesta): empanada, jugo ; fuera: ninguno (todos están en A o en B).')
# --- Clase 4 (ejemplo: pedidos del lunes A = {chipa, mixta, coquito}, B = {mixta, empanada, gaseosa})
R[4, 2] = ('Con A = {QR, efectivo} (medios de pago del turno mañana) y B = {efectivo, tarjeta} (turno siesta): calculá A∪B y A∩B.',
           'A∪B = {QR, efectivo, tarjeta} ; A∩B = {efectivo}.')
R[4, 7] = ('Los pedidos del martes: turno mañana A = {chipa, empanada, jugo, cocido}, turno siesta B = {empanada, coquito, cocido}. Calculá todo lo vendido en el día (A∪B) y lo pedido en ambos turnos (A∩B).',
           'A∪B = {chipa, empanada, jugo, cocido, coquito} (todo lo vendido); A∩B = {empanada, cocido} (pedido en los dos turnos).')
R[4, 8] = ('Con A y B del ítem anterior y C = {coquito, gaseosa}: calculá (A∩B)∪C y A∩(B∪C).',
           'A∩B = {empanada, cocido}; (A∩B)∪C = {empanada, cocido, coquito, gaseosa}. B∪C = {empanada, coquito, cocido, gaseosa}; A∩(B∪C) = {empanada, cocido}. Los resultados son distintos.')
R[4, 9] = ('Verificá con los conjuntos A y B del martes (ítem 7) la fórmula n(A∪B) = n(A) + n(B) − n(A∩B) contando los elementos.',
           'n(A) = 4, n(B) = 3, n(A∩B) = 2, n(A∪B) = 5. 4 + 3 − 2 = 5: la fórmula se cumple.')
R[4, 13] = ('En una encuesta rápida, 24 clientes piden cocido y 17 piden chipa; 9 piden ambos. Usando n(A∪B) = n(A) + n(B) − n(A∩B), calculá cuántos piden al menos uno de los dos.',
            'Al menos uno = n(A∪B) = 24 + 17 − 9 = 32 clientes.')
R[4, 5] = ('Con A = {1,2,3,4,5} y B = {4,5,6,7}: calculá A∪B, A∩B y verificá n(A∪B) = n(A) + n(B) − n(A∩B).',
           'A∪B = {1,2,3,4,5,6,7} (n = 7) ; A∩B = {4,5} (n = 2). 5 + 4 − 2 = 7: la fórmula se cumple.')
# --- Clase 5 (ejemplos: A − B con los turnos del lunes; encuesta 30/18/15/8)
R[5, 3] = ('Con A = {chipa, empanada, jugo, cocido} y B = {empanada, coquito, cocido}: calculá A−B y B−A.',
           'A−B = {chipa, jugo} ; B−A = {coquito}.')
R[5, 4] = ('Con U = {efectivo, QR, tarjeta, transferencia} y A = {efectivo, QR}: calculá A′.',
           'A′ = {tarjeta, transferencia}.')
R[5, 6] = ('Encuesta: 36 clientes, 21 compran chipa, 13 compran gaseosa y 7 compran ambas. Calculá solo chipa, solo gaseosa y ninguna, y verificá que las cuatro regiones sumen 36.',
           'Centro 7 ; solo chipa 21 − 7 = 14 ; solo gaseosa 13 − 7 = 6 ; ninguna 36 − (14 + 7 + 6) = 9. Control: 14 + 7 + 6 + 9 = 36.')
R[5, 7] = ('De 40 clientes del copetín, 22 pagan en efectivo, 25 con QR y 12 usan ambos medios. Calculá solo efectivo, solo QR y ninguno; verificá con el control del universo.',
           'Ambos 12 ; solo efectivo 22 − 12 = 10 ; solo QR 25 − 12 = 13 ; ninguno 40 − (10 + 12 + 13) = 5. Control: 10 + 12 + 13 + 5 = 40.')
R[5, 8] = ('Con U = {1, ..., 10}, A = {1,2,3,4,5} y B = {4,5,6,7}: comprobá con estos conjuntos que (A∩B)′ = A′∪B′.',
           'A∩B = {4,5}; (A∩B)′ = {1,2,3,6,7,8,9,10}. A′ = {6,7,8,9,10}; B′ = {1,2,3,8,9,10}; A′∪B′ = {1,2,3,6,7,8,9,10}. Coinciden.')
R[5, 13] = ('De 50 clientes: 30 compran chipa, 25 compran cocido y 10 no compran ninguno de los dos. Calculá cuántos compran ambos (pista: primero calculá cuántos compran al menos uno) y armá el diagrama con las cuatro regiones.',
            'Al menos uno = 50 − 10 = 40. Ambos = 30 + 25 − 40 = 15. Solo chipa = 30 − 15 = 15 ; solo cocido = 25 − 15 = 10 ; ninguno = 10. Control: 15 + 15 + 10 + 10 = 50.')
# --- Clase 6 (ejemplo: «Hay chipa», «Hay chipa y hay cocido», «Hoy no hay empanada», «el producto x está agotado»)
R[6, 2] = ('Clasificá las que sean proposición en atómica o molecular: a) «Hay mbeju» ; b) «Hay cocido o hay tereré» ; c) «No aceptamos tarjeta».',
           'a) atómica ; b) molecular (conectivo «o») ; c) molecular (negación «no»).')
R[6, 5] = ('Identificá cuáles son proposiciones abiertas: a) «x es par» ; b) «hoy es lunes» ; c) «el cliente x pagó con QR».',
           'a) abierta ; b) no (es proposición cerrada) ; c) abierta (depende de qué cliente sea x).')
# --- Clase 7 (ejemplos: harina, queso y chipa; la promesa de las dos chipas)
R[7, 2] = ('Simbolizá: a) «no hay chipa pero hay cocido» (p, q) ; b) «hay chipa o hay mixta» ; c) «si llueve y hace frío, se vende cocido» (p, q, r).',
           'a) ¬p ∧ q ; b) p ∨ q ; c) (p ∧ q) → r.')
R[7, 9] = ('Ña Rosa avisa: «si llueve, se vende más cocido» (p = «llueve», q = «se vende más cocido»). Escribí p→q y explicá en qué único caso el aviso resulta falso.',
           'p→q: es F solo si llueve (p = V) y no se vende más cocido (q = F). Si no llueve, el aviso no queda desmentido, se venda más cocido o no.')
# --- Clase 8 (ejemplo: ¬p ∨ q coincide con p → q)
R[8, 4] = ('Construí la tabla de ¬p ∧ ¬q e indicá en qué única fila es verdadera.',
           '¬p: F,F,V,V ; ¬q: F,V,F,V ; ¬p ∧ ¬q: F,F,F,V. Es V solo en la fila p = F, q = F.')
R[8, 9] = ('Construí la tabla de p↔q y la de (p∧q) ∨ (¬p∧¬q), y compará sus columnas finales: ¿coinciden?',
           'p↔q: V,F,F,V. p∧q: V,F,F,F ; ¬p∧¬q: F,F,F,V ; disyunción: V,F,F,V. Sí, coinciden: las dos fórmulas son equivalentes.')
# --- Clase 9 (ejemplos: (p ∧ q) → p tautología; (p ∧ q) → r con 8 filas)
R[9, 2] = ('Construí la tabla de (p∨q)→p e indicá su clase (tautología, contradicción o indeterminación).',
           'p∨q: V,V,V,F ; (p∨q)→p: V,V,F,V → indeterminación (es F en la fila p = F, q = V).')
R[9, 7] = ('Construí la tabla completa (8 filas) de (p∨q)→r e indicá las filas en que resulta falsa.',
           'p∨q es V en las filas 1 a 6. (p∨q)→r es F cuando p∨q = V y r = F: filas 2 (V V F), 4 (V F F) y 6 (F V F). En las otras 5 filas es V: indeterminación.')
# --- Clase 10 (ejemplo: negar «hay chipa y hay cocido»)
R[10, 6] = ('Negá con De Morgan: «hay mbeju o hay chipa».',
            '¬p ∧ ¬q: «no hay mbeju y no hay chipa» (no hay ninguno de los dos).')
R[10, 7] = ('Verificá con tablas de verdad que ¬(p∨q) ≡ ¬p∧¬q.',
            '¬(p∨q): p∨q = V,V,V,F → F,F,F,V. ¬p∧¬q: (F,F,V,V)∧(F,V,F,V) = F,F,F,V. Las columnas son iguales: la equivalencia se cumple.')
R[10, 9] = ('Negá correctamente el aviso «el copetín abre el sábado y abre el domingo» y explicá por qué «no abre el sábado y no abre el domingo» sería un error.',
            'Negación correcta: «no abre el sábado o no abre el domingo» (¬p ∨ ¬q): basta que cierre uno de los dos días. «No abre ni el sábado ni el domingo» es ¬p ∧ ¬q, la negación de p ∨ q: niega otra cosa.')
# --- Clase 11 (ejemplo: ∃ «x cuesta G. 500»; ∀ «x es frito» con la gaseosa de contraejemplo)
R[11, 2] = ('Sobre el menú M con los precios del día (chipa 4.000, mixta 10.000, empanada 6.000, coquito 500, gaseosa 8.000), decidí el valor de ∃x: «x cuesta G. 6.000».',
            'V — la empanada cuesta G. 6.000 (existe al menos uno).')
R[11, 7] = ('Sobre M = {chipa, mixta, empanada, coquito, gaseosa}: evaluá ∀x: «x es salado» y dá un contraejemplo si resulta falsa.',
            '∀x: «x es salado» es F. Contraejemplo: el coquito (es dulce); la gaseosa también sirve.')
R[11, 9] = ('Ña Rosa afirma: «existe al menos un producto que cuesta menos de G. 5.000». Con los precios del día, decidí el valor y justificá exhibiendo un ejemplo.',
            'V — basta exhibir un ejemplo: la chipa cuesta G. 4.000 < G. 5.000 (el coquito también sirve).')
# --- Clase 12 (ejemplo: «si es viernes, hay chipa» con MTT)
R[12, 9] = ('«Si hay corte de luz, el horno no anda. El horno anda.» Simbolizá, concluí e indicá la regla; después explicá por qué de «si hay corte de luz, el horno no anda» y «el horno no anda» NO se concluye que haya corte de luz.',
            'p = hay corte de luz, q = el horno no anda. Premisas: p→q y ¬q. Por MTT: ¬p («no hay corte de luz»). De p→q y q no se concluye p (falacia de afirmación del consecuente): el horno puede no andar por otra causa, por ejemplo, porque se rompió.')
# --- Clase 13 (ejemplo: «preparar el mostrador» y «calcular el vuelto»)
R[13, 3] = ('Para «calcular el precio de media docena de chipas», identificá entrada, proceso y salida.',
            'Entrada: el precio de una chipa. Proceso: precio × 6. Salida: el precio de la media docena.')
R[13, 6] = ('Escribí los pasos (3 a 4) de un algoritmo cualitativo para «reponer las servilletas de las mesas».',
            'Ej.: 1) buscar el paquete de servilletas en el depósito ; 2) recorrer las mesas una por una ; 3) completar cada servilletero ; 4) guardar el paquete en su lugar.')
R[13, 13] = ('Escribí dos algoritmos de la tarde del copetín: uno cualitativo («lavar las tazas») y uno cuantitativo («calcular cuántas docenas completas de chipa salieron del horno, conociendo la cantidad de chipas»), con pasos numerados, y justificá por qué cada uno pertenece a su tipo.',
             'Cualitativo: 1) juntar las tazas usadas ; 2) lavarlas con detergente ; 3) enjuagarlas ; 4) dejarlas secar boca abajo (no hay cálculos). Cuantitativo: 1) leer la cantidad de chipas ; 2) docenas ← trunc(cantidad / 12) ; 3) escribir docenas (opera con números; con 50 chipas da 4 docenas completas).')
# --- Clase 14 (ejemplo: el vuelto con 12.000 y 20.000; Figura 16.1: docena a 48.000)
R[14, 4] = ('Traducí a símbolos del diagrama cada línea de este algoritmo: Inicio, Leer precio, Leer cantidad, total ← precio * cantidad, Escribir total, Fin.',
            'Inicio → óvalo ; Leer precio → paralelogramo ; Leer cantidad → paralelogramo ; total ← precio * cantidad → rectángulo ; Escribir total → paralelogramo ; Fin → óvalo.')
R[14, 7] = ('La media docena de empanadas cuesta G. 33.000 en la promo. Escribí en pseudocódigo un algoritmo que lea el precio de la media docena y escriba el precio de una empanada. Probalo con 33000.',
            'Inicio / Leer precioMedia / unidad ← precioMedia / 6 / Escribir unidad / Fin. Con 33000: 33000 / 6 = 5500 (G. 5.500).')
R[14, 8] = ('Indicá qué símbolo del diagrama corresponde a cada línea del algoritmo Inicio / Leer lado / perimetro ← lado * 4 / Escribir perimetro / Fin, y cuántas figuras tiene el diagrama.',
            'Inicio → óvalo ; Leer lado → paralelogramo ; perimetro ← lado * 4 → rectángulo ; Escribir perimetro → paralelogramo ; Fin → óvalo. Cinco figuras: 2 óvalos, 2 paralelogramos y 1 rectángulo.')
R[14, 9] = ('Escribí el pseudocódigo de un algoritmo que lea el precio de un producto y la cantidad, y escriba el total. Probalo con precio = 6000 y cantidad = 4.',
            'Inicio / Leer precio / Leer cantidad / total ← precio * cantidad / Escribir total / Fin. Con 6000 y 4: total = 24000 (G. 24.000).')
R[14, 13] = ('Escribí en pseudocódigo un algoritmo que lea dos precios y escriba el total; describí su diagrama de flujo completo con los símbolos correctos y probalo con 4000 y 6000.',
             'Inicio / Leer precio1 / Leer precio2 / total ← precio1 + precio2 / Escribir total / Fin. Diagrama: óvalo (Inicio) → paralelogramo (Leer precio1) → paralelogramo (Leer precio2) → rectángulo (suma) → paralelogramo (Escribir total) → óvalo (Fin). Con 4000 y 6000: total = 10000.')
# --- Clase 15 (ejemplo: precio 4.000, cantidad 3, + 2.000; tabla de operadores)
R[15, 2] = ('Evaluá las relacionales (V/F): a) 7000 > 9000 ; b) 3 < 12 ; c) 15 >= 16 ; d) 4 <> 6.',
            'a) F ; b) V ; c) F ; d) V.')
R[15, 3] = ('Con precio = 6000 y cantidad = 2, evaluá total ← precio * cantidad + 3000.',
            '6000 * 2 = 12000 ; 12000 + 3000 = 15000.')
R[15, 6] = ('Clasificá el tipo de dato: a) 4000 ; b) "chipa" ; c) Verdadero.',
            'a) numérico ; b) texto (cadena) ; c) lógico.')
R[15, 7] = ('Evaluá paso a paso, con precio = 5000 y cantidad = 4: a) precio * cantidad − 3000 ; b) precio * (cantidad − 3) ; c) (precio * cantidad > 15000) Y (cantidad <= 4).',
            'a) 5000 * 4 = 20000 ; 20000 − 3000 = 17000. b) (4 − 3) = 1 ; 5000 * 1 = 5000. c) 5000 * 4 = 20000 > 15000 (V) Y 4 <= 4 (V) = V.')
R[15, 8] = ('Escribí una expresión lógica que sea V cuando un cliente compra 2 o más chipas Y paga con QR, usando las variables cantidadChipas y medioPago.',
            '(cantidadChipas >= 2) Y (medioPago = "QR"). El texto va entre comillas rectas; sin comillas, QR sería el nombre de una variable.')
R[15, 9] = ('Con precio = 2500 y cantidad = 6, calculá total ← precio * cantidad − 1000 y evaluá (total > 12000) Y (cantidad < 5).',
            'total = 2500 * 6 − 1000 = 15000 − 1000 = 14000 ; (14000 > 12000) Y (6 < 5) = V Y F = F.')
R[15, 13] = ('Escribí la fórmula del «precio con 10 % de recargo» como base + base * 10 / 100, evaluala con base = 20000 respetando la jerarquía, y mostrá con paréntesis cómo cambiaría el resultado si se sumara antes de multiplicar.',
             'base + base * 10 / 100 con base = 20000: primero 20000 * 10 = 200000 ; / 100 = 2000 ; + 20000 = 22000. Con paréntesis (base + base) * 10 / 100 = 40000 * 10 / 100 = 4000: el resultado cambia por completo, por eso la jerarquía importa.')
# --- Clase 16 (ejemplos: la compra completa con 4.000, 3 y 20.000; intercambio con auxiliar)
R[16, 6] = ('Hacé las dos primeras filas de la prueba de escritorio de la compra completa con precioChipa = 4000 y cantidad = 7, con una columna por variable.',
            'Fila 1 (Leer precioChipa): precioChipa = 4000; las demás, sin valor. Fila 2 (Leer cantidad): precioChipa = 4000, cantidad = 7; total y vuelto, todavía sin valor.')
R[16, 7] = ('Escribí un algoritmo que lea los precios de tres productos y escriba el total de la compra. Hacé la prueba de escritorio con 4000, 6000 y 2500.',
            'Inicio / Leer p1 / Leer p2 / Leer p3 / total ← p1 + p2 + p3 / Escribir total / Fin. Prueba: total = 4000 + 6000 + 2500 = 12500.')
R[16, 9] = ('Escribí el algoritmo de la compra de empanadas (Leer precio, cantidad, pago ; total ← precio * cantidad ; vuelto ← pago − total ; Escribir total, vuelto) y probalo con 6000, 4 y 30000.',
            'total = 6000 * 4 = 24000 ; vuelto = 30000 − 24000 = 6000. Se escriben total = 24000 y vuelto = 6000.')
R[16, 13] = ('Escribí un algoritmo que «rote» los valores de tres variables (a recibe el valor de b, b el de c y c el de a) usando una variable auxiliar, y hacé la prueba de escritorio con a = 1, b = 2 y c = 3.',
             'Inicio / aux ← a / a ← b / b ← c / c ← aux / Escribir a, b, c / Fin. Prueba: aux = 1 ; a = 2 ; b = 3 ; c = 1. Se escriben 2, 3 y 1.')
# --- Clase 17 (ejemplo: descuento con 60.000, 50.000 y 30.000)
R[17, 1] = ('Con total = 72.000 y la regla «compras de 50.000 o más, 10 % de descuento», calculá cuánto se paga.',
            '72.000 − 7.200 = 64.800.')
R[17, 2] = ('Con total = 49.000 y la misma regla, calculá cuánto se paga.',
            '49.000 (no alcanza el descuento).')
R[17, 3] = ('Con total = 55.000 y la condición total >= 50000, calculá cuánto se paga.',
            '55.000 − 5.500 = 49.500.')
R[17, 5] = ('Escribí la condición de un Si para «la compra supera G. 40.000».',
            'total > 40000 (sin separador de miles dentro del código).')
R[17, 7] = ('Escribí un algoritmo que lea la edad de una persona y escriba "puede votar" si la edad es 18 o más, y "todavía no" en caso contrario. Probalo con 17, 18 y 45.',
            'Inicio / Leer edad / Si edad >= 18 Entonces Escribir "puede votar" Sino Escribir "todavía no" FinSi / Fin. Prueba: 17 → todavía no ; 18 → puede votar ; 45 → puede votar.')
R[17, 8] = ('Ña Rosa regala un cocido cuando la compra supera G. 40.000. Escribí el algoritmo (Leer total, decidir, Escribir el mensaje) y explicá qué pasa con una compra de exactamente G. 40.000 según la condición que elegiste.',
            'Inicio / Leer total / Si total > 40000 Entonces Escribir "regalo un cocido" Sino Escribir "sin regalo" FinSi / Fin. Con exactamente 40000, la condición total > 40000 es F: no hay regalo («supera» se traduce con >).')
R[17, 9] = ('Escribí el algoritmo del descuento (compras de 50.000 o más, 10 %) con Si–Entonces–Sino y hacé la prueba de escritorio con 85.000, 50.000 y 42.000.',
            'Si total >= 50000 Entonces pagar ← total − total * 10 / 100 Sino pagar ← total FinSi. Prueba: 85.000 → 76.500 ; 50.000 → 45.000 (frontera) ; 42.000 → 42.000.')
R[17, 13] = ('Escribí un algoritmo que lea el total y el medio de pago y aplique 10 % de descuento solo si el total es de 50.000 o más Y el pago es con QR. Probalo con (60.000, QR), (60.000, efectivo) y (40.000, QR).',
             'Inicio / Leer total / Leer medioPago / Si (total >= 50000) Y (medioPago = "QR") Entonces pagar ← total − total * 10 / 100 Sino pagar ← total FinSi / Escribir pagar / Fin. Pruebas: (60.000, QR) → 54.000 ; (60.000, efectivo) → 60.000 ; (40.000, QR) → 40.000.')
# --- Clase 18 (ejemplo: mayorista / frecuente / ocasional con 80.000 y 40.000)
R[18, 3] = ('El stock de cada producto se clasifica así: 50 unidades o más, «suficiente»; de 10 a 49, «bajo»; menos de 10, «crítico». Clasificá: 120, 50, 49, 10 y 3.',
            '120 suficiente ; 50 suficiente (frontera) ; 49 bajo ; 10 bajo (frontera) ; 3 crítico.')
R[18, 5] = ('Con stock = 10, decidí la categoría según la regla del ejercicio 3.',
            'Bajo (10 >= 10 es V, y 10 >= 50 es F).')
R[18, 6] = ('Ordená las preguntas de la más exigente a la menos exigente para los tramos del ejercicio 3.',
            'Preguntar primero stock >= 50 y después stock >= 10; lo que queda es «crítico».')
R[18, 7] = ('Escribí un algoritmo que lea una calificación de 1 a 5 y escriba "excelente" si es 5, "aprobado" si es 2, 3 o 4, y "reprobado" si es 1. Probalo con 5, 3 y 1.',
            'Inicio / Leer nota / Si nota = 5 Entonces Escribir "excelente" Sino Si nota = 1 Entonces Escribir "reprobado" Sino Escribir "aprobado" FinSi FinSi / Fin. Prueba: 5 → excelente ; 3 → aprobado ; 1 → reprobado.')
R[18, 8] = ('Ña Rosa cobra el delivery así: pedidos de G. 100.000 o más, envío gratis ; de 50.000 a menos de 100.000, envío G. 5.000 ; menos de 50.000, envío G. 10.000. Escribí la decisión anidada y probala con 120.000, 100.000, 70.000 y 30.000.',
            'Si total >= 100000 Entonces envio ← 0 Sino Si total >= 50000 Entonces envio ← 5000 Sino envio ← 10000 FinSi FinSi. Prueba: 120.000 → gratis ; 100.000 → gratis (frontera) ; 70.000 → 5.000 ; 30.000 → 10.000.')
R[18, 9] = ('Clasificá el stock (suficiente / bajo / crítico) con una decisión anidada y hacé la prueba con 75 y 9.',
            'Si stock >= 50 Entonces Escribir "suficiente" Sino Si stock >= 10 Entonces Escribir "bajo" Sino Escribir "crítico" FinSi FinSi. Prueba: 75 → suficiente ; 9 → crítico.')
R[18, 13] = ('Escribí un algoritmo que lea total y medioPago y clasifique en "mayorista con QR", "mayorista sin QR" o "no mayorista" (mayorista: 80.000 o más), combinando una condición con una decisión anidada. Probalo con (90.000, QR), (90.000, efectivo) y (30.000, QR).',
             'Inicio / Leer total / Leer medioPago / Si total >= 80000 Entonces Si medioPago = "QR" Entonces Escribir "mayorista con QR" Sino Escribir "mayorista sin QR" FinSi Sino Escribir "no mayorista" FinSi / Fin. Pruebas: (90.000, QR) → mayorista con QR ; (90.000, efectivo) → mayorista sin QR ; (30.000, QR) → no mayorista.')
# --- Clase 19 (ejemplos: del 1 al 5 con Mientras; la tabla del 7 con Para)
R[19, 1] = ('¿Cuántas vueltas da: c ← 3 ; Mientras c <= 7 Hacer Escribir c ; c ← c + 1 FinMientras?',
            '5 vueltas (c toma 3, 4, 5, 6, 7; con c = 8 la condición es F).')
R[19, 3] = ('Escribí con Mientras un algoritmo que escriba los números del 4 al 9.',
            'Inicio / c ← 4 / Mientras c <= 9 Hacer Escribir c ; c ← c + 1 FinMientras / Fin. Da 6 vueltas.')
R[19, 8] = ('El copetín atiende 8 clientes por hora pico. Escribí con Para un algoritmo que escriba «Cliente n atendido» para n de 1 a 8, e indicá cuántas vueltas da.',
            'Para n ← 1 Hasta 8 Hacer Escribir "Cliente ", n, " atendido" FinPara. Da 8 vueltas.')
R[19, 9] = ('Escribí con Mientras un algoritmo que escriba 5, 10, 15 y 20, y hacé la prueba de escritorio con las columnas c y «¿c <= 20?».',
            'c ← 5 ; Mientras c <= 20 Hacer Escribir c ; c ← c + 5 FinMientras. Prueba: (c = 5, V, escribe 5) (10, V, 10) (15, V, 15) (20, V, 20) (25, F, termina).')
# --- Clase 20 (ejemplo: la caja del mediodía con 12.000, 8.000 y 15.000)
R[20, 3] = ('Calculá el promedio con suma = 42.000 y c = 4.',
            'promedio = 42.000 / 4 = 10.500.')
R[20, 6] = ('Con suma = 0, aplicá suma ← suma + 15000 y luego suma ← suma + 9000. ¿Cuánto vale suma?',
            'suma = 24000.')
R[20, 7] = ('Escribí un algoritmo que lea las ventas del día hasta el centinela 0 y escriba solamente cuántas ventas superaron G. 10.000. Probalo con 12.000, 6.000, 25.000, 9.000 y 0.',
            'Inicio / cg ← 0 / Leer venta / Mientras venta <> 0 Hacer Si venta > 10000 Entonces cg ← cg + 1 FinSi ; Leer venta FinMientras / Escribir cg / Fin. Con 12.000, 6.000, 25.000, 9.000, 0: cg = 2 (12.000 y 25.000).')
R[20, 9] = ('Escribí un algoritmo con centinela 0 que acumule las propinas del día, cuente cuántas hubo y calcule el promedio protegiendo la división por cero. Probalo con 2.000, 5.000, 5.000 y 0.',
            'Inicio / suma ← 0 / c ← 0 / Leer propina / Mientras propina <> 0 Hacer suma ← suma + propina ; c ← c + 1 ; Leer propina FinMientras / Si c > 0 Entonces Escribir suma, suma / c Sino Escribir "sin propinas" FinSi / Fin. Prueba: suma = 12.000, c = 3, promedio = 4.000.')
R[20, 11] = ('V o F: «Si no se carga ningún dato, el algoritmo de la caja del mediodía escribe la leyenda "sin ventas".»',
             'VERDADERO — si c = 0, el Si c > 0 es falso y se ejecuta el Sino, que escribe "sin ventas".')
R[20, 13] = ('Modificá el algoritmo de la caja para que, además de la suma y el promedio, informe la venta más alta del día (pista: mayor ← 0 y una decisión dentro del ciclo). Probalo con 12.000, 30.000, 9.000 y 0.',
             'Agregar mayor ← 0 antes del ciclo y, dentro del ciclo, Si venta > mayor Entonces mayor ← venta FinSi. Con 12.000, 30.000, 9.000, 0: suma = 51.000, c = 3, promedio = 17.000, mayor = 30.000.')
# --- Clase 21 (ejemplo: el día real 20.000, 60.000, 15.000, 50.000)
R[21, 2] = ('Con una venta de G. 75.000, calculá cuánto se cobra (10 % de descuento si es de 50.000 o más).',
            '75.000 − 7.500 = 67.500.')
R[21, 3] = ('Con una venta de G. 49.999, calculá cuánto se cobra.',
            '49.999 (no llega a 50.000: sin descuento).')
R[21, 4] = ('Con una venta de G. 35.000, calculá cuánto se cobra.',
            '35.000 (no alcanza el descuento).')
R[21, 6] = ('Calculá el promedio con suma = 126.000 y c = 4.',
            '126.000 / 4 = 31.500.')
R[21, 7] = ('Hacé la prueba de escritorio completa del sistema de caja Karumbé con las ventas 45.000, 80.000, 10.000, 15.000 y el centinela 0. Indicá suma, c, cd y promedio, y verificá con el control cruzado.',
            '45.000 → cobrar 45.000 (sin descuento) ; 80.000 → 72.000 (cd = 1) ; 10.000 → 10.000 ; 15.000 → 15.000. suma = 142.000, c = 4, cd = 1, promedio = 142.000 / 4 = 35.500. Control: sin descuentos 150.000 − 8.000 = 142.000.')
R[21, 9] = ('Hacé la prueba de escritorio del sistema con las ventas 30.000, 55.000, 90.000 y el centinela 0. Indicá suma, c, cd y promedio.',
            '30.000 → 30.000 ; 55.000 → 49.500 (cd = 1) ; 90.000 → 81.000 (cd = 2). suma = 160.500, c = 3, cd = 2, promedio = 160.500 / 3 = 53.500. Control: sin descuentos 175.000 − 14.500 = 160.500.')
R[21, 13] = ('Ampliá el sistema para separar lo cobrado en efectivo y con QR (dos acumuladores más y una decisión por medio de pago). Escribí el fragmento que agregás y explicá dónde va dentro del ciclo.',
             'Antes del ciclo: sumaEf ← 0 y sumaQR ← 0. Dentro del ciclo, después de calcular cobrar: Leer medioPago ; Si medioPago = "QR" Entonces sumaQR ← sumaQR + cobrar Sino sumaEf ← sumaEf + cobrar FinSi. Va después de la decisión del descuento y antes de leer la próxima venta. Control: sumaEf + sumaQR = suma.')

R[17, 6] = ('Decidí si las condiciones total > 50000 y total >= 50000 dan el mismo resultado con total = 50.000.',
            'No — con >= la compra de 50.000 recibe descuento; con > no. Difieren justo en la frontera.')
R[17, 10] = ('V o F: «Las condiciones total > 50000 y total >= 50000 son equivalentes.»',
             'FALSO — difieren en el caso frontera (total = 50.000): >= lo incluye, > lo deja afuera.')
R[21, 12] = ('Elegí y justificá: una venta de exactamente G. 50.000 se cobra a) 50.000 b) 55.000. c) 45.000.',
             'c) 45.000 — con la condición venta >= 50000, la frontera recibe el 10 %: 50.000 − 5.000 = 45.000.')

# T6: opciones de «Elegí y justificá» con una sola forma de puntuación (a) X; b) Y; c) Z.)
OPC = {
 (1, 11): ('{x / x es par y 0 < x < 10} está determinado por', ['comprensión', 'extensión']),
 (2, 12): ('un conjunto de 4 elementos tiene', ['8 subconjuntos', '32 subconjuntos', '16 subconjuntos']),
 (3, 11): ('dos óvalos que se cruzan dividen al universo en', ['2 regiones', '4 regiones', '3 regiones']),
 (4, 11): ('la propiedad A∪B = B∪A se llama', ['idempotente', 'asociativa', 'conmutativa']),
 (5, 12): ('en un problema de Venn conviene completar primero', ['solo A', 'la intersección', 'ni A ni B']),
 (6, 12): ('«x es un número par» es una proposición', ['abierta', 'molecular', 'atómica']),
 (7, 12): ('el único caso en que p→q es F es cuando', ['p = V, q = V', 'p = V, q = F', 'p = F, q = V']),
 (8, 12): ('al evaluar una fórmula, lo primero que se resuelve es', ['los paréntesis y las negaciones', 'el conectivo principal']),
 (9, 12): ('si la columna final es F, F, F, F, la fórmula es', ['tautología', 'indeterminación', 'contradicción']),
 (10, 12): ('de p∧q se concluye q por', ['simplificación', 'adjunción', 'De Morgan']),
 (11, 12): ('para demostrar que ∃x: p(x) es verdadera alcanza con', ['revisar todos los elementos', 'exhibir un ejemplo que cumpla', 'hallar un contraejemplo']),
 (12, 12): ('de «si llueve, la clase es virtual» y «llueve» se concluye «la clase es virtual» por', ['MTT', 'MTP', 'MPP']),
 (13, 12): ('«calcular el promedio de las ventas de la semana» es un algoritmo', ['cualitativo', 'cuantitativo']),
 (14, 12): ('los cálculos en el diagrama de flujo se representan con', ['un óvalo', 'un rombo', 'un rectángulo']),
 (15, 12): ('2 + 3 * 4 vale', ['14', '24', '20']),
 (16, 12): ('después de x ← 5 y luego x ← x + 2, la variable x vale', ['10', '5', '7']),
 (17, 12): ('una decisión simple requiere como mínimo', ['dos pruebas (camino V y camino F)', 'cuatro pruebas de escritorio', 'una prueba']),
 (18, 12): ('negar (hayStock Y pagoAprobado) equivale a', ['¬hayStock Y ¬pagoAprobado', '¬hayStock O ¬pagoAprobado']),
 (19, 12): ('si un contador dentro de un Mientras nunca se incrementa, el ciclo', ['no termina nunca', 'termina enseguida']),
 (20, 12): ('el promedio se calcula', ['dentro del ciclo, en cada vuelta', 'después del ciclo, una sola vez']),
 (21, 12): ('una venta de exactamente G. 50.000 se cobra', ['50.000', '55.000', '45.000']),
}

# respuestas de la base que se ajustan sin cambiar el enunciado
RESP = {
 (9, 1): '8 filas. Orden estándar: p, cuatro V y después cuatro F; q, dos V y dos F, repetido dos veces; r, una V y una F, alternadas.',
 (3, 13): 'A∩B = {3, 4} ; A∪B = {1,2,3,4,5,6}. Regiones: solo A {1,2} = 2, central {3,4} = 2, solo B {5,6} = 2, fuera {7,8} = 2. Suma: 2 + 2 + 2 + 2 = 8 = n(U).',
}


def _fam(f):
    for k, v in FAM.items():
        if f.startswith(k):
            return v
    raise ValueError(f)


A = {}
for n in range(1, 22):
    lst = []
    for fam, k, enun, resp in BASE[str(n)]:
        nuevo = False
        if (n, k) in R:
            enun, resp = R[n, k]; nuevo = True
        if (n, k) in RESP:
            resp = RESP[n, k]; nuevo = True
        if (n, k) in OPC:
            tallo, ops = OPC[n, k]
            enun = 'Elegí y justificá: %s %s.' % (tallo, '; '.join('%s) %s' % ('abc'[i], o) for i, o in enumerate(ops))); nuevo = True
        lst.append((_fam(fam), k, enun, resp, nuevo))
    A[n] = lst


def items(n):
    """Lista plana [(familia, número, enunciado, respuesta, nuevo)]."""
    return A[n]


# Código: comparación o asignación con un número con punto de miles, o texto entre «» después de Escribir/=
CODIGO_MAL = re.compile(r'(?:[<>]=?|<>|←)\s*\d{1,3}\.\d{3}\b|\d{1,3}\.\d{3}\s*(?:[<>]=?|<>)|(?:Escribir|[a-zA-Z] =)\s*«')

if __name__ == '__main__':
    tot = 0
    for n in A:
        it = items(n)
        assert len(it) == 13, n
        for fam, k, e, r, nv in it:
            if e.startswith('Elegí y justificá'):
                assert (n, k) in OPC and re.match(r'^[a-c]\)', r), (n, k)
        for fam, k, e, r, nv in it:
            assert not re.search('[✓✗✅✔≈]', e + r), (n, k)
            if n >= 14:
                assert not CODIGO_MAL.search(e + ' ' + r), (n, k, CODIGO_MAL.search(e + ' ' + r).group())
        tot += sum(1 for x in it if x[4])
    print('ítems', sum(len(A[n]) for n in A), 'nuevos o modificados', tot)

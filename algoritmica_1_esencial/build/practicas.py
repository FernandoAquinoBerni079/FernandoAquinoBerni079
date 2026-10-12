# -*- coding: utf-8 -*-
"""Las 21 prácticas de la Edición Esencial de Algorítmica 1.º, tomadas del Cuaderno de Prácticas original y corregidas:
- los puntos de control ya no revelan resultados: piden un control cruzado o contrastar con lo anticipado;
- los datos que repetían un ejemplo de la clase se cambiaron (P7, P8, P10 y P18);
- el código usa números sin separador de miles y comillas rectas;
- P3 y P14 remiten a las Figuras 3.1 y 14.1 de la clase en lugar de repetir la imagen.
Los algoritmos de las prácticas 14 a 21 se tradujeron a PSeInt 20250314 (perfil Flexible) y se ejecutaron con los
datos de cada actividad (algoritmica_1_esencial/pseint/pr/). 'sol' alimenta el Solucionario."""

PAPEL = 'papel y lápiz'
VER = ' (Algoritmo comprobado en PSeInt 20250314, perfil Flexible.)'


def E(*lineas):
    """Pseudocódigo: cada línea se compone en monoespaciado."""
    return ['§' + x for x in lineas]


PR = {}

# =============================================================== UNIDAD 1 — TEORÍA DE CONJUNTOS
PR[1] = dict(
 titulo='Escribir conjuntos con precisión', entorno=PAPEL,
 competencia='Determinar conjuntos por extensión y por comprensión, usar la notación de pertenencia y calcular cardinales.',
 saber=['Un conjunto se escribe entre llaves, con cada elemento una sola vez y sin que importe el orden. x ∈ A significa que x es elemento de A; x ∉ A, que no lo es.',
        'Por extensión se listan todos los elementos; por comprensión se escribe {x / x cumple la propiedad}. El cardinal n(A) es la cantidad de elementos.'],
 antes='Trabajá en tu carpeta, con letras mayúsculas para los conjuntos y minúsculas para los elementos.',
 acts=[
  dict(titulo='Del mostrador a las llaves', objetivo='Escribir por extensión conjuntos tomados de una situación real.',
       modelo=('Menú del martes en el Copetín Karumbé', ["Hoy Ña Rosa ofrece: tortilla, croqueta, chipa so'o y jugo. Además acepta tres medios de pago: efectivo, QR y tarjeta."]),
       pasos=['Escribí por extensión el conjunto T de los productos del martes.', 'Escribí por extensión el conjunto P de los medios de pago.', 'Calculá n(T) y n(P).', 'Escribí dos afirmaciones verdaderas: una con ∈ y una con ∉ (por ejemplo, sobre la empanada, que hoy no está en el menú).'],
       control='Cada producto y cada medio de pago aparece una sola vez entre llaves, y tus cardinales coinciden con un segundo conteo hecho directamente sobre el menú.'),
  dict(titulo='De la propiedad a la lista', objetivo='Traducir conjuntos dados por comprensión a su forma por extensión.',
       modelo=None,
       pasos=['Escribí por extensión: A = {x / x es día del fin de semana}.', 'Escribí por extensión: B = {x / x es impar y 1 ≤ x ≤ 9}.', 'Escribí por extensión: C = {x / x es vocal de la palabra «tereré»}.', 'Calculá n(A), n(B) y n(C). Recordá: en un conjunto, los elementos no se repiten.'],
       control='Cada elemento que escribiste cumple la propiedad, no falta ninguno que la cumpla y en C ninguna letra aparece dos veces.'),
  dict(titulo='De la lista a la propiedad', objetivo='Escribir por comprensión conjuntos dados por extensión.',
       modelo=None,
       pasos=['Escribí por comprensión: D = {enero, febrero, marzo, ..., diciembre}.', 'Escribí por comprensión: E = {2, 4, 6, 8, 10}.', 'Compará con tu pareja de banco: ¿escribieron la misma propiedad? ¿Las dos describen exactamente los mismos elementos y ninguno más?'],
       control='Al leer tu propiedad, tu pareja reconstruye la lista exacta: ni un elemento de más, ni uno de menos.'),
 ],
 desafio='Escribí por extensión el conjunto K de las letras distintas de la palabra «Karumbé» y calculá n(K). Después inventá una palabra cuyo conjunto de letras tenga cardinal 4.',
 sol=dict(resultado="Act. 1: T = {tortilla, croqueta, chipa so'o, jugo}, n(T) = 4; P = {efectivo, QR, tarjeta}, n(P) = 3; por ejemplo, tortilla ∈ T y empanada ∉ T. Act. 2: A = {sábado, domingo}, n(A) = 2; B = {1, 3, 5, 7, 9}, n(B) = 5; C = {e}, n(C) = 1 (la e aparece tres veces en la palabra, pero se escribe una sola vez). Act. 3: D = {x / x es mes del año}; E = {x / x es número par y 2 ≤ x ≤ 10} (también es válida «x es par y 1 ≤ x ≤ 10»; no lo es «x es par», que agrega elementos). Desafío: K = {k, a, r, u, m, b, é}, n(K) = 7; una palabra con cardinal 4: «mesa» (m, e, s, a) o «sopa».",
          errores='Repetir elementos (escribir la e tres veces en C); usar paréntesis o corchetes en lugar de llaves; escribir propiedades demasiado amplias («x es número»); confundir ∈ con ⊂.'))

PR[2] = dict(
 titulo='Clasificar conjuntos y generar subconjuntos', entorno=PAPEL,
 competencia='Clasificar conjuntos en finitos, infinitos, unitarios o vacíos, y generar todos los subconjuntos de un conjunto pequeño.',
 saber=['Finito: se termina de contar. Infinito: no se termina. Unitario: un solo elemento. Vacío (∅): ninguno. Universal (U): el conjunto de referencia.',
        'A ⊆ B cuando todo elemento de A está en B. Un conjunto de n elementos tiene 2ⁿ subconjuntos, contando ∅ y el conjunto entero.'],
 antes='Para cada clasificación, la justificación es lo que se evalúa: una palabra sola no alcanza.',
 acts=[
  dict(titulo='Clasificar sin dudar', objetivo='Asignar a cada conjunto su tipo con una justificación.',
       modelo=None,
       pasos=['Clasificá (finito, infinito, unitario o vacío) y justificá en una línea: a) los números naturales mayores que 100; b) las capitales del Paraguay; c) los productos del menú que cuestan G. 0; d) las letras del achegety; e) los clientes que pagaron hoy con un cheque fechado en 1811.', 'Escribí el cardinal de cada conjunto que lo tenga.'],
       control='Cada tipo está justificado con la cantidad de elementos (o con la imposibilidad de terminar de contarlos), y los conjuntos sin elementos están escritos con ∅, no con {∅}.'),
  dict(titulo='La fábrica de subconjuntos', objetivo='Generar en forma ordenada los 2ⁿ subconjuntos de un conjunto.',
       modelo=('Método ordenado', ['Para no olvidar ninguno: primero ∅, después los de 1 elemento, después los de 2, y así hasta el conjunto entero.']),
       pasos=['Escribí todos los subconjuntos de B = {jugo, agua}.', "Escribí todos los subconjuntos de F = {tortilla, croqueta, chipa so'o}, agrupados por cantidad de elementos (0, 1, 2, 3).", 'Contá cuántos obtuviste en cada caso y verificá con la fórmula 2ⁿ.', 'Subrayá, en cada caso, los dos subconjuntos impropios.'],
       control='La cantidad de subconjuntos coincide con 2ⁿ en los dos casos, y en F el grupo de 0 elementos tiene tantos subconjuntos como el de 3, y el de 1 tantos como el de 2.'),
  dict(titulo='¿Pertenece o está incluido?', objetivo='Distinguir ∈ (elemento) de ⊆ (conjunto).',
       modelo=None,
       pasos=["Con M = {tortilla, croqueta, chipa so'o, jugo} y F = {tortilla, croqueta}, marcá V o F: a) tortilla ∈ M ; b) F ∈ M ; c) F ⊆ M ; d) jugo ⊆ M ; e) ∅ ⊆ F ; f) F ⊂ F.", 'Corregí por escrito las falsas, cambiando el símbolo por el correcto.'],
       control='En cada afirmación corregida, ∈ une un elemento con un conjunto y ⊆ o ⊂ unen un conjunto con otro conjunto.'),
 ],
 desafio='Ña Rosa quiere armar combos con productos distintos elegidos de una lista de 4. ¿Cuántos combos posibles hay (incluyendo el combo vacío y el de los 4 productos)? ¿Y si suma un quinto producto? Escribí la cuenta, no la lista.',
 sol=dict(resultado='Act. 1: a) infinito (los naturales no se terminan de contar); b) unitario, {Asunción}, cardinal 1; c) vacío, ∅, cardinal 0; d) finito, 33 letras; e) vacío, ∅ (en 1811 no existía el copetín ni ese medio de pago), cardinal 0. Act. 2: B: ∅, {jugo}, {agua}, {jugo, agua}: 2² = 4. F: ∅ · {tortilla}, {croqueta}, {chipa so\'o} · {tortilla, croqueta}, {tortilla, chipa so\'o}, {croqueta, chipa so\'o} · F: 1 + 3 + 3 + 1 = 8 = 2³. Impropios: ∅ y el conjunto entero. Act. 3: a) V; b) F → F ⊆ M; c) V; d) F → jugo ∈ M (o {jugo} ⊆ M); e) V; f) F → F ⊆ F (un conjunto no es subconjunto propio de sí mismo). Desafío: 2⁴ = 16 combos; con un quinto producto, 2⁵ = 32 (se duplican).',
          errores='Escribir {∅} para el vacío (es un unitario); olvidar ∅ o el conjunto entero en la lista de subconjuntos; usar ∈ entre dos conjuntos; creer que F ⊂ F es verdadero.'))

PR[3] = dict(
 titulo='Dibujar y leer diagramas de Venn', entorno=PAPEL,
 competencia='Representar conjuntos con diagramas de Venn y traducir entre el gráfico y el lenguaje simbólico.',
 saber=['El rectángulo es U; cada óvalo, un conjunto. Dos óvalos cruzados generan cuatro regiones: solo A, A y B, solo B, ni A ni B.',
        'Cada elemento del universo se ubica en exactamente una región; por eso los cardinales de las regiones suman n(U).'],
 antes='Tené a la vista la Figura 3.1 de la clase: así tiene que quedar tu diagrama terminado, con cada elemento en su región y ninguna región olvidada.',
 acts=[
  dict(titulo='Ubicar cada elemento en su región', objetivo='Distribuir un universo completo en las cuatro regiones.',
       modelo=('Datos', ['U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} · A = {2, 4, 6, 8, 10} (pares) · B = {3, 4, 8, 9}.']),
       pasos=['Dibujá el rectángulo U con los óvalos A y B cruzados.', 'Ubicá primero los elementos de A ∩ B en la zona central.', 'Completá «solo A», «solo B» y «ni A ni B».', 'Contá los elementos de cada región y sumá los cuatro cardinales.'],
       control='Cada número del 1 al 10 aparece una sola vez en el diagrama y la suma de los cardinales de las cuatro regiones es igual a n(U).'),
  dict(titulo='Del diagrama al símbolo', objetivo='Leer las relaciones de un diagrama dado.',
       modelo=('Situación', ['En un diagrama, el óvalo F (fritos) está dibujado completamente adentro del óvalo M (menú), y el óvalo B (bebidas) está separado de F, dentro de M.']),
       pasos=['Escribí con símbolos la relación entre F y M, y entre B y M.', 'Escribí con símbolos la relación entre F y B (pensá en su intersección).', 'Redactá en una oración qué significa el dibujo en el mostrador del copetín.'],
       control='Cada relación que escribiste se comprueba mirando el dibujo: un óvalo dentro de otro indica inclusión; dos óvalos que no se tocan, intersección vacía.'),
  dict(titulo='Del enunciado al diagrama', objetivo='Elegir el dibujo correcto para cada relación.',
       modelo=None,
       pasos=['Dibujá el diagrama que corresponde a cada caso: a) A ⊂ B ; b) A ∩ B = ∅ ; c) A y B con elementos comunes y propios cada uno.', 'Rotulá cada dibujo con su caso y sombreá en a) y en b) la región que queda sin elementos.'],
       control='Los tres dibujos son distintos entre sí y cada uno cumple la relación de su caso; si dos se parecen, releé el enunciado.'),
 ],
 desafio='Inventá un universo de 8 elementos del copetín y dos conjuntos A y B tales que «solo A» tenga 3 elementos, la intersección 1, «solo B» 2 y «ni A ni B» 2. Verificá que las regiones sumen n(U).',
 sol=dict(resultado='Act. 1: A ∩ B = {4, 8}; solo A = {2, 6, 10}; solo B = {3, 9}; ni A ni B = {1, 5, 7}; 2 + 3 + 2 + 3 = 10 = n(U). Act. 2: F ⊂ M y B ⊂ M; F ∩ B = ∅. En palabras: los fritos y las bebidas forman parte del menú, y ningún frito es bebida. Act. 3: a) óvalo A dentro del óvalo B (la región «solo A» queda vacía); b) óvalos separados (la región común no existe o queda vacía); c) óvalos cruzados con las cuatro regiones. Desafío: respuesta abierta; se controla que 3 + 1 + 2 + 2 = 8.',
          errores='Escribir los elementos de A ∩ B dos veces (en «solo A» y en el centro); olvidar la región «ni A ni B»; usar ∈ para relacionar dos conjuntos; dibujar óvalos cruzados para A ⊂ B.'))

PR[4] = dict(
 titulo='Unir e intersecar conjuntos', entorno=PAPEL,
 competencia='Calcular uniones e intersecciones y verificar sus propiedades con ejemplos concretos.',
 saber=['A ∪ B junta todo (los repetidos, una sola vez). A ∩ B guarda solo lo común. Si A ∩ B = ∅, los conjuntos son disjuntos.',
        'Vale n(A ∪ B) = n(A) + n(B) − n(A ∩ B): al sumar cardinales, lo común se contó dos veces y hay que restarlo una.'],
 antes='Escribí cada resultado entre llaves y, al lado, su cardinal.',
 acts=[
  dict(titulo='Los pedidos del miércoles', objetivo='Calcular unión e intersección sobre datos reales.',
       modelo=('Datos', ["Pedidos del turno mañana: A = {empanada, jugo, chipa so'o, coquito}. Pedidos del turno siesta: B = {jugo, tortilla, coquito}."]),
       pasos=['Calculá A ∪ B (todo lo pedido en el día).', 'Calculá A ∩ B (lo pedido en los dos turnos).', 'Calculá n(A), n(B), n(A ∩ B) y n(A ∪ B).', 'Verificá la fórmula: n(A ∪ B) = n(A) + n(B) − n(A ∩ B).'],
       control='La fórmula cierra con tus cardinales: el número de la izquierda coincide con la cuenta de la derecha. Si no cierra, buscá un elemento repetido en la unión.'),
  dict(titulo='Con números', objetivo='Operar con conjuntos numéricos y detectar conjuntos disjuntos.',
       modelo=None,
       pasos=['Con P = {1, 3, 5, 7}, Q = {5, 7, 9} y R = {2, 4}: calculá P ∪ Q, P ∩ Q, P ∩ R y Q ∪ R.', 'Revisá los tres pares (P y Q, P y R, Q y R) e indicá cuáles son disjuntos y por qué.', 'Calculá (P ∩ Q) ∪ R y P ∩ (Q ∪ R): ¿dan lo mismo?'],
       control='Cada par que declaraste disjunto tiene intersección vacía, y tu respuesta al paso 3 se apoya en un elemento concreto que está en un resultado y no en el otro (o en que coinciden todos).'),
  dict(titulo='Propiedades a prueba', objetivo='Verificar las propiedades conmutativa e idempotente y las reglas con ∅ y U.',
       modelo=None,
       pasos=['Con A y B de la Actividad 1, escribí B ∪ A y compará con A ∪ B.', 'Calculá A ∪ A y A ∩ A. ¿Qué propiedad verificaste?', 'Con U = {todos los productos y bebidas del día}, escribí sin calcular: A ∪ ∅, A ∩ ∅, A ∩ U.'],
       control='Cada resultado que escribiste sin calcular coincide con el que obtenés al calcularlo elemento por elemento.'),
 ],
 desafio='Buscá dos conjuntos A y B tales que A ∪ B = A. ¿Qué relación hay entre ellos? Escribila con el símbolo correcto y explicá por qué siempre pasa.',
 sol=dict(resultado="Act. 1: A ∪ B = {empanada, jugo, chipa so'o, coquito, tortilla}; A ∩ B = {jugo, coquito}; n(A) = 4, n(B) = 3, n(A ∩ B) = 2, n(A ∪ B) = 5 = 4 + 3 − 2. Act. 2: P ∪ Q = {1, 3, 5, 7, 9}; P ∩ Q = {5, 7}; P ∩ R = ∅; Q ∪ R = {2, 4, 5, 7, 9}. Disjuntos: P y R, y también Q y R (Q ∩ R = ∅); P y Q no (comparten 5 y 7). (P ∩ Q) ∪ R = {2, 4, 5, 7} y P ∩ (Q ∪ R) = {5, 7}: no dan lo mismo (el 2 y el 4 están solo en el primero). Act. 3: B ∪ A = A ∪ B (conmutativa); A ∪ A = A ∩ A = A (idempotente); A ∪ ∅ = A, A ∩ ∅ = ∅, A ∩ U = A. Desafío: ocurre cuando B ⊆ A: todo lo que aporta B ya está en A.",
          errores='Escribir los repetidos dos veces en la unión (n(A ∪ B) = 7); confundir ∪ con ∩; declarar disjunto solo un par; responder el desafío con un ejemplo sin nombrar la relación de inclusión.'))

PR[5] = dict(
 titulo='Diferencia, complemento y problemas de conteo', entorno=PAPEL,
 competencia='Calcular diferencias y complementos, y resolver problemas de conteo con el diagrama de Venn y el control del universo.',
 saber=['A − B: lo de A que no está en B (no es conmutativa). A′ = U − A: todo lo del universo fuera de A. De Morgan: (A ∪ B)′ = A′ ∩ B′ y (A ∩ B)′ = A′ ∪ B′.',
        'Método de conteo: 1.º la intersección en el centro; 2.º «solo A» y «solo B» restando; 3.º «ninguno» para completar n(U). Verificá siempre la suma.'],
 antes='En los problemas de conteo, dibujá siempre el diagrama antes de calcular.',
 acts=[
  dict(titulo='Restar y complementar', objetivo='Calcular diferencias y complementos con precisión.',
       modelo=('Datos', ['U = {1, 2, 3, 4, 5, 6, 7, 8} · A = {1, 2, 3, 6} · B = {2, 3, 5, 7}.']),
       pasos=['Calculá A − B y B − A. ¿Dieron lo mismo?', 'Calculá A′ y B′.', 'Calculá (A ∪ B)′ y A′ ∩ B′, y compará los resultados.', 'Escribí en una línea qué ley acabás de verificar.'],
       control='Comprobaste cada complemento contando: n(A) + n(A′) = n(U), y lo mismo con B. Tu conclusión del paso 4 nombra la ley y la escribe con símbolos.'),
  dict(titulo='La encuesta del tereré', objetivo='Resolver un problema completo de dos conjuntos.',
       modelo=('Situación', ['Ña Rosa preguntó a 45 clientes: 28 toman tereré, 21 toman cocido y 12 toman ambos.']),
       pasos=['Dibujá el diagrama y anotá 12 en la intersección.', 'Calculá «solo tereré» y «solo cocido» restando.', 'Calculá cuántos toman al menos una de las dos bebidas.', 'Calculá cuántos no toman ninguna y verificá el control del universo.'],
       control='Las cuatro regiones de tu diagrama suman el total de encuestados. Si no, revisá las restas del paso 2.'),
  dict(titulo='Leer al revés', objetivo='Reconstruir los datos a partir de las regiones.',
       modelo=('Situación', ['En otra encuesta, el diagrama terminado muestra: solo chipa 15, ambos 9, solo empanada 8, ninguno 6.']),
       pasos=['Calculá cuántos clientes fueron encuestados en total.', 'Calculá cuántos compran chipa (en total) y cuántos compran empanada (en total).', 'Explicá por qué «compran chipa» no es lo mismo que «solo chipa».'],
       control='Comprobaste tus totales por un segundo camino: compran chipa + compran empanada − ambos + ninguno da el total de encuestados.'),
 ],
 desafio='De 50 estudiantes, 30 usan el laboratorio y 25 usan su celular para practicar; 5 no usan ninguno. ¿Cuántos usan ambos? (Pista: primero calculá cuántos usan al menos uno, después aplicá la fórmula de la unión.)',
 sol=dict(resultado='Act. 1: A − B = {1, 6}; B − A = {5, 7} (distintas: la diferencia no es conmutativa). A′ = {4, 5, 7, 8}; B′ = {1, 4, 6, 8}. A ∪ B = {1, 2, 3, 5, 6, 7}, (A ∪ B)′ = {4, 8}; A′ ∩ B′ = {4, 8}: ley de De Morgan, (A ∪ B)′ = A′ ∩ B′. Act. 2: solo tereré 28 − 12 = 16; solo cocido 21 − 12 = 9; al menos una 16 + 12 + 9 = 37; ninguna 45 − 37 = 8. Control: 16 + 12 + 9 + 8 = 45. Act. 3: total 15 + 9 + 8 + 6 = 38; compran chipa 15 + 9 = 24; compran empanada 8 + 9 = 17. Control: 24 + 17 − 9 + 6 = 38. «Compran chipa» incluye a los que compran las dos cosas; «solo chipa» los excluye. Desafío: al menos uno 50 − 5 = 45; ambos 30 + 25 − 45 = 10 (solo laboratorio 20, solo celular 15).',
          errores='Escribir 28 y 21 directamente en las regiones «solo» (no se restó la intersección); olvidar la región «ninguno»; restar la intersección dos veces; creer que A − B = B − A.'))

# =============================================================== UNIDAD 2 — LÓGICA SIMBÓLICA
PR[6] = dict(
 titulo='Cazar proposiciones', entorno=PAPEL,
 competencia='Distinguir proposiciones de otras expresiones y clasificarlas en abiertas, atómicas y moleculares.',
 saber=['Proposición: oración declarativa con un único valor de verdad (V o F). Preguntas, órdenes, exclamaciones y opiniones sin criterio no lo son.',
        'Abierta: contiene variable (sin valor hasta reemplazarla). Atómica: afirma una sola cosa. Molecular: combina atómicas con conectivos (la negación cuenta).'],
 antes='Justificá cada decisión con el criterio de la clase, no con la intuición.',
 acts=[
  dict(titulo='¿Es o no es?', objetivo='Decidir con criterio cuáles expresiones son proposiciones.',
       modelo=None,
       pasos=['Marcá P (proposición) o N (no lo es) y justificá en una línea: a) El río Paraguay atraviesa el país. b) ¡Salió la chipa del horno! c) 12 − 5 = 7. d) ¿Aceptan tarjeta? e) x − 4 = 9. f) La croqueta es lo más rico del mundo. g) Hoy no hay tortilla. h) Cerrá la heladera.', 'Contá cuántas P obtuviste y compará con tu pareja de banco.'],
       control='Cada N lleva su motivo (pregunta, orden, exclamación u opinión) y la expresión con variable quedó señalada aparte como abierta.'),
  dict(titulo='Atómica o molecular', objetivo='Clasificar proposiciones según tengan o no conectivos.',
       modelo=('Recordá', ['«y», «o», «si... entonces», «si y solo si» y el «no» son conectivos. «Pero» funciona como «y».']),
       pasos=['Clasificá en atómica (A) o molecular (M): a) Hay jugo. b) Hay jugo y hay agua. c) No hay croqueta. d) Si llueve, entonces hay más ventas de cocido. e) El copetín abre a las 6:00. f) O llevás tortilla o llevás empanada.', 'En las moleculares, subrayá el conectivo y escribí las atómicas que la componen.'],
       control='Cada molecular tiene un conectivo subrayado y al menos una atómica escrita aparte; cada atómica afirma una sola cosa sin conectivos.'),
  dict(titulo='Letras y valores', objetivo='Pasar del idioma a la notación p, q, r con valores de verdad.',
       modelo=None,
       pasos=['Asigná p, q y r a tres proposiciones atómicas sobre tu aula (dos verdaderas y una falsa) y anotá sus valores.', 'Escribí en palabras: ¬r, p ∧ q y q ∨ r, e indicá el valor de verdad de cada una según tus valores.', 'Intercambiá con tu pareja de banco y verificá los valores del otro.'],
       control='Tu pareja llegó a los mismos valores que vos usando las tablas de los conectivos.'),
 ],
 desafio='Escribí una oración que parezca proposición pero no lo sea, y otra que parezca simple pero sea molecular. Explicá la trampa de cada una.',
 sol=dict(resultado='Act. 1: proposiciones: a) (V), c) (V) y g) (su valor depende del día, pero es V o F). No lo son: b) exclamación, d) pregunta, f) opinión sin criterio, h) orden. e) es una expresión proposicional abierta: tendrá valor cuando x reciba un valor (con x = 13 es V). Act. 2: atómicas a) y e); moleculares b) (y: «hay jugo», «hay agua»), c) (negación de «hay croqueta»), d) (si... entonces: «llueve», «hay más ventas de cocido») y f) (o: «llevás tortilla», «llevás empanada»). Act. 3: depende de los valores elegidos; con p = V, q = V, r = F: ¬r = V, p ∧ q = V, q ∨ r = V. Desafío: abierta, por ejemplo «Ese producto cuesta 4.000» (sin decir cuál) o una opinión con forma declarativa; molecular disimulada: «No abrimos el domingo» (negación).',
          errores='Aceptar opiniones como proposiciones; marcar e) como proposición falsa; olvidar que la negación es conectivo; elegir valores y después no usarlos en las tablas.'))

PR[7] = dict(
 titulo='Simbolizar y evaluar con conectivos', entorno=PAPEL,
 competencia='Traducir reglas del lenguaje común a símbolos lógicos y calcular el valor de verdad de proposiciones compuestas.',
 saber=['¬ no · ∧ y · ∨ o (inclusiva) · ⊻ o exclusiva · → si... entonces · ↔ si y solo si. El condicional solo es F en el caso V → F.',
        'Para evaluar: reemplazá valores, resolvé paréntesis y negaciones primero, y el conectivo principal al final.'],
 antes='En las fórmulas con dos o más conectivos, usá paréntesis para que haya una sola lectura posible.',
 acts=[
  dict(titulo='Traducir reglas del copetín', objetivo='Simbolizar oraciones con letras, conectivos y paréntesis.',
       modelo=('Diccionario', ['p: hay leche · q: hay yerba · r: hay cocido · s: hace frío.']),
       pasos=['Simbolizá: a) Hay leche y hay yerba. b) No hay cocido. c) Si hace frío, entonces hay cocido. d) Si hace frío y hay yerba, entonces hay cocido. e) O hay leche o hay cocido (una sola cosa). f) Hay cocido si y solo si hace frío.', 'Marcá con un círculo el conectivo principal de d).'],
       control='Cada fórmula con más de un conectivo lleva paréntesis y, al leerla en voz alta con el diccionario, dice lo mismo que la oración.'),
  dict(titulo='Calcular paso a paso', objetivo='Evaluar compuestas con valores dados, de adentro hacia afuera.',
       modelo=('Valores del día', ['p = V · q = F · r = V · s = F.']),
       pasos=['Calculá mostrando cada paso: a) p ∧ q ; b) p ∨ q ; c) q → r ; d) ¬p ⊻ r.', 'Calculá: e) (p ∧ q) → r ; f) (p ∨ s) ↔ (q ∨ r) ; g) ¬(p ∧ r).', 'Rodeá los resultados F y explicá en una línea por qué dieron F.'],
       control='En cada fórmula escribiste el valor de cada parte antes del conectivo principal, y cada resultado F tiene su explicación.'),
  dict(titulo='El condicional bajo la lupa', objetivo='Dominar la fila V–F, la única que hace falso al condicional.',
       modelo=None,
       pasos=['Ña Rosa promete: «si comprás tres tortillas, te regalo un jugo». Escribí los cuatro escenarios posibles (comprás/no comprás × regala/no regala).', 'Indicá en cuál escenario la promesa se rompe y qué valores de p y q tiene.', 'Explicá por qué la promesa no se rompe cuando el cliente no compra las tres tortillas.'],
       control='Decidiste cada escenario con la tabla del condicional, y tu explicación del paso 3 habla de lo que Ña Rosa prometió y de lo que no prometió.'),
 ],
 desafio='Inventá una regla del copetín que se simbolice con tres letras y dos conectivos distintos, con paréntesis. Dale valores a las letras y calculá su valor de verdad.',
 sol=dict(resultado='Act. 1: a) p ∧ q; b) ¬r; c) s → r; d) (s ∧ q) → r (conectivo principal: →); e) p ⊻ r; f) r ↔ s. Act. 2: a) V ∧ F = F; b) V ∨ F = V; c) F → V = V; d) ¬p = F, F ⊻ V = V; e) p ∧ q = F, F → V = V; f) p ∨ s = V, q ∨ r = V, V ↔ V = V; g) p ∧ r = V, ¬V = F. Resultados F: a) (la conjunción exige las dos y q es F) y g) (se niega algo verdadero). Act. 3: p = «compra tres tortillas», q = «le regala un jugo»: V–V cumple (V); V–F rompe la promesa (F); F–V y F–F no la rompen (V): la promesa no dice nada de quien no compra. Desafío: respuesta abierta; se controla que los paréntesis indiquen el conectivo principal.',
          errores='Escribir s ∧ q → r sin paréntesis; usar ∨ en e) (era «una sola cosa»: ⊻); evaluar el conectivo principal antes que los paréntesis; creer que el condicional es F cuando el antecedente es F.'))

PR[8] = dict(
 titulo='Construir tablas de verdad (dos variables)', entorno=PAPEL,
 competencia='Construir tablas de verdad completas de fórmulas con dos variables, evaluando por columnas en el orden correcto.',
 saber=['Con 2 variables: 4 filas en orden estándar (p: V V F F · q: V F V F). Una columna por cada paso intermedio; el conectivo principal, al final.',
        'La columna final dice en qué combinaciones la fórmula es verdadera.'],
 antes='Dibujá las tablas con regla: una columna por cada parte de la fórmula.',
 acts=[
  dict(titulo='Armar el esqueleto', objetivo='Construir la tabla con filas y columnas bien ordenadas.',
       modelo=('Fórmula', ['p ∧ ¬q']),
       pasos=['Armá la tabla con columnas p, q, ¬q y p ∧ ¬q, y las 4 filas estándar.', 'Completá primero la columna ¬q, fila por fila.', 'Completá la columna final combinando p con ¬q mediante ∧.', 'Respondé: ¿en qué combinaciones la fórmula es V?'],
       control='Completaste ¬q antes de la columna final, y cada casillero de la columna final combina los valores de su propia fila.'),
  dict(titulo='Dos fórmulas, misma tabla', objetivo='Evaluar dos fórmulas en paralelo y compararlas.',
       modelo=('Fórmulas', ['¬(p ∨ q)  y  (p → q) ∧ p']),
       pasos=['Construí la tabla de ¬(p ∨ q) (columnas: p, q, p ∨ q, ¬(p ∨ q)).', 'Construí la tabla de (p → q) ∧ p (columnas: p, q, p → q, final).', 'Anotá cuántas V tiene cada columna final.', 'Escribí en una línea qué significan las V de cada fórmula.'],
       control='Cada columna intermedia está completa antes de la final, y revisaste la fila V–F del condicional, que es la que más se equivoca.'),
  dict(titulo='Leer la tabla como una regla', objetivo='Usar la columna final para responder preguntas del negocio.',
       modelo=('Situación', ['El sábado, el copetín abre si hay feria en el colegio o hay partido en la cancha (abre = f ∨ c).']),
       pasos=['Construí la tabla de f ∨ c.', 'Marcá las filas en las que el copetín abre.', 'Respondé: ¿en qué caso el copetín queda cerrado? Escribilo en palabras y con símbolos (usá De Morgan si te animás).'],
       control='Las filas marcadas son las que tienen V en la columna final, y tu respuesta en palabras describe la fila que quedó sin marcar.'),
 ],
 desafio='Construí la tabla de ¬p ↔ q y encontrá otra fórmula ya vista en el libro cuya columna final sea exactamente la opuesta.',
 sol=dict(resultado='Act. 1: ¬q: F V F V; p ∧ ¬q: F V F F: es V solo en la fila p = V, q = F. Act. 2: p ∨ q: V V V F, ¬(p ∨ q): F F F V (una V, fila F–F: no pasa ninguna de las dos); p → q: V F V V, (p → q) ∧ p: V F F F (una V, fila V–V: se cumplen p y q). Act. 3: f ∨ c: V V V F; abre en tres filas; queda cerrado solo si no hay feria y no hay partido: ¬f ∧ ¬c (De Morgan: ¬(f ∨ c) ≡ ¬f ∧ ¬c). Desafío: ¬p ↔ q da F V V F; la opuesta, V F F V, es la de p ↔ q (bicondicional).',
          errores='Cambiar el orden estándar de las filas; calcular la columna final sin las intermedias; dar V al condicional en la fila V–F; leer «sin promo / cerrado» como la fila con V.'))

PR[9] = dict(
 titulo='Tres variables y clasificación de fórmulas', entorno=PAPEL,
 competencia='Construir tablas de 8 filas y clasificar fórmulas en tautología, contradicción o indeterminación.',
 saber=['Con 3 variables: 8 filas (p de a cuatro, q de a dos, r de a una). Tautología: todas V. Contradicción: todas F. Indeterminación: mezcla.',
        'Una regla que es tautología no filtra nada; una que es contradicción nunca podrá cumplirse: las dos son señales de error de diseño.'],
 antes='Antes de completar, verificá que las 8 filas sean distintas entre sí.',
 acts=[
  dict(titulo='Las 8 filas sin perder ninguna', objetivo='Dominar el orden estándar con tres variables.',
       modelo=('Fórmula', ['p → (q ∨ r)']),
       pasos=['Escribí las 8 combinaciones en orden estándar.', 'Completá la columna q ∨ r.', 'Completá la columna final p → (q ∨ r).', 'Contá las F de la columna final y anotá en qué filas están.'],
       control='Las columnas p, q y r siguen el patrón de cuatro, dos y uno; ninguna fila se repite, y cada F de la columna final corresponde a un antecedente V con consecuente F.'),
  dict(titulo='Clasificar tres fórmulas', objetivo='Decidir la clase de cada fórmula con su tabla de 4 filas.',
       modelo=('Fórmulas', ['a) (p ∧ q) → q   b) p ↔ ¬p   c) p ⊻ q']),
       pasos=['Construí la tabla de cada fórmula.', 'Clasificá cada una: tautología, contradicción o indeterminación.', 'Si alguna es contradicción, explicá en una línea por qué nunca puede ser V.'],
       control='Cada clasificación se apoya en la columna final completa (todas V, todas F o mezcla), no en una sola fila.'),
  dict(titulo='Detectar reglas rotas', objetivo='Usar la clasificación para revisar reglas de negocio.',
       modelo=('Situación', ['Un sistema mal configurado tiene dos reglas: R1: «el pedido es para llevar y no es para llevar» y R2: «el pedido es para llevar o no es para llevar».']),
       pasos=['Simbolizá R1 y R2 con la letra p.', 'Clasificá cada una con su tabla de 2 filas.', 'Escribí qué le dirías al que configuró el sistema sobre cada regla.'],
       control='Simbolizaste con una sola letra y tu mensaje al configurador explica qué pasa en la práctica con cada regla.'),
 ],
 desafio='Construí la tabla de 8 filas de (p ∧ q) ∧ r y respondé: ¿cuántas V tiene? ¿Qué tendría que pasar en el copetín para que una regla con tres condiciones en «y» se cumpla?',
 sol=dict(resultado='Act. 1: q ∨ r: V V V F V V V F; p → (q ∨ r): V V V F V V V V: una sola F, en la fila p = V, q = F, r = F (indeterminación). Act. 2: a) V V V V: tautología; b) p ↔ ¬p: F F: contradicción (p y ¬p nunca tienen el mismo valor); c) F V V F: indeterminación. Act. 3: R1 = p ∧ ¬p: contradicción, la regla no se activa nunca; R2 = p ∨ ¬p: tautología, se activa siempre y no filtra nada. Desafío: una sola V (fila V V V): las tres condiciones tienen que cumplirse a la vez.',
          errores='Repetir o saltear una fila; alternar r de a dos; clasificar mirando una sola fila; creer que una tautología es una «regla buena» porque siempre se cumple.'),
 transfer=dict(
  caso=('el sistema de pedidos por mensaje', ['p: «el pedido está pagado» · q: «el pedido tiene dirección».', 'R1: (p ∧ q) → p · R2: (p ∨ q) ∧ (¬p ∧ ¬q) · R3: p → (p ∧ q).']),
  pasos=['Construí la tabla de cada regla y clasificala.', 'Intercambiá las tablas con otro equipo: revisá fila por fila y marcá cualquier casillero en el que no estén de acuerdo.', 'Corregí tu versión con lo que te señalaron y escribí, para cada regla, si conviene dejarla en el sistema y por qué.'],
  control='Las dos versiones del equipo terminan con la misma columna final para cada regla, y la recomendación de cada regla se apoya en su clasificación.',
  sol='R1: V V V V, tautología (no filtra: siempre se activa). R2: p ∨ q = V V V F; ¬p ∧ ¬q = F F F V; R2 = F F F F, contradicción (no se activa nunca). R3: p ∧ q = V F F F; R3 = V F V V, indeterminación: es F solo cuando el pedido está pagado y no tiene dirección, la única regla útil (detecta los pedidos pagados sin dirección). Error típico en la revisión: dar V a R3 en la fila V–F.'))

PR[10] = dict(
 titulo='Aplicar equivalencias y leyes lógicas', entorno=PAPEL,
 competencia='Verificar equivalencias con tablas y negar proposiciones compuestas con las leyes de De Morgan.',
 saber=['Dos fórmulas son equivalentes (≡) si sus columnas finales coinciden. Doble negación: ¬(¬p) ≡ p.',
        'De Morgan: ¬(p ∧ q) ≡ ¬p ∨ ¬q y ¬(p ∨ q) ≡ ¬p ∧ ¬q. Adjunción: de p y q, p ∧ q. Simplificación: de p ∧ q, cada parte.'],
 antes='La Figura 10.1 de la clase muestra una equivalencia ya verificada; acá verificás otra con el mismo método.',
 acts=[
  dict(titulo='Verificar con tablas', objetivo='Demostrar una equivalencia comparando columnas.',
       modelo=('Equivalencia a verificar (contrarrecíproco)', ['p → q ≡ ¬q → ¬p']),
       pasos=['Construí la tabla de p → q.', 'Construí, al lado, la tabla de ¬q → ¬p, con las columnas ¬q y ¬p.', 'Compará las columnas finales fila por fila.', 'Escribí la conclusión con el símbolo ≡, o explicá por qué no se puede escribir.'],
       control='Comparaste las cuatro filas una por una y escribiste ≡ solo si coinciden todas.'),
  dict(titulo='Negar carteles sin equivocarse', objetivo='Aplicar De Morgan a frases del negocio.',
       modelo=None,
       pasos=['Negá correctamente (símbolos y palabras): a) «hay tortilla y hay jugo»; b) «acepto QR o acepto tarjeta»; c) «no hay croqueta» (doble negación).', 'Para a) y b), escribí también la negación incorrecta típica y explicá por qué está mal.'],
       control='Comprobaste cada negación con un caso concreto: cuando la frase original es verdadera, tu negación es falsa, y al revés.'),
  dict(titulo='Deducciones mínimas', objetivo='Usar adjunción y simplificación citando la regla.',
       modelo=('Premisas del día', ['1) Hay leche. 2) Hay azúcar. 3) Hay yerba y hay agua caliente.']),
       pasos=['A partir de 1) y 2), obtené una conjunción nueva e indicá la regla.', 'A partir de 3), obtené «hay agua caliente» e indicá la regla.', 'Combiná lo obtenido para afirmar «hay leche, hay azúcar y hay agua caliente», citando cada paso.'],
       control='Cada paso nuevo cita una sola regla y usa únicamente premisas o pasos anteriores.'),
 ],
 desafio='El sistema de pedidos por mensaje avisa «pedido incompleto» cuando NO se cumple «tiene dirección y tiene teléfono». Escribí la condición del aviso aplicando De Morgan y decidí: ¿se avisa en un pedido con dirección pero sin teléfono?',
 sol=dict(resultado='Act. 1: p → q: V F V V; ¬q: F V F V; ¬p: F F V V; ¬q → ¬p: V F V V. Coinciden las cuatro filas: p → q ≡ ¬q → ¬p. Act. 2: a) ¬(t ∧ j) ≡ ¬t ∨ ¬j: «no hay tortilla o no hay jugo» (incorrecta típica: «no hay tortilla y no hay jugo», que solo cubre el caso en que faltan las dos); b) ¬(q ∨ t) ≡ ¬q ∧ ¬t: «no acepto QR y no acepto tarjeta» (incorrecta: «no acepto QR o no acepto tarjeta», que sigue siendo verdadera si acepto uno de los dos); c) ¬(¬c) ≡ c: «hay croqueta». Act. 3: 4) hay leche y hay azúcar (adjunción, 1 y 2); 5) hay agua caliente (simplificación, 3); 6) hay leche, hay azúcar y hay agua caliente (adjunción, 4 y 5). Desafío: aviso = ¬(d ∧ t) ≡ ¬d ∨ ¬t; con dirección y sin teléfono, ¬t es V, así que se avisa (basta que falte uno de los dos datos).',
          errores='Negar cada parte sin cambiar el conectivo; olvidar las columnas ¬q y ¬p; escribir ≡ con una fila distinta; citar «De Morgan» en la adjunción.'))

PR[11] = dict(
 titulo='Cuantificar y buscar contraejemplos', entorno=PAPEL,
 competencia='Evaluar y negar proposiciones con cuantificadores sobre conjuntos concretos.',
 saber=['∀x: p(x) es V si todos los elementos cumplen; un contraejemplo la vuelve F. ∃x: p(x) es V si al menos uno cumple; un ejemplo alcanza para probarla.',
        'Negaciones: ¬(∀x: p(x)) ≡ ∃x: ¬p(x) y ¬(∃x: p(x)) ≡ ∀x: ¬p(x).'],
 antes='Un contraejemplo tiene nombre y apellido: el elemento exacto que derriba la afirmación.',
 acts=[
  dict(titulo='Veredicto sobre D', objetivo='Decidir el valor de proposiciones cuantificadas con justificación.',
       modelo=('Conjunto de referencia', ['D = {1, 2, 3, 4, 5, 6}.']),
       pasos=['Determiná V o F y justificá con ejemplo o contraejemplo: a) ∀x: x < 7 ; b) ∃x: x > 5 ; c) ∀x: x es par ; d) ∃x: x² = 10 ; e) ∀x: x + x = 2x.', 'Para cada F, escribí el contraejemplo con el número exacto que la derriba o, si es un ∃, mostrá que revisaste todos los elementos.'],
       control='Cada V con ∃ tiene un ejemplo, cada F con ∀ tiene un contraejemplo concreto, y en las F con ∃ revisaste los seis elementos de D.'),
  dict(titulo='Con los precios del día', objetivo='Cuantificar sobre una lista de precios.',
       modelo=('Precios del día', ["tortilla G. 3.000 · croqueta G. 2.500 · chipa so'o G. 5.000 · jugo G. 4.000."]),
       pasos=['Evaluá: a) ∀x: «x cuesta menos de G. 6.000» ; b) ∃x: «x cuesta G. 2.500» ; c) ∀x: «x cuesta más de G. 2.500» ; d) ∃x: «x cuesta G. 10.000».', 'Justificá cada respuesta con el producto que sirve de ejemplo o contraejemplo.'],
       control='Cada respuesta nombra el producto que la justifica, y revisaste con cuidado los precios iguales al límite: «más de» no es lo mismo que «al menos».'),
  dict(titulo='Negar cuantificadores', objetivo='Intercambiar ∀ y ∃ al negar.',
       modelo=None,
       pasos=['Negá en símbolos y en palabras: a) «todos los pedidos salieron a tiempo»; b) «existe un producto agotado»; c) «todos los clientes pagaron».', 'Para a), explicá cuántos pedidos atrasados bastan para que la negación sea verdadera.'],
       control='Cada negación cambió el cuantificador y negó la propiedad; al leerla en voz alta, contradice a la original.'),
 ],
 desafio='Escribí una proposición con ∀ sobre tu sección que sea falsa, y convertila en verdadera cambiando solamente el cuantificador. ¿Siempre se puede hacer ese arreglo? Pensá un caso donde ni ∀ ni ∃ la salven.',
 sol=dict(resultado="Act. 1: a) V (los seis son menores que 7); b) V (ejemplo: 6); c) F (contraejemplo: 1, o cualquier impar de D); d) F (los cuadrados de D son 1, 4, 9, 16, 25, 36: ninguno es 10); e) V (vale para todo número). Act. 2: a) V (el más caro, la chipa so'o, cuesta 5.000); b) V (la croqueta); c) F (contraejemplo: la croqueta cuesta exactamente 2.500, no más); d) F (ningún producto cuesta 10.000). Act. 3: a) ∃x: x no salió a tiempo, «algún pedido salió atrasado»; b) ∀x: x no está agotado, «ningún producto está agotado»; c) ∃x: x no pagó, «algún cliente no pagó». Para a) basta un solo pedido atrasado. Desafío: no siempre: si ningún elemento cumple la propiedad, ∃ también es F (por ejemplo, «todos tienen 30 años»).",
          errores='Negar «todos» con «ninguno»; probar un ∀ con un ejemplo; contestar c) como V por no distinguir «más de» de «al menos»; revisar solo algunos elementos en d).'))

PR[12] = dict(
 titulo='Deducir con reglas de inferencia', entorno=PAPEL,
 competencia='Identificar y aplicar MPP, MTT, MTP y los silogismos en razonamientos simbolizados.',
 saber=['MPP: p → q, p ⊢ q. MTT: p → q, ¬q ⊢ ¬p. MTP: p ∨ q, ¬p ⊢ q. Silogismo hipotético: p → q, q → r ⊢ p → r.',
        'Falacia de afirmación del consecuente: de p → q y q NO se concluye p. Detectarla vale tanto como aplicar bien las reglas.'],
 antes='Simbolizá siempre antes de nombrar la regla: la forma de las premisas decide cuál corresponde.',
 acts=[
  dict(titulo='Nombrar la regla', objetivo='Reconocer qué regla sostiene cada razonamiento.',
       modelo=None,
       pasos=["Simbolizá y nombrá la regla: a) «Si hay masa, hay tortilla. Hay masa. Luego, hay tortilla.» b) «Si el horno anda, hay chipa so'o. No hay chipa so'o. Luego, el horno no anda.» c) «El pedido es para llevar o para la mesa. No es para la mesa. Luego, es para llevar.» d) «Si llueve, hay más cocido; si hay más cocido, falta azúcar. Luego, si llueve, falta azúcar.»", 'Subrayá en cada caso la premisa que «dispara» la conclusión.'],
       control='Cada razonamiento está simbolizado antes de nombrar la regla, y la regla elegida tiene la misma forma que tus premisas.'),
  dict(titulo='Completar la conclusión', objetivo='Producir la conclusión válida a partir de premisas dadas.',
       modelo=('Premisas', ['1) Si el cliente tiene vaso propio, hay descuento (v → d). 2) v. 3) d → s (si hay descuento, sonríe). 4) t ∨ m ; ¬t.']),
       pasos=['De 1) y 2), concluí e indicá la regla.', 'Con lo obtenido y 3), concluí de nuevo e indicá la regla.', 'De 4), concluí e indicá la regla.', 'Escribí la cadena completa en una línea: premisas ⊢ conclusiones.'],
       control='Cada conclusión usa solo premisas o conclusiones anteriores y lleva el nombre de su regla.'),
  dict(titulo='Cazar la falacia', objetivo='Distinguir deducciones válidas de falacias.',
       modelo=None,
       pasos=["Analizá: «Si es sábado, hay chipa so'o. Hay chipa so'o. Luego, es sábado.» ¿Es válido? Justificá con la tabla del condicional o con un contraejemplo del copetín.", 'Analizá: «Probé dos jugos y estaban fríos; todos los jugos del copetín están fríos.» ¿Qué tipo de razonamiento es y qué garantiza su conclusión?'],
       control='Para el primero diste un contraejemplo concreto o la fila de la tabla que lo invalida, y para el segundo dijiste qué grado de certeza tiene la conclusión.'),
 ],
 desafio='Construí una deducción de tres pasos con premisas propias del copetín que use, en algún orden, MPP, MTT y adjunción. Indicá la regla en cada paso.',
 sol=dict(resultado="Act. 1: a) p → q, p ⊢ q: MPP; b) p → q, ¬q ⊢ ¬p: MTT; c) p ∨ q, ¬q ⊢ p: MTP; d) p → q, q → r ⊢ p → r: silogismo hipotético. Act. 2: de 1) y 2): d (MPP); de d y 3): s (MPP); de 4): m (MTP). Cadena: v → d, v, d → s, t ∨ m, ¬t ⊢ d, s, m. Act. 3: el primero es la falacia de afirmación del consecuente: Ña Rosa puede hacer chipa so'o un martes (fila p = F, q = V: premisas V y conclusión F). El segundo es inductivo: la conclusión es probable, no segura; un tercer jugo tibio la refuta. Desafío: respuesta abierta; se controla que cada paso cite su regla y use pasos anteriores.",
          errores='Confundir MTT con la falacia de negación del antecedente; aplicar MTP sin la negación de una de las partes; aceptar la afirmación del consecuente como MPP; tratar una inducción como deducción.'),
 )

# =============================================================== UNIDAD 3 — INTRODUCCIÓN A LA ALGORITMIA
PR[13] = dict(
 titulo='Reconocer y reparar algoritmos', entorno=PAPEL,
 competencia='Identificar las características de un algoritmo, clasificarlo y detectar defectos de precisión, finitud o definición.',
 saber=['Todo algoritmo debe ser preciso (sin ambigüedad), finito (termina) y definido (misma entrada, mismo resultado).',
        'Cualitativo: pasos sin cálculo. Cuantitativo: opera con números. Etapas de resolución: análisis → diseño → prueba.'],
 antes='Un buen algoritmo lo puede seguir otra persona sin hacerte preguntas: usá esa prueba en las tres actividades.',
 acts=[
  dict(titulo='Ordenar el caos', objetivo='Reconstruir la secuencia correcta de un algoritmo cualitativo.',
       modelo=('Pasos desordenados de «preparar el cocido quemado»', ['· Servir en la taza · Tostar la yerba con el azúcar en la olla · Agregar el agua (o la leche) · Colar · Dejar hervir unos minutos · Encender el fuego']),
       pasos=['Numerá los seis pasos en el orden correcto.', 'Verificá con tu pareja de banco: ¿alguien podría seguir tu orden sin haber preparado nunca un cocido?', 'Indicá cuál sería el dato de «entrada» y cuál el «resultado» de este algoritmo.'],
       control='Tu pareja pudo seguir el orden sin preguntar nada, y ningún paso necesita algo que se hace después.'),
  dict(titulo='Cualitativo o cuantitativo', objetivo='Clasificar algoritmos del entorno.',
       modelo=None,
       pasos=['Clasificá (CL o CT): a) calcular el vuelto de una compra; b) armar la mesa para los clientes; c) promediar las notas de la etapa; d) doblar servilletas; e) sumar la recaudación del día; f) encender la computadora del laboratorio.', 'Elegí un CT y anotá qué números entran y qué número sale.'],
       control='Cada CT tiene identificados los números que entran y el que sale, y cada CL se puede hacer sin calcular nada.'),
  dict(titulo='El detector de defectos', objetivo='Diagnosticar qué característica viola cada algoritmo defectuoso.',
       modelo=('Tres algoritmos con problemas', ['1) «Cobrá un precio razonable al cliente.» 2) «Mientras haya clientes, repetí: atendé al siguiente» — en un copetín que nunca cierra la fila. 3) «Elegí al azar si aplicás o no el descuento.»']),
       pasos=['Indicá para cada uno la característica violada: precisión, finitud o definición.', 'Reescribí el 1) para que sea preciso (inventá el precio exacto).', 'Proponé para el 2) una condición de corte que lo haga finito.'],
       control='Tu versión del 1) la puede cumplir cualquier cajero sin preguntar nada, y tu condición de corte del 2) llega a cumplirse en algún momento.'),
 ],
 desafio='Escribí un algoritmo cualitativo de 5 pasos para «cargar crédito al celular» y marcá al costado de cada paso una P (preciso) si cualquiera podría ejecutarlo sin dudar. Corregí los que no la lleven.',
 sol=dict(resultado='Act. 1: 1) Encender el fuego; 2) Tostar la yerba con el azúcar en la olla; 3) Agregar el agua (o la leche); 4) Dejar hervir unos minutos; 5) Colar; 6) Servir en la taza. Cada paso necesita el anterior: no se puede colar lo que no hirvió ni servir lo que no se coló. Entrada: yerba, azúcar y agua (o leche); resultado: el cocido servido. Act. 2: CT: a), c), e); CL: b), d), f). Ejemplo: en a) entran el total y el pago, sale el vuelto. Act. 3: 1) precisión («razonable» no es un número): «Cobrá G. 3.000 por tortilla»; 2) finitud: «hasta las 12:00» o «mientras haya clientes y la hora sea menor que las 12:00»; 3) definición (la misma compra puede dar dos resultados). Desafío: respuesta abierta.',
          errores='Colar antes de hervir o agregar el agua antes de tostar la yerba; clasificar como cuantitativo todo lo que use la computadora; confundir finitud con precisión; corregir el 1) con otra palabra vaga («precio justo»).'))

PR[14] = dict(
 titulo='Escribir pseudocódigo y dibujar diagramas', entorno=PAPEL,
 competencia='Escribir algoritmos secuenciales en pseudocódigo y traducirlos al diagrama de flujo con los símbolos normalizados.',
 saber=['Pseudocódigo: Inicio, Leer, asignación (←), Escribir, Fin. Diagrama: óvalo (terminal), paralelogramo (entrada/salida), rectángulo (proceso), rombo (decisión), flechas de flujo.',
        'Método: entradas → Leer; fórmula → asignación; resultado → Escribir. Después, prueba de escritorio.'],
 antes='Tené a la vista la Figura 14.1 de la clase con la simbología normalizada: cada figura tiene una función fija y usarla bien forma parte de la evaluación.',
 acts=[
  dict(titulo='Del enunciado al pseudocódigo', objetivo='Traducir un problema de fórmula directa.',
       modelo=('Problema', ['Ña Rosa quiere saber el doble de la cantidad de tortillas que vendió, porque mañana es feria y espera vender el doble.']),
       pasos=['Identificá la entrada, el proceso y la salida.', 'Escribí el pseudocódigo completo entre Inicio y Fin.', 'Antes de la prueba, anotá el resultado que esperás para cantidad = 35; después hacé la prueba de escritorio.', 'Anotá qué línea cambiarías si mañana esperara vender el triple.'],
       control='La prueba de escritorio llega al mismo número que anotaste antes de hacerla. Si no, revisá la asignación.'),
  dict(titulo='Emparejar símbolos', objetivo='Asignar a cada acción su figura del diagrama.',
       modelo=None,
       pasos=['Uní cada acción con su símbolo: a) Leer base — b) area ← base * altura — c) ¿area > 40? — d) Escribir area — e) Inicio — f) Fin.', 'Indicá cuántos paralelogramos, rectángulos, rombos y óvalos usaste en total.'],
       control='Cada figura cumple la función que le asigna la Figura 14.1, y el total de figuras coincide con la cantidad de acciones.'),
  dict(titulo='Del pseudocódigo al diagrama', objetivo='Dibujar el diagrama de flujo completo de un algoritmo dado.',
       modelo=('Algoritmo', E('Inicio', '    Leer base', '    Leer altura', '    area ← base * altura', '    Escribir area', 'Fin')),
       pasos=['Dibujá el diagrama completo, de arriba hacia abajo, con las flechas.', 'Verificá que cada línea del pseudocódigo tenga su figura y que las figuras sean las correctas.', 'Calculá a mano el área para base = 8 y altura = 5; después hacé la prueba de escritorio siguiendo el diagrama con el dedo.'],
       control='Cada línea del pseudocódigo tiene su figura, y el recorrido con el dedo da el mismo resultado que tu cálculo a mano.'),
 ],
 desafio='Escribí el pseudocódigo y dibujá el diagrama de un algoritmo que lea el precio de 1 kg de harina y escriba el costo de 3,5 kg. Probalo con G. 6.000 el kilo. (En la asignación, el número se escribe 3.5: dentro del código el punto es la coma decimal.)',
 sol=dict(resultado='Act. 1: entrada cantidad; proceso doble ← cantidad * 2; salida doble. Inicio / Leer cantidad / doble ← cantidad * 2 / Escribir doble / Fin. Con 35 escribe 70. Para el triple se cambia solo la asignación: doble ← cantidad * 3 (conviene renombrar la variable). Act. 2: a) y d) paralelogramo; b) rectángulo; c) rombo; e) y f) óvalo: 2 óvalos, 2 paralelogramos, 1 rectángulo, 1 rombo. Act. 3: 6 figuras: 2 óvalos, 3 paralelogramos (dos Leer y un Escribir), 1 rectángulo; con base 8 y altura 5 escribe 40. Desafío: Inicio / Leer precio / costo ← precio * 3.5 / Escribir costo / Fin; con 6000 escribe 21000 (G. 21.000).' + VER,
          errores='Usar rectángulo para Leer o Escribir; escribir el resultado sin asignarlo; escribir 3,5 dentro del código; olvidar las flechas o el óvalo de Fin.'))

PR[15] = dict(
 titulo='Evaluar expresiones como la computadora', entorno=PAPEL,
 competencia='Evaluar expresiones aritméticas, relacionales y lógicas respetando la jerarquía de operadores.',
 saber=['Jerarquía: 1.º paréntesis · 2.º * y / · 3.º + y − · 4.º relacionales (>, <, >=, <=, =, <>) · 5.º NO, Y, O.',
        'Las relacionales devuelven V o F; las lógicas combinan esos V/F con las tablas de la Unidad 2. Dentro del código, los números se escriben sin separador de miles y los textos van entre comillas rectas.'],
 antes='Mostrá cada paso intermedio: el resultado final sin pasos no se puede revisar.',
 acts=[
  dict(titulo='Aritmética con jerarquía', objetivo='Evaluar paso a paso, mostrando el orden.',
       modelo=None,
       pasos=['Evaluá mostrando cada paso: a) 7 + 2 * 3 ; b) (7 + 2) * 3 ; c) 18 − 6 / 2 ; d) 4 * 5 − 3 * 2 ; e) 100 − (20 + 5) * 2.', 'Marcá con un círculo, en cada caso, la operación que se hace primero.'],
       control='En cada expresión, la operación marcada es la de mayor jerarquía, y al recalcular con una calculadora científica obtenés lo mismo.'),
  dict(titulo='Relacionales: veredicto V o F', objetivo='Evaluar comparaciones, incluida la frontera.',
       modelo=('Valores', ['a = 12 · b = 12 · c = 5.']),
       pasos=['Evaluá: a) a > b ; b) a >= b ; c) c <> 5 ; d) a − b = 0 ; e) c * 3 <= a + b.', 'Explicá en una línea la diferencia entre a) y b) con estos valores.'],
       control='Para cada comparación escribiste primero los dos valores que se comparan y recién después decidiste V o F.'),
  dict(titulo='Condiciones compuestas del mostrador', objetivo='Evaluar expresiones lógicas con datos de una venta.',
       modelo=('Venta en curso', E('total = 58000 · cantidad = 4 · medioPago = "efectivo"')),
       pasos=['Evaluá: a) (total >= 60000) Y (medioPago = "QR") ; b) (total >= 60000) O (cantidad >= 4) ; c) NO (medioPago = "QR") ; d) (total > 50000) Y (cantidad < 10) Y (medioPago = "efectivo").', 'Para cada resultado F, señalá exactamente qué comparación (o qué comparaciones) lo produjo.'],
       control='Cada comparación está evaluada por separado antes de aplicar Y, O o NO, y para cada F nombraste todas las comparaciones responsables.'),
 ],
 desafio='Escribí una condición compuesta que sea V para la venta del modelo pero que se vuelva F si el cliente cambia el pago a "QR". Verificala en los dos escenarios.',
 sol=dict(resultado='Act. 1: a) 7 + 6 = 13; b) 9 * 3 = 27; c) 18 − 3 = 15; d) 20 − 6 = 14; e) 100 − 25 * 2 = 100 − 50 = 50. Act. 2: a) F; b) V; c) F; d) V (0 = 0); e) 15 <= 24, V. Tres V y dos F: con a = b, > es F y >= es V; la frontera separa los dos operadores. Act. 3: a) F Y F = F (las dos comparaciones fallan: 58000 no llega a 60000 y el pago no es "QR"); b) F O V = V; c) NO F = V; d) V Y V Y V = V. Desafío: por ejemplo (total > 50000) Y (medioPago = "efectivo"): V con la venta del modelo y F con medioPago = "QR".' + VER,
          errores='Calcular de izquierda a derecha (7 + 2 * 3 = 27); confundir > con >=; escribir 60.000 dentro de la expresión (vale 60); nombrar un solo culpable en a).'))

PR[16] = dict(
 titulo='Algoritmos secuenciales y prueba de escritorio', entorno=PAPEL,
 competencia='Escribir algoritmos secuenciales completos y validarlos con pruebas de escritorio en tabla.',
 saber=['Leer trae datos; la asignación (←) calcula y guarda; Escribir muestra; Fin termina. Toda variable recibe valor antes de usarse.',
        'Prueba de escritorio: una columna por variable, una fila por enunciado; se anota el valor de cada variable después de cada paso.'],
 antes='En la tabla de escritorio, el valor anterior de una variable se tacha, no se borra: así se ve el recorrido.',
 acts=[
  dict(titulo='Completar el algoritmo', objetivo='Rellenar las líneas que faltan en un algoritmo con huecos.',
       modelo=('Algoritmo incompleto (calcula el total y el vuelto)', E('Inicio', '    Leer precio', '    Leer cantidad', '    Leer pago', '    total ← ______', '    vuelto ← ______', '    Escribir ______', 'Fin')),
       pasos=['Completá las tres líneas con las expresiones correctas.', 'Hacé la prueba de escritorio con precio = 3500, cantidad = 4 y pago = 25000.', 'Anotá el total y el vuelto finales.'],
       control='Tu tabla tiene una fila por línea del algoritmo, y el vuelto sumado al total devuelve exactamente el pago.'),
  dict(titulo='La tabla que no miente', objetivo='Rastrear asignaciones encadenadas sin perder ningún valor.',
       modelo=('Algoritmo', E('Inicio', '    a ← 7', '    b ← 3', '    a ← a + b', '    b ← a − b', '    a ← a − b', '    Escribir a, b', 'Fin')),
       pasos=['Armá la tabla con columnas a y b, y una fila por asignación.', 'Completala paso a paso: cada línea usa los valores de la fila anterior.', 'Anotá qué se escribe al final y respondé: ¿qué hizo este algoritmo con los valores iniciales de a y b?'],
       control='Repetiste la tabla con otro par de valores iniciales elegido por vos, y el algoritmo hizo con ellos lo mismo que con los originales.'),
  dict(titulo='Diseñar desde cero', objetivo='Producir un algoritmo secuencial propio y probarlo.',
       modelo=('Problema', ['El cliente lleva tres productos de precios distintos. Ña Rosa quiere el total y el promedio por producto.']),
       pasos=['Escribí el algoritmo (tres lecturas, dos asignaciones, dos escrituras).', 'Hacé la prueba de escritorio con 2000, 4500 y 3500.', 'Verificá tu promedio multiplicándolo por 3: debe devolverte el total.'],
       control='Tu promedio multiplicado por 3 devuelve el total; si redondeaste, la diferencia es de centésimos y sabés explicar de dónde sale.'),
 ],
 desafio='Escribí un algoritmo que lea un precio y escriba el precio con 10 % de recargo por delivery (sin usar decisión). Probalo con G. 18.000 y verificá que el recargo agregado sea exactamente la décima parte del precio.',
 sol=dict(resultado='Act. 1: total ← precio * cantidad; vuelto ← pago − total; Escribir total, vuelto. Prueba: total = 14000, vuelto = 11000 (control: 14000 + 11000 = 25000). Act. 2: a = 7, b = 3 → a = 10 → b = 7 → a = 3; escribe 3 y 7: intercambió los valores sin variable auxiliar. Con otro par, por ejemplo a = 10 y b = 4, escribe 4 y 10. Act. 3: Leer p1, p2, p3 / total ← p1 + p2 + p3 / promedio ← total / 3 / Escribir total / Escribir promedio. total = 10000; promedio = 10000 / 3 = 3333,33… (periódico; PSeInt muestra 3333.3333333333). El valor exacto por 3 da 10000; redondeado a 3333,33, da 9999,99: el centésimo que falta es el redondeo. Desafío: conRecargo ← precio + precio * 10 / 100; con 18000 escribe 19800; recargo 1800 = 18000 / 10.' + VER,
          errores='Invertir la resta del vuelto (da negativo); en la Actividad 2, usar el valor inicial de a en lugar del de la fila anterior; definir el promedio como entero; escribir 18.000 dentro del código.'))

PR[17] = dict(
 titulo='Decidir con Si–Entonces–Sino', entorno=PAPEL,
 competencia='Diseñar y probar algoritmos con decisiones simples, con atención al caso frontera.',
 saber=['Si condición Entonces bloque-V Sino bloque-F FinSi: se ejecuta exactamente un bloque. La condición es una expresión lógica.',
        'Toda decisión se prueba al menos con un caso V, un caso F y —si existe— el caso frontera del operador (>= vs >).'],
 antes='Antes de cada prueba, anotá el resultado esperado: la prueba sirve si se compara con algo.',
 acts=[
  dict(titulo='El envío del pedido', objetivo='Completar y probar una decisión con frontera.',
       modelo=('Regla del copetín: pedidos de G. 70.000 o más, envío gratis; los demás pagan G. 8.000', E('Inicio', '    Leer pedido', '    Si pedido ______ 70000 Entonces', '        envio ← ______', '    Sino', '        envio ← ______', '    FinSi', '    Escribir pedido + envio', 'Fin')),
       pasos=['Completá el operador y las dos asignaciones.', 'Anotá el resultado esperado para pedido = 85000, 70000 y 45000; después probá los tres casos.', 'Explicá por qué elegiste >= y no >.'],
       control='Los tres resultados coinciden con los que anotaste, y el pedido que está exactamente en el límite recibe lo que dice la regla («o más»).'),
  dict(titulo='Par o impar', objetivo='Usar el operador mod en una condición.',
       modelo=('Recordá', ['n mod 2 es el resto de dividir n entre 2: vale 0 si n es par y 1 si es impar.']),
       pasos=['Escribí un algoritmo que lea un número de boleta y escriba "par" o "impar" usando n mod 2.', 'Probalo con 128 y con 45.', 'Respondé: ¿qué escribe con 0? ¿Tu condición lo trata bien?'],
       control='Tu condición compara el resto con un valor concreto, y la prueba con 0 está anotada con su explicación.'),
  dict(titulo='Diseñar la decisión completa', objetivo='Producir una decisión propia desde el enunciado.',
       modelo=('Problema', ['Si el cliente compra 10 croquetas o más, paga G. 2.000 por unidad; si compra menos, paga G. 2.500 por unidad. Escribir el total.']),
       pasos=['Escribí el algoritmo con Leer cantidad, la decisión y el cálculo del total.', 'Probalo con cantidad = 12, 10 y 6.', 'Marcá cuál de tus tres pruebas fue la frontera y por qué era obligatoria.'],
       control='Una de tus tres pruebas está exactamente en el límite de la regla, y su total está calculado con el precio que le corresponde.'),
 ],
 desafio='Modificá el algoritmo del envío para que, además, escriba "¡Envío gratis!" solo cuando corresponda, sin duplicar la decisión (todo dentro del mismo Si). Probalo con los tres casos anteriores.',
 sol=dict(resultado='Act. 1: Si pedido >= 70000 Entonces envio ← 0 Sino envio ← 8000 FinSi. Escribe 85000, 70000 y 53000. Con > el pedido de 70000 pagaría envío, y la regla dice «o más». Act. 2: Si n mod 2 = 0 Entonces Escribir "par" Sino Escribir "impar" FinSi. 128 → par; 45 → impar; 0 → par (0 mod 2 = 0). Act. 3: Si cantidad >= 10 Entonces total ← cantidad * 2000 Sino total ← cantidad * 2500 FinSi. 12 → 24000; 10 → 20000 (frontera: precio mayorista); 6 → 15000. Desafío: se agrega Escribir "¡Envío gratis!" en el bloque Entonces; aparece con 85000 y 70000, no con 45000.' + VER,
          errores='Usar > en la frontera; escribir 70.000 en la condición (PSeInt lo lee como 70); comparar n mod 2 con 2; en la Actividad 3, multiplicar siempre por 2500.'))

PR[18] = dict(
 titulo='Clasificar con decisiones anidadas', entorno=PAPEL,
 competencia='Construir decisiones anidadas que clasifican en tres o más categorías completas y disjuntas.',
 saber=['Un Si dentro del Sino de otro Si clasifica en más de dos categorías; cada dato recorre exactamente una rama.',
        'Preguntá de la categoría más exigente a la menos exigente. Cada rama Sino hereda la negación de las condiciones anteriores.'],
 antes='Para cada clasificación, probá un valor de cada categoría y cada valor de frontera.',
 acts=[
  dict(titulo='Los tres tamaños del jugo', objetivo='Completar una clasificación anidada de tres categorías.',
       modelo=('Regla: 500 ml o más, «grande» (G. 6.000); de 300 a menos de 500, «mediano» (G. 4.500); menos de 300, «chico» (G. 3.000)', E('Inicio', '    Leer ml', '    Si ml >= 500 Entonces', '        …', '    Sino', '        Si ml >= ______ Entonces', '            …', '        Sino', '            …', '        FinSi', '    FinSi', 'Fin')),
       pasos=['Completá la condición interna y las tres ramas (categoría y precio).', 'Probá con ml = 500, 499, 300 y 250, anotando categoría y precio.', 'Explicá qué habría pasado con ml = 499 y con ml = 500 si la primera pregunta hubiera sido ml >= 300.'],
       control='Cada valor de prueba cayó en una sola categoría, y los dos valores de frontera de la regla están probados.'),
  dict(titulo='Condición compuesta + decisión', objetivo='Combinar Y/O dentro de un Si.',
       modelo=('Regla de la promo', ['Hay promo si el pedido es de G. 30.000 o más Y el pago es con QR.']),
       pasos=['Escribí la decisión que muestra "promo" o "sin promo".', 'Probá los cuatro escenarios: (30000, QR), (30000, efectivo), (20000, QR), (50000, QR).', 'Relacioná tus cuatro pruebas con la tabla de verdad de la conjunción.'],
       control='Para cada escenario anotaste el valor de cada comparación por separado, y el resultado coincide con la fila correspondiente de la tabla de la conjunción.'),
  dict(titulo='Reparar la cadena rota', objetivo='Detectar y corregir el error de orden en una cadena anidada.',
       modelo=('Cadena defectuosa (pedidos para eventos: 30 unidades o más, «evento»; de 10 a 29, «familiar»; menos de 10, «individual»)', E('Si cantidad >= 10 Entonces', '    Escribir "familiar"', 'Sino', '    Si cantidad >= 30 Entonces', '        Escribir "evento"', '    Sino', '        Escribir "individual"', '    FinSi', 'FinSi')),
       pasos=['Probá la cadena tal como está con cantidad = 45 y anotá qué escribe.', 'Explicá por qué el resultado es incorrecto aunque la sintaxis sea válida.', 'Reescribí la cadena en el orden correcto y volvé a probar con 45, 18 y 4.'],
       control='La cadena corregida pregunta primero por la categoría más exigente, y tus tres pruebas caen cada una en una categoría distinta.'),
 ],
 desafio='Diseñá una clasificación de CUATRO categorías para el tiempo de espera de un pedido (por ejemplo: hasta 5 min, hasta 15, hasta 30, más de 30) y probala con un valor de cada categoría más una frontera.',
 sol=dict(resultado='Act. 1: interna ml >= 300; ramas: "grande" 6000 · "mediano" 4500 · "chico" 3000. 500 → grande 6.000; 499 → mediano 4.500; 300 → mediano 4.500 (frontera); 250 → chico 3.000. Con la primera pregunta ml >= 300, el 499 seguiría en «mediano», pero el 500 también caería en «mediano»: el orden protege a la categoría superior. Act. 2: Si (pedido >= 30000) Y (pago = "QR") Entonces Escribir "promo" Sino Escribir "sin promo" FinSi. Promo: (30000, QR) y (50000, QR); sin promo: (30000, efectivo) (V Y F) y (20000, QR) (F Y V). Act. 3: con 45 escribe «familiar»: la primera pregunta (>= 10) captura también a los de 30 o más, y la rama «evento» nunca se alcanza. Corregida (Si cantidad >= 30 … Sino Si cantidad >= 10 …): 45 → evento; 18 → familiar; 4 → individual. Desafío: respuesta abierta; se controla que cada valor caiga en una sola rama y que la frontera esté probada.' + VER,
          errores='Preguntar de menor a mayor exigencia; repetir en la rama Sino una condición que ya está negada; usar O en lugar de Y en la promo; olvidar probar las fronteras.'))

PR[19] = dict(
 titulo='Repetir con ciclos y contadores', entorno=PAPEL,
 competencia='Diseñar y rastrear ciclos Mientras y Para con contadores bien inicializados y actualizados.',
 saber=['Mientras evalúa la condición ANTES de cada vuelta; algo del bloque debe acercarla a F. Para inicializa, compara e incrementa solo.',
        'Contador: se inicializa fuera del ciclo (c ← 0 o c ← 1) y se actualiza dentro (c ← c + 1). Sin actualización: ciclo infinito.'],
 antes='En la tabla de un ciclo va una fila por vuelta, más la evaluación final de la condición.',
 acts=[
  dict(titulo='Rastrear vuelta por vuelta', objetivo='Seguir un ciclo con la tabla de escritorio.',
       modelo=('Algoritmo', E('Inicio', '    c ← 2', '    Mientras c <= 12 Hacer', '        Escribir c', '        c ← c + 3', '    FinMientras', '    Escribir "fin"', 'Fin')),
       pasos=['Armá la tabla: vuelta, c al entrar, ¿c <= 12?, escribe, c al salir.', 'Completala hasta que la condición dé F.', 'Anotá cuántas vueltas dio y con qué valor de c salió del ciclo.'],
       control='La última fila de tu tabla es la evaluación que da F, y en esa fila no se escribe nada: el valor con que sale c no se muestra.'),
  dict(titulo='El Para cuenta solo', objetivo='Usar el ciclo Para cuando las vueltas se conocen.',
       modelo=('Situación', ["Ña Rosa numera las 9 bandejas de chipa so'o que hornea cada sábado."]),
       pasos=['Escribí con Para un algoritmo que escriba «Bandeja n lista» para n de 1 a 9.', 'Indicá cuántas vueltas da sin hacer la tabla (justificá).', 'Reescribí el mismo algoritmo con Mientras y compará: ¿qué tres cosas hace solo el Para que en el Mientras escribiste vos?'],
       control='Tu cantidad de vueltas sale de los límites del Para, y en la versión con Mientras aparecen, escritas por vos, las tres partes que el Para hace solo.'),
  dict(titulo='Cazar el ciclo infinito', objetivo='Diagnosticar y reparar errores clásicos de ciclos.',
       modelo=('Dos ciclos con problemas', E('1)  c ← 1', '    Mientras c <= 5 Hacer', '        Escribir c', '    FinMientras', '', '2)  Mientras c <= 5 Hacer', '        Escribir c', '        c ← c + 1', '    FinMientras')),
       pasos=['Indicá qué le falta a cada uno y qué pasaría al ejecutarlo.', 'Reescribí los dos corregidos.', 'Verificá con una tabla corta que tus versiones escriben 1 a 5 y terminan.'],
       control='Cada versión corregida termina, y tu tabla corta lo demuestra mostrando la vuelta en que la condición se vuelve F.'),
 ],
 desafio='Escribí un ciclo que haga la cuenta regresiva del cierre: escriba 10, 9, 8, ..., 1 y al final "¡Cerrado!". Pista: el contador también puede restar.',
 sol=dict(resultado='Act. 1: escribe 2, 5, 8 y 11 (4 vueltas); con c = 14 la condición da F y sale; se escribe «fin». Act. 2: Para n ← 1 Hasta 9 Hacer Escribir "Bandeja ", n, " lista" FinPara: 9 vueltas (de 1 a 9, de a uno). Con Mientras: n ← 1 (inicialización), Mientras n <= 9 (comparación), n ← n + 1 (incremento). Act. 3: 1) no incrementa: escribe 1 sin fin (ciclo infinito); 2) no inicializa c: no tiene valor de partida definido y el algoritmo no se puede verificar. Corregidos (c ← 1 antes y c ← c + 1 adentro), escriben 1 a 5 y salen con c = 6. Desafío: Para c ← 10 Hasta 1 Con Paso −1 Hacer Escribir c FinPara / Escribir "¡Cerrado!" (o con Mientras, c ← c − 1).' + VER,
          errores='Escribir el 14 en la Actividad 1 (se evaluó una vuelta de más); inicializar el contador dentro del ciclo; olvidar el incremento; en la cuenta regresiva, usar Para sin paso negativo (no da ninguna vuelta).'))

PR[20] = dict(
 titulo='Acumular totales y promedios', entorno=PAPEL,
 competencia='Calcular totales y promedios con acumulador, contador y centinela, protegiendo la división por cero.',
 saber=['Acumulador: s ← 0 fuera del ciclo; s ← s + valor adentro. Con el contador forman el promedio: promedio ← s / c, solo si c > 0.',
        'Centinela: valor que significa «terminé» (por ejemplo 0). Se lee antes de entrar y al final de cada vuelta; se compara pero nunca se acumula.'],
 antes='En la tabla de escritorio, el centinela tiene su propia fila: es la que corta el ciclo.',
 acts=[
  dict(titulo='La caja de la tarde', objetivo='Rastrear un ciclo con acumulador, contador y centinela.',
       modelo=('Algoritmo', E('Inicio', '    s ← 0', '    c ← 0', '    Leer venta', '    Mientras venta <> 0 Hacer', '        s ← s + venta', '        c ← c + 1', '        Leer venta', '    FinMientras', '    Si c > 0 Entonces', '        Escribir s, s / c', '    Sino', '        Escribir "sin ventas"', '    FinSi', 'Fin')),
       pasos=['Hacé la tabla de escritorio con las ventas 7000, 13000, 4000 y el centinela 0.', 'Anotá s, c y el promedio finales.', 'Repetí la prueba ingresando 0 como primer dato: ¿qué se escribe y por qué no falla?'],
       control='Tu tabla tiene una fila por venta más la fila del centinela, y el centinela no aparece sumado en s.'),
  dict(titulo='Contar con condición', objetivo='Combinar acumulador con un contador condicionado.',
       modelo=('Problema', ['Además del total, Ña Rosa quiere saber cuántas ventas de la tarde fueron de G. 10.000 o más.']),
       pasos=['Agregá al algoritmo de la Actividad 1 un contador cg que solo cuente las ventas >= 10000 (¿dónde va su Si?).', 'Probá con las mismas ventas (7000, 13000, 4000, 0).', 'Respondé: ¿cg se inicializa igual que c? ¿Se incrementa en las mismas vueltas?'],
       control='El Si de cg está dentro del ciclo, y en ninguna fila de tu tabla cg es mayor que c.'),
  dict(titulo='Diseñar la totalización completa', objetivo='Producir desde cero un ciclo con centinela y doble salida.',
       modelo=('Problema', ['Registrar los kilos de harina que llegan en varias bolsas (fin de carga: 0) y escribir el total de kilos y el promedio por bolsa.']),
       pasos=['Escribí el algoritmo completo, con la guarda de división por cero.', 'Probalo con las bolsas de 25, 25 y 10 kilos.', 'Verificá: promedio × cantidad de bolsas = total.'],
       control='Tu algoritmo tiene la guarda de división por cero, y la verificación del paso 3 devuelve el total de tu tabla.'),
 ],
 desafio='Ampliá el algoritmo de la Actividad 3 para que también escriba la bolsa más pesada. Pista: mayor ← 0 antes del ciclo y una decisión adentro. ¿Qué valor inicial usarías si pudieran existir valores negativos?',
 sol=dict(resultado='Act. 1: s = 24000, c = 3, promedio 24000 / 3 = 8000. Con 0 como primer dato no entra al ciclo, c queda en 0 y escribe "sin ventas": la guarda c > 0 evita dividir por cero. Act. 2: cg ← 0 antes del ciclo; dentro, Si venta >= 10000 Entonces cg ← cg + 1 FinSi. cg = 1 (solo la de 13000). Se inicializa igual que c, pero se incrementa solo cuando su condición es V. Act. 3: total ← 0, bolsas ← 0, Leer kilos, Mientras kilos <> 0 (acumular, contar, leer), Si bolsas > 0 Entonces Escribir total, total / bolsas. Total 60 kilos, 3 bolsas, promedio 20; 20 × 3 = 60. Desafío: mayor = 25; si pudieran existir valores negativos, mayor se inicializa con el primer dato leído (no con 0).' + VER,
          errores='Inicializar s o c dentro del ciclo; acumular el centinela; dividir sin la guarda c > 0; poner el Si de cg fuera del ciclo; leer el siguiente dato antes de acumular el actual.'),
 transfer=dict(
  caso=('la rifa de la promoción', ['Cada estudiante entrega lo recaudado con su talonario; la carga termina con 0.', 'Datos: 35000 · 50000 · 20000 · 45000 · 0.', 'Se pide: total recaudado, cantidad de talonarios, promedio por talonario y cuántos talonarios superaron G. 40.000.']),
  pasos=['Adaptá el algoritmo de la Actividad 2 a la rifa (otro contador condicionado y otro umbral).', 'Intercambiá el algoritmo con otro equipo: hacé su prueba de escritorio con los datos de la rifa y buscá al menos un error o una mejora.', 'Corregí tu versión con lo que te señalaron y justificá por escrito la versión final.'],
  control='Las dos versiones del equipo (la original y la corregida) llegan a los mismos resultados en la prueba de escritorio, y la justificación nombra el cambio hecho.',
  sol='Total 150.000; 4 talonarios; promedio 37.500; superaron 40.000: 2 (50.000 y 45.000). Errores típicos que se detectan en la revisión: usar >= en lugar de > (no cambia el resultado con estos datos, pero sí con un talonario de exactamente 40.000) y acumular el centinela.' + VER))

PR[21] = dict(
 titulo='Proyecto: construir el sistema de caja completo', entorno=PAPEL,
 competencia='Integrar análisis, diseño, decisión, ciclo, contador y acumulador en un algoritmo completo validado con prueba de escritorio.',
 saber=['Método integral: análisis (entradas, proceso, salidas) → diseño (pseudocódigo) → prueba (tabla) → control cruzado.',
        'El sistema de caja combina: ciclo con centinela, decisión por el descuento, acumulador de lo cobrado y contadores de ventas y de descuentos.'],
 antes='Si tenés PSeInt, podés pasar el algoritmo terminado como en el apartado «Puente a PSeInt» de la clase y comparar su salida con tu tabla; la prueba de escritorio sigue siendo obligatoria.',
 acts=[
  dict(titulo='Análisis del encargo', objetivo='Definir las variables antes de escribir una sola línea.',
       modelo=('El encargo de Ña Rosa', ['«Cargá mis ventas del cierre una por una y terminá con 0. Las de G. 50.000 o más llevan 10 % de descuento. Al final quiero: lo recaudado, cuántas ventas hubo, cuántas con descuento y el promedio por venta.»']),
       pasos=['Listá las entradas, el proceso y las salidas del sistema.', 'Definí el nombre y el valor inicial de cada variable (incluida la del monto a cobrar por venta).', 'Indicá cuál es el centinela y por qué no debe procesarse.'],
       control='Cada variable tiene nombre, función y valor inicial, y el centinela no forma parte de ninguna suma ni de ningún conteo.'),
  dict(titulo='Diseño y prueba con el cierre del jueves', objetivo='Escribir el algoritmo completo y validarlo con datos.',
       modelo=('Ventas del jueves', ['80.000 · 30.000 · 70.000 · 0 (fin).']),
       pasos=['Escribí el pseudocódigo completo (ciclo con centinela, decisión del descuento, acumulador y los dos contadores, guarda de división por cero).', 'Hacé la prueba de escritorio completa con las ventas del jueves: una fila por vuelta, columnas venta, ¿≥ 50.000?, cobrar, suma, c, cd.', 'Anotá los cuatro resultados finales (recaudación, ventas, con descuento, promedio).'],
       control='Tu tabla tiene una fila por venta más la del centinela, y cada venta con descuento cobra exactamente el 90 % de su monto.'),
  dict(titulo='Control cruzado y mejora', objetivo='Verificar por un camino independiente y extender el sistema.',
       modelo=None,
       pasos=['Control cruzado: sumá las ventas SIN descuento, calculá el descuento total otorgado y verificá: suma sin descuentos − descuentos = tu recaudación.', 'Agregá al sistema la venta más alta del día (variable mayor) y anotá qué valor da con las ventas del jueves.', 'Escribí en dos líneas qué otra estadística útil podría pedirte Ña Rosa y qué bloques reutilizarías para calcularla.'],
       control='El control cruzado cierra al guaraní con tu recaudación; si no cierra, el error está en una fila de la tabla y lo buscás antes de seguir.'),
 ],
 desafio='Corré tu sistema completo con un día inventado por vos de cinco ventas (al menos dos con descuento y una frontera de exactamente G. 50.000). Entregá la tabla de escritorio y el control cruzado: si el control no cierra al guaraní, el error está en la tabla, no en la suerte.',
 sol=dict(resultado='Act. 1: entradas: cada venta (centinela 0); proceso: decidir el descuento, acumular y contar; salidas: recaudación, cantidad de ventas, ventas con descuento y promedio. Variables: venta, cobrar, suma ← 0, c ← 0, cd ← 0. El centinela 0 corta el ciclo antes de procesarse: si se acumulara, contaría una venta inexistente. Act. 2: 80.000 → V → 72.000 (suma 72.000, c 1, cd 1); 30.000 → F → 30.000 (102.000, 2, 1); 70.000 → V → 63.000 (165.000, 3, 2); 0 corta. Recaudación 165.000; 3 ventas; 2 con descuento; promedio 165.000 / 3 = 55.000. Act. 3: sin descuentos 180.000; descuentos 8.000 + 7.000 = 15.000; 180.000 − 15.000 = 165.000: el control cierra. Venta más alta: 80.000 (sobre el monto original; si se toma lo cobrado, 72.000: hay que aclarar el criterio). Desafío: respuesta abierta; la frontera de 50.000 debe cobrar 45.000.' + VER,
          errores='Aplicar el descuento con > en lugar de >= (50.000 sin descuento); acumular venta en lugar de cobrar; contar el centinela; dividir sin la guarda; comparar mayor con cobrar en una vuelta y con venta en otra.'))

PR[5]['transfer'] = dict(
 caso=('la biblioteca del colegio', ['La bibliotecaria encuestó a 40 estudiantes: 22 leen historietas, 17 leen novelas y 9 no leen ninguna de las dos.', 'Hay que completar las cuatro regiones del diagrama.']),
 pasos=['Resolvé el problema con el método de la clase: primero calculá cuántos leen al menos una, después la intersección.', 'Intercambiá el diagrama con otro equipo: revisá sus restas y el control del universo, y anotá cualquier diferencia.', 'Corregí tu versión con lo que te señalaron y justificá por escrito la versión final.'],
 control='Las dos versiones del equipo terminan con las mismas cuatro regiones, que suman el total de encuestados, y la justificación nombra el cambio hecho (o explica por qué no hizo falta).',
 sol='Al menos una: 40 − 9 = 31; ambas: 22 + 17 − 31 = 8; solo historietas 14; solo novelas 9; ninguna 9. Control: 14 + 8 + 9 + 9 = 40. Error típico que se detecta en la revisión: escribir 22 y 17 en las regiones «solo» sin restar la intersección.')


if __name__ == '__main__':
    import re
    for n in range(1, 22):
        p = PR[n]
        assert len(p['acts']) == 3 and p['sol']['resultado'] and p['sol']['errores'] and p['antes'], n
        for a in p['acts']:
            assert a['control'] and not re.search(r'[✓✗✅✔]', a['control']), (n, a['titulo'])
            for l in (a['modelo'][1] if a.get('modelo') else []):
                if l.startswith('§'):
                    assert not re.search(r'\d\.\d{3}\b', l) and '«' not in l, (n, l)
    print('prácticas', len(PR), 'actividades', sum(len(p['acts']) for p in PR.values()), 'transferencias', sum(1 for p in PR.values() if p.get('transfer')))

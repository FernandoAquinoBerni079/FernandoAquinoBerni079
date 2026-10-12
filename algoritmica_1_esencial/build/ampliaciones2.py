# -*- coding: utf-8 -*-
"""Segundo bloque de ampliación: un caso resuelto más por clase, para llegar al mínimo de 750 palabras con
contenido real. Se agrega al final del desarrollo de cada clase (antes de las actividades)."""
from ediciones import H2, P, CAJA, TABLA, COD

EXTRA = {
 3: [H2('Del diagrama a la frase'),
     P('Leer un diagrama también es escribir frases precisas. Si en el diagrama del mostrador la mixta está en la zona central, se puede decir «la mixta se vendió en los dos turnos»; si el jugo está fuera de los óvalos, «el jugo no se vendió en ningún turno». Cada región del diagrama corresponde a una frase con «y», «o» o «ni», y esa traducción es la que vas a usar en la Unidad 2 para pasar del dibujo a la lógica.')],
 4: [H2('Un control rápido de los resultados'),
     P('Antes de dar por buena una unión o una intersección, conviene un control con cardinales. Con A = {chipa, mixta, coquito} y B = {mixta, empanada, gaseosa}: n(A) + n(B) − n(A ∩ B) = 3 + 3 − 1 = 5, y n(A ∪ B) = 5. Si los dos números no coinciden, alguno de los conjuntos está mal escrito. Este control es la versión con conjuntos de la prueba de escritorio.')],
 5: [H2('Cuando el universo cambia'),
     P('El complemento depende del universo. Si U es el menú de cinco productos, el complemento de A = {chipa, mixta, coquito} es {empanada, gaseosa}. Si el universo es más grande —por ejemplo, todos los productos que Ña Rosa sabe preparar, incluidos el cocido y el jugo—, el complemento también crece: {empanada, gaseosa, cocido, jugo}. Por eso, en todo problema con complementos, lo primero es escribir U.')],
 6: [H2('Por qué importa en informática'),
     P('Una computadora solo puede decidir con preguntas que tengan respuesta V o F: «¿el total llega a 50000?», «¿el producto tiene stock?». Cuando una regla de negocio se escribe con palabras vagas —«si la venta es grande», «si el cliente es bueno»—, antes de programarla hay que convertirla en una proposición con un único valor de verdad. Esa conversión es exactamente lo que practicás en esta clase.'),
     P('Por ejemplo, «la venta es grande» puede convertirse en «el total de la venta es mayor o igual que 50000». Ahora sí, para cada venta concreta, la oración es verdadera o falsa, y un algoritmo puede usarla para decidir.')],
 7: [H2('Evaluar con valores dados, paso a paso'),
     P('Con p = «hay chipa» (V), q = «hay cocido» (F) y r = «hay promoción» (V), evaluemos ¬p ∨ (q ↔ r). Primero lo de adentro de los paréntesis: q ↔ r = F ↔ V = F, porque tienen valores distintos. Después la negación: ¬p = F. Al final, el conectivo principal: F ∨ F = F. Escribir cada paso con su resultado parcial evita el error más común, que es aplicar el conectivo principal antes de tiempo.')],
 8: [H2('Leer una tabla como una regla de negocio'),
     P('Supongamos que la promo del copetín se activa cuando se cumple p ∨ q, con p = «paga con QR» y q = «lleva vaso propio». La tabla de p ∨ q dice que la promo se activa en tres de los cuatro casos y que solo falla cuando el cliente no paga con QR y no lleva vaso. Esa fila es la que conviene anunciar en el cartel: «sin QR y sin vaso, no hay promo». La tabla no solo calcula: también ayuda a comunicar la regla sin ambigüedad.')],
 9: [H2('Tautologías que se usan todos los días'),
     P('Algunas tautologías son razonamientos que usamos sin darnos cuenta. ((p → q) ∧ p) → q es la forma del MPP: si su tabla da V en las ocho filas —en este caso, en las cuatro, porque tiene dos variables—, el razonamiento es válido en cualquier situación. En la Clase 12 vas a usar esta idea: un razonamiento es válido cuando el condicional «premisas → conclusión» es una tautología.'),
     P('Al revés, una regla de negocio que resulta contradicción nunca se activa. Detectarlo con una tabla antes de programarla ahorra horas de buscar por qué un descuento «no funciona».')],
 10: [H2('De Morgan en los carteles'),
      P('El cartel dice «se aceptan efectivo o QR» (p ∨ q). ¿Qué significa que el cartel sea falso? Por De Morgan, ¬(p ∨ q) ≡ ¬p ∧ ¬q: no se acepta efectivo y no se acepta QR. Y si el cartel dijera «hay stock y hay precio cargado» (p ∧ q), su negación sería «no hay stock o no hay precio cargado»: alcanza con que falle una de las dos. Negar bien una regla es indispensable para escribir el camino Sino de una decisión en la Unidad 3.')],
 11: [H2('Del cuantificador al algoritmo'),
      P('Comprobar un «para todo» sobre un conjunto finito es recorrer todos sus elementos y detenerse en el primero que no cumple. Comprobar un «existe» es recorrerlos hasta encontrar uno que cumple. En la Unidad 3 vas a escribir esos recorridos como ciclos: un ciclo que revisa todos los precios del menú es, en el fondo, la verificación de una proposición cuantificada.'),
      P('Por eso, cuando un enunciado dice «todos» o «alguno», conviene preguntarse de entrada: ¿qué conjunto se recorre?, ¿qué propiedad se mira?, ¿qué resultado se espera si aparece un contraejemplo?')],
 12: [H2('Inducción: útil, pero no segura'),
      P('Ña Rosa probó tres chipas de la nueva tanda y estaban bien cocidas; concluye que toda la tanda está bien. Es un razonamiento inductivo: generaliza a partir de casos observados. Puede ser una buena decisión práctica, pero la conclusión es probable, no segura: la cuarta chipa podría estar cruda. En programación pasa lo mismo con las pruebas: que un algoritmo funcione con tres datos no demuestra que funcione con todos. Por eso se eligen casos frontera, que son los que tienen más chances de mostrar un error.')],
 13: [H2('Generalidades: qué tienen en común todos los algoritmos'),
      P('Todo algoritmo tiene entradas (los datos que recibe), un proceso (lo que hace con ellos) y salidas (los resultados que entrega), aunque alguno de los tres sea muy simple. Además, se escribe para alguien que lo ejecuta —una persona o una máquina— y debe poder seguirse sin preguntar nada. Esa es la razón de las tres características: precisión, finitud y definición.')],
 14: [H2('Del diagrama al pseudocódigo'),
      P('La traducción también funciona al revés. Ante un diagrama, se recorre el flujo de arriba hacia abajo y cada figura se convierte en una línea: el óvalo de arriba en Inicio, cada paralelogramo en Leer o Escribir según la flecha de los datos, cada rectángulo en una asignación y el óvalo de abajo en Fin. Si el diagrama tiene un rombo, aparece una decisión, que vas a escribir con Si… Entonces en la Clase 17.')],
 15: [H2('Tipos de datos y operaciones permitidas'),
      P('Cada tipo de dato admite ciertas operaciones. Con números se suma, se resta, se multiplica, se divide y se compara. Con textos se compara (igual o distinto) y se puede unir uno con otro, pero no tiene sentido multiplicarlos. Con valores lógicos se opera con Y, O y NO. Elegir el tipo correcto evita errores: la cantidad de chipas es un número entero, el precio promedio puede tener decimales, el medio de pago es un texto y «¿aplica descuento?» es un valor lógico.'),
      TABLA(['Dato', 'Tipo', 'Operaciones que tienen sentido'], [
          ['cantidad de chipas', 'numérico entero', '+, −, *, comparación'], ['promedio de ventas', 'numérico con decimales', '/, comparación'],
          ['medio de pago', 'texto', '=, <>'], ['¿aplica descuento?', 'lógico', 'Y, O, NO']])],
 16: [H2('Una prueba de escritorio que encuentra un error'),
      P('Un estudiante escribió: Leer precio / total ← precio * cantidad / Leer cantidad / Escribir total. En la prueba de escritorio, al llegar a la segunda línea, la columna de cantidad está vacía: no se puede calcular total. El error no es de cuenta, es de orden: la lectura de la cantidad tiene que ir antes del cálculo. La prueba de escritorio lo encontró sin necesidad de ejecutar nada, que es justamente su función.'),
      P('Con el orden corregido —Leer precio / Leer cantidad / total ← precio * cantidad / Escribir total— y los datos precio = 4000 y cantidad = 5, la tabla termina con total = 20000.')],
 17: [H2('Decisiones y conjuntos'),
      P('Una decisión divide los datos posibles en dos conjuntos: los que hacen V la condición y los que la hacen F. Con Si total >= 50000, el primer conjunto es el de las compras de 50000 o más, y el segundo, el de las menores. Los dos conjuntos son disjuntos y su unión es el universo de todas las compras posibles: exactamente lo que garantiza el Si… Sino, que ejecuta un solo camino por dato.'),
      P('Pensar la decisión como una partición del universo ayuda a elegir los datos de prueba: al menos uno de cada conjunto, más el valor frontera, que es el que está en el borde entre los dos.')],
 18: [H2('Decisiones con NO'),
      P('A veces es más claro escribir la condición negada. «Si no hay stock, avisar» se escribe Si NO (stock > 0) Entonces Escribir "sin stock" FinSi. Es equivalente a Si stock <= 0, y cualquiera de las dos es correcta. Para negar una condición compuesta se aplica De Morgan: NO ((total >= 50000) Y (medioPago = "QR")) es lo mismo que (total < 50000) O (medioPago <> "QR"). Elegí la forma que se lea con menos esfuerzo y comprobala con un dato de cada caso.')],
 19: [H2('Mientras o Para: cómo elegir'),
      P('Si el enunciado dice cuántas vueltas hay —«los 5 días hábiles», «las 12 chipas de la docena»—, conviene Para: el contador se maneja solo. Si la cantidad depende de los datos —«hasta que se ingrese 0», «mientras haya clientes»—, corresponde Mientras. Usar Para cuando no se sabe cuántas vueltas habrá obliga a inventar un número; usar Mientras cuando sí se sabe obliga a manejar el contador a mano y abre la puerta a olvidar el incremento.')],
 20: [H2('El centinela debe ser un valor imposible'),
      P('El centinela tiene que ser un valor que nunca aparezca como dato real. El 0 sirve para las ventas porque no existe una venta de 0 guaraníes. Para registrar temperaturas, en cambio, el 0 sería un mal centinela, porque una temperatura de 0 grados es un dato posible; allí convendría, por ejemplo, −999. Elegir mal el centinela hace que el algoritmo termine antes de tiempo y pierda datos sin dar ningún aviso.')],
}

DESC = {n: 'Segundo bloque de ampliación: «%s».' % b[0]['text'] for n, b in EXTRA.items()}


def aplicar(C, LOG):
    for n, bloques in EXTRA.items():
        C[n]['cuerpo'].extend(bloques)
        LOG.append((n, 'C%d-A2' % n, DESC[n]))

EXTRA3 = {
 2: [P('Un detalle que suele aparecer en las evaluaciones: ¿cuántos subconjuntos propios tiene un conjunto de n elementos? Todos menos el propio conjunto: 2ⁿ − 1. Con {chipa, mixta, coquito} son 8 − 1 = 7. Si además se excluye el vacío, quedan 2ⁿ − 2 = 6.')],
 6: [P('Esta habilidad —decidir qué se puede afirmar con precisión y qué no— es la base de toda la unidad: sin proposiciones bien formadas no hay tablas de verdad ni razonamientos válidos.'), P('Un último consejo práctico: cuando dudes si una oración es proposición, intentá anteponerle «es verdad que…». «Es verdad que el coquito cuesta G. 500» tiene sentido; «es verdad que ¿hay chipa?» o «es verdad que traé el vuelto» no lo tienen. Si la frase resultante suena absurda, la oración original no era una proposición. La prueba no reemplaza el criterio, pero ayuda a decidir rápido.')],
 7: [P('Los paréntesis cambian el significado. ¬(p ∧ q) dice «no es cierto que haya las dos cosas», mientras que ¬p ∧ q dice «no hay p, pero sí hay q». Con p = V y q = V, la primera es F y la segunda también; con p = F y q = V, la primera es V y la segunda también; pero con p = V y q = F, la primera es V y la segunda es F. Una sola fila distinta alcanza para que dos fórmulas no digan lo mismo.')],
 8: [P('Antes de entregar una tabla, revisá tres cosas: que tenga 2ⁿ filas, que el orden sea el estándar y que la columna final corresponda al conectivo principal.')],
 9: [P('Recordá también que la clasificación es de la fórmula, no de los hechos: una tautología es verdadera aunque no sepamos si hay harina, queso o chipa.'), P('Por último, un control para tablas de tres variables: en el orden estándar, la columna de p tiene cuatro V seguidas de cuatro F; la de q, dos V, dos F, dos V, dos F; y la de r alterna una a una. Si alguna de las tres columnas no sigue ese patrón, falta o sobra una fila y la clasificación no es confiable. Hacé este control antes de escribir la primera columna auxiliar: corregir después cuesta mucho más.')],
 10: [P('Las equivalencias también sirven para simplificar. ¬(¬p ∧ ¬q) parece complicada, pero por De Morgan es ¬¬p ∨ ¬¬q, y por doble negación, p ∨ q: «no es cierto que no haya ni chipa ni cocido» quiere decir, simplemente, «hay chipa o hay cocido».')],
 11: [P('En resumen: el universal se demuestra revisando todos los elementos y se refuta con un contraejemplo; el existencial se demuestra con un ejemplo y se refuta revisando todos.'), P('Un ejemplo con el curso. Sea A el conjunto de estudiantes de tu sección y t(x) = «x tiene celular». ∀x: t(x) afirma que todos tienen; para refutarlo basta encontrar a una persona sin celular. ∃x: ¬t(x) es justamente su negación: «alguien no tiene celular». Las dos proposiciones no pueden ser verdaderas a la vez ni falsas a la vez: una es la negación de la otra, igual que p y ¬p.'),
      P('Y si el conjunto de referencia es vacío, el «para todo» es verdadero por defecto, porque no hay ningún contraejemplo posible. Es una convención de la lógica que vuelve en programación: un ciclo que revisa una lista vacía no encuentra ningún elemento que falle.')],
 12: [P('Para escribir una demostración ordenada: numerá las premisas, agregá una línea por cada paso y citá a la derecha la regla y los números de línea que usaste. Quien lea la demostración tiene que poder controlarla sin preguntarte nada.')],
 15: [P('Un último cuidado con la división: dividir por cero no tiene resultado. Si una expresión puede llegar a tener un divisor igual a 0 —por ejemplo, un promedio cuando no se cargó ningún dato—, el algoritmo tiene que preverlo con una decisión antes de dividir, como vas a ver en la Clase 20.')],
 16: [P('La prueba de escritorio también sirve para comunicar: una tabla bien hecha le muestra a otra persona exactamente qué hace el algoritmo con cada dato, sin necesidad de leer el pseudocódigo línea por línea.')],
 17: [P('Por último, el orden de las acciones dentro de cada camino importa. En el descuento del copetín, el cálculo de pagar tiene que estar dentro del Si, y el Escribir, después del FinSi, para que se ejecute en los dos casos. Si el Escribir quedara dentro del camino V, una compra de 30000 no mostraría ningún resultado: el algoritmo terminaría en silencio.')],
 18: [P('Si agregás una categoría nueva, revisá otra vez las fronteras: cada límite tiene que pertenecer a una sola categoría.'), H2('Una clasificación con cuatro categorías'),
      P('Ña Rosa clasifica los pedidos de delivery por distancia: hasta 2 km, «cerca» (sin recargo); de más de 2 a 5 km, «media» (recargo de 3000); de más de 5 a 10 km, «lejos» (recargo de 6000); más de 10 km, «fuera de zona». Con decisiones anidadas, se pregunta en orden: Si distancia <= 2, «cerca»; Sino, Si distancia <= 5, «media»; Sino, Si distancia <= 10, «lejos»; Sino, «fuera de zona». Son tres preguntas para cuatro categorías: siempre hace falta una pregunta menos que categorías, porque la última es «todo lo que queda».'),
      P('Datos de prueba: 2 (frontera de «cerca»), 3, 5 (frontera de «media»), 8, 10 (frontera de «lejos») y 12. Seis datos para cuatro categorías y tres fronteras.')],
 19: [P('Con esas tres respuestas escritas, el ciclo prácticamente se escribe solo.'), P('Antes de escribir un ciclo, respondé tres preguntas: ¿qué se repite?, ¿cuántas veces o hasta cuándo?, ¿qué variable cambia en cada vuelta? Si alguna respuesta no está clara, el ciclo todavía no está listo para escribirse.')],
 20: [P('Por último, el lugar de la segunda lectura importa. En el ciclo con centinela, Leer venta aparece dos veces: una antes del Mientras, para tener el primer dato, y otra al final del cuerpo del ciclo, para traer el siguiente. Si la segunda lectura se pone al principio del cuerpo, el primer dato se pierde.')],
}


def aplicar3(C, LOG):
    for n, bloques in EXTRA3.items():
        C[n]['cuerpo'].extend(bloques)
        LOG.append((n, 'C%d-A3' % n, 'Tercer bloque de ampliación (mínimo de 750 palabras).'))

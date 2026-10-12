# -*- coding: utf-8 -*-
"""Las 21 prácticas de la Edición Esencial de Algorítmica 2.º, con datos NUEVOS respecto de cada clase:
el contexto de laboratorio es la Librería escolar Arandu (las clases y las actividades usan el Copetín Karumbé).
Formato (modelo Software 1.º / Algorítmica 3.º): Competencia · Lo que necesitás saber · Antes de empezar ·
Actividades (objetivo → modelo → pasos → punto de control) · Transferencia (donde hace falta) · Desafío final.
Los puntos de control no revelan resultados: piden contrastar con lo anticipado o con un control cruzado.
Todo el pseudocódigo de las prácticas 1 a 14 se ejecutó en PSeInt 20250314, perfil Flexible
(programas en algoritmica_2_esencial/pseint/). 'sol' alimenta el Solucionario."""

PSEINT = 'PSeInt'
PAPEL = 'papel y lápiz'
EXPLORADOR = 'Explorador de archivos de Windows y Bloc de notas'
ACCESS = 'Microsoft Access'
VER = ' (Ejecutado en PSeInt 20250314, perfil Flexible.)'


def E(*lineas):
    """Esqueleto o modelo de código: cada línea se compone en monoespaciado."""
    return ['§' + x for x in lineas]


ARTICULOS = [('LIB-01', 'Cuaderno', '8000', 'papelería', '35'), ('LIB-02', 'Bolígrafo', '3000', 'escritura', '120'),
             ('LIB-03', 'Lápiz', '2000', 'escritura', '90'), ('LIB-04', 'Regla', '4000', 'geometría', '18'),
             ('LIB-05', 'Carpeta', '15000', 'papelería', '12'), ('LIB-06', 'Resaltador', '6000', 'escritura', '44'),
             ('LIB-07', 'Goma', '1500', 'escritura', '59'), ('LIB-08', 'Compás', '12000', 'geometría', '7')]
assert sum(int(a[2]) * int(a[4]) for a in ARTICULOS) == 1508500

PR = {}

# =============================================================== UNIDAD 1
PR[1] = dict(
 titulo='La compra de útiles: del algoritmo en papel al programa en PSeInt', entorno=PSEINT,
 competencia='Escribir un algoritmo secuencial con sus tipos de datos, ejecutarlo en PSeInt y verificar el resultado con un cálculo hecho a mano.',
 saber=['Un algoritmo secuencial ejecuta sus pasos en orden: leer los datos, calcular y mostrar. Antes de ejecutar, conviene saber qué resultado esperar.',
        'En PSeInt, Definir declara el tipo de cada variable (Entero, Real, Caracter, Logico), Leer guarda lo que escribe el usuario, <- asigna y Escribir muestra.'],
 antes='Abrí PSeInt y, en Configurar → Opciones del Lenguaje (perfiles), seleccioná el perfil Flexible: es el perfil de referencia de este libro. En la Librería escolar Arandu el cuaderno cuesta 8.000 y el bolígrafo 3.000.',
 acts=[
  dict(titulo='El algoritmo en papel', objetivo='Escribir en pseudocódigo el algoritmo que lee cuántos cuadernos y cuántos bolígrafos compra un cliente, calcula el total y el vuelto de su pago.',
       modelo=('Estructura que debe tener tu algoritmo', ['1) Definir las variables y su tipo.', '2) Leer las dos cantidades.', '3) Calcular el total con los precios de la librería.', '4) Leer el pago y calcular el vuelto.', '5) Mostrar el total y el vuelto.']),
       pasos=['Elegí nombres claros para las variables (cantCuad, cantBol, total, pago, vuelto) y decidí el tipo de cada una.', 'Escribí el algoritmo completo en tu carpeta, con sangría.', 'Calculá a mano el total y el vuelto para un cliente que compra 3 cuadernos y 4 bolígrafos y paga con 50.000. Anotalos al costado.'],
       control='Cada variable tiene un tipo justificado y tu cálculo a mano está anotado antes de pasar a la computadora.'),
  dict(titulo='Ejecutarlo en PSeInt', objetivo='Pasar el algoritmo a PSeInt, ejecutarlo con dos clientes y comparar con el cálculo a mano.',
       modelo=('Esqueleto para completar (las líneas «…» las escribís vos)', E('Algoritmo CompraUtiles', '    Definir cantCuad, cantBol, total, pago, vuelto Como Entero', '    Escribir "Cantidad de cuadernos:"', '    Leer cantCuad', '    …', '    total <- …', '    Escribir "Total a pagar: ", total', '    …', '    vuelto <- …', '    Escribir "Vuelto: ", vuelto', 'FinAlgoritmo')),
       pasos=['Completá el esqueleto con lo que escribiste en papel.', 'Ejecutalo con el cliente de la Actividad 1 (3 cuadernos, 4 bolígrafos, pago de 50.000).', 'Ejecutalo con un segundo cliente que elijas vos; calculá su total a mano antes de ejecutar.', 'Guardá el archivo como CompraUtiles.psc.'],
       control='En los dos clientes, el total y el vuelto de la pantalla coinciden con los que calculaste antes de ejecutar.'),
 ],
 desafio='Agregá una variable Real que calcule el precio medio por artículo (total dividido por la cantidad de artículos). Probalo con 3 cuadernos y 5 bolígrafos y explicá por qué esa variable no puede ser Entero en general.',
 sol=dict(resultado='Act. 1: variables Entero (guaraníes y unidades sin decimales). 3 × 8.000 + 4 × 3.000 = 24.000 + 12.000 = 36.000; vuelto 50.000 − 36.000 = 14.000. Act. 2: la pantalla muestra «Total a pagar: 36000» y «Vuelto: 14000»; el segundo cliente se corrige con la cuenta del estudiante. Desafío: (24.000 + 15.000) / 8 = 4.875; con otras cantidades la división puede no ser exacta (3 cuadernos y 4 bolígrafos dan 5.142,857…), por eso el promedio va como Real.' + VER,
          errores='Leer el pago después de calcular el vuelto; escribir el precio dentro de Leer; usar el carácter ← en lugar de <- (PSeInt no lo reconoce); no anotar el resultado esperado antes de ejecutar; definir el precio medio como Entero.'))

PR[2] = dict(
 titulo='Descuentos y avisos con Si simple', entorno=PSEINT,
 competencia='Programar decisiones con Si simple y comprobar los dos caminos (condición verdadera y falsa), incluido el caso límite.',
 saber=['El bloque de un Si simple se ejecuta solo cuando la condición es Verdadera; si es Falsa, se saltea y el algoritmo sigue.',
        'Para probar una decisión hacen falta al menos tres datos: uno que cumpla, uno que no cumpla y el valor exacto del límite.'],
 antes='La Librería Arandu descuenta el 10 % en las compras de 100.000 o más, y avisa cuando quedan menos de 10 carpetas.',
 acts=[
  dict(titulo='El descuento de la librería', objetivo='Programar el descuento del 10 % con un Si simple y probarlo con tres totales.',
       modelo=('Esqueleto para completar', E('Algoritmo DescuentoLibreria', '    Definir total Como Entero', '    Escribir "Total de la compra:"', '    Leer total', '    Si … Entonces', '        total <- …', '        Escribir "Se aplicó el 10 % de descuento"', '    FinSi', '    Escribir "Total final: ", total', 'FinAlgoritmo')),
       pasos=['Antes de ejecutar, armá una tabla con tres totales: 120.000, 95.000 y 100.000, y anotá qué debería mostrar cada uno.', 'Completá la condición y el cálculo, y ejecutá con los tres totales.', 'Marcá en la tabla cuál de los tres es el caso límite y por qué importa probarlo.'],
       control='Los tres resultados coinciden con tu tabla y el caso límite tomó el camino que anticipaste.'),
  dict(titulo='Dos avisos independientes', objetivo='Escribir dos Si simples seguidos para controlar el stock de carpetas.',
       modelo=('Reglas del control de stock', ['Si el stock es menor que 10, mostrar «Reponer carpetas».', 'Si el stock es 0, mostrar además «No vender: sin stock».', 'Siempre, al final, mostrar «Control terminado».']),
       pasos=['Escribí el algoritmo AvisoStock con dos Si simples (no anidados).', 'Anticipá qué mensajes salen con stock 7, 0 y 25.', 'Ejecutá con los tres valores.'],
       control='Para cada stock salen exactamente los mensajes anticipados, y «Control terminado» aparece en las tres ejecuciones.'),
 ],
 desafio='Ejecutá el descuento con un total de 100.005 y anotá qué pasa. Corregilo con trunc(...) en la asignación y explicá en una línea qué hace trunc.',
 sol=dict(resultado='Act. 1: 120.000 → «Se aplicó el 10 % de descuento» y «Total final: 108000»; 95.000 → «Total final: 95000»; 100.000 (límite, >= lo incluye) → 90000. Act. 2: stock 7 → «Reponer carpetas» y «Control terminado»; stock 0 → los tres mensajes; stock 25 → solo «Control terminado». Desafío: con 100.005 el resultado sería 90.004,5 y PSeInt se detiene con «ERROR 314: No coinciden los tipos, el valor a asignar debe ser un entero.»; con total <- trunc(total − total * 0.10) muestra 90004 (trunc descarta los decimales).' + VER,
          errores='Usar > en lugar de >= (100.000 queda sin descuento); anidar el segundo Si dentro del primero; escribir la condición como monto => 100000; olvidar que el 10 % puede no ser entero.'))

PR[3] = dict(
 titulo='Envíos y pagos con Si… Sino', entorno=PSEINT,
 competencia='Programar una decisión de dos caminos con Si… Sino y diseñar los casos de prueba de cada camino.',
 saber=['El Si… Sino ejecuta siempre exactamente uno de sus dos bloques.',
        'Un buen caso de prueba se elige antes de ejecutar y se anota con el resultado esperado.'],
 antes='La librería envía sin cargo los pedidos de 150.000 o más; a los demás les suma 15.000 de envío.',
 acts=[
  dict(titulo='El cargo de envío', objetivo='Programar el cargo de envío con un Si… Sino y probar los dos caminos.',
       modelo=('Esqueleto para completar', E('Algoritmo EnvioLibreria', '    Definir total Como Entero', '    Leer total', '    Si … Entonces', '        Escribir "Envío sin cargo"', '    Sino', '        total <- …', '        Escribir "Se suma el envío: 15000"', '    FinSi', '    Escribir "Total final: ", total', 'FinAlgoritmo')),
       pasos=['Elegí tres totales de prueba: uno por debajo, uno por encima y el valor exacto del límite. Anotá el resultado esperado de cada uno.', 'Completá el esqueleto y ejecutá con tus tres totales.', 'Probá también con 98.000.'],
       control='Los cuatro totales finales coinciden con lo que anotaste antes de ejecutar.'),
  dict(titulo='¿Alcanza el pago?', objetivo='Programar un control de pago que muestre el vuelto o cuánto falta.',
       modelo=('Comportamiento esperado', ['Si el pago alcanza: mostrar «Vuelto: » y el vuelto.', 'Si no alcanza: mostrar «Faltan: » y la diferencia.', 'Nunca debe mostrarse un vuelto negativo.']),
       pasos=['Escribí el algoritmo ControlPago con un Si… Sino.', 'Probalo con un total de 64.000 y pagos de 70.000 y de 50.000.', 'Agregá un tercer caso de pago exacto y decidí qué camino debería tomar.'],
       control='En ninguna de las tres ejecuciones aparece un número negativo, y el pago exacto tomó el camino que habías decidido.'),
 ],
 desafio='Combiná las dos actividades en un solo algoritmo: primero calcula el total con o sin envío y después controla el pago. Probalo con un pedido de 98.000 y un pago de 120.000.',
 sol=dict(resultado='Act. 1: totales menores que 150.000 suman 15.000 («Se suma el envío: 15000»); 150.000 (límite) → «Envío sin cargo», total 150000; 98.000 → total final 113000. Act. 2: 64.000 con 70.000 → «Vuelto: 6000»; con 50.000 → «Faltan: 14000»; pago exacto (64.000) → camino del Entonces con «Vuelto: 0» (pago >= total). Desafío: 98.000 + 15.000 = 113.000; vuelto 120.000 − 113.000 = 7.000.' + VER,
          errores='Elegir casos de prueba que pasan todos por el mismo camino; restar al revés (total − pago); escribir dos Si separados en lugar de Si… Sino; olvidar actualizar total en el Sino.'))

PR[4] = dict(
 titulo='Condiciones compuestas: descuento estudiantil y medios de pago', entorno=PSEINT,
 competencia='Escribir condiciones compuestas con Y, O y NO, usar variables lógicas y verificar el resultado con la tabla de verdad.',
 saber=['Y es verdadera solo si las dos condiciones lo son; O, si al menos una lo es; NO invierte el valor.',
        'Una variable Logico guarda Verdadero o Falso. En PSeInt se puede leer escribiendo Verdadero o Falso.'],
 antes='La librería hace un 10 % de descuento a quien presenta carnet de estudiante y compra 50.000 o más. Acepta efectivo, QR y tarjeta.',
 acts=[
  dict(titulo='El descuento estudiantil', objetivo='Programar una condición con Y sobre una variable lógica y un monto.',
       modelo=('Esqueleto para completar', E('Algoritmo DescuentoEstudiante', '    Definir total Como Entero', '    Definir esEstudiante Como Logico', '    Leer total', '    Leer esEstudiante', '    Si (…) Y (…) Entonces', '        total <- total - total * 0.10', '        Escribir "Descuento estudiantil aplicado"', '    Sino', '        Escribir "Sin descuento"', '    FinSi', '    Escribir "Total final: ", total', 'FinAlgoritmo')),
       pasos=['Armá la tabla de verdad de la condición con sus cuatro combinaciones y marcá en cuál hay descuento.', 'Completá el esqueleto y ejecutá tres casos: 65.000 con Verdadero, 65.000 con Falso y 40.000 con Verdadero.', 'Ubicá cada ejecución en una fila de tu tabla.'],
       control='Cada ejecución cae en la fila de la tabla que anticipaste, y solo la combinación V-V aplica el descuento.'),
  dict(titulo='Medio de pago y stock', objetivo='Combinar O y NO en una decisión anidada.',
       modelo=('Reglas', ['Si NO hay stock (NO (stock > 0)): «Venta rechazada: sin stock».', 'Si hay stock y el medio es efectivo O QR O tarjeta: «Venta aceptada».', 'Si hay stock y el medio es otro: «Medio de pago no aceptado».']),
       pasos=['Definí medio como Caracter y stock como Entero.', 'Escribí el algoritmo MedioDePago con un Si… Sino que tiene otro Si… Sino adentro.', 'Probalo con: QR y stock 5; cheque y stock 5; efectivo y stock 0.'],
       control='Los tres casos producen tres mensajes distintos, y el caso sin stock no llega a preguntar por el medio de pago.'),
 ],
 desafio='Cambiá el Y del descuento estudiantil por O y volvé a ejecutar los tres casos de la Actividad 1. ¿Qué casos cambian? Respondé con la tabla de verdad.',
 sol=dict(resultado='Act. 1: tabla V-V → descuento; V-F, F-V, F-F → sin descuento. 65.000 y Verdadero → «Descuento estudiantil aplicado», 58500; 65.000 y Falso → «Sin descuento», 65000; 40.000 y Verdadero → «Sin descuento», 40000. Act. 2: QR/5 → «Venta aceptada»; cheque/5 → «Medio de pago no aceptado»; efectivo/0 → «Venta rechazada: sin stock». Desafío: con O, los casos 65.000-Falso (V O F) y 40.000-Verdadero (F O V) pasan a tener descuento: 58.500 y 36.000.' + VER,
          errores='Escribir "QR" sin comillas o con otra capitalización ("qr" no es igual a "QR"); usar 1/0 en lugar de una variable lógica; olvidar los paréntesis en cada comparación; poner el control de stock después del de medio de pago.'))

PR[5] = dict(
 titulo='Clasificar pedidos y armar el menú de la librería', entorno=PSEINT,
 competencia='Elegir entre Si anidado y Segun según el tipo de decisión, y programar ambos con sus casos límite.',
 saber=['Para rangos (menos de, entre, más de) se usa Si anidado; para valores exactos (1, 2, 3…) conviene Segun.',
        'En un Si anidado se toma el primer camino cuya condición es verdadera; el orden de las preguntas importa.'],
 antes='La librería clasifica los pedidos de cuadernos: menos de 12, minorista; de 12 a 49, por docena; 50 o más, mayorista.',
 acts=[
  dict(titulo='Tipo de pedido con Si anidado', objetivo='Programar la clasificación en tres categorías y probar los dos límites.',
       modelo=('Esqueleto para completar', E('Algoritmo TipoPedido', '    Definir cantidad Como Entero', '    Leer cantidad', '    Si cantidad < … Entonces', '        Escribir "Pedido minorista"', '    Sino', '        Si … Entonces', '            Escribir "Pedido por docena"', '        Sino', '            Escribir "Pedido mayorista"', '        FinSi', '    FinSi', 'FinAlgoritmo')),
       pasos=['Antes de ejecutar, armá una tabla con las cantidades 11, 12, 49 y 50 y la categoría que les corresponde según la regla.', 'Completá las dos condiciones y ejecutá con las cuatro cantidades.', 'Explicá en una línea por qué la segunda condición no necesita preguntar «cantidad >= 12».'],
       control='Las cuatro cantidades límite caen en la categoría de tu tabla.'),
  dict(titulo='El menú con Segun', objetivo='Programar un menú de cinco artículos con Segun y De Otro Modo.',
       modelo=('Menú de la caja', ['1 Cuaderno 8.000 · 2 Bolígrafo 3.000 · 3 Lápiz 2.000 · 4 Regla 4.000 · 5 Carpeta 15.000', 'Otra opción: «Opción inválida».', 'Escribí cada opción del Segun en su propia línea: 1: y abajo, con sangría, la asignación del precio.']),
       pasos=['Escribí el algoritmo MenuLibreria: guardá el precio en una variable dentro de cada opción y mostralo después del FinSegun solo si se eligió una opción válida.', 'Probalo con las opciones 4 y 7.', 'Probá también la opción 0.'],
       control='Las opciones válidas muestran el precio del menú y las inválidas muestran un solo mensaje, sin un precio debajo.'),
 ],
 desafio='Reescribí el menú con Si anidados y contá cuántas líneas tiene cada versión. ¿Cuál es más fácil de leer y por qué?',
 sol=dict(resultado='Act. 1: 11 → «Pedido minorista»; 12 y 49 → «Pedido por docena»; 50 → «Pedido mayorista». La segunda condición es cantidad < 50: si se llegó al Sino, ya se sabe que cantidad >= 12. Act. 2: opción 4 → «Precio: 4000»; 7 y 0 → «Opción inválida». La variable precio arranca en 0 y se muestra solo si precio > 0. Desafío: la versión con Si anidados necesita cinco niveles de Si… Sino; el Segun es más legible para valores exactos.' + VER,
          errores='Poner la condición del mayorista primero con < (el orden cambia el resultado); escribir 12 <= cantidad < 50 (no es válido en PSeInt); escribir la acción en la misma línea que el «1:» y el Si; mostrar «Precio: 0» para las opciones inválidas.'))

PR[6] = dict(
 titulo='Validar datos y llegar a la meta con ciclos', entorno=PSEINT,
 competencia='Usar Repetir… Hasta Que para validar datos y Mientras para acumular hasta una meta, con contadores y acumuladores.',
 saber=['Repetir… Hasta Que se ejecuta al menos una vez y corta cuando la condición es Verdadera; Mientras puede no ejecutarse nunca y sigue mientras la condición es Verdadera.',
        'Un contador suma 1 en cada vuelta; un acumulador suma un valor.'],
 antes='La librería tiene 12 carpetas en stock y se fija una meta de venta de 200.000 por turno.',
 acts=[
  dict(titulo='Validar la cantidad', objetivo='Pedir una cantidad hasta que esté entre 1 y el stock disponible, contando los intentos.',
       modelo=('Esqueleto para completar', E('Algoritmo ValidarCantidad', '    Definir stock, cantidad, intentos Como Entero', '    stock <- 12', '    intentos <- 0', '    Repetir', '        Escribir "Cantidad de carpetas (1 a ", stock, "):"', '        Leer cantidad', '        intentos <- …', '    Hasta Que (…) Y (…)', '    Escribir "Cantidad aceptada: ", cantidad, " en ", intentos, " intentos"', 'FinAlgoritmo')),
       pasos=['Completá la condición de salida: el ciclo corta cuando la cantidad es válida.', 'Ejecutá ingresando, en orden, 0, 15 y 5.', 'Anticipá cuántos intentos va a informar antes de ingresar el último dato.'],
       control='El programa rechaza los datos inválidos sin mensaje de error de PSeInt y la cantidad de intentos coincide con tu anticipación.'),
  dict(titulo='La meta del turno', objetivo='Acumular importes de tickets con Mientras hasta alcanzar la meta y contar los tickets.',
       modelo=('Datos del turno (en este orden)', ['45.000 · 60.000 · 38.000 · 72.000 · 20.000']),
       pasos=['Escribí el algoritmo MetaLibreria con un acumulador, un contador y un Mientras acumulado < 200000.', 'Hacé primero la prueba de escritorio en una tabla (vuelta, ticket, acumulado, tickets).', 'Ejecutá ingresando los importes en orden; si el programa deja de pedir datos, no ingreses más.'],
       control='El programa deja de pedir importes en la misma vuelta en que tu prueba de escritorio supera la meta, y muestra el mismo acumulado.'),
 ],
 desafio='¿Qué pasaría con la Actividad 2 si la meta fuera 0? Cambiala, ejecutá y explicá el resultado con la diferencia entre Mientras y Repetir.',
 sol=dict(resultado='Act. 1: condición Hasta Que (cantidad >= 1) Y (cantidad <= stock); con 0, 15 y 5 → «Cantidad aceptada: 5 en 3 intentos». Act. 2: 45.000 → 105.000 → 143.000 → 215.000: corta en el 4.º ticket; «Meta alcanzada con 4 tickets: 215000» (el quinto importe no se pide). Desafío: con meta 0 la condición 0 < 0 es Falsa desde el inicio: el Mientras no se ejecuta y muestra «Meta alcanzada con 0 tickets: 0»; un Repetir habría pedido al menos un ticket.' + VER,
          errores='Escribir la condición de Repetir al revés (condición de permanencia en lugar de salida); olvidar incrementar intentos; inicializar acumulado dentro del ciclo; ingresar los cinco importes aunque el programa ya haya cortado.'))

PR[7] = dict(
 titulo='La semana de la librería: Para, acumulador, centinela y bandera', entorno=PSEINT,
 competencia='Resolver problemas de la semana con ciclo Para, acumuladores, contadores, centinela y banderas, verificando con prueba de escritorio.',
 saber=['El Para se usa cuando se conoce la cantidad de repeticiones; el centinela, cuando la carga termina con un valor especial.',
        'Una bandera es una variable lógica que arranca en Falso y pasa a Verdadero cuando ocurre algo.'],
 antes='La librería abre de lunes a sábado. Ventas de la semana: 180.000 · 240.000 · 150.000 · 310.000 · 290.000 · 210.000.',
 acts=[
  dict(titulo='Total y promedio con Para', objetivo='Acumular las seis ventas con un Para y calcular el promedio.',
       modelo=('Esqueleto para completar', E('Algoritmo SemanaLibreria', '    Definir venta, total, i Como Entero', '    Definir promedio Como Real', '    total <- 0', '    Para i <- 1 Hasta 6 Con Paso 1 Hacer', '        Leer venta', '        total <- …', '    FinPara', '    promedio <- …', '    Escribir "Total: ", total', '    Escribir "Promedio: ", promedio', 'FinAlgoritmo')),
       pasos=['Calculá a mano el total y el promedio y anotalos.', 'Completá el esqueleto y ejecutá con las seis ventas.', 'Explicá por qué total arranca en 0 antes del ciclo y no dentro.'],
       control='El total y el promedio de la pantalla coinciden con los anotados.'),
  dict(titulo='Los tickets del turno con centinela', objetivo='Cargar importes hasta que se ingrese 0 y mostrar cuántos tickets hubo y el total.',
       modelo=('Datos del turno', ['12.000 · 8.500 · 30.000 · 4.500 · 0 (centinela)']),
       pasos=['Escribí el algoritmo TicketsDelTurno: una lectura antes del Mientras y otra al final del cuerpo.', 'Ejecutá con los datos del turno.', 'Ejecutá otra vez ingresando 0 de entrada.'],
       control='El 0 no se cuenta como ticket, y la ejecución que empieza con 0 informa un turno vacío sin error.'),
  dict(titulo='Contador y bandera en el mismo recorrido', objetivo='Contar los días que alcanzaron el promedio y detectar con una bandera si hubo un día por debajo de 160.000.',
       modelo=('Qué tiene que informar', ['Cuántos días alcanzaron 230.000 (el promedio de la Actividad 1).', 'Si hubo algún día por debajo de 160.000 (bandera) y cuál fue.']),
       pasos=['Escribí el algoritmo ControlSemana con un Para, un contador, una bandera hubo y una variable diaBajo.', 'Hacé la prueba de escritorio con las seis ventas antes de ejecutar.', 'Ejecutá y compará.'],
       control='El contador y la bandera coinciden con tu prueba de escritorio. Si PSeInt marca «Identificador no válido», revisá que ninguna variable se llame igual que el algoritmo.'),
 ],
 desafio='Modificá la Actividad 3 para que también informe el mejor día (número de día y venta) sin usar vectores.',
 sol=dict(resultado='Act. 1: total 1.380.000; promedio 1.380.000 / 6 = 230.000 («Total: 1380000», «Promedio: 230000»). Act. 2: «Tickets: 4  Total: 55000»; con 0 de entrada, «Tickets: 0  Total: 0». Act. 3: «Días que alcanzaron 230000: 3» (martes, jueves y viernes) y «¿Hubo un día por debajo de 160000? VERDADERO  (día 3)». Desafío: mejor día 4 con 310.000 (variables mayor y diaMayor actualizadas dentro del Para). Comprobado también: si el algoritmo se llama igual que una variable (Algoritmo DiaBajo con la variable diaBajo), PSeInt marca «ERROR 48: Identificador no válido».' + VER,
          errores='Inicializar total dentro del ciclo; contar el centinela como ticket; leer solo dentro del Mientras (se procesa el 0); dejar la bandera sin inicializar; usar el nombre del algoritmo como variable.'))

# =============================================================== UNIDAD 2
PR[8] = dict(
 titulo='El vector de precios y la consulta por número', entorno=PSEINT,
 competencia='Declarar, cargar y consultar vectores (incluidos vectores paralelos) validando el índice antes de usarlo.',
 saber=['Un vector se declara con Dimension y cada casillero se identifica por su índice: en el perfil Flexible, de 1 al tamaño.',
        'Dos vectores son paralelos cuando la misma posición describe el mismo objeto: nombres[3] y precios[3] hablan del mismo artículo.'],
 antes='Precios de la librería, en este orden: Cuaderno 8.000 · Bolígrafo 3.000 · Lápiz 2.000 · Regla 4.000 · Carpeta 15.000 · Resaltador 6.000 · Goma 1.500.',
 acts=[
  dict(titulo='Cargar y mostrar', objetivo='Cargar el vector precios[7] con un Para y mostrar elementos por su índice.',
       modelo=('Esqueleto para completar', E('Algoritmo VectorPrecios', '    Definir precios, i Como Entero', '    Dimension precios[7]', '    Para i <- 1 Hasta 7 Con Paso 1 Hacer', '        Leer …', '    FinPara', '    Escribir "Artículo 5: ", …', '    Escribir "Primero y último: ", …, " y ", …', 'FinAlgoritmo')),
       pasos=['Anotá en papel qué valor debería mostrar cada línea de salida.', 'Completá el esqueleto y ejecutá cargando los siete precios en orden.', 'Ejecutá otra vez cargando los precios en orden inverso y explicá qué cambió.'],
       control='Las dos ejecuciones muestran los valores que anticipaste para cada orden de carga.'),
  dict(titulo='Consulta con vectores paralelos', objetivo='Consultar nombre y precio de un artículo por su número, validando que el número exista.',
       modelo=('Comportamiento esperado', ['Se cargan nombres[7] y precios[7] con asignaciones (no con Leer).', 'Se lee un número de artículo.', 'Si está entre 1 y 7, se muestra «nombre: precio»; si no, «No existe ese artículo».']),
       pasos=['Escribí el algoritmo ConsultaArticulo con los dos vectores paralelos.', 'Probalo con los números 6 y 9.', 'Quitá la validación, ejecutá con 9 y copiá el mensaje que da PSeInt. Después volvé a poner la validación.'],
       control='Con la validación, ningún número produce un error de PSeInt; sin ella, el número fuera de rango detiene el programa.'),
 ],
 desafio='Agregá un tercer vector paralelo con el stock de cada artículo y mostrá, para el número consultado, cuántas unidades quedan y cuánto dinero representan.',
 sol=dict(resultado='Act. 1: «Artículo 5: 15000» y «Primero y último: 8000 y 1500»; en orden inverso, el artículo 5 es 2.000 y primero y último pasan a 1.500 y 8.000 (el índice no cambia: cambia el contenido). Act. 2: 6 → «Resaltador: 6000»; 9 → «No existe ese artículo»; sin validación, PSeInt se detiene con «ERROR 303: Subindice (9) fuera de rango (1...7).». Desafío: con stock[7] paralelo (por ejemplo, Resaltador 44), muestra 44 unidades y 44 × 6.000 = 264.000.' + VER,
          errores='Confundir el índice con el valor; usar índice 0 en el perfil Flexible; olvidar declarar Dimension; cargar los vectores paralelos en órdenes distintos; validar con O en lugar de Y.'))

PR[9] = dict(
 titulo='Recorrer el vector de unidades vendidas', entorno=PSEINT,
 competencia='Calcular total, promedio, máximo, mínimo y búsqueda secuencial recorriendo un vector, verificando con prueba de escritorio.',
 saber=['Para el máximo y el mínimo se arranca con el primer elemento y se actualiza cuando aparece uno mayor (o menor), guardando la posición.',
        'La búsqueda secuencial compara elemento por elemento y puede cortar en cuanto encuentra el buscado.'],
 antes='Unidades vendidas en la semana, por artículo (mismo orden que en la Práctica 8): 35 · 120 · 90 · 18 · 12 · 44 · 59.',
 acts=[
  dict(titulo='Total, promedio, máximo y mínimo', objetivo='Recorrer el vector unid[7] y calcular total, promedio, cuántos superan el promedio, máximo y mínimo con sus posiciones.',
       modelo=('Qué tiene que informar', ['Total y promedio de unidades.', 'Cuántos artículos superan el promedio.', 'Mayor y menor, con su posición.']),
       pasos=['Hacé la prueba de escritorio del máximo en una tabla (i, unid[i], mayor, posMayor).', 'Escribí el algoritmo UnidadesSemana: un Para de carga, uno para el total y otro para el resto.', 'Ejecutá con los siete valores.'],
       control='Los seis datos de la pantalla coinciden con tu prueba de escritorio; el total dividido por 7 da exactamente el promedio informado.'),
  dict(titulo='Buscar un artículo por su nombre', objetivo='Programar una búsqueda secuencial que se detenga al encontrar y cuente las comparaciones.',
       modelo=('Esqueleto para completar', E('pos <- 0', 'i <- 1', 'Mientras (i <= 7) Y (pos = 0) Hacer', '    Si nombres[i] = buscado Entonces', '        pos <- i', '    FinSi', '    i <- i + 1', 'FinMientras')),
       pasos=['Completá el algoritmo BuscarArticulo con el vector nombres[7] de la Práctica 8 y el mensaje final (encontrado en la posición… o no está).', 'Buscá «Carpeta», «Compás» y «carpeta» (en minúscula).', 'Anotá cuántas comparaciones hizo cada búsqueda.'],
       control='Una búsqueda que encuentra hace menos comparaciones que una que no encuentra. Explicá con tus palabras el resultado de «carpeta».'),
 ],
 desafio='Ampliá la Actividad 1 para informar también el segundo artículo más vendido, en el mismo recorrido.',
 sol=dict(resultado='Act. 1: «Total: 378  Promedio: 54  Sobre el promedio: 3» (120, 90 y 59) y «Mayor: 120 (posición 2)  Menor: 12 (posición 5)», es decir, Bolígrafo y Carpeta. Act. 2: Carpeta → posición 5 con 5 comparaciones; Compás → no está, 7 comparaciones; «carpeta» → no está: la comparación de cadenas distingue mayúsculas y minúsculas (se retoma en la Práctica 14). Desafío: segundo = 90 (Lápiz).' + VER,
          errores='Inicializar mayor en 0 y menor en 0 (el menor nunca cambia); comparar con >= y quedarse con la última posición del empate; recorrer los 7 elementos aunque ya se encontró; mostrar «no está» dentro del ciclo.'))

PR[10] = dict(
 titulo='La matriz de ventas de la librería', entorno=PSEINT,
 competencia='Cargar y recorrer matrices con ciclos anidados, calcular totales por fila, por columna y general, y facturación con un vector paralelo.',
 saber=['En v[f,c], f es la fila y c la columna. Para recorrer una matriz completa se anidan dos Para.',
        'La suma de los totales de fila y la suma de los totales de columna tienen que dar el mismo total general: es un control automático.'],
 antes='Unidades vendidas de lunes a viernes (filas: Cuaderno, Bolígrafo, Carpeta). Cargá la matriz con los datos de la tabla al final de la práctica.',
 acts=[
  dict(titulo='Cargar la matriz y sumar por fila', objetivo='Cargar v[3,5] fila por fila y mostrar el total de cada artículo.',
       modelo=('Esqueleto para completar', E('Dimension v[3,5]', 'Para f <- 1 Hasta 3 Con Paso 1 Hacer', '    Para c <- 1 Hasta 5 Con Paso 1 Hacer', '        Leer v[f,c]', '    FinPara', 'FinPara', 'Para f <- 1 Hasta 3 Con Paso 1 Hacer', '    totalFila <- 0', '    …', '    Escribir "Fila ", f, ": ", totalFila', 'FinPara')),
       pasos=['Calculá a mano el total de cada fila con la tabla de datos.', 'Completá el esqueleto en el algoritmo MatrizVentas y ejecutá cargando los 15 datos fila por fila.', 'Explicá por qué totalFila vuelve a 0 en cada fila.'],
       control='Los tres totales de fila coinciden con tu cálculo a mano.'),
  dict(titulo='Totales por día y el día con más unidades', objetivo='Recorrer la matriz por columnas, mostrar el total de cada día y detectar el de más unidades.',
       modelo=('Qué tiene que informar', ['El total de cada uno de los cinco días.', 'El total general.', 'El día con más unidades y cuántas fueron.']),
       pasos=['Agregá al algoritmo un recorrido con el Para de columnas afuera y el de filas adentro.', 'Acumulá el total general mientras recorrés las filas.', 'Ejecutá y compará.'],
       control='La suma de los cinco totales por día es igual a la suma de los tres totales por fila.'),
  dict(titulo='La facturación con un vector paralelo', objetivo='Calcular cuánto facturó cada artículo y la facturación total, con precio[3] paralelo a las filas.',
       modelo=('Precios', ['precio[1] = 8.000 (Cuaderno) · precio[2] = 3.000 (Bolígrafo) · precio[3] = 15.000 (Carpeta)']),
       pasos=['Multiplicá cada total de fila por su precio.', 'Acumulá la facturación total.', 'Ejecutá y verificá cada producto con la calculadora.'],
       control='La facturación total es igual a la suma de las tres facturaciones por artículo que calculaste.'),
 ],
 desafio='Agregá el promedio diario de cada artículo como Real y mostrá cuál artículo tiene el promedio más alto.',
 datos=[('Matriz v[3,5] — unidades vendidas de lunes a viernes', ['Artículo', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi'],
         [['Cuaderno', '8', '5', '7', '10', '6'], ['Bolígrafo', '25', '30', '18', '22', '27'], ['Carpeta', '2', '4', '1', '3', '5']])],
 sol=dict(resultado='Act. 1: «Fila 1: 36», «Fila 2: 122», «Fila 3: 15». Act. 2: días 35, 39, 26, 35, 38; total general 173 (= 36 + 122 + 15); día de más unidades: 2, martes, con 39. Act. 3: 36 × 8.000 = 288.000; 122 × 3.000 = 366.000; 15 × 15.000 = 225.000; facturación 879.000. Desafío: promedios 7,2 · 24,4 · 3; el más alto es el Bolígrafo.' + VER,
          errores='Cargar por columnas y leer por filas (los totales salen cruzados); no reiniciar totalFila; invertir los índices v[c,f] (error de subíndice fuera de rango); acumular el total general dos veces (en filas y en columnas).'))

PR[11] = dict(
 titulo='El ranking de la librería: burbuja y selección', entorno=PSEINT,
 competencia='Ordenar vectores con la burbuja optimizada y con el método de selección, moviendo juntos los vectores paralelos.',
 saber=['La burbuja compara vecinos e intercambia; la versión optimizada corta cuando una pasada no hizo intercambios (bandera hubo).',
        'Si el vector tiene un paralelo (los nombres), cada intercambio se hace en los dos vectores, o el ranking queda con nombres equivocados.'],
 antes='Usá las unidades de la Práctica 9 (35 · 120 · 90 · 18 · 12 · 44 · 59) y los nombres de la Práctica 8.',
 acts=[
  dict(titulo='Ranking con la burbuja optimizada', objetivo='Ordenar unid[7] de mayor a menor con la burbuja optimizada, intercambiando también los nombres, y contar las pasadas.',
       modelo=('Esqueleto para completar', E('i <- 1', 'pasadas <- 0', 'Repetir', '    hubo <- Falso', '    Para j <- 1 Hasta 7 - i Con Paso 1 Hacer', '        Si u[j] < u[j+1] Entonces', '            // intercambiar u[j] con u[j+1]', '            // intercambiar nom[j] con nom[j+1]', '            hubo <- Verdadero', '        FinSi', '    FinPara', '    pasadas <- pasadas + 1', '    i <- i + 1', 'Hasta Que NO hubo O i > 6')),
       pasos=['Hacé a mano la primera pasada y anotá cómo queda el vector.', 'Completá el algoritmo RankingBurbuja con los dos intercambios (usá aux para los números y auxN para los nombres).', 'Mostrá el ranking con su puesto y la cantidad de pasadas.'],
       control='Tu primera pasada a mano coincide con la del programa (podés mostrar el vector después de cada pasada para comprobarlo), y cada nombre del ranking conserva sus unidades de la Práctica 9.'),
  dict(titulo='Precios de menor a mayor con selección', objetivo='Ordenar los siete precios de menor a mayor con el método de selección y contar los intercambios.',
       modelo=('Idea del método', ['En la vuelta i se busca la posición del menor entre i y 7 (posMin).', 'Si posMin es distinta de i, se intercambian p[i] y p[posMin] y se cuenta el intercambio.']),
       pasos=['Escribí el algoritmo PreciosSeleccion.', 'Antes de ejecutar, anticipá cuál será el primer intercambio.', 'Ejecutá con los siete precios en el orden de la Práctica 8.'],
       control='El vector final está en orden creciente, el primer intercambio fue el que anticipaste y la cantidad de intercambios es menor que 7.'),
 ],
 desafio='Contá cuántas comparaciones hizo cada método con el mismo vector (agregá un contador justo antes del Si que compara). ¿Cuál comparó menos?',
 sol=dict(resultado='Act. 1: ranking 1. Bolígrafo 120 · 2. Lápiz 90 · 3. Goma 59 · 4. Resaltador 44 · 5. Cuaderno 35 · 6. Regla 18 · 7. Carpeta 12; «Pasadas: 5» (la quinta no intercambia y el ciclo corta antes de la sexta). Primera pasada: [120, 90, 35, 18, 44, 59, 12]. Act. 2: 1500 2000 3000 4000 6000 8000 15000; primer intercambio: 8.000 con 1.500; «Intercambios: 4». Desafío: con este vector, la burbuja hace 6 + 5 + 4 + 3 + 2 = 20 comparaciones en sus 5 pasadas y la selección 6 + 5 + 4 + 3 + 2 + 1 = 21.' + VER,
          errores='Intercambiar solo las unidades (los nombres quedan desfasados); usar > para un ranking descendente; recorrer j hasta 7 (u[j+1] sale de rango); no reiniciar hubo en cada pasada; intercambiar en selección dentro del Para interno.'))

PR[12] = dict(
 titulo='Sorteos y simulaciones con Azar', entorno=PSEINT,
 competencia='Generar valores aleatorios en un rango, usarlos en sorteos y simulaciones, y controlar los resultados con invariantes que no dependen del azar.',
 saber=['Azar(n) devuelve un entero entre 0 y n − 1. Para un rango de mín a máx se usa Azar(máx − mín + 1) + mín.',
        'Como el resultado cambia en cada ejecución, se controla con propiedades que siempre se cumplen: el rango, las sumas, las cantidades.'],
 antes='La librería sortea un cuaderno por curso y quiere simular cuántas unidades compra cada cliente (de 1 a 6).',
 acts=[
  dict(titulo='El sorteo del cuaderno', objetivo='Sortear cinco veces un número de lista entre 1 y la cantidad de estudiantes del curso.',
       modelo=('Esqueleto para completar', E('Leer estudiantes', 'Para k <- 1 Hasta 5 Con Paso 1 Hacer', '    ganador <- …', '    Escribir "Sorteo ", k, ": número de lista ", ganador', 'FinPara')),
       pasos=['Escribí la expresión con Azar para un rango de 1 a estudiantes.', 'Ejecutá tres veces con la cantidad de estudiantes de tu curso.', 'Anotá los 15 números obtenidos.'],
       control='Ninguno de los 15 números es 0 ni supera la cantidad de estudiantes, y las tres ejecuciones no dieron la misma secuencia.'),
  dict(titulo='Simular 20 clientes', objetivo='Simular las unidades que compran 20 clientes y contar las frecuencias en un vector.',
       modelo=('Idea', ['frec[6] arranca en 0.', 'Para cada cliente: u <- Azar(6) + 1 ; frec[u] <- frec[u] + 1.', 'Al final, mostrar frec y la suma de frec.']),
       pasos=['Escribí el algoritmo SimulacionCompras.', 'Ejecutalo dos veces y copiá las dos tablas de frecuencias.', 'Compará las dos tablas: ¿qué cambia y qué se mantiene?'],
       control='En las dos ejecuciones la suma de las frecuencias es exactamente 20, aunque las frecuencias cambien.'),
 ],
 desafio='Llevá la simulación a 600 clientes y observá las frecuencias. ¿Alrededor de qué valor se ubican? Explicá por qué.',
 sol=dict(resultado='Act. 1: ganador <- Azar(estudiantes) + 1; resultados entre 1 y la cantidad de estudiantes (en una prueba con 32: 25, 4, 19, 22, 18). Act. 2: las frecuencias varían en cada ejecución (por ejemplo 3, 3, 0, 2, 8, 4) pero siempre suman 20 («Clientes simulados: 20»). Desafío: con 600 clientes cada frecuencia ronda 100 (600 / 6), porque cada valor tiene la misma chance.' + VER,
          errores='Escribir Azar(estudiantes) sin + 1 (sale 0 y nunca el último); usar Azar(6) + 1 como índice sin dimensionar frec[6]; no inicializar las frecuencias; esperar que dos ejecuciones den lo mismo.'))

PR[13] = dict(
 titulo='La caja de la librería en módulos', entorno=PSEINT,
 competencia='Dividir un programa en funciones y procedimientos con parámetros, reutilizarlos y comprobar el alcance local de las variables.',
 saber=['Una Funcion devuelve un valor que se usa en una expresión; un SubProceso realiza una acción y no devuelve valor.',
        'En PSeInt no hay variables globales: cada módulo tiene sus propias variables; los datos entran por parámetros.'],
 antes='Los módulos se escriben antes del Algoritmo principal, en el mismo archivo. Un SubProceso sin parámetros se escribe sin paréntesis.',
 acts=[
  dict(titulo='Funciones y procedimiento de la caja', objetivo='Programar CalcularImporte, AplicarDescuento (10 % desde 100.000) y MostrarTicket, y usarlos desde el principal.',
       modelo=('Esqueleto para completar', E('Funcion importe <- CalcularImporte(precio, cantidad)', '    importe <- …', 'FinFuncion', '', 'Funcion neto <- AplicarDescuento(monto)', '    …', 'FinFuncion', '', 'SubProceso MostrarTicket(articulo, total)', '    Escribir "Librería Arandu | ", articulo, " | Total: ", total', 'FinSubProceso', '', 'Algoritmo CajaArandu', '    …', 'FinAlgoritmo')),
       pasos=['Completá los módulos y el principal: leer artículo, precio y cantidad; calcular el bruto; aplicar el descuento; mostrar el ticket.', 'Anticipá el ticket para 8 carpetas a 15.000 y para 6 reglas a 4.000.', 'Ejecutá los dos casos.'],
       control='Los dos tickets coinciden con lo anticipado y solo uno de los dos tuvo descuento.'),
  dict(titulo='Reutilizar y comprobar el alcance', objetivo='Invocar la misma función varias veces y comprobar que una variable local no modifica la del principal.',
       modelo=('Dos experimentos', E('// 1) Un pedido de tres líneas con la misma función:', 'total <- CalcularImporte(8000, 5) + CalcularImporte(3000, 10) + CalcularImporte(1500, 4)', '// 2) Alcance: el módulo y el principal usan una variable llamada tickets', 'SubProceso SumarTres', '    Definir tickets Como Entero', '    tickets <- 3', '    Escribir "En el módulo: ", tickets', 'FinSubProceso')),
       pasos=['Calculá a mano el total del pedido de tres líneas y ejecutalo en un algoritmo TresLineas.', 'Escribí el algoritmo Alcance: tickets <- 10, llamá a SumarTres y después mostrá tickets.', 'Antes de ejecutar, escribí qué creés que va a mostrar el principal.'],
       control='El total del pedido coincide con tu cálculo, y lo que muestra el principal confirma o corrige tu hipótesis escrita.'),
 ],
 desafio='Agregá una función CantidadParaMeta(precio, meta) que devuelva cuántas unidades hay que vender para llegar a una meta (usá trunc y sumá 1 si no es exacta). Probala con precio 6.000 y meta 100.000.',
 sol=dict(resultado='Act. 1: 8 × 15.000 = 120.000 → descuento → «Librería Arandu | Carpeta | Total: 108000»; 6 × 4.000 = 24.000 → sin descuento → «Librería Arandu | Regla | Total: 24000». Act. 2: 40.000 + 30.000 + 6.000 = 76.000 («Total del pedido: 76000»); alcance: «En el módulo: 3» y «En el principal: 10» (la variable del módulo es local). Desafío: 100.000 / 6.000 = 16,67 → trunc da 16 → no es exacta → 17 unidades.' + VER,
          errores='Escribir SubProceso SumarTres() con paréntesis vacíos (PSeInt da error); olvidar asignar la variable de retorno de la función; invocar un SubProceso dentro de una expresión; esperar que el módulo cambie la variable del principal.'))

PR[14] = dict(
 titulo='Parámetros por referencia y códigos de artículos', entorno=PSEINT,
 competencia='Distinguir el pasaje por valor y por referencia y procesar cadenas (Longitud, Subcadena, Mayusculas, Concatenar y comparación) en códigos y nombres.',
 saber=['Por valor, el módulo recibe una copia; por referencia (Por Referencia), trabaja sobre la variable original.',
        'Las cadenas se comparan carácter por carácter según su código: las mayúsculas van antes que las minúsculas y "12" es menor que "9" como texto.'],
 antes='Los códigos de la librería tienen el formato XXX-NN: tres letras de categoría, un guion y dos dígitos (por ejemplo, ESC-03).',
 acts=[
  dict(titulo='Valor o referencia', objetivo='Comprobar con un experimento qué pasa con la variable original en cada tipo de pasaje.',
       modelo=('Los dos módulos', E('SubProceso RecargoValor(monto)', '    monto <- monto + 5000', '    Escribir "Dentro (por valor): ", monto', 'FinSubProceso', '', 'SubProceso RecargoRef(monto Por Referencia)', '    monto <- monto + 5000', '    Escribir "Dentro (por referencia): ", monto', 'FinSubProceso')),
       pasos=['Escribí el algoritmo PasajeParametros: total <- 40000; llamá a RecargoValor(total) y mostrá total; llamá a RecargoRef(total) y mostrá total.', 'Antes de ejecutar, completá una tabla con lo que esperás ver en cada una de las cuatro líneas.', 'Ejecutá y compará.'],
       control='Las cuatro líneas coinciden con tu tabla; si alguna no coincide, explicá por qué con el tipo de pasaje.'),
  dict(titulo='Desarmar un código de artículo', objetivo='Extraer la categoría y el número de un código y armar un mensaje con Concatenar.',
       modelo=('Esqueleto para completar', E('Leer cod', 'cat <- Subcadena(cod, …, …)', 'num <- Subcadena(cod, …, …)', 'msj <- Concatenar("Categoría ", Mayusculas(cat))', 'msj <- Concatenar(msj, ", número ")', 'msj <- Concatenar(msj, num)', 'Escribir msj', 'Escribir "Longitud del código: ", Longitud(cod)')),
       pasos=['Completá las posiciones de Subcadena para el formato XXX-NN.', 'Ejecutá con "cua-08" (en minúsculas) y con "GEO-12".', 'Explicá qué hizo Mayusculas en el primer caso.'],
       control='Los dos códigos dan categoría en mayúsculas y número de dos dígitos, y la longitud informada es la misma en ambos.'),
  dict(titulo='Comparar nombres sin que molesten las mayúsculas', objetivo='Comparar cadenas directamente y en mayúsculas, y sacar conclusiones.',
       modelo=('Comparaciones a probar', E('Escribir "Directo: ", a < b', 'Escribir "En mayúsculas: ", Mayusculas(a) < Mayusculas(b)', 'Escribir "¿Iguales sin importar mayúsculas? ", Mayusculas(a) = Mayusculas(b)')),
       pasos=['Escribí el algoritmo CompararNombres que lee a y b y muestra las tres comparaciones.', 'Anticipá y después ejecutá con: "carpeta" y "Regla"; "Lápiz" y "lápiz"; "12" y "9".', 'Escribí una regla práctica para ordenar nombres escritos por personas distintas.'],
       control='Para cada par, al menos una de las tres comparaciones contradice el orden alfabético que esperarías al leer: tu regla práctica explica por qué.'),
 ],
 desafio='Escribí una función lógica CodigoValido(cod) que devuelva Verdadero si el código tiene 6 caracteres y un guion en la posición 4. Probala con ESC-03, ESC03, ES-003 y GEO-1.',
 sol=dict(resultado='Act. 1: «Dentro (por valor): 45000», «Después del pasaje por valor: 40000», «Dentro (por referencia): 45000», «Después del pasaje por referencia: 45000». Act. 2: Subcadena(cod, 1, 3) y Subcadena(cod, 5, 6); «Categoría CUA, número 08» y «Categoría GEO, número 12»; longitud 6 en ambos. Act. 3: carpeta/Regla → Directo FALSO (la c minúscula va después de la R mayúscula), En mayúsculas VERDADERO, Iguales FALSO; Lápiz/lápiz → Directo VERDADERO, En mayúsculas FALSO, Iguales VERDADERO; 12/9 → Directo VERDADERO y En mayúsculas VERDADERO (como texto, "1" < "9"), Iguales FALSO. Regla práctica: comparar en mayúsculas y guardar los números como Entero. Atención: las vocales acentuadas quedan después de la Z («Árbol» < «Bolsa» da FALSO). Desafío: solo ESC-03 es válido.' + VER,
          errores='Contar las posiciones desde 0; usar Subcadena(cod, 5, 2) pensando en «desde 5, dos caracteres» (el tercer argumento es la posición final); comparar sin normalizar mayúsculas; olvidar Por Referencia en la cabecera.'))

# =============================================================== UNIDAD 3
PR[15] = dict(
 titulo='Los archivos de la librería: tipos, propiedades y formato', entorno=EXPLORADOR,
 competencia='Crear archivos de texto, reconocer sus características (nombre, extensión, tamaño, ubicación) y diseñar el formato de un archivo de datos.',
 saber=['Un archivo es un conjunto de datos con nombre guardado en memoria secundaria; la extensión indica qué tipo de contenido tiene.',
        'Un archivo de texto con una línea por registro y los campos separados por punto y coma se puede abrir con el Bloc de notas y con una planilla de cálculo.'],
 antes='Trabajá en una carpeta tuya dentro de Documentos. Si la vista del Explorador no muestra las extensiones, activá Vista → Extensiones de nombre de archivo (o la opción equivalente de tu versión de Windows).',
 acts=[
  dict(titulo='Crear el primer archivo de datos', objetivo='Crear con el Bloc de notas el archivo articulos.txt con los ocho artículos de la librería y observar sus propiedades.',
       modelo=('Primeras líneas del archivo (formato código;nombre;precio;stock)', E('LIB-01;Cuaderno;8000;35', 'LIB-02;Bolígrafo;3000;120', '…')),
       pasos=['Copiá las ocho líneas de la tabla de datos, una por artículo, sin líneas en blanco.', 'Guardá como articulos.txt en tu carpeta, con codificación UTF-8.', 'En el Explorador, abrí Propiedades del archivo y anotá: nombre, extensión, tipo, ubicación y tamaño.'],
       control='El archivo tiene exactamente ocho líneas y anotaste las cinco propiedades leyéndolas del cuadro Propiedades, no de memoria.'),
  dict(titulo='Clasificar archivos', objetivo='Clasificar archivos de la computadora por extensión, tipo de contenido y forma de acceso.',
       modelo=('Tabla para completar', ['Archivo | Extensión | Texto o binario | ¿Se puede leer con el Bloc de notas? | Acceso típico (secuencial o directo)']),
       pasos=['Buscá en tu carpeta o en Documentos cinco archivos de tipos distintos (por ejemplo .txt, .docx, .jpg, .pdf, .accdb).', 'Abrí cada uno con el Bloc de notas (Abrir con) solo para observar; cerralo sin guardar.', 'Completá la tabla.'],
       control='Clasificaste como texto solo los archivos que el Bloc de notas muestra legibles, y no guardaste cambios en ningún archivo binario.'),
  dict(titulo='Diseñar el archivo de ventas', objetivo='Diseñar el formato del archivo donde la librería registra cada venta.',
       modelo=('Decisiones de diseño', ['Nombre del archivo y extensión.', 'Campos de cada línea y su orden.', 'Separador.', 'Una línea de ejemplo.', 'Cuántas líneas tendría en un día con 25 ventas.']),
       pasos=['Elegí los campos mínimos: fecha, código de artículo, cantidad e importe.', 'Escribí tres líneas de ejemplo coherentes con los precios de la librería.', 'Creá el archivo con el Bloc de notas y abrilo con una planilla de cálculo para verificar que cada campo cae en su columna.'],
       control='Al abrirlo con la planilla, cada campo de tus tres líneas cae en una columna distinta y el importe es precio × cantidad.'),
 ],
 desafio='Agregá un renglón de encabezado al archivo de ventas (con los nombres de los campos). ¿Qué ventaja tiene y qué tendría que tener en cuenta un programa que lo lea?',
 datos=[('Artículos de la Librería Arandu', ['Código', 'Nombre', 'Precio', 'Categoría', 'Stock'], [list(a) for a in ARTICULOS])],
 sol=dict(resultado='Act. 1: articulos.txt, extensión .txt, tipo «Documento de texto», ubicación la carpeta del estudiante; tamaño de unos 200 bytes (varía según codificación y saltos de línea; no hay un único valor correcto). Act. 2: .txt texto legible; .docx, .jpg, .pdf y .accdb binarios (el Bloc de notas muestra símbolos); acceso: texto típicamente secuencial, bases de datos con acceso directo. Act. 3: ejemplo ventas_2026.txt con fecha;codigo;cantidad;importe → 2026-03-02;LIB-02;4;12000; un día con 25 ventas tiene 25 líneas. Desafío: el encabezado documenta los campos; el programa debe saltear la primera línea.',
          errores='Guardar como articulos.txt.txt (extensiones ocultas); dejar líneas en blanco al final; guardar cambios al abrir un binario con el Bloc de notas; usar coma como separador cuando los números pueden llevar coma decimal.'))

PR[16] = dict(
 titulo='Escribir, leer y agregar: operaciones con archivos', entorno=PAPEL + ' y ' + EXPLORADOR,
 competencia='Expresar las operaciones con archivos en la notación conceptual del libro, hacer su prueba de escritorio y realizar las operaciones de administración en el Explorador.',
 saber=['La secuencia es siempre abrir (con un modo) → leer o escribir → cerrar. Escritura empieza en blanco; Agregar escribe al final; Lectura no modifica.',
        'La notación del libro es conceptual (PSeInt no trabaja con archivos): Abrir … Para …, Escribir Archivo, Leer Archivo, FinDeArchivo, Cerrar Archivo.'],
 antes='Usá el archivo articulos.txt de la Práctica 15.',
 acts=[
  dict(titulo='Grabar el stock en papel', objetivo='Escribir en la notación del libro el procedimiento que graba codigos[8] y stock[8] en el archivo stock.txt.',
       modelo=('Esqueleto para completar', E('Abrir "stock.txt" Para …', 'Para i <- 1 Hasta 8 Con Paso 1 Hacer', '    Escribir Archivo …', 'FinPara', 'Cerrar Archivo')),
       pasos=['Elegí el modo de apertura y justificá por qué no es Agregar.', 'Completá la línea que graba código y stock separados por punto y coma.', 'Escribí cómo quedan las tres primeras líneas del archivo.'],
       control='Tu procedimiento abre una sola vez, cierra una sola vez y graba exactamente ocho líneas.'),
  dict(titulo='Prueba de escritorio de una lectura', objetivo='Seguir paso a paso la lectura de stock.txt para sumar el stock total.',
       modelo=('Procedimiento a seguir', E('total <- 0', 'Abrir "stock.txt" Para Lectura', 'Mientras No FinDeArchivo Hacer', '    Leer Archivo linea', '    total <- total + StockDe(linea)', 'FinMientras', 'Cerrar Archivo', '// StockDe(linea) representa extraer el número que está después del punto y coma')),
       pasos=['Armá la tabla de la prueba de escritorio: vuelta, línea leída, stock extraído, total.', 'Recorré las ocho líneas y agregá la fila en la que FinDeArchivo corta el ciclo.', 'Contrastá el total con la suma de la columna Stock de la tabla de datos.'],
       control='Tu tabla tiene ocho vueltas con lectura más la fila de corte, y el total final es igual a la suma de la columna Stock.'),
  dict(titulo='Administrar archivos en el Explorador', objetivo='Realizar las operaciones de administración de archivos y registrar qué hizo el sistema operativo en cada una.',
       modelo=('Operaciones', ['Copiar articulos.txt y renombrar la copia como articulos_respaldo.txt.', 'Crear una subcarpeta Respaldos y mover la copia allí.', 'Eliminar la copia y restaurarla desde la Papelera de reciclaje.']),
       pasos=['Realizá las operaciones en el orden indicado.', 'Después de cada una, anotá dónde está el archivo y qué cambió en sus propiedades (fecha de modificación, ubicación).', 'Abrí la copia restaurada y verificá su contenido.'],
       control='Al terminar, el original sigue intacto en tu carpeta y la copia restaurada tiene las mismas ocho líneas.'),
 ],
 desafio='Escribí en la notación del libro el procedimiento que agrega al final de stock.txt el artículo LIB-09 (Escuadra, stock 10) sin borrar lo anterior. ¿Qué pasaría si usaras el modo Escritura?',
 sol=dict(resultado='Act. 1: Abrir "stock.txt" Para Escritura (Agregar sumaría líneas a un archivo viejo y duplicaría artículos); Escribir Archivo codigos[i], ";", stock[i]; primeras líneas LIB-01;35 · LIB-02;120 · LIB-03;90. Act. 2: total acumulado 35, 155, 245, 263, 275, 319, 378, 385; en la vuelta 9 FinDeArchivo es Verdadero y corta; total 385 = suma de la columna Stock. Act. 3: copiar crea un archivo nuevo con el mismo contenido; renombrar y mover cambian nombre y ubicación (no el contenido); eliminar lo lleva a la Papelera y restaurar lo devuelve a la carpeta de donde se eliminó. Desafío: Abrir "stock.txt" Para Agregar ; Escribir Archivo "LIB-09;10" ; Cerrar Archivo. Con Escritura el archivo quedaría con una sola línea.',
          errores='Abrir dentro del ciclo; olvidar Cerrar Archivo; contar la vuelta de FinDeArchivo como una lectura; eliminar el original en lugar de la copia; vaciar la Papelera antes de restaurar.'))

PR[17] = dict(
 titulo='Proteger y respaldar los archivos de la librería', entorno=EXPLORADOR,
 competencia='Aplicar mecanismos de protección de archivos (solo lectura, respaldo) y razonar sobre acceso secuencial, acceso directo y buffer.',
 saber=['El atributo Solo lectura reduce sobrescrituras accidentales en aplicaciones que lo respetan; no reemplaza los permisos ni el respaldo.',
        'Un buffer junta datos en memoria para acceder al disco menos veces; cerrar el archivo vacía el buffer.'],
 antes='Trabajá con articulos.txt y stock.txt de las prácticas anteriores. Tené a mano un pendrive o una carpeta de la nube del colegio, si está disponible.',
 acts=[
  dict(titulo='El atributo Solo lectura', objetivo='Marcar un archivo como Solo lectura y observar qué pasa al intentar guardar cambios.',
       modelo=('Registro del experimento', ['Qué hiciste · Qué mostró la computadora · Qué conclusión sacás']),
       pasos=['En Propiedades de articulos.txt, marcá Solo lectura y aceptá.', 'Abrilo con el Bloc de notas, cambiá un precio e intentá Guardar.', 'Anotá qué pasó, cerrá sin guardar y quitá el atributo.'],
       control='El archivo original no cambió: su contenido y su fecha de modificación son los mismos que antes del experimento.'),
  dict(titulo='Un plan de respaldo', objetivo='Diseñar y ejecutar un respaldo de los archivos de la librería.',
       modelo=('El plan responde', ['Qué archivos se respaldan.', 'Cada cuánto.', 'Dónde (un soporte distinto del original).', 'Cómo se nombra cada copia.', 'Quién lo hace.']),
       pasos=['Escribí el plan en cinco líneas.', 'Hacé el primer respaldo: copiá los archivos a otro soporte o carpeta con el nombre que definiste (por ejemplo, con la fecha).', 'Simulá una pérdida: renombrá el original y recuperalo desde el respaldo.'],
       control='Recuperaste el archivo desde la copia y su contenido es idéntico al original.'),
  dict(titulo='Acceso y buffer en números', objetivo='Calcular accesos al disco y comparar acceso secuencial y directo con casos de la librería.',
       modelo=('Casos', ['(a) Un archivo de 10 líneas se lee con un buffer de 4 líneas: ¿cuántos accesos al disco?', '(b) El mismo archivo sin buffer: ¿cuántos accesos?', '(c) Un archivo de 300 ventas: para consultar la venta 250, ¿cuántos registros se leen con acceso secuencial y cuántos con acceso directo?']),
       pasos=['Resolvé cada caso con un dibujo de tandas o de registros.', 'Escribí una conclusión: ¿cuándo conviene cada tipo de acceso?', 'Relacioná el caso (a) con la importancia de cerrar el archivo.'],
       control='En (a) cada línea quedó en exactamente una tanda y la cantidad de tandas es la cantidad de accesos.'),
 ],
 desafio='Averiguá en tu colegio o en tu casa cómo se respaldan los archivos importantes (fotos, trabajos). Compará con tu plan: ¿qué le falta a cada uno?',
 sol=dict(resultado='Act. 1: el Bloc de notas no sobrescribe un archivo de solo lectura: muestra un aviso o abre «Guardar como» (el mensaje varía según la versión de Windows). Act. 2: plan coherente con soporte distinto del original; la recuperación devuelve el contenido idéntico. Act. 3: (a) 3 accesos (4 + 4 + 2); (b) 10 accesos; (c) secuencial 250 lecturas; directo 1. Conclusión: directo para consultas puntuales, secuencial para procesar todo el archivo. Al cerrar, el sistema vacía el buffer de escritura.',
          errores='Creer que Solo lectura protege contra borrar o contra otras personas con permisos; guardar el respaldo en la misma carpeta; responder 2 accesos en (a) (la última tanda incompleta también es un acceso); confundir acceso directo con «más rápido siempre».'))

PR[18] = dict(
 titulo='El árbol de carpetas de la librería', entorno=EXPLORADOR,
 competencia='Crear y recorrer una estructura de carpetas, escribir rutas absolutas y relativas y buscar archivos con comodines.',
 saber=['La ruta absoluta empieza en la unidad (C:\\…); la relativa se cuenta desde la carpeta en la que uno está.',
        'En la búsqueda del Explorador, el asterisco reemplaza cualquier cantidad de caracteres: *.txt encuentra todos los archivos de texto.'],
 antes='Trabajá dentro de tu carpeta de Documentos. Si en el colegio no podés crear carpetas, hacé las actividades en papel y verificalas en la primera clase con equipo disponible.',
 acts=[
  dict(titulo='Construir el árbol', objetivo='Crear la estructura de carpetas de la librería para 2026.',
       modelo=('Estructura a crear', ['Arandu', '   Ventas → 2026 → marzo, abril', '   Compras → 2026 → marzo', '   Respaldos']),
       pasos=['Dibujá el árbol en tu carpeta antes de crearlo.', 'Creá las carpetas en el Explorador.', 'Copiá articulos.txt en Ventas\\2026\\marzo y stock.txt en Compras\\2026\\marzo.'],
       control='El panel de navegación del Explorador muestra el mismo árbol que dibujaste, con cada archivo en su carpeta.'),
  dict(titulo='Rutas absolutas y relativas', objetivo='Escribir las rutas de los archivos y comprobarlas en la barra de direcciones.',
       modelo=('Tabla para completar', ['Archivo · Ruta absoluta · Ruta relativa desde Arandu']),
       pasos=['Escribí la ruta absoluta y la relativa de los dos archivos copiados.', 'Pegá cada ruta absoluta en la barra de direcciones del Explorador (sin el nombre del archivo) y verificá que abra la carpeta correcta.', 'Escribí cuántos niveles hay entre la unidad y cada archivo.'],
       control='Cada ruta absoluta abre la carpeta esperada al pegarla en la barra de direcciones.'),
  dict(titulo='Buscar con comodines', objetivo='Usar el cuadro de búsqueda con comodines y anticipar los resultados.',
       modelo=('Búsquedas', ['*.txt dentro de Arandu', 'stock* dentro de Arandu', '*.txt dentro de Arandu\\Compras']),
       pasos=['Antes de cada búsqueda, anotá cuántos archivos esperás encontrar y cuáles.', 'Hacé las tres búsquedas.', 'Compará con lo anotado.'],
       control='Cada búsqueda encontró exactamente los archivos que anticipaste; si no, encontraste por qué en el árbol.'),
 ],
 desafio='Proponé una regla de nombres para los archivos de ventas diarias (por ejemplo, con la fecha en formato año-mes-día) y explicá por qué ese formato ordena bien los archivos por nombre.',
 sol=dict(resultado='Act. 1: árbol Arandu\\{Ventas\\2026\\{marzo, abril}, Compras\\2026\\marzo, Respaldos}. Act. 2: por ejemplo C:\\Users\\<usuario>\\Documentos\\Arandu\\Ventas\\2026\\marzo\\articulos.txt (la parte inicial depende del equipo) y relativa Ventas\\2026\\marzo\\articulos.txt; desde la unidad hay tantos niveles como carpetas en la ruta. Act. 3: *.txt en Arandu → 2 archivos; stock* → 1 (stock.txt); *.txt en Compras → 1. Desafío: ventas_2026-03-02.txt: año-mes-día hace coincidir el orden alfabético con el cronológico.',
          errores='Escribir la ruta con barras / en lugar de \; incluir el nombre del archivo al pegar en la barra de direcciones; buscar desde una carpeta que no contiene a las demás; nombres con fechas en formato día-mes-año (se ordenan mal).'))

# =============================================================== UNIDAD 4
PR[19] = dict(
 titulo='La tabla Artículos en Access: diseño, carga y filtros', entorno=ACCESS,
 competencia='Crear una tabla en Access con sus campos, tipos de datos y clave principal, cargar registros y aplicar filtros anticipando el resultado.',
 saber=['Cada campo tiene un tipo de dato: Texto corto para códigos y nombres, Número para cantidades y precios. Si el precio se guarda como texto, los filtros numéricos no funcionan bien.',
        'Un filtro oculta los registros que no cumplen el criterio; no los borra. Al quitar el filtro, vuelven todos.'],
 antes='Abrí Access, elegí Base de datos en blanco y guardala como Arandu.accdb en tu carpeta. ' + 'Las rutas de menú de este libro corresponden a Microsoft Access 2016 en castellano; en otras versiones algún nombre o ubicación puede variar.',
 acts=[
  dict(titulo='Diseñar la tabla', objetivo='Crear la tabla Articulos en vista Diseño con sus cinco campos, tipos y clave principal.',
       modelo=('Diseño de la tabla Articulos', ['codigo · Texto corto · clave principal', 'nombre · Texto corto', 'precio · Número (Entero largo)', 'categoria · Texto corto', 'stock · Número (Entero largo)']),
       pasos=['Crear → Diseño de tabla. Escribí los cinco nombres de campo y elegí el tipo de dato de cada uno.', 'Seleccioná codigo y marcá Clave principal (el indicador de clave aparece a la izquierda del campo).', 'Guardá la tabla con el nombre Articulos y cerrá la vista Diseño.'],
       control='En el panel de navegación aparece la tabla Articulos y, al reabrirla en Diseño, precio y stock figuran como Número y codigo tiene el indicador de clave.'),
  dict(titulo='Cargar los ocho artículos', objetivo='Cargar los registros en la vista Hoja de datos y comprobar la clave principal.',
       modelo=('Datos', ['Los ocho artículos de la tabla de datos, al final de la práctica.']),
       pasos=['Abrí Articulos en vista Hoja de datos y cargá los ocho registros.', 'Intentá cargar un noveno registro con el código LIB-03 repetido y anotá qué pasa. Después borrá esa fila incompleta (Esc).', 'Contá los registros en la barra inferior de la hoja.'],
       control='La barra de registros indica 8 y Access no aceptó el código repetido.'),
  dict(titulo='Filtros con anticipación', objetivo='Aplicar tres filtros, anticipando antes cuántos registros va a mostrar cada uno.',
       modelo=('Filtros', ['stock < 20', 'categoria = "escritura"', 'precio >= 8000']),
       pasos=['Para cada filtro, anotá en tu carpeta cuántos registros esperás y cuáles.', 'Aplicá cada filtro desde Inicio → Ordenar y filtrar (Filtro por formulario o Filtros de número / de texto en el encabezado de la columna) y alterná con Alternar filtro.', 'Quitá el último filtro y contá los registros.'],
       control='Cada filtro mostró los registros que anticipaste y, al quitar el filtro, la barra vuelve a indicar 8.'),
 ],
 desafio='Combiná dos criterios en un mismo filtro: artículos de escritura con stock menor a 60. Anticipá el resultado antes de aplicarlo.',
 datos=[('Artículos de la Librería Arandu', ['Código', 'Nombre', 'Precio', 'Categoría', 'Stock'], [list(a) for a in ARTICULOS])],
 sol=dict(resultado='Act. 1: tabla Articulos con codigo como clave principal; precio y stock de tipo Número (si se dejan como texto, «< 20» compara como texto y falla). Act. 2: al repetir LIB-03 Access no guarda el registro y muestra un aviso de valores duplicados en la clave principal (el texto exacto depende de la versión); 8 registros. Act. 3: stock < 20 → Regla (18), Carpeta (12), Compás (7): 3 registros; categoria = "escritura" → Bolígrafo, Lápiz, Resaltador, Goma: 4; precio >= 8000 → Cuaderno, Carpeta, Compás: 3. Desafío: escritura y stock < 60 → Resaltador (44) y Goma (59): 2.',
          errores='Dejar precio y stock como Texto corto; no guardar la tabla con su nombre (queda Tabla1); escribir los criterios con comillas en campos numéricos; cerrar Access con un filtro aplicado y creer que se borraron registros.'))

PR[20] = dict(
 titulo='Consultas de la librería: selección, parámetro, totales y campo calculado', entorno=ACCESS,
 competencia='Diseñar, ejecutar y guardar consultas de selección, paramétricas, de totales y con campo calculado, comparando cada resultado con lo anticipado.',
 saber=['Una consulta se arma en la cuadrícula de diseño: campos, orden, criterios. Se guarda con un nombre y se puede volver a ejecutar.',
        'Un parámetro se escribe entre corchetes en la fila Criterios: Access lo pregunta al ejecutar. Un campo calculado se escribe como Nombre: expresión.'],
 antes='Usá la base Arandu.accdb con la tabla Articulos de la Práctica 19. ' + 'Las rutas de menú de este libro corresponden a Microsoft Access 2016 en castellano; en otras versiones algún nombre o ubicación puede variar.',
 acts=[
  dict(titulo='Selección con criterio y orden', objetivo='Mostrar nombre, precio y stock de los artículos de escritura, ordenados por precio de mayor a menor.',
       modelo=('Cuadrícula de diseño', ['Campos: nombre, precio, stock, categoria.', 'Criterios: "escritura" en categoria (desmarcá Mostrar en esa columna).', 'Orden: Descendente en precio.']),
       pasos=['Crear → Diseño de consulta; agregá la tabla Articulos.', 'Anotá el resultado esperado (cantidad y orden) antes de ejecutar.', 'Ejecutá con Diseño → Ejecutar y guardá la consulta como Escritura_por_precio.'],
       control='El resultado tiene la cantidad y el orden que anotaste, y la columna categoria no se muestra.'),
  dict(titulo='Una consulta paramétrica', objetivo='Pedir la categoría al ejecutar la consulta.',
       modelo=('Criterio con parámetro', ['En la fila Criterios de categoria: [¿Qué categoría?]']),
       pasos=['Creá la consulta con nombre, categoria y stock y el parámetro en categoria.', 'Ejecutala tres veces: papelería, geometría y una categoría que no existe (por ejemplo, arte).', 'Guardala como Por_categoria.'],
       control='Las dos categorías existentes muestran solo sus artículos y la inexistente devuelve una hoja vacía, sin error.'),
  dict(titulo='Totales por categoría y valor del stock', objetivo='Agrupar por categoría para contar artículos y sumar stock, y calcular el valor del stock de cada artículo.',
       modelo=('Dos consultas', ['Totales: categoria (Agrupar por) · codigo (Cuenta) · stock (Suma).', 'Campo calculado: ValorStock: [precio]*[stock], con nombre y los dos campos.']),
       pasos=['Para la de totales, activá Diseño → Totales y elegí la función de cada columna.', 'Para la otra, escribí el campo calculado en una columna vacía y agregá una fila de totales en la hoja de datos (Inicio → Totales) para sumar ValorStock.', 'Guardá las dos consultas.'],
       control='La suma de las cuentas por categoría da 8, la suma de los stocks por categoría coincide con el stock total de la tabla, y el ValorStock de cada artículo es su precio por su stock.'),
 ],
 desafio='Creá una consulta paramétrica con el criterio <=[Precio máximo] en precio y ejecutala con 6000. ¿Qué artículos se pueden comprar con ese presupuesto por unidad?',
 sol=dict(resultado='Act. 1: Resaltador 6.000 (44), Bolígrafo 3.000 (120), Lápiz 2.000 (90), Goma 1.500 (59): 4 registros. Act. 2: papelería → Cuaderno y Carpeta; geometría → Regla y Compás; arte → hoja vacía. Act. 3: totales: escritura 4 artículos y 313 de stock; geometría 2 y 25; papelería 2 y 47 (8 artículos, 385 de stock). ValorStock: Cuaderno 280.000 · Bolígrafo 360.000 · Lápiz 180.000 · Regla 72.000 · Carpeta 180.000 · Resaltador 264.000 · Goma 88.500 · Compás 84.000; suma 1.508.500 (en la vista SQL la expresión aparece igual: [precio]*[stock]). Desafío: Bolígrafo, Lápiz, Regla, Resaltador y Goma (5). Verificación manual pendiente: el nombre de la función de conteo en la fila Total (Cuenta) puede variar con la versión.',
          errores='Dejar marcado Mostrar en la columna del criterio (aparece una columna repetida); escribir el parámetro sin corchetes (Access lo toma como texto fijo); usar Suma sobre codigo; escribir ValorStock = precio*stock en lugar de ValorStock: [precio]*[stock].'))

PR[21] = dict(
 titulo='La referencia cruzada de la librería y el informe de reposición', entorno=ACCESS,
 competencia='Preparar el origen con un campo calculado condicional, construir una consulta de referencias cruzadas con el asistente y controlarla contra la tabla.',
 saber=['El asistente de referencias cruzadas trabaja sobre una sola tabla o consulta: si una columna no existe, se calcula antes en una consulta de origen.',
        'En la cuadrícula de Access en castellano, la función condicional se escribe SiInm(condición;valor_si;valor_no); en la vista SQL aparece como IIf.'],
 antes='Usá Arandu.accdb. ' + 'Las rutas de menú de este libro corresponden a Microsoft Access 2016 en castellano; en otras versiones algún nombre o ubicación puede variar.',
 acts=[
  dict(titulo='La consulta de origen', objetivo='Crear una consulta que agregue a cada artículo su nivel de stock: «reponer» si el stock es menor que 20 y «ok» si no.',
       modelo=('Campo calculado', ['Nivel: SiInm([stock]<20;"reponer";"ok")']),
       pasos=['Creá una consulta con nombre, categoria, stock y el campo calculado Nivel.', 'Antes de ejecutar, marcá en la tabla de datos qué artículos deberían decir «reponer».', 'Ejecutá, revisá la vista SQL para ver cómo aparece la expresión y guardá la consulta como Origen_nivel.'],
       control='Cada artículo tiene el nivel que marcaste en la tabla de datos. Si Access rechaza la expresión, revisá el separador (punto y coma) y las comillas.'),
  dict(titulo='La referencia cruzada con el asistente', objetivo='Construir la grilla categoría × nivel con el asistente.',
       modelo=('Opciones del asistente', ['Crear → Asistente para consultas → Asistente para consultas de referencias cruzadas.', 'Origen: la consulta Origen_nivel.', 'Encabezado de fila: categoria · encabezado de columna: Nivel · valor: nombre con la función de conteo.']),
       pasos=['Antes de usar el asistente, dibujá en papel la grilla con sus celdas completas.', 'Recorré el asistente con las opciones del modelo y guardá la consulta como Cruce_nivel.', 'Compará la grilla de Access con la de papel.'],
       control='Las celdas de Access coinciden con tu grilla de papel y la suma de todas las celdas da la cantidad de artículos de la tabla.'),
  dict(titulo='Del dato a la decisión', objetivo='Usar la grilla para redactar un informe breve de reposición.',
       modelo=('El informe responde', ['¿Qué categorías necesitan reposición y cuántos artículos?', '¿Qué categoría no tiene ningún artículo para reponer?', '¿Qué artículo pedirías primero y por qué (mirá también el stock)?']),
       pasos=['Respondé las tres preguntas con datos de la grilla y de la consulta de origen.', 'Cambiá en la tabla el stock de la Regla a 25, volvé a ejecutar Cruce_nivel y anotá qué celda cambió.', 'Devolvé el stock de la Regla a 18.'],
       control='Después del cambio, la grilla sigue sumando 8 y solo cambiaron las dos celdas de la fila de la categoría de la Regla.'),
 ],
 desafio='Cambiá la grilla para que en lugar de contar artículos sume el stock. ¿Qué información nueva da y qué información se pierde?',
 sol=dict(resultado='Act. 1: reponer → Regla (18), Carpeta (12), Compás (7); ok → los otros 5. En la vista SQL la expresión aparece como IIf([stock]<20,"reponer","ok"). Act. 2: grilla (filas categoría, columnas ok / reponer): escritura 4 / —; geometría — / 2; papelería 1 / 1; total 5 + 3 = 8. Access deja vacías las celdas sin registros (no muestra 0). Act. 3: reposición en geometría (2) y papelería (1); escritura no tiene artículos para reponer; prioridad: Compás (stock 7, el más bajo). Con la Regla en 25, geometría pasa a ok 1 / reponer 1 y el total sigue en 8. Desafío: con Suma de stock la grilla muestra unidades (escritura ok 313; geometría reponer 25; papelería ok 35, reponer 12) y se pierde cuántos artículos distintos hay en cada celda. Verificación manual pendiente: el nombre de la función de conteo del asistente (Cuenta) y el texto de los botones pueden variar con la versión.',
          errores='Usar coma como separador de SiInm en Access en castellano; elegir la tabla Articulos como origen (no tiene Nivel); elegir stock como valor con Cuenta; leer una celda vacía como error; olvidar devolver el stock de la Regla a 18.'))

# =============================================================== Transferencias (solo en prácticas de dos encuentros)
PR[7]['transfer'] = dict(
 caso=('la cantina del colegio', ['La cantina abre cinco días. Ventas: 95.000 · 120.000 · 80.000 · 140.000 · 115.000.', 'Programá en un solo algoritmo: total, promedio, cuántos días superaron 100.000 y una bandera que indique si algún día vendió menos de 85.000.']),
 pasos=['Adaptá el algoritmo de la Actividad 3 a cinco días y a los nuevos umbrales.', 'Intercambiá el programa con otro equipo: ejecutalo con los datos de la cantina y buscá al menos un error o una mejora.', 'Corregí tu versión con lo que te señalaron y justificá por escrito la versión final.'],
 control='Las dos versiones del equipo (la original y la corregida) dan los mismos resultados que la prueba de escritorio de la cantina, y la justificación nombra el cambio hecho.',
 sol='Total 550.000; promedio 110.000; superan 100.000: 3 días (120.000, 140.000, 115.000); bandera Verdadero (80.000, día 3). Errores típicos que se detectan en la revisión: Para hasta 6 (sale de rango de datos y pide un dato de más), umbral con >= en lugar de >.')
PR[10]['transfer'] = dict(
 caso=('la cantina del colegio', ['Matriz m[2,3]: filas Empanada y Jugo; columnas Recreo 1, Recreo 2, Salida.', 'Empanada: 40 · 35 · 52 · Jugo: 18 · 26 · 21.']),
 pasos=['Adaptá MatrizVentas a 2 filas y 3 columnas: total por fila, por columna y general.', 'Intercambiá con otro equipo: revisá los límites de los Para y el reinicio de los totales.', 'Corregí y justificá la versión final.'],
 control='En la versión final, la suma de los totales de fila es igual a la suma de los totales de columna.',
 sol='Filas: 127 y 65; columnas: 58, 61, 73; total 192 por los dos caminos.' + VER)
PR[14]['transfer'] = dict(
 caso=('validar códigos', ['La librería recibe códigos escritos a mano: ESC-03, ESC03, ES-003, GEO-1.', 'Hay que decidir cuáles tienen el formato XXX-NN.']),
 pasos=['Escribí una condición con Longitud y Subcadena que acepte solo el formato XXX-NN y probala con los cuatro códigos.', 'Intercambiá con otro equipo y buscá un código inválido que tu condición acepte por error.', 'Mejorá la condición o justificá por qué es suficiente para la librería.'],
 control='Los cuatro códigos se clasifican igual en las versiones de los dos equipos, y la justificación indica qué casos quedan fuera del control.',
 sol='Condición (Longitud(cod) = 6) Y (Subcadena(cod, 4, 4) = "-"): solo ESC-03 es válido.' + VER + ' Límite del control: acepta «12A-XY» (no verifica que haya letras y dígitos); se acepta justificar que alcanza para detectar errores de tipeo frecuentes.')


if __name__ == '__main__':
    for n in range(1, 22):
        p = PR[n]
        assert len(p['acts']) >= 2 and p['sol']['resultado'] and p['sol']['errores'], n
        assert (len(p['acts']) == 3) == (n in (7, 10, 14, 15, 16, 17, 18, 19, 20, 21)), n
    print('prácticas', len(PR), 'actividades', sum(len(p['acts']) for p in PR.values()), 'transferencias', sum(1 for p in PR.values() if p.get('transfer')))

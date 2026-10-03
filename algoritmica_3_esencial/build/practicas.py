# -*- coding: utf-8 -*-
"""Las 21 prácticas de la Edición Esencial: datos NUEVOS respecto de cada clase.
Formato por práctica (modelo Software 1.º): Competencia · Lo que necesitás saber · Antes de empezar ·
Actividades (objetivo → modelo → pasos → punto de control) · Desafío final.
'sol' alimenta el Solucionario (resultado esperado y errores frecuentes)."""
from datos import PROD2, CLI2, TEL2, VEN2, DET2

PSEINT = 'PSeInt'
PAPEL = 'papel y lápiz'
ACCESS = 'Microsoft Access'


def g(n):
    return 'G. ' + format(n, ',').replace(',', '.')


PR = {}

PR[1] = dict(
 titulo='El cobro de un pedido para llevar, en órdenes precisas y en PSeInt', entorno=PSEINT,
 competencia='Traducir un procedimiento de cobro a instrucciones sin ambigüedad y ejecutarlo en PSeInt, verificando el resultado con un cálculo hecho a mano.',
 saber=['Una computadora ejecuta exactamente lo que se le ordena. Cada paso debe decir qué dato usa, qué operación hace y dónde guarda el resultado.',
        'En PSeInt, Leer guarda en una variable lo que escribe el usuario, <- asigna un valor (en el pseudocódigo en papel lo escribimos con la flecha ←) y Escribir muestra un resultado. Si … Entonces … SiNo … FinSi elige entre dos caminos.'],
 antes='Abrí PSeInt y, en Configurar → Opciones del Lenguaje (perfiles), seleccioná el perfil Flexible: es el perfil de referencia de este libro.',
 acts=[
  dict(titulo='Órdenes precisas en papel', objetivo='Escribir el algoritmo para cobrar un pedido para llevar: 3 mbeju (G. 5.000 c/u) y 2 cocidos (G. 4.000 c/u), con un costo de envío fijo de G. 5.000. El cliente paga con G. 50.000.',
       modelo=('Estructura que debe tener tu algoritmo (sin los números)', ['1) Leer las cantidades y el pago.', '2) Calcular el subtotal de cada producto.', '3) Sumar los subtotales y el envío.', '4) Calcular el vuelto.', '5) Mostrar el total y el vuelto.']),
       pasos=['Numerá cada paso; ninguno puede decir «calcular» sin decir cómo.', 'Reemplazá cada precio y cada cantidad por su valor.', 'Hacé la cuenta a mano y anotá el total y el vuelto al costado.'],
       control='El vuelto más el total deben dar exactamente lo pagado (G. 50.000). Si un compañero sigue tus pasos sin preguntarte nada, llega a los mismos números.'),
  dict(titulo='El mismo algoritmo, ejecutado en PSeInt', objetivo='Escribir el algoritmo en PSeInt, ejecutarlo y comprobar que coincide con la cuenta a mano.',
       modelo=('Esqueleto para completar (las líneas «…» las escribís vos)', ['Algoritmo CobroParaLlevar', '    Definir cantMbeju, cantCocido, pago, total, vuelto Como Entero', '    Escribir "Cantidad de mbeju:"', '    Leer cantMbeju', '    …', '    total <- …', '    Si pago >= total Entonces', '        vuelto <- pago - total', '        Escribir "Total: ", total, "  Vuelto: ", vuelto', '    SiNo', '        Escribir "El pago no alcanza"', '    FinSi', 'FinAlgoritmo']),
       pasos=['Copiá el esqueleto en PSeInt y completá las líneas que faltan (leer cantCocido y pago; calcular total con el envío).', 'Ejecutalo con el pedido del papel (3, 2 y 50.000).', 'Ejecutalo de nuevo con 1 mbeju, 1 cocido y un pago de G. 10.000.', 'Guardá el archivo como CobroParaLlevar.psc.'],
       control='Con el primer caso, la pantalla muestra los mismos números que tu papel. Con el segundo caso, el programa no debe mostrar un vuelto negativo.'),
 ],
 desafio='Agregá un descuento de G. 2.000 cuando el total (con envío) supere G. 25.000. Probá que el descuento aparezca en el primer caso y no en el segundo.',
 sol=dict(resultado='Act. 1: subtotales 15.000 y 8.000; total = 15.000 + 8.000 + 5.000 = G. 28.000; vuelto = G. 22.000. Act. 2: el programa muestra «Total: 28000  Vuelto: 22000»; con 1 mbeju, 1 cocido y G. 10.000: total 14.000 > 10.000 → «El pago no alcanza». Desafío: total 26.000 y vuelto 24.000 en el primer caso; sin descuento en el segundo. (Los tres casos se ejecutaron en PSeInt 20250314 con el perfil Flexible.)',
          errores='Escribir pasos vagos («calcular el total»); olvidar el envío; usar = para asignar (el perfil Flexible lo acepta, pero conviene escribir <-, que es lo que exigen los perfiles estrictos); escribir el carácter ← en PSeInt (no lo reconoce: se escribe <-); no leer el pago antes de usarlo; ubicar el descuento después de calcular el vuelto.'))

PR[2] = dict(
 titulo='Traductores y errores en acción', entorno=PSEINT,
 competencia='Reconocer niveles de lenguaje y observar en PSeInt cuándo y cómo aparecen los errores de sintaxis, de ejecución y de lógica.',
 saber=['Máquina → ensamblador → alto nivel: cuanto más alto el nivel, más necesita una herramienta que lo traduzca o lo procese.',
        'PSeInt interpreta el pseudocódigo: lo analiza, avisa los errores de escritura y lo ejecuta en el momento, incluso paso a paso.'],
 antes='Tené a mano el archivo CobroParaLlevar.psc de la Práctica 1.',
 acts=[
  dict(titulo='¿En qué nivel está cada fragmento?', objetivo='Clasificar cinco fragmentos nuevos según su nivel e indicar qué herramienta necesita cada uno para ejecutarse.',
       modelo=('Fragmentos', ['(a) 0100 1000 0110 1001', '(b) ADD R2, R3', '(c) print(precio * 2)', '(d) Escribir "Total: ", total', '(e) MOV R1, 5000']),
       pasos=['Armá una tabla con tres columnas: fragmento, nivel y herramienta que necesita.', 'Ubicá primero el fragmento que la CPU ejecuta sin ayuda.', 'Para los de alto nivel, anotá si los conocés de algún lenguaje.'],
       control='Ningún fragmento quedó sin nivel y cada herramienta anotada corresponde al nivel que le asignaste.'),
  dict(titulo='Tres errores provocados a propósito', objetivo='Provocar en PSeInt un error de cada tipo y registrar cuándo aparece y quién lo detecta.',
       modelo=('Tabla para completar', ['Tipo de error | Qué cambiaste | Cuándo apareció | Quién lo detectó']),
       pasos=['Sintaxis: abrí CobroParaLlevar.psc, borrá la línea FinSi y pulsá Ejecutar. Copiá el mensaje que muestra PSeInt y volvé a escribir FinSi.', 'Lógica: cambiá el cálculo para que sume el precio del mbeju en vez de multiplicarlo (cantMbeju + 5000). Ejecutá con 3, 2 y 50.000 y compará con tu papel.', 'Ejecución: agregá al final las líneas Definir ventasDelDia Como Entero, ventasDelDia <- 0 y Escribir total / ventasDelDia. Ejecutá y anotá qué pasa. Al intentar dividir por cero, el problema aparece durante la ejecución. Registrá el mensaje exacto mostrado por la versión de PSeInt instalada.', 'Usá el botón Ejecutar paso a paso en la versión correcta y observá cómo PSeInt avanza línea por línea.'],
       control='Tu tabla tiene un error de cada tipo. En la fila del error de lógica, la columna «quién lo detectó» no puede decir «PSeInt».'),
 ],
 desafio='Si tu versión de PSeInt ofrece exportar el algoritmo a otros lenguajes (menú Archivo), exportalo a C o a Python y comparalo con tu pseudocódigo: ¿qué líneas se parecen y cuáles cambiaron?',
 sol=dict(resultado='Act. 1: (a) máquina, no necesita traductor; (b) ensamblador, necesita un ensamblador; (c) alto nivel (Python), intérprete/runtime; (d) alto nivel (pseudocódigo), lo interpreta PSeInt; (e) ensamblador. Act. 2: sintaxis → al intentar ejecutar, lo detecta PSeInt con mensaje y línea; lógica → corre sin aviso y muestra un total distinto del de papel (lo detecta la persona); ejecución → el programa arranca y, al llegar a la división entre cero, PSeInt lo detiene con un mensaje. Comprobado en PSeInt 20250314 (perfil Flexible): sin FinSi aparece «ERROR 117: Falta cerrar SI.» antes de ejecutar; con cantMbeju + 5000 el programa muestra «Total: 18003  Vuelto: 31997» sin ningún aviso; con la división, primero muestra el total y el vuelto y luego se detiene con «ERROR 296: Division por cero». En otras versiones el texto puede variar: vale el mensaje que registre el estudiante.',
          errores='Clasificar (d) como «no es lenguaje»; creer que el error de lógica lo marca PSeInt; corregir el error de sintaxis sin leer el mensaje completo.'))

PR[3] = dict(
 titulo='Paradigmas en la biblioteca y un acumulador en PSeInt', entorno=PSEINT,
 competencia='Reconocer paradigmas en fragmentos nuevos y programar en estilo estructurado un recorrido con acumulador.',
 saber=['Imperativo/estructurado: pasos, decisiones y repeticiones. Orientado a objetos: objetos con datos y acciones. Lógico: hechos y reglas. Funcional: funciones que se combinan. Eventos: el programa responde a acciones del usuario. Declarativo: se pide el qué, no el cómo.',
        'Un acumulador es una variable que empieza en 0 y en cada vuelta suma un valor nuevo.'],
 antes='En PSeInt (perfil Flexible), la estructura Para i <- 1 Hasta 6 Hacer … FinPara repite seis veces lo que está adentro.',
 acts=[
  dict(titulo='¿Qué paradigma es?', objetivo='Clasificar seis fragmentos del sistema de una biblioteca escolar.',
       modelo=('Fragmentos', ['(a) Para cada libro de la lista: si está prestado, sumar 1 al contador.', '(b) libro.prestar(socio)', '(c) socio_habilitado(X) si no_tiene_deudas(X).', '(d) Al hacer clic en «Buscar», mostrar los resultados.', '(e) suma(map(precio, compras))', '(f) Contar los préstamos de marzo, pedido a la base de datos.']),
       pasos=['Leé cada fragmento y subrayá la palabra que delata el paradigma (para cada, objeto con punto, si…, al hacer clic, función aplicada a una lista, pedido a la base).', 'Escribí el paradigma y una frase que lo justifique.'],
       control='Clasificaste los seis fragmentos, justificaste cada elección con una evidencia del enunciado y no asignaste dos categorías por simple intuición.'),
  dict(titulo='La recaudación de una semana, con acumulador', objetivo='Programar en PSeInt la suma de los seis importes de la semana del 9 al 11 de marzo y su promedio.',
       modelo=('Importes de la semana (en guaraníes)', ['19.000 · 17.000 · 29.000 · 19.000 · 9.000 · 42.000']),
       pasos=['Definí total, importe e i como Entero y promedio como Real; inicializá total en 0.', 'Usá Para i <- 1 Hasta 6 Hacer: leé el importe y sumalo a total.', 'Después del ciclo, calculá promedio <- total / 6 y mostrá los dos valores.', 'Antes de ejecutar, completá en papel una traza con el valor de total al terminar cada vuelta.'],
       control='El último valor de tu traza coincide con el total que muestra PSeInt, y el promedio multiplicado por 6 da ese mismo total.'),
 ],
 desafio='Agregá un contador que diga cuántas ventas superaron G. 20.000.',
 sol=dict(resultado='Act. 1: (a) estructurado/imperativo; (b) orientado a objetos; (c) lógico; (d) dirigido por eventos; (e) funcional; (f) declarativo. Act. 2: traza 19.000 → 36.000 → 65.000 → 84.000 → 93.000 → 135.000; total G. 135.000; promedio G. 22.500 (PSeInt muestra «Total: 135000» y «Promedio: 22500»). Desafío: 2 ventas (29.000 y 42.000). Todo se ejecutó en PSeInt 20250314 con el perfil Flexible.',
          errores='Inicializar total dentro del ciclo (el programa termina mostrando solo el último importe, 42000); dividir antes de terminar el ciclo; definir promedio como Entero (con estos importes la división es exacta y no falla, pero con un promedio no entero PSeInt se detiene con «No coinciden los tipos»); no definir i; confundir lógico con estructurado porque ambos tienen «si».'))

PR[4] = dict(
 titulo='Elegir la tecnología para la biblioteca escolar', entorno=PAPEL,
 competencia='Construir y documentar una matriz de decisión ponderada para elegir la tecnología de un sistema real, y analizar cuánto depende la decisión de los pesos elegidos.',
 saber=['La matriz ponderada multiplica el puntaje de cada opción por el peso de cada criterio y suma. Los pesos suman 1.',
        'Una decisión técnica se documenta: criterios, pesos, puntajes, ganador y riesgos.'],
 antes='Caso: la biblioteca del colegio quiere que los estudiantes reserven libros desde el celular y que la bibliotecaria registre préstamos desde la computadora.',
 acts=[
  dict(titulo='La matriz de decisión', objetivo='Calcular el puntaje de tres opciones con los criterios y los pesos que fijó la dirección.',
       modelo=('Datos de la dirección', ['Criterios y pesos: funciona en el navegador del celular 0,5 · hay programadores disponibles 0,3 · costo de herramientas (más alto = más barato) 0,2', 'Opción X — sistema web (JavaScript + lenguaje de servidor): 9 · 8 · 9', 'Opción Y — programa de escritorio en C#: 3 · 8 · 7', 'Opción Z — app Android nativa en Kotlin: 7 · 6 · 8']),
       pasos=['Verificá que los pesos sumen 1.', 'Armá la tabla: opción, tres productos (puntaje × peso) y total.', 'Ordená las opciones de mayor a menor.'],
       control='Cada total está entre 1 y 10 y coincide con el que obtiene un compañero que calcula por separado.'),
  dict(titulo='¿Y si cambian las prioridades?', objetivo='Recalcular la matriz con otros pesos y comprobar si la decisión se sostiene.',
       modelo=('Nuevos pesos (la cooperadora prioriza el costo)', ['navegador del celular 0,2 · programadores 0,3 · costo 0,5 (mismos puntajes)']),
       pasos=['Recalculá los tres totales.', 'Compará el orden con el de la Actividad 1.', 'Escribí una conclusión de dos oraciones: ¿la decisión es robusta o depende mucho de los pesos?'],
       control='Tus dos tablas tienen las mismas opciones y los mismos puntajes; solo cambiaron los pesos.'),
  dict(titulo='Chequeo de ecosistema y ficha de decisión', objetivo='Pasar la opción ganadora por el chequeo de ecosistema y dejar la decisión documentada.',
       modelo=('Ficha de decisión (completala)', ['Fecha · Problema · Criterios y pesos · Opciones y puntajes · Decisión · Chequeo de ecosistema (librerías, entorno, documentación, comunidad) · Riesgos']),
       pasos=['Respondé las cuatro preguntas del chequeo de ecosistema para la opción ganadora.', 'Anotá un riesgo de la decisión y cómo lo mitigarías.', 'Completá la ficha con letra clara: la va a leer otra persona.'],
       control='La ficha tiene sus siete campos completos y el riesgo anotado no repite un criterio de la matriz.'),
 ],
 desafio='Proponé un criterio que la dirección olvidó (por ejemplo, la protección de los datos personales de los estudiantes), asignale un peso y explicá si cambiaría la decisión.',
 sol=dict(resultado='Act. 1: X = 9×0,5 + 8×0,3 + 9×0,2 = 4,5 + 2,4 + 1,8 = 8,7; Z = 3,5 + 1,8 + 1,6 = 6,9; Y = 1,5 + 2,4 + 1,4 = 5,3. Orden X > Z > Y. Act. 2: X = 1,8 + 2,4 + 4,5 = 8,7; Z = 1,4 + 1,8 + 4,0 = 7,2; Y = 0,6 + 2,4 + 3,5 = 6,5. X sigue ganando: decisión robusta. Act. 3: ficha completa; riesgo posible: dependencia de conexión a internet (mitigación: modo de consulta del catálogo impreso).',
          errores='Sumar puntajes sin multiplicar por el peso; pesos que no suman 1; cambiar los puntajes al cambiar los pesos; ficha sin riesgos.'))

PR[5] = dict(
 titulo='Del cuaderno de préstamos a datos estructurados', entorno=PAPEL,
 competencia='Transformar los registros desordenados de un cuaderno en datos estructurados, y detectar redundancias, inconsistencias y problemas de calidad.',
 saber=['Estructurar es separar cada hecho en sus piezas (quién, qué, cuándo) sin perder la posibilidad de reconstruirlo.',
        'La calidad de un dato se juzga por su exactitud, completitud, actualidad, consistencia y unicidad.'],
 antes='Este es el cuaderno de préstamos de la biblioteca del colegio, copiado tal como está escrito.',
 acts=[
  dict(titulo='Identificar las piezas', objetivo='Separar socios, libros y préstamos, y asignar un código a cada uno.',
       modelo=('Cuaderno de la biblioteca', ['1) 03/03 – Lucía Ortiz (3.º A) llevó «Hijo de hombre», de Augusto Roa Bastos.', '2) 03/03 – Marcos Rojas (2.º B) llevó «El trueno entre las hojas», de Roa Bastos.', '3) 04/03 – Lucia Ortiz (3A) llevó «La babosa», de Gabriel Casaccia.', '4) 05/03 – Marcos Rojas (2.º B) devolvió «El trueno entre las hojas».', '5) 05/03 – Ana Paula Vera (1.º C) llevó «Hijo de Hombre», de A. Roa Bastos.', '6) 05/03 – Ana Paula Vera (1.º C) llevó «Hijo de hombre».']),
       pasos=['Hacé tres listas: socios, libros y préstamos.', 'Asigná códigos: S01, S02… a los socios y L01, L02… a los libros.', 'Reescribí cada préstamo como (código de socio, código de libro, fecha).'],
       control='Ningún código se repite y ninguna persona ni libro aparece con dos códigos. Para cada renglón del cuaderno podés decir si generó un préstamo y por qué.'),
  dict(titulo='Detectar los problemas del cuaderno', objetivo='Señalar las redundancias, las inconsistencias y las fallas de calidad.',
       modelo=('Tabla para completar', ['Renglón · Problema · Dimensión de calidad afectada · Cómo lo evita una base de datos']),
       pasos=['Compará los renglones 1 y 3, y los renglones 5 y 6.', 'Buscá un mismo dato escrito de dos maneras distintas.', 'Decidí qué tiene de especial el renglón 4.'],
       control='Encontraste al menos cuatro problemas distintos y cada uno tiene su dimensión de calidad.'),
  dict(titulo='Dato, información y conocimiento', objetivo='Clasificar enunciados sobre la biblioteca y decidir qué se guarda una sola vez.',
       modelo=('Enunciados', ['(a) «L01»', '(b) «Lucía Ortiz llevó Hijo de hombre el 03/03»', '(c) «Las novelas de Roa Bastos son las más pedidas por 3.er curso»', '(d) «05/03»']),
       pasos=['Clasificá cada enunciado.', 'Hacé la lista de los datos que la biblioteca guardaría una sola vez.'],
       control='Cada clasificación está justificada con la definición de dato, información o conocimiento.'),
 ],
 desafio='El renglón 4 registra una devolución. Proponé cómo guardarla en tu estructura sin crear un préstamo nuevo.',
 sol=dict(resultado='Act. 1: socios S01 Lucía Ortiz (3.º A), S02 Marcos Rojas (2.º B), S03 Ana Paula Vera (1.º C); libros L01 Hijo de hombre (Roa Bastos), L02 El trueno entre las hojas (Roa Bastos), L03 La babosa (Casaccia); préstamos (S01, L01, 03/03), (S02, L02, 03/03), (S01, L03, 04/03), (S03, L01, 05/03). Son 4 préstamos en 6 renglones: el 4 es una devolución y el 6 repite el 5. Act. 2: «Lucía/Lucia» y «3.º A/3A» (consistencia); «Hijo de hombre/Hijo de Hombre» y «Roa Bastos/A. Roa Bastos» (consistencia); renglón 6 duplicado (unicidad); el autor repetido en cada préstamo (redundancia); renglón 6 sin autor (completitud). Act. 3: (a) dato; (b) información; (c) conocimiento; (d) dato. Se guardan una vez: socios con su curso y libros con su autor. Desafío: agregar fecha_devolución al préstamo 102 (S02, L02) = 05/03.',
          errores='Dar dos códigos a Lucía; contar la devolución como préstamo; no ver el duplicado; tomar «A. Roa Bastos» como otro autor.'))

PR[6] = dict(
 titulo='El catálogo de la biblioteca como tabla relacional', entorno=PAPEL,
 competencia='Construir una tabla relacional nueva, reconocer sus partes y decidir el modelo y la infraestructura adecuados para distintos escenarios.',
 saber=['En el modelo relacional cada tabla guarda un tipo de cosa: una fila por ejemplar del tipo y una columna por dato.',
        'Base local: un solo puesto, sin red. Base en servidor: muchos usuarios a la vez, con red.'],
 antes='Datos de cinco libros: Hijo de hombre, Augusto Roa Bastos, 1960, novela · El trueno entre las hojas, Augusto Roa Bastos, 1953, cuentos · La babosa, Gabriel Casaccia, 1952, novela · Yo el Supremo, Augusto Roa Bastos, 1974, novela · Don Quijote de la Mancha, Miguel de Cervantes, 1605, novela.',
 acts=[
  dict(titulo='La tabla Libros', objetivo='Armar la tabla Libros con código, título, autor, año y género.',
       modelo=('Encabezado de la tabla', ['código | título | autor | año | género']),
       pasos=['Asigná los códigos L01 a L05 en el orden de la lista.', 'Cargá una fila por libro.', 'Pintá una fila (registro) y una columna (campo) con dos colores distintos.', 'Marcá qué columna serviría como clave principal y por qué el título no sirve.'],
       control='Tu tabla tiene una columna por dato y una fila por libro; ninguna celda tiene dos valores.'),
  dict(titulo='Modelo e infraestructura', objetivo='Elegir el modelo de datos y decidir entre base local o en servidor para cinco escenarios.',
       modelo=('Escenarios', ['(a) La biblioteca escolar, con una sola computadora.', '(b) La red de bibliotecas municipales de un departamento, que comparten el catálogo.', '(c) Una app de lectura con millones de reseñas de formatos muy variados.', '(d) El organigrama fijo del colegio.', '(e) Un supermercado con ocho cajas.']),
       pasos=['Para cada escenario elegí el modelo (jerárquico, en red, relacional, NoSQL).', 'Decidí local o servidor, salvo en (d).', 'Justificá con una característica de la tabla de la clase.'],
       control='Cada decisión está justificada con una característica (usuarios simultáneos, red, tipo de datos), no con «porque sí».'),
  dict(titulo='El archivo de la base, por dentro', objetivo='Planificar qué objetos tendría el archivo Biblioteca.accdb.',
       modelo=('Familias de objetos', ['tablas · consultas · formularios · informes']),
       pasos=['Proponé dos objetos de cada familia para la biblioteca.', 'Clasificá los objetos según su función principal: datos y consulta (tablas y consultas) o interfaz y presentación (formularios e informes). Recordá que Access integra ambas funciones en una misma herramienta.'],
       control='Tenés ocho objetos y cada uno tiene un nombre que dice qué hace.'),
 ],
 desafio='Proponé una segunda tabla, Socios, y explicá con qué tabla tendría que unirse para saber quién tiene cada libro.',
 sol=dict(resultado='Act. 1: Libros(L01 Hijo de hombre, Roa Bastos, 1960, novela; L02 El trueno entre las hojas, Roa Bastos, 1953, cuentos; L03 La babosa, Casaccia, 1952, novela; L04 Yo el Supremo, Roa Bastos, 1974, novela; L05 Don Quijote de la Mancha, Cervantes, 1605, novela). Clave: código; el título puede repetirse (ediciones, homónimos) y puede corregirse. Act. 2: (a) relacional, local; (b) relacional, servidor; (c) NoSQL, servidor; (d) jerárquico; (e) relacional, servidor. Act. 3: p. ej. tablas Libros y Socios; consultas «Libros prestados» y «Préstamos por curso»; formularios «Registrar préstamo» y «Alta de socio»; informes «Libros más pedidos» y «Préstamos vencidos». Tablas y consultas pertenecen principalmente a la capa de datos/consulta; formularios e informes, a la capa de interfaz/presentación. En Access las cuatro familias son objetos de la misma aplicación y trabajan integradas. Desafío: Socios se une a Libros a través de una tabla Préstamos.',
          errores='Poner autor y año en la misma celda; elegir el título como clave; decidir «servidor» para la biblioteca de una sola PC.'))

PR[7] = dict(
 titulo='La cantina del colegio: problemas que resuelve un SGBD', entorno=PAPEL,
 competencia='Diagnosticar los problemas del manejo desordenado de datos y proponer la función del SGBD que los resuelve: permisos, transacciones y concurrencia.',
 saber=['Redundancia: un dato repetido. Inconsistencia: copias que no coinciden. El SGBD guarda una sola vez, controla permisos, agrupa operaciones en transacciones y ordena los accesos simultáneos.'],
 antes='La cantina del colegio lleva dos planillas: una en la caja y otra en el depósito.',
 acts=[
  dict(titulo='Dos planillas, un problema', objetivo='Detectar redundancia, inconsistencia y dificultad de acceso comparando las planillas.',
       modelo=('Planillas de la cantina', ['Caja: Jugo G. 5.000 · Sándwich G. 7.000 · Agua G. 3.000', 'Depósito: Jugo G. 5.500 · Sándwich G. 7.000 · Agua mineral G. 3.000 · Stock: Jugo 12, Sándwich 4, Agua mineral 20']),
       pasos=['Marcá los datos que están en las dos planillas.', 'Marcá los que no coinciden.', 'Escribí qué pregunta no se puede responder sin juntar las dos planillas a mano.'],
       control='Cada problema que nombraste tiene un ejemplo concreto de las planillas y la consecuencia que tiene para la cantina.'),
  dict(titulo='Quién puede qué', objetivo='Armar la matriz de permisos de la cantina aplicando el mínimo privilegio.',
       modelo=('Matriz para completar (Sí/No)', ['Roles: dueña · cajera · repositor', 'Operaciones: consultar precios · registrar venta · cambiar precio · cargar stock · borrar producto']),
       pasos=['Completá la matriz.', 'Justificá un «No» de cada rol.'],
       control='Ninguna persona tiene un permiso que no necesita para su trabajo, y toda operación la puede hacer al menos una persona.'),
  dict(titulo='Todo o nada', objetivo='Simular una transacción con falla y relacionar cada propiedad ACID con un hecho.',
       modelo=('Venta de la cantina', ['Insertar venta 501 · renglón 1: 2 jugos · renglón 2: 1 sándwich · renglón 3: 1 agua mineral · falla al guardar el renglón 3']),
       pasos=['Escribí qué queda guardado al volver el sistema y por qué.', 'Asociá: (a) «la venta confirmada no se pierde con un corte de luz»; (b) «la venta no queda por la mitad»; (c) «dos cajas que venden a la vez no se pisan»; (d) «el stock nunca queda negativo».'],
       control='Tu respuesta sobre la falla y cada asociación están justificadas con el nombre de la propiedad y su definición.'),
 ],
 desafio='Quedan 1 sándwich en stock y dos cajeras lo venden en el mismo segundo. Explicá qué debe hacer el SGBD y qué ve cada cajera.',
 sol=dict(resultado='Act. 1: redundancia (los tres productos y sus precios en las dos planillas); inconsistencia (jugo 5.000 vs 5.500; «Agua» vs «Agua mineral»); dificultad de acceso («¿cuánto vale el stock de jugo a precio de venta?» exige cruzar a mano). Act. 2: dueña: todo Sí; cajera: consultar precios y registrar venta; repositor: consultar precios y cargar stock; borrar producto y cambiar precio solo la dueña. Act. 3: no queda nada de la venta 501 (atomicidad); (a) durabilidad; (b) atomicidad; (c) aislamiento; (d) consistencia. Desafío: control de concurrencia: la primera transacción toma el registro; la segunda espera y, al ver stock 0, se rechaza con aviso.',
          errores='Confundir redundancia con inconsistencia; dar a la cajera permiso de cambiar precios; creer que quedan guardados los renglones 1 y 2.'))

PR[8] = dict(
 titulo='Claves de la biblioteca', entorno=PAPEL,
 competencia='Elegir claves principales con criterio, reconocer claves alternativas, foráneas y compuestas, y seguir las referencias entre tablas.',
 saber=['Clave principal: única, estable y nunca vacía. Clave alternativa: otro campo que también sería único. Clave foránea: apunta a la clave principal de otra tabla. Clave compuesta: dos o más campos juntos.'],
 antes='La biblioteca organizó sus datos en tres tablas.',
 acts=[
  dict(titulo='Candidatas a clave', objetivo='Evaluar los candidatos a clave principal de Socios y Libros.',
       modelo=('Tablas de la biblioteca', ['Socios(cod_socio, cédula, nombre, curso, email)', 'Libros(cod_libro, ISBN, título, autor)', 'Préstamos(nro_préstamo, cod_socio, cod_libro, fecha)']),
       pasos=['Para cada campo de Socios, respondé: ¿es único?, ¿es estable?, ¿puede quedar vacío?', 'Elegí la clave principal de cada tabla y nombrá las claves alternativas.'],
       control='Cada tabla tiene exactamente una clave principal; las alternativas cumplen la unicidad.'),
  dict(titulo='Seguir las flechas', objetivo='Marcar las claves foráneas y recorrerlas con datos.',
       modelo=('Datos', ['Socios: S01 Lucía Ortiz (3.º A) · S02 Marcos Rojas (2.º B) · S03 Ana Paula Vera (1.º C)', 'Libros: L01 Hijo de hombre · L02 El trueno entre las hojas · L03 La babosa', 'Préstamos: 101 (S01, L01, 03/03) · 102 (S02, L02, 03/03) · 103 (S01, L03, 04/03) · 104 (S03, L01, 05/03)']),
       pasos=['Dibujá las tres tablas y trazá una flecha desde cada clave foránea hacia la clave principal que referencia.', 'Respondé: ¿quiénes llevaron L01?, ¿qué libros llevó S01?, ¿a qué curso pertenece quien hizo el préstamo 102?'],
       control='Cada flecha sale de una clave foránea y llega a la clave principal que referencia, y respondiste las tres preguntas recorriendo las flechas.'),
  dict(titulo='Una clave de dos campos', objetivo='Encontrar la clave de una tabla de horarios y asignar tipos de datos.',
       modelo=('Horario (fragmento)', ['3.º A · lunes · 1.ª hora · Algorítmica', '3.º A · lunes · 2.ª hora · Algorítmica', '3.º B · lunes · 1.ª hora · Matemática', '3.º A · martes · 1.ª hora · Inglés']),
       pasos=['Probá si curso, día u hora identifican solos una fila.', 'Encontrá la combinación mínima que identifica.', 'Asigná un tipo de dato a cada campo de Préstamos.'],
       control='Tu clave compuesta no tiene campos de más: si quitás uno, deja de identificar.'),
 ],
 desafio='La biblioteca compra un segundo ejemplar de «Hijo de hombre». ¿Puede el ISBN seguir siendo clave? Proponé una solución.',
 sol=dict(resultado='Act. 1: Socios: clave cod_socio; alternativas cédula (si todos la tienen) y email (si es obligatorio y único); el nombre no sirve (puede repetirse y cambiar). Libros: clave cod_libro; ISBN alternativa (mientras haya un ejemplar por título). Préstamos: nro_préstamo. Act. 2: FK cod_socio → Socios y cod_libro → Libros. L01: Lucía (101) y Ana Paula (104). S01: L01 y L03. El préstamo 102 es de Marcos, 2.º B. Act. 3: ninguno identifica solo; clave compuesta (curso, día, hora). Tipos: nro_préstamo Número o Autonumeración; cod_socio y cod_libro Texto corto; fecha Fecha/Hora. Desafío: no, porque el ISBN se repite entre ejemplares; se agrega cod_ejemplar como clave de una tabla Ejemplares (con ISBN como dato).',
          errores='Elegir el nombre como clave; trazar flechas desde la principal hacia la foránea; clave compuesta con (curso, día, hora, materia), que sobra.'))

PR[9] = dict(
 titulo='La integridad referencial pone orden en la biblioteca', entorno=PAPEL,
 competencia='Predecir la reacción del SGBD ante operaciones que afectan relaciones, con distintas configuraciones, y reconocer las tres integridades y el valor nulo.',
 saber=['Restringir rechaza la orden mientras haya registros que apuntan; eliminar en cascada borra también los dependientes; actualizar en cascada corrige las referencias.'],
 antes='Usá las tablas y los datos de la Práctica 8 (socios S01–S03, libros L01–L03, préstamos 101–104).',
 acts=[
  dict(titulo='¿Acepta o rechaza?', objetivo='Decidir la reacción del SGBD (configurado para restringir) ante seis operaciones.',
       modelo=('Operaciones', ['(a) Registrar el préstamo 105 del socio S04.', '(b) Borrar al socio S02.', '(c) Borrar el libro L03.', '(d) Agregar el libro L04 «Yo el Supremo».', '(e) Borrar el préstamo 102.', '(f) Cambiar el código S01 por S10, con «Actualizar en cascada» activado.']),
       pasos=['Para cada operación, buscá qué registros apuntan al afectado.', 'Escribí «acepta» o «rechaza» y nombrá el registro que provoca el rechazo.'],
       control='Cada rechazo nombra al registro que lo provoca; cada aceptación explica por qué no rompe ninguna relación.'),
  dict(titulo='La cascada, con números', objetivo='Calcular qué se borra si la relación Socios–Préstamos se configura con «Eliminar en cascada».',
       modelo=('Orden', ['Borrar al socio S01.']),
       pasos=['Listá los préstamos que se borrarían.', 'Contá cuántos préstamos quedan en la base.', 'Decidí si conviene esa configuración en una biblioteca y justificá.'],
       control='La cantidad de préstamos que quedan, más los borrados, da los préstamos que había.'),
  dict(titulo='Tres integridades y un nulo', objetivo='Clasificar violaciones e interpretar el valor nulo.',
       modelo=('Situaciones', ['(a) Dos libros con el código L02.', '(b) Un préstamo con fecha 31/02/2026.', '(c) Un préstamo del libro L09, que no existe.', '(d) El préstamo 104 tiene la fecha de devolución vacía (nula).']),
       pasos=['Clasificá (a), (b) y (c) como de entidad, de dominio o referencial.', 'Explicá qué significa el nulo de (d) y cómo lo buscarías.'],
       control='Cada clasificación nombra la regla que se viola y el dato que la viola.'),
 ],
 desafio='Proponé la configuración completa (exigir integridad, actualizar en cascada, eliminar en cascada) para la relación Socios–Préstamos y para Libros–Préstamos, y justificá.',
 sol=dict(resultado='Act. 1: (a) rechaza: S04 no existe; (b) rechaza: lo referencia el préstamo 102; (c) rechaza: lo referencia el 103; (d) acepta: no apunta a nadie; (e) acepta: ningún registro apunta a un préstamo; (f) acepta y corrige 101 y 103 a S10. Act. 2: se borran 101 y 103; quedan 2 (102 y 104); no conviene: se pierde la historia de préstamos. Act. 3: (a) entidad; (b) dominio; (c) referencial; (d) el libro aún no se devolvió; se busca con Es Nulo en fecha de devolución. Desafío: en ambas relaciones, exigir integridad sí, actualizar en cascada sí, eliminar en cascada no.',
          errores='Aceptar (b) porque «el socio existe»; creer que borrar un préstamo afecta al socio; tomar el nulo como cero o como «sin fecha válida».'))

PR[10] = dict(
 titulo='Lenguajes, usuarios y vistas de la biblioteca', entorno=PAPEL,
 competencia='Clasificar tareas en DDL y DML, reconocer tipos de usuario y diseñar vistas respetando la independencia de datos.',
 saber=['DDL define la estructura; DML trabaja con el contenido. Cada usuario ve la base a través de su vista; la independencia permite cambiar un nivel sin romper los otros.'],
 antes='Trabajamos sobre la base de la biblioteca de las prácticas anteriores.',
 acts=[
  dict(titulo='¿DDL o DML?', objetivo='Clasificar ocho tareas.',
       modelo=('Tareas', ['(a) Crear la tabla Socios.', '(b) Agregar el campo email a Socios.', '(c) Registrar el préstamo 105.', '(d) Corregir el título mal escrito de L03.', '(e) Borrar la tabla Temporal.', '(f) Consultar los libros prestados hoy.', '(g) Eliminar al socio S03, que no tiene préstamos.', '(h) Crear un índice sobre el título de Libros.']),
       pasos=['Marcá DDL o DML.', 'Para (e) y (g), explicá la diferencia entre borrar el molde y sacar un registro.'],
       control='Cada tarea que modifica la estructura (tablas, campos, índices) quedó como DDL.'),
  dict(titulo='¿Qué tipo de usuario es?', objetivo='Clasificar a cinco personas que usan la base.',
       modelo=('Personas', ['(a) La bibliotecaria, que registra préstamos con un formulario.', '(b) El profesor de Informática, que escribe sus propias consultas para un informe.', '(c) Una estudiante que programa una app que se conecta a la base.', '(d) Un técnico que desarrolla un sistema especial de catalogación con imágenes de portadas.', '(e) Quien crea los usuarios, asigna permisos y programa los respaldos.']),
       pasos=['Asigná a cada persona su tipo de usuario.', 'Indicá qué nivel de abstracción usa cada una.'],
       control='Cada asignación está justificada con lo que hace la persona y con la forma en que accede a la base.'),
  dict(titulo='Dos vistas y tres cambios', objetivo='Diseñar dos vistas y predecir qué nivel afecta cada cambio.',
       modelo=('Vistas pedidas y cambios', ['Vista para estudiantes: catálogo disponible.', 'Vista para la dirección: cantidad de préstamos por curso.', 'Cambios: (1) mover la base a un disco más rápido; (2) agregar el campo editorial a Libros; (3) crear la vista de la dirección.']),
       pasos=['Para cada vista, listá los campos que muestra y los que oculta.', 'Indicá el nivel afectado por cada cambio y si la otra vista se entera.'],
       control='Ninguna vista muestra datos personales a quien no los necesita.'),
 ],
 desafio='Escribí con tus palabras la orden DDL que crearía la tabla Socios (nombre de la tabla, campos, tipos y clave).',
 sol=dict(resultado='Act. 1: DDL: (a), (b), (e), (h); DML: (c), (d), (f), (g). Borrar la tabla destruye el molde y todo su contenido; eliminar un registro deja la tabla. Act. 2: (a) usuario normal (vistas); (b) sofisticado (lógico); (c) programador de aplicaciones (lógico); (d) especializado; (e) administrador de la base (físico y lógico). Act. 3: estudiantes: título, autor y disponibilidad, sin datos de socios; dirección: curso y cantidad de préstamos, sin nombres. (1) físico, nadie se entera; (2) lógico, las vistas que no lo usan siguen iguales; (3) externo, solo la dirección. Desafío: crear tabla Socios con cod_socio (texto, clave principal), cédula (texto), nombre (texto), curso (texto) y email (texto).',
          errores='Clasificar «crear índice» como DML; confundir usuario sofisticado con programador; vista de estudiantes que muestra quién tiene cada libro.'))

PR[11] = dict(
 titulo='El mini-mundo del club deportivo', entorno=PAPEL,
 competencia='Relevar requisitos a partir de una entrevista, delimitar el mini-mundo y formular las preguntas que el modelo debe responder.',
 saber=['El mini-mundo es la porción de la realidad que entra en el modelo. Se delimita con la necesidad del cliente y se documenta lo que queda afuera.'],
 antes='Leé la entrevista con el presidente del Club Atlético Yvága, un club de barrio inventado para esta práctica.',
 acts=[
  dict(titulo='Leer la entrevista y delimitar', objetivo='Decidir qué entra y qué queda afuera del mini-mundo.',
       modelo=('Entrevista (resumen)', ['«Tenemos unos 200 socios y tres disciplinas: fútbol, vóley y básquet. Cada socio paga una cuota mensual y quiero saber quién está al día.»', '«Un socio puede anotarse en varias disciplinas; cada disciplina tiene un solo entrenador, pero un entrenador puede tener más de una.»', '«La cantina la maneja otra comisión, y el arreglo de la cancha lo vemos aparte.»', '«Quiero saber cuántos socios hay por disciplina y quién debe cuotas.»']),
       pasos=['Subrayá en la entrevista los sustantivos que podrían ser entidades.', 'Hacé dos listas: «entra» y «queda afuera», con el motivo de cada decisión.'],
       control='Todo lo que pusiste en «queda afuera» tiene un motivo escrito.'),
  dict(titulo='Las preguntas que el modelo debe responder', objetivo='Escribir la lista de preguntas del presidente y verificar el mini-mundo contra ella.',
       modelo=('Formato', ['Pregunta del club → datos del mini-mundo que la responden']),
       pasos=['Escribí al menos cuatro preguntas que el sistema debe responder.', 'Al lado de cada una, anotá qué datos del mini-mundo usa.', 'Indicá qué modelo de datos vas a usar y en qué fase del diseño estás.'],
       control='Cada pregunta se responde con algo de tu mini-mundo y nada de tu mini-mundo sobra.'),
 ],
 desafio='El club quiere sumar en el futuro la venta de la cantina. Escribí cómo documentarías hoy esa decisión para que nadie la olvide.',
 sol=dict(resultado='Act. 1: entran socios, disciplinas, entrenadores, inscripciones de socios a disciplinas y cuotas mensuales (con su pago). Quedan afuera la cantina (otra comisión) y el mantenimiento de la cancha (no responde a ninguna pregunta). Act. 2: ¿quién está al día con la cuota? (socios + cuotas); ¿cuántos socios hay por disciplina? (inscripciones); ¿quién entrena cada disciplina? (entrenadores); ¿qué cuotas debe un socio? (cuotas impagas). Modelo entidad-relación, fase conceptual. Desafío: registro de alcance con fecha, motivo y responsable: «cantina fuera del alcance de la versión 1».',
          errores='Incluir la cantina «por las dudas»; listar entidades sin preguntas; confundir la fase conceptual con la física.'))

PR[12] = dict(
 titulo='Las entidades del club: socios y disciplinas', entorno=PAPEL,
 competencia='Clasificar atributos, definir dominios, elegir identificadores y dibujarlos con la notación del DER.',
 saber=['Simple/compuesto, univalorado/multivalorado y derivado son tres preguntas independientes sobre cada atributo. El identificador va subrayado; el multivaluado, con doble elipse; el derivado, punteado.'],
 antes='Seguimos con el Club Atlético Yvága de la Práctica 11.',
 acts=[
  dict(titulo='La ficha de SOCIO', objetivo='Clasificar los atributos de SOCIO y definir sus dominios.',
       modelo=('Atributos relevados', ['nro_socio · cédula · nombre completo · fecha de nacimiento · edad · dirección (calle, número y barrio) · teléfonos · categoría (infantil, juvenil o mayor, según la edad) · fecha de alta']),
       pasos=['Armá una tabla: atributo, simple o compuesto, univalorado o multivalorado, ¿derivado?, dominio.', 'Elegí el identificador y explicá por qué no elegiste la cédula.', 'Dibujá SOCIO con todos sus atributos en notación clásica.'],
       control='Los atributos derivados están punteados y en tu tabla dice que no se guardan.'),
  dict(titulo='DISCIPLINA y sus horarios', objetivo='Decidir cómo tratar un atributo multivaluado.',
       modelo=('Atributos de DISCIPLINA', ['código · nombre · cuota mensual · horarios (por ejemplo, lunes 18:00 y jueves 18:00)']),
       pasos=['Clasificá cada atributo.', 'Proponé el tratamiento de horarios en el diseño.', 'Escribí el dominio de cuota mensual.'],
       control='Tu propuesta para horarios no deja dos valores en una misma celda.'),
 ],
 desafio='Cada cuota se identifica por el socio y el número de mes (cuota 3 del socio 15). ¿Es CUOTA una entidad fuerte o débil? Dibujala.',
 sol=dict(resultado='Act. 1: nro_socio simple, identificador; cédula simple (alternativa: algunos socios infantiles pueden no tenerla al asociarse); nombre completo compuesto; fecha de nacimiento simple; edad derivada (de la fecha); dirección compuesta; teléfonos multivaluado; categoría derivada (de la edad); fecha de alta simple. Dominios: nro_socio entero positivo; fechas reales; categoría {infantil, juvenil, mayor}. Act. 2: código identificador, nombre simple, cuota simple (entero positivo en guaraníes), horarios multivaluado → entidad aparte HORARIO(disciplina, día, hora) relacionada 1:N con DISCIPLINA. Desafío: débil (doble rectángulo): no existe sin el socio; nro_cuota es su discriminante (subrayado discontinuo) y la clave completa es nro_socio + nro_cuota; se une a SOCIO por una relación identificadora (doble rombo).',
          errores='Marcar categoría como atributo para cargar a mano; poner los horarios separados por comas; elegir el nombre como identificador.'))

PR[13] = dict(
 titulo='Cardinalidades del club, leídas en los datos', entorno=PAPEL,
 competencia='Determinar cardinalidad, participación y grado de relaciones nuevas a partir de datos y reglas del negocio.',
 saber=['Toda relación se lee en los dos sentidos. El par (mín, máx) de cada extremo combina participación (0 o 1) y cardinalidad (1 o N).'],
 antes='Datos del club: socios 1 Alan, 2 Belén, 3 Carlos y 4 Diana; disciplinas FUT, VOL y BAS; entrenadores Ruiz y Paredes.',
 acts=[
  dict(titulo='Leer las cardinalidades', objetivo='Determinar la cardinalidad de SOCIO–DISCIPLINA y de ENTRENADOR–DISCIPLINA.',
       modelo=('Registros', ['Inscripciones: Alan–FUT · Alan–BAS · Belén–VOL · Carlos–FUT · Diana–VOL · Diana–FUT', 'Entrena: Ruiz–FUT · Paredes–VOL · Paredes–BAS', 'Regla del club: cada disciplina tiene un solo entrenador']),
       pasos=['Para cada relación, contá cuántos del otro lado tiene cada uno (en los dos sentidos).', 'Escribí la cardinalidad y el par (mín, máx) de cada extremo.', 'Indicá cuál es la relación N:M y qué evidencia la prueba.'],
       control='Para cada relación escribiste dos lecturas, una por sentido, y una evidencia de los datos.'),
  dict(titulo='Grado y relaciones especiales', objetivo='Clasificar relaciones por su grado.',
       modelo=('Enunciados', ['(a) Un socio es padrino de otros socios nuevos.', '(b) Un entrenador dirige una disciplina en una cancha determinada, y el dato solo tiene sentido con los tres.', '(c) Un socio paga cuotas.']),
       pasos=['Indicá el grado de cada relación.', 'Dibujá (a) con sus dos roles.'],
       control='Para cada enunciado contaste cuántas entidades participan y, en (a), nombraste los dos roles.'),
 ],
 desafio='El club decide que un socio puede anotarse en dos disciplinas como máximo. ¿Sigue siendo N:M la relación? ¿Cómo lo anotarías con el par (mín, máx)?',
 sol=dict(resultado='Act. 1: SOCIO–DISCIPLINA es N:M (Alan tiene 2 disciplinas; FUT tiene 3 socios); pares SOCIO (0, N) y DISCIPLINA (0, N), o mínimo 1 si el club exige inscripción. ENTRENADOR–DISCIPLINA es 1:N (Paredes tiene 2; cada disciplina, 1); pares ENTRENADOR (1, N) y DISCIPLINA (1, 1). Act. 2: (a) unaria (roles padrino/ahijado); (b) ternaria; (c) binaria. Desafío: sigue siendo N:M, porque una disciplina tiene muchos socios y un socio puede tener más de una; el extremo de SOCIO se anota (0, 2).',
          errores='Leer un solo sentido; concluir 1:1 porque Belén tiene una sola disciplina; dibujar la unaria como dos entidades distintas.'))

PR[14] = dict(
 titulo='El DER de los talleres del colegio', entorno=PAPEL,
 competencia='Construir un DER completo y validado a partir de requisitos nuevos, con atributos de relación y cardinalidades en ambos extremos.',
 saber=['Rectángulo: entidad. Elipse: atributo (subrayado si es identificador). Rombo: relación, con sus atributos propios. Cardinalidad en los dos extremos.'],
 antes='Requisitos de la coordinación de talleres extracurriculares.',
 acts=[
  dict(titulo='Del texto al diagrama', objetivo='Dibujar el DER a partir de los requisitos.',
       modelo=('Requisitos', ['Cada alumno tiene código, nombre y curso. Cada taller tiene código, nombre y día de la semana.', 'Un alumno puede inscribirse en varios talleres y un taller tiene muchos alumnos; de cada inscripción interesa la fecha.', 'Cada taller lo dicta un solo docente, y un docente puede dictar varios talleres. Del docente interesan código, nombre y teléfono.', 'Cada taller usa un aula fija y cada aula aloja un solo taller. Del aula interesan código y capacidad.']),
       pasos=['Paso 1: dibujá las entidades.', 'Paso 2: uní con rombos y nombrá cada relación.', 'Paso 3: anotá las cardinalidades en los dos extremos.', 'Paso 4: colgá los atributos; ubicá la fecha de inscripción donde corresponde.'],
       control='Hay tantas relaciones como vínculos describen los requisitos, y cada rombo tiene nombre y cardinalidad en los dos extremos.'),
  dict(titulo='Validar el diagrama', objetivo='Pasar tu DER por la lista de control de la clase y leerlo en voz alta.',
       modelo=('Lista de control', ['¿Toda entidad tiene identificador subrayado?', '¿Toda relación tiene nombre y cardinalidad en ambos extremos?', '¿Algún atributo está repetido en dos entidades?', '¿Los atributos de relación están sobre el rombo?', '¿Responde «¿qué alumnos tiene el taller de Robótica y quién lo dicta?»?']),
       pasos=['Respondé cada pregunta con Sí o No.', 'Corregí lo que tenga No y volvé a controlar.', 'Leé cada relación en los dos sentidos ante un compañero.'],
       control='Las cinco preguntas tienen Sí y tu compañero no encontró ninguna lectura falsa.'),
 ],
 desafio='La coordinación quiere registrar la asistencia de cada alumno a cada encuentro del taller (fecha y presente/ausente). Agregalo al DER y justificá si es entidad o relación.',
 sol=dict(resultado='Act. 1: ALUMNO(cod_alumno, nombre, curso) —(se inscribe, N:M, atributo fecha_inscripción)— TALLER(cod_taller, nombre, día); DOCENTE(cod_docente, nombre, teléfono) —(dicta, 1:N)— TALLER; AULA(cod_aula, capacidad) —(usa, 1:1)— TALLER. Act. 2: las cinco preguntas respondidas con Sí; la pregunta se responde recorriendo ALUMNO–se inscribe–TALLER–dicta–DOCENTE. Desafío: ASISTENCIA como entidad (o relación ternaria ALUMNO–TALLER–ENCUENTRO) con fecha y estado; se justifica porque se consulta por sí misma y tiene datos propios.',
          errores='Poner fecha_inscripción en ALUMNO; dibujar «dicta» como N:M; olvidar la 1:1 del aula; rombos sin nombre.'))

PR[15] = dict(
 titulo='Del DER de los talleres a las tablas', entorno=PAPEL,
 competencia='Aplicar las reglas de transformación a un DER nuevo: entidades, 1:N, N:M con tabla puente y 1:1 con clave foránea única.',
 saber=['Entidad → tabla. 1:N → la clave del «uno» viaja como FK al «muchos». N:M → tabla puente con las dos FK y los atributos del rombo. 1:1 → FK sin duplicados en el lado obligatorio, o fusión.'],
 antes='Usá el DER validado de la Práctica 14.',
 acts=[
  dict(titulo='El esquema de tablas', objetivo='Traducir el DER a tablas con sus claves.',
       modelo=('Formato de cada tabla', ['NombreTabla(campo PK, campo, campo FK → Tabla, …)']),
       pasos=['Escribí una tabla por entidad.', 'Resolvé «dicta» (1:N) con una FK.', 'Resolvé «se inscribe» (N:M) con una tabla puente; indicá su clave.', 'Resolvé «usa» (1:1) e indicá la propiedad que la mantiene 1:1.'],
       control='La cantidad de tablas es igual a la cantidad de entidades más la de relaciones N:M.'),
  dict(titulo='Cargar la tabla puente', objetivo='Escribir las filas de la tabla puente para tres inscripciones.',
       modelo=('Inscripciones', ['Lucía Ortiz (A01) en Robótica (T1), el 02/03/2026', 'Lucía Ortiz (A01) en Teatro (T2), el 03/03/2026', 'Marcos Rojas (A02) en Robótica (T1), el 02/03/2026']),
       pasos=['Escribí una fila por inscripción, con códigos y fecha.', 'Verificá que la clave compuesta no se repita.', 'Intentá cargar de nuevo a Lucía en Robótica y explicá qué pasa.'],
       control='Ninguna fila repite la pareja alumno + taller.'),
 ],
 desafio='Si un alumno puede volver a inscribirse en el mismo taller al año siguiente, ¿qué le pasa a la clave de la tabla puente? Proponé el cambio.',
 sol=dict(resultado='Act. 1: Alumnos(cod_alumno PK, nombre, curso); Docentes(cod_docente PK, nombre, teléfono); Aulas(cod_aula PK, capacidad); Talleres(cod_taller PK, nombre, día, cod_docente FK → Docentes, cod_aula FK → Aulas con índice sin duplicados); Inscripciones(cod_alumno FK, cod_taller FK, fecha_inscripción; PK compuesta cod_alumno + cod_taller). Total: 4 entidades + 1 N:M = 5 tablas. Act. 2: (A01, T1, 02/03/2026), (A01, T2, 03/03/2026), (A02, T1, 02/03/2026); la segunda carga de (A01, T1) se rechaza por clave duplicada. Desafío: agregar año a la clave: (cod_alumno, cod_taller, año).',
          errores='Poner cod_taller en Alumnos; olvidar fecha_inscripción en la puente; FK de aula sin restricción de unicidad; crear una tabla para «dicta».'))

PR[16] = dict(
 titulo='Anomalías y dependencias en la planilla de talleres', entorno=PAPEL,
 competencia='Detectar anomalías y escribir y clasificar dependencias funcionales en una tabla nueva, y medir su redundancia.',
 saber=['Dependencia completa: necesita toda la clave. Parcial: alcanza con una parte. Transitiva: pasa por un campo que no es clave. Una DF es una regla, no una coincidencia de los datos.'],
 antes='La coordinación guarda las inscripciones en una sola planilla. Su clave es (cod_alumno, cod_taller).',
 acts=[
  dict(titulo='Ensayar operaciones', objetivo='Encontrar una anomalía de cada tipo.',
       modelo=('Planilla de inscripciones', ['A01 · Lucía Ortiz · 3.º A · T1 · Robótica · Prof. Ruiz · 0981 222 333 · 02/03/2026', 'A01 · Lucía Ortiz · 3.º A · T2 · Teatro · Prof. Benítez · 0982 444 555 · 03/03/2026', 'A02 · Marcos Rojas · 2.º B · T1 · Robótica · Prof. Ruiz · 0981 222 333 · 02/03/2026', 'A03 · Ana Paula Vera · 1.º C · T3 · Ajedrez · Prof. Ruiz · 0981 222 333 · 04/03/2026', 'A02 · Marcos Rojas · 2.º B · T3 · Ajedrez · Prof. Ruiz · 0981 222 333 · 05/03/2026', 'A04 · Diego Acosta · 3.º A · T2 · Teatro · Prof. Benítez · 0982 444 555 · 05/03/2026', 'Columnas: cod_alumno · nombre_alumno · curso · cod_taller · nombre_taller · docente · tel_docente · fecha_insc']),
       pasos=['Ensayá: crear el taller T4 «Coro» sin inscriptos; cambiar el teléfono del Prof. Ruiz; dar de baja la única inscripción de Ana Paula Vera.', 'Para cada ensayo, escribí qué se rompe y qué anomalía es.'],
       control='Para cada anomalía señalaste en qué filas de la planilla ocurre.'),
  dict(titulo='El mapa de dependencias', objetivo='Escribir las dependencias funcionales, clasificarlas y medir la redundancia.',
       modelo=('Modelo de diagrama', ['Cajas con las ocho columnas en fila; flechas desde lo que determina hacia lo determinado, como en la figura de dependencias de la clase.']),
       pasos=['Escribí todas las DF que valen como regla del colegio.', 'Clasificá cada una como completa, parcial o transitiva.', 'Dibujá el diagrama con tres colores.', 'Contá, columna por columna, las celdas que repiten un dato ya escrito en otra fila.'],
       control='Toda DF que escribiste se cumple en las seis filas y tiene sentido como regla del colegio.'),
 ],
 desafio='¿Es «docente → cod_taller» una dependencia funcional? Justificá con los datos.',
 sol=dict(resultado='Act. 1: inserción: T4 Coro no puede entrar sin un alumno (la clave pide cod_alumno); actualización: el teléfono de Ruiz está en 4 filas (1, 3, 4 y 5); borrado: al dar de baja A03–T3 se pierde Ana Paula Vera (Ajedrez no se pierde porque Marcos sigue inscripto). Act. 2: cod_alumno → nombre_alumno, curso (parcial); cod_taller → nombre_taller, docente (parcial); docente → tel_docente (transitiva: cod_taller → docente → tel_docente); (cod_alumno, cod_taller) → fecha_insc (completa). Redundancia: nombre y curso 2 + 2 = 4; nombre del taller y docente 3 + 3 = 6; teléfono 6 − 2 = 4; total 14 celdas. Desafío: no, Ruiz dicta T1 y T3.',
          errores='Escribir «nombre_alumno → cod_alumno»; clasificar docente → teléfono como parcial; contar la primera aparición como redundante.'))

PR[17] = dict(
 titulo='Normalizar los pedidos de la librería Arasa\'i', entorno=PAPEL,
 competencia='Llevar una planilla nueva de 1FN a 3FN sin perder información, verificando la reconstrucción de los importes.',
 saber=['1FN: un valor por celda. 2FN: sin dependencias parciales. 3FN: sin dependencias transitivas. Normalizar bien no pierde ni inventa datos.'],
 antes='Precios de la librería: cuaderno (R1) G. 8.000 · lapicera (R2) G. 2.500 · mochila (R3) G. 95.000.',
 acts=[
  dict(titulo='Primera forma normal', objetivo='Separar la lista de productos de cada pedido.',
       modelo=('Planilla de pedidos', ['31 · 06/03/2026 · K01 · Ramona Giménez · 0984 111 222 · 2 cuadernos; 1 lapicera', '32 · 06/03/2026 · K02 · Julio Sanabria · 0991 333 444 · 1 mochila; 2 lapiceras', '33 · 07/03/2026 · K01 · Ramona Giménez · 0984 111 222 · 1 cuaderno; 1 mochila', 'Columnas: pedido · fecha · cod_cliente · cliente · teléfono · productos']),
       pasos=['Calculá primero el importe de cada pedido con la planilla original y anotalo.', 'Reescribí la planilla con una fila por producto de cada pedido (con cantidad y precio_unitario).', 'Indicá la clave de la tabla en 1FN.'],
       control='Ninguna celda tiene más de un producto y la clave identifica cada fila.'),
  dict(titulo='Segunda y tercera forma normal', objetivo='Eliminar dependencias parciales y transitivas.',
       modelo=('Preguntas guía', ['¿Qué datos dependen solo del pedido?', '¿Cuáles solo del producto?', '¿Hay algún dato que dependa del pedido a través de otro campo?']),
       pasos=['Aplicá la 2FN y escribí las tablas resultantes.', 'Aplicá la 3FN y escribí el esquema final con claves principales y foráneas.', 'Reconstruí desde tus tablas finales el importe de cada pedido.'],
       control='La suma de los importes reconstruidos desde tus tablas finales es igual a la suma de los importes que calculaste con la planilla original.'),
 ],
 desafio='La librería quiere hacer descuentos: a veces sobre un producto de un pedido, a veces sobre el pedido entero. ¿En qué tabla va cada descuento?',
 sol=dict(resultado='Importes originales: 31 = 16.000 + 2.500 = 18.500; 32 = 95.000 + 5.000 = 100.000; 33 = 8.000 + 95.000 = 103.000; suma G. 221.500. Act. 1 (1FN, clave pedido + producto): (31, R1, 2, 8.000), (31, R2, 1, 2.500), (32, R3, 1, 95.000), (32, R2, 2, 2.500), (33, R1, 1, 8.000), (33, R3, 1, 95.000), con fecha, cliente y teléfono repetidos. Act. 2: 2FN → Pedidos(pedido, fecha, cod_cliente, cliente, teléfono), Productos(cod, nombre, precio), DetallePedido(pedido, producto, cantidad, precio_unitario). 3FN → Clientes(cod_cliente, cliente, teléfono) y Pedidos(pedido, fecha, cod_cliente FK). Reconstrucción: 18.500 + 100.000 + 103.000 = G. 221.500. Desafío: descuento por producto en DetallePedido; descuento global en Pedidos.',
          errores='Dejar el teléfono en Pedidos (transitiva); sacar precio_unitario del detalle; clave de 1FN solo «pedido»; no verificar la reconstrucción.'))


def _tabla_prod2():
    return [[k, v[0], v[1], g(v[2])] for k, v in PROD2.items()]


def _tabla_cli2():
    return [[k, v, TEL2[k] or '(sin teléfono)'] for k, v in CLI2.items()]


def _tabla_ven2():
    return [[k, v[0], v[1]] for k, v in VEN2.items()]


def _tabla_det2():
    return [[v, p, str(q), g(pu)] for v, p, q, pu in DET2]


PR[18] = dict(
 titulo='La base de la segunda semana, creada en Access', entorno=ACCESS,
 competencia='Crear en Access una base relacional completa: tablas con tipos y propiedades, clave compuesta, relaciones con integridad referencial y carga de datos en el orden correcto.',
 saber=['Crear → Diseño de tabla. Clave compuesta: seleccionar las dos filas con Ctrl y pulsar Clave principal. Relaciones: Herramientas de base de datos → Relaciones → Exigir integridad referencial.',
        'El catálogo cambió: desde el 10/03/2026 la gaseosa cuesta G. 9.000. Las ventas guardan en precio_unitario lo que realmente se cobró.'],
 antes='Creá una base en blanco llamada Copetin_Semana2.accdb en tu carpeta de trabajo. Las tablas de datos están al final de esta práctica.',
 datos=[('Productos (catálogo actual)', ['código', 'nombre', 'categoría', 'precio'], _tabla_prod2()),
        ('Clientes', ['código', 'nombre', 'teléfono'], _tabla_cli2()),
        ('Ventas', ['código', 'fecha', 'cliente'], _tabla_ven2()),
        ('DetalleVenta', ['venta', 'producto', 'cantidad', 'precio_unitario'], _tabla_det2())],
 acts=[
  dict(titulo='Las cuatro tablas, con sus propiedades', objetivo='Crear Productos, Clientes, Ventas y DetalleVenta con tipos de datos y propiedades que protejan los datos.',
       modelo=('Diseño pedido', ['Productos: código (Texto corto, PK) · nombre (Texto corto, Requerido) · categoría (Texto corto, lista Panificados/Salados/Bebidas con Limitar a la lista = Sí) · precio (Moneda, regla >0)', 'Clientes: código (Texto corto, PK) · nombre (Texto corto, Requerido) · teléfono (Texto corto, no requerido)', 'Ventas: código (Texto corto, PK) · fecha (Fecha/Hora) · cliente (Texto corto)', 'DetalleVenta: venta + producto (PK compuesta) · cantidad (Número, regla >0) · precio_unitario (Moneda)']),
       pasos=['Creá cada tabla en la vista Diseño con sus campos y tipos.', 'Configurá las propiedades indicadas (Requerido, Regla de validación con su texto, lista de categorías).', 'En DetalleVenta, creá la clave compuesta seleccionando venta y producto con Ctrl.', 'Guardá cada tabla con su nombre exacto.'],
       control='Al abrir DetalleVenta en vista Diseño se ven dos iconos de clave; al escribir «Lácteos» en categoría, Access lo rechaza.'),
  dict(titulo='Las relaciones', objetivo='Definir las tres relaciones con integridad referencial.',
       modelo=('Relaciones', ['Clientes.código → Ventas.cliente', 'Ventas.código → DetalleVenta.venta', 'Productos.código → DetalleVenta.producto', 'En las tres: Exigir integridad referencial: Sí · Actualizar en cascada los campos relacionados: Sí · Eliminar en cascada los registros relacionados: No']),
       pasos=['Abrí Herramientas de base de datos → Relaciones y agregá las cuatro tablas.', 'Arrastrá cada clave principal sobre su clave foránea y configurá las casillas.', 'Guardá el diseño de relaciones.'],
       control='Las tres líneas muestran 1 y ∞ en sus extremos.'),
  dict(titulo='La carga de datos', objetivo='Cargar los datos de la semana en el orden que exige la integridad referencial.',
       modelo=('Orden', ['1.º Productos y Clientes → 2.º Ventas → 3.º DetalleVenta']),
       pasos=['Cargá Productos (8) y Clientes (6). Hugo Cáceres no dio teléfono: dejá el campo vacío.', 'Cargá Ventas (6).', 'Cargá DetalleVenta (13) con el precio_unitario de la tabla de datos, no el del catálogo.', 'Probá cargar un renglón con el producto P09 y cancelalo.'],
       control='El total de registros coincide con la suma de los registros indicados en las cuatro tablas de datos. Verificaste además que los valores históricos de DetalleVenta no fueron sustituidos automáticamente por los precios actuales del catálogo.'),
 ],
 desafio='Intentá cargar un renglón con cantidad 0 y otro con una venta inexistente (V20). Anotá el mensaje de cada rechazo y qué regla lo provocó.',
 sol=dict(resultado='Base con 4 tablas y 3 relaciones con integridad (1–∞). Registros: 8 + 6 + 6 + 13 = 33. DetalleVenta con PK compuesta (dos iconos de clave). V8: (V8, P06, 1, 8.000) y V11: (V11, P06, 2, 9.000). El renglón con P09 se rechaza por integridad referencial. Desafío: cantidad 0 → se rechaza por la regla de validación >0 (muestra el texto de validación); V20 → se rechaza por integridad referencial (no existe en Ventas).',
          errores='Cargar DetalleVenta antes que Ventas; poner el precio de catálogo en V8; clave principal solo en venta (impide dos productos por venta); tipo Número en los códigos (pierde formato).'))

PR[19] = dict(
 titulo='Filtros y consultas sobre la segunda semana', entorno=ACCESS,
 competencia='Aplicar filtros y diseñar consultas de selección con criterios de comparación, rango, texto, nulos y fechas, anticipando el resultado y verificándolo.',
 saber=['Números directos (> 6000), textos entre comillas ("Bebidas"), fechas entre numerales (#10/03/2026#, escrita en la cuadrícula de Diseño con configuración día/mes/año). Misma fila = Y; filas distintas = O. Es Nulo encuentra campos vacíos.'],
 antes='Abrí Copetin_Semana2.accdb (Práctica 18). Antes de ejecutar cada consulta, escribí en tu hoja qué esperás que devuelva.',
 acts=[
  dict(titulo='Filtrar sin consultar', objetivo='Usar el filtro por selección en la hoja de datos de Ventas.',
       modelo=('Pedido', ['Ver solo las ventas del 10/03/2026; luego quitar el filtro.']),
       pasos=['Abrí Ventas en vista Hoja de datos.', 'Hacé clic derecho sobre una fecha 10/03/2026 → «Es igual a 10/03/2026».', 'Anotá cuántas ventas se ven y quitá el filtro con Alternar filtro.'],
       control='El filtro muestra solamente las ventas de la fecha elegida y, al quitarlo, reaparece el conjunto completo sin que ningún registro haya sido modificado.'),
  dict(titulo='Cuatro consultas con criterio', objetivo='Diseñar, anticipar, ejecutar y guardar cuatro consultas.',
       modelo=('Consultas pedidas', ['ConsProductosCaros: nombre y precio de los productos de más de G. 6.000, del más caro al más barato.', 'ConsBebidasEconomicas: bebidas de menos de G. 8.000 (dos criterios en la misma fila).', 'ConsClientesSinTelefono: clientes con el teléfono vacío.', 'ConsVentas9y10: ventas entre el 09/03/2026 y el 10/03/2026, incluidos los bordes.']),
       pasos=['Crear → Diseño de consulta; agregá la tabla y bajá los campos.', 'Escribí el criterio de cada consulta y, si corresponde, el orden.', 'Ejecutá y compará con lo que anticipaste.', 'Guardá cada consulta con su nombre.'],
       control='Cada resultado coincide con lo anticipado. Los registros devueltos y los no devueltos, juntos y sin superposición, reconstruyen el conjunto completo de Ventas.'),
  dict(titulo='La fecha por dentro', objetivo='Comprobar en la vista SQL cómo guarda Access las fechas del criterio.',
       modelo=('Qué mirar', ['Inicio → Ver → Vista SQL de ConsVentas9y10']),
       pasos=['Abrí la vista SQL y copiá la línea WHERE.', 'Explicá por qué el 10/03 aparece escrito como 3/10.', 'Escribí qué fecha entendería Access si en la vista SQL alguien escribiera #10/03/2026#.'],
       control='Tu explicación menciona el orden mes/día/año de la vista SQL.'),
 ],
 desafio='Diseñá una consulta con los productos cuyo nombre contiene la letra «a» y cuestan menos de G. 6.000. Anticipá el resultado antes de ejecutarla.',
 sol=dict(resultado='Act. 1: 2 ventas (V8 y V9). Act. 2: ConsProductosCaros → Milanesa 15.000, Gaseosa 9.000, Jugo natural 7.000; ConsBebidasEconomicas (categoría "Bebidas" y precio < 8000) → Cocido 4.000 y Jugo natural 7.000; ConsClientesSinTelefono (Es Nulo) → Hugo Cáceres; ConsVentas9y10 (en la cuadrícula de Diseño con configuración d/m/a: Entre #09/03/2026# Y #10/03/2026#; en la vista SQL: Between #3/9/2026# And #3/10/2026#) → V6, V7, V8 y V9 (complemento: V10 y V11, del 11/03). Act. 3: WHERE fecha Between #3/9/2026# And #3/10/2026#; la vista SQL usa mes/día/año; #10/03/2026# escrito en SQL sería el 3 de octubre. Desafío: Como "*a*" y < 6000 → Chipa (3.000).',
          errores='Escribir las fechas como texto; poner los dos criterios de ConsBebidasEconomicas en filas distintas (devuelve de más); usar = "" en lugar de Es Nulo; olvidar el orden descendente.'))

PR[20] = dict(
 titulo='Consultas que preguntan, sobre la segunda semana', entorno=ACCESS,
 competencia='Crear consultas paramétricas simples, con comodines y multi-tabla, y probarlas con valores que dan resultados, ninguno o varios.',
 saber=['El parámetro va entre corchetes en la fila Criterios. Con Como y el asterisco se busca por parte del texto. Una consulta con varias tablas usa las relaciones ya definidas.'],
 antes='Abrí Copetin_Semana2.accdb. Probá cada consulta con todos los valores pedidos, incluso los que parecen no tener sentido.',
 acts=[
  dict(titulo='Las ventas de un cliente', objetivo='Crear ParVentasPorCliente y probarla con tres clientes.',
       modelo=('Diseño', ['Tabla Ventas · campos código, fecha y cliente · en cliente: [Ingresá el código de cliente]']),
       pasos=['Diseñá y guardá la consulta.', 'Ejecutala con C05, con C06 y con C04.', 'Anotá cuántas ventas devuelve cada prueba.'],
       control='La consulta produce una respuesta coherente tanto para clientes con ventas como para un cliente que no tenga registros coincidentes.'),
  dict(titulo='Renglones por categoría y un buscador', objetivo='Crear una consulta paramétrica multi-tabla y un buscador con comodines.',
       modelo=('Consultas', ['ParRenglonesPorCategoria: Ventas + DetalleVenta + Productos + Clientes; muestra venta, nombre del cliente, producto, cantidad y precio_unitario; parámetro en categoría.', 'ParBuscador: Productos; en nombre: Como "*" & [Buscar producto:] & "*".']),
       pasos=['Agregá las cuatro tablas y verificá que Access dibuje las relaciones.', 'Probá ParRenglonesPorCategoria con «Panificados» y con «Bebidas».', 'Probá ParBuscador con «jug» y con «pa».'],
       control='La cantidad de renglones de «Panificados» más los de «Bebidas» más los de «Salados» da la cantidad total de renglones de DetalleVenta.'),
 ],
 desafio='Creá ParVentasEntreFechas, que pida una fecha inicial y una final, y probala con 10/03/2026 y 11/03/2026.',
 sol=dict(resultado='Act. 1: C05 → V7 y V10; C06 → V9; C04 → ninguna (Miguel Ortiz no compró en esta semana: la hoja vacía es la respuesta correcta). Act. 2: Panificados → 4 renglones (chipas de V7, chipas de V8, sopa de V9, mbeju de V10); Bebidas → 6 renglones (jugo de V6, cocidos de V7, gaseosa de V8, jugo de V9, cocido de V10, gaseosas de V11); Salados → 3 (4 + 6 + 3 = 13). Buscador: «jug» → Jugo natural; «pa» → Chipa, Empanada y Sopa paraguaya. Desafío: Entre [Fecha inicial] Y [Fecha final] → V8, V9, V10 y V11.',
          errores='Escribir el parámetro sin corchetes; buscar con Como [Buscar] sin asteriscos; agregar tablas sin relación (producto cartesiano).'))

PR[21] = dict(
 titulo='Totales, cálculos y cruces de la segunda semana', entorno=ACCESS,
 competencia='Construir consultas de totales, campos calculados y referencias cruzadas con controles cruzados, y detectar el error de usar el precio de catálogo en lugar del precio cobrado.',
 saber=['Subtotal: [cantidad]*[precio_unitario]. La fila Total (botón Totales) agrupa y calcula. La referencia cruzada pone un campo en filas, otro en columnas y un valor en el cruce.',
        'Promedio por venta: primero se suma por venta (TotalPorVenta) y después se promedia.'],
 antes='Abrí Copetin_Semana2.accdb. En esta práctica vas a comprobar los mismos totales por varios caminos.',
 acts=[
  dict(titulo='El detalle calculado', objetivo='Crear ConsDetalle con el campo calculado Subtotal.',
       modelo=('Diseño', ['Tablas: Ventas, DetalleVenta, Productos, Clientes · campos: venta, fecha, cliente, nombre del cliente, categoría, producto, cantidad, precio_unitario · Subtotal: [cantidad]*[precio_unitario]']),
       pasos=['Diseñá la consulta con el campo calculado.', 'Ejecutala y revisá el subtotal de cada renglón de la venta V11.', 'Guardala: será la base de las demás.'],
       control='ConsDetalle contiene un renglón por cada registro de DetalleVenta y ningún Subtotal queda vacío.'),
  dict(titulo='Totales por cuatro caminos', objetivo='Crear consultas de totales y verificar que coincidan.',
       modelo=('Consultas sobre ConsDetalle', ['TotPorCliente · TotPorCategoria · TotPorProducto (con Suma de cantidad y de Subtotal) · TotalPorVenta y, sobre ella, PromedioVenta (Promedio, Máx y Mín de TotalVenta)']),
       pasos=['Creá cada consulta con el botón Totales: Agrupar por en el campo de grupo y Suma en Subtotal.', 'Anotá el total general de cada una.', 'Creá TotalPorVenta y luego PromedioVenta.'],
       control='Los totales generales por cliente, por categoría y por producto son iguales entre sí. Además, el promedio multiplicado por la cantidad de ventas da ese mismo total.'),
  dict(titulo='La cruzada y la trampa del precio', objetivo='Armar la referencia cruzada y comprobar qué pasa si se usa el precio de catálogo.',
       modelo=('Pasos', ['Referencia cruzada sobre ConsDetalle: nombre del cliente (fila) · categoría (columna) · Suma de Subtotal (valor).', 'Campo de prueba en una copia de ConsDetalle: SubtotalCatalogo: [cantidad]*[Productos].[precio]']),
       pasos=['Creá la cruzada con el asistente o desde la vista Diseño.', 'Verificá la suma de una fila y la de una columna.', 'Creá la copia con SubtotalCatalogo y sumalo.', 'Encontrá el renglón que explica la diferencia.'],
       control='La cruzada coincide con TotPorCliente y TotPorCategoria. Comparaste la suma con precio de catálogo con la suma real y, si difieren, señalaste el renglón o los renglones que explican la diferencia.'),
 ],
 desafio='Creá un informe basado en TotPorCategoria (Crear → Informe) y exportalo a PDF (Datos externos → PDF o XPS) con el nombre Recaudacion_Semana2.pdf.',
 sol=dict(resultado='Act. 1: 13 renglones; V11: empanadas 24.000 y gaseosas 18.000. Act. 2: por cliente Rosa 29.000, Luis 19.000, Ana 42.000, Teresa 26.000, Hugo 19.000 (Miguel no aparece: no compró); por categoría Panificados 32.000, Salados 51.000, Bebidas 52.000; por producto Empanada 36.000 (6 u.), Gaseosa 26.000 (3 u.), Chipa 15.000 (5 u.), Milanesa 15.000 (1 u.), Jugo natural 14.000 (2 u.), Cocido 12.000 (3 u.), Sopa paraguaya 12.000 (2 u.), Mbeju 5.000 (1 u.); total G. 135.000 en los tres caminos. TotalPorVenta: V6 19.000, V7 17.000, V8 29.000, V9 19.000, V10 9.000, V11 42.000; promedio G. 22.500; máx 42.000 (V11); mín 9.000 (V10). Act. 3: cruzada Rosa (Pan 6.000, Sal 15.000, Beb 8.000), Luis (Sal 12.000, Beb 7.000), Ana (Sal 24.000, Beb 18.000), Teresa (Pan 14.000, Beb 12.000), Hugo (Pan 12.000, Beb 7.000). Con precio de catálogo da G. 136.000: la diferencia de G. 1.000 está en V8, donde la gaseosa se cobró 8.000 y el catálogo hoy dice 9.000.',
          errores='Sumar Productos.precio; promediar los 13 renglones (≈ 10.385) en vez de las 6 ventas; olvidar Agrupar por; poner categoría en filas y cliente en columnas y no saber leerla (es válido, pero la lectura cambia).'))


# ------------------------------------------------------------------ v2 · Transferencia y revisión entre pares
# Solo en las continuaciones de papel cuyas Actividades 2 y 3 quedan cortas para 120 minutos (P5, P6, P8, P9, P10).
def _pares(tarea):
    return [tarea,
            'Intercambiá tu resolución con la de otro equipo.',
            'Revisá la resolución que recibiste y señalá por escrito al menos un error o una decisión sin justificar.',
            'Con la revisión que te devolvieron, corregí tu versión.',
            'Escribí en tres o cuatro renglones por qué tu versión final es correcta.']


CONTROL_PARES = 'Tu versión final incorpora la corrección que recibiste (o explica por escrito por qué no correspondía) y tu justificación usa los conceptos de la clase.'

PR[5]['transfer'] = dict(
 caso=('Libreta de fiados del almacén de la esquina', ['1) 10/03 – Doña Petrona Ayala lleva 2 kg de azúcar (G. 6.000 el kilo).', '2) 10/03 – Petrona Ayala lleva 1 paquete de yerba (G. 12.000).', '3) 11/03 – Don Ramón Sosa lleva 3 panificados (G. 2.000 c/u).', '4) 11/03 – Doña Petrona pagó G. 12.000.', '5) 12/03 – R. Sosa lleva 1 paquete de yerba (G. 12.000).']),
 pasos=_pares('Separá clientes, productos y fiados con códigos, como en la Actividad 1, y anotá los problemas de calidad de la libreta con su dimensión.'),
 control=CONTROL_PARES,
 sol='Clientes K1 Petrona Ayala y K2 Ramón Sosa; productos azúcar (G. 6.000/kg), yerba (G. 12.000) y panificado (G. 2.000); fiados (K1, azúcar, 2, 10/03), (K1, yerba, 1, 10/03), (K2, panificado, 3, 11/03), (K2, yerba, 1, 12/03). El renglón 4 no es un fiado sino un pago: va en una estructura aparte (cliente, fecha, monto). Problemas: «Doña Petrona Ayala / Petrona Ayala / Doña Petrona» y «Don Ramón Sosa / R. Sosa» (consistencia); el precio de la yerba repetido en cada renglón (redundancia). Saldos: Petrona 12.000 + 12.000 − 12.000 = G. 12.000; Ramón 6.000 + 12.000 = G. 18.000. Error que suelen detectar los pares: registrar el pago como un fiado negativo.')

PR[6]['transfer'] = dict(
 caso=('Inventario del laboratorio de informática', ['PC-01 · computadora · Lenovo · 2019 · 8 GB de memoria · sala 1', 'PC-02 · computadora · HP · 2021 · 8 GB de memoria · sala 1', 'PC-03 · computadora · Lenovo · 2019 · 4 GB de memoria · sala 2', 'IMP-01 · impresora · Epson · 2020 · (sin memoria informada) · sala 2', 'Escenarios: (a) solo la encargada del laboratorio usa el inventario, en su computadora; (b) los colegios del distrito comparten un único inventario.']),
 pasos=_pares('Armá la tabla Equipos con un campo por dato, elegí la clave principal y decidí base local o en servidor para los escenarios (a) y (b).'),
 control=CONTROL_PARES,
 sol='Equipos(código PK, tipo, marca, año, memoria_GB, sala) con cuatro filas; la impresora deja memoria_GB vacío (no se inventa un 0). Clave: código (marca, año y sala se repiten). (a) base local: una sola persona y un solo equipo; (b) base en servidor: varios usuarios simultáneos en red. Error que suelen detectar los pares: escribir «8 GB» como texto en vez de un número en un campo de memoria.')

PR[8]['transfer'] = dict(
 caso=('Taller mecánico del barrio', ['Clientes(cédula, nombre, teléfono)', 'Vehículos(nro_chasis, chapa, marca, cédula_dueño)', 'Reparaciones(nro_orden, nro_chasis, fecha, monto)', 'Dato del taller: la chapa de un vehículo puede cambiar si se lo vuelve a empadronar; el número de chasis no cambia.']),
 pasos=_pares('Marcá en cada tabla la clave principal, las claves alternativas y las claves foráneas, y dibujá las flechas FK → PK.'),
 control=CONTROL_PARES,
 sol='Clientes: PK cédula (o un código propio si no se quiere pedir la cédula). Vehículos: PK nro_chasis; chapa es candidata pero no estable, así que no conviene como clave; FK cédula_dueño → Clientes. Reparaciones: PK nro_orden; FK nro_chasis → Vehículos. Error que suelen detectar los pares: elegir la chapa como clave principal.')

PR[9]['transfer'] = dict(
 caso=('Docentes y materias del colegio', ['Docentes: D1 Benítez · D2 Ruiz', 'Materias: M1 Algorítmica (docente D1) · M2 Matemática (docente D2) · M3 Inglés (docente D1)', 'Operaciones: (a) borrar a D2, con la relación configurada para restringir; (b) cambiar el código D1 por D10, con «Actualizar en cascada» activado; (c) agregar la materia M4 con el docente D7; (d) borrar a D1, con «Eliminar en cascada» activado.']),
 pasos=_pares('Para cada operación, decidí si el SGBD la acepta o la rechaza y qué registros quedan afectados.'),
 control=CONTROL_PARES,
 sol='(a) rechaza: M2 apunta a D2; (b) acepta: M1 y M3 pasan a D10; (c) rechaza: D7 no existe en Docentes; (d) acepta y borra también M1 y M3; queda solo M2 (con D2). Error que suelen detectar los pares: creer que en (b) hay que corregir M1 y M3 a mano.')

PR[10]['transfer'] = dict(
 caso=('La base de la cantina del colegio', ['(a) Agregar el campo stock_mínimo a la tabla Productos.', '(b) Registrar que llegaron 20 jugos.', '(c) Crear para la cajera una vista que muestre solo producto y precio.', '(d) La dueña consulta las ventas del día desde un formulario.', '(e) Mudar el archivo de la base a un disco nuevo.']),
 pasos=_pares('Clasificá cada tarea como DDL o DML, indicá el nivel de abstracción que afecta y el tipo de usuario de la cajera y de la dueña.'),
 control=CONTROL_PARES,
 sol='(a) DDL, nivel lógico; (b) DML; (c) definición de una vista: DDL, nivel de vistas; (d) DML, usuario normal que accede por formulario; (e) nivel físico, sin cambios para los usuarios. La cajera y la dueña son usuarias normales. Error que suelen detectar los pares: clasificar (c) como DML porque «muestra datos».')


def cantidad_acts(n):
    return len(PR[n]['acts'])


if __name__ == '__main__':
    assert len(PR) == 21
    for n, p in PR.items():
        print(n, p['entorno'], len(p['acts']), p['titulo'])

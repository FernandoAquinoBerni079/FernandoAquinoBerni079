# -*- coding: utf-8 -*-
"""Actividades de aplicación de las 21 clases, cada ítem con su respuesta (fuente única libro ↔ solucionario).
Familias: Ejercitá · Resolvé (caso Copetín Karumbé) · Pensá y decidí · Desafío.
Marcador N = ítem nuevo o modificado en la Edición Esencial (para las notas del piloto)."""
E, R, PD, D = 'Ejercitá', 'Resolvé (caso Copetín Karumbé)', 'Pensá y decidí (justificá tu respuesta)', 'Desafío'
N = True

A = {}
A[1] = [
 (E, [('Escribí con tus palabras qué es un lenguaje de programación.', 'Conjunto de reglas y símbolos para escribir instrucciones precisas que la computadora puede transformar en acciones.'),
      ('Indicá dos diferencias entre el lenguaje natural y un lenguaje de programación.', 'El natural es flexible y tolera la ambigüedad; el de programación es formal, con sintaxis y semántica definidas y una única interpretación por instrucción.'),
      ('Nombrá tres campos de aplicación del software y un ejemplo de cada uno.', 'Gestión (sistema de ventas), web (tienda en línea), móvil (app de delivery), datos (reportes). Se aceptan otros ejemplos válidos.'),
      ('Clasificá estas tareas según su campo: (a) app de pedidos, (b) sistema de ventas de un local, (c) página web del colegio.', '(a) móvil; (b) gestión/escritorio; (c) web.')]),
 (R, [('El Copetín Karumbé quiere un sistema que registre sus ventas. Indicá a qué campo de aplicación pertenece y proponé un lenguaje razonable.', 'Gestión/escritorio. Lenguaje razonable: Java, C# o Python (se acepta otro con justificación).'),
      ('Escribí, como órdenes precisas y numeradas, los pasos para cobrar 1 milanesa (G. 15.000) y 2 cocidos (G. 4.000 c/u). Verificá el total con una cuenta a mano.', '1) subtotal1 ← 1 × 15.000 = 15.000; 2) subtotal2 ← 2 × 4.000 = 8.000; 3) total ← subtotal1 + subtotal2 = 23.000; 4) Escribir total. Verificación: 15.000 + 8.000 = G. 23.000.', N),
      ('El programa de cobro muestra G. 19.000 para la venta de 1 milanesa y 2 cocidos. ¿Qué tipo de error es y cuál pudo ser la causa?', 'Error de lógica: el programa corre sin avisar, pero calcula mal. 15.000 + 4.000 = 19.000: tomó un solo cocido (no multiplicó por la cantidad 2). Se detecta comparando con el total calculado a mano (23.000).', N)]),
 (PD, [('«Cualquier lenguaje sirve igual para cualquier problema.»', 'Falso: cada lenguaje se adapta mejor a ciertos problemas y contextos.'),
       ('«Si un programa no muestra ningún mensaje de error, calcula bien.»', 'Falso: el error de lógica no se anuncia; solo se descubre comparando el resultado con uno calculado de antemano.', N)]),
 (D, [('Elegí una tarea de tu vida diaria (preparar un tereré, por ejemplo) y escribila como una secuencia de instrucciones precisas, numeradas, que otra persona pueda seguir sin preguntarte nada.', 'Respuesta abierta: secuencia numerada, completa y sin ambigüedades, que un tercero pueda ejecutar.')]),
]
A[2] = [
 (E, [('Ordená de más cercano a la máquina a más cercano a la persona: alto nivel, máquina, ensamblador.', 'Máquina → ensamblador → alto nivel.'),
      ('Explicá en una oración qué hace un traductor.', 'Convierte o procesa el código escrito por la persona hasta instrucciones que la máquina puede ejecutar.'),
      ('Indicá una diferencia entre compilador e intérprete.', 'Modelo introductorio: el compilador traduce antes de ejecutar y puede generar un ejecutable; el intérprete procesa el programa durante la ejecución. Se aceptan menciones a sistemas híbridos.'),
      ('Asociá el modelo más típico: (a) realiza una traducción previa y puede generar un ejecutable; (b) ejecuta mediante un intérprete o runtime sin requerir necesariamente un ejecutable nativo independiente. Opciones: compilación previa / interpretación-runtime.', '(a) compilación previa; (b) interpretación/runtime.'),
      ('Mencioná una ventaja posible de la compilación previa y una de trabajar con un entorno interpretado o interactivo.', 'Compilación: posible mejor rendimiento y distribución como binario. Interpretado/interactivo: respuesta inmediata para probar. Son tendencias que dependen de la implementación.')]),
 (R, [('El programador del Copetín escribió «subtotal = 3 * 6000» en alto nivel. Explicá por qué la CPU no puede ejecutar esa línea tal cual y qué hace falta.', 'Está en alto nivel; la CPU solo ejecuta código máquina. Hace falta una implementación que la traduzca o procese (compilador, intérprete/runtime o combinación).', N),
      ('Si el sistema del Copetín se va a usar todos los días y el rendimiento es un criterio importante, ¿qué estrategia de ejecución o implementación priorizarías? Fundamentá sin asumir que el nombre del lenguaje determina por sí solo el recorrido.', 'Se acepta priorizar compilación previa u optimización si se justifica por rendimiento, aclarando que depende de la implementación y que conviene medir el caso real.')]),
 (PD, [('«El lenguaje de máquina necesita un traductor para ejecutarse.»', 'Falso: el lenguaje de máquina se ejecuta directamente; el ensamblador y el alto nivel requieren herramientas de traducción o ejecución.'),
       ('«Un intérprete traduce todo el programa antes de correrlo.»', 'Falso: eso describe el modelo de compilación previa; la interpretación ocurre durante la ejecución.')]),
 (D, [('Buscá dos lenguajes reales (por ejemplo C y Python) y averiguá cómo se ejecuta una implementación habitual de cada uno: compilación nativa, bytecode/VM, intérprete/runtime o una combinación. Anotá tu fuente.', 'Ej.: C suele compilarse a código nativo; CPython compila a bytecode y lo ejecuta en su máquina virtual. Se valora citar la fuente y reconocer que el lenguaje no fija un único mecanismo.')]),
]
A[3] = [
 (E, [('Definí «paradigma de programación» en una oración.', 'Forma o estilo de pensar y organizar la solución de un problema.'),
      ('Escribí la idea central de cada uno de los cuatro paradigmas.', 'Imperativo: ordenar paso a paso. Funcional: combinar funciones sin cambiar datos. Lógico: declarar hechos y reglas para deducir. Orientado a objetos: objetos que reúnen datos y acciones.'),
      ('Asociá cada lenguaje a su paradigma típico: Prolog, Java, C, Haskell.', 'Prolog → lógico; Java → orientado a objetos; C → imperativo; Haskell → funcional.'),
      ('Indicá qué paradigma describe la solución «paso a paso».', 'El imperativo (y su forma estructurada).')]),
 (R, [('El sistema del Copetín tendrá objetos como Producto, Venta y Cliente, cada uno con sus datos y sus acciones. ¿A qué paradigma corresponde ese diseño?', 'Orientado a objetos.'),
      ('Reescribí en estilo imperativo, con un acumulador, el cálculo del total de un pedido de 2 empanadas (G. 6.000 c/u) y 3 cocidos (G. 4.000 c/u).', 'total ← 0; total ← total + 2 × 6.000 (total = 12.000); total ← total + 3 × 4.000 (total = 24.000); Escribir total → G. 24.000.', N),
      ('Indicá el paradigma de cada situación: (a) «al pulsar el botón Imprimir ticket, se imprime el comprobante»; (b) «si un producto se vendió más de cinco veces en la semana, entonces es producto estrella»; (c) «la suma de los importes de las ventas del día», pedida a la base de datos.', '(a) dirigido por eventos; (b) lógico (regla); (c) declarativo (se pide el qué, no el cómo).', N)]),
 (PD, [('«Un lenguaje solo puede pertenecer a un paradigma.»', 'Falso: muchos lenguajes son multiparadigma (por ejemplo, Python).'),
       ('«El paradigma orientado a objetos organiza el programa en objetos que reúnen datos y acciones.»', 'Verdadero.')]),
 (D, [('Elegí un paradigma distinto del imperativo y explicá con tus palabras en qué tipo de problema conviene usarlo.', 'Respuesta abierta coherente: lógico para deducción y sistemas expertos; funcional para procesar grandes volúmenes con previsibilidad; eventos para interfaces.')]),
]
A[4] = [
 (E, [('Enumerá tres criterios para elegir un lenguaje de programación.', 'Tres entre: tipo de aplicación, rendimiento, facilidad de aprendizaje, comunidad y soporte, conocimiento del equipo, costo y ecosistema.'),
      ('Explicá por qué no existe un lenguaje «mejor» para todo.', 'Porque cada lenguaje se adapta mejor a ciertos problemas, equipos y contextos; la elección depende del caso.'),
      ('Completá: «Elijo un lenguaje según el ______, el ______ y el ______».', '…según el problema (tipo de aplicación), el equipo y el mantenimiento (se aceptan otros criterios vistos).'),
      ('Dado un juego para celular, ¿qué criterio pesa más: tipo de aplicación o color del logo? Justificá.', 'Tipo de aplicación: define si el lenguaje sirve para móvil; el color del logo es irrelevante.')]),
 (R, [('Una ferretería de barrio quiere una tienda en línea donde sus clientes vean el stock desde el celular. Elegí un tipo de lenguaje razonable y justificá con dos criterios.', 'Tecnologías web: JavaScript en el navegador más un lenguaje de servidor (PHP, Python, Java u otro). Criterios: tipo de aplicación (web accesible desde el celular) y comunidad o disponibilidad de programadores.', N),
      ('Un cliente quiere una app móvil. Indicá qué criterio descarta usar un lenguaje pensado solo para escritorio.', 'El tipo de aplicación.'),
      ('Recalculá la matriz de decisión del Copetín si el dueño cambia los pesos a facilidad 0,2; disponibilidad de programadores 0,3 y velocidad 0,5, con los mismos puntajes. ¿Cambia el ganador?', 'A: 9×0,2 + 9×0,3 + 6×0,5 = 1,8 + 2,7 + 3,0 = 7,5. B: 7×0,2 + 8×0,3 + 5×0,5 = 1,4 + 2,4 + 2,5 = 6,3. C: 5×0,2 + 6×0,3 + 7,5×0,5 = 1,0 + 1,8 + 3,75 = 6,55. Gana A igual; C supera a B.', N)]),
 (PD, [('«Siempre conviene el lenguaje más nuevo o de moda.»', 'Falso: conviene el más adecuado al problema, al equipo y al mantenimiento.'),
       ('«El conocimiento del equipo es un criterio válido para elegir el lenguaje.»', 'Verdadero.')]),
 (D, [('Elegí una app que uses seguido y proponé, con argumentos, qué criterios habrán pesado al elegir su lenguaje de desarrollo.', 'Respuesta abierta argumentada.')]),
]
A[5] = [
 (E, [('Definí «base de datos» con tus palabras.', 'Colección de datos organizados y relacionados, guardados para consultarlos y actualizarlos con facilidad y sin repetición innecesaria.'),
      ('Escribí tres características de una base de datos organizada.', 'Tres entre: organización, relación, no redundancia, coherencia, accesibilidad.'),
      ('Indicá un problema de anotar las ventas repitiendo el precio en cada renglón.', 'Se multiplican los errores: un precio mal copiado deja dos precios para el mismo producto.'),
      ('Dado un conjunto de fichas sueltas sin ninguna relación, decidí si es o no una base de datos y justificá.', 'No: faltan organización y relación entre los datos.')]),
 (R, [('El cuaderno del Copetín repite «Gaseosa G. 8.000» en cada venta. Explicá qué característica de una base de datos evita ese problema.', 'La no redundancia: el precio se guarda una sola vez, en la tabla de productos.'),
      ('Proponé qué datos del Copetín conviene guardar una sola vez (no en cada venta).', 'Nombre, categoría y precio de cada producto; nombre y datos del cliente.'),
      ('Clasificá como dato, información o conocimiento: (a) «17000»; (b) «la venta V4 totalizó G. 17.000»; (c) «los martes se venden más chipas que cualquier otro día».', '(a) dato; (b) información; (c) conocimiento.', N),
      ('En el cuaderno, la venta V2 aparece anotada dos veces y en otro renglón falta el producto. ¿Qué dimensiones de la calidad de los datos fallan?', 'Unicidad (venta duplicada) y completitud (renglón sin producto).', N)]),
 (PD, [('«Una base de datos es simplemente un montón de datos guardados juntos.»', 'Falso: además deben estar organizados y relacionados.'),
       ('«La no redundancia significa guardar cada dato una sola vez.»', 'Verdadero.')]),
 (D, [('Mirá el cuaderno de notas de una materia y proponé cómo lo organizarías como base de datos: qué datos guardarías una sola vez y cuáles se repetirían.', 'Respuesta abierta coherente: alumnos y materias una vez; las notas se registran por alumno, materia y fecha.')]),
]
A[6] = [
 (E, [('Indicá qué organiza el modelo relacional.', 'La información en tablas relacionadas entre sí.'),
      ('Nombrá dos gestores de bases de datos relacionales.', 'Dos entre Microsoft Access, MySQL y PostgreSQL.'),
      ('En una tabla, ¿qué es una fila y qué es una columna?', 'Fila = registro (un caso concreto); columna = campo (un dato).'),
      ('Asociá: (a) sistema de un banco; (b) red social. ¿Usan base de datos? Justificá.', 'Sí, ambos: guardan y relacionan cuentas y movimientos, usuarios y publicaciones.')]),
 (R, [('Una cooperativa abre una sucursal y necesita que sus tres cajas consulten los mismos socios a la vez. ¿Base local o en servidor? Justificá con dos aspectos de la tabla de la clase.', 'En servidor: varios usuarios simultáneos y acceso por red a datos compartidos.', N),
      ('Indicá qué otras dos tablas necesitará el Copetín además de Productos y por qué.', 'Clientes (a quién se vendió) y Ventas con su detalle (cada operación y qué productos llevó).'),
      ('Indicá qué modelo conviene en cada caso: (a) el organigrama fijo de una empresa; (b) millones de mensajes de una app, con formatos muy variados; (c) ventas, clientes y productos de un comercio.', '(a) jerárquico; (b) no relacional (NoSQL); (c) relacional.', N)]),
 (PD, [('«En el modelo relacional cada columna es un registro.»', 'Falso: la fila es el registro; la columna es el campo.'),
       ('«Las tablas de una base de datos relacional pueden relacionarse entre sí.»', 'Verdadero.')]),
 (D, [('Elegí un sistema que uses (una app, el sistema del colegio) y proponé dos tablas que podría tener y qué columnas guardaría cada una.', 'Respuesta abierta coherente.')]),
]
A[7] = [
 (E, [('Explicá la diferencia entre base de datos y SGBD.', 'La base de datos son los datos; el SGBD es el software que los crea, guarda, protege y consulta.'),
      ('Nombrá tres problemas que evita un SGBD.', 'Tres entre: redundancia, inconsistencia, dificultad de acceso, problemas de integridad, concurrencia y seguridad.'),
      ('Definí redundancia y definí inconsistencia.', 'Redundancia: el mismo dato repetido. Inconsistencia: copias del mismo dato que no coinciden.'),
      ('Asociá el problema con su solución: (a) mismo dato repetido; (b) varios editan a la vez. Soluciones: control de concurrencia / no redundancia.', '(a) no redundancia; (b) control de concurrencia.')]),
 (R, [('La cantina del colegio anota los precios en una planilla para la caja y en otra para el depósito. El jugo figura a G. 5.000 en una y a G. 5.500 en la otra. Nombrá los dos problemas y explicá cómo los evita un SGBD.', 'Redundancia (el precio está en dos lugares) e inconsistencia (las copias no coinciden). El SGBD guarda el precio una sola vez y todas las aplicaciones lo consultan desde ahí.', N),
      ('Solo el dueño debería cambiar precios; los empleados solo registran ventas. ¿Qué problema resuelve esto y con qué herramienta del SGBD?', 'Seguridad: permisos por usuario (perfiles o roles).'),
      ('Al registrar la venta V2 (1 milanesa y 1 cocido) se corta la luz justo después de guardar el renglón de la milanesa. Según la atomicidad, ¿qué queda guardado al volver la energía?', 'Nada de esa venta: la transacción no se confirmó, así que el SGBD deshace lo hecho (venta y renglón). La venta se registra de nuevo, completa.', N)]),
 (PD, [('«La base de datos y el SGBD son lo mismo.»', 'Falso: la base son los datos; el SGBD es el programa.'),
       ('«La inconsistencia aparece cuando copias del mismo dato no coinciden.»', 'Verdadero.')]),
 (D, [('Pensá una situación de tu colegio donde el mismo dato esté repetido en varios lugares y explicá qué problema podría causar.', 'Respuesta abierta coherente (por ejemplo, el teléfono de un padre anotado en tres planillas distintas).')]),
]
A[8] = [
 (E, [('Definí campo y registro.', 'Campo = columna (un dato); registro = fila (un caso concreto).'),
      ('¿Qué dos condiciones cumple una clave principal?', 'Es única (no se repite) y nunca queda vacía.'),
      ('Indicá cuál es la clave principal de la tabla Productos.', 'El código (P01, P02…).'),
      ('Explicá con tus palabras qué hace una clave foránea.', 'Apunta a la clave principal de otra tabla y así las relaciona.'),
      ('En la tabla Ventas, ¿qué campo es la clave foránea y a qué tabla apunta?', 'El campo cliente; apunta a Clientes.')]),
 (R, [('Seguí la clave foránea de la venta V4 y decí a quién pertenece. Luego indicá cuántas ventas tiene esa persona en la tabla Ventas.', 'V4 → C03 = Ana Gómez. Tiene una sola venta (V4).', N),
      ('Proponé una clave principal para la tabla Clientes y justificá por qué sirve.', 'Un código propio (C01…): único, estable y nunca vacío. La cédula serviría solo si se valida que todos la tienen y no se repite.'),
      ('Asigná el tipo de dato (Texto, Número, Moneda, Fecha/Hora o Sí/No) a: teléfono del cliente, cantidad vendida, precio_unitario, fecha de la venta y «¿pagó con tarjeta?».', 'Texto; Número; Moneda; Fecha/Hora; Sí/No.', N)]),
 (PD, [('«La clave principal puede repetirse entre registros.»', 'Falso: es única.'),
       ('«La clave foránea relaciona una tabla con otra.»', 'Verdadero.')]),
 (D, [('Diseñá una tabla Empleados para el Copetín: proponé tres campos e indicá cuál sería la clave principal.', 'Ej.: Empleados(código, nombre, cargo); clave principal = código.')]),
]
A[9] = [
 (E, [('Definí integridad referencial.', 'Regla que garantiza que toda clave foránea apunte a un registro que existe.'),
      ('Escribí las dos reglas básicas que impone.', 'No registrar una venta con un cliente inexistente; no borrar un cliente que todavía tiene ventas.'),
      ('Indicá si el SGBD permite registrar una venta con un cliente que no existe.', 'No: violaría la integridad referencial.'),
      ('Explicá qué es una venta «huérfana».', 'Una venta cuya clave foránea apunta a un cliente que ya no existe.')]),
 (R, [('Se intenta registrar una venta del cliente C07, que no está en la tabla Clientes. ¿Qué hace el SGBD configurado para restringir y por qué?', 'La rechaza: C07 no existe en Clientes y la clave foránea apuntaría a la nada.', N),
      ('El dueño quiere borrar a Ana Gómez (C03), que tiene la venta V4 (G. 17.000). Indicá qué pasaría con cada configuración: (a) restringir; (b) eliminar en cascada.', '(a) Se rechaza el borrado mientras exista V4. (b) Se borran Ana, la venta V4 y sus dos renglones de detalle: se pierden G. 17.000 de historia comercial.', N),
      ('Clasificá cada violación como de entidad, de dominio o referencial: (a) dos clientes con el código C02; (b) una cantidad de −2; (c) un renglón de detalle con el producto P09, que no existe.', '(a) entidad; (b) dominio; (c) referencial.', N)]),
 (PD, [('«La integridad referencial permite claves foráneas que apuntan a registros inexistentes.»', 'Falso: justamente lo impide.'),
       ('«No se puede borrar un cliente que aún tiene ventas registradas.»', 'Verdadero (con la configuración de restringir, la predeterminada).')]),
 (D, [('Proponé una tercera situación (además de las dos reglas vistas) donde la integridad referencial proteja los datos del Copetín.', 'Ej.: impedir un renglón de DetalleVenta con un producto que no existe, o borrar un producto que figura en ventas.')]),
]
A[10] = [
 (E, [('Nombrá los tres niveles de abstracción de datos.', 'Físico, lógico (conceptual) y de vistas (externo).'),
      ('Indicá qué describe el nivel lógico.', 'Qué tablas y relaciones hay: los datos y sus vínculos.'),
      ('Diferenciá un usuario normal de un programador de aplicaciones.', 'El usuario normal usa el sistema sin ver la base; el programador desarrolla las aplicaciones y las conecta a la base.'),
      ('Asociá: (a) crear una tabla; (b) consultar registros. Lenguajes: DDL / DML.', '(a) DDL; (b) DML.')]),
 (R, [('El empleado de la caja del Copetín solo necesita ver productos y precios. ¿Qué nivel de abstracción describe eso y qué tipo de usuario es?', 'Nivel de vistas; usuario normal (final).'),
      ('Clasificá como DDL o DML: (a) borrar la tabla Proveedores; (b) corregir el precio de la empanada; (c) crear el campo barrio en Clientes; (d) eliminar la venta V2.', '(a) DDL; (b) DML; (c) DDL; (d) DML.', N),
      ('Para acelerar las búsquedas se indexa el campo cliente de Ventas. ¿Qué nivel cambia y qué tipo de independencia permite que la vista del cajero siga funcionando sin tocarla?', 'Cambia el nivel físico; la independencia física permite que tablas y vistas sigan iguales.', N)]),
 (PD, [('«El nivel de vistas muestra toda la base de datos a todos los usuarios.»', 'Falso: cada vista muestra solo la porción que cada usuario necesita.'),
       ('«El DDL define la estructura y el DML manipula los datos.»', 'Verdadero.')]),
 (D, [('Proponé dos vistas distintas de la base del Copetín: una para el empleado y otra para el dueño, e indicá qué datos vería cada uno.', 'Empleado: productos y precios (y quizás las ventas del día). Dueño: además ventas, clientes y recaudación por categoría.')]),
]
A[11] = [
 (E, [('Definí «modelo de datos».', 'Representación de la información y sus relaciones, previa e independiente del programa que la implemente.'),
      ('Nombrá dos modelos de datos.', 'Dos entre: entidad-relación, orientado a objetos, lógico basado en registros, lógico basado en objetos.'),
      ('Explicá por qué conviene diseñar antes de crear las tablas.', 'Porque corregir el diseño en papel es barato; corregirlo con datos cargados es caro y riesgoso.'),
      ('Compará: ¿qué es al plano de una casa lo que el modelo de datos es a la base?', 'El modelo de datos es a la base lo que el plano es a la casa: la guía previa de la construcción.')]),
 (R, [('Escribí, en una frase, qué información guardará el Copetín y cómo se relaciona (productos, clientes, ventas).', 'Guarda productos, clientes y ventas; cada venta es de un cliente y contiene varios productos.'),
      ('Indicá qué modelo de datos usaremos para diseñar y por qué es el adecuado para empezar.', 'Entidad-relación: describe la realidad con entidades y relaciones, sin depender de ningún programa.'),
      ('El dueño pide: «quiero saber cuántas chipas me quedan en el horno». ¿Entra en el mini-mundo del sistema de ventas tal como fue delimitado? ¿Qué habría que agregar?', 'No: el mini-mundo registra ventas, no producción ni existencias. Habría que ampliarlo con el stock o la producción (por ejemplo, existencias por producto) y documentar la decisión.', N)]),
 (PD, [('«El modelo de datos depende del programa que se use para crear la base.»', 'Falso: es previo e independiente del programa.'),
       ('«Diseñar antes de crear las tablas ayuda a evitar errores costosos.»', 'Verdadero.')]),
 (D, [('Elegí algo que conozcas (una biblioteca, un club) y escribí en una frase qué entidades y relaciones tendría su modelo de datos.', 'Respuesta abierta coherente (biblioteca: socios y libros relacionados por préstamos).')]),
]
A[12] = [
 (E, [('Definí entidad y definí atributo.', 'Entidad: cosa de la realidad sobre la que se guardan datos. Atributo: cada dato de esa entidad.'),
      ('Clasificá: precio (simple o compuesto); teléfonos de un cliente (univalorado o multivalorado).', 'Precio: simple. Teléfonos: multivalorado.'),
      ('Indicá un atributo derivado y de qué otro se calcula.', 'Ej.: edad, derivada de la fecha de nacimiento; subtotal, de cantidad × precio_unitario.'),
      ('Listá los atributos de la entidad Producto del Copetín.', 'Código, nombre, categoría y precio.')]),
 (R, [('En el sistema de un colegio, clasificá los atributos de ALUMNO: cédula, nombre completo, fecha de nacimiento, edad y teléfonos de los padres.', 'Cédula: simple y univalorado (candidato a identificador). Nombre completo: compuesto. Fecha de nacimiento: simple. Edad: derivado. Teléfonos de los padres: multivalorado.', N),
      ('En la entidad Cliente, indicá qué atributo puede ser la clave y por qué.', 'El código de cliente: único, estable y nunca vacío.'),
      ('Definí el dominio de: cantidad vendida, categoría y código de cliente.', 'Cantidad: entero de 1 en adelante. Categoría: Panificados, Salados o Bebidas. Código de cliente: «C» seguida de dos dígitos.', N)]),
 (PD, [('«Un atributo multivalorado guarda un solo valor por registro.»', 'Falso: admite varios valores para el mismo registro.'),
       ('«Cada entidad se convierte luego en una tabla.»', 'Verdadero.')]),
 (D, [('Diseñá la entidad Empleado del Copetín con cuatro atributos e indicá el tipo de cada uno (simple, compuesto, derivado…).', 'Ej.: código (simple, identificador), nombre completo (compuesto), fecha de ingreso (simple), antigüedad (derivado).')]),
]
A[13] = [
 (E, [('Definí «relación» y «cardinalidad».', 'Relación: vínculo entre entidades. Cardinalidad: cuántos registros de una entidad se vinculan con cuántos de la otra.'),
      ('Indicá la cardinalidad: un cliente y sus ventas.', '1:N.'),
      ('Indicá la cardinalidad: ventas y productos.', 'N:M.'),
      ('Dado «cada país tiene una capital y cada capital pertenece a un país», indicá la cardinalidad.', '1:1.')]),
 (R, [('En el Copetín, determiná la cardinalidad entre Cliente y Venta, y entre Venta y Producto.', 'Cliente–Venta: 1:N. Venta–Producto: N:M.'),
      ('Justificá con los datos que Venta–Producto es N:M usando la chipa y la venta V2.', 'La venta V2 contiene dos productos (milanesa y cocido) y la chipa aparece en dos ventas (V1 y V4): muchos con muchos.', N),
      ('Indicá el grado de cada relación: (a) un socio de la biblioteca recomienda a otro socio; (b) un cliente realiza ventas; (c) un docente dicta una materia en un curso.', '(a) unaria; (b) binaria; (c) ternaria.', N),
      ('Escribí el par (mín, máx) de cada extremo de «CURSO tiene ALUMNO», sabiendo que todo alumno está inscripto en exactamente un curso y que puede haber cursos recién abiertos sin alumnos.', 'CURSO: (0, N). ALUMNO: (1, 1).', N)]),
 (PD, [('«Una relación de muchos a muchos se guarda directamente en dos tablas.»', 'Falso: necesita una tabla intermedia.'),
       ('«Un cliente puede realizar muchas ventas: la relación Cliente-Venta es 1:N.»', 'Verdadero.')]),
 (D, [('Proponé una relación 1:1 y una 1:N en un sistema escolar, e indicá las entidades de cada una.', 'Ej.: 1:1 alumno–legajo; 1:N curso–alumnos.')]),
]
A[14] = [
 (E, [('Indicá con qué símbolo se representa una entidad y con cuál una relación.', 'Entidad: rectángulo. Relación: rombo.'),
      ('Nombrá las tres entidades del DER del Copetín.', 'Cliente, Venta y Producto.'),
      ('Indicá qué atributos lleva la relación «contiene».', 'Cantidad y precio_unitario.', N),
      ('Escribí en palabras qué dice el DER del Copetín.', 'Un cliente realiza muchas ventas; una venta contiene muchos productos y un producto aparece en muchas ventas, con su cantidad y su precio unitario.')]),
 (R, [('Leé el DER del Copetín en castellano llano, en los dos sentidos de cada relación (cuatro oraciones).', 'Un cliente puede realizar muchas ventas; cada venta la realiza un solo cliente; una venta contiene uno o más productos; un producto puede estar en muchas ventas (o en ninguna todavía).', N),
      ('Agregá al DER una entidad Empleado relacionada con Venta (1:N) e indicá cómo quedaría el vínculo.', 'EMPLEADO —(atiende, 1:N)— VENTA: un empleado atiende muchas ventas; cada venta la atiende un empleado.'),
      ('¿Entidad, atributo o relación? (a) la categoría del producto, si solo se usa su nombre; (b) la categoría, si además se guardan su descripción y el porcentaje de descuento de cada categoría; (c) «qué alumnos se inscribieron en qué taller».', '(a) atributo de PRODUCTO; (b) entidad CATEGORÍA (tiene datos propios), con relación 1:N hacia PRODUCTO; (c) relación N:M entre ALUMNO y TALLER.', N)]),
 (PD, [('«En un DER, las entidades se representan con rombos.»', 'Falso: las entidades son rectángulos; los rombos, relaciones.'),
       ('«La relación entre Venta y Producto lleva los atributos cantidad y precio_unitario.»', 'Verdadero: pertenecen al par venta-producto.', N)]),
 (D, [('Dibujá el DER de una biblioteca con Socio, Libro y Préstamo, indicando la cardinalidad de cada relación.', 'SOCIO —(1:N)— PRÉSTAMO —(N:1)— LIBRO: cada préstamo es de un socio y de un libro (o de un ejemplar); un socio y un libro pueden tener muchos préstamos. Préstamo es entidad porque tiene número y vida propia.')]),
]
A[15] = [
 (E, [('Indicá en qué se convierte cada entidad al pasar a tablas.', 'En una tabla: atributos → campos; identificador → clave principal.'),
      ('Explicá cómo se resuelve una relación 1:N.', 'La clave principal del lado «uno» se copia como clave foránea en el lado «muchos».'),
      ('Explicá cómo se resuelve una relación N:M.', 'Con una tabla intermedia (puente) que lleva las claves foráneas de ambas entidades y los atributos de la relación.'),
      ('Nombrá las cuatro tablas del esquema final del Copetín.', 'Productos, Clientes, Ventas y DetalleVenta.')]),
 (R, [('Traducí la relación «Cliente realiza Venta» (1:N) indicando qué clave foránea aparece y en qué tabla.', 'El código de cliente aparece como clave foránea (campo cliente) en Ventas.'),
      ('Una venta nueva, que el sistema numerará V12, lleva 3 empanadas y 1 cocido a los precios del catálogo. Escribí sus filas de DetalleVenta (venta, producto, cantidad, precio_unitario) y calculá el total.', '(V12, P03, 3, 6.000) y (V12, P05, 1, 4.000). Total: 18.000 + 4.000 = G. 22.000.', N),
      ('Cada caja registradora del Copetín la usa un solo cajero y cada cajero usa una sola caja. Traducí esa 1:1 indicando dónde va la clave foránea y qué propiedad evita que se convierta en 1:N.', 'La FK va en una de las dos tablas (por ejemplo, caja en Cajeros) con índice sin duplicados: en Access, Indexado = «Sí (Sin duplicados)».', N)]),
 (PD, [('«Una relación N:M se puede guardar sin tabla intermedia.»', 'Falso: necesita una tabla intermedia.'),
       ('«En una relación 1:N, la clave del lado ‘uno’ va como foránea en el lado ‘muchos’.»', 'Verdadero.')]),
 (D, [('Traducí a tablas el DER de la biblioteca (Socio, Libro, Préstamo) que dibujaste, indicando claves principales y foráneas.', 'Socios(cod_socio PK, …), Libros(cod_libro PK, …), Préstamos(nro_préstamo PK, cod_socio FK → Socios, cod_libro FK → Libros, fecha_préstamo, fecha_devolución).')]),
]
A[16] = [
 (E, [('Nombrá las tres anomalías y explicá una.', 'Inserción, actualización y borrado. Ej.: actualización = cambiar un precio obliga a corregir muchos renglones.'),
      ('Definí dependencia funcional.', 'A → B: a cada valor de A le corresponde siempre un único valor de B.'),
      ('Escribí la dependencia funcional entre código de producto y su precio de catálogo.', 'código de producto → precio.'),
      ('Indicá qué problema evita separar los productos en su propia tabla.', 'La anomalía de actualización (y la redundancia): el precio se cambia en un solo lugar.')]),
 (R, [('En la tabla única, Luis Benítez tiene una sola venta (V2). Indicá qué anomalía aparece si se anula V2 y qué dato se pierde.', 'Anomalía de borrado: desaparece el cliente Luis Benítez (sus datos solo estaban en esos renglones). La milanesa y el cocido no se pierden porque figuran también en V5.', N),
      ('Escribí dos dependencias funcionales que existan en los datos del Copetín.', 'Ej.: producto → nombre, categoría, precio; venta → fecha, cliente; cliente → nombre.'),
      ('¿Es una dependencia funcional «categoría → precio»? Justificá con los datos de Productos.', 'No: Panificados tiene la chipa (3.000) y el mbeju (5.000). Un mismo valor de categoría corresponde a dos precios.', N),
      ('Clasificá como completa, parcial o transitiva, en la tabla única: (a) venta + producto → cantidad; (b) producto → categoría; (c) venta → nombre del cliente.', '(a) completa; (b) parcial; (c) transitiva (venta → cliente → nombre).', N)]),
 (PD, [('«Normalizar busca aumentar la redundancia de los datos.»', 'Falso: busca reducirla.'),
       ('«El código de producto determina su precio de catálogo: es una dependencia funcional.»', 'Verdadero.')]),
 (D, [('Inventá una tabla mal diseñada de tu colegio (que junte todo) y señalá una anomalía de inserción, una de actualización y una de borrado.', 'Respuesta abierta coherente.')]),
]
A[17] = [
 (E, [('Enunciá la regla de la 1FN.', 'Cada campo con un solo valor (atómico) y sin grupos repetidos.'),
      ('Enunciá la regla de la 2FN.', 'Estando en 1FN, ningún campo no clave depende solo de una parte de una clave compuesta.'),
      ('Enunciá la regla de la 3FN.', 'Estando en 2FN, ningún campo no clave depende de otro campo no clave (sin dependencias transitivas).'),
      ('Indicá qué se movió a la tabla Productos y qué a la tabla Clientes al normalizar.', 'A Productos: nombre, categoría y precio de catálogo. A Clientes: nombre (y teléfono).')]),
 (R, [('La librería Arasa\'i anota «3 cuadernos, 1 regla» en un solo campo del pedido N.º 12. Llevá ese renglón a 1FN.', 'Una fila por producto: (12, cuaderno, 3) y (12, regla, 1).', N),
      ('Explicá por qué el precio de catálogo violaría la 2FN si se guardara en DetalleVenta, y por qué precio_unitario sí puede quedarse ahí.', 'El precio de catálogo depende solo del producto (una parte de la clave venta + producto): dependencia parcial, va a Productos. precio_unitario es lo cobrado en esa venta: depende de la clave completa y se queda en DetalleVenta.', N),
      ('Una tabla Clientes(código, nombre, barrio, ciudad_del_barrio) tiene clave simple. ¿Está en 2FN? ¿Y en 3FN? Justificá.', 'Está en 2FN (con clave simple no puede haber dependencias parciales). No está en 3FN: código → barrio → ciudad es transitiva. Se separa Barrios(barrio, ciudad) y Clientes conserva barrio como FK.', N)]),
 (PD, [('«La 3FN se puede aplicar sin haber pasado por la 1FN y la 2FN.»', 'Falso: cada forma normal se apoya en la anterior.'),
       ('«Al normalizar el Copetín se llega a las cuatro tablas del esquema final.»', 'Verdadero: Productos, Clientes, Ventas y DetalleVenta.')]),
 (D, [('Tomá la tabla mal diseñada que inventaste en la clase anterior y llevala hasta la 3FN, mostrando las tablas resultantes.', 'Respuesta abierta coherente hasta 3FN, con claves y sin pérdida de información.')]),
]
A[18] = [
 (E, [('Escribí los pasos para crear la tabla Productos con su clave principal en Access.', 'Crear → Diseño de tabla; escribir campos y tipos; seleccionar código y pulsar Clave principal; guardar como Productos.'),
      ('Indicá en qué pestaña de Access se definen las relaciones.', 'Herramientas de base de datos → Relaciones.'),
      ('Explicá qué hace la opción «Exigir integridad referencial».', 'Impide claves foráneas que apunten a registros inexistentes y borrados que dejen huérfanos.'),
      ('Indicá la clave principal y la clave foránea de la tabla Ventas.', 'Clave principal: código. Clave foránea: cliente (→ Clientes).')]),
 (R, [('Diseñá la tabla Clientes del Copetín (campos, tipos y clave principal) tal como la crearías en Access.', 'Clientes(código Texto corto [clave principal], nombre Texto corto, teléfono Texto corto).'),
      ('Describí cómo crear la relación entre DetalleVenta y Productos activando la integridad referencial.', 'En Relaciones, arrastrar código de Productos sobre producto de DetalleVenta y marcar Exigir integridad referencial.'),
      ('Indicá cómo configurarías las tres casillas de la relación Clientes–Ventas (exigir integridad, actualizar en cascada, eliminar en cascada) y por qué.', 'Exigir integridad: sí. Actualizar en cascada: sí (corrige referencias si cambia un código). Eliminar en cascada: no (borraría la historia de ventas).', N),
      ('Proponé una regla de validación y su texto de validación para el campo cantidad de DetalleVenta.', 'Regla: >0. Texto: «La cantidad debe ser mayor que cero.»', N)]),
 (PD, [('«En Access, la integridad referencial se activa al crear la relación.»', 'Verdadero.'),
       ('«Crear tablas y claves es trabajo DML.»', 'Falso: es DDL (definición de la estructura).')]),
 (D, [('Escribí el plan completo para armar en Access las cuatro tablas del Copetín y sus relaciones, en el orden correcto.', 'Crear Productos y Clientes; luego Ventas (FK a Clientes) y DetalleVenta (PK compuesta, FK a Ventas y Productos); definir las tres relaciones con integridad; cargar en el orden Productos/Clientes → Ventas → DetalleVenta.')]),
]
A[19] = [
 (E, [('Explicá la diferencia entre un filtro y una consulta.', 'El filtro es temporal y actúa sobre una tabla; la consulta se guarda, se reutiliza y puede combinar tablas.'),
      ('Indicá dónde se escribe el criterio en una consulta.', 'En la fila Criterios de la cuadrícula de diseño.'),
      ('Escribí el criterio para mostrar los productos cuyo precio esté entre G. 4.000 y G. 6.000, incluidos los bordes, e indicá cuáles aparecen.', 'Entre 4000 Y 6000 en precio → Mbeju (5.000), Empanada (6.000) y Cocido (4.000).', N),
      ('Interpretá: ¿qué devuelve una consulta de Ventas con criterio fecha >= #04/03/2026#?', 'V3, V4 y V5.', N)]),
 (R, [('Diseñá (en papel) una consulta sobre Productos que muestre nombre y precio de los productos que NO son Bebidas, ordenados del más caro al más barato. Indicá el resultado.', 'Criterio <> "Bebidas" en categoría (Mostrar desactivado); orden descendente en precio. Resultado: Milanesa 15.000, Empanada 6.000, Mbeju 5.000, Chipa 3.000.', N),
      ('Escribí los criterios para listar las ventas del cliente C01 realizadas después del 03/03/2026 e indicá el resultado.', 'cliente = "C01" y fecha > #03/03/2026# en la misma fila (Y) → V3.', N),
      ('Una compañera escribió "04/03/2026" (entre comillas) como criterio de fecha y no obtuvo resultados. Explicá el error y corregilo.', 'Entre comillas es texto, no fecha. Las fechas van entre numerales: #04/03/2026#.', N)]),
 (PD, [('«Un filtro modifica los datos de la tabla.»', 'Falso: solo muestra un subconjunto.'),
       ('«Una consulta de selección se guarda y se puede reutilizar.»', 'Verdadero.')]),
 (D, [('Diseñá una consulta que detecte los productos sin categoría cargada y explicá por qué el criterio = "" no sirve.', 'Criterio Es Nulo en categoría. Un campo nulo no es una cadena vacía: = "" no encuentra los nulos.', N)]),
]
A[20] = [
 (E, [('Definí consulta paramétrica.', 'Consulta cuyo criterio se pide al usuario cada vez que se ejecuta.'),
      ('Escribí cómo se anota un parámetro en el criterio.', 'Entre corchetes en la fila Criterios, por ejemplo [Ingresá el código de cliente].'),
      ('Indicá una ventaja de una consulta paramétrica frente a una fija.', 'Una sola consulta sirve para cualquier valor: menos objetos y menos mantenimiento.'),
      ('Interpretá: si en el parámetro de cliente se ingresa C02, ¿qué muestra?', 'La venta V2 (03/03/2026).', N)]),
 (R, [('Escribí un criterio paramétrico que pida una fecha inicial y una final, e indicá el resultado si se ingresan 04/03/2026 y 05/03/2026.', 'Entre [Fecha inicial] Y [Fecha final] en fecha → V3, V4 y V5.', N),
      ('Con el buscador Como "*" & [Buscar producto:] & "*", indicá qué devuelve si se tipea «e».', 'Mbeju, Empanada, Milanesa y Gaseosa (Access no distingue mayúsculas en Como).', N),
      ('Escribí cómo pedirías las ventas del cliente que ingrese el usuario y del 04/03/2026 a la vez, e indicá el resultado para C03.', 'En la misma fila: [Ingresá el código de cliente] en cliente y #04/03/2026# en fecha (Y). Con C03 → V4.', N)]),
 (PD, [('«Una consulta paramétrica tiene el criterio fijo.»', 'Falso: el criterio se pide al usuario.'),
       ('«El parámetro se escribe entre corchetes en la fila Criterios.»', 'Verdadero.')]),
 (D, [('Diseñá una consulta paramétrica que pida una fecha y muestre las ventas de ese día; indicá el resultado si se ingresa 05/03/2026.', '[Ingresá la fecha] en el campo fecha; con 05/03/2026 → V5.', N)]),
]
A[21] = [
 (E, [('Nombrá tres operaciones de una consulta de totales.', 'Tres entre Suma, Promedio, Cuenta, Máx y Mín.'),
      ('Escribí la fórmula del subtotal como campo calculado.', 'Subtotal: [cantidad]*[precio_unitario].'),
      ('Explicá qué muestra una consulta de referencias cruzadas.', 'Una tabla de doble entrada: un campo en filas, otro en columnas y un valor agregado en cada cruce.'),
      ('Usá Cuenta: ¿cuántos renglones de detalle tiene cada categoría?', 'Panificados 3; Salados 3; Bebidas 5 (total 11).', N)]),
 (R, [('Agrupando por producto, calculá cuántas unidades se vendieron de cada uno. ¿Coincide el producto más vendido en unidades con el que más ingresó?', 'Chipa 6, Gaseosa 5, Empanada 3, Milanesa 3, Cocido 2, Mbeju 1. Más unidades: chipa. Más ingresos: milanesa (G. 45.000). No coinciden.', N),
      ('Agrupando por fecha, calculá la recaudación de cada día y verificá que sumen la recaudación total.', '03/03: 33.000; 04/03: 51.000; 05/03: 50.000. Suma: G. 134.000.', N),
      ('Explicá por qué aplicar Promedio al Subtotal de los 11 renglones no da la venta promedio.', 'Daría el promedio por renglón (134.000 / 11 ≈ G. 12.182), no por venta. Primero hay que sumar por venta (TotalPorVenta) y después promediar: 134.000 / 5 = G. 26.800.', N)]),
 (PD, [('«Un campo calculado se guarda como dato en la tabla.»', 'Falso: se calcula al mostrarlo.'),
       ('«La suma por cliente, por producto y por categoría debe dar la misma recaudación total.»', 'Verdadero: son tres particiones de los mismos renglones.')]),
 (D, [('Siguiendo el protocolo de la clase, describí una consulta de actualización que cambie a G. 8.500 el precio de catálogo de la gaseosa, y explicá por qué las ventas pasadas no cambian.', 'Respaldar; ensayar como selección (código = "P06" → 1 registro); convertir en actualización de Productos.precio a 8500; verificar 1 registro afectado. Las ventas no cambian porque sus importes se calculan con DetalleVenta.precio_unitario, que no se toca.', N)]),
]


def items(n):
    """Lista plana [(familia, numero, enunciado, respuesta, nuevo)]."""
    out = []; k = 0
    for fam, lst in A[n]:
        for it in lst:
            k += 1
            out.append((fam, k, it[0], it[1], len(it) > 2))
    return out


if __name__ == '__main__':
    for n in A:
        it = items(n)
        assert len(it) >= 8, n
        print(n, len(it), 'nuevos', sum(1 for x in it if x[4]))

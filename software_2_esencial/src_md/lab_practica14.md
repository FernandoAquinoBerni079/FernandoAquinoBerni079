@@H1 Práctica 14 — Topologías de red
Nombre y Apellido: _______________________________  Curso: ______  Fecha: ____ / ____ / ____
Competencia de la práctica: Dibujar en PowerPoint la topología en estrella de una red real con las herramientas de formas y señalar su punto único de falla.
Para esta práctica, tené a mano las Figuras 14.1 y 14.2 de la Clase 14.
## Lo que necesitás saber
• PowerPoint dibuja diagramas con Insertar → Formas; los conectores se enganchan a las formas y las siguen al moverlas.
• Un buen diagrama de red rotula cada elemento y marca el punto único de falla.
• Caso de esta práctica: Panambi también atiende a la Farmacia Tajy, que tiene 6 computadoras (4 cajas, 1 en el depósito y 1 en administración), 1 impresora de red, 1 access point y el router del proveedor.
## Actividades
Actividad 1 — Objetivo: Dibujar la estrella de la Farmacia Tajy con el switch en el centro.
[[CAJA Ejemplo — Modelo a reproducir]]
Diagrama: un rectángulo central «Switch»; alrededor, «Caja-1» a «Caja-4», «Depósito», «Administración», «Impresora» y «Access point»; arriba, «Router». Todos se unen al switch con Conector recto, anclado a los puntos de conexión de las formas.
[[/CAJA]]
   1. Abrí PowerPoint, creá una presentación en blanco y eliminá los cuadros de texto de la diapositiva.
   2. Insertá el rectángulo central: Insertar → Formas → Rectángulo; dibujalo y escribí Switch.
   3. Insertá un rectángulo «Caja-1», copialo con Ctrl + C / Ctrl + V tres veces y renombralos hasta Caja-4.
   4. Agregá los rectángulos «Depósito», «Administración», «Impresora» y «Access point» y distribuí todo alrededor del switch.
   5. Uní cada forma al switch con Insertar → Formas → Líneas → Conector recto, arrastrando desde un punto de conexión de la forma hasta un punto de conexión del switch.
   6. Agregá el rectángulo «Router» arriba y unilo al switch también con un Conector recto.
   7. Guardá como Topologia_farmacia_[apellido].pptx.
Punto de control: Todas las formas quedan unidas al switch y, al mover una forma, su conector la sigue anclado.
Actividad 2 — Objetivo: Señalar el punto único de falla y titular el plano.
[[CAJA Ejemplo — Modelo a reproducir]]
Título «Red de la Farmacia Tajy — topología en estrella» y una llamada (flecha con texto) apuntando al elemento cuya caída deja sin red a todos los puestos.
[[/CAJA]]
   1. Insertá un cuadro de texto arriba con el título del modelo (Insertar → Cuadro de texto).
   2. Decidí qué elemento es el punto único de falla e insertá la llamada: Insertar → Formas → Llamadas.
   3. Pintá ese elemento de un color distinto con Formato de forma → Relleno.
   4. Revisá que ningún rótulo quede tapado y guardá los cambios.
Punto de control: El plano tiene título, un único elemento resaltado y la llamada explica en una línea por qué su caída afecta a toda la red.
[[CAJA Desafío final (si terminás antes)]]
Duplicá la diapositiva y convertí el diagrama en árbol: agregá un segundo switch en el depósito, al que pasen a conectarse el puesto del depósito y una segunda impresora.
[[/CAJA]]

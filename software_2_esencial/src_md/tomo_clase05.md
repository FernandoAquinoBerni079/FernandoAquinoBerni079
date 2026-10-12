@@H2 Clase 5 — Puertos de conexión
[[FICHA]]
Capacidad: Identifica los diferentes puertos de conexión que existen en una computadora.
Tema: Puertos de conexión: concepto, tipos, características y conexión.
- Reconoce los puertos externos de una computadora actual y su uso.
- Distingue las versiones de USB por su velocidad y su conector.
- Selecciona el puerto de video adecuado para un monitor dado.
[[/FICHA]]
[[IMG T_image9.png|11.1]]
Figura 5.1 — Identificación de puertos en el panel trasero de una computadora.
## Concepto
Los puertos son los conectores externos por los que la computadora se comunica con los periféricos y con la red. Se concentran en el panel trasero de la placa madre y en el frente del gabinete. Conocerlos permite conectar cualquier dispositivo sin adivinar y detectar de un vistazo qué puede y qué no puede hacer un equipo.
[[CAJA Concepto clave — Puerto]]
Conector físico normalizado por el que la computadora intercambia datos, video, audio o energía con otros dispositivos. Cada puerto responde a un estándar que define su forma, sus señales y su velocidad.
[[/CAJA]]
## La familia USB
USB (Universal Serial Bus) es la familia de conexión de propósito general para teclados, mouse, impresoras, pendrives, celulares y muchos otros dispositivos. Conviene separar dos ideas: el estándar de datos y el conector físico. USB 2.0 alcanza 480 Mb/s; USB 3.2 contempla 5, 10 y 20 Gb/s; USB4 puede ofrecer enlaces de mayor rendimiento, incluso hasta 80 Gb/s en implementaciones compatibles. USB-A y USB-C describen la forma del conector: que un puerto sea USB-C no permite deducir por sí solo su velocidad, capacidad de video o potencia de carga; deben verificarse las especificaciones del equipo y del cable.
[[CAJA Ejemplo — El proyector del aula]]
El Instituto Ko'ẽju conserva un proyector con entrada VGA. Panambi lo prevé en el presupuesto: la mayoría de las placas nuevas ya no traen VGA, así que incluye un adaptador HDMI a VGA por equipo docente. Detectar el detalle antes de instalar evita el clásico 'no podemos proyectar' del primer día de clases.
[[/CAJA]]
## Puertos de video
HDMI es el puerto de video y audio más difundido en monitores, proyectores y televisores. DisplayPort es su alternativa habitual en monitores de computadora, con altas resoluciones y frecuencias. VGA es el conector analógico azul de 15 pines, heredado: todavía aparece en proyectores de aulas e instituciones.
[[TABLA]]
Puerto | Uso principal | Detalle para reconocerlo
USB-A 2.0 / 3.2 | Periféricos y almacenamiento | Rectangular; el azul suele indicar USB 5 Gb/s (USB 3.2 Gen 1)
USB-C | Datos, video y carga | Ovalado pequeño, reversible
HDMI | Video y audio digital | Trapezoidal, en monitores y TV
DisplayPort | Video de monitores de PC | Rectangular con una esquina recortada
VGA | Video analógico heredado | Azul, 15 pines, con tornillos
RJ-45 | Red cableada | Como ficha telefónica, más ancha
[[/TABLA]]
## Red, audio y otros
El puerto RJ-45 conecta el cable de red y es la vía más estable para internet. Los jacks de 3,5 mm (verde: salida; rosa: micrófono) manejan el audio analógico. Completan el panel el lector de tarjetas SD en muchos equipos y, en placas recientes, el botón o puerto para actualizar el firmware.
Identificá cada puerto del panel trasero por su forma y su color: la familia USB, los de video (HDMI, DisplayPort, VGA), el RJ-45 de red y los jacks de audio.
[[IMG T_image10.png|16.0]]
Figura 5.2 — Panel trasero de la placa con sus puertos rotulados.
[[CAJA En Paraguay — USB-C: un cargador para todo]]
Con la masificación de celulares con USB-C, en el país se volvió común cargar y transferir datos con un mismo cable. Para el técnico es una ventaja concreta: menos adaptadores en el taller y un solo tipo de repuesto para recomendar al cliente.
[[/CAJA]]
## Leer un puerto antes de prometer algo
El nombre comercial de un puerto puede confundir. Con USB conviven varios nombres para lo mismo: lo que hoy se rotula como «USB 5Gbps» es el viejo USB 3.0, también llamado USB 3.2 Gen 1; «USB 10Gbps» es USB 3.2 Gen 2, y «USB 20Gbps» es USB 3.2 Gen 2×2. Por eso el técnico no promete una velocidad mirando el color o la forma: busca el rótulo junto al puerto o la ficha del equipo.
Con USB-C pasa lo mismo, multiplicado. Un puerto USB-C puede servir solo para datos, para datos y carga o para datos, carga y video. El fabricante lo indica con símbolos junto al conector (por ejemplo, el de DisplayPort o el de carga) o en la ficha. El cable también cuenta: un cable de carga barato puede transferir datos solo a velocidad USB 2.0.
[[CAJA Ejemplo — Conectar la notebook de dirección al televisor]]
La directora del Instituto Ko'ẽju quiere conectar su notebook al televisor de la sala de reuniones. La notebook tiene un HDMI y dos USB-C; el televisor solo tiene entradas HDMI.
Paso 1. Se revisa el HDMI de la notebook: es la conexión directa. Basta un cable HDMI del largo necesario.
Paso 2. Si el HDMI estuviera ocupado, se consulta la ficha: uno de los USB-C indica «DisplayPort Alt Mode», así que admite un adaptador USB-C a HDMI; el otro solo transfiere datos.
Paso 3. Se prueba antes de la reunión con el cable y el adaptador definitivos.
Paso 4. Se anota en la ficha del equipo cuál de los USB-C saca video.
[[/CAJA]]
Para un aula o una oficina, el inventario de puertos se hace antes de comprar: cuántos periféricos van a estar conectados siempre (teclado, mouse, impresora, lector), qué monitores o proyectores se usan y si hace falta red cableada. Si los puertos no alcanzan, se suma un hub USB alimentado, que tiene su propia fuente y no depende de la energía del puerto.
[[CAJA Errores frecuentes — Con los puertos]]
• Prometer video por cualquier USB-C: solo algunos lo soportan.
• Confundir el conector (USB-A, USB-C) con la versión o la velocidad.
• Usar un cable de carga cualquiera para pasar archivos grandes y culpar al disco por la lentitud.
• Forzar un conector en la posición equivocada: los USB-A tienen una sola posición correcta.
[[/CAJA]]
## Actividades de aplicación
Marcá la opción correcta:
1. El puerto de propósito general para periféricos es:
    a) HDMI
    b) USB
    c) RJ-45
    d) VGA
2. Un conector USB de color azul indica normalmente:
    a) USB 1.1
    b) USB 2.0
    c) USB 3.x de 5 Gb/s
    d) Un puerto dañado
3. El puerto que conecta el cable de red es:
    a) RJ-45
    b) DisplayPort
    c) Jack de 3,5 mm
    d) USB-C
4. La ventaja característica del conector USB-C es que:
    a) Solo sirve para cargar
    b) Es reversible y multiuso
    c) Es analógico
    d) Solo existe en celulares
Completá los espacios:
5. El puerto de video analógico heredado, de 15 pines y color azul, es el ________.
6. La sigla USB significa ________ Serial Bus.
7. El jack de 3,5 mm de color verde corresponde a la ________ de audio.
Verdadero o falso (justificá las falsas):
8. (....) HDMI transmite video y también audio.
9. (....) USB 2.0 es más rápido que USB 3.2.
10. (....) El RJ-45 y la ficha telefónica son idénticos.
Respondé y fundamentá:
11. Un cliente compró un monitor nuevo que solo trae HDMI, pero su equipo viejo solo tiene VGA. ¿Qué opciones le presentarías?
12. ¿Por qué conviene conectar la impresora del taller por USB o red cableada antes que por Wi-Fi? Fundamentá.

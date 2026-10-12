## Medir la distancia en milisegundos
El alcance de una red se nota en la demora (latencia): el tiempo que tarda un paquete en ir y volver. El comando ping la informa en milisegundos (ms). Dentro de una LAN la respuesta suele llegar en 1 ms o menos; un servidor en la misma ciudad responde en pocos milisegundos; uno en otro continente puede tardar 150 ms o más, porque la señal recorre miles de kilómetros y atraviesa muchos routers. El comando tracert muestra esos saltos uno por uno.
La velocidad contratada (por ejemplo, 300 Mb/s) y la latencia son cosas distintas. La primera dice cuántos datos pasan por segundo; la segunda, cuánto tarda en llegar cada paquete. Una videollamada sufre más con mucha latencia que con poca velocidad; una descarga grande, al revés.
[[CAJA Ejemplo — Leer tres mediciones del aula]]
Desde una PC de la secretaría del Instituto Ko'ẽju se hacen tres pruebas con ping y se anota el promedio:
Prueba A, la impresora de la secretaría: 1 ms. Prueba B, el sitio de un diario de Asunción: 9 ms. Prueba C, un servidor de videos en Europa: 210 ms.
Paso 1. Prueba A: el destino está en la misma LAN; la demora es mínima.
Paso 2. Prueba B: el tráfico sale por la WAN del proveedor, pero no deja el país; la demora sigue siendo baja.
Paso 3. Prueba C: cruza enlaces internacionales; la demora es unas 200 veces mayor que en la LAN.
Paso 4. Conclusión para el informe: la LAN responde bien; las demoras grandes dependen de la distancia y de la WAN, no del cableado del aula.
[[/CAJA]]
Para el técnico, conocer el alcance de cada tramo sirve para diagnosticar. Si falla todo lo externo pero la impresora local responde, el problema está en la salida a internet (router, ONT o proveedor). Si falla incluso la impresora local, el problema está dentro de la LAN: cable, switch o configuración del equipo. Ese razonamiento por tramos ahorra horas de pruebas a ciegas.
[[CAJA Errores frecuentes — Al hablar de alcance]]
• Llamar «red WAN» a la red Wi-Fi de la casa: el alcance la define, no el medio.
• Confundir velocidad contratada con latencia.
• Culpar al cableado local por una página extranjera lenta sin medir antes con ping o tracert.
• Pensar que la MAN es siempre de una sola empresa: muchas se arman con enlaces alquilados.
[[/CAJA]]

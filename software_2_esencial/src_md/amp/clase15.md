## Cómo se dimensiona el switch y dónde va cada equipo
Para elegir el switch se cuentan las bocas que se van a ocupar (equipos cableados, impresoras, access points y el enlace al router) y se suma una reserva de al menos un 20 %. Después se elige el tamaño comercial inmediato superior: 8, 16, 24 o 48 puertos. También se mira si hace falta PoE (Power over Ethernet): con PoE, el mismo cable de red alimenta al access point o a una cámara, y no hace falta un tomacorriente junto al techo.
El router se ubica donde llega el servicio del proveedor; el switch, en el rack o en el centro del cableado, y el access point, en un lugar alto y despejado, lejos de paredes gruesas y de metal. Cada equipo se rotula con su función y su dirección IP.
[[CAJA Ejemplo — El switch para la sala de profesores]]
La sala de profesores del Instituto Ko'ẽju pasa a red cableada: 4 computadoras, 1 impresora de red, 1 access point en el techo y el enlace al router de la secretaría.
Paso 1. Bocas ocupadas: 4 + 1 + 1 + 1 = 7.
Paso 2. Reserva del 20 %: 7 × 1,2 = 8,4; se necesitan al menos 9 puertos.
Paso 3. Tamaño comercial: un switch de 8 puertos no alcanza; se elige uno de 16.
Paso 4. Alimentación: como el access point va en el techo, se elige un switch con al menos un puerto PoE, o se suma un inyector PoE.
[[/CAJA]]
En una institución conviene además que el switch sea Gigabit en todos sus puertos y, si el presupuesto lo permite, administrable: así se pueden separar redes (por ejemplo, la de estudiantes y la de administración) y ver qué puerto está teniendo errores. Para un aula chica, uno no administrable de buena calidad es suficiente.
[[CAJA Errores frecuentes — Con los equipos de red]]
• Contar solo las computadoras y olvidar la impresora, el access point y el enlace al router.
• Comprar un switch sin puertos libres de reserva.
• Poner el access point dentro de un mueble metálico o detrás del rack.
• Encadenar el «router del proveedor» con otro router sin revisar las direcciones: quedan dos redes separadas.
[[/CAJA]]

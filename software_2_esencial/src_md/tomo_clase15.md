@@H2 Clase 15 — Equipos de red
[[FICHA]]
Capacidad: Identifica equipos y materiales para una red
Tema: Equipos de red: concepto, características, tipos, aplicación y generalidades.
- Describe la función de switch, router, access point y módem/ONT.
- Diferencia el switch del router por el problema que resuelve cada uno.
- Selecciona los equipos necesarios para una red local dada.
[[/FICHA]]
[[IMG T_image29.jpg|12.8]]
Figura 15.1 — Reconocimiento de router, switch y punto de acceso.
## El switch
El switch es el corazón de la red local: recibe los datos por un puerto y los reenvía solo al puerto del destinatario, aprendiendo qué equipo vive detrás de cada boca. Se elige por cantidad de puertos (8, 16, 24, 48), velocidad (Fast Ethernet de 100 Mb/s o Gigabit de 1.000 Mb/s) y tipo: no administrable (enchufar y usar) o administrable (permite configurar y segmentar).
[[CAJA Concepto clave — Puerta de enlace]]
Dirección del router por la que la red local sale hacia otras redes. Todo paquete destinado fuera de la LAN se entrega primero a la puerta de enlace, que decide su camino.
[[/CAJA]]
## El router
El router conecta redes distintas y decide por dónde encaminar cada paquete. Cuando actúa como puerta de enlace de una red doméstica o escolar hacia internet, suele ofrecer además NAT/PAT para compartir una dirección pública, DHCP, firewall básico y, en equipos integrados, Wi-Fi. NAT es una función frecuente del gateway, pero no es sinónimo de enrutamiento: un router puede encaminar tráfico sin realizar traducción de direcciones.
[[CAJA Ejemplo — La lista de equipos del aula]]
Para el aula del Instituto Ko'ẽju, Panambi lista: un switch Gigabit de 16 puertos (13 ocupados: 10 PC + impresora + access point + enlace al router; quedan 3 libres), el router con firewall y DHCP y un access point para las notebooks de los docentes. La ONT la aporta el proveedor de internet que el colegio contrate.
[[/CAJA]]
## Access point y módem/ONT
El access point (punto de acceso) da acceso inalámbrico a la red cableada: convierte el cable en Wi-Fi para los dispositivos móviles. El módem u ONT es el equipo del proveedor que adapta la señal del medio contratado (fibra óptica, coaxial) al conector de red del cliente: la ONT es la variante para fibra al hogar.
Seguí el camino desde internet: entra por el módem u ONT, pasa al router y de ahí al switch, que reparte a los equipos cableados; el access point suma el Wi-Fi.
[[IMG T_image30.png|16.0]]
Figura 15.2 — Esquema de una red local típica.
[[TABLA]]
Equipo | Problema que resuelve | Dato clave al elegirlo
Switch | Interconectar los equipos de la LAN | Puertos y velocidad (Gigabit)
Router | Conectar la LAN con otras redes | Servicios: DHCP, firewall, NAT
Access point | Sumar acceso inalámbrico | Estándar Wi-Fi y ubicación
Módem / ONT | Adaptar la señal del proveedor | Lo define el medio contratado
Repetidor | Extender el alcance de la señal | Dónde ubicarlo (mitad de camino)
[[/TABLA]]
## Otros equipos
Completan el cuadro el repetidor o extensor (regenera la señal para llegar más lejos), el firewall dedicado (filtra el tráfico en organizaciones que lo requieren) y los equipos combinados: el 'router del proveedor' hogareño suele ser ONT, router, switch de cuatro bocas y access point en una sola caja.
[[CAJA En Paraguay — La caja del proveedor]]
En los hogares paraguayos con fibra, la 'cajita' que instala el proveedor concentra ONT, router, switch y Wi-Fi. Para el técnico es clave saberlo: cuando un cliente pide 'mejorar el Wi-Fi', muchas veces la solución no es cambiar esa caja sino sumar un access point bien ubicado, cableado hasta donde la señal no llega.
[[/CAJA]]
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
## Actividades de aplicación
Marcá la opción correcta:
1. El equipo que reenvía los datos solo al puerto del destinatario dentro de la LAN es:
    a) El router
    b) El switch
    c) La ONT
    d) El repetidor
2. El equipo que conecta la red local con internet y encamina los paquetes es:
    a) El switch
    b) El access point
    c) El router
    d) El patch panel
3. La ONT es el equipo que:
    a) Da Wi-Fi a los celulares
    b) Adapta la señal de la fibra del proveedor
    c) Interconecta los equipos del aula
    d) Imprime en red
4. Un access point sirve para:
    a) Reemplazar al switch
    b) Dar acceso inalámbrico a la red cableada
    c) Traducir nombres de dominio
    d) Filtrar virus
Completá los espacios:
5. Un switch ________ de 1.000 Mb/s por puerto se conoce como switch Gigabit.
6. El router que reparte direcciones automáticamente cumple la función de servidor ________.
7. El equipo del proveedor para fibra al hogar se llama ________.
Verdadero o falso (justificá las falsas):
8. (....) Dentro de una LAN, los equipos se comunican entre sí a través del switch sin pasar por internet.
9. (....) El switch decide el camino de los paquetes hacia otras redes.
10. (....) El router hogareño típico integra varias funciones en una sola caja.
Respondé y fundamentá:
11. Con la metáfora de un edificio de correspondencia interna y correo externo, explicá la diferencia entre switch y router.
12. Un local comercial tiene buena señal Wi-Fi en el salón y nula en el depósito del fondo. Proponé dos soluciones con equipos de esta clase y compará.

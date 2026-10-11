@@H2 Clase 13 — Redes por alcance: LAN, MAN y WAN
[[FICHA]]
Capacidad: Analiza los principios de las redes de comunicación.
Tema: Redes geográficamente distribuidas (LAN, MAN, WAN): definición, características, alcance y elementos.
- Clasifica redes según su alcance geográfico.
- Describe los elementos característicos de LAN, MAN y WAN.
- Explica internet como interconexión de redes de distinto alcance.
[[/FICHA]]
[[IMG T_image25.jpg|12.8]]
Figura 13.1 — Representación del alcance de distintas redes.
## LAN: la red local
La LAN (local area network) cubre un espacio limitado: una casa, una oficina, un aula, un edificio. Es la red que se diseña y administra por completo: sus equipos, su cableado, su switch y su router pertenecen al dueño del lugar. Suele ofrecer velocidades altas y demoras bajas por las distancias cortas, aunque una medición real también depende de congestión, calidad del enlace, ruta y políticas de los equipos intermedios.
[[CAJA Concepto clave — Alcance]]
Extensión geográfica que una red cubre y administra. Al crecer el alcance crecen la distancia, la demora y la dependencia de terceros: la LAN es tuya; la WAN se contrata.
[[/CAJA]]
## MAN: la red metropolitana
La MAN (metropolitan area network) interconecta redes locales dentro de una ciudad o área metropolitana: las sucursales de un banco, las dependencias de una municipalidad, los edificios de una universidad. Suele apoyarse en fibra óptica tendida por la ciudad, propia o alquilada a un proveedor.
[[CAJA Ejemplo — ¿Qué red es cuál?]]
En el proyecto del Instituto Ko'ẽju, Panambi lo explica con el propio colegio: el aula de informática será una LAN; si el colegio conectara su sede céntrica con el anexo del otro barrio, contrataría un enlace tipo MAN; y cuando un estudiante consulta un sitio alojado en otro país, sus datos viajan por la WAN de los proveedores.
[[/CAJA]]
## WAN: la red de área amplia
La WAN (wide area network) une redes separadas por grandes distancias: ciudades, países, continentes. Usa enlaces de larga distancia (fibras troncales, enlaces satelitales) operados por empresas de telecomunicaciones. Internet es el caso extremo: la interconexión mundial de millones de redes, una 'red de redes'.
[[TABLA]]
Red | Alcance típico | Ejemplo | ¿Quién la administra?
PAN | Metros (personal) | Celular + auriculares Bluetooth | El usuario
LAN | Casa, aula, edificio | El aula de informática | El dueño del lugar
MAN | Ciudad | Sucursales de un banco en una misma ciudad | La organización + proveedor
WAN | País, continente, mundo | Internet | Operadores de telecomunicaciones
[[/TABLA]]
## PAN y la escala completa
En el extremo más chico está la PAN (personal area network): los dispositivos personales conectados entre sí, como el celular y los auriculares por Bluetooth. La escala completa —PAN, LAN, MAN, WAN— describe cualquier comunicación: un mensaje puede nacer en tu PAN, cruzar la LAN del aula y viajar por la WAN hasta otro continente.
Leé los anillos de adentro hacia afuera: de la PAN (unos metros) a la WAN (todo el mundo). Cada escala contiene a la anterior.
[[IMG T_image26.png|14.0]]
Figura 13.2 — Escala de las redes: PAN, LAN, MAN y WAN.
[[CAJA En Paraguay — La troncal que une al país]]
La Red Nacional de Fibra Óptica es la gran WAN pública del Paraguay: su Red Metro interconecta instituciones del Estado en la capital y su Red Troncal, en modernización junto a COPACO y la ANDE, extiende la capacidad hacia el interior. Sobre infraestructuras así viajan los datos de todas las LAN del país.
[[/CAJA]]
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
## Actividades de aplicación
Marcá la opción correcta:
1. La red que cubre un aula o un edificio es una:
    a) PAN
    b) LAN
    c) MAN
    d) WAN
2. Las sucursales de una empresa distribuidas en una misma ciudad se interconectan típicamente con una:
    a) PAN
    b) LAN
    c) MAN
    d) WAN
3. Internet se describe mejor como:
    a) Una LAN gigante
    b) Una red de redes de alcance mundial
    c) Una MAN pública
    d) Un protocolo
4. A medida que crece el alcance de una red:
    a) Disminuye la demora
    b) Crece la dependencia de terceros y la distancia
    c) Desaparecen los protocolos
    d) Baja el costo de los enlaces
Completá los espacios:
5. La sigla LAN significa red de área ________.
6. La red personal de dispositivos cercanos (celular y auriculares) es una ________.
7. Las WAN usan enlaces de larga distancia operados por empresas de ________.
Verdadero o falso (justificá las falsas):
8. (....) En general, la LAN ofrece más velocidad y menos demora que la WAN.
9. (....) Una MAN interconecta redes locales dentro de una ciudad.
10. (....) El dueño de una LAN también administra los enlaces de la WAN que usa.
Respondé y fundamentá:
11. Trazá el recorrido de un correo desde una PC del aula hasta un servidor en Europa, nombrando las redes que atraviesa.
12. Una cooperativa tiene casa central y tres sucursales en la misma ciudad. ¿Qué tipo de red las une y qué elemento contrataría a un proveedor?

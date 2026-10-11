@@H2 Clase 12 — Protocolos y estándares
[[FICHA]]
Capacidad: Analiza los principios de las redes de comunicación.
Tema: Protocolos y estándares: concepto, tipos, características y funciones.
- Explica la función de los protocolos en la comunicación de datos.
- Reconoce los protocolos principales de la familia TCP/IP y su rol.
- Interpreta una dirección IP, su máscara y la puerta de enlace.
[[/FICHA]]
[[IMG T_image23.jpg|12.8]]
Figura 12.1 — Configuración de parámetros de red IPv4.
## Qué es un protocolo
Un protocolo es el conjunto de reglas que definen cómo se establece, mantiene y cierra una comunicación: cómo se identifican los equipos, cómo se fragmentan los datos, cómo se detectan errores y cómo se confirma la recepción. Dos equipos de marcas y sistemas distintos se entienden porque hablan los mismos protocolos.
[[CAJA Concepto clave — Dirección IP privada]]
Direcciones reservadas para redes internas por la RFC 1918: 10.0.0.0 a 10.255.255.255, 172.16.0.0 a 172.31.255.255 y 192.168.0.0 a 192.168.255.255. Se repiten en millones de redes locales sin conflicto porque no salen a internet: el router las traduce hacia afuera.
[[/CAJA]]
## La familia TCP/IP
Internet y casi todas las redes locales funcionan sobre la familia TCP/IP, organizada por capas donde cada protocolo cumple una función: IP direcciona y encamina los paquetes; TCP garantiza que lleguen completos y en orden (UDP los envía rápido sin garantías, útil para video en vivo); DNS traduce nombres como mec.gov.py a direcciones numéricas; DHCP reparte direcciones automáticamente; HTTP y HTTPS transportan las páginas web, con la S de la versión cifrada.
[[CAJA Ejemplo — El plan de direcciones del aula]]
Para el aula del Instituto Ko'ẽju, Panambi define un plan simple: red 192.168.10.0 con máscara 255.255.255.0, el router en 192.168.10.1 como puerta de enlace, la impresora fija en 192.168.10.20 y las diez computadoras recibiendo su dirección automáticamente por DHCP. Todo queda escrito en la carpeta técnica del proyecto.
[[/CAJA]]
## Direcciones IP
Cada equipo de la red se identifica con una dirección IP: cuatro números de 0 a 255 separados por puntos, como 192.168.0.15. La máscara de subred indica qué parte identifica a la red y qué parte al equipo. En una máscara 255.255.255.0 (/24), dos equipos están en la misma red cuando coinciden los tres primeros octetos; con otra máscara ese atajo puede fallar y hay que interpretar la IP junto con su máscara. La puerta de enlace es la dirección del dispositivo (el router) por donde la red local sale hacia afuera.
Observá cómo se parte una dirección IP: la máscara separa la parte de red de la parte del equipo. La puerta de enlace es la salida de la red local hacia internet.
[[IMG T_image24.png|16.0]]
Figura 12.2 — Anatomía de una dirección IP y la puerta de enlace.
[[TABLA]]
Protocolo | Función | Ejemplo de uso
IP | Direcciona y encamina paquetes | Llevar datos de 192.168.0.15 al router
TCP | Entrega completa y en orden | Descargar un archivo sin errores
UDP | Entrega rápida sin garantías | Videollamada en vivo
DNS | Traduce nombres a direcciones | mec.gov.py → dirección IP
DHCP | Asigna direcciones automáticamente | La PC recibe su IP al encender
HTTPS | Transporta páginas web cifradas | Home banking, compras en línea
[[/TABLA]]
## Estándares y organismos
Los estándares son especificaciones publicadas por organismos internacionales para que fabricantes distintos produzcan tecnología compatible: el IEEE mantiene la familia 802 (802.3 es Ethernet, la red cableada; 802.11 es Wi-Fi), la ISO normaliza el modelo de referencia de capas y la TIA publica las normas de cableado que veremos más adelante. Sin estándares, cada marca sería una isla.
[[CAJA En Paraguay — El dominio .py]]
Los nombres de internet del país terminan en .py y su registro lo administra NIC Paraguay. Cuando escribís una dirección terminada en .py, el protocolo DNS la traduce a la dirección IP del servidor que la aloja: la misma traducción que hace tu red con cualquier sitio del mundo.
[[/CAJA]]
## ¿Están en la misma red? Cómo se verifica
Con una máscara 255.255.255.0 (/24), la parte de red son los tres primeros números y el último identifica al equipo. Dos equipos se comunican directamente solo si su parte de red coincide; si no, el tráfico tiene que pasar por un router. En Windows, el comando ipconfig muestra la dirección IPv4, la máscara y la puerta de enlace de la placa de red; ping comprueba si otro equipo responde.
Los números del último octeto también tienen reglas: en una red /24 la dirección terminada en .0 identifica a la red, la terminada en .255 es la de difusión (llega a todos) y las 254 restantes, de .1 a .254, se pueden asignar a equipos. Por eso conviene reservar un rango fijo para impresoras y equipos de red y dejar el resto al DHCP.
[[CAJA Ejemplo — La impresora que «no aparece» en la biblioteca]]
En la biblioteca del Instituto Ko'ẽju, una PC muestra en ipconfig: IPv4 172.16.30.45, máscara 255.255.255.0, puerta de enlace 172.16.30.1. La impresora de la biblioteca tiene configurada la dirección fija 172.16.31.8 con la misma máscara.
Paso 1. Parte de red de la PC: 172.16.30. Parte de red de la impresora: 172.16.31.
Paso 2. No coinciden: están en redes distintas, por eso la PC no la encuentra.
Paso 3. Corrección: asignar a la impresora una dirección libre dentro de la red de la biblioteca, por ejemplo 172.16.30.240, fuera del rango que reparte el DHCP.
Paso 4. Verificación: desde la PC, ping 172.16.30.240 debe responder; después se vuelve a agregar la impresora.
[[/CAJA]]
[[CAJA Errores frecuentes — Con las direcciones IP]]
• Comparar solo el último número de dos direcciones y concluir que están en la misma red.
• Asignar a mano una dirección que el DHCP también reparte: aparecen conflictos de IP.
• Usar la dirección terminada en .0 o .255 para un equipo.
• Olvidar la puerta de enlace: el equipo ve la red local, pero no sale a internet.
[[/CAJA]]
## Actividades de aplicación
Marcá la opción correcta:
1. El protocolo que traduce nombres de sitios a direcciones numéricas es:
    a) TCP
    b) DNS
    c) DHCP
    d) IP
2. La diferencia clave entre TCP y UDP es que:
    a) TCP garantiza la entrega completa y en orden; UDP prioriza la velocidad
    b) UDP cifra los datos; TCP no
    c) TCP es inalámbrico; UDP es cableado
    d) No hay diferencia
3. En una red doméstica típica, la dirección 192.168.0.1 suele corresponder a:
    a) La impresora
    b) La puerta de enlace (router)
    c) El servidor DNS de internet
    d) Un sitio web
4. El estándar IEEE 802.11 corresponde a:
    a) Ethernet cableada
    b) Wi-Fi
    c) El cableado estructurado
    d) La fibra óptica
Completá los espacios:
5. El protocolo ________ reparte direcciones IP automáticamente a los equipos.
6. La ________ de subred indica qué parte de la dirección identifica a la red.
7. La S final de HTTPS indica que la comunicación viaja ________.
Verdadero o falso (justificá las falsas):
8. (....) Dos equipos de marcas distintas pueden comunicarse si comparten protocolos.
9. (....) Las direcciones que empiezan con 192.168 son públicas de internet.
10. (....) UDP es preferible a TCP para descargar un archivo que no admite errores.
Respondé y fundamentá:
11. Explicá el viaje de una página web desde que escribís su nombre hasta que la ves, nombrando al menos tres protocolos.
12. ¿Por qué a la impresora del aula conviene fijarle la dirección IP en vez de dejarla por DHCP?

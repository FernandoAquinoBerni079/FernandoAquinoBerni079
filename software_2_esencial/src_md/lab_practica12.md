@@H1 Práctica 12 — Protocolos y estándares
Nombre y Apellido: _______________________________  Curso: ______  Fecha: ____ / ____ / ____
Competencia de la práctica: Leer la configuración TCP/IP real del equipo con ipconfig e interpretarla.
[[IMG L_image15.jpg|10.9]]
Figura 12.3 — Configuración y prueba de una red local.
## Lo que necesitás saber
• El Símbolo del sistema (cmd) ejecuta comandos de diagnóstico de red.
• ipconfig /all muestra dirección IP, máscara, puerta de enlace, servidores DNS y si la dirección vino por DHCP.
## Actividades
Actividad 1 — Objetivo: Obtener la configuración de red del equipo con ipconfig.
[[CAJA Ejemplo — Modelo a reproducir]]
Datos a registrar: dirección IPv4, máscara de subred, puerta de enlace predeterminada, servidores DNS, DHCP habilitado (sí/no).
[[/CAJA]]
   1. Presioná Windows + R, escribí cmd y presioná Enter.
   2. Escribí ipconfig /all y presioná Enter.
   3. Ubicá el adaptador activo (Ethernet o Wi-Fi) y leé sus datos.
   4. Anotá los cinco datos del modelo tal como aparecen.
Punto de control: Registraste la dirección IPv4 realmente observada, su máscara y el estado del adaptador, y la clasificaste como privada, pública, de enlace local o ausente. Si aparece 169.254.x.x o no hay IPv4 utilizable, registrá la anomalía y consultá al docente sin cambiar la configuración.
Actividad 2 — Objetivo: Interpretar la configuración en una tabla de Word.
[[CAJA Ejemplo — Modelo a reproducir]]
Tabla de 3 columnas: Dato / Valor en mi equipo / Qué significa. Cinco filas con los datos relevados y su interpretación en una línea cada una.
[[/CAJA]]
   1. Abrí Word e insertá una tabla de 3 × 6 (encabezado + cinco datos).
   2. Volcá los valores obtenidos con ipconfig.
   3. Completá la tercera columna explicando cada dato con tus palabras (una línea).
   4. Compará tu IPv4 y tu máscara con las de un compañero. Si ambas máscaras son 255.255.255.0 (/24), verificá que coinciden los tres primeros octetos. Si la máscara es distinta, no uses ese atajo: registrá la máscara y consultá el cálculo de red con el docente.
   5. Guardá como TCPIP_[apellido].docx.
Punto de control: La tabla explica los cinco datos y la pertenencia a la misma red se justificó usando la máscara; con /24, coinciden los tres primeros octetos.
[[CAJA Desafío final (si terminás antes)]]
Ejecutá nslookup mec.gov.py en el cmd, anotá la dirección que responde y explicá en una línea qué protocolo acabás de usar.
[[/CAJA]]

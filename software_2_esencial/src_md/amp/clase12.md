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

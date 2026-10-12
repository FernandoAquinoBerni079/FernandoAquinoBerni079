@@H2 Clase 18 — Medios de transmisión no guiados
[[FICHA]]
Capacidad: Identifica las características principales de los medios de transmisión más utilizados.
Tema: Medios no guiados: concepto, tipos, normativas, características y aplicación.
- Caracteriza las transmisiones por Wi-Fi, Bluetooth, radioenlaces y satélite.
- Relaciona las bandas de frecuencia del Wi-Fi con su alcance y velocidad.
- Reconoce el rol del Estado en la administración del espectro radioeléctrico.
[[/FICHA]]
[[IMG T_image35.jpg|12.8]]
Figura 18.1 — Evaluación de la ubicación de un punto de acceso Wi-Fi.
## Transmitir por el aire
Los medios no guiados transmiten por ondas electromagnéticas sin cable de por medio. Ganan movilidad y evitan obras, a cambio de compartir el aire: la señal se atenúa con la distancia y los obstáculos, y compite con las señales vecinas. El espectro radioeléctrico es un recurso limitado, y por eso el Estado lo administra.
[[CAJA Concepto clave — Espectro radioeléctrico]]
Conjunto de las frecuencias de radio disponibles para transmitir. Es un recurso limitado del Estado: algunas bandas son de uso libre regulado (como las del Wi-Fi) y otras se licitan a operadores con licencia.
[[/CAJA]]
## Wi-Fi
El Wi-Fi (familia IEEE 802.11) es la tecnología habitual de LAN inalámbrica. Puede operar en 2,4 GHz, 5 GHz y, en equipos compatibles, 6 GHz. La frecuencia influye en propagación y penetración de obstáculos, pero la velocidad real no depende solo de «más GHz»: también intervienen la generación Wi-Fi, el ancho de canal, la cantidad de flujos espaciales, la interferencia, la distancia y las capacidades del cliente. En general, 2,4 GHz llega más lejos y se congestiona más; 5 y 6 GHz ofrecen más canales y pueden habilitar mayor rendimiento cuando las condiciones y los equipos lo permiten. En Paraguay, CONATEL habilitó en 2025 (Resolución 1035/2025) solo la porción baja de la banda de 6 GHz, de 5.925 a 6.425 MHz, para Wi-Fi 6E y Wi-Fi 7, con límites de potencia: los equipos deben estar homologados y configurados según la norma técnica NTC-RF-5925:2025.
Ubicá las tres bandas del Wi-Fi sobre los ejes. La frecuencia más alta suele tener menor alcance y penetración, pero no determina por sí sola la velocidad: el rendimiento depende del estándar, ancho de canal, interferencia, MIMO y dispositivo. La banda de 6 GHz ofrece espectro amplio y menos congestionado para equipos compatibles.
[[IMG T_image36.png|16.0]]
Figura 18.2 — Las bandas del Wi-Fi: alcance frente a velocidad.
[[CAJA Ejemplo — El Wi-Fi de los docentes]]
En el proyecto del Instituto Ko'ẽju, el access point del aula transmite en 2,4 y 5 GHz: los celulares viejos se enganchan a la primera y las notebooks de los docentes aprovechan la segunda. Panambi lo ubica en el techo, centrado y lejos del microondas de la cocina: el aire también se diseña.
[[/CAJA]]
## Bluetooth y radioenlaces
Bluetooth conecta dispositivos personales a corta distancia: auriculares, teclados, impresoras de tickets portátiles; es la red PAN por excelencia. Los radioenlaces punto a punto unen ubicaciones distantes con antenas direccionales enfrentadas: la solución clásica para llevar internet donde el cable no llega, con la línea de vista despejada como requisito.
[[TABLA]]
Medio | Alcance típico | Fortaleza | Limitación
Wi-Fi 2,4 GHz | Decenas de metros | Atraviesa mejor los obstáculos | Banda saturada, menor velocidad
Wi-Fi 5 y 6 GHz | Menor que 2,4 | Alta velocidad | Menos alcance
Bluetooth | Metros | Bajo consumo, dispositivos personales | Corto alcance
Radioenlace | Kilómetros | Une puntos sin cable | Exige línea de vista
Satélite LEO | Todo el territorio | Llega donde nada más llega | Costo del servicio y clima
[[/TABLA]]
## Satélite
La transmisión satelital cubre cualquier punto del territorio. Los satélites tradicionales, muy lejanos, imponen demoras altas; las constelaciones de órbita baja (LEO) redujeron esa demora y volvieron viable el internet satelital de alta velocidad para zonas rurales y aisladas, complementando —no reemplazando— a la fibra y los radioenlaces.
[[CAJA En Paraguay — 5G y Starlink: el aire paraguayo se mueve]]
El espectro paraguayo vivió dos hitos recientes: la licencia de operación de Starlink (2023) llevó internet satelital de órbita baja a las zonas más aisladas del Chaco, y la licitación 5G articulada por CONATEL y el MITIC adjudicó en 2025 espectro de 3,5 GHz a Claro y a Nubicom; la quinta generación móvil entró en servicio el 18 de diciembre de 2025 con el lanzamiento de Claro.
[[/CAJA]]
## Elegir canal y ubicación del access point
En la banda de 2,4 GHz los canales se superponen entre sí: los únicos tres que no se pisan son el 1, el 6 y el 11. Si dos redes vecinas usan canales cercanos, se interfieren y las dos funcionan peor. Por eso, antes de configurar un access point, el técnico releva qué canales usan las redes del lugar y elige el menos ocupado entre esos tres. En 5 GHz hay muchos más canales sin superposición, lo que alivia el problema.
La ubicación pesa tanto como el canal. El access point rinde mejor alto, en un lugar central y sin obstáculos metálicos ni de hormigón entre él y los usuarios. Conviene además que llegue por cable al switch: un access point cableado entrega mucho más que un repetidor que retransmite por el aire.
[[CAJA Ejemplo — El Wi-Fi de la biblioteca]]
En la biblioteca del Instituto Ko'ẽju, un relevamiento con el celular detecta cinco redes en 2,4 GHz: dos en el canal 1, dos en el canal 6 y una en el canal 3.
Paso 1. Canales sin superposición: 1, 6 y 11. El 1 y el 6 están ocupados por dos redes cada uno.
Paso 2. La red del canal 3 se superpone con el 1 y con el 6, pero no con el 11.
Paso 3. Decisión para 2,4 GHz: canal 11. Para 5 GHz se deja la selección automática, porque hay muchos canales libres.
Paso 4. Ubicación: en el techo, en el centro de la sala, lejos de las estanterías metálicas, y cableado al switch.
[[/CAJA]]
[[CAJA Errores frecuentes — Con el Wi-Fi]]
• Elegir un canal «del medio» (3, 4, 8) en 2,4 GHz: se superpone con dos canales a la vez.
• Esconder el access point en un mueble o en el piso.
• Usar un repetidor inalámbrico donde se puede llevar un cable.
• Dejar la red con la contraseña de fábrica o con seguridad anterior a WPA2.
[[/CAJA]]
## Actividades de aplicación
Marcá la opción correcta:
1. La banda Wi-Fi con más alcance pero más interferencia es la de:
    a) 2,4 GHz
    b) 5 GHz
    c) 6 GHz
    d) 60 GHz
2. Bluetooth es el medio típico de una red:
    a) WAN
    b) MAN
    c) PAN
    d) troncal
3. El requisito característico de un radioenlace punto a punto es:
    a) Cable coaxial
    b) Línea de vista despejada entre antenas
    c) Fibra multimodo
    d) Un patch panel
4. La ventaja de las constelaciones satelitales de órbita baja (LEO) es:
    a) Eliminar la lluvia
    b) Reducir la demora frente a los satélites lejanos
    c) No usar espectro
    d) Reemplazar a la fibra
Completá los espacios:
5. El estándar del Wi-Fi pertenece a la familia IEEE 802.________.
6. Las generaciones actuales del Wi-Fi se nombran Wi-Fi 4, 5, 6, 6E y ________.
7. El recurso limitado de frecuencias que administra el Estado es el ________ radioeléctrico.
Verdadero o falso (justificá las falsas):
8. (....) Por usar 5 GHz, una red Wi-Fi es siempre más rápida que una red de 2,4 GHz.
9. (....) El espectro radioeléctrico es ilimitado y de uso totalmente libre.
10. (....) El internet satelital reemplaza a la fibra en las ciudades.
Respondé y fundamentá:
11. Una escuela rural sin cobertura de fibra ni de radioenlaces cercanos necesita internet. ¿Qué medio proponés y qué dos limitaciones le advertís?
12. ¿Por qué el Wi-Fi del aula conviene como complemento y no como reemplazo de la red cableada?

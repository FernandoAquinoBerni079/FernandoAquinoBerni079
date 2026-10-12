@@H2 Clase 19 — Cableado estructurado
[[FICHA]]
Capacidad: Analiza las normas de cableado estructurado utilizadas en la actualidad.
Tema: Normas de cableado estructurado: tipos, características, alcance y aplicación.
- Explica el propósito del cableado estructurado y sus subsistemas.
- Aplica la regla de los 100 metros de canal en un plano.
- Reconoce los esquemas de conexión T568A y T568B y el rol de la certificación.
[[/FICHA]]
[[IMG T_image37.jpg|12.8]]
Figura 19.1 — Organización de equipos y cableado en un rack.
## Qué es el cableado estructurado
El cableado estructurado es la instalación de red planificada según normas internacionales, pensada para servir a cualquier equipo y durar muchos años: puntos de red genéricos, tendidos ordenados, remates normalizados y documentación. Su referencia principal es la familia de normas ANSI/TIA-568, que estandariza desde el cable hasta el conector.
[[CAJA Concepto clave — Canal]]
Recorrido completo de la señal entre el equipo del usuario y el equipo del rack: patch cord + tendido fijo + patch cord. La regla de los 100 metros se mide sobre el canal, no solo sobre el cable de la pared.
[[/CAJA]]
## Los subsistemas
La norma organiza la instalación en subsistemas: el área de trabajo (la roseta y el patch cord del usuario), el cableado horizontal (de cada roseta al cuarto de telecomunicaciones del piso), el cuarto de telecomunicaciones (rack, patch panel y equipos), el cableado vertical o backbone (une pisos y edificios, a menudo con fibra) y la entrada de servicios (donde llega el proveedor).
[[CAJA Ejemplo — El punto más lejano del aula]]
En el plano del Instituto Ko'ẽju, el puesto más lejano queda a 34 metros de tendido fijo del rack: sumando los patch cords, el canal ronda los 38 metros, holgadamente dentro de norma. Panambi lo deja asentado en la carpeta técnica, junto al esquema elegido (T568B en toda la instalación) y el compromiso de certificar los 12 enlaces.
[[/CAJA]]
## La regla de los 100 metros
En el cableado horizontal con par trenzado, el canal completo no debe superar los 100 metros: hasta 90 metros de tendido fijo (roseta a patch panel) más un total de 10 metros de patch cords en los extremos. Superar el límite degrada la señal, aunque el cable 'funcione': la norma existe para garantizar las prestaciones de la categoría.
Medí el canal completo: hasta 90 metros de tendido fijo (de la roseta al patch panel) más un total de 10 metros de patch cords en los extremos; nunca más de 100 metros.
[[IMG T_image38.png|16.0]]
Figura 19.2 — La regla de los 100 metros del canal de cableado horizontal.
[[TABLA]]
Subsistema | Qué abarca | Medio habitual
Área de trabajo | Roseta y patch cord del usuario | UTP
Cableado horizontal | Roseta → cuarto de telecomunicaciones | UTP cat. 6/6A
Cuarto de telecomunicaciones | Rack, patch panel, switches | —
Backbone (vertical) | Une pisos y edificios | Fibra óptica
Entrada de servicios | Llegada del proveedor | Fibra del operador
[[/TABLA]]
## T568A, T568B y certificación
Los ocho conductores del par trenzado se rematan siguiendo los esquemas normalizados T568A o T568B. En un enlace Ethernet directo convencional se usa el mismo esquema en ambos extremos y se documenta el criterio adoptado. Un cable cruzado intencional usa A en un extremo y B en el otro, aunque hoy muchos equipos corrigen automáticamente el cruce (Auto MDI-X). En cableado estructurado profesional, la verificación con un certificador comprueba que el enlace cumple los parámetros de la categoría, no solo el orden de colores.
Compará los dos esquemas de colores: T568A y T568B intercambian los pares verde y naranja. Para un enlace directo, usá el mismo esquema en ambos extremos y documentalo; el uso A–B corresponde a un cruce intencional.
[[IMG T_image39.png|16.0]]
Figura 19.3 — Los esquemas de remate T568A y T568B.
[[CAJA En Paraguay — La carpeta técnica que diferencia]]
En las licitaciones y compras institucionales del país, la diferencia entre un instalador informal y una empresa seria suele estar en el papel: plano de puntos, esquema de conexión declarado, etiquetado y certificación de cada enlace. Esa carpeta técnica es lo que permite mantener la red años después sin adivinar nada.
[[/CAJA]]
## Verificar el canal y documentar la instalación
La regla de los 100 metros se verifica punto por punto en el plano: tendido fijo medido, más los patch cords de los dos extremos. Si un punto supera los 90 metros de tendido fijo, se busca otra solución antes de instalar: acercar el rack, cambiar el recorrido o sumar un cuarto de telecomunicaciones con su propio switch, unido al principal por un backbone.
Terminada la instalación, cada enlace se prueba. La certificación con un instrumento especializado mide parámetros como longitud, pérdida de señal y diafonía, y emite un informe por punto; en instalaciones chicas, como mínimo se usa un comprobador de continuidad que detecta pares cortados o cruzados. Todo resultado va a la carpeta técnica, junto con el plano de puntos y la tabla de etiquetas.
[[CAJA Ejemplo — Los puntos del salón de actos]]
El Instituto Ko'ẽju quiere tres puntos de red en el salón de actos, lejos del rack. Las mediciones de tendido fijo dan: punto 1, 78 m; punto 2, 86 m; punto 3, 94 m. Se prevén cordones de 3 m en el puesto y de 2 m en el rack.
Paso 1. Canal del punto 1: 78 + 3 + 2 = 83 m. Cumple.
Paso 2. Canal del punto 2: 86 + 3 + 2 = 91 m. Cumple (tendido fijo menor de 90 m y canal menor de 100 m).
Paso 3. Punto 3: el tendido fijo de 94 m supera los 90 m, aunque el canal total (99 m) no llegue a 100. No cumple.
Paso 4. Solución: un pequeño rack con switch en el salón, unido al principal por un backbone; los tres puntos rematan ahí con tendidos cortos.
[[/CAJA]]
[[CAJA Errores frecuentes — Con el cableado estructurado]]
• Medir solo el tendido de la pared y olvidar los patch cords.
• Rematar un extremo en T568A y el otro en T568B sin querer.
• Destrenzar los pares más de lo necesario al armar el jack.
• Entregar la instalación sin plano ni etiquetas: la red funciona, pero nadie puede mantenerla.
[[/CAJA]]
## Actividades de aplicación
Marcá la opción correcta:
1. La familia de normas de referencia del cableado estructurado es:
    a) IEEE 802.11
    b) ANSI/TIA-568
    c) ISO 9001
    d) Ley 642/95
2. El canal de cableado horizontal admite como máximo:
    a) 90 m de tendido fijo + 10 m de cordones
    b) 150 m en total
    c) 100 m de cordones
    d) 305 m
3. El backbone o cableado vertical suele resolverse con:
    a) Coaxial
    b) Fibra óptica
    c) Bluetooth
    d) Cable telefónico
4. Sobre T568A y T568B es correcto afirmar que:
    a) Solo el A es legal
    b) Conviene usar y documentar un esquema uniforme; en cada enlace directo, los dos extremos se terminan igual
    c) Se combinan al azar
    d) El B duplica la velocidad
Completá los espacios:
5. El recorrido completo de la señal, cordones incluidos, se llama ________.
6. El tendido fijo del cableado horizontal no debe superar los ________ metros.
7. La verificación instrumental de cada enlace terminado se llama ________.
Verdadero o falso (justificá las falsas):
8. (....) Un canal de 110 metros 'que funciona' cumple igual con la norma.
9. (....) La documentación y el etiquetado forman parte del cableado estructurado.
10. (....) El área de trabajo es el subsistema que une pisos entre sí.
Respondé y fundamentá:
11. Un cliente propone ahorrar saltando el patch panel y llevando los cables directo al switch. Escribí tu respuesta profesional en cuatro líneas.
12. ¿Por qué la certificación de enlaces protege tanto al cliente como al instalador?

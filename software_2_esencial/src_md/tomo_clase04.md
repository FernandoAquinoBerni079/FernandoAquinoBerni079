@@H2 Clase 4 — Slots de expansión
[[FICHA]]
Capacidad: Identifica las características principales de los slots de expansión de las placas madres.
Tema: Slots de expansión: concepto, tipos, características y conexión.
- Explica para qué sirven las ranuras de expansión.
- Distingue los tipos de ranura PCI Express por su tamaño y velocidad.
- Describe cómo se conecta correctamente una tarjeta de expansión.
[[/FICHA]]
[[IMG T_image7.jpg|12.8]]
Figura 4.1 — Instalación de una tarjeta de expansión en una computadora.
## Concepto
Los slots o ranuras de expansión son conectores alargados de la placa madre donde se insertan tarjetas que agregan funciones al equipo: video, red, sonido, capturadoras o puertos adicionales. Gracias a ellos una computadora puede crecer sin cambiar la placa: se 'expande' agregando la tarjeta que haga falta.
[[CAJA Concepto clave — Carril (lane) PCIe]]
Canal de comunicación punto a punto entre la ranura y el chipset o el procesador. Una ranura x16 tiene dieciséis carriles trabajando en paralelo; por eso es la indicada para las tarjetas de video, que mueven grandes volúmenes de datos.
[[/CAJA]]
## Tipos de ranura
El estándar actual es PCI Express (PCIe), que reemplazó al viejo PCI. Las ranuras se describen por su ancho lógico (x1, x4, x8, x16) y por su generación. El tamaño físico orienta, pero no siempre revela cuántos carriles están cableados eléctricamente: una ranura con largo x16 puede funcionar internamente con menos carriles. El conector M.2 también usa un formato compacto para SSD y tarjetas inalámbricas, pero su interfaz real debe verificarse en la placa y en el módulo.
[[CAJA Ejemplo — ¿Sirve esta placa para diseño?]]
Un cliente de Panambi quiere sumar una tarjeta de video para trabajar con diseño gráfico. El técnico verifica primero que la placa tenga una ranura PCIe x16 libre y que el gabinete y la fuente soporten la tarjeta. La respuesta al cliente incluye las tres verificaciones, no solo el precio.
[[/CAJA]]
## Características y generaciones
La generación y la cantidad de carriles determinan conjuntamente el ancho de banda. PCIe 3.0 opera a 8 GT/s por carril, PCIe 4.0 a 16 GT/s y PCIe 5.0 a 32 GT/s; por eso una misma tarjeta puede disponer de mucho más ancho de banda en una generación nueva. Las generaciones mantienen compatibilidad hacia atrás en muchos casos, pero el enlace negocia la velocidad y el ancho que ambos extremos soportan.
Compará el largo de las ranuras como referencia mecánica, pero verificá siempre la generación y los carriles eléctricos disponibles en la especificación de la placa. El rendimiento no se deduce únicamente por el tamaño visible.
[[IMG T_image8.png|16.3]]
Figura 4.2 — Ranuras PCIe a escala y velocidad por carril según la generación.
[[TABLA]]
Ranura | Largo relativo | Uso típico | Velocidad aprox. (gen. 4.0)
PCIe x1 | Corta | Red, sonido, puertos USB extra | 2 GB/s
PCIe x4 | Media | Capturadoras, controladoras | 8 GB/s
PCIe x16 | Larga | Tarjetas de video | 32 GB/s
M.2 | Módulo plano | SSD NVMe, tarjetas Wi-Fi | Hasta 8 GB/s (x4)
[[/TABLA]]
## Conexión
La tarjeta se inserta con el equipo apagado y desenchufado, alineando su borde de contactos con la ranura y presionando en forma pareja hasta que el seguro plástico trasero encastre. El soporte metálico de la tarjeta se atornilla al gabinete. Una tarjeta mal asentada es una de las causas más comunes de 'no da video'.
[[CAJA En Paraguay — La tarjeta de red que salva el día]]
En muchos talleres del país, la venta más común de tarjetas de expansión no es la de video sino la humilde tarjeta de red PCIe x1: cuando el puerto de red integrado de una placa se quema por una tormenta, agregar una tarjeta x1 cuesta mucho menos que cambiar la placa madre completa.
[[/CAJA]]
## Ancho de banda: cómo se calcula y para qué sirve
El ancho de banda aproximado de una ranura se obtiene multiplicando la velocidad por carril de su generación por la cantidad de carriles. Como referencia práctica, un carril PCIe 3.0 mueve cerca de 1 GB/s, uno 4.0 cerca de 2 GB/s y uno 5.0 cerca de 4 GB/s (en cada sentido). Con esa tabla mental el técnico estima si una ranura limita a la tarjeta que se va a instalar.
El enlace siempre trabaja con lo que soportan los dos extremos: la generación más baja y la cantidad menor de carriles. Una tarjeta PCIe 4.0 x4 en una ranura 3.0 x4 funciona, pero a velocidad de 3.0; una tarjeta x8 en una ranura x16 funciona como x8.
[[CAJA Ejemplo — La capturadora del área de comunicación]]
El área de comunicación del Instituto Ko'ẽju quiere instalar una capturadora de video PCIe 3.0 x4 para grabar las transmisiones de los actos. La placa de su equipo tiene una ranura x16 ocupada por la tarjeta de video y una ranura de largo x16 que, según el manual, funciona eléctricamente como x4 PCIe 3.0.
Paso 1. Capturadora: generación 3.0, 4 carriles. Ranura libre: generación 3.0, 4 carriles eléctricos.
Paso 2. Ancho de banda disponible: 4 carriles × ≈ 1 GB/s ≈ 4 GB/s. La capturadora trabaja a pleno.
Paso 3. Verificación física: la tarjeta x4 entra en una ranura de largo x16; se confirma que no choque con el disipador de la tarjeta de video.
Paso 4. Conclusión: se instala en la segunda ranura y se deja anotado en la ficha del equipo.
[[/CAJA]]
[[CAJA Errores frecuentes — Con las ranuras de expansión]]
• Deducir los carriles por el largo de la ranura: hay que leer el manual de la placa.
• Creer que una tarjeta nueva no funciona en una placa vieja: funciona, a la velocidad de la generación menor.
• Olvidar que algunas ranuras M.2 comparten carriles con una ranura PCIe y la desactivan al ocuparse.
• Instalar la tarjeta sin conectar su alimentación adicional cuando la tiene.
[[/CAJA]]
## Actividades de aplicación
Marcá la opción correcta:
1. Las ranuras de expansión sirven para:
    a) Conectar el monitor
    b) Agregar tarjetas que suman funciones al equipo
    c) Insertar la memoria RAM
    d) Alimentar la placa madre
2. La ranura indicada para una tarjeta de video es la:
    a) PCIe x1
    b) PCIe x4
    c) PCIe x16
    d) M.2
3. De la generación 3.0 a la 4.0 de PCIe, la velocidad por carril:
    a) Se mantiene
    b) Se duplica
    c) Se reduce a la mitad
    d) Se cuadruplica
4. El conector M.2 recibe habitualmente:
    a) Módulos de RAM
    b) Unidades SSD y tarjetas Wi-Fi
    c) Procesadores
    d) Discos duros de 3,5"
Completá los espacios:
5. El estándar de ranuras que reemplazó al viejo PCI es ________ ________.
6. Cada canal de comunicación de una ranura PCIe se llama ________.
7. Una tarjeta se inserta siempre con el equipo ________ y desenchufado.
Verdadero o falso (justificá las falsas):
8. (....) Una tarjeta PCIe de generación nueva no funciona en una ranura de generación anterior.
9. (....) La ranura PCIe x16 es físicamente la más larga.
10. (....) El seguro trasero de la ranura x16 debe encastrar al asentar la tarjeta.
Respondé y fundamentá:
11. Explicá por qué la tarjeta de video necesita más carriles que una tarjeta de sonido.
12. Un equipo 'no da video' después de instalar una tarjeta. Proponé dos causas relacionadas con la ranura y su conexión.

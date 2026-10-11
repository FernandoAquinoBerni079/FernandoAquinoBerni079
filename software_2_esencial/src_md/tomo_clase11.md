@@H2 Clase 11 — La red de computadoras
[[FICHA]]
Capacidad: Reconoce las características principales de una red de comunicaciones.
Tema: Red de computadoras: definición, ventajas, características, tipos, elementos y usos.
- Define qué es una red de computadoras y enumera sus ventajas.
- Identifica los elementos que participan en toda comunicación en red.
- Distingue redes cliente-servidor de redes entre pares.
[[/FICHA]]
[[IMG T_image21.jpg|12.8]]
Figura 11.1 — Análisis de una red de computadoras en clase.
## Definición y ventajas
Una red de computadoras es un conjunto de equipos conectados entre sí que comparten recursos e información mediante reglas comunes. Sus ventajas explican por qué hoy casi ninguna computadora trabaja aislada: compartir archivos e impresoras, comunicarse al instante, centralizar respaldos, acceder a internet desde todos los equipos y reducir costos al no duplicar recursos.
[[CAJA Concepto clave — Red de computadoras]]
Conjunto de equipos autónomos interconectados que comparten recursos e información según protocolos comunes. Sin reglas compartidas no hay red: solo cables.
[[/CAJA]]
## Elementos de la comunicación
En toda comunicación en red intervienen: un emisor, un receptor, un mensaje (los datos), un medio de transmisión (cable o aire) y un protocolo (las reglas que ambos extremos respetan). A eso se suman los componentes físicos —equipos, tarjetas de red, cables, dispositivos de interconexión— y el software de red que administra el intercambio.
Seguí el recorrido del mensaje del emisor al receptor por el medio, bajo las reglas del protocolo. Abajo, las dos formas de relacionar los equipos: entre pares y cliente-servidor.
[[IMG T_image22.png|16.0]]
Figura 11.2 — Los elementos de la comunicación y los dos modelos de red.
[[CAJA Ejemplo — El aula que trabaja en red]]
El encargo del Instituto Ko'ẽju no termina en las diez computadoras: piden que todas compartan la impresora de la secretaría, accedan a una carpeta común de trabajos y salgan a internet. Panambi lo traduce: además de los equipos, hay que diseñar una red cliente-servidor sencilla. Ese diseño ocupa el resto de la unidad.
[[/CAJA]]
## Tipos según la relación entre equipos
En una red entre pares (peer to peer) todos los equipos son iguales: cada uno comparte y consume recursos; es simple y sirve para grupos chicos. En una red cliente-servidor, uno o más servidores concentran servicios (archivos, impresión, aplicaciones) y los clientes los consumen: es el modelo de las instituciones, porque centraliza la administración y la seguridad.
[[TABLA]]
Elemento | Función en la comunicación | Ejemplo en el aula
Emisor | Origina el mensaje | La PC del estudiante
Receptor | Recibe e interpreta | La impresora de secretaría
Mensaje | Los datos transmitidos | El documento a imprimir
Medio | Camino físico de la señal | El cable de red
Protocolo | Reglas comunes | TCP/IP
[[/TABLA]]
## Usos cotidianos
Las redes están detrás de casi todo: la caja del supermercado que consulta precios, la planilla compartida de una oficina, las aulas con acceso a internet, la factura electrónica que viaja al servidor de la administración tributaria. Entender la red es entender la infraestructura invisible del trabajo moderno.
[[CAJA En Paraguay — Conectar es política pública]]
En Paraguay la conexión dejó de ser un lujo urbano: el programa estatal de internet gratuito mantiene más de 400 puntos Wi-Fi en plazas, hospitales y escuelas, incluidas comunidades del Chaco. Cada punto es, en el fondo, lo mismo que vas a diseñar en esta unidad: una red local que comparte una salida a internet.
[[/CAJA]]
## Compartir recursos con orden: permisos y servicios
Una red útil no es solo equipos conectados: es decidir qué se comparte, con quién y con qué permisos. En Windows, una carpeta compartida tiene permisos de lectura (ver y copiar) o de lectura y escritura (también modificar y borrar). Una impresora compartida se instala una vez en el equipo o servidor que la atiende, y los demás la agregan como impresora de red. La regla práctica es dar a cada usuario el permiso mínimo que necesita: el estudiante lee la carpeta de materiales y solo escribe en la de entregas.
La elección entre pares y cliente-servidor se decide por tres preguntas: cuántos equipos hay, qué tan importantes son los datos y quién va a administrar. Con pocos equipos y sin datos críticos, entre pares alcanza. Cuando hay más equipos, datos que respaldar o muchos usuarios, conviene un servidor: los permisos y las copias se manejan en un solo lugar.
[[CAJA Ejemplo — La red de la sala de profesores]]
La sala de profesores del Instituto Ko'ẽju tiene 4 computadoras y una impresora USB conectada a una de ellas. Los docentes quieren imprimir desde cualquier equipo y compartir las planillas de notas.
Paso 1. Tamaño: 4 equipos y un solo grupo de usuarios: una red entre pares es suficiente.
Paso 2. Impresora: se comparte desde la PC a la que está conectada; esa PC debe quedar encendida para que los demás impriman.
Paso 3. Planillas: se crea una carpeta compartida «Notas» con lectura y escritura solo para los docentes, y una copia semanal en un disco externo.
Paso 4. Límite del diseño: si la PC de la impresora se apaga o se rompe, nadie imprime. Por eso, a mediano plazo, Panambi propone una impresora de red.
[[/CAJA]]
En toda red, por chica que sea, conviene llevar un inventario: nombre de cada equipo, quién lo usa, qué recursos comparte y con qué permisos. Ese registro es el que permite a otro técnico continuar el trabajo, que es justamente lo que se espera de un profesional.
[[CAJA Errores frecuentes — Al armar una red chica]]
• Compartir carpetas con permiso total para «Todos»: cualquiera puede borrar el trabajo ajeno.
• Depender de una PC que se apaga para compartir la impresora de todo el grupo.
• No respaldar la carpeta compartida porque «está en la red».
• Confundir red local con internet: los equipos de la LAN se comunican aunque falle la conexión externa.
[[/CAJA]]
## Actividades de aplicación
Marcá la opción correcta:
1. Una red de computadoras es, ante todo:
    a) Un grupo de cables
    b) Equipos interconectados que comparten recursos con reglas comunes
    c) Un programa de mensajería
    d) Un tipo de servidor
2. En el modelo cliente-servidor:
    a) Todos los equipos son iguales
    b) Los servicios se concentran en servidores
    c) No hay protocolos
    d) Solo funciona sin cables
3. El protocolo es:
    a) El cable que une los equipos
    b) El conjunto de reglas que ambos extremos respetan
    c) El mensaje transmitido
    d) El equipo receptor
4. Una ventaja directa de trabajar en red es:
    a) Duplicar impresoras por equipo
    b) Compartir recursos y centralizar respaldos
    c) Evitar el uso de protocolos
    d) Aislar los equipos entre sí
Completá los espacios:
5. En una red entre ________ (peer to peer) todos los equipos comparten y consumen recursos por igual.
6. Los cinco elementos de la comunicación son emisor, receptor, mensaje, ________ y protocolo.
7. El modelo que concentra los servicios en servidores se llama ________-________.
Verdadero o falso (justificá las falsas):
8. (....) Dos computadoras cableadas entre sí ya forman una red aunque no compartan protocolo.
9. (....) El modelo cliente-servidor facilita la administración centralizada.
10. (....) Las redes solo sirven para acceder a internet.
Respondé y fundamentá:
11. Un cyber de barrio tiene ocho equipos que no comparten nada: cada uno con su pendrive y su impresora. Enumerá tres beneficios concretos de ponerlos en red.
12. ¿Por qué una institución educativa elige cliente-servidor en vez de una red entre pares? Da dos razones.

@@H2 Clase 14 — Topologías de red
[[FICHA]]
Capacidad: Analiza los principios de las redes de comunicación.
Tema: Topología de red física y lógica: definición, tipos, ventajas y desventajas.
- Diferencia topología física de topología lógica.
- Describe las topologías clásicas con sus ventajas y desventajas.
- Justifica el predominio actual de la estrella y la estrella extendida.
[[/FICHA]]
[[IMG T_image27.jpg|12.8]]
Figura 14.1 — Modelado físico de topologías de red.
## Topología física y lógica
La topología física es el mapa real de cables y equipos: cómo están conectados. La topología lógica describe cómo circulan los datos por esa estructura. Pueden no coincidir: una red puede cablearse en estrella y, si el centro es un hub (tecnología antigua), comportarse lógicamente como un bus donde todos escuchan el mismo canal. Con un switch, en cambio, cada puerto es un enlace propio.
[[CAJA Concepto clave — Punto único de falla]]
Componente cuya caída interrumpe toda la red: el troncal en el bus, el switch central en la estrella. Identificarlo es el primer paso para decidir dónde invertir en redundancia.
[[/CAJA]]
## Las topologías clásicas
En bus, todos los equipos cuelgan de un único cable troncal: barata, pero un corte en el troncal tumba toda la red. En anillo, cada equipo se conecta al siguiente formando un círculo por el que los datos giran: ordenada, pero una estación caída interrumpe el giro. Ambas dominaron el pasado y hoy sobreviven en usos puntuales.
[[CAJA Ejemplo — El plano del aula]]
Para el aula del Instituto Ko'ẽju, Panambi dibuja una estrella: las diez computadoras, la impresora y el access point llegan cada uno con su propio cable al switch del rack, y el switch se conecta al router. Son 13 puertos ocupados en el switch. En el plano marca el punto único de falla —el switch— y prevé puertos libres de reserva.
[[/CAJA]]
## Estrella, malla y árbol
En estrella, cada equipo se conecta con su propio cable a un dispositivo central (el switch): si un cable falla, cae solo ese equipo. Su punto débil es el centro: si el switch muere, cae todo. En malla, los nodos se interconectan por múltiples caminos: máxima tolerancia a fallas, máximo costo; se reserva para enlaces críticos. El árbol o estrella extendida conecta varias estrellas entre sí: es la forma de las redes de edificios.
Compará las cinco topologías: en bus todos cuelgan de un troncal; en anillo forman un círculo; en estrella cada equipo llega al switch; la malla suma caminos; el árbol une estrellas. La estrella es la que se impuso.
[[IMG T_image28.png|16.0]]
Figura 14.2 — Las cinco topologías de red.
[[TABLA]]
Topología | Ventaja principal | Desventaja principal
Bus | Poco cable, bajo costo | Un corte en el troncal tumba todo
Anillo | Tráfico ordenado | Una estación caída corta el giro
Estrella | Las fallas quedan aisladas | El centro es punto único de falla
Malla | Tolerancia máxima a fallas | Costo y cableado máximos
Árbol | Escala a edificios enteros | Hereda el riesgo de cada centro
[[/TABLA]]
## Por qué ganó la estrella
La estrella se impuso porque aísla las fallas (cada cable afecta a un solo equipo), simplifica el mantenimiento (todo converge en el rack) y escala: agregar un equipo es tirar un cable al switch. Las normas de cableado estructurado que veremos en la clase 19 están pensadas para esta topología.
[[CAJA En Paraguay — Malla donde no puede fallar]]
Los enlaces troncales que interconectan las centrales de los operadores del país se diseñan con caminos redundantes, acercándose a la malla: si una fibra se corta por una obra o una tormenta, el tráfico se desvía por otro camino. En la red de un aula esa inversión no se justifica; en la columna vertebral de las telecomunicaciones, sí.
[[/CAJA]]
## Dibujar la topología antes de cablear
El plano de topología es el primer documento de un proyecto de red. Se dibuja con símbolos simples (rectángulos para los equipos, líneas para los cables), se numera cada punto de red y se indica a qué puerto del switch llega. Con ese plano se cuentan los puertos, se estima el cable y se identifican los puntos únicos de falla antes de comprar nada.
Cuando la red ocupa varios ambientes o pisos, la estrella se repite en cada sector y los switches se unen entre sí: se forma un árbol. El enlace entre switches lleva el tráfico de muchos equipos a la vez, así que conviene que sea de mayor capacidad o que tenga un segundo cable de reserva.
[[CAJA Ejemplo — El laboratorio de ciencias en dos ambientes]]
El Instituto Ko'ẽju quiere conectar el laboratorio de ciencias: 6 computadoras en la sala principal y 3 en la sala de balanzas, separadas por un pasillo.
Paso 1. Opción estrella simple: un solo switch en la sala principal y 3 cables largos hasta la sala de balanzas.
Paso 2. Opción árbol: un switch en cada sala y un único cable entre ambos switches.
Paso 3. Comparación: la opción árbol usa menos cable por el pasillo y facilita sumar equipos en la sala de balanzas, pero agrega un segundo punto de falla (el switch chico).
Paso 4. Decisión: árbol, con un cable de reserva entre los dos switches, porque se prevé ampliar la sala de balanzas.
[[/CAJA]]
En el plano también se anota la longitud aproximada de cada cable: más adelante, con la regla de los 100 metros, vas a verificar que ningún tramo supere el máximo permitido.
[[CAJA Errores frecuentes — Con la topología]]
• Dibujar la topología física y suponer que describe también cómo circulan los datos.
• Unir switches en círculo «por las dudas»: sin la configuración adecuada se forman bucles que saturan la red.
• No marcar en el plano el punto único de falla ni prever puertos libres.
• Llevar un cable por cada equipo a otro ambiente cuando un segundo switch resuelve mejor.
[[/CAJA]]
## Actividades de aplicación
Marcá la opción correcta:
1. La topología donde cada equipo tiene su propio cable hasta un dispositivo central es:
    a) Bus
    b) Anillo
    c) Estrella
    d) Malla
2. El punto único de falla de la topología en estrella es:
    a) Cualquier cable
    b) El dispositivo central (switch)
    c) La impresora
    d) El último equipo
3. La topología con múltiples caminos entre nodos, usada en enlaces críticos, es la:
    a) Malla
    b) Bus
    c) Estrella
    d) Anillo
4. La topología lógica describe:
    a) El mapa físico de cables
    b) Cómo circulan los datos por la estructura
    c) La marca de los equipos
    d) El costo de la red
Completá los espacios:
5. En la topología en ________, todos los equipos cuelgan de un único cable troncal.
6. Conectar varias estrellas entre sí produce la topología en ________ o estrella extendida.
7. El componente cuya caída interrumpe toda la red se llama punto ________ de falla.
Verdadero o falso (justificá las falsas):
8. (....) En estrella, la falla de un cable afecta a un solo equipo.
9. (....) La topología física y la lógica siempre coinciden.
10. (....) La malla se usa en aulas por su bajo costo.
Respondé y fundamentá:
11. Compará qué pasa en bus y en estrella cuando falla (a) un cable de estación y (b) el elemento central o troncal.
12. ¿Dónde invertirías en redundancia en la red de un colegio con presupuesto limitado? Justificá con el concepto de punto único de falla.

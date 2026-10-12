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

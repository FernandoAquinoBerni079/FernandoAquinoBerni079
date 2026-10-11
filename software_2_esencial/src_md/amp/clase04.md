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

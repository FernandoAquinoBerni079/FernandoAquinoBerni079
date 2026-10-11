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

@@H1 Práctica 18 — Medios de transmisión no guiados
Nombre y Apellido: _______________________________  Curso: ______  Fecha: ____ / ____ / ____
Competencia de la práctica: Relevar las redes Wi-Fi del entorno con Windows y analizar bandas y seguridad.
[[IMG L_image24.jpg|10.9]]
Figura 18.3 — Referencia visual de un punto de acceso inalámbrico. La práctica de Software no requiere instalación física del equipo.
## Lo que necesitás saber
• El comando netsh wlan show networks mode=bssid lista redes visibles con canal y seguridad y, según la versión/controlador, puede mostrar también la banda. El número de canal por sí solo no siempre permite distinguir 2,4/5/6 GHz en equipos modernos.
• Muchas redes en el mismo canal de 2,4 GHz se interfieren entre sí.
## Actividades
Actividad 1 — Objetivo: Listar las redes Wi-Fi visibles desde el equipo.
[[CAJA Ejemplo — Modelo a reproducir]]
Registro por red: nombre (SSID), autenticación, canal. Mínimo cinco redes (si el equipo no tiene Wi-Fi, el docente provee un listado impreso).
[[/CAJA]]
   1. Abrí el Símbolo del sistema (Windows + R → cmd).
   2. Escribí netsh wlan show networks mode=bssid y presioná Enter.
   3. Recorré el listado y registrá nombre, autenticación y canal de cinco redes.
   4. Si la salida informa «Banda», registrala. Si solo muestra canal, no deduzcas automáticamente la banda: anotá «no determinada» salvo que el docente proporcione la banda/frecuencia de referencia.
Punto de control: Tenés cinco redes registradas con sus tres datos.
Actividad 2 — Objetivo: Analizar el relevamiento en Excel.
[[CAJA Ejemplo — Modelo a reproducir]]
Tabla: SSID | Canal | Banda verificada (2,4/5/6 GHz o «no determinada») | Seguridad. Debajo: cuántas redes comparten el canal más usado y una recomendación de banda/canal para una red nueva.
[[/CAJA]]
   1. Cargá la tabla del modelo con tus cinco redes.
   2. Completá la banda con el dato informado por el sistema o por el listado de referencia. Si no aparece, escribí «no determinada»; no clasifiques 2,4/5/6 GHz solamente por el número de canal.
   3. Contá cuántas redes usan el canal más repetido y escribilo en una celda.
   4. Escribí en una línea qué canal usarías para una red nueva y por qué.
   5. Guardá como WiFi_entorno_[apellido].xlsx.
Punto de control: Cada red tiene canal y seguridad registrados, la banda está documentada cuando puede verificarse y la recomendación distingue 2,4/5/6 GHz sin inferir la banda solo por el canal.
[[CAJA Desafío final (si terminás antes)]]
Investigá en el listado si alguna red aparece sin seguridad (abierta) y escribí en dos líneas qué riesgos implica conectarse a ella.
[[/CAJA]]

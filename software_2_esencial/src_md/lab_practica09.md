@@H1 Práctica 9 — Lectoras de CD, DVD y Blu-ray
Nombre y Apellido: _______________________________  Curso: ______  Fecha: ____ / ____ / ____
Competencia de la práctica: Calcular capacidades y tiempos de transferencia óptica y presentar la migración de un archivo institucional.
[[IMG L_image12.jpg|10.9]]
Figura 9.3 — Identificación de unidades y medios ópticos.
## Lo que necesitás saber
• Tiempo ≈ tamaño ÷ velocidad. Las velocidades 1x de cada formato están en la tabla de la clase.
• Una diapositiva bien armada comunica una propuesta técnica en un minuto.
## Actividades
Actividad 1 — Objetivo: Calcular en Excel cuántos discos exige un archivo dado y cuánto tarda su lectura.
[[CAJA Ejemplo — Modelo a reproducir]]
Datos: archivo institucional de 61 GB. Tabla: Formato | Capacidad por capa (GB) | Discos necesarios | Velocidad de lectura (MB/s) | Horas de lectura. Formatos: CD (0,7 GB; 7,8 MB/s), DVD (4,7 GB; 22,2 MB/s), Blu-ray (25 GB; 36 MB/s). Usá las capacidades en GB decimales (1 GB = 1.000 MB) en toda la planilla.
[[/CAJA]]
   1. Abrí Excel, cargá los encabezados y los tres formatos con sus datos; escribí «Archivo (GB)» en G1 y 61 en H1.
   2. En Discos necesarios usá =REDONDEAR.MAS($H$1/B2;0) y arrastrá.
   3. En Horas de lectura usá =$H$1*1000/D2/3600 y arrastrá.
   4. Dejá un decimal en las horas con el formato de número.
   5. Marcá con relleno verde el formato más razonable para leer el archivo.
Punto de control: Al modificar solo la celda H1, los discos y las horas de los tres formatos se recalculan sin editar ninguna fórmula.
Actividad 2 — Objetivo: Armar una diapositiva de propuesta de migración en PowerPoint.
[[CAJA Ejemplo — Modelo a reproducir]]
Una diapositiva: título «Migración del archivo óptico», tres viñetas (leer y verificar · migrar con estructura de carpetas · respaldar y controlar) y la tabla de discos pegada desde Excel.
[[/CAJA]]
   1. Abrí PowerPoint y elegí una presentación en blanco.
   2. Escribí el título del modelo en el marcador de título.
   3. Cargá las tres viñetas en el cuadro de contenido.
   4. En Excel, seleccioná tu tabla y copiala con Ctrl + C.
   5. En PowerPoint, pegala con Ctrl + V y acomodá su tamaño.
   6. Guardá como Migracion_[apellido].pptx.
Punto de control: La diapositiva tiene título, tres viñetas y la tabla de Excel visible y legible.
[[CAJA Desafío final (si terminás antes)]]
Agregá al pie de la diapositiva el tiempo total estimado del proyecto suponiendo verificación al doble del tiempo de lectura.
[[/CAJA]]

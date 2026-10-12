@@H1 Práctica 4 — Slots de expansión
Nombre y Apellido: _______________________________  Curso: ______  Fecha: ____ / ____ / ____
Competencia de la práctica: Relevar las ranuras de expansión del equipo y construir un cuadro comparativo de velocidades en Excel.
Para esta práctica, tené a mano las Figuras 4.1 y 4.2 de la Clase 4.
## Lo que necesitás saber
• dxdiag informa el dispositivo de video actual; el Administrador de dispositivos muestra las tarjetas presentes.
• El ancho de banda depende de dos datos: generación PCIe y cantidad de carriles activos. El tamaño físico de la ranura no basta para conocerlos.
## Actividades
Actividad 1 — Objetivo: Identificar qué tarjetas de expansión reconoce el equipo.
[[CAJA Ejemplo — Modelo a reproducir]]
Datos a registrar: nombre del adaptador de pantalla y del adaptador de red.
[[/CAJA]]
   1. Presioná Windows + R, escribí dxdiag y presioná Enter.
   2. En la pestaña Pantalla, leé el Nombre del dispositivo y anotalo.
   3. Cerrá dxdiag, abrí el Administrador de dispositivos (clic derecho en Inicio).
   4. En Adaptadores de red anotá el nombre del adaptador principal.
Punto de control: Tenés anotados el adaptador de pantalla y el de red del equipo.
Actividad 2 — Objetivo: Calcular en Excel el ancho de banda aproximado de enlaces PCIe 3.0 y 5.0 con distinto número de carriles.
[[CAJA Ejemplo — Modelo a reproducir]]
Tabla: Ranura | Carriles | Total PCIe 3.0 (≈ 1 GB/s por carril) | Total PCIe 5.0 (≈ 4 GB/s por carril). Filas: x1 (1), x2 (2), x8 (8), x16 (16).
[[/CAJA]]
   1. Abrí Excel y cargá los encabezados del modelo en la fila 1.
   2. Completá las columnas Ranura y Carriles; en F1 y F2 escribí los valores por carril de cada generación (1 y 4).
   3. En C2 escribí =B2*$F$1 y en D2 =B2*$F$2; presioná Enter.
   4. Arrastrá el relleno de C2:D2 hasta la fila 5.
   5. Insertá un gráfico: seleccioná A1:A5 y C1:D5 (con Ctrl), andá a Insertar → Gráficos → Columna agrupada.
   6. Guardá como Slots_PCIe_[apellido].xlsx.
Punto de control: Las dos columnas de totales se calculan con fórmula a partir de las celdas F1 y F2, y el gráfico muestra las dos generaciones lado a lado.
[[CAJA Desafío final (si terminás antes)]]
Agregá una columna para PCIe 4.0 (≈ 2 GB/s por carril) y escribí debajo qué generación necesitaría la mitad de carriles que PCIe 3.0 para el mismo ancho de banda.
[[/CAJA]]

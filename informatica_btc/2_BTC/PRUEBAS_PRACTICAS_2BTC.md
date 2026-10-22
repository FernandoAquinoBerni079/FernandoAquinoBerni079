# Pruebas prácticas en software · Informática 2.º BTC (R3)

Ninguna de estas pruebas se hizo en esta revisión. Son las que hay que hacer en el laboratorio de la institución
antes de liberar el material. Cada prueba la hace un docente o un revisor siguiendo el Cuaderno de Laboratorio R3 tal
como está impreso, sin conocimientos previos del caso.

## Datos que se registran en cada prueba

- Fecha y persona que prueba.
- Sistema operativo.
- Programa, versión e idioma de la interfaz (por ejemplo, «LibreOffice Calc 24.8, español»).
- Separador de argumentos: punto y coma o coma.
- Tiempo real usado, en minutos.
- Resultado: **Pasa**, **Pasa con adaptación** (anotar cuál) o **Falla** (anotar el paso y el mensaje).

## Programas requeridos

| Bloque | Programa | Prácticas |
|---|---|---|
| Planillas | Una planilla electrónica: LibreOffice Calc o Microsoft Excel (probar las dos si la institución no definió cuál) | 1-10, 15-18, 20 (desafío) |
| Diseño vectorial | Un editor vectorial: Inkscape o CorelDRAW | 11-14 |
| Portal | Navegador actualizado con acceso a `dnit.gov.py` | 19-20 |
| Impresión | Impresora de la institución, papel oficio y A4 | 6, 10, 14 |

## Pruebas

### Planillas

| P | Procedimiento a probar | Resultado esperado (punto de control) | Evidencia |
|---|---|---|---|
| 1 | Crear `Honorarios_Arandu_2026`, renombrar la hoja y agregar tres hojas | Cuatro hojas en orden Honorarios · Sueldos · Egresos · Resultado; fila 1 con Cliente · Régimen · Honorario | Captura de las pestañas y de la fila 1; archivo guardado |
| 2 | Cargar 16 clientes y aplicar `=ESNUMERO(C2)` hasta H17 | 16 VERDADERO en H2:H17 | Captura de H2:H17 |
| 3 | Formato de miles sin decimales; encabezado y fila de total | 450.000 / 900.000 / 1.800.000 con punto de miles y sin ### | Captura de la hoja |
| 4 | `=SUMA(C2:C17)` en C18 y `=C18*12` en C20; cambiar un honorario a 500.000 y restaurar | C18 = 12.150.000; C20 = 145.800.000; recálculo automático | Capturas antes, durante y después del cambio |
| 5 | Hoja Sueldos con `=B2*$G$1`, `=B2-C2`, `=B2*$G$2`; copiar la fila; `=HOY()`, `=AHORA()`, `=K4-J4` con formato [HH]:MM | 306.000 + 3.094.000 = 3.400.000; patronal 561.000; duración 01:30 | Captura con fórmulas visibles (Ver → Mostrar fórmulas) |
| 6 | Inmovilizar la fila 1; encabezado y pie; vista previa | Fila 1 fija al desplazarse; vista previa con encabezado y número de página | Captura de la vista previa y, si se imprime, la hoja impresa |
| 7 | SUMA, PROMEDIO, MAX, MIN, CONTAR sobre C2:C17 | 12.150.000 · 759.375 · 1.800.000 · 450.000 · 16 | Captura de las cinco celdas |
| 8 | Subtotales por régimen; gráfico de columnas y circular | Circular ≈ 33,3 % · 37,0 % · 29,6 %; control 12.150.000 | Captura de ambos gráficos con rótulos |
| 9 | Ordenar por honorario y por cliente; seleccionar A1:C17 **sin la fila 18** y activar el autofiltro | SIMPLE: 5 filas; RESIMPLE: 9; sin filtro: 16. La fila de total no se oculta | Capturas de los dos filtros. Comprobar la corrección H-2-09 en Calc y en Excel |
| 10 | Hoja Egresos y hoja Resultado vinculadas; dos gráficos; área de impresión A1:O22 horizontal; cambiar el alquiler a 2.300.000 | 145.800.000 − 91.800.000 = 54.000.000; egresos mensuales 7.650.000; con el alquiler nuevo, 51.600.000 | PDF exportado del informe; hoja impresa para comprobar que las cifras de los gráficos se leen |
| 15 | Tres reglas de formato condicional sobre C2:C17; cambiar 10 → 45 | Verde → rojo sin tocar el formato | Captura antes y después |
| 16 | `=SI(C2>=1800000;"GENERAL";SI(C2>=900000;"SIMPLE";"RESIMPLE"))` en D2:D17; CONTAR.SI | D coincide con B en las 16 filas; 9 · 5 · 2. Si el programa usa coma, la fórmula con `;` debe adaptarse: anotarlo | Captura de B y D lado a lado y de los tres CONTAR.SI |
| 17 | Tabla dinámica (Régimen en filas, Suma de Honorario) y gráfico dinámico; cambiar Régimen por Cliente | RESIMPLE 4.050.000 · SIMPLE 4.500.000 · GENERAL 3.600.000 · Total 12.150.000 | Captura de la tabla y del gráfico |
| 18 | Nombre de rango «Honorarios»; desbloquear C2:C17; proteger la hoja; vincular un libro externo `Resumen_Arandu` | `=SUMA(Honorarios)` = 12.150.000; C5 editable y C18 bloqueada; Resultado!B4 = 4.500.000; el libro externo muestra 54.000.000 después de cerrar y reabrir | Captura del aviso de protección y del vínculo externo actualizado. Anotar la sintaxis de la referencia externa en cada programa |
| 20 (desafío) | Tabla de las 20 prácticas con formato condicional | Las prácticas marcadas cambian de color | Captura |

### Diseño vectorial

| P | Procedimiento a probar | Resultado esperado | Evidencia |
|---|---|---|---|
| 11 | Páginas A4 vertical, 90 × 50 mm y 2000 × 800 mm horizontal; rectángulo guía en cada una | Tres archivos con su tamaño de página. Comprobar que el editor acepta 2000 × 800 mm o anotar el límite | Captura de las propiedades de página de cada archivo |
| 12 | Tarjeta con relleno, texto artístico, texto de párrafo y línea | Cuatro objetos, dos tipografías como máximo, texto dentro del marco | Captura con el panel de objetos o capas visible |
| 13 | Rectángulo → curvas; agregar dos nodos; escalar con y sin bloqueo de proporciones; Descombinar o Separar subtrazados | Seis nodos o más; proporción conservada con el bloqueo. Anotar el nombre real del comando en el editor usado | Captura con la herramienta de nodos activa |
| 14 | Alinear y distribuir; agrupar; soldar o unir; exportar tres PDF y un PNG transparente | Tres PDF con las medidas correctas al abrirlos fuera del editor; PNG con fondo transparente; el grupo conserva dos objetos y la unión es una sola geometría | Los cuatro archivos exportados y las propiedades del PDF en un lector |

### Portal DNIT

| P | Procedimiento a probar | Resultado esperado | Evidencia |
|---|---|---|---|
| 19 | Recorrer `dnit.gov.py` según los pasos 1-7, sin ingresar a Marangatú | Las secciones nombradas existen (consultas sin clave, vencimientos, Marangatú, normativa, sistemas). Si alguna cambió de nombre, anotar el nombre actual para corregir el cuaderno | Capturas fechadas de cada sección |
| 20 | Localizar facturación electrónica, e-Kuatia y e-Kuatia'i, cronograma vigente e imagen de un KuDE | Existe material sobre los dos sistemas y el cronograma. El KuDE de ejemplo muestra el CDC y el QR | Capturas fechadas y URL de cada página |

## Prueba de impresión

Imprimir en la impresora de la institución:
- el tomo, páginas 5-10;
- el laboratorio completo;
- una página de cada plan de clase;
- el plan anual en oficio apaisado.

Verificar:
- que se lea todo el texto de las figuras a distancia normal de lectura (el más chico mide 7 pt);
- que los renglones de respuesta sean suficientes para escribir a mano;
- que los márgenes alcancen para el anillado.

Evidencia: fotografías de las páginas impresas y la lista de páginas con problemas.

## Prueba en Word

Abrir los cinco DOCX R3 en Microsoft Word en Windows y verificar:
- que la paginación coincida con los PDF de revisión (tomo 75 páginas);
- que las entradas del índice coincidan con las páginas reales;
- que ninguna figura salte de página dejando huecos.

Evidencia: la lista de diferencias de página.

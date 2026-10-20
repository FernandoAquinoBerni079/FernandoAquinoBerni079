# Transición de la colección al formato oficio — especificación

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · 20 de octubre de 2026**

**Estado:** especificación para aprobar.
- No se modificó ningún original en A4.
- No se produjo todavía ninguna versión oficio entregable: la prueba de este documento es de factibilidad y sus archivos no se guardan.

## 1. Medidas propuestas

Se propone el mismo perfil que ya usa la colección en Algorítmica 3.º. Las medidas se comprobaron en los DOCX y PDF de `algoritmica_3_esencial/salida_FINAL_OFICIO_v3/`: libro, solucionario, plan anual y planes de clase.

| Elemento | Medida |
|---|---|
| Papel | **Oficio, 21,59 × 33,02 cm** (8½ × 13 pulgadas), vertical |
| Márgenes | **1,27 cm** en los cuatro lados («Estrecho» de Word) |
| Ancho útil | 19,05 cm |
| Encabezado y pie | A 0,6 cm del borde (a fijar en la maqueta) |
| Tablas | Al 100 % del ancho útil, con las proporciones de columnas actuales |
| Figuras | Ancho de impresión igual al del lienzo, como hoy. Las figuras actuales (hasta 15,5 cm) entran sin escalar. |
| Plan anual | Oficio. Algorítmica 3.º lo hace vertical. La orientación horizontal de otras colecciones (por ejemplo, Historia y Geografía 7.º) queda a decidir. |

**Variante conservadora (B2), para comparar:** oficio con los márgenes actuales (2,2 cm a los lados y 2,0 cm arriba y abajo) y un ancho útil de 17,19 cm.

## 2. Prueba de factibilidad sobre el lote 1

**Qué se hizo:**
- **Sin tocar los originales:** se tomaron copias de `ADS_3BTI_LOTE1_ESTUDIANTE.docx` y `ADS_3BTI_LOTE1_GUIA_DOCENTE.docx` (commit `cdc96a6`).
- **Variante A:** solo se cambió el papel.
- **Variante B:** se cambiaron el papel y los márgenes, y las columnas de las tablas se escalaron al nuevo ancho.
- **Renderizado:** LibreOffice con Carlito.

El script está en `prueba_factibilidad/a_oficio_prueba.py`.

| Documento | A4 (original) | Oficio A: márgenes actuales | Oficio B: márgenes de 1,27 cm |
|---|---:|---:|---:|
| Libro del estudiante | 56 págs. | 51 págs. | 46 págs. |
| Guía docente | 19 págs. | 17 págs. | 14 págs. |
| Hojas en blanco | 0 | 0 | 0 |
| Ancho máximo de figura | 15,5 cm | 15,5 cm (entra) | 15,5 cm (entra) |
| Índice estático | Correcto (9/9) | **Desfasado (8/9)** | **Desfasado (8/9)** |

**Lectura:**
- El cambio es viable: no aparecen hojas en blanco y las figuras entran.
- **El índice estático del libro no sirve después de convertir el DOCX.** La versión oficio no puede salir de una conversión: tiene que reconstruirse con el constructor, que calcula el índice sobre el PDF real.
- Las hojas con menos de la mitad ocupada cambian de lugar: son finales de sección antes de una página nueva. La versión reconstruida tiene que revisarlas de nuevo con el bloque H del verificador.

## 3. Procedimiento de la transición

1. **Fernando aprueba las medidas** del §1, o la variante B2.
2. **Se parametriza la maqueta.** `helpers.py` y `maqueta.py` toman papel, márgenes y ancho útil de un perfil (`A4`, `OFICIO`). Las anchuras de tabla se escriben en proporciones; hoy son centímetros que suman 16,6.
3. **Se ajusta el verificador del lote 1.**
   - El control G hoy exige que `helpers.py` y `maqueta.py` sean idénticos a los del Capítulo 4 v2.1. Pasa a comparar contra la maqueta parametrizada de la colección.
   - El control H se recalcula con el perfil oficio.
   - Los demás bloques no cambian.
4. **Se reconstruye el lote 1 en oficio** en una carpeta nueva, `lote_1_oficio/`, con nombres nuevos (`ADS_3BTI_LOTE1_..._OFICIO`). La carpeta `lote_1/` no se toca.
5. **Se comprueba:**
   - el mismo texto que la versión A4, palabra por palabra, salvo los números de página;
   - índice correcto;
   - tablas con todas sus filas y su encabezado repetido;
   - figuras al tamaño de su lienzo;
   - prácticas y evaluaciones en página propia;
   - ninguna hoja en blanco y ningún renglón suelto;
   - prueba con tres fuentes de sustitución.
6. **Se arma el informe y el manifiesto,** con las huellas de las dos versiones.
7. **Desde el lote 2,** todo se construye directamente en oficio.

## 4. Pendientes

- Confirmar si el plan anual va en oficio vertical (como Algorítmica 3.º) u horizontal.
- La prueba se hizo con Carlito, porque Calibri no está en el entorno. En Word, la paginación puede variar levemente, como ya advierte el informe del lote 1.

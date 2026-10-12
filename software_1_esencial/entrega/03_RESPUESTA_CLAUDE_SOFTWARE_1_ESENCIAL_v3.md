# 03_RESPUESTA_CLAUDE_SOFTWARE_1_ESENCIAL_v3

**Respuesta del constructor: pasada v3 autorizada por Fer el 12/10/2026** · Protocolo v0.4, §3, paso 5

Gabinete de Informática – Software · 1.er Curso BTI · Edición Esencial · versión corregida **v3**

**Estado: corregido — vuelve a ChatGPT para la auditoría de cierre.** No se declara listo para la venta.

**Base:**
- Matriz `06_CONCILIACION_AUDITORIAS_SOFTWARE_1_ESENCIAL_v2.md`, que concilia `02_AUDITORIA_CHATGPT_SOFTWARE_1_ESENCIAL_v2` (maquetación) y `04_AUDITORIA_CHATGPT_SOFTWARE_1_ESENCIAL_v2` (exhaustiva).
- Versión de comparación: commit `558a335` (v2).

## 1. Qué se hizo

| N.º | Gravedad | Qué se hizo |
|---|---|---|
| **H02** | MAYOR | Filas 18 y 36 del Plan Anual. Detalle debajo de la tabla. |
| **H15** | MAYOR | Se quitaron del texto **77 pictogramas**: 56 en el Libro (46 «✅» y 10 «✓») y 21 «✓» en el Solucionario. La Muestra se rearmó a partir del Libro corregido, así que también quedó en 0. Detalle debajo de la tabla. |
| H18 | MAYOR | Se cerró junto con H15: la Muestra ya no tiene ningún pictograma ni páginas de continuación. |

**H02 en detalle:**
- **Cambio en el texto.** Las remisiones «Todas las capacidades… transcriptas en las secuencias…» se reemplazaron por las capacidades MEC **literales**, con el mismo formato que las demás filas (cursiva, entre comillas, debajo de «Capacidad MEC:»):
  - fila 18: las **7** de la Unidad 1;
  - fila 36: las **13** de las Unidades 2 y 3.

  Los textos coinciden con el Anexo B del informe exhaustivo y con el programa MEC (págs. 59–63).
- **Paginación.** Las dos filas son ahora más largas. Para no dejar media hoja en blanco antes de ellas, se les permite partirse entre hojas; el encabezado de la tabla se repite en cada hoja. No se redujo la letra ni se quitó contenido.
- **Resultado:**
  - El Plan Anual pasa de **10 a 11 páginas**. Es un aumento legítimo por el texto agregado.
  - Ninguna hoja queda casi vacía: la ocupación de las hojas 2 a 11 va del 69 % al 93 %.
  - La última hoja tiene el final de la fila 36, los criterios generales, las estrategias de inclusión y la firma.

**H15 en detalle:**
- **Qué se quitó:**
  - «✅ Punto de control: …» pasa a «Punto de control: …».
  - Las verificaciones terminan sin el signo: «Verificación: 64+8+4+2 = 78.».

  Se conservan los rótulos «Punto de control» y «Verificación», y todos los enunciados, procedimientos y resultados.
- **Lo que no se tocó:** ninguna imagen. Las 28 del Libro son idénticas byte a byte a las de la v2.
- **Paginación y muestra:** el Libro sigue en 107 páginas y el Solucionario en 17, con el mismo texto en cada página. Se regeneró la Muestra.

## 2. Controles

**Controles automáticos (registro completo en `build/auditoria_resultado.txt`):**

| Control | Resultado |
|---|---|
| `build/control_v3.py`, contra el commit `558a335` | **657 OK · 0 fallos** |
| `build/auditoria_v1.py` (contenido) | **117 OK · 0 fallos** |
| Índices contra el PDF (`build/tocchk.py`) | Libro 61/61, Solucionario 65/65, Planes 36/36 |

| Requisito de Fer | Cómo se verificó | Resultado |
|---|---|---|
| 1. Identidad de contenido salvo H02 y H15 | Párrafo por párrafo contra `558a335`, en los cuatro .docx | Libro y Solucionario: solo cambian los pictogramas. Planes: idéntico. Plan Anual: solo las filas 18 y 36 (390 → 408 párrafos, +20 capacidades, −2 remisiones). |
| 2. Las 20 capacidades MEC | Texto literal en Libro, Plan Anual y Planes; las 36 filas del Plan Anual con todas sus capacidades y sin remisiones | Correcto |
| 3. Coincidencia Libro–Solucionario | Mismo texto que la v2 en ambos, salvo los pictogramas. Más los controles de claves y cálculos de `auditoria_v1.py`. | Correcto |
| 4. Índices y páginas | Comparación del índice con el PDF | Coinciden todas las entradas |
| 5. Integridad de imágenes | Hash de cada archivo de `word/media/` en los cuatro .docx contra la v2 | Idénticas (Libro: 28) |
| 6. Sin tablas cortadas, hojas vacías ni texto fuera de margen | Ocupación de cada página y distancia al borde (texto a 1 cm o más). Revisión ocular de las hojas del Plan Anual y de las líneas corregidas del Libro y el Solucionario. | Correcto, con la salvedad de la nota de abajo |
| 7. Planes: 36 completos, uno por hoja | Sin cambios en la v3; las págs. 3–38 abren los planes 1–36 con sus firmas | Correcto |
| 8. Muestra sin claves ni fragmentos | 13 páginas, cada una idéntica en imagen a su página de origen (Libro 1–4, 6–10 y 107, Solucionario 1, Planes 1 y 3). Sin «Opción correcta», «Resultado esperado», «Orientación:» ni «continuación». | Correcto |
| 9. Paginación final | Libro 107 · Solucionario 17 · Plan Anual 11 · Planes 38 · Muestra 13 | Todo en oficio; Plan Anual en oficio horizontal |
| Pictogramas en 0 | Recuento de ✓ ✗ ✅ ✔ en los cuatro .docx y los cinco PDF | **0** en todos |

**Nota:** la pág. 2 del Solucionario («Presentación», dos párrafos) ocupa menos del 20 % de la hoja. Es un preliminar que está así desde la v1 y no lo señaló ninguna auditoría. Se dejó como está porque cambiarlo excede esta pasada. Si Fer quiere, puede compartir hoja con el índice en una pasada futura.

**Ajustes en los scripts de control:**
- `auditoria_v1.py`: dos cadenas esperadas incluían el «✓»; se actualizaron sin el signo.
- `tocchk.py`: ahora reconoce el título «EVALUACIÓN INTEGRADORA · 1.ª/2.ª ETAPA». Antes daba 2 falsas diferencias en el Libro, que el informe exhaustivo había notado.
- `control_v2.py` queda como histórico de la v2.

Estos controles son internos del constructor y **no reemplazan la auditoría independiente de ChatGPT**.

## 3. Fuera de esta pasada (decisión de Fer)

- **V2-03:** portada y contraportada del Libro, intactas.
- **H14 / V2-04:** nota vieja en Drive (`_TRABAJO/03_NOTAS_PILOTO…v1`).
- **H19:** subida a Drive con verificación de hashes desde el commit de esta versión. No se movió ni se reemplazó nada en Drive.
- **Imágenes con signos dibujados:** el recuento cubre solo el texto. Si alguna figura del Libro tuviera un «✓» dibujado, queda para la decisión de Fer, como se hizo con la Figura 9.1 de Algorítmica 3.º.

# Lote 1 en oficio — versión de PRUEBA

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · 20 de octubre de 2026**

**Estado:** versión de prueba para auditoría independiente.
- **No es la conversión definitiva** ni una versión aprobada. La aprobación es de Fernando.
- Los maestros A4 de `lote_1/` (commit `cdc96a6`) **no se modificaron**: se comprobó con el SHA-256 de sus 31 archivos antes y después.

**Autorización:** decisión de Fernando del 20 de octubre de 2026.
- Papel oficio de 21,59 × 33,02 cm, vertical.
- Comparar el margen de 1,27 cm con variantes de margen interior ampliado para encuadernación, sin optimizar solo por la cantidad de páginas.
- Reconstruir desde las fuentes, con índices actualizados y controles.

## 1. Cómo se hizo

`build/construir_oficio.py` importa los módulos de `lote_1/build/` tal como están: contenido de los capítulos, caso, maqueta, constructor y guía. Cambia solo la geometría:

| Qué cambia | Cómo |
|---|---|
| Página | Oficio y márgenes del perfil (§2). En O2 y O3, márgenes espejados para impresión a doble cara. |
| Tablas de varias columnas | Anchos escalados en proporción al ancho útil del perfil. Las fuentes los escriben para 16,6 cm. |
| Índice | Se recalcula sobre el PDF real con el mismo bucle del constructor original, y su tabulación derecha pasa al nuevo ancho |
| Figuras | Se regeneran con el mismo código (en `build/figs/`) y se imprimen al mismo tamaño en cm. Se comprobó que tienen el mismo tamaño en píxeles que las originales. |
| Portada | La línea de versión agrega «· prueba en oficio Ox, no definitiva». Es la **única diferencia de texto intencional**. |
| Párrafo vacío después de una tabla | Se quita cuando lo sigue un título que abre hoja o el final del documento. Si no, pasaba solo a la hoja siguiente y dejaba **una hoja en blanco** (se vio en la guía con O2 y O3). |
| Tablas con celdas no impresas | Ver §4. El rótulo de la tabla afectada pasa a abrir hoja nueva y el documento se reconstruye. |

**Reconstrucción:**

```
python3 lote_1_oficio/build/construir_oficio.py O1|O2|O3
python3 lote_1_oficio/build/verificar_oficio.py O1|O2|O3
python3 lote_1_oficio/build/docx_vs_pdf.py
python3 lote_1_oficio/build/comparar.py
```

## 2. Perfiles comparados

| Perfil | Márgenes | Ancho útil | Libro | Guía | Caracteres por renglón de texto (mediana / máximo) |
|---|---|---:|---:|---:|---|
| A4 original (referencia) | 2,2 cm a los lados; 2,0 cm arriba y abajo | 16,60 cm | 56 págs. | 19 págs. | 104 / 121 |
| **O1** | 1,27 cm en los cuatro lados (perfil de Algorítmica 3.º) | 19,05 cm | 46 | 14 | 114 / 137 |
| **O2** | Espejados: interior 2,0 cm; exterior, superior e inferior 1,27 cm | 18,32 cm | 48 | 14 | 113 / 134 |
| **O3** | Espejados: interior 2,5 cm, exterior 1,8 cm, superior e inferior 1,5 cm | 17,29 cm | 49 | 14 | 107 / 126 |

**Márgenes medidos en el PDF** (texto de las págs. 10 a 13):
- **O2:** interior de 2,0 cm a la izquierda en las impares y a la derecha en las pares.
- **O3:** lo mismo, con 2,5 cm de interior.

El espejado funciona: el margen ancho queda siempre del lado del lomo.

**Lectura de la comparación:**
- **O1** es el que más ahorra, con 10 páginas menos que el A4. A cambio:
  - no deja margen para encuadernar: con anillado o abrochado, el texto queda pegado al lomo;
  - tiene el renglón más largo (mediana de 114 caracteres, máximo de 137). Ya en el A4 el renglón es largo para la lectura escolar.
- **O2** suma 2 páginas y protege el lomo, pero conserva el renglón largo.
- **O3** suma 3 páginas sobre O1:
  - protege el lomo (2,5 cm);
  - deja un exterior de 1,8 cm para tomar el libro sin tapar el texto;
  - mantiene el largo de renglón del A4 (107 frente a 104 caracteres).

**Recomendación: O3** para el libro y la guía. La decisión es de Fernando.
- **Si se prioriza la cantidad de páginas,** O2 es la alternativa intermedia.
- **Los márgenes espejados suponen impresión a doble cara.** Si se imprime a una sola cara, el interior siempre queda a la izquierda.

## 3. Controles

| Control | O1 | O2 | O3 |
|---|---|---|---|
| Verificador del lote 1 (bloques A a J) con las sustituciones declaradas (§3.1) | 118 correctos, 0 fallos | 118, 0 | 118, 0 |
| Texto del DOCX idéntico al A4, párrafo por párrafo y celda por celda (salvo índice y versión) | Idéntico (1721 párrafos con texto en el libro) | Idéntico | Idéntico |
| Párrafos del DOCX que no aparecen impresos en el PDF (control nuevo, §4) | 0 en libro y guía | 0 y 0 | 0 y 0 |
| Figuras del mismo tamaño que las originales | Sí | Sí | Sí |
| Tablas que abren hoja nueva para no perder filas | Ninguna | «Destino de los 31 elementos del candidato» (guía) | Ninguna |

### 3.1 Sustituciones del verificador

`build/verificar_oficio.py` ejecuta el verificador del lote 1 sin modificarlo en disco. Solo cambia esto, y cada cambio tiene que aplicarse exactamente una vez:
1. las rutas del libro, de la guía y del resultado de construcción;
2. el ancho esperado de las tablas: 16,6 cm (9411 twips) pasa al ancho útil del perfil;
3. los rangos de extensión del plan (libro 51 a 65 págs.; guía 18 a 22), escalados por la razón entre el área útil del A4 y la del perfil;
4. el archivo de resultado.

El control G sigue exigiendo que `helpers.py` y `maqueta.py` sean idénticos a los del Capítulo 4 v2.1, y lo son.

## 4. Hallazgo para la auditoría: el PDF A4 del lote 1 no imprime 6 filas de la Tabla 3.5

**Qué falta.** En `ADS_3BTI_LOTE1_ESTUDIANTE.pdf` (A4, commit `cdc96a6`), la **Tabla 3.5, «Alcance mínimo del proyecto (núcleo)»**, muestra el encabezado y la fila «Catálogo y ejemplares» al pie de la página 46. **Las 6 filas siguientes no aparecen en ninguna página:** Lectores, Préstamo, Devolución, Consultas, Permisos mínimos, y Persistencia y entrega. El DOCX sí las tiene.

**Por qué no se detectó.** El verificador del lote 1 controla el texto del DOCX, no lo que se imprime.

**Causa** (reproducida sobre copias):
- es la combinación de **encabezado repetido** y **«no dividir fila»**: cuando la tabla empieza cerca del pie, LibreOffice imprime el encabezado y la primera fila y omite el resto;
- quitando cualquiera de las dos propiedades, o haciendo que la tabla empiece en hoja nueva, se imprimen las 14 celdas;
- con el perfil O2 pasó lo mismo con otra tabla de la guía, la de los 31 elementos: le faltaban 63 de sus 94 celdas.

**Tratamiento en esta prueba:**
- **Control nuevo** (`build/docx_vs_pdf.py`): todo párrafo del DOCX de 12 caracteres o más tiene que aparecer en el PDF. Se busca en trozos de 12 caracteres sin espacios, lo que tolera cortes de renglón y celdas que se extraen intercaladas.
- **Corrección en el constructor:** después de cada construcción se mide el déficit de palabras de cada tabla con encabezado repetido. La tabla con mayor déficit pasa a abrir hoja nueva, sin quitarle ninguna de las dos propiedades, y se reconstruye. Se repite hasta que no falta nada.
- **Resultado:** en las seis versiones en oficio, **0 párrafos sin imprimir**.

**En el A4 no se corrigió nada,** por la indicación de no modificar los maestros. Para el A4 hay que decidir una de dos:
1. regenerarlo con este control;
2. darlo por reemplazado por la versión oficio cuando se apruebe.

El control y la corrección deben incorporarse a la maqueta canónica de la colección.

## 5. Observaciones menores

- **Palabras partidas sin guion en celdas angostas.** En columnas de menos de 2 cm, LibreOffice corta palabras largas a mitad de palabra: «Programació|n», «Comunicació|n», «Fragment|o». Ya pasa en el A4 (guía, págs. 2 y 3). Afecta a 1 a 3 palabras por documento. Se corrige ensanchando esas columnas en la versión definitiva.
- **Hojas con menos de la mitad ocupada.** Son finales de sección antes de una página que abre (práctica, evaluación, capítulo):
  - libro: 10 en O1, 11 en O2 y 11 en O3, contando la portada;
  - A4: 8, sin contar la portada.
  
  Ninguna está en blanco; el bloque H del verificador las admite. Conviene revisarlas a la vista en la auditoría.
- **Tipografía.** El renderizado se hizo con Carlito, que tiene las métricas de Calibri, como en el lote 1. En Word la paginación puede variar levemente.

## 6. Archivos

| Carpeta | Contenido |
|---|---|
| `O1/`, `O2/`, `O3/` | `ADS_3BTI_LOTE1_ESTUDIANTE_OFICIO_Ox` y `ADS_3BTI_LOTE1_GUIA_DOCENTE_OFICIO_Ox` (DOCX y PDF), `resultado_construccion.json`, `verificacion_resultado.txt` y `.json` |
| `build/` | `perfiles.py`, `construir_oficio.py`, `verificar_oficio.py`, `docx_vs_pdf.py`, `comparar.py` y las figuras regeneradas |
| Raíz | `COMPARACION.json` (identidad de texto y medidas de lectura), `DOCX_VS_PDF.json` (impresión completa) y `MANIFIESTO_PRUEBA_OFICIO.json` (SHA-256 de todo, incluidos los cuatro originales A4 de referencia) |

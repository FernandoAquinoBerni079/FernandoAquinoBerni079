# Ronda de correcciones DPS-01 a DPS-04 — Dictamen de auditoría del 14/10/2026

Estado: **candidatas para reauditoría puntual de ChatGPT.** No están aprobadas para la venta. La aprobación comercial corresponde a Fernando.

## 1. Alcance

Se modificaron **solo 5 documentos**: los tres Planes Anuales y los Planes de Clase de 7.º y 8.º.

- Los otros 13 entregables quedan **idénticos byte a byte** a los auditados: los tomos DOCX y PDF, los solucionarios DOCX y PDF, y los Planes de Clase de 9.º.
- Los auditados son los de `faa8ef9` para 7.º y 8.º, y los de `bd1512c` para 9.º.
- No se tocaron capacidades, indicadores, numeración, talleres PEC ni imágenes.

| Documento | SHA-256 auditado | SHA-256 nuevo | Bytes |
|---|---|---|---|
| `7mo/DPS_7mo_PLAN_ANUAL_PEC_OFICIO_2026.docx` | `7a5a153f4b652b904c7a225b8e4ae9c84b08b9b2884ae62f006a9a830914f596` | `d340a13a5f6913bfa3b703f43f982b62180347f12af4e92672690e682b5933ec` | 182254 |
| `7mo/DPS_7mo_PLANES_DE_CLASE_PEC_OFICIO_2026.docx` | `36e109a303149634c97e87419ccf80d89a937a02aba61ff670edba5d1166fd14` | `2d9f5118d97f7df132124fd4878cd0c4362d1b05952bb20205c42562d341e0bc` | 218615 |
| `8vo/DPS_8vo_PLAN_ANUAL_PEC_OFICIO_2026.docx` | `7dc6578c6c11dde8adccae76f4ea81b2d9380e70bc49efe872360cc08c0a3633` | `b0d630b811e140833fd14a376ec531aa7d8679f36f703bd2ffa0daf6e25ba43d` | 181850 |
| `8vo/DPS_8vo_PLANES_DE_CLASE_PEC_OFICIO_2026.docx` | `fcba85f9019f0bf28c6340c6c64475c161b915d7ff935442b2e10b0b9adbb4e8` | `730735665e37662108e6c22600e2cc97ffbfbb2bb3fc30c523a016d720df9f24` | 279422 |
| `9no/DPS_9no_PLAN_ANUAL_PEC_OFICIO_2026.docx` | `1f6c4614c2b0fb3c226eb4267565abdfb91a4ec9e2aa18fecc95c9f421f42aa2` | `953999f751bb9e7a7f1128b398618966062442f3acccb8b23b33f9b2063e8905` | 181858 |

**Punto de partida comprobado.** Antes de aplicar los cambios se regeneraron los seis documentos de Plan Anual y Planes con el script vigente, y su texto resultó idéntico, párrafo por párrafo, al auditado. La ronda solo agrega los pasos de la sección 2. Están en `edicion/edit_docs.py` y se activan por grado en `edicion/config_grados.py` (`pa_flujo_continuo`, `planes_pagina_propia`, `planes_indice_nuevo`).

## 2. Correcciones

### DPS-01 — Plan Anual 7.º: filas partidas y página residual

- **Filas.** Todas las filas de todas las tablas llevan «no dividir fila entre páginas» (`cantSplit`). La fila de títulos de columnas se repite al pasar de página (`tblHeader`).
- **Unidades seguidas.** Se quitaron los 7 saltos de página manuales entre unidades. Eran los que dejaban páginas casi vacías: la 4, con solo el encuentro 5, y la 13, con solo el 35. El título de cada unidad (etapa y banda de capacidades) queda unido a su tabla para que no quede huérfano.
- **Tabla PEC.** La tabla de correspondencia de talleres va entera y unida a su párrafo de presentación.
- **Resultado en la renderización de control (LibreOffice):**

| | Páginas | Ocupación por página |
|---|---|---|
| Antes | 14 | 2 páginas casi vacías (23 % y 20 %) |
| Después | 10 | Todas entre 72 % y 94 % |

  Ninguna fila partida. La tabla PEC queda entera en la última página.

El auditor había contado 15 páginas antes; aquí salían 14. Pequeñas diferencias de fuentes entre instalaciones de LibreOffice pueden mover el corte, pero con filas no divisibles y sin saltos manuales el resultado no depende de eso.

### DPS-02 — Planes de Clase 8.º: Planes 26 y 32 partidos

- **Cambio.** Cada plan, del 2 al 36, empieza en página nueva. El plan 1 ya empezaba después del índice.
- **Causa del defecto.** Los Planes 25 y 31 son evaluaciones cortas, y los Planes 26 y 32 empezaban en la misma hoja, al pie.
- **Resultado:**
  - 39 páginas: portada, índice, los 36 planes uno por hoja (págs. 3 a 38) y la guía de articulación (pág. 39);
  - ningún plan empieza a mitad de página, comprobado en el PDF de control;
  - el índice se recalculó y sus 36 números coinciden con la página real de cada plan.

### DPS-03 — Planes Anuales 7.º, 8.º y 9.º: notación horaria

- La columna TIEMPO dice **«3 HC» en los 36 encuentros** de cada grado. Antes decía «3 h» en 30 filas.
- Antes de la tabla hay una sola nota: «En este esquema editorial, cada encuentro dura 3 HC (horas cátedra), que equivalen a 120 minutos; los 36 encuentros suman 108 HC.»
- La carga anual no cambia.

### DPS-04 — Índice de los Planes de Clase 7.º (mejora opcional)

- Se agregó un índice de los 36 planes en página propia (pág. 3), después de la portada interna, con el mismo formato que en 8.º y 9.º.
- Los planes siguen uno por hoja (págs. 4 a 39) y la guía queda en la pág. 40.
- Las 36 entradas coinciden con su página.
- No hubo regresiones: ningún plan cambió de contenido ni quedó partido.

## 3. Comprobaciones

Se agregaron controles automáticos en `edicion/verificar.py`:
- TIEMPO = «3 HC» en los 36 encuentros;
- presencia de la nota de 120 minutos;
- ninguna fila de Plan Anual divisible;
- el índice de los Planes de Clase contra la página real de cada plan.

| Grado | Controles correctos | Fallos |
|---|---|---|
| 7.º | 271 | 0 |
| 8.º | 362 | 0 |
| 9.º | 351 | 0 |

El cotejo literal de las 51 capacidades contra los programas MEC 2014 sigue en 0 fallos.

**Revisión visual.** Se renderizaron completos el Plan Anual de 7.º, los Planes de Clase de 7.º y 8.º y las páginas finales del Plan Anual de 9.º. Los PDF de control se usan solo para verificar y no se entregan, por indicación expresa: no hay PDF del Plan Anual ni de los Planes.

## 4. Encargo para la reauditoría puntual

> Reauditá solo estos cinco DOCX del commit indicado por Claude: los tres Planes Anuales y los Planes de Clase de 7.º y 8.º. Confirmá también que los otros 13 entregables conservan los SHA-256 auditados.
>
> Verificá en tu propia renderización:
> - DPS-01: ninguna fila partida ni página residual en el Plan Anual 7.º.
> - DPS-02: Planes 26 y 32 de 8.º en hoja propia, con el índice correcto.
> - DPS-03: «3 HC» en los 36 encuentros de los tres grados, más la nota.
> - DPS-04: índice de 7.º sin regresiones.

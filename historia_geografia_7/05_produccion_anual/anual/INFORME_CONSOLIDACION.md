# Informe de control — Paquete anual consolidado (36 encuentros)

**Estado: desarrollado, verificado automáticamente e inspeccionado visualmente. Pendiente de auditoría independiente (ChatGPT y Work). NO es apto comercialmente.** La aprobación final corresponde a Fernando.

Modelo: muestra 3, commit `841f5bc9`. Los commits de cada bloque y de sus correcciones están en `MANIFIESTO_VERSIONES.md`.

## 1. Paquete entregado

| Documento | Formato | Páginas |
|---|---|---:|
| `tomo/TOMO_ANUAL_oficio.docx` y `.pdf` | Oficio vertical | 155 |
| `planes/PLANES_ANUAL_A4.docx` y `.pdf` | A4 vertical | 74 |
| `solucionario/SOLUCIONARIO_ANUAL_A4.docx` y `.pdf` | A4 vertical | 40 |
| `plan_anual/PLAN_ANUAL_oficio.docx` y `.pdf` | Oficio horizontal | 6 |
| `matriz/MATRIZ_CURRICULAR_36_ENCUENTROS_A4.docx` y `.pdf` | A4 horizontal | 2 |
| `figuras/` | PNG a 300 ppp, dibujadas al tamaño de impresión | 58 |
| `revision_liviana/` | PDF livianos para revisión | — |
| `datos/` | Trazabilidad, páginas del tomo, controles por encuentro (`controles.json`) y de consolidación (`controles_consolidacion.json`) | — |

**Arquitectura:**
- 21 clases, 7 continuaciones, 6 evaluaciones de unidad y 2 integradoras.
- 3 horas cátedra de 40 minutos por encuentro: 120 minutos.

**Origen de los documentos:** todos se generan desde los mismos módulos `scripts/contenido/e01.py` a `e36.py` y `scripts/curriculo.py`. El plan anual y la matriz no copian la planificación del maestro.

**Para reconstruir:**
- `python3 scripts/construir_bloque.py anual MAESTRO GEO`
- `python3 scripts/verificar.py anual`
- `python3 scripts/anuales.py`

## 2. Controles automáticos

| Conjunto | Correctos | Fallos |
|---|---:|---:|
| Controles por encuentro sobre el volumen anual (`verificar.py anual`, 13 controles) | 6385 | 0 |
| Controles de consolidación (`anuales.py`, 8 controles) | 1031 | 0 |

### 2.1 Controles por encuentro (los 13 de cada bloque, aplicados a los 36)

Capacidades y temas literales; tomo ↔ solucionario; tomo ↔ planes; funciones; secuencias de 120 minutos; rúbricas, puntajes y matrices; claves; figuras; trazabilidad; equidad; integridad visual; voseo; numeración. El resultado detallado está en `datos/controles.json`.

**Claves de opción múltiple del año:** a 35, b 38, c 34, d 33.

### 2.2 Controles de consolidación (condición 6)

| Control | Qué comprueba | Correctos | Fallos |
|---|---|---:|---:|
| A. Arquitectura | 21/7/6/2 y secuencias que terminan en el minuto 120 | 37 | 0 |
| B. Continuidad de evaluaciones | Cada evaluación con tiempo adicional y cierre sin claves; el plan siguiente reserva 0-20 para la devolución | 15 | 0 |
| C. Repeticiones | Ningún ítem de una sección repite textualmente uno de otra (salvo la consigna genérica «Ordená del 1 al 6…») | 367 | 0 |
| D. Capacidades | Las clases cubren H1-H6 y G1-G4. La matriz de cada integradora coincide con sus capacidades y estas fueron enseñadas en la etapa | 3 | 0 |
| E. Guerra Guaranítica (A05) | Solo aparece en el recuadro «Ampliación optativa» del encuentro 22. Ninguna respuesta del solucionario la exige y no está en el tema ni en los indicadores del 22 | 503 | 0 |
| F. Figuras y cartografía | Todos los archivos existen y cada número de figura es único en el año | 103 | 0 |
| G. N01 | La Clase 18 no usa el Acuífero Patiño como uso de un río | 2 | 0 |
| H. Plan 31 | 0-20 devolución de la U5 y G3 desde el minuto 20 | 1 | 0 |

## 3. Condiciones del cierre

| N.º | Condición | Cumplimiento |
|---:|---|---|
| 1 | **Encuentro 22.** Versión centrada en el Guairá y Mbororé, con plan anual, matriz y JSON alineados. | El plan anual, la matriz y `datos/trazabilidad.json` leen el encuentro 22 del módulo `e22.py`: temas H5c y H5d con vínculo literal. La observación dice «Núcleo del siglo XVII… Ampliación optativa, no evaluada: Guerra Guaranítica». No se usó la planificación del maestro (control E). |
| 2 | **Fuentes históricas.** Conservar las referencias y diferenciar cita textual de paráfrasis. | Las referencias se conservan. Hay dos tipos de fragmentos de época: citas textuales entre comillas y versiones escolares resumidas declaradas. Las dos citas textuales son el fragmento 1 de la Real Provisión, de Rivarola Paoli, y la primera oración del art. 7 de la Constitución. Las versiones resumidas son las de Colón, Schmidl, el testamento de Irala, Alfaro, el Sínodo de 1603, Montoya, Santo Tomás y Equiano. El fragmento 2 de la Real Provisión es una adaptación declarada. **Pendiente:** verificar los resúmenes contra una edición antes de publicar (lista en §5). |
| 3 | **N01, encuentro 28.** | Cumplido (control G). El Acuífero Patiño queda solo en el apartado de aguas subterráneas. |
| 4 | **Encuentro 31.** 20 + 100 minutos y procedimiento para quien no rindió. | Cumplido (control H). Quien no rindió no participa de la devolución, lee la clase aparte y rinde después una versión alternativa equivalente. Nadie rinde mientras se revelan claves. |
| 5 | **Integradora final.** H5, H6 y G1-G4 enseñados, matriz y sin Guerra Guaranítica. | Cumplido (controles D y E). La matriz suma 28 puntos y cubre las seis capacidades. |
| 6 | **Consolidación anual.** | Ver §2.2 y §4. |
| 7 | **Trazabilidad de commits.** | Cada bloque y cada corrección tiene su commit; ninguno se reescribió. Ver `MANIFIESTO_VERSIONES.md`. |

## 4. Correcciones hechas durante la consolidación

**Repeticiones (control C).** Cinco ítems repetían textualmente actividades de clase y se reformularon:

| Encuentro | Ítem | Repetía | Cambio |
|---|---|---|---|
| 17 (Evaluación U3) | 3 | Clase 7 | Se reformuló; la clave no cambia. |
| 17 (Evaluación U3) | 8 | Clase 10 | Se reformuló; la respuesta sigue siendo «Falso» y se ajustó su justificación en el solucionario. |
| 25 (Evaluación U4) | 5 | Clase 15 (Quebec) | Pasa a Nueva Ámsterdam. Nueva clave: b. |
| 25 (Evaluación U4) | 8 | Clase 13 | Se reformuló y pasa a «Verdadero». |
| 28 (Clase 18) | 2 | Clase 2 | Se reformuló. |

**Maquetación del volumen anual:**
- El índice del tomo ocupa dos hojas. Se ajustaron la detección y la iteración de la paginación.
- El índice de los 36 planes se compactó.
- La matriz final del solucionario ya no deja filas sueltas.

**Bloques reconstruidos:** II, III y IV, con controles de nuevo en 0 fallos:

| Bloque | Correctos | Fallos |
|---|---:|---:|
| II | 1655 | 0 |
| III | 1539 | 0 |
| IV | 1702 | 0 |

## 5. Inspección visual

**Revisado página por página durante la producción de cada bloque:**
- tomo: 161 páginas;
- planes: 80 páginas;
- solucionario: 41 páginas;
- figuras: 58.

**Revisado del paquete anual:**
- la matriz y el plan anual, completos;
- las páginas del índice y las zonas de unión entre bloques.

**Observaciones menores que quedan:**
- **Hojas con espacio libre antes de un mapa grande:** págs. 32 y 34 del Bloque III. Superan el umbral del control.
- **Nombres de archivo de figuras:** algunos no siguen el número impreso de la figura (Bloques I y III). El número impreso es el correcto.
- **Plan anual:** es una tabla continua de 6 páginas, con encabezado repetido y bandas de etapa y de unidad.

## 6. Pendiente antes de una versión comercial (no es parte de esta entrega)

- **Auditorías:**
  - auditoría independiente de los cuatro bloques y del paquete anual (ChatGPT y Work);
  - aprobación de Fernando.
- **Verificaciones documentales:** la lista completa está en `datos/trazabilidad.json`, campo `pendientes_de_verificacion`. Las principales:
  - cotejo literal del fragmento 1 de la Real Provisión;
  - resúmenes de Colón, Schmidl, Irala, Alfaro, el Sínodo de 1603, Montoya (*Conquista espiritual*), Santo Tomás y Equiano;
  - leyes ambientales y fechas de creación del MADES y de la SEAM;
  - coordenadas y alturas del Paraguay;
  - valores de lluvia;
  - ecorregiones oficiales del MADES;
  - Roulet sobre Tabaré.
- **Pruebas materiales:**
  - prueba física de impresión o fotocopia, sobre todo de los mapas y de las fichas reproducibles;
  - validación de los tiempos en aula.
- **Cotejo del programa:** con la edición oficial del MEC 2014. Se trabajó sobre una reproducción identificada por su SHA-256.

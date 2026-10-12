# 06_CONCILIACION_AUDITORIAS_SOFTWARE_1_ESENCIAL_v2

**Conciliación de los dos informes de ChatGPT sobre Software 1.º Esencial** · 12/10/2026

Versión contrastada: **v2 actual** (rama `claude/libros-5z31jx`, commit `558a335`, carpeta `software_1_esencial/salida/`).

**Informes conciliados:**

| | Documento | Alcance | Veredicto |
|---|---|---|---|
| **Informe 1 (I1)** | `02_AUDITORIA_CHATGPT_SOFTWARE_1_ESENCIAL_v2.md` (Drive, `_TRABAJO`) | Maquetación | APTO CON CORRECCIONES MAYORES |
| **Informe 2 (I2)** | `04_AUDITORIA_CHATGPT_SOFTWARE_1_ESENCIAL_v2` (Google Doc) | Exhaustivo: 14 hallazgos v1 + 5 nuevos (H15–H19) | NO APTO |

Las correcciones V2-01 y V2-02 del I1 ya están aplicadas y se conservan. **Nada de este documento declara el paquete aprobado para la venta.**

## 1. Avances de la v2 actual respecto de la versión que auditaron ambos informes

| Documento | Auditado (v1) | v2 actual |
|---|---|---|
| Planes de Clase | 60 págs. (21 hojas de continuación) | **38 págs.**: portada, índice y un plan por hoja oficio |
| Plan Anual | 12 págs. (la última, solo con la firma) | **10 págs.** |
| Muestra | 14 págs. (Plan 1 partido en dos hojas) | **13 págs.** (Plan 1 en una hoja) |
| Márgenes de Plan Anual y Planes | 1,50 y 1,60/2,00 cm | **1,27 cm** en todas las secciones |
| Libro / Solucionario | 107 / 17 págs. | sin cambios |

## 2. Matriz de conciliación

Estados: **CORREGIDO** (cerrado en la v2 actual) · **RESUELTO** (ya estaba cerrado según ambos informes) · **PENDIENTE** (requiere la próxima pasada) · **DECISIÓN DE FER**.

| N.º | Gravedad | I1 | I2 | Estado en la v2 actual | Evidencia (verificada sobre `salida/` del commit 558a335) | Corrección pendiente |
|---|---|---|---|---|---|---|
| H01 | CRÍTICO | Cerrado | Resuelto | RESUELTO | La capacidad de abstracción, análisis y síntesis figura literal en el Libro (Ficha K), el Plan 30 y la secuencia 30 del Plan Anual. | — |
| **H02** | MAYOR | «Cerrado con ajuste» | **Parcial** | **PENDIENTE** (prevalece el I2) | Las filas 18 y 36 del Plan Anual dicen solo «Todas las capacidades de la Unidad 1, transcriptas en las secuencias 1 a 15» y «… de las Unidades 2 y 3, transcriptas en las secuencias 19 a 34». Les faltan 7 y 13 enunciados literales. Ninguna otra fila remite: las 34 restantes tienen sus capacidades completas. Los **Planes de Clase 18 y 36 sí** las transcriben completas (7 y 13). | Reemplazar el texto de las dos filas por la lista literal del Anexo B del I2. Coincide con `build/caps.py`: U1 = capacidades 1–7; U2 + U3 = capacidades 8–20. Después volver a medir la paginación del Plan Anual. |
| H03 | MAYOR | Cerrado | Resuelto | RESUELTO | 20/20 capacidades textuales en Libro, Plan Anual y Planes. | — |
| H04 | CRÍTICO | Cerrado | Resuelto | RESUELTO | Plan Anual: Ley 7593/2025 con vigencia diferida al 27/11/2027 (art. 57). | — |
| H05 | CRÍTICO | Cerrado | Resuelto | RESUELTO | Clase 7, actividad 11 e integradora 1 con datos distintos del ejemplo. | — |
| H06 | CRÍTICO | Cerrado en muestras | Resuelto | RESUELTO | Operandos de la Unidad 3 recalculados por el I2 (Anexo A4). | — |
| H07–H11 | MAYOR / MENOR | Cerrados | Resueltos | RESUELTOS | Licencias y Windows no genuino, grooming, Figuras 5.1/5.2 y 8.1/8.2, «del gabinete». | — |
| **H12** | MAYOR | Parcial (= V2-01) | Parcial | **CORREGIDO** | Planes: 38 páginas; las págs. 3–38 abren los planes 1–36, en orden; ninguna hoja de «continuación». | — |
| H13 | MAYOR | Cerrado | Resuelto | RESUELTO | Plan Anual y Planes sin «ESENCIAL» en el nombre. | — |
| **H14** | MENOR | Parcial documental (= V2-04) | Resuelto en el repositorio | **DECISIÓN DE FER** | En `_TRABAJO` sigue la nota vieja `03_NOTAS_PILOTO_SOFTWARE_1_ESENCIAL_v1` (137 págs., A4). Las notas vigentes son `entrega/NOTAS_PILOTO_SOFTWARE_1_ESENCIAL_v2.md`. | Fer autoriza a rotular la nota vieja «HISTÓRICA / SUPERSEDIDA». No se toca Drive sin esa orden. |
| **H15** | MAYOR (nuevo) | No relevado | **Abierto** | **PENDIENTE** | Recuento propio, en el texto de los .docx y de los PDF: ver §3. Hay **78 pictogramas**: Libro 56, Solucionario 21, Muestra 1; Plan Anual y Planes, 0. | Quitarlos del texto según §3. Regenerar los PDF del Libro, el Solucionario y la Muestra. Recuento final 0 en .docx y PDF. Las imágenes no se tocan. |
| **H16** | MAYOR (nuevo) | = V2-02 | Abierto | **CORREGIDO** | Plan Anual de 10 páginas. La última tiene criterios generales, estrategias de inclusión y firma, con un 71 % de la hoja ocupado. | Volver a verificar después de la corrección H02, porque las filas 18 y 36 se alargan. |
| **H17** | MAYOR (nuevo) | No relevado | Abierto | **CORREGIDO** | Márgenes de 1,27 cm en las 37 secciones de los Planes y en las 2 del Plan Anual, medidos con python-docx. Libro y Solucionario ya los tenían. | — |
| **H18** | MAYOR (nuevo) | No relevado | Abierto | **CORREGIDO** (en parte) | La Muestra termina en la portada de los Planes y en el Plan 1 completo en una hoja; no queda ninguna página de continuación. **Pero la pág. 9 (Práctica 1) conserva un «✅»** (H15). | Se cierra junto con H15, cuando la Muestra se rearme con el Libro sin pictogramas. |
| **H19** | MENOR (nuevo) | No relevado | A confirmar | **PENDIENTE (operativo)** | El I2 registra que el PDF y el .docx del Libro en Drive difieren en bytes de los de GitHub. | No se sube ni se reemplaza nada en Drive sin la orden de Fer. Cuando Fer apruebe, la subida debe hacerse desde un commit fijo, con verificación de hashes de cada .docx y PDF, y las versiones anteriores pasan a SUPERSEDIDOS. |
| V2-01 | MAYOR | Abierto | (= H12) | CORREGIDO | Ver H12. | — |
| V2-02 | MAYOR | Abierto | (= H16) | CORREGIDO | Ver H16. | — |
| **V2-03** | MENOR | Decisión de Fer | — | **DECISIÓN DE FER** | La portada y la contraportada del Libro (lienzo ampliado a oficio alrededor de una foto de Gemini) están **intactas** desde la v1 y no se tocan. | Fer decide, con Gemini si lo considera, a partir de una comparación antes/después a igual escala. |
| V2-04 | MENOR | Abierto | (= H14) | DECISIÓN DE FER | Ver H14. | — |

**Resumen:**

| Estado | Hallazgos |
|---|---|
| CORREGIDO en la v2 actual | H12, H16, H17, H18 (salvo el «✅» de la pág. 9) |
| RESUELTO desde antes | H01, H03–H11, H13 |
| PENDIENTE | **H02**, **H15**, H19 |
| DECISIÓN DE FER | H14/V2-04, V2-03 |

## 3. Pictogramas (H15)

| Documento | En el texto (.docx = PDF) | Dónde |
|---|---|---|
| Libro | **56**: 46 «✅» y 10 «✓» | Los 46 «✅» encabezan el renglón «✅ Punto de control: …» de las prácticas. Los 10 «✓» cierran verificaciones en los ejemplos resueltos de las Clases 17 a 20, del tipo «Verificación: 64+8+4+2 = 78 ✓». Págs. 10, 14, 18, 19, 23, 28, 29, 33, 37, 38, 43, 44, 48, 49, 50, 52, 58, 62, 63, 67, 71, 72, 76, 77, 81, 85, 87, 92, 96, 97, 99–101, 103. |
| Solucionario | **21** «✓» | Verificaciones de las Clases 17 a 20 y de las evaluaciones (págs. 11–13). |
| Muestra | **1** «✅» | Pág. 9, Práctica 1. |
| Plan Anual / Planes de Clase | 0 | — |
| «✗» y «✔» | 0 en los cinco documentos | — |

**¿Existe una prohibición aprobada?** Sí, como regla de colección establecida por Fer, y ya se aplicó en otros paquetes:
- **Algorítmica 3.º v2**, hallazgos 14.1 y 14.2: se retiraron «✓», «✗», «✔» y «✅» porque el «✅» depende de una fuente de emoji y puede perderse al imprimir o copiar.
- **Algorítmica 3.º v2.2**: por pedido de Fer, se quitaron el «✓» y las «✗» de la Figura 9.1 (retoque en copia, original conservado).
- **Software 2.º**, diagnóstico §7: «Están prohibidos en la colección». Se quitaron los 52 «✅», y ese paquete fue aprobado por Fer el 11/10/2026.

Por eso, para Software 1.º la normalización no es una decisión editorial nueva: es aplicar una regla vigente. Para la próxima pasada se propone:
1. **Prácticas.** «✅ Punto de control: …» pasa a «Punto de control: …», sin pictograma. El recuadro de la práctica ya lo identifica, como en Algorítmica 3.º y Software 2.º.
2. **Verificaciones.** Se quita el «✓» final: «Verificación: 64+8+4+2 = 78.»
3. **Muestra.** Se rearma con la página del Libro ya corregida.
4. **Imágenes.** No se modifica ninguna imagen aprobada. Si alguna figura del Libro tiene un «✓» dibujado, se le informa a Fer por separado y se espera su decisión, como en la Figura 9.1 de Algorítmica 3.º. El recuento automático solo cubre el texto.

## 4. ¿La reducción de páginas eliminó contenido? (requisito 6)

Verificado sobre los .docx, comparando la v1 (commit `61feba7`) con la v2 actual:

- **Texto de los Planes de Clase:** 2461 párrafos en cada versión. Son idénticos uno a uno, salvo 35 números de página del índice.
- **Texto del Plan Anual:** 390 párrafos, todos idénticos.
- **Inventario por plan:**
  - Viñetas de indicadores, actividades y criterios: 611 en cada versión.
  - Momentos Inicio, Desarrollo y Cierre con sus tiempos: presentes en los 36 planes.
  - Bloque de evaluación, con procedimientos, instrumentos y criterios: presente en los 36.
  - «Observaciones» y las dos firmas: presentes en los 36.
  - Las diferencias de longitud de texto en los planes 5–7 son solo los dígitos de página del índice.
- **Capacidades MEC por plan:** las 36 secuencias tienen todas sus capacidades literales. Los Planes 18 y 36 tienen las 7 y las 13 completas.
- **Revisión ocular:** revisé las 38 hojas de los Planes y las 10 del Plan Anual. Ningún bloque cortado y las firmas dentro de la hoja. Letra de 9 pt en las celdas de los Planes (antes 9,5 pt), legible.

Los controles automáticos (`build/control_v2.py`, 94; `build/auditoria_v1.py`, 117) son controles internos del constructor y **no reemplazan la auditoría independiente**. Ninguno de los dos contaba los pictogramas: por eso H15 pasó inadvertido. Se agregará ese recuento en la próxima pasada.

## 5. Próxima pasada propuesta (requiere autorización)

Sin reconstruir nada, solo sobre los .docx de `salida/`:

1. **H02:** filas 18 y 36 del Plan Anual con las capacidades literales. Volver a medir la paginación (la meta sigue siendo como máximo 11 hojas, sin hoja de firma suelta).
2. **H15:** quitar los 78 pictogramas del texto del Libro, el Solucionario y la Muestra. Regenerar los PDF del Libro y el Solucionario con LibreOffice y Carlito, que es la misma vía de los PDF actuales. Comprobar que el Libro siga en 107 páginas, el Solucionario en 17 y los índices iguales al PDF. Rearmar la Muestra.
3. **Controles:** sumar el recuento de pictogramas (0 en los .docx y los PDF) y la identidad textual con la v2 actual: solo deben cambiar las dos filas y los pictogramas.
4. **Documentación:** `03_RESPUESTA_CLAUDE_SOFTWARE_1_ESENCIAL_v3.md` y `NOTAS_PILOTO v3`. Las versiones anteriores quedan en el historial de git.

**Queda fuera de la pasada, hasta la decisión de Fer:** portada y contraportada (V2-03), nota vieja de Drive (H14) y subida a Drive con hashes (H19).

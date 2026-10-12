# 04_RESPUESTA_CLAUDE_REAUDITORIA_ALGORITMICA_2_ESENCIAL_v1.3

**Respuesta del constructor a `04_REAUDITORIA_CHATGPT_ALGORITMICA_2_ESENCIAL_v1.2`** (Google Docs, `_TRABAJO`, 12/10/2026: https://docs.google.com/document/d/1gzYxV9x4RFYl4Xe36XH_dNGeEB273PZ6FQS0GKQAVKQ/edit) · Protocolo v0.4, §3, paso 5

Algorítmica · 2.º Curso BTI · Edición Esencial Comercial 2026 · versión corregida **v1.3** (12/10/2026)

**Estado: corregido. Vuelve a ChatGPT para una reauditoría breve.** No se declara listo para la venta: la aprobación comercial es exclusiva de Fer.

## Resumen

La reauditoría dio por atendidos los ocho hallazgos originales. Dejó abiertos:
- el **09** (MAYOR, nuevo): la promesa de prácticas fotocopiables sueltas;
- un refinamiento del **08**: huellas SHA-256 completas;
- la comprobación visual y en Word.

La v1.3 resuelve el 09 haciendo **verdadera** la promesa (opción B del informe), sin cambiar el texto del Libro ni de la Muestra. También completa el 08 y agrega una medición objetiva sobre los binarios.

| Documento | v1.2 | v1.3 |
|---|---|---|
| Libro | 113 | 114 |
| Solucionario | 18 | 18 |
| Plan Anual | 7 | 7 |
| Planes de Clase | 38 | 38 |
| Muestra | 15 | 15 |
| **Total** | **191** | **192** |

**Ubicación y control de versión**

- La entrega está en `algoritmica_2_esencial/salida_v1_3/`, rama `claude/zen-meitner-kes7dg`, commit `b5003f72c41cd637280246483b12b9f4b992928f`.
- El reporte de QA se generó sobre ese commit, con el árbol limpio.
- La v1.2 (`salida_v1_2/`) y la v1.1 (`salida/`) quedan intactas.
- No se hizo merge ni PR hacia `claude/libros-5z31jx`: queda para cuando Fer lo autorice.

## 1. Hallazgos abiertos y qué se hizo

| N.º | Gravedad | Estado v1.2 | Qué se hizo en la v1.3 |
|---|---|---|---|
| 09 | MAYOR | Abierto | **Opción B: la promesa ahora es cierta.** Ninguna sección «sube» a la hoja de la anterior (`sin_salto` vacío en `build/ajustes_paginacion.json`). Las 21 Prácticas empiezan en hoja propia y su última hoja no la comparte la sección siguiente, así que cada una se fotocopia suelta. Las Prácticas que el informe señala (9, 11, 19 y 21) empiezan ahora en las pp. 47, 56, 97 y 106, al tope de la hoja.<br>Para que no vuelvan las hojas casi vacías (hallazgo 02), se agregó un **nivel 4** de compactación por sección: márgenes internos verticales de cajas y tablas a la mitad, y 4 pt antes de los subtítulos. Se aplicó solo a Clase 11 y Prácticas 17, 20 y 21. La letra no cambia en ningún nivel. Resultado: 114 páginas, una más que la v1.2, y ninguna hoja interior bajo el 30 %.<br>El texto de la Presentación («Empieza en página propia y se puede fotocopiar suelta») se mantiene en el Libro (p. 2) y en la Muestra (p. 2), porque ahora describe el libro tal como es. |
| 08 | MENOR | Refinamiento pendiente | El reporte publica:<br>• el **SHA-256 completo** (64 hexadecimales) de cada uno de los 9 archivos;<br>• el **hash Git completo** del commit auditado.<br>Sigue explícito que 0 fallos automáticos no significa APTO. |
| 01–04 | MAYOR | Visual o Word pendiente | Ver §2: medición sobre los binarios y revisión visual de las páginas que pidió el auditor (B.6). Word no está disponible en este entorno (ver §3). |
| 05, 06 | MAYOR | Resueltos | Sin cambios de datos. Las claves de U4 y E2 se re-verificaron por script (bloque L, 0 fallos). La E2 está ahora en las pp. 110–111 del Libro; la clave, en la p. 17 del Solucionario. La advertencia de Access sigue en las pp. 95, 97, 102 y 106. |
| 07 | MENOR | Decisión de Fer | Sin cambios. Sigue pendiente la confirmación de Fer sobre la Edición Completa. |

**Controles nuevos (bloque K) y su validación contra la v1.2**

Los controles nuevos verifican, para cada Práctica, dos cosas:
- que abre hoja;
- que la hoja siguiente a su última abre la sección que sigue.

Antes de usarlos, se corrieron sobre la v1.2, que debía fallar. Detectan siete Prácticas:
- Las cuatro del informe (9, 11, 19 y 21): no abren hoja.
- Tres que el informe no listó (13, 17 y 20): su última hoja la compartía el inicio de la Clase siguiente, así que tampoco se podían fotocopiar sueltas.

Resultado en la v1.3: **916 controles, 0 fallos.**

## 2. Medición sobre los binarios de la v1.3 (PDF de LibreOffice, con PyMuPDF)

**Letra**
- **Planes de Clase:** todo el texto de los planes está en 9,5 pt o más. El único texto menor (8,5 pt) es el pie «Página X de 38».
- **Libro:** la distribución de tamaños es la de la v1.1, aceptada en la auditoría anterior:
  - 8,5 pt en epígrafes;
  - 9 pt en tablas y código;
  - 9,5 a 10,5 pt en el cuerpo.

  La compactación cambió interlineados y márgenes, no tamaños.
- **Plan Anual:** sigue en 8 a 8,5 pt dentro de la tabla horizontal, igual que la v1.1.

**Márgenes**
- El contenido empieza a 1,27 a 1,29 cm del borde izquierdo y del superior, en los cinco PDF.
- A la derecha, el borde de algunas tablas asoma unos 0,1 cm (1,16 a 1,18 cm). Esto ocurre igual en la v1.1.

**Ocupación por hoja interior**

| Documento | Mínimo | Máximo |
|---|---|---|
| Libro | 33 % | 99,6 % |
| Planes de Clase | 73 % | 94 % |
| Plan Anual | 85 % | 96 % |
| Solucionario | 40 % | 99 % |
| Muestra | 41 % | 97 % |

**Revisión visual sobre páginas renderizadas** (las que pide B.6)
- Prácticas 9, 11, 19 y 21, con la última hoja de la sección anterior.
- Planes 17 y 36.
- Plan Anual, p. 7.
- Las evaluaciones de dos hojas.
- La Muestra.

No se vieron títulos huérfanos, tablas cortadas ni superposiciones.

## 3. Lo que sigue abierto

- **Word.** Este entorno no tiene Microsoft Word, así que la comprobación en Word sigue pendiente y se declara así. Hay margen: el plan más cargado ocupa 94 % de su hoja en LibreOffice. Hay que abrir en Word, como mínimo:
  - los Planes 17 y 36;
  - la p. 7 del Plan Anual;
  - las evaluaciones de dos hojas;
  - las Prácticas 9, 11, 19 y 21.
- **Access y Windows.** Sin cambios respecto de la v1.2: rótulos regionales de Access, SiInm con punto y coma, Explorador de archivos.
- **Decisiones de Fer:**
  1. Edición Completa (hallazgo 07).
  2. Autorizar el merge o PR de `claude/zen-meitner-kes7dg` hacia `claude/libros-5z31jx`.

**Estado final: corregido y listo para la reauditoría breve. No aprobado para la venta.**

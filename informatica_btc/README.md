# Informática 2.º y 3.º BTC · Revisiones R2 y R3

Auditoría independiente y mejora editorial del 22 de octubre de 2026, sobre la entrega R1
(rama `codex/entrega-btc-r1-2026-10-22`, carpeta `Entregas_BTC/R1_2026-10-22`).

- R1, sus paquetes y los originales de Drive no se modificaron: R2 se construye en copias nuevas.
- No se subió nada a Drive ni se publicó ningún paquete comercial.
- Análisis y Diseño de Sistemas 3.º BTI sigue en pausa.

## Revisión R3 (cierre, 22 de octubre de 2026)

R3 se construye sobre copias de R2. R2 queda intacta: lo comprobé con las huellas SHA-256 antes y después de cada
construcción. R3 cubre cinco puntos:
- legibilidad de figuras: piso de 7 pt al tamaño impreso;
- cierre de las observaciones editoriales que se podían resolver;
- lista exacta de verificación legal: los sitios oficiales no respondieron desde este entorno;
- comparación visual para aprobación;
- pruebas prácticas por curso.

| Carpeta / archivo | Qué es |
|---|---|
| `*/R3/` | Los cinco DOCX R3 de cada curso |
| `*/pdf_revision_R3/`, `*/revision_visual_R3/` | PDF de revisión y hojas de contacto de R3 |
| `*/figuras_R3/` | Figuras usadas en R3 |
| `*/CIERRE_R3_*.md` | Qué se resolvió, qué decide Fernando y qué queda para la institución o para verificación externa |
| `*/LEGIBILIDAD_R3_*.md` | Medición calibrada por figura, tomo y laboratorio, antes y después |
| `*/BITACORA_R2_R3_*.md` | Registro de cada cambio R2 → R3 |
| `*/COMPARACION_PARA_APROBACION_*.pdf` | R1 frente a R3 de cada figura, con casillas de aprobación. En 2.º incluye además los encuentros 33-35 |
| `*/VERIFICACION_LEGAL_PENDIENTE_*.md` | Normas, artículos, afirmaciones y páginas que hay que comprobar sobre el texto oficial. Ninguna fila está marcada como verificada |
| `*/PRUEBAS_PRACTICAS_*.md` | Pruebas por práctica: programa, procedimiento, resultado esperado y evidencia |

| Curso | Páginas R3 (tomo / lab / plan / sol / planes) | Cambio principal |
|---|---|---|
| 2.º BTC | 75 / 26 / 4 / 23 / 37 | Laboratorio sin textos de figura bajo 7 pt; figuras 1 y 2; 8 ajustes editoriales |
| 3.º BTC | 77 / 33 / 7 / 22 / 37 | Tomo y laboratorio sin textos de figura bajo 7 pt; figuras 2 y 19; 6 ajustes editoriales |

**Ninguna de las dos colecciones está declarada apta para la venta.** Los dictámenes son provisionales y
dejan observaciones abiertas.

## Contenido

| Carpeta / archivo | Qué es |
|---|---|
| `2_BTC/R2/`, `3_BTC/R2/` | Los cinco DOCX R2 de cada curso: tomo, laboratorio, plan anual, solucionario y planes de clase |
| `*/pdf_revision/` | PDF de revisión renderizados con LibreOffice. El entregable es el DOCX |
| `*/revision_visual/` | Hojas de contacto de todas las páginas, usadas en la revisión visual |
| `*/figuras/` | Figuras usadas en R2 (PNG) y fuentes SVG de las reconstruidas en vector |
| `3_BTC/recursos/` | Los cinco CSV de laboratorio, sin cambios respecto de R1 (verificados) |
| `*/MATRIZ_HALLAZGOS_*.md` | Hallazgos bloqueantes, importantes y menores, con archivo, sección, evidencia, corrección y estado; observaciones abiertas |
| `*/BITACORA_R1_R2_*.md` | Registro de cada cambio R1 → R2, generado por el constructor |
| `*/DECISIONES_FIGURAS_*.md` | Decisión por figura (incorporar, corregir o reconstruir), con motivo y legibilidad |
| `*/PRUEBAS_Y_PENDIENTES_*.md` | Pruebas realizadas y verificaciones pendientes |
| `*/DICTAMEN_*.md` | Veredicto provisional y su alcance |
| `FUENTES_CONSULTADAS.md` | Fuentes curriculares y legales con fecha y alcance |
| `build_comun/` | Utilidades: edición diferencial de DOCX, índices, hojas de contacto, cotejo de claves, medición de legibilidad, bitácora |
| `*/build/` | Constructores de cada curso (`figuras_*.py`, `r2_*.py`) y su registro JSON |

## Resumen

| Curso | Hallazgos corregidos | Observaciones abiertas | Figuras | Páginas R2 (tomo / lab / plan / sol / planes) | Veredicto |
|---|---|---|---|---|---|
| 2.º BTC | 22 (3 bloqueantes) | 11 | 9 incorporadas, 1 corregida, 3 en vector | 75 / 23 / 4 / 23 / 37 | APTO CON OBSERVACIONES (revisión editorial) |
| 3.º BTC | 17 (1 bloqueante) | 9 | 17 incorporadas, 2 corregidas, 1 en vector | 77 / 22 / 7 / 22 / 37 | APTO CON OBSERVACIONES (revisión editorial) |

## Reconstrucción

Requiere python-docx, Pillow, matplotlib, shapely, PyMuPDF, LibreOffice y la fuente Carlito.

```
cd 2_BTC/build && python3 figuras_2btc.py <R1>/Imagenes_2_BTC_13_Figuras/Propuestas ../figuras
python3 r2_2btc.py <R1>/Informatica_2_BTC_R1
cd ../../3_BTC/build && python3 figuras_3btc.py <R1>/Imagenes_3_BTC_20_Figuras/Propuestas ../figuras
python3 r2_3btc.py <R1>/Informatica_3_BTC_R1
# R3 (lee R2 solo para lectura)
cd ../../2_BTC/build && python3 figuras_r3_2btc.py ../figuras ../figuras_R3 && python3 r3_2btc.py
cd ../../3_BTC/build && python3 figuras_r3_3btc.py ../figuras ../figuras_R3 && python3 r3_3btc.py
```

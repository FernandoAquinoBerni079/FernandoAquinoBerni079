# Informática 2.º y 3.º BTC · Revisión R2

Auditoría independiente y mejora editorial del 22 de octubre de 2026, sobre la entrega R1
(rama `codex/entrega-btc-r1-2026-10-22`, carpeta `Entregas_BTC/R1_2026-10-22`).

- R1, sus paquetes y los originales de Drive no se modificaron: R2 se construye en copias nuevas.
- No se subió nada a Drive ni se publicó ningún paquete comercial.
- Análisis y Diseño de Sistemas 3.º BTI sigue en pausa.

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
```

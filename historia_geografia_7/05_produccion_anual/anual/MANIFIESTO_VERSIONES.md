# Manifiesto de versiones — Historia y Geografía 7.º, producción anual

Rama: `claude/libros-5z31jx`. Cada fila es un commit. Para ver exactamente qué cambió en cada paso:

```
git show --stat <commit>
git diff <commit_anterior> <commit> -- historia_geografia_7/05_produccion_anual/scripts/contenido/
```

Ningún commit anterior se reescribió.

## Historia de la producción

| Commit | Fecha | Contenido |
|---|---|---|
| `841f5bc` | — | **Muestra 3**, aprobada como modelo (no comercial). Carpeta `04_muestra3/`, congelada. |
| `1feea85` | 14/10/2026 | Estructura de la producción anual. Condiciones del dictamen: A05, A10, A14, A17, A19 y N01-N05. |
| `755d7ad` | 14/10/2026 | **Bloque I** (encuentros 1-9). |
| `ea3cf5f` | 15/10/2026 | **Bloque II** (encuentros 10-18). |
| `754fc8d` | 15/10/2026 | **Correcciones del Bloque II**, tras la revisión de Fernando. A19: el segundo fragmento de la Real Provisión pasa a ser una adaptación declarada. Tabaré, 1543. Comparación de los mapas del Bloque I. Ver `bloque_2/INFORME_BLOQUE_II.md` §7. |
| `372362e` | 15/10/2026 | **Bloque III** (encuentros 19-27). Encuentro 22 con núcleo del siglo XVII. |
| `f1df4c2` | 15/10/2026 | **Bloque IV** (encuentros 28-36). |
| este commit | 15/10/2026 | **Consolidación anual**. Ver la sección siguiente. |

## Cambios introducidos en la consolidación

Están documentados en `INFORME_CONSOLIDACION.md` §4.

| Archivo | Cambio | Motivo |
|---|---|---|
| `scripts/contenido/e17.py` | Ítems 3 y 8 de la Evaluación U3 reformulados; ajuste en la clave del ítem 8. | Repetían textualmente actividades de las Clases 7 y 10 (control C, repeticiones). |
| `scripts/contenido/e25.py` | El ítem 5 de la Evaluación U4 pasa de Quebec a Nueva Ámsterdam, con su clave. El ítem 8 se reformula y pasa de falso a verdadero. | Repetían actividades de las Clases 13 y 15. |
| `scripts/contenido/e28.py` | Ítem 2 de la Clase 18 reformulado. | Repetía la actividad 3 de la Clase 2. |
| `scripts/construir_bloque.py` | El índice estático se itera hasta que la paginación queda estable. | El índice del tomo anual ocupa dos hojas. |
| `scripts/motor/pdf.py` | Detecta la última hoja del índice. | Ídem. |
| `scripts/motor/planes.py` | Índice compacto cuando hay más de 20 planes. | El índice de los 36 planes dejaba una hoja casi vacía. |
| `scripts/motor/solucionario.py` | Las últimas filas de la matriz ítem-capacidad-puntaje van juntas. | Evita dos filas sueltas al pie del volumen anual. |
| `scripts/anuales.py` (nuevo) | Plan anual, matriz curricular y controles de consolidación. | Condiciones 1, 5 y 6 del cierre. |

Los Bloques II, III y IV se reconstruyeron con esos cambios: sus PDF nuevos reemplazan a los de los commits `754fc8d`, `372362e` y `f1df4c2`, que siguen disponibles en el historial. El Bloque I no se reconstruyó: no tuvo cambios de contenido, y conserva los archivos del commit `754fc8d`.

## Archivos del paquete anual

Las huellas SHA-256 de todos los archivos están en `../MANIFIESTO.json`, que genera `scripts/estado.py tabla`.

| Documento | Formato | Archivo |
|---|---|---|
| Tomo del estudiante | Oficio vertical | `anual/tomo/TOMO_ANUAL_oficio.docx` y `.pdf` |
| Planes de clase | A4 vertical | `anual/planes/PLANES_ANUAL_A4.docx` y `.pdf` |
| Solucionario docente | A4 vertical | `anual/solucionario/SOLUCIONARIO_ANUAL_A4.docx` y `.pdf` |
| Plan anual | Oficio horizontal | `anual/plan_anual/PLAN_ANUAL_oficio.docx` y `.pdf` |
| Matriz curricular | A4 horizontal | `anual/matriz/MATRIZ_CURRICULAR_36_ENCUENTROS_A4.docx` y `.pdf` |
| Figuras | PNG, 300 ppp | `anual/figuras/` |
| Copias livianas para revisión | PDF | `anual/revision_liviana/` |
| Datos | JSON | `anual/datos/`: trazabilidad, páginas, controles por encuentro y controles de consolidación |

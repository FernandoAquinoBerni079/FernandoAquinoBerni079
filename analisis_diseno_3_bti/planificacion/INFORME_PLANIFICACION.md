# Informe de planificación — ADS 3.º BTI: plan anual y 36 planes de clase

**Análisis y Diseño de Sistemas, 3.er curso BTI · Plan Optativo · 21 de octubre de 2026**

**Base:** colección v0.2, commit `88c5cb5`.

**Estado:** versión 0.1 para revisión final.
- No es definitiva: falta que la institución confirme el encuadre institucional y la carga horaria.
- No es una impresión comercial ni está validada en Windows o en aulas.
- No está autorizada para la venta.

Lectura recomendada, en este orden:
1. `ESTRUCTURA_Y_ALINEACION.md`: estructura propuesta, respaldo curricular y controles de alineación.
2. Este informe.
3. Los documentos.

## 1. Primera tarea: documentación de cierre de la v0.2

Está en `00_cierre_v0_2/`: la adenda, su script y `VERIFICACION_CIERRE_v0_2.json`. **Ningún archivo de `coleccion/` se sobrescribió.** El control A lo comprueba con `git diff 88c5cb5`.

| Punto | Resultado |
|---|---|
| 51 frente a 57 instrumentos | El control de impresión comprobó 57 ubicaciones: los 51 instrumentos de la tabla «Instrumentos del año» y las 6 tablas de calendario de la sección 1. El texto del control llamaba «instrumentos» a las 57. La cifra del informe se corrige a: «51 instrumentos y 6 tablas de calendario, 57 ubicaciones comprobadas». Sigue habiendo 0 fallos |
| 160 frente a 101 archivos | El ZIP tiene 101 entradas: 98 archivos y 3 carpetas. De los 98, 97 son archivos del manifiesto con el mismo SHA-256, y el otro es el propio manifiesto. Los 63 que no van en el ZIP están todos en `build/figs/` (58 PNG y 5 `simbolos.json`): son intermedios regenerados, que están en git. Cuenta: 97 + 63 = 160 |
| Observación nueva | El rótulo interno de `MANIFIESTO_COLECCION.json` todavía dice «v0.1», pero sus huellas son las de la v0.2. Queda registrado sin corregir el archivo aprobado |

## 2. Segunda y tercera tarea: entregables

Todo está en `analisis_diseno_3_bti/planificacion/`.

| Documento | Páginas | Contenido |
|---|---:|---|
| `ADS_3BTI_PLAN_ANUAL_OFICIO_O3.docx` y `.pdf` | 23 | Encuadre en tres niveles, competencia y capacidades, organización y tiempo, metodología y recursos, evaluación con los hitos, desarrollo de los 18 capítulos y 36 encuentros, condiciones para declararlo definitivo, Anexo A (HC por categoría, capacidades y columna de fechas para la institución) y Anexo B (matriz de correspondencia) |
| `ADS_3BTI_PLANES_DE_CLASE_OFICIO_O3.docx` y `.pdf` | 73 | Tabla de los planes con su página y los 36 planes, cada uno en página nueva y de dos páginas |

**Formato:** el comercial aprobado el 20 de octubre (`formatos_comerciales/formatos.py`, importado sin cambios):
- oficio con márgenes espejados O3;
- Calibri 10;
- letra mínima de 8 pt;
- campos editables de institución, docente, sección, año lectivo y fecha (184 en los planes);
- anexos en horizontal.

El DOCX es el entregable editable y el PDF sirve de control.

**Distribución del tiempo:**
- Cada plan suma 5 HC con la misma secuencia de la guía aprobada.
- En el Encuentro 35, la guía reparte el tiempo con la planilla de tiempos (alternativas A, B y B+). El plan no supone minutos ni un segundo evaluador.
- En 7 encuentros, el inicio toma 0,5 HC del primer tramo de la guía, que en esos casos dura 2 a 4 HC.
- Las Prácticas 9 y 13 quedan fuera de las 5 HC, como indica la guía.

**Lo que agrega la planificación, siempre con su fuente:**
- la selección de 2 a 4 indicadores por encuentro;
- el propósito del encuentro (el foco de Work);
- la tarea anterior;
- las ideas clave (recuadros «Concepto clave» del libro);
- los errores frecuentes (claves de la guía);
- la preparación previa (secciones 0 de cada parte de la guía);
- las alternativas sin computadoras (guía, Parte IV, sección 0.3, y Parte V).

18 actividades del libro, de 11 encuentros, no aparecen en ninguna secuencia de la guía. Se informan como opcionales, sin tiempo asignado.

## 3. Auditoría

| Control | Resultado |
|---|---|
| `controles_plan.py`: 83 controles en 8 bloques. A: fuentes; B: correspondencia curricular; C: tiempo; D: numeración; E: evaluación; F: referencias; G: paginación y legibilidad; H: reservados | **0 fallos y 0 sin ejecutar**. Se corrió con la copia del MEC y el PDF de Work |
| `prueba_fuentes_plan.py`: Carlito, Liberation Sans y DejaVu Sans | **6 de 6 combinaciones correctas** (detalle abajo) |
| Revisión visual de las 96 páginas (`revision_visual/`, 17 hojas de contacto) | Sin defectos pendientes |

**Prueba de fuentes:**

| Fuente | Plan anual | Planes |
|---|---:|---:|
| Carlito | 23 págs. | 73 págs. |
| Liberation Sans | 24 págs. | 74 págs. |
| DejaVu Sans | 26 págs. | 74 págs. |

En las tres fuentes:
- no hay páginas en blanco;
- cada plan sigue empezando en página propia, ocupa como máximo dos páginas y termina con sus firmas.

Si el DOCX se abre en un equipo sin Calibri ni Carlito, la paginación cambia. En ese caso, las páginas de los planes que cita el plan anual (Anexo B) y la tabla inicial de los planes se regeneran con `construir_todo.py`.

**Revisión visual.** Se corrigieron tres cosas:
- una fila partida que dejaba una página casi vacía en el plan anual;
- la ficha de capítulo que se cortaba entre páginas;
- las consignas que se cortaban en un «:».

Las salidas de cada paso están en `evidencias/`. `MANIFIESTO_PLANIFICACION.json` tiene el SHA-256 de cada archivo de `planificacion/` y de las fuentes leídas.

Para regenerar todo:

```
ADS_MEC_PDF=<copia del MEC> python3 -B analisis_diseno_3_bti/planificacion/build/construir_todo.py
```

## 4. Lo que no se tocó

- Los tres documentos de la colección v0.2, sus evidencias y su manifiesto.
- Los seis lotes y los materiales de otras asignaturas.
- Las herramientas del lote 6.

No se subió nada a Drive. El PDF del MEC y el informe de Work no se copiaron al repositorio, y tampoco se agregaron datos DR ni variantes V6.

## 5. Limitaciones y pendientes

- La auditoría se hizo en pantalla, con PDF de LibreOffice y Carlito. No se abrió en Microsoft Word ni en Windows, y no hubo prueba impresa.
- La selección de indicadores por encuentro y las 7 aperturas son decisiones de esta planificación y conviene que las revise un docente.
- La asignación de los antecedentes MEC a cada capítulo es la del plan preliminar, rotulada como propuesta.
- **Para declararla definitiva hace falta:**
  - la confirmación institucional de la sección 1.3 del plan anual (PCI, carga horaria, duración de la HC, calendario, 36 o 28 encuentros, períodos de calificación);
  - la prueba de campo del entorno en las computadoras de la institución;
  - la revisión jurídica de la licencia de la Unidad VI;
  - la revisión docente.

Me detengo para la revisión final.

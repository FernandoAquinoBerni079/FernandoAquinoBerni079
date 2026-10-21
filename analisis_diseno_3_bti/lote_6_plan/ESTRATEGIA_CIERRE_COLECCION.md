# Estrategia de cierre de la colección — Análisis y Diseño de Sistemas, 3.º BTI

**Biblioteca Comercial 2026 · 21 de octubre de 2026**

**Estado:** propuesta para aprobar. **No se ejecuta nada de lo que sigue** hasta que estén aprobados el lote 6 y esta estrategia. No se genera el tomo anual ni los 36 planes, no se sube nada a Drive y no se declara aptitud comercial.

**Objetivo:** producir una colección anual coherente desde las fuentes ya aprobadas, **sin repetir las auditorías superadas**.
- Lo aprobado no se reescribe: se arma.
- La auditoría de cierre revisa solo lo que el armado cambia y lo que no existía antes: el tomo como un todo, los planes y el plan anual definitivo.

## 1. Principio: armado desde las fuentes, con auditoría diferencial

**Los seis lotes tienen su fuente editable.**
- Cada lote tiene sus módulos de contenido (`capN.py`), su caso y su constructor.
- `lote_5/build/tomo.py` ya lista de dónde sale cada capítulo.
- El cierre agrega una carpeta nueva, `coleccion/`, que importa esas fuentes y no las copia. Los lotes 1 a 6 no se modifican.

**Control de equivalencia (la base de la auditoría diferencial).**
- El armado unificado extrae el texto de cada capítulo y lo compara con el del documento aprobado de su lote, párrafo por párrafo y tabla por tabla.
- Solo pueden diferir:
  - la portada, los preliminares y el índice;
  - las aperturas de unidad;
  - las menciones a «lote» en el libro del estudiante, que se reemplazan (sección 2);
  - las remisiones a secciones de la guía, que cambian de número;
  - los encabezados y la paginación.
- Toda otra diferencia es un fallo. La lista de diferencias admitidas, con cada caso, es lo que se audita, no los 18 capítulos otra vez.

**Versiones.**
- Cada lote queda en su versión aprobada:
  - lote 1: candidata O3;
  - lote 2;
  - lote 3 v1.1;
  - lote 4 v1.1;
  - lote 5;
  - lote 6, cuando se apruebe.
- Ningún commit se reescribe.

## 2. Tomo anual unificado (libro del estudiante, 18 capítulos)

**Cómo se arma:** `coleccion/build/tomo_anual.py`.
- **Una sola portada y un solo índice.** Los preliminares son los del lote 1 (`lote_1/build/prelim.py`), con la tabla de unidades completa.
- **Las seis aperturas de unidad.**
- **Los 18 capítulos,** cada uno con la función de armado de su lote.
- **La carga de cada módulo, aislada.** Los constructores de los lotes comparten nombres de módulos (`construir`, `guia`, `piezas`, `diagramas`), así que cada lote se importa con su propio espacio de nombres.
- **Las figuras y los fragmentos de código,** regenerados desde sus scripts y leídos del proyecto, como en cada lote.

**Ajustes del armado:** son pocos, cada uno se lista y el control de equivalencia los admite uno por uno.
- **Las menciones a «lote» y a «lote anterior»** en el libro del estudiante se reemplazan por «unidad» o por el número de capítulo. Ejemplo: la apertura de la Unidad V dice «la del lote anterior».
- **Las remisiones a la guía** («guía, sección 0.2») se reasignan a la numeración de la guía unificada.
- **Los complementos editoriales** (Prácticas 9 y 13) conservan su rótulo.
- **El formato del libro del lote 1:**
  - la candidata O3 se compuso antes del perfil común de los lotes 2 a 6;
  - antes de armar, compruebo si tiene diferencias de maqueta con el perfil O3 (márgenes, tamaños, cajas);
  - si las hay, las informo para decidir, en lugar de corregirlas en silencio.

**Extensión:** cerca de 225 a 235 páginas en oficio. Sale de la suma de los libros aprobados (49 + 39 + 35 + 44 + 30), sin repetir portadas ni índices parciales, más el lote 6. Si supera el límite práctico de encuadernación que fije la editorial, propongo dos volúmenes por etapa (Unidades I a III y IV a VI), que coinciden con el corte del H3.

## 3. Guía docente unificada y solucionarios

**Estructura propuesta:**
- **Parte general:**
  - capacidades y rótulos;
  - entorno y ficha E-1 a E-12;
  - coordinación con Laboratorio;
  - las dos distribuciones de la base;
  - las copias descartables;
  - el procedimiento DR, solo la plantilla;
  - el calendario de 36 y 28 encuentros completo.
- **Una parte por unidad,** con lo que ya está en cada guía aprobada:
  - la secuencia por encuentro;
  - las claves;
  - las listas de cotejo;
  - las referencias de código;
  - las rúbricas de los hitos;
  - los bancos de variantes.
- **Parte final:**
  - la planilla anual H1 a H6 y la defensa;
  - la ponderación editorial;
  - los resultados de las pruebas con su entorno;
  - la procedencia consolidada de todos los recursos.

**Solucionario:** las claves salen del mismo registro de claves que genera cada evaluación (`H.CLAVES`). El control comprueba que cada ítem de cada evaluación del tomo tenga su clave y su criterio, con las mismas letras que en el libro.

**Observaciones de la auditoría del lote 5, para la guía unificada.** El lote 5 está congelado, así que estas notas se agregan en la parte de la Unidad V de la guía unificada, como diferencias admitidas:
- **Preparación del Encuentro 30:**
  - el docente prepara de antemano las copias de evaluación con DR, las cuentas, las tareas impresas y las planillas;
  - las 5 HC se reparten entre las dos sesiones de uso, la revisión cruzada y el acta;
  - si falta equipamiento, se documenta una rotación, sin omitir evidencias esenciales.
- **Conjunto reservado:**
  - DR se guarda fuera de GitHub y de las carpetas del alumnado;
  - se recomienda agregar casos propios;
  - sus resultados privados no cuentan como auditados de forma independiente hasta que se examine ese paquete.

**Lo reservado:** el conjunto DR no entra en la guía unificada ni en ningún entregable versionado. Se entrega al docente por separado, como en el lote 5.

## 4. Cuaderno de prácticas integrado

- Reúne las prácticas de los 18 capítulos, desde las mismas funciones que el libro.
  - El lote 1 no tuvo cuaderno: sus Prácticas 1 a 3 se extraen igual que las demás.
  - Los Capítulos 16 y 18 no tienen práctica.
- **Sin contenidos duplicados:**
  - el cuaderno no repite secciones, ejemplos ni evaluaciones;
  - remite a las tablas y figuras del libro por su número.
- El control comprueba que cada práctica tenga el mismo texto que en el libro y que ninguna evaluación aparezca en el cuaderno.

## 5. Plan anual definitivo

- Se genera con el formato canónico de la colección:
  - el pipeline `plan_anual.py`;
  - la tabla continua de 7 columnas;
  - `formatos_comerciales/FORMATO_PLAN_ANUAL_OFICIO`.
- Sale del plan anual preliminar, que ya lee las fichas de los capítulos construidos.
- **Indicadores:** se leen de las fichas, nunca se escriben a mano. Se comprueba que haya una ficha por capítulo, 18 en total.
- **Procedimientos e instrumentos:** únicos en todo el año, como pide el formato canónico. Salen de los instrumentos reales de cada capítulo: rúbricas de los hitos, listas de cotejo de las prácticas, evaluaciones y planillas.
- **Calendario:** dos etapas, con el corte en el H3 (Encuentro 18), y la adaptación de 28 encuentros como anexo.
- **Rótulos:**
  - las capacidades, rotuladas como propuesta para el programa institucional;
  - lo único del MEC son los antecedentes del Diseño Curricular que cita Work §3, con su página.

## 6. Los 36 planes de clase

- **Formato:** la plantilla V3 ya aprobada para esta asignatura (`planes_clase/PLANTILLA_PLAN_DE_CLASE_ADS.md`), en modo A (tomo → plan anual → planes) y en HC. No se supone la duración de la hora cátedra.
- **De dónde sale cada campo:**
  - tema, procedimientos e instrumentos: del plan anual, textuales;
  - capacidad e indicadores: de la ficha del capítulo;
  - momentos: de las tablas de secuencia por encuentro de cada guía (por ejemplo, `SEC_C14` en `guia_u5.py`), que ya dan los tramos y sus HC;
  - recursos: de las tablas, figuras, ejemplos y actividades citados, con correspondencia bidireccional.
- **Producción por unidad,** con la auditoría de 100 puntos de cada plan:
  - unicidad con piso verificable;
  - suma de HC igual a 5;
  - evidencia de Work §5.2 nombrada en la evaluación;
  - rúbrica del hito en los Encuentros 6, 12, 18, 26, 32 y 34.
- **Revisión:** Fernando revisa una unidad de muestra antes de producir las otras cinco.

## 7. Control de coherencia de la colección

Un verificador de colección (`coleccion/build/coherencia.py`) cruza los documentos entre sí:
- **Libro ↔ guía:** cada tabla, figura, código, ejemplo y actividad que cita la guía existe en el libro, con el mismo número. Las claves cubren todas las actividades y evaluaciones.
- **Libro ↔ cuaderno:** las prácticas son idénticas.
- **Libro ↔ código:** cada fragmento se lee del archivo del proyecto y coincide línea por línea. Las versiones citadas (lote 4, v2, v2 con SC-02 y paquete del lote 6) existen.
- **Evaluaciones:** semillas únicas en todo el año, 15 puntos cada una y claves en el solucionario.
- **Planificación:**
  - el plan anual cubre los 36 encuentros y 180 HC;
  - cada plan de clase coincide con su fila del plan anual y con la ficha;
  - los hitos están en sus encuentros;
  - la tabla de 28 encuentros es la misma en el libro, la guía y el plan anual.
- **Rótulos:**
  - ninguna capacidad presentada como oficial del MEC;
  - nada declarado validado ni probado en colegios;
  - los pendientes del entorno, siempre como pendientes.
- **Trazabilidad:** cada código citado (RF, RNF, ME, OP, P, C, IN, SC…) existe en las fuentes del caso.
- **Reserva:** ningún dato de DR en los entregables, y la comprobación opcional con la ruta privada.

## 8. Auditoría de impresión en oficio O3

- Sobre el tomo, la guía y el cuaderno unificados, con los mismos programas de los lotes:
  - filas de tablas completas;
  - párrafos impresos;
  - palabras enteras;
  - figuras con su epígrafe;
  - índice estable;
  - márgenes espejados;
  - cortes de tabla;
  - bloques de código enteros;
  - prueba con tres fuentes de sustitución.
- Los planes de clase y el plan anual usan sus propios controles de formato (cantSplit selectivo en planes y universal en el plan anual), sin cruzar reglas.
- **Láminas de revisión:** una por unidad y una por cada tipo de pieza (hitos, prácticas, evaluaciones, código, planillas), para que la revisión visual no tenga que recorrer todo el tomo.

## 9. Inventario de entregables, versiones y manifiestos

| Entregable | Formato | Fuente |
|---|---|---|
| Libro del estudiante (tomo anual) | DOCX (entregable) y PDF (control) | `coleccion/build/tomo_anual.py` |
| Guía docente con solucionario | DOCX y PDF | `coleccion/build/guia_anual.py` |
| Cuaderno de prácticas | DOCX y PDF | `coleccion/build/cuaderno_anual.py` |
| Plan anual | DOCX y PDF | `coleccion/build/plan_anual.py` |
| 36 planes de clase | Un DOCX y su PDF | `coleccion/build/planes.py` |
| Base de proyecto: base del estudiante y referencia docente vigente | Carpetas y ZIP | `lote_4/proyecto/`, `lote_5/proyecto/`, `lote_6/proyecto/` |
| Herramientas de la Unidad V: cargador DP y plantilla DR | Carpetas | `lote_5/proyecto/cargador_dp/`, `lote_5/caso/dr_plantilla.py` |
| Conjunto reservado DR | Fuera del repositorio | Lo genera y guarda el docente |

- **Inventario de versiones:**
  - `coleccion/INVENTARIO.md` dice de qué versión aprobada de cada lote sale cada capítulo;
  - qué referencia de código es la vigente y cuáles se conservan como historia;
  - qué queda pendiente: pruebas institucionales en Windows, instalación y restauración en laboratorio y concurrencia.
- **Manifiesto SHA-256 de la colección:** `coleccion/MANIFIESTO_COLECCION.json`, con cada entregable y las huellas de los manifiestos de los seis lotes. Una sola comprobación muestra que nada aprobado cambió.
- **Estado declarado en todos los documentos:** versión para revisión de la colección. Sin aprobación comercial ni validación en laboratorios hasta que Fernando lo decida.

## 10. Orden de ejecución propuesto y puntos de aprobación

1. Construcción del lote 6 y su auditoría.
2. Tomo, guía y cuaderno unificados, con el control de equivalencia.
   - **Aprobación 1:** la lista de diferencias admitidas.
3. Plan anual definitivo.
   - **Aprobación 2.**
4. Planes de clase de una unidad de muestra.
   - **Aprobación 3:** formato y contenido.
5. Los 36 planes.
6. Verificador de coherencia, auditoría de impresión, inventario y manifiesto de la colección.
   - **Aprobación final de Fernando,** sobre la colección completa.

Ninguno de estos pasos sube archivos maestros a Drive ni declara aptitud comercial.

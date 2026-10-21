# Estructura propuesta y controles de alineación curricular — Planificación ADS 3.º BTI

**Análisis y Diseño de Sistemas, 3.er curso BTI · Plan Optativo · 21 de octubre de 2026**

**Base:** colección v0.2, commit `88c5cb5`. Fue aprobada como base editorial estable para la planificación docente.

**Estado:** versión 0.1 para revisión.
- No es definitiva. Para eso falta que la institución confirme el encuadre institucional y la carga horaria (sección 1.3).
- No incluye validación en Windows, impresión comercial ni autorización de venta.

## 1. Respaldo curricular e institucional disponible

### 1.1 Disposiciones oficiales del MEC (comprobadas)

**Fuente:** *Diseño Curricular del Bachillerato Técnico en Servicios, Informática*, mayo de 2026.
- Copia de 111 páginas y 1 457 383 bytes.
- SHA-256 `a0052cc5…4bdd0856`: es la misma copia que cita el informe de Work.

Se volvieron a leer las páginas en esa copia. Las 11 citas del plan anual son textuales; las comprueba `controles_plan.py`.

| Pág. | Qué establece | Uso en el plan |
|---|---|---|
| 29 | El Plan Optativo lo eligen las instituciones según las necesidades e intereses de los estudiantes. «Cada institución puede elaborar su propio programa de estudio» | La asignatura es un programa institucional, no nacional |
| 24 | La adecuación se concreta en el PCI. Las disciplinas incorporadas no reemplazan a las nacionales ni reducen sus cargas horarias | La institución adopta el programa en su PCI. El optativo no toma horas de otras disciplinas |
| 34 | Plan de estudios «vigente según la Resolución N° 2141/2016»; «Plan Optativo 5» en 3.º | La tabla no dice la unidad: el informe de Work la lee como horas cátedra semanales, y la institución debe confirmarlo |
| 31 y 33 | El docente define los indicadores de cada capacidad y, con ellos, los procedimientos e instrumentos | Es la estructura del plan anual y de los planes |
| 96 y 101 | Aprendizaje basado en proyectos; evaluación continua e individual | Metodología y evaluación |

**Lo que el documento no establece** (se revisaron sus 111 páginas):
- la duración de la hora cátedra;
- la cantidad de semanas o encuentros, y sus fechas;
- etapas o períodos de evaluación del optativo;
- un programa o capacidades para «Análisis y Diseño de Sistemas»;
- un trámite de aprobación del programa institucional.

El plan no inventa nada de eso.

### 1.2 Propuesta editorial de la colección (no oficial)

Todo esto viene del informe de Work v0.1 (SHA-256 `3d4f5ab9…065069a`) y lo desarrolla la colección v0.2. Cada documento lo rotula como propuesta:
- el nombre de la asignatura;
- la competencia y las capacidades C1 a C10;
- 36 encuentros de 5 HC (180 HC), como estimación editorial;
- 6 unidades y 18 capítulos;
- el caso Arapoty y el caso de práctica Mbokaja;
- el entorno técnico provisional;
- los hitos H1 a H6, la ponderación sugerida, el reparto 60/40 y los cuatro niveles;
- la adaptación alternativa a 28 encuentros.

### 1.3 Decisiones institucionales sin confirmar

Quedan como campos editables en el plan anual:
- la adopción del programa en el PCI;
- la carga horaria semanal;
- la duración de la HC;
- el calendario y las fechas;
- la elección entre 36 y 28 encuentros;
- los períodos de calificación y la conversión de los niveles;
- la coordinación con Algorítmica y con Laboratorio;
- el equipamiento y la prueba de campo;
- la custodia de los datos DR y V6.

## 2. Estructura del plan anual

Documento `ADS_3BTI_PLAN_ANUAL_OFICIO_O3`, en DOCX editable y PDF de control: 23 páginas en oficio O3, con los dos anexos en horizontal.

| Sección | Contenido | Fuente |
|---|---|---|
| Identificación y estado | Campos editables: institución, docente, sección y año lectivo | Formato comercial del 20 de octubre |
| 1. Encuadre | Tres niveles: citas del MEC, propuesta editorial y decisiones institucionales | MEC; Work §2 |
| 2. Competencia y capacidades | Competencia y C1 a C10, con contenidos, indicadores, evidencia y criterio | Work §4.1-4.2 |
| 3. Organización y tiempo | Seis unidades, encuentros, HC, capítulos, resultado, hitos y las dos etapas de la colección; totales por categoría; adaptación a 28 | Work §5.1; libro; guía |
| 4. Metodología y recursos | ABP, estructura de taller, cuatro bloques de actividades, tres niveles de práctica, trabajo en equipo con evidencia individual, diagnóstico, coordinación, equipamiento y alternativas sin computadoras | Libro, pág. 6; guía; Work §3 y §5.1 |
| 5. Evaluación | Evaluación continua, ponderación, 60/40, niveles, evaluaciones de capítulo opcionales, condiciones mínimas y tabla de los seis hitos | Work §4.3; guía |
| 6. Desarrollo por unidad y capítulo | Para cada capítulo: la ficha del libro sin cambios, las secciones con su página y la articulación. Para cada encuentro: foco, páginas, secuencia de la guía, actividades, equipamiento, capacidades, indicadores, evidencia e instrumentos | Libro; guía; Work §5.2 |
| 7. Condiciones para declararlo definitivo | Lo que falta confirmar | — |
| Anexo A | Los 36 encuentros con sus HC en las 7 categorías, las capacidades C1 a C10 marcadas y una columna «Semana o fecha» que completa la institución | Distribución v2.1; Work §5.2 |
| Anexo B | Matriz de correspondencia (ver sección 4) | Colección v0.2 |

## 3. Estructura de cada plan de clase

Documento `ADS_3BTI_PLANES_DE_CLASE_OFICIO_O3`: 73 páginas. Trae una tabla inicial con la página de cada plan, y cada uno de los 36 planes empieza en página nueva y ocupa dos.

| Bloque | Contenido | De dónde sale |
|---|---|---|
| Identificación | Encuentro n de 36, unidad, capítulo, páginas del libro, del cuaderno y de la guía, y tema. Docente, sección y fecha son campos editables | Libro; guía; Work §5.2 |
| Capacidades | La capacidad de la ficha, textual y con su rótulo de propuesta institucional, más las capacidades del encuentro | Ficha del libro; Work §5.2 |
| Indicadores | De 2 a 4 indicadores de la ficha, textuales | Ficha del libro; selección en `modelo.py` |
| Momentos | Inicio, desarrollo y cierre con sus HC. Incluyen: los tramos de la guía, textuales; el propósito; la tarea anterior; las ideas clave («Concepto clave» del libro); los ejemplos resueltos; las actividades con su consigna; la práctica; la evidencia; la síntesis «Para repasar», y la tarea | Guía; libro; Work |
| Orientaciones metodológicas | Organización del trabajo, preparación previa, niveles de la práctica, errores frecuentes y «Si el calendario se acorta» | Guía; libro |
| Recursos | Secciones, tablas, figuras, códigos y ejemplos con su página; cuaderno; guía; equipamiento | Libro; guía; cuaderno |
| Sin computadoras | La alternativa de cada encuentro | Guía, Parte IV, sección 0.3 (pág. 56), y Parte V (pág. 78) |
| Evaluación | Procedimientos, instrumentos con su página de la guía y criterios: indicadores, evidencia, lista de cotejo y criterios de la rúbrica | Guía; Work §5.2 |
| Vinculación | Guía, cuaderno, hito y plan anual | — |
| Observaciones y firmas | Docente y visto bueno de la Dirección | Formato comercial |

**Decisiones propias de la planificación:** son tres, y están declaradas y controladas.

1. **Indicadores por encuentro** (`INDICADORES_POR_ENCUENTRO`):
   - cada encuentro evidencia de 2 a 4 indicadores de la ficha de su capítulo;
   - cada uno de los 90 indicadores se evidencia en al menos un encuentro.
2. **Apertura de 0,5 HC** en los Encuentros 18, 19, 26, 30, 32, 34 y 36:
   - en esos siete, el primer tramo de la guía dura entre 2 y 4 HC;
   - el inicio toma 0,5 HC de ese tramo para organizar la sesión;
   - la suma del tramo y del encuentro no cambia.
3. **Orientaciones y alternativas sin computadoras:** se arman con las secciones de la guía que las respaldan, citadas con su página. Las actividades del libro que la secuencia de la guía no programa (18 actividades, en 11 encuentros) se informan como «a criterio del docente», fuera de las 5 HC.

No se agregó ni cambió teoría, ejemplos, actividades, prácticas, claves, puntajes, indicadores ni criterios.

## 4. Matriz de correspondencia (plan anual, Anexo B)

Cada fila es un encuentro y tiene estas columnas:
- unidad y capítulo;
- páginas del libro;
- guía: parte, página de la secuencia y página de las claves;
- práctica: páginas del libro y del cuaderno, y lista de cotejo;
- evaluación opcional del capítulo y su clave;
- hito: libro, rúbrica y planilla, o el hito que prepara;
- capacidades;
- número del plan de clase y su página.

Los seis hitos tienen además su propia tabla en la sección 5: encuentro, capítulos que integran, qué se evalúa, capacidades y las páginas de la rúbrica, la planilla y las evidencias 60/40.

| Hito | Encuentro | Capítulos | Libro, pág. | Guía: rúbrica · planilla · evidencias |
|---|---:|---|---:|---|
| H1 | 6 | 1 a 3 | 47 | 19 · 20 · 19 |
| H2 | 12 | 4 a 6 | 85 | 37 · 38 · 37 |
| H3 | 18 | 7 a 9 | 121 | 52 · 53 · 52 |
| H4 | 26 | 10 a 13 | 163 | 74 · 75 · 75 |
| H5 | 32 | 14 a 16 | 190 | 91 · 92 · 92 |
| H6 | 34 | 17 | 203 | 107 · 108 · 107 |

## 5. Controles de alineación curricular

Resultado: **83 controles, 0 fallos y 0 sin ejecutar** (`CONTROLES_PLANIFICACION.json`). Además, la prueba de fuentes dio **6 de 6 combinaciones** correctas.

| Bloque | Qué se comprueba | Resultado |
|---|---|---|
| A. Fuentes (8) | La colección y los seis lotes no cambiaron desde `88c5cb5`. Solo cambió `planificacion/`. Los documentos leídos tienen el SHA-256 del manifiesto. Se verificaron las huellas de Work y del MEC, y las 11 citas son textuales | Correcto |
| B. Correspondencia (18) | Las 18 fichas coinciden con las fuentes de los lotes. Los 90 indicadores están cubiertos, con 2 a 4 por encuentro, y son textuales. Las capacidades llevan su rótulo y ninguna se presenta como oficial. Los 108 tramos de la guía y las 145 consignas son textuales. Foco y evidencia coinciden con Work §5.2 en el PDF original. No hay unidades, capítulos ni prácticas nuevas | Correcto |
| C. Tiempo (9) | Hay 5 HC por plan y la guía también suma 5 HC. El Encuentro 35 se reparte con la planilla. Solo hay 7 aperturas, y ningún inicio supera 1,5 HC. Los complementos quedan fuera. Son 180 HC: 30/30/30/40/30/20. No se fijan minutos ni fechas propias | Correcto |
| D. Numeración (7) | 36 planes del 1 al 36, cada uno en página nueva, con sus 12 bloques y 184 campos editables. La matriz cita la página de cada plan | Correcto |
| E. Evaluación (6) | Procedimientos e instrumentos en cada plan. Los seis hitos tienen rúbrica, planilla y evidencias. Hay 16 prácticas y 15 listas de cotejo en clase. Las 17 evaluaciones de capítulo figuran como opcionales. Diagnóstico, defensa y recuperación | Correcto |
| F. Referencias (10) | Hay 331 referencias al libro, 77 instrumentos de la guía, 20 secciones previas, prácticas en libro y cuaderno, hitos y recuadros. Cada uno está en la página que indica | Correcto |
| G. Paginación y legibilidad (18) | Oficio en todas las páginas y márgenes espejados O3. Letra mínima de 8 pt, fuentes incrustadas, nada a menos de 5 mm del borde. Sin páginas en blanco ni títulos solos al pie. Cada plan termina con sus firmas | Correcto |
| H. Reservados (7) | Ningún dato de DR ni de V6, comprobado con las rutas privadas. Hay avisos de seguridad, no hay archivos reservados y no se nombra ningún modelo de IA | Correcto |

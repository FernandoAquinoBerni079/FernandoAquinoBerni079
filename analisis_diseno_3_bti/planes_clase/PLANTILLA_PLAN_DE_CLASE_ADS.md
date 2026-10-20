# Plantilla canónica de los 36 planes de clase — Análisis y Diseño de Sistemas, 3.º BTI

**Biblioteca Comercial 2026 · Plan Optativo · 20 de octubre de 2026**

**Estado:** plantilla para aprobar. **No se produjeron los 36 planes.** Hay un único ejemplo completo, el del Encuentro 1 (§5), que sirve para validar el formato.

**Base:**
- formato canónico V3 de la colección (`cuadernillos-mec`, `references/plan-de-clase.md`): nueve bloques, registro neutro, unicidad §1.5bis y auditoría de 100 puntos;
- las secuencias por encuentro de las guías docentes (encuentros 1 a 6 en el lote 1; 7 y 8 en el Capítulo 4 v2.1);
- el plan anual preliminar (`../plan_anual/`).

## 1. Parámetros fijados para esta asignatura

| Parámetro (V3 §4) | Valor | Razón |
|---|---|---|
| `MODO_DERIVACIÓN` | A (pipeline): tomo → plan anual → planes | Hay tomo y habrá plan anual |
| `PERFIL` | Institucional (Bachillerato Técnico, Plan Optativo) | La asignatura no tiene programa oficial del MEC (Work §2.2) |
| `FUENTE_CAPACIDAD` | Ficha del capítulo en el tomo, **verbatim y con su rótulo** de propuesta institucional | Nunca se presenta como capacidad oficial del MEC |
| Tiempo | **5 HC por encuentro**, en HC | Work §2.2: las páginas verificadas no fijan la duración de la HC. `MINUTOS_HORA_CÁTEDRA` no se presume. |
| `VERSIÓN` | Comercial: institución, docente, fecha y sección en blanco | — |
| `USA_TOMO` | Sí: se citan capítulo, secciones, figuras, tablas, ejemplos y actividades por su número | Las páginas se citan solo si el tomo vigente es el oficio aprobado |
| Papel | Oficio vertical, con el perfil de `../formato/ESPECIFICACION_OFICIO.md` | Igual que Algorítmica 3.º |

## 2. Los nueve bloques y de dónde sale cada campo

| N.º | Bloque | Contenido | Fuente del campo |
|---|---|---|---|
| 1 | Título | «Plan de Clase N.º X — [foco corto del encuentro]» | Foco de Work §5.2, abreviado |
| 2 | Banda de identificación | Institución (en blanco) + «Plan de Clase N.º X de 36 · 2026» | — |
| 3 | Tabla de datos | <ul><li>Docente / Disciplina: «Análisis y Diseño de Sistemas (Plan Optativo, programa institucional)».</li><li>Curso: 3.º BTI / Tiempo: «5 HC (Encuentro X de 36)».</li><li>Organizador: Unidad y capítulo.</li><li>Material: tomo, con capítulo y secciones.</li><li>Fecha.</li><li>Tema, en fila ancha.</li></ul> | Unidad, capítulo y secciones: plan anual. Tema: fila del plan anual (verbatim). |
| 4 | Capacidad e indicadores | La capacidad de la ficha del capítulo, con su rótulo. De 2 a 4 indicadores **del capítulo** cuya evidencia se produce en ese encuentro. | Ficha (verbatim). La selección de indicadores por encuentro se fija en el plan anual. |
| 5 | Momentos didácticos | Tabla MOMENTO / ACTIVIDADES / TIEMPO, en HC. La estructura de taller de Work §5.1 da el punto de partida: <ul><li>**Inicio** = problema y explicación (aprox. 1 HC);</li><li>**Desarrollo** = práctica (aprox. 3 HC);</li><li>**Cierre** = revisión, evidencia y cierre (aprox. 1 HC).</li></ul> Se redistribuye en los encuentros de diagnóstico, relevamiento, hitos y defensa, como hacen las guías. | Tramos de la secuencia de la guía del capítulo |
| 6 | Recursos y medios auxiliares | Las secciones, figuras, tablas, ejemplos y actividades del tomo que se usan, más los recursos de aula: equipos, entorno del prototipo desde la Unidad IV, material impreso. | Correspondencia bidireccional con las actividades (V3 §8) |
| 7 | Evaluación | Banda + Procedimientos / Instrumentos / Criterios. Nombra la **evidencia del encuentro** de Work §5.2 y, en los hitos, la rúbrica del Hx. | Procedimientos e instrumentos: plan anual (verbatim). Criterios: guía. |
| 8 | Observaciones | Línea en blanco | — |
| 9 | Firmas | Docente / Dirección — Visto bueno | — |

**Tarea domiciliaria.** Va solo si la guía la asigna, y siempre con el número de actividad.

## 3. Reglas de redacción y de control

- **Registro.** La prosa del plan es neutra e impersonal: «Lectura guiada de…», «Se realiza la puesta en común…». Las consignas del tomo conservan su voseo y se citan igual que en el original (V3 §1.8bis).
- **Tiempos.** Inicio, desarrollo y cierre suman exactamente 5 HC, y las actividades deben caber en ese tiempo.
- **Trazabilidad.** Cada indicador recorre la cadena actividad observable → evidencia → criterio → instrumento. Los códigos de control no se imprimen.
- **Unicidad (§1.5bis).**
  - Ningún par de planes coincide a la vez en la primera actividad de Inicio, el procedimiento y el instrumento.
  - Si un instrumento se repite en más de 3 planes consecutivos, se marca para revisión.
  - En una asignatura por proyecto, la lista de cotejo y la bitácora se repiten con legitimidad: se diferencian por la evidencia del encuentro.
- **Planes condicionales.**
  - El diagnóstico va en el Encuentro 1.
  - Los hitos H1 a H6 van en los encuentros 6, 12, 18, 26, 32 y 34.
  - La defensa va en el 35 y la recuperación en el 36.
  - Cada hito y cada evaluación integradora tiene su plan, con actividades de sesión de evaluación (V3 §9).
- **Sin códigos internos** en campos visibles: nada de rutas, nombres de archivo de figura ni semillas de evaluación.
- **Auditoría de 100 puntos** de V3 §12, más tres controles propios:
  1. la capacidad figura con su rótulo de propuesta institucional;
  2. el tiempo está en HC y suma 5;
  3. la evidencia del encuentro coincide con Work §5.2.

## 4. Lo que hay hoy para cada encuentro

| Encuentros | Insumo para el bloque 5 | Estado |
|---|---|---|
| 1 a 6 | Secuencia en tramos de la guía del lote 1 (`lote_1/build/guia.py`, `SEC_C1` a `SEC_C3`) | Disponible; pendiente de la auditoría del lote 1 |
| 7 y 8 | Secuencia de la guía del Capítulo 4 v2.1 | Disponible; cambia con la especificación C3 (la Actividad 1 (d) del Encuentro 8 pasa a tarea) |
| 9 a 36 | — | Se escriben con cada lote, en la guía y luego en el plan |

**Orden de producción.** Los 36 planes se generan con el constructor de la colección, a partir del plan anual y de las guías aprobadas. No se escriben a mano.

## 5. Ejemplo completo: Plan de Clase N.º 1

Construido solo con lo que ya dicen la guía del lote 1 (secuencia del Encuentro 1, claves del diagnóstico) y la ficha del Capítulo 1. Valida el formato; no es el plan definitivo.

**Plan de Clase N.º 1 — El reto y el sistema que ya existe**

*Institución: ______________ · Plan de Clase N.º 1 de 36 · 2026*

| Campo | Contenido | Campo | Contenido |
|---|---|---|---|
| Docente | ______________ | Disciplina | Análisis y Diseño de Sistemas (Plan Optativo, programa institucional) |
| Curso | 3.º BTI | Tiempo | 5 HC (Encuentro 1 de 36) |
| Organizador curricular | Unidad I. Comprender el problema y su contexto · Capítulo 1. Un sistema comienza con una necesidad | Sección | ______ |
| Material | Tomo: preliminares (acuerdo de trabajo, diagnóstico de entrada); Capítulo 1, secciones 1.1 y 1.2 | Fecha | ___ / ___ / ______ |
| Tema | Presentación del reto y diagnóstico de programación, formularios, datos y comunicación. | | |

**Capacidades propuestas para el programa institucional** (C1 y C7, en parte; no son capacidades oficiales del MEC):
- C1. Delimita un problema y evalúa la factibilidad de una solución.
- C7, en parte. Organiza y registra el trabajo colaborativo (acuerdo de trabajo y plan de apoyo).

**Indicadores de logro** (de la ficha del Capítulo 1, los que se evidencian en este encuentro):
- Distingue una dificultad cotidiana del problema de información que la explica y de una solución anticipada.
- Describe un sistema de información con sus personas, procesos, datos, recursos y límites.
- Reconoce sus conocimientos previos y acuerda un plan de apoyo y las reglas de trabajo del equipo.

| Momento | Actividades | Tiempo |
|---|---|---|
| Inicio | Presentación del libro y del caso (preliminares). Diagnóstico de entrada, individual y sin nota: es la «resolución individual breve» de Work. Autoevaluación por área. | aprox. 1,5 HC |
| Desarrollo | Sección 1.1 con la Tabla 1.1 y el Ejemplo resuelto 1.1 (ficha de problema). Sección 1.2 con la Figura 1.1 y el Ejemplo resuelto 1.2. Actividades 1 a 3, en parejas. | aprox. 2,5 HC |
| Cierre | Actividad 4 en plenario. Los equipos firman el acuerdo de trabajo de los preliminares. El docente recoge los diagnósticos y arma el mapa de apoyos del curso (evidencia del Encuentro 1). La Actividad 5 queda como tarea. | aprox. 1 HC |
| **Total** | | **5 HC** |

**Recursos y medios auxiliares:**
- tomo: preliminares (acuerdo de trabajo y diagnóstico de entrada);
- Tabla 1.1, Figura 1.1 y Ejemplos resueltos 1.1 y 1.2;
- Actividades 1 a 5;
- claves del diagnóstico (guía docente, §1).

**Evaluación**

| Procedimientos | Instrumentos | Criterios |
|---|---|---|
| Diagnóstico de entrada, individual y sin nota; observación del trabajo en parejas (Actividades 1 a 3) | Registro del diagnóstico por área y mapa de apoyos del curso | Cada área (programación, ítems 1 a 3; formularios, 4 y 5; datos, 6 y 7; comunicación, 8 y 9) se marca «firme» (todos los ítems correctos), «a reforzar» (alguno) o «a enseñar» (ninguno), y se compara con la autoevaluación del estudiante. Evidencia del encuentro (Work §5.2): resolución individual breve; mapa de apoyos. |

**Tarea:** Actividad 5 del Capítulo 1.

**Observaciones:** ________________________________________________

Docente ______________________ · Dirección — Visto bueno ______________________

**Control del ejemplo:**
- tiempos: 1,5 + 2,5 + 1 = 5 HC;
- capacidad con rótulo;
- indicadores verbatim de la ficha;
- actividades y criterios tomados de la guía (`SEC_C1` y §1 de la guía);
- evidencia igual a Work §5.2, encuentro 01;
- ningún código interno visible.

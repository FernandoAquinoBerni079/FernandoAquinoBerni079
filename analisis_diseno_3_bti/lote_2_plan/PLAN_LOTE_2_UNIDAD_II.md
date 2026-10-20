# Plan detallado del lote editorial 2 — Unidad II (Capítulos 4, 5 y 6)

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · 20 de octubre de 2026**

**Estado:** plan para aprobar. **No se construye nada hasta cerrar la auditoría del lote 1 y recibir la autorización de Fernando.**
- No se escribieron los Capítulos 5 y 6.
- No se modificó ningún archivo existente.
- Este plan amplía, y no reemplaza, `PREPARACION_LOTE_2_UNIDAD_II.md` (commit `d0bb8d9`), que queda sin cambios.

**Fuentes:**
- Informe de Work v0.1, recuperado. SHA-256 `3d4f5ab9daf3329f0dd34b13bc30b7001cb8e65780262c536346dbbea065069a`, verificado. Secciones usadas: §4.2 (C3, C4 y C7), §4.3, §5.2 (encuentros 7 a 12), §6 (índice de la Unidad II) y §7 (caso, reglas y trazabilidad).
- `lote_1/caso/dossier.py` y `lote_1/caso/mbokaja.py`.
- Capítulo 4: v2 (libro), v2.1 (guía) y especificación C3.
- Distribución de 180 HC, v2.1.

## 0. Criterios editoriales adoptados (revisión con ChatGPT, 20 de octubre)

1. **Formato oficio** para toda la colección. Las medidas exactas están en `../formato/ESPECIFICACION_OFICIO.md`. Los originales en A4 no se tocan: se producen versiones nuevas.
2. **Buzón B-01 a B-08 de Arapoty** en la Práctica 4. Mbokaja sigue como caso de transferencia donde corresponda. Toda práctica exige datos y decisiones nuevos (Work §7.4).
3. **Un único tomo anual de 18 capítulos**, construido por unidades sobre una fuente editable común (§5).
4. **Capítulo 4:** se aplica la especificación C3 sin rehacer el contenido.
5. **Plan anual preliminar** en paralelo: `../plan_anual/`.
6. **Plantilla canónica de los 36 planes de clase**, con los encuentros 1 a 8 como referencia: `../planes_clase/`.
7. **H2:** evalúa el análisis de requisitos, los modelos funcionales, la solicitud de cambio y la actualización del dossier.

## 1. La Unidad II en Work

**Unidad II — Especificar qué debe resolver el sistema.** Encuentros 7 a 12, 30 HC.
- **Resultado de la unidad:** «Requisitos, procesos y trazabilidad inicial» (Work §5.1).
- **Capacidades propuestas:** C3, C4, C7 y C9. Se rotulan siempre como propuestas para el programa institucional, no oficiales del MEC.

| Enc. | Foco (Work §5.2) | Evidencia o evaluación (Work §5.2) | Capacidades | HC (distribución v2.1) |
|---:|---|---|---|---|
| 7 | Formular requisitos funcionales y reglas de préstamo. | Catálogo con identificadores y fuente. | C3 | A 5 |
| 8 | Definir calidad, restricciones y criterios de aceptación. | Requisitos comprobables; revisión entre pares. | C3, C9 | A 4, V 1 |
| 9 | Representar proceso actual y proceso propuesto. | Flujos comentados y decisiones justificadas. | C4 | A 3, D 2 |
| 10 | Desarrollar casos de uso y excepciones. | Préstamo, devolución y consulta con alternativas. | C3, C4 | A 5 |
| 11 | Priorizar, planificar incrementos y establecer trazabilidad. | Requisito-modelo-prueba; tareas y responsables. | C3, C7 | A 2, G 3 |
| 12 | Resolver una solicitud de cambio; revisión de unidad II. | H2: requisitos y modelos funcionales versionados. | C3, C4, C7 | A 3, E 2 |

**Indicadores y criterios de Work §4.2 que la unidad debe dejar evidenciados:**
- **C3:** al menos ocho requisitos funcionales y cuatro no funcionales o restricciones; aceptación y prioridad; una modificación registrada. Criterio: distinción correcta entre requisito, regla y solución.
- **C4:** límites y actores representados; tres casos de uso prioritarios con flujo alternativo; coherencia con los requisitos. Criterio: «sin mezclar notaciones».
- **C7:** tareas, responsables, versiones y revisión entre pares.

## 2. Capítulo 4. Requisitos que se pueden comprobar (encuentros 7 y 8)

Las secciones 4.1 a 4.4 y la práctica ya coinciden con Work §6, y lo verifica un control del piloto v2. El trabajo es de **integración**, no de reescritura.

| Tarea | Detalle | Control |
|---|---|---|
| Especificación C3 | Consigna común RNF-04 (B-03) antes de los niveles. Nivel 2 desde RNF-05 y solo con B-08. Actividad 1 (d) del Encuentro 8 a tarea. En la guía: clave, fila de cotejo y fila de correspondencia. | Las cuatro comprobaciones del §4 de la especificación |
| Fuente única | El extracto del dossier, las reglas RN-01 a RN-06, el **catálogo RF-01 a RS-02**, los postergados y el **buzón B-01 a B-08** pasan a `caso/dossier.py`. El capítulo los lee de ahí. | El control actual de `verificar_caso.py`, más el texto idéntico del catálogo y del buzón antes y después del traslado |
| Buzón de Arapoty | Se conserva (criterio 2). Ya exige decisiones nuevas: la regla nueva RN-07 a partir de B-06, el estado «dañado» de B-02 y la contradicción interna de B-08. La guía lo declara como datos nuevos del mismo caso, no usados en los ejemplos. | No hay ningún pedido del buzón en los ejemplos resueltos 4.1 a 4.5 |
| Integración en el tomo | Sin portada ni recuadro de piloto. Lo precede una apertura de la Unidad II con el formato de la Unidad I. El rótulo de capacidad sigue el formato del lote 1. | Bloque B del lote 1 extendido |
| Evaluación | Se conserva la semilla `ADS3-C4v2-2`, en página propia, con 15 puntos | Bloque I extendido |

## 3. Capítulo 5. Procesos, contexto y casos de uso (encuentros 9 y 10)

**Capacidades:** C4 (encuentros 9 y 10) y C3 (encuentro 10).
**Secciones (Work §6, textuales):**

| Sección | Encuentro | Contenido previsto | Fuente de datos del caso |
|---|---|---|---|
| 5.1. Proceso actual y proceso propuesto. | 9 | Diagrama del proceso actual de préstamo y devolución, de 5 a 7 pasos, con los problemas del dossier marcados. Proceso propuesto con las reglas RN-01 a RN-06. Qué cambia, quién lo hace y qué decisión se tomó en cada paso. | E1-L2, E1-L4, E4-L2, E4-L4 y reglas |
| 5.2. Diagrama de contexto y límites de intercambio de información. | 9 | El sistema como caja; entidades externas (bibliotecaria, lector, dirección, encargado de informática); qué información entra y sale; qué queda fuera del límite (Work §7.2, «fuera del núcleo»). | Interesados y alcance del dossier |
| 5.3. Actores, casos de uso y escenarios principales. | 10 | Actor y rol frente a persona. Los tres casos de uso prioritarios de Work §4.2: préstamo, devolución y consulta de disponibilidad, cada uno con su escenario principal y los requisitos que cubre. | RF-01 a RF-08 y RNF-02 |
| 5.4. Excepciones, decisiones y flujos alternativos. | 10 | Un flujo alternativo por caso de uso, como mínimo: ejemplar ya prestado (RF-04), lector en el máximo (RF-05) o inactivo (RF-06), devolución sin préstamo identificable (E4-L2). Punto de decisión y resultado esperado. | RF-04 a RF-06, E4-L2 |

**Notación.** Para cumplir el criterio de C4, «sin mezclar notaciones», se usan una sola notación de flujo de proceso y la notación de casos de uso, y cada una se presenta en su sección. Hay que decidir el símbolo de cada elemento y fijarlo en `diagramas.py` antes de escribir.

**Práctica 5** (Work: «modelar préstamo y devolución con situaciones problemáticas nuevas»): **caso de transferencia Mbokaja**.
- **Datos:** las fichas de cartón (V-03) y las devoluciones sin anotar (V-11) ya están en `mbokaja.py`.
- **Situaciones nuevas, que no aparecen en los ejemplos:** ejemplar devuelto dañado, y estudiante del turno mañana con la biblioteca abierta solo de tarde (V-01).
- **Tres niveles:**
  1. proceso actual;
  2. proceso propuesto con un caso de uso;
  3. un segundo caso de uso con su flujo alternativo y la decisión que lo resuelve.

**Para no duplicar Algorítmica 3.º:**
- Work §8.2 señala que sus prácticas de biblioteca trabajan datos, claves, integridad y la elección de tecnología. El Capítulo 5 modela **procesos e interacciones**, no tablas.
- **Control:** no usar las personas ni los títulos de Algorítmica 3.º (`PROHIBIDOS_ALGORITMICA`), ni diagramas entidad-relación.
- Dibujo Técnico 1.º (pp. 35-38) da la legibilidad y las convenciones. La semántica del diagrama de contexto y de casos de uso se enseña acá (Work §3, «N»).

**Si el calendario se acorta.** La adaptación de 28 encuentros (v2.1) une los encuentros 9 y 10 y conserva el proceso actual simplificado (5 a 7 pasos, aprox. 1 HC), el proceso propuesto y los tres casos de uso con un flujo alternativo cada uno.

**Evaluación opcional:** 15 puntos, en página propia, con semilla nueva distinta de las cuatro existentes.

## 4. Capítulo 6. Priorizar y mantener la coherencia (encuentros 11 y 12)

**Capacidades:** C3 y C7 (encuentro 11); C3, C4 y C7 (encuentro 12).
**Secciones (Work §6, textuales):**

| Sección | Encuentro | Contenido previsto | Fuente |
|---|---|---|---|
| 6.1. Alcance mínimo y funcionalidades postergables. | 11 | El núcleo de Work §7.2 frente a lo postergable: los postergados del Capítulo 4, como la renovación sin traer el libro (E3-L4), y lo de «fuera del núcleo». Criterio de prioridad con su razón. Sin matriz ponderada (control E del lote 1). | Catálogo y postergados del Capítulo 4; alcance del dossier |
| 6.2. Trazabilidad entre necesidad, requisito, modelo y prueba. | 11 | Matriz de trazabilidad N → RN → RF → caso de uso o flujo → criterio de aceptación → prueba prevista. Ejemplo resuelto con la cadena de Work §7.3 (N-02, RN-01, RF-04, P-07), extendida al caso de uso del Capítulo 5. | Work §7.3, Figura 4.2 y Capítulo 5 |
| 6.3. Iteraciones, tareas, dependencias y responsabilidades. | 11 | Incrementos del prototipo (los encuentros 19 a 26 como referencia de Work §5.2), tareas con responsable, dependencias sencillas y versiones. Sin PERT ni teoría de grafos (Work §3, Matemática Aplicada: articulación condicional). | Distribución v2.1 y bitácora del lote 1 |
| 6.4. Solicitud de cambio y análisis de impacto. | 12 | Solicitud formal: quién la pide, qué cambia, a qué requisitos, casos de uso y pruebas afecta (con la matriz de 6.2), decisión y nueva versión del catálogo. | Una necesidad nueva del usuario (§4.1) |

### 4.1 Revisión de la Unidad II e hito H2 (encuentro 12)

**Work §6:** «Revisión de unidad II: nueva necesidad del usuario y actualización del dossier; H2». Evidencia (§5.2): «requisitos y modelos funcionales versionados».

**El H2 evalúa (criterio 7):**
1. el análisis de requisitos (C3);
2. los modelos funcionales (C4);
3. la resolución de la solicitud de cambio, con el análisis de impacto (C3 y C7);
4. la actualización del dossier y de su versión (C2 y C7).

**Dónde se aplica.** El H2 se hace sobre el proyecto de cada equipo, igual que el H1:
- el dossier del caso, si el curso trabaja con él;
- el relevamiento real autorizado, si lo hizo.

La nueva necesidad no puede estar en el dossier ni en el buzón.

**Instrumento: rúbrica del H2** en la guía, con el formato del H1:
- entre cinco y seis criterios × cuatro niveles (Sólido, Logrado, En desarrollo, Inicial; Work §4.3);
- en cada criterio, 60 % de evidencia del equipo y 40 % individual: cada estudiante explica el impacto de un cambio acotado;
- la ausencia de evidencia se registra aparte;
- planilla de registro;
- rótulo de «propuesta editorial».

**Si el calendario se acorta.** La v2.1 de la distribución une los encuentros 11 y 12. Se conservan la trazabilidad, una solicitud de cambio y el H2.

## 5. Tomo anual único y fuente editable común

Criterio 3: el tomo anual se construye por unidades, sin rehacer lo aprobado.

| Pieza | Hoy | Para el tomo anual |
|---|---|---|
| Contenido de los capítulos | `lote_1/build/cap1.py` a `cap3.py` y `fase2_pilotos/A2_capitulo4_v2/build/contenido.py` | Un módulo por capítulo (`capNN.py`) en una sola carpeta de fuentes. Los del lote 1 se mueven sin cambiar el texto, y lo comprueba un control de igualdad de texto. |
| Datos del caso | `caso/dossier.py` y `caso/mbokaja.py` | Los mismos dos módulos, ampliados con el catálogo y el buzón (§2) |
| Maqueta | `helpers.py` y `maqueta.py`, en A4 | Una sola maqueta parametrizada (papel y márgenes) con el perfil oficio de la especificación |
| Constructor | `construir.py` del lote 1 | Un constructor que arma, con las mismas fuentes: tomo del estudiante, guía docente con solucionario, **cuaderno de prácticas** (extracción imprimible de las prácticas, Work §9), plan anual y planes de clase |
| Verificador | `verificar.py` del lote 1 (bloques A a J) | El mismo verificador, aplicado a todos los capítulos construidos, más los controles nuevos (C3, notación, trazabilidad entre capítulos) |

**Orden de transición, para no mezclar riesgos:**
1. Se cierra la auditoría del lote 1 en A4.
2. Se produce la **versión oficio del lote 1** con el mismo contenido, como versión nueva, y se verifica.
3. Recién entonces se construye el lote 2, ya en oficio y en la fuente común.

## 6. Entregables del lote 2

- **Tomo del estudiante, Unidad II,** en oficio (DOCX y PDF):
  - apertura de la unidad;
  - Capítulos 4 a 6 con ficha, secciones, ejemplos resueltos, figuras, actividades en cuatro bloques, práctica en tres niveles, «Para repasar», «Si el calendario se acorta» y evaluación opcional;
  - revisión de la unidad con el H2.
- **Guía docente con solucionario de la Unidad II:**
  - secuencia por encuentro en HC;
  - claves de todas las actividades, prácticas y evaluaciones;
  - listas de cotejo;
  - rúbrica del H2 con planilla;
  - procedencia de los recursos.
- **Cuaderno de prácticas, Unidad II:** extracción de las Prácticas 4 a 6, de la misma fuente.
- **Controles y prueba con tres fuentes de sustitución.**
- **Informe del lote y manifiesto SHA-256.**

## 7. Riesgos

| Riesgo | Tratamiento |
|---|---|
| Mezclar notaciones en 5.1 a 5.4 (criterio de C4) | Notación fijada en `diagramas.py`, con un control de que cada figura use solo la suya |
| Casos de uso que citan requisitos inexistentes o cambian su texto | Control de que todo RF, RNF o RS citado exista en el catálogo de la fuente única |
| Repetir el ejemplo del texto en la Práctica 5 | Mbokaja, con situaciones que no están en los ejemplos (Work §7.4) |
| Que la solicitud de cambio del H2 se resuelva copiando un ejemplo | La nueva necesidad del H2 no está en el dossier ni en el buzón, y la rúbrica pide el análisis de impacto |
| Duplicar Algorítmica 3.º o Matemática Aplicada | Controles E del lote 1 y sin PERT ni grafos en 6.3 |

## 8. Decisiones que necesita Fernando

1. Aprobación del lote 1, una vez cerrada la auditoría.
2. Medidas del oficio. Se propone el perfil de Algorítmica 3.º (`../formato/ESPECIFICACION_OFICIO.md`).
3. Notación de los diagramas de proceso del Capítulo 5.
4. Autorización para construir el lote 2 después de la versión oficio del lote 1.

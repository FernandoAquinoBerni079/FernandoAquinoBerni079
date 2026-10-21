# Plan detallado del lote editorial 5 — Unidad V (Capítulos 14, 15 y 16)

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · 21 de octubre de 2026**

**Estado:** plan para auditar. **No se construye ningún capítulo hasta que Fernando lo autorice**, después de auditar este plan y la versión 1.1 del lote 4.
- No se escribió ningún capítulo de la Unidad V.
- No se modificaron los lotes 1, 2, 3 ni 4 para preparar este plan.
- No se generaron los 36 planes de clase ni se subió nada a Drive.

**Base:**
- el informe de Work v0.1 (`BTI3_Analisis_Diseno_Diagnostico_Propuesta_v0.1.pdf`, SHA-256 `3d4f5ab9…065069a`): §3, §4.2, §4.3, §5.1, §5.2, §6, §7.3, §7.4, §7.5 y §8.2;
- la distribución de 180 HC v2.1: `fase2_pilotos/C_informe_esfuerzo/v2_1/distribucion_36.csv` y `distribucion_28.csv`;
- el catálogo v1.1 (`lote_3/caso/diseno.py`), con 16 requisitos (RF-01 a RF-11, RNF-01 a RNF-03, RS-01 y RS-02), y las pruebas previstas P-01 a P-15 (`lote_2/caso/requisitos.py`);
- la versión 1.1 del lote 4:
  - los contratos OP-01 a OP-06 y OA-01 a OA-05;
  - los mensajes ME, MA y MV;
  - la base de proyecto en dos distribuciones;
  - los resultados de `lote_4/resultados_pruebas/`;
  - las incidencias de la Tabla 13.3;
  - la Práctica 13.

**Sobre el entorno:** HTML/CSS, PHP y SQLite siguen siendo una **referencia provisional**. Todas las pruebas automáticas corrieron solo en el contenedor de construcción (Linux 6.18.44, PHP 8.3.6, SQLite 3.45.1).

**Siguen pendientes, y el lote 5 no los declara satisfechos:**
- Windows;
- la instalación en un laboratorio escolar;
- la concurrencia real;
- el protocolo E-1 a E-12.

## 1. La Unidad V en Work

**Unidad V — Verificar, validar y mejorar.** Encuentros 27 a 32, **30 HC**.

**Resultado de la unidad (Work §5.1):** «Evidencia de pruebas, correcciones y aceptación».

**Índice de Work §6, textual:**

| Capítulo | Encuentros | Secciones | Cierre |
|---|---|---|---|
| 14. Probar con criterios y datos independientes | 27 y 28 | 14.1. Verificación, validación y aceptación. · 14.2. Casos normales, límites, excepciones y rechazos. · 14.3. Resultado esperado, resultado obtenido y evidencia. · 14.4. Cobertura de requisitos y reporte de defectos. | Práctica: elaborar y ejecutar una batería nueva de pruebas. |
| 15. Probar el sistema completo con usuarios | 29 y 30 | 15.1. Pruebas de integración y persistencia. · 15.2. Permisos, recuperación de datos y manejo de errores. · 15.3. Sesiones de uso y observación de dificultades. · 15.4. Aceptación por criterios acordados y prioridad de correcciones. | Práctica: revisión cruzada entre equipos con datos reservados para evaluación. |
| 16. Corregir y volver a comprobar | 31 y 32 | 16.1. Diagnóstico de incidencias e impacto de cambios. · 16.2. Corrección, revisión entre pares y regresión. · 16.3. Actualización de modelos, pruebas y documentación. · 16.4. Recuperación técnica y versión candidata. | Revisión de unidad V: evidencia de calidad y límites conocidos; H5. |

**El Capítulo 16 no tiene práctica en Work:** su cierre es el H5. Agregarle una práctica sería un complemento editorial (decisión abierta 5).

**Lo que dice Work sobre la unidad (textual):**
- **C9 (§4.2):**
  - Indicadores: «Ejecuta al menos doce casos identificados; registra esperado/obtenido; incluye seis rechazos o límites; corrige y vuelve a probar; realiza dos sesiones de uso».
  - Criterio: «La evidencia permite reproducir resultados; las correcciones responden a hallazgos y no introducen regresiones conocidas».
- **Condiciones mínimas de aceptación (§4.3):** «circuito de préstamo/devolución ejecutable; persistencia comprobada; ninguna pérdida de historial en las operaciones acordadas; rechazo de préstamo simultáneo del mismo ejemplar; evidencia de pruebas; instalación y restauración reproducibles. […] Si falta uno, se requiere recuperación específica».
- **Recuperación (§5.1):** «El encuentro 32 reserva recuperación técnica».
- **Trazabilidad (§7.3, ejemplo guía):** necesidad N-02 → RN-01 → RF-04 → diseño → aceptación → P-07 → «Resultado esperado/obtenido, consulta del estado final y explicación de la decisión técnica».
- **Transferencia (§7.4):** «Cada práctica debe exigir una decisión o desempeño nuevo […] Cambiar nombres conservando toda la solución no basta».

## 2. Capacidades y secuencia en HC

**Capacidades** (Work §4.2), rotuladas siempre como **propuestas para el programa institucional, no oficiales del MEC**:

| Capacidad | En la Unidad V |
|---|---|
| **C9.** Verifica y mejora la solución a partir de evidencia. | Núcleo de los seis encuentros. Doce casos o más, seis rechazos o límites, esperado y obtenido, corrección y nueva prueba, dos sesiones de uso. |
| **C8.** Integra un prototipo funcional con persistencia. | Encuentros 28, 29 y 32: el prototipo se prueba completo y se recupera lo que falte. |
| **C10.** Documenta, entrega y defiende el prototipo. | Solo en el Encuentro 29 (Work: «C8-C10»): la restauración probada. La entrega es de la Unidad VI. |
| **C3.** Especifica y prioriza requisitos verificables. | Encuentro 30: los criterios de aceptación del catálogo y la prioridad de las correcciones. |
| **C6.** Diseña la interacción y la arquitectura del prototipo. | Encuentro 30: las dificultades observadas en las sesiones de uso. |
| **C7.** Organiza y registra el trabajo colaborativo. | Encuentro 31 (Work: «C7-C9»): versiones, revisión entre pares y bitácora. |

**Secuencia (Work §5.2 y distribución v2.1, encuentros 27 a 32):**

| Enc. | Foco (Work §5.2) | Evidencia (Work §5.2) | Capacidades | HC (v2.1) |
|---:|---|---|---|---|
| 27 | Diseñar cobertura y datos independientes de prueba. | Matriz con resultados esperados y requisitos cubiertos. | C9 | V 5 |
| 28 | Ejecutar pruebas funcionales, límites y entradas inválidas. | Resultados obtenidos e incidencias reproducibles. | C8, C9 | V 5 |
| 29 | Probar integración, permisos, persistencia y restauración. | Evidencia del circuito completo y recuperación. | C8-C10 | V 5 |
| 30 | Realizar sesiones de uso y prueba de aceptación. | Observaciones de dos usuarios/roles y prioridades. | C3, C6, C9 | A 1, V 4 |
| 31 | Corregir problemas y repetir pruebas afectadas. | Registro de regresión; trazabilidad actualizada. | C7-C9 | P 2, V 3 |
| 32 | Recuperación técnica y revisión de unidad V. | H5: versión candidata con límites conocidos. | C8, C9 | P 2, V 1, E 2 |

Total: 30 HC (V 23, P 4, A 1, E 2).

**Estructura de los encuentros:** el taller de Work (§5.1), con 1 HC de problema y explicación, 3 de práctica y 1 de revisión. En esta unidad casi todas las HC son de verificación (V). La «práctica» del taller es diseñar, ejecutar y registrar pruebas. Los criterios de la v2.1 son: pruebas (27 a 29), aceptación y nueva prioridad (30), corrección y regresión (31), y recuperación técnica más la revisión del H5 (32).

**Adaptación a 28 encuentros (`distribucion_28.csv`):**

| 28 | Reúne | Foco | Ajuste de alcance (v2.1, textual) |
|---:|---|---|---|
| 20 | 27 | Cobertura y datos de prueba. | Sin cambios. |
| 21 | 28 | Pruebas funcionales y de límite. | Sin cambios. |
| 22 | 29 | Integración, permisos, persistencia y restauración. | Sin cambios. |
| 23 | 30 | Uso y aceptación. | Sin cambios. |
| 24 | 31+32 | Corrección, regresión; H5. | «Sin encuentro de reserva para recuperación técnica.» |

La unidad pasa de 30 a 25 HC. El encuentro 24 conserva las 2 HC de evaluación del H5, y la corrección se hace en P 2 y V 1. Cada capítulo llevará su recuadro «Si el calendario se acorta». La guía dirá qué hacer cuando un equipo necesite recuperación técnica y no hay encuentro de reserva: recuperación específica fuera del horario o con alcance reducido, registrada como tal.

## 3. Punto de partida: lo que deja la Unidad IV, y si es real o simulado

El lote 5 empieza con los resultados y las incidencias de la Unidad IV. Cada uno lleva su **condición**:
- **Real comprobado:** se ejecutó y se registró con su entorno.
- **Real reproducido:** se reprodujo sobre una copia temporal de la referencia docente al preparar este plan, con `lote_5_plan/reproducir_incidencias_u4.sh`. La salida, con el entorno, está en `reproduccion_incidencias_u4.txt`.
- **Simulado:** son datos de un caso ficticio, rotulados como tales.
- **Pendiente:** no se probó.

Nada simulado se presenta como real.

| Código | Qué es | Condición | Evidencia |
|---|---|---|---|
| R4-1 | Las ocho pruebas de la referencia docente y las seis de la base del estudiante, sin fallos | Real comprobado | `lote_4/resultados_pruebas/resumen.json`; contenedor de construcción, no una computadora escolar |
| R4-2 | Prueba de pedidos simultáneos (P-07, RI-02): 5 rondas, nunca dos préstamos activos | Real comprobado, solo en Linux | `referencia_docente__prueba_carrera.txt` |
| R4-3 | Ejemplo del Capítulo 10 (PA-01) y Práctica 11 (17 de 17) | Real comprobado | `reproduccion_ejemplo_capitulo_10.txt`, `practica_11_mbokaja.txt` |
| IN-02 | PT-08: después de un error, el formulario de alta de lector no recuerda los datos ni el tipo elegido | **Real reproducido** | `lote_5_plan/reproducir_incidencias_u4.sh` → `reproduccion_incidencias_u4.txt`: después de MV-04 el tipo vuelve a «Estudiante» |
| IN-03 | OP-05: en un mes sin préstamos, el informe muestra solo «Total 0», sin mensaje de vacío | **Real reproducido** | El mismo script: `informe.php?mes=2026-01` muestra solo «Total 0». Ya figuraba como hueco en la clave 3 del Encuentro 17 (lote 3): RF-09 sin mensaje de vacío |
| IN-01 | PT-07: con la fecha de referencia vacía, MV-08 «sin decir qué fecha usar» | **Simulado tal como está escrito**: el mensaje sí da el formato y un ejemplo | Se observó un detalle real menor: con la fecha vacía dice «La fecha  no es válida» (doble espacio, sin el valor). Se reformula como IN-01 bis, real |
| MI-01 a MI-07 | La semana de Mbokaja (Práctica 13): devolución no registrada, vencimiento del mismo día marcado como vencido | Simulado | Rotulado «datos simulados» en la Práctica 13 v1.1 |
| E-1 a E-12, Windows y concurrencia real | Prueba de campo | **Pendiente** | No hay acta de campo |

**Uso en los capítulos:**
- **Capítulo 14:** la matriz de pruebas parte de P-01 a P-15 y de los resultados R4-1 a R4-3. Las pruebas que solo corrieron en el contenedor quedan marcadas «comprobada en el entorno de construcción; pendiente en el del colegio».
- **Capítulo 16:** el ejemplo resuelto de corrección usa una incidencia **real reproducida** (IN-03, propuesta), no una simulada. El diagnóstico, el impacto, la corrección y la regresión se pueden ejecutar de verdad.
- **Los equipos:** usan sus propias incidencias del H4. La guía explica cómo rotular cada una (real, simulada o pendiente).

## 4. Datos de prueba independientes y datos reservados

Work pide «datos independientes de prueba» (Encuentro 27) y «datos reservados para evaluación» (Práctica 15). Se preparan dos conjuntos nuevos, en `lote_5/caso/datos_prueba_u5.py`:

1. **Conjunto de prueba del libro (DP).** Obras, ediciones, ejemplares, lectores y fechas que no aparecen en ningún ejemplo resuelto de los lotes 1 a 4. Códigos del rango 1000 a 1999 (OB-1xxx, ED-1xxx, EJ-1xxx y LE-1xxx), que no usa ningún lote anterior (los de la serie 05xx no sirven: EJ-0512 es un dato inicial), más fechas de otro mes.
   - Incluye los casos que piden los límites:
     - lector en su máximo (2 y 5) y uno por debajo;
     - vencimiento el mismo día de la fecha de referencia y el día anterior;
     - ejemplar inactivo con historial;
     - código con un dígito de menos y otro con uno de más;
     - comillas y comodines en la búsqueda («%», «_»);
     - lector que cambia de curso entre dos préstamos.
2. **Conjunto reservado (DR).** Va solo en la guía docente. El docente lo entrega en el Encuentro 30 para la revisión cruzada (Práctica 15) y como insumo de las variantes del H5.

**Controles previstos:** ningún código, título ni fecha de DP o DR coincide con los ejemplos resueltos, las prácticas anteriores, el banco del H4 o los datos iniciales de la base. DR no aparece en el libro ni en el cuaderno.

**Cómo se cargan:** en una **copia de práctica** de la base del equipo, como en la Práctica 11 v1.1, con un instalador de datos de prueba que no toca la base de la clase (decisión abierta 2). Si se prefiere no agregar código, los equipos los cargan con sus propias operaciones y la carga misma es la primera prueba.

## 5. Contratos, requisitos y pruebas por capítulo

La Unidad V **no cambia el diseño**:
- los contratos OP-01 a OP-06 y OA-01 a OA-05 siguen como están;
- también los mensajes ME-01 a ME-13 y los roles, con ME-12 solo en el ingreso y ME-13 para la falta de permiso;
- un cambio que aparezca al corregir se tramita como solicitud de cambio (Capítulo 6), con su versión.

| Capítulo | Qué se prueba | Requisitos | Pruebas previstas que se completan | Evidencia nueva |
|---|---|---|---|---|
| 14 | Cada operación con casos normales, límites, excepciones y rechazos | Los 16 del catálogo v1.1, con prioridad | P-01 a P-12, ampliadas a doce casos o más por equipo, seis de ellos rechazos o límites (C9) | Matriz de pruebas con esperado, obtenido, entorno y requisito; reportes de defecto |
| 15 | El circuito completo; permisos con las tres cuentas; respaldo y restauración; sesiones de uso; aceptación | RF-01 a RF-11, RNF-01 a RNF-03, RS-01 | P-13 (sin internet), P-14 (sesión de uso, RNF-01), E-11 y E-12 (restauración, C10), P-11 ampliada | Dos sesiones de uso con dos roles; criterios de aceptación verificados; correcciones priorizadas |
| 16 | Las correcciones y su regresión | Los afectados por cada corrección | El conjunto de regresión: las pruebas afectadas más un núcleo fijo (P-01, P-03, P-07, P-11 y la consulta de control) | Registro de regresión; trazabilidad requisito-defecto-corrección-prueba; versión candidata con límites conocidos |

**Lo que no se repite:**
- la matriz de trazabilidad del Capítulo 6 y la de coherencia del Capítulo 9 se amplían, no se rehacen;
- la sesión con usuarios simulados del Capítulo 8 (bocetos) no se repite: ahora se prueba el sistema funcionando.

**P-15 (licencias):** se revisa en el Capítulo 15 como parte de la aceptación de RS-02. La documentación de procedencia es de la Unidad VI.

## 6. Capítulo 14 — Probar con criterios y datos independientes (encuentros 27 y 28)

**Capacidades:** C9 (27); C8 y C9 (28).

| Sección | Contenido previsto |
|---|---|
| 14.1. Verificación, validación y aceptación. | Verificar es comprobar contra el requisito y el contrato. Validar es comprobar contra la necesidad del dossier. Aceptar es comprobar contra los criterios acordados. Ejemplo con la cadena de Work §7.3 (N-02 → RN-01 → RF-04 → P-07). |
| 14.2. Casos normales, límites, excepciones y rechazos. | Clases de casos y cómo se eligen desde las reglas: máximos 2 y 5, el vencimiento del mismo día, el formato de los códigos, los comodines en la búsqueda, la base ocupada (MV-09). Datos DP. |
| 14.3. Resultado esperado, resultado obtenido y evidencia. | El esperado se escribe antes de ejecutar. El obtenido se anota con el mensaje exacto, el estado de los datos (consulta de control) y el entorno. «Pendiente del entorno» no es «correcto». |
| 14.4. Cobertura de requisitos y reporte de defectos. | La matriz requisito-casos, con los huecos de cobertura. El reporte de defecto lleva pasos para reproducirlo, esperado, obtenido, gravedad, entorno, requisito y condición (real, simulado o pendiente). |

**Figuras previstas** (esquemas didácticos, sin notación nueva):
- clases de casos alrededor de un límite;
- de un caso de prueba a un reporte de defecto.

**Práctica 14 — Mbokaja: elaborar y ejecutar una batería nueva de pruebas.**
- **Datos nuevos:** una regla de Mbokaja que la Unidad IV no probó (por ejemplo, el plazo de siete días con un feriado anotado en el registro) y lectores y libros nuevos, cargados en la copia de práctica con la correspondencia fija de la Práctica 11.
- **Nivel 1:** completar la matriz de ocho casos de una operación, con su esperado.
- **Nivel 2:** ejecutar doce casos o más (seis rechazos o límites) y reportar los defectos que aparezcan, con su condición.
- **Nivel 3:** encontrar un hueco de cobertura en la matriz del equipo modelo y proponer los casos que faltan.
- **Para que se pueda hacer con el entorno entregado:** los niveles 1 y 2 se ejecutan en la copia de práctica. La guía trae una comprobación reproducible, como la de `lote_4/practica_11/`.

## 7. Capítulo 15 — Probar el sistema completo con usuarios (encuentros 29 y 30)

**Capacidades:** C8, C9 y C10 (29); C3, C6 y C9 (30).

| Sección | Contenido previsto |
|---|---|
| 15.1. Pruebas de integración y persistencia. | El recorrido E-6a de punta a punta con los datos DP. La persistencia después de reiniciar. P-13 sin internet. La consulta de control del estado final (Work §7.3). |
| 15.2. Permisos, recuperación de datos y manejo de errores. | La Tabla 11.3 ejecutada completa, con las tres cuentas. Respaldo y restauración probados (E-11, E-12): `restaurar.php` con la copia previa verificada (C10, solo restauración). Los fallos previsibles de la Tabla 12.3. |
| 15.3. Sesiones de uso y observación de dificultades. | Dos sesiones con dos roles (bibliotecaria y dirección, o lector en la consulta pública). Tarjetas de rol con tareas nuevas. El observador anota lo que ve y no ayuda. Las dificultades se registran como observaciones, no como opiniones (P-14, RNF-01). |
| 15.4. Aceptación por criterios acordados y prioridad de correcciones. | Cada criterio de aceptación del catálogo v1.1 se marca aceptado, no aceptado o pendiente, con su evidencia. Las correcciones se priorizan por gravedad, frecuencia y requisito afectado, dentro del alcance. Lo que no entra queda como límite conocido. |

**Práctica 15 — Revisión cruzada entre equipos con datos reservados para evaluación** (Work).
- Cada equipo prueba el prototipo de otro con el conjunto **DR**, que el docente entrega en el momento, y le entrega un reporte de defectos con su condición.
- **Niveles:**
  1. ejecutar los casos dados;
  2. diseñar casos propios con DR;
  3. priorizar los defectos recibidos y justificar la prioridad.
- **Sin datos personales reales.** Las sesiones de uso se hacen con compañeros en roles; si participa una persona de la biblioteca real, solo con autorización, como en el relevamiento de la Unidad I.

## 8. Capítulo 16 — Corregir y volver a comprobar (encuentros 31 y 32)

**Capacidades:** C7, C8 y C9 (31); C8 y C9 (32).

| Sección | Contenido previsto |
|---|---|
| 16.1. Diagnóstico de incidencias e impacto de cambios. | Reproducir la incidencia; distinguir el síntoma de la causa; localizar la capa (Figura 9.1); usar la matriz de trazabilidad para ver qué requisitos, contratos, pantallas y pruebas toca la corrección. |
| 16.2. Corrección, revisión entre pares y regresión. | Corrección mínima; otro integrante la revisa antes de integrarla; el conjunto de regresión se vuelve a ejecutar y se registra. Si una corrección rompe algo, se registra como regresión y se resuelve antes de la versión candidata. |
| 16.3. Actualización de modelos, pruebas y documentación. | Lo que cambia se actualiza con su versión: el catálogo (si hay una solicitud de cambio), el contrato, la tabla de mensajes, la prueba y la bitácora. La trazabilidad queda requisito-defecto-corrección-prueba. |
| 16.4. Recuperación técnica y versión candidata. | Encuentro 32: recuperación específica para el equipo al que le falta una condición mínima (Work §4.3). Versión candidata con sus límites conocidos: lo que no se corrigió, lo que no se probó y los pendientes del entorno. |

**Ejemplo resuelto central (propuesta):** **IN-03, real reproducida.** El informe de un mes sin préstamos no tiene mensaje de vacío.
- **Diagnóstico:** la causa está en el contrato de OP-05, que no previó el caso, y no en el código.
- **Impacto:** el contrato de OP-05, PT-09, la Tabla 8.6, P-09 y RF-09.
- **Corrección:** tramitarla como solicitud de cambio SC-02, con un mensaje nuevo para el informe vacío.
- **Regresión:** P-09 más el núcleo.
- **Dónde va el código corregido:** queda para decidir (decisión abierta 3). La base del lote 4 no se modifica.

**IN-02** (el formulario que pierde los datos después de un error, real reproducida) queda como ejemplo de corrección de presentación: no cambia contratos.

### H5 — Revisión de unidad V (Encuentro 32)

**Qué es, según Work:** «evidencia de calidad y límites conocidos; H5» (§6) y «H5: versión candidata con límites conocidos» (§5.2).

**Qué se demuestra:**
- la matriz de pruebas con doce casos o más (seis rechazos o límites), con esperado, obtenido y entorno;
- los reportes de defecto con su condición;
- las dos sesiones de uso;
- la aceptación por criterios;
- las correcciones con su regresión;
- la versión candidata con sus límites conocidos.

**Las condiciones mínimas de Work §4.3** se revisan una por una. Si falta una, recuperación específica en el mismo Encuentro 32 (2 HC: P 2) o, en el calendario de 28 encuentros, fuera del horario.

**Instrumento:** una rúbrica con el formato del H1 al H4.

| Criterio | Capacidad | Evidencia del equipo (60 %) | Evidencia individual (40 %) |
|---|---|---|---|
| Diseño y cobertura de pruebas | C9 | Matriz requisito-casos, huecos explicados | Elige los casos de una variante |
| Ejecución y evidencia reproducible | C9 | Esperado, obtenido, entorno, consulta de control | Reproduce un caso ante el docente |
| Integración, permisos, persistencia y recuperación | C8 | E-6a, Tabla 11.3, E-11 y E-12 | Explica una protección y su prueba |
| Uso y aceptación | C9 | Dos sesiones, criterios marcados, prioridades | Justifica una prioridad |
| Corrección y regresión | C9 | Registro de regresión, trazabilidad defecto-corrección-prueba | Diagnostica la variante y nombra la regresión |
| Versión candidata y límites conocidos | C8 | Versión con límites, pendientes del entorno separados | Distingue falla, límite y pendiente |

**Reglas de la rúbrica:**
- cuatro niveles (Sólido, Logrado, En desarrollo e Inicial);
- 60/40 como **propuesta editorial** (Work §4.3);
- la ausencia de evidencia (AE) se registra aparte;
- planilla de registro;
- **un pendiente del entorno no se cuenta como falla del equipo.**

**Evidencia individual:** cada estudiante recibe un reporte de defecto nuevo, del banco V5, y explica:
- la causa probable;
- la capa;
- el impacto;
- la corrección mínima;
- las pruebas de regresión.

Las variantes no están en el dossier, el buzón, D3, los bancos del H3 y el H4 ni las prácticas.

## 9. Evaluaciones de los capítulos

Igual que en los lotes anteriores:
- una evaluación opcional por capítulo, de 15 puntos y en una página;
- texto base de otra situación ficticia de Work §7.4 (equipos audiovisuales, talleres, soporte o espacios), sin repetir las ya usadas;
- semillas `ADS3-L5-C14` a `C16`, con tres letras distintas como mínimo en las claves de opción múltiple.

En el Capítulo 16, el instrumento principal es el H5.

## 10. Dependencias técnicas

| Dependencia | Estado | Qué hace falta |
|---|---|---|
| Base de proyecto del lote 4 (dos distribuciones) | Lista; no se modifica | Nada. Las correcciones de los equipos van en su propia base. |
| Copia de práctica y correspondencia fija (Práctica 11 v1.1) | Lista | Se reutiliza para las Prácticas 14 y 15. |
| Conjuntos DP y DR | Nuevos | `lote_5/caso/datos_prueba_u5.py`, más el control de independencia. Cargador: decisión abierta 2. |
| Plantillas: matriz de pruebas, reporte de defecto, registro de regresión, acta de aceptación | Nuevas | Tablas en el libro y el cuaderno; versión imprimible en la guía. |
| Ejecución de las pruebas | Existe | Manual, desde las pantallas, con su registro. `prueba_mis_operaciones.php` como regresión automática del núcleo. La automatización no es obligatoria (Laboratorio 3.º, p. 58: TDD e integración continua; se articula, no se repite). |
| Restauración (E-12, C10 en el Encuentro 29) | `restaurar.php` existe y se probó en Linux | Ejecutarla en el colegio: pendiente del entorno. |
| P-07 en Windows | Pendiente | Protocolo de la guía del lote 4. En la matriz, «pendiente del entorno». |
| Ejemplo IN-03 corregido | Nuevo, si se aprueba | Dónde vive el código corregido: decisión abierta 3. |

## 11. Qué no repetir y con quién coordinar

- **Laboratorio 3.º, p. 58** (metodologías, TDD, integración continua): se aplican iteraciones, revisión y regresión. No se presenta una unidad de TDD ni de herramientas de pruebas automáticas.
- **Algorítmica 3.º:** no se repiten ejercicios de consultas ni de normalización. Las consultas de control son de una línea, al servicio de la evidencia.
- **Capítulo 8 (sesión con bocetos)** y **Capítulo 6 (trazabilidad):** se amplían, no se rehacen.
- **Coordinación:** antes del Encuentro 29, el docente confirma con Laboratorio que la restauración se puede hacer en los equipos (E-12). Si no se puede, se registra como pendiente del entorno.

## 12. Fuente común y entregables

**Fuente** (sin tocar los módulos de los lotes 1 a 4):
- `lote_5/caso/verificacion.py`, con:
  - la matriz de pruebas del equipo modelo;
  - los reportes de defecto con su condición (real, simulado o pendiente);
  - las sesiones de uso;
  - el acta de aceptación;
  - el registro de regresión;
  - el banco V5.
  Lee `lote_3/caso/diseno.py`, `lote_4/caso/construccion.py` y `lote_4/resultados_pruebas/`.
- `lote_5/caso/datos_prueba_u5.py`: los conjuntos DP y DR.
- `lote_5/caso/mbokaja_u5.py`: los datos nuevos de las Prácticas 14 y 15.
- `lote_5/build/cap14.py` a `cap16.py`: con los mismos atributos que los capítulos anteriores (lo comprueba `tomo.py`).

**Entregables, como en los lotes 2 a 4:**
- libro, guía docente con solucionario y cuaderno de prácticas, en DOCX y PDF;
- resultados de las pruebas con su entorno;
- informe, manifiesto SHA-256 y láminas.

**Extensión estimada en oficio O3:** libro de 32 a 40 págs.; guía de 16 a 22; cuaderno de 6 a 10. Es una estimación: no se rellena para alcanzarla.

## 13. Controles nuevos previstos

1. **Índice de Work:** los títulos, las secciones, los cierres, los Encuentros 27 a 32 y las capacidades de §5.2, textuales.
2. **Condición de cada incidencia:** cada incidencia y resultado lleva su condición (real comprobado, real reproducido, simulado o pendiente). Ninguna simulada sin rótulo. Las «reales reproducidas» se vuelven a reproducir automáticamente en cada construcción, sobre una copia de la referencia.
3. **Independencia de datos:** DP y DR no coinciden con ejemplos, prácticas ni bancos anteriores. DR no figura en el libro ni en el cuaderno.
4. **C9:** la matriz del equipo modelo tiene doce casos o más, seis de ellos rechazos o límites. Cada caso tiene requisito, esperado, obtenido y entorno.
5. **Permisos y persistencia:** la Tabla 11.3 se ejecuta completa (sin sesión, bibliotecaria y dirección); se comprueba la persistencia después de reiniciar; la restauración se registra con su entorno.
6. **Regresión:** cada corrección tiene su conjunto de regresión y su resultado. Trazabilidad requisito-defecto-corrección-prueba sin huecos.
7. **Entorno:** ningún resultado se declara válido para todos los colegios. Los pendientes del entorno (Windows, campo y concurrencia) siguen pendientes.
8. **Lotes 1 a 4 intactos:** git y los manifiestos SHA-256.
9. **Impresión:** los controles 1 a 7 de los lotes 3 y 4.

## 14. Decisiones abiertas para Fernando

1. **Ejemplo central del Capítulo 16:** ¿se usa IN-03 (real reproducida: informe sin mensaje de vacío, con la solicitud de cambio SC-02 y un mensaje nuevo) o IN-02 (real reproducida: formulario que pierde los datos, sin cambio de contrato)?
2. **Datos de prueba DP:**
   - ¿se entrega un cargador que los instala en una copia de práctica sin tocar la base de la clase?
   - ¿o los equipos los cargan con sus operaciones, y la carga es la primera prueba?
3. **Código corregido del ejemplo:**
   - ¿se publica una referencia docente v2 en `lote_5/proyecto/` (derivada, sin tocar la del lote 4)?
   - ¿o el ejemplo queda solo en el libro y la guía, como diagnóstico y diseño de la corrección?
4. **Sesiones de uso (Encuentro 30):** ¿solo con compañeros en roles, o también con una persona de la biblioteca real si la institución lo autoriza?
5. **Capítulo 16:** Work no prevé una práctica (el cierre es el H5). ¿Se agrega un complemento editorial breve, o el H5 alcanza?
6. **Calendario de 28 encuentros:** al no haber encuentro de reserva, ¿la recuperación técnica se hace fuera del horario o reduciendo el alcance de la versión candidata?

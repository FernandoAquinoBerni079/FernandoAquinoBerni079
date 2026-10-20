# Plan detallado del lote editorial 3 — Unidad III (Capítulos 7, 8 y 9)

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · 20 de octubre de 2026**

**Estado:** plan para aprobar. **No se construye nada hasta que Fernando lo autorice.**
- No se escribió ningún capítulo de la Unidad III.
- No se modificó ningún archivo de los lotes 1 y 2.
- La única fuente actualizada en esta etapa es el generador del plan anual (decisión 4 de Fernando, §9).

**Base:**
- lote 2 aceptado como versión de referencia (commit `733932c`);
- catálogo v1.1 del caso Arapoty (`lote_2/caso/requisitos.py`);
- informe de Work v0.1, SHA-256 `3d4f5ab9…065069a`: §3 (articulación), §4.2 (C5, C6 y C9), §4.3, §5.2 (encuentros 13 a 18), §6 (índice), §7.2, §7.4, §7.5 y §8.2;
- distribución de 180 HC v2.1 (36 y 28 encuentros);
- libro de Algorítmica 3.º de la colección (`algoritmica_3_esencial/`), leído para no duplicarlo (§2).

## 1. La Unidad III en Work

**Unidad III — Diseñar una solución coherente.** Encuentros 13 a 18, 30 HC.

**Resultado de la unidad (Work §5.1):** «Modelo de datos, interacción y arquitectura revisados».

**Índice de Work §6, textual:**

| Capítulo | Encuentros | Secciones | Cierre |
|---|---|---|---|
| 7. Datos que representan las reglas | 13 y 14 | 7.1. Recuperación aplicada de modelos de Algorítmica. · 7.2. Obra/edición, ejemplar, lector y préstamo: identidad y responsabilidad. · 7.3. Relaciones, restricciones, historial y diccionario de datos. · 7.4. Revisión de normalización con ejemplos del proyecto. | Práctica: justificar el modelo frente a pérdida, devolución y duplicación de solicitudes. |
| 8. Diseñar para las tareas de las personas | 15 y 16 | 8.1. Recorridos de usuario y organización de pantallas. · 8.2. Bocetos y prototipo de baja fidelidad. · 8.3. Estados vacío, carga, error y confirmación. · 8.4. Etiquetas, navegación por teclado y lectura comprensible. | Práctica: observar el uso del boceto y modificarlo con evidencia. |
| 9. Arquitectura y revisión del diseño | 17 y 18 | 9.1. Presentación, reglas de negocio y persistencia. · 9.2. Responsabilidades, entradas, salidas y contratos de operaciones. · 9.3. Entorno, dependencias y decisiones técnicas justificadas. · 9.4. Coherencia entre requisitos, datos e interfaces. | Evaluación integradora de la primera etapa: defensa y corrección del dossier; H3. |

## 2. Capacidades y secuencia en HC

**Capacidades** (Work §4.2, rotuladas siempre como propuestas para el programa institucional, no oficiales del MEC):

| Capacidad | Indicadores de Work | Criterio de Work |
|---|---|---|
| **C5.** Justifica el modelo de información y sus reglas de integridad. | Distingue obra/edición y ejemplar; vincula cada préstamo a un ejemplar; justifica claves y relaciones; detecta una anomalía y corrige el diseño. Evidencia: modelo y diccionario. | El modelo representa las reglas acordadas, conserva el historial y evita referencias inválidas y préstamos activos duplicados. |
| **C6.** Diseña la interacción y la arquitectura del prototipo. | Traza tres recorridos; muestra estados vacío, error y éxito; identifica presentación, reglas y datos; justifica una decisión con alternativas. Evidencia: bocetos y esquema de arquitectura. | El diseño permite completar las tareas, es legible y es coherente con el alcance, los datos y el entorno. |
| **C9.** Verifica y mejora la solución a partir de evidencia. | En esta unidad: revisión del modelo con ejemplos y contraejemplos (Encuentro 14) y sesión con usuarios simulados (Encuentro 16). | — |
| **C1 a C7** | Se evalúan juntas en el H3 (Encuentro 18) | Dossier consistente y evidencia individual |

**Secuencia (Work §5.2 y distribución v2.1):**

| Enc. | Foco (Work §5.2) | Evidencia (Work §5.2) | Capacidades | HC |
|---:|---|---|---|---|
| 13 | Revisar antecedentes de Algorítmica y modelar el dominio | Obras/ediciones, ejemplares, lectores y préstamos | C5 | D 5 |
| 14 | Validar integridad, historial y diccionario de datos | Revisión del modelo con ejemplos y contraejemplos | C5 | D 4, V 1 |
| 15 | Diseñar recorridos y bocetos de pantallas | Tres tareas completas en prototipo de baja fidelidad | C6 | D 5 |
| 16 | Revisar accesibilidad, mensajes y estados con usuarios simulados | Registro de problemas y bocetos corregidos | C6, C9 | D 3, V 2 |
| 17 | Diseñar responsabilidades, conexiones y entorno de ejecución | Esquema de arquitectura y decisión técnica | C5, C6 | D 5 |
| 18 | Evaluación intermedia: defender análisis y diseño; corregir | H3: dossier consistente y evidencia individual | C1 a C7 | D 1, E 4 |

**Estructura de cada encuentro:** el taller de Work, con 1 HC de problema y explicación, 3 de práctica y 1 de revisión. En el 16, la revisión es la sesión con usuarios simulados (2 HC de verificación). En el 18, la defensa ocupa 4 HC de evaluación y 1 HC de corrección del dossier.

**Adaptación a 28 encuentros (v2.1):**
- se unen el 15 y el 16: tres recorridos en baja fidelidad y una sola sesión de revisión entre equipos;
- el 13, el 14, el 17 y el 18 no cambian.

El Capítulo 8 lleva su recuadro «Si el calendario se acorta» con esa fusión.

## 3. Qué no repetir de Algorítmica 3.º y qué profundizar

**Lo que ya enseña Algorítmica 3.º** (leído en `algoritmica_3_esencial/build/`):
- **Unidad 2:** base de datos, claves e integridad referencial, con prácticas de biblioteca: Socios, Libros y Préstamos (Prácticas 5, 6, 8, 9 y 10). La Práctica 9 calcula una «Eliminar en cascada» sobre Socios–Préstamos.
- **Unidad 3:** modelo entidad-relación en notación clásica (entidad, rombo, atributos en elipse, cardinalidad), con un club, unos talleres y una librería; paso a tablas; anomalías, dependencia funcional y 1FN a 3FN.
- **Unidad 4:** Access y consultas.
- **El ejemplar aparece una sola vez:** en el desafío de la Práctica 8, como tabla Ejemplares con el ISBN como dato.

**Tratamiento en este lote** (Work §3: «justificar decisiones del modelo y su correspondencia con reglas; no capítulos completos repetidos sobre BD y formas normales»):

| Tema | Algorítmica 3.º | Capítulo 7 de este libro |
|---|---|---|
| Notación entidad-relación | La enseña | **Se recupera, no se enseña.** 7.1 es una ficha de recuperación de una página, con remisión a sus clases, y una actividad diagnóstica breve. La guía trae el acuerdo de Work: antes del Encuentro 13, Algorítmica informa qué ya trabajó. |
| Libro y ejemplar | Una tabla Libros; el ejemplar, como desafío | **Núcleo del capítulo.** Obra (título y autor), edición (editorial y año), ejemplar físico (código y estado) y préstamo de un ejemplar. Se muestra por qué la falta de esa distinción causa los problemas del dossier: E4-L2 (no se sabe qué ejemplar vuelve) y E4-L4 (doble préstamo). |
| Borrado | «Eliminar en cascada», calculado | **Se contrasta con las reglas del caso:** RN-05 (la devolución no borra) y RN-06 (se inactiva, no se borra). El modelo conserva el historial: los préstamos no se borran nunca. |
| Normalización | Teoría de 1FN a 3FN | **Solo revisión aplicada (7.4)** sobre datos del proyecto: la línea del cuaderno (D1-A4) y el informe sin curso (D2-8). No se repiten las definiciones de las formas normales. |
| Claves | Candidatas, principal y foránea | Se usan para justificar decisiones: por qué el código del ejemplar y no el ISBN, o por qué un código interno del lector y no la cédula (privacidad, RNF-03). |

**Controles que se agregan al verificador del lote:**
- ninguna persona, título, archivo ni tecnología del caso de Algorítmica 3.º (`PROHIBIDOS_ALGORITMICA`, ya vigente);
- no se usan los nombres de sus tablas («Socios», «Libros» como entidad única);
- no hay una sección sobre formas normales;
- la cascada aparece solo como contraste con RN-05 y RN-06.

## 4. Dependencias del catálogo v1.1

La Unidad III tiene que **diseñar para el catálogo v1.1, no para la v1.0**: RN-02 modificada y RF-11 nuevo (SC-01, Capítulo 6). Cada requisito tiene que tener su respuesta en el modelo de datos, en la interfaz y en la arquitectura. El control 9.4 lo comprueba.

| Requisito o regla | Capítulo 7: datos | Capítulo 8: interfaz | Capítulo 9: arquitectura |
|---|---|---|---|
| RF-01, RF-02 (préstamo y vencimiento según el «plazo vigente») | Préstamo de un ejemplar a un lector, con fechas. El plazo vigente es un **dato** (parámetro), no un número en el programa. | Recorrido «Registrar préstamo» (CU-01) | Operación `registrar préstamo`: contrato con precondiciones y errores |
| RF-03 (devolución identificando el ejemplar) | El préstamo referencia al ejemplar, no a la obra (resuelve E4-L2) | Recorrido «Registrar devolución» (CU-02) | Operación `registrar devolución` |
| RF-04, RN-01 (un préstamo activo por ejemplar) | Restricción: a lo sumo un préstamo sin devolución por ejemplar. Contraejemplo en el Encuentro 14. | Estado de error del flujo 5a | Regla en la capa de reglas, protegida también en la persistencia. La decisión de dónde, con su razón, se registra en 9.1. |
| RF-05, RN-02 v1.1 y RF-11 (máximo según el tipo de lector) | Tipo de lector (RF-11). El máximo por tipo es un parámetro. | Mensaje del flujo 4b con el máximo que corresponde | Regla que lee el parámetro: cambiar la regla no obliga a reprogramar |
| RF-06, RN-04 y RF-10, RN-06 (inactivos sin borrar) | Estado activo o inactivo del lector y del ejemplar; sin borrado físico | Estado de error del flujo 4a; pantalla de inactivación (CU-05) | Ninguna operación borra registros con historial |
| RN-05 (la devolución no borra) | Historial: el préstamo se cierra con su fecha | Confirmación de la devolución | El contrato de devolución no elimina nada |
| RF-07, RNF-03 (consulta pública sin datos personales) | Disponibilidad **derivada** (ejemplares sin préstamo activo), no guardada | Recorrido «Consultar disponibilidad» (CU-03) y estados vacío y «0 disponibles» | La consulta pública solo usa la obra y los conteos |
| RF-08 (quién tiene cada ejemplar) | Consulta que une préstamo activo, ejemplar y lector | Lista de préstamos activos | Operación de consulta con permiso de la bibliotecaria |
| RF-09 (informe mensual por curso) | El curso del lector es obligatorio (D2-8: seis préstamos sin curso) | Pantalla del informe (CU-04) | Consulta con un mes como parámetro |
| RNF-01 (uso sin ayuda) | — | Etiquetas, mensajes y sesión con usuarios simulados (Encuentro 16) | — |
| RNF-02 (solo la bibliotecaria registra) | Cuenta y rol, si se implementan sesiones (Work §7.2) | Pantallas públicas separadas de las de la bibliotecaria | Permisos comprobados en el servidor, no solo en la pantalla (Work §7.5) |
| RS-01, RS-02 (sin internet y sin costo) | — | — | Decisión técnica de 9.3, con estas dos restricciones como excluyentes |

**Lo que queda fuera del diseño del núcleo:**
- la renovación (N-13, postergada en 6.1);
- la reserva del plan lector (N-12);
- el estado «en reparación» (B-02) y la regla RN-07, que en la Práctica 4 son ejercicios, no decisiones del caso.

Si la auditoría prefiere incluir alguno, entra por solicitud de cambio, como SC-01.

## 5. Capítulo 7. Datos que representan las reglas (encuentros 13 y 14)

**Capacidad:** C5; C9 en la revisión del Encuentro 14.

| Sección | Contenido previsto |
|---|---|
| 7.1. Recuperación aplicada de modelos de Algorítmica. | Ficha de recuperación de una página: entidad, atributo, clave, relación y cardinalidad, con remisión a Algorítmica 3.º (Clases 8, 9 y 11 a 15). Una actividad diagnóstica con datos del dossier. La guía da las dos rutas de Work §3: el curso ya trabajó el modelado, o hay que entregar un esquema inicial explicado. |
| 7.2. Obra/edición, ejemplar, lector y préstamo: identidad y responsabilidad. | Qué identifica a cada cosa y quién responde por ella. **Ejemplo resuelto:** tres ejemplares de una lectura obligatoria (E2-L2) muestran por qué el préstamo tiene que ser de un ejemplar. El lector con un código interno, sin la cédula (RNF-03). El tipo de lector (RF-11). |
| 7.3. Relaciones, restricciones, historial y diccionario de datos. | Relaciones y cardinalidades del núcleo. Restricciones que salen de las reglas (RN-01, RN-02 v1.1, RN-04 a RN-06). Datos derivados frente a guardados (la disponibilidad). Parámetros (plazo y máximo vigentes). **Diccionario:** cada campo con su significado, obligatoriedad, ejemplo y requisito que lo pide. **Encuentro 14:** revisión con ejemplos y contraejemplos (C9). |
| 7.4. Revisión de normalización con ejemplos del proyecto. | Se aplica a la línea del cuaderno (D1-A4), que mezcla lector, curso, título y fecha, y al informe con préstamos sin curso (D2-8). Cada anomalía (repetición, actualización y borrado) se lee en los datos del caso y se corrige el diseño. Sin teoría de formas normales. |

**Figuras previstas:**
- **7.1:** modelo del núcleo en la notación de Algorítmica 3.º. Los atributos van en el diccionario y no en el diagrama, para que se pueda leer.
- **7.2:** obra, edición y ejemplares, con tres ejemplares de un mismo título.
- **7.3:** historial de un ejemplar: préstamos sucesivos, ninguno borrado.

**Práctica 7 — Mbokaja: justificar el modelo frente a pérdida, devolución y duplicación de solicitudes.** Datos nuevos de `mbokaja_u3.py`:
- tres ejemplares por libro de lectura obligatoria;
- un libro **perdido** que se repone con otro (norma M-N5);
- fichas con devoluciones sin anotar (V-11);
- dos voluntarios de 9.º que el mismo miércoles cargan el **mismo préstamo dos veces** (M-F5).

**Niveles:**
1. modelo con obra y ejemplar, y explicación de dónde se registra la pérdida sin perder el historial;
2. además, el diccionario y la restricción contra la doble carga;
3. además, el caso de los docentes con plazo de un mes (si la Práctica 6 aceptó MC-1) y su impacto en el modelo.

**Decisión nueva frente a Arapoty:** el ejemplar perdido y su reposición. Es un estado y un vínculo nuevos, que no aparecen en ningún ejemplo.

## 6. Capítulo 8. Diseñar para las tareas de las personas (encuentros 15 y 16)

**Capacidad:** C6; C9 en la sesión del Encuentro 16.

| Sección | Contenido previsto |
|---|---|
| 8.1. Recorridos de usuario y organización de pantallas. | Los tres recorridos de C6 salen de los casos de uso prioritarios del Capítulo 5: registrar un préstamo, registrar una devolución y consultar la disponibilidad. Cada paso de la plantilla se convierte en una pantalla o una acción. **Mapa de navegación** entre pantallas, con las públicas separadas de las de la bibliotecaria (RNF-02, RNF-03). |
| 8.2. Bocetos y prototipo de baja fidelidad. | Bocetos de cajas grises, sin colores ni logotipos: qué va en cada pantalla y por qué, con el requisito que lo pide. Prototipo en papel que se recorre con el dedo. |
| 8.3. Estados vacío, carga, error y confirmación. | Cada flujo alternativo de CU-01 a CU-03 se convierte en un estado con su mensaje. Ejemplos: 4a lector inactivo, 4b máximo del tipo de lector, 5a ejemplar ya prestado, 2a de la devolución sin préstamo activo, y «0 disponibles» sin datos de lectores. **Regla del mensaje:** qué pasó, por qué y qué se puede hacer. |
| 8.4. Etiquetas, navegación por teclado y lectura comprensible. | Etiqueta visible en cada campo, orden de tabulación, foco visible, sin depender del color, frases cortas y palabras de la bibliotecaria («ejemplar», no «ID»). Lista de verificación breve, propia, sin citar normas que no se puedan verificar. |

**Sesión del Encuentro 16:**
- con usuarios simulados, mediante tarjetas de rol en la guía;
- con registro de los problemas observados y los bocetos corregidos (evidencia de Work);
- RNF-01 da la meta observable: completar la tarea sin ayuda.

**Figuras previstas:**
- mapa de navegación;
- bocetos de las tres tareas;
- lámina de los cuatro estados de una misma pantalla.

**Práctica 8 — Mbokaja: observar el uso del boceto y modificarlo con evidencia.**
- **Usuarios distintos:** el encargado, un **voluntario de 9.º** (un estudiante que usa la pantalla de registro, lo que plantea qué puede hacer) y una estudiante del turno mañana que consulta.
- **Para quien no puede hacer la sesión real:** la práctica trae un registro de observación (OBS-1 a OBS-6).

**Niveles:**
1. clasificar las observaciones y corregir un boceto;
2. además, escribir los mensajes de error y de confirmación;
3. además, decidir qué ve y qué no ve el voluntario, justificado con MN-05 (datos de menores).

## 7. Capítulo 9. Arquitectura y revisión del diseño (encuentros 17 y 18)

**Capacidades:** C5 y C6 (Encuentro 17); C1 a C7 (H3, Encuentro 18).

| Sección | Contenido previsto |
|---|---|
| 9.1. Presentación, reglas de negocio y persistencia. | Tres responsabilidades separadas: qué muestra, qué decide y qué guarda. Dónde vive cada regla del caso: las reglas se comprueban en el servidor, no solo en la pantalla (Work §7.5). La restricción de RN-01 se protege también en la persistencia. |
| 9.2. Responsabilidades, entradas, salidas y contratos de operaciones. | Contrato de cada operación del núcleo: entradas, precondiciones, salidas, poscondiciones y errores, cada uno ligado al requisito y al flujo alternativo. **Ejemplo resuelto:** `registrar préstamo`, desde CU-01, RF-04 a RF-06 y RN-02 v1.1. |
| 9.3. Entorno, dependencias y decisiones técnicas justificadas. | **Registro de decisión** (contexto, opciones, decisión, consecuencias y requisitos que la condicionan), con RS-01 y RS-02 como excluyentes. **Sin matriz de pesos**, que es la técnica de la Práctica 4 de Algorítmica 3.º. El ejemplo es la ruta de Work §7.5 (HTML y CSS, PHP y SQLite, ejecución local), presentada como opción editorial **a verificar en los equipos de la institución**: la institución puede usar el entorno que ya domine. |
| 9.4. Coherencia entre requisitos, datos e interfaces. | Matriz de coherencia: la Tabla 6.2 del Capítulo 6 ampliada con entidad y campo, pantalla y estado, y operación. Se buscan huecos y contradicciones. **Ejemplo:** el impacto de SC-01 en las tres capas. |

**Figuras previstas:**
- esquema de las tres capas con las operaciones del núcleo;
- contrato de `registrar préstamo` como recuadro de texto, no como diagrama.

**Evaluación integradora de la primera etapa — H3: dossier consistente y evidencia individual (Encuentro 18)**
- **Qué se defiende:** el dossier completo de las Unidades I a III, en sus versiones vigentes:
  - problema y alcance;
  - relevamiento;
  - catálogo v1.x;
  - modelos funcionales;
  - modelo de datos y diccionario;
  - bocetos y estados;
  - arquitectura, contratos y decisión técnica;
  - matriz de coherencia.
- **Evidencia individual:** cada estudiante resuelve una **variante** que propone el docente (por ejemplo, un cambio de regla) y explica qué cambia en los datos, en la pantalla y en la operación. La guía trae un banco de variantes que no están en el dossier, en el buzón, en D3 ni en las prácticas.
- **Instrumento:** rúbrica con el formato del H1 y el H2:
  - seis criterios (relevamiento y alcance C1 y C2; requisitos C3; modelos funcionales C4; datos C5; interacción y arquitectura C6; versiones y trabajo del equipo C7);
  - cuatro niveles;
  - 60 % de evidencia del equipo y 40 % individual (propuesta editorial);
  - la ausencia de evidencia, aparte;
  - planilla de registro.
- **Después de la defensa:** el equipo corrige el dossier y registra la nueva versión (1 HC de diseño).

**Práctica 9 (a decidir, §10):** Work no prevé una práctica en el Capítulo 9; el lote 2 sí agregó la Práctica 6 en el Capítulo 6. La propuesta es una práctica breve con Mbokaja:
- **Datos nuevos:** la computadora donada (M-F7) y el encargado con menos horas (M-F4).
- **Pedido:**
  - el contrato de `registrar devolución` con el libro dañado (MS-1);
  - dónde vive la regla de reposición (M-N5);
  - una decisión técnica en la que pese quién va a mantener la computadora.

## 8. Notaciones del lote (a fijar en `diagramas.py` antes de escribir)

Se mantiene el criterio de C4 del Capítulo 5: una notación por figura, con su leyenda y su registro de símbolos.

| Figura | Notación | Símbolos | Lo que no se mezcla |
|---|---|---|---|
| Modelo de datos (7.1) | **Entidad-relación en la notación clásica de Algorítmica 3.º** | Entidad (rectángulo), relación (rombo) y cardinalidad (1, N). Los atributos van en el diccionario. | Sin símbolos UML ni flechas de flujo |
| Historial y obra/ejemplar (7.2 y 7.3) | Esquema didáctico, como la Figura 2.1 | Cajas y líneas de tiempo | Sin rombos ni cardinalidades |
| Mapa de navegación (8.1) | **Mapa de navegación** (nuevo) | Pantalla (rectángulo con nombre), transición (flecha rotulada con la acción del usuario, con verbo), inicio (punto) y zona con permiso (marco punteado con rol) | No usa los flujos del diagrama de contexto, que llevan sustantivos, ni los carriles de actividades |
| Bocetos y estados (8.2 y 8.3) | Boceto de baja fidelidad | Cajas grises, campos con etiqueta, botones y zona de mensaje | Sin colores de marca ni capturas de software real |
| Capas (9.1) | Esquema de capas | Tres bandas (presentación, reglas y persistencia) y operaciones como flechas entre bandas | Sin símbolos UML de componentes |

**Leyendas:** cada notación nueva tiene su tabla de símbolos dibujados, en el libro y en la guía, con los errores frecuentes. Es la misma solución del Capítulo 5.

## 9. Fuente común y entregables

**Fuente única ampliada** (sin tocar los módulos de los lotes 1 y 2):
- **`lote_3/caso/diseno.py`:**
  - entidades, relaciones, restricciones con su regla o requisito, parámetros y diccionario;
  - recorridos, pantallas, estados y mensajes, derivados de las plantillas de los casos de uso;
  - capas, operaciones y contratos;
  - registro de decisión técnica;
  - banco de variantes del H3.
- **`lote_3/caso/mbokaja_u3.py`:** datos de las Prácticas 7 a 9.
- **`lote_3/build/cap7.py` a `cap9.py`:** mismos atributos que los capítulos 1 a 6 (lo comprueba `tomo.py`, que se amplía).
- **Maqueta, perfil y controles:**
  - la maqueta del lote 1 y el perfil O3 de `lote_2/build/oficio.py`;
  - el control de filas de la candidata O3;
  - el verificador por bloques del lote 2, extendido.

**Controles nuevos previstos:**
1. **Índice de Work:** títulos y secciones textuales, encuentros, capacidades de §5.2 y H3.
2. **No duplicar Algorítmica 3.º** (§3).
3. **Obra y ejemplar:** todo préstamo referencia a un ejemplar; la disponibilidad es derivada; ninguna operación borra registros con historial.
4. **Diccionario:** cada campo cita un requisito, una regla o una necesidad que existe.
5. **Catálogo v1.1** (§4): cada requisito tiene su respuesta en datos, interfaz y arquitectura, o «no aplica» con razón.
6. **Casos de uso:** cada flujo alternativo de CU-01 a CU-03 tiene su estado y su mensaje en el Capítulo 8, y su error en el contrato del Capítulo 9.
7. **Notaciones:** sin mezcla en ninguna figura, con leyenda completa.
8. **Decisión técnica:** cita RS-01 y RS-02 y no usa pesos.
9. **Impresión:** todas las filas, párrafos y palabras contra el PDF, evaluaciones en página propia, márgenes espejados y láminas de revisión visual.

**Entregables** (igual que el lote 2):
- libro del estudiante de la Unidad III;
- guía docente con solucionario (claves, listas de cotejo, tarjetas de rol del Encuentro 16, rúbrica y planilla del H3 y banco de variantes);
- cuaderno de prácticas;
- DOCX, PDF, scripts, informe y manifiesto SHA-256.

**Extensión estimada en oficio O3:**
- libro, entre 38 y 46 págs.;
- guía, entre 16 y 22;
- cuaderno, entre 7 y 10.

**Evaluaciones opcionales:** 15 puntos cada una, entera en una página, con semillas nuevas (`ADS3-L3-C7`, `-C8` y `-C9`). Cada una se basa en una situación de otro dominio, que no se usó en el libro ni en Algorítmica 3.º:
- **Capítulo 7:** reserva de espacios del colegio (Work §7.4: superposición de franjas y cancelación).
- **Capítulo 8:** pedido de constancias en la secretaría (formulario y estados).
- **Capítulo 9:** inventario del laboratorio de ciencias (capas y contrato).

**Plan anual (decisión 4, ya hecha):**
- **Qué cambió:** `plan_anual/plan_anual_preliminar.py` ahora importa las fichas de los Capítulos 4 a 6 del lote 2 y lee sus indicadores, títulos, encuentros y rótulos de capacidad. No se editó el resultado a mano: el CSV y el MD se regeneraron con el script.
- **Controles nuevos:** el título y los encuentros de cada ficha coinciden con Work, y cada ficha rotula las capacidades de §5.2 como no oficiales.
- **Resultado:** los Capítulos 4 a 6 dejaron de figurar «pendientes».
- **Para el lote 3:** cuando se construya, solo hay que agregar `cap7.py` a `cap9.py` a `FICHAS`.

## 10. Decisiones que necesita Fernando

1. **Aprobar este plan** y autorizar la construcción del lote 3.
2. **Notación del modelo de datos.**
   - **Recomendada:** la clásica de Algorítmica 3.º, que el curso ya conoce, con los atributos en el diccionario.
   - **Alternativa:** pata de gallo. Agregaría una notación nueva.
3. **Notación del mapa de navegación** (§8). Es nueva en la colección y conviene aprobarla como se aprobaron las del Capítulo 5.
4. **Práctica 9:** incluirla (recomendado, por coherencia con el cuaderno y con el Capítulo 6) o dejar el Capítulo 9 solo con el H3, como dice el índice de Work.
5. **Entorno técnico de referencia en 9.3.** Se propone la ruta de Work §7.5 como ejemplo, sin recomendarla como única y con la indicación «a verificar en la institución». La verificación real de la instalación queda como requisito previo de la Unidad IV, que no está autorizada.

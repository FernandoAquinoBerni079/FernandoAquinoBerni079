# Informe de trazabilidad — Reauditoría de la Fase 2, Análisis y Diseño de Sistemas 3.º BTI

**Responde a:** el dictamen «FASE 2 CON OBSERVACIONES» de ChatGPT sobre el commit `5044b60fa33076705849acdf0462c38496a02cad`.

**Estado:** versión corregida de los pilotos, candidata para una nueva auditoría independiente.
- No es material apto para la venta.
- No se construyeron otros capítulos, no se reemplazaron maestros y no se subió nada a Drive.
- Cualquier fase posterior depende de la aprobación expresa de Fernando.

**Documento base leído íntegramente:** «BTI3_Analisis_Diseno_Diagnostico_Propuesta_v0.1.pdf», de Work: 22 páginas, 82.525 bytes, SHA-256 `3d4f5ab9daf3329f0dd34b13bc30b7001cb8e65780262c536346dbbea065069a`. **No se subió al repositorio, que es público:** es un informe interno, y se cita por su hash.

## 0. Archivos de esta entrega

**Archivos auditados que se conservan.** No se modificó ninguno de `5044b60`: `A_piloto_capitulo4/`, `B_prueba_tecnica/prototipo/`, `B_prueba_tecnica/INFORME_PRUEBA_TECNICA_PHP_SQLITE.md`, `C_informe_esfuerzo/INFORME_DISTRIBUCION_ESFUERZO.md` y `NOTAS_FASE2_PILOTOS.md` conservan sus bytes. Los que corresponde reemplazar quedan reemplazados por los nuevos.

| Piloto | Archivo nuevo | Págs. | Bytes | SHA-256 |
|---|---|---|---|---|
| A | `A2_capitulo4_v2/ADS_3BTI_CAP4_v2_ESTUDIANTE.docx` | 16 | 227663 | `52ddb6d8cc0f1f04b6e2a6a0988eb0176429e71e1eece7f4e30ab45d66c9a46a` |
| A | `A2_capitulo4_v2/ADS_3BTI_CAP4_v2_GUIA_DOCENTE.docx` | 6 | 45332 | `1031d3b3f57d8ed33d8107186acf024ba7a8c1ac163d6e94d3f7925c932c30c0` |
| A | `A2_capitulo4_v2/ADS_3BTI_CAP4_v2_ESTUDIANTE.pdf` (control) | 16 | 384800 | `68b566e8914031119c8bb75e1eae103db60af6a84fb080ae0e2bd43caffb3972` |
| A | `A2_capitulo4_v2/ADS_3BTI_CAP4_v2_GUIA_DOCENTE.pdf` (control) | 6 | 134251 | `90aa78d66844055c186f4589e504005fe93f0f84ba44e0489fefc33ce2a82d36` |
| A (cap. 2) | `A1_candidato_capitulo2/ADS_3BTI_CANDIDATO_CAP2_v1_1_ESTUDIANTE.docx` | 16 | 187364 | `410fcb5c07d63ff903b6d3096337441886fbca285d8995a86ec05629d9d6158c` |
| A (cap. 2) | `A1_candidato_capitulo2/ADS_3BTI_CANDIDATO_CAP2_v1_1_GUIA_DOCENTE.docx` | 6 | 45338 | `ba9447ead6e1619bca370ffb0e2cb030b9f91fb382d5e728e0244eef2db10515` |
| A (cap. 2) | `A1_candidato_capitulo2/…_ESTUDIANTE.pdf` y `…_GUIA_DOCENTE.pdf` (control) | 16 y 6 | 358291 y 130341 | `bb7105e6d73cf18269d499dcac11c3185dcea2d5b5a1b4ee1d7a62aa43e385bf` · `3763d84d6309d0e571e5b2d42765da399292ee2d84fdd0f18500f21aadb3055c` |
| B | `B_prueba_tecnica/INFORME_PRUEBA_TECNICA_v2.md` | — | 10004 | `c58906d059feb62252fd0d0227753f30b1b28535b502e6654412e4c3c72b944d` |
| B | `B_prueba_tecnica/prototipo_v2/src/db.php` | — | 10576 | `47b568f50da8d99223007d08583e0cc9b170ec893c1826900766923dbf646ec7` |
| B | `B_prueba_tecnica/prototipo_v2/src/auth.php` | — | 1817 | `39ab25dd22e3a0e4da4edb15a81fb4ecae35e382f94d3224ce6543f650ba14df` |
| B | `B_prueba_tecnica/prototipo_v2/instalar.php` | — | 3653 | `bfaa1a5072a8041da13da4dc34555c977a68505e9789aaf4be6f944293a02c51` |
| C | `C_informe_esfuerzo/v2/INFORME_DISTRIBUCION_ESFUERZO_v2.md` | — | 8440 | `ff9799df18d50f27af2098fb38bafce2a05e7e6e94a57994c00792d6c94e75fa` |
| C | `C_informe_esfuerzo/v2/distribucion.py` | — | 15138 | `0deb15d247548168564ff133049ec6880158d6050862be84eded8a55eaf44c36` |
| C | `C_informe_esfuerzo/v2/tablas_generadas.md` | — | 10010 | `b2809d8879de8d6fc9c3ddc9854b4af539e0ec2ba845fb1e1888fa3d959f7c96` |

Los demás archivos del prototipo v2, las pruebas, las capturas y los scripts de construcción y control están en las mismas carpetas.

## 1. Observaciones de esta reauditoría

### Piloto A — Corrección curricular

| Observación | Estado | Dónde y cómo |
|---|---|---|
| Conservar el material actual como candidato para el Capítulo 2, sin sobrescribirlo | **Resuelta** | `A_piloto_capitulo4/` intacto. La copia corregida está en `A1_candidato_capitulo2/` (v1.1), rotulada en portada como «material candidato para el Capítulo 2», con la advertencia de que su numeración interna (4.x, encuentros 7 y 8) se reasignará si se integra. |
| Nueva versión del Capítulo 4, alineada con 4.1 a 4.4 de Work | **Resuelta** | `A2_capitulo4_v2/`: «Requisitos que se pueden comprobar», encuentros 7 y 8, Unidad II. Las secciones 4.1 a 4.4 llevan los títulos del índice de Work, y lo verifica un control automático. Capacidad: C3 de Work, «Especifica y prioriza requisitos verificables», rotulada como propuesta institucional y no oficial del MEC. La práctica corresponde a la de Work: «convertir pedidos de usuarios en requisitos verificables». |
| Priorizar funcionales y no funcionales, reglas, identificación, fuentes, aceptación, prioridades y ambigüedades | **Resuelta** | **4.1:** necesidad, requisito, regla y solución. **4.2:** funcionales, calidad y restricciones, con un catálogo de 10 RF, 3 RNF y 2 RS (cumple el mínimo de C3: 8 + 4). **4.3:** identificadores, fuente, tres niveles de prioridad y criterio «Dado… cuando… entonces…». **4.4:** seis tipos de ambigüedad. Reglas RN-01 a RN-06 tomadas de Work §7.2; cadena N-02, RN-01, RF-04, P-07 de Work §7.3 (Figura 4.2). |
| Mantener los buenos recursos | **Resuelta** | Cuatro ejemplos resueltos; dos figuras originales; seis tablas en el libro del estudiante; diez actividades en cuatro bloques; práctica en tres niveles con datos nuevos (buzón B-01 a B-08); evaluación de 15 puntos en página propia con claves repartidas (d, c, b, a); guía docente con secuencia en HC, claves, lista de cotejo, criterios de puntaje parcial, calendario reducido y procedencia; voseo. |
| Corregir referencias a entrevistas que no respaldan lo atribuido | **Resuelta** | Ver §2. En el Capítulo 4 v2, cada fuente es un fragmento reproducido en el propio capítulo. Los controles automáticos verifican: <ul><li>que existan los 31 códigos citados;</li><li>que coincidan las 8 citas textuales;</li><li>que la fuente de 13 requisitos contenga la expresión que los justifica.</li></ul> En el candidato del Capítulo 2 se corrigieron seis referencias. |

**Controles automáticos:**
- Capítulo 4 v2: 37 correctos, 0 fallos (`A2_capitulo4_v2/build/verificacion_resultado.txt`).
- Candidato del Capítulo 2: 33 correctos, 0 fallos.
- **Robustez de maqueta del Capítulo 4 v2**, con tres fuentes de sustitución: la evaluación siempre empieza en página propia y ningún renglón queda suelto.

| Fuente de sustitución | Páginas |
|---|---|
| Carlito | 16 |
| Liberation Sans | 16 |
| DejaVu Sans | 17 |

### Piloto B — Modelo y alcance

| Observación | Estado | Dónde y cómo |
|---|---|---|
| Distinguir obra/edición, ejemplar y préstamo | **Resuelta** | Tablas `obras`, `ejemplares` (código único) y `prestamos` en `prototipo_v2/src/db.php` |
| Préstamo contra un ejemplar identificable | **Resuelta** | `prestamos.ejemplar_id`. Prueba: «el préstamo queda vinculado al ejemplar A-1, no a la obra». |
| Sin préstamos activos incompatibles | **Resuelta en el alcance probado** | **RN-01:** índice único parcial de la base y comprobación en una transacción `BEGIN IMMEDIATE`. **RN-02 y RN-04:** en la misma transacción. **Pruebas:** <ul><li>37 de 37 de reglas;</li><li>10 de 10 rondas simultáneas en procesos separados;</li><li>8 pedidos HTTP simultáneos en 8 sesiones, que dejan un solo préstamo activo.</li></ul> |
| Conservar el historial | **Resuelta** | Disparadores de la base: sin borrado de préstamos, devolución única, datos del préstamo fijos, lectores y ejemplares con historial que solo se inactivan |
| Proteger los datos ante el instalador | **Resuelta** | Sin `--reiniciar` se niega y la base queda idéntica (comparada con su hash). Con `--reiniciar` exige escribir «REINICIAR» y guarda antes un respaldo. Las tres situaciones están probadas. |
| Separar lo que el piloto demuestra de lo que no implementa | **Resuelta** | Tabla del §3 del informe v2 |
| Discrepancia de permisos mínimos | **Resuelta como propuesta; requiere OK de Fernando** | Se alinea con Work. Los permisos mínimos pasan al núcleo: consulta pública, una cuenta de operación con clave cifrada, 403 sin sesión y CSRF. La gestión de usuarios y roles queda como ampliación. Está implementado y probado. |
| Mantener PHP + SQLite como alternativa provisional | **Aplicada** | El informe v2 lo declara provisional hasta una prueba de campo en Windows y equipos escolares |
| No equiparar el bloqueo de SQLite con una verificación completa de concurrencia | **Aplicada** | El §5 del informe v2 dice qué comprueban las pruebas simultáneas y enumera cinco cosas que no comprueban |

### Piloto C — Reconciliación con Work

| Observación | Estado | Dónde y cómo |
|---|---|---|
| Conservar la secuencia original | **Resuelta** | 6 unidades: 1–6, 7–12, 13–18, 19–26, 27–32 y 33–36, con 30/30/30/40/30/20 HC. El foco, las capacidades y los hitos se copian de Work §5.2. |
| Recalcular la distribución identificando el tiempo de cada actividad | **Resuelta** | `distribucion.py` asigna las 5 HC de cada encuentro a siete categorías, con el criterio escrito por fila, y verifica las sumas. **Resultado sobre 180 HC:** <ul><li>análisis 26,7 %;</li><li>diseño 17,2 %;</li><li>programación 15,0 %;</li><li>verificación y validación 20,0 %;</li><li>documentación 3,9 %;</li><li>gestión 4,4 %;</li><li>evaluación 12,8 %.</li></ul> |
| Cálculo verificable, sin modificar el alcance en silencio | **Resuelta** | El script falla si una suma no coincide con Work. El alcance de la secuencia de 36 no cambia. Se explica la diferencia entre las 40 HC de la Unidad IV y las 23 HC de programación pura de esa unidad. |
| Adaptación de 28 encuentros que preserve competencias y evidencias | **Resuelta** | Ocho fusiones con su ajuste de alcance escrito. El script comprueba que cada encuentro de Work aparezca una vez y que se conserven C1 a C10 y H1 a H6. **Riesgo declarado:** se pierde el encuentro de reserva y la preparación del entorno pasa a la base del docente. |

### Decisiones editoriales provisionales

| Decisión | Estado |
|---|---|
| Verde BTI como identidad preliminar, sujeta a cotejo con el catálogo | **Aplicada.** El cotejo sigue **pendiente**: el inventario de identidades del catálogo no está en este entorno. |
| 5 HC semanales como unidad de planificación, en varios bloques | **Aplicada** en la ficha, la guía y el Piloto C |
| Capacidades propuestas separadas de las oficiales del MEC | **Aplicada**, con control automático en los dos capítulos |

## 2. Referencias corregidas en el candidato del Capítulo 2 (v1.1)

| N.º | Lugar en el piloto auditado | Problema | Corrección |
|---|---|---|---|
| 1 | Ejemplo resuelto 4.5, Paso 1 | Citaba «T1-L3», un registro de taller que no existe, y «E1-L4» para el plazo de 7 días, que E1-L4 no menciona | La situación se rotula como hipotética. Se explica qué registros se citarían en un caso real, sin inventar códigos. |
| 2 | Ejemplo resuelto 4.5, situación | Atribuía a la bibliotecaria la frase «si no, los libros no vuelven», que no está en ningún registro | Se reformula sin cita textual |
| 3 | Tabla 4.1 | Presentaba entre comillas, como dichas por el interesado, tres frases que eran paráfrasis («Pierdo media hora…», «A fin de mes cuento…», «Quiero una app…») | Las dos primeras se reemplazan por las frases literales de E1-L4 y E1-L8, con su código. La tercera, por el intercambio real de E1-L11/12, en el que la propuesta fue del analista. |
| 4 | Tabla 4.6, RC-01 | Origen «H1, H2», mientras el texto del Ejemplo 4.4 decía que H1 no genera requisito | Origen «H2 (contexto: H1)» |
| 5 | Guía, clave de la Actividad 2 del Encuentro 8 | Origen «H3, H4 y H5»: H3 (cuánto tarda encontrar un libro) no respalda registrar la devolución | Origen «H4 y H5», con la razón |
| 6 | Guía, claves de los Niveles 1 y 2 | «O1, línea 4» sin numeración en el registro, y «menos de un minuto», cifra que la observación O1 no respalda | Las líneas de O1 se numeran O1-1 a O1-4. El requisito se reformula como «agilizar el registro en hora pico», y la meta de tiempo queda para preguntársela a la bibliotecaria. |

Un control nuevo comprueba que las 21 referencias a líneas de registro del candidato existan y que no haya referencias a registros inexistentes.

## 3. Observaciones de la primera auditoría (1 a 8): estado actualizado

| N.º | Observación | Estado |
|---|---|---|
| 1 | No convertir la asignatura en otro curso de programación web | **Atendida.** El Capítulo 4 no exige programar. En la secuencia de Work, la programación es el 15 % del tiempo y el código se entrega como base explicada. |
| 2 | Separar el núcleo de las ampliaciones | **Atendida con un cambio.** Los permisos mínimos pasan al núcleo, como en Work. La gestión de usuarios y roles, y la evaluación de concurrencia en condiciones reales, quedan fuera. Requiere OK. |
| 3 | No dar por dominados Laboratorio y Algorítmica de 3.º | **Atendida.** Coordinación antes de los encuentros 13 y 19 (Work §3); base de proyecto; ruta sin computadora. |
| 4 | Calendario con menos encuentros | **Atendida.** Adaptación de 28 encuentros con controles, más un recuadro de contingencia en el Capítulo 4. |
| 5 | No duplicar los ejercicios de biblioteca de Algorítmica 3.º | **Atendida.** Control automático: ninguna persona ni dato de ese libro. El Capítulo 4 trabaja requisitos y reglas, no tablas ni claves. |
| 6 | Validar el entorno antes de fijarlo | **Parcial.** Validado en Linux con PHP 8.3. **Pendiente:** prueba de campo en Windows y equipos escolares, y versiones de PHP de la 7.4 a la 8.2. |
| 7 | Capacidades institucionales separadas de las oficiales del MEC | **Atendida.** La afirmación de Work sobre la p. 29 del diseño curricular se cita como lectura de Work, no verificada por separado. |
| 8 | Procedencia y derechos | **Atendida para esta entrega.** Todo es original o tomado del informe interno de Work; el inventario está en la guía de cada capítulo. Los títulos de libros del prototipo son datos bibliográficos; las personas son ficticias. |

## 4. Pendientes que no dependen de una decisión

1. Prueba de campo del prototipo v2 en el laboratorio destino: dos máquinas, al menos una con Windows.
2. Ejecución en PHP 7.4–8.2.
3. Cotejo de la identidad verde BTI contra el inventario del catálogo.
4. Verificación independiente, si se requiere, de las páginas del diseño curricular MEC de mayo de 2026 que cita Work (pp. 24, 29 y 34).

## 5. Decisiones que necesitan aprobación de Fernando

1. **Permisos mínimos en el núcleo** (consulta pública y cuenta de operación), con la gestión de usuarios como ampliación. Alinea con Work y cambia lo dicho en la versión 1.
2. **Destino del material de elicitación:** integrarlo al Capítulo 2 (con renumeración y alineación con la C2 de Work), usarlo solo como banco de actividades o descartarlo.
3. **Reparto del tiempo por encuentro (Piloto C):** aprobar la asignación editorial o pedir ajustes por fila.
4. **Adaptación de 28 encuentros:** aprobar las ocho fusiones, en especial la base de proyecto entregada por el docente y la pérdida del encuentro de reserva.
5. **Reglas RN-01 a RN-06:** confirmarlas como supuestos didácticos del caso, tal como las propone Work.
6. **Evaluación escrita del capítulo:** mantenerla como instrumento opcional y formativo (propuesta actual) o hacerla obligatoria.
7. **Informe de Work:** dónde guardarlo de forma privada. No se subió al repositorio público.
8. **Fase siguiente:** autorizar o no la construcción de más capítulos tras la nueva auditoría.

## 6. Encargo para la nueva auditoría de ChatGPT

> Auditá la versión corregida de los pilotos de la Fase 2 en `analisis_diseno_3_bti/fase2_pilotos/`, en el commit indicado por Claude, contra el informe de Work v0.1 y tu dictamen anterior.
>
> **A.** Revisá en tu propia renderización `A2_capitulo4_v2/`:
> - alineación con 4.1 a 4.4 de Work y con C3;
> - corrección conceptual;
> - que cada fuente citada respalde lo que se le atribuye;
> - progresión de la práctica;
> - coherencia entre indicadores, actividades, evaluación y guía;
> - voseo y maqueta.
>
> Revisá también `A1_candidato_capitulo2/` solo en cuanto a las seis referencias corregidas.
>
> **B.** Ejecutá o revisá `B_prueba_tecnica/prototipo_v2/` y su informe:
> - modelo obra/ejemplar/préstamo;
> - reglas en la base;
> - protección del instalador;
> - permisos mínimos;
> - honestidad de los límites de la verificación de concurrencia.
>
> **C.** Corré `C_informe_esfuerzo/v2/distribucion.py`. Revisá:
> - los criterios de asignación por encuentro;
> - la adaptación de 28 encuentros;
> - que no se haya modificado el alcance de Work.
>
> Indicá qué observaciones quedan resueltas, cuáles siguen abiertas y cuáles son decisiones de Fernando.

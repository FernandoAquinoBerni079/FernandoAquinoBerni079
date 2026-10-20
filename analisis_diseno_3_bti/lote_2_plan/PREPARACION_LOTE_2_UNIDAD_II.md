# Preparación del lote editorial 2 — Unidad II (Capítulos 4, 5 y 6)

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · 20 de octubre de 2026**

**Estado:** preparación. **No se construye nada:**
- el lote 2 empieza cuando se audite y apruebe el lote 1 (Capítulos 1 a 3);
- no se empezaron los Capítulos 5 y 6;
- no se modificó ningún archivo existente, ni del lote 1 ni de los pilotos del Capítulo 4.

**Base:**
- `lote_1/` (commit `cdc96a6`), con la fuente única del caso `caso/dossier.py`;
- `fase2_pilotos/A2_capitulo4_v2/` (libro y guía);
- `fase2_pilotos/A2_capitulo4_v2_1/` (guía);
- `fase2_pilotos/A2_capitulo4_proxima_version/ESPECIFICACION_EVIDENCIA_C3.md`;
- la distribución de 180 HC (`C_informe_esfuerzo/v2_1/distribucion_36.csv`).

## 1. Alcance de la Unidad II

**Unidad II — Especificar qué debe resolver el sistema.** Encuentros 7 a 12 (30 HC), con el hito H2 en el encuentro 12.

| Capítulo | Encuentros | Foco de cada encuentro (Work §5.2, tomado de la distribución) | Capacidades | Situación |
|---|---|---|---|---|
| 4. Requisitos que se pueden comprobar | 7 | Formular requisitos funcionales y reglas de préstamo | C3 | Existe la v2: libro de 16 págs. y guía v2.1. Falta la versión con C3 integrada. |
| | 8 | Definir calidad, restricciones y criterios de aceptación | C3, C9 | |
| 5 | 9 | Representar el proceso actual y el proceso propuesto | C4 | No empezado |
| | 10 | Desarrollar casos de uso y excepciones | C3, C4 | |
| 6 | 11 | Priorizar, planificar incrementos y establecer trazabilidad | C3, C7 | No empezado |
| | 12 | Resolver una solicitud de cambio; revisión de la Unidad II | C3, C4, C7 | Hito H2: requisitos y modelos funcionales |

**Títulos y secciones de los Capítulos 5 y 6.** Salen del índice de Work (§6), que no está en el repositorio ni en Drive. Hay que recibir el PDF de Work (SHA-256 `3d4f5ab9…065069a`) antes de planificarlos en detalle. No se inventaron títulos.

**Adaptación a 28 encuentros.** La v2.1 de la distribución une los encuentros 9 y 10 de Work en uno solo, que conserva el proceso actual simplificado, el proceso propuesto y los tres casos de uso con un flujo alternativo cada uno. El Capítulo 5 necesita su recuadro «Si el calendario se acorta» con esa fusión.

## 2. Capítulo 4: qué se integra y qué cambia

El capítulo **no se reescribe**. Se toma la v2 (libro) y la v2.1 (guía) y se les aplica:

### 2.1 La especificación de evidencia C3, tal como fue aprobada

**Libro:**
- consigna común obligatoria en la Práctica 4, antes de los niveles: RNF-04 a partir de B-03, con su criterio «Dado… cuando… entonces…», su fuente y su prioridad;
- Nivel 2: numerar desde RNF-05 y corregir solo la ambigüedad de B-08;
- Nivel 3 sin cambios;
- la Actividad 1 (d) del Encuentro 8 pasa a tarea, para compensar las 0,25 HC.

**Guía:**
- clave de la consigna común;
- fila nueva en la lista de cotejo (criterio de calidad, indicador 3);
- fila RNF-04 en la tabla de correspondencia, con origen «Trabajo del estudiante»;
- nota sobre la evidencia mínima de C3.

**Verificador:** las cuatro comprobaciones del §4 de la especificación.

### 2.2 Integración con el dossier del lote 1

| Punto | Hoy (v2) | En el lote 2 |
|---|---|---|
| Extracto del dossier (E1, E4, E3 y E5) | Escrito a mano en `contenido.py` del Capítulo 4. `lote_1/caso/verificar_caso.py` comprueba que coincide con el dossier. | Se lee de `caso/dossier.py`, la fuente única. Se elimina la copia. |
| Reglas RN-01 a RN-06 | En el capítulo, numeradas | Se toman del dossier, cuyo texto ya es idéntico (control del lote 1). El Capítulo 4 es el primero que las numera, como prevé el lote 1. |
| Necesidades N-01 a N-13 | El capítulo usa N-02 (E4-L4) | Las necesidades citadas se leen del dossier. La cadena de la Figura 4.2 se verifica contra el dossier. |
| **Buzón de pedidos B-01 a B-08** (Práctica 4) | Solo en el Capítulo 4, como pedidos del caso Arapoty | **Decisión necesaria** (§2.3). Una vez decidido, el buzón pasa a la fuente única del caso que corresponda. |
| Portada y recuadro de piloto | El capítulo tiene portada y estado propios | Se quitan. El capítulo entra en el libro unificado, después de una apertura de la Unidad II con el mismo formato que la de la Unidad I. |
| Rótulo de capacidad | «Capacidad propuesta para el programa institucional (C3; no es una capacidad oficial del MEC)» | Se iguala al formato del lote 1 («Capacidades propuestas para el programa institucional (…; no son capacidades oficiales del MEC)»). El verificador B del lote 1 ya lo controla. |
| Semilla de la evaluación | `ADS3-C4v2-2` | Se conserva si las claves no cambian. El lote 1 ya comprobó que es distinta de las tres suyas. |
| Maqueta | `helpers.py` y `maqueta.py` (A4) | Los mismos módulos que el lote 1. Si se decide el oficio (ver el inventario, §1.1), el cambio se hace una vez para toda la colección. |

### 2.3 Decisión: el buzón de la Práctica 4 y la regla de Work §7.4

El lote 1 aplicó Work §7.4 así: las tres prácticas usan **otra escuela ficticia (Mbokaja)**, con datos distintos de los ejemplos. La Práctica 4 del Capítulo 4 usa, en cambio, el **buzón de pedidos del Colegio Arapoty**, el mismo caso de los ejemplos, aunque con pedidos que los ejemplos no usan. La especificación C3 aprobada está escrita sobre B-03 de ese buzón.

| Opción | Qué implica | Costo |
|---|---|---|
| **A. Conservar el buzón de Arapoty** y declararlo excepción: son datos nuevos del mismo caso, no usados en los ejemplos | La especificación C3 se aplica tal cual. El buzón entra en `caso/dossier.py`. | Mínimo. Rompe la regla tal como la aplicó el lote 1. |
| **B. Rehacer el buzón en Mbokaja** | Hay que reescribir los ocho pedidos, las consignas de los tres niveles, las claves, la consigna común C3 (B-03 → pedido equivalente) y la tabla de correspondencia | Medio. Es una nueva ronda sobre material aprobado. |

**Recomendación: A.** Es la que menos rehace. La especificación C3 ya fue aprobada sobre B-03. La decisión es de Fernando.

## 3. Capítulos 5 y 6: lo que se puede preparar sin el índice de Work

No se escriben. Para cuando se autoricen, conviene tener presente:

- **Fuentes.** Deben salir del mismo dossier y del catálogo de requisitos del Capítulo 4. Los casos de uso del Capítulo 5 y la trazabilidad del Capítulo 6 tienen que citar requisitos que existan: RF-01 a RF-10, RNF y RS del catálogo, más RNF-04, que crea la consigna común.
- **Algorítmica 3.º.** Hay que verificar, con el libro completo de Algorítmica 3.º (está en Drive), que los diagramas de proceso, los casos de uso y la planificación de incrementos no repitan sus ejercicios de biblioteca ni sus personas. Es el mismo control E del lote 1.
- **Hito H2** (encuentro 12). Hace falta una rúbrica con el formato del H1: cuatro niveles y la proporción 60/40 como propuesta editorial. Su evidencia son los requisitos y los modelos funcionales.
- **Solicitud de cambio** (encuentro 12). Puede tomar un pedido no atendido del dossier o del buzón, por ejemplo la renovación sin traer el libro (E3-L4).

## 4. Entregables del lote 2

| Entregable | Contenido |
|---|---|
| Libro del estudiante, Unidad II (DOCX y PDF de control) | Apertura de la Unidad II y Capítulos 4, 5 y 6 con la misma estructura del lote 1: ficha, secciones de Work, ejemplos resueltos, figuras, actividades en cuatro bloques, práctica en tres niveles, «Para repasar», «Si el calendario se acorta» y evaluación opcional en página propia. El Capítulo 6 cierra con la revisión de la Unidad II (H2). |
| Guía docente, Unidad II (DOCX y PDF) | Secuencia por encuentro en HC, claves, listas de cotejo, rúbrica del H2 y procedencia de los recursos |
| Controles | Los bloques A a J del lote 1, extendidos a los Capítulos 4 a 6, más los cuatro controles de C3 y la trazabilidad de requisitos entre capítulos |
| Informe y manifiesto | Con el mismo formato del lote 1 |

**Decisión de armado.** El libro unificado puede salir de dos formas: como documento separado de la Unidad II, o como un único libro con los lotes 1 y 2. En el segundo caso, el lote 1 se regenera sin cambios de contenido.

## 5. Orden de trabajo, cuando se autorice

1. Fuente única ampliada: `caso/dossier.py` con el buzón y el catálogo de requisitos del Capítulo 4, más sus controles.
2. Capítulo 4 integrado, con C3.
3. Capítulo 5 y Capítulo 6, con el índice de Work a la vista.
4. Guía de la unidad.
5. Controles, PDF, prueba de fuentes, informe y commit.
6. Auditoría independiente y aprobación de Fernando.

## 6. Decisiones que necesita Fernando

1. **Aprobar el lote 1**, después de la auditoría.
2. **Formato de página:** A4, como hoy, u oficio, para toda la colección (inventario, §1.1).
3. **Buzón de la Práctica 4:** opción A o B (§2.3).
4. **Libro de la Unidad II:** separado, o unificado con el lote 1 (§4).
5. **Enviar el informe de Work v0.1 en PDF,** para los títulos y secciones de los Capítulos 5 y 6.

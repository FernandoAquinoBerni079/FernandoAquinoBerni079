# Piloto C — Distribución del esfuerzo entre análisis y diseño, y programación

**Proyecto:** Biblioteca Comercial 2026 — Análisis y Diseño de Sistemas, 3.º BTI (Plan Optativo, 5 HC semanales, 36 encuentros).
**Estado:** candidato para la auditoría de ChatGPT. No es una decisión cerrada.

## 0. Advertencia sobre la estructura usada

El documento base, «BTI3_Analisis_Diseno_Diagnostico_Propuesta_v0.1.pdf», no llegó a este entorno: no estaba entre los adjuntos ni en Drive. Este informe usa una **estructura de trabajo supuesta**, coherente con lo que el encargo sí fija:
- 6 unidades, 18 capítulos y 36 encuentros, a dos encuentros por capítulo;
- la secuencia: necesidades, requisitos, modelado, diseño, validación y documentación, con un prototipo web integrador.

Cuando el documento base esté disponible, la tabla del §2 se reemplaza por su estructura. Los porcentajes y las recomendaciones se recalculan con el mismo método.

## 1. Criterio

La asignatura **no es un segundo curso de programación web** (observación 1). Su producto principal son los documentos de análisis y diseño: requisitos, modelos, diseño y plan de pruebas. El prototipo existe para **validar** esos documentos, no al revés.

Por eso la programación se ubica:
- **tarde:** en la Segunda Etapa, cuando Algorítmica y Laboratorio de 3.º ya avanzaron (observación 3);
- **acotada:** al núcleo medido en el Piloto B, que entra en 239 líneas de PHP;
- **andamiada:** el estudiante completa y modifica código dado, no escribe desde cero.

## 2. Distribución por unidad (estructura supuesta)

Clasificación de cada encuentro:
- **AD:** análisis, diseño, validación y documentación, sin escribir código;
- **P:** programación del prototipo;
- **E:** evaluación e integración.

Las fracciones indican encuentros compartidos.

| Unidad | Capítulos (supuestos) | Enc. | AD | P | E |
|---|---|---|---|---|---|
| 1. Sistemas y necesidades | 1. Sistemas de información en la escuela · 2. Ciclo de vida y rol del analista · 3. Diagnóstico de la situación actual | 1–6 | 5,5 | 0 | 0,5 |
| 2. Ingeniería de requisitos | **4. Elicitación de requisitos (piloto A)** · 5. Especificación: funcionales, no funcionales, historias de usuario · 6. Priorización, validación y trazabilidad | 7–12 | 5,5 | 0 | 0,5 |
| 3. Modelado | 7. Casos de uso · 8. Procesos y actividades · 9. Modelo conceptual de la información | 13–18 | 5 | 0 | 1 (cierre de la Primera Etapa) |
| 4. Diseño | 10. Arquitectura y componentes · 11. Interfaz y prototipo en papel · 12. Diseño de datos y de reglas | 19–24 | 5 | 0,5 (maqueta HTML estática, opcional) | 0,5 |
| 5. Construcción guiada y pruebas | 13. Del diseño al código: el núcleo · 14. Pruebas contra los requisitos · 15. Validación con usuarios | 25–30 | 2,5 | 3 | 0,5 |
| 6. Documentación y entrega | 16. Documentación técnica y de usuario · 17. Implantación y mantenimiento · 18. Presentación del proyecto | 31–36 | 3,5 | 1 (ajustes del prototipo) | 1,5 (cierre de la Segunda Etapa y defensa) |
| **Total** | 18 | 36 | **27 (75 %)** | **4,5 (12,5 %)** | **4,5 (12,5 %)** |

**Lectura:** tres de cada cuatro encuentros son de análisis y diseño. La programación ocupa unos cuatro encuentros y medio, concentrados entre los encuentros 25 y 32. El Capítulo 9 se apoya en el modelo de datos que el estudiante ve en Algorítmica 3.º y **no repite** sus ejercicios de claves, integridad y normalización sobre la biblioteca (observación 5). Allí el foco es el vocabulario del negocio: qué información necesita cada interesado.

## 3. Por qué no más programación

1. **Es otra asignatura.** La programación web se enseña en otras materias del bachillerato. Si esta materia la repite, pierde lo que solo ella da: escuchar al usuario, escribir requisitos verificables, modelar y decidir con criterio.
2. **Calendario simultáneo.** En febrero y marzo el estudiante de 3.º recién empieza Algorítmica y Laboratorio. No se puede suponer que maneja PHP, SQL ni formularios (observación 3). En agosto ya hay base para completar código guiado.
3. **El núcleo es chico.** El Piloto B muestra que catálogo, préstamo y devolución con su regla entran en 239 líneas. Lo difícil del proyecto no es el código: es saber **qué** tiene que hacer.
4. **Evaluabilidad.** Un requisito, un caso de uso o un caso de prueba se corrigen con rúbrica en papel. El código exige una máquina por estudiante y tiempo de laboratorio, que no siempre existe.

## 4. Recomendaciones para estudiantes de nivel técnico medio

1. **Código dado, comentado y verificable.** El libro entrega el núcleo del Piloto B completo. Cada práctica de programación pide una de estas cosas:
   - **completar** un hueco: una validación o un mensaje;
   - **modificar** algo: un campo o un texto de la interfaz;
   - **agregar** una funcionalidad pequeña, trazada a un requisito.

   Nunca «programá el sistema».
2. **Todo cambio de código nace de un requisito.** La práctica pide anotar qué requisito implementa y qué caso de prueba lo comprueba. Así la programación queda subordinada al análisis.
3. **Tres niveles en cada práctica de programación:**
   - **Base:** modificar textos, validaciones o campos existentes.
   - **Intermedio:** agregar una consulta o un listado nuevo.
   - **Avanzado, como ampliación:** autenticación, roles y concurrencia, nunca obligatorios (observación 2).
4. **Ruta alternativa sin computadora.** Si el laboratorio no está disponible, las prácticas del prototipo tienen una versión en papel: leer el código impreso, predecir la salida y escribir el caso de prueba. La evaluación no se cae por falta de máquinas.
5. **Prueba de campo antes de la Unidad 5.** El docente corre `verificar_entorno.php` en el laboratorio en julio, no el día de la primera práctica.

## 5. Alternativa para un calendario con menos encuentros (observación 4)

Supuesto: el año escolar real da **28 encuentros efectivos** en lugar de 36, por feriados, actos, jornadas o suspensiones. La regla es **conservar intactos los requisitos y el modelado**, que son el centro de la asignatura, y comprimir los extremos.

| Ajuste | Encuentros que se liberan |
|---|---|
| Capítulos 1 y 2 en un solo encuentro cada uno (lectura previa y una actividad central) | 2 |
| Capítulo 9 en un encuentro, apoyado en Algorítmica 3.º | 1 |
| Capítulo 12 en un encuentro | 1 |
| Capítulo 13: el docente presenta el código dado y el estudiante hace solo la práctica base | 1 |
| Capítulos 16 y 17 unidos en dos encuentros | 2 |
| Capítulo 18: presentación en un solo encuentro | 1 |
| **Total** | **8 (de 36 a 28)** |

Con 28 encuentros:
- análisis y diseño ocupan 22 (79 %);
- programación, 2,5 (9 %);
- evaluación, 3,5 (12 %).

La reducción **sube** la proporción de análisis y diseño: no se sacrifica el núcleo de la materia. Cada capítulo del libro marcará cuál es su «actividad central», la que no se omite cuando el capítulo se da en un solo encuentro. El Piloto A muestra cómo se hace en el Capítulo 4.

## 6. Qué tiene que confirmar el documento base

- Los títulos y el orden reales de los 18 capítulos, en especial el del Capítulo 4.
- Si la propuesta de Work fija otro reparto entre análisis y programación.
- Si existe un programa oficial del MEC para la asignatura en el Plan Optativo. Mientras no se verifique documentalmente, toda capacidad del libro se rotula como **institucional o editorial**, nunca como oficial (observación 7).

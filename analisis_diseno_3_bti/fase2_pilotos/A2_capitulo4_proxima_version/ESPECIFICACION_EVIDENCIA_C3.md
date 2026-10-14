# Capítulo 4 — Cambio para la próxima versión editorial: evidencia de C3 en todos los alumnos

**Estado:** especificación aprobable. **No se rehízo el capítulo.** Los archivos del piloto quedan sin cambios: `A2_capitulo4_v2/` (libro y guía) y `A2_capitulo4_v2_1/` (guía). El cambio se aplica cuando Fernando autorice la versión siguiente del capítulo.

## 1. Problema

C3 pide definir criterios de aceptación. Hoy, un alumno puede terminar el capítulo sin haber escrito ningún criterio sobre un **requisito de calidad**:

| Dónde | Qué se pide hoy | Por qué no alcanza |
|---|---|---|
| Encuentro 8, Actividad 2 | Criterios de RF-05 y RF-06 | Los dos son funcionales |
| Encuentro 8, Actividad 5 | Criterio de RNF-03 | Es el Desafío: opcional y como tarea |
| Práctica 4, Nivel 1 (el piso común) | Ficha de un RF con criterio y ficha de una RS | La RS no lleva criterio, y no hay ningún RNF |
| Práctica 4, Nivel 2 | Dos RNF con criterio | Solo para quienes hacen el Nivel 2 |
| Práctica 4, Nivel 3 | No pide RNF | — |
| Evaluación (opcional) | El ítem 8 es funcional (vencidos) | — |

## 2. Cambio: consigna común obligatoria en la Práctica 4

Se agrega antes de los tres niveles, con este rótulo y texto:

> **Consigna común — para todos, antes de empezar tu nivel**
>
> El pedido B-03 dice: «El sistema tiene que avisar rápido si el libro está».
> 1. Redactalo como requisito de calidad RNF-04, con una cifra comprobable marcada «a confirmar».
> 2. Escribí su criterio de aceptación «Dado… cuando… entonces…», de modo que otra persona pueda comprobarlo.
> 3. Anotá la fuente (B-03) y una prioridad con su razón.

**Ajustes que arrastra:**
- **Nivel 2, consigna 1:** numerar desde **RNF-05**, porque RNF-04 lo usa la consigna común.
- **Nivel 2, consigna 2:** corregir la ambigüedad de **B-08** solamente; la de B-03 ya la resolvió la consigna común.
- **Nivel 3:** sin cambios. La consigna común le asegura la evidencia de un requisito de calidad.
- **Tiempo:** la consigna común ocupa aprox. 0,25 HC de las 1,5 HC de la práctica. Para compensar, la Actividad 1 (d) del Encuentro 8 pasa a tarea.

## 3. Cambios en la guía docente

**Clave de la consigna común** (respuesta de referencia):

> RNF-04. La consulta de disponibilidad de un título debe mostrar el resultado en menos de 3 segundos en la computadora de la biblioteca (cifra a confirmar con quien lo pidió). Fuente: B-03. Prioridad: importante; la consulta funciona igual sin esa meta de tiempo, pero es lo que pidió el lector.
>
> Criterio: Dado un título con ejemplares cargados y la computadora de la biblioteca en uso normal, cuando un lector lo busca por su título cinco veces seguidas, entonces el resultado aparece cada vez en menos de 3 segundos.
>
> Se acepta otra cifra o situación si es comprobable. No se acepta «rápido», «enseguida» ni ninguna otra palabra vaga en el criterio.

**Lista de cotejo**, una fila nueva:

| Criterio | Indicador |
|---|---|
| Redacta al menos un criterio de aceptación comprobable para un requisito de calidad (consigna común) | Indicador 3 |

**Correspondencia de requisitos y criterios**, sección 3 de la guía:
- **Fila nueva:** «RNF-04 (buzón, B-03) — Trabajo del estudiante — Práctica 4, consigna común».
- **Nota bajo la tabla:** la evidencia mínima de C3 es, para cada alumno, un criterio funcional (Encuentro 8, Actividad 2) y uno de calidad (consigna común).

## 4. Control automático que se agregará al verificador del capítulo

**Comprobaciones:**
1. Existe una consigna fuera de `NIVELES` rotulada «Consigna común», que menciona «requisito de calidad», «RNF-04» y «Dado… cuando… entonces…».
2. La lista de cotejo tiene la fila del criterio de calidad, vinculada al indicador 3.
3. La tabla de correspondencia incluye RNF-04 con origen «Trabajo del estudiante».
4. Ninguna consigna de nivel reutiliza RNF-04.

**Resultado esperado:** todo camino posible por la Práctica 4 incluye al menos un criterio de aceptación sobre un requisito de calidad.

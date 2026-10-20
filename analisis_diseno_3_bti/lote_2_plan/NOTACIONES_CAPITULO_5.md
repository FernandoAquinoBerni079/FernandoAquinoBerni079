# Notaciones del Capítulo 5 — especificación

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · 20 de octubre de 2026**

**Estado:** especificación aprobada por Fernando. Se aplica cuando se autorice el lote 2; el capítulo no se construye ahora.

**Criterio de Work (§4.2, C4):** «los diagramas ayudan a explicar el funcionamiento y permiten detectar omisiones, sin mezclar notaciones».

## 1. Una notación por representación

| Sección | Representación | Notación | Qué muestra |
|---|---|---|---|
| 5.1 | Proceso actual y proceso propuesto | **Diagrama de actividades UML con particiones (carriles)** | Qué hace cada participante, en qué orden y dónde se decide |
| 5.2 | Diagrama de contexto | **Diagrama de contexto**: sistema, entidades externas y flujos de información | Qué información entra y sale del sistema y con quién la intercambia |
| 5.3 y 5.4 | Actores, casos de uso y escenarios | **Diagrama de casos de uso UML**: actores, casos y límite del sistema | Quién usa el sistema y para qué. Los escenarios y los flujos alternativos van en una plantilla de texto, no en el diagrama. |

**Ninguna figura mezcla símbolos de dos notaciones.** En particular:
- el diagrama de contexto no usa la figura de persona de los actores;
- el diagrama de casos de uso no lleva flechas de datos ni rombos;
- el diagrama de actividades no lleva elipses.

## 2. Símbolos que se definen y explican en el libro

### 2.1 Diagrama de actividades con particiones (5.1)

| Símbolo | Nombre | Significado | Regla de uso |
|---|---|---|---|
| Círculo negro relleno | Nodo inicial | Donde empieza el proceso | Uno por diagrama |
| Rectángulo de esquinas redondeadas | Acción | Una tarea que hace un participante | Verbo en infinitivo y objeto: «Registrar el préstamo» |
| Rombo | Decisión (y fusión) | El camino se divide según una condición, o se vuelve a unir | Cada salida lleva su guarda entre corchetes: «[ejemplar disponible]», «[ya prestado]» |
| Flecha | Flujo | El orden en que se suceden las acciones | Sin rótulo, salvo las guardas que salen de una decisión |
| Círculo con un círculo negro dentro | Nodo final | Donde termina el proceso | Puede haber más de uno |
| Columna con el nombre arriba | Partición (carril) | El responsable de las acciones de esa columna | Una por participante. En el proceso actual: lector y bibliotecaria. En el propuesto se agrega «Sistema». |

**Fuera del núcleo:** bifurcación y unión (barras), nodo final de flujo y objetos. No hacen falta para el préstamo y la devolución, y agregarían símbolos sin necesidad.

**Responsabilidades a la vista.** Cada acción queda en el carril de quien la hace. En el proceso propuesto, las comprobaciones de las reglas (RN-01 a RN-04) van en el carril «Sistema», junto al requisito que las cubre (RF-04 a RF-06).

### 2.2 Diagrama de contexto (5.2)

| Símbolo | Nombre | Significado | Regla de uso |
|---|---|---|---|
| Un solo círculo o rectángulo redondeado en el centro | Sistema | El sistema de gestión de la biblioteca, visto como un todo | Uno por diagrama, con su nombre |
| Rectángulo | Entidad externa | Persona, rol o sistema que da o recibe información y queda fuera del límite | Bibliotecaria, lector, dirección. El encargado de informática solo si intercambia información. |
| Flecha rotulada | Flujo de información | Un dato o documento que va en un sentido | Rótulo con sustantivo: «pedido de préstamo», «informe mensual por curso». Nunca con verbo de acción. |

**Diferencia que se explica en el texto.** Una entidad externa del diagrama de contexto y un actor del diagrama de casos de uso pueden ser la misma persona. Pero el diagrama de contexto muestra **qué información** intercambia, y el de casos de uso muestra **para qué usa** el sistema.

### 2.3 Diagrama de casos de uso (5.3)

| Símbolo | Nombre | Significado | Regla de uso |
|---|---|---|---|
| Figura de persona con nombre | Actor | Un rol que usa el sistema, no una persona concreta | «Bibliotecaria», «Lector», no un nombre propio |
| Elipse | Caso de uso | Un objetivo del actor que el sistema cumple | Verbo y objeto: «Registrar préstamo», «Consultar disponibilidad» |
| Rectángulo con nombre | Límite del sistema | Lo que queda adentro es responsabilidad del sistema | Los actores quedan afuera |
| Línea sin flecha | Asociación | El actor participa en el caso de uso | Sin flechas ni rótulos |

**Fuera del núcleo:** «include», «extend» y generalización. Los flujos alternativos de 5.4 se escriben en la plantilla del caso de uso, con estos campos:
- actor;
- precondición;
- escenario principal, en pasos numerados;
- flujos alternativos, numerados desde el paso donde se desvían;
- requisitos que cubre.

## 3. Leyenda para la guía docente

La guía del lote 2 trae una **leyenda de notaciones**:
- una tabla por notación con los símbolos del §2 dibujados, su nombre y su significado;
- los errores frecuentes:
  - mezclar símbolos;
  - poner verbos en los flujos del diagrama de contexto;
  - nombrar personas en lugar de roles;
  - acciones del sistema en el carril de la bibliotecaria;
  - casos de uso que son pasos («Escribir el código») en lugar de objetivos.

La misma leyenda, sin los errores frecuentes, va en el libro, en un recuadro de 5.1, 5.2 y 5.3, junto a la primera figura de cada notación.

## 4. Control de coherencia de los diagramas

El módulo de diagramas del lote 2 dibuja con **funciones por notación**:
- `actividad_*` para nodo inicial, acción, decisión, flujo, nodo final y carril;
- `contexto_*` para sistema, entidad y flujo;
- `cu_*` para actor, caso, límite y asociación.

Cada figura declara su notación, y cada función registra el símbolo que dibuja. El verificador comprueba:

1. **Sin mezcla:** cada figura usa solo símbolos de la notación que declara.
2. **Reglas de forma:**
   - en el diagrama de actividades, un nodo inicial, al menos un nodo final y guardas en todas las salidas de cada decisión;
   - en el de contexto, un solo sistema;
   - en el de casos de uso, los actores fuera del límite.
3. **Responsabilidad:** toda acción tiene carril. En el proceso propuesto, toda acción del carril «Sistema» nombra o cita un requisito del catálogo.
4. **Coherencia con el catálogo:**
   - todo RF, RNF o RS citado en un diagrama, un caso de uso o un flujo alternativo existe en la fuente única;
   - los casos de uso «Registrar préstamo», «Registrar devolución» y «Consultar disponibilidad» cubren entre los tres RF-01 a RF-08.
5. **Coherencia entre diagramas:**
   - cada actor del diagrama de casos de uso es una entidad externa del diagrama de contexto, o un carril del proceso propuesto;
   - cada flujo de información del contexto corresponde a algún dato del dossier (registro o línea citada).
6. **Excepciones de 5.4:**
   - cada caso de uso tiene al menos un flujo alternativo;
   - los de préstamo cubren RF-04 (ya prestado), RF-05 (máximo) y RF-06 (lector inactivo).
7. **Leyenda:** cada símbolo usado en una figura figura en la leyenda de la guía.

## 5. Relación con lo ya hecho

La Figura 2.1 del lote 1 («proceso de relevamiento») es un esquema didáctico del trabajo del equipo y no usa UML.

El Capítulo 5 aclara que, desde ahí, los procesos del sistema se representan con la notación UML. La Figura 2.1 no se modifica.

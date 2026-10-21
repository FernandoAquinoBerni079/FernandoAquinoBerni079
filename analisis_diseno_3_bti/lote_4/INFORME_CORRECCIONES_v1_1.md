# Lote 4, versión 1.1 — Corrección del cierre de auditoría

**Análisis y Diseño de Sistemas, 3.º BTI · 21 de octubre de 2026**

**Base:** auditoría de ChatGPT del commit `10c877a`. El dictamen fue «apto con una observación puntual para integración editorial». Se corrigió solo esa observación, la de la Práctica 11.

**Estado:** el lote se puede integrar en lo editorial, pero no está validado para todos los colegios ni aprobado para la venta. Las pruebas de campo siguen pendientes:
- Windows;
- la instalación en un laboratorio escolar;
- la concurrencia real;
- el protocolo E-1 a E-12.

## 1. Versión 1.0 conservada

`lote_4/version_1_0/` guarda la v1.0:
- los seis DOCX y PDF;
- el informe y el manifiesto;
- los resultados de los controles y las láminas;
- las fuentes (`fuentes/caso` y `fuentes/build`).

El verificador comprueba que los seis documentos coinciden con su manifiesto SHA-256. La base de proyecto no cambió y no se copió.

## 2. La observación y la solución elegida

**Observación:** el nivel 2 pedía registrar libros con etiquetas MB- y tres cifras. El proyecto entregado valida EJ- y cuatro cifras. El relato daba por hecho una adaptación que no se podía reproducir.

**Solución:** la práctica se ejecuta con el entorno entregado, sin una tercera base.

**Por qué no hice una base aislada para Mbokaja:**
- habría que copiar el sistema completo de la referencia, que publica resueltas las operaciones de los Capítulos 11 y 12;
- o habría que mantener una tercera distribución con otra validación y otra restricción de la base.

**Cómo queda:**

1. **Copia de práctica.** Cada equipo instala su base en otra carpeta, con `php instalar.php`. La base de la clase no se toca. Si el equipo todavía no construyó OA-01 a OA-03, el docente hace la carga en una copia de la referencia.
2. **Correspondencia fija**, en una tabla nueva del libro y del cuaderno:
   - las etiquetas MB- y tres cifras se escriben EJ-0 y las mismas tres cifras (MB-201 → EJ-0201);
   - una etiqueta con otro formato (MB205) se escribe tal cual, para ver el rechazo;
   - las obras, las ediciones y los lectores tienen códigos asignados (OB-0210, ED-0210, LE-0301 y los demás).
3. **Qué se ejecuta y qué se resuelve en papel**, en otra tabla nueva:

   | Nivel | Dónde se hace |
   |---|---|
   | 1 | Se prevé en papel y se comprueba en la copia |
   | 2 | Se ejecuta en la copia |
   | 3 | Se resuelve en papel: el sistema entregado no tiene un rol de voluntario, así que se decide y se diseña la prueba sin programarla |

4. **Comprobación reproducible:** `lote_4/practica_11/comprobar_practica_11.php`.
   - Usa el código de la referencia docente sin modificarlo, sobre una base temporal.
   - Lee los pasos de `secuencia.json`, que `build/reproducir.py` genera desde `caso/mbokaja_u4.py` (PASOS_P11 y CONSULTAS_P11).
   - Resultado: **17 de 17 correctas**, con el entorno registrado (Linux, PHP 8.3.6, SQLite 3.45.1).
   - Comprueba 13 pasos con su mensaje y 3 consultas públicas:
     - «laguna»: 3 disponibles;
     - «Canciones»: ME-08, porque su ejemplar se rechazó por la etiqueta repetida;
     - «Mapas»: 1 disponible.
   - Comprueba también que la consulta no muestre ningún dato de lectores.
   - El docente puede correrla sobre la copia de un equipo: `php comprobar_practica_11.php <carpeta>`.

## 3. Otros ajustes, para que todas las prácticas de Mbokaja se puedan hacer con el entorno entregado

Cada práctica dice ahora qué se ejecuta y qué se resuelve en papel:
- **Práctica 10:** los niveles 1 y 2 se hacen en una copia de práctica; el nivel 3, en papel.
- **Práctica 12:** se resuelve en papel.
- **Práctica 13:** el registro de la semana y lo que mostró el sistema de Mbokaja se rotulan como **datos simulados**. La práctica se resuelve en papel y no se reproduce en la base entregada.

**Guía docente:**
- claves de la Práctica 11 con los códigos de la correspondencia;
- la tabla «Práctica 11: secuencia comprobada del nivel 2»;
- un criterio nuevo en la lista de cotejo;
- el resultado de la comprobación en la sección 7.

## 4. Lo que no cambió

- **La base Arapoty no cambió:** ni la referencia docente ni la base del estudiante. El verificador lo comprueba con `git diff 10c877a -- lote_4/proyecto` vacío. Sus pruebas siguen sin fallos.
- **No cambiaron:** los contratos, los roles, los mensajes, los fragmentos de código ni las Prácticas 10, 12 y 13, salvo la frase de cada una.

## 5. Documentos y páginas que cambian

| Documento | v1.1 | Páginas que cambian |
|---|---|---|
| Libro | 44 págs. | 1 (versión), 12 (Práctica 10), 22 y 23 (Práctica 11), 32 (Práctica 12), 39 y 40 (Práctica 13) |
| Guía | 24 págs. (antes 23) | Claves y cotejo de la Práctica 11, secuencia comprobada y sección 7. Las demás páginas solo se corren. |
| Cuaderno | 9 págs. | Las mismas prácticas que el libro |

## 6. Resultados

| Programa | v1.0 | v1.1 |
|---|---|---|
| `build/verificar.py` | 274 correctos, 0 fallos | **285 correctos, 0 fallos** (agrega el bloque W y el control de la v1.0 conservada) |
| `build/controles_finales.py` | 26 controles, 0 fallos | **26 controles, 0 fallos** |
| `build/prueba_fuentes.py` | 9 combinaciones, 0 fallos | **9 combinaciones, 0 fallos** |
| `build/reproducir.py` | 0 fallos | **0 fallos** (agrega la Práctica 11: 17 de 17) |

**Bloque W, Práctica 11 reproducible (11 controles nuevos):**
- la práctica no supone un sistema adaptado;
- están las tablas de correspondencia y de ejecución;
- la secuencia sale de la fuente;
- la comprobación no tiene fallos;
- los pasos usan solo códigos que la base acepta o rechaza con su mensaje;
- la base Arapoty no cambió;
- la secuencia está en la guía;
- el nivel 3 dice que se resuelve en papel;
- las Prácticas 10, 12 y 13 dicen cómo se trabajan;
- la v1.0 está conservada;
- la versión 1.1 figura en la portada.

Las láminas de `revision_visual/` se regeneraron desde los PDF de la v1.1. Las de la v1.0 están en `version_1_0/revision_visual/`.

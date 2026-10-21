# Lote 3, versión 1.1 — Correcciones del cierre de auditoría

**Análisis y Diseño de Sistemas, 3.º BTI · 21 de octubre de 2026**

**Base:** auditoría de ChatGPT del commit `f1c8bbf` (dictamen: apto con observaciones para integración editorial). Se corrigieron solo las dos inconsistencias señaladas. No hubo otros cambios de contenido.

**Estado:** sigue siendo un lote para auditoría. No está aprobado para la venta.

## 1. Versión 1.0 conservada

`lote_3/version_1_0/` guarda la v1.0 completa:
- los tres DOCX y PDF;
- el informe y el manifiesto;
- los resultados de los controles y las láminas;
- las fuentes (`fuentes/caso`, `fuentes/build`, con las figuras).

El verificador comprueba que esos seis documentos coinciden con su manifiesto SHA-256.

## 2. Corrección 1: acceso al informe mensual (PT-09)

**Criterio adoptado:** la bibliotecaria y la dirección consultan el informe; el servidor comprueba el rol.

**Fuente (`caso/diseno.py`):**
- La zona «Dirección» se reemplaza por **«Bibliotecaria o dirección»**.
- PT-09 queda en esa zona.
- Se agregan `ROLES_ZONA`, `ROLES_OP` y `PANTALLA_OP`: los roles de cada zona, los de cada operación y la operación que pide cada pantalla.
- La precondición de OP-05 dice: «Rol de bibliotecaria o de dirección, comprobado por el servidor (RNF-02)».

**Libro:**
- Figura 8.1: zona compartida alrededor de PT-09, con el rótulo en dos renglones y sin cruces de flechas.
- Tabla 8.3: zona de PT-09.
- Nota del mapa: explica la zona compartida.
- Tabla 8.1 y leyenda de la guía: la zona agrupa las pantallas de «un rol o un grupo de roles».
- Texto de 8.1 ajustado.

**Guía:**
- Clave 5 del Encuentro 15.
- Dos errores frecuentes nuevos en la tabla del mapa.

## 3. Corrección 2: autenticación y autorización

**Mensajes:**
- **ME-12** queda solo para el inicio de sesión: usuario o contraseña incorrectos, en PT-03.
- **ME-13** es nuevo: «No tenés permiso para hacer esta operación con tu cuenta. Si la necesitás, consultá con la dirección.» Corresponde a PT-05 a PT-09.

**Contratos:**
- OP-01, OP-02, OP-04, OP-05 y OP-06 devuelven ME-13 cuando falta el permiso.
- OP-03, que es pública, no lo devuelve.

**Dónde se aplicó:**
- Tabla 8.6, con 13 mensajes;
- Tabla 9.4, con los contratos;
- Ejemplo resuelto 9.1;
- Figura 9.1, donde la capa de presentación dice «ME-01 a ME-13»;
- Tabla 9.6, fila RNF-02: «PT-03, ME-12, ME-13; zonas» y las operaciones con permiso;
- contratos de referencia OP-04 y OP-05 de la guía;
- clave 2 del Encuentro 17.

## 4. Controles nuevos (bloque R del verificador, 15 controles)

**Zonas, roles y contratos:**
- cada zona tiene roles y cada pantalla con operación la nombra;
- los roles de la zona de cada pantalla son los que admite su operación;
- la precondición de cada contrato nombra exactamente esos roles, o dice que la operación es pública;
- cada ingreso desde PT-03 lleva a una zona que admite ese rol;
- cada rol llega por el mapa a las pantallas de su zona;
- PT-09 y OP-05 quedan para los dos roles, con comprobación en el servidor.

**Autenticación y autorización:**
- ME-12 es solo de PT-03 y no habla de permisos;
- ME-13 es distinto de ME-12;
- ningún contrato usa ME-12;
- toda operación con roles tiene ME-13, y la pública no;
- ningún texto del libro, la guía, el cuaderno ni los contratos asocia ME-12 con falta de permiso;
- ME-13 figura en la matriz, la Tabla 8.6 y la guía.

**Prueba de los propios controles:** se les dan tres errores a propósito y los detectan los tres:
- PT-09 como exclusiva de un rol;
- OP-05 con roles distintos de los de su zona;
- ME-12 como «sin permiso» en un contrato.

**Impresión:** se agrega el control 6, «Cortes de tabla». Ninguna tabla repartida deja menos de dos filas de datos en una página. El control se agregó porque la Tabla 8.6, ahora más larga, dejaba la fila ME-13 sola en la página siguiente; ahora se encadenan también las dos últimas filas de cada tabla larga.

## 5. Documentos regenerados

| Documento | v1.1 | Páginas que cambian |
|---|---|---|
| Libro del estudiante | Regenerado (35 págs.) | 1 (versión), 15, 16, 17, 20, 21, 27, 28 y 30 |
| Guía docente | Regenerada (16 págs.) | 1 (versión), 7, 8, 11, 12 y 13 |
| Cuaderno de prácticas | **No se regeneró**: ninguna práctica cambia. Es idéntico, byte a byte, al de la v1.0. | — |

**Plan anual:** no cambia. Los indicadores de las fichas son los mismos, y el generador se volvió a ejecutar sin diferencias.

## 6. Resultados

| Programa | v1.0 | v1.1 |
|---|---|---|
| `build/verificar.py` | 200 correctos, 0 fallos | **216 correctos, 0 fallos** (agrega el bloque R y el control de la v1.0 conservada) |
| `build/controles_finales.py` | 18 controles, 0 fallos | **22 controles, 0 fallos** (agrega cortes de tabla) |
| `build/prueba_fuentes.py` | 9 combinaciones, 0 fallos | **9 combinaciones, 0 fallos** |
| `plan_anual/plan_anual_preliminar.py` | Correcto | Correcto, sin cambios |

Se mantienen sin fallos:
- todas las filas de todas las tablas, en los tres PDF;
- figuras con su epígrafe;
- H3 en página propia;
- evaluaciones en página propia;
- cuaderno igual al libro.

## 7. Láminas nuevas

- `revision_visual/16_v1_1_libro_paginas_afectadas.png`
- `revision_visual/17_v1_1_guia_paginas_afectadas.png`
- `revision_visual/18_v1_0_frente_a_v1_1_mapa_de_navegacion.png`
- `revision_visual/19_v1_1_tabla_8_6_con_ME_13.png`

Las páginas afectadas se detectaron comparando, página por página, el texto y la imagen de los PDF de la v1.0 y la v1.1 (`revision_visual/paginas_afectadas_v1_1.json`). Las láminas 01 a 15 se regeneraron desde los PDF de la v1.1; las de la v1.0 están en `version_1_0/revision_visual/`.

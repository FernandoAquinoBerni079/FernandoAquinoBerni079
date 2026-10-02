# 01_DIAGNOSTICO — Algorítmica 3.er Curso BTI · Edición Esencial Comercial 2026

Fecha: 02/10/2026 · Responsable: Claude (constructor) · Estado: diagnóstico previo a la construcción.

## 1. Paquete analizado (versiones vigentes en Drive, carpeta `Algoritmica_3er_Curso`)

| Pieza | Archivo | Última modificación | Observación |
|---|---|---|---|
| Tomo | Algoritmica_3er_Curso_TOMO_COMPLETO.docx | 27/08/2026 | 110 páginas (A4), 21 clases, 28 figuras, 6 evaluaciones |
| Cuaderno | Algoritmica_3er_Curso_CUADERNO_PRACTICAS.docx | 27/08/2026 | 26 páginas, 21 prácticas + Proyecto Final Integrador |
| Solucionario | Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE.docx | 27/08/2026 | Respuestas de clases, evaluaciones y prácticas |
| Plan Anual | Algoritmica_3er_Curso_PLAN_ANUAL.docx | 27/08/2026 | 36 encuentros / 144 HC; filas por clase (8 h en las clases con continuación) |
| Planes de Clase | Algoritmica_3er_Curso_PLANES_DE_CLASE.docx | 27/08/2026 | 36 planes de 4 HC (160 min) |
| Programa | DISEÑO CURRICULAR ALGORITMICA - MAYO 2026 (1).pdf | — | Tercer curso, págs. 77–79 |
| Otra fuente | ALGORITMICA PRELIMINAR(1).pdf | 31/07/2026 | Versión preliminar del tomo (no es fuente oficial) |

Los originales no se modificaron. Se trabajó sobre copias locales.

## 2. Cobertura del programa oficial (Tercer curso)

| Contenido del programa | Clase(s) | Estado |
|---|---|---|
| Lenguajes de programación: tipos, campos de aplicación | 1, 2 | Cubierto |
| Lenguajes imperativa, funcional, lógica, orientada a objetos: propiedades | 3 | Cubierto |
| Importancia de los distintos tipos de lenguajes | 4 | Cubierto |
| Bases de datos: conceptos, características, tipos, aplicación | 5, 6 | Cubierto |
| Componentes, tablas, relacionamiento; clave principal y secundaria; integridad referencial | 8, 9 | Cubierto. **Ambigüedad terminológica**: el tomo iguala «clave secundaria» a «clave foránea» sin aclarar que en otros textos significa clave alternativa o índice secundario |
| SGBD: gestión, propósitos, inconvenientes, redundancia, inconsistencia, aislamiento, integridad, atomicidad, concurrencia, seguridad | 7 | Cubierto |
| Niveles de abstracción físico, lógico y de vistas | 10 | Cubierto (sin diagrama) |
| Tipos de usuario | 10 | Cubierto |
| DDL y DML | 10 | Cubierto |
| Modelos de datos: E-R, orientado a objetos, lógico basado en registros, lógico basado en objetos | 11 | Cubierto, pero la tabla omite «lógico basado en objetos» |
| Entidades, tipos de atributos, ligaduras de correspondencia, claves, DER | 12–14 | Cubierto |
| Tipos de atributos simple/compuesto, univalorado/multivalorado, derivado | 12 | Cubierto (sin diagrama de notación) |
| Cuestiones de diseño: uso de conjuntos de entidades **o atributos** y de entidades **o relaciones** | 14 | **Parcial**: se trata el atributo que debe ser entidad; falta el criterio entidad o relación |
| Ligaduras 1:1, uno a varios, **varios a uno**, varios a varios | 13 | Cubierto; falta decir explícitamente que N:1 es la 1:N leída al revés |
| Reglas de normalización: atributo, clave, dominio, relacionamiento, **grado de relacionamiento** | 12–17 | **Falta «grado de la relación»** (unaria, binaria, ternaria) |
| Dependencia funcional, funcional compuesta o completa, transitiva | 16, 17 | Cubierto; conviene nombrar la DF «compuesta o completa» con el término del programa |
| Técnicas, procedimientos, normativas; casos prácticos | 15, 17, 18–21 | Cubierto |
| Uso de un gestor de bases de datos (Access) | 18–21 | Cubierto (justificado por «programación de base de datos utilizando un gerenciador») |
| Práctica conductual | Transversal | Actitudinal; se trabaja en prácticas y Proyecto |

**Conclusión:** las 21 clases cubren el programa. **No se cambia la estructura curricular.** Se agregan dentro de las clases existentes los puntos faltantes: grado de relación (Clase 13), entidad o relación (Clase 14), N:1 (Clase 13), modelo lógico basado en objetos (Clase 11) y la aclaración sobre clave secundaria (Clase 8).

## 3. Extensión real por clase (desarrollo sin ficha ni actividades)

Mínimo de la Edición Esencial para Media/BT: 750 palabras.

| Clase | Palabras | Ítems de actividad | Figuras |
|---|---|---|---|
| 1 | 1.305 | 9 | 1 |
| 2 | 1.642 | 10 | 3 |
| 3 | 1.139 | 9 | 1 |
| 4 | 1.157 | 9 | 1 |
| 5 | 1.394 | 9 | 1 |
| 6 | 1.293 | 9 | 1 |
| 7 | 1.084 | 9 | 1 |
| 8 | 1.521 | 10 | 2 |
| 9 | 1.280 | 9 | 2 |
| 10 | 1.055 | 9 | **0** |
| 11 | 1.014 | 9 | 1 |
| 12 | 1.252 | 9 | **0** |
| 13 | 1.283 | 9 | 2 |
| 14 | 1.134 | 9 | 2 |
| 15 | 1.220 | 9 | 2 |
| 16 | 1.376 | 9 | **0** |
| 17 | 1.331 | 9 | 1 |
| 18 | 1.329 | 9 | 2 |
| 19 | 1.190 | 9 | 2 |
| 20 | 1.297 | 9 | 1 |
| 21 | 1.254 | 9 | 2 |

Ninguna clase está por debajo del mínimo; la más corta tiene 1.014 palabras. **No se rellena texto.** Las ampliaciones responden a huecos técnicos o del programa. Las clases 10, 12 y 16 no tienen ningún diagrama; el estándar gráfico los exige en materias procedimentales.

## 4. Correspondencia Clase N ↔ Práctica N y ejercicios repetidos

- La numeración es 1:1 (21 ↔ 21), pero **las 21 prácticas repiten el ejemplo resuelto o las actividades de su clase**. Coincidencias de datos detectadas automáticamente: P1 (14.000 / 3.000 / 8.000 = ejemplo resuelto de la Clase 1), P6 (los seis precios del catálogo), P8 (V3→C01), P9 (C01 y C09), P13 (V5 y gaseosa), P15 (filas de V1), P19 (V1–V5 del ejemplo resuelto), P20 (C01→V1/V3 y C04→V5, ya resueltos en la tabla de la clase), P21 (todos los totales de la clase).
- Las prácticas sin números repiten consignas: P2 (los mismos tres fragmentos de la tabla de niveles), P3 (Prolog/Java/C/Haskell = actividad 3 de la Clase 3), P4 (el mismo caso del Copetín de la caja Ejemplo), P10 (las mismas cuatro tareas de la actividad 6), P12–P14, P16 y P17 (el mismo modelo del Copetín ya resuelto en la clase).
- La mayoría de las prácticas tiene una sola actividad de tres pasos. Eso no alcanza para un encuentro propio de 4 HC: el Plan Anual asigna encuentro propio a las prácticas 4–10, 18, 19 y 21.
- Todo el trabajo de diseño (DER, transformación, normalización) usa el mismo caso: no hay contextos alternativos.

## 5. Respuestas reveladas dentro de actividades y evaluaciones

- Clase 1, act. 6; Clase 3, act. 6: piden exactamente el ejemplo resuelto (2 chipas y 1 gaseosa, G. 14.000).
- Clase 6, act. 5: «Escribí la lista de productos (usá los datos de la clase)»: es copiar.
- Clase 13, act. 6; Clase 15, act. 6; Clase 19, act. 5, 6 y 9; Clase 20, act. 4–6; Clase 21, act. 4–6: la respuesta está en el texto o en la tabla de la misma clase.
- Evaluación U1, ítem 8: repite la caja «Ejemplo» de la Clase 1 (3 empanadas + 2 gaseosas = G. 34.000).
- Evaluación U4, ítems 5 y 6, y Evaluación de la 2.ª etapa, ítems 7 y 8: **la respuesta va escrita entre paréntesis en la consigna** («resultado esperado (V1 y V2)», «(V5, G. 50.000)», «(Rosa 48.000…)»).
- Varios puntos de control de las prácticas dan el resultado completo («El resultado son V1 (C01) y V2 (C02)»).

## 6. Errores conceptuales y técnicos (revisión especial, clases 13–17 incluidas)

| N.º | Clase | Problema | Gravedad |
|---|---|---|---|
| T1 | 14 | El texto dice que «contiene» lleva **solo** el atributo cantidad (sección «El DER del Copetín», paso 4 del ejemplo resuelto, act. 3 y act. 8), mientras que la Figura 3.2 y la Clase 15 llevan cantidad **y** precio_unitario | Crítico (incoherencia interna) |
| T2 | Solucionario | Ev. U3 ítem 6 y Ev. 2.ª etapa ítem 4: DER con «contiene» solo con cantidad | Crítico (tomo ↔ solucionario) |
| T3 | 15 | La tabla de la Figura 3.3 rotula «DetalleVenta» la columna de la venta y muestra nombres de producto en vez de códigos (la FK es el código) | Mayor |
| T4 | 15 | Control final: «tres FK del mismo tipo (texto de 3 caracteres)»; los códigos de venta V1–V5 tienen 2 caracteres | Menor |
| T5 | 15 | Traducción 1:1: se omite que la FK debe llevar índice **sin duplicados** (UNIQUE). Sin esa restricción, la relación pasa a ser 1:N | Mayor |
| T6 | 12 ↔ 13/15 | El «renglón» aparece como entidad débil en la Clase 12 y como atributos de la relación N:M en las clases 13–15, sin explicar que son dos modelados equivalentes | Mayor |
| T7 | 16 | Tabla de anomalías: «De borrado: al borrar una venta se pierde el dato del producto». Solo ocurre si era la única venta de ese producto | Mayor |
| T8 | 16 | Caja «la cuenta de la redundancia»: «once renglones × 5 datos ≈ 55 celdas redundantes». Es incorrecto: la primera aparición de cada dato no es redundante. Contado columna por columna, son **34 celdas** | Crítico (dato falso) |
| T9 | 16 | Caja rotulada «En Paraguay — dependencia funcional» que solo define DF: el rótulo no corresponde al contenido | Menor |
| T10 | 16 | No se distingue una DF (regla del negocio) de una coincidencia de los datos: con los seis precios distintos, «precio → producto» se cumple en los datos pero no es una DF | Mayor (riesgo de concepto incorrecto) |
| T11 | 17 | El ejemplo resuelto no dice dónde queda el nombre del cliente después de la 2FN y luego lo «separa» en la 3FN: el paso intermedio queda implícito | Mayor |
| T12 | 17 | Act. 6: «el precio del producto viola la 2FN en DetalleVenta» no distingue precio de catálogo de precio_unitario (el texto sí los distingue) | Mayor |
| T13 | 17 | Falta advertir que una tabla en 1FN con clave simple está automáticamente en 2FN (error frecuente) | Mayor |
| T14 | 19 | Fechas en Access: no se advierte que en la vista SQL los literales `#…#` se escriben en orden mes/día/año, ni que en la cuadrícula se interpretan según la configuración regional. Con 04/03/2026 el error es silencioso (3 de abril) | Mayor |
| T15 | 20 | La tabla de funciones de la fila Total aparece en la Clase 20, aunque el propio texto dice que los totales recién se enseñan en la Clase 21 | Mayor (secuencia) |
| T16 | 20 | «“an” devuelve Empanada y Ana Gómez (según la tabla)»: mezcla dos tablas en un solo resultado | Menor |
| T17 | 8 | «Clave foránea (secundaria)»: falta la aclaración terminológica de §2 | Mayor |
| T18 | 13 | No se menciona el grado de la relación (programa); no se explicita N:1 | Mayor (cobertura) |
| T19 | 11 | La tabla de modelos omite «lógico basado en objetos» (programa) | Menor |
| T20 | 9 / 18 | «Anular la referencia» se presenta sin aclarar que Access solo ofrece en la ventana Relaciones las casillas «Actualizar en cascada» y «Eliminar en cascada» | Menor |
| T21 | 18 | No se explica cómo crear la clave principal compuesta de DetalleVenta en la vista Diseño (solo aparece en la práctica) | Menor |
| T22 | 1–21 | Numeración de figuras por unidad (Figura 1.3 aparece antes que la 1.1; en la Clase 2 están la 1.1, la 1.2 y la 1.4). El protocolo pide numerar por clase | Menor |

Pseudocódigo: los fragmentos del tomo (`total ← 2 × 3000`, recorrido con acumulador) son correctos. Las prácticas en PSeInt que se agreguen deben respetar su sintaxis (`Algoritmo … FinAlgoritmo`, `Leer`, `Escribir`, `Si … Entonces … SiNo … FinSi`, `Para … Hasta … Hacer … FinPara`).

Bases de datos (comprobado con un script): las claves, las FK y las cardinalidades del caso son coherentes. La transformación a cuatro tablas es correcta y la normalización llega correctamente a 3FN. Las once filas de DetalleVenta reconstruyen G. 134.000 por cliente (48.000/19.000/17.000/50.000), por categoría (23.000/63.000/48.000) y por producto (18.000/5.000/18.000/45.000/8.000/40.000). La venta promedio es G. 26.800.

## 7. Coherencia del caso Copetín Karumbé

El caso funciona pedagógicamente y sus números cierran, así que se conserva. Su problema es el agotamiento: los ejercicios, las prácticas y las evaluaciones giran sobre las mismas cinco ventas. Para la nueva edición:

- **Semana 2 del Copetín** (solo en las prácticas de Access 18–21): ventas V6–V11 del 09 al 11/03/2026, dos productos nuevos (P07 Jugo natural, P08 Sopa paraguaya), dos clientes nuevos (C05 Teresa Villalba, C06 Hugo Cáceres) y un **aumento de la gaseosa a G. 9.000** el 10/03, que obliga a usar precio_unitario y no el precio de catálogo.
- **Contextos alternativos** en las prácticas de diseño: biblioteca escolar, talleres del colegio, cantina escolar y librería del barrio.

## 8. Coherencia con solucionario, Plan Anual y Planes de Clase

- Solucionario: ver T2. Todas sus respuestas de prácticas quedan obsoletas al reescribirse las prácticas.
- Plan Anual y Planes: remiten a «Cuadernillo del estudiante» y «Cuaderno de Prácticas». Los cierres citan puntos de control con datos que cambian (por ejemplo, «el total debe dar G. 14.000»). Los planes de continuación (10 encuentros) describen prácticas de una sola actividad.
- El Plan Anual agrupa 2 encuentros en una fila de «8 h». El modelo de Software 1.º usa una fila por encuentro (36 filas numeradas igual que los 36 planes).

## 9. Imágenes

Las 28 figuras son diagramas; varias tienen el acabado de las imágenes trabajadas con Gemini. Se conservan **sin cambios** (sin recortar ni recomprimir): solo se renumeran y se ajustan sus epígrafes. Ninguna lleva el rótulo «generada con IA». No hay ilustración de portada para Algorítmica: queda pendiente para Gemini. Mientras tanto, la portada usa un esquema gráfico construido por Claude, que es un diagrama y no una ilustración.

## 10. Identidad visual

Algorítmica 1.º–3.º tiene registrada la identidad **VERDE BTI** (#1B5E20 / #2E7D32), compartida por la serie BTI (excepción de serie documentada en `identidades.md` §8). Las 28 figuras del tomo están dibujadas en esa paleta, con acento ámbar. Se mantiene el verde de la serie con **acento ámbar (#B8860B / #F2C14E)** propio de Algorítmica, en lugar del amarillo de Software 1.º. Si Fer prefiere otro color, las figuras quedarían desentonadas, porque las de Gemini no se tocan.

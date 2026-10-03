# NOTAS_PILOTO_ALGORITMICA_3_ESENCIAL_v2

**Algorítmica · 3.er Curso BTI · Edición Esencial Comercial 2026 — Ronda de correcciones v2**

**Estado: CORREGIDO — pendiente de auditoría final de ChatGPT y aprobación de Fer.**

El paquete **no está listo para la venta**. Esta ronda aplica correcciones puntuales a partir de la auditoría independiente de ChatGPT y de las decisiones finales de Fer. No se reconstruyó el paquete. No cambiaron las 21 clases, los 36 encuentros, las 144 HC, las 4 unidades ni el caso integrador.

Fecha: 03/10/2026.

## 1. Archivos

La versión auditada (v1) se conserva sin cambios. Los archivos v2 llevan el sufijo `_v2`.

| Pieza | Archivo v2 | Páginas | v1 |
|---|---|---|---|
| Libro | Algoritmica_3er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026_v2 (.docx y .pdf) | 154 | 155 |
| Solucionario | Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026_v2 (.docx y .pdf) | 24 | 22 |
| Planes de Clase | Algoritmica_3er_Curso_PLANES_DE_CLASE_ESENCIAL_COMERCIAL_2026_v2 (.docx y .pdf) | 75 | 75 |
| Plan Anual | Algoritmica_3er_Curso_PLAN_ANUAL_ESENCIAL_COMERCIAL_2026_v2 (.docx y .pdf) | 8 | 7 |
| Muestra comercial | Algoritmica_3er_Curso_MUESTRA_COMERCIAL_2026_v2.pdf | 18 | 18 |

Los originales de Drive (TOMO_COMPLETO, CUADERNO_PRACTICAS, SOLUCIONARIO_DOCENTE, PLAN_ANUAL y PLANES_DE_CLASE) tampoco se tocaron.

## 2. Tabla de hallazgos y correcciones

En la columna de ubicación, «L» es el libro, «S» el solucionario, «PA» el Plan Anual y «PC» los Planes de Clase. Los números de página son los del PDF v2.

| N.º | Hallazgo de ChatGPT / decisión de Fer | Corrección aplicada | Archivo/página | Estado |
|---|---|---|---|---|
| 1.1 | Fichas con capacidades reformuladas o fusionadas | Las 21 fichas reproducen letra por letra la capacidad del programa (DISEÑO CURRICULAR – MAYO 2026, Tercer curso, págs. 77–79). Cuando una capacidad abarca varias clases, se repite (ver §3). Los indicadores no se tocaron. | L, ficha de cada clase; PC, los 36 planes | CORREGIDO |
| 1.2 | La Clase 10 tenía una sola capacidad fusionada | La ficha muestra las tres capacidades oficiales: niveles de abstracción, tipos de usuario y lenguajes de manipulación de datos. | L p. 66; PC p. 34 | CORREGIDO |
| 1.3 | Faltaba la nota sobre capacidades e indicadores | Se agrega al Plan Anual el texto acordado («Las capacidades se reproducen textualmente…»). | PA p. 2 | CORREGIDO |
| 1.4 | Faltaba la capacidad transversal | El Plan Anual incluye «Reconoce la importancia de la práctica Conductual en el desarrollo de las actividades.» y explica cómo se trabaja: prácticas, trabajo colaborativo, responsabilidad sobre los datos y Proyecto Final. También figura en las capacidades de los talleres del PFI. | PA p. 2 y banda del PFI; PC, planes 33–35 | CORREGIDO |
| 1.5 | Las bandas de unidad del Plan Anual resumían las capacidades | Cada banda lista ahora las capacidades textuales del programa para esa unidad. Los planes de talleres y de evaluaciones integradoras también llevan capacidades textuales. | PA pp. 2–8; PC | CORREGIDO |
| 2 | La Clase 8 presentaba «clave secundaria» como sinónimo de clave foránea | Se reemplaza el recuadro por el texto acordado y el tema de la ficha pasa a «…Clave principal, clave foránea y el término “clave secundaria”». En la clave de la Evaluación de la Unidad 2, la respuesta es «clave foránea»; si el estudiante escribe «clave secundaria», se acepta cuando explica que referencia la clave principal. | L p. 53; S p. 21 | CORREGIDO |
| 3.1 | Profundidad de la entidad débil | La Clase 12 suma una tabla de conceptos: entidad fuerte, entidad débil, dependencia de existencia, discriminante (identificador parcial) y relación identificadora. También explica la notación (doble rectángulo, doble rombo y subrayado discontinuo). | L p. 82 | CORREGIDO |
| 3.2 | Decía que RENGLÓN y la N:M producen «exactamente la misma tabla» | Se reemplaza con la idea de Fer y se agrega el ejemplo comparativo: Caso A con PK (venta, producto) y Caso B con RENGLÓN y discriminante nro_renglón, PK (venta, nro_renglón). Se agrega cuándo aparece una entidad asociativa. Los textos de las Clases 13–15 no cambian. | L pp. 82–83 | CORREGIDO |
| 3.3 | La solución del desafío de la Práctica 12 (CUOTA débil) | Ahora usa la misma terminología: discriminante nro_cuota, relación identificadora y doble rombo. | S, Práctica 12 | CORREGIDO |
| 4 | El histórico de precios aparecía como «fuera del mini-mundo» | En la Clase 11 se reemplaza por el texto acordado: el precio de catálogo vive en Productos y precio_unitario conserva lo cobrado. | L p. 78 | CORREGIDO |
| 5.1 | Perfil de PSeInt sin precisar | Se indica el perfil Flexible: en la Práctica 1 se elige desde Configurar → Opciones del Lenguaje (perfiles)…, y la Práctica 3 lo vuelve a nombrar. El nombre del menú se tomó del propio PSeInt 20250314. | L pp. 10 y 24 | CORREGIDO |
| 5.2 | Práctica 3: faltaba definir i | Se usa el texto acordado: «Definí total, importe e i como Entero y promedio como Real; inicializá total en 0.» | L p. 24 | CORREGIDO |
| 5.3 | Práctica 2: el texto del error de división por cero no estaba comprobado | El libro usa el texto neutro acordado y pide registrar el mensaje de la versión instalada. El solucionario documenta lo que se comprobó, ver §4. | L p. 18; S p. 15 | CORREGIDO |
| 5.4 | Verificación de las Prácticas 1–3 | Se ejecutaron todos los casos en PSeInt 20250314 para Linux con el perfil Flexible, desde el intérprete por línea de comandos. Resultados en §4. | S pp. 15–16 | CORREGIDO (intérprete). La interfaz gráfica queda como VERIFICACIÓN MANUAL PENDIENTE (§4) |
| 5.5 | Hallazgo propio de la verificación: «←» y «=» | PSeInt no reconoce el carácter «←» escrito en el editor. Además, el perfil Flexible acepta «=» como asignación, así que el error frecuente «asignar con =» era impreciso. La Práctica 1 indica escribir <-, y el solucionario explica ambos puntos. | L p. 10; S p. 15 | CORREGIDO |
| 6.1 | Interfaz base de Access | La Clase 18 incluye una sola vez la frase de referencia a Access 2016 en castellano. No se afirma que sea «la versión actual» ni «la más utilizada». | L p. 120 | CORREGIDO |
| 6.2 | «La clave principal marcada con estrella» | Se reemplaza por «la clave principal identificada con el icono/indicador de clave». Por coherencia, «dos llaves» pasa a «dos iconos de clave» en la Clase 18, la Práctica 18 y el solucionario. | L pp. 120–121 y 125; S | CORREGIDO |
| 6.3 | Nombres de comandos de Access | Se ajustaron cuatro cosas: el tipo de dato se llama «Autonumeración» y no «autonumérico» (Clases 8 y 15 y Práctica 8); la importación usa la ruta de Access 2016, «Datos externos → Importar y vincular → Excel», porque «Nuevo origen de datos» es de versiones posteriores; la Clase 21 dice dónde se elige la referencia cruzada; y la exportación usa el botón «PDF o XPS». Las casillas de cascada de la Práctica 18 aparecen con su nombre completo y Sí/No. | L pp. 53, 123, 125, 142–143 | CORREGIDO en el texto; los rótulos exactos quedan como VERIFICACIÓN MANUAL PENDIENTE (§5) |
| 7.1 | Fechas en la respuesta de la Evaluación de la Unidad 4 | Se usa la respuesta acordada: «En la cuadrícula de Diseño con configuración regional d/m/a: #05/03/2026# → V5. En la vista SQL: #3/5/2026#.», más la cantidad esperada (1 registro). | S p. 22 | CORREGIDO |
| 7.2 | Las demás respuestas con fechas | Las seis respuestas de actividades con fechas (Clases 19 y 20) y la de la Práctica 19 indican el criterio de lectura: cuadrícula con d/m/a o vista SQL. La Clase 19 declara que todos los criterios del libro están escritos en la cuadrícula con configuración d/m/a, y la Práctica 19 lo recuerda en «Lo que necesitás saber». | L pp. 131 y 133; S | CORREGIDO |
| 8.1 | Puntos de control de las Prácticas 18–21 | Se usan los cuatro reemplazos acordados. La Práctica 20 recibe además «da la cantidad total de renglones de DetalleVenta» (antes decía 13), y la Práctica 21 (Actividad 3) ya no anticipa que la diferencia se explica con un solo renglón. | L pp. 126, 133, 139, 145–146 | CORREGIDO |
| 8.2 | Otros puntos de control que revelaban el resultado | Se reescribieron 10 más: P2 (decía cuántos fragmentos no necesitan herramienta), P4 (margen del ganador), P5 Act. 1 y 3 (adelantaban que hay menos préstamos que renglones y la distribución por nivel), P7 Act. 1 y 3 (enumeraban los tres problemas y adelantaban la atomicidad), P8 (decía de qué tabla salen las flechas), P9 (una integridad por situación), P10 (los cuatro tipos de usuario) y P13 (los tres grados). Ahora piden evidencia y justificación. Los resultados numéricos quedan solo en el solucionario. En total, contando 8.1 y el punto 9, son 17 puntos de control reescritos. | L pp. 18, 30, 38, 50, 58, 65, 70, 92 | CORREGIDO |
| 9 | Punto de control de la Práctica 3 que enumeraba los paradigmas | Se usa el texto acordado («Clasificaste los seis fragmentos…»). | L p. 24 | CORREGIDO |
| 10 | Continuaciones que podían quedar cortas para 120 minutos | Se agrega «Transferencia y revisión entre pares» (30–40 min) solo en las cinco continuaciones en papel con actividades breves: P5 (libreta de fiados), P6 (inventario del laboratorio), P8 (taller mecánico), P9 (docentes y materias) y P10 (base de la cantina). Cada una trae un mini-caso con otros datos, intercambio, detección de al menos un error, corrección y justificación escrita. La solución está en el solucionario y el plan de continuación la incluye en el Desarrollo y en el Cierre. En P4, P7, P18, P19 y P21 no se agregó porque ya alcanzan. El Plan Anual y los 36 encuentros no cambian. | L pp. 39, 45, 59, 65, 71; S pp. 16–17; PC pp. 16, 20, 28, 32, 36 | CORREGIDO |
| 11.1 | Recuadros «En Paraguay» con contenido universal | Se revisaron los 43 recuadros de contexto del libro: 3 conservan «En Paraguay» (§6); 14 pasan a «Aplicación profesional» (10) o «Ejemplo cotidiano» (4); 9 se integran al texto como párrafo común; y 17 se eliminan porque repetían el desarrollo o un recuadro cercano. No se inventó ningún dato paraguayo. Los Planes de Clase se actualizaron para no citar recuadros eliminados. | L; PC | CORREGIDO |
| 11.2 | Clases 13, 14 y 20 | Clase 13: «cardinalidades de la vida real» pasa a Ejemplo cotidiano y «las N:M piden atención» se integra al texto. Clase 14: queda una sola «Aplicación profesional» y se eliminan dos recuadros repetidos. Clase 20: se eliminan los dos «En Paraguay» y queda la «Aplicación profesional» que ya existía. | L | CORREGIDO |
| 11.3 | Que «Aplicación profesional» o «Ejemplo cotidiano» no fueran mecánicos | Seis clases (3, 8, 9, 15, 16 y 19) no tienen ninguno de los dos, y ninguna clase tiene más de dos. | L | CORREGIDO |
| 12 | Formulario e informe del PFI | Dejan de figurar entre los requisitos mínimos. Se agrega el texto acordado de «Extensión recomendada»; los entregables y el Taller 3 lo nombran como extensión, y no suman puntaje obligatorio. | L p. 152; PC p. 72 | CORREGIDO |
| 13 | Rúbrica del PFI | Se convierte en rúbrica analítica: los mismos cinco criterios y pesos (25/25/20/15/15), cuatro niveles (Logrado, En proceso, Inicial y No presentado con 100/60/30/0 % del peso) y, en cada celda, la evidencia observable y los puntos. | S p. 23 | CORREGIDO |
| 14.1 | Residuo en la Práctica 14 («✓ o ✗») | Se cambia por «Respondé cada pregunta con Sí o No». También se quitan ✓ y ✗ de la Práctica 18, del solucionario y del texto del tomo (23 marcas ✔/✓ en ejemplos resueltos). | L p. 98 | CORREGIDO |
| 14.2 | Símbolo ✅ de los puntos de control | Lo dibujaba una fuente de emoji (NotoColorEmoji) y podía perderse al convertir o copiar. Se retira; el recuadro verde ya identifica el punto de control. | L, todas las prácticas | CORREGIDO |
| 14.3 | Búsqueda de residuos | Controles automáticos sobre los cuatro documentos: glifos faltantes (U+FFFD y U+25A1), fuentes de emoji en el PDF, marcadores de figura, comillas o paréntesis vacíos, punto doble, espacio antes de puntuación, palabras repetidas y referencias a figuras inexistentes. Se revisaron además a mano los párrafos sin puntuación final: todos son títulos o celdas de tabla. | Los 4 documentos | CORREGIDO (0 hallazgos) |
| 14.4 | Hallazgo propio | Ocho recuadros del tomo traían el cuerpo pegado al título. Se separan, sin cambio visible, para que los controles los lean bien. | L | CORREGIDO |
| 15 | Lo que no debía cambiar | Se comprobó con la auditoría automática: 21 clases, 36 encuentros, 144 HC, 4 unidades, N:1, grados, tabla puente, FK única en 1:1, precio de catálogo frente a precio_unitario, DF como regla, DF completa, parcial y transitiva, 1FN → 2FN → 3FN, ejemplo de normalización, 34 celdas, G. 134.000 / 26.800, G. 135.000 / 22.500, 33 registros, V8 a G. 8.000 frente al catálogo de G. 9.000 y los contextos alternativos. | Todos | NO APLICA: sin cambios, verificado |

## 3. Capacidades del programa por clase

| Clases | Capacidad textual del programa MEC |
|---|---|
| 1, 2 | Reconoce los diferentes tipos de lenguajes de programación y sus campos de aplicación. |
| 3 | Establece diferencias entre los distintos lenguajes de programación existentes en el mercado. |
| 4 | Reconoce la importancia de los diferentes tipos de lenguajes de programación existentes. |
| 5, 6, 19, 20, 21 | Reconoce los conceptos requeridos en la programación de base de datos utilizando un gerenciador de base de datos. |
| 7 | Utiliza conceptos de sistema de gestión de base de datos, propósitos, inconvenientes, redundancia e inconsistencia de datos en la creación de Bases de Datos. |
| 8, 9 | Analiza la composición de una base de datos. |
| 10 | Identifica los diferentes niveles de abstracción de los datos. · Analiza los tipos de usuarios de base de datos. · Reconoce los diferentes lenguajes de manipulación de datos más utilizados. |
| 11 | Analiza los diferentes modelos de datos. |
| 12 | Aplica los conceptos fundamentales en la construcción de entidades. |
| 13, 14 | Trabaja con el modelo Entidad Relación en la representación de los datos. |
| 15, 18 | Ejecuta técnicas, procedimientos y normativas en el desarrollo de entidades normalizadas. |
| 16, 17 | Utiliza las reglas de la normalización (1FN- 2FN- 3FN) para la obtención de datos agrupados en diferentes entidades. |
| Talleres PFI | Las de las clases 15/18 y 19–21, más la transversal («práctica Conductual»). |
| Transversal (Plan Anual) | Reconoce la importancia de la práctica Conductual en el desarrollo de las actividades. |

Asignaciones que Fer puede querer revisar:

- **Clase 15** (Del DER a las tablas) usa «Ejecuta técnicas, procedimientos y normativas…». También podría usar «Trabaja con el modelo Entidad Relación…».
- **Clases 19–21** (consultas en Access) usan «Reconoce los conceptos requeridos en la programación de base de datos utilizando un gerenciador…», la única capacidad del programa que nombra el gerenciador.

## 4. PSeInt: verificación ejecutada

- **Versión:** PSeInt 20250314, paquete oficial para Linux de 64 bits (pseint-l64-20250314.tgz, SourceForge).
- **Perfil:** Flexible, con el archivo `perfiles/Flexible` de la distribución.
- **Modo:** intérprete por línea de comandos (`pseint archivo.psc --profile=… --input=…`). La interfaz gráfica usa el mismo intérprete, pero no se abrió.
- **Archivos .psc probados:** carpeta `pseint_v2/` del repositorio.

| Práctica | Caso | Resultado obtenido |
|---|---|---|
| 1 | 3 mbeju, 2 cocidos, pago 50.000 | «Total: 28000  Vuelto: 22000» |
| 1 | 1 mbeju, 1 cocido, pago 10.000 | «El pago no alcanza» |
| 1, desafío | 3, 2, 50.000 / 1, 1, 10.000 | «Total: 26000  Vuelto: 24000» / «El pago no alcanza» |
| 2, sintaxis | Sin FinSi | «ERROR 117: Falta cerrar SI.», antes de ejecutar |
| 2, lógica | cantMbeju + 5000 | «Total: 18003  Vuelto: 31997», sin aviso |
| 2, ejecución | total / ventasDelDia con 0 | Muestra total y vuelto, luego «ERROR 296: Division por cero» |
| 3 | Seis importes de la semana 2 | Traza 19.000 → 36.000 → 65.000 → 84.000 → 93.000 → 135.000; «Promedio: 22500» |
| 3, desafío | Contador de ventas mayores a 20.000 | 2 |
| 3, error frecuente | total ← 0 dentro del ciclo | Muestra 42000 |
| 3, error frecuente | promedio Entero con un promedio no exacto | «ERROR 314: No coinciden los tipos…» |
| Sintaxis | Carácter «←» en el archivo | No reconocido («Caracter no válido») |
| Sintaxis | total = 2 * 3000 | Flexible lo acepta; Estricto lo rechaza |

**VERIFICACIÓN MANUAL PENDIENTE:** abrir los tres algoritmos en la interfaz gráfica de PSeInt del laboratorio y confirmar dos cosas: que el perfil Flexible aparece con ese nombre en Configurar → Opciones del Lenguaje (perfiles)…, y que el botón «Ejecutar Paso a Paso» y el menú Archivo → Exportar (a C o Python) están donde dice la Práctica 2. Los rótulos se tomaron del binario de la versión 20250314.

## 5. Access 2016: VERIFICACIÓN MANUAL PENDIENTE

Access no se pudo ejecutar en el entorno de construcción. Los rótulos usados en el libro son los de Access 2016 en castellano tal como se conocen; las cifras esperadas de cada consulta se verificaron con un script sobre los mismos datos. Falta comprobar en un equipo con Access 2016 en castellano:

| Rótulo usado en el libro | Dónde | Comprobar |
|---|---|---|
| Herramientas de base de datos → Relaciones | Clase 18, Práctica 18 | Pestaña y botón |
| Exigir integridad referencial / Actualizar en cascada los campos relacionados / Eliminar en cascada los registros relacionados | Clases 9 y 18, Práctica 18 | Texto exacto de las tres casillas |
| Crear → Diseño de tabla / Diseño de consulta | Clases 18–19 | Botones |
| Botón Totales; fila «Total»; Agrupar por, Suma, Promedio, Cuenta, Máx, Mín | Clase 21, Práctica 21 | Que diga «Cuenta» y no «Recuento» en la fila Total |
| Referencias cruzadas: Asistente para consultas o cambio de tipo en la vista Diseño | Clase 21, Práctica 21 | Nombre del botón de tipo de consulta (puede figurar como «General» o «Tabla de referencias cruzadas») y nombre de la fila |
| Datos externos → PDF o XPS | Clase 21, Práctica 21 | Botón del grupo Exportar |
| Datos externos → Importar y vincular → Excel | Clase 18 | Grupo y botón (en compilaciones de Microsoft 365 aparece «Nuevo origen de datos») |
| Indexado: «Sí (Sin duplicados)», Limitar a la lista, Requerido, Regla de validación | Clases 15 y 18, Práctica 18 | Nombres de propiedades |
| Autonumeración, Texto corto, Moneda, Fecha/Hora | Clases 8 y 18 | Nombres de tipos de datos |
| Es igual a…, Alternar filtro, Inicio → Ver → Vista SQL | Práctica 19 | Menú contextual y botones |

## 6. Recuadros «En Paraguay» que se conservan

| Clase | Recuadro | Por qué se conserva |
|---|---|---|
| 5 | Bases de datos que usás sin darte cuenta | Nombra registros paraguayos concretos y verificables: el padrón electoral y el sistema Marangatú de la DNIT. |
| 8 | Códigos que identifican | Cédula, RUC y matrícula de vehículo: identificadores paraguayos reales. |
| 9 | Por qué importa | Relaciona la integridad referencial con la facturación ante la DNIT. |

## 7. Auditoría automática

`build/auditoria.py` → `build/auditoria_resultado.txt`: **861 controles, 0 fallos**. Son los 729 controles de v1, adaptados a los nombres v2, más un bloque «I» de 132 controles nuevos, uno por cada punto de esta ronda.

| Bloque | Controles | Fallos |
|---|---|---|
| A. Estructura y correspondencia | 129 | 0 |
| B. Paginación, índice, saltos y encabezados | 125 | 0 |
| C. Coherencia aritmética | 13 | 0 |
| D. Libro ↔ solucionario | 78 | 0 |
| E. Duplicados | 46 | 0 |
| F. Figuras | 7 | 0 |
| G. Plan Anual y Planes de Clase | 281 | 0 |
| H. Lengua, residuos y cobertura curricular | 50 | 0 |
| I. Correcciones v2 | 132 | 0 |

## 8. Para la auditoría final de ChatGPT

1. Revisar las asignaciones de capacidad de §3, en especial las de las Clases 15 y 19–21.
2. Leer la ampliación de entidad débil de la Clase 12 (pp. 82–83) y juzgar si el nivel es adecuado para 3.er curso BTI.
3. Revisar los cinco mini-casos de transferencia y sus soluciones.
4. Revisar los 17 puntos de control reescritos (8.1, 8.2 y 9).
5. Verificar que los 14 recuadros retitulados aporten valor y no sean relleno.

## 9. Pendiente de decisión de Fer

- Aprobar o cambiar las asignaciones de capacidad de §3.
- Hacer la verificación manual de Access 2016 (§5) y de la interfaz de PSeInt (§4) en el laboratorio.
- Encargar a Gemini la ilustración de portada (sigue pendiente desde v1).
- Elegir el sello o nombre de colección (sigue pendiente).
- Subir los archivos v2 a Drive y, cuando apruebe esta edición, mover los originales a SUPERSEDIDOS.

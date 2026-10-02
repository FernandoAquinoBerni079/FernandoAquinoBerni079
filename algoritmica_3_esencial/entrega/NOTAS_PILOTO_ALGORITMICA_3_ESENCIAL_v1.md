# Algorítmica 3.er Curso BTI — Edición Esencial (v1, 02/10/2026)

**Estado: Listo para auditoría independiente de ChatGPT y aprobación de Fer.**

No está aprobado para la venta. Los archivos originales del paquete (TOMO_COMPLETO, CUADERNO_PRACTICAS, SOLUCIONARIO_DOCENTE, PLAN_ANUAL y PLANES_DE_CLASE) no se modificaron ni se sobrescribieron.

## Archivos del combo

| Archivo | Páginas | Peso del .docx |
|---|---|---|
| Algoritmica_3er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026 (.docx y .pdf) | 155 | 4,7 MB |
| Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026 (.docx y .pdf) | 22 | 0,3 MB |
| Algoritmica_3er_Curso_PLANES_DE_CLASE_ESENCIAL_COMERCIAL_2026 (.docx y .pdf) | 75 (36 planes) | 0,4 MB |
| Algoritmica_3er_Curso_PLAN_ANUAL_ESENCIAL_COMERCIAL_2026 (.docx y .pdf) | 7 (36 encuentros) | 0,3 MB |
| Algoritmica_3er_Curso_MUESTRA_COMERCIAL_2026.pdf | 18 | — |

La muestra comercial reúne la portada, la presentación, el índice, la prueba diagnóstica, la Unidad 1 con la Clase 1 y la Práctica 1, la contraportada, las portadas del solucionario, del plan anual y de los planes, la primera hoja del plan anual y el Plan de Clase N.º 1.

Como en el piloto de Software 1.º, el conector de Drive no permite subir archivos de este tamaño. Los archivos finales se entregan por el chat y en la rama de trabajo del repositorio; Fer los sube a la carpeta del paquete.

## Qué cambió

### 1. Estructura: un solo libro

- El Cuaderno de Prácticas deja de existir como libro aparte. El orden es: Clase N (ficha, desarrollo, actividades) → Práctica N (en página propia, fotocopiable). Así de la Clase 1 a la 21, y después el Proyecto Final Integrador.
- Las evaluaciones van en páginas propias: banda ámbar para las de unidad (4) y banda azul para las de etapa (2), después de la práctica que cierra cada unidad.
- La estructura curricular es la misma: 4 unidades y 21 clases con la misma numeración y las mismas fichas. Las 21 clases cubren el programa oficial (ver 01_DIAGNOSTICO, §2). Los puntos del programa que faltaban se agregaron dentro de las clases existentes.
- La portada a página completa, la contraportada y las portadas del material docente siguen la plantilla de la Edición Esencial de Software 1.º.
- El índice viene poblado: dos niveles (unidades; clases, prácticas y evaluaciones) y números de página verificados contra el PDF. No aparece la leyenda «Ctrl+E/F9».

### 2. Las 21 prácticas, reescritas por completo

Las prácticas anteriores repetían el ejemplo resuelto o las actividades de su clase. Las nuevas usan datos y contextos distintos, siempre con el formato competencia → lo que necesitás saber → actividades (objetivo, modelo, pasos, punto de control) → desafío final.

| Prácticas | Entorno | Contexto |
|---|---|---|
| 1–3 | PSeInt | Pedido para llevar del Copetín; errores de sintaxis, ejecución y lógica provocados a propósito; acumulador con la recaudación de la semana 2 |
| 4–10 | Papel | Biblioteca escolar (decisión tecnológica, cuaderno de préstamos, claves, integridad, vistas) y cantina del colegio (SGBD, permisos, transacciones) |
| 11–13 | Papel | Club Atlético Yvága, un club de barrio inventado (mini-mundo, entidades, cardinalidades) |
| 14–16 | Papel | Talleres del colegio (DER con N:M, 1:N y 1:1; transformación; anomalías y dependencias) |
| 17 | Papel | Librería Arasa'i (normalización 1FN → 3FN con verificación de importes) |
| 18–21 | Microsoft Access | Semana 2 del Copetín: V6–V11 del 09 al 11/03/2026, productos P07–P08, clientes C05–C06, un cliente sin teléfono (Es Nulo) y la gaseosa que sube a G. 9.000 el 10/03, para obligar a usar precio_unitario |

- Las 10 prácticas que tienen encuentro propio en el Plan Anual (4–10, 18, 19 y 21) traen 3 actividades; las demás, 2.
- Los puntos de control permiten verificar el trabajo sin dar la respuesta. Por ejemplo: «el vuelto más el total deben dar exactamente lo pagado», o «la cantidad de tablas es igual a entidades más relaciones N:M». Algunos dan un conteo para la autocorrección, como «cargaste 33 registros».

### 3. Actividades, evaluaciones y diagnóstica

- Las 21 clases tienen 215 ítems de actividad: entre 10 y 11 por clase, con un mínimo Esencial de 8. Hay **57 ítems nuevos o reescritos**: reemplazan los que repetían el ejemplo resuelto o tenían la respuesta en el propio texto de la clase.
- Las 6 evaluaciones se rehicieron. Se quitaron las respuestas que estaban entre paréntesis en las consignas (Ev. U4, ítems 5 y 6; Ev. 2.ª etapa, ítems 7 y 8) y los ítems repetidos de la caja «Ejemplo» (Ev. U1, ítem 8) o de otras evaluaciones (Ev. 1.ª etapa, ítem 1, igual al ítem 3 de U1). La evaluación de la Unidad 3 usa un caso nuevo, la veterinaria Jaguarete, para medir la transferencia del diseño a otro contexto.

### 4. Correcciones técnicas (diagnóstico T1–T22), con atención a las clases 13 a 17

| Código | Clase | Corrección |
|---|---|---|
| T1/T2 | 14 + solucionario | «contiene» lleva cantidad **y** precio_unitario en todo el libro y el solucionario. Antes el texto, el ejemplo resuelto y las actividades decían solo cantidad |
| T3 | 15 | La tabla de DetalleVenta muestra las FK (venta, producto) con código; antes la columna de la venta estaba rotulada «DetalleVenta» y aparecían nombres en lugar de códigos |
| T4 | 15 | «Texto de 3 caracteres» pasa a «el mismo tipo de dato que la clave (Texto corto)» |
| T5 | 15 | 1:1: la FK debe declararse sin duplicados (Indexado «Sí (Sin duplicados)»); sin esa restricción la relación degenera en 1:N. Se agrega el término «tabla puente» |
| T6 | 12 | Se explica que el renglón de venta como entidad débil y como atributos de la relación «contiene» son modelados equivalentes que producen la misma tabla |
| T7 | 16 | La anomalía de borrado se da al borrar la **única** venta de un producto o de un cliente |
| T8 | 16 | La cuenta de redundancia de la tabla única es **34 celdas**, contadas columna por columna (antes: «11 × 5 ≈ 55»). Verificado por script |
| T9 | 16 | La caja «En Paraguay — dependencia funcional» pasa a «Concepto clave» |
| T10 | 16 | Nueva sección «Dependencia funcional: regla, no coincidencia» (precio → producto se cumple en los datos pero no es DF), con el término del programa «DF compuesta o completa» |
| T11 | 17 | El ejemplo de normalización muestra que, tras la 2FN, el nombre del cliente queda en Ventas y que la 3FN corta la cadena venta → cliente → nombre |
| T12 | 17 | Act. 6: distingue el precio de catálogo (va a Productos) de precio_unitario (queda en DetalleVenta) |
| T13 | 17 | Errores frecuentes: una tabla con clave simple en 1FN ya está en 2FN; no sacar precio_unitario; atomicidad ≠ partirlo todo |
| T14 | 19 | Fechas en Access: la cuadrícula usa la configuración regional (d/m/a) y la vista SQL, m/d/a; se indica cómo probar con fechas sin ambigüedad. La Práctica 19 lo hace comprobar en la vista SQL |
| T15 | 20 → 21 | La tabla de funciones de la fila Total se traslada a la Clase 21, porque adelantaba contenido |
| T16 | 20 | El buscador «an» ya no mezcla dos tablas en un mismo resultado |
| T17 | 8 | Aclaración sobre «clave secundaria»: en el programa equivale a clave foránea; en otros textos significa clave alternativa o índice secundario |
| T18 | 13 | Nueva sección «Grado de una relación» (unaria, binaria y ternaria, con figura, tabla y ejemplo) y la ligadura «varios a uno» como 1:N leída al revés |
| T19 | 11 | Se agrega el «modelo lógico basado en objetos» del programa |
| T20 | 9, 18 | Opciones reales de Access: «Actualizar en cascada» y «Eliminar en cascada»; «anular referencia» no se configura desde la ventana Relaciones |
| T21 | 18 | Cómo crear la clave principal compuesta en la vista Diseño (Ctrl + Clave principal) |
| T22 | todas | Las figuras se numeran por clase (Figura N.M) y se ajustan las referencias cruzadas |

Además se agregaron recuadros de **Errores frecuentes** en las clases 13, 15, 16, 17 y 19, y la sección **Cuestiones de diseño: ¿entidad, atributo o relación?** en la Clase 14 (programa). PSeInt se describe como intérprete que ejecuta sin generar un ejecutable (C2) y figura como «pseudocódigo de PSeInt», no como lenguaje (C3). Las 7 menciones de «tomo» o «cuadernillo» pasan a «libro».

### 5. Profundidad

No se rellenó texto: las 21 clases ya superaban el mínimo Esencial de 750 palabras (antes: mínimo 1.014; ahora: mínimo 1.078 y máximo 1.776). Las ampliaciones responden a huecos técnicos o del programa (§4).

### 6. Figuras

- Las **28 figuras originales se conservan byte a byte**, sin recortar ni recomprimir (control automático por hash). Solo cambian su número y su epígrafe.
- **4 diagramas nuevos** hechos por Claude con el estándar gráfico (matplotlib, verde BTI con acentos): 10.1 niveles de abstracción, 12.1 notación de atributos, 13.3 grado de una relación y 16.1 diagrama de dependencias funcionales. Así ninguna clase técnica queda sin figura.
- La Figura PFI.1 (mapa de la solución) se tomó del Cuaderno anterior, sin cambios.
- Ningún epígrafe dice «generada con IA».
- Portada y contraportada: plantilla de colección con una lámina-esquema propia (tablas, DER y consulta), que es un diagrama y no una ilustración. **La ilustración de portada queda pendiente para Gemini.**

### 7. Solucionario, Plan Anual y Planes de Clase

- El **Solucionario** se genera desde las mismas fuentes que el libro, así que no puede quedar ninguna respuesta de ejercicios viejos. Contiene: orientaciones de la diagnóstica; respuestas de los 215 ítems; resultado esperado y errores frecuentes de las 21 prácticas; claves de las 6 evaluaciones con puntaje sugerido (18 puntos); orientaciones y rúbrica del Proyecto Final Integrador (pesos 25/25/20/15/15 y niveles de logro).
- **Plan Anual**: 36 filas, una por encuentro, con la misma numeración que los planes. Se respetan los 36 encuentros y las 144 HC de la planificación oficial existente. Capacidades e indicadores son literales de las fichas del libro (no se tocaron). Procedimientos e instrumentos son únicos (36 y 36) y se mantienen los de la planificación anterior en las 21 clases. Las 10 continuaciones prácticas tienen procedimientos e instrumentos propios.
- **Planes de Clase**: los 36 planes conservan el formato V3. Las viñetas de los planes de clase se actualizaron por regla (material = «el libro»; figuras renumeradas; rangos de actividades y números de «Pensá y decidí» según la edición nueva; puntos de control de las prácticas nuevas). Los 10 planes de continuación y los 3 talleres del Proyecto se reescribieron a partir de las prácticas y los requisitos nuevos. Los planes de laboratorio (PSeInt o Access) incluyen una alternativa en papel.
- Ningún documento menciona ya «Cuaderno de Prácticas», «cuadernillo» ni «tomo».

### 8. Identidad visual

Se mantiene el **VERDE de la serie BTI** (#1B5E20 / #2E7D32), que es la identidad registrada de Algorítmica 1.º–3.º y la paleta en la que están dibujadas las 28 figuras. Para distinguirla de Software 1.º, el acento es **ámbar/oro (#F2C14E)** en lugar del amarillo. Cambiar el color de fondo dejaría desentonadas las figuras de Gemini, que no se tocan.

## Control automático (auditoria.py)

Resultado: **729 controles, 0 fallos**.

| Bloque | Controles | Qué verifica |
|---|---|---|
| A. Estructura y correspondencia | 129 | 21 clases, 21 prácticas, orden Clase N → Práctica N, títulos, numeración, fichas, mínimo de actividades, 3 actividades en las continuaciones |
| B. Paginación, índice, saltos y encabezados | 125 | Cada entrada del índice contra su página del PDF (libro, solucionario y planes); cada práctica y evaluación abre página; pie en todas las páginas salvo portada y contraportada; encabezado «· continuación» de los planes; .docx < 25 MB; metadatos; PDF posterior al .docx; cantSplit al 100 % |
| C. Coherencia aritmética | 13 | 134.000, 135.000, 136.000 (trampa), 33 registros, 34 celdas y otros cálculos |
| D. Libro ↔ solucionario | 78 | Cada consigna y su respuesta; prácticas; opción múltiple coherente; sin respuestas viejas; sin respuestas en el libro ni en las consignas |
| E. Duplicados | 46 | Práctica N vs. ejemplos resueltos de la Clase N; consignas, objetivos e ítems de evaluación sin repeticiones |
| F. Figuras | 7 | Numeración por clase, epígrafes, originales intactas, anuncio en el texto, referencias cruzadas |
| G. Plan Anual y Planes | 281 | 36 encuentros; indicadores literales; unicidad; figuras, prácticas, rangos de actividades y «Pensá y decidí» citados en cada plan; tiempos de 160 min |
| H. Lengua, residuos y cobertura | 50 | Voseo; residuos («Cuaderno», «cuadernillo», «tomo», «Ctrl+E», «{FIG»); sin institución ni ciudad; 37 contenidos del programa presentes |

La paginación se verificó con LibreOffice. Si al abrirlo en Word cambian los números, se actualiza el índice con F9.

## Para la auditoría de ChatGPT

1. **Clases 13 a 17**: revisar con especial rigor las secciones nuevas (grado de relación, cuestiones de diseño, 1:1 con FK única, DF regla vs. coincidencia, recuadros de errores frecuentes) y el ejemplo de normalización corregido (T11).
2. **Prácticas 1–3 en PSeInt**: PSeInt no está disponible en el entorno de construcción, así que los esqueletos se revisaron contra la sintaxis documentada, sin ejecutarlos. Conviene ejecutarlos una vez con el perfil de lenguaje que usa el colegio. La Práctica 2 provoca una división por cero a propósito; ver si el mensaje que muestra PSeInt le resulta claro al estudiante.
3. **Prácticas 18–21 en Access**: Access tampoco estaba disponible para ejecutar los pasos; las cifras esperadas se verificaron por script con los mismos datos. Validar los pasos en la versión de Access del laboratorio (nombres de menús en castellano: «Herramientas de base de datos», «Limitar a la lista», «Datos externos → PDF o XPS»). La Práctica 19 depende de la configuración regional d/m/a del equipo.
4. **Puntos de control**: juzgar si alguno revela demasiado (por ejemplo, «Cargaste 33 registros», «el filtro mostró 2 de las 6 ventas») o si, al revés, alguno se queda corto para que el estudiante pueda autocorregirse.
5. **Recuadros «En Paraguay»**: varios son generales (Clases 13, 14 y 20) y no citan una norma ni un organismo concreto. Proponer anclajes paraguayos verificables si los considera insuficientes.
6. **Evaluación de la Unidad 3 con caso nuevo (veterinaria)**: evaluar si la transferencia a otro contexto es adecuada o si prefiere el Copetín.
7. **Equivalencia entidad débil / relación con atributos (Clase 12)**: verificar que la aclaración no confunda a nivel de bachillerato.
8. **Los 10 planes de continuación**: verificar que las actividades 2 y 3 alcanzan para 120 minutos (100 cuando se aplica la evaluación de unidad).
9. **Paginación en Word**: algunas prácticas terminan con media página en blanco (el desafío final), y las evaluaciones ocupan 2 páginas cada una.

## Pendiente de decisión de Fer

- Aprobar o cambiar la identidad (verde BTI con acento ámbar) y encargar a Gemini la ilustración de portada de Algorítmica.
- Sello o nombre de colección (sigue pendiente del piloto).
- Confirmar que las prácticas en PSeInt (1 a 3) se hacen en el laboratorio de 3.er curso.
- Subir los archivos a la carpeta del paquete y mover los originales a SUPERSEDIDOS cuando apruebe esta edición.

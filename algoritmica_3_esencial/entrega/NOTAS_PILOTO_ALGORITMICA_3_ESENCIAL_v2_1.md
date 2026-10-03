# NOTAS_PILOTO_ALGORITMICA_3_ESENCIAL_v2_1

**Algorítmica · 3.er Curso BTI · Edición Esencial Comercial 2026 — Corrección de cierre v2.1**

**Estado: CORREGIDO — pendiente de comprobación manual de Access/PSeInt y aprobación de Fer.**

El paquete no está declarado listo para la venta.

Fecha: 03/10/2026. Esta es una corrección puntual sobre la v2: no se reconstruyó ni se reformateó el paquete. No cambian la numeración, las actividades, los cálculos ni la estructura curricular. Las versiones v1 y v2 se conservan; los archivos nuevos llevan el sufijo `_v2_1`.

## 1. Archivos

| Pieza | Archivo v2.1 | Páginas |
|---|---|---|
| Libro | Algoritmica_3er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026_v2_1 (.docx y .pdf) | 154 (igual que v2) |
| Solucionario | Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026_v2_1 (.docx y .pdf) | 24 (igual) |
| Planes de Clase | Algoritmica_3er_Curso_PLANES_DE_CLASE_ESENCIAL_COMERCIAL_2026_v2_1 (.docx y .pdf) | 75 (igual) |
| Plan Anual | Algoritmica_3er_Curso_PLAN_ANUAL_ESENCIAL_COMERCIAL_2026_v2_1 (.docx y .pdf) | 8 (igual) |
| Muestra comercial | Algoritmica_3er_Curso_MUESTRA_COMERCIAL_2026_v2_1.pdf | 18 (igual) |

El índice del libro no cambia. Solo varía el texto de las páginas 7, 45, 61–62, 68–69, 100, 133 y 142; en 62 y 69 es apenas un reacomodo dentro de la misma clase.

## 2. Correcciones aplicadas

| N.º | Pedido de Fer | Corrección aplicada | Archivo/página | Estado |
|---|---|---|---|---|
| 1 | Capacidad de la Clase 15 | Ahora dice: «Trabaja con el modelo Entidad Relación en la representación de los datos.» Los indicadores no cambian. En el Plan Anual, la banda de la Unidad 3 lista solo las capacidades de sus clases (C10–C13). La capacidad «Ejecuta técnicas, procedimientos y normativas…» queda en la Clase 18 y en los talleres del PFI. | Libro p. 100; Planes, plan 23 (pp. 48–49); Plan Anual, banda de la Unidad 3 (p. 5) | CORREGIDO |
| 2 | Recuadro «En Paraguay» de la Clase 9 | Pasa a llamarse «En Paraguay — integridad y facturación» y lleva el texto acordado, sin más detalle tributario. El plan de la Clase 9 cita el título nuevo. | Libro p. 61 | CORREGIDO |
| 3 | Práctica 6, Actividad 3 | El paso 2 usa el texto acordado («Clasificá los objetos según su función principal…»), y el solucionario, el texto sobre las capas de datos/consulta e interfaz/presentación. Ya no aparece la dicotomía «gestor/aplicación». | Libro p. 45; Solucionario p. 16 | CORREGIDO |
| 4 | Punto de control de la Práctica 19, Actividad 2 | Se usa el texto acordado («…juntos y sin superposición, reconstruyen el conjunto completo de Ventas.»). | Libro p. 133 | CORREGIDO |
| 5 | Recuadros de oficio de las Clases 1 y 10 | Se retiran «Aplicación profesional — programar como oficio» (Clase 1) y «Aplicación profesional — un oficio con demanda» (Clase 10). Su contenido pasa al texto común como párrafo, sin recuadro de reemplazo. | Libro pp. 7 y 68 | CORREGIDO |
| 6 | Rutas de Access confirmadas por la documentación oficial de Microsoft | La Clase 21 indica las dos rutas: «Crear → Asistente para consultas → Asistente para consultas de referencias cruzadas» y, en la vista Diseño, «Tipo de consulta → Tabla de referencias cruzadas». La Clase 18 ya tenía «Datos externos → Importar y vincular → Excel». Se dan por confirmadas. | Libro pp. 123 y 142 | CORREGIDO |

## 3. Verificación manual que sigue pendiente

Solo quedan los rótulos que dependen de la interfaz instalada en el laboratorio.

| Programa | Qué comprobar | Dónde |
|---|---|---|
| Access 2016 | En la fila Total, si la operación dice «Cuenta» o «Recuento» | Clase 21, Práctica 21 |
| Access 2016 | El texto de las casillas de la ventana Modificar relaciones: «Exigir integridad referencial», «Actualizar en cascada los campos relacionados» y «Eliminar en cascada los registros relacionados» | Clases 9 y 18, Práctica 18 |
| Access 2016 | Los menús contextuales y botones del filtro: «Es igual a…», «Alternar filtro», «Ver → Vista SQL» | Práctica 19 |
| Access 2016 | Los nombres de las propiedades y tipos de datos: Indexado «Sí (Sin duplicados)», Limitar a la lista, Autonumeración | Clases 8, 15 y 18 |
| PSeInt (interfaz gráfica) | Que el perfil Flexible aparezca en Configurar → Opciones del Lenguaje (perfiles)…, y la ubicación de «Ejecutar Paso a Paso» y de Archivo → Exportar | Prácticas 1–3 |

Los algoritmos de las Prácticas 1–3 ya se ejecutaron en v2 con el intérprete de PSeInt 20250314 y el perfil Flexible (ver NOTAS_PILOTO v2, §4).

Ya se consideran confirmadas por la documentación oficial de Microsoft: Datos externos → Importar y vincular → Excel; Crear → Asistente para consultas → Asistente para consultas de referencias cruzadas; y Tipo de consulta → Tabla de referencias cruzadas.

## 4. Auditoría automática

Resultado: **874 controles, 0 fallos**. Son los 861 de v2 más un bloque «J» de 13 controles, uno por cada pedido de esta corrección.

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
| J. Corrección de cierre v2.1 | 13 | 0 |

## 5. Pendiente

- Hacer la comprobación manual de §3 en el laboratorio.
- Aprobación de Fer.
- Ilustración de portada (Gemini) y sello de colección, que siguen pendientes desde v1.
- Subir los archivos v2.1 a Drive; una vez aprobados, mover las versiones anteriores a SUPERSEDIDOS.

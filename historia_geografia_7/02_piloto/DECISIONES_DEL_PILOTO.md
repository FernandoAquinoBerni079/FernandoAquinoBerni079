# Piloto de diseño: Historia y Geografía 7.º

**Estado:** muestras para que Fernando elija el formato. No reemplazan a ningún archivo comercial. Fernando aprueba antes de aplicar nada al combo completo, y ChatGPT audita página por página.

**Qué se generó:**
- Todos los PDF salen de LibreOffice. En Word la paginación puede variar algunas líneas.
- Las fuentes del documento se reemplazaron por equivalentes métricos: Arial por Liberation Sans y Calibri por Carlito.
- Los scripts están en `scripts/` y regeneran todo.

## 1. Tomo: tres variantes con el mismo contenido

**Muestras:** portada, presentación, índice, Unidad 1 con la Clase 1 (Historia), Clase 14 (Historia), Clase 18 (Geografía), Continuación F y Evaluación de la Unidad 5.

**Texto e imágenes intactos.** `scripts/verificar_tomo.py` lo comprueba en las tres variantes:
- las mismas 2.773 palabras del DOCX base, en el mismo orden;
- las 5 imágenes idénticas byte a byte;
- las imágenes conservan su proporción y solo se reducen si no entran en el ancho útil.

**Cambios por variante:**

| Variante | Archivo | Papel y márgenes | Cuerpo | Cambios |
|---|---|---|---|---|
| A. Oficio actual corregido | `tomo/TOMO_PILOTO_oficio_actual` | Oficio, 1,27 cm (sin cambios) | 10,5 pt (sin cambios) | Solo saltos: cada unidad, clase, continuación y evaluación en hoja nueva |
| B. Oficio mejorado | `tomo/TOMO_PILOTO_oficio_mejorado` | Oficio, 2,0 cm a los lados, 2,2 cm arriba y 2,0 cm abajo | 11,5 pt (+1 pt en todo) | <ul><li>los saltos de A;</li><li>opciones a) a d) en uno o dos renglones;</li><li>tres renglones para cada pregunta abierta y uno para justificar cada V/F.</li></ul> |
| C. A4 mejorado | `tomo/TOMO_PILOTO_a4_mejorado` | A4, 1,8 cm a los lados, 2,0 cm arriba y abajo | 11,5 pt | Lo mismo que B |

**Mediciones del PDF** (`tomo/medicion_tomo.json`):

| | A | B | C |
|---|---|---|---|
| Páginas de la muestra | 12 | 14 | 16 |
| Páginas de contenido (sin portada, presentación ni índice) | 9 | 11 (+22 %) | 13 (+44 %) |
| Dónde empieza cada sección | 4 % a 5 % superior de su página | 7 % superior | 7 % a 8 % superior |
| Índice con número de página real | Sí, estable en dos pasadas | Sí | Sí |
| Tomo completo, estimación (*) | unas 80 págs. | unas 95 a 100 | unas 110 a 115 |

(*) Es una extrapolación de la muestra sobre el tomo completo generado con el mismo programa (72 págs.). El costo de impresión depende de esa cifra.

**Recomendación: B, oficio mejorado.**
- Mantiene el papel que ya se usa, con márgenes que admiten fotocopia y anillado.
- La letra es legible y deja espacio para escribir, que hoy no existe.
- Cuesta unas 20 páginas más que A.
- La C solo conviene si el cliente pide A4: es la más cómoda, pero la más larga.

## 2. Planes de clase: A4 vertical (`planes/PLANES_PILOTO_A4`)

**Planes de la muestra:**

| Plan | Encuentro | Por qué está en la muestra |
|---|---|---|
| 1 | Clase de Historia, con la prueba diagnóstica | Clase histórica |
| 28 | Clase 18 | Corregido (§3) |
| 29 | Continuación F | Continuación |
| 30 | Evaluación U5 | Evaluación |
| 31 | Clase 19 | Clase geográfica, con dos correcciones a la Clase 19 |

**Maqueta:**
- A4 vertical, 2,0 cm a los lados y 1,8 cm arriba y abajo.
- Cuerpo de 10,5 pt y tablas de 10 pt.
- Portada sola e índice solo, con número de página real.
- Cada plan empieza en hoja nueva y ocupa 2 páginas. Los 36 planes darían unas 74 páginas (hoy son 37).

**Contenido nuevo de cada plan:**
- **Propósito del encuentro.**
- **Secuencia minuto a minuto:** qué hace el docente, qué hacen los alumnos y el producto de cada fase. Asigna las 12 actividades de la clase entre la clase y la tarea.
- **Atención a la diversidad**, con apoyos y un desafío.
- **Evaluación** con criterios observables.
- **Precisiones para el docente:** dónde el tomo tiene un error o le falta contenido, y cómo manejarlo en clase mientras no se corrija.
- **Tarea.**

**Origen de los campos:** Capacidad, Tema e Indicadores se copian de la ficha del tomo. No se presentan como capacidades oficiales del MEC hasta hacer el cotejo (diagnóstico §4).

## 3. Plan 28 corregido

| Campo | Antes (corrido) | Ahora |
|---|---|---|
| Tema | Elementos y factores del clima… (de la Clase 19) | La hidrografía. La Hidrovía Paraguay-Paraná. Recursos naturales y su preservación. |
| Indicadores | Los del clima | Reconoce los principales ríos del Paraguay. Explica la importancia de la Hidrovía. Valora la preservación de los recursos naturales. |
| Desarrollo | Tiempo y clima, elementos y factores, tereré (de la Clase 19) | Ríos y mapa (15 a 30 min), usos y represas (30 a 45), Hidrovía y fuente (45 a 65), cuidado del agua (65 a 80) y actividades (80 a 95) |

El Plan 27 tiene el mismo problema en el Tema y los Indicadores. Su corrección está en el diagnóstico (§7) y se aplica con el combo completo.

## 4. Plan anual: A4 contra oficio horizontal

**Lo que no cambia:** el mismo documento y el mismo texto. No se cortó nada.

**Lo que cambia:**
- columnas proporcionales: de cada 26,7 cm, 0,9 / 5,0 / 6,3 / 1,7 / 5,2 / 4,2 / 3,4, para N.º, Temas, Indicadores, Tiempo, Procedimientos, Instrumentos y Observación;
- encabezado repetido en cada hoja;
- filas que no se parten.

| | Original | A4 piloto | Oficio piloto |
|---|---|---|---|
| Letra de la tabla | 8,5 pt | 9,5 pt | 10 pt |
| Columnas | 7 iguales de 3,82 cm | Proporcionales, 26,7 cm | Proporcionales, 30,0 cm |
| Páginas | 9 | 8 | 8 |

**Recomendación: A4 horizontal.**
- El oficio gana medio punto de letra.
- El plan anual suele entregarse a la dirección junto con otros documentos en A4.
- Si Fernando prefiere todo el combo en oficio, la versión oficio está lista.

## 5. Solucionario (`solucionario/SOLUCIONARIO_PILOTO_A4`)

**Secciones de la muestra:** Clase 18, Continuación F y Evaluación U5.

**Maqueta:**
- A4 vertical, letra de 10,5 pt y criterios de corrección en 10 pt.
- Una tabla por bloque de actividades: N.º | Respuesta | Criterio de corrección.

**Cambios respecto del solucionario actual:**
- **Numeración igual a la del tomo:** 1 a 12, sin reiniciar en cada bloque.
- **Página del tomo** de cada sección.
- **Criterios de corrección** para todas las respuestas abiertas, incluidas las respuestas parciales.
- **La continuación en su lugar** de la secuencia, no al final.
- **Puntaje total** de la evaluación, que incluye la Parte C complementaria del Plan 30.

**Extensión estimada del solucionario completo:** 30 a 35 páginas (hoy son 17).

## 6. Decisiones para Fernando

1. **Tomo:** variante A, B o C.
2. **Planes:** confirmar el formato de dos páginas por plan, con secuencia minuto a minuto.
3. **Plan anual:** A4 u oficio.
4. **Solucionario:** confirmar la maqueta con criterios de corrección.
5. **Contenido:** ¿se amplía el tomo con lo que falta (§6 del diagnóstico) o solo se corrigen los errores?
   - **Ampliar** cambia el número de páginas de §1 y requiere fuentes reales y mapas nuevos.
   - **Corregir solamente** deja los encuentros cortos para 120 minutos. Los planes lo compensan con la secuencia, pero no lo resuelven.

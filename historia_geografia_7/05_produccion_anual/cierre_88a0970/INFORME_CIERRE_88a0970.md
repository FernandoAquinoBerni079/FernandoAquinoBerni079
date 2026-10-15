# Historia y Geografía 7.º — Informe de cierre de la versión candidata (corrección de 88a0970)

Fecha: 15 de octubre de 2026
Rama: `claude/hg7-cierre-88a0970`, derivada de `88a0970`
Estado: **versión candidata para el control final de Fernando.** No es una aprobación comercial.

## 1. Alcance

Se corrigieron los 18 hallazgos del dictamen definitivo de Work sobre `88a0970` (Drive 1700rOr4_U3Z_ZYbvNPIvNYbz_t2WHu4I). El paquete correctivo de ChatGPT (`PARChe_HG7_20261015.py`) sirvió de base. No hubo rediseño: solo se tocaron los textos, las figuras y las tablas señaladas.

Insumos originales usados:
- Maestro DOCX `TOMO_OCTUBRE_MAESTRO.docx`, SHA-256 `8dbc4f44…179413`, verificado antes de construir.
- GeoJSON de Natural Earth (dominio público), el mismo de las versiones anteriores.

La resolución de cada hallazgo está en `TABLA_RESOLUCION_18_HALLAZGOS.csv`. El registro de lo que aplicó el parche está en `INFORME_APLICACION_PARCHE_HG7.json`.

## 2. Revisión del parche de ChatGPT

La mayoría de los reemplazos de texto se aplicaron tal como venían, después de revisarlos uno por uno. Cinco puntos no eran compatibles o tenían errores. Se resolvieron según el dictamen, sin suprimir ninguna validación.

| Punto | Problema en el parche | Resolución |
|---|---|---|
| BIV-01 | Por el orden de los reemplazos, la diferencia de 1.400 mm terminaba en 1.600 mm. Con las normales 1971-2000 (unos 600 a 1.800 mm) la diferencia correcta es 1.200 mm. | Corregido a «Unos 1.200 mm» en la clave de e31. Texto y plan citan Grassi (2020), MADES-STP, p. 20 impresa (p. 22 del PDF), fig. 7. |
| BI-01 | El nuevo encuadre de la Ficha B-1 no incluía Asia, así que Beringia no se podía marcar. | Mapa mudo propio (`mapa_mudo_poblamiento`) con Siberia y Alaska contiguas. El código verifica que los cinco sitios entren en el encuadre. `mapa_civilizaciones` vuelve a su firma original. |
| AN-01 | El cambio de encuadre empujaba la escala fuera de los ejes y la encimaba con la leyenda. | Lienzo más alto, franja inferior libre para la escala y espacio propio para la leyenda. |
| BI-03 | Quedaba «en discusión» en la fuente, en F1 y en el ítem 10 de e06. | Se reemplazó por la corroboración de 2023, sin afirmar unanimidad. |
| BIII-02 | El esquema de la yerba redibujado desbordaba el texto de sus cajas. | Tamaños y rótulos ajustados, con tres ramas desde Santa Fe. |

Además, se completó lo que el parche dejaba fuera del alcance de un reemplazo de texto:

- **BIII-01:** marca de la confluencia aproximada del Negro/Otuquis en la Figura 16.2, con fuente MRE/CNDL. Su rótulo se reubicó para no superponerse con el del río Paraguay.
- **BIII-05:** variante de 20 + 100 minutos en los planes 20 y 27.
- **COM-01:** nota de puntaje compartido en las matrices del solucionario.
- **COM-02:** sección «Referencias para el docente».
- **COM-03:** ancho de la columna «Capacidades» de la matriz curricular.
- **BIII-02:** respuestas modelo de e19 y e25 sobre la salida por Buenos Aires.

Los hallazgos BII-02 y BII-03, ya resueltos en `88a0970`, no se revirtieron.

## 3. Regeneración

Se regeneraron los cuatro bloques y el volumen anual, en DOCX y PDF:

- Tomo anual (oficio).
- Planes de los 36 encuentros (A4).
- Solucionario (A4).
- Plan anual (oficio).
- Matriz curricular (A4).

| Producto | Páginas |
|---|---|
| Tomo anual | __TOMO__ |
| Planes (36) | __PLANES__ |
| Solucionario anual | __SOL__ |
| Plan anual | __PA__ |
| Matriz curricular | __MATRIZ__ |

## 4. Verificación

| Verificador | Controles | Fallos |
|---|---|---|
__VERIF__

Cotejo de los 18 hallazgos (`scripts/cotejo_hallazgos_88a0970.py`, resultado en `cotejo_hallazgos.json`): __COTEJO__. Este cotejo busca en el texto de los PDF anuales lo que cada corrección debe mostrar y lo que ya no debe aparecer. También controla los totales de las ocho evaluaciones: 23, 22, 25, 28, 25, 28, 25 y 28 puntos, sin cambios.

Revisión visual a tamaño de impresión de las páginas modificadas:

- Ficha B-1 (mapa con el nordeste de Asia) y Ficha B-2.
- Figura 5.2.
- Mapa clave de la U3 y Figura 8.1.
- Ficha C muda.
- Esquema de la yerba (Figura 12.1).
- Tabla de límites y Figura 16.2.
- Figura 19.3.
- Referencias para el docente y notas de puntaje compartido del solucionario.
- Matriz curricular.
- Variantes de los planes 20 y 27.

Durante la revisión se corrigieron dos defectos que había introducido esta misma ronda:

- una página en blanco en el Bloque II, causada por la Ficha C muda, que crecía;
- la leyenda de la Figura 16.2, que se encimaba con las coordenadas del eje.

## 5. Limitaciones y pendientes, sin ocultar

- **COM-02 (parcial).** Varias fuentes quedan marcadas «edición por cotejar»:
  - Colón, Cortés, el Requerimiento, Schmidl, el testamento de Irala y Santo Tomás;
  - la síntesis arqueológica y la etnohistórica;
  - el cotejo paleográfico de la Real Provisión.
  No se inventaron ediciones ni páginas. Antes de una edición comercial hay que cotejarlas con una edición identificada.
- **COM-03 (parcial).** Se ensanchó la columna «Capacidades» de la matriz. Los cortes cortos que quedan en algunos planes y en la hoja de autoevaluación se mantienen: el dictamen les asigna prioridad menor y no se redujo la letra.
- **Ley 6676/2020.** La vigencia de la prórroga de la Ley 2524/2004 debe confirmarse antes de cada edición.
- **Impresión.** No se hizo una prueba de impresión física ni una simulación de imprenta.
- **Programa del MEC.** El cotejo contra la edición del programa del MEC (tarea 39) sigue pendiente y es independiente de este cierre.

## 6. Decisión

Esta es una versión candidata. La aprobación final corresponde a Fernando.

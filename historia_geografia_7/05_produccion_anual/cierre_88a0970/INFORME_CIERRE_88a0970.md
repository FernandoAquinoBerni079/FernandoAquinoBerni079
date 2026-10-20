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
| Tomo anual | 156 |
| Planes (36) | 74 |
| Solucionario anual | 41 |
| Plan anual | 6 |
| Matriz curricular | 2 |

## 4. Verificación

| Verificador | Controles | Fallos |
|---|---|---|
| Bloque I (`verificar.py 1`) | 1626 | 0 |
| Bloque II | 1657 | 0 |
| Bloque III | 1539 | 0 |
| Bloque IV | 1702 | 0 |
| Anual (`verificar.py anual`) | 6389 | 0 |
| Consolidación de anuales (`anuales.py`) | 1031 | 0 |

Cotejo de los 18 hallazgos (`scripts/cotejo_hallazgos_88a0970.py`, resultado en `cotejo_hallazgos.json`): 33 controles correctos, 0 fallos. En la primera corrida dio 3 fallos; los tres eran del propio cotejo, no del libro, y se corrigieron sin aflojar los controles: (a) el patrón del Pilcomayo atravesaba una coma y tomaba «entre los ríos Verde y Pilcomayo, y el tratado de paz con Bolivia» (Laudo Hayes), que es correcto; (b) el PDF de los planes corta «1971-» y «2000» en dos líneas; (c) se buscaba una frase literal del comentario del código que estaba redactada de otro modo. Este cotejo busca en el texto de los PDF anuales lo que cada corrección debe mostrar y lo que ya no debe aparecer. También controla los totales de las ocho evaluaciones: 23, 22, 25, 28, 25, 28, 25 y 28 puntos, sin cambios.

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

Las figuras de los Bloques I y IV son idénticas byte a byte a las del volumen anual, así que esos bloques no quedaron desactualizados por los últimos ajustes de figuras de los Bloques II y III.

## 5. Limitaciones y pendientes, sin ocultar

- **COM-02 (parcial).** Varias fuentes quedan marcadas «edición por cotejar»:
  - Colón, Cortés, el Requerimiento, Schmidl, el testamento de Irala y la carta de fray Domingo de Santo Tomás (1550);
  - la síntesis arqueológica y la etnohistórica;
  - el cotejo paleográfico de la Real Provisión.
  No se inventaron ediciones ni páginas. Antes de una edición comercial hay que cotejarlas con una edición identificada.
- **COM-03 (parcial).** Se ensanchó la columna «Capacidades» de la matriz. Los cortes cortos que quedan en algunos planes y en la hoja de autoevaluación se mantienen: el dictamen les asigna prioridad menor y no se redujo la letra.
- **Ley 6676/2020.** La vigencia de la prórroga de la Ley 2524/2004 debe confirmarse antes de cada edición.
- **Impresión.** No se hizo una prueba de impresión física ni una simulación de imprenta.
- **Programa del MEC.** El cotejo contra la edición del programa del MEC (tarea 39) sigue pendiente y es independiente de este cierre.

## 6. Errata posterior a 041c44f

En la revisión del commit `041c44f`, Fernando detectó una errata en las «Referencias para el docente». La fila de la Clase 14 decía «Santo Tomás de Aquino», pero la fuente que usa `e23.py` es la carta de 1550 de fray Domingo de Santo Tomás al Consejo de Indias, sobre Potosí. Se corrigió solo esa atribución en `scripts/referencias_docente.py`; la fuente sigue como «Versión escolar» y «Edición por cotejar».

Se regeneró únicamente el solucionario anual en DOCX y PDF, junto con su copia liviana. Las «Referencias para el docente» solo están en el volumen anual, así que no hacía falta tocar los solucionarios de los bloques ni los demás documentos.

- La paginación se mantiene en 41 páginas.
- Al comparar el texto página por página con la versión anterior, solo cambia la fila corregida de la página 41.
- Verificador anual: 6389 controles correctos, 0 fallos.
- Cotejo de hallazgos: 33 controles correctos, 0 fallos.
- Se revisó la página 41 a la vista.

COM-02 y COM-03 siguen como observaciones parciales.

## 7. Manifiesto

`MANIFIESTO_SHA256.txt` lista el SHA-256 de cada DOCX y PDF regenerado (bloques y anual) y de los documentos de cierre.

## 8. Decisión

Esta es una versión candidata. La aprobación final corresponde a Fernando.

## Anexo: edición compacta en papel legal

Por pedido de Fernando, el tomo se rearmó en papel legal con márgenes estrechos, con letra e interlineado menores, menos huecos y la prueba diagnóstica en hoja propia. El tomo anual pasa de 156 a 114 páginas sin perder contenido. El detalle, los controles y los huecos que quedan están en `EDICION_COMPACTA_LEGAL.md`. Los números de páginas y de controles de las secciones anteriores de este informe corresponden a la versión en oficio (`c2cf12b`).

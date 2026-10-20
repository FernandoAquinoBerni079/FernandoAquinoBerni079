# HG7: edición compacta del tomo en papel legal

Fecha: 15 de octubre de 2026
Rama: `claude/hg7-cierre-88a0970`
Pedido de Fernando: ahorrar espacio en el tomo.

## Qué se pidió

- Achicar la letra y el interlineado.
- No dejar espacios en blanco.
- Cada clase empieza en su hoja.
- Tablas sin perder contenido y adaptadas a la ventana.
- Prueba diagnóstica en hoja propia, antes de la Clase 1.
- Papel legal con márgenes estrechos.

## Qué se cambió

Los cambios son solo de maquetación; el contenido no se tocó.

| Aspecto | Antes | Ahora |
|---|---|---|
| Papel | Oficio (21,59 × 33,02 cm) | Legal (21,59 × 35,56 cm) |
| Márgenes | 2,0 / 2,0 / 2,2 / 2,0 cm | 1,27 cm en los cuatro lados («Estrecho» de Word); encabezado y pie a 0,5 cm |
| Letra del texto | 11,5 pt | 10,5 pt, el tamaño del maestro |
| Letra de recuadros y tablas | 10,5 y 10 pt | 9,5 y 9 pt |
| Interlineado | 1,15 | Sencillo |
| Espacio después de cada párrafo | 6 pt | 4 pt |
| Separador entre recuadros | Un renglón vacío | 4 pt |
| Renglones para responder | 7,8 mm | 7 mm |
| Tablas | Ancho fijo en centímetros | 100 % del ancho útil («Autoajustar a la ventana»), con las mismas proporciones de columnas |

### Cada clase en su hoja

Se mantiene la regla de antes: cada unidad, clase, continuación, ficha reproducible y evaluación empieza en hoja nueva. La primera clase de cada unidad comparte la hoja con el título de la unidad.

### Prueba diagnóstica

Sale de la Clase 1 y queda en una hoja propia, antes de la Unidad 1, con su entrada en el índice. Las consignas y las claves (D1 a D5) no cambian. En el solucionario y en la matriz curricular, las páginas del encuentro 1 la incluyen.

### Huecos

**Figuras.** Cuando una figura no entra al pie de la hoja, el texto que la sigue sube a llenar el hueco y la figura pasa a la hoja siguiente, como en imprenta. Las reglas:

- La figura puede pasar párrafos, listas, subtítulos, recuadros, tablas y recuadros de fuente o «Ubicate».
- Nunca pasa una actividad, otra figura ni el fin de la sección.
- Un subtítulo nunca queda separado de su texto.
- Las figuras se imprimen al tamaño de su lienzo (control A17); no se achicaron para que entren.

**Recuadros «Trabajá con la fuente».** Ahora tienen dos partes. El texto de la fuente puede seguir en la hoja siguiente. Las preguntas van siempre juntas, con sus tres primeros renglones.

**Renglones largos.** Una consigna con muchos renglones va unida a los cuatro primeros; los demás pueden seguir en la hoja siguiente.

**Última hoja de una sección casi vacía.** Primero se aprietan los renglones (6,3 mm) y el espacio entre párrafos de esa sección. Si así no alcanza para que la sección ocupe una hoja menos, se airea (renglones de 8,5 mm): la sección queda con las mismas hojas, pero sin una última hoja casi vacía.

**Mapa mudo de la Parte C de la Evaluación de la Unidad 5.** Pasó de 12 a 11 cm de ancho, en la figura y en el tomo, para que entre con su consigna. Así se evita una media hoja vacía.

## Resultado

| Tomo | Antes (oficio, `c2cf12b`) | Ahora (legal compacto) |
|---|---|---|
| Anual | 156 págs. | 114 págs. |
| Bloque I | 41 | 31 |
| Bloque II | 40 | 28 |
| Bloque III | 40 | 30 |
| Bloque IV | 41 | 34 |

Contenido: se compararon todas las palabras del tomo anual anterior y del nuevo. No falta texto. Las únicas diferencias son estas:

- el título nuevo «Prueba diagnóstica»;
- los encabezados de tabla que se repiten o dejan de repetirse según dónde corta la hoja (la tabla de autoevaluación y la de límites);
- dos palabras que el PDF corta distinto dentro de una celda («Gobernaba» y «Asunción b)»).

Las páginas del tomo que citan el solucionario y la matriz curricular se actualizaron solas.

## Controles

| Verificador | Controles | Fallos |
|---|---|---|
| Bloque I | 1608 | 0 |
| Bloque II | 1633 | 0 |
| Bloque III | 1519 | 0 |
| Bloque IV | 1684 | 0 |
| Anual | 6309 | 0 |
| Consolidación de anuales | 1031 | 0 |
| Cotejo de los 18 hallazgos | 33 | 0 |

La cantidad de controles cambió respecto de la versión anterior porque hay menos hojas que revisar en el control de integridad visual. Ese control (11) se adaptó a la nueva geometría: antes descartaba todo lo que estaba por debajo del 94 % del alto, una cifra pensada para los márgenes del oficio. Con márgenes estrechos, los epígrafes del final de la hoja quedaban por debajo de esa línea y no se medían. Ahora el límite es el borde real del pie de página («Página N de M»). La exigencia sigue siendo la misma.

## Huecos que quedan, a propósito

Se midieron las hojas que, sin ser la última de su sección, quedan vacías en más del 15 % de su alto. En el tomo anual quedan dos:

- **Portada (pág. 1):** es la del maestro y no se tocó.
- **Clase 8 (pág. 38):** las Figuras 8.1 y 8.2 van seguidas. La 8.1 no entra al pie, y para pasarla detrás del texto habría que invertir el orden de las dos figuras. Se dejó el hueco (28 %) para no desordenar la numeración.

En el tomo original en oficio había 23 hojas así.

## Archivos

- El tomo pasa a llamarse `TOMO_…_legal` (anual y bloques). Los `TOMO_…_oficio` se quitaron de la carpeta y quedan en el historial de git.
- El plan anual sigue en oficio horizontal, y la matriz, los planes y el solucionario en A4, porque el pedido fue sobre el tomo. Igual se regeneraron, porque citan las páginas del tomo.

# Decisiones de figuras · Informática 3.º BTC

Comparé las 20 propuestas con las originales R1 y con la clase, el pie, la tabla, la práctica y el solucionario donde
se usa cada una. Para identificarlas usé la huella SHA-256 de cada imagen incrustada, no el nombre interno.
- El tomo usa las figuras 1-20 en orden.
- El laboratorio usa 18 figuras en este orden: 1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20. Las
  prácticas 12 y 16 no llevan imagen.
- La «imagen 6» del laboratorio es la figura 7 del tomo, y no la figura 6.

Las propuestas son PNG de 1536 × 1024 px (3:2), no vectores. En el tomo conservé el ancho R1 de 14,2 cm (≈ 275 ppi
efectivos). En el laboratorio conservé el alto R1, con el ancho × 0,895 (≈ 9,6 y 7,2 cm), para que cada práctica siga
en su página. La P2 lleva un 15 % menos.

| Fig. | Uso | Decisión | Motivo |
|---|---|---|---|
| 1 | Clase 1 / P1 · módulos | Incorporar | Mismo modelo de cuatro módulos y base compartida; aclara que los nombres varían según el programa |
| 2 | Clase 2 / P2 · alta de la empresa | Incorporar | Datos idénticos a la ficha del caso (RUC 4.812.907-6, SIMPLE 701, IVA 211, e-Kuatia'i, ejercicio 2026). Rotulada «datos ficticios» |
| 3 | Clase 3 / P3 · permisos | Incorporar | Coincide celda por celda con la tabla de permisos de la clase (el operador no anula ni cierra) |
| 4 | Clase 4 / P4 · niveles del plan | Incorporar | El conector corregido une 1.1 y 1.2 al Activo. Códigos y cuentas iguales a los del plan |
| 5 | Clase 5 / P5 · del comprobante al asiento | Incorporar | Distingue el control aritmético del control de contenido, coherente con la Clase 9 |
| 6 | Clase 5 · documento electrónico | Incorporar | Distingue DE, DTE y KuDE (representación gráfica). «Entrega al receptor: documento y/o KuDE, según corresponda» coincide con la corrección H-3-02. Pie actualizado |
| 7 | Clase 6 / P6 · saldos iniciales | Incorporar | 8 + 22 + 25 + 9 = 64 M contra Capital 64 M |
| 8 | Clase 7 / P7 · diez asientos | Incorporar (barras → tabla) | La tabla trae los diez totales exactos y suma 143.899.700 por columna. Las barras R1 redondeaban a millones con un decimal. Es más útil para cotejar el Diario |
| 9 | Clase 8 / P8 · Mayor de Caja | Incorporar | Movimientos, sumas y saldo idénticos al CSV |
| 10 | Clase 9 / P9 · balance de comprobación | Incorporar | Dos igualdades con los importes correctos y la advertencia de lo que no detecta |
| 11 | Clase 10 · Estado de Resultados | Incorporar (cascada → operaciones) | Las operaciones 30.250.000 − 18.150.000 = 12.100.000 y 12.100.000 − 7.600.000 = 4.500.000 son exactas y se leen mejor que la cascada |
| 12 | Clase 10 / P10 · Balance General | Incorporar | Activo 75.441.300 = 8.941.300 + 66.500.000, por cuenta |
| 13 | Clase 11 / P11 · píxeles | Incorporar | 2.880.000 px; 8.640.000 bytes ≈ 8,24 MiB; 2400 ÷ 300 × 2,54 = 20,32 cm |
| 14 | Clase 13 / P13 · capas | Incorporar | Mismas cuatro capas que la tabla de la clase |
| 15 | Clase 14 / P14 · retoque | Incorporar (efecto ilustrativo) | Íconos de proceso, no una foto retocada. Respeta el límite ético de la clase («sin falsear el producto») |
| 16 | Clase 15 / P15 · filtros | Incorporar (efectos ilustrativos) | Esquemas, no resultados reales de un filtro: así lo rotula la figura. El pie R1 no coincidía con los paneles y lo corregí (H-3-04) |
| 17 | Clase 17 / P17 · salidas del pack | Corregir | Dimensiones, control y formato iguales a la tabla de la clase. Reemplacé el logotipo de una red social comercial por un ícono genérico de celular |
| 18 | Clase 18 / P18 · anatomía de una página | Corregir | La propuesta dice «esquema, no sitio publicado». Reemplacé el logotipo de una aplicación de mensajería por un globo genérico y el botón dice «Pedí por mensaje» |
| 19 | Clase 19 / P19 · mapa del sitio | Incorporar | Quita el dominio de la figura R1 y rotula «Esquema didáctico · no es un sitio publicado». Coincide con las cinco páginas de la clase |
| 20 | Clase 20 / P20 · ciclo de la promoción | Reconstruir en vector | Errores de render («San Ḃlas», «maestro ercapas») y logotipos comerciales. Rehecha con los datos concretos del caso que tenía la R1 (20 % en fiambres, del 5 al 12; publicación 1080 × 1080; medir contra el mes anterior), con retroalimentación al paso 1 y la nota «no representa una campaña real». SVG + PNG a 300 ppi |

## Esquemas tributarios y web

- **Figura 6**: no presenta el KuDE como la factura. Dice que la entrega depende del receptor y de la normativa.
- **Figuras 18 y 19**: maquetas rotuladas como esquema, sin URL publicada.
- **Figura 20**: aclara que no representa una campaña real.

## Legibilidad

Medí la altura de línea del texto (`medir_texto.py` y mediciones puntuales) al ancho final de 14,2 cm:
- Títulos, rótulos y cifras: 7-15 pt.
- Notas secundarias de algunas propuestas: alrededor de 4-6 pt, por ejemplo «Esquema de laboratorio…» (fig. 2),
  «Esquemas de efectos…» (fig. 16), «Importes en guaraníes» (fig. 12) y «Esquema didáctico…» (fig. 19).
- En el laboratorio, a 9,6 cm, esas notas bajan a unos 3-4 pt. Ninguna nota lleva información que no esté también en
  el texto o en el pie.

Queda como observación O-3-03, junto con la prueba de impresión física.

## Archivos

- `figuras/R2_Figura_NN.png`: las 20 figuras usadas.
- `figuras/R2_Figura_20.svg`: fuente vectorial.
- `build/figuras_3btc.py`: genera todo desde la carpeta de propuestas.

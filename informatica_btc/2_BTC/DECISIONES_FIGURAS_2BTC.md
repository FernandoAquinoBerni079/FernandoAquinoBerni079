# Decisiones de figuras · Informática 2.º BTC

Comparé las 13 propuestas (`Imagenes_2_BTC_13_Figuras/Propuestas`) con las originales R1 (`Antes_R1`) y con la clase,
el pie, la tabla y la actividad donde se usa cada una. Las identifiqué por contenido: la huella SHA-256 de cada
imagen R1 incrustada en los DOCX coincide con la de su `Antes_R1`. No me guié por el nombre interno.

Las propuestas son PNG de 1536 × 1024 px, no vectores. En el tomo se insertan a 15,5 cm de ancho, lo que da unos
250 ppi efectivos. En el laboratorio van a 12 cm, salvo las imágenes de la Práctica 10 (8 cm) y de la Práctica 14 (9,5 cm), reducidas para que cada práctica siga en una página.

| Fig. | Uso (clase / práctica) | Decisión | Motivo |
|---|---|---|---|
| 1 | Clase 1 · zonas de la ventana de la planilla | Incorporar | Mismas cinco zonas que la clase, más legible. Observación O-2-05: el ícono verde recuerda a una marca comercial |
| 2 | Clase 2 · dirección de celda y rango | Incorporar | «La columna siempre va primero», coherente con las actividades de rango C2:C17 (H-2-19) |
| 3 | Clase 4 · anatomía de una fórmula | Incorporar | `=SUMA(C2:C17)*12` sobre la columna C del honorario: 12.150.000 × 12 = 145.800.000. Aclara que supone doce meses iguales |
| 4 | Clase 5 · referencias relativas y absolutas | Corregir | La propuesta decía «absoliutas» en el subtítulo. Volví a escribir esa franja en Carlito Bold («Referencias relativas y absolutas») sin tocar el resto |
| 5 | Clase 8 · tipos de gráfico | Reconstruir en vector | La propuesta cambió a un esquema de tipos con cifras que no salen del caso. Rehecha con datos reales (millones de guaraníes): columnas RESIMPLE 4,05 / SIMPLE 4,50 / GENERAL 3,60; línea de 12 meses en 12,15; torta 33,3 / 37,0 / 29,6 % (nota: suma 99,9 % por redondeo); barras de egresos ordenadas (Sueldo 3,40; Alquiler 2,10; Servicios 0,65; IPS patronal 0,56; Publicidad 0,56; Insumos 0,38). SVG + PNG a 300 ppi |
| 6 | Clase 10 · circuito de la Unidad 3 | Incorporar | Del dato suelto al informe impreso, igual que la secuencia de la unidad |
| 7 | Clase 11 · vector y píxel | Incorporar | La figura R1 tenía texto superpuesto; la propuesta lo resuelve |
| 8 | Clase 13 · nodos y curvas Bézier | Reconstruir en vector | La geometría de la propuesta no mostraba manijas tangentes reales. Rehecha con una Bézier cúbica exacta (p0 (35,46), p1 (50,80), p2 (105,80), p3 (120,46)) y una variante punteada con la manija q2 movida, para mostrar el efecto de mover un nodo |
| 9 | Clase 14 / P14 · agrupar y soldar | Reconstruir en vector | La propuesta cambiaba el tamaño de los objetos entre «Antes» y «Después» (rectángulo alto de 142 a ~119 px), lo que confunde «soldar» con «escalar». Rehecha con tamaños idénticos y unión geométrica real. En R1, además, el pie cruzaba el borde punteado |
| 10 | Clase 16 · SI anidado (también en el laboratorio) | Incorporar | Usa la columna C (honorario), coherente con H-2-01/H-2-03 |
| 11 | Clase 17 · flujo de la tabla dinámica | Incorporar | De la base al resumen, con control de cierre contra el total de la base |
| 12 | Clase 19 · secciones del portal de la DNIT | Incorporar | Mapa esquemático de secciones; no reproduce la interfaz del sitio oficial |
| 13 | Clase 20 · factura electrónica | Incorporar | Distingue DE, DTE y KuDE, y la entrega según el receptor. Pie actualizado (H-2-04) |

## Legibilidad

Medí la altura de línea del texto (`medir_texto.py` y mediciones puntuales) al ancho final.
- En el tomo (15,5 cm), los títulos, rótulos y cifras de las rasters quedan en 7-20 pt.
- Algunas notas secundarias, como «Importes en guaraníes» de la figura 3, quedan en unos 6 pt.
- En el laboratorio (12 cm o menos), esas notas bajan a unos 4,5-5 pt.
- Las vectoriales usan Carlito de 8,5 pt como mínimo a 15,5 cm.

Sigue pendiente la prueba de impresión física (O-2-09).

## Archivos

- `figuras/R2_Figura_NN.png`: las 13 figuras usadas.
- `figuras/R2_Figura_05.svg`, `R2_Figura_08.svg`, `R2_Figura_09.svg`: fuentes vectoriales editables.
- `build/figuras_2btc.py`: genera todo lo anterior desde la carpeta de propuestas.

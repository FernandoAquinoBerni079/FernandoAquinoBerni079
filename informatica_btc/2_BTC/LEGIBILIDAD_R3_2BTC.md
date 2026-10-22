# Legibilidad de figuras · Informática 2.º BTC · R3

## Qué estaba mal en R2

En R2 medí el texto de las figuras con un método que contaba la altura de cada línea sin distinguir mayúsculas de
minúsculas. Por eso informé «notas de 4-6 pt» también en el tomo.

En R3 medí de nuevo, línea por línea, con una herramienta calibrada (`build_comun/medir_caja.py`):
- toma la altura de las mayúsculas y ascendentes de cada línea (0,70 del cuerpo en Carlito y fuentes sans afines);
- la calibré con texto de cuerpo conocido; el error es de ±8 %;
- en las figuras vectoriales (5, 8 y 9) uso el cuerpo de diseño del archivo SVG.

Resultado:
- **En el tomo (15,5 cm) no había ningún texto por debajo de 7,8 pt.**
- El problema real estaba en el **laboratorio**. Ahí las figuras iban a 12 cm, y la de la Práctica 10 a 8 cm y la de
  la Práctica 14 a 9,5 cm, para que cada práctica entrara en una página. Con esas reducciones el texto bajaba a
  4,5-6,7 pt.

## Criterio de R3

- **Piso de 7 pt** para cualquier texto de figura al tamaño impreso.
- Cada figura del laboratorio va al ancho más grande, en pasos de 0,5 cm hasta 15,5 cm, con el que su práctica entra
  en una página.
- **Ninguna figura baja del ancho que deja su texto más chico en 7 pt.**
- Si una práctica no entra en una página con ese ancho, la figura vuelve a 15,5 cm y la práctica pasa a ocupar dos
  páginas.
- No recorté contenido. Las Prácticas 10 y 14 recuperaron los tres renglones de anotaciones que les había quitado
  en R2.
- Prácticas en dos páginas: 1, 10 y 14. En la segunda página quedan el desafío y las anotaciones; completé los
  renglones de anotaciones hasta el pie para que esa página sirva de espacio de trabajo.
- El laboratorio pasa de 23 a 26 páginas. El ajuste lo hace `build/r3_2btc.py` y el resultado queda en
  `build/ajuste_laboratorio_r3_2btc.json`.

## Medición por figura (texto más chico de cada una)

| Fig, | Práctica | Texto más chico | Tomo 15,5 cm | Lab R2: ancho → cuerpo | Lab R3: ancho → cuerpo | Ancho mínimo para 7 pt |
|---|---|---|---|---|---|---|
| 1 | 1 | nota «Vista abreviada…» y pestañas | 8,2 pt | 12,0 cm → 6,3 pt | 15,5 cm → 8,2 pt | 13,3 cm |
| 2 | 2 | «Columna B + fila 3» / celda | 9,8 pt | 12,0 cm → 7,6 pt | 12,5 cm → 7,9 pt | 11,1 cm |
| 3 | 4 | «Importes en guaraníes» | 8,6 pt | 12,0 cm → 6,7 pt | 15,5 cm → 8,6 pt | 12,7 cm |
| 4 | 5 | «$ fija la columna G» | 9,3 pt | 12,0 cm → 7,2 pt | 13,0 cm → 7,8 pt | 11,7 cm |
| 5 | 8 | ejes y rótulos (diseño 8,5 pt) | 8,5 pt | 12,0 cm → 6,6 pt | 15,5 cm → 8,5 pt | 12,8 cm |
| 6 | 10 | «Proyección didáctica…» | 8,8 pt | 8,0 cm → 4,5 pt | 15,5 cm → 8,8 pt | 12,4 cm |
| 7 | 11 | «Ampliar una imagen…» | 11,4 pt | 12,0 cm → 8,8 pt | 13,0 cm → 9,6 pt | 9,6 cm |
| 8 | 13 | nota de la manija (diseño 9,5 pt) | 9,5 pt | 12,0 cm → 7,4 pt | 12,5 cm → 7,7 pt | 11,5 cm |
| 9 | 14 | rótulos de columna (diseño 9,5 pt) | 9,5 pt | 9,5 cm → 5,8 pt | 15,5 cm → 9,5 pt | 11,5 cm |
| 10 | 16 | pie amarillo | 9,7 pt | 12,0 cm → 7,5 pt | 12,0 cm → 7,5 pt | 11,2 cm |
| 11 | 17 | «A · Cliente» de la miniatura | 7,8 pt | 12,0 cm → 6,0 pt | 14,5 cm → 7,3 pt | 14,0 cm |
| 12 | 19 | «Mapa didáctico…» | 8,2 pt | 12,0 cm → 6,3 pt | 14,5 cm → 7,7 pt | 13,3 cm |
| 13 | 20 | «La entrega y los requisitos…» | 9,0 pt | 12,0 cm → 7,0 pt | 14,0 cm → 8,1 pt | 12,1 cm |

Las figuras R3 1 y 2 cambian por contenido, no por legibilidad; ver `CIERRE_R3_2BTC.md`.

## Pendiente

Esta medición no reemplaza la prueba de impresión física. El texto de 7-8 pt en papel oficio, impreso en la
impresora del laboratorio, debe comprobarse a distancia normal de lectura (ver `PRUEBAS_PRACTICAS_2BTC.md`).

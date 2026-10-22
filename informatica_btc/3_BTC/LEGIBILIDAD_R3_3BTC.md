# Legibilidad de figuras · Informática 3.º BTC · R3

## Qué estaba mal en R2

El método de medición de R2 era el mismo que en 2.º y tenía el mismo defecto (ver `../2_BTC/LEGIBILIDAD_R3_2BTC.md`).
Volví a medir con la herramienta calibrada `build_comun/medir_caja.py`:
- usa la altura de mayúsculas y ascendentes, que es 0,68-0,70 del cuerpo;
- el error es de ±8 %;
- en la Figura 20, que es vectorial, uso el cuerpo de diseño.

En 3.º, a diferencia de 2.º, **el tomo sí tenía textos por debajo de 7 pt**. Las figuras iban a 14,2 cm, y en las
figuras 1, 2, 12, 18 y 19 el texto más chico medía entre 6,0 y 6,7 pt.

En el laboratorio, las figuras iban a 9,6 cm, y la de la Práctica 2 a 7,2 cm. Con esos anchos el texto bajaba a
3-7 pt.

## Qué se hizo en R3

**Tomo**
- Las 20 figuras pasan de 14,2 a 15,5 cm, el ancho útil de la caja.
- El tomo sigue teniendo 77 páginas y ninguna clase cambió de página.

**Figura 2**
- La nota «Esquema de laboratorio: no corresponde a un registro tributario real», de dos líneas y 6 pt, sale de la
  imagen.
- Pasa como texto al pie de figura, en el tomo y en el laboratorio.

**Figura 19**
- La nota «Esquema didáctico · no es un sitio publicado.» se reescribió más grande: de 6,4 a 8,8 pt.
- En la misma pasada, «WhatsApp» pasó a «Mensajería» (ver `CIERRE_R3_3BTC.md`).

**Laboratorio**
- Se aplicó el mismo criterio que en 2.º:
  - piso de 7 pt;
  - cada figura va al mayor ancho con el que su práctica entra en una página;
  - ninguna figura baja del ancho mínimo;
  - si la práctica no entra en una página, la figura vuelve a 15,5 cm y la práctica ocupa dos páginas.
- Once prácticas quedan en dos páginas: 1, 2, 3, 6, 7, 9, 10, 17, 18, 19 y 20.
- En la segunda página de cada una van el desafío y el registro del estudiante. Completé los renglones del registro
  hasta el pie, con 8 mm de paso.
- El cuaderno pasa de **22 a 33 páginas**. Es una decisión de costo para Fernando: D-3-04 en `CIERRE_R3_3BTC.md`.
- Los anchos finales están en `build/ajuste_laboratorio_r3_3btc.json`.

## Medición por figura (texto más chico de cada una)

| Fig. | Práctica | Texto más chico | Tomo R2 (14,2 cm) | Tomo R3 (15,5 cm) | Lab R2: ancho → cuerpo | Lab R3: ancho → cuerpo | Ancho mínimo para 7 pt (cm) |
|---|---|---|---|---|---|---|---|
| 1 | 1 | nota «Los nombres y las funciones…» | 6,7 pt | 7,3 pt | 9,6 cm → 4,5 pt | 15,5 cm → 7,3 pt | 14,9 |
| 2 | 2 | rótulos de campo (R2: nota de 2 líneas) | 6,0 pt | 10,9 pt | 7,2 cm → 3,0 pt | 15,5 cm → 10,9 pt | 10,0 |
| 3 | 3 | rótulos y pies internos | 8,1 pt | 8,8 pt | 9,6 cm → 5,5 pt | 15,5 cm → 8,8 pt | 12,3 |
| 4 | 4 | rótulos y pies internos | 9,2 pt | 10,0 pt | 9,6 cm → 6,2 pt | 12,5 cm → 8,1 pt | 10,8 |
| 5 | 5 | rótulos y pies internos | 10,4 pt | 11,4 pt | 9,6 cm → 7,1 pt | 12,5 cm → 9,2 pt | 9,5 |
| 6 | — | rótulos de las etapas | 8,6 pt | 9,4 pt | no va en el cuaderno | no va en el cuaderno | — |
| 7 | 6 | pie «Importes en guaraníes…» | 7,5 pt | 8,2 pt | 9,6 cm → 5,1 pt | 15,5 cm → 8,2 pt | 13,2 |
| 8 | 7 | pie de la tabla | 7,5 pt | 8,2 pt | 9,6 cm → 5,1 pt | 15,5 cm → 8,2 pt | 13,2 |
| 9 | 8 | rótulos y pies internos | 9,6 pt | 10,5 pt | 9,6 cm → 6,5 pt | 12,5 cm → 8,5 pt | 10,3 |
| 10 | 9 | rótulos y pies internos | 10,0 pt | 10,9 pt | 9,6 cm → 6,8 pt | 15,5 cm → 10,9 pt | 10,0 |
| 11 | — | rótulos y pies internos | 10,8 pt | 11,8 pt | no va en el cuaderno | no va en el cuaderno | — |
| 12 | 10 | «Cuenta» e «Importes en guaraníes.» | 6,4 pt | **7,0 pt** | 9,6 cm → 4,3 pt | 15,5 cm → **7,0 pt** | 15,5 |
| 13 | 11 | rótulos y pies internos | 8,9 pt | 9,7 pt | 9,6 cm → 6,0 pt | 11,5 cm → 7,2 pt | 11,2 |
| 14 | 13 | rótulos y pies internos | 10,0 pt | 10,9 pt | 9,6 cm → 6,8 pt | 12,5 cm → 8,8 pt | 10,0 |
| 15 | 14 | rótulos y pies internos | 11,2 pt | 12,2 pt | 9,6 cm → 7,6 pt | 12,0 cm → 9,4 pt | 8,9 |
| 16 | 15 | pie de la figura | 7,5 pt | 8,2 pt | 9,6 cm → 5,1 pt | 14,0 cm → 7,4 pt | 13,2 |
| 17 | 17 | rótulos y pies internos | 9,2 pt | 10,0 pt | 9,6 cm → 6,2 pt | 15,5 cm → 10,0 pt | 10,8 |
| 18 | 18 | descripciones de los cinco bloques | 6,4 pt | **7,0 pt** | 9,6 cm → 4,3 pt | 15,5 cm → **7,0 pt** | 15,5 |
| 19 | 19 | nota «Esquema didáctico…» | 6,4 pt | 8,8 pt | 9,6 cm → 4,3 pt | 15,5 cm → 8,8 pt | 12,3 |
| 20 | 20 | textos de las tarjetas (diseño 8,5 pt) | 7,8 pt | 8,5 pt | 9,6 cm → 5,3 pt | 15,5 cm → 8,5 pt | 12,8 |

## Límite de lo que resolví

Las figuras 12 y 18 quedan **justo en el piso de 7 pt**. Ya están al ancho máximo de la caja, así que ampliarlas no
es posible. Con el margen de error de la medición, pueden imprimirse algo por debajo de 7 pt.

Cómo cerrarlo de verdad:
- **Figura 12:** volver a dibujar la tabla con letra más grande.
- **Figura 18:** acortar o sacar las descripciones bajo cada bloque. El texto de la Clase 18 ya las explica.

Lo dejo como decisión D-3-01 de Fernando. Requiere redibujar desde la fuente, que no tengo para estas dos imágenes
raster.

Esta medición no reemplaza la prueba de impresión física: ver `PRUEBAS_PRACTICAS_3BTC.md`.

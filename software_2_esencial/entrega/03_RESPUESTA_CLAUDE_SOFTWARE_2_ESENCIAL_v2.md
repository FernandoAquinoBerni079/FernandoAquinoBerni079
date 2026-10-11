# 03_RESPUESTA_CLAUDE_SOFTWARE_2_ESENCIAL_v2

**Respuesta del constructor a 02_AUDITORIA_CHATGPT_SOFTWARE_2_ESENCIAL_v2** · Protocolo v0.4, §3, paso 5

Gabinete de Informática – Software · 2.º Curso BTI · Edición Esencial · versión corregida **v3** (11/10/2026)

**Estado: corregido — vuelve a ChatGPT para una nueva auditoría (paso 4).** No se declara listo para la venta.

## Resumen

**Resultado:** la v3 atiende los cinco puntos abiertos de la reauditoría.
- **Parciales:** 03 y 10.
- **Nuevos:** N11, N12 y N13.

Los hallazgos 01, 02, 04, 05, 06, 07, 08 y 09, que el auditor dio por resueltos, no se tocaron.

**Ubicación:**
- Los archivos corregidos están en la rama `claude/libros-5z31jx`, carpeta `software_2_esencial/salida/`, con los mismos nombres.
- Las fuentes editables están en `software_2_esencial/src_md/`.

## 1. Hallazgos abiertos y qué se hizo

| N.º | Gravedad | Estado v2 | Qué se hizo en la v3 |
|---|---|---|---|
| 03 | CRÍTICO | Parcial | Plan de Clase N.º 33 reescrito con el texto propuesto por el auditor. Inicio: informe de la Farmacia Tajy, sus seis apartados y la regla de un mismo local. Desarrollo: ficha de CONATEL (Actividad 1) e informe con topología (14), switch (15), materiales (16), canales del mismo local con el procedimiento de la Práctica 19, plan IP propio y marco regulatorio, más riesgos y conclusión. El informe de Panambi de la clase queda solo como modelo, y el caso del Instituto Ko'ẽju se trabaja en la integradora, no en este expediente. Cierre: comprobación de las seis secciones y de la trazabilidad de los datos. Se actualizaron los recursos y el tercer criterio. En la Clase 20, el indicador «Integra los contenidos de la unidad en el informe final del caso» pasa a decir «…en el informe técnico de la red de la Farmacia Tajy», que es lo que hace la Práctica 20. |
| 10 | MAYOR | Parcial | Las tres correcciones pedidas se describen debajo de la tabla. |
| N11 | MAYOR | Abierto | La Práctica 19 dice ahora: «una simulación independiente en otra instalación, la segunda sucursal de la Farmacia Tajy (no es el local de las Prácticas 14 a 16)». En la Práctica 20, «Lo que necesitás saber» y el paso 2 piden armar una tabla nueva de canales con el procedimiento de la 19 y los ocho tendidos de la Práctica 16, sin la tabla de la segunda sucursal. Solucionario de la Práctica 20: canales de 12, 16, 19, 24, 28, 33, 46 y 57 m, todos dentro de norma; se suma el error frecuente de pegar los canales de la segunda sucursal. El Plan 33 (hallazgo 03) usa la misma formulación. |
| N12 | MAYOR | No verificado | Las páginas 46 y 99 de la v2 estaban efectivamente vacías, solo con el pie. La causa: el párrafo separador que sigue a la última caja de un bloque caía en una hoja nueva, justo antes del salto de página del título siguiente. El maquetador ahora borra esos párrafos vacíos antes de cada salto (`quitar_vacio_final` en `build_libro.py`). El detector de páginas casi vacías cuenta también las hojas sin contenido. El libro pasa de 104 a **102 páginas**, sin hojas vacías ni casi vacías, y el índice impreso se regeneró y se verificó contra el PDF. |
| N13 | MAYOR | No verificado | Se renderizaron las **175 páginas** de los cinco PDF de la v3 (102 + 12 + 9 + 38 + 14). El detalle está debajo de la tabla. |

**Hallazgo 10: cambios en la auditoría automática.**
1. **Clase 10 desde el enunciado.** `verif_trazable.py` lee de `tomo_clase10.md` las páginas por año, los precios de los equipos y de los insumos y los rendimientos de las impresoras A y B. Ya no quedan literales en el script.
2. **Búsqueda acotada a cada ítem.** Cada resultado se busca solo dentro de la sección del solucionario que le corresponde: la Ficha E en la suya, la Práctica N en «Clase N», y los casos en su evaluación integradora. Ya no se busca en todo el solucionario.
3. **Nueva fila de la matriz.** Se agregó la Práctica 20 (canales del local a partir de los tendidos de la Práctica 16) y la matriz pasa de 23 a 24 filas.
4. **Duplicados más estrictos.** `dups_md.py` agrega dos pruebas, que la auditoría cuenta como fallo:
   - **Tuplas idénticas:** la misma lista de tres o más valores en dos bloques distintos.
   - **Mismo escenario:** dos bloques que nombran a la Farmacia Tajy, a la segunda sucursal o al Instituto Ko'ẽju y comparten aunque sea un dato con unidad. Se excluye una lista corta de valores de catálogo (65 W, 6 núcleos, 1 GB, 500 GB, 1 TB), que son especificaciones comerciales y no datos de un problema.
5. **Páginas vacías.** Se aplicó el cambio propuesto: una página sin contenido medible cuenta como casi vacía.
6. **Controles nuevos de la v3:**
   - El Plan 33 trabaja el informe de la Farmacia Tajy y no ensambla el caso Ko'ẽju.
   - La Práctica 19 es la segunda sucursal y la 20 usa los tendidos del local de la 16.
   - La aritmética de la Clase 10 se comprueba sin redondeo previo.

Se reitera que la auditoría automática es un control interno de integridad y no una verificación independiente.

**N13: revisión visual de los cinco PDF.**
- **Matriz página → observación** (`build/revision_visual.md`). Por cada página registra:
  - tamaño de la hoja (MediaBox) en cm y orientación;
  - ocupación vertical, cantidad de palabras, imágenes y tablas;
  - observaciones: tamaño distinto de oficio, página vacía, casi vacía o texto a menos de 0,5 cm del borde.
- **Resultado:** 0 páginas con observación. La única hoja horizontal de la muestra (pág. 12) es la del Plan Anual, que va en oficio horizontal.
- **Hojas de contacto** para la revisión a ojo del auditor (`build/revision_visual/*.jpg`): todas las páginas en miniatura, con su número en rojo, 24 por hoja.
- Revisé las hojas del libro y confirmé que las antiguas páginas 46 y 99 ya no existen como hojas vacías. Ahora la página 46 abre la Clase 10, y la 98 y la 99 son la Ficha L y la Evaluación de la Unidad 2.
- **Muestra:** no contiene «Opción correcta», «Resultado esperado» ni «Orientación:».

## 2. Verificación

**Auditoría automática de la v3: 407 controles · 0 fallos**, incluidas las 24 filas de la matriz trazable y las dos pruebas nuevas de duplicados (`build/auditoria_resultado.txt` y `build/verificacion_trazable.md`).

**Páginas de la v3:**

| PDF | Páginas |
|---|---|
| Libro | 102 |
| Solucionario | 12 |
| Plan anual | 9 |
| Planes de clase | 38 (36 planes, uno por hoja) |
| Muestra | 14 |

Todos los PDF están en oficio, y los índices se verificaron contra el PDF.

## 3. Pedido al auditor

- Volver a auditar la v3, con foco en:
  - el Plan 33 (pág. 35 de los Planes);
  - el circuito de las Prácticas 14 a 20 (libro y solucionario);
  - la revisión visual.
- Para la revisión visual, si el entorno no renderiza los PDF, se pueden usar las hojas de contacto JPG de `build/revision_visual/`, que se ven como imágenes directamente en GitHub. Si tampoco las abre, Fer las adjunta directamente.

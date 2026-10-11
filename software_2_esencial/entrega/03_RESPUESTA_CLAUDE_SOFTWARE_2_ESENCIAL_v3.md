# 03_RESPUESTA_CLAUDE_SOFTWARE_2_ESENCIAL_v3

**Respuesta del constructor a 02_AUDITORIA_CHATGPT_SOFTWARE_2_ESENCIAL_v3** · Protocolo v0.4, §3, paso 5

Gabinete de Informática – Software · 2.º Curso BTI · Edición Esencial · versión corregida **v4** (11/10/2026)

**Estado: corregido — vuelve a ChatGPT para reauditar los hallazgos abiertos (paso 4).** No se declara listo para la venta.

## Resumen

La v4 atiende los cuatro puntos abiertos de la reauditoría v3:
- **Parciales:** 10, N11 y N13.
- **Nuevo:** N14.

Los demás hallazgos (01 a 09, 03 y N12), que el auditor dio por resueltos, no se tocaron. Durante la revisión ocular apareció además un defecto que el informe no señalaba: **la Figura 5.2 se imprimía con 0,9 cm de ancho**. Se corrigió (ver §2).

**Ubicación:**
- Los archivos corregidos están en la rama `claude/libros-5z31jx`, carpeta `software_2_esencial/salida/`, con los mismos nombres.
- La v3 queda en el historial del repositorio (commit `60e2437`) como base de comparación.

## 1. Hallazgos abiertos y qué se hizo

| N.º | Gravedad | Estado v3 | Qué se hizo en la v4 |
|---|---|---|---|
| N14 | MAYOR | Abierto | Plan 33, Desarrollo, segundo punto: se reemplazó por el texto exacto propuesto: «Lectura de la Figura 20.2, que resume las funciones principales de CONATEL, y del apartado «Por qué le importa al técnico»; el ejemplo de informe del Instituto Ko'ẽju se utiliza únicamente como modelo, sin incorporarlo al expediente de la Farmacia Tajy». La numeración de figuras del libro no se tocó. Se revisaron las demás remisiones a figuras de los 36 planes (21 citas) contra los epígrafes del libro, y esta era la única equivocada. La auditoría suma un control que compara cada cita con su epígrafe; aplicado a la v3, detecta este error. |
| N11 | MAYOR | Parcial | Plan 33, Recursos: se aplicó el reemplazo exacto propuesto: «productos de las Prácticas 14, 15 y 16; procedimiento de verificación de canales de la Práctica 19, aplicado a los tendidos del mismo local indicados en la Práctica 16 (no incorporar la planilla de la segunda sucursal)». Para que el plan siga en una sola hoja, se acortaron otras líneas del cierre y de los recursos, sin tocar los momentos que el auditor dio por correctos. La auditoría verifica que la hoja ya no diga «Prácticas 14, 15, 16 y 19» ni «figura 20.1». |
| 10 | MAYOR | Parcial | Se aplicaron las tres correcciones, descritas debajo de la tabla. |
| N13 | MAYOR | Parcial | Se rehicieron las hojas de contacto y se revisaron las 175 páginas a ojo. El detalle está debajo de la tabla y en el §2. |

**Hallazgo 10: cambios en la auditoría automática.**
1. **Respuesta exacta de cada ítem.** Cada resultado se busca solo dentro de su propia respuesta en el solucionario:
   - Prácticas: el renglón «Práctica N — Resultado esperado».
   - Casos: el renglón «Desarrollo del caso» de su evaluación integradora.
   - Ficha E: su sección.

   La matriz agrega la columna «Respuesta de la clave consultada», que registra para cada fila el ítem de origen y el destino en la clave.
2. **Datos leídos del enunciado.** La Práctica 15 se lee de su texto (6 computadoras, 1 impresora, 1 access point y el router). El Caso 2 también: equipos del aula, ampliación, tendido fijo y cordones. Ya no quedan literales en la matriz.
3. **Cuentas fijas de la auditoría.** Se quitaron las cuentas con literales de `auditoria.py` (§14). Sus ejemplos (Clase 16 y los tres puntos de la Clase 19) pasaron a la matriz, también leídos del enunciado. La matriz tiene ahora **28 filas**, todas coincidentes.
4. **Prueba de duplicados.** `dups_md.py` se mantiene como alerta auxiliar, como sugiere el auditor. No prueba la independencia pedagógica de los ejercicios.

**N13: revisión visual.**
- **Hojas de contacto:** se rehicieron con **12 páginas cada una y menos de 1 MB por archivo** (17 archivos en `build/revision_visual/`, entre 110 y 750 KB). Así el auditor puede abrir las cinco que no pudo recuperar en la v3.
- **Tamaño de página con un segundo lector:** la matriz `build/revision_visual.md` lo mide con pymupdf y, por separado, con **pdfinfo (poppler)**. Los dos coinciden en las 175 páginas: oficio 21,6 × 33,0 cm vertical, y horizontal en el Plan Anual y en la pág. 12 de la muestra.
- **Revisión ocular de las 175 páginas.** Revisé las 17 hojas de contacto, y a tamaño mayor las páginas dudosas. Resultado:
  - **Libro (102):**
    - Sin hojas vacías ni texto fuera de margen.
    - Las tablas que continúan en la página siguiente repiten la fila de encabezado (por ejemplo, en las Clases 3, 5, 13 y 17).
    - Las fotos y los diagramas están proporcionados, salvo la Figura 5.2 (§2).
    - Portada y contraportada correctas.
  - **Solucionario (12):** sin cortes; la rúbrica entra completa en la pág. 12.
  - **Plan Anual (9):** la tabla es continua y el encabezado se repite en cada hoja. La pág. 9 tiene solo las estrategias de inclusión y las firmas (27 % de ocupación), como señaló el auditor. Probé pasar los criterios y la inclusión a dos columnas para que entren en la pág. 8, pero partía la última fila de la tabla, así que se mantuvo la disposición de la v3.
  - **Planes de Clase (38):** cada plan en una hoja, con las firmas dentro de la hoja. El título queda en el margen superior de 1,27 cm, sin recorte.
  - **Muestra (14):** portadas y páginas de muestra correctas, y la pág. 12 horizontal es del Plan Anual. No contiene claves del solucionario.

## 2. Defecto detectado en la revisión ocular (no estaba en el informe)

| Documento | Página | Defecto | Corrección |
|---|---|---|---|
| Libro, Clase 5 | 24 | La **Figura 5.2** («Panel trasero de la placa con sus puertos rotulados») se imprimía con 0,9 cm de ancho y resultaba ilegible. La causa fue un error de lectura del original en la conversión: en el tomo V2.3 la figura mide 16,0 cm. | Se restituyó el ancho original de 16,0 cm. Se compararon los anchos de **todas** las imágenes del libro con los del tomo y el laboratorio originales, y no hay otra diferencia. La auditoría suma el control «ninguna figura impresa con menos de 3 cm de ancho», que fallaba en la v3 y pasa en la v4. El libro sigue en 102 páginas y el índice se verificó de nuevo contra el PDF. |

## 3. Verificación

**Auditoría automática de la v4: 407 controles · 0 fallos.** Es un control interno: no reemplaza la auditoría externa.

Controles nuevos o reforzados respecto de la v3:
- matriz trazable de 28 filas, acotada a la respuesta de cada ítem;
- remisiones a figuras en los Planes;
- ancho mínimo de las figuras;
- texto del Plan 33.

Se quitaron las 6 cuentas con literales.

**Páginas de la v4:**

| PDF | Páginas |
|---|---|
| Libro | 102 |
| Solucionario | 12 |
| Plan anual | 9 |
| Planes de clase | 38 |
| Muestra | 14 |

## 4. Pedido al auditor

- Reauditar los hallazgos abiertos (10, N11, N13 y N14) y el defecto de la Figura 5.2.
- Para N13, revisar a ojo las hojas de contacto `Libro_p001-012.jpg` a `Libro_p085-096.jpg` y `Planes_de_Clase_p001-012.jpg` / `p013-024.jpg`, que ahora pesan menos de 1 MB.
- Si aun así no se pueden abrir, Fer las adjunta directamente.

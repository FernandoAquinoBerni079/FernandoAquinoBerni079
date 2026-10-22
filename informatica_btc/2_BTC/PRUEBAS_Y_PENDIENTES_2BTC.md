# Pruebas realizadas y verificaciones pendientes · Informática 2.º BTC (R2)

## Pruebas realizadas

| Prueba | Método | Resultado |
|---|---|---|
| Integridad de los insumos R1 | SHA-256 de los 6 archivos del paquete contra `Verificacion_entrega.json`. Para .md y .csv, recalculado con fin de línea CRLF: Git había guardado LF | Coinciden |
| Lectura completa | Volcado a texto de los 5 DOCX (párrafos con estilo, tablas, imágenes, saltos) y lectura íntegra | Hecha |
| Cotejo con el programa MEC BTC 2.º | Unidades, capacidades y subrayadas contra plan anual, fichas y planes | Cobertura completa. Capacidades agregadas al plan anual (H-2-07) |
| Carga horaria | Suma de tiempos del plan anual y de los 36 planes | 72 HC en 36 encuentros |
| Aritmética del caso | Recalculo de cada cifra del tomo, el laboratorio y el solucionario | Sin diferencias tras H-2-01/02 (ver la matriz) |
| Fórmulas y referencias | Cada fórmula del tomo y del laboratorio contra la estructura A = Cliente, B = Régimen, C = Honorario, filas 2-17 | Corregidas `B4`, `B17` y la figura de la P16 |
| Claves de opción múltiple | `claves.py`: letra y texto de cada clave contra la opción impresa, por sección | 116/116. Distribución 29/29/29/29 |
| Sincronía entre documentos | Cambios replicados en tomo, laboratorio, plan anual, solucionario y planes | Ver la bitácora |
| Construcción R2 | `build/r2_2btc.py`: cada reemplazo exige la cantidad exacta de apariciones; si no la encuentra, se detiene | 62 cambios registrados |
| Índices estáticos | Recalculados dos veces sobre el PDF renderizado | Tomo, laboratorio, solucionario y planes verificados |
| Formato | Oficio de 216 × 330 mm (plan anual en apaisado), márgenes, tipografía y saltos | Igual que R1. Planes a 9,5 pt (H-2-22) |
| Revisión visual | Render con LibreOffice y 29 hojas de contacto que cubren las 162 páginas, revisadas una por una (tomo 75, lab 23, plan 4, sol 23, planes 37) | Sin páginas en blanco, rótulos huérfanos ni desbordes. Ver O-2-06 |
| Figuras | Cotejo de contenido con su clase, legibilidad medida al ancho final | Ver `DECISIONES_FIGURAS_2BTC.md` |
| Legales y tributarias | Búsqueda en fuentes oficiales y doctrina verificada | Ver `../FUENTES_CONSULTADAS.md` |

## Verificaciones pendientes (no realizadas)

1. **Prueba en software real** de las 20 prácticas: planilla electrónica, editor vectorial y portal DNIT. Hay que
   probar las rutas de menú, el autofiltro, la tabla dinámica, la exportación a PDF y la conversión a curvas.
2. **Prueba de impresión física** en oficio, con legibilidad de figuras y renglones. El plan anual va en apaisado.
3. **Apertura en Microsoft Word en Windows**. Solo se renderizó con LibreOffice. Hay que confirmar la paginación y
   que los índices estáticos coincidan.
4. **Texto oficial de la RG DNIT 54/2026** y nueva consulta del portal `dnit.gov.py`, que no respondió desde este
   entorno.
5. **Ratificación institucional** del programa vigente (edición de 2014), de la hora cátedra de 40 min y de la
   distribución en 36 encuentros.
6. **Aprobación de Fernando** sobre las figuras incorporadas y las reconstruidas (5, 8 y 9) y sobre la
   redistribución de los encuentros 33-35.
7. Observaciones menores O-2-01 a O-2-05 de la matriz, para la R3.

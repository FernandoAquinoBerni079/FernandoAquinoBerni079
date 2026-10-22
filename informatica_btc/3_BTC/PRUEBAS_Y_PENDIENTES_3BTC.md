# Pruebas realizadas y verificaciones pendientes · Informática 3.º BTC (R2)

## Pruebas realizadas

| Prueba | Método | Resultado |
|---|---|---|
| Integridad de los insumos R1 | SHA-256 de los 6 archivos del paquete contra `Verificacion_entrega.json` | Coinciden |
| Lectura completa | Volcado y lectura íntegra de los 5 DOCX: tomo de 1948 líneas, laboratorio 708, plan 55, solucionario 657, planes 1275 | Hecha |
| CSV de laboratorio | Script: balance por asiento, totales, saldos, existencia y nombre de cada cuenta en el plan, `controles_docente.csv` asiento por asiento, y las dos copias con errores | Todo cierra (ver la matriz). Los CSV se copian sin cambios a `recursos/` |
| Aritmética del caso | Recalculo de Caja, Banco, IVA, IPS, resultado, balance, proyección, píxeles, A3, etiqueta, sangrado y quincena | Sin diferencias |
| Cotejo con el programa MEC BTC 3.º | Unidades, capacidades, subrayadas y contenidos | Cobertura completa. Se agregan los «otros registros» (H-3-08) y las capacidades al plan anual (H-3-05) |
| Carga horaria | Plan anual y 36 planes | 108 HC en 36 encuentros. Cada plan suma 120 min |
| Claves | `claves3.py`: 119 claves de opción múltiple (letra y texto) y la cantidad de ítems por sección | 119/119. Distribución 28/33/28/30 |
| Puntajes de las evaluaciones | Suma de los puntajes sugeridos contra los ítems impresos | Coinciden en las 8 evaluaciones |
| Construcción R2 | `build/r2_3btc.py`: reemplazos con cantidad exacta | 39 cambios registrados |
| Índices estáticos | Dos pasadas sobre el PDF (tomo y planes) | Verificados |
| Formato | Oficio, márgenes y tipografía de R1. Plan anual en apaisado. Rótulos huérfanos detectados en el render y corregidos | Tomo 77, lab 22, plan 7, sol 22, planes 37 páginas |
| Revisión visual | 30 hojas de contacto que cubren las 165 páginas, revisadas una por una | Ver O-3-02 |
| Figuras | Huella de cada imagen incrustada, cotejo con su clase y práctica, legibilidad medida | Ver `DECISIONES_FIGURAS_3BTC.md` |
| Legales | Búsqueda y doctrina verificada | Ver `../FUENTES_CONSULTADAS.md`. Se detectó el art. 76 desactualizado (H-3-01) |

## Verificaciones pendientes (no realizadas)

1. **Prueba en software real**, con el sistema contable, el editor raster y el entorno web de la institución:
   - importación de los CSV en el sistema contable;
   - perfiles y bitácora;
   - cierre anual simulado;
   - animación GIF;
   - exportación WEBP;
   - publicación de prueba.
2. **Prueba de impresión física** en oficio. Hay que revisar sobre todo las notas chicas de las figuras raster
   (O-3-03) y los renglones.
3. **Apertura en Microsoft Word en Windows** para confirmar la paginación y los índices.
4. **Texto consolidado oficial** del art. 76 de la Ley 1034/83 según la Ley 4924/2013 (O-3-04) y de la Ley 7593/2025
   (O-3-05). BACN y DNIT no respondieron desde este entorno.
5. **Ratificación institucional** del programa, de la hora cátedra de 40 min y de los 36 encuentros. Validar los
   encuentros de cierre con un grupo real (O-3-01).
6. **Aprobación de Fernando** sobre las 20 figuras: 17 incorporadas, 2 corregidas y 1 reconstruida.

# Comparación independiente de los cinco mapas del Bloque I

Estado anterior: `755d7adbd0a4b57f0b91a95c85cd8b9ac978c705`. Estado auditado: `ea3cf5f6349f4de2e1f3c495b92707b641e6d37e`.

Se compararon los cinco PNG descargados de ambos commits, las dimensiones, la caja de píxeles distintos y el código de la escala. El estado anterior solo se usa como comparación; el dictamen pedagógico corresponde íntegramente a ea3cf5f.

La modificación de `scripts/figuras/comun.py` suprime el rótulo intermedio cuando la barra ocupa una fracción igual o inferior a 0,22 del ancho del mapa. Conserva el cálculo `km / (111,32 × cos(latitud de referencia))`, la longitud de la barra, la tipografía y sus extremos. Es una escala aproximada sobre el esquema, no una certificación geodésica.

| Archivo | Dimensiones px | Caja de cambios (x 0,y 0,x 1,y 1) | Resto de píxeles sin cambios | SHA256 anterior | SHA256 actual |
| --- | --- | --- | --- | --- | --- |
| eval_u1_mapa.png | [1062, 1190] | [188, 954, 251, 988] | Sí | 0b2ad8aff304ea4a57192b3ddf3aa81621c94b2c83ece6ee8bcbd885e36ebcdf | 7138c88b9f8499d6f176dbc17ef061cbf37691630bc6cba26af40a323cf7d556 |
| eval_u1_mapa_clave.png | [1062, 1190] | [188, 954, 251, 988] | Sí | 720a91b9ca737ecb8d3eac87e617a116ee7064d73927e2a6ba3781f6c07fbb2e | ab4bb6340ddff1bc2b6a9562e30cf29ab4f520f7e25e8cace9c484084596672c |
| fig_1_3_mapa_orientacion.png | [1417, 1535] | [239, 1274, 301, 1307] | Sí | e3f63737ca37b8bed51832ac1e5524226d55793362c86b1345be8c59376ecaa6 | 5d4e36935cb9f5eedb1abb069afa903cc5585dd73b5648a59de6724052c5a7cf |
| fig_2_2_regiones.png | [1299, 1455] | [222, 1190, 284, 1224] | Sí | 7a3875a2385ef3f225922fb99da4bca9646f56a7f814030a6cf5f0b423f4ad1a | 6df6cbe22410c65a26500cd18ee0dc57d2ba17cea0be09610c2149684c395de7 |
| fig_3_1_area_guarani.png | [1358, 1476] | [242, 1180, 305, 1213] | Sí | 31e974f0a93fe34c5b295bcc4096a41142ba915d58242a944ac5fc40922a6a87 | 5b7759f3eb883b5e85688dc9ef058d4f9e585ca9fd2f904da9e0d1098c4c366e |

Las diferencias quedan confinadas a los antiguos rótulos «100» o «200» de la escala. Fuera de cada caja indicada, los píxeles son iguales; no se desplazaron cauces, fronteras, ciudades, áreas ni leyendas. En las cinco comparaciones visuales se separan con claridad 0 y 200 km, o 0 y 400 km. La leyenda distingue río continuo y límite discontinuo. Los mapas mantienen proporciones y no muestran nuevos recortes.

En el tomo, Figura 1.3 p 7, Figura 2.2 p 12, Figura 3.2 p 16 y mapa U1 p 25; clave U1 en solucionario p 6. El nombre de archivo `fig_3_1_area_guarani.png` no es el número impreso: se cotejó con Figura 3.2. La orientación de Encarnación respecto de Asunción es sudeste; distancia recta aproximada compatible con 250–330 km de la clave. La evaluación U1 no exige medir esa distancia.

Se inspeccionaron los rótulos al tamaño digital de página y las simulaciones digitales de grises. En grises permanecen distinguibles ríos, límites, ciudades y zonas; los mapas mudos permiten añadir nombres y trazados con lápiz. Los rótulos pequeños y pies requieren una prueba física final en la impresora escolar; esta auditoría no hizo impresión ni fotocopia.

**Resultado de los cinco mapas regenerados: conforme para la corrección de escala examinada.** Ese resultado no valida todos los mapas del bloque: la Ficha B-1 (tomo pp 36–37) excluye Beringia y Monte Verde (BI-01) y debe corregirse antes de uso.

**Bloque II:** rutas de viajes p 5 declaradas aproximadas; Tordesillas p 9 distingue oeste Castilla/este Portugal y 370 leguas desde Cabo Verde (líneaaprox 46°O); expediciones del Río de la Plata p 14 y Ficha C p 20 incluyen los lugares que pide la consigna. Países actuales se usan como referencia y se declara su carácter aproximado. Clave gráfica U3 p 8 ubica Buenos Aires 1536, Asunción 1537 y Sancti Spiritus 1527. Los itinerarios esquemáticos no deben evaluarse como trazados históricos exactos; el solucionario lo aclara.

Evidencias: cinco archivos `COMPARACION_*.png`, cinco simulaciones `GRISES_*.png` y páginas pertinentes en `EVIDENCIAS_VISUALES/`. Las imágenes comparativas recortan solo el sector de la escala y se rotulan ANTES/DESPUÉS; los mapas originales no fueron editados.

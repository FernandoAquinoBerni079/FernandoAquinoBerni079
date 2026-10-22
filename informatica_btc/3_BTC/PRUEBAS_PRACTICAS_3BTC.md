# Pruebas prácticas en software · Informática 3.º BTC (R3)

Ninguna de estas pruebas se hizo en esta revisión. Se hacen en el laboratorio de la institución, siguiendo el
Cuaderno de Laboratorio R3 tal como está impreso, antes de liberar el material.

## Datos que se registran en cada prueba

- Fecha y persona que prueba.
- Sistema operativo.
- Programa, versión e idioma.
- Tiempo real usado.
- Resultado: **Pasa**, **Pasa con adaptación** (anotar cuál) o **Falla** (anotar el paso y el mensaje).

Las prácticas contables se prueban en una **empresa de prueba** del sistema: nunca sobre datos reales ni mezclando
las copias con errores con la base correcta.

## Programas requeridos

| Bloque | Programa | Prácticas |
|---|---|---|
| Contabilidad | El sistema administrativo contable que use la institución. Debe tener: alta de empresa, plan de cuentas por niveles, asientos con control Debe = Haber, usuarios y perfiles, bitácora, libros Diario, Mayor e Inventario, balance de comprobación, estados y cierre. Necesita además una vía para importar CSV o la carga manual de los diez asientos | 1-10 |
| Imagen raster | Un editor con capas, máscaras, capas de ajuste y exportación a JPG, PNG, WEBP, TIFF o PDF y GIF animado: GIMP, Krita, Photopea o un programa comercial | 11-17 |
| Web | Navegador. Para publicar: un alojamiento educativo habilitado por la institución, opcional | 18-20 |
| Recursos | `recursos/diario_base.csv`, `plan_cuentas.csv`, `diario_error_imputacion.csv`, `diario_error_duplicacion.csv` y `controles_docente.csv`: separador `;`, UTF-8, importes enteros | 4, 6, 7, 9 |

## Pruebas del sistema contable

| P | Procedimiento a probar | Resultado esperado (punto de control) | Evidencia |
|---|---|---|---|
| 1 | Recorrer el menú y clasificar opciones en cuatro módulos | Al menos ocho opciones ubicadas. Anotar los nombres reales del menú para la guía docente | Captura del menú principal |
| 2 | Alta de Despensa San Blas (RUC ficticio 4.812.907-6, SIMPLE 701, ejercicio 2026, guaraní sin decimales) | Un reporte vacío muestra razón social y RUC. Verificar si el sistema rechaza el RUC ficticio por el dígito verificador: el dígito calculado es 0 y el caso usa 6 | Captura del encabezado del reporte. Si el sistema valida el RUC, anotar el mensaje: puede hacer falta un RUC de prueba distinto |
| 3 | Crear los usuarios operador y consulta; probar una carga con el usuario consulta; revisar la bitácora | El usuario consulta no puede registrar. Anotar qué eventos registra la bitácora | Capturas del rechazo y de la bitácora |
| 4 | Cargar el plan de 17 cuentas imputables por niveles (manual o desde `plan_cuentas.csv`); imputar contra 1.1 | El reporte muestra la jerarquía y el sistema rechaza la cuenta de agrupación | Reporte del plan y mensaje de rechazo |
| 5 | Tabla de imputación de seis comprobantes | Coincide con la tabla de la Clase 5 (sin software) | Hoja del estudiante |
| 6 | Cargar los diez asientos (manual o importando `diario_base.csv`); intentar un asiento desbalanceado | 143.899.700 por columna, igual que `controles_docente.csv`; el desbalanceado no se registra | Diario emitido y captura del rechazo. **Comprobar si el sistema importa el CSV y con qué mapeo de columnas** |
| 7 | Emitir el Diario del 01/09 al 30/09 y el Inventario o reporte patrimonial al 01/09; exportar a PDF | Diez asientos y 143.899.700 por columna; inventario de 64.000.000. Primera quincena: 133.912.500 | `diario_sanblas_202609.pdf` |
| 8 | Mayor de Caja, Banco y Ventas | Caja 14.791.300; Banco 28.800.000; Ventas con saldo acreedor de 30.250.000 | Mayores exportados |
| 9 | Balance de comprobación con la base correcta y con cada copia con errores, en empresas separadas | Base: 143.899.700 y 104.828.500. Error de imputación: mismas igualdades, Mercaderías 32.000.000 y Muebles 18.000.000. Duplicación: 11 asientos y 151.249.700 | Tres balances exportados |
| 10 | Ajustes de costo de mercaderías e IVA; Estado de Resultados y Balance General al 30/09; simulación del cierre anual | Utilidad 4.500.000; activo 75.441.300 = 8.941.300 + 66.500.000. Anotar si el sistema permite simular el cierre sin cerrar el ejercicio real | Estados en PDF; captura del cierre o constancia de que se simuló |

## Pruebas del editor de imágenes

| P | Procedimiento a probar | Resultado esperado | Evidencia |
|---|---|---|---|
| 11 | Abrir una foto, calcular el ancho a 300 y 72 ppi, ampliar al 800 %, guardar JPG alto y bajo y PNG | Tabla de tres variantes con su peso; el cambio de ppi no altera los píxeles | Tabla y archivos |
| 12 | Crear el maestro A3 de 3508 × 4961 px a 300 ppi y las salidas de 1080 × 1080, 1600 × 600 y 1200 × 800 px | Las cuatro con medidas exactas. Desafío: sangrado de 3 mm → aproximadamente 3579 × 5031 px | Propiedades de cada archivo |
| 13 | Componer en capas, con opacidad y capa de ajuste | Cuatro capas nombradas y una de ajuste | Captura del panel de capas |
| 14 | Duplicar la capa, recortar a tres proporciones, ajustar con capas de ajuste y clonar | Original intacto; tres versiones | Las tres versiones exportadas |
| 15 | Tres filtros sobre copias; desenfoque del fondo; sombra en el texto | La pieza se lee reducida al 25 % | Capturas comparadas |
| 16 | Grupos «fijas» y «variables»; tres piezas de serie desde `sanblas_maestro_v2` | Misma estructura; cambian foto, nombre y precio | Tres JPG lado a lado |
| 17 | Animación de tres cuadros (1 s, 1 s y 3 s) y exportación de las cuatro salidas | Ciclo de 5 s; cuatro archivos con medidas exactas. **Comprobar si el editor exporta GIF animado**; si no, anotar la herramienta complementaria | GIF y las cuatro salidas |

## Pruebas web

| P | Procedimiento a probar | Resultado esperado | Evidencia |
|---|---|---|---|
| 18 | Clasificar cinco sitios reales y desarmar una página de inicio | Ficha completa con URL y fecha | Ficha y capturas fechadas |
| 19 | Mapa del sitio, textos y portada en WEBP de 1600 px; publicación de prueba solo si hay alojamiento habilitado | Maqueta con cinco secciones. Si se publica: URL, fecha y enlaces probados; si no, quedar rotulado como proyecto | Maqueta, WEBP con su peso y, si corresponde, URL |
| 20 | Planificar la promoción de cinco pasos con indicadores | Plan con fechas, responsables e indicadores; guion de exposición de tres minutos | Plan escrito |

## Prueba de impresión y apertura en Word

Igual que en 2.º:
- imprimir en oficio el tomo, el laboratorio, una página de los planes y el plan anual en apaisado;
- verificar figuras (el texto más chico mide 7 pt), renglones y márgenes;
- abrir los DOCX R3 en Word y comparar la paginación con los PDF de revisión.

# Matriz de hallazgos · Informática 3.º BTC · R1 → R2

Auditoría independiente del 22 de octubre de 2026 sobre los cinco documentos R1 y los cinco CSV de laboratorio.
Leí completos el tomo, el laboratorio, el plan anual, el solucionario y los planes. Las afirmaciones de la bitácora R1
las volví a verificar. Cada corrección está en `build/r2_3btc.py` y queda registrada en `BITACORA_R1_R2_3BTC.md`.

Gravedad:
- **Bloqueante**: enseña algo incorrecto o impide la actividad.
- **Importante**: error de contenido, de sincronía o de maquetación con efecto en el uso.
- **Menor**: redacción o presentación.

## Hallazgos corregidos en R2

| ID | Gravedad | Archivo | Clase / sección | Evidencia en R1 | Corrección R2 | Estado |
|---|---|---|---|---|---|---|
| H-3-01 | Bloqueante | Tomo, Solucionario | Clase 7, recuadro legal; Sol. «Fuentes y alcance» | «El artículo 76 exige autorización judicial para medios mecánicos u otros sistemas modernos». Ese texto fue modificado por la Ley 4924/2013: hoy basta una comunicación del sistema, con firma certificada por escribano, ante la Dirección de Registro Público de Comercio, sin orden judicial | Recuadro reescrito con el texto vigente del art. 76. En el solucionario, la fuente cita la Ley 4924/2013 | Corregido |
| H-3-02 | Importante | Tomo, Solucionario | Clase 5 (texto, concepto clave, pie de la Fig. 6); Sol. Clase 5 D11 | «Lo que se imprime o se envía por celular es el KuDE», sin distinguir receptor | Entrega según el receptor: XML al facturador electrónico, KuDE en papel o digital al no electrónico o consumidor final. CDC + QR. El KuDE no reemplaza al documento electrónico. Igual criterio que 2.º | Corregido |
| H-3-03 | Menor | Tomo | Clase 12, ejemplo del caso | La publicación de redes se crea con «fondo transparente». La tabla de la misma clase y la Práctica 12 dicen «color» | «fondo de color» | Corregido |
| H-3-04 | Importante | Tomo | Clase 15, pie de la Figura 16 | El pie anunciaba «original, desenfoque, contraste e inversión». La figura muestra desenfoque, contraste, escala de grises e inversión | Pie: «Cuatro filtros como operaciones sobre los valores de la imagen: desenfoque, contraste, escala de grises e inversión» | Corregido |
| H-3-05 | Importante | Plan anual | Bandas de unidad y criterios | El plan anual no mostraba las capacidades ni cuáles son las subrayadas | Cada banda lleva su capacidad (U4 y U5: «Diseña…» y «Edita…»). El criterio indica que en el PDF consultado aparecen subrayadas «Aplica…», «Diseña…» y «Edita…», y que la institución confirma esa lectura. Firma no queda sola en la última página | Corregido |
| H-3-06 | Importante | Tomo | Clase 18, ejemplo del caso | `sanblas.com.py` aparece como dominio del comercio sin aclarar que es un ejemplo | Aclaración: nombre de ejemplo, disponibilidad no verificada y no corresponde a un sitio publicado. Las figuras 18-19 dicen «esquema, no sitio publicado» | Corregido |
| H-3-07 | Importante | Tomo | Clase 10, recuadro «En Paraguay» | La obligación 948 (estados financieros, RG DNIT 49/2026) aparecía sin relación con el régimen del caso: San Blas es unipersonal en IRE SIMPLE | Agrega que el profesional verifica si esa obligación le alcanza a San Blas antes de preparar una presentación | Corregido |
| H-3-08 | Importante | Tomo | Clase 9, reportes | El programa incluye «otros registros» y el tomo no los nombraba | Agrega los otros registros que emite el sistema: compras y ventas para el IVA, listados de comprobantes, plan de cuentas | Corregido |
| H-3-09 | Importante | Tomo | Preguntas abiertas y prueba diagnóstica | Sin espacio para responder en el tomo | 174 renglones: 2 en la diagnóstica y en las evaluaciones de unidad, 3 en clases, 4 en etapas. Cada pregunta se mantiene junto a sus renglones | Corregido |
| H-3-10 | Importante | Laboratorio | Práctica 8, desafío | «El extracto muestra un cheque de ₲ 1.500.000 aún no cobrado»: si no se cobró, no figura en el extracto. El solucionario ya planteaba el caso correcto | «…San Blas emitió y registró un cheque de ₲ 1.500.000 que el banco todavía no debitó, por lo que no figura en el extracto». Queda sincronizado con la orientación P8 | Corregido |
| H-3-11 | Importante | Laboratorio, Plan anual, Planes, Solucionario | Práctica 20 paso 6; fila 20; Plan 35; orientación P20 | El encuentro de cierre (75 min + 30 de evaluación) incluía «la presentación del proyecto integrador» de tres minutos por estudiante. Con un curso de 30 son 90 min | Se prepara el guion de tres minutos y la exposición se organiza por grupos o por muestreo. Sincronizado en los cuatro documentos | Corregido |
| H-3-12 | Importante | Tomo | Saltos y rótulos «Actividades de la clase N» | El rótulo de las actividades quedaba huérfano al pie de página en las clases 1, 10, 11 y 18 (render R2) | El constructor detecta el rótulo huérfano en el render y le pone salto de página anterior. (El tomo de 3.º no tenía saltos manuales en párrafo propio: 0 conversiones) | Corregido |
| H-3-13 | Menor | Laboratorio | Práctica 2, paso 5 | «Emitir … y verificar», en infinitivo; el resto del cuaderno usa voseo | «Emití … y verificá» | Corregido |
| H-3-14 | Menor | Solucionario | Clase 2, A1 | El texto de la clave no era idéntico a la opción d) del tomo | Texto idéntico | Corregido |
| H-3-15 | Menor | Solucionario | Evaluación de la Unidad 3, B7 | Clave «declarada», término que la clase no enseña | «cerrada (se aceptan "utilizada" o "declarada" con justificación coherente)» | Corregido |
| H-3-16 | Importante | Planes de clase | Los 36 planes | Cuerpo de 7,5 pt | 9,5 pt, igual que en 2.º. Renglón del docente 30 → 22 guiones. Cada plan sigue en su página (37 páginas) | Corregido |
| H-3-17 | Importante | Tomo, Laboratorio | Figuras 17, 18 y 20 | Las propuestas tenían logotipos de redes y de mensajería comerciales. La 20 traía además errores de render («San Ḃlas», «maestro ercapas») | 17 y 18 corregidas con íconos genéricos («Pedí por mensaje»). La 20 se reconstruyó en vector con los datos concretos del caso. Ver `DECISIONES_FIGURAS_3BTC.md` | Corregido |

## Observaciones abiertas (no corregidas en R2)

| ID | Gravedad | Archivo | Clase / sección | Observación | Qué falta / quién decide |
|---|---|---|---|---|---|
| O-3-01 | Importante | Planes, Plan anual | Encuentros de cierre (clases 3, 7, 10, 14, 17 y 20) | En 120 min entran teoría, práctica integrada (75 min) y evaluación de unidad de 25-30 puntos (30 min). Es ajustado pero posible. No reestructuré los 36 encuentros | Lo valida Fernando con un grupo real |
| O-3-02 | Importante | Tomo | Evaluaciones de las Unidades 1, 2 y 4 | Con los renglones, la última pregunta abierta pasa a una segunda página. La Clase 12 deja su última pregunta sola en la página 47 | Aceptable en doble faz. Para una sola hoja, reducir o reorganizar |
| O-3-03 | Importante | Figuras | Notas al pie de las propuestas raster | A 14,2 cm, los títulos y datos quedan en 7-14 pt. Las notas secundarias («Esquema didáctico…», «Importes en guaraníes») quedan en unos 4-6 pt, y menos en el laboratorio (9,6 cm) | Prueba de impresión. Rehacer en vector las figuras cuyas notas sean necesarias |
| O-3-04 | Importante | Tomo | Clase 7 | El texto del art. 76 tras la Ley 4924/2013 se tomó de resúmenes de BACN y de una consulta vinculante de la DNIT: los sitios oficiales no respondieron desde este entorno. Hay además un proyecto de 2019 que modifica la Ley 4924; no sé si se aprobó | Verificar el texto consolidado en BACN antes de liberar |
| O-3-05 | Importante | Tomo, Solucionario | Clase 20 | La Ley 7593/2025 (datos personales), publicada el 27/11/2025, entra en vigor 24 meses después según su art. 57. Fuentes secundarias coinciden; no leí el texto oficial | Verificar en BACN |
| O-3-06 | Menor | Tomo | Clase 2 | IRE SIMPLE admite registros simplificados, pero el caso lleva contabilidad completa. Didácticamente es válido: el sistema lo permite y el programa lo pide | Nota de alcance opcional |
| O-3-07 | Menor | Tomo | Clase 3 | El recuadro de la Clase 3 cita solo la Ley 6534/2020 (datos crediticios) | Al entrar en vigor la Ley 7593/2025, mencionarla también |
| O-3-08 | Importante | Laboratorio | Todas las prácticas | No se probó ninguna práctica en software real (sistema contable, editor raster, alojamiento web). La importación de los CSV en un sistema contable concreto no está probada | Prueba de laboratorio con el software de la institución |
| O-3-09 | Importante | Todos | Organización anual | Hora cátedra de 40 min y 36 encuentros: referencias editoriales sin ratificar | Institución |

## Verificado sin hallazgos

- CSV: los 10 asientos de `diario_base.csv` balancean. Total 143.899.700 por columna. Saldos deudores = acreedores =
  104.828.500. Todas las cuentas existen en `plan_cuentas.csv` con el mismo nombre. `controles_docente.csv` coincide
  asiento por asiento.
- `diario_error_imputacion.csv`: mismos totales; Mercaderías 32.000.000 y Muebles 18.000.000.
  `diario_error_duplicacion.csv`: 11 asientos y 151.249.700, por la compra del 05/09 repetida. Coinciden con la
  orientación P9.
- Aritmética del tomo:
  - Caja: 40.662.500 − 25.871.200 = 14.791.300. Banco: 42.000.000 − 13.200.000 = 28.800.000.
  - IVA: DF 1.800.000 + 612.500 = 2.412.500. CF 900.000 + 350.000 + 300.000 + 87.200 = 1.637.200. A pagar 775.300.
  - IPS: 288.000 / 528.000 / 816.000. Neto del sueldo 2.912.000.
  - Resultado: CMV 18.150.000, utilidad bruta 12.100.000, gastos 7.600.000, utilidad 4.500.000.
  - Balance: Mercaderías al cierre 22.850.000. Activo 75.441.300 = pasivo 8.941.300 + PN 66.500.000.
  - Proyección: 30.250.000 × 12 = 363.000.000.
  - Logo: 2400 px a 300 ppi = 20,32 cm; 8.640.000 bytes ≈ 8,24 MiB.
  - A3 a 300 ppi = 3508 × 4961 px. Etiqueta 1200 × 800 px a 300 ppi ≈ 102 × 68 mm.
  - Primera quincena 133.912.500; con sangrado de 3 mm, 3579 × 5031 px.
- 119 claves de opción múltiple, letra y texto, entre tomo y solucionario. Distribución 28/33/28/30. Los ítems de
  completar, V/F y abiertos coinciden en número y sección.
- Puntajes: unidades de 30 = 5 + 4 + 4 + 2 × 8,5; de 25 = 4 + 3 + 3 + 15; etapas de 40 = 6 + 5 + 5 + 3 × 8.
- 108 HC en 36 encuentros: 14 × 6 h + 6 × 3 h + 2 × 3 h. Los planes suman 120 min por encuentro.
- Cobertura del programa MEC BTC 3.º: 3 unidades temáticas y 4 capacidades. Los contenidos «Software de
  Contabilidad», «Temporización de las transiciones» y «Promociones en la WEB» tienen clase propia.
- Régimen tributario (coincide con la doctrina verificada):
  - SIMPLE (701) para unipersonales hasta ₲ 2.000 M; RESIMPLE (702) solo para unipersonales hasta ₲ 80 M.
  - SIMPLE (701) y RESIMPLE (702) no están disponibles para S.R.L.
  - SIFEN para proveedores del Estado (RG 41/2025); e-Kuatia'i.
  - Ley 1334/98; salario mínimo ₲ 3.044.000; IPS 9 % / 16,5 %.
- RUC del caso 4.812.907-6: su dígito verificador por módulo 11 sería 0, así que no puede ser un RUC real. Es
  coherente con «datos ficticios».

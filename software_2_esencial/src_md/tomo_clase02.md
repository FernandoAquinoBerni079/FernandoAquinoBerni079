@@H2 Clase 2 — La fuente de alimentación
[[FICHA]]
Capacidad: Analiza las principales funciones de una fuente de alimentación de computadora.
Tema: Fuentes de alimentación: concepto, funciones, tipos, voltajes utilizados y voltaje real.
- Explica la función de conversión de corriente que cumple la fuente.
- Identifica los voltajes de salida de una fuente ATX y sus usos.
- Interpreta la diferencia entre potencia declarada y potencia real.
[[/FICHA]]
[[IMG T_image3.jpg|13.2]]
Figura 2.1 — Fuente ATX de cableado fijo. © Raimond Spekking / CC BY-SA 4.0, vía Wikimedia Commons.
## Concepto y función
La fuente de alimentación (PSU, power supply unit) convierte la corriente alterna del tomacorriente (en Paraguay, 220 voltios) en las corrientes continuas de bajo voltaje que consumen los componentes. Además filtra la energía, protege contra picos y distribuye la potencia mediante cables con conectores específicos para la placa, el procesador, los discos y las tarjetas.
[[CAJA Concepto clave — Tolerancia de voltaje]]
Margen de variación aceptado alrededor del voltaje nominal (±5 % en el estándar ATX). Dentro de ese rango el componente funciona bien; fuera de él aparecen reinicios, cuelgues o daños.
[[/CAJA]]
## Tipos de fuente
El estándar dominante es la fuente ATX, con variantes de tamaño como SFX para gabinetes compactos. Según el cableado pueden ser fijas, semimodulares o modulares. La certificación 80 PLUS evalúa la eficiencia energética de la fuente bajo cargas definidas: indica qué proporción de la energía tomada del tomacorriente llega a los componentes y cuánta se pierde como calor. No certifica por sí sola la calidad general de la fuente ni garantiza que cualquier dato publicitario de potencia sea correcto.
[[CAJA Ejemplo — Nominal vs. real / Para el presupuesto del Instituto Ko'ẽju, Panambi compara dos fuentes de '500 W': una genérica sin certificación y una 80 Plus Bronze. La certificada cuesta más y su sello 80 PLUS permite verificar un nivel de eficiencia energética ensayado. Para saber si realmente entrega su potencia nominal de forma adecuada hay que revisar la especificación y pruebas confiables del modelo; el sello 80 PLUS no sustituye esa verificación. En diez equipos funcionando toda la jornada escolar, la diferencia se nota en la factura de la ANDE.]]
[[/CAJA]]
## Voltajes utilizados
Una fuente ATX entrega varias líneas de voltaje a la vez: +12 V (procesador, tarjeta de video, motores de discos), +5 V (puertos USB y circuitos), +3,3 V (chips de la placa) y +5 VSB (standby: mantiene el equipo listo para encender). Cada conector lleva la combinación de líneas que su componente necesita.
Seguí las flechas desde el tomacorriente: la fuente convierte los 220 V y reparte cuatro líneas de voltaje, cada una hacia los componentes que la necesitan.
[[IMG T_image4.png|16.0]]
Figura 2.2 — De los 220 V del tomacorriente a las líneas de la fuente ATX.
[[TABLA]]
Línea de voltaje | Rango aceptado (±5 %) | Alimenta principalmente a
+12 V | 11,4 V a 12,6 V | Procesador, tarjeta de video, motores de discos
+5 V | 4,75 V a 5,25 V | Puertos USB, circuitos lógicos
+3,3 V | 3,14 V a 3,47 V | Chips de la placa madre, ranuras PCIe y SSD M.2
+5 VSB | 4,75 V a 5,25 V | Modo de espera (standby)
[[/TABLA]]
## Voltaje real y potencia real
Los voltajes nominales admiten tolerancias definidas por la especificación ATX; para las líneas principales trabajadas en este curso usamos ±5 % como referencia didáctica. Con la potencia hay que ser más cuidadosos: una etiqueta puede anunciar 600 W, pero la decisión técnica debe considerar la potencia nominal del modelo, la corriente disponible en sus líneas, sus protecciones y ensayos confiables. 80 PLUS sirve para comparar eficiencia, no para certificar por sí sola la potencia sostenida ni la calidad total del producto.
[[CAJA En Paraguay — 220 V, tormentas y picos de tensión]]
La red eléctrica paraguaya es de 220 V y 50 Hz, y en época de tormentas los picos de tensión son frecuentes. Por eso los técnicos recomiendan acompañar cada equipo con un protector de picos o una UPS: cuesta menos que reemplazar una placa madre quemada.
[[/CAJA]]
## Cuánta potencia hace falta: cómo se calcula
Elegir la fuente no es «comprar la de más watts». Se suma el consumo aproximado de los componentes, se agrega un margen de seguridad y se elige una fuente de calidad que cubra ese total con holgura. El margen sirve para los picos de consumo (al arrancar, al abrir varios programas) y para que la fuente trabaje cerca de la mitad de su capacidad, donde suele rendir mejor y calentar menos.
La eficiencia completa la cuenta. Si una fuente tiene 85 % de eficiencia, de cada 100 W que toma del tomacorriente entrega 85 W a los componentes y pierde 15 W como calor. Por eso, para un mismo equipo, una fuente más eficiente consume menos de la red eléctrica.
[[CAJA Ejemplo — La fuente para la PC de la secretaría]]
Panambi calcula la fuente de la PC de la secretaría del Instituto Ko'ẽju, que no lleva tarjeta de video.
Paso 1. Consumo estimado: procesador 65 W + placa y memorias 35 W + SSD 6 W + ventiladores 9 W + periféricos USB 15 W = 130 W.
Paso 2. Margen del 50 %: 130 W × 1,5 = 195 W. Cualquier fuente de calidad de 300 W o más cubre ese total con holgura.
Paso 3. Consumo desde la red con una fuente de 85 % de eficiencia: 130 W ÷ 0,85 ≈ 153 W. Con una de 75 %, serían 130 W ÷ 0,75 ≈ 173 W: unos 20 W más durante toda la jornada.
Paso 4. En el presupuesto se escribe la cuenta, no solo el modelo elegido.
[[/CAJA]]
Medir también es parte del trabajo. Con un multímetro, o con el programa de monitoreo de la placa, se lee el voltaje real de cada línea y se compara con su rango: una línea de +12 V que marca 11,9 V está dentro de tolerancia; una que baja de 11,4 V con el equipo trabajando avisa que la fuente está fallando.
[[CAJA Errores frecuentes — Al elegir y revisar la fuente]]
• Confundir el sello 80 PLUS con una garantía de potencia: certifica eficiencia, no los watts sostenidos.
• Elegir por los watts de la etiqueta sin revisar la marca, el modelo, las protecciones ni las pruebas del producto.
• Sumar el consumo sin margen: la fuente trabaja al límite, calienta y falla antes.
• Medir el voltaje con el equipo en reposo y dar la fuente por buena: los problemas aparecen con carga.
[[/CAJA]]
## Actividades de aplicación
Marcá la opción correcta:
1. La función principal de la fuente es:
    a) Almacenar energía para cortes de luz
    b) Convertir corriente alterna en continua de bajo voltaje
    c) Aumentar el voltaje del tomacorriente
    d) Refrigerar el gabinete
2. La línea que alimenta al procesador y a la tarjeta de video es la de:
    a) +3,3 V
    b) +5 V
    c) +12 V
    d) +5 VSB
3. La certificación 80 Plus indica:
    a) La potencia máxima de la fuente
    b) La eficiencia energética de la fuente
    c) La cantidad de conectores
    d) El nivel de ruido del ventilador
4. Con tolerancia de ±5 %, una línea de +5 V es correcta si mide:
    a) Entre 4,75 V y 5,25 V
    b) Exactamente 5,00 V
    c) Entre 4 V y 6 V
    d) Más de 5,5 V
Completá los espacios:
5. En Paraguay la red eléctrica domiciliaria entrega ________ voltios de corriente alterna.
6. La línea +5 ________ mantiene el equipo en modo de espera, listo para encender.
7. Una fuente ________ permite conectar solo los cables que se van a usar.
Verdadero o falso (justificá las falsas):
8. (....) La potencia declarada en la caja de una fuente genérica siempre coincide con la real.
9. (....) La fuente también filtra la energía y protege contra picos.
10. (....) Una línea de +12 V que mide 12,4 V está fuera de tolerancia.
Respondé y fundamentá:
11. ¿Por qué una fuente de mala calidad puede dañar componentes que sí son de buena calidad?
12. Explicá con tus palabras qué gana una escuela al elegir fuentes con certificación 80 Plus para diez equipos.

@@H2 Clase 7 — Las memorias
[[FICHA]]
Capacidad: Identifica los diferentes tipos de memorias utilizados en la computadora.
Tema: Memorias: concepto, tipos, características y conexión.
- Diferencia memoria RAM, ROM y caché por su función.
- Interpreta capacidad, tipo y frecuencia de un módulo de RAM.
- Explica el montaje correcto de los módulos y el doble canal.
[[/FICHA]]
[[IMG T_image13.jpg|12.8]]
Figura 7.1 — Instalación de un módulo de memoria RAM.
## Concepto y jerarquía
La computadora usa varias memorias organizadas en jerarquía: cuanto más cerca del procesador, más rápida y más chica. La caché vive dentro de la CPU; la RAM es la memoria de trabajo donde residen los programas abiertos; el almacenamiento (disco o SSD) guarda todo de forma permanente. El firmware de la placa (UEFI, sucesor del BIOS) conserva las instrucciones de arranque en un chip de memoria flash no volátil: históricamente era una ROM de solo lectura, y hoy se puede actualizar con las herramientas del fabricante.
Leé la jerarquía de arriba hacia abajo: cuanto más cerca del procesador, más rápida y más chica es la memoria. A la derecha, cómo el doble canal duplica el ancho de banda.
[[IMG T_image14.png|16.0]]
Figura 7.2 — Jerarquía de memorias y doble canal.
[[CAJA Concepto clave — Volatilidad]]
Propiedad de una memoria de perder su contenido al cortarse la energía. La RAM es volátil; el SSD y la ROM no lo son. Por eso 'guardar el archivo' significa pasarlo de la RAM al almacenamiento permanente.
[[/CAJA]]
## La memoria RAM
RAM significa memoria de acceso aleatorio: el procesador lee y escribe cualquier posición en el mismo tiempo. Es volátil (se borra al apagar). Los módulos actuales son DDR4 y DDR5 en formato DIMM (equipos de escritorio) y SO-DIMM (notebooks). Cuanta más RAM, más programas y pestañas conviven sin que el equipo se arrastre.
[[CAJA Ejemplo — ¿8 o 16 GB para el aula?]]
Panambi calcula la RAM del aula del Instituto Ko'ẽju: sistema operativo más navegador con varias pestañas más una planilla ocupan cómodamente 8 GB. Cotiza 2 × 8 GB por equipo: 16 GB en doble canal, con margen para los próximos años sin cambiar de placa.
[[/CAJA]]
## Características de un módulo
Un módulo se describe por su capacidad (8, 16, 32 GB), su tipo (DDR4/DDR5, no intercambiables entre sí: la muesca del módulo es distinta) y su frecuencia o velocidad de transferencia (por ejemplo 3200 MT/s). La placa define qué tipo acepta y hasta qué frecuencia aprovecha. La velocidad observada no basta para identificar la generación: antes de comprar, verificá el fabricante y modelo del equipo o de la placa madre y consultá su especificación de memoria.
[[TABLA]]
Memoria | Ubicación | Velocidad relativa | ¿Volátil?
Caché | Dentro de la CPU | La más rápida | Sí
RAM (DDR4/DDR5) | Ranuras DIMM de la placa | Muy rápida | Sí
ROM / firmware (flash) | Chip de la placa | Lenta; se copia a la RAM al arrancar | No
Almacenamiento (SSD/HDD) | Bahías o M.2 | La más lenta de la jerarquía | No
[[/TABLA]]
## Conexión y doble canal
Los módulos se insertan en las ranuras DIMM alineando la muesca y presionando hasta que las trabas laterales cierren solas. Instalando dos módulos iguales en las ranuras correctas se habilita el doble canal: la placa accede a ambos en paralelo y el ancho de banda de memoria prácticamente se duplica.
[[CAJA En Paraguay — La ampliación más pedida]]
En los talleres del país, la ampliación de RAM es el servicio de mejora más solicitado: es barata, rápida y el cliente la percibe de inmediato. El técnico verifica antes el tipo (DDR4 o DDR5), las ranuras libres y el máximo que soporta la placa: tres datos que evitan comprar un módulo que no sirve.
[[/CAJA]]
## Cuánta memoria hace falta y cómo se verifica
La memoria necesaria se estima por el uso real. Windows 11 y sus servicios ocupan alrededor de 3 a 4 GB; un navegador con diez pestañas puede sumar otros 2 a 3 GB; una planilla grande o una videollamada, 1 GB más cada una. Cuando la RAM se llena, el sistema empieza a usar el disco como memoria de reserva (archivo de paginación) y todo se vuelve lento, aunque el procesador esté libre. En el Administrador de tareas, la pestaña Rendimiento → Memoria muestra cuánto se usa y cuántas ranuras están ocupadas.
Antes de ampliar se reúnen tres datos: el tipo de memoria (DDR4 o DDR5), la cantidad de ranuras libres y el máximo que admite la placa. También conviene sumar módulos iguales en capacidad y velocidad: si se mezclan, todos trabajan a la velocidad del más lento.
[[CAJA Ejemplo — Ampliar la PC de la biblioteca]]
La PC de la biblioteca del Instituto Ko'ẽju tiene un solo módulo DDR4 de 4 GB a 2666 MT/s, la placa tiene dos ranuras y admite hasta 32 GB. Con el catálogo abierto y varias pestañas, el Administrador de tareas marca 92 % de memoria en uso.
Paso 1. Diagnóstico: la RAM está casi llena; ese es el cuello de botella.
Paso 2. Opción A: sumar otro módulo de 4 GB igual. Resultado: 8 GB en doble canal.
Paso 3. Opción B: reemplazar por 2 × 8 GB DDR4. Resultado: 16 GB en doble canal, con margen para los próximos años.
Paso 4. Recomendación: la opción B si el presupuesto lo permite; la A como solución mínima. En los dos casos se respeta el tipo DDR4 que acepta la placa.
[[/CAJA]]
[[CAJA Errores frecuentes — Con la memoria]]
• Comprar un módulo por la capacidad sin verificar si la placa usa DDR4 o DDR5.
• Instalar dos módulos en ranuras que no forman doble canal: el manual de la placa indica cuáles usar.
• Confundir la memoria RAM con el almacenamiento: «tengo 512 GB de memoria» suele referirse al disco.
• Mezclar módulos de distinta velocidad y esperar que trabajen a la del más rápido.
[[/CAJA]]
## Actividades de aplicación
Marcá la opción correcta:
1. La memoria de trabajo donde residen los programas abiertos es la:
    a) ROM
    b) Caché
    c) RAM
    d) SSD
2. Que la RAM sea volátil significa que:
    a) No se puede ampliar
    b) Pierde su contenido al apagar
    c) Es más lenta que el disco
    d) Solo admite lectura
3. Los módulos DDR4 y DDR5:
    a) Son intercambiables entre sí
    b) Tienen muescas distintas y no se intercambian
    c) Solo cambian de color
    d) Usan la misma frecuencia
4. El doble canal se logra instalando:
    a) Un módulo grande
    b) Dos módulos iguales en las ranuras correctas
    c) Módulos de distinto tipo
    d) La RAM en el conector M.2
Completá los espacios:
5. La memoria ultrarrápida integrada dentro del procesador es la ________.
6. El formato de módulo de RAM de las notebooks se llama ________-DIMM.
7. Las instrucciones de arranque residen en el ________ de la placa, guardado en un chip de memoria flash.
Verdadero o falso (justificá las falsas):
8. (....) Guardar un archivo lo pasa de la RAM al almacenamiento permanente.
9. (....) Cuanto más lejos del procesador, más rápida es la memoria.
10. (....) La placa madre define el tipo y la frecuencia máxima de RAM que aprovecha.
Respondé y fundamentá:
11. Un equipo con 4 GB de RAM 'se arrastra' con muchas pestañas abiertas. Explicá qué pasa por dentro y qué solución proponés.
12. ¿Por qué conviene comprar 2 × 8 GB en vez de 1 × 16 GB si la placa tiene dos ranuras? ¿Y qué desventaja tiene?

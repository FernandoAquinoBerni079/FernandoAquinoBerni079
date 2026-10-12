@@H2 Clase 8 — Almacenamiento: discos duros y SSD
[[FICHA]]
Capacidad: Reconoce las características de los dispositivos de almacenamiento secundario.
Tema: Discos duros y unidades SSD: concepto, componentes, tipos, características y conexión.
- Describe los componentes internos de un disco duro mecánico.
- Compara HDD y SSD en velocidad, resistencia y costo por GB.
- Identifica las conexiones SATA y M.2 NVMe y sus diferencias.
[[/FICHA]]
[[IMG T_image15.jpg|12.8]]
Figura 8.1 — Comparación de unidades HDD y SSD en el taller.
## El disco duro mecánico (HDD)
El disco duro guarda la información magnéticamente sobre platos giratorios. Sus componentes: los platos (giran a 5.400 o 7.200 vueltas por minuto), los cabezales de lectura/escritura que flotan sobre ellos, el brazo que los desplaza y la electrónica controladora. Al ser mecánico, es sensible a golpes y más lento para encontrar datos dispersos.
[[CAJA Concepto clave — Almacenamiento secundario]]
Memoria permanente y de gran capacidad donde residen el sistema, los programas y los archivos del usuario. A diferencia de la RAM, conserva los datos sin energía.
[[/CAJA]]
## La unidad de estado sólido (SSD)
El SSD guarda los datos en chips de memoria flash: no tiene partes móviles. Resulta mucho más rápido (el sistema arranca en segundos), silencioso y resistente a golpes. Su costo por gigabyte es mayor que el del HDD, aunque la diferencia se achica año a año.
[[CAJA Ejemplo — El arranque que convence]]
Panambi demuestra al Instituto Ko'ẽju la diferencia con dos equipos idénticos: uno con HDD tarda más de un minuto en estar operativo; el otro, con SSD NVMe, unos quince segundos. En un aula donde la clase dura 40 minutos, ese minuto por equipo y por encendido es tiempo de enseñanza recuperado.
[[/CAJA]]
## Tipos y conexiones
Los HDD de escritorio suelen ser de 3,5 pulgadas y conectarse por SATA (un cable de datos y otro de energía). En SSD hay que distinguir formato físico e interfaz: existen SSD de 2,5 pulgadas por SATA y módulos M.2. Un módulo M.2 puede trabajar con SATA o con PCI Express/NVMe según el modelo, la llave (key) y la compatibilidad del zócalo de la placa. Por eso «M.2» no significa automáticamente «NVMe». Los NVMe que usan PCIe pueden alcanzar varios miles de MB/s, mientras SATA queda limitado por su propia interfaz.
Compará las dos tecnologías: el disco duro tiene partes móviles (platos, cabezal, brazo); el SSD, chips de memoria. Recordá además que M.2 describe un formato: para saber si un módulo es SATA o NVMe/PCIe hay que revisar su especificación y la del zócalo.
[[IMG T_image16.png|16.0]]
Figura 8.2 — Disco duro mecánico frente a unidad de estado sólido.
[[TABLA]]
Característica | HDD 3,5" | SSD SATA 2,5" | SSD M.2 NVMe
Tecnología | Platos magnéticos | Memoria flash | Memoria flash
Velocidad típica | 80–250 MB/s | Hasta ~550 MB/s | 2.000–14.000 MB/s (según PCIe 3.0, 4.0 o 5.0)
Resistencia a golpes | Baja | Alta | Alta
Costo por GB | El más bajo | Medio | Medio-alto
Conexión | SATA + energía | SATA + energía | Ranura M.2 (PCIe)
[[/TABLA]]
## Cómo se combinan en la práctica
Una configuración habitual es usar SSD para sistema operativo y programas y, cuando se necesita mucha capacidad económica, sumar almacenamiento adicional. En equipos nuevos de oficina y aula un solo SSD puede ser suficiente. La elección entre SATA y NVMe/PCIe debe basarse en compatibilidad, capacidad, rendimiento requerido, costo y posibilidad de ampliación.
[[CAJA En Paraguay — La migración a SSD]]
Clonar el disco de un equipo con HDD hacia un SSD es hoy uno de los servicios más rentables de los talleres paraguayos: con una inversión moderada, una máquina de hace años vuelve a sentirse ágil. Es la alternativa que el técnico honesto ofrece antes de recomendar cambiar todo el equipo.
[[/CAJA]]
## Capacidad real, salud y respaldo
La capacidad que muestra Windows es menor que la que dice la caja. El fabricante cuenta en unidades decimales (1 GB = 1.000.000.000 bytes) y Windows informa en unidades binarias (1 GiB = 1.073.741.824 bytes), aunque las rotule «GB». Por eso un SSD de 500 GB aparece con unos 465 GB: no falta espacio, cambia la unidad de medida. A eso se suma lo que ocupa el sistema y las particiones de recuperación.
Los discos también envejecen. Los HDD acumulan sectores dañados y los SSD tienen una cantidad limitada de escrituras (indicada como TBW, terabytes escritos). El estado se revisa con los datos SMART del disco, que muestran temperatura, horas de uso y porcentaje de vida restante; ningún disco reemplaza a un respaldo.
[[CAJA Ejemplo — ¿Alcanza el SSD del equipo de la directora?]]
El equipo de la dirección del Instituto Ko'ẽju tiene un SSD de 256 GB. Windows lo muestra con 238 GB, de los que hay 205 GB usados, y la directora quiere guardar este año unos 40 GB de fotos de actos.
Paso 1. Espacio libre: 238 − 205 = 33 GB. No alcanza para 40 GB.
Paso 2. Margen sano: conviene mantener al menos un 15 a 20 % libre para que el sistema trabaje bien (en este disco, unos 36 a 48 GB).
Paso 3. Opciones: migrar a un SSD de 1 TB y conservar el de 256 GB como respaldo, o guardar las fotos en un disco externo.
Paso 4. Recomendación: migrar el sistema al SSD nuevo y sumar una copia de las fotos en un disco externo.
[[/CAJA]]
En un taller, la regla práctica es 3-2-1: tres copias de los datos importantes, en dos medios distintos y una fuera del lugar (por ejemplo, en la nube o en otra sede).
[[CAJA Errores frecuentes — Con el almacenamiento]]
• Pensar que al disco «le falta» capacidad por la diferencia entre GB decimales y binarios.
• Comprar un módulo M.2 NVMe para una placa cuya ranura M.2 solo acepta SATA.
• Guardar todo en un único disco sin respaldo: un SSD también puede fallar de un día para otro.
• Llenar el disco del sistema hasta el último gigabyte: el equipo se vuelve lento y las actualizaciones fallan.
[[/CAJA]]
## Actividades de aplicación
Marcá la opción correcta:
1. Los componentes móviles del disco duro son:
    a) Chips y controladora
    b) Platos, cabezales y brazo
    c) Ranuras y carriles
    d) Celdas de memoria flash
2. La ventaja principal del SSD frente al HDD es:
    a) Mayor capacidad al mismo precio
    b) Mayor velocidad y resistencia
    c) Menor consumo de RAM
    d) No necesitar conexión
3. El límite práctico de velocidad de la interfaz SATA ronda los:
    a) 100 MB/s
    b) 550 MB/s
    c) 3.000 MB/s
    d) 7.000 MB/s
4. Un SSD M.2 NVMe se conecta:
    a) Con cable SATA y energía
    b) Directo en la ranura M.2 de la placa
    c) Al puerto USB interno
    d) A la ranura DIMM
Completá los espacios:
5. Los platos de un disco duro de escritorio giran típicamente a 5.400 o ________ vueltas por minuto.
6. El SSD guarda los datos en chips de memoria ________.
7. La configuración recomendada combina SSD para el sistema y ________ para archivos grandes.
Verdadero o falso (justificá las falsas):
8. (....) El SSD es más sensible a los golpes que el HDD.
9. (....) Un SSD conectado por SATA no puede superar el límite de esa interfaz.
10. (....) El almacenamiento secundario pierde los datos al apagar el equipo.
Respondé y fundamentá:
11. Un estudio contable guarda quince años de documentos digitalizados y quiere velocidad para trabajar. Proponé una configuración de almacenamiento y justificala.
12. ¿Por qué la velocidad de un disco importa aunque el procesador sea potente?

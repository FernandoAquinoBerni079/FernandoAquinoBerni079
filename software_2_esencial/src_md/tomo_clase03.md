@@H2 Clase 3 — La placa madre
[[FICHA]]
Capacidad: Identifica los diferentes tipos de Placa Madre utilizados en las computadoras.
Tema: Placa madre: concepto, clasificación, características y componentes.
- Describe la función integradora de la placa madre.
- Clasifica placas madre según su factor de forma.
- Ubica los componentes principales de una placa madre.
[[/FICHA]]
[[IMG T_image5.jpg|11.4]]
Figura 3.1 — Detalle de componentes y ranuras de una placa madre. Lenharth Systems / CC0, vía Wikimedia Commons.
## Concepto
La placa madre (motherboard o placa base) es el circuito impreso principal de la computadora: sobre ella se montan o conectan todos los demás componentes. Su función es integrarlos y comunicarlos entre sí a través de sus circuitos, llamados buses. Si el procesador es el cerebro, la placa madre es el sistema nervioso que lo conecta con todo lo demás.
[[CAJA Concepto clave — Chipset]]
Conjunto de chips de la placa madre que administra la comunicación entre el procesador y el resto de los componentes. Define cuántos puertos, ranuras y prestaciones puede ofrecer la placa.
[[/CAJA]]
## Clasificación
Las placas se clasifican principalmente por su factor de forma: ATX (estándar, con más ranuras y conectores), micro-ATX (más chica y económica, la más vendida para oficina) y mini-ITX (compacta, para equipos pequeños). También se distinguen por la plataforma que admiten: cada placa está diseñada para una familia concreta de procesadores Intel o AMD.
[[CAJA Ejemplo — Elegir la placa para el aula]]
Para las diez computadoras del Instituto Ko'ẽju, Panambi elige placas micro-ATX: cuestan menos que las ATX, entran en las torres medias ya cotizadas y ofrecen las dos ranuras de memoria y el conector M.2 que el aula necesita. En el presupuesto, cada elección se justifica por escrito.
[[/CAJA]]
## Características
Al evaluar una placa se miran: el zócalo (qué procesadores acepta), el chipset (qué prestaciones habilita), la cantidad y tipo de ranuras de memoria, las ranuras de expansión, los conectores de almacenamiento (SATA y M.2), el panel trasero de puertos y la calidad de los componentes de energía (VRM) que alimentan al procesador.
[[TABLA]]
Factor de forma | Tamaño (aprox.) | Ranuras de expansión típicas | Uso frecuente
ATX | 30,5 × 24,4 cm | 4 a 7 | Equipos de rendimiento, ampliables
micro-ATX | 24,4 × 24,4 cm | 2 a 4 | Oficinas, aulas, hogares
mini-ITX | 17 × 17 cm | 1 | Equipos compactos
[[/TABLA]]
## Componentes principales
Sobre la placa se identifican: el zócalo o socket del procesador, las ranuras DIMM para memoria RAM, el chipset (a menudo bajo un disipador), las ranuras PCI Express, los conectores SATA y M.2, los conectores de energía de 24 y 8 pines, la pila que conserva la configuración (CMOS), y los pines del panel frontal donde se conectan el botón de encendido y las luces del gabinete.
Recorré el mapa de la placa y ubicá cada componente: el zócalo del procesador, las ranuras DIMM, el chipset, las ranuras PCIe, los conectores SATA y M.2, los de energía y la pila CMOS.
[[IMG T_image6.png|16.0]]
Figura 3.2 — Mapa de una placa madre ATX con sus componentes principales.
[[CAJA En Paraguay — Placas de generaciones anteriores]]
En el mercado local convive lo nuevo con placas de generaciones anteriores a precios bajos. Antes de recomendar una 'oferta', el técnico verifica que el zócalo y el chipset tengan repuestos y soporte: una placa discontinuada barata puede salir cara cuando falla y no hay reemplazo compatible.
[[/CAJA]]
## Leer la ficha técnica de una placa madre
La ficha técnica del fabricante es la fuente de verdad para decidir. Una línea como «micro-ATX, zócalo LGA1700, chipset B760, 2 × DDR4 (máx. 64 GB), 1 × PCIe 4.0 x16, 2 × M.2, 4 × SATA» dice casi todo lo que el técnico necesita: el tamaño (entra en una torre media o mini), qué familia de procesadores acepta (el zócalo), qué memoria lleva (DDR4, no DDR5) y cuántas unidades de almacenamiento se pueden conectar. Las placas de AMD siguen la misma lógica con sus zócalos AM4 (DDR4) y AM5 (DDR5).
Además del zócalo, el procesador debe figurar en la lista de compatibilidad de la placa (CPU support list): a veces un procesador nuevo necesita una versión más reciente del firmware para arrancar. Esa lista se consulta en el sitio del fabricante antes de cerrar el presupuesto.
[[CAJA Ejemplo — Verificar una combinación antes de comprar]]
Un cliente de Panambi trae esta propuesta: placa mini-ITX con zócalo AM5 y 2 ranuras DDR5, procesador AMD de zócalo AM5 y dos módulos DDR4 de 8 GB que ya tenía.
Paso 1. Zócalo: placa AM5 y procesador AM5. Compatible.
Paso 2. Memoria: la placa admite DDR5 y los módulos son DDR4. Incompatible: las muescas están en lugares distintos y no encastran.
Paso 3. Almacenamiento y tamaño: se revisa que la placa tenga al menos una ranura M.2 para el SSD y que el gabinete admita mini-ITX.
Paso 4. Conclusión para el cliente: la combinación sirve si se reemplazan los módulos por DDR5; se presupuesta ese cambio y se explica por qué.
[[/CAJA]]
También importa la calidad de la alimentación del procesador. Las placas de gama baja traen menos fases de VRM y disipadores más chicos: sirven para procesadores de consumo moderado, pero se calientan con los más exigentes. Para un aula, una placa de gama de entrada con un procesador de 65 W es una combinación equilibrada; para una estación de edición de video conviene una placa con mejor VRM.
[[CAJA Errores frecuentes — Al elegir la placa]]
• Suponer que «es Intel» o «es AMD» alcanza: lo que decide es el zócalo y la lista de compatibilidad.
• Mezclar DDR4 y DDR5: cada placa acepta un solo tipo de memoria.
• No contar los conectores: una placa con una sola ranura M.2 obliga a usar SATA para el segundo disco.
• Olvidar el firmware: un procesador más nuevo que la placa puede necesitar una actualización previa.
[[/CAJA]]
## Actividades de aplicación
Marcá la opción correcta:
1. La función principal de la placa madre es:
    a) Procesar los datos
    b) Integrar y comunicar todos los componentes
    c) Almacenar los programas
    d) Convertir la corriente
2. El componente de la placa que define qué procesadores acepta es:
    a) El chipset
    b) La pila CMOS
    c) El zócalo o socket
    d) El conector de 24 pines
3. El factor de forma de placa más compacto de los vistos es:
    a) ATX
    b) micro-ATX
    c) mini-ITX
    d) E-ATX
4. La pila de la placa madre sirve para:
    a) Encender el equipo sin fuente
    b) Conservar la configuración básica (CMOS)
    c) Alimentar al procesador
    d) Cargar la batería del monitor
Completá los espacios:
5. Los circuitos de la placa que comunican los componentes entre sí se llaman ________.
6. Las ranuras donde se insertan los módulos de memoria RAM se denominan ranuras ________.
7. El ________ administra la comunicación entre el procesador y el resto de la placa.
Verdadero o falso (justificá las falsas):
8. (....) Cualquier procesador puede montarse en cualquier placa madre.
9. (....) Las placas micro-ATX son las más vendidas para equipos de oficina.
10. (....) El VRM es el circuito que alimenta de energía al procesador.
Respondé y fundamentá:
11. ¿Por qué se dice que la placa madre 'condiciona' todas las demás compras del equipo? Da dos ejemplos.
12. Un cliente quiere 'la placa más barata'. ¿Qué dos verificaciones harías antes de aceptar el pedido?

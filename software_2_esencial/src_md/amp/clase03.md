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

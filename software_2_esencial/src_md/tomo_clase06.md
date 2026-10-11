@@H2 Clase 6 — El microprocesador
[[FICHA]]
Capacidad: Reconoce las principales características de los microprocesadores de computadoras.
Tema: Microprocesador: concepto, evolución, tipos, características y conexión.
- Explica la función del microprocesador como unidad central de proceso.
- Interpreta núcleos, hilos, frecuencia y caché al comparar procesadores.
- Describe los cuidados de la conexión del procesador al zócalo.
[[/FICHA]]
[[IMG T_image11.png|10.9]]
Figura 6.1 — Reconocimiento del microprocesador y su zócalo.
## Concepto
El microprocesador o CPU (unidad central de proceso) es el chip que ejecuta las instrucciones de los programas: busca cada instrucción en memoria, la decodifica, la ejecuta y guarda el resultado, millones de veces por segundo. Es el componente que más define el rendimiento general del equipo.
Seguí el ciclo de la CPU en el sentido de las flechas: busca la instrucción, la decodifica, la ejecuta y guarda el resultado, millones de veces por segundo. A la derecha, cómo seis núcleos manejan doce hilos.
[[IMG T_image12.png|10.6]]
Figura 6.2 — El ciclo de la CPU y la relación entre núcleos e hilos.
[[CAJA Concepto clave — Núcleo e hilo]]
Un núcleo es una unidad de proceso completa dentro del chip; un hilo es cada tarea que el sistema puede asignarle en simultáneo. Un procesador de 6 núcleos y 12 hilos atiende hasta doce tareas a la vez.
[[/CAJA]]
## Evolución
Desde los primeros microprocesadores de los años setenta, la industria multiplicó la cantidad de transistores por chip generación tras generación. El gran salto moderno fue pasar de aumentar solo la frecuencia a integrar varios núcleos en un mismo chip: hoy hasta los procesadores económicos traen varios núcleos que trabajan en paralelo.
[[CAJA Ejemplo — Comparar sin marketing]]
Para el aula del Instituto Ko'ẽju, Panambi compara dos procesadores de precio similar: uno de 4 núcleos a 3,6 GHz y otro de 6 núcleos a 3,2 GHz. Para el uso escolar (varias aplicaciones abiertas a la vez), recomienda el de 6 núcleos: el paralelismo pesa más que unas décimas de GHz.
[[/CAJA]]
## Tipos y características
Las dos familias dominantes en computadoras son Intel Core y AMD Ryzen (3, 5, 7, 9). En Intel conviven dos nomenclaturas: las generaciones anteriores se llamaban Core i3, i5, i7 e i9, y las actuales se llaman Core 3, 5 y 7 y Core Ultra 5, 7 y 9; en el mercado se venden ambas. Para compararlos se leen: núcleos (unidades de proceso completas), hilos (tareas simultáneas que manejan), frecuencia en GHz (velocidad de cada núcleo), caché (memoria interna ultrarrápida) y consumo (TDP, en watts), que determina el disipador necesario.
[[TABLA]]
Característica | Qué indica | Ejemplo de lectura
Núcleos / hilos | Tareas en paralelo | 6 núcleos / 12 hilos
Frecuencia | Velocidad por núcleo | 3,4 GHz (turbo 4,6 GHz)
Caché | Memoria interna rápida | 12 MB
TDP | Calor a disipar | 65 W
[[/TABLA]]
## Conexión
El procesador se monta en el zócalo de la placa con una orientación única marcada por un triángulo o muescas; nunca se fuerza. Entre el procesador y su disipador va una capa fina de pasta térmica que transfiere el calor. Un procesador sin disipador correctamente montado se sobrecalienta en segundos.
[[CAJA En Paraguay — Leer la publicación completa]]
En los portales de venta locales abundan títulos como 'PC gamer i7' sin aclarar la generación del procesador. Un i7 de hace diez años rinde menos que un i3 actual. El técnico paraguayo que sabe leer el modelo completo (familia, generación, sufijo) protege a su cliente de pagar de más por un nombre.
[[/CAJA]]
## Cómo leer el nombre de un procesador
El nombre comercial de un procesador se lee por partes. En «Intel Core i5-12400» el «i5» es la gama, el «12» indica la generación (duodécima) y «400» es el modelo dentro de esa generación; una letra al final agrega información: «F» indica que no trae video integrado y «K» que admite overclocking. En «AMD Ryzen 5 5600G», el «5» es la gama, el primer «5» del número es la serie y la «G» indica que tiene gráficos integrados. En la nomenclatura nueva de Intel («Core Ultra 5 225») la lógica es parecida: gama, serie y modelo.
Ese detalle de los gráficos integrados importa mucho en un aula. Un procesador con video integrado permite conectar el monitor a la placa sin comprar tarjeta de video; uno sin video integrado obliga a sumarla. Antes de cerrar el presupuesto, el técnico confirma también que el disipador incluido alcance para el TDP del procesador.
[[CAJA Ejemplo — ¿Hace falta tarjeta de video para la sala de profesores?]]
La sala de profesores del Instituto Ko'ẽju necesita una PC para documentos, planillas y videollamadas. Panambi tiene dos ofertas del mismo precio: un procesador de 6 núcleos sin video integrado (sufijo F) y otro de 6 núcleos con video integrado.
Paso 1. Uso previsto: ofimática y videollamadas; no hay edición de video ni juegos.
Paso 2. Con el modelo F hay que sumar una tarjeta de video de entrada: el costo total sube.
Paso 3. El modelo con video integrado cubre el uso, consume menos y deja libre la ranura PCIe x16.
Paso 4. Recomendación: el procesador con video integrado, con la justificación por escrito.
[[/CAJA]]
Para comparar dos modelos de forma objetiva, el técnico busca pruebas de rendimiento independientes del mismo tipo de uso (ofimática, compilación, edición) y mira el consumo: entre dos procesadores que rinden parecido, conviene el que consume menos.
[[CAJA Errores frecuentes — Al comparar procesadores]]
• Comparar solo los GHz entre procesadores de generaciones distintas.
• Leer «i7» o «Ryzen 7» sin mirar la generación: un modelo viejo de gama alta puede rendir menos que uno nuevo de gama media.
• Comprar un procesador sin video integrado para un equipo que no tiene tarjeta de video.
• Reutilizar la pasta térmica vieja al remontar el disipador: hay que limpiarla y aplicar una capa nueva y fina.
[[/CAJA]]
## Actividades de aplicación
Marcá la opción correcta:
1. La CPU ejecuta las instrucciones siguiendo el ciclo:
    a) Guardar, borrar, copiar
    b) Buscar, decodificar, ejecutar
    c) Encender, apagar, reiniciar
    d) Comprimir, enviar, recibir
2. Un procesador de 6 núcleos y 12 hilos puede atender en simultáneo hasta:
    a) 6 tareas
    b) 12 tareas
    c) 18 tareas
    d) 1 tarea
3. La memoria interna ultrarrápida del procesador se llama:
    a) RAM
    b) ROM
    c) Caché
    d) Virtual
4. La pasta térmica se coloca entre:
    a) El procesador y el zócalo
    b) El procesador y el disipador
    c) El disipador y el gabinete
    d) La placa y la fuente
Completá los espacios:
5. La sigla CPU significa unidad ________ de ________.
6. La velocidad de cada núcleo se mide en ________ (GHz).
7. El ________ indica cuántos watts de calor debe manejar el disipador.
Verdadero o falso (justificá las falsas):
8. (....) Más GHz siempre significa mejor rendimiento entre dos procesadores cualesquiera.
9. (....) El procesador se inserta en el zócalo con una orientación única.
10. (....) Un procesador puede funcionar de forma prolongada sin disipador.
Respondé y fundamentá:
11. ¿Por qué la industria pasó de subir la frecuencia a sumar núcleos? Explicalo con la idea de trabajo en paralelo.
12. Redactá la recomendación de procesador para un aula donde se usan planillas, documentos y navegación con varias pestañas. Justificá con dos características.

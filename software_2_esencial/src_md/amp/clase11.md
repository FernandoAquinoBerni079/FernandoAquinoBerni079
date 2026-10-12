## Compartir recursos con orden: permisos y servicios
Una red útil no es solo equipos conectados: es decidir qué se comparte, con quién y con qué permisos. En Windows, una carpeta compartida tiene permisos de lectura (ver y copiar) o de lectura y escritura (también modificar y borrar). Una impresora compartida se instala una vez en el equipo o servidor que la atiende, y los demás la agregan como impresora de red. La regla práctica es dar a cada usuario el permiso mínimo que necesita: el estudiante lee la carpeta de materiales y solo escribe en la de entregas.
La elección entre pares y cliente-servidor se decide por tres preguntas: cuántos equipos hay, qué tan importantes son los datos y quién va a administrar. Con pocos equipos y sin datos críticos, entre pares alcanza. Cuando hay más equipos, datos que respaldar o muchos usuarios, conviene un servidor: los permisos y las copias se manejan en un solo lugar.
[[CAJA Ejemplo — La red de la sala de profesores]]
La sala de profesores del Instituto Ko'ẽju tiene 4 computadoras y una impresora USB conectada a una de ellas. Los docentes quieren imprimir desde cualquier equipo y compartir las planillas de notas.
Paso 1. Tamaño: 4 equipos y un solo grupo de usuarios: una red entre pares es suficiente.
Paso 2. Impresora: se comparte desde la PC a la que está conectada; esa PC debe quedar encendida para que los demás impriman.
Paso 3. Planillas: se crea una carpeta compartida «Notas» con lectura y escritura solo para los docentes, y una copia semanal en un disco externo.
Paso 4. Límite del diseño: si la PC de la impresora se apaga o se rompe, nadie imprime. Por eso, a mediano plazo, Panambi propone una impresora de red.
[[/CAJA]]
En toda red, por chica que sea, conviene llevar un inventario: nombre de cada equipo, quién lo usa, qué recursos comparte y con qué permisos. Ese registro es el que permite a otro técnico continuar el trabajo, que es justamente lo que se espera de un profesional.
[[CAJA Errores frecuentes — Al armar una red chica]]
• Compartir carpetas con permiso total para «Todos»: cualquiera puede borrar el trabajo ajeno.
• Depender de una PC que se apaga para compartir la impresora de todo el grupo.
• No respaldar la carpeta compartida porque «está en la red».
• Confundir red local con internet: los equipos de la LAN se comunican aunque falle la conexión externa.
[[/CAJA]]

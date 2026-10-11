@@H2 Clase 16 — Materiales de red
[[FICHA]]
Capacidad: Identifica equipos y materiales para una red
Tema: Materiales de red: concepto, características, tipos, aplicación y generalidades.
- Identifica los materiales pasivos de una instalación de red.
- Explica la función del patch panel y de las rosetas en la instalación.
- Elabora la lista de materiales de una red local pequeña.
[[/FICHA]]
[[IMG T_image31.jpg|13.2]]
Figura 16.1 — Terminación de conductores en un patch panel. Dennis van Zuijlekom / CC BY-SA 2.0, vía Wikimedia Commons.
## Activos y pasivos
En una instalación se distinguen los componentes activos (los equipos con electrónica: switch, router, access point) de los pasivos: cables, conectores, rosetas, canaletas, patch panel y rack. Los pasivos no procesan nada, pero de su calidad y prolijidad depende que la red funcione estable durante años.
[[CAJA Concepto clave — Cableado fijo y cordones]]
La instalación se divide en cableado fijo (de la roseta al patch panel, oculto en canaletas, pensado para durar años) y cordones de conexión (patch cords reemplazables en los extremos). Se interviene sobre los cordones; el fijo no se toca.
[[/CAJA]]
## Cables y conectores
El material protagonista es el cable UTP, que se compra en cajas de 305 metros y se corta a medida. En sus extremos van los conectores RJ-45 (para armar cables) o se remata en jacks hembra (para rosetas y patch panel). Los patch cords son cables cortos ya armados de fábrica que unen la roseta con el equipo y el patch panel con el switch.
[[CAJA Ejemplo — La lista de materiales del aula]]
Para el aula del Instituto Ko'ẽju, Panambi lista los pasivos: una caja de cable UTP, 12 rosetas con sus jacks, un patch panel de 16 bocas, 24 patch cords para los 12 puntos (uno en el puesto y uno en el rack) y 1 patch cord adicional para enlazar switch y router: 25 en total. El cordón entre la ONT y el router se considera parte de la instalación del proveedor o se presupuesta por separado. Se suman canaletas, un rack de pared y etiquetas.
[[/CAJA]]
## Rosetas, canaletas y patch panel
La roseta es la caja de pared donde el usuario conecta su equipo: el punto de red. Las canaletas y bandejas protegen y ordenan el recorrido de los cables. El patch panel es la regleta del rack donde rematan todos los cables de las rosetas: cada boca del panel se une al switch con un patch cord, de modo que los cambios se hacen moviendo cordones, nunca tocando el cableado fijo.
Seguí el camino de la señal por los componentes pasivos: del equipo al patch panel del rack pasando por la roseta y el cableado horizontal fijo. Los patch cords se mueven; el tendido fijo no se toca.
[[IMG T_image32.png|16.0]]
Figura 16.2 — Recorrido de la señal por los materiales pasivos de la red.
[[TABLA]]
Material | Función | Se cotiza por
Cable UTP en caja | El medio del cableado fijo | Caja de 305 m
Conector RJ-45 | Terminar cables armados | Unidad / bolsa
Roseta + jack | Punto de red del usuario | Unidad por puesto
Patch panel | Rematar el cableado en el rack | Bocas (16, 24, 48)
Patch cord | Unir roseta-equipo y panel-switch | Unidad por punta
Canaleta | Proteger y ordenar recorridos | Metro lineal
Rack | Alojar panel y equipos | Unidades de altura (U)
[[/TABLA]]
## El rack y el orden
El rack o gabinete de comunicaciones aloja patch panel, switch, router y ONT en un solo lugar ventilado y cerrado. El orden se completa con organizadores de cable, precintos reutilizables y etiquetado en ambos extremos de cada cable: en una red bien etiquetada, cualquier técnico ubica una falla en minutos.
[[CAJA En Paraguay — El calor también cuenta]]
En los veranos del país, un rack cerrado sin ventilación puede superar temperaturas que degradan los equipos. Los instaladores locales lo saben: rack con ventilación (o ventilador propio), lejos de la pared que da al oeste, y canaletas que no corran pegadas a cables de energía, para evitar calor e interferencias a la vez.
[[/CAJA]]
## Cómo se calcula la lista de materiales
La lista de materiales (en inglés, BOM) se arma a partir del plano. Se cuentan los puntos de red y, para cada uno, se suman: una roseta con su jack, una boca de patch panel, un patch cord en el puesto y otro en el rack. Al total de patch cords se agregan los enlaces entre equipos del rack (switch con router, por ejemplo). El cable se calcula sumando la longitud de cada tendido, más un 10 % por curvas y desperdicio y un sobrante en cada extremo para rematar.
El patch panel y el switch se eligen por cantidad de bocas con reserva, y el rack por su altura en unidades (U): se suman las U del patch panel, el switch, el router, un organizador de cables y una bandeja, y se deja espacio libre para ventilar y crecer.
[[CAJA Ejemplo — Los materiales de la biblioteca]]
La biblioteca del Instituto Ko'ẽju lleva 6 puntos de red. Los tendidos medidos en el plano son de 12, 15, 18, 21, 24 y 27 metros.
Paso 1. Rosetas y jacks: 6. Bocas de patch panel necesarias: 6; se elige uno de 12 bocas para tener reserva.
Paso 2. Patch cords: 6 puntos × 2 + 1 enlace switch–router = 13.
Paso 3. Cable: 12 + 15 + 18 + 21 + 24 + 27 = 117 m; con 10 % de margen, unos 129 m. Una caja de 305 m alcanza y sobra cable para futuras ampliaciones.
Paso 4. Rack: patch panel (1 U) + switch (1 U) + router en bandeja (2 U) + organizador (1 U) = 5 U; se elige un rack mural de 9 U.
[[/CAJA]]
[[CAJA Errores frecuentes — Con los materiales]]
• Contar un solo patch cord por punto y olvidar el del rack.
• Comprar cable justo, sin margen para curvas y remates.
• Pasar el cable de red pegado al cable de energía en la misma canaleta.
• Armar cables a mano para el cableado fijo en lugar de rematar en jacks y patch panel.
[[/CAJA]]
## Actividades de aplicación
Marcá la opción correcta:
1. Los componentes pasivos de una red son:
    a) Switch y router
    b) Cables, rosetas, canaletas, patch panel y rack
    c) Los servidores
    d) Los protocolos
2. El patch panel sirve para:
    a) Dar Wi-Fi
    b) Rematar el cableado fijo en el rack y ordenar las conexiones
    c) Reemplazar al switch
    d) Filtrar el tráfico
3. El punto de red donde el usuario conecta su equipo es:
    a) El patch cord
    b) La roseta
    c) El rack
    d) La canaleta
4. Ante un cambio de puesto, lo correcto es:
    a) Recablear el tendido fijo
    b) Mover patch cords en el panel
    c) Cortar la canaleta
    d) Cambiar el switch
Completá los espacios:
5. El cable UTP se comercializa en cajas de ________ metros.
6. Los cables cortos armados de fábrica que unen roseta y equipo se llaman patch ________.
7. El gabinete que aloja panel, switch y router se llama ________.
Verdadero o falso (justificá las falsas):
8. (....) La calidad de los materiales pasivos no influye en la estabilidad de la red.
9. (....) El etiquetado en ambos extremos de cada cable acelera la localización de fallas.
10. (....) El cableado fijo se diseña para modificarse todas las semanas.
Respondé y fundamentá:
11. ¿Por qué conviene rematar el cableado en rosetas y patch panel en vez de armar un cable largo directo del switch a cada PC?
12. Elaborá la lista de materiales pasivos para una oficina de 4 puestos con impresora de red, con cantidades.

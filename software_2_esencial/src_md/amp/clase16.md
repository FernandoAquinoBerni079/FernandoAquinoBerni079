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

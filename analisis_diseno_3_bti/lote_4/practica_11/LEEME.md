# Práctica 11 — comprobación reproducible (lote 4 v1.1)

La Práctica 11 se hace en una **copia de práctica** de la base del equipo: otra carpeta, instalada con
`php instalar.php`. No se cambia la base Arapoty de la clase, ni su validación ni su esquema. Las etiquetas de Mbokaja
(MB- y tres cifras) se escriben con la correspondencia fija del libro (MB-201 → EJ-0201), porque el sistema entregado
valida EJ- y cuatro cifras. El nivel 3 (rol de voluntario) se resuelve en papel.

Este script es para el docente y para la auditoría: comprueba que la secuencia del nivel 2 da los mensajes y las
cantidades que espera la guía.

    php comprobar_practica_11.php                         # con la referencia docente
    php comprobar_practica_11.php ../ruta/a/la/copia      # con la base de un equipo que ya construyó OA-01 a OA-03

Trabaja sobre una base temporal propia, con los datos ficticios de ejemplo: no toca ninguna base instalada.
`secuencia.json` se genera desde `caso/mbokaja_u4.py` (PASOS_P11, CONSULTAS_P11) con `build/reproducir.py`.

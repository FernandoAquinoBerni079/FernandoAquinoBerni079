# Cargador del conjunto de prueba DP

    php cargar_dp.php --sistema=<carpeta de tu base> --destino=<carpeta nueva> [--clave=XXXX]

- Copia el código de tu base (sin `datos/`) a una carpeta nueva y crea ahí una base con los datos de `dp.json`.
- La base de la clase y la carpeta de origen no cambian.
- Si la carpeta de destino ya existe, se niega y no cambia nada.
- Al terminar dice «Estado esperado: correcto» y una huella de los datos: con los mismos datos, la huella es la misma
  en cualquier computadora y con cualquier base del curso.
- La parte manual de DP (`manual` en `dp.json`; Tabla 14.4 del libro) no la carga el cargador: la cargás vos con tus
  operaciones, porque eso también se prueba.
- `--datos=<archivo>` carga otro conjunto con el mismo formato (lo usa el docente con el conjunto reservado).

# Pruebas pendientes del entorno — protocolo de campo

**Estado del entorno:** PHP + SQLite es una **alternativa provisional**. Las pruebas automáticas corrieron solo en Ubuntu 24.04 con PHP 8.3.6 y SQLite 3.45.1, que no es el entorno de la escuela. Hasta completar este protocolo y registrar sus resultados, no se declara definitivo ni se fija para el libro.

## 1. Qué falta probar

| N.º | Prueba | Por qué importa | Estado |
|---|---|---|---|
| 1 | Windows 10 u 11 con el PHP portátil oficial (zip) | Es el caso más probable en los laboratorios; `pdo_sqlite` viene desactivado en el `php.ini` de ejemplo | Pendiente |
| 2 | Windows con XAMPP ya instalado (usando solo su `php.exe`) | Muchos laboratorios ya lo tienen | Pendiente |
| 3 | Al menos dos equipos del laboratorio destino, con su usuario de estudiante | Permisos de carpeta, perfiles restringidos y equipos lentos | Pendiente |
| 4 | PHP 7.4, 8.0, 8.1 y 8.2 | El código evita funciones exclusivas de PHP 8, pero solo se ejecutó en 8.3 | Pendiente |
| 5 | Antivirus y políticas de equipos administrados | Pueden bloquear `php.exe` o el puerto 8000 | Pendiente |
| 6 | Proyecto en un pendrive y en una carpeta de red | SQLite desaconseja la base sobre carpetas de red; retirar el pendrive con el servidor abierto puede dañarla | Pendiente: recomendar disco local |
| 7 | Concurrencia en Windows | `PHP_CLI_SERVER_WORKERS` no existe en Windows: `php -S` atiende de a un pedido. Las pruebas simultáneas de Linux no se trasladan. | Pendiente: probar `prueba_carrera.php` |
| 8 | Respaldo y restauración en Windows | Windows no deja borrar archivos abiertos: hay que confirmar que `--reiniciar` funciona con el servidor detenido | Pendiente |

## 2. Procedimiento en cada equipo (aprox. 30 minutos)

1. Copiar la carpeta `prototipo_v2_1/` a un disco local, por ejemplo `C:\biblioteca`.
2. Ejecutar `php verificar_entorno.php` y anotar la salida completa.
3. Ejecutar `php instalar.php` y anotar la clave que muestra.
4. Ejecutar `php pruebas/prueba_reglas.php`, `php pruebas/prueba_garantias.php`, `php pruebas/prueba_respaldo.php` y `php pruebas/prueba_carrera.php`, y anotar la línea «Resultado» de cada una.
5. Ejecutar `php -S localhost:8000 -t public` y abrir el navegador. Hacer a mano:
   - consultar el catálogo sin sesión;
   - ingresar;
   - prestar;
   - intentar prestar el mismo ejemplar;
   - devolver;
   - salir.
6. Detener el servidor y ejecutar `php respaldar.php` y `php instalar.php --reiniciar`, escribiendo REINICIAR. Comprobar que quedó el respaldo en `datos/respaldos/`.
7. Si algo falla, copiar el mensaje exacto.

## 3. Acta por equipo

| Dato | Equipo 1 | Equipo 2 |
|---|---|---|
| Fecha y responsable | | |
| Sistema operativo y versión | | |
| Instalación de PHP (zip oficial, XAMPP, otra) y versión | | |
| Versión de SQLite (de `verificar_entorno.php`) | | |
| `verificar_entorno.php`: ¿todo BIEN? | | |
| Resultado de las cuatro pruebas PHP | | |
| Recorrido manual del paso 5: ¿completo? | | |
| Respaldo y reinicio del paso 6: ¿correctos? | | |
| Bloqueos de antivirus o políticas | | |
| Observaciones | | |

## 4. Criterio para fijar el entorno

Se propone fijar PHP + SQLite para el libro si se cumplen las tres condiciones:
- al menos dos equipos del laboratorio destino, uno con Windows, completan el procedimiento sin cambios en el código;
- los ajustes de instalación que hagan falta caben en una ficha de una página;
- Fernando lo aprueba.

**Si no se cumplen,** Work (§7.5) admite otro entorno que la institución domine, siempre que produzca evidencias equivalentes: las mismas reglas, pruebas y entregables.

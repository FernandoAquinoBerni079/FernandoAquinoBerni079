# Piloto B — Prueba técnica mínima: PHP + SQLite en ejecución local

**Proyecto:** Biblioteca Comercial 2026 — Análisis y Diseño de Sistemas, 3.º BTI (Plan Optativo).
**Fase:** 2, pilotos.
**Estado:** candidato para la auditoría de ChatGPT. No es una decisión cerrada sobre el entorno del libro.

## 1. Qué se quería saber

Observación 6 de la auditoría: validar el entorno antes de fijarlo para todo el libro.

La prueba responde tres preguntas:
1. ¿Alcanzan PHP y SQLite, sin servidor de base de datos ni Apache, para el núcleo del prototipo integrador (catálogo, préstamo, devolución)?
2. ¿Qué hay que instalar y qué puede fallar en una computadora de laboratorio?
3. ¿Dónde están los límites del entorno, para separar el núcleo obligatorio de las ampliaciones (observación 2)?

## 2. Qué se construyó

Un prototipo deliberadamente chico, en `prototipo/`:

| Archivo | Líneas | Función |
|---|---|---|
| `src/db.php` | 105 | Conexión PDO, esquema de 3 tablas y las reglas de préstamo y devolución |
| `public/index.php` | 101 | Una sola página: catálogo con búsqueda, préstamo y devolución |
| `instalar.php` | 33 | Crea la base y carga datos de ejemplo |
| `verificar_entorno.php` | 25 | Diagnóstico de la máquina, para el docente |
| `pruebas/` | 3 archivos | Pruebas de reglas, de punta a punta por HTTP y de concurrencia |

Decisiones técnicas:
- **Sin librerías ni Composer.** Solo PHP y su extensión `pdo_sqlite`.
- **Seguridad básica:** sentencias preparadas en todas las consultas con datos del usuario, salida escapada con `htmlspecialchars`.
- **Integridad:** claves foráneas activadas en cada conexión (SQLite las trae apagadas) y una restricción CHECK.
- **Fecha local:** zona horaria `America/Asuncion` fijada en el código. Sin esto, PHP usa UTC cuando el `php.ini` no fija una zona, y un préstamo registrado de noche quedaría con la fecha del día siguiente.
- **Sin funciones exclusivas de PHP 8**, para que el código pueda correr en PHP 7.4. Esto no se probó (ver §5).

**Captura del prototipo en ejecución:** `resultados/captura_prototipo.png`.

## 3. Requisitos

| Componente | Mínimo | Recomendado | Nota |
|---|---|---|---|
| PHP (línea de comandos) | 7.4 | 8.1 o superior | Trae el servidor web incorporado (`php -S`) |
| Extensión `pdo_sqlite` | activa | — | Incluye el motor SQLite; no hay que instalar SQLite aparte |
| Navegador | cualquiera actual | — | — |
| Editor de texto | cualquiera | uno con resaltado de sintaxis | — |
| Disco | menos de 1 MB para el prototipo y su base | — | Sin contar la instalación de PHP |
| Red | no hace falta | — | Todo corre en `localhost` |

**No hacen falta:** Apache, MySQL ni MariaDB, XAMPP, Composer ni conexión a internet.

## 4. Instalación

### Linux (Ubuntu o derivados) — probado

```
sudo apt install php-cli php-sqlite3
php verificar_entorno.php
php instalar.php
php -S localhost:8000 -t public
```

### Windows — documentado, no probado en este entorno

**Opción 1. PHP portátil, el paquete «zip» oficial de windows.php.net.**
1. Descomprimir en una carpeta.
2. Copiar `php.ini-development` como `php.ini`.
3. Quitar el `;` de la línea `extension=pdo_sqlite`. Si PHP no encuentra la extensión, ajustar también `extension_dir`.
4. Puede requerir el redistribuible de Visual C++ que indica la página de descarga.

**Opción 2. XAMPP, si el laboratorio ya lo tiene instalado.**
- Se usa solo su `php.exe`. No hace falta iniciar Apache ni MySQL.
- Confirmar `pdo_sqlite` con `php verificar_entorno.php`.

En ambos casos, el paso 1 de cada máquina es correr `verificar_entorno.php`. Dice qué falta en lenguaje del estudiante.

## 5. Resultados

Entorno de la prueba: Ubuntu 24.04 (x86_64), PHP 8.3.6, SQLite 3.45.1. Salida completa en `resultados/salida_pruebas_linux.txt`.

| Prueba | Resultado |
|---|---|
| Reglas del núcleo (`prueba_reglas.php`) | **15 de 15 correctas** |
| De punta a punta por HTTP (`prueba_http.sh`) | **10 de 10 correctas** |
| Concurrencia (`prueba_concurrencia.php`) | Comportamiento esperado (ver abajo) |
| `php -l` en los 6 archivos PHP | Sin errores de sintaxis |

**Reglas del núcleo comprobadas:**
- disponibilidad calculada;
- préstamo válido;
- rechazo cuando no quedan ejemplares, sin dejar filas a medias;
- libro o lector inexistente;
- devolución y rechazo de la doble devolución;
- claves foráneas y CHECK activos en la base;
- tildes y ñ;
- zona horaria de Paraguay;
- base creada en una carpeta con espacios y tildes, como «Análisis y Diseño».

**Por HTTP:**
- catálogo visible;
- UTF-8 correcto;
- búsqueda por autor;
- préstamo, rechazo y devolución desde los formularios;
- formulario incompleto;
- texto con `<script>` escapado;
- comilla simple en la búsqueda sin romper la consulta;
- servidor sin avisos ni errores de PHP.

**Concurrencia.** Una conexión retiene la escritura y una segunda intenta escribir:
- sin espera, la segunda se rechaza al instante con «database is locked»;
- con 1 s de espera, se rechaza a los 1004 ms;
- cuando la primera libera, la segunda escribe sin problema.

Es el comportamiento documentado de SQLite: **un solo escritor a la vez**.

**Falla simulada: falta `pdo_sqlite`.** Se corrió PHP sin `php.ini` (`php -n`):
- `verificar_entorno.php` marca la falta y termina con código 1;
- `instalar.php` aborta con un error fatal poco legible para un estudiante.

Por eso el verificador va primero. En Linux sin ini falta todo PDO. En Windows, PDO viene incorporado y lo que suele faltar es solo el controlador (`pdo_sqlite`). En ese caso el mensaje esperable es otro («could not find driver»), pero tampoco es legible para un estudiante.

## 6. Limitaciones y lo que no se probó

1. **No se probó en Windows ni en las computadoras de un laboratorio escolar real.** El entorno de esta prueba es Linux. Antes de fijar el entorno hay que correr `verificar_entorno.php` y el prototipo en al menos dos máquinas del laboratorio destino. Lo ideal es una con XAMPP y otra con el PHP portátil.
2. **No se probó PHP 7.4 ni 8.0–8.2.** El código evita funciones exclusivas de PHP 8, pero solo se ejecutó en 8.3.
3. **El servidor `php -S` es para desarrollo.** El manual de PHP lo indica así. Atiende de a una petición por vez, sirve para que cada estudiante pruebe su copia y no sirve como servidor compartido del curso.
4. **SQLite admite un solo escritor a la vez.** Con un servidor y muchos usuarios simultáneos aparecen esperas y rechazos.
5. **La base no debe vivir en una carpeta de red compartida.** La documentación de SQLite desaconseja usar el archivo de la base sobre sistemas de archivos en red. En un pendrive funciona, pero retirarlo con el servidor abierto puede dañar la base.
6. **No se probaron antivirus ni políticas de seguridad de Windows.** Pueden bloquear `php.exe` o el puerto 8000 en máquinas administradas.
7. **El prototipo no tiene autenticación, permisos ni registro de usuarios.** Es a propósito: son ampliaciones (§7).

## 7. Consecuencia para el libro: núcleo y ampliaciones

| Núcleo obligatorio: alcanzable con este entorno | Ampliación avanzada: fuera del núcleo |
|---|---|
| Una base local por estudiante o por equipo | Servidor compartido con varios usuarios simultáneos |
| Altas y consultas del catálogo; préstamo y devolución con su regla de disponibilidad | Autenticación (inicio de sesión, contraseñas con `password_hash`) |
| Validación de datos y mensajes al usuario | Roles y permisos (bibliotecaria, estudiante, docente) |
| Sentencias preparadas y salida escapada como práctica mínima de seguridad | Concurrencia: bloqueos, reintentos, servidor de base de datos real |
| Pruebas de aceptación contra los requisitos | Despliegue en un hosting |

El núcleo entero (conexión, reglas, página e instalador) entra en 239 líneas de PHP. El peso del libro puede quedar en el análisis y el diseño. La programación es el último eslabón del proceso y se apoya en código que el libro da hecho y comentado (observación 1; ver el Piloto C).

## 8. Recomendación

- **Adoptar provisionalmente:** PHP 8.1 o superior en línea de comandos, `pdo_sqlite` y el servidor incorporado como entorno del núcleo.
- **Condición antes de fijarlo para todo el libro:** prueba de campo en el laboratorio destino con `verificar_entorno.php` y el prototipo, en al menos dos máquinas.
- **Si la prueba de campo falla por políticas del laboratorio:** la alternativa es una carpeta portátil con PHP ya configurado, preparada por el docente.
- **Contingencia:** las unidades de análisis y diseño no dependen del entorno. Si el laboratorio no está disponible, solo se ve afectada la parte de prototipo.

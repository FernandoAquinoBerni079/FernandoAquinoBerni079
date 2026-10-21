# Guía de instalación, configuración y ejecución

Versión del paquete: Entrega 1.0 (versión candidata v2 con SC-02, equipo modelo, caso Arapoty)

## Antes de empezar

- PHP 8.1 o superior con las extensiones pdo_sqlite y session (la guía de la base admite desde 7.4).
- Una carpeta en el disco local de la computadora, con permiso de escritura (no un pendrive ni una carpeta de red).
- Un navegador. No hace falta internet: el sistema funciona en la misma computadora.
- Para las pruebas automáticas por HTTP (opcionales): bash y curl.

El paso 2 muestra una sola vez las claves de las cuentas de demostración bibliotecaria1 y direccion1. Anotalas. Son de demostración: no se usan con datos reales sin cambiarlas.

## Pasos

### Paso 1. Comprobar el entorno

```
php verificar_entorno.php
```
Resultado esperado: «Esta computadora está lista para el prototipo.»
Si falla: Si una línea dice FALTA, corregí ese punto (por ejemplo, activar pdo_sqlite en php.ini) y repetí el paso.

### Paso 2. Crear la base con los datos de ejemplo

```
php instalar.php
```
Resultado esperado: «Base creada en:»
Si falla: Si dice que ya existe una base, no la borres: seguí con el paso 3 o usá php instalar.php --reiniciar, que pide confirmación y guarda antes un respaldo.

### Paso 3. Iniciar el sistema

```
php -S localhost:8000 -t public
```
Si falla: Dejá esa ventana abierta mientras usás el sistema. Si el puerto 8000 está ocupado, usá otro: localhost:8001.

### Paso 4. Abrir el sistema en el navegador

Abrí en el navegador: http://localhost:8000
Resultado esperado: «PT-01 Buscar un título»
Si falla: Si el navegador no encuentra la página, revisá que la ventana del paso 3 siga abierta.

### Paso 5. Detener el sistema

Detené el sistema.
Si falla: En la ventana del paso 3, Ctrl+C.

### Paso 6. Hacer un respaldo

```
php respaldar.php
```
Resultado esperado: «Respaldo guardado y verificado»
Si falla: Si dice que la base está en uso, detené el sistema (paso 5) y repetí.

### Paso 7. Comprobar que el respaldo se puede restaurar

```
php restaurar.php datos/respaldos/respaldo_AAAAMMDD_HHMMSS.sqlite
```
Cuando lo pida, escribí RESTAURAR y apretá Enter.
Resultado esperado: «Restauración terminada y comprobada»
Si falla: Usá el nombre del respaldo que mostró el paso 6. Si no escribís RESTAURAR, no se cambia nada.

## Límites

Leé ENTREGA/LIMITES.md antes de usar el sistema con datos que no sean de prueba.

<?php
// Comprueba si esta computadora puede ejecutar el prototipo. Uso: php verificar_entorno.php
// Pensado para correrlo en cada máquina del laboratorio antes de la primera clase práctica.
$ok = true;
function linea($bien, $texto)
{
    global $ok;
    if (!$bien) {
        $ok = false;
    }
    echo ($bien ? '[ BIEN ] ' : '[ FALTA ] ') . $texto . PHP_EOL;
}

linea(version_compare(PHP_VERSION, '7.4.0', '>='), 'Versión de PHP: ' . PHP_VERSION . ' (mínimo 7.4; recomendado 8.1 o superior)');
linea(extension_loaded('pdo_sqlite'), 'Extensión pdo_sqlite ' . (extension_loaded('pdo_sqlite') ? 'activa' : 'no activa: habilitar «extension=pdo_sqlite» en php.ini'));
if (extension_loaded('pdo_sqlite')) {
    $v = (new PDO('sqlite::memory:'))->query('SELECT sqlite_version()')->fetchColumn();
    linea(true, 'Versión de SQLite: ' . $v);
}
$dir = __DIR__ . '/datos';
linea(is_dir($dir) && is_writable($dir), 'Permiso de escritura en la carpeta datos/');
$ini = php_ini_loaded_file();
echo '[ INFO ] Archivo php.ini en uso: ' . ($ini ? $ini : 'ninguno (se usan los valores por defecto)') . PHP_EOL;
echo PHP_EOL . ($ok ? 'Esta computadora está lista para el prototipo.' : 'Corregí los puntos marcados con FALTA antes de usar el prototipo.') . PHP_EOL;
exit($ok ? 0 : 1);

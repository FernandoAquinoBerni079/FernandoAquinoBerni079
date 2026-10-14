<?php
// Copia consistente y verificada de la base, aunque el servidor esté funcionando. Uso: php respaldar.php
// Restaurar: detener el servidor y copiar el respaldo sobre datos/biblioteca.sqlite.
require __DIR__ . '/src/db.php';
require __DIR__ . '/src/respaldo.php';
$ruta = ruta_base();
if (!file_exists($ruta)) {
    fwrite(STDERR, "No hay base para respaldar.\n");
    exit(1);
}
$destino = dirname($ruta) . '/respaldos/respaldo_' . date('Ymd_His') . '.sqlite';
$error = respaldar_base(conectar(), $destino);
if ($error !== null) {
    fwrite(STDERR, $error . "\n");
    exit(1);
}
echo "Respaldo guardado y verificado en: $destino\n";

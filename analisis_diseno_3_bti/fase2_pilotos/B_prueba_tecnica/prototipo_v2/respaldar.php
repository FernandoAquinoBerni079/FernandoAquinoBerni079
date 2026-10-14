<?php
// Copia consistente de la base, aunque el servidor esté funcionando. Uso: php respaldar.php
// Restaurar: detener el servidor y copiar el respaldo sobre datos/biblioteca.sqlite.
require __DIR__ . '/src/db.php';
$ruta = ruta_base();
if (!file_exists($ruta)) {
    fwrite(STDERR, "No hay base para respaldar.\n");
    exit(1);
}
$dir = dirname($ruta) . '/respaldos';
if (!is_dir($dir)) {
    mkdir($dir, 0775, true);
}
$destino = $dir . '/respaldo_' . date('Ymd_His') . '.sqlite';
$pdo = conectar();
$st = $pdo->prepare('VACUUM INTO ?');   // requiere SQLite 3.27 o superior
$st->execute(array($destino));
echo "Respaldo guardado en: $destino\n";

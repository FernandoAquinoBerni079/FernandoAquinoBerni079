<?php
// Proceso auxiliar de prueba_marca_huerfana.php: simula un corte de energía matándose a sí mismo (SIGKILL)
// en un momento elegido, sin cerrar la base ni quitar la marca. Uso interno:
//   php _corte.php <base> diario   reinicio a medio hacer: tablas borradas y recreadas sin confirmar (diario caliente)
//   php _corte.php <base> wal      base en modo WAL con un préstamo confirmado que todavía no pasó al archivo principal
putenv('BIBLIO_DB=' . $argv[1]);
require __DIR__ . '/../src/db.php';
$modo = $argv[2];
$marca = ruta_marca_mantenimiento();
$fh = fopen($marca, 'x');
fwrite($fh, date('c') . ' ' . getmypid() . "\n");
fclose($fh);
$pdo = new PDO('sqlite:' . ruta_base());
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
if ($modo === 'diario') {
    $pdo->exec('PRAGMA cache_size = 2');   // obliga a SQLite a escribir páginas en el archivo antes de confirmar
    $pdo->exec('BEGIN EXCLUSIVE');
    $obj = $pdo->query("SELECT type, name FROM sqlite_master WHERE name NOT LIKE 'sqlite_%' AND type IN ('table', 'trigger', 'index')")->fetchAll(PDO::FETCH_ASSOC);
    foreach (array('trigger', 'index', 'table') as $tipo) {
        foreach ($obj as $o) {
            if ($o['type'] === $tipo) {
                $pdo->exec('DROP ' . strtoupper($tipo) . ' IF EXISTS "' . $o['name'] . '"');
            }
        }
    }
    crear_esquema($pdo);
    $pdo->exec('CREATE TABLE relleno (x TEXT)');
    $st = $pdo->prepare('INSERT INTO relleno VALUES (?)');
    for ($i = 0; $i < 400; $i++) {
        $st->execute(array(str_repeat('x', 500)));
    }
} else {
    $pdo->exec('PRAGMA journal_mode = WAL');
    $pdo->exec('PRAGMA wal_autocheckpoint = 0');
    $pdo->exec("INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (5, 3, '2026-03-03', '2026-03-10')");
}
echo "LISTO\n";
posix_kill(getmypid(), SIGKILL);

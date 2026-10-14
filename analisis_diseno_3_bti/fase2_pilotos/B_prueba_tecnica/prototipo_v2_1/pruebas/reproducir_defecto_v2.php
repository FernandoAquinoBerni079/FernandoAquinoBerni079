<?php
// Reproduce el defecto del instalador v2 (copy()) con lo confirmado aún en -wal.
// Uso: php pruebas/reproducir_defecto_v2.php <ruta a prototipo_v2>
$v2 = $argv[1];
$dir = sys_get_temp_dir() . '/repro_v2_' . getmypid(); @mkdir($dir);
$ruta = "$dir/biblioteca.sqlite"; putenv("BIBLIO_DB=$ruta");
exec(escapeshellarg(PHP_BINARY) . " $v2/instalar.php --clave=x 2>&1");
$o = new PDO("sqlite:$ruta"); $o->exec('PRAGMA journal_mode=WAL'); $o->exec('PRAGMA wal_autocheckpoint=0');
$o->exec("INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (1,1,'2026-03-02','2026-03-09'),(2,2,'2026-03-02','2026-03-09')");
echo "Préstamos confirmados antes de reiniciar: " . $o->query('SELECT COUNT(*) FROM prestamos')->fetchColumn() . PHP_EOL;
exec(escapeshellarg(PHP_BINARY) . " $v2/instalar.php --reiniciar --si --clave=x 2>&1");
$r = glob("$dir/respaldos/antes_de_reiniciar_*.sqlite")[0];
echo "Préstamos en el respaldo que dejó el instalador v2: " . (new PDO("sqlite:$r"))->query('SELECT COUNT(*) FROM prestamos')->fetchColumn() . PHP_EOL;
$o = null; exec('rm -rf ' . escapeshellarg($dir));

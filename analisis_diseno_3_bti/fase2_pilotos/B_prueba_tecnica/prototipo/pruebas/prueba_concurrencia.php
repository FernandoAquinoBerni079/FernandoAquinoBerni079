<?php
// Dos conexiones escriben a la vez sobre la misma base. Uso: php pruebas/prueba_concurrencia.php
// Muestra qué pasa cuando una escritura queda bloqueada por otra (límite conocido de SQLite).
$tmp = sys_get_temp_dir() . '/biblio_conc_' . getmypid() . '.sqlite';
@unlink($tmp);
$a = new PDO('sqlite:' . $tmp);
$a->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$a->exec('CREATE TABLE t (x INTEGER)');
$b = new PDO('sqlite:' . $tmp);
$b->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

foreach (array(0, 1) as $espera) {
    $b->setAttribute(PDO::ATTR_TIMEOUT, $espera);
    $a->exec('BEGIN IMMEDIATE');           // A toma el permiso de escritura y no lo suelta
    $a->exec('INSERT INTO t VALUES (1)');
    $ini = microtime(true);
    try {
        $b->exec('INSERT INTO t VALUES (2)');
        $res = 'B escribió';
    } catch (PDOException $e) {
        $res = 'B rechazado: ' . $e->getMessage();
    }
    $ms = round((microtime(true) - $ini) * 1000);
    $a->exec('COMMIT');
    echo "Espera configurada en B: {$espera} s -> {$res} (tardó {$ms} ms)" . PHP_EOL;
}
$b->exec('INSERT INTO t VALUES (3)');
echo 'Con A ya liberada, B escribe sin problema. Filas: ' . $a->query('SELECT COUNT(*) FROM t')->fetchColumn() . PHP_EOL;
@unlink($tmp);

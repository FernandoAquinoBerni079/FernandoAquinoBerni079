<?php
// Conexión y esquema de la base. Capa de persistencia (Capítulo 9, Figura 9.1).
// Adaptado del Piloto B v2.3: misma conexión, mismas garantías (claves foráneas, espera ante
// otra escritura, mantenimiento controlado); esquema nuevo con el diseño del lote 3 v1.1.

// Sin esta línea, PHP usa UTC si el php.ini no fija una zona y un préstamo
// registrado de noche quedaría con la fecha del día siguiente.
date_default_timezone_set('America/Asuncion');

require_once __DIR__ . '/mantenimiento.php';

// En el servidor web, una base en mantenimiento responde 503 en lugar de un error de PHP.
if (PHP_SAPI !== 'cli') {
    set_exception_handler(function ($e) {
        if ($e instanceof EnMantenimiento) {
            http_response_code(503);
            header('Retry-After: 60');
            echo '<!doctype html><meta charset="utf-8"><p id="mantenimiento">' . htmlspecialchars($e->getMessage()) . '</p>';
            return;
        }
        http_response_code(500);
        error_log('Error no previsto: ' . $e->getMessage());
        echo '<!doctype html><meta charset="utf-8"><p>Error interno.</p>';
    });
}

const VERSION_ESQUEMA = 3;

function ruta_base()
{
    $env = getenv('BIBLIO_DB');
    if ($env !== false && $env !== '') {
        return $env;
    }
    return __DIR__ . '/../datos/biblioteca.sqlite';
}

function conectar($cerrar = false)
{
    static $pdo = null;
    if ($cerrar) {
        $pdo = null;
        return null;
    }
    if ($pdo !== null) {
        return $pdo;
    }
    // Durante un mantenimiento (reinicio o restauración) no se abren conexiones nuevas.
    if (file_exists(ruta_base() . '.mantenimiento')) {
        throw new EnMantenimiento('La base está en mantenimiento. Intentá de nuevo en unos minutos.');
    }
    $pdo = new PDO('sqlite:' . ruta_base());
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
    // Espera hasta 5 s si otra conexión está escribiendo, en lugar de fallar enseguida.
    $pdo->setAttribute(PDO::ATTR_TIMEOUT, 5);
    // SQLite no controla claves foráneas si no se le pide en cada conexión.
    $pdo->exec('PRAGMA foreign_keys = ON');
    return $pdo;
}

function cerrar_conexion()
{
    conectar(true);
}

// Crea las tablas, el índice de RI-01 y los disparadores del historial (src/esquema.sql).
function crear_esquema(PDO $pdo)
{
    $sql = file_get_contents(__DIR__ . '/esquema.sql');
    foreach (preg_split('/^-- fin\s*$/m', $sql) as $s) {
        $s = trim(preg_replace('/^--.*$/m', '', $s));
        if ($s !== '') {
            $pdo->exec($s);
        }
    }
    $pdo->exec('PRAGMA user_version = ' . VERSION_ESQUEMA);
}

function fila(PDO $pdo, $sql, $params)
{
    $st = $pdo->prepare($sql);
    $st->execute($params);
    return $st->fetch();
}

// Valor vigente de un parámetro (plazo y máximos): las cifras de las reglas no van en el programa.
function parametro(PDO $pdo, $nombre)
{
    $f = fila($pdo, 'SELECT valor FROM parametros WHERE nombre = ?', array($nombre));
    if (!$f) {
        throw new RuntimeException("Falta el parámetro $nombre.");
    }
    return (int) $f['valor'];
}

function sumar_dias($fecha, $dias)
{
    $d = DateTime::createFromFormat('!Y-m-d', $fecha);
    if ($d === false || $d->format('Y-m-d') !== $fecha) {
        return null;
    }
    $d->modify('+' . (int) $dias . ' days');
    return $d->format('Y-m-d');
}

// 2026-03-09 → 09/03, como en los mensajes del Capítulo 8.
function fecha_visible($fecha)
{
    return substr($fecha, 8, 2) . '/' . substr($fecha, 5, 2);
}

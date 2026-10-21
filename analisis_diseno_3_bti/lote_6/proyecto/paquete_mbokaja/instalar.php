<?php
// Crea la base con datos ficticios. Uso:
//   php instalar.php                     crea la base si no existe; si existe, no toca nada
//   php instalar.php --reiniciar         respalda la base actual y la reinicia en el mismo archivo (pide confirmación);
//                                        se niega si otra conexión está usando la base (ver src/mantenimiento.php)
//   opciones: --si (no pide confirmación), --clave=XXXX (clave de demostración para las dos cuentas;
//             si no se da, se genera una al azar para cada una y se muestra una sola vez)
// Adaptado del Piloto B v2.3: misma protección (nunca borra una base existente sin respaldo verificado).
require __DIR__ . '/src/db.php';
require __DIR__ . '/src/respaldo.php';
require __DIR__ . '/src/datos_ejemplo.php';

$args = array_slice($argv, 1);
$reiniciar = in_array('--reiniciar', $args, true);
$sin_preguntar = in_array('--si', $args, true);
$clave = null;
foreach ($args as $a) {
    if (strpos($a, '--clave=') === 0) {
        $clave = substr($a, 8);
    }
}

$ruta = ruta_base();
if (file_exists($ruta) && filesize($ruta) > 0) {
    if (!$reiniciar) {
        fwrite(STDERR, "Ya existe una base en $ruta.\nNo se modificó nada. Para empezar de cero: php instalar.php --reiniciar\n(se hace solo sin conexiones activas y con un respaldo previo en datos/respaldos/).\n");
        exit(1);
    }
    if (!$sin_preguntar) {
        echo "Se va a reemplazar el contenido de la base por datos de ejemplo. Detené antes el servidor (Ctrl+C)\ny cerrá cualquier otro programa que tenga la base abierta.\nEscribí REINICIAR para confirmar: ";
        $resp = trim((string) fgets(STDIN));
        if ($resp !== 'REINICIAR') {
            fwrite(STDERR, "Cancelado. No se modificó nada.\n");
            exit(1);
        }
    }
    // Reinicio con mantenimiento controlado (src/mantenimiento.php): marca de mantenimiento,
    // bloqueo exclusivo, respaldo verificado y reinicio dentro del mismo archivo.
    $copia = dirname($ruta) . '/respaldos/antes_de_reiniciar_' . date('Ymd_His') . '.sqlite';
    $error = reiniciar_con_mantenimiento($copia, function ($pdo) use ($clave, &$resumen) {
        $resumen = sembrar_ejemplo($pdo, $clave);
    });
    if ($error !== null) {
        fwrite(STDERR, $error . "\n");
        exit(1);
    }
    echo "Respaldo verificado en: $copia\n";
    if (!empty($GLOBALS['mantenimiento_salio_de_wal'])) {
        echo "La base estaba en modo WAL y quedó en modo DELETE, el predeterminado del prototipo.\n";
    }
    informar($ruta, $resumen);
    exit(0);
}

$pdo = conectar();
$pdo->exec('BEGIN');
crear_esquema($pdo);
$resumen = sembrar_ejemplo($pdo, $clave);
$pdo->exec('COMMIT');
informar($ruta, $resumen);

function informar($ruta, $r)
{
    echo "Base creada en: " . realpath($ruta) . "\n";
    echo "Obras: {$r[0]} · Ejemplares: {$r[1]} (uno inactivo) · Lectores: {$r[2]} (uno inactivo)\n";
    foreach ($r[3] as $usuario => $clave) {
        echo "Cuenta de demostración «{$usuario}»" . ($clave !== null ? ", clave «{$clave}» (anotala: no se vuelve a mostrar; cambiala antes de usar datos reales)" : '') . "\n";
    }
}

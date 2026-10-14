<?php
// Crea la base con datos ficticios. Uso:
//   php instalar.php                     crea la base si no existe; si existe, no toca nada
//   php instalar.php --reiniciar         respalda la base actual y la vuelve a crear (pide confirmación)
//   opciones: --si (no pide confirmación), --clave=XXXX (clave de la cuenta «bibliotecaria»)
require __DIR__ . '/src/db.php';
require __DIR__ . '/src/respaldo.php';

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
        fwrite(STDERR, "Ya existe una base en $ruta.\nNo se modificó nada. Para empezar de cero: php instalar.php --reiniciar\n(antes de borrar se guarda un respaldo en datos/respaldos/).\n");
        exit(1);
    }
    if (!$sin_preguntar) {
        echo "Se va a reemplazar la base actual por datos de ejemplo. Detené antes el servidor (Ctrl+C).\nEscribí REINICIAR para confirmar: ";
        $resp = trim((string) fgets(STDIN));
        if ($resp !== 'REINICIAR') {
            fwrite(STDERR, "Cancelado. No se modificó nada.\n");
            exit(1);
        }
    }
    // Respaldo consistente y verificado ANTES de borrar nada (mismo procedimiento que respaldar.php).
    $copia = dirname($ruta) . '/respaldos/antes_de_reiniciar_' . date('Ymd_His') . '.sqlite';
    $error = respaldar_base(conectar(), $copia);
    if ($error !== null) {
        fwrite(STDERR, $error . "\nNo se modificó nada.\n");
        exit(1);
    }
    echo "Respaldo verificado en: $copia\n";
    cerrar_conexion();
    // Se borra la base y sus archivos auxiliares de SQLite, para no mezclar restos con la base nueva.
    foreach (array('', '-wal', '-shm', '-journal') as $suf) {
        if (file_exists($ruta . $suf) && !unlink($ruta . $suf)) {
            fwrite(STDERR, "No se pudo borrar $ruta$suf. El respaldo quedó en $copia.\n");
            exit(1);
        }
    }
}

$pdo = conectar();
$pdo->exec('BEGIN');
crear_esquema($pdo);

// Datos ficticios. Las obras son títulos reales de dominio público o de uso común como dato
// bibliográfico; los lectores, códigos y fechas son inventados.
$obras = array(
    array('Cuentos de la selva', 'Horacio Quiroga', 'Edición escolar 2019', 3),
    array('El hombre que calculaba', 'Malba Tahan', 'Edición 2015', 2),
    array('Platero y yo', 'Juan Ramón Jiménez', 'Edición 2018', 1),
    array('Manual de primeros auxilios escolares', 'Equipo editorial (ficticio)', '1.ª edición', 1),
);
$n = 0;
foreach ($obras as $o) {
    $st = $pdo->prepare('INSERT INTO obras (titulo, autor, edicion) VALUES (?, ?, ?)');
    $st->execute(array($o[0], $o[1], $o[2]));
    $obra_id = $pdo->lastInsertId();
    for ($i = 0; $i < $o[3]; $i++) {
        $n++;
        $st = $pdo->prepare('INSERT INTO ejemplares (obra_id, codigo) VALUES (?, ?)');
        $st->execute(array($obra_id, sprintf('EJ-%04d', $n)));
    }
}
$lectores = array(
    array('L-001', 'Rocío Giménez', '3.º BTI', 1),
    array('L-002', 'Tobías Acosta', '1.º BC', 1),
    array('L-003', 'Prof. Nilda Cáceres', 'Docente', 1),
    array('L-004', 'Gael Sanabria', '2.º BTI', 0),
);
foreach ($lectores as $l) {
    $st = $pdo->prepare('INSERT INTO lectores (codigo, nombre, curso, activo) VALUES (?, ?, ?, ?)');
    $st->execute($l);
}
$mostrar = false;
if ($clave === null || $clave === '') {
    $clave = substr(bin2hex(random_bytes(6)), 0, 10);
    $mostrar = true;
}
$st = $pdo->prepare("INSERT INTO usuarios (usuario, clave_hash, rol) VALUES ('bibliotecaria', ?, 'bibliotecaria')");
$st->execute(array(password_hash($clave, PASSWORD_DEFAULT)));
$pdo->exec('COMMIT');

echo "Base creada en: " . realpath($ruta) . "\n";
echo "Obras: " . count($obras) . " · Ejemplares: $n · Lectores: " . count($lectores) . " (uno inactivo)\n";
echo "Cuenta de operación: usuario «bibliotecaria»" . ($mostrar ? ", clave «$clave» (anotala: no se vuelve a mostrar)" : '') . "\n";

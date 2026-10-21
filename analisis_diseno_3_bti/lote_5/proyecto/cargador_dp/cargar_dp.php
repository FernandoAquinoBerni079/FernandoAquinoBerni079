<?php
// Cargador del conjunto de prueba DP (Unidad V). Crea una COPIA DESCARTABLE del sistema en una carpeta nueva, con una
// base propia cargada con los datos de dp.json, y comprueba que quedó el estado esperado. No toca la base de la clase
// ni la carpeta de origen: copia solo el código (sin datos/) y crea la base en la carpeta nueva.
// Uso: php cargar_dp.php --sistema=<carpeta del sistema> --destino=<carpeta nueva> [--clave=XXXX] [--datos=<archivo>]
//   --sistema   la base de tu equipo o la referencia docente (se copia; no se modifica)
//   --destino   una carpeta que NO exista: si ya existe, el cargador se niega y no cambia nada
//   --clave     clave de las cuentas de demostración bibliotecaria1 y direccion1 (si no se da, una al azar)
//   --datos     otro conjunto con el mismo formato que dp.json (por ejemplo, el reservado DR del docente,
//               que no se publica); si no se da, se carga dp.json
// Al terminar, la copia funciona como cualquier instalación: cd <destino> y php -S localhost:8000 -t public
$op = array();
foreach (array_slice($argv, 1) as $a) {
    if (preg_match('/^--(sistema|destino|clave|datos)=(.*)$/', $a, $m)) {
        $op[$m[1]] = $m[2];
    }
}
function salir($texto)
{
    fwrite(STDERR, $texto . PHP_EOL . 'No se cambió nada.' . PHP_EOL);
    exit(1);
}
if (empty($op['sistema']) || empty($op['destino'])) {
    salir('Uso: php cargar_dp.php --sistema=<carpeta del sistema> --destino=<carpeta nueva> [--clave=XXXX]');
}
$origen = realpath($op['sistema']);
if (!$origen || !is_file($origen . '/src/db.php') || !is_file($origen . '/src/esquema.sql')) {
    salir('La carpeta del sistema no es una base de proyecto (falta src/db.php o src/esquema.sql).');
}
$destino = rtrim($op['destino'], '/\\');
if (file_exists($destino)) {
    salir("Ya existe $destino. El cargador solo crea copias nuevas: elegí otra carpeta o borrala vos, si es descartable.");
}
if (strpos(realpath(dirname($destino)) . '/', $origen . '/') === 0) {
    salir('La copia no puede ir dentro de la carpeta del sistema que se copia.');
}

$archivo = isset($op['datos']) ? $op['datos'] : __DIR__ . '/dp.json';
$dp = json_decode((string) @file_get_contents($archivo), true);
if (!$dp || !isset($dp['esperado'])) {
    salir("El archivo de datos $archivo no tiene el formato de dp.json.");
}

// 1. Copia del código, sin la carpeta de datos (la base de origen no se lee ni se copia).
function copiar($de, $a)
{
    mkdir($a, 0777, true);
    foreach (scandir($de) as $f) {
        if ($f === '.' || $f === '..' || $f === 'datos') {
            continue;
        }
        is_dir("$de/$f") ? copiar("$de/$f", "$a/$f") : copy("$de/$f", "$a/$f");
    }
}
copiar($origen, $destino);
mkdir("$destino/datos/respaldos", 0777, true);
$ruta = "$destino/datos/biblioteca.sqlite";
putenv('BIBLIO_DB=' . $ruta);
require "$destino/src/db.php";

// 2. Esquema y datos de dp.json, en una sola transacción.
$pdo = conectar();
$pdo->exec('BEGIN');
crear_esquema($pdo);
$ins = function ($sql, $fila) use ($pdo) {
    $pdo->prepare($sql)->execute($fila);
};
$id = function ($tabla, $codigo) use ($pdo) {
    $st = $pdo->prepare("SELECT id FROM $tabla WHERE codigo = ?");
    $st->execute(array($codigo));
    return $st->fetchColumn();
};
foreach ($dp['parametros'] as $p) {
    $ins('INSERT INTO parametros (nombre, valor) VALUES (?, ?)', $p);
}
foreach ($dp['obras'] as $o) {
    $ins('INSERT INTO obras (codigo, titulo, autor) VALUES (?, ?, ?)', $o);
}
foreach ($dp['ediciones'] as $d) {
    $ins('INSERT INTO ediciones (codigo, obra_id, editorial_anio) VALUES (?, ?, ?)', array($d[0], $id('obras', $d[1]), $d[2]));
}
foreach ($dp['ejemplares'] as $e) {
    $ins('INSERT INTO ejemplares (codigo, edicion_id, activo) VALUES (?, ?, 1)', array($e[0], $id('ediciones', $e[1])));
}
foreach ($dp['lectores'] as $l) {
    $ins('INSERT INTO lectores (codigo, nombre, tipo, curso, activo) VALUES (?, ?, ?, ?, ?)', $l);
}
foreach ($dp['prestamos'] as $p) {
    $ins('INSERT INTO prestamos (ejemplar_id, lector_id, curso_al_prestar, fecha_salida, fecha_vencimiento,
        fecha_devolucion) VALUES (?, ?, ?, ?, ?, ?)', array($id('ejemplares', $p[0]), $id('lectores', $p[1]),
        $p[2], $p[3], $p[4], $p[5]));
}
foreach ($dp['ejemplares'] as $e) {   // la baja va después del historial, como pasaría en la biblioteca
    if (!$e[2]) {
        $ins('UPDATE ejemplares SET activo = 0 WHERE codigo = ?', array($e[0]));
    }
}
$claves = array();
foreach (array('bibliotecaria1' => 'bibliotecaria', 'direccion1' => 'direccion') as $usuario => $rol) {
    $c = isset($op['clave']) && $op['clave'] !== '' ? $op['clave'] : substr(bin2hex(random_bytes(6)), 0, 10);
    $ins('INSERT INTO cuentas (usuario, clave_hash, rol) VALUES (?, ?, ?)', array($usuario, password_hash($c, PASSWORD_DEFAULT), $rol));
    $claves[$usuario] = isset($op['clave']) ? null : $c;
}
$pdo->exec('COMMIT');

// 3. Estado esperado (dp.json → esperado) y huella reproducible de los datos (sin las cuentas, que llevan sal).
$n = function ($sql) use ($pdo) {
    return (int) $pdo->query($sql)->fetchColumn();
};
$es = $dp['esperado'];
$fallas = array();
foreach (array('obras', 'ediciones', 'ejemplares', 'lectores', 'prestamos') as $t) {
    if ($n("SELECT COUNT(*) FROM $t") !== $es[$t]) {
        $fallas[] = "cantidad de $t";
    }
}
if ($n('SELECT COUNT(*) FROM prestamos WHERE fecha_devolucion IS NULL') !== $es['prestamos_activos']) {
    $fallas[] = 'préstamos activos';
}
foreach ($es['activos_por_lector'] as $le => $k) {
    if ($n("SELECT COUNT(*) FROM prestamos p JOIN lectores l ON l.id = p.lector_id
        WHERE l.codigo = '$le' AND p.fecha_devolucion IS NULL") !== $k) {
        $fallas[] = "préstamos activos de $le";
    }
}
foreach ($es['ejemplares_y_disponibles_por_obra'] as $ob => $v) {
    $ej = $n("SELECT COUNT(*) FROM ejemplares e JOIN ediciones d ON d.id = e.edicion_id JOIN obras o ON o.id = d.obra_id
        WHERE o.codigo = '$ob' AND e.activo = 1");
    $di = $ej - $n("SELECT COUNT(*) FROM prestamos p JOIN ejemplares e ON e.id = p.ejemplar_id JOIN ediciones d
        ON d.id = e.edicion_id JOIN obras o ON o.id = d.obra_id WHERE o.codigo = '$ob' AND e.activo = 1
        AND p.fecha_devolucion IS NULL");
    if (array($ej, $di) !== $v) {
        $fallas[] = "ejemplares o disponibles de $ob";
    }
}
$volcado = '';
foreach (array('parametros' => 'nombre', 'obras' => 'codigo', 'ediciones' => 'codigo', 'ejemplares' => 'codigo',
    'lectores' => 'codigo', 'prestamos' => 'id') as $t => $orden) {
    $volcado .= json_encode($pdo->query("SELECT * FROM $t ORDER BY $orden")->fetchAll(PDO::FETCH_ASSOC)) . "\n";
}
$huella = hash('sha256', $volcado);
cerrar_conexion();
file_put_contents("$destino/COPIA_DESCARTABLE_DP.txt", 'Copia descartable con el conjunto ' . $dp['conjunto'] . ".\n"
    . 'Creada: ' . date('Y-m-d H:i') . "\nSistema copiado: $origen\nHuella de los datos: $huella\n"
    . "No es la base de la clase. Se puede borrar cuando termine la prueba.\n");
echo "Copia descartable creada en: $destino\n";
foreach ($claves as $u => $c) {
    echo "Cuenta de demostración «{$u}»" . ($c !== null ? ", clave «{$c}» (se muestra una sola vez)" : '') . "\n";
}
echo 'Estado esperado: ' . ($fallas ? 'FALLA (' . implode(', ', $fallas) . ')' : 'correcto') . "\n";
echo "Huella de los datos: $huella\n";
exit($fallas ? 1 : 0);

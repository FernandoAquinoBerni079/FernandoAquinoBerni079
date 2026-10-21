<?php
// Utilidades de las pruebas automáticas. Cada prueba trabaja sobre una base temporal propia con los datos
// ficticios de src/datos_ejemplo.php: nunca toca datos/biblioteca.sqlite.
function comprobar($desc, $cond)
{
    global $fallos, $n;
    $n++;
    if (!$cond) {
        $fallos++;
    }
    echo ($cond ? 'CORRECTO ' : 'FALLA    ') . $desc . PHP_EOL;
}

function terminar_prueba()
{
    global $fallos, $n;
    echo PHP_EOL . 'Resultado: ' . ($n - $fallos) . " de $n correctas" . PHP_EOL;
    exit($fallos ? 1 : 0);
}

// Prepara una base temporal con el esquema y los datos de ejemplo, y la deja en BIBLIO_DB.
function base_de_prueba($nombre)
{
    $dir = sys_get_temp_dir() . '/biblio_l4_' . $nombre . '_' . getmypid();
    exec('rm -rf ' . escapeshellarg($dir));
    mkdir($dir);
    $ruta = $dir . '/biblioteca.sqlite';
    putenv('BIBLIO_DB=' . $ruta);
    return array($dir, $ruta);
}

function contar(PDO $pdo, $sql, $params = array())
{
    $st = $pdo->prepare($sql);
    $st->execute($params);
    return (int) $st->fetchColumn();
}

// Huella de todas las tablas: sirve para comprobar que una operación rechazada no cambió ningún dato.
function huella(PDO $pdo)
{
    $h = '';
    foreach (array('parametros', 'obras', 'ediciones', 'ejemplares', 'lectores', 'cuentas', 'prestamos') as $t) {
        $h .= $t . json_encode($pdo->query('SELECT * FROM "' . $t . '" ORDER BY 1')->fetchAll(PDO::FETCH_NUM));
    }
    return hash('sha256', $h);
}

// Cuentas de prueba, como las deja la sesión después de ingresar.
function cuenta($rol)
{
    return array('id' => $rol === 'bibliotecaria' ? 1 : 2, 'usuario' => $rol . '1', 'rol' => $rol);
}

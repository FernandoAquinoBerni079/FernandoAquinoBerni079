<?php
// Ejecuta la matriz de pruebas del equipo modelo (lote_5/caso/verificacion.py → casos.json) sobre una COPIA
// DESCARTABLE creada con cargar_dp.php. Cada caso llama a la operación del sistema copiado con la cuenta indicada y
// compara el código del mensaje y el control (consulta del estado, texto o filas). Los casos «HTTP» se registran
// como no ejecutados acá: los corre build/reproducir.py con su script.
// Uso: php ejecutar_matriz.php <carpeta de la copia> <casos.json> [esperados_alternativos.json]  → JSON por la salida
$copia = realpath($argv[1]);
if (!$copia || !is_file("$copia/COPIA_DESCARTABLE_DP.txt")) {
    fwrite(STDERR, "Solo se ejecuta sobre una copia descartable creada con cargar_dp.php.\n");
    exit(1);
}
putenv("BIBLIO_DB=$copia/datos/biblioteca.sqlite");
require "$copia/src/db.php";
require "$copia/src/mensajes.php";
require "$copia/src/auth.php";
require "$copia/src/reglas.php";
$casos = json_decode(file_get_contents($argv[2]), true);
$alt = isset($argv[3]) ? json_decode(file_get_contents($argv[3]), true) : array();
$pdo = conectar();
$cuentas = array('bibliotecaria' => array('id' => 1, 'usuario' => 'bibliotecaria1', 'rol' => 'bibliotecaria'),
    'direccion' => array('id' => 2, 'usuario' => 'direccion1', 'rol' => 'direccion'));
$fn = array('OP-01' => 'registrar_prestamo', 'OP-02' => 'registrar_devolucion', 'OP-03' => 'consultar_disponibilidad',
    'OP-04' => 'listar_prestamos_activos', 'OP-05' => 'informe_mensual', 'OA-01' => 'alta_ejemplar',
    'OA-03' => 'alta_lector');
function huella_datos(PDO $pdo)
{
    $s = '';
    foreach (array('obras', 'ediciones', 'ejemplares', 'lectores', 'prestamos') as $t) {
        $s .= json_encode($pdo->query("SELECT * FROM $t ORDER BY id")->fetchAll(PDO::FETCH_ASSOC));
    }
    return md5($s);
}
$salida = array();
foreach ($casos as $c) {
    if ($c['operacion'] === 'HTTP') {
        $salida[] = array('id' => $c['id'], 'ejecutado' => false);
        continue;
    }
    $esperado = array_key_exists($c['id'], $alt) ? $alt[$c['id']] : $c['esperado_codigo'];
    $cuenta = $c['cuenta'] ? $cuentas[$c['cuenta']] : null;
    $args = $c['operacion'] === 'OP-03' ? array_merge(array($pdo), $c['entradas'])
        : array_merge(array($pdo, $cuenta), $c['entradas']);
    $antes = huella_datos($pdo);
    $r = call_user_func_array($fn[$c['operacion']], $args);
    $ok = $r['codigo'] === $esperado;
    $obs = array('codigo' => $r['codigo'], 'texto' => $r['texto']);
    if (!$r['ok'] && huella_datos($pdo) !== $antes) {   // un rechazo no puede cambiar datos
        $ok = false;
        $obs['cambio_datos'] = true;
    }
    $k = $c['control'];
    if ($k) {
        if (isset($k['sql'])) {
            $v = (int) $pdo->query($k['sql'])->fetchColumn();
            $obs['sql'] = $v;
            $ok = $ok && $v === $k['valor'];
        }
        if (isset($k['texto'])) {
            $ok = $ok && strpos($r['texto'], $k['texto']) !== false;
        }
        $filas = isset($r['filas']) ? $r['filas'] : array();
        if (isset($k['filas_cuenta'])) {
            $obs['filas_cuenta'] = count($filas);
            $ok = $ok && count($filas) === $k['filas_cuenta'];
        }
        if (isset($k['filas'])) {
            foreach ($k['filas'] as $par) {
                list($donde, $debe) = $par;
                $f = array_values(array_filter($filas, function ($f) use ($donde) {
                    foreach ($donde as $campo => $v) {
                        if (!isset($f[$campo]) || (string) $f[$campo] !== (string) $v) {
                            return false;
                        }
                    }
                    return true;
                }));
                $bien = count($f) === 1;
                foreach ($debe as $campo => $v) {
                    $bien = $bien && (string) $f[0][$campo] === (string) $v;
                }
                $obs['filas'][] = $f ? $f[0] : null;
                $ok = $ok && $bien;
            }
        }
        if (isset($k['sin_campos'])) {
            foreach ($filas as $f) {
                $ok = $ok && !array_intersect(array_keys($f), $k['sin_campos']);
            }
            $obs['campos'] = $filas ? array_keys($filas[0]) : array();
        }
        if (isset($k['total'])) {
            $obs['total'] = $r['total'];
            $ok = $ok && $r['total'] === $k['total'];
        }
    }
    $salida[] = array('id' => $c['id'], 'ejecutado' => true, 'esperado_codigo' => $esperado, 'correcto' => $ok, 'obtenido' => $obs);
}
cerrar_conexion();
echo json_encode($salida, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT) . "\n";

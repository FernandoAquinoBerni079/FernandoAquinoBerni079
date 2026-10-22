<?php
// Pruebas de integración del Capítulo 15 sobre una COPIA DESCARTABLE creada con cargar_dp.php:
//   permisos: cada operación (OP-01 a OP-06, OA-01 a OA-05) con las tres cuentas, contra la Tabla 11.3;
//             cada rechazo es ME-13 y no cambia datos;
//   persistencia: «escribir» registra un préstamo; «leer», en otro proceso, comprueba que sigue (como al reiniciar).
// Uso: php integracion.php <copia> permisos | escribir | leer
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
$pdo = conectar();
$n = 0; $bien = 0;
function chk($desc, $cond)
{
    global $n, $bien;
    $n++;
    $bien += $cond ? 1 : 0;
    echo ($cond ? 'CORRECTO ' : 'FALLA    ') . $desc . PHP_EOL;
}
function huella(PDO $pdo)
{
    $s = '';
    foreach (array('obras', 'ediciones', 'ejemplares', 'lectores', 'prestamos') as $t) {
        $s .= json_encode($pdo->query("SELECT * FROM $t ORDER BY id")->fetchAll(PDO::FETCH_ASSOC));
    }
    return md5($s);
}
$modo = $argv[2];
if ($modo === 'permisos') {
    $c = array('sin sesión' => null, 'bibliotecaria' => array('id' => 1, 'usuario' => 'bibliotecaria1', 'rol' => 'bibliotecaria'),
        'dirección' => array('id' => 2, 'usuario' => 'direccion1', 'rol' => 'direccion'));
    // operación → [roles permitidos, llamada]. Las entradas son válidas para DP; con permiso, la operación sigue.
    $ops = array(
        'OP-01' => array(array('bibliotecaria'), function ($cu) use ($pdo) { return registrar_prestamo($pdo, $cu, 'LE-1005', 'EJ-1008', '2026-05-12'); }),
        'OP-02' => array(array('bibliotecaria'), function ($cu) use ($pdo) { return registrar_devolucion($pdo, $cu, 'EJ-1003', '2026-05-12'); }),
        'OP-04' => array(array('bibliotecaria'), function ($cu) use ($pdo) { return listar_prestamos_activos($pdo, $cu, '2026-05-12'); }),
        'OP-05' => array(array('bibliotecaria', 'dirección'), function ($cu) use ($pdo) { return informe_mensual($pdo, $cu, '2026-05'); }),
        'OP-06' => array(array('bibliotecaria'), function ($cu) use ($pdo) { return inactivar($pdo, $cu, 'lector', 'LE-1004'); }),
        'OA-01' => array(array('bibliotecaria'), function ($cu) use ($pdo) { return alta_ejemplar($pdo, $cu, 'EJ-1099', 'ED-1001'); }),
        'OA-02' => array(array('bibliotecaria'), function ($cu) use ($pdo) { return alta_obra_edicion($pdo, $cu, 'OB-1099', 'Obra de permisos (ficticia)', 'Autor (ficticio)', 'ED-1099', ''); }),
        'OA-03' => array(array('bibliotecaria'), function ($cu) use ($pdo) { return alta_lector($pdo, $cu, 'LE-1099', 'Lector de permisos (ficticio)', 'docente', ''); }),
        'OA-04' => array(array('bibliotecaria'), function ($cu) use ($pdo) { return editar_lector($pdo, $cu, 'LE-1001', 'Lector de prueba 1 (ficticio)', '1.º BTI'); }),
        'OA-05' => array(array('bibliotecaria'), function ($cu) use ($pdo) { return editar_obra($pdo, $cu, 'OB-1002', 'Huerta escolar paso a paso', 'Autor de prueba (ficticio)'); }),
    );
    foreach ($ops as $op => $d) {
        foreach (array('sin sesión', 'dirección', 'bibliotecaria') as $quien) {   // los rechazos primero, sin cambios
            $antes = huella($pdo);
            $r = call_user_func($d[1], $c[$quien]);
            if (in_array($quien, $d[0], true)) {
                chk("$op con $quien: permitida (no ME-13)", $r['codigo'] !== 'ME-13');
            } else {
                chk("$op con $quien: ME-13 y ningún dato cambia", $r['codigo'] === 'ME-13' && huella($pdo) === $antes);
            }
        }
    }
    $r = consultar_disponibilidad($pdo, 'río');
    chk('OP-03 sin sesión: permitida (pública), sin datos de lectores', $r['ok'] && !array_intersect(array_keys($r['filas'][0]), array('lector', 'nombre', 'curso')));
    chk('Ninguna operación usó ME-12 (solo el ingreso)', strpos(file_get_contents("$copia/src/reglas.php"), "'ME-12'") === false);
} elseif ($modo === 'escribir') {
    $r = registrar_prestamo($pdo, array('id' => 1, 'usuario' => 'bibliotecaria1', 'rol' => 'bibliotecaria'), 'LE-1005', 'EJ-1008', '2026-05-12');
    chk('Persistencia, 1.º proceso: préstamo de EJ-1008 a LE-1005 registrado (ME-04)', $r['codigo'] === 'ME-04');
} elseif ($modo === 'leer') {
    $v = $pdo->query("SELECT COUNT(*) FROM prestamos p JOIN ejemplares e ON e.id = p.ejemplar_id
        WHERE e.codigo = 'EJ-1008' AND p.fecha_devolucion IS NULL")->fetchColumn();
    chk('Persistencia, 2.º proceso (otra conexión, como al reiniciar): el préstamo de EJ-1008 sigue', (int) $v === 1);
}
cerrar_conexion();
echo PHP_EOL . "Resultado: $bien de $n correctas" . PHP_EOL;
exit($bien === $n ? 0 : 1);

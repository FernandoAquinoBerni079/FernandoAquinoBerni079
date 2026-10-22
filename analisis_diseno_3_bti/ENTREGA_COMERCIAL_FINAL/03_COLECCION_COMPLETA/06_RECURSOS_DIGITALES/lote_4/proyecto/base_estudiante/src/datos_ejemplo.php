<?php
// Datos ficticios iniciales (caso Arapoty, lote 3). Ninguna persona es real: los lectores se nombran
// con un código y una descripción. Las cuentas son de demostración y su clave se elige al instalar.
const DATOS_EJEMPLO = array(
    'parametros' => array(array('plazo_dias', 7), array('maximo_estudiante', 2), array('maximo_docente', 5)),
    // código, título, autor
    'obras' => array(
        array('OB-0031', 'Cuentos del arroyo Arapoty', 'Autora del caso (ficticia)'),
        array('OB-0032', 'El arroyo y la escuela', 'Autor del caso (ficticio)'),
        array('OB-0040', 'Atlas escolar', 'Equipo editorial del caso (ficticio)'),
    ),
    // código, obra, editorial y año
    'ediciones' => array(
        array('ED-0045', 'OB-0031', 'Editorial del caso, 2019'),
        array('ED-0052', 'OB-0031', 'Otra editorial, 2023'),
        array('ED-0060', 'OB-0032', 'Editorial del caso, 2021'),
        array('ED-0070', 'OB-0040', 'Editorial del caso, 2018'),
    ),
    // código, edición, activo (EJ-0459 está inactivo, como en la Figura 7.2)
    'ejemplares' => array(
        array('EJ-0457', 'ED-0045', 1), array('EJ-0458', 'ED-0045', 1), array('EJ-0459', 'ED-0045', 0),
        array('EJ-0512', 'ED-0052', 1), array('EJ-0601', 'ED-0060', 1), array('EJ-0701', 'ED-0070', 1),
    ),
    // código, nombre, tipo, curso, activo
    'lectores' => array(
        array('LE-0123', 'Estudiante A (ficticio)', 'estudiante', '2.º BTI', 1),
        array('LE-0124', 'Estudiante B (ficticio)', 'estudiante', '7.º grado', 1),
        array('LE-0125', 'Estudiante C (ficticio, egresado)', 'estudiante', '3.º BTI', 0),
        array('LE-0201', 'Docente D (ficticio)', 'docente', null, 1),
    ),
);

// Carga los datos de ejemplo y las dos cuentas de demostración. Si no se da una clave, se genera una
// al azar para cada cuenta y se devuelve para mostrarla una sola vez.
function sembrar_ejemplo(PDO $pdo, $clave = null)
{
    $id = array();
    foreach (DATOS_EJEMPLO['parametros'] as $p) {
        $pdo->prepare('INSERT INTO parametros (nombre, valor) VALUES (?, ?)')->execute($p);
    }
    foreach (DATOS_EJEMPLO['obras'] as $o) {
        $pdo->prepare('INSERT INTO obras (codigo, titulo, autor) VALUES (?, ?, ?)')->execute($o);
        $id[$o[0]] = $pdo->lastInsertId();
    }
    foreach (DATOS_EJEMPLO['ediciones'] as $d) {
        $pdo->prepare('INSERT INTO ediciones (codigo, obra_id, editorial_anio) VALUES (?, ?, ?)')->execute(array($d[0], $id[$d[1]], $d[2]));
        $id[$d[0]] = $pdo->lastInsertId();
    }
    foreach (DATOS_EJEMPLO['ejemplares'] as $e) {
        $pdo->prepare('INSERT INTO ejemplares (codigo, edicion_id, activo) VALUES (?, ?, ?)')->execute(array($e[0], $id[$e[1]], $e[2]));
    }
    foreach (DATOS_EJEMPLO['lectores'] as $l) {
        $pdo->prepare('INSERT INTO lectores (codigo, nombre, tipo, curso, activo) VALUES (?, ?, ?, ?, ?)')->execute($l);
    }
    $claves = array();
    foreach (array('bibliotecaria1' => 'bibliotecaria', 'direccion1' => 'direccion') as $usuario => $rol) {
        $c = ($clave === null || $clave === '') ? substr(bin2hex(random_bytes(6)), 0, 10) : $clave;
        $pdo->prepare('INSERT INTO cuentas (usuario, clave_hash, rol) VALUES (?, ?, ?)')->execute(array($usuario, password_hash($c, PASSWORD_DEFAULT), $rol));
        $claves[$usuario] = ($clave === null || $clave === '') ? $c : null;
    }
    return array(count(DATOS_EJEMPLO['obras']), count(DATOS_EJEMPLO['ejemplares']), count(DATOS_EJEMPLO['lectores']), $claves);
}

<?php
// Pruebas de las operaciones que construye el equipo (Capítulos 10 a 13). Uso: php pruebas/prueba_mis_operaciones.php
// Una operación que todavía responde PENDIENTE se informa como PENDIENTE y no cuenta como falla.
// Cuando la construyas, sus pruebas pasan a contar: tienen que dar CORRECTO.
// La misma prueba corre sobre la referencia docente, donde todas las operaciones están hechas.
require __DIR__ . '/_comun.php';
list($dir, $ruta) = base_de_prueba('mis_operaciones');
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/mensajes.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/../src/reglas.php';
require __DIR__ . '/../src/datos_ejemplo.php';
$fallos = 0;
$n = 0;
$pendientes = 0;
$pdo = conectar();
$pdo->exec('BEGIN');
crear_esquema($pdo);
sembrar_ejemplo($pdo, 'prueba-solo-local');
$pdo->exec('COMMIT');
$bib = cuenta('bibliotecaria');
$dir_ = cuenta('direccion');

// Ejecuta la operación y compara el código del mensaje. Si la operación está pendiente, no la evalúa.
function caso($prueba, $desc, $f, $esperado)
{
    global $pdo, $pendientes;
    $antes = huella($pdo);
    $r = $f();
    if ($r['codigo'] === 'PENDIENTE') {
        $pendientes++;
        echo "PENDIENTE $prueba: $desc ({$r['texto']})" . PHP_EOL;
        return;
    }
    $sin_cambios = $r['ok'] || huella($pdo) === $antes;
    comprobar("$prueba: $desc → $esperado" . ($r['ok'] ? '' : ' y sin cambios'), $r['codigo'] === $esperado && $sin_cambios);
}

caso('PA-01', 'alta de EJ-0800 en ED-0060', function () use ($pdo, $bib) { return alta_ejemplar($pdo, $bib, 'EJ-0800', 'ED-0060'); }, 'MA-01');
caso('PA-01', 'el mismo código otra vez', function () use ($pdo, $bib) { return alta_ejemplar($pdo, $bib, 'EJ-0800', 'ED-0060'); }, 'MA-02');
caso('PA-01', 'formato inválido', function () use ($pdo, $bib) { return alta_ejemplar($pdo, $bib, 'EJ-80', 'ED-0060'); }, 'MV-02');
caso('PA-01', 'edición inexistente', function () use ($pdo, $bib) { return alta_ejemplar($pdo, $bib, 'EJ-0801', 'ED-9999'); }, 'MA-03');
caso('PA-01', 'con la cuenta de dirección', function () use ($pdo, $dir_) { return alta_ejemplar($pdo, $dir_, 'EJ-0801', 'ED-0060'); }, 'ME-13');
caso('PA-05', 'corregir el título de OB-0032 sin autor', function () use ($pdo, $bib) { return editar_obra($pdo, $bib, 'OB-0032', 'El arroyo y la escuela', ''); }, 'MV-01');
caso('PA-03', 'estudiante sin curso (RI-06)', function () use ($pdo, $bib) { return alta_lector($pdo, $bib, 'LE-0300', 'Estudiante E', 'estudiante', ''); }, 'MV-03');
caso('P-10', 'inactivar el ejemplar EJ-0701', function () use ($pdo, $bib) { return inactivar($pdo, $bib, 'ejemplar', 'EJ-0701'); }, 'MA-08');
caso('P-01', 'préstamo válido de EJ-0457 a LE-0123', function () use ($pdo, $bib) { return registrar_prestamo($pdo, $bib, 'LE-0123', 'EJ-0457', '2026-03-05'); }, 'ME-04');
caso('P-07', 'segunda solicitud sobre EJ-0457', function () use ($pdo, $bib) { return registrar_prestamo($pdo, $bib, 'LE-0124', 'EJ-0457', '2026-03-05'); }, 'ME-03');
caso('P-05', 'préstamo a un lector inactivo', function () use ($pdo, $bib) { return registrar_prestamo($pdo, $bib, 'LE-0125', 'EJ-0458', '2026-03-05'); }, 'ME-01');
caso('P-11', 'préstamo con la cuenta de dirección', function () use ($pdo, $dir_) { return registrar_prestamo($pdo, $dir_, 'LE-0124', 'EJ-0458', '2026-03-05'); }, 'ME-13');
caso('P-03', 'devolución de EJ-0457', function () use ($pdo, $bib) { return registrar_devolucion($pdo, $bib, 'EJ-0457', '2026-03-09'); }, 'ME-07');
caso('OP-02', 'segunda devolución de EJ-0457', function () use ($pdo, $bib) { return registrar_devolucion($pdo, $bib, 'EJ-0457', '2026-03-10'); }, 'ME-06');
caso('OP-03', 'consulta sin coincidencias', function () use ($pdo) { return consultar_disponibilidad($pdo, 'zzz'); }, 'ME-08');
caso('OP-04', 'préstamos activos con la cuenta de dirección', function () use ($pdo, $dir_) { return listar_prestamos_activos($pdo, $dir_, '2026-03-20'); }, 'ME-13');
caso('OP-05', 'informe sin sesión', function () use ($pdo) { return informe_mensual($pdo, null, '2026-03'); }, 'ME-13');

cerrar_conexion();
exec('rm -rf ' . escapeshellarg($dir));
echo PHP_EOL . "Pendientes: $pendientes (no cuentan como falla)" . PHP_EOL;
terminar_prueba();

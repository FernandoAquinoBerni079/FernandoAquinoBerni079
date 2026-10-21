<?php
// Plantilla común de las pantallas: encabezado, menú según el rol y estado de carga (ME-11).
function cabecera($titulo, $codigo_pantalla)
{
    $c = cuenta_actual();
    echo '<!doctype html><html lang="es"><head><meta charset="utf-8">'
        . '<meta name="viewport" content="width=device-width, initial-scale=1">'
        . '<title>' . e($titulo) . '</title><style>'
        . 'body{font-family:sans-serif;max-width:56rem;margin:1rem auto;padding:0 1rem;font-size:1.05rem}'
        . 'label{display:block;margin:.4rem 0}input,select,button{font-size:1rem;padding:.25rem}'
        . ':focus{outline:3px solid #b8860b;outline-offset:2px}'
        . 'table{border-collapse:collapse;width:100%;margin:.5rem 0 1rem}th,td{border:1px solid #bbb;padding:.3rem .5rem;text-align:left}'
        . '.ok{color:#1b5e20}.error{color:#b71c1c}nav{margin-bottom:1rem}'
        . '</style></head><body>';
    echo '<nav><a href="index.php">Consulta pública</a> · ';
    if ($c && $c['rol'] === 'bibliotecaria') {
        echo '<a href="inicio.php">Inicio</a> · ';
    }
    if ($c) {
        // En la base del estudiante, PT-09 aparece en el menú cuando se construye (Capítulo 13).
        echo (is_file(__DIR__ . '/informe.php') ? '<a href="informe.php">Informe mensual</a> · ' : '')
            . 'Sesión: ' . e($c['usuario']) . ' · <a href="salir.php">Salir</a>';
    } else {
        echo '<a href="login.php">Ingreso del personal</a>';
    }
    echo '</nav><h1>' . e($codigo_pantalla . ' ' . $titulo) . '</h1>';
}

// Muestra el resultado de una operación: qué pasó, por qué y qué hacer (regla de 8.3), con su código.
function aviso($r)
{
    if ($r && $r['texto'] !== '') {
        echo '<p class="' . ($r['ok'] ? 'ok' : 'error') . '" id="' . ($r['ok'] ? 'mensaje' : 'error') . '" data-codigo="' . e($r['codigo']) . '">' . e($r['texto']) . '</p>';
    }
}

// Formulario con ficha CSRF. Al enviarlo, el botón se desactiva y muestra «Guardando…» (ME-11).
function formulario_inicio($accion = '')
{
    echo '<form method="post" onsubmit="var b=this.querySelector(\'button\');b.disabled=true;b.textContent=\'Guardando…\'">'
        . '<input type="hidden" name="csrf" value="' . e(ficha_csrf()) . '">'
        . ($accion !== '' ? '<input type="hidden" name="accion" value="' . e($accion) . '">' : '');
}

// Patrón POST-redirección-GET: el resultado se guarda en la sesión y se muestra una sola vez.
function guardar_aviso($r, $destino)
{
    $_SESSION['aviso'] = $r;
    header('Location: ' . $destino, true, 303);
    exit;
}

function tomar_aviso()
{
    $a = isset($_SESSION['aviso']) ? $_SESSION['aviso'] : null;
    unset($_SESSION['aviso']);
    return $a;
}

function pie()
{
    echo '</body></html>';
}

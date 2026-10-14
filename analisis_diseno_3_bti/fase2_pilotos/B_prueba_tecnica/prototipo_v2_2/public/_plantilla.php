<?php
function cabecera($titulo)
{
    $u = usuario_actual();
    echo '<!doctype html><html lang="es"><head><meta charset="utf-8">'
        . '<meta name="viewport" content="width=device-width, initial-scale=1">'
        . '<title>' . e($titulo) . '</title><style>'
        . 'body{font-family:sans-serif;max-width:56rem;margin:1rem auto;padding:0 1rem}'
        . 'table{border-collapse:collapse;width:100%;margin:.5rem 0 1rem}th,td{border:1px solid #bbb;padding:.3rem .5rem;text-align:left}'
        . '.ok{color:#1b5e20}.error{color:#b71c1c}nav{margin-bottom:1rem}'
        . '</style></head><body>';
    echo '<nav><a href="index.php">Catálogo</a> · ';
    if ($u) {
        echo '<a href="operaciones.php">Operaciones</a> · Sesión: ' . e($u['usuario']) . ' · <a href="salir.php">Salir</a>';
    } else {
        echo '<a href="login.php">Ingresar (bibliotecaria)</a>';
    }
    echo '</nav><h1>' . e($titulo) . '</h1>';
}

function pie()
{
    echo '</body></html>';
}

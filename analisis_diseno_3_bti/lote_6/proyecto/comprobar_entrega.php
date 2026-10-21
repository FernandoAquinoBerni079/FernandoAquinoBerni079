<?php
// Comprueba que un paquete de entrega sea coherente (Capítulo 17).
// Uso, desde la carpeta del paquete: php comprobar_entrega.php
// No cambia nada: lee los archivos y corre las pruebas de la lista, que usan bases temporales.
// A: cada comando «php ...» de la guía nombra un archivo que existe.
// B: cada archivo de la lista de entrega existe.
// C: cada prueba de la lista termina bien y da su línea «Resultado:».
// D: cada recurso de public/ que no es código tiene su fila en la ficha de procedencia.
// E: cada mensaje y cada pantalla que nombra el manual existen.
// F: la versión es la misma en todos los documentos que la declaran.
$raiz = __DIR__;
$faltas = array();
function leer_doc($ruta)
{
    return is_file($ruta) ? file_get_contents($ruta) : '';
}
function falta($bloque, $texto)
{
    global $faltas;
    $faltas[] = "INCOHERENCIA [$bloque] $texto";
}

$guia = leer_doc("$raiz/ENTREGA/INSTALAR.md");
$lista = leer_doc("$raiz/ENTREGA/LISTA_ENTREGA.md");
$manual = leer_doc("$raiz/ENTREGA/MANUAL.md");
$procedencia = leer_doc("$raiz/ENTREGA/PROCEDENCIA.md");
foreach (array('INSTALAR.md' => $guia, 'LISTA_ENTREGA.md' => $lista, 'MANUAL.md' => $manual,
               'PROCEDENCIA.md' => $procedencia) as $nombre => $texto) {
    if ($texto === '') {
        falta('B', "falta el documento ENTREGA/$nombre");
    }
}

// A. Comandos de la guía (dentro de los bloques ```).
preg_match_all('/```\n(.*?)```/s', $guia, $bloques);
foreach ($bloques[1] as $bloque) {
    foreach (explode("\n", trim($bloque)) as $linea) {
        if (preg_match('/^php\s+(?:-S\s+\S+\s+-t\s+(\S+)|(\S+\.php))/', trim($linea), $m)) {
            $ruta = isset($m[2]) && $m[2] !== '' ? $m[2] : $m[1];
            if (!file_exists("$raiz/$ruta")) {
                falta('A', "la guía usa «" . trim($linea) . "», pero no existe $ruta");
            }
        }
    }
}

// B y C. Archivos y pruebas de la lista de entrega.
preg_match_all('/^- archivo: `([^`]+)`/m', $lista, $archivos);
foreach ($archivos[1] as $ruta) {
    if (!file_exists("$raiz/$ruta")) {
        falta('B', "la lista de entrega incluye $ruta, que no está en el paquete");
    }
}
preg_match_all('/^- prueba: `([^`]+)`/m', $lista, $pruebas);
foreach ($pruebas[1] as $comando) {
    exec('cd ' . escapeshellarg($raiz) . ' && ' . $comando . ' 2>&1', $salida, $codigo);
    $ultima = trim((string) end($salida));
    $bien = $codigo === 0 && strpos($ultima, 'Resultado:') === 0;
    echo ($bien ? 'PRUEBA BIEN  ' : 'PRUEBA FALLA ') . "$comando — $ultima" . PHP_EOL;
    if (!$bien) {
        $motivo = $ultima === '' ? 'sin resultado' : $ultima;
        falta('C', "la prueba «{$comando}» no terminó bien ($motivo)");
    }
    $salida = array();
}

// D. Recursos que no son código, con su procedencia.
$carpeta = new RecursiveDirectoryIterator("$raiz/public", FilesystemIterator::SKIP_DOTS);
$iter = new RecursiveIteratorIterator($carpeta);
foreach ($iter as $archivo) {
    $ruta = 'public/' . substr($archivo->getPathname(), strlen("$raiz/public/"));
    if (substr($ruta, -4) !== '.php' && strpos($procedencia, $ruta) === false) {
        falta('D', "$ruta no tiene su fila en la ficha de procedencia");
    }
}

// E. Mensajes y pantallas que nombra el manual.
require "$raiz/src/mensajes.php";
$mensajes = MENSAJES;
preg_match_all('/\b(M[EAV]-\d\d)\b/', $manual, $codigos);
foreach (array_unique($codigos[1]) as $codigo_m) {
    if (!isset($mensajes[$codigo_m])) {
        falta('E', "el manual nombra el mensaje $codigo_m, que el sistema no tiene");
    }
}
preg_match_all('#\b(public/[a-z_]+\.php)\b#', $manual, $pantallas);
foreach (array_unique($pantallas[1]) as $ruta) {
    if (!is_file("$raiz/$ruta")) {
        falta('E', "el manual describe $ruta, que no está en el paquete");
    }
}

// F. La misma versión en todos los documentos que la declaran.
$versiones = array();
$con_version = array('LEEME.txt', 'ENTREGA/LISTA_ENTREGA.md', 'ENTREGA/LIMITES.md',
                     'ENTREGA/ACTA_ENTREGA.md');
foreach ($con_version as $doc) {
    if (preg_match('/^Versión: (.+)$/m', leer_doc("$raiz/$doc"), $m)) {
        $versiones[$doc] = trim($m[1]);
    } else {
        falta('F', "$doc no declara su versión");
    }
}
if (count(array_unique($versiones)) > 1) {
    $detalle = json_encode($versiones, JSON_UNESCAPED_UNICODE);
    falta('F', "los documentos declaran versiones distintas: $detalle");
}

echo implode(PHP_EOL, $faltas) . ($faltas ? PHP_EOL : '');
echo 'Resultado: ' . count($faltas) . ' incoherencias' . PHP_EOL;
exit($faltas ? 1 : 0);

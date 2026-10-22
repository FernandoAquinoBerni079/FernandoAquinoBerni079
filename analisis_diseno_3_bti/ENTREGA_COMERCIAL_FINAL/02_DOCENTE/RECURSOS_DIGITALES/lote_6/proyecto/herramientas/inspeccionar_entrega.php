<?php
// Inspección ESTÁTICA de un paquete de entrega (Capítulo 17). Herramienta del docente: vive fuera del paquete.
// Uso: php inspeccionar_entrega.php <carpeta del paquete>
// No ejecuta, no incluye y no interpreta ningún archivo del paquete: solo lee texto y nombres de archivo.
// A: cada comando de la guía tiene una forma conocida y nombra un archivo que existe dentro del paquete.
// B: cada archivo de la lista de entrega existe dentro del paquete; no hay enlaces simbólicos.
// C: cada prueba declarada es «php pruebas/<nombre>.php», está en la lista cerrada y existe (no se ejecuta).
// D: cada recurso de public/ que no es código tiene su fila en la ficha de procedencia.
// E: cada mensaje y cada pantalla que nombra el manual existen (los mensajes se leen como texto).
// F: la versión es la misma en todos los documentos que la declaran.
const PRUEBAS_PERMITIDAS = array('prueba_contratos', 'prueba_garantias', 'prueba_respaldo');
$faltas = array();
function falta($bloque, $texto)
{
    global $faltas;
    $faltas[] = "INCOHERENCIA [$bloque] $texto";
}
function texto_de($raiz, $ruta)
{
    $p = "$raiz/$ruta";
    return is_file($p) && !is_link($p) ? (string) file_get_contents($p) : '';
}
function dentro($ruta)
{
    return $ruta !== '' && $ruta[0] !== '/' && strpos($ruta, '\\') === false && !preg_match('#(^|/)\.\.(/|$)#', $ruta);
}

if ($argc < 2 || !is_dir($argv[1])) {
    fwrite(STDERR, "Uso: php inspeccionar_entrega.php <carpeta del paquete>\n");
    exit(2);
}
$raiz = rtrim(realpath($argv[1]), '/');
$guia = texto_de($raiz, 'ENTREGA/INSTALAR.md');
$lista = texto_de($raiz, 'ENTREGA/LISTA_ENTREGA.md');
$manual = texto_de($raiz, 'ENTREGA/MANUAL.md');
$procedencia = texto_de($raiz, 'ENTREGA/PROCEDENCIA.md');
foreach (array('INSTALAR.md', 'LISTA_ENTREGA.md', 'MANUAL.md', 'PROCEDENCIA.md') as $doc) {
    if (texto_de($raiz, "ENTREGA/$doc") === '') {
        falta('B', "falta el documento ENTREGA/$doc");
    }
}
$todos = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($raiz, FilesystemIterator::SKIP_DOTS),
                                       RecursiveIteratorIterator::SELF_FIRST);
foreach ($todos as $f) {
    if ($f->isLink()) {
        falta('B', 'enlace simbólico ' . substr($f->getPathname(), strlen($raiz) + 1) . ': no se sigue');
    }
}

// A. Comandos de la guía: solo se leen.
preg_match_all('/```\n(.*?)```/s', $guia, $bloques);
foreach ($bloques[1] as $bloque) {
    foreach (explode("\n", trim($bloque)) as $linea) {
        $linea = trim($linea);
        $servidor = preg_match('/^php -S \S+ -t (\S+)$/', $linea, $m);
        if ($servidor || preg_match('/^php (\S+\.php)(?: [^;&|`$<>]*)?$/', $linea, $m)) {
            if (!dentro($m[1]) || !file_exists("$raiz/$m[1]")) {
                falta('A', "la guía usa «{$linea}», pero no existe {$m[1]} en el paquete");
            }
        } elseif ($linea !== '') {
            falta('A', "la guía tiene un comando de forma desconocida: «{$linea}»");
        }
    }
}

// B. Archivos de la lista de entrega.
preg_match_all('/^- archivo: `([^`]+)`/m', $lista, $archivos);
foreach ($archivos[1] as $ruta) {
    if (!dentro($ruta)) {
        falta('B', "la lista de entrega nombra $ruta, que está fuera del paquete");
    } elseif (!file_exists("$raiz/$ruta")) {
        falta('B', "la lista de entrega incluye $ruta, que no está en el paquete");
    }
}

// C. Pruebas declaradas: lista cerrada, sin ejecutar nada.
preg_match_all('/^- prueba: `([^`]+)`/m', $lista, $pruebas);
foreach ($pruebas[1] as $comando) {
    $forma = preg_match('#^php pruebas/([a-z_0-9]+)\.php$#', $comando, $m);
    if (!$forma || !in_array($m[1], PRUEBAS_PERMITIDAS, true)) {
        $aviso = 'no está en la lista cerrada: no se ejecuta';
        falta('C', "la prueba declarada «{$comando}» $aviso");
    } elseif (!is_file("$raiz/pruebas/{$m[1]}.php")) {
        falta('C', "la prueba declarada pruebas/{$m[1]}.php no está en el paquete");
    }
}

// D. Recursos que no son código, con su procedencia.
$carpeta = null;
if (is_dir("$raiz/public")) {
    $carpeta = new RecursiveDirectoryIterator("$raiz/public", FilesystemIterator::SKIP_DOTS);
}
$publicos = $carpeta ? new RecursiveIteratorIterator($carpeta) : array();
foreach ($publicos as $archivo) {
    $ruta = 'public/' . substr($archivo->getPathname(), strlen("$raiz/public/"));
    if (substr($ruta, -4) !== '.php' && strpos($procedencia, $ruta) === false) {
        falta('D', "$ruta no tiene su fila en la ficha de procedencia");
    }
}

// E. Mensajes y pantallas que nombra el manual (src/mensajes.php se lee como texto, no se incluye).
preg_match_all("/'(M[EAV]-\\d\\d)'\\s*=>/", texto_de($raiz, 'src/mensajes.php'), $definidos);
preg_match_all('/\b(M[EAV]-\d\d)\b/', $manual, $codigos);
foreach (array_unique($codigos[1]) as $codigo) {
    if (!in_array($codigo, $definidos[1], true)) {
        falta('E', "el manual nombra el mensaje $codigo, que el sistema no tiene");
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
    if (preg_match('/^Versión: (.+)$/m', texto_de($raiz, $doc), $m)) {
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
echo 'Resultado: ' . count($faltas) . ' incoherencias (inspección estática; no se ejecutó nada)' . PHP_EOL;
exit($faltas ? 1 : 0);

<?php
// Respaldo consistente de la base, compartido por respaldar.php e instalar.php.
// Copiar el archivo con copy() no alcanza: si la base está en modo WAL, lo último
// confirmado puede estar todavía en biblioteca.sqlite-wal; y si otra conexión está
// confirmando una escritura, la copia puede quedar a mitad de camino.
// VACUUM INTO lee una instantánea consistente a través de SQLite (requiere 3.27).

// Crea el respaldo en $destino y lo verifica. Devuelve null si salió bien,
// o un mensaje de error (en ese caso no deja un archivo de respaldo a medias).
function respaldar_base(PDO $pdo, $destino)
{
    if (file_exists($destino)) {
        return 'Ya existe un archivo con ese nombre: ' . $destino;
    }
    $dir = dirname($destino);
    if (!is_dir($dir) && !mkdir($dir, 0775, true)) {
        return 'No se pudo crear la carpeta de respaldos.';
    }
    try {
        $st = $pdo->prepare('VACUUM INTO ?');
        $st->execute(array($destino));
    } catch (PDOException $e) {
        @unlink($destino);
        return 'No se pudo crear el respaldo: ' . $e->getMessage();
    }
    return verificar_respaldo($pdo, $destino);
}

// El respaldo se abre por separado: tiene que pasar integrity_check y tener las mismas
// filas que la base de origen en cada tabla.
function verificar_respaldo(PDO $origen, $ruta)
{
    try {
        $copia = new PDO('sqlite:' . $ruta);
        $copia->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $estado = $copia->query('PRAGMA integrity_check')->fetchColumn();
        if ($estado !== 'ok') {
            @unlink($ruta);
            return 'El respaldo no pasó la verificación de integridad: ' . $estado;
        }
        $tablas = $origen->query("SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%'")->fetchAll(PDO::FETCH_COLUMN);
        foreach ($tablas as $t) {
            $a = (int) $origen->query('SELECT COUNT(*) FROM "' . $t . '"')->fetchColumn();
            $b = (int) $copia->query('SELECT COUNT(*) FROM "' . $t . '"')->fetchColumn();
            if ($a !== $b) {
                $copia = null;
                @unlink($ruta);
                return "El respaldo no coincide con la base en la tabla $t ($b filas en lugar de $a).";
            }
        }
    } catch (PDOException $e) {
        @unlink($ruta);
        return 'No se pudo verificar el respaldo: ' . $e->getMessage();
    }
    return null;
}

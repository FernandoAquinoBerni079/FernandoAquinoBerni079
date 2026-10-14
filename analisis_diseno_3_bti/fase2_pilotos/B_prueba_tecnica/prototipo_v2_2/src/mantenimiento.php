<?php
// Mantenimiento controlado: reiniciar la base sin conexiones activas.
//
// Procedimiento (reiniciar_con_mantenimiento):
//  1. Marca de mantenimiento (archivo <base>.mantenimiento, creado en forma exclusiva):
//     conectar() rechaza conexiones nuevas mientras existe.
//  2. Bloqueo exclusivo de SQLite (BEGIN EXCLUSIVE + locking_mode = EXCLUSIVE), con espera limitada.
//     No se obtiene si otra conexión tiene una transacción abierta. Si la base está en modo WAL, antes
//     se la pasa a modo DELETE, cosa que SQLite solo permite sin otras conexiones abiertas (aunque estén
//     inactivas); la base queda en modo DELETE, el predeterminado del prototipo. Si no se obtiene el
//     bloqueo: no se toca nada.
//  3. Con el bloqueo tomado, ninguna otra conexión puede leer ni escribir:
//     respaldo consistente y verificado (VACUUM INTO) y reinicio DENTRO del mismo archivo
//     (se eliminan y recrean las tablas en una transacción). La base no se borra ni se reemplaza:
//     una conexión inactiva que quedara abierta ve después la base nueva, no un archivo huérfano.
//  4. Se libera el bloqueo y se quita la marca, salga bien o mal.

class EnMantenimiento extends RuntimeException
{
}

function ruta_marca_mantenimiento()
{
    return ruta_base() . '.mantenimiento';
}

// Devuelve null si salió bien, o el motivo por el que no se hizo (en ese caso la base queda igual).
function reiniciar_con_mantenimiento($copia, $sembrar, $espera_segundos = 5)
{
    $marca = ruta_marca_mantenimiento();
    $fh = @fopen($marca, 'x');
    if ($fh === false) {
        return "Ya hay un mantenimiento en curso (existe $marca). Si quedó de un corte, borralo a mano.";
    }
    fwrite($fh, date('c') . ' ' . getmypid() . "\n");
    $pdo = null;
    try {
        $pdo = new PDO('sqlite:' . ruta_base());
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $pdo->setAttribute(PDO::ATTR_TIMEOUT, 0);
        // Intentos cortos durante la espera; cada intento fallido suelta sus bloqueos para que la otra
        // conexión pueda confirmar su transacción en el intervalo.
        //  - Si la base está en modo WAL, primero se la pasa a modo DELETE. SQLite solo lo permite si
        //    ninguna otra conexión la tiene abierta (aunque esté inactiva): es el control de «sin
        //    conexiones». No se usa locking_mode = EXCLUSIVE sobre una base WAL, porque así SQLite deja
        //    de usar la memoria compartida que coordina con las demás conexiones.
        //  - En modo DELETE, locking_mode = EXCLUSIVE se activa recién dentro de la transacción
        //    exclusiva; si se activara antes, un intento fallido retendría el bloqueo compartido y las
        //    dos conexiones se trabarían hasta agotar la espera.
        $limite = microtime(true) + $espera_segundos;
        $obtenido = false;
        do {
            try {
                $modo = strtolower((string) $pdo->query('PRAGMA journal_mode')->fetchColumn());
                if ($modo === 'wal') {
                    $modo = strtolower((string) $pdo->query('PRAGMA journal_mode = DELETE')->fetchColumn());
                    if ($modo === 'wal') {
                        throw new PDOException('la base sigue en modo WAL');
                    }
                    $GLOBALS['mantenimiento_salio_de_wal'] = true;
                }
                $pdo->exec('BEGIN EXCLUSIVE');
                $pdo->exec('PRAGMA locking_mode = EXCLUSIVE');
                $pdo->exec('COMMIT');
                $pdo->query('SELECT COUNT(*) FROM sqlite_master')->fetchAll();
                $obtenido = true;
            } catch (PDOException $e) {
                try {
                    $pdo->exec('ROLLBACK');
                } catch (PDOException $e2) {
                }
                $pdo->exec('PRAGMA locking_mode = NORMAL');
                try {
                    $pdo->query('SELECT COUNT(*) FROM sqlite_master')->fetchAll();   // suelta lo retenido
                } catch (PDOException $e3) {
                }
                usleep(100000);
            }
        } while (!$obtenido && microtime(true) < $limite);
        if (!$obtenido) {
            return 'Hay otra conexión usando la base (una operación en curso o, en modo WAL, una conexión abierta). '
                . 'No se tocó nada. Detené el servidor y cerrá otras herramientas que tengan la base abierta.';
        }
        $pdo->setAttribute(PDO::ATTR_TIMEOUT, $espera_segundos);
        // Solo para las pruebas automáticas: mantiene la ventana de mantenimiento abierta unos segundos.
        $pausa = getenv('BIBLIO_PRUEBA_PAUSA');
        if ($pausa !== false && $pausa !== '') {
            usleep((int) ((float) $pausa * 1e6));
        }
        // Desde acá el bloqueo exclusivo queda tomado hasta volver a locking_mode = NORMAL.
        $error = respaldar_base($pdo, $copia);
        if ($error !== null) {
            return $error . ' No se tocó nada.';
        }
        $pdo->exec('PRAGMA foreign_keys = OFF');
        $pdo->exec('BEGIN');
        try {
            $obj = $pdo->query("SELECT type, name FROM sqlite_master WHERE name NOT LIKE 'sqlite_%' AND type IN ('table', 'trigger', 'index')")->fetchAll(PDO::FETCH_ASSOC);
            foreach (array('trigger', 'index', 'table') as $tipo) {
                foreach ($obj as $o) {
                    if ($o['type'] === $tipo) {
                        $pdo->exec('DROP ' . strtoupper($tipo) . ' IF EXISTS "' . $o['name'] . '"');
                    }
                }
            }
            crear_esquema($pdo);
            call_user_func($sembrar, $pdo);
            if ($pdo->query('PRAGMA foreign_key_check')->fetch()) {
                throw new RuntimeException('los datos de ejemplo violan una clave foránea');
            }
            $pdo->exec('COMMIT');
        } catch (Exception $e) {
            $pdo->exec('ROLLBACK');
            return 'No se pudo reiniciar (' . $e->getMessage() . '). La base quedó como estaba; el respaldo está en ' . $copia;
        }
        return null;
    } finally {
        if ($pdo !== null) {
            try {
                $pdo->exec('PRAGMA locking_mode = NORMAL');
                $pdo->query('SELECT COUNT(*) FROM sqlite_master')->fetchAll();   // libera el bloqueo
            } catch (PDOException $e) {
            }
            $pdo = null;
        }
        fclose($fh);
        @unlink($marca);
    }
}

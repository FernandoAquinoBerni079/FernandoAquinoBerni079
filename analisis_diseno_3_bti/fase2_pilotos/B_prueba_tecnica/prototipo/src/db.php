<?php
// Conexión única a la base SQLite del prototipo.
// La base es un solo archivo dentro de la carpeta datos/.

// Sin esta línea, PHP usa la hora UTC si el php.ini no fija una zona,
// y los préstamos registrados de noche quedarían con la fecha del día siguiente.
date_default_timezone_set('America/Asuncion');

function ruta_base()
{
    $env = getenv('BIBLIO_DB');
    if ($env !== false && $env !== '') {
        return $env;
    }
    return __DIR__ . '/../datos/biblioteca.sqlite';
}

function conectar()
{
    static $pdo = null;
    if ($pdo !== null) {
        return $pdo;
    }
    $pdo = new PDO('sqlite:' . ruta_base());
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
    // SQLite no controla claves foráneas si no se le pide en cada conexión.
    $pdo->exec('PRAGMA foreign_keys = ON');
    // Espera hasta 3 s si otra conexión está escribiendo, en lugar de fallar enseguida.
    $pdo->setAttribute(PDO::ATTR_TIMEOUT, 3);
    return $pdo;
}

function crear_esquema(PDO $pdo)
{
    $pdo->exec('CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ejemplares INTEGER NOT NULL CHECK (ejemplares >= 0)
    )');
    $pdo->exec('CREATE TABLE IF NOT EXISTS lectores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        curso TEXT NOT NULL
    )');
    $pdo->exec('CREATE TABLE IF NOT EXISTS prestamos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        libro_id INTEGER NOT NULL REFERENCES libros(id),
        lector_id INTEGER NOT NULL REFERENCES lectores(id),
        fecha_salida TEXT NOT NULL,
        fecha_devolucion TEXT
    )');
}

// Ejemplares disponibles = ejemplares del libro menos préstamos sin devolver.
function disponibles(PDO $pdo, $libro_id)
{
    $st = $pdo->prepare('SELECT l.ejemplares - (SELECT COUNT(*) FROM prestamos p
                          WHERE p.libro_id = l.id AND p.fecha_devolucion IS NULL) AS d
                         FROM libros l WHERE l.id = ?');
    $st->execute(array($libro_id));
    $d = $st->fetchColumn();
    return $d === false ? null : (int) $d;
}

// Regla de negocio central del núcleo: no se presta lo que no está disponible.
// Devuelve un mensaje de error o null si el préstamo se registró.
function registrar_prestamo(PDO $pdo, $libro_id, $lector_id, $fecha)
{
    $pdo->beginTransaction();
    try {
        $d = disponibles($pdo, $libro_id);
        if ($d === null) {
            $pdo->rollBack();
            return 'El libro no existe.';
        }
        if ($d <= 0) {
            $pdo->rollBack();
            return 'No quedan ejemplares disponibles de ese libro.';
        }
        $st = $pdo->prepare('SELECT COUNT(*) FROM lectores WHERE id = ?');
        $st->execute(array($lector_id));
        if ((int) $st->fetchColumn() === 0) {
            $pdo->rollBack();
            return 'El lector no existe.';
        }
        $st = $pdo->prepare('INSERT INTO prestamos (libro_id, lector_id, fecha_salida) VALUES (?, ?, ?)');
        $st->execute(array($libro_id, $lector_id, $fecha));
        $pdo->commit();
        return null;
    } catch (Exception $e) {
        if ($pdo->inTransaction()) {
            $pdo->rollBack();
        }
        throw $e;
    }
}

function registrar_devolucion(PDO $pdo, $prestamo_id, $fecha)
{
    $st = $pdo->prepare('UPDATE prestamos SET fecha_devolucion = ? WHERE id = ? AND fecha_devolucion IS NULL');
    $st->execute(array($fecha, $prestamo_id));
    return $st->rowCount() === 1 ? null : 'Ese préstamo no existe o ya fue devuelto.';
}

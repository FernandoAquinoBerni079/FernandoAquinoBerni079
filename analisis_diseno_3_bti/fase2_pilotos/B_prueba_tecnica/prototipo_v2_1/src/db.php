<?php
// Datos y reglas del núcleo: obra/edición, ejemplar, lector, préstamo y usuario.
// Las reglas RN-01 a RN-06 son supuestos didácticos del proyecto, no normas del MEC
// ni políticas de una biblioteca real.

// Sin esta línea, PHP usa UTC si el php.ini no fija una zona y un préstamo
// registrado de noche quedaría con la fecha del día siguiente.
date_default_timezone_set('America/Asuncion');

const PLAZO_DIAS = 7;              // RN-03
const MAX_ACTIVOS_POR_LECTOR = 2;  // RN-02
const VERSION_ESQUEMA = 2;

function ruta_base()
{
    $env = getenv('BIBLIO_DB');
    if ($env !== false && $env !== '') {
        return $env;
    }
    return __DIR__ . '/../datos/biblioteca.sqlite';
}

function conectar($cerrar = false)
{
    static $pdo = null;
    if ($cerrar) {
        $pdo = null;
        return null;
    }
    if ($pdo !== null) {
        return $pdo;
    }
    $pdo = new PDO('sqlite:' . ruta_base());
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
    // Espera hasta 5 s si otra conexión está escribiendo, en lugar de fallar enseguida.
    $pdo->setAttribute(PDO::ATTR_TIMEOUT, 5);
    // SQLite no controla claves foráneas si no se le pide en cada conexión.
    $pdo->exec('PRAGMA foreign_keys = ON');
    return $pdo;
}

// Cierra la conexión compartida (el instalador la cierra antes de borrar el archivo).
function cerrar_conexion()
{
    conectar(true);
}

function crear_esquema(PDO $pdo)
{
    $sql = array(
        // Obra/edición: la descripción bibliográfica. No se presta.
        'CREATE TABLE obras (
            id INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            edicion TEXT NOT NULL
        )',
        // Ejemplar: el libro físico, con un código propio. Es lo que se presta.
        'CREATE TABLE ejemplares (
            id INTEGER PRIMARY KEY,
            obra_id INTEGER NOT NULL REFERENCES obras(id),
            codigo TEXT NOT NULL UNIQUE,
            activo INTEGER NOT NULL DEFAULT 1 CHECK (activo IN (0, 1))
        )',
        'CREATE TABLE lectores (
            id INTEGER PRIMARY KEY,
            codigo TEXT NOT NULL UNIQUE,
            nombre TEXT NOT NULL,
            curso TEXT NOT NULL,
            activo INTEGER NOT NULL DEFAULT 1 CHECK (activo IN (0, 1))
        )',
        // Cada préstamo corresponde a un ejemplar. Abierto mientras fecha_devolucion es NULL.
        'CREATE TABLE prestamos (
            id INTEGER PRIMARY KEY,
            ejemplar_id INTEGER NOT NULL REFERENCES ejemplares(id),
            lector_id INTEGER NOT NULL REFERENCES lectores(id),
            fecha_salida TEXT NOT NULL,
            fecha_vencimiento TEXT NOT NULL,
            fecha_devolucion TEXT,
            CHECK (fecha_vencimiento >= fecha_salida),
            CHECK (fecha_devolucion IS NULL OR fecha_devolucion >= fecha_salida)
        )',
        // RN-01: un ejemplar solo puede tener un préstamo activo. Lo garantiza la base,
        // aunque dos solicitudes lleguen a la vez o el formulario se envíe dos veces.
        'CREATE UNIQUE INDEX un_prestamo_activo_por_ejemplar ON prestamos(ejemplar_id) WHERE fecha_devolucion IS NULL',
        // RN-05: la devolución no elimina el préstamo; el historial no se borra.
        "CREATE TRIGGER prestamos_sin_borrado BEFORE DELETE ON prestamos
         BEGIN SELECT RAISE(ABORT, 'Los préstamos no se borran: forman el historial.'); END",
        "CREATE TRIGGER prestamos_datos_fijos BEFORE UPDATE OF ejemplar_id, lector_id, fecha_salida ON prestamos
         BEGIN SELECT RAISE(ABORT, 'El ejemplar, el lector y la fecha de salida de un préstamo no se modifican.'); END",
        "CREATE TRIGGER devolucion_unica BEFORE UPDATE OF fecha_devolucion ON prestamos
         WHEN OLD.fecha_devolucion IS NOT NULL
         BEGIN SELECT RAISE(ABORT, 'Ese préstamo ya fue devuelto.'); END",
        // RN-06: lectores y ejemplares con historial no se borran; se inactivan.
        "CREATE TRIGGER ejemplar_con_historial BEFORE DELETE ON ejemplares
         WHEN EXISTS (SELECT 1 FROM prestamos WHERE ejemplar_id = OLD.id)
         BEGIN SELECT RAISE(ABORT, 'El ejemplar tiene historial: se inactiva, no se borra.'); END",
        "CREATE TRIGGER lector_con_historial BEFORE DELETE ON lectores
         WHEN EXISTS (SELECT 1 FROM prestamos WHERE lector_id = OLD.id)
         BEGIN SELECT RAISE(ABORT, 'El lector tiene historial: se inactiva, no se borra.'); END",
        // Permisos mínimos: una cuenta con rol de operación. Sin sesión solo se consulta.
        "CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY,
            usuario TEXT NOT NULL UNIQUE,
            clave_hash TEXT NOT NULL,
            rol TEXT NOT NULL CHECK (rol IN ('bibliotecaria'))
        )",
        'PRAGMA user_version = ' . VERSION_ESQUEMA,
    );
    foreach ($sql as $s) {
        $pdo->exec($s);
    }
}

function sumar_dias($fecha, $dias)
{
    $d = DateTime::createFromFormat('!Y-m-d', $fecha);
    if ($d === false || $d->format('Y-m-d') !== $fecha) {
        return null;
    }
    $d->modify('+' . (int) $dias . ' days');
    return $d->format('Y-m-d');
}

function fila(PDO $pdo, $sql, $params)
{
    $st = $pdo->prepare($sql);
    $st->execute($params);
    return $st->fetch();
}

// Registra un préstamo. Devuelve null si se registró, o el motivo del rechazo.
// BEGIN IMMEDIATE toma el permiso de escritura antes de leer: dos préstamos
// simultáneos no pueden comprobar las reglas al mismo tiempo (RN-01 y RN-02).
function registrar_prestamo(PDO $pdo, $codigo_ejemplar, $codigo_lector, $fecha)
{
    $vence = sumar_dias($fecha, PLAZO_DIAS);
    if ($vence === null) {
        return 'La fecha no es válida.';
    }
    try {
        $pdo->exec('BEGIN IMMEDIATE');
    } catch (PDOException $e) {
        return 'La base está ocupada. Intentá de nuevo en unos segundos.';
    }
    try {
        $ej = fila($pdo, 'SELECT id, activo FROM ejemplares WHERE codigo = ?', array($codigo_ejemplar));
        $le = fila($pdo, 'SELECT id, activo FROM lectores WHERE codigo = ?', array($codigo_lector));
        $motivo = null;
        if (!$ej) {
            $motivo = 'El ejemplar no existe.';
        } elseif (!$ej['activo']) {
            $motivo = 'El ejemplar está dado de baja.';
        } elseif (!$le) {
            $motivo = 'El lector no existe.';
        } elseif (!$le['activo']) {
            $motivo = 'El lector está inactivo y no puede recibir préstamos.';                 // RN-04
        } elseif (fila($pdo, 'SELECT 1 FROM prestamos WHERE ejemplar_id = ? AND fecha_devolucion IS NULL', array($ej['id']))) {
            $motivo = 'El ejemplar ya tiene un préstamo activo.';                               // RN-01
        } else {
            $n = fila($pdo, 'SELECT COUNT(*) AS n FROM prestamos WHERE lector_id = ? AND fecha_devolucion IS NULL', array($le['id']));
            if ((int) $n['n'] >= MAX_ACTIVOS_POR_LECTOR) {
                $motivo = 'El lector ya tiene ' . MAX_ACTIVOS_POR_LECTOR . ' préstamos activos.'; // RN-02
            }
        }
        if ($motivo !== null) {
            $pdo->exec('ROLLBACK');
            return $motivo;
        }
        $st = $pdo->prepare('INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (?, ?, ?, ?)');
        $st->execute(array($ej['id'], $le['id'], $fecha, $vence));
        $pdo->exec('COMMIT');
        return null;
    } catch (PDOException $e) {
        try {
            $pdo->exec('ROLLBACK');
        } catch (PDOException $e2) {
        }
        // Segunda barrera de RN-01: el índice único de la base.
        if (strpos($e->getMessage(), 'UNIQUE') !== false) {
            return 'El ejemplar ya tiene un préstamo activo.';
        }
        throw $e;
    }
}

function registrar_devolucion(PDO $pdo, $prestamo_id, $fecha)
{
    if (sumar_dias($fecha, 0) === null) {
        return 'La fecha no es válida.';
    }
    try {
        $st = $pdo->prepare('UPDATE prestamos SET fecha_devolucion = ? WHERE id = ? AND fecha_devolucion IS NULL');
        $st->execute(array($fecha, $prestamo_id));
    } catch (PDOException $e) {
        if (strpos($e->getMessage(), 'CHECK') !== false) {
            return 'La fecha de devolución no puede ser anterior a la de salida.';
        }
        throw $e;
    }
    return $st->rowCount() === 1 ? null : 'Ese préstamo no existe o ya fue devuelto.';
}

function inactivar($pdo, $tabla, $codigo)
{
    if ($tabla !== 'lectores' && $tabla !== 'ejemplares') {
        return 'Tabla no válida.';
    }
    $st = $pdo->prepare("UPDATE $tabla SET activo = 0 WHERE codigo = ? AND activo = 1");
    $st->execute(array($codigo));
    return $st->rowCount() === 1 ? null : 'No existe o ya estaba inactivo.';
}

// ---- Consultas ----

function catalogo(PDO $pdo, $q)
{
    $st = $pdo->prepare("SELECT o.titulo, o.autor, o.edicion,
            COUNT(e.id) AS ejemplares,
            SUM(CASE WHEN p.id IS NULL THEN 1 ELSE 0 END) AS disponibles
        FROM obras o
        JOIN ejemplares e ON e.obra_id = o.id AND e.activo = 1
        LEFT JOIN prestamos p ON p.ejemplar_id = e.id AND p.fecha_devolucion IS NULL
        WHERE o.titulo LIKE ? OR o.autor LIKE ?
        GROUP BY o.id ORDER BY o.titulo");
    $st->execute(array('%' . $q . '%', '%' . $q . '%'));
    return $st->fetchAll();
}

function ejemplares_disponibles(PDO $pdo)
{
    return $pdo->query("SELECT e.codigo, o.titulo FROM ejemplares e JOIN obras o ON o.id = e.obra_id
        WHERE e.activo = 1 AND NOT EXISTS (SELECT 1 FROM prestamos p WHERE p.ejemplar_id = e.id AND p.fecha_devolucion IS NULL)
        ORDER BY e.codigo")->fetchAll();
}

function lectores_activos(PDO $pdo)
{
    return $pdo->query('SELECT codigo, nombre, curso FROM lectores WHERE activo = 1 ORDER BY nombre')->fetchAll();
}

function prestamos_activos(PDO $pdo)
{
    return $pdo->query('SELECT p.id, e.codigo, o.titulo, l.nombre, p.fecha_salida, p.fecha_vencimiento
        FROM prestamos p JOIN ejemplares e ON e.id = p.ejemplar_id JOIN obras o ON o.id = e.obra_id
        JOIN lectores l ON l.id = p.lector_id WHERE p.fecha_devolucion IS NULL ORDER BY p.fecha_vencimiento, p.id')->fetchAll();
}

// Vencidos respecto de una fecha de referencia explícita (no siempre «hoy»).
function prestamos_vencidos(PDO $pdo, $fecha_ref)
{
    $st = $pdo->prepare('SELECT p.id, e.codigo, o.titulo, l.nombre, p.fecha_vencimiento
        FROM prestamos p JOIN ejemplares e ON e.id = p.ejemplar_id JOIN obras o ON o.id = e.obra_id
        JOIN lectores l ON l.id = p.lector_id
        WHERE p.fecha_devolucion IS NULL AND p.fecha_vencimiento < ? ORDER BY p.fecha_vencimiento');
    $st->execute(array($fecha_ref));
    return $st->fetchAll();
}

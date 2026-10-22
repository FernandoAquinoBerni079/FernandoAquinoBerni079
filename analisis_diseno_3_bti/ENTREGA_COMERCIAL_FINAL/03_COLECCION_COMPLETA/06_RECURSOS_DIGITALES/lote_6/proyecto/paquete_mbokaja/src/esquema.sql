-- Esquema de la base del sistema de préstamos (versión 3 del esquema, diseño del lote 3 v1.1).
-- Cada sentencia termina en una línea «-- fin»; crear_esquema() las ejecuta en orden.
-- Las restricciones RI-01 a RI-08 son del Capítulo 7 (Tabla 7.3). Datos ficticios: caso Arapoty.

-- Obra: lo que se busca (RF-07). Edición: una publicación de la obra. No se prestan.
CREATE TABLE obras (
    id INTEGER PRIMARY KEY,
    codigo TEXT NOT NULL UNIQUE CHECK (codigo GLOB 'OB-[0-9][0-9][0-9][0-9]'),
    titulo TEXT NOT NULL CHECK (length(trim(titulo)) > 0),
    autor TEXT NOT NULL CHECK (length(trim(autor)) > 0)
)
-- fin
CREATE TABLE ediciones (
    id INTEGER PRIMARY KEY,
    codigo TEXT NOT NULL UNIQUE CHECK (codigo GLOB 'ED-[0-9][0-9][0-9][0-9]'),
    obra_id INTEGER NOT NULL REFERENCES obras(id),
    editorial_anio TEXT
)
-- fin
-- Ejemplar: el libro físico, con su etiqueta. Es lo que se presta (Capítulo 7, 7.2).
CREATE TABLE ejemplares (
    id INTEGER PRIMARY KEY,
    codigo TEXT NOT NULL UNIQUE CHECK (codigo GLOB 'EJ-[0-9][0-9][0-9][0-9]'),
    edicion_id INTEGER NOT NULL REFERENCES ediciones(id),
    activo INTEGER NOT NULL DEFAULT 1 CHECK (activo IN (0, 1))
)
-- fin
-- Lector: código interno, nunca la cédula (RNF-03).
-- RI-06: curso obligatorio solo para estudiantes.
CREATE TABLE lectores (
    id INTEGER PRIMARY KEY,
    codigo TEXT NOT NULL UNIQUE CHECK (codigo GLOB 'LE-[0-9][0-9][0-9][0-9]'),
    nombre TEXT NOT NULL CHECK (length(trim(nombre)) > 0),
    tipo TEXT NOT NULL CHECK (tipo IN ('estudiante', 'docente')),
    curso TEXT,
    activo INTEGER NOT NULL DEFAULT 1 CHECK (activo IN (0, 1)),
    CHECK ((tipo = 'estudiante' AND curso IS NOT NULL AND length(trim(curso)) > 0) OR (tipo = 'docente' AND curso IS NULL))
)
-- fin
-- Parámetro: las cifras de las reglas, que pueden cambiar (RF-02, RF-05, SC-01).
CREATE TABLE parametros (
    nombre TEXT PRIMARY KEY CHECK (nombre IN ('plazo_dias', 'maximo_estudiante', 'maximo_docente')),
    valor INTEGER NOT NULL CHECK (valor > 0)
)
-- fin
-- Préstamo: siempre de un ejemplar. Activo mientras fecha_devolucion es NULL.
-- RI-07: el vencimiento se calcula al prestar y se guarda. RI-08: el curso del estudiante ese día.
CREATE TABLE prestamos (
    id INTEGER PRIMARY KEY,
    ejemplar_id INTEGER NOT NULL REFERENCES ejemplares(id),
    lector_id INTEGER NOT NULL REFERENCES lectores(id),
    curso_al_prestar TEXT,
    fecha_salida TEXT NOT NULL,
    fecha_vencimiento TEXT NOT NULL,
    fecha_devolucion TEXT,
    CHECK (fecha_vencimiento >= fecha_salida),
    CHECK (fecha_devolucion IS NULL OR fecha_devolucion >= fecha_salida)
)
-- fin
-- RI-01, segunda barrera: un solo préstamo sin devolución por ejemplar,
-- aunque dos pedidos lleguen a la vez o alguien saltee las reglas de negocio.
CREATE UNIQUE INDEX un_prestamo_activo_por_ejemplar ON prestamos(ejemplar_id)
WHERE fecha_devolucion IS NULL
-- fin
-- RI-04 (RN-05): la devolución no borra el préstamo.
CREATE TRIGGER prestamos_sin_borrado BEFORE DELETE ON prestamos
BEGIN SELECT RAISE(ABORT, 'Los préstamos no se borran: forman el historial.'); END
-- fin
CREATE TRIGGER prestamos_datos_fijos
BEFORE UPDATE OF ejemplar_id, lector_id, fecha_salida, fecha_vencimiento, curso_al_prestar ON prestamos
BEGIN SELECT RAISE(ABORT, 'Los datos de un préstamo registrado no se modifican.'); END
-- fin
CREATE TRIGGER devolucion_unica BEFORE UPDATE OF fecha_devolucion ON prestamos
WHEN OLD.fecha_devolucion IS NOT NULL
BEGIN SELECT RAISE(ABORT, 'Ese préstamo ya fue devuelto.'); END
-- fin
-- RI-05 (RN-06): lo que tiene historial no se borra ni cambia de código; se inactiva.
CREATE TRIGGER ejemplar_con_historial BEFORE DELETE ON ejemplares
WHEN EXISTS (SELECT 1 FROM prestamos WHERE ejemplar_id = OLD.id)
BEGIN SELECT RAISE(ABORT, 'El ejemplar tiene historial: se inactiva, no se borra.'); END
-- fin
CREATE TRIGGER lector_con_historial BEFORE DELETE ON lectores
WHEN EXISTS (SELECT 1 FROM prestamos WHERE lector_id = OLD.id)
BEGIN SELECT RAISE(ABORT, 'El lector tiene historial: se inactiva, no se borra.'); END
-- fin
CREATE TRIGGER codigo_ejemplar_con_historial
BEFORE UPDATE OF codigo, edicion_id ON ejemplares
WHEN EXISTS (SELECT 1 FROM prestamos WHERE ejemplar_id = OLD.id)
BEGIN SELECT RAISE(ABORT, 'El ejemplar tiene historial: su código y su edición no cambian.');
END
-- fin
CREATE TRIGGER codigo_lector_con_historial BEFORE UPDATE OF codigo ON lectores
WHEN EXISTS (SELECT 1 FROM prestamos WHERE lector_id = OLD.id)
BEGIN SELECT RAISE(ABORT, 'El lector tiene historial: su código no se cambia.'); END
-- fin
-- Cuenta: quién opera y con qué rol (RNF-02). Las claves se guardan solo como hash.
CREATE TABLE cuentas (
    id INTEGER PRIMARY KEY,
    usuario TEXT NOT NULL UNIQUE,
    clave_hash TEXT NOT NULL,
    rol TEXT NOT NULL CHECK (rol IN ('bibliotecaria', 'direccion'))
)
-- fin

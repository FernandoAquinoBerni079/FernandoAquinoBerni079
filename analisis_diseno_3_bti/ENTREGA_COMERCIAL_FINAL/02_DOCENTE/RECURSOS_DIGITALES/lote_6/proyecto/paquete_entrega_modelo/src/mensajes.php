<?php
// Mensajes del sistema. ME-01 a ME-13: los de la Tabla 8.6 (lote 3 v1.1), con sus datos variables.
// MA-01 a MA-07: mensajes de las operaciones auxiliares de la Unidad IV (OA-01 a OA-04).
// MV-01 a MV-12: validación de entradas (formato y obligatorios), con la regla de 8.3:
// qué pasó, por qué y qué puede hacer la persona.
// ME-12 es solo de autenticación (usuario o contraseña); ME-13, de autorización (sin permiso).

const MENSAJES = array(
    'ME-01' => 'No se puede prestar: este lector está inactivo. Si debería poder retirar libros, consultá con la dirección.',
    'ME-02' => 'No se puede prestar: el lector ya tiene %d préstamos activos, el máximo para %s. Tiene que devolver uno antes.',
    'ME-03' => 'No se puede prestar: el ejemplar %s ya está prestado y vence el %s. Elegí otro ejemplar disponible.',
    'ME-04' => 'Préstamo registrado. Vence el %s.',
    'ME-05' => 'Ese código no corresponde a ningún ejemplar de la biblioteca. Revisá la etiqueta; si no es de la biblioteca, apartalo.',
    'ME-06' => 'Este ejemplar no tiene un préstamo activo. No se cerró ningún préstamo: apartalo para revisarlo con el historial.',
    'ME-07' => 'Devolución registrada. El préstamo queda en el historial y el ejemplar está disponible.',
    'ME-08' => 'No encontramos títulos con esas palabras. Probá con otra parte del título.',
    'ME-09' => '0 disponibles por ahora.',
    'ME-10' => 'No hay préstamos activos.',
    'ME-12' => 'No pudimos iniciar la sesión. Revisá el usuario y la contraseña.',
    'ME-13' => 'No tenés permiso para hacer esta operación con tu cuenta. Si la necesitás, consultá con la dirección.',
    // SC-02 (Unidad V): mensaje de estado vacío del informe mensual (PT-09).
    'ME-14' => 'No hay préstamos registrados en %s. El informe está vacío: no es un error.',
    'MA-01' => 'Ejemplar %s registrado en la edición %s. Ya está disponible para prestar.',
    'MA-02' => 'Ya hay un ejemplar con el código %s. Revisá la etiqueta: cada libro físico tiene un código distinto.',
    'MA-03' => 'No hay ninguna edición con el código %s. Registrá primero la obra y su edición.',
    'MA-04' => 'Obra %s y edición %s registradas.',
    'MA-05' => 'Ya existe el código %s. Elegí otro código: no se reutilizan.',
    'MA-06' => 'Lector %s registrado.',
    'MA-07' => 'Datos del lector %s actualizados. Su código y su historial no cambian.',
    'MA-08' => '%s %s inactivado. Su historial se conserva y ya no puede usarse en préstamos nuevos.',
    'MA-09' => 'Datos de la obra %s corregidos. Sus ediciones, sus ejemplares y su historial no cambian.',
    'MV-01' => 'Falta completar: %s. Escribilo y volvé a intentar.',
    'MV-02' => 'El código %s no tiene el formato esperado (%s). Revisá la etiqueta o el registro.',
    'MV-03' => 'Falta el curso: es obligatorio para los estudiantes. Escribilo y volvé a intentar.',
    'MV-04' => 'Los docentes no llevan curso. Dejá el curso vacío y volvé a intentar.',
    'MV-05' => 'No encontramos un lector con el código %s. Revisá el código o registralo primero.',
    'MV-06' => 'No se puede prestar: el ejemplar %s está dado de baja. Elegí otro ejemplar disponible.',
    'MV-07' => 'No encontramos %s con el código %s, o ya estaba inactivo.',
    'MV-08' => 'La fecha %s no es válida. Escribila como año-mes-día, por ejemplo 2026-03-09.',
    'MV-09' => 'La base está ocupada con otra operación. No se registró nada: intentá de nuevo en unos segundos.',
    'MV-10' => 'La devolución no puede tener una fecha anterior a la salida (%s). Revisá la fecha.',
    'MV-11' => 'El mes %s no es válido. Escribilo como año-mes, por ejemplo 2026-04.',
    'MV-12' => 'El formulario venció y no se registró nada. Recargá la página y volvé a intentar.',
);

// Devuelve el texto del mensaje con sus datos, por ejemplo mensaje('ME-04', '09/03').
function mensaje($codigo, ...$datos)
{
    return $datos ? vsprintf(MENSAJES[$codigo], $datos) : MENSAJES[$codigo];
}

// Resultado de una operación: el código del mensaje y su texto. ok = la operación cambió los datos.
function resultado($ok, $codigo, ...$datos)
{
    return array('ok' => $ok, 'codigo' => $codigo, 'texto' => mensaje($codigo, ...$datos));
}

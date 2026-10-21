# Manual breve por tareas

Cada tarea dice quién la hace, dónde, los pasos y qué significan los mensajes.

## T-01. Ingresar al sistema

Quién: Bibliotecaria o dirección. Dónde: public/login.php.

1. Abrí «Ingreso del personal».
2. Escribí tu usuario y tu clave.
3. Apretá «Ingresar».

- ME-12: El usuario o la clave no coinciden: revisalos y volvé a intentar.

## T-02. Prestar un libro

Quién: Bibliotecaria. Dónde: public/prestamo.php.

1. Escribí el código del lector (LE-…) y el del ejemplar (EJ-…).
2. Revisá la fecha.
3. Apretá «Prestar».

- ME-04: Listo: el mensaje dice cuándo vence.
- ME-02: El lector llegó a su máximo: tiene que devolver uno.
- ME-03: El ejemplar ya está prestado: elegí otro.
- ME-01: El lector está inactivo: consultá con la dirección.

## T-03. Registrar una devolución

Quién: Bibliotecaria. Dónde: public/devolucion.php.

1. Escribí el código del ejemplar que vuelve.
2. Revisá la fecha.
3. Apretá «Confirmar devolución».

- ME-07: Listo: el préstamo queda en el historial.
- ME-06: Ese ejemplar no estaba prestado: apartalo y revisá el historial.
- MV-10: La fecha es anterior a la salida: corregila.

## T-04. Ver los préstamos activos y los vencidos

Quién: Bibliotecaria. Dónde: public/activos.php.

1. Escribí la fecha de referencia (año-mes-día).
2. Apretá «Ver».

- ME-10: No hay préstamos activos.
- MV-08: La fecha no es válida: escribila como 2026-03-09.

## T-05. Sacar el informe del mes

Quién: Bibliotecaria o dirección. Dónde: public/informe.php.

1. Escribí el mes (año-mes).
2. Apretá «Ver informe».

- ME-14: Ese mes no tiene préstamos: el informe está vacío y no es un error.
- MV-11: El mes no es válido: escribilo como 2026-04.

## T-06. Buscar un título

Quién: Cualquier persona, sin ingresar. Dónde: public/index.php.

1. Escribí una parte del título.
2. Apretá «Buscar».

- ME-08: No hay títulos con esas palabras: probá con otra parte.
- ME-09: Hay ejemplares, pero todos están prestados.

## T-07. Dar de alta un lector

Quién: Bibliotecaria. Dónde: public/lectores.php.

1. En «Alta de un lector», escribí el código, el nombre y el tipo.
2. Si es estudiante, escribí el curso.
3. Apretá «Registrar el lector».

- MA-06: Listo.
- MV-03: Falta el curso del estudiante.
- MV-04: Los docentes no llevan curso.

## T-08. Hacer un respaldo y restaurarlo

Quién: Responsable técnico. Dónde: consola (pasos 6 y 7 de la guía).

1. Detené el sistema.
2. php respaldar.php.
3. Para volver a un respaldo: php restaurar.php con su nombre y escribí RESTAURAR.

- —: La restauración guarda antes una copia de la base actual en datos/respaldos/.

## T-09. Reservar un libro

Quién: Bibliotecaria. Dónde: public/reservas.php.

1. Escribí el código del lector y el del libro.
2. Apretá «Reservar».

- ME-15: La reserva quedó registrada.

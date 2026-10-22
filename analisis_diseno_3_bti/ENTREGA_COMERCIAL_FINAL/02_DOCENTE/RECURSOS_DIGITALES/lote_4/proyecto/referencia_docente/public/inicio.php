<?php
// PT-04: inicio de la bibliotecaria (zona Bibliotecaria).
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/mensajes.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/_plantilla.php';

exigir_zona('Bibliotecaria');
cabecera('Inicio de la bibliotecaria', 'PT-04');
?>
<ul>
<li><a href="prestamo.php">Prestar</a></li>
<li><a href="devolucion.php">Devolver</a></li>
<li><a href="activos.php">Ver préstamos</a></li>
<li><a href="lectores.php">Gestionar lectores</a></li>
<li><a href="informe.php">Ver informe</a></li>
</ul>
<?php pie();

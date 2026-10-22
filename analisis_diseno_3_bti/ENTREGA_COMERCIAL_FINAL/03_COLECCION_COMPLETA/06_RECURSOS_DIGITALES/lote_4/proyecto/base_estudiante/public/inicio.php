<?php
// PT-04: inicio de la bibliotecaria (zona Bibliotecaria). Cada pantalla se agrega en su capítulo.
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/mensajes.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/_plantilla.php';

exigir_zona('Bibliotecaria');
cabecera('Inicio de la bibliotecaria', 'PT-04');
?>
<ul>
<li><a href="lectores.php">Gestionar lectores</a> (alta de ejemplar: Capítulo 10; lo demás: Capítulo 11)</li>
<li>Prestar y Devolver: se construyen en el Capítulo 12 (PT-05 y PT-06)</li>
<li>Ver préstamos y Ver informe: se construyen en el Capítulo 13 (PT-07 y PT-09)</li>
</ul>
<?php pie();

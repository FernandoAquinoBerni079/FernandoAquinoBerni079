<?php
require __DIR__ . '/../src/auth.php';
iniciar_sesion();
$_SESSION = array();
session_destroy();
header('Location: index.php', true, 303);

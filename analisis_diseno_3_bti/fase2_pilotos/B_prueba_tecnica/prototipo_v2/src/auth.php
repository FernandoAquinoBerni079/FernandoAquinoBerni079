<?php
// Permisos mínimos: sin sesión se consulta el catálogo; registrar préstamos y
// devoluciones exige iniciar sesión con el rol «bibliotecaria».

function iniciar_sesion()
{
    if (session_status() !== PHP_SESSION_ACTIVE) {
        session_set_cookie_params(array('httponly' => true, 'samesite' => 'Lax'));
        session_start();
    }
}

function usuario_actual()
{
    iniciar_sesion();
    return isset($_SESSION['usuario']) ? $_SESSION['usuario'] : null;
}

function exigir_bibliotecaria()
{
    $u = usuario_actual();
    if ($u === null || $u['rol'] !== 'bibliotecaria') {
        http_response_code(403);
        echo '<!doctype html><meta charset="utf-8"><p id="error">Acceso no autorizado: iniciá sesión como bibliotecaria.</p><p><a href="login.php">Ingresar</a></p>';
        exit;
    }
    return $u;
}

function ingresar(PDO $pdo, $usuario, $clave)
{
    $st = $pdo->prepare('SELECT id, usuario, clave_hash, rol FROM usuarios WHERE usuario = ?');
    $st->execute(array($usuario));
    $f = $st->fetch();
    if (!$f || !password_verify($clave, $f['clave_hash'])) {
        return false;
    }
    iniciar_sesion();
    session_regenerate_id(true);
    $_SESSION['usuario'] = array('id' => $f['id'], 'usuario' => $f['usuario'], 'rol' => $f['rol']);
    return true;
}

// Ficha anti-falsificación: un formulario de otro sitio no puede operar con la sesión abierta.
function ficha_csrf()
{
    iniciar_sesion();
    if (empty($_SESSION['csrf'])) {
        $_SESSION['csrf'] = bin2hex(random_bytes(16));
    }
    return $_SESSION['csrf'];
}

function csrf_valida()
{
    iniciar_sesion();
    return isset($_POST['csrf'], $_SESSION['csrf']) && hash_equals($_SESSION['csrf'], (string) $_POST['csrf']);
}

function e($s)
{
    return htmlspecialchars((string) $s, ENT_QUOTES, 'UTF-8');
}

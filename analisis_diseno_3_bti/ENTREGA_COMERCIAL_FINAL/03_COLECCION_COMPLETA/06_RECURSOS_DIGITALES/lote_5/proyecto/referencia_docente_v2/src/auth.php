<?php
// Autenticación y autorización (RNF-02). Adaptado del Piloto B v2.3, con dos roles.
//  - Autenticación: ingresar() comprueba usuario y clave; si fallan, ME-12.
//  - Autorización: cada operación comprueba el rol de la cuenta en el servidor; si no alcanza, ME-13.
// Las zonas del mapa (Figura 8.1) definen qué roles usa cada pantalla:
const ROLES_ZONA = array(
    'Pública' => array(),
    'Bibliotecaria' => array('bibliotecaria'),
    'Bibliotecaria o dirección' => array('bibliotecaria', 'direccion'),
);

function iniciar_sesion()
{
    if (session_status() !== PHP_SESSION_ACTIVE) {
        session_set_cookie_params(array('httponly' => true, 'samesite' => 'Lax'));
        session_start();
    }
}

function cuenta_actual()
{
    iniciar_sesion();
    return isset($_SESSION['cuenta']) ? $_SESSION['cuenta'] : null;
}

// ¿La cuenta tiene uno de los roles pedidos? Lo usan las páginas y también cada operación
// de src/reglas.php.
function tiene_rol($cuenta, array $roles)
{
    return $cuenta !== null && in_array($cuenta['rol'], $roles, true);
}

// Para las páginas: si la cuenta no tiene el rol, responde 403 con ME-13 y no sigue.
function exigir_zona($zona)
{
    $cuenta = cuenta_actual();
    if (!tiene_rol($cuenta, ROLES_ZONA[$zona])) {
        http_response_code(403);
        echo '<!doctype html><meta charset="utf-8">'
            . '<p id="error" data-codigo="ME-13">' . e(mensaje('ME-13')) . '</p>'
            . '<p><a href="login.php">Ingresar</a> · '
            . '<a href="index.php">Consulta pública</a></p>';
        exit;
    }
    return $cuenta;
}

// Devuelve null si ingresó, o el texto de ME-12. No dice si falló el usuario o la clave.
function ingresar(PDO $pdo, $usuario, $clave)
{
    $f = fila($pdo, 'SELECT id, usuario, clave_hash, rol FROM cuentas WHERE usuario = ?', array($usuario));
    if (!$f || !password_verify($clave, $f['clave_hash'])) {
        return mensaje('ME-12');
    }
    iniciar_sesion();
    session_regenerate_id(true);
    $_SESSION['cuenta'] = array('id' => $f['id'], 'usuario' => $f['usuario'], 'rol' => $f['rol']);
    return null;
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

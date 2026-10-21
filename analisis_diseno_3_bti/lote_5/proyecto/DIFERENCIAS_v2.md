# Diferencias de la referencia docente v2 (lote 5)

Generado por `lote_5/build/diferencias.py`. La referencia del lote 4 (`lote_4/proyecto/referencia_docente/`) no se modificó: las versiones nuevas son copias en `lote_5/proyecto/`. Las pruebas de regresión están en `lote_5/resultados_pruebas/`.

## referencia_docente_v2 — Corrección de IN-02 (Capítulo 16, ejemplo central)

| Archivo | Cambio | Líneas agregadas | Líneas quitadas |
|---|---|---|---|
| `LEEME.txt` | modificado | 2 | 0 |
| `pruebas/prueba_in02.sh` | nuevo | 46 | 0 |
| `public/_plantilla.php` | modificado | 25 | 1 |
| `public/lectores.php` | modificado | 12 | 5 |

### `LEEME.txt`

```diff
--- antes/LEEME.txt
+++ despues/LEEME.txt
@@ -1,3 +1,5 @@
 Sistema de préstamos de la biblioteca escolar — REFERENCIA DOCENTE (lote 4, Unidad IV)
+VERSIÓN 2 (lote 5): corrige IN-02 (PT-08 conserva lo escrito después de un error). Prueba: pruebas/prueba_in02.sh.
+No reemplaza a lote_4/proyecto/referencia_docente, que se conserva sin cambios. Diferencias: ../DIFERENCIAS_v2.md
 Caso Arapoty, datos ficticios. Adaptado del Piloto B v2.3 al diseño del lote 3 v1.1.
 
```

### `pruebas/prueba_in02.sh`

```diff
--- antes/pruebas/prueba_in02.sh
+++ despues/pruebas/prueba_in02.sh
@@ -0,0 +1,46 @@
+#!/usr/bin/env bash
+# Prueba de la incidencia IN-02 (lote 4, Tabla 13.3; real reproducida): después de un error en el alta de un lector,
+# PT-08 tiene que volver a mostrar lo que se escribió, con el tipo elegido. Agregada con la corrección (referencia v2).
+# Se corre desde la carpeta del sistema: bash pruebas/prueba_in02.sh. Usa una base temporal (BIBLIO_DB).
+# Sobre la referencia del lote 4, que no tiene la corrección, tiene que FALLAR: así se reproduce la incidencia.
+set -u
+PUERTO=${PUERTO:-8781}
+BASE="http://127.0.0.1:$PUERTO"
+TMP=$(mktemp -d)
+export BIBLIO_DB="$TMP/biblioteca.sqlite"
+JAR="$TMP/cookies.txt"; CLAVE=prueba-solo-local
+ok=0; total=0
+chk() { total=$((total+1)); if eval "$2"; then ok=$((ok+1)); echo "CORRECTO $1"; else echo "FALLA    $1"; fi; }
+ficha() { curl -s -b "$JAR" -c "$JAR" "$BASE/$1" | grep -o 'name="csrf" value="[0-9a-f]*"' | head -1 | sed 's/.*value="//;s/"//'; }
+php instalar.php --clave=$CLAVE > /dev/null
+php -S 127.0.0.1:$PUERTO -t public > "$TMP/servidor.log" 2>&1 &
+SRV=$!
+trap 'kill $SRV 2>/dev/null; wait $SRV 2>/dev/null; rm -rf "$TMP"' EXIT
+for i in $(seq 1 20); do curl -s -o /dev/null "$BASE/" && break; sleep 0.25; done
+curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$(ficha login.php)" -d usuario=bibliotecaria1 -d clave=$CLAVE "$BASE/login.php"
+
+# 1. Error MV-04: docente con curso. Lo escrito tiene que volver, con «Docente» elegido.
+curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$(ficha lectores.php)" -d accion=alta_lector -d codigo=LE-0990 \
+  -d nombre="Docente de prueba (ficticio)" -d tipo=docente -d curso=6 "$BASE/lectores.php"
+H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/lectores.php")
+chk "IN-02: después de MV-04 se muestra el mensaje" 'echo "$H" | grep -q "data-codigo=\"MV-04\""'
+chk "IN-02: el tipo elegido (Docente) sigue elegido" 'echo "$H" | grep -q "value=\"docente\" selected"'
+chk "IN-02: el código y el nombre escritos se conservan" 'echo "$H" | grep -q "value=\"LE-0990\"" && echo "$H" | grep -q "value=\"Docente de prueba (ficticio)\""'
+chk "IN-02: la ficha CSRF no se conserva como dato escrito" '! echo "$H" | grep -q "name=\"csrf\" value=\"\""'
+# 2. Los datos se muestran una sola vez: al volver a entrar, el formulario está vacío.
+H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/lectores.php")
+chk "IN-02: al recargar, el formulario vuelve a estar vacío" '! echo "$H" | grep -q "value=\"LE-0990\""'
+# 3. Si sale bien, no se conserva nada.
+curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$(ficha lectores.php)" -d accion=alta_lector -d codigo=LE-0991 \
+  -d nombre="Docente de prueba 2 (ficticio)" -d tipo=docente -d curso= "$BASE/lectores.php"
+H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/lectores.php")
+chk "IN-02: después de un alta correcta (MA-06), el formulario queda vacío" 'echo "$H" | grep -q "data-codigo=\"MA-06\"" && ! echo "$H" | grep -q "value=\"LE-0991\""'
+# 4. Lo conservado es solo del alta de lector: otro formulario con error no llena el del lector.
+curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$(ficha lectores.php)" -d accion=alta_ejemplar -d codigo=EJ-12 \
+  -d edicion=ED-0060 "$BASE/lectores.php"
+H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/lectores.php")
+chk "IN-02: un error en otro formulario (MV-02) no llena el alta de lector" 'echo "$H" | grep -q "data-codigo=\"MV-02\"" && ! echo "$H" | grep -q "value=\"EJ-12\""'
+echo
+echo "Resultado: $ok de $total correctas"
+[ $ok -eq $total ]
+
```

### `public/_plantilla.php`

```diff
--- antes/public/_plantilla.php
+++ despues/public/_plantilla.php
@@ -44,9 +44,33 @@
 
 // Patrón POST-redirección-GET: el resultado se guarda en la sesión y se muestra una sola vez.
-function guardar_aviso($r, $destino)
+// v2 (corrección de IN-02): si la operación falló, se guardan también los datos escritos,
+// sin la ficha CSRF ni la contraseña, para que el formulario los vuelva a mostrar.
+// Si salió bien, no se guarda nada.
+function guardar_aviso($r, $destino, array $entradas = array())
 {
     $_SESSION['aviso'] = $r;
+    unset($entradas['csrf'], $entradas['clave']);
+    $_SESSION['entradas'] = $r['ok'] ? array() : $entradas;
     header('Location: ' . $destino, true, 303);
     exit;
+}
+
+// v2 (IN-02): los datos del último envío fallido de ese formulario; se entregan una sola vez.
+function tomar_entradas($accion)
+{
+    $e = isset($_SESSION['entradas']) ? $_SESSION['entradas'] : array();
+    unset($_SESSION['entradas']);
+    return (isset($e['accion']) && $e['accion'] === $accion) ? $e : array();
+}
+
+// v2 (IN-02): valor escrito antes, ya escapado, y la opción que estaba elegida.
+function valor(array $e, $campo)
+{
+    return isset($e[$campo]) ? e((string) $e[$campo]) : '';
+}
+
+function elegido(array $e, $campo, $opcion)
+{
+    return (isset($e[$campo]) && $e[$campo] === $opcion) ? ' selected' : '';
 }
 
```

### `public/lectores.php`

```diff
--- antes/public/lectores.php
+++ despues/public/lectores.php
@@ -33,8 +33,9 @@
         $r = resultado(false, 'MV-01', 'la operación');
     }
-    guardar_aviso($r, 'lectores.php');
+    guardar_aviso($r, 'lectores.php', $_POST);
 }
 cabecera('Lectores y ejemplares', 'PT-08');
 aviso(tomar_aviso());
+$previo = tomar_entradas('alta_lector');   // v2 (IN-02)
 ?>
 <h2>Alta de un ejemplar</h2>
@@ -65,8 +66,14 @@
 <h2>Alta de un lector</h2>
 <?php formulario_inicio('alta_lector'); ?>
-<label>Código del lector <input name="codigo" placeholder="LE-0000"></label>
-<label>Nombre <input name="nombre"></label>
-<label>Tipo <select name="tipo"><option value="estudiante">Estudiante</option><option value="docente">Docente</option></select></label>
-<label>Curso (solo estudiantes) <input name="curso"></label>
+<label>Código del lector
+<input name="codigo" placeholder="LE-0000"
+    value="<?= valor($previo, 'codigo') ?>"></label>
+<label>Nombre <input name="nombre" value="<?= valor($previo, 'nombre') ?>"></label>
+<label>Tipo <select name="tipo">
+<option value="estudiante"<?= elegido($previo, 'tipo', 'estudiante') ?>>Estudiante</option>
+<option value="docente"<?= elegido($previo, 'tipo', 'docente') ?>>Docente</option>
+</select></label>
+<label>Curso (solo estudiantes)
+<input name="curso" value="<?= valor($previo, 'curso') ?>"></label>
 <button>Registrar el lector</button>
 </form>
```

## referencia_docente_v2_sc02 — Cambio aprobado SC-02 sobre la v2 (Capítulo 16, ejemplo complementario)

| Archivo | Cambio | Líneas agregadas | Líneas quitadas |
|---|---|---|---|
| `LEEME.txt` | modificado | 1 | 1 |
| `pruebas/prueba_contratos.php` | modificado | 6 | 0 |
| `public/informe.php` | modificado | 1 | 1 |
| `src/mensajes.php` | modificado | 2 | 0 |
| `src/reglas.php` | modificado | 5 | 0 |

### `LEEME.txt`

```diff
--- antes/LEEME.txt
+++ despues/LEEME.txt
@@ -1,4 +1,4 @@
 Sistema de préstamos de la biblioteca escolar — REFERENCIA DOCENTE (lote 4, Unidad IV)
-VERSIÓN 2 (lote 5): corrige IN-02 (PT-08 conserva lo escrito después de un error). Prueba: pruebas/prueba_in02.sh.
+VERSIÓN 2 CON SC-02 (lote 5): IN-02 corregida y el cambio aprobado SC-02 (ME-14 para el informe de un mes vacío).
 No reemplaza a lote_4/proyecto/referencia_docente, que se conserva sin cambios. Diferencias: ../DIFERENCIAS_v2.md
 Caso Arapoty, datos ficticios. Adaptado del Piloto B v2.3 al diseño del lote 3 v1.1.
```

### `pruebas/prueba_contratos.php`

```diff
--- antes/pruebas/prueba_contratos.php
+++ despues/pruebas/prueba_contratos.php
@@ -186,4 +186,10 @@
 rechaza('PA-05: con la cuenta de dirección', function () use ($pdo, $dir_) { return editar_obra($pdo, $dir_, 'OB-0031', 'X', 'Y'); }, 'ME-13');
 
+echo "-- SC-02 informe de un mes sin préstamos (Unidad V)\n";
+$v = informe_mensual($pdo, $dir_, '2026-01');
+comprobar('SC-02: mes sin préstamos → correcto, ME-14, sin filas y total 0', $v['ok'] && $v['codigo'] === 'ME-14' && $v['filas'] === array() && $v['total'] === 0);
+comprobar('SC-02: el texto de ME-14 nombra el mes', strpos($v['texto'], '2026-01') !== false);
+comprobar('SC-02: un mes con préstamos sigue sin mensaje y con su total', informe_mensual($pdo, $dir_, '2026-03')['codigo'] === null);
+
 echo "-- Otros\n";
 comprobar('Zona horaria de Paraguay', date_default_timezone_get() === 'America/Asuncion');
```

### `public/informe.php`

```diff
--- antes/public/informe.php
+++ despues/public/informe.php
@@ -14,5 +14,5 @@
 <form method="get"><label>Mes (año-mes) <input name="mes" value="<?= e($mes) ?>"></label> <button>Ver informe</button></form>
 <?php aviso($r); ?>
-<?php if ($r['ok']): ?>
+<?php if ($r['ok'] && $r['total'] > 0):   // SC-02: el mes vacío muestra solo ME-14 ?>
 <table id="informe">
 <tr><th>Grupo</th><th>Préstamos</th></tr>
```

### `src/mensajes.php`

```diff
--- antes/src/mensajes.php
+++ despues/src/mensajes.php
@@ -19,4 +19,6 @@
     'ME-12' => 'No pudimos iniciar la sesión. Revisá el usuario y la contraseña.',
     'ME-13' => 'No tenés permiso para hacer esta operación con tu cuenta. Si la necesitás, consultá con la dirección.',
+    // SC-02 (Unidad V): mensaje de estado vacío del informe mensual (PT-09).
+    'ME-14' => 'No hay préstamos registrados en %s. El informe está vacío: no es un error.',
     'MA-01' => 'Ejemplar %s registrado en la edición %s. Ya está disponible para prestar.',
     'MA-02' => 'Ya hay un ejemplar con el código %s. Revisá la etiqueta: cada libro físico tiene un código distinto.',
```

### `src/reglas.php`

```diff
--- antes/src/reglas.php
+++ despues/src/reglas.php
@@ -421,4 +421,6 @@
 //   Resultado: préstamos del mes por curso al prestar (RI-08), la fila «Docentes» y el total
 //   contado de nuevo. Errores: ME-13. Validación: MV-11. Prueba: P-09.
+//   SC-02 (Unidad V): si el mes no tiene préstamos, el resultado es correcto, sin filas, con el
+//   mensaje de estado vacío ME-14. Prueba: P-09 (caso del mes vacío).
 function informe_mensual(PDO $pdo, $cuenta, $mes)
 {
@@ -442,4 +444,7 @@
     $total = fila($pdo, 'SELECT COUNT(*) AS n FROM prestamos
         WHERE substr(fecha_salida, 1, 7) = ?', array($mes));
+    if ((int) $total['n'] === 0) {
+        return resultado(true, 'ME-14', $mes) + $vacio;                  // SC-02
+    }
     return array('ok' => true, 'codigo' => null, 'texto' => '', 'filas' => $filas,
         'total' => (int) $total['n']);
```

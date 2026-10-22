#!/usr/bin/env bash
# Prueba de punta a punta con el servidor incorporado de PHP (E-6a: prototipo docente completo).
# Uso: bash pruebas/prueba_http.sh   (desde la carpeta referencia_docente/; requiere bash y curl; en Windows, Git Bash)
# Adaptada del Piloto B v2.3 a las pantallas PT-01 a PT-09, los dos roles y los mensajes ME-12 y ME-13.
# La última parte (pedidos simultáneos por HTTP) necesita PHP_CLI_SERVER_WORKERS, que solo existe en Linux y macOS:
# en Windows el servidor incorporado atiende de a un pedido y NO sirve como prueba de simultaneidad
# (para eso está pruebas/prueba_carrera.php, con procesos independientes).
set -u
PUERTO=${PUERTO:-8772}
BASE="http://127.0.0.1:$PUERTO"
TMP=$(mktemp -d)
export BIBLIO_DB="$TMP/biblioteca.sqlite"
LOG="$TMP/servidor.log"
JAR="$TMP/cookies.txt"; JAR_D="$TMP/cookies_dir.txt"
CLAVE=prueba-solo-local
ok=0; total=0
chk() { total=$((total+1)); if eval "$2"; then ok=$((ok+1)); echo "CORRECTO $1"; else echo "FALLA    $1"; fi; }
consulta() { php -r 'putenv("BIBLIO_DB=".$argv[1]); require "src/db.php"; echo conectar()->query($argv[2])->fetchColumn();' "$BIBLIO_DB" "$1"; }
arrancar() {
  PHP_CLI_SERVER_WORKERS=${1:-1} php -S 127.0.0.1:$PUERTO -t public >> "$LOG" 2>&1 &
  SRV=$!
  for i in $(seq 1 20); do curl -s -o /dev/null "$BASE/" && break; sleep 0.25; done
}
parar() { kill $SRV 2>/dev/null; wait $SRV 2>/dev/null; }
trap 'parar; rm -rf "$TMP"' EXIT
ficha() { curl -s -b "$2" -c "$2" "$BASE/$1" | grep -o 'name="csrf" value="[0-9a-f]*"' | head -1 | sed 's/.*value="//;s/"//'; }
ingresar() { T=$(ficha login.php "$2"); curl -s -o /dev/null -w "%{http_code} %{redirect_url}" -b "$2" -c "$2" -d csrf="$T" -d usuario="$1" -d clave="$3" "$BASE/login.php"; }
codigo_en() { echo "$1" | grep -o 'data-codigo="[A-Z]*-[0-9]*"' | head -1 | sed 's/data-codigo="//;s/"//'; }

php instalar.php --clave=$CLAVE > /dev/null
arrancar 1

# Consulta pública (PT-01, PT-02, OP-03)
H=$(curl -s --get --data-urlencode "q=arroyo" "$BASE/")
chk "P-08: la consulta pública muestra las dos obras que coinciden con «arroyo»" 'echo "$H" | grep -q "Cuentos del arroyo Arapoty" && echo "$H" | grep -q "El arroyo y la escuela"'
chk "P-12: la consulta pública no muestra códigos ni nombres de lectores" '! echo "$H" | grep -q -E "LE-[0-9]{4}|Estudiante A|Docente D"'
chk "La consulta pública no tiene formularios que modifiquen datos" '! echo "$H" | grep -q "method=\"post\""'
H=$(curl -s --get --data-urlencode "q=zzz" "$BASE/")
chk "OP-03 sin coincidencias: ME-08" '[ "$(codigo_en "$H")" = ME-08 ]'

# Autorización sin sesión (ME-13) y autenticación fallida (ME-12)
H=$(curl -s -w "%{http_code}" "$BASE/inicio.php")
chk "PT-04 sin sesión: 403 con ME-13" 'echo "$H" | grep -q "403$" && [ "$(codigo_en "$H")" = ME-13 ]'
C=$(curl -s -o /dev/null -w "%{http_code}" -d lector=LE-0123 -d ejemplar=EJ-0457 "$BASE/prestamo.php")
chk "P-11: préstamo enviado sin sesión: 403 y ningún préstamo creado" '[ "$C" = 403 ] && [ "$(consulta "SELECT COUNT(*) FROM prestamos")" = 0 ]'
T=$(ficha login.php "$JAR")
H=$(curl -s -b "$JAR" -c "$JAR" -d csrf="$T" -d usuario=bibliotecaria1 -d clave=equivocada "$BASE/login.php")
chk "Clave incorrecta: ME-12, el mensaje de autenticación" '[ "$(codigo_en "$H")" = ME-12 ]'

# Dirección: solo la zona «Bibliotecaria o dirección»
R=$(ingresar direccion1 "$JAR_D" $CLAVE)
chk "La dirección ingresa y va al informe (PT-09)" 'echo "$R" | grep -q "^303 .*informe.php"'
H=$(curl -s -b "$JAR_D" -c "$JAR_D" -w "%{http_code}" "$BASE/inicio.php")
chk "La dirección no entra a PT-04: 403 con ME-13 (no ME-12)" 'echo "$H" | grep -q "403$" && [ "$(codigo_en "$H")" = ME-13 ]'
TD=$(ficha informe.php "$JAR_D")
C=$(curl -s -o /dev/null -w "%{http_code}" -b "$JAR_D" -c "$JAR_D" -d csrf="$TD" -d lector=LE-0123 -d ejemplar=EJ-0457 "$BASE/prestamo.php")
chk "La dirección no registra préstamos: 403 y ningún préstamo" '[ "$C" = 403 ] && [ "$(consulta "SELECT COUNT(*) FROM prestamos")" = 0 ]'
C=$(curl -s -o /dev/null -w "%{http_code}" -b "$JAR_D" -c "$JAR_D" "$BASE/informe.php?mes=2026-03")
chk "La dirección ve el informe mensual (200)" '[ "$C" = 200 ]'

# Bibliotecaria
R=$(ingresar bibliotecaria1 "$JAR" $CLAVE)
chk "La bibliotecaria ingresa y va a PT-04" 'echo "$R" | grep -q "^303 .*inicio.php"'
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d lector=LE-0123 -d ejemplar=EJ-0457 "$BASE/prestamo.php"
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/prestamo.php")
chk "Préstamo sin ficha CSRF: MV-12 y no se registra" '[ "$(codigo_en "$H")" = MV-12 ] && [ "$(consulta "SELECT COUNT(*) FROM prestamos")" = 0 ]'
T=$(ficha prestamo.php "$JAR")
C=$(curl -s -o /dev/null -w "%{http_code}" -b "$JAR" -c "$JAR" -d csrf="$T" -d lector=LE-0123 -d ejemplar=EJ-0457 "$BASE/prestamo.php")
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/prestamo.php")
chk "P-01: préstamo válido: 303 y ME-04 con el vencimiento" '[ "$C" = 303 ] && [ "$(codigo_en "$H")" = ME-04 ]'
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$T" -d lector=LE-0124 -d ejemplar=EJ-0457 "$BASE/prestamo.php"
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/prestamo.php")
chk "P-07: reenvío sobre el mismo ejemplar: ME-03" '[ "$(codigo_en "$H")" = ME-03 ]'
chk "P-07: sigue habiendo un solo préstamo activo de EJ-0457" '[ "$(consulta "SELECT COUNT(*) FROM prestamos WHERE ejemplar_id = 1 AND fecha_devolucion IS NULL")" = 1 ]'
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/prestamo.php")
chk "Patrón POST-redirección-GET: recargar no repite la operación (el aviso ya no aparece)" '[ -z "$(codigo_en "$H")" ]'
chk "ME-11: el formulario desactiva el botón y muestra «Guardando…» al enviarse" 'echo "$H" | grep -q "Guardando…"'
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$T" -d lector=LE-0125 -d ejemplar=EJ-0458 "$BASE/prestamo.php"
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/prestamo.php")
chk "P-05: lector inactivo: ME-01" '[ "$(codigo_en "$H")" = ME-01 ]'
T=$(ficha lectores.php "$JAR")
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$T" -d accion=alta_ejemplar -d codigo=EJ-0810 -d edicion=ED-0070 "$BASE/lectores.php"
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/lectores.php")
chk "PA-01: alta de un ejemplar desde PT-08: MA-01" '[ "$(codigo_en "$H")" = MA-01 ]'
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/activos.php?fecha=2099-01-01")
chk "P-04: PT-07 muestra quién tiene EJ-0457, vencido respecto de una fecha de referencia lejana" 'echo "$H" | grep -q "EJ-0457" && echo "$H" | grep -q "LE-0123" && echo "$H" | grep -q "Vencido"'
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/informe.php?mes=$(date +%Y-%m)")
chk "P-09: la bibliotecaria también ve el informe; el préstamo de hoy cuenta en el curso 2.º BTI" 'echo "$H" | grep -q "<td>2.º BTI</td><td>1</td>"'

# Devolución
T=$(ficha devolucion.php "$JAR")
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$T" -d ejemplar=EJ-0457 "$BASE/devolucion.php"
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/devolucion.php")
chk "P-03: devolución registrada: ME-07" '[ "$(codigo_en "$H")" = ME-07 ]'
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$T" -d ejemplar=EJ-0457 "$BASE/devolucion.php"
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/devolucion.php")
chk "Segunda devolución del mismo ejemplar: ME-06" '[ "$(codigo_en "$H")" = ME-06 ]'
chk "RI-04: el préstamo devuelto se conserva en el historial" '[ "$(consulta "SELECT COUNT(*) FROM prestamos WHERE fecha_devolucion IS NOT NULL")" = 1 ]'

# Entradas hostiles
H=$(curl -s --get --data-urlencode "q=<script>alert(1)</script>" "$BASE/")
chk "Texto con etiquetas se muestra escapado" '! echo "$H" | grep -q "<script>alert" && echo "$H" | grep -q "&lt;script&gt;"'
H=$(curl -s --get --data-urlencode "q=' OR 1=1 --" "$BASE/")
chk "Comilla en la búsqueda no altera la consulta (consulta parametrizada): ME-08" '[ "$(codigo_en "$H")" = ME-08 ]'

# Salir
curl -s -o /dev/null -b "$JAR" -c "$JAR" "$BASE/salir.php"
H=$(curl -s -b "$JAR" -c "$JAR" -w "%{http_code}" "$BASE/inicio.php")
chk "Después de salir, PT-04 vuelve a responder 403 con ME-13" 'echo "$H" | grep -q "403$"'

# Persistencia entre ejecuciones del servidor
ANTES=$(consulta "SELECT COUNT(*) FROM prestamos")
parar; arrancar 1
chk "Tras reiniciar el servidor se conservan los $ANTES préstamos y el ejemplar EJ-0810" '[ "$(consulta "SELECT COUNT(*) FROM prestamos")" = "$ANTES" ] && [ "$(consulta "SELECT COUNT(*) FROM ejemplares WHERE codigo = '"'"'EJ-0810'"'"'")" = 1 ]'

# Pedidos HTTP simultáneos en 8 sesiones distintas (solo Linux y macOS: PHP_CLI_SERVER_WORKERS)
if [ "$(uname -s)" = Linux ] || [ "$(uname -s)" = Darwin ]; then
  parar; arrancar 8
  for k in 1 2 3 4 5 6 7 8; do
    J="$TMP/sesion_$k.txt"; ingresar bibliotecaria1 "$J" $CLAVE > /dev/null; ficha prestamo.php "$J" > "$TMP/ficha_$k"
  done
  PIDS=""
  for k in 1 2 3 4 5 6 7 8; do
    L=$([ $((k % 2)) = 0 ] && echo LE-0124 || echo LE-0201)
    curl -s -o /dev/null -b "$TMP/sesion_$k.txt" -d csrf="$(cat "$TMP/ficha_$k")" -d lector=$L -d ejemplar=EJ-0601 "$BASE/prestamo.php" &
    PIDS="$PIDS $!"
  done
  wait $PIDS
  chk "8 pedidos HTTP simultáneos de EJ-0601 en 8 sesiones (8 procesos del servidor): un solo préstamo activo" '[ "$(consulta "SELECT COUNT(*) FROM prestamos p JOIN ejemplares e ON e.id = p.ejemplar_id WHERE e.codigo = '"'"'EJ-0601'"'"' AND p.fecha_devolucion IS NULL")" = 1 ]'
  AV=$(for k in 1 2 3 4 5 6 7 8; do codigo_en "$(curl -s -b "$TMP/sesion_$k.txt" "$BASE/prestamo.php")"; done | sort | uniq -c)
  echo "$AV" | sed 's/^/         /'
  chk "Las otras 7 sesiones recibieron ME-03" 'echo "$AV" | grep -q "7 ME-03"'
else
  echo "PENDIENTE La prueba HTTP simultánea no corre en este sistema: usá pruebas/prueba_carrera.php"
fi

chk "El servidor no registró errores de PHP" '! grep -qi -E "fatal|warning|notice|deprecated" "$LOG"'
echo "Entorno: $(uname -s) $(uname -r), $(php -r 'echo "PHP ".PHP_VERSION.", SQLite ".(new PDO("sqlite::memory:"))->query("SELECT sqlite_version()")->fetchColumn();'), curl $(curl --version | head -1 | cut -d" " -f2)"
echo
echo "Resultado: $ok de $total correctas"
[ "$ok" -eq "$total" ]

#!/usr/bin/env bash
# Comprobación de la BASE DEL ESTUDIANTE (E-6b). Uso: bash pruebas/prueba_base.sh   (desde base_estudiante/)
# Comprueba solo lo que la base trae preparado: instalación, esquema con sus protecciones, consulta pública que
# responde, ingreso del personal (ME-12), autorización por zona (ME-13), formulario del alta de ejemplar,
# persistencia, respaldo y restauración. NO exige las operaciones que construyen los estudiantes: esas responden
# «PENDIENTE» hasta que se hacen (Capítulos 10 a 13).
set -u
PUERTO=${PUERTO:-8773}
BASE="http://127.0.0.1:$PUERTO"
TMP=$(mktemp -d)
export BIBLIO_DB="$TMP/biblioteca.sqlite"
LOG="$TMP/servidor.log"; JAR="$TMP/c.txt"; JAR_D="$TMP/d.txt"
CLAVE=prueba-solo-local
ok=0; total=0
chk() { total=$((total+1)); if eval "$2"; then ok=$((ok+1)); echo "CORRECTO $1"; else echo "FALLA    $1"; fi; }
consulta() { php -r 'putenv("BIBLIO_DB=".$argv[1]); require "src/db.php"; echo conectar()->query($argv[2])->fetchColumn();' "$BIBLIO_DB" "$1"; }
arrancar() { php -S 127.0.0.1:$PUERTO -t public >> "$LOG" 2>&1 & SRV=$!; for i in $(seq 1 20); do curl -s -o /dev/null "$BASE/" && break; sleep 0.25; done; }
parar() { kill $SRV 2>/dev/null; wait $SRV 2>/dev/null; }
trap 'parar; rm -rf "$TMP"' EXIT
ficha() { curl -s -b "$2" -c "$2" "$BASE/$1" | grep -o 'name="csrf" value="[0-9a-f]*"' | head -1 | sed 's/.*value="//;s/"//'; }
ingresar() { T=$(ficha login.php "$2"); curl -s -o /dev/null -w "%{http_code} %{redirect_url}" -b "$2" -c "$2" -d csrf="$T" -d usuario="$1" -d clave="$3" "$BASE/login.php"; }
codigo_en() { echo "$1" | grep -o 'data-codigo="[A-Z]*-*[0-9]*"' | head -1 | sed 's/data-codigo="//;s/"//'; }

php verificar_entorno.php > "$TMP/entorno.txt"; R=$?
chk "verificar_entorno.php: el entorno tiene lo necesario" '[ $R = 0 ]'
php instalar.php --clave=$CLAVE > /dev/null
chk "Instalación: esquema 3 con datos ficticios (6 ejemplares, 4 lectores, 2 cuentas)" '[ "$(consulta "PRAGMA user_version")" = 3 ] && [ "$(consulta "SELECT COUNT(*) FROM ejemplares")" = 6 ] && [ "$(consulta "SELECT COUNT(*) FROM cuentas")" = 2 ]'
chk "El esquema trae las dos protecciones de la base: índice de RI-01 y disparadores del historial" '[ "$(consulta "SELECT COUNT(*) FROM sqlite_master WHERE name IN ('"'"'un_prestamo_activo_por_ejemplar'"'"', '"'"'prestamos_sin_borrado'"'"', '"'"'devolucion_unica'"'"')")" = 3 ]'
H1=$(sha256sum "$BIBLIO_DB" | cut -c1-64); php instalar.php > /dev/null 2>&1; R=$?
chk "Instalar de nuevo no borra la base existente (código 1, misma huella)" '[ $R = 1 ] && [ "$(sha256sum "$BIBLIO_DB" | cut -c1-64)" = "$H1" ]'
arrancar
C=$(curl -s -o /dev/null -w "%{http_code}" --get --data-urlencode "q=arroyo" "$BASE/")
chk "La consulta pública responde (200); OP-03 queda PENDIENTE hasta el Capítulo 13" '[ "$C" = 200 ]'
H=$(curl -s -w "%{http_code}" "$BASE/inicio.php")
chk "PT-04 sin sesión: 403 con ME-13" 'echo "$H" | grep -q "403$" && [ "$(codigo_en "$H")" = ME-13 ]'
T=$(ficha login.php "$JAR")
H=$(curl -s -b "$JAR" -c "$JAR" -d csrf="$T" -d usuario=bibliotecaria1 -d clave=equivocada "$BASE/login.php")
chk "Clave incorrecta: ME-12" '[ "$(codigo_en "$H")" = ME-12 ]'
R=$(ingresar bibliotecaria1 "$JAR" $CLAVE)
chk "La bibliotecaria ingresa y va a PT-04" 'echo "$R" | grep -q "^303 .*inicio.php"'
R=$(ingresar direccion1 "$JAR_D" $CLAVE)
H=$(curl -s -b "$JAR_D" -c "$JAR_D" -w "%{http_code}" "$BASE/lectores.php")
chk "La dirección no entra a PT-08: 403 con ME-13" 'echo "$H" | grep -q "403$" && [ "$(codigo_en "$H")" = ME-13 ]'
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/lectores.php")
chk "PT-08 tiene el formulario del alta de un ejemplar, con ficha CSRF" 'echo "$H" | grep -q "Código del ejemplar" && echo "$H" | grep -q "name=\"csrf\""'
T=$(ficha lectores.php "$JAR")
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$T" -d accion=alta_ejemplar -d codigo=EJ-0810 -d edicion=ED-0070 "$BASE/lectores.php"
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/lectores.php")
chk "El formulario llega al servidor y responde con el resultado de OA-01 (PENDIENTE hasta el Capítulo 10, o MA-01 si ya se completó)" '[ "$(codigo_en "$H")" = PENDIENTE ] || [ "$(codigo_en "$H")" = MA-01 ]'
php -r 'putenv("BIBLIO_DB=".$argv[1]); require "src/db.php"; conectar()->exec("INSERT INTO prestamos (ejemplar_id, lector_id, curso_al_prestar, fecha_salida, fecha_vencimiento) VALUES (1, 1, '"'"'2.º BTI'"'"', '"'"'2026-03-02'"'"', '"'"'2026-03-09'"'"')");' "$BIBLIO_DB"
parar; arrancar
chk "Persistencia: un dato guardado sigue después de reiniciar el servidor" '[ "$(consulta "SELECT COUNT(*) FROM prestamos")" = 1 ]'
parar
php respaldar.php > /dev/null; RESP=$(ls -t "$TMP"/respaldos/respaldo_*.sqlite | head -1)
chk "Respaldo verificado (E-11)" '[ -s "$RESP" ]'
php -r 'putenv("BIBLIO_DB=".$argv[1]); require "src/db.php"; conectar()->exec("UPDATE prestamos SET fecha_devolucion = '"'"'2026-03-05'"'"'");' "$BIBLIO_DB"
echo RESTAURAR | php restaurar.php "$RESP" > /dev/null 2>&1; R=$?
chk "Restauración probada (E-12): vuelve el préstamo activo y queda una copia de lo anterior" '[ $R = 0 ] && [ "$(consulta "SELECT COUNT(*) FROM prestamos WHERE fecha_devolucion IS NULL")" = 1 ] && ls "$TMP"/respaldos/antes_de_restaurar_*.sqlite > /dev/null 2>&1'
chk "El servidor no registró errores de PHP" '! grep -qi -E "fatal|warning|notice|deprecated" "$LOG"'
echo "Entorno: $(uname -s) $(uname -r), $(php -r 'echo "PHP ".PHP_VERSION.", SQLite ".(new PDO("sqlite::memory:"))->query("SELECT sqlite_version()")->fetchColumn();')"
echo; echo "Resultado: $ok de $total correctas"
[ "$ok" -eq "$total" ]

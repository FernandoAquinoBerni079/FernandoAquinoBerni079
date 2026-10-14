#!/usr/bin/env bash
# Prueba de punta a punta con el servidor incorporado de PHP.
# Uso: bash pruebas/prueba_http.sh   (desde la carpeta prototipo_v2/)
set -u
PUERTO=${PUERTO:-8771}
BASE="http://127.0.0.1:$PUERTO"
TMP=$(mktemp -d)
export BIBLIO_DB="$TMP/biblioteca.sqlite"
LOG="$TMP/servidor.log"
JAR="$TMP/cookies.txt"
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
ficha() { curl -s -b "$JAR" -c "$JAR" "$BASE/$1" | grep -o 'name="csrf" value="[0-9a-f]*"' | head -1 | sed 's/.*value="//;s/"//'; }

php instalar.php --clave=prueba-1234 > /dev/null
arrancar 1

# Consulta pública
H=$(curl -s "$BASE/")
chk "Catálogo público visible sin sesión" 'echo "$H" | grep -q "Cuentos de la selva"'
chk "Catálogo muestra ejemplares y disponibles por obra (3 y 3)" 'echo "$H" | grep -q "<td>Cuentos de la selva</td><td>Horacio Quiroga</td><td>Edición escolar 2019</td><td>3</td><td>3</td>"'
chk "El catálogo público no tiene formularios que modifiquen datos" '! echo "$H" | grep -q "method=\"post\""'

# Permisos mínimos
C=$(curl -s -o /dev/null -w "%{http_code}" "$BASE/operaciones.php")
chk "Operaciones sin sesión: acceso denegado (403)" '[ "$C" = 403 ]'
C=$(curl -s -o /dev/null -w "%{http_code}" -d accion=prestar -d ejemplar=EJ-0001 -d lector=L-001 "$BASE/operaciones.php")
chk "Préstamo enviado sin sesión: 403 y ningún préstamo creado" '[ "$C" = 403 ] && [ "$(consulta "SELECT COUNT(*) FROM prestamos")" = 0 ]'
T=$(ficha login.php)
H=$(curl -s -b "$JAR" -c "$JAR" -d csrf="$T" -d usuario=bibliotecaria -d clave=equivocada "$BASE/login.php")
chk "Clave incorrecta: no ingresa" 'echo "$H" | grep -q "Usuario o clave incorrectos"'
T=$(ficha login.php)
C=$(curl -s -o /dev/null -w "%{http_code}" -b "$JAR" -c "$JAR" -d csrf="$T" -d usuario=bibliotecaria -d clave=prueba-1234 "$BASE/login.php")
chk "Clave correcta: ingresa y redirige a operaciones (303)" '[ "$C" = 303 ]'

# Préstamo con protección CSRF y patrón POST-redirección-GET
C=$(curl -s -o /dev/null -w "%{http_code}" -b "$JAR" -c "$JAR" -d accion=prestar -d ejemplar=EJ-0001 -d lector=L-001 "$BASE/operaciones.php")
chk "Préstamo sin ficha CSRF: no se registra" '[ "$(consulta "SELECT COUNT(*) FROM prestamos")" = 0 ]'
T=$(ficha operaciones.php)
C=$(curl -s -o /dev/null -w "%{http_code}" -b "$JAR" -c "$JAR" -d csrf="$T" -d accion=prestar -d ejemplar=EJ-0001 -d lector=L-001 "$BASE/operaciones.php")
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/operaciones.php")
chk "Préstamo válido: 303 y aviso «Préstamo registrado»" '[ "$C" = 303 ] && echo "$H" | grep -q "Préstamo registrado"'
chk "El préstamo queda en el ejemplar EJ-0001" '[ "$(consulta "SELECT e.codigo FROM prestamos p JOIN ejemplares e ON e.id = p.ejemplar_id")" = EJ-0001 ]'
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$T" -d accion=prestar -d ejemplar=EJ-0001 -d lector=L-002 "$BASE/operaciones.php"
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/operaciones.php")
chk "Reenvío del formulario sobre el mismo ejemplar: rechazado con mensaje" 'echo "$H" | grep -q "El ejemplar ya tiene un préstamo activo"'
chk "Sigue habiendo un solo préstamo activo de EJ-0001" '[ "$(consulta "SELECT COUNT(*) FROM prestamos WHERE ejemplar_id = 1 AND fecha_devolucion IS NULL")" = 1 ]'
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/operaciones.php")
chk "Recargar la página no repite la operación (el aviso ya no aparece)" '! echo "$H" | grep -q "El ejemplar ya tiene"'
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$T" -d accion=prestar -d ejemplar=EJ-0002 -d lector=L-004 "$BASE/operaciones.php"
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/operaciones.php")
chk "Lector inactivo rechazado (RN-04)" 'echo "$H" | grep -q "inactivo"'
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$T" -d accion=prestar -d ejemplar=EJ-0004 -d lector=L-001 "$BASE/operaciones.php"
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$T" -d accion=prestar -d ejemplar=EJ-0005 -d lector=L-001 "$BASE/operaciones.php"
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/operaciones.php")
chk "Tercer préstamo del mismo lector rechazado (RN-02)" 'echo "$H" | grep -q "ya tiene 2 préstamos activos"'
H=$(curl -s "$BASE/")
chk "El catálogo público refleja la disponibilidad (Cuentos: 3 y 2)" 'echo "$H" | grep -q "<td>3</td><td>2</td>"'
V=$(consulta "SELECT fecha_vencimiento FROM prestamos WHERE id = 1")
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/operaciones.php?fecha=$(php -r 'echo date("Y-m-d", strtotime("+8 days"));')")
chk "Vencidos con fecha de referencia futura: aparece EJ-0001 (vence $V)" 'echo "$H" | sed -n "/id=\"vencidos\"/,/<\/table>/p" | grep -q "EJ-0001"'

# Devolución
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$T" -d accion=devolver -d prestamo_id=1 "$BASE/operaciones.php"
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/operaciones.php")
chk "Devolución registrada" 'echo "$H" | grep -q "Devolución registrada"'
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$T" -d accion=devolver -d prestamo_id=1 "$BASE/operaciones.php"
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/operaciones.php")
chk "Doble devolución rechazada (RN-05)" 'echo "$H" | grep -q "ya fue devuelto"'
chk "El préstamo devuelto se conserva en el historial" '[ "$(consulta "SELECT COUNT(*) FROM prestamos WHERE id = 1 AND fecha_devolucion IS NOT NULL")" = 1 ]'

# Entradas hostiles
H=$(curl -s --get --data-urlencode "q=<script>alert(1)</script>" "$BASE/")
chk "Texto con etiquetas se muestra escapado" '! echo "$H" | grep -q "<script>alert" && echo "$H" | grep -q "&lt;script&gt;"'
H=$(curl -s --get --data-urlencode "q=' OR 1=1 --" "$BASE/")
chk "Comilla en la búsqueda no altera la consulta (consulta parametrizada)" 'echo "$H" | grep -q "No hay resultados"'

# Cerrar sesión
curl -s -o /dev/null -b "$JAR" -c "$JAR" "$BASE/salir.php"
C=$(curl -s -o /dev/null -w "%{http_code}" -b "$JAR" -c "$JAR" "$BASE/operaciones.php")
chk "Después de salir, operaciones vuelve a estar denegado" '[ "$C" = 403 ]'

# Persistencia entre ejecuciones
ANTES=$(consulta "SELECT COUNT(*) FROM prestamos")
parar; arrancar 1
chk "Tras reiniciar el servidor se conservan los $ANTES préstamos" '[ "$(consulta "SELECT COUNT(*) FROM prestamos")" = "$ANTES" ]'

# Instalador protegido
H1=$(sha256sum "$BIBLIO_DB" | cut -c1-64)
php instalar.php > /dev/null 2>&1; R=$?
chk "Instalar de nuevo sin --reiniciar: se niega (código 1) y la base queda idéntica" '[ $R = 1 ] && [ "$(sha256sum "$BIBLIO_DB" | cut -c1-64)" = "$H1" ]'
echo "NO" | php instalar.php --reiniciar > /dev/null 2>&1; R=$?
chk "--reiniciar sin escribir REINICIAR: cancela y la base queda idéntica" '[ $R = 1 ] && [ "$(sha256sum "$BIBLIO_DB" | cut -c1-64)" = "$H1" ]'

# Respaldo y restauración
php respaldar.php > /dev/null
RESP=$(ls -t "$TMP"/respaldos/respaldo_*.sqlite | head -1)
chk "Respaldo creado con el servidor en marcha" '[ -s "$RESP" ]'
parar
echo "REINICIAR" | php instalar.php --reiniciar --clave=prueba-1234 > /dev/null 2>&1
chk "Con confirmación, --reiniciar guarda respaldo previo y deja la base vacía de préstamos" '[ -n "$(ls "$TMP"/respaldos/antes_de_reiniciar_*.sqlite 2>/dev/null)" ] && [ "$(consulta "SELECT COUNT(*) FROM prestamos")" = 0 ]'
cp "$RESP" "$BIBLIO_DB"
chk "Restauración manual del respaldo: vuelven los $ANTES préstamos" '[ "$(consulta "SELECT COUNT(*) FROM prestamos")" = "$ANTES" ]'

# Pedidos HTTP simultáneos: 8 sesiones distintas (con una sola sesión, PHP bloquea el
# archivo de sesión y atiende los pedidos de a uno). PHP_CLI_SERVER_WORKERS solo existe en Linux y macOS.
arrancar 8
for k in 1 2 3 4 5 6 7 8; do
  J="$TMP/sesion_$k.txt"
  T=$(curl -s -b "$J" -c "$J" "$BASE/login.php" | grep -o 'name="csrf" value="[0-9a-f]*"' | sed 's/.*value="//;s/"//')
  curl -s -o /dev/null -b "$J" -c "$J" -d csrf="$T" -d usuario=bibliotecaria -d clave=prueba-1234 "$BASE/login.php"
  curl -s -b "$J" -c "$J" "$BASE/operaciones.php" | grep -o 'name="csrf" value="[0-9a-f]*"' | head -1 | sed 's/.*value="//;s/"//' > "$TMP/ficha_$k"
done
PIDS=""
for k in 1 2 3 4 5 6 7 8; do
  L=$([ $((k % 2)) = 0 ] && echo L-002 || echo L-003)
  curl -s -o /dev/null -b "$TMP/sesion_$k.txt" -d csrf="$(cat "$TMP/ficha_$k")" -d accion=prestar -d ejemplar=EJ-0007 -d lector=$L "$BASE/operaciones.php" &
  PIDS="$PIDS $!"
done
wait $PIDS
chk "8 pedidos HTTP simultáneos, en 8 sesiones, del ejemplar EJ-0007: un solo préstamo activo" '[ "$(consulta "SELECT COUNT(*) FROM prestamos p JOIN ejemplares e ON e.id = p.ejemplar_id WHERE e.codigo = '"'"'EJ-0007'"'"' AND p.fecha_devolucion IS NULL")" = 1 ]'
AVISOS=$(for k in 1 2 3 4 5 6 7 8; do curl -s -b "$TMP/sesion_$k.txt" "$BASE/operaciones.php" | grep -o 'id="\(mensaje\|error\)">[^<]*'; done | sort | uniq -c)
echo "$AVISOS" | sed 's/^/         /'
chk "Las otras 7 sesiones recibieron el rechazo de RN-01" 'echo "$AVISOS" | grep -q "7 id=\"error\">El ejemplar ya tiene un préstamo activo."'

chk "El servidor no registró errores de PHP" '! grep -qi -E "fatal|warning|notice|deprecated" "$LOG"'
echo
echo "Resultado: $ok de $total correctas"
[ "$ok" -eq "$total" ]

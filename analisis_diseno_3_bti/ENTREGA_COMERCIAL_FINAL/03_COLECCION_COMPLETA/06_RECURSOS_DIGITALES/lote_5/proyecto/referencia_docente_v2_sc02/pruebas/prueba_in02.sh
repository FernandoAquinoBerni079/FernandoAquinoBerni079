#!/usr/bin/env bash
# Prueba de la incidencia IN-02 (lote 4, Tabla 13.3; real reproducida): después de un error en el alta de un lector,
# PT-08 tiene que volver a mostrar lo que se escribió, con el tipo elegido. Agregada con la corrección (referencia v2).
# Se corre desde la carpeta del sistema: bash pruebas/prueba_in02.sh. Usa una base temporal (BIBLIO_DB).
# Sobre la referencia del lote 4, que no tiene la corrección, tiene que FALLAR: así se reproduce la incidencia.
set -u
PUERTO=${PUERTO:-8781}
BASE="http://127.0.0.1:$PUERTO"
TMP=$(mktemp -d)
export BIBLIO_DB="$TMP/biblioteca.sqlite"
JAR="$TMP/cookies.txt"; CLAVE=prueba-solo-local
ok=0; total=0
chk() { total=$((total+1)); if eval "$2"; then ok=$((ok+1)); echo "CORRECTO $1"; else echo "FALLA    $1"; fi; }
ficha() { curl -s -b "$JAR" -c "$JAR" "$BASE/$1" | grep -o 'name="csrf" value="[0-9a-f]*"' | head -1 | sed 's/.*value="//;s/"//'; }
php instalar.php --clave=$CLAVE > /dev/null
php -S 127.0.0.1:$PUERTO -t public > "$TMP/servidor.log" 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null; wait $SRV 2>/dev/null; rm -rf "$TMP"' EXIT
for i in $(seq 1 20); do curl -s -o /dev/null "$BASE/" && break; sleep 0.25; done
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$(ficha login.php)" -d usuario=bibliotecaria1 -d clave=$CLAVE "$BASE/login.php"

# 1. Error MV-04: docente con curso. Lo escrito tiene que volver, con «Docente» elegido.
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$(ficha lectores.php)" -d accion=alta_lector -d codigo=LE-0990 \
  -d nombre="Docente de prueba (ficticio)" -d tipo=docente -d curso=6 "$BASE/lectores.php"
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/lectores.php")
chk "IN-02: después de MV-04 se muestra el mensaje" 'echo "$H" | grep -q "data-codigo=\"MV-04\""'
chk "IN-02: el tipo elegido (Docente) sigue elegido" 'echo "$H" | grep -q "value=\"docente\" selected"'
chk "IN-02: el código y el nombre escritos se conservan" 'echo "$H" | grep -q "value=\"LE-0990\"" && echo "$H" | grep -q "value=\"Docente de prueba (ficticio)\""'
chk "IN-02: la ficha CSRF no se conserva como dato escrito" '! echo "$H" | grep -q "name=\"csrf\" value=\"\""'
# 2. Los datos se muestran una sola vez: al volver a entrar, el formulario está vacío.
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/lectores.php")
chk "IN-02: al recargar, el formulario vuelve a estar vacío" '! echo "$H" | grep -q "value=\"LE-0990\""'
# 3. Si sale bien, no se conserva nada.
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$(ficha lectores.php)" -d accion=alta_lector -d codigo=LE-0991 \
  -d nombre="Docente de prueba 2 (ficticio)" -d tipo=docente -d curso= "$BASE/lectores.php"
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/lectores.php")
chk "IN-02: después de un alta correcta (MA-06), el formulario queda vacío" 'echo "$H" | grep -q "data-codigo=\"MA-06\"" && ! echo "$H" | grep -q "value=\"LE-0991\""'
# 4. Lo conservado es solo del alta de lector: otro formulario con error no llena el del lector.
curl -s -o /dev/null -b "$JAR" -c "$JAR" -d csrf="$(ficha lectores.php)" -d accion=alta_ejemplar -d codigo=EJ-12 \
  -d edicion=ED-0060 "$BASE/lectores.php"
H=$(curl -s -b "$JAR" -c "$JAR" "$BASE/lectores.php")
chk "IN-02: un error en otro formulario (MV-02) no llena el alta de lector" 'echo "$H" | grep -q "data-codigo=\"MV-02\"" && ! echo "$H" | grep -q "value=\"EJ-12\""'
echo
echo "Resultado: $ok de $total correctas"
[ $ok -eq $total ]

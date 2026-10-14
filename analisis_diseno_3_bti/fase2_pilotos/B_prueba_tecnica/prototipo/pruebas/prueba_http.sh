#!/usr/bin/env bash
# Prueba de punta a punta con el servidor incorporado de PHP.
# Uso: bash pruebas/prueba_http.sh   (desde la carpeta prototipo/)
set -u
PUERTO=${PUERTO:-8765}
BASE="http://127.0.0.1:$PUERTO"
export BIBLIO_DB="$(mktemp -d)/biblioteca.sqlite"
php instalar.php
php -S 127.0.0.1:$PUERTO -t public > /tmp/biblio_server.log 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null' EXIT
for i in 1 2 3 4 5 6 7 8 9 10; do curl -s -o /dev/null "$BASE/" && break; sleep 0.3; done
ok=0; total=0
chk() { total=$((total+1)); if eval "$2"; then ok=$((ok+1)); echo "CORRECTO $1"; else echo "FALLA    $1"; fi; }
H=$(curl -s "$BASE/")
chk "La página responde y muestra el catálogo" 'echo "$H" | grep -q "Cuentos de la selva"'
chk "Se ve con tildes (UTF-8)" 'echo "$H" | grep -q "Juan Ramón Jiménez"'
H=$(curl -s "$BASE/?q=Tahan")
chk "La búsqueda filtra por autor" 'echo "$H" | grep -q "El hombre que calculaba" && ! echo "$H" | grep -q "Platero"'
H=$(curl -s -d accion=prestar -d libro_id=2 -d lector_id=1 "$BASE/")
chk "Préstamo válido desde el formulario" 'echo "$H" | grep -q "Préstamo registrado"'
H=$(curl -s -d accion=prestar -d libro_id=2 -d lector_id=2 "$BASE/")
chk "Préstamo sin ejemplares se rechaza con mensaje" 'echo "$H" | grep -q "No quedan ejemplares"'
H=$(curl -s -d accion=prestar -d libro_id= -d lector_id=1 "$BASE/")
chk "Formulario incompleto se rechaza" 'echo "$H" | grep -q "Elegí un libro y un lector"'
H=$(curl -s -d accion=devolver -d prestamo_id=1 "$BASE/")
chk "Devolución desde el formulario" 'echo "$H" | grep -q "Devolución registrada"'
H=$(curl -s --get --data-urlencode "q=<script>alert(1)</script>" "$BASE/")
chk "Texto con etiquetas se muestra escapado (sin inyección HTML)" '! echo "$H" | grep -q "<script>alert" && echo "$H" | grep -q "&lt;script&gt;"'
H=$(curl -s --get --data-urlencode "q=' OR 1=1 --" "$BASE/")
chk "Búsqueda con comilla no rompe la consulta (sentencias preparadas)" 'echo "$H" | grep -q "<h2>Catálogo</h2>" && ! echo "$H" | grep -q "Cuentos de la selva"'
chk "El servidor no registró errores de PHP" '! grep -qi -E "fatal|warning|notice" /tmp/biblio_server.log'
echo
echo "Resultado: $ok de $total correctas"
[ "$ok" -eq "$total" ]

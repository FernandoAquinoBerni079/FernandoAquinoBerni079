#!/usr/bin/env bash
# Reproduce sobre una COPIA TEMPORAL de la referencia docente del lote 4 las incidencias IN-01 a IN-03 (Tabla 13.3)
# para clasificarlas como reales o simuladas en el plan del lote 5. No modifica lote_4/.
# Uso: bash lote_5_plan/reproducir_incidencias_u4.sh  →  lote_5_plan/reproduccion_incidencias_u4.txt
set -u
AQUI="$(cd "$(dirname "$0")" && pwd)"
REF="$AQUI/../lote_4/proyecto/referencia_docente"
T="$(mktemp -d)"; cp -r "$REF" "$T/r"; cd "$T/r"
php instalar.php --clave=demo-local >/dev/null
PUERTO=8791; php -S 127.0.0.1:$PUERTO -t public >/dev/null 2>&1 & SRV=$!; sleep 1
U="http://127.0.0.1:$PUERTO"; J="$T/j"
csrf() { curl -s -b "$J" -c "$J" "$1" | grep -o 'name="csrf" value="[^"]*"' | head -1 | sed 's/.*value="//;s/"//'; }
curl -s -b "$J" -c "$J" -o /dev/null -d "csrf=$(csrf $U/login.php)&usuario=bibliotecaria1&clave=demo-local" "$U/login.php"
{
echo "Entorno: $(uname -sr), PHP $(php -r 'echo PHP_VERSION;'), SQLite $(php -r 'echo (new PDO("sqlite::memory:"))->query("SELECT sqlite_version()")->fetchColumn();')"
echo "Copia temporal de lote_4/proyecto/referencia_docente; datos ficticios de ejemplo."
echo
echo "IN-01 (PT-07, fecha de referencia vacía):"
curl -s -b "$J" "$U/activos.php?fecha=" | grep -o 'data-codigo="[^"]*">[^<]*'
echo
echo "IN-02 (PT-08, alta de lector con error MV-04: ¿se conserva el tipo elegido?):"
curl -s -b "$J" -c "$J" -o /dev/null -d "csrf=$(csrf $U/lectores.php)&accion=alta_lector&codigo=LE-0400&nombre=X&tipo=docente&curso=6" "$U/lectores.php"
P="$(curl -s -b "$J" "$U/lectores.php")"
echo "$P" | grep -o 'data-codigo="[^"]*">[^<]*'
echo "$P" | grep -o '<select name="tipo">.*</select>' | head -1
echo "$P" | grep -q 'value="docente" selected' && echo "→ conserva «docente»" || echo "→ vuelve a «Estudiante» (primera opción): se reproduce"
echo
echo "IN-03 (PT-09, informe de un mes sin préstamos):"
curl -s -b "$J" "$U/informe.php?mes=2026-01" | sed -n '/<table/,/<\/table>/p' | sed 's/<[^>]*>/ /g' | tr -s ' \n' ' '; echo
curl -s -b "$J" "$U/informe.php?mes=2026-01" | grep -q 'data-codigo=' && echo "→ hay mensaje" || echo "→ sin mensaje de vacío: se reproduce"
} > "$AQUI/reproduccion_incidencias_u4.txt"
kill $SRV; rm -rf "$T"
cat "$AQUI/reproduccion_incidencias_u4.txt"

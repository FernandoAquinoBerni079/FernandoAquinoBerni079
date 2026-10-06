#!/bin/bash
# uso: run.sh archivo.psc in1 in2 ...  (el .psc se convierte a latin-1 antes de ejecutar)
P=/home/claude/pseint/pseint
f=$1; shift
iconv -f utf-8 -t latin1 "$f" > /tmp/claude-0/_run.psc
args=()
for x in "$@"; do args+=("--input=$(printf %s "$x" | iconv -f utf-8 -t latin1)"); done
LD_LIBRARY_PATH=$P/lib timeout 20 $P/bin/pseint /tmp/claude-0/_run.psc --profile=$P/perfiles/Flexible --nouser "${args[@]}" 2>&1 | iconv -f latin1 -t utf-8

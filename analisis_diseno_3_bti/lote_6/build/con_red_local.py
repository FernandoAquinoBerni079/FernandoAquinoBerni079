# -*- coding: utf-8 -*-
"""Dentro de un espacio de red nuevo (unshare -n) enciende solo la interfaz local y ejecuta el comando que sigue.
Las pruebas HTTP del proyecto necesitan localhost; ninguna otra red queda disponible.
Uso: unshare -n python3 -I con_red_local.py <comando> [argumentos]"""
import os, sys, socket, fcntl, struct
s = socket.socket()
fcntl.ioctl(s.fileno(), 0x8914, struct.pack('16sH14s', b'lo', 0x1 | 0x8 | 0x40, b'\0' * 14))   # SIOCSIFFLAGS
s.close()
os.execvp(sys.argv[1], sys.argv[1:])

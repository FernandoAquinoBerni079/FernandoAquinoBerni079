# -*- coding: utf-8 -*-
"""Cómo el lote corre las herramientas del docente (proyecto/herramientas/) sobre un paquete, tal como lo pide su LEEME:
  - inspeccionar(paquete): la inspección estática. Solo lee el paquete, así que corre directamente.
  - probar_aislado(paquete): las pruebas de la lista cerrada, siguiendo el procedimiento: el paquete se copia a una
    carpeta descartable de la cuenta sin privilegios nobody, y la herramienta (una copia confiable, fuera del paquete)
    corre con esa cuenta y en un espacio de red aislado (unshare -n: sin red). La carpeta se borra al terminar.
Las usan build/reproducir.py y build/pruebas_negativas.py. Si el entorno no permite aislar, probar_aislado no ejecuta
nada y lo informa."""
import os, shutil, subprocess, tempfile
AQUI = os.path.dirname(os.path.abspath(__file__))
L6 = os.path.dirname(AQUI)
HERRAMIENTAS = os.path.join(L6, 'proyecto', 'herramientas')
INSPECTOR = os.path.join(HERRAMIENTAS, 'inspeccionar_entrega.php')
EJECUTOR = os.path.join(HERRAMIENTAS, 'probar_en_aislamiento.php')
NADIE = 65534
SIN_PRIVILEGIOS = ['setpriv', '--reuid=%d' % NADIE, '--regid=%d' % NADIE, '--clear-groups']


def incoherencias(salida):
    return sorted(l.replace('INCOHERENCIA ', '', 1) for l in salida.split('\n') if l.startswith('INCOHERENCIA'))


def inspeccionar(paquete):
    p = subprocess.run(['php', INSPECTOR, paquete], capture_output=True, text=True, timeout=120)
    return p.returncode, p.stdout + p.stderr, incoherencias(p.stdout)


def puede_aislar():
    return os.name == 'posix' and os.geteuid() == 0 and all(shutil.which(c) for c in ('unshare', 'setpriv'))


def probar_aislado(paquete, limite=120, como_administrador=False, sin_red=True):
    """Devuelve (código de salida, salida, incoherencias, carpeta descartable usada). como_administrador=True corre la
    herramienta SIN bajar de cuenta (solo para la prueba negativa que comprueba que se niega)."""
    if not puede_aislar():
        return None, 'El entorno no permite aislar (unshare y setpriv con root): no se ejecutó ninguna prueba.', [], None
    base = tempfile.mkdtemp(prefix='ads_entrada_', dir='/tmp')
    try:
        os.chmod(base, 0o755)
        herramienta = os.path.join(base, 'probar_en_aislamiento.php')
        shutil.copy2(EJECUTOR, herramienta)
        os.chmod(herramienta, 0o644)
        copia = os.path.join(base, 'paquete')
        shutil.copytree(paquete, copia, symlinks=True, ignore=shutil.ignore_patterns('*.sqlite'))
        for d, _, fs in os.walk(copia):
            for x in [d] + [os.path.join(d, f) for f in fs]:
                os.lchown(x, NADIE, NADIE)
        cmd = (['unshare', '-n'] if sin_red else []) + ([] if como_administrador else SIN_PRIVILEGIOS) + \
            ['php', herramienta, copia, '--limite=%d' % limite]
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=limite * 4 + 60,
                           env={'PATH': '/usr/bin:/bin', 'TMPDIR': '/tmp', 'LANG': 'C.UTF-8'})
        return p.returncode, p.stdout + p.stderr, incoherencias(p.stdout), base
    finally:
        shutil.rmtree(base, ignore_errors=True)

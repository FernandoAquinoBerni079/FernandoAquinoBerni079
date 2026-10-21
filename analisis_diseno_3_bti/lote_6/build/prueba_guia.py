# -*- coding: utf-8 -*-
"""La guía como prueba (Capítulo 17): sigue ENTREGA/INSTALAR.md de un paquete al pie de la letra, en una copia limpia
y en procesos nuevos, sin usar nada que la guía no diga. Por cada paso ejecuta el comando escrito, escribe la entrada
que la guía indica y busca en la salida el «Resultado esperado». El paso del navegador se hace con una pedida HTTP.

Es una COMPROBACIÓN TÉCNICA de que la guía se puede seguir. No reemplaza la instalación por otro equipo, sin ayuda, que
evalúa una persona ajena al desarrollo (Encuentro 34): esa evidencia la produce el curso, en su laboratorio.
Únicas adaptaciones, que se informan en el resultado: el puerto 8000 se cambia por uno libre, y el nombre de ejemplo del
respaldo (AAAAMMDD_HHMMSS) por el del respaldo que creó el paso anterior, como pide la guía.

v1.1 (auditoría del lote 6): la guía es texto recibido, así que sus comandos no pasan por la consola del sistema. Solo
se ejecutan las formas conocidas (php <archivo>.php [argumentos] y php -S <dirección> -t <carpeta>), armadas como lista
de argumentos; cualquier otra línea es un paso fallido que no se ejecuta. Cuando el entorno lo permite (Linux, con
unshare y setpriv), todo corre en un espacio de red aislado (sin red; solo la interfaz local) y cada comando con la
cuenta sin privilegios nobody, sobre una copia descartable que se borra al terminar.
Uso: python3 lote_6/build/prueba_guia.py <carpeta del paquete>"""
import os, re, sys, json, glob, shlex, shutil, socket, subprocess, tempfile, time, urllib.request
NADIE = 65534
ULTIMO = {}   # cómo se aisló la última ejecución
SIN_PRIVILEGIOS = ['setpriv', '--reuid=%d' % NADIE, '--regid=%d' % NADIE, '--clear-groups']
FORMAS = (re.compile(r'^php -S \S+ -t \S+$'), re.compile(r'^php [\w./-]+\.php(?: [^;&|`$<>(){}*?\\]*)?$'))


def puede_aislar():
    return os.name == 'posix' and os.geteuid() == 0 and all(shutil.which(c) for c in ('unshare', 'setpriv'))


def _interfaz_local():
    """En un espacio de red nuevo la interfaz local está apagada: se enciende (no hay otra interfaz)."""
    import fcntl, struct
    s = socket.socket()
    fcntl.ioctl(s.fileno(), 0x8914, struct.pack('16sH14s', b'lo', 0x1 | 0x8 | 0x40, b'\0' * 14))   # SIOCSIFFLAGS
    s.close()


def _sin_red():
    try:
        socket.create_connection(('1.1.1.1', 53), timeout=2).close()
        return False
    except OSError:
        return True


def pasos(guia):
    out = []
    for bloque in re.split(r'^### ', guia, flags=re.M)[1:]:
        titulo = re.sub(r'^Paso \d+\. ', '', bloque.split('\n', 1)[0])
        cmd = re.search(r'```\n(.+?)\n```', bloque)
        nav = re.search(r'^Abrí en el navegador: (\S+)', bloque, re.M)
        esperado = re.search(r'^Resultado esperado: «(.+)»', bloque, re.M)
        entrada = re.search(r'^Cuando lo pida, escribí (\S+) y apretá Enter', bloque, re.M)
        out.append({'titulo': titulo, 'comando': cmd.group(1) if cmd else None, 'navegador': nav.group(1) if nav else None,
                    'detener': 'Detené el sistema.' in bloque, 'esperado': esperado.group(1) if esperado else None,
                    'entrada': entrada.group(1) if entrada else None})
    return out


def _puerto():
    s = socket.socket(); s.bind(('127.0.0.1', 0)); p = s.getsockname()[1]; s.close(); return p


def ejecutar(paquete):
    """Si se puede aislar y todavía no se está aislado, se vuelve a lanzar en un espacio de red nuevo."""
    if puede_aislar() and not os.environ.get('ADS_GUIA_AISLADA'):
        q = subprocess.run(['unshare', '-n', sys.executable, '-I', os.path.abspath(__file__), '--json',
                            os.path.abspath(paquete)], env=dict(os.environ, ADS_GUIA_AISLADA='1'),
                           capture_output=True, text=True, timeout=1800)
        datos = json.loads(q.stdout)
        ULTIMO['aislamiento'] = datos['aislamiento']
        return datos['pasos']
    ULTIMO['aislamiento'] = aislamiento()
    return _ejecutar(paquete)


def aislamiento():
    if os.environ.get('ADS_GUIA_AISLADA'):
        return 'espacio de red aislado (%s) y cuenta nobody, copia descartable' % ('sin red' if _sin_red() else 'CON RED')
    return 'sin aislar (el entorno no permite unshare y setpriv)'


def _ejecutar(paquete):
    aislada = bool(os.environ.get('ADS_GUIA_AISLADA'))
    if aislada:
        _interfaz_local()
    tmp = tempfile.mkdtemp(prefix='ads_guia_', dir='/tmp' if aislada else None)
    copia = os.path.join(tmp, 'paquete')
    shutil.copytree(paquete, copia, ignore=shutil.ignore_patterns('*.sqlite'), symlinks=True)
    entorno = {'PATH': '/usr/bin:/bin', 'HOME': copia, 'TMPDIR': copia, 'LANG': 'C.UTF-8'}
    previo = []
    if aislada:
        os.chmod(tmp, 0o755)
        for d, ds, fs in os.walk(copia):
            for x in [d] + [os.path.join(d, f) for f in fs]:
                os.lchown(x, NADIE, NADIE)
        previo = SIN_PRIVILEGIOS
    puerto, servidor, res = _puerto(), None, []
    try:
        for i, p in enumerate(pasos(open(os.path.join(copia, 'ENTREGA', 'INSTALAR.md'), encoding='utf8').read()), start=1):
            salida, nota = '', ''
            if p['comando'] and not any(f.match(p['comando']) for f in FORMAS):
                bien, salida = False, 'forma de comando no permitida: no se ejecuta'
            elif p['comando'] and ' -S ' in p['comando']:
                cmd = p['comando'].replace('localhost:8000', '127.0.0.1:%d' % puerto)
                servidor = subprocess.Popen(previo + shlex.split(cmd), cwd=copia, env=entorno, stdout=subprocess.DEVNULL,
                                            stderr=subprocess.DEVNULL)
                time.sleep(1.0)
                bien, nota = servidor.poll() is None, 'puerto %d en lugar de 8000' % puerto
            elif p['navegador']:
                url = p['navegador'].replace('localhost:8000', '127.0.0.1:%d' % puerto)
                try:
                    salida = urllib.request.urlopen(url, timeout=10).read().decode('utf8', 'replace')
                except Exception as e:   # noqa: BLE001 — se informa como falla del paso
                    salida = str(e)
                bien = bool(p['esperado']) and p['esperado'] in salida
            elif p['detener']:
                if servidor:
                    servidor.terminate(); servidor.wait(10)
                bien = servidor is not None and servidor.poll() is not None
            else:
                cmd = p['comando']
                if 'AAAAMMDD_HHMMSS' in cmd:
                    ultimo = sorted(glob.glob(os.path.join(copia, 'datos', 'respaldos', 'respaldo_*.sqlite')))
                    cmd = cmd.replace(re.search(r'\S*AAAAMMDD_HHMMSS\S*', cmd).group(0),
                                      os.path.relpath(ultimo[-1], copia) if ultimo else 'SIN_RESPALDO')
                    nota = 'nombre del respaldo del paso anterior'
                q = subprocess.run(previo + shlex.split(cmd), cwd=copia, env=entorno, capture_output=True, text=True, timeout=600,
                                   input=(p['entrada'] + '\n') if p['entrada'] else '')
                salida = q.stdout + q.stderr
                bien = q.returncode == 0 and (not p['esperado'] or p['esperado'] in salida)
            res.append({'paso': i, 'titulo': p['titulo'], 'comando': p['comando'] or p['navegador'] or 'detener',
                        'esperado': p['esperado'], 'correcto': bool(bien), 'nota': nota,
                        'salida': '' if bien else salida[-400:]})
    finally:
        if servidor and servidor.poll() is None:
            servidor.kill()
        shutil.rmtree(tmp, ignore_errors=True)
    return res


if __name__ == '__main__':
    if sys.argv[1] == '--json':
        r = _ejecutar(sys.argv[2]) if os.environ.get('ADS_GUIA_AISLADA') else ejecutar(sys.argv[2])
        print(json.dumps({'pasos': r, 'aislamiento': aislamiento()}, ensure_ascii=False))
        sys.exit(0)
    r = ejecutar(sys.argv[1])
    for x in r:
        print('%s Paso %d. %s — %s%s' % ('CORRECTO' if x['correcto'] else 'FALLA   ', x['paso'], x['titulo'], x['comando'],
                                         ' (%s)' % x['nota'] if x['nota'] else ''))
    print('Resultado: %d de %d pasos correctos' % (sum(x['correcto'] for x in r), len(r)))
    sys.exit(0 if all(x['correcto'] for x in r) else 1)

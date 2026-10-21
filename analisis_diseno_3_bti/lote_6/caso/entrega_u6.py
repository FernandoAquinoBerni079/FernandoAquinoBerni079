# -*- coding: utf-8 -*-
"""Fuente única de la entrega del equipo modelo (Unidad VI, Capítulo 17): los documentos del paquete de entrega
(guía de instalación, manual por tareas, límites, ficha de procedencia, borrador de licencia, acta y lista de entrega)
y las tablas que el libro y la guía docente muestran de ellos. Los archivos ENTREGA/*.md del paquete se generan desde
acá (build/armar_paquetes.py): el libro y el paquete dicen lo mismo.

Decisiones de Fernando (21-oct-2026): D-1, el paquete es una copia nueva de la referencia v2 con SC-02 del lote 5,
que no se modifica; D-2, licencia provisional de uso educativo institucional, presentada como BORRADOR (el aspecto
jurídico no se declara cerrado); cada recurso externo, con su licencia verificada según su versión exacta; no se
atribuye a la editorial código ajeno ni código original de los estudiantes. Datos ficticios."""
import os, sys, importlib.util
AQUI = os.path.dirname(os.path.abspath(__file__))
L6 = os.path.dirname(AQUI)
ADS = os.path.dirname(L6)
ORIGEN = os.path.join(ADS, 'lote_5', 'proyecto', 'referencia_docente_v2_sc02')
FECHA_CONSULTA = '21/10/2026'

VERSION = 'Entrega 1.0 (versión candidata v2 con SC-02, equipo modelo, caso Arapoty)'


def _cap16():
    """Ficha del Capítulo 16 (lote 5), solo para leer sus límites conocidos (Tabla 16.8), sin modificarla."""
    for p in (os.path.join(ADS, 'lote_5', 'caso'), os.path.join(ADS, 'lote_4', 'caso'), os.path.join(ADS, 'lote_3', 'caso'),
              os.path.join(ADS, 'lote_2', 'caso'), os.path.join(ADS, 'lote_1', 'caso')):
        if p not in sys.path:
            sys.path.append(p)
    spec = importlib.util.spec_from_file_location('cap16_l5', os.path.join(ADS, 'lote_5', 'build', 'cap16.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


# ------------------------------------------------------------------ 17.1 guía de instalación (pasos comprobables)
REQUISITOS = [
    'PHP 8.1 o superior con las extensiones pdo_sqlite y session (la guía de la base admite desde 7.4).',
    'Una carpeta en el disco local de la computadora, con permiso de escritura (no un pendrive ni una carpeta de red).',
    'Un navegador. No hace falta internet: el sistema funciona en la misma computadora.',
    'Para las pruebas automáticas por HTTP (opcionales): bash y curl.',
]
# (título, comando o acción, entrada que se escribe, resultado esperado: texto que tiene que aparecer, si falla)
PASOS = [
    ('Comprobar el entorno', 'php verificar_entorno.php', None, 'Esta computadora está lista para el prototipo.',
     'Si una línea dice FALTA, corregí ese punto (por ejemplo, activar pdo_sqlite en php.ini) y repetí el paso.'),
    ('Crear la base con los datos de ejemplo', 'php instalar.php', None, 'Base creada en:',
     'Si dice que ya existe una base, no la borres: seguí con el paso 3 o usá php instalar.php --reiniciar, que pide '
     'confirmación y guarda antes un respaldo.'),
    ('Iniciar el sistema', 'php -S localhost:8000 -t public', None, None,
     'Dejá esa ventana abierta mientras usás el sistema. Si el puerto 8000 está ocupado, usá otro: localhost:8001.'),
    ('Abrir el sistema en el navegador', 'NAVEGADOR http://localhost:8000', None, 'PT-01 Buscar un título',
     'Si el navegador no encuentra la página, revisá que la ventana del paso 3 siga abierta.'),
    ('Detener el sistema', 'DETENER', None, None, 'En la ventana del paso 3, Ctrl+C.'),
    ('Hacer un respaldo', 'php respaldar.php', None, 'Respaldo guardado y verificado',
     'Si dice que la base está en uso, detené el sistema (paso 5) y repetí.'),
    ('Comprobar que el respaldo se puede restaurar', 'php restaurar.php datos/respaldos/respaldo_AAAAMMDD_HHMMSS.sqlite',
     'RESTAURAR', 'Restauración terminada y comprobada',
     'Usá el nombre del respaldo que mostró el paso 6. Si no escribís RESTAURAR, no se cambia nada.'),
    ('Comprobar el paquete completo', 'php comprobar_entrega.php', None, 'Resultado: 0 incoherencias',
     'Si aparece una INCOHERENCIA, anotala en el acta de entrega: dice qué falta y dónde.'),
]
CUENTAS = ('El paso 2 muestra una sola vez las claves de las cuentas de demostración bibliotecaria1 y direccion1. '
           'Anotalas. Son de demostración: no se usan con datos reales sin cambiarlas.')


def instalar_md():
    out = ['# Guía de instalación, configuración y ejecución', '', 'Versión del paquete: ' + VERSION, '',
           '## Antes de empezar', ''] + ['- ' + r for r in REQUISITOS] + ['', CUENTAS, '', '## Pasos', '']
    for i, (t, cmd, entrada, esperado, si_falla) in enumerate(PASOS, start=1):
        out.append('### Paso %d. %s' % (i, t)); out.append('')
        if cmd.startswith('NAVEGADOR '):
            out.append('Abrí en el navegador: %s' % cmd.split(' ', 1)[1])
        elif cmd == 'DETENER':
            out.append('Detené el sistema.')
        else:
            out += ['```', cmd, '```']
        if entrada:
            out.append('Cuando lo pida, escribí %s y apretá Enter.' % entrada)
        if esperado:
            out.append('Resultado esperado: «%s»' % esperado)
        out.append('Si falla: ' + si_falla); out.append('')
    out += ['## Límites', '', 'Leé ENTREGA/LIMITES.md antes de usar el sistema con datos que no sean de prueba.', '']
    return '\n'.join(out)


# ------------------------------------------------------------------ 17.2 manual breve por tareas
# (código, tarea, quién, pantalla, pasos, mensajes que puede ver)
TAREAS = [
    ('T-01', 'Ingresar al sistema', 'Bibliotecaria o dirección', 'public/login.php',
     ['Abrí «Ingreso del personal».', 'Escribí tu usuario y tu clave.', 'Apretá «Ingresar».'],
     [('ME-12', 'El usuario o la clave no coinciden: revisalos y volvé a intentar.')]),
    ('T-02', 'Prestar un libro', 'Bibliotecaria', 'public/prestamo.php',
     ['Escribí el código del lector (LE-…) y el del ejemplar (EJ-…).', 'Revisá la fecha.', 'Apretá «Prestar».'],
     [('ME-04', 'Listo: el mensaje dice cuándo vence.'), ('ME-02', 'El lector llegó a su máximo: tiene que devolver uno.'),
      ('ME-03', 'El ejemplar ya está prestado: elegí otro.'), ('ME-01', 'El lector está inactivo: consultá con la dirección.')]),
    ('T-03', 'Registrar una devolución', 'Bibliotecaria', 'public/devolucion.php',
     ['Escribí el código del ejemplar que vuelve.', 'Revisá la fecha.', 'Apretá «Confirmar devolución».'],
     [('ME-07', 'Listo: el préstamo queda en el historial.'), ('ME-06', 'Ese ejemplar no estaba prestado: apartalo y revisá el historial.'),
      ('MV-10', 'La fecha es anterior a la salida: corregila.')]),
    ('T-04', 'Ver los préstamos activos y los vencidos', 'Bibliotecaria', 'public/activos.php',
     ['Escribí la fecha de referencia (año-mes-día).', 'Apretá «Ver».'],
     [('ME-10', 'No hay préstamos activos.'), ('MV-08', 'La fecha no es válida: escribila como 2026-03-09.')]),
    ('T-05', 'Sacar el informe del mes', 'Bibliotecaria o dirección', 'public/informe.php',
     ['Escribí el mes (año-mes).', 'Apretá «Ver informe».'],
     [('ME-14', 'Ese mes no tiene préstamos: el informe está vacío y no es un error.'),
      ('MV-11', 'El mes no es válido: escribilo como 2026-04.')]),
    ('T-06', 'Buscar un título', 'Cualquier persona, sin ingresar', 'public/index.php',
     ['Escribí una parte del título.', 'Apretá «Buscar».'],
     [('ME-08', 'No hay títulos con esas palabras: probá con otra parte.'), ('ME-09', 'Hay ejemplares, pero todos están prestados.')]),
    ('T-07', 'Dar de alta un lector', 'Bibliotecaria', 'public/lectores.php',
     ['En «Alta de un lector», escribí el código, el nombre y el tipo.', 'Si es estudiante, escribí el curso.', 'Apretá «Registrar el lector».'],
     [('MA-06', 'Listo.'), ('MV-03', 'Falta el curso del estudiante.'), ('MV-04', 'Los docentes no llevan curso.')]),
    ('T-08', 'Hacer un respaldo y restaurarlo', 'Responsable técnico', 'consola (pasos 6 y 7 de la guía)',
     ['Detené el sistema.', 'php respaldar.php.', 'Para volver a un respaldo: php restaurar.php con su nombre y escribí RESTAURAR.'],
     [('—', 'La restauración guarda antes una copia de la base actual en datos/respaldos/.')]),
]


def manual_md():
    out = ['# Manual breve por tareas', '', 'Cada tarea dice quién la hace, dónde, los pasos y qué significan los mensajes.', '']
    for cod, t, quien, pant, pasos, msgs in TAREAS:
        out += ['## %s. %s' % (cod, t), '', 'Quién: %s. Dónde: %s.' % (quien, pant), '']
        out += ['%d. %s' % (i, p) for i, p in enumerate(pasos, start=1)] + ['']
        out += ['- %s: %s' % (c, s) for c, s in msgs] + ['']
    return '\n'.join(out)


# ------------------------------------------------------------------ límites conocidos y pendientes
PENDIENTES = [
    ('Pruebas en Windows y en las computadoras del colegio (E-1 a E-12, P-13, concurrencia)', 'Pendiente',
     'La institución las hace con la ficha de entorno antes de usar el sistema'),
    ('Instalación por una persona ajena al desarrollo, siguiendo esta guía', 'Pendiente hasta el acta del Encuentro 34',
     'La hace otro equipo, sin ayuda, y la registra en el acta de entrega'),
    ('Uso con datos reales de lectores', 'No previsto',
     'El paquete trae datos ficticios; antes de usar datos reales hay que cambiar las claves y acordarlo con la institución'),
]


def limites():
    filas = [tuple(f) for f in _cap16().TABLA_168[1] if 'Instalación por otro equipo' not in f[0]]
    return filas + PENDIENTES


def limites_md():
    out = ['# Límites conocidos y pendientes', '', 'Versión: ' + VERSION, '',
           'Lo que este paquete no hace, o no se probó todavía. Un límite dicho no es una falla escondida.', '',
           '| Límite | Condición | Qué se hace |', '|---|---|---|']
    out += ['| %s | %s | %s |' % f for f in limites()]
    return '\n'.join(out) + '\n'


# ------------------------------------------------------------------ 17.3 procedencia y licencias (verificadas)
# (recurso, archivos, autor o titular, licencia o condición, fuente verificada, en el paquete)
PROCEDENCIA = [
    ('Código original de referencia', 'src/, public/, pruebas/, instalar.php, respaldar.php, restaurar.php, '
     'retirar_marca.php, verificar_entorno.php, comprobar_entrega.php',
     'Titulares del material editorial «Análisis y Diseño de Sistemas, 3.º BTI» (adaptado del Piloto B v2.3 de la colección)',
     'Borrador de uso educativo institucional (ENTREGA/LICENCIA_BORRADOR.md)', 'Registro de versiones del proyecto',
     'Se entrega'),
    ('Datos de ejemplo', 'src/datos_ejemplo.php', 'Inventados para el caso Arapoty (ficticios)',
     'La misma del código de referencia', 'Registro de versiones del proyecto', 'Se entrega'),
    ('Documentación de la entrega', 'LEEME.txt y ENTREGA/', 'Equipo modelo del libro', 'La misma del código de referencia',
     'Registro de versiones del proyecto', 'Se entrega'),
    ('PHP 8.3.6 (intérprete y extensión pdo_sqlite)', '—', 'The PHP Group y colaboradores',
     'The PHP License, version 3.01', 'Archivo LICENSE de php-src, etiqueta php-8.3.6 (consultado el %s)' % FECHA_CONSULTA,
     'No se entrega: la institución lo instala. Las distribuciones de PHP pueden incluir bibliotecas con licencias propias'),
    ('SQLite 3.45.1 (base de datos usada por pdo_sqlite)', '—', 'Autores de SQLite',
     'Dedicado al dominio público («The author disclaims copyright to this source code»)',
     'LICENSE.md de SQLite, etiqueta version-3.45.1, y sqlite.org/copyright.html (consultados el %s)' % FECHA_CONSULTA,
     'No se entrega: viene con PHP'),
    ('curl 8.5.0 (solo para la prueba HTTP opcional)', '—', 'Daniel Stenberg y colaboradores',
     'Licencia propia de curl («COPYRIGHT AND PERMISSION NOTICE»)', 'Archivo COPYING de curl, etiqueta curl-8_5_0 '
     '(consultado el %s)' % FECHA_CONSULTA, 'No se entrega'),
    ('GNU bash 5.2.21 (solo para las pruebas .sh)', '—', 'Free Software Foundation',
     'GPL versión 3 o posterior («License GPLv3+»)', 'Aviso del propio programa (bash --version) en el entorno de '
     'construcción', 'No se entrega'),
    ('Imágenes, iconos y fuentes tipográficas', '—', '—', '—', '—',
     'El paquete no tiene: la interfaz usa la fuente del sistema'),
]
PROCEDENCIA_NOTA = ('Las licencias de terceros se verificaron con su fuente primaria, según la versión exacta que usaron '
                    'las pruebas. Si la institución usa otra versión, hay que verificar la licencia de esa versión.')
FICHA_CAMPOS = ['Recurso', 'Archivos', 'Autor o titular', 'Licencia o condición', 'Fuente verificada y fecha', 'En el paquete']


def procedencia_md():
    out = ['# Ficha de procedencia y licencias', '', PROCEDENCIA_NOTA, '',
           '| ' + ' | '.join(FICHA_CAMPOS) + ' |', '|' + '---|' * len(FICHA_CAMPOS)]
    out += ['| ' + ' | '.join(f) + ' |' for f in PROCEDENCIA]
    out += ['', 'El código que escriban los estudiantes es de sus autores: no lo cubre esta ficha ni se atribuye a la '
            'editorial. Cada equipo registra su autoría en su propia ficha.', '']
    return '\n'.join(out)


LICENCIA = [
    'BORRADOR — Licencia de uso educativo institucional. Este texto es una propuesta provisional: el aspecto jurídico '
    'no está cerrado y requiere la revisión de los titulares y el asesoramiento que correspondan.',
    'Titulares: los titulares de los derechos del material editorial «Análisis y Diseño de Sistemas, 3.º BTI». Todos los '
    'derechos reservados.',
    'Qué cubre: el código original de referencia, los datos de ejemplo y la documentación que la ficha de procedencia '
    'marca con esta licencia. No cubre los componentes de terceros (PHP, SQLite, curl, bash), que tienen sus propias '
    'licencias, ni el código original de los estudiantes, que es de sus autores.',
    'Qué autoriza, solo dentro de la institución que adquirió el material: instalar, ejecutar, estudiar y modificar el '
    'proyecto para fines educativos.',
    'Qué no autoriza: la redistribución comercial del material editorial, ni su publicación o entrega fuera de la '
    'institución adquirente.',
    'Sin garantía: el proyecto es un prototipo educativo con datos ficticios y límites conocidos (ENTREGA/LIMITES.md).',
]


def licencia_md():
    return '\n\n'.join(['# Licencia (borrador)'] + LICENCIA) + '\n'


# ------------------------------------------------------------------ 17.4 acta de entrega simulada y lista de entrega
ACTA_CAMPOS = [
    ('Qué se entrega', 'Paquete con código, datos ficticios, pruebas y documentación (lista de entrega)'),
    ('Versión', VERSION),
    ('Equipo que entrega', ''),
    ('Equipo que recibe e instala (ajeno al desarrollo)', ''),
    ('Computadora, sistema y versiones', ''),
    ('Pasos de la guía: hecho, con dificultad o fallido, con el mensaje exacto', ''),
    ('Restauración de un respaldo', ''),
    ('Resultado de php comprobar_entrega.php', ''),
    ('Límites conocidos y pendientes que se informan', 'ENTREGA/LIMITES.md'),
    ('Observaciones del equipo receptor', ''),
    ('Ajustes que hizo el equipo autor y paso que se volvió a probar', ''),
    ('Firmas (equipo que entrega, equipo que recibe, docente)', ''),
]


def acta_md():
    out = ['# Acta de entrega (simulada)', '', 'Versión: ' + VERSION, '',
           'La completa el equipo que recibe el paquete, después de instalarlo sin ayuda.', '', '| Campo | Contenido |', '|---|---|']
    out += ['| %s | %s |' % (k, v) for k, v in ACTA_CAMPOS if k != 'Versión']
    return '\n'.join(out) + '\n'


ARCHIVOS_LISTA = [
    ('LEEME.txt', 'Qué es el paquete y por dónde empezar'),
    ('ENTREGA/INSTALAR.md', 'Guía de instalación, configuración y ejecución'),
    ('ENTREGA/MANUAL.md', 'Manual breve por tareas'),
    ('ENTREGA/LIMITES.md', 'Límites conocidos y pendientes'),
    ('ENTREGA/PROCEDENCIA.md', 'Ficha de procedencia y licencias'),
    ('ENTREGA/LICENCIA_BORRADOR.md', 'Licencia (borrador)'),
    ('ENTREGA/ACTA_ENTREGA.md', 'Acta de entrega para completar'),
    ('src/datos_ejemplo.php', 'Datos ficticios'),
    ('src/esquema.sql', 'Esquema de la base'),
    ('instalar.php', 'Instalación'), ('respaldar.php', 'Respaldo'), ('restaurar.php', 'Restauración'),
    ('comprobar_entrega.php', 'Comprobador de la entrega'),
]
PRUEBAS_LISTA = ['php pruebas/prueba_contratos.php', 'php pruebas/prueba_garantias.php', 'php pruebas/prueba_respaldo.php']
PRUEBAS_OPCIONALES = ['bash pruebas/prueba_http.sh (requiere bash y curl)', 'bash pruebas/prueba_in02.sh (requiere bash y curl)']


def lista_md(archivos=None, version=None):
    out = ['# Lista de entrega', '', 'Versión: ' + (version or VERSION), '', '## Archivos', '']
    out += ['- archivo: `%s` — %s' % a for a in (archivos or ARCHIVOS_LISTA)]
    out += ['', '## Pruebas que acompañan la entrega (las ejecuta php comprobar_entrega.php)', '']
    out += ['- prueba: `%s`' % p for p in PRUEBAS_LISTA]
    out += ['', '## Pruebas opcionales', ''] + ['- %s' % p for p in PRUEBAS_OPCIONALES]
    return '\n'.join(out) + '\n'


def leeme_txt(titulo='Sistema de préstamos de la biblioteca escolar — PAQUETE DE ENTREGA', version=None):
    return '\n'.join([titulo, 'Versión: ' + (version or VERSION), 'Datos ficticios. Prototipo educativo.', '',
                      'Por dónde empezar:', '  1. ENTREGA/INSTALAR.md   (instalación, paso a paso)',
                      '  2. ENTREGA/MANUAL.md     (cómo se usa, por tareas)', '  3. ENTREGA/LIMITES.md    (lo que no hace o no se probó)',
                      '', 'Comprobar el paquete:   php comprobar_entrega.php', '',
                      'Procedencia y licencia: ENTREGA/PROCEDENCIA.md y ENTREGA/LICENCIA_BORRADOR.md (borrador).', ''])


DOCUMENTOS = {'ENTREGA/INSTALAR.md': instalar_md, 'ENTREGA/MANUAL.md': manual_md, 'ENTREGA/LIMITES.md': limites_md,
              'ENTREGA/PROCEDENCIA.md': procedencia_md, 'ENTREGA/LICENCIA_BORRADOR.md': licencia_md,
              'ENTREGA/ACTA_ENTREGA.md': acta_md, 'ENTREGA/LISTA_ENTREGA.md': lista_md, 'LEEME.txt': leeme_txt}

# -*- coding: utf-8 -*-
"""Cierre de ENTREGA_COMERCIAL_FINAL/ (después de auditoria_final.py): informe final de auditoría, validaciones realizadas,
resolución de discrepancias, LEEME, índice general de archivos, manifiesto SHA-256 y los cinco ZIP de entrega con su
SHA256SUMS.txt. Comprueba cada ZIP (integridad, mismo contenido que la carpeta, sin archivos reservados ni datos DR/V6).
Uso: python3 -B analisis_diseno_3_bti/edicion_v1_0/build/cierre_entrega.py
"""
import hashlib, json, os, re, sys, zipfile
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__)); ED = os.path.dirname(AQUI); ADS = os.path.dirname(ED)
sys.path.insert(0, AQUI)
import pymupdf
import textos_entrega as TX
import cubiertas as CU

ENT = os.path.join(ADS, 'ENTREGA_COMERCIAL_FINAL'); QC = os.path.join(ENT, '05_CONTROL_DE_CALIDAD')
ZIPS = os.path.join(ADS, 'ENTREGA_COMERCIAL_FINAL_ZIP'); SAL = os.path.join(ED, 'salida')
CARPETAS = ['01_ESTUDIANTE', '02_DOCENTE', '03_COLECCION_COMPLETA', '04_PRESENTACION_COMERCIAL', '05_CONTROL_DE_CALIDAD']
FECHA = '22 de octubre de 2026'
R = json.load(open(os.path.join(QC, 'RESULTADOS_DE_CONTROLES.json'), encoding='utf8'))
C = json.load(open(os.path.join(SAL, 'cifras_entrega.json'), encoding='utf8'))
CP = json.load(open(os.path.join(SAL, 'CONTROLES_PLANIFICACION.json'), encoding='utf8'))
FALLOS = []


def sha(ruta):
    h = hashlib.sha256()
    with open(ruta, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def archivos(base):
    for dp, ds, fs in os.walk(base):
        ds.sort()
        for f in sorted(fs):
            yield os.path.relpath(os.path.join(dp, f), base)


def detalle(ruta):
    if ruta.endswith('.pdf'):
        d = pymupdf.open(ruta); r = d[0].rect
        return '%d pp · %.0f × %.0f mm' % (len(d), r.width / 72 * 25.4, r.height / 72 * 25.4)
    return ''


def control(desc, ok, extra=''):
    print(('ok    ' if ok else 'FALLA ') + desc + ('' if ok else '  →  %s' % extra))
    if not ok:
        FALLOS.append(desc)
    return {'detalle': desc, 'resultado': 'ok' if ok else 'falla'}


# ---------------------------------------------------------------- 1. resolución de discrepancias
DISC = [
    ('h', 'Criterio general'),
    ('p', 'Ninguna discrepancia era un error de contenido: en todos los casos el registro de controles (archivo JSON) es la fuente '
          'que manda, y los informes en prosa repetían una cifra de una corrida intermedia o contaban otra cosa. No se cambió '
          'ningún contenido aprobado para cerrarlas; se fijó qué cuenta cada cifra.'),
    ('t', (['Discrepancia', 'Qué cuenta cada cifra', 'Cifra vigente en v1.0', 'Fuente'], [
        ['77 frente a 78 referencias a instrumentos (planificación v0.1)',
         '77 aparece en ESTRUCTURA_Y_ALINEACION.md, escrito con una corrida intermedia. El registro final de la planificación '
         '(CONTROLES_PLANIFICACION.json, bloque F) comprobó 78 referencias, todas en su página.',
         '79: la v1.0 separa el «Mapa de apoyos del curso (modelo)» (guía, p. 7) de las claves del diagnóstico de entrada en el '
         'encuentro 1. Las 79 están en la página que indican.',
         'edicion_v1_0/salida/CONTROLES_PLANIFICACION.json, bloque F'],
        ['15 listas de cotejo frente a 16 encuentros con práctica',
         '«15 listas de cotejo en clase» aparece en ESTRUCTURA_Y_ALINEACION.md, escrito con una corrida intermedia. El registro '
         'final comprobó 16 encuentros con práctica en clase (Prácticas 1 a 15 y 17), cada uno con su lista de cotejo.',
         '16 encuentros con práctica en clase y 16 listas de cotejo. Las Prácticas 9 y 13 (complementos editoriales) también se '
         'citan como complemento, por eso hay 18 citas de práctica en total.',
         'CONTROLES_PLANIFICACION.json, bloque E'],
        ['51 frente a 57 instrumentos de la guía',
         '51 son las filas de la tabla «Instrumentos del año»; 57 son las ubicaciones que verificó el control de impresión: esas 51 '
         'más las 6 tablas de calendario.',
         '51 instrumentos + 6 calendarios = 57 ubicaciones, sin fallos.',
         'planificacion/00_cierre_v0_2/ADENDA_CIERRE_EDITORIAL_v0_2.md, §1'],
        ['Rótulo del manifiesto de la colección v0.2',
         'coleccion/MANIFIESTO_COLECCION.json dice «documentos anuales v0.1» aunque acompaña al cierre v0.2 (commit 88c5cb5). Los '
         '160 SHA-256 coinciden con los archivos de ese commit.',
         'El rótulo no se corrige en el archivo para no alterar una versión cerrada; esta tabla deja constancia. La v1.0 tiene su '
         'propio manifiesto (05_CONTROL_DE_CALIDAD/MANIFIESTO_SHA256.json).',
         'ADENDA_CIERRE_EDITORIAL_v0_2.md, §2'],
        ['160 archivos del manifiesto frente a 101 entradas del ZIP v0.2',
         'El ZIP lleva 97 archivos de entrega + el manifiesto + 3 carpetas = 101 entradas; los otros 63 archivos del manifiesto '
         'son intermedios de construcción que no se distribuyen.',
         'Los ZIP v1.0 se describen en el índice general de archivos y en SHA256SUMS.txt.',
         'ADENDA_CIERRE_EDITORIAL_v0_2.md, §2'],
    ], [3, 5, 4, 3])),
    ('h', 'Carga horaria'),
    ('p', 'Confirmada por el titular: 5 horas cátedra semanales, 36 encuentros, 180 HC. La adaptación a 28 encuentros se conserva '
          'como alternativa (recuadros «Si el calendario se acorta» del libro y sección correspondiente de la guía).'),
]


# ---------------------------------------------------------------- 2. validaciones realizadas y no realizadas
def validaciones():
    no_ej = [x['detalle'] for v in R['controles'].values() for x in v if x['resultado'] == 'no ejecutado']
    t = ['# Validaciones realizadas — edición comercial v1.0', '', 'Fecha: %s.' % FECHA, '',
         '## Realizadas (en el entorno de construcción, Linux)', '',
         '| Validación | Cómo | Resultado |', '|---|---|---|',
         '| Auditoría final de la entrega | `edicion_v1_0/build/auditoria_final.py` (%d controles) | %d fallos |' % (R['total'], len(R['fallos'])),
         '| Auditoría de la planificación | `edicion_v1_0/build/plan/controles_plan.py` (%d controles) | %d fallos |' % (CP['total'], len(CP['fallos'])),
         '| Fidelidad al contenido aprobado | Texto de cada página del libro y de la guía v1.0 comparado con v0.2 desde la página 2 | Idéntico |',
         '| Renglones del cuaderno | Medición en el PDF de la distancia entre renglones | 8 mm (mediana) |',
         '| Compatibilidad de fuentes | Calibri reemplazada por Carlito, Liberation Sans y DejaVu Sans; conversión a PDF | Ver PRUEBA_DE_FUENTES.json |',
         '| Ortografía | Diccionario Hunspell de español con regla de voseo | 0 errores reales; formas no reconocidas listadas |',
         '| Legibilidad de código y tablas | Render a 220 ppp de las páginas con código de 7,5 pt | Nítido |',
         '| Datos reservados | Búsqueda en todo el texto de la entrega de los textos y códigos del conjunto DR y de las variantes V6 | Ninguno presente |',
         '| ZIP de entrega | Prueba de integridad, contenido idéntico a la carpeta, búsqueda de archivos reservados | Ver INFORME_FINAL_DE_AUDITORIA |',
         '| Manifiesto | SHA-256 de cada archivo de la entrega | MANIFIESTO_SHA256.json |', '',
         '## No realizadas (requieren acceso o intervención que este entorno no tiene)', '',
         '| Validación | Por qué no se hizo | Quién la hace |', '|---|---|---|',
         '| Apertura y edición de los DOCX en Microsoft Word sobre Windows | No hay acceso a Windows ni a Word | Titular, antes de la venta |',
         '| Prueba de campo del entorno técnico (PHP, SQLite) en las computadoras de la institución (E-1 a E-12) | Solo se probó en Linux | Docente, en la institución |',
         '| Prueba de impresión física (prueba de color, encuadernación, lomo) | No hay imprenta | Imprenta, con la prueba de color firmada |',
         '| Revisión jurídica (titularidad, licencia del código, condiciones de uso) | Requiere un profesional | Abogado de propiedad intelectual |',
         '| Consulta directa a los sitios oficiales (DINAPI, Agencia Paraguaya del ISBN, Biblioteca Nacional, DNIT) | Los sitios no respondieron desde el entorno; se usaron resúmenes de búsqueda | Titular o su asesor |',
         '| ISBN y depósito legal | Los trámites los hace el editor | Editor |', '']
    if no_ej:
        t += ['## Controles automáticos no ejecutados', ''] + ['- %s' % x for x in no_ej] + ['']
    t += ['Ninguna de las validaciones de la segunda tabla se declara cumplida en ningún documento de la entrega.', '']
    return '\n'.join(t)


# ---------------------------------------------------------------- 3. LEEME e índice
LEEME = """# Análisis y Diseño de Sistemas · 3.º BTI — Edición comercial v1.0

Colección anual para el Plan Optativo (36 encuentros, 180 horas cátedra, 5 HC semanales): libro del estudiante, cuaderno de
prácticas, guía docente con solucionario, plan anual y 36 planes de clase.

| Carpeta | Para quién | Contenido |
|---|---|---|
| 01_ESTUDIANTE | Estudiante | Libro y cuaderno en PDF digital, instrucciones |
| 02_DOCENTE | Docente | Guía, plan anual y planes en PDF digital y DOCX editable, recursos digitales del proyecto, instrucciones |
| 03_COLECCION_COMPLETA | Imprenta e institución | Los cinco productos: interior y cubierta de impresión, PDF digital y DOCX editable |
| 04_PRESENTACION_COMERCIAL | Titular | Descripción y fichas técnicas, portadas y contraportadas, textos para WhatsApp y redes, propuesta de comercialización, condiciones de entrega y uso, licencias y atribuciones |
| 05_CONTROL_DE_CALIDAD | Titular | Informe final de auditoría, resultados, validaciones realizadas, registro de licencias, manifiesto SHA-256, instrucciones de impresión, derechos y requisitos legales |

**Estado:** edición técnicamente cerrada. La venta **no** está habilitada hasta completar los requisitos de
`05_CONTROL_DE_CALIDAD/DERECHOS_Y_REQUISITOS_LEGALES.pdf` (titular y editor, ISBN, revisión jurídica).

El conjunto DR y las variantes V6 son materiales reservados del docente: **no** están en esta entrega ni en ningún ZIP
público. Las capacidades C1 a C10 son una propuesta para el programa institucional: no es un programa oficial ni está
aprobado por el MEC.

El índice completo de archivos está en `03_COLECCION_COMPLETA/INDICE_GENERAL_DE_ARCHIVOS.md`.
"""


def indice():
    t = ['# Índice general de archivos — edición comercial v1.0', '',
         'Todos los archivos de ENTREGA_COMERCIAL_FINAL/, por carpeta. El SHA-256 de cada uno está en '
         '05_CONTROL_DE_CALIDAD/MANIFIESTO_SHA256.json.', '']
    for c in CARPETAS:
        fs = list(archivos(os.path.join(ENT, c)))
        rec = [f for f in fs if 'RECURSOS_DIGITALES' in f]
        t += ['## %s (%d archivos)' % (c, len(fs)), '', '| Archivo | Tamaño | Detalle |', '|---|---|---|']
        for f in fs:
            if f in rec:
                continue
            r = os.path.join(ENT, c, f)
            t.append('| %s | %.1f MB | %s |' % (f, os.path.getsize(r) / 1e6, detalle(r)) if os.path.getsize(r) > 1e5 else
                     '| %s | %.0f kB | %s |' % (f, os.path.getsize(r) / 1e3, detalle(r)))
        if rec:
            raiz = sorted(set(f.split('RECURSOS_DIGITALES')[0] + 'RECURSOS_DIGITALES' for f in rec))
            t.append('| %s/ | %d archivos | Proyecto PHP de referencia y del estudiante, casos e instrumentos de los lotes 4 a 6 (ver LEEME_RECURSOS.md) |'
                     % (', '.join(raiz), len(rec)))
        t.append('')
    t += ['## Raíz', '', '- LEEME.md', '']
    return '\n'.join(t)


# ---------------------------------------------------------------- 4. informe final
def informe(zips):
    filas = []
    for b, v in R['controles'].items():
        filas.append('| %s | %d | %d | %d |' % (b, len(v), sum(x['resultado'] == 'correcto' for x in v),
                                                sum(x['resultado'] not in ('correcto', 'no ejecutado') for x in v)))
    t = ['# Informe final de auditoría — edición comercial v1.0', '', 'Fecha: %s. Rama `claude/libros-5z31jx`.' % FECHA, '',
         '## Resultado', '',
         '- Auditoría de la entrega: **%d controles, %d fallos**.' % (R['total'], len(R['fallos'])),
         '- Auditoría de la planificación: **%d controles, %d fallos**.' % (CP['total'], len(CP['fallos'])),
         '- Cierre de la entrega y ZIP: **%d controles, %d fallos**.' % (len(zips['controles']), len(FALLOS)), '',
         '| Bloque | Controles | Correctos | Fallos |', '|---|---|---|---|'] + filas + ['',
         '## Productos', '', '| Producto | Páginas | Hojas | Lomo (mm) | Formatos |', '|---|---|---|---|---|']
    for k in CU.ORDEN:
        t.append('| %s | %d | %d | %.1f | %s |' % (CU.PRODUCTOS[k]['nombre'], C['paginas'][k], C['hojas'][k], C['lomo'][k],
                                                 C['productos'][k]['formatos']))
    t += ['', '## Correcciones hechas en esta corrida', '',
          '- Página 1 del libro y del cuaderno: se explica qué es «Work», porque el texto lo cita (secuencia y evidencias). '
          'Desde la página 2, el texto es idéntico al de v0.2.',
          '- Instrumento del encuentro 1: el «Mapa de apoyos del curso (modelo)» se cita aparte de las claves del diagnóstico (79 referencias).',
          '- Cuaderno: un renglón más por respuesta, interlineado exacto de 8 mm, índice actualizado.',
          '- Rótulo «Biblioteca Comercial 2026» reemplazado por «Edición 2026»; datos de edición con campos «[a completar por el titular]».',
          '', '## Discrepancias', '', 'Ver RESOLUCION_DE_DISCREPANCIAS.pdf: ninguna era un error de contenido.', '',
          '## ZIP de entrega', '', 'Una carpeta por ZIP, más el LEEME. El SHA-256 de cada ZIP está en SHA256SUMS.txt, junto a los ZIP '
          '(no puede figurar acá: este informe va dentro del ZIP 05).', '', '| ZIP | Entradas |', '|---|---|']
    for z in zips['zips']:
        t.append('| %s | %d |' % (z['nombre'], z['archivos']))
    t += ['', '## Controles del cierre', ''] + ['- %s: %s' % (x['resultado'], x['detalle']) for x in zips['controles']]
    t += ['', '## Pendiente (no técnico)', '',
          'La venta no está habilitada: falta identificar al titular y al editor, la revisión jurídica y el ISBN. Ver '
          'DERECHOS_Y_REQUISITOS_LEGALES.pdf y VALIDACIONES_REALIZADAS.md.', '']
    return '\n'.join(t)


def md_a_pdf(md, nombre, titulo):
    bloques, tabla = [], None
    for linea in md.split('\n')[1:]:
        if linea.startswith('|'):
            celdas = [c.strip().replace('`', '').replace('**', '') for c in linea.strip('|').split('|')]
            if set(''.join(celdas)) <= set('-'):
                continue
            if tabla is None:
                tabla = [celdas, []]
            else:
                tabla[1].append(celdas)
            continue
        if tabla:
            bloques.append(('t', (tabla[0], tabla[1], [1] * len(tabla[0])))); tabla = None
        x = linea.replace('**', '').replace('`', '')
        if x.startswith('## '): bloques.append(('h', x[3:]))
        elif x.startswith('- '): bloques.append(('ul', [x[2:]]))
        elif x.strip(): bloques.append(('p', x))
    if tabla:
        bloques.append(('t', (tabla[0], tabla[1], [1] * len(tabla[0]))))
    TX.render(nombre, titulo, bloques, QC)
    os.remove(os.path.join(QC, nombre + '.docx'))


# ---------------------------------------------------------------- 5. manifiesto y ZIP
def reservados():
    claves = []
    for ruta, et in (('/home/user/ADS_LOTE5_RESERVADO_DOCENTE/dr.json', 'DR'),
                     ('/home/user/ADS_LOTE6_RESERVADO_DOCENTE/variantes_v6.json', 'V6')):
        if os.path.exists(ruta):
            d = json.load(open(ruta, encoding='utf8'))
            claves += [v['situacion'][:40] for v in d] if et == 'V6' else [x[0] for k in ('obras', 'ediciones', 'ejemplares', 'lectores') for x in d[k]]
    return claves


def zips():
    os.makedirs(ZIPS, exist_ok=True)
    for f in os.listdir(ZIPS):
        os.remove(os.path.join(ZIPS, f))
    claves = reservados(); res = {'zips': [], 'controles': []}
    prohib = re.compile(r'(^|/)(dr\.json|variantes_v6\.json|comprobacion_(dr|v6)\.txt)$|__pycache__|\.pyc$|\.sqlite3?$|\.db$|~\$|\.DS_Store$|\.bak$|~$')
    for c in CARPETAS:
        nombre = 'ADS_3BTI_v1_0_%s.zip' % c; ruta = os.path.join(ZIPS, nombre)
        fs = list(archivos(os.path.join(ENT, c)))
        with zipfile.ZipFile(ruta, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            z.write(os.path.join(ENT, 'LEEME.md'), 'ADS_3BTI_v1_0/LEEME.md')
            for f in fs:
                z.write(os.path.join(ENT, c, f), 'ADS_3BTI_v1_0/%s/%s' % (c, f))
        with zipfile.ZipFile(ruta) as z:
            malo = z.testzip(); nombres = z.namelist()
            iguales = all(hashlib.sha256(z.read('ADS_3BTI_v1_0/%s/%s' % (c, f))).hexdigest() == sha(os.path.join(ENT, c, f)) for f in fs)
            texto = []
            for n in nombres:
                if n.endswith(('.md', '.txt', '.php', '.py', '.sql', '.sh', '.json', '.csv', '.html', '.css')):
                    texto.append(z.read(n).decode('utf8', 'ignore'))
                elif n.endswith('.pdf'):
                    texto.append(' '.join(p.get_text() for p in pymupdf.open(stream=z.read(n), filetype='pdf')))
            texto = '\n'.join(texto)
        res['controles'].append(control('%s: íntegro (testzip) y con los %d archivos de la carpeta, byte a byte' % (nombre, len(fs)),
                                        malo is None and iguales and len(nombres) == len(fs) + 1, malo))
        res['controles'].append(control('%s: sin archivos reservados, temporales ni bases de datos' % nombre,
                                        not [n for n in nombres if prohib.search(n)]))
        res['controles'].append(control('%s: ninguno de los %d textos o códigos DR/V6 en su contenido' % (nombre, len(claves)),
                                        bool(claves) and not [k for k in claves if k in texto]))
        res['controles'].append(control('%s: menos de 95 MB (límite de GitHub: 100 MB por archivo)' % nombre, os.path.getsize(ruta) < 95e6))
        res['zips'].append({'nombre': nombre, 'archivos': len(nombres), 'bytes': os.path.getsize(ruta), 'sha256': sha(ruta)})
    if not claves:
        res['controles'].append(control('Rutas privadas DR/V6 disponibles para la búsqueda', False))
    with open(os.path.join(ZIPS, 'SHA256SUMS.txt'), 'w', encoding='utf8') as f:
        for z in res['zips']:
            f.write('%s  %s\n' % (z['sha256'], z['nombre']))
    return res


def manifiesto():
    m = {'edicion': 'Análisis y Diseño de Sistemas · 3.º BTI · edición comercial v1.0', 'fecha': FECHA,
         'nota': 'SHA-256 de cada archivo de ENTREGA_COMERCIAL_FINAL/ (el manifiesto no se incluye a sí mismo).', 'archivos': {}}
    for f in archivos(ENT):
        if f != os.path.join('05_CONTROL_DE_CALIDAD', 'MANIFIESTO_SHA256.json'):
            m['archivos'][f] = {'bytes': os.path.getsize(os.path.join(ENT, f)), 'sha256': sha(os.path.join(ENT, f))}
    json.dump(m, open(os.path.join(QC, 'MANIFIESTO_SHA256.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    return len(m['archivos'])


if __name__ == '__main__':
    if R['fallos'] or CP['fallos']:
        sys.exit('La auditoría tiene fallos: no se cierra la entrega.')
    TX.render('RESOLUCION_DE_DISCREPANCIAS', 'Resolución de discrepancias y criterios de conteo', DISC, QC)
    os.remove(os.path.join(QC, 'RESOLUCION_DE_DISCREPANCIAS.docx'))
    open(os.path.join(QC, 'VALIDACIONES_REALIZADAS.md'), 'w', encoding='utf8').write(validaciones())
    open(os.path.join(ENT, 'LEEME.md'), 'w', encoding='utf8').write(LEEME)
    # informe provisional para que figure en el índice y en el ZIP; se reescribe con los resultados de los ZIP
    for nombre in ('INFORME_FINAL_DE_AUDITORIA.md', 'MANIFIESTO_SHA256.json'):
        open(os.path.join(QC, nombre), 'w').write('')
    md_a_pdf('# x\n', 'INFORME_FINAL_DE_AUDITORIA', 'Informe final de auditoría')
    open(os.path.join(ENT, '03_COLECCION_COMPLETA', 'INDICE_GENERAL_DE_ARCHIVOS.md'), 'w', encoding='utf8').write(indice())
    # el informe resume los controles de los ZIP, y el ZIP 05 lleva el informe: primero una pasada de control, después la definitiva
    previo = zips()
    inf = informe(previo)
    open(os.path.join(QC, 'INFORME_FINAL_DE_AUDITORIA.md'), 'w', encoding='utf8').write(inf)
    md_a_pdf(inf, 'INFORME_FINAL_DE_AUDITORIA', 'Informe final de auditoría')
    n = manifiesto()
    FALLOS.clear()
    final = zips()
    control('Manifiesto SHA-256 con %d archivos' % n, n == len(list(archivos(ENT))) - 1)
    json.dump(final, open(os.path.join(SAL, 'resultado_cierre.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print(open(os.path.join(ZIPS, 'SHA256SUMS.txt')).read())
    print('%d controles de cierre, %d fallos' % (len(final['controles']) + 1, len(FALLOS)))
    sys.exit(1 if FALLOS else 0)

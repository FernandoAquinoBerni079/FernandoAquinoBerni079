# -*- coding: utf-8 -*-
"""Genera, desde los resultados de la construcción y de los controles, coleccion/DIFERENCIAS.md (lista cerrada de
diferencias con los seis lotes y dónde aparece cada una) e coleccion/INVENTARIO.md (inventario provisional: de qué
versión aprobada sale cada capítulo, cada parte de la guía y cada práctica; qué referencia de código está vigente; qué
sigue pendiente). Uso: python3 -B coleccion/build/informes.py (después de los controles)."""
import os, sys, json
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
COL = os.path.dirname(AQUI)
ADS = os.path.dirname(COL)
sys.path.insert(0, AQUI)
import fuentes as FU
FU.cargar()
import piezas_coleccion as PC
import diferencias_coleccion as DF

j = lambda n: json.load(open(os.path.join(COL, n), encoding='utf8'))
R, EQ, CO = j('resultado_construccion.json'), j('EQUIVALENCIA.json'), j('COHERENCIA.json')
IND = dict(R['indice_libro'])

# ---------------------------------------------------------------- DIFERENCIAS.md
md = ['# Lista cerrada de diferencias con los seis lotes', '',
      '**Colección ADS 3.º BTI · documentos anuales %s**' % PC.VERSION, '',
      'Estas son **todas** las diferencias admitidas entre los documentos anuales y los documentos aprobados de los lotes. '
      'La equivalencia (`build/equivalencia.py`) compara cada capítulo, cada parte de la guía y cada práctica, bloque por '
      'bloque: el texto, el estilo y el formato de cada párrafo, cada celda de cada tabla, los anchos de columna, el '
      'sombreado y los píxeles de cada imagen. Cualquier diferencia que no esté en esta lista es un fallo.', '',
      'Resultado de la equivalencia: **%d fallos**, en %d segmentos del libro, %d partes de la guía y %d prácticas.' % (
          len(EQ['fallos']), len(EQ['libro']), len(EQ['guia']), len(EQ['cuaderno'])), '',
      '| Id. | Documento | Categoría | Qué cambia | Dónde | Cómo se controla |', '|---|---|---|---|---|---|']
md += ['| %s |' % ' | '.join(d) for d in DF.DIFERENCIAS]
md += ['', '## Apariciones de los reemplazos del libro (D-05 a D-11 y D-18 a D-20)', '',
       '| Reemplazo | Apariciones esperadas | Apariciones en el armado |', '|---|---|---|']
hechos = dict((a, b) for a, b in R['reemplazos'])
md += ['| %s | %d | %d |' % (r[0], r[4], hechos.get(r[0], 0)) for r in PC.REEMPLAZOS]
rf = R.get('rutas_fichas', {})
md += ['', '## Rutas de las fichas de código (D-21)', '',
       '| Documento | Fichas esperadas | Fichas unificadas | Rutas distintas |', '|---|---|---|---|']
md += ['| %s | %d | %d | %s |' % (k, PC.FICHAS_ESPERADAS[k], len(rf.get(k, [])),
                                 ', '.join(sorted({'`%s` → `%s`' % tuple(x) for x in rf.get(k, [])}))) for k in ('libro', 'guia')]
md += ['', '## Qué no cambió', '',
       '- Ningún texto de teoría, ejemplo, práctica, consigna, evaluación, puntaje, indicador ni solución.',
       '- Ninguna figura: se generaron otra vez con los scripts de cada lote y sus píxeles coinciden con los de los documentos '
       'aprobados.',
       '- Ningún bloque de código: se leen de los archivos del proyecto, igual que en los lotes.',
       '- Las menciones a «lote» de la guía docente se conservan: remiten a las carpetas del repositorio (la parte general '
       'de la guía lo explica). Las del libro del estudiante que eran referencias editoriales son D-05 a D-11; las demás '
       'nombran un lote de libros donados (Práctica 11) o los lotes del plan lector (caso Arapoty) y no son referencias '
       'editoriales.',
       '- Las rutas de archivos del prototipo (por ejemplo, lote_5/proyecto/…) se conservan: los archivos siguen en esas '
       'carpetas y el verificador de coherencia comprueba que existan.']
open(os.path.join(COL, 'DIFERENCIAS.md'), 'w', encoding='utf8').write('\n'.join(md) + '\n')

# ---------------------------------------------------------------- INVENTARIO.md
commits = CO['controles']['commits_de_los_lotes']
inv = ['# Inventario provisional de la colección', '',
       '**Análisis y Diseño de Sistemas, 3.º BTI · documentos anuales %s**' % PC.VERSION, '',
       'Estado: versión para la auditoría de integración. No está aprobada para la venta ni para uso en aula; la aprobación '
       'final corresponde a Fernando. Las capacidades C1 a C10 son propuestas para el programa institucional, no '
       'capacidades oficiales del MEC.', '',
       '## 1. Documentos anuales', '',
       '| Documento | Archivo (DOCX entregable, PDF de control) | Páginas |', '|---|---|---|',
       '| Libro del estudiante | ADS_3BTI_LIBRO_ANUAL_ESTUDIANTE_OFICIO_O3 | %d |' % R['paginas']['libro'],
       '| Guía docente anual con solucionario | ADS_3BTI_GUIA_DOCENTE_ANUAL_OFICIO_O3 | %d |' % R['paginas']['guia'],
       '| Cuaderno anual de prácticas | ADS_3BTI_CUADERNO_ANUAL_PRACTICAS_OFICIO_O3 | %d |' % R['paginas']['cuaderno'], '',
       'Formato oficio O3: 21,59 × 33,02 cm, interior 2,5 cm, exterior 1,8 cm, superior e inferior 1,5 cm, márgenes '
       'espejados. Constructor: `coleccion/build/armar_coleccion.py`.', '',
       '## 2. Capítulos del libro y su fuente aprobada', '',
       '| Capítulo | Encuentros | Página | Fuente (módulo y función de armado) | Versión aprobada | Último commit del lote |',
       '|---|---|---|---|---|---|']
for c in range(1, 19):
    m = FU.capitulo(c); n = FU.lote_de(c)
    t = '%s — %s' % (m.CAPITULO, m.TITULO)
    inv.append('| %s | %s | %s | lote_%d/build/cap%d.py · construir.py: capitulo%d | Lote %d, %s | %s |' % (
        t, ' y '.join(map(str, m.ENCUENTROS)), IND.get(t, '—'), n, c, c, n, FU.VERSIONES[n], commits[str(n)] if str(n) in commits else commits[n]))
inv += ['', 'Preliminares: lote_1/build/prelim.py (construir.py del lote 1: preliminares). Aperturas de unidad: la función '
        'apertura_unidad del constructor de cada lote.', '',
        '## 3. Partes de la guía docente', '',
        '| Parte | Fuente | Versión aprobada |', '|---|---|---|']
inv += ['| %s | lote_%d/build/%s.py: construir | Lote %d, %s |' % (PC.titulo_parte(n), n, FU.GUIAS[n], n, FU.VERSIONES[n]) for n in range(1, 7)]
inv += ['', 'Parte general: coleccion/build/guia_general.py (texto nuevo, diferencia D-12).', '',
        '## 4. Prácticas del cuaderno', '',
        '| Práctica | Página del libro | Fuente |', '|---|---|---|']
for t, p in R['indice_cuaderno']:
    if t.startswith('Práctica'):
        c = int(t.split()[1]); n = FU.lote_de(c)
        inv.append('| %s | %s | lote_%d/build/cap%d.py (PRACTICA_*, NIVELES) %s |' % (
            t, IND.get(t, '—'), n, c, '· cuerpo: las llamadas de capitulo%d del lote 1' % c if n == 1 else '· construir.py: PRACTICAS'))
inv += ['', 'Los Capítulos 16 y 18 no tienen práctica (decisiones D-3 y D-4); el 18 tampoco tiene evaluación escrita.', '',
        '## 5. Base de proyecto y referencias de código', '',
        '| Carpeta | Qué es | Estado |', '|---|---|---|',
        '| lote_4/proyecto/base_estudiante/ | Base del estudiante (Unidad IV) | Vigente para los equipos |',
        '| lote_4/proyecto/referencia_docente/ | Referencia docente de la Unidad IV | Se conserva como historia: es el prototipo que reproduce IN-02 |',
        '| lote_5/proyecto/referencia_docente_v2/ | Referencia docente v2 (corrección de IN-02) | Historia de la Unidad V |',
        '| lote_5/proyecto/referencia_docente_v2_sc02/ | Referencia v2 con SC-02 | Referencia docente vigente |',
        '| lote_5/proyecto/cargador_dp/ y lote_5/caso/dr_plantilla.py | Cargador de datos de prueba y plantilla DR | Herramientas de la Unidad V |',
        '| lote_6/proyecto/paquete_entrega_modelo/ y paquete_mbokaja/ | Paquete de entrega modelo y paquete de la Práctica 17 | Vigentes |',
        '| lote_6/proyecto/herramientas/ | Inspección estática y pruebas en aislamiento (v1.1) | Vigentes, sin cambios; Windows y laboratorios pendientes |',
        '', 'Los 29 bloques de código del libro y de la guía se leen de esos archivos al armar, igual que en los lotes.', '',
        '## 6. Reservado (fuera del repositorio)', '',
        '- El conjunto DR (Unidad V) y el banco de variantes V6 (Unidad VI) son exclusivos del docente. No están en GitHub, ni '
        'en los documentos anuales, ni en coleccion/. El verificador de coherencia lo comprobó con las rutas privadas.', '',
        '## 7. Pendiente', '',
        '- Pruebas institucionales en Windows y en las computadoras escolares; instalación y restauración en el laboratorio; '
        'concurrencia real; instalación por otro equipo (la hace el curso).',
        '- Revisión jurídica del borrador de licencia de la Unidad VI.',
        '- Plan anual definitivo y 36 planes de clase: no se generan hasta que se apruebe esta integración.',
        '- Decisión sobre un tomo o dos volúmenes (EVALUACION_ENCUADERNACION.md).']
open(os.path.join(COL, 'INVENTARIO.md'), 'w', encoding='utf8').write('\n'.join(inv) + '\n')
print('DIFERENCIAS.md: %d diferencias · INVENTARIO.md: %d capítulos' % (len(DF.DIFERENCIAS), 18))

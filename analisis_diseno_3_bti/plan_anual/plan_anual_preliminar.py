"""Plan anual preliminar de Análisis y Diseño de Sistemas, 3.º BTI (estructura completa, sin maquetar).

Fuentes, transcritas sin cambios:
- Informe de Work «BTI3_Analisis_Diseno_Diagnostico_Propuesta_v0.1.pdf»
  (SHA-256 3d4f5ab9daf3329f0dd34b13bc30b7001cb8e65780262c536346dbbea065069a):
  - §3: antecedentes del Diseño Curricular MEC;
  - §4.1 y §4.2: competencia y capacidades propuestas, contenidos, indicadores y criterios;
  - §4.3: evaluación;
  - §5.2: foco, evidencia y capacidades de cada encuentro;
  - §6: índice de capítulos y secciones.
- `fase2_pilotos/C_informe_esfuerzo/v2_1/distribucion_36.csv`: HC por categoría de cada encuentro.
- Fichas de los capítulos construidos: `lote_1/build/cap1.py` a `cap3.py` (Unidad I), `lote_2/build/cap4.py` a
  `cap6.py` (Unidad II, versión de referencia aceptada por Fernando el 20-oct-2026) y `lote_3/build/cap7.py` a
  `cap9.py` (Unidad III, lote 3 v1.1, aceptado para integración), `lote_4/build/cap10.py` a `cap13.py` (Unidad IV,
  lote 4 v1.1, versión de referencia para la integración) y `lote_5/build/cap14.py` a `cap16.py` (Unidad V, lote 5
  para auditoría). Los módulos se importan y se leen sus claves (INDICADORES, TITULO,
  ENCUENTROS, ROTULO_CAPACIDAD): ningún indicador se transcribe a mano.

Regla de rotulado:
- todo lo de Work §4 y §6 es propuesta editorial para el programa institucional (columna «Origen»);
- lo único que viene del MEC son las referencias de antecedentes del Diseño Curricular de mayo de 2026,
  con su página, tal como las cita Work §3;
- ninguna capacidad se presenta como oficial del MEC.

Uso: python3 plan_anual_preliminar.py
Escribe `plan_anual_preliminar.csv` y `PLAN_ANUAL_PRELIMINAR.md`. Si un control falla, no escribe nada.
"""
import csv
import importlib.util
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(AQUI)

ROTULO = 'Propuesta editorial para el programa institucional del Plan Optativo; no es programa ni capacidad oficial del MEC.'

COMPETENCIA = ('Analiza necesidades de información de una organización de su entorno y diseña, construye y valida '
               'colaborativamente un prototipo de aplicación web, mediante requisitos verificables, modelos coherentes, '
               'decisiones técnicas justificadas y documentación de entrega, actuando con responsabilidad sobre los datos, '
               'los recursos y los acuerdos del proyecto.')   # Work §4.1

# Work §4.2: código, capacidad, contenidos esenciales, indicadores y evidencia, criterio de evaluación
CAPACIDADES = {
    'C1': ('Delimita un problema y evalúa la factibilidad de una solución.',
           'Sistema, entorno, actores, alcance, alternativas, restricciones, costo y riesgo básicos.',
           'Diferencia problema y solución; identifica actores y restricciones; compara al menos dos alternativas; presenta alcance y exclusiones. Evidencia: ficha de problema y factibilidad.',
           'El alcance responde a una necesidad documentada y es realizable con los recursos disponibles.'),
    'C2': ('Obtiene y contrasta información sobre necesidades de usuarios.',
           'Entrevista, observación, revisión documental, registro de fuentes y resguardo de datos.',
           'Formula preguntas abiertas; registra evidencia; separa hechos, opiniones y supuestos; contrasta dos fuentes o dos roles simulados. Evidencia: dossier de relevamiento.',
           'Las conclusiones son rastreables a evidencia y respetan a las personas consultadas.'),
    'C3': ('Especifica y prioriza requisitos verificables.',
           'Funcionales, no funcionales, reglas, restricciones, aceptación, prioridad y cambios.',
           'Identifica cada requisito; formula al menos ocho funcionales y cuatro no funcionales o restricciones; define aceptación y prioridad; registra una modificación. Evidencia: catálogo versionado.',
           'Requisitos comprensibles, consistentes, necesarios y comprobables; distinción correcta entre requisito, regla y solución.'),
    'C4': ('Modela procesos e interacciones del sistema.',
           'Proceso actual y propuesto, contexto, casos de uso, escenarios y excepciones.',
           'Representa límites y actores; desarrolla tres casos de uso prioritarios con flujo alternativo; mantiene coherencia con requisitos. Evidencia: modelos comentados.',
           'Los diagramas ayudan a explicar el funcionamiento y permiten detectar omisiones, sin mezclar notaciones.'),
    'C5': ('Justifica el modelo de información y sus reglas de integridad.',
           'Entidades, ejemplares, relaciones, claves, diccionario, persistencia e historial; revisión aplicada de normalización.',
           'Distingue obra/edición y ejemplar; vincula cada préstamo a un ejemplar; justifica claves y relaciones; detecta una anomalía y corrige el diseño. Evidencia: modelo y diccionario.',
           'El modelo representa las reglas acordadas, conserva historial y evita referencias inválidas y duplicación de préstamos activos.'),
    'C6': ('Diseña la interacción y la arquitectura del prototipo.',
           'Tareas de usuario, bocetos, navegación, estados, accesibilidad básica y separación de responsabilidades.',
           'Traza tres recorridos; muestra estados vacío/error/éxito; identifica presentación, reglas y datos; justifica una decisión con alternativas. Evidencia: bocetos y esquema de arquitectura.',
           'El diseño permite completar tareas, es legible y resulta coherente con alcance, datos y entorno.'),
    'C7': ('Organiza y registra el trabajo colaborativo.',
           'Iteraciones, tareas, responsables, estimación, versiones, cambios, autoría y revisión entre pares.',
           'Mantiene tareas y decisiones al día; produce al menos tres versiones identificables; registra aportes de cada integrante y el origen de recursos. Evidencia: bitácora y revisiones.',
           'El proceso es verificable, el equipo responde a cambios y cada estudiante demuestra participación sustantiva.'),
    'C8': ('Integra un prototipo funcional con persistencia.',
           'Formularios, validación del servidor, consultas parametrizadas, reglas, transacciones y reportes mínimos.',
           'Ejecuta catálogo, lectores, préstamo y devolución; conserva datos al reiniciar; rechaza operaciones inválidas; relaciona módulos con requisitos. Evidencia: prototipo y demostración.',
           'Funciona el circuito completo y las reglas se hacen cumplir más allá de la apariencia de las pantallas.'),
    'C9': ('Verifica y mejora la solución a partir de evidencia.',
           'Casos normales y límite, integración, usabilidad, aceptación, incidencias y regresión.',
           'Ejecuta al menos doce casos identificados; registra esperado/obtenido; incluye seis rechazos o límites; corrige y vuelve a probar; realiza dos sesiones de uso. Evidencia: matriz de pruebas e incidencias.',
           'La evidencia permite reproducir resultados; las correcciones responden a hallazgos y no introducen regresiones conocidas.'),
    'C10': ('Documenta, entrega y defiende el prototipo.',
            'Instalación, uso, respaldo/restauración, límites, pendientes, aceptación y comunicación técnica.',
            'Otro equipo instala con la guía; recupera un respaldo; cada integrante explica una decisión y una prueba; comunica limitaciones. Evidencia: paquete de entrega y defensa individual.',
            'La entrega es reproducible, comprensible, honesta sobre sus límites y utilizable por una persona ajena al desarrollo.'),
}

UNIDADES = {   # Work §5.1
    'I': ('Comprender el problema y su contexto', (1, 6), 30, 'Problema, relevamiento y alcance viable.'),
    'II': ('Especificar qué debe resolver el sistema', (7, 12), 30, 'Requisitos, procesos y trazabilidad inicial.'),
    'III': ('Diseñar una solución coherente', (13, 18), 30, 'Modelo de datos, interacción y arquitectura revisados.'),
    'IV': ('Construir el prototipo por incrementos', (19, 26), 40, 'Circuito funcional integrado y persistente.'),
    'V': ('Verificar, validar y mejorar', (27, 32), 30, 'Evidencia de pruebas, correcciones y aceptación.'),
    'VI': ('Entregar y comunicar', (33, 36), 20, 'Paquete reproducible, defensa y recuperación.'),
}

# Work §6: capítulo → (unidad, título, encuentros, secciones, cierre)
CAPITULOS = {
    1: ('I', 'Un sistema comienza con una necesidad', (1, 2),
        ['1.1. De la dificultad cotidiana al problema de información.', '1.2. Personas, procesos, datos, recursos y límites del sistema.',
         '1.3. Actores e interesados: necesidades diferentes, decisiones compartidas.', '1.4. Diagnóstico de conocimientos previos y plan de apoyo.'],
        'Práctica: describir una biblioteca y separar hechos, supuestos y soluciones anticipadas.'),
    2: ('I', 'Investigar antes de diseñar', (3, 4),
        ['2.1. Entrevistar para comprender tareas y problemas.', '2.2. Observar un proceso y analizar documentos.',
         '2.3. Contrastar fuentes, contradicciones y necesidades no expresadas.', '2.4. Registrar evidencia con respeto por las personas y sus datos.'],
        'Práctica: dossier de relevamiento con roles de bibliotecario, lector y dirección.'),
    3: ('I', 'Elegir un alcance posible', (5, 6),
        ['3.1. Objetivos y resultados esperados.', '3.2. Comparación de alternativas y factibilidad básica.',
         '3.3. Recursos, riesgos, límites y exclusiones.', '3.4. Acuerdo de proyecto y organización del equipo.'],
        'Revisión de unidad I: defensa del problema y del alcance; H1.'),
    4: ('II', 'Requisitos que se pueden comprobar', (7, 8),
        ['4.1. Necesidad, requisito, regla de negocio y solución técnica.', '4.2. Requisitos funcionales, calidad y restricciones.',
         '4.3. Identificación, fuente, prioridad y criterios de aceptación.', '4.4. Ambigüedades frecuentes y cómo corregirlas.'],
        'Práctica: convertir pedidos de usuarios en requisitos verificables.'),
    5: ('II', 'Procesos, contexto y casos de uso', (9, 10),
        ['5.1. Proceso actual y proceso propuesto.', '5.2. Diagrama de contexto y límites de intercambio de información.',
         '5.3. Actores, casos de uso y escenarios principales.', '5.4. Excepciones, decisiones y flujos alternativos.'],
        'Práctica: modelar préstamo y devolución con situaciones problemáticas nuevas.'),
    6: ('II', 'Priorizar y mantener la coherencia', (11, 12),
        ['6.1. Alcance mínimo y funcionalidades postergables.', '6.2. Trazabilidad entre necesidad, requisito, modelo y prueba.',
         '6.3. Iteraciones, tareas, dependencias y responsabilidades.', '6.4. Solicitud de cambio y análisis de impacto.'],
        'Revisión de unidad II: nueva necesidad del usuario y actualización del dossier; H2.'),
    7: ('III', 'Datos que representan las reglas', (13, 14),
        ['7.1. Recuperación aplicada de modelos de Algorítmica.', '7.2. Obra/edición, ejemplar, lector y préstamo: identidad y responsabilidad.',
         '7.3. Relaciones, restricciones, historial y diccionario de datos.', '7.4. Revisión de normalización con ejemplos del proyecto.'],
        'Práctica: justificar el modelo frente a pérdida, devolución y duplicación de solicitudes.'),
    8: ('III', 'Diseñar para las tareas de las personas', (15, 16),
        ['8.1. Recorridos de usuario y organización de pantallas.', '8.2. Bocetos y prototipo de baja fidelidad.',
         '8.3. Estados vacío, carga, error y confirmación.', '8.4. Etiquetas, navegación por teclado y lectura comprensible.'],
        'Práctica: observar el uso del boceto y modificarlo con evidencia.'),
    9: ('III', 'Arquitectura y revisión del diseño', (17, 18),
        ['9.1. Presentación, reglas de negocio y persistencia.', '9.2. Responsabilidades, entradas, salidas y contratos de operaciones.',
         '9.3. Entorno, dependencias y decisiones técnicas justificadas.', '9.4. Coherencia entre requisitos, datos e interfaces.'],
        'Evaluación integradora de la primera etapa: defensa y corrección del dossier; H3.'),
    10: ('IV', 'Del diseño a la primera operación funcional', (19, 20),
         ['10.1. Preparación del entorno y estructura del proyecto.', '10.2. Versiones, bitácora y conjunto inicial de datos ficticios.',
          '10.3. Una operación completa: formulario, procesamiento y almacenamiento.', '10.4. Validación, consulta parametrizada y evidencia de persistencia.'],
         'Práctica: demostrar una operación y vincularla con su requisito y prueba.'),
    11: ('IV', 'Catálogo, ejemplares y lectores', (21, 22),
         ['11.1. Implementación de tareas priorizadas a partir de los bocetos.', '11.2. Datos obligatorios, códigos, duplicados y mensajes útiles.',
          '11.3. Permisos mínimos y comprobaciones del servidor.', '11.4. Edición y baja lógica sin pérdida de historial.'],
         'Práctica: registrar un lote distinto del ejemplo y resolver entradas inválidas.'),
    12: ('IV', 'Préstamos y devoluciones consistentes', (23, 24),
         ['12.1. Precondiciones y reglas de la operación de préstamo.', '12.2. Doble envío, disponibilidad y operaciones atómicas.',
          '12.3. Devolución, estado del ejemplar y conservación de historial.', '12.4. Fallos previsibles y comprobación de resultados.'],
         'Práctica: resolver dos solicitudes incompatibles y explicar la protección elegida.'),
    13: ('IV', 'Información útil e integración', (25, 26),
         ['13.1. Búsqueda de ejemplares disponibles y préstamos activos.', '13.2. Vencimientos y fecha de referencia.',
          '13.3. Integración de módulos y revisión del alcance mínimo.', '13.4. Demostración del incremento y registro de pendientes.'],
         'Revisión de unidad IV: circuito funcional completo; H4.'),
    14: ('V', 'Probar con criterios y datos independientes', (27, 28),
         ['14.1. Verificación, validación y aceptación.', '14.2. Casos normales, límites, excepciones y rechazos.',
          '14.3. Resultado esperado, resultado obtenido y evidencia.', '14.4. Cobertura de requisitos y reporte de defectos.'],
         'Práctica: elaborar y ejecutar una batería nueva de pruebas.'),
    15: ('V', 'Probar el sistema completo con usuarios', (29, 30),
         ['15.1. Pruebas de integración y persistencia.', '15.2. Permisos, recuperación de datos y manejo de errores.',
          '15.3. Sesiones de uso y observación de dificultades.', '15.4. Aceptación por criterios acordados y prioridad de correcciones.'],
         'Práctica: revisión cruzada entre equipos con datos reservados para evaluación.'),
    16: ('V', 'Corregir y volver a comprobar', (31, 32),
         ['16.1. Diagnóstico de incidencias e impacto de cambios.', '16.2. Corrección, revisión entre pares y regresión.',
          '16.3. Actualización de modelos, pruebas y documentación.', '16.4. Recuperación técnica y versión candidata.'],
         'Revisión de unidad V: evidencia de calidad y límites conocidos; H5.'),
    17: ('VI', 'Preparar una entrega reproducible', (33, 34),
         ['17.1. Guía de instalación, configuración y ejecución.', '17.2. Manual breve basado en tareas.',
          '17.3. Respaldo, restauración, licencias y registro de procedencia.', '17.4. Prueba de instalación por otro equipo y acta de entrega simulada.'],
         'Práctica: entregar código, datos, pruebas y documentación coherentes; H6.'),
    18: ('VI', 'Demostrar, defender y aprender del proyecto', (35, 36),
         ['18.1. Demostración organizada por requisitos y evidencias.', '18.2. Defensa individual de decisiones y resolución de una variante.',
          '18.3. Recuperación de aprendizajes pendientes.', '18.4. Retrospectiva y mejoras futuras justificadas.'],
         'Evaluación integradora de la segunda etapa y cierre del proyecto.'),
}

# Work §5.2, columna «Evidencia o evaluación», por encuentro
EVIDENCIA = {
    1: 'Resolución individual breve; mapa de apoyos.', 2: 'Ficha de problema; mapa de actores.',
    3: 'Guion y criterios para resguardar información.', 4: 'Notas, fuentes y registro de contradicciones.',
    5: 'Matriz de factibilidad y riesgos.', 6: 'H1: problema y alcance defendidos; correcciones.',
    7: 'Catálogo con identificadores y fuente.', 8: 'Requisitos comprobables; revisión entre pares.',
    9: 'Flujos comentados y decisiones justificadas.', 10: 'Préstamo, devolución y consulta con alternativas.',
    11: 'Requisito-modelo-prueba; tareas y responsables.', 12: 'H2: requisitos y modelos funcionales versionados.',
    13: 'Obras/ediciones, ejemplares, lectores y préstamos.', 14: 'Revisión del modelo con ejemplos y contraejemplos.',
    15: 'Tres tareas completas en prototipo de baja fidelidad.', 16: 'Registro de problemas y bocetos corregidos.',
    17: 'Esquema de arquitectura y decisión técnica.', 18: 'H3: dossier consistente y evidencia individual.',
    19: 'Ejecución inicial reproducible; ficha de entorno.', 20: 'Formulario-servidor-BD; prueba de persistencia.',
    21: 'Alta, consulta y edición con reglas de validación.', 22: 'Validación en servidor; rechazo de acceso indebido.',
    23: 'Operación coherente ante reenvío o segunda solicitud.', 24: 'Devolución única, conservación de referencias y pruebas.',
    25: 'Reporte correcto con fecha de referencia definida.', 26: 'H4: prototipo completo mínimo y lista de incidencias.',
    27: 'Matriz con resultados esperados y requisitos cubiertos.', 28: 'Resultados obtenidos e incidencias reproducibles.',
    29: 'Evidencia del circuito completo y recuperación.', 30: 'Observaciones de dos usuarios/roles y prioridades.',
    31: 'Registro de regresión; trazabilidad actualizada.', 32: 'H5: versión candidata con límites conocidos.',
    33: 'Documentación probada por el propio equipo.', 34: 'H6: paquete reproducible; ajustes finales.',
    35: 'Rúbrica de producto y preguntas de transferencia.', 36: 'Evidencia faltante, balance y propuesta de continuidad.',
}

# Antecedentes del Diseño Curricular MEC (mayo de 2026) citados en Work §3, con sus páginas tal como los da Work.
# Work los lista por asignatura; la ASIGNACIÓN A CADA CAPÍTULO es propuesta de esta estructura y debe revisarse.
# Son referencias de articulación, no capacidades de esta asignatura.
ANTECEDENTES_MEC = {
    1: 'Algorítmica 1.º, pp. 70-73 (reglas sin ambigüedad); Laboratorio 1.º, pp. 41-47 (documentos colaborativos, ética).',
    2: 'Laboratorio 1.º, pp. 41-47 (documentos colaborativos, seguridad y ética).',
    3: 'Administración Financiera 2.º-3.º, pp. 80-87 (factibilidad básica y evidencia); Matemática Aplicada, pp. 88-94 (estimaciones; articulación condicional, ver Work §3).',
    4: 'Algorítmica 1.º, pp. 70-73 (reglas de préstamo sin ambigüedad).',
    5: 'Dibujo Técnico 1.º, pp. 35-38 (legibilidad y convenciones; la semántica del diagrama de contexto y de casos de uso es aporte nuevo).',
    6: 'Matemática Aplicada, pp. 88-94 (dependencias y cronograma sencillo; articulación condicional); Laboratorio 3.º, p. 58 (iteraciones y metodologías).',
    7: 'Algorítmica 3.º, pp. 77-79 (DER, integridad, normalización; concurrente).',
    8: 'Laboratorio 1.º, pp. 39-40 (HTML/CSS, formularios).',
    9: 'Laboratorio 3.º, pp. 52-54 (ciclo de vida, responsabilidades); Laboratorio 2.º, pp. 50-52 (servidor web).',
    10: 'Laboratorio 2.º, pp. 47-49 (variables, funciones, GET/POST); Algorítmica 2.º, pp. 74-76 (modularización, validación).',
    11: 'Laboratorio 3.º, pp. 54-55 (CRUD, SQL, restricciones; concurrente).',
    12: 'Laboratorio 3.º, pp. 54-55 (conexión a BD y consistencia; concurrente).',
    13: 'Laboratorio 3.º, pp. 54-55; Algorítmica 2.º, pp. 74-76 (filtros y consultas).',
    14: 'Laboratorio 3.º, p. 58 (TDD e integración continua como antecedentes concurrentes).',
    15: 'Laboratorio 3.º, pp. 54-55 (persistencia); Hardware 2.º, pp. 66-69 (respaldos y entorno).',
    16: 'Laboratorio 3.º, p. 58 (revisión entre pares y mejora).',
    17: 'Software 1.º, pp. 59-63 (licencias, procedencia); Hardware 2.º, pp. 66-69 (instalación y respaldos).',
    18: 'Orientaciones de evaluación por competencias, pp. 95-106 (evidencia individual).',
}

# Indicadores ya escritos en las fichas de los capítulos construidos (se leen del código, no se transcriben a mano)
FICHAS = {1: 'lote_1/build/cap1.py', 2: 'lote_1/build/cap2.py', 3: 'lote_1/build/cap3.py',
          4: 'lote_2/build/cap4.py', 5: 'lote_2/build/cap5.py', 6: 'lote_2/build/cap6.py',
          7: 'lote_3/build/cap7.py', 8: 'lote_3/build/cap8.py', 9: 'lote_3/build/cap9.py',
          10: 'lote_4/build/cap10.py', 11: 'lote_4/build/cap11.py', 12: 'lote_4/build/cap12.py', 13: 'lote_4/build/cap13.py',
          14: 'lote_5/build/cap14.py', 15: 'lote_5/build/cap15.py', 16: 'lote_5/build/cap16.py'}


def cargar_ficha(n, ruta):
    """Importa el módulo del capítulo (sin escribir cachés en las carpetas de los lotes) y devuelve el módulo."""
    sys.dont_write_bytecode = True
    carpeta = os.path.dirname(os.path.join(ADS, ruta))
    for p in (carpeta, os.path.join(ADS, 'lote_1', 'build'), os.path.join(ADS, 'lote_1', 'caso')):
        if p not in sys.path:
            sys.path.append(p)
    spec = importlib.util.spec_from_file_location('ficha_cap%d' % n, os.path.join(ADS, ruta))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def main():
    fallos = []

    def chk(cond, msg):
        if not cond:
            fallos.append(msg)

    dist = list(csv.DictReader(open(os.path.join(ADS, 'fase2_pilotos/C_informe_esfuerzo/v2_1/distribucion_36.csv'), encoding='utf-8')))
    cats = ['A', 'D', 'P', 'V', 'Doc', 'G', 'E']
    chk(len(dist) == 36, 'la distribución no tiene 36 encuentros')
    chk(sum(int(r[c]) for r in dist for c in cats) == 180, 'la distribución no suma 180 HC')
    for u, (_, (a, z), hc, _) in UNIDADES.items():
        chk(sum(int(r[c]) for r in dist if a <= int(r['encuentro']) <= z for c in cats) == hc, f'la Unidad {u} no suma {hc} HC')
    chk(sorted(e for c in CAPITULOS.values() for e in c[2]) == list(range(1, 37)), 'los capítulos no cubren los 36 encuentros una sola vez')
    chk(set(EVIDENCIA) == set(range(1, 37)), 'falta la evidencia de algún encuentro')
    chk(set(ANTECEDENTES_MEC) == set(CAPITULOS), 'falta el antecedente MEC de algún capítulo')
    hitos = {int(r['encuentro']): r['hito'] for r in dist if r['hito']}
    chk(hitos == {6: 'H1', 12: 'H2', 18: 'H3', 26: 'H4', 32: 'H5', 34: 'H6'}, f'hitos inesperados {hitos}')
    for r in dist:
        chk(r['hito'] == '' or EVIDENCIA[int(r['encuentro'])].startswith(r['hito']), f"E{r['encuentro']}: la evidencia de Work no nombra el hito")

    def caps_de(txt):
        out = set()
        for parte in txt.replace(' ', '').split(','):
            if '-' in parte:
                a, z = (int(x[1:]) for x in parte.split('-'))
                out |= {f'C{k}' for k in range(a, z + 1)}
            else:
                out.add(parte)
        return out
    for r in dist:
        chk(caps_de(r['capacidades_work']) <= set(CAPACIDADES), f"E{r['encuentro']}: capacidad desconocida")
    mods = {n: cargar_ficha(n, r) for n, r in FICHAS.items()}
    ind = {n: list(m.INDICADORES) for n, m in mods.items()}
    for n, m in mods.items():
        u, tit, encs, secs, cierre = CAPITULOS[n]
        chk(m.TITULO == tit, f'Capítulo {n}: el título de la ficha no es el de Work')
        chk(tuple(m.ENCUENTROS) == tuple(encs), f'Capítulo {n}: los encuentros de la ficha no son los de Work')
        chk(ind[n] and all(isinstance(i, str) and i for i in ind[n]), f'Capítulo {n}: indicadores vacíos')
        caps = set().union(*(caps_de(dist[e - 1]['capacidades_work']) for e in encs))
        rot = set(re.findall(r'C\d+', m.ROTULO_CAPACIDAD))
        for a, z in re.findall(r'C(\d+) a C(\d+)', m.ROTULO_CAPACIDAD):   # «C1 a C7» rotula del C1 al C7
            rot |= {f'C{k}' for k in range(int(a), int(z) + 1)}
        chk(caps <= rot, f'Capítulo {n}: la ficha no rotula las capacidades de Work §5.2 {sorted(caps - rot)}')
        chk('no son capacidades oficiales del MEC' in m.ROTULO_CAPACIDAD or 'no es una capacidad oficial del MEC' in m.ROTULO_CAPACIDAD, f'Capítulo {n}: el rótulo no aclara que no son capacidades oficiales')
    if fallos:
        print('FALLAS:\n- ' + '\n- '.join(fallos)); sys.exit(1)

    filas = []
    for n, (u, tit, encs, secs, cierre) in CAPITULOS.items():
        caps = sorted(set().union(*(caps_de(dist[e - 1]['capacidades_work']) for e in encs)), key=lambda c: int(c[1:]))
        for e in encs:
            r = dist[e - 1]
            filas.append({
                'unidad': u, 'capitulo': n, 'titulo_capitulo': tit, 'encuentro': e,
                'foco_work': r['foco_work'], 'capacidades_encuentro': r['capacidades_work'],
                'capacidades_capitulo': ', '.join(caps), 'secciones': ' '.join(secs), 'cierre': cierre,
                'evidencia_work': EVIDENCIA[e], 'hito': r['hito'],
                'indicadores': ' | '.join(ind[n]) if n in ind else 'Pendiente: se fijan en la ficha del capítulo (referencia: indicadores de Work §4.2 de ' + ', '.join(caps) + ').',
                'origen_indicadores': ('ficha del capítulo construido: ' + FICHAS[n]) if n in ind else 'pendiente',
                'antecedentes_mec': ANTECEDENTES_MEC[n],
                **{'hc_' + c: r[c] for c in cats},
                'origen': 'Propuesta editorial (Work §4-§6); antecedentes: Diseño Curricular MEC, mayo de 2026, páginas según Work §3, asignados al capítulo por esta estructura',
            })
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(filas[0]), lineterminator='\n'); w.writeheader(); w.writerows(filas)
    open(os.path.join(AQUI, 'plan_anual_preliminar.csv'), 'w', encoding='utf-8').write(buf.getvalue())

    md = ['# Plan anual preliminar — Análisis y Diseño de Sistemas, 3.º BTI (estructura)', '',
          '**Biblioteca Comercial 2026 · Plan Optativo · 5 HC semanales · 36 encuentros · 180 HC**', '',
          '> **Estado:** estructura preliminar para revisión. No es el plan anual maquetado ni está aprobado. ' + ROTULO, '',
          '> Se genera con `plan_anual_preliminar.py` desde el informe de Work v0.1 (SHA-256 `3d4f5ab9…065069a`), '
          'la distribución de 180 HC (v2.1) y las fichas de los capítulos construidos. No editar a mano: corregir las fuentes y regenerar.', '',
          '## 1. Competencia propuesta (Work §4.1)', '', COMPETENCIA, '',
          '## 2. Capacidades propuestas (Work §4.2)', '', ROTULO, '',
          '| Código | Capacidad | Contenidos esenciales | Indicadores observables y evidencia | Criterio de evaluación |', '|---|---|---|---|---|']
    for c, (cap, cont, indi, crit) in CAPACIDADES.items():
        md.append(f'| {c} | {cap} | {cont} | {indi} | {crit} |')
    md += ['', '## 3. Unidades (Work §5.1)', '', '| Unidad | Encuentros | HC | Resultado de unidad |', '|---|---|---:|---|']
    for u, (t, (a, z), hc, res) in UNIDADES.items():
        md.append(f'| {u}. {t} | {a}-{z} | {hc} | {res} |')
    md += ['', '## 4. Secuencia por capítulo y encuentro', '',
           'HC por categoría (distribución v2.1): A análisis · D diseño · P programación · V verificación y validación · Doc documentación · G gestión · E evaluación.', '']
    for n, (u, tit, encs, secs, cierre) in CAPITULOS.items():
        fs = [f for f in filas if f['capitulo'] == n]
        md += [f'### Capítulo {n}. {tit} (Unidad {u}; encuentros {encs[0]}-{encs[1]})', '',
               f'- **Capacidades del capítulo:** {fs[0]["capacidades_capitulo"]} (propuestas).',
               '- **Secciones (Work §6):** ' + ' '.join(secs), f'- **Cierre:** {cierre}',
               f'- **Indicadores:** {fs[0]["indicadores"]}' + (f' _(de {FICHAS[n]})_' if n in ind else ''),
               f'- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): {ANTECEDENTES_MEC[n]}', '',
               '| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |',
               '|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|']
        for f in fs:
            md.append(f"| {f['encuentro']} | {f['foco_work']} | {f['capacidades_encuentro']} | {f['evidencia_work']} | "
                      + ' | '.join(f['hc_' + c] for c in cats) + ' |')
        md.append('')
    tot = {c: sum(int(r[c]) for r in dist) for c in cats}
    md += ['## 5. Totales', '', '| ' + ' | '.join(cats) + ' | Total |', '|' + '---:|' * (len(cats) + 1),
           '| ' + ' | '.join(str(tot[c]) for c in cats) + f' | {sum(tot.values())} |', '',
           '## 6. Evaluación (Work §4.3)', '',
           '- Evaluación continua basada en evidencias, con diagnóstico inicial, revisiones de unidad (H1, H2, H4, H5), '
           'evaluación intermedia (H3, encuentro 18), entrega (H6, encuentro 34) y defensa individual (encuentro 35).',
           '- Ponderación editorial sugerida: problema y relevamiento 15 %; requisitos y trazabilidad 20 %; modelos y diseño 20 %; '
           'prototipo e integración 20 %; pruebas y mejora 15 %; documentación y defensa 10 %. No es una escala oficial del MEC.',
           '- En cada criterio, 60 % de evidencia del producto compartido y 40 % de evidencia individual (propuesta editorial).',
           '- Niveles de desempeño: 4 Sólido, 3 Logrado, 2 En desarrollo, 1 Inicial; la ausencia de evidencia se registra aparte.', '',
           '## 7. Lo que falta para el plan anual definitivo', '',
           '- Indicadores de los Capítulos 17 y 18: se fijan en la ficha de cada capítulo al construirlo (unicidad y verificabilidad).',
           '- Procedimientos e instrumentos por encuentro, con unicidad dentro del año (como en el formato canónico de la colección).',
           '- Calendario por etapas del año escolar y adaptación de 28 encuentros (distribución v2.1, `distribucion_28.csv`).',
           '- Maquetación en oficio con el formato canónico de la colección, y cotejo con las fichas del libro aprobado.']
    open(os.path.join(AQUI, 'PLAN_ANUAL_PRELIMINAR.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    print(f'Controles correctos. {len(filas)} encuentros, {len(CAPITULOS)} capítulos, {sum(tot.values())} HC.')


if __name__ == '__main__':
    main()

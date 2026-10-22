# -*- coding: utf-8 -*-
"""Textos de la entrega comercial v1.0 (instrucciones, fichas, propuesta comercial, condiciones de uso, licencias,
análisis legal, impresión). Cada documento es una lista de bloques que render() convierte en DOCX y PDF con la maqueta de
la colección (oficio, verde BTI, Calibri/Carlito). Las cifras (páginas, hojas, lomo, tamaños) las calcula empaquetar.py y
llegan en el diccionario C."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, 'plan'))
import maqueta_plan as MP

TITULO = 'Análisis y Diseño de Sistemas · 3.º BTI · Edición comercial v1.0'
AVISO_MEC = ('Las capacidades C1 a C10 y la planificación son propuestas para el programa institucional del Plan Optativo, que '
             'cada institución puede elaborar según el Diseño Curricular del MEC (mayo de 2026, p. 29). No constituyen un '
             'programa oficial aprobado por el MEC. Citar el Diseño Curricular no significa que el MEC haya aprobado este '
             'material.')

FUENTES_LEGALES = [
    ('Ley N.º 1328/98 de Derecho de Autor y Derechos Conexos (texto en SICE/OEA y BACN)',
     'http://www.sice.oas.org/int_prop/nat_leg/paraguay/L132898a.asp'),
    ('Ley N.º 1328/98, ficha de la BACN', 'https://www.bacn.gov.py/leyes-paraguayas/908/ley-n-1328-derecho-de-autor-y-derechos-conexos'),
    ('Decreto N.º 5159/99, reglamento de la Ley 1328/98 (Digesto del Senado)', 'http://digesto.senado.gov.py/detalles&id=2923'),
    ('Depósito legal (BACN, «Conoce tu ley»)', 'https://www.bacn.gov.py/conoce-tu-ley/8372/deposito-legal'),
    ('ISBN, agencia en Paraguay (BACN, «Conoce tu ley»)', 'https://www.bacn.gov.py/conoce-tu-ley/8368/isbn-agencia-en-paraguay'),
    ('Ley N.º 7140/2023 de Fomento de la Lectura y del Libro (BACN)',
     'https://www.bacn.gov.py/leyes-paraguayas/11927/ley-n-7140-de-fomento-de-la-lectura-y-del-libro'),
    ('Resumen de la Ley 7140/2023 (Vouga Abogados, noviembre de 2023)',
     'https://www.vouga.com.py/en/novedades-legislativas-en-materia-de-derecho-digital-y-propiedad-intelectual-noviembre-2023/'),
    ('Ley N.º 3436/08, Biblioteca y Archivo Central del Congreso (depósito legal)',
     'https://www.bacn.gov.py/leyes-paraguayas/3477/ley-n-3436-creacion-de-la-biblioteca-y-archivo-central-del-congreso-nacional'),
    ('DNIT, IVA en la comercialización de libros digitales',
     'https://www.dnit.gov.py/web/portal-institucional/w/iva-comercializacion-de-libros-digitales-'),
]


def render(nombre, titulo, bloques, destino, subtitulo=None):
    """bloques: ('h', texto) · ('h2', texto) · ('p', texto) · ('ul', [..]) · ('t', (enc, filas, anchos)) · ('box', (tit, [..]))."""
    d = MP.documento()
    MP.parrafo(d, TITULO, 9, color=MP.VERDE)
    MP.titulo(d, titulo, 1)
    if subtitulo:
        MP.parrafo(d, subtitulo, 10, italica=True)
    for tipo, x in bloques:
        if tipo == 'h': MP.titulo(d, x, 2)
        elif tipo == 'h3': MP.titulo(d, x, 3)
        elif tipo == 'p': MP.parrafo(d, x, 10)
        elif tipo == 'ul': MP.lista(d, x, 10)
        elif tipo == 't':
            enc, filas, anchos = x
            esc = MP.UTIL / sum(anchos)
            MP.tabla(d, enc, filas, [a * esc for a in anchos], tam=8.5, dividir_filas=True)
            MP.parrafo(d, '', 4)
        elif tipo == 'box': MP.recuadro(d, x[0], x[1])
    MP.pie(d.sections[0], '%s · %s' % (TITULO, titulo))
    os.makedirs(destino, exist_ok=True)
    ruta = os.path.join(destino, nombre + '.docx')
    d.save(ruta)
    MP.a_pdf(ruta, destino)
    return ruta


# ---------------------------------------------------------------- documentos
def instrucciones_estudiante(C):
    return [
        ('p', 'Este paquete tiene los dos materiales del estudiante para todo el año de Análisis y Diseño de Sistemas, 3.er curso '
              'del Bachillerato Técnico en Informática.'),
        ('t', (['Archivo', 'Qué es', 'Cómo se usa'], [
            ['Libro del estudiante (PDF, %d págs.)' % C['paginas']['libro'], 'Teoría, ejemplos resueltos, actividades, prácticas y '
             'evaluaciones de los 18 capítulos', 'Se lee y se trabaja en clase. Las actividades tienen renglones para respuestas breves.'],
            ['Cuaderno de prácticas (PDF, %d págs.)' % C['paginas']['cuaderno'], 'Las 16 prácticas con renglones de 8 mm',
             'Se imprime y se completa a mano. Tu docente te indica el nivel (1, 2 o 3) de cada práctica.'],
        ], [5, 6, 7])),
        ('h', 'Cómo se organiza el año'),
        ('ul', ['Seis unidades y 18 capítulos; cada capítulo ocupa dos encuentros de 5 horas cátedra.',
                'Las actividades están en cuatro bloques: «Ejercitá», «Resolvé», «Pensá y decidí» y «Desafío».',
                'Cada unidad termina con un hito integrador (H1 a H6), donde tu equipo presenta su trabajo y vos mostrás '
                'individualmente lo que sabés hacer.',
                'Llevá la bitácora del equipo desde el primer día: es parte de tu evidencia individual.']),
        ('h', 'Imprimir el cuaderno'),
        ('ul', ['Papel oficio (21,59 × 33,02 cm), a doble faz, volteo por el borde largo.',
                'Imprimí al 100 % («tamaño real»), sin ajustar a la página, para que los renglones queden de 8 mm.']),
        ('h', 'Derechos'),
        ('p', 'Estos materiales tienen derechos de autor. Son para tu uso personal como estudiante del curso: no los compartas ni '
              'los publiques. ' + AVISO_MEC),
    ]


def instrucciones_docente(C):
    R = C['ref']
    return [
        ('p', 'Este paquete tiene los materiales del docente: la guía con solucionario, el plan anual y los 36 planes de clase '
              '(editables) y los recursos digitales del proyecto.'),
        ('t', (['Archivo o carpeta', 'Contenido', 'Formato'], [
            ['Guía docente con solucionario', 'Secuencia de los 36 encuentros, claves, rúbricas e instrumentos (%d págs.)' % C['paginas']['guia'], 'PDF y DOCX'],
            ['Plan anual', 'Encuadre, capacidades, desarrollo por encuentro, distribución de 180 HC y matriz (%d págs.)' % C['paginas']['plan_anual'], 'DOCX editable y PDF'],
            ['Planes de clase', 'Los 36 planes, dos páginas cada uno (%d págs.)' % C['paginas']['planes'], 'DOCX editable y PDF'],
            ['RECURSOS_DIGITALES/', 'Base del proyecto del estudiante, referencias docentes, cargador de datos de prueba, paquetes '
             'de entrega, herramientas de revisión y planilla de tiempos del Encuentro 35', 'Carpetas con la misma ruta que cita la guía'],
        ], [5, 9, 4])),
        ('h', 'Antes de empezar el año'),
        ('ul', ['Leer la parte general de la guía (págs. 4 a 6): organización, instrumentos y seguridad.',
                'Adoptar el plan anual en el PCI y completar sus campos (sección 1.3 y Anexo A). La carga es de 5 HC semanales; '
                'si el calendario tiene menos semanas efectivas, usar la adaptación a 28 encuentros de la guía.',
                'Completar en los planes de clase los campos grises: institución, docente, sección y fecha.']),
        ('h', 'Preparación durante el año'),
        ('t', (['Cuándo', 'Qué preparar', 'Guía, pág.'], [
            ['Antes del Encuentro 13', 'Acuerdo con Algorítmica 3.º (ruta A o B)', str(R['acuerdo_algoritmica'])],
            ['Antes del Encuentro 19', 'Coordinación con Laboratorio y prueba de campo del entorno E-1 a E-12 en las computadoras de la institución', '%d-%d' % (R['laboratorio_iv'], R['ficha_entorno'])],
            ['Antes del Encuentro 27', 'Copias descartables y cargador de datos de prueba', str(R['copias'])],
            ['Antes del Encuentro 30', 'Conjunto reservado DR, generado por el docente con la plantilla', str(R['dr'])],
            ['Antes del Encuentro 33', 'Paquete modelo, herramientas y paquete de Mbokaja', str(R['paquete_modelo'])],
            ['Antes del Encuentro 35', 'Variantes reservadas V6 y planilla de tiempos', '%d-%d' % (R['variantes'], R['tiempos_e35'])],
        ], [4, 11, 3])),
        ('h', 'Materiales reservados y seguridad'),
        ('ul', ['El conjunto DR (Unidad V) y el banco de variantes V6 (Unidad VI) no vienen en este paquete: los genera cada '
                'docente con las plantillas lote_5/caso/dr_plantilla.py y lote_6/caso/v6_plantilla.py, y los guarda fuera de '
                'las carpetas del alumnado.',
                'Un paquete de código recibido de otro equipo es código desconocido: primero se inspecciona sin ejecutarlo y '
                'las pruebas se corren solo en un equipo aislado (guía, pág. %d).' % R['codigo_recibido'],
                'El entorno de referencia (PHP y SQLite) se probó en Linux; en Windows y en los equipos escolares se hace la '
                'prueba de campo antes del Encuentro 19. Si no hay computadoras suficientes, cada plan de clase trae su alternativa.']),
        ('h', 'Derechos'),
        ('p', 'Los materiales son para uso del docente y de la institución adquirente. ' + AVISO_MEC),
    ]


def fichas(C):
    filas = []
    for k in ('libro', 'cuaderno', 'guia', 'plan_anual', 'planes'):
        P = C['productos'][k]
        filas.append(['**%s**' % P['nombre'], P['destinatario'], '%d págs. · %d hojas' % (C['paginas'][k], C['hojas'][k]),
                      P['formatos'], P['cifras']])
    bloques = [
        ('h', 'La colección'),
        ('p', 'Colección anual para Análisis y Diseño de Sistemas en 3.er curso del Bachillerato Técnico en Informática, como '
              'propuesta para el programa institucional del Plan Optativo: 5 horas cátedra semanales, 36 encuentros y 180 HC. '
              'El curso analiza, diseña, construye, verifica y entrega un prototipo web para la biblioteca de un colegio, desde el '
              'relevamiento hasta la defensa individual.'),
        ('ul', ['Aprendizaje basado en proyectos, con evidencia individual en cada hito.',
                'Cinco productos coherentes entre sí: cada plan de clase cita las páginas del libro, del cuaderno y de la guía.',
                'Formato oficio, márgenes para encuadernar e impresión a doble faz; DOCX editables para el docente.',
                'Recursos digitales del proyecto: base del estudiante, referencias docentes, pruebas y herramientas.',
                AVISO_MEC]),
        ('h', 'Fichas técnicas'),
        ('t', (['Producto', 'Destinatario', 'Extensión', 'Formatos', 'Contenido'], filas, [3.4, 2.6, 2.4, 3.6, 5.4])),
    ]
    for k in ('libro', 'cuaderno', 'guia', 'plan_anual', 'planes'):
        P = C['productos'][k]
        bloques += [('h3', P['nombre']),
                    ('t', (['Dato', 'Valor'], [
                        ['Título', 'Análisis y Diseño de Sistemas — %s' % P['nombre']],
                        ['Curso', '3.er Curso · Bachillerato Técnico en Informática · Plan Optativo'],
                        ['Edición', 'Edición comercial v1.0, %s' % C['anio']],
                        ['Formato', 'Oficio 21,59 × 33,02 cm, vertical; márgenes espejados (interior 2,5 cm)'],
                        ['Páginas', '%d (%d hojas a doble faz); lomo estimado %s mm en papel de 75 g/m²' % (
                            C['paginas'][k], C['hojas'][k], str(C['lomo'][k]).replace('.', ','))],
                        ['Archivos', P['formatos']],
                        ['Contenido', P['descripcion']],
                        ['ISBN', C['isbn'].get(k) or 'a asignar por el editor (Agencia Paraguaya del ISBN)'],
                        ['Titular y editor', C['titular'] or 'a completar por el titular'],
                    ], [3, 14]))]
    return bloques


def propuesta(C):
    return [
        ('p', 'Propuesta de comercialización para que el titular decida. Los precios se dejan en blanco: este documento no fija '
              'valores, descuentos ni condiciones que no fueron decididos por el titular.'),
        ('h', 'Modalidades'),
        ('t', (['Modalidad', 'Contenido', 'Para quién', 'Precio (a definir)'], [
            ['Libro del estudiante', 'Libro impreso o PDF personal', 'Cada estudiante', ''],
            ['Cuaderno de prácticas', 'Cuaderno impreso o PDF para imprimir', 'Cada estudiante', ''],
            ['Pack del estudiante', 'Libro + cuaderno', 'Cada estudiante', ''],
            ['Pack del docente', 'Guía con solucionario + plan anual + 36 planes + recursos digitales', 'Docente o institución', ''],
            ['Colección completa institucional', 'Los cinco productos y los recursos, con licencia de uso para la institución '
             'y ejemplares del estudiante por cantidad', 'Institución', ''],
        ], [4, 7, 3, 3])),
        ('h', 'Criterios sugeridos'),
        ('ul', ['El pack del docente se entrega a la institución que adopta la colección para sus cursos.',
                'Los ejemplares del estudiante se venden por estudiante (impresos o en PDF personal), no como licencia libre de copia.',
                'La venta en librerías y la distribución comercial amplia requieren el ISBN de cada libro (Ley 7140/2023).',
                'La venta a instituciones requiere factura legal del vendedor; el tratamiento del IVA de libros y material '
                'educativo se confirma con un contador (Constitución, art. 83; DNIT).']),
        ('h', 'Antes del lanzamiento'),
        ('ul', ['Completar los datos del titular y del editor y obtener los ISBN.',
                'Contar con el dictamen jurídico sobre titularidad y sobre las condiciones de uso del código del proyecto.',
                'Aprobar una prueba impresa completa.',
                'Definir precios, canales y condiciones de entrega.']),
    ]


def condiciones(C):
    return [
        ('box', ('Texto para revisión jurídica', ['Estas condiciones son una propuesta redactada para el titular. No tienen valor '
                 'hasta que el titular las apruebe con asesoramiento profesional.'])),
        ('h', '1. Qué se entrega'),
        ('ul', ['Estudiante: libro del estudiante y cuaderno de prácticas en PDF (o impresos).',
                'Docente: guía docente con solucionario (PDF y DOCX), plan anual y 36 planes de clase (DOCX editable y PDF) y '
                'recursos digitales del proyecto.',
                'La entrega digital se hace en archivos ZIP con su huella SHA-256 para comprobar que llegaron completos.']),
        ('h', '2. Uso autorizado'),
        ('ul', ['El estudiante usa su ejemplar para su propio aprendizaje.',
                'El docente y la institución adquirente usan la guía, la planificación y los recursos para sus cursos; pueden '
                'adaptar los DOCX de planificación para su uso interno.',
                'Los recursos digitales del proyecto pueden instalarse, ejecutarse, estudiarse y modificarse dentro de la '
                'institución adquirente, con fines educativos.']),
        ('h', '3. Uso no autorizado'),
        ('ul', ['Reproducir, distribuir o comunicar públicamente los materiales fuera de lo autorizado, salvo las excepciones de '
                'la Ley N.º 1328/98.',
                'Publicar el solucionario o entregarlo a estudiantes.',
                'Revender o redistribuir el material, total o parcialmente, o presentarlo como material oficial del MEC.']),
        ('h', '4. Componentes de terceros'),
        ('p', 'PHP, SQLite, curl, bash y el navegador no se entregan: los instala la institución, con sus propias licencias. Las '
              'fuentes Carlito y Liberation Mono incrustadas en los PDF tienen la SIL Open Font License 1.1.'),
        ('h', '5. Alcance y limitaciones'),
        ('ul', [AVISO_MEC,
                'El entorno técnico de referencia se probó en Linux; la institución hace la prueba de campo en sus equipos '
                '(guía, Parte IV, sección 0.2). El prototipo es educativo, con datos ficticios.',
                'Los casos, personas e instituciones de los ejemplos son ficticios.']),
        ('h', '6. Datos personales'),
        ('p', 'Los materiales no contienen datos personales reales. Las planillas de evaluación se completan en la institución, que '
              'es responsable de resguardar los datos de sus estudiantes.'),
    ]


def licencias(C):
    return [
        ('p', 'Relación de los recursos de terceros que intervienen en la colección y de las atribuciones que corresponden. '
              'Fuente: tablas «Procedencia y derechos de los recursos» de cada parte de la guía docente y licencias verificadas '
              'en el lote 6 con su fuente primaria y su versión.'),
        ('t', (['Recurso', 'Uso en la colección', 'Licencia o condición', '¿Se distribuye?', 'Obligación'], [
            ['Carlito (fuente)', 'Texto de los PDF y de las cubiertas', 'SIL Open Font License 1.1', 'Incrustada en los PDF',
             'Ninguna para documentos con la fuente incrustada; se recomienda mencionarla en los créditos'],
            ['Liberation Mono (fuente)', 'Bloques de código de los PDF', 'SIL Open Font License 1.1', 'Incrustada en los PDF', 'Igual que Carlito'],
            ['Calibri (fuente)', 'Fuente declarada en los DOCX', 'Propiedad de su titular', 'No', 'Ninguna: la provee el sistema del usuario'],
            ['PHP 8.3.6', 'Entorno del prototipo', 'The PHP License 3.01', 'No', 'Ninguna mientras no se distribuya'],
            ['SQLite 3.45.1', 'Base de datos del prototipo', 'Dominio público', 'No', 'Ninguna'],
            ['curl 8.5.0', 'Prueba HTTP opcional', 'Licencia de curl', 'No', 'Ninguna mientras no se distribuya'],
            ['GNU bash 5.2', 'Scripts de prueba .sh', 'GPL v3 o posterior', 'No', 'Ninguna mientras no se distribuya'],
            ['matplotlib', 'Herramienta para generar las figuras', 'Licencia de matplotlib (tipo BSD)', 'No', 'Ninguna sobre las figuras generadas'],
            ['Diseño Curricular del MEC (mayo de 2026)', 'Citas con su página en el plan anual', 'Documento oficial público',
             'Solo citas', 'Citar la fuente: se cita con título y página'],
            ['Constitución Nacional, art. 140', 'Referencia en un recuadro del libro', 'Norma pública', 'Solo referencia', 'Ninguna'],
        ], [3.4, 3.4, 3.2, 2.4, 4.4])),
        ('h', 'Material propio de la colección'),
        ('p', 'Textos, ejemplos, actividades, prácticas, evaluaciones, figuras y diagramas (generados por código), casos ficticios '
              'Arapoty y Mbokaja, código del prototipo y herramientas: redacción y producción originales del proyecto, según las '
              'tablas de procedencia de la guía. Su titularidad la declara el titular (ver «Derechos y requisitos legales»).'),
        ('h', 'Atribuciones que deben figurar'),
        ('ul', ['La fuente del Diseño Curricular del MEC en cada cita (ya figura con su página).',
                'El aviso de que la propuesta institucional no es un programa oficial del MEC (ya figura en la página 1 y en las cubiertas).',
                'Recomendado: «Tipografías Carlito y Liberation Mono, SIL Open Font License 1.1» en la página de créditos.']),
    ]


def legal(C):
    estado = lambda x: '**%s**' % x
    return [
        ('box', ('Alcance', ['Análisis documental preparado desde este entorno. Distingue lo verificado en los archivos de lo que '
                 'necesita constancia del titular, de una autoridad o de un profesional. No es un dictamen jurídico. Los sitios '
                 'oficiales paraguayos no se pudieron abrir desde el entorno de trabajo: lo normativo se tomó de resúmenes de '
                 'búsqueda con enlace a la fuente y debe confirmarse en el texto oficial.'])),
        ('h', 'Resumen'),
        ('t', (['Requisito', 'Estado', 'Qué falta', 'Responsable'], [
            ['1. Titularidad de textos, figuras, diagramas y código', estado('Pendiente'), 'Identificar al titular y al editor; '
             'declaración de titularidad; dictamen sobre la autoría (ver punto 1)', 'Titular y asesor en propiedad intelectual'],
            ['2. Licencias de terceros', estado('Verificado'), 'Nada: ningún componente de terceros se distribuye, salvo las fuentes '
             'OFL incrustadas', '—'],
            ['3. Referencias y atribuciones', estado('Verificado'), 'Agregar la mención de las fuentes OFL en los créditos (recomendado)', 'Editor'],
            ['4. Condiciones de reproducción, distribución e impresión', estado('Redactadas, sin aprobar'), 'Aprobación del titular '
             'con revisión jurídica; incluye el borrador de licencia del código (decisión D-2)', 'Titular y abogado'],
            ['5. ISBN y depósito legal', estado('Pendiente'), 'ISBN de cada libro antes de la venta; depósito legal después de la '
             'edición', 'Editor'],
            ['6. Cita del MEC sin afirmar aprobación', estado('Verificado'), 'Nada: el aviso figura en los cinco productos y las cubiertas', '—'],
        ], [4.5, 2.5, 7, 3])),
        ('h', '1. Titularidad y autoría'),
        ('ul', ['Verificado en los archivos: las tablas de procedencia de la guía declaran propios del proyecto los textos, las '
                'figuras (generadas por código), los casos ficticios y el código; no se incorporaron textos, figuras ni ejercicios '
                'de terceros.',
                'Ley N.º 1328/98: el autor es la persona física que realiza la creación intelectual; la protección no depende del '
                'registro ni de otra formalidad. Para obras colectivas, la ley presume la cesión de los derechos patrimoniales a '
                'quien las publica con su nombre, y para programas de ordenador, al productor (arts. 68 y 69), salvo pacto en contrario.',
                'Pendiente: los archivos no acreditan quién es el titular ni el editor. Los documentos dejan esos campos para '
                'completar (datos_edicion.json) y no se inventan.',
                'Pendiente de dictamen: el material se elaboró con asistencia de herramientas de inteligencia artificial, bajo la '
                'dirección, selección y aprobación del responsable del proyecto. Conviene que un asesor en propiedad intelectual '
                'determine cómo documentar la autoría humana y la titularidad (por ejemplo, como obra colectiva del editor) antes '
                'de registrar o vender.',
                'Recomendado: registrar la obra en la Dirección General de Derecho de Autor de la DINAPI. El registro es declarativo, '
                'pero sirve como prueba.']),
        ('h', '2. Licencias de componentes de terceros'),
        ('p', 'Verificado: ver «Licencias y atribuciones». PHP, SQLite, curl y bash no se distribuyen; sus licencias se verificaron '
              'con su fuente primaria en el lote 6. Las fuentes incrustadas tienen la SIL Open Font License 1.1, que permite '
              'incrustarlas en documentos.'),
        ('h', '3. Referencias y atribuciones obligatorias'),
        ('p', 'Verificado: el Diseño Curricular del MEC se cita con título y página; la Constitución se cita como norma pública. No '
              'hay fotografías ni imágenes de terceros.'),
        ('h', '4. Condiciones de reproducción, distribución e impresión'),
        ('p', 'Redactadas en «Condiciones de entrega y uso» y en el aviso de derechos de cada producto. Falta la aprobación del '
              'titular con revisión jurídica, que incluye el borrador de licencia de uso educativo institucional del código del '
              'proyecto (lote 6, decisión D-2), pendiente desde la Unidad VI.'),
        ('h', '5. ISBN y depósito legal'),
        ('ul', ['ISBN: en Paraguay lo asigna la Agencia Paraguaya del ISBN (Biblioteca Nacional, Secretaría Nacional de Cultura). '
                'La Ley N.º 7140/2023 de Fomento de la Lectura y del Libro define el libro paraguayo con código de barras, '
                'símbolo de copyright, nombre y domicilio del editor, año, tiraje y número de edición, y, según el resumen '
                'consultado, vuelve obligatoria la incorporación del ISBN. Corresponde pedir un ISBN por producto con forma de libro '
                '(libro, cuaderno y guía) y decidir con la agencia si el plan anual y los planes de clase, que son documentos '
                'editables, se publican como libro.',
                'Depósito legal: el art. 25 del Decreto N.º 5159/99 prevé la entrega de ejemplares al registrar la obra '
                '(dos para el registro y dos para la Biblioteca Nacional), y la Ley N.º 3436/08 prevé dos ejemplares para la '
                'Biblioteca y Archivo Central del Congreso dentro de los treinta días de la edición. Es una obligación posterior a '
                'la edición impresa.',
                'Los documentos ya tienen el lugar para el ISBN (página 1 y contratapa); al completar datos_edicion.json y '
                'regenerar, el número aparece en todos los productos.']),
        ('h', '6. Citar el Diseño Curricular frente a afirmar una aprobación'),
        ('p', 'Verificado. El plan anual separa las disposiciones oficiales (citas textuales con su página) de la propuesta editorial '
              'y de las decisiones institucionales. Los cinco productos y las cubiertas dicen que la propuesta no constituye un '
              'programa oficial aprobado por el MEC. El control B de la auditoría comprueba que ningún texto presente capacidades, '
              'competencias o programas como oficiales.'),
        ('h', 'Textos legales listos para usar'),
        ('box', ('Aviso de derechos (página 1 de cada producto)', [
            '© %s [titular]. Todos los derechos reservados. Ninguna parte de esta obra puede reproducirse, distribuirse ni '
            'comunicarse públicamente sin autorización escrita del titular, salvo las excepciones de la Ley N.º 1328/98 de '
            'Derecho de Autor y Derechos Conexos.' % C['anio']])),
        ('box', ('Aviso sobre el MEC', [AVISO_MEC])),
        ('box', ('Créditos tipográficos (recomendado)', ['Tipografías Carlito y Liberation Mono, bajo SIL Open Font License 1.1.'])),
        ('h', 'Fuentes consultadas'),
        ('ul', ['%s: %s' % (t, u) for t, u in FUENTES_LEGALES]),
    ]


def impresion(C):
    filas = []
    for k in ('libro', 'cuaderno', 'guia', 'plan_anual', 'planes'):
        n = C['paginas'][k]
        filas.append([C['productos'][k]['nombre'], str(n), str(C['hojas'][k]),
                      ' · '.join(str((-n) % m) for m in (4, 8, 16)), str(C['lomo'][k]).replace('.', ',') + ' mm'])
    return [
        ('h', 'Archivos para la imprenta'),
        ('ul', ['Interior: <producto>_INTERIOR_IMPRESION.pdf, con las fuentes incrustadas. A la imprenta se le entrega el PDF, no el DOCX.',
                'Cubierta: <producto>_CUBIERTA_IMPRESION.pdf, pliego de contratapa, lomo y tapa con 3 mm de sangrado.',
                'Versión digital: <producto>_DIGITAL.pdf (con tapa, contratapa y marcadores); no es para imprenta.']),
        ('h', 'Datos de cada producto'),
        ('t', (['Producto', 'Páginas', 'Hojas', 'Páginas en blanco para pliegos de 4 · 8 · 16', 'Lomo (75 g/m²)'], filas, [5, 2, 2, 5, 3])),
        ('h', 'Especificaciones'),
        ('ul', ['Papel oficio 216 × 330 mm, vertical, a doble faz, volteo por el borde largo. La página 1 va en el frente de la primera hoja.',
                'Márgenes espejados: interior 2,5 cm para el fresado o el anillado; exterior 1,8 cm; superior e inferior 1,5 cm.',
                'Las páginas en blanco que haga falta agregar para completar el pliego van al final, después de la última página.',
                'El lomo se calculó con 0,1 mm por hoja (papel de 75 g/m²): la imprenta lo ajusta a su papel y regenera la cubierta '
                '(cubiertas.py) si hace falta.',
                'Interior en color, recomendado: las cajas, tablas y figuras usan el verde de la colección. Si se imprime en '
                'escala de grises, hacer antes una prueba de contraste.',
                'Cuaderno: imprimir al 100 %, sin ajustar a la página, para conservar los renglones de 8 mm.',
                'Libro: 106 hojas; encuadernación sugerida, fresado y pegado (lomo de unos 10,6 mm) o anillado.']),
        ('h', 'Prueba impresa antes del tiraje'),
        ('ul', ['Margen interior después de encuadernar.', 'Contraste de los fondos de color de las cajas y de los bloques de código.',
                'Legibilidad del código en 7,5 pt (en pantalla, ampliado a 220 dpi, se lee con nitidez).',
                'Renglones del cuaderno de 8 mm medidos en papel.']),
    ]


WHATSAPP = """*Análisis y Diseño de Sistemas · 3.º BTI* — Colección anual 2026 (edición v1.0)

Un año completo para que tus estudiantes analicen, diseñen, construyan y entreguen un sistema real: el préstamo de libros de la biblioteca de un colegio.

✅ Libro del estudiante: 18 capítulos, 6 unidades, 16 prácticas
✅ Cuaderno de prácticas con renglones para escribir
✅ Guía docente con solucionario y rúbricas
✅ Plan anual y 36 planes de clase editables (5 HC semanales)
✅ Recursos digitales del proyecto

Propuesta para el programa institucional del Plan Optativo (no es un programa oficial del MEC).
Consultas: [completar contacto del titular]
"""

REDES = """Análisis y Diseño de Sistemas para 3.º BTI: una colección anual completa para el Plan Optativo.

El curso parte de un problema real —la biblioteca de un colegio— y llega a un prototipo web probado, documentado y defendido por cada estudiante. Cinco productos coherentes entre sí: libro del estudiante, cuaderno de prácticas, guía docente con solucionario, plan anual y 36 planes de clase editables.

• Aprendizaje basado en proyectos, de punta a punta
• Evaluación por evidencias, con rúbricas y seis hitos integradores
• Formato oficio, listo para imprimir a doble faz

Propuesta para el programa institucional del Plan Optativo; no es un programa oficial del MEC.
Más información: [completar contacto del titular]
#BTI #Informática #Paraguay #PlanOptativo #AnálisisYDiseño
"""

import sys
from lib import *
from lib import _ppr

T = 21
doc = nuevo_documento("vertical", (1.6, 2.0, 1.4, 2.0),
                      pie="Química 3.º · Plan Específico CBT · Informe de revisión v3")
BL = {"color": "FFFFFF", "b": True}
PAGINAS = dict(zip(["planes", "anual", "matriz"], sys.argv[2:5]))


def titulo(txt, before=200):
    p = doc.add_paragraph(style="Plan de Clase")
    _ppr(p, keep_next=True, before=before, after=60)
    add_runs(p, [(txt, {})], size=25)


def texto(partes, after=70, keep_next=False):
    return parrafo(doc, partes, size=T, before=0, after=after, line=252, keep_next=keep_next)


def vinetas(items):
    for it in items:
        texto(it if isinstance(it, list) else [("• ", {}), (it, {})], after=40)


def tabla_simple(anchos, cab, filas, size=20):
    t = tabla(doc, anchos)
    fila(t, [dict(txt=[(h, BL)], fill=OSCURO, size=size) for h in cab], header=True, keep_next=True)
    for f in filas:
        fila(t, [dict(txt=[(f[0], {"b": True})], size=size)] + [dict(txt=x, size=size) for x in f[1:]])
    separador(doc, 80, keep_next=False)
    return t


p = doc.add_paragraph(style="Plan de Clase")
_ppr(p, keep_next=True, before=0, after=40)
add_runs(p, [("Informe de revisión y control · Química 3.º · v3", {})], size=30)
texto("Plan Específico Ciencias Básicas y Tecnología · Año lectivo 2026 · Revisión del 21/10/2026")
texto("Documentos base (v2, conservados sin cambios en la carpeta de Drive): Planes de clase v2 COMPACTO, Plan Anual v2, "
      "Matriz curricular v2 e Informe de control v2. Entregables: los tres documentos con sufijo v3_REVISADO y este informe.")

titulo("1. Resultado en síntesis", before=120)
vinetas([
    f"Planes de clase: 36 planes en {PAGINAS['planes']} páginas A4, uno por página (el plan N.º n ocupa la página n). "
    "Sin guías de aplicación, ejemplos resueltos, prácticas ni claves independientes.",
    f"Plan Anual: documento independiente de {PAGINAS['anual']} páginas A4 horizontales (la v2 ocupaba 17). "
    "Tema, capacidades, indicadores, procedimientos e instrumentos coinciden textualmente con los 36 planes.",
    f"Matriz curricular: {PAGINAS['matriz']} páginas A4 horizontales; encuentros y evidencias por capacidad derivados de los planes.",
    "Auditoría automática sobre los DOCX finales: 0 fallos (tiempos, subdivisiones, coherencia planes–anual–matriz, "
    "clase 36, anonimización y residuos). Los controles se probaron con una copia alterada a propósito y detectaron los "
    "defectos introducidos. Validación del esquema OOXML: aprobada en los tres documentos.",
    "No se pudo consultar el programa oficial del MEC: la red del entorno bloqueó todas las fuentes (sección 7). "
    "Las verificaciones curriculares siguen pendientes y así se declara en cada documento.",
])

titulo("2. Errores científicos y pedagógicos corregidos en los planes")
tabla_simple([1.3, 7.6, 8.1], ["Clase", "Problema en v2", "Corrección en v3"], [
    ("7", "Emisión beta menos de «³₂H»: núcleo inexistente (Z = 2 corresponde al helio).", "Tritio, ³₁H (producto: ³₂He)."),
    ("8", "La errata del programa («Fusion») se presentaba a los estudiantes en el Inicio; «E = Δmc²»; el indicador de fusión no tenía ecuación propia.",
     "Nota para el docente en el Desarrollo; ΔE = Δm·c²; se agregó la verificación de ²₁H + ³₁H → ⁴₂He + ¹₀n."),
    ("12", "Tres indicadores genéricos para cuatro capacidades; ninguno remitía a C2 ni a C3–C4 por separado.",
     "Cuatro indicadores, cada uno ligado a una tarea de la prueba (C1, C2, C3–C4 y autocorrección)."),
    ("16", "Indicador «Balancea conservando átomos y carga» sin tarea que evaluara carga; tres indicadores para C3–C6.",
     "Un indicador y una tarea por capacidad (C3, C4, C5, C6)."),
    ("35", "Un indicador mezclaba nomenclatura (C8) y ecuación (C9); «(10 min)» duplicado en el texto; devolución individual prometida sin tiempo para corregir.",
     "Cuatro indicadores (C7–C10); la devolución individual escrita pasa al Inicio de la clase 36."),
    ("36", "Un indicador fusionaba C8 y C9; sin actividad para quienes no tenían pendientes.",
     "Cuatro indicadores y cuatro tareas evaluables; transferencia con butanoato de metilo; C1–C6 explícitamente fuera."),
    ("6", "Indicador vago («Explica una aplicación redox con evidencia química»).", "«Explica la corrosión del hierro como proceso redox», con actividad asociada."),
    ("10", "«Gráfico concentración tiempo»; expresión de velocidad solo literal.", "«Concentración-tiempo»; v = −(1/a)·Δ[A]/Δt = (1/b)·Δ[B]/Δt."),
    ("18", "Indicador «Integra geometría e hibridación…» sin actividad que lo evaluara.",
     "«Selecciona el modelo adecuado…» con consigna sobre He₂ en la aplicación individual."),
    ("20", "Indicador ambiguo «concentraciones de bases distintas» (puede leerse como bases químicas).",
     "«Concentraciones expresadas sobre masa y sobre volumen»."),
    ("25, 30", "«Cloruro de etanoilo/propanoilo»; el indicador pedía cuatro estructuras y la consigna tenía tres.",
     "«Etanoílo/propanoílo»; se agregó el ácido butanoico."),
    ("27", "Confusión señalada solo entre sulfuro orgánico e ion sulfato.", "Sulfuro orgánico, ion sulfuro (S²⁻) e ion sulfato (SO₄²⁻)."),
    ("28", "«Cuatro enlaces suelen requerir carga positiva».", "Un N con cuatro enlaces y sin par libre lleva carga +1."),
    ("29", "Nota curricular dirigida a los estudiantes en el Inicio; «polinucleados» solo carbocíclicos.",
     "Interpretación declarada para el docente; se agrega la quinolina (polinuclear nitrogenado)."),
    ("31, 32", "Redundancia «catalizada por ácido… catalizador ácido»; oxidación de tiol sin coeficientes.",
     "Doble flecha con H⁺; saponificación no reversible; 4 RSH + O₂ → 2 RSSR + 2 H₂O."),
    ("33", "Oración incompleta («y simultáneamente el enlace C–Br hacia Br»).", "Segunda flecha descrita completa: del enlace C–Br hacia el Br."),
    ("4, 13, 14", "Excepciones y ángulos sin precisar.", "Peróxidos e hidruros; boro con seis electrones en BF₃; ángulos 109,5°, ≈107° y ≈104,5°."),
])
texto("Se verificaron con cálculo propio todos los datos numéricos de las consignas (estequiometría, semividas, "
      "velocidades, concentraciones, balances de masa y carga). Los resultados no se incluyen en los planes porque "
      "la consigna pedía no incorporar solucionarios; pueden entregarse en un documento docente aparte si se solicita.")

titulo("3. Tiempos y viabilidad")
texto("En v2 solo las clases 12, 16 y 35 tenían el Desarrollo subdividido. En v3 las 36 clases detallan cada actividad "
      "del Desarrollo con sus minutos y una fila «Total 80 min»; la auditoría lee esos valores del DOCX y confirma que "
      "suman en las 36 clases.")
tabla_simple([1.3, 5.5, 5.4, 4.8], ["Clase", "v2", "v3", "Motivo"], [
    ("12", "15 + 50 (35 + 10 + 5) + 15", "10 + 60 (40 + 10 + 10) + 10",
     "Cuatro tareas en 35 min y devolución por indicador en el mismo Cierre no eran viables."),
    ("16", "15 + 50 (35 + 10 + 5) + 15; 5 min para entrevistar «dos o tres estudiantes por grupo»",
     "10 + 60 (40 + 10 + 10) + 10; entrevistas a 3–4 estudiantes mientras el grupo se autoevalúa",
     "Tiempo de prueba suficiente; devolución individual en la clase 17."),
    ("35", "10 + 60 (40 + 10 + 10) + 10, con devolución individual en el Cierre", "Misma distribución; devolución individual al inicio de la clase 36",
     "No se puede corregir y devolver por escrito en 10 min."),
    ("24", "Circuito de cuatro estaciones sin tiempo asignado", "15 + 50 (12 + 24 + 14) + 15", "Seis minutos por estación."),
    ("36", "15 + 50 + 15 para tres tareas, comparación y registro", "10 + 60 (15 + 20 + 15 + 10) + 10", "Tiempo explícito por capacidad."),
])
texto("Las clases 13 y 17 reservan 5 minutos del Inicio para entregar la devolución de las evaluaciones 12 y 16.")

titulo("4. Clase 36: capacidad declarada y evidencia")
tabla_simple([1.5, 7.0, 8.5], ["Cap.", "Indicador", "Evidencia concreta y evaluable"], [
    ("C7", "Calcula el volumen de alícuota de una dilución con sus unidades.", "Cálculo: 100 mL a 0,0800 mol/L desde 0,400 mol/L."),
    ("C8", "Nombra un éster y los productos de su hidrólisis básica.", "Nombre de CH₃CH₂COOCH₂CH₃ y de sus productos."),
    ("C9", "Escribe la ecuación de hidrólisis básica conservando átomos y carga.", "Ecuación balanceada con NaOH."),
    ("C10", "Representa con flechas el ataque nucleofílico al carbonilo y la carga del intermedio.", "Mecanismo dibujado con flechas y carga."),
])
texto("C1–C6 no se atribuyen a la clase 36: sus evidencias están en las clases 1–18 (valoradas en las clases 12 y 16).")

titulo("5. Diseño y estructura")
vinetas([
    "Se conserva la identidad visual de la plantilla v2 (Calibri, morados 4A148C/6A1B9A/F3E5F5, bordes grises, A4). "
    "El Plan Anual y la matriz, que usaban Arial y encabezados marrones, se unificaron con esa identidad.",
    "Contraste: la banda «EVALUACIÓN» tenía texto negro sobre 4A148C (1,8:1, ilegible al imprimir); ahora es blanco (11,9:1). "
    "Rótulos blancos sobre 6A1B9A: 9,4:1.",
    "Cada plan conserva identificación (docente, institución, sección y fecha en blanco), capacidad con su código, "
    "indicadores, Inicio/Desarrollo/Cierre con tiempos y total, recursos, procedimientos e instrumentos, observaciones y firmas.",
    "Evaluación sin repeticiones: la v2 repetía el instrumento «Lista de cotejo y producción individual» en 27 planes y "
    "empezaba los 36 procedimientos con «Revisión individual…»; el Plan Anual repetía el mismo procedimiento en 34 filas. "
    "En v3 cada clase nombra su procedimiento y los criterios de su instrumento; que los indicadores son los criterios "
    "se declara una sola vez, en el Plan Anual.",
    "Tipografía: cuerpo de 11 pt (v2: 10,5 pt), márgenes laterales de 2 cm, superior de 1,6 cm e inferior de 1,4 cm. "
    "Exponentes y subíndices con caracteres o formato de Word, sin el símbolo «^».",
    "Paginación: título con «Conservar con el siguiente» y salto de página anterior; tablas con rejilla real "
    "(tblGrid + layout fijo) y sin propiedades duplicadas; filas cortas no divisibles y fila Desarrollo divisible; "
    "encabezado de MOMENTOS repetible; control de viudas y huérfanas activo.",
    "Pie con campos reales «Página X de Y» y nombre del documento; se eliminaron 112 partes de encabezado y pie sin uso "
    "heredadas (de 116, solo 4 estaban referenciadas). Idioma de revisión: español.",
    "Plan Anual: tabla de 7 columnas con anchos proporcionales (26,7 cm útiles) en lugar de 7 columnas iguales; "
    "bandas de etapa y de unidad, encabezado repetido y filas que no se cortan. Matriz: evidencias completas por clase "
    "(la v2 listaba solo los títulos de las tres primeras clases de cada capacidad).",
])

titulo("6. Anonimización")
texto("En los tres documentos y en este informe no hay nombres personales ni referencias a la institución de origen en "
      "cuerpo, encabezados, pies ni propiedades. No hay comentarios ni cambios controlados. Autor, último editor, empresa "
      "y administrador están vacíos y no hay propiedades personalizadas. Docente, institución, sección, turno y fecha "
      "quedan como campos en blanco. Se conservan los términos científicos (estructuras de Lewis, nomenclatura de Stock).")

titulo("7. Fuentes consultadas y alcance curricular")
texto([("Fuentes oficiales efectivamente consultadas: ninguna. ", {"b": True}),
       ("No se pudo abrir el programa del MEC ni ninguna resolución. La política de red del entorno bloqueó los "
        "dominios informacionpublica.paraguay.gov.py, dspacereva.conacyt.gov.py, siteal.iiep.unesco.org, scribd.com y "
        "academia.edu. Las búsquedas en Drive (por título y por frases de las capacidades) no encontraron una copia del "
        "programa de este Plan Específico.", {})])
texto([("Pistas obtenidas solo de listados del buscador (sin abrir los documentos): ", {"b": True}),
       ("un PDF titulado «enfasiscienciasbasicasytecnologia.pdf» en el repositorio del CONACYT "
        "(dspacereva.conacyt.gov.py/jspui-repo/bitstream/123456789/133/1/), probablemente el programa buscado; y notas de "
        "prensa que atribuyen a la Resolución MEC N.º 2065/2025 el calendario 2026 (23/02 al 30/11; receso del 13 al 24 de "
        "julio). Ninguno de estos datos se presenta como verificado.", {})])
tabla_simple([4.2, 12.8], ["Tipo", "Contenido"], [
    ("Comprobado en fuente oficial", "Nada en esta revisión."),
    ("Comprobado internamente", "Corrección química y numérica de las consignas; sumas de tiempos; coherencia textual "
     "planes–anual–matriz; anonimización; validez OOXML."),
    ("Decisión didáctica", "2 HC por encuentro con HC de 40 min; 36 encuentros y su reparto mensual; secuencia de "
     "unidades; momentos de evaluación (1, 12, 16, 24, 35, 36); interpretación de «Fusion» (I3) y de «bases "
     "cuaternarias y polinucleados» (I5)."),
    ("Pendiente de verificación", "Texto y páginas de las capacidades; malla de la p. 20 y carga horaria; duración de la "
     "hora cátedra; vigencia del programa de 2014; texto de la Resolución 2065/2025; incidencias I1–I8 de la matriz."),
])

titulo("8. Control visual: alcance real")
vinetas([
    "Render completo de los cuatro documentos con LibreOffice 24.2 a PDF y a imágenes. Calibri se sustituyó por "
    "Carlito, que tiene las mismas métricas: la paginación debería coincidir con Word, pero no se verificó en "
    "Microsoft Word.",
    "Planes: las 36 páginas se revisaron una por una, de a dos por imagen. En esa revisión se corrigieron la línea de "
    "observaciones que se partía, el exponente de la clase 9 y el nombre de la unidad 8, que ocupaba dos renglones. "
    "Después de esos cambios se volvió a renderizar y a revisar la serie completa. Llenado medido: entre 66 % y 89 % "
    "de la altura de página; ninguna clase pasa a una segunda página.",
    f"Plan Anual: {PAGINAS['anual']} páginas revisadas. Se corrigieron una página casi vacía, el encabezado «OBSERVACIONES» "
    "partido, «Septiembre» y «Noviembre» cortados en la columna TIEMPO y la bibliografía dividida entre dos páginas.",
    f"Matriz: {PAGINAS['matriz']} páginas revisadas. Se corrigieron la fila I8 aislada y una última página con un solo bloque.",
    "Informe: todas sus páginas revisadas tras el render final.",
])

titulo("9. Incidencias pendientes")
vinetas([
    "Cotejar capacidades, contenidos y páginas con el PDF oficial (sugerido: descargar el archivo del repositorio del "
    "CONACYT y subirlo a la carpeta para una revisión posterior).",
    "Confirmar la carga semanal de Química específica (malla de la p. 20) y la duración de la hora cátedra en la "
    "institución; si difieren, reajustar los minutos de cada momento.",
    "Confirmar el calendario 2026 con el texto de la Resolución 2065/2025 y ajustar los meses al día de clase y a los feriados.",
    "Validar con el departamento de Ciencias la interpretación de «bases cuaternarias y polinucleados en combinaciones» (clase 29).",
    "Abrir los DOCX en Microsoft Word y comprobar que cada plan siga ocupando una página (actualizar campos con F9 si "
    "el pie muestra «Página 1 de 1»).",
])

separador(doc, 200, keep_next=False)
parrafo(doc, "Revisión independiente: ______________________     Fecha: ____ / ____ / 2026", size=T, keep_lines=True)

guardar(doc, sys.argv[1])
print("ok")

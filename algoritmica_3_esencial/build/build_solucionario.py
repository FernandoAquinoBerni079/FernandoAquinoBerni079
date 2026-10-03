# -*- coding: utf-8 -*-
"""Solucionario Docente — Edición Esencial Comercial 2026. Se genera desde las mismas fuentes que el libro
(actividades.py, practicas.py, evaluaciones.py, preliminares.py): no puede quedar ninguna respuesta de ejercicios viejos."""
import os, re, json
import maqueta as M
from estructura import cargar
import ediciones, actividades, practicas, evaluaciones, preliminares as PRE
from build_libro import a_pdf

B = '/home/claude/alg3/build/'; OUT = '/home/claude/alg3/salida_v2_1/'
NOMBRE = 'Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026_v2_1'
pre, C, _, U = cargar()
ediciones.aplicar(C)


def entradas():
    E = [(1, 'Prueba diagnóstica — Orientaciones de corrección'), (1, 'Primera parte — Actividades de aplicación')]
    for n in range(1, 22):
        E.append((2, 'Clase %d — %s' % (n, C[n]['titulo'])))
    E.append((1, 'Segunda parte — Prácticas: resultado esperado y errores frecuentes'))
    for n in range(1, 22):
        E.append((2, 'Práctica %d — %s' % (n, practicas.PR[n]['titulo'])))
    E.append((1, 'Tercera parte — Evaluaciones: claves y criterios'))
    for e in evaluaciones.EV:
        E.append((2, 'Clave — ' + e['titulo']))
    E.append((1, 'Proyecto Final Integrador — Orientaciones y rúbrica'))
    return E


def construir(pags=None):
    d = M.nuevo_doc('Algorítmica · 3.er Curso · Solucionario del docente', 'Material exclusivo del docente',
                    'Algorítmica; BTI; 3.er Curso; solucionario')
    M.imagen_pagina_completa(d, B + 'portadas/portada_solucionario.jpg')
    cuerpo = M.portada_en_seccion(d)
    M.heading(d, 'Presentación', 1, estilo='Título preliminar')
    for t in ['Este solucionario es material exclusivo del docente. Contiene, con la misma numeración del libro del estudiante, las respuestas de todas las actividades de aplicación de las 21 clases, las orientaciones para corregir la prueba diagnóstica y las claves de las cuatro evaluaciones de unidad y de las dos integradoras de etapa, con el desarrollo de los cálculos.',
              'Incluye además, para cada una de las 21 prácticas del libro, el resultado esperado y los errores frecuentes que conviene vigilar durante la sesión, y las orientaciones y la rúbrica del Proyecto Final Integrador. El libro del estudiante no contiene respuestas: los puntos de control de las prácticas permiten verificar el trabajo sin revelar el resultado.',
              'Las capacidades de cada ficha se reproducen textualmente del programa MEC vigente; los indicadores de logro son operativizaciones observables. Los algoritmos de las Prácticas 1 a 3 se ejecutaron en PSeInt 20250314 con el perfil Flexible, que es el perfil de referencia del libro. Los procedimientos de Access toman como referencia Access 2016 en castellano y no se ejecutaron en el programa: los resultados de las consultas se verificaron con un script sobre los mismos datos.',
              'Los números del caso Copetín Karumbé cierran en una recaudación de G. 134.000 (semana del 3 al 5 de marzo, usada en las clases) y de G. 135.000 (semana del 9 al 11 de marzo, usada en las prácticas de Access 18 a 21). Todas las cifras de este solucionario se verificaron con un script antes de la edición.']:
        M.par(d, t)
    M.heading(d, 'Índice', 1, salto=True, estilo='Título preliminar')
    E = entradas()
    M.indice(d, E, pags)
    # diagnóstica
    M.heading(d, E[0][1], 1, salto=True)
    M.par(d, 'La prueba no lleva nota. Sirve para conocer el punto de partida del grupo y calibrar el ritmo de las unidades 1 y 4.', 10, italic=True)
    for i, (q, o) in enumerate(PRE.DIAGNOSTICA, 1):
        M.par(d, 'Consigna %d — %s' % (i, o), 10, indent=0.2, despues=3)
    # primera parte
    M.heading(d, E[1][1], 1, salto=True)
    u_prev = None
    for n in range(1, 22):
        if C[n]['unidad'] != u_prev:
            u_prev = C[n]['unidad']
            M.par(d, 'UNIDAD %d — %s' % (u_prev, U[u_prev]), 11, True, color=M.DARK, antes=8, keep=True)
        M.heading(d, 'Clase %d — %s' % (n, C[n]['titulo']), 2)
        fam_prev = None
        for fam, k, enun, resp, nuevo in actividades.items(n):
            if fam != fam_prev:
                M.par(d, fam.split(' (')[0] + ':', 9.5, True, color=M.MED, keep=True, antes=3, despues=1)
                fam_prev = fam
            M.par(d, '%d. %s' % (k, resp), 9.5, indent=0.3, despues=2)
    # segunda parte
    M.heading(d, E[23][1], 1, salto=True)
    M.par(d, 'Para cada práctica: el resultado esperado (lo que el docente debe ver al recorrer los puestos o al corregir) y los errores frecuentes que conviene anticipar. Los puntos de control del libro remiten a estos resultados sin revelarlos.', 10, italic=True)
    for n in range(1, 22):
        p = practicas.PR[n]
        M.heading(d, 'Práctica %d — %s' % (n, p['titulo']), 2)
        q = M.par(d, '', 9.5, despues=2); M.run(q, 'Entorno: ', True, size=9.5); M.run(q, p['entorno'] + ' · ' + str(len(p['acts'])) + ' actividades.', size=9.5)
        q = M.par(d, '', 9.5, despues=2); M.run(q, 'Resultado esperado: ', True, size=9.5, color=M.DARK); M.run(q, p['sol']['resultado'], size=9.5)
        q = M.par(d, '', 9.5, despues=2 if p.get('transfer') else 4); M.run(q, 'Errores frecuentes: ', True, size=9.5, color='A04000'); M.run(q, p['sol']['errores'], size=9.5)
        if p.get('transfer'):
            q = M.par(d, '', 9.5, despues=4); M.run(q, 'Transferencia y revisión entre pares: ', True, size=9.5, color=M.DARK); M.run(q, p['transfer']['sol'], size=9.5)
    # tercera parte
    M.heading(d, E[45][1], 1, salto=True)
    M.par(d, 'Puntaje sugerido para cada evaluación: Parte A, 1 punto por ítem (3 puntos); Parte B, 3 puntos por ítem (15 puntos); total 18 puntos. En las preguntas abiertas se acepta cualquier respuesta equivalente que cumpla el criterio indicado.', 10, italic=True)
    for e in evaluaciones.EV:
        M.heading(d, 'Clave — ' + e['titulo'], 2)
        M.par(d, 'Parte A', 9.5, True, color=M.MED, keep=True, despues=1)
        k = 0
        for enun, ops, letra in e['mc']:
            k += 1
            M.par(d, '%d. %s) %s' % (k, letra, ops['abc'.index(letra)]), 9.5, indent=0.3, despues=1)
        M.par(d, 'Parte B', 9.5, True, color=M.MED, keep=True, antes=3, despues=1)
        for enun, resp in e['ab']:
            k += 1
            M.par(d, '%d. %s' % (k, resp), 9.5, indent=0.3, despues=2)
    # PFI
    M.heading(d, E[-1][1], 1, salto=True)
    M.par(d, 'Orientaciones docentes', 10.5, True, color=M.DARK, keep=True)
    for t in PRE.ORIENTACIONES_PFI:
        M.par(d, '• ' + t, 10, indent=0.3, despues=2)
    M.par(d, 'Rúbrica analítica de evaluación (los pesos suman 100 %)', 10.5, True, color=M.DARK, keep=True, antes=6)
    M.par(d, 'Cada criterio se califica en uno de cuatro niveles. El nivel asigna una parte fija del peso del criterio: Logrado, el 100 %; En proceso, el 60 %; Inicial, el 30 %; No presentado, el 0 %. Cada descriptor dice qué evidencia observable corresponde al nivel. El formulario y el informe son una extensión recomendada: no suman puntaje obligatorio.', 9.5, italic=True)

    def pts(x):
        return ('%g' % x).replace('.', ',')
    filas = []
    for crit, peso, desc in PRE.RUBRICA_ANALITICA:
        filas.append(['%s\n(peso %d %%)' % (crit, peso)] + ['%s pts. %s' % (pts(peso * f), dsc) for (_, f), dsc in zip(PRE.NIVELES, desc)])
    M.tabla(d, ['Criterio'] + ['%s (%d %%)' % (n, round(f * 100)) for n, f in PRE.NIVELES], filas, anchos=[2.9, 3.6, 3.5, 3.5, 3.1], size=8)
    M.par(d, 'Puntaje total: suma de los cinco criterios (máximo 100 puntos).', 9.5, italic=True)
    M.pie_paginas(d, cuerpo)
    M.no_actualizar_campos(d)
    M.purgar_relaciones(d)
    assert sum(int(x[1].split()[0]) for x in PRE.RUBRICA) == 100
    return d, E


if __name__ == '__main__':
    tmp = B + 'tmp/'
    d, E = construir(None)
    p1 = tmp + NOMBRE + '.docx'; d.save(p1); pdf1 = a_pdf(p1, tmp)
    import pymupdf
    doc = pymupdf.open(pdf1)
    idx_last = max(i for i, pg in enumerate(doc) if re.search(r'\.{5,}\s*000', pg.get_text())) + 1
    pags, total = M.paginas_de(pdf1, [t for _, t in E], desde=idx_last + 1)
    for it in range(3):
        d, E = construir(pags)
        out = OUT + NOMBRE + '.docx'; d.save(out); pdf = a_pdf(out, OUT)
        pags2, total = M.paginas_de(pdf, [t for _, t in E], desde=idx_last + 1)
        if pags2 == pags:
            break
        pags = pags2
    json.dump({'entradas': E, 'paginas': pags, 'total': total}, open(B + 'indice_sol.json', 'w'), ensure_ascii=False, indent=1)
    print('Solucionario: páginas', total, 'índice verificado =', pags2 == pags)

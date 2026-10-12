# -*- coding: utf-8 -*-
"""Genera los HTML de portada (libro, solucionario, plan anual, planes), contraportada y lámina,
y los rasteriza con Chromium (render.js) a JPG A4."""
import os, subprocess
D = '/home/claude/alg1/build/portadas/'
F = 'fonts/'
CSS = """
@font-face{font-family:'Merri';font-weight:700;src:url('%(f)su-4D0qyriQwlOrhSvowK_l5UcA6zuSYEqOzpPe3HOZJ5eX1WtLaQwmYiScCmDxhtNOKl8yDrOSAqEw.ttf');}
@font-face{font-family:'Mont';font-weight:400;src:url('%(f)sJTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCtr6Ew-.ttf');}
@font-face{font-family:'Mont';font-weight:600;src:url('%(f)sJTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCu170w-.ttf');}
@font-face{font-family:'Mont';font-weight:800;src:url('%(f)sJTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCvr70w-.ttf');}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:216mm;height:330mm}
body{background:#1B5E20;color:#fff;font-family:'Mont',sans-serif;position:relative;overflow:hidden}
.top{position:absolute;top:0;left:0;right:0;height:19mm;background:#123F16;display:flex;align-items:center;justify-content:center;
     font-weight:800;font-size:11.5pt;letter-spacing:.6pt}
.bot{position:absolute;bottom:0;left:0;right:0;height:30mm;background:#123F16;text-align:center;padding-top:8mm}
.bot .p{font-size:9.6pt;opacity:.9;font-weight:400}
.bot .r{font-size:13pt;font-weight:800;margin-top:4mm}
.ser{font-family:'Merri';font-weight:700;text-align:center}
.big{font-family:'Mont';font-weight:800;color:#F2C14E;text-align:center;letter-spacing:1pt}
.pill{display:inline-block;background:#fff;color:#1B5E20;font-weight:800;border-radius:9mm;padding:1.6mm 7mm;font-size:16pt}
.card{position:absolute;left:21mm;right:21mm;background:#fff;border-radius:6mm;color:#333;text-align:center}
.ltl{font-weight:800;color:#2E7D32;font-size:11.5pt;letter-spacing:.4pt}
.h{font-weight:800;color:#1B5E20}
.lin{width:62%%;height:1px;background:#C8E6C9;margin:5mm auto}
.lst{font-size:11.4pt;line-height:1.95;color:#444}
.acc{color:#2E7D32;font-size:10.8pt;margin-top:9mm}
"""


def lamina_svg():
    # esquema propio: diagrama de Venn, tabla de verdad y decisión de un algoritmo
    return """
<svg viewBox="0 0 600 380" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" font-family="Mont">
 <rect x="0" y="0" width="600" height="380" rx="18" fill="#F4FBF5"/>
 <g font-size="13">
  <rect x="24" y="22" width="270" height="170" rx="6" fill="#fff" stroke="#1B5E20" stroke-width="2"/>
  <text x="36" y="42" fill="#1B5E20" font-weight="800">U</text>
  <ellipse cx="120" cy="112" rx="70" ry="55" fill="#2E7D32" fill-opacity=".18" stroke="#2E7D32" stroke-width="2.5"/>
  <ellipse cx="198" cy="112" rx="70" ry="55" fill="#B8860B" fill-opacity=".18" stroke="#B8860B" stroke-width="2.5"/>
  <text x="88" y="70" fill="#1B5E20" font-weight="800">A</text><text x="222" y="70" fill="#8A6508" font-weight="800">B</text>
  <text x="96" y="118" fill="#333" text-anchor="middle">chipa</text><text x="159" y="118" fill="#333" text-anchor="middle" font-weight="800">mixta</text><text x="224" y="118" fill="#333" text-anchor="middle">jugo</text>
  <text x="159" y="184" fill="#616161" text-anchor="middle" font-size="12">A ∩ B = {mixta}</text>
  <rect x="320" y="22" width="256" height="170" rx="6" fill="#fff" stroke="#1565C0" stroke-width="2"/>
  <rect x="320" y="22" width="256" height="30" rx="6" fill="#1565C0"/>
  <text x="362" y="42" fill="#fff" font-weight="800" text-anchor="middle">p</text><text x="412" y="42" fill="#fff" font-weight="800" text-anchor="middle">q</text><text x="500" y="42" fill="#fff" font-weight="800" text-anchor="middle">p → q</text>
  <text x="362" y="78" text-anchor="middle" fill="#333">V</text><text x="412" y="78" text-anchor="middle" fill="#333">V</text><text x="500" y="78" text-anchor="middle" fill="#1B5E20" font-weight="800">V</text>
  <text x="362" y="111" text-anchor="middle" fill="#333">V</text><text x="412" y="111" text-anchor="middle" fill="#333">F</text><text x="500" y="111" text-anchor="middle" fill="#C62828" font-weight="800">F</text>
  <text x="362" y="144" text-anchor="middle" fill="#333">F</text><text x="412" y="144" text-anchor="middle" fill="#333">V</text><text x="500" y="144" text-anchor="middle" fill="#1B5E20" font-weight="800">V</text>
  <text x="362" y="177" text-anchor="middle" fill="#333">F</text><text x="412" y="177" text-anchor="middle" fill="#333">F</text><text x="500" y="177" text-anchor="middle" fill="#1B5E20" font-weight="800">V</text>
  <rect x="30" y="218" width="110" height="34" rx="17" fill="#2E7D32"/><text x="85" y="240" fill="#fff" text-anchor="middle" font-weight="800">Inicio</text>
  <line x1="140" y1="235" x2="186" y2="235" stroke="#616161" stroke-width="2.5"/>
  <polygon points="266,199 346,235 266,271 186,235" fill="#FFF4D6" stroke="#B8860B" stroke-width="2.5"/>
  <text x="266" y="232" fill="#5A4200" text-anchor="middle" font-weight="800">total</text><text x="266" y="248" fill="#5A4200" text-anchor="middle" font-weight="800">&gt;= 50000</text>
  <line x1="346" y1="235" x2="388" y2="235" stroke="#616161" stroke-width="2.5"/><text x="356" y="227" fill="#2E7D32" font-weight="800">V</text>
  <rect x="388" y="217" width="184" height="36" fill="#fff" stroke="#2E7D32" stroke-width="2"/><text x="480" y="240" fill="#1B5E20" text-anchor="middle" font-weight="800">10 % de descuento</text>
  <rect x="30" y="290" width="542" height="70" rx="8" fill="#fff" stroke="#2E7D32" stroke-width="1.5"/>
  <text x="46" y="314" fill="#333" font-family="monospace">Si total &gt;= 50000 Entonces</text>
  <text x="46" y="334" fill="#333" font-family="monospace">    cobrar ← total − total * 10 / 100</text>
  <text x="46" y="352" fill="#616161" font-size="11">pseudocódigo, prueba de escritorio y, al cierre del año, PSeInt</text>
 </g>
</svg>"""


def html(body, css_extra=''):
    return '<!doctype html><html><head><meta charset="utf-8"><style>%s%s</style></head><body>%s</body></html>' % (CSS % {'f': F}, css_extra, body)


TOP = '<div class="top">BACHILLERATO TÉCNICO EN SERVICIOS &nbsp;·&nbsp; ESPECIALIDAD INFORMÁTICA</div>'
BOT = '<div class="bot"><div class="p">Programa de estudio del Ministerio de Educación y Ciencias · Diseño Curricular de Informática</div><div class="r">República del Paraguay · 2026</div></div>'
TIT = '''<div style="position:absolute;top:37mm;left:0;right:0">
 <div class="ser" style="font-size:25pt">Conjuntos, lógica y algoritmos</div>
 <div class="big" style="font-size:58pt;margin-top:3mm">ALGORÍTMICA</div>
 <div style="text-align:center;margin-top:3mm"><span class="pill">1.er Curso</span></div></div>'''


def libro():
    body = TOP + TIT + '''
<div style="position:absolute;top:116mm;left:24mm;right:24mm;height:122mm;border:3mm solid #fff;border-radius:5mm;background:#F4FBF5;overflow:hidden">%s</div>
<div style="position:absolute;top:249mm;left:0;right:0;text-align:center">
 <div style="font-weight:800;font-size:17pt">Libro del estudiante con prácticas</div>
 <div style="font-size:11.4pt;opacity:.92;margin-top:3mm">Enfoque «Aprender Haciendo» &nbsp;·&nbsp; Conjuntos, lógica y pseudocódigo</div>
 <div style="font-size:11.4pt;opacity:.92;margin-top:2mm">Caso integrador: Copetín Karumbé</div></div>''' % lamina_svg() + BOT
    return html(body)


def docente(titulo, lineas, acompana='Acompaña al libro del estudiante con prácticas'):
    body = TOP + TIT + '''
<div class="card" style="top:120mm;height:112mm;padding-top:14mm">
 <div class="ltl">MATERIAL DEL DOCENTE</div>
 <div class="h" style="font-size:31pt;margin-top:6mm">%s</div>
 <div class="lin"></div>
 <div class="lst">%s</div>
 <div class="acc">%s</div></div>''' % (titulo, '<br>'.join(lineas), acompana) + BOT
    return html(body)


def contra():
    def li(t):
        return '<div style="display:flex;gap:4mm;align-items:flex-start;margin:2.4mm 0"><span style="color:#F2C14E;font-size:14pt;line-height:1">●</span><span>%s</span></div>' % t
    body = '''
<div style="position:absolute;top:24mm;left:0;right:0;text-align:center">
 <div class="ser" style="font-size:22pt">Algorítmica · Conjuntos, lógica y algoritmos</div>
 <div style="font-size:11.5pt;opacity:.9;margin-top:3mm">1.er Curso · Bachillerato Técnico en Servicios · Especialidad Informática</div></div>
<div style="position:absolute;top:64mm;left:22mm;right:22mm;font-size:12pt">
 <div style="color:#F2C14E;font-weight:800;font-size:17pt;margin-bottom:3mm">En este libro</div>
 %s
 <div style="color:#F2C14E;font-weight:800;font-size:17pt;margin:9mm 0 3mm">Para el docente</div>
 %s
</div>
<div style="position:absolute;top:238mm;left:30mm;right:30mm;height:30mm;background:#123F16;border-radius:5mm;text-align:center;padding-top:7mm">
 <div style="color:#F2C14E;font-weight:800;font-size:13.5pt">Enfoque «Aprender Haciendo»</div>
 <div style="font-size:11pt;margin-top:2mm">Caso integrador: Copetín Karumbé</div></div>
<div class="bot" style="padding-top:12mm"><div class="r" style="margin:0">República del Paraguay · 2026</div></div>''' % (
        ''.join(li(t) for t in ['21 clases desarrolladas con ejemplos resueltos y diagramas', '21 prácticas paso a paso con puntos de control para verificar tu trabajo',
                                 'Teoría de conjuntos, lógica simbólica e introducción a la algoritmia', 'Prueba diagnóstica, 3 evaluaciones de unidad y 2 de etapa',
                                 'Proyecto Final Integrador para la Feria de Informática']),
        ''.join(li(t) for t in ['Solucionario docente con todas las respuestas', 'Plan anual de 37 encuentros (4 horas cátedra semanales)', '37 planes de clase listos para usar']))
    return html(body)


PIEZAS = {
 'portada_libro': libro(),
 'portada_solucionario': docente('Solucionario', ['Respuestas de las 21 clases, la prueba diagnóstica', 'y las 5 evaluaciones, con el desarrollo de los cálculos', 'Resultados esperados de las 21 prácticas', 'Errores frecuentes a vigilar en cada práctica', 'Orientaciones y rúbrica del Proyecto Final Integrador']),
 'portada_plan_anual': docente('Plan anual', ['37 encuentros de 4 horas cátedra en dos etapas', 'Temas, indicadores de logro, procedimientos', 'e instrumentos de evaluación por encuentro']),
 'portada_planes': docente('Planes de clase', ['37 planes de 4 horas cátedra, listos para usar', '21 clases, 14 jornadas de continuación', 'y 2 evaluaciones integradoras de etapa', 'Capacidad, indicadores, momentos didácticos,', 'recursos y criterios de evaluación en cada plan']),
 'contraportada': contra(),
}

if __name__ == '__main__':
    for k, v in PIEZAS.items():
        open(D + k + '.html', 'w').write(v)
    subprocess.run(['node', D + 'render.js'] + list(PIEZAS), check=True, cwd=D)

    from PIL import Image
    for k in PIEZAS:
        Image.open(D + k + '.png').convert('RGB').save(D + k + '.jpg', quality=92)

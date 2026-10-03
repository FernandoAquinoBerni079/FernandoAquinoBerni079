# -*- coding: utf-8 -*-
"""Genera los HTML de portada (libro, solucionario, plan anual, planes), contraportada y lámina,
y los rasteriza con Chromium (render.js) a JPG A4."""
import os, subprocess
D = '/home/claude/alg2/build/portadas/'
F = 'fonts/'
CSS = """
@font-face{font-family:'Merri';font-weight:700;src:url('%(f)su-4D0qyriQwlOrhSvowK_l5UcA6zuSYEqOzpPe3HOZJ5eX1WtLaQwmYiScCmDxhtNOKl8yDrOSAqEw.ttf');}
@font-face{font-family:'Mont';font-weight:400;src:url('%(f)sJTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCtr6Ew-.ttf');}
@font-face{font-family:'Mont';font-weight:600;src:url('%(f)sJTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCu170w-.ttf');}
@font-face{font-family:'Mont';font-weight:800;src:url('%(f)sJTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCvr70w-.ttf');}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:210mm;height:297mm}
body{background:#1B5E20;color:#fff;font-family:'Mont',sans-serif;position:relative;overflow:hidden}
.top{position:absolute;top:0;left:0;right:0;height:19mm;background:#123F16;display:flex;align-items:center;justify-content:center;
     font-weight:800;font-size:11.5pt;letter-spacing:.6pt}
.bot{position:absolute;bottom:0;left:0;right:0;height:30mm;background:#123F16;text-align:center;padding-top:7mm}
.bot .p{font-size:9.6pt;opacity:.9;font-weight:400}
.bot .r{font-size:13pt;font-weight:800;margin-top:3.2mm}
.ser{font-family:'Merri';font-weight:700;text-align:center}
.big{font-family:'Mont';font-weight:800;color:#F2C14E;text-align:center;letter-spacing:1pt}
.pill{display:inline-block;background:#fff;color:#1B5E20;font-weight:800;border-radius:9mm;padding:1.6mm 7mm;font-size:16pt}
.card{position:absolute;left:21mm;right:21mm;background:#fff;border-radius:6mm;color:#333;text-align:center}
.ltl{font-weight:800;color:#2E7D32;font-size:11.5pt;letter-spacing:.4pt}
.h{font-weight:800;color:#1B5E20}
.lin{width:62%%;height:1px;background:#C8E6C9;margin:5mm auto}
.lst{font-size:11.4pt;line-height:1.95;color:#444}
.acc{color:#2E7D32;font-size:10.8pt;margin-top:8mm}
"""


def lamina_svg():
    # esquema propio: decisión en un flujograma, un vector recorrido y una consulta filtrada
    return """
<svg viewBox="0 0 600 380" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" font-family="Mont">
 <rect x="0" y="0" width="600" height="380" rx="18" fill="#F4FBF5"/>
 <g font-size="13">
  <rect x="40" y="26" width="120" height="34" rx="17" fill="#2E7D32"/><text x="100" y="48" fill="#fff" text-anchor="middle" font-weight="800">Inicio</text>
  <line x1="100" y1="60" x2="100" y2="82" stroke="#616161" stroke-width="2.5"/>
  <polygon points="100,82 170,120 100,158 30,120" fill="#FFF4D6" stroke="#B8860B" stroke-width="2.5"/>
  <text x="100" y="117" fill="#5A4200" text-anchor="middle" font-weight="800">monto</text><text x="100" y="133" fill="#5A4200" text-anchor="middle" font-weight="800">&gt;= 50000</text>
  <line x1="170" y1="120" x2="215" y2="120" stroke="#616161" stroke-width="2.5"/><text x="180" y="112" fill="#2E7D32" font-weight="800">Sí</text>
  <rect x="215" y="102" width="130" height="36" fill="#fff" stroke="#2E7D32" stroke-width="2"/><text x="280" y="125" fill="#1B5E20" text-anchor="middle" font-weight="800">descuento</text>
  <line x1="100" y1="158" x2="100" y2="182" stroke="#616161" stroke-width="2.5"/><text x="108" y="176" fill="#C62828" font-weight="800">No</text>
  <rect x="40" y="182" width="120" height="34" rx="17" fill="#2E7D32"/><text x="100" y="204" fill="#fff" text-anchor="middle" font-weight="800">Fin</text>
  <text x="380" y="40" fill="#1B5E20" font-weight="800">ventas[7]</text>
  <g font-size="12">
   <rect x="380" y="50" width="28" height="30" fill="#fff" stroke="#2E7D32" stroke-width="2"/><rect x="408" y="50" width="28" height="30" fill="#fff" stroke="#2E7D32" stroke-width="2"/>
   <rect x="436" y="50" width="28" height="30" fill="#fff" stroke="#2E7D32" stroke-width="2"/><rect x="464" y="50" width="28" height="30" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
   <rect x="492" y="50" width="28" height="30" fill="#fff" stroke="#2E7D32" stroke-width="2"/><rect x="520" y="50" width="28" height="30" fill="#fff" stroke="#2E7D32" stroke-width="2"/>
   <rect x="548" y="50" width="28" height="30" fill="#fff" stroke="#2E7D32" stroke-width="2"/>
   <text x="394" y="98" text-anchor="middle" fill="#616161">1</text><text x="422" y="98" text-anchor="middle" fill="#616161">2</text><text x="450" y="98" text-anchor="middle" fill="#616161">3</text>
   <text x="478" y="98" text-anchor="middle" fill="#B8860B" font-weight="800">i</text><text x="506" y="98" text-anchor="middle" fill="#616161">5</text><text x="534" y="98" text-anchor="middle" fill="#616161">6</text><text x="562" y="98" text-anchor="middle" fill="#616161">7</text>
  </g>
  <text x="380" y="132" fill="#333">Para i &lt;- 1 Hasta 7</text><text x="396" y="152" fill="#333">total &lt;- total + ventas[i]</text>
  <rect x="30" y="245" width="540" height="112" rx="8" fill="#fff" stroke="#1565C0" stroke-width="2"/>
  <rect x="30" y="245" width="540" height="28" rx="8" fill="#1565C0"/>
  <text x="46" y="264" fill="#fff" font-weight="800">Productos · filtro: stock &lt; 10</text>
  <text x="46" y="296" fill="#333">MIX-01</text><text x="150" y="296" fill="#333">Sándwich mixto</text><text x="520" y="296" fill="#1B5E20" text-anchor="end" font-weight="800">8</text>
  <text x="46" y="322" fill="#333">SOP-01</text><text x="150" y="322" fill="#333">Sopa paraguaya</text><text x="520" y="322" fill="#1B5E20" text-anchor="end" font-weight="800">6</text>
  <text x="46" y="346" fill="#616161" font-size="11">los demás registros siguen en la tabla: el filtro no borra</text>
 </g>
</svg>"""


def html(body, css_extra=''):
    return '<!doctype html><html><head><meta charset="utf-8"><style>%s%s</style></head><body>%s</body></html>' % (CSS % {'f': F}, css_extra, body)


TOP = '<div class="top">BACHILLERATO TÉCNICO EN SERVICIOS &nbsp;·&nbsp; ESPECIALIDAD INFORMÁTICA</div>'
BOT = '<div class="bot"><div class="p">Programa de estudio del Ministerio de Educación y Ciencias · Diseño Curricular de Informática</div><div class="r">República del Paraguay · 2026</div></div>'
TIT = '''<div style="position:absolute;top:33mm;left:0;right:0">
 <div class="ser" style="font-size:25pt">Algoritmos, archivos y consultas</div>
 <div class="big" style="font-size:58pt;margin-top:3mm">ALGORÍTMICA</div>
 <div style="text-align:center;margin-top:3mm"><span class="pill">2.º Curso</span></div></div>'''


def libro():
    body = TOP + TIT + '''
<div style="position:absolute;top:104mm;left:24mm;right:24mm;height:110mm;border:3mm solid #fff;border-radius:5mm;background:#F4FBF5;overflow:hidden">%s</div>
<div style="position:absolute;top:224mm;left:0;right:0;text-align:center">
 <div style="font-weight:800;font-size:17pt">Libro del estudiante con prácticas de laboratorio</div>
 <div style="font-size:11.4pt;opacity:.92;margin-top:3mm">Enfoque «Aprender Haciendo» &nbsp;·&nbsp; PSeInt y Microsoft Access</div>
 <div style="font-size:11.4pt;opacity:.92;margin-top:1.5mm">Caso integrador: Copetín Karumbé</div></div>''' % lamina_svg() + BOT
    return html(body)


def docente(titulo, lineas, acompana='Acompaña al libro del estudiante con prácticas de laboratorio'):
    body = TOP + TIT + '''
<div class="card" style="top:108mm;height:112mm;padding-top:13mm">
 <div class="ltl">MATERIAL DEL DOCENTE</div>
 <div class="h" style="font-size:31pt;margin-top:5mm">%s</div>
 <div class="lin"></div>
 <div class="lst">%s</div>
 <div class="acc">%s</div></div>''' % (titulo, '<br>'.join(lineas), acompana) + BOT
    return html(body)


def contra():
    def li(t):
        return '<div style="display:flex;gap:4mm;align-items:flex-start;margin:2.4mm 0"><span style="color:#F2C14E;font-size:14pt;line-height:1">●</span><span>%s</span></div>' % t
    body = '''
<div style="position:absolute;top:22mm;left:0;right:0;text-align:center">
 <div class="ser" style="font-size:22pt">Algorítmica · Algoritmos, archivos y consultas</div>
 <div style="font-size:11.5pt;opacity:.9;margin-top:3mm">2.º Curso · Bachillerato Técnico en Servicios · Especialidad Informática</div></div>
<div style="position:absolute;top:58mm;left:22mm;right:22mm;font-size:12pt">
 <div style="color:#F2C14E;font-weight:800;font-size:17pt;margin-bottom:3mm">En este libro</div>
 %s
 <div style="color:#F2C14E;font-weight:800;font-size:17pt;margin:9mm 0 3mm">Para el docente</div>
 %s
</div>
<div style="position:absolute;top:214mm;left:30mm;right:30mm;height:30mm;background:#123F16;border-radius:5mm;text-align:center;padding-top:6mm">
 <div style="color:#F2C14E;font-weight:800;font-size:13.5pt">Enfoque «Aprender Haciendo»</div>
 <div style="font-size:11pt;margin-top:2mm">Caso integrador: Copetín Karumbé</div></div>
<div class="bot" style="padding-top:11mm"><div class="r" style="margin:0">República del Paraguay · 2026</div></div>''' % (
        ''.join(li(t) for t in ['21 clases desarrolladas con ejemplos resueltos y diagramas', '21 prácticas paso a paso en PSeInt, en el Explorador de archivos y en Microsoft Access',
                                 'Estructuras de control, vectores, matrices, módulos, archivos y consultas', 'Prueba diagnóstica, 4 evaluaciones de unidad y 2 de etapa',
                                 'Proyecto Final Integrador para la Feria de Informática']),
        ''.join(li(t) for t in ['Solucionario docente con todas las respuestas', 'Plan anual de 36 encuentros (4 horas cátedra semanales)', '36 planes de clase listos para usar']))
    return html(body)


PIEZAS = {
 'portada_libro': libro(),
 'portada_solucionario': docente('Solucionario', ['Respuestas de las 21 clases, la prueba diagnóstica', 'y las 6 evaluaciones, con el desarrollo de los cálculos', 'Resultados esperados de las 21 prácticas', 'Errores frecuentes a vigilar en cada práctica', 'Orientaciones y rúbrica del Proyecto Final Integrador']),
 'portada_plan_anual': docente('Plan anual', ['36 encuentros de 4 horas cátedra en dos etapas', 'Temas, indicadores de logro, procedimientos', 'e instrumentos de evaluación por encuentro']),
 'portada_planes': docente('Planes de clase', ['36 planes de 4 horas cátedra, listos para usar', '21 clases, 10 continuaciones prácticas,', '3 talleres del proyecto y 2 evaluaciones de etapa', 'Capacidad, indicadores, momentos didácticos,', 'recursos y criterios de evaluación en cada plan']),
 'contraportada': contra(),
}

if __name__ == '__main__':
    for k, v in PIEZAS.items():
        open(D + k + '.html', 'w').write(v)
    subprocess.run(['node', D + 'render.js'] + list(PIEZAS), check=True, cwd=D)

    from PIL import Image
    for k in PIEZAS:
        Image.open(D + k + '.png').convert('RGB').save(D + k + '.jpg', quality=92)

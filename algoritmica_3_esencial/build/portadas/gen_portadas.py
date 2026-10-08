# -*- coding: utf-8 -*-
"""Genera los HTML de portada (libro, solucionario, plan anual, planes), contraportada y lámina,
y los rasteriza con Chromium (render.js) a JPG A4."""
import os, subprocess
D = '/home/claude/alg3/build/portadas/'
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
    # esquema: dos tablas relacionadas + DER + consulta (dibujo vectorial propio, no ilustración)
    return """
<svg viewBox="0 0 600 380" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" font-family="Mont">
 <rect x="0" y="0" width="600" height="380" rx="18" fill="#F4FBF5"/>
 <g font-size="13">
  <rect x="30" y="38" width="170" height="30" rx="6" fill="#2E7D32"/><text x="115" y="58" fill="#fff" text-anchor="middle" font-weight="800">CLIENTES</text>
  <rect x="30" y="68" width="170" height="104" fill="#fff" stroke="#2E7D32" stroke-width="2"/>
  <text x="42" y="92" fill="#1B5E20" font-weight="800">🔑 código</text><text x="42" y="118" fill="#333">nombre</text><text x="42" y="144" fill="#333">teléfono</text>
  <rect x="400" y="38" width="170" height="30" rx="6" fill="#2E7D32"/><text x="485" y="58" fill="#fff" text-anchor="middle" font-weight="800">VENTAS</text>
  <rect x="400" y="68" width="170" height="104" fill="#fff" stroke="#2E7D32" stroke-width="2"/>
  <text x="412" y="92" fill="#1B5E20" font-weight="800">🔑 código</text><text x="412" y="118" fill="#333">fecha</text><text x="412" y="144" fill="#1565C0" font-weight="800">cliente (FK)</text>
  <path d="M200 88 C 300 88, 300 140, 400 140" stroke="#B8860B" stroke-width="3" fill="none"/>
  <text x="207" y="82" fill="#B8860B" font-weight="800">1</text><text x="385" y="132" fill="#B8860B" font-weight="800">∞</text>
  <rect x="30" y="215" width="120" height="44" fill="#2E7D32" stroke="#1B5E20" stroke-width="2"/><text x="90" y="242" fill="#fff" text-anchor="middle" font-weight="800">VENTA</text>
  <polygon points="200,237 260,207 320,237 260,267" fill="#FFF4D6" stroke="#B8860B" stroke-width="2.5"/><text x="260" y="242" fill="#5A4200" text-anchor="middle" font-weight="800">contiene</text>
  <rect x="370" y="215" width="140" height="44" fill="#2E7D32" stroke="#1B5E20" stroke-width="2"/><text x="440" y="242" fill="#fff" text-anchor="middle" font-weight="800">PRODUCTO</text>
  <line x1="150" y1="237" x2="200" y2="237" stroke="#616161" stroke-width="2.5"/><line x1="320" y1="237" x2="370" y2="237" stroke="#616161" stroke-width="2.5"/>
  <text x="162" y="228" fill="#1B5E20" font-weight="800">N</text><text x="350" y="228" fill="#1B5E20" font-weight="800">M</text>
  <rect x="30" y="292" width="540" height="62" rx="8" fill="#fff" stroke="#1565C0" stroke-width="2"/>
  <text x="46" y="318" fill="#1565C0" font-weight="800">SELECT</text><text x="112" y="318" fill="#333">categoría, Sum(cantidad*precio_unitario)</text>
  <text x="46" y="342" fill="#1565C0" font-weight="800">GROUP BY</text><text x="130" y="342" fill="#333">categoría</text>
  <text x="560" y="342" fill="#2E7D32" text-anchor="end" font-weight="800">G. 134.000</text>
 </g>
</svg>"""


def html(body, css_extra=''):
    return '<!doctype html><html><head><meta charset="utf-8"><style>%s%s</style></head><body>%s</body></html>' % (CSS % {'f': F}, css_extra, body)


TOP = '<div class="top">BACHILLERATO TÉCNICO EN SERVICIOS &nbsp;·&nbsp; ESPECIALIDAD INFORMÁTICA</div>'
BOT = '<div class="bot"><div class="p">Programa de estudio del Ministerio de Educación y Ciencias · Diseño Curricular de Informática</div><div class="r">República del Paraguay · 2026</div></div>'
TIT = '''<div style="position:absolute;top:37mm;left:0;right:0">
 <div class="ser" style="font-size:25pt">Lenguajes y bases de datos</div>
 <div class="big" style="font-size:58pt;margin-top:3mm">ALGORÍTMICA</div>
 <div style="text-align:center;margin-top:3mm"><span class="pill">3.er Curso</span></div></div>'''


def libro():
    body = TOP + TIT + '''
<div style="position:absolute;top:116mm;left:24mm;right:24mm;height:122mm;border:3mm solid #fff;border-radius:5mm;background:#F4FBF5;overflow:hidden">%s</div>
<div style="position:absolute;top:249mm;left:0;right:0;text-align:center">
 <div style="font-weight:800;font-size:17pt">Libro del estudiante con prácticas de laboratorio</div>
 <div style="font-size:11.4pt;opacity:.92;margin-top:3mm">Enfoque «Aprender Haciendo» &nbsp;·&nbsp; PSeInt y Microsoft Access</div>
 <div style="font-size:11.4pt;opacity:.92;margin-top:2mm">Caso integrador: Copetín Karumbé</div></div>''' % lamina_svg() + BOT
    return html(body)


def docente(titulo, lineas, acompana='Acompaña al libro del estudiante con prácticas de laboratorio'):
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
 <div class="ser" style="font-size:27pt">Algorítmica · Lenguajes y bases de datos</div>
 <div style="font-size:11.5pt;opacity:.9;margin-top:3mm">3.er Curso · Bachillerato Técnico en Servicios · Especialidad Informática</div></div>
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
        ''.join(li(t) for t in ['21 clases desarrolladas con ejemplos del caso integrador', '21 prácticas paso a paso en PSeInt, en papel y en Microsoft Access',
                                 'Diseño Entidad-Relación, normalización hasta 3FN y consultas', 'Prueba diagnóstica, 4 evaluaciones de unidad y 2 de etapa',
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

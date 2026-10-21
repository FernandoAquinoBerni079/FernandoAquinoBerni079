import re, sys, zipfile, docx
O = "out/"
P = docx.Document(O + "Quimica_3_CBT_Planes_de_Clase_2026_v3_REVISADO.docx")
A = docx.Document(O + "Quimica_3_CBT_Plan_Anual_2026_v3_REVISADO.docx")
M = docx.Document(O + "Quimica_3_CBT_Matriz_Curricular_2026_v3_REVISADO.docx")
fallos = []
def ok(c, m):
    if not c: fallos.append(m)
# --- Planes: leer del DOCX
titulos = [p.text for p in P.paragraphs if p.style.name == "Plan de Clase"]
ok(len(titulos) == 36, f"títulos {len(titulos)}")
ok([int(re.search(r"N\.º (\d+)", t).group(1)) for t in titulos] == list(range(1, 37)), "numeración")
tabs = P.tables
ok(len(tabs) == 36 * 5, f"tablas {len(tabs)}")
planes = {}
for i in range(36):
    ident, capind, mom, rec, ev = tabs[5*i:5*i+5]
    filas = {r.cells[0].text: r for r in mom.rows}
    def mins(t): return int(re.match(r"(\d+) min", t).group(1))
    ti, td, tc = (mins(filas[k].cells[2].text) for k in ("Inicio", "Desarrollo", "Cierre"))
    tot = mins(mom.rows[-1].cells[-1].text)
    sub = sum(int(x) for x in re.findall(r"\((\d+) min\)", filas["Desarrollo"].cells[1].text))
    ok(ti + td + tc == tot == 80, f"clase {i+1}: {ti}+{td}+{tc} != {tot}")
    ok(sub == td, f"clase {i+1}: subdivisiones {sub} != {td}")
    inds = [l[2:] for l in capind.rows[1].cells[1].text.split("\n")]
    caps = re.findall(r"^(C\d+) ·", capind.rows[0].cells[1].text, re.M)
    planes[i+1] = dict(tema=titulos[i].split("  ·  ", 1)[1], ind=inds, caps=caps,
                       proc=ev.rows[1].cells[1].text, inst=ev.rows[2].cells[1].text, rec=rec.rows[0].cells[1].text)
    ok(len(set(c._tc for c in ident.rows[3].cells)) == 4 and "____" in ident.rows[3].cells[1].text, f"clase {i+1}: institución no en blanco")
    ok("____" in ident.rows[0].cells[1].text, f"clase {i+1}: docente no en blanco")
# --- Plan Anual: tabla de secuencia
seq = [t for t in A.tables if t.rows[0].cells[0].text == "N.º"][0]
anual = {}
for r in seq.rows[1:]:
    cs = []
    for c in r.cells:
        if not cs or c._tc is not cs[-1]._tc: cs.append(c)
    if len(cs) == 7:
        n = int(cs[0].text)
        tema, capsl = cs[1].text.split("\n")
        anual[n] = dict(tema=tema, caps=capsl.split(", "), ind=[l[2:] for l in cs[2].text.split("\n")],
                        proc=cs[4].text, inst=cs[5].text)
ok(sorted(anual) == list(range(1, 37)), "anual: encuentros")
for n in range(1, 37):
    for k in ("tema", "caps", "ind", "proc", "inst"):
        ok(anual[n][k] == planes[n][k], f"anual≠plan clase {n} campo {k}: {anual[n][k]!r} / {planes[n][k]!r}")
# --- Matriz
mt = M.tables[0]
for r in mt.rows[1:]:
    cap = r.cells[0].text.split(" ·")[0]
    ns = [int(x) for x in r.cells[2].text.split(", ")]
    esperado = [n for n in range(1, 37) if cap in planes[n]["caps"]]
    ok(ns == esperado, f"matriz {cap}: {ns} vs {esperado}")
    evn = [int(x) for x in re.findall(r"Cl\. (\d+):", r.cells[3].text)]
    ok(evn == esperado, f"matriz {cap}: evidencias {evn}")
# --- Clase 36: cada capacidad con indicador y tarea propia
c36 = planes[36]
for cap in c36["caps"]:
    ok(any(f"({cap})" in i for i in c36["ind"]), f"clase 36: {cap} sin indicador")
ok(set(c36["caps"]) == {"C7", "C8", "C9", "C10"}, "clase 36 capacidades")
# --- Residuos y anonimización en TODAS las partes
for f in ["Quimica_3_CBT_Planes_de_Clase_2026_v3_REVISADO.docx", "Quimica_3_CBT_Plan_Anual_2026_v3_REVISADO.docx",
          "Quimica_3_CBT_Matriz_Curricular_2026_v3_REVISADO.docx"] + sys.argv[1:]:
    z = zipfile.ZipFile(O + f)
    todo = " ".join(z.read(n).decode("utf8", "ignore") for n in z.namelist() if n.endswith((".xml", ".rels")))
    for pat in [r"(?i)villarrica", r"(?i)colegio nacional", r"(?i)guía de aplicación", r"(?i)ejemplo resuelto",
                r"(?i)clave y explicación", r"w:author=", r"<w:comment ", r"<w:ins ", r"<w:del ", r"(?i)solucionario",
                r"<dc:creator>[^<]", r"<cp:lastModifiedBy>[^<]", r"(?i)<Company>[^<]", r"(?i)<Manager>[^<]", r"\^\("]:
        ok(not re.search(pat, todo), f"{f}: residuo {pat}")
    ok(not any("comments" in n or "custom.xml" in n for n in z.namelist()), f"{f}: partes de comentarios/propiedades personalizadas")
print("FALLOS:", len(fallos)); print("\n".join(fallos))

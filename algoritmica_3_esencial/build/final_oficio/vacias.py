import sys,pymupdf
def fill(p):
    bl=[b for b in p.get_text('blocks') if not b[4].strip().startswith('Página')]
    ys=[b[3] for b in bl]+[dr['rect'].y1 for dr in p.get_drawings()]
    for im in p.get_images(full=True):
        ys+=[r.y1 for r in p.get_image_rects(im[0])]
    return round(max(ys)/p.rect.height,2) if ys else 0
d=pymupdf.open(sys.argv[1]); print(len(d),'pags; <25%:',[(i+1,fill(p)) for i,p in enumerate(d) if fill(p)<0.25])

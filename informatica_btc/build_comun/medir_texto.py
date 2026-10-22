"""Mide la altura (px) de cada línea de texto oscuro de una imagen y la convierte a cuerpo aproximado (pt) al ancho final."""
import sys, numpy as np
from PIL import Image
def lineas(ruta, umbral=110):
    a = np.asarray(Image.open(ruta).convert('L')).astype(int)
    oscuro = a < umbral
    filas = oscuro.sum(1)
    res = []; dentro = False
    for y, v in enumerate(filas):
        if v > 3 and not dentro: ini = y; dentro = True
        elif v <= 3 and dentro:
            dentro = False
            if 6 <= y - ini <= 60: res.append((ini, y - ini))
    return a.shape[1], res
if __name__ == '__main__':
    for ruta in sys.argv[2:]:
        ancho_cm = float(sys.argv[1]); w, ls = lineas(ruta)
        pxcm = w / ancho_cm
        hs = sorted(h for _, h in ls)
        # cuerpo ≈ altura de la línea con ascendentes/descendentes / 0,95 ; 1 pt = 0,03528 cm
        pt = [round(h / pxcm / 0.03528 / 0.95, 1) for h in hs[:3]]
        print(ruta.split('/')[-1], 'líneas', len(ls), 'alturas mínimas px', hs[:3], '≈ pt', pt)

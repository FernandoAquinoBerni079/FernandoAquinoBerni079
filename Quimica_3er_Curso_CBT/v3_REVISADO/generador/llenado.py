import sys,glob
from PIL import Image
for f in sorted(glob.glob(sys.argv[1])):
    im=Image.open(f).convert('L'); w,h=im.size
    px=im.load()
    # última fila con tinta por encima del pie (ignora 7% inferior)
    last=0
    for y in range(int(h*0.93)):
        if any(px[x,y]<200 for x in range(0,w,3)): last=y
    print(f.split('/')[-1], f"{100*last/h:.0f}%")

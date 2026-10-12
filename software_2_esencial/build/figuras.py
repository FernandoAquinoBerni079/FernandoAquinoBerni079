# -*- coding: utf-8 -*-
"""Una sola vez sobre src_md: numeración correlativa por clase (Figura N.k, clase y práctica), epígrafes sin
«generada con IA», y las imágenes de la práctica que repiten una de su clase se reemplazan por la remisión."""
import re, glob
S = '/home/claude/sw2/src_md/'
def cap_limpio(c):
    c = re.sub(r'^(Figura|Fotografía) [0-9P]+(\.[0-9]+)? — ', '', c.strip())
    c = re.sub(r'\s*\(imagen generada con IA\)\.?', '.', c)
    c = re.sub(r'\.\.+', '.', c)
    return c.strip()
log = []
for n in range(1, 21):
    k = 0; donde = {}
    for f, tipo in ((S + 'tomo_clase%02d.md' % n, 'C'), (S + 'lab_practica%02d.md' % n, 'P')):
        L = open(f).read().split('\n'); out = []; i = 0
        while i < len(L):
            m = re.match(r'\[\[IMG (\S+)\|([\d.]+)\]\]', L[i])
            if m:
                arch = m.group(1); cap = L[i + 1]
                if tipo == 'P' and arch in donde:
                    out.append('Para esta práctica, tené a mano la %s de la Clase %d.' % (donde[arch], n))
                    log.append((n, 'práctica: remite a ' + donde[arch], arch))
                else:
                    if arch.startswith('T_') and tipo == 'P':
                        log.append((n, 'AVISO: imagen del tomo de otra clase', arch))
                    k += 1; lab = 'Figura %d.%d' % (n, k); donde[arch] = lab
                    out.append(L[i]); out.append('%s — %s' % (lab, cap_limpio(cap)))
                i += 2; continue
            out.append(L[i]); i += 1
        open(f, 'w').write('\n'.join(out))
for x in log: print(x)
print(sum('generada con IA' in open(f).read() for f in glob.glob(S + '*.md')), 'archivos con «generada con IA»')

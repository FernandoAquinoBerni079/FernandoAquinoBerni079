import re,sys
S='/home/claude/sw2/src_md/'
def dev_words(n):
    L=open(S+'tomo_clase%02d.md'%n).read().split('\n')
    end=next(i for i,l in enumerate(L) if l.startswith('## Actividades'))
    w=0; inside=None; skipnext=False
    for l in L[1:end]:
        if skipnext: skipnext=False; continue
        if l.startswith('[[FICHA]]'): inside='F'; continue
        if l.startswith('[[/FICHA]]'): inside=None; continue
        if l.startswith('[[TABLA]]'): inside='T'; continue
        if l.startswith('[[/TABLA]]'): inside=None; continue
        if inside: continue
        if l.startswith('[[IMG'): skipnext=True; continue
        if l.startswith('## ') or l.startswith('[[/CAJA'): continue
        if l.startswith('[[CAJA'):
            t=l[7:-2]
            if ' / ' in t: l=t.split(' / ',1)[1]
            else: continue
        w+=len(re.findall(r'\w+',l))
    return w
if __name__=='__main__':
    for n in range(1,21): print(n, dev_words(n))

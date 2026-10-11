import sys,glob,os,re
S='/home/claude/sw2/src_md/'
for f in sorted(glob.glob(S+'amp/clase*.md')):
    n=int(re.search(r'(\d+)',os.path.basename(f)).group(1))
    p=S+'tomo_clase%02d.md'%n; s=open(p).read(); a=open(f).read().strip()+'\n'
    first=a.split('\n')[0]
    if first in s:
        i=s.index(first); j=s.index('## Actividades de aplicación')
        s=s[:i]+s[j:]
    s=s.replace('## Actividades de aplicación', a+'## Actividades de aplicación',1); open(p,'w').write(s)

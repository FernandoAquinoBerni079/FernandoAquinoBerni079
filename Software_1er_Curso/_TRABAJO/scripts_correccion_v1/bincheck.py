import itertools
b=lambda n: format(n,'b')
# fixed triples (a,op,b) in decimal, with label
fixed = {
 'C20 expl suma1 (Fig 20.1)':(11,'+',6),'C20 expl suma2':(13,'+',11),
 'C20 expl resta1':(13,'-',5),'C20 expl resta2':(18,'-',7),
 'C20 expl mult1':(5,'*',3),'C20 expl mult2':(6,'*',5),
 'C20 expl div1':(12,'/',4),'C20 expl div2':(45,'/',5),
 'C20 compl2':(9,'-',3),
 'C20 it2':(14,'+',5),'C20 it3':(6,'*',3),'C20 it10':(60,'/',6),
 'C20 it11a':(23,'+',13),'C20 it11b':(20,'-',11),
 'P20 suma':(22,'+',13),'P20 resta':(26,'-',11),'P20 mult':(11,'*',3),'P20 desafio':(72,'/',8),
 'EU3 a':(14,'+',11),'EU3 b':(21,'-',6),'EU3 c':(7,'*',5),'EU3 d':(18,'/',3),
 'EI2 a':(27,'+',14),'EI2 b':(22,'-',9),'EI2 c':(13,'*',2),'EI2 d':(21,'/',7),
}
def res(a,o,c): return {'+':a+c,'-':a-c,'*':a*c,'/':a//c}[o]
def nums(t): a,o,c=t; return {a,c,res(a,o,c)}
def check(d, verbose=True):
  bad=[]
  for (k1,t1),(k2,t2) in itertools.combinations(d.items(),2):
    s=nums(t1)&nums(t2)
    if len(s)>=2: bad.append((k1,k2,sorted(s)))
  if verbose:
    for x in bad: print('  CHOQUE',x)
  return bad
if __name__=='__main__':
  import sys
  cur=dict(fixed); cur.update({'C20 stock':(11,'+',6),'C20 it4':(15,'/',5),'C20 it8':(11,'-',6),'C20 it12s':(6,'+',5),'C20 it12r':(6,'-',5),'P20 div':(30,'/',6)})
  print('VERSIÓN AUDITADA:'); check(cur)

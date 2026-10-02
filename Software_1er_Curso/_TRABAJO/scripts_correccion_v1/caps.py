C={
1:'Identifica las características principales de la Informática.',
2:'Analiza los antecedentes históricos de la informática.',
3:'Identifica los elementos básicos de la computadora.',
4:'Reconoce las ventajas, desventajas, usos, aplicaciones y conexiones de las diferentes unidades de almacenamiento.',
5:'Analiza las normas éticas y de seguridad vigentes en el ámbito informático.',
6:'Analiza las características principales de los diferentes tipos de software.',
7:'Reflexiona sobre las aplicaciones actuales de la informática.',
8:'Analiza el propósito y los objetivos de un sistema operativo.',
9:'Reconoce el origen y evolución de los Sistemas Operativos.',
10:'Reconoce las ventajas y desventajas de los Sistemas Operativos actuales.',
11:'Analiza los diferentes tipos de licencias de software presentes en entornos modernos de computación.',
12:'Analiza el funcionamiento del Sistema Operativo y del Sistema de Aplicación.',
13:'Reconoce los diferentes tipos de administración de procesos utilizados en los Sistemas Operativos.',
14:'Identifica los diferentes tipos de Sistemas de Archivos utilizados por los Sistemas operativos.',
15:'Identifica los diferentes tipos de memoria.',
16:'Analiza el funcionamiento de la administración de memoria.',
17:'Reconoce la importancia de la capacidad de abstracción, análisis y síntesis en los trabajos realizados.',
18:'Reconoce los diferentes tipos de Sistemas de Numeración utilizados en la informática.',
19:'Aplica procedimientos para convertir un número entero o fraccionario de cualquier base.',
20:'Resuelve operaciones con números binarios.',
}
U1=[1,2,3,4,5,6,7]; U2=[8,9,10,11,12,13,14,15,16,17]; U3=[18,19,20]
# secuencia del Plan Anual / Plan de Clase -> capacidades oficiales
SEQ={1:[1],2:[1],3:[1],4:[1],5:[2],6:[3],7:[3],8:[3],9:[4],10:[4],11:[5],12:[5],
13:[6,7],14:[6],15:[3,4,5,6],16:U1,17:U1,18:U1,
19:[8],20:[9,10],21:[10],22:[11,12],23:[13],24:[13],25:[13],26:[13],27:[14],28:[15,16],
29:[8,9,10,11,12,13,14,15,16],30:[17,13,14,15],
31:[18,19],32:[19],33:[19],34:[20],35:U3,36:U2+U3}
# 36 lists all of U2 incl. 17 + U3 — in Plan anual se resume por altura de fila
# clase del libro -> capacidades
CLASE={1:[1],2:[1],3:[1],4:[2],5:[3],6:[3],7:[4],8:[5],9:[6,7],10:[8],11:[9,10],12:[11,12],
13:[13],14:[13],15:[14],16:[15,16],17:[18,19],18:[19],19:[19],20:[20]}
assert set(c for v in SEQ.values() for c in v)==set(C), 'falta cubrir alguna capacidad'

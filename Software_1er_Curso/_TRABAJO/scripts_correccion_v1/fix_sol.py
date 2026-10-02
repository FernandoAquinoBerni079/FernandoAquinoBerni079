import docx
from ed import *
doc=docx.Document('Gabinete_Informatica_Software_1er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026.docx')
replace(doc,'11. Diseñador: SSD de 480 GB (₲ 280.000) por velocidad de lectura/escritura. Despensa: HDD de 1 TB (₲ 350.000) por capacidad económica para respaldos.',
 '11. Diseñador: SSD de 512 GB (₲ 320.000) por su velocidad de lectura/escritura. Despensa: HDD de 3 TB (₲ 560.000) por su menor costo por GB (≈ ₲ 187 frente a ≈ ₲ 625 del SSD) y su amplia capacidad para respaldos.',tag='H5 Clase 7 ítem 11')
replace(doc,'b) Recomendación técnica: SSD de 480 GB (₲ 280.000) para el sistema y los programas (arranque rápido) — los 16 GB de planos caben con holgura; si su archivo crecerá por años, agregar el HDD de 1 TB (₲ 350.000) como unidad de respaldo.',
 'b) Recomendación técnica: SSD de 256 GB (₲ 210.000) para el sistema, los programas y los planos (arranque rápido): los 16 GB de planos caben con holgura. El HDD de 6 TB (₲ 1.020.000) solo se justifica si el archivo va a crecer mucho o se necesita respaldo masivo; para 16 GB es una capacidad desproporcionada y no acelera el arranque.',tag='H5 Integradora 1, 3 b)')
replace(doc,'3. a) 10010 (6×3=18).','3. a) 11110 (10×3=30).',tag='H6 ítem 3')
replace(doc,'4. d) 11 (15÷5=3).','4. d) 101 (20÷4=5).',tag='H6 ítem 4')
replace(doc,'8. VERDADERO (11−6=5).','8. VERDADERO (25−10=15).',tag='H6 ítem 8')
replace(doc,'12. Suma: 110+101 = 1011 (6+5=11 teclados ✓). Diferencia: 110−101 = 1 (6−5=1 teclado ✓).',
 '12. Suma: 1110+1010 = 11000 (14+10=24 teclados ✓). Diferencia: 1110−1010 = 100 (14−10=4 teclados ✓).',tag='H6 ítem 12')
replace(doc,'11110 ÷ 110 = 101 (30÷6=5)','11100 ÷ 100 = 111 (28÷4=7)',tag='H6 Práctica 20')
replace(doc,'d) 110 (18÷3=6 ✓).','d) 1000 (24÷3=8 ✓).',tag='H6 Eval. U3 3 d)')
replace(doc,'b) 1101 (22−9=13 ✓).','b) 10001 (26−9=17 ✓).',tag='H6 Integradora 2, 4 b)')
replace(doc,'10. FALSO — carece de actualizaciones garantizadas y viola la Ley 1328/98.',
 '10. FALSO — una copia no genuina no recibe las mismas garantías ni beneficios que una original y su uso puede implicar infracción de la Ley 1328/98; sin embargo, Microsoft indica que las actualizaciones críticas de seguridad siguen disponibles incluso para Windows no genuino.',tag='H7 Clase 12 ítem 10')
replace(doc,'Desafío: ej. C:\\Oficina\\Documentos\\2026; buscar por nombre o por fecha de modificación en el Explorador.',
 'Paso 5 (síntesis): cuatro líneas, una por problema (síntoma → tema → dato observado → solución); separar el caso en partes evita confundir síntomas y atacar cada causa por separado: abstracción, análisis y síntesis aplicados al diagnóstico. Desafío: ej. C:\\Oficina\\Documentos\\2026; buscar por nombre o por fecha de modificación en el Explorador.',tag='H1 Ficha K')
doc.save('SOL_v2.docx')
for l in LOG: print(l[0],'·',l[3])

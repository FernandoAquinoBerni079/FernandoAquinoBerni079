// Simulación de Apps Script para Entrega_Algoritmica3_Comercial.gs con los bytes reales del commit.
const fs = require('fs'), crypto = require('crypto'), path = require('path'), vm = require('vm');
const SIM = process.argv[2];
const signed = b => Array.from(b, x => x > 127 ? x - 256 : x);
const unsigned = a => Buffer.from(a.map(x => x < 0 ? x + 256 : x));
const gh = fs.readFileSync(SIM + '/listado.txt', 'utf8').trim().split('\n').map(l => { const [sha, size, name] = l.split(' '); return { type: 'file', name, sha, size: +size }; });
let nid = 0; const archivos = {}, carpetas = {};
function carpeta(id, nombre, padre) { carpetas[id] = { id, nombre, padre }; return id; }
function archivo(id, nombre, bytes, padre, mime) { archivos[id] = { id, nombre, bytes, padres: [padre], mime, desc: '', acceso: 'PRIVATE', trashed: false }; }
const CURSO = carpeta('1pxhhdfRZjTVxF06Qn-97AU-Cbqc1X6y-', 'Algoritmica_3er_Curso', 'raiz');
carpeta('trabajo', '_TRABAJO', CURSO);
const ANT = [['1dulBKdlxMmQSn0wBeh7BLC2Y-BUUBGYb','Algoritmica_3er_Curso_TOMO_COMPLETO.docx',3617395],['1L-cawfAcL9NW54BdfwplbbSyJG1yXVWY','Algoritmica_3er_Curso_TOMO_COMPLETO.pdf',3527813],['1Hmrv7Ab9mja0RcvZR58_QoTlD5GkNLJ9','Algoritmica_3er_Curso_CUADERNO_PRACTICAS.docx',301502],['11iXxo6QrLRX9t_500fB0sf7JVnt_p4WS','Algoritmica_3er_Curso_CUADERNO_PRACTICAS.pdf',342456],['1-v-GkSOo2X0q2o5WEfqm8RdilUTxUAU6','Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE.docx',90219],['1d6aIe0-scDUbkpQjBJzkPo3YfuI7dlEA','Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE.pdf',300087],['1gganEyLUD7781Irj7a2WkB8IdKJEAvOY','Algoritmica_3er_Curso_PLAN_ANUAL.docx',44217],['1LvHIDGFUpv2rc_wVHXZEGvL3syDkcvcd','Algoritmica_3er_Curso_PLAN_ANUAL.pdf',142410],['1j1AAGODMLvPUVZIara0eHECAYrRJMiRr','Algoritmica_3er_Curso_PLANES_DE_CLASE.docx',159388],['1a6IPbQG2Hr4QqJ_oYLg4F58tfOJoWCrZ','Algoritmica_3er_Curso_PLANES_DE_CLASE.pdf',1015926]];
ANT.forEach(([id, n, s]) => archivo(id, n, Buffer.alloc(s), CURSO, n.endsWith('pdf') ? 'application/pdf' : 'docx'));
const it = arr => { let i = 0; return { hasNext: () => i < arr.length, next: () => arr[i++] }; };
function F(id) { const a = archivos[id]; return {
  getId: () => id, getName: () => a.nombre, getSize: () => a.bytes.length, getMimeType: () => a.mime,
  getBlob: () => ({ getBytes: () => signed(a.bytes) }), getUrl: () => 'https://drive.google.com/file/d/' + id + '/view',
  setDescription: d => { a.desc = d; }, getDescription: () => a.desc, getSharingAccess: () => a.acceso,
  isTrashed: () => a.trashed, getParents: () => it(a.padres.map(D)), moveTo: c => { a.padres = [c.getId()]; } }; }
function D(id) { const c = carpetas[id]; return {
  getId: () => id, getName: () => c.nombre, getUrl: () => 'https://drive.google.com/drive/folders/' + id,
  getFilesByName: n => it(Object.values(archivos).filter(a => a.padres.includes(id) && a.nombre === n && !a.trashed).map(a => F(a.id))),
  getFiles: () => it(Object.values(archivos).filter(a => a.padres.includes(id) && !a.trashed).map(a => F(a.id))),
  getFoldersByName: n => it(Object.values(carpetas).filter(x => x.padre === id && x.nombre === n).map(x => D(x.id))),
  getFolders: () => it(Object.values(carpetas).filter(x => x.padre === id).map(x => D(x.id))),
  createFolder: n => D(carpeta('f' + (++nid), n, id)),
  createFile: blob => { const fid = 'n' + (++nid); archivo(fid, blob._n, blob._b, id, blob._t); return F(fid); } }; }
const descargas = [];
const ctx = {
  Logger: { log: m => console.log(m) }, console,
  LockService: { getScriptLock: () => ({ tryLock: () => true, releaseLock: () => {} }) },
  PropertiesService: { getScriptProperties: () => ({ getProperty: () => null }) },
  MimeType: { PDF: 'application/pdf' },
  DriveApp: { getFolderById: D, getFileById: F, Access: { PRIVATE: 'PRIVATE' } },
  Utilities: { DigestAlgorithm: { SHA_1: 'sha1', SHA_256: 'sha256' },
    newBlob: s => ({ getBytes: () => signed(Buffer.from(s, 'utf8')) }),
    computeDigest: (alg, arr) => signed(crypto.createHash(alg).update(unsigned(arr)).digest()) },
  UrlFetchApp: { fetch: url => {
    if (url.includes('api.github.com')) { if (!url.includes('?ref=45af175d81a069fc5f6259099108c5aab8185a94')) throw new Error('ref no fijo'); return { getResponseCode: () => 200, getContentText: () => JSON.stringify(gh) }; }
    if (!url.includes('/45af175d81a069fc5f6259099108c5aab8185a94/')) throw new Error('descarga sin commit fijo: ' + url);
    const n = decodeURIComponent(url.split('/').pop()); descargas.push(n); const b = fs.readFileSync(path.join(SIM, n));
    return { getResponseCode: () => 200, getContent: () => signed(b),
      getBlob: () => { const o = { _b: b, _n: null, _t: null }; o.setName = x => { o._n = x; return o; }; o.setContentType = x => { o._t = x; return o; }; return o; } }; } } };
ctx.MimeType.PDF = 'application/pdf';
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(process.argv[3], 'utf8'), ctx);
const correr = f => { try { return vm.runInContext(f + '()', ctx); } catch (e) { console.log('LANZÓ: ' + e.message); return null; } };
console.log('== Compuerta: paso 3 antes del paso 1 ==');
correr('paso3y4_supersedidosEInventarioAlgoritmica3');
console.log('anteriores movidos tras compuerta:', ANT.filter(a => archivos[a[0]].padres[0] !== CURSO).length);
console.log('== Paso 1-2 ==');
const r1 = correr('paso1y2_copiarYVerificarAlgoritmica3');
console.log('descargas:', descargas.length, 'correctos:', r1 && r1.correctos);
console.log('== Paso 1-2 repetido (idempotente) ==');
const r1b = correr('paso1y2_copiarYVerificarAlgoritmica3'); console.log('descargas tras repetir:', descargas.length, 'correctos:', r1b && r1b.correctos);
console.log('== Paso 3-4 ==');
const r3 = correr('paso3y4_supersedidosEInventarioAlgoritmica3');
console.log('verificados', r3 && r3.verificados, 'inventario', r3 && r3.inventarioConforme, r3 && JSON.stringify(r3.subcarpetas), 'supersedidos', r3 && r3.anterioresEnSupersedidos);
console.log('archivos borrados/papelera:', Object.values(archivos).filter(a => a.trashed).length, '· total archivos:', Object.keys(archivos).length);
console.log('== Corrupción simulada de un archivo en Drive ==');
const libro = Object.values(archivos).find(a => a.nombre === 'Algoritmica_3er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026.pdf');
const orig = libro.bytes; libro.bytes = Buffer.from(orig); libro.bytes[1000] ^= 1;
const r4 = correr('informeAlgoritmica3'); console.log('verificados con 1 byte cambiado:', r4.verificados, r4.incidencias);
libro.bytes = orig;
console.log('== Solucionario compartido por enlace ==');
const sol = Object.values(archivos).find(a => a.nombre.startsWith('Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026.pdf')); sol.acceso = 'ANYONE_WITH_LINK';
const r5 = correr('informeAlgoritmica3'); console.log('verificados:', r5.verificados, r5.incidencias);

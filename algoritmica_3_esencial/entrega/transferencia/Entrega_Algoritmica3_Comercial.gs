/**
 * CIERRE COMERCIAL — Algorítmica 3.º Esencial Comercial 2026 (FINAL OFICIO v3, APROBADO por Fer el 12/10/2026)
 * Biblioteca Comercial BTI 2026 · Acta: ACTA_APROBACION_EDITORIAL_ALGORITMICA_3_ESENCIAL_COMERCIAL_2026
 *
 * Agregar como NUEVO ARCHIVO .gs en el proyecto BTI_Software_2_Auditoria_Sync (el que ya funciona).
 * NO reemplazar Código.gs ni Entrega_Software2_v4.gs, NO tocar disparadores.
 *
 * Ejecutar EN ESTE ORDEN, una función por vez, revisando el Registro de ejecución:
 *   1) paso1y2_copiarYVerificarAlgoritmica3   → copia los 9 originales (sin conversión) y los verifica 9/9
 *   2) paso3y4_supersedidosEInventarioAlgoritmica3 → SOLO si 1) terminó «9/9»: mueve los 10 anteriores
 *      a SUPERSEDIDOS (sin borrar) y comprueba que la carpeta quede con los 9 aprobados + subcarpetas
 *   3) informeAlgoritmica3 (solo lectura, repetible) → enlaces, tamaños y hashes para el informe
 *
 * Verificación binaria: para cada archivo en Drive se recalcula el SHA-1 de blob de Git
 * (sha1("blob <tamaño>\0" + bytes)) sobre los bytes que quedaron en Drive y se compara con el del
 * commit fijo; también se informa SHA-256. Nada se borra, nada se convierte, nada se comparte.
 */

const ALG3_COMERCIAL = Object.freeze({
  propietario: 'FernandoAquinoBerni079',
  repositorio: 'FernandoAquinoBerni079',
  commit: '45af175d81a069fc5f6259099108c5aab8185a94',
  rutaOrigen: 'algoritmica_3_esencial/salida_FINAL_OFICIO_v3',
  carpetaCursoId: '1pxhhdfRZjTVxF06Qn-97AU-Cbqc1X6y-',
  carpetaCursoNombre: 'Algoritmica_3er_Curso',
  supersedidos: 'SUPERSEDIDOS',
  subcarpetasAdmitidas: ['_TRABAJO', 'SUPERSEDIDOS'],
  // [nombre en GitHub, nombre comercial (acta §3), bytes, SHA de blob Git]
  archivos: Object.freeze([
    ['Algoritmica_3er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO_v3.docx', 'Algoritmica_3er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026.docx', 4817731, 'b9a6b9d5a4477472100da0953740df96e0dda18b'],
    ['Algoritmica_3er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO_v3.pdf', 'Algoritmica_3er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026.pdf', 4820457, '47922a679d9190b665b65650e4042102b4b65e0c'],
    ['Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO_v3.docx', 'Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026.docx', 338509, 'dfd2d9e7e640cd89f6984e90acf737b65b9cb952'],
    ['Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO_v3.pdf', 'Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026.pdf', 573498, 'fa9e978ab9a244e034c23a0a0605dfaf53a41819'],
    ['Algoritmica_3er_Curso_PLAN_ANUAL_COMERCIAL_2026_FINAL_OFICIO_v3.docx', 'Algoritmica_3er_Curso_PLAN_ANUAL_COMERCIAL_2026.docx', 263844, 'c342884b686a30777638636775282d2f428258ad'],
    ['Algoritmica_3er_Curso_PLAN_ANUAL_COMERCIAL_2026_FINAL_OFICIO_v3.pdf', 'Algoritmica_3er_Curso_PLAN_ANUAL_COMERCIAL_2026.pdf', 453019, '9036f83f60bb309e86fa1eb83d1486257afe0e83'],
    ['Algoritmica_3er_Curso_PLANES_DE_CLASE_COMERCIAL_2026_FINAL_OFICIO_v3.docx', 'Algoritmica_3er_Curso_PLANES_DE_CLASE_COMERCIAL_2026.docx', 424465, '672331134fa6659362b6007809040d5a4c64efb8'],
    ['Algoritmica_3er_Curso_PLANES_DE_CLASE_COMERCIAL_2026_FINAL_OFICIO_v3.pdf', 'Algoritmica_3er_Curso_PLANES_DE_CLASE_COMERCIAL_2026.pdf', 1357484, '09fed96aad242b728cef295e652df98cd26dc190'],
    ['Algoritmica_3er_Curso_MUESTRA_COMERCIAL_2026_FINAL_OFICIO_v3.pdf', 'Algoritmica_3er_Curso_MUESTRA_COMERCIAL_2026.pdf', 1780929, '3316414914b034805e7c3229473a3e8c1191eda8']
  ]),
  // Los 10 archivos de agosto de 2026 que hoy están en la carpeta: [id Drive, nombre, bytes]
  anteriores: Object.freeze([
    ['1dulBKdlxMmQSn0wBeh7BLC2Y-BUUBGYb', 'Algoritmica_3er_Curso_TOMO_COMPLETO.docx', 3617395],
    ['1L-cawfAcL9NW54BdfwplbbSyJG1yXVWY', 'Algoritmica_3er_Curso_TOMO_COMPLETO.pdf', 3527813],
    ['1Hmrv7Ab9mja0RcvZR58_QoTlD5GkNLJ9', 'Algoritmica_3er_Curso_CUADERNO_PRACTICAS.docx', 301502],
    ['11iXxo6QrLRX9t_500fB0sf7JVnt_p4WS', 'Algoritmica_3er_Curso_CUADERNO_PRACTICAS.pdf', 342456],
    ['1-v-GkSOo2X0q2o5WEfqm8RdilUTxUAU6', 'Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE.docx', 90219],
    ['1d6aIe0-scDUbkpQjBJzkPo3YfuI7dlEA', 'Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE.pdf', 300087],
    ['1gganEyLUD7781Irj7a2WkB8IdKJEAvOY', 'Algoritmica_3er_Curso_PLAN_ANUAL.docx', 44217],
    ['1LvHIDGFUpv2rc_wVHXZEGvL3syDkcvcd', 'Algoritmica_3er_Curso_PLAN_ANUAL.pdf', 142410],
    ['1j1AAGODMLvPUVZIara0eHECAYrRJMiRr', 'Algoritmica_3er_Curso_PLANES_DE_CLASE.docx', 159388],
    ['1a6IPbQG2Hr4QqJ_oYLg4F58tfOJoWCrZ', 'Algoritmica_3er_Curso_PLANES_DE_CLASE.pdf', 1015926]
  ])
});

const ALG3_MIME_DOCX = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document';
const ALG3_ETIQUETA = 'Cierre comercial BTI Algoritmica 3 Esencial 2026 (acta 12/10/2026)';

/** PASOS 1 y 2: copiar los nueve originales y verificarlos 9/9 (nombre, tamaño, tipo y hash). No mueve nada. */
function paso1y2_copiarYVerificarAlgoritmica3() {
  const cfg = ALG3_COMERCIAL;
  const cerrojo = LockService.getScriptLock();
  if (!cerrojo.tryLock(30000)) throw new Error('Otra ejecución está en curso. Reintentá más tarde.');
  const creados = [];
  let actual = '(verificación inicial)';
  try {
    const curso = carpetaCursoAlg3_();
    // Preflight GitHub: los nueve archivos del commit fijo, con su SHA de blob y tamaño del acta.
    const api = 'https://api.github.com/repos/' + cfg.propietario + '/' + cfg.repositorio;
    const listado = solicitarGithubAlg3_(api + '/contents/' + cfg.rutaOrigen + '?ref=' + cfg.commit);
    if (!Array.isArray(listado)) throw new Error('Listado de GitHub inválido.');
    const enGithub = {};
    listado.forEach(function (a) { if (a.type === 'file') enGithub[a.name] = a; });
    if (Object.keys(enGithub).length !== 9) throw new Error('El commit fijo no tiene exactamente 9 archivos en la carpeta de salida.');
    cfg.archivos.forEach(function (d) {
      actual = d[0];
      const gh = enGithub[d[0]];
      if (!gh || gh.size !== d[2] || gh.sha !== d[3]) {
        throw new Error('El origen no coincide con el acta: ' + d[0] + (gh ? ' (' + gh.size + ' bytes, ' + gh.sha + ')' : ' NO EXISTE'));
      }
    });
    // Preflight Drive: no sobrescribir ni duplicar. Solo se reutiliza un archivo creado por ESTE script y ya verificado.
    cfg.archivos.forEach(function (d) {
      actual = d[1];
      const it = curso.getFilesByName(d[1]);
      if (!it.hasNext()) return;
      const f = it.next();
      if (it.hasNext()) throw new Error('Hay más de un archivo con el nombre ' + d[1] + '. No se continúa.');
      const v = verificarArchivoAlg3_(f, d);
      if (!v.ok) throw new Error('Ya existe ' + d[1] + ' y NO coincide con el acta (' + v.motivo + '). No se sobrescribe.');
    });
    // Copia binaria desde el commit fijo, sin conversión.
    cfg.archivos.forEach(function (d) {
      actual = d[1];
      if (curso.getFilesByName(d[1]).hasNext()) { Logger.log('YA PRESENTE Y VERIFICADO: ' + d[1]); return; }
      const url = 'https://raw.githubusercontent.com/' + cfg.propietario + '/' + cfg.repositorio + '/' + cfg.commit + '/' +
        cfg.rutaOrigen + '/' + encodeURIComponent(d[0]);
      const r = UrlFetchApp.fetch(url, { muteHttpExceptions: true, followRedirects: true,
        headers: { 'User-Agent': 'BTI-Cierre-Comercial-Algoritmica3' } });
      if (r.getResponseCode() !== 200) throw new Error('Descarga falló (HTTP ' + r.getResponseCode() + '): ' + d[0]);
      const bytes = r.getContent();
      if (bytes.length !== d[2]) throw new Error('Bytes descargados distintos del acta: ' + d[0]);
      if (shaBlobGitAlg3_(bytes) !== d[3]) throw new Error('SHA de blob de la descarga distinto del acta: ' + d[0]);
      const mime = /\.pdf$/i.test(d[1]) ? MimeType.PDF : ALG3_MIME_DOCX;
      const archivo = curso.createFile(r.getBlob().setName(d[1]).setContentType(mime));
      creados.push(d[1]);
      archivo.setDescription(ALG3_ETIQUETA + '; origen GitHub ' + cfg.commit + ':' + cfg.rutaOrigen + '/' + d[0] +
        '; GitHub blob SHA: ' + d[3] + '; tamaño: ' + d[2] + ' bytes');
      Logger.log('COPIADO: ' + d[1] + ' | ' + d[2] + ' bytes | ' + archivo.getUrl());
    });
    // PASO 2: verificación 9/9 sobre lo que quedó en Drive (se relee cada archivo).
    const r = verificarNueveAlg3_();
    if (r.correctos !== 9) throw new Error('Verificación ' + r.correctos + '/9. NO pasar al paso 3. Incidencias: ' + r.incidencias.join(' | '));
    Logger.log('PASOS 1 Y 2 COMPLETADOS: 9/9 verificados (nombre, tamaño, tipo, SHA-1 de blob recalculado). Ya podés ejecutar paso3y4_supersedidosEInventarioAlgoritmica3.');
    return r;
  } catch (e) {
    Logger.log('PASO 1-2 INCOMPLETO en: ' + actual + '. Creados en esta ejecución: ' + JSON.stringify(creados));
    Logger.log('CAUSA: ' + e.message);
    throw e;
  } finally {
    cerrojo.releaseLock();
  }
}

/** PASOS 3 y 4: solo con 9/9 confirmado en este momento. Mueve (no borra) los 10 anteriores y comprueba la carpeta. */
function paso3y4_supersedidosEInventarioAlgoritmica3() {
  const cfg = ALG3_COMERCIAL;
  const cerrojo = LockService.getScriptLock();
  if (!cerrojo.tryLock(30000)) throw new Error('Otra ejecución está en curso. Reintentá más tarde.');
  try {
    const curso = carpetaCursoAlg3_();
    // Compuerta: se vuelve a verificar 9/9 antes de mover cualquier cosa.
    const v = verificarNueveAlg3_();
    if (v.correctos !== 9) throw new Error('Compuerta: verificación ' + v.correctos + '/9. No se mueve nada.');
    const sup = obtenerOCrearSubcarpetaAlg3_(curso, cfg.supersedidos);
    // Precomprobar los 10 antes de mover el primero: identidad, nombre, tamaño y ubicación.
    const aMover = [];
    cfg.anteriores.forEach(function (d) {
      const f = DriveApp.getFileById(d[0]);
      if (f.getName() !== d[1] || f.getSize() !== d[2]) throw new Error('El anterior no coincide (nombre/tamaño): ' + d[1]);
      if (f.isTrashed()) throw new Error('El anterior está en la papelera: ' + d[1]);
      const padres = []; const it = f.getParents();
      while (it.hasNext()) padres.push(it.next().getId());
      if (padres.indexOf(sup.getId()) !== -1) { Logger.log('YA EN SUPERSEDIDOS: ' + d[1]); return; }
      if (padres.length !== 1 || padres[0] !== curso.getId()) throw new Error('El anterior no está solo en la carpeta del curso: ' + d[1]);
      aMover.push(f);
    });
    aMover.forEach(function (f) {
      f.moveTo(sup);
      Logger.log('MOVIDO A SUPERSEDIDOS (sin borrar): ' + f.getName() + ' | ' + f.getUrl());
    });
    // PASO 4: la carpeta comercial debe tener EXACTAMENTE los 9 aprobados + subcarpetas administrativas.
    const inv = inventarioAlg3_(curso);
    if (!inv.ok) throw new Error('Inventario NO conforme: ' + inv.incidencias.join(' | '));
    Logger.log('PASOS 3 Y 4 COMPLETADOS: 10 anteriores en SUPERSEDIDOS (' + sup.getUrl() + '); carpeta comercial = 9 aprobados + ' +
      JSON.stringify(inv.subcarpetas));
    return informeAlgoritmica3();
  } finally {
    cerrojo.releaseLock();
  }
}

/** Solo lectura y repetible: enlaces, tamaños, SHA-1 de blob y SHA-256 de los nueve, inventario y estado de SUPERSEDIDOS. */
function informeAlgoritmica3() {
  const cfg = ALG3_COMERCIAL;
  const curso = carpetaCursoAlg3_();
  const v = verificarNueveAlg3_();
  const inv = inventarioAlg3_(curso);
  const supIt = curso.getFoldersByName(cfg.supersedidos);
  let enSup = 0;
  if (supIt.hasNext()) {
    const sup = supIt.next();
    cfg.anteriores.forEach(function (d) {
      const it = DriveApp.getFileById(d[0]).getParents();
      while (it.hasNext()) if (it.next().getId() === sup.getId()) enSup++;
    });
  }
  const informe = { verificados: v.correctos + '/9', detalle: v.detalle, incidencias: v.incidencias,
    inventarioConforme: inv.ok, subcarpetas: inv.subcarpetas, inventarioIncidencias: inv.incidencias,
    anterioresEnSupersedidos: enSup + '/10' };
  Logger.log('INFORME ALGORITMICA 3 COMERCIAL:\n' + JSON.stringify(informe, null, 2));
  return informe;
}

// ---------- auxiliares ----------

function carpetaCursoAlg3_() {
  const c = DriveApp.getFolderById(ALG3_COMERCIAL.carpetaCursoId);
  if (c.getName() !== ALG3_COMERCIAL.carpetaCursoNombre) throw new Error('La carpeta destino no es la esperada: ' + c.getName());
  return c;
}

function verificarNueveAlg3_() {
  const curso = carpetaCursoAlg3_();
  const detalle = [], incidencias = [];
  ALG3_COMERCIAL.archivos.forEach(function (d) {
    const it = curso.getFilesByName(d[1]);
    if (!it.hasNext()) { incidencias.push('FALTA ' + d[1]); return; }
    const f = it.next();
    if (it.hasNext()) { incidencias.push('DUPLICADO ' + d[1]); return; }
    const r = verificarArchivoAlg3_(f, d);
    if (!r.ok) { incidencias.push(d[1] + ': ' + r.motivo); return; }
    const privado = f.getSharingAccess() === DriveApp.Access.PRIVATE;
    if (/SOLUCIONARIO/.test(d[1]) && !privado) { incidencias.push(d[1] + ': el solucionario NO es privado (' + f.getSharingAccess() + ')'); return; }
    detalle.push({ nombre: d[1], bytes: f.getSize(), mime: f.getMimeType(), shaBlobGit: r.shaBlob, sha256: r.sha256,
      acceso: String(f.getSharingAccess()), id: f.getId(), url: f.getUrl() });
    Logger.log('OK ' + d[1] + ' | ' + f.getSize() + ' bytes | blob ' + r.shaBlob + ' | sha256 ' + r.sha256 + ' | ' + f.getUrl());
  });
  Logger.log('VERIFICACION: ' + detalle.length + '/9 correctos; incidencias=' + incidencias.length);
  return { correctos: detalle.length, detalle: detalle, incidencias: incidencias };
}

function verificarArchivoAlg3_(f, d) {
  const mime = /\.pdf$/i.test(d[1]) ? MimeType.PDF : ALG3_MIME_DOCX;
  if (f.getName() !== d[1]) return { ok: false, motivo: 'nombre' };
  if (f.getMimeType() !== mime) return { ok: false, motivo: 'tipo ' + f.getMimeType() };
  if (f.getSize() !== d[2]) return { ok: false, motivo: 'tamaño ' + f.getSize() + ' ≠ ' + d[2] };
  const bytes = f.getBlob().getBytes();
  if (bytes.length !== d[2]) return { ok: false, motivo: 'bytes leídos ' + bytes.length };
  const shaBlob = shaBlobGitAlg3_(bytes);
  if (shaBlob !== d[3]) return { ok: false, motivo: 'SHA de blob ' + shaBlob + ' ≠ ' + d[3] };
  return { ok: true, shaBlob: shaBlob, sha256: hexAlg3_(Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, bytes)) };
}

function inventarioAlg3_(curso) {
  const permitidos = ALG3_COMERCIAL.archivos.map(function (d) { return d[1]; });
  const vistos = {}, incidencias = [], subcarpetas = [];
  const fi = curso.getFiles();
  while (fi.hasNext()) {
    const n = fi.next().getName();
    if (permitidos.indexOf(n) === -1) incidencias.push('archivo no aprobado en la carpeta: ' + n);
    vistos[n] = (vistos[n] || 0) + 1;
  }
  permitidos.forEach(function (n) { if (vistos[n] !== 1) incidencias.push(n + ' aparece ' + (vistos[n] || 0) + ' veces'); });
  const ci = curso.getFolders();
  while (ci.hasNext()) {
    const n = ci.next().getName();
    subcarpetas.push(n);
    if (ALG3_COMERCIAL.subcarpetasAdmitidas.indexOf(n) === -1) incidencias.push('subcarpeta no prevista: ' + n);
  }
  return { ok: incidencias.length === 0, incidencias: incidencias, subcarpetas: subcarpetas };
}

function obtenerOCrearSubcarpetaAlg3_(padre, nombre) {
  const it = padre.getFoldersByName(nombre);
  if (it.hasNext()) {
    const c = it.next();
    if (it.hasNext()) throw new Error('Carpetas duplicadas: ' + nombre);
    return c;
  }
  return padre.createFolder(nombre);
}

/** SHA-1 de blob de Git: sha1("blob " + tamaño + "\0" + bytes). */
function shaBlobGitAlg3_(bytes) {
  const cabecera = Utilities.newBlob('blob ' + bytes.length + '\u0000').getBytes();
  return hexAlg3_(Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_1, cabecera.concat(bytes)));
}

function hexAlg3_(digest) {
  return digest.map(function (n) { return ('0' + (n < 0 ? n + 256 : n).toString(16)).slice(-2); }).join('');
}

function solicitarGithubAlg3_(url) {
  const headers = { 'Accept': 'application/vnd.github+json', 'User-Agent': 'BTI-Cierre-Comercial-Algoritmica3',
    'X-GitHub-Api-Version': '2022-11-28' };
  const token = PropertiesService.getScriptProperties().getProperty('GITHUB_TOKEN_BTI');
  if (token && token.trim()) headers['Authorization'] = 'Bearer ' + token.trim();
  const r = UrlFetchApp.fetch(url, { muteHttpExceptions: true, headers: headers });
  if (r.getResponseCode() !== 200) throw new Error('GitHub HTTP ' + r.getResponseCode() + ': ' + r.getContentText().slice(0, 600) + ' | URL=' + url);
  return JSON.parse(r.getContentText());
}

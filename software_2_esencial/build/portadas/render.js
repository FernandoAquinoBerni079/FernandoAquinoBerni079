const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 816, height: 1247 }, deviceScaleFactor: 2.5 });
  for (const n of process.argv.slice(2)) {
    await p.goto('file://' + __dirname + '/' + n + '.html');
    await p.waitForTimeout(400);
    await p.screenshot({ path: __dirname + '/' + n + '.png', fullPage: false });
  }
  await b.close();
})();

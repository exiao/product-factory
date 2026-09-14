const assert = require('node:assert/strict');
const fs = require('node:fs');
const http = require('node:http');
const { chromium } = require('playwright');
const path = require('node:path');
const screenshotPath = path.join(require('node:os').tmpdir(), 'artifact-review-actions.png');

const helper = fs.readFileSync(path.join(__dirname, '..', 'assets', 'review-actions.js'), 'utf8');
const styles = fs.readFileSync(path.join(__dirname, '..', 'assets', 'review-actions.css'), 'utf8');
const fixture = `<!doctype html>
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="/review-actions.css">
<style>body{font:16px system-ui;margin:40px}#host{max-width:640px}</style>
<main id="host"></main>
<script type="module">
import {mountReviewActions} from '/review-actions.js';
const host = document.querySelector('#host');
let teardown;
window.events = [];
window.failNext = false;
window.render = config => {
  teardown?.();
  host.replaceChildren();
  window.events.length = 0;
  teardown = mountReviewActions(host, {
    ...config,
    onAction: async payload => {
      window.events.push(payload);
      if (window.failNext) {
        window.failNext = false;
        throw new Error('expected save failure');
      }
    }
  });
};
</script>`;

function startServer() {
  return new Promise(resolve => {
    const server = http.createServer((request, response) => {
      if (request.url === '/review-actions.js') {
        response.writeHead(200, {'content-type': 'text/javascript'});
        response.end(helper);
        return;
      }
      if (request.url === '/review-actions.css') {
        response.writeHead(200, {'content-type': 'text/css'});
        response.end(styles);
        return;
      }
      response.writeHead(200, {'content-type': 'text/html'});
      response.end(fixture);
    });
    server.listen(0, '127.0.0.1', () => resolve(server));
  });
}

async function main() {
  const server = await startServer();
  const address = server.address();
  let browser;
  try {
    browser = await chromium.launch();
    const page = await browser.newPage({viewport: {width: 900, height: 700}});
    await page.goto(`http://127.0.0.1:${address.port}/`);
    await page.waitForFunction(() => typeof window.render === 'function');

    await page.evaluate(() => window.render({}));
    assert.equal(await page.locator('.ar-actions').count(), 0, 'default mount has no action bar');
    assert.equal(await page.locator('button').count(), 0, 'default mount has no buttons');

    await page.evaluate(() => window.render({actions: ['option', 'research', 'comment', 'ignored']}));
    assert.deepEqual(await page.locator('.ar-actions button').allTextContents(), [
      'Request new option', 'Request research', 'Add comment'
    ], 'only supplied known actions render');

    await page.evaluate(() => window.render({actions: ['option', 'research'], connected: true}));
    assert.deepEqual(await page.locator('.ar-actions button').allTextContents(), [
      'New option', 'Research further'
    ], 'connected labels describe executable requests');

    await page.evaluate(() => window.render({actions: ['comment']}));
    const comment = page.getByRole('button', {name: 'Add comment'});
    await comment.click();
    await page.getByRole('textbox', {name: 'Comment'}).fill('  hello  ');
    await page.getByRole('button', {name: 'Save comment'}).click();
    await page.waitForFunction(() => window.events.length === 1);
    assert.deepEqual(await page.evaluate(() => window.events[0]), {kind: 'comment', text: 'hello'}, 'comment payload is trimmed and typed');
    assert.equal(await page.locator('.ar-popover').count(), 0, 'successful save closes popover');

    await page.evaluate(() => window.render({actions: ['comment']}));
    await page.getByRole('button', {name: 'Add comment'}).click();
    const text = page.getByRole('textbox', {name: 'Comment'});
    await text.fill('Keep me');
    await page.evaluate(() => { window.failNext = true; });
    await page.getByRole('button', {name: 'Save comment'}).click();
    await page.getByRole('status').waitFor({state: 'visible'});
    assert.equal(await page.getByRole('status').textContent(), 'Could not save. Your text is still here.', 'failed save explains retention');
    assert.equal(await text.inputValue(), 'Keep me', 'failed save retains visible text');
    await page.screenshot({path: screenshotPath, fullPage: true});

    await comment.click();
    assert.equal(await page.getByRole('textbox', {name: 'Comment'}).inputValue(), 'Keep me', 'draft reopens after failed save');
    await page.getByRole('textbox', {name: 'Comment'}).press('Escape');
    assert.equal(await page.locator('.ar-popover').count(), 0, 'Escape closes popover');
    assert.equal(await page.evaluate(() => document.activeElement.textContent), 'Add comment', 'Escape returns focus to trigger');

    await page.evaluate(() => window.render({actions: ['dismiss']}));
    await page.getByRole('button', {name: 'Dismiss'}).click();
    await page.waitForFunction(() => window.events.length === 1);
    assert.deepEqual(await page.evaluate(() => window.events[0]), {kind: 'dismiss'}, 'supplied dismiss callback receives only dismiss kind');
    await page.evaluate(() => window.render({}));
    assert.equal(await page.locator('button').count(), 0, 'without dismiss action no dismiss callback can fire');

    console.log('PASS artifact-review review-actions browser check');
    console.log('screenshot:', screenshotPath);
  } finally {
    await browser?.close();
    await new Promise(resolve => server.close(resolve));
  }
}

main().catch(error => {
  console.error(error.stack || error);
  process.exitCode = 1;
});

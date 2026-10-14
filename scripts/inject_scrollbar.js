const WebSocket = require('ws');
const http = require('http');
const fs = require('fs');
const path = require('path');

function getDevToolsPort() {
  const portFilePath = path.join(
    process.env.APPDATA || 'C:\\Users\\Admin\\AppData\\Roaming',
    'Antigravity',
    'DevToolsActivePort'
  );
  if (!fs.existsSync(portFilePath)) {
    throw new Error('DevToolsActivePort file not found at ' + portFilePath);
  }
  const content = fs.readFileSync(portFilePath, 'utf8').trim().split('\n');
  return parseInt(content[0].trim(), 10);
}

const port = getDevToolsPort();
console.log(`Connecting to Antigravity DevTools on port ${port}...`);

http.get(`http://localhost:${port}/json`, (res) => {
  let data = '';
  res.on('data', (c) => (data += c));
  res.on('end', () => {
    try {
      const targets = JSON.parse(data);
      console.log(`Found ${targets.length} targets:`);
      targets.forEach((t) => console.log(` - [${t.type}] ${t.title || t.url} (${t.webSocketDebuggerUrl})`));

      // Inject into all page and webview targets with a debugger url
      const injectableTargets = targets.filter((t) => t.webSocketDebuggerUrl);
      if (injectableTargets.length === 0) {
        console.error('No injectable targets found');
        process.exit(1);
      }

      let completed = 0;
      injectableTargets.forEach((target) => {
        injectScrollbar(target, () => {
          completed++;
          if (completed === injectableTargets.length) {
            console.log('All targets injected successfully!');
            process.exit(0);
          }
        });
      });
    } catch (e) {
      console.error('Error parsing targets:', e);
      process.exit(1);
    }
  });
}).on('error', (err) => {
  console.error('Failed to connect to DevTools port:', err.message);
  process.exit(1);
});

function injectScrollbar(target, callback) {
  const ws = new WebSocket(target.webSocketDebuggerUrl);

  ws.on('open', () => {
    const cssText = [
      '::-webkit-scrollbar { width: 14px !important; height: 14px !important; display: block !important; }',
      '::-webkit-scrollbar-track { background: rgba(255, 255, 255, 0.08) !important; border-radius: 8px !important; }',
      '::-webkit-scrollbar-thumb { background: #3b82f6 !important; border-radius: 8px !important; border: 2px solid rgba(0,0,0,0.4) !important; }',
      '::-webkit-scrollbar-thumb:hover { background: #60a5fa !important; }',
      '* { scrollbar-width: auto !important; scrollbar-color: #3b82f6 rgba(255, 255, 255, 0.08) !important; }',
      'div, main, section { scrollbar-gutter: stable !important; }'
    ].join(' ');

    const script = `
      (function() {
        let el = document.getElementById('ag-force-scrollbar');
        if (!el) {
          el = document.createElement('style');
          el.id = 'ag-force-scrollbar';
          document.head.appendChild(el);
        }
        el.textContent = ${JSON.stringify(cssText)};
        return 'SUCCESS_INJECTED';
      })()
    `;

    ws.send(
      JSON.stringify({
        id: 1,
        method: 'Runtime.evaluate',
        params: { expression: script, returnByValue: true },
      })
    );
  });

  ws.on('message', (msg) => {
    console.log(`Target [${target.type}] ${target.title || target.url} -> Result:`, msg.toString());
    ws.close();
    callback();
  });

  ws.on('error', (err) => {
    console.error(`WebSocket error on target ${target.title}:`, err.message);
    callback();
  });
}

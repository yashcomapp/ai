const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const resourcesDir = path.join(
  process.env.LOCALAPPDATA || 'C:\\Users\\Admin\\AppData\\Local',
  'Programs',
  'antigravity',
  'resources'
);
const asarPath = path.join(resourcesDir, 'app.asar');
const backupPath = path.join(resourcesDir, 'app.asar.bak');
const extractDir = path.join(resourcesDir, 'app_extracted');
const modifiedAsarPath = path.join(resourcesDir, 'app_modified.asar');

if (!fs.existsSync(asarPath)) {
  console.error(`app.asar not found at: ${asarPath}`);
  process.exit(1);
}

console.log('1. Backing up app.asar...');
fs.copyFileSync(asarPath, backupPath);

console.log('2. Extracting app.asar...');
if (fs.existsSync(extractDir)) {
  fs.rmSync(extractDir, { recursive: true, force: true });
}
execSync(`npx @electron/asar extract "${asarPath}" "${extractDir}"`, { stdio: 'inherit' });

console.log('3. Patching preload.js...');
const preloadPath = path.join(extractDir, 'dist', 'preload.js');
let preloadContent = fs.readFileSync(preloadPath, 'utf8');

const scrollbarCode = `
// Persistent default visible scrollbar across all conversations, windows, and panels
(() => {
  const css = \`
    ::-webkit-scrollbar {
      width: 14px !important;
      height: 14px !important;
      display: block !important;
    }
    ::-webkit-scrollbar-track {
      background: rgba(255, 255, 255, 0.08) !important;
      border-radius: 8px !important;
    }
    ::-webkit-scrollbar-thumb {
      background: #3b82f6 !important;
      border-radius: 8px !important;
      border: 2px solid rgba(0, 0, 0, 0.4) !important;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #60a5fa !important;
    }
    * {
      scrollbar-width: auto !important;
      scrollbar-color: #3b82f6 rgba(255, 255, 255, 0.08) !important;
    }
    div, main, section, [class*="scroll"], [class*="container"] {
      scrollbar-gutter: stable !important;
    }
  \`;

  const injectStyle = () => {
    try {
      const target = document.head || document.documentElement;
      if (!target) return;
      let el = document.getElementById('ag-force-scrollbar');
      if (!el) {
        el = document.createElement('style');
        el.id = 'ag-force-scrollbar';
        target.appendChild(el);
      }
      if (el.textContent !== css) {
        el.textContent = css;
      }
    } catch (e) {}
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectStyle);
  } else {
    injectStyle();
  }
  window.addEventListener('load', injectStyle);

  try {
    const observer = new MutationObserver(() => {
      if (!document.getElementById('ag-force-scrollbar')) {
        injectStyle();
      }
    });
    const attach = () => {
      if (document.documentElement) {
        observer.observe(document.documentElement, { childList: true, subtree: true });
      }
    };
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', attach);
    } else {
      attach();
    }
  } catch (e) {}
})();
`;

if (!preloadContent.includes('ag-force-scrollbar')) {
  preloadContent += '\n' + scrollbarCode;
  fs.writeFileSync(preloadPath, preloadContent, 'utf8');
  console.log('   -> Added scrollbar injector to preload.js');
} else {
  console.log('   -> preload.js already contains scrollbar injector');
}

console.log('4. Patching utils.js...');
const utilsPath = path.join(extractDir, 'dist', 'utils.js');
let utilsContent = fs.readFileSync(utilsPath, 'utf8');

const insertCSSText = `
            win.webContents.insertCSS(\`
                ::-webkit-scrollbar { width: 14px !important; height: 14px !important; display: block !important; }
                ::-webkit-scrollbar-track { background: rgba(255, 255, 255, 0.08) !important; border-radius: 8px !important; }
                ::-webkit-scrollbar-thumb { background: #3b82f6 !important; border-radius: 8px !important; border: 2px solid rgba(0, 0, 0, 0.4) !important; }
                ::-webkit-scrollbar-thumb:hover { background: #60a5fa !important; }
                * { scrollbar-width: auto !important; scrollbar-color: #3b82f6 rgba(255, 255, 255, 0.08) !important; }
                div, main, section, [class*="scroll"], [class*="container"] { scrollbar-gutter: stable !important; }
            \`).catch(() => {});
`;

if (!utilsContent.includes('::-webkit-scrollbar { width: 14px !important')) {
  utilsContent = utilsContent.replace(
    /win\.webContents\.on\('did-finish-load',\s*\(\)\s*=>\s*\{/g,
    `win.webContents.on('did-finish-load', () => {${insertCSSText}`
  );
  fs.writeFileSync(utilsPath, utilsContent, 'utf8');
  console.log('   -> Added insertCSS to utils.js');
} else {
  console.log('   -> utils.js already contains insertCSS');
}

console.log('5. Repacking asar with unpacked native modules...');
if (fs.existsSync(modifiedAsarPath)) {
  fs.rmSync(modifiedAsarPath, { force: true });
}
execSync(
  `npx @electron/asar pack "${extractDir}" "${modifiedAsarPath}" --unpack-dir "node_modules/chrome-devtools-mcp"`,
  { stdio: 'inherit' }
);

console.log('6. Replacing app.asar...');
fs.copyFileSync(modifiedAsarPath, asarPath);

console.log('7. Cleaning up temporary build files...');
fs.rmSync(modifiedAsarPath, { force: true });
fs.rmSync(extractDir, { recursive: true, force: true });

console.log('SUCCESS! Antigravity desktop app now has default visible scrollbars permanently in all conversations and windows.');

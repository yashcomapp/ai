const ts = require('typescript');
const fs = require('fs');
const path = require('path');

// 1. Auto-load .env.local
const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const content = fs.readFileSync(envPath, 'utf8');
  content.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        const key = trimmed.slice(0, idx).trim();
        const val = trimmed.slice(idx + 1).trim().replace(/^["']|["']$/g, '');
        if (!process.env[key]) {
          process.env[key] = val;
        }
      }
    }
  });
}

const srcDir = path.resolve(__dirname, '../src');

function registerTsHook() {
  require.extensions['.ts'] = function(module, filename) {
    let content = fs.readFileSync(filename, 'utf8');
    const fileDir = path.dirname(filename);
    
    // Replace '@/...' with relative paths
    content = content.replace(/(from\s+['"])@\/([^'"]+)(['"])/g, (match, p1, p2, p3) => {
      let rel = path.relative(fileDir, path.join(srcDir, p2)).replace(/\\/g, '/');
      if (!rel.startsWith('.')) rel = './' + rel;
      return `${p1}${rel}${p3}`;
    });

    content = content.replace(/(require\(['"])@\/([^'"]+)(['"]\))/g, (match, p1, p2, p3) => {
      let rel = path.relative(fileDir, path.join(srcDir, p2)).replace(/\\/g, '/');
      if (!rel.startsWith('.')) rel = './' + rel;
      return `${p1}${rel}${p3}`;
    });

    const transpiled = ts.transpileModule(content, {
      compilerOptions: {
        module: ts.ModuleKind.CommonJS,
        target: ts.ScriptTarget.ES2020,
        esModuleInterop: true
      }
    }).outputText;

    module._compile(transpiled, filename);
  };
}

module.exports = { registerTsHook };

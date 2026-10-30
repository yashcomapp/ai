const fs = require('fs');

const files = fs.readdirSync('backups/staging').filter(f => f.startsWith('mh9_scit_') && (f.endsWith('enhanced.json') || f.endsWith('compact.json') || f.endsWith('curated.json')));

files.forEach(f => {
  try {
    const data = JSON.parse(fs.readFileSync('backups/staging/' + f, 'utf8'));
    if (Array.isArray(data)) {
      console.log(f.padEnd(35), 'Count:', String(data.length).padStart(4), 'Sample code:', data[0]?.questionCode || data[0]?.id);
    }
  } catch (e) {
    console.error(f, e.message);
  }
});

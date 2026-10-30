const fs = require('fs');
let lines = fs.readFileSync('scripts/ch2_foundation_data.py', 'utf8').split('\n');
for (let i = 0; i < lines.length; i++) {
  if (lines[i].includes('"options": [')) {
    let prev = lines[i-1].trim();
    if (prev.endsWith('",') && !prev.endsWith('""",')) {
      const idx = lines[i-1].lastIndexOf('",');
      if (idx !== -1) {
        lines[i-1] = lines[i-1].substring(0, idx) + '""",';
        console.log('Fixed line', i);
      }
    }
  }
}
fs.writeFileSync('scripts/ch2_foundation_data.py', lines.join('\n'), 'utf8');
console.log('Done fixing quotes!');

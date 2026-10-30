const fs = require('fs');

function fixPythonTuples(filePath) {
  let lines = fs.readFileSync(filePath, 'utf8').split('\n');
  let fixed = 0;
  for (let i = 0; i < lines.length; i++) {
    // If next line has list of options like `     ["` or `      ["`
    if (lines[i].trim().startsWith('["') && i > 0) {
      let prev = lines[i - 1].trim();
      if (prev.endsWith('",') && !prev.endsWith('""",')) {
        const idx = lines[i - 1].lastIndexOf('",');
        if (idx !== -1) {
          lines[i - 1] = lines[i - 1].substring(0, idx) + '""",';
          fixed++;
        }
      }
    }
  }
  fs.writeFileSync(filePath, lines.join('\n'), 'utf8');
  console.log(`Fixed ${fixed} lines in ${filePath}`);
}

const target = process.argv[2] || 'scripts/generate_topic2_3.py';
fixPythonTuples(target);

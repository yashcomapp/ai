const fs = require('fs');
const file = process.argv[2];
const lines = fs.readFileSync(file, 'utf8').split('\n');
let inTriple = false;
let startLine = 0;
for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  const count = (line.match(/"""/g) || []).length;
  if (count > 0) {
    console.log(`Line ${i + 1} (count=${count}, wasInTriple=${inTriple}): ${line.substring(0, 60)}`);
    if (count === 1) {
      if (!inTriple) {
        inTriple = true;
        startLine = i + 1;
      } else {
        inTriple = false;
      }
    }
  }
}
if (inTriple) {
  console.log('Unclosed triple quote started at line', startLine);
} else {
  console.log('All triple quotes balanced!');
}

const fs = require('fs');
const file = process.argv[2];
let c = fs.readFileSync(file, 'utf8');

// For any exam/practice single line questions starting with '    ("' and ending with '""",\n     [':
c = c.replace(/(\n\s+\([rR]?\"[^\n\"]+)\"\"\",(\r?\n\s+\[)/g, '$1",$2');

// For mock questions that contain <svg, ensure the question string ends with '""",':
c = c.replace(/(<svg[\s\S]*?\n[^\n]+)\",(\r?\n\s+\[)/g, '$1""",\n     [');

fs.writeFileSync(file, c, 'utf8');
console.log('Fixed quotes accurately in', file);

const fs = require('fs');
const file = process.argv[2];
let c = fs.readFileSync(file, 'utf8');

// Replace any occurrence of ?\",\r?\n\s+\[ with ?\"\"\",\n     [
c = c.replace(/\?\",(\r?\n\s+\[)/g, '?\"\"\",$1');

fs.writeFileSync(file, c, 'utf8');
console.log('Fixed triple quotes in', file);

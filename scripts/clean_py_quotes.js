const fs = require('fs');

const file = process.argv[2] || 'scripts/generate_topic5_5.py';
let code = fs.readFileSync(file, 'utf8');

// Replace corrupted trailing quotes
code = code.replace(/\"\"\"\"+/g, '"""');
code = code.replace(/\"\"\\\"\"\"/g, '"""');
code = code.replace(/\"\"\\\"\"/g, '"""');

fs.writeFileSync(file, code, 'utf8');
console.log(`Cleaned ${file}`);

const fs = require('fs');

const file = process.argv[2] || 'scripts/generate_ch6_topic1.py';
let code = fs.readFileSync(file, 'utf8');

// Replace bullets
code = code.replace(/•/g, '-');

// Fix multiline string opening with (""" and ending with ",
code = code.replace(/(\(\"\"\"[\s\S]*?)\",\s*(\[\s*[\"'])/g, '$1""",\n     $2');

fs.writeFileSync(file, code, 'utf8');
console.log(`Processed ${file}`);

const fs = require('fs');

const file = process.argv[2];
if (!file) {
  console.log('Usage: node scripts/fix_python_escapes.js <path>');
  process.exit(1);
}

let content = fs.readFileSync(file, 'utf8');

// Replace (""" with (r"""
content = content.replace(/\(\"\"\"/g, '(r"""');

// Also replace standard string quotes that might have \u without escaping, or \mu -> \\mu
// Specifically \text, \mu, etc. if inside regular strings
// Let's replace any single or double quoted strings that have \u with \\u if not \uXXXX
// Or replace `\mu` with `\\mu`
content = content.replace(/\\mu/g, '\\\\mu');

fs.writeFileSync(file, content);
console.log(`Updated raw strings and escapes in ${file}`);

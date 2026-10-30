const fs = require('fs');
let content = fs.readFileSync('scripts/generate_ch11_topic2.py', 'utf8');
content = content.replace('("Assertion (A): For a spherical mirror of small aperture, R = 2f is valid.\r\nReason (R):', '("Assertion (A): For a spherical mirror of small aperture, R = 2f is valid.\\nReason (R):');
content = content.replace('("Assertion (A): For a spherical mirror of small aperture, R = 2f is valid.\nReason (R):', '("Assertion (A): For a spherical mirror of small aperture, R = 2f is valid.\\nReason (R):');
fs.writeFileSync('scripts/generate_ch11_topic2.py', content, 'utf8');
console.log('Fixed newline');

const fs = require('fs');
let content = fs.readFileSync('scripts/generate_ch11_topic4.py', 'utf8');
content = content.replace('("Assertion (A): Convex mirrors are used as rear-view mirrors in cars.\r\nReason (R):', '("Assertion (A): Convex mirrors are used as rear-view mirrors in cars.\\nReason (R):');
content = content.replace('("Assertion (A): Convex mirrors are used as rear-view mirrors in cars.\nReason (R):', '("Assertion (A): Convex mirrors are used as rear-view mirrors in cars.\\nReason (R):');
fs.writeFileSync('scripts/generate_ch11_topic4.py', content, 'utf8');
console.log('Fixed newline in ch11_topic4');

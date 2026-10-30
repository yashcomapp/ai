const fs = require('fs');

const file = process.argv[2];
if (!file) {
  console.error('Please provide a file path');
  process.exit(1);
}

let content = fs.readFileSync(file, 'utf8');

const replacements = [
  [/°/g, '^{\\circ}'],
  [/θ/g, '\\theta'],
  [/δ/g, '\\delta'],
  [/λ/g, '\\lambda'],
  [/ν/g, '\\nu'],
  [/≈/g, '\\approx'],
  [/Δ/g, '\\Delta'],
  [/₁/g, '_1'],
  [/₂/g, '_2'],
  [/₃/g, '_3'],
  [/₄/g, '_4']
];

replacements.forEach(([regex, rep]) => {
  content = content.replace(regex, rep);
});

// Also replace × with *
content = content.replace(/×/g, '*');

// In mock_data, ensure all triple quotes close properly
const idx = content.indexOf('mock_data = [');
if (idx !== -1) {
  let before = content.slice(0, idx);
  let after = content.slice(idx);
  // Match any line ending with ?\",\r?\n\s+\[
  after = after.replace(/([^\"])\",\r?\n\s+\[/g, '$1\"\"\",\n     [');
  after = after.replace(/([^\"])\",\r?\n\s+\"/g, '$1\"\"\",\n     \"');
  content = before + after;
}

fs.writeFileSync(file, content, 'utf8');
console.log(`Successfully cleaned non-ascii chars in ${file}`);

const fs = require('fs');

const file = process.argv[2];
if (!file) {
  console.error('Please provide a file path');
  process.exit(1);
}

let content = fs.readFileSync(file, 'utf8');

const replacements = [
  [/°/g, ' degrees '],
  [/θ/g, 'theta'],
  [/δ/g, 'delta'],
  [/λ/g, 'lambda'],
  [/ν/g, 'nu'],
  [/≈/g, '~='],
  [/Δ/g, 'Delta'],
  [/₁/g, '_1'],
  [/₂/g, '_2'],
  [/₃/g, '_3'],
  [/₄/g, '_4'],
  [/×/g, '*'],
  [/μ/g, 'u'],
  [/\\mu\b/g, 'u']
];

replacements.forEach(([regex, rep]) => {
  content = content.replace(regex, rep);
});

fs.writeFileSync(file, content, 'utf8');
console.log(`Successfully cleaned non-ascii chars in ${file}`);

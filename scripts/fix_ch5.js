const fs = require('fs');
let content = fs.readFileSync('scripts/build_clean_mth1_ch5_all.py', 'utf8');

// Replace line 1042
content = content.replace(
  '("In a three-digit number, hundreds digit is x, tens digit is y, unit digit is z. What is the number in expanded form?", "\\\\(100x + 10y + z\\\\)", ["\\\\(xyz\\\\)", "\\\\(100z + 10y + x\\\\)", "\\\\(x + y + z\\\\)"])',
  '("In a three-digit number, hundreds digit is x, tens digit is y, unit digit is z. What is the number in expanded form?", "\\\\(100x + 10y + z\\\\)", ["\\\\(xyz\\\\)", "\\\\(100x + y + z\\\\)", "\\\\(10x + y + z\\\\)"])'
);

// Replace line 1043
content = content.replace(
  '("If a three-digit number \\\\(100x + 10y + z\\\\) is reversed, what is the new number?", "\\\\(100z + 10y + x\\\\)", ["\\\\(100x + 10y + z\\\\)", "\\\\(zyx\\\\)", "\\\\(z + y + x\\\\)"])',
  '("If a three-digit number \\\\(100x + 10y + z\\\\) is reversed, what is the new number?", "\\\\(100z + 10y + x\\\\)", ["\\\\(100z + y + x\\\\)", "\\\\(zyx\\\\)", "\\\\(z + y + x\\\\)"])'
);

// Replace line 1122
content = content.replace(
  '["\\\\(x - y = 12\\\\)", "\\\\(xy = 12\\\\)", "\\\\(x/y = 12\\\\)"]',
  '["\\\\(x - y = 12\\\\)", "\\\\(xy = 12\\\\)", "\\\\(2x + y = 12\\\\)"]'
);

fs.writeFileSync('scripts/build_clean_mth1_ch5_all.py', content, 'utf8');
console.log('Successfully replaced in build_clean_mth1_ch5_all.py!');

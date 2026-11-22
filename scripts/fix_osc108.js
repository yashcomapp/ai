const fs = require('fs');
let content = fs.readFileSync('scripts/build_clean_mth1_ch5_all.py', 'utf8');

content = content.replace(
  '["\\\\(s_1 - s_2\\\\)", "\\\\(s_1 s_2\\\\)", "\\\\(s_1 / s_2\\\\)"]',
  '["\\\\(s_1 - s_2\\\\)", "\\\\((s_1 + s_2)/2\\\\)", "\\\\(s_1 / s_2\\\\)"]'
);

fs.writeFileSync('scripts/build_clean_mth1_ch5_all.py', content, 'utf8');
console.log('Fixed OSC-108 in build_clean_mth1_ch5_all.py');

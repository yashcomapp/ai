const fs = require('fs');
let content = fs.readFileSync('scripts/build_clean_mth1_ch7_part2.py', 'utf8');

// Fix archs_722.append to archs_731.append around line 498
content = content.replace(
  '    # Arch 7: Properties and limitations of the Arithmetic Mean\n    archs_722.append({',
  '    # Arch 7: Properties and limitations of the Arithmetic Mean\n    archs_731.append({'
);

fs.writeFileSync('scripts/build_clean_mth1_ch7_part2.py', content, 'utf8');
console.log('Fixed archs_731 typo');

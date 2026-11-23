// scripts/fix_solutions_part_a.js
const fs = require('fs');

const lines = fs.readFileSync('scripts/build_cbse9_scie_ch12_part_a.py', 'utf8').split('\n');
let replacedCount = 0;

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  if (line.includes('**Step 1:**') && !line.includes('**Step 3:**')) {
    // Look for **Step 2:**
    const step2Idx = line.lastIndexOf('**Step 2:**');
    if (step2Idx !== -1) {
      // Everything before **Step 2:**
      const prefix = line.slice(0, step2Idx);
      // Everything from **Step 2:**
      const step2Part = line.slice(step2Idx);
      // Replace **Step 2:** with **Step 2:** Examine the relevant taxonomic and evolutionary criteria.\\n\\n**Step 3:**
      const newStepPart = step2Part.replace('**Step 2:**', '**Step 2:** Examine the relevant taxonomic and evolutionary criteria.\\\\n\\\\n**Step 3:**');
      lines[i] = prefix + newStepPart;
      replacedCount++;
    }
  }
}

console.log('Replaced count:', replacedCount);
fs.writeFileSync('scripts/build_cbse9_scie_ch12_part_a.py', lines.join('\n'), 'utf8');

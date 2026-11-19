const fs = require('fs');
const questions = JSON.parse(fs.readFileSync('ch5_140_questions.json', 'utf-8'));

questions.slice(0, 5).forEach((q, i) => {
  console.log(`\n--- Q${i+1}: [${q.id}] ---`);
  console.log('Text:', q.text);
  console.log('Ans:', q.correctAnswer);
  const opts = q.options.map(o => typeof o === 'object' ? o.text : String(o));
  console.log('Options:', opts);
  const sol = q.solution || '';
  const part1 = sol.split('### 2.')[0].replace('### 1. Scientific Principle & Mathematical Derivation:', '').trim();
  console.log('Part 1 preview:', part1.slice(0, 200));
});

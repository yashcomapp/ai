const fs = require('fs');
const d = JSON.parse(fs.readFileSync('all_boilerplate_questions.json', 'utf8'));
const scit9 = d.questions.filter(q => q.topicCode.startsWith('MH-9-SCIT'));

const oosKws = [
  'rocket variable mass', 'dp/dt = v', 'integrating both sides', 'schrodinger', 'maxwell',
  'hamiltonian', 'lagrangian', 'relativistic', 'larmor', 'lorentz'
];

const flagged = [];
scit9.forEach(q => {
  const full = (q.text + ' ' + (q.fullExplanation || '')).toLowerCase();
  for (const kw of oosKws) {
    if (full.includes(kw)) {
      flagged.push({ code: q.questionCode, topic: q.topicCode, kw, text: q.text, exp: (q.fullExplanation || '').slice(0, 150) });
      break;
    }
  }
});

console.log('Flagged OOS in MH-9-SCIT:', flagged.length);
flagged.forEach(f => {
  console.log(`- [${f.code}] (${f.topic}) [kw: ${f.kw}]: ${f.text}`);
});

const fs = require('fs');
const d = JSON.parse(fs.readFileSync('ch5_all_questions.json', 'utf8'));

const advancedTerms = [
  '\\lambda', 'lambda', 'photon', '\\Delta E', 'delta e', '\\nu',
  'subshell', 'spectrum', 'spectral', 'quantum', 'joule', '\\text{eV}',
  'angstrom', '\\text{Å}', 'angular momentum', 'mvr', 'c = 3',
  'dielectric', 'permittivity', '0.529', '6.626', 'sin^4', 'larmor',
  'de broglie', 'maxwell', 'schrodinger', 'fermion', 'spin', 'bohr radius',
  'specific charge', 'volume ratio', '10^{15}', '10^{-10}'
];

const flagged = [];
d.questions.forEach(q => {
  const qStr = (q.text + ' ' + JSON.stringify(q.options)).toLowerCase();
  for (const t of advancedTerms) {
    if (qStr.includes(t.toLowerCase())) {
      flagged.push({
        id: q.id,
        code: q.code,
        topic: q.topicCode,
        term: t,
        text: q.text,
        options: q.options,
        correctAnswer: q.correctAnswer
      });
      break;
    }
  }
});

console.log(`Total questions in MH-8-SCI-5 flagged for advanced/OOS terms: ${flagged.length}`);
flagged.forEach((f, idx) => {
  console.log(`[${idx+1}] [${f.code}] (${f.topic}) [Term: ${f.term}]: ${f.text}`);
});

fs.writeFileSync('all_ch5_advanced_flagged.json', JSON.stringify(flagged, null, 2));

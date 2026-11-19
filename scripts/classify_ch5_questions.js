const fs = require('fs');
const d = JSON.parse(fs.readFileSync('ch5_all_questions.json', 'utf8'));

// Forbidden in Class 8 question text/options:
const forbiddenTermsInQuestions = [
  'planck', '6.626', '\\hbar', '0.529', 'sin^4', 'larmor', 'de broglie', '2\\pi r = n\\lambda',
  'mvr = \\frac{nh}{2\\pi}', 'volume ratio', '10^{15}', 'line spectrum', 'spectroscopy',
  'specific charge ratio', 'fermion', 'quantum spin', 'angular momentum', 'hc/\\lambda',
  '\\frac{hc}{\\lambda}', 'maxwell'
];

const badQuestions = [];
const cleanTextButBoilerplateExp = [];

d.questions.forEach(q => {
  const qAndOpts = (q.text + ' ' + JSON.stringify(q.options)).toLowerCase();
  let hasForbidden = false;
  for (const term of forbiddenTermsInQuestions) {
    if (qAndOpts.includes(term.toLowerCase())) {
      hasForbidden = true;
      badQuestions.push({
        id: q.id,
        code: q.code,
        topic: q.topicCode,
        forbiddenTerm: term,
        text: q.text,
        options: q.options,
        correctAnswer: q.correctAnswer
      });
      break;
    }
  }

  const exp = q.explanation || '';
  const hasBoilerplate = /###\s*1\.|###\s*2\.|###\s*3\.|Physical Context:|Core Calculation|Option Analysis|Option [A-D] is correct|Option [A-D] is incorrect/i.test(exp);
  if (!hasForbidden && hasBoilerplate) {
    cleanTextButBoilerplateExp.push({
      id: q.id,
      code: q.code,
      topic: q.topicCode,
      text: q.text
    });
  }
});

console.log(`Bad Question Text / Options (Needs Replacement/Rewrite): ${badQuestions.length}`);
console.log(`Good Question Text but Boilerplate Explanation: ${cleanTextButBoilerplateExp.length}`);

fs.writeFileSync('ch5_classification.json', JSON.stringify({
  badQuestionsCount: badQuestions.length,
  badQuestions,
  cleanTextCount: cleanTextButBoilerplateExp.length,
  cleanTextButBoilerplateExp
}, null, 2));

console.log('Sample Bad Questions:');
badQuestions.slice(0, 10).forEach(b => {
  console.log(`- [${b.code}] (${b.topic}) [Term: ${b.forbiddenTerm}]: ${b.text}`);
});

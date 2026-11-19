const fs = require('fs');
const d = JSON.parse(fs.readFileSync('ch5_all_questions.json', 'utf8'));
const q = d.questions.find(x => x.code === 'MH-8-SCI-5-5.3.2-OSC-006' || x.id === 'MH-8-SCI-5-5.3.2-OSC-006');
if (q) {
  console.log('Found MH-8-SCI-5-5.3.2-OSC-006:');
  console.log(JSON.stringify(q, null, 2));
} else {
  console.log('Not found in ch5_all_questions.json');
}

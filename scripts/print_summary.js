const fs = require('fs');
const data = JSON.parse(fs.readFileSync('scripts/students_dump.json', 'utf-8'));
const { students } = data;

const batches = [...new Set(students.map(s => s.batchName))].sort();

batches.forEach(b => {
  console.log('\n### ' + b);
  const inBatch = students.filter(s => s.batchName === b);
  const auto = inBatch.filter(s => s.autonomous);
  const reg = inBatch.filter(s => !s.autonomous);
  console.log(`\n**Autonomous (${auto.length}):**`);
  auto.forEach((s, i) => console.log(`${i + 1}. ${s.name} (${s.studentCode}) - ${s.status}`));
  console.log(`\n**Regular (${reg.length}):**`);
  reg.forEach((s, i) => console.log(`${i + 1}. ${s.name} (${s.studentCode}) - ${s.status}`));
});

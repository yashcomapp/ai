const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function audit() {
  console.log('Auditing MH-10-MTH1 questions in Firestore...');
  const snap = await db.collection('questions')
    .where('subjectCode', '==', 'MTH1')
    .where('class', '==', '10')
    .get();

  console.log(`Total questions with subjectCode MTH1: ${snap.size}`);

  const topicCounts = {};
  const vaultCounts = { exam: 0, practice: 0, mock: 0, other: 0 };
  let issues = 0;

  snap.docs.forEach(doc => {
    const data = doc.data();
    const t = data.topicCode || 'NO_TOPIC';
    topicCounts[t] = (topicCounts[t] || 0) + 1;
    const v = data.vault || 'other';
    vaultCounts[v] = (vaultCounts[v] || 0) + 1;
  });

  console.log('\n--- Tally by Topic ---');
  const sortedTopics = Object.keys(topicCounts).sort();
  for (const t of sortedTopics) {
    const count = topicCounts[t];
    const status = count === 82 ? 'OK' : 'MISMATCH';
    if (count !== 82) issues++;
    console.log(`  ${t}: ${count} [${status}]`);
  }

  console.log('\n--- Vault Distribution ---');
  console.log(`  Exam: ${vaultCounts.exam} (Target: ${sortedTopics.length * 40})`);
  console.log(`  Practice: ${vaultCounts.practice} (Target: ${sortedTopics.length * 30})`);
  console.log(`  Mock: ${vaultCounts.mock} (Target: ${sortedTopics.length * 12})`);
  console.log(`  Other: ${vaultCounts.other}`);

  console.log(`\nTotal topics audited: ${sortedTopics.length} / 29`);
  console.log(`Total questions: ${snap.size} / 2378`);
  console.log(`Issues found: ${issues}`);

  process.exit(issues > 0 ? 1 : 0);
}

audit();

// scripts/verify_mh9_mth1_full_compliance.js
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function verifyCompliance() {
  console.log('=== FULL COMPLIANCE AUDIT: MH-9-MTH1 (ALL CHAPTERS 1 TO 7) ===\n');

  let totalQuestions = 0;
  let nonCompliantTopics = [];
  let compliantTopics = 0;

  for (let ch = 1; ch <= 7; ch++) {
    const snap = await adminDb.collection('questions')
      .where('questionCode', '>=', `MH-9-MTH1-${ch}-`)
      .where('questionCode', '<=', `MH-9-MTH1-${ch}-\uf8ff`)
      .get();
    
    totalQuestions += snap.size;
    console.log(`--- Chapter ${ch} (Total Questions: ${snap.size}) ---`);

    const byTopic = {};
    snap.docs.forEach(d => {
      const q = d.data();
      const t = q.topicCode || 'unknown';
      if (!byTopic[t]) byTopic[t] = { exam: 0, practice: 0, foundation: 0, total: 0 };
      const vault = (q.vault || 'exam').toLowerCase();
      byTopic[t][vault] = (byTopic[t][vault] || 0) + 1;
      byTopic[t].total++;
    });

    for (const [topic, counts] of Object.entries(byTopic)) {
      const isCompliant = counts.exam >= 40 && counts.practice >= 20 && counts.foundation >= 20 && counts.total >= 80;
      if (isCompliant) {
        compliantTopics++;
        console.log(`  ✓ ${topic}: Total ${counts.total} (Exam: ${counts.exam}, Practice: ${counts.practice}, Foundation: ${counts.foundation})`);
      } else {
        nonCompliantTopics.push({ topic, counts });
        console.error(`  ✗ ${topic}: Total ${counts.total} (Exam: ${counts.exam}, Practice: ${counts.practice}, Foundation: ${counts.foundation}) - DEFICIT DETECTED!`);
      }
    }
  }

  console.log(`\n================ SUMMARY ================`);
  console.log(`Total MH-9-MTH1 Questions in Database: ${totalQuestions}`);
  console.log(`Compliant Topics: ${compliantTopics}`);
  console.log(`Non-Compliant Topics: ${nonCompliantTopics.length}`);

  if (nonCompliantTopics.length > 0) {
    console.error('FAILED: Some topics do not meet Rule 2T (80Q standard)!');
    process.exit(1);
  } else {
    console.log('SUCCESS: ALL TOPICS IN MH-9-MTH1 ARE 100% COMPLIANT WITH RULE 2T!');
    process.exit(0);
  }
}

verifyCompliance().catch(console.error);

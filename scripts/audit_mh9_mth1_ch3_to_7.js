// scripts/audit_mh9_mth1_ch3_to_7.js
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function audit() {
  for (let ch = 3; ch <= 7; ch++) {
    const snap = await adminDb.collection('questions')
      .where('questionCode', '>=', `MH-9-MTH1-${ch}-`)
      .where('questionCode', '<=', `MH-9-MTH1-${ch}-\uf8ff`)
      .get();
    
    console.log(`\n================ Chapter ${ch} (Total: ${snap.size} questions) ================`);
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
      const examDeficit = Math.max(0, 40 - counts.exam);
      const practiceDeficit = Math.max(0, 20 - counts.practice);
      const foundationDeficit = Math.max(0, 20 - counts.foundation);
      const totalDeficit = Math.max(0, 80 - counts.total);
      console.log(`Topic: ${topic} | Total: ${counts.total} (Exam: ${counts.exam}, Practice: ${counts.practice}, Foundation: ${counts.foundation}) | Deficit -> Exam: ${examDeficit}, Practice: ${practiceDeficit}, Foundation: ${foundationDeficit}`);
    }
  }
}

audit().catch(console.error);

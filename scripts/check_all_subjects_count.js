const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function check() {
  const snap = await adminDb.collection('questions').select('boardCode', 'class', 'subjectCode').get();
  const summary = {};
  snap.docs.forEach(d => {
    const data = d.data();
    const key = `${data.boardCode}-${data.class}-${data.subjectCode}`;
    summary[key] = (summary[key] || 0) + 1;
  });
  console.log('Current Firestore Questions by Subject:');
  console.table(summary);
}
check().catch(console.error);

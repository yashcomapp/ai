const admin = require('firebase-admin');
const fs = require('fs');
const envVars = {};
fs.readFileSync('.env.local', 'utf-8').split('\n').forEach(l => {
  const t = l.trim();
  if (t && !t.startsWith('#')) {
    const idx = t.indexOf('=');
    if (idx > 0) envVars[t.slice(0, idx).trim()] = t.slice(idx + 1).trim().replace(/^['"]|['"]$/g, '');
  }
});
admin.initializeApp({ credential: admin.credential.cert(JSON.parse(envVars.FIREBASE_SERVICE_ACCOUNT_KEY)) });
const db = admin.firestore();

async function inspectReviews() {
  // Find review with studentCode ST-2026-000066
  const rSnap = await db.collection('reviews').where('studentCode', '==', 'ST-2026-000066').get();
  console.log('Reviews for ST-2026-000066:', rSnap.size);
  rSnap.forEach(d => {
    const data = d.data();
    console.log('Doc ID:', d.id);
    console.log('Exam ID:', data.examId);
    console.log('Student Name in review doc:', data.studentName);
    console.log('Score:', data.score, 'totalMarks:', data.totalMarks, 'percentage:', data.percentage);
  });
}

inspectReviews().catch(console.error);

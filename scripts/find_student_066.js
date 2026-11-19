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

async function findStudent() {
  const uSnap = await db.collection('users').where('studentCode', '==', 'ST-2026-000066').get();
  console.log('Users found:', uSnap.size);
  uSnap.forEach(d => console.log('User:', d.id, 'name:', d.data().name, 'studentName:', d.data().studentName, 'role:', d.data().role));

  const aSnap = await db.collection('attempts').where('studentCode', '==', 'ST-2026-000066').get();
  console.log('Attempts found:', aSnap.size);
  aSnap.forEach(d => {
    const data = d.data();
    console.log('Attempt ID:', d.id, 'examId:', data.examId, 'studentName:', data.studentName, 'score:', data.score, 'percentage:', data.percentage, 'marksObtained:', data.marksObtained);
  });
}

findStudent().catch(console.error);

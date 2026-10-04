const fs = require('fs');
const admin = require('firebase-admin');

const envContent = fs.readFileSync('.env.local', 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      const k = trimmed.slice(0, idx).trim();
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[k] = v;
    }
  }
});

const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  if (sa) {
    const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
    admin.initializeApp({ credential: admin.credential.cert(cred) });
  } else {
    admin.initializeApp({ projectId: envVars.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom' });
  }
}
const db = admin.firestore();

async function testAdhiraReviews() {
  const studentCode = 'ST-2026-000065'; // Adhira Sumit Warge
  const [objSnaps, evalSnaps] = await Promise.all([
    db.collection('reviews').where('studentCode', '==', studentCode).get(),
    db.collection('evaluations').where('studentCode', '==', studentCode).where('evaluatorType', '==', 'parent').get()
  ]);

  const evalMap = new Map();
  evalSnaps.docs.forEach(doc => {
    const data = doc.data();
    if (data.attemptId) evalMap.set(data.attemptId, data);
    if (data.legacyId) evalMap.set(data.legacyId, data);
    if (data.examId) evalMap.set(data.examId, data);
    if (doc.id) evalMap.set(doc.id, data);
  });

  const objMapped = objSnaps.docs.map(doc => {
    const data = doc.data();
    if (data.examType === 'practice') return null;
    const isReviewed = data.status === 'approved' || data.parentStatus === 'approved' || evalMap.has(doc.id) || (data.examId && evalMap.has(data.examId));
    return {
      id: doc.id,
      examId: data.examId,
      status: isReviewed ? 'approved' : 'pending',
      score: data.score,
      completedAt: data.completedAt || data.startedAt
    };
  }).filter(Boolean);

  const pending = objMapped.filter(r => r.status === 'pending');
  const approved = objMapped.filter(r => r.status === 'approved');

  console.log('TOTAL OBJECTIVE REVIEWS:', objMapped.length);
  console.log('PENDING REVIEWS:', JSON.stringify(pending, null, 2));
  console.log('APPROVED REVIEWS COUNT:', approved.length);
}

testAdhiraReviews().catch(console.error);

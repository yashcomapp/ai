const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[trimmed.slice(0, idx).trim()] = v;
    }
  }
});
const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

function toDate(ts) {
  if (!ts) return null;
  if (ts.toDate) return ts.toDate();
  if (ts._seconds) return new Date(ts._seconds * 1000);
  if (typeof ts === 'string' || typeof ts === 'number') return new Date(ts);
  return null;
}

async function run() {
  console.log('=== Checking Class 10 Exams and Attempts in Oct/Nov 2026 ===');
  const attemptsSnap = await db.collection('examAttempts').get();
  console.log(`Total examAttempts in DB: ${attemptsSnap.size}`);

  const recentClass10 = [];
  attemptsSnap.forEach(d => {
    const data = d.data();
    const dDate = toDate(data.submittedAt) || toDate(data.createdAt);
    if (!dDate) return;
    const iso = dDate.toISOString();
    if (iso.startsWith('2026-11') || iso.startsWith('2026-10')) {
      const examId = data.examId || '';
      const isClass10 = examId.includes('-10-') || d.id.includes('-10-') || (data.examName && data.examName.includes('10'));
      if (isClass10) {
        recentClass10.push({
          id: d.id,
          examId: data.examId,
          examName: data.examName,
          studentName: data.studentName,
          studentCode: data.studentCode,
          score: data.score,
          totalMarks: data.totalMarks,
          percentage: data.percentage,
          date: dDate.toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })
        });
      }
    }
  });

  console.log(`Found ${recentClass10.length} Class 10 attempts in Oct/Nov 2026:`);
  console.table(recentClass10);

  // Check if Exam 024 (the one created today or yesterday for Class 10) had any attempts
  const exam024Snap = await db.collection('examAttempts')
    .where('examId', 'in', ['024-MH-10-Quadratic-2.1-2.3-191126', '024-MH-10-Quadratic-2.1-2.3-201126'])
    .get();
  console.log(`Attempts for Exam 024: ${exam024Snap.size}`);
}

run().catch(console.error);

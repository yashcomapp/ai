const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
let saKey = '';
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed.startsWith('FIREBASE_SERVICE_ACCOUNT_KEY=')) {
    saKey = trimmed.replace('FIREBASE_SERVICE_ACCOUNT_KEY=', '').trim();
    if ((saKey.startsWith('"') && saKey.endsWith('"')) || (saKey.startsWith("'") && saKey.endsWith("'"))) {
      saKey = saKey.slice(1, -1);
    }
  }
});

const cred = JSON.parse(saKey.startsWith('{') ? saKey : Buffer.from(saKey, 'base64').toString('utf-8'));
if (!admin.apps.length) admin.initializeApp({ credential: admin.credential.cert(cred) });
const db = admin.firestore();

async function check() {
  const collections = [
    'questions', 'syllabus', 'syllabusTopicIndex', 'exams', 'subjectiveExams',
    'examAttempts', 'subjectiveAttempts', 'reviews', 'parentReviews',
    'evaluations', 'studentTopicMastery', 'liveExamSessions', 'liveExamEvidence',
    'chatMessages', 'chatChannels', 'users', 'batches', 'notices',
    'attendance', 'dailyPractices', 'practiceSubmissions'
  ];
  console.log('Collection Document Counts (via aggregation count - zero payload):');
  for (const c of collections) {
    try {
      const snap = await db.collection(c).count().get();
      console.log(`  ${c.padEnd(25)}: ${snap.data().count}`);
    } catch (e) {
      console.log(`  ${c.padEnd(25)}: error - ${e.message}`);
    }
  }
  const inProgSnap = await db.collection('liveExamSessions').where('status', '==', 'in-progress').count().get();
  console.log(`\n  Live Sessions 'in-progress': ${inProgSnap.data().count}`);
}
check().catch(console.error);

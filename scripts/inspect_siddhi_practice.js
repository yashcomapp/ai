const path = require('path');
const fs = require('fs');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const content = fs.readFileSync(envPath, 'utf8');
  content.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        const key = trimmed.slice(0, idx).trim();
        let val = trimmed.slice(idx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
        if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
        process.env[key] = val;
      }
    }
  });
}

const admin = require('firebase-admin');
const credential = JSON.parse(
  process.env.FIREBASE_SERVICE_ACCOUNT_KEY.startsWith('{')
    ? process.env.FIREBASE_SERVICE_ACCOUNT_KEY
    : Buffer.from(process.env.FIREBASE_SERVICE_ACCOUNT_KEY, 'base64').toString('utf-8')
);
if (!admin.apps.length) {
  admin.initializeApp({
    credential: admin.credential.cert(credential)
  });
}
const db = admin.firestore();

async function inspectSiddhi() {
  console.log('--- Finding Siddhi Dangra ---');
  const uSnap = await db.collection('users')
    .where('role', '==', 'student')
    .get();

  let siddhi = null;
  uSnap.forEach(d => {
    const data = d.data();
    if ((data.name && data.name.toLowerCase().includes('siddhi')) || (data.displayName && data.displayName.toLowerCase().includes('siddhi'))) {
      siddhi = { id: d.id, ...data };
    }
  });

  if (!siddhi) {
    console.log('Siddhi not found in users collection!');
    return;
  }
  console.log(`Found student: ${siddhi.name} (${siddhi.studentCode}), Class: ${siddhi.className}, uid: ${siddhi.uid || siddhi.id}`);

  console.log('\n--- Checking practiceSubmissions for Siddhi ---');
  const pSnap = await db.collection('practiceSubmissions')
    .where('studentCode', '==', siddhi.studentCode)
    .get();

  console.log(`Found ${pSnap.size} practice submissions for ${siddhi.studentCode}`);
  pSnap.forEach(doc => {
    const sub = doc.data();
    console.log(`\nPractice ID: ${doc.id} | TopicCode: ${sub.topicCode} | Date: ${sub.createdAt ? (sub.createdAt.toDate ? sub.createdAt.toDate().toISOString() : sub.createdAt) : 'N/A'}`);
    console.log(`Topic Title: ${sub.topicTitle || sub.title}`);
    console.log(`Score: ${sub.score} / ${sub.totalQuestions}`);
    if (sub.questions) {
      console.log(`Questions count in submission: ${sub.questions.length}`);
      sub.questions.forEach((q, i) => {
        console.log(`  [Q${i+1}] ID: ${q.questionId || q.id || q.questionCode}`);
        console.log(`       Text: ${q.text || q.questionText}`);
        console.log(`       Student Ans: ${q.selectedAnswer || q.userAnswer || q.studentAnswer}`);
        console.log(`       Correct Ans: ${q.correctAnswer}`);
        console.log(`       isCorrect: ${q.isCorrect}`);
        console.log(`       Sol: ${q.solution || q.explanation}`);
      });
    }
  });

  // Also check parentReviews
  const prSnap = await db.collection('parentReviews')
    .where('studentCode', '==', siddhi.studentCode)
    .get();
  console.log(`\nFound ${prSnap.size} parent reviews for ${siddhi.studentCode}`);
  prSnap.forEach(doc => {
    const pr = doc.data();
    console.log(`ParentReview ID: ${doc.id} | Type: ${pr.examType || pr.type} | ExamId: ${pr.examId} | Title: ${pr.title}`);
    if (pr.questions) {
      pr.questions.forEach((q, i) => {
        console.log(`  [Review Q${i+1}] ${q.text || q.questionText}`);
        console.log(`       Correct: ${q.correctAnswer} | Given: ${q.selectedAnswer || q.userAnswer}`);
        console.log(`       Sol: ${q.solution || q.explanation}`);
      });
    }
  });
}

inspectSiddhi().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });

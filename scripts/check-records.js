const path = require('path');
const fs = require('fs');

// Load environment
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
const projectId = process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || "ai-yashcom";

if (!admin.apps.length) {
  const serviceAccount = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
  if (serviceAccount) {
    const credential = JSON.parse(
      serviceAccount.startsWith('{')
        ? serviceAccount
        : Buffer.from(serviceAccount, 'base64').toString('utf-8')
    );
    admin.initializeApp({
      credential: admin.credential.cert(credential)
    });
  } else {
    admin.initializeApp({ projectId });
  }
}

const db = admin.firestore();

async function run() {
  console.log('Querying users for Vrujesh...');
  const usersSnap = await db.collection('users').get();
  const allUsers = [];
  usersSnap.forEach(d => allUsers.push({ id: d.id, ...d.data() }));

  const vrujesh = allUsers.find(u => (u.name && u.name.toLowerCase().includes('vrujesh')) || (u.studentName && u.studentName.toLowerCase().includes('vrujesh')));
  console.log('Vrujesh user doc:', vrujesh ? { id: vrujesh.id, studentCode: vrujesh.studentCode, name: vrujesh.name, role: vrujesh.role } : 'Not found');

  const studentCode = vrujesh?.studentCode || 'ST-2026-000030';

  console.log(`\nChecking practiceSubmissions for ${studentCode}...`);
  const pracSnap = await db.collection('practiceSubmissions').where('studentCode', '==', studentCode).get();
  console.log(`Found ${pracSnap.size} practiceSubmissions for ${studentCode}`);
  pracSnap.forEach(doc => {
    const data = doc.data();
    console.log(`\nPractice ID: ${doc.id}`);
    console.log(`Topic: ${data.topicCode}, Score: ${data.score}/${data.questionsAttempted}, Total Qs: ${(data.questions || []).length}`);
    if (data.questions) {
      data.questions.forEach((q, idx) => {
        console.log(`  Q${idx + 1}: type=${q.type}, userAns=${JSON.stringify(q.userAnswer)}, correctAns=${JSON.stringify(q.correctAnswer || q.correctAnswers)}, isCorrect=${q.isCorrect}`);
        if (q.options) {
          console.log(`      options: ${JSON.stringify(q.options)}`);
        }
      });
    }
  });

  console.log(`\nChecking examAttempts for ${studentCode}...`);
  const examSnap = await db.collection('examAttempts').where('studentCode', '==', studentCode).get();
  console.log(`Found ${examSnap.size} examAttempts for ${studentCode}`);
  examSnap.forEach(doc => {
    const data = doc.data();
    console.log(`\nExam Attempt ID: ${doc.id}`);
    console.log(`Exam ID: ${data.examId}, Score: ${data.score}/${data.totalMarks}, Percentage: ${data.percentage}%`);
    if (data.questionDetails) {
      data.questionDetails.forEach((qd, idx) => {
        console.log(`  Q${idx + 1}: code=${qd.questionCode}, userAns=${JSON.stringify(qd.userAnswer)}, correctAns=${JSON.stringify(qd.correctAnswer)}, isCorrect=${qd.isCorrect}`);
      });
    }
  });
}

run().catch(console.error).then(() => process.exit(0));

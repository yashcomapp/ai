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

async function checkClass10ScoreImpact() {
  const examId = '023-MH-10-Linear Equations-1.4-1.5-181126';
  const attSnap = await db.collection('examAttempts').where('examId', '==', examId).get();
  
  // In Exam 023, every question Q1 to Q15 had correctAnswer = 'A' at exam time!
  // If every question had correctAnswer = 'A', then:
  // Any answer 'A' gets +4 marks.
  // Any answer that is not 'A' and not empty (e.g. 'B', 'C', 'D') gets -1 mark.
  // Any empty answer gets 0 marks.
  // Regardless of the order of questions, if EVERY question has correctAnswer = 'A',
  // does the total score change if questions are re-ordered?
  // Let's check!
  
  console.log('=== CHECKING IF TOTAL SCORE CHANGED FOR CLASS 10 STUDENTS ===');
  for (const doc of attSnap.docs) {
    const att = doc.data();
    const rawAnswers = att.userAnswers || [];
    
    let calcScore = 0;
    let correct = 0;
    let wrong = 0;
    let unattempted = 0;
    
    rawAnswers.forEach(ansObj => {
      const a = (typeof ansObj === 'object' ? ansObj.answer : ansObj || '').trim().toUpperCase();
      if (!a) {
        unattempted++;
      } else if (a === 'A') {
        correct++;
        calcScore += 4;
      } else {
        wrong++;
        calcScore -= 1;
      }
    });
    
    console.log(`${att.studentName.padEnd(25)} | Recorded Score: ${att.score} | Pure A Score: ${calcScore} | Diff: ${calcScore - att.score} | C:${correct} W:${wrong} U:${unattempted}`);
  }
}

checkClass10ScoreImpact().catch(console.error);

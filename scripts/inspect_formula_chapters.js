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
const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
admin.initializeApp({ credential: admin.credential.cert(cred) });
const db = admin.firestore();

async function inspectFormulaChapters() {
  // Collect all question IDs used in exams or attempts
  const usedQuestionIds = new Set();
  
  const examsSnap = await db.collection('exams').get();
  examsSnap.forEach(doc => {
    const data = doc.data();
    if (Array.isArray(data.questions)) {
      data.questions.forEach(q => {
        if (typeof q === 'string') usedQuestionIds.add(q);
        else if (q && q.id) usedQuestionIds.add(q.id);
        else if (q && q.questionCode) usedQuestionIds.add(q.questionCode);
      });
    }
  });

  const attemptsSnap = await db.collection('examAttempts').get();
  attemptsSnap.forEach(doc => {
    const data = doc.data();
    if (data.answers && typeof data.answers === 'object') {
      Object.keys(data.answers).forEach(qid => usedQuestionIds.add(qid));
    }
  });

  console.log(`Total used question identifiers: ${usedQuestionIds.size}`);

  // Formula chapters to inspect
  const formulaChapters = [
    'MH-9-SCIT-1',   // Laws of Motion
    'MH-9-SCIT-2',   // Work and Energy
    'MH-9-SCIT-3',   // Current Electricity
    'MH-9-SCIT-4',   // Measurement of Matter
    'MH-9-SCIT-11',  // Reflection of Light
    'MH-9-SCIT-12',  // Study of Sound
    'MH-9-SCIT-18',  // Observing Space: Telescopes
    'MH-8-SCI-3',    // Force and Pressure
    'MH-8-SCI-14',   // Measurement and Effects of Heat
    'MH-8-SCI-15'    // Sound
  ];

  for (const ch of formulaChapters) {
    const qSnap = await db.collection('questions')
      .where('topicCode', '>=', ch)
      .where('topicCode', '<=', ch + '-\uf8ff')
      .get();
    
    let total = qSnap.size;
    let oneCount = 0;
    let ssnCount = 0;
    let unusedTheoretical = 0;

    qSnap.forEach(doc => {
      const q = doc.data();
      const isUsed = usedQuestionIds.has(doc.id) || usedQuestionIds.has(q.questionCode);
      const isNum = q.type === 'ONE' || q.type === 'SSN' || q.type === 'SLN';
      if (q.type === 'ONE') oneCount++;
      if (q.type === 'SSN') ssnCount++;
      if (!isUsed && !isNum) unusedTheoretical++;
    });

    console.log(`\nChapter ${ch}:`);
    console.log(`  Total Questions: ${total}`);
    console.log(`  Current Numericals (ONE): ${oneCount}, (SSN): ${ssnCount}`);
    console.log(`  Unused Theoretical Questions available to replace: ${unusedTheoretical}`);
  }
}

inspectFormulaChapters().then(() => process.exit(0)).catch(console.error);

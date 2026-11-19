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

async function checkClass10() {
  const allExams = await db.collection('exams').get();
  const class10Exams = [];
  allExams.forEach(d => {
    const data = d.data();
    if ((data.name && data.name.includes('-10-')) || data.class === 'Class 10') {
      class10Exams.push({ id: d.id, ...data });
    }
  });

  console.log(`Found ${class10Exams.length} Class 10 exams.`);
  for (const ex of class10Exams) {
    console.log(`\nExam: [${ex.id}] ${ex.name} (Status: ${ex.status}, Date: ${ex.date})`);
    const qCodes = ex.questionCodes || [];
    console.log(`  Question codes count: ${qCodes.length}`);
    if (qCodes.length === 0) continue;

    // Check if doc IDs exist directly in 'questions'
    const refs = qCodes.map(id => db.collection('questions').doc(id));
    const docSnaps = await db.getAll(...refs);
    const foundDirectly = docSnaps.filter(s => s.exists).length;
    console.log(`  Direct doc ID match: ${foundDirectly} / ${qCodes.length}`);

    // If direct doc ID match is 100%, getAll(...refs) preserves exact array order!
    // In Class 8, direct match was 0/30 because doc IDs were MH-8-SCI-5-5.1-OSC-xxx while codes were 5.1.1!
    
    // Check attempts
    const attSnap = await db.collection('examAttempts').where('examId', '==', ex.id).get();
    console.log(`  Attempts count: ${attSnap.size}`);
    
    // Check if any attempt has reviews
    for (const aDoc of attSnap.docs) {
      const att = aDoc.data();
      const revSnap = await db.collection('reviews').doc(aDoc.id).get();
      const rev = revSnap.exists ? revSnap.data() : null;
      console.log(`    - ${att.studentName || att.studentCode}: score=${att.score}/${att.maxScore} (${att.percentage}%), reviewStored=${!!rev}`);
    }
  }
}

checkClass10().catch(console.error);

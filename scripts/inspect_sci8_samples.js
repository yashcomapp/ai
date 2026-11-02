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

async function inspectSci8() {
  const snap = await db.collection('questions')
    .where('subjectCode', '==', 'SCI')
    .where('class', 'in', ['8', 8])
    .get();

  console.log(`Total questions in MH-8-SCI: ${snap.size}`);

  let withoutSol = 0;
  let withSol = 0;

  snap.forEach(d => {
    const q = d.data();
    const sol = (q.solution || q.explanation || '').trim();
    if (!sol) withoutSol++;
    else withSol++;
  });

  console.log(`With solution: ${withSol}, Without solution: ${withoutSol}`);

  // Sample 5 questions without solution
  console.log('\nSample 5 questions without solution in MH-8-SCI:');
  let count = 0;
  snap.forEach(d => {
    const q = d.data();
    const sol = (q.solution || q.explanation || '').trim();
    if (!sol && count < 5) {
      console.log(`[${d.id}] Ch: ${q.chapterNumber}`);
      console.log(`  Text: ${q.text}`);
      console.log(`  Opts:`, q.options);
      console.log(`  Correct:`, q.correctAnswer);
      count++;
    }
  });
}

inspectSci8().then(() => process.exit(0)).catch(console.error);

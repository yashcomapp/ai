// scripts/extract-ch3-raw.js
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
  admin.initializeApp({ projectId: 'ai-yashcom' });
}

const db = admin.firestore();

async function extractRaw() {
  console.log('Fetching all Chapter 3 questions (MH-9-SCIT-3)...');
  const snap = await db.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .where('chapterNumber', '==', '3')
    .get();

  console.log(`Fetched ${snap.size} questions.`);
  const questions = [];
  snap.forEach(d => {
    questions.push({ id: d.id, ...d.data() });
  });

  // Sort by numeric sequence in id
  questions.sort((a, b) => {
    const numA = parseInt(a.id.split('-').pop(), 10) || 0;
    const numB = parseInt(b.id.split('-').pop(), 10) || 0;
    return numA - numB;
  });

  const outPath = 'backups/staging/mh9_scit_3_raw.json';
  fs.writeFileSync(outPath, JSON.stringify(questions, null, 2), 'utf8');
  console.log(`Saved raw Chapter 3 questions to ${outPath} (${fs.statSync(outPath).size} bytes).`);
}

extractRaw().then(() => process.exit(0)).catch(err => {
  console.error(err);
  process.exit(1);
});

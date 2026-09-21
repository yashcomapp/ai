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

async function checkOMC() {
  const qSnap = await db.collection('questions')
    .where('topicCode', '==', 'MH-9-SCIT-8-8.1.2')
    .where('type', '==', 'multiple_mcq')
    .get();

  console.log(`Found ${qSnap.size} multiple_mcq questions for MH-9-SCIT-8-8.1.2:`);
  qSnap.forEach(d => {
    const q = d.data();
    console.log(`\nID: ${d.id}, Code: ${q.questionCode}`);
    console.log(`Text: ${q.text}`);
    console.log(`Options: ${JSON.stringify(q.options)}`);
    console.log(`correctAnswer: ${JSON.stringify(q.correctAnswer)}`);
    console.log(`correctAnswers: ${JSON.stringify(q.correctAnswers)}`);
  });
}

checkOMC().catch(console.error).then(() => process.exit(0));

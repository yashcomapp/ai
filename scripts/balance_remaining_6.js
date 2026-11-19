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

const targetTopics = [
  'CBSE-8-CURI-5-5.3.3',
  'MH-10-SCIT2-8-8.4.2',
  'MH-8-MTH-13-13.1.1',
  'MH-8-MTH-13-13.2.1',
  'MH-8-MTH-8-8.4.1',
  'MH-9-MTH1-3-3.3.1'
];

async function balance6() {
  const batch = db.batch();
  for (const tCode of targetTopics) {
    const snap = await db.collection('questions')
      .where('topicCode', '==', tCode)
      .where('correctAnswer', '==', 'A')
      .get();
    
    // We only need to swap 3 questions to B, C, D to bring A down to ~25%
    const letters = ['B', 'C', 'D'];
    let idx = 0;
    for (const doc of snap.docs) {
      if (idx >= 3) break;
      const d = doc.data();
      const currentOpts = [...d.options];
      const targetLetter = letters[idx];
      const targetIdx = targetLetter.charCodeAt(0) - 65;

      const temp = currentOpts[0];
      currentOpts[0] = currentOpts[targetIdx];
      currentOpts[targetIdx] = temp;

      if (typeof currentOpts[0] === 'object' && currentOpts[0] !== null) {
        currentOpts.forEach((opt, oi) => {
          opt.isCorrect = (oi === targetIdx);
        });
      }

      batch.update(doc.ref, {
        options: currentOpts,
        correctAnswer: targetLetter,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      idx++;
    }
  }
  await batch.commit();
  console.log('✓ Successfully balanced the remaining 6 topics.');
}

balance6().catch(console.error);

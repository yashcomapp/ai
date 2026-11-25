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

function stripOptionLetterCitations(str) {
  if (typeof str !== 'string') return str;
  let out = str;
  // Remove trailing/inline "Correct Choice is (A)."
  out = out.replace(/\s*\n*Correct Choice is \([A-D]\)\.?/gi, '');
  // Remove "Hence/Therefore/Thus/So, Option A is correct." or "Option (A) is correct."
  out = out.replace(/\s*(?:Hence,?\s*|Therefore,?\s*|Thus,?\s*|So,?\s*)?Option\s*\(?[A-D]\)?\s*is\s*correct\.?/gi, '');
  return out.trim();
}

async function run() {
  const backupDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(backupDir)) fs.mkdirSync(backupDir, { recursive: true });
  const backupPath = path.join(backupDir, `snapshot_strip_opt_letters_${Date.now()}.jsonl`);
  const backupStream = fs.createWriteStream(backupPath, { flags: 'w', encoding: 'utf-8' });

  let lastDoc = null;
  const pageSize = 5000;
  let scanned = 0;
  let updated = 0;

  while (true) {
    let qRef = db.collection('questions').orderBy(admin.firestore.FieldPath.documentId()).limit(pageSize);
    if (lastDoc) qRef = qRef.startAfter(lastDoc);
    const snap = await qRef.get();
    if (snap.empty) break;

    let batch = db.batch();
    let batchCount = 0;

    for (const doc of snap.docs) {
      scanned++;
      const q = doc.data();
      const origSol = q.solution;
      const origExp = q.explanation;

      const newSol = typeof origSol === 'string' ? stripOptionLetterCitations(origSol) : origSol;
      const newExp = typeof origExp === 'string' ? stripOptionLetterCitations(origExp) : origExp;

      const solChanged = typeof origSol === 'string' && newSol !== origSol && newSol.length >= 10;
      const expChanged = typeof origExp === 'string' && newExp !== origExp && newExp.length >= 10;

      if (solChanged || expChanged) {
        backupStream.write(JSON.stringify({ id: doc.id, solution: origSol, explanation: origExp }) + '\n');
        const payload = { updatedAt: admin.firestore.FieldValue.serverTimestamp() };
        if (solChanged) payload.solution = newSol;
        if (expChanged) payload.explanation = newExp;
        batch.update(doc.ref, payload);
        batchCount++;
        updated++;

        if (batchCount >= 400) {
          await batch.commit();
          batch = db.batch();
          batchCount = 0;
        }
      }
    }

    if (batchCount > 0) {
      await batch.commit();
    }

    lastDoc = snap.docs[snap.docs.length - 1];
    console.log(`Scanned ${scanned}... (updated so far: ${updated})`);
  }

  backupStream.end();
  console.log(`\n✓ Done! Scanned: ${scanned}, Updated explanations: ${updated}`);
  console.log(`✓ Pre-mutation backup saved to ${path.basename(backupPath)}`);
}

run().catch(err => {
  console.error(err);
  process.exit(1);
});

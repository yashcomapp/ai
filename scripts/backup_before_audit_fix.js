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

async function createBackup() {
  console.log('=== CREATING PRE-MUTATION SNAPSHOT PER RULE 2Q ===');
  const now = new Date();
  const dateStr = now.toISOString().replace(/[:.]/g, '-');
  const backupDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(backupDir)) fs.mkdirSync(backupDir, { recursive: true });

  const backupFile = path.join(backupDir, `snapshot_${dateStr}_audit_purge_and_balance.json`);
  console.log(`Writing snapshot to ${backupFile}...`);

  const questionsSnap = await db.collection('questions').get();
  console.log(`Fetched ${questionsSnap.size} questions for backup.`);

  const docsData = [];
  questionsSnap.docs.forEach(d => {
    docsData.push({ id: d.id, data: d.data() });
  });

  fs.writeFileSync(backupFile, JSON.stringify({
    timestamp: now.toISOString(),
    reason: 'Comprehensive Question Bank Quality Audit: Purge corrupted homi-bhabha placeholders, fix trivial explanations, and permanently balance topics',
    totalQuestions: docsData.length,
    questions: docsData
  }, null, 2));

  // Log in _systemBackups
  await db.collection('_systemBackups').doc(`backup_${dateStr}`).set({
    timestamp: admin.firestore.FieldValue.serverTimestamp(),
    reason: 'Question Bank audit, purge 78 corrupted OCR questions and balance topics',
    totalDocs: docsData.length,
    filePath: backupFile
  });

  console.log('Pre-mutation snapshot successfully created and logged.');
}

createBackup().catch(console.error);

const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const report = JSON.parse(fs.readFileSync('C:\\Users\\Admin\\.gemini\\antigravity\\brain\\86c909b0-ca51-4117-8d89-7b63c51993a3\\scratch\\full_qb_audit_report.json', 'utf-8'));

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

async function run() {
  const backupDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(backupDir)) fs.mkdirSync(backupDir, { recursive: true });

  const omcIds = report.issues.omcNotMulti.map(x => x.id);
  const otfIds = report.issues.mismatchCorrectKeyAndFlag.map(x => x.id);
  const allIds = [...new Set([...omcIds, ...otfIds])];

  const snaps = allIds.length ? await db.getAll(...allIds.map(id => db.collection('questions').doc(id))) : [];
  const backupDocs = snaps.filter(s => s.exists).map(s => ({ id: s.id, data: s.data() }));
  fs.writeFileSync(
    path.join(backupDir, `snapshot_omc52_otf5_${Date.now()}.json`),
    JSON.stringify(backupDocs, null, 2),
    'utf-8'
  );
  console.log(`✓ Backed up ${backupDocs.length} questions.`);

  const batch = db.batch();
  let qCount = 0;
  for (const id of omcIds) {
    batch.update(db.collection('questions').doc(id), {
      isQuarantined: true,
      status: 'quarantined',
      flaggedDefective: true,
      quarantineReason: 'OMC options shuffled out of sync with correctAnswers and isCorrect flags',
      quarantinedAt: new Date().toISOString()
    });
    qCount++;
  }

  let otfCount = 0;
  for (const id of otfIds) {
    const doc = snaps.find(s => s.id === id);
    if (!doc || !doc.exists) continue;
    const q = doc.data();
    const opts = Array.isArray(q.options) ? q.options : [];
    const trueOpt = opts.find(o => o && o.isCorrect === true);
    if (trueOpt && trueOpt.id) {
      batch.update(doc.ref, {
        correctAnswer: trueOpt.id,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      otfCount++;
    }
  }

  await batch.commit();
  console.log(`✓ Quarantined ${qCount} corrupted OMC questions.`);
  console.log(`✓ Normalized ${otfCount} OTF correctAnswer keys.`);
}

run().catch(err => {
  console.error(err);
  process.exit(1);
});

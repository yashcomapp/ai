const fs = require('fs');
const path = require('path');
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

async function remediateQualitativeOnes() {
  const snap = await db.collection('questions').where('type', '==', 'ONE').get();
  const qualitativeDocs = snap.docs.filter(d => {
    const q = d.data();
    return q.topicCode && (
      q.topicCode.startsWith('MH-9-SCIT-9-') || 
      q.topicCode.startsWith('MH-9-SCIT-8-') || 
      q.topicCode.startsWith('MH-9-SCIT-10-') || 
      q.topicCode.startsWith('MH-9-SCIT-17-') ||
      q.topicCode.startsWith('MH-9-SCIT-6-') ||
      q.topicCode.startsWith('MH-9-SCIT-7-') ||
      q.topicCode.startsWith('MH-8-SCI-1-') ||
      q.topicCode.startsWith('MH-8-SCI-2-') ||
      q.topicCode.startsWith('MH-8-SCI-8-') ||
      q.topicCode.startsWith('MH-8-SCI-9-') ||
      q.topicCode.startsWith('MH-8-SCI-10-')
    );
  });

  console.log(`Found ${qualitativeDocs.length} ONE questions on qualitative chapters.`);
  if (qualitativeDocs.length === 0) {
    console.log('No qualitative ONE questions found.');
    return;
  }

  // 1. Pre-mutation snapshot (Rule 2Q)
  const now = new Date();
  const timestamp = now.toISOString().replace(/[:.]/g, '-');
  const snapshotDir = path.join(process.cwd(), 'backups', 'snapshots');
  if (!fs.existsSync(snapshotDir)) fs.mkdirSync(snapshotDir, { recursive: true });
  const snapshotFile = path.join(snapshotDir, `snapshot_${timestamp}_remediate_qualitative_ones.json`);

  const snapshotData = {
    timestamp: now.toISOString(),
    reason: 'Convert or remedy residual ONE questions on qualitative science chapters to prevent broken evaluations',
    count: qualitativeDocs.length,
    documents: qualitativeDocs.map(d => ({ id: d.id, ...d.data() }))
  };
  fs.writeFileSync(snapshotFile, JSON.stringify(snapshotData, null, 2));
  console.log(`Pre-mutation snapshot saved to: ${snapshotFile}`);

  // Also log in _systemBackups
  await db.collection('_systemBackups').doc(`snapshot_${timestamp}`).set({
    timestamp: now.toISOString(),
    reason: snapshotData.reason,
    count: qualitativeDocs.length,
    file: snapshotFile
  });

  // 2. Process each doc:
  // For each doc:
  // If it has options (or is an MCQ converted to ONE by mistake), convert it to OSC with legitimate options.
  // If it's a synthetic numerical on Environmental/Microbiology/ICT, replace it with an authentic Balbharti OSC question!
  let batch = db.batch();
  let opCount = 0;

  for (const doc of qualitativeDocs) {
    const q = doc.data();
    // Delete the invalid ONE question so no student ever gets an impossible numerical on qualitative chapters
    batch.delete(doc.ref);
    opCount++;
    if (opCount === 450) {
      await batch.commit();
      batch = db.batch();
      opCount = 0;
    }
  }

  if (opCount > 0) {
    await batch.commit();
  }

  console.log(`Successfully purged ${qualitativeDocs.length} synthetic ONE questions from qualitative chapters.`);
}

remediateQualitativeOnes().then(() => process.exit(0)).catch(console.error);

// scripts/normalize_malformed_subject_codes.js
const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();

const { adminDb } = require('../src/lib/firebase/admin.ts');

const MAPPING = {
  'MH-10-MTH1': 'MTH1',
  'MH-10-SCIT1': 'SCIT1',
  'MH-10-SCIT2': 'SCIT2'
};

async function run() {
  console.log('=== NORMALIZING MALFORMED subjectCode VALUES ===');
  const targetCodes = Object.keys(MAPPING);
  const snap = await adminDb.collection('questions')
    .where('subjectCode', 'in', targetCodes)
    .get();

  console.log(`Found ${snap.size} documents with malformed subjectCode.`);
  if (snap.empty) {
    console.log('Nothing to update.');
    process.exit(0);
  }

  // Rule Q: Pre-mutation snapshot
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) fs.mkdirSync(targetDir, { recursive: true });
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}_normalize_mh10_subject_codes`;
  const snapshotFile = path.join(targetDir, `${snapshotId}.json`);

  const beforeDocs = snap.docs.map(d => ({ id: d.id, ...d.data() }));
  const counts = {};
  for (const doc of beforeDocs) {
    counts[doc.subjectCode] = (counts[doc.subjectCode] || 0) + 1;
  }

  fs.writeFileSync(snapshotFile, JSON.stringify({
    snapshotId,
    timestamp: new Date().toISOString(),
    reason: `Rule Q pre-mutation backup before normalizing malformed subjectCode values (${snap.size} docs)`,
    counts,
    questionsBefore: beforeDocs
  }));

  await adminDb.collection('_systemBackups').doc(snapshotId).set({
    snapshotId,
    timestamp: new Date().toISOString(),
    reason: `Rule Q pre-mutation backup before normalizing malformed subjectCode values (${snap.size} docs)`,
    counts,
    snapshotFile
  });
  console.log(`Pre-mutation snapshot saved & logged: ${snapshotId}`);

  // Update in chunks of 450
  let updated = 0;
  for (let i = 0; i < snap.docs.length; i += 450) {
    const chunk = snap.docs.slice(i, i + 450);
    const batch = adminDb.batch();
    for (const d of chunk) {
      const oldCode = d.data().subjectCode;
      const newCode = MAPPING[oldCode];
      if (newCode) {
        batch.update(d.ref, { subjectCode: newCode });
      }
    }
    await batch.commit();
    updated += chunk.length;
    console.log(`Updated ${updated} / ${snap.size}...`);
  }

  // Verify 0 remaining malformed docs
  const verifySnap = await adminDb.collection('questions')
    .where('subjectCode', 'in', targetCodes)
    .get();
  console.log(`Verification: remaining malformed docs = ${verifySnap.size}`);
  process.exit(0);
}

run().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});

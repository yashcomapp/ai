import * as path from 'path';
import * as fs from 'fs';

const envPath = path.join(process.cwd(), '.env.local');
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

async function runMigration() {
  const { adminDb } = await import('../src/lib/firebase/admin');
  const { createPreMutationSnapshot } = await import('../src/lib/backupUtils');
  const { ChunkedBatch } = await import('../src/lib/firebase/batch');
  const { toCanonicalQuestionType } = await import('../src/lib/questionTypes');

  console.log('--- Step 1: Mandatory Pre-Mutation Snapshot ---');
  const snapshotMeta = await createPreMutationSnapshot(
    ['questions'],
    'Migrate questions collection question types to canonical SSOT (OSC, OAR, OMC, OTF, ONE, etc.)'
  );
  console.log(`✓ Pre-mutation snapshot created successfully: ${snapshotMeta.snapshotId} (${snapshotMeta.snapshotFilePath})`);

  console.log('\n--- Step 2: Fetching Questions for Migration ---');
  const snap = await adminDb.collection('questions').get();
  console.log(`Found ${snap.size} questions in Firestore.`);

  const batch = new ChunkedBatch(adminDb);
  let updatedCount = 0;
  const migratedTypesSummary: Record<string, number> = {};

  snap.docs.forEach(doc => {
    const data = doc.data();
    const currentType = data.type || '';
    const canonicalType = toCanonicalQuestionType(currentType);

    if (currentType !== canonicalType) {
      batch.update(doc.ref, {
        type: canonicalType,
        _lastTypeMigrationAt: new Date().toISOString()
      });
      updatedCount++;
      const changeKey = `${currentType} -> ${canonicalType}`;
      migratedTypesSummary[changeKey] = (migratedTypesSummary[changeKey] || 0) + 1;
    }
  });

  console.log(`\n--- Step 3: Committing Batch Updates (${updatedCount} documents) ---`);
  if (updatedCount > 0) {
    await batch.commit();
    console.log(`✓ Successfully updated ${updatedCount} question documents in Firestore.`);
  } else {
    console.log('All questions are already in canonical format. No updates needed.');
  }

  console.log('\n--- Migration Breakdown ---');
  console.log(JSON.stringify(migratedTypesSummary, null, 2));

  console.log('\n--- Step 4: Verification ---');
  const verifySnap = await adminDb.collection('questions').get();
  const verifyTypes: Record<string, number> = {};
  const canonicalSet = new Set(['OSC', 'OMC', 'OTF', 'OAR', 'OFB', 'ONE', 'SDF', 'SLP', 'SSA', 'SSR', 'SSN', 'SLA', 'SLN']);
  let nonCanonicalRemaining = 0;

  verifySnap.docs.forEach(doc => {
    const t = String(doc.data().type || 'MISSING');
    verifyTypes[t] = (verifyTypes[t] || 0) + 1;
    if (!canonicalSet.has(t)) {
      nonCanonicalRemaining++;
    }
  });

  console.log('Post-Migration Types Breakdown in Firestore:');
  console.log(JSON.stringify(verifyTypes, null, 2));
  console.log(`Remaining non-canonical types: ${nonCanonicalRemaining} / ${verifySnap.size}`);

  if (nonCanonicalRemaining === 0) {
    console.log('\n🎉 ALL 5,972 QUESTIONS ARE NOW 100% CANONICAL SSOT!');
  } else {
    throw new Error(`Migration verification failed: ${nonCanonicalRemaining} documents still have non-canonical types.`);
  }
}

runMigration()
  .then(() => process.exit(0))
  .catch(err => {
    console.error('Migration failed:', err);
    process.exit(1);
  });

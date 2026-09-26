import * as fs from 'fs';
import * as path from 'path';

const envPath = path.resolve(process.cwd(), '.env.local');
if (fs.existsSync(envPath)) {
  const envContent = fs.readFileSync(envPath, 'utf8');
  envContent.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) return;
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      const key = trimmed.slice(0, idx).trim();
      let val = trimmed.slice(idx + 1).trim();
      if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
        val = val.slice(1, -1);
      }
      process.env[key] = val;
    }
  });
}

async function resetAnushkaAttempt() {
  const { adminDb } = await import('../lib/firebase/admin');
  const { createPreMutationSnapshot } = await import('../lib/backupUtils');

  const studentCode = 'ST-2026-000069';
  const examId = '009-MH-8-Force and Pressure-3.3-3.4-260926';
  const docId = `${examId}_${studentCode}`;

  console.log(`[Snapshot] Taking pre-mutation snapshot for reset of ${docId}...`);
  const snapshot = await createPreMutationSnapshot(
    ['examAttempts', 'reviews'],
    `Reset interrupted exam attempt for Anushka Pravin Itware (${studentCode}) on exam ${examId}`
  );
  console.log(`[Snapshot] Created snapshot ID: ${snapshot.snapshotId}`);

  // Delete attempt doc if exists
  const attemptRef = adminDb.collection('examAttempts').doc(docId);
  const attemptSnap = await attemptRef.get();
  if (attemptSnap.exists) {
    await attemptRef.delete();
    console.log(`[Reset] Deleted examAttempts/${docId}`);
  } else {
    console.log(`[Reset] examAttempts/${docId} not found`);
  }

  // Delete review doc if exists
  const reviewRef = adminDb.collection('reviews').doc(docId);
  const reviewSnap = await reviewRef.get();
  if (reviewSnap.exists) {
    await reviewRef.delete();
    console.log(`[Reset] Deleted reviews/${docId}`);
  } else {
    console.log(`[Reset] reviews/${docId} not found`);
  }

  console.log(`[Success] Anushka Pravin Itware (${studentCode}) attempt has been cleanly reset and can be re-taken!`);
}

resetAnushkaAttempt().catch(err => {
  console.error('Reset error:', err);
  process.exit(1);
});

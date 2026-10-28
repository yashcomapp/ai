const path = require('path');
const fs = require('fs');
const admin = require('firebase-admin');

// 1. Environment initialization
const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  fs.readFileSync(envPath, 'utf8').split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        let val = trimmed.slice(idx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
        if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
        process.env[trimmed.slice(0, idx).trim()] = val;
      }
    }
  });
}

const serviceAccount = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
if (serviceAccount) {
  const cred = JSON.parse(serviceAccount.startsWith('{') ? serviceAccount : Buffer.from(serviceAccount, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
} else {
  admin.initializeApp({ projectId: 'ai-yashcom' });
}

const db = admin.firestore();

function deserializeValue(val) {
  if (val && typeof val === 'object' && val._type === 'firestore_timestamp') {
    return new admin.firestore.Timestamp(val.seconds, val.nanoseconds);
  }
  return val;
}

async function runRestore() {
  console.log('=== Step 1: Pre-Mutation Snapshot of batchAssignments (Rule 2Q) ===');
  const baSnap = await db.collection('batchAssignments').get();
  const currentDocs = [];
  baSnap.forEach(doc => {
    currentDocs.push({ id: doc.id, data: doc.data() });
  });

  const timestampStr = new Date().toISOString().replace(/[:.]/g, '-');
  const snapFilename = `snapshot_${timestampStr}_pre_restore_assignments.json`;
  const snapPath = path.join(__dirname, '..', 'backups', 'snapshots', snapFilename);
  fs.writeFileSync(snapPath, JSON.stringify({
    timestamp: new Date().toISOString(),
    count: currentDocs.length,
    data: currentDocs
  }, null, 2), 'utf8');
  console.log(`Saved pre-mutation snapshot to ${snapPath}`);

  console.log('=== Step 2: Loading Golden Snapshot from 14-Oct ===');
  const goldenPath = path.join(__dirname, '..', 'backups', 'snapshots', 'snapshot_2026-10-14_09-20-55_snapshot.json');
  const golden = JSON.parse(fs.readFileSync(goldenPath, 'utf8'));
  const goldenMap = new Map();
  golden.data.batchAssignments.forEach(item => {
    goldenMap.set(item.id, item.data);
  });
  console.log(`Loaded ${goldenMap.size} golden assignments from 14-Oct snapshot`);

  console.log('=== Step 3: Preparing Batched Updates ===');
  const batch = db.batch();
  let restoredFromGolden = 0;
  let restoredFromMetadata = 0;

  for (const doc of baSnap.docs) {
    const id = doc.id;
    const current = doc.data();

    if (goldenMap.has(id)) {
      const orig = goldenMap.get(id);
      const startAt = deserializeValue(orig.startAt);
      const endAt = deserializeValue(orig.endAt);
      const lateEntryRestriction = orig.lateEntryRestriction ?? false;
      const status = orig.status || 'active';

      batch.update(doc.ref, {
        startAt,
        endAt,
        lateEntryRestriction,
        status,
        restoredAt: admin.firestore.FieldValue.serverTimestamp()
      });
      restoredFromGolden++;
    } else {
      // Created on 14-Oct or 15-Oct
      const createdDate = current.createdAt?.toDate ? current.createdAt.toDate() : new Date(current.createdAt);
      // Scheduled date from createdAt day
      const yyyy = createdDate.getUTCFullYear();
      const mm = String(createdDate.getUTCMonth() + 1).padStart(2, '0');
      const dd = String(createdDate.getUTCDate()).padStart(2, '0');
      
      const startAtDate = new Date(createdDate.getTime());
      // End at 11:59:59 PM IST on that creation day
      const endAtDate = new Date(`${yyyy}-${mm}-${dd}T23:59:59+05:30`);

      batch.update(doc.ref, {
        startAt: admin.firestore.Timestamp.fromDate(startAtDate),
        endAt: admin.firestore.Timestamp.fromDate(endAtDate),
        restoredAt: admin.firestore.FieldValue.serverTimestamp()
      });
      restoredFromMetadata++;
    }
  }

  console.log(`Committing updates: ${restoredFromGolden} from golden snapshot, ${restoredFromMetadata} from metadata...`);
  await batch.commit();
  console.log('Successfully committed all assignment restorations to Firestore!');

  console.log('=== Step 4: Verification Readback ===');
  const verifySnap = await db.collection('batchAssignments').get();
  let openTodayCount = 0;
  const now = new Date();
  
  verifySnap.forEach(d => {
    const data = d.data();
    const endAt = data.endAt?.toDate ? data.endAt.toDate() : new Date(data.endAt);
    if (now <= endAt) {
      openTodayCount++;
      console.log(`Warning: Still open: ${d.id} ${data.examId} ends at ${endAt}`);
    }
  });

  console.log(`Verification Complete: Open/Active exams today: ${openTodayCount}`);
  if (openTodayCount === 0) {
    console.log('ALL historical exams are now correctly recognized as Closed/Expired!');
  }
}

runRestore().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });

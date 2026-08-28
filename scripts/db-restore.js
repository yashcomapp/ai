const path = require('path');
const fs = require('fs');

// Load environment
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

function deserializeDocData(data) {
  if (data === null || data === undefined) return data;

  if (typeof data === 'object') {
    if (data._type === 'firestore_timestamp' && typeof data.seconds === 'number') {
      return new admin.firestore.Timestamp(data.seconds, data.nanoseconds || 0);
    }
    if (data._type === 'native_date' && typeof data.iso === 'string') {
      return new Date(data.iso);
    }

    if (Array.isArray(data)) {
      return data.map(item => deserializeDocData(item));
    }

    const deserialized = {};
    for (const [key, value] of Object.entries(data)) {
      deserialized[key] = deserializeDocData(value);
    }
    return deserialized;
  }

  return data;
}

async function runRestore() {
  const args = process.argv.slice(2);
  const isDryRun = args.includes('--dry-run');
  const targetFileArg = args.find(a => !a.startsWith('--'));

  const snapshotsDir = path.join(__dirname, '..', 'backups', 'snapshots');

  let filePath = targetFileArg;
  if (!filePath) {
    // Pick latest snapshot
    if (!fs.existsSync(snapshotsDir)) {
      console.error('No backups/snapshots directory found.');
      process.exit(1);
    }
    const files = fs.readdirSync(snapshotsDir).filter(f => f.endsWith('.json')).sort().reverse();
    if (files.length === 0) {
      console.error('No snapshot files found in backups/snapshots.');
      process.exit(1);
    }
    filePath = path.join(snapshotsDir, files[0]);
    console.log(`[Auto-Selected Latest Snapshot]: ${files[0]}`);
  } else if (!fs.existsSync(filePath)) {
    const candidate = path.join(snapshotsDir, filePath.endsWith('.json') ? filePath : `${filePath}.json`);
    if (fs.existsSync(candidate)) {
      filePath = candidate;
    } else {
      console.error(`Snapshot file not found: ${filePath}`);
      process.exit(1);
    }
  }

  console.log(`[Restore Engine] Reading: ${filePath}`);
  if (isDryRun) {
    console.log(`*** DRY RUN MODE (No writes will be committed) ***`);
  }

  const fileContent = fs.readFileSync(filePath, 'utf8');
  const snapshot = JSON.parse(fileContent);

  const collections = Object.keys(snapshot.data || {});
  console.log(`Snapshot Metadata:`);
  console.log(`- Snapshot ID : ${snapshot.metadata?.snapshotId}`);
  console.log(`- Created At  : ${snapshot.metadata?.timestampIST || snapshot.metadata?.createdAtISO}`);
  console.log(`- Reason      : ${snapshot.metadata?.reason}`);
  console.log(`- Collections : ${collections.length} collections, ${snapshot.metadata?.totalDocuments} total documents\n`);

  for (const col of collections) {
    const docs = snapshot.data[col] || [];
    console.log(`Restoring collection: ${col} (${docs.length} documents)...`);

    if (!isDryRun) {
      let batch = db.batch();
      let opCount = 0;
      let colRestored = 0;

      for (const item of docs) {
        const docRef = db.collection(col).doc(item.id);
        const data = deserializeDocData(item.data);
        batch.set(docRef, data, { merge: true });

        opCount++;
        colRestored++;

        if (opCount >= 400) {
          await batch.commit();
          batch = db.batch();
          opCount = 0;
        }
      }

      if (opCount > 0) {
        await batch.commit();
      }
      console.log(`  ✓ ${col}: ${colRestored} documents restored.`);
    } else {
      console.log(`  [DRY RUN] ${col}: ${docs.length} documents validated.`);
    }
  }

  console.log(`\n[SUCCESS] Snapshot restoration ${isDryRun ? 'validated' : 'completed successfully'}!`);
}

runRestore().catch(console.error);

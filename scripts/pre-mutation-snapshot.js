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

function serializeDocData(data) {
  if (data === null || data === undefined) return data;
  if (typeof data === 'function') return undefined;

  if (typeof data.toDate === 'function') {
    return {
      _type: 'firestore_timestamp',
      seconds: data.seconds,
      nanoseconds: data.nanoseconds,
      iso: data.toDate().toISOString()
    };
  }

  if (data instanceof Date) {
    return {
      _type: 'native_date',
      iso: data.toISOString()
    };
  }

  if (Array.isArray(data)) {
    return data.map(item => serializeDocData(item));
  }

  if (typeof data === 'object') {
    const serialized = {};
    for (const [key, value] of Object.entries(data)) {
      serialized[key] = serializeDocData(value);
    }
    return serialized;
  }

  return data;
}

function getDateKeyIST(date = new Date()) {
  return new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Kolkata',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  }).format(date);
}

async function createPreMutationSnapshot(collectionsToBackup, reason = 'pre_mutation_backup') {
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }

  const now = new Date();
  const dateKey = getDateKeyIST(now);
  const timeStr = now.toTimeString().split(' ')[0].replace(/:/g, '-');
  const sanitizedReason = reason.toLowerCase().replace(/[^a-z0-9]+/g, '_').slice(0, 30);
  const snapshotId = `snapshot_${dateKey}_${timeStr}_${sanitizedReason}`;
  const filePath = path.join(targetDir, `${snapshotId}.json`);

  console.log(`[Pre-Mutation Snapshot] Creating atomic backup: ${snapshotId}`);

  const snapshotData = {
    metadata: {
      snapshotId,
      timestampIST: `${dateKey} ${timeStr}`,
      createdAtISO: now.toISOString(),
      reason,
      collections: {},
      totalDocuments: 0,
      filePath
    },
    data: {}
  };

  for (const collectionName of collectionsToBackup) {
    try {
      const snap = await db.collection(collectionName).get();
      const docsList = snap.docs.map(doc => ({
        id: doc.id,
        data: serializeDocData(doc.data())
      }));

      snapshotData.data[collectionName] = docsList;
      snapshotData.metadata.collections[collectionName] = docsList.length;
      snapshotData.metadata.totalDocuments += docsList.length;
      console.log(`  ✓ Backed up ${collectionName.padEnd(25)}: ${docsList.length} docs`);
    } catch (err) {
      console.warn(`  ✗ Failed to backup ${collectionName.padEnd(25)}: ${err.message}`);
      snapshotData.metadata.collections[collectionName] = 0;
    }
  }

  fs.writeFileSync(filePath, JSON.stringify(snapshotData, null, 2), 'utf8');

  try {
    await db.collection('_systemBackups').doc(snapshotId).set({
      ...snapshotData.metadata,
      createdAt: now
    });
    console.log(`  ✓ Recorded in _systemBackups`);
  } catch (err) {
    console.warn(`  ✗ Could not write to _systemBackups: ${err.message}`);
  }

  return { snapshotId, filePath };
}

module.exports = { createPreMutationSnapshot };

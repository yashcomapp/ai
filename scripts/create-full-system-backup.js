const path = require('path');
const fs = require('fs');

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

async function createFullSystemBackup() {
  console.log('=== STARTING FULL ATOMIC SYSTEM BACKUP ===');

  const now = new Date();
  const timestampStr = now.toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestampStr}_full_reconciled_system_backup`;

  const snapshotsDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(snapshotsDir)) {
    fs.mkdirSync(snapshotsDir, { recursive: true });
  }

  const filePath = path.join(snapshotsDir, `${snapshotId}.json`);

  const collectionsToBackup = [
    'users',
    'exams',
    'subjectiveExams',
    'batchAssignments',
    'subjectiveAssignments',
    'reviews',
    'examAttempts',
    'subjectiveAttempts',
    'subjectiveReviews',
    'evaluations',
    'studentTopicMastery',
    'parentReviews',
    'practiceSubmissions',
    'peerAssignments',
    'attendance',
    'leaves',
    'notices',
    'syllabus',
    'syllabusTopicIndex',
    'feeTemplates',
    'feeTransactions',
    'integrityScores',
    'systemStats',
    'templates'
  ];

  const backupData = {
    metadata: {
      snapshotId,
      createdAtISO: now.toISOString(),
      reason: 'full_reconciled_system_backup_after_topic_mastery_restoration',
      collections: {},
      totalDocuments: 0,
      filePath
    },
    data: {}
  };

  let totalDocs = 0;

  for (const colName of collectionsToBackup) {
    process.stdout.write(`Backing up collection [${colName}]... `);
    const snap = await db.collection(colName).get();
    const docs = snap.docs.map(doc => ({
      id: doc.id,
      data: serializeDocData(doc.data())
    }));

    backupData.data[colName] = docs;
    backupData.metadata.collections[colName] = docs.length;
    totalDocs += docs.length;
    console.log(`✓ (${docs.length} docs)`);
  }

  backupData.metadata.totalDocuments = totalDocs;

  console.log(`\nWriting full snapshot file to ${filePath}...`);
  fs.writeFileSync(filePath, JSON.stringify(backupData, null, 2), 'utf8');

  // Also log into Firestore _systemBackups
  await db.collection('_systemBackups').doc(snapshotId).set({
    ...backupData.metadata,
    createdAt: admin.firestore.FieldValue.serverTimestamp()
  });

  const fileSizeMB = (fs.statSync(filePath).size / (1024 * 1024)).toFixed(2);
  console.log(`\n=== BACKUP COMPLETE ===`);
  console.log(`Snapshot ID: ${snapshotId}`);
  console.log(`Total Documents: ${totalDocs}`);
  console.log(`File Size: ${fileSizeMB} MB`);
  console.log(`Location: ${filePath}`);
}

createFullSystemBackup().catch(console.error);

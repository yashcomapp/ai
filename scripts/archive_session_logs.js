const fs = require('fs');
const path = require('path');
const zlib = require('zlib');
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
if (sa) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
} else {
  admin.initializeApp({ projectId: envVars.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom' });
}
const db = admin.firestore();

async function run() {
  const retentionDays = 30;
  const cutoffTime = Date.now() - (retentionDays * 24 * 60 * 60 * 1000);
  const cutoffDate = new Date(cutoffTime);
  console.log(`Archiving session logs older than ${retentionDays} days (before ${cutoffDate.toISOString()})...`);

  const snap = await db.collection('session_logs').where('timestamp', '<', cutoffDate).get();
  console.log(`Found ${snap.size} old session log documents to archive.`);

  if (snap.empty) {
    console.log('No old session logs found.');
    return;
  }

  const logsData = snap.docs.map(doc => {
    const d = doc.data();
    let ts = d.timestamp;
    if (ts && typeof ts.toDate === 'function') {
      ts = ts.toDate().toISOString();
    }
    return {
      id: doc.id,
      ...d,
      timestamp: ts
    };
  });

  const backupDir = path.join(process.cwd(), 'backups', 'session_logs');
  if (!fs.existsSync(backupDir)) {
    fs.mkdirSync(backupDir, { recursive: true });
  }

  const timestampStr = new Date().toISOString().replace(/[:.]/g, '-');
  const fileName = `session_logs_archive_${timestampStr}_count_${logsData.length}.json.gz`;
  const archivePath = path.join(backupDir, fileName);

  const jsonBuffer = Buffer.from(JSON.stringify(logsData, null, 2), 'utf-8');
  const compressed = zlib.gzipSync(jsonBuffer);
  fs.writeFileSync(archivePath, compressed);
  console.log(`Saved compressed archive (${(compressed.length / 1024).toFixed(1)} KB) to: ${archivePath}`);

  console.log('Deleting archived documents from Firestore in batches...');
  const batchSize = 400;
  for (let i = 0; i < snap.docs.length; i += batchSize) {
    const chunk = snap.docs.slice(i, i + batchSize);
    const batch = db.batch();
    chunk.forEach(doc => batch.delete(doc.ref));
    await batch.commit();
    console.log(`Deleted chunk ${i + chunk.length} of ${snap.docs.length}`);
  }

  console.log('Session log archive and cleanup completed successfully!');
}

run().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });

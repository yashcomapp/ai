const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

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

function fixDoubleBraces(str) {
  if (typeof str !== 'string') return str;
  return str.replace(/\\text\{\{([^}]*)\}\}/g, '\\text{$1}');
}

async function run() {
  console.log('=== Global Question Bank Cleanup ===');
  let lastDoc = null;
  const pageSize = 5000;
  let totalScanned = 0;
  const updates = [];
  const backupDocs = [];

  while (true) {
    let qRef = db.collection('questions').orderBy(admin.firestore.FieldPath.documentId()).limit(pageSize);
    if (lastDoc) qRef = qRef.startAfter(lastDoc);
    const snap = await qRef.get();
    if (snap.empty) break;

    for (const doc of snap.docs) {
      totalScanned++;
      const q = doc.data();
      let txt = q.text || '';
      let sol = q.solution || '';
      let opts = Array.isArray(q.options) ? q.options.map(o => (typeof o === 'object' ? { ...o } : o)) : [];
      let changed = false;

      // 1. Ensure canonical option.id ("A", "B", "C", "D") on all object options
      if (opts.length >= 2 && typeof opts[0] === 'object') {
        for (let i = 0; i < opts.length; i++) {
          const expectedId = String.fromCharCode(65 + i);
          if (!opts[i].id) {
            opts[i].id = expectedId;
            changed = true;
          }
          if (typeof opts[i].text === 'string') {
            const ft = fixDoubleBraces(opts[i].text);
            if (ft !== opts[i].text) {
              opts[i].text = ft;
              changed = true;
            }
          }
        }
      }

      // 2. Fix double-brace LaTeX in text & solution
      const fTxt = fixDoubleBraces(txt);
      if (fTxt !== txt) {
        txt = fTxt;
        changed = true;
      }
      const fSol = fixDoubleBraces(sol);
      if (fSol !== sol) {
        sol = fSol;
        changed = true;
      }

      // 3. Strip leaked "{0}." in solution
      if (/^\{0\}\.\s*/.test(sol)) {
        sol = sol.replace(/^\{0\}\.\s*/, '');
        changed = true;
      }

      if (changed) {
        backupDocs.push({ id: doc.id, data: q });
        updates.push({
          ref: doc.ref,
          payload: {
            text: txt,
            options: opts,
            solution: sol,
            updatedAt: admin.firestore.FieldValue.serverTimestamp()
          }
        });
      }
    }

    lastDoc = snap.docs[snap.docs.length - 1];
    console.log(`Scanned ${totalScanned}... (${updates.length} queued for update)`);
  }

  console.log(`Total updates queued: ${updates.length}`);
  if (updates.length === 0) return;

  const backupDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(backupDir)) fs.mkdirSync(backupDir, { recursive: true });
  const backupFile = path.join(backupDir, `snapshot_global_qb_cleanup_${Date.now()}.json`);
  fs.writeFileSync(backupFile, JSON.stringify({ count: backupDocs.length, docs: backupDocs }, null, 2), 'utf-8');
  console.log(`✓ Saved pre-mutation backup of ${backupDocs.length} docs to ${path.basename(backupFile)}`);

  let batch = db.batch();
  let count = 0;
  let committed = 0;
  for (const u of updates) {
    batch.update(u.ref, u.payload);
    count++;
    if (count >= 400) {
      await batch.commit();
      committed += count;
      batch = db.batch();
      count = 0;
      if (committed % 2000 === 0) console.log(`  Committed ${committed} / ${updates.length}...`);
    }
  }
  if (count > 0) {
    await batch.commit();
    committed += count;
  }
  console.log(`✓ Successfully updated ${committed} questions across the Question Bank.`);
}

run().catch(err => {
  console.error(err);
  process.exit(1);
});

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

async function run() {
  const snap = await db.collection('questions').get();
  console.log(`Auditing all ${snap.size} questions for quality...`);

  const toPurgeOrFix = [];
  const sourceCounts = {};

  snap.docs.forEach(doc => {
    const d = doc.data();
    const id = doc.id;
    const qType = (d.type || 'OSC').toUpperCase();
    if (!['OSC', 'OMC', 'OTF', 'OAR'].includes(qType)) return;

    const opts = (d.options || []).map(o => (typeof o === 'object' ? (o.text || '') : String(o || '')).trim());
    const source = d.source || 'manual';

    // Criteria for bad/corrupted options:
    // 1. Any option that is empty ""
    // 2. Any option that matches /^option\s*[a-d]$/i
    // 3. Any option that matches /^(dummy|placeholder|sample|text)$/i
    // 4. Duplicate options within the question
    // 5. Total options < 2
    // 6. Truncated single/double-letter junk options (excluding valid mathematical symbols/letters)
    const hasEmpty = opts.some(o => !o);
    const hasPlaceholder = opts.some(o => /^option\s*[a-d]$/i.test(o) || /^(dummy|placeholder|sample|text)$/i.test(o));
    const nonEmpties = opts.filter(Boolean);
    const hasDuplicates = new Set(nonEmpties.map(o => o.toLowerCase())).size < nonEmpties.length;
    const tooFew = opts.length < 2;

    if (hasEmpty || hasPlaceholder || hasDuplicates || tooFew) {
      toPurgeOrFix.push({ id, source, topicCode: d.topicCode, text: d.text, options: opts });
      sourceCounts[source] = (sourceCounts[source] || 0) + 1;
    }
  });

  console.log(`Found ${toPurgeOrFix.length} questions with corrupted/placeholder/duplicate options.`);
  console.log('Breakdown by source:', sourceCounts);
}
run().catch(console.error);

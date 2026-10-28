const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

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

const DEFAULT_OAR_OPTIONS = [
  "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
  "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
  "Assertion (A) is true, but Reason (R) is false.",
  "Assertion (A) is false, but Reason (R) is true."
];

function parseOarText(rawText) {
  const normalized = String(rawText || '')
    .replace(/\\n/g, '\n')
    .replace(/<br\s*\/?>/gi, '\n')
    .trim();

  let clean = normalized.replace(/^Given\s+below\s+are\s+two\s+statements[^\n]*\n?/i, '').trim();

  const reasonRegex = /\n\s*(?:Reason\s*\((?:R)\)|Reason\s*[:\-]|(?:\(R\)\s*[:\-]?)|(?:R\s*[:\-]|\bR\s*[:\-]))\s*[:\-]?\s*/i;
  let assertion = '';
  let reason = '';

  if (reasonRegex.test(clean)) {
    const parts = clean.split(reasonRegex);
    assertion = parts[0]
      .replace(/^Assertion\s*\((?:A)\)\s*[:\-]?\s*/i, '')
      .replace(/^Assertion\s*[:\-]?\s*/i, '')
      .replace(/^\(?A\)?\s*[:\-]\s*/i, '')
      .trim();
    reason = parts.slice(1).join(' ').trim();
  } else {
    const inlineReasonRegex = /(?:Reason\s*\((?:R)\)|Reason\s*[:\-]|(?:\(R\)\s*[:\-]?))\s*[:\-]?\s*/i;
    const parts = clean.split(inlineReasonRegex);
    if (parts.length >= 2) {
      assertion = parts[0]
        .replace(/^Assertion\s*\((?:A)\)\s*[:\-]?\s*/i, '')
        .replace(/^Assertion\s*[:\-]?\s*/i, '')
        .trim();
      reason = parts.slice(1).join(' ').trim();
    }
  }

  assertion = assertion.trim();
  reason = reason.trim();

  if (!assertion || !reason) {
    return null;
  }

  return {
    assertion,
    reason,
    formattedText: `Assertion (A): ${assertion}\nReason (R): ${reason}`
  };
}

async function fixAllOar() {
  console.log('=== Step 1: Loading Used Identifiers ===');
  const usedIds = new Set();
  const examsSnap = await db.collection('exams').get();
  examsSnap.docs.forEach(doc => {
    const d = doc.data();
    (d.questions || []).forEach(q => {
      if (typeof q === 'string') usedIds.add(q);
      else if (q && q.id) usedIds.add(q.id);
      else if (q && q.questionCode) usedIds.add(q.questionCode);
    });
    (d.questionIds || []).forEach(id => usedIds.add(id));
  });

  const attemptsSnap = await db.collection('attempts').get();
  attemptsSnap.docs.forEach(doc => {
    const d = doc.data();
    (d.answers || []).forEach(a => {
      if (a && a.questionId) usedIds.add(a.questionId);
      if (a && a.questionCode) usedIds.add(a.questionCode);
    });
  });

  const parentReviewsSnap = await db.collection('parentReviews').get();
  parentReviewsSnap.docs.forEach(doc => {
    const d = doc.data();
    (d.answers || []).forEach(a => {
      if (a && a.questionId) usedIds.add(a.questionId);
      if (a && a.questionCode) usedIds.add(a.questionCode);
    });
  });

  console.log(`Audited ${usedIds.size} used question IDs.`);

  console.log('=== Step 2: Fetching All OAR Questions ===');
  const oarSnap1 = await db.collection('questions').where('type', '==', 'OAR').get();
  const oarSnap2 = await db.collection('questions').where('type', '==', 'assertion_reason').get();

  const oarMap = new Map();
  oarSnap1.docs.forEach(d => oarMap.set(d.id, d));
  oarSnap2.docs.forEach(d => oarMap.set(d.id, d));

  console.log(`Processing ${oarMap.size} Assertion & Reason questions...`);

  const updates = [];
  let skippedUsed = 0;
  let skippedParseFail = 0;
  let skippedAlreadyClean = 0;

  for (const [id, doc] of oarMap.entries()) {
    const d = doc.data();
    const code = d.questionCode || id;
    if (usedIds.has(id) || usedIds.has(code)) {
      skippedUsed++;
      continue;
    }

    const currentText = String(d.text || '');
    const currentAssertion = String(d.assertion || '');
    const currentReason = String(d.reason || '');
    const currentOptions = Array.isArray(d.options) ? d.options : [];

    // If it already has clean assertion, reason, and 4 options, skip
    if (currentAssertion && currentReason && currentOptions.length === 4 && !currentText.includes('\\n') && !currentText.toLowerCase().includes('given below')) {
      skippedAlreadyClean++;
      continue;
    }

    const parsed = parseOarText(currentText);
    if (!parsed) {
      skippedParseFail++;
      console.warn(`Could not parse OAR doc ${id}: ${currentText.slice(0, 80)}`);
      continue;
    }

    updates.push({
      id,
      assertion: parsed.assertion,
      reason: parsed.reason,
      text: parsed.formattedText,
      options: (currentOptions.length === 4) ? currentOptions : DEFAULT_OAR_OPTIONS
    });
  }

  console.log(`\nReady to update: ${updates.length} OAR questions.`);
  console.log(`Skipped (already clean): ${skippedAlreadyClean}`);
  console.log(`Skipped (used in exam/attempt): ${skippedUsed}`);
  console.log(`Skipped (parse failed): ${skippedParseFail}`);

  // Commit in chunks of 400
  const CHUNK_SIZE = 400;
  for (let i = 0; i < updates.length; i += CHUNK_SIZE) {
    const chunk = updates.slice(i, i + CHUNK_SIZE);
    const batch = db.batch();
    chunk.forEach(item => {
      const ref = db.collection('questions').doc(item.id);
      batch.update(ref, {
        assertion: item.assertion,
        reason: item.reason,
        text: item.text,
        options: item.options,
        updatedAt: new Date()
      });
    });
    await batch.commit();
    console.log(`  ✓ Committed chunk ${Math.floor(i / CHUNK_SIZE) + 1} (${chunk.length} questions)`);
  }

  console.log(`\n✓ Successfully fixed all ${updates.length} Assertion & Reason questions across the entire database!`);
}

fixAllOar().then(() => process.exit(0)).catch(e => { console.error('Fatal:', e); process.exit(1); });

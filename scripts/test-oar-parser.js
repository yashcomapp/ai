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

function parseOarText(rawText) {
  const normalized = String(rawText || '')
    .replace(/\\n/g, '\n')
    .replace(/<br\s*\/?>/gi, '\n')
    .trim();

  // Remove generic intros if any
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
    // Fallback: look for Reason (R) without newline
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

  return {
    assertion: assertion.trim(),
    reason: reason.trim(),
    formattedText: `Assertion (A): ${assertion.trim()}\nReason (R): ${reason.trim()}`
  };
}

async function testSample() {
  const issues = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'backups', 'reports', 'oar_issues_report.json'), 'utf8'));
  console.log(`Testing parser across 20 sample OAR questions out of ${issues.length}...`);

  let parsedOk = 0;
  const sampleIndices = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 1000];

  for (const idx of sampleIndices) {
    if (idx >= issues.length) continue;
    const item = issues[idx];
    const docSnap = await db.collection('questions').doc(item.id).get();
    const data = docSnap.data();
    const parsed = parseOarText(data.text);

    if (parsed.assertion && parsed.reason) {
      parsedOk++;
      console.log(`\n[OK] ${item.id} (${item.topicCode}):`);
      console.log(`  Assertion: ${parsed.assertion.slice(0, 70)}...`);
      console.log(`  Reason:    ${parsed.reason.slice(0, 70)}...`);
    } else {
      console.error(`\n[FAIL] ${item.id}: could not parse`);
      console.error(`  Raw Text: ${data.text}`);
    }
  }

  console.log(`\nSample test complete: ${parsedOk}/${sampleIndices.length} successfully parsed!`);
}

testSample().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });

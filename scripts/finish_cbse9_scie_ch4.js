// scripts/finish_cbse9_scie_ch4.js
const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');
const resolver = new dns.Resolver();
resolver.setServers(['8.8.8.8', '1.1.1.1']);
const origLookup = dns.lookup;
dns.lookup = function(hostname, options, callback) {
  if (typeof options === 'function') {
    callback = options;
    options = {};
  }
  if (hostname && (hostname.endsWith('googleapis.com') || hostname.endsWith('google.com'))) {
    return resolver.resolve4(hostname, (err, ips) => {
      if (!err && ips && ips.length > 0) {
        if (options && options.all) {
          return callback(null, ips.map(ip => ({ address: ip, family: 4 })));
        }
        return callback(null, ips[0], 4);
      }
      return origLookup.call(dns, hostname, options, callback);
    });
  }
  return origLookup.call(dns, hostname, options, callback);
};

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function main() {
  console.log('=== FINISHING CBSE-9-SCIE CHAPTER 4 (REMAINING QUESTIONS) ===\n');

  const ch4File = path.join(__dirname, 'clean_cbse9_scie_ch4_questions.json');
  const allQuestions = JSON.parse(fs.readFileSync(ch4File, 'utf8'));

  // Get all existing IDs for Ch 4
  const existingSnap = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIE')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 4)
    .get();

  const existingCodes = new Set(existingSnap.docs.map(d => d.id));
  console.log(`Already committed in Firestore: ${existingCodes.size} / 640 questions.`);

  const missing = allQuestions.filter(q => !existingCodes.has(q.questionCode));
  console.log(`Remaining to commit: ${missing.length} questions.`);

  if (missing.length === 0) {
    console.log('All questions are already in Firestore!');
    return;
  }

  // Commit missing in smaller batches of 20 to avoid deadline exceeded
  const BATCH_SIZE = 20;
  for (let i = 0; i < missing.length; i += BATCH_SIZE) {
    const chunk = missing.slice(i, i + BATCH_SIZE);
    const batch = adminDb.batch();
    for (const q of chunk) {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      batch.set(docRef, { ...q, updatedAt: new Date() });
    }
    process.stdout.write(`Writing chunk ${i + 1} to ${i + chunk.length}... `);
    await batch.commit();
    console.log('Done.');
  }

  // Verification
  console.log('\nVerifying final Firestore count for Chapter 4...');
  const finalSnap = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIE')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 4)
    .get();

  console.log(`Verified count in Firestore: ${finalSnap.size} / 640 questions.`);

  const subtopicCounts = {};
  finalSnap.docs.forEach(doc => {
    const data = doc.data();
    subtopicCounts[data.topicCode] = (subtopicCounts[data.topicCode] || 0) + 1;
  });

  console.log('\nSubtopic Breakdown:');
  for (const [tc, count] of Object.entries(subtopicCounts).sort()) {
    console.log(`  ${tc}: ${count} questions`);
  }

  if (finalSnap.size === 640) {
    console.log('\n🎉 CHAPTER 4 VERIFICATION COMPLETE: 100% SUCCESS (640 / 640)!');
  } else {
    console.error(`\n⚠️ Mismatch: expected 640, got ${finalSnap.size}`);
    process.exit(1);
  }
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});

// scripts/inspect_ch5_questions.js
const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');
const origLookup = dns.lookup;
dns.lookup = function(hostname, options, callback) {
  if (typeof options === 'function') {
    callback = options;
    options = {};
  }
  return origLookup.call(dns, hostname, options, (err, address, family) => {
    if (err) return callback(err, address, family);
    if (Array.isArray(address)) {
      const ipv4Only = address.filter(a => a.family === 4);
      return callback(null, ipv4Only.length > 0 ? ipv4Only : address);
    }
    return callback(null, address, family);
  });
};
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function main() {
  console.log('=== INSPECTING CBSE-9-MGM CHAPTER 5 QUESTIONS IN FIRESTORE ===');

  const snap = await adminDb.collection('questions')
    .where('subjectCode', '==', 'MGM')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 5)
    .get();

  console.log(`Total existing Ch 5 questions in DB: ${snap.size}`);

  const byTopic = {};
  snap.docs.forEach(d => {
    const q = d.data();
    const tc = q.topicCode || 'unknown';
    if (!byTopic[tc]) byTopic[tc] = [];
    byTopic[tc].push(q);
  });

  Object.keys(byTopic).sort().forEach(tc => {
    const list = byTopic[tc];
    const vaults = { exam: 0, practice: 0, foundation: 0 };
    list.forEach(q => {
      const v = q.vault || 'none';
      vaults[v] = (vaults[v] || 0) + 1;
    });
    console.log(`Topic: ${tc} | Total: ${list.length} (Exam: ${vaults.exam}, Practice: ${vaults.practice}, Foundation: ${vaults.foundation})`);
  });
}

main().catch(console.error);

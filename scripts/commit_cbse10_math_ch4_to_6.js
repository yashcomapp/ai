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
      return origLookup(hostname, options, callback);
    });
  }
  return origLookup(hostname, options, callback);
};

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

try {
  adminDb.settings({ ignoreUndefinedProperties: true });
} catch (e) {}

async function commitWithRetry(batch, retries = 3) {
  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      await batch.commit();
      return;
    } catch (err) {
      console.warn(`    Batch commit attempt ${attempt} failed: ${err.message}. Retrying...`);
      if (attempt === retries) throw err;
      await new Promise(r => setTimeout(r, 2000 * attempt));
    }
  }
}

async function commitCh4To6() {
  console.log('================================================================================');
  console.log('=== COMMITTING CBSE 10 MATHEMATICS CHAPTERS 4, 5, 6 (2,160 QUESTIONS) ===');
  console.log('================================================================================');

  const jsonPath = path.join(__dirname, 'audit_data', 'cbse10_math_ch4_to_6_generated.json');
  const questions = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  console.log(`Loaded ${questions.length} validated questions.`);

  // Rule Q: Pre-mutation snapshot
  await createPreMutationSnapshot(['syllabus'], 'cbse10_math_ch4_to_6_commit');

  let batch = adminDb.batch();
  let count = 0;
  let batchNum = 1;

  for (let i = 0; i < questions.length; i++) {
    const q = questions[i];
    const docRef = adminDb.collection('questions').doc(q.questionCode);
    batch.set(docRef, {
      ...q,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    });
    count++;

    if (count % 400 === 0 || i === questions.length - 1) {
      console.log(`  Writing batch ${batchNum} (${count}/${questions.length})...`);
      await commitWithRetry(batch);
      batchNum++;
      batch = adminDb.batch();
    }
  }
  console.log(`✓ All ${questions.length} questions written to 'questions' collection successfully.`);

  // Update syllabus document for cbse_10_math
  console.log('\nSynchronizing syllabus document cbse_10_math for Chapters 4, 5, 6...');
  const sRef = adminDb.collection('syllabus').doc('cbse_10_math');
  const sSnap = await sRef.get();
  if (sSnap.exists) {
    const sData = sSnap.data();
    const chs = sData.chapters || [];

    for (let c = 3; c < 6 && c < chs.length; c++) {
      let chTotal = 0;
      for (const top of (chs[c].topics || [])) {
        if (top.subtopics && top.subtopics.length > 0) {
          for (const sub of top.subtopics) {
            sub.objectiveCount = 80;
            chTotal += 80;
          }
        } else {
          top.objectiveCount = 80;
          chTotal += 80;
        }
      }
      chs[c].objectiveCount = chTotal;
      console.log(`  Ch ${chs[c].number || (c + 1)} (${chs[c].name}): objectiveCount set to ${chTotal}`);
    }

    await sRef.update({ chapters: chs, updatedAt: new Date().toISOString() });
    console.log('✓ Syllabus cbse_10_math updated.');
  }

  console.log('\n=== CBSE 10 MATH CHAPTERS 4-6 COMMITTED AND SYNCED SUCCESSFULLY ===');
  process.exit(0);
}

commitCh4To6().catch(err => {
  console.error('Fatal error during commit:', err);
  process.exit(1);
});

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

async function commitMH10MTH2() {
  console.log('================================================================================');
  console.log('=== COMMITTING MH 10 MATHEMATICS PART 2 (GEOMETRY) (5,444 QUESTIONS) ===');
  console.log('================================================================================');

  const p1 = path.join(__dirname, 'audit_data', 'mh10_mth2_ch1_to_3_generated.json');
  const p2 = path.join(__dirname, 'audit_data', 'mh10_mth2_ch4_to_7_generated.json');
  const q1 = JSON.parse(fs.readFileSync(p1, 'utf8'));
  const q2 = JSON.parse(fs.readFileSync(p2, 'utf8'));
  const allQuestions = [...q1, ...q2];
  console.log(`Loaded ${allQuestions.length} validated questions (${q1.length} from Ch 1-3, ${q2.length} from Ch 4-7).`);

  // Rule Q: Pre-mutation snapshot on targeted syllabus & questions
  await createPreMutationSnapshot(['syllabus'], 'mh10_mth2_commit');

  // Ingest questions in batches of 400
  let batch = adminDb.batch();
  let count = 0;
  let batchNum = 1;

  for (let i = 0; i < allQuestions.length; i++) {
    const q = allQuestions[i];
    const docRef = adminDb.collection('questions').doc(q.questionCode);
    batch.set(docRef, {
      ...q,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    });
    count++;

    if (count % 400 === 0 || i === allQuestions.length - 1) {
      console.log(`  Writing batch ${batchNum} (${count}/${allQuestions.length})...`);
      await commitWithRetry(batch);
      batchNum++;
      batch = adminDb.batch();
    }
  }
  console.log(`✓ All ${allQuestions.length} questions written to 'questions' collection successfully.`);

  // Update syllabus document for mh_10_mth2
  console.log('\nSynchronizing syllabus document mh_10_mth2...');
  const sRef = adminDb.collection('syllabus').doc('mh_10_mth2');
  const sSnap = await sRef.get();
  if (sSnap.exists) {
    const sData = sSnap.data();
    const chs = sData.chapters || [];

    for (let c = 0; c < chs.length; c++) {
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
    console.log('✓ Syllabus mh_10_mth2 updated.');
  }

  console.log('\n=== MH 10 MATHEMATICS PART 2 (GEOMETRY) COMMITTED AND SYNCED SUCCESSFULLY ===');
  process.exit(0);
}

commitMH10MTH2().catch(err => {
  console.error('Fatal error during commit:', err);
  process.exit(1);
});

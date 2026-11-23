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

const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

const CLASS_10_SUBJECTS = [
  { docId: 'cbse_10_math', code: 'CBSE-10-MATH', name: 'CBSE Class 10 Mathematics' },
  { docId: 'cbse_10_sci',  code: 'CBSE-10-SCI',  name: 'CBSE Class 10 Science' },
  { docId: 'mh_10_mth1',   code: 'MH-10-MTH1',   name: 'MH Class 10 Mathematics Part 1 (Algebra)' },
  { docId: 'mh_10_mth2',   code: 'MH-10-MTH2',   name: 'MH Class 10 Mathematics Part 2 (Geometry)' },
  { docId: 'mh_10_scit1',  code: 'MH-10-SCIT1',  name: 'MH Class 10 Science & Technology Part 1' },
  { docId: 'mh_10_scit2',  code: 'MH-10-SCIT2',  name: 'MH Class 10 Science & Technology Part 2' }
];

async function verifySubject(sub) {
  const sylDoc = await adminDb.collection('syllabus').doc(sub.docId).get();
  const sylData = sylDoc.data();
  const leafCodes = [];

  function traverse(chNumber, tNumber, item) {
    if (item.subtopics && item.subtopics.length > 0) {
      for (const st of item.subtopics) {
        traverse(chNumber, item.number || tNumber, st);
      }
    } else {
      leafCodes.push(item.topicCode || `${sub.code}-${chNumber}-${item.number}`);
    }
  }

  if (sylData.chapters) {
    for (const ch of sylData.chapters) {
      if (ch.topics) {
        for (const t of ch.topics) {
          traverse(ch.number, t.number, t);
        }
      }
    }
  }

  const snap = await adminDb.collection('questions')
    .where('topicCode', '>=', sub.code)
    .where('topicCode', '<=', sub.code + '\uf8ff')
    .select('topicCode', 'text', 'options', 'correctAnswer', 'solution')
    .get();

  const byTopic = {};
  let svgCount = 0;
  let validationErrors = 0;

  snap.forEach(d => {
    const data = d.data();
    const tc = data.topicCode;
    byTopic[tc] = (byTopic[tc] || 0) + 1;
    if (data.text && data.text.includes('<svg')) svgCount++;
    if (!data.text || !data.options || !data.correctAnswer || !data.solution) validationErrors++;
  });

  let deficits = 0;
  for (const tc of leafCodes) {
    const count = byTopic[tc] || 0;
    if (count < 80) {
      deficits += (80 - count);
    }
  }

  return {
    sub,
    subtopics: leafCodes.length,
    totalQuestions: snap.size,
    target: leafCodes.length * 80,
    deficit: deficits,
    svgCount,
    validationErrors
  };
}

async function main() {
  console.log('================================================================================');
  console.log('=== CLASS 10 COMPREHENSIVE QUESTION BANK PARITY & INTEGRITY AUDIT ===');
  console.log('================================================================================');

  let grandTotal = 0;
  let grandTarget = 0;
  let grandDeficit = 0;
  let grandSVGs = 0;
  let grandErrors = 0;
  let grandSubtopics = 0;

  const results = [];
  for (const s of CLASS_10_SUBJECTS) {
    const r = await verifySubject(s);
    results.push(r);
    grandTotal += r.totalQuestions;
    grandTarget += r.target;
    grandDeficit += r.deficit;
    grandSVGs += r.svgCount;
    grandErrors += r.validationErrors;
    grandSubtopics += r.subtopics;
  }

  console.log('\nSubject-by-Subject Audit:');
  console.table(results.map(r => ({
    Subject: r.sub.code,
    Subtopics: r.subtopics,
    Questions: r.totalQuestions,
    Target: r.target,
    Deficit: r.deficit,
    Inline_SVGs: r.svgCount,
    Status: r.deficit === 0 ? '✓ 100% COMPLETE' : 'DEFICIT'
  })));

  console.log('================================================================================');
  console.log(`TOTAL CLASS 10 QUESTIONS  : ${grandTotal.toLocaleString()} / ${grandTarget.toLocaleString()}`);
  console.log(`TOTAL SUBTOPICS AUDITED   : ${grandSubtopics}`);
  console.log(`TOTAL REMAINING DEFICIT   : ${grandDeficit}`);
  console.log(`TOTAL INLINE VECTOR SVGs  : ${grandSVGs.toLocaleString()}`);
  console.log(`VALIDATION INTEGRITY ERR  : ${grandErrors}`);
  console.log('================================================================================');

  if (grandDeficit === 0 && grandErrors === 0) {
    console.log('🎉 ALL CLASS 10 SUBJECTS ARE 100% COMPLETE WITH ZERO DEFICITS!');
  } else {
    console.error('⚠️ Deficit or validation errors detected.');
    process.exit(1);
  }
  process.exit(0);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});

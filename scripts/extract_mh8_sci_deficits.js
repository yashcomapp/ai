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

async function extractMh8SciDeficits() {
  console.log('Extracting ground-truth deficits for mh_8_sci...');
  const doc = await adminDb.collection('syllabus').doc('mh_8_sci').get();
  const data = doc.data();
  const manifest = [];
  let totalDeficit = 0;
  let totalLeafs = 0;

  for (const ch of (data.chapters || [])) {
    const chNum = String(ch.number || ch.chapterNumber);
    const chName = ch.name || ch.title;
    const chLeafs = [];

    for (const top of (ch.topics || [])) {
      const subtopics = top.subtopics || [];
      if (subtopics.length > 0) {
        for (const sub of subtopics) {
          const tCode = sub.topicCode || sub.code;
          const snap = await adminDb.collection('questions').where('topicCode', '==', tCode).get();
          const count = snap.size;
          const needed = Math.max(0, 80 - count);
          totalDeficit += needed;
          totalLeafs++;
          chLeafs.push({
            topicCode: tCode,
            name: sub.name || sub.title,
            number: sub.number,
            parentTopic: top.name,
            current: count,
            needed: needed
          });
        }
      } else {
        const tCode = top.topicCode || top.code;
        const snap = await adminDb.collection('questions').where('topicCode', '==', tCode).get();
        const count = snap.size;
        const needed = Math.max(0, 80 - count);
        totalDeficit += needed;
        totalLeafs++;
        chLeafs.push({
          topicCode: tCode,
          name: top.name || top.title,
          number: top.number,
          parentTopic: chName,
          current: count,
          needed: needed
        });
      }
    }

    manifest.push({
      chapterNumber: chNum,
      chapterName: chName,
      leafCount: chLeafs.length,
      currentTotal: chLeafs.reduce((acc, l) => acc + l.current, 0),
      neededTotal: chLeafs.reduce((acc, l) => acc + l.needed, 0),
      leafs: chLeafs
    });
  }

  fs.writeFileSync(path.join(__dirname, 'mh8_sci_deficit_manifest.json'), JSON.stringify(manifest, null, 2));
  console.log(`\n=== MH 8 SCIENCE DEFICIT MANIFEST GENERATED ===`);
  console.log(`Total chapters: ${manifest.length} | Total leaf subtopics: ${totalLeafs} | Total questions needed: ${totalDeficit}`);
  manifest.forEach(m => {
    console.log(`Ch ${m.chapterNumber}: ${m.chapterName} -> ${m.leafCount} subtopics | current: ${m.currentTotal} | needed: ${m.neededTotal}`);
  });
}

extractMh8SciDeficits().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });

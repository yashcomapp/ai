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
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function checkChapter(chNum) {
  const manifest = JSON.parse(fs.readFileSync('scripts/mh8_mth_deficit_manifest.json'));
  const ch = manifest.find(c => c.chapterNumber === String(chNum));
  console.log(`Checking Ch ${chNum}: ${ch.chapterName} (${ch.leafs.length} leafs)`);
  let totalDeficit = 0;
  const results = [];
  for (const l of ch.leafs) {
    const snap = await adminDb.collection('questions').where('topicCode', '==', l.topicCode).get();
    const cur = snap.size;
    const need = Math.max(0, 80 - cur);
    totalDeficit += need;
    results.push({ topicCode: l.topicCode, name: l.name, current: cur, needed: need });
    console.log(`  ${l.topicCode}: ${cur} Qs (need ${need}) -> ${l.name}`);
  }
  console.log(`Total deficit for Ch ${chNum}: ${totalDeficit} Qs`);
  return results;
}

const targetCh = process.argv[2] || 8;
checkChapter(targetCh).then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });

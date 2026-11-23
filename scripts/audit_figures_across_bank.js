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
const fs = require('fs');
const path = require('path');

const SUBJECTS_TO_AUDIT = [
  // Class 10
  { code: 'MH-10-MTH1', name: 'MH 10 Algebra', domain: 'Math 1' },
  { code: 'MH-10-MTH2', name: 'MH 10 Geometry', domain: 'Math 2' },
  { code: 'MH-10-SCIT1', name: 'MH 10 Science 1 (Phy/Chem)', domain: 'Science 1' },
  { code: 'MH-10-SCIT2', name: 'MH 10 Science 2 (Bio/Env)', domain: 'Science 2' },
  { code: 'CBSE-10-MATH', name: 'CBSE 10 Math', domain: 'Math' },
  { code: 'CBSE-10-SCI', name: 'CBSE 10 Science', domain: 'Science' },
  // Class 9
  { code: 'MH-9-MTH1', name: 'MH 9 Algebra', domain: 'Math 1' },
  { code: 'MH-9-MTH2', name: 'MH 9 Geometry', domain: 'Math 2' },
  { code: 'MH-9-SCIT', name: 'MH 9 Science & Tech', domain: 'Science' },
  { code: 'CBSE-9-MGM', name: 'CBSE 9 Mathematics', domain: 'Math' },
  { code: 'CBSE-9-SCIE', name: 'CBSE 9 Science', domain: 'Science' },
  // Class 8
  { code: 'CBSE-8-MGP1', name: 'CBSE 8 Mathematics', domain: 'Math' },
  { code: 'CBSE-8-CURI', name: 'CBSE 8 Science', domain: 'Science' },
  { code: 'MH-8-SCI', name: 'MH 8 Science', domain: 'Science' }
];

async function auditSubjectFigures(sub) {
  console.log(`Auditing figures for ${sub.code} (${sub.name})...`);
  const snap = await adminDb.collection('questions')
    .where('topicCode', '>=', sub.code)
    .where('topicCode', '<=', sub.code + '\uf8ff')
    .select('topicCode', 'chapterNumber', 'text', 'requiresFigure')
    .get();

  const total = snap.size;
  let totalWithSvg = 0;
  const byChapter = {};
  const byTopic = {};

  snap.forEach(d => {
    const data = d.data();
    const ch = data.chapterNumber || 'Unknown';
    const tc = data.topicCode || 'Unknown';
    const text = data.text || '';
    const hasSvg = text.includes('<svg') || text.includes('<img') || data.requiresFigure === true;

    if (!byChapter[ch]) byChapter[ch] = { total: 0, withSvg: 0 };
    byChapter[ch].total++;

    if (!byTopic[tc]) byTopic[tc] = { total: 0, withSvg: 0, chapter: ch };
    byTopic[tc].total++;

    if (hasSvg) {
      totalWithSvg++;
      byChapter[ch].withSvg++;
      byTopic[tc].withSvg++;
    }
  });

  return {
    sub,
    total,
    totalWithSvg,
    svgPercentage: total > 0 ? ((totalWithSvg / total) * 100).toFixed(1) + '%' : '0%',
    byChapter,
    byTopic
  };
}

async function main() {
  console.log('================================================================================');
  console.log('=== AUDITING FIGURE-BASED QUESTIONS ACROSS QUESTION BANK ===');
  console.log('================================================================================');

  const allAudits = [];
  for (const s of SUBJECTS_TO_AUDIT) {
    const res = await auditSubjectFigures(s);
    allAudits.push(res);
  }

  console.log('\n--- FIGURE AUDIT SUMMARY BY SUBJECT ---');
  console.table(allAudits.map(a => ({
    Subject: a.sub.code,
    Name: a.sub.name,
    Total_Questions: a.total,
    With_Figures: a.totalWithSvg,
    Figure_Percentage: a.svgPercentage
  })));

  const outPath = path.join(__dirname, 'audit_data', 'figure_audit_full.json');
  fs.writeFileSync(outPath, JSON.stringify(allAudits, null, 2));
  console.log(`\nDetailed report written to ${outPath}`);
  process.exit(0);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});

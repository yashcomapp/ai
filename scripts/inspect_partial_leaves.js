const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function main() {
  const targets = [
    ['mh_10_mth1', 'MH-10-MTH1'],
    ['mh_10_scit1', 'MH-10-SCIT1'],
    ['mh_10_scit2', 'MH-10-SCIT2'],
  ];

  const out = {};

  for (const [docId, prefix] of targets) {
    const sylSnap = await adminDb.collection('syllabus').doc(docId).get();
    const syl = sylSnap.data();

    const qSnap = await adminDb
      .collection('questions')
      .where('topicCode', '>=', prefix + '-')
      .where('topicCode', '<=', prefix + '-\uf8ff')
      .select('topicCode', 'questionCode', 'type', 'vault', 'difficulty', 'status', 'disputed', 'text')
      .get();

    const byTopic = {};
    qSnap.forEach((d) => {
      const q = d.data();
      if (q.status === 'quarantined' || q.disputed) return;
      if (!byTopic[q.topicCode]) byTopic[q.topicCode] = [];
      byTopic[q.topicCode].push({ id: d.id, ...q });
    });

    const partials = [];
    for (const ch of syl.chapters || []) {
      const chNum = Number(ch.number || ch.chapterNumber);
      const chName = ch.name || ch.chapterName;
      for (const t of ch.topics || []) {
        const leaves =
          Array.isArray(t.subtopics) && t.subtopics.length > 0
            ? t.subtopics.map((s) => ({
                code: s.subtopicCode || s.topicCode,
                name: s.name || s.subtopicName,
              }))
            : [{ code: t.topicCode, name: t.name || t.topicName }];

        for (const leaf of leaves) {
          const qs = byTopic[leaf.code] || [];
          if (qs.length > 0 && qs.length < 80) {
            const vaults = {};
            const types = {};
            let maxSeq = 0;
            for (const q of qs) {
              vaults[q.vault || 'unset'] = (vaults[q.vault || 'unset'] || 0) + 1;
              types[q.type || 'unset'] = (types[q.type || 'unset'] || 0) + 1;
              const m = String(q.questionCode || q.id).match(/-(\d+)$/);
              if (m) maxSeq = Math.max(maxSeq, Number(m[1]));
            }
            partials.push({
              ch: chNum,
              chName,
              code: leaf.code,
              name: leaf.name,
              count: qs.length,
              missing: 80 - qs.length,
              maxSeq,
              vaults,
              types,
              existingTexts: qs.map((q) => (q.text || '').slice(0, 80)),
            });
          }
        }
      }
    }

    out[docId] = partials;
    console.log(`\n=== ${docId}: ${partials.length} partial leaves ===`);
    for (const p of partials) {
      console.log(
        `  ${p.code.padEnd(24)} | ${String(p.count).padStart(2)}/80 (need ${String(p.missing).padStart(2)}) | vaults=${JSON.stringify(p.vaults)} | types=${JSON.stringify(p.types)} | ${p.name}`
      );
    }
  }

  const outPath = path.join(__dirname, 'audit_data', 'partial_leaves_detail.json');
  fs.writeFileSync(outPath, JSON.stringify(out, null, 2), 'utf8');
  console.log('\nSaved:', outPath);
  process.exit(0);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});

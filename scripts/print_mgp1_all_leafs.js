const fs = require('fs');
const manifest = JSON.parse(fs.readFileSync('scripts/cbse8_mgp1_deficit_manifest.json', 'utf8'));

manifest.forEach(ch => {
  console.log(`\n================ Chapter ${ch.chapterNumber}: ${ch.chapterName} (${ch.neededTotal} needed) ================`);
  ch.leafs.forEach(l => {
    console.log(`  ${l.topicCode.padEnd(24)} | cur: ${String(l.current).padStart(2)} | need: ${String(l.needed).padStart(2)} | ${l.name}`);
  });
});

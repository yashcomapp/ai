const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function run() {
  const s = await db.collection('syllabusTopicIndex')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .get();

  const topicsByCh = {};
  s.forEach(d => {
    const data = d.data();
    const ch = data.chapterNumber;
    if (ch >= 11 && ch <= 18) {
      if (!topicsByCh[ch]) topicsByCh[ch] = [];
      // Only keep top-level topics (e.g. 11.1, 11.2, not 11.1.1)
      const parts = data.topicCode.split('-');
      const tCode = parts[parts.length - 1]; // e.g. "11.1" or "11.1.1"
      if (tCode.split('.').length === 2) {
        topicsByCh[ch].push({ topicCode: data.topicCode, topicName: data.topicName, chapterName: data.chapterName });
      }
    }
  });

  Object.keys(topicsByCh).sort((a,b)=>Number(a)-Number(b)).forEach(ch => {
    console.log('=== Chapter ' + ch + ': ' + topicsByCh[ch][0].chapterName + ' (' + topicsByCh[ch].length + ' canonical topics) ===');
    topicsByCh[ch].forEach(t => console.log('  ' + t.topicCode + ': ' + t.topicName));
  });
}

run().then(()=>process.exit(0)).catch(e=>{console.error(e);process.exit(1);});

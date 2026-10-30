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
    if (!topicsByCh[ch]) topicsByCh[ch] = [];
    topicsByCh[ch].push({ topicCode: data.topicCode, topicName: data.topicName, chapterName: data.chapterName });
  });

  Object.keys(topicsByCh).sort((a,b)=>Number(a)-Number(b)).forEach(ch => {
    console.log('Chapter ' + ch + ': ' + (topicsByCh[ch][0] ? topicsByCh[ch][0].chapterName : '') + ' (' + topicsByCh[ch].length + ' topics)');
    topicsByCh[ch].forEach(t => console.log('  ' + t.topicCode + ': ' + t.topicName));
  });
}

run().then(()=>process.exit(0)).catch(e=>{console.error(e);process.exit(1);});

const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function auditTopics() {
  const docSnap = await db.collection('syllabus').doc('mh_9_scit').get();
  if (!docSnap.exists) {
    console.error('Document mh_9_scit not found!');
    return;
  }
  const syllabusData = docSnap.data();
  console.log(`Loaded mh_9_scit syllabus with ${syllabusData.chapters ? syllabusData.chapters.length : 0} chapters.`);

  // Get all questions for SCIT Class 9
  const qSnap = await db.collection('questions')
    .where('class', 'in', ['9', 9])
    .where('subjectCode', '==', 'SCIT')
    .select('topicCode', 'chapterNumber', 'questionCode')
    .get();
  
  console.log(`Total questions in SCIT Class 9: ${qSnap.size}`);
  
  const countByTopic = {};
  qSnap.forEach(d => {
    const data = d.data();
    const tc = data.topicCode || 'unknown';
    countByTopic[tc] = (countByTopic[tc] || 0) + 1;
  });

  const topicCatalog = [];
  (syllabusData.chapters || []).forEach(ch => {
    const chNum = parseInt(ch.chapterNumber || ch.number || ch.id, 10);
    const chName = ch.chapterName || ch.title || ch.name || '';
    (ch.topics || []).forEach(t => {
      const tc = t.topicCode || t.code || t.id;
      const tName = t.topicName || t.name || t.title || '';
      const count = countByTopic[tc] || 0;
      topicCatalog.push({
        chapterNumber: chNum,
        chapterName: chName,
        topicCode: tc,
        topicName: tName,
        count: count
      });
    });
  });

  topicCatalog.sort((a,b) => {
    if (a.chapterNumber !== b.chapterNumber) return a.chapterNumber - b.chapterNumber;
    return a.topicCode.localeCompare(b.topicCode);
  });

  console.log('\n========================================================================================');
  console.log('TOPIC AUDIT FOR MH-9-SCIT: DEFICIENT TOPICS (< 40 Qs)');
  console.log('========================================================================================');
  let deficitTotal = 0;
  let deficientTopics = 0;
  let wellStockedTopics = 0;

  topicCatalog.forEach(t => {
    const deficit = Math.max(0, 40 - t.count);
    if (t.count < 40) {
      deficientTopics++;
      deficitTotal += deficit;
      console.log(`Ch ${String(t.chapterNumber).padStart(2)} | ${t.topicCode.padEnd(25)} | Current: ${String(t.count).padStart(2)} | Deficit: +${String(deficit).padStart(2)} | ${t.topicName}`);
    } else {
      wellStockedTopics++;
    }
  });

  console.log('\n========================================================================================');
  console.log('ALL TOPIC BREAKDOWN IN MH-9-SCIT');
  console.log('========================================================================================');
  let currentCh = null;
  topicCatalog.forEach(t => {
    if (t.chapterNumber !== currentCh) {
      currentCh = t.chapterNumber;
      console.log(`\n--- Chapter ${currentCh}: ${t.chapterName} ---`);
    }
    const status = t.count >= 40 ? '✅' : '⚠️ DEFICIENT';
    console.log(`  ${status} | ${t.topicCode.padEnd(25)} | ${String(t.count).padStart(3)} Qs | ${t.topicName}`);
  });

  console.log('\n========================================================================================');
  console.log('SUMMARY');
  console.log('========================================================================================');
  console.log('Total topics cataloged in syllabus:', topicCatalog.length);
  console.log('Topics with >= 40 questions:', wellStockedTopics);
  console.log('Topics with < 40 questions:', deficientTopics);
  console.log('Total questions needed to reach 40/topic threshold:', deficitTotal);
}

auditTopics().catch(console.error);

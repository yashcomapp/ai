const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');
const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      const k = trimmed.slice(0, idx).trim();
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[k] = v;
    }
  }
});

const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

async function auditClass8() {
  const class8Subjects = [
    { id: 'cbse_8_curi', name: 'CBSE 8 Science (Curiosity)' },
    { id: 'cbse_8_mgp1', name: 'CBSE 8 Maths (Ganit Prakash Part 1)' },
    { id: 'cbse_8_mgp2', name: 'CBSE 8 Maths (Ganit Prakash Part 2)' },
    { id: 'mh_8_mth', name: 'MH 8 Mathematics' },
    { id: 'mh_8_sci', name: 'MH 8 General Science' }
  ];

  console.log('======================================================================');
  console.log('                    CLASS 8 COMPREHENSIVE AUDIT                       ');
  console.log('======================================================================\n');

  let grandTotalSubtopics = 0;
  let grandTotalCurrent = 0;
  let grandTarget = 0;
  let grandDeficit = 0;

  const subjectBreakdowns = [];

  for (const sub of class8Subjects) {
    const doc = await db.collection('syllabus').doc(sub.id).get();
    if (!doc.exists) {
      console.log(`MISSING SYLLABUS DOC: ${sub.id}`);
      continue;
    }
    const data = doc.data();
    const chapters = data.chapters || [];
    
    let subTotalSubtopics = 0;
    let subCurrentQs = 0;
    let subDeficit = 0;
    const chapterDetails = [];

    chapters.forEach((ch, chIdx) => {
      let chSubtopics = 0;
      let chCurrentQs = 0;
      let chDeficit = 0;
      const chLeafs = [];

      (ch.topics || []).forEach(top => {
        const subtopics = top.subtopics || [];
        if (subtopics.length > 0) {
          subtopics.forEach(s => {
            chSubtopics++;
            const count = s.objectiveCount || 0;
            chCurrentQs += count;
            const def = Math.max(0, 80 - count);
            chDeficit += def;
            chLeafs.push({
              code: s.topicCode || s.code,
              name: s.name || s.title,
              number: s.number,
              parentTopic: top.name,
              current: count,
              deficit: def
            });
          });
        } else {
          chSubtopics++;
          const count = top.objectiveCount || 0;
          chCurrentQs += count;
          const def = Math.max(0, 80 - count);
          chDeficit += def;
          chLeafs.push({
            code: top.topicCode || top.code,
            name: top.name || top.title,
            number: top.number,
            parentTopic: ch.name,
            current: count,
            deficit: def
          });
        }
      });

      subTotalSubtopics += chSubtopics;
      subCurrentQs += chCurrentQs;
      subDeficit += chDeficit;

      chapterDetails.push({
        num: ch.number || ch.chapterNumber || (chIdx + 1),
        title: ch.name || ch.title,
        subtopics: chSubtopics,
        currentQs: chCurrentQs,
        targetQs: chSubtopics * 80,
        deficit: chDeficit,
        leafs: chLeafs
      });
    });

    grandTotalSubtopics += subTotalSubtopics;
    grandTotalCurrent += subCurrentQs;
    grandTarget += (subTotalSubtopics * 80);
    grandDeficit += subDeficit;

    subjectBreakdowns.push({
      id: sub.id,
      name: sub.name,
      boardCode: data.boardCode,
      class: data.class,
      subjectCode: data.subjectCode,
      chaptersCount: chapters.length,
      subtopicsCount: subTotalSubtopics,
      currentQs: subCurrentQs,
      targetQs: subTotalSubtopics * 80,
      deficit: subDeficit,
      chapters: chapterDetails
    });

    console.log(`### ${sub.name} (${sub.id})`);
    console.log(`  Chapters:             ${chapters.length}`);
    console.log(`  Leaf Subtopics:       ${subTotalSubtopics}`);
    console.log(`  Current Questions:    ${subCurrentQs}`);
    console.log(`  Target Questions:     ${subTotalSubtopics * 80}`);
    console.log(`  Questions Needed:     ${subDeficit}`);
    console.log(`  Chapters with deficit: ${chapterDetails.filter(c => c.deficit > 0).length} / ${chapters.length}\n`);
  }

  console.log('----------------------------------------------------------------------');
  console.log('GRADE 8 OVERALL SUMMARY:');
  console.log(`  Total Leaf Subtopics:  ${grandTotalSubtopics}`);
  console.log(`  Current Questions:     ${grandTotalCurrent}`);
  console.log(`  Target (80 Qs/sub):    ${grandTarget}`);
  console.log(`  Total Questions Needed: ${grandDeficit}`);
  console.log('======================================================================\n');

  fs.writeFileSync(path.join(__dirname, 'class8_audit_summary.json'), JSON.stringify(subjectBreakdowns, null, 2));
  console.log('Full audit details saved to scripts/class8_audit_summary.json');
}

auditClass8().catch(err => {
  console.error(err);
  process.exit(1);
});

const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');
const { db, SUBTOPIC_INFO } = require('./ch1_topup_base.js');
const { part1Questions } = require('./ch1_topup_data_part1.js');
const { part2Questions } = require('./ch1_topup_data_part2.js');

async function insertAll() {
  const allQuestions = [...part1Questions, ...part2Questions];
  console.log(`Loaded ${allQuestions.length} top-up questions for MH-9-SCIT Chapter 1.`);

  // Group by subtopicNumber
  const bySubtopic = {};
  allQuestions.forEach(q => {
    if (!bySubtopic[q.subtopicNumber]) bySubtopic[q.subtopicNumber] = [];
    bySubtopic[q.subtopicNumber].push(q);
  });

  console.log('Breakdown by subtopic:');
  Object.entries(bySubtopic).forEach(([st, arr]) => {
    console.log(`  Subtopic ${st}: ${arr.length} questions`);
  });

  // Fetch highest sequence numbers for each subtopic
  console.log('Fetching existing questions in Chapter 1 to establish sequence numbering...');
  const existingSnap = await db.collection('questions')
    .where('chapterNumber', '==', 1)
    .where('subjectCode', '==', 'SCIT')
    .where('boardCode', '==', 'MH')
    .where('class', '==', '9')
    .get();

  const maxSeq = {}; // key: `${subtopicNumber}-${type}`
  existingSnap.docs.forEach(d => {
    const data = d.data();
    const stNum = data.subtopicNumber || data.topicNumber;
    const type = data.questionType || data.type || 'OSC';
    const qcode = data.questionCode || '';
    const parts = qcode.split('-');
    if (parts.length >= 7) {
      const seq = parseInt(parts[parts.length - 1], 10);
      const key = `${stNum}-${type}`;
      if (!isNaN(seq)) {
        maxSeq[key] = Math.max(maxSeq[key] || 0, seq);
      }
    }
  });

  console.log('Current max sequence table:', maxSeq);

  // Prepare batch writes (max 400 per batch)
  const batches = [db.batch()];
  let currentBatchIndex = 0;
  let opCount = 0;
  let totalInserted = 0;

  const subtopicAddedCounts = {};

  allQuestions.forEach(q => {
    const stNum = q.subtopicNumber;
    const info = SUBTOPIC_INFO[stNum];
    if (!info) {
      throw new Error(`Missing metadata for subtopic ${stNum}`);
    }

    const type = q.type || 'OSC';
    const key = `${stNum}-${type}`;
    maxSeq[key] = (maxSeq[key] || 0) + 1;
    const seqStr = String(maxSeq[key]).padStart(3, '0');
    const qcode = `MH-9-SCIT-1-${stNum}-${type}-${seqStr}`;

    const docRef = db.collection('questions').doc(qcode);
    const docData = {
      ...q,
      boardCode: 'MH',
      class: '9',
      subjectCode: 'SCIT',
      board: 'Maharashtra State Board',
      subject: 'Science and Technology',
      chapterNumber: 1,
      chapter: 'Laws of Motion',
      vault: 'practice',
      examCategory: 'standard',
      requiresFigure: false,
      marks: 4,
      timesUsed: 0,
      usedInClassroomTest: false,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      subtopicCode: info.subtopicCode,
      subtopicName: info.subtopicName,
      subtopic: info.subtopicName,
      parentTopicCode: info.parentTopicCode,
      parentTopicName: info.parentTopicName,
      topicCode: info.parentTopicCode,
      topic: info.parentTopicName,
      topicName: info.parentTopicName,
      topicNumber: stNum,
      questionCode: qcode
    };

    if (opCount >= 400) {
      batches.push(db.batch());
      currentBatchIndex++;
      opCount = 0;
    }

    batches[currentBatchIndex].set(docRef, docData);
    opCount++;
    totalInserted++;
    subtopicAddedCounts[stNum] = (subtopicAddedCounts[stNum] || 0) + 1;
  });

  console.log(`Writing ${totalInserted} questions across ${batches.length} batch(es)...`);
  for (let i = 0; i < batches.length; i++) {
    await batches[i].commit();
    console.log(`  Batch ${i + 1}/${batches.length} committed.`);
  }

  console.log('All questions inserted successfully!');

  // Update syllabus document
  console.log('Updating syllabus/mh_9_scit document...');
  const sylRef = db.collection('syllabus').doc('mh_9_scit');
  const sylDoc = await sylRef.get();
  if (sylDoc.exists) {
    const data = sylDoc.data();
    const ch1 = (data.chapters || []).find(c => String(c.number) === '1');
    if (ch1) {
      let chAdded = 0;
      (ch1.topics || []).forEach(t => {
        let topicAdded = 0;
        (t.subtopics || []).forEach(st => {
          const added = subtopicAddedCounts[st.number] || 0;
          if (added > 0) {
            st.objectiveCount = (st.objectiveCount || 0) + added;
            topicAdded += added;
            chAdded += added;
            console.log(`  Updated Subtopic ${st.number} obj count to ${st.objectiveCount}`);
          }
        });
        if (topicAdded > 0) {
          t.objectiveCount = (t.objectiveCount || 0) + topicAdded;
          console.log(`  Updated Topic ${t.number} obj count to ${t.objectiveCount}`);
        }
      });
      ch1.objectiveCount = (ch1.objectiveCount || 0) + chAdded;
      console.log(`  Updated Chapter 1 obj count to ${ch1.objectiveCount}`);
      await sylRef.update({ chapters: data.chapters });
      console.log('Syllabus updated successfully.');
    }
  }
}

insertAll().catch(err => {
  console.error('Error inserting topup:', err);
  process.exit(1);
});

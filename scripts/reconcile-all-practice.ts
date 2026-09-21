import * as path from 'path';
import * as fs from 'fs';

const envPath = path.join(process.cwd(), '.env.local');
if (fs.existsSync(envPath)) {
  const content = fs.readFileSync(envPath, 'utf8');
  content.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        const key = trimmed.slice(0, idx).trim();
        let val = trimmed.slice(idx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
        if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
        process.env[key] = val;
      }
    }
  });
}

async function reconcilePracticeData() {
  const { adminDb } = await import('../src/lib/firebase/admin');
  const { createPreMutationSnapshot } = await import('../src/lib/backupUtils');
  const { evaluateQuestionAnswer, toCanonicalQuestionType, parseAnswerList, isMultipleChoiceType } = await import('../src/lib/questionTypes');

  console.log('--- Step 1: Taking Pre-Mutation Snapshot ---');
  const snapshotMeta = await createPreMutationSnapshot(
    ['parentReviews'],
    'Reconcile parentReviews practiceNumber, timestamp, topicName, and canonical evaluation sync'
  );
  console.log(`Snapshot saved: ${snapshotMeta.snapshotFilePath} (${snapshotMeta.collections.parentReviews} reviews)`);

  console.log('\n--- Step 2: Fetching Syllabus Topic Index ---');
  const syllabusSnap = await adminDb.collection('syllabusTopicIndex').get();
  const topicMap = new Map<string, any>();
  syllabusSnap.docs.forEach(doc => {
    topicMap.set(doc.id, doc.data());
  });
  console.log(`Loaded ${topicMap.size} syllabus topics.`);

  console.log('\n--- Step 3: Fetching All parentReviews ---');
  const reviewsSnap = await adminDb.collection('parentReviews').get();
  console.log(`Found ${reviewsSnap.docs.length} total parentReviews docs.`);

  // Group by studentCode + topicCode
  const studentTopicGroups = new Map<string, any[]>();
  reviewsSnap.docs.forEach(doc => {
    const data = { _docId: doc.id, ...doc.data() as any };
    const sCode = data.studentCode || 'unknown';
    const tCode = data.topicCode || 'unknown';
    const key = `${sCode}___${tCode}`;
    if (!studentTopicGroups.has(key)) {
      studentTopicGroups.set(key, []);
    }
    studentTopicGroups.get(key)!.push(data);
  });

  let updatedCount = 0;
  let batch = adminDb.batch();
  let batchOps = 0;

  for (const [groupKey, items] of studentTopicGroups.entries()) {
    // Sort chronologically (oldest first)
    items.sort((a, b) => {
      const ta = a.startedAt?.toDate ? a.startedAt.toDate().getTime() : (a.createdAt?.toDate ? a.createdAt.toDate().getTime() : (new Date(a.createdAt || a.timestamp || 0).getTime()));
      const tb = b.startedAt?.toDate ? b.startedAt.toDate().getTime() : (b.createdAt?.toDate ? b.createdAt.toDate().getTime() : (new Date(b.createdAt || b.timestamp || 0).getTime()));
      return ta - tb;
    });

    for (let index = 0; index < items.length; index++) {
      const item = items[index];
      const practiceNumber = index + 1;
      const topicCode = item.topicCode;
      let topicName = item.topicName;
      let subjectName = item.subjectName || 'General';
      let chapterName = item.chapterName || 'General Chapter';

      if (topicCode && topicMap.has(topicCode)) {
        const sData = topicMap.get(topicCode);
        topicName = sData.topicName || sData.title || topicName || topicCode;
        subjectName = sData.subjectName || sData.subject || subjectName;
        chapterName = sData.chapterName || sData.chapterTitle || sData.chapter || chapterName;
      }

      const rawCreated = item.createdAt?.toDate ? item.createdAt.toDate() : (item.createdAt ? new Date(item.createdAt) : null);
      const rawStarted = item.startedAt?.toDate ? item.startedAt.toDate() : (item.startedAt ? new Date(item.startedAt) : null);
      const timestamp = (rawCreated || rawStarted || new Date()).toISOString();

      // Re-evaluate questions
      const questions = Array.isArray(item.questions) ? item.questions : (Array.isArray(item.questionDetails) ? item.questionDetails : []);
      let correctCount = 0;
      let disputedCount = item.disputedCount || 0;

      const reconciledQuestions = questions.map((q: any) => {
        const canonicalType = toCanonicalQuestionType(q.type);
        const isMultiple = isMultipleChoiceType(canonicalType);
        const resolvedCorrectAnswer = isMultiple
          ? (Array.isArray(q.correctAnswers) && q.correctAnswers.length > 0 ? q.correctAnswers : (q.correctAnswer ? parseAnswerList(q.correctAnswer) : []))
          : (q.correctAnswer || (Array.isArray(q.correctAnswers) ? q.correctAnswers[0] : ''));

        const evalResult = evaluateQuestionAnswer(
          canonicalType,
          q.userAnswer ?? '',
          resolvedCorrectAnswer,
          q.options || []
        );

        const isDisputed = !!q.isDisputed;
        if (!isDisputed && evalResult) {
          correctCount++;
        }

        return {
          ...q,
          type: canonicalType,
          isCorrect: evalResult
        };
      });

      const validCount = Math.max(1, reconciledQuestions.length - disputedCount);
      const scorePercent = Math.round((correctCount / validCount) * 100);

      const docRef = adminDb.collection('parentReviews').doc(item._docId);
      const updateData: any = {
        practiceNumber,
        topicName: topicName || topicCode || 'Practice Session',
        subjectName,
        chapterName,
        timestamp,
        submittedAt: item.submittedAt || rawCreated || rawStarted || new Date(),
        score: correctCount,
        totalMarks: validCount,
        percentage: scorePercent,
        correctCount,
        scorePercent,
        totalQuestions: validCount,
        examType: 'practice',
        type: 'practice'
      };

      if (reconciledQuestions.length > 0) {
        updateData.questions = reconciledQuestions;
        updateData.questionDetails = reconciledQuestions;
      }

      batch.set(docRef, updateData, { merge: true });
      batchOps++;
      updatedCount++;

      if (batchOps >= 400) {
        await batch.commit();
        batch = adminDb.batch();
        batchOps = 0;
      }
    }
  }

  if (batchOps > 0) {
    await batch.commit();
  }

  console.log(`\n✅ Successfully reconciled ${updatedCount} parentReviews documents across ${studentTopicGroups.size} student-topic groups!`);
}

reconcilePracticeData()
  .then(() => process.exit(0))
  .catch(err => {
    console.error('Reconciliation failed:', err);
    process.exit(1);
  });

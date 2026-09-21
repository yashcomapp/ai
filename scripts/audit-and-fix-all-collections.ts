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

async function auditAndFixAllCollections() {
  const { adminDb } = await import('../src/lib/firebase/admin');
  const { createPreMutationSnapshot } = await import('../src/lib/backupUtils');
  const { evaluateQuestionAnswer, toCanonicalQuestionType, parseAnswerList, isMultipleChoiceType } = await import('../src/lib/questionTypes');

  console.log('=== Step 1: Pre-Mutation Snapshot ===');
  const snapshotMeta = await createPreMutationSnapshot(
    ['questions', 'parentReviews', 'practiceSubmissions', 'reviews'],
    'Comprehensive harmonization of all old question and practice records'
  );
  console.log(`Snapshot saved: ${snapshotMeta.snapshotFilePath}`);
  console.log('Collections counts:', snapshotMeta.collections);

  // 1. Audit & Fix questions collection
  console.log('\n=== Step 2: Checking Questions Collection ===');
  const questionsSnap = await adminDb.collection('questions').get();
  let nonCanonicalQuestions = 0;
  let qBatch = adminDb.batch();
  let qBatchOps = 0;

  for (const doc of questionsSnap.docs) {
    const data = doc.data();
    const canonical = toCanonicalQuestionType(data.type);
    if (data.type !== canonical) {
      nonCanonicalQuestions++;
      qBatch.update(doc.ref, { type: canonical });
      qBatchOps++;
      if (qBatchOps >= 400) {
        await qBatch.commit();
        qBatch = adminDb.batch();
        qBatchOps = 0;
      }
    }
  }
  if (qBatchOps > 0) {
    await qBatch.commit();
  }
  console.log(`Questions collection: ${questionsSnap.size} total docs, fixed ${nonCanonicalQuestions} non-canonical types.`);

  // 2. Audit & Fix syllabusTopicIndex map
  const syllabusSnap = await adminDb.collection('syllabusTopicIndex').get();
  const topicMap = new Map<string, any>();
  syllabusSnap.docs.forEach(doc => {
    topicMap.set(doc.id, doc.data());
  });
  console.log(`Loaded ${topicMap.size} syllabus topics for enrichment.`);

  // 3. Audit & Fix practiceSubmissions
  console.log('\n=== Step 3: Checking practiceSubmissions Collection ===');
  const submissionsSnap = await adminDb.collection('practiceSubmissions').get();
  let subFixed = 0;
  let subBatch = adminDb.batch();
  let subBatchOps = 0;

  // Group submissions by studentCode + topicCode for chronological practiceNumber assignment
  const studentTopicSubs = new Map<string, any[]>();
  submissionsSnap.docs.forEach(doc => {
    const d = { _docId: doc.id, ...doc.data() as any };
    const sCode = d.studentCode || 'unknown';
    const tCode = d.topicCode || 'unknown';
    const key = `${sCode}___${tCode}`;
    if (!studentTopicSubs.has(key)) {
      studentTopicSubs.set(key, []);
    }
    studentTopicSubs.get(key)!.push(d);
  });

  for (const [key, items] of studentTopicSubs.entries()) {
    items.sort((a, b) => {
      const ta = a.submittedAt?.toDate ? a.submittedAt.toDate().getTime() : (a.submittedAt ? new Date(a.submittedAt).getTime() : (a.startedAt ? new Date(a.startedAt).getTime() : 0));
      const tb = b.submittedAt?.toDate ? b.submittedAt.toDate().getTime() : (b.submittedAt ? new Date(b.submittedAt).getTime() : (b.startedAt ? new Date(b.startedAt).getTime() : 0));
      return ta - tb;
    });

    for (let i = 0; i < items.length; i++) {
      const item = items[i];
      const practiceNumber = i + 1;
      const topicCode = item.topicCode;
      let topicName = item.topicName;
      if (topicCode && topicMap.has(topicCode)) {
        topicName = topicMap.get(topicCode).topicName || topicName || topicCode;
      }

      const questions = Array.isArray(item.questions) ? item.questions : [];
      let correctCount = 0;
      let hasChange = false;

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

        if (q.type !== canonicalType || q.isCorrect !== evalResult) {
          hasChange = true;
        }

        if (!q.isDisputed && evalResult) {
          correctCount++;
        }

        return {
          ...q,
          type: canonicalType,
          isCorrect: evalResult
        };
      });

      const rawSubmitted = item.submittedAt?.toDate ? item.submittedAt.toDate() : (item.submittedAt ? new Date(item.submittedAt) : new Date());

      const updateData: any = {
        practiceNumber,
        topicName: topicName || topicCode || 'Practice Session',
        score: correctCount,
        submittedAt: rawSubmitted,
        timestamp: rawSubmitted.toISOString()
      };

      if (reconciledQuestions.length > 0) {
        updateData.questions = reconciledQuestions;
      }

      const docRef = adminDb.collection('practiceSubmissions').doc(item._docId);
      subBatch.set(docRef, updateData, { merge: true });
      subBatchOps++;
      subFixed++;

      if (subBatchOps >= 400) {
        await subBatch.commit();
        subBatch = adminDb.batch();
        subBatchOps = 0;
      }
    }
  }

  if (subBatchOps > 0) {
    await subBatch.commit();
  }
  console.log(`practiceSubmissions collection: ${submissionsSnap.size} total docs, synchronized ${subFixed} records.`);

  // 4. Audit & Fix parentReviews
  console.log('\n=== Step 4: Checking parentReviews Collection ===');
  const reviewsSnap = await adminDb.collection('parentReviews').get();
  let reviewsFixed = 0;
  let rBatch = adminDb.batch();
  let rBatchOps = 0;

  const studentTopicReviews = new Map<string, any[]>();
  reviewsSnap.docs.forEach(doc => {
    const d = { _docId: doc.id, ...doc.data() as any };
    const sCode = d.studentCode || 'unknown';
    const tCode = d.topicCode || 'unknown';
    const key = `${sCode}___${tCode}`;
    if (!studentTopicReviews.has(key)) {
      studentTopicReviews.set(key, []);
    }
    studentTopicReviews.get(key)!.push(d);
  });

  for (const [key, items] of studentTopicReviews.entries()) {
    items.sort((a, b) => {
      const ta = a.startedAt?.toDate ? a.startedAt.toDate().getTime() : (a.createdAt?.toDate ? a.createdAt.toDate().getTime() : (new Date(a.createdAt || a.timestamp || 0).getTime()));
      const tb = b.startedAt?.toDate ? b.startedAt.toDate().getTime() : (b.createdAt?.toDate ? b.createdAt.toDate().getTime() : (new Date(b.createdAt || b.timestamp || 0).getTime()));
      return ta - tb;
    });

    for (let i = 0; i < items.length; i++) {
      const item = items[i];
      const practiceNumber = i + 1;
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

        if (!q.isDisputed && evalResult) {
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
      const rawCreated = item.createdAt?.toDate ? item.createdAt.toDate() : (item.createdAt ? new Date(item.createdAt) : new Date());
      const rawStarted = item.startedAt?.toDate ? item.startedAt.toDate() : (item.startedAt ? new Date(item.startedAt) : rawCreated);
      const timestamp = (rawCreated || rawStarted).toISOString();

      const docRef = adminDb.collection('parentReviews').doc(item._docId);
      const updateData: any = {
        practiceNumber,
        topicName: topicName || topicCode || 'Practice Session',
        subjectName,
        chapterName,
        timestamp,
        submittedAt: item.submittedAt || rawCreated,
        score: correctCount,
        totalMarks: validCount,
        percentage: scorePercent,
        correctCount,
        scorePercent,
        totalQuestions: validCount,
        examType: 'practice',
        type: 'practice',
        questions: reconciledQuestions,
        questionDetails: reconciledQuestions
      };

      rBatch.set(docRef, updateData, { merge: true });
      rBatchOps++;
      reviewsFixed++;

      if (rBatchOps >= 400) {
        await rBatch.commit();
        rBatch = adminDb.batch();
        rBatchOps = 0;
      }
    }
  }

  if (rBatchOps > 0) {
    await rBatch.commit();
  }
  console.log(`parentReviews collection: ${reviewsSnap.size} total docs, harmonized ${reviewsFixed} records.`);

  // 5. Audit & Fix formal exam reviews
  console.log('\n=== Step 5: Checking formal exam reviews Collection ===');
  const examReviewsSnap = await adminDb.collection('reviews').get();
  let examReviewsFixed = 0;
  let erBatch = adminDb.batch();
  let erBatchOps = 0;

  for (const doc of examReviewsSnap.docs) {
    const item = doc.data();
    const qDetails = Array.isArray(item.questionDetails) ? item.questionDetails : [];
    let hasChange = false;

    const reconciledQDetails = qDetails.map((q: any) => {
      const canonicalType = toCanonicalQuestionType(q.type);
      if (q.type !== canonicalType) hasChange = true;
      return {
        ...q,
        type: canonicalType
      };
    });

    if (hasChange) {
      erBatch.update(doc.ref, { questionDetails: reconciledQDetails });
      erBatchOps++;
      examReviewsFixed++;
      if (erBatchOps >= 400) {
        await erBatch.commit();
        erBatch = adminDb.batch();
        erBatchOps = 0;
      }
    }
  }

  if (erBatchOps > 0) {
    await erBatch.commit();
  }
  console.log(`reviews collection: ${examReviewsSnap.size} total docs, harmonized ${examReviewsFixed} records.`);

  console.log('\n🎉 ALL DATABASE RECORDS ARE 100% RECONCILED AND HARMONIZED!');
}

auditAndFixAllCollections()
  .then(() => process.exit(0))
  .catch(err => {
    console.error('Audit and fix failed:', err);
    process.exit(1);
  });

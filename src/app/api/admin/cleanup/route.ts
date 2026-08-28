import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    // 1. Fetch all active exams to build the "known exams" list
    const [objExamsSnap, subjExamsSnap] = await Promise.all([
      adminDb.collection('exams').get(),
      adminDb.collection('subjectiveExams').get()
    ]);

    const examDocIds = new Set<string>();
    const examCodes = new Set<string>();

    objExamsSnap.docs.forEach(doc => {
      examDocIds.add(doc.id);
      const data = doc.data();
      if (data.examCode) examCodes.add(data.examCode);
      if (data.examId) examCodes.add(data.examId);
    });

    subjExamsSnap.docs.forEach(doc => {
      examDocIds.add(doc.id);
      const data = doc.data();
      if (data.examCode) examCodes.add(data.examCode);
      if (data.examId) examCodes.add(data.examId);
    });

    const isKnownExam = (ref: string) => {
      if (!ref) return false;
      return examDocIds.has(ref) || examCodes.has(ref);
    };

    const isPracticeOrSyllabusRef = (ref: string) => {
      if (!ref) return false;
      const r = ref.toUpperCase().trim();
      if (r.startsWith('PRACTICE_') || r.includes('PRACTICE')) return true;
      const isSyllabusPattern = /^(CBSE|MH|NCERT|ICSE)-\d+-([A-Z0-9]+)-\d+/i.test(r);
      return isSyllabusPattern;
    };

    // 2. Fetch all collections to scan for orphans
    const [
      attemptsSnap,
      reviewsSnap,
      batchAssignmentsSnap,
      subjAttemptsSnap,
      subjReviewsSnap,
      subjAssignmentsSnap,
      peerAssignmentsSnap,
      masterySnap,
      profilesSnap,
      evalSnap,
      liveSessionsSnap
    ] = await Promise.all([
      adminDb.collection('examAttempts').get(),
      adminDb.collection('reviews').get(),
      adminDb.collection('batchAssignments').get(),
      adminDb.collection('subjectiveAttempts').get(),
      adminDb.collection('subjectiveReviews').get(),
      adminDb.collection('subjectiveAssignments').get(),
      adminDb.collection('peerAssignments').get(),
      adminDb.collection('studentTopicMastery').get(),
      adminDb.collection('studentProfiles').get(),
      adminDb.collection('evaluations').get(),
      adminDb.collection('liveExamSessions').get()
    ]);

    const orphanedData = {
      objectiveAttempts: [] as any[],
      objectiveReviews: [] as any[],
      objectiveAssignments: [] as any[],
      subjectiveAttempts: [] as any[],
      subjectiveReviews: [] as any[],
      subjectiveAssignments: [] as any[],
      peerAssignments: [] as any[],
      masteryRecordsToClearLink: [] as any[],
      orphanedProfiles: [] as any[],
      evaluations: [] as any[],
      liveSessions: [] as any[]
    };

    // Scan attempts
    attemptsSnap.docs.forEach(doc => {
      const d = doc.data();
      if (d.examId && !isKnownExam(d.examId) && !isPracticeOrSyllabusRef(d.examId)) {
        orphanedData.objectiveAttempts.push({ id: doc.id, examId: d.examId, studentCode: d.studentCode });
      }
    });

    // Scan reviews
    reviewsSnap.docs.forEach(doc => {
      const d = doc.data();
      const examRef = d.examId || doc.id.split('_')[0];
      if (examRef && !isKnownExam(examRef) && !isPracticeOrSyllabusRef(examRef)) {
        orphanedData.objectiveReviews.push({ id: doc.id, examId: examRef });
      }
    });

    // Scan assignments
    batchAssignmentsSnap.docs.forEach(doc => {
      const d = doc.data();
      if (d.examId && !isKnownExam(d.examId) && !isPracticeOrSyllabusRef(d.examId)) {
        orphanedData.objectiveAssignments.push({ id: doc.id, examId: d.examId });
      }
    });

    // Scan subjective attempts
    subjAttemptsSnap.docs.forEach(doc => {
      const d = doc.data();
      if (d.examId && !isKnownExam(d.examId) && !isPracticeOrSyllabusRef(d.examId)) {
        orphanedData.subjectiveAttempts.push({ id: doc.id, examId: d.examId });
      }
    });

    // Scan subjective reviews
    subjReviewsSnap.docs.forEach(doc => {
      const d = doc.data();
      if (d.examId && !isKnownExam(d.examId) && !isPracticeOrSyllabusRef(d.examId)) {
        orphanedData.subjectiveReviews.push({ id: doc.id, examId: d.examId });
      }
    });

    // Scan subjective assignments
    subjAssignmentsSnap.docs.forEach(doc => {
      const d = doc.data();
      if (d.examId && !isKnownExam(d.examId) && !isPracticeOrSyllabusRef(d.examId)) {
        orphanedData.subjectiveAssignments.push({ id: doc.id, examId: d.examId });
      }
    });

    // Scan peer assignments
    peerAssignmentsSnap.docs.forEach(doc => {
      const d = doc.data();
      if (d.examId && !isKnownExam(d.examId) && !isPracticeOrSyllabusRef(d.examId)) {
        orphanedData.peerAssignments.push({ id: doc.id, examId: d.examId });
      }
    });

    // Scan evaluations (orphaned if attemptId doesn't exist)
    const existingAttemptIds = new Set([
      ...attemptsSnap.docs.map(doc => doc.id),
      ...subjAttemptsSnap.docs.map(doc => doc.id)
    ]);

    evalSnap.docs.forEach(doc => {
      const d = doc.data();
      const attemptId = d.attemptId || d.legacyId || '';
      if (attemptId && !existingAttemptIds.has(attemptId) && !isPracticeOrSyllabusRef(attemptId)) {
        orphanedData.evaluations.push({ id: doc.id, attemptId });
      }
    });

    // Scan live sessions
    liveSessionsSnap.docs.forEach(doc => {
      const d = doc.data();
      if (d.examId && !isKnownExam(d.examId) && !isPracticeOrSyllabusRef(d.examId)) {
        orphanedData.liveSessions.push({ id: doc.id, examId: d.examId });
      }
    });

    // Scan studentTopicMastery (Mastery Records)
    // CRITICAL FIX: skip codes starting with PRACTICE_ (they are legitimate self-study practices, not exams)
    masterySnap.docs.forEach(doc => {
      const d = doc.data();
      const lastExamCode = d.lastExamCode;
      if (lastExamCode) {
        const isPractice = lastExamCode.startsWith('PRACTICE_');
        if (!isPractice && !isKnownExam(lastExamCode)) {
          orphanedData.masteryRecordsToClearLink.push({
            id: doc.id,
            studentCode: d.studentCode,
            topicCode: d.topicCode,
            lastExamCode
          });
        }
      }
    });

    // Scan stale profile caches
    const studentsWithMastery = new Set(masterySnap.docs.map(doc => doc.data().studentCode));
    profilesSnap.docs.forEach(doc => {
      const p = doc.data();
      const code = p.studentCode || doc.id;
      const hasStaleCache =
        (p.totalTopics || 0) > 0 ||
        (p.masteredTopics || 0) > 0 ||
        (p.needsAttentionTopics || 0) > 0 ||
        (p.overallMastery || 0) > 0;

      if (hasStaleCache && !studentsWithMastery.has(code)) {
        orphanedData.orphanedProfiles.push({ id: doc.id, studentCode: code });
      }
    });

    const totalOrphanedCount =
      orphanedData.objectiveAttempts.length +
      orphanedData.objectiveReviews.length +
      orphanedData.objectiveAssignments.length +
      orphanedData.subjectiveAttempts.length +
      orphanedData.subjectiveReviews.length +
      orphanedData.subjectiveAssignments.length +
      orphanedData.peerAssignments.length +
      orphanedData.evaluations.length +
      orphanedData.liveSessions.length +
      orphanedData.masteryRecordsToClearLink.length +
      orphanedData.orphanedProfiles.length;

    return NextResponse.json({
      success: true,
      counts: {
        objectiveExams: objExamsSnap.size,
        subjectiveExams: subjExamsSnap.size,
        totalOrphaned: totalOrphanedCount,
        objectiveAttempts: orphanedData.objectiveAttempts.length,
        objectiveReviews: orphanedData.objectiveReviews.length,
        objectiveAssignments: orphanedData.objectiveAssignments.length,
        subjectiveAttempts: orphanedData.subjectiveAttempts.length,
        subjectiveReviews: orphanedData.subjectiveReviews.length,
        subjectiveAssignments: orphanedData.subjectiveAssignments.length,
        peerAssignments: orphanedData.peerAssignments.length,
        evaluations: orphanedData.evaluations.length,
        liveSessions: orphanedData.liveSessions.length,
        masteryRecordsToClearLink: orphanedData.masteryRecordsToClearLink.length,
        orphanedProfiles: orphanedData.orphanedProfiles.length
      },
      orphanedData
    });
  } catch (err: any) {
    console.error('API get cleanup report error:', err);
    return NextResponse.json({ success: false, error: err.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { action, payload } = await req.json();

    if (action === 'cleanup') {
      const batch = new ChunkedBatch(adminDb);
      let count = 0;

      // 1. Delete standard orphaned collections
      const deleteCollections = [
        { key: 'objectiveAttempts', col: 'examAttempts' },
        { key: 'objectiveReviews', col: 'reviews' },
        { key: 'objectiveAssignments', col: 'batchAssignments' },
        { key: 'subjectiveAttempts', col: 'subjectiveAttempts' },
        { key: 'subjectiveReviews', col: 'subjectiveReviews' },
        { key: 'subjectiveAssignments', col: 'subjectiveAssignments' },
        { key: 'peerAssignments', col: 'peerAssignments' },
        { key: 'evaluations', col: 'evaluations' },
        { key: 'liveSessions', col: 'liveExamSessions' }
      ];

      for (const item of deleteCollections) {
        const list = payload?.[item.key] || [];
        list.forEach((docObj: any) => {
          batch.delete(adminDb.collection(item.col).doc(docObj.id));
          count++;
        });
      }

      // 2. Clear link on orphaned mastery records instead of deleting them (safe progress retention)
      const masteryList = payload?.masteryRecordsToClearLink || [];
      masteryList.forEach((docObj: any) => {
        batch.update(adminDb.collection('studentTopicMastery').doc(docObj.id), {
          lastExamCode: null
        });
        count++;
      });

      // 3. Reset stale cached profiles
      const profileList = payload?.orphanedProfiles || [];
      profileList.forEach((docObj: any) => {
        batch.update(adminDb.collection('studentProfiles').doc(docObj.id), {
          totalTopics: 0,
          masteredTopics: 0,
          needsAttentionTopics: 0,
          overallMastery: 0
        });
        count++;
      });

      await batch.commit();
      return NextResponse.json({ success: true, message: `Successfully cleaned up ${count} items.` });
    }

    if (action === 'fixSubjectiveRefs') {
      // Load all subjective exams to match by name
      const subjExamsSnap = await adminDb.collection('subjectiveExams').get();
      const examMap = new Map<string, any>();
      subjExamsSnap.docs.forEach(doc => {
        const data = doc.data();
        examMap.set(doc.id, data);
      });

      const batch = new ChunkedBatch(adminDb);
      let fixed = 0;

      // Scan and fix subjective attempts pointing to deleted exams with matching names
      const subjAttemptsSnap = await adminDb.collection('subjectiveAttempts').get();
      for (const doc of subjAttemptsSnap.docs) {
        const data = doc.data();
        if (data.examId && !examMap.has(data.examId)) {
          for (const [examId, examData] of examMap.entries()) {
            if (examData.name === data.examName) {
              batch.update(doc.ref, { examId });
              fixed++;
              break;
            }
          }
        }
      }

      // Scan and fix subjective reviews pointing to deleted exams
      const subjReviewsSnap = await adminDb.collection('subjectiveReviews').get();
      const neededAttemptIds = Array.from(new Set(
        subjReviewsSnap.docs
          .map(d => d.data())
          .filter(data => data.examId && !examMap.has(data.examId) && data.attemptId)
          .map(data => data.attemptId)
      )) as string[];

      const attemptMap = new Map<string, any>();
      if (neededAttemptIds.length > 0) {
        const attemptRefs = neededAttemptIds.map(id => adminDb.collection('subjectiveAttempts').doc(id));
        const attemptSnaps = await adminDb.getAll(...attemptRefs);
        attemptSnaps.forEach(snap => {
          if (snap.exists) {
            attemptMap.set(snap.id, snap.data());
          }
        });
      }

      for (const doc of subjReviewsSnap.docs) {
        const data = doc.data();
        if (data.examId && !examMap.has(data.examId)) {
          const attemptData = attemptMap.get(data.attemptId);
          if (attemptData) {
            if (attemptData.examId && examMap.has(attemptData.examId)) {
              batch.update(doc.ref, { examId: attemptData.examId });
              fixed++;
            }
          }
        }
      }

      await batch.commit();
      return NextResponse.json({ success: true, message: `Successfully repaired ${fixed} subjective exam references.` });
    }

    if (action === 'migrateLegacyQuestionTypes') {
      const batch = new ChunkedBatch(adminDb);
      let migratedCount = 0;
      let boardNormalizedCount = 0;

      // A. Migrate legacy question types (including subjective_5m)
      const questionsSnap = await adminDb.collection('questions')
        .where('type', 'in', ['numerical', 'subjective_1m', 'subjective_2m', 'subjective_3m', 'subjective_4m', 'subjective_5m'])
        .get();

      const typeMigrationMap: { [key: string]: string } = {
        numerical: 'numerical_short',
        subjective_1m: 'subjective_define',
        subjective_2m: 'subjective_short',
        subjective_3m: 'subjective_short',
        subjective_4m: 'subjective_long',
        subjective_5m: 'subjective_long'
      };

      questionsSnap.docs.forEach(doc => {
        const data = doc.data();
        const oldType = data.type;
        const newType = typeMigrationMap[oldType];
        if (newType) {
          batch.update(doc.ref, { type: newType });
          migratedCount++;
        }
      });

      // B. Normalize Board names in questions (MSBSHSE / MH -> Maharashtra Board)
      const questionsBoardSnap1 = await adminDb.collection('questions').where('board', '==', 'MSBSHSE').get();
      questionsBoardSnap1.docs.forEach(doc => {
        batch.update(doc.ref, { board: 'Maharashtra Board' });
        boardNormalizedCount++;
      });

      const questionsBoardSnap2 = await adminDb.collection('questions').where('board', '==', 'MH').get();
      questionsBoardSnap2.docs.forEach(doc => {
        batch.update(doc.ref, { board: 'Maharashtra Board' });
        boardNormalizedCount++;
      });

      // C. Normalize Board names in syllabus (MSBSHSE / MH -> Maharashtra Board)
      const syllabusBoardSnap1 = await adminDb.collection('syllabus').where('board', '==', 'MSBSHSE').get();
      syllabusBoardSnap1.docs.forEach(doc => {
        batch.update(doc.ref, { board: 'Maharashtra Board' });
        boardNormalizedCount++;
      });

      const syllabusBoardSnap2 = await adminDb.collection('syllabus').where('board', '==', 'MH').get();
      syllabusBoardSnap2.docs.forEach(doc => {
        batch.update(doc.ref, { board: 'Maharashtra Board' });
        boardNormalizedCount++;
      });

      // D. Normalize boardCode in syllabusTopicIndex (MSBSHSE -> MH)
      const topicIndexSnap = await adminDb.collection('syllabusTopicIndex').where('boardCode', '==', 'MSBSHSE').get();
      topicIndexSnap.docs.forEach(doc => {
        batch.update(doc.ref, { boardCode: 'MH' });
        boardNormalizedCount++;
      });

      await batch.commit();
      return NextResponse.json({ 
        success: true, 
        message: `Successfully migrated ${migratedCount} legacy questions, and normalized ${boardNormalizedCount} board references.` 
      });
    }
    return NextResponse.json({ success: false, error: 'Invalid cleanup action' }, { status: 400 });
  } catch (err: any) {
    console.error('API cleanup processing error:', err);
    return NextResponse.json({ success: false, error: err.message || 'Internal Server Error' }, { status: 500 });
  }
}

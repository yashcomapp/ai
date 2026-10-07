import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { AttemptService } from './attempt.service';
import { ProctoringViolations } from '@/types/attempt.types';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';
import { MasteryService } from './mastery.service';
import { invalidateCache } from '@/lib/firebase/cache';
import { ReportCacheManager } from '@/lib/reportCache';

export class ExamService {
  /**
   * Helper to fetch active assignments targeted specifically to a student (by batch or direct assignment),
   * avoiding full collection scans across tens of thousands of active assignments.
   */
  private static async fetchStudentActiveAssignments(studentCode: string, studentBatchIds: string[]): Promise<{
    objAssignments: admin.firestore.QueryDocumentSnapshot[];
    subAssignments: admin.firestore.QueryDocumentSnapshot[];
  }> {
    const batchList = (studentBatchIds || []).filter(Boolean);
    const batchChunks: string[][] = [];
    for (let i = 0; i < batchList.length; i += 30) {
      batchChunks.push(batchList.slice(i, i + 30));
    }

    const objPromises: Promise<admin.firestore.QuerySnapshot>[] = [];
    const subPromises: Promise<admin.firestore.QuerySnapshot>[] = [];

    // 1. Batch-targeted assignments
    batchChunks.forEach(chunk => {
      objPromises.push(
        adminDb.collection('batchAssignments')
          .where('status', '==', 'active')
          .where('targetBatches', 'array-contains-any', chunk)
          .get()
      );
      subPromises.push(
        adminDb.collection('subjectiveAssignments')
          .where('status', '==', 'active')
          .where('targetBatches', 'array-contains-any', chunk)
          .get()
      );
    });

    // 2. Student-specific assignments
    if (studentCode) {
      objPromises.push(
        adminDb.collection('batchAssignments')
          .where('status', '==', 'active')
          .where('targetStudents', 'array-contains', studentCode)
          .get()
      );
      subPromises.push(
        adminDb.collection('subjectiveAssignments')
          .where('status', '==', 'active')
          .where('targetStudents', 'array-contains', studentCode)
          .get()
      );
    }

    const [objSnaps, subSnaps] = await Promise.all([
      Promise.all(objPromises),
      Promise.all(subPromises)
    ]);

    const seenObjDocIds = new Set<string>();
    const objDocs: admin.firestore.QueryDocumentSnapshot[] = [];
    objSnaps.forEach(snap => {
      snap.docs.forEach(d => {
        if (!seenObjDocIds.has(d.id)) {
          seenObjDocIds.add(d.id);
          objDocs.push(d);
        }
      });
    });

    const seenSubDocIds = new Set<string>();
    const subDocs: admin.firestore.QueryDocumentSnapshot[] = [];
    subSnaps.forEach(snap => {
      snap.docs.forEach(d => {
        if (!seenSubDocIds.has(d.id)) {
          seenSubDocIds.add(d.id);
          subDocs.push(d);
        }
      });
    });

    return { objAssignments: objDocs, subAssignments: subDocs };
  }

  /**
   * Checks whether the student has any unattempted and unacknowledged past scheduled exams.
   * Batches all lookups to prevent N+1 queries and targets assignments to student.
   */
  static async verifyStudentPastExamAbsenceBlock(params: {
    studentCode: string;
    studentBatchIds: string[];
    currentExamId: string;
    evalMap?: Set<string> | Map<string, any>;
    isAutonomous?: boolean;
  }): Promise<{ blocked: boolean; examTitle?: string; message?: string }> {
    const { studentCode, studentBatchIds, currentExamId, evalMap, isAutonomous } = params;
    
    // Autonomous students do not have active parent accounts to acknowledge absences
    if (isAutonomous) {
      return { blocked: false };
    }

    const now = new Date();

    const { objAssignments, subAssignments } = await this.fetchStudentActiveAssignments(studentCode, studentBatchIds);

    const pastAssignedExams: Array<{ examId: string; endAt: Date }> = [];
    const seenExamIds = new Set<string>();

    const collectPast = (docs: admin.firestore.QueryDocumentSnapshot[]) => {
      docs.forEach(doc => {
        const data = doc.data();
        if (!data.examId || data.examId === currentExamId || seenExamIds.has(data.examId)) return;
        const targetType = data.targetType;
        const isTargeted = targetType === 'student'
          ? (Array.isArray(data.targetStudents) && data.targetStudents.includes(studentCode))
          : (Array.isArray(data.targetBatches) && data.targetBatches.some((b: string) => studentBatchIds.includes(b)));

        if (isTargeted && data.endAt) {
          const endAtDate = data.endAt.toDate ? data.endAt.toDate() : new Date(data.endAt);
          if (now > endAtDate) {
            seenExamIds.add(data.examId);
            pastAssignedExams.push({ examId: data.examId, endAt: endAtDate });
          }
        }
      });
    };

    collectPast(objAssignments);
    collectPast(subAssignments);

    if (pastAssignedExams.length === 0) {
      return { blocked: false };
    }

    // Step 1: Batch-fetch all direct doc references in 1 round-trip
    const directDocRefs: admin.firestore.DocumentReference[] = [];
    pastAssignedExams.forEach(pe => {
      directDocRefs.push(adminDb.collection('examAttempts').doc(`${pe.examId}_${studentCode}`));
      directDocRefs.push(adminDb.collection('subjectiveAttempts').doc(`${pe.examId}_${studentCode}`));
      directDocRefs.push(adminDb.collection('examAbsenceReasons').doc(`${studentCode}_${pe.examId}`));
    });

    const directDocSnaps = await adminDb.getAll(...directDocRefs);
    const snapMap = new Map<string, admin.firestore.DocumentSnapshot>();
    directDocSnaps.forEach(snap => {
      snapMap.set(snap.ref.path, snap);
    });

    // Check which exams are already satisfied
    const unverifiedPastExams: typeof pastAssignedExams = [];

    for (const pastExam of pastAssignedExams) {
      const attemptSnap = snapMap.get(`examAttempts/${pastExam.examId}_${studentCode}`);
      const subAttemptSnap = snapMap.get(`subjectiveAttempts/${pastExam.examId}_${studentCode}`);
      const reasonSnap = snapMap.get(`examAbsenceReasons/${studentCode}_${pastExam.examId}`);

      const directAttempted = (attemptSnap?.exists && attemptSnap.data()?.status !== 'precheck') ||
                              (subAttemptSnap?.exists && subAttemptSnap.data()?.status !== 'precheck') ||
                              (evalMap && evalMap.has(pastExam.examId));

      if (directAttempted) {
        continue;
      }

      const isReasonAcknowledged = reasonSnap?.exists && (reasonSnap.data()?.acknowledgedByParent === true || !!reasonSnap.data()?.reason);
      if (isReasonAcknowledged) {
        continue;
      }

      unverifiedPastExams.push(pastExam);
    }

    if (unverifiedPastExams.length === 0) {
      return { blocked: false };
    }

    // Step 2: For any exams still unverified, check query-based attempts / reviews in batched 'in' chunks (up to 30)
    const unverifiedIds = unverifiedPastExams.map(pe => pe.examId);
    const attemptedExamIds = new Set<string>();

    for (let i = 0; i < unverifiedIds.length; i += 30) {
      const chunk = unverifiedIds.slice(i, i + 30);
      const [qAttemptsSnap, qReviewsSnap, qSubSnap, qEvalSnap] = await Promise.all([
        adminDb.collection('examAttempts').where('studentCode', '==', studentCode).where('examId', 'in', chunk).get(),
        adminDb.collection('reviews').where('studentCode', '==', studentCode).where('examId', 'in', chunk).get(),
        adminDb.collection('subjectiveAttempts').where('studentCode', '==', studentCode).where('examId', 'in', chunk).get(),
        adminDb.collection('evaluations').where('studentCode', '==', studentCode).where('examId', 'in', chunk).get()
      ]);

      qAttemptsSnap.docs.forEach(d => {
        if (d.data()?.status !== 'precheck') attemptedExamIds.add(d.data().examId);
      });
      qReviewsSnap.docs.forEach(d => {
        if (d.data()?.status !== 'precheck') attemptedExamIds.add(d.data().examId);
      });
      qSubSnap.docs.forEach(d => {
        if (d.data()?.status !== 'precheck') attemptedExamIds.add(d.data().examId);
      });
      qEvalSnap.docs.forEach(d => {
        const dt = d.data();
        if (dt?.examId) attemptedExamIds.add(dt.examId);
      });
    }

    const strictlyMissed = unverifiedPastExams.filter(pe => !attemptedExamIds.has(pe.examId));
    if (strictlyMissed.length > 0) {
      const firstMissed = strictlyMissed[0];
      let pastExamTitle = firstMissed.examId;
      try {
        const [eDoc, sDoc] = await Promise.all([
          adminDb.collection('exams').doc(firstMissed.examId).get(),
          adminDb.collection('subjectiveExams').doc(firstMissed.examId).get()
        ]);
        if (eDoc.exists) {
          pastExamTitle = eDoc.data()?.name || eDoc.data()?.title || firstMissed.examId;
        } else if (sDoc.exists) {
          pastExamTitle = sDoc.data()?.name || sDoc.data()?.title || firstMissed.examId;
        }
      } catch {}

      return {
        blocked: true,
        examTitle: pastExamTitle,
        message: `You missed your scheduled exam '${pastExamTitle}'. You are blocked from taking new exams until your parent reviews and acknowledges this absence in the Parent Portal.`
      };
    }

    return { blocked: false };
  }

  /**
   * Discovers and compiles absent exam review items for a student.
   * Batches all reads using adminDb.getAll and chunked queries.
   */
  static async getStudentPastExamAbsenceReviews(params: {
    studentCode: string;
    studentBatchIds: string[];
    objSnaps?: admin.firestore.QuerySnapshot | { docs: any[] };
    subjSnaps?: admin.firestore.QuerySnapshot | { docs: any[] };
    evalSnaps?: admin.firestore.QuerySnapshot | { docs: any[] };
  }): Promise<Array<{
    id: string;
    examId: string;
    type: 'absent_exam';
    name: string;
    subject: string;
    chapter: string;
    date: string;
    status: 'approved' | 'pending';
    isAbsent: true;
    reason: string | null;
    reviewedByActor: 'parent' | null;
  }>> {
    const { studentCode, studentBatchIds, objSnaps, subjSnaps, evalSnaps } = params;
    const now = new Date();

    const { objAssignments, subAssignments } = await this.fetchStudentActiveAssignments(studentCode, studentBatchIds);

    const pastAssignedExams: Array<{ examId: string; endAt: Date; collection: string }> = [];
    const seenExamIds = new Set<string>();

    const collectPast = (docs: admin.firestore.QueryDocumentSnapshot[], col: string) => {
      docs.forEach(doc => {
        const data = doc.data();
        if (!data.examId || seenExamIds.has(data.examId)) return;
        const targetType = data.targetType;
        const isTargeted = targetType === 'student'
          ? (Array.isArray(data.targetStudents) && data.targetStudents.includes(studentCode))
          : (Array.isArray(data.targetBatches) && data.targetBatches.some((b: string) => studentBatchIds.includes(b)));

        if (isTargeted && data.endAt) {
          const endAtDate = data.endAt.toDate ? data.endAt.toDate() : new Date(data.endAt);
          if (now > endAtDate) {
            seenExamIds.add(data.examId);
            pastAssignedExams.push({ examId: data.examId, endAt: endAtDate, collection: col });
          }
        }
      });
    };

    collectPast(objAssignments, 'batchAssignments');
    collectPast(subAssignments, 'subjectiveAssignments');

    if (pastAssignedExams.length === 0) return [];

    const unverifiedPastExams = pastAssignedExams.filter(pe => {
      const hasObjReview = objSnaps?.docs.some(d => {
        const dData = d.data();
        return dData.examId === pe.examId || d.id === `${pe.examId}_${studentCode}` || d.id.includes(pe.examId);
      });
      const hasSubjAttempt = subjSnaps?.docs.some(d => {
        const dData = d.data();
        return dData.examId === pe.examId || d.id === `${pe.examId}_${studentCode}` || d.id.includes(pe.examId);
      });
      const hasEvaluation = evalSnaps?.docs.some(d => {
        const dData = d.data();
        return dData.examId === pe.examId || (dData.legacyId && dData.legacyId.includes(pe.examId));
      });
      return !hasObjReview && !hasSubjAttempt && !hasEvaluation;
    });

    if (unverifiedPastExams.length === 0) return [];

    const docRefs: admin.firestore.DocumentReference[] = [];
    const examDocRefs: admin.firestore.DocumentReference[] = [];
    unverifiedPastExams.forEach(pe => {
      docRefs.push(adminDb.collection('examAttempts').doc(`${pe.examId}_${studentCode}`));
      docRefs.push(adminDb.collection('subjectiveAttempts').doc(`${pe.examId}_${studentCode}`));
      docRefs.push(adminDb.collection('examAbsenceReasons').doc(`${studentCode}_${pe.examId}`));
      examDocRefs.push(adminDb.collection(pe.collection === 'batchAssignments' ? 'exams' : 'subjectiveExams').doc(pe.examId));
    });

    const [allDocs, allExamDocs] = await Promise.all([
      docRefs.length > 0 ? adminDb.getAll(...docRefs).catch(() => []) : [],
      examDocRefs.length > 0 ? adminDb.getAll(...examDocRefs).catch(() => []) : []
    ]);

    const docMap = new Map<string, any>();
    allDocs.forEach(d => {
      if (d && d.exists) docMap.set(`${d.ref.parent.id}/${d.id}`, d.data());
    });

    const examDataMap = new Map<string, any>();
    allExamDocs.forEach(d => {
      if (d && d.exists) examDataMap.set(d.id, d.data());
    });

    const candidateExamIds = unverifiedPastExams.map(pe => pe.examId);
    const attemptedExamIds = new Set<string>();

    for (let i = 0; i < candidateExamIds.length; i += 30) {
      const chunk = candidateExamIds.slice(i, i + 30);
      const [qAttSnap, qRevSnap, qSubSnap, qEvalSnap] = await Promise.all([
        adminDb.collection('examAttempts').where('studentCode', '==', studentCode).where('examId', 'in', chunk).get(),
        adminDb.collection('reviews').where('studentCode', '==', studentCode).where('examId', 'in', chunk).get(),
        adminDb.collection('subjectiveAttempts').where('studentCode', '==', studentCode).where('examId', 'in', chunk).get(),
        adminDb.collection('evaluations').where('studentCode', '==', studentCode).where('examId', 'in', chunk).get()
      ]);
      qAttSnap.docs.forEach(d => {
        if (d.data()?.status !== 'precheck') attemptedExamIds.add(d.data().examId);
      });
      qRevSnap.docs.forEach(d => {
        if (d.data()?.status !== 'precheck') attemptedExamIds.add(d.data().examId);
      });
      qSubSnap.docs.forEach(d => {
        if (d.data()?.status !== 'precheck') attemptedExamIds.add(d.data().examId);
      });
      qEvalSnap.docs.forEach(d => {
        const dt = d.data();
        if (dt?.examId) attemptedExamIds.add(dt.examId);
      });
    }

    const absentReviews: any[] = [];
    unverifiedPastExams.forEach(pastExam => {
      const directAtt = docMap.get(`examAttempts/${pastExam.examId}_${studentCode}`);
      const directSub = docMap.get(`subjectiveAttempts/${pastExam.examId}_${studentCode}`);
      const attempted = (directAtt && directAtt.status !== 'precheck') ||
                        (directSub && directSub.status !== 'precheck') ||
                        attemptedExamIds.has(pastExam.examId);

      if (!attempted) {
        const reasonData = docMap.get(`examAbsenceReasons/${studentCode}_${pastExam.examId}`);
        const isReasonAcknowledged = reasonData && (reasonData.acknowledgedByParent === true || !!reasonData.reason);
        const eData = examDataMap.get(pastExam.examId);
        const pastExamTitle = eData?.name || eData?.title || pastExam.examId;
        const subject = eData?.subject || eData?.subjectName || (eData?.subjects ? eData.subjects[0] : 'General');
        const chapter = eData?.chapter || eData?.chapterName || '-';

        absentReviews.push({
          id: `absent_${pastExam.examId}_${studentCode}`,
          examId: pastExam.examId,
          type: 'absent_exam' as const,
          name: `${pastExamTitle} (Missed / Absent)`,
          subject,
          chapter,
          date: pastExam.endAt.toISOString(),
          status: isReasonAcknowledged ? 'approved' as const : 'pending' as const,
          isAbsent: true as const,
          reason: reasonData?.reason || null,
          reviewedByActor: isReasonAcknowledged ? 'parent' as const : null
        });
      }
    });

    return absentReviews;
  }

  /**
   * Delegates MCQ exam submission evaluation to AttemptService.
   */
  static async submitExam(params: {
    studentCode: string;
    studentId: string;
    studentName: string;
    examId: string;
    examData: any;
    questions: any[];
    userAnswers: any[];
    durationSpent: number;
    tabViolations: number;
    proctoringViolations: ProctoringViolations;
    startedAt: string | null;
    assignmentsSnap: admin.firestore.QuerySnapshot | null;
    proctoringViolationTriggered?: boolean;
    micBypassed?: boolean;
    violations?: any;
    abandoned?: boolean;
    disputedQuestionIds?: string[];
    isLate?: boolean;
  }) {
    return AttemptService.submitAttempt(params);
  }

  /**
   * Permanently deletes an exam and purges ALL downstream mutations caused by it:
   * 1. The exam document (exams or subjectiveExams)
   * 2. All batchAssignments, subjectiveAssignments, and legacy assignments
   * 3. All examAttempts, subjectiveAttempts
   * 4. All reviews, subjectiveReviews
   * 5. All evaluations
   * 6. All peerAssignments
   * 7. All examAbsenceReasons
   * 8. All notices linked to this exam
   * 9. Reverts and recalculates studentTopicMastery for every affected student and topic:
   *    - If no other surviving exam attempts or practices exist for that topic, deletes the studentTopicMastery doc entirely (releasing the topic from student's learning page, dashboard, and mastery counts).
   *    - If other surviving exam attempts or practices exist, recalculates mastery based purely on surviving records.
   * 10. Releases all candidate questions back into the Question Bank:
   *     - For questions not used by any other surviving active exam, sets usedInClassroomTest = false and timesUsed = 0.
   * 11. Re-syncs class exam sequence counters.
   * 12. Invalidates all student, admin, and report caches.
   */
  static async deleteExamCompletely(examId: string, preferredType?: string): Promise<{
    success: boolean;
    examId: string;
    examName: string;
    deletedCount: number;
    details: {
      examDocs: number;
      assignments: number;
      attempts: number;
      reviews: number;
      evaluations: number;
      peerAssignments: number;
      notices: number;
      absenceReasons: number;
      masteryDeleted: number;
      masteryRecalculated: number;
      questionsReleased: number;
    };
  }> {
    if (!examId) throw new Error('Missing examId parameter.');

    // Step 1: Fetch target exam doc from exams or subjectiveExams
    const [objExamSnap, subjExamSnap] = await Promise.all([
      adminDb.collection('exams').doc(examId).get(),
      adminDb.collection('subjectiveExams').doc(examId).get()
    ]);

    const targetExamDoc = objExamSnap.exists ? objExamSnap : (subjExamSnap.exists ? subjExamSnap : null);
    const targetExamData = targetExamDoc ? targetExamDoc.data() : null;
    const examName = targetExamData?.name || targetExamData?.title || examId;

    // Step 2: Collect Candidate Question Codes & Affected Topics from Exam Definition
    const candidateQuestionCodes = new Set<string>();
    const affectedTopicCodes = new Set<string>();

    const addQuestionCode = (c: any) => {
      if (!c) return;
      const str = String(c).trim();
      if (str) {
        candidateQuestionCodes.add(str);
        const derived = deriveTopicCodeFromQuestionCode(str);
        if (derived && derived.includes('-')) affectedTopicCodes.add(derived);
      }
    };

    if (targetExamData) {
      (targetExamData.questionCodes || []).forEach(addQuestionCode);
      (targetExamData.questionIds || []).forEach(addQuestionCode);
      if (Array.isArray(targetExamData.questions)) {
        targetExamData.questions.forEach((q: any) => {
          if (typeof q === 'string') addQuestionCode(q);
          else if (q && typeof q === 'object') {
            if (q.id) addQuestionCode(q.id);
            if (q.questionCode) addQuestionCode(q.questionCode);
            if (q.topicCode) affectedTopicCodes.add(String(q.topicCode).trim());
          }
        });
      }
      if (targetExamData.topicCode) affectedTopicCodes.add(String(targetExamData.topicCode).trim());
      if (Array.isArray(targetExamData.topicCodes)) {
        targetExamData.topicCodes.forEach((tc: any) => { if (tc) affectedTopicCodes.add(String(tc).trim()); });
      }
    }

    // Step 3: Query all related documents across collections in parallel
    const [
      objAttemptsSnap,
      subjAttemptsSnap,
      reviewsSnap,
      subjReviewsSnap,
      evalsSnap,
      peerAssignSnap,
      objAssignSnap,
      subjAssignSnap,
      noticesSnap,
      absenceSnap
    ] = await Promise.all([
      adminDb.collection('examAttempts').where('examId', '==', examId).get(),
      adminDb.collection('subjectiveAttempts').where('examId', '==', examId).get(),
      adminDb.collection('reviews').where('examId', '==', examId).get(),
      adminDb.collection('subjectiveReviews').where('examId', '==', examId).get(),
      adminDb.collection('evaluations').where('examId', '==', examId).get(),
      adminDb.collection('peerAssignments').where('examId', '==', examId).get(),
      adminDb.collection('batchAssignments').where('examId', '==', examId).get(),
      adminDb.collection('subjectiveAssignments').where('examId', '==', examId).get(),
      adminDb.collection('notices').where('examId', '==', examId).get(),
      adminDb.collection('examAbsenceReasons').where('examId', '==', examId).get().catch(() => ({ docs: [] } as any))
    ]);

    // Harvest studentCodes, extra questions, and topics from attempts & reviews
    const affectedStudentCodes = new Set<string>();

    const processReviewOrAttempt = (doc: admin.firestore.QueryDocumentSnapshot) => {
      const data = doc.data();
      if (data.studentCode) affectedStudentCodes.add(String(data.studentCode).trim());
      if (data.revieweeCode) affectedStudentCodes.add(String(data.revieweeCode).trim());
      if (data.reviewerStudentCode) affectedStudentCodes.add(String(data.reviewerStudentCode).trim());

      const details = data.questionDetails || [];
      details.forEach((qd: any) => {
        if (qd.id) addQuestionCode(qd.id);
        if (qd.questionCode) addQuestionCode(qd.questionCode);
        if (qd.topicCode) affectedTopicCodes.add(String(qd.topicCode).trim());
      });
    };

    objAttemptsSnap.docs.forEach(processReviewOrAttempt);
    subjAttemptsSnap.docs.forEach(processReviewOrAttempt);
    reviewsSnap.docs.forEach(processReviewOrAttempt);
    subjReviewsSnap.docs.forEach(processReviewOrAttempt);

    evalsSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.studentCode) affectedStudentCodes.add(String(data.studentCode).trim());
      const qReviews = data.questionReviews || [];
      qReviews.forEach((qr: any) => {
        if (qr.questionId) addQuestionCode(qr.questionId);
        if (qr.questionCode) addQuestionCode(qr.questionCode);
        if (qr.topicCode) affectedTopicCodes.add(String(qr.topicCode).trim());
      });
    });

    peerAssignSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.reviewerStudentCode) affectedStudentCodes.add(String(data.reviewerStudentCode).trim());
      if (data.revieweeStudentCode) affectedStudentCodes.add(String(data.revieweeStudentCode).trim());
    });

    objAssignSnap.docs.forEach(doc => {
      const data = doc.data();
      if (Array.isArray(data.targetStudents)) {
        data.targetStudents.forEach((sc: string) => affectedStudentCodes.add(String(sc).trim()));
      }
    });

    subjAssignSnap.docs.forEach(doc => {
      const data = doc.data();
      if (Array.isArray(data.targetStudents)) {
        data.targetStudents.forEach((sc: string) => affectedStudentCodes.add(String(sc).trim()));
      }
    });

    // Step 4: Batch Delete All Direct Exam Artifacts
    const batch = new ChunkedBatch(adminDb);
    let examDocsDeleted = 0;

    if (objExamSnap.exists) {
      batch.delete(objExamSnap.ref);
      examDocsDeleted++;
    }
    if (subjExamSnap.exists) {
      batch.delete(subjExamSnap.ref);
      examDocsDeleted++;
    }

    const assignmentsDeleted = objAssignSnap.size + subjAssignSnap.size;
    objAssignSnap.docs.forEach(d => batch.delete(d.ref));
    subjAssignSnap.docs.forEach(d => batch.delete(d.ref));

    const attemptsDeleted = objAttemptsSnap.size + subjAttemptsSnap.size;
    objAttemptsSnap.docs.forEach(d => batch.delete(d.ref));
    subjAttemptsSnap.docs.forEach(d => batch.delete(d.ref));

    const reviewsDeleted = reviewsSnap.size + subjReviewsSnap.size;
    reviewsSnap.docs.forEach(d => batch.delete(d.ref));
    subjReviewsSnap.docs.forEach(d => batch.delete(d.ref));

    const evaluationsDeleted = evalsSnap.size;
    evalsSnap.docs.forEach(d => batch.delete(d.ref));

    const peerAssignmentsDeleted = peerAssignSnap.size;
    peerAssignSnap.docs.forEach(d => batch.delete(d.ref));

    const noticesDeleted = noticesSnap.size;
    noticesSnap.docs.forEach(d => batch.delete(d.ref));

    const absenceReasonsDeleted = absenceSnap.docs.length;
    absenceSnap.docs.forEach((d: any) => batch.delete(d.ref));

    // Also ensure composite IDs `${examId}_${studentCode}` are queued for deletion
    for (const sc of Array.from(affectedStudentCodes)) {
      batch.delete(adminDb.collection('examAttempts').doc(`${examId}_${sc}`));
      batch.delete(adminDb.collection('reviews').doc(`${examId}_${sc}`));
      batch.delete(adminDb.collection('subjectiveAttempts').doc(`${examId}_${sc}`));
      batch.delete(adminDb.collection('subjectiveReviews').doc(`${examId}_${sc}`));
      batch.delete(adminDb.collection('examAbsenceReasons').doc(`${sc}_${examId}`));
    }

    await batch.commit();

    // Step 5: Recalculate or Purge Topic Mastery for All Affected Students
    let totalMasteryDeleted = 0;
    let totalMasteryRecalculated = 0;
    const candidateTopicArray = Array.from(affectedTopicCodes);

    for (const studentCode of Array.from(affectedStudentCodes)) {
      try {
        const { deletedCount, updatedCount } = await MasteryService.recalculateOrPurgeTopicsForStudent({
          studentCode,
          excludedExamId: examId,
          candidateTopicCodes: candidateTopicArray
        });
        totalMasteryDeleted += deletedCount;
        totalMasteryRecalculated += updatedCount;
      } catch (masteryErr) {
        console.warn(`Mastery cleanup warning for student ${studentCode}:`, masteryErr);
      }
    }

    // Step 6: Release Candidate Questions Back to Question Bank
    let questionsReleasedCount = 0;
    const uniqueCandidateCodes = Array.from(candidateQuestionCodes);

    if (uniqueCandidateCodes.length > 0) {
      try {
        const [otherObjExamsSnap, otherSubjExamsSnap] = await Promise.all([
          adminDb.collection('exams').select('questionCodes', 'questionIds', 'questions').get(),
          adminDb.collection('subjectiveExams').select('questionCodes', 'questionIds', 'questions').get()
        ]);

        const otherActiveQuestions = new Set<string>();
        const indexOtherExam = (doc: admin.firestore.QueryDocumentSnapshot) => {
          if (doc.id === examId) return;
          const edata = doc.data();
          (edata.questionCodes || []).forEach((c: any) => { if (c) otherActiveQuestions.add(String(c).trim()); });
          (edata.questionIds || []).forEach((c: any) => { if (c) otherActiveQuestions.add(String(c).trim()); });
          if (Array.isArray(edata.questions)) {
            edata.questions.forEach((q: any) => {
              if (typeof q === 'string') otherActiveQuestions.add(q.trim());
              else if (q && typeof q === 'object') {
                if (q.id) otherActiveQuestions.add(String(q.id).trim());
                if (q.questionCode) otherActiveQuestions.add(String(q.questionCode).trim());
              }
            });
          }
        };

        otherObjExamsSnap.docs.forEach(indexOtherExam);
        otherSubjExamsSnap.docs.forEach(indexOtherExam);

        const codesToRelease = uniqueCandidateCodes.filter(c => !otherActiveQuestions.has(c));
        const codesToDecrement = uniqueCandidateCodes.filter(c => otherActiveQuestions.has(c));

        const releaseBatch = new ChunkedBatch(adminDb);

        // Fully release unused questions
        for (const code of codesToRelease) {
          releaseBatch.set(adminDb.collection('questions').doc(code), {
            usedInClassroomTest: false,
            timesUsed: 0
          }, { merge: true });
        }

        for (let i = 0; i < codesToRelease.length; i += 30) {
          const chunk = codesToRelease.slice(i, i + 30);
          try {
            const matchedSnap = await adminDb.collection('questions')
              .where('questionCode', 'in', chunk)
              .get();
            matchedSnap.docs.forEach(qDoc => {
              releaseBatch.set(qDoc.ref, {
                usedInClassroomTest: false,
                timesUsed: 0
              }, { merge: true });
            });
          } catch (mErr) {
            console.warn('Matched question release lookup warning:', mErr);
          }
        }

        // Decrement timesUsed for questions that remain in other surviving exams
        for (const code of codesToDecrement) {
          releaseBatch.set(adminDb.collection('questions').doc(code), {
            timesUsed: admin.firestore.FieldValue.increment(-1)
          }, { merge: true });
        }

        await releaseBatch.commit();
        questionsReleasedCount = codesToRelease.length;
      } catch (relErr) {
        console.warn('Failed to release questions during exam delete:', relErr);
      }
    }

    // Step 7: Auto Re-sync Class Exam Counters
    try {
      await ExamService.reSyncClassExamCounters();
    } catch (e) {
      console.warn('Error auto re-syncing exam counters after delete:', e);
    }

    // Step 8: Invalidate Admin & Report Caches
    try {
      invalidateCache('admin_dashboard_');
      invalidateCache('admin_students_list');
      invalidateCache('qb_base_');
      await Promise.all([
        ReportCacheManager.invalidateReport(`exam-report-objective-${examId}`),
        ReportCacheManager.invalidateReport(`exam-report-subjective-${examId}`),
        ReportCacheManager.invalidateReport(`truth-test-report-${examId}`)
      ]);
    } catch {}

    const totalDeleted = examDocsDeleted + assignmentsDeleted + attemptsDeleted + reviewsDeleted + evaluationsDeleted + peerAssignmentsDeleted + noticesDeleted + absenceReasonsDeleted + totalMasteryDeleted;

    return {
      success: true,
      examId,
      examName,
      deletedCount: totalDeleted,
      details: {
        examDocs: examDocsDeleted,
        assignments: assignmentsDeleted,
        attempts: attemptsDeleted,
        reviews: reviewsDeleted,
        evaluations: evaluationsDeleted,
        peerAssignments: peerAssignmentsDeleted,
        notices: noticesDeleted,
        absenceReasons: absenceReasonsDeleted,
        masteryDeleted: totalMasteryDeleted,
        masteryRecalculated: totalMasteryRecalculated,
        questionsReleased: questionsReleasedCount
      }
    };
  }

  /**
   * Helper to re-sync exam sequence counters per class based on active exams
   */
  static async reSyncClassExamCounters() {
    const classes = ['6', '7', '8', '9', '10', '11', '12'];
    
    const [objDocs, subjDocs] = await Promise.all([
      adminDb.collection('exams').select('class', 'sequence', 'name').get(),
      adminDb.collection('subjectiveExams').select('class', 'sequence', 'name').get()
    ]);

    const classMaxSeq: Record<string, number> = {};

    const processDoc = (data: any) => {
      const classNum = String(data.class || '').trim();
      if (!classNum) return;

      let seq = Number(data.sequence) || 0;
      if (!seq && data.name) {
        const match = data.name.match(/^(\d{3})-/);
        if (match) {
          seq = parseInt(match[1], 10);
        }
      }

      if (seq > 0) {
        classMaxSeq[classNum] = Math.max(classMaxSeq[classNum] || 0, seq);
      }
    };

    objDocs.docs.forEach(doc => processDoc(doc.data()));
    subjDocs.docs.forEach(doc => processDoc(doc.data()));

    const batch = adminDb.batch();
    classes.forEach(cNum => {
      const maxS = classMaxSeq[cNum] || 0;
      const ref = adminDb.collection('examCounters').doc(`class-${cNum}`);
      batch.set(ref, { nextSequence: maxS + 1 }, { merge: true });
    });

    await batch.commit();
  }

  /**
   * Resets all past attempts, reviews, evaluations, absence records, and mastery
   * for an exam when it is reassigned or assigned again.
   * Ensures start counts drop to 0 and all students can take the exam cleanly.
   */
  static async resetExamAttemptsAndRecordsForReassignment(params: {
    examId: string;
    type?: 'objective' | 'subjective';
    targetType?: 'batch' | 'student' | 'mixed';
    targetStudents?: string[];
  }): Promise<{
    success: boolean;
    examId: string;
    attemptsDeleted: number;
    reviewsDeleted: number;
    evaluationsDeleted: number;
    absenceReasonsDeleted: number;
    masteryRecalculated: number;
  }> {
    const { examId, type = 'objective', targetType = 'batch', targetStudents = [] } = params;
    if (!examId) throw new Error('Missing examId parameter.');

    // 1. Fetch exam details to derive candidate topics
    const [objExamSnap, subjExamSnap] = await Promise.all([
      adminDb.collection('exams').doc(examId).get(),
      adminDb.collection('subjectiveExams').doc(examId).get()
    ]);

    const targetExamDoc = objExamSnap.exists ? objExamSnap : (subjExamSnap.exists ? subjExamSnap : null);
    const targetExamData = targetExamDoc ? targetExamDoc.data() : null;

    const affectedTopicCodes = new Set<string>();
    if (targetExamData) {
      if (targetExamData.topicCode) affectedTopicCodes.add(String(targetExamData.topicCode).trim());
      if (Array.isArray(targetExamData.topicCodes)) {
        targetExamData.topicCodes.forEach((tc: any) => { if (tc) affectedTopicCodes.add(String(tc).trim()); });
      }
      if (Array.isArray(targetExamData.questions)) {
        targetExamData.questions.forEach((q: any) => {
          if (q && typeof q === 'object' && q.topicCode) {
            affectedTopicCodes.add(String(q.topicCode).trim());
          }
        });
      }
    }

    // 2. Query attempts, reviews, evaluations, absence reasons, and peer assignments
    const [
      objAttemptsSnap,
      subjAttemptsSnap,
      reviewsSnap,
      subjReviewsSnap,
      evalsSnap,
      peerAssignSnap,
      absenceSnap
    ] = await Promise.all([
      adminDb.collection('examAttempts').where('examId', '==', examId).get(),
      adminDb.collection('subjectiveAttempts').where('examId', '==', examId).get(),
      adminDb.collection('reviews').where('examId', '==', examId).get(),
      adminDb.collection('subjectiveReviews').where('examId', '==', examId).get(),
      adminDb.collection('evaluations').where('examId', '==', examId).get(),
      adminDb.collection('peerAssignments').where('examId', '==', examId).get(),
      adminDb.collection('examAbsenceReasons').where('examId', '==', examId).get().catch(() => ({ docs: [] } as any))
    ]);

    const isSpecificStudentFilter = targetType === 'student' && targetStudents.length > 0;
    const filterSet = isSpecificStudentFilter ? new Set(targetStudents.map(s => String(s).trim())) : null;

    const affectedStudentCodes = new Set<string>();
    if (filterSet) {
      filterSet.forEach(sc => affectedStudentCodes.add(sc));
    }

    const shouldDeleteDoc = (data: any, docId: string): boolean => {
      const sc = data?.studentCode || (docId.includes('_') ? docId.split('_').slice(1).join('_') : '');
      if (sc) affectedStudentCodes.add(sc);
      if (!filterSet) return true;
      return filterSet.has(sc) || filterSet.has(docId);
    };

    const batch = new ChunkedBatch(adminDb);
    let attemptsDeleted = 0;
    let reviewsDeleted = 0;
    let evaluationsDeleted = 0;
    let absenceReasonsDeleted = 0;

    objAttemptsSnap.docs.forEach(doc => {
      if (shouldDeleteDoc(doc.data(), doc.id)) {
        batch.delete(doc.ref);
        attemptsDeleted++;
      }
    });

    subjAttemptsSnap.docs.forEach(doc => {
      if (shouldDeleteDoc(doc.data(), doc.id)) {
        batch.delete(doc.ref);
        attemptsDeleted++;
      }
    });

    reviewsSnap.docs.forEach(doc => {
      if (shouldDeleteDoc(doc.data(), doc.id)) {
        batch.delete(doc.ref);
        reviewsDeleted++;
      }
    });

    subjReviewsSnap.docs.forEach(doc => {
      if (shouldDeleteDoc(doc.data(), doc.id)) {
        batch.delete(doc.ref);
        reviewsDeleted++;
      }
    });

    evalsSnap.docs.forEach(doc => {
      if (shouldDeleteDoc(doc.data(), doc.id)) {
        batch.delete(doc.ref);
        evaluationsDeleted++;
      }
    });

    peerAssignSnap.docs.forEach(doc => {
      if (shouldDeleteDoc(doc.data(), doc.id)) {
        batch.delete(doc.ref);
      }
    });

    absenceSnap.docs.forEach((doc: any) => {
      if (shouldDeleteDoc(doc.data(), doc.id)) {
        batch.delete(doc.ref);
        absenceReasonsDeleted++;
      }
    });

    // Also explicitly delete composite doc IDs for all affected student codes
    for (const sc of Array.from(affectedStudentCodes)) {
      batch.delete(adminDb.collection('examAttempts').doc(`${examId}_${sc}`));
      batch.delete(adminDb.collection('subjectiveAttempts').doc(`${examId}_${sc}`));
      batch.delete(adminDb.collection('reviews').doc(`${examId}_${sc}`));
      batch.delete(adminDb.collection('subjectiveReviews').doc(`${examId}_${sc}`));
      batch.delete(adminDb.collection('examAbsenceReasons').doc(`${sc}_${examId}`));
    }

    await batch.commit();

    // Recalculate or purge topic mastery for affected students
    let masteryRecalculated = 0;
    const candidateTopicArray = Array.from(affectedTopicCodes);

    for (const studentCode of Array.from(affectedStudentCodes)) {
      try {
        const { updatedCount } = await MasteryService.recalculateOrPurgeTopicsForStudent({
          studentCode,
          excludedExamId: examId,
          candidateTopicCodes: candidateTopicArray
        });
        masteryRecalculated += updatedCount;
      } catch (err) {
        console.warn(`Mastery recalculation warning for student ${studentCode} during reassignment reset:`, err);
      }
    }

    // Invalidate caches
    try {
      invalidateCache('admin_dashboard_');
      invalidateCache('admin_students_list');
      await Promise.all([
        ReportCacheManager.invalidateReport(`exam-report-objective-${examId}`),
        ReportCacheManager.invalidateReport(`exam-report-subjective-${examId}`),
        ReportCacheManager.invalidateReport(`truth-test-report-${examId}`)
      ]);
    } catch {}

    return {
      success: true,
      examId,
      attemptsDeleted,
      reviewsDeleted,
      evaluationsDeleted,
      absenceReasonsDeleted,
      masteryRecalculated
    };
  }
}

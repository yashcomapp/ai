import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { AttemptService } from './attempt.service';
import { ProctoringViolations } from '@/types/attempt.types';

export class ExamService {
  /**
   * Checks whether the student has any unattempted and unacknowledged past scheduled exams.
   * Batches all lookups to prevent N+1 queries.
   */
  static async verifyStudentPastExamAbsenceBlock(params: {
    studentCode: string;
    studentBatchIds: string[];
    currentExamId: string;
    evalMap?: Set<string> | Map<string, any>;
  }): Promise<{ blocked: boolean; examTitle?: string; message?: string }> {
    const { studentCode, studentBatchIds, currentExamId, evalMap } = params;
    const now = new Date();

    const [allObjAssignmentsSnap, allSubAssignmentsSnap] = await Promise.all([
      adminDb.collection('batchAssignments').where('status', '==', 'active').get(),
      adminDb.collection('subjectiveAssignments').where('status', '==', 'active').get()
    ]);

    const pastAssignedExams: Array<{ examId: string; endAt: Date }> = [];
    const seenExamIds = new Set<string>();

    const collectPast = (snap: admin.firestore.QuerySnapshot) => {
      snap.docs.forEach(doc => {
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

    collectPast(allObjAssignmentsSnap);
    collectPast(allSubAssignmentsSnap);

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
      const [qAttemptsSnap, qReviewsSnap, qSubSnap] = await Promise.all([
        adminDb.collection('examAttempts').where('studentCode', '==', studentCode).where('examId', 'in', chunk).get(),
        adminDb.collection('reviews').where('studentCode', '==', studentCode).where('examId', 'in', chunk).get(),
        adminDb.collection('subjectiveAttempts').where('studentCode', '==', studentCode).where('examId', 'in', chunk).get()
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
  }) {
    return AttemptService.submitAttempt(params);
  }
}

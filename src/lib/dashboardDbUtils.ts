import { adminDb } from '@/lib/firebase/admin';
import { getDateKeyIST } from '@/lib/dateUtils';
import { deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';

/**
 * Deduplicate assignments by examId to prevent double-counting across batch & student-specific assignments.
 */
export function deduplicateAssignments(assignmentDocs: any[]): Map<string, any> {
  const uniqueAssignments = new Map<string, any>();
  assignmentDocs.forEach((doc: any) => {
    const d = typeof doc.data === 'function' ? doc.data() : doc;
    const examId = d.examId;
    if (examId) {
      if (d.examType === 'entrance') return; // Skip entrance exams from absent statistics
      const currentEndAt = d.endAt?.toDate ? d.endAt.toDate() : new Date(d.endAt);
      const existing = uniqueAssignments.get(examId);
      if (!existing || currentEndAt > existing.endAt) {
        uniqueAssignments.set(examId, {
          id: doc.id || examId,
          ...d,
          examId,
          endAt: currentEndAt,
          examType: d.examType || (doc.ref?.parent?.id?.includes('subjective') ? 'subjective' : 'objective')
        });
      }
    }
  });
  return uniqueAssignments;
}

/**
 * Resolves the student's latest integrity compliance score (0-100%) from Firestore snapshots.
 */
export function resolveIntegrityScore(integritySnapshot: any): { integrityScore: number; latestRecord: any | null } {
  if (!integritySnapshot || integritySnapshot.empty) {
    return { integrityScore: 100, latestRecord: null };
  }

  const records = integritySnapshot.docs.map((doc: any) => doc.data());
  records.sort((a: any, b: any) => {
    const ad = a.weekStart?.toDate ? a.weekStart.toDate() : new Date(a.weekStart || 0);
    const bd = b.weekStart?.toDate ? b.weekStart.toDate() : new Date(b.weekStart || 0);
    return bd.getTime() - ad.getTime();
  });

  const latest = records[0];
  const score = typeof latest?.integrityScore === 'number' ? latest.integrityScore : (typeof latest?.overallScore === 'number' ? latest.overallScore : 100);
  return { integrityScore: score, latestRecord: latest };
}

/**
 * Computes today and weekly time aggregations and study streak from user time logs.
 */
export function calculateTimeLogSummary(timeLogDocs: any[]) {
  let todaySeconds = 0;
  let todayExamSeconds = 0;
  let todayPracticeSeconds = 0;
  let todayReviewSeconds = 0;
  let todayGeneralSeconds = 0;

  let weekSeconds = 0;
  let weekExamSeconds = 0;
  let weekPracticeSeconds = 0;
  let weekReviewSeconds = 0;
  let weekGeneralSeconds = 0;

  const todayStr = getDateKeyIST(new Date());

  timeLogDocs.forEach((doc: any) => {
    const d = typeof doc.data === 'function' ? doc.data() : doc;
    const s = Number(d.seconds) || 0;
    const ex = Number(d.examSeconds) || 0;
    const pr = Number(d.practiceSeconds) || 0;
    const rv = Number(d.reviewSeconds) || 0;
    const gen = Math.max(0, s - (ex + pr + rv));

    if (d.date === todayStr) {
      todaySeconds = s;
      todayExamSeconds = ex;
      todayPracticeSeconds = pr;
      todayReviewSeconds = rv;
      todayGeneralSeconds = gen;
    }
  });

  for (let i = 0; i < 7; i++) {
    const dateObj = new Date();
    dateObj.setDate(dateObj.getDate() - i);
    const k = getDateKeyIST(dateObj);
    const match = timeLogDocs.find((doc: any) => {
      const data = typeof doc.data === 'function' ? doc.data() : doc;
      return data.date === k;
    });
    if (match) {
      const data = typeof match.data === 'function' ? match.data() : match;
      const s = Number(data.seconds) || 0;
      const ex = Number(data.examSeconds) || 0;
      const pr = Number(data.practiceSeconds) || 0;
      const rv = Number(data.reviewSeconds) || 0;
      const gen = Math.max(0, s - (ex + pr + rv));
      weekSeconds += s;
      weekExamSeconds += ex;
      weekPracticeSeconds += pr;
      weekReviewSeconds += rv;
      weekGeneralSeconds += gen;
    }
  }

  let streakDays = 0;
  const d = new Date();
  while (streakDays < 100) {
    const key = getDateKeyIST(d);
    const matchDoc = timeLogDocs.find((doc: any) => {
      const data = typeof doc.data === 'function' ? doc.data() : doc;
      return data.date === key;
    });
    const matchData = matchDoc ? (typeof matchDoc.data === 'function' ? matchDoc.data() : matchDoc) : null;
    if (!matchData || !(matchData.seconds > 0)) break;
    streakDays++;
    d.setDate(d.getDate() - 1);
  }

  return {
    todaySeconds,
    todayExamSeconds,
    todayPracticeSeconds,
    todayReviewSeconds,
    todayGeneralSeconds,
    weekSeconds,
    weekExamSeconds,
    weekPracticeSeconds,
    weekReviewSeconds,
    weekGeneralSeconds,
    streakDays
  };
}

/**
 * Extracts and maps canonical topic codes from objective or subjective exam dictionaries.
 */
export function extractTopicCodesFromExams(examsMap: Map<string, any>, allTopicCodes: Set<string>) {
  examsMap.forEach((examData) => {
    let topicCode = '';
    if (Array.isArray(examData.topicCodes) && examData.topicCodes.length > 0) {
      topicCode = examData.topicCodes[0];
    } else {
      const qIds = examData.questionIds || [];
      if (qIds.length > 0) {
        topicCode = deriveTopicCodeFromQuestionCode(qIds[0]);
      }
    }
    if (topicCode) {
      allTopicCodes.add(topicCode);
      examData.resolvedTopicCode = topicCode;
    }
  });
}

/**
 * SSOT for resolving all valid, active studentCodes linked to a parent account.
 * Searches explicit studentCodes array, studentCode field, and queries user accounts
 * by parentEmail and parentPhone with role === 'student'.
 */
export async function resolveParentStudentCodes(parentData: any): Promise<string[]> {
  const studentCodes: string[] = [];
  if (Array.isArray(parentData?.studentCodes)) {
    parentData.studentCodes.forEach((code: any) => {
      if (typeof code === 'string' && code.startsWith('ST-')) {
        studentCodes.push(code);
      }
    });
  }
  if (typeof parentData?.studentCode === 'string' && parentData.studentCode.startsWith('ST-')) {
    if (!studentCodes.includes(parentData.studentCode)) {
      studentCodes.push(parentData.studentCode);
    }
  }

  const parentEmail = parentData?.email?.toLowerCase();
  const parentPhone = parentData?.phone || parentData?.parentPhone || parentData?.mobile;
  if (parentEmail || parentPhone) {
    try {
      const [emailSnap, phoneSnap] = await Promise.all([
        parentEmail
          ? adminDb.collection('users')
              .where('role', '==', 'student')
              .where('parentEmail', '==', parentEmail)
              .get()
              .catch(() => ({ docs: [] } as any))
          : Promise.resolve({ docs: [] } as any),
        parentPhone
          ? adminDb.collection('users')
              .where('role', '==', 'student')
              .where('parentPhone', '==', parentPhone)
              .get()
              .catch(() => ({ docs: [] } as any))
          : Promise.resolve({ docs: [] } as any)
      ]);

      emailSnap.docs.forEach((doc: any) => {
        const data = doc.data();
        if (data.status !== 'inactive' && typeof data.studentCode === 'string' && data.studentCode.startsWith('ST-') && !studentCodes.includes(data.studentCode)) {
          studentCodes.push(data.studentCode);
        }
      });
      phoneSnap.docs.forEach((doc: any) => {
        const data = doc.data();
        if (data.status !== 'inactive' && typeof data.studentCode === 'string' && data.studentCode.startsWith('ST-') && !studentCodes.includes(data.studentCode)) {
          studentCodes.push(data.studentCode);
        }
      });
    } catch (err) {
      console.warn('Error resolving parent student codes:', err);
    }
  }

  const uniqueCodes = Array.from(new Set(studentCodes.filter(Boolean)));
  if (uniqueCodes.length === 0) return [];

  // Filter out any deactivated student accounts
  const chunks: string[][] = [];
  for (let i = 0; i < uniqueCodes.length; i += 30) {
    chunks.push(uniqueCodes.slice(i, i + 30));
  }
  const activeCodes: string[] = [];
  await Promise.all(chunks.map(async chunk => {
    const snap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .where('studentCode', 'in', chunk)
      .get()
      .catch(() => ({ docs: [] } as any));
    snap.docs.forEach((d: any) => {
      const sData = d.data();
      if (sData.status !== 'inactive' && sData.studentCode) {
        activeCodes.push(sData.studentCode);
      }
    });
  }));

  return Array.from(new Set(activeCodes));
}


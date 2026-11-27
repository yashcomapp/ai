import { adminDb } from '@/lib/firebase/admin';
import { getCachedSyllabus, invalidateCache } from '@/lib/firebase/cache';
import { getCanonicalBoardCode, getCanonicalClass, getCanonicalSubjectCode } from '@/lib/syllabusUtils';

export const SYLLABUS_STATS_COLLECTION = 'syllabusStats';
export const SYLLABUS_STATS_VERSION = 1;

export interface VaultCounts {
  exam: { objective: number; subjective: number };
  practice: { objective: number; subjective: number };
  foundation: { objective: number; subjective: number };
}

export interface ChapterStatsEntry {
  vaultCounts: VaultCounts;
  totalTopicsCount: number;
  conductedTopicsCount: number;
  examStatus: 'all_conducted' | 'partial_conducted' | 'unconducted';
  testsCount: number;
}

export interface TopicStatsEntry {
  vaultCounts: VaultCounts;
  testsCount: number;
}

export interface SyllabusStatsDoc {
  version: number;
  docId: string;
  boardCode: string;
  class: string;
  subjectCode: string;
  questionsStale: boolean;
  examsStale: boolean;
  updatedAt: number;
  chapters: Record<string, ChapterStatsEntry>;
  topics: Record<string, TopicStatsEntry>;
}

/**
 * Applies pre-computed stats from syllabusStats/{docId} onto a syllabus document's
 * chapters/topics/subtopics for the requested activeVault.
 */
export function applySyllabusStatsToSubjectDoc(
  subjectData: any,
  stats: SyllabusStatsDoc,
  activeVault: 'exam' | 'practice' | 'foundation'
) {
  const bCode = getCanonicalBoardCode(subjectData.boardCode || subjectData.board || '');
  const cls = getCanonicalClass(subjectData.class);
  const sCode = getCanonicalSubjectCode(bCode, cls, subjectData.subjectCode || subjectData.subject || '');
  const canonicalTopicPrefix = `${bCode}-${cls}-${sCode}`;

  const chapters = Array.isArray(subjectData.chapters) ? subjectData.chapters : [];
  chapters.forEach((chap: any) => {
    if (!chap || typeof chap !== 'object') return;
    const chapNumStr = String(chap.number ?? '').trim();
    const chapStats = stats.chapters?.[chapNumStr];

    if (chapStats) {
      chap.vaultCounts = chapStats.vaultCounts;
      chap.objectiveCount = chapStats.vaultCounts?.[activeVault]?.objective ?? 0;
      chap.subjectiveCount = chapStats.vaultCounts?.[activeVault]?.subjective ?? 0;
      chap.testsCount = chapStats.testsCount ?? 0;
      chap.totalTopicsCount = chapStats.totalTopicsCount ?? 0;
      chap.conductedTopicsCount = chapStats.conductedTopicsCount ?? 0;
      chap.examStatus = chapStats.examStatus ?? 'unconducted';
    }

    const topics = Array.isArray(chap.topics) ? chap.topics : [];
    topics.forEach((top: any) => {
      if (!top || typeof top !== 'object') return;
      const topNumStr = String(top.number ?? '').trim();
      const cleanTopicCode = String(top.topicCode || `${canonicalTopicPrefix}-${chapNumStr}-${topNumStr}`).trim();
      const topStats = stats.topics?.[cleanTopicCode] || stats.topics?.[`${chapNumStr}:${topNumStr}`];

      if (topStats) {
        top.vaultCounts = topStats.vaultCounts;
        top.objectiveCount = topStats.vaultCounts?.[activeVault]?.objective ?? 0;
        top.subjectiveCount = topStats.vaultCounts?.[activeVault]?.subjective ?? 0;
        top.testsCount = topStats.testsCount ?? 0;
      }

      const rawSubtopics = Array.isArray(top.subtopics) ? top.subtopics : [];
      top.subtopics = rawSubtopics.map((sub: any, subIdx: number) => {
        const subObj =
          typeof sub === 'string'
            ? {
                name: sub,
                number: `${topNumStr}.${subIdx + 1}`,
                subtopicNumber: `${topNumStr}.${subIdx + 1}`,
                subtopicCode: `${cleanTopicCode}.${subIdx + 1}`,
                objectiveCount: 0,
                subjectiveCount: 0,
              }
            : sub;

        if (!subObj || typeof subObj !== 'object') return subObj;
        const subNumStr = String(subObj.number ?? '').trim();
        const cleanSubCode = String(
          subObj.subtopicCode || subObj.topicCode || `${canonicalTopicPrefix}-${chapNumStr}-${subNumStr}`
        ).trim();
        const subStats = stats.topics?.[cleanSubCode] || stats.topics?.[`${chapNumStr}:${subNumStr}`];

        if (subStats) {
          subObj.vaultCounts = subStats.vaultCounts;
          subObj.objectiveCount = subStats.vaultCounts?.[activeVault]?.objective ?? 0;
          subObj.subjectiveCount = subStats.vaultCounts?.[activeVault]?.subjective ?? 0;
          subObj.testsCount = subStats.testsCount ?? 0;
        }
        return subObj;
      });
    });
  });

  return subjectData;
}

/**
 * Marks matching syllabusStats documents as stale so they recompute incrementally
 * on next access without forcing a full-collection question scan on exam changes.
 */
export async function markSyllabusStatsStale(opts: {
  type: 'exams' | 'questions' | 'all';
  docId?: string;
  boardCode?: string;
  classNum?: string | number;
  subjectCode?: string;
}) {
  try {
    invalidateCache('syllabus-all');

    const updatePayload: Record<string, any> = {
      updatedAt: Date.now(),
    };
    if (opts.type === 'exams' || opts.type === 'all') updatePayload.examsStale = true;
    if (opts.type === 'questions' || opts.type === 'all') updatePayload.questionsStale = true;

    if (opts.docId) {
      await adminDb
        .collection(SYLLABUS_STATS_COLLECTION)
        .doc(opts.docId)
        .set(updatePayload, { merge: true });
      return;
    }

    const syllabusSnap = await getCachedSyllabus();
    const targetBoard = opts.boardCode ? getCanonicalBoardCode(opts.boardCode) : '';
    const targetClass = opts.classNum !== undefined && opts.classNum !== '' ? getCanonicalClass(opts.classNum) : '';
    const targetSubj =
      targetBoard && targetClass && opts.subjectCode
        ? getCanonicalSubjectCode(targetBoard, targetClass, opts.subjectCode)
        : '';

    const matchingDocIds: string[] = [];
    syllabusSnap.docs.forEach((doc: any) => {
      const data = typeof doc.data === 'function' ? doc.data() : doc;
      const bCode = getCanonicalBoardCode(data.boardCode || data.board || '');
      const cls = getCanonicalClass(data.class);
      const sCode = getCanonicalSubjectCode(bCode, cls, data.subjectCode || data.subject || '');

      if (targetBoard && bCode !== targetBoard) return;
      if (targetClass && cls !== targetClass) return;
      if (targetSubj && sCode !== targetSubj) return;
      matchingDocIds.push(doc.id);
    });

    if (matchingDocIds.length === 0) return;

    const batch = adminDb.batch();
    matchingDocIds.forEach(id => {
      batch.set(adminDb.collection(SYLLABUS_STATS_COLLECTION).doc(id), updatePayload, { merge: true });
    });
    await batch.commit();
  } catch (err) {
    console.warn('[syllabusStats] Failed to mark stats stale:', err);
  }
}

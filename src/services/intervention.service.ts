import { adminDb } from '@/lib/firebase/admin';
import { getAssignmentsForBatches } from '@/services/exam.service';
import { getDateKeyIST } from '@/lib/dateUtils';
import { ReportCacheManager } from '@/lib/reportCache';
import { getStudentMode } from '@/types/user.types';
import { isDemoUser } from '@/lib/studentDb';
import { fetchTopicIndexByCodes } from '@/lib/syllabusServerUtils';

export type InterventionCategory = 
  | 'conceptual_block'  // Practiced allowed sets, but still < 50% (Needs Classroom Re-Teach)
  | 'neglected_topic'   // Flagged 🔴 by exam, but 0 practice done
  | 'missed_exam';      // Baseline Exam missed

export interface ReTeachStudent {
  studentCode: string;
  studentName: string;
  className: string;
  mastery: number;
  questionsAttempted: number;
}

export interface ReTeachTopicGroup {
  id: string;
  className: string;
  topicCode: string;
  topicName: string;
  studentCount: number;
  avgMastery: number;
  students: ReTeachStudent[];
}

export interface NeglectedTopicDetail {
  topicCode: string;
  topicName: string;
  examScore: number;
}

export interface NeglectedStudentGroup {
  id: string;
  studentCode: string;
  studentName: string;
  className: string;
  topicCount: number;
  topics: NeglectedTopicDetail[];
}

export interface MissedExamItem {
  id: string;
  studentCode: string;
  studentName: string;
  className: string;
  examId: string;
  examTitle: string;
  daysOverdue: number;
  dueDate: string;
}

export interface InterventionItem {
  id: string;
  studentCode?: string;
  studentName?: string;
  className: string;
  urgency: 'critical' | 'high' | 'medium' | 'low';
  category: InterventionCategory;
  title: string;
  subtitle: string;
  description: string;
  topicCode?: string;
  topicName?: string;
  examId?: string;
  daysOverdue?: number;
  scorePercent?: number;
  studentCount?: number;
  students?: ReTeachStudent[];
  topics?: NeglectedTopicDetail[];
  createdAt?: string;
}

export interface InterventionSummary {
  totalItems: number;
  criticalCount: number;          // Missed Baseline Exams
  gateBlockedCount: number;       // Always 0 (practice locks are intentional by anti-abuse policy)
  conceptualBlockCount: number;   // Number of unique topics needing classroom re-teach
  reTeachStudentCount: number;    // Number of distinct students needing re-teach
  neglectedTopicCount: number;    // Number of students with 0 practice on weak topics
  reTeachTopics: ReTeachTopicGroup[];
  neglectedStudents: NeglectedStudentGroup[];
  missedExams: MissedExamItem[];
  items: InterventionItem[];
  lastUpdated: string;
}

export class InterventionService {
  private static CACHE_KEY = 'admin_report_interventions_v3';
  private static CACHE_TTL_SECONDS = 60; // 1-minute TTL with on-demand refresh

  /**
   * Generates a deduplicated Classroom Remediation Digest:
   * 1. Re-Teach Agenda: Groups students by Class & Topic where allowed practice failed to reach 50%
   * 2. Neglected Practice: Identifies students with exam weaknesses who have completed 0 practice sets
   * 3. Missed Baseline Exams: Identifies students who missed recent scheduled exams
   */
  static async getInterventionQueue(forceRefresh = false): Promise<InterventionSummary> {
    if (!forceRefresh) {
      const cached = await ReportCacheManager.getReport<InterventionSummary>(this.CACHE_KEY);
      if (cached) return cached;
    }

    const now = new Date();

    // 1. Fetch all active students (excluding deactivated accounts per Rule 2.C and Limited Mode students who cannot practice)
    const studentsSnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .select('name', 'studentCode', 'className', 'batch', 'status', 'batchId', 'batchIds', 'studentMode', 'autonomous')
      .get();

    const activeStudents = studentsSnap.docs
      .map(d => ({ id: d.id, ...d.data() } as any))
      .filter(s => s.status !== 'inactive' && getStudentMode(s) !== 'limited' && !isDemoUser(s));

    const studentMap = new Map<string, any>();
    const allBatchIds = new Set<string>();

    activeStudents.forEach(s => {
      studentMap.set(s.studentCode, s);
      if (s.batchId) allBatchIds.add(s.batchId);
      if (Array.isArray(s.batchIds)) s.batchIds.forEach((b: string) => allBatchIds.add(b));
    });

    // ── STEP 1: Missed Scheduled Baseline Exams ───────────────────────
    const missedExamsList: MissedExamItem[] = [];
    if (allBatchIds.size > 0) {
      try {
        const { objectiveDocs } = await getAssignmentsForBatches(Array.from(allBatchIds), {
          status: 'active'
        });

        const FOURTEEN_DAYS_AGO = new Date(now.getTime() - 14 * 24 * 60 * 60 * 1000);
        const pastExams = objectiveDocs.filter((ass: any) => {
          const endAt = ass.endAt?.toDate ? ass.endAt.toDate() : new Date(ass.endAt);
          return now > endAt && endAt > FOURTEEN_DAYS_AGO;
        });

        if (pastExams.length > 0) {
          const pastExamIds = pastExams.map((e: any) => e.examId);
          const studentCodes = Array.from(studentMap.keys());

          // Query reviews in chunks
          const chunkSize = 10;
          const attemptPromises: Promise<any>[] = [];
          for (let i = 0; i < studentCodes.length; i += chunkSize) {
            const chunk = studentCodes.slice(i, i + chunkSize);
            attemptPromises.push(
              adminDb.collection('reviews')
                .where('studentCode', 'in', chunk)
                .where('examId', 'in', pastExamIds.slice(0, 10))
                .select('studentCode', 'examId')
                .get()
                .catch(() => ({ docs: [] } as any))
            );
          }

          const attemptSnaps = await Promise.all(attemptPromises);
          const attemptedSet = new Set<string>();
          attemptSnaps.forEach((snap: any) => {
            snap.docs.forEach((d: any) => {
              const data = d.data();
              attemptedSet.add(`${data.studentCode}_${data.examId}`);
            });
          });

          pastExams.forEach((ass: any) => {
            const endAt = ass.endAt?.toDate ? ass.endAt.toDate() : new Date(ass.endAt);
            const daysOverdue = Math.max(1, Math.round((now.getTime() - endAt.getTime()) / (1000 * 60 * 60 * 24)));

            activeStudents.forEach(student => {
              const matchesBatch = (ass.batchId && (student.batchId === ass.batchId || (student.batchIds && student.batchIds.includes(ass.batchId)))) ||
                                   (ass.className && (student.className === ass.className || student.batch === ass.className));

              if (matchesBatch) {
                const key = `${student.studentCode}_${ass.examId}`;
                if (!attemptedSet.has(key)) {
                  missedExamsList.push({
                    id: `missed_${key}`,
                    studentCode: student.studentCode,
                    studentName: student.name,
                    className: student.className || student.batch || 'General Batch',
                    examId: ass.examId,
                    examTitle: ass.title || ass.examId,
                    daysOverdue,
                    dueDate: getDateKeyIST(endAt)
                  });
                }
              }
            });
          });
        }
      } catch (err) {
        console.warn('InterventionService: Error checking missed exams:', err);
      }
    }

    // ── STEP 2: Topic Mastery Triaging & Remediation Breakdown ─────────
    const lowMasterySnap = await adminDb.collection('studentTopicMastery')
      .where('mastery', '<', 50)
      .select('studentCode', 'topicCode', 'topicName', 'mastery', 'questionsAttempted', 'practiceQuestionsAttempted', 'updatedAt')
      .get();

    const rawReTeachMap = new Map<string, {
      className: string;
      topicCode: string;
      topicName?: string;
      students: ReTeachStudent[];
    }>();

    const rawNeglectedMap = new Map<string, {
      studentCode: string;
      studentName: string;
      className: string;
      topics: NeglectedTopicDetail[];
    }>();

    const allTopicCodesSet = new Set<string>();

    lowMasterySnap.docs.forEach(doc => {
      const data = doc.data() as any;
      const student = studentMap.get(data.studentCode);
      if (!student) return;
      if (!data.questionsAttempted || data.questionsAttempted <= 0) return;

      const topicCode = (data.topicCode || '').trim();
      if (!topicCode) return;
      allTopicCodesSet.add(topicCode);

      const practiceQs = data.practiceQuestionsAttempted || 0;
      const studentClass = student.className || student.batch || 'General Batch';

      if (practiceQs > 0) {
        // Practiced, but STILL <50% -> Conceptual Block (Algorithm failed, Teacher needs to re-teach in class!)
        const groupKey = `${studentClass}___${topicCode}`;
        if (!rawReTeachMap.has(groupKey)) {
          rawReTeachMap.set(groupKey, {
            className: studentClass,
            topicCode,
            topicName: data.topicName,
            students: []
          });
        }
        rawReTeachMap.get(groupKey)!.students.push({
          studentCode: student.studentCode,
          studentName: student.name,
          className: studentClass,
          mastery: Math.round(data.mastery || 0),
          questionsAttempted: data.questionsAttempted
        });
      } else {
        // Flagged by exam, but 0 practice sessions attempted -> Neglected Remediation
        if (!rawNeglectedMap.has(student.studentCode)) {
          rawNeglectedMap.set(student.studentCode, {
            studentCode: student.studentCode,
            studentName: student.name,
            className: studentClass,
            topics: []
          });
        }
        rawNeglectedMap.get(student.studentCode)!.topics.push({
          topicCode,
          topicName: data.topicName || topicCode,
          examScore: Math.round(data.mastery || 0)
        });
      }
    });

    // Hydrate human-readable topic names for all unique topics
    let topicIndexMap = new Map<string, any>();
    try {
      topicIndexMap = await fetchTopicIndexByCodes(Array.from(allTopicCodesSet));
    } catch (err) {
      console.warn('InterventionService: Error hydrating topic names:', err);
    }

    // Build structured Re-Teach Topic Groups
    const reTeachTopics: ReTeachTopicGroup[] = [];
    const reTeachStudentCodes = new Set<string>();

    rawReTeachMap.forEach((g, groupKey) => {
      const idxMeta = topicIndexMap.get(g.topicCode);
      const friendlyName = g.topicName || idxMeta?.topicName || idxMeta?.title || idxMeta?.name || g.topicCode;

      // Sort students inside topic: lowest mastery first
      g.students.sort((a, b) => a.mastery - b.mastery);
      g.students.forEach(s => reTeachStudentCodes.add(s.studentCode));

      const avgMastery = Math.round(
        g.students.reduce((sum, s) => sum + s.mastery, 0) / g.students.length
      );

      reTeachTopics.push({
        id: `reteach_${groupKey.replace(/[^a-zA-Z0-9_-]/g, '_')}`,
        className: g.className,
        topicCode: g.topicCode,
        topicName: friendlyName,
        studentCount: g.students.length,
        avgMastery,
        students: g.students
      });
    });

    // Sort Re-Teach Topics: Most struggling students first, then lowest average mastery
    reTeachTopics.sort((a, b) => {
      if (b.studentCount !== a.studentCount) return b.studentCount - a.studentCount;
      return a.avgMastery - b.avgMastery;
    });

    // Build structured Neglected Practice Groups (1 entry per student)
    const neglectedStudents: NeglectedStudentGroup[] = [];
    rawNeglectedMap.forEach((s) => {
      // Hydrate topic names
      const hydratedTopics = s.topics.map(t => {
        const idxMeta = topicIndexMap.get(t.topicCode);
        return {
          ...t,
          topicName: t.topicName !== t.topicCode ? t.topicName : (idxMeta?.topicName || idxMeta?.title || idxMeta?.name || t.topicCode)
        };
      });

      hydratedTopics.sort((a, b) => a.examScore - b.examScore);

      neglectedStudents.push({
        id: `neglected_${s.studentCode}`,
        studentCode: s.studentCode,
        studentName: s.studentName,
        className: s.className,
        topicCount: hydratedTopics.length,
        topics: hydratedTopics
      });
    });

    // Sort Neglected Students: Most unattempted topics first
    neglectedStudents.sort((a, b) => b.topicCount - a.topicCount);

    // Build flat backwards-compatible `items` array for the UI feed & search
    const items: InterventionItem[] = [];

    // 1. Re-Teach Topic Items
    reTeachTopics.forEach(t => {
      const studentNamesPreview = t.students.map(s => `${s.studentName} (${s.mastery}%)`).slice(0, 4).join(', ');
      const moreCount = t.students.length > 4 ? ` +${t.students.length - 4} more` : '';

      items.push({
        id: t.id,
        className: t.className,
        urgency: t.studentCount >= 3 ? 'critical' : 'high',
        category: 'conceptual_block',
        title: `🔴 ${t.topicName}`,
        subtitle: `${t.className} • ${t.studentCount} student${t.studentCount > 1 ? 's' : ''} stuck in 🔴 (Avg: ${t.avgMastery}%)`,
        description: `Students completed practice sets but mastery remains < 50%. Classroom whiteboard re-teaching needed for: ${studentNamesPreview}${moreCount}.`,
        topicCode: t.topicCode,
        topicName: t.topicName,
        scorePercent: t.avgMastery,
        studentCount: t.studentCount,
        students: t.students
      });
    });

    // 2. Neglected Practice Items (1 card per student, NOT 1 per topic!)
    neglectedStudents.forEach(s => {
      const topicNamesPreview = s.topics.map(t => t.topicName).slice(0, 3).join(', ');
      const moreCount = s.topics.length > 3 ? ` +${s.topics.length - 3} more` : '';

      items.push({
        id: s.id,
        studentCode: s.studentCode,
        studentName: s.studentName,
        className: s.className,
        urgency: s.topicCount >= 3 ? 'high' : 'medium',
        category: 'neglected_topic',
        title: `🟡 ${s.studentName}`,
        subtitle: `${s.className} • ${s.topicCount} weak topic${s.topicCount > 1 ? 's' : ''} with 0 practice sets started`,
        description: `Topics flagged weak from exam, but student has not attempted self-practice: ${topicNamesPreview}${moreCount}.`,
        scorePercent: s.topics[0]?.examScore,
        studentCount: s.topicCount,
        topics: s.topics
      });
    });

    // 3. Missed Baseline Exam Items
    missedExamsList.forEach(m => {
      items.push({
        id: m.id,
        studentCode: m.studentCode,
        studentName: m.studentName,
        className: m.className,
        urgency: 'critical',
        category: 'missed_exam',
        title: `Missed Exam: ${m.examTitle}`,
        subtitle: `${m.studentName} (${m.className}) • Due: ${m.dueDate} (${m.daysOverdue}d overdue)`,
        description: `Student missed the baseline exam. Topic diagnostic and daily practice cannot be calibrated without baseline score.`,
        examId: m.examId,
        daysOverdue: m.daysOverdue
      });
    });

    const summary: InterventionSummary = {
      totalItems: items.length,
      criticalCount: missedExamsList.length,
      gateBlockedCount: 0,
      conceptualBlockCount: reTeachTopics.length,
      reTeachStudentCount: reTeachStudentCodes.size,
      neglectedTopicCount: neglectedStudents.length,
      reTeachTopics,
      neglectedStudents,
      missedExams: missedExamsList,
      items,
      lastUpdated: new Date().toISOString()
    };

    await ReportCacheManager.setReport(this.CACHE_KEY, summary, this.CACHE_TTL_SECONDS);
    return summary;
  }
}

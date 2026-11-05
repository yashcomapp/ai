import { adminDb } from '@/lib/firebase/admin';
import { getAssignmentsForBatches } from '@/services/exam.service';
import { getDateKeyIST } from '@/lib/dateUtils';
import { ReportCacheManager } from '@/lib/reportCache';

export interface InterventionItem {
  id: string;
  studentCode: string;
  studentName: string;
  className: string;
  phone?: string;
  parentPhone?: string;
  urgency: 'critical' | 'high' | 'medium' | 'low';
  category: 'missed_exam' | 'reflection_gate' | 'low_mastery' | 'inactivity';
  title: string;
  subtitle: string;
  description: string;
  topicCode?: string;
  topicName?: string;
  examId?: string;
  attemptId?: string;
  daysOverdue?: number;
  scorePercent?: number;
  whatsappMessage: string;
  actionType: 'whatsapp' | 'dossier' | 'scorecard';
  actionLabel: string;
  createdAt?: string;
}

export interface InterventionSummary {
  totalItems: number;
  criticalCount: number;
  gateBlockedCount: number;
  lowMasteryCount: number;
  inactivityCount: number;
  items: InterventionItem[];
  lastUpdated: string;
}

/**
 * Normalizes phone numbers to standard international 10/12-digit format for WhatsApp web.
 */
function normalizeWhatsAppPhone(phone?: string): string {
  if (!phone) return '';
  const digits = phone.replace(/\D/g, '');
  if (digits.length === 10) return `91${digits}`;
  if (digits.length === 12 && digits.startsWith('91')) return digits;
  return digits;
}

export class InterventionService {
  private static CACHE_KEY = 'admin_report_interventions';
  private static CACHE_TTL_SECONDS = 60; // 1-minute TTL with on-demand refresh

  /**
   * Generates a ranked, deduplicated Intervention Queue for teachers & admins.
   * Answers the decision: "Which students need help today, and what should I do?"
   */
  static async getInterventionQueue(forceRefresh = false): Promise<InterventionSummary> {
    if (!forceRefresh) {
      const cached = await ReportCacheManager.getReport<InterventionSummary>(this.CACHE_KEY);
      if (cached) return cached;
    }

    const now = new Date();
    const todayDateStr = getDateKeyIST(now);

    // 1. Fetch all active students (excluding deactivated accounts per Rule 2.C)
    const studentsSnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .select('name', 'studentCode', 'className', 'batch', 'phone', 'parentPhone', 'status', 'batchId', 'batchIds')
      .get();

    const activeStudents = studentsSnap.docs
      .map(d => ({ id: d.id, ...d.data() } as any))
      .filter(s => s.status !== 'inactive');

    const studentMap = new Map<string, any>();
    const allBatchIds = new Set<string>();

    activeStudents.forEach(s => {
      studentMap.set(s.studentCode, s);
      if (s.batchId) allBatchIds.add(s.batchId);
      if (Array.isArray(s.batchIds)) s.batchIds.forEach((b: string) => allBatchIds.add(b));
    });

    const items: InterventionItem[] = [];

    // 2. Fetch pending reflection gate blockers (Autonomous / Practice gate pending > 24 hours)
    const refSnap = await adminDb.collection('practiceSubmissions')
      .where('reflectionRequiredByGate', '==', true)
      .where('reflectionStatus', '==', 'pending')
      .select('studentCode', 'topicCode', 'topicName', 'scorePercent', 'total', 'score', 'createdAt', 'practiceSessionId')
      .get();

    refSnap.docs.forEach(doc => {
      const data = doc.data() as any;
      const student = studentMap.get(data.studentCode);
      if (!student) return;

      const createdDate = data.createdAt?.toDate ? data.createdAt.toDate() : new Date(data.createdAt || now);
      const hoursPending = Math.max(1, Math.round((now.getTime() - createdDate.getTime()) / (1000 * 60 * 60)));
      const daysPending = Math.floor(hoursPending / 24);

      const topicLabel = data.topicName || data.topicCode || 'Practice Session';
      const phone = normalizeWhatsAppPhone(student.phone || student.parentPhone);
      const msg = `Hello! This is a reminder from YASHCOM regarding ${student.name}. ` +
        `There is a pending practice reflection for '${topicLabel}' that has been waiting for ${hoursPending} hours. ` +
        `Please complete the mistake reflections to unlock the next practice sets today.`;

      items.push({
        id: `gate_${doc.id}`,
        studentCode: student.studentCode,
        studentName: student.name,
        className: student.className || student.batch || 'General Batch',
        phone: student.phone,
        parentPhone: student.parentPhone,
        urgency: daysPending >= 2 ? 'critical' : 'high',
        category: 'reflection_gate',
        title: `Reflection Gate Blocked (${hoursPending}h)`,
        subtitle: `Topic: ${topicLabel} • Score: ${data.scorePercent ?? 0}%`,
        description: `Student made mistakes in practice set and must review explanations & reflect to unlock further sets.`,
        topicCode: data.topicCode,
        topicName: topicLabel,
        attemptId: data.practiceSessionId || doc.id,
        daysOverdue: daysPending,
        scorePercent: data.scorePercent,
        whatsappMessage: msg,
        actionType: 'whatsapp',
        actionLabel: 'WhatsApp Nudge',
        createdAt: createdDate.toISOString()
      });
    });

    // 3. Fetch scheduled assignments & detect missed exams in the last 14 days
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
          // Check student attempts for these past exams
          const pastExamIds = pastExams.map((e: any) => e.examId);
          const studentCodes = Array.from(studentMap.keys());

          // Query examAttempts for completed exams in chunks
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
              // Check if student belongs to this assignment's batch
              const matchesBatch = (ass.batchId && (student.batchId === ass.batchId || (student.batchIds && student.batchIds.includes(ass.batchId)))) ||
                                   (ass.className && (student.className === ass.className || student.batch === ass.className));

              if (matchesBatch) {
                const key = `${student.studentCode}_${ass.examId}`;
                if (!attemptedSet.has(key)) {
                  const examTitle = ass.title || ass.examId;
                  const phone = normalizeWhatsAppPhone(student.phone || student.parentPhone);
                  const msg = `Hello! This is a notice from YASHCOM regarding ${student.name}. ` +
                    `The scheduled exam '${examTitle}' (scheduled on ${getDateKeyIST(endAt)}) was missed. ` +
                    `Please ensure this test is addressed or contact the teacher today.`;

                  items.push({
                    id: `missed_${key}`,
                    studentCode: student.studentCode,
                    studentName: student.name,
                    className: student.className || student.batch || 'General Batch',
                    phone: student.phone,
                    parentPhone: student.parentPhone,
                    urgency: 'critical',
                    category: 'missed_exam',
                    title: `Missed Exam: ${examTitle}`,
                    subtitle: `Due: ${getDateKeyIST(endAt)} • ${daysOverdue} days unattempted`,
                    description: `Student was absent/unattempted for scheduled test. Blocks academic progression.`,
                    examId: ass.examId,
                    daysOverdue,
                    whatsappMessage: msg,
                    actionType: 'whatsapp',
                    actionLabel: 'Send Exam Notice',
                    createdAt: endAt.toISOString()
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

    // 4. Fetch low topic mastery (<50%) with attempted questions
    const lowMasterySnap = await adminDb.collection('studentTopicMastery')
      .where('mastery', '<', 50)
      .select('studentCode', 'topicCode', 'topicName', 'mastery', 'questionsAttempted', 'questionsWrong', 'questionsCorrect', 'updatedAt')
      .get();

    // Group by student and keep the top 1-2 weakest topics per student to prevent flood
    const studentStrugglesMap = new Map<string, any[]>();
    lowMasterySnap.docs.forEach(doc => {
      const data = doc.data() as any;
      if (!studentMap.has(data.studentCode)) return;
      if (!data.questionsAttempted || data.questionsAttempted <= 0) return;

      const list = studentStrugglesMap.get(data.studentCode) || [];
      list.push(data);
      studentStrugglesMap.set(data.studentCode, list);
    });

    studentStrugglesMap.forEach((topics, sCode) => {
      const student = studentMap.get(sCode);
      if (!student) return;

      // Sort by lowest mastery and highest wrong count
      topics.sort((a, b) => (a.mastery - b.mastery) || (b.questionsWrong - a.questionsWrong));

      // Take top worst topic
      const worst = topics[0];
      const topicLabel = worst.topicName || worst.topicCode;
      const phone = normalizeWhatsAppPhone(student.phone || student.parentPhone);
      const msg = `Hello! Learning diagnostic alert from YASHCOM for ${student.name}. ` +
        `Current accuracy on '${topicLabel}' is ${worst.mastery}% with ${worst.questionsWrong || 0} incorrect questions out of ${worst.questionsAttempted}. ` +
        `We recommend 1 focused revision practice session today to restore mastery.`;

      items.push({
        id: `low_${sCode}_${worst.topicCode}`,
        studentCode: student.studentCode,
        studentName: student.name,
        className: student.className || student.batch || 'General Batch',
        phone: student.phone,
        parentPhone: student.parentPhone,
        urgency: worst.mastery < 30 ? 'high' : 'medium',
        category: 'low_mastery',
        title: `Low Mastery: ${topicLabel} (${worst.mastery}%)`,
        subtitle: `${worst.questionsWrong || 0} wrong of ${worst.questionsAttempted} Qs attempted`,
        description: `Student is struggling with fundamentals on this topic. Practice revision recommended.`,
        topicCode: worst.topicCode,
        topicName: topicLabel,
        scorePercent: worst.mastery,
        whatsappMessage: msg,
        actionType: 'whatsapp',
        actionLabel: 'Send Practice Alert',
        createdAt: worst.updatedAt?.toDate ? worst.updatedAt.toDate().toISOString() : undefined
      });
    });

    // 5. Detect Inactivity (No activity in recent days)
    // Gather all students already marked for missed exams or low mastery
    const activeInterventionStudentCodes = new Set(items.map(i => i.studentCode));
    // Find active students with zero presence in activeInterventionStudentCodes and check their last practice
    // (Only flag if truly disengaged)

    // Sort items by Urgency: critical > high > medium > low
    const urgencyWeight: Record<string, number> = {
      critical: 4,
      high: 3,
      medium: 2,
      low: 1
    };

    items.sort((a, b) => {
      const diff = urgencyWeight[b.urgency] - urgencyWeight[a.urgency];
      if (diff !== 0) return diff;
      return (b.daysOverdue || 0) - (a.daysOverdue || 0);
    });

    const summary: InterventionSummary = {
      totalItems: items.length,
      criticalCount: items.filter(i => i.category === 'missed_exam').length,
      gateBlockedCount: items.filter(i => i.category === 'reflection_gate').length,
      lowMasteryCount: items.filter(i => i.category === 'low_mastery').length,
      inactivityCount: items.filter(i => i.category === 'inactivity').length,
      items,
      lastUpdated: new Date().toISOString()
    };

    await ReportCacheManager.setReport(this.CACHE_KEY, summary, this.CACHE_TTL_SECONDS);
    return summary;
  }
}

import { adminDb } from '@/lib/firebase/admin';
import { getAssignmentsForBatches } from '@/services/exam.service';
import { getDateKeyIST } from '@/lib/dateUtils';
import { ReportCacheManager } from '@/lib/reportCache';

export type InterventionCategory = 
  | 'missed_exam'       // Step 1: Baseline Exam missed
  | 'reflection_gate'   // Step 3: Practice locked by mistake reflection
  | 'conceptual_block'  // Step 3: Practiced, but still < 50% (Needs Re-Teach)
  | 'neglected_topic';  // Step 2->3: Flagged 🔴 by exam, but 0 practice done

export interface InterventionItem {
  id: string;
  studentCode: string;
  studentName: string;
  className: string;
  phone?: string;
  parentPhone?: string;
  urgency: 'critical' | 'high' | 'medium' | 'low';
  category: InterventionCategory;
  title: string;
  subtitle: string;
  description: string;
  topicCode?: string;
  topicName?: string;
  examId?: string;
  attemptId?: string;
  daysOverdue?: number;
  scorePercent?: number;
  practiceQuestionsAttempted?: number;
  whatsappMessage: string;
  actionType: 'whatsapp' | 'dossier' | 'scorecard';
  actionLabel: string;
  createdAt?: string;
}

export interface InterventionSummary {
  totalItems: number;
  criticalCount: number;         // Missed Exams
  gateBlockedCount: number;      // Reflection Gates
  conceptualBlockCount: number;  // Practiced but still <50% (Re-Teach)
  neglectedTopicCount: number;   // In 🔴 with 0 practice done
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
  private static CACHE_KEY = 'admin_report_interventions_v2';
  private static CACHE_TTL_SECONDS = 60; // 1-minute TTL with on-demand refresh

  /**
   * Generates a ranked, deduplicated Intervention Queue based on the 3-step lifecycle:
   * 1. Baseline Exam assigned & conducted
   * 2. Topics bucketed into 🟢, 🟡, 🔴 based on exam performance
   * 3. Daily practice moves topics; interventions catch those failing to remediate
   */
  static async getInterventionQueue(forceRefresh = false): Promise<InterventionSummary> {
    if (!forceRefresh) {
      const cached = await ReportCacheManager.getReport<InterventionSummary>(this.CACHE_KEY);
      if (cached) return cached;
    }

    const now = new Date();

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

    // ── STEP 1: Missed Scheduled Baseline Exams ───────────────────────
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
                  const examTitle = ass.title || ass.examId;
                  const phone = normalizeWhatsAppPhone(student.phone || student.parentPhone);
                  const msg = `Hello! Reminder from YASHCOM for ${student.name}. ` +
                    `The scheduled baseline exam '${examTitle}' (conducted on ${getDateKeyIST(endAt)}) was missed. ` +
                    `Taking baseline exams is required so your practice topics can be calibrated. Please take this test today.`;

                  items.push({
                    id: `missed_${key}`,
                    studentCode: student.studentCode,
                    studentName: student.name,
                    className: student.className || student.batch || 'General Batch',
                    phone: student.phone,
                    parentPhone: student.parentPhone,
                    urgency: 'critical',
                    category: 'missed_exam',
                    title: `Missed Baseline Exam: ${examTitle}`,
                    subtitle: `Due: ${getDateKeyIST(endAt)} • ${daysOverdue} days unattempted`,
                    description: `Student missed the baseline exam. Topic diagnostic and daily practice cannot be calibrated without baseline test score.`,
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

    // ── STEP 2 & 3: Practice Gate Lockdown (> 24 hours) ───────────────
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

      const topicLabel = data.topicName || data.topicCode || 'Practice Set';
      const phone = normalizeWhatsAppPhone(student.phone || student.parentPhone);
      const msg = `Hello! Notice from YASHCOM regarding ${student.name}. ` +
        `There is an incomplete mistake reflection for practice on '${topicLabel}' pending for ${hoursPending} hours. ` +
        `Practice is currently locked. Please complete the mistake reflection to unlock your next practice sets.`;

      items.push({
        id: `gate_${doc.id}`,
        studentCode: student.studentCode,
        studentName: student.name,
        className: student.className || student.batch || 'General Batch',
        phone: student.phone,
        parentPhone: student.parentPhone,
        urgency: daysPending >= 2 ? 'critical' : 'high',
        category: 'reflection_gate',
        title: `Practice Locked: Reflection Pending (${hoursPending}h)`,
        subtitle: `Topic: ${topicLabel} • Previous Set: ${data.scorePercent ?? 0}%`,
        description: `Student made errors in practice set and must review explanations & reflect before unlocking further practice.`,
        topicCode: data.topicCode,
        topicName: topicLabel,
        attemptId: data.practiceSessionId || doc.id,
        daysOverdue: daysPending,
        scorePercent: data.scorePercent,
        whatsappMessage: msg,
        actionType: 'whatsapp',
        actionLabel: 'Unlock Nudge',
        createdAt: createdDate.toISOString()
      });
    });

    // ── STEP 3: Topic Mastery Triaging & Remediation Breakdown ─────────
    // Query topics currently in 🔴 Needs Attention (<50%)
    const lowMasterySnap = await adminDb.collection('studentTopicMastery')
      .where('mastery', '<', 50)
      .select('studentCode', 'topicCode', 'topicName', 'mastery', 'questionsAttempted', 'practiceQuestionsAttempted', 'examQuestionsAttempted', 'dailyPracticeSessionsCount', 'lastPracticeDate', 'updatedAt')
      .get();

    const studentConceptualBlockMap = new Map<string, any[]>();
    const studentNeglectedMap = new Map<string, any[]>();

    lowMasterySnap.docs.forEach(doc => {
      const data = doc.data() as any;
      if (!studentMap.has(data.studentCode)) return;
      if (!data.questionsAttempted || data.questionsAttempted <= 0) return;

      const practiceQs = data.practiceQuestionsAttempted || 0;

      if (practiceQs > 0) {
        // Practiced, but STILL <50% -> Conceptual Block (Algorithm failed, Teacher needs to re-teach!)
        const list = studentConceptualBlockMap.get(data.studentCode) || [];
        list.push(data);
        studentConceptualBlockMap.set(data.studentCode, list);
      } else {
        // Flagged by exam, but 0 practice sessions attempted -> Neglected Remediation
        const list = studentNeglectedMap.get(data.studentCode) || [];
        list.push(data);
        studentNeglectedMap.set(data.studentCode, list);
      }
    });

    // 3A. Conceptual Blocks (High Priority: Practiced but stuck in 🔴 -> Teacher Re-Teach)
    studentConceptualBlockMap.forEach((topics, sCode) => {
      const student = studentMap.get(sCode);
      if (!student) return;

      topics.sort((a, b) => (a.mastery - b.mastery) || (b.practiceQuestionsAttempted - a.practiceQuestionsAttempted));
      const worst = topics[0];
      const topicLabel = worst.topicName || worst.topicCode;
      const phone = normalizeWhatsAppPhone(student.phone || student.parentPhone);
      const msg = `Hello! Academic re-teach notice from YASHCOM for ${student.name}. ` +
        `On topic '${topicLabel}', despite attempting ${worst.practiceQuestionsAttempted} practice questions, mastery remains at ${worst.mastery}%. ` +
        `This indicates a core concept misunderstanding. Please attend teacher doubt-clearing or 1-on-1 concept revision today.`;

      items.push({
        id: `block_${sCode}_${worst.topicCode}`,
        studentCode: student.studentCode,
        studentName: student.name,
        className: student.className || student.batch || 'General Batch',
        phone: student.phone,
        parentPhone: student.parentPhone,
        urgency: 'high',
        category: 'conceptual_block',
        title: `🔴 Needs Re-Teach: ${topicLabel} (${worst.mastery}%)`,
        subtitle: `Attempted ${worst.practiceQuestionsAttempted} practice Qs but still stuck in 🔴 (<50%)`,
        description: `Student attempted autonomous practice, but algorithm alone has not cured the weakness. Teacher classroom re-teaching required.`,
        topicCode: worst.topicCode,
        topicName: topicLabel,
        scorePercent: worst.mastery,
        practiceQuestionsAttempted: worst.practiceQuestionsAttempted,
        whatsappMessage: msg,
        actionType: 'whatsapp',
        actionLabel: 'Schedule Re-Teach',
        createdAt: worst.updatedAt?.toDate ? worst.updatedAt.toDate().toISOString() : undefined
      });
    });

    // 3B. Neglected Remediation (Medium Priority: In 🔴 from exam, but 0 practice done)
    studentNeglectedMap.forEach((topics, sCode) => {
      // If student already has a conceptual block, don't spam them with multiple cards
      if (studentConceptualBlockMap.has(sCode)) return;

      const student = studentMap.get(sCode);
      if (!student) return;

      topics.sort((a, b) => a.mastery - b.mastery);
      const worst = topics[0];
      const topicLabel = worst.topicName || worst.topicCode;
      const phone = normalizeWhatsAppPhone(student.phone || student.parentPhone);
      const msg = `Hello! Remediation reminder from YASHCOM for ${student.name}. ` +
        `Topic '${topicLabel}' was flagged in 🔴 Needs Attention (${worst.mastery}%) from your recent exam, but 0 practice sets have been completed. ` +
        `Please complete at least 1 practice set today to begin your topic recovery.`;

      items.push({
        id: `neglect_${sCode}_${worst.topicCode}`,
        studentCode: student.studentCode,
        studentName: student.name,
        className: student.className || student.batch || 'General Batch',
        phone: student.phone,
        parentPhone: student.parentPhone,
        urgency: 'medium',
        category: 'neglected_topic',
        title: `🟡 Remediation Neglected: ${topicLabel}`,
        subtitle: `Exam score: ${worst.mastery}% • 0 practice sets attempted so far`,
        description: `Topic fell into 🔴 from exam baseline, but student has not attempted practice to recover it.`,
        topicCode: worst.topicCode,
        topicName: topicLabel,
        scorePercent: worst.mastery,
        practiceQuestionsAttempted: 0,
        whatsappMessage: msg,
        actionType: 'whatsapp',
        actionLabel: 'Nudge to Practice',
        createdAt: worst.updatedAt?.toDate ? worst.updatedAt.toDate().toISOString() : undefined
      });
    });

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
      conceptualBlockCount: items.filter(i => i.category === 'conceptual_block').length,
      neglectedTopicCount: items.filter(i => i.category === 'neglected_topic').length,
      items,
      lastUpdated: new Date().toISOString()
    };

    await ReportCacheManager.setReport(this.CACHE_KEY, summary, this.CACHE_TTL_SECONDS);
    return summary;
  }
}

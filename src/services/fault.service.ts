import { adminDb } from '@/lib/firebase/admin';
import { getDateKeyIST, parseDateInput } from '@/lib/dateUtils';
import { isDemoUser } from '@/lib/studentDb';

export interface FaultCategory {
  id: string;
  name: string;
  category: 'academic' | 'conduct' | 'punctuality' | 'admin' | 'review' | 'custom';
  target: 'student' | 'parent' | 'shared';
  autoDetectKey?: 'no_exam_review' | 'exam_absent' | 'no_absent_comm' | 'late_fees' | 'zero_practice';
  icon?: string;
  isDefault?: boolean;
}

export const DEFAULT_FAULT_CATEGORIES: FaultCategory[] = [
  { id: 'no_exam_review', name: 'No Exam Review (>60m)', category: 'review', target: 'student', autoDetectKey: 'no_exam_review', icon: '⏱️', isDefault: true },
  { id: 'no_absent_comm', name: 'No Communication on Absence', category: 'punctuality', target: 'shared', autoDetectKey: 'no_absent_comm', icon: '📞', isDefault: true },
  { id: 'exam_absent', name: 'Exam Absenteeism', category: 'punctuality', target: 'student', autoDetectKey: 'exam_absent', icon: '📝', isDefault: true },
  { id: 'late_fees', name: 'Late Fees Payment', category: 'admin', target: 'parent', autoDetectKey: 'late_fees', icon: '💳', isDefault: true },
  { id: 'no_homework', name: 'Incomplete / No Homework', category: 'academic', target: 'student', icon: '📚', isDefault: true },
  { id: 'no_pre_reading', name: 'No Pre-Reading / Topic Prep', category: 'academic', target: 'student', icon: '📖', isDefault: true },
  { id: 'zero_practice', name: 'Zero Practice / No Self-Study', category: 'academic', target: 'student', autoDetectKey: 'zero_practice', icon: '🎯', isDefault: true },
  { id: 'carelessness', name: 'Carelessness / Lack of Focus', category: 'academic', target: 'student', icon: '⚠️', isDefault: true },
  { id: 'class_talking', name: 'Class Talking / Disruption', category: 'conduct', target: 'student', icon: '🗣️', isDefault: true },
  { id: 'ptm_absent', name: 'Absent in Parent Meeting', category: 'conduct', target: 'parent', icon: '👥', isDefault: true }
];

export interface StudentFaultEntry {
  studentCode: string;
  studentName: string;
  batchId: string;
  batchName?: string;
  classNum?: string | number;
  parentName?: string;
  parentPhone?: string;
  faults: Record<string, boolean>; // categoryId -> boolean
  notes: Record<string, string>;  // categoryId -> note
  autoSuggested: Record<string, boolean>;
  updatedAt?: string;
  recordedBy?: string;
}

export class FaultService {
  /**
   * Retrieves or initializes all available fault categories
   */
  static async getCategories(): Promise<FaultCategory[]> {
    try {
      const snap = await adminDb.collection('config').doc('faultCategories').get();
      if (snap.exists) {
        const customCategories = snap.data()?.categories || [];
        const merged = [...DEFAULT_FAULT_CATEGORIES];
        customCategories.forEach((c: FaultCategory) => {
          if (!merged.some(m => m.id === c.id)) {
            merged.push(c);
          }
        });
        return merged;
      }
    } catch (e) {
      console.warn('Failed to load custom fault categories, using defaults:', e);
    }
    return DEFAULT_FAULT_CATEGORIES;
  }

  /**
   * Saves custom categories to system config
   */
  static async saveCategories(categories: FaultCategory[]): Promise<void> {
    await adminDb.collection('config').doc('faultCategories').set({
      categories,
      updatedAt: new Date().toISOString()
    }, { merge: true });
  }

  /**
   * Builds the full batch matrix for a specified date and batch
   */
  static async getBatchMatrix(dateKey: string, batchId: string): Promise<{
    date: string;
    batchId: string;
    batchName: string;
    categories: FaultCategory[];
    students: StudentFaultEntry[];
  }> {
    const categories = await this.getCategories();

    // 1. Fetch batch info
    let batchName = 'All Batches';
    if (batchId && batchId !== 'all') {
      const bDoc = await adminDb.collection('batches').doc(batchId).get();
      if (bDoc.exists) batchName = bDoc.data()?.name || batchName;
    }

    // 2. Fetch active students in batch
    let studentQuery: FirebaseFirestore.Query = adminDb.collection('users')
      .where('role', '==', 'student');

    if (batchId && batchId !== 'all') {
      studentQuery = studentQuery.where('batchIds', 'array-contains', batchId);
    }

    const studentsSnap = await studentQuery.get();
    const activeStudents = studentsSnap.docs
      .map(doc => {
        const d = doc.data();
        const bId = d.batchId || (Array.isArray(d.batchIds) && d.batchIds.length > 0 ? d.batchIds[0] : '');
        return {
          studentCode: d.studentCode || '',
          studentName: d.name || 'Student',
          batchId: bId,
          classNum: d.classNum || d.class || '',
          parentName: d.parentName || '',
          parentPhone: d.parentPhone || d.parentMobile || '',
          status: d.status || 'active',
          isDemo: isDemoUser(d)
        };
      })
      .filter(s => s.status === 'active' && !s.isDemo && s.studentCode);

    // Fallback if batchId wasn't using array-contains (e.g. single batchId field)
    let filteredStudents = activeStudents;
    if (batchId && batchId !== 'all' && activeStudents.length === 0) {
      const allStudentsSnap = await adminDb.collection('users').where('role', '==', 'student').get();
      filteredStudents = allStudentsSnap.docs
        .map(doc => {
          const d = doc.data();
          const bIds: string[] = d.batchIds || (d.batchId ? [d.batchId] : []);
          return {
            studentCode: d.studentCode || '',
            studentName: d.name || 'Student',
            batchId: bIds[0] || '',
            batchIds: bIds,
            classNum: d.classNum || d.class || '',
            parentName: d.parentName || '',
            parentPhone: d.parentPhone || d.parentMobile || '',
            status: d.status || 'active',
            isDemo: isDemoUser(d)
          };
        })
        .filter(s => s.status === 'active' && !s.isDemo && s.studentCode && s.batchIds?.includes(batchId));
    }

    // Sort students by name alphabetically
    filteredStudents.sort((a, b) => a.studentName.localeCompare(b.studentName));

    // 3. Fetch existing fault records for this date
    const faultDocsSnap = await adminDb.collection('faultRecords')
      .where('date', '==', dateKey)
      .get();

    const existingFaultsMap = new Map<string, any>();
    faultDocsSnap.docs.forEach(doc => {
      const d = doc.data();
      if (d.studentCode) {
        existingFaultsMap.set(d.studentCode.toUpperCase(), d);
      }
    });

    // 4. Run System Auto-Detect for the date
    const autoDetections = await this.runAutoDetect(dateKey, filteredStudents.map(s => s.studentCode));

    // 5. Construct matrix rows
    const studentEntries: StudentFaultEntry[] = filteredStudents.map(s => {
      const codeUpper = s.studentCode.toUpperCase();
      const existing = existingFaultsMap.get(codeUpper);
      const detected = autoDetections.get(codeUpper) || {};

      const faults: Record<string, boolean> = {};
      const notes: Record<string, string> = {};
      const autoSuggested: Record<string, boolean> = {};

      categories.forEach(cat => {
        // If teacher previously saved a record, use it
        if (existing?.faults && existing.faults[cat.id] !== undefined) {
          faults[cat.id] = !!existing.faults[cat.id];
          notes[cat.id] = existing.notes?.[cat.id] || '';
        } else if (detected[cat.id]) {
          // If auto-detected and not yet overwritten, suggest true
          faults[cat.id] = true;
          notes[cat.id] = detected[`${cat.id}_note`] || 'Auto-detected by system';
          autoSuggested[cat.id] = true;
        } else {
          faults[cat.id] = false;
          notes[cat.id] = '';
        }
      });

      return {
        studentCode: s.studentCode,
        studentName: s.studentName,
        batchId: s.batchId,
        batchName,
        classNum: s.classNum,
        parentName: s.parentName,
        parentPhone: s.parentPhone,
        faults,
        notes,
        autoSuggested,
        updatedAt: existing?.updatedAt,
        recordedBy: existing?.recordedBy
      };
    });

    return {
      date: dateKey,
      batchId,
      batchName,
      categories,
      students: studentEntries
    };
  }

  /**
   * Auto-detects systemic faults for a given date across target students
   */
  private static async runAutoDetect(dateKey: string, studentCodes: string[]): Promise<Map<string, Record<string, any>>> {
    const results = new Map<string, Record<string, any>>();
    if (!studentCodes.length) return results;

    const studentCodesSet = new Set(studentCodes.map(c => c.toUpperCase()));
    const initEntry = (code: string) => {
      const cUpper = code.toUpperCase();
      if (!results.has(cUpper)) results.set(cUpper, {});
      return results.get(cUpper)!;
    };

    try {
      const now = new Date();
      const [attendanceSnap, feesSnap, reviewsSnap, examReviewsSnap] = await Promise.all([
        // 1. Attendance for date
        adminDb.collection('attendance').where('date', '==', dateKey).get(),
        // 2. Overdue fees
        adminDb.collection('studentFees').where('hasOverdueInstallment', '==', true).get(),
        // 3. Reviews completed on this date
        adminDb.collection('reviews').get(),
        // 4. Completed exam reviews
        adminDb.collection('examReviews').get()
      ]);

      // A. Check Absence without Communication
      attendanceSnap.docs.forEach(doc => {
        const records = doc.data().records || {};
        Object.entries(records).forEach(([sCode, r]: [string, any]) => {
          if (studentCodesSet.has(sCode.toUpperCase()) && r.status === 'absent' && !r.reason && !r.declaredLeave) {
            const entry = initEntry(sCode);
            entry['no_absent_comm'] = true;
            entry['no_absent_comm_note'] = 'Absent marked without prior leave notice';
          }
        });
      });

      // B. Check Late Fees
      feesSnap.docs.forEach(doc => {
        const sCode = doc.id.toUpperCase();
        if (studentCodesSet.has(sCode)) {
          const entry = initEntry(sCode);
          entry['late_fees'] = true;
          entry['late_fees_note'] = 'Overdue installment pending';
        }
      });

      // C. Check Missed 60-Min Exam Reviews for exams finished on this date
      const verifiedReviewsSet = new Set<string>();
      examReviewsSnap.docs.forEach(doc => {
        const d = doc.data();
        if (d.studentCode && d.examId) {
          verifiedReviewsSet.add(`${d.studentCode.toUpperCase()}_${d.examId}`);
        }
      });

      reviewsSnap.docs.forEach(doc => {
        const d = doc.data();
        const sCode = (d.studentCode || '').toUpperCase();
        if (!studentCodesSet.has(sCode) || d.examType === 'entrance' || d.examType === 'practice') return;

        const compDate = parseDateInput(d.completedAt || d.submittedAt || d.createdAt);
        if (compDate && getDateKeyIST(compDate) === dateKey) {
          const examId = d.examId || d.examCode;
          const reviewKey = `${sCode}_${examId}`;
          const isVerified = verifiedReviewsSet.has(reviewKey);

          // If exam completed > 60 minutes ago and no verified review submitted
          const diffMinutes = Math.floor((now.getTime() - compDate.getTime()) / (1000 * 60));
          if (!isVerified && diffMinutes > 60) {
            const entry = initEntry(sCode);
            entry['no_exam_review'] = true;
            entry['no_exam_review_note'] = `Exam review not completed within 60m window (${diffMinutes}m elapsed for ${d.examName || examId})`;
          }
        }
      });

    } catch (err) {
      console.error('Error running fault auto-detection:', err);
    }

    return results;
  }

  /**
   * Saves a student fault entry for a given date
   */
  static async saveStudentFaults(params: {
    date: string;
    studentCode: string;
    faults: Record<string, boolean>;
    notes?: Record<string, string>;
    recordedBy: string;
  }): Promise<void> {
    const { date, studentCode, faults, notes = {}, recordedBy } = params;
    const sCodeUpper = studentCode.trim().toUpperCase();
    const docId = `${sCodeUpper}_${date}`;

    // Fetch student profile to keep record self-contained
    const userQuery = await adminDb.collection('users')
      .where('role', '==', 'student')
      .where('studentCode', '==', sCodeUpper)
      .limit(1)
      .get();

    const studentUser = userQuery.empty ? null : userQuery.docs[0].data();
    const studentName = studentUser?.name || 'Student';
    const batchId = studentUser?.batchId || (Array.isArray(studentUser?.batchIds) ? studentUser.batchIds[0] : '');

    const activeFaultCount = Object.values(faults).filter(Boolean).length;

    await adminDb.collection('faultRecords').doc(docId).set({
      id: docId,
      date,
      studentCode: sCodeUpper,
      studentName,
      batchId,
      faults,
      notes,
      activeFaultCount,
      updatedAt: new Date().toISOString(),
      recordedBy
    }, { merge: true });
  }

  /**
   * Fetches historical timeline of faults for a student (Parent & Student views)
   */
  static async getStudentTimeline(studentCode: string): Promise<{
    summary: { totalIncidents: number; thisMonthCount: number; categoryBreakdown: Record<string, number> };
    records: Array<{ date: string; faults: string[]; notes: Record<string, string>; recordedBy?: string; updatedAt: string }>;
  }> {
    const sCodeUpper = studentCode.trim().toUpperCase();
    const snap = await adminDb.collection('faultRecords')
      .where('studentCode', '==', sCodeUpper)
      .get();

    const records: Array<any> = [];
    const categoryBreakdown: Record<string, number> = {};
    let totalIncidents = 0;
    let thisMonthCount = 0;

    const currentMonthPrefix = getDateKeyIST().slice(0, 7); // "YYYY-MM"

    snap.docs.forEach(doc => {
      const data = doc.data();
      const date = data.date || '';
      const faultsMap = data.faults || {};
      const activeFaults = Object.keys(faultsMap).filter(k => faultsMap[k]);

      if (activeFaults.length > 0) {
        totalIncidents += activeFaults.length;
        if (date.startsWith(currentMonthPrefix)) {
          thisMonthCount += activeFaults.length;
        }

        activeFaults.forEach(f => {
          categoryBreakdown[f] = (categoryBreakdown[f] || 0) + 1;
        });

        records.push({
          date,
          faults: activeFaults,
          notes: data.notes || {},
          recordedBy: data.recordedBy,
          updatedAt: data.updatedAt || date
        });
      }
    });

    // Sort descending by date
    records.sort((a, b) => b.date.localeCompare(a.date));

    return {
      summary: {
        totalIncidents,
        thisMonthCount,
        categoryBreakdown
      },
      records
    };
  }
}

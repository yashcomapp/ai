import { adminDb } from '@/lib/firebase/admin';
import { getDateKeyIST, parseDateInput } from '@/lib/dateUtils';
import { isDemoUser } from '@/lib/studentDb';

export interface FaultCategory {
  id: string;
  name: string;
  category: 'academic' | 'conduct' | 'punctuality' | 'admin' | 'review' | 'custom';
  target: 'student' | 'parent' | 'shared';
  autoDetectKey?: 'no_exam_review' | 'exam_absent' | 'exam_absent_no_info' | 'no_absent_comm' | 'zero_practice';
  icon?: string;
  isDefault?: boolean;
}

export const DEFAULT_FAULT_CATEGORIES: FaultCategory[] = [
  { id: 'no_exam_review', name: 'No Exam Review (>60m)', category: 'review', target: 'student', autoDetectKey: 'no_exam_review', icon: '⏱️', isDefault: true },
  { id: 'no_absent_comm', name: 'No Communication on Absence', category: 'punctuality', target: 'shared', autoDetectKey: 'no_absent_comm', icon: '📞', isDefault: true },
  { id: 'exam_absent', name: 'Exam Absenteeism', category: 'punctuality', target: 'student', autoDetectKey: 'exam_absent', icon: '📝', isDefault: true },
  { id: 'exam_absent_no_info', name: 'Exam Absence without Information', category: 'punctuality', target: 'shared', autoDetectKey: 'exam_absent_no_info', icon: '📵', isDefault: true },
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
        const customCategories = (snap.data()?.categories || []).filter((c: FaultCategory) => c.id !== 'late_fees');
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
    const isSpecificBatch = batchId && batchId !== 'all';

    // 1. Fetch categories, batch info, students, and existing fault records in parallel
    const [categories, bDoc, studentsSnap, faultDocsSnap] = await Promise.all([
      this.getCategories(),
      isSpecificBatch ? adminDb.collection('batches').doc(batchId).get() : Promise.resolve(null),
      adminDb.collection('users').where('role', '==', 'student').get(),
      adminDb.collection('faultRecords').where('date', '==', dateKey).get()
    ]);

    let batchName = 'All Batches';
    if (bDoc && bDoc.exists) {
      batchName = bDoc.data()?.name || batchName;
    }

    // 2. Filter active students for the selected batch
    const allActiveStudents = studentsSnap.docs
      .map(doc => {
        const d = doc.data();
        const bIds: string[] = Array.isArray(d.batchIds) ? d.batchIds : (d.batchId ? [d.batchId] : []);
        return {
          studentCode: d.studentCode || '',
          studentName: d.name || 'Student',
          batchId: bIds[0] || d.batchId || '',
          batchIds: bIds,
          classNum: d.classNum || d.class || '',
          parentName: d.parentName || '',
          parentPhone: d.parentPhone || d.parentMobile || '',
          status: d.status || 'active',
          isDemo: isDemoUser(d)
        };
      })
      .filter(s => s.status === 'active' && !s.isDemo && s.studentCode);

    const filteredStudents = isSpecificBatch
      ? allActiveStudents.filter(s => s.batchIds?.includes(batchId) || s.batchId === batchId)
      : allActiveStudents;

    // Sort students alphabetically
    filteredStudents.sort((a, b) => a.studentName.localeCompare(b.studentName));

    // 3. Map existing fault records
    const existingFaultsMap = new Map<string, any>();
    faultDocsSnap.docs.forEach(doc => {
      const d = doc.data();
      if (d.studentCode) {
        existingFaultsMap.set(d.studentCode.toUpperCase(), d);
      }
    });

    // 4. Run scoped auto-detection for targeted students
    const autoDetections = await this.runAutoDetect(dateKey, filteredStudents);

    // 5. Construct matrix rows
    const studentEntries: StudentFaultEntry[] = filteredStudents.map(s => {
      const codeUpper = s.studentCode.toUpperCase();
      const existing = existingFaultsMap.get(codeUpper);
      const detected = autoDetections.get(codeUpper) || {};

      const faults: Record<string, boolean> = {};
      const notes: Record<string, string> = {};
      const autoSuggested: Record<string, boolean> = {};

      categories.forEach(cat => {
        if (existing?.faults && existing.faults[cat.id] !== undefined) {
          faults[cat.id] = !!existing.faults[cat.id];
          notes[cat.id] = existing.notes?.[cat.id] || '';
        } else if (detected[cat.id]) {
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
   * Auto-detects systemic faults for a given date across target students (strictly scoped to assigned exams)
   */
  private static async runAutoDetect(
    dateKey: string,
    targetStudents: Array<{
      studentCode: string;
      studentName?: string;
      batchIds?: string[];
      batchId?: string;
      classNum?: string | number;
    }>
  ): Promise<Map<string, Record<string, any>>> {
    const results = new Map<string, Record<string, any>>();
    if (!targetStudents.length) return results;

    const studentCodesSet = new Set(targetStudents.map(s => (s.studentCode || '').toUpperCase()).filter(Boolean));
    const initEntry = (code: string) => {
      const cUpper = code.toUpperCase();
      if (!results.has(cUpper)) results.set(cUpper, {});
      return results.get(cUpper)!;
    };

    try {
      const now = new Date();
      // 1. Fetch Attendance, Scheduled Exams (Objective + Subjective), Batch Assignments, Leaves and Declarations in parallel
      const [
        attendanceSnap,
        scheduledExamsSnap,
        scheduledSubjExamsSnap,
        batchAssignmentsSnap,
        subjAssignmentsSnap,
        leavesSnap,
        declsSnap
      ] = await Promise.all([
        adminDb.collection('attendance').where('date', '==', dateKey).get(),
        adminDb.collection('exams').where('scheduledDate', '==', dateKey).get(),
        adminDb.collection('subjectiveExams').where('scheduledDate', '==', dateKey).get(),
        adminDb.collection('batchAssignments').where('status', '==', 'active').get(),
        adminDb.collection('subjectiveAssignments').where('status', '==', 'active').get(),
        adminDb.collection('leaveApplications').where('endDate', '>=', dateKey).get(),
        adminDb.collection('attendanceDeclarations').where('endDate', '>=', dateKey).get()
      ]);

      // Fallback check for subjective exams that might store date under 'date'
      let subjExamsDocs = scheduledSubjExamsSnap.docs;
      if (subjExamsDocs.length === 0) {
        const altSubjSnap = await adminDb.collection('subjectiveExams').where('date', '==', dateKey).get();
        subjExamsDocs = altSubjSnap.docs;
      }

      // Track active leaves and attendance declarations for dateKey
      const activeLeavesMap = new Map<string, any>();
      leavesSnap.docs.forEach(doc => {
        const d = doc.data();
        if (d.studentCode && d.startDate <= dateKey && (!d.status || d.status === 'approved' || d.status === 'pending')) {
          activeLeavesMap.set(d.studentCode.toUpperCase(), d);
        }
      });

      const activeDeclarationsMap = new Map<string, any>();
      declsSnap.docs.forEach(doc => {
        const d = doc.data();
        if (d.studentCode && d.startDate <= dateKey) {
          activeDeclarationsMap.set(d.studentCode.toUpperCase(), d);
        }
      });

      // Index active assignments by examId
      const assignmentsByExam = new Map<string, any[]>();
      [...batchAssignmentsSnap.docs, ...subjAssignmentsSnap.docs].forEach(doc => {
        const d = doc.data();
        if (d.examId) {
          const list = assignmentsByExam.get(d.examId) || [];
          list.push(d);
          assignmentsByExam.set(d.examId, list);
        }
      });

      // A. Check Absence Communication from Classroom Attendance
      attendanceSnap.docs.forEach(doc => {
        const data = doc.data();
        const records = data.records || {};

        Object.entries(records).forEach(([sCode, r]: [string, any]) => {
          const sUpper = sCode.toUpperCase();
          if (!studentCodesSet.has(sUpper)) return;

          if (r.status === 'absent') {
            const hasLeave = activeLeavesMap.has(sUpper);
            const hasDecl = activeDeclarationsMap.has(sUpper);
            const hasExplicitInfo = !!(r.reason || r.declaredLeave || r.leaveType);
            const hasPriorInfo = hasLeave || hasDecl || hasExplicitInfo;

            if (!hasPriorInfo) {
              const entry = initEntry(sUpper);
              entry['no_absent_comm'] = true;
              entry['no_absent_comm_note'] = 'Absent marked without prior leave application or declaration';
            }
          }
        });
      });

      // Helper to evaluate if a student was assigned/targeted for a specific exam
      const isStudentAssignedToExam = (
        student: { studentCode: string; batchIds?: string[]; batchId?: string; classNum?: string | number },
        examData: any,
        examAssignments: any[]
      ): boolean => {
        const sCodeUpper = (student.studentCode || '').toUpperCase();
        const sBatches: string[] = (Array.isArray(student.batchIds) && student.batchIds.length > 0
          ? student.batchIds
          : (student.batchId ? [student.batchId] : [])).map(b => String(b).trim()).filter(Boolean);
        const sClassStr = String(student.classNum || '').trim().replace(/[^0-9]/g, '');

        // 1. Check formal assignments (batchAssignments & subjectiveAssignments)
        if (examAssignments && examAssignments.length > 0) {
          for (const a of examAssignments) {
            if (Array.isArray(a.targetStudents) && a.targetStudents.map((c: string) => String(c).toUpperCase()).includes(sCodeUpper)) {
              return true;
            }
            if (Array.isArray(a.targetBatches) && a.targetBatches.some((b: string) => sBatches.includes(String(b).trim()))) {
              return true;
            }
          }
        }

        // 2. Direct targetStudents on the exam doc
        const targetStudentsList: string[] = (examData.targetStudents || examData.studentCodes || []).map((c: string) => String(c).toUpperCase());
        if (targetStudentsList.length > 0) {
          return targetStudentsList.includes(sCodeUpper);
        }

        // 3. Class match check
        const examClassRaw = examData.classNum || examData.class;
        const examClassStr = String(examClassRaw || '').trim().replace(/[^0-9]/g, '');
        if (sClassStr && examClassStr && sClassStr !== examClassStr) {
          return false;
        }

        // 4. Direct targetBatches on the exam doc
        const examBatches: string[] = (examData.targetBatches || examData.assignedBatches || examData.batchIds || (examData.batchId ? [examData.batchId] : []))
          .map((b: any) => String(b).trim())
          .filter(Boolean);
        if (examBatches.length > 0) {
          return sBatches.some(b => examBatches.includes(b));
        }

        // 5. If no target students and no target batches:
        // If class is specified on exam, it targets all students of that class
        if (examClassStr) {
          return sClassStr === examClassStr;
        }

        // If neither batch nor class is specified, exam applies to all students
        return true;
      };

      // B. Check Missed Scheduled Exams (Objective + Subjective) & 60-Min Reviews on this Date
      const objExamIds = scheduledExamsSnap.docs.map(doc => doc.id);
      const subjExamIds = subjExamsDocs.map(doc => doc.id);

      if (objExamIds.length > 0 || subjExamIds.length > 0) {
        // Fetch reviews, examReviews, and subjectiveAttempts for all scheduled exams
        const [objReviewsSnaps, examReviewsSnaps, subjAttemptsSnaps, subjReviewsSnaps] = await Promise.all([
          Promise.all(objExamIds.map(eId =>
            adminDb.collection('reviews')
              .where('examId', '==', eId)
              .select('studentCode', 'examId', 'completedAt', 'submittedAt', 'createdAt', 'examName', 'examType')
              .get()
          )),
          Promise.all(objExamIds.map(eId =>
            adminDb.collection('examReviews')
              .where('examId', '==', eId)
              .select('studentCode', 'examId')
              .get()
          )),
          Promise.all(subjExamIds.map(eId =>
            adminDb.collection('subjectiveAttempts')
              .where('examId', '==', eId)
              .select('studentCode', 'examId', 'completedAt', 'submittedAt', 'createdAt')
              .get()
          )),
          Promise.all(subjExamIds.map(eId =>
            adminDb.collection('reviews')
              .where('examId', '==', eId)
              .select('studentCode', 'examId')
              .get()
          ))
        ]);

        const attemptedStudentsForExam = new Set<string>();
        const verifiedReviewsSet = new Set<string>();
        const completedExams: Array<{ studentCode: string; examId: string; examName: string; completedAt: any }> = [];

        examReviewsSnaps.forEach(snap => {
          snap.docs.forEach(doc => {
            const d = doc.data();
            if (d.studentCode && d.examId) {
              verifiedReviewsSet.add(`${d.studentCode.toUpperCase()}_${d.examId}`);
            }
          });
        });

        objReviewsSnaps.forEach(snap => {
          snap.docs.forEach(doc => {
            const d = doc.data();
            const sCode = (d.studentCode || '').toUpperCase();
            if (d.examId && sCode) {
              attemptedStudentsForExam.add(`${sCode}_${d.examId}`);
              if (studentCodesSet.has(sCode) && d.examType !== 'entrance' && d.examType !== 'practice') {
                completedExams.push({
                  studentCode: sCode,
                  examId: d.examId,
                  examName: d.examName || d.examId,
                  completedAt: d.completedAt || d.submittedAt || d.createdAt
                });
              }
            }
          });
        });

        subjAttemptsSnaps.forEach(snap => {
          snap.docs.forEach(doc => {
            const d = doc.data();
            const sCode = (d.studentCode || '').toUpperCase();
            if (d.examId && sCode) {
              attemptedStudentsForExam.add(`${sCode}_${d.examId}`);
            }
          });
        });

        subjReviewsSnaps.forEach(snap => {
          snap.docs.forEach(doc => {
            const d = doc.data();
            const sCode = (d.studentCode || '').toUpperCase();
            if (d.examId && sCode) {
              attemptedStudentsForExam.add(`${sCode}_${d.examId}`);
            }
          });
        });

        const allScheduledExams = [
          ...scheduledExamsSnap.docs.map(doc => ({ doc, isSubjective: false })),
          ...subjExamsDocs.map(doc => ({ doc, isSubjective: true }))
        ];

        allScheduledExams.forEach(({ doc: examDoc, isSubjective }) => {
          const examData = examDoc.data();
          const examId = examDoc.id;
          const examName = examData.title || examData.name || examId;
          const examAssignments = assignmentsByExam.get(examId) || [];

          targetStudents.forEach(student => {
            const sUpper = (student.studentCode || '').toUpperCase();
            if (!sUpper || !studentCodesSet.has(sUpper)) return;

            // Scope check: only evaluate absenteeism if the student is assigned to this exam
            if (!isStudentAssignedToExam(student, examData, examAssignments)) {
              return;
            }

            const hasAttempted = attemptedStudentsForExam.has(`${sUpper}_${examId}`);
            if (!hasAttempted) {
              const entry = initEntry(sUpper);
              entry['exam_absent'] = true;
              const hasLeave = activeLeavesMap.has(sUpper);
              const hasDecl = activeDeclarationsMap.has(sUpper);

              if (hasLeave || hasDecl) {
                const leaveReason = hasLeave
                  ? (activeLeavesMap.get(sUpper)?.reason || 'Leave applied')
                  : (activeDeclarationsMap.get(sUpper)?.reason || 'Attendance declared');
                entry['exam_absent_note'] = `Missed scheduled ${isSubjective ? 'subjective ' : ''}exam: ${examName} (${leaveReason})`;
              } else {
                entry['exam_absent_note'] = `Missed scheduled ${isSubjective ? 'subjective ' : ''}exam: ${examName}`;
                entry['exam_absent_no_info'] = true;
                entry['exam_absent_no_info_note'] = `Missed scheduled ${isSubjective ? 'subjective ' : ''}exam (${examName}) without prior information`;
              }
            }
          });
        });

        // C. Check Missed 60-Min Exam Reviews
        completedExams.forEach(item => {
          const compDate = parseDateInput(item.completedAt);
          if (compDate && getDateKeyIST(compDate) === dateKey) {
            const reviewKey = `${item.studentCode}_${item.examId}`;
            const isVerified = verifiedReviewsSet.has(reviewKey);
            const diffMinutes = Math.floor((now.getTime() - compDate.getTime()) / (1000 * 60));
            if (!isVerified && diffMinutes > 60) {
              const entry = initEntry(item.studentCode);
              entry['no_exam_review'] = true;
              entry['no_exam_review_note'] = `Exam review not completed within 60m window (${diffMinutes}m elapsed for ${item.examName})`;
            }
          }
        });
      }

    } catch (err) {
      console.error('Error running fault auto-detection:', err);
    }

    return results;
  }

  /**
   * Saves a student fault entry for a given date (0 read cost when studentName is supplied)
   */
  static async saveStudentFaults(params: {
    date: string;
    studentCode: string;
    studentName?: string;
    batchId?: string;
    faults: Record<string, boolean>;
    notes?: Record<string, string>;
    recordedBy: string;
  }): Promise<void> {
    const { date, studentCode, faults, notes = {}, recordedBy, studentName, batchId } = params;
    const sCodeUpper = studentCode.trim().toUpperCase();
    const docId = `${sCodeUpper}_${date}`;

    let resolvedName = studentName;
    let resolvedBatchId = batchId;

    if (!resolvedName) {
      const userQuery = await adminDb.collection('users')
        .where('role', '==', 'student')
        .where('studentCode', '==', sCodeUpper)
        .limit(1)
        .get();

      const studentUser = userQuery.empty ? null : userQuery.docs[0].data();
      resolvedName = studentUser?.name || 'Student';
      resolvedBatchId = studentUser?.batchId || (Array.isArray(studentUser?.batchIds) ? studentUser.batchIds[0] : '');
    }

    const activeFaultCount = Object.values(faults).filter(Boolean).length;

    await adminDb.collection('faultRecords').doc(docId).set({
      id: docId,
      date,
      studentCode: sCodeUpper,
      studentName: resolvedName,
      batchId: resolvedBatchId || '',
      faults,
      notes,
      activeFaultCount,
      updatedAt: new Date().toISOString(),
      recordedBy
    }, { merge: true });
  }

  /**
   * Saves multiple student fault entries in a single atomic Firestore batch (0 read cost, 1 network roundtrip)
   */
  static async saveBulkFaults(entries: Array<{
    date: string;
    studentCode: string;
    studentName?: string;
    batchId?: string;
    faults: Record<string, boolean>;
    notes?: Record<string, string>;
    recordedBy: string;
  }>): Promise<void> {
    if (!entries.length) return;
    const batch = adminDb.batch();

    entries.forEach(entry => {
      const sCodeUpper = entry.studentCode.trim().toUpperCase();
      const docId = `${sCodeUpper}_${entry.date}`;
      const docRef = adminDb.collection('faultRecords').doc(docId);
      const activeFaultCount = Object.values(entry.faults || {}).filter(Boolean).length;

      batch.set(docRef, {
        id: docId,
        date: entry.date,
        studentCode: sCodeUpper,
        studentName: entry.studentName || 'Student',
        batchId: entry.batchId || '',
        faults: entry.faults || {},
        notes: entry.notes || {},
        activeFaultCount,
        updatedAt: new Date().toISOString(),
        recordedBy: entry.recordedBy
      }, { merge: true });
    });

    await batch.commit();
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

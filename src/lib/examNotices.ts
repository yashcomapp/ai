import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { sendPushNotification } from '@/lib/notifications';

export interface ExamNoticeResult {
  success: boolean;
  message: string;
  totalNoticesSent?: number;
}

export async function generateAndDispatchExamNotices(examId: string, bypassTimeCheck: boolean = false): Promise<ExamNoticeResult> {
  try {
    if (!examId) {
      return { success: false, message: 'Missing examId parameter.' };
    }

    // 1. Fetch exam document
    let examDoc = await adminDb.collection('exams').doc(examId).get();
    let examData = examDoc.exists ? examDoc.data() : null;
    let isSubjective = false;

    if (!examData) {
      examDoc = await adminDb.collection('subjectiveExams').doc(examId).get();
      examData = examDoc.exists ? examDoc.data() : null;
      isSubjective = true;
    }

    if (!examData) {
      return { success: false, message: `Exam with ID '${examId}' not found.` };
    }

    // Check if exam is still ongoing before dispatching notices
    const availableUntilRaw = examData.availableUntil || examData.endTime || examData.expiresAt;
    if (!bypassTimeCheck && availableUntilRaw) {
      const endTime = availableUntilRaw.toDate ? availableUntilRaw.toDate() : new Date(availableUntilRaw);
      if (!isNaN(endTime.getTime()) && new Date() < endTime) {
        return {
          success: false,
          message: `Exam '${examData.title || examData.name || examId}' is still ongoing (ends at ${endTime.toLocaleTimeString()}). Notices will be dispatched automatically after the exam end time.`
        };
      }
    }

    const examTitle = examData.title || examData.name || examData.examName || examId;
    const totalMarks = examData.totalMarks || (isSubjective ? 100 : 120);
    const examDateStr = examData.date || new Date().toLocaleDateString('en-GB');

    // 2. Fetch all reviews/attempts, batch assignments, and absence reasons in parallel
    const [reviewsSnap, assignmentsSnap, studentsSnap, attendanceSnap, absenceReasonsSnap] = await Promise.all([
      adminDb.collection('reviews').where('examId', '==', examId).get(),
      adminDb.collection('batchAssignments').where('examId', '==', examId).get(),
      adminDb.collection('users').where('role', '==', 'student').get(),
      adminDb.collection('attendance').get(),
      adminDb.collection('examAbsenceReasons').where('examId', '==', examId).get()
    ]);

    // Map recorded absence reasons by studentCode
    const recordedReasonMap = new Map<string, string>();
    absenceReasonsSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.studentCode && data.reason) {
        recordedReasonMap.set(data.studentCode, data.reason);
      }
    });

    // Map all student codes assigned to this exam
    const assignedStudentCodes = new Set<string>();
    const studentMap = new Map<string, any>();

    studentsSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.studentCode) {
        studentMap.set(data.studentCode, { id: doc.id, ...data });
      }
    });

    assignmentsSnap.docs.forEach(doc => {
      const ba = doc.data();
      (ba.targetStudents || []).forEach((code: string) => assignedStudentCodes.add(code));
      const targetBatches = ba.targetBatches || [];
      if (targetBatches.length > 0) {
        studentMap.forEach((student, code) => {
          const sBatchIds = student.batchIds && student.batchIds.length ? student.batchIds : (student.batchId ? [student.batchId] : []);
          if (sBatchIds.some((b: string) => targetBatches.includes(b))) {
            assignedStudentCodes.add(code);
          }
        });
      }
    });

    // 3. Process submitted reviews & compute ranks, average marks, and topper time
    const attempts: any[] = [];
    reviewsSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.studentCode) {
        attempts.push({
          id: doc.id,
          studentCode: data.studentCode,
          score: data.score || 0,
          percentage: data.percentage || (data.score ? Math.round((data.score / totalMarks) * 100) : 0),
          durationSpent: data.durationSpent || 0 // seconds
        });
      }
    });

    // Sort by score descending to determine ranks
    attempts.sort((a, b) => b.score - a.score);

    // Calculate Class Average
    const totalSubmittedCount = attempts.length;
    const classAvgMarks = totalSubmittedCount > 0
      ? (attempts.reduce((sum, a) => sum + a.score, 0) / totalSubmittedCount).toFixed(1)
      : '0';

    // Determine Topper's Time Spent (in minutes)
    const topperAttempt = attempts[0] || null;
    const topperTimeMinutes = topperAttempt ? Math.max(1, Math.round((topperAttempt.durationSpent || 0) / 60)) : null;

    // Create Rank Map: studentCode -> rank number
    const rankMap = new Map<string, number>();
    attempts.forEach((att, index) => {
      if (!rankMap.has(att.studentCode)) {
        rankMap.set(att.studentCode, index + 1);
      }
    });

    // 4. Calculate cumulative exam absence counts per student
    const absenceCountMap = new Map<string, number>();
    attendanceSnap.docs.forEach(doc => {
      const attData = doc.data();
      const records = attData.records || {};
      Object.keys(records).forEach(code => {
        const r = records[code];
        if (r && r.status === 'absent') {
          absenceCountMap.set(code, (absenceCountMap.get(code) || 0) + 1);
        }
      });
    });

    // Batch writer for notices
    const nowISO = new Date().toISOString();
    const batchWriter = adminDb.batch();
    let sentCount = 0;

    // 5. Generate Personalized Notices for each assigned student
    for (const code of Array.from(assignedStudentCodes)) {
      const student = studentMap.get(code);
      const attempt = attempts.find(a => a.studentCode === code);
      const isPresent = !!attempt;

      let type = 'general';
      let title = '';
      let body = '';

      if (isPresent) {
        const pct = attempt.percentage;
        const studentRank = rankMap.get(code) || 1;
        const studentTimeMinutes = Math.max(1, Math.round((attempt.durationSpent || 0) / 60));

        if (pct >= 80) {
          type = 'exam_excellent';
          title = `🏆 EXCELLENT EXAM RESULT: ${examTitle}`;
        } else if (pct >= 60) {
          type = 'exam_good';
          title = `🌟 EXAM RESULT: ${examTitle}`;
        } else {
          type = 'exam_needs_improvement';
          title = `⚠️ EXAM RESULT - ATTENTION: ${examTitle}`;
        }

        body = `📊 Exam Result Announcement: ${examTitle} (${examDateStr})

• Your Rank: #${studentRank} out of ${totalSubmittedCount}
• Your Score: ${attempt.score} / ${totalMarks} (${pct}%)
• Class Average: ${classAvgMarks} / ${totalMarks}
• Time Spent: ${studentTimeMinutes} mins ${topperTimeMinutes ? `(Topper Time: ${topperTimeMinutes} mins)` : ''}

${pct >= 80 ? '🌟 Outstanding performance! Keep up the excellent work.' : pct >= 60 ? '👍 Good effort! Review your incorrect answers to improve further.' : '💡 Focus on weak topics and practice more questions to boost your score.'}`;

      } else {
        type = 'exam_absent';
        title = `🚨 EXAM ABSENCE ALERT: ${examTitle}`;
        const pastAbsences = (absenceCountMap.get(code) || 0) + 1;
        const recordedReason = recordedReasonMap.get(code);

        body = `🚨 EXAM ABSENCE ALERT

• Exam: ${examTitle} (${examDateStr})
• Status: ABSENT (Did not start exam)
${recordedReason ? `• Recorded Reason: ${recordedReason}\n` : ''}⚠️ Total Exam Absences So Far: ${pastAbsences} Exam${pastAbsences > 1 ? 's' : ''}

Please review or update the reason for absence in your Exam Register.`;
      }

      // Only record ABSENT notices in Sent Announcement History for reference (do not log result announcements)
      if (!isPresent) {
        const noticeRef = adminDb.collection('notices').doc();
        const noticePayload = {
          id: noticeRef.id,
          title,
          body,
          type,
          examId,
          studentCode: code,
          targetType: 'student',
          targetValues: [code],
          isOverlay: true,
          noticeDate: examDateStr,
          createdAt: nowISO,
          createdBy: 'System Engine'
        };

        batchWriter.set(noticeRef, noticePayload);
        sentCount++;
      }

      // Trigger Push Notification asynchronously to parent and student
      if (student && student.id) {
        sendPushNotification(
          [student.id],
          title,
          isPresent
            ? `Rank #${rankMap.get(code)}: ${attempt.score}/${totalMarks} (${attempt.percentage}%)`
            : `🚨 ABSENT for ${examTitle}. Action required.`
        ).catch(err => console.error(`Error sending push notification for ${code}:`, err));
      }
    }

    await batchWriter.commit();

    return {
      success: true,
      message: `Successfully generated and dispatched ${sentCount} exam notices.`,
      totalNoticesSent: sentCount
    };

  } catch (error: any) {
    console.error('Error in generateAndDispatchExamNotices:', error);
    return {
      success: false,
      message: error.message || 'Internal Server Error while generating exam notices.'
    };
  }
}

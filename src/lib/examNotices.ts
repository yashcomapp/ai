import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { sendPushNotification } from '@/lib/notifications';
import { ChunkedBatch } from '@/lib/firebase/batch';

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

    // 2. Fetch reviews/attempts, assignments, and absence reasons in parallel
    const [reviewsSnap, objAssignSnap, subjAssignSnap, attendanceSnap, absenceReasonsSnap] = await Promise.all([
      adminDb.collection('reviews').where('examId', '==', examId).get(),
      adminDb.collection('batchAssignments').where('examId', '==', examId).get(),
      adminDb.collection('subjectiveAssignments').where('examId', '==', examId).get(),
      adminDb.collection('attendance').select('records').get(),
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

    // Extract target batches and explicit student codes from exam and assignments
    const targetBatches = new Set<string>();
    const explicitStudentCodes = new Set<string>();

    if (examData.batchId) targetBatches.add(examData.batchId);
    if (Array.isArray(examData.batchIds)) {
      examData.batchIds.forEach((b: string) => { if (b) targetBatches.add(b); });
    }

    [...objAssignSnap.docs, ...subjAssignSnap.docs].forEach(doc => {
      const ba = doc.data();
      (ba.targetStudents || []).forEach((code: string) => { if (code) explicitStudentCodes.add(code); });
      (ba.targetBatches || []).forEach((b: string) => { if (b) targetBatches.add(b); });
    });

    reviewsSnap.docs.forEach(doc => {
      const code = doc.data().studentCode;
      if (code) explicitStudentCodes.add(code);
    });

    // Query targeted students only
    const studentMap = new Map<string, any>();
    const assignedStudentCodes = new Set<string>();

    const batchChunks: string[][] = [];
    const batchArr = Array.from(targetBatches);
    for (let i = 0; i < batchArr.length; i += 30) {
      batchChunks.push(batchArr.slice(i, i + 30));
    }

    const studentCodeChunks: string[][] = [];
    const studentCodeArr = Array.from(explicitStudentCodes);
    for (let i = 0; i < studentCodeArr.length; i += 30) {
      studentCodeChunks.push(studentCodeArr.slice(i, i + 30));
    }

    const studentQueries: Promise<any>[] = [];

    batchChunks.forEach(chunk => {
      studentQueries.push(
        adminDb.collection('users')
          .where('role', '==', 'student')
          .where('batchIds', 'array-contains-any', chunk)
          .get()
          .catch(() => null),
        adminDb.collection('users')
          .where('role', '==', 'student')
          .where('batchId', 'in', chunk)
          .get()
          .catch(() => null)
      );
    });

    studentCodeChunks.forEach(chunk => {
      studentQueries.push(
        adminDb.collection('users')
          .where('role', '==', 'student')
          .where('studentCode', 'in', chunk)
          .get()
          .catch(() => null)
      );
    });

    if (studentQueries.length === 0) {
      // Fallback: active students
      const fallbackSnap = await adminDb.collection('users').where('role', '==', 'student').get();
      fallbackSnap.docs.forEach(doc => {
        const data = doc.data();
        if (data.studentCode) {
          studentMap.set(data.studentCode, { id: doc.id, ...data });
          assignedStudentCodes.add(data.studentCode);
        }
      });
    } else {
      const studentSnaps = await Promise.all(studentQueries);
      studentSnaps.forEach(snap => {
        if (!snap) return;
        snap.docs.forEach((doc: any) => {
          const data = doc.data();
          if (data.studentCode) {
            studentMap.set(data.studentCode, { id: doc.id, ...data });
            assignedStudentCodes.add(data.studentCode);
          }
        });
      });
    }

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
    const batchWriter = new ChunkedBatch(adminDb);
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

        body = `🚨 परीक्षा अनुपस्थिति सूचना (EXAM ABSENCE ALERT)

• Exam: ${examTitle} (${examDateStr})
• Status: ABSENT (परीक्षा में उपस्थित नहीं हुए)
${recordedReason ? `• Recorded Reason: ${recordedReason}\n` : ''}⚠️ कुल अनुपस्थित परीक्षाएं (Total Absences): ${pastAbsences} Exam${pastAbsences > 1 ? 's' : ''}

⚠️ अभिभावक कृपया ध्यान दें (Parental Advisory):
आदरणीय अभिभावक, बिना किसी ठोस कारण के नियमित निर्धारित परीक्षा छोड़ना बच्चे के शैक्षणिक अनुशासन, निरंतरता और परीक्षा परिणामों के लिए अत्यंत हानिकारक है। कृपया अपने बच्चे के साथ दृढ़ता बरतें और सुनिश्चित करें कि वे प्रत्येक परीक्षा में समय पर उपस्थित हों। अगली परीक्षा देने के लिए कृपया इस अनुपस्थिति की समीक्षा और पुष्टि करें।`;
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

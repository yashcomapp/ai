import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { formatTimeIST, getDateKeyIST } from '@/lib/dateUtils';

// In-memory deduplication cache to prevent duplicate notifications within cooldown period
const recentNotificationCache = new Map<string, number>();

function isDuplicateNotification(dedupKey: string, cooldownMs = 60000): boolean {
  const now = Date.now();
  const lastSent = recentNotificationCache.get(dedupKey);
  if (lastSent && (now - lastSent) < cooldownMs) {
    return true; // Duplicate detected!
  }
  recentNotificationCache.set(dedupKey, now);

  if (recentNotificationCache.size > 300) {
    for (const [k, v] of recentNotificationCache.entries()) {
      if (now - v > cooldownMs) recentNotificationCache.delete(k);
    }
  }
  return false;
}

/**
 * Resolves all parent UIDs associated with a given studentCode
 */
async function resolveParentUids(studentCode: string): Promise<string[]> {
  const parentUids = new Set<string>();

  // 1. Fetch student user document to extract parentEmail
  try {
    const studentSnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .where('studentCode', '==', studentCode)
      .limit(1)
      .get();

    let parentEmail = '';
    if (!studentSnap.empty) {
      const studentData = studentSnap.docs[0].data();
      parentEmail = studentData.parentEmail || '';
    }

    // 2. Query parents matching parentEmail
    if (parentEmail) {
      const emailParentsSnap = await adminDb.collection('users')
        .where('role', '==', 'parent')
        .where('email', '==', parentEmail.toLowerCase())
        .get();
      emailParentsSnap.docs.forEach(doc => parentUids.add(doc.id));
    }
  } catch (err) {
    console.error('Error resolving parent by email:', err);
  }

  // 3. Query parents by studentCodes array
  try {
    const codesParentsSnap = await adminDb.collection('users')
      .where('role', '==', 'parent')
      .where('studentCodes', 'array-contains', studentCode)
      .get();
    codesParentsSnap.docs.forEach(doc => parentUids.add(doc.id));

    // Fallback: search studentCode string matches
    const singleCodeParentsSnap = await adminDb.collection('users')
      .where('role', '==', 'parent')
      .where('studentCode', '==', studentCode)
      .get();
    singleCodeParentsSnap.docs.forEach(doc => parentUids.add(doc.id));
  } catch (err) {
    console.error('Error resolving parents by student code mapping:', err);
  }

  return Array.from(parentUids);
}

/**
 * Multicasts a push notification to user tokens belonging to target UIDs
 */
export async function sendPushNotification(
  targetUids: string[],
  title: string,
  body: string,
  data?: Record<string, string>
) {
  if (targetUids.length === 0) return;

  try {
    // 1. Gather all tokens for these UIDs
    const tokens: string[] = [];

    // Chunk targetUids into groups of 30 (Firestore limit for 'in' queries)
    const chunks: string[][] = [];
    for (let i = 0; i < targetUids.length; i += 30) {
      chunks.push(targetUids.slice(i, i + 30));
    }

    const allSnaps = await Promise.all(
      chunks.map(chunk => 
        adminDb.collection('users')
          .where(admin.firestore.FieldPath.documentId(), 'in', chunk)
          .get()
          .catch(err => {
            console.error('Error fetching user chunk for push notification:', err);
            return null;
          })
      )
    );

    allSnaps.forEach(usersSnap => {
      if (!usersSnap || usersSnap.empty) return;
      usersSnap.docs.forEach(doc => {
        const userData = doc.data();
        if (Array.isArray(userData.fcmTokens)) {
          userData.fcmTokens.forEach((t: string) => {
            if (t && typeof t === 'string' && !tokens.includes(t)) {
              tokens.push(t);
            }
          });
        }
      });
    });

    if (tokens.length === 0) {
      console.log(`No registered FCM tokens found for target UIDs: ${targetUids.join(', ')}`);
      return;
    }

    const messages = tokens.map(token => ({
      token,
      data: {
        title,
        body,
        ...(data || {})
      }
    }));

    // 2. Multicast push messages in chunks of 500 (FCM limit)
    const FCM_CHUNK_SIZE = 500;
    const fcmChunks: any[][] = [];
    for (let i = 0; i < messages.length; i += FCM_CHUNK_SIZE) {
      fcmChunks.push(messages.slice(i, i + FCM_CHUNK_SIZE));
    }

    let successCount = 0;
    let failureCount = 0;
    await Promise.all(fcmChunks.map(async (chunk) => {
      try {
        const response = await admin.messaging().sendEach(chunk);
        successCount += response.successCount;
        failureCount += response.failureCount;
      } catch (fcmErr) {
        console.error('Error sending FCM multicast chunk:', fcmErr);
        failureCount += chunk.length;
      }
    }));
    console.log(`FCM multicast complete: successfully sent ${successCount} of ${messages.length} messages (failed: ${failureCount}).`);

    // 3. Log to history collection for each recipient in batches of 500 (Firestore limit)
    try {
      const BATCH_CHUNK_SIZE = 500;
      const uidChunks: string[][] = [];
      for (let i = 0; i < targetUids.length; i += BATCH_CHUNK_SIZE) {
        uidChunks.push(targetUids.slice(i, i + BATCH_CHUNK_SIZE));
      }

      await Promise.all(uidChunks.map(async (chunk) => {
        const batch = adminDb.batch();
        chunk.forEach(uid => {
          const logRef = adminDb.collection('pushNotificationsHistory').doc();
          batch.set(logRef, {
            userId: uid,
            title,
            body,
            data: data || null,
            sentAt: admin.firestore.FieldValue.serverTimestamp()
          });
        });
        await batch.commit();
      }));
    } catch (logErr) {
      console.error('Error logging push notification history:', logErr);
    }
  } catch (error) {
    console.error('Error sending multicast FCM notification:', error);
  }
}

/**
 * 1. Event: New Exam Assigned to both Students/Parents
 */
function formatNotificationDateTime(timestamp?: admin.firestore.Timestamp): string {
  if (!timestamp) return 'Immediately';
  const date = timestamp.toDate();
  return date.toLocaleString('en-US', {
    timeZone: 'Asia/Kolkata',
    day: 'numeric',
    month: 'short',
    year: 'numeric',
    hour: 'numeric',
    minute: '2-digit',
    hour12: true
  }) + ' IST';
}

export async function notifyNewExam(
  examId: string,
  targetType: string,
  targetBatches: string[],
  targetStudents: string[],
  startAt?: admin.firestore.Timestamp,
  endAt?: admin.firestore.Timestamp,
  examType?: 'objective' | 'subjective'
) {
  try {
    const studentUids = new Set<string>();
    const parentUids = new Set<string>();

    // Fetch all parent users once to avoid sequential N+1 query loops
    const parentsSnap = await adminDb.collection('users').where('role', '==', 'parent').get();
    const parents = parentsSnap.docs.map(doc => ({ id: doc.id, ...doc.data() as any }));

    const findParentUidsInMemory = (studentCode: string, parentEmail?: string) => {
      const uids = new Set<string>();
      const normEmail = parentEmail ? parentEmail.toLowerCase() : '';
      parents.forEach(p => {
        const pEmail = p.email ? p.email.toLowerCase() : '';
        if (normEmail && pEmail === normEmail) {
          uids.add(p.id);
        }
        const pCodes = p.studentCodes || [];
        if (pCodes.includes(studentCode)) {
          uids.add(p.id);
        }
        if (p.singleCodeParentsSnap === studentCode || p.studentCode === studentCode) {
          uids.add(p.id);
        }
      });
      return Array.from(uids);
    };

    if (targetType === 'student' && targetStudents.length > 0) {
      // Fetch user ids of specific students
      const studSnap = await adminDb.collection('users')
        .where('role', '==', 'student')
        .where('studentCode', 'in', targetStudents)
        .get();

      studSnap.docs.forEach(doc => {
        studentUids.add(doc.id);
        const data = doc.data();
        if (data.studentCode) {
          const pUids = findParentUidsInMemory(data.studentCode, data.parentEmail);
          pUids.forEach(uid => parentUids.add(uid));
        }
      });
    } else if (targetType === 'batch' && targetBatches.length > 0) {
      // Fetch all students belonging to the target batches
      // Since a student can be mapped via batchId or batchIds array
      const batchStudsSnap = await adminDb.collection('users')
        .where('role', '==', 'student')
        .get();

      for (const doc of batchStudsSnap.docs) {
        const data = doc.data();
        const sBatchId = data.batchId;
        const sBatchIds = data.batchIds || [];
        const matchesBatch = targetBatches.includes(sBatchId) || sBatchIds.some((b: string) => targetBatches.includes(b));

        if (matchesBatch) {
          studentUids.add(doc.id);
          if (data.studentCode) {
            const pUids = findParentUidsInMemory(data.studentCode, data.parentEmail);
            pUids.forEach(uid => parentUids.add(uid));
          }
        }
      }
    } else {
      // Fallback: mixed or not specified, notify all active students
      const allStuds = await adminDb.collection('users').where('role', '==', 'student').get();
      for (const doc of allStuds.docs) {
        const data = doc.data();
        studentUids.add(doc.id);
        if (data.studentCode) {
          try {
            const pUids = findParentUidsInMemory(data.studentCode, data.parentEmail);
            pUids.forEach(uid => parentUids.add(uid));
          } catch (err) {
            console.error('Failed to resolve parents in notifyNewExam fallback:', err);
          }
        }
      }
    }

    // Resolve exam details for richer push notification body
    let examData: any = null;
    try {
      if (examType) {
        const doc = await adminDb.collection(examType === 'subjective' ? 'subjectiveExams' : 'exams').doc(examId).get();
        if (doc.exists) examData = doc.data();
      } else {
        const [objDoc, subjDoc] = await Promise.all([
          adminDb.collection('exams').doc(examId).get(),
          adminDb.collection('subjectiveExams').doc(examId).get()
        ]);
        if (objDoc.exists) examData = objDoc.data();
        else if (subjDoc.exists) examData = subjDoc.data();
      }
    } catch (err) {
      console.warn('Failed to fetch exam details for richer notification:', err);
    }

    const subjectList = examData?.subjects || (examData?.subjectName ? [examData.subjectName] : (examData?.subjectCode ? [examData.subjectCode] : []));
    const subjectStr = subjectList.length > 0 ? subjectList.join(', ') : 'General';

    let chapterStr = examData?.chapter || examData?.chapterName || '';
    if (!chapterStr && examData?.chapterNumber) {
      chapterStr = `Chapter ${examData.chapterNumber}`;
    }
    if (!chapterStr) chapterStr = '-';

    const boardCode = examData?.boardCode || '';
    const classVal = examData?.class || '';
    const subjectCode = examData?.subjectCode || '';
    const chapterNumber = examData?.chapterNumber || '';

    const topicCodes = examData?.topicCodes || [];
    let resolvedTopics = topicCodes;
    if (topicCodes.length > 0) {
      try {
        const refs = topicCodes.map((code: string) => {
          const fullCode = code.includes('-') ? code : `${boardCode}-${classVal}-${subjectCode}-${chapterNumber}-${code}`;
          return adminDb.collection('syllabusTopicIndex').doc(fullCode);
        });
        const snaps = await adminDb.getAll(...refs).catch(() => []);
        resolvedTopics = snaps.filter(s => s && s.exists).map(s => s.data()?.topicName || s.id);
      } catch (e) {
        console.warn('Failed to resolve topic names in notification:', e);
      }
    }
    const topicStr = resolvedTopics.length > 0 ? resolvedTopics.join(', ') : '-';

    const scheduleStr = startAt ? formatNotificationDateTime(startAt) : 'Immediately';

    const isSubjective = examType === 'subjective' || examData?.examType === 'subjective';
    const typeLabel = isSubjective ? 'Subjective' : 'Objective';

    const title = 'YASHCOM';
    const body = `📝 New Exam Assigned - ( ${typeLabel} )\nSubject (s) :- ${subjectStr}\nChapter (s) :- ${chapterStr}\nTopic (s) :- ${topicStr}\nSchedule :- ${scheduleStr}`;

    // Multicast to students and parents
    const allRecipients = Array.from(new Set([...studentUids, ...parentUids]));
    await sendPushNotification(allRecipients, title, body, { type: 'new_exam', examId });
  } catch (err) {
    console.error('Error sending New Exam notifications:', err);
  }
}

/**
 * 2. Event: Review is pending for Parents
 */
export async function notifyReviewPending(params: {
  studentCode: string;
  studentName: string;
  topicName: string;
  scorePercent: number;
  reviewId?: string;
  startedAt?: Date;
  completedAt?: Date;
  durationSpentSec?: number;
  tabViolations?: number;
  gazeViolations?: number;
}) {
  try {
    const dedupKey = `review_pending_${params.studentCode}_${params.reviewId || params.topicName}`;
    if (isDuplicateNotification(dedupKey)) {
      console.log(`[DEDUP] Suppressed duplicate notifyReviewPending for ${dedupKey}`);
      return;
    }

    const parentUids = await resolveParentUids(params.studentCode);
    if (parentUids.length === 0) return;

    const startTime = params.startedAt ? formatTimeIST(params.startedAt) : '';
    const endTime = params.completedAt ? formatTimeIST(params.completedAt) : '';
    const mins = Math.max(1, Math.round((params.durationSpentSec || 0) / 60));

    const title = 'YASHCOM';
    const body = `Your child ${params.studentName} started ${startTime} and completed ${endTime} practice on "${params.topicName}" scoring ${params.scorePercent}%, Time taken = ${mins} minutes, Tab Switch = ${params.tabViolations || 0}, Gaze = ${params.gazeViolations || 0}.`;

    await sendPushNotification(parentUids, title, body, {
      type: 'practice_review_pending',
      reviewId: params.reviewId || '',
      studentCode: params.studentCode
    });
  } catch (err) {
    console.error('Error sending Review Pending notification:', err);
  }
}

/**
 * 3. Event: Student logged in (Parents)
 */
export async function notifyStudentLogin(studentCode: string, studentName: string) {
  try {
    const dedupKey = `student_login_${studentCode}`;
    if (isDuplicateNotification(dedupKey)) {
      console.log(`[DEDUP] Suppressed duplicate notifyStudentLogin for ${dedupKey}`);
      return;
    }

    const parentUids = await resolveParentUids(studentCode);
    if (parentUids.length === 0) return;

    const title = 'YASHCOM';
    const body = `🟢 Log In: ${studentName} logged into learning platform.`;

    await sendPushNotification(parentUids, title, body, { type: 'student_login', studentCode });
  } catch (err) {
    console.error('Error sending Student Login notification:', err);
  }
}

/**
 * 4. Event: Student logged out (Parents)
 * Includes summary of today's time logs
 */
export async function notifyStudentLogout(studentCode: string, studentName: string, studentUid: string) {
  try {
    const dedupKey = `student_logout_${studentCode}`;
    if (isDuplicateNotification(dedupKey)) {
      console.log(`[DEDUP] Suppressed duplicate notifyStudentLogout for ${dedupKey}`);
      return;
    }

    const parentUids = await resolveParentUids(studentCode);
    if (parentUids.length === 0) return;

    // Retrieve today's time log for the student in IST date key
    const key = getDateKeyIST();
    const logDocId = `${studentUid}_${key}`;

    const logSnap = await adminDb.collection('userTimeLog').doc(logDocId).get();
    const logData = logSnap.exists ? logSnap.data()! : {};

    const formatMinutes = (secs: number) => {
      if (!secs || secs < 0) return '0 min';
      const m = Math.round(secs / 60);
      if (m < 60) return `${m} min`;
      const hrs = Math.floor(m / 60);
      const mins = m % 60;
      return mins > 0 ? `${hrs} hr ${mins} min` : `${hrs} hr`;
    };

    const totalStr = formatMinutes(logData.seconds || 0);
    const examStr = formatMinutes(logData.examSeconds || 0);
    const reviewStr = formatMinutes(logData.reviewSeconds || 0);
    const practiceStr = formatMinutes(logData.practiceSeconds || 0);

    const title = 'YASHCOM';
    const body = `🔴 Log Out: ${studentName} logged out. Today's summary: Total: ${totalStr} | Practice: ${practiceStr} | Exam: ${examStr} | Review: ${reviewStr}.`;

    await sendPushNotification(parentUids, title, body, { type: 'student_logout', studentCode });
  } catch (err) {
    console.error('Error sending Student Logout notification:', err);
  }
}

/**
 * 5. Event: Notice published
 */
export async function notifyNotice(
  title: string,
  body: string,
  targetType: 'all' | 'batch' | 'student' | 'parent',
  targetValues: string[]
) {
  try {
    const uids = new Set<string>();

    // Fetch all parent users once to avoid sequential N+1 query loops
    const parentsSnap = await adminDb.collection('users').where('role', '==', 'parent').get();
    const parents = parentsSnap.docs.map(doc => ({ id: doc.id, ...doc.data() as any }));

    const findParentUidsInMemory = (studentCode: string, parentEmail?: string) => {
      const parentUids = new Set<string>();
      const normEmail = parentEmail ? parentEmail.toLowerCase() : '';
      parents.forEach(p => {
        const pEmail = p.email ? p.email.toLowerCase() : '';
        if (normEmail && pEmail === normEmail) {
          parentUids.add(p.id);
        }
        const pCodes = p.studentCodes || [];
        if (pCodes.includes(studentCode)) {
          parentUids.add(p.id);
        }
        if (p.singleCodeParentsSnap === studentCode || p.studentCode === studentCode) {
          parentUids.add(p.id);
        }
      });
      return Array.from(parentUids);
    };

    if (targetType === 'all') {
      // Notify all parents and students
      const snaps = await adminDb.collection('users').get();
      snaps.docs.forEach(doc => uids.add(doc.id));
    } else if (targetType === 'batch' && targetValues.length > 0) {
      // Notify all students in this batch and their parents
      const batchStudsSnap = await adminDb.collection('users')
        .where('role', '==', 'student')
        .get();

      for (const doc of batchStudsSnap.docs) {
        const data = doc.data();
        const sBatchId = data.batchId;
        const sBatchIds = data.batchIds || [];
        const matchesBatch = targetValues.includes(sBatchId) || sBatchIds.some((b: string) => targetValues.includes(b));

        if (matchesBatch) {
          uids.add(doc.id);
          if (data.studentCode) {
            const pList = findParentUidsInMemory(data.studentCode, data.parentEmail);
            pList.forEach(pUid => uids.add(pUid));
          }
        }
      }
    } else if (targetType === 'student' && targetValues.length > 0) {
      // Notify specific students and their parents
      const studSnap = await adminDb.collection('users')
        .where('role', '==', 'student')
        .where('studentCode', 'in', targetValues)
        .get();
      for (const doc of studSnap.docs) {
        uids.add(doc.id);
        const data = doc.data();
        if (data.studentCode) {
          const pList = findParentUidsInMemory(data.studentCode, data.parentEmail);
          pList.forEach(pUid => uids.add(pUid));
        }
      }
    } else if (targetType === 'parent' && targetValues.length > 0) {
      // Notify specific parents matching email
      const parentSnap = await adminDb.collection('users')
        .where('role', '==', 'parent')
        .where('email', 'in', targetValues.map(v => v.toLowerCase()))
        .get();
      parentSnap.docs.forEach(doc => uids.add(doc.id));
    }

    const displayTitle = 'YASHCOM';
    const displayBody = `${title}: ${body}`;
    await sendPushNotification(Array.from(uids), displayTitle, displayBody, { type: 'announcement' });
  } catch (err) {
    console.error('Error sending Notice notification:', err);
  }
}

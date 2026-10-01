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
 * Resolves all parent UIDs associated with given studentCodes and/or parentEmails
 */
async function resolveParentUidsForStudents(studentCodes: string[], parentEmails: string[] = []): Promise<string[]> {
  const parentUids = new Set<string>();
  const cleanCodes = Array.from(new Set(studentCodes.map(c => (c || '').trim()).filter(Boolean)));
  const cleanEmails = Array.from(new Set(parentEmails.map(e => (e || '').trim().toLowerCase()).filter(Boolean)));

  const codeChunks: string[][] = [];
  for (let i = 0; i < cleanCodes.length; i += 30) {
    codeChunks.push(cleanCodes.slice(i, i + 30));
  }

  const emailChunks: string[][] = [];
  for (let i = 0; i < cleanEmails.length; i += 30) {
    emailChunks.push(cleanEmails.slice(i, i + 30));
  }

  const queries: Promise<any>[] = [];

  codeChunks.forEach(chunk => {
    queries.push(
      adminDb.collection('users')
        .where('role', '==', 'parent')
        .where('studentCodes', 'array-contains-any', chunk)
        .get()
        .catch(() => null),
      adminDb.collection('users')
        .where('role', '==', 'parent')
        .where('studentCode', 'in', chunk)
        .get()
        .catch(() => null)
    );
  });

  emailChunks.forEach(chunk => {
    queries.push(
      adminDb.collection('users')
        .where('role', '==', 'parent')
        .where('email', 'in', chunk)
        .get()
        .catch(() => null)
    );
  });

  const snaps = await Promise.all(queries);
  snaps.forEach(snap => {
    if (!snap) return;
    snap.docs.forEach((d: any) => parentUids.add(d.id));
  });

  return Array.from(parentUids);
}

/**
 * Resolves all parent UIDs associated with a single studentCode
 */
async function resolveParentUids(studentCode: string): Promise<string[]> {
  let parentEmail = '';
  try {
    const studentSnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .where('studentCode', '==', studentCode)
      .limit(1)
      .get();
    if (!studentSnap.empty) {
      parentEmail = studentSnap.docs[0].data()?.parentEmail || '';
    }
  } catch (err) {
    console.error('Error finding student parentEmail:', err);
  }

  return resolveParentUidsForStudents([studentCode], parentEmail ? [parentEmail] : []);
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
    // 1. Gather all tokens for these UIDs (and track token -> uid map for pruning dead tokens)
    const tokens: string[] = [];
    const tokenToUidMap = new Map<string, string>();

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
        const uid = doc.id;
        if (Array.isArray(userData.fcmTokens)) {
          userData.fcmTokens.forEach((t: string) => {
            if (t && typeof t === 'string') {
              tokenToUidMap.set(t, uid);
              if (!tokens.includes(t)) {
                tokens.push(t);
              }
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
    const deadTokensByUid = new Map<string, string[]>();

    await Promise.all(fcmChunks.map(async (chunk) => {
      try {
        const response = await admin.messaging().sendEach(chunk);
        successCount += response.successCount;
        failureCount += response.failureCount;

        // Inspect individual response results to identify dead / unregistered tokens
        response.responses.forEach((resp, idx) => {
          if (!resp.success && resp.error) {
            const errorCode = resp.error.code;
            if (
              errorCode === 'messaging/registration-token-not-registered' ||
              errorCode === 'messaging/invalid-registration-token'
            ) {
              const deadToken = chunk[idx]?.token;
              const uid = deadToken ? tokenToUidMap.get(deadToken) : null;
              if (deadToken && uid) {
                const list = deadTokensByUid.get(uid) || [];
                list.push(deadToken);
                deadTokensByUid.set(uid, list);
              }
            }
          }
        });
      } catch (fcmErr) {
        console.error('Error sending FCM multicast chunk:', fcmErr);
        failureCount += chunk.length;
      }
    }));
    console.log(`FCM multicast complete: successfully sent ${successCount} of ${messages.length} messages (failed: ${failureCount}).`);

    // Prune dead/unregistered tokens from users collection asynchronously
    if (deadTokensByUid.size > 0) {
      try {
        const pruneBatch = adminDb.batch();
        deadTokensByUid.forEach((tokensToRemove, uid) => {
          const userRef = adminDb.collection('users').doc(uid);
          pruneBatch.update(userRef, {
            fcmTokens: admin.firestore.FieldValue.arrayRemove(...tokensToRemove)
          });
        });
        await pruneBatch.commit();
        console.log(`Pruned ${deadTokensByUid.size} users' unregistered FCM tokens.`);
      } catch (pruneErr) {
        console.warn('Failed to prune dead FCM tokens:', pruneErr);
      }
    }

    // 3. Log to pushNotificationsHistory collection for non-chat notifications
    // Chat messages already have their own persistent collection (chatRooms/{roomId}/messages) with unread counts
    if (data?.type !== 'chat_message') {
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
    }
  } catch (error) {
    console.error('Error sending multicast FCM notification:', error);
  }
}

export interface BulkPersonalizedNotificationItem {
  userId: string;
  title: string;
  body: string;
  data?: Record<string, string>;
  tokens?: string[];
}

/**
 * Sends personalized push notifications to multiple users in bulk with chunked FCM & Firestore operations
 */
export async function sendBulkPersonalizedPushNotifications(
  items: BulkPersonalizedNotificationItem[]
) {
  if (!items || items.length === 0) return;

  try {
    // 1. Collect all user IDs needing token lookup
    const uidToItemMap = new Map<string, BulkPersonalizedNotificationItem[]>();
    const uidsToFetch: string[] = [];

    items.forEach(item => {
      if (!item.userId) return;
      const list = uidToItemMap.get(item.userId) || [];
      list.push(item);
      uidToItemMap.set(item.userId, list);

      if (!item.tokens || item.tokens.length === 0) {
        if (!uidsToFetch.includes(item.userId)) {
          uidsToFetch.push(item.userId);
        }
      }
    });

    // 2. Fetch tokens for UIDs in chunks of 30
    const uidToTokensMap = new Map<string, string[]>();

    // Pre-populate with any explicitly provided tokens
    items.forEach(item => {
      if (item.tokens && item.tokens.length > 0) {
        const existing = uidToTokensMap.get(item.userId) || [];
        item.tokens.forEach(t => {
          if (t && !existing.includes(t)) existing.push(t);
        });
        uidToTokensMap.set(item.userId, existing);
      }
    });

    if (uidsToFetch.length > 0) {
      const uidChunks: string[][] = [];
      for (let i = 0; i < uidsToFetch.length; i += 30) {
        uidChunks.push(uidsToFetch.slice(i, i + 30));
      }

      const userSnaps = await Promise.all(
        uidChunks.map(chunk =>
          adminDb.collection('users')
            .where(admin.firestore.FieldPath.documentId(), 'in', chunk)
            .select('fcmTokens')
            .get()
            .catch(err => {
              console.error('Error fetching user tokens in bulk personalized push:', err);
              return null;
            })
        )
      );

      userSnaps.forEach(snap => {
        if (!snap || snap.empty) return;
        snap.docs.forEach(doc => {
          const uData = doc.data();
          if (Array.isArray(uData.fcmTokens)) {
            const validTokens = uData.fcmTokens.filter((t: any) => typeof t === 'string' && t.trim().length > 0);
            const existing = uidToTokensMap.get(doc.id) || [];
            validTokens.forEach((t: string) => {
              if (!existing.includes(t)) existing.push(t);
            });
            uidToTokensMap.set(doc.id, existing);
          }
        });
      });
    }

    // 3. Build individual FCM messages & track token -> uid for dead token pruning
    const tokenToUidMap = new Map<string, string>();
    const fcmMessages: any[] = [];

    items.forEach(item => {
      const userTokens = uidToTokensMap.get(item.userId) || [];
      userTokens.forEach(token => {
        tokenToUidMap.set(token, item.userId);
        fcmMessages.push({
          token,
          data: {
            title: item.title,
            body: item.body,
            ...(item.data || {})
          }
        });
      });
    });

    if (fcmMessages.length === 0) {
      console.log(`No active FCM tokens found across ${items.length} personalized notification targets.`);
      return;
    }

    // 4. Multicast in chunks of 500
    const FCM_CHUNK_SIZE = 500;
    const fcmChunks: any[][] = [];
    for (let i = 0; i < fcmMessages.length; i += FCM_CHUNK_SIZE) {
      fcmChunks.push(fcmMessages.slice(i, i + FCM_CHUNK_SIZE));
    }

    let successCount = 0;
    let failureCount = 0;
    const deadTokensByUid = new Map<string, string[]>();

    await Promise.all(fcmChunks.map(async (chunk) => {
      try {
        const response = await admin.messaging().sendEach(chunk);
        successCount += response.successCount;
        failureCount += response.failureCount;

        response.responses.forEach((resp, idx) => {
          if (!resp.success && resp.error) {
            const errorCode = resp.error.code;
            if (
              errorCode === 'messaging/registration-token-not-registered' ||
              errorCode === 'messaging/invalid-registration-token'
            ) {
              const deadToken = chunk[idx]?.token;
              const uid = deadToken ? tokenToUidMap.get(deadToken) : null;
              if (deadToken && uid) {
                const list = deadTokensByUid.get(uid) || [];
                list.push(deadToken);
                deadTokensByUid.set(uid, list);
              }
            }
          }
        });
      } catch (fcmErr) {
        console.error('Error sending personalized FCM chunk:', fcmErr);
        failureCount += chunk.length;
      }
    }));

    console.log(`Personalized FCM multicast complete: sent ${successCount} of ${fcmMessages.length} messages (failed: ${failureCount}).`);

    // 5. Prune dead tokens asynchronously
    if (deadTokensByUid.size > 0) {
      try {
        const pruneBatch = adminDb.batch();
        deadTokensByUid.forEach((tokensToRemove, uid) => {
          const userRef = adminDb.collection('users').doc(uid);
          pruneBatch.update(userRef, {
            fcmTokens: admin.firestore.FieldValue.arrayRemove(...tokensToRemove)
          });
        });
        await pruneBatch.commit();
        console.log(`Pruned ${deadTokensByUid.size} users' unregistered FCM tokens.`);
      } catch (pruneErr) {
        console.warn('Failed to prune dead FCM tokens in bulk send:', pruneErr);
      }
    }

    // 6. Log history in batch
    try {
      const BATCH_CHUNK_SIZE = 500;
      const historyChunks: BulkPersonalizedNotificationItem[][] = [];
      for (let i = 0; i < items.length; i += BATCH_CHUNK_SIZE) {
        historyChunks.push(items.slice(i, i + BATCH_CHUNK_SIZE));
      }

      await Promise.all(historyChunks.map(async (chunk) => {
        const batch = adminDb.batch();
        chunk.forEach(item => {
          const logRef = adminDb.collection('pushNotificationsHistory').doc();
          batch.set(logRef, {
            userId: item.userId,
            title: item.title,
            body: item.body,
            data: item.data || null,
            sentAt: admin.firestore.FieldValue.serverTimestamp()
          });
        });
        await batch.commit();
      }));
    } catch (logErr) {
      console.error('Error logging personalized push notification history:', logErr);
    }
  } catch (error) {
    console.error('Error in sendBulkPersonalizedPushNotifications:', error);
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
    const studentCodes: string[] = [];
    const parentEmails: string[] = [];

    if (targetType === 'student' && targetStudents.length > 0) {
      // Fetch user ids of specific students in chunks of 30
      const studentChunks: string[][] = [];
      for (let i = 0; i < targetStudents.length; i += 30) {
        studentChunks.push(targetStudents.slice(i, i + 30));
      }

      const snaps = await Promise.all(
        studentChunks.map(chunk =>
          adminDb.collection('users')
            .where('role', '==', 'student')
            .where('studentCode', 'in', chunk)
            .get()
            .catch(() => null)
        )
      );

      snaps.forEach(snap => {
        if (!snap) return;
        snap.docs.forEach(doc => {
          studentUids.add(doc.id);
          const data = doc.data();
          if (data.studentCode) studentCodes.push(data.studentCode);
          if (data.parentEmail) parentEmails.push(data.parentEmail);
        });
      });
    } else if (targetType === 'batch' && targetBatches.length > 0) {
      // Fetch only students belonging to the target batches using chunked array-contains-any and in queries
      const batchChunks: string[][] = [];
      for (let i = 0; i < targetBatches.length; i += 30) {
        batchChunks.push(targetBatches.slice(i, i + 30));
      }

      const snaps = await Promise.all(
        batchChunks.flatMap(chunk => [
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
        ])
      );

      snaps.forEach(snap => {
        if (!snap) return;
        snap.docs.forEach(doc => {
          studentUids.add(doc.id);
          const data = doc.data();
          if (data.studentCode) studentCodes.push(data.studentCode);
          if (data.parentEmail) parentEmails.push(data.parentEmail);
        });
      });
    } else {
      // Fallback: mixed or not specified, notify all active students
      const allStuds = await adminDb.collection('users').where('role', '==', 'student').get();
      for (const doc of allStuds.docs) {
        const data = doc.data();
        studentUids.add(doc.id);
        if (data.studentCode) studentCodes.push(data.studentCode);
        if (data.parentEmail) parentEmails.push(data.parentEmail);
      }
    }

    // Resolve targeted parents
    const parentUids = await resolveParentUidsForStudents(studentCodes, parentEmails);

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

    if (targetType === 'all') {
      // Notify all parents and students
      const snaps = await adminDb.collection('users').get();
      snaps.docs.forEach(doc => uids.add(doc.id));
    } else if (targetType === 'batch' && targetValues.length > 0) {
      // Notify all students in this batch and their parents
      const batchChunks: string[][] = [];
      for (let i = 0; i < targetValues.length; i += 30) {
        batchChunks.push(targetValues.slice(i, i + 30));
      }

      const studentCodes: string[] = [];
      const parentEmails: string[] = [];

      const snaps = await Promise.all(
        batchChunks.flatMap(chunk => [
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
        ])
      );

      snaps.forEach(snap => {
        if (!snap) return;
        snap.docs.forEach(doc => {
          uids.add(doc.id);
          const data = doc.data();
          if (data.studentCode) studentCodes.push(data.studentCode);
          if (data.parentEmail) parentEmails.push(data.parentEmail);
        });
      });

      const parentUids = await resolveParentUidsForStudents(studentCodes, parentEmails);
      parentUids.forEach(pUid => uids.add(pUid));
    } else if (targetType === 'student' && targetValues.length > 0) {
      // Notify specific students and their parents
      const studentChunks: string[][] = [];
      for (let i = 0; i < targetValues.length; i += 30) {
        studentChunks.push(targetValues.slice(i, i + 30));
      }

      const studentCodes: string[] = [];
      const parentEmails: string[] = [];

      const snaps = await Promise.all(
        studentChunks.map(chunk =>
          adminDb.collection('users')
            .where('role', '==', 'student')
            .where('studentCode', 'in', chunk)
            .get()
            .catch(() => null)
        )
      );

      snaps.forEach(snap => {
        if (!snap) return;
        snap.docs.forEach(doc => {
          uids.add(doc.id);
          const data = doc.data();
          if (data.studentCode) studentCodes.push(data.studentCode);
          if (data.parentEmail) parentEmails.push(data.parentEmail);
        });
      });

      const parentUids = await resolveParentUidsForStudents(studentCodes, parentEmails);
      parentUids.forEach(pUid => uids.add(pUid));
    } else if (targetType === 'parent' && targetValues.length > 0) {
      // Notify specific parents matching email
      const emailChunks: string[][] = [];
      for (let i = 0; i < targetValues.length; i += 30) {
        emailChunks.push(targetValues.slice(i, i + 30));
      }

      const snaps = await Promise.all(
        emailChunks.map(chunk =>
          adminDb.collection('users')
            .where('role', '==', 'parent')
            .where('email', 'in', chunk.map(v => v.toLowerCase()))
            .get()
            .catch(() => null)
        )
      );

      snaps.forEach(snap => {
        if (!snap) return;
        snap.docs.forEach(doc => uids.add(doc.id));
      });
    }

    const displayTitle = 'YASHCOM';
    const displayBody = `${title}: ${body}`;
    await sendPushNotification(Array.from(uids), displayTitle, displayBody, { type: 'announcement' });
  } catch (err) {
    console.error('Error sending Notice notification:', err);
  }
}

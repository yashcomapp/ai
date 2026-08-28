import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { getDateKeyIST } from '@/lib/dateUtils';
import { verifyToken } from '@/lib/auth';

export const dynamic = 'force-dynamic';

const dateKeyOf = (d: Date) => getDateKeyIST(d);

// 1. GET - Load time log stats (today, this week, last week, trend)
export async function GET(req: NextRequest) {
  try {
    const decodedToken = await verifyToken(req);
    if (!decodedToken) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 401 });
    }

    const { searchParams } = new URL(req.url);
    const targetUid = searchParams.get('uid') || decodedToken.uid;

    if (targetUid !== decodedToken.uid) {
      // Must be admin or parent of this child
      const callerDoc = await adminDb.collection('users').doc(decodedToken.uid).get();
      const callerData = callerDoc.data() || {};
      const callerRole = callerData.role;

      if (callerRole !== 'admin') {
        if (callerRole === 'parent') {
          // Verify targetUid belongs to parent
          const studentDoc = await adminDb.collection('users').doc(targetUid).get();
          if (!studentDoc.exists) {
            return NextResponse.json({ message: 'Unauthorized. Target user not found.' }, { status: 403 });
          }
          const studentData = studentDoc.data() || {};
          if (studentData.role !== 'student') {
            return NextResponse.json({ message: 'Unauthorized. Target user must be a student.' }, { status: 403 });
          }

          const parentEmail = callerData.email?.toLowerCase();
          const studentParentEmail = studentData.parentEmail?.toLowerCase();

          let isLinked = false;
          if (parentEmail && studentParentEmail && parentEmail === studentParentEmail) {
            isLinked = true;
          }

          if (!isLinked) {
            let parentStudentCodes: string[] = [];
            if (Array.isArray(callerData.studentCodes)) {
              parentStudentCodes = callerData.studentCodes.filter(Boolean);
            } else if (callerData.studentCode) {
              parentStudentCodes = [callerData.studentCode];
            } else if (callerData.studentId) {
              parentStudentCodes = [callerData.studentId];
            }

            if (studentData.studentCode && parentStudentCodes.includes(studentData.studentCode)) {
              isLinked = true;
            }
          }

          if (!isLinked) {
            return NextResponse.json({ message: 'Access denied: student does not belong to parent profile.' }, { status: 403 });
          }
        } else {
          return NextResponse.json({ message: 'Unauthorized. Access denied.' }, { status: 403 });
        }
      }
    }

    const fourteenDaysAgo = new Date();
    fourteenDaysAgo.setDate(fourteenDaysAgo.getDate() - 14);
    const fourteenDaysAgoKey = dateKeyOf(fourteenDaysAgo);

    const timeLogSnapshot = await adminDb.collection('userTimeLog')
      .where('uid', '==', targetUid)
      .where('date', '>=', fourteenDaysAgoKey)
      .get();

    const timeLog: Record<string, number> = {};
    timeLogSnapshot.docs.forEach(doc => {
      const d = doc.data();
      if (d.date) {
        timeLog[d.date] = d.seconds || 0;
      }
    });

    const today = new Date();
    const todayKey = dateKeyOf(today);
    const todaySeconds = timeLog[todayKey] || 0;

    let thisWeekSeconds = 0;
    for (let i = 0; i < 7; i++) {
      const d = new Date(today);
      d.setDate(d.getDate() - i);
      thisWeekSeconds += timeLog[dateKeyOf(d)] || 0;
    }

    let lastWeekSeconds = 0;
    for (let j = 7; j < 14; j++) {
      const d2 = new Date(today);
      d2.setDate(d2.getDate() - j);
      lastWeekSeconds += timeLog[dateKeyOf(d2)] || 0;
    }

    let pctChange = 0;
    let trend: 'up' | 'down' | 'flat' = 'flat';
    if (lastWeekSeconds > 0) {
      pctChange = Math.round(((thisWeekSeconds - lastWeekSeconds) / lastWeekSeconds) * 100);
      if (pctChange > 3) trend = 'up';
      else if (pctChange < -3) trend = 'down';
    }

    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const yesterdayKey = dateKeyOf(yesterday);
    const yesterdaySeconds = timeLog[yesterdayKey] || 0;

    let todayPct = 0;
    let todayTrend: 'up' | 'down' | 'flat' = 'flat';
    if (yesterdaySeconds > 0) {
      todayPct = Math.round(((todaySeconds - yesterdaySeconds) / yesterdaySeconds) * 100);
      if (todayPct > 3) todayTrend = 'up';
      else if (todayPct < -3) todayTrend = 'down';
    }

    return NextResponse.json({
      success: true,
      todaySeconds,
      thisWeekSeconds,
      lastWeekSeconds,
      pctChange,
      trend,
      todayTrend,
      todayPct
    });
  } catch (error: any) {
    console.error('GET time-log error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 2. POST - Flush active time and update presence page info
export async function POST(req: NextRequest) {
  try {
    const decodedToken = await verifyToken(req);
    if (!decodedToken) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 401 });
    }

    const { uid } = decodedToken;
    const body = await req.json();
    const { secondsToFlush, dateKey, currentPage, currentPagePath } = body;

    const key = dateKey || dateKeyOf(new Date());

    if (secondsToFlush && secondsToFlush > 0) {
      const docId = `${uid}_${key}`;
      const ref = adminDb.collection('userTimeLog').doc(docId);
      const userRef = adminDb.collection('users').doc(uid);
      
      let examSecondsAdd = 0;
      let reviewSecondsAdd = 0;
      let practiceSecondsAdd = 0;

      if (currentPagePath) {
        if (currentPagePath.includes('take-exam') || currentPagePath.includes('take-subjective-exam')) {
          examSecondsAdd = Number(secondsToFlush);
        } else if (currentPagePath.includes('results')) {
          reviewSecondsAdd = Number(secondsToFlush);
        } else if (currentPagePath.includes('topic') || currentPagePath.includes('learning')) {
          practiceSecondsAdd = Number(secondsToFlush);
        }
      }

      await adminDb.runTransaction(async (tx) => {
        const snap = await tx.get(ref);
        const existingData = snap.exists ? snap.data()! : {};
        const existingSeconds = existingData.seconds || 0;
        const existingExam = existingData.examSeconds || 0;
        const existingReview = existingData.reviewSeconds || 0;
        const existingPractice = existingData.practiceSeconds || 0;

        const newSeconds = Math.min(86400, existingSeconds + Number(secondsToFlush));
        const newExam = Math.min(86400, existingExam + examSecondsAdd);
        const newReview = Math.min(86400, existingReview + reviewSecondsAdd);
        const newPractice = Math.min(86400, existingPractice + practiceSecondsAdd);

        const addedSeconds = newSeconds - existingSeconds;

        tx.set(ref, {
          uid,
          date: key,
          seconds: newSeconds,
          examSeconds: newExam,
          reviewSeconds: newReview,
          practiceSeconds: newPractice,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        }, { merge: true });

        if (addedSeconds > 0) {
          tx.set(userRef, {
            cumulativeSeconds: admin.firestore.FieldValue.increment(addedSeconds),
            updatedAt: admin.firestore.FieldValue.serverTimestamp()
          }, { merge: true });
        }
      });
    }

    const presenceState = body.presenceState || 'active';

    await adminDb.collection('users').doc(uid).set({
      currentPage: currentPage || '',
      currentPagePath: currentPagePath || '',
      currentPageAt: admin.firestore.FieldValue.serverTimestamp(),
      presenceState,
      lastActiveAt: admin.firestore.FieldValue.serverTimestamp(),
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    }, { merge: true });

    return NextResponse.json({ success: true });
  } catch (error: any) {
    console.error('POST time-log error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

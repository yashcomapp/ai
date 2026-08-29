import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { notifyNewExam } from '@/lib/notifications';
import { getDateKeyIST } from '@/lib/dateUtils';
export const dynamic = 'force-dynamic';

const parseIST = (dateStr: string) => {
  if (!dateStr) return new Date();
  const hasOffset = /[+-]\d{2}:?\d{2}$/.test(dateStr) || dateStr.endsWith('Z');
  if (!hasOffset) {
    return new Date(dateStr + '+05:30');
  }
  return new Date(dateStr);
};

const updateExamNameWithAssignedDate = (currentName: string, assignedDate: Date): string => {
  if (!currentName || !assignedDate) return currentName;
  const [year, month, day] = getDateKeyIST(assignedDate).split('-');
  const newDateStr = `${day}${month}${year}`;

  const dateRegex = /-\d{8}$/;
  if (dateRegex.test(currentName)) {
    return currentName.replace(dateRegex, `-${newDateStr}`);
  }
  return currentName;
};

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const action = req.nextUrl.searchParams.get('action');
    const studentCodeParam = req.nextUrl.searchParams.get('studentCode');

    if (action === 'studentTopicStatus' && studentCodeParam) {
      const [masterySnap, parentReviewsSnap] = await Promise.all([
        adminDb.collection('studentTopicMastery').where('studentCode', '==', studentCodeParam).get(),
        adminDb.collection('parentReviews').where('studentCode', '==', studentCodeParam).get()
      ]);

      const practiceCountMap = new Map<string, number>();
      parentReviewsSnap.docs.forEach(doc => {
        const tCode = doc.data().topicCode;
        if (tCode) {
          practiceCountMap.set(tCode, (practiceCountMap.get(tCode) || 0) + 1);
        }
      });

      const topicCodes = Array.from(new Set(masterySnap.docs.map(d => d.data().topicCode).filter(Boolean)));
      const syllabusMap = new Map<string, any>();

      if (topicCodes.length > 0) {
        const chunks = [];
        for (let i = 0; i < topicCodes.length; i += 30) {
          chunks.push(topicCodes.slice(i, i + 30));
        }
        const snaps = await Promise.all(
          chunks.map(chunk => adminDb.collection('syllabusTopicIndex').where('topicCode', 'in', chunk).get())
        );
        snaps.forEach(sSnap => {
          sSnap.docs.forEach(doc => syllabusMap.set(doc.data().topicCode, doc.data()));
        });
      }

      const mastered: any[] = [];
      const practicing: any[] = [];
      const needsAttention: any[] = [];

      masterySnap.docs.forEach(doc => {
        const d = doc.data();
        const tCode = d.topicCode;
        const sData = syllabusMap.get(tCode) || {};

        const mastery = Number(d.mastery || 0);
        const confidence = Number(d.confidence || 0);
        const practiceCount = practiceCountMap.get(tCode) || 0;
        const attempts = d.questionsAttempted || d.attempts || 0;
        const isRecovery = !!d.isRecoveryMastered;
        const isLimitReached = practiceCount >= 5;

        let state = 'needsAttention';
        let expIcon = '🚨';
        let expColor = '#ef4444';
        let expText = '';

        if ((mastery >= 90 && confidence >= 20) || isRecovery) {
          state = 'mastered';
          if (isRecovery) {
            expIcon = '⚡';
            expColor = '#8b5cf6';
            expText = 'Mastered via Recovery Diagnostic (Passed fresh unseen + remediated question assessment).';
          } else {
            expIcon = '⭐';
            expColor = '#10b981';
            expText = `Mastered on 1st attempt (${mastery}% accuracy across ${attempts} verified questions).`;
          }
          mastered.push({
            topicCode: tCode,
            topicName: sData.topicName || d.topicName || tCode,
            subjectName: sData.subjectName || 'General',
            chapterName: sData.chapterName || 'General',
            chapterNumber: sData.chapterNumber || '',
            topicNumber: sData.topicNumber || '',
            mastery,
            confidence,
            practiceCount,
            attempts,
            state,
            expIcon,
            expColor,
            expText
          });
        } else if (mastery >= 50) {
          if (mastery >= 90 && confidence < 20) {
            state = 'revision';
            const needed = Math.max(1, 20 - attempts);
            expIcon = '📖';
            expColor = '#3b82f6';
            expText = `High accuracy (${mastery}%), but needs ${needed} more attempts to reach 20-question Confidence threshold for Mastered.`;
          } else if (isLimitReached) {
            state = 'continuePractice';
            expIcon = '⚡';
            expColor = '#8b5cf6';
            expText = `5/5 practices done (${mastery}% accuracy). Take the Recovery Quiz (Fresh + Missed Qs) to achieve Mastered!`;
          } else {
            state = 'continuePractice';
            expIcon = '📈';
            expColor = '#f59e0b';
            expText = `${practiceCount}/5 practices done (${mastery}% accuracy). ${5 - practiceCount} practice(s) left to aim for 90%+ Mastered.`;
          }
          practicing.push({
            topicCode: tCode,
            topicName: sData.topicName || d.topicName || tCode,
            subjectName: sData.subjectName || 'General',
            chapterName: sData.chapterName || 'General',
            chapterNumber: sData.chapterNumber || '',
            topicNumber: sData.topicNumber || '',
            mastery,
            confidence,
            practiceCount,
            attempts,
            state,
            expIcon,
            expColor,
            expText
          });
        } else {
          state = 'needsAttention';
          if (isLimitReached) {
            expIcon = '⚡';
            expColor = '#8b5cf6';
            expText = `5/5 practices done (${mastery}% accuracy). Take the Recovery Quiz (Fresh + Missed Qs) to achieve Mastered!`;
          } else if (attempts === 0) {
            expIcon = '⚪';
            expColor = '#94a3b8';
            expText = 'Not attempted yet. Start 1st practice to assess concept baseline.';
          } else {
            expIcon = '🚨';
            expColor = '#ef4444';
            expText = `${practiceCount}/5 practices done (${mastery}% accuracy). ${5 - practiceCount} practice(s) left — focus on weak areas.`;
          }
          needsAttention.push({
            topicCode: tCode,
            topicName: sData.topicName || d.topicName || tCode,
            subjectName: sData.subjectName || 'General',
            chapterName: sData.chapterName || 'General',
            chapterNumber: sData.chapterNumber || '',
            topicNumber: sData.topicNumber || '',
            mastery,
            confidence,
            practiceCount,
            attempts,
            state,
            expIcon,
            expColor,
            expText
          });
        }
      });

      return NextResponse.json({
        mastered,
        practicing,
        needsAttention,
        stats: {
          masteredCount: mastered.length,
          practicingCount: practicing.length,
          needsAttentionCount: needsAttention.length
        }
      });
    }

    const since = new Date();
    since.setDate(since.getDate() - 90);

    const [
      examsList,
      subjExamsList,
      batchesList,
      studentsList,
      objAssignList,
      subjAssignList,
      reviewsSnap,
      attemptsSnap,
      parentReviewsSnap,
      masterySnap,
      parentsSnap
    ] = await Promise.all([
      adminDb.collection('exams').where('status', 'in', ['active', 'draft']).get(),
      adminDb.collection('subjectiveExams').where('status', 'in', ['active', 'draft']).get(),
      adminDb.collection('batches').select('name').get(),
      adminDb.collection('users').where('role', '==', 'student').select('studentCode', 'name', 'rollNumber', 'batchIds', 'batchId', 'status').get(),
      adminDb.collection('batchAssignments').where('endAt', '>=', since).get(),
      adminDb.collection('subjectiveAssignments').where('endAt', '>=', since).get(),
      adminDb.collection('reviews').where('startedAt', '>=', since).select('examId').get(),
      adminDb.collection('examAttempts').where('startedAt', '>=', since).select('examId').get(),
      adminDb.collection('parentReviews').where('startedAt', '>=', since).get(),
      adminDb.collection('studentTopicMastery').get(),
      adminDb.collection('users').where('role', '==', 'parent').select('email', 'studentCode', 'studentCodes', 'name').get()
    ]);

    const exams = examsList.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    const subjectiveExams = subjExamsList.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    const batches = batchesList.docs.map(doc => ({ id: doc.id, name: doc.data().name || doc.id }));
    
    const students = studentsList.docs.map(doc => {
      const data = doc.data();
      return {
        id: doc.id,
        studentCode: data.studentCode || '',
        name: data.name || '',
        rollNumber: data.rollNumber || '',
        batchIds: data.batchIds || [],
        batchId: data.batchId || null,
        status: data.status || 'active'
      };
    }).filter(s => !!s.studentCode && s.status !== 'inactive');

    const parents = parentsSnap.docs.map(doc => {
      const data = doc.data();
      const pEmail = data.email || '';
      const pName = data.name || '';
      const pCodes = data.studentCodes || (data.studentCode ? [data.studentCode] : []);
      
      const childNames: string[] = [];
      pCodes.forEach((code: string) => {
        const stud = students.find(s => 
          String(s.studentCode).toLowerCase() === String(code).toLowerCase() ||
          String(s.id).toLowerCase() === String(code).toLowerCase()
        );
        if (stud && stud.name) {
          childNames.push(stud.name);
        }
      });

      if (childNames.length === 0) return null;

      const displayName = childNames.map(name => `${name} (P)`).join(', ');

      return {
        email: pEmail,
        displayName: displayName,
        studentCodes: pCodes
      };
    }).filter((p): p is { email: string; displayName: string; studentCodes: string[] } => p !== null && !!p.email)
    .sort((a, b) => a.displayName.localeCompare(b.displayName));

    const practiceStats: Record<string, { totalSessions: number, questionsAttempted: number, avgScore: number, lastActive: string | null }> = {};
    
    // 1. Process parentReviews collection (practice records)
    parentReviewsSnap.docs.forEach(doc => {
      const data = doc.data();
      const code = data.studentCode;
      if (!code) return;

      if (!practiceStats[code]) {
        practiceStats[code] = {
          totalSessions: 0,
          questionsAttempted: 0,
          avgScore: 0,
          lastActive: null
        };
      }

      const stats = practiceStats[code];
      stats.totalSessions += 1;
      stats.questionsAttempted += (data.totalQuestions || 0);
      stats.avgScore += (data.scorePercent || 0);

      const itemDate = data.startedAt?.toDate ? data.startedAt.toDate() : data.createdAt?.toDate ? data.createdAt.toDate() : data.startedAt ? new Date(data.startedAt) : null;
      if (itemDate) {
        if (!stats.lastActive || itemDate > new Date(stats.lastActive)) {
          stats.lastActive = itemDate.toISOString();
        }
      }
    });

    // 2. Process practice sessions in reviews collection removed (unified under parentReviews)

    // 3. Calculate average score
    Object.keys(practiceStats).forEach(code => {
      const stats = practiceStats[code];
      if (stats.totalSessions > 0) {
        stats.avgScore = Math.round(stats.avgScore / stats.totalSessions);
      }
    });

    const masteryGroup: Record<string, number[]> = {};
    const masteredCount: Record<string, number> = {};
    const practicingCount: Record<string, number> = {};
    const needsAttentionCount: Record<string, number> = {};

    // Map of studentCode -> Map of topicCode -> totalQuestions
    const studentTopicPracticeMap: Record<string, Map<string, number>> = {};
    parentReviewsSnap.docs.forEach(doc => {
      const data = doc.data();
      const code = data.studentCode;
      const tCode = data.topicCode;
      if (!code || !tCode) return;

      if (!studentTopicPracticeMap[code]) {
        studentTopicPracticeMap[code] = new Map<string, number>();
      }
      const map = studentTopicPracticeMap[code];
      map.set(tCode, (map.get(tCode) || 0) + (data.totalQuestions || 0));
    });

    // Map of studentCode -> Map of topicCode -> { mastery, confidence }
    const studentTopicMasteryMap: Record<string, Map<string, { mastery: number, confidence: number }>> = {};

    masterySnap.docs.forEach(doc => {
      const data = doc.data();
      const code = data.studentCode;
      if (!code) return;

      const val = Number(data.mastery || 0);
      const conf = Number(data.confidence || 0);
      const tCode = data.topicCode;

      if (tCode) {
        if (!studentTopicMasteryMap[code]) {
          studentTopicMasteryMap[code] = new Map();
        }
        studentTopicMasteryMap[code].set(tCode, { mastery: val, confidence: conf });
      }

      if (!masteryGroup[code]) masteryGroup[code] = [];
      masteryGroup[code].push(val);

      if (val >= 90 && conf >= 20) {
        masteredCount[code] = (masteredCount[code] || 0) + 1;
      } else if (val >= 50) {
        practicingCount[code] = (practicingCount[code] || 0) + 1;
      } else {
        needsAttentionCount[code] = (needsAttentionCount[code] || 0) + 1;
      }
    });

    const masteryStats: Record<string, { avgMastery: number, avgQuality: number, mastered: number, practicing: number, needsAttention: number }> = {};
    students.forEach(s => {
      const code = s.studentCode;
      const list = masteryGroup[code] || [];
      const avg = list.length ? Math.round(list.reduce((sum, v) => sum + v, 0) / list.length) : 0;

      // Calculate Quality score
      const topicPractice = studentTopicPracticeMap[code] || new Map<string, number>();
      const topicMastery = studentTopicMasteryMap[code] || new Map<string, { mastery: number, confidence: number }>();
      
      let totalQualityScore = 0;
      let topicsCount = 0;
      topicPractice.forEach((q, topicCode) => {
        const record = topicMastery.get(topicCode) || { mastery: 0, confidence: 0 };
        const mastery = record.mastery;
        const confidence = record.confidence;
        
        let topicQuality = 0;
        if (mastery >= 90 && confidence >= 20) {
          const excess = Math.max(0, q - 20);
          topicQuality = Math.max(30, 100 - excess * 1.5);
        } else {
          const excess = Math.max(0, q - 20);
          topicQuality = Math.max(0, mastery - excess * 1.5);
        }
        totalQualityScore += topicQuality;
        topicsCount++;
      });

      const avgQuality = topicsCount > 0 ? Math.round(totalQualityScore / topicsCount) : 100;

      masteryStats[code] = {
        avgMastery: avg,
        avgQuality: avgQuality,
        mastered: masteredCount[code] || 0,
        practicing: practicingCount[code] || 0,
        needsAttention: needsAttentionCount[code] || 0
      };
    });

    const attemptCounts: { [key: string]: number } = {};
    const examAttemptsMap: { [key: string]: Set<string> } = {};

    reviewsSnap.docs.forEach(doc => {
      const eid = doc.data().examId;
      const studentCode = doc.id.includes('_') ? doc.id.split('_').slice(1).join('_') : doc.id;
      if (eid && studentCode) {
        if (!examAttemptsMap[eid]) examAttemptsMap[eid] = new Set();
        examAttemptsMap[eid].add(studentCode);
      }
    });

    attemptsSnap.docs.forEach(doc => {
      const eid = doc.data().examId;
      const studentCode = doc.id.includes('_') ? doc.id.split('_').slice(1).join('_') : doc.id;
      if (eid && studentCode) {
        if (!examAttemptsMap[eid]) examAttemptsMap[eid] = new Set();
        examAttemptsMap[eid].add(studentCode);
      }
    });

    for (const eid in examAttemptsMap) {
      attemptCounts[eid] = examAttemptsMap[eid].size;
    }

    const objAssignments = objAssignList.docs.map(doc => {
      const data = doc.data();
      return {
        id: doc.id,
        examId: data.examId,
        collection: 'batchAssignments',
        targetType: data.targetType || 'batch',
        targetBatches: data.targetBatches || [],
        targetStudents: data.targetStudents || [],
        openMode: data.openMode || 'immediate',
        startAt: data.startAt ? (data.startAt.toDate ? data.startAt.toDate() : new Date(data.startAt)) : null,
        endAt: data.endAt ? (data.endAt.toDate ? data.endAt.toDate() : new Date(data.endAt)) : null,
        attemptLimit: data.attemptLimit || 1,
        examDuration: data.examDuration || 30,
        lateEntryRestriction: data.lateEntryRestriction === true,
        status: data.status || 'active',
        createdAt: data.createdAt ? (data.createdAt.toDate ? data.createdAt.toDate() : new Date(data.createdAt)) : null
      };
    });

    const subjAssignments = subjAssignList.docs.map(doc => {
      const data = doc.data();
      return {
        id: doc.id,
        examId: data.examId,
        collection: 'subjectiveAssignments',
        targetType: data.targetType || 'batch',
        targetBatches: data.targetBatches || [],
        targetStudents: data.targetStudents || [],
        openMode: data.openMode || 'immediate',
        startAt: data.startAt ? (data.startAt.toDate ? data.startAt.toDate() : new Date(data.startAt)) : null,
        endAt: data.endAt ? (data.endAt.toDate ? data.endAt.toDate() : new Date(data.endAt)) : null,
        attemptLimit: data.attemptLimit || 1,
        examMode: data.examMode || 'home',
        classroomDuration: data.classroomDuration || 60,
        classroomTimePerQ: data.classroomTimePerQ || 5,
        lateEntryRestriction: data.lateEntryRestriction === true,
        status: data.status || 'active',
        createdAt: data.createdAt ? (data.createdAt.toDate ? data.createdAt.toDate() : new Date(data.createdAt)) : null
      };
    });

    return NextResponse.json({
      exams,
      subjectiveExams,
      batches,
      students,
      parents,
      assignments: [...objAssignments, ...subjAssignments],
      attemptCounts,
      practiceStats,
      masteryStats
    });

  } catch (error: any) {
    console.error('API load admin exams error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 2. POST - Assign/schedule a new exam (objective or subjective)
export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { 
      examId, 
      type, // 'objective' or 'subjective'
      targetType, // 'batch', 'student', 'mixed'
      targetBatches, 
      targetStudents,
      openMode, // 'immediate', 'scheduled', 'fixed-slot'
      startAtStr,
      endAtStr,
      attemptLimit,
      // objective fields
      examDuration,
      // subjective fields
      examMode, // 'home' or 'classroom'
      classroomDuration,
      classroomTimePerQ,
      lateEntryRestriction
    } = body;

    if (!examId || !type) {
      return NextResponse.json({ message: 'Missing parameters (examId, type).' }, { status: 400 });
    }

    // Guard against duplicate active assignment by superseding/archiving previous assignment
    const collName = type === 'objective' ? 'batchAssignments' : 'subjectiveAssignments';
    const dupSnap = await adminDb.collection(collName)
      .where('examId', '==', examId)
      .where('status', '==', 'active')
      .get();
    
    if (!dupSnap.empty) {
      const incomingBatches = new Set(targetBatches || []);
      const incomingStudents = new Set(targetStudents || []);
      const archiveBatch = adminDb.batch();
      let hasArchived = false;

      for (const doc of dupSnap.docs) {
        const data = doc.data();
        if (targetType === 'batch' && data.targetType === 'batch') {
          const existingBatches = data.targetBatches || [];
          const overlap = existingBatches.some((b: string) => incomingBatches.has(b));
          if (overlap) {
            archiveBatch.update(doc.ref, { status: 'archived', updatedAt: admin.firestore.FieldValue.serverTimestamp() });
            hasArchived = true;
          }
        } else if (targetType === 'student' && data.targetType === 'student') {
          const existingStudents = data.targetStudents || [];
          const overlap = existingStudents.some((s: string) => incomingStudents.has(s));
          if (overlap) {
            archiveBatch.update(doc.ref, { status: 'archived', updatedAt: admin.firestore.FieldValue.serverTimestamp() });
            hasArchived = true;
          }
        }
      }

      if (hasArchived) {
        await archiveBatch.commit().catch(() => {});
      }
    }

    let startAt = new Date();
    let endAt = new Date();
    endAt.setDate(endAt.getDate() + 30);

    if (openMode !== 'immediate') {
      if (!startAtStr || !endAtStr) {
        return NextResponse.json({ message: 'Start and end dates are required for scheduled openings.' }, { status: 400 });
      }
      startAt = parseIST(startAtStr);
      endAt = parseIST(endAtStr);
    }

    try {
      const examRef = adminDb.collection(type === 'objective' ? 'exams' : 'subjectiveExams').doc(examId);
      const examDoc = await examRef.get();
      if (examDoc.exists) {
        const origExamData = examDoc.data() || {};
        const currentName = origExamData.name || origExamData.title || examId;
        const newName = updateExamNameWithAssignedDate(currentName, startAt);
        if (newName !== currentName) {
          await examRef.update({ name: newName, updatedAt: admin.firestore.FieldValue.serverTimestamp() });
        }
      }
    } catch (err) {
      console.warn('Failed to update exam name with assigned date:', err);
    }

    const payload: any = {
      examId: examId,
      targetType: targetType || 'batch',
      targetBatches: targetBatches || [],
      targetStudents: targetStudents || [],
      openMode: openMode || 'immediate',
      startAt: admin.firestore.Timestamp.fromDate(startAt),
      endAt: admin.firestore.Timestamp.fromDate(endAt),
      attemptLimit: Number(attemptLimit) || 1,
      lateEntryRestriction: lateEntryRestriction === true,
      status: 'active',
      createdBy: (adminUser.decodedToken?.email || adminUser.userData?.email) || 'admin@yashcom.com',
      createdAt: admin.firestore.FieldValue.serverTimestamp(),
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    };

    let assignmentDocId: string;

    if (type === 'objective') {
      payload.title = '';
      payload.assignmentType = 'exam';
      payload.examDuration = Number(examDuration) || 30;
      
      const existingSnap = await adminDb.collection('batchAssignments')
        .where('examId', '==', examId)
        .get();

      if (!existingSnap.empty) {
        const targetDoc = existingSnap.docs[0];
        assignmentDocId = targetDoc.id;
        const deleteBatch = adminDb.batch();
        deleteBatch.set(targetDoc.ref, payload);
        for (let i = 1; i < existingSnap.docs.length; i++) {
          deleteBatch.delete(existingSnap.docs[i].ref);
        }
        await deleteBatch.commit();
      } else {
        const docRef = await adminDb.collection('batchAssignments').add(payload);
        assignmentDocId = docRef.id;
      }

      try {
        await notifyNewExam(
          examId,
          payload.targetType,
          payload.targetBatches,
          payload.targetStudents,
          payload.startAt,
          payload.endAt,
          'objective'
        );
      } catch (err) {
        console.error('Error sending exam notifications:', err);
      }
      return NextResponse.json({ success: true, id: assignmentDocId });
    } else {
      payload.examType = 'subjective';
      payload.examMode = examMode || 'home';
      if (examMode === 'classroom') {
        payload.classroomDuration = Number(classroomDuration) || 60;
        payload.classroomTimePerQ = Number(classroomTimePerQ) || 5;
      }

      // Update mode and batchId in the base exam document
      const baseUpdates: any = {
        mode: examMode || 'home'
      };
      if (payload.targetBatches && payload.targetBatches.length > 0) {
        baseUpdates.batchId = payload.targetBatches[0];
      }
      await adminDb.collection('subjectiveExams').doc(examId).update(baseUpdates)
        .catch(e => console.warn('Failed to update subjectiveExams base details:', e.message));
      
      const existingSnap = await adminDb.collection('subjectiveAssignments')
        .where('examId', '==', examId)
        .get();

      if (!existingSnap.empty) {
        const targetDoc = existingSnap.docs[0];
        assignmentDocId = targetDoc.id;
        const deleteBatch = adminDb.batch();
        deleteBatch.set(targetDoc.ref, payload);
        for (let i = 1; i < existingSnap.docs.length; i++) {
          deleteBatch.delete(existingSnap.docs[i].ref);
        }
        await deleteBatch.commit();
      } else {
        const docRef = await adminDb.collection('subjectiveAssignments').add(payload);
        assignmentDocId = docRef.id;
      }

      try {
        await notifyNewExam(
          examId,
          payload.targetType,
          payload.targetBatches,
          payload.targetStudents,
          payload.startAt,
          payload.endAt,
          'subjective'
        );
      } catch (err) {
        console.error('Error sending exam notifications:', err);
      }
      return NextResponse.json({ success: true, id: assignmentDocId });
    }
  } catch (error: any) {
    console.error('API create exam assignment error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 3. PUT - Edit an existing assignment schedule
export async function PUT(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { id, collection, openMode, startAtStr, endAtStr, attemptLimit, examDuration, status, lateEntryRestriction } = body;

    if (!id || !collection) {
      return NextResponse.json({ message: 'Missing parameters (id, collection).' }, { status: 400 });
    }

    const assignRef = adminDb.collection(collection).doc(id);
    const assignSnap = await assignRef.get();
    if (!assignSnap.exists) {
      return NextResponse.json({ message: 'Assignment not found.' }, { status: 404 });
    }

    if (status) {
      await assignRef.update({
        status,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      return NextResponse.json({ success: true, message: `Assignment status updated to ${status}.` });
    }

    const assignData = assignSnap.data()!;
    const startAt = assignData.startAt ? (assignData.startAt.toDate ? assignData.startAt.toDate() : new Date(assignData.startAt)) : null;

    // Block edit if exam already started
    if (startAt && startAt <= new Date() && assignData.openMode !== 'immediate') {
      return NextResponse.json({ message: 'Cannot edit: the exam has already started.' }, { status: 400 });
    }

    let updatedStart = new Date();
    let updatedEnd = new Date();
    updatedEnd.setDate(updatedEnd.getDate() + 30);

    if (openMode !== 'immediate') {
      if (!startAtStr || !endAtStr) {
        return NextResponse.json({ message: 'Start and end dates are required for scheduled openings.' }, { status: 400 });
      }
      updatedStart = parseIST(startAtStr);
      updatedEnd = parseIST(endAtStr);
    }

    const updates: any = {
      openMode,
      startAt: admin.firestore.Timestamp.fromDate(updatedStart),
      endAt: admin.firestore.Timestamp.fromDate(updatedEnd),
      attemptLimit: Number(attemptLimit) || 1,
      lateEntryRestriction: lateEntryRestriction === true,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    };

    if (examDuration) {
      updates.examDuration = Number(examDuration);
    }

    await assignRef.update(updates);

    if (assignData.examId) {
      const examType = collection === 'batchAssignments' ? 'objective' : 'subjective';
      try {
        const examRef = adminDb.collection(examType === 'objective' ? 'exams' : 'subjectiveExams').doc(assignData.examId);
        const examDoc = await examRef.get();
        if (examDoc.exists) {
          const currentName = examDoc.data()?.name || examDoc.data()?.title || assignData.examId;
          const newName = updateExamNameWithAssignedDate(currentName, updatedStart);
          if (newName !== currentName) {
            await examRef.update({ name: newName });
          }
        }
      } catch (err) {
        console.warn('Failed to update exam name during assignment schedule update:', err);
      }
    }

    return NextResponse.json({ success: true, message: 'Assignment updated successfully.' });

  } catch (error: any) {
    console.error('API edit assignment error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 4. DELETE - Delete an exam along with all related details
export async function DELETE(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const examId = searchParams.get('examId') || '';
    const type = searchParams.get('type') || ''; // 'objective' or 'subjective'

    if (!examId || !type) {
      return NextResponse.json({ message: 'Missing parameters (examId, type).' }, { status: 400 });
    }

    const batch = new ChunkedBatch(adminDb);
    let deletedCount = 0;

    if (type === 'objective') {
      // Delete from exams collection
      const examRef = adminDb.collection('exams').doc(examId);
      batch.delete(examRef);
      deletedCount++;

      // Delete corresponding batchAssignments
      const assignmentsSnap = await adminDb.collection('batchAssignments').where('examId', '==', examId).get();
      assignmentsSnap.docs.forEach(doc => {
        batch.delete(doc.ref);
        deletedCount++;
      });

      // Delete examAttempts
      const attemptsSnap = await adminDb.collection('examAttempts').where('examId', '==', examId).get();
      attemptsSnap.docs.forEach(doc => {
        batch.delete(doc.ref);
        deletedCount++;
      });

      // Delete reviews written by this exam (Finding #3)
      const reviewsSnap = await adminDb.collection('reviews').where('examId', '==', examId).get();
      reviewsSnap.docs.forEach(doc => {
        batch.delete(doc.ref);
        deletedCount++;
      });

      // Delete studentTopicMastery written by this exam
      const masterySnap = await adminDb.collection('studentTopicMastery').where('examId', '==', examId).get();
      masterySnap.docs.forEach(doc => {
        batch.delete(doc.ref);
        deletedCount++;
      });

    } else {
      // Delete from subjectiveExams collection
      const examRef = adminDb.collection('subjectiveExams').doc(examId);
      batch.delete(examRef);
      deletedCount++;

      // Delete subjectiveAssignments
      const assignmentsSnap = await adminDb.collection('subjectiveAssignments').where('examId', '==', examId).get();
      assignmentsSnap.docs.forEach(doc => {
        batch.delete(doc.ref);
        deletedCount++;
      });

      // Delete subjectiveAttempts
      const attemptsSnap = await adminDb.collection('subjectiveAttempts').where('examId', '==', examId).get();
      attemptsSnap.docs.forEach(doc => {
        batch.delete(doc.ref);
        deletedCount++;
      });

      // Delete peerAssignments
      const peerSnap = await adminDb.collection('peerAssignments').where('examId', '==', examId).get();
      peerSnap.docs.forEach(doc => {
        batch.delete(doc.ref);
        deletedCount++;
      });

      // Delete evaluations
      const evalSnap = await adminDb.collection('evaluations').where('examId', '==', examId).get();
      evalSnap.docs.forEach(doc => {
        batch.delete(doc.ref);
        deletedCount++;
      });

      // Delete subjectiveReviews
      const reviewsSnap = await adminDb.collection('subjectiveReviews').where('examId', '==', examId).get();
      reviewsSnap.docs.forEach(doc => {
        batch.delete(doc.ref);
        deletedCount++;
      });
    }

    await batch.commit();

    // Auto re-sync class counters to highest remaining active exam sequence
    try {
      await reSyncClassExamCounters();
    } catch (e) {
      console.warn('Error auto re-syncing exam counters after delete:', e);
    }

    return NextResponse.json({ success: true, deletedCount });

  } catch (error: any) {
    console.error('API delete exam error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

async function reSyncClassExamCounters() {
  const classes = ['6', '7', '8', '9', '10', '11', '12'];
  
  const [objDocs, subjDocs] = await Promise.all([
    adminDb.collection('exams').select('class', 'sequence', 'name').get(),
    adminDb.collection('subjectiveExams').select('class', 'sequence', 'name').get()
  ]);

  const classMaxSeq: Record<string, number> = {};

  const processDoc = (data: any) => {
    const classNum = String(data.class || '').trim();
    if (!classNum) return;

    let seq = Number(data.sequence) || 0;
    if (!seq && data.name) {
      const match = data.name.match(/^(\d{3})-/);
      if (match) {
        seq = parseInt(match[1], 10);
      }
    }

    if (seq > 0) {
      classMaxSeq[classNum] = Math.max(classMaxSeq[classNum] || 0, seq);
    }
  };

  objDocs.docs.forEach(doc => processDoc(doc.data()));
  subjDocs.docs.forEach(doc => processDoc(doc.data()));

  const batch = adminDb.batch();
  classes.forEach(cNum => {
    const maxS = classMaxSeq[cNum] || 0;
    const ref = adminDb.collection('examCounters').doc(`class-${cNum}`);
    batch.set(ref, { nextSequence: maxS + 1 }, { merge: true });
  });

  await batch.commit();
}

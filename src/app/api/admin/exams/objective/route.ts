import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { evaluateQuestionAnswer } from '@/lib/questionTypes';
import { getCachedSyllabus } from '@/lib/firebase/cache';
import { ReportCacheManager } from '@/lib/reportCache';
export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const examId = searchParams.get('examId') || '';

    if (!examId) {
      return NextResponse.json({ message: 'Missing parameters (examId).' }, { status: 400 });
    }

    const cacheKey = `exam-report-objective-${examId}`;
    const cached = await ReportCacheManager.getReport(cacheKey);
    if (cached) {
      return NextResponse.json(cached);
    }

    const examSnap = await adminDb.collection('exams').doc(examId).get();
    if (!examSnap.exists) {
      return NextResponse.json({ message: 'Exam not found.' }, { status: 404 });
    }

    // Load reviews, assignments, students, batches, syllabus, and parent evaluations in parallel
    const [reviewsSnap, assignmentsSnap, studentsSnap, batchesSnap, syllabusList, evalSnaps] = await Promise.all([
      adminDb.collection('reviews').where('examId', '==', examId).get(),
      adminDb.collection('batchAssignments').where('examId', '==', examId).get(),
      adminDb.collection('users').where('role', '==', 'student').select('studentCode', 'name', 'batchId', 'batchIds', 'autonomous', 'status', 'lastLoginAt', 'lastActiveAt').get(),
      adminDb.collection('batches').select('name').get(),
      getCachedSyllabus(),
      adminDb.collection('evaluations').where('examId', '==', examId).get()
    ]);

    const evalApprovedMap = new Map<string, any>();
    evalSnaps.docs.forEach(doc => {
      const d = doc.data();
      const rawEvalDate = d.reviewedAt || d.createdAt || d.updatedAt;
      const evalDate = rawEvalDate ? (rawEvalDate.toDate ? rawEvalDate.toDate() : new Date(rawEvalDate)) : null;
      const info = { ...d, evalDate };
      if (d.attemptId) evalApprovedMap.set(d.attemptId, info);
      if (d.legacyId) evalApprovedMap.set(d.legacyId, info);
      if (d.studentCode) evalApprovedMap.set(`${examId}_${d.studentCode}`, info);
    });

    const examData = examSnap.data() || {};
    const targetTopicCodes = examData.topicCodes || [];
    const targetChapterNum = examData.chapterNumber || '';
    const topicNames: string[] = [];

    syllabusList.docs.forEach(doc => {
      const sylData = doc.data();
      const matchesBoard = String(sylData.board || '').toLowerCase() === String(examData.board || '').toLowerCase() || doc.id.startsWith(String(examData.boardCode || '').toLowerCase());
      const matchesClass = String(sylData.class || '') === String(examData.class || '');
      const matchesSubject = String(sylData.subjectCode || '').toLowerCase() === String(examData.subjectCode || '').toLowerCase();
      
      if (matchesBoard && matchesClass && matchesSubject && sylData.chapters) {
        Object.values(sylData.chapters).forEach((ch: any) => {
          if (String(ch.number) === String(targetChapterNum) && ch.topics) {
            ch.topics.forEach((t: any) => {
              if (targetTopicCodes.includes(String(t.number))) {
                topicNames.push(t.name);
              }
            });
          }
        });
      }
    });

    if (topicNames.length === 0) {
      syllabusList.docs.forEach(doc => {
        const sylData = doc.data();
        const matchesSubject = String(sylData.subjectCode || '').toLowerCase() === String(examData.subjectCode || '').toLowerCase();
        if (matchesSubject && sylData.chapters) {
          Object.values(sylData.chapters).forEach((ch: any) => {
            if (ch.topics) {
              ch.topics.forEach((t: any) => {
                if (targetTopicCodes.includes(String(t.number))) {
                  topicNames.push(t.name);
                }
              });
            }
          });
        }
      });
    }

    const attempts = reviewsSnap.docs.map(doc => {
      const data = doc.data();
      const rawStarted = data.startedAt || data.createdAt;
      const startedAt = rawStarted ? (rawStarted.toDate ? rawStarted.toDate() : new Date(rawStarted)) : null;
      const rawCompleted = data.completedAt || data.updatedAt;
      const completedAt = rawCompleted ? (rawCompleted.toDate ? rawCompleted.toDate() : new Date(rawCompleted)) : null;
      const isApproved = data.status === 'approved' || !!evalApprovedMap.get(doc.id) || !!evalApprovedMap.get(`${examId}_${data.studentCode}`);
      const evalInfo = evalApprovedMap.get(doc.id) || evalApprovedMap.get(`${examId}_${data.studentCode}`);
      const rawReviewed = data.reviewedAt || evalInfo?.evalDate || (isApproved ? completedAt : null);
      const reviewedAt = rawReviewed ? (rawReviewed.toDate ? rawReviewed.toDate() : new Date(rawReviewed)) : null;

      const qDetails = (data.questionDetails || []).map((qd: any) => ({
        ...qd,
        isAttempted: qd.isAttempted !== undefined ? Boolean(qd.isAttempted) : Boolean(qd.isCorrect || (qd.userAnswer !== undefined && qd.userAnswer !== null && qd.userAnswer !== ''))
      }));

      return {
        id: doc.id,
        ...data,
        questionDetails: qDetails,
        totalMarks: data.totalMarks || examData.totalMarks || 0,
        status: isApproved ? 'approved' : (data.status || 'pending'),
        startedAt: startedAt ? (startedAt.toISOString ? startedAt.toISOString() : new Date(startedAt).toISOString()) : null,
        completedAt: completedAt ? (completedAt.toISOString ? completedAt.toISOString() : new Date(completedAt).toISOString()) : null,
        reviewedAt: reviewedAt ? (reviewedAt.toISOString ? reviewedAt.toISOString() : new Date(reviewedAt).toISOString()) : null
      };
    });

    const assignments = assignmentsSnap.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    const students = studentsSnap.docs.map(doc => {
      const data = doc.data();
      return {
        id: doc.id,
        studentCode: data.studentCode || '',
        name: data.name || '',
        batchId: data.batchId || null,
        batchIds: data.batchIds || [],
        autonomous: data.autonomous || false,
        status: data.status || 'active',
        lastLoginAt: data.lastLoginAt ? (data.lastLoginAt.toDate ? data.lastLoginAt.toDate().toISOString() : new Date(data.lastLoginAt).toISOString()) : null,
        lastActiveAt: data.lastActiveAt ? (data.lastActiveAt.toDate ? data.lastActiveAt.toDate().toISOString() : new Date(data.lastActiveAt).toISOString()) : null
      };
    }).filter(s => s.status !== 'inactive');

    const batches = batchesSnap.docs.map(doc => ({ id: doc.id, name: doc.data().name || doc.id }));

    // Scan unique question codes from exam document and attempts
    const uniqueCodes = new Set<string>();
    (examData.questionCodes || examData.questions || []).forEach((code: string) => {
      if (code) uniqueCodes.add(code);
    });
    attempts.forEach((r: any) => {
      (r.questionDetails || []).forEach((qd: any) => {
        if (qd.questionCode) uniqueCodes.add(qd.questionCode);
      });
    });

    // Load full question data matching old codes (direct ID, questionCode query, or _migratedFrom query)
    const questions: any[] = [];
    if (uniqueCodes.size > 0) {
      const codeList = Array.from(uniqueCodes);
      const refs = codeList.map(code => adminDb.collection('questions').doc(code));
      const firstSnaps = refs.length > 0 ? await adminDb.getAll(...refs).catch(() => []) : [];
      
      const missingCodes: string[] = [];
      firstSnaps.forEach((snap, idx) => {
        if (snap && snap.exists) {
          questions.push({ id: codeList[idx], questionCode: codeList[idx], ...snap.data() });
        } else {
          missingCodes.push(codeList[idx]);
        }
      });

      if (missingCodes.length > 0) {
        // Query fallback for questionCode and _migratedFrom using bulk chunked queries
        const chunks = [];
        const chunkSize = 30;
        for (let i = 0; i < missingCodes.length; i += chunkSize) {
          chunks.push(missingCodes.slice(i, i + chunkSize));
        }

        const [byCodeResults, byMigratedResults] = await Promise.all([
          Promise.all(chunks.map(chunk =>
            adminDb.collection('questions')
              .where('questionCode', 'in', chunk)
              .get()
          )),
          Promise.all(chunks.map(chunk =>
            adminDb.collection('questions')
              .where('_migratedFrom', 'in', chunk)
              .get()
          ))
        ]);

        byCodeResults.forEach(snap => {
          snap.docs.forEach(doc => {
            const data = doc.data();
            const qCode = data.questionCode;
            if (qCode && missingCodes.includes(qCode) && !questions.some(q => q.id === qCode || q.questionCode === qCode)) {
              questions.push({ id: qCode, ...data });
            }
          });
        });

        byMigratedResults.forEach(snap => {
          snap.docs.forEach(doc => {
            const data = doc.data();
            const originalCode = data._migratedFrom;
            if (originalCode && missingCodes.includes(originalCode) && !questions.some(q => q.id === originalCode || q.questionCode === originalCode)) {
              questions.push({ id: originalCode, ...data });
            }
          });
        });
      }
    }

    const resultReport = {
      exam: { id: examSnap.id, ...examData, topicNames },
      attempts,
      assignments,
      students,
      batches,
      questions
    };

    const now = new Date();
    let isCompleted = true;
    assignments.forEach((ba: any) => {
      if (ba.status !== 'completed' && (!ba.endAt || new Date(ba.endAt) > now)) {
        isCompleted = false;
      }
    });

    if (isCompleted && attempts.length > 0) {
      await ReportCacheManager.setReport(cacheKey, resultReport, 300);
    }

    return NextResponse.json(resultReport);

  } catch (error: any) {
    console.error('API get objective exam report error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// POST - Update status or delete / override score / reset attempt / rescore questions
export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { action, examId, questionId, newCorrectAnswer, attemptId, updates } = body;

    const resolvedExamId = examId || (attemptId ? (await adminDb.collection('reviews').doc(attemptId).get().then(s => s.data()?.examId).catch(() => null)) : null);
    if (resolvedExamId) {
      await ReportCacheManager.invalidateReport(`exam-report-objective-${resolvedExamId}`);
    }

    if (action === 'rescore') {
      if (!examId || !questionId || newCorrectAnswer === undefined) {
        return NextResponse.json({ message: 'Missing parameters (examId, questionId, newCorrectAnswer).' }, { status: 400 });
      }

      // 1. Update question in questions collection
      let questionRef: any = adminDb.collection('questions').doc(questionId);
      let questionSnap: any = await questionRef.get();
      if (!questionSnap.exists) {
        const queryByCode = await adminDb.collection('questions').where('questionCode', '==', questionId).limit(1).get();
        if (!queryByCode.empty) {
          questionSnap = queryByCode.docs[0];
          questionRef = questionSnap.ref;
        } else {
          return NextResponse.json({ message: 'Question not found.' }, { status: 404 });
        }
      }
      const questionData = questionSnap.data()!;
      await questionRef.update({ 
        correctAnswer: newCorrectAnswer,
        correctAnswers: [newCorrectAnswer]
      });

      const qType = questionData.type || 'single_mcq';
      const qOptions = questionData.options || [];

      // 2. Fetch all reviews for this exam to re-score
      const reviewsSnap = await adminDb.collection('reviews').where('examId', '==', examId).get();
      const examSnap = await adminDb.collection('exams').doc(examId).get();
      const examData = examSnap.exists ? examSnap.data()! : {};
      const negativePerWrong = Number(examData.negativeMarks) || 0;

      const batch = new ChunkedBatch(adminDb);
      let updatedCount = 0;

      for (const doc of reviewsSnap.docs) {
        const r = doc.data();
        const details = r.questionDetails || [];
        const idx = details.findIndex((qd: any) => qd.questionCode === questionId);
        if (idx === -1) continue;

        const qd = details[idx];
        const wasCorrect = qd.isCorrect;
        const wasAttempted = qd.isAttempted;
        
        let nowCorrect = false;
        if (wasAttempted) {
          nowCorrect = evaluateQuestionAnswer(qType, qd.userAnswer, newCorrectAnswer, qOptions);
        }

        if (wasCorrect === nowCorrect && String(qd.correctAnswer) === String(newCorrectAnswer)) continue;

        const updatedDetails = [...details];
        updatedDetails[idx] = { ...qd, correctAnswer: newCorrectAnswer, isCorrect: nowCorrect };
        
        const marks = qd.marks || 1;
        let newScore = r.score || 0;
        if (wasCorrect && !nowCorrect) {
          newScore -= marks;
          if (wasAttempted) newScore -= negativePerWrong;
        } else if (!wasCorrect && nowCorrect) {
          newScore += marks;
          if (wasAttempted) newScore += negativePerWrong;
        }
        newScore = Math.max(0, newScore);
        const newPct = r.totalMarks ? parseFloat(((newScore / r.totalMarks) * 100).toFixed(1)) : r.percentage;

        batch.update(doc.ref, {
          questionDetails: updatedDetails,
          score: newScore,
          percentage: newPct
        });

        // Also update matching examAttempts document
        const attemptRef = adminDb.collection('examAttempts').doc(doc.id);
        batch.update(attemptRef, {
          score: newScore,
          percentage: newPct
        });
        updatedCount++;
      }

      await batch.commit();
      return NextResponse.json({ message: 'Answer updated and all attempts re-scored successfully.', updatedCount });
    }

    if (!attemptId) {
      return NextResponse.json({ message: 'Missing parameters (attemptId).' }, { status: 400 });
    }

    if (action === 'delete') {
      await Promise.all([
        adminDb.collection('reviews').doc(attemptId).delete(),
        adminDb.collection('examAttempts').doc(attemptId).delete()
      ]);
      return NextResponse.json({ message: 'Attempt deleted successfully.' });
    }

    if (action === 'update') {
      await Promise.all([
        adminDb.collection('reviews').doc(attemptId).update(updates),
        adminDb.collection('examAttempts').doc(attemptId).update(updates)
      ]);
      return NextResponse.json({ message: 'Attempt updated successfully.' });
    }

    return NextResponse.json({ message: 'Invalid action.' }, { status: 400 });

  } catch (error: any) {
    console.error('API update objective attempt error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

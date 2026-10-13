import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { evaluateQuestionAnswer, isMultipleChoiceType, parseAnswerList } from '@/lib/questionTypes';
import { getCachedSyllabus, getFromCache, setInCache } from '@/lib/firebase/cache';
import { ReportCacheManager } from '@/lib/reportCache';
import { isDemoUser } from '@/lib/studentDb';
import { getDateKeyIST, getMidnightIST } from '@/lib/dateUtils';
import { MasteryService } from '@/services/mastery.service';
import { ExamService } from '@/services/exam.service';

async function resolveObjectiveExam(inputExamId: string) {
  let snap = await adminDb.collection('exams').doc(inputExamId).get();
  if (snap.exists) return { snap, examId: snap.id };

  const decoded = decodeURIComponent(inputExamId);
  const candidates = new Set<string>([
    decoded,
    inputExamId.replace(/ /g, '+'),
    inputExamId.replace(/\+/g, ' '),
    decoded.replace(/ /g, '+'),
    decoded.replace(/\+/g, ' ')
  ]);

  for (const cand of candidates) {
    if (cand && cand !== inputExamId) {
      snap = await adminDb.collection('exams').doc(cand).get();
      if (snap.exists) return { snap, examId: snap.id };
    }
  }

  const clean = (s: string) => (s || '').toLowerCase().replace(/[^a-z0-9]/g, '');
  const targetClean = clean(decoded);

  // Short-circuit: if input is empty or invalid, return not found immediately
  if (!targetClean) {
    return { snap, examId: inputExamId };
  }

  // Attempt direct query by examId field before scanning collection
  const directFieldQuery = await adminDb.collection('exams').where('examId', '==', inputExamId).limit(1).get().catch(() => null);
  if (directFieldQuery && !directFieldQuery.empty) {
    return { snap: directFieldQuery.docs[0], examId: directFieldQuery.docs[0].id };
  }

  // Use cached exams list (5-minute TTL) to avoid expensive full DB scan on every non-exact request
  const CACHE_KEY = 'all_exams_summary_for_fuzzy';
  let cachedDocs = getFromCache<any[]>(CACHE_KEY);
  if (!cachedDocs) {
    const allExamsSnap = await adminDb.collection('exams').select('title', 'name', 'examId', 'id').get();
    cachedDocs = allExamsSnap.docs;
    setInCache(CACHE_KEY, cachedDocs, 300000); // 5 min TTL
  }

  let bestCandidate: { snap: any; examId: string } | null = null;
  let highestScore = 0;

  for (const doc of cachedDocs) {
    const data = doc.data();
    let score = 0;

    if (doc.id === inputExamId || doc.id === decoded || data.id === inputExamId || data.examId === inputExamId) {
      score = 1000;
    } else if (clean(doc.id) === targetClean) {
      score = 900;
    } else if (clean(data.title || data.name || '') === targetClean) {
      score = 850;
    } else {
      const docClean = clean(doc.id);
      if (targetClean.length > 10 && docClean.length > 10) {
        let matchingChars = 0;
        const minLen = Math.min(targetClean.length, docClean.length);
        for (let i = 0; i < minLen; i++) {
          if (targetClean[i] === docClean[i]) matchingChars++;
        }
        const similarity = matchingChars / Math.max(targetClean.length, docClean.length);
        if (similarity > 0.6) {
          score = Math.round(similarity * 800);
        }
      }
    }

    if (score > highestScore) {
      highestScore = score;
      bestCandidate = { snap: doc, examId: doc.id };
    }
  }

  if (bestCandidate && highestScore >= 500) {
    // If the doc was only a projected summary, fetch full document for caller
    const fullSnap = await adminDb.collection('exams').doc(bestCandidate.examId).get();
    return { snap: fullSnap.exists ? fullSnap : bestCandidate.snap, examId: bestCandidate.examId };
  }

  return { snap, examId: inputExamId };
}

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

    const { snap: examSnap, examId: resolvedExamId } = await resolveObjectiveExam(examId);
    if (!examSnap || !examSnap.exists) {
      return NextResponse.json({ message: 'Exam not found.' }, { status: 404 });
    }

    // On-demand proctoring snapshots fetch for a specific student attempt (keeps main report fast & lightweight)
    const snapshotsAttemptId = searchParams.get('snapshotsAttemptId');
    const snapshotsStudentCode = searchParams.get('snapshotsStudentCode');
    if (snapshotsAttemptId || (snapshotsStudentCode && examId)) {
      let attemptDoc: any = null;
      if (snapshotsAttemptId) {
        const doc = await adminDb.collection('examAttempts').doc(snapshotsAttemptId).get();
        if (doc.exists) attemptDoc = doc;
      }
      if (!attemptDoc && snapshotsStudentCode) {
        const directDoc = await adminDb.collection('examAttempts').doc(`${resolvedExamId}_${snapshotsStudentCode}`).get();
        if (directDoc.exists) {
          attemptDoc = directDoc;
        } else {
          const q = await adminDb.collection('examAttempts')
            .where('examId', '==', resolvedExamId)
            .where('studentCode', '==', snapshotsStudentCode)
            .limit(1)
            .get();
          if (!q.empty) attemptDoc = q.docs[0];
        }
      }
      if (attemptDoc && attemptDoc.exists) {
        const attData = attemptDoc.data() || {};
        const completedAt = attData.completedAt?.toDate ? attData.completedAt.toDate() : (attData.completedAt ? new Date(attData.completedAt) : null);
        const startedAt = attData.startedAt?.toDate ? attData.startedAt.toDate() : (attData.startedAt ? new Date(attData.startedAt) : null);
        const snapshotsExpiresAt = attData.proctoringSnapshotsExpiresAt || (completedAt ? getMidnightIST(completedAt).toISOString() : (startedAt ? getMidnightIST(startedAt).toISOString() : null));
        const todayKeyIST = getDateKeyIST(new Date());
        const attemptDateKey = completedAt ? getDateKeyIST(completedAt) : (startedAt ? getDateKeyIST(startedAt) : null);
        const isPastDay = attemptDateKey ? attemptDateKey < todayKeyIST : false;
        const isExpired = isPastDay || (snapshotsExpiresAt ? Date.now() >= new Date(snapshotsExpiresAt).getTime() : false);
        const rawSnapshots = isExpired ? [] : (attData.proctoringSnapshots || []);
        return NextResponse.json({
          snapshots: rawSnapshots,
          isPurged: isExpired,
          snapshotsExpiresAt
        });
      }
      return NextResponse.json({ snapshots: [], isPurged: true, snapshotsExpiresAt: null });
    }

    const cacheKey = `exam-report-objective-${resolvedExamId}`;
    const cached = await ReportCacheManager.getReport(cacheKey);
    if (cached) {
      return NextResponse.json(cached);
    }

    // Load reviews, attempts, assignments, students, batches, syllabus, and parent evaluations in parallel
    // NOTE: Projected select on examAttempts prevents multi-megabyte base64 webcam dumps across network
    const [reviewsSnap, attemptsSnap, assignmentsSnap, studentsSnap, batchesSnap, syllabusList, evalSnaps] = await Promise.all([
      adminDb.collection('reviews').where('examId', '==', resolvedExamId).get(),
      adminDb.collection('examAttempts').where('examId', '==', resolvedExamId).select('studentCode', 'startedAt', 'completedAt', 'proctoringSnapshotsExpiresAt').get(),
      adminDb.collection('batchAssignments').where('examId', '==', resolvedExamId).get(),
      adminDb.collection('users').where('role', '==', 'student').select('studentCode', 'name', 'batchId', 'batchIds', 'autonomous', 'status', 'lastLoginAt', 'lastActiveAt').get(),
      adminDb.collection('batches').select('name').get(),
      getCachedSyllabus(),
      adminDb.collection('evaluations').where('examId', '==', resolvedExamId).get()
    ]);

    const attemptsMap = new Map<string, any>();
    attemptsSnap.docs.forEach(doc => {
      const d = doc.data();
      attemptsMap.set(doc.id, d);
      if (d.studentCode) {
        attemptsMap.set(`${resolvedExamId}_${d.studentCode}`, d);
        attemptsMap.set(d.studentCode, d);
      }
    });

    const evalApprovedMap = new Map<string, any>();
    evalSnaps.docs.forEach(doc => {
      const d = doc.data();
      const rawEvalDate = d.reviewedAt || d.createdAt || d.updatedAt;
      const evalDate = rawEvalDate ? (rawEvalDate.toDate ? rawEvalDate.toDate() : new Date(rawEvalDate)) : null;
      const info = { ...d, evalDate };
      if (d.attemptId) evalApprovedMap.set(d.attemptId, info);
      if (d.legacyId) evalApprovedMap.set(d.legacyId, info);
      if (d.studentCode) evalApprovedMap.set(`${resolvedExamId}_${d.studentCode}`, info);
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

    const nowMs = Date.now();
    const attempts = reviewsSnap.docs.map(doc => {
      const data = doc.data();
      const rawAttempt = attemptsMap.get(doc.id) || attemptsMap.get(`${resolvedExamId}_${data.studentCode}`) || attemptsMap.get(data.studentCode) || {};
      const rawStarted = data.startedAt || rawAttempt.startedAt || data.createdAt;
      const startedAt = rawStarted ? (rawStarted.toDate ? rawStarted.toDate() : new Date(rawStarted)) : null;
      const rawCompleted = data.completedAt || rawAttempt.completedAt || data.updatedAt;
      const completedAt = rawCompleted ? (rawCompleted.toDate ? rawCompleted.toDate() : new Date(rawCompleted)) : null;
      const isApproved = data.status === 'approved' || !!evalApprovedMap.get(doc.id) || !!evalApprovedMap.get(`${examId}_${data.studentCode}`);
      const evalInfo = evalApprovedMap.get(doc.id) || evalApprovedMap.get(`${examId}_${data.studentCode}`);
      const rawReviewed = data.reviewedAt || evalInfo?.evalDate || (isApproved ? completedAt : null);
      const reviewedAt = rawReviewed ? (rawReviewed.toDate ? rawReviewed.toDate() : new Date(rawReviewed)) : null;

      const qDetails = (data.questionDetails || []).map((qd: any) => ({
        ...qd,
        isAttempted: qd.isAttempted !== undefined ? Boolean(qd.isAttempted) : Boolean(qd.isCorrect || (qd.userAnswer !== undefined && qd.userAnswer !== null && qd.userAnswer !== ''))
      }));

      // Automatic same-day 12 AM IST auto-purge check for proctoring snapshots
      const snapshotsExpiresAt = rawAttempt.proctoringSnapshotsExpiresAt || data.proctoringSnapshotsExpiresAt || (completedAt ? getMidnightIST(completedAt).toISOString() : (startedAt ? getMidnightIST(startedAt).toISOString() : null));
      const todayKeyIST = getDateKeyIST(new Date());
      const attemptDateKey = completedAt ? getDateKeyIST(completedAt) : (startedAt ? getDateKeyIST(startedAt) : null);
      const isPastDay = attemptDateKey ? attemptDateKey < todayKeyIST : false;
      const isExpired = isPastDay || (snapshotsExpiresAt ? nowMs >= new Date(snapshotsExpiresAt).getTime() : false);

      // Clean up heavy proctoring screenshots from legacy violations object to prevent multi-megabyte payloads
      let sanitizedViolations = data.violations;
      if (sanitizedViolations && typeof sanitizedViolations === 'object') {
        const { screenshots, proctoringSnapshots: vSnaps, ...restViolations } = sanitizedViolations;
        sanitizedViolations = restViolations;
      }

      return {
        id: doc.id,
        ...data,
        violations: sanitizedViolations,
        questionDetails: qDetails,
        totalMarks: data.totalMarks || examData.totalMarks || 0,
        status: isApproved ? 'approved' : (data.status || 'pending'),
        proctoringSnapshots: [], // Omit heavy base64 images from report overview; fetched on demand when student modal opens
        proctoringSnapshotsExpiresAt: snapshotsExpiresAt,
        proctoringSnapshotsPurged: isExpired,
        startedAt: startedAt ? (startedAt.toISOString ? startedAt.toISOString() : new Date(startedAt).toISOString()) : null,
        completedAt: completedAt ? (completedAt.toISOString ? completedAt.toISOString() : new Date(completedAt).toISOString()) : null,
        reviewedAt: reviewedAt ? (reviewedAt.toISOString ? reviewedAt.toISOString() : new Date(reviewedAt).toISOString()) : null
      };
    }).filter(a => !isDemoUser(a));

    const assignments = assignmentsSnap.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    const students = studentsSnap.docs.map(doc => {
      const data = doc.data();
      return {
        id: doc.id,
        studentCode: data.studentCode || '',
        name: data.name || '',
        email: data.email || '',
        batchId: data.batchId || null,
        batchIds: data.batchIds || [],
        autonomous: data.autonomous || false,
        status: data.status || 'active',
        lastLoginAt: data.lastLoginAt ? (data.lastLoginAt.toDate ? data.lastLoginAt.toDate().toISOString() : new Date(data.lastLoginAt).toISOString()) : null,
        lastActiveAt: data.lastActiveAt ? (data.lastActiveAt.toDate ? data.lastActiveAt.toDate().toISOString() : new Date(data.lastActiveAt).toISOString()) : null
      };
    }).filter(s => s.status !== 'inactive' && !isDemoUser(s));

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

    if (attempts.length > 0) {
      // Completed exams cache for 5 minutes; in-progress exams cache for 30 seconds for blazing-fast navigation
      const ttl = isCompleted ? 300 : 30;
      await ReportCacheManager.setReport(cacheKey, resultReport, ttl, isCompleted);
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

    const { examId: resolvedExamId } = examId ? await resolveObjectiveExam(examId) : { examId: null };
    const finalExamId = resolvedExamId || (attemptId ? (await adminDb.collection('reviews').doc(attemptId).get().then(s => s.data()?.examId).catch(() => null)) : null);
    if (finalExamId) {
      await ReportCacheManager.invalidateReport(`exam-report-objective-${finalExamId}`);
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
      const qType = questionData.type || 'single_mcq';
      const isMulti = isMultipleChoiceType(qType);
      
      let newAnswersList: string[] = [];
      if (Array.isArray(newCorrectAnswer)) {
        newAnswersList = newCorrectAnswer.map(s => String(s).trim()).filter(Boolean);
      } else if (isMulti) {
        newAnswersList = parseAnswerList(newCorrectAnswer);
      } else {
        newAnswersList = [String(newCorrectAnswer).trim()];
      }

      const primaryAnswer = isMulti ? newAnswersList.join(', ') : (newAnswersList[0] || String(newCorrectAnswer));

      await questionRef.update({ 
        correctAnswer: primaryAnswer,
        correctAnswers: newAnswersList
      });

      const qOptions = questionData.options || [];

      // 2. Fetch all reviews for this exam to re-score
      const reviewsSnap = await adminDb.collection('reviews').where('examId', '==', finalExamId).get();
      const { snap: examSnap } = await resolveObjectiveExam(finalExamId || examId);
      const examData = examSnap && examSnap.exists ? examSnap.data()! : {};
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
          nowCorrect = evaluateQuestionAnswer(qType, qd.userAnswer, isMulti ? newAnswersList : primaryAnswer, qOptions);
        }

        const isAnswerUnchanged = isMulti
          ? (Array.isArray(qd.correctAnswers) && JSON.stringify(qd.correctAnswers.sort()) === JSON.stringify(newAnswersList.sort()))
          : String(qd.correctAnswer) === String(primaryAnswer);

        if (wasCorrect === nowCorrect && isAnswerUnchanged) continue;

        const updatedDetails = [...details];
        updatedDetails[idx] = { 
          ...qd, 
          correctAnswer: isMulti ? newAnswersList : primaryAnswer,
          ...(isMulti ? { correctAnswers: newAnswersList } : {}),
          isCorrect: nowCorrect 
        };
        
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
      await ReportCacheManager.invalidatePattern(finalExamId || examId);
      return NextResponse.json({ message: 'Answer updated and all attempts re-scored successfully.', updatedCount });
    }

    if (!attemptId) {
      return NextResponse.json({ message: 'Missing parameters (attemptId).' }, { status: 400 });
    }

    if (action === 'delete') {
      let targetExamId = examId;
      let targetStudentCode = '';

      // Check reviews doc
      const reviewSnap = await adminDb.collection('reviews').doc(attemptId).get();
      if (reviewSnap.exists) {
        const rData = reviewSnap.data() || {};
        targetExamId = targetExamId || rData.examId;
        targetStudentCode = rData.studentCode || '';
      }

      // Check examAttempts doc if not found
      if (!targetExamId) {
        const attemptSnap = await adminDb.collection('examAttempts').doc(attemptId).get();
        if (attemptSnap.exists) {
          const aData = attemptSnap.data() || {};
          targetExamId = targetExamId || aData.examId;
          targetStudentCode = targetStudentCode || aData.studentCode || '';
        }
      }

      const deletePromises: Promise<any>[] = [
        adminDb.collection('reviews').doc(attemptId).delete(),
        adminDb.collection('examAttempts').doc(attemptId).delete()
      ];

      if (targetExamId && targetStudentCode) {
        const compositeId = `${targetExamId}_${targetStudentCode}`;
        if (compositeId !== attemptId) {
          deletePromises.push(adminDb.collection('reviews').doc(compositeId).delete());
          deletePromises.push(adminDb.collection('examAttempts').doc(compositeId).delete());
        }

        // Also delete any evaluations linked to this attempt
        const evalSnap = await adminDb.collection('evaluations')
          .where('examId', '==', targetExamId)
          .where('studentCode', '==', targetStudentCode)
          .get();
        evalSnap.docs.forEach(d => deletePromises.push(d.ref.delete()));
      }

      await Promise.all(deletePromises);

      if (targetExamId && targetStudentCode) {
        try {
          const examDoc = await adminDb.collection('exams').doc(targetExamId).get();
          const eData = examDoc.exists ? examDoc.data() : null;
          const targetTopicCodes: string[] = [];
          if (eData?.topicCode) targetTopicCodes.push(eData.topicCode);
          if (Array.isArray(eData?.topicCodes)) eData.topicCodes.forEach((tc: any) => targetTopicCodes.push(String(tc)));
          await MasteryService.recalculateOrPurgeTopicsForStudent({
            studentCode: targetStudentCode,
            excludedExamId: targetExamId,
            candidateTopicCodes: targetTopicCodes
          });
        } catch (mErr) {
          console.warn('Error recalculating topics for deleted attempt:', mErr);
        }
      }

      if (targetExamId) {
        await ReportCacheManager.invalidateReport(`exam-report-objective-${targetExamId}`);
      }

      return NextResponse.json({ message: 'Attempt reset/deleted successfully.' });
    }

    if (action === 'resetAllAttempts') {
      const { examId, targetType, targetStudents } = body;
      if (!examId) {
        return NextResponse.json({ message: 'Missing examId parameter.' }, { status: 400 });
      }
      const result = await ExamService.resetExamAttemptsAndRecordsForReassignment({
        examId,
        type: 'objective',
        targetType: targetType || 'batch',
        targetStudents: targetStudents || []
      });
      return NextResponse.json({ message: 'All attempts reset successfully.', ...result });
    }

    return NextResponse.json({ message: 'Invalid action.' }, { status: 400 });

  } catch (error: any) {
    console.error('API update objective attempt error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export const PUT = POST;


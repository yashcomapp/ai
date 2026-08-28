import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole, verifyAnyRole } from '@/lib/auth';
import { IntegrityService } from '@/services/integrity.service';
import { deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';
import { getStudentResultsData } from '@/lib/resultsDb';
export const dynamic = 'force-dynamic';

function determineExamType(data: any): string {
  if (data.examType === 'practice') return 'practice';
  if (data.examType === 'subjective') return 'subjective';
  const qDetails = data.questionDetails || [];
  const hasSubjective = qDetails.some((qd: any) => {
    const code = qd.questionCode || '';
    const qType = qd.type || '';
    
    // Unified subjective code detection: typeCode starts with 'S'
    const parts = code.split('-');
    const typeCode = parts.length >= 2 ? parts[parts.length - 2] : '';
    const isSubjectiveCode = typeCode.startsWith('S');
    
    return qType.startsWith('subjective') || 
           (qType.includes('reason') && qType !== 'assertion_reason') || 
           qType.includes('notes') || 
           qType.includes('differentiate') ||
           isSubjectiveCode ||
           code.includes('-SA-') || 
           code.includes('-LA-') || 
           code.includes('-SR-') || 
           code.includes('-SN-') || 
           code.includes('-DF-') || 
           code.includes('-LP-');
  });
  if (hasSubjective) return 'subjective';
  return data.examType || 'objective';
}

export async function GET(req: NextRequest) {
  try {
    const authResult = await verifyAnyRole(req, ['student', 'parent', 'admin']);
    if (!authResult) {
      return NextResponse.json({ message: 'Unauthorized. Student, Parent or Admin role required.' }, { status: 403 });
    }
    const { role } = authResult;
    const student = role === 'student' ? authResult : null;
    const parent = role === 'parent' ? authResult : null;
    const adminUser = role === 'admin' ? authResult : null;

    const { searchParams } = new URL(req.url);
    const id = searchParams.get('id');
    const paramStudentCode = searchParams.get('studentCode');

    let studentCode = student?.userData?.studentCode || '';
    if (adminUser && paramStudentCode) {
      studentCode = paramStudentCode;
    } else if (parent) {
      const parentData = parent.userData;
      let studentCodes: string[] = [];
      if (Array.isArray(parentData?.studentCodes)) {
        studentCodes = parentData.studentCodes.filter(Boolean);
      } else if (parentData?.studentCode) {
        studentCodes = [parentData.studentCode];
      }
      
      const parentEmail = parentData?.email?.toLowerCase();
      if (parentEmail) {
        const querySnap = await adminDb.collection('users')
          .where('role', '==', 'student')
          .where('parentEmail', '==', parentEmail)
          .get();
        querySnap.docs.forEach(doc => {
          const data = doc.data();
          if (data.studentCode && !studentCodes.includes(data.studentCode)) {
            studentCodes.push(data.studentCode);
          }
        });
      }
      studentCode = paramStudentCode || '';
      if (!studentCodes.includes(studentCode)) {
        if (id) {
          // Fallback: If id is provided, we can fetch the document first and verify if its studentCode is one of parent's children
          // We will perform that check right below.
        } else {
          return NextResponse.json({ message: 'Forbidden. You do not have permission to view results for this student.' }, { status: 403 });
        }
      }
    }

    if (!studentCode && !id) {
      return NextResponse.json({ message: 'Missing student identifier profile.' }, { status: 400 });
    }

    if (id) {
      // 1. Fetch details of a single review submission (try reviews first, then parentReviews)
      let reviewSnap = await adminDb.collection('reviews').doc(id).get();
      let reviewData: any = null;
      let isPractice = false;
      let evaluationsList: any[] = [];
      let isSubjective = false;
      let evaluationsSnap: any = { docs: [] };

      if (reviewSnap.exists) {
        reviewData = reviewSnap.data()!;
      } else {
        const pSnap = await adminDb.collection('parentReviews').doc(id).get();
        if (pSnap.exists) {
          reviewData = pSnap.data()!;
          isPractice = true;
        } else {
          // Try loading from subjectiveAttempts!
          const subSnap = await adminDb.collection('subjectiveAttempts').doc(id).get();
          if (subSnap.exists) {
            const subData = subSnap.data()!;
            isSubjective = true;

            // Load evaluations and reviews for this attempt
            const [evalSnap, subReviewsSnap] = await Promise.all([
              adminDb.collection('evaluations')
                .where('attemptId', '==', id)
                .get(),
              adminDb.collection('subjectiveReviews')
                .where('attemptId', '==', id)
                .get()
            ]);

            const evalsList = evalSnap.docs.map(doc => doc.data());
            
            // Merge subjectiveReviews into evalsList
            subReviewsSnap.docs.forEach(doc => {
              const rData = doc.data();
              if (Array.isArray(rData.questionReviews)) {
                rData.questionReviews.forEach((qr: any) => {
                  evalsList.push({
                    questionId: qr.questionId,
                    evaluatorType: rData.reviewerType || 'parent',
                    evaluatorName: rData.reviewerId || 'Evaluator',
                    marksAwarded: Number(qr.marksAwarded) || 0,
                    maxMarks: Number(qr.maxMarks) || 0,
                    feedback: qr.feedback || '',
                    stepMarks: qr.stepMarks || [],
                    attemptId: rData.attemptId,
                    examId: rData.examId
                  });
                });
              }
            });

            reviewData = {
              id: subSnap.id,
              studentCode: subData.studentCode,
              examId: subData.examId,
              examCode: subData.examId,
              examName: subData.examName || '',
              examType: 'subjective',
              score: subData.finalScore !== undefined ? subData.finalScore : (subData.peerScore !== undefined ? subData.peerScore : (subData.parentScore !== undefined ? subData.parentScore : 0)),
              totalMarks: subData.totalMarks || 0,
              totalQuestions: subData.questionIds?.length || 0,
              percentage: subData.totalMarks > 0 ? Math.round(((subData.finalScore !== undefined ? subData.finalScore : (subData.peerScore !== undefined ? subData.peerScore : (subData.parentScore !== undefined ? subData.parentScore : 0))) / (subData.totalMarks || 1)) * 100) : 0,
              durationSpent: subData.timeSpentSeconds || 0,
              submittedAt: subData.completedAt || subData.startedAt || null,
              status: subData.status,
              tabViolations: subData.tabViolations || 0,
              proctoringViolations: subData.violations || {},
              questionCodes: [],
              questionDetails: (subData.questionSnapshot || []).map((q: any) => ({
                questionId: q.id,
                questionCode: q.questionCode,
                text: q.text,
                type: q.type || 'subjective',
                marks: q.marks
              }))
            };

            evaluationsList = evalsList;
          }
        }
      }

      if (!reviewData && studentCode) {
        // Try looking up review by composite ID ${studentCode}_${id}
        const compSnap = await adminDb.collection('reviews').doc(`${studentCode}_${id}`).get();
        if (compSnap.exists) {
          reviewData = compSnap.data()!;
        } else {
          // Try looking up review by query
          const qSnap = await adminDb.collection('reviews')
            .where('studentCode', '==', studentCode)
            .where('examId', '==', id)
            .limit(1)
            .get();
          if (!qSnap.empty) {
            reviewData = qSnap.docs[0].data();
          } else {
            // Try looking up subjectiveAttempt by query
            const subQSnap = await adminDb.collection('subjectiveAttempts')
              .where('studentCode', '==', studentCode)
              .where('examId', '==', id)
              .limit(1)
              .get();
            if (!subQSnap.empty) {
              const subDoc = subQSnap.docs[0];
              const subData = subDoc.data();
              isSubjective = true;

              const [evalSnap, subReviewsSnap] = await Promise.all([
                adminDb.collection('evaluations')
                  .where('attemptId', '==', subDoc.id)
                  .get(),
                adminDb.collection('subjectiveReviews')
                  .where('attemptId', '==', subDoc.id)
                  .get()
              ]);

              const evalsList = evalSnap.docs.map(doc => doc.data());
              subReviewsSnap.docs.forEach(doc => {
                const rData = doc.data();
                if (Array.isArray(rData.questionReviews)) {
                  rData.questionReviews.forEach((qr: any) => {
                    evalsList.push({
                      questionId: qr.questionId,
                      evaluatorType: rData.reviewerType || 'parent',
                      evaluatorName: rData.reviewerId || 'Evaluator',
                      marksAwarded: Number(qr.marksAwarded) || 0,
                      maxMarks: Number(qr.maxMarks) || 0,
                      feedback: qr.feedback || '',
                      stepMarks: qr.stepMarks || [],
                      attemptId: rData.attemptId,
                      examId: rData.examId
                    });
                  });
                }
              });

              reviewData = {
                id: subDoc.id,
                studentCode: subData.studentCode,
                examId: subData.examId,
                examCode: subData.examId,
                examName: subData.examName || '',
                examType: 'subjective',
                score: subData.finalScore !== undefined ? subData.finalScore : (subData.peerScore !== undefined ? subData.peerScore : (subData.parentScore !== undefined ? subData.parentScore : 0)),
                totalMarks: subData.totalMarks || 0,
                totalQuestions: subData.questionIds?.length || 0,
                percentage: subData.totalMarks > 0 ? Math.round(((subData.finalScore !== undefined ? subData.finalScore : (subData.peerScore !== undefined ? subData.peerScore : (subData.parentScore !== undefined ? subData.parentScore : 0))) / (subData.totalMarks || 1)) * 100) : 0,
                durationSpent: subData.timeSpentSeconds || 0,
                submittedAt: subData.completedAt || subData.startedAt || null,
                status: subData.status,
                tabViolations: subData.tabViolations || 0,
                proctoringViolations: subData.violations || {},
                questionCodes: [],
                questionDetails: (subData.questionSnapshot || []).map((q: any) => ({
                  questionId: q.id,
                  questionCode: q.questionCode,
                  text: q.text,
                  type: q.type || 'subjective',
                  marks: q.marks
                }))
              };

              evaluationsList = evalsList;
            }
          }
        }
      }

      if (!reviewData) {
        return NextResponse.json({ message: 'Result report not found. The student may have been absent or no scorecard was recorded.' }, { status: 404 });
      }

      // Check results release constraint for autonomous students
      const isAutonomous = student?.userData?.autonomous === true;
      if (student && isAutonomous && !isPractice) {
        const studentBatches = student?.userData?.batchIds || [];
        if (studentBatches.length > 0) {
          const baSnap = await adminDb.collection('batchAssignments')
            .where('examId', '==', reviewData.examId || reviewData.examCode || '')
            .where('status', '==', 'active')
            .get();
          const matchingAssignment = baSnap.docs
            .map((doc: any) => doc.data())
            .find((data: any) => {
              const targets = data.targetBatches || [];
              return targets.some((b: string) => studentBatches.includes(b));
            });
          if (matchingAssignment && matchingAssignment.endAt) {
            const endAtDate = matchingAssignment.endAt.toDate ? matchingAssignment.endAt.toDate() : new Date(matchingAssignment.endAt);
            if (new Date() < endAtDate) {
              return NextResponse.json({ 
                message: `Access Denied. Results for this exam will be released directly after the stipulated end time: ${endAtDate.toLocaleString('en-IN')}` 
              }, { status: 403 });
            }
          }
        }
      }

      if (!isSubjective) {
        evaluationsSnap = await adminDb.collection('evaluations')
          .where('studentCode', '==', reviewData.studentCode)
          .where('evaluatorType', '==', 'parent')
          .get();
        evaluationsList = evaluationsSnap.docs.map((doc: any) => doc.data());
      }

      if (parent) {
        // Strict parent authorization check on the retrieved document
        const parentData = parent.userData;
        let studentCodes: string[] = [];
        if (Array.isArray(parentData?.studentCodes)) {
          studentCodes = parentData.studentCodes.filter(Boolean);
        } else if (parentData?.studentCode) {
          studentCodes = [parentData.studentCode];
        }
        const parentEmail = parentData?.email?.toLowerCase();
        if (parentEmail) {
          const querySnap = await adminDb.collection('users')
            .where('role', '==', 'student')
            .where('parentEmail', '==', parentEmail)
            .get();
          querySnap.docs.forEach(doc => {
            const data = doc.data();
            if (data.studentCode && !studentCodes.includes(data.studentCode)) {
              studentCodes.push(data.studentCode);
            }
          });
        }
        if (!studentCodes.includes(reviewData.studentCode)) {
          return NextResponse.json({ message: 'Access denied to this report.' }, { status: 403 });
        }
      } else if (!adminUser && reviewData.studentCode !== studentCode) {
        return NextResponse.json({ message: 'Access denied to this report.' }, { status: 403 });
      }

      if (isPractice) {
        const qList = Array.isArray(reviewData.questions) ? reviewData.questions : (Array.isArray(reviewData.questionDetails) ? reviewData.questionDetails : []);
        const total = qList.length > 0 ? qList.length : (reviewData.totalQuestions || 1);
        const score = reviewData.score !== undefined && reviewData.score !== null
          ? Number(reviewData.score)
          : (reviewData.correctCount !== undefined && reviewData.correctCount !== null
              ? Number(reviewData.correctCount)
              : qList.filter((q: any) => q.isCorrect).length);
        const percentage = reviewData.scorePercent !== undefined && reviewData.scorePercent !== null
          ? Number(reviewData.scorePercent)
          : (reviewData.percentage !== undefined && reviewData.percentage !== null
              ? Number(reviewData.percentage)
              : (total > 0 ? Math.round((score / total) * 100) : 0));

        reviewData.examCode = reviewData.topicCode || '';
        reviewData.examName = reviewData.topicName || 'Practice Session';
        reviewData.score = score;
        reviewData.totalQuestions = total;
        reviewData.totalMarks = total;
        reviewData.percentage = percentage;
        reviewData.examType = 'practice';
        reviewData.status = reviewData.parentStatus || 'pending';

        // Calculate duration spent dynamically from startedAt and createdAt/updatedAt
        const start = reviewData.startedAt?.toDate ? reviewData.startedAt.toDate() : (reviewData.startedAt ? new Date(reviewData.startedAt) : null);
        const end = reviewData.createdAt?.toDate ? reviewData.createdAt.toDate() : (reviewData.updatedAt?.toDate ? reviewData.updatedAt.toDate() : (reviewData.completedAt?.toDate ? reviewData.completedAt.toDate() : null));
        let calculatedDuration = reviewData.durationSpent || 0;
        if (!calculatedDuration && start && end && !isNaN(start.getTime()) && !isNaN(end.getTime())) {
          calculatedDuration = Math.max(0, Math.floor((end.getTime() - start.getTime()) / 1000));
        }
        reviewData.durationSpent = calculatedDuration;

        // If questionDetails is missing on parentReview, hydrate from practiceSubmissions
        if ((!reviewData.questionDetails || reviewData.questionDetails.length === 0) && (!reviewData.questions || reviewData.questions.length === 0)) {
          try {
            // Try loading from practiceSubmissions by doc ID or practiceSessionId
            const candidateIds = [
              id,
              reviewData.practiceSessionId,
              `${reviewData.studentCode}_PRACTICE_${reviewData.topicCode}_${reviewData.practiceSessionId}`,
              `${reviewData.studentCode}_PRACTICE_${reviewData.topicCode}_${id}`
            ].filter(Boolean);

            let subDocFound: any = null;
            for (const subId of candidateIds) {
              const subDoc = await adminDb.collection('practiceSubmissions').doc(subId).get();
              if (subDoc.exists) {
                subDocFound = subDoc.data();
                break;
              }
            }

            if (!subDocFound && reviewData.studentCode && reviewData.topicCode) {
              const subQuery = await adminDb.collection('practiceSubmissions')
                .where('studentCode', '==', reviewData.studentCode)
                .where('topicCode', '==', reviewData.topicCode)
                .orderBy('submittedAt', 'desc')
                .limit(5)
                .get();
              if (!subQuery.empty) {
                // Pick closest submission by time
                const targetTime = (reviewData.createdAt?.toDate ? reviewData.createdAt.toDate() : new Date(reviewData.createdAt || Date.now())).getTime();
                let closest = subQuery.docs[0];
                let minDiff = Infinity;
                subQuery.docs.forEach(doc => {
                  const sTime = doc.data().submittedAt?.toDate ? doc.data().submittedAt.toDate().getTime() : 0;
                  const diff = Math.abs(sTime - targetTime);
                  if (diff < minDiff) {
                    minDiff = diff;
                    closest = doc;
                  }
                });
                subDocFound = closest.data();
              }
            }

            if (subDocFound && Array.isArray(subDocFound.questions)) {
              reviewData.questionDetails = subDocFound.questions.map((q: any) => ({
                questionId: q.id || q.questionId || '',
                questionCode: q.questionCode || q.id || '',
                questionText: q.text || q.assertion || '',
                text: q.text || q.assertion || '',
                type: q.type || 'single_mcq',
                options: q.options || [],
                userAnswer: q.userAnswer ?? '',
                correctAnswer: q.correctAnswer ?? '',
                correctAnswers: q.correctAnswers || [],
                isCorrect: !!q.isCorrect,
                solution: q.solution || q.explanation || '',
                difficulty: q.difficulty || 'medium',
                bloomLevel: q.bloomLevel || 'Understand',
                marks: q.marks || 1
              }));
            }
          } catch (pSubErr) {
            console.warn('Could not backfill practice questions from practiceSubmissions:', pSubErr);
          }
        }
      }

      // Fetch full question docs to show correct answers and explanations
      const questionCodes = reviewData.questionCodes || [];
      let questionDetails = (reviewData.questionDetails && reviewData.questionDetails.length > 0)
        ? reviewData.questionDetails
        : (reviewData.questions || []);

      const questionsMap: Record<string, any> = {};

      // If review is linked to an official exam, load the questions array directly from the exam document
      const wrongAnswersSet = new Set(Array.isArray(reviewData.wrongAnswers) ? reviewData.wrongAnswers : []);
      const unattemptedSet = new Set(Array.isArray(reviewData.unattemptedQuestions) ? reviewData.unattemptedQuestions : []);
      const isPerfectScore = (Number(reviewData.score || 0) >= Number(reviewData.totalMarks || 1) && Number(reviewData.totalMarks || 0) > 0);

      if (reviewData.examId) {
        try {
          const examDoc = await adminDb.collection('exams').doc(reviewData.examId).get();
          if (examDoc.exists) {
            const eData = examDoc.data() || {};
            const examCodes = eData.questionCodes || eData.questions || [];
            if (questionDetails.length === 0 && examCodes.length > 0) {
              questionDetails = examCodes.map((code: any, idx: number) => {
                const qCode = typeof code === 'string' ? code : (code.questionCode || code.id || '');
                const isWrong = wrongAnswersSet.has(qCode) || wrongAnswersSet.has(idx);
                const isUnattempted = unattemptedSet.has(qCode) || unattemptedSet.has(idx);
                const isCorrect = isPerfectScore ? true : (!isWrong && !isUnattempted);

                return {
                  questionCode: qCode,
                  questionId: qCode,
                  isAttempted: !isUnattempted,
                  isCorrect,
                  marks: eData.positiveMarks || 4
                };
              });
              if (!reviewData.totalMarks || reviewData.totalMarks === 0) {
                reviewData.totalMarks = eData.totalMarks || (examCodes.length * (eData.positiveMarks || 4));
              }
            }
            if (!reviewData.examName || reviewData.examName === reviewData.examId) {
              reviewData.examName = eData.name || eData.examName || reviewData.examName;
            }
            if (!reviewData.chapter && eData.chapter) {
              reviewData.chapter = eData.chapter;
            }
            if (!reviewData.subject && (eData.subject || eData.subjectName)) {
              reviewData.subject = eData.subject || eData.subjectName;
            }
            const examQuestions = eData.questions || [];
            if (Array.isArray(examQuestions)) {
              examQuestions.forEach((q: any) => {
                if (q.id) questionsMap[q.id] = q;
                if (q.questionCode) questionsMap[q.questionCode] = q;
              });
            }
          }
        } catch (eErr) {
          console.warn('Failed to load exam doc for scorecard hydration:', eErr);
        }
      }

      // Query database for all unique questionCodes in the exam
      const uniqueCodes = Array.from(new Set<string>([
        ...questionCodes,
        ...questionDetails.map((qd: any) => qd.questionCode).filter(Boolean),
        ...questionDetails.map((qd: any) => qd.questionId || qd.id).filter(Boolean)
      ]));

      // 1. Fetch by Document IDs in batch
      if (uniqueCodes.length > 0) {
        const refs = uniqueCodes.map(code => adminDb.collection('questions').doc(code));
        const docSnaps = await adminDb.getAll(...refs).catch(() => []);
        docSnaps.forEach(ds => {
          if (ds && ds.exists) {
            const data = ds.data()!;
            questionsMap[ds.id] = { id: ds.id, ...data };
            if (data.questionCode) {
              questionsMap[data.questionCode] = { id: ds.id, ...data };
            }
          }
        });
      }

      // 2. Fetch by questionCode field in chunks of 30 for any items not found by doc ID
      const missingCodes = uniqueCodes.filter(c => !questionsMap[c]);
      if (missingCodes.length > 0) {
        const chunks = [];
        for (let i = 0; i < missingCodes.length; i += 30) {
          chunks.push(missingCodes.slice(i, i + 30));
        }

        const queries = chunks.map(chunk =>
          adminDb.collection('questions')
            .where('questionCode', 'in', chunk)
            .get()
        );

        const queryResults = await Promise.all(queries);
        queryResults.forEach(snap => {
          snap.docs.forEach(doc => {
            const data = doc.data();
            questionsMap[doc.id] = { id: doc.id, ...data };
            if (data.questionCode) {
              questionsMap[data.questionCode] = { id: doc.id, ...data };
            }
          });
        });
      }

      // Determine accurate question counts based on actual score
      const totalQ = questionDetails.length || 1;
      const scoreVal = Number(reviewData.score || 0);
      const maxMarksVal = Number(reviewData.totalMarks || (totalQ * 4) || 1);
      const marksPerQ = maxMarksVal > 0 && totalQ > 0 ? (maxMarksVal / totalQ) : 4;
      const computedCorrectCount = isPerfectScore 
        ? totalQ 
        : Math.min(totalQ, Math.max(0, Math.round(scoreVal / (marksPerQ || 4))));

      const hasExplicitMistakes = wrongAnswersSet.size > 0 || unattemptedSet.size > 0;

      // Construct a merged question review scorecard
      const questionsWithAnswers = questionDetails.map((qd: any, index: number) => {
        const qCode = qd.questionCode || qd.id || '';
        const qDb = questionsMap[qCode] || 
                    questionsMap[qd.questionId] || 
                    questionsMap[qd.id] || 
                    Object.values(questionsMap).find((q: any) => q.id === (qd.questionId || qd.id) || q.questionCode === qCode) || 
                    {};

        // Find evaluations for this specific question
        const qEvaluations = (evaluationsList || []).filter((e: any) => e.questionId === (qd.questionId || qd.id || qDb.id));

        let resolvedIsCorrect = false;
        if (qd.isCorrect !== undefined && typeof qd.isCorrect === 'boolean') {
          resolvedIsCorrect = qd.isCorrect;
        } else if (hasExplicitMistakes) {
          const isWrong = wrongAnswersSet.has(qCode) || wrongAnswersSet.has(index);
          const isUnattempted = unattemptedSet.has(qCode) || unattemptedSet.has(index);
          resolvedIsCorrect = !isWrong && !isUnattempted;
        } else {
          // Fall back to score-proportion distribution so correct/incorrect counters match the score exactly
          resolvedIsCorrect = index < computedCorrectCount;
        }

        const rawOptions = (qDb.options && Array.isArray(qDb.options) && qDb.options.length > 0) ? qDb.options : (qd.options || []);
        const correctAns = qd.correctAnswer || qDb.correctAnswer || (Array.isArray(qDb.correctAnswers) ? qDb.correctAnswers[0] : '');
        
        let resolvedUserAns = qd.userAnswer !== undefined && qd.userAnswer !== null ? String(qd.userAnswer) : '';
        const isExplicitlyUnattempted = unattemptedSet.has(qCode) || 
                                        unattemptedSet.has(index) || 
                                        (Array.isArray(reviewData.unattemptedQuestions) && reviewData.unattemptedQuestions.includes(qCode)) ||
                                        (!resolvedIsCorrect && qd.userAnswer === '');

        if (resolvedIsCorrect) {
          if (!resolvedUserAns || resolvedUserAns === '') {
            resolvedUserAns = correctAns;
          }
        } else if (isExplicitlyUnattempted) {
          resolvedUserAns = ''; // Keep strictly blank for unattempted (0 marks)
        } else {
          // Wrong question (-1 mark)
          if (!resolvedUserAns || resolvedUserAns === '' || resolvedUserAns === correctAns) {
            if (Array.isArray(rawOptions) && rawOptions.length > 1) {
              const wrongOpt = rawOptions.find((opt: any) => {
                const optText = typeof opt === 'string' ? opt : (opt.text || opt.value || '');
                return optText !== correctAns && optText !== '';
              });
              resolvedUserAns = wrongOpt ? (typeof wrongOpt === 'string' ? wrongOpt : (wrongOpt.text || wrongOpt.value || '')) : 'B';
            } else {
              resolvedUserAns = correctAns === 'A' ? 'B' : 'A';
            }
          }
        }

        return {
          id: qd.questionId || qd.id || qDb.id || '',
          questionCode: qCode || qDb.questionCode || '',
          text: qDb.text || qDb.assertion || qd.questionText || qd.text || qd.assertion || '',
          type: qDb.type || qd.type || 'single_mcq',
          options: rawOptions,
          assertion: qDb.assertion || qd.assertion || '',
          reason: qDb.reason || qd.reason || '',
          solution: qDb.solution || qDb.explanation || qDb.solutionText || qd.solution || qd.explanation || '',
          difficulty: qDb.difficulty || qd.difficulty || 'medium',
          bloomLevel: qDb.bloomLevel || qd.bloomLevel || 'Understand',
          userAnswer: resolvedUserAns,
          isCorrect: resolvedIsCorrect,
          correctAnswer: correctAns,
          correctAnswers: Array.isArray(qd.correctAnswer)
            ? qd.correctAnswer
            : (Array.isArray(qd.correctAnswers) && qd.correctAnswers.length > 0
                ? qd.correctAnswers
                : (Array.isArray(qDb.correctAnswers) ? qDb.correctAnswers : (qDb.correctAnswer ? [qDb.correctAnswer] : []))),
          marks: qd.marks || qDb.marks || 0,
          steps: qDb.steps || [],
          evaluations: qEvaluations.map((ev: any) => ({
            evaluatorType: ev.evaluatorType,
            evaluatorName: ev.evaluatorName,
            marksAwarded: ev.marksAwarded,
            maxMarks: ev.maxMarks,
            feedback: ev.feedback,
            stepMarks: ev.stepMarks || []
          }))
        };
      });

      let subject = reviewData.subject || '';
      let chapter = reviewData.chapter || '';
      let topicName = '';

      if (determineExamType(reviewData) === 'practice' && reviewData.examName) {
        try {
          const tSnap = await adminDb.collection('syllabusTopicIndex').doc(reviewData.examName).get();
          if (tSnap.exists) {
            const tData = tSnap.data()!;
            subject = tData.subjectName || '';
            chapter = tData.chapterName || '';
            topicName = tData.topicName || '';
          }
        } catch {}
      } else {
        // Resolve topic names for formal exams from question details
        const examTopics = new Set<string>();
        const qDetails = reviewData.questionDetails || [];
        const uniqueQdCodes = Array.from(new Set<string>([
          ...(reviewData.questionCodes || []),
          ...qDetails.map((qd: any) => qd.questionCode).filter(Boolean)
        ]));
        
        const topicCodesForLookup = uniqueQdCodes.map(code => deriveTopicCodeFromQuestionCode(code)).filter(Boolean);
        if (topicCodesForLookup.length > 0) {
          const refs = Array.from(new Set(topicCodesForLookup)).map(code => adminDb.collection('syllabusTopicIndex').doc(code));
          const syllabusSnaps = refs.length > 0 ? await adminDb.getAll(...refs).catch(() => []) : [];
          syllabusSnaps.forEach(snap => {
            if (snap && snap.exists) {
              const sData = snap.data();
              if (sData && sData.topicName) {
                examTopics.add(sData.topicName);
                if (sData.subjectName) subject = sData.subjectName;
                if (sData.chapterName) chapter = sData.chapterName;
              }
            }
          });
        }
        if (examTopics.size > 0) {
          topicName = Array.from(examTopics).join(', ');
        }
      }

      const resolvedSubmittedAt = reviewData.submittedAt || reviewData.completedAt || reviewData.processedAt || null;

      return NextResponse.json({
        id,
        examCode: reviewData.examCode,
        examName: topicName || reviewData.examName || reviewData.examCode,
        examType: determineExamType(reviewData),
        score: reviewData.score || 0,
        totalMarks: reviewData.totalMarks || reviewData.totalQuestions || 0,
        percentage: reviewData.percentage ?? Math.round(((reviewData.score || 0) / (reviewData.totalMarks || reviewData.totalQuestions || 1)) * 100),
        durationSpent: reviewData.durationSpent || reviewData.totalSeconds || 0,
        submittedAt: resolvedSubmittedAt?.toDate ? resolvedSubmittedAt.toDate().toISOString() : resolvedSubmittedAt || null,
        tabViolations: reviewData.tabViolations || 0,
        subject,
        chapter,
        topicName,
        practiceNumber: reviewData.practiceNumber || null,
        violations: reviewData.violations || null,
        proctoringViolations: reviewData.proctoringViolations || reviewData.violations || {},
        integrityScore: (() => {
          if (reviewData.integrityScore !== undefined && reviewData.integrityScore !== null) {
            return reviewData.integrityScore;
          }
          const tabViols = Number(reviewData.tabViolations || 0);
          const pViols = reviewData.proctoringViolations || reviewData.violations || {};
          const normViols = {
            noFace: Number(pViols.noFace || pViols.noFaceCount || 0),
            lookingAway: Number(pViols.lookingAway || pViols.lookingAwayCount || 0),
            multipleFaces: Number(pViols.multipleFaces || pViols.multipleFacesCount || 0),
            headMovement: Number(pViols.headMovement || pViols.headMovementCount || 0)
          };
          return IntegrityService.calculateScore(tabViols, normViols).integrityScore;
        })(),
        status: (() => {
          if (reviewData.status === 'approved') return 'approved';
          if (isSubjective) return reviewData.status;
          const hasEval = evaluationsSnap.docs.some((doc: any) => {
            const d = doc.data();
            return d.attemptId === id || d.legacyId === id || d.attemptId === reviewData.examCode || d.legacyId === reviewData.examCode;
          });
          return hasEval ? 'approved' : (reviewData.status || 'pending');
        })(),
        wrongAnswerReasons: reviewData.wrongAnswerReasons || [],
        questions: questionsWithAnswers
      });
    }

    const isListAutonomous = student?.userData?.autonomous === true;
    const studentBatches = student?.userData?.batchIds || [];

    const data = await getStudentResultsData(studentCode, isListAutonomous, studentBatches);
    return NextResponse.json(data);

  } catch (error: any) {
    console.error('API get results error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

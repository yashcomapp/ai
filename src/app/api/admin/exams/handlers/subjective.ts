import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ReportCacheManager } from '@/lib/reportCache';
import { chunkArray } from '@/lib/firestoreUtils';
import { MasteryService } from '@/services/mastery.service';
export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const examId = searchParams.get('examId') || '';
    const attemptId = searchParams.get('attemptId') || '';

    // Scenario A: Load details of a specific attempt (with model answers)
    if (attemptId) {
      const attemptSnap = await adminDb.collection('subjectiveAttempts').doc(attemptId).get();
      if (!attemptSnap.exists) {
        return NextResponse.json({ message: 'Attempt not found.' }, { status: 404 });
      }
      const attempt = attemptSnap.data()!;

      const examSnap = await adminDb.collection('subjectiveExams').doc(attempt.examId).get();
      const exam = examSnap.exists ? examSnap.data()! : {};

      // Load questions (favoring questionSnapshot if saved, then inline exam.questions)
      let questions: any[] = [];
      if (Array.isArray(attempt.questionSnapshot) && attempt.questionSnapshot.length > 0) {
        questions = attempt.questionSnapshot;
      } else if (exam && Array.isArray(exam.questions) && exam.questions.length > 0) {
        questions = exam.questions;
      } else {
        const questionIds = attempt.questionIds || exam.questionIds || [];
        if (questionIds.length > 0) {
          const refs = questionIds.map((qid: string) => adminDb.collection('questions').doc(qid));
          const snaps = await adminDb.getAll(...refs).catch(() => []);
          questions = snaps
            .filter((s: any): s is admin.firestore.DocumentSnapshot => !!s && s.exists)
            .map(s => ({ id: s.id, ...s.data() }));
        }
      }

      // Load evaluations and subjectiveReviews for student attempt
      const [evaluationsSnap, reviewsSnap] = await Promise.all([
        adminDb.collection('evaluations')
          .where('attemptId', '==', attemptId)
          .get(),
        adminDb.collection('subjectiveReviews')
          .where('attemptId', '==', attemptId)
          .get()
      ]);

      let evaluationsList = evaluationsSnap.docs.map(doc => doc.data());
      if (evaluationsList.length === 0) {
        const fallbackSnap = await adminDb.collection('evaluations')
          .where('studentCode', '==', attempt.studentCode)
          .where('examId', '==', attempt.examId)
          .get();
        evaluationsList = fallbackSnap.docs.map(doc => doc.data());
      }

      // Merge per-question review items from subjectiveReviews
      reviewsSnap.docs.forEach(doc => {
        const rData = doc.data();
        if (Array.isArray(rData.questionReviews)) {
          rData.questionReviews.forEach((qr: any) => {
            evaluationsList.push({
              questionId: qr.questionId,
              evaluatorType: rData.reviewerType || 'parent',
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

      return NextResponse.json({
        attempt: { id: attemptSnap.id, ...attempt },
        exam: { id: examSnap.id, ...exam },
        questions,
        evaluations: evaluationsList
      });
    }

    // Scenario B: Load all attempts for a given examId
    if (!examId) {
      return NextResponse.json({ message: 'Missing parameters (examId or attemptId).' }, { status: 400 });
    }

    const cacheKey = `exam-report-subjective-${examId}`;
    const cached = await ReportCacheManager.getReport(cacheKey);
    if (cached) {
      return NextResponse.json(cached);
    }

    const examSnap = await adminDb.collection('subjectiveExams').doc(examId).get();
    if (!examSnap.exists) {
      return NextResponse.json({ message: 'Exam not found.' }, { status: 404 });
    }

    const attemptsSnap = await adminDb.collection('subjectiveAttempts')
      .where('examId', '==', examId)
      .where('status', 'in', ['completed', 'parent_reviewed', 'peer_reviewed', 'approved', 'peer_review_pending'])
      .get();

    const attemptsMap = new Map<string, any>();
    attemptsSnap.docs.forEach(doc => {
      const data = doc.data();
      const parentScore = data.parentScore !== undefined ? data.parentScore : null;
      const peerScore = data.peerScore !== undefined ? data.peerScore : null;
      const totalMarks = data.totalMarks || 0;

      let flagged = false;
      if (parentScore !== null && peerScore !== null && totalMarks > 0) {
        const diff = Math.abs(parentScore - peerScore);
        flagged = (diff / totalMarks) > 0.25;
      }

      const studentCode = data.studentCode || '';
      const createdAtRaw = data.createdAt?.toDate ? data.createdAt.toDate() : (data.createdAt ? new Date(data.createdAt) : null);
      const createdAtTime = createdAtRaw ? createdAtRaw.getTime() : 0;

      const attemptObj = {
        id: doc.id,
        studentCode,
        status: data.status || '',
        parentScore,
        peerScore,
        finalScore: data.finalScore !== undefined ? data.finalScore : null,
        totalMarks,
        isFinalReviewed: !!data.isFinalReviewed,
        flagged,
        createdAtTime,
        weeklyAvgPercent: null as number | null,
        examPercent: null as number | null,
        truthPercent: null as number | null
      };

      const existing = attemptsMap.get(studentCode);
      if (!existing) {
        attemptsMap.set(studentCode, attemptObj);
      } else {
        const newIsCompleted = attemptObj.status !== 'completed';
        const existingIsCompleted = existing.status !== 'completed';
        
        if (newIsCompleted && !existingIsCompleted) {
          attemptsMap.set(studentCode, attemptObj);
        } else if (!newIsCompleted && existingIsCompleted) {
          // Keep existing
        } else if (attemptObj.createdAtTime > existing.createdAtTime) {
          attemptsMap.set(studentCode, attemptObj);
        }
      }
    });

    const classroomExam = examSnap.data()!;
    const isClassroomTest = classroomExam.type === 'classroom_test' || classroomExam.mode === 'classroom';
    const attempts = Array.from(attemptsMap.values());

    if (isClassroomTest) {
      // 1. Fetch home practice exams associated
      let homeExamIds = classroomExam.sampledFromHomeExamIds || [];
      if (homeExamIds.length === 0) {
        const classQIds = classroomExam.questionIds || [];
        if (classQIds.length > 0) {
          try {
            const homePracticesSnap = await adminDb.collection('subjectiveExams')
              .where('type', '==', 'home_practice')
              .where('class', '==', classroomExam.class)
              .get();
            homePracticesSnap.docs.forEach(doc => {
              const hData = doc.data();
              const hQIds = hData.questionIds || [];
              if (hQIds.some((id: string) => classQIds.includes(id))) {
                homeExamIds.push(doc.id);
              }
            });
          } catch (e) {
            console.error('Error fetching fallback home exams:', e);
          }
        }
      }
      homeExamIds = Array.from(new Set(homeExamIds));

      // 2. Fetch home exams totalMarks mapping
      const homeExamsMap = new Map();
      if (homeExamIds.length > 0) {
        try {
          const refs = homeExamIds.map((id: string) => adminDb.collection('subjectiveExams').doc(id));
          const snaps = await adminDb.getAll(...refs).catch(() => []);
          snaps.forEach(snap => {
            if (snap && snap.exists) {
              const data = snap.data();
              homeExamsMap.set(snap.id, data?.totalMarks || 10);
            }
          });
        } catch (e) {
          console.error('Error fetching home exams mapping:', e);
        }
      }

      // 3. Fetch parent reviews and peer reviews in parallel
      let parentReviews: any[] = [];
      let classReviews: any[] = [];
      try {
        const fetchQueries = [];
        if (homeExamIds.length > 0) {
          const chunks = chunkArray(homeExamIds, 30);
          chunks.forEach(chunk => {
            fetchQueries.push(
              adminDb.collection('subjectiveReviews')
                .where('examId', 'in', chunk)
                .where('reviewerType', '==', 'parent')
                .get()
            );
          });
        }
        fetchQueries.push(adminDb.collection('subjectiveReviews').where('examId', '==', examId).get());

        const querySnaps = await Promise.all(fetchQueries);
        const classSnap = querySnaps[querySnaps.length - 1];
        classReviews = classSnap.docs.map(doc => doc.data());

        const parentSnaps = querySnaps.slice(0, querySnaps.length - 1);
        parentSnaps.forEach(snap => {
          snap.docs.forEach((doc: any) => {
            parentReviews.push(doc.data());
          });
        });
      } catch (e) {
        console.error('Error fetching reviews:', e);
      }

      // 4. Map reviews by studentCode
      const studentHomePercentsMap = new Map();
      parentReviews.forEach(rev => {
        const sCode = rev.revieweeCode || rev.studentCode;
        if (!sCode) return;
        const maxMarks = homeExamsMap.get(rev.examId) || 10;
        const pct = (rev.totalScore / maxMarks) * 100;
        if (!studentHomePercentsMap.has(sCode)) {
          studentHomePercentsMap.set(sCode, []);
        }
        studentHomePercentsMap.get(sCode).push(pct);
      });

      const studentParentReviews = new Map();
      parentReviews.forEach(rev => {
        const sCode = rev.revieweeCode || rev.studentCode;
        if (sCode) {
          if (!studentParentReviews.has(sCode)) {
            studentParentReviews.set(sCode, []);
          }
          studentParentReviews.get(sCode).push(rev);
        }
      });

      const studentPeerReviews = new Map();
      classReviews.forEach(rev => {
        const sCode = rev.revieweeCode || rev.studentCode;
        if (sCode) {
          studentPeerReviews.set(sCode, rev);
        }
      });

      // 5. Populate attempt metrics
      attempts.forEach(a => {
        // Average Weekly Percentage
        const pcts = studentHomePercentsMap.get(a.studentCode);
        if (pcts && pcts.length > 0) {
          const sum = pcts.reduce((s: number, p: number) => s + p, 0);
          a.weeklyAvgPercent = Math.round(sum / pcts.length);
        }

        // Exam Percentage
        const score = a.finalScore !== null ? a.finalScore : a.peerScore;
        if (score !== null && a.totalMarks > 0) {
          a.examPercent = Math.round((score / a.totalMarks) * 100);
        }

        // Truth Percentage based on overlapping questions
        const peerRev = studentPeerReviews.get(a.studentCode);
        const parentRevs = studentParentReviews.get(a.studentCode) || [];

        if (peerRev && Array.isArray(peerRev.questionReviews) && parentRevs.length > 0) {
          let matched = 0;
          let aligned = 0;

          peerRev.questionReviews.forEach((pQr: any) => {
            const qId = pQr.questionId;
            if (!qId) return;

            // Find parent review for this exact question
            let foundParentMarks = null;
            for (const pRev of parentRevs) {
              if (Array.isArray(pRev.questionReviews)) {
                const pQrMatch = pRev.questionReviews.find((q: any) => q.questionId === qId);
                if (pQrMatch && pQrMatch.marksAwarded !== undefined && pQrMatch.marksAwarded !== null) {
                  foundParentMarks = Number(pQrMatch.marksAwarded);
                  break;
                }
              }
            }

            if (foundParentMarks !== null && pQr.marksAwarded !== undefined && pQr.marksAwarded !== null) {
              matched++;
              const diff = Math.abs(foundParentMarks - Number(pQr.marksAwarded));
              if (diff <= 0.5) {
                aligned++;
              }
            }
          });

          if (matched > 0) {
            a.truthPercent = Math.round((aligned / matched) * 100);
          }
        }
      });
    }

    const resultReport = {
      exam: { id: examSnap.id, ...examSnap.data() },
      attempts
    };

    const now = new Date();
    let isCompleted = true;
    try {
      const assignmentsSnap = await adminDb.collection('subjectiveAssignments')
        .where('examId', '==', examId)
        .get();
      assignmentsSnap.docs.forEach(doc => {
        const data = doc.data();
        const endAt = data.endAt?.toDate ? data.endAt.toDate() : new Date(data.endAt);
        if (now < endAt) {
          isCompleted = false;
        }
      });
    } catch {}

    await ReportCacheManager.setReport(cacheKey, resultReport, isCompleted ? 604800 : 60, isCompleted);

    return NextResponse.json(resultReport);

  } catch (error: any) {
    console.error('API load subjective attempts error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 2. POST - Finalize grading or delete/reset attempt for a subjective exam
export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { action, attemptId } = body;

    if (action === 'delete') {
      if (!attemptId) {
        return NextResponse.json({ message: 'Missing parameters (attemptId).' }, { status: 400 });
      }

      const attemptRef = adminDb.collection('subjectiveAttempts').doc(attemptId);
      const attemptSnap = await attemptRef.get();
      if (!attemptSnap.exists) {
        return NextResponse.json({ message: 'Attempt document not found.' }, { status: 404 });
      }
      const attempt = attemptSnap.data()!;
      const examId = attempt.examId;

      if (examId) {
        await ReportCacheManager.invalidateReport(`exam-report-subjective-${examId}`);
      }

      // Delete subjectiveAttempts document
      await attemptRef.delete();

      const batch = adminDb.batch();

      // Delete subjectiveReviews documents
      const reviewsSnap = await adminDb.collection('subjectiveReviews')
        .where('attemptId', '==', attemptId)
        .get();
      reviewsSnap.docs.forEach(doc => {
        batch.delete(doc.ref);
      });

      // Delete evaluations documents
      const evaluationsSnap = await adminDb.collection('evaluations')
        .where('attemptId', '==', attemptId)
        .get();
      evaluationsSnap.docs.forEach(doc => {
        batch.delete(doc.ref);
      });

      // Reset peerAssignments status back to pending
      if (attempt.studentCode && examId) {
        const peerSnap = await adminDb.collection('peerAssignments')
          .where('revieweeStudentCode', '==', attempt.studentCode)
          .where('examId', '==', examId)
          .get();
        peerSnap.docs.forEach(doc => {
          batch.update(doc.ref, {
            status: 'pending',
            completedAt: null,
            submittedAt: null,
            score: null
          });
        });
      }

      await batch.commit();
      return NextResponse.json({ success: true, message: 'Attempt reset successfully.' });
    }

    const { questionReviews, totalScore } = body;

    if (!attemptId || !questionReviews || totalScore === undefined) {
      return NextResponse.json({ message: 'Missing parameters (attemptId, questionReviews, totalScore).' }, { status: 400 });
    }

    const attemptRef = adminDb.collection('subjectiveAttempts').doc(attemptId);
    const attemptSnap = await attemptRef.get();
    if (!attemptSnap.exists) {
      return NextResponse.json({ message: 'Attempt document not found.' }, { status: 404 });
    }
    const attempt = attemptSnap.data()!;
    if (attempt.examId) {
      await ReportCacheManager.invalidateReport(`exam-report-subjective-${attempt.examId}`);
    }

    // A. Add record to subjectiveReviews
    const reviewData = {
      attemptId,
      examId: attempt.examId,
      reviewerId: (adminUser.decodedToken?.email || adminUser.userData?.email) || 'admin@yashcom.com',
      reviewerType: 'admin',
      questionReviews,
      totalScore: Number(totalScore) || 0,
      isFinal: true,
      submittedAt: new Date(),
      createdAt: new Date()
    };
    await adminDb.collection('subjectiveReviews').add(reviewData);

    // B. Update subjectiveAttempt details
    await attemptRef.update({
      finalScore: Number(totalScore) || 0,
      finalReviewerType: 'admin',
      finalReviewedAt: new Date(),
      isFinalReviewed: true,
      status: 'parent_reviewed' // or keeping it aligned with parent reviews approved statuses
    });

    // C. Write teacher evaluations records
    const attemptMode = attempt.mode || 'home';
    await Promise.all(
      questionReviews.map((qr: any) =>
        adminDb.collection('evaluations').add({
          studentCode: attempt.studentCode,
          questionId: qr.questionId,
          attemptId: attemptId,
          examId: attempt.examId,
          evaluatorType: 'teacher',
          evaluatorId: adminUser.decodedToken?.uid,
          evaluatorName: (adminUser.decodedToken?.email || adminUser.userData?.email) || 'admin@yashcom.com',
          marksAwarded: Number(qr.marksAwarded) || 0,
          maxMarks: Number(qr.maxMarks) || 0,
          feedback: qr.feedback || '',
          stepMarks: qr.stepMarks || [],
          modelAnswerVersion: 'v1.0',
          attemptMode,
          evaluationType: 'subjective',
          isFinal: true,
          createdAt: new Date(),
          updatedAt: new Date()
        }).catch(e => console.warn(`Error writing teacher evaluation for question ${qr.questionId}:`, e.message))
      )
    );

    // D. Process topic mastery updates for Class 10 students
    try {
      let questions: any[] = [];
      if (Array.isArray(attempt.questionSnapshot) && attempt.questionSnapshot.length > 0) {
        questions = attempt.questionSnapshot;
      } else if (attempt.examId) {
        const examSnap = await adminDb.collection('subjectiveExams').doc(attempt.examId).get();
        if (examSnap.exists) {
          questions = examSnap.data()?.questions || [];
        }
      }

      await MasteryService.processSubjectiveMasteryUpdate({
        studentCode: attempt.studentCode,
        examId: attempt.examId,
        questions,
        questionReviews
      });
    } catch (masteryErr: any) {
      console.warn('Could not update topic mastery from admin subjective review:', masteryErr?.message || masteryErr);
    }

    return NextResponse.json({ success: true, message: 'Grades finalized successfully.' });

  } catch (error: any) {
    console.error('API finalize subjective grading error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

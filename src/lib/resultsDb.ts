import { adminDb } from '@/lib/firebase/admin';
import { IntegrityService } from '@/services/integrity.service';
import { deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';

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

export async function getStudentResultsData(
  studentCode: string,
  isListAutonomous: boolean,
  studentBatches: string[]
) {
  // 2. Fetch list of all results for this student (exams from reviews, practice from parentReviews, subjective from subjectiveAttempts)
  const [reviewsSnap, parentReviewsSnap, evaluationsSnap, assignmentsSnap, subjectiveAttemptsSnap] = await Promise.all([
    adminDb.collection('reviews').where('studentCode', '==', studentCode).get(),
    adminDb.collection('parentReviews').where('studentCode', '==', studentCode).get(),
    adminDb.collection('evaluations')
      .where('studentCode', '==', studentCode)
      .where('evaluatorType', '==', 'parent')
      .get(),
    isListAutonomous && studentBatches.length > 0
      ? adminDb.collection('batchAssignments')
          .where('status', '==', 'active')
          .get()
      : Promise.resolve({ docs: [] } as any),
    adminDb.collection('subjectiveAttempts').where('studentCode', '==', studentCode).get()
  ]);

  const assignments = assignmentsSnap.docs
    .map((doc: any) => doc.data())
    .filter((data: any) => {
      const targets = data.targetBatches || [];
      return targets.some((b: string) => studentBatches.includes(b));
    });

  // Group all unique topic codes from formal exam questions to resolve their names in batch
  const allTopicCodes = new Set<string>();
  reviewsSnap.docs.forEach(doc => {
    const data = doc.data();
    const qDetails = data.questionDetails || [];
    qDetails.forEach((qd: any) => {
      const code = qd.questionCode;
      if (code) {
        const tCode = deriveTopicCodeFromQuestionCode(code);
        if (tCode) {
          allTopicCodes.add(tCode);
        }
      }
    });
  });

  // Extract topic codes from subjective attempts as well
  subjectiveAttemptsSnap.docs.forEach(doc => {
    const data = doc.data();
    const qDetails = data.questionSnapshot || [];
    qDetails.forEach((qd: any) => {
      const code = qd.questionCode;
      if (code) {
        const tCode = deriveTopicCodeFromQuestionCode(code);
        if (tCode) {
          allTopicCodes.add(tCode);
        }
      }
    });
  });

  const uniqueTopicCodes = Array.from(allTopicCodes);
  const refs = uniqueTopicCodes.map(code => adminDb.collection('syllabusTopicIndex').doc(code));
  const syllabusSnaps = refs.length > 0 ? await adminDb.getAll(...refs).catch(() => []) : [];

  const syllabusMap = new Map<string, any>();
  syllabusSnaps.forEach(snap => {
    if (snap && snap.exists) {
      syllabusMap.set(snap.id, snap.data());
    }
  });

  const examResults = reviewsSnap.docs.map(doc => {
    const data = doc.data();

    // Check results release constraint for autonomous students
    if (isListAutonomous) {
      const matchingAssignment = assignments.find((a: any) => a.examId === data.examId || a.examId === data.examCode);
      if (matchingAssignment && matchingAssignment.endAt) {
        const endAtDate = matchingAssignment.endAt.toDate ? matchingAssignment.endAt.toDate() : new Date(matchingAssignment.endAt);
        if (new Date() < endAtDate) {
          return null; // Restricted / Hidden
        }
      }
    }

    const score = data.score || 0;
    const total = data.totalMarks || data.totalQuestions || 1;
    const percentage = data.percentage ?? Math.round((score / total) * 100);

    let subject = data.subject || '';
    let chapter = data.chapter || '';
    let topicName = '';

    const examTopics = new Set<string>();
    const qDetails = data.questionDetails || [];
    qDetails.forEach((qd: any) => {
      const code = qd.questionCode;
      if (code) {
        const tCode = deriveTopicCodeFromQuestionCode(code);
        if (tCode) {
          const sData = syllabusMap.get(tCode);
          if (sData && sData.topicName) {
            examTopics.add(sData.topicName);
          }
        }
      }
    });
    if (examTopics.size > 0) {
      topicName = Array.from(examTopics).join(', ');
    }

    const resolvedSubmittedAt = data.submittedAt || data.completedAt || data.processedAt || null;

    return {
      id: doc.id,
      examCode: data.examCode,
      examName: topicName || data.examName || data.examCode,
      examType: determineExamType(data),
      score,
      totalQuestions: data.totalQuestions || 0,
      totalMarks: total,
      percentage,
      durationSpent: data.durationSpent || data.totalSeconds || 0,
      submittedAt: resolvedSubmittedAt?.toDate ? resolvedSubmittedAt.toDate().toISOString() : resolvedSubmittedAt || null,
      status: (() => {
        if (data.status === 'approved' || data.parentStatus === 'approved') return 'approved';
        const hasEval = evaluationsSnap.docs.some(evDoc => {
          const d = evDoc.data();
          return d.attemptId === doc.id || 
                 d.legacyId === doc.id || 
                 d.attemptId === data.examCode || 
                 d.legacyId === data.examCode ||
                 d.examId === data.examId ||
                 (data.examId && d.legacyId && d.legacyId.startsWith(data.examId));
        });
        return hasEval ? 'approved' : (data.status || 'pending');
      })(),
      subject,
      chapter,
      topicName,
      suspiciousLevel: (() => {
        if (data.suspiciousLevel) return data.suspiciousLevel;
        const integrityScore = (() => {
          if (data.integrityScore !== undefined && data.integrityScore !== null) {
            return data.integrityScore;
          }
          const tabViols = Number(data.tabViolations || 0);
          const pViols = data.proctoringViolations || data.violations || {};
          const normViols = {
            noFace: Number(pViols.noFace || pViols.noFaceCount || 0),
            lookingAway: Number(pViols.lookingAway || pViols.lookingAwayCount || 0),
            multipleFaces: Number(pViols.multipleFaces || pViols.multipleFacesCount || 0),
            headMovement: Number(pViols.headMovement || pViols.headMovementCount || 0)
          };
          return IntegrityService.calculateScore(tabViols, normViols).integrityScore;
        })();
        return integrityScore < 70 ? 'red' : (integrityScore < 90 ? 'yellow' : 'green');
      })()
    };
  });

  const mappedPracticeResults = parentReviewsSnap.docs.map(doc => {
    const data = doc.data();
    const qList = Array.isArray(data.questions) ? data.questions : (Array.isArray(data.questionDetails) ? data.questionDetails : []);
    const total = qList.length > 0 ? qList.length : (data.totalQuestions || 1);
    const score = data.score !== undefined && data.score !== null
      ? Number(data.score)
      : (data.correctCount !== undefined && data.correctCount !== null
          ? Number(data.correctCount)
          : qList.filter((q: any) => q.isCorrect).length);
    const percentage = data.scorePercent !== undefined && data.scorePercent !== null
      ? Number(data.scorePercent)
      : (data.percentage !== undefined && data.percentage !== null
          ? Number(data.percentage)
          : (total > 0 ? Math.round((score / total) * 100) : 0));

    const resolvedSubmittedAt = data.submittedAt || data.createdAt || data.updatedAt || data.startedAt || null;

    // Calculate duration spent dynamically from startedAt and createdAt/updatedAt
    const start = data.startedAt?.toDate ? data.startedAt.toDate() : (data.startedAt ? new Date(data.startedAt) : null);
    const end = data.createdAt?.toDate ? data.createdAt.toDate() : (data.updatedAt?.toDate ? data.updatedAt.toDate() : (resolvedSubmittedAt?.toDate ? resolvedSubmittedAt.toDate() : (resolvedSubmittedAt ? new Date(resolvedSubmittedAt) : null)));
    let calculatedDuration = data.durationSpent || 0;
    if (!calculatedDuration && start && end && !isNaN(start.getTime()) && !isNaN(end.getTime())) {
      calculatedDuration = Math.max(0, Math.floor((end.getTime() - start.getTime()) / 1000));
    }

    const rawTimestamp = start ? start.getTime() : (end ? end.getTime() : 0);

    const isPracticeApproved = data.parentStatus === 'approved' || 
                               data.status === 'approved' || 
                               evaluationsSnap.docs.some(e => e.data().attemptId === doc.id || e.data().legacyId === doc.id);

    return {
      id: doc.id,
      examCode: data.topicCode || '',
      examName: data.topicName || 'Practice Session',
      examType: 'practice',
      score,
      totalQuestions: total,
      totalMarks: total,
      percentage,
      durationSpent: calculatedDuration,
      submittedAt: resolvedSubmittedAt?.toDate ? resolvedSubmittedAt.toDate().toISOString() : resolvedSubmittedAt || null,
      rawTimestamp,
      status: isPracticeApproved ? 'approved' : (data.parentStatus || data.status || 'pending'),
      subject: data.subjectName || 'General',
      chapter: data.chapterName || 'General Chapter',
      topicName: data.topicName || '',
      suspiciousLevel: data.suspiciousLevel || 'green'
    };
  });

  // Sort chronologically (oldest first) to compute stable sequential numbers
  const chronologicalPrac = [...mappedPracticeResults].sort((a, b) => a.rawTimestamp - b.rawTimestamp);
  const pracSequenceMap = new Map<string, number>();
  const pracTopicCounts = new Map<string, number>();

  chronologicalPrac.forEach(r => {
    const tCode = r.examCode || 'unknown';
    const nextSeq = (pracTopicCounts.get(tCode) || 0) + 1;
    pracTopicCounts.set(tCode, nextSeq);
    pracSequenceMap.set(r.id, nextSeq);
  });

  const practiceResults = mappedPracticeResults.map(r => {
    const seqNum = pracSequenceMap.get(r.id) || 1;
    return {
      ...r,
      practiceNumber: seqNum
    };
  });

  const finishedStatuses = ['completed', 'peer_review_pending', 'peer_reviewed', 'parent_reviewed', 'approved'];

  const subjectiveResults = subjectiveAttemptsSnap.docs
    .filter(doc => finishedStatuses.includes(doc.data().status))
    .map(doc => {
      const data = doc.data();

      // Check results release constraint for autonomous students
      if (isListAutonomous) {
        const matchingAssignment = assignments.find((a: any) => a.examId === data.examId);
        if (matchingAssignment && matchingAssignment.endAt) {
          const endAtDate = matchingAssignment.endAt.toDate ? matchingAssignment.endAt.toDate() : new Date(matchingAssignment.endAt);
          if (new Date() < endAtDate) {
            return null; // Restricted / Hidden
          }
        }
      }

      const score = data.finalScore !== undefined ? data.finalScore : (data.peerScore !== undefined ? data.peerScore : (data.parentScore !== undefined ? data.parentScore : 0));
      const total = data.totalMarks || 0;
      const percentage = total > 0 ? Math.round((score / total) * 100) : 0;

      let subject = '';
      let chapter = '';
      let topicName = '';

      // Resolve topic names from questionSnapshot
      const examTopics = new Set<string>();
      const qDetails = data.questionSnapshot || [];
      qDetails.forEach((q: any) => {
        const code = q.questionCode;
        if (code) {
          const tCode = deriveTopicCodeFromQuestionCode(code);
          if (tCode) {
            const sData = syllabusMap.get(tCode);
            if (sData && sData.topicName) {
              examTopics.add(sData.topicName);
              if (sData.subjectName) subject = sData.subjectName;
              if (sData.chapterName) chapter = sData.chapterName;
            }
          }
        }
      });
      if (examTopics.size > 0) {
        topicName = Array.from(examTopics).join(', ');
      }

      const resolvedSubmittedAt = data.completedAt || data.startedAt || null;

      return {
        id: doc.id,
        examCode: data.examId,
        examName: topicName || data.examName || data.examId,
        examType: 'subjective',
        score,
        totalQuestions: data.questionIds?.length || 0,
        totalMarks: total,
        percentage,
        durationSpent: data.timeSpentSeconds || 0,
        submittedAt: resolvedSubmittedAt?.toDate ? resolvedSubmittedAt.toDate().toISOString() : resolvedSubmittedAt || null,
        status: data.status,
        subject,
        chapter,
        topicName,
        suspiciousLevel: (() => {
          const integrityScore = data.integrityScore !== undefined ? data.integrityScore : 100;
          return integrityScore < 70 ? 'red' : (integrityScore < 90 ? 'yellow' : 'green');
        })()
      };
    }).filter(Boolean);

  const results = [...(examResults.filter(Boolean) as any[]), ...subjectiveResults, ...practiceResults];

  // Sort by submittedAt descending
  results.sort((a, b) => {
    const da = a.submittedAt ? new Date(a.submittedAt).getTime() : 0;
    const db = b.submittedAt ? new Date(b.submittedAt).getTime() : 0;
    return db - da;
  });

  return { results };
}

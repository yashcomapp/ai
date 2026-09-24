import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { notifyNewExam } from '@/lib/notifications';
import { getDateKeyIST } from '@/lib/dateUtils';
import { getRequiredConfidence, isDemoUser } from '@/lib/studentDb';
import { evaluateSessionSincerity } from '@/lib/practiceTimeUtils';
import { getCanonicalSubjectName, parseTopicCode } from '@/lib/questionTypes';
import { getObjectiveExamTopics, getSubjectiveExamTopics, getExamDateKey, isExamForStudent } from '@/services/quotient.service';
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
  const newDateStr6 = `${day}${month}${year.slice(-2)}`;
  const newDateStr8 = `${day}${month}${year}`;

  const dateRegex6 = /-\d{6}$/;
  if (dateRegex6.test(currentName)) {
    return currentName.replace(dateRegex6, `-${newDateStr6}`);
  }
  const dateRegex8 = /-\d{8}$/;
  if (dateRegex8.test(currentName)) {
    return currentName.replace(dateRegex8, `-${newDateStr8}`);
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
      const [studentUserSnap, masterySnap, parentReviewsSnap, examsSnap, subjExamsSnap] = await Promise.all([
        adminDb.collection('users').where('studentCode', '==', studentCodeParam).where('role', '==', 'student').limit(1).get(),
        adminDb.collection('studentTopicMastery').where('studentCode', '==', studentCodeParam).get(),
        adminDb.collection('parentReviews').where('studentCode', '==', studentCodeParam).get(),
        adminDb.collection('exams').where('status', 'in', ['active', 'draft']).get(),
        adminDb.collection('subjectiveExams').where('status', 'in', ['active', 'draft']).get()
      ]);

      const studentUser = studentUserSnap.docs[0]?.data();
      const bIds = studentUser?.batchIds || (studentUser?.batchId ? [studentUser.batchId] : []);
      const studentClass = studentUser?.class || studentUser?.className || '';
      const todayDateStr = getDateKeyIST();

      const conductedTopicsSet = new Set<string>();

      examsSnap.docs.forEach(doc => {
        const exam = { id: doc.id, ...doc.data() };
        const examDateStr = getExamDateKey(exam) || todayDateStr;
        if (examDateStr <= todayDateStr && isExamForStudent(exam, studentCodeParam, bIds, studentClass)) {
          getObjectiveExamTopics(exam).forEach(t => conductedTopicsSet.add(t));
        }
      });

      subjExamsSnap.docs.forEach(doc => {
        const exam = { id: doc.id, ...doc.data() };
        const examDateStr = getExamDateKey(exam) || todayDateStr;
        if (examDateStr <= todayDateStr && isExamForStudent(exam, studentCodeParam, bIds, studentClass)) {
          getSubjectiveExamTopics(exam).forEach(t => conductedTopicsSet.add(t));
        }
      });

      masterySnap.docs.forEach(d => {
        if (d.data().topicCode) conductedTopicsSet.add(d.data().topicCode);
      });
      parentReviewsSnap.docs.forEach(d => {
        if (d.data().topicCode) conductedTopicsSet.add(d.data().topicCode);
      });

      const practiceCountMap = new Map<string, number>();
      const practiceQuestionsMap = new Map<string, number>();
      parentReviewsSnap.docs.forEach(doc => {
        const data = doc.data();
        const tCode = data.topicCode;
        if (tCode) {
          practiceCountMap.set(tCode, (practiceCountMap.get(tCode) || 0) + 1);
          const qCount = Number(data.questionsCount || data.totalQuestions || (Array.isArray(data.questions) ? data.questions.length : (data.questionDetails?.length || 0)));
          practiceQuestionsMap.set(tCode, (practiceQuestionsMap.get(tCode) || 0) + qCount);
        }
      });

      const topicCodes = Array.from(conductedTopicsSet);
      const queryCodesSet = new Set<string>(topicCodes);
      topicCodes.forEach(tc => {
        const lastDot = tc.lastIndexOf('.');
        if (lastDot !== -1) {
          queryCodesSet.add(tc.substring(0, lastDot));
        }
      });
      const allQueryCodes = Array.from(queryCodesSet);

      const syllabusMap = new Map<string, any>();

      if (allQueryCodes.length > 0) {
        const chunks = [];
        for (let i = 0; i < allQueryCodes.length; i += 30) {
          chunks.push(allQueryCodes.slice(i, i + 30));
        }
        const snaps = await Promise.all(
          chunks.map(chunk => adminDb.collection('syllabusTopicIndex').where('topicCode', 'in', chunk).get())
        );
        snaps.forEach(sSnap => {
          sSnap.docs.forEach(doc => syllabusMap.set(doc.data().topicCode, doc.data()));
        });
      }

      const masteryByTopic = new Map<string, any>();
      masterySnap.docs.forEach(doc => {
        const d = doc.data();
        if (d.topicCode) masteryByTopic.set(d.topicCode, d);
      });

      const mastered: any[] = [];
      const practicing: any[] = [];
      const needsAttention: any[] = [];

      topicCodes.forEach(tCode => {
        const d = masteryByTopic.get(tCode);
        let sData = syllabusMap.get(tCode);
        let parentTopic = null;
        if (!sData && tCode) {
          const lastDot = tCode.lastIndexOf('.');
          if (lastDot !== -1) {
            const parentCode = tCode.substring(0, lastDot);
            parentTopic = syllabusMap.get(parentCode);
          }
        }
        if (!sData && parentTopic) {
          sData = parentTopic;
        }

        const parsed = parseTopicCode(tCode);
        const subCode = sData?.subjectCode || parsed?.subjectCode || (tCode.includes('-') ? tCode.split('-')[2] : '') || '';
        const subName = sData?.subjectName || getCanonicalSubjectName(subCode, tCode, sData?.chapterName);
        const chapName = d?.chapterName || sData?.chapterName || (parsed?.chapterNumber ? `Chapter ${parsed.chapterNumber}` : 'General');
        const chapNum = parsed?.chapterNumber || sData?.chapterNumber || '';
        const topName = d?.topicName || (sData?.topicName ? (parentTopic ? `${sData.topicName} (${parsed?.topicNumber || tCode})` : sData.topicName) : (d?.name || `Topic ${parsed?.topicNumber || tCode}`));

        const practiceCount = practiceCountMap.get(tCode) || 0;
        const attempts = d ? (d.questionsAttempted || d.attempts || 0) : 0;
        const mastery = d ? Number(d.mastery || 0) : 0;
        const confidence = d ? Number(d.confidence || 0) : 0;
        const isRecovery = d ? !!d.isRecoveryMastered : false;
        const classification = sData?.topicClassification || d?.topicClassification;
        const targetQ = sData?.targetQuestions || d?.targetQuestions;
        const reqConfidence = getRequiredConfidence(classification, targetQ);
        const isFullConfidence = confidence >= reqConfidence;
        const rawScope = String(classification || '').toLowerCase().trim();
        const isMinorTopic = rawScope === 'minor' || rawScope === 'micro' || (targetQ !== undefined && targetQ <= 20);
        const maxPractices = isMinorTopic ? 2 : 3;
        const isLimitReached = practiceCount >= maxPractices;

        let state = 'needsAttention';
        let expIcon = '🚨';
        let expColor = 'var(--danger)';
        let expText = '';

        if (!d && attempts === 0 && practiceCount === 0) {
          state = 'needsAttention';
          expIcon = '⚪';
          expColor = 'var(--text-muted)';
          expText = 'Not attempted yet (conducted in batch exams). Start 1st practice to assess concept baseline.';
          needsAttention.push({
            topicCode: tCode,
            topicName: topName,
            subjectName: subName,
            chapterName: chapName,
            chapterNumber: chapNum,
            topicNumber: parsed?.topicNumber || sData?.topicNumber || '',
            mastery: 0,
            confidence: 0,
            practiceCount: 0,
            attempts: 0,
            state,
            expIcon,
            expColor,
            expText
          });
        } else if ((mastery >= 90 && isFullConfidence) || isRecovery) {
          state = 'mastered';
          if (isRecovery) {
            expIcon = '⚡';
            expColor = 'var(--purple)';
            expText = 'Mastered via Recovery Diagnostic (Passed fresh unseen + remediated question assessment).';
          } else {
            expIcon = '⭐';
            expColor = 'var(--success)';
            expText = `Mastered (${mastery}% accuracy across ${attempts} verified questions).`;
          }
          mastered.push({
            topicCode: tCode,
            topicName: topName,
            subjectName: subName,
            chapterName: chapName,
            chapterNumber: chapNum,
            topicNumber: parsed?.topicNumber || sData?.topicNumber || '',
            mastery,
            confidence,
            practiceCount,
            attempts,
            state,
            expIcon,
            expColor,
            expText
          });
        } else if (mastery >= 90 && !isFullConfidence) {
          state = 'revision';
          const needed = Math.max(1, reqConfidence - attempts);
          expIcon = '📖';
          expColor = 'var(--accent)';
          expText = `High accuracy (${mastery}%), but needs ${needed} more verified question(s) to reach full confidence for Mastered.`;
          practicing.push({
            topicCode: tCode,
            topicName: topName,
            subjectName: subName,
            chapterName: chapName,
            chapterNumber: chapNum,
            topicNumber: parsed?.topicNumber || sData?.topicNumber || '',
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
          state = 'continuePractice';
          if (isLimitReached) {
            expIcon = '⚡';
            expColor = 'var(--purple)';
            expText = `${maxPractices}/${maxPractices} practices done (${mastery}% accuracy). Take the Recovery Quiz (Fresh + Missed Qs) to achieve Mastered!`;
          } else {
            expIcon = '📈';
            expColor = 'var(--warning)';
            expText = `${practiceCount}/${maxPractices} practices done (${mastery}% accuracy). Complete 1 practice set (6 Qs) to aim for 90%+ Mastered.`;
          }
          practicing.push({
            topicCode: tCode,
            topicName: topName,
            subjectName: subName,
            chapterName: chapName,
            chapterNumber: chapNum,
            topicNumber: parsed?.topicNumber || sData?.topicNumber || '',
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
            expColor = 'var(--purple)';
            expText = `${maxPractices}/${maxPractices} practices done (${mastery}% accuracy). Take the Recovery Quiz (Fresh + Missed Qs) to achieve Mastered!`;
          } else if (attempts === 0) {
            expIcon = '⚪';
            expColor = 'var(--text-muted)';
            expText = 'Not attempted yet. Start 1st practice to assess concept baseline.';
          } else {
            expIcon = '🚨';
            expColor = 'var(--danger)';
            expText = `${practiceCount}/${maxPractices} practices done (${mastery}% accuracy). ${Math.max(0, maxPractices - practiceCount)} practice(s) left — focus on weak areas.`;
          }
          needsAttention.push({
            topicCode: tCode,
            topicName: topName,
            subjectName: subName,
            chapterName: chapName,
            chapterNumber: chapNum,
            topicNumber: parsed?.topicNumber || sData?.topicNumber || '',
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
      adminDb.collection('users').where('role', '==', 'student').select('studentCode', 'name', 'rollNumber', 'batchIds', 'batchId', 'class', 'className', 'status').get(),
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
        email: data.email || '',
        rollNumber: data.rollNumber || '',
        batchIds: data.batchIds || [],
        batchId: data.batchId || null,
        class: data.class || data.className || '',
        className: data.className || data.class || '',
        status: data.status || 'active'
      };
    }).filter(s => !!s.studentCode && s.status !== 'inactive' && !isDemoUser(s));

    const parents = parentsSnap.docs.map(doc => {
      const data = doc.data();
      if (isDemoUser(data)) return null;
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
    const studentPacingMap: Record<string, number[]> = {};
    
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
      const qCount = Number(data.totalQuestions || data.questionsCount || (Array.isArray(data.questions) ? data.questions.length : (data.questionDetails?.length || 0)));
      stats.questionsAttempted += qCount;
      const percent = data.percentage !== undefined && data.percentage !== null
        ? Number(data.percentage)
        : (data.scorePercent !== undefined && data.scorePercent !== null
          ? Number(data.scorePercent)
          : (data.totalMarks > 0 ? Math.round(((data.score || 0) / data.totalMarks) * 100) : 0));
      stats.avgScore += percent;

      let pacing = data.sincerityPacingScore;
      if (typeof pacing !== 'number') {
        const sincerity = evaluateSessionSincerity({
          questions: data.questions || data.questionDetails || [],
          durationSpent: Number(data.durationSpent || (qCount ? qCount * 35 : 180)),
          scorePercent: Number(data.scorePercent || percent || 100)
        });
        pacing = sincerity.sincerityPacingScore;
      }
      if (!studentPacingMap[code]) studentPacingMap[code] = [];
      studentPacingMap[code].push(pacing);

      const itemDate = data.startedAt?.toDate ? data.startedAt.toDate() : data.createdAt?.toDate ? data.createdAt.toDate() : data.startedAt ? new Date(data.startedAt) : null;
      if (itemDate) {
        if (!stats.lastActive || itemDate > new Date(stats.lastActive)) {
          stats.lastActive = itemDate.toISOString();
        }
      }
    });

    // 2. Calculate average score
    Object.keys(practiceStats).forEach(code => {
      const stats = practiceStats[code];
      if (stats.totalSessions > 0) {
        stats.avgScore = Math.round(stats.avgScore / stats.totalSessions);
      }
    });

    const todayDateStr = getDateKeyIST();

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

    // Map of studentCode -> Map of topicCode -> { mastery, confidence, reqConf, isRecoveryMastered }
    const studentTopicMasteryMap: Record<string, Map<string, { mastery: number, confidence: number, reqConf?: number, isRecoveryMastered?: boolean }>> = {};

    masterySnap.docs.forEach(doc => {
      const data = doc.data();
      const code = data.studentCode;
      if (!code) return;

      const val = Number(data.mastery || 0);
      const conf = Number(data.confidence || 0);
      const tCode = data.topicCode;

      const reqConf = getRequiredConfidence(data.topicClassification, data.targetQuestions);

      if (tCode) {
        if (!studentTopicMasteryMap[code]) {
          studentTopicMasteryMap[code] = new Map();
        }
        studentTopicMasteryMap[code].set(tCode, {
          mastery: val,
          confidence: conf,
          reqConf,
          isRecoveryMastered: Boolean(data.isRecoveryMastered)
        });
      }
    });

    // Build conducted topics per student based on their batch / class / target exams
    const studentConductedTopicsMap: Record<string, string[]> = {};
    students.forEach(s => {
      const code = s.studentCode;
      const bIds = s.batchIds || (s.batchId ? [s.batchId] : []);
      const studentClass = (s as any).class || (s as any).className || '';

      const topicsSet = new Set<string>();

      exams.forEach((exam: any) => {
        const examDateStr = getExamDateKey(exam) || todayDateStr;
        if (examDateStr <= todayDateStr && isExamForStudent(exam, code, bIds, studentClass)) {
          getObjectiveExamTopics(exam).forEach(t => topicsSet.add(t));
        }
      });

      subjectiveExams.forEach((exam: any) => {
        const examDateStr = getExamDateKey(exam) || todayDateStr;
        if (examDateStr <= todayDateStr && isExamForStudent(exam, code, bIds, studentClass)) {
          getSubjectiveExamTopics(exam).forEach(t => topicsSet.add(t));
        }
      });

      // Also include any topics student practiced or has mastery records for
      if (studentTopicMasteryMap[code]) {
        studentTopicMasteryMap[code].forEach((_, t) => topicsSet.add(t));
      }
      if (studentTopicPracticeMap[code]) {
        studentTopicPracticeMap[code].forEach((_, t) => topicsSet.add(t));
      }

      studentConductedTopicsMap[code] = Array.from(topicsSet);
    });

    const masteryStats: Record<string, { avgMastery: number, avgQuality: number, mastered: number, practicing: number, needsAttention: number }> = {};
    students.forEach(s => {
      const code = s.studentCode;
      const conductedTopics = studentConductedTopicsMap[code] || [];
      const masteryMap = studentTopicMasteryMap[code] || new Map();

      let mCount = 0;
      let pCount = 0;
      let naCount = 0;
      let totalMasterySum = 0;

      conductedTopics.forEach(tCode => {
        const record = masteryMap.get(tCode);
        if (record) {
          const val = record.mastery;
          const conf = record.confidence;
          const reqConf = record.reqConf || 10;
          totalMasterySum += val;

          if ((val >= 90 && conf >= reqConf) || record.isRecoveryMastered) {
            mCount++;
          } else if (val >= 50) {
            pCount++;
          } else {
            naCount++;
          }
        } else {
          // Unattempted conducted topic counts as 0% under needsAttention
          naCount++;
        }
      });

      const avg = conductedTopics.length > 0
        ? Math.round(totalMasterySum / conductedTopics.length)
        : 0;

      // Calculate Quality score (40% Session Accuracy + 30% Pacing Sincerity + 30% Mastery Efficiency)
      const topicPractice = studentTopicPracticeMap[code] || new Map<string, number>();
      
      let totalEfficiencyScore = 0;
      let topicsCount = 0;
      topicPractice.forEach((q, topicCode) => {
        const record = masteryMap.get(topicCode) || { mastery: 0, confidence: 0, reqConf: 10 };
        const mastery = record.mastery;
        const confidence = record.confidence;
        const requiredConf = record.reqConf || 10;
        
        let topicEfficiency = 0;
        if (mastery >= 90 && confidence >= requiredConf) {
          const excess = Math.max(0, q - 15);
          topicEfficiency = Math.max(40, 100 - excess * 1.5);
        } else {
          const excess = Math.max(0, q - 15);
          topicEfficiency = Math.max(0, mastery - excess * 1.5);
        }
        totalEfficiencyScore += topicEfficiency;
        topicsCount++;
      });

      const avgEfficiency = topicsCount > 0 ? Math.round(totalEfficiencyScore / topicsCount) : 100;

      const studentPractice = practiceStats[code];
      const hasPractice = studentPractice && studentPractice.totalSessions > 0;
      const avgAccuracy = hasPractice ? studentPractice.avgScore : 0;
      const pacingList = studentPacingMap[code] || [];
      const avgPacing = (hasPractice && pacingList.length > 0)
        ? Math.round(pacingList.reduce((sum, v) => sum + v, 0) / pacingList.length)
        : 100;

      const avgQuality = hasPractice
        ? Math.max(0, Math.min(100, Math.round(avgAccuracy * 0.40 + avgPacing * 0.30 + avgEfficiency * 0.30)))
        : 0;

      masteryStats[code] = {
        avgMastery: avg,
        avgQuality: avgQuality,
        mastered: mCount,
        practicing: pCount,
        needsAttention: naCount
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
    const { 
      id, 
      collection, 
      openMode, 
      startAtStr, 
      endAtStr, 
      attemptLimit, 
      examDuration, 
      status, 
      lateEntryRestriction,
      targetType,
      targetBatches,
      targetStudents
    } = body;

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

    if (targetType) {
      updates.targetType = targetType;
    }
    if (Array.isArray(targetBatches)) {
      updates.targetBatches = targetBatches;
    }
    if (Array.isArray(targetStudents)) {
      updates.targetStudents = targetStudents;
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

// 4. DELETE - Delete an exam along with all related details and release its questions
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

    // Retrieve the target exam document first to inspect questions to release
    const targetCollection = type === 'objective' ? 'exams' : 'subjectiveExams';
    const targetExamDoc = await adminDb.collection(targetCollection).doc(examId).get();
    const targetExamData = targetExamDoc.exists ? targetExamDoc.data() : null;

    const assignedQuestionCodes: string[] = [];
    if (targetExamData) {
      const codes = targetExamData.questionCodes || targetExamData.questionIds || [];
      codes.forEach((c: any) => { if (c) assignedQuestionCodes.push(String(c).trim()); });
      if (Array.isArray(targetExamData.questions)) {
        targetExamData.questions.forEach((q: any) => {
          if (q?.id) assignedQuestionCodes.push(String(q.id).trim());
          if (q?.questionCode) assignedQuestionCodes.push(String(q.questionCode).trim());
        });
      }
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

    // Release questions back into question bank vault if not locked by other active exams
    if (assignedQuestionCodes.length > 0) {
      try {
        const uniqueCandidateCodes = Array.from(new Set(assignedQuestionCodes));
        const [remainingObjSnap, remainingSubjSnap] = await Promise.all([
          adminDb.collection('exams').get(),
          adminDb.collection('subjectiveExams').get()
        ]);

        const otherActiveCodes = new Set<string>();
        remainingObjSnap.docs.forEach(doc => {
          if (doc.id === examId) return;
          const edata = doc.data();
          const codes = edata.questionCodes || edata.questionIds || [];
          codes.forEach((c: any) => { if (c) otherActiveCodes.add(String(c).trim()); });
          if (Array.isArray(edata.questions)) {
            edata.questions.forEach((q: any) => {
              if (q?.id) otherActiveCodes.add(String(q.id).trim());
              if (q?.questionCode) otherActiveCodes.add(String(q.questionCode).trim());
            });
          }
        });
        remainingSubjSnap.docs.forEach(doc => {
          if (doc.id === examId) return;
          const edata = doc.data();
          const codes = edata.questionCodes || edata.questionIds || [];
          codes.forEach((c: any) => { if (c) otherActiveCodes.add(String(c).trim()); });
          if (Array.isArray(edata.questions)) {
            edata.questions.forEach((q: any) => {
              if (q?.id) otherActiveCodes.add(String(q.id).trim());
              if (q?.questionCode) otherActiveCodes.add(String(q.questionCode).trim());
            });
          }
        });

        const codesToRelease = uniqueCandidateCodes.filter(c => !otherActiveCodes.has(c));
        if (codesToRelease.length > 0) {
          const releaseBatch = new ChunkedBatch(adminDb);
          for (const code of codesToRelease) {
            const qRef = adminDb.collection('questions').doc(code);
            releaseBatch.set(qRef, { usedInClassroomTest: false }, { merge: true });
          }

          for (let i = 0; i < codesToRelease.length; i += 30) {
            const chunk = codesToRelease.slice(i, i + 30);
            try {
              const matchedSnap = await adminDb.collection('questions')
                .where('questionCode', 'in', chunk)
                .get();
              matchedSnap.docs.forEach(qDoc => {
                releaseBatch.set(qDoc.ref, { usedInClassroomTest: false }, { merge: true });
              });
            } catch (mErr) {
              console.warn('Matched question release lookup warning:', mErr);
            }
          }

          await releaseBatch.commit();
        }
      } catch (relErr) {
        console.warn('Failed to release questions during exam delete:', relErr);
      }
    }

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

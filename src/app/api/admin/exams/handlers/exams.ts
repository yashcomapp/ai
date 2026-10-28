import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { notifyNewExam } from '@/lib/notifications';
import { getDateKeyIST } from '@/lib/dateUtils';
import { ReportCacheManager } from '@/lib/reportCache';
import { getRequiredConfidence, isDemoUser } from '@/lib/studentDb';
import { evaluateSessionSincerity } from '@/lib/practiceTimeUtils';
import { getCanonicalSubjectName, parseTopicCode } from '@/lib/questionTypes';
import { getObjectiveExamTopics, getSubjectiveExamTopics, getExamDateKey, isExamForStudent, QuotientService } from '@/services/quotient.service';
import { ExamService, getAssignmentsForBatches } from '@/services/exam.service';
import { getCachedBatches } from '@/lib/firebase/cache';

const parseIST = (dateStr: string): Date => {
  if (!dateStr) return new Date();
  let trimmed = String(dateStr).trim();

  // Handle slash formats e.g. 10/16/2026 or 16/10/2026
  const slashMatch = trimmed.match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})$/);
  if (slashMatch) {
    const n1 = parseInt(slashMatch[1], 10);
    const n2 = parseInt(slashMatch[2], 10);
    const year = slashMatch[3];
    let month = n1;
    let day = n2;
    if (n1 > 12 && n2 <= 12) {
      day = n1;
      month = n2;
    } else if (n2 > 12 && n1 <= 12) {
      month = n1;
      day = n2;
    }
    trimmed = `${year}-${String(month).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
  }

  const hasOffset = /[+-]\d{2}:?\d{2}$/.test(trimmed) || trimmed.endsWith('Z');
  if (!hasOffset) {
    const timePart = trimmed.includes('T') ? '' : 'T00:00:00';
    const d = new Date(`${trimmed}${timePart}+05:30`);
    if (!isNaN(d.getTime())) return d;
  }
  const d = new Date(trimmed);
  return isNaN(d.getTime()) ? new Date() : d;
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

const is6amOr9pmSlot = (d: Date) => {
  try {
    const hr = Number(d.toLocaleTimeString('en-US', { timeZone: 'Asia/Kolkata', hour: '2-digit', hour12: false }));
    return hr === 6 || hr === 21;
  } catch {
    return false;
  }
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
      // 1. Fetch student user document, mastery, and parent reviews
      const [studentUserSnap, masterySnap, parentReviewsSnap] = await Promise.all([
        adminDb.collection('users').where('studentCode', '==', studentCodeParam).where('role', '==', 'student').limit(1).get(),
        adminDb.collection('studentTopicMastery').where('studentCode', '==', studentCodeParam).get(),
        adminDb.collection('parentReviews').where('studentCode', '==', studentCodeParam).get()
      ]);

      const studentUser = studentUserSnap.docs[0]?.data();
      const bIds = studentUser?.batchIds || (studentUser?.batchId ? [studentUser.batchId] : []);
      const studentClass = studentUser?.class || studentUser?.className || '';
      const cleanClass = String(studentClass).replace(/\D/g, '');
      const todayDateStr = getDateKeyIST();

      // 2. Targeted batch assignment queries via unified getAssignmentsForBatches
      const baPromise = getAssignmentsForBatches(bIds, {
        type: 'objective',
        status: null,
        studentCode: studentCodeParam
      });

      // 3. Class-scoped active/draft exams
      const objExamsQuery = cleanClass
        ? adminDb.collection('exams').where('class', '==', cleanClass).where('status', 'in', ['active', 'draft']).get()
        : adminDb.collection('exams').where('status', 'in', ['active', 'draft']).limit(200).get();

      const subjExamsQuery = cleanClass
        ? adminDb.collection('subjectiveExams').where('class', '==', cleanClass).where('status', 'in', ['active', 'draft']).get()
        : adminDb.collection('subjectiveExams').where('status', 'in', ['active', 'draft']).limit(200).get();

      const [examsSnap, subjExamsSnap, baResult] = await Promise.all([
        objExamsQuery,
        subjExamsQuery,
        baPromise
      ]);

      const examsMap = new Map<string, any>();
      examsSnap.docs.forEach(doc => {
        examsMap.set(doc.id, { id: doc.id, ...doc.data() });
      });

      const subjExamsMap = new Map<string, any>();
      subjExamsSnap.docs.forEach(doc => {
        subjExamsMap.set(doc.id, { id: doc.id, ...doc.data() });
      });

      const assignedExamIds = new Set<string>();
      baResult.objectiveDocs.forEach(doc => {
        const bData = doc.data();
        if (bData.examId) {
          assignedExamIds.add(bData.examId);
          if (examsMap.has(bData.examId)) {
            const ex = examsMap.get(bData.examId);
            const tBatches = new Set([...(ex.targetBatches || []), ...(bData.targetBatches || [])]);
            const tStudents = new Set([...(ex.targetStudents || []), ...(bData.targetStudents || [])]);
            ex.targetBatches = Array.from(tBatches);
            ex.targetStudents = Array.from(tStudents);
          }
        }
      });

      // Hydrate any missing assigned objective/subjective exams not in class query
      const missingObjIds = Array.from(assignedExamIds).filter(id => !examsMap.has(id));
      if (missingObjIds.length > 0) {
        const refs = missingObjIds.map(id => adminDb.collection('exams').doc(id));
        const missingDocs = await adminDb.getAll(...refs);
        missingDocs.forEach(doc => {
          if (doc.exists) {
            examsMap.set(doc.id, { id: doc.id, ...doc.data() });
          }
        });
      }

      const missingSubjIds = Array.from(assignedExamIds).filter(id => !subjExamsMap.has(id) && !examsMap.has(id));
      if (missingSubjIds.length > 0) {
        const refs = missingSubjIds.map(id => adminDb.collection('subjectiveExams').doc(id));
        const missingDocs = await adminDb.getAll(...refs);
        missingDocs.forEach(doc => {
          if (doc.exists) {
            subjExamsMap.set(doc.id, { id: doc.id, ...doc.data() });
          }
        });
      }

      const conductedTopicsSet = new Set<string>();

      examsMap.forEach(exam => {
        const examDateStr = getExamDateKey(exam) || todayDateStr;
        if (examDateStr <= todayDateStr && isExamForStudent(exam, studentCodeParam, bIds, studentClass)) {
          getObjectiveExamTopics(exam).forEach(t => conductedTopicsSet.add(t));
        }
      });

      subjExamsMap.forEach(exam => {
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
        } else if (mastery >= 90 && isFullConfidence) {
          state = 'mastered';
          expIcon = '⭐';
          expColor = 'var(--success)';
          expText = `Mastered (${mastery}% accuracy across ${attempts} verified questions).`;
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
            expIcon = '🔒';
            expColor = 'var(--text-muted)';
            expText = `${maxPractices}/${maxPractices} practices done (${mastery}% accuracy). Practice quota reached. Revise textbook concepts before exams.`;
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
            expIcon = '🔒';
            expColor = 'var(--text-muted)';
            expText = `${maxPractices}/${maxPractices} practices done (${mastery}% accuracy). Practice quota reached. Revise textbook concepts before exams.`;
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

    if (action === 'practiceTracks') {
      const batchIdParam = req.nextUrl.searchParams.get('batchId');
      const daysParam = req.nextUrl.searchParams.get('days');
      const startDateParam = req.nextUrl.searchParams.get('startDate');
      const endDateParam = req.nextUrl.searchParams.get('endDate');

      const cacheKey = `practice-tracks-v4-${batchIdParam || 'all'}-${daysParam || '7'}-${startDateParam || ''}-${endDateParam || ''}`;
      const cached = await ReportCacheManager.getReport<any>(cacheKey);
      if (cached) {
        return NextResponse.json(cached);
      }

      let studentsPromise: Promise<any>;
      if (batchIdParam) {
        studentsPromise = Promise.all([
          adminDb.collection('users').where('role', '==', 'student').where('batchId', '==', batchIdParam).select('studentCode', 'name', 'email', 'isDemo', 'rollNumber', 'batchIds', 'batchId', 'class', 'className', 'status').get(),
          adminDb.collection('users').where('role', '==', 'student').where('batchIds', 'array-contains', batchIdParam).select('studentCode', 'name', 'email', 'isDemo', 'rollNumber', 'batchIds', 'batchId', 'class', 'className', 'status').get()
        ]).then(([s1, s2]) => {
          const docMap = new Map<string, any>();
          s1.docs.forEach(d => docMap.set(d.id, d));
          s2.docs.forEach(d => docMap.set(d.id, d));
          return { docs: Array.from(docMap.values()) };
        });
      } else {
        studentsPromise = adminDb.collection('users').where('role', '==', 'student').select('studentCode', 'name', 'email', 'isDemo', 'rollNumber', 'batchIds', 'batchId', 'class', 'className', 'status').get();
      }

      const studentsList = await studentsPromise;

      const students = studentsList.docs.map((doc: any) => {
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
      }).filter((s: any) => !!s.studentCode && s.status !== 'inactive' && !isDemoUser(s));

      const studentCodes = students.map((s: any) => s.studentCode);
      if (studentCodes.length === 0) {
        return NextResponse.json({ practiceStats: {}, masteryStats: {}, weeklyStats: {}, weekDays: [] });
      }

      // Calculate unified metrics via Single Source of Truth (QuotientService & calculateUnifiedMetrics)
      const quotientsMap = await QuotientService.calculateBulkQuotients(studentCodes, 'all');

      // Generate dynamic sliding window / date keys in IST
      const now = new Date();
      const todayKey = getDateKeyIST(now);
      const dayKeys: string[] = [];
      const weekDays: Array<{ dateKey: string; label: string; shortLabel: string; dayName: string; isToday: boolean }> = [];

      if (startDateParam && endDateParam) {
        // Custom date range: parse start and end, clamp up to 60 days
        const startD = parseIST(startDateParam);
        const endD = parseIST(endDateParam);
        const actualStart = startD.getTime() <= endD.getTime() ? startD : endD;
        const actualEnd = startD.getTime() <= endD.getTime() ? endD : startD;

        const current = new Date(actualStart);
        const endKey = getDateKeyIST(actualEnd);
        let count = 0;

        while (count < 60) {
          const dateKey = getDateKeyIST(current);
          const dayName = current.toLocaleDateString('en-US', { timeZone: 'Asia/Kolkata', weekday: 'short' });
          const dayMonth = current.toLocaleDateString('en-GB', { timeZone: 'Asia/Kolkata', day: '2-digit', month: '2-digit' });

          dayKeys.push(dateKey);
          weekDays.push({
            dateKey,
            label: `${dayName} ${dayMonth}`,
            shortLabel: dayName,
            dayName,
            isToday: dateKey === todayKey
          });

          if (dateKey === endKey) break;
          current.setDate(current.getDate() + 1);
          count++;
        }
      } else {
        // Preset days window (default 7 days, clamped between 1 and 60)
        const numDays = Math.min(60, Math.max(1, parseInt(daysParam || '7', 10) || 7));
        for (let i = numDays - 1; i >= 0; i--) {
          const d = new Date(now.getTime() - i * 86400000);
          const dateKey = getDateKeyIST(d);
          const dayName = d.toLocaleDateString('en-US', { timeZone: 'Asia/Kolkata', weekday: 'short' });
          const dayMonth = d.toLocaleDateString('en-GB', { timeZone: 'Asia/Kolkata', day: '2-digit', month: '2-digit' });
          dayKeys.push(dateKey);
          weekDays.push({
            dateKey,
            label: `${dayName} ${dayMonth}`,
            shortLabel: dayName,
            dayName,
            isToday: dateKey === todayKey
          });
        }
      }

      // Fetch practice reviews for daily history, time tracking, and lastActive
      const chunks: string[][] = [];
      for (let i = 0; i < studentCodes.length; i += 30) {
        chunks.push(studentCodes.slice(i, i + 30));
      }
      const reviewsSnaps = await Promise.all(
        chunks.map(chunk =>
          adminDb.collection('parentReviews')
            .where('studentCode', 'in', chunk)
            .select('studentCode', 'startedAt', 'createdAt', 'submittedAt', 'totalQuestions', 'questionsCount', 'correctCount', 'scorePercent', 'type', 'durationSpent')
            .get()
            .catch(() => null)
        )
      );

      const lastActiveMap: Record<string, string | null> = {};
      const cumulativeDurationMap: Record<string, number> = {};
      const weeklyStats: Record<string, {
        days: Record<string, { questionsCount: number; sessionsCount: number; avgScore: number; correctCount: number; durationSeconds: number }>;
        totalQuestions: number;
        totalSessions: number;
        activeDays: number;
        avgScore: number;
        activeDates: string[];
        totalDurationSeconds: number;
      }> = {};

      students.forEach((s: any) => {
        const dayMap: Record<string, { questionsCount: number; sessionsCount: number; avgScore: number; correctCount: number; durationSeconds: number }> = {};
        dayKeys.forEach(dk => {
          dayMap[dk] = { questionsCount: 0, sessionsCount: 0, avgScore: 0, correctCount: 0, durationSeconds: 0 };
        });
        weeklyStats[s.studentCode] = {
          days: dayMap,
          totalQuestions: 0,
          totalSessions: 0,
          activeDays: 0,
          avgScore: 0,
          activeDates: [],
          totalDurationSeconds: 0
        };
      });

      reviewsSnaps.filter(Boolean).flatMap(s => s!.docs).forEach(doc => {
        const data = doc.data();
        const code = data.studentCode;
        if (!code || !weeklyStats[code]) return;
        if (data.type && data.type !== 'practice') return;

        const duration = Math.max(0, Number(data.durationSpent) || 0);
        cumulativeDurationMap[code] = (cumulativeDurationMap[code] || 0) + duration;

        const itemDate = data.startedAt?.toDate ? data.startedAt.toDate() : data.createdAt?.toDate ? data.createdAt.toDate() : data.submittedAt?.toDate ? data.submittedAt.toDate() : data.startedAt ? new Date(data.startedAt) : null;
        if (!itemDate) return;

        if (!lastActiveMap[code] || itemDate > new Date(lastActiveMap[code]!)) {
          lastActiveMap[code] = itemDate.toISOString();
        }

        const dateKey = getDateKeyIST(itemDate);
        if (weeklyStats[code].days[dateKey]) {
          const dayData = weeklyStats[code].days[dateKey];
          const qCount = Number(data.totalQuestions || data.questionsCount || 6);
          const score = Number(data.scorePercent ?? (data.totalQuestions ? Math.round(((data.correctCount || 0) / data.totalQuestions) * 100) : 0));
          const correct = Number(data.correctCount ?? Math.round((qCount * score) / 100));

          dayData.sessionsCount += 1;
          dayData.questionsCount += qCount;
          dayData.correctCount += correct;
          dayData.durationSeconds += duration;
        }
      });

      // Finalize weekly aggregates per student
      Object.values(weeklyStats).forEach(w => {
        let weekQ = 0;
        let weekCorrect = 0;
        let weekSess = 0;
        let activeD = 0;
        let totalDuration = 0;
        const activeDatesArr: string[] = [];

        dayKeys.forEach(dk => {
          const d = w.days[dk];
          if (d.sessionsCount > 0) {
            d.avgScore = d.questionsCount > 0 ? Math.round((d.correctCount / d.questionsCount) * 100) : 0;
            weekQ += d.questionsCount;
            weekCorrect += d.correctCount;
            weekSess += d.sessionsCount;
            totalDuration += (d.durationSeconds || 0);
            activeD += 1;
            activeDatesArr.push(dk);
          }
        });

        w.totalQuestions = weekQ;
        w.totalSessions = weekSess;
        w.activeDays = activeD;
        w.totalDurationSeconds = totalDuration;
        w.avgScore = weekQ > 0 ? Math.round((weekCorrect / weekQ) * 100) : 0;
        w.activeDates = activeDatesArr;
      });

      const practiceStats: Record<string, { totalSessions: number, questionsAttempted: number, avgScore: number, examAvg: number, lastActive: string | null, totalDurationSeconds: number }> = {};
      const masteryStats: Record<string, { avgMastery: number, avgQuality: number, efforts: number, mastered: number, practicing: number, needsAttention: number, totalAssigned: number }> = {};

      students.forEach((s: any) => {
        const code = s.studentCode;
        const qData = quotientsMap[code];
        if (!qData) {
          practiceStats[code] = { totalSessions: 0, questionsAttempted: 0, avgScore: 0, examAvg: 0, lastActive: null, totalDurationSeconds: 0 };
          masteryStats[code] = { avgMastery: 0, avgQuality: 100, efforts: 0, mastered: 0, practicing: 0, needsAttention: 0, totalAssigned: 0 };
          return;
        }

        const examComp = qData.components.find(c => c.parameterId === 'exam');
        const practiceComp = qData.components.find(c => c.parameterId === 'practice');
        const qualityComp = qData.components.find(c => c.parameterId === 'quality');
        const healthComp = qData.components.find(c => c.parameterId === 'topicHealth');

        const totalAssigned = healthComp?.details?.totalTopics ?? practiceComp?.details?.totalAssignedTopics ?? 0;
        const mastered = healthComp?.details?.masteredCount ?? 0;
        const needsAttention = healthComp?.details?.attentionCount ?? 0;
        const practicing = healthComp?.details?.practicingCount ?? Math.max(0, totalAssigned - mastered - needsAttention);

        practiceStats[code] = {
          totalSessions: practiceComp?.details?.practicesCompletedCount ?? 0,
          questionsAttempted: practiceComp?.details?.totalQuestionsAttempted ?? 0,
          avgScore: practiceComp?.details?.averagePracticeScore ?? 0,
          examAvg: examComp?.score ?? 0,
          lastActive: lastActiveMap[code] || null,
          totalDurationSeconds: cumulativeDurationMap[code] || 0
        };

        masteryStats[code] = {
          avgMastery: healthComp?.score ?? 0,
          avgQuality: qualityComp?.score ?? 100,
          efforts: practiceComp?.score ?? 0,
          mastered,
          practicing,
          needsAttention,
          totalAssigned
        };
      });

      const responsePayload = {
        practiceStats,
        masteryStats,
        weeklyStats,
        weekDays,
        periodInfo: {
          daysCount: dayKeys.length,
          startDate: dayKeys[0] || '',
          endDate: dayKeys[dayKeys.length - 1] || '',
          startLabel: weekDays[0]?.label || '',
          endLabel: weekDays[weekDays.length - 1]?.label || ''
        }
      };
      await ReportCacheManager.setReport(cacheKey, responsePayload, 180);

      return NextResponse.json(responsePayload);
    }

    const since = new Date();
    since.setDate(since.getDate() - 90);

    const includeParents = req.nextUrl.searchParams.get('includeParents') === 'true';

    const [
      examsList,
      subjExamsList,
      batchesList,
      studentsList,
      parentsSnap
    ] = await Promise.all([
      adminDb.collection('exams').where('status', 'in', ['active', 'draft']).get(),
      adminDb.collection('subjectiveExams').where('status', 'in', ['active', 'draft']).get(),
      getCachedBatches(),
      adminDb.collection('users').where('role', '==', 'student').select('studentCode', 'name', 'email', 'isDemo', 'rollNumber', 'batchIds', 'batchId', 'class', 'className', 'status').get(),
      includeParents 
        ? adminDb.collection('users').where('role', '==', 'parent').select('email', 'studentCode', 'studentCodes', 'name').get()
        : Promise.resolve({ docs: [] } as any)
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

    const parents = includeParents ? parentsSnap.docs.map((doc: any) => {
      const data = doc.data();
      if (isDemoUser(data)) return null;
      const pEmail = data.email || '';
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
    }).filter((p: any): p is { email: string; displayName: string; studentCodes: string[] } => p !== null && !!p.email)
    .sort((a: any, b: any) => a.displayName.localeCompare(b.displayName)) : [];

    // Target assignments and attempt counts strictly by active/draft exam IDs
    const objExamIds = exams.map(e => e.id).filter(Boolean);
    const subjExamIds = subjectiveExams.map(e => e.id).filter(Boolean);
    const allExamIds = Array.from(new Set([...objExamIds, ...subjExamIds]));

    const allChunks: string[][] = [];
    for (let i = 0; i < allExamIds.length; i += 30) {
      allChunks.push(allExamIds.slice(i, i + 30));
    }

    const [objAssignSnaps, subjAssignSnaps, reviewSnaps, attemptSnaps] = await Promise.all([
      allChunks.length > 0 ? Promise.all(allChunks.map(chunk =>
        adminDb.collection('batchAssignments')
          .where('examId', 'in', chunk)
          .get()
          .catch(err => {
            console.error('Error fetching batchAssignments chunk:', err);
            return { docs: [] } as any;
          })
      )) : Promise.resolve([]),
      allChunks.length > 0 ? Promise.all(allChunks.map(chunk =>
        adminDb.collection('subjectiveAssignments')
          .where('examId', 'in', chunk)
          .get()
          .catch(err => {
            console.error('Error fetching subjectiveAssignments chunk:', err);
            return { docs: [] } as any;
          })
      )) : Promise.resolve([]),
      Promise.all(allChunks.map(chunk => 
        adminDb.collection('reviews')
          .where('examId', 'in', chunk)
          .select('examId', 'startedAt', 'status')
          .get()
          .catch(() => null)
      )),
      Promise.all(allChunks.map(chunk => 
        adminDb.collection('examAttempts')
          .where('examId', 'in', chunk)
          .select('examId', 'startedAt', 'status')
          .get()
          .catch(() => null)
      ))
    ]);

    const objAssignDocs = (objAssignSnaps as any[]).flatMap(s => s?.docs || []);
    const subjAssignDocs = (subjAssignSnaps as any[]).flatMap(s => s?.docs || []);

    const attemptCounts: { [key: string]: number } = {};
    const examAttemptsMap: { [key: string]: Set<string> } = {};

    [...reviewSnaps, ...attemptSnaps].forEach(snap => {
      if (!snap) return;
      snap.docs.forEach((doc: any) => {
        const d = doc.data();
        if (d.status === 'precheck') return;
        const eid = d.examId;
        const startedAt = d.startedAt;
        if (startedAt) {
          const startDate = startedAt.toDate ? startedAt.toDate() : new Date(startedAt);
          if (startDate < since) return;
        }
        const studentCode = doc.id.includes('_') ? doc.id.split('_').slice(1).join('_') : doc.id;
        if (eid && studentCode) {
          if (!examAttemptsMap[eid]) examAttemptsMap[eid] = new Set();
          examAttemptsMap[eid].add(studentCode);
        }
      });
    });

    for (const eid in examAttemptsMap) {
      attemptCounts[eid] = examAttemptsMap[eid].size;
    }

    const objAssignments: any[] = [];
    objAssignDocs.forEach((doc: any) => {
      const data = doc.data();
      if (data.status && data.status !== 'active' && data.status !== 'draft') return;
      objAssignments.push({
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
      });
    });

    const subjAssignments: any[] = [];
    subjAssignDocs.forEach((doc: any) => {
      const data = doc.data();
      if (data.status && data.status !== 'active' && data.status !== 'draft') return;
      subjAssignments.push({
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
      });
    });

    return NextResponse.json({
      exams,
      subjectiveExams,
      batches,
      students,
      parents,
      assignments: [...objAssignments, ...subjAssignments],
      attemptCounts
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
      lateEntryRestriction,
      action
    } = body;

    if (action === 'resetAttempts') {
      if (!examId) {
        return NextResponse.json({ message: 'Missing examId parameter.' }, { status: 400 });
      }
      const resetResult = await ExamService.resetExamAttemptsAndRecordsForReassignment({
        examId,
        type: type || 'objective',
        targetType: targetType || 'batch',
        targetStudents: targetStudents || []
      });
      return NextResponse.json({ success: true, message: 'All attempts and records reset successfully.', details: resetResult });
    }

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
      lateEntryRestriction: lateEntryRestriction === true || (lateEntryRestriction !== false && is6amOr9pmSlot(startAt)),
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

      // Reassigned exam or target students: wipe previous attempts & recalculate mastery
      if (!existingSnap.empty || body.resetAttempts || targetType === 'student' || body.action === 'reassign') {
        try {
          await ExamService.resetExamAttemptsAndRecordsForReassignment({
            examId,
            type: 'objective',
            targetType: targetType || 'batch',
            targetStudents: targetStudents || []
          });
        } catch (resetErr) {
          console.warn('Objective reassignment reset warning:', resetErr);
        }
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

      // Reassigned exam or target students: wipe previous attempts & recalculate mastery
      if (!existingSnap.empty || body.resetAttempts || targetType === 'student' || body.action === 'reassign') {
        try {
          await ExamService.resetExamAttemptsAndRecordsForReassignment({
            examId,
            type: 'subjective',
            targetType: targetType || 'batch',
            targetStudents: targetStudents || []
          });
        } catch (resetErr) {
          console.warn('Subjective reassignment reset warning:', resetErr);
        }
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
      targetStudents,
      resetAttempts
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
      lateEntryRestriction: lateEntryRestriction === true || (lateEntryRestriction !== false && is6amOr9pmSlot(updatedStart)),
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

    const isRescheduled = assignData.startAt && Math.abs(updatedStart.getTime() - (assignData.startAt.toDate ? assignData.startAt.toDate().getTime() : new Date(assignData.startAt).getTime())) > 600000;
    if ((resetAttempts || isRescheduled) && assignData.examId) {
      try {
        const examType = collection === 'batchAssignments' ? 'objective' : 'subjective';
        await ExamService.resetExamAttemptsAndRecordsForReassignment({
          examId: assignData.examId,
          type: examType,
          targetType: targetType || assignData.targetType || 'batch',
          targetStudents: targetStudents || assignData.targetStudents || []
        });
      } catch (resetErr) {
        console.warn('Assignment reschedule reset error (non-fatal):', resetErr);
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

    if (!examId) {
      return NextResponse.json({ message: 'Missing parameter (examId).' }, { status: 400 });
    }

    const result = await ExamService.deleteExamCompletely(examId, type);
    return NextResponse.json(result);

  } catch (error: any) {
    console.error('API delete exam error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}


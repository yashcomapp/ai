import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { isTopicPurelyQualitative } from '@/lib/curriculumGuard';
import { deriveTopicCodeFromQuestionCode, normalizeTopicCode } from '@/lib/questionTypes';
import { classifyAssignedTopics } from '@/lib/dashboardMetrics';
import { getFromCache, setInCache, getCachedSyllabus } from '@/lib/firebase/cache';

export const dynamic = 'force-dynamic';
export const maxDuration = 60;

/**
 * GET /api/admin/exams/topic-coverage?batchId=<batchId>
 * 
 * Aggregates conducted topics for a given batch from assigned exams.
 * Strictly returns CONDUCTED topics only.
 * 
 * Performance & Cost Invariants:
 * 1. Zero full-collection scans (strictly queries users belonging to batchId with .select()).
 * 2. Parallel getAll() batch reads for exams and mastery records.
 * 3. In-memory cached syllabus index via getCachedSyllabus().
 * 4. SSOT classification via classifyAssignedTopics (guaranteeing exact dashboard parity).
 * 5. 3-minute in-memory caching to eliminate redundant round-trips on batch navigation.
 */
export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const batchId = searchParams.get('batchId') || '';

    if (!batchId) {
      return NextResponse.json({ message: 'Missing batchId parameter.' }, { status: 400 });
    }

    // 0. Cache Check (3-minute TTL for instant response and zero redundant reads)
    const cacheKey = `topic-coverage_${batchId}`;
    const cachedResponse = getFromCache<any>(cacheKey);
    if (cachedResponse) {
      return NextResponse.json(cachedResponse);
    }

    // 1. Get batch details
    const batchDoc = await adminDb.collection('batches').doc(batchId).get();
    if (!batchDoc.exists) {
      return NextResponse.json({ message: 'Batch not found.' }, { status: 404 });
    }
    const batchData = batchDoc.data()!;
    const batchClass = String(batchData.class || batchData.className || '').trim();

    // 2. Fetch students belonging strictly to this batch (Targeted query with .select())
    const studentsSnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .where('batchIds', 'array-contains', batchId)
      .select('studentCode', 'name', 'status', 'batchIds', 'batchId')
      .get();

    let batchStudents = studentsSnap.docs.map(d => ({ id: d.id, ...d.data() }));

    // Fallback for legacy student documents with singular batchId
    if (batchStudents.length === 0) {
      const legacySnap = await adminDb.collection('users')
        .where('role', '==', 'student')
        .where('batchId', '==', batchId)
        .select('studentCode', 'name', 'status', 'batchIds', 'batchId')
        .get();
      batchStudents = legacySnap.docs.map(d => ({ id: d.id, ...d.data() }));
    }

    // Exclude inactive students per Rule 2C
    batchStudents = batchStudents.filter((s: any) => s.status !== 'inactive' && s.studentCode);
    const studentCodes = batchStudents.map((s: any) => String(s.studentCode).trim());

    // 3. Find all conducted/assigned exams for this batch
    const [assignmentsSnap, subjAssignmentsSnap, batchExamsSnap, batchSubjExamsSnap] = await Promise.all([
      adminDb.collection('batchAssignments').where('targetBatches', 'array-contains', batchId).select('examId').get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('subjectiveAssignments').where('targetBatches', 'array-contains', batchId).select('examId').get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('exams').where('batchId', '==', batchId).select('name', 'title', 'scheduledDate', 'createdAt', 'topicCodes', 'topicCode', 'questionCodes').get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('subjectiveExams').where('batchId', '==', batchId).select('name', 'title', 'scheduledDate', 'createdAt', 'topicCodes', 'topicCode', 'questionCodes').get().catch(() => ({ docs: [] } as any))
    ]);

    const examDataMap = new Map<string, { examId: string; name: string; date: string; type: string; topicCodes: string[] }>();

    // Process exams already directly attached to batch
    batchExamsSnap.docs.forEach((d: any) => {
      const data = d.data();
      const extractedTopics = extractTopicsFromExam(data);
      examDataMap.set(d.id, {
        examId: d.id,
        name: data.name || data.title || d.id,
        date: formatDateFromField(data.scheduledDate || data.createdAt),
        type: 'objective',
        topicCodes: extractedTopics
      });
    });

    batchSubjExamsSnap.docs.forEach((d: any) => {
      const data = d.data();
      const extractedTopics = extractTopicsFromExam(data);
      examDataMap.set(d.id, {
        examId: d.id,
        name: data.name || data.title || d.id,
        date: formatDateFromField(data.scheduledDate || data.createdAt),
        type: 'subjective',
        topicCodes: extractedTopics
      });
    });

    // Collect additional assigned exam IDs that need fetching
    const assignedObjExamIds = new Set<string>();
    const assignedSubjExamIds = new Set<string>();

    assignmentsSnap.docs.forEach((d: any) => {
      const eid = d.data()?.examId;
      if (eid && !examDataMap.has(eid)) assignedObjExamIds.add(eid);
    });

    subjAssignmentsSnap.docs.forEach((d: any) => {
      const eid = d.data()?.examId;
      if (eid && !examDataMap.has(eid)) assignedSubjExamIds.add(eid);
    });

    // Fetch assigned exams in efficient parallel chunks using getAll()
    const objIdsToFetch = Array.from(assignedObjExamIds).slice(0, 100);
    const subjIdsToFetch = Array.from(assignedSubjExamIds).slice(0, 50);

    const [objSnaps, subjSnaps] = await Promise.all([
      objIdsToFetch.length > 0
        ? adminDb.getAll(...objIdsToFetch.map(id => adminDb.collection('exams').doc(id)))
        : Promise.resolve([]),
      subjIdsToFetch.length > 0
        ? adminDb.getAll(...subjIdsToFetch.map(id => adminDb.collection('subjectiveExams').doc(id)))
        : Promise.resolve([])
    ]);

    objSnaps.forEach(snap => {
      if (snap.exists) {
        const data = snap.data()!;
        const extracted = extractTopicsFromExam(data);
        examDataMap.set(snap.id, {
          examId: snap.id,
          name: data.name || data.title || snap.id,
          date: formatDateFromField(data.scheduledDate || data.createdAt),
          type: 'objective',
          topicCodes: extracted
        });
      }
    });

    subjSnaps.forEach(snap => {
      if (snap.exists) {
        const data = snap.data()!;
        const extracted = extractTopicsFromExam(data);
        examDataMap.set(snap.id, {
          examId: snap.id,
          name: data.name || data.title || snap.id,
          date: formatDateFromField(data.scheduledDate || data.createdAt),
          type: 'subjective',
          topicCodes: extracted
        });
      }
    });

    // 4. Map conducted exams to canonical topic codes
    const topicExamsMap: { [canonicalTopicCode: string]: Array<{ examId: string; name: string; date: string; type: string }> } = {};

    examDataMap.forEach(exam => {
      exam.topicCodes.forEach(rawTc => {
        const tc = normalizeTopicCode(rawTc);
        if (!tc) return;
        if (!topicExamsMap[tc]) topicExamsMap[tc] = [];
        topicExamsMap[tc].push({
          examId: exam.examId,
          name: exam.name,
          date: exam.date,
          type: exam.type
        });
      });
    });

    const conductedTopicCodes = Object.keys(topicExamsMap);

    // 5. In-Memory Syllabus Metadata via getCachedSyllabus() (Zero extra Firestore reads)
    const syllabusSnap = await getCachedSyllabus();
    const syllabusTopicsMap = new Map<string, any>();

    syllabusSnap.docs.forEach(d => {
      const data = d.data();
      const subjName = data.name || data.subject || '';
      const cls = data.class || '';
      (data.chapters || []).forEach((ch: any) => {
        const chName = ch.name || ch.title || '';
        (ch.topics || []).forEach((top: any) => {
          if (top.code) {
            const norm = normalizeTopicCode(top.code);
            syllabusTopicsMap.set(norm, {
              topicCode: norm,
              topicName: top.name || top.title || norm,
              chapterName: chName,
              subjectName: subjName,
              className: cls,
              topicClassification: top.topicClassification || top.classification || 'medium',
              targetQuestions: Number(top.targetQuestions) || 30,
              requiredConfidence: Number(top.requiredConfidence) || 18,
              hasNumericals: !isTopicPurelyQualitative(norm, chName, subjName)
            });
          }
        });
      });
    });

    // 6. Fetch Student Topic Mastery in efficient parallel batch chunks
    // For 15-25 batch students, this takes only 2-3 queries instead of hundreds of individual reads
    const studentMasteryMap = new Map<string, any[]>();
    studentCodes.forEach(sc => studentMasteryMap.set(sc, []));

    if (studentCodes.length > 0) {
      const studentChunks: string[][] = [];
      for (let i = 0; i < studentCodes.length; i += 10) {
        studentChunks.push(studentCodes.slice(i, i + 10));
      }

      const masterySnaps = await Promise.all(
        studentChunks.map(chunk =>
          adminDb.collection('studentTopicMastery')
            .where('studentCode', 'in', chunk)
            .select('studentCode', 'topicCode', 'mastery', 'verifiedConfidence', 'confidence', 'requiredConfidence', 'practiceQuestionsAttempted')
            .get()
            .catch(() => ({ docs: [] } as any))
        )
      );

      masterySnaps.forEach(snap => {
        snap.docs.forEach((doc: any) => {
          const d = doc.data();
          const sCode = d.studentCode;
          if (sCode && studentMasteryMap.has(sCode)) {
            studentMasteryMap.get(sCode)!.push(d);
          }
        });
      });
    }

    // 7. SSOT Classification via classifyAssignedTopics for each student
    // Ensures 100% parity with Learning OS, Student Dashboard, Parent Portal, and Admin Reports
    const studentClassifiedResults = new Map<string, Map<string, any>>();

    batchStudents.forEach((st: any) => {
      const sCode = st.studentCode;
      const masteries = studentMasteryMap.get(sCode) || [];

      const result = classifyAssignedTopics({
        assignedTopicCodes: conductedTopicCodes,
        topicMasteries: masteries,
        syllabusTopicsMap
      });

      const topicItemMap = new Map<string, any>();
      result.topics.forEach(item => {
        topicItemMap.set(item.topicCode, item);
      });
      studentClassifiedResults.set(sCode, topicItemMap);
    });

    // 8. Aggregate Conducted Topics Statistics
    const topicsData: Array<{
      topicCode: string;
      topicName: string;
      chapterName: string;
      subject: string;
      className: string;
      hasNumericals: boolean;
      examsConductedCount: number;
      exams: Array<{ examId: string; name: string; date: string; type: string }>;
      batchAvgScore: number;
      totalStudents: number;
      studentsMastered: number;
      studentsPracticing: number;
      studentsNeedsAttention: number;
      students: Array<{
        studentCode: string;
        name: string;
        mastery: number;
        status: 'mastered' | 'practicing' | 'needsAttention' | 'unattempted';
        confidence: number;
        requiredConfidence: number;
      }>;
    }> = [];

    for (const tc of conductedTopicCodes) {
      const sMeta = syllabusTopicsMap.get(tc);
      const tName = sMeta?.topicName || tc;
      const chName = sMeta?.chapterName || '';
      const subjName = sMeta?.subjectName || '';
      const clsName = sMeta?.className || batchClass;
      const hasNumericals = sMeta?.hasNumericals ?? !isTopicPurelyQualitative(tc, chName, subjName);

      let scoreSum = 0;
      let evaluatedCount = 0;
      let masteredCount = 0;
      let practicingCount = 0;
      let needsAttentionCount = 0;

      const studentRoster: any[] = [];

      for (const st of batchStudents) {
        const sCode = (st as any).studentCode;
        const studentMap = studentClassifiedResults.get(sCode);
        const item = studentMap?.get(tc);

        let mastery = 0;
        let confidence = 0;
        let reqConf = sMeta?.requiredConfidence || 18;
        let status: 'mastered' | 'practicing' | 'needsAttention' | 'unattempted' = 'unattempted';

        if (item) {
          mastery = Number(item.mastery) || 0;
          confidence = Number(item.confidence) || 0;
          reqConf = Number(item.requiredConfidence) || reqConf;

          if (item.isUnattempted) {
            status = 'unattempted';
            needsAttentionCount++;
          } else if (item.state === 'mastered') {
            status = 'mastered';
            masteredCount++;
            scoreSum += mastery;
            evaluatedCount++;
          } else if (item.state === 'practicing') {
            status = 'practicing';
            practicingCount++;
            scoreSum += mastery;
            evaluatedCount++;
          } else {
            status = 'needsAttention';
            needsAttentionCount++;
            scoreSum += mastery;
            evaluatedCount++;
          }
        } else {
          status = 'unattempted';
          needsAttentionCount++;
        }

        studentRoster.push({
          studentCode: sCode,
          name: (st as any).name || sCode,
          mastery,
          status,
          confidence,
          requiredConfidence: reqConf
        });
      }

      const batchAvg = evaluatedCount > 0 ? Math.round(scoreSum / evaluatedCount) : 0;

      topicsData.push({
        topicCode: tc,
        topicName: tName,
        chapterName: chName,
        subject: subjName,
        className: clsName,
        hasNumericals,
        examsConductedCount: topicExamsMap[tc].length,
        exams: topicExamsMap[tc],
        batchAvgScore: batchAvg,
        totalStudents: batchStudents.length,
        studentsMastered: masteredCount,
        studentsPracticing: practicingCount,
        studentsNeedsAttention: needsAttentionCount,
        students: studentRoster.sort((a, b) => a.mastery - b.mastery)
      });
    }

    // Sort topics by canonical topicCode
    topicsData.sort((a, b) => a.topicCode.localeCompare(b.topicCode, undefined, { numeric: true }));

    const payload = {
      success: true,
      batchId,
      batchName: batchData.name || batchId,
      batchClass,
      totalStudents: batchStudents.length,
      conductedTopicsCount: topicsData.length,
      topics: topicsData
    };

    // Cache result in memory for 3 minutes (invalidated immediately when teacher assigns practice)
    setInCache(cacheKey, payload, 180000);

    return NextResponse.json(payload);

  } catch (err: any) {
    console.error('Error in GET /api/admin/exams/topic-coverage:', err);
    return NextResponse.json({ message: err.message || 'Internal server error.' }, { status: 500 });
  }
}

// ---------------------------------------------------------------------------
// Helper Functions
// ---------------------------------------------------------------------------

function extractTopicsFromExam(examData: any): string[] {
  if (!examData) return [];
  const found = new Set<string>();

  if (Array.isArray(examData.topicCodes)) {
    examData.topicCodes.forEach((tc: any) => {
      const code = normalizeTopicCode(String(tc || '').trim());
      if (code) found.add(code);
    });
  }

  if (examData.topicCode) {
    const code = normalizeTopicCode(String(examData.topicCode || '').trim());
    if (code) found.add(code);
  }

  if (Array.isArray(examData.questionCodes)) {
    examData.questionCodes.forEach((qc: any) => {
      const str = String(qc || '').trim();
      const derived = deriveTopicCodeFromQuestionCode(str);
      const code = normalizeTopicCode(derived);
      if (code) found.add(code);
    });
  }

  return Array.from(found);
}

function formatDateFromField(field: any): string {
  if (!field) return '';
  if (typeof field === 'string') return field;
  if (field.toDate && typeof field.toDate === 'function') {
    return field.toDate().toISOString();
  }
  return String(field);
}

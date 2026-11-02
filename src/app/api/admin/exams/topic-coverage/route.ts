import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { getDateKeyIST } from '@/lib/dateUtils';
import { isTopicPurelyQualitative } from '@/lib/curriculumGuard';

export const dynamic = 'force-dynamic';

/**
 * GET /api/admin/exams/topic-coverage?batchId=<batchId>
 * 
 * Aggregates conducted topics for a given batch from assigned exams,
 * calculating batch-level topic mastery, student distribution (Green/Yellow/Red),
 * and exam occurrences. Strictly returns CONDUCTED topics only.
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

    // 1. Get batch details and students in this batch
    const batchDoc = await adminDb.collection('batches').doc(batchId).get();
    if (!batchDoc.exists) {
      return NextResponse.json({ message: 'Batch not found.' }, { status: 404 });
    }
    const batchData = batchDoc.data()!;
    const batchClass = String(batchData.class || batchData.className || '').trim();

    // Fetch active students in this batch
    const studentsSnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .where('status', '!=', 'inactive')
      .get();

    const batchStudents = studentsSnap.docs
      .map(d => ({ id: d.id, ...d.data() }))
      .filter((s: any) => {
        const bIds = s.batchIds || [s.batchId].filter(Boolean);
        return bIds.includes(batchId) || (batchClass && (s.class === batchClass || s.className === batchClass));
      });

    const studentCodes = batchStudents.map((s: any) => s.studentCode).filter(Boolean);

    // 2. Find all exams assigned or conducted for this batch
    // We check both batchAssignments collection and direct exam properties
    const [assignmentsSnap, subjAssignmentsSnap, examsSnap, subjExamsSnap] = await Promise.all([
      adminDb.collection('batchAssignments').where('targetBatches', 'array-contains', batchId).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('subjectiveAssignments').where('targetBatches', 'array-contains', batchId).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('exams').where('batchId', '==', batchId).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('subjectiveExams').where('batchId', '==', batchId).get().catch(() => ({ docs: [] } as any))
    ]);

    const conductedExamIds = new Set<string>();
    assignmentsSnap.docs.forEach((d: any) => {
      const data = d.data();
      if (data.examId) conductedExamIds.add(data.examId);
    });
    subjAssignmentsSnap.docs.forEach((d: any) => {
      const data = d.data();
      if (data.examId) conductedExamIds.add(data.examId);
    });
    examsSnap.docs.forEach((d: any) => conductedExamIds.add(d.id));
    subjExamsSnap.docs.forEach((d: any) => conductedExamIds.add(d.id));

    // Also look up exams targeting the batch class if batch-specific assignments are sparse
    if (batchClass && conductedExamIds.size === 0) {
      const classExamsSnap = await adminDb.collection('exams').where('class', '==', batchClass).limit(50).get().catch(() => ({ docs: [] } as any));
      classExamsSnap.docs.forEach((d: any) => conductedExamIds.add(d.id));
    }

    // 3. For all conducted exams, extract unique topicCodes
    const topicExamsMap: { [topicCode: string]: Array<{ examId: string; name: string; date: string; type: string }> } = {};

    const examDocsToFetch = Array.from(conductedExamIds).slice(0, 150);
    for (const eid of examDocsToFetch) {
      let eSnap = await adminDb.collection('exams').doc(eid).get();
      let eType = 'objective';
      if (!eSnap.exists) {
        eSnap = await adminDb.collection('subjectiveExams').doc(eid).get();
        eType = 'subjective';
      }
      if (eSnap.exists) {
        const eData = eSnap.data()!;
        const examName = eData.name || eData.title || eid;
        const examDate = eData.scheduledDate || eData.createdAt ? (eData.createdAt.toDate ? eData.createdAt.toDate().toISOString() : String(eData.createdAt)) : '';
        
        let tCodes: string[] = [];
        if (Array.isArray(eData.topicCodes) && eData.topicCodes.length > 0) {
          tCodes = eData.topicCodes;
        } else if (eData.topicCode) {
          tCodes = [eData.topicCode];
        } else if (Array.isArray(eData.questionCodes) && eData.questionCodes.length > 0) {
          // Derive topicCode from questionCodes: MH-9-SCIT-1-1.1-OSC-001 -> MH-9-SCIT-1-1.1
          const extracted = new Set<string>();
          eData.questionCodes.forEach((qc: string) => {
            const parts = String(qc).split('-');
            if (parts.length >= 6) {
              extracted.add(parts.slice(0, 5).join('-'));
            }
          });
          tCodes = Array.from(extracted);
        }

        tCodes.forEach(tc => {
          if (!topicExamsMap[tc]) topicExamsMap[tc] = [];
          topicExamsMap[tc].push({
            examId: eid,
            name: examName,
            date: examDate,
            type: eType
          });
        });
      }
    }

    const conductedTopicCodes = Object.keys(topicExamsMap);

    // 4. Load topic metadata from syllabusTopicIndex or syllabus
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

    // Fetch student topic mastery for all batch students on these conducted topics
    for (const tc of conductedTopicCodes) {
      // Get topic metadata
      let tName = tc;
      let chName = '';
      let subjName = '';
      let clsName = batchClass;

      try {
        const sSnap = await adminDb.collection('syllabusTopicIndex').doc(tc).get();
        if (sSnap.exists) {
          const sd = sSnap.data()!;
          tName = sd.topicName || tName;
          chName = sd.chapterName || chName;
          subjName = sd.subjectName || sd.subject || subjName;
          clsName = sd.class || clsName;
        }
      } catch (err) {
        // silent fallback
      }

      // Check whether this topic can have numerical questions
      const hasNumericals = !isTopicPurelyQualitative(tc, chName, subjName);

      // Student performance stats
      let scoreSum = 0;
      let evaluatedCount = 0;
      let masteredCount = 0;
      let practicingCount = 0;
      let needsAttentionCount = 0;

      const studentRoster: any[] = [];

      for (const st of batchStudents) {
        const sCode = (st as any).studentCode;
        if (!sCode) continue;

        const mDocId = `${sCode}_${tc}`;
        const mSnap = await adminDb.collection('studentTopicMastery').doc(mDocId).get();
        let mastery = 0;
        let confidence = 0;
        let reqConf = 18;

        if (mSnap.exists) {
          const md = mSnap.data()!;
          mastery = Number(md.mastery) || 0;
          confidence = Number(md.verifiedConfidence) || Number(md.confidence) || 0;
          reqConf = Number(md.requiredConfidence) || 18;
        }

        let status: 'mastered' | 'practicing' | 'needsAttention' | 'unattempted' = 'unattempted';
        if (mSnap.exists) {
          if (mastery >= 90 && confidence >= reqConf) {
            status = 'mastered';
            masteredCount++;
          } else if (mastery >= 50) {
            status = 'practicing';
            practicingCount++;
          } else {
            status = 'needsAttention';
            needsAttentionCount++;
          }
          scoreSum += mastery;
          evaluatedCount++;
        } else {
          // If unattempted, categorize as needs attention under Rule 2F
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
        students: studentRoster.sort((a, b) => a.mastery - b.mastery) // Lowest mastery first for rapid remediation
      });
    }

    // Sort topics by chapter and topicCode
    topicsData.sort((a, b) => a.topicCode.localeCompare(b.topicCode, undefined, { numeric: true }));

    return NextResponse.json({
      success: true,
      batchId,
      batchName: batchData.name || batchId,
      batchClass,
      totalStudents: batchStudents.length,
      conductedTopicsCount: topicsData.length,
      topics: topicsData
    });
  } catch (err: any) {
    console.error('Error in GET /api/admin/exams/topic-coverage:', err);
    return NextResponse.json({ message: err.message || 'Internal server error.' }, { status: 500 });
  }
}

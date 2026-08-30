import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { OBJECTIVE_QUESTION_TYPES, SUBJECTIVE_QUESTION_TYPES } from '@/lib/questionTypes';
import { verifyRole } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';
export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const docId = searchParams.get('docId') || '';
    const action = searchParams.get('action') || '';

    // Action A: Fetch candidate questions pool
    if (action === 'fetchPool') {
      const board = searchParams.get('board') || '';
      const classNum = searchParams.get('classNum') || '';
      const subject = searchParams.get('subject') || '';
      const topicNumbers = searchParams.get('topicNumbers') ? searchParams.get('topicNumbers')!.split(',') : [];
      const questionType = searchParams.get('questionType') || 'objective';
      const examCategory = searchParams.get('examCategory') || 'standard';

      if (!board || !classNum || !subject) {
        return NextResponse.json({ message: 'Missing parameters (board, classNum, subject).' }, { status: 400 });
      }

      // Query questions collection for matching board/class/subject + query existing exams to cross-check used questions
      const [questionsSnap, existingObjExamsSnap, existingSubjExamsSnap] = await Promise.all([
        adminDb.collection('questions')
          .where('board', '==', board)
          .where('class', '==', classNum)
          .where('subject', '==', subject)
          .get(),
        adminDb.collection('exams')
          .where('board', '==', board)
          .where('class', '==', classNum)
          .get(),
        adminDb.collection('subjectiveExams')
          .where('board', '==', board)
          .where('class', '==', classNum)
          .get()
      ]);

      // Collect all question codes/IDs that have been used in any existing exam
      const usedInExamsSet = new Set<string>();
      existingObjExamsSnap.docs.forEach(doc => {
        const edata = doc.data();
        const codes = edata.questionCodes || edata.questionIds || [];
        codes.forEach((c: string) => { if (c) usedInExamsSet.add(String(c).trim()); });
        if (Array.isArray(edata.questions)) {
          edata.questions.forEach((q: any) => {
            if (q?.id) usedInExamsSet.add(String(q.id).trim());
            if (q?.questionCode) usedInExamsSet.add(String(q.questionCode).trim());
          });
        }
      });
      existingSubjExamsSnap.docs.forEach(doc => {
        const edata = doc.data();
        const codes = edata.questionIds || edata.questionCodes || [];
        codes.forEach((c: string) => { if (c) usedInExamsSet.add(String(c).trim()); });
        if (Array.isArray(edata.questions)) {
          edata.questions.forEach((q: any) => {
            if (q?.id) usedInExamsSet.add(String(q.id).trim());
            if (q?.questionCode) usedInExamsSet.add(String(q.questionCode).trim());
          });
        }
      });

      const OBJECTIVE_TYPES = OBJECTIVE_QUESTION_TYPES.map(t => t.id);
      const SUBJECTIVE_TYPES = SUBJECTIVE_QUESTION_TYPES.map(t => t.id);
      const targetTypes = questionType === 'subjective' ? SUBJECTIVE_TYPES : OBJECTIVE_TYPES;

      const pool = questionsSnap.docs.map(doc => ({ id: doc.id, ...doc.data() as any }))
        .filter(q => {
          const typeMatch = targetTypes.includes(q.type);
          const isUsed = q.usedInClassroomTest === true || 
                         usedInExamsSet.has(String(q.id || '').trim()) || 
                         usedInExamsSet.has(String(q.questionCode || '').trim());
          const unusedMatch = !isUsed;
          const categoryMatch = (q.examCategory || 'standard') === examCategory;

          const searchTopics = topicNumbers.map(t => String(t).trim()).filter(Boolean);
          const topicMatch = searchTopics.length === 0 || searchTopics.some(tNum => 
            String(q.topicNumber || '').trim() === tNum ||
            String(q.subtopicNumber || '').trim() === tNum ||
            String(q.topicCode || '').trim() === tNum ||
            String(q.subtopicCode || '').trim() === tNum ||
            String(q.topicCode || '').endsWith(`-${tNum}`) ||
            String(q.subtopicCode || '').endsWith(`-${tNum}`)
          );

          return typeMatch && unusedMatch && categoryMatch && topicMatch;
        });

      return NextResponse.json({ success: true, count: pool.length, questions: pool });
    }

    // Action B: Fetch single syllabus document with live calculated question counts
    if (docId) {
      const docSnap = await adminDb.collection('syllabus').doc(docId).get();
      if (!docSnap.exists) {
        return NextResponse.json({ message: 'Subject syllabus not found.' }, { status: 404 });
      }

      const subjectData = docSnap.data()!;
      let questionsList: any[] = [];

      try {
        const boardVal = subjectData.board || '';
        const classVal = subjectData.class !== undefined ? subjectData.class : '';
        const subjectVal = subjectData.subject || '';

        const questionsSnap = await adminDb.collection('questions')
          .where('class', 'in', [String(classVal), Number(classVal)].filter(v => v !== ''))
          .get();

        questionsList = questionsSnap.docs
          .map(doc => {
            const q = doc.data();
            const b = String(q.board || '').toLowerCase();
            const s = String(q.subject || '').toLowerCase();
            const sc = String(q.subjectCode || '').toLowerCase();
            const bMatch = b === String(boardVal).toLowerCase() || 
                           b === String(subjectData.boardCode || '').toLowerCase() ||
                           (String(boardVal).toLowerCase().includes('cbse') && b.includes('cbse')) ||
                           (String(boardVal).toLowerCase().includes('mh') && (b.includes('mh') || b.includes('maharashtra')));
            const sMatch = s === String(subjectVal).toLowerCase() || 
                           sc === String(subjectData.subjectCode || '').toLowerCase() ||
                           s.includes(String(subjectVal).toLowerCase());
            if (!bMatch || !sMatch) return null;

            let chNum = String(q.chapterNumber || q.chapter || '').replace(/^Ch\.?\s*/i, '').trim();
            const topNum = String(q.topicNumber || '').trim();
            const subNum = String(q.subtopicNumber || '').trim();
            const tCode = String(q.topicCode || q.topic || '').trim();
            const sCode = String(q.subtopicCode || q.subtopic || '').trim();
            const qtype = q.type || '';
            const isObjective = !qtype.startsWith('subjective');

            if (!chNum && tCode.includes('-')) {
              const parts = tCode.split('-');
              if (parts.length >= 4) { chNum = parts[3]; }
            }
            if (!chNum && doc.id.includes('-')) {
              const parts = doc.id.split('-');
              if (parts.length >= 4) { chNum = parts[3]; }
            }

            return { id: doc.id, chNum, topNum, subNum, tCode, sCode, isObjective };
          })
          .filter(Boolean) as any[];
      } catch (err) {
        console.warn('Questions count query bypassed:', err);
      }

      const bCode = subjectData.boardCode || (String(subjectData.board || '').toUpperCase().includes('CBSE') ? 'CBSE' : 'MH');
      const cls = String(subjectData.class || '');
      const sCode = String(subjectData.subjectCode || '');
      const canonicalTopicPrefix = `${bCode}-${cls}-${sCode}`;

      try {
        const chapters = Array.isArray(subjectData.chapters) ? subjectData.chapters : [];
        chapters.forEach((chap: any) => {
          if (!chap || typeof chap !== 'object') return;
          const chapNumStr = String(chap.number ?? '').trim();
          
          const chapQuestions = questionsList.filter(q => {
            if (!q) return false;
            if (q.chNum && q.chNum === chapNumStr) return true;
            const tParts = String(q.tCode || '').split('-');
            if (tParts.length >= 4 && tParts[3] === chapNumStr) return true;
            const idParts = String(q.id || '').split('-');
            if (idParts.length >= 4 && idParts[3] === chapNumStr) return true;
            return false;
          });

          const topics = Array.isArray(chap.topics) ? chap.topics : [];
          topics.forEach((top: any) => {
            if (!top || typeof top !== 'object') return;
            const topNumStr = String(top.number ?? '').trim();
            const cleanTopicCode = String(top.topicCode || `${canonicalTopicPrefix}-${chapNumStr}-${topNumStr}`).trim();
            const subtopics = Array.isArray(top.subtopics) ? top.subtopics : [];

            const topicBranchQuestions = chapQuestions.filter(q => {
              if (!q) return false;
              const tCode = String(q.tCode || '');
              const sCode = String(q.sCode || '');
              const subNum = String(q.subNum || '');
              const id = String(q.id || '');

              if (q.topNum === topNumStr) return true;
              if (tCode === cleanTopicCode) return true;
              if (tCode === `${chapNumStr}.${topNumStr}` || tCode.endsWith(`-${chapNumStr}.${topNumStr}`)) return true;
              if (tCode.endsWith(`-${topNumStr}`)) return true;
              const tParts = tCode.split('-');
              if (tParts.length >= 5 && (tParts[4] === topNumStr || tParts[4] === `${chapNumStr}.${topNumStr}`)) return true;
              const idParts = id.split('-');
              if (idParts.length >= 5 && (idParts[4] === topNumStr || idParts[4] === `${chapNumStr}.${topNumStr}`)) return true;
              if (sCode.includes(`-${topNumStr}.`)) return true;
              if (subNum.startsWith(`${topNumStr}.`)) return true;
              return false;
            });

            if (subtopics.length > 0) {
              subtopics.forEach((sub: any) => {
                if (!sub || typeof sub !== 'object') return;
                const subNumStr = String(sub.number ?? '').trim();
                const cleanSubCode = String(sub.subtopicCode || `${canonicalTopicPrefix}-${chapNumStr}-${subNumStr}`).trim();
                const subQuestions = topicBranchQuestions.filter(q => {
                  if (!q) return false;
                  const sCode = String(q.sCode || '');
                  const subNum = String(q.subNum || '');
                  const id = String(q.id || '');

                  if (subNum && (subNum === subNumStr || subNum === `${topNumStr}.${subNumStr}` || subNum === `${chapNumStr}.${subNumStr}` || subNum === `${chapNumStr}.${topNumStr}.${subNumStr}` || subNum.endsWith(`.${subNumStr}`))) {
                    return true;
                  }
                  if (sCode && (sCode === cleanSubCode || sCode.endsWith(`-${subNumStr}`) || sCode.endsWith(`_${subNumStr}`) || sCode.endsWith(`.${subNumStr}`))) {
                    return true;
                  }
                  const sParts = sCode.split(/[-_]/);
                  if (sParts.length >= 6 && (sParts[5] === subNumStr || sParts[5] === `${topNumStr}.${subNumStr}`)) return true;
                  const idParts = id.split(/[-_]/);
                  if (idParts.length >= 6 && (idParts[5] === subNumStr || idParts[5] === `${topNumStr}.${subNumStr}`)) return true;

                  return false;
                });

                sub.objectiveCount = subQuestions.filter(q => q.isObjective).length;
                sub.subjectiveCount = subQuestions.filter(q => !q.isObjective).length;
              });
            }

            // Top-level topic objective/subjective count is the total unique questions under this topic branch
            top.objectiveCount = topicBranchQuestions.filter(q => q.isObjective).length;
            top.subjectiveCount = topicBranchQuestions.filter(q => !q.isObjective).length;
          });

          // Chapter total is the exact unique count of questions for this chapter
          chap.objectiveCount = chapQuestions.filter(q => q.isObjective).length;
          chap.subjectiveCount = chapQuestions.filter(q => !q.isObjective).length;
        });
      } catch (countErr) {
        console.warn('Chapter questions aggregation error bypassed:', countErr);
      }

      return NextResponse.json(subjectData);
    }

    // Default Action: Load templates, live syllabus collection, and metadata codes
    const [
      templatesSnap,
      syllabusSnap,
      boardCodesSnap,
      subjectCodesSnap
    ] = await Promise.all([
      adminDb.collection('templates').get(),
      adminDb.collection('syllabus').get(),
      adminDb.collection('config').doc('boardCodes').get(),
      adminDb.collection('config').doc('subjectCodes').get()
    ]);

    const templates = templatesSnap.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    const boardCodes: Record<string, string> = {
      'Maharashtra Board': 'MH',
      'CBSE': 'CBSE',
      'ICSE': 'ICSE',
      ...(boardCodesSnap.exists ? boardCodesSnap.data()! : {})
    };
    const subjectCodes: Record<string, string> = {
      ...(subjectCodesSnap.exists ? subjectCodesSnap.data()! : {})
    };

    // Dynamically build syllabusSubjects directly from live syllabus collection
    const subjectsMap: Record<string, Record<string, Record<string, { docId: string }>>> = {};

    syllabusSnap.docs.forEach(doc => {
      const data = doc.data();
      const board = data.board || 'Maharashtra Board';
      const cls = String(data.class || '8');
      const subject = data.subject;
      const subjectCode = data.subjectCode;
      const bCode = data.boardCode || (board.toLowerCase().includes('cbse') ? 'CBSE' : board.toLowerCase().includes('icse') ? 'ICSE' : 'MH');

      if (board && subject) {
        boardCodes[board] = bCode;
        if (subjectCode) {
          subjectCodes[subject] = subjectCode;
        }
        if (!subjectsMap[board]) {
          subjectsMap[board] = {};
        }
        if (!subjectsMap[board][cls]) {
          subjectsMap[board][cls] = {};
        }
        subjectsMap[board][cls][subject] = {
          docId: doc.id
        };
      }
    });

    const syllabusSubjects = {
      version: 1,
      subjects: subjectsMap
    };

    return NextResponse.json({
      templates,
      syllabusSubjects,
      boardCodes,
      subjectCodes
    });

  } catch (error: any) {
    console.error('API load exam generator metrics error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 2. POST - Handle saving generated questions OR creating final exams
export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { action } = body;

    if (!action) {
      return NextResponse.json({ message: 'Missing parameters (action).' }, { status: 400 });
    }

    // Compile and Save Final Exam
    if (action === 'saveExam') {
      const { 
        name, board, classNum, subjectName, subjects, subjectWeightage, weightageMode,
        chapter, chapterNumber, topicCodes, isMixed, totalMarks, questionCodes, templateId,
        templateDetails, duration, positiveMarks, negativeMarks, examType
      } = body;

      const boardCodesSnap = await adminDb.collection('config').doc('boardCodes').get();
      const subjectCodesSnap = await adminDb.collection('config').doc('subjectCodes').get();
      
      const boardCodes = boardCodesSnap.exists ? boardCodesSnap.data()! : {};
      const subjectCodes = subjectCodesSnap.exists ? subjectCodesSnap.data()! : {};

      const boardCode = boardCodes[board] || board.substring(0, 4).toUpperCase();
      const subjectCode = subjectCodes[subjectName] || subjectName.substring(0, 4).toUpperCase();

      // Check if all selected questions are subjective
      let isAllSubjective = false;
      if (questionCodes && questionCodes.length > 0) {
        const chunks = [];
        for (let i = 0; i < questionCodes.length; i += 30) {
          chunks.push(questionCodes.slice(i, i + 30));
        }

        const questionDocs: any[] = [];
        const snaps = await Promise.all(
          chunks.map(chunk =>
            adminDb.collection('questions')
              .where(admin.firestore.FieldPath.documentId(), 'in', chunk)
              .get()
          )
        );
        snaps.forEach(snap => {
          snap.docs.forEach(doc => questionDocs.push(doc.data()));
        });

        const subjectiveTypes = [
          'numerical_short', 'numerical_long', 'subjective_short', 
          'subjective_long', 'subjective_reason', 'subjective_notes', 'subjective_define',
          'subjective_laws'
        ];
        const hasObjective = questionDocs.some(q => !subjectiveTypes.includes(q.type));
        isAllSubjective = questionDocs.length > 0 && !hasObjective && examType !== 'obj' && examType !== 'objective';
      }

      const examTypeCode = isAllSubjective ? 'SUBJ' : (examType === 'entrance' ? 'ENTR' : 'OBJ');
      const cleanTopic = String((Array.isArray(topicCodes) && topicCodes[0]) || chapterNumber || '1_1').replace(/\./g, '_');
      const chapterPart = isMixed ? `${cleanTopic}_M` : cleanTopic;
      
      const now = new Date();
      const dateStr = `${String(now.getDate()).padStart(2,'0')}${String(now.getMonth()+1).padStart(2,'0')}${now.getFullYear()}`;

      // Generate atomic sequence ID using class-only counter
      const counterId = `class-${classNum}`;
      const counterRef = adminDb.collection('examCounters').doc(counterId);

      let initialSeq = 1;
      const counterSnap = await counterRef.get();
      if (!counterSnap.exists) {
        const [objectiveQuery, subjectiveQuery] = await Promise.all([
          adminDb.collection('exams')
            .where('class', '==', classNum)
            .get(),
          adminDb.collection('subjectiveExams')
            .where('class', '==', classNum)
            .get()
        ]);
        initialSeq = objectiveQuery.size + subjectiveQuery.size + 1;
      }

      const nextSeq = await adminDb.runTransaction(async (tx) => {
        const snap = await tx.get(counterRef);
        const seqNow = (snap.exists && snap.data()?.nextSequence) || initialSeq;
        tx.set(counterRef, { nextSequence: seqNow + 1 }, { merge: true });
        return seqNow;
      });

      const seq3digit = String(nextSeq).padStart(3, '0');
      const examId = `${boardCode}-${classNum}-${subjectCode}-${examTypeCode}-${chapterPart}-${dateStr}-${nextSeq}`;

      const getTwoWords = (chName: string) => {
        if (!chName) return '';
        const clean = chName.replace(/[^a-zA-Z0-9\s-]/g, '').trim();
        const words = clean.split(/\s+/).filter(w => w.length > 0 && w.toLowerCase() !== 'and');
        if (words.length >= 2) return `${words[0]} ${words[1]}`;
        return words[0] || '';
      };
      
      const twoWords = getTwoWords(chapter || '');
      const chapterDisplayPart = twoWords || chapterPart;
      const dateStrYY = `${String(now.getDate()).padStart(2,'0')}${String(now.getMonth()+1).padStart(2,'0')}${String(now.getFullYear()).substring(2, 4)}`;

      const examData: any = {
        examId,
        name: name || `${seq3digit}-${classNum}-${subjectCode}-${chapterDisplayPart}-${isAllSubjective ? 'Sub' : 'Obj'}-${dateStrYY}`,
        sequence: nextSeq,
        sequence3digit: seq3digit,
        board,
        boardCode,
        class: classNum,
        subjectCode,
        subjects: subjects || [subjectName],
        subjectWeightage: subjectWeightage || {},
        weightageMode: weightageMode || 'equal',
        chapter: chapter || '',
        chapterNumber: chapterNumber || '',
        topicCodes: topicCodes || [],
        isMixed: !!isMixed,
        examType: examType || (isAllSubjective ? 'subjective' : 'obj'),
        totalMarks: Number(totalMarks) || 0,
        questionCount: Array.isArray(questionCodes) ? questionCodes.length : 0,
        status: 'active',
        createdAt: admin.firestore.FieldValue.serverTimestamp(),
        createdBy: (adminUser.decodedToken?.email || adminUser.userData?.email) || 'admin@yashcom.com',
        templateId: templateId || '',
        templateDetails: templateDetails || {},
        duration: Number(duration) || 30,
        source: 'exam_generator'
      };

      if (isAllSubjective) {
        examData.questionIds = questionCodes || [];
        examData.mode = 'home';
        examData.totalTime = Number(duration) || 90;
        await adminDb.collection('subjectiveExams').doc(examId).set(examData);
      } else {
        examData.questionCodes = questionCodes || [];
        examData.positiveMarks = Number(positiveMarks) || 4;
        examData.negativeMarks = Number(negativeMarks) ?? 1;
        await adminDb.collection('exams').doc(examId).set(examData);
      }

      // Mark all selected candidate questions as used
      const batch = new ChunkedBatch(adminDb);
      const validCodes = (Array.isArray(questionCodes) ? questionCodes : []).filter(Boolean);
      
      // Update by direct doc ID
      for (const qcode of validCodes) {
        const questionRef = adminDb.collection('questions').doc(qcode);
        batch.set(questionRef, { usedInClassroomTest: true }, { merge: true });
      }

      // Also query and mark questions where questionCode == qcode in case doc.id is an auto-ID
      if (validCodes.length > 0) {
        const chunks = [];
        for (let i = 0; i < validCodes.length; i += 30) {
          chunks.push(validCodes.slice(i, i + 30));
        }
        for (const chunk of chunks) {
          try {
            const matchedSnap = await adminDb.collection('questions')
              .where('questionCode', 'in', chunk)
              .get();
            matchedSnap.docs.forEach(doc => {
              batch.set(doc.ref, { usedInClassroomTest: true }, { merge: true });
            });
          } catch (mErr) {
            console.warn('Matching questionCode lookup warning:', mErr);
          }
        }
      }

      try {
        await batch.commit();
      } catch (bErr) {
        console.warn('Batch mark questions as used warning:', bErr);
      }

      return NextResponse.json({ success: true, examId });
    }

    return NextResponse.json({ message: 'Action not found.' }, { status: 400 });

  } catch (error: any) {
    console.error('API create generated exam error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

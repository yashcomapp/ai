import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { QuestionRepository } from '@/repositories/question.repository';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { validateQuestion, normalizeBloomLevel, OBJECTIVE_QUESTION_TYPES, SUBJECTIVE_QUESTION_TYPES, QUESTION_TYPE_MAP } from '@/lib/questionTypes';
import { getFromCache, setInCache, invalidateCache } from '@/lib/firebase/cache';
export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    
    // Support fetching comma-separated list of question IDs or questionCodes directly
    const idsParam = searchParams.get('ids') || '';
    if (idsParam) {
      const ids = idsParam.split(',').map(s => s.trim()).filter(Boolean);
      if (ids.length > 0) {
        const refs = ids.map(id => adminDb.collection('questions').doc(id));
        const snaps = await adminDb.getAll(...refs).catch(() => []);
        let questions = snaps
          .filter(s => !!s && s.exists)
          .map(s => ({ id: s.id, ...s.data() }));

        // Fallback: If some question codes were passed instead of doc IDs, query by questionCode
        if (questions.length < ids.length) {
          const qSnap = await adminDb.collection('questions')
            .where('questionCode', 'in', ids.slice(0, 30))
            .get()
            .catch(() => null);

          if (qSnap && !qSnap.empty) {
            const extra = qSnap.docs.map(doc => ({ id: doc.id, ...doc.data() }));
            const existingIds = new Set(questions.map(q => q.id));
            extra.forEach(eq => {
              if (!existingIds.has(eq.id)) {
                questions.push(eq);
              }
            });
          }
        }

        return NextResponse.json({ questions });
      }
    }

    const action = searchParams.get('action') || '';

    // Scenario B: Scan for duplicate questions
    if (action === 'fetchDuplicates') {
      let filterBoard = searchParams.get('board') || '';
      if (filterBoard === 'MSBSHSE' || filterBoard === 'MH' || filterBoard === 'State Board') {
        filterBoard = 'Maharashtra Board';
      }
      let filterClass = searchParams.get('classNum') || searchParams.get('class') || '';
      if (filterClass.includes('Class')) {
        const match = filterClass.match(/\d+/);
        if (match) filterClass = match[0];
      }
      const filterSubject = searchParams.get('subject') || '';

      const filters = (filterBoard || filterClass || filterSubject) ? {
        board: filterBoard || undefined,
        classNum: filterClass || undefined,
        subject: filterSubject || undefined
      } : undefined;

      const duplicateGroups = await QuestionRepository.getDuplicateGroups(10000, filters);
      return NextResponse.json({ duplicateGroups });
    }

    // Default Scenario: Paginated Questions List with filters
    let board = searchParams.get('board') || '';
    if (board === 'MSBSHSE' || board === 'MH' || board === 'State Board') {
      board = 'Maharashtra Board';
    }
    let classNum = searchParams.get('classNum') || searchParams.get('class') || '';
    if (classNum.includes('Class')) {
      const match = classNum.match(/\d+/);
      if (match) classNum = match[0];
    }
    const subject = searchParams.get('subject') || '';
    
    let rawChapter = searchParams.get('chapterNumber') || searchParams.get('chapter') || '';
    let cleanChapNum = '';
    if (rawChapter) {
      const match = rawChapter.match(/\d+/);
      if (match) cleanChapNum = match[0];
      else cleanChapNum = rawChapter.trim();
    }

    const topicNumber = searchParams.get('topicNumber') || searchParams.get('topic') || '';
    const category = searchParams.get('category') || '';
    const type = searchParams.get('type') || '';
    const limitVal = parseInt(searchParams.get('limit') || '20');
    const lastCode = searchParams.get('lastCode') || '';
    const usageStatus = searchParams.get('usageStatus') || '';

    // Fetch base documents matching board, class, subject (in-memory cached)
    const cacheKey = `qb_base_${board}_${classNum}_${subject}`;
    let allQuestions = getFromCache<any[]>(cacheKey);

    if (!allQuestions) {
      let baseQuery: admin.firestore.Query = adminDb.collection('questions');
      if (board) baseQuery = baseQuery.where('board', '==', board);
      if (classNum) baseQuery = baseQuery.where('class', '==', classNum);
      if (subject) baseQuery = baseQuery.where('subject', '==', subject);

      const baseSnap = await baseQuery.get();
      allQuestions = baseSnap.docs.map(doc => ({ id: doc.id, ...doc.data() as any }));
      setInCache(cacheKey, allQuestions, 180000); // 3 mins cache
    }

    // In-memory filter for chapter, topic, category, type, usageStatus
    allQuestions = allQuestions.filter(q => {
      // Chapter check
      if (cleanChapNum) {
        const qCh = String(q.chapterNumber || q.chapter || '').trim();
        const chMatch = qCh === cleanChapNum || qCh.startsWith(`Chapter ${cleanChapNum}`) || qCh.startsWith(`Ch.${cleanChapNum}`);
        if (!chMatch) return false;
      }

      // Topic check
      if (topicNumber) {
        const qTopNum = String(q.topicNumber || '').trim();
        const qSubNum = String(q.subtopicNumber || '').trim();
        const qTopCode = String(q.topicCode || q.topic || '').trim();
        const qSubCode = String(q.subtopicCode || q.subtopic || '').trim();
        const searchTop = String(topicNumber).trim();

        const matchesTop = qTopNum === searchTop || qSubNum === searchTop ||
          qTopCode === searchTop || qSubCode === searchTop ||
          qTopCode.endsWith(`-${searchTop}`) || qSubCode.endsWith(`-${searchTop}`) ||
          qTopCode.includes(`-${searchTop}-`) || qSubCode.includes(`-${searchTop}-`);
        if (!matchesTop) return false;
      }

      // Type check
      if (type) {
        if (q.type !== type) return false;
      } else if (category === 'objective') {
        const objTypes = OBJECTIVE_QUESTION_TYPES.map(t => t.id);
        if (!objTypes.includes(q.type)) return false;
      } else if (category === 'subjective') {
        const subjTypes = SUBJECTIVE_QUESTION_TYPES.map(t => t.id);
        if (!subjTypes.includes(q.type)) return false;
      }

      // Usage status check
      if (usageStatus === 'used') {
        if (q.usedInClassroomTest !== true) return false;
      } else if (usageStatus === 'unused') {
        if (q.usedInClassroomTest === true) return false;
      }

      return true;
    });

    const totalCount = allQuestions.length;

    if (limitVal <= 0) {
      return NextResponse.json({ questions: [], totalCount });
    }

    let paginated = allQuestions;
    if (lastCode) {
      const startIndex = allQuestions.findIndex(item => item.id === lastCode);
      if (startIndex !== -1) {
        paginated = allQuestions.slice(startIndex + 1);
      }
    }
    paginated = paginated.slice(0, limitVal);

    return NextResponse.json({
      questions: paginated,
      totalCount
    });
  } catch (error: any) {
    console.error('API load questions error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}



// 2. POST - Save (Create/Update) question
export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { action } = body;

    if (action === 'bulkSave' || (Array.isArray(body.questions) && body.questions.length > 0)) {
      const { questions } = body;
      if (!Array.isArray(questions) || questions.length === 0) {
        return NextResponse.json({ message: 'Invalid or empty questions array.' }, { status: 400 });
      }

      // Pre-fetch boardCodes & subjectCodes config
      const boardCodesSnap = await adminDb.collection('config').doc('boardCodes').get();
      const subjectCodesSnap = await adminDb.collection('config').doc('subjectCodes').get();
      const boardCodes = boardCodesSnap.exists ? boardCodesSnap.data()! : {};
      const subjectCodes = subjectCodesSnap.exists ? subjectCodesSnap.data()! : {};

      const createdByEmail = (adminUser.decodedToken?.email || adminUser.userData?.email) || 'admin@yashcom.com';

      // 1. Group questions by counterId to allocate sequence numbers efficiently
      const counterNeeds: Record<string, number> = {};
      const processedItems: any[] = [];

      for (let idx = 0; idx < questions.length; idx++) {
        const item = questions[idx];
        const qtype = item.qtype || item.type || 'single_mcq';
        const board = item.board;
        const classNum = item.classNum || item.class;
        const subjectName = item.subjectName || item.subject;
        const text = item.text;

        if (!text || !qtype || !board || !classNum || !subjectName) {
          return NextResponse.json({ message: `Question #${idx + 1} is missing required fields.` }, { status: 400 });
        }

        let finalBoard = String(board).trim();
        if (finalBoard === 'MSBSHSE' || finalBoard === 'MH') {
          finalBoard = 'Maharashtra Board';
        }

        const boardCode = boardCodes[board] || board.substring(0, 4).toUpperCase();
        const subjectCode = subjectCodes[subjectName] || subjectName.substring(0, 4).toUpperCase();
        const typeCode = QUESTION_TYPE_MAP[qtype]?.code || 'SSA';
        const chapterPart = item.chapterNumber || '01';
        const topicPart = item.topicNumber || '1.1';
        const topicCode = `${boardCode}-${classNum}-${subjectCode}-${chapterPart}-${topicPart}`;
        const counterId = `${topicCode}-${typeCode}`;

        counterNeeds[counterId] = (counterNeeds[counterId] || 0) + 1;
        processedItems.push({
          item,
          qtype,
          finalBoard,
          boardCode,
          subjectCode,
          typeCode,
          chapterPart,
          topicPart,
          topicCode,
          counterId
        });
      }

      // 2. Transactionally reserve sequence numbers for all counterIds
      const startSeqMap: Record<string, number> = {};
      await adminDb.runTransaction(async (tx) => {
        const counterRefs = Object.keys(counterNeeds).map(cid => adminDb.collection('questionCounters').doc(cid));
        const snaps = await tx.getAll(...counterRefs);
        
        snaps.forEach(snap => {
          const cid = snap.id;
          const needed = counterNeeds[cid];
          const currentSeq = snap.exists && snap.data() ? (snap.data()!.nextSequence || 1) : 1;
          startSeqMap[cid] = currentSeq;
          tx.set(snap.ref, { nextSequence: currentSeq + needed }, { merge: true });
        });
      });

      // 3. Pre-fetch syllabus topic names
      const uniqueTopicCodes = Array.from(new Set(processedItems.map(p => p.topicCode)));
      const topicNameMap: Record<string, string> = {};
      if (uniqueTopicCodes.length > 0) {
        try {
          const refs = uniqueTopicCodes.map(tc => adminDb.collection('syllabusTopicIndex').doc(tc));
          const snaps = await adminDb.getAll(...refs);
          snaps.forEach(snap => {
            if (snap.exists) topicNameMap[snap.id] = snap.data()?.topicName || '';
          });
        } catch (e) {
          console.warn('Failed to pre-fetch syllabus topic names:', e);
        }
      }

      // 4. Validate & prepare document batch
      const currentSeqOffset: Record<string, number> = { ...startSeqMap };
      const batch = new ChunkedBatch(adminDb);
      const marksMap: { [key: string]: number } = {
        single_mcq: 4, multiple_mcq: 4, true_false: 4, assertion_reason: 4, fill_blanks: 4,
        numerical: 4, numerical5: 4, numerical_short: 2, numerical_long: 4,
        subjective_short: 2, subjective_long: 4, subjective_reason: 2, subjective_notes: 2,
        subjective_define: 1, subjective_laws: 1
      };

      for (let idx = 0; idx < processedItems.length; idx++) {
        const p = processedItems[idx];
        const { item, qtype, finalBoard, topicPart, topicCode, counterId } = p;

        const seqNum = currentSeqOffset[counterId]++;
        const seqStr = String(seqNum).padStart(3, '0');
        const finalCode = item.id || `${counterId}-${seqStr}`;
        const normalizedQType = qtype === 'numerical5' ? 'numerical' : qtype;

        let finalTopicName = (topicNameMap[topicCode] || item.topic || item.topicName || '').trim();
        if (topicPart && finalTopicName.startsWith(topicPart)) {
          finalTopicName = finalTopicName.substring(topicPart.length).replace(/^[:\s\-]+/g, '').trim();
        }

        const resolvedMarks = marksMap[normalizedQType] ?? (Number(item.marks) > 0 ? Number(item.marks) : 4);
        const questionDoc: any = {
          questionCode: finalCode,
          type: normalizedQType,
          text: item.text,
          options: item.options || [],
          correctAnswer: item.correctAnswer || '',
          correctAnswers: item.correctAnswers || [],
          assertion: item.assertion || '',
          reason: item.reason || '',
          solution: item.solution || '',
          difficulty: item.difficulty || 'medium',
          bloomLevel: normalizeBloomLevel(item.bloomLevel, item.difficulty, normalizedQType),
          board: finalBoard,
          class: item.classNum || item.class,
          subject: item.subjectName || item.subject,
          chapterNumber: item.chapterNumber || '1',
          topicNumber: item.topicNumber || '1.1',
          topic: finalTopicName,
          topicName: finalTopicName,
          textbookPracticeSet: item.textbookPracticeSet || '',
          textbookProblemSet: item.textbookProblemSet || '',
          isSolvedExample: !!item.isSolvedExample,
          isTheorem: !!item.isTheorem,
          requiresFigure: !!item.requiresFigure,
          imageUrl: item.imageUrl || '',
          keywords: item.keywords || [],
          marks: resolvedMarks,
          examCategory: item.examCategory || 'standard',
          createdAt: admin.firestore.FieldValue.serverTimestamp(),
          createdBy: createdByEmail,
          timesUsed: 0,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        };

        const isObjective = normalizedQType === 'numerical' || (!normalizedQType.startsWith('subjective') && normalizedQType !== 'numerical_short' && normalizedQType !== 'numerical_long');
        const validationErrors = validateQuestion(questionDoc, isObjective ? 'objective' : 'subjective');
        if (validationErrors.length > 0) {
          return NextResponse.json({ message: `Question #${idx + 1} validation failed: ${validationErrors.join(', ')}` }, { status: 400 });
        }

        const docRef = adminDb.collection('questions').doc(finalCode);
        batch.set(docRef, questionDoc, { merge: true });
      }

      await batch.commit();
      invalidateCache('qb_base_');
      return NextResponse.json({ success: true, count: processedItems.length, savedCount: processedItems.length });
    }

    const { id, qtype, text, options, correctAnswer, correctAnswers, assertion, reason, solution, difficulty, bloomLevel, board, classNum, subjectName, chapterNumber, topicNumber, topic, topicName, textbookPracticeSet, textbookProblemSet, isSolvedExample, isTheorem, requiresFigure, imageUrl, keywords, examCategory } = body;

    if (!text || !qtype || !board || !classNum || !subjectName) {
      return NextResponse.json({ message: 'Missing required parameters.' }, { status: 400 });
    }

    let finalBoard = String(board).trim();
    if (finalBoard === 'MSBSHSE' || finalBoard === 'MH') {
      finalBoard = 'Maharashtra Board';
    }

    // Load board codes and subject codes maps
    const boardCodesSnap = await adminDb.collection('config').doc('boardCodes').get();
    const subjectCodesSnap = await adminDb.collection('config').doc('subjectCodes').get();
    const boardCodes = boardCodesSnap.exists ? boardCodesSnap.data()! : {};
    const subjectCodes = subjectCodesSnap.exists ? subjectCodesSnap.data()! : {};

    const boardCode = boardCodes[board] || board.substring(0, 4).toUpperCase();
    const subjectCode = subjectCodes[subjectName] || subjectName.substring(0, 4).toUpperCase();

    const typeCode = QUESTION_TYPE_MAP[qtype]?.code || 'SSA';

    let finalCode = id || '';

    // If adding a new question, compile sequential ID via transaction
    if (!finalCode) {
      const chapterPart = chapterNumber || '01';
      const topicPart = topicNumber || '1.1';
      const topicCode = `${boardCode}-${classNum}-${subjectCode}-${chapterPart}-${topicPart}`;

      const counterId = `${topicCode}-${typeCode}`;
      const counterRef = adminDb.collection('questionCounters').doc(counterId);

      const nextSeq = await adminDb.runTransaction(async (tx) => {
        const snap = await tx.get(counterRef);
        const seqNow = snap.exists && snap.data() ? (snap.data()!.nextSequence || 1) : 1;
        tx.set(counterRef, { nextSequence: seqNow + 1 }, { merge: true });
        return seqNow;
      });

      const seqStr = String(nextSeq).padStart(3, '0');
      finalCode = `${counterId}-${seqStr}`;
    }

    const normalizedQType = qtype === 'numerical5' ? 'numerical' : qtype;

    const marksMap: { [key: string]: number } = {
      single_mcq: 4,
      multiple_mcq: 4,
      true_false: 4,
      assertion_reason: 4,
      fill_blanks: 4,
      numerical: 4,
      numerical5: 4,
      numerical_short: 2,
      numerical_long: 4,
      subjective_short: 2,
      subjective_long: 4,
      subjective_reason: 2,
      subjective_notes: 2,
      subjective_define: 1,
      subjective_laws: 1
    };
    // Resolve clean topic name using master syllabus index
    let finalTopicName = (topic || topicName || '').trim();
    const chapterPart = chapterNumber || '01';
    const topicPart = topicNumber || '1.1';
    const topicCode = `${boardCode}-${classNum}-${subjectCode}-${chapterPart}-${topicPart}`;

    try {
      const syllabusDoc = await adminDb.collection('syllabusTopicIndex').doc(topicCode).get();
      if (syllabusDoc.exists) {
        finalTopicName = syllabusDoc.data()?.topicName || finalTopicName;
      }
    } catch (e) {
      console.warn('Failed to fetch topic name for:', topicCode, e);
    }

    // Double check & strip redundant topic number prefix
    if (topicPart && finalTopicName.startsWith(topicPart)) {
      finalTopicName = finalTopicName.substring(topicPart.length).replace(/^[:\s\-]+/g, '').trim();
    }

    const resolvedMarks = marksMap[normalizedQType] ?? (Number(body.marks) > 0 ? Number(body.marks) : 4);

    const questionDoc: any = {
      questionCode: finalCode,
      type: normalizedQType,
      text,
      options: options || [],
      correctAnswer: correctAnswer || '',
      correctAnswers: correctAnswers || [],
      assertion: assertion || '',
      reason: reason || '',
      solution: solution || '',
      difficulty: difficulty || 'medium',
      bloomLevel: normalizeBloomLevel(bloomLevel, difficulty, normalizedQType),
      board: finalBoard,
      class: classNum,
      subject: subjectName,
      chapterNumber: chapterNumber || '1',
      topicNumber: topicNumber || '1.1',
      topic: finalTopicName,
      topicName: finalTopicName,
      textbookPracticeSet: textbookPracticeSet || '',
      textbookProblemSet: textbookProblemSet || '',
      isSolvedExample: !!isSolvedExample,
      isTheorem: !!isTheorem,
      requiresFigure: !!requiresFigure,
      imageUrl: imageUrl || '',
      keywords: keywords || [],
      marks: resolvedMarks,
      examCategory: examCategory || 'standard',
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    };

    // Run SSOT validation check on backend as final guard
    const isObjective = normalizedQType === 'numerical' || (!normalizedQType.startsWith('subjective') && normalizedQType !== 'numerical_short' && normalizedQType !== 'numerical_long');
    const validationErrors = validateQuestion(questionDoc, isObjective ? 'objective' : 'subjective');
    if (validationErrors.length > 0) {
      return NextResponse.json({ message: `Question validation failed: ${validationErrors.join(', ')}` }, { status: 400 });
    }

    if (!id) {
      questionDoc.createdAt = admin.firestore.FieldValue.serverTimestamp();
      questionDoc.createdBy = (adminUser.decodedToken?.email || adminUser.userData?.email) || 'admin@yashcom.com';
      questionDoc.timesUsed = 0;
    }

    await adminDb.collection('questions').doc(finalCode).set(questionDoc, { merge: true });
    invalidateCache('qb_base_');

    return NextResponse.json({ success: true, questionCode: finalCode });

  } catch (error: any) {
    console.error('API save question error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 3. DELETE - Delete question or list of questions in bulk
export async function DELETE(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const id = searchParams.get('id') || '';

    // Handle single question deletion
    if (id) {
      await adminDb.collection('questions').doc(id).delete();
      invalidateCache('qb_base_');
      return NextResponse.json({ success: true });
    }

    // Handle bulk questions deletion
    const body = await req.json();
    const { ids } = body;

    if (!Array.isArray(ids) || ids.length === 0) {
      return NextResponse.json({ message: 'Missing parameters (ids).' }, { status: 400 });
    }

    const batch = new ChunkedBatch(adminDb);
    ids.forEach(qCode => {
      const docRef = adminDb.collection('questions').doc(qCode);
      batch.delete(docRef);
    });
    await batch.commit();
    invalidateCache('qb_base_');

    return NextResponse.json({ success: true, count: ids.length });

  } catch (error: any) {
    console.error('API delete questions error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

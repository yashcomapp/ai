import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole, verifyAnyRole } from '@/lib/auth';
import { getCachedSyllabusList, getFromCache, setInCache, invalidateCache } from '@/lib/firebase/cache';
import { 
  getCanonicalBoardCode, 
  getCanonicalBoardName, 
  getCanonicalClass, 
  getCanonicalSubjectCode 
} from '@/lib/syllabusUtils';
export const dynamic = 'force-dynamic';

const matchTopicCode = (examTopicCodes: any, cleanCode: string, number: string, chapNum: string) => {
  if (!Array.isArray(examTopicCodes)) return false;
  const cleanCodeLower = String(cleanCode || '').toLowerCase().trim();
  const numStr = String(number || '').trim();
  const chapNumStr = String(chapNum || '').trim();
  
  const compareNum = numStr.replace(/[-_]/g, '.');
  const compareChapNum = `${chapNumStr}.${numStr}`.replace(/[-_]/g, '.');

  return examTopicCodes.some((code: any) => {
    if (!code) return false;
    const c = String(code).toLowerCase().trim();
    if (c === cleanCodeLower) return true;
    if (c === numStr) return true;
    
    const compareC = c.replace(/[-_]/g, '.');
    if (compareC === compareNum) return true;
    if (compareC === compareChapNum) return true;
    
    // Boundary-aware suffix match for full topic code
    if (cleanCodeLower.endsWith('-' + c) || cleanCodeLower.endsWith('_' + c)) return true;
    
    // Boundary-aware suffix match for exam code ending in topic number
    if (c.endsWith('-' + compareNum) || c.endsWith('_' + compareNum)) return true;
    if (c.endsWith('-' + compareChapNum) || c.endsWith('_' + compareChapNum)) return true;

    return false;
  });
};

export async function GET(req: NextRequest) {
  try {
    const authResult = await verifyAnyRole(req, ['admin']);
    if (!authResult) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const subjectId = searchParams.get('subjectId') || '';

    if (subjectId) {
      const cacheKey = `syllabus_subject_${subjectId}`;
      const cached = getFromCache<any>(cacheKey);
      if (cached) {
        return NextResponse.json(cached, {
          headers: {
            'Cache-Control': 'private, max-age=30, stale-while-revalidate=60'
          }
        });
      }

      const docSnap = await adminDb.collection('syllabus').doc(subjectId).get();
      if (!docSnap.exists) {
        return NextResponse.json({ message: 'Subject not found.' }, { status: 404 });
      }

      const subjectData = docSnap.data()!;

      // 1. Fetch questions matching board, class, subject
      const qCounts: Record<string, { obj: number; subj: number }> = {};
      try {
        const boardVal = subjectData.board || '';
        const classVal = subjectData.class !== undefined ? subjectData.class : '';
        const subjectVal = subjectData.subject || '';

        const cleanClassVal = String(classVal).replace(/\D/g, '');

        const questionsSnap = await adminDb.collection('questions')
          .where('class', '==', cleanClassVal)
          .get();

        questionsSnap.docs.forEach(doc => {
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
          if (!bMatch || !sMatch) return;

          const chNum = String(q.chapterNumber || '').trim();
          const topNum = String(q.topicNumber || '').trim();
          const subNum = String(q.subtopicNumber || '').trim();
          const tCode = String(q.topicCode || q.topic || '').trim();
          const sCode = String(q.subtopicCode || q.subtopic || '').trim();
          const qtype = q.type || '';
          const isObjective = !qtype.startsWith('subjective');

          const increment = (k: string) => {
            if (!k) return;
            if (!qCounts[k]) qCounts[k] = { obj: 0, subj: 0 };
            if (isObjective) qCounts[k].obj++;
            else qCounts[k].subj++;
          };

          // 1. Direct topicCode / topic
          increment(tCode);

          // 2. Direct subtopicCode / subtopic
          increment(sCode);

          // 3. Direct `${chNum}_${topNum}` or `${chNum}_${subNum}`
          if (chNum && topNum) increment(`${chNum}_${topNum}`);
          if (chNum && subNum) increment(`${chNum}_${subNum}`);

          // 4. Derived `${chap}_${top}` from topicCode
          if (tCode.includes('-')) {
            const parts = tCode.split('-');
            if (parts.length >= 5) {
              const derivedChap = parts[3];
              const derivedTop = parts[4];
              increment(`${derivedChap}_${derivedTop}`);
            }
          }

          // 5. Derived `${chap}_${sub}` from subtopicCode
          if (sCode.includes('-')) {
            const parts = sCode.split('-');
            if (parts.length >= 5) {
              const derivedChap = parts[3];
              const derivedSub = parts[4];
              increment(`${derivedChap}_${derivedSub}`);
            }
          }
        });
      } catch (err) {
        console.warn('Syllabus questions count error bypassed:', err);
      }

      // 2. Fetch exams to count test coverage
      let examsList: any[] = [];
      let subjectiveExamsList: any[] = [];
      try {
        const cleanClassVal = String(subjectData.class !== undefined ? subjectData.class : '').replace(/\D/g, '');
        const [examsSnap, subjectiveExamsSnap] = await Promise.all([
          adminDb.collection('exams')
            .where('class', '==', cleanClassVal)
            .get(),
          adminDb.collection('subjectiveExams')
            .where('class', '==', cleanClassVal)
            .get()
        ]);

        examsList = examsSnap.docs
          .map(doc => ({ id: doc.id, ...doc.data() as any }))
          .filter(exam => {
            const isPractice = exam.id.startsWith('PRACTICE_') || exam.type === 'practice' || exam.isPractice === true;
            const scMatch = !subjectData.subjectCode || exam.subjectCode === subjectData.subjectCode;
            const subjMatch = !subjectData.subject || (Array.isArray(exam.subjects) && exam.subjects.includes(subjectData.subject)) || exam.subject === subjectData.subject;
            return !isPractice && (scMatch || subjMatch);
          });

        subjectiveExamsList = subjectiveExamsSnap.docs
          .map(doc => ({ id: doc.id, ...doc.data() as any }))
          .filter(exam => {
            const isPractice = exam.id.startsWith('PRACTICE_') || exam.type === 'home_practice' || exam.isPractice === true;
            const subjMatch = !subjectData.subject || exam.subject === subjectData.subject || exam.subjectCode === subjectData.subjectCode;
            return !isPractice && subjMatch;
          });
      } catch (examErr) {
        console.warn('Exams count query bypassed:', examErr);
      }

      const getUniqueTests = (testsArr: any[]) => {
        const seen = new Set();
        return (testsArr || []).filter(t => {
          if (!t || seen.has(t.id)) return false;
          seen.add(t.id);
          return true;
        });
      };

      const bCode = subjectData.boardCode || (String(subjectData.board || '').toUpperCase().includes('CBSE') ? 'CBSE' : 'MH');
      const cls = String(subjectData.class || '');
      const sCode = String(subjectData.subjectCode || '');
      const canonicalTopicPrefix = `${bCode}-${cls}-${sCode}`;

      const chapters = Array.isArray(subjectData.chapters) ? subjectData.chapters : [];
      try {
        chapters.forEach((chap: any) => {
          if (!chap || typeof chap !== 'object') return;
          let chObj = 0;
          let chSubj = 0;
          const allTestsCountsUnderChapter: number[] = [];
          const chapNumStr = String(chap.number ?? '').trim();

          const topics = Array.isArray(chap.topics) ? chap.topics : [];
          topics.forEach((top: any) => {
            if (!top || typeof top !== 'object') return;
            const topNumStr = String(top.number ?? '').trim();
            const topicCode = top.topicCode || `${canonicalTopicPrefix}-${chapNumStr}-${topNumStr}`;
            const cleanTopicCode = String(topicCode).trim();

            // Count questions for this topic/subtopic
            const topicKey = `${chapNumStr}_${topNumStr}`;
            const topicQStats = qCounts[cleanTopicCode] || qCounts[topicKey] || { obj: 0, subj: 0 };
            
            let topObj = topicQStats.obj;
            let topSubj = topicQStats.subj;

            // Count tests covering this topic directly
            let directTopicTests = 0;
            const directTopicTestsList: any[] = [];
            
            // Match objective exams
            examsList.forEach(exam => {
              const topicCodes = Array.isArray(exam.topicCodes) ? exam.topicCodes : [];
              const isMatch = matchTopicCode(topicCodes, cleanTopicCode, topNumStr, chapNumStr);
              if (isMatch) {
                directTopicTests++;
                directTopicTestsList.push({ id: exam.id, name: exam.name || exam.examCode || exam.id, type: 'objective' });
              }
            });

            // Match subjective exams
            subjectiveExamsList.forEach(exam => {
              const topicCodes = Array.isArray(exam.topicCodes) ? exam.topicCodes : [];
              let isMatch = matchTopicCode(topicCodes, cleanTopicCode, topNumStr, chapNumStr);

              // Fallback 1: first question code
              if (!isMatch) {
                const qIds = Array.isArray(exam.questionIds) ? exam.questionIds : [];
                if (qIds.length > 0) {
                  const qId = String(qIds[0] || '');
                  const cleanCode = qId.replace(/[-_]\d+$/, '');
                  const parts = cleanCode.split(/[-_]/);
                  if (parts.length >= 5) {
                    let derived = '';
                    if (parts[4].includes('.')) {
                      derived = `${parts[0]}-${parts[1]}-${parts[2]}-${parts[3]}-${parts[4]}`;
                    } else if (parts.length >= 7 && /^\d+$/.test(parts[4]) && /^\d+$/.test(parts[5]) && /^\d+$/.test(parts[6])) {
                      derived = `${parts[0]}-${parts[1]}-${parts[2]}-${parts[4]}-${parts[5]}.${parts[6]}`;
                    }
                    if (derived === cleanTopicCode) isMatch = true;
                  }
                }
              }

              // Fallback 2: topic name match
              if (!isMatch) {
                const examTopics = Array.isArray(exam.topics) ? exam.topics : [];
                if (examTopics.some((tName: any) => String(tName || '').toLowerCase() === String(top.name || '').toLowerCase())) {
                  isMatch = true;
                }
              }

              if (isMatch) {
                directTopicTests++;
                directTopicTestsList.push({ id: exam.id, name: exam.name || exam.id, type: 'subjective' });
              }
            });

            // Subtopics processing
            const subtopics = Array.isArray(top.subtopics) ? top.subtopics : [];
            subtopics.forEach((sub: any) => {
              if (!sub || typeof sub !== 'object') return;
              const subNumStr = String(sub.number ?? '').trim();
              const subCode = sub.subtopicCode || `${canonicalTopicPrefix}-${chapNumStr}-${subNumStr}`;
              const cleanSubCode = String(subCode).trim();

              const subtopicKey = `${chapNumStr}_${subNumStr}`;
              const subQStats = qCounts[cleanSubCode] || qCounts[subtopicKey] || { obj: 0, subj: 0 };
              
              sub.objectiveCount = subQStats.obj;
              sub.subjectiveCount = subQStats.subj;

              // Count tests for subtopic
              let subTests = 0;
              const subTestsList: any[] = [];
              examsList.forEach(exam => {
                const topicCodes = Array.isArray(exam.topicCodes) ? exam.topicCodes : [];
                if (matchTopicCode(topicCodes, cleanSubCode, subNumStr, chapNumStr)) {
                  subTests++;
                  subTestsList.push({ id: exam.id, name: exam.name || exam.examCode || exam.id, type: 'objective' });
                }
              });
              subjectiveExamsList.forEach(exam => {
                const topicCodes = Array.isArray(exam.topicCodes) ? exam.topicCodes : [];
                if (matchTopicCode(topicCodes, cleanSubCode, subNumStr, chapNumStr)) {
                  subTests++;
                  subTestsList.push({ id: exam.id, name: exam.name || exam.id, type: 'subjective' });
                }
              });

              sub.testsCount = subTests;
              sub.tests = subTestsList;
              allTestsCountsUnderChapter.push(subTests);

              // Add subtopic counts to topic counts
              topObj += sub.objectiveCount;
              topSubj += sub.subjectiveCount;
            });

            top.objectiveCount = topObj;
            top.subjectiveCount = topSubj;
            
            // Topic tests count rule: must equal highest subtopic count if subtopics exist
            top.testsCount = subtopics.length > 0 
              ? Math.max(0, ...subtopics.map((s: any) => s.testsCount || 0))
              : directTopicTests;
            
            // Topic tests list: if subtopics exist, aggregate their unique tests, else use direct tests
            if (subtopics.length > 0) {
              const accumTests: any[] = [];
              subtopics.forEach((s: any) => {
                if (Array.isArray(s.tests)) accumTests.push(...s.tests);
              });
              top.tests = getUniqueTests(accumTests);
            } else {
              top.tests = directTopicTestsList;
            }
            
            allTestsCountsUnderChapter.push(top.testsCount);

            // Add topic counts to chapter counts
            chObj += topObj;
            chSubj += topSubj;
          });

          chap.objectiveCount = chObj;
          chap.subjectiveCount = chSubj;
          
          // Chapter tests list: union of all child topic tests
          const chapAccumTests: any[] = [];
          topics.forEach((t: any) => {
            if (Array.isArray(t.tests)) chapAccumTests.push(...t.tests);
          });
          chap.tests = getUniqueTests(chapAccumTests);
          
          // Chapter tests count rule: must equal the highest test topic or subtopic count.
          chap.testsCount = allTestsCountsUnderChapter.length > 0 
            ? Math.max(0, ...allTestsCountsUnderChapter) 
            : 0;
        });
      } catch (loopErr) {
        console.warn('Syllabus chapter aggregation loop error bypassed:', loopErr);
      }

      const responseData = { 
        id: docSnap.id, 
        ...subjectData,
        chapters
      };

      setInCache(cacheKey, responseData, 60000); // 60s cache

      return NextResponse.json(responseData, {
        headers: {
          'Cache-Control': 'private, max-age=30, stale-while-revalidate=60'
        }
      });
    }

    // Return list of all subjects (cached in memory to reduce serverless CPU usage)
    const subjects = await getCachedSyllabusList();

    return NextResponse.json(subjects, {
      headers: {
        'Cache-Control': 'public, s-maxage=60, stale-while-revalidate=300'
      }
    });

  } catch (error: any) {
    console.error('API load syllabus subjects error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

async function syncSyllabusConfigTree() {
  try {
    invalidateCache('syllabus');
    invalidateCache('config');

    const syllabusSnap = await adminDb.collection('syllabus').get();
    const subjectsMap: Record<string, Record<string, Record<string, { docId: string }>>> = {};
    const boardCodes: Record<string, string> = {
      'Maharashtra Board': 'MH',
      'CBSE': 'CBSE',
      'ICSE': 'ICSE'
    };
    const subjectCodes: Record<string, string> = {};

    syllabusSnap.docs.forEach(doc => {
      const data = doc.data();
      const board = getCanonicalBoardName(data.board);
      const cls = getCanonicalClass(data.class);
      const subject = data.subject;
      const bCode = getCanonicalBoardCode(data.boardCode || board);
      const subjectCode = data.subjectCode || getCanonicalSubjectCode(bCode, cls, subject);

      if (board && subject) {
        boardCodes[board] = bCode;
        if (subjectCode) {
          subjectCodes[subject] = subjectCode;
        }
        if (!subjectsMap[board]) subjectsMap[board] = {};
        if (!subjectsMap[board][cls]) subjectsMap[board][cls] = {};
        subjectsMap[board][cls][subject] = { docId: doc.id };
      }
    });

    await Promise.all([
      adminDb.collection('config').doc('syllabusSubjects').set({
        subjects: subjectsMap,
        version: 1,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      }, { merge: true }),
      adminDb.collection('config').doc('boardCodes').set(boardCodes, { merge: true }),
      adminDb.collection('config').doc('subjectCodes').set(subjectCodes, { merge: true })
    ]);
  } catch (err) {
    console.warn('Failed to sync syllabus config tree:', err);
  }
}

// 2. POST - Save/edit a syllabus subject document
export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { docId, board, classNum, subjectName, chapters } = body;

    if (!docId || !board || !classNum || !subjectName) {
      return NextResponse.json({ message: 'Missing parameters (docId, board, classNum, subjectName).' }, { status: 400 });
    }

    const finalBoard = getCanonicalBoardName(board);
    const bCode = getCanonicalBoardCode(board);
    const cleanClass = getCanonicalClass(classNum);
    const subjectCode = body.subjectCode || getCanonicalSubjectCode(bCode, cleanClass, subjectName);

    // Check existing to carry forward chapters if empty/unset
    const existingSnap = await adminDb.collection('syllabus').doc(docId).get();
    const existingData = existingSnap.exists ? existingSnap.data()! : {};

    const subjectData = {
      board: finalBoard,
      boardCode: bCode,
      class: cleanClass,
      subject: subjectName.trim(),
      subjectCode,
      chapters: Array.isArray(chapters) ? chapters : (existingData.chapters || []),
      updatedAt: new Date()
    };

    await adminDb.collection('syllabus').doc(docId).set(subjectData, { merge: true });
    await syncSyllabusConfigTree();

    return NextResponse.json({ success: true, message: 'Subject saved successfully.' });

  } catch (error: any) {
    console.error('API save syllabus subject error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 3. DELETE - Delete a subject syllabus document & clean up unused questions
export async function DELETE(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const subjectId = searchParams.get('subjectId') || '';

    if (!subjectId) {
      return NextResponse.json({ message: 'Missing parameters (subjectId).' }, { status: 400 });
    }

    const subjectRef = adminDb.collection('syllabus').doc(subjectId);
    const subjectSnap = await subjectRef.get();
    if (!subjectSnap.exists) {
      return NextResponse.json({ message: 'Subject not found.' }, { status: 404 });
    }
    const subjectData = subjectSnap.data()!;

    // 1. Delete the syllabus subject document
    await subjectRef.delete();
    await syncSyllabusConfigTree();

    // 2. Cascade delete unused questions matching board/class/subject
    let questionsDeleted = 0;
    let questionsSkippedUsed = 0;

    if (subjectData.board && subjectData.class && subjectData.subject) {
      const questionsSnap = await adminDb.collection('questions')
        .where('board', '==', subjectData.board)
        .where('class', '==', subjectData.class)
        .where('subject', '==', subjectData.subject)
        .get();

      const candidates = questionsSnap.docs.map(doc => ({ id: doc.id, ref: doc.ref, ...doc.data() as any }));
      const unused = candidates.filter(q => !q.timesUsed);
      questionsSkippedUsed = candidates.length - unused.length;

      if (unused.length > 0) {
        // Run batch deletes (max 450 writes per batch)
        for (let i = 0; i < unused.length; i += 450) {
          const chunk = unused.slice(i, i + 450);
          const batch = adminDb.batch();
          chunk.forEach(q => batch.delete(q.ref));
          await batch.commit();
          questionsDeleted += chunk.length;
        }
      }
    }

    return NextResponse.json({ 
      success: true, 
      questionsDeleted, 
      questionsSkippedUsed 
    });

  } catch (error: any) {
    console.error('API delete syllabus subject error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 4. PUT - Save syllabus hierarchy (chapters list) or edit subject metadata
export async function PUT(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const docId = body.id || body.docId;

    if (!docId) {
      return NextResponse.json({ message: 'Missing subject ID parameter (id or docId).' }, { status: 400 });
    }

    // Case 1: Editing subject metadata (board, classNum, subjectName, subjectCode)
    if (body.board || body.classNum || body.subjectName || body.subjectCode) {
      const { board, classNum, subjectName } = body;
      const updateData: Record<string, any> = { updatedAt: new Date() };

      if (board) {
        updateData.board = getCanonicalBoardName(board);
        updateData.boardCode = getCanonicalBoardCode(board);
      }
      if (classNum) {
        updateData.class = getCanonicalClass(classNum);
      }
      if (subjectName) {
        updateData.subject = subjectName.trim();
      }
      if (body.subjectCode) {
        updateData.subjectCode = body.subjectCode;
      } else if (updateData.boardCode && updateData.class && updateData.subject) {
        updateData.subjectCode = getCanonicalSubjectCode(updateData.boardCode, updateData.class, updateData.subject);
      }

      if (Array.isArray(body.chapters)) {
        updateData.chapters = body.chapters;
      }

      await adminDb.collection('syllabus').doc(docId).set(updateData, { merge: true });
      await syncSyllabusConfigTree();

      return NextResponse.json({ success: true, message: 'Subject details updated successfully.' });
    }

    // Case 2: Hierarchy / chapters reorder or update
    if (Array.isArray(body.chapters)) {
      await adminDb.collection('syllabus').doc(docId).update({
        chapters: body.chapters,
        updatedAt: new Date()
      });
      await syncSyllabusConfigTree();

      return NextResponse.json({ success: true, message: 'Syllabus hierarchy updated successfully.' });
    }

    return NextResponse.json({ message: 'Missing parameters (chapters or subject details).' }, { status: 400 });

  } catch (error: any) {
    console.error('API update syllabus error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

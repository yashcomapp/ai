import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole, verifyAnyRole } from '@/lib/auth';
import { getCachedSyllabusList, invalidateCache } from '@/lib/firebase/cache';
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

        const questionsSnap = await adminDb.collection('questions')
          .where('class', 'in', [String(classVal), Number(classVal)].filter(v => v !== ''))
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
        const classVal = subjectData.class !== undefined ? subjectData.class : '';
        const [examsSnap, subjectiveExamsSnap] = await Promise.all([
          adminDb.collection('exams')
            .where('class', 'in', [String(classVal), Number(classVal)].filter(v => v !== ''))
            .get(),
          adminDb.collection('subjectiveExams')
            .where('class', 'in', [String(classVal), Number(classVal)].filter(v => v !== ''))
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

      return NextResponse.json({ 
        id: docSnap.id, 
        ...subjectData,
        chapters
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

    // Resolve subjectCode
    const subjectCodesSnap = await adminDb.collection('config').doc('subjectCodes').get();
    const subjectCodes = subjectCodesSnap.exists ? subjectCodesSnap.data()! : {};
    const subjectCode = subjectCodes[subjectName] || subjectName.substring(0, 4).toUpperCase();

    // Check existing to carry forward chapters if empty/unset
    const existingSnap = await adminDb.collection('syllabus').doc(docId).get();
    const existingData = existingSnap.exists ? existingSnap.data()! : {};

    const subjectData = {
      board: board.trim(),
      class: classNum.trim(),
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

// 4. PUT - Save syllabus hierarchy (chapters list) for a subject
export async function PUT(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { id, chapters } = body;

    if (!id || !Array.isArray(chapters)) {
      return NextResponse.json({ message: 'Missing parameters (id, chapters).' }, { status: 400 });
    }

    await adminDb.collection('syllabus').doc(id).update({
      chapters,
      updatedAt: new Date()
    });
    await syncSyllabusConfigTree();

    return NextResponse.json({ success: true, message: 'Syllabus hierarchy updated successfully.' });

  } catch (error: any) {
    console.error('API update syllabus hierarchy error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

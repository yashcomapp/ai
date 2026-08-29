import { NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { NextRequest } from 'next/server';
import { shuffleArray } from '@/lib/questionTypes';
import { areQuestionsTooSimilar, filterDistinctCandidates } from '@/lib/questionSimilarity';
import { getDateKeyIST } from '@/lib/dateUtils';

export async function GET(request: NextRequest) {
  try {
    const adminUser = await verifyRole(request, 'admin');
    if (!adminUser) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });

    // Fetch all scheduled weekly suite daily tests & Saturday exams
    const snap = await adminDb.collection('subjectiveExams')
      .where('type', 'in', ['home_practice', 'classroom_test'])
      .get();

    const exams = snap.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));

    const assignSnap = await adminDb.collection('subjectiveAssignments').get();
    const assignments = assignSnap.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));

    return NextResponse.json({ exams, assignments });
  } catch (err: any) {
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

export async function POST(request: NextRequest) {
  try {
    const adminUser = await verifyRole(request, 'admin');
    if (!adminUser) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });

    const body = await request.json();
    const { action } = body;

    // Action A: Explicitly Assign an existing Weekly Suite to a Batch
    if (action === 'assign') {
      const { examIds, targetBatchId } = body;
      if (!examIds || !Array.isArray(examIds) || !targetBatchId) {
        return NextResponse.json({ error: 'Missing examIds array or targetBatchId' }, { status: 400 });
      }

      const batch = adminDb.batch();
      examIds.forEach((id: string) => {
        const ref = adminDb.collection('subjectiveExams').doc(id);
        batch.update(ref, { 
          batchId: targetBatchId,
          assignedAt: new Date().toISOString() 
        });
      });
      await batch.commit();
      // Trigger push notifications for all assigned exams asynchronously
      try {
        const { notifyNewExam } = await import('@/lib/notifications');
        const examRefs = examIds.map((id: string) => adminDb.collection('subjectiveExams').doc(id));
        const examSnaps = examRefs.length > 0 ? await adminDb.getAll(...examRefs) : [];

        for (const doc of examSnaps) {
          if (doc.exists) {
            const data = doc.data()!;
            const startAt = data.availableFrom 
              ? admin.firestore.Timestamp.fromDate(new Date(data.availableFrom)) 
              : admin.firestore.Timestamp.now();
            const endAt = data.availableUntil 
              ? admin.firestore.Timestamp.fromDate(new Date(data.availableUntil)) 
              : admin.firestore.Timestamp.now();
            await notifyNewExam(
              doc.id,
              'batch',
              [targetBatchId],
              [],
              startAt,
              endAt,
              'subjective'
            ).catch(err => console.error(`Failed to notify for assigned exam ${doc.id}:`, err));
          }
        }
      } catch (err) {
        console.error('Failed to trigger notifications during batch assignment:', err);
      }
      return NextResponse.json({ success: true, message: `Successfully assigned ${examIds.length} tests to batch.` });
    }

    // Action B: Compile Weekly Suite (Unassigned by default unless batchId specified)
    const { 
      board, 
      class: className, 
      subject, 
      chapterNumber, 
      chapterName, 
      weekStartDate, 
      batchId, 
      daysConfig,
      createdBy,
      subjects,
      selectedChaptersList
    } = body;

    let targetBoard = board || '';
    if (targetBoard === 'MSBSHSE' || targetBoard === 'MH' || targetBoard === 'State Board') {
      targetBoard = 'Maharashtra Board';
    }

    if (!targetBoard || !className || !daysConfig || !Array.isArray(daysConfig)) {
      return NextResponse.json({ error: 'Missing required parameters or daysConfig array' }, { status: 400 });
    }

    const generatedExamsForNotification: { id: string; start: string; end: string }[] = [];

    const boardCodesSnap = await adminDb.collection('config').doc('boardCodes').get();
    const subjectCodesSnap = await adminDb.collection('config').doc('subjectCodes').get();
    
    const boardCodes = boardCodesSnap.exists ? boardCodesSnap.data()! : {};
    const subjectCodes = subjectCodesSnap.exists ? subjectCodesSnap.data()! : {};
    const boardCode = boardCodes[targetBoard] || targetBoard.substring(0, 4).toUpperCase();

    const targetSubjects = subjects && Array.isArray(subjects) ? subjects : [subject].filter(Boolean);
    const targetChapters = selectedChaptersList && Array.isArray(selectedChaptersList) 
      ? selectedChaptersList 
      : [{ subject, chapterNumber, chapterName }].filter(c => c.subject && c.chapterNumber);

    if (targetSubjects.length === 0 || targetChapters.length === 0) {
      return NextResponse.json({ error: 'Missing subjects or chapters selection' }, { status: 400 });
    }

    // Date validation: prevent scheduling in the past
    const todayStr = new Date().toLocaleDateString('en-CA');
    const hasPastActiveDay = daysConfig.some((d: any) => d.active && d.date < todayStr);
    if (hasPastActiveDay) {
      return NextResponse.json({ error: 'Cannot schedule tests on past dates.' }, { status: 400 });
    }

    const isMath = targetSubjects.some((s: string) => /math|algebra|geometry|ganit/i.test(s));

    // Load syllabus subject configurations to resolve subtopic hierarchy matching (and build Math placeholders)
    const syllabusSnap = await adminDb.collection('syllabus')
      .where('board', '==', targetBoard)
      .where('class', '==', className)
      .get();

    // 1. Always load questions for selected subjects/chapters from Question Bank first
    const questionsSnap = await adminDb.collection('questions')
      .where('board', '==', targetBoard)
      .where('class', '==', className)
      .where('subject', 'in', targetSubjects)
      .get();

    let dbQuestions = questionsSnap.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    })) as any[];

    // Filter questions matching target chapters
    dbQuestions = dbQuestions.filter(q => {
      const qSubj = q.subject || q.subjectName || '';
      const qCh = String(q.chapterNumber || q.topicNumber || '').trim();
      return targetChapters.some(tc => 
        String(tc.subject).toLowerCase().trim() === String(qSubj).toLowerCase().trim() && 
        String(tc.chapterNumber).trim() === qCh
      );
    });

    const dbSubjectiveQuestions = dbQuestions.filter(q => {
      const type = q.type || q.qtype || '';
      return type.includes('subjective') || type.includes('numerical');
    });

    let allQuestions: any[] = [];

    if (isMath && dbSubjectiveQuestions.length === 0) {
      // Mathematics fallback: dynamic textbook-reference placeholder pool generation
      targetChapters.forEach(tc => {
        const matchingSyllabusDoc = syllabusSnap.docs.find(doc => {
          const sName = String(doc.data().subject || doc.data().subjectName || doc.id).toLowerCase();
          return sName.includes(tc.subject.toLowerCase()) || tc.subject.toLowerCase().includes(sName);
        });

        if (!matchingSyllabusDoc) return;
        const data = matchingSyllabusDoc.data();
        const chapters = data.chapters || [];
        const ch = chapters.find((c: any) => String(c.number || c.chapterNumber).trim() === String(tc.chapterNumber).trim());
        if (!ch) return;

        const subjectCode = data.subjectCode || tc.subject.substring(0, 4).toUpperCase();
        const chNum = String(ch.number || ch.chapterNumber);
        const chName = ch.name || ch.chapterName || tc.chapterName;

        // Traverse topics to collect textbookSets and subtopics
        const topics = ch.topics || [];
        topics.forEach((topic: any) => {
          let sets = topic.textbookSets || [];
          if (!Array.isArray(sets) || sets.length === 0) {
            // Fallback: build default sets for each topic
            const topicNum = String(topic.number);
            sets = [
              { name: `Practice Set ${topicNum}`, type: 'practice_set', questionCount: 8 },
              { name: `Chapter ${chNum} Solved Examples (Topic ${topicNum})`, type: 'solved_examples', questionCount: 4 }
            ];
          }

          // A. Generate Practice Set / Solved Examples placeholders (marked isTheorem: false)
          sets.forEach((set: any) => {
            const setName = set.name || '';
            const qCount = Number(set.questionCount) || 8;
            const setType = set.type || 'practice_set';
            const cleanSetName = setName.replace(/\s+/g, '');

            for (let i = 1; i <= qCount; i++) {
              allQuestions.push({
                id: `placeholder-${subjectCode}-${chNum}-${cleanSetName}-Q${i}`,
                text: `Solve ${setName}: Q${i}`,
                textbookPracticeSet: `${setName}: Q${i}`,
                marks: 2,
                type: 'numerical_short',
                isTheorem: false,
                isSolvedExample: setType === 'solved_examples',
                solution: 'Refer to the prescribed textbook for the complete step-by-step solution.',
                keywords: [],
                board: targetBoard,
                classNum: className,
                subject: tc.subject,
                subjectName: tc.subject,
                chapterNumber: chNum,
                chapterName: chName,
                topic: topic.name || '',
                topicName: topic.name || ''
              });
            }
          });

          // B. Generate dedicated Theorem placeholders from subtopics that contain theorem names
          const subtopics = topic.subtopics || [];
          subtopics.forEach((sub: any) => {
            const subName = sub.name || '';
            const isTh = /theorem|proof|BPT|Pythagoras|Appollonius|angle\s+bisector|parallel\s+lines|cyclic\s+quadrilateral|inscribed\s+angle/i.test(subName);
            if (isTh) {
              const cleanSubName = subName.replace(/\s+/g, '');
              allQuestions.push({
                id: `placeholder-${subjectCode}-${chNum}-Theorem-${cleanSubName}`,
                text: `Prove the theorem: ${subName}`,
                textbookPracticeSet: `Theorem: ${subName}`,
                marks: 4,
                type: 'numerical_long',
                isTheorem: true,
                isSolvedExample: false,
                solution: 'Refer to the prescribed textbook for the complete proof.',
                keywords: [],
                board: targetBoard,
                classNum: className,
                subject: tc.subject,
                subjectName: tc.subject,
                chapterNumber: chNum,
                chapterName: chName,
                topic: topic.name || '',
                topicName: topic.name || ''
              });
            }
          });
        });

        // C. Also add chapter-level exercises (like Problem Sets)
        const chapExercises = ch.chapterExercises || [];
        chapExercises.forEach((set: any) => {
          const setName = set.name || '';
          const qCount = Number(set.questionCount) || 8;
          const cleanSetName = setName.replace(/\s+/g, '');

          for (let i = 1; i <= qCount; i++) {
            allQuestions.push({
              id: `placeholder-${subjectCode}-${chNum}-${cleanSetName}-Q${i}`,
              text: `Solve ${setName}: Q${i}`,
              textbookProblemSet: `${setName}: Q${i}`,
              marks: 2,
              type: 'numerical_short',
              isTheorem: false,
              isSolvedExample: false,
              solution: 'Refer to the prescribed textbook for the complete step-by-step solution.',
              keywords: [],
              board: targetBoard,
              classNum: className,
              subject: tc.subject,
              subjectName: tc.subject,
              chapterNumber: chNum,
              chapterName: chName,
              topic: chName,
              topicName: chName
            });
          }
        });
      });
      console.log(`[Weekly Suite] Dynamically generated ${allQuestions.length} placeholder questions for Mathematics (subject: ${targetSubjects.join(', ')}).`);
    } else {
      allQuestions = dbSubjectiveQuestions;
    }

    // Map normalized topic name -> { number: string, parentNumber: string }
    const topicLookup: Record<string, { number: string; parentNumber: string }> = {};
    const cleanString = (s: string) => String(s || '').toLowerCase().replace(/[^a-z0-9]/g, '').trim();

    syllabusSnap.docs.forEach(doc => {
      const data = doc.data();
      const chapters = data.chapters || [];
      chapters.forEach((ch: any) => {
        const chNum = String(ch.number || ch.chapterNumber || '');
        const flatten = (items: any[], parentNum: string) => {
          items.forEach((item: any, idx: number) => {
            const name = String(typeof item === 'string' ? item : (item.name || item.topicName || ''));
            const num = String(item.number || `${parentNum}.${idx + 1}`);
            if (name) {
              topicLookup[cleanString(name)] = { number: num, parentNumber: parentNum };
            }
            if (item && Array.isArray(item.subtopics)) {
              flatten(item.subtopics, num);
            }
          });
        };
        flatten(ch.topics || [], chNum);
      });
    });

    const isMatchTopic = (q: any, top: string): boolean => {
      const qTopicName = String(q.topic || q.topicName || '').toLowerCase();
      const topLower = String(top).toLowerCase();

      const cleanTop = cleanString(top);
      const cleanQTopic = cleanString(qTopicName);

      if (cleanQTopic === cleanTop) return true;

      const topInfo = topicLookup[cleanTop];
      const qTopicNum = String(q.topicNumber || '').trim();

      if (topInfo && qTopicNum) {
        const targetPrefix = topInfo.number;
        if (qTopicNum === targetPrefix || qTopicNum.startsWith(targetPrefix + '.')) {
          return true;
        }
      }

      const qTopicCode = (() => {
        const code = q.questionCode || q.id || '';
        if (!code) return '';
        const parts = code.split('-');
        return parts.length > 2 ? parts.slice(0, parts.length - 2).join('-').toLowerCase() : code.toLowerCase();
      })();

      return qTopicCode.includes(topLower) || qTopicName.includes(topLower);
    };

    if (allQuestions.length === 0) {
      return NextResponse.json({ error: `No questions found for the selected subjects and chapters in the Question Bank.` }, { status: 400 });
    }

    const compiledDailyTests: any[] = [];
    const allAssignedQuestionIds: string[] = [];
    const usedQuestionIdsInWeek = new Set<string>();

    // Shuffle helper
    const shuffle = (arr: any[]) => shuffleArray(arr);

    // Math Type detection
    let detectedMathType = body.mathType;
    if (!detectedMathType) {
      const isAlgebra = targetSubjects.some((s: string) => {
        const sLower = s.toLowerCase();
        return sLower.includes('algebra') || sLower.includes('part 1') || subjectCodes[s] === 'MTH1';
      });
      const isGeometry = targetSubjects.some((s: string) => {
        const sLower = s.toLowerCase();
        return sLower.includes('geometry') || sLower.includes('part 2') || subjectCodes[s] === 'MTH2';
      });
      if (isAlgebra) {
        detectedMathType = 'algebra';
      } else if (isGeometry) {
        detectedMathType = 'geometry';
      }
    }

    const activeWeekdays = daysConfig.filter(day => day.active && !day.isSaturday);
    const activeDaysCount = activeWeekdays.length;

    // Distribute Geometry theorems
    let theoremChunks: any[][] = Array.from({ length: activeDaysCount }, () => []);
    let allTheorems: any[] = [];
    let nonTheorems: any[] = [];
    if (detectedMathType === 'geometry') {
      allTheorems = shuffle(allQuestions.filter(q => !!q.isTheorem));
      nonTheorems = allQuestions.filter(q => !q.isTheorem);
      if (allTheorems.length > 0) {
        allTheorems.forEach((theorem, index) => {
          const chunkIndex = index % activeDaysCount;
          theoremChunks[chunkIndex].push(theorem);
        });
      }
    }

    // Pre-allocate sequence numbers
    const weekdayCount = daysConfig.filter(d => !d.isSaturday && d.active).length;
    const saturdayCount = daysConfig.filter(d => d.isSaturday && d.active).length;
    const totalNeeded = weekdayCount + saturdayCount;

    const counterId = `class-${className}`;
    const counterRef = adminDb.collection('examCounters').doc(counterId);

    let initialSeq = 1;
    const counterSnap = await counterRef.get();
    if (!counterSnap.exists) {
      const [objectiveQuery, subjectiveQuery] = await Promise.all([
        adminDb.collection('exams').where('class', '==', className).get(),
        adminDb.collection('subjectiveExams').where('class', '==', className).get()
      ]);
      initialSeq = objectiveQuery.size + subjectiveQuery.size + 1;
    }

    const startSeq = await adminDb.runTransaction(async (tx) => {
      const snap = await tx.get(counterRef);
      const seqNow = (snap.exists && snap.data()?.nextSequence) || initialSeq;
      tx.set(counterRef, { nextSequence: seqNow + totalNeeded }, { merge: true });
      return seqNow;
    });

    const writeBatch = adminDb.batch();
    let activeDayIndex = 0;

    // 2. Build Daily Home Practice for each active day (skipping Saturdays)
    for (const day of daysConfig) {
      if (!day.active || day.isSaturday) continue;

      const dayDate = day.date; // YYYY-MM-DD
      const assignedTopics: string[] = day.topics || [];

      // Filter questions matching day's topics if available (topic code or topic name)
      const isScience = targetSubjects.some((s: string) => /science/i.test(s));
      const isMath = targetSubjects.some((s: string) => /math|algebra|geometry|ganit/i.test(s));
      const savedTopics = assignedTopics.map((t: any) => String(t).trim().replace(/\s*\(\d+\s*Qs\)/i, ''));

      let learningForDay: any[] = [];
      let selectedForDay: any[] = [];

      if (isScience) {
        // Science: STRICT topic isolation per assigned day topics
        const dayCandidates: any[] = [];
        savedTopics.forEach(top => {
          const topQs = allQuestions.filter(q => isMatchTopic(q, top));

          const qs2m = topQs.filter(q => (Number(q.marks) === 2 || ['subjective_short', 'numerical_short', 'subjective_reason', 'subjective_notes'].includes(q.type)) && !['subjective_define', 'subjective_laws'].includes(q.type) && Number(q.marks) !== 1);
          const qs4m = topQs.filter(q => (Number(q.marks) === 4 || ['subjective_long', 'numerical_long'].includes(q.type)) && !['subjective_define', 'subjective_laws'].includes(q.type) && Number(q.marks) !== 1);

          // Exclude questions used on previous days of the week
          const fresh2m = qs2m.filter(q => !usedQuestionIdsInWeek.has(q.id));
          const fresh4m = qs4m.filter(q => !usedQuestionIdsInWeek.has(q.id));

          // Pick up to 3 of 2m and 1 of 4m (fallback to any matching if pool exhausted)
          const pool2m = fresh2m.length > 0 ? fresh2m : qs2m;
          const pool4m = fresh4m.length > 0 ? fresh4m : qs4m;

          dayCandidates.push(...shuffle(pool2m).slice(0, 3));
          dayCandidates.push(...shuffle(pool4m).slice(0, 1));
        });

        // Filter distinct to eliminate near-duplicates within the day
        learningForDay = filterDistinctCandidates(dayCandidates, []);

        // Daily online test: sample exactly 3 distinct questions (2 of 2m, 1 of 4m)
        const testCandidates2m = learningForDay.filter(q => Number(q.marks) === 2 || ['subjective_short', 'numerical_short', 'subjective_reason', 'subjective_notes'].includes(q.type));
        const testCandidates4m = learningForDay.filter(q => Number(q.marks) === 4 || ['subjective_long', 'numerical_long'].includes(q.type));

        const distinct2m = filterDistinctCandidates(shuffle(testCandidates2m), []);
        const picked2mTest = distinct2m.slice(0, 2);
        const distinct4m = filterDistinctCandidates(shuffle(testCandidates4m), picked2mTest);
        const picked4mTest = distinct4m.slice(0, 1);

        selectedForDay = [...picked2mTest, ...picked4mTest];

        if (selectedForDay.length < 3) {
          const testPickedIds = new Set(selectedForDay.map(q => q.id));
          const remainingDistinct = filterDistinctCandidates(shuffle(learningForDay), selectedForDay);
          for (const q of remainingDistinct) {
            if (!testPickedIds.has(q.id)) {
              selectedForDay.push(q);
              testPickedIds.add(q.id);
              if (selectedForDay.length >= 3) break;
            }
          }
        }
      } else if (isMath) {
        // Math (Algebra/Geometry): exact practice set filtering and natural partition logic
        let candidateQs: any[] = [];

        savedTopics.forEach(top => {
          const topStr = String(top).trim();
          const partMatch = topStr.match(/^(.+?)\s*\(?Part\s*(\d+)(?:\s*of\s*(\d+))?\)?$/i);
          
          let baseTopic = topStr;
          let partNum = 1;
          let totalParts = 0;
          let isPart = false;
          
          if (partMatch) {
            baseTopic = partMatch[1].trim();
            partNum = parseInt(partMatch[2]);
            totalParts = partMatch[3] ? parseInt(partMatch[3]) : 0;
            isPart = true;
          }
          
          const matchedQs = allQuestions.filter(q => {
            const pSet = String(q.textbookPracticeSet || '').toLowerCase();
            const pbSet = String(q.textbookProblemSet || '').toLowerCase();
            const baseTopicLower = baseTopic.toLowerCase();
            return isMatchTopic(q, baseTopic) || pSet.includes(baseTopicLower) || pbSet.includes(baseTopicLower);
          });
          
          if (isPart) {
            if (totalParts === 0) {
              let maxPart = 1;
              daysConfig.forEach(d => {
                if (d.active && !d.isSaturday && d.topics) {
                  d.topics.forEach((t: any) => {
                    const m = String(t).match(/^(.+?)\s*\(?Part\s*(\d+)(?:\s*of\s*(\d+))?\)?$/i);
                    if (m && m[1].trim().toLowerCase() === baseTopic.toLowerCase()) {
                      const pVal = parseInt(m[2]);
                      if (pVal > maxPart) maxPart = pVal;
                    }
                  });
                }
              });
              totalParts = maxPart;
            }
            
            // Sort in natural textbook order (by sequence suffix)
            matchedQs.sort((a, b) => {
              const codeA = a.questionCode || a.id || '';
              const codeB = b.questionCode || b.id || '';
              return codeA.localeCompare(codeB);
            });
            
            const start = Math.floor(((partNum - 1) / totalParts) * matchedQs.length);
            const end = Math.floor((partNum / totalParts) * matchedQs.length);
            candidateQs = [...candidateQs, ...matchedQs.slice(start, end)];
          } else {
            candidateQs = [...candidateQs, ...matchedQs];
          }
        });

        if (candidateQs.length === 0) {
          candidateQs = allQuestions.filter(q => savedTopics.some(top => isMatchTopic(q, top)));
          if (candidateQs.length === 0) candidateQs = [...allQuestions];
        }

        if (detectedMathType === 'geometry') {
          // Geometry: dedicated theorems per day
          let dayTheorems = [...(theoremChunks[activeDayIndex] || [])];
          if (dayTheorems.length < 2 && allTheorems.length > 0) {
            const dayThIds = new Set(dayTheorems.map(q => q.id));
            const extraTheorems = allTheorems.filter(q => !dayThIds.has(q.id) && !usedQuestionIdsInWeek.has(q.id));
            dayTheorems = [...dayTheorems, ...shuffle(extraTheorems).slice(0, 2 - dayTheorems.length)];
          }

          const dayTheoremsIds = new Set(dayTheorems.map(q => q.id));
          let candidateNonTheorems = candidateQs.filter(q => !q.isTheorem && !dayTheoremsIds.has(q.id));
          
          learningForDay = filterDistinctCandidates([...dayTheorems, ...candidateNonTheorems], []);
        } else {
          // Algebra
          learningForDay = filterDistinctCandidates(candidateQs, []);
        }

        // Daily online test selection (3 distinct questions):
        if (detectedMathType === 'geometry') {
          const dayTheorems = learningForDay.filter(q => !!q.isTheorem);
          const dayNonTheorems = learningForDay.filter(q => !q.isTheorem);

          if (dayTheorems.length > 0 && dayNonTheorems.length > 0) {
            const pickedTheorem = shuffle(dayTheorems)[0];
            const pickedNonTheorems = filterDistinctCandidates(shuffle(dayNonTheorems), [pickedTheorem]).slice(0, 2);
            selectedForDay = [pickedTheorem, ...pickedNonTheorems];
          } else {
            selectedForDay = filterDistinctCandidates(shuffle(dayNonTheorems), []).slice(0, 3);
          }

          if (selectedForDay.length < 3) {
            const pickedIds = new Set(selectedForDay.map(q => q.id));
            for (const q of filterDistinctCandidates(shuffle(learningForDay), selectedForDay)) {
              if (!pickedIds.has(q.id)) {
                selectedForDay.push(q);
                pickedIds.add(q.id);
                if (selectedForDay.length >= 3) break;
              }
            }
          }
        } else {
          // Algebra
          selectedForDay = filterDistinctCandidates(shuffle(learningForDay), []).slice(0, 3);
          if (selectedForDay.length < 3) {
            const pickedIds = new Set(selectedForDay.map(q => q.id));
            for (const q of filterDistinctCandidates(shuffle(learningForDay), selectedForDay)) {
              if (!pickedIds.has(q.id)) {
                selectedForDay.push(q);
                pickedIds.add(q.id);
                if (selectedForDay.length >= 3) break;
              }
            }
          }
        }
      } else {
        // Standard subjects
        let standardCandidateQs = allQuestions.filter(q => {
          return savedTopics.some(top => isMatchTopic(q, top));
        });

        if (standardCandidateQs.length === 0) {
          standardCandidateQs = [...allQuestions];
        }

        learningForDay = filterDistinctCandidates(standardCandidateQs, []);
        selectedForDay = filterDistinctCandidates(shuffle(learningForDay), []).slice(0, 3);
      }

      // Record assigned questions in weekly registry to prevent cross-day duplicate repetitions
      learningForDay.forEach(q => usedQuestionIdsInWeek.add(q.id));
      selectedForDay.forEach(q => usedQuestionIdsInWeek.add(q.id));

      const totalMarks = selectedForDay.reduce((sum, q) => sum + (Number(q.marks) || 2), 0);
      const qIds = selectedForDay.map(q => q.id);
      qIds.forEach(id => {
        if (!allAssignedQuestionIds.includes(id)) allAssignedQuestionIds.push(id);
      });

      const daySubjects = Array.from(new Set(selectedForDay.map(q => q.subject || q.subjectName).filter(Boolean)));
      const dayChapters = Array.from(new Set(selectedForDay.map(q => q.chapterNumber).filter(Boolean)));

      const firstSubj = daySubjects[0] || targetSubjects[0] || '';

      const nextSeq = startSeq + activeDayIndex;

      const seq3digit = String(nextSeq).padStart(3, '0');
      const subjectCode = subjectCodes[firstSubj] || firstSubj.substring(0, 4).toUpperCase();
      const chapterPart = dayChapters.join('_') || '1_1';
      const dateStr = dayDate.replace(/-/g, '');
      const examId = `${boardCode}-${className}-${subjectCode}-SUBJ-${chapterPart}-${dateStr}-${nextSeq}`;

      // Science and others: 8:30 PM - 10:30 PM IST (15:00:00.000Z - 17:00:00.000Z UTC)
      // Math: 5:00 AM - 7:00 AM IST (previous day 11:30 PM - 01:30 AM UTC)
      let availableFrom = `${dayDate}T15:00:00.000Z`;
      let availableUntil = `${dayDate}T17:00:00.000Z`;

      if (isMath) {
        const prevDate = getDateKeyIST(new Date(new Date(dayDate).getTime() - 24 * 60 * 60 * 1000));
        availableFrom = `${prevDate}T23:30:00.000Z`;
        availableUntil = `${dayDate}T01:30:00.000Z`;
      }

      const dayChapterNames = dayChapters.map(chNum => {
        const found = targetChapters.find(tc => String(tc.chapterNumber).trim() === String(chNum).trim());
        return found ? found.chapterName : '';
      }).filter(Boolean);

      const activeChapterLabel = dayChapterNames.length > 0 
        ? dayChapterNames.join(', ') 
        : chapterName;

      const dayTopicNames = Array.from(new Set(selectedForDay.map(q => q.topic || q.topicName).filter(Boolean)));
      const activeTopicLabel = dayTopicNames.length > 0 ? dayTopicNames.join(', ') : 'General Practice';

      const homeExamData = {
        examId,
        type: 'home_practice',
        name: `${seq3digit}-${className}-${subjectCode}-${chapterPart}-Subjective-${dateStr}`,
        board: targetBoard,
        class: className,
        subject: daySubjects.length > 0 ? daySubjects.join(', ') : targetSubjects.join(', '),
        subjects: daySubjects.length > 0 ? daySubjects : targetSubjects,
        chapterNumber: dayChapters.length > 0 ? dayChapters.join(', ') : targetChapters.map(c => c.chapterNumber).join(', '),
        chapterName: activeChapterLabel,
        topics: savedTopics,
        batchId: batchId || null, // Unassigned by default unless teacher explicitly assigns
        scheduledDate: dayDate,
        dayName: day.dayName,
        availableFrom,
        availableUntil,
        totalQuestions: selectedForDay.length,
        totalMarks,
        totalTime: totalMarks * 2,
        questionIds: qIds,
        questions: selectedForDay,
        learningQuestions: learningForDay, // Save learning questions for the daily print PDF!
        status: 'active',
        createdBy: createdBy || 'admin',
        createdAt: new Date().toISOString()
      };

      writeBatch.set(adminDb.collection('subjectiveExams').doc(examId), homeExamData, { merge: true });

      if (batchId) {
        generatedExamsForNotification.push({
          id: examId,
          start: availableFrom,
          end: availableUntil
        });
      }

      compiledDailyTests.push({
        dayName: day.dayName,
        date: dayDate,
        active: true,
        examId,
        topics: savedTopics,
        totalQuestions: selectedForDay.length,
        totalMarks,
        questions: selectedForDay,
        learningQuestions: learningForDay // Also pass back to frontend so they compile correctly in PDF immediately
      });
      activeDayIndex++;
    }

    // 3. Auto-sample Saturday Classroom Tests for each active Saturday in the config
    const compiledSaturdayTests: any[] = [];
    const satDays = daysConfig.filter(d => d.isSaturday && d.active);

    // Fetch all existing classroom tests for this board, class, and subjects to determine Week Index W
    const existingExamsQuery = adminDb.collection('subjectiveExams')
      .where('type', '==', 'classroom_test')
      .where('board', '==', targetBoard)
      .where('class', '==', className)
      .where('subject', 'in', targetSubjects)
      .where('batchId', '==', null);
    
    const existingExamsSnap = await existingExamsQuery.get();
    const existingExams = existingExamsSnap.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    })) as any[];

    // Calculate Week Index W (number of existing tests + 1)
    const W = existingExams.length + 1;

    // Fetch all previously used question IDs for this batch/subjects to avoid repeats
    const batchFilterValues = batchId ? [batchId, null] : [null];
    const allPreviousExamsQuery = adminDb.collection('subjectiveExams')
      .where('board', '==', targetBoard)
      .where('class', '==', className)
      .where('subject', 'in', targetSubjects)
      .where('batchId', 'in', batchFilterValues);

    const previousExamsSnap = await allPreviousExamsQuery.get();
    const thisWeekDailyTestIds = new Set(compiledDailyTests.map(t => t.examId));
    const priorUsedQuestionIds = new Set<string>();
    previousExamsSnap.docs.forEach(doc => {
      if (thisWeekDailyTestIds.has(doc.id)) {
        return; // Skip current week's daily tests so we can reuse their questions for Saturday!
      }
      const qIds = doc.data().questionIds || [];
      qIds.forEach((id: string) => priorUsedQuestionIds.add(id));
    });

    // Fetch all unique chapter numbers in the Question Bank for target subjects to resolve prior chapters
    const allQsSnap = await adminDb.collection('questions')
      .where('board', '==', targetBoard)
      .where('class', '==', className)
      .where('subject', 'in', targetSubjects)
      .get();
    
    const questionsList = allQsSnap.docs.map(doc => ({ id: doc.id, ...doc.data() })) as any[];
    
    // For each target subject, we determine the previous chapters
    let previousChaptersQuestions: any[] = [];
    let hasPreviousChapters = false;
    
    targetChapters.forEach(tc => {
      const subjQs = questionsList.filter(q => String(q.subject || q.subjectName || '').toLowerCase().trim() === String(tc.subject).toLowerCase().trim());
      const uniqueChapters = Array.from(new Set(subjQs.map(q => String(q.chapterNumber || q.topicNumber || '').trim()).filter(Boolean)));
      
      uniqueChapters.sort((a, b) => {
        const numA = parseFloat(a);
        const numB = parseFloat(b);
        if (!isNaN(numA) && !isNaN(numB)) return numA - numB;
        return a.localeCompare(b);
      });
      
      const cleanChNum = String(tc.chapterNumber).trim();
      const currentChIdx = uniqueChapters.indexOf(cleanChNum);
      const prevChs = currentChIdx > 0 ? uniqueChapters.slice(0, currentChIdx) : [];
      
      if (prevChs.length > 0) {
        hasPreviousChapters = true;
        const prevQs = subjQs.filter((q: any) => {
          const qCh = String(q.chapterNumber || q.topicNumber || '').trim();
          if (W === 2 || W === 3) {
            const prevCh = uniqueChapters[currentChIdx - 1];
            return qCh === prevCh;
          } else {
            return prevChs.includes(qCh);
          }
        });
        previousChaptersQuestions = [...previousChaptersQuestions, ...prevQs];
      }
    });

    for (let satIdx = 0; satIdx < satDays.length; satIdx++) {
      const sat = satDays[satIdx];
      const satDate = sat.date;

      // Find weekdays in this week (preceding this Saturday and after previous Saturday)
      const prevSatDate = satIdx > 0 ? satDays[satIdx - 1].date : '';
      const thisWeekDailyTests = compiledDailyTests.filter(t => {
        if (prevSatDate) {
          return t.date < satDate && t.date > prevSatDate;
        }
        return t.date < satDate;
      });

      // 1. Used questions pool (questions actually assigned in weekdays)
      const usedDailyMap = new Map();
      thisWeekDailyTests.forEach(t => {
        if (t.questions && Array.isArray(t.questions)) {
          t.questions.forEach((q: any) => usedDailyMap.set(q.id, q));
        }
      });
      const usedDailyPool = Array.from(usedDailyMap.values());

      // 2. Unused questions pool (questions in PDF / learning pool but not used in daily practice)
      const unusedLearningMap = new Map();
      thisWeekDailyTests.forEach(t => {
        if (t.learningQuestions && Array.isArray(t.learningQuestions)) {
          t.learningQuestions.forEach((q: any) => {
            if (!usedDailyMap.has(q.id)) {
              unusedLearningMap.set(q.id, q);
            }
          });
        }
      });
      const unusedLearningPool = Array.from(unusedLearningMap.values());

      // Saturday Classroom Test length (N)
      const N = 8; // Default Saturday test is 8 questions

      // Splits: 70% from used daily questions (6 Qs), 30% from unused daily PDF questions (2 Qs)
      const N_used = Math.round(0.70 * N); // 6 questions
      const N_unused = N - N_used;          // 2 questions

      const satQuestions: any[] = [];
      const selectedIds = new Set<string>();

      const pickFrom = (pool: any[], count: number) => {
        const distinctPool = filterDistinctCandidates(shuffle(pool), satQuestions);
        let picked = 0;
        for (const q of distinctPool) {
          if (picked >= count) break;
          if (!selectedIds.has(q.id) && !areQuestionsTooSimilar(q, satQuestions)) {
            satQuestions.push(q);
            selectedIds.add(q.id);
            picked++;
          }
        }
        return picked;
      };

      // Select used questions
      pickFrom(usedDailyPool, N_used);

      // Select unused questions
      pickFrom(unusedLearningPool, N_unused);

      // Fallback: If we couldn't meet N_used or N_unused, pad from the other pool
      if (satQuestions.length < N) {
        const remaining = N - satQuestions.length;
        pickFrom(unusedLearningPool, remaining);
      }
      if (satQuestions.length < N) {
        const remaining = N - satQuestions.length;
        pickFrom(usedDailyPool, remaining);
      }
      // Ultimate fallback: pad from allQuestions matching the weekly topic keys
      if (satQuestions.length < N) {
        const remaining = N - satQuestions.length;
        
        // Find weekly topic keys
        const thisWeekTopicKeysForFallback = new Set<string>();
        thisWeekDailyTests.forEach(t => {
          if (t.topics && Array.isArray(t.topics)) {
            t.topics.forEach((tc: string) => thisWeekTopicKeysForFallback.add(String(tc).trim().toLowerCase()));
          }
          if (t.questions && Array.isArray(t.questions)) {
            t.questions.forEach((q: any) => {
              if (q.topicCode) thisWeekTopicKeysForFallback.add(String(q.topicCode).trim().toLowerCase());
              if (q.topic) thisWeekTopicKeysForFallback.add(String(q.topic).trim().toLowerCase());
              if (q.topicName) thisWeekTopicKeysForFallback.add(String(q.topicName).trim().toLowerCase());
            });
          }
        });

        const weeklyTopicQuestions = allQuestions.filter(q => {
          const code = q.topicCode ? String(q.topicCode).trim().toLowerCase() : '';
          const name = q.topic ? String(q.topic).trim().toLowerCase() : '';
          const topicName = q.topicName ? String(q.topicName).trim().toLowerCase() : '';
          return (code && thisWeekTopicKeysForFallback.has(code)) || 
                 (name && thisWeekTopicKeysForFallback.has(name)) || 
                 (topicName && thisWeekTopicKeysForFallback.has(topicName));
        });

        const fallbackPool = weeklyTopicQuestions.length > 0 ? weeklyTopicQuestions : allQuestions;
        pickFrom(shuffle(fallbackPool), remaining);
      }

      const satSubjects = Array.from(new Set(satQuestions.map(q => q.subject || q.subjectName).filter(Boolean)));
      const satChapters = Array.from(new Set(satQuestions.map(q => q.chapterNumber).filter(Boolean)));

      const firstSatSubj = satSubjects[0] || targetSubjects[0] || '';

      const nextSeqSat = startSeq + weekdayCount + satIdx;

      const seq3digitSat = String(nextSeqSat).padStart(3, '0');
      const subjectCodeSat = subjectCodes[firstSatSubj] || firstSatSubj.substring(0, 4).toUpperCase();
      const chapterPartSat = (satChapters.join('_') || '1_1') + '_M';
      const dateStrSat = satDate.replace(/-/g, '');
      const satExamId = `${boardCode}-${className}-${subjectCodeSat}-SUBJ-${chapterPartSat}-${dateStrSat}-${nextSeqSat}`;

      const satTotalMarks = satQuestions.reduce((sum, q) => sum + (Number(q.marks) || 2), 0);
      const satQIds = satQuestions.map(q => q.id);

      const satChapterNames = satChapters.map(chNum => {
        const found = targetChapters.find(tc => String(tc.chapterNumber).trim() === String(chNum).trim());
        return found ? found.chapterName : '';
      }).filter(Boolean);

      const satActiveChapterLabel = satChapterNames.length > 0 
        ? satChapterNames.join(', ') 
        : chapterName;

      const satTopicNames = Array.from(new Set(satQuestions.map(q => q.topic || q.topicName).filter(Boolean)));
      const satActiveTopicLabel = satTopicNames.length > 0 ? satTopicNames.join(', ') : 'General Revision';

      const satExamData = {
        examId: satExamId,
        type: 'classroom_test',
        name: `${seq3digitSat}-${className}-${subjectCodeSat}-${chapterPartSat}-Subjective-${dateStrSat}`,
        board: targetBoard,
        class: className,
        subject: satSubjects.length > 0 ? satSubjects.join(', ') : targetSubjects.join(', '),
        subjects: satSubjects.length > 0 ? satSubjects : targetSubjects,
        chapterNumber: satChapters.length > 0 ? satChapters.join(', ') : targetChapters.map(c => c.chapterNumber).join(', '),
        chapterName: satActiveChapterLabel,
        batchId: null,
        scheduledDate: satDate,
        sampledFromHomeExamIds: thisWeekDailyTests.map(t => t.examId),
        totalQuestions: satQuestions.length,
        totalMarks: satTotalMarks,
        totalTime: satTotalMarks * 2,
        questionIds: satQIds,
        questions: satQuestions,
        status: 'active',
        createdBy: createdBy || 'admin',
        createdAt: new Date().toISOString()
      };

      writeBatch.set(adminDb.collection('subjectiveExams').doc(satExamId), satExamData, { merge: true });

      compiledSaturdayTests.push({
        examId: satExamId,
        date: satDate,
        totalQuestions: satQuestions.length,
        totalMarks: satTotalMarks,
        questions: satQuestions
      });
    }

    await writeBatch.commit();

    // Trigger push notifications for all generated daily exams
    if (batchId && generatedExamsForNotification.length > 0) {
      try {
        const { notifyNewExam } = await import('@/lib/notifications');
        for (const item of generatedExamsForNotification) {
          const startTimestamp = admin.firestore.Timestamp.fromDate(new Date(item.start));
          const endTimestamp = admin.firestore.Timestamp.fromDate(new Date(item.end));
          await notifyNewExam(
            item.id,
            'batch',
            [batchId],
            [],
            startTimestamp,
            endTimestamp,
            'subjective'
          ).catch(err => console.error(`Failed to notify for compiled exam ${item.id}:`, err));
        }
      } catch (err) {
        console.error('Failed to trigger notifications during compilation:', err);
      }
    }

    return NextResponse.json({
      success: true,
      message: 'Weekly Subjective Suite compiled successfully.',
      chapterName,
      dailyTests: compiledDailyTests,
      saturdayTest: compiledSaturdayTests[0] || null, // Return the first one for backwards compatibility
      saturdayTests: compiledSaturdayTests // Return the full array
    });

  } catch (err: any) {
    console.error('Weekly suite generation error:', err);
    return NextResponse.json({ error: err.message || 'Weekly suite generation failed.' }, { status: 500 });
  }
}

// DELETE Handler to remove scheduled tests / suites
export async function DELETE(request: NextRequest) {
  try {
    const adminUser = await verifyRole(request, 'admin');
    if (!adminUser) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });

    const body = await request.json();
    const { examIds } = body;

    if (!examIds || !Array.isArray(examIds) || examIds.length === 0) {
      return NextResponse.json({ error: 'Missing examIds array to delete' }, { status: 400 });
    }

    const batch = adminDb.batch();
    examIds.forEach((id: string) => {
      const ref = adminDb.collection('subjectiveExams').doc(id);
      batch.delete(ref);
    });

    // Also delete corresponding subjectiveAssignments to prevent orphans
    const assignmentsSnap = await adminDb.collection('subjectiveAssignments')
      .where('examId', 'in', examIds)
      .get();
    assignmentsSnap.docs.forEach(doc => {
      batch.delete(doc.ref);
    });

    await batch.commit();

    return NextResponse.json({ success: true, message: `Successfully deleted ${examIds.length} scheduled test(s).` });
  } catch (err: any) {
    console.error('Delete scheduled tests error:', err);
    return NextResponse.json({ error: err.message || 'Delete failed.' }, { status: 500 });
  }
}

function satTotalTotalMarks(qs: any[]) {
  return qs.reduce((sum, q) => sum + (Number(q.marks) || 2), 0);
}

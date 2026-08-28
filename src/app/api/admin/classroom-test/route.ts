import { NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { NextRequest } from 'next/server';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { shuffleArray } from '@/lib/questionTypes';

export async function GET(request: NextRequest) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });

    const [bSnap, configSnap] = await Promise.all([
      adminDb.collection('batches').get(),
      adminDb.collection('config').doc('syllabusSubjects').get()
    ]);

    const batches = bSnap.docs.map(doc => ({ id: doc.id, name: doc.data().name || doc.id }));
    const syllabusSubjects = configSnap.exists ? (configSnap.data()?.subjects || {}) : {};

    return NextResponse.json({ success: true, batches, syllabusSubjects });
  } catch (err: any) {
    console.error(err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
export async function POST(request: Request) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    const body = await request.json();
    const { 
      testType, 
      board, 
      class: className, 
      subject, 
      chapterNumber, 
      chapterName, 
      weekNumber, 
      totalQuestions, 
      batchId, 
      createdBy,
      subjects,
      selectedChaptersList
    } = body;

    if (!board || !className || !batchId) {
      return NextResponse.json({ error: 'Missing required parameters' }, { status: 400 });
    }

    const targetSubjects = subjects && Array.isArray(subjects) ? subjects : [subject].filter(Boolean);
    const targetChapters = selectedChaptersList && Array.isArray(selectedChaptersList) 
      ? selectedChaptersList 
      : [{ subject, chapterNumber, chapterName }].filter(c => c.subject && c.chapterNumber);

    if (targetSubjects.length === 0 || targetChapters.length === 0) {
      return NextResponse.json({ error: 'Missing subjects or chapters selection' }, { status: 400 });
    }

    // 1. Fetch questions matching criteria
    const questionsSnap = await adminDb.collection('questions')
      .where('board', '==', board)
      .where('class', '==', className)
      .where('subject', 'in', targetSubjects)
      .get();

    let allQuestions = questionsSnap.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    })) as any[];

    // Filter by subject-chapter combinations
    allQuestions = allQuestions.filter(q => {
      const qSubj = q.subject || q.subjectName || '';
      const qCh = String(q.chapterNumber || q.topicNumber || '').trim();
      return targetChapters.some(tc => 
        String(tc.subject).toLowerCase().trim() === String(qSubj).toLowerCase().trim() && 
        String(tc.chapterNumber).trim() === qCh
      );
    });

    if (allQuestions.length === 0) {
      return NextResponse.json({ error: `No questions found matching criteria in the Question Bank.` }, { status: 400 });
    }

    // Spaced repetition simulation/selection: prioritize unused questions
    const unused = allQuestions.filter(q => !q.usedInClassroomTest);
    const used = allQuestions.filter(q => q.usedInClassroomTest);

    const selectedQuestions = [...shuffleArray(unused), ...shuffleArray(used)].slice(0, totalQuestions);
    const usedCount = selectedQuestions.filter(q => q.usedInClassroomTest).length;
    const newCount = selectedQuestions.length - usedCount;

    // 2. Build unique Exam ID
    const now = new Date();
    const dateStr = now.toISOString().slice(0, 10).replace(/-/g, '');
    const timeStr = now.toTimeString().slice(0, 8).replace(/:/g, '');
    const rand = Math.floor(100 + Math.random() * 900);
    const firstSubj = targetSubjects[0] || '';
    const firstChName = targetChapters.map(c => c.chapterName).join(', ');
    const firstChNum = targetChapters.map(c => c.chapterNumber).join(', ');

    const examId = `EXAM-${board.slice(0, 2).toUpperCase()}-${className}-${firstSubj.slice(0, 3).toUpperCase()}-${dateStr}-${timeStr}-${rand}`;

    const examName = `Classroom-${className}-${firstSubj.slice(0, 3).toUpperCase()}-${firstChName.slice(0, 20)}-${testType === 'weekly' ? 'W' + weekNumber : 'Ch'}-${dateStr}`;

    const totalMarks = selectedQuestions.reduce((sum, q) => sum + (q.marks || 4), 0);
    const questionIds = selectedQuestions.map(q => q.id);

    // Write to subjectiveExams
    const examData = {
      examId,
      name: examName,
      questionIds,
      board,
      class: className,
      subject: targetSubjects.join(', '),
      subjects: targetSubjects,
      chapter: firstChName,
      chapterNumber: firstChNum,
      totalMarks,
      questionCount: selectedQuestions.length,
      mode: 'classroom',
      totalTime: 90,
      examType: 'subjective',
      status: 'active',
      weekNumber: weekNumber || 2,
      testType,
      usedCount,
      newCount,
      generatedBy: 'classroom_test_generator',
      createdAt: new Date(),
      createdBy: createdBy || 'admin'
    };

    await adminDb.collection('subjectiveExams').doc(examId).set(examData);

    // 3. Write Assignment mapping to subjectiveAssignments
    const assignmentData = {
      examId,
      examType: 'subjective',
      examMode: 'classroom',
      targetType: 'batch',
      targetBatches: [batchId],
      targetStudents: [],
      openMode: 'scheduled',
      startAt: new Date(),
      endAt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000), // 7 days active
      classroomDuration: 90,
      weekNumber: weekNumber || 2,
      status: 'active',
      createdBy: createdBy || 'admin',
      createdAt: new Date(),
      updatedAt: new Date()
    };

    await adminDb.collection('subjectiveAssignments').add(assignmentData);

    // 4. Mark questions as used in classroom test
    const writeBatch = new ChunkedBatch(adminDb);
    selectedQuestions.forEach(q => {
      const qRef = adminDb.collection('questions').doc(q.id);
      writeBatch.update(qRef, {
        usedInClassroomTest: true,
        timesUsed: (q.timesUsed || 0) + 1,
        lastUsedDate: new Date()
      });
    });
    await writeBatch.commit();

    return NextResponse.json({
      success: true,
      examId,
      examName,
      totalQuestions: selectedQuestions.length,
      usedCount,
      newCount,
      testType,
      weekNumber
    });

  } catch (err: any) {
    console.error(err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

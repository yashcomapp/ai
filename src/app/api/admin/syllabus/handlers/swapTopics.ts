import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { subjectId, chapterNumber, sourceTopicIdx, targetTopicIdx } = body;

    if (
      !subjectId ||
      chapterNumber === undefined ||
      sourceTopicIdx === undefined ||
      targetTopicIdx === undefined
    ) {
      return NextResponse.json({ message: 'Missing parameters.' }, { status: 400 });
    }

    const subjectRef = adminDb.collection('syllabus').doc(subjectId);
    const subjectSnap = await subjectRef.get();
    if (!subjectSnap.exists) {
      return NextResponse.json({ message: 'Subject not found.' }, { status: 404 });
    }

    const subjectData = subjectSnap.data()!;
    const chapters = Array.isArray(subjectData.chapters) ? [...subjectData.chapters] : [];
    const chapterIdx = chapters.findIndex(c => String(c.number) === String(chapterNumber));

    if (chapterIdx === -1) {
      return NextResponse.json({ message: 'Chapter not found.' }, { status: 404 });
    }

    const chapter = { ...chapters[chapterIdx] };
    const topics = Array.isArray(chapter.topics) ? [...chapter.topics] : [];

    if (
      sourceTopicIdx < 0 ||
      sourceTopicIdx >= topics.length ||
      targetTopicIdx < 0 ||
      targetTopicIdx >= topics.length
    ) {
      return NextResponse.json({ message: 'Invalid topic indices.' }, { status: 400 });
    }

    const topicA = { ...topics[sourceTopicIdx] };
    const topicB = { ...topics[targetTopicIdx] };

    const oldCodeA = topicA.topicCode;
    const oldCodeB = topicB.topicCode;
    const oldNumA = topicA.number;
    const oldNumB = topicB.number;

    if (!oldCodeA || !oldCodeB) {
      return NextResponse.json({ message: 'Topic codes not found on documents.' }, { status: 400 });
    }

    // 1. Swap positions, numbers, and codes
    const newCodeA = oldCodeB; // A moves to B's old position
    const newCodeB = oldCodeA; // B moves to A's old position

    // Swap subtopic numbers and subtopicCodes internally
    if (Array.isArray(topicA.subtopics)) {
      topicA.subtopics = topicA.subtopics.map((sub: any) => {
        const newSubNumber = sub.number.replace(new RegExp(`^${oldNumA}`), oldNumB);
        const newSubCode = sub.subtopicCode
          ? sub.subtopicCode.replace(new RegExp(`-${oldNumA}-`), `-${oldNumB}-`).replace(new RegExp(`-${oldNumA}$`), `-${oldNumB}`)
          : sub.subtopicCode;
        return { ...sub, number: newSubNumber, subtopicCode: newSubCode };
      });
    }

    if (Array.isArray(topicB.subtopics)) {
      topicB.subtopics = topicB.subtopics.map((sub: any) => {
        const newSubNumber = sub.number.replace(new RegExp(`^${oldNumB}`), oldNumA);
        const newSubCode = sub.subtopicCode
          ? sub.subtopicCode.replace(new RegExp(`-${oldNumB}-`), `-${oldNumA}-`).replace(new RegExp(`-${oldNumB}$`), `-${oldNumA}`)
          : sub.subtopicCode;
        return { ...sub, number: newSubNumber, subtopicCode: newSubCode };
      });
    }

    // Update position properties
    topics[sourceTopicIdx] = {
      ...topicB,
      number: oldNumA,
      topicCode: newCodeB
    };

    topics[targetTopicIdx] = {
      ...topicA,
      number: oldNumB,
      topicCode: newCodeA
    };

    chapter.topics = topics;
    chapters[chapterIdx] = chapter;

    // 2. Fetch and swap questions
    const questionsASnap = await adminDb.collection('questions')
      .where('topicCode', '==', oldCodeA)
      .get();
    
    const questionsBSnap = await adminDb.collection('questions')
      .where('topicCode', '==', oldCodeB)
      .get();

    const questionsA = questionsASnap.docs;
    const questionsB = questionsBSnap.docs;

    const tempPlaceholderCode = `${oldCodeA}_TEMP_SWAP`;

    // Perform the operations in sequential batches to prevent collisions
    // Step A: Update A to temp
    if (questionsA.length > 0) {
      const batchA = adminDb.batch();
      questionsA.forEach(doc => {
        batchA.update(doc.ref, { topicCode: tempPlaceholderCode, updatedAt: new Date() });
      });
      await batchA.commit();
    }

    // Step B: Update B to A
    if (questionsB.length > 0) {
      const batchB = adminDb.batch();
      questionsB.forEach(doc => {
        batchB.update(doc.ref, { topicCode: newCodeB, updatedAt: new Date() }); // moves to sourceTopic (oldCodeA)
      });
      await batchB.commit();
    }

    // Step C: Update temp to B
    if (questionsA.length > 0) {
      const batchTemp = adminDb.batch();
      questionsA.forEach(doc => {
        batchTemp.update(doc.ref, { topicCode: newCodeA, updatedAt: new Date() }); // moves to targetTopic (oldCodeB)
      });
      await batchTemp.commit();
    }

    // 3. Save the modified syllabus document
    await subjectRef.update({
      chapters,
      updatedAt: new Date()
    });

    const totalMigrated = questionsA.length + questionsB.length;

    return NextResponse.json({
      success: true,
      message: 'Topics and associated questions swapped successfully.',
      migratedCount: totalMigrated
    });

  } catch (error: any) {
    console.error('API swap syllabus topics error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

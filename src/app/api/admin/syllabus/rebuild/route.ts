import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
export const dynamic = 'force-dynamic';

// Rebuild helper logic (adapted from syllabusIndexService.js)
async function runIndexRebuild() {
  const summary = { subjectsProcessed: 0, topicsIndexed: 0, staleRemoved: 0, errors: [] as string[] };
  const validCodes = new Set<string>();
  const syllabusSubjectsTree: any = {};

  const syllabusSnap = await adminDb.collection('syllabus').get();
  if (syllabusSnap.empty) {
    summary.errors.push('Syllabus collection is empty.');
    return summary;
  }

  // Load board codes and subject codes
  const boardCodesSnap = await adminDb.collection('config').doc('boardCodes').get();
  const subjectCodesSnap = await adminDb.collection('config').doc('subjectCodes').get();
  
  const boardCodes = boardCodesSnap.exists ? boardCodesSnap.data()! : {};
  const subjectCodes = subjectCodesSnap.exists ? subjectCodesSnap.data()! : {};

  let batch = adminDb.batch();
  let opsInBatch = 0;
  const MAX_BATCH_OPS = 450;

  async function flushBatch() {
    if (opsInBatch > 0) {
      await batch.commit();
      batch = adminDb.batch();
      opsInBatch = 0;
    }
  }

  for (const doc of syllabusSnap.docs) {
    const data = doc.data();
    const board = data.board || '';
    const classNum = String(data.class || '');
    const subjectName = data.subject || '';

    if (!board || !classNum || !subjectName) {
      summary.errors.push(`Skipped syllabus doc "${doc.id}" due to missing board/class/subject values.`);
      continue;
    }

    if (!syllabusSubjectsTree[board]) {
      syllabusSubjectsTree[board] = {};
    }
    if (!syllabusSubjectsTree[board][classNum]) {
      syllabusSubjectsTree[board][classNum] = {};
    }
    syllabusSubjectsTree[board][classNum][subjectName] = {
      docId: doc.id
    };

    const boardCode = boardCodes[board] || board.substring(0, 4).toUpperCase();
    const subjectCode = subjectCodes[subjectName] || subjectName.substring(0, 4).toUpperCase();

    const chapters = Array.isArray(data.chapters) ? data.chapters : [];
    for (const chapter of chapters) {
      const chapterNum = chapter.number;
      if (!chapterNum) continue;
      const chapterName = chapter.name || '';

      const topics = Array.isArray(chapter.topics) ? chapter.topics : [];
      for (const topic of topics) {
        const topicNum = topic.number;
        if (!topicNum) continue;
        const topicName = topic.name || '';
        
        const topicCode = `${boardCode}-${classNum}-${subjectCode}-${chapterNum}-${topicNum}`;
        const subtopics = Array.isArray(topic.subtopics) ? topic.subtopics : [];
        const hasSubs = subtopics.length > 0;
        const subtopicsSum = hasSubs
          ? subtopics.reduce((acc: number, s: any) => acc + (Number(s.targetQuestions) || 30), 0)
          : 0;
        const topicTarget = hasSubs ? subtopicsSum : (Number(topic.targetQuestions) || 30);

        const docRef = adminDb.collection('syllabusTopicIndex').doc(topicCode);
        batch.set(docRef, {
          boardCode,
          classCode: String(classNum),
          subjectCode,
          subjectName,
          chapterNumber: String(chapterNum),
          chapterName,
          topicNumber: String(topicNum),
          topicName,
          topicCode,
          targetQuestions: topicTarget,
          hasSubtopics: hasSubs,
          createdAt: admin.firestore.FieldValue.serverTimestamp()
        }, { merge: true });

        opsInBatch++;
        summary.topicsIndexed++;
        if (opsInBatch >= MAX_BATCH_OPS) await flushBatch();

        // Subtopics indexing
        for (const subtopic of subtopics) {
          const subNum = subtopic.number;
          if (!subNum) continue;
          const subName = subtopic.name || '';

          const subCode = `${boardCode}-${classNum}-${subjectCode}-${chapterNum}-${subNum}`;
          validCodes.add(subCode);

          const subRef = adminDb.collection('syllabusTopicIndex').doc(subCode);
          batch.set(subRef, {
            boardCode,
            classCode: String(classNum),
            subjectCode,
            subjectName,
            chapterNumber: String(chapterNum),
            chapterName,
            topicNumber: String(subNum),
            topicName: subName,
            parentTopicCode: topicCode,
            topicCode: subCode,
            targetQuestions: Number(subtopic.targetQuestions) || 30,
            createdAt: admin.firestore.FieldValue.serverTimestamp()
          }, { merge: true });

          opsInBatch++;
          summary.topicsIndexed++;
          if (opsInBatch >= MAX_BATCH_OPS) await flushBatch();
        }
      }
    }
    summary.subjectsProcessed++;
  }

  await flushBatch();

  // Purge stale index records
  try {
    const existingIndexDocs = await adminDb.collection('syllabusTopicIndex').get();
    const staleDocs = existingIndexDocs.docs.filter(d => !validCodes.has(d.id));
    for (const staleDoc of staleDocs) {
      batch.delete(staleDoc.ref);
      opsInBatch++;
      summary.staleRemoved++;
      if (opsInBatch >= MAX_BATCH_OPS) await flushBatch();
    }
    await flushBatch();
  } catch (e: any) {
    summary.errors.push('Could not purge stale index records: ' + e.message);
  }

  try {
    await adminDb.collection('config').doc('syllabusSubjects').set({
      subjects: syllabusSubjectsTree,
      version: 1,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    }, { merge: true });
  } catch (e: any) {
    summary.errors.push('Could not rebuild config/syllabusSubjects: ' + e.message);
  }

  return summary;
}


export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { action } = body;

    if (action === 'dedupe') {
      const syllabusSnap = await adminDb.collection('syllabus').get();
      let chaptersRemoved = 0;
      let topicsRemoved = 0;
      let subtopicsRemoved = 0;
      let subjectsChanged = 0;

      const dedupeBatch = adminDb.batch();
      for (const doc of syllabusSnap.docs) {
        const subjectDoc = doc.data();
        let changed = false;

        const chapters = Array.isArray(subjectDoc.chapters) ? subjectDoc.chapters : [];
        const seenChapters = new Set<string>();
        const dedupedChapters: any[] = [];

        for (const chapter of chapters) {
          const chNum = String(chapter.number);
          if (seenChapters.has(chNum)) {
            chaptersRemoved++;
            changed = true;
            continue;
          }
          seenChapters.add(chNum);

          const topics = Array.isArray(chapter.topics) ? chapter.topics : [];
          const seenTopics = new Set<string>();
          const dedupedTopics: any[] = [];

          for (const topic of topics) {
            const tNum = String(topic.number);
            if (seenTopics.has(tNum)) {
              topicsRemoved++;
              changed = true;
              continue;
            }
            seenTopics.add(tNum);

            const subtopics = Array.isArray(topic.subtopics) ? topic.subtopics : [];
            const seenSubtopics = new Set<string>();
            const dedupedSubtopics: any[] = [];

            for (const subtopic of subtopics) {
              const sNum = String(subtopic.number);
              if (seenSubtopics.has(sNum)) {
                subtopicsRemoved++;
                changed = true;
                continue;
              }
              seenSubtopics.add(sNum);
              dedupedSubtopics.push(subtopic);
            }
            topic.subtopics = dedupedSubtopics;
            dedupedTopics.push(topic);
          }
          chapter.topics = dedupedTopics;
          dedupedChapters.push(chapter);
        }

        if (changed) {
          dedupeBatch.update(doc.ref, {
            chapters: dedupedChapters,
            updatedAt: new Date()
          });
          subjectsChanged++;
        }
      }

      if (subjectsChanged > 0) {
        await dedupeBatch.commit();
      }

      // Rebuild index after cleaning duplicates
      const reindexSummary = await runIndexRebuild();

      return NextResponse.json({
        success: true,
        chaptersRemoved,
        topicsRemoved,
        subtopicsRemoved,
        subjectsChanged,
        reindexSummary
      });
    }

    // Default action: rebuild index
    const summary = await runIndexRebuild();
    return NextResponse.json({ success: true, summary });

  } catch (error: any) {
    console.error('API syllabus indexing error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

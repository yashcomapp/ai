import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { isSubjectiveType } from '@/lib/questionTypes';
import { invalidateCache } from '@/lib/firebase/cache';

/**
 * Real-time atomic syllabus and topic counts synchronization.
 * Updates both the parent syllabus document and syllabusTopicIndex entries
 * whenever questions are created, updated, or deleted.
 */
export async function syncTopicCountsToSyllabus(topicCodes: string[]) {
  if (!topicCodes || !Array.isArray(topicCodes) || topicCodes.length === 0) return;
  const uniqueCodes = Array.from(new Set(topicCodes.filter(Boolean)));
  if (uniqueCodes.length === 0) return;

  // Group by (boardCode, class, subjectCode)
  const sylTargets = new Set<string>();
  uniqueCodes.forEach(code => {
    const parts = code.split('-');
    if (parts.length >= 3) {
      const bCode = parts[0].toLowerCase();
      const cls = parts[1];
      const sCode = parts[2].toLowerCase();
      sylTargets.add(`${bCode}_${cls}_${sCode}`);
    }
  });

  for (const targetKey of Array.from(sylTargets)) {
    try {
      const [bCode, cls, sCode] = targetKey.split('_');

      // Find syllabus document
      let sylDocRef = adminDb.collection('syllabus').doc(targetKey);
      let sylDocSnap = await sylDocRef.get();

      if (!sylDocSnap.exists) {
        const qSnap = await adminDb.collection('syllabus')
          .where('class', '==', cls)
          .where('subjectCode', '==', sCode.toUpperCase())
          .get();
        if (!qSnap.empty) {
          sylDocSnap = qSnap.docs[0];
          sylDocRef = sylDocSnap.ref;
        }
      }

      if (!sylDocSnap.exists) continue;
      const sylData = sylDocSnap.data()!;
      const boardCode = sylData.boardCode || (sylData.board === 'CBSE' ? 'CBSE' : 'MH');
      const classNum = String(sylData.class);
      const subjectCode = sylData.subjectCode;

      // Fetch all questions for this subject/class
      const qSnap = await adminDb.collection('questions')
        .where('class', '==', classNum)
        .where('subjectCode', '==', subjectCode)
        .get();

      const topicObjCounts: Record<string, number> = {};
      const topicSubjCounts: Record<string, number> = {};

      qSnap.docs.forEach(qDoc => {
        const q = qDoc.data();
        const tCode = q.topicCode;
        const type = q.type || '';
        if (!tCode) return;

        if (isSubjectiveType(type)) {
          topicSubjCounts[tCode] = (topicSubjCounts[tCode] || 0) + 1;
        } else {
          topicObjCounts[tCode] = (topicObjCounts[tCode] || 0) + 1;
        }
      });

      const chapters = sylData.chapters || [];
      const topicIndexBatch = adminDb.batch();
      let hasIndexUpdates = false;

      const updatedChapters = chapters.map((ch: any) => {
        const chNum = String(ch.number);
        let chObj = 0;
        let chSubj = 0;

        const topics = ch.topics || [];
        const updatedTopics = topics.map((t: any, tIdx: number) => {
          const isObj = t && typeof t === 'object';
          const tNum = isObj ? String(t.number || `${chNum}.${tIdx + 1}`) : `${chNum}.${tIdx + 1}`;
          const tName = isObj ? (t.name || t.title || '') : String(t);
          const tCode = isObj && t.topicCode ? t.topicCode : `${boardCode}-${classNum}-${subjectCode}-${chNum}-${tNum}`;

          let topObj = topicObjCounts[tCode] || 0;
          let topSubj = topicSubjCounts[tCode] || 0;

          let updatedSubtopics: any[] = [];
          if (isObj && Array.isArray(t.subtopics) && t.subtopics.length > 0) {
            updatedSubtopics = t.subtopics.map((st: any, stIdx: number) => {
              const isStObj = st && typeof st === 'object';
              const stNum = isStObj ? String(st.number || `${tNum}.${stIdx + 1}`) : `${tNum}.${stIdx + 1}`;
              const stName = isStObj ? (st.name || st.title || '') : String(st);
              const stCode = isStObj && st.topicCode ? st.topicCode : `${boardCode}-${classNum}-${subjectCode}-${chNum}-${stNum}`;

              const subObj = topicObjCounts[stCode] || 0;
              const subSubj = topicSubjCounts[stCode] || 0;

              topObj += subObj;
              topSubj += subSubj;

              // Stage topic index update for subtopic
              const idxRef = adminDb.collection('syllabusTopicIndex').doc(stCode);
              topicIndexBatch.set(idxRef, {
                objectiveCount: subObj,
                subjectiveCount: subSubj,
                updatedAt: admin.firestore.FieldValue.serverTimestamp()
              }, { merge: true });
              hasIndexUpdates = true;

              return {
                ...(isStObj ? st : {}),
                number: stNum,
                name: stName,
                topicCode: stCode,
                objectiveCount: subObj,
                subjectiveCount: subSubj
              };
            });
          }

          chObj += topObj;
          chSubj += topSubj;

          // Stage topic index update for main topic
          const idxRef = adminDb.collection('syllabusTopicIndex').doc(tCode);
          topicIndexBatch.set(idxRef, {
            objectiveCount: topObj,
            subjectiveCount: topSubj,
            updatedAt: admin.firestore.FieldValue.serverTimestamp()
          }, { merge: true });
          hasIndexUpdates = true;

          return {
            ...(isObj ? t : {}),
            number: tNum,
            name: tName,
            topicCode: tCode,
            objectiveCount: topObj,
            subjectiveCount: topSubj,
            subtopics: updatedSubtopics
          };
        });

        return {
          ...ch,
          objectiveCount: chObj,
          subjectiveCount: chSubj,
          topics: updatedTopics
        };
      });

      const totalDocObj = updatedChapters.reduce((acc: number, c: any) => acc + (c.objectiveCount || 0), 0);
      const totalDocSubj = updatedChapters.reduce((acc: number, c: any) => acc + (c.subjectiveCount || 0), 0);

      await sylDocRef.update({
        chapters: updatedChapters,
        totalObjectiveQuestions: totalDocObj,
        totalSubjectiveQuestions: totalDocSubj,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });

      if (hasIndexUpdates) {
        await topicIndexBatch.commit();
      }

      // Invalidate relevant caches
      invalidateCache(`syllabus_subject_${sylDocRef.id}`);
      invalidateCache('syllabus_all');
      invalidateCache('syllabus_list');
    } catch (err) {
      console.error(`Error syncing syllabus counts for target ${targetKey}:`, err);
    }
  }
}

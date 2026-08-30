import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { preprocessMathText, QUESTION_TYPE_MAP } from '@/lib/questionTypes';
import { invalidateCache } from '@/lib/firebase/cache';

export const dynamic = 'force-dynamic';

// Canonical Subject Code Map according to AGENTS.md Section L
const CANONICAL_SUBJECT_MAP: Record<string, { board: string; class: string; subjectCode: string; subjectName: string }> = {
  // CBSE Class 8
  'CBSE_8_GANI': { board: 'CBSE', class: '8', subjectCode: 'MGP1', subjectName: 'Ganit Prakash 1' },
  'CBSE_8_MATH': { board: 'CBSE', class: '8', subjectCode: 'MGP1', subjectName: 'Ganit Prakash 1' },
  'CBSE_8_MATHEMATICS': { board: 'CBSE', class: '8', subjectCode: 'MGP1', subjectName: 'Ganit Prakash 1' },
  'CBSE_8_SCIE': { board: 'CBSE', class: '8', subjectCode: 'CURI', subjectName: 'Curiosity' },
  'CBSE_8_SCIENCE': { board: 'CBSE', class: '8', subjectCode: 'CURI', subjectName: 'Curiosity' },
  // CBSE Class 9
  'CBSE_9_MATH': { board: 'CBSE', class: '9', subjectCode: 'MGM', subjectName: 'Mathematics - Ganita Manjari' },
  'CBSE_9_MATHEMATICS': { board: 'CBSE', class: '9', subjectCode: 'MGM', subjectName: 'Mathematics - Ganita Manjari' },
  'CBSE_9_SCIE': { board: 'CBSE', class: '9', subjectCode: 'SCIE', subjectName: 'Science - Exploration' },
  'CBSE_9_SCIENCE': { board: 'CBSE', class: '9', subjectCode: 'SCIE', subjectName: 'Science - Exploration' },
  // CBSE Class 10
  'CBSE_10_MATH': { board: 'CBSE', class: '10', subjectCode: 'MATH', subjectName: 'Mathematics' },
  'CBSE_10_MATHEMATICS': { board: 'CBSE', class: '10', subjectCode: 'MATH', subjectName: 'Mathematics' },
  'CBSE_10_SCIE': { board: 'CBSE', class: '10', subjectCode: 'SCI', subjectName: 'Science' },
  'CBSE_10_SCIENCE': { board: 'CBSE', class: '10', subjectCode: 'SCI', subjectName: 'Science' },
  // MH Class 8
  'MH_8_SCI': { board: 'MH', class: '8', subjectCode: 'SCI', subjectName: 'General Science' },
  'MH_8_SCIENCE': { board: 'MH', class: '8', subjectCode: 'SCI', subjectName: 'General Science' },
  // MH Class 9
  'MH_9_MTH1': { board: 'MH', class: '9', subjectCode: 'MTH1', subjectName: 'Algebra' },
  'MH_9_MTH2': { board: 'MH', class: '9', subjectCode: 'MTH2', subjectName: 'Geometry' },
  'MH_9_SCIT': { board: 'MH', class: '9', subjectCode: 'SCIT', subjectName: 'Science & Technology' },
  // MH Class 10
  'MH_10_MTH1': { board: 'MH', class: '10', subjectCode: 'MTH1', subjectName: 'Algebra' },
  'MH_10_MTH2': { board: 'MH', class: '10', subjectCode: 'MTH2', subjectName: 'Geometry' },
  'MH_10_SCIT1': { board: 'MH', class: '10', subjectCode: 'SCIT1', subjectName: 'Science & Tech Part 1' },
  'MH_10_SCIT2': { board: 'MH', class: '10', subjectCode: 'SCIT2', subjectName: 'Science & Tech Part 2' }
};

export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { mode } = await req.json().catch(() => ({ mode: 'dry_run' }));
    const isDryRun = mode === 'dry_run';

    // 1. Fetch all questions and syllabus topic index
    const [questionsSnap, topicIndexSnap] = await Promise.all([
      adminDb.collection('questions').get(),
      adminDb.collection('syllabusTopicIndex').get()
    ]);

    const stats = {
      totalScanned: questionsSnap.size,
      migratedSubjectCodes: 0,
      migratedDocIds: 0,
      mathFormatted: 0,
      typeStandardized: 0,
      topicCodeUpdated: 0,
      orphanedAutoIdsRemoved: 0,
      details: [] as string[]
    };

    const batch = new ChunkedBatch(adminDb);
    const docIdsToDelete = new Set<string>();
    const idMigrationMap = new Map<string, string>();

    for (const doc of questionsSnap.docs) {
      const data = doc.data();
      const currentDocId = doc.id;
      let isModified = false;
      const changes: string[] = [];

      // A. Standardize Board / Class / Subject / SubjectCode
      let board = String(data.board || 'CBSE').trim().toUpperCase();
      if (board === 'MAHARASHTRA') board = 'MH';
      let classNum = String(data.class || '8').trim();
      let rawSubject = String(data.subject || data.subjectName || data.subjectCode || '').trim().toUpperCase();

      // Lookup canonical subject definition
      const lookupKey = `${board}_${classNum}_${rawSubject}`;
      const canonicalSubj = CANONICAL_SUBJECT_MAP[lookupKey];

      let subjectCode = data.subjectCode || (canonicalSubj ? canonicalSubj.subjectCode : rawSubject);
      let subjectName = data.subjectName || data.subject || (canonicalSubj ? canonicalSubj.subjectName : rawSubject);

      if (canonicalSubj && (data.subjectCode !== canonicalSubj.subjectCode || data.subject !== canonicalSubj.subjectName)) {
        changes.push(`SubjectCode updated: ${data.subjectCode || rawSubject} -> ${canonicalSubj.subjectCode}`);
        subjectCode = canonicalSubj.subjectCode;
        subjectName = canonicalSubj.subjectName;
        isModified = true;
        stats.migratedSubjectCodes++;
      }

      // B. Standardize Question Type & Marks
      const currentType = data.type || 'single_mcq';
      const typeDef = QUESTION_TYPE_MAP[currentType] || QUESTION_TYPE_MAP['single_mcq'];
      const typeCode = typeDef.code || 'OSC';
      const defaultMarks = typeDef.defaultMarks || 4;
      const marks = data.marks !== undefined ? Number(data.marks) : defaultMarks;

      if (data.marks === undefined) {
        isModified = true;
        stats.typeStandardized++;
      }

      // C. Standardize Topic Code & Question Code
      let chapterNumber = String(data.chapterNumber || data.chapter || '1').replace(/^Ch\.?\s*/i, '').trim();
      let topicNumber = String(data.topicNumber || data.subtopicNumber || '1.1').trim();
      if (!topicNumber.includes('.')) {
        topicNumber = `${chapterNumber}.${topicNumber}`;
      }

      const canonicalTopicCode = `${board}-${classNum}-${subjectCode}-${chapterNumber}-${topicNumber}`;
      let topicCode = data.topicCode || canonicalTopicCode;

      if (topicCode.includes('-GANI-') || (topicCode.includes('-SCIE-') && classNum === '8')) {
        const oldTopic = topicCode;
        topicCode = topicCode.replace('-GANI-', '-MGP1-').replace('-SCIE-', '-CURI-');
        changes.push(`TopicCode updated: ${oldTopic} -> ${topicCode}`);
        isModified = true;
        stats.topicCodeUpdated++;
      }

      // Extract or compute 3-digit sequence
      let sequenceStr = '001';
      if (data.questionCode) {
        const parts = String(data.questionCode).split('-');
        const lastPart = parts[parts.length - 1];
        if (/^\d{3}$/.test(lastPart)) {
          sequenceStr = lastPart;
        }
      } else if (/^\d+$/.test(currentDocId)) {
        sequenceStr = String(currentDocId).padStart(3, '0');
      }

      const canonicalQuestionCode = `${canonicalTopicCode}-${typeCode}-${sequenceStr}`;
      let questionCode = data.questionCode || canonicalQuestionCode;

      if (questionCode.includes('-GANI-') || (questionCode.includes('-SCIE-') && classNum === '8')) {
        questionCode = questionCode.replace('-GANI-', '-MGP1-').replace('-SCIE-', '-CURI-');
        isModified = true;
      }

      // D. Standardize KaTeX & Math Formatting
      const originalText = String(data.text || data.questionText || '');
      const formattedText = preprocessMathText(originalText);

      const originalSolution = String(data.solution || data.explanation || '');
      const formattedSolution = preprocessMathText(originalSolution);

      let formattedOptions = Array.isArray(data.options)
        ? data.options.map((opt: any) => preprocessMathText(opt))
        : [];

      if (originalText !== formattedText || originalSolution !== formattedSolution) {
        isModified = true;
        stats.mathFormatted++;
      }

      // E. Check if Document ID matches canonical Question Code
      const targetDocId = canonicalQuestionCode;
      const isAutoId = currentDocId !== targetDocId;

      if (isAutoId) {
        stats.migratedDocIds++;
        changes.push(`Doc ID migrated from [${currentDocId}] to canonical [${targetDocId}]`);
        isModified = true;
        idMigrationMap.set(currentDocId, targetDocId);
        if (data.questionCode && data.questionCode !== targetDocId) {
          idMigrationMap.set(data.questionCode, targetDocId);
        }
      }

      if (isModified || isAutoId) {
        const updatedQuestion = {
          ...data,
          board,
          class: classNum,
          subject: subjectName,
          subjectCode,
          chapterNumber,
          topicNumber,
          topicCode,
          type: currentType,
          typeCode,
          marks,
          questionCode: targetDocId,
          text: formattedText,
          questionText: formattedText,
          solution: formattedSolution,
          explanation: formattedSolution,
          options: formattedOptions,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        };

        if (!isDryRun) {
          const targetRef = adminDb.collection('questions').doc(targetDocId);
          batch.set(targetRef, updatedQuestion, { merge: true });

          if (isAutoId && currentDocId !== targetDocId) {
            docIdsToDelete.add(currentDocId);
          }
        }

        stats.details.push(`• ${targetDocId}: ${changes.join('; ')}`);
      }
    }

    // Helper to remap any question code/ID across all migrations
    const remapQuestionCode = (c: string): string => {
      if (!c) return c;
      let mapped = idMigrationMap.get(c) || c;
      mapped = mapped.replace('-GANI-', '-MGP1-').replace('-SCIE-', '-CURI-');
      return mapped;
    };

    // Also synchronize active exams and subjectiveExams questionCodes
    const [examsSnap, subjExamsSnap] = await Promise.all([
      adminDb.collection('exams').get(),
      adminDb.collection('subjectiveExams').get()
    ]);

    for (const doc of examsSnap.docs) {
      const edata = doc.data();
      let updated = false;
      const updates: any = {};

      if (Array.isArray(edata.questionCodes)) {
        const newCodes = edata.questionCodes.map((c: string) => remapQuestionCode(c));
        if (JSON.stringify(newCodes) !== JSON.stringify(edata.questionCodes)) {
          updates.questionCodes = newCodes;
          updated = true;
        }
      }
      if (Array.isArray(edata.questionIds)) {
        const newIds = edata.questionIds.map((c: string) => remapQuestionCode(c));
        if (JSON.stringify(newIds) !== JSON.stringify(edata.questionIds)) {
          updates.questionIds = newIds;
          updated = true;
        }
      }
      if (Array.isArray(edata.questions)) {
        const newQuestions = edata.questions.map((q: any) => {
          if (!q || typeof q !== 'object') return q;
          const currentId = q.id || q.questionCode || '';
          const remappedId = remapQuestionCode(currentId);
          if (remappedId !== currentId) {
            return { ...q, id: remappedId, questionCode: remappedId };
          }
          return q;
        });
        if (JSON.stringify(newQuestions) !== JSON.stringify(edata.questions)) {
          updates.questions = newQuestions;
          updated = true;
        }
      }
      if (edata.subjectCode === 'GANI') {
        updates.subjectCode = 'MGP1';
        updated = true;
      }
      if (edata.subjectCode === 'SCIE' && String(edata.class) === '8') {
        updates.subjectCode = 'CURI';
        updated = true;
      }

      if (updated && !isDryRun) {
        batch.set(doc.ref, updates, { merge: true });
      }
    }

    for (const doc of subjExamsSnap.docs) {
      const edata = doc.data();
      let updated = false;
      const updates: any = {};

      if (Array.isArray(edata.questionIds)) {
        const newIds = edata.questionIds.map((c: string) => remapQuestionCode(c));
        if (JSON.stringify(newIds) !== JSON.stringify(edata.questionIds)) {
          updates.questionIds = newIds;
          updated = true;
        }
      }
      if (Array.isArray(edata.questionCodes)) {
        const newCodes = edata.questionCodes.map((c: string) => remapQuestionCode(c));
        if (JSON.stringify(newCodes) !== JSON.stringify(edata.questionCodes)) {
          updates.questionCodes = newCodes;
          updated = true;
        }
      }
      if (Array.isArray(edata.questions)) {
        const newQuestions = edata.questions.map((q: any) => {
          if (!q || typeof q !== 'object') return q;
          const currentId = q.id || q.questionCode || '';
          const remappedId = remapQuestionCode(currentId);
          if (remappedId !== currentId) {
            return { ...q, id: remappedId, questionCode: remappedId };
          }
          return q;
        });
        if (JSON.stringify(newQuestions) !== JSON.stringify(edata.questions)) {
          updates.questions = newQuestions;
          updated = true;
        }
      }
      if (edata.subjectCode === 'GANI') {
        updates.subjectCode = 'MGP1';
        updated = true;
      }
      if (edata.subjectCode === 'SCIE' && String(edata.class) === '8') {
        updates.subjectCode = 'CURI';
        updated = true;
      }

      if (updated && !isDryRun) {
        batch.set(doc.ref, updates, { merge: true });
      }
    }

    // Delete old orphan auto-ID documents
    if (!isDryRun && docIdsToDelete.size > 0) {
      for (const oldId of Array.from(docIdsToDelete)) {
        const oldRef = adminDb.collection('questions').doc(oldId);
        batch.delete(oldRef);
        stats.orphanedAutoIdsRemoved++;
      }
      await batch.commit();
      invalidateCache('qb_base_');
      invalidateCache('syllabus');
    } else if (!isDryRun) {
      await batch.commit();
      invalidateCache('qb_base_');
      invalidateCache('syllabus');
    }

    return NextResponse.json({
      success: true,
      mode: isDryRun ? 'dry_run' : 'applied',
      stats,
      sampleDetails: stats.details.slice(0, 30)
    });

  } catch (error: any) {
    console.error('API question bank harmonization error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

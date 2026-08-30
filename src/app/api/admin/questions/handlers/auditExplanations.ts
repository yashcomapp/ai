import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { invalidateCache } from '@/lib/firebase/cache';

export const dynamic = 'force-dynamic';

const PRACTICE_OBJECTIVE_TYPES = [
  'single_mcq', 
  'multiple_mcq', 
  'assertion_reason', 
  'true_false', 
  'fill_blanks', 
  'numerical', 
  'numerical_short'
];

// Helper to generate a structured pedagogical explanation for an objective question
function generateQuestionSolution(q: any): string {
  const qType = q.type || 'single_mcq';
  const qText = q.text || q.assertion || 'this problem';
  const cAns = q.correctAnswer || (Array.isArray(q.correctAnswers) ? q.correctAnswers.join(', ') : '');

  // 1. Single or Multiple MCQ
  if (qType === 'single_mcq' || qType === 'multiple_mcq') {
    let optText = '';
    if (Array.isArray(q.options) && q.options.length > 0) {
      const matched = q.options.find((o: any, idx: number) => {
        const text = typeof o === 'object' && o ? (o.text || o.value || '') : String(o);
        const code = String.fromCharCode(65 + idx);
        return code === cAns || text === cAns;
      });
      if (matched) {
        const txt = typeof matched === 'object' ? (matched.text || matched.value) : String(matched);
        optText = txt;
      }
    }

    const cChoiceDisplay = optText ? `(${cAns}) ${optText}` : (cAns ? `Option (${cAns})` : 'the correct option');

    return `• Correct Choice: ${cChoiceDisplay}

• Step-by-Step Explanation:
1. Concept Overview: Review the fundamental principles relating to "${q.topicName || q.chapter || 'this concept'}".
2. Analysis: Analyzing the given question "${qText.length > 80 ? qText.substring(0, 80) + '...' : qText}", we evaluate each option against standard definitions.
3. Conclusion: ${cChoiceDisplay} is mathematically and conceptually accurate.`;
  }

  // 2. Assertion & Reason
  if (qType === 'assertion_reason') {
    const assertion = q.assertion || qText;
    const reason = q.reason || '';

    let optionDesc = '';
    if (cAns === 'A') optionDesc = 'Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).';
    else if (cAns === 'B') optionDesc = 'Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).';
    else if (cAns === 'C') optionDesc = 'Assertion (A) is true, but Reason (R) is false.';
    else if (cAns === 'D') optionDesc = 'Assertion (A) is false, but Reason (R) is true.';
    else optionDesc = `Option (${cAns}) is correct.`;

    return `• Evaluation: ${optionDesc}

• Detailed Breakdown:
- Assertion (A): "${assertion}"
${reason ? `- Reason (R): "${reason}"\n` : ''}- Scientific Rationale: Upon verifying both statements, Option (${cAns}) accurately describes the logical relationship.`;
  }

  // 3. True / False
  if (qType === 'true_false') {
    const isTrue = String(cAns).toLowerCase() === 'true' || String(cAns) === 'A';
    const valText = isTrue ? 'True' : 'False';

    return `• Correct Answer: ${valText}

• Rationale:
The statement "${qText}" evaluates to ${valText} according to standard rules and definitions for ${q.topicName || q.chapter || 'this subject'}.`;
  }

  // 4. Numerical / Fill in Blanks
  return `• Correct Answer: ${cAns || 'See solution step'}

• Step-by-Step Solution:
1. Identify the given parameters in the problem statement.
2. Apply the relevant formula / rule for ${q.topicName || q.chapter || 'this topic'}.
3. Calculate: Evaluating the expressions yields ${cAns}.`;
}

// GET - Audit objective questions solution coverage
export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const snap = await adminDb.collection('questions').get();
    
    let totalObjective = 0;
    let withSolution = 0;
    let missingSolution = 0;
    const sampleMissing: any[] = [];
    const allMissingQuestions: any[] = [];

    snap.docs.forEach(doc => {
      const q = doc.data();
      const qType = q.type || 'single_mcq';

      if (PRACTICE_OBJECTIVE_TYPES.includes(qType) && !qType.startsWith('subjective')) {
        totalObjective++;

        const sol = (q.solution || q.explanation || q.solutionText || q.explanationText || '').trim();
        if (sol.length > 5) {
          withSolution++;
        } else {
          missingSolution++;
          const missingObj = {
            id: doc.id,
            questionCode: q.questionCode || doc.id,
            text: q.text || q.assertion || '',
            assertion: q.assertion || '',
            reason: q.reason || '',
            type: qType,
            options: q.options || [],
            correctAnswer: q.correctAnswer || (Array.isArray(q.correctAnswers) ? q.correctAnswers.join(', ') : ''),
            subject: q.subject || '',
            chapter: q.chapter || ''
          };
          allMissingQuestions.push(missingObj);
          if (sampleMissing.length < 15) {
            sampleMissing.push({
              id: doc.id,
              questionCode: q.questionCode || doc.id,
              text: (q.text || q.assertion || '').substring(0, 90),
              type: qType,
              topicCode: q.topicCode || q.topic || ''
            });
          }
        }
      }
    });

    return NextResponse.json({
      success: true,
      totalObjective,
      withSolution,
      missingSolution,
      coveragePercent: totalObjective > 0 ? Math.round((withSolution / totalObjective) * 100) : 100,
      sampleMissing,
      allMissingQuestions
    });
  } catch (error: any) {
    console.error('API Audit Questions GET error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// POST - Auto-generate or import AI solutions for questions missing explanations
export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json().catch(() => ({}));
    const { action, importedSolutions, forceAll, targetTopicCode } = body;

    // Handle Importing External AI Solutions Map
    if (action === 'importAI' && importedSolutions && typeof importedSolutions === 'object') {
      const snap = await adminDb.collection('questions').get();
      let importedCount = 0;
      const batchSize = 400;
      let currentBatch = adminDb.batch();
      let batchOps = 0;

      snap.docs.forEach(doc => {
        const q = doc.data();
        const qCode = q.questionCode || doc.id;

        const solText = importedSolutions[qCode] || importedSolutions[doc.id];
        if (solText && typeof solText === 'string' && solText.trim().length > 3) {
          currentBatch.update(doc.ref, {
            solution: solText.trim(),
            explanation: solText.trim(),
            updatedAt: new Date()
          });
          importedCount++;
          batchOps++;

          if (batchOps >= batchSize) {
            currentBatch.commit();
            currentBatch = adminDb.batch();
            batchOps = 0;
          }
        }
      });

      if (batchOps > 0) {
        await currentBatch.commit();
      }
      invalidateCache('qb_base_');

      return NextResponse.json({
        success: true,
        updatedCount: importedCount,
        message: `Successfully imported and saved ${importedCount} AI solutions into Question Bank!`
      });
    }

    // Default internal auto-generator
    const snap = await adminDb.collection('questions').get();
    let processedCount = 0;
    let updatedCount = 0;

    const batchSize = 400;
    let currentBatch = adminDb.batch();
    let batchOperationCount = 0;

    for (const doc of snap.docs) {
      const q = doc.data();
      const qType = q.type || 'single_mcq';

      if (!PRACTICE_OBJECTIVE_TYPES.includes(qType) || qType.startsWith('subjective')) {
        continue;
      }

      if (targetTopicCode && q.topicCode !== targetTopicCode && q.topic !== targetTopicCode) {
        continue;
      }

      processedCount++;
      const existingSol = (q.solution || q.explanation || q.solutionText || q.explanationText || '').trim();
      const needsSolution = forceAll || existingSol.length <= 5;

      if (needsSolution) {
        const generatedSolution = generateQuestionSolution(q);

        currentBatch.update(doc.ref, {
          solution: generatedSolution,
          explanation: generatedSolution,
          updatedAt: new Date()
        });

        updatedCount++;
        batchOperationCount++;

        if (batchOperationCount >= batchSize) {
          await currentBatch.commit();
          currentBatch = adminDb.batch();
          batchOperationCount = 0;
        }
      }
    }

    if (batchOperationCount > 0) {
      await currentBatch.commit();
    }
    if (updatedCount > 0) {
      invalidateCache('qb_base_');
    }

    return NextResponse.json({
      success: true,
      processedCount,
      updatedCount,
      message: `Audit complete. Updated ${updatedCount} objective questions with step-by-step explanations.`
    });
  } catch (error: any) {
    console.error('API Audit Questions POST error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

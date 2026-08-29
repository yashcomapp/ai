import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';

export const dynamic = 'force-dynamic';

function isCandidateNumericalQuestion(q: any): boolean {
  if (!q) return false;
  
  // If already numerical, skip
  if (q.type === 'numerical' || q.type === 'numerical_short' || q.type === 'numerical_long') {
    return false;
  }

  const qCode = String(q.questionCode || q.code || '');
  const text = String(q.text || '');
  const ans = String(q.correctAnswer || '').trim();
  const options = Array.isArray(q.options) ? q.options : [];

  // Check 1: Explicit question code marked as ONE (Objective Numerical)
  if (/-ONE-/.test(qCode)) {
    return true;
  }

  // Check 2: Pure numeric answer with calculation/numerical question phrasing or empty/numeric options
  const isPureNumber = ans !== '' && !isNaN(Number(ans)) && !/^0\d+/.test(ans);
  
  if (isPureNumber) {
    // If all options (if present) are numeric or options is empty
    const allOptionsNumeric = options.length === 0 || options.every((opt: any) => !isNaN(Number(String(opt).trim())));
    if (allOptionsNumeric) {
      return true;
    }

    // Or if question text contains calculation keywords
    const calculationPhrases = /(?:calculate|find the value|determine the|numerical value|how many|what is the magnitude|evaluate the value|speed of|velocity of|frequency of|mass of|volume of|area of)/i;
    if (calculationPhrases.test(text)) {
      return true;
    }
  }

  return false;
}

// 1. GET - Audit preview candidate non-numerical objective questions
export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const snap = await adminDb.collection('questions').get();
    const candidates: any[] = [];

    snap.docs.forEach(doc => {
      const data = doc.data();
      const qObj = { id: doc.id, ...data };
      if (isCandidateNumericalQuestion(qObj)) {
        candidates.push({
          id: doc.id,
          questionCode: data.questionCode || '',
          type: data.type || '',
          text: data.text || '',
          correctAnswer: data.correctAnswer || '',
          options: data.options || []
        });
      }
    });

    return NextResponse.json({
      totalQuestionsScanned: snap.docs.length,
      candidateCount: candidates.length,
      candidates
    });
  } catch (error: any) {
    console.error('Audit numerical GET error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 2. POST - Execute migration: Convert candidate questions to 'numerical' type and update codes
export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const snap = await adminDb.collection('questions').get();
    const batch = new ChunkedBatch(adminDb);
    let updatedCount = 0;

    snap.docs.forEach(doc => {
      const data = doc.data();
      const qObj = { id: doc.id, ...data };
      if (isCandidateNumericalQuestion(qObj)) {
        const docRef = doc.ref;
        const currentCode = data.questionCode || '';
        
        // Update questionCode prefix to -ONE- if it had -OSC-, -OFB-, -OMC-, etc.
        let newCode = currentCode;
        if (currentCode) {
          newCode = currentCode.replace(/-(OSC|OFB|OMC|OTF|OAR)-/, '-ONE-');
        }

        batch.update(docRef, {
          type: 'numerical',
          questionCode: newCode,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        });

        updatedCount++;
      }
    });

    if (updatedCount > 0) {
      await batch.commit();
    }

    return NextResponse.json({
      success: true,
      updatedCount,
      message: `Successfully audited and migrated ${updatedCount} objective questions to 'numerical' type.`
    });
  } catch (error: any) {
    console.error('Audit numerical POST error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

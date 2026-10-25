import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { invalidateCache } from '@/lib/firebase/cache';
import { fetchPageByDocId, fetchAllByDocIdRange, fetchCollectionWithPagination } from '@/lib/firebase/docIdPagination';


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

    const selectFields = ['type', 'questionCode', 'correctAnswer', 'text', 'options'];
    const { docs, hasMore, nextCursor, isPaginated } = await fetchCollectionWithPagination('questions', req.url, selectFields);

    const candidates: any[] = [];

    docs.forEach(doc => {
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
      totalQuestionsScanned: docs.length,
      candidateCount: candidates.length,
      candidates,
      hasMore,
      nextCursor
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

    const body = await req.json().catch(() => ({}));
    const cursor = body?.cursor;
    const limitParam = body?.limit;
    const isPaginated = cursor !== undefined || limitParam !== undefined;
    const limit = limitParam ? Math.min(Math.max(parseInt(limitParam, 10) || 500, 1), 1000) : 500;

    const selectFields = ['type', 'questionCode', 'correctAnswer', 'text', 'options'];
    let docs: admin.firestore.QueryDocumentSnapshot[] = [];
    let hasMore = false;
    let nextCursor: string | null = null;

    if (isPaginated) {
      const page = await fetchPageByDocId('questions', { selectFields, cursor, limit });
      docs = page.docs;
      hasMore = page.hasMore;
      nextCursor = page.nextCursor;
    } else {
      docs = await fetchAllByDocIdRange('questions', { selectFields, chunkSize: 500 });
      hasMore = false;
      nextCursor = null;
    }

    const batch = new ChunkedBatch(adminDb);
    let updatedCount = 0;

    docs.forEach(doc => {
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
      invalidateCache('qb_base_');
    }

    return NextResponse.json({
      success: true,
      updatedCount,
      hasMore,
      nextCursor,
      message: `Successfully audited and migrated ${updatedCount} objective questions to 'numerical' type.`
    });
  } catch (error: any) {
    console.error('Audit numerical POST error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

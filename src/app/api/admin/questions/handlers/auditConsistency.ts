import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import * as admin from 'firebase-admin';
import { isTopicPurelyQualitative } from '@/lib/curriculumGuard';

export interface ConsistencyAnomaly {
  docId: string;
  qCode: string;
  topicCode: string;
  type: string;
  currentCorrectAnswer: string;
  currentNumericalValue?: number;
  fixedCorrectAnswer?: string;
  fixedNumericalValue?: number;
  reason: string;
  confidence: 'HIGH' | 'MEDIUM';
}

export function evaluateQuestionConsistency(q: any, docId: string): ConsistencyAnomaly | null {
  const qCode = q.questionCode || docId;
  const type = q.type || 'OSC';
  const cAns = String(q.correctAnswer || '').trim().toUpperCase();
  const sol = (q.solution || q.explanation || '').trim();
  const options = Array.isArray(q.options) ? q.options : [];

  if (!sol || sol.length < 5) return null;

  const getOptText = (idx: number): string => {
    if (idx < 0 || idx >= options.length) return '';
    const opt = options[idx];
    if (typeof opt === 'object' && opt !== null) {
      return (opt.text || opt.value || opt.label || '').trim();
    }
    return String(opt).trim();
  };

  // 1. Check: Numerical Objective (ONE) on purely qualitative chapter OR explanation mismatch
  if (type === 'ONE' || qCode.includes('-ONE-')) {
    if (isTopicPurelyQualitative(q.topicCode || qCode, q.chapterName || q.chapterTitle, q.subject)) {
      return {
        docId,
        qCode,
        topicCode: q.topicCode || '',
        type,
        currentCorrectAnswer: cAns,
        reason: `ONE numerical question is forbidden on purely qualitative chapter (${q.topicCode || qCode}). Convert to OSC.`,
        confidence: 'HIGH'
      };
    }
    const numMatch = sol.match(/Correct\s+Answer\s+is\s+([0-9.]+)/i);
    if (numMatch) {
      const calcNum = parseFloat(numMatch[1]);
      let matchingIdx = -1;

      if (options.length > 0) {
        options.forEach((opt: any, idx: number) => {
          const txt = getOptText(idx).replace(/\\text\{[^}]+\}/g, '').replace(/[^0-9.]/g, '');
          const val = parseFloat(txt);
          if (!isNaN(val) && Math.abs(val - calcNum) < 0.05) {
            matchingIdx = idx;
          }
        });
      }

      const matchingLetter = matchingIdx !== -1 ? String.fromCharCode(65 + matchingIdx) : undefined;
      const numValMismatch = q.numericalValue !== undefined && Math.abs(parseFloat(q.numericalValue) - calcNum) > 0.05;
      const optMismatch = matchingLetter && matchingLetter !== cAns;

      if (numValMismatch || optMismatch) {
        return {
          docId,
          qCode,
          topicCode: q.topicCode || '',
          type,
          currentCorrectAnswer: cAns,
          currentNumericalValue: q.numericalValue,
          fixedCorrectAnswer: matchingLetter || cAns,
          fixedNumericalValue: calcNum,
          reason: `Explanation calculated ${calcNum}, but DB has answer=${cAns} and numericalValue=${q.numericalValue}. Matching option is ${matchingLetter || 'N/A'}.`,
          confidence: 'HIGH'
        };
      }
    }
  }

  // 2. Check: Object-based options with explicit isCorrect flag contradicting correctAnswer
  if (options.length > 0 && typeof options[0] === 'object' && options[0] !== null) {
    const correctIndices: number[] = [];
    options.forEach((opt: any, idx: number) => {
      if (opt && (opt.isCorrect === true || opt.correct === true)) {
        correctIndices.push(idx);
      }
    });

    if (correctIndices.length === 1) {
      const expectedLetter = String.fromCharCode(65 + correctIndices[0]);
      if (expectedLetter !== cAns && ['A', 'B', 'C', 'D'].includes(cAns)) {
        return {
          docId,
          qCode,
          topicCode: q.topicCode || '',
          type,
          currentCorrectAnswer: cAns,
          fixedCorrectAnswer: expectedLetter,
          reason: `Option ${expectedLetter} has isCorrect: true, but correctAnswer is ${cAns}.`,
          confidence: 'HIGH'
        };
      }
    }
  }

  // 3. Check: Explicit "Correct Choice is (X)" in explanation
  const choiceMatches = [
    ...sol.matchAll(/Correct\s+(?:Choice|Option)\s+(?:is\s+)?\(?([A-D])\)?/gi),
    ...sol.matchAll(/Option\s+\(?([A-D])\)?\s+is\s+correct/gi)
  ];

  if (choiceMatches.length > 0) {
    const lastMatch = choiceMatches[choiceMatches.length - 1];
    const statedLetter = lastMatch[1].toUpperCase();
    if (statedLetter !== cAns && ['A', 'B', 'C', 'D'].includes(statedLetter)) {
      return {
        docId,
        qCode,
        topicCode: q.topicCode || '',
        type,
        currentCorrectAnswer: cAns,
        fixedCorrectAnswer: statedLetter,
        reason: `Explanation explicitly states "${lastMatch[0]}", but correctAnswer is ${cAns}.`,
        confidence: 'HIGH'
      };
    }
  }

  return null;
}

// GET: Run audit inspection (dry-run)
export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const subjectCode = searchParams.get('subjectCode');
    const classVal = searchParams.get('class');
    const boardCode = searchParams.get('boardCode') || searchParams.get('board');
    const limit = Math.min(parseInt(searchParams.get('limit') || '500', 10), 2000);
    const cursor = searchParams.get('cursor');

    let query: admin.firestore.Query = adminDb.collection('questions');

    if (subjectCode) query = query.where('subjectCode', '==', subjectCode);
    if (classVal) query = query.where('class', '==', String(classVal));
    if (boardCode) query = query.where('boardCode', '==', boardCode);

    query = query.select(
      'questionCode',
      'text',
      'options',
      'correctAnswer',
      'solution',
      'explanation',
      'type',
      'numericalValue',
      'topicCode',
      'class',
      'subjectCode',
      'boardCode'
    );

    query = query.orderBy(admin.firestore.FieldPath.documentId()).limit(limit);
    if (cursor) {
      query = query.startAfter(cursor);
    }

    const snap = await query.get();
    const anomalies: ConsistencyAnomaly[] = [];

    snap.docs.forEach(doc => {
      const anomaly = evaluateQuestionConsistency(doc.data(), doc.id);
      if (anomaly) {
        anomalies.push(anomaly);
      }
    });

    const hasMore = snap.docs.length === limit;
    const nextCursor = hasMore && snap.docs.length > 0 ? snap.docs[snap.docs.length - 1].id : null;

    return NextResponse.json({
      success: true,
      scannedCount: snap.docs.length,
      anomalyCount: anomalies.length,
      anomalies,
      hasMore,
      nextCursor
    });
  } catch (err: any) {
    console.error('Audit Consistency GET Error:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

// POST: Execute targeted atomic fixes on detected anomalies
export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json().catch(() => ({}));
    const fixes: ConsistencyAnomaly[] = Array.isArray(body.fixes) ? body.fixes : [];

    if (fixes.length === 0) {
      return NextResponse.json({ message: 'No fixes provided in request body.' }, { status: 400 });
    }

    // Pre-mutation backup of targeted docs in _systemBackups
    const backupId = `consistency_fix_${Date.now()}`;
    const backupData: Record<string, any> = {};

    const batch = adminDb.batch();
    for (const fix of fixes) {
      if (!fix.docId) continue;
      const ref = adminDb.collection('questions').doc(fix.docId);
      const prevDoc = await ref.get();
      if (prevDoc.exists) {
        backupData[fix.docId] = prevDoc.data();
      }

      const updatePayload: Record<string, any> = {
        updatedAt: new Date()
      };
      if (fix.fixedCorrectAnswer) {
        updatePayload.correctAnswer = fix.fixedCorrectAnswer;
      }
      if (fix.fixedNumericalValue !== undefined) {
        updatePayload.numericalValue = fix.fixedNumericalValue;
      }

      batch.update(ref, updatePayload);
    }

    // Save backup record
    await adminDb.collection('_systemBackups').doc(backupId).set({
      type: 'question_consistency_fix',
      count: Object.keys(backupData).length,
      data: backupData,
      createdAt: new Date()
    });

    await batch.commit();

    return NextResponse.json({
      success: true,
      backupId,
      appliedCount: fixes.length
    });
  } catch (err: any) {
    console.error('Audit Consistency POST Error:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

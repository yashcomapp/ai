import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { getDateKeyIST as getISTDateString } from '@/lib/dateUtils';
import { toPositiveNumber } from '@/lib/validationUtils';
import { normalizeStudentFeeRecord } from '@/lib/feeUtils';
import { FeeService } from '@/services/fee.service';



export async function GET(req: NextRequest) {
  try {
    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const studentCode = searchParams.get('studentCode');

    let snap;
    const limitParam = parseInt(searchParams.get('limit') || '300', 10);
    const queryLimit = Math.min(Math.max(1, isNaN(limitParam) ? 300 : limitParam), 1000);

    let hasMore = false;
    if (studentCode) {
      const sCodeUpper = studentCode.trim().toUpperCase();
      snap = await adminDb.collection('feeTransactions')
        .where('studentCode', '==', sCodeUpper)
        .get();
      
      // Fallback if legacy documents were saved with exact casing
      if (snap.empty && studentCode.trim() !== sCodeUpper) {
        snap = await adminDb.collection('feeTransactions')
          .where('studentCode', '==', studentCode.trim())
          .get();
      }
    } else {
      snap = await adminDb.collection('feeTransactions')
        .orderBy('timestamp', 'desc')
        .limit(queryLimit + 1)
        .get()
        .catch(async () => {
          return await adminDb.collection('feeTransactions').limit(queryLimit + 1).get();
        });

      if (snap.docs.length > queryLimit) {
        hasMore = true;
        snap = { docs: snap.docs.slice(0, queryLimit) } as any;
      }
    }

    const transactions = (snap.docs as any[])
      .map((doc: any) => {
        const d = doc.data();
        return {
          id: doc.id,
          transactionId: d.transactionId || doc.id,
          ...d
        };
      })
      .sort((a: any, b: any) => new Date(b.timestamp || 0).getTime() - new Date(a.timestamp || 0).getTime());

    return NextResponse.json({ success: true, transactions, hasMore });
  } catch (error: any) {
    console.error('API GET fee transactions error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

function parsePaymentTimestamp(paymentDate?: string, rawTimestamp?: string): string {
  const now = new Date();
  if (rawTimestamp && rawTimestamp.includes('T') && !rawTimestamp.endsWith('T00:00:00.000Z') && !rawTimestamp.endsWith('T00:00:00Z')) {
    const p = new Date(rawTimestamp);
    if (!isNaN(p.getTime())) return p.toISOString();
  }
  const dateStr = paymentDate || (rawTimestamp && rawTimestamp.split('T')[0]);
  if (dateStr && dateStr.includes('-')) {
    const parts = dateStr.split('-').map(Number);
    if (parts.length === 3 && parts[0] && parts[1] && parts[2]) {
      const d = new Date();
      d.setFullYear(parts[0], parts[1] - 1, parts[2]);
      d.setHours(now.getHours(), now.getMinutes(), now.getSeconds(), now.getMilliseconds());
      return d.toISOString();
    }
  }
  return now.toISOString();
}

export async function POST(req: NextRequest) {
  try {
    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { action, transactionId, transactionData } = body;

    if (action === 'bulk') {
      const { payments } = body; // payments: { studentCode, amountPaid, paymentMethod, referenceNumber, installmentId, paymentDate }[]
      if (!Array.isArray(payments) || payments.length === 0) {
        return NextResponse.json({ error: 'Missing or invalid payments array.' }, { status: 400 });
      }

      // Preload existing transactions for these students to prevent double-posting the exact same installment
      const uniqueStudentCodes = Array.from(new Set(
        payments.map(p => (p.studentCode || '').trim().toUpperCase()).filter(Boolean)
      ));

      const existingTxsSnap = await adminDb.collection('feeTransactions')
        .where('studentCode', 'in', uniqueStudentCodes.slice(0, 30))
        .get();
      
      const existingTxSet = new Set<string>();
      existingTxsSnap.docs.forEach(d => {
        const data = d.data();
        if (data.studentCode && data.installmentId) {
          existingTxSet.add(`${data.studentCode.toUpperCase()}_${data.installmentId}_${data.amountPaid}`);
        }
      });

      const results = [];
      const batch = adminDb.batch();
      const affectedStudentCodes = new Set<string>();

      for (const pay of payments) {
        const { studentCode, amountPaid, paymentMethod, referenceNumber, installmentId, paymentDate } = pay;
        if (!studentCode || amountPaid === undefined || !paymentMethod) continue;

        let validAmount: number;
        try {
          validAmount = toPositiveNumber(amountPaid, `amountPaid for ${studentCode}`);
        } catch {
          continue; // Skip invalid or zero/negative payment rows in bulk
        }

        const cleanCode = studentCode.trim().toUpperCase();

        // Guard against duplicate insertion if same installment & amount is already recorded
        const txKey = `${cleanCode}_${installmentId}_${validAmount}`;
        if (installmentId && existingTxSet.has(txKey)) {
          console.warn(`Skipping duplicate transaction for ${cleanCode} ${installmentId} (₹${validAmount})`);
          continue;
        }

        affectedStudentCodes.add(cleanCode);
        existingTxSet.add(txKey);

        const txTimestamp = parsePaymentTimestamp(paymentDate);

        const newTxRef = adminDb.collection('feeTransactions').doc();
        const newTx = {
          transactionId: newTxRef.id,
          studentCode: cleanCode,
          installmentId: installmentId || '',
          amountPaid: validAmount,
          paymentMethod,
          referenceNumber: referenceNumber || '',
          receiptUrl: '',
          recordedBy: admin.decodedToken?.email || 'admin',
          timestamp: txTimestamp
        };

        batch.set(newTxRef, newTx);
        results.push(newTx);
      }

      if (results.length > 0) {
        await batch.commit();
        // Sync student fees in parallel for all unique student codes affected
        await Promise.all(
          Array.from(affectedStudentCodes).map(code => FeeService.recalculateAndSyncStudentFeeRecord(code))
        );
      }

      return NextResponse.json({ success: true, count: results.length });
    }

    if (action === 'create') {
      const { studentCode, installmentId, amountPaid, paymentMethod, referenceNumber, receiptUrl, timestamp } = transactionData;
      if (!studentCode || amountPaid === undefined || !paymentMethod) {
        return NextResponse.json({ error: 'Missing required transaction fields.' }, { status: 400 });
      }

      const validAmount = toPositiveNumber(amountPaid, 'amountPaid');
      const cleanCode = studentCode.trim().toUpperCase();
      const newTxRef = adminDb.collection('feeTransactions').doc();
      const newTx = {
        transactionId: newTxRef.id,
        studentCode: cleanCode,
        installmentId: installmentId || '',
        amountPaid: validAmount,
        paymentMethod,
        referenceNumber: referenceNumber || '',
        receiptUrl: receiptUrl || '',
        recordedBy: admin.decodedToken?.email || 'admin',
        timestamp: parsePaymentTimestamp(undefined, timestamp)
      };

      await newTxRef.set(newTx);
      await FeeService.recalculateAndSyncStudentFeeRecord(cleanCode);

      return NextResponse.json({ success: true, transaction: newTx });
    }

    if (action === 'edit') {
      if (!transactionId) {
        return NextResponse.json({ error: 'Missing transactionId.' }, { status: 400 });
      }
      const { studentCode, installmentId, amountPaid, paymentMethod, referenceNumber, receiptUrl, timestamp, paymentDate } = transactionData || {};
      if (amountPaid === undefined || !paymentMethod) {
        return NextResponse.json({ error: 'Missing required transaction fields.' }, { status: 400 });
      }

      const validAmount = toPositiveNumber(amountPaid, 'amountPaid');

      let txRef = adminDb.collection('feeTransactions').doc(transactionId);
      let txSnap = await txRef.get();
      
      if (!txSnap.exists) {
        const altQuery = await adminDb.collection('feeTransactions').where('transactionId', '==', transactionId).limit(1).get();
        if (!altQuery.empty) {
          txRef = altQuery.docs[0].ref;
          txSnap = altQuery.docs[0];
        } else {
          return NextResponse.json({ error: 'Transaction not found.' }, { status: 404 });
        }
      }

      const existingData = txSnap.data() || {};
      const cleanCode = (studentCode || existingData.studentCode || '').trim().toUpperCase();
      const updatedTimestamp = parsePaymentTimestamp(paymentDate, timestamp || existingData.timestamp);

      await txRef.update({
        studentCode: cleanCode,
        installmentId: installmentId !== undefined ? installmentId : (existingData.installmentId || ''),
        amountPaid: validAmount,
        paymentMethod,
        referenceNumber: referenceNumber !== undefined ? referenceNumber : (existingData.referenceNumber || ''),
        receiptUrl: receiptUrl !== undefined ? receiptUrl : (existingData.receiptUrl || ''),
        timestamp: updatedTimestamp
      });

      if (cleanCode) {
        await FeeService.recalculateAndSyncStudentFeeRecord(cleanCode);
      }
      return NextResponse.json({ success: true, message: 'Transaction updated successfully.' });
    }

    if (action === 'delete') {
      if (!transactionId) {
        return NextResponse.json({ error: 'Missing transactionId.' }, { status: 400 });
      }
      
      let txRef = adminDb.collection('feeTransactions').doc(transactionId);
      let txSnap = await txRef.get();
      if (!txSnap.exists) {
        const altQuery = await adminDb.collection('feeTransactions').where('transactionId', '==', transactionId).limit(1).get();
        if (!altQuery.empty) {
          txRef = altQuery.docs[0].ref;
          txSnap = altQuery.docs[0];
        } else {
          return NextResponse.json({ error: 'Transaction not found.' }, { status: 404 });
        }
      }

      const cleanCode = txSnap.data()?.studentCode;
      await txRef.delete();

      if (cleanCode) {
        await FeeService.recalculateAndSyncStudentFeeRecord(cleanCode);
      }
      return NextResponse.json({ success: true, message: 'Transaction deleted successfully.' });
    }

    return NextResponse.json({ error: 'Invalid action.' }, { status: 400 });
  } catch (error: any) {
    console.error('API POST fee transactions error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { getDateKeyIST as getISTDateString } from '@/lib/dateUtils';

export const dynamic = 'force-dynamic';

// Function to synchronize aggregate balances and status in studentFees doc based on ledger transactions
async function syncStudentFees(studentCode: string) {
  const studentCodeUpper = studentCode.trim().toUpperCase();
  const feeRef = adminDb.collection('studentFees').doc(studentCodeUpper);
  const feeDoc = await feeRef.get();
  
  if (!feeDoc.exists) return;
  const feeData = feeDoc.data()!;

  // 1. Fetch all payment transactions for this student
  const txSnap = await adminDb.collection('feeTransactions')
    .where('studentCode', '==', studentCodeUpper)
    .get();
  const transactions = txSnap.docs.map(doc => doc.data());

  // 2. Sum overall paid totals
  const totalPaidAmount = transactions.reduce((sum, tx) => sum + Number(tx.amountPaid || 0), 0);
  const netPayableAmount = Number(feeData.netPayableAmount || feeData.totalPackageAmount || 0);
  const outstandingAmount = Math.max(0, netPayableAmount - totalPaidAmount);

  // 3. Map transaction payments by installmentId
  const paymentsByInst: Record<string, number> = {};
  let regPaidTotal = 0;

  transactions.forEach(tx => {
    if (tx.installmentId === 'registration') {
      regPaidTotal += Number(tx.amountPaid || 0);
    } else if (tx.installmentId) {
      paymentsByInst[tx.installmentId] = (paymentsByInst[tx.installmentId] || 0) + Number(tx.amountPaid || 0);
    }
  });

  // 4. Update registration status
  const regFeeData = feeData.registrationFee || { amount: 0, status: 'pending' };
  const regStatus = regPaidTotal >= Number(regFeeData.amount || 0) ? 'paid' : 'pending';
  const updatedRegFee = {
    ...regFeeData,
    status: regStatus,
    paidAt: regStatus === 'paid' ? (regFeeData.paidAt || new Date().toISOString()) : null
  };

  // 5. Update individual installments status
  const todayStr = getISTDateString();
  const installments = Array.isArray(feeData.installments) ? feeData.installments : [];
  let hasOverdueInstallment = false;
  let nextInstallmentDueDate: string | null = null;

  const updatedInstallments = installments.map((inst: any) => {
    const instId = inst.installmentId || `inst_${inst.installmentNo}`;
    const paidForInst = paymentsByInst[instId] || 0;
    const targetAmount = Number(inst.amount || 0);
    
    let status = 'pending';
    let paidAt = inst.paidAt || null;

    if (paidForInst >= targetAmount) {
      status = 'paid';
      paidAt = paidAt || new Date().toISOString();
    } else {
      // Unpaid or partially paid. Check if due date has passed
      if (inst.dueDate && inst.dueDate < todayStr) {
        status = 'overdue';
        hasOverdueInstallment = true;
      }
      
      // Track earliest next due date
      if (!nextInstallmentDueDate || (inst.dueDate && inst.dueDate < nextInstallmentDueDate)) {
        nextInstallmentDueDate = inst.dueDate;
      }
    }

    return {
      ...inst,
      installmentId: instId,
      status,
      paidAt
    };
  });

  // Determine overall status
  let feeStatus = 'unpaid';
  if (totalPaidAmount >= netPayableAmount) {
    feeStatus = 'fully_paid';
  } else if (totalPaidAmount > 0) {
    feeStatus = 'partially_paid';
  }

  // 6. Write synchronized results to studentFees document
  await feeRef.update({
    totalPaidAmount,
    outstandingAmount,
    feeStatus,
    hasOverdueInstallment,
    nextInstallmentDueDate,
    registrationFee: updatedRegFee,
    installments: updatedInstallments,
    updatedAt: new Date().toISOString()
  });

  // 7. Also sync user profile feeStatus field for backward-compatibility
  const studentQuery = await adminDb.collection('users')
    .where('studentCode', '==', studentCodeUpper)
    .get();
  if (!studentQuery.empty) {
    await studentQuery.docs[0].ref.update({
      feeStatus
    });
  }
}

export async function GET(req: NextRequest) {
  try {
    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const studentCode = searchParams.get('studentCode');

    let query = adminDb.collection('feeTransactions').orderBy('timestamp', 'desc');
    if (studentCode) {
      query = query.where('studentCode', '==', studentCode.trim().toUpperCase());
    }

    const snap = await query.get();
    const transactions = snap.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));

    return NextResponse.json({ success: true, transactions });
  } catch (error: any) {
    console.error('API GET fee transactions error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
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
      const { payments } = body; // payments: { studentCode, amountPaid, paymentMethod, referenceNumber, installmentId }[]
      if (!Array.isArray(payments) || payments.length === 0) {
        return NextResponse.json({ error: 'Missing or invalid payments array.' }, { status: 400 });
      }

      const results = [];
      const batch = adminDb.batch();
      const uniqueStudentCodes = new Set<string>();

      for (const pay of payments) {
        const { studentCode, amountPaid, paymentMethod, referenceNumber, installmentId } = pay;
        if (!studentCode || amountPaid === undefined || Number(amountPaid) <= 0 || !paymentMethod) continue;

        const cleanCode = studentCode.trim().toUpperCase();
        uniqueStudentCodes.add(cleanCode);

        const newTxRef = adminDb.collection('feeTransactions').doc();
        const newTx = {
          transactionId: newTxRef.id,
          studentCode: cleanCode,
          installmentId: installmentId || '',
          amountPaid: Number(amountPaid),
          paymentMethod,
          referenceNumber: referenceNumber || '',
          receiptUrl: '',
          recordedBy: admin.decodedToken?.email || 'admin',
          timestamp: new Date().toISOString()
        };

        batch.set(newTxRef, newTx);
        results.push(newTx);
      }

      if (results.length > 0) {
        await batch.commit();
        // Sync student fees in parallel for all unique student codes affected
        await Promise.all(
          Array.from(uniqueStudentCodes).map(code => syncStudentFees(code))
        );
      }

      return NextResponse.json({ success: true, count: results.length });
    }

    if (action === 'create') {
      const { studentCode, installmentId, amountPaid, paymentMethod, referenceNumber, receiptUrl, timestamp } = transactionData;
      if (!studentCode || amountPaid === undefined || !paymentMethod) {
        return NextResponse.json({ error: 'Missing required transaction fields.' }, { status: 400 });
      }

      const cleanCode = studentCode.trim().toUpperCase();
      const newTxRef = adminDb.collection('feeTransactions').doc();
      const newTx = {
        transactionId: newTxRef.id,
        studentCode: cleanCode,
        installmentId: installmentId || '',
        amountPaid: Number(amountPaid),
        paymentMethod,
        referenceNumber: referenceNumber || '',
        receiptUrl: receiptUrl || '',
        recordedBy: admin.decodedToken?.email || 'admin',
        timestamp: timestamp || new Date().toISOString()
      };

      await newTxRef.set(newTx);
      await syncStudentFees(cleanCode);

      return NextResponse.json({ success: true, transaction: newTx });
    }

    if (action === 'edit') {
      if (!transactionId) {
        return NextResponse.json({ error: 'Missing transactionId.' }, { status: 400 });
      }
      const { studentCode, installmentId, amountPaid, paymentMethod, referenceNumber, receiptUrl, timestamp } = transactionData;
      if (!studentCode || amountPaid === undefined || !paymentMethod) {
        return NextResponse.json({ error: 'Missing required transaction fields.' }, { status: 400 });
      }

      const cleanCode = studentCode.trim().toUpperCase();
      const txRef = adminDb.collection('feeTransactions').doc(transactionId);
      
      await txRef.update({
        installmentId: installmentId || '',
        amountPaid: Number(amountPaid),
        paymentMethod,
        referenceNumber: referenceNumber || '',
        receiptUrl: receiptUrl || '',
        timestamp: timestamp || new Date().toISOString()
      });

      await syncStudentFees(cleanCode);
      return NextResponse.json({ success: true, message: 'Transaction updated successfully.' });
    }

    if (action === 'delete') {
      if (!transactionId) {
        return NextResponse.json({ error: 'Missing transactionId.' }, { status: 400 });
      }
      
      const txRef = adminDb.collection('feeTransactions').doc(transactionId);
      const txSnap = await txRef.get();
      if (!txSnap.exists) {
        return NextResponse.json({ error: 'Transaction not found.' }, { status: 404 });
      }

      const cleanCode = txSnap.data()?.studentCode;
      await txRef.delete();

      if (cleanCode) {
        await syncStudentFees(cleanCode);
      }
      return NextResponse.json({ success: true, message: 'Transaction deleted successfully.' });
    }

    return NextResponse.json({ error: 'Invalid action.' }, { status: 400 });
  } catch (error: any) {
    console.error('API POST fee transactions error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

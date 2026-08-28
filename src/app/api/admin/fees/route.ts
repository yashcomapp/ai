import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { getDateKeyIST as getISTDateString } from '@/lib/dateUtils';

export const dynamic = 'force-dynamic';

// Function to synchronize student fees aggregate values (same logic as transactions sync)
async function recalculateStudentFeeStats(studentCode: string) {
  const studentCodeUpper = studentCode.trim().toUpperCase();
  const feeRef = adminDb.collection('studentFees').doc(studentCodeUpper);
  const feeDoc = await feeRef.get();
  
  if (!feeDoc.exists) return;
  const feeData = feeDoc.data()!;

  const txSnap = await adminDb.collection('feeTransactions')
    .where('studentCode', '==', studentCodeUpper)
    .get();
  const transactions = txSnap.docs.map(doc => doc.data());

  const totalPaidAmount = transactions.reduce((sum, tx) => sum + Number(tx.amountPaid || 0), 0);
  const netPayableAmount = Number(feeData.netPayableAmount || feeData.totalPackageAmount || 0);
  const outstandingAmount = Math.max(0, netPayableAmount - totalPaidAmount);

  const paymentsByInst: Record<string, number> = {};
  let regPaidTotal = 0;

  transactions.forEach(tx => {
    if (tx.installmentId === 'registration') {
      regPaidTotal += Number(tx.amountPaid || 0);
    } else if (tx.installmentId) {
      paymentsByInst[tx.installmentId] = (paymentsByInst[tx.installmentId] || 0) + Number(tx.amountPaid || 0);
    }
  });

  const regFeeData = feeData.registrationFee || { amount: 0, status: 'pending' };
  const regStatus = regPaidTotal >= Number(regFeeData.amount || 0) ? 'paid' : 'pending';
  const updatedRegFee = {
    ...regFeeData,
    status: regStatus,
    paidAt: regStatus === 'paid' ? (regFeeData.paidAt || new Date().toISOString()) : null
  };

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
      if (inst.dueDate && inst.dueDate < todayStr) {
        status = 'overdue';
        hasOverdueInstallment = true;
      }
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

  let feeStatus = 'unpaid';
  if (totalPaidAmount >= netPayableAmount) {
    feeStatus = 'fully_paid';
  } else if (totalPaidAmount > 0) {
    feeStatus = 'partially_paid';
  }

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

    // 1. Fetch all student profiles
    const studentsSnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .get();
    const students = studentsSnap.docs.map(doc => {
      const d = doc.data();
      return {
        uid: doc.id,
        name: d.name || '',
        studentCode: d.studentCode || '',
        email: d.email || '',
        batchId: d.batchId || '',
        classNum: d.class || d.classNum || '',
        status: d.status || 'active'
      };
    }).filter(s => s.status === 'active');

    // 2. Fetch existing student fees records
    const feesSnap = await adminDb.collection('studentFees').get();
    const feesMap = new Map<string, any>();
    feesSnap.docs.forEach(doc => {
      feesMap.set(doc.id.toUpperCase(), { id: doc.id, ...doc.data() });
    });

    if (studentCode) {
      const codeUpper = studentCode.trim().toUpperCase();
      const feeRecord = feesMap.get(codeUpper) || null;
      return NextResponse.json({ success: true, feeRecord });
    }

    // Combine student list with their fee statuses
    const studentsWithFees = students.map(s => {
      const codeUpper = s.studentCode.toUpperCase();
      const fee = feesMap.get(codeUpper) || null;
      return {
        ...s,
        fee
      };
    });

    return NextResponse.json({ success: true, students: studentsWithFees });
  } catch (error: any) {
    console.error('API GET student fees error:', error);
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
    const { action, studentCode, feeData } = body;

    if (action === 'saveStudentFee') {
      if (!studentCode || !feeData) {
        return NextResponse.json({ error: 'Missing studentCode or feeData.' }, { status: 400 });
      }

      const cleanCode = studentCode.trim().toUpperCase();
      const feeRef = adminDb.collection('studentFees').doc(cleanCode);

      const netPayable = Number(feeData.totalPackageAmount || 0) - Number(feeData.discountAmount || 0);

      // Save custom installments list
      const installments = Array.isArray(feeData.installments) ? feeData.installments : [];
      const formattedInstallments = installments.map((inst: any, idx: number) => ({
        installmentId: inst.installmentId || `inst_${idx + 1}`,
        installmentNo: idx + 1,
        amount: Number(inst.amount),
        dueDate: inst.dueDate, // YYYY-MM-DD
        status: inst.status || 'pending',
        paidAt: inst.paidAt || null
      }));

      const record = {
        studentCode: cleanCode,
        studentName: feeData.studentName || '',
        classNum: String(feeData.classNum || ''),
        batchId: feeData.batchId || '',
        totalPackageAmount: Number(feeData.totalPackageAmount),
        discountAmount: Number(feeData.discountAmount || 0),
        netPayableAmount: netPayable,
        registrationFee: {
          amount: Number(feeData.registrationFee?.amount || 0),
          status: feeData.registrationFee?.status || 'pending',
          paidAt: feeData.registrationFee?.paidAt || null
        },
        installments: formattedInstallments,
        updatedAt: new Date().toISOString()
      };

      // Set options with merge false to overwrite custom overrides
      await feeRef.set(record);
      
      // Perform recalculation based on actual payment transactions
      await recalculateStudentFeeStats(cleanCode);

      return NextResponse.json({ success: true, message: 'Student fee configuration saved.' });
    }

    return NextResponse.json({ error: 'Invalid action.' }, { status: 400 });
  } catch (error: any) {
    console.error('API POST student fees error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

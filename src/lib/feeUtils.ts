import { getDateKeyIST } from '@/lib/dateUtils';
import { safeNumber } from '@/lib/validationUtils';

export interface FeeInstallment {
  installmentId?: string;
  installmentNo?: number;
  label?: string;
  amount: number;
  dueDate: string;
  status: 'pending' | 'overdue' | 'paid';
  statusOverride?: 'pending' | 'overdue' | 'paid';
  paidAt?: string | null;
  notes?: string;
}

export interface StudentFeeRecord {
  id?: string;
  studentCode: string;
  totalPackageAmount: number;
  discountAmount: number;
  netPayableAmount: number;
  totalPaidAmount: number;
  outstandingAmount: number;
  feeStatus: 'unpaid' | 'partially_paid' | 'fully_paid' | 'exempted';
  hasOverdueInstallment: boolean;
  nextInstallmentDueDate: string | null;
  installments: FeeInstallment[];
  academicYear?: string;
  createdAt?: any;
  updatedAt?: any;
  [key: string]: any;
}

/**
 * Single Source of Truth (SSOT) fee record normalization.
 * Dynamically computes installment overdue status based on current IST date.
 * Zero-cost in-memory evaluation on read and write.
 */
export function normalizeStudentFeeRecord(
  feeData: any,
  transactions: any[] = []
): StudentFeeRecord {
  if (!feeData) return feeData;

  const todayStr = getDateKeyIST();
  const netPayableAmount = safeNumber(feeData.netPayableAmount, safeNumber(feeData.totalPackageAmount, 0));

  // 1. Calculate transaction sums by installment
  const paymentsByInst: Record<string, number> = {};
  let totalTxPaidAmount = 0;

  if (Array.isArray(transactions) && transactions.length > 0) {
    transactions.forEach(tx => {
      const amt = safeNumber(tx.amountPaid, 0);
      totalTxPaidAmount += amt;
      if (tx.installmentId) {
        paymentsByInst[tx.installmentId] = (paymentsByInst[tx.installmentId] || 0) + amt;
      }
    });
  }

  const rawInstallments = Array.isArray(feeData.installments) ? feeData.installments : [];
  let hasOverdueInstallment = false;
  let nextInstallmentDueDate: string | null = null;

  const installments: FeeInstallment[] = rawInstallments.map((inst: any, idx: number) => {
    const instId = inst.installmentId || `inst_${idx + 1}`;
    const paidForInst = paymentsByInst[instId] || 0;
    const targetAmount = safeNumber(inst.amount, 0);

    let status: 'pending' | 'overdue' | 'paid' = 'pending';
    let paidAt = inst.paidAt || null;

    // Check if fully paid
    if (paidForInst >= targetAmount && targetAmount > 0) {
      status = 'paid';
      paidAt = paidAt || new Date().toISOString();
    } else if (inst.statusOverride === 'paid' || inst.status === 'paid') {
      status = 'paid';
      paidAt = paidAt || new Date().toISOString();
    } else if (inst.statusOverride === 'overdue') {
      status = 'overdue';
      hasOverdueInstallment = true;
    } else if (inst.statusOverride === 'pending') {
      status = 'pending';
      if (!nextInstallmentDueDate || (inst.dueDate && inst.dueDate < nextInstallmentDueDate)) {
        nextInstallmentDueDate = inst.dueDate;
      }
    } else {
      // Dynamic evaluation based on due date vs current date (IST)
      if (inst.dueDate && inst.dueDate < todayStr) {
        status = 'overdue';
        hasOverdueInstallment = true;
      } else {
        status = 'pending';
        if (!nextInstallmentDueDate || (inst.dueDate && inst.dueDate < nextInstallmentDueDate)) {
          nextInstallmentDueDate = inst.dueDate;
        }
      }
    }

    if (status === 'overdue') {
      hasOverdueInstallment = true;
    }

    return {
      ...inst,
      installmentId: instId,
      installmentNo: idx + 1,
      amount: targetAmount,
      dueDate: inst.dueDate || '',
      status,
      paidAt
    };
  });

  const directPaidSum = installments
    .filter(i => i.status === 'paid')
    .reduce((sum, i) => sum + safeNumber(i.amount, 0), 0);

  const totalPaidAmount = Math.max(
    totalTxPaidAmount,
    safeNumber(feeData.totalPaidAmount, directPaidSum)
  );
  const outstandingAmount = Math.max(0, netPayableAmount - totalPaidAmount);

  let feeStatus: 'unpaid' | 'partially_paid' | 'fully_paid' | 'exempted' = 'unpaid';
  const allPaid = installments.length > 0 && installments.every(i => i.status === 'paid');

  if (netPayableAmount === 0) {
    feeStatus = 'exempted';
  } else if ((totalPaidAmount >= netPayableAmount && netPayableAmount > 0) || allPaid) {
    feeStatus = 'fully_paid';
  } else if (totalPaidAmount > 0 || installments.some(i => i.status === 'paid')) {
    feeStatus = 'partially_paid';
  }

  return {
    ...feeData,
    totalPaidAmount,
    outstandingAmount,
    feeStatus,
    hasOverdueInstallment,
    nextInstallmentDueDate,
    installments
  };
}

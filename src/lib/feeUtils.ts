import { getDateKeyIST } from '@/lib/dateUtils';
import { safeNumber } from '@/lib/validationUtils';

export interface FeeInstallment {
  installmentId?: string;
  installmentNo?: number;
  label?: string;
  amount: number;
  paidAmount?: number;
  remainingAmount?: number;
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
 * Features automatic FIFO waterfall allocation for unallocated payments and excess roll-forward.
 * Zero-cost in-memory evaluation on read and write.
 */
export function normalizeStudentFeeRecord(
  feeData: any,
  transactions: any[] = []
): StudentFeeRecord {
  if (!feeData) return feeData;

  const todayStr = getDateKeyIST();
  const netPayableAmount = safeNumber(feeData.netPayableAmount, safeNumber(feeData.totalPackageAmount, 0));

  // 1. Separate transaction payments into specific installment payments and unallocated pool
  const specificPayments: Record<string, number> = {};
  let totalTxPaidAmount = 0;
  let unallocatedPool = 0;

  if (Array.isArray(transactions) && transactions.length > 0) {
    transactions.forEach(tx => {
      const amt = safeNumber(tx.amountPaid, 0);
      totalTxPaidAmount += amt;
      const instId = typeof tx.installmentId === 'string' ? tx.installmentId.trim() : '';
      if (instId) {
        specificPayments[instId] = (specificPayments[instId] || 0) + amt;
      } else {
        unallocatedPool += amt;
      }
    });
  }

  // If base fee record has a higher totalPaidAmount than transactions ledger sum, treat difference as unallocated
  const baseTotalPaid = safeNumber(feeData.totalPaidAmount, 0);
  if (baseTotalPaid > totalTxPaidAmount) {
    unallocatedPool += (baseTotalPaid - totalTxPaidAmount);
    totalTxPaidAmount = baseTotalPaid;
  }

  const rawInstallments = Array.isArray(feeData.installments) ? feeData.installments : [];

  // Pass 1: Apply specific installment payments up to required amount; roll forward any excess into unallocatedPool
  const allocatedByInst: Record<string, number> = {};

  rawInstallments.forEach((inst: any, idx: number) => {
    const instId = inst.installmentId || `inst_${idx + 1}`;
    const targetAmount = safeNumber(inst.amount, 0);
    const specificAmt = specificPayments[instId] || 0;

    if (specificAmt > targetAmount) {
      allocatedByInst[instId] = targetAmount;
      unallocatedPool += (specificAmt - targetAmount); // Roll forward excess to unallocated pool
    } else {
      allocatedByInst[instId] = specificAmt;
    }
  });

  // Pass 2: Waterfall / FIFO allocate the unallocatedPool to remaining unpaid installments
  rawInstallments.forEach((inst: any, idx: number) => {
    const instId = inst.installmentId || `inst_${idx + 1}`;
    const targetAmount = safeNumber(inst.amount, 0);
    const currentlyAllocated = allocatedByInst[instId] || 0;
    const needed = Math.max(0, targetAmount - currentlyAllocated);

    if (needed > 0 && unallocatedPool > 0) {
      const allocateFromPool = Math.min(unallocatedPool, needed);
      allocatedByInst[instId] = currentlyAllocated + allocateFromPool;
      unallocatedPool -= allocateFromPool;
    }
  });

  // Pass 3: Determine installment statuses, overdue flags, and next due date
  let hasOverdueInstallment = false;
  let nextInstallmentDueDate: string | null = null;
  const isFullyPaidOverall = (totalTxPaidAmount >= netPayableAmount && netPayableAmount > 0) || (netPayableAmount === 0);

  const installments: FeeInstallment[] = rawInstallments.map((inst: any, idx: number) => {
    const instId = inst.installmentId || `inst_${idx + 1}`;
    const paidForInst = allocatedByInst[instId] || 0;
    const targetAmount = safeNumber(inst.amount, 0);

    let status: 'pending' | 'overdue' | 'paid' = 'pending';
    let paidAt = inst.paidAt || null;

    // Check if fully paid (either overall, covered by allocated amount, or explicit override)
    if (isFullyPaidOverall || (paidForInst >= targetAmount && targetAmount > 0)) {
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
      paidAmount: paidForInst,
      remainingAmount: Math.max(0, targetAmount - paidForInst),
      dueDate: inst.dueDate || '',
      status,
      paidAt
    };
  });

  const totalPaidAmount = Math.max(
    totalTxPaidAmount,
    safeNumber(feeData.totalPaidAmount, 0)
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

  if (feeStatus === 'fully_paid' || feeStatus === 'exempted') {
    hasOverdueInstallment = false;
    nextInstallmentDueDate = null;
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

import React from 'react';

export interface StudentFeeRecord {
  uid: string;
  name: string;
  studentCode: string;
  email: string;
  batchId: string;
  batchName?: string;
  classNum: string;
  fee: {
    totalPackageAmount: number;
    discountAmount: number;
    netPayableAmount: number;
    totalPaidAmount: number;
    outstandingAmount: number;
    feeStatus?: string;
    status?: string;
    hasOverdueInstallment?: boolean;
    installments?: any[];
  } | null;
}

/**
 * Returns numeric weight for student fee ledger statuses for consistent sorting:
 * overdue (4) -> partially_paid (3) -> fully_paid/exempted (2) -> pending (1) -> unconfigured (0)
 */
export function getStatusWeight(s: any): number {
  if (!s) return 0;
  const fee = s.fee || (s.totalPackageAmount !== undefined ? s : null);
  if (!fee || fee.totalPackageAmount === undefined) return 0;
  if (fee.hasOverdueInstallment || fee.status === 'overdue') return 4;
  if (fee.feeStatus === 'partially_paid' || fee.status === 'partial') return 3;
  if (fee.feeStatus === 'fully_paid' || fee.feeStatus === 'exempted' || fee.status === 'paid' || fee.netPayableAmount === 0) return 2;
  return 1;
}

/**
 * Calculates timeliness remarks between payment date and installment due date.
 */
export function getLateRemarks(dueDateStr?: string, paymentDateStr?: string): { isLate: boolean; daysLate: number; remark: string } | null {
  if (!dueDateStr || !paymentDateStr) return null;
  const due = new Date(dueDateStr);
  const pay = new Date(paymentDateStr);
  if (isNaN(due.getTime()) || isNaN(pay.getTime())) return null;

  const diffDays = Math.floor((pay.getTime() - due.getTime()) / (1000 * 60 * 60 * 24));
  if (diffDays > 0) {
    return { isLate: true, daysLate: diffDays, remark: `Paid ${diffDays} day${diffDays > 1 ? 's' : ''} late` };
  }
  return { isLate: false, daysLate: 0, remark: 'Paid on time' };
}

/**
 * Returns user-facing late string (e.g. 'Late by 3 days') or empty string if on time.
 */
export function getLateDaysString(dueDateStr?: string, paymentDateStr?: string): string {
  const res = getLateRemarks(dueDateStr, paymentDateStr);
  if (!res || !res.isLate) return '';
  return `Late by ${res.daysLate} day${res.daysLate > 1 ? 's' : ''}`;
}

/**
 * Shared Sortable Table Header renderer for Fees management and Journal
 */
export function renderSortHeader(
  label: string,
  field: string,
  currentField: string,
  currentDir: 'asc' | 'desc',
  onSort: (f: any) => void,
  alignRight = false
) {
  const isCurrent = currentField === field;
  return (
    <th
      key={field}
      onClick={() => onSort(field)}
      style={{
        padding: '12px 14px',
        textAlign: alignRight ? 'right' : 'left',
        cursor: 'pointer',
        userSelect: 'none',
        whiteSpace: 'nowrap',
        color: isCurrent ? 'var(--accent)' : 'var(--text-muted)',
        background: isCurrent ? 'var(--surface-3)' : 'transparent',
        transition: 'all 0.15s ease',
        fontSize: '11px',
        fontWeight: 800,
        textTransform: 'uppercase'
      }}
      title={`Sort by ${label}`}
    >
      <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', justifyContent: alignRight ? 'flex-end' : 'flex-start' }}>
        {label}
        <span style={{ fontSize: '10px', opacity: isCurrent ? 1 : 0.35 }}>
          {isCurrent ? (currentDir === 'asc' ? '▲' : '▼') : '↕'}
        </span>
      </span>
    </th>
  );
}

/**
 * Shared API call to delete a fee transaction and adjust balance
 */
export async function deleteFeeTransaction(
  token: string,
  transactionId: string,
  studentCode?: string
): Promise<{ success: boolean; error?: string }> {
  try {
    const res = await fetch('/api/admin/fees/transactions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        action: 'delete',
        transactionId,
        studentCode
      })
    });
    const data = await res.json();
    if (!res.ok || !data.success) {
      return { success: false, error: data.error || 'Failed to delete transaction' };
    }
    return { success: true };
  } catch (err: any) {
    return { success: false, error: err.message || 'Failed to delete transaction' };
  }
}

export interface ConfirmAndDeleteOptions {
  transactionId: string;
  studentCode?: string;
  studentName?: string;
  amount?: number;
  paymentMethod?: string;
  dateStr?: string;
  getToken: () => Promise<string | null | undefined>;
  onSuccess?: () => void | Promise<void>;
  onError?: (errMessage: string) => void;
  onSetDeleting?: (isDeleting: boolean) => void;
}

/**
 * Shared confirmation and deletion lifecycle for fee transactions.
 */
export async function confirmAndDeleteTransaction(options: ConfirmAndDeleteOptions): Promise<boolean> {
  const {
    transactionId,
    studentCode,
    studentName,
    amount,
    paymentMethod,
    dateStr,
    getToken,
    onSuccess,
    onError,
    onSetDeleting
  } = options;

  let confirmMsg = 'Are you sure you want to delete this payment log? Balance will be adjusted.';
  if (studentName || amount !== undefined) {
    const name = studentName || studentCode || 'Student';
    const amtStr = amount !== undefined ? `₹${Number(amount).toLocaleString('en-IN')}` : '';
    const details = [
      `Student: ${name}`,
      amtStr ? `Amount: ${amtStr}` : '',
      paymentMethod ? `Payment Mode: ${paymentMethod}` : '',
      dateStr ? `Date: ${dateStr}` : ''
    ].filter(Boolean).join('\n');
    confirmMsg = `Are you sure you want to delete this transaction?\n\n${details}\n\nThis will permanently remove the transaction and update the student's fee balance.`;
  }

  if (typeof window !== 'undefined' && !window.confirm(confirmMsg)) {
    return false;
  }

  if (onSetDeleting) onSetDeleting(true);
  try {
    const token = await getToken();
    if (!token) throw new Error('Not authenticated');
    const res = await deleteFeeTransaction(token, transactionId, studentCode);
    if (!res.success) {
      const msg = res.error || 'Failed to delete transaction';
      if (onError) onError(msg);
      else if (typeof window !== 'undefined') window.alert(msg);
      return false;
    }
    if (onSuccess) await onSuccess();
    return true;
  } catch (err: any) {
    const msg = err.message || 'Failed to delete transaction';
    if (onError) onError(msg);
    else if (typeof window !== 'undefined') window.alert(msg);
    return false;
  } finally {
    if (onSetDeleting) onSetDeleting(false);
  }
}


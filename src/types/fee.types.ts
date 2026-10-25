/**
 * Canonical Fee & Transaction Type Definitions (SSOT).
 */

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

/**
 * Server/Database fee record stored in `fees` collection.
 */
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
 * Client-side table roster row combining student details with nested fee summary.
 */
export interface FeeRosterRow {
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

export interface FeeTransaction {
  id: string;
  studentCode: string;
  studentName?: string;
  amountPaid: number;
  paymentMode: 'cash' | 'upi' | 'bank_transfer' | 'cheque' | 'card' | 'other';
  paymentDate: string;
  receiptNumber?: string;
  installmentId?: string;
  installmentLabel?: string;
  notes?: string;
  recordedBy?: string;
  createdAt?: any;
}

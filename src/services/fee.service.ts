import { adminDb } from '@/lib/firebase/admin';
import { normalizeStudentFeeRecord } from '@/lib/feeUtils';
import { StudentFeeRecord } from '@/types/fee.types';

export class FeeService {
  /**
   * Recalculates student fee ledger status from all recorded transactions
   * and synchronizes the student's status across `studentFees` and `users` collections.
   */
  static async recalculateAndSyncStudentFeeRecord(studentCode: string): Promise<StudentFeeRecord | null> {
    const studentCodeUpper = studentCode.trim().toUpperCase();
    const feeRef = adminDb.collection('studentFees').doc(studentCodeUpper);
    const feeDoc = await feeRef.get();
    
    if (!feeDoc.exists) return null;
    const feeData = feeDoc.data()!;

    const txSnap = await adminDb.collection('feeTransactions')
      .where('studentCode', '==', studentCodeUpper)
      .get();
    const transactions = txSnap.docs.map(doc => doc.data());

    const normalized = normalizeStudentFeeRecord(feeData, transactions);

    await feeRef.update({
      totalPaidAmount: normalized.totalPaidAmount,
      outstandingAmount: normalized.outstandingAmount,
      feeStatus: normalized.feeStatus,
      hasOverdueInstallment: normalized.hasOverdueInstallment,
      nextInstallmentDueDate: normalized.nextInstallmentDueDate,
      installments: normalized.installments,
      updatedAt: new Date().toISOString()
    });

    const studentQuery = await adminDb.collection('users')
      .where('studentCode', '==', studentCodeUpper)
      .where('role', '==', 'student')
      .get();
    if (!studentQuery.empty) {
      await studentQuery.docs[0].ref.update({
        feeStatus: normalized.feeStatus
      });
    }

    return normalized;
  }
}

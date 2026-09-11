'use client';

import React, { useState, useEffect, useMemo } from 'react';
import { formatDateDMY as formatDateStr, getDateKeyIST } from '@/lib/dateUtils';
import DateInputDMY from '@/components/DateInputDMY';

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
    feeStatus: string;
    hasOverdueInstallment: boolean;
    installments?: { installmentId: string; installmentNo: number; amount: number; dueDate: string; status: string; paidAt: string | null }[];
  } | null;
}

export interface Transaction {
  transactionId: string;
  studentCode: string;
  installmentId: string;
  amountPaid: number;
  paymentMethod: string;
  referenceNumber: string;
  receiptUrl: string;
  recordedBy: string;
  timestamp: string;
}

interface FeesJournalProps {
  students: StudentFeeRecord[];
  loadingStudents: boolean;
  getIdToken: () => Promise<string | null>;
  onSelectStudent?: (student: StudentFeeRecord) => void;
}

export default function FeesJournal({
  students,
  loadingStudents,
  getIdToken,
  onSelectStudent
}: FeesJournalProps) {
  // Sub-view Tab State
  const [subView, setSubView] = useState<'batch' | 'date' | 'student'>('batch');

  // All Transactions State (for Date-wise Journal)
  const [allTransactions, setAllTransactions] = useState<Transaction[]>([]);
  const [loadingTransactions, setLoadingTransactions] = useState<boolean>(false);

  // Filters - Date-wise Journal
  const [journalSearch, setJournalSearch] = useState('');
  const [journalClassFilter, setJournalClassFilter] = useState('ALL');
  const [journalMethodFilter, setJournalMethodFilter] = useState('ALL');
  const [dateFrom, setDateFrom] = useState<string>('');
  const [dateTo, setDateTo] = useState<string>('');

  // Filters - Student-wise Balances
  const [studentSearch, setStudentSearch] = useState('');
  const [studentClassFilter, setStudentClassFilter] = useState('ALL');
  const [studentStatusFilter, setStudentStatusFilter] = useState('ALL');

  // Sorting - Batch-wise
  const [batchSortField, setBatchSortField] = useState<'classNum' | 'students' | 'expected' | 'paid' | 'outstanding' | 'percent' | 'overdue'>('classNum');
  const [batchSortDir, setBatchSortDir] = useState<'asc' | 'desc'>('asc');

  // Sorting - Date-wise
  const [dateSortField, setDateSortField] = useState<'timestamp' | 'studentName' | 'classNum' | 'amountPaid' | 'paymentMethod' | 'recordedBy'>('timestamp');
  const [dateSortDir, setDateSortDir] = useState<'asc' | 'desc'>('desc');

  // Sorting - Student-wise
  const [studentSortField, setStudentSortField] = useState<'name' | 'classNum' | 'package' | 'discount' | 'netDues' | 'paid' | 'outstanding' | 'status' | 'lastPayment'>('name');
  const [studentSortDir, setStudentSortDir] = useState<'asc' | 'desc'>('asc');

  // Fetch all transactions for the date-wise ledger
  const fetchAllTransactions = async () => {
    setLoadingTransactions(true);
    try {
      const token = await getIdToken();
      if (!token) return;
      const res = await fetch('/api/admin/fees/transactions', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await res.json();
      if (data.success && Array.isArray(data.transactions)) {
        setAllTransactions(data.transactions);
      }
    } catch (err) {
      console.error('Failed to load all fee transactions:', err);
    } finally {
      setLoadingTransactions(false);
    }
  };

  useEffect(() => {
    fetchAllTransactions();
  }, []);

  // Map studentCode -> Student Profile
  const studentMap = useMemo(() => {
    const map = new Map<string, StudentFeeRecord>();
    students.forEach(s => {
      if (s.studentCode) {
        map.set(s.studentCode.toUpperCase(), s);
      }
    });
    return map;
  }, [students]);

  // Map studentCode -> Last Payment Timestamp
  const studentLastPaymentMap = useMemo(() => {
    const map = new Map<string, string>();
    allTransactions.forEach(tx => {
      const code = tx.studentCode?.toUpperCase();
      if (!code) return;
      const current = map.get(code);
      if (!current || new Date(tx.timestamp).getTime() > new Date(current).getTime()) {
        map.set(code, tx.timestamp);
      }
    });
    return map;
  }, [allTransactions]);

  // Helper for late remarks
  const getLateRemarks = (studentCode: string, installmentId?: string, paymentDateStr?: string) => {
    if (!paymentDateStr) return '';
    const student = studentMap.get(studentCode?.toUpperCase());
    if (!student?.fee?.installments) return '';

    const inst = student.fee.installments.find(i => (i.installmentId || `inst_${i.installmentNo}`) === installmentId);
    if (!inst || !inst.dueDate) return '';

    try {
      const due = new Date(inst.dueDate);
      const pay = new Date(paymentDateStr);
      if (isNaN(due.getTime()) || isNaN(pay.getTime())) return '';

      const dueUtc = Date.UTC(due.getFullYear(), due.getMonth(), due.getDate());
      const payUtc = Date.UTC(pay.getFullYear(), pay.getMonth(), pay.getDate());

      const diffDays = Math.floor((payUtc - dueUtc) / (1000 * 60 * 60 * 24));
      if (diffDays > 0) {
        return `Late by ${diffDays} day${diffDays > 1 ? 's' : ''}`;
      } else {
        return 'On Time';
      }
    } catch {
      return '';
    }
  };

  // Macro Summary Calculations (Total So Far)
  const macroSummary = useMemo(() => {
    let totalExpected = 0;
    let totalCollected = 0;
    let totalOutstanding = 0;
    let totalStudents = students.length;
    let fullyPaidCount = 0;
    let partiallyPaidCount = 0;
    let unpaidCount = 0;
    let overdueCount = 0;

    students.forEach(s => {
      const net = s.fee?.netPayableAmount ?? s.fee?.totalPackageAmount ?? 0;
      const paid = s.fee?.totalPaidAmount ?? 0;
      const outstanding = s.fee?.outstandingAmount ?? Math.max(0, net - paid);

      totalExpected += net;
      totalCollected += paid;
      totalOutstanding += outstanding;

      if (s.fee?.hasOverdueInstallment) {
        overdueCount++;
      }
      if (s.fee?.feeStatus === 'fully_paid' || (net > 0 && paid >= net)) {
        fullyPaidCount++;
      } else if (s.fee?.feeStatus === 'partially_paid' || (paid > 0 && paid < net)) {
        partiallyPaidCount++;
      } else {
        unpaidCount++;
      }
    });

    const collectionPercent = totalExpected > 0 ? Math.min(100, Math.round((totalCollected / totalExpected) * 100)) : 0;

    return {
      totalExpected,
      totalCollected,
      totalOutstanding,
      totalStudents,
      fullyPaidCount,
      partiallyPaidCount,
      unpaidCount,
      overdueCount,
      collectionPercent
    };
  }, [students]);

  // Batch-wise Aggregations
  const batchSummaries = useMemo(() => {
    const classGroups: Record<string, {
      classNum: string;
      totalStudents: number;
      expected: number;
      paid: number;
      outstanding: number;
      fullyPaid: number;
      partiallyPaid: number;
      unpaid: number;
      overdue: number;
    }> = {};

    students.forEach(s => {
      const cls = String(s.classNum || 'Unassigned');
      if (!classGroups[cls]) {
        classGroups[cls] = {
          classNum: cls,
          totalStudents: 0,
          expected: 0,
          paid: 0,
          outstanding: 0,
          fullyPaid: 0,
          partiallyPaid: 0,
          unpaid: 0,
          overdue: 0
        };
      }

      const net = s.fee?.netPayableAmount ?? s.fee?.totalPackageAmount ?? 0;
      const paid = s.fee?.totalPaidAmount ?? 0;
      const outstanding = s.fee?.outstandingAmount ?? Math.max(0, net - paid);

      classGroups[cls].totalStudents += 1;
      classGroups[cls].expected += net;
      classGroups[cls].paid += paid;
      classGroups[cls].outstanding += outstanding;

      if (s.fee?.hasOverdueInstallment) {
        classGroups[cls].overdue += 1;
      }
      if (s.fee?.feeStatus === 'fully_paid' || (net > 0 && paid >= net)) {
        classGroups[cls].fullyPaid += 1;
      } else if (s.fee?.feeStatus === 'partially_paid' || (paid > 0 && paid < net)) {
        classGroups[cls].partiallyPaid += 1;
      } else {
        classGroups[cls].unpaid += 1;
      }
    });

    return Object.values(classGroups).map(g => ({
      ...g,
      percent: g.expected > 0 ? Math.round((g.paid / g.expected) * 100) : 0
    }));
  }, [students]);

  // Sorted Batch Summaries
  const sortedBatches = useMemo(() => {
    return [...batchSummaries].sort((a, b) => {
      let valA: any = 0;
      let valB: any = 0;

      if (batchSortField === 'classNum') {
        valA = Number(a.classNum) || 999;
        valB = Number(b.classNum) || 999;
      } else if (batchSortField === 'students') {
        valA = a.totalStudents;
        valB = b.totalStudents;
      } else {
        valA = a[batchSortField];
        valB = b[batchSortField];
      }

      if (valA < valB) return batchSortDir === 'asc' ? -1 : 1;
      if (valA > valB) return batchSortDir === 'asc' ? 1 : -1;
      return 0;
    });
  }, [batchSummaries, batchSortField, batchSortDir]);

  // Filtered & Sorted Date-wise Transactions
  const filteredTransactions = useMemo(() => {
    return allTransactions.filter(tx => {
      const student = studentMap.get(tx.studentCode?.toUpperCase());
      const studentName = student?.name || '';
      const classNum = String(student?.classNum || '');

      // Search match
      if (journalSearch.trim()) {
        const query = journalSearch.toLowerCase();
        const matchName = studentName.toLowerCase().includes(query);
        const matchRef = (tx.referenceNumber || '').toLowerCase().includes(query);
        const matchRec = (tx.recordedBy || '').toLowerCase().includes(query);
        if (!matchName && !matchRef && !matchRec) return false;
      }

      // Class filter
      if (journalClassFilter !== 'ALL' && classNum !== journalClassFilter) {
        return false;
      }

      // Method filter
      if (journalMethodFilter !== 'ALL' && tx.paymentMethod?.toLowerCase() !== journalMethodFilter.toLowerCase()) {
        return false;
      }

      // Date Range filter
      if (dateFrom) {
        const txDateKey = getDateKeyIST(tx.timestamp);
        if (txDateKey < dateFrom) return false;
      }
      if (dateTo) {
        const txDateKey = getDateKeyIST(tx.timestamp);
        if (txDateKey > dateTo) return false;
      }

      return true;
    }).sort((a, b) => {
      const studentA = studentMap.get(a.studentCode?.toUpperCase());
      const studentB = studentMap.get(b.studentCode?.toUpperCase());

      let valA: any = '';
      let valB: any = '';

      if (dateSortField === 'timestamp') {
        valA = new Date(a.timestamp).getTime() || 0;
        valB = new Date(b.timestamp).getTime() || 0;
      } else if (dateSortField === 'studentName') {
        valA = (studentA?.name || '').toLowerCase();
        valB = (studentB?.name || '').toLowerCase();
      } else if (dateSortField === 'classNum') {
        valA = Number(studentA?.classNum) || 0;
        valB = Number(studentB?.classNum) || 0;
      } else if (dateSortField === 'amountPaid') {
        valA = Number(a.amountPaid || 0);
        valB = Number(b.amountPaid || 0);
      } else if (dateSortField === 'paymentMethod') {
        valA = (a.paymentMethod || '').toLowerCase();
        valB = (b.paymentMethod || '').toLowerCase();
      } else if (dateSortField === 'recordedBy') {
        valA = (a.recordedBy || '').toLowerCase();
        valB = (b.recordedBy || '').toLowerCase();
      }

      if (valA < valB) return dateSortDir === 'asc' ? -1 : 1;
      if (valA > valB) return dateSortDir === 'asc' ? 1 : -1;
      return 0;
    });
  }, [allTransactions, studentMap, journalSearch, journalClassFilter, journalMethodFilter, dateFrom, dateTo, dateSortField, dateSortDir]);

  // Total collected in current date-wise filter view
  const filteredJournalTotal = useMemo(() => {
    return filteredTransactions.reduce((sum, tx) => sum + Number(tx.amountPaid || 0), 0);
  }, [filteredTransactions]);

  // Filtered & Sorted Student-wise Balances
  const filteredStudents = useMemo(() => {
    return students.filter(s => {
      // Search
      if (studentSearch.trim()) {
        const q = studentSearch.toLowerCase();
        if (!s.name.toLowerCase().includes(q) && !s.email.toLowerCase().includes(q)) {
          return false;
        }
      }

      // Class filter
      if (studentClassFilter !== 'ALL' && String(s.classNum) !== studentClassFilter) {
        return false;
      }

      // Status filter
      if (studentStatusFilter !== 'ALL') {
        if (studentStatusFilter === 'overdue' && !s.fee?.hasOverdueInstallment) return false;
        if (studentStatusFilter === 'fully_paid' && s.fee?.feeStatus !== 'fully_paid') return false;
        if (studentStatusFilter === 'partially_paid' && s.fee?.feeStatus !== 'partially_paid') return false;
        if (studentStatusFilter === 'unpaid' && (s.fee?.feeStatus === 'fully_paid' || s.fee?.feeStatus === 'partially_paid')) return false;
      }

      return true;
    }).sort((a, b) => {
      let valA: any = '';
      let valB: any = '';

      if (studentSortField === 'name') {
        valA = (a.name || '').toLowerCase();
        valB = (b.name || '').toLowerCase();
      } else if (studentSortField === 'classNum') {
        valA = Number(a.classNum) || 0;
        valB = Number(b.classNum) || 0;
      } else if (studentSortField === 'package') {
        valA = Number(a.fee?.totalPackageAmount ?? -1);
        valB = Number(b.fee?.totalPackageAmount ?? -1);
      } else if (studentSortField === 'discount') {
        valA = Number(a.fee?.discountAmount ?? -1);
        valB = Number(b.fee?.discountAmount ?? -1);
      } else if (studentSortField === 'netDues') {
        valA = Number(a.fee?.netPayableAmount ?? -1);
        valB = Number(b.fee?.netPayableAmount ?? -1);
      } else if (studentSortField === 'paid') {
        valA = Number(a.fee?.totalPaidAmount ?? -1);
        valB = Number(b.fee?.totalPaidAmount ?? -1);
      } else if (studentSortField === 'outstanding') {
        valA = Number(a.fee?.outstandingAmount ?? -1);
        valB = Number(b.fee?.outstandingAmount ?? -1);
      } else if (studentSortField === 'status') {
        const getStatusWeight = (s: StudentFeeRecord) => {
          if (!s.fee) return 0;
          if (s.fee.hasOverdueInstallment) return 4;
          if (s.fee.feeStatus === 'partially_paid') return 3;
          if (s.fee.feeStatus === 'fully_paid') return 2;
          return 1;
        };
        valA = getStatusWeight(a);
        valB = getStatusWeight(b);
      } else if (studentSortField === 'lastPayment') {
        const lastA = studentLastPaymentMap.get(a.studentCode?.toUpperCase()) || '';
        const lastB = studentLastPaymentMap.get(b.studentCode?.toUpperCase()) || '';
        valA = lastA ? new Date(lastA).getTime() : 0;
        valB = lastB ? new Date(lastB).getTime() : 0;
      }

      if (valA < valB) return studentSortDir === 'asc' ? -1 : 1;
      if (valA > valB) return studentSortDir === 'asc' ? 1 : -1;
      return 0;
    });
  }, [students, studentSearch, studentClassFilter, studentStatusFilter, studentSortField, studentSortDir, studentLastPaymentMap]);

  // Filtered Student Totals
  const filteredStudentTotals = useMemo(() => {
    let pkg = 0, disc = 0, net = 0, paid = 0, out = 0;
    filteredStudents.forEach(s => {
      pkg += Number(s.fee?.totalPackageAmount || 0);
      disc += Number(s.fee?.discountAmount || 0);
      net += Number(s.fee?.netPayableAmount || (s.fee?.totalPackageAmount || 0));
      paid += Number(s.fee?.totalPaidAmount || 0);
      out += Number(s.fee?.outstandingAmount || 0);
    });
    return { pkg, disc, net, paid, out };
  }, [filteredStudents]);

  // Unique Classes list
  const uniqueClasses = useMemo(() => {
    const set = new Set<string>();
    students.forEach(s => {
      if (s.classNum) set.add(String(s.classNum));
    });
    return Array.from(set).sort((a, b) => (Number(a) || 0) - (Number(b) || 0));
  }, [students]);

  // Helper Sort Header Renderer
  const renderSortHeader = (
    label: string,
    field: string,
    currentField: string,
    currentDir: 'asc' | 'desc',
    onSort: (f: any) => void,
    alignRight = false
  ) => {
    const isActive = currentField === field;
    return (
      <th
        onClick={() => onSort(field)}
        style={{
          padding: '12px 14px',
          fontSize: '11px',
          fontWeight: 800,
          color: isActive ? 'var(--accent)' : 'var(--text-muted)',
          textTransform: 'uppercase',
          cursor: 'pointer',
          userSelect: 'none',
          textAlign: alignRight ? 'right' : 'left',
          transition: 'color 0.15s ease',
          whiteSpace: 'nowrap'
        }}
        title={`Click to sort by ${label}`}
      >
        <div style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', justifyContent: alignRight ? 'flex-end' : 'flex-start' }}>
          <span>{label}</span>
          <span style={{ fontSize: '10px', opacity: isActive ? 1 : 0.35 }}>
            {isActive ? (currentDir === 'asc' ? '▲' : '▼') : '↕'}
          </span>
        </div>
      </th>
    );
  };

  // CSV Exporters
  const exportJournalCSV = () => {
    const headers = ['Transaction ID', 'Date (IST)', 'Student Name', 'Class', 'Component Split', 'Amount (INR)', 'Payment Mode', 'Reference ID', 'Timeliness', 'Recorded By'];
    const rows = filteredTransactions.map(tx => {
      const student = studentMap.get(tx.studentCode?.toUpperCase());
      const studentName = student?.name || 'Unknown Student';
      const classStr = student?.classNum ? `Class ${student.classNum}` : '--';
      const instStr = tx.installmentId?.startsWith('inst_') ? `Installment #${tx.installmentId.replace('inst_', '')}` : (tx.installmentId || 'Installment #1');
      const lateStr = getLateRemarks(tx.studentCode, tx.installmentId, tx.timestamp);
      const dateStr = `${formatDateStr(tx.timestamp)} ${new Date(tx.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`;

      return [
        `"${tx.transactionId || ''}"`,
        `"${dateStr}"`,
        `"${studentName}"`,
        `"${classStr}"`,
        `"${instStr}"`,
        tx.amountPaid || 0,
        `"${tx.paymentMethod || ''}"`,
        `"${tx.referenceNumber || ''}"`,
        `"${lateStr}"`,
        `"${tx.recordedBy || ''}"`
      ];
    });

    const csvContent = [headers.join(','), ...rows.map(r => r.join(','))].join('\n');
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.setAttribute('href', url);
    link.setAttribute('download', `fees_journal_${getDateKeyIST()}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const exportStudentBalancesCSV = () => {
    const headers = ['Student Name', 'Class', 'Package Fee (INR)', 'Discount (INR)', 'Net Payable (INR)', 'Paid So Far (INR)', 'Balance Outstanding (INR)', 'Fee Status', 'Last Payment Date'];
    const rows = filteredStudents.map(s => {
      const lastPayment = studentLastPaymentMap.get(s.studentCode?.toUpperCase());
      const lastPayStr = lastPayment ? formatDateStr(lastPayment) : 'No Payments';
      const statusStr = s.fee?.hasOverdueInstallment ? 'OVERDUE' : (s.fee?.feeStatus?.toUpperCase() || 'UNCONFIGURED');

      return [
        `"${s.name}"`,
        `"Class ${s.classNum}"`,
        s.fee?.totalPackageAmount || 0,
        s.fee?.discountAmount || 0,
        s.fee?.netPayableAmount || 0,
        s.fee?.totalPaidAmount || 0,
        s.fee?.outstandingAmount || 0,
        `"${statusStr}"`,
        `"${lastPayStr}"`
      ];
    });

    const csvContent = [headers.join(','), ...rows.map(r => r.join(','))].join('\n');
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.setAttribute('href', url);
    link.setAttribute('download', `student_fee_balances_${getDateKeyIST()}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
      
      {/* 1. Macro KPI / Total So Far Summary Bar */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '14px' }}>
        
        {/* Total Expected */}
        <div className="card glass" style={{ padding: '16px 20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', background: 'var(--surface)' }}>
          <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
            💼 Total Expected Fees
          </div>
          <div style={{ fontSize: '1.6rem', fontWeight: 800, color: 'var(--text)', marginTop: '4px' }}>
            ₹{macroSummary.totalExpected.toLocaleString('en-IN')}
          </div>
          <div style={{ fontSize: '11px', color: 'var(--text-faint)', marginTop: '4px' }}>
            Across {macroSummary.totalStudents} enrolled students
          </div>
        </div>

        {/* Total Collected */}
        <div className="card glass" style={{ padding: '16px 20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', background: 'var(--surface)' }}>
          <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--success)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
            💰 Total Collected So Far
          </div>
          <div style={{ fontSize: '1.6rem', fontWeight: 800, color: 'var(--success)', marginTop: '4px' }}>
            ₹{macroSummary.totalCollected.toLocaleString('en-IN')}
          </div>
          <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '4px' }}>
            {macroSummary.fullyPaidCount} fully paid • {macroSummary.partiallyPaidCount} partial
          </div>
        </div>

        {/* Total Balance / Outstanding */}
        <div className="card glass" style={{ padding: '16px 20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', background: 'var(--surface)' }}>
          <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--danger)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
            ⏳ Total Balance Outstanding
          </div>
          <div style={{ fontSize: '1.6rem', fontWeight: 800, color: 'var(--danger)', marginTop: '4px' }}>
            ₹{macroSummary.totalOutstanding.toLocaleString('en-IN')}
          </div>
          <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '4px' }}>
            {macroSummary.overdueCount > 0 ? (
              <span style={{ color: 'var(--danger)', fontWeight: 700 }}>⚠️ {macroSummary.overdueCount} students overdue</span>
            ) : (
              <span>{macroSummary.unpaidCount} unpaid students</span>
            )}
          </div>
        </div>

        {/* Collection % Progress */}
        <div className="card glass" style={{ padding: '16px 20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', background: 'var(--surface)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--accent)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
              📊 Collection Rate
            </div>
            <span className="badge badge-info" style={{ fontSize: '11px', fontWeight: 800 }}>
              {macroSummary.collectionPercent}%
            </span>
          </div>
          <div style={{ width: '100%', height: '8px', background: 'var(--bg-soft)', borderRadius: '999px', overflow: 'hidden', marginTop: '12px' }}>
            <div
              style={{
                width: `${macroSummary.collectionPercent}%`,
                height: '100%',
                background: macroSummary.collectionPercent >= 75 ? 'var(--success)' : macroSummary.collectionPercent >= 40 ? 'var(--accent)' : 'var(--warning)',
                borderRadius: '999px',
                transition: 'width 0.4s ease'
              }}
            />
          </div>
          <div style={{ fontSize: '11px', color: 'var(--text-faint)', marginTop: '8px' }}>
            Target: 100% of academic year dues
          </div>
        </div>

      </div>

      {/* 2. Sub-views Switcher */}
      <div style={{ display: 'flex', gap: '8px', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', flexWrap: 'wrap', alignItems: 'center', justifyContent: 'space-between' }}>
        <div style={{ display: 'flex', gap: '6px' }}>
          <button
            onClick={() => setSubView('batch')}
            style={{
              padding: '8px 16px',
              borderRadius: 'var(--radius)',
              border: '1px solid var(--border-light)',
              background: subView === 'batch' ? 'var(--accent)' : 'var(--surface)',
              color: subView === 'batch' ? '#ffffff' : 'var(--text)',
              fontWeight: 700,
              fontSize: '12px',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              transition: 'all 0.15s ease'
            }}
          >
            <span>Batch-wise Summary</span>
          </button>
          
          <button
            onClick={() => setSubView('date')}
            style={{
              padding: '8px 16px',
              borderRadius: 'var(--radius)',
              border: '1px solid var(--border-light)',
              background: subView === 'date' ? 'var(--accent)' : 'var(--surface)',
              color: subView === 'date' ? '#ffffff' : 'var(--text)',
              fontWeight: 700,
              fontSize: '12px',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              transition: 'all 0.15s ease'
            }}
          >
            <span>Date-wise Journal ({allTransactions.length})</span>
          </button>
          
          <button
            onClick={() => setSubView('student')}
            style={{
              padding: '8px 16px',
              borderRadius: 'var(--radius)',
              border: '1px solid var(--border-light)',
              background: subView === 'student' ? 'var(--accent)' : 'var(--surface)',
              color: subView === 'student' ? '#ffffff' : 'var(--text)',
              fontWeight: 700,
              fontSize: '12px',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              transition: 'all 0.15s ease'
            }}
          >
            <span>Student-wise Balances ({students.length})</span>
          </button>
        </div>

        {/* Quick Refresh / Export Action */}
        <div style={{ display: 'flex', gap: '8px' }}>
          {subView === 'date' && (
            <button
              onClick={exportJournalCSV}
              className="btn btn-secondary"
              style={{ padding: '6px 12px', fontSize: '11px', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '4px' }}
              title="Export filtered date-wise journal entries to CSV"
            >
              📥 Export Journal CSV
            </button>
          )}
          {subView === 'student' && (
            <button
              onClick={exportStudentBalancesCSV}
              className="btn btn-secondary"
              style={{ padding: '6px 12px', fontSize: '11px', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '4px' }}
              title="Export student fee balances to CSV"
            >
              📥 Export Balances CSV
            </button>
          )}
        </div>
      </div>

      {/* 3. SUB-VIEW A: BATCH-WISE SUMMARY */}
      {subView === 'batch' && (
        <div className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', overflow: 'hidden' }}>
          <div style={{ padding: '14px 18px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 800 }}>Class & Batch-wise Fees Collection</h3>
              <p style={{ margin: '2px 0 0 0', fontSize: '11px', color: 'var(--text-muted)' }}>
                Consolidated expected revenue, collections, outstanding balances, and completion rates by class.
              </p>
            </div>
          </div>

          {loadingStudents ? (
            <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '13px' }}>Loading batch breakdown...</div>
          ) : batchSummaries.length === 0 ? (
            <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '13px' }}>No batch data available.</div>
          ) : (
            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                    {renderSortHeader('Class / Batch', 'classNum', batchSortField, batchSortDir, (f) => {
                      if (batchSortField === f) setBatchSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setBatchSortField(f); setBatchSortDir('asc'); }
                    })}
                    {renderSortHeader('Students', 'students', batchSortField, batchSortDir, (f) => {
                      if (batchSortField === f) setBatchSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setBatchSortField(f); setBatchSortDir('asc'); }
                    })}
                    {renderSortHeader('Expected (₹)', 'expected', batchSortField, batchSortDir, (f) => {
                      if (batchSortField === f) setBatchSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setBatchSortField(f); setBatchSortDir('asc'); }
                    }, true)}
                    {renderSortHeader('Collected (₹)', 'paid', batchSortField, batchSortDir, (f) => {
                      if (batchSortField === f) setBatchSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setBatchSortField(f); setBatchSortDir('asc'); }
                    }, true)}
                    {renderSortHeader('Balance (₹)', 'outstanding', batchSortField, batchSortDir, (f) => {
                      if (batchSortField === f) setBatchSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setBatchSortField(f); setBatchSortDir('asc'); }
                    }, true)}
                    {renderSortHeader('Collection %', 'percent', batchSortField, batchSortDir, (f) => {
                      if (batchSortField === f) setBatchSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setBatchSortField(f); setBatchSortDir('asc'); }
                    })}
                    {renderSortHeader('Overdue', 'overdue', batchSortField, batchSortDir, (f) => {
                      if (batchSortField === f) setBatchSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setBatchSortField(f); setBatchSortDir('asc'); }
                    })}
                    <th style={{ padding: '12px 16px', fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', textAlign: 'right' }}>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {sortedBatches.map(b => (
                    <tr key={b.classNum} style={{ borderBottom: '1px solid var(--border-light)' }}>
                      <td style={{ padding: '14px 16px', fontSize: '13px', fontWeight: 800 }}>
                        Class {b.classNum}
                      </td>
                      <td style={{ padding: '14px 16px', fontSize: '13px', color: 'var(--text-muted)' }}>
                        {b.totalStudents} student{b.totalStudents > 1 ? 's' : ''}
                      </td>
                      <td style={{ padding: '14px 16px', fontSize: '13px', fontWeight: 700, textAlign: 'right' }}>
                        ₹{b.expected.toLocaleString('en-IN')}
                      </td>
                      <td style={{ padding: '14px 16px', fontSize: '13px', color: 'var(--success)', fontWeight: 700, textAlign: 'right' }}>
                        ₹{b.paid.toLocaleString('en-IN')}
                      </td>
                      <td style={{ padding: '14px 16px', fontSize: '13px', color: 'var(--danger)', fontWeight: 700, textAlign: 'right' }}>
                        ₹{b.outstanding.toLocaleString('en-IN')}
                      </td>
                      <td style={{ padding: '14px 16px', minWidth: '150px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <div style={{ flex: 1, height: '6px', background: 'var(--bg-soft)', borderRadius: '999px', overflow: 'hidden' }}>
                            <div
                              style={{
                                width: `${b.percent}%`,
                                height: '100%',
                                background: b.percent >= 75 ? 'var(--success)' : b.percent >= 40 ? 'var(--accent)' : 'var(--warning)',
                                borderRadius: '999px'
                              }}
                            />
                          </div>
                          <span style={{ fontSize: '11px', fontWeight: 700, width: '34px', textAlign: 'right' }}>
                            {b.percent}%
                          </span>
                        </div>
                      </td>
                      <td style={{ padding: '14px 16px' }}>
                        {b.overdue > 0 ? (
                          <span className="badge badge-danger" style={{ fontSize: '10px' }}>
                            {b.overdue} OVERDUE
                          </span>
                        ) : (
                          <span className="badge badge-success" style={{ fontSize: '10px' }}>
                            0 OVERDUE
                          </span>
                        )}
                      </td>
                      <td style={{ padding: '14px 16px', textAlign: 'right' }}>
                        <button
                          onClick={() => {
                            setStudentClassFilter(b.classNum);
                            setSubView('student');
                          }}
                          className="btn btn-secondary"
                          style={{ padding: '4px 10px', fontSize: '11px', fontWeight: 600 }}
                        >
                          View Students →
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
                <tfoot>
                  <tr style={{ background: 'var(--bg-soft)', fontWeight: 800, borderTop: '2px solid var(--border-light)' }}>
                    <td style={{ padding: '14px 16px', fontSize: '13px' }}>TOTAL ALL BATCHES</td>
                    <td style={{ padding: '14px 16px', fontSize: '13px' }}>{macroSummary.totalStudents} Students</td>
                    <td style={{ padding: '14px 16px', fontSize: '13px', textAlign: 'right' }}>₹{macroSummary.totalExpected.toLocaleString('en-IN')}</td>
                    <td style={{ padding: '14px 16px', fontSize: '13px', color: 'var(--success)', textAlign: 'right' }}>₹{macroSummary.totalCollected.toLocaleString('en-IN')}</td>
                    <td style={{ padding: '14px 16px', fontSize: '13px', color: 'var(--danger)', textAlign: 'right' }}>₹{macroSummary.totalOutstanding.toLocaleString('en-IN')}</td>
                    <td style={{ padding: '14px 16px', fontSize: '13px' }}>{macroSummary.collectionPercent}% Overall</td>
                    <td style={{ padding: '14px 16px' }}>
                      {macroSummary.overdueCount > 0 ? (
                        <span className="badge badge-danger" style={{ fontSize: '10px' }}>{macroSummary.overdueCount} OVERDUE</span>
                      ) : (
                        <span className="badge badge-success" style={{ fontSize: '10px' }}>0 OVERDUE</span>
                      )}
                    </td>
                    <td style={{ padding: '14px 16px' }}></td>
                  </tr>
                </tfoot>
              </table>
            </div>
          )}
        </div>
      )}

      {/* 4. SUB-VIEW B: DATE-WISE COLLECTION JOURNAL */}
      {subView === 'date' && (
        <div className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', overflow: 'hidden' }}>
          
          {/* Header & Filter Controls */}
          <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '14px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '12px' }}>
              <div>
                <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 800 }}>Date-wise Transaction Ledger</h3>
                <p style={{ margin: '2px 0 0 0', fontSize: '11px', color: 'var(--text-muted)' }}>
                  Chronological record of every installment payment collected across all students.
                </p>
              </div>
              
              {/* Filtered Subtotal Callout */}
              <div style={{ background: 'var(--bg-soft)', padding: '6px 14px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', fontSize: '12px' }}>
                <span>Showing <strong>{filteredTransactions.length}</strong> transactions • Total: </span>
                <strong style={{ color: 'var(--success)' }}>₹{filteredJournalTotal.toLocaleString('en-IN')}</strong>
              </div>
            </div>

            {/* Filter Bar */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(160px, 1fr))', gap: '10px', alignItems: 'flex-end' }}>
              
              {/* Search */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>Search Student / Ref / Admin</label>
                <input
                  type="text"
                  placeholder="e.g. Yash, UPI1293..."
                  value={journalSearch}
                  onChange={(e) => setJournalSearch(e.target.value)}
                  style={{ padding: '7px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '12px' }}
                />
              </div>

              {/* Class Filter */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>Class</label>
                <select
                  value={journalClassFilter}
                  onChange={(e) => setJournalClassFilter(e.target.value)}
                  style={{ padding: '7px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '12px' }}
                >
                  <option value="ALL">All Classes</option>
                  {uniqueClasses.map(cls => (
                    <option key={cls} value={cls}>Class {cls}</option>
                  ))}
                </select>
              </div>

              {/* Payment Mode Filter */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>Payment Mode</label>
                <select
                  value={journalMethodFilter}
                  onChange={(e) => setJournalMethodFilter(e.target.value)}
                  style={{ padding: '7px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '12px' }}
                >
                  <option value="ALL">All Modes</option>
                  <option value="UPI">UPI / GPay</option>
                  <option value="Cash">Cash</option>
                  <option value="Cheque">Cheque</option>
                  <option value="NetBanking">Net Banking</option>
                </select>
              </div>

              {/* Date From */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>From Date</label>
                <DateInputDMY
                  value={dateFrom}
                  onChange={(val) => setDateFrom(val)}
                  style={{ width: '100%' }}
                />
              </div>

              {/* Date To */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>To Date</label>
                <DateInputDMY
                  value={dateTo}
                  onChange={(val) => setDateTo(val)}
                  style={{ width: '100%' }}
                />
              </div>

              {/* Clear Filters Button */}
              {(journalSearch || journalClassFilter !== 'ALL' || journalMethodFilter !== 'ALL' || dateFrom || dateTo) && (
                <div>
                  <button
                    onClick={() => {
                      setJournalSearch('');
                      setJournalClassFilter('ALL');
                      setJournalMethodFilter('ALL');
                      setDateFrom('');
                      setDateTo('');
                    }}
                    className="btn btn-secondary"
                    style={{ padding: '7px 12px', fontSize: '11px', width: '100%' }}
                  >
                    Clear Filters
                  </button>
                </div>
              )}

            </div>
          </div>

          {/* Transactions Table */}
          {loadingTransactions ? (
            <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '13px' }}>Loading transaction ledger...</div>
          ) : filteredTransactions.length === 0 ? (
            <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '13px' }}>
              No transactions match the selected filters.
            </div>
          ) : (
            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                    {renderSortHeader('Date & Time', 'timestamp', dateSortField, dateSortDir, (f) => {
                      if (dateSortField === f) setDateSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setDateSortField(f); setDateSortDir('desc'); }
                    })}
                    {renderSortHeader('Student Name', 'studentName', dateSortField, dateSortDir, (f) => {
                      if (dateSortField === f) setDateSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setDateSortField(f); setDateSortDir('asc'); }
                    })}
                    {renderSortHeader('Class', 'classNum', dateSortField, dateSortDir, (f) => {
                      if (dateSortField === f) setDateSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setDateSortField(f); setDateSortDir('asc'); }
                    })}
                    <th style={{ padding: '12px 14px', fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Component</th>
                    {renderSortHeader('Amount Paid', 'amountPaid', dateSortField, dateSortDir, (f) => {
                      if (dateSortField === f) setDateSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setDateSortField(f); setDateSortDir('desc'); }
                    }, true)}
                    {renderSortHeader('Mode', 'paymentMethod', dateSortField, dateSortDir, (f) => {
                      if (dateSortField === f) setDateSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setDateSortField(f); setDateSortDir('asc'); }
                    })}
                    <th style={{ padding: '12px 14px', fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Ref / Remarks</th>
                    <th style={{ padding: '12px 14px', fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Timeliness</th>
                    {renderSortHeader('Recorded By', 'recordedBy', dateSortField, dateSortDir, (f) => {
                      if (dateSortField === f) setDateSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setDateSortField(f); setDateSortDir('asc'); }
                    })}
                  </tr>
                </thead>
                <tbody>
                  {filteredTransactions.map(tx => {
                    const student = studentMap.get(tx.studentCode?.toUpperCase());
                    const studentName = student?.name || 'Unknown Student';
                    const classNum = student?.classNum || '--';
                    const instStr = tx.installmentId?.startsWith('inst_')
                      ? `Installment #${tx.installmentId.replace('inst_', '')}`
                      : (tx.installmentId === 'registration' ? 'Installment #1' : (tx.installmentId || 'Installment #1'));
                    const lateStr = getLateRemarks(tx.studentCode, tx.installmentId, tx.timestamp);

                    // Clean time formatting helper: avoid false 05:30 AM artifact on date-only UTC timestamps
                    const getTimeString = (ts: string) => {
                      if (!ts) return null;
                      try {
                        const d = new Date(ts);
                        if (isNaN(d.getTime())) return null;
                        if (d.getUTCHours() === 0 && d.getUTCMinutes() === 0 && d.getUTCSeconds() === 0) {
                          return null; // Date-only entry
                        }
                        return d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
                      } catch {
                        return null;
                      }
                    };
                    const timeStr = getTimeString(tx.timestamp);

                    return (
                      <tr key={tx.transactionId} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '12px 14px', fontSize: '12px', whiteSpace: 'nowrap' }}>
                          <div style={{ fontWeight: 600 }}>{formatDateStr(tx.timestamp)}</div>
                          {timeStr && (
                            <div style={{ fontSize: '10px', color: 'var(--text-faint)' }}>
                              {timeStr}
                            </div>
                          )}
                        </td>
                        <td style={{ padding: '12px 14px', fontSize: '13px', fontWeight: 700 }}>
                          {onSelectStudent && student ? (
                            <button
                              onClick={() => onSelectStudent(student)}
                              style={{ border: 'none', background: 'transparent', padding: 0, color: 'var(--accent)', fontWeight: 700, cursor: 'pointer', textAlign: 'left', fontSize: '13px' }}
                              title="Click to view student fee profile"
                            >
                              {studentName}
                            </button>
                          ) : (
                            <span>{studentName}</span>
                          )}
                        </td>
                        <td style={{ padding: '12px 14px', fontSize: '12px', fontWeight: 600 }}>
                          Class {classNum}
                        </td>
                        <td style={{ padding: '12px 14px', fontSize: '12px', color: 'var(--text-muted)' }}>
                          <span className="badge badge-secondary" style={{ fontSize: '10px' }}>
                            {instStr}
                          </span>
                        </td>
                        <td style={{ padding: '12px 14px', fontSize: '13px', color: 'var(--success)', fontWeight: 800, textAlign: 'right', whiteSpace: 'nowrap' }}>
                          ₹{Number(tx.amountPaid || 0).toLocaleString('en-IN')}
                        </td>
                        <td style={{ padding: '12px 14px', fontSize: '12px' }}>
                          <span className="badge badge-info" style={{ fontSize: '10px' }}>
                            {tx.paymentMethod}
                          </span>
                        </td>
                        <td style={{ padding: '12px 14px', fontSize: '12px', color: 'var(--text)' }}>
                          {tx.referenceNumber ? (
                            <span style={{ fontWeight: 600 }}>{tx.referenceNumber}</span>
                          ) : (
                            <span style={{ color: 'var(--text-faint)' }}>--</span>
                          )}
                        </td>
                        <td style={{ padding: '12px 14px', fontSize: '11px' }}>
                          {lateStr.startsWith('Late') ? (
                            <span style={{ color: 'var(--danger)', fontWeight: 700 }}>⚠️ {lateStr}</span>
                          ) : lateStr === 'On Time' ? (
                            <span style={{ color: 'var(--success)', fontWeight: 600 }}>✓ On Time</span>
                          ) : (
                            <span style={{ color: 'var(--text-faint)' }}>--</span>
                          )}
                        </td>
                        <td style={{ padding: '12px 14px', fontSize: '11px', color: 'var(--text-faint)' }}>
                          {tx.recordedBy}
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          )}

        </div>
      )}

      {/* 5. SUB-VIEW C: STUDENT-WISE BALANCES */}
      {subView === 'student' && (
        <div className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', overflow: 'hidden' }}>
          
          {/* Header & Filter Controls */}
          <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '14px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '12px' }}>
              <div>
                <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 800 }}>Student-wise Collection & Balance Report</h3>
                <p style={{ margin: '2px 0 0 0', fontSize: '11px', color: 'var(--text-muted)' }}>
                  Total package fees, scholarships, payments made, remaining balance, and overdue status per student.
                </p>
              </div>

              {/* Filtered Count */}
              <div style={{ background: 'var(--bg-soft)', padding: '6px 14px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', fontSize: '12px' }}>
                <span>Showing <strong>{filteredStudents.length}</strong> of <strong>{students.length}</strong> students</span>
              </div>
            </div>

            {/* Filter Controls */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '10px', alignItems: 'flex-end' }}>
              
              {/* Search */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>Search Student Name</label>
                <input
                  type="text"
                  placeholder="e.g. Adhira, Yash..."
                  value={studentSearch}
                  onChange={(e) => setStudentSearch(e.target.value)}
                  style={{ padding: '7px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '12px' }}
                />
              </div>

              {/* Class Filter */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>Class</label>
                <select
                  value={studentClassFilter}
                  onChange={(e) => setStudentClassFilter(e.target.value)}
                  style={{ padding: '7px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '12px' }}
                >
                  <option value="ALL">All Classes</option>
                  {uniqueClasses.map(cls => (
                    <option key={cls} value={cls}>Class {cls}</option>
                  ))}
                </select>
              </div>

              {/* Status Filter */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>Fee Status</label>
                <select
                  value={studentStatusFilter}
                  onChange={(e) => setStudentStatusFilter(e.target.value)}
                  style={{ padding: '7px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '12px' }}
                >
                  <option value="ALL">All Statuses</option>
                  <option value="overdue">⚠️ Overdue Only</option>
                  <option value="fully_paid">🟢 Fully Paid</option>
                  <option value="partially_paid">🟡 Partially Paid</option>
                  <option value="unpaid">🔴 Unpaid / Pending</option>
                </select>
              </div>

              {/* Clear Filters */}
              {(studentSearch || studentClassFilter !== 'ALL' || studentStatusFilter !== 'ALL') && (
                <div>
                  <button
                    onClick={() => {
                      setStudentSearch('');
                      setStudentClassFilter('ALL');
                      setStudentStatusFilter('ALL');
                    }}
                    className="btn btn-secondary"
                    style={{ padding: '7px 12px', fontSize: '11px', width: '100%' }}
                  >
                    Clear Filters
                  </button>
                </div>
              )}

            </div>
          </div>

          {/* Student Table */}
          {loadingStudents ? (
            <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '13px' }}>Loading student balance sheet...</div>
          ) : filteredStudents.length === 0 ? (
            <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '13px' }}>
              No students match the selected filters.
            </div>
          ) : (
            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                    {renderSortHeader('Student Name', 'name', studentSortField, studentSortDir, (f) => {
                      if (studentSortField === f) setStudentSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setStudentSortField(f); setStudentSortDir('asc'); }
                    })}
                    {renderSortHeader('Class', 'classNum', studentSortField, studentSortDir, (f) => {
                      if (studentSortField === f) setStudentSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setStudentSortField(f); setStudentSortDir('asc'); }
                    })}
                    {renderSortHeader('Package (₹)', 'package', studentSortField, studentSortDir, (f) => {
                      if (studentSortField === f) setStudentSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setStudentSortField(f); setStudentSortDir('asc'); }
                    }, true)}
                    {renderSortHeader('Discount (₹)', 'discount', studentSortField, studentSortDir, (f) => {
                      if (studentSortField === f) setStudentSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setStudentSortField(f); setStudentSortDir('asc'); }
                    }, true)}
                    {renderSortHeader('Net Payable (₹)', 'netDues', studentSortField, studentSortDir, (f) => {
                      if (studentSortField === f) setStudentSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setStudentSortField(f); setStudentSortDir('asc'); }
                    }, true)}
                    {renderSortHeader('Paid (₹)', 'paid', studentSortField, studentSortDir, (f) => {
                      if (studentSortField === f) setStudentSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setStudentSortField(f); setStudentSortDir('asc'); }
                    }, true)}
                    {renderSortHeader('Balance (₹)', 'outstanding', studentSortField, studentSortDir, (f) => {
                      if (studentSortField === f) setStudentSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setStudentSortField(f); setStudentSortDir('asc'); }
                    }, true)}
                    {renderSortHeader('Status', 'status', studentSortField, studentSortDir, (f) => {
                      if (studentSortField === f) setStudentSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setStudentSortField(f); setStudentSortDir('asc'); }
                    })}
                    {renderSortHeader('Last Payment', 'lastPayment', studentSortField, studentSortDir, (f) => {
                      if (studentSortField === f) setStudentSortDir(d => d === 'asc' ? 'desc' : 'asc');
                      else { setStudentSortField(f); setStudentSortDir('asc'); }
                    })}
                    {onSelectStudent && (
                      <th style={{ padding: '12px 14px', fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', textAlign: 'right' }}>Actions</th>
                    )}
                  </tr>
                </thead>
                <tbody>
                  {filteredStudents.map(s => {
                    const lastPayment = studentLastPaymentMap.get(s.studentCode?.toUpperCase());

                    return (
                      <tr key={s.studentCode} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '12px 14px', fontSize: '13px', fontWeight: 700 }}>
                          <div>{s.name}</div>
                        </td>
                        <td style={{ padding: '12px 14px', fontSize: '12px', fontWeight: 600 }}>
                          Class {s.classNum}
                        </td>
                        <td style={{ padding: '12px 14px', fontSize: '13px', fontWeight: 600, textAlign: 'right' }}>
                          ₹{s.fee?.totalPackageAmount !== undefined ? s.fee.totalPackageAmount.toLocaleString('en-IN') : '--'}
                        </td>
                        <td style={{ padding: '12px 14px', fontSize: '13px', color: 'var(--text-muted)', textAlign: 'right' }}>
                          ₹{s.fee?.discountAmount !== undefined ? s.fee.discountAmount.toLocaleString('en-IN') : '0'}
                        </td>
                        <td style={{ padding: '12px 14px', fontSize: '13px', fontWeight: 700, textAlign: 'right' }}>
                          ₹{s.fee?.netPayableAmount !== undefined ? s.fee.netPayableAmount.toLocaleString('en-IN') : '--'}
                        </td>
                        <td style={{ padding: '12px 14px', fontSize: '13px', color: 'var(--success)', fontWeight: 700, textAlign: 'right' }}>
                          ₹{s.fee?.totalPaidAmount !== undefined ? s.fee.totalPaidAmount.toLocaleString('en-IN') : '--'}
                        </td>
                        <td style={{ padding: '12px 14px', fontSize: '13px', color: 'var(--danger)', fontWeight: 700, textAlign: 'right' }}>
                          ₹{s.fee?.outstandingAmount !== undefined ? s.fee.outstandingAmount.toLocaleString('en-IN') : '--'}
                        </td>
                        <td style={{ padding: '12px 14px' }}>
                          {s.fee?.hasOverdueInstallment ? (
                            <span className="badge badge-danger" style={{ fontSize: '10px' }}>OVERDUE</span>
                          ) : s.fee?.feeStatus === 'fully_paid' ? (
                            <span className="badge badge-success" style={{ fontSize: '10px' }}>PAID</span>
                          ) : s.fee?.feeStatus === 'partially_paid' ? (
                            <span className="badge badge-info" style={{ fontSize: '10px' }}>PARTIAL</span>
                          ) : (
                            <span className="badge badge-secondary" style={{ fontSize: '10px' }}>UNCONFIGURED</span>
                          )}
                        </td>
                        <td style={{ padding: '12px 14px', fontSize: '11px', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>
                          {lastPayment ? formatDateStr(lastPayment) : '--'}
                        </td>
                        {onSelectStudent && (
                          <td style={{ padding: '12px 14px', textAlign: 'right' }}>
                            <button
                              onClick={() => onSelectStudent(s)}
                              className="btn btn-secondary"
                              style={{ padding: '4px 8px', fontSize: '11px', fontWeight: 600 }}
                              title="Configure fees or view ledger"
                            >
                              ⚙️ Manage
                            </button>
                          </td>
                        )}
                      </tr>
                    );
                  })}
                </tbody>
                <tfoot>
                  <tr style={{ background: 'var(--bg-soft)', fontWeight: 800, borderTop: '2px solid var(--border-light)' }}>
                    <td style={{ padding: '14px 14px', fontSize: '13px' }}>FILTERED TOTALS</td>
                    <td style={{ padding: '14px 14px', fontSize: '13px' }}>{filteredStudents.length} Students</td>
                    <td style={{ padding: '14px 14px', fontSize: '13px', textAlign: 'right' }}>₹{filteredStudentTotals.pkg.toLocaleString('en-IN')}</td>
                    <td style={{ padding: '14px 14px', fontSize: '13px', textAlign: 'right' }}>₹{filteredStudentTotals.disc.toLocaleString('en-IN')}</td>
                    <td style={{ padding: '14px 14px', fontSize: '13px', textAlign: 'right' }}>₹{filteredStudentTotals.net.toLocaleString('en-IN')}</td>
                    <td style={{ padding: '14px 14px', fontSize: '13px', color: 'var(--success)', textAlign: 'right' }}>₹{filteredStudentTotals.paid.toLocaleString('en-IN')}</td>
                    <td style={{ padding: '14px 14px', fontSize: '13px', color: 'var(--danger)', textAlign: 'right' }}>₹{filteredStudentTotals.out.toLocaleString('en-IN')}</td>
                    <td colSpan={onSelectStudent ? 3 : 2} style={{ padding: '14px 14px' }}></td>
                  </tr>
                </tfoot>
              </table>
            </div>
          )}

        </div>
      )}

    </div>
  );
}

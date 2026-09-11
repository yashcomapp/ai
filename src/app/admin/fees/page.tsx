'use client';

import React, { useState, useEffect, Suspense } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter, useSearchParams } from 'next/navigation';
import { formatDateDMY as formatDateStr, getDateKeyIST } from '@/lib/dateUtils';
import DateInputDMY from '@/components/DateInputDMY';
import FeesJournal from '@/components/admin/FeesJournal';

interface FeeTemplate {
  templateId: string;
  name: string;
  classNum: string;
  totalPackageAmount: number;
  installments: { installmentNo: number; amount: number; dueDate?: string; dueDateOffsetDays?: number }[];
}

interface StudentFeeRecord {
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

interface Transaction {
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

function AdminFeesContent() {
  const { firebaseUser } = useAuth();
  const router = useRouter();
  const searchParams = useSearchParams();
  const tabParam = searchParams.get('tab');

  // Tabs
  const [activeTab, setActiveTab] = useState<'students' | 'templates' | 'mass_entry' | 'journal'>(() => {
    if (tabParam === 'templates' || tabParam === 'mass_entry' || tabParam === 'journal') return tabParam;
    return 'students';
  });

  useEffect(() => {
    if (tabParam && (tabParam === 'students' || tabParam === 'templates' || tabParam === 'mass_entry' || tabParam === 'journal')) {
      setActiveTab(tabParam);
    }
  }, [tabParam]);

  // Bulk Entry State
  const [bulkClass, setBulkClass] = useState('8');
  const [bulkSelectedInstallment, setBulkSelectedInstallment] = useState<string>('inst_1');
  const [bulkPaymentDate, setBulkPaymentDate] = useState<string>(() => getDateKeyIST());
  const [bulkPayments, setBulkPayments] = useState<Record<string, { checked: boolean; amount: number; method: string; ref: string; component: string }>>({});
  const [savingBulk, setSavingBulk] = useState(false);

  // Helper to compute late days remark
  const getLateRemarks = (dueDateStr?: string, paymentDateStr?: string) => {
    if (!dueDateStr || !paymentDateStr) return '';
    try {
      const due = new Date(dueDateStr);
      const pay = new Date(paymentDateStr);
      if (isNaN(due.getTime()) || isNaN(pay.getTime())) return '';
      
      const dueUtc = Date.UTC(due.getFullYear(), due.getMonth(), due.getDate());
      const payUtc = Date.UTC(pay.getFullYear(), pay.getMonth(), pay.getDate());
      
      const diffDays = Math.floor((payUtc - dueUtc) / (1000 * 60 * 60 * 24));
      if (diffDays > 0) {
        return `Late by ${diffDays} day${diffDays > 1 ? 's' : ''}`;
      }
    } catch (e) {}
    return '';
  };

  // Sorting States
  const [studentSortField, setStudentSortField] = useState<'name' | 'classNum' | 'netDues' | 'paid' | 'outstanding' | 'status'>('name');
  const [studentSortDir, setStudentSortDir] = useState<'asc' | 'desc'>('asc');

  const [tmplSortField, setTmplSortField] = useState<'name' | 'classNum' | 'totalPackageAmount' | 'splits'>('classNum');
  const [tmplSortDir, setTmplSortDir] = useState<'asc' | 'desc'>('asc');

  const [bulkSortField, setBulkSortField] = useState<'name' | 'status' | 'netDues' | 'paid' | 'outstanding'>('name');
  const [bulkSortDir, setBulkSortDir] = useState<'asc' | 'desc'>('asc');

  const handleStudentSort = (field: typeof studentSortField) => {
    if (studentSortField === field) {
      setStudentSortDir(prev => prev === 'asc' ? 'desc' : 'asc');
    } else {
      setStudentSortField(field);
      setStudentSortDir('asc');
    }
  };

  const handleTmplSort = (field: typeof tmplSortField) => {
    if (tmplSortField === field) {
      setTmplSortDir(prev => prev === 'asc' ? 'desc' : 'asc');
    } else {
      setTmplSortField(field);
      setTmplSortDir('asc');
    }
  };

  const handleBulkSort = (field: typeof bulkSortField) => {
    if (bulkSortField === field) {
      setBulkSortDir(prev => prev === 'asc' ? 'desc' : 'asc');
    } else {
      setBulkSortField(field);
      setBulkSortDir('asc');
    }
  };

  const renderSortHeader = (label: string, field: string, currentField: string, currentDir: 'asc' | 'desc', onSort: (f: any) => void, alignRight = false) => {
    const isActive = currentField === field;
    return (
      <th
        onClick={() => onSort(field)}
        style={{
          padding: '12px 16px',
          fontSize: '11px',
          fontWeight: 800,
          color: isActive ? 'var(--accent)' : 'var(--text-muted)',
          textTransform: 'uppercase',
          cursor: 'pointer',
          userSelect: 'none',
          textAlign: alignRight ? 'right' : 'left',
          transition: 'color 0.15s ease'
        }}
        title={`Click to sort by ${label}`}
      >
        <div style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', justifyContent: alignRight ? 'flex-end' : 'flex-start' }}>
          <span>{label}</span>
          <span style={{ fontSize: '10px', opacity: isActive ? 1 : 0.4 }}>
            {isActive ? (currentDir === 'asc' ? '▲' : '▼') : '↕'}
          </span>
        </div>
      </th>
    );
  };

  // Helper to construct bulk transaction dropdowns
  const getComponentOptions = (s: StudentFeeRecord) => {
    const options: { id: string; label: string }[] = [];
    if (s.fee?.installments && s.fee.installments.length > 0) {
      s.fee.installments.forEach(inst => {
        options.push({
          id: inst.installmentId || `inst_${inst.installmentNo}`,
          label: `Split #${inst.installmentNo} (₹${inst.amount} - ${inst.status.toUpperCase()})`
        });
      });
    }
    if (options.length === 0) {
      options.push({ id: 'inst_1', label: 'Split #1 (Unconfigured)' });
    }
    return options;
  };

  const handleSaveBulkPayments = async () => {
    const selectedList = Object.entries(bulkPayments)
      .filter(([_, data]) => data.checked && data.amount > 0)
      .map(([code, data]) => ({
        studentCode: code,
        amountPaid: Number(data.amount),
        paymentMethod: data.method,
        referenceNumber: data.ref,
        installmentId: data.component,
        paymentDate: bulkPaymentDate
      }));

    if (selectedList.length === 0) {
      alert('Please check at least one student and enter a payment amount greater than 0.');
      return;
    }

    if (!confirm(`Are you sure you want to post payments for ${selectedList.length} student(s)?`)) return;

    setSavingBulk(true);
    setError('');
    setSuccess('');
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/fees/transactions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          action: 'bulk',
          payments: selectedList
        })
      });

      const resData = await res.json();
      if (!res.ok) throw new Error(resData.error || 'Failed to save bulk payments');

      setSuccess(`Successfully posted payments for ${resData.count} students!`);
      setBulkPayments({});
      loadStudents();
    } catch (e: any) {
      setError(e.message);
    } finally {
      setSavingBulk(false);
    }
  };

  // Templates
  const [templates, setTemplates] = useState<FeeTemplate[]>([]);
  const [showTemplateModal, setShowTemplateModal] = useState(false);
  const [selectedTemplate, setSelectedTemplate] = useState<FeeTemplate | null>(null);
  const [tmplName, setTmplName] = useState('');
  const [tmplClass, setTmplClass] = useState('10');
  const [tmplTotal, setTmplTotal] = useState(0);
  const [tmplInstallments, setTmplInstallments] = useState<{ amount: number; dueDate: string }[]>([]);
  const [savingTmpl, setSavingTmpl] = useState(false);

  // Student Fees
  const [students, setStudents] = useState<StudentFeeRecord[]>([]);
  const [loadingStudents, setLoadingStudents] = useState(true);
  const [selectedStudent, setSelectedStudent] = useState<StudentFeeRecord | null>(null);
  const [customPackageTotal, setCustomPackageTotal] = useState(0);
  const [customDiscount, setCustomDiscount] = useState(0);
  const [customInstallments, setCustomInstallments] = useState<{ installmentId?: string; amount: number; dueDate: string; status: string }[]>([]);
  const [savingCustomFee, setSavingCustomFee] = useState(false);

  // Ledger Transactions Drawer
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [loadingTransactions, setLoadingTransactions] = useState(false);
  const [showTxModal, setShowTxModal] = useState(false);
  const [editingTx, setEditingTx] = useState<Transaction | null>(null);
  const [txAmount, setTxAmount] = useState(0);
  const [txMethod, setTxMethod] = useState('Cash');
  const [txRef, setTxRef] = useState('');
  const [txInstId, setTxInstId] = useState('inst_1');
  const [txDate, setTxDate] = useState(() => getDateKeyIST());
  const [savingTx, setSavingTx] = useState(false);

  // Mass Apply Template State
  const [massApplying, setMassApplying] = useState(false);

  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  // Mass apply template to entire class/batch
  const handleMassApplyTemplate = async (templateId: string, classNum?: string, onlyUnconfigured = false) => {
    const tmpl = templates.find(t => t.templateId === templateId);
    if (!tmpl) {
      alert('Please select a valid Blanket Template.');
      return;
    }
    const targetClass = classNum || tmpl.classNum;
    const countStudentsInClass = students.filter(s => String(s.classNum) === String(targetClass)).length;
    
    const confirmMsg = onlyUnconfigured
      ? `Apply template "${tmpl.name}" to all UNCONFIGURED students in Class ${targetClass}?\n(Total students in class: ${countStudentsInClass})`
      : `Apply template "${tmpl.name}" to ALL active students in Class ${targetClass}?\n(Total students to update: ${countStudentsInClass})`;
    
    if (!confirm(confirmMsg)) return;

    setMassApplying(true);
    setError('');
    setSuccess('');
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/fees', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          action: 'applyTemplateToBatch',
          templateId,
          classNum: targetClass,
          onlyUnconfigured
        })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to mass apply template');
      setSuccess(data.message || `Successfully configured fees for Class ${targetClass}.`);
      loadStudents();
    } catch (e: any) {
      setError(e.message);
    } finally {
      setMassApplying(false);
    }
  };

  // Fetch student sheets
  async function loadStudents() {
    if (!firebaseUser) return;
    setLoadingStudents(true);
    try {
      const token = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/fees', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await res.json();
      setStudents(data.students || []);
    } catch (e: any) {
      setError(e.message);
    } finally {
      setLoadingStudents(false);
    }
  }

  // Fetch templates
  async function loadTemplates() {
    if (!firebaseUser) return;
    try {
      const token = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/fees/templates', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await res.json();
      setTemplates(data.templates || []);
    } catch (e: any) {
      setError(e.message);
    }
  }

  useEffect(() => {
    loadStudents();
    loadTemplates();

    if (typeof window !== 'undefined') {
      const tabParam = new URLSearchParams(window.location.search).get('tab');
      if (tabParam === 'journal' || tabParam === 'templates' || tabParam === 'mass_entry' || tabParam === 'students') {
        setActiveTab(tabParam as any);
      }
    }
  }, [firebaseUser]);

  const getIdToken = async () => {
    if (!firebaseUser) return null;
    return await firebaseUser.getIdToken();
  };

  // Load transactions for student
  async function loadTransactions(studentCode: string) {
    setLoadingTransactions(true);
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch(`/api/admin/fees/transactions?studentCode=${studentCode}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await res.json();
      setTransactions(data.transactions || []);
    } catch (e) {
      console.error(e);
    } finally {
      setLoadingTransactions(false);
    }
  }

  // Apply blanket template splits to custom form fields
  const handleApplyTemplate = (tmplId: string) => {
    const tmpl = templates.find(t => t.templateId === tmplId);
    if (!tmpl) return;

    setCustomPackageTotal(tmpl.totalPackageAmount);
    setCustomDiscount(0);

    const mapped = tmpl.installments.map(inst => {
      const dueDateStr = inst.dueDate || (inst.dueDateOffsetDays 
        ? getDateKeyIST(new Date(Date.now() + inst.dueDateOffsetDays * 24 * 60 * 60 * 1000))
        : getDateKeyIST());
      return {
        amount: inst.amount,
        dueDate: dueDateStr,
        status: 'pending'
      };
    });
    setCustomInstallments(mapped);
  };

  // Save customized package
  const handleSaveCustomFee = async () => {
    if (!selectedStudent || savingCustomFee) return;
    setSavingCustomFee(true);
    setError('');
    setSuccess('');
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/fees', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          action: 'saveStudentFee',
          studentCode: selectedStudent.studentCode,
          feeData: {
            studentName: selectedStudent.name,
            classNum: selectedStudent.classNum,
            batchId: selectedStudent.batchId,
            totalPackageAmount: customPackageTotal,
            discountAmount: customDiscount,
            installments: customInstallments
          }
        })
      });

      const resData = await res.json();
      if (!res.ok) throw new Error(resData.error || 'Failed to save dues config');

      setSuccess(`Custom fee structure for ${selectedStudent.name} saved successfully.`);
      setSelectedStudent(null);
      loadStudents();
    } catch (e: any) {
      setError(e.message);
    } finally {
      setSavingCustomFee(false);
    }
  };

  // Add custom installment row
  const addInstallmentRow = () => {
    setCustomInstallments(prev => [...prev, { amount: 0, dueDate: getDateKeyIST(), status: 'pending' }]);
  };

  // Remove custom installment row
  const removeInstallmentRow = (idx: number) => {
    setCustomInstallments(prev => prev.filter((_, i) => i !== idx));
  };

  // Save / Edit payment transaction ledger logs
  const handleSaveTransaction = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedStudent || savingTx) return;
    setSavingTx(true);
    try {
      const token = await firebaseUser!.getIdToken();
      const payload = {
        action: editingTx ? 'edit' : 'create',
        transactionId: editingTx?.transactionId || undefined,
        transactionData: {
          studentCode: selectedStudent.studentCode,
          installmentId: txInstId,
          amountPaid: Number(txAmount),
          paymentMethod: txMethod,
          referenceNumber: txRef,
          timestamp: new Date(txDate).toISOString()
        }
      };

      const res = await fetch('/api/admin/fees/transactions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(payload)
      });

      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.error || 'Failed to record transaction');
      }

      setTxAmount(0);
      setTxRef('');
      setTxDate(getDateKeyIST());
      setEditingTx(null);
      loadTransactions(selectedStudent.studentCode);
      loadStudents();
      alert('Transaction ledger logs updated successfully!');
    } catch (err: any) {
      alert(err.message);
    } finally {
      setSavingTx(false);
    }
  };

  // Delete transaction log
  const handleDeleteTransaction = async (txId: string) => {
    if (!confirm('Are you sure you want to delete this payment log? Balance will be adjusted.')) return;
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/fees/transactions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          action: 'delete',
          transactionId: txId
        })
      });

      if (!res.ok) throw new Error('Failed to delete transaction log');
      loadTransactions(selectedStudent!.studentCode);
      loadStudents();
    } catch (e: any) {
      alert(e.message);
    }
  };

  // Save Template Splits
  const handleSaveTemplate = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!tmplName || savingTmpl) return;
    setSavingTmpl(true);
    try {
      const token = await firebaseUser!.getIdToken();
      const payload = {
        action: 'saveTemplate',
        templateId: selectedTemplate?.templateId || undefined,
        templateData: {
          name: tmplName,
          classNum: tmplClass,
          totalPackageAmount: tmplTotal,
          installments: tmplInstallments.map((inst, idx) => ({
            installmentNo: idx + 1,
            amount: inst.amount,
            dueDate: inst.dueDate
          }))
        }
      };

      const res = await fetch('/api/admin/fees/templates', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(payload)
      });

      if (!res.ok) throw new Error('Failed to save template splits');
      setShowTemplateModal(false);
      loadTemplates();
    } catch (err: any) {
      alert(err.message);
    } finally {
      setSavingTmpl(false);
    }
  };

  const addTmplInstRow = () => {
    setTmplInstallments(prev => {
      const currentSum = prev.reduce((sum, inst) => sum + Number(inst.amount || 0), 0);
      const remaining = Math.max(0, Number(tmplTotal || 0) - currentSum);

      let nextDate = '2026-03-15';
      if (prev.length > 0 && prev[prev.length - 1].dueDate) {
        try {
          const lastD = new Date(prev[prev.length - 1].dueDate);
          if (!isNaN(lastD.getTime())) {
            lastD.setMonth(lastD.getMonth() + 1);
            nextDate = getDateKeyIST(lastD);
          }
        } catch (e) {}
      }
      return [...prev, { amount: remaining > 0 ? remaining : 0, dueDate: nextDate }];
    });

    setTimeout(() => {
      const scrollBox = document.getElementById('tmpl-splits-scroll-container');
      if (scrollBox) {
        scrollBox.scrollTop = scrollBox.scrollHeight;
      }
      const amountInputs = document.querySelectorAll<HTMLInputElement>('.tmpl-inst-amount-input');
      if (amountInputs.length > 0) {
        const lastInput = amountInputs[amountInputs.length - 1];
        lastInput.focus();
        lastInput.select();
      }
    }, 50);
  };

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', padding: '24px 12px' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '20px' }}>
        
        {/* Header Block */}
        <div className="card glass" style={{ padding: '20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <h2 style={{ fontSize: '1.5rem', fontWeight: 800, color: 'var(--accent)', margin: 0 }}>Fees Manager & Ledger</h2>
          </div>
          <button className="btn btn-secondary" onClick={() => router.push('/admin')}>Back</button>
        </div>

        {error && <div className="alert-box alert-box-danger">{error}</div>}
        {success && <div className="alert-box alert-box-success">{success}</div>}

        {/* Workspace navigation tabs */}
        <div style={{ display: 'flex', gap: '4px', borderBottom: '1px solid var(--border-light)', paddingBottom: '1px' }}>
          <button
            onClick={() => { setActiveTab('students'); setSelectedStudent(null); }}
            style={{
              padding: '10px 20px',
              border: 'none',
              background: activeTab === 'students' ? 'var(--surface)' : 'transparent',
              borderBottom: activeTab === 'students' ? '2px solid var(--accent)' : 'none',
              color: activeTab === 'students' ? 'var(--accent)' : 'var(--text-muted)',
              fontWeight: 'bold',
              cursor: 'pointer',
              fontSize: '13px'
            }}
          >
            Student Dues Override
          </button>
          <button
            onClick={() => { setActiveTab('templates'); setSelectedStudent(null); }}
            style={{
              padding: '10px 20px',
              border: 'none',
              background: activeTab === 'templates' ? 'var(--surface)' : 'transparent',
              borderBottom: activeTab === 'templates' ? '2px solid var(--accent)' : 'none',
              color: activeTab === 'templates' ? 'var(--accent)' : 'var(--text-muted)',
              fontWeight: 'bold',
              cursor: 'pointer',
              fontSize: '13px'
            }}
          >
            Blanket Templates
          </button>
          <button
            onClick={() => { setActiveTab('mass_entry'); setSelectedStudent(null); }}
            style={{
              padding: '10px 20px',
              border: 'none',
              background: activeTab === 'mass_entry' ? 'var(--surface)' : 'transparent',
              borderBottom: activeTab === 'mass_entry' ? '2px solid var(--accent)' : 'none',
              color: activeTab === 'mass_entry' ? 'var(--accent)' : 'var(--text-muted)',
              fontWeight: 'bold',
              cursor: 'pointer',
              fontSize: '13px'
            }}
          >
            Mass Fees Entry
          </button>
          <button
            onClick={() => { setActiveTab('journal'); setSelectedStudent(null); }}
            style={{
              padding: '10px 20px',
              border: 'none',
              background: activeTab === 'journal' ? 'var(--surface)' : 'transparent',
              borderBottom: activeTab === 'journal' ? '2px solid var(--accent)' : 'none',
              color: activeTab === 'journal' ? 'var(--accent)' : 'var(--text-muted)',
              fontWeight: 'bold',
              cursor: 'pointer',
              fontSize: '13px'
            }}
          >
            Fees Journal
          </button>
        </div>

        {/* WORKSPACE 1: Student Sheets Override */}
        {activeTab === 'students' && !selectedStudent && (
          <div className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', overflow: 'hidden' }}>
            <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '12px' }}>
              <div>
                <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800 }}>Active Students Ledgers</h3>
                <p style={{ margin: '2px 0 0 0', fontSize: '11px', color: 'var(--text-muted)' }}>
                  Total {students.length} students across classes. Assign blanket structures or override individually.
                </p>
              </div>
            </div>

            {loadingStudents ? (
              <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>Loading student sheets...</div>
            ) : students.length === 0 ? (
              <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>No student records found.</div>
            ) : (
              <div style={{ overflowX: 'auto' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                  <thead>
                    <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                      {renderSortHeader('Student', 'name', studentSortField, studentSortDir, handleStudentSort)}
                      {renderSortHeader('Class', 'classNum', studentSortField, studentSortDir, handleStudentSort)}
                      {renderSortHeader('Net Dues', 'netDues', studentSortField, studentSortDir, handleStudentSort)}
                      {renderSortHeader('Paid', 'paid', studentSortField, studentSortDir, handleStudentSort)}
                      {renderSortHeader('Outstanding', 'outstanding', studentSortField, studentSortDir, handleStudentSort)}
                      {renderSortHeader('Status', 'status', studentSortField, studentSortDir, handleStudentSort)}
                      <th style={{ padding: '12px 16px', fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', textAlign: 'right' }}>Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    {(() => {
                      const sortedStudents = [...students].sort((a, b) => {
                        let valA: any = '';
                        let valB: any = '';
                        if (studentSortField === 'name') {
                          valA = (a.name || '').toLowerCase();
                          valB = (b.name || '').toLowerCase();
                        } else if (studentSortField === 'classNum') {
                          valA = Number(a.classNum) || 0;
                          valB = Number(b.classNum) || 0;
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
                            if (!s.fee) return 1;
                            if (s.fee.hasOverdueInstallment) return 4;
                            if (s.fee.feeStatus === 'partially_paid') return 3;
                            if (s.fee.feeStatus === 'fully_paid') return 2;
                            return 0;
                          };
                          valA = getStatusWeight(a);
                          valB = getStatusWeight(b);
                        }
                        if (valA < valB) return studentSortDir === 'asc' ? -1 : 1;
                        if (valA > valB) return studentSortDir === 'asc' ? 1 : -1;
                        return 0;
                      });

                      return sortedStudents.map(s => (
                        <tr key={s.studentCode} style={{ borderBottom: '1px solid var(--border-light)' }}>
                          <td style={{ padding: '14px 16px', fontSize: '13px' }}>
                            <div><strong>{s.name}</strong></div>
                          </td>
                          <td style={{ padding: '14px 16px', fontSize: '13px', fontWeight: 600 }}>
                            Class {s.classNum}
                          </td>
                          <td style={{ padding: '14px 16px', fontSize: '13px', fontWeight: 700 }}>
                            ₹{s.fee?.netPayableAmount !== undefined ? s.fee.netPayableAmount : '--'}
                          </td>
                          <td style={{ padding: '14px 16px', fontSize: '13px', color: 'var(--success)', fontWeight: 700 }}>
                            ₹{s.fee?.totalPaidAmount !== undefined ? s.fee.totalPaidAmount : '--'}
                          </td>
                          <td style={{ padding: '14px 16px', fontSize: '13px', color: 'var(--danger)', fontWeight: 700 }}>
                            ₹{s.fee?.outstandingAmount !== undefined ? s.fee.outstandingAmount : '--'}
                          </td>
                          <td style={{ padding: '14px 16px' }}>
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
                          <td style={{ padding: '14px 16px', textAlign: 'right' }}>
                            <button
                              onClick={() => {
                                setSelectedStudent(s);
                                setCustomPackageTotal(s.fee?.totalPackageAmount || 0);
                                setCustomDiscount(s.fee?.discountAmount || 0);
                                setCustomInstallments(s.fee?.installments || []);
                              }}
                              className="btn btn-secondary"
                              style={{ padding: '4px 8px', fontSize: '11px', fontWeight: 'bold' }}
                            >
                              ⚙️ Configure Installments
                            </button>
                          </td>
                        </tr>
                      ));
                    })()}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        )}

        {/* WORKSPACE 2: Custom Sheet Editor */}
        {activeTab === 'students' && selectedStudent && (
          <div className="card" style={{ padding: '24px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', borderBottom: '1px solid var(--border-light)', paddingBottom: '16px', marginBottom: '20px' }}>
              <div>
                <h3 style={{ margin: 0, fontSize: '1.2rem', fontWeight: 800, color: 'var(--accent)' }}>
                  ⚙️ Customize Fees: {selectedStudent.name}
                </h3>
                <p style={{ margin: '2px 0 0 0', fontSize: '11px', color: 'var(--text-muted)' }}>
                  Customize the totals, discounts, and installment splits for: <strong>{selectedStudent.name}</strong>
                </p>
              </div>
              <div style={{ display: 'flex', gap: '8px' }}>
                <button className="btn btn-secondary" onClick={() => {
                  loadTransactions(selectedStudent.studentCode);
                  setShowTxModal(true);
                }}>
                  💸 Ledger Logs & Receipts
                </button>
                <button className="btn btn-secondary" onClick={() => setSelectedStudent(null)}>Cancel</button>
              </div>
            </div>

            {/* Template Apply quickbar */}
            <div style={{ background: 'var(--bg-soft)', padding: '12px 16px', borderRadius: 'var(--radius)', marginBottom: '24px', border: '1.5px dashed var(--border-light)' }}>
              <span style={{ fontSize: '12px', fontWeight: 'bold', marginRight: '12px' }}>⚡ Apply Blanket Template:</span>
              <select
                onChange={(e) => { if (e.target.value) handleApplyTemplate(e.target.value); }}
                defaultValue=""
                style={{ padding: '6px 12px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              >
                <option value="">-- Choose template --</option>
                {templates.map(t => (
                  <option key={t.templateId} value={t.templateId}>{t.name} (₹{t.totalPackageAmount})</option>
                ))}
              </select>
            </div>

            {/* Package Totals Grid */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '16px', marginBottom: '24px' }}>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600 }}>Total Package Rate (₹)</label>
                <input
                  type="number"
                  value={customPackageTotal}
                  onChange={(e) => setCustomPackageTotal(Number(e.target.value))}
                  style={{ padding: '8px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                />
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600 }}>Scholarship / Discount (₹)</label>
                <input
                  type="number"
                  value={customDiscount}
                  onChange={(e) => setCustomDiscount(Number(e.target.value))}
                  style={{ padding: '8px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                />
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600 }}>Net Payable Dues (₹)</label>
                <input
                  type="number"
                  value={customPackageTotal - customDiscount}
                  disabled
                  style={{ padding: '8px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text-muted)', cursor: 'not-allowed', fontWeight: 'bold' }}
                />
              </div>
            </div>

            {/* Installments listing */}
            <div style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius)', overflow: 'hidden', marginBottom: '24px' }}>
              <div style={{ padding: '12px 16px', background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <h4 style={{ margin: 0, fontSize: '13px', fontWeight: 'bold' }}>📅 Custom Installment Matrix</h4>
                <button className="btn btn-secondary" onClick={addInstallmentRow} style={{ padding: '4px 10px', fontSize: '11px' }}>
                  ➕ Add Installment
                </button>
              </div>

              {(() => {
                const sumOfSplits = customInstallments.reduce((sum, inst) => sum + Number(inst.amount || 0), 0);
                const netPayable = customPackageTotal - customDiscount;
                const isMatch = sumOfSplits === netPayable;
                return (
                  <div style={{
                    padding: '8px 12px',
                    fontSize: '11px',
                    fontWeight: 600,
                    background: isMatch ? 'rgba(16, 185, 129, 0.1)' : 'rgba(239, 68, 68, 0.1)',
                    color: isMatch ? 'var(--success)' : 'var(--danger)',
                    borderBottom: '1px solid var(--border-light)'
                  }}>
                    {isMatch ? (
                      <span>✓ Splits match Net Payable Dues (₹{netPayable}).</span>
                    ) : (
                      <span>⚠️ Sum of splits (₹{sumOfSplits}) does not match Net Payable Dues (₹{netPayable}). Difference: ₹{netPayable - sumOfSplits}.</span>
                    )}
                  </div>
                );
              })()}

              {customInstallments.length === 0 ? (
                <div style={{ padding: '30px', textAlign: 'center', color: 'var(--text-faint)', fontSize: '12px' }}>
                  No installments configured. Click Add to create one.
                </div>
              ) : (
                <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                  <thead>
                    <tr style={{ borderBottom: '1px solid var(--border-light)', fontSize: '11px', color: 'var(--text-muted)', background: 'var(--bg-soft)' }}>
                      <th style={{ padding: '10px 16px' }}>Installment #</th>
                      <th style={{ padding: '10px 16px' }}>Amount (₹)</th>
                      <th style={{ padding: '10px 16px' }}>Due Date</th>
                      <th style={{ padding: '10px 16px' }}>Status Override</th>
                      <th style={{ padding: '10px 16px', textAlign: 'right' }}>Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    {customInstallments.map((inst, idx) => (
                      <tr key={idx} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '12px 16px', fontSize: '13px', fontWeight: 600 }}>Installment {idx + 1}</td>
                        <td style={{ padding: '12px 16px' }}>
                          <input
                            type="number"
                            value={inst.amount}
                            onChange={(e) => {
                              const val = Number(e.target.value);
                              setCustomInstallments(prev => prev.map((item, i) => i === idx ? { ...item, amount: val } : item));
                            }}
                            style={{ padding: '6px 10px', width: '120px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                          />
                        </td>
                        <td style={{ padding: '12px 16px' }}>
                          <DateInputDMY
                            value={inst.dueDate || ''}
                            onChange={(val) => {
                              setCustomInstallments(prev => prev.map((item, i) => i === idx ? { ...item, dueDate: val } : item));
                            }}
                            style={{ width: '130px' }}
                          />
                        </td>
                        <td style={{ padding: '12px 16px' }}>
                          <select
                            value={inst.status}
                            onChange={(e) => {
                              const val = e.target.value;
                              setCustomInstallments(prev => prev.map((item, i) => i === idx ? { ...item, status: val } : item));
                            }}
                            style={{ padding: '6px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                          >
                            <option value="pending">Pending</option>
                            <option value="paid">Paid</option>
                            <option value="overdue">Overdue</option>
                          </select>
                        </td>
                        <td style={{ padding: '12px 16px', textAlign: 'right' }}>
                          <button
                            onClick={() => removeInstallmentRow(idx)}
                            style={{ border: 'none', background: 'transparent', color: 'var(--danger)', cursor: 'pointer', fontSize: '1rem' }}
                          >
                            🗑️
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px' }}>
              <button className="btn btn-secondary" onClick={() => setSelectedStudent(null)}>Cancel</button>
              <button className="btn btn-primary" onClick={handleSaveCustomFee} disabled={savingCustomFee}>
                {savingCustomFee ? 'Saving...' : '💾 Save Customized Package'}
              </button>
            </div>
          </div>
        )}

        {/* WORKSPACE 3: Blanket Templates Constructor */}
        {activeTab === 'templates' && (
          <div className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', overflow: 'hidden' }}>
            <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold' }}>Blanket Templates Configurations</h3>
              <button
                className="btn btn-primary"
                onClick={() => {
                  setSelectedTemplate(null);
                  setTmplName('');
                  setTmplClass('10');
                  setTmplTotal(0);
                  setTmplInstallments([]);
                  setShowTemplateModal(true);
                }}
                style={{ padding: '6px 12px', fontSize: '12px' }}
              >
                ➕ Create Template
              </button>
            </div>

            {templates.length === 0 ? (
              <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>No templates found. Click create to get started.</div>
            ) : (
              <div style={{ overflowX: 'auto' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                  <thead>
                    <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                      {renderSortHeader('Template Name', 'name', tmplSortField, tmplSortDir, handleTmplSort)}
                      {renderSortHeader('Class', 'classNum', tmplSortField, tmplSortDir, handleTmplSort)}
                      {renderSortHeader('Package Fee', 'totalPackageAmount', tmplSortField, tmplSortDir, handleTmplSort)}
                      {renderSortHeader('Splits', 'splits', tmplSortField, tmplSortDir, handleTmplSort)}
                      <th style={{ padding: '12px 16px', fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', textAlign: 'right' }}>Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    {(() => {
                      const sortedTemplates = [...templates].sort((a, b) => {
                        let valA: any = '';
                        let valB: any = '';
                        if (tmplSortField === 'name') {
                          valA = (a.name || '').toLowerCase();
                          valB = (b.name || '').toLowerCase();
                        } else if (tmplSortField === 'classNum') {
                          valA = Number(a.classNum) || 0;
                          valB = Number(b.classNum) || 0;
                        } else if (tmplSortField === 'totalPackageAmount') {
                          valA = Number(a.totalPackageAmount) || 0;
                          valB = Number(b.totalPackageAmount) || 0;
                        } else if (tmplSortField === 'splits') {
                          valA = a.installments?.length || 0;
                          valB = b.installments?.length || 0;
                        }
                        if (valA < valB) return tmplSortDir === 'asc' ? -1 : 1;
                        if (valA > valB) return tmplSortDir === 'asc' ? 1 : -1;
                        return 0;
                      });

                      return sortedTemplates.map(t => (
                        <tr key={t.templateId} style={{ borderBottom: '1px solid var(--border-light)' }}>
                          <td style={{ padding: '14px 16px', fontSize: '13px', fontWeight: 'bold' }}>{t.name}</td>
                          <td style={{ padding: '14px 16px', fontSize: '13px' }}>Class {t.classNum}</td>
                          <td style={{ padding: '14px 16px', fontSize: '13px', fontWeight: 700 }}>₹{t.totalPackageAmount}</td>
                          <td style={{ padding: '14px 16px', fontSize: '13px' }}>{t.installments?.length || 0} Splits</td>
                          <td style={{ padding: '14px 16px', textAlign: 'right' }}>
                            <button
                              onClick={() => handleMassApplyTemplate(t.templateId, t.classNum, false)}
                              disabled={massApplying}
                              className="btn btn-primary"
                              style={{ padding: '4px 10px', fontSize: '11px', fontWeight: 700, marginRight: '8px', borderRadius: '4px' }}
                              title={`Apply ${t.name} to all active Class ${t.classNum} students`}
                            >
                              ⚡ Apply to Class {t.classNum}
                            </button>
                            <button
                              onClick={() => {
                                setSelectedTemplate(t);
                                setTmplName(t.name);
                                setTmplClass(t.classNum);
                                setTmplTotal(t.totalPackageAmount);
                                setTmplInstallments(t.installments.map(i => ({ 
                                  amount: i.amount, 
                                  dueDate: i.dueDate || (i.dueDateOffsetDays ? getDateKeyIST(new Date(new Date().getTime() + i.dueDateOffsetDays * 24 * 60 * 60 * 1000)) : '')
                                })));
                                setShowTemplateModal(true);
                              }}
                              className="btn btn-secondary"
                              style={{ padding: '4px 8px', fontSize: '11px', marginRight: '8px' }}
                            >
                              ✏️ Edit
                            </button>
                            <button
                              onClick={async () => {
                                if (!confirm('Are you sure you want to delete this template?')) return;
                                const token = await firebaseUser!.getIdToken();
                                await fetch('/api/admin/fees/templates', {
                                  method: 'POST',
                                  headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
                                  body: JSON.stringify({ action: 'deleteTemplate', templateId: t.templateId })
                                });
                                loadTemplates();
                              }}
                              style={{ border: 'none', background: 'transparent', color: 'var(--danger)', cursor: 'pointer', fontSize: '1rem' }}
                              title="Delete template"
                            >
                              🗑️
                            </button>
                          </td>
                        </tr>
                      ));
                    })()}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        )}

        {/* WORKSPACE 4: Mass Fees Entry Sheet */}
        {activeTab === 'mass_entry' && (
          <div className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', overflow: 'hidden' }}>
            <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px' }}>
              <div>
                <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold' }}>💰 Mass Fees Entry Sheet</h3>
                <p style={{ margin: '4px 0 0 0', fontSize: '12px', color: 'var(--text-muted)' }}>
                  Record payments for multiple students in a single class batch.
                </p>
              </div>

              {/* Class Filter Selection */}
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '12px', fontWeight: 'bold' }}>Filter by Class:</span>
                <select
                  value={bulkClass}
                  onChange={(e) => {
                    setBulkClass(e.target.value);
                    setBulkPayments({});
                  }}
                  style={{ padding: '6px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontWeight: 600 }}
                >
                  <option value="8">Class 8</option>
                  <option value="9">Class 9</option>
                  <option value="10">Class 10</option>
                  <option value="11">Class 11</option>
                  <option value="12">Class 12</option>
                </select>
              </div>
            </div>

            {/* Student List */}
            {(() => {
              const filteredStudents = students.filter(s => s.classNum === bulkClass);

              // Resolve template for this class to populate selectable installment amount/dates
              const classTemplate = templates.find(t => t.classNum === bulkClass);
              const bulkInstallmentOptions: { id: string; label: string; amount: number; dueDate?: string }[] = [];
              if (classTemplate && classTemplate.installments) {
                classTemplate.installments.forEach((inst) => {
                  bulkInstallmentOptions.push({
                    id: `inst_${inst.installmentNo}`,
                    label: `#${inst.installmentNo} (₹${inst.amount}${inst.dueDate ? ` - Due: ${formatDateStr(inst.dueDate)}` : ''})`,
                    amount: inst.amount,
                    dueDate: inst.dueDate
                  });
                });
              }
              if (bulkInstallmentOptions.length === 0) {
                bulkInstallmentOptions.push({
                  id: 'inst_1',
                  label: '#1 (₹0 - Unconfigured)',
                  amount: 0
                });
              }

              const selectedOpt = bulkInstallmentOptions.find(o => o.id === bulkSelectedInstallment) || bulkInstallmentOptions[0];

              if (filteredStudents.length === 0) {
                return (
                  <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>
                    No active student records found for Class {bulkClass}.
                  </div>
                );
              }

              return (
                <div>
                  {/* Sourced Template Config bar */}
                  <div style={{ display: 'flex', gap: '20px', flexWrap: 'wrap', background: 'var(--bg-soft)', padding: '16px 20px', borderBottom: '1px solid var(--border-light)', alignItems: 'center' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span style={{ fontSize: '12px', fontWeight: 'bold' }}>Select:</span>
                      <select
                        value={bulkSelectedInstallment}
                        onChange={(e) => {
                          const val = e.target.value;
                          setBulkSelectedInstallment(val);
                          const matchingOpt = bulkInstallmentOptions.find(o => o.id === val);
                          if (matchingOpt) {
                            setBulkPayments(prev => {
                              const next = { ...prev };
                              Object.keys(next).forEach(studentCode => {
                                next[studentCode] = {
                                  ...next[studentCode],
                                  amount: next[studentCode].checked ? matchingOpt.amount : 0,
                                  component: val
                                };
                              });
                              return next;
                            });
                          }
                        }}
                        style={{ padding: '6px 12px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px', fontWeight: 600 }}
                      >
                        {bulkInstallmentOptions.map(opt => (
                          <option key={opt.id} value={opt.id}>{opt.label}</option>
                        ))}
                      </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span style={{ fontSize: '12px', fontWeight: 'bold' }}>Payment Date:</span>
                      <DateInputDMY
                        value={bulkPaymentDate}
                        onChange={(val) => {
                          setBulkPaymentDate(val);
                        }}
                        style={{ width: '135px' }}
                      />
                    </div>

                    <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                      Sourced Amount: <strong style={{ color: 'var(--accent)', fontSize: '13px' }}>₹{selectedOpt.amount}</strong>
                    </div>
                  </div>

                  <div style={{ overflowX: 'auto' }}>
                    <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                      <thead>
                        <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                          <th style={{ padding: '12px 16px', width: '40px' }}>
                            <input
                              type="checkbox"
                              onChange={(e) => {
                                const checked = e.target.checked;
                                const next = { ...bulkPayments };
                                filteredStudents.forEach(s => {
                                  const sCode = s.studentCode;
                                  next[sCode] = {
                                    checked,
                                    amount: checked ? selectedOpt.amount : 0,
                                    method: next[sCode]?.method || 'Cash',
                                    ref: next[sCode]?.ref || '',
                                    component: selectedOpt.id
                                  };
                                });
                                setBulkPayments(next);
                              }}
                            />
                          </th>
                          {renderSortHeader('Student', 'name', bulkSortField, bulkSortDir, handleBulkSort)}
                          {renderSortHeader('Ledger Status', 'status', bulkSortField, bulkSortDir, handleBulkSort)}
                          <th style={{ padding: '12px 16px', fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Amount to Pay (₹)</th>
                          <th style={{ padding: '12px 16px', fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Method</th>
                          <th style={{ padding: '12px 16px', fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Reference / Remarks</th>
                        </tr>
                      </thead>
                      <tbody>
                        {(() => {
                          const sortedFilteredStudents = [...filteredStudents].sort((a, b) => {
                            let valA: any = '';
                            let valB: any = '';
                            if (bulkSortField === 'name') {
                              valA = (a.name || '').toLowerCase();
                              valB = (b.name || '').toLowerCase();
                            } else if (bulkSortField === 'status') {
                              const getStatusWeight = (s: StudentFeeRecord) => {
                                if (!s.fee) return 1;
                                if (s.fee.hasOverdueInstallment) return 4;
                                if (s.fee.feeStatus === 'partially_paid') return 3;
                                if (s.fee.feeStatus === 'fully_paid') return 2;
                                return 0;
                              };
                              valA = getStatusWeight(a);
                              valB = getStatusWeight(b);
                            }
                            if (valA < valB) return bulkSortDir === 'asc' ? -1 : 1;
                            if (valA > valB) return bulkSortDir === 'asc' ? 1 : -1;
                            return 0;
                          });

                          return sortedFilteredStudents.map(s => {
                            const sCode = s.studentCode;
                            const payment = bulkPayments[sCode] || {
                              checked: false,
                              amount: 0,
                              method: 'Cash',
                              ref: '',
                              component: selectedOpt.id
                            };

                          const updateField = (field: string, value: any) => {
                            setBulkPayments(prev => ({
                              ...prev,
                              [sCode]: {
                                ...(prev[sCode] || { checked: false, amount: 0, method: 'Cash', ref: '', component: selectedOpt.id }),
                                [field]: value
                              }
                            }));
                          };

                          return (
                            <tr key={sCode} style={{ borderBottom: '1px solid var(--border-light)', background: payment.checked ? 'var(--bg-soft)' : 'transparent' }}>
                              <td style={{ padding: '14px 16px' }}>
                                <input
                                  type="checkbox"
                                  checked={payment.checked}
                                  onChange={(e) => {
                                    const checked = e.target.checked;
                                    updateField('checked', checked);
                                    updateField('amount', checked ? selectedOpt.amount : 0);
                                    updateField('component', selectedOpt.id);
                                  }}
                                />
                              </td>
                              <td style={{ padding: '14px 16px', fontSize: '13px' }}>
                                <div><strong>{s.name}</strong></div>
                              </td>
                              <td style={{ padding: '14px 16px', fontSize: '12px' }}>
                                {s.fee ? (
                                  <div>
                                    <div>Outstanding: <strong style={{ color: 'var(--danger)' }}>₹{s.fee.outstandingAmount}</strong></div>
                                    <div style={{ fontSize: '10px', color: 'var(--text-muted)' }}>Net: ₹{s.fee.netPayableAmount} | Paid: ₹{s.fee.totalPaidAmount}</div>
                                  </div>
                                ) : (
                                  <span style={{ fontStyle: 'italic', color: 'var(--text-faint)' }}>Not Configured</span>
                                )}
                              </td>
                              <td style={{ padding: '14px 16px' }}>
                                <input
                                  type="number"
                                  disabled
                                  value={payment.checked ? selectedOpt.amount : ''}
                                  placeholder="--"
                                  style={{ padding: '6px 8px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text-muted)', width: '100px', fontSize: '12px', cursor: 'not-allowed' }}
                                />
                              </td>
                              <td style={{ padding: '14px 16px' }}>
                                <select
                                  value={payment.method}
                                  onChange={(e) => updateField('method', e.target.value)}
                                  disabled={!payment.checked}
                                  style={{ padding: '6px 8px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                                >
                                  <option value="UPI">UPI</option>
                                  <option value="Cash">Cash</option>
                                  <option value="Cheque">Cheque</option>
                                </select>
                              </td>
                              <td style={{ padding: '14px 16px' }}>
                                <input
                                  type="text"
                                  placeholder="Transaction ref / notes"
                                  value={payment.ref}
                                  onChange={(e) => updateField('ref', e.target.value)}
                                  disabled={!payment.checked}
                                  style={{ padding: '6px 8px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', width: '100%', fontSize: '12px' }}
                                />
                              </td>
                            </tr>
                          );
                        });
                      })()}
                    </tbody>
                    </table>
                  </div>

                  <div style={{ padding: '16px 20px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end', gap: '8px' }}>
                    <button
                      className="btn btn-primary"
                      onClick={handleSaveBulkPayments}
                      disabled={savingBulk}
                    >
                      {savingBulk ? 'Posting payments...' : '💾 Post Mass Payments'}
                    </button>
                  </div>
                </div>
              );
            })()}
          </div>
        )}

        {/* WORKSPACE 4: Fees Journal & Ledger */}
        {activeTab === 'journal' && !selectedStudent && (
          <FeesJournal
            students={students}
            loadingStudents={loadingStudents}
            getIdToken={getIdToken}
            onSelectStudent={(s) => {
              setSelectedStudent(s);
              setCustomPackageTotal(s.fee?.totalPackageAmount || 0);
              setCustomDiscount(s.fee?.discountAmount || 0);
              setCustomInstallments(s.fee?.installments || []);
              setActiveTab('students');
            }}
          />
        )}

      </div>

      {/* Template Modal */}
      {showTemplateModal && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.65)', backdropFilter: 'blur(5px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 9999, padding: '16px' }}>
          <div className="card" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: '12px', maxWidth: '680px', width: '100%', maxHeight: '90vh', display: 'flex', flexDirection: 'column', boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.4)', overflow: 'hidden' }}>
            
            {/* Modal Header */}
            <div style={{ padding: '16px 22px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--surface-popover)', flexShrink: 0 }}>
              <div>
                <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 700, color: 'var(--text)' }}>
                  {selectedTemplate ? '✏️ Edit Blanket Template' : '➕ Create Blanket Template'}
                </h3>
                <p style={{ margin: '2px 0 0 0', fontSize: '11px', color: 'var(--text-muted)' }}>
                  Define standard package fees and installment due dates for a class
                </p>
              </div>
              <button 
                type="button"
                style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.4rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '4px', borderRadius: '4px' }} 
                onClick={() => setShowTemplateModal(false)}
              >
                ✕
              </button>
            </div>

            {/* Modal Form Body */}
            <form onSubmit={handleSaveTemplate} style={{ display: 'flex', flexDirection: 'column', flex: 1, minHeight: 0, overflow: 'hidden' }}>
              <div style={{ padding: '16px 22px', display: 'flex', flexDirection: 'column', gap: '14px', overflowY: 'auto', flex: 1, minHeight: 0, boxSizing: 'border-box' }}>
                
                {/* Template Name */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
                  <label style={{ fontSize: '11px', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.5px', color: 'var(--text-muted)' }}>Template Name</label>
                  <input
                    type="text"
                    required
                    value={tmplName}
                    onChange={(e) => setTmplName(e.target.value)}
                    placeholder="e.g. Class 8th 2026-27"
                    style={{ padding: '8px 12px', height: '38px', borderRadius: '6px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '13px', boxSizing: 'border-box' }}
                  />
                </div>

                {/* Class & Total Row */}
                <div style={{ display: 'grid', gridTemplateColumns: '130px 1fr', gap: '12px' }}>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
                    <label style={{ fontSize: '11px', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.5px', color: 'var(--text-muted)' }}>Class</label>
                    <select
                      value={tmplClass}
                      onChange={(e) => setTmplClass(e.target.value)}
                      style={{ padding: '8px 10px', height: '38px', borderRadius: '6px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '13px', fontWeight: 600, width: '100%', boxSizing: 'border-box' }}
                    >
                      <option value="8">Class 8</option>
                      <option value="9">Class 9</option>
                      <option value="10">Class 10</option>
                      <option value="11">Class 11</option>
                      <option value="12">Class 12</option>
                    </select>
                  </div>

                  <div style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
                    <label style={{ fontSize: '11px', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.5px', color: 'var(--text-muted)' }}>Total Package (₹)</label>
                    <input
                      type="number"
                      required
                      value={tmplTotal === 0 ? '' : (tmplTotal ?? '')}
                      onChange={(e) => {
                        const raw = e.target.value;
                        setTmplTotal(raw === '' ? '' as any : Number(raw));
                      }}
                      placeholder="e.g. 25000"
                      style={{ padding: '8px 12px', height: '38px', borderRadius: '6px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '13px', fontWeight: 600, boxSizing: 'border-box' }}
                    />
                  </div>
                </div>

                {/* Installments Splits Section */}
                <div style={{ border: '1px solid var(--border-light)', borderRadius: '8px', overflow: 'hidden', background: 'var(--surface)', display: 'flex', flexDirection: 'column' }}>
                  {/* Splits Header */}
                  <div style={{ padding: '10px 14px', background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexShrink: 0 }}>
                    <div>
                      <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text)' }}>Installment Splits</span>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', marginLeft: '8px' }}>(Press Tab on last date to add next split)</span>
                    </div>
                    <button 
                      type="button" 
                      className="btn btn-secondary" 
                      onClick={addTmplInstRow} 
                      style={{ padding: '4px 10px', fontSize: '11px', fontWeight: 600, borderRadius: '6px' }}
                    >
                      ➕ Add Split
                    </button>
                  </div>

                  {/* Balance validation bar */}
                  {(() => {
                    const sumOfSplits = tmplInstallments.reduce((sum, inst) => sum + Number(inst.amount || 0), 0);
                    const totalPkg = Number(tmplTotal || 0);
                    const isMatch = totalPkg > 0 && sumOfSplits === totalPkg;
                    const diff = totalPkg - sumOfSplits;
                    return (
                      <div style={{
                        padding: '8px 14px',
                        fontSize: '11px',
                        fontWeight: 600,
                        background: isMatch ? 'rgba(16, 185, 129, 0.1)' : 'rgba(239, 68, 68, 0.08)',
                        color: isMatch ? 'var(--success)' : 'var(--danger)',
                        borderBottom: '1px solid var(--border-light)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'space-between',
                        flexShrink: 0
                      }}>
                        <span>
                          {isMatch 
                            ? `✓ Splits perfectly match Total Package (₹${totalPkg}).` 
                            : `⚠️ Sum of splits (₹${sumOfSplits}) does not match Total Package (₹${totalPkg}). Difference: ₹${diff}.`
                          }
                        </span>
                        {diff > 0 && tmplInstallments.length > 0 && (
                          <button
                            type="button"
                            onClick={() => {
                              setTmplInstallments(prev => {
                                const copy = [...prev];
                                const lastIdx = copy.length - 1;
                                copy[lastIdx] = { ...copy[lastIdx], amount: Number(copy[lastIdx].amount || 0) + diff };
                                return copy;
                              });
                            }}
                            style={{ border: 'none', background: 'transparent', color: 'var(--accent)', cursor: 'pointer', fontSize: '10px', fontWeight: 700, textDecoration: 'underline' }}
                          >
                            Auto-balance +₹{diff}
                          </button>
                        )}
                      </div>
                    );
                  })()}

                  {/* Splits rows list with dedicated vertical scrolling */}
                  <div 
                    id="tmpl-splits-scroll-container"
                    style={{ 
                      maxHeight: '220px', 
                      minHeight: '100px',
                      overflowY: 'scroll', 
                      overflowX: 'hidden',
                      scrollbarWidth: 'thin',
                      scrollbarGutter: 'stable',
                      overscrollBehavior: 'contain'
                    }}
                  >
                    {tmplInstallments.length === 0 ? (
                      <div style={{ padding: '24px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '12px' }}>
                        No installment splits added yet. Click <strong>+ Add Split</strong> to create one.
                      </div>
                    ) : (
                      tmplInstallments.map((inst, idx) => (
                        <div 
                          key={idx} 
                          style={{ 
                            display: 'grid', 
                            gridTemplateColumns: '40px 140px 1fr 36px', 
                            gap: '10px', 
                            padding: '8px 14px', 
                            borderBottom: idx === tmplInstallments.length - 1 ? 'none' : '1px solid var(--border-light)', 
                            alignItems: 'center',
                            boxSizing: 'border-box'
                          }}
                        >
                          {/* Index */}
                          <span style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', background: 'var(--bg-soft)', borderRadius: '4px', padding: '3px 6px', textAlign: 'center' }}>
                            #{idx + 1}
                          </span>

                          {/* Amount */}
                          <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                            <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted)' }}>₹</span>
                            <input
                              type="number"
                              placeholder="Amount"
                              required
                              className="tmpl-inst-amount-input"
                              value={inst.amount === 0 ? '' : (inst.amount ?? '')}
                              onChange={(e) => {
                                const raw = e.target.value;
                                const val = raw === '' ? ('' as any) : Number(raw);
                                setTmplInstallments(prev => prev.map((item, i) => i === idx ? { ...item, amount: val } : item));
                              }}
                              style={{ 
                                width: '100%', 
                                height: '36px', 
                                padding: '6px 8px', 
                                borderRadius: '6px', 
                                border: '1px solid var(--border-light)', 
                                background: 'var(--surface)', 
                                color: 'var(--text)', 
                                fontSize: '12px', 
                                fontWeight: 600,
                                boxSizing: 'border-box'
                              }}
                            />
                          </div>

                          {/* Due Date */}
                          <div>
                            <DateInputDMY
                              value={inst.dueDate || ''}
                              onChange={(val) => {
                                setTmplInstallments(prev => prev.map((item, i) => i === idx ? { ...item, dueDate: val } : item));
                              }}
                              onKeyDown={(e) => {
                                if (e.key === 'Tab' && !e.shiftKey && idx === tmplInstallments.length - 1) {
                                  e.preventDefault();
                                  addTmplInstRow();
                                }
                              }}
                            />
                          </div>

                          {/* Delete Action */}
                          <button
                            type="button"
                            onClick={() => setTmplInstallments(prev => prev.filter((_, i) => i !== idx))}
                            style={{ 
                              border: 'none', 
                              background: 'transparent', 
                              color: 'var(--danger)', 
                              cursor: 'pointer', 
                              fontSize: '1.1rem', 
                              padding: '4px', 
                              display: 'flex', 
                              alignItems: 'center', 
                              justifyContent: 'center',
                              borderRadius: '4px'
                            }}
                            title="Delete split"
                          >
                            🗑️
                          </button>
                        </div>
                      ))
                    )}
                  </div>
                </div>
              </div>

              {/* Modal Footer (Pinned at bottom) */}
              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', padding: '14px 22px', borderTop: '1px solid var(--border-light)', background: 'var(--surface-popover)', flexShrink: 0 }}>
                <button 
                  type="button" 
                  className="btn btn-secondary" 
                  onClick={() => setShowTemplateModal(false)}
                  style={{ padding: '8px 16px', fontSize: '13px', borderRadius: '6px' }}
                >
                  Cancel
                </button>
                <button 
                  type="submit" 
                  className="btn btn-primary" 
                  disabled={savingTmpl}
                  style={{ padding: '8px 20px', fontSize: '13px', borderRadius: '6px', fontWeight: 600 }}
                >
                  {savingTmpl ? 'Saving...' : '💾 Save Template splits'}
                </button>
              </div>

            </form>
          </div>
        </div>
      )}

      {/* Transaction Ledger Modal */}
      {showTxModal && selectedStudent && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.5)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 9999, padding: '16px' }}>
          <div className="card" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '900px', width: '100%', maxHeight: '90vh', display: 'flex', flexDirection: 'column', boxShadow: 'var(--shadow-lg)' }}>
            
            <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold' }}>
                💸 Ledger Logs & Receipts: {selectedStudent.name}
              </h3>
              <button style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }} onClick={() => setShowTxModal(false)}>×</button>
            </div>

            <div style={{ padding: '20px', overflowY: 'auto', display: 'grid', gridTemplateColumns: '1fr 1.5fr', gap: '24px', flex: 1 }}>
              
              {/* Record transaction log form */}
              <form onSubmit={handleSaveTransaction} style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
                <h4 style={{ margin: 0, fontSize: '12px', textTransform: 'uppercase', color: 'var(--text-muted)' }}>
                  {editingTx ? '✏️ Edit Logged Payment' : '➕ Record Payment Log'}
                </h4>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  <label style={{ fontSize: '11px', fontWeight: 600 }}>Payment Area / Installment</label>
                  <select
                    value={txInstId}
                    onChange={(e) => setTxInstId(e.target.value)}
                    style={{ padding: '8px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                  >
                    {customInstallments.map((inst, idx) => (
                      <option key={idx} value={inst.installmentId || `inst_${idx + 1}`}>Installment {idx + 1} (₹{inst.amount})</option>
                    ))}
                  </select>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  <label style={{ fontSize: '11px', fontWeight: 600 }}>Amount Paid (₹)</label>
                  <input
                    type="number"
                    required
                    value={txAmount === 0 ? '' : (txAmount ?? '')}
                    onChange={(e) => {
                      const raw = e.target.value;
                      setTxAmount(raw === '' ? '' as any : Number(raw));
                    }}
                    style={{ padding: '8px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                  />
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  <label style={{ fontSize: '11px', fontWeight: 600 }}>Payment Date</label>
                  <DateInputDMY
                    required
                    value={txDate}
                    onChange={(val) => setTxDate(val)}
                    style={{ width: '100%' }}
                  />
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px' }}>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                    <label style={{ fontSize: '11px', fontWeight: 600 }}>Method</label>
                    <select
                      value={txMethod}
                      onChange={(e) => setTxMethod(e.target.value)}
                      style={{ padding: '8px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                    >
                      <option value="UPI">UPI / GPay</option>
                      <option value="Cash">Cash</option>
                      <option value="Cheque">Cheque</option>
                      <option value="NetBanking">Net Banking</option>
                    </select>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                    <label style={{ fontSize: '11px', fontWeight: 600 }}>Ref ID / Receipt</label>
                    <input
                      type="text"
                      value={txRef}
                      onChange={(e) => setTxRef(e.target.value)}
                      placeholder="e.g. UPI12938129"
                      style={{ padding: '8px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                    />
                  </div>
                </div>

                <div style={{ display: 'flex', gap: '8px', marginTop: '10px' }}>
                  {editingTx && (
                    <button type="button" className="btn btn-secondary" style={{ flex: 1 }} onClick={() => {
                      setEditingTx(null);
                      setTxAmount(0);
                      setTxRef('');
                    }}>Cancel Edit</button>
                  )}
                  <button type="submit" className="btn btn-primary" style={{ flex: 1 }} disabled={savingTx}>
                    {savingTx ? 'Recording...' : editingTx ? 'Apply Changes' : 'Record Payment'}
                  </button>
                </div>
              </form>

              {/* Transactions List */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                <h4 style={{ margin: 0, fontSize: '12px', textTransform: 'uppercase', color: 'var(--text-muted)' }}>Payment Ledger Logs</h4>
                {loadingTransactions ? (
                  <div style={{ color: 'var(--text-faint)', fontSize: '12px', textAlign: 'center', padding: '20px' }}>Loading logs...</div>
                ) : transactions.length === 0 ? (
                  <div style={{ color: 'var(--text-faint)', fontSize: '12px', textAlign: 'center', padding: '20px' }}>No payment logs recorded.</div>
                ) : (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', maxHeight: '380px', overflowY: 'auto' }}>
                    {transactions.map(tx => (
                      <div key={tx.transactionId} className="card" style={{ padding: '12px', background: 'var(--bg-soft)', border: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <div>
                          <div style={{ fontSize: '13px', fontWeight: 'bold' }}>₹{tx.amountPaid} via <span style={{ color: 'var(--accent)' }}>{tx.paymentMethod}</span></div>
                          <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '2.5px' }}>
                            <strong>Log ID:</strong> {tx.transactionId}
                          </div>
                          <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                            <strong>Allocated to:</strong> {tx.installmentId?.startsWith('inst_') ? `Installment #${tx.installmentId.replace('inst_', '')}` : (tx.installmentId === 'registration' ? 'Installment #1' : (tx.installmentId || '--'))}
                          </div>
                          {tx.referenceNumber && (
                            <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                              <strong>Ref:</strong> {tx.referenceNumber}
                            </div>
                          )}
                          <div style={{ fontSize: '10px', color: 'var(--text-faint)', marginTop: '2.5px' }}>
                            {formatDateStr(tx.timestamp)} {new Date(tx.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })} by {tx.recordedBy}
                          </div>
                        </div>

                        <div style={{ display: 'flex', gap: '4px' }}>
                          <button
                            onClick={() => {
                              setEditingTx(tx);
                              setTxInstId(tx.installmentId || 'inst_1');
                              setTxAmount(tx.amountPaid);
                              setTxRef(tx.referenceNumber);
                              setTxMethod(tx.paymentMethod);
                              setTxDate(tx.timestamp ? getDateKeyIST(tx.timestamp) : getDateKeyIST());
                            }}
                            style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.05rem' }}
                            title="Edit payment log"
                          >
                            ✏️
                          </button>
                          <button
                            onClick={() => handleDeleteTransaction(tx.transactionId)}
                            style={{ border: 'none', background: 'transparent', color: 'var(--danger)', cursor: 'pointer', fontSize: '1.05rem' }}
                            title="Delete payment log"
                          >
                            🗑️
                          </button>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>

            </div>

          </div>
        </div>
      )}

    </div>
  );
}

export default function AdminFeesPage() {
  return (
    <Suspense fallback={
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>Loading...</div>
      </div>
    }>
      <AdminFeesContent />
    </Suspense>
  );
}

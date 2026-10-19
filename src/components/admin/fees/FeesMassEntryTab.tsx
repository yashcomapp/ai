'use client';

import React from 'react';
import DateInputDMY from '@/components/DateInputDMY';
import { renderSortHeader, getStatusWeight, StudentFeeRecord } from '@/lib/feesUtils';
import { formatDateDMY as formatDateStr } from '@/lib/dateUtils';
import { FeeTemplate } from './FeesTemplatesTab';

interface BulkPaymentItem {
  checked: boolean;
  amount: number;
  method: string;
  ref: string;
  component: string;
}

interface FeesMassEntryTabProps {
  students: StudentFeeRecord[];
  templates: FeeTemplate[];
  uniqueClasses: string[];
  bulkClass: string;
  setBulkClass: (cls: string) => void;
  bulkPayments: Record<string, BulkPaymentItem>;
  setBulkPayments: React.Dispatch<React.SetStateAction<Record<string, BulkPaymentItem>>>;
  bulkSelectedInstallment: string;
  setBulkSelectedInstallment: (instId: string) => void;
  bulkPaymentDate: string;
  setBulkPaymentDate: (d: string) => void;
  bulkSortField: string;
  bulkSortDir: 'asc' | 'desc';
  handleBulkSort: (field: any) => void;
  handleSaveBulkPayments: () => void | Promise<void>;
  savingBulk: boolean;
}

export default function FeesMassEntryTab({
  students,
  templates,
  uniqueClasses,
  bulkClass,
  setBulkClass,
  bulkPayments,
  setBulkPayments,
  bulkSelectedInstallment,
  setBulkSelectedInstallment,
  bulkPaymentDate,
  setBulkPaymentDate,
  bulkSortField,
  bulkSortDir,
  handleBulkSort,
  handleSaveBulkPayments,
  savingBulk
}: FeesMassEntryTabProps) {
  const filteredStudents = students.filter(s => String(s.classNum).trim() === String(bulkClass).trim());

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

  // Helper to resolve specific installment amount for a student (supporting custom fee matrix)
  const getStudentInstallmentAmount = (s: StudentFeeRecord, installmentId: string, defaultAmount: number): number => {
    if (s.fee?.installments && s.fee.installments.length > 0) {
      const instNo = parseInt(installmentId.replace('inst_', ''), 10);
      const matched = s.fee.installments.find(i => 
        (i.installmentId && i.installmentId === installmentId) ||
        (i.installmentNo && i.installmentNo === instNo) ||
        (`inst_${i.installmentNo}` === installmentId)
      );
      if (matched && typeof matched.amount === 'number') {
        return matched.amount;
      }
    }
    return defaultAmount;
  };

  const selectedOpt = bulkInstallmentOptions.find(o => o.id === bulkSelectedInstallment) || bulkInstallmentOptions[0];

  const sortedFilteredStudents = [...filteredStudents].sort((a, b) => {
    let valA: any = '';
    let valB: any = '';
    if (bulkSortField === 'name') {
      valA = (a.name || '').toLowerCase();
      valB = (b.name || '').toLowerCase();
    } else if (bulkSortField === 'status') {
      valA = getStatusWeight(a);
      valB = getStatusWeight(b);
    }
    if (valA < valB) return bulkSortDir === 'asc' ? -1 : 1;
    if (valA > valB) return bulkSortDir === 'asc' ? 1 : -1;
    return 0;
  });

  return (
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
            {(uniqueClasses.length > 0 ? uniqueClasses : ['8', '9', '10', '11', '12']).map(cls => (
              <option key={cls} value={cls}>Class {cls}</option>
            ))}
          </select>
        </div>
      </div>

      {filteredStudents.length === 0 ? (
        <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>
          No active student records found for Class {bulkClass}.
        </div>
      ) : (
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
                  const defAmt = matchingOpt?.amount || 0;
                  setBulkPayments(prev => {
                    const next = { ...prev };
                    filteredStudents.forEach(s => {
                      const sCode = s.studentCode;
                      if (next[sCode]) {
                        const studentAmt = getStudentInstallmentAmount(s, val, defAmt);
                        next[sCode] = {
                          ...next[sCode],
                          amount: next[sCode].checked ? studentAmt : 0,
                          component: val
                        };
                      }
                    });
                    return next;
                  });
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
              Standard Template Rate: <strong style={{ color: 'var(--accent)', fontSize: '13px' }}>₹{selectedOpt.amount}</strong>
              <span style={{ fontSize: '11px', color: 'var(--text-muted)', marginLeft: '8px' }}>(Students with custom matrices auto-populate their individual rate)</span>
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
                          const matchingInst = s.fee?.installments?.find((inst: any) => inst.installmentId === selectedOpt.id || (inst.installmentNo && `inst_${inst.installmentNo}` === selectedOpt.id));
                          const isInstPaid = matchingInst?.status === 'paid';
                          
                          // Do not auto-select students who have already paid this installment
                          if (checked && isInstPaid) {
                            return;
                          }

                          const studentAmt = getStudentInstallmentAmount(s, selectedOpt.id, selectedOpt.amount);
                          next[sCode] = {
                            checked,
                            amount: checked ? (next[sCode]?.amount > 0 ? next[sCode].amount : studentAmt) : 0,
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
                {sortedFilteredStudents.map(s => {
                  const sCode = s.studentCode;
                  const studentInstAmt = getStudentInstallmentAmount(s, selectedOpt.id, selectedOpt.amount);
                  const matchingInst = s.fee?.installments?.find((inst: any) => inst.installmentId === selectedOpt.id || (inst.installmentNo && `inst_${inst.installmentNo}` === selectedOpt.id));
                  const isInstPaid = matchingInst?.status === 'paid';

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

                  const isCustomized = s.fee?.installments && studentInstAmt !== selectedOpt.amount;

                  return (
                    <tr key={sCode} style={{ borderBottom: '1px solid var(--border-light)', background: isInstPaid ? 'rgba(16, 185, 129, 0.04)' : (payment.checked ? 'var(--bg-soft)' : 'transparent') }}>
                      <td style={{ padding: '14px 16px' }}>
                        <input
                          type="checkbox"
                          checked={payment.checked}
                          disabled={isInstPaid}
                          title={isInstPaid ? 'This installment is already settled' : undefined}
                          onChange={(e) => {
                            const checked = e.target.checked;
                            updateField('checked', checked);
                            updateField('amount', checked ? (payment.amount > 0 ? payment.amount : studentInstAmt) : 0);
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
                            {isInstPaid && (
                              <div style={{ marginTop: '3px' }}>
                                <span style={{ background: 'rgba(16, 185, 129, 0.15)', color: 'var(--success)', padding: '2px 8px', borderRadius: '10px', fontSize: '10px', fontWeight: 700 }}>
                                  ✓ {selectedOpt.label} Paid
                                </span>
                              </div>
                            )}
                          </div>
                        ) : (
                          <span style={{ fontStyle: 'italic', color: 'var(--text-faint)' }}>Not Configured</span>
                        )}
                      </td>
                      <td style={{ padding: '14px 16px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap' }}>
                          <input
                            type="number"
                            min="0"
                            disabled={!payment.checked}
                            value={payment.checked ? (payment.amount ?? '') : ''}
                            onChange={(e) => {
                              const raw = e.target.value;
                              const val = raw === '' ? 0 : Number(raw);
                              updateField('amount', val);
                            }}
                            placeholder={payment.checked ? '0' : '--'}
                            style={{
                              padding: '6px 8px',
                              borderRadius: '4px',
                              border: '1px solid var(--border-light)',
                              background: payment.checked ? 'var(--surface)' : 'var(--bg-soft)',
                              color: payment.checked ? 'var(--text)' : 'var(--text-muted)',
                              width: '90px',
                              fontSize: '12px',
                              fontWeight: 600
                            }}
                          />
                          {isCustomized && (
                            <span 
                              title={`Custom installment amount for ${s.name}: ₹${studentInstAmt} (Standard template rate is ₹{selectedOpt.amount})`}
                              style={{ fontSize: '10px', padding: '2px 6px', borderRadius: '4px', background: 'rgba(168, 85, 247, 0.15)', color: 'var(--purple)', fontWeight: 700, whiteSpace: 'nowrap' }}
                            >
                              Custom ₹{studentInstAmt}
                            </span>
                          )}
                        </div>
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
                })}
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
      )}
    </div>
  );
}

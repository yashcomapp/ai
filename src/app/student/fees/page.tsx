'use client';

import React, { useState, useEffect } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import useSWR from 'swr';
import { fetchWithToken } from '@/lib/swrFetcher';
import { formatDateDMY as formatDateStr } from '@/lib/dateUtils';

export default function StudentFeesPage() {
  const { firebaseUser, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();

  const fetcher = async (url: string) => {
    return fetchWithToken(url, firebaseUser);
  };

  const { data, error, isLoading } = useSWR<any>(
    firebaseUser ? '/api/student/fees' : null,
    fetcher
  );

  const fee = data?.feeRecord || null;
  const transactions = data?.transactions || [];

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Top Header Bar matching Review Page */}
      <div className="page-header glass" style={{ padding: '8px 16px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderRadius: '0', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <button 
            onClick={() => router.push('/student')}
            style={{
              background: 'transparent',
              border: 'none',
              color: 'var(--text)',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              padding: '6px',
              borderRadius: '50%',
              transition: 'background 0.2s'
            }}
            title="Back to Dashboard"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>
          </button>
          <span className="brand" style={{ fontWeight: 800, fontSize: '1.1rem', color: 'var(--accent)', cursor: 'pointer' }} onClick={() => router.push('/student')}>YASHCOM</span>
        </div>
        <div className="page-header-right" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          
          <button className="btn btn-secondary logout-btn" onClick={() => logout()} style={{ fontSize: '1rem', padding: '6px 10px', display: 'flex', alignItems: 'center', justifyContent: 'center' }} title="Logout">🚪</button>
        </div>
      </div>

      <div style={{ flex: 1, padding: '24px 12px' }}>
        <div style={{ maxWidth: '900px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '20px' }}>

        {error && <div className="alert-box alert-box-danger">Failed to load fees details.</div>}

        {isLoading ? (
          <div style={{ padding: '60px', textAlign: 'center', color: 'var(--text-muted)' }}>Loading fees register...</div>
        ) : !fee ? (
          <div className="card" style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)', background: 'var(--surface)' }}>
            🪙 No active package configured for your account yet. Please contact the administrator.
          </div>
        ) : (
          <>
            {/* Summary Row */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '12px' }}>
              <div className="card" style={{ background: 'var(--surface)', padding: '16px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '4px', alignItems: 'center', textAlign: 'center' }}>
                <span style={{ fontSize: '10px', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 800 }}>Net Payable Rate</span>
                <span style={{ fontSize: '1.45rem', fontWeight: 800, color: 'var(--text)' }}>₹{fee.netPayableAmount}</span>
                <span style={{ fontSize: '10px', color: 'var(--text-faint)' }}>Package: ₹{fee.totalPackageAmount} | Disc: ₹{fee.discountAmount}</span>
              </div>
              <div className="card" style={{ background: 'var(--surface)', padding: '16px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '4px', alignItems: 'center', textAlign: 'center' }}>
                <span style={{ fontSize: '10px', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 800 }}>Total Paid</span>
                <span style={{ fontSize: '1.45rem', fontWeight: 800, color: 'var(--success)' }}>₹{fee.totalPaidAmount}</span>
              </div>
              <div className="card" style={{ background: 'var(--surface)', padding: '16px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '4px', alignItems: 'center', textAlign: 'center' }}>
                <span style={{ fontSize: '10px', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 800 }}>Outstanding Balance</span>
                <span style={{ fontSize: '1.45rem', fontWeight: 800, color: fee.outstandingAmount > 0 ? 'var(--danger)' : 'var(--success)' }}>₹{fee.outstandingAmount}</span>
              </div>
            </div>

            {/* Overdue alert */}
            {fee.hasOverdueInstallment && (
              <div className="alert-box alert-box-danger" style={{ display: 'block', margin: 0, fontWeight: 700 }}>
                ⚠️ ATTENTION: You have overdue installments pending. Please clear your outstanding dues as soon as possible.
              </div>
            )}

            {/* Registration Fee Box */}
            {fee.registrationFee && (
              <div className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', padding: '16px 20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div>
                  <h4 style={{ margin: 0, fontSize: '13px', fontWeight: 'bold' }}>🔑 Registration Fee</h4>
                  <p style={{ margin: '2px 0 0 0', fontSize: '11px', color: 'var(--text-muted)' }}>Initial seat booking rate</p>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                  <strong style={{ fontSize: '14px' }}>₹{fee.registrationFee.amount}</strong>
                  {fee.registrationFee.status === 'paid' ? (
                    <span className="badge badge-success" style={{ fontSize: '10px' }}>PAID</span>
                  ) : (
                    <span className="badge badge-secondary" style={{ fontSize: '10px' }}>PENDING</span>
                  )}
                </div>
              </div>
            )}

            {/* Installments schedule list */}
            <div className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', overflow: 'hidden' }}>
              <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)' }}>
                <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold' }}>📅 Installments Dues Timeline</h3>
              </div>
              <div style={{ overflowX: 'auto' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                  <thead>
                    <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', fontSize: '11px', color: 'var(--text-muted)' }}>
                      <th style={{ padding: '12px 16px' }}>INSTALLMENT</th>
                      <th style={{ padding: '12px 16px' }}>DUE AMOUNT</th>
                      <th style={{ padding: '12px 16px' }}>DUE DATE</th>
                      <th style={{ padding: '12px 16px' }}>STATUS</th>
                    </tr>
                  </thead>
                  <tbody>
                    {fee.installments?.map((inst: any, idx: number) => (
                      <tr key={idx} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '14px 16px', fontSize: '13px', fontWeight: 'bold' }}>Installment {inst.installmentNo}</td>
                        <td style={{ padding: '14px 16px', fontSize: '13px', fontWeight: 700 }}>₹{inst.amount}</td>
                        <td style={{ padding: '14px 16px', fontSize: '13px' }}>{formatDateStr(inst.dueDate)}</td>
                        <td style={{ padding: '14px 16px' }}>
                          {inst.status === 'paid' ? (
                            <span className="badge badge-success" style={{ fontSize: '10px' }}>PAID</span>
                          ) : inst.status === 'overdue' ? (
                            <span className="badge badge-danger" style={{ fontSize: '10px' }}>OVERDUE</span>
                          ) : (
                            <span className="badge badge-secondary" style={{ fontSize: '10px' }}>PENDING</span>
                          )}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            {/* Payment history list */}
            <div className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', overflow: 'hidden' }}>
              <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)' }}>
                <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold' }}>🧾 Logged Ledger Receipts</h3>
              </div>
              {transactions.length === 0 ? (
                <div style={{ padding: '30px', textAlign: 'center', color: 'var(--text-faint)', fontSize: '12px' }}>No payments logged yet.</div>
              ) : (
                <div style={{ overflowX: 'auto' }}>
                  <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                    <thead>
                      <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', fontSize: '11px', color: 'var(--text-muted)' }}>
                        <th style={{ padding: '12px 16px' }}>RECEIPT ID</th>
                        <th style={{ padding: '12px 16px' }}>ALLOCATED DUES</th>
                        <th style={{ padding: '12px 16px' }}>METHOD</th>
                        <th style={{ padding: '12px 16px' }}>REF / TR REF</th>
                        <th style={{ padding: '12px 16px' }}>AMOUNT PAID</th>
                        <th style={{ padding: '12px 16px' }}>DATE LOGGED</th>
                      </tr>
                    </thead>
                    <tbody>
                      {transactions.map((tx: any) => (
                        <tr key={tx.transactionId} style={{ borderBottom: '1px solid var(--border-light)', fontSize: '13px' }}>
                          <td style={{ padding: '14px 16px', fontWeight: 'bold', fontFamily: 'monospace' }}>{tx.transactionId}</td>
                          <td style={{ padding: '14px 16px' }}>
                            {tx.installmentId === 'registration' ? 'Registration Fee' : tx.installmentId}
                          </td>
                          <td style={{ padding: '14px 16px' }}>{tx.paymentMethod}</td>
                          <td style={{ padding: '14px 16px', color: 'var(--text-muted)' }}>{tx.referenceNumber || '--'}</td>
                          <td style={{ padding: '14px 16px', color: 'var(--success)', fontWeight: 700 }}>₹{tx.amountPaid}</td>
                          <td style={{ padding: '14px 16px', color: 'var(--text-faint)' }}>{formatDateStr(tx.timestamp)}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </div>
          </>
        )}

        </div>
      </div>
    </div>
  );
}

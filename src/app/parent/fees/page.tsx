'use client';

import React, { useState, useEffect, Suspense } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter, useSearchParams } from 'next/navigation';
import useSWR from 'swr';
import { fetchWithToken, createTokenFetcher } from '@/lib/swrFetcher';
import { formatDateDMY as formatDateStr } from '@/lib/dateUtils';
import { ParentPageShell } from '@/components/parent';

function ParentFeesContent() {
  const { firebaseUser, user, logout } = useAuth();
  const router = useRouter();
  const searchParams = useSearchParams();

  const parentCodes = (user as any)?.studentCodes || ((user as any)?.studentCode ? [(user as any)?.studentCode] : []);
  const defaultCode = searchParams.get('studentCode') || parentCodes[0] || '';
  const [selectedChildCode, setSelectedChildCode] = useState(defaultCode);

  useEffect(() => {
    if (defaultCode && defaultCode !== selectedChildCode) {
      setSelectedChildCode(defaultCode);
    }
  }, [defaultCode]);

  const fetcher = createTokenFetcher(firebaseUser);

  // SWR for parent children name mapping
  const { data: parentDashboardData } = useSWR<any>(
    firebaseUser ? '/api/parent/dashboard' : null,
    fetcher,
    { revalidateOnFocus: false, dedupingInterval: 60000 }
  );
  const childrenList = parentDashboardData?.children || [];

  // Map studentCode -> name
  const childNameMap: Record<string, string> = {};
  childrenList.forEach((c: any) => {
    if (c.studentCode) {
      childNameMap[c.studentCode.toUpperCase()] = c.name || c.studentCode;
    }
  });

  const getChildName = (code: string) => {
    const upper = String(code).trim().toUpperCase();
    return childNameMap[upper] || upper;
  };

  const displayName = getChildName(selectedChildCode);

  const { data, error, isLoading } = useSWR<any>(
    firebaseUser && selectedChildCode ? `/api/student/fees?studentCode=${selectedChildCode}` : null,
    fetcher,
    { revalidateOnFocus: false, dedupingInterval: 60000 }
  );

  const fee = data?.feeRecord || null;
  const transactions = data?.transactions || [];

  return (
    <ParentPageShell maxWidth="900px">
      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>

        {/* Child Selector */}
        {parentCodes.length > 1 && (
          <div className="card" style={{ padding: '8px 12px', background: 'var(--surface)', display: 'flex', alignItems: 'center', gap: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius)' }}>
            <span style={{ fontSize: '11.5px', fontWeight: 'bold' }}>Select Student:</span>
            <select
              value={selectedChildCode}
              onChange={(e) => setSelectedChildCode(e.target.value)}
              style={{ padding: '4px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '11.5px', fontWeight: 600 }}
            >
              {parentCodes.map((code: string) => {
                const childName = getChildName(code);
                return (
                  <option key={code} value={code}>{childName}</option>
                );
              })}
            </select>
          </div>
        )}

        {error && <div className="alert-box alert-box-danger">Failed to load child's fees details.</div>}

        {isLoading ? (
          <div style={{ padding: '24px 12px', textAlign: 'center', color: 'var(--text-muted)' }}>Loading fees statement...</div>
        ) : !fee ? (
          <div className="card" style={{ padding: '20px 12px', textAlign: 'center', color: 'var(--text-muted)', background: 'var(--surface)' }}>
            🪙 No active package configured for {displayName} yet. Please contact the administrator.
          </div>
        ) : (
          <>
            {/* Summary Row */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '8px' }}>
              <div className="card" style={{ background: 'var(--surface)', padding: '10px 8px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '2px', alignItems: 'center', textAlign: 'center' }}>
                <span style={{ fontSize: '10px', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 800 }}>Net Payable Rate • कुल देय शुल्क</span>
                <span style={{ fontSize: '1.3rem', fontWeight: 800, color: 'var(--text)' }}>₹{fee.netPayableAmount}</span>
                <span style={{ fontSize: '10px', color: 'var(--text-faint)' }}>Package: ₹{fee.totalPackageAmount} | Disc: ₹{fee.discountAmount}</span>
              </div>
              <div className="card" style={{ background: 'var(--surface)', padding: '10px 8px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '2px', alignItems: 'center', textAlign: 'center' }}>
                <span style={{ fontSize: '10px', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 800 }}>Total Paid • कुल जमा राशि</span>
                <span style={{ fontSize: '1.3rem', fontWeight: 800, color: 'var(--success)' }}>₹{fee.totalPaidAmount}</span>
              </div>
              <div className="card" style={{ background: 'var(--surface)', padding: '10px 8px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '2px', alignItems: 'center', textAlign: 'center' }}>
                <span style={{ fontSize: '10px', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 800 }}>Outstanding Balance • बकाया राशि</span>
                <span style={{ fontSize: '1.3rem', fontWeight: 800, color: fee.outstandingAmount > 0 ? 'var(--danger)' : 'var(--success)' }}>₹{fee.outstandingAmount}</span>
              </div>
            </div>

            {/* Overdue alert */}
            {fee.hasOverdueInstallment && (
              <div className="alert-box alert-box-danger" style={{ display: 'block', margin: 0, fontWeight: 700 }}>
                ⚠️ ATTENTION: Your child has overdue installments pending. Please clear these dues as soon as possible.
                <div style={{ fontSize: '11px', fontWeight: 500, marginTop: '2px' }}>
                  ध्यान दें: आपके पाल्य की फीस की किश्त बकाया है। कृपया इसे यथाशीघ्र जमा करें।
                </div>
              </div>
            )}


            {/* Installments schedule list */}
            <div className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', overflow: 'hidden' }}>
              <div style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
                <h3 style={{ margin: 0, fontSize: '13px', fontWeight: 'bold' }}>📅 Installments Dues Timeline • किश्त भुगतान समय-सारणी</h3>
              </div>
              <div style={{ overflowX: 'auto' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                  <thead>
                    <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', fontSize: '11px', color: 'var(--text-muted)' }}>
                      <th style={{ padding: '6px 10px' }}>INSTALLMENT • किश्त</th>
                      <th style={{ padding: '6px 10px' }}>DUE AMOUNT • देय राशि</th>
                      <th style={{ padding: '6px 10px' }}>DUE DATE • अंतिम तारीख</th>
                      <th style={{ padding: '6px 10px' }}>STATUS • स्थिति</th>
                    </tr>
                  </thead>
                  <tbody>
                    {fee.installments?.map((inst: any, idx: number) => (
                      <tr key={idx} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '6px 10px', fontSize: '12.5px', fontWeight: 'bold' }}>Installment {inst.installmentNo} (किश्त {inst.installmentNo})</td>
                        <td style={{ padding: '6px 10px', fontSize: '12.5px', fontWeight: 700 }}>₹{inst.amount}</td>
                        <td style={{ padding: '6px 10px', fontSize: '12.5px' }}>{formatDateStr(inst.dueDate)}</td>
                        <td style={{ padding: '6px 10px' }}>
                          {inst.status === 'paid' ? (
                            <span className="badge badge-success" style={{ fontSize: '10px' }}>PAID • जमा</span>
                          ) : inst.status === 'overdue' ? (
                            <span className="badge badge-danger" style={{ fontSize: '10px' }}>OVERDUE • बकाया</span>
                          ) : (
                            <span className="badge badge-secondary" style={{ fontSize: '10px' }}>PENDING • आगामी</span>
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
              <div style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
                <h3 style={{ margin: 0, fontSize: '13px', fontWeight: 'bold' }}>🧾 Logged Receipts History • फीस भुगतान रसीदें</h3>
              </div>
              {transactions.length === 0 ? (
                <div style={{ padding: '16px', textAlign: 'center', color: 'var(--text-faint)', fontSize: '12px' }}>No payments logged yet. • अभी तक कोई रसीद दर्ज नहीं है।</div>
              ) : (
                <div style={{ overflowX: 'auto' }}>
                  <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                    <thead>
                      <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', fontSize: '11px', color: 'var(--text-muted)' }}>
                        <th style={{ padding: '6px 10px' }}>RECEIPT ID • रसीद क्र.</th>
                        <th style={{ padding: '6px 10px' }}>ALLOCATED DUES • किश्त</th>
                        <th style={{ padding: '6px 10px' }}>METHOD • माध्यम</th>
                        <th style={{ padding: '6px 10px' }}>REF / TR REF</th>
                        <th style={{ padding: '6px 10px' }}>AMOUNT PAID • जमा</th>
                        <th style={{ padding: '6px 10px' }}>DATE LOGGED • तारीख</th>
                      </tr>
                    </thead>
                    <tbody>
                      {transactions.map((tx: any) => (
                        <tr key={tx.transactionId} style={{ borderBottom: '1px solid var(--border-light)', fontSize: '12.5px' }}>
                          <td style={{ padding: '6px 10px', fontWeight: 'bold', fontFamily: 'monospace' }}>{tx.transactionId}</td>
                          <td style={{ padding: '6px 10px' }}>
                            {tx.installmentId?.startsWith('inst_') ? `Installment ${tx.installmentId.replace('inst_', '')}` : (tx.installmentId === 'registration' ? 'Installment 1' : (tx.installmentId || '--'))}
                          </td>
                          <td style={{ padding: '6px 10px' }}>{tx.paymentMethod}</td>
                          <td style={{ padding: '6px 10px', color: 'var(--text-muted)' }}>{tx.referenceNumber || '--'}</td>
                          <td style={{ padding: '6px 10px', color: 'var(--success)', fontWeight: 700 }}>₹{tx.amountPaid}</td>
                          <td style={{ padding: '6px 10px', color: 'var(--text-faint)' }}>{formatDateStr(tx.timestamp)}</td>
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
    </ParentPageShell>
  );
}

export default function ParentFeesPage() {
  return (
    <Suspense fallback={<div style={{ padding: '20px 12px', textAlign: 'center', color: 'var(--text-muted)' }}>Loading fees register...</div>}>
      <ParentFeesContent />
    </Suspense>
  );
}

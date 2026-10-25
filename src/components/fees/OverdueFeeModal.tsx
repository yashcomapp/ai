'use client';

import React from 'react';
import { useRouter } from 'next/navigation';

export interface OverdueFeeModalProps {
  isOpen: boolean;
  onDismiss: () => void;
  outstandingAmount: number | string;
  role?: 'student' | 'parent';
  studentCode?: string;
}

export function OverdueFeeModal({
  isOpen,
  onDismiss,
  outstandingAmount,
  role = 'student',
  studentCode
}: OverdueFeeModalProps) {
  const router = useRouter();

  if (!isOpen) return null;

  const isParent = role === 'parent';
  const targetHref = isParent && studentCode
    ? `/parent/fees?studentCode=${encodeURIComponent(studentCode)}`
    : isParent
    ? '/parent/fees'
    : '/student/fees';

  return (
    <div style={{
      position: 'fixed',
      inset: 0,
      background: 'rgba(0, 0, 0, 0.45)',
      backdropFilter: 'blur(8px)',
      WebkitBackdropFilter: 'blur(8px)',
      zIndex: 99999,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '20px'
    }}>
      <div className="card" style={{
        background: 'var(--surface-popover)',
        border: '1px solid var(--border-popover)',
        borderRadius: 'var(--radius-lg)',
        padding: '28px',
        maxWidth: '500px',
        width: '100%',
        textAlign: 'center',
        boxShadow: 'var(--shadow-lg)'
      }}>
        <span style={{ fontSize: '3rem', display: 'block', marginBottom: '16px' }}>{isParent ? '💳' : '🪙'}</span>
        <h2 style={{ fontSize: isParent ? '1.35rem' : '1.45rem', fontWeight: 800, color: 'var(--danger)', margin: '0 0 10px 0' }}>
          Fee Installment Overdue
          {isParent && (
            <>
              <br />
              <span style={{ fontSize: '1rem', fontWeight: 700 }}>किश्त की अंतिम तारीख निकल चुकी है</span>
            </>
          )}
        </h2>
        <p style={{ fontSize: '13px', color: 'var(--text)', lineHeight: '1.6', margin: '0 0 20px 0' }}>
          {isParent ? (
            <>
              Your child&apos;s account has an outstanding overdue balance of <strong>₹{outstandingAmount || 0}</strong>. Please check the dues schedule and complete payment.<br />
              <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>आपके बच्चे के खाते में <strong>₹{outstandingAmount || 0}</strong> की बकाया फीस देय है। कृपया फीस विवरण देखकर भुगतान पूरा करें।</span>
            </>
          ) : (
            <>
              Your account has an outstanding overdue balance of <strong>₹{outstandingAmount || 0}</strong>. Please check your dues schedule and complete payment.
            </>
          )}
        </p>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <button 
            type="button"
            className="btn btn-primary" 
            onClick={() => {
              router.push(targetHref);
              onDismiss();
            }}
            style={{ width: '100%' }}
          >
            {isParent ? 'View Fees & Invoices / फीस और रसीद देखें' : 'View Fees & Invoices'}
          </button>
          <button 
            type="button"
            className="btn btn-secondary" 
            onClick={onDismiss}
            style={{ width: '100%' }}
          >
            {isParent ? 'Dismiss / हटाएं' : 'Dismiss'}
          </button>
        </div>
      </div>
    </div>
  );
}

export default OverdueFeeModal;

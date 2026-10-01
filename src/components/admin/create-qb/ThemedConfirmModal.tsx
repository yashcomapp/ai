'use client';

import React from 'react';

export interface ThemedConfirmModalProps {
  showConfirmModal: boolean;
  setShowConfirmModal: (show: boolean) => void;
  confirmTitle: string;
  confirmMessage: string;
  onConfirmCallback: (() => void) | null;
  onCancelCallback: (() => void) | null;
  setOnConfirmCallback: (cb: any) => void;
  setOnCancelCallback: (cb: any) => void;
}

export function ThemedConfirmModal({
  showConfirmModal,
  setShowConfirmModal,
  confirmTitle,
  confirmMessage,
  onConfirmCallback,
  onCancelCallback,
  setOnConfirmCallback,
  setOnCancelCallback,
}: ThemedConfirmModalProps) {
  if (!showConfirmModal) return null;

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 30000 }}>
      <div className="card" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '440px', width: '90%', display: 'flex', flexDirection: 'column', gap: '16px', boxShadow: '0 10px 25px rgba(0,0,0,0.2)' }}>
        <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 'bold', color: 'var(--text)', display: 'flex', alignItems: 'center', gap: '8px' }}>
          ❓ {confirmTitle || 'Confirm Action'}
        </h3>
        <p style={{ margin: 0, fontSize: '13px', color: 'var(--text-muted)', lineHeight: '1.5' }}>
          {confirmMessage}
        </p>
        <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '4px' }}>
          <button 
            type="button" 
            className="btn btn-secondary" 
            onClick={() => {
              setShowConfirmModal(false);
              if (onCancelCallback) onCancelCallback();
              setOnConfirmCallback(null);
              setOnCancelCallback(null);
            }}
          >
            Cancel
          </button>
          <button 
            type="button" 
            className="btn btn-primary" 
            onClick={() => {
              setShowConfirmModal(false);
              if (onConfirmCallback) onConfirmCallback();
              setOnConfirmCallback(null);
              setOnCancelCallback(null);
            }}
          >
            Confirm
          </button>
        </div>
      </div>
    </div>
  );
}

export default ThemedConfirmModal;

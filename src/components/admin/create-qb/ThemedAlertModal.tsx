'use client';

import React from 'react';

export interface ThemedAlertModalProps {
  showAlertModal: boolean;
  setShowAlertModal: (show: boolean) => void;
  alertTitle: string;
  alertMessage: string;
  alertHasOkButton: boolean;
  onAlertCloseCallback: (() => void) | null;
  setOnAlertCloseCallback: (cb: any) => void;
}

export function ThemedAlertModal({
  showAlertModal,
  setShowAlertModal,
  alertTitle,
  alertMessage,
  alertHasOkButton,
  onAlertCloseCallback,
  setOnAlertCloseCallback,
}: ThemedAlertModalProps) {
  if (!showAlertModal) return null;

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 30000 }}>
      <div className="card" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '440px', width: '90%', display: 'flex', flexDirection: 'column', gap: '16px', boxShadow: '0 10px 25px rgba(0,0,0,0.2)' }}>
        <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 'bold', color: 'var(--text)', display: 'flex', alignItems: 'center', gap: '8px' }}>
          {alertTitle?.toLowerCase().includes('success') ? '✅' : '⚠️'} {alertTitle || 'Notice'}
        </h3>
        <p style={{ margin: 0, fontSize: '13px', color: 'var(--text-muted)', lineHeight: '1.5' }}>
          {alertMessage}
        </p>
        {alertHasOkButton && (
          <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '4px' }}>
            <button 
              type="button" 
              className="btn btn-primary" 
              onClick={() => {
                setShowAlertModal(false);
                if (onAlertCloseCallback) onAlertCloseCallback();
                setOnAlertCloseCallback(null);
              }}
            >
              OK
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default ThemedAlertModal;

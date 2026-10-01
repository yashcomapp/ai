'use client';

import React from 'react';

export interface BulkSaveProgressModalProps {
  savingProgress: boolean;
  savePercentage: number;
  saveStats: { current: number; total: number };
}

export function BulkSaveProgressModal({
  savingProgress,
  savePercentage,
  saveStats,
}: BulkSaveProgressModalProps) {
  if (!savingProgress) return null;

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.8)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', padding: '30px', maxWidth: '420px', width: '90%', textAlign: 'center', border: '1px solid var(--border-light)', margin: 'auto' }}>
        <h3 style={{ margin: '0 0 6px', color: 'var(--text)', fontSize: '16px' }}>💾 Saving Questions...</h3>
        <p style={{ fontSize: '12px', color: 'var(--text-muted)', marginBottom: '18px' }}>
          Writing database records sequentially. Do not close this browser tab.
        </p>
        <div style={{ width: '100%', height: '14px', borderRadius: '8px', background: 'var(--bg-soft)', overflow: 'hidden', border: '1px solid var(--border-light)' }}>
          <div style={{ height: '100%', width: `${savePercentage}%`, background: 'var(--accent)', borderRadius: '8px', transition: 'width 0.2s ease' }} />
        </div>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '10px', fontSize: '11px', color: 'var(--text-muted)' }}>
          <span>Progress: {savePercentage}%</span>
          <span>{saveStats.current} / {saveStats.total} Saved</span>
        </div>
      </div>
    </div>
  );
}

export default BulkSaveProgressModal;

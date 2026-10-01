'use client';

import React from 'react';

export interface BulkSaveProgressModalProps {
  qbSaving: boolean;
  saveStats: { current: number; total: number };
}

export function BulkSaveProgressModal({ qbSaving, saveStats }: BulkSaveProgressModalProps) {
  if (!qbSaving || saveStats.total <= 0) return null;

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.8)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '16px' }}>
      <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', padding: '30px', maxWidth: '440px', width: '90%', textAlign: 'center', border: '1px solid var(--border-light)', margin: 'auto' }}>
        <h3 style={{ margin: '0 0 6px', color: 'var(--text)', fontSize: '16px', fontWeight: 800 }}>💾 Saving Questions to Question Bank...</h3>
        <p style={{ fontSize: '12px', color: 'var(--text-muted)', marginBottom: '18px' }}>
          Writing database records sequentially. Please do not close or refresh this tab.
        </p>
        <div style={{ width: '100%', height: '14px', borderRadius: '8px', background: 'var(--bg-soft)', overflow: 'hidden', border: '1px solid var(--border-light)' }}>
          <div style={{ height: '100%', width: `${Math.round((saveStats.current / saveStats.total) * 100)}%`, background: 'var(--accent)', borderRadius: '8px', transition: 'width 0.2s ease' }} />
        </div>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '10px', fontSize: '11px', color: 'var(--text-muted)', fontWeight: 700 }}>
          <span>Progress: {Math.round((saveStats.current / saveStats.total) * 100)}%</span>
          <span>{saveStats.current} / {saveStats.total} Saved</span>
        </div>
      </div>
    </div>
  );
}

export default BulkSaveProgressModal;

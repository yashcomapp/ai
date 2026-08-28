import React from 'react';

export default function Loading() {
  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      minHeight: '80vh',
      background: 'var(--bg)',
      color: 'var(--text)',
      fontFamily: 'Inter, system-ui, -apple-system, sans-serif',
      gap: '16px'
    }}>
      <div 
        style={{
          width: '40px',
          height: '40px',
          borderRadius: '50%',
          border: '3px solid var(--border-light)',
          borderTopColor: 'var(--accent)',
          animation: 'spin 1s linear infinite'
        }}
      />
      <span style={{ fontSize: '13px', color: 'var(--text-muted)', fontWeight: 600 }}>
        Loading data...
      </span>
      <style>{`
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
}

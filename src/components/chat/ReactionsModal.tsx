'use client';

import React from 'react';

export interface ReactionsModalProps {
  showReactorsModal: {
    isOpen: boolean;
    thumbsup: string[];
    pray: string[];
  } | null;
  setShowReactorsModal: (val: any) => void;
  participantNames: Record<string, string>;
}

export function ReactionsModal({
  showReactorsModal,
  setShowReactorsModal,
  participantNames,
}: ReactionsModalProps) {
  if (!showReactorsModal || !showReactorsModal.isOpen) return null;

  return (
    <div 
      style={{ 
        position: 'fixed', 
        inset: 0, 
        background: 'rgba(0, 0, 0, 0.6)', 
        backdropFilter: 'blur(4px)', 
        display: 'flex', 
        alignItems: 'center', 
        justifyContent: 'center', 
        zIndex: 99999, 
        padding: '16px' 
      }}
      onClick={() => setShowReactorsModal(null)}
    >
      <div 
        style={{ 
          background: 'var(--surface-popover)', 
          border: '1px solid var(--border)', 
          borderRadius: '12px', 
          maxWidth: '360px', 
          width: '100%', 
          boxShadow: '0 4px 24px rgba(0,0,0,0.3)', 
          color: 'var(--text)', 
          display: 'flex', 
          flexDirection: 'column' 
        }}
        onClick={(e) => e.stopPropagation()}
      >
        <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 700 }}>Message Reactions</h3>
          <button 
            style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.5rem', color: 'var(--text-muted)', lineHeight: 1 }} 
            onClick={() => setShowReactorsModal(null)}
          >
            ×
          </button>
        </div>
        <div style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '16px', maxHeight: '300px', overflowY: 'auto' }}>
          {showReactorsModal.thumbsup.length > 0 && (
            <div>
              <h4 style={{ fontSize: '13px', fontWeight: 650, color: 'var(--accent)', margin: '0 0 8px 0', display: 'flex', alignItems: 'center', gap: '6px' }}>
                👍 Thumbs Up ({showReactorsModal.thumbsup.length})
              </h4>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', paddingLeft: '8px' }}>
                {showReactorsModal.thumbsup.map(uid => (
                  <div key={uid} style={{ fontSize: '13.5px', color: 'var(--text)' }}>
                    • {participantNames[uid] || uid}
                  </div>
                ))}
              </div>
            </div>
          )}
          {showReactorsModal.pray.length > 0 && (
            <div>
              <h4 style={{ fontSize: '13px', fontWeight: 650, color: 'var(--warning)', margin: '0 0 8px 0', display: 'flex', alignItems: 'center', gap: '6px' }}>
                🙏 Folded Hands ({showReactorsModal.pray.length})
              </h4>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', paddingLeft: '8px' }}>
                {showReactorsModal.pray.map(uid => (
                  <div key={uid} style={{ fontSize: '13.5px', color: 'var(--text)' }}>
                    • {participantNames[uid] || uid}
                  </div>
                ))}
              </div>
            </div>
          )}
          {showReactorsModal.thumbsup.length === 0 && showReactorsModal.pray.length === 0 && (
            <div style={{ color: 'var(--text-muted)', fontSize: '13px', textAlign: 'center' }}>No reactions yet.</div>
          )}
        </div>
      </div>
    </div>
  );
}

export default ReactionsModal;

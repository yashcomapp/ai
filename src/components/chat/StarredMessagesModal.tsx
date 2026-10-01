'use client';

import React from 'react';

export interface StarredMessagesModalProps {
  showStarredModal: boolean;
  setShowStarredModal: (show: boolean) => void;
  messages: any[];
  starredMessageIds: Record<string, boolean>;
  toggleStarMessage: (messageId: string) => void;
  scrollToMessage: (messageId: string) => void;
}

export function StarredMessagesModal({
  showStarredModal,
  setShowStarredModal,
  messages,
  starredMessageIds,
  toggleStarMessage,
  scrollToMessage,
}: StarredMessagesModalProps) {
  if (!showStarredModal) return null;

  const starred = messages.filter(m => starredMessageIds[m.messageId]);

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.6)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 9999, padding: '16px' }}>
      <div style={{ background: 'var(--surface-popover)', border: '1px solid var(--border)', borderRadius: '12px', maxWidth: '480px', width: '100%', maxHeight: '85vh', display: 'flex', flexDirection: 'column', boxShadow: '0 4px 24px rgba(0,0,0,0.3)', color: 'var(--text)' }}>
        <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 700, color: 'var(--warning)' }}>★ Starred Messages</h3>
          <button style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.5rem', color: 'var(--text-muted)', lineHeight: 1 }} onClick={() => setShowStarredModal(false)}>×</button>
        </div>
        <div style={{ flex: 1, overflowY: 'auto', padding: '16px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
          {starred.length === 0 ? (
            <div style={{ color: 'var(--text-muted)', fontStyle: 'italic', fontSize: '13px', padding: '24px', textAlign: 'center' }}>No messages starred in this room.</div>
          ) : (
            starred.map(msg => (
              <div key={msg.messageId} style={{ background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: '8px', padding: '12px', display: 'flex', flexDirection: 'column', gap: '6px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
                  <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--accent)' }}>{msg.senderName}</span>
                  <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>{(() => {
                    const d = new Date(msg.createdAt);
                    if (isNaN(d.getTime())) return '';
                    const day = String(d.getDate()).padStart(2, '0');
                    const month = String(d.getMonth() + 1).padStart(2, '0');
                    return `${day}/${month}/${d.getFullYear()}`;
                  })()}</span>
                </div>
                <div style={{ fontSize: '13px', color: 'var(--text)', wordBreak: 'break-word' }}>
                  {msg.text}
                </div>
                <div style={{ display: 'flex', gap: '10px', justifyContent: 'flex-end', marginTop: '6px' }}>
                  <button
                    onClick={() => toggleStarMessage(msg.messageId)}
                    style={{ background: 'transparent', border: 'none', color: 'var(--danger)', fontSize: '11px', cursor: 'pointer' }}
                  >
                    Unstar
                  </button>
                  <button
                    onClick={() => {
                      setShowStarredModal(false);
                      scrollToMessage(msg.messageId);
                    }}
                    style={{ background: 'rgba(99, 102, 241, 0.15)', border: '1px solid rgba(99, 102, 241, 0.4)', borderRadius: '4px', color: 'var(--accent)', fontSize: '11px', padding: '3px 8px', cursor: 'pointer' }}
                  >
                    Go to Message →
                  </button>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default StarredMessagesModal;

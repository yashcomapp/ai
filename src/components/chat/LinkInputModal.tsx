'use client';

import React from 'react';

export interface LinkInputModalProps {
  showLinkModal: boolean;
  setShowLinkModal: (show: boolean) => void;
  linkUrl: string;
  setLinkUrl: (url: string) => void;
  linkLabel: string;
  setLinkLabel: (label: string) => void;
  onInsertLink: (url: string, label: string) => void;
}

export function LinkInputModal({
  showLinkModal,
  setShowLinkModal,
  linkUrl,
  setLinkUrl,
  linkLabel,
  setLinkLabel,
  onInsertLink,
}: LinkInputModalProps) {
  if (!showLinkModal) return null;

  return (
    <div style={{
      position: 'fixed',
      inset: 0,
      background: 'rgba(0, 0, 0, 0.6)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 10000,
      backdropFilter: 'blur(4px)',
      padding: '16px'
    }}>
      <div style={{
        background: 'var(--surface-popover)',
        border: '1px solid var(--border)',
        borderRadius: '12px',
        padding: '20px',
        width: '320px',
        display: 'flex',
        flexDirection: 'column',
        gap: '12px'
      }}>
        <h4 style={{ margin: '0 0 4px 0', fontSize: '14px', fontWeight: 'bold', color: 'var(--text)' }}>🔗 Insert Hyperlink</h4>
        
        <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
          <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Link Address:</span>
          <input 
            type="text"
            value={linkUrl}
            onChange={(e) => setLinkUrl(e.target.value)}
            placeholder="https://example.com"
            style={{ padding: '8px', fontSize: '16px', borderRadius: '6px', border: '1px solid var(--border)', background: 'var(--surface)', color: 'var(--text)', outline: 'none' }}
          />
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
          <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Display Text:</span>
          <input 
            type="text"
            value={linkLabel}
            onChange={(e) => setLinkLabel(e.target.value)}
            placeholder="Maharashtra Board Syllabus"
            style={{ padding: '8px', fontSize: '16px', borderRadius: '6px', border: '1px solid var(--border)', background: 'var(--surface)', color: 'var(--text)', outline: 'none' }}
          />
        </div>

        <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '8px' }}>
          <button
            type="button"
            onClick={() => {
              setShowLinkModal(false);
              setLinkUrl('');
              setLinkLabel('');
            }}
            style={{ padding: '6px 12px', fontSize: '12px', border: '1px solid var(--border)', background: 'transparent', color: 'var(--text-muted)', borderRadius: '6px', cursor: 'pointer' }}
          >
            Cancel
          </button>
          <button
            type="button"
            onClick={() => {
              if (!linkUrl) return;
              const display = linkLabel.trim() || linkUrl;
              onInsertLink(linkUrl, display);
              setShowLinkModal(false);
              setLinkUrl('');
              setLinkLabel('');
            }}
            style={{ padding: '6px 14px', fontSize: '12px', border: 'none', background: 'var(--accent)', color: 'var(--text-white)', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}
          >
            Insert Link
          </button>
        </div>
      </div>
    </div>
  );
}

export default LinkInputModal;

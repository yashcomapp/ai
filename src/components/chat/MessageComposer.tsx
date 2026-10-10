'use client';

import React from 'react';
import { Message } from './MessageItem';

interface MessageComposerProps {
  isMobile: boolean;
  isMessageSelectMode: boolean;
  isAllMessagesSelected?: boolean;
  onToggleSelectAllMessages?: () => void;
  selectedCount: number;
  onCancelSelect: () => void;
  onBulkDelete: () => void;
  handleSendMessage: (e: React.FormEvent) => void;
  showMentionSuggestions: boolean;
  mentionCandidates: any[];
  selectMention: (name: string) => void;
  replyingTo: Message | null;
  setReplyingTo: (msg: Message | null) => void;
  showAttachmentMenu: boolean;
  setShowAttachmentMenu: React.Dispatch<React.SetStateAction<boolean>>;
  fileInputRef: React.RefObject<HTMLInputElement | null>;
  handleFileUpload: (e: React.ChangeEvent<HTMLInputElement>) => void;
  setShowLinkModal: (val: boolean) => void;
  setShowPollModal: (val: boolean) => void;
  inputText: string;
  handleInputChange: (text: string) => void;
}

export default function MessageComposer({
  isMobile,
  isMessageSelectMode,
  isAllMessagesSelected,
  onToggleSelectAllMessages,
  selectedCount,
  onCancelSelect,
  onBulkDelete,
  handleSendMessage,
  showMentionSuggestions,
  mentionCandidates,
  selectMention,
  replyingTo,
  setReplyingTo,
  showAttachmentMenu,
  setShowAttachmentMenu,
  fileInputRef,
  handleFileUpload,
  setShowLinkModal,
  setShowPollModal,
  inputText,
  handleInputChange
}: MessageComposerProps) {
  if (isMessageSelectMode) {
    return (
      <div style={{ padding: '10px 16px', background: 'rgba(239, 68, 68, 0.08)', borderTop: '1px solid rgba(239, 68, 68, 0.2)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '12px', zIndex: 5, flexWrap: 'wrap' }}>
        <span style={{ fontSize: '13px', fontWeight: 'bold', color: 'var(--danger)' }}>
          🗑️ {selectedCount} messages selected
        </span>
        <div style={{ display: 'flex', gap: '6px' }}>
          {onToggleSelectAllMessages && (
            <button
              type="button"
              onClick={onToggleSelectAllMessages}
              style={{ background: 'var(--surface-2)', border: '1px solid var(--border)', color: 'var(--text)', borderRadius: '6px', padding: '6px 12px', fontSize: '11.5px', fontWeight: 'bold', cursor: 'pointer' }}
            >
              {isAllMessagesSelected ? 'Deselect All' : 'Select All'}
            </button>
          )}
          <button
            type="button"
            onClick={onCancelSelect}
            style={{ background: 'transparent', border: '1px solid var(--border)', color: 'var(--text-muted)', borderRadius: '6px', padding: '6px 12px', fontSize: '11.5px', fontWeight: 'bold', cursor: 'pointer' }}
          >
            Cancel
          </button>
          <button
            type="button"
            onClick={onBulkDelete}
            disabled={selectedCount === 0}
            style={{ background: 'var(--danger)', border: 'none', color: 'var(--text-white)', borderRadius: '6px', padding: '6px 14px', fontSize: '11.5px', fontWeight: 'bold', cursor: 'pointer', opacity: selectedCount === 0 ? 0.5 : 1 }}
          >
            Delete Selected
          </button>
        </div>
      </div>
    );
  }

  return (
    <form onSubmit={handleSendMessage} style={{ position: 'relative', padding: isMobile ? '6px 8px' : '6px 12px', background: 'var(--surface-popover)', display: 'flex', flexDirection: 'column', gap: '4px', zIndex: 5, borderTop: '1px solid var(--border)' }}>
      
      {/* Mention / Tag Suggestions dropdown */}
      {showMentionSuggestions && mentionCandidates.length > 0 && (
        <div style={{
          position: 'absolute',
          bottom: '105%',
          left: '12px',
          width: '260px',
          background: 'var(--surface-popover)',
          border: '1px solid var(--border)',
          borderRadius: '8px',
          boxShadow: '0 -4px 12px rgba(0,0,0,0.15)',
          maxHeight: '150px',
          overflowY: 'auto',
          zIndex: 1000,
          padding: '4px 0',
          marginBottom: '4px'
        }}>
          {mentionCandidates.map((cand: any) => (
            <div
              key={cand.id}
              onClick={() => selectMention(cand.name)}
              style={{
                padding: '6px 10px',
                cursor: 'pointer',
                fontSize: '12px',
                color: 'var(--text)',
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center'
              }}
              onMouseEnter={(e) => e.currentTarget.style.background = 'var(--surface-2)'}
              onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
            >
              <span style={{ fontWeight: 600 }}>{cand.name}</span>
              <span style={{ fontSize: '9.5px', color: 'var(--text-muted)' }}>{cand.id}</span>
            </div>
          ))}
        </div>
      )}
      
      {/* Replying Draft Preview */}
      {replyingTo && (
        <div style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          background: 'var(--surface-3)',
          borderLeft: '3px solid var(--accent)',
          padding: '4px 10px',
          borderRadius: '6px',
          marginBottom: '2px'
        }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1px', fontSize: '11px', overflow: 'hidden' }}>
            <span style={{ color: 'var(--accent)', fontWeight: 600 }}>Replying to {replyingTo.senderName}</span>
            <span style={{ color: 'var(--text-muted)', textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap', maxWidth: '280px' }}>
              {replyingTo.text}
            </span>
          </div>
          <button 
            type="button" 
            onClick={() => setReplyingTo(null)}
            style={{ background: 'transparent', border: 'none', color: 'var(--danger)', fontSize: '12px', cursor: 'pointer', padding: '2px 4px' }}
          >
            ✕
          </button>
        </div>
      )}

      <div style={{ display: 'flex', gap: '8px', alignItems: 'center', width: '100%' }}>
        {/* Attachment clip and smiley inside a single pill input wrapper */}
        <div style={{
          flex: 1,
          minWidth: '0',
          background: 'var(--surface)',
          border: '1px solid var(--border)',
          borderRadius: '18px',
          padding: '2px 10px',
          display: 'flex',
          alignItems: 'center',
          gap: '6px',
          minHeight: '34px',
          height: 'auto'
        }}>
          <div 
            onClick={() => setShowAttachmentMenu(prev => !prev)}
            style={{ color: 'var(--text-muted)', cursor: 'pointer', display: 'flex', alignItems: 'center', position: 'relative' }} 
            title="Attach file or insert link"
          >
            <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M16.5 6v11.5c0 2.21-1.79 4-4 4s-4-1.79-4-4V5c0-3.31 2.69-6 6-6s6 2.69 6 6v10.5c0 4.42-3.58 8-8 8s-8-3.58-8-8V6h2v9.5c0 3.31 2.69 6 6 6s6-2.69 6-6V5c0-2.21-1.79-4-4-4s-4 1.79-4 4v12.5c0 1.1.9 2 2 2s2-.9 2-2V6h2z"/></svg>
            
            {showAttachmentMenu && (
              <div style={{
                position: 'absolute',
                bottom: '36px',
                left: '0',
                background: 'var(--surface-popover)',
                border: '1px solid var(--border)',
                borderRadius: '8px',
                padding: '4px 0',
                display: 'flex',
                flexDirection: 'column',
                width: '130px',
                boxShadow: '0 4px 12px rgba(0,0,0,0.2)',
                zIndex: 100
              }}>
                <button
                  type="button"
                  onClick={(e) => {
                    e.stopPropagation();
                    setShowAttachmentMenu(false);
                    fileInputRef.current?.click();
                  }}
                  style={{
                    background: 'transparent',
                    border: 'none',
                    color: 'var(--text)',
                    padding: '5px 10px',
                    textAlign: 'left',
                    fontSize: '11.5px',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '5px',
                    width: '100%'
                  }}
                  onMouseEnter={(e) => e.currentTarget.style.background = 'var(--surface-2)'}
                  onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
                >
                  📂 Upload File
                </button>
                <button
                  type="button"
                  onClick={(e) => {
                    e.stopPropagation();
                    setShowAttachmentMenu(false);
                    setShowLinkModal(true);
                  }}
                  style={{
                    background: 'transparent',
                    border: 'none',
                    color: 'var(--text)',
                    padding: '5px 10px',
                    textAlign: 'left',
                    fontSize: '11.5px',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '5px',
                    width: '100%'
                  }}
                  onMouseEnter={(e) => e.currentTarget.style.background = 'var(--surface-2)'}
                  onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
                >
                  🔗 Insert Link
                </button>
                <button
                  type="button"
                  onClick={(e) => {
                    e.stopPropagation();
                    setShowAttachmentMenu(false);
                    setShowPollModal(true);
                  }}
                  style={{
                    background: 'transparent',
                    border: 'none',
                    color: 'var(--text)',
                    padding: '5px 10px',
                    textAlign: 'left',
                    fontSize: '11.5px',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '5px',
                    width: '100%'
                  }}
                  onMouseEnter={(e) => e.currentTarget.style.background = 'var(--surface-2)'}
                  onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
                >
                  📊 Create Poll
                </button>
              </div>
            )}
          </div>
          <input 
            type="file" 
            ref={fileInputRef as any} 
            onChange={handleFileUpload} 
            style={{ display: 'none' }} 
          />
          <textarea
            value={inputText}
            onChange={(e) => handleInputChange(e.target.value)}
            placeholder="Type a message..."
            rows={1}
            style={{
              flex: 1,
              width: '100%',
              minWidth: '0',
              border: 'none',
              background: 'transparent',
              color: 'var(--text)',
              fontSize: '13.5px',
              resize: 'none',
              height: '20px',
              minHeight: '20px',
              maxHeight: '80px',
              outline: 'none',
              lineHeight: '1.3',
              padding: '1px 0',
              margin: 0,
              overflowY: 'auto'
            }}
            onBlur={() => {
              setTimeout(() => {
                window.scrollTo(0, 0);
              }, 100);
            }}
          />
          <div style={{ color: 'var(--text-muted)', cursor: 'pointer', display: 'flex', alignItems: 'center' }} title="Emojis">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 14H11v-2h2v2zm0-4H11V7h2v5z"/></svg>
          </div>
        </div>

        <button 
          type="submit" 
          style={{ 
            height: '34px', 
            borderRadius: '50%', 
            width: '34px', 
            minWidth: '34px', 
            padding: '0', 
            display: 'flex', 
            alignItems: 'center', 
            justifyContent: 'center', 
            background: 'var(--accent)', 
            border: 'none', 
            color: 'var(--text-white)', 
            cursor: 'pointer',
            boxShadow: '0 2px 6px rgba(79, 70, 229, 0.35)',
            transition: 'transform 0.1s'
          }}
          onMouseDown={(e) => e.currentTarget.style.transform = 'scale(0.95)'}
          onMouseUp={(e) => e.currentTarget.style.transform = 'scale(1)'}
          title="Send message"
        >
          <svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor" style={{ transform: 'rotate(45deg)' }}><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
        </button>
      </div>
    </form>
  );
}

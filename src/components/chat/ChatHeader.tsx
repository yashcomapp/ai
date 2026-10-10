'use client';

import React from 'react';

export interface ChatRoom {
  roomId: string;
  type: 'group' | 'dm';
  name: string;
  participants: string[];
  unreadCounts: Record<string, number>;
  isMutedForStudents?: boolean;
  isMutedForParents?: boolean;
  lastMessage?: { text: string; senderName: string; timestamp: string };
  pinnedMessage?: { messageId: string; text: string; senderName: string; timestamp: string } | null;
}

interface ChatHeaderProps {
  isMobile: boolean;
  onBack: () => void;
  activeRoom: ChatRoom | null | undefined;
  activeDisplayName: string;
  getGroupBadgeColor: (name: string) => string;
  getGroupInitials: (name: string) => string;
  isMessageSelectMode: boolean;
  isAllMessagesSelected?: boolean;
  onToggleSelectAllMessages?: () => void;
  onCancelSelect: () => void;
  handleDeleteConversation: () => void;
  muteStudents: boolean;
  muteParents: boolean;
  handleToggleMute: (target: 'students' | 'parents', muted: boolean) => void;
  scrollToMessage: (messageId: string) => void;
  handleUnpinMessage: () => void;
}

export default function ChatHeader({
  isMobile,
  onBack,
  activeRoom,
  activeDisplayName,
  getGroupBadgeColor,
  getGroupInitials,
  isMessageSelectMode,
  isAllMessagesSelected,
  onToggleSelectAllMessages,
  onCancelSelect,
  handleDeleteConversation,
  muteStudents,
  muteParents,
  handleToggleMute,
  scrollToMessage,
  handleUnpinMessage
}: ChatHeaderProps) {
  return (
    <>
      <div style={{ 
        padding: isMobile ? '6px 8px' : '6px 12px', 
        borderBottom: '1px solid var(--border)', 
        background: 'var(--surface-popover)', 
        display: 'flex', 
        flexDirection: isMobile ? 'column' : 'row',
        alignItems: isMobile ? 'stretch' : 'center',
        justifyContent: 'space-between',
        gap: isMobile ? '4px' : '8px', 
        zIndex: 5 
      }}>
        {/* Row 1: Back + Info */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', minWidth: 0, width: '100%', justifyContent: 'space-between' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', minWidth: 0 }}>
            {isMobile && (
              <button 
                onClick={onBack} 
                style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '13px', padding: '4px 2px', color: 'var(--accent)', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '2px' }}
              >
                <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg>
              </button>
            )}
            <div style={{ position: 'relative', flexShrink: 0 }}>
              <div style={{
                width: isMobile ? '30px' : '34px',
                height: isMobile ? '30px' : '34px',
                borderRadius: activeRoom?.type === 'group' ? '8px' : '50%',
                background: activeRoom?.type === 'group' ? getGroupBadgeColor(activeDisplayName) : 'var(--accent)',
                color: 'var(--text-on-accent)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontWeight: 'bold',
                fontSize: isMobile ? '11px' : '13px'
              }}>
                {activeRoom?.type === 'group' ? getGroupInitials(activeDisplayName) : (activeDisplayName ? activeDisplayName[0].toUpperCase() : 'S')}
              </div>
              <span style={{ position: 'absolute', bottom: '0px', right: '0px', width: '7px', height: '7px', borderRadius: '50%', background: 'var(--success)', border: '1.5px solid var(--surface-popover)' }} />
            </div>
            <div style={{ minWidth: 0, marginLeft: '2px', display: 'flex', alignItems: 'center', gap: '6px' }}>
              <h3 style={{ margin: 0, fontSize: isMobile ? '13px' : '14px', fontWeight: 600, color: 'var(--text)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                {activeDisplayName}
              </h3>
              {isMessageSelectMode && (
                <div style={{ display: 'flex', gap: '4px', alignItems: 'center' }}>
                  {onToggleSelectAllMessages && (
                    <button
                      onClick={onToggleSelectAllMessages}
                      style={{
                        background: 'var(--surface-2)',
                        border: '1px solid var(--border)',
                        borderRadius: '4px',
                        color: 'var(--text)',
                        padding: '2px 6px',
                        fontSize: '9.5px',
                        fontWeight: 'bold',
                        cursor: 'pointer'
                      }}
                    >
                      {isAllMessagesSelected ? 'Deselect All' : 'Select All'}
                    </button>
                  )}
                  <button
                    onClick={onCancelSelect}
                    style={{
                      background: 'rgba(239, 68, 68, 0.15)',
                      border: '1px solid rgba(239, 68, 68, 0.3)',
                      borderRadius: '4px',
                      color: 'var(--danger)',
                      padding: '2px 5px',
                      fontSize: '9.5px',
                      fontWeight: 'bold',
                      cursor: 'pointer'
                    }}
                  >
                    Cancel Select
                  </button>
                </div>
              )}
            </div>
          </div>

          {isMobile && (
            <button
              onClick={handleDeleteConversation}
              style={{
                background: 'rgba(239, 68, 68, 0.15)',
                border: '1px solid rgba(239, 68, 68, 0.4)',
                borderRadius: '6px',
                color: 'var(--danger)',
                padding: '4px 8px',
                fontSize: '12px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center'
              }}
              title="Delete Conversation"
            >
              🗑️
            </button>
          )}
        </div>

        {/* Row 2: Mute switches and buttons */}
        <div style={{ 
          display: 'flex', 
          gap: '6px', 
          alignItems: 'center', 
          justifyContent: 'space-between',
          flexWrap: 'wrap',
          width: isMobile ? '100%' : 'auto',
          borderTop: isMobile ? '1px solid var(--border-light)' : 'none',
          paddingTop: isMobile ? '4px' : '0',
          marginTop: isMobile ? '2px' : '0'
        }}>
          {activeRoom?.type === 'group' && (
            <div style={{ display: 'flex', gap: '6px', alignItems: 'center', fontSize: '10.5px', fontWeight: 600, color: 'var(--text-muted)' }}>
              <span>Mute:</span>
              <label style={{ display: 'flex', alignItems: 'center', gap: '3px', cursor: 'pointer', userSelect: 'none' }}>
                <input
                  type="checkbox"
                  checked={muteStudents}
                  onChange={(e) => handleToggleMute('students', e.target.checked)}
                  style={{ width: '12px', height: '12px', cursor: 'pointer' }}
                />
                Student
              </label>
              <label style={{ display: 'flex', alignItems: 'center', gap: '3px', cursor: 'pointer', userSelect: 'none' }}>
                <input
                  type="checkbox"
                  checked={muteParents}
                  onChange={(e) => handleToggleMute('parents', e.target.checked)}
                  style={{ width: '12px', height: '12px', cursor: 'pointer' }}
                />
                Parent
              </label>
            </div>
          )}

          <div style={{ display: 'flex', gap: '6px', marginLeft: 'auto' }}>
            {!isMobile && (
              <button
                onClick={handleDeleteConversation}
                style={{
                  background: 'rgba(239, 68, 68, 0.15)',
                  border: '1px solid rgba(239, 68, 68, 0.4)',
                  borderRadius: '6px',
                  color: 'var(--danger)',
                  padding: '4px 8px',
                  fontSize: '10.5px',
                  fontWeight: 'bold',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '3px',
                  transition: 'all 0.2s'
                }}
              >
                🗑️ Delete Chat
              </button>
            )}
          </div>
        </div>
      </div>

      {/* Pinned Message Banner */}
      {activeRoom?.pinnedMessage && (
        <div style={{
          background: 'var(--surface-3)',
          borderBottom: '1px solid var(--border)',
          padding: '5px 12px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          gap: '8px',
          zIndex: 4
        }}>
          <div 
            onClick={() => scrollToMessage(activeRoom.pinnedMessage!.messageId)}
            style={{ display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer', overflow: 'hidden', flex: 1 }}
          >
            <span style={{ fontSize: '12px' }}>📌</span>
            <div style={{ fontSize: '11px', minWidth: 0 }}>
              <span style={{ color: 'var(--accent)', fontWeight: 600 }}>Pinned Message: </span>
              <span style={{ color: 'var(--text-secondary)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', display: 'inline-block', maxWidth: '300px', verticalAlign: 'bottom' }}>
                {activeRoom.pinnedMessage.text}
              </span>
            </div>
          </div>
          <button
            onClick={handleUnpinMessage}
            style={{ background: 'transparent', border: 'none', color: 'var(--danger)', fontSize: '11px', cursor: 'pointer', padding: '1px 4px' }}
            title="Unpin Message"
          >
            ✕
          </button>
        </div>
      )}
    </>
  );
}

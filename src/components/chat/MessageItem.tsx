'use client';

import React from 'react';
import { renderMarkdown } from '@/lib/markdown';

export interface Message {
  messageId: string;
  senderId: string;
  senderName: string;
  senderRole: string;
  text: string;
  type: string;
  createdAt: string;
  isDeleted?: boolean;
  isEdited?: boolean;
  readBy?: Record<string, string>;
  isOptimistic?: boolean;
  replyToId?: string;
  replyToText?: string;
  replyToSenderName?: string;
  pollOptions?: { text: string; votesCount: number }[] | null;
  pollVotes?: Record<string, number> | null;
  reactions?: {
    thumbsup?: string[];
    pray?: string[];
  };
}

interface MessageItemProps {
  msg: Message;
  adminUid: string;
  isMobile: boolean;
  isSameSender: boolean;
  isMessageSelectMode: boolean;
  isSelected: boolean;
  isStarred: boolean;
  isPinned: boolean;
  participantNames: Record<string, string>;
  editingMessageId: string;
  editingText: string;
  setEditingText: (val: string) => void;
  setEditingMessageId: (val: string) => void;
  handleEditMessage: (messageId: string, text: string) => void;
  handleDeleteMessage: (messageId: string) => void;
  handleToggleReaction: (messageId: string, reaction: 'thumbsup' | 'pray') => void;
  toggleStarMessage: (messageId: string) => void;
  handlePinMessage: (messageId: string) => void;
  handleUnpinMessage: () => void;
  setReplyingTo: (msg: Message) => void;
  handleVotePoll: (messageId: string, optionIdx: number) => void;
  setShowReactorsModal: (val: { isOpen: boolean; thumbsup: string[]; pray: string[] }) => void;
  scrollToMessage: (messageId: string) => void;
  onLongPressStart: (messageId: string) => void;
  onLongPressEnd: () => void;
  onSelectMessage: (messageId: string) => void;
  onReadReceiptsClick: (msg: Message) => void;
  messageRef?: (el: HTMLDivElement | null) => void;
}

function MessageItemComponent({
  msg,
  adminUid,
  isMobile,
  isSameSender,
  isMessageSelectMode,
  isSelected,
  isStarred,
  isPinned,
  participantNames,
  editingMessageId,
  editingText,
  setEditingText,
  setEditingMessageId,
  handleEditMessage,
  handleDeleteMessage,
  handleToggleReaction,
  toggleStarMessage,
  handlePinMessage,
  handleUnpinMessage,
  setReplyingTo,
  handleVotePoll,
  setShowReactorsModal,
  scrollToMessage,
  onLongPressStart,
  onLongPressEnd,
  onSelectMessage,
  onReadReceiptsClick,
  messageRef
}: MessageItemProps) {
  const isMe = msg.senderId === adminUid;
  const readersCount = Object.keys(msg.readBy || {}).filter(k => k !== msg.senderId).length;
  const hasAttachment = msg.text.toLowerCase().includes('.pdf') || msg.text.toLowerCase().includes('.doc') || msg.text.toLowerCase().includes('.xlsx');

  return (
    <div
      ref={messageRef}
      onTouchStart={() => onLongPressStart(msg.messageId)}
      onTouchEnd={onLongPressEnd}
      onTouchMove={onLongPressEnd}
      onMouseDown={() => onLongPressStart(msg.messageId)}
      onMouseUp={onLongPressEnd}
      onMouseLeave={onLongPressEnd}
      onClick={() => {
        if (isMessageSelectMode) {
          onSelectMessage(msg.messageId);
        }
      }}
      style={{
        alignSelf: isMe ? 'flex-end' : 'flex-start',
        maxWidth: isMobile ? '88%' : '75%',
        display: 'flex',
        gap: '8px',
        marginTop: isSameSender ? '2px' : '8px',
        opacity: msg.isOptimistic ? 0.7 : 1,
        cursor: isMessageSelectMode ? 'pointer' : 'default',
        background: isMessageSelectMode && isSelected ? 'rgba(239, 68, 68, 0.05)' : 'transparent',
        borderRadius: '8px',
        padding: isMessageSelectMode ? '4px 8px' : '0'
      }}
    >
      {isMessageSelectMode && (
        <input 
          type="checkbox" 
          checked={isSelected}
          onChange={() => {}} // parent onClick handles toggle
          style={{ alignSelf: 'center', width: '16px', height: '16px', cursor: 'pointer', accentColor: 'var(--danger)', marginRight: '4px' }}
        />
      )}

      {/* Avatar for incoming messages */}
      {!isMe && !isSameSender && (
        <div style={{
          width: '28px',
          height: '28px',
          borderRadius: '50%',
          background: 'var(--accent)',
          color: 'var(--text-on-accent)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontWeight: 'bold',
          fontSize: '10px',
          flexShrink: 0,
          marginTop: '4px'
        }}>
          {msg.senderName ? msg.senderName[0].toUpperCase() : 'U'}
        </div>
      )}
      
      {/* Spacer to align bubbles when avatar is missing */}
      {!isMe && isSameSender && <div style={{ width: '28px', flexShrink: 0 }} />}

      <div style={{ display: 'flex', flexDirection: 'column', alignItems: isMe ? 'flex-end' : 'flex-start', minWidth: 0, width: '100%' }}>
        
        {/* Name header */}
        {!isMe && !isSameSender && (
          <span style={{ fontSize: '11px', color: 'var(--accent)', marginBottom: '3px', fontWeight: 600, paddingLeft: '4px' }}>
            {msg.senderName} ({msg.senderRole.toUpperCase()})
          </span>
        )}

        {/* Bubble */}
        <div
          onDoubleClick={() => {
            if (!msg.isDeleted && !msg.isOptimistic) {
              setReplyingTo(msg);
            }
          }}
          style={{
            background: isMe ? 'var(--accent)' : 'var(--surface)',
            color: isMe ? 'var(--text-on-accent)' : 'var(--text)',
            padding: '7px 11px',
            minWidth: 0,
            width: '100%',
            borderRadius: isMe 
              ? (isSameSender ? '12px 12px 12px 12px' : '12px 12px 3px 12px')
              : (isSameSender ? '12px 12px 12px 12px' : '12px 12px 12px 3px'),
            border: isMe ? 'none' : '1px solid var(--border-light)',
            fontSize: '13.5px',
            lineHeight: '1.4',
            position: 'relative',
            wordBreak: 'break-word',
            boxShadow: isMe ? '0 1px 4px rgba(37,99,235,0.2)' : '0 1px 4px rgba(0,0,0,0.05)'
          }}
        >
          {/* Quote message reference */}
          {msg.replyToId && (
            <div 
              onClick={() => scrollToMessage(msg.replyToId!)}
              style={{
                background: isMe ? 'rgba(0,0,0,0.15)' : 'var(--surface-2)',
                borderLeft: isMe ? '3px solid var(--info)' : '3px solid var(--accent)',
                padding: '4px 8px',
                borderRadius: '4px',
                marginBottom: '4px',
                fontSize: '11px',
                cursor: 'pointer',
                display: 'flex',
                flexDirection: 'column',
                gap: '2px'
              }}
            >
              <div style={{ fontWeight: 600, color: isMe ? 'var(--info)' : 'var(--accent)' }}>{msg.replyToSenderName}</div>
              <div style={{ color: isMe ? 'rgba(255,255,255,0.85)' : 'var(--text-muted)', textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap' }}>
                {msg.replyToText}
              </div>
            </div>
          )}

          {msg.isDeleted ? (
            <span style={{ fontStyle: 'italic', color: isMe ? 'rgba(255,255,255,0.7)' : 'var(--text-faint)' }}>🚫 This message was deleted</span>
          ) : editingMessageId === msg.messageId ? (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', minWidth: '220px' }}>
              <textarea
                value={editingText}
                onChange={(e) => setEditingText(e.target.value)}
                style={{
                  width: '100%',
                  background: 'var(--surface-2)',
                  border: '1px solid var(--accent)',
                  borderRadius: '6px',
                  color: 'var(--text)',
                  padding: '6px',
                  fontSize: '13px',
                  resize: 'none',
                  outline: 'none'
                }}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    handleEditMessage(msg.messageId, editingText);
                  }
                }}
              />
              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '6px' }}>
                <button
                  onClick={() => setEditingMessageId('')}
                  style={{ background: 'transparent', border: '1px solid var(--border)', color: 'var(--text-muted)', borderRadius: '4px', padding: '3px 8px', fontSize: '10px', cursor: 'pointer' }}
                >
                  Cancel
                </button>
                <button
                  onClick={() => handleEditMessage(msg.messageId, editingText)}
                  style={{ background: 'var(--accent)', border: 'none', color: 'var(--text-on-accent)', borderRadius: '4px', padding: '3px 8px', fontSize: '10px', cursor: 'pointer', fontWeight: 'bold' }}
                >
                  Save
                </button>
              </div>
            </div>
          ) : msg.type === 'poll' ? (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', minWidth: '240px' }}>
              <div style={{ fontWeight: 600, fontSize: '14px', display: 'flex', alignItems: 'center', gap: '6px', color: isMe ? 'var(--text-on-accent)' : 'var(--accent)' }}>
                📊 {msg.text}
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', marginTop: '6px' }}>
                {(msg.pollOptions || []).map((opt, oIdx) => {
                  const votesMap = msg.pollVotes || {};
                  const totalVotes = Object.keys(votesMap).length;
                  const hasVotedThis = votesMap[adminUid] === oIdx;
                  const percentage = totalVotes > 0 ? Math.round((opt.votesCount / totalVotes) * 100) : 0;
                  return (
                    <div
                      key={oIdx}
                      onClick={() => handleVotePoll(msg.messageId, oIdx)}
                      style={{
                        position: 'relative',
                        background: hasVotedThis ? (isMe ? 'rgba(255,255,255,0.2)' : 'var(--accent-soft)') : (isMe ? 'rgba(0,0,0,0.12)' : 'var(--surface-2)'),
                        border: hasVotedThis ? (isMe ? '1px solid var(--info)' : '1px solid var(--accent)') : (isMe ? '1px solid rgba(255,255,255,0.2)' : '1px solid var(--border-light)'),
                        borderRadius: '8px',
                        padding: '8px 12px',
                        cursor: 'pointer',
                        overflow: 'hidden',
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'flex-start',
                        fontSize: '13px',
                        transition: 'all 0.2s',
                        userSelect: 'none',
                        width: '100%'
                      }}
                    >
                      <div
                        style={{
                          position: 'absolute',
                          left: 0,
                          top: 0,
                          bottom: 0,
                          width: `${percentage}%`,
                          background: hasVotedThis ? (isMe ? 'rgba(255,255,255,0.15)' : 'rgba(37, 99, 235, 0.15)') : (isMe ? 'rgba(0,0,0,0.08)' : 'rgba(148, 163, 184, 0.08)'),
                          zIndex: 0,
                          transition: 'width 0.3s'
                        }}
                      />
                      {(() => {
                        const voterKeys = Object.entries(msg.pollVotes || {})
                          .filter(([_, oIdxVal]) => oIdxVal === oIdx)
                          .map(([vKey]) => participantNames[vKey] || vKey);
                        return (
                          <>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '100%', zIndex: 1 }}>
                              <span style={{ fontWeight: 555 }}>{opt.text}</span>
                              <span style={{ fontSize: '11px', color: isMe ? 'rgba(255,255,255,0.85)' : 'var(--text-muted)' }}>
                                {opt.votesCount} votes ({percentage}%)
                              </span>
                            </div>
                            {voterKeys.length > 0 && (
                              <div style={{ fontSize: '10px', color: isMe ? 'rgba(255,255,255,0.75)' : 'var(--text-muted)', marginTop: '4px', zIndex: 1, textAlign: 'left', width: '100%', opacity: 0.85, whiteSpace: 'normal', wordBreak: 'break-word' }}>
                                Voters: {voterKeys.join(', ')}
                              </div>
                            )}
                          </>
                        );
                      })()}
                    </div>
                  );
                })}
              </div>
            </div>
          ) : (
            <>
              <div className="selectable-text" style={{ wordBreak: 'break-word', whiteSpace: 'pre-wrap', fontSize: '13.5px' }} dangerouslySetInnerHTML={{ __html: renderMarkdown(msg.text, participantNames) }} />
              
              {/* Attachment box */}
              {hasAttachment && (
                <div style={{
                  marginTop: '6px',
                  background: isMe ? 'rgba(0,0,0,0.15)' : 'var(--surface-2)',
                  borderRadius: '6px',
                  padding: '6px 10px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  gap: '10px',
                  border: isMe ? '1px solid rgba(255,255,255,0.2)' : '1px solid var(--border)',
                  minWidth: '220px'
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <div style={{ background: 'var(--danger)', width: '28px', height: '30px', borderRadius: '4px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', fontWeight: 'bold', fontSize: '8.5px', color: 'var(--text-white)' }}>
                      <span>FILE</span>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                      <span style={{ fontSize: '11.5px', fontWeight: 600, color: isMe ? 'var(--text-on-accent)' : 'var(--text)', maxWidth: '140px', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{msg.text.split(' ').pop()}</span>
                      <span style={{ fontSize: '9.5px', color: isMe ? 'rgba(255,255,255,0.75)' : 'var(--text-muted)', marginTop: '1px' }}>Attachment Link</span>
                    </div>
                  </div>
                  <a href={msg.text.includes('(') ? msg.text.substring(msg.text.indexOf('(') + 1, msg.text.indexOf(')')) : msg.text} target="_blank" rel="noopener noreferrer" style={{ color: isMe ? 'var(--info)' : 'var(--accent)', cursor: 'pointer', display: 'flex', alignItems: 'center' }} title="Download file">
                    <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/></svg>
                  </a>
                </div>
              )}
            </>
          )}

          {/* Quick reactions summary inside the bubble */}
          {!msg.isDeleted && msg.reactions && (
            <div style={{ display: 'flex', gap: '4px', flexWrap: 'wrap', marginTop: '4px' }}>
              {msg.reactions.thumbsup && msg.reactions.thumbsup.length > 0 && (
                <span 
                  onClick={(e) => {
                    e.stopPropagation();
                    setShowReactorsModal({
                      isOpen: true,
                      thumbsup: msg.reactions?.thumbsup || [],
                      pray: msg.reactions?.pray || []
                    });
                  }}
                  style={{
                    fontSize: '10.5px',
                    background: msg.reactions.thumbsup.includes(adminUid) ? 'var(--accent-soft)' : (isMe ? 'rgba(0,0,0,0.12)' : 'var(--surface-2)'),
                    border: msg.reactions.thumbsup.includes(adminUid) ? '1px solid var(--accent)' : (isMe ? '1px solid rgba(255,255,255,0.2)' : '1px solid var(--border-light)'),
                    padding: '1px 5px',
                    borderRadius: '8px',
                    cursor: 'pointer',
                    display: 'inline-flex',
                    alignItems: 'center',
                    gap: '2px',
                    userSelect: 'none'
                  }}
                  title={`Reacted by: ${msg.reactions.thumbsup.map(uid => participantNames[uid] || uid).join(', ')}`}
                >
                  👍 <span style={{ color: isMe ? 'rgba(255,255,255,0.85)' : 'var(--text-muted)', fontSize: '9.5px' }}>{msg.reactions.thumbsup.length}</span>
                </span>
              )}
              {msg.reactions.pray && msg.reactions.pray.length > 0 && (
                <span 
                  onClick={(e) => {
                    e.stopPropagation();
                    setShowReactorsModal({
                      isOpen: true,
                      thumbsup: msg.reactions?.thumbsup || [],
                      pray: msg.reactions?.pray || []
                    });
                  }}
                  style={{
                    fontSize: '10.5px',
                    background: msg.reactions.pray.includes(adminUid) ? 'var(--accent-soft)' : (isMe ? 'rgba(0,0,0,0.12)' : 'var(--surface-2)'),
                    border: msg.reactions.pray.includes(adminUid) ? '1px solid var(--accent)' : (isMe ? '1px solid rgba(255,255,255,0.2)' : '1px solid var(--border-light)'),
                    padding: '1px 5px',
                    borderRadius: '8px',
                    cursor: 'pointer',
                    display: 'inline-flex',
                    alignItems: 'center',
                    gap: '2px',
                    userSelect: 'none'
                  }}
                  title={`Reacted by: ${msg.reactions.pray.map(uid => participantNames[uid] || uid).join(', ')}`}
                >
                  🙏 <span style={{ color: isMe ? 'rgba(255,255,255,0.85)' : 'var(--text-muted)', fontSize: '9.5px' }}>{msg.reactions.pray.length}</span>
                </span>
              )}
            </div>
          )}
          
          {/* Bubble Footer Meta (time + ticks) */}
          <div style={{ 
            display: 'flex', 
            justifyContent: 'flex-end', 
            alignItems: 'center', 
            gap: '4px', 
            fontSize: '10.5px', 
            color: isMe ? 'rgba(255,255,255,0.75)' : 'var(--text-faint)', 
            marginTop: '4px',
            textAlign: 'right',
            flexWrap: 'wrap'
          }}>
            {isStarred && (
              <span style={{ color: 'var(--warning)', marginRight: '3px', fontSize: '11px' }} title="Starred Message">★</span>
            )}
            {msg.isEdited && <span style={{ fontStyle: 'italic', fontSize: '9.5px', color: isMe ? 'rgba(255,255,255,0.75)' : 'var(--text-faint)', marginRight: '3px' }}>edited</span>}
            <span>{new Date(msg.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>

            {/* Quick reactions */}
            {!msg.isDeleted && !msg.isOptimistic && (
              <>
                <span 
                  onClick={(e) => {
                    e.stopPropagation();
                    handleToggleReaction(msg.messageId, 'thumbsup');
                  }}
                  style={{ 
                    cursor: 'pointer', 
                    marginLeft: '10px', 
                    opacity: msg.reactions?.thumbsup?.includes(adminUid) ? 1 : 0.4,
                    fontSize: '15px',
                    display: 'inline-flex', 
                    alignItems: 'center',
                    userSelect: 'none'
                  }}
                  title="React Thumbs Up"
                >
                  👍
                </span>
                <span 
                  onClick={(e) => {
                    e.stopPropagation();
                    handleToggleReaction(msg.messageId, 'pray');
                  }}
                  style={{ 
                    cursor: 'pointer', 
                    marginLeft: '8px', 
                    opacity: msg.reactions?.pray?.includes(adminUid) ? 1 : 0.4,
                    fontSize: '15px',
                    display: 'inline-flex', 
                    alignItems: 'center',
                    userSelect: 'none'
                  }}
                  title="React Folding Hand"
                >
                  🙏
                </span>
              </>
            )}
            
            {/* Star Action */}
            {!msg.isDeleted && !msg.isOptimistic && (
              <span 
                onClick={(e) => {
                  e.stopPropagation();
                  toggleStarMessage(msg.messageId);
                }}
                style={{ color: isStarred ? 'var(--warning)' : (isMe ? 'rgba(255,255,255,0.7)' : 'var(--text-faint)'), cursor: 'pointer', marginLeft: '10px', display: 'inline-flex', alignItems: 'center', padding: '2px' }}
                title={isStarred ? "Unstar Message" : "Star Message"}
              >
                <svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </span>
            )}

            {/* Reply Action */}
            {!msg.isDeleted && !msg.isOptimistic && (
              <span 
                onClick={(e) => {
                  e.stopPropagation();
                  setReplyingTo(msg);
                }}
                style={{ color: isMe ? 'rgba(255,255,255,0.7)' : 'var(--text-faint)', cursor: 'pointer', marginLeft: '8px', display: 'inline-flex', alignItems: 'center', padding: '2px' }}
                title="Reply to message"
              >
                <svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M10 9V5l-7 7 7 7v-4.1c5 0 8.5 1.6 11 5.1-1-5-4-10-11-11z"/></svg>
              </span>
            )}

            {/* Pin Action (Admin only) */}
            {!msg.isDeleted && !msg.isOptimistic && (
              <span 
                onClick={(e) => {
                  e.stopPropagation();
                  if (isPinned) handleUnpinMessage();
                  else handlePinMessage(msg.messageId);
                }}
                style={{ color: isPinned ? (isMe ? 'var(--info)' : 'var(--accent)') : (isMe ? 'rgba(255,255,255,0.7)' : 'var(--text-faint)'), cursor: 'pointer', marginLeft: '8px', display: 'inline-flex', alignItems: 'center', fontSize: '15px' }}
                title={isPinned ? "Unpin Message" : "Pin Message"}
              >
                📌
              </span>
            )}

            {/* Edit Action for Admin (no time limit, text type only) */}
            {!msg.isDeleted && !msg.isOptimistic && msg.type !== 'poll' && (
              <span 
                onClick={(e) => {
                  e.stopPropagation();
                  setEditingMessageId(msg.messageId);
                  setEditingText(msg.text);
                }}
                style={{ color: isMe ? 'var(--info)' : 'var(--accent)', cursor: 'pointer', marginLeft: '8px', display: 'inline-flex', alignItems: 'center', padding: '2px' }}
                title="Edit message"
              >
                <svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>
              </span>
            )}

            {/* Delete Action for Admin (no limit) */}
            {!msg.isDeleted && !msg.isOptimistic && (
              <span 
                onClick={(e) => {
                  e.stopPropagation();
                  handleDeleteMessage(msg.messageId);
                }}
                style={{ color: 'var(--danger)', cursor: 'pointer', marginLeft: '8px', display: 'inline-flex', alignItems: 'center', padding: '2px' }}
                title="Delete message"
              >
                <svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/></svg>
              </span>
            )}

            {isMe && !msg.isDeleted && (
              <span 
                onClick={() => onReadReceiptsClick(msg)}
                style={{ display: 'inline-flex', cursor: 'pointer', marginLeft: '4px' }}
                title="View Read Receipts"
              >
                {readersCount > 0 ? (
                  <svg viewBox="0 0 16 15" width="16" height="15" fill="var(--info)"><path d="M15.01 3.3l-5.5 5.5-2.76-2.77-.88.88 3.64 3.64 6.38-6.37-.88-.88zm-5.56 5.5l-.89-.89-.88.88 1.77 1.77 1-.99-.88-.88-.12.12zm-3.8-1.92l-.88-.88-2.77 2.76-1.39-1.39-.88.88 2.27 2.27 3.65-3.64z"/></svg>
                ) : (
                  <svg viewBox="0 0 16 15" width="16" height="15" fill="rgba(255,255,255,0.6)"><path d="M15.01 3.3l-5.5 5.5-2.76-2.77-.88.88 3.64 3.64 6.38-6.37-.88-.88zm-5.56 5.5l-.89-.89-.88.88 1.77 1.77 1-.99-.88-.88-.12.12zm-3.8-1.92l-.88-.88-2.77 2.76-1.39-1.39-.88.88 2.27 2.27 3.65-3.64z"/></svg>
                )}
              </span>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export const MessageItem = React.memo(MessageItemComponent, (prev, next) => {
  return (
    prev.msg.messageId === next.msg.messageId &&
    prev.msg.text === next.msg.text &&
    prev.msg.isDeleted === next.msg.isDeleted &&
    prev.msg.isEdited === next.msg.isEdited &&
    prev.msg.isOptimistic === next.msg.isOptimistic &&
    prev.isSameSender === next.isSameSender &&
    prev.isSelected === next.isSelected &&
    prev.isStarred === next.isStarred &&
    prev.isPinned === next.isPinned &&
    prev.isMessageSelectMode === next.isMessageSelectMode &&
    prev.editingMessageId === next.editingMessageId &&
    prev.editingText === next.editingText &&
    prev.isMobile === next.isMobile &&
    prev.adminUid === next.adminUid &&
    JSON.stringify(prev.msg.reactions) === JSON.stringify(next.msg.reactions) &&
    JSON.stringify(prev.msg.pollVotes) === JSON.stringify(next.msg.pollVotes) &&
    JSON.stringify(prev.msg.readBy) === JSON.stringify(next.msg.readBy)
  );
});

export default MessageItem;

'use client';

import React from 'react';
import { useRouter, usePathname } from 'next/navigation';
import { MessageSquare } from 'lucide-react';
import { useUnreadChatCount } from '@/hooks/useUnreadChatCount';

interface TopBarChatButtonProps {
  role?: 'admin' | 'student' | 'parent';
  chatUrl?: string;
  style?: React.CSSProperties;
  count?: number;
}

export default function TopBarChatButton({
  role = 'admin',
  chatUrl = '/admin/chat',
  style = {},
  count
}: TopBarChatButtonProps) {
  const router = useRouter();
  const pathname = usePathname();
  const hookCount = useUnreadChatCount(count !== undefined ? null : role, pathname);
  const unreadCount = count !== undefined ? count : hookCount;
  const isActive = pathname === chatUrl || pathname.startsWith(chatUrl);

  return (
    <button
      className="page-header-btn topbar-chat-btn"
      onClick={() => router.push(chatUrl)}
      title={
        unreadCount > 0
          ? `${unreadCount} unread message${unreadCount > 1 ? 's' : ''} in chat - Click to open Chat`
          : 'Live Chat Workspace'
      }
      aria-label="Live Chat Workspace"
      style={{
        background: isActive
          ? 'var(--info-bg, rgba(59, 130, 246, 0.15))'
          : unreadCount > 0
            ? 'rgba(239, 68, 68, 0.14)'
            : 'rgba(255, 255, 255, 0.05)',
        border: isActive
          ? '1px solid var(--info, #3b82f6)'
          : unreadCount > 0
            ? '1px solid rgba(239, 68, 68, 0.5)'
            : '1px solid var(--border)',
        borderRadius: unreadCount > 0 ? '20px' : '50%',
        width: unreadCount > 0 ? 'auto' : '36px',
        minWidth: '36px',
        height: '36px',
        padding: unreadCount > 0 ? '0 10px' : '0',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: unreadCount > 0 ? '6px' : '0',
        cursor: 'pointer',
        color: 'var(--text)',
        flexShrink: 0,
        position: 'relative',
        transition: 'all 0.25s cubic-bezier(0.16, 1, 0.3, 1)',
        boxShadow: unreadCount > 0 ? '0 0 14px rgba(239, 68, 68, 0.3)' : 'none',
        ...style
      }}
    >
      <MessageSquare
        size={16}
        color={unreadCount > 0 ? '#ef4444' : isActive ? 'var(--info, #3b82f6)' : 'var(--info, #3b82f6)'}
      />
      {unreadCount > 0 && (
        <span
          className="chat-unread-badge"
          style={{
            background: '#ef4444',
            color: '#ffffff',
            fontSize: '11px',
            fontWeight: 800,
            padding: '2px 7px',
            borderRadius: '10px',
            lineHeight: 1,
            minWidth: '18px',
            textAlign: 'center',
            letterSpacing: '0.2px',
            boxShadow: '0 2px 4px rgba(0,0,0,0.3)',
            animation: 'chatBadgePulse 2s infinite ease-in-out'
          }}
        >
          {unreadCount > 99 ? '99+' : unreadCount}
        </span>
      )}
    </button>
  );
}

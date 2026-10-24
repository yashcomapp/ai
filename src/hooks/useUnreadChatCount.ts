'use client';

import { useChat } from '@/context/ChatContext';

/**
 * Real-time hook for tracking total unread chat messages across all group and direct message rooms.
 * Sourced directly from the single shared ChatContext subscription.
 */
export function useUnreadChatCount(role: 'admin' | 'student' | 'parent' | null = 'admin', currentPath?: string): number {
  const chatContext = useChat();
  return chatContext?.unreadCount ?? 0;
}

'use client';

import { useState, useEffect, useRef } from 'react';
import { useAuth } from '@/context/AuthContext';
import { db } from '@/lib/firebase/firestore';
import { collection, onSnapshot, query, where, orderBy, limit } from 'firebase/firestore';
import { playNotificationSound } from '@/lib/audioUtils';
import { useChat } from '@/context/ChatContext';

/**
 * Real-time hook for tracking total unread chat messages across all group and direct message rooms.
 * Dynamically computes unread count per role (admin, student, parent) and triggers audio intimation
 * when new messages arrive while user is on other screens.
 */
export function useUnreadChatCount(role: 'admin' | 'student' | 'parent' | null = 'admin', currentPath?: string) {
  const chatContext = useChat();
  const { firebaseUser, user } = useAuth();
  const [unreadCount, setUnreadCount] = useState<number>(0);
  const previousUnreadRef = useRef<number>(0);
  const isInitialMountRef = useRef<boolean>(true);

  useEffect(() => {
    // Skip fallback subscription if shared ChatContext is active, or if user is on /chat screen, or unauthenticated/null role
    if (chatContext || !firebaseUser || !role || currentPath?.includes('/chat')) {
      if (!firebaseUser || !role) {
        setUnreadCount(0);
      }
      return;
    }

    let unsubscribe = () => {};
    try {
      let q;
      if (role === 'admin') {
        q = query(collection(db, 'chatRooms'), orderBy('lastMessage.timestamp', 'desc'), limit(100));
      } else if (role === 'student') {
        const sCode = user?.studentCode;
        if (!sCode) return;
        q = query(collection(db, 'chatRooms'), where('participants', 'array-contains', sCode));
      } else if (role === 'parent') {
        const pKey = user?.email ? `PR-${user.email.toLowerCase().trim()}` : '';
        if (!pKey) return;
        q = query(collection(db, 'chatRooms'), where('participants', 'array-contains', pKey));
      } else {
        return;
      }

      unsubscribe = onSnapshot(q, (snapshot) => {
        let total = 0;
        snapshot.docs.forEach((doc) => {
          const data = doc.data();
          const uCounts = data.unreadCounts || {};

          if (role === 'admin') {
            const adminCount = Number(uCounts['admin'] || 0);
            const uidCount = firebaseUser?.uid ? Number(uCounts[firebaseUser.uid] || 0) : 0;
            total += Math.max(adminCount, uidCount);
          } else if (role === 'student') {
            const sCode = user?.studentCode || '';
            const sCount = sCode ? Math.max(
              Number(uCounts[sCode] || 0),
              Number(uCounts[sCode.toUpperCase()] || 0),
              Number(uCounts[sCode.toLowerCase()] || 0)
            ) : 0;
            const uidCount = firebaseUser?.uid ? Number(uCounts[firebaseUser.uid] || 0) : 0;
            total += Math.max(sCount, uidCount);
          } else if (role === 'parent') {
            const pKey = user?.email ? `PR-${user.email.toLowerCase().trim()}` : '';
            const sCode = user?.studentCode || '';
            const pCount = pKey ? Number(uCounts[pKey] || 0) : 0;
            const sCount = sCode ? Math.max(
              Number(uCounts[`PR-${sCode}`] || 0),
              Number(uCounts[`PR-${sCode.toUpperCase()}`] || 0)
            ) : 0;
            const uidCount = firebaseUser?.uid ? Number(uCounts[firebaseUser.uid] || 0) : 0;
            total += Math.max(pCount, sCount, uidCount);
          }
        });

        // Trigger sound if unread count increased and user is not currently in chat
        if (!isInitialMountRef.current && total > previousUnreadRef.current) {
          const isCurrentlyInChat = currentPath?.includes('/chat');
          if (!isCurrentlyInChat) {
            try {
              playNotificationSound();
            } catch {
              // Ignore audio autoplay restrictions
            }
          }
        } else {
          isInitialMountRef.current = false;
        }

        previousUnreadRef.current = total;
        setUnreadCount(total);
      }, (err) => {
        console.warn('useUnreadChatCount listener warning:', err);
      });
    } catch (err) {
      console.warn('useUnreadChatCount setup error:', err);
    }

    return () => unsubscribe();
  }, [firebaseUser, user?.studentCode, user?.email, role, currentPath]);

  return chatContext ? chatContext.unreadCount : unreadCount;
}

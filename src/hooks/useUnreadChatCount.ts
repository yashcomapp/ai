'use client';

import { useState, useEffect, useRef } from 'react';
import { useAuth } from '@/context/AuthContext';
import { db } from '@/lib/firebase/firestore';
import { collection, onSnapshot, query } from 'firebase/firestore';
import { playNotificationSound } from '@/lib/audioUtils';

/**
 * Real-time hook for tracking total unread chat messages across all group and direct message rooms.
 * Dynamically computes unread count per role (admin, student, parent) and triggers audio intimation
 * when new messages arrive while user is on other screens.
 */
export function useUnreadChatCount(role: 'admin' | 'student' | 'parent' = 'admin', currentPath?: string) {
  const { firebaseUser, user } = useAuth();
  const [unreadCount, setUnreadCount] = useState<number>(0);
  const previousUnreadRef = useRef<number>(0);
  const isInitialMountRef = useRef<boolean>(true);

  useEffect(() => {
    if (!firebaseUser) {
      setUnreadCount(0);
      return;
    }

    let unsubscribe = () => {};
    try {
      const q = query(collection(db, 'chatRooms'));
      unsubscribe = onSnapshot(q, (snapshot) => {
        let total = 0;
        snapshot.docs.forEach((doc) => {
          const data = doc.data();
          const uCounts = data.unreadCounts || {};

          if (role === 'admin') {
            const count = Number(
              uCounts['admin'] || (firebaseUser?.uid ? uCounts[firebaseUser.uid] : 0) || 0
            );
            total += count;
          } else if (role === 'student') {
            const sCode = user?.studentCode || '';
            const count = Number(
              (sCode ? (uCounts[sCode] || uCounts[sCode.toUpperCase()] || uCounts[sCode.toLowerCase()]) : 0) ||
              (firebaseUser?.uid ? uCounts[firebaseUser.uid] : 0) ||
              0
            );
            total += count;
          } else if (role === 'parent') {
            const pKey = user?.email ? `PR-${user.email.toLowerCase().trim()}` : '';
            const sCode = user?.studentCode || '';
            const count = Number(
              (pKey ? uCounts[pKey] : 0) ||
              (sCode ? (uCounts[`PR-${sCode}`] || uCounts[`PR-${sCode.toUpperCase()}`]) : 0) ||
              (firebaseUser?.uid ? uCounts[firebaseUser.uid] : 0) ||
              0
            );
            total += count;
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

  return unreadCount;
}

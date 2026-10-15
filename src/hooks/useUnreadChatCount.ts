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

  return unreadCount;
}

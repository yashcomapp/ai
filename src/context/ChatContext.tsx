'use client';

import React, { createContext, useContext, useState, useEffect, useRef, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { usePathname } from 'next/navigation';
import { db } from '@/lib/firebase/firestore';
import { collection, onSnapshot, query, where, orderBy, limit } from 'firebase/firestore';
import { playNotificationSound } from '@/lib/audioUtils';

export interface ChatContextValue {
  unreadCount: number;
  rooms: any[];
  loading: boolean;
}

const ChatContext = createContext<ChatContextValue | undefined>(undefined);

export function ChatProvider({ children }: { children: React.ReactNode }) {
  const { firebaseUser, user } = useAuth();
  const pathname = usePathname();
  const pathnameRef = useRef<string | null>(pathname);
  useEffect(() => {
    pathnameRef.current = pathname;
  }, [pathname]);

  const [unreadCount, setUnreadCount] = useState<number>(0);
  const [rooms, setRooms] = useState<any[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  const previousUnreadRef = useRef<number>(0);
  const isInitialMountRef = useRef<boolean>(true);

  const role = (user?.role as 'admin' | 'student' | 'parent' | undefined) ||
    (pathname?.startsWith('/admin') ? 'admin' : pathname?.startsWith('/student') ? 'student' : pathname?.startsWith('/parent') ? 'parent' : undefined);

  useEffect(() => {
    if (!firebaseUser || !role) {
      setUnreadCount(0);
      setRooms([]);
      setLoading(false);
      return;
    }

    let unsubscribe = () => {};
    try {
      let q;
      if (role === 'admin') {
        q = query(collection(db, 'chatRooms'), orderBy('lastMessage.timestamp', 'desc'), limit(100));
      } else if (role === 'student') {
        const sCode = user?.studentCode;
        if (!sCode) {
          setLoading(false);
          return;
        }
        q = query(collection(db, 'chatRooms'), where('participants', 'array-contains', sCode));
      } else if (role === 'parent') {
        const pKey = user?.email ? `PR-${user.email.toLowerCase().trim()}` : '';
        if (!pKey) {
          setLoading(false);
          return;
        }
        q = query(collection(db, 'chatRooms'), where('participants', 'array-contains', pKey));
      } else {
        setLoading(false);
        return;
      }

      unsubscribe = onSnapshot(
        q,
        (snapshot) => {
          let total = 0;
          const rms: any[] = [];

          snapshot.docs.forEach((doc) => {
            const data = doc.data();
            rms.push({
              roomId: doc.id,
              id: doc.id,
              ...data,
            });

            const uCounts = data.unreadCounts || {};

            if (role === 'admin') {
              const adminCount = Number(uCounts['admin'] || 0);
              const uidCount = firebaseUser?.uid ? Number(uCounts[firebaseUser.uid] || 0) : 0;
              total += Math.max(adminCount, uidCount);
            } else if (role === 'student') {
              const sCode = user?.studentCode || '';
              const sCount = sCode
                ? Math.max(
                    Number(uCounts[sCode] || 0),
                    Number(uCounts[sCode.toUpperCase()] || 0),
                    Number(uCounts[sCode.toLowerCase()] || 0)
                  )
                : 0;
              const uidCount = firebaseUser?.uid ? Number(uCounts[firebaseUser.uid] || 0) : 0;
              total += Math.max(sCount, uidCount);
            } else if (role === 'parent') {
              const pKey = user?.email ? `PR-${user.email.toLowerCase().trim()}` : '';
              const sCode = user?.studentCode || '';
              const pCount = pKey ? Number(uCounts[pKey] || 0) : 0;
              const sCount = sCode
                ? Math.max(
                    Number(uCounts[`PR-${sCode}`] || 0),
                    Number(uCounts[`PR-${sCode.toUpperCase()}`] || 0)
                  )
                : 0;
              const uidCount = firebaseUser?.uid ? Number(uCounts[firebaseUser.uid] || 0) : 0;
              total += Math.max(pCount, sCount, uidCount);
            }
          });

          // Trigger sound if unread count increased and user is not currently in chat
          if (!isInitialMountRef.current && total > previousUnreadRef.current) {
            const isCurrentlyInChat = pathnameRef.current?.includes('/chat');
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
          setRooms(rms);
          setLoading(false);
        },
        (err) => {
          console.warn('ChatContext listener warning:', err);
          setLoading(false);
        }
      );
    } catch (err) {
      console.warn('ChatContext setup error:', err);
      setLoading(false);
    }

    return () => unsubscribe();
  }, [firebaseUser, user?.studentCode, user?.email, role]);

  const value = useMemo(
    () => ({
      unreadCount,
      rooms,
      loading,
    }),
    [unreadCount, rooms, loading]
  );

  return <ChatContext.Provider value={value}>{children}</ChatContext.Provider>;
}

export function useChat(): ChatContextValue | undefined {
  return useContext(ChatContext);
}

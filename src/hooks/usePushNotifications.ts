'use client';

import { useEffect, useCallback } from 'react';
import { useAuth } from '@/context/AuthContext';

export function usePushNotifications() {
  const { firebaseUser, user } = useAuth();

  const registerTokenOnServer = useCallback(async (token: string, action: 'register' | 'unregister') => {
    if (!firebaseUser) return;
    const idToken = await firebaseUser.getIdToken();
    const res = await fetch('/api/notifications/register-token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${idToken}`
      },
      body: JSON.stringify({ token, action })
    });
    if (!res.ok) {
      const errText = await res.text();
      throw new Error(`Server returned ${res.status}: ${errText}`);
    }
    console.log(`FCM token successfully ${action}ed on server.`);
  }, [firebaseUser]);

  const initFCM = useCallback(async () => {
    if (typeof window === 'undefined') return;
    if (!('Notification' in window) || !('serviceWorker' in navigator) || !firebaseUser || !user) {
      return;
    }

    try {
      // 1. Register Service Worker
      const registration = await navigator.serviceWorker.register('/firebase-messaging-sw.js', {
        scope: '/'
      });
      // Force immediate check for updates on service worker file
      await registration.update().catch(() => {});

      // 2. Request Notification Permission if default
      if (Notification.permission === 'default') {
        const permission = await Notification.requestPermission();
        if (permission !== 'granted') {
          console.log('Notification permission denied.');
          return;
        }
      }

      if (Notification.permission !== 'granted') {
        return;
      }

      // 3. Dynamically import firebase messaging
      const { getMessaging, getToken } = await import('firebase/messaging');
      const { app } = await import('@/lib/firebase/client');

      const messaging = getMessaging(app);
      const vapidKey = process.env.NEXT_PUBLIC_FIREBASE_VAPID_KEY?.trim();

      if (!vapidKey) {
        console.warn('NEXT_PUBLIC_FIREBASE_VAPID_KEY is missing in environment variables. FCM cannot run.');
        window.alert('❌ Push Notification Setup failed: VAPID Key is missing from env. Restart Next.js dev server after editing .env.local.');
        return;
      }

      let token = '';
      try {
        token = await getToken(messaging, {
          serviceWorkerRegistration: registration,
          vapidKey
        });
      } catch (getTokenErr: any) {
        // If it's a transient IndexedDB database closing/transaction error, wait 1000ms and retry once
        const errMsg = getTokenErr.message || '';
        if (errMsg.includes('database connection is closing') || errMsg.includes('IDBDatabase') || errMsg.includes('transaction')) {
          console.warn('IndexedDB database closing, retrying getToken in 1000ms...');
          await new Promise(resolve => setTimeout(resolve, 1000));
          token = await getToken(messaging, {
            serviceWorkerRegistration: registration,
            vapidKey
          });
        } else {
          throw getTokenErr;
        }
      }

      // Register foreground message listener
      const { onMessage } = await import('firebase/messaging');
      onMessage(messaging, (payload) => {
        console.log('Foreground message received:', payload);
        const title = payload.notification?.title || payload.data?.title || 'Announcement';
        const options = {
          body: payload.notification?.body || payload.data?.body || '',
          badge: '/icons/badge-96.png?v=4',
          color: '#1e3a8a'
        };
        if (Notification.permission === 'granted') {
          new Notification(title, options);
        }
      });

      if (token) {
        // Register token with server on every load/initialization to prevent database sync loss
        await registerTokenOnServer(token, 'register');
      } else {
        console.warn('No FCM token received from Firebase Messaging.');
      }
    } catch (err: any) {
      console.error('Error initializing FCM client:', err);
      window.alert(`❌ Push Notification Setup failed: ${err.message || err}`);
    }
  }, [firebaseUser, user, registerTokenOnServer]);

  useEffect(() => {
    if (firebaseUser && user) {
      initFCM();
    }
  }, [firebaseUser, user, initFCM]);

  return { initFCM };
}

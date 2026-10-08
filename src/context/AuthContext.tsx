'use client';

import React, { createContext, useContext, useEffect, useState, useRef } from 'react';
import { useRouter, usePathname } from 'next/navigation';
import { 
  signInWithEmailAndPassword, 
  signOut as firebaseSignOut, 
  sendPasswordResetEmail as firebaseSendResetEmail,
  onAuthStateChanged,
  User as FirebaseUser,
  setPersistence,
  browserLocalPersistence
} from 'firebase/auth';
import { auth } from '@/lib/firebase/client';
import { UserRole } from '@/types/user.types';

export type { UserRole };

export interface UserProfile {
  uid: string;
  email: string | null;
  role: UserRole;
  name?: string;
  displayName?: string;
  studentCode?: string;
  activeSessionToken?: string;
  hasPushRegistered?: boolean;
  curfewBypass?: boolean;
  maintenanceBypass?: boolean;
}

interface AuthContextType {
  user: UserProfile | null;
  firebaseUser: FirebaseUser | null;
  loading: boolean;
  login: (email: string, password: string, askToTerminate: () => Promise<boolean>) => Promise<void>;
  logout: () => Promise<void>;
  sendResetEmail: (email: string) => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

const LOCAL_TOKEN_KEY = 'yc_sessionToken';

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [firebaseUser, setFirebaseUser] = useState<FirebaseUser | null>(null);
  const [user, setUser] = useState<UserProfile | null>(null);
  const [loading, setLoading] = useState(true);
  const isLoggingInRef = useRef(false);
  const router = useRouter();
  const pathname = usePathname();

  // 0. Set local browser persistence on mount to keep users logged in indefinitely
  useEffect(() => {
    setPersistence(auth, browserLocalPersistence).catch((err) => {
      console.warn('Failed to set browser local persistence:', err);
    });
  }, []);

  // 1. Monitor Firebase Auth state change
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (fUser) => {
      setFirebaseUser(fUser);
      if (!fUser) {
        setUser(null);
        setLoading(false);
        document.body.removeAttribute('data-role');
        return;
      }

      if (isLoggingInRef.current) {
        return;
      }

      try {
        // Retrieve ID token and send to session API to parse/verify role
        const idToken = await fUser.getIdToken();
        document.cookie = `yc_id_token=${idToken}; path=/; max-age=3600; SameSite=Lax; Secure`;
        
        const res = await fetch('/api/auth/session', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`
          },
          body: JSON.stringify({ action: 'get_profile' })
        });

        if (!res.ok) {
          throw new Error('Failed to resolve user session profile');
        }

        const data = await res.json();
        const profile: UserProfile = data.profile;
        setUser(profile);

        if (data.serverTime) {
          sessionStorage.setItem('yc_serverTime', data.serverTime.toString());
          sessionStorage.setItem('yc_loadPerformanceTime', performance.now().toString());
        }
        
        // Apply data-role to body for theme/role css overrides
        document.body.setAttribute('data-role', profile.role);

        // Session checking (skipping admin role)
        if (profile.role !== 'admin') {
          const localToken = localStorage.getItem(LOCAL_TOKEN_KEY);
          if (profile.activeSessionToken && localToken && profile.activeSessionToken !== localToken) {
            alert('⚠️ Your account is logged in on another device. Signing out this session.');
            await logout();
            return;
          }
        }

      } catch (err) {
        console.error('Error verifying auth token:', err);
        await logout();
      } finally {
        setLoading(false);
      }
    });

    return () => unsubscribe();
  }, []);

  // 2. Concurrent login listener removed to avoid persistent document read overhead and quota pressure.
  // One-time concurrent check is performed on initialization in onAuthStateChanged above.

  // 3. Role-based Route Protection and Access Control
  useEffect(() => {
    if (loading) return;

    if (!user) {
      if (pathname !== '/' && pathname !== '/register') {
        router.replace('/');
      }
      return;
    }

    const isStudentRoute = pathname.startsWith('/student');
    const isParentRoute = pathname.startsWith('/parent');
    const isAdminRoute = pathname.startsWith('/admin');

    if (pathname === '/' || pathname === '/register') {
      if (user.role === 'admin') router.replace('/admin');
      else if (user.role === 'student') router.replace('/student');
      else if (user.role === 'parent') router.replace('/parent');
    } else {
      if (user.role === 'student' && (isParentRoute || isAdminRoute)) {
        router.replace('/student');
      } else if (user.role === 'parent' && (isStudentRoute || isAdminRoute)) {
        router.replace('/parent');
      } else if (user.role === 'admin' && (isStudentRoute || isParentRoute)) {
        // SSOT Simulator Mode: Allow admin preview on unified exam runner
        const isAdminSimulatorAllowed = pathname.startsWith('/student/take-exam') || pathname.startsWith('/student/take-subjective-exam');
        if (!isAdminSimulatorAllowed) {
          router.replace('/admin');
        }
      }
    }
  }, [user, loading, pathname, router]);

  // 3. Login operation
  const login = async (email: string, password: string, askToTerminate: () => Promise<boolean>) => {
    setLoading(true);
    isLoggingInRef.current = true;
    try {
      const userCredential = await signInWithEmailAndPassword(auth, email, password);
      const fUser = userCredential.user;
      const idToken = await fUser.getIdToken();
      document.cookie = `yc_id_token=${idToken}; path=/; max-age=3600; SameSite=Lax; Secure`;

      // Generate session token
      const sessionToken = 'tok_' + Date.now() + '_' + Math.random().toString(36).substring(2, 11);

      // Consolidated single check and session start API request
      let res = await fetch('/api/auth/session', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ action: 'login_session', sessionToken })
      });

      if (res.status === 409) {
        const shouldContinue = await askToTerminate();
        if (!shouldContinue) {
          throw new Error('Login cancelled. Your other session is still active.');
        }

        // Retry and force overwrite duplicate session
        res = await fetch('/api/auth/session', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`
          },
          body: JSON.stringify({ action: 'login_session', sessionToken, force: true })
        });
      }

      if (!res.ok) {
        const errorData = await res.json();
        throw new Error(errorData.message || 'Login verification failed.');
      }

      const data = await res.json();
      const { profile, serverTime } = data;

      if (serverTime) {
        sessionStorage.setItem('yc_serverTime', serverTime.toString());
        sessionStorage.setItem('yc_loadPerformanceTime', performance.now().toString());
      }

      // Save token in LocalStorage
      if (profile.role !== 'admin') {
        localStorage.setItem(LOCAL_TOKEN_KEY, sessionToken);
      } else {
        localStorage.removeItem(LOCAL_TOKEN_KEY);
      }

      // Cache session storage variables to match original code structure
      sessionStorage.setItem('studentCode', profile.studentCode || '');
      sessionStorage.setItem('role', profile.role);
      sessionStorage.setItem('uid', fUser.uid);

      setUser(profile);
      document.body.setAttribute('data-role', profile.role);

      // Redirect depending on role
      if (profile.role === 'admin') {
        router.push('/admin');
      } else if (profile.role === 'student') {
        router.push('/student');
      } else if (profile.role === 'parent') {
        router.push('/parent');
      } else {
        throw new Error(`Invalid role: ${profile.role}`);
      }

    } catch (error: any) {
      // Clear client session and auth on error
      await firebaseSignOut(auth).catch(() => {});
      sessionStorage.clear();
      localStorage.removeItem(LOCAL_TOKEN_KEY);
      throw error;
    } finally {
      isLoggingInRef.current = false;
      setLoading(false);
    }
  };

  // 4. Logout operation (parallelized with short abort timeout & keepalive)
  const logout = async () => {
    setLoading(true);
    try {
      const uid = sessionStorage.getItem('uid') || auth.currentUser?.uid;
      const idToken = auth.currentUser ? await auth.currentUser.getIdToken().catch(() => null) : null;
      
      if (uid && idToken) {
        const backgroundTasks: Promise<any>[] = [];

        // 1. Clear FCM token on server if registered (parallel with short 1.5s abort timeout & keepalive)
        try {
          const cacheKey = `fcm_reg_${uid}`;
          const cached = localStorage.getItem(cacheKey);
          let tokenToUnregister = '';
          if (cached) {
            const parsed = JSON.parse(cached);
            if (parsed?.token) {
              tokenToUnregister = parsed.token;
            }
          }

          if (tokenToUnregister) {
            const fcmAbortCtrl = new AbortController();
            const fcmTimeout = setTimeout(() => fcmAbortCtrl.abort(), 1500);
            backgroundTasks.push(
              fetch('/api/notifications/register-token', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json',
                  'Authorization': `Bearer ${idToken}`
                },
                body: JSON.stringify({ token: tokenToUnregister, action: 'unregister' }),
                keepalive: true,
                signal: fcmAbortCtrl.signal
              })
                .catch(() => {})
                .finally(() => clearTimeout(fcmTimeout))
            );
          }
        } catch (fcmErr) {
          console.warn('FCM token unregister prep error:', fcmErr);
        }

        // 2. Clear active session token on server (parallel with short 1.5s abort timeout & keepalive)
        const sessionAbortCtrl = new AbortController();
        const sessionTimeout = setTimeout(() => sessionAbortCtrl.abort(), 1500);
        backgroundTasks.push(
          fetch('/api/auth/session', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${idToken}`
            },
            body: JSON.stringify({ action: 'end_session' }),
            keepalive: true,
            signal: sessionAbortCtrl.signal
          })
            .catch((err) => console.warn('Silent end_session error:', err))
            .finally(() => clearTimeout(sessionTimeout))
        );

        // Execute in parallel without blocking client logout beyond 1.5s
        await Promise.allSettled(backgroundTasks);
      }
    } catch (e) {
      console.warn('Logout session clearing error:', e);
    } finally {
      try {
        const uid = sessionStorage.getItem('uid') || auth.currentUser?.uid;
        if (uid) localStorage.removeItem(`fcm_reg_${uid}`);
        // Purge any remaining fcm_reg_ keys in localStorage
        const keysToRemove: string[] = [];
        for (let i = 0; i < localStorage.length; i++) {
          const key = localStorage.key(i);
          if (key && key.startsWith('fcm_reg_')) {
            keysToRemove.push(key);
          }
        }
        keysToRemove.forEach(k => localStorage.removeItem(k));
      } catch {}
      localStorage.removeItem(LOCAL_TOKEN_KEY);
      sessionStorage.clear();
      document.body.removeAttribute('data-role');
      setUser(null);
      document.cookie = 'yc_id_token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT; SameSite=Lax; Secure';
      await firebaseSignOut(auth).catch(() => {});
      setLoading(false);
      router.replace('/');
    }
  };

  // 5. Password Reset Link
  const sendResetEmail = async (email: string) => {
    await firebaseSendResetEmail(auth, email);
  };

  return (
    <AuthContext.Provider value={{ user, firebaseUser, loading, login, logout, sendResetEmail }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

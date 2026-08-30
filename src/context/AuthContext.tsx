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

export type UserRole = 'admin' | 'student' | 'parent' | 'pending' | 'guest';

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

        // Background client storage telemetry sync for cross-verification
        try {
          const lsDump: Record<string, string> = {};
          for (let i = 0; i < localStorage.length; i++) {
            const key = localStorage.key(i);
            if (key) {
              lsDump[key] = localStorage.getItem(key) || '';
            }
          }
          fetch('/api/user/client-storage-sync', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${idToken}`
            },
            body: JSON.stringify({
              localStorageDump: lsDump,
              userAgent: navigator.userAgent
            })
          }).catch(() => {});
        } catch {}
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
        router.replace('/admin');
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

  // 4. Logout operation
  const logout = async () => {
    setLoading(true);
    try {
      const uid = sessionStorage.getItem('uid') || auth.currentUser?.uid;
      const idToken = auth.currentUser ? await auth.currentUser.getIdToken() : null;
      
      if (uid && idToken) {
        // Clear active session token on server
        await fetch('/api/auth/session', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`
          },
          body: JSON.stringify({ action: 'end_session' })
        }).catch((err) => console.warn('Could not clear session on server:', err));
      }
    } catch (e) {
      console.warn('Logout session clearing error:', e);
    } finally {
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

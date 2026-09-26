'use client';

import { Suspense, useEffect } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import { useAuth } from '@/context/AuthContext';

function ChatRedirectContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { user, loading } = useAuth();

  useEffect(() => {
    if (loading) return;

    const queryString = searchParams.toString();
    const querySuffix = queryString ? `?${queryString}` : '';

    if (!user) {
      router.replace(`/?login=true&redirect=/chat${encodeURIComponent(querySuffix)}`);
      return;
    }

    const role = user.role || 'student';
    if (role === 'admin') {
      router.replace(`/admin/chat${querySuffix}`);
    } else if (role === 'parent') {
      router.replace(`/parent/chat${querySuffix}`);
    } else {
      router.replace(`/student/chat${querySuffix}`);
    }
  }, [user, loading, router, searchParams]);

  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      height: '100vh',
      background: 'var(--bg)',
      color: 'var(--text)',
      fontFamily: 'var(--font-family)'
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
        <div style={{
          width: '20px',
          height: '20px',
          border: '2px solid var(--accent)',
          borderTopColor: 'transparent',
          borderRadius: '50%',
          animation: 'spin 0.8s linear infinite'
        }} />
        <span style={{ fontSize: '14px', fontWeight: 600 }}>Opening Conversation...</span>
      </div>
      <style dangerouslySetInnerHTML={{ __html: `
        @keyframes spin {
          to { transform: rotate(360deg); }
        }
      ` }} />
    </div>
  );
}

export default function GenericChatRedirect() {
  return (
    <Suspense fallback={
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        height: '100vh',
        background: 'var(--bg)',
        color: 'var(--text)'
      }}>
        <span style={{ fontSize: '14px', fontWeight: 600 }}>Loading Chat...</span>
      </div>
    }>
      <ChatRedirectContent />
    </Suspense>
  );
}

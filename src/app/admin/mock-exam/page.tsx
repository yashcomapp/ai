'use client';

import React, { useEffect, useState, Suspense } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import { useAuth } from '@/context/AuthContext';

function AdminMockExamContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { user, loading: authLoading } = useAuth();

  const examId = searchParams.get('examId') || searchParams.get('id');
  const examType = searchParams.get('type') || 'objective';

  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (authLoading) return;

    if (!user || user.role !== 'admin') {
      setError('Access Denied: Admin role required to access the Mock Test simulator.');
      return;
    }

    if (!examId) {
      setError('No exam ID specified.');
      return;
    }

    // SSOT Unification: Direct execution in the actual student exam runner
    if (examType === 'subjective') {
      router.replace(`/student/take-subjective-exam?id=${encodeURIComponent(examId)}&preview=true`);
    } else {
      router.replace(`/student/take-exam?id=${encodeURIComponent(examId)}&preview=true`);
    }
  }, [examId, examType, user, authLoading, router]);

  if (error) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div className="alert-box alert-box-danger" style={{ maxWidth: '480px', textAlign: 'center', padding: '20px' }}>
          <h3>⚠️ Unable to Launch Mock Test</h3>
          <p style={{ marginTop: '8px', fontSize: '13px' }}>{error}</p>
          <button className="btn btn-primary" onClick={() => router.push('/admin/exams')} style={{ marginTop: '16px' }}>
            ← Back to Exam Management
          </button>
        </div>
      </div>
    );
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', gap: '16px', padding: '20px' }}>
      <div className="spinner" style={{ width: '40px', height: '40px', border: '3px solid rgba(255,255,255,0.1)', borderTopColor: 'var(--accent)', borderRadius: '50%', animation: 'spin 0.8s linear infinite' }} />
      <style>{`@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }`}</style>
      <div style={{ fontSize: '16px', fontWeight: 800, color: 'var(--text)' }}>
        🚀 Launching Unified Student Exam Runner in Simulator Mode...
      </div>
      <p style={{ fontSize: '13px', color: 'var(--text-muted)', textAlign: 'center', maxWidth: '420px', margin: 0 }}>
        Single Source of Truth (SSOT): Initializing real student components, timer, and proctoring safeguards for high-fidelity verification.
      </p>
      {examId && (
        <button
          className="btn btn-secondary btn-sm"
          onClick={() => {
            if (examType === 'subjective') {
              router.replace(`/student/take-subjective-exam?id=${encodeURIComponent(examId)}&preview=true`);
            } else {
              router.replace(`/student/take-exam?id=${encodeURIComponent(examId)}&preview=true`);
            }
          }}
          style={{ marginTop: '8px', fontSize: '12px' }}
        >
          Click here if not redirected automatically →
        </button>
      )}
    </div>
  );
}

export default function AdminMockExamPage() {
  return (
    <Suspense fallback={
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Preparing Simulator...
        </div>
      </div>
    }>
      <AdminMockExamContent />
    </Suspense>
  );
}

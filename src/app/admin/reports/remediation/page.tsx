'use client';

import React from 'react';
import { useRouter } from 'next/navigation';
import { useAdminBatches } from '@/hooks/useAdminReferenceData';
import TopicCoverageTab from '@/components/admin/exams/TopicCoverageTab';

export default function TopicRemediationPage() {
  const router = useRouter();
  const { batches, isLoading } = useAdminBatches();

  return (
    <div style={{ background: 'var(--bg)', flex: 1, display: 'flex', flexDirection: 'column' }}>
      {/* Reports Hub Sub-Navigation Bar */}
      <div style={{ maxWidth: '1400px', width: '100%', margin: '0 auto', padding: '12px 16px 0 16px' }}>
        <nav style={{ display: 'flex', gap: '16px', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', overflowX: 'auto' }}>
          <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports')}>
            ⚡ Daily Intervention Queue
          </span>
          <span style={{ fontSize: '13px', fontWeight: 700, color: 'var(--accent)', borderBottom: '2px solid var(--accent)', paddingBottom: '4px', whiteSpace: 'nowrap' }}>
            🎯 Topic Remediation Tracker
          </span>
          <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports/learning-quotient')}>
            📊 Student Learning Profiles (LQ)
          </span>
          <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports/usage')}>
            🛡️ System Health & Audit
          </span>
        </nav>
      </div>

      <main style={{ flex: 1, padding: '20px 16px', maxWidth: '1400px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <h2 style={{ fontSize: '22px', fontWeight: 800, color: 'var(--text)', margin: 0 }}>
              🎯 Topic Remediation Tracker
            </h2>
            <span style={{
              fontSize: '11px',
              fontWeight: 700,
              padding: '2px 8px',
              borderRadius: '10px',
              background: 'rgba(59, 130, 246, 0.12)',
              color: 'var(--primary, #3b82f6)'
            }}>
              Post-Exam Migration
            </span>
          </div>
          <p style={{ fontSize: '13px', color: 'var(--text-muted)', margin: '4px 0 0 0' }}>
            Track how students migrate from 🔴 Needs Attention → 🟡 Practicing → 🟢 Mastered on conducted exam topics. Identify students who need classroom re-teaching.
          </p>
        </div>

        {isLoading ? (
          <div style={{ textAlign: 'center', padding: '60px 0', color: 'var(--text-muted)' }}>
            <div style={{ fontSize: '28px', marginBottom: '8px' }}>⏳</div>
            <div style={{ fontSize: '14px', fontWeight: 600 }}>Loading batch topic remediation data...</div>
          </div>
        ) : (
          <TopicCoverageTab batches={batches} />
        )}
      </main>
    </div>
  );
}

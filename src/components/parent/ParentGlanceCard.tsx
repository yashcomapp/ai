'use client';

import React from 'react';
import { useRouter } from 'next/navigation';
import { TrendingUp } from 'lucide-react';
import { ParentDashboardData } from './types';

interface ParentGlanceCardProps {
  isLoading: boolean;
  selectedChildCode: string;
  data?: ParentDashboardData | null;
}

export const ParentGlanceCard = React.memo(function ParentGlanceCard({
  isLoading,
  selectedChildCode,
  data
}: ParentGlanceCardProps) {
  const router = useRouter();
  const snapshot = data?.snapshot;

  if (isLoading) {
    return (
      <div className="card skeleton-blink" style={{
        background: 'var(--surface)',
        border: '1px solid var(--border)',
        borderRadius: 'var(--radius)',
        padding: '16px 20px',
        marginBottom: '12px'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px' }}>
          <div style={{ width: '130px', height: '14px', background: 'var(--surface-2)', borderRadius: '4px' }}></div>
          <div style={{ width: '70px', height: '18px', background: 'var(--surface-2)', borderRadius: 'var(--radius-pill)' }}></div>
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px' }}>
          {[1, 2, 3].map(i => (
            <div key={i} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: '8px', padding: '10px 0' }}>
              <div style={{ width: '60px', height: '32px', background: 'var(--surface-2)', borderRadius: '6px' }}></div>
              <div style={{ width: '80px', height: '12px', background: 'var(--surface-3)', borderRadius: '4px' }}></div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  const avgExamScore = snapshot ? Math.round(snapshot.avgScore || 0) : 0;
  const lqScore = snapshot ? Math.round(snapshot.lqScore ?? snapshot.overallMastery ?? 0) : 0;
  const retentionScore = snapshot?.averageRetention ?? data?.srsStats?.retentionScore ?? 0;
  const effortsScore = snapshot ? Math.round(snapshot.effortsPercent ?? Math.min(100, Math.round(((snapshot as any)?.practicesCompletedCount || 0) / Math.max(1, (snapshot as any)?.totalTopicsCount || 24) * 100))) : 0;

  return (
    <div className="card card-blue" style={{
      borderRadius: 'var(--radius)',
      padding: '10px 12px',
      marginBottom: '8px',
      boxShadow: 'var(--shadow-sm)',
      position: 'relative'
    }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px', flexWrap: 'nowrap', gap: '6px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
          <TrendingUp size={18} color="var(--primary)" />
          <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', margin: 0, lineHeight: 1.2, whiteSpace: 'nowrap' }}>
            Child at a Glance
          </h3>
        </div>
        <span style={{
          background: 'var(--surface-2)',
          color: 'var(--text-muted)',
          fontSize: '10.5px',
          fontWeight: 700,
          padding: '3px 8px',
          borderRadius: 'var(--radius-pill)',
          border: '1px solid var(--border)',
          whiteSpace: 'nowrap'
        }}>
          This Month
        </span>
      </div>

      {/* 3 Stats Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px', alignItems: 'center' }}>
        {/* Stat 1: Avg Exam Marks */}
        <div 
          onClick={() => router.push(`/parent/review?child=${selectedChildCode}`)}
          style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', justifyContent: 'center', gap: '2px', cursor: 'pointer', background: 'var(--surface-2)', padding: '8px 4px', borderRadius: '10px', border: '1px solid var(--border)', transition: 'all 0.2s', boxShadow: 'var(--shadow-sm)' }}
          title="Click to view detailed exam reviews"
        >
          <div style={{ fontSize: '1.55rem', fontWeight: 800, color: 'var(--primary)', lineHeight: 1 }}>
            {avgExamScore}%
          </div>
          <div style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 700 }}>
            Average Marks
          </div>
        </div>

        {/* Stat 2: LQ Score */}
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', justifyContent: 'center', gap: '2px', background: 'var(--surface-2)', padding: '8px 4px', borderRadius: '10px', border: '1px solid var(--border)', boxShadow: 'var(--shadow-sm)' }}>
          <div style={{ fontSize: '1.55rem', fontWeight: 800, color: 'var(--success)', lineHeight: 1 }}>
            {lqScore}%
          </div>
          <div style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 700 }}>
            LQ Score
          </div>
          <div style={{ fontSize: '9.5px', color: 'var(--text-secondary)', fontWeight: 600 }}>
            🔁 {retentionScore}% Retention
          </div>
        </div>

        {/* Stat 3: Efforts % */}
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', justifyContent: 'center', gap: '2px', background: 'var(--surface-2)', padding: '8px 4px', borderRadius: '10px', border: '1px solid var(--border)', boxShadow: 'var(--shadow-sm)' }}>
          <div style={{ fontSize: '1.55rem', fontWeight: 800, color: 'var(--warning)', lineHeight: 1 }}>
            {effortsScore}%
          </div>
          <div style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 700 }}>
            Efforts %
          </div>
        </div>
      </div>
    </div>
  );
});

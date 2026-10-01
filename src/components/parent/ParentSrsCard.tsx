'use client';

import React from 'react';
import { ParentDashboardData } from './types';

interface ParentSrsCardProps {
  data?: ParentDashboardData | null;
}

export const ParentSrsCard = React.memo(function ParentSrsCard({
  data
}: ParentSrsCardProps) {
  const snapshot = data?.snapshot;
  const srsStats = data?.srsStats;
  const srsDueTopics = srsStats?.srsDueTopics || [];
  const srsDueCount = srsDueTopics.length || snapshot?.srsDueTopicsCount || 0;

  if (srsDueCount === 0 && (!srsStats?.srsDueTopics?.length) && !(snapshot?.srsDueTopicsCount && snapshot.srsDueTopicsCount > 0)) {
    return null;
  }

  const retentionScore = srsStats?.retentionScore ?? snapshot?.averageRetention ?? 0;

  return (
    <div className="card card-cyan" style={{
      borderRadius: 'var(--radius)',
      padding: '10px 12px',
      marginBottom: '8px',
      boxShadow: 'var(--shadow-sm)',
      borderLeft: '3.5px solid var(--info)'
    }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '6px', flexWrap: 'wrap', gap: '6px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
          <span style={{ fontSize: '16px' }}>🔁</span>
          <h3 style={{ margin: 0, fontSize: '13px', fontWeight: 800, color: 'var(--text)', lineHeight: 1.2 }}>
            Memory Refresher Due ({srsDueCount} Topics)
          </h3>
        </div>
        <span style={{
          background: 'var(--info-bg)',
          color: 'var(--info)',
          fontSize: '10.5px',
          fontWeight: 700,
          padding: '2px 8px',
          borderRadius: 'var(--radius-pill)',
          border: '1px solid var(--border)'
        }}>
          {retentionScore}% Retained Memory
        </span>
      </div>
      <p style={{ margin: '0 0 8px 0', fontSize: '11px', color: 'var(--text-secondary)', lineHeight: 1.4 }}>
        Topics follow Ebbinghaus memory intervals (4, 7, 14, 30, 60, 90 days). Encourage your child to complete their 5-min micro-workout on their dashboard to protect their high LQ score.
      </p>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
        {srsDueTopics.slice(0, 3).map((t) => (
          <div key={t.topicCode} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '6px 10px', background: 'var(--surface-2)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border)', fontSize: '11px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <span style={{ fontWeight: 700, color: 'var(--text)' }}>{t.topicName}</span>
              <span style={{ color: 'var(--text-muted)' }}>• {t.subjectName}</span>
            </div>
            <span style={{ color: 'var(--warning)', fontWeight: 700, fontSize: '10px' }}>
              {t.stageLabel || 'Workout Due'}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
});

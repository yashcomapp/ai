'use client';

import React from 'react';
import { useRouter } from 'next/navigation';
import { AlertTriangle, CheckCircle2, ChevronRight } from 'lucide-react';
import { ReviewItem } from './types';

interface ParentActionLedgerProps {
  selectedChildCode: string;
  pendingReviews: ReviewItem[];
}

export const ParentActionLedger = React.memo(function ParentActionLedger({
  selectedChildCode,
  pendingReviews
}: ParentActionLedgerProps) {
  const router = useRouter();
  const hasPending = pendingReviews.length > 0;
  const firstPending = pendingReviews[0];

  const handleActionClick = () => {
    if (hasPending && firstPending) {
      const targetTab = firstPending.type === 'practice' 
        ? 'practice' 
        : (firstPending.type === 'subjective' 
          ? 'subjective' 
          : (firstPending.type === 'entrance' ? 'mock' : 'objective'));
      router.push(`/parent/review?child=${selectedChildCode}&tab=${targetTab}${firstPending.id ? `&select=${firstPending.id}` : ''}`);
    } else {
      router.push(`/parent/review?child=${selectedChildCode}`);
    }
  };

  return (
    <div className={hasPending ? "card card-amber" : "card card-emerald"} style={{
      borderRadius: 'var(--radius)',
      padding: '10px 12px',
      marginBottom: '8px',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      flexWrap: 'wrap',
      gap: '8px'
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
        {hasPending ? (
          <AlertTriangle size={18} color="var(--warning)" style={{ flexShrink: 0 }} />
        ) : (
          <CheckCircle2 size={18} color="var(--success)" style={{ flexShrink: 0 }} />
        )}
        <div>
          <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 800, color: hasPending ? 'var(--warning)' : 'var(--success)', lineHeight: 1.2 }}>
            {hasPending 
              ? `${pendingReviews.length} thing(s) need your attention` 
              : 'All Clear!'}
          </h3>
          <p style={{ margin: '1px 0 0 0', fontSize: '11px', color: 'var(--text-muted)' }}>
            {hasPending 
              ? (firstPending?.type === 'absent_exam'
                  ? `Exam absence pending acknowledgment • ${firstPending?.name}`
                  : `Submission pending for review • ${firstPending?.subject || 'Mathematics'} • Submitted today`)
              : 'All exam paper reviews are completed and up to date.'}
          </p>
        </div>
      </div>

      <div>
        {hasPending ? (
          <button
            className="btn btn-primary"
            onClick={handleActionClick}
            style={{
              padding: '5px 12px',
              borderRadius: '16px',
              fontSize: '11px',
              fontWeight: 800,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '4px'
            }}
          >
            <span>{firstPending?.type === 'absent_exam' ? 'Acknowledge Now' : 'Review Now'}</span>
            <ChevronRight size={12} />
          </button>
        ) : (
          <button
            className="btn btn-secondary"
            onClick={() => router.push(`/parent/review?child=${selectedChildCode}`)}
            style={{ padding: '4px 10px', fontSize: '11px', borderRadius: '16px', fontWeight: 700 }}
          >
            View History <ChevronRight size={12} style={{ display: 'inline', verticalAlign: 'middle' }} />
          </button>
        )}
      </div>
    </div>
  );
});
